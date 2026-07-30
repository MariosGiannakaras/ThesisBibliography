> Source: https://arxiv.org/pdf/2301.00858

Robust Average-Reward Markov Decision Processes 
Yue Wang,1 Alvaro Velasquez, 2 George Atia, 3 Ashley Prater-Bennette, 4 Shaofeng Zou 1 
1 University at Buffalo, The State University of New York 2 University of Colorado Boulder 
3 University of Central Florida 4 Air Force Research Laboratory 
ywang294@buffalo.com, alvaro.velasquez@colorado.edu, george.atia@ucf.edu, ashley.prater-bennette@us.af.mil, szou3@buffalo.edu 
Abstract 
In robust Markov decision processes (MDPs), the uncertainty in the transition kernel is addressed by finding a policy that optimizes the worst-case performance over an uncertainty set of MDPs. While much of the literature has focused on discounted MDPs, robust average-reward MDPs remain largely unexplored. In this paper, we focus on robust average-reward MDPs, where the goal is to find a policy that optimizes the worst-case average reward over an uncertainty set. We first take an approach that approximates average-reward MDPs using discounted MDPs. We prove that the robust discounted value function converges to the robust average-reward as the discount factor γ goes to 1, and moreover, when γ is large, any optimal policy of the robust discounted MDP is also an optimal policy of the robust average-reward. We further design a robust dynamic programming approach, and theoretically characterize its convergence to the optimum. Then, we investigate robust average-reward MDPs directly without using discounted MDPs as an intermediate step. We derive the robust Bellman equation for robust average-reward MDPs, prove that the optimal policy can be derived from its solution, and further design a robust relative value iteration algorithm that provably find its solution, or equivalently, the optimal robust policy. 
Introduction A Markov decision process (MDP) is an effective mathematical tool for sequential decision-making in stochastic environments (Derman 1970; Puterman 1994). Solving an MDP problem entails finding an optimal policy that maximizes a cumulative reward according to a given criterion. However, in practice there could exist a mismatch between the assumed MDP model and the underlying environment due to various factors, such as non-stationarity of the environment, modeling error, exogenous perturbation, partial observability, and adversarial attacks. The ensuing model mismatch could result in solution policies with poor performance. 
This challenge spurred noteworthy efforts on developing and analyzing a framework of robust MDPs e.g., (Bagnell, Ng, and Schneider 2001; Nilim and El Ghaoui 2004; Iyengar 2005). Rather than adopting a fixed MDP model, in the robust MDP setting, one seeks to optimize the worst-case performance over an uncertainty set of possible MDP models. The 
Copyright © 2023, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 
solution to the robust MDP problem provides performance guarantee for all uncertain MDP models, and is thus robust to the model mismatch. 
Robust MDP problems falling under different reward optimality criteria are fundamentally different. In robust discounted MDPs, the goal is to find a policy that maximizes the discounted cumulative reward in the worst case. In this setting, as the agent interacts with the environment, the reward received diminishes exponentially over time. Much of the prior work in the robust setting has focused on the discounted reward formulation. The model-based method, e.g., (Iyengar 2005; Nilim and El Ghaoui 2004; Bagnell, Ng, and Schneider 2001; Satia and Lave Jr 1973; Wiesemann, Kuhn, and Rustem 2013; Tamar, Mannor, and Xu 2014; Lim and Autef 2019; Xu and Mannor 2010; Yu and Xu 2015; Lim, Xu, and Mannor 2013), where information about the uncertainty set is assumed to be known to the learner, unveiled several fundamental characterizations of robust discounted MDPs. This was further extended to the more practical model-free setting in which only samples from a simulator (the centroid of the uncertainty set) are available to the learner. For example, the value-based method (Roy, Xu, and Pokutta 2017; Badrinath and Kalathil 2021; Wang and Zou 2021; Tessler, Efroni, and Mannor 2019; Zhou et al. 2021; Yang, Zhang, and Zhang 2021; Panaganti and Kalathil 2021; Goyal and Grand-Clement 2018; Kaufman and Schaefer 2013; Ho, Petrik, and Wiesemann 2018, 2021; Si et al. 2020) optimizes the worst-case performance using the robust value function as an intermediate step; on the other hand, the model-free policy-based method (Russel, Benosman, and Van Baar 2020; Derman, Geist, and Mannor 2021; Eysenbach and Levine 2021; Wang and Zou 2022) directly optimizes the policy and is thus scalable to large/continuous state and action spaces. 
Although discounted MDPs induce an elegant Bellman operator that is a contraction, and have been studied extensively, the policy obtained usually has poor long-term performance when a system operates for an extended period of time. When the discount factor is very close to 1, the agent may prefer to compare policies on the basis of their average expected reward instead of their expected total discounted reward, e.g., queueing control, inventory management in supply chains, scheduling automatic guided vehicles and applications in communication networks (Kober, Bagnell, and Peters 2013). Therefore, it is also important to optimize the long-term aver-
 
 
 
 
 
 
 
 
 
 
age performance of a system. However, robust MDPs under the average-reward crite-
rion are largely understudied. Compared to the discounted setting, the average-reward setting depends on the limiting behavior of the underlying stochastic process, and hence is markedly more intricate. A recognized instance of such intricacy concerns the one-to-one correspondence between the stationary policies and the limit points of state-action frequencies, which while true for discounted MDPs, breaks down under the average-reward criterion even in the non-robust setting except in some very special cases (Puterman 1994; Atia et al. 2021). This is largely due to dependence of the necessary conditions for establishing a contraction in averagereward settings on the graph structure of the MDP, versus the discounted-reward setting where it simply suffices to have a discount factor that is strictly less than one. Heretofore, only a handful of studies have considered average-reward MDPs in the robust setting. The first work by (Tewari and Bartlett 2007) considers robust average-reward MDPs under a specific finite interval uncertainty set, but their method is not easily applicable to other uncertainty sets. More recently, (Lim, Xu, and Mannor 2013) proposed an algorithm for robust average-reward MDPs under the `1 uncertainty set. However, obtaining fundamental characterizations of the problem and convergence guarantee remains elusive. 
Challenges and Contributions In this paper, we derive characterizations of robust averagereward MDPs with general uncertainty sets, and develop model-based approaches with provable theoretical guarantee. Our approach is fundamentally different from previous work on robust discounted MDPs, robust and non-robust averagereward MDPs. In particular, the key challenges and the main contributions are summarized below. 
 We characterize the limiting behavior of robust discounted value function as the discount factor γ → 1. For the standard non-robust setting and for a specific transition kernel, the discounted non-robust value function converges to the average-reward non-robust value function as γ → 1 (Puterman 1994). However, in the robust setting, we need to consider the worst-case limiting behavior under all possible transition kernels in the uncertainty set. Hence, the previous point-wise convergence result (Puterman 1994) cannot be directly applied. In (Tewari and Bartlett 2007), a finite interval uncertainty set is studied, where due to its special structure, the number of possible worst-case transition kernels of robust discounted MDPs is finite, and hence the order of min (over transition kernel) and limγ→1 can be exchanged, and therefore, the robust discounted value function converges to the robust average-reward value function. This result, however, does not hold for general uncertainty sets investigated in this paper. We first prove the uniform convergence of discounted non-robust value function to average-reward w.r.t. the transition kernels and policies. Based on this uniform convergence, we show the convergence of the robust discounted value function to the robust average-reward. This uniform convergence result is the first in the literature and is of key importance to motivate 
our algorithm design and to guarantee convergence to the optimal robust policy in the average-reward setting. 
 We design algorithms for robust policy evaluation and optimal control based on the limit method. Based on the uniform convergence, we then use robust discounted MDPs to approximate robust average-reward MDPs. We show that when γ is large, any optimal policy of the robust discounted MDP is also an optimal policy of the robust average-reward, and hence solves the robust optimal control problem in the average reward setting. This result is similar to the Black-well optimality (Blackwell 1962; Hordijk and Yushkevich 2002) for the non-robust setting, however, our proof is fundamentally different. Technically, the proof in (Blackwell 1962; Hordijk and Yushkevich 2002) is based on the fact that the difference between the discounted value functions of two policies is a rational function of the discount factor, which has a finite number of zeros. However, in the robust setting with a general uncertainty set, the difference is no longer a rational function due to the min over the transition kernel. We construct a novel proof based on the limiting behavior of robust discounted MDPs, and show that the (optimal) robust discounted value function converges to the (optimal) robust average-reward as γ → 1. Motivated by these insights, we then design our algorithms by applying a sequence of robust discounted Bellman operators while increasing the discount factor at a certain rate. We prove that our method can (i) evaluate the robust average-reward for a given policy and; (ii) find the optimal robust value function and, in turn, the optimal robust policy for general uncertainty sets. 
 We design a robust relative value iteration method without using the discounted MDPs as an intermediate step. We further pursue a direct approach that solves the robust average-reward MDPs without using the limit method, i.e., without using discounted MDPs as an intermediate step. We derive a robust Bellman equation for robust average-reward MDPs, and show that the pair of robust relative value function and robust average-reward is a solution to the robust Bellman equation under the average-reward setting. We further prove that if we can find any solution to the robust Bellman equation, then the optimal policy can be derived by a greedy approach. The problem hence can be equivalently solved by solving the robust Bellman equation. We then design a robust value iteration method which provably converges to the solution of the robust Bell-man equation, i.e., solve the optimal policy for the robust average-reward MDP problem. 
Related Work Robust discounted MDPs. Model-based methods for robust discounted MDPs were studied in (Iyengar 2005; Nilim and El Ghaoui 2004; Bagnell, Ng, and Schneider 2001; Satia and Lave Jr 1973; Wiesemann, Kuhn, and Rustem 2013; Lim and Autef 2019; Xu and Mannor 2010; Yu and Xu 2015; Lim, Xu, and Mannor 2013; Tamar, Mannor, and Xu 2014), where the uncertainty set is assumed to be known, and the problem can be solved using robust dynamic programming. Later, the studies were generalized to the model-free setting where stochas-
tic samples from the centroid MDP of the uncertainty set are available in an online fashion (Roy, Xu, and Pokutta 2017; Badrinath and Kalathil 2021; Wang and Zou 2021, 2022; Tessler, Efroni, and Mannor 2019) and an offline fashion (Zhou et al. 2021; Yang, Zhang, and Zhang 2021; Panaganti and Kalathil 2021; Goyal and Grand-Clement 2018; Kaufman and Schaefer 2013; Ho, Petrik, and Wiesemann 2018, 2021; Si et al. 2020). There are also empirical studies on robust RL, e.g., (Vinitsky et al. 2020; Pinto et al. 2017; Abdullah et al. 2019; Hou et al. 2020; Rajeswaran et al. 2017; Huang et al. 2017; Kos and Song 2017; Lin et al. 2017; Pattanaik et al. 2018; Mandlekar et al. 2017). For discounted MDPs, the robust Bellman operator is a contraction, based on which robust dynamic programming and value-based methods can be designed. In this paper, we focus on robust average-reward MDPs. However, the robust Bellman operator for averagereward MDPs is not a contraction, and its fixed point may not be unique. Moreover, the average-reward setting depends on the limiting behavior of the underlying stochastic process, which is thus more intricate. Robust average-reward MDPs. Studies on robust averagereward MDPs are quite limited in the literature. Robust average-reward MDPs under a specific finite interval uncertainty set was studied in (Tewari and Bartlett 2007), where the authors showed the existence of a Blackwell optimal policy, i.e., there exists some δ ∈ [0, 1), such that the optimal robust policy exists and remains unchanged for any discount factor γ ∈ [δ, 1). However, this result depends on the structure of the uncertainty set. For general uncertainty sets, the existence of a Blackwell optimal policy may not be guaranteed. More recently, (Lim, Xu, and Mannor 2013) designed a model-free algorithm for a specific `1-norm uncertainty set and characterized its regret bound. However, their method also relies on the structure of the `1-norm uncertainty set, and may not be generalizable to other types of uncertainty sets. In this paper, our results can be applied to various types of uncertainty sets, and thus is more general. 
Preliminaries and Problem Model In this section, we introduce some preliminaries on discounted MDPs, average-reward MDPs, and robust MDPs. 
Discounted MDPs. A discounted MDP (S,A,P, r, γ) is specified by: a state space S, an action space A, a transition kernel P = {pas ∈ ∆(S), a ∈ A, s ∈ S}1, where pas is the distribution of the next state over S upon taking action a in state s (with pas,s′ denoting the probability of transitioning to s′), a reward function r : S×A→ [0, 1], and a discount factor γ ∈ [0, 1). At each time step t, the agent at state st takes an action at, the environment then transitions to the next state st+1 according to patst , and produces a reward signal r(st, at) ∈ [0, 1] to the agent. In this paper, we also write rt = r(st, at) for convenience. 
A stationary policy π : S → ∆(A) is a distribution over A for any given state s, and the agent takes action a at state s with probability π(a|s). The discounted value function of a stationary policy π starting from s ∈ S is defined as the 
1∆(S): the (|S| − 1)-dimensional probability simplex on S. 
expected discounted cumulative reward by following policy π: V πP,γ(s) , Eπ,P [ 
∑∞ t=0 γ 
trt|S0 = s]. 
Average-Reward MDPs. Different from discounted MDPs, average-reward MDPs do not discount the reward over time, and consider the behavior of the underlying Markov process under the steady-state distribution. More specifically, under a specific transition kernel P, the average-reward of a policy π starting from s ∈ S is defined as 
gπP(s) , lim n→∞ 
Eπ,P [ 
1 
n 
n−1∑ t=0 
rt|S0 = s 
] , (1) 
which we also refer to in this paper as the average-reward value function for convenience. 
The average-reward value function can also be equivalently written as follows: gπP = limn→∞ 
1 n 
∑n−1 t=0 (Pπ)trπ , 
Pπ∗rπ, where (Pπ)s,s′ , ∑ a π(a|s)pas,s′ and rπ(s) ,∑ 
a π(a|s)r(s, a) are the transition matrix and reward function induced by π, and Pπ∗ , limn→∞ 
1 n 
∑n−1 t=0 (Pπ)t is the 
limit matrix of Pπ . In the average-reward setting, we also define the following 
relative value function 
V πP (s) , Eπ,P [ ∞∑ t=0 
(rt − gπP)|S0 = s 
] , (2) 
which is the cumulative difference over time between the reward and the average value gπP . It has been shown that (Puterman 1994): V πP = Hπ 
P rπ, where Hπ P , (I − Pπ + 
Pπ∗ ) −1(I − Pπ∗ ) is defined as the deviation matrix of Pπ . 
The relationship between the average-reward and the relative value functions can be characterized by the following Bellman equation (Puterman 1994): 
V πP (s) = Eπ [ r(s,A)− gπP(s) + 
∑ s′∈S 
pAs,s′V π P (s′) 
] . (3) 
Robust discounted and average-reward MDPs. For robust MDPs, the transition kernel is not fixed but belongs to some uncertainty set P. After the agent takes an action, the environment transits to the next state according to an arbitrary transition kernel P ∈ P. In this paper, we focus on the (s, a)-rectangular uncertainty set (Nilim and El Ghaoui 2004; Iyen-gar 2005), i.e., P = 
⊗ s,a P 
a s , where Pas ⊆ ∆(S). We note 
that there are also studies on relaxing the (s, a)-rectangular uncertainty set to s-rectangular uncertainty set, which is not the focus of this paper. 
Under the robust setting, we consider the worst-case performance over the uncertainty set of MDPs. More specifically, the robust discounted value function of a policy π for a discounted MDP is defined as 
V πP,γ(s) , min κ∈ 
⊗ t≥0 P 
Eπ,κ 
[ ∞∑ t=0 
γtrt|S0 = s 
] , (4) 
where κ = (P0,P1...) ∈ ⊗ 
t≥0 P.
In this paper, we focus on the following worst-case averagereward for a policy π: 
gπP(s) , min κ∈ 
⊗ t≥0 P 
lim n→∞ 
Eπ,κ 
[ 1 
n 
n−1∑ t=0 
rt|S0 = s 
] , (5) 
to which, for convenience, we refer as the robust averagereward value function. 
For robust discounted MDPs, it has been shown that the robust discounted value function is the unique fixed-point of the robust discounted Bellman operator (Nilim and El Ghaoui 2004; Iyengar 2005; Puterman 1994): 
TπV (s) , ∑ a∈A 
π(a|s) ( r(s, a) + γσPas (V ) 
) , (6) 
where σPas (V ) , minp∈Pas p >V is the support function of 
V on Pas . Based on the contraction of Tπ, robust dynamic programming approaches, e.g., robust value iteration, can be designed (Nilim and El Ghaoui 2004; Iyengar 2005) (see Appendix for a review of these methods). However, there is no such contraction result for robust average-reward MDPs. In this paper, our goal is to find a policy that optimizes the robust average-reward value function: 
max π∈Π 
gπP(s), for any s ∈ S, (7) 
where Π is the set of all stationary policies, and we denote by g∗P(s) , maxπ g 
π P(s) the optimal robust average-reward. 
Limit Approach for Robust Average-Reward MDPs 
We first take a limit approach to solve the problem of robust average-reward MDPs in eq. (7). It is known that under the non-robust setting, for any fixed π and P, the discounted value function converges to the average-reward value function as the discount factor γ approaches 1 (Puterman 1994), i.e., 
lim γ→1 
(1− γ)V πP,γ = gπP . (8) 
We take a similar idea, and show that the same result holds in the robust case: limγ→1(1 − γ)V πP,γ = gπP under a mild assumption. Based on this result, we further design algorithms (Algorithms 1 and 2) that apply a sequence of robust discounted Bellman operators while increasing the discount factor at a certain rate. We then theoretically prove that our algorithms converge to the optimal solutions. 
In the following, we first show that the convergence limγ→1(1 − γ)V πP,γ = gπP is uniform on the set Π × P. In studies of average-reward MDPs, it is usually the case that a certain class of MDPs are considered, e.g., unichain and communicating (Wei et al. 2020; Zhang and Ross 2021; Chen, Jain, and Luo 2022; Wan, Naik, and Sutton 2021). In this paper, we focus on the unichain setting to highlight the major technical novelty to achieve robustness. 
Assumption 1. For any s ∈ S, a ∈ A, the uncertainty set Pas is a compact subset of ∆(S). And for any π ∈ Π,P ∈ P, the induced MDP is a unichain. 
The first part of Assumption 1 amounts to assuming that the uncertainty set is closed. We remark that many standard uncertainty sets satisfy this assumption, e.g., those defined by ε-contamination (Huber 1965), finite interval (Tewari and Bartlett 2007), total-variation (Rahimian, Bayraksan, and De-Mello 2022) and KL-divergence (Hu and Hong 2013). The unichain assumption is also widely used in studies of average-reward MDPs, e.g., (Puterman 1994; Wan, Naik, and Sutton 2021; Zhang and Ross 2021; Lan 2020; Zhang, Zhang, and Maguluri 2021). Also it is worth noting that under the unichain assumption, the robust average-reward is identical for every starting state, i.e., gπP(s1) = gπP(s2),∀s1, s2 ∈ S (Bertsekas 2011). Remark 1. The results in this section actually only require the uniform boundedness of ‖Hπ 
P‖,∀π ∈ Π,P ∈ P (Lemma 2 in Appendix). Assumption 1 is one sufficient condition. 
In (Puterman 1994), the convergence limγ→1(1 − γ)V πP,γ = gπP for a fixed policy π and a fixed transition kernel P (non-robust setting) is point-wise. However, such point-wise convergence does not provide any convergence guarantee on the robust discounted value function, as the robust value function measures the worst-case performance over the uncertainty set and the order of lim and min may not be exchanged in general. In the following theorem, we prove the uniform convergence of the discounted value function under the foregoing assumption. Theorem 1 (Uniform convergence). Under Assumption 1, the discounted value function converges uniformly to the average-reward value function on Π × P as γ → 1, i.e., 
lim γ→1 
(1− γ)V πP,γ = gπP , uniformly. (9) 
With uniform convergence in Theorem 1, the order of the limit γ → 1 and minP can be interchanged, then the following convergence of the robust discounted value function can be established. Theorem 2. The robust discounted value function in eq. (4) converges to the robust average-reward uniformly on Π: 
lim γ→1 
(1− γ)V πP,γ = gπP uniformly. (10) 
We note that a similar convergence result is shown in (Tewari and Bartlett 2007), but only for a special uncertainty set of finite interval. Our Theorem 2 holds for general compact uncertainty sets. Moreover, it is worth highlighting that our proof technique is fundamentally different from the one in (Tewari and Bartlett 2007). Specifically, under the finite interval uncertainty set, the worst-case transition kernels are from a finite set, i.e., V πP,γ = minP∈M V πP,γ for a finite set M ⊆ P. This hence implies the interchangeability of lim and min. However, for general uncertainty sets, the number of worst-case transition kernels may not be finite. We demonstrate the interchangeability via our uniform convergence result in Theorem 1. 
The previous two convergence results play a fundamental role in limit method for robust average-reward MDPs, and are of key importance to motivate the design of the following
two algorithms, the basic idea of which is to apply a sequence of robust discounted Bellman operators on an arbitrary initialization while increasing the discount factor at a certain rate. 
We first consider the robust policy evaluation problem, which aims to estimate the robust average-reward gπP for a fixed policy π. This problem for robust discounted MDPs is well studied in the literature, however, results for robust average-reward MDPs are quite limited except for the one in (Tewari and Bartlett 2007) for a specific finite interval uncertainty set. We present the a robust value iteration (robust VI) algorithm for evaluating the robust average-reward with general uncertainty sets in Algorithm 1. 
Algorithm 1: Robust VI: Policy Evaluation Input: π, V0(s) = 0,∀s, T 
1: for t = 0, 1, ..., T − 1 do 2: γt ← t+1 
t+2 
3: for all s ∈ S do 4: Vt+1(s)← Eπ[(1− γt)r(s,A) + γtσPAs (Vt)] 5: end for 6: end for 7: return VT 
At each time step t, the discount factor γt is set to t+1 t+2 , 
which converges to 1 as t → ∞. Subsequently, a robust Bellman operator w.r.t discount factor γt is applied on the current estimate Vt of the robust discounted value function (1 − γt)V πP,γt . As the discount factor approaches 1, the estimated robust discounted value function converges to the robust average-reward gπP by Theorem 2. The following result shows that the output of Algorithm 1 converges to the robust average-reward. Theorem 3. Algorithm 1 converges to robust average reward, i.e., limT→∞ VT = gπP. 
Besides the robust policy evaluation problem, it is also of great practical importance to find an optimal policy that maximizes the worst-case average-reward, i.e., to solve eq. (7). Based on a similar idea as the one of Algorithm 1, we extend our limit approach to solve the robust optimal control problem in Algorithm 2. 
Algorithm 2: Robust VI: Optimal Control Input: V0(s) = 0,∀s, T 
1: for t = 0, 1, ..., T − 1 do 2: γt ← t+1 
t+2 
3: for all s ∈ S do 4: Vt+1(s)← max 
a∈A 
{ (1− γt)r(s, a) + γtσPas (Vt) 
} 5: end for 6: end for 7: for s ∈ S do 8: πT (s)← arg maxa∈A 
{ (1− γt)r(s, a) + γtσPas (VT ) 
} 9: end for 
10: return VT , πT 
Similar to Algorithm 1, at each time step, the discount factor γt is set to be closer to 1, and a one-step robust discounted Bellman operator (for optimal control) w.r.t. γt is applied to 
the current estimate Vt. The following theorem establishes that VT in Algorithm 2 converges to the optimal robust value function, hence can find the optimal robust policy. 
Theorem 4. The output VT in Algorithm 2 converges to the optimal robust average-reward g∗P: VT → g∗P as T →∞. 
As discussed in (Blackwell 1962; Hordijk and Yushkevich 2002), the average-reward criterion is insensitive and under selective since it is only interested in the performance under the steady-state distribution. For example, two policies providing rewards: 100 + 0 + 0 + · · · and 0 + 0 + 0 + · · · are equally good/bad. Towards this issue, for the non-robust setting, a more sensitive term of optimality was introduced by Blackwell (Blackwell 1962). More specifically, a policy is said to be Blackwell optimal if it optimizes the discounted value function for all discount factor γ ∈ (δ, 1) for some δ ∈ (0, 1). Together with eq. (8), the optimal policy obtained by taking γ → 1 is optimal not only for the average-reward criterion, but also for the discounted criterion with large γ. Intuitively, it is optimal under the average-reward setting, and is sensitive to early rewards. 
Following a similar idea, we justify that the obtained policy from Algorithm 2 is not only optimal in the robust averagereward setting, but also sensitive to early rewards. 
Denote by Π∗D the set of all the deterministic optimal policies for robust average-reward (proved to exist in Lemma 7), i.e. Π∗D = {π ∈ ΠD : gπP = g∗P} . 
Theorem 5 (Blackwell optimality). There exists 0 < δ < 1, such that for any γ > δ, the deterministic optimal robust policy for robust discounted value function V ∗P,γ belongs to Π∗D. Moreover, when Π∗D is a singleton, there exists a unique Blackwell optimal policy. 
This result implies that using the limit method in this section to find the optimal robust policy for average-reward MDPs has an additional advantage that the policy it finds not only optimizes the average reward in steady state, but also is sensitive to early rewards. 
It is worth highlighting the distinction of our results from the technique used in the proof of Blackwell optimality (Blackwell 1962). In the non-robust setting, the existence of a stationary Blackwell optimal policy is proved via contradiction, where a difference function of two policies π and ν: fπ,ν(γ) , V πP,γ − V 
µ P,γ is used in the proof. It was shown by 
contradiction that f has infinitely many zeros, which however contradicts with the fact that f is a rational function of γ with a finite number of zeros. A similar technique was also used in (Tewari and Bartlett 2007) for the finite interval uncertainty set. Specifically, in (Tewari and Bartlett 2007), it was shown that the worst-case transition kernels for any π, γ are from a finite set M, hence fπ,ν(γ) , minP∈M V πP,γ−minP∈M V µP,γ can also be shown to be a rational function with a finite number of zeroes. For a general uncertainty set P, the difference function fπ,ν(γ), however, may not be rational. This makes the method in (Blackwell 1962; Tewari and Bartlett 2007) inapplicable to our problem.
Direct Approach for Robust Average-Reward MDPs 
The limit approach in Section is based on the uniform convergence of the discounted value function, and uses discounted MDPs to approximate average-reward MDPs. In this section, we develop a direct approach to solving the robust averagereward MDPs that does not adopt discounted MDPs as intermediate steps. 
For average-reward MDPs, the relative value iteration (RVI) approach (Puterman 1994) is commonly used since it is numerically stable and has convergence guarantee. In the following, we generalize the RVI algorithm to the robust setting, and design the robust RVI algorithm in Algorithm 3. 
We first generalize the relative value function in eq. (2) to the robust relative value function. The robust relative value function measures the difference between the worst-case cumulative reward and the worst-case average-reward for a policy π. Definition 1. The robust relative value function is defined as 
V πP (s) , min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP)|S0 = s 
] , (11) 
where gπP is the worst-case average-reward defined in eq. (5). The following theorem presents a robust Bellman equation 
for robust average-reward MDPs. Theorem 6. For any s and π, (V πP , g 
π P) is a solution to the 
following robust Bellman equation: 
V (s) + g = ∑ a 
π(a|s) ( r(s, a) + σPas (V ) 
) . (12) 
It can be seen that the robust Bellman equation for averagereward MDPs has a similar structure to the one for discounted MDPs in eq. (6) except for a discount factor. This actually reveals a fundamental difference between the robust Bellman operator of the discounted MDPs and the average-reward ones. For a discounted MDP, its robust Bellman operator is a contraction with constant γ (Nilim and El Ghaoui 2004; Iyengar 2005), and hence the fixed point is unique. Based on this, the robust value function can be found by recursively applying the robust Bellman operator (see Appendix ). In sharp contrast, in the average-reward setting, the robust Bellman is not necessarily a contraction, and the fixed point may not be unique. Therefore, repeatedly applying the robust Bell-man operator in the average-reward setting may not even converge, which underscores that the two problem settings are fundamentally different. 
We first derive the following equivalent optimality condition for robust average-reward MDPs. Theorem 7. For any (g, V ) that is a solution to 
max a 
{ r(s, a)− g + σPas (V )− V (s) 
} = 0,∀s, (13) 
g = g∗P. If we further set 
π∗(s) = arg max a 
{ r(s, a) + σPas (V ) 
} (14) 
for any s ∈ S, then π∗ is an optimal robust policy. 
Theorem 7 suggests that as long as we find a solution (g, V ) to eq. (13), which though may not be unique, then g is the optimal robust average-reward g∗P, and the greedy policy π∗ is the optimal policy to our robust average-reward MDP problem in eq. (7). 
In the following, we generalize the RVI approach to the robust setting, and design a robust RVI algorithm in Algo-rithm 3. We will further show that the output of this algorithm converges to a solution to eq. (13), and further the optimal policy could be obtained by eq. (14). Here 1 de-
Algorithm 3: Robust RVI Input: V0, ε and arbitrary s∗ ∈ S 
1: w0 ← V0 − V0(s∗)1 2: while sp(wt − wt+1) ≥ ε do 3: for all s ∈ S do 4: Vt+1(s)← maxa(r(s, a) + σPas (wt)) 5: wt+1(s)← Vt+1(s)− Vt+1(s∗) 6: end for 7: end while 8: return wt, Vt 
notes the all-ones vector, and sp denotes the span semi-norm: sp(w) = maxs w(s)−mins w(s). Different from Algorithm 2, in Algorithm 3, we do not need to apply the robust discounted Bellman operator. The method directly solves the robust optimal control problem for average-reward robust MDPs. 
To study the convergence of the robust RVI algorithm, we first make an additional assumption as follows. 
Assumption 2. There exists a positive integer J such that for any P = {pas ∈ ∆(S)} ∈ P and any stationary deterministic policy π, there exists κ > 0 and a state s ∈ S, such that ((Pπ)J)x,s ≥ κ,∀x ∈ S. 
This assumption is shown to be equivalent to assuming unichain and aperiodic (Bertsekas 2011). It can be also replaced using some weaker ones, e.g., Proposition 4.3.2 of (Bertsekas 2011), or be removed by designing a variant of RVI, e.g., Proposition 4.3.4 of (Bertsekas 2011). In the following theorem, we show that our Algorithm 3 converges to a solution of eq. (13), hence according to Theorem 7 if we set π according to (14), then π is the optimal robust policy. 
Theorem 8. (wt, Vt) converges to a solution (w, V ) to eq. (13) as ε→ 0. 
Remark 2. In this section, we mainly present the robust RVI algorithm for the robust optimal control problem, and its convergence and optimality guarantee. A robust RVI algorithm for robust policy evaluation can be similarly designed by replacing the max in line 4, Algorithm 3 with an expectation w.r.t. π. The convergence results in Theorem 8 can also be similarly derived. 
Examples and Numerical Results In this section, we study several commonly used uncertainty set models, including contamination model, Kullback-Lerbler (KL) divergence and total-variation defined model.
As can be observed from Algorithms 1 to 3, for different uncertainty sets, the only difference lies in how the support function σPas (V ) is calculated. In the sequel, we discuss how to efficiently calculate the support function for various uncertainty sets. 
We numerically compare our robust (relative) value iteration methods v.s. non-robust (relative) value iteration method on different uncertainty sets. Our experiments are based on the Garnet problem G(20, 40) (Archibald, McKinnon, and Thomas 1995). More specifically, there are 20 states and 30 actions; the nominal transition kernel P = {pas ∈ ∆(S)} is randomly generated according to the uniform distribution, and the reward functions r(s, a) ∼ N(0, σs,a), where σs,a ∼ Uniform[0, 1]. In our experiments, the uncertainty sets are designed to be centered at the nominal transition kernel. We run different algorithms, i.e., (robust) value iteration and (robust) relative value iteration, and obtain the greedy policies at each time step. Then, we use robust averagereward policy evaluation (Algorithm 1) to evaluate the robust average-reward of these policies. We plot the robust averagereward against the number of iterations. Contamination model. For any (s, a) the uncertainty set Pas is defined as Pas = {q : q = (1−R)pas +Rp′, p′ ∈ ∆(S)}, where pas is the nominal transition kernel. It can be viewed as an adversarial model, where at each time-step, the environment transits according to the nominal transition kernel p with probability 1 − R, and according to an arbitrary kernel p′ with probability R. Note that σPas (V ) = 
(1 − R)(pas)>V + Rmins V (s). Our experimental results under the contamination model are shown in Figure 1. 
(a) Robust VI. (b) Robust RVI. 
Figure 1: Comparison on contamination model with R = 0.4. 
Total variation. The total variation distance is another commonly used distance metric to measure the difference between two distributions. For two distributions p and q, it is defined as DTV (p, q) = 1 
2‖p − q‖1. Con-sider an uncertainty set defined via total variation: Pas = {q : DTV (q||pas) ≤ R}. Then, its support function can be efficiently solved as follows (Iyengar 2005): σPas (V ) = p>V − Rminµ≥0 {maxs(V (s)− µ(s))−mins(V (s)− µ(s))} . 
Our experimental results under the total variation model are shown in Figure 2. Kullback-Lerbler (KL) divergence. The Kullback–Leibler divergence is widely used to measure the distance between two probability distributions. For distributions p, q, it is defined as DKL(q||p) = 
∑ s q(s) log q(s) 
p(s) . Consider an uncertainty set defined via KL divergence: Pas = {q : DKL(q||pas) ≤ R}. Then, its support function can be efficiently solved using the duality result in (Hu and Hong 
(a) Robust VI. (b) Robust RVI. 
Figure 2: Comparison on total variation model with R = 0.6. 
2013): σPas (V ) = −minα≥0 
{ Rα+ α log 
( p>e 
−V α 
)} . 
Our experimental results under the KL-divergence model are shown in Figure 3. 
(a) Robust VI. (b) Robust RVI. 
Figure 3: Comparison on KL-divergence model with R = 0.8. 
It can be seen that our robust methods can obtain policies that achieve higher worst-case reward. Also, both our limit-based robust value iteration and our direct method of robust relative value iteration converge to the optimal robust policies, which validates our theoretical results. 
Conclusion In this paper, we investigated the problem of robust MDPs under the average-reward setting. We established uniform convergence of the discounted value function to averagereward, which further implies the uniform convergence of the robust discounted value function to robust average-reward. Based on this insight, we designed a robust dynamic programming approach using the robust discounted MDPs as an approximation (the limit method). We theoretically proved their convergence and optimality and proved a robust version of the Blackwell optimality (Blackwell 1962). We then designed a direct approach for robust average-reward MDPs, where we derived the robust Bellman equation for robust average-reward MDPs. We further designed a robust RVI method, which was proven to converge to the optimal robust solution. Technically, our proof techniques are fundamentally different from existing studies on average-reward robust MDPs, e.g., those in (Blackwell 1962; Tewari and Bartlett 2007). 
Acknowledgment This work was supported by the National Science Foundation under Grants CCF-2106560, CCF-2007783, CCF-2106339 and CCF-1552497.
References Abdullah, M. A.; Ren, H.; Ammar, H. B.; Milenkovic, V.; Luo, R.; Zhang, M.; and Wang, J. 2019. Wasserstein robust reinforcement learning. arXiv preprint arXiv:1907.13196. Archibald, T.; McKinnon, K.; and Thomas, L. 1995. On the generation of Markov decision processes. Journal of the Operational Research Society, 46(3): 354–361. Atia, G. K.; Beckus, A.; Alkhouri, I.; and Velasquez, A. 2021. Steady-State Planning in Expected Reward Multichain MDPs. Journal of Artificial Intelligence Research, 72: 1029–1082. Badrinath, K. P.; and Kalathil, D. 2021. Robust Reinforce-ment Learning using Least Squares Policy Iteration with Provable Performance Guarantees. In Proc. International Conference on Machine Learning (ICML), 511–520. PMLR. Bagnell, J. A.; Ng, A. Y.; and Schneider, J. G. 2001. Solving uncertain Markov decision processes. Bertsekas, D. P. 2011. Dynamic Programming and Opti-mal Control 3rd edition, volume II. Belmont, MA: Athena Scientific. Blackwell, D. 1962. Discrete dynamic programming. The Annals of Mathematical Statistics, 719–726. Chen, L.; Jain, R.; and Luo, H. 2022. Learning Infinite-Horizon Average-Reward Markov Decision Processes with Constraints. arXiv preprint arXiv:2202.00150. Derman, C. 1970. Finite state Markovian decision processes. Academic Press, Inc. Derman, E.; Geist, M.; and Mannor, S. 2021. Twice regularized MDPs and the equivalence between robustness and regularization. In Proc. Advances in Neural Information Processing Systems (NeurIPS). Eysenbach, B.; and Levine, S. 2021. Maximum entropy RL (provably) solves some robust RL problems. arXiv preprint arXiv:2103.06257. Goyal, V.; and Grand-Clement, J. 2018. Robust Markov decision process: Beyond rectangularity. arXiv preprint arXiv:1811.00215. Ho, C. P.; Petrik, M.; and Wiesemann, W. 2018. Fast Bellman updates for robust MDPs. In Proc. International Conference on Machine Learning (ICML), 1979–1988. PMLR. Ho, C. P.; Petrik, M.; and Wiesemann, W. 2021. Partial policy iteration for L1-robust Markov decision processes. Journal of Machine Learning Research, 22(275): 1–46. Hordijk, A.; and Yushkevich, A. A. 2002. Blackwell optimality. In Handbook of Markov decision processes, 231–267. Springer. Hou, L.; Pang, L.; Hong, X.; Lan, Y.; Ma, Z.; and Yin, D. 2020. Robust Reinforcement Learning with Wasserstein Constraint. arXiv preprint arXiv:2006.00945. Hu, Z.; and Hong, L. J. 2013. Kullback-Leibler divergence constrained distributionally robust optimization. Available at Optimization Online, 1695–1724. Huang, S.; Papernot, N.; Goodfellow, I.; Duan, Y.; and Abbeel, P. 2017. Adversarial attacks on neural network policies. In Proc. International Conference on Learning Representations (ICLR). 
Huber, P. J. 1965. A Robust Version of the Probability Ratio Test. Ann. Math. Statist., 36: 1753–1758. Iyengar, G. N. 2005. Robust dynamic programming. Mathe-matics of Operations Research, 30(2): 257–280. Kaufman, D. L.; and Schaefer, A. J. 2013. Robust modified policy iteration. INFORMS Journal on Computing, 25(3): 396–410. Kober, J.; Bagnell, J. A.; and Peters, J. 2013. Reinforcement Learning in Robotics: A Survey. The International Journal of Robotics Research, 32(11): 1238–1274. Kos, J.; and Song, D. 2017. Delving into adversarial attacks on deep policies. In Proc. International Conference on Learning Representations (ICLR). Lan, G. 2020. First-order and Stochastic Optimization Meth-ods for Machine Learning. Springer Nature. Lim, S. H.; and Autef, A. 2019. Kernel-based reinforcement learning in robust Markov decision processes. In Proc. In-ternational Conference on Machine Learning (ICML), 3973– 3981. PMLR. Lim, S. H.; Xu, H.; and Mannor, S. 2013. Reinforcement learning in robust Markov decision processes. In Proc. Ad-vances in Neural Information Processing Systems (NIPS), 701–709. Lin, Y.-C.; Hong, Z.-W.; Liao, Y.-H.; Shih, M.-L.; Liu, M.-Y.; and Sun, M. 2017. Tactics of adversarial attack on deep reinforcement learning agents. In Proc. International Joint Conferences on Artificial Intelligence (IJCAI), 3756–3762. Mandlekar, A.; Zhu, Y.; Garg, A.; Fei-Fei, L.; and Savarese, S. 2017. Adversarially robust policy learning: Active construction of physically-plausible perturbations. In 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 3932–3939. IEEE. Nilim, A.; and El Ghaoui, L. 2004. Robustness in Markov decision problems with uncertain transition matrices. In Proc. Advances in Neural Information Processing Systems (NIPS), 839–846. Panaganti, K.; and Kalathil, D. 2021. Sample Complexity of Robust Reinforcement Learning with a Generative Model. arXiv preprint arXiv:2112.01506. Pattanaik, A.; Tang, Z.; Liu, S.; Bommannan, G.; and Chowd-hary, G. 2018. Robust Deep Reinforcement Learning with Adversarial Attacks. In Proc. International Conference on Autonomous Agents and MultiAgent Systems, 2040–2042. Pinto, L.; Davidson, J.; Sukthankar, R.; and Gupta, A. 2017. Robust adversarial reinforcement learning. In Proc. Interna-tional Conference on Machine Learning (ICML), 2817–2826. PMLR. Puterman, M. L. 1994. Markov Decision Processes: Discrete Stochastic Dynamic Programming. Rahimian, H.; Bayraksan, G.; and De-Mello, T. H. 2022. Effective scenarios in multistage distributionally robust optimization with a focus on total variation distance. SIAM Journal on Optimization, 32(3): 1698–1727. Rajeswaran, A.; Ghotra, S.; Ravindran, B.; and Levine, S. 2017. Epopt: Learning robust neural network policies using
model ensembles. In Proc. International Conference on Learning Representations (ICLR). Roy, A.; Xu, H.; and Pokutta, S. 2017. Reinforcement learning under model mismatch. In Proc. Advances in Neural Information Processing Systems (NIPS), 3046–3055. Rudin, W. 2022. Functional Analysis. McGraw-Hill Science &Engineering &Math, 2nd edition. Russel, R. H.; Benosman, M.; and Van Baar, J. 2020. Ro-bust Constrained-MDPs: Soft-Constrained Robust Policy Optimization under Model Uncertainty. arXiv preprint arXiv:2010.04870. Satia, J. K.; and Lave Jr, R. E. 1973. Markovian decision processes with uncertain transition probabilities. Operations Research, 21(3): 728–740. Si, N.; Zhang, F.; Zhou, Z.; and Blanchet, J. 2020. Distri-butionally robust policy evaluation and learning in offline contextual bandits. In Proc. International Conference on Machine Learning (ICML), 8884–8894. PMLR. Sigaud, O.; and Buffet, O. 2013. Markov decision processes in artificial intelligence. John Wiley & Sons. Sutton, R. S.; and Barto, A. G. 2018. Reinforcement Learning: An Introduction. Cambridge, Massachusetts: The MIT Press. Tamar, A.; Mannor, S.; and Xu, H. 2014. Scaling up robust MDPs using function approximation. In Proc. International Conference on Machine Learning (ICML), 181–189. PMLR. Tessler, C.; Efroni, Y.; and Mannor, S. 2019. Action robust reinforcement learning and applications in continuous control. In International Conference on Machine Learning, 6215– 6224. PMLR. Tewari, A.; and Bartlett, P. L. 2007. Bounded parameter Markov decision processes with average reward criterion. In International Conference on Computational Learning Theory, 263–277. Springer. Vinitsky, E.; Du, Y.; Parvate, K.; Jang, K.; Abbeel, P.; and Bayen, A. 2020. Robust Reinforcement Learning using Ad-versarial Populations. arXiv preprint arXiv:2008.01825. Wan, Y.; Naik, A.; and Sutton, R. S. 2021. Learning and planning in average-reward markov decision processes. In In-ternational Conference on Machine Learning, 10653–10662. PMLR. Wang, Y.; and Zou, S. 2021. Online Robust Reinforcement Learning with Model Uncertainty. In Proc. Advances in Neural Information Processing Systems (NeurIPS). Wang, Y.; and Zou, S. 2022. Policy Gradient Method For Robust Reinforcement Learning. In Proc. International Con-ference on Machine Learning (ICML), volume 162, 23484– 23526. PMLR. Wei, C.-Y.; Jahromi, M. J.; Luo, H.; Sharma, H.; and Jain, R. 2020. Model-free reinforcement learning in infinite-horizon average-reward markov decision processes. In International conference on machine learning, 10170–10180. PMLR. Wiesemann, W.; Kuhn, D.; and Rustem, B. 2013. Robust Markov decision processes. Mathematics of Operations Re-search, 38(1): 153–183. 
Xu, H.; and Mannor, S. 2010. Distributionally Robust Markov Decision Processes. In Proc. Advances in Neural Information Processing Systems (NIPS), 2505–2513. Yang, W.; Zhang, L.; and Zhang, Z. 2021. Towards The-oretical Understandings of Robust Markov Decision Pro-cesses: Sample Complexity and Asymptotics. arXiv preprint arXiv:2105.03863. Yu, P.; and Xu, H. 2015. Distributionally robust counterpart in Markov decision processes. IEEE Transactions on Automatic Control, 61(9): 2538–2543. Zhang, S.; Zhang, Z.; and Maguluri, S. T. 2021. Finite Sample Analysis of Average-Reward TD Learning and Q-Learning. Advances in Neural Information Processing Systems, 34: 1230–1242. Zhang, Y.; and Ross, K. W. 2021. On-policy deep reinforcement learning for the average-reward criterion. In Proc. Inter-national Conference on Machine Learning (ICML), 12535– 12545. PMLR. Zhou, Z.; Bai, Q.; Zhou, Z.; Qiu, L.; Blanchet, J.; and Glynn, P. 2021. Finite-Sample Regret Bound for Distributionally Robust Offline Tabular Reinforcement Learning. In Proc. In-ternational Conference on Artifical Intelligence and Statistics (AISTATS), 3331–3339. PMLR.
Review of Robust Discounted MDPs In this section, we provide a brief review on the existing methods and results for robust discounted MDPs. 
Robust Policy Evaluation We first consider the robust policy evaluation problem, where we aim to estimate the robust value function V πP,γ for any policy π. It has been shown that the robust Bellman operator Tπ is a γ-contraction, and the robust value function V πP,γ is its unique fixed-point. Hence by recursively applying the robust Bellman operator, we can find the robust discounted value function (Nilim and El Ghaoui 2004; Iyengar 2005). 
Algorithm 4: Policy evaluation for robust discounted MDPs Input: π, V0, T 
1: for t = 0, 1, ..., T − 1 do 2: for all s ∈ S do 3: Vt+1(s)← Eπ[r(s,A) + γσPAs (Vt)] 4: end for 5: end for 6: return VT 
Robust Optimal Control Another important problem in robust MDP is to find the optimal policy which maximizes the robust discounted value function: 
π∗ = arg max π 
V πP,γ . (15) 
A robust value iteration approach is developed in (Nilim and El Ghaoui 2004; Iyengar 2005) as follows. 
Algorithm 5: Optimal Control for robust discounted MDPs Input: V0, T 
1: for t = 0, 1, ..., T − 1 do 2: for all s ∈ S do 3: Vt+1(s)← maxa 
{ r(s, a) + γσPas (Vt) 
} 4: end for 5: end for 6: π∗(s)← arg maxa 
{ r(s, a) + γσPas (VT ) 
} ,∀s 
7: return π∗ 
Equivalence between Time-Varying and Stationary Models We first provide an equivalence result between time-varying and stationary transition kernel models under stationary policies, which is an analog result to the one for robust discounted MDPs (Iyengar 2005; Nilim and El Ghaoui 2004). This result will be used in our following proofs. 
Recall the definitions of robust discounted value function and worst-case average reward in eqs. (4) and (5), the worst-case is taken w.r.t. κ = (P0,P1...) ∈ 
⊗ t≥0 P, therefore, the transition kernel at each time step could be different. This model is 
referred to as time-varying transition kernel model (as in (Iyengar 2005; Nilim and El Ghaoui 2004)). Another commonly used setting is that the transition kernels at different time step are the same, which is referred to as the stationary model (Iyengar 2005; Nilim and El Ghaoui 2004). In this paper, we use the following notations to distinguish the two models. By EP[·], we denote the expectation when the transition kernels at all time steps are the same, P, i.e., the stationary model. We also denote by gπP(s) , limn→∞ EP,π 
[ 1 n 
∑n−1 t=0 rt 
∣∣S0 = s ] 
and V πP,γ(s) , EP,π 
[∑∞ t=0 γ 
trt ∣∣S0 = s 
] being the expected average-reward and 
expected discounted value function under the stationary model P. By Eκ[·], we denote the expectation when the transition kernel at time t is Pt, i.e., the time-varying model. 
For the discounted setting, it has been shown in (Nilim and El Ghaoui 2004) that for a stationary policy π, any γ ∈ [0, 1), and any s ∈ S, 
V πP,γ(s) = min κ∈ 
⊗ t≥0 P 
Eπ,κ 
[ ∞∑ t=0 
γtrt|S0 = s 
]
= min P∈P 
Eπ,P 
[ ∞∑ t=0 
γtrt|S0 = s 
] . (16) 
In the following theorem, we prove an analog of eq. (16) for robust-average reward MDPs that if we consider stationary policies, then the robust average-reward problem with the time-varying model can be equivalently solved by a stationary model. 
Specifically, we define the worst-case average reward for the stationary transition kernel model as follows: 
min P∈P 
lim n→∞ 
Eπ,P 
[ 1 
n 
n−1∑ t=0 
rt ∣∣S0 = s 
] . (17) 
Recall the worst-case average reward for the time-varying model in eq. (5). We will show that for any stationary policy, eq. (5) can be equivalently solved by solving eq. (17). 
Theorem 9. Consider an arbitrary stationary policy π. Then, the worst-case average-reward under the time-varying model is the same as the one under the stationary model: 
gπP(s) , min κ∈ 
⊗ t≥0 P 
lim n→∞ 
Eκ,π 
[ 1 
n 
n−1∑ t=0 
rt|S0 = s 
] 
= min P∈P 
lim n→∞ 
EP,π 
[ 1 
n 
n−1∑ t=0 
rt ∣∣S0 = s 
] . (18) 
Similar result also holds for the robust relative value function: 
V πP (s) , min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP)|S0 = s 
] 
= min P∈P 
EP,π 
[ ∞∑ t=0 
(rt − gπP)|S0 = s 
] . (19) 
Proof. From the robust Bellman equation in Theorem 6 2, we have that 
V πP (s) + gπP = ∑ a 
π(a|s) ( r(s, a) + σPas (V πP ) 
) . (20) 
Denote by arg minp∈Pas (p)>V πP , pas 3, and denote by Pπ , {pas : s ∈ S, a ∈ A}. It then follows that 
V πP (s) = ∑ a 
π(a|s) ( r(s, a)− gπP + σPas (V πP ) 
) = ∑ a 
π(a|s)(r(s, a)− gπP) + ∑ a 
π(a|s)EPπ [V πP (S1)|S0 = s,A0 = a] 
= ∑ a 
π(a|s)(r(s, a)− gπP) + EPπ,π[V πP (S1)|S0 = s] 
= ∑ a 
π(a|s)(r(s, a)− gπP) + EPπ,π 
[∑ a 
π(a|S1)(r(S1, a)− gπP)|S0 = s 
] + EPπ,π 
[∑ a 
π(a|S1)σPaS1 (V πP )|S0 = s 
] = ∑ a 
π(a|s)(r(s, a)− gπP) + EPπ,π [r1 − gπP|S0 = s] + EPπ,π 
[ σ P A1 S1 
(V πP )|S0 = s 
] = ∑ a 
π(a|s)(r(s, a)− gπP) + EPπ,π 
[ r1 − gπP 
∣∣S0 = s 
] + EPπ,π 
[ (pA1 
S1 )>V πP |S0 = s 
] = EPπ,π 
[ r0 − gπP + r1 − gπP|S0 = s 
] + EPπ,π[V πP (S2)|S0 = s] 
...... 
2The proof of Theorem 6 is independent of theorem 9 and does not relay on the results to be showed here. 3We pick one arbitrarily, if there are multiple minimizers.
= EPπ,π 
[ ∞∑ t=0 
(rt − gπP)|s ] . (21) 
By the definition, the following always hold: 
min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP)|S0 = s 
] ≤ min 
P∈P EP,π 
[ ∞∑ t=0 
(rt − gπP)|S0 = s 
] . (22) 
This hence implies that a stationary transition kernel sequence κ = (Pπ,Pπ, ...) is one of the worst-case transition kernels for V πP . Therefore, eq. (19) can be proved. 
Consider the transition kernel Pπ . We denote its non-robust average-reward and the non-robust relative value function by gπPπ and V πPπ . By the non-robust Bellman equation (Sutton and Barto 2018), we have that 
V πPπ (s) = ∑ a 
π(a|s)(r(s, a)− gπPπ ) + EPπ,π[V πPπ (S1)|s]. (23) 
On the other hand, the robust Bellman equation shows that 
V πP (s) = V πPπ (s) = ∑ a 
π(a|s)(r(s, a)− gπP) + EPπ,π[V πPπ (S1)|s]. (24) 
These two equations hence implies that gπP = gπPπ , and hence the stationary kernel (Pπ,Pπ, ...) is also a worst-case kernel of robust average-reward in the time-varying setting. This proves eq. (18). 
Proof of Theorem 1 In the proof, unless otherwise specified, we denote by ‖v‖ the l∞ norm of a vector v, and for a matrix A, we denote by ‖A‖ its matrix norm induced by l∞ norm, i.e., ‖A‖ = supx∈Rd 
‖Ax‖∞ ‖x‖∞ . 
Lemma 1. [Theorem 8.2.3 in (Puterman 1994)] For any P, γ, π, 
V πP,γ = 1 
1− γ gπP + hπP + fπP (γ), (25) 
where hπP = Hπ P rπ , and fπP (γ) = 1 
γ 
∑∞ n=1(−1)n 
( 1−γ γ 
)n (Hπ 
P )n+1rπ . 
Following Proposition 8.4.6 in (Puterman 1994), we can show the following lemma. Lemma 2. Hπ 
P is continuous on Π × P. If Π and P are compact, ‖Hπ P‖ is uniformly bounded on Π × P, i.e., there exists a 
constant h, such that ‖Hπ P‖ ≤ h for any π,P. 
For simplicity, denote by 
Sπ∞(P, γ) , 1 
γ 
∞∑ n=1 
(−1)n ( 
1− γ γ 
)n (Hπ 
P )n+1rπ, 
SπN (P, γ) , 1 
γ 
N∑ n=1 
(−1)n ( 
1− γ γ 
)n (Hπ 
P )n+1rπ. (26) 
Clearly Sπ∞(P, γ) = fπP (γ) and limN→∞ SπN (P, γ) = Sπ∞(P, γ) for any specific π,P. Lemma 3. There exists δ ∈ (0, 1), such that 
lim N→∞ 
SπN (P, γ) = Sπ∞(P, γ) (27) 
uniformly on Π × P× [δ, 1]. 
Proof. Note that ‖Hπ P‖ ≤ h, hence there exists δ, s.t. 
1− δ δ 
h ≤ k < 1 (28) 
for some constant k. Then for any γ ≥ δ, 
1− γ γ 
h ≤ 1− δ δ 
h ≤ k. (29)
Moreover, note that ∥∥∥∥ 1 
γ (−1)n 
( 1− γ γ 
)n (Hπ 
P )n+1r 
∥∥∥∥ ≤ 1 
γ 
( 1− γ γ 
)n hn+1 ≤ hkn 
δ ,Mn, (30) 
which is because ‖A+B‖ ≤ ‖A‖+ ‖B‖ for induced l∞ norm, ‖Ax‖ ≤ ‖A‖‖x‖ and ‖rπ‖∞ ≤ 1. Note that 
∞∑ n=1 
Mn = h 
δ 
k 
1− k , (31) 
hence by Weierstrass M -test (Rudin 2022), SπN (P, γ) uniformly converges to Sπ∞(P, γ) on Π × P× [δ, 1]. 
Lemma 4. There exists a uniform constant L, such that 
‖SπN (P, γ1)− SπN (P, γ2)‖ ≤ L|γ1 − γ2|, (32) 
for any N , π, P, γ1, γ2 ∈ [δ, 1]. 
Proof. We first show that γSπN (P, γ) = ∑N n=1(−1)n 
( 1−γ γ 
)n (Hπ 
P )n+1rπ , TπN (P, γ) is uniformly Lipschitz w.r.t. the l∞ norm, i.e., 
‖TπN (P, γ1)− TπN (P, γ2)‖ ≤ l|γ1 − γ2|, (33) 
for any N , π, P, γ1, γ2 ∈ [δ, 1] and some constant l. Clearly, it can be shown by verifying∇TπN (P, γ) is uniformly bounded for any π,N,P or γ. First, it can be shown that 
∇TπN (P, γ) = 
N∑ n=1 
(−1)nn 
( 1− γ γ 
)n−1 −1 
γ2 (Hπ 
P )n+1rπ, (34) 
and moreover 
‖∇TπN (P, γ)‖ ≤ N∑ n=1 
n 
( 1− γ γ 
)n−1 1 
γ2 hn+1 , lN (γ). (35) 
Note that 
h 1− γ γ 
lN (γ) = 
N∑ n=1 
n 
( 1− γ γ 
)n 1 
γ2 hn+2, (36) 
then, we can show that ( 1− h1− γ 
γ 
) lN (γ) 
= 
N∑ n=1 
n 
( 1− γ γ 
)n−1 1 
γ2 hn+1 − 
N∑ n=1 
n 
( 1− γ γ 
)n 1 
γ2 hn+2 
= 1 
γ2 h2 −N 
( 1− γ γ 
)N 1 
γ2 hN+2 + 
N∑ n=2 
( 1− γ γ 
)n−1 1 
γ2 hn+1 
≤ 1 
γ2 h2 + 
h2 
γ2 
1− γ γ 
h 1 
1− 1−γ γ h 
= h2 
γ2 + h2 
γ2 
1− γ γ 
h 1 
1− 1−γ γ h 
. (37) 
Hence, we have that 
‖∇TπN (P, γ)‖ ≤ lN (γ) ≤ 1 
1− h 1−γ γ 
( h2 
γ2 + h2 
γ2 
1− γ γ 
h 1 
1− 1−γ γ h 
)
≤ 1 
1− k 
( h2 
δ2 + h2 
δ2 
k 
1− k 
) , (38) 
which implies a uniform bound on ‖∇TπN (P, γ)‖. Now, we have that 
|SπN (P, γ1)− SπN (P, γ2)| 
≤ |γ2 − γ1| γ1γ2 
‖TπN (P, γ1)‖+ ‖TπN (P, γ1)− TπN (P, γ2)‖ 
γ2 . (39) 
To show ‖TπN (P, γ)‖ is uniformly bounded, we have that 
‖TπN (P, γ)‖ ≤ N∑ n=1 
∥∥∥∥(1− γ γ 
)n (Hπ 
P )n+1r 
∥∥∥∥ ≤ 
N∑ n=1 
( 1− γ γ 
)n hn+1 
≤ N∑ n=1 
knh 
≤ h k 
1− k . (40) 
Then, it follows that 
‖SπN (P, γ1)− SπN (P, γ2)‖ 
= 
∥∥∥∥γ2 − γ1 
γ1γ2 TπN (P, γ1) + 
TπN (P, γ1)− TπN (P, γ2) 
γ2 
∥∥∥∥ ≤ ( 
1 
δ2 h 
k 
1− k + 
1 
δ 
1 
1− k 
( h2 
δ2 + h2 
δ2 
k 
1− k 
)) |γ1 − γ2| 
, L|γ1 − γ2|, (41) 
where L = ( 
1 δ2h 
k 1−k + 1 
δ 1 
1−k 
( h2 
δ2 + h2 
δ2 k 
1−k 
)) is a universal constant that does not depend on N,P, π or γ. 
Lemma 5. Sπ∞(P, γ) uniformly converges as γ → 1 on Π × P. Also, Sπ∞(P, γ) is L-Lipschitz for any γ > δ: for any π,P and any γ1, γ2 ∈ (δ, 1]. 
‖Sπ∞(P, γ1)− Sπ∞(P, γ2)‖ ≤ L|γ1 − γ2|. (42) 
Proof. From Lemma 3, for any ε, there exists Nε, such that for any n ≥ Nε, π,P, γ > δ, 
‖Sπ∞(P, γ)− Sπn(P, γ)‖ < ε. (43) 
Thus for any γ1, γ2 ∈ (δ, 1], 
‖Sπ∞(P, γ1)− Sπ∞(P, γ2)‖ ≤ ‖Sπ∞(P, γ1)− Sπn(P, γ1)‖+ ‖Sπn(P, γ1)− Sπn(P, γ2)‖+ ‖Sπn(P, γ2)− Sπ∞(P, γ2)‖ ≤ 2ε+ ‖Sπn(P, γ1)− Sπn(P, γ2)‖ ≤ 2ε+ L|γ1 − γ2|, (44) 
where the last step is from Lemma 4. Thus, for any ε, there exists ω = max {δ, 1− ε}, such that for any γ1, γ2 > ω, 
‖Sπ∞(P, γ1)− Sπ∞(P, γ2)‖ < (2 + L)ε, (45) 
and hence by Cauchy’s criterion we conclude that Sπ∞(P, γ) converges uniformly on Π × P. On the other hand, since eq. (44) holds for any ε, it implies that 
‖Sπ∞(P, γ1)− Sπ∞(P, γ2)‖ ≤ L|γ1 − γ2|, (46) 
which completes the proof.
We now prove Theorem 1. For any P, π, we have that 
V πP,γ = 1 
1− γ gπP + hπP + fπP (γ). (47) 
It then follows that 
(1− γ)V πP,γ = gπP + (1− γ)hπP + (1− γ)fπP (γ). (48) 
Clearly (1− γ)hπP → 0 uniformly on Π × P because ‖hπP‖ = ‖Hπ P rπ‖ ≤ h is uniformly bounded. Then, 
‖(1− γ1)fπP (γ1)− (1− γ2)fπP (γ2)‖ ≤ ‖(1− γ1)fπP (γ1)− (1− γ1)fπP (γ2)‖+ ‖(1− γ1)fπP (γ2)− (1− γ2)fπP (γ2)‖ ≤ (1− γ1)L|γ1 − γ2|+ ‖fπP (γ2)‖|γ1 − γ2|. (49) 
For any π,P, γ > δ, 
‖fπP (γ)‖ = 
∥∥∥∥ 1 
γ 
∞∑ n=1 
(−1)n ( 
1− γ γ 
)n (Hπ 
P )n+1rπ 
∥∥∥∥ ≤ ∣∣∣∣ 1γ 
∞∑ n=1 
( 1− γ γ 
)n hn+1 
∣∣∣∣ ≤ h 
δ 
1− γ γ 
h 1 
1− 1−γ γ h 
≤ h 
δ 
k 
1− k , cf . (50) 
Hence, (1− γ)fπP (γ)→ 0 uniformly on Π × P due to the fact that ‖fπP (γ)‖ is uniformly bounded for any π, γ > δ,P. Then we have that limγ→1(1− γ)V πP,γ = gπP uniformly on P×Π . This completes the proof of Theorem 1. 
Proof of Theorem 2 We first show a lemma which allows us to interchange the order of lim and max. Lemma 6. If a function f(x, y) converges uniformly to F (x) on X as y → y0, then 
max x 
lim y→y0 
f(x, y) = lim y→y0 
max x 
f(x, y). (51) 
Proof. For each f(x, y), denote by arg maxx f(x, y) = xy, and hence f(xy, y) ≥ f(x, y) for any x, y. Also denote by arg maxx F (x) = x′. Now because f(x, y) uniformly converges to F (x), then for any ε, there exists δ′, such that ∀|y−y0| < δ′, 
|f(x, y)− F (x)| ≤ ε (52) 
for any x. Now consider |f(xy, y)− F (x′)| for |y − y0| < δ′. If f(xy, y)− F (x′) > 0, then 
|f(xy, y)− F (x′)| = f(xy, y)− F (x′) = f(xy, y)− F (xy) + F (xy)− F (x′) ≤ ε; (53) 
On the other hand if f(xy, y)− F (x′) < 0, then 
|f(xy, y)− F (x′)| = F (x′)− f(xy, y) = F (x′)− f(x′, y) + f(x′, y)− f(xy, y) ≤ ε. (54) 
Hence, we showed that for any ε, there exists δ′, such that ∀|y − y0| < δ′, 
|f(xy, y)− F (x′)| = |max x 
f(x, y)−max x 
F (x)| ≤ ε, (55) 
and hence 
lim y→y0 
max x 
f(x, y) = max x 
F (x) = max x 
lim y→y0 
f(x, y), (56) 
and this completes the proof. 
Then, we show that the robust discounted value function converges uniformly to the robust average-reward as the discounted factor approaches 1.
Theorem 10 (Restatement of Theorem 2). The robust discounted value function converges uniformly to the robust average-reward on Π: 
lim γ→1 
(1− γ)V πP,γ = gπP. (57) 
Proof. Due to Theorem 9, for any stationary policy π, gπP(s) = minP∈P g π P(s) under the stationary model. Hence from the 
uniform convergence in Theorem 1, we first show the following: 
gπP = min P∈P 
gπP 
= min P∈P 
lim γ→1 
(1− γ)V πP,γ 
(a) = lim 
γ→1 min P∈P 
(1− γ)V πP,γ 
= lim γ→1 
(1− γ)V πP,γ , (58) 
where (a) is because Lemma 6. Moreover, note that limγ→1(1− γ)V πP,γ = gπP uniformly on Π × P, hence the convergence in (58) is also uniform on Π . Thus, we complete the proof. 
Proof of Theorem 3 Theorem 11 (Restatement of Theorem 3). VT generated by Algorithm 1 converges to the robust average-reward gπP as T →∞. 
Proof. From discounted robust Bellman equation (Nilim and El Ghaoui 2004), it can be shown that 
(1− γt)V πP,γt = (1− γt) ∑ a 
π(a|s)(r(s, a) + γtσPas (V πP,γt)). (59) 
Then we can show that for any s ∈ S, 
|Vt+1(s)− (1− γt+1)V πP,γt+1 (s)| 
= |Vt+1(s)− (1− γt)V πP,γt(s) + (1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 (s)| (60) 
≤ |(1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 (s)|+ |Vt+1(s)− (1− γt)V πP,γt(s)| 
= |(1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 (s)| 
+ 
∣∣∣∣∑ a 
π(a|s) ( 
(1− γt)r(s, a) + γtσPas (Vt)− ((1− γt)r(s, a) + γtσPas ((1− γt)V πP,γt)) )∣∣∣∣ 
= |(1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 (s)|+ 
∣∣∣∣∑ a 
π(a|s) ( γtσPas (Vt)− γtσPas ((1− γt)V πP,γt) 
)∣∣∣∣ = |(1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 
(s)|+ γt 
∣∣∣∣∑ a 
π(a|s) ( σPas (Vt)− σPas ((1− γt)V πP,γt) 
)∣∣∣∣. (61) 
If we denote by ∆t , ‖Vt − (1− γt)V πP,γt‖∞, then 
∆t+1 ≤ ‖(1− γt)V πP,γt − (1− γt+1)V πP,γt+1 ‖∞ + γt max 
s 
{∑ a 
π(a|s) ∣∣∣∣σPas (Vt)− σPas ((1− γt)V πP,γt) 
∣∣∣∣}. (62) 
It can be easily verified that σPas (V ) is a 1-Lipschitz function, thus the second term in (62) can be further bounded as∑ a 
π(a|s) ∣∣∣∣σPas (Vt)− σPas ((1− γt)V πP,γt) 
∣∣∣∣ ≤ ∑ a 
π(a|s)‖Vt − (1− γt)V πP,γt‖∞ 
= ‖Vt − (1− γt)V πP,γt‖∞, (63) 
and hence 
∆t+1 ≤ ‖(1− γt)V πP,γt − (1− γt+1)V πP,γt+1 ‖∞ + γt∆t. (64)
Recall that 
(1− γt)V πP,γt = (1− γt) min P V πP,γt . (65) 
Let s∗t , arg maxs |(1− γt)V πP,γt(s)− (1− γt+1)V πP,γt+1 (s)|. Then it follows that 
‖(1− γt)V πP,γt − (1− γt+1)V πP,γt+1 ‖∞ = |(1− γt)V πP,γt(s 
∗ t )− (1− γt+1)V πP,γt+1 
(s∗t )|. (66) 
Note that from (Nilim and El Ghaoui 2004; Iyengar 2005), for any stationary policy π, there exists a stationary model P such 
that V πP,γ(s) = EP,π 
[∑∞ t=0 γ 
trt|S0 = s 
] , V πP,γ . Hence in the following, for each γt, we denote the worst-case transition 
kernel of V πP,γt by Pt. If (1− γt)V πP,γt(s 
∗ t ) ≥ (1− γt+1)V πP,γt+1 
(s∗t ), then 
|(1− γt)V πP,γt(s ∗ t )− (1− γt+1)V πP,γt+1 
(s∗t )| = min 
P (1− γt)V πP,γt(s 
∗ t )−min 
P (1− γt+1)V πP,γt+1 
(s∗t ) 
= (1− γt)V πPt,γt(s ∗ t )− (1− γt+1)V πPt+1,γt+1 
(s∗t ) 
= (1− γt)V πPt,γt(s ∗ t )− (1− γt)V πPt+1,γt(s 
∗ t ) + (1− γt)V πPt+1,γt(s 
∗ t )− (1− γt+1)V πPt+1,γt+1 
(s∗t ) 
(a) 
≤ (1− γt)V πPt+1,γt(s ∗ t )− (1− γt+1)V πPt+1,γt+1 
(s∗t ) 
≤ ‖(1− γt)V πPt+1,γt − (1− γt+1)V πPt+1,γt+1 ‖∞, (67) 
where (a) is due to (1− γt)V πPt,γt(s ∗ t ) = minP(1− γt)V πP,γt(s 
∗ t ) ≤ (1− γt)V πPt+1,γt 
(s∗t ). Now, according to Lemma 1, 
(1− γt)V πPt+1,γt = gπPt+1 + (1− γt)hπPt+1 
+ (1− γt)fπPt+1 (γt), (68) 
(1− γt+1)V πPt+1,γt+1 = gπPt+1 
+ (1− γt+1)hπPt+1 + (1− γt+1)fπPt+1 
(γt+1). (69) 
Hence, for any γt > δ, eq. (67) can be further bounded as 
‖(1− γt)V πPt+1,γt − (1− γt+1)V πPt+1,γt+1 ‖∞ 
= ‖(γt+1 − γt)hπPt+1 + (1− γt)fπPt+1 
(γt)− (1− γt+1)fπPt+1 (γt+1)‖∞ 
≤ (γt+1 − γt)‖hπPt+1 ‖∞ + ‖fπPt+1 
(γt)− fπPt+1 (γt+1)‖∞ + ‖γt+1f 
π Pt+1 
(γt+1)− γtfπPt+1 (γt)‖∞ 
(a) 
≤ h(γt+1 − γt) + L(γt+1 − γt) + ‖γt+1f π Pt+1 
(γt+1)− γtfπPt+1 (γt)‖∞ 
≤ h(γt+1 − γt) + L(γt+1 − γt) + ‖γt+1f π Pt+1 
(γt+1)− γt+1f π Pt+1 
(γt)‖∞ + ‖γt+1f π Pt+1 
(γt)− γtfπPt+1 (γt)‖∞ 
≤ h(γt+1 − γt) + L(γt+1 − γt) + γt+1‖fπPt+1 (γt+1)− fπPt+1 
(γt)‖∞ + ‖fπPt+1 (γt)‖∞(γt+1 − γt) 
(b) 
≤ (h+ L+ γt+1L+ sup π,P,γ 
‖fπP (γ)‖∞)(γt+1 − γt) 
≤ K(γt+1 − γt), (70) 
where (a) is from Lemma 5 for any γt > δ, cf is defined in (50) and K , h+ 2L+ cf is a uniform constant; And (b) is from Lemma 5. 
Similarly, the inequality also holds for the case when (1− γt)V πP,γt(s ∗ t ) ≤ (1− γt+1)V πP,γt+1 
(s∗t ). Thus we have that for any t such that γt > δ, 
∆t+1 ≤ K(γt+1 − γt) + γt∆t, (71) 
where K is a uniform constant. Following Lemma 8 from (Tewari and Bartlett 2007), we have that ∆t → 0. Note that 
‖Vt − gπP‖∞ ≤ ‖Vt − (1− γt)V πP,γt‖∞ + ‖(1− γt)V πP,γt − g π P‖∞ = ∆t + ‖(1− γt)V πP,γt − g 
π P‖∞. (72) 
Together with Theorem 2, we further have that 
lim t→∞ 
‖Vt − gπP‖∞ = 0, (73) 
which completes the proof.
Proof of Theorem 4 Note that the optimal robust average-reward is defined as 
g∗P(s) , max π 
gπP(s). (74) 
We further define V ∗P,γ(s) , max 
π V πP,γ(s). (75) 
Theorem 12 (Restatement of Theorem 4). VT generated by Algorithm 2 converges to the optimal robust average-reward g∗P as T →∞. 
Proof. Firstly, from the uniform convergence in Theorem 2, it can be shown that 
lim t→∞ 
(1− γt)V ∗P,γt = g∗P. (76) 
We then show that for any s ∈ S, |Vt+1(s)− (1− γt+1)V ∗P,γt+1 
(s)| ≤ |Vt+1(s)− (1− γt)V ∗P,γt(s)|+ |(1− γt)V 
∗ P,γt(s)− (1− γt+1)V ∗P,γt+1 
(s)| (a) = |(1− γt)V ∗P,γt(s)− (1− γt+1)V ∗P,γt+1 
(s)| 
+ 
∣∣∣∣max a 
( (1− γt)r(s, a) + γtσPas (Vt) 
) −max 
a 
( ((1− γt)r(s, a) + γtσPas ((1− γt)V ∗P,γt)) 
)∣∣∣∣ ≤ |(1− γt)V ∗P,γt(s)− (1− γt+1)V ∗P,γt+1 
(s)| 
+ max a 
∣∣∣∣(1− γt)r(s, a) + γtσPas (Vt)− ((1− γt)r(s, a) + γtσPas ((1− γt)V ∗P,γt)) ∣∣∣∣, (77) 
where (a) is because the optimal robust Bellman equation, and the last inequality is from the fact that |maxx f(x)−maxx g(x)| ≤ maxx |f(x)− g(x)|. 
Hence eq. (77) can be further bounded as |Vt+1(s)− (1− γt+1)V ∗P,γt+1 
(s)| 
≤ |(1− γt)V ∗P,γt(s)− (1− γt+1)V ∗P,γt+1 (s)|+ γt max 
a 
∣∣∣∣σPas (Vt)− σPas ((1− γt)V ∗P,γt) ∣∣∣∣. (78) 
If we denote by ∆t , ‖Vt − (1− γt)V ∗P,γt‖∞, then 
∆t+1 ≤ ‖(1− γt)V ∗P,γt − (1− γt+1)V ∗P,γt+1 ‖∞ + γt max 
s.a 
∣∣∣∣σPas (Vt)− σPas ((1− γt)V ∗P,γt) ∣∣∣∣. (79) 
Since the support function σPas (V ) is 1-Lipschitz, then it can be shown that for any s, a,∣∣∣∣σPas (Vt)− σPas ((1− γt)V ∗P,γt) ∣∣∣∣ ≤ ‖Vt − (1− γt)V ∗P,γt‖∞. (80) 
Hence ∆t+1 ≤ ‖(1− γt)V ∗P,γt − (1− γt+1)V ∗P,γt+1 
‖∞ + γt∆t. (81) 
Similar to (70) in Theorem 3, we can show that ‖(1− γt)V ∗P,γt − (1− γt+1)V ∗P,γt+1 
‖∞ ≤ K|γt − γt+1|, (82) 
and similar to Lemma 8 from (Tewari and Bartlett 2007), lim t→∞ 
∆t = 0. (83) 
Moreover, note that ‖Vt − g∗P‖∞ ≤ ‖Vt − (1− γt)V ∗P,γt‖∞ + ‖(1− γt)V ∗P,γt − g 
∗ P‖∞ = ∆t + ‖(1− γt)V ∗P,γt − g 
∗ P‖∞, (84) 
which together with eq. (76) implies that ‖Vt − g∗P‖∞ → 0, (85) 
and hence it completes the proof. 
Lemma 7. There exists a deterministic optimal policy, i.e., ∃π∗ ∈ ΠD, s.t. gπ ∗ 
P = g∗P = maxπ∈Π g π P.
Proof of Lemma 7 Lemma 8. (Restatement of Lemma 7). There exists a deterministic optimal policy, i.e., ∃π∗ ∈ ΠD, s.t. gπ 
∗ 
P = g∗P = maxπ∈Π g π P. 
Proof. Assume that there is no deterministic optimal robust policy, i.e., there exists a strictly random policy πr ∈ Π , such that for any deterministic policy π ∈ ΠD, 
gπrP > gπP. (86) According to theorem 2, we have that 
lim γ→1 
(1− γ)V πrP,γ = gπrP , (87) 
lim γ→1 
(1− γ)V πP,γ = gπP,∀π ∈ ΠD. (88) 
Since there are only finite number of deterministic policies, there exists δ < 1, such that for any γ > δ, V πrP,γ > V πP,γ ,∀π ∈ ΠD. (89) 
This implies that for γ > δ, the random policy πr is better than all the deterministic policies, i.e., V πrP,γ > max 
π∈ΠD V πP,γ . (90) 
However, Theorem 3.1 of (Iyengar 2005) implies that there exists deterministic optimal robust policy, i.e., max π∈ΠD 
V πP,γ = max π∈Π 
V πP,γ ≥ V πr P,γ , (91) 
which contradicts to (90). Hence it implies that there exists a deterministic optimal robust policy, and completes the proof. 
Proof of Theorem 5 Theorem 13 (Restatement of Theorem 5). There exists 0 < δ < 1, such that for any γ > δ, a deterministic optimal robust policy for robust discounted value function V ∗P,γ is also an optimal policy for robust average-reward, i.e., 
V π ∗ 
P,γ = V ∗P,γ . (92) Moreover, when arg maxπ∈ΠD g 
π P is a singleton, there exists a unique Blackwell optimal policy. 
Proof. According to Lemma 7, there exists π∗ ∈ ΠD such that 
g∗P = gπ ∗ 
P . (93) Assume the robust average-reward of all deterministic policies are sorted in a descending order: 
g∗P = g π∗1 P = g 
π∗2 P = ... = g 
π∗m P > gπ1 
P ≥ ... ≥ g πn P (94) 
for all π∗i , πi ∈ ΠD, and we define Π∗ = {π∗i : i = 1, ...,m}. Denote by d = g π∗i P − g 
π1 
P . From Theorem 2, we know that for any π ∈ ΠD, 
lim γ→1 
(1− γ)V πP,γ = gπP. (95) 
Because the set ΠD is finite, for any ε < d 2 , there exists δ′ < 1, such that for any γ > δ′, π∗i and πj , 
|(1− γ)V π∗i P,γ − g 
∗ P| < ε, (96) 
|(1− γ)V πj P,γ − g 
πj P | < ε. (97) 
It hence implies that 
(1− γ)V π∗i P,γ ≥ (d− 2ε) + (1− γ)V 
πj P,γ > (1− γ)V 
πj P,γ , (98) 
and V π∗i P,γ > V 
πj P,γ . (99) 
Note that from Theorem 3.1 in (Iyengar 2005), i.e., maxπ∈ΠD V π P,γ = V ∗P,γ , we have that for any γ, there exists a deterministic 
policy π ∈ ΠD, such that V ∗P,γ = V πP,γ . Together with (99), it implies that all the possible optimal robust polices of V πP,γ belong to {π∗1 , ...π∗m}, i.e., the set Π∗. Hence, there exists π∗j ∈ Π∗, such that 
V π∗j P,γ = max 
π∈ΠD V πP,γ = V ∗P,γ . (100) 
For the second part, when the optimal robust policy of robust average-reward is unique, i.e., Π∗ = {π∗}. Then from the results above, there exists δ′, such that for any γ > δ′, V π 
∗ 
P,γ > V πP,γ for any π∗ 6= π ∈ ΠD, and hence π∗ is the optimal policy for discounted robust MDPs, which is the unique Blackwell optimal policy.
Proof of Results for Direct Approach Recall that 
V πP (s) , min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP) ∣∣S0 = s 
] , (101) 
where 
gπP = min κ∈ 
⊗ t≥0 P 
lim n→∞ 
Eκ,π 
[ 1 
n 
n−1∑ t=0 
rt|S0 = s 
] . (102) 
We first show that the robust relative function is always finite. Lemma 9. For any π, V πP is finite. 
Proof. According to Theorem 9, V πP = minP∈P V π P = minP∈P EP,π 
[∑∞ t=0(rt − gπP) 
] . Note that V πP can be rewritten as 
V πP = min P∈P 
EP,π 
[ ∞∑ t=0 
(rt − gπP) 
] 
= min P∈P 
EP,π 
[ lim n→∞ 
n∑ t=0 
(rt − gπP) 
] 
= min P∈P 
EP,π 
[ lim n→∞ 
n∑ t=0 
(rt − gπP + gπP − gπP) 
] = min 
P∈P EP,π 
[ lim n→∞ 
(Rn − ngπP + ngπP − ngπP) 
] , (103) 
where Rn = ∑n t=0 rt. Note that for any P ∈ P and n, ngπP ≥ ngπP, hence 
lim n→∞ 
(Rn − ngπP + ngπP − ngπP) ≥ lim n→∞ 
(Rn − ngπP), (104) 
and thus the lower bound of V πP can be derived as follows, 
V πP ≥ min P∈P 
EP,π 
[ ∞∑ t=0 
(rt − gπP) 
] = min 
P∈P V πP 
= min P∈P 
Hπ P rπ. (105) 
which is finite due to the fact that Hπ P is continuous on the compact set P. 
From Theorem 9, we denote the stationary worst-case transition kernel of gπP by Pg. Then the upper bound of V πP can be bounded by noting that 
V πP = min P∈P 
EP,π 
[ ∞∑ t=0 
(rt − gπPg ) 
] 
≤ EPg,π 
[ ∞∑ t=0 
(rt − gπPg ) 
] = V πPg , (106) 
which is also finite and Pg denotes the worst-case transition kernel of gπP. Hence we show that V πP is finite for any π and hence complete the proof. 
After showing that the robust relative value function is well-defined, we show the following robust Bellman equation for average-reward robust MDPs. Theorem 14 (Restatement of Theorem 6). For any s and π, (V πP , g 
π P) is a solution to the following robust Bellman equation: 
V (s) + g = ∑ a 
π(a|s) ( r(s, a) + σPas (V ) 
) . (107)
Proof. From the definition, 
V πP (s) = min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP) ∣∣S0 = s 
] , (108) 
hence 
V πP (s) = min κ∈ 
⊗ t≥0 P 
Eκ,π [ ∞∑ t=0 
(rt − gπP) ∣∣S0 = s 
] 
= min κ∈ 
⊗ t≥0 P 
Eκ,π [ (r0 − gπP) + 
∞∑ t=1 
(rt − gπP) ∣∣S0 = s 
] 
= min κ∈ 
⊗ t≥0 P 
{∑ a 
π(a|s)r(s, a)− gπP + Eκ,π [ ∞∑ t=1 
(rt − gπP) ∣∣S0 = s 
]} 
= ∑ a 
π(a|s) (r(s, a)− gπP) + min κ∈ 
⊗ t≥0 P 
∑ a,s′ 
π(a|s)Pas,s′Eκ,π [ ∞∑ t=1 
(rt − gπP)|S1 = s′ ] 
= ∑ a 
π(a|s) (r(s, a)− gπP) + min P0∈P 
min κ=(P1,...)∈ 
⊗ t≥1 P 
∑ a,s′ 
π(a|s)(P0)as,s′Eκ,π [ ∞∑ t=1 
(rt − gπP)|S1 = s′ ] 
= ∑ a 
π(a|s) (r(s, a)− gπP) + min P0∈P 
∑ a,s′ 
π(a|s)(P0)as,s′ min κ=(P1,...)∈ 
⊗ t≥1 P 
{ Eκ,π 
[ ∞∑ t=1 
(rt − gπP)|S1 = s′ ]} 
= ∑ a 
π(a|s) (r(s, a)− gπP) + ∑ a 
π(a|s) ∑ s′ 
min pa s,s′∈P 
a s 
pas,s′V π P (s′) 
= ∑ a 
π(a|s) (r(s, a)− gπP) + ∑ a 
π(a|s)σPas (V πP ) 
= ∑ a 
π(a|s) ( r(s, a)− gπP + σPas (V πP ) 
) . (109) 
This hence completes the proof. 
Theorem 15. [Restatement of Theorem 7, Part 1] For any (g, V ) that is a solution to maxa { r(s, a)− g + σPas (V )− V (s) 
} = 
0,∀s, then g = g∗P. 
Proof. In this proof, for two vectors v, w ∈ Rn, v ≥ w denotes that v(s) ≥ w(s) entry-wise. Let B(g, V )(s) , maxa 
{ r(s, a)− g + σPas (V )− V (s) 
} . Since (g, V ) is a solution to (13), hence for any a ∈ A and any 
s ∈ S, 
r(s, a)− g + σPas (V )− V (s) ≤ 0, (110) 
from which it follows that for any policy π, 
g(s) ≥ rπ(s) + ∑ a 
π(a|s)σPas (V )− V (s) , rπ(s) + ∑ a 
π(a|s)(pas)>V − V (s), (111) 
where rπ(s) , ∑ a π(a|s)r(s, a), pas , arg minp∈Pas p 
>V , and PV = {pas : s ∈ S, a ∈ A}. We also denotes the state transition matrix induced by π and PV by PπV . 
Using these notations, and rewrite eq. (111), we have that 
g1 ≥ rπ + (PπV − I)V. (112) 
Since the inequality in eq. (112) holds entry-wise, all entries of PπV are positive, then by multiplying both sides of eq. (112) by PπV , we have that 
g1 = gPπV 1 ≥ PπV rπ + PπV (PπV − I)V. (113) 
Multiplying the both sides of eq. (113) by PπV , and repeatedly doing that, we have that 
g1 ≥ (PπV )2rπ + (PπV )2(PπV − I)V, (114)
... ... (115) 
g1 ≥ (PπV )n−1rπ + (PπV )n−1(PπV − I)V. (116) 
Summing up these inequalities from eq. (112) to eq. (116), we have that 
ng1 ≥ (I + PπV + ...+ (PπV )n−1)rπ + (I + PπV + ...+ (PπV )n−1)(PπV − I)V, (117) 
and from which, it follows that 
g1 ≥ 1 
n (I + PπV + ...+ (PπV )n−1)rπ + 
1 
n (I + PπV + ...+ (PπV )n−1)(PπV − I)V 
= 1 
n (I + PπV + ...+ (PπV )n−1)rπ + 
1 
n ((PπV )n − I)V. (118) 
It can be easily verified that limn→∞ 1 n ((PπV )n − I)V = 0, and hence it implies that 
g1 ≥ lim n→∞ 
1 
n (I + PπV + ...+ (PπV )n−1)rπ 
= lim n→∞ 
1 
n EPπV ,π 
[ n∑ t=0 
rt 
] = gπPπV 1 
≥ gπP1. (119) 
Since eq. (119) holds for any policy π, it follows that g ≥ g∗P. On the other hand, since B(g, V ) = 0, there exists a policy τ such that 
g1 = rτ + (PτV − I)V, (120) 
where rτ ,PτV are similarly defined as for π. From Theorem 9, there exists a stationary transition kernel Pτave such that gτP = gτPτave . 
We denote the state transition matrix induced by τ and Pτave by Pτ . Then because PτV is the worst-case transition of V , it follows that 
PτV V ≤ PτV. (121) 
Thus 
g1 ≤ rτ + (Pτ − I)V. (122) 
Similarly, we have that 
g1 ≤ (Pτ )j−1rτ + (Pτ )j−1(Pτ − I)V, (123) 
for j = 2, ..., n. Summing these inequalities together we have that 
ng1 ≤ (I + Pτ + ...+ (Pτ )n−1)rτ + (I + Pτ + ...+ (Pτ )n−1)(Pτ )n−1(Pτ − I)V 
= (I + Pτ + ...+ (Pτ )n−1)rτ + ((Pτ )n − I)V. (124) 
Hence 
g1 ≤ lim n→∞ 
1 
n EPτave,τ 
[ n∑ t=0 
rt 
] = gτPτave 
1 = gτP1 ≤ g∗P1. (125) 
Thus g = g∗P, and this concludes the proof. 
Theorem 16 (Restatement of Theorem 7, Part 2). For any (g, V ) that is a solution to 
max a 
{ r(s, a)− g + σPas (V )− V (s) 
} = 0,∀s, (126) 
if we set 
π∗(s) = arg max a 
{ r(s, a) + σPas (V ) 
} (127) 
for any s ∈ S, then π∗ is an optimal robust policy.
Proof. Note that for any stationary policy π, we denote by σPπ (V ) , ( ∑ a π(a|s1)σPas1 (V ), ..., 
∑ a π(a|s|S|)σPas|S| (V )) being 
a vector in R|S|. Then eq. (14) is equivalent to 
rπ∗ + σPπ∗ (V ) = max π {rπ + σPπ (V )} . (128) 
Hence, 
rπ∗ − g + σPπ∗ (V )− V = max π {rπ − g + σPπ (V )− V } . (129) 
Since (g, V ) is a solution to (13), it follows that 
rπ∗ − g + σPπ∗ (V )− V = 0. (130) 
According to the robust Bellman equation eq. (12), (gπ ∗ 
P , V π ∗ 
P ) is a solution to eq. (130). Thus from Theorem 15, gπ ∗ 
P = g∗P, and hence π∗ is an optimal robust policy. 
Theorem 17 (Restatement of Theorem 8). (wT , Vt) in Algorithm 3 converges to a solution of eq. (13). 
Proof. We first denote the update operator as 
Lv(s) , max a 
(r(s, a) + σPas (v)). (131) 
Now, consider sp(Lv − Lu). Denote by ś , arg maxs(Lv(s) − Lu(s)) and s̀ , arg mins(Lv(s) − Lu(s)). Also denote by av , arg maxa(r(ś, a) + σPaś (v)) and au , arg maxa(r(ś, a) + σPaś (u)) Then 
Lv(ś)− Lu(ś) = max a 
(r(ś, a) + σPaś (v))−max a 
(r(ś, a) + σPaś (u)) 
, r(ś, av) + σPavś (v)− (r(ś, au) + σPauś (u)) 
≤ r(ś, av) + σPavś (v)− (r(ś, av) + σPavś (u)) 
= σPavś (v)− σPavś (u) 
, (pav,vś )>v − (pav,uś )>u, (132) 
where pav,vś = arg minp∈Pavś p>v and pav,uś = arg minp∈Pavś p>u. Thus eq. (132) can be further bounded as 
Lv(ś)− Lu(ś) 
≤ (pav,vś )>v − (pav,uś )>u 
≤ (pav,uś )>(v − u). (133) 
Similarly, 
Lv(s̀)− Lu(s̀) ≥ (pau,vs̀ )>(v − u). (134) 
Thus 
sp(Lv − Lu) ≤ (pav,uś )>(v − u)− (pau,vs̀ )>(v − u). (135) 
Now denote by v−u , (x1, x2, ..., xn), pav,uś = (p1, ..., pn) and pau,vs̀ = (q1, ..., qn). Further denote by bi , min{pi, qi} Then 
n∑ i=1 
pixi − n∑ i=1 
qixi 
= 
n∑ i=1 
(pi − bi)xi − n∑ i=1 
(qi − bi)xi 
≤ n∑ i=1 
(pi − bi) max{xi} − n∑ i=1 
(qi − bi) min{xi} 
= 
n∑ i=1 
(pi − bi)sp(x) + 
( n∑ i=1 
(pi − bi)− n∑ i=1 
(qi − bi) ) 
min{xi}
= ( 1− 
n∑ i=1 
bi 
) sp(x). (136) 
Thus we showed that 
sp(Lv − Lu) ≤ ( 
1− n∑ i=1 
bi 
) sp(v − u). (137) 
Now from Assumption 2, and following Theorem 8.5.3 from (Puterman 1994), it can be shown that there exists 1 > λ > 0, such that for any a, u, v, 
n∑ i=1 
bi ≥ λ. (138) 
Further, following Theorem 8.5.2 in (Puterman 1994), it can be shown that L is a J-step contraction operator for some integer J , i.e., 
sp(LJv − LJu) ≤ (1− λ)sp(v − u). (139) 
Then, it can be shown that the relative value iteration converges to a solution of the optimal equation similar to the relative value iteration for non-robust MDPs under the average-reward criterion (Theorem 8.5.7 in (Puterman 1994), Section 1.6.4 in(Sigaud and Buffet 2013)), and hence (wt, Vt) converges to a solution to eq. (13) as ε→ 0.