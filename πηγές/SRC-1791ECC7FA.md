> Source: https://proceedings.mlr.press/v151/panaganti22a/panaganti22a.pdf

Sample Complexity of Robust Reinforcement Learning with a Generative Model 
Kishan Panaganti Dileep Kalathil Texas A&M University Texas A&M University 
Abstract 
The Robust Markov Decision Process (RMDP) framework focuses on designing control policies that are robust against the parameter uncertainties due to the mismatches between the simulator model and real-world settings. An RMDP problem is typically formulated as a max-min problem, where the objective is to find the policy that maximizes the value function for the worst possible model that lies in an uncertainty set around a nominal model. The standard robust dynamic programming approach requires the knowledge of the nominal model for computing the optimal robust policy. In this work, we propose a model-based reinforcement learning (RL) algorithm for learning an ε-optimal robust policy when the nominal model is unknown. We consider three different forms of uncertainty sets, characterized by the total variation distance, chi-square divergence, and KL divergence. For each of these uncertainty sets, we give a precise characterization of the sample complexity of our proposed algorithm. In addition to the sample complexity results, we also present a formal analytical argument on the benefit of using robust policies. Finally, we demonstrate the performance of our algorithm on two benchmark problems. 
1 Introduction 
Reinforcement Learning (RL) algorithms typically require a large number of data samples to learn a control policy, which makes the training of RL algorithms di-
Proceedings of the 25th International Conference on Artifi-cial Intelligence and Statistics (AISTATS) 2022, Valencia, Spain. PMLR: Volume 151. Copyright 2022 by the author(s). 
rectly on the real-world systems expensive and potentially dangerous. This problem is typically avoided by training the RL algorithm on a simulator and transferring the trained policy to the real-world system. How-ever, due to multiple reasons such as the approximation errors incurred while modeling, changes in the real-world parameters over time and possible adversarial disturbances in the real-world, there will be inevitable mismatches between the simulator model and the real-world system. For example, the standard simulator settings of the sensor noise, action delays, friction, and mass of a mobile robot can be different from that of the actual real-world robot. This mismatch between the simulator and real-world model parameters, often called ‘simulation-to-reality gap’, can significantly degrade the real-world performance of the RL algorithms trained on a simulator model. 
Robust Markov Decision Process (RMDP) addresses the planning problem of computing the optimal policy that is robust against the parameter mismatch between the simulator and real-world system. The RMDP framework was first introduced in (Iyengar, 2005; Nilim and El Ghaoui, 2005). The RMDP problem has been analyzed extensively in the literature (Xu and Mannor, 2010; Wiesemann et al., 2013; Yu and Xu, 2015; Mannor et al., 2016; Russel and Petrik, 2019), considering different types of uncertainty set and computationally efficient algorithms. However, these works are limited to the planning problem, which assumes the knowledge of the system. Robust RL algorithms for learning the optimal robust policy have also been proposed (Roy et al., 2017; Panaganti and Kalathil, 2021), but they only provide asymptotic convergence guarantees. Robust RL problem has also been addressed using deep RL methods (Pinto et al., 2017; Derman et al., 2018, 2020; Mankowitz et al., 2020; Zhang et al., 2020a). However, these works are empirical in nature and do not provide any theoretical guarantees for the learned policies. In particular, there are few works that provide robust RL algorithms with provable (non-asymptotic) finite-sample performance guarantees.
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
In this work, we address the problem of developing a model-based robust RL algorithm with provable finitesample guarantees on its performance, characterized by the metric of sample complexity in a PAC (probably approximately correct) sense. The RMDP framework assumes that the real-world model lies within some uncertainty set P around a nominal (simulator) model P o. The goal is to learn a policy that performs the best under the worst possible model in this uncertainty set. We do not assume that the algorithm knows the exact simulator model (and hence the exact uncertainty set). Instead, similar to the standard (non-robust) RL setting (Singh and Yee, 1994; Azar et al., 2013; Haskell et al., 2016; Sidford et al., 2018; Agarwal et al., 2020; Li et al., 2020; Kalathil et al., 2021), we assume that the algorithm has access to a generative sampling model that can generate nextstate samples for all state-action pairs according to the nominal simulator model. In this context, we answer the following important question: How many samples from the nominal simulator model do we need to learn an ε-optimal robust policy with high probability? 
Our contributions: The main contributions of our work are as follows: 
(1) We propose a model-based robust RL algorithm, which we call the robust empirical value iteration algorithm (REVI), for learning an approximately optimal robust policy. We consider three different classes of RMDPs with three different uncertainty sets: (i) Total Variation (TV) uncertainty set, (ii) Chi-square uncertainty set, and (iii) Kullback-Leibler (KL) uncertainty set, each characterized by its namesake distance measure. Robust RL problem is much more challenging than the standard (non-robust) RL problems due to the inherent nonlinearity associated with the robust dynamic programming and the resulting unbiasedness of the empirical estimates. We overcome this challenge analytically by developing a series of upperbounds that are amenable to using concentration inequality results (which are typically useful only in the unbiased setting), where we exploit a uniform concentration bound with a covering number argument. We rigorously characterize the sample complexity of the proposed algorithm for each of these uncertainty sets. We also make a precise comparison with the sample complexity of non-robust RL. 
(2) We give a formal argument for the need for using a robust policy when the simulator model is different from the real-world model. More precisely, we analytically address the question ‘why do we need robust policies?’, by showing that the worst case performance of a non-robust policy can be arbitrarily bad (as bad as a random policy) when compared to that of a robust policy. While the need for robust policies have 
been discussed in the literature qualitatively, to the best of our knowledge, this is the first work that gives an analytical answer to the above question. 
(3) Finally, we demonstrate the performance of our REVI algorithm in two experiment settings and for two different uncertainty sets. In each setting, we show that the policy learned by our proposed REVI algorithm is indeed robust against the changes in the model parameters. We also illustrate the convergence of our algorithm with respect to the number of samples and the number of iterations. 
1.1 Related Work 
Robust RL: An RMDP setting where some stateaction pairs are adversarial and the others are stationary was considered by (Lim et al., 2013), who proposed an online algorithm to address this problem. An approximate robust dynamic programming approach with linear function approximation was proposed in (Tamar et al., 2014). State aggregation and kernel-based function approximation for robust RL were studied in (Petrik and Subramanian, 2014; Lim and Autef, 2019). (Roy et al., 2017) proposed a robust version of the Q-learning algorithm. (Panaganti and Kalathil, 2021) developed a least squares policy iteration approach to learn the optimal robust policy using linear function approximation with provable guarantees. A soft robust RL algorithm was proposed in (Derman et al., 2018) and a maximum a posteriori policy optimization approach was used in (Mankowitz et al., 2020). While the above mentioned works make interesting contributions to the area of robust RL, they focus either on giving asymptotic performance guarantees or on the empirical performance without giving provable guarantees. In particular, they do not provide provable guarantees on the finite-sample performance of the robust RL algorithms. 
The closest to our work is (Zhou et al., 2021), which analyzed the sample complexity with a KL uncertainty set. Our work is different in two significant aspects: Firstly, we consider the total variation uncertainty set and chi-square uncertainty set, in addition to the KL uncertainty set. The analysis for these uncertainty sets are very challenging and significantly different from that of the KL uncertainty set. Secondly, we give a more precise characterization of the sample complexity bound for the KL uncertainty set by clearly specifying the exponential dependence on (1 − γ)−1, where γ is the discount factor, which was left unspecified in (Zhou et al., 2021). 
While this paper was under review, we were notified of a concurrent work (Yang et al., 2021), which also provides similar sample complexity bounds for robust
Kishan Panaganti, Dileep Kalathil 
Table 1: Comparison of the sample complexities of different uncertainty sets and the best known result in the non-robust setting (Li et al., 2020). Here |S| and |A| are the cardinality of the state and action spaces, cr is the robust RL problem parameter, and γ is the discount factor. We consider the optimality gap ε ∈ (0, c/(1 − γ)), where c > 0 is a constant. We refer to Section 3.2 for further details. 
Uncertainty set TV Chi-square KL Non-robust 
Sample Complexity O( |S| 2|A| 
(1−γ)4ε2 ) O( cr|S| 2|A| 
(1−γ)4ε2 ) O( |S| 2|A| exp(1/(1−γ)) c2r(1−γ)4ε2 ) O( |S||A| 
(1−γ)3ε2 ) 
RL. Our proof technique is significantly different from their work. Moreover, we also provide open-source experimental results that illustrate the performance of our robust RL algorithm. 
Other related works: Robust control is a wellstudied area (Zhou et al., 1996; Dullerud and Paganini, 2013) in the classical control theory. Recently, there are some interesting works that address the robust RL problem using this framework, especially focusing on the linear quadratic regulator setting (Zhang et al., 2020b). Our framework of robust MDP is significantly different from this line of work. Risk sensitive RL algorithms (Borkar, 2002) and adversarial RL algorithms (Pinto et al., 2017) also address the robustness problem implicitly. Our approach is different from these works also. 
Notations: For any set X , |X | denotes its cardinality. For any vector x, ‖x‖ denotes its infinity norm ‖x‖∞. 
2 Preliminaries: Robust Markov Decision Process 
A Markov Decision Process (MDP) is a tuple (S,A, r, P, γ), where S is the state space, A is the action space, r : S × A → R is the reward function, and γ ∈ (0, 1) is the discount factor. The transition probability function Ps,a(s′) represents the probability of transitioning to state s′ when action a is taken at state s. P is also called the the model of the system. We consider a finite MDP setting where |S| and |A| are finite. We will also assume that r(s, a) ∈ [0, 1], for all (s, a) ∈ S ×A, without loss of generality. 
A (deterministic) policy π maps each state to an action. The value of a policy π for an MDP with model P , evaluated at state s is given by 
Vπ,P (s) = Eπ,P [ 
∞∑ t=0 
γtr(st, at) | s0 = s], (1) 
where at = π(st), st+1 ∼ Pst,at(·). The optimal value function V ∗P and the optimal policy π∗P of an MDP with the model P are defined as 
V ∗P = max π 
Vπ,P , π∗P = arg max π 
Vπ,P . (2) 
Uncertainty set: Unlike the standard MDP which considers a single model (transition probability function), the RMDP formulation considers a set of models. We call this set as the uncertainty set and denote it as P. We assume that the set P satisfies the standard rectangularity condition (Iyengar, 2005). We note that a similar uncertainty set can be considered for the reward function at the expense of additional notations. However, since the analysis will be similar and the samples complexity guarantee will be identical upto a constant, without loss of generality, we assume that the reward function is known and deterministic. We specify a robust MDP as a tuple M = (S,A, r,P, γ). 
The uncertainty set P is typically defined as 
P = ⊗Ps,a, where, Ps,a = {Ps,a ∈ [0, 1]|S| : 
D(Ps,a, P o s,a) ≤ cr, 
∑ s′∈S 
Ps,a(s′) = 1}, (3) 
where P o = (P os,a, (s, a) ∈ S × A) is the nominal transition probability function, cr > 0 indicates the level of robustness, and D(·, ·) is a distance metric between two probability distributions. In the following, we call P o as the nominal model. In other words, P is the set of all valid transition probability functions in the neighborhood of the nominal model P o, where the neighborhood is defined using the distance metric D(·, ·). We note that the radius cr can depend on the state-action pair (s, a). We omit this to reduce the notation complexity. We also note that for cr ↓ 0, we recover the non-robust regime. 
We consider three different uncertainty sets corresponding to three different distance metrics D(·, ·). 
1. Total Variation (TV) uncertainty set (Ptv): We define Ptv = ⊗Ptv 
s,a, where Ptv s,a is defined as in (3) 
using the total variation distance 
Dtv(Ps,a, P o s,a) = (1/2)‖Ps,a − P os,a‖1. (4) 
2. Chi-square uncertainty set (Pc): We define Pc = ⊗Pc 
s,a, where Pc s,a is defined as in (3) using the Chi-
square distance 
Dc(Ps,a, P o s,a) = 
∑ s′∈S 
(Ps,a(s′)− P os,a(s′))2 
P os,a(s′) . (5)
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
3. Kullback-Leibler (KL) uncertainty set (Pkl): We define Pkl = ⊗Pkl 
s,a, where Pkl s,a is defined as in (3) 
using the Kullback-Leibler (KL) distance 
Dkl(Ps,a, P o s,a) = 
∑ s′ 
Ps,a(s′) log Ps,a(s′) 
P os,a(s′) . (6) 
We note that the sample complexity and its analysis will depend on the specific form of the uncertainty set. 
Robust value iteration: The goal of the RMDP problem is to compute the optimal robust policy which maximizes the value even under the worst model in the uncertainty set. Formally, the robust value function Vπ corresponding to a policy π and the optimal robust value function V ∗ are defined as (Iyengar, 2005; Nilim and El Ghaoui, 2005) 
V π = inf P∈P 
Vπ,P , V ∗ = sup π 
inf P∈P 
Vπ,P . (7) 
The optimal robust policy π∗ is such that the robust value function corresponding to it matches the optimal robust value function, i.e., V π 
∗ = V ∗. It is known that 
there exists a deterministic optimal policy (Iyengar, 2005) for the RMDP problem. So, we will restrict our attention to the class of deterministic policies. 
For any set B and a vector v, let 
σB(v) = inf{u>v : u ∈ B}. 
Using this notation, we can define the robust Bellman operator (Iyengar, 2005) as T (V )(s) = maxa (r(s, a) + γσPs,a(V )). It is known that T is a contraction mapping in infinity norm and the V ∗ is the unique fixed point of T (Iyengar, 2005). Since T is a contraction, robust value iteration can be used to compute V ∗, similar to the non-robust MDP setting (Iyengar, 2005). More precisely, the robust value iteration, defined as Vk+1 = TVk, converges to V ∗, i.e., Vk → V ∗. Similar to the optimal robust value function, we can also define the optimal robust action-value function as Q∗(s, a) = r(s, a) + γσPs,a(V ∗). Similar to the non-robust setting, it is straight forward to show that π∗(s) = arg maxaQ 
∗(s, a) and V ∗(s) = maxaQ ∗(s, a). 
3 Algorithm and Sample Complexity 
The robust value iteration requires the knowledge of the nominal model P o and the radius of the uncertainty set cr to compute V ∗ and π∗. While cr may be available as design parameter, the form of the nominal model may not be available in most practical problems. So, we do not assume the knowledge of the nominal model P o. Instead, similar to the non-robust RL setting, we assume only to have access to the samples from a generative model, which can generate samples 
Algorithm 1 Robust Empirical Value Iteration (REVI) Algorithm 
1: Input: Loop termination number K 2: Initialize: Q0 = 0 3: Compute the empirical uncertainty set P̂ accord-
ing to (8) 4: for k = 0, · · · ,K − 1 do 5: Vk(s) = maxaQk(s, a), ∀s 6: Qk+1(s, a) = r(s, a) + γσP̂s,a(Vk), ∀(s, a) 
7: end for 8: Output: πK(s) = arg maxaQK(s, a),∀s ∈ S 
of the next state s′ according to P os,a(·), given the stateaction pair (s, a) as the input. We propose a model-based robust RL algorithm that uses these samples to estimate the nominal model and uncertainty set. 
3.1 Robust Empirical Value Iteration (REVI) Algorithm 
We first get a maximum likelihood estimate P̂ o of the nominal model P o by following the standard approach (Azar et al., 2013, Algorithm 3). More precisely, we generate N next-state samples corresponding to each state-action pairs. Then, the maximum likelihood estimate P̂ o is given by P̂ os,a(s′) = N(s, a, s′)/N , where N(s, a, s′) is the number of times the state s′ is realized out of the total N transitions from the stateaction pair (s, a). Given P̂ o, we can get an empirical 
estimate P̂ of the uncertainty set P as, 
P̂ =⊗ P̂s,a, where, P̂s,a = {P ∈ [0, 1]S : 
D(Ps,a, P̂s,a) ≤ cr, ∑ s′∈S 
Ps,a(s′) = 1}, (8) 
where D is one of the metrics specified in (4) - (6). 
For finding an approximately optimal robust policy, we now consider the empirical RMDP M̂ = (S,A, r, P̂, γ) 
and perform robust value iteration using P̂. This is indeed our approach, which we call the Robust Empir-ical Value Iteration (REVI) Algorithm. The optimal 
robust policy and value function of M̂ are denoted as π̂?, V̂ ?, respectively. 
3.2 Sample Complexity 
In this section we give the sample complexity guarantee of the REVI algorithm for the three uncertainty sets. We first consider the TV uncertainty set. 
Theorem 1 (TV Uncertainty Set). Consider an RMDP with a total variation uncertainty set Ptv. Fix δ ∈ (0, 1) and ε ∈ (0, 24γ/(1−γ)). Consider the REVI
Kishan Panaganti, Dileep Kalathil 
algorithm with K ≥ K0 and N ≥ N tv, where 
K0 = 1 
log(1/γ) log( 
8γ 
ε(1− γ)2 ) and (9) 
N tv = 72γ2|S| 
(1− γ)4ε2 log( 
144γ|S||A| (δε(1− γ)2) 
). (10) 
Then, ‖V ∗−V πK‖ ≤ ε with probability at least 1−2δ. 
Remark 1. The total number of samples needed in the REVI algorithm is Ntotal = N |S||A|. So the sample complexity of the REVI algorithm with the TV uncer-
tainty set is O( |S| 2|A| 
(1−γ)4ε2 ). 
Remark 2 (Comparison with the sample complexity of the non-robust RL). For the non-robust setting, the lowerbound for the total number of samples from 
the generative sampling device is Ω( |S||A| ε2(1−γ)3 log |S||A|δ ) 
(Azar et al., 2013, Theorem 3). The variance reduced value iteration algorithm proposed in (Sid-ford et al., 2018) achieves a sample complexity 
of O( |S||A| ε2(1−γ)3 log |S||A|δε ), matching the lower bound. 
However, this work is restricted to ε ∈ (0, 1), whereas ε can be considered upto the value 1/(1 − γ) for the MDP problems. Recently, this result has been further improved recently by (Agarwal et al., 2020) and (Li et al., 2020), which considered ε ∈ (0, 1/ 
√ (1− γ)) 
and ε ∈ (0, 1/(1− γ)), respectively. 
Theorem 1 for the robust RL setting also considers ε upto O(1/(1 − γ)). However, the sample complexity obtained is worse by a factor of |S| and 1/(1−γ) when compared to the non-robust setting. These additional terms are appearing in our result due to a covering number argument we used in the proof, which seems necessary for getting a tractable bound. However, it is not clear if this is fundamental to the robust RL problem with TV uncertainty set. We leave this investigation for our future work. 
We next consider the chi-square uncertainty set. 
Theorem 2 (Chi-square Uncertainty Set). Consider an RMDP with a Chi-square uncertainty set Pc. Fix δ ∈ (0, 1) and ε ∈ (0, 16γ/(1 − γ)), for an absolute constant c1 > 1. Consider the REVI algorithm with K ≥ K0 and N ≥ N c, where K0 is as given in (9) and 
N c = 64γ2(2cr + 1)|S| 
(1− γ)4ε2 log( 
192|S||A|γ (δε(1− γ)2) 
). (11) 
Then, ‖V ∗−V πK‖ ≤ ε with probability at least 1−2δ. 
Remark 3. The sample complexity of the algorithm 
with the chi-square uncertainty set isO( |S| 2|A|cr 
(1−γ)4ε2 ). The 
order of sample complexity remains the same compared to that of the TV uncertainty set given in The-orem 1. 
Finally, we consider the KL uncertainty set. 
Theorem 3 (KL Uncertainty Set). Consider an RMDP with a KL uncertainty set Pkl. Fix δ ∈ (0, 1) and ε ∈ (0, 1/(1 − γ)). Consider the REVI algorithm with K ≥ K0 and N ≥ Nkl, where K0 is as in (9) and 
Nkl= 8γ2|S| 
c2r(1− γ)4ε2 exp( 
2λkl + 4 
λkl(1− γ) ) log( 
9|S||A| δλkl(1− γ) 
), 
(12) 
and λkl is a problem dependent parameter but independent of Nkl. Then, ‖V ∗ − V πK‖ ≤ ε with probability at least 1− 2δ. 
Remark 4. The sample complexity with the KL un-
certainty set is O( |S|2|A| (1−γ)4ε2c2r 
exp( 1 (1−γ) )). We note that 
(Zhou et al., 2021) also considered the robust RL problem with KL uncertainty set. They provided a sample 
complexity bound of the form O( C|S|2|A| (1−γ)4ε2c2r 
), However 
the exponential dependence on 1/(1 − γ) was hidden inside the constant C. In this work, we clearly specify the depends on the factor 1/(1− γ). 
4 Why Do We Need Robust Policies? 
In the introduction, we have given a qualitative description about the need for finding a robust policy. In this section, we give a formal argument to show that the worst case performance of a non-robust policy can be arbitrarily bad (as bad as a random policy) when compared to that of a robust policy. 
We consider a simple setting with an uncertainty set that contains only two models, i.e., P = {P o, P ′}. Let π∗ be the optimal robust policy. Following the notation in (2), let πo = πP o and π′ = πP ′ be the nonrobust optimal policies when the model is P o and P ′, respectively. Assume that nominal model is P o and we decide to employ the non-robust policy πo. The worst case performance of πo is characterized by its robust value function V π 
o 
which is min{Vπo,P o , Vπo,P ′}. 
We now state the following result. 
Theorem 4 (Robustness Gap). There exists a robust MDP M with uncertainty set P = {P o, P ′}, discount factor γ ∈ (γo, 1], and state s1 ∈ S such that 
V π o 
(s1) ≤ V π ∗ (s1)− c/(1− γ), 
where c is a positive constant, π∗ is the optimal robust policy, and πo = πP o is the non-robust optimal policy when the model is P o. 
Theorem 4 states that the worst case performance of the non-robust policy πo is lower than that of the optimal robust policy π∗, and this performance gap is
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
Ω(1/(1 − γ)). Since |r(s, a)| ≤ 1,∀(s, a) ∈ S × A by assumption, ‖Vπ,P ‖ ≤ 1/(1 − γ) for any policy π and any model P . Therefore, the difference between the optimal (robust) value function and the (robust) value function of an arbitrary policy cannot be greater than O(1/(1− γ)). Thus the worst-case performance of the non-robust policy πo can be as bad as an arbitrary policy in an order sense. 
5 Sample Complexity Analysis 
In this section we explain the key ideas used in the analysis of the REVI algorithm for obtaining the sample complexity bound for each of the uncertainty sets. Recall that we consider an RMDP M and its empirical estimate version as M̂ . 
To bound ‖V ∗ − V πK‖, we split it into three terms as 
‖V ∗−V πK‖ ≤ ‖V ∗−V̂ ∗‖+‖V̂ ∗−V̂ πK‖+‖V̂ πK−V πK‖, and analyze each term separately. 
Analyzing the second term, ‖V̂ ∗ − V̂ πK‖, is similar to that of non-robust algorithms. Due to the contraction property of the robust Bellman operator, it is straight forward to show that ‖V̂ ∗ − V̂ πk+1‖ ≤ γ‖V̂ ∗ − V̂ πk‖ for any k. This exponential convergence, with some additional results from the MDP theory, enables us to get a bound ‖V̂ ∗ − V̂ πK‖ ≤ 2γK+1/(1− γ)2. 
The analysis of terms ‖V ∗−V̂ ∗‖ and ‖V̂ πK−V πK‖ are however non-trivial and significantly more challenging compared to the non-robust setting. We will focus on the latter, and the analysis of the former is similar. 
For any policy π and for any state s, and denoting a = π(s), we have 
V π(s)− V̂ π(s) = γσPs,a(V π)− γσP̂s,a(V̂ π) 
= γ(σPs,a(V π)− σPs,a(V̂ π)) + γ(σPs,a(V̂ π)− σP̂s,a(V̂ π)) 
(13) 
To bound the first term in (13), we present a result that shows that σPs,a is 1-Lipschitz in the sup-norm. 
Lemma 1. For any (s, a) ∈ S×A and for any V1, V2 ∈ R|S|, we have |σPs,a(V1)− σPs,a(V2)| ≤ ‖V1 − V2‖ and |σP̂s,a(V1)− σP̂s,a(V2)| ≤ ‖V1 − V2‖. 
Using the above lemma, the first term in (13) will be 
bounded by γ‖V π−V̂ π‖ and the discount factor makes this term amenable to getting a closed form bound. 
Obtaining a bound for σPs,a(V̂ π) − σP̂s,a(V̂ π) is the 
most challenging part of our analysis. In the nonrobust setting, this will be equivalent to the error term P os,aV − P̂s,aV , which is unbiased and can be easily bounded using concentration inequalities. In the robust setting, however, because of the nonlinear nature 
of the function σ(·), E[σP̂s,a(V̂ π)] 6= σPs,a(V̂ π). So, 
using concentration inequalities to get a bound is not immediate. Our strategy is to find appropriate upperbound for this term that is amenable to using concentration inequalities. To that end, we will analyze this term separately for each of the three uncertainty set. 
5.1 Total variation uncertainty set 
We will first get following upperbound: 
Lemma 2 (TV uncertainty set). Let V = {V ∈ R|S| : ‖V ‖ ≤ 1/(1− γ)}. For any (s, a) ∈ S ×A and for any V ∈ V, 
|σP̂tv s,a 
(V )− σPtv s,a 
(V )| ≤ 2 max µ∈V |P̂s,aµ− P os,aµ|. (14) 
While the term |P̂s,aµ − P os,aµ| in (14) can be upperbounded using the standard Hoeffding’s inequality, bounding maxµ∈V |P̂s,aµ − P os,aµ| is more challenging as it requires a uniform bound. Since µ can take a continuum of values, a simple union bound argument will also not work. We overcome this issue by using a covering number argument and obtain the following bound. 
Lemma 3. Let V ∈ R|S| with ‖V ‖ ≤ 1/(1 − γ). For any η, δ ∈ (0, 1), 
max µ:0≤µ≤V 
max s,a |P̂s,aµ− P os,aµ| ≤ 
1 
1− γ 
√ |S| 2N 
log( 12|S||A| 
(δη(1− γ)) + 2η, 
with probability at least 1− δ/2. 
We note that this uniform bound adds an additional√ |S| factor compared to the non-robust setting, which 
results in an additional |S| in the sample complexity. Combining these, we finally get the following result. 
Proposition 1. Let V = {V ∈ R|S| : ‖V ‖ ≤ 1/(1 − γ)}. For any η, δ ∈ (0, 1), with probability at least 1−δ, 
max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )| ≤ Ctv 
u (N, η, δ), where, 
Ctv u (N, η, δ) = 4η + 
2 
1− γ 
√ |S| log(6|S||A|/(δη(1− γ))) 
2N . (15) 
Tracing back the steps to (13), we can get an arbitrary 
small bound for ‖V π − V̂ π‖ by selecting N appropriately, as specified in Theorem 1. 
5.2 Chi-square uncertainty set 
We will first get the following upperbound:
Kishan Panaganti, Dileep Kalathil 
Lemma 4 (Chi-square uncertainty set). For any (s, a) ∈ S ×A and for any V ∈ R|S|, ‖V ‖ ≤ 1/(1− γ), 
|σP̂c s,a 
(V )− σPc s,a 
(V )| ≤ 
max µ:0≤µ≤V 
| √ crVarP̂s,a(V − µ)− 
√ crVarP os,a(V − µ)| 
+ max µ:0≤µ≤V 
|P̂s,a(V − µ)− P os,a(V − µ)|. (16) 
The second term of (16) can be bounded using Lemma 3. However, the first term, which involves the squareroot of the variance is more challenging. We use a concentration inequality that is applicable for variance to overcome this challenge. Finally, we get the following result. 
Proposition 2. Let V = {V ∈ R|S| : ‖V ‖ ≤ 1/(1 − γ)}. For any η, δ ∈ (0, 1), with probability at least (1− δ), 
max V ∈V 
max s,a |σP̂c 
s,a (V )− σPc 
s,a (V )| ≤ Cc 
u(N, η, δ), where, 
Cc u(N, η, δ) ≤ 
√ 32ηcr 1− γ 
+ 2η+ 
1 
1− γ 
√ (2cr + 1)|S| log(12|S||A|/(δη(1− γ))) 
N , (17) 
Now, by selecting appropriate N as specified in Theo-rem 2, we can show the ε-optimality of πK . 
The details on the KL uncertainty set analysis is included in the appendix. 
6 Experiments 
In this section we demonstrate the convergence behavior and robust performance of our REVI algorithm using numerical experiments. We consider two different settings, namely, the Gambler’s Problem environment (Sutton and Barto, 2018, Example 4.3) and FrozenLake8x8 environment in OpenAI Gym (Brock-man et al., 2016). We also consider the TV uncertainty set and chi-square uncertainty set. We solve the optimization problem σP̂ and σP using the Scipy (Virtanen et al., 2020) optimization library. 
We illustrate the following important characteristics of the REVI algorithm: 
(1) Rate of convergence with respect to the number of iterations: To demonstrate this, we plot ‖Vk − V ∗‖ against the iteration number k, where Vk is the value at the kth step of the REVI algorithm with N = 5000. We compute V ∗ using the full knowledge of the uncertainty set for benchmarking the performance of the REVI algorithm. 
(2) Rate of convergence with respect to the number of samples: To show this, we plot ‖VK(N)− V ∗‖ against the number of samples N , where VK(N) is final value obtained from the REVI algorithm using N samples. (3) Robustness of the learned policy: To demonstrate this, we plot the number of times the robust policy πK (obtained from the REVI algorithm) successfully completed the task as a function of the change in an environment parameter. We perform 1000 trials for each environment and each uncertainty set, and plot the fraction of the success. 
Gambler’s Problem: In gambler’s problem, a gambler starts with a random balance in her account and makes bets on a sequence of coin flips, winning her stake with heads and losing with tails, until she wins $100 or loses all money. This problem can be formulated as a chain MDP with states in {1, · · · , 99} and when in state s the available actions are in {0, 1, · · · ,min(s, 100 − s)}. The agent is rewarded 1 after reaching a goal and rewarded 0 in every other timestep. The biased coin probability is fixed throughout the game. We denote its heads-up probability as ph and use 0.6 as a nominal model for training our algorithm. We also fix cr = 0.2 for the chi-square uncertainty set experiments and cr = 0.4 for the TV uncertainty set experiments. 
The red curves with square markers in the first two plots in Fig. 1 show the rate of convergence with respect to the number of iterations for TV and chisquare uncertainty sets respectively. As expected, convergence is fast due to the contraction property of the robust Bellman operator. 
The blue curves with triangle markers in the first two plots in Fig. 1 show the rate of convergence with respect to the number of samples for TV and chi-square uncertainty sets. We generated these curves for 10 different seed runs. The bold line depicts the mean of these runs and the error bar is the standard deviation. As expected, the plots show that VK(N) converges to V ∗ as N increases. 
We then demonstrate the robustness of the approximate robust policy πK (obtained with N = 100, 500, 3000) by evaluating its performance on environments with different values of ph. We plot the fraction of the wins out of 1000 trails. We also plot the performance the optimal robust policy π∗ as a benchmark. The third and fourth plot in Fig. 1 show the results with TV and chi-square uncertainty sets respectively. We note that the performance of the non-robust policy decays drastically as we decrease the parameter ph from its nominal value 0.6. On the other hand, the optimal robust policy performs consistently better under this change in the environment. We also note that
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
 
 
 
 
 
 
 
 
nRn-rRbust Rptimal rRbust Rptimal rRbust, N 100 rRbust, N 500 rRbust, N 3000 
1 2 3 4 5 6 7 
iteration k ■ 
0.1 
0.2 
0.3 
0.4 
0.5 
||V 
k 
− V 
* | | 
■ 
102 103 
N samples ▾ 
0.0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
||V 
K 
− V 
* | | 
▾ 
TV uncertainty set 
1 2 3 4 5 6 
iteration k ■ 
0.00 
0.05 
0.10 
0.15 
0.20 
0.25 
0.30 
0.35 
||V 
k 
− V 
* | | 
■ 
102 103 
N samples ▾ 
0.05 
0.10 
0.15 
0.20 
||V 
K 
− V 
* | | 
▾ 
chi-square uncertainty set 
0.2 0.3 0.4 0.5 0.6 0.7 
Test heads-up probability 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Ra tio 
 o f w 
in ni 
ng  in 
 1 00 
0 ga 
m es TV uncertainty set 
0.2 0.3 0.4 0.5 0.6 0.7 
Test heads-up probability 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Ra tio 
 o f w 
in ni 
ng  in 
 1 00 
0 ga 
m es chi-square uncertainty set 
Figure 1: Experiment results for the Gambler’s problem. The first two plots shows the rate of convergence with respect to the number of iterations (k) and the rate of convergence with respect to the number of samples (N) for the TV and chi-square uncertainty set, respectively. The third and fourth plots shows the robustness of the learned policy against changes in the model parameter (heads-up probability). 
0.0 0.1 0.2 0.3 0.4 0.5 3rRbability Rf picking randRP actiRn 
0.0 
0.2 
0.4 
0.6 
0.8 
 
 
 
nRn-rRbust RptiPal rRbust RptiPal rRbust, N 50 rRbust, N 1000 rRbust, N 3000 
0 25 50 75 100 125 150 175 
iteration k ■ 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
||V 
k 
− V 
* | | 
■ 
102 103 
N samples ▾ 
0.10 
0.12 
0.14 
0.16 
0.18 
||V 
K 
− V 
* | | 
▾TV uncertainty set 
0 2 4 6 8 10 12 
iteration k ■ 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
||V 
k 
− V 
* | | 
■ 
102 103 
N samples ▾ 
0.09 
0.10 
0.11 
0.12 
0.13 
0.14 
0.15 
0.16 
||V 
K 
− V 
* | | 
▾ 
chi-square uncertainty set 
0.0 0.1 0.2 0.3 0.4 0.5 
Probability of picking random action 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Ra tio 
 o f w 
in ni 
ng  in 
 1 00 
0 ga 
m es TV uncertainty set 
0.0 0.1 0.2 0.3 0.4 0.5 
Probability of picking random action 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Ra tio 
 o f w 
in ni 
ng  in 
 1 00 
0 ga 
m es chi-square uncertainty set 
Figure 2: Experiment results for the FrozenLake8x8 environment. The first two plots shows the rate of convergence with respect to the number of iterations (k) and the rate of convergence with respect to the number of samples (N) for the TV and chi-square uncertainty set, respectively. The third and fourth plots shows the robustness of the learned policy against changes in the model parameter (probability of picking a random action). 
πK(N) closely follows the performance of π∗ for large enough N . 
Frozen Lake environment: FrozenLake8x8 is a gridworld environment of size 8×8. It consists of some flimsy tiles which makes the agent fall into the water. The agent is rewarded 1 after reaching a goal tile without falling and rewarded 0 in every other timestep. We use the FrozenLake8x8 environment with default design as our nominal model except that we make the probability of transitioning to a state in the intended direction to be 0.4 (the default value is 1/3). We also set cr = 0.35 for the chi-square uncertainty set experiments and cr = 0.7 for the TV uncertainty set experiments. 
The red curves in the first two plots in Fig. 2 show the rate of convergence with respect to the number of iterations for TV and chi-square uncertainty sets respectively. The blue curves in the first two plots in Fig. 2 show the rate of convergence with respect to the number of samples for TV and chi-square uncertainty sets respectively. The behavior is similar to the one observed in the case of gambler’s problem. 
We demonstrate the robustness of the learned policy by evaluating it on FrozenLake test environments with action perturbations. In the real-world settings, due 
to model mismatch or noise in the environments, the resulting action can be different from the intended action. We model this by picking a random action with some probability at each time step. In addition, we change the probability of transitioning to a state in the intended direction to be 0.2 for these test environments. We observe that the performance of the robust RL policy is consistently better than the non-robust policy as we introduce model mismatch in terms of the probability of picking random actions. We also note that πK(N) closely follows the performance of π∗ 
for large enough N . 
We note that we have included our code for experiments in this GitHub page. We note that we can employ a hyperparameter learning strategy to find the best value of cr. We demonstrate this on the FrozenLake environment for the TV uncertainty set. We computed the optimal robust policy for each cr ∈ {0.1, 0.2, . . . , 1.6}. We tested these policies across 1000 games with random action probabilities {0.1, 0.2, . . . , 0.5} on the test environment. We found that the policy for cr = 1.2 has the best winning ratio across all the random action probabilities. We do not exhibit exhaustive experiments on this hyperparameter learning strategy as it is out of scope of the intent of this manuscript.
Kishan Panaganti, Dileep Kalathil 
7 Conclusion and Future Work 
We presented a model-based robust reinforcement learning algorithm called Robust Empirical Value Iter-ation algorithm, where we used an approximate robust Bellman updates in the vanilla robust value iteration algorithm. We provided a finite sample performance characterization of the learned policy with respect to the optimal robust policy for three different uncertainty sets, namely, the total variation uncertainty set, the chi-square uncertainty set, and the Kullback-Leibler uncertainty set. We also demonstrated the performance of REVI algorithm on two different environments showcasing its theoretical properties of convergence. We also showcased the REVI algorithm based policy being robust to the changes in the environment as opposed to the non-robust policies. 
The goal of this work was to develop the fundamental theoretical results for the finite state space and action space regime. As mentioned earlier, the sub-optimality of the sample complexity of our REVI algorithm in factors |S| and 1/(1−γ) needs more investigation and refinements in the analyses. In the future, we will extend this idea to robust RL with linear and nonlinear function approximation architectures and for more general models in deep RL. 
Acknowledgments 
Dileep Kalathil gratefully acknowledges funding from the U.S. National Science Foundation (NSF) grants NSF-EAGER-1839616, NSF-CRII-CPS-1850206 and NSF-CAREER-EPCN-2045783. 
References 
Agarwal, A., Kakade, S., and Yang, L. F. (2020). Model-based reinforcement learning with a generative model is minimax optimal. In Conference on Learning Theory, pages 67–83. 2, 5 
Azar, M. G., Munos, R., and Kappen, H. J. (2013). Minimax PAC bounds on the sample complexity of reinforcement learning with a generative model. Mach. Learn., 91(3):325–349. 2, 4, 5 
Borkar, V. S. (2002). Q-learning for risk-sensitive control. Mathematics of operations research, 27(2):294– 311. 3 
Brockman, G., Cheung, V., Pettersson, L., Schneider, J., Schulman, J., Tang, J., and Zaremba, W. (2016). Openai gym. arXiv preprint arXiv:1606.01540. 7 
Derman, E., Mankowitz, D., Mann, T., and Mannor, S. (2020). A bayesian approach to robust reinforcement learning. In Uncertainty in Artificial Intelli-gence, pages 648–658. 1 
Derman, E., Mankowitz, D. J., Mann, T. A., and Mannor, S. (2018). Soft-robust actor-critic policygradient. In AUAI press for Association for Uncer-tainty in Artificial Intelligence, pages 208–218. 1, 2 
Dullerud, G. E. and Paganini, F. (2013). A course in robust control theory: a convex approach, volume 36. Springer Science & Business Media. 3 
Haskell, W. B., Jain, R., and Kalathil, D. (2016). Em-pirical dynamic programming. Mathematics of Op-erations Research, 41(2):402–429. 2 
Iyengar, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280. 1, 3, 4, 13, 14, 15, 18 
Kalathil, D., Borkar, V. S., and Jain, R. (2021). Empirical Q-Value Iteration. Stochastic Systems, 11(1):1–18. 2 
Li, G., Wei, Y., Chi, Y., Gu, Y., and Chen, Y. (2020). Breaking the sample size barrier in model-based reinforcement learning with a generative model. In Advances in Neural Information Processing Sys-tems, volume 33, pages 12861–12872. 2, 3, 5 
Lim, S. H. and Autef, A. (2019). Kernel-based reinforcement learning in robust Markov decision processes. In International Conference on Machine Learning, pages 3973–3981. 2 
Lim, S. H., Xu, H., and Mannor, S. (2013). Reinforce-ment learning in robust Markov decision processes. In Advances in Neural Information Processing Sys-tems, pages 701–709. 2 
Mankowitz, D. J., Levine, N., Jeong, R., Abdolmaleki, A., Springenberg, J. T., Shi, Y., Kay, J., Hester, T., Mann, T., and Riedmiller, M. (2020). Robust reinforcement learning for continuous control with model misspecification. In International Conference on Learning Representations. 1, 2 
Mannor, S., Mebel, O., and Xu, H. (2016). Robust mdps with k-rectangular uncertainty. Mathematics of Operations Research, 41(4):1484–1509. 1 
Maurer, A. and Pontil, M. (2009). Empirical bernstein bounds and sample-variance penalization. In COLT 2009 - The 22nd Conference on Learning Theory, Montreal, Quebec, Canada, June 18-21, 2009. 11 
Nilim, A. and El Ghaoui, L. (2005). Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798. 1, 4, 18, 21 
Panaganti, K. and Kalathil, D. (2021). Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In Proceedings of the 38th International Conference on Machine Learning, pages 511–520. 1, 2
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
Petrik, M. and Subramanian, D. (2014). Raam: The benefits of robustness in approximating aggregated mdps in reinforcement learning. In NIPS, pages 1979–1987. 2 
Pinto, L., Davidson, J., Sukthankar, R., and Gupta, A. (2017). Robust adversarial reinforcement learning. In International Conference on Machine Learning, pages 2817–2826. 1, 3 
Roy, A., Xu, H., and Pokutta, S. (2017). Reinforce-ment learning under model mismatch. In Advances in Neural Information Processing Systems, pages 3043–3052. 1, 2 
Russel, R. H. and Petrik, M. (2019). Beyond confidence regions: Tight bayesian ambiguity sets for robust mdps. Advances in Neural Information Pro-cessing Systems. 1 
Sidford, A., Wang, M., Wu, X., Yang, L. F., and Ye, Y. (2018). Near-optimal time and sample complexities for solving markov decision processes with a generative model. In Proceedings of the 32nd International Conference on Neural Information Processing Sys-tems, pages 5192–5202. 2, 5 
Singh, S. P. and Yee, R. C. (1994). An upper bound on the loss from approximate optimal-value functions. Machine Learning, 16(3):227–233. 2, 14 
Sutton, R. S. and Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press. 7 
Tamar, A., Mannor, S., and Xu, H. (2014). Scaling up robust mdps using function approximation. In In-ternational Conference on Machine Learning, pages 181–189. 2 
van Handel, R. (2014). Probability in High Dimension. Technical report, Princeton University NJ. 11 
Vershynin, R. (2018). High-Dimensional Probability: An Introduction with Applications in Data Science, volume 47. Cambridge University press. 11 
Virtanen, P., Gommers, R., Oliphant, T. E., Haber-land, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N., Nelson, A. R. J., Jones, E., Kern, R., Larson, E., Carey, C. J., Polat, İ., Feng, Y., Moore, E. W., VanderPlas, J., Laxalde, D., Perktold, J., Cimrman, R., Henriksen, I., Quintero, E. A., Harris, C. R., Archibald, A. M., Ribeiro, A. H., Pedregosa, F., van Mulbregt, P., and SciPy 1.0 Contributors (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17:261–272. 7 
Wiesemann, W., Kuhn, D., and Rustem, B. (2013). Robust Markov decision processes. Mathematics of Operations Research, 38(1):153–183. 1 
Xu, H. and Mannor, S. (2010). Distributionally robust Markov decision processes. In Advances in Neural Information Processing Systems, pages 2505–2513. 1 
Yang, W., Zhang, L., and Zhang, Z. (2021). Towards theoretical understandings of robust markov decision processes: Sample complexity and asymptotics. arXiv preprint arXiv:2105.03863. 2 
Yu, P. and Xu, H. (2015). Distributionally robust counterpart in Markov decision processes. IEEE Transactions on Automatic Control, 61(9):2538– 2543. 1 
Zhang, H., Chen, H., Xiao, C., Li, B., Liu, M., Boning, D., and Hsieh, C.-J. (2020a). Robust deep reinforcement learning against adversarial perturbations on state observations. Advances in Neural Information Processing Systems, 33:21024–21037. 1 
Zhang, K., Hu, B., and Basar, T. (2020b). Policy optimization for H2 linear control with H∞ robustness guarantee: Implicit regularization and global convergence. In Proceedings of the 2nd Annual Conference on Learning for Dynamics and Control, L4DC 2020, Online Event, Berkeley, CA, USA, 11-12 June 2020, volume 120 of Proceedings of Machine Learning Research, pages 179–190. 3 
Zhou, K., Doyle, J. C., Glover, K., et al. (1996). Robust and optimal control, volume 40. Prentice hall New Jersey. 3 
Zhou, Z., Bai, Q., Zhou, Z., Qiu, L., Blanchet, J., and Glynn, P. (2021). Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 3331–3339. 2, 5, 17
Kishan Panaganti, Dileep Kalathil 
Appendix 
A Useful Technical Results 
In this section we state some existing results that are useful in our analysis. 
Lemma 5 (Hoeffding’s inequality (Vershynin, 2018, Theorem 2.2.6)). Let X1, · · · , XT be independent random variables. Assume that Xt ∈ [mt,Mt] for every t with Mt > mt. Then, for any ε > 0, we have 
P 
( T∑ t=1 
(Xt − E[Xt]) ≥ ε 
) ≤ exp 
( − 2ε2∑T 
t=1(Mt −mt)2 
) . 
Lemma 6 (Self-bounding variance inequality (Maurer and Pontil, 2009, Theorem 10)). Let X1, · · · , XT be in-dependent and identically distributed random variables with finite variance, that is, Var(X1) <∞. Assume that 
Xt ∈ [0,M ] for every t with M > 0, and let S2 T = 1 
T 
∑T t=1X 
2 t − ( 1 
T 
∑T t=1Xt) 
2. Then, for any ε > 0, we have 
P ( |ST − 
√ Var(X1)| ≥ ε 
) ≤ 2 exp 
( − Tε2 
2M2 
) . 
Proof. The proof of this lemma directly follows from (Maurer and Pontil, 2009, Theorem 10) by noting that we can rewrite S2 
T as follows 
T 
T − 1 S2 T = 
1 
T (T − 1) 
T∑ i,j=1 
(Xi −Xj) 2. 
Also, note that we apply (Maurer and Pontil, 2009, Theorem 10) for the scaled random variables Xt/M ∈ [0, 1]. 
We now provide a covering number result that is useful to get high probability concentration bounds for value function classes. We first define minimal η-cover of a set. 
Definition 1 (Minimal η-cover; (van Handel, 2014, Definition 5.5)). A set NV(η) is called an η-cover for a metric space (V, d) if for every V ∈ V, there exists a V ′ ∈ N such that d(V, V ′) ≤ η. Furthermore, NV(η) with the minimal cardinality (|NV(η)|) is called a minimal η-cover. 
From (van Handel, 2014, Exercise 5.5 and Lemma 5.13) we have the following result. 
Lemma 7 (Covering Number). Let V = {V ∈ R|S| : ‖V ‖ ≤ Vmax}. Let NV(η) be a minimal η-cover of V with respect to the distance metric d(V, V ′) = ‖V − V ′‖ for some fixed η ∈ (0, 1). Then we have 
log |NV(η)| ≤ |S| · log 
( 3Vmax 
η 
) . 
Proof. We will consider the normalized metric space (Vn, dn), where 
Vn := V/Vmax = {V ∈ R|S| : ‖V ‖ ≤ 1} 
and dn := d/Vmax to make use of the fact that the covering number is invariant to the scaling of a metric space. Let ηn := η/Vmax. Then, it follows from (van Handel, 2014, Exercise 5.5 and Lemma 5.13) that 
log |NV(η)| = log |NVn(ηn)| ≤ |S| · log 
( 3 
ηn 
) = |S| · log 
( 3Vmax 
η 
) . 
This completes the proof. 
Here we present another covering number result, with a similar proof as Lemma 7, that is useful to get our upperbound for the KL uncertainty set. 
Lemma 8 (Covering Number of a bounded real line). Let Θ ⊂ R with Θ = [l, u] for some real numbers u > l. Let NΘ(η) be a minimal η-cover of Θ with respect to the distance metric d(θ, θ′) = |θ − θ′| for some fixed η ∈ (0, 1). Then we have |NΘ(η)| ≤ 3(u− l)/η.
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
B Proof of the Theorems 
B.1 Concentration Results 
Here, we prove Lemma 3. We state the following result first. 
Lemma 9. For any V ∈ R|S| with ‖V ‖ ≤ Vmax, with probability at least 1− δ, 
max (s,a) |P os,aV − P̂s,aV | ≤ Vmax 
√ log(2|S||A|/δ) 
2N 
Proof. Fix any (s, a) pair. Consider a discrete random variable X taking value V (j) with probability P os,a(j) for all j ∈ {1, 2, · · · , |S|}. From Hoeffding’s inequality (Lemma 5), we have 
P(P os,aV − P̂s,aV ≥ ε) ≤ exp(−2Nε2/V 2 max), P(P̂s,aV − P os,aV ≥ ε) ≤ exp(−2Nε2/V 2 
max). 
Choosing ε = Vmax 
√ log(2|S||A|/δ) 
2N , we get P(|P os,aV − P̂s,aV | ≥ Vmax 
√ log(2|S||A|/δ) 
2N ) ≤ δ |S||A| . Now, using union 
bound, we get 
P(max (s,a) |P os,aV − P̂s,aV | ≥ Vmax 
√ log(2|S||A|/δ) 
2N ) ≤ 
∑ s,a 
P(|P os,aV − P̂s,aV | ≥ Vmax 
√ log(2|S||A|/δ) 
2N )≤ δ. 
This completes the proof. 
Proof of Lemma 3: Let V = {V ∈ R|S| : ‖V ‖∞ ≤ 1/(1 − γ)}. Let NV(η) be a minimal η-cover of V. Fix a µ ≤ V . By the definition of NV(η), there exists a µ′ ∈ NV(η) such that ‖µ− µ′‖ ≤ η. Now, for these particular µ and µ′, we get 
|P̂s,aµ− P os,aµ| ≤ |P̂s,aµ− P̂s,aµ′|+ |P̂s,aµ′ − P os,aµ′|+ |P os,aµ′ − P os,aµ| (a) 
≤ ‖P̂s,a‖1‖µ− µ′‖∞ + |P̂s,aµ′ − P os,aµ′|+ ‖P os,a‖1‖µ′ − µ‖∞ ≤ sup µ′∈NV(η) 
max s,a |P̂s,aµ′ − P os,aµ′|+ 2η 
where (a) follows from Hölder’s inequality. Now, taking max on both sides with respect to µ and (s, a) we get 
sup µ∈V 
max s,a |P̂s,aµ− P os,aµ| ≤ sup 
µ′∈NV(η) 
max s,a |P̂s,aµ′ − P os,aµ′|+ 2η 
(b) 
≤ 1 
1− γ 
√ log(4|S||A||NV(η)|/δ) 
2N + 2η 
(c) 
≤ 1 
1− γ 
√ |S| log(12|S||A|/(δη(1− γ))) 
2N + 2η, 
with probability at least 1 − δ/2. Here, (b) follows from Lemma 9 and the union bound and (c) from Lemma 7. 
B.2 Proof of Theorem 1 
Proof of Lemma 1. We only prove the first inequality since the proof is analogous for the other inequality. For any (s, a) ∈ S ×A we have 
σPs,a(V2)− σPs,a(V1) = inf q∈Ps,a 
q>V2 − inf q̃∈Ps,a 
q̃>V1 = inf q∈Ps,a 
sup q̃∈Ps,a 
q>V2 − q̃>V1 
≥ inf q∈Ps,a 
q>(V2 − V1) = σPs,a(V2 − V1). (18)
Kishan Panaganti, Dileep Kalathil 
By definition, for any arbitrary ε > 0, there exists a Ps,a ∈ Ps,a such that 
P>s,a(V2 − V1)− ε ≤ σPs,a(V2 − V1). (19) 
Using (19) and (18), 
σPs,a(V1)− σPs,a(V2) ≤ P>s,a(V1 − V2) + ε (a) 
≤ ‖Ps,a‖1‖V1 − V2‖+ ε = ‖V1 − V2‖+ ε 
where (a) follows from Holder’s inequality. Since ε is arbitrary, we get, σPs,a(V1) − σPs,a(V2) ≤ ‖V1 − V2‖. Exchanging the roles of V1 and V2 completes the proof. 
Proof of Lemma 2. Fix any (s, a) pair. From (Iyengar, 2005, Lemma 4.3) we have that 
σPtv s,a 
(V ) = P os,aV + max µ:0≤µ≤V 
( − P os,aµ− cr max 
s (Vµ(s)) + cr min 
s (Vµ(s)) 
) (20) 
σP̂tv s,a 
(V ) = P̂s,aV + max µ:0≤µ≤V 
( − P̂s,aµ− cr max 
s (Vµ(s)) + cr min 
s (Vµ(s)) 
) , (21) 
where 0 ≤ µ ≤ V is an elementwise inequality and Vµ(s) = V (s)− µ(s) for all s ∈ S. 
Using the fact that |maxx f(x)−maxx g(x)| ≤ maxx |f(x)− g(x)|, it directly follows that 
|σP̂tv s,a 
(V )− σPtv s,a 
(V )| ≤ |P̂s,aV − P os,aV |+ max µ:0≤µ≤V 
|P̂s,aµ− P os,aµ|. 
Further simplifying we get 
|σP̂tv s,a 
(V )− σPtv s,a 
(V )| ≤ |P̂s,aV − P os,aV |+ max µ:0≤µ≤V 
|P̂s,aµ− P os,aµ| 
≤ max µ∈V |P̂s,aµ− P os,aµ|+ max 
µ:0≤µ≤V |P̂s,aµ− P os,aµ| ≤ 2 max 
µ∈V |P̂s,aµ− P os,aµ|. 
This completes the proof. 
We are now ready to prove Proposition 1. 
Proof of Proposition 1. For any given V ∈ V and (s, a), from Lemma 2, we have 
|σP̂tv s,a 
(V )− σPtv s,a 
(V )| ≤ 2 max µ∈V |P̂s,aµ− P os,aµ| ≤ 2 max 
µ∈V max s,a |P̂s,aµ− P os,aµ|. 
Taking the maximum over V and (s, a) on both sides, we get 
max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )| ≤ 2 max 
µ∈V max s,a |P̂s,aµ− P os,aµ|. (22) 
Now, from the proof of Lemma 3, for any η, δ ∈ (0, 1), we get 
max µ∈V 
max s,a |P̂s,aµ− P os,aµ| ≤ 
1 
1− γ 
√ |S| log(6|S||A|/(δη(1− γ))) 
2N + 2η, (23) 
with probability greater than 1− δ. Using (23) in (22), we get the desired result. 
We also need the following result that specifies the amplification when replacing the algorithm iterate value function with the value function of the policy towards approximating the optimal value. 
Lemma 10. Let Vk and Qk be as given in the REVI algorithm for k ≥ 1. Also, let πk = arg maxaQk(s, a). Then, 
‖V̂ ∗ − V̂ πk‖ ≤ 2γ 
1− γ ‖Vk − V̂ ∗‖. 
Furthermore, 
‖V ∗ − V πk‖ ≤ 2 
1− γ ‖Qk −Q∗‖.
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
Proof. The proof is similar to the proof in (Singh and Yee, 1994, Main Theorem, Corollary 2). A straight forward modification to this proof, using the fact that σP̂s,a and σPs,a are 1-Lipschitz functions as shown in Lemma 1, 
will give the desired result. 
Proof of Theorem 1. Recall the empirical RMDP M̂ = (S,A, r, P̂tv, γ). For any policy π, let V̂ π be robust 
value function of policy π with respect to the RMDP M̂ . The optimal robust policy, value function, and state-action value function of M̂ are denoted as π̂?, V̂ ? and Q̂?, respectively. Also, for any policy π, we have Q̂π(s, a) = r(s, a) + γσP̂tv 
s,a (V̂ π) and Qπ(s, a) = r(s, a) + γσPtv 
s,a (V π). 
Let Vk and Qk be as given in the REVI algorithm for k ≥ 1. Also, let πk(s) = arg maxaQk(s, a). Now, 
‖V ∗ − V πk‖ ≤ ‖V ∗ − V̂ ∗‖+ ‖V̂ ∗ − V̂ πk‖+ ‖V̂ πk − V πk‖. (24) 
1) Bounding the first term in (24): Let V = {V ∈ R|S| : ‖V ‖ ≤ 1/(1− γ)}. For any s ∈ S, 
V ∗(s)− V̂ ∗(s) = Q∗(s, π∗(s))− Q̂∗(s, π̂∗(s)) (a) 
≤ Q∗(s, π∗(s))− Q̂∗(s, π∗(s)) (b) = γσPtv 
s,π∗(s) (V ∗)− γσP̂tv 
s,π∗(s) (V̂ ∗) 
= γ(σPtv s,π∗(s) 
(V ∗)− σP̂tv s,π∗(s) 
(V ∗)) + γ(σP̂tv s,π∗(s) 
(V ∗)− σP̂tv s,π∗(s) 
(V̂ ∗)) 
(c) 
≤ γ(σPtv s,π∗(s) 
(V ∗)− σP̂tv s,π∗(s) 
(V ∗)) + γ‖V ∗ − V̂ ∗‖ 
≤ γ max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )|+ γ‖V ∗ − V̂ ∗‖ 
where (a) follows since π̂∗ is the robust optimal policy for M̂ , (b) follows from the definitions of Q∗ and Q̂∗, (c) 
follows from Lemma 1. Similarly analyzing for V̂ ∗(s)− V ∗(s), we get 
‖V ∗ − V̂ ∗‖ ≤ γ 
(1− γ) max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )|. (25) 
Now, using Proposition 1, with probability greater than 1− δ, we get 
‖V ∗ − V̂ ∗‖ ≤ γ 
(1− γ) Ctv u (N, η, δ), (26) 
where Ctv u (N, η, δ) is given in equation (15) in the statement of Proposition 1. 
2) Bounding the second term in (24): Let T̂ be the robust Bellman operator corresponding to M̂ . So, T̂ is 
a γ-contraction mapping and V̂ ∗ is its unique fixed point (Iyengar, 2005). The REVI iterates Vk, k ≥ 0, with 
V0 = 0, can now be expressed as Vk+1 = T̂ Vk. Using the properties of T̂ , we get 
‖Vk − V̂ ∗‖ = ‖T̂ Vk−1 − T̂ V̂ ∗‖ ≤ γ‖Vk−1 − V̂ ∗‖ ≤ · · · ≤ γk‖V0 − V̂ ∗‖ ≤ γk/(1− γ). (27) 
Now, using Lemma 10, we get 
‖V̂ πk − V̂ ∗‖ ≤ 2γk+1 
(1− γ)2 . (28) 
3) Bounding the third term in (24): This is similar to bounding the first term. For any s ∈ S, 
V πk(s)− V̂ πk(s) = Qπk(s, πk(s))− Q̂πk(s, πk(s)) = γσPs,πk(s) (V πk)− γσP̂s,πk(s) 
(V̂ πk) 
= γ(σPs,πk(s) (V πk)− σPs,πk(s) 
(V̂ πk)) + γ(σPs,πk(s) (V̂ πk)− σP̂s,πk(s) 
(V̂ πk)) 
(d) 
≤ γ‖V πk − V̂ πk‖+ γ(σPs,πk(s) (V̂ πk)− σP̂s,πk(s) 
(V̂ πk)) 
≤ γ‖V πk − V̂ πk‖+ γ max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )|
Kishan Panaganti, Dileep Kalathil 
where (d) follows from Lemma 1. Similarly analyzing for V̂ πk(s)− V πk(s), we get, 
‖V πk − V̂ πk‖ ≤ γ 
(1− γ) max V ∈V 
max s,a |σP̂tv 
s,a (V )− σPtv 
s,a (V )|. (29) 
Now, using Proposition 1, with probability greater than 1− δ, we get 
‖V πk − V̂ πk‖ ≤ γ 
(1− γ) Ctv u (N, η, δ). (30) 
Using (26) - (30) in (24), we get, with probability at least 1− 2δ, 
‖V ∗ − V πk‖ ≤ 2γk+1 
(1− γ)2 + 
2γ 
(1− γ) Ctv u (N, η, δ). (31) 
Using the value of Ctv u (N, η, δ) as given in Proposition 1, we get 
‖V ∗ − V πk‖ ≤ 2γk+1 
(1− γ)2 + 
4γ 
(1− γ)2 
√ |S| log(6|S||A|/(δη(1− γ))) 
2N + 
8γη 
(1− γ) (32) 
with probability at least 1− 2δ. 
Now, choose η = ε(1− γ)/(24γ). Since ε ∈ (0, 24γ/(1− γ)), this particular η is in (0, 1). Now, choosing 
k ≥ K0 = 1 
log(1/γ) log( 
6γ 
ε(1− γ)2 ), (33) 
N ≥ N tv = 72γ2 
(1− γ)4 
|S| log(144γ|S||A|/(δε(1− γ)2)) 
ε2 , (34) 
we get ‖V ∗ − V πk‖ ≤ ε with probability at least 1− 2δ. 
B.3 Proof of Theorem 2 
Proof of Lemma 4. Fix an (s, a) pair. From (Iyengar, 2005, Lemma 4.2), we have 
σPc s,a 
(V ) = max µ:0≤µ≤V 
( P os,a(V − µ)− 
√ crVarP os,a(V − µ) 
) , (35) 
where VarP os,a(V − µ) = P os,a(V − µ)2 − (P os,a(V − µ))2. We get a similar expression for σP̂c s,a 
(V ). Using these 
expressions, with the additional facts that |maxx f(x)−maxx g(x)| ≤ maxx |f(x)−g(x)| and maxx(f(x)+g(x)) ≤ maxx f(x) + maxx g(x), we get the desired result. 
We state the following concentration result that is useful for the proof of Proposition 2. 
Lemma 11. For any V ∈ R|S|+ with ‖V ‖ ≤ Vmax, with probability at least 1− δ, 
max (s,a) | √ 
VarP os,aV − √ 
VarP̂s,aV | ≤ Vmax 
√ 2 log(2|S||A|/δ) 
N 
Proof. Fix any (s, a) pair. Consider a discrete random variable X taking value V (j) with probability P os,a(j) for all j ∈ {1, 2, · · · , |S|}. From the Self-bounding variance inequality (Lemma 6), we have 
P(| √ 
VarP os,aV − √ 
VarP̂s,aV | ≥ ε) ≤ 2 exp(−Nε2/(2V 2 max)). 
Choosing ε = Vmax 
√ 2 log(2|S||A|/δ) 
N , we get P(|P os,aV − P̂s,aV | ≥ Vmax 
√ 2 log(2|S||A|/δ) 
N ) ≤ δ |S||A| . Now, using union 
bound, we get 
P(max (s,a) | √ 
VarP os,aV − √ 
VarP̂s,aV | ≥ Vmax 
√ 2 log(2|S||A|/δ) 
N ) 
≤ ∑ s,a 
P(| √ 
VarP os,aV − √ 
VarP̂s,aV | ≥ Vmax 
√ 2 log(2|S||A|/δ) 
N )≤ δ. 
This completes the proof.
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
We are now ready to prove Proposition 2. 
Proof of Proposition 2. Fix an (s, a) pair. From Lemma 4, for any given V ∈ V, we have 
|σP̂c s,a 
(V )− σPc s,a 
(V )| ≤ max µ:0≤µ≤V 
| √ crVarP̂s,a(V − µ)− 
√ crVarPos,a(V − µ)|+ max 
µ:0≤µ≤V |P̂s,a(V − µ)− P os,a(V − µ)|. 
By a simple variable substitution, we get 
|σP̂c s,a 
(V )− σPc s,a 
(V )| ≤ max µ∈V+ 
max s,a | √ crVarP̂s,aµ− 
√ crVarP os,aµ|+ max 
µ∈V max s,a |P̂s,aµ− P os,aµ|, 
which will give 
max V ∈V 
max s,a |σP̂c 
s,a (V )− σPc 
s,a (V )| ≤ max 
µ∈V+ 
max s,a | √ crVarP̂s,aµ− 
√ crVarP os,aµ|+ max 
µ∈V max s,a |P̂s,aµ− P os,aµ|, 
(36) 
where V+ = {V ∈ R|S|+ : ‖V ‖ ≤ 1/(1− γ)}. 
We will first bound the second term on the RHS of (36). From the proof of Lemma 3, for any η, δ ∈ (0, 1), we get 
max µ∈V 
max s,a |P̂s,aµ− P os,aµ| ≤ 
1 
1− γ 
√ |S| log(12|S||A|/(δη(1− γ))) 
2N + 2η, (37) 
with probability greater than 1− δ/2. 
Now, we will focus on the first term on the RHS of (36). Fix a µ ∈ V+. Consider a minimal η-cover NV+ (η) of 
the set V+. By definition, there exists µ′ ∈ NV+ (η) such that ‖µ− µ′‖ ≤ η. Now, following the same step as in 
the proof of Lemma 3, we get 
| √ 
VarP̂s,aµ− √ 
VarP os,aµ| ≤ | √ 
VarP̂s,aµ− √ 
VarP̂s,aµ ′|+ | 
√ VarP̂s,aµ 
′ − √ 
VarP os,aµ ′|+ | 
√ VarP os,aµ− 
√ VarP os,aµ 
′| 
(a) 
≤ | √ 
VarP̂s,aµ ′ − √ 
VarP os,aµ ′|+ 
√ |VarP̂s,aµ−VarP̂s,aµ 
′|+ √ |VarP os,aµ−VarP os,aµ 
′| 
(b) 
≤ | √ 
VarP̂s,aµ ′ − √ 
VarP os,aµ ′|+ 
√ |P̂s,a(µ2 − µ′2)|+ 
√ |(P̂s,aµ)2 − (P̂s,aµ′)2)|+√ 
|P os,a(µ2 − µ′2)|+ √ |(P os,aµ)2 − (P os,aµ 
′)2)| (c) 
≤ | √ 
VarP̂s,aµ ′ − √ 
VarP os,aµ ′|+ 
√ 32η 
1− γ 
≤ sup µ′∈NV+ 
(η) 
max s,a | √ 
VarP̂s,aµ ′ − √ 
VarP os,aµ ′|+ 
√ 32η 
1− γ 
where (a) follows from the fact | √ x − √y| ≤ 
√ |x− y| for all x, y ∈ R+, (b) follows from the fact | 
√ x+ y| ≤√ 
x + √ y for all x, y ∈ R+, and (c) follows by using the fact x2 − y2 = (x + y)(x − y), ‖µ‖ ≤ 1/(1 − γ), and 
‖µ′‖ ≤ 1/(1− γ) with Hölder’s inequality. Now, taking max on both sides with respect to µ and (s, a) we get 
sup µ∈V+ 
max s,a | √ 
VarP̂s,aµ− √ 
VarP os,aµ| ≤ sup µ′∈NV+ 
(η) 
max s,a | √ 
VarP̂s,aµ ′ − √ 
VarP os,aµ ′|+ 
√ 32η 
1− γ 
(d) 
≤ 1 
1− γ 
√ 2 log(4|S||A||NV+ 
(η)|/δ) N 
+ 
√ 32η 
1− γ (e) 
≤ 1 
1− γ 
√ 2|S| log(12|S||A|/(δη(1− γ))) 
N + 
√ 32η 
1− γ , (38) 
with probability at least 1− δ/2. Here, (d) follows from Lemma 11 and the union bound and (e) from Lemma 7.
Kishan Panaganti, Dileep Kalathil 
Applying (37) and (38) in (36), we get 
max V ∈V 
max s,a |σP̂c 
s,a (V )− σPc 
s,a (V )| ≤ 1 
1− γ 
√ 2cr|S| log(12|S||A|/(δη(1− γ))) 
N + 
√ 32ηcr 1− γ 
+ 1 
1− γ 
√ |S| log(12|S||A|/(δη(1− γ))) 
2N + 2η, 
with probability greater than 1− δ. This completes the proof. 
Proof of Theorem 2. The basic steps of the proof is similar to that of Theorem 1. So, we present only the important steps. 
Following the same steps as given before (26) and using Proposition 2, we get, with probability greater than 1− δ, 
‖V ∗ − V̂ ∗‖ ≤ γ 
(1− γ) Cc u(N, η, δ) (39) 
Similarly, following the steps as given before (28), we get 
‖V̂ πk − V̂ ∗‖ ≤ 2γk+1 
(1− γ)2 . (40) 
In the same vein, following the steps as given before (30) and using Proposition 2, we get, with probability greater than 1− δ, 
‖V πk − V̂ πk‖ ≤ γ 
(1− γ) Cc u(N, η, δ). (41) 
Using (39) - (41), similar to (31), we get, with probability greater than 1− 2δ, 
‖V ∗ − V πk‖ ≤ 2γk+1 
(1− γ)2 + 
2γ 
(1− γ) Cc u(N, η, δ). (42) 
Using the value of Cc u(N, η, δ) as given in Proposition 2, we get, with probability greater than 1− 2δ, 
‖V ∗ − V πk‖ ≤ 2γk+1 
(1− γ)2 + 
8γ √ 
2ηcr (1− γ)3/2 
+ 4γη 
1− γ + 
2γ 
(1− γ)2 
√ (2cr + 1)|S| log(12|S||A|/(δη(1− γ))) 
N . 
We can now choose k, ε, η to make each of the term on the RHS of the above inequality small. In particular, we select ε ∈ (0,min{16γ/(1− γ), 32γ 
√ 2cr/(1− γ)3/2}) and η = min{ε(1− γ)/(16γ), ε2(1− γ)3/(2048crγ 
2)}. Note that this choice also ensure η ∈ (0, 1). Now, by choosing 
k ≥ K0 = 1 
log(1/γ) · log( 
8γ 
ε(1− γ)2 ), (43) 
N ≥ N c = 64γ2 
(1− γ)4 · (2cr + 1)|S| log(12|S||A|/(δη(1− γ))) 
ε2 , (44) 
we will get ‖V ∗ − V πk‖ ≤ ε with probability at least 1− 2δ. 
B.4 Proof of Theorem 3 
We state a result from (Zhou et al., 2021) that will be useful in the proof of Theorem 3. 
Lemma 12 ((Zhou et al., 2021, Lemma 4) ). Fix any δ ∈ (0, 1). Let X ∼ P be a bounded random variable with X ∈ [0,M ] and let PN denote the empirical distribution of P with N samples. For t > 0, for any 
λ∗ ∈ arg max λ≥0 
{−λ log(EP [exp(−X/λ)])− λt} ,
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
(1) λ∗ = 0. Furthermore, let the support of X be finite. Then there exists a problem dependent constant 
N ′(δ, t, P ) := max{log(2/δ)/ log(1/(1− min x∈supp(X) 
P (X = x))) , 2M2 log(4/δ)/(P (X = ess inf X)− exp(−t))2}, 
such that for N ≥ N ′(δ, t, P ) we have, with probability at least 1− δ, 
0 ∈ arg max λ≥0 
{−λ log(EPN [exp(−X/λ)])− λt} . 
(2) λ∗ > 0. Then there exists a problem dependent constant 
N ′′(δ, t, P ) := max λ∈{λ,λ∗,M/t} 
8M2 exp(2M/λ) 
τ2 log(6/δ), 
where λ = λ∗/2 > 0 (independent of N) and 
τ = min{λ log(EP [exp(−X/λ)]) + λt, (M/t) log(EP [exp(−tX/M)]) +M} − (λ∗ log(EP [exp(−X/λ∗)]) + λ∗t) > 0, 
such that for N ≥ N ′′(δ, t, P ), with probability at least 1− δ, there exists a 
λ̂∗ ∈ arg max λ≥0 
{−λ log(EPN [exp(−X/λ)])− λt} , 
such that λ∗, λ̂∗ ∈ [λ,M/t]. 
We now prove the following result. 
Lemma 13. For any (s, a) ∈ S ×A and for any V ∈ R|S| with ‖V ‖ ≤ 1/(1− γ), 
|σP̂kl s,a 
(V )− σPkl s,a 
(V )| ≤ exp(1/λkl(1− γ)) 
cr(1− γ) max 
λ∈[λkl, 1 
cr(1−γ) ] |(P os,a − P̂s,a) exp(−V/λ)| (45) 
holds with probability at least 1 − δ/(2|S||A|) for N ≥ max{N ′(δ/(4|S||A|), cr, P os,a), N ′′(δ/(4|S||A|), cr, P os,a)}, where both N ′, N ′′ are defined as in Lemma 12. 
Proof. Fix any (s, a) pair. From (Iyengar, 2005, Lemma 4.1), we have 
σPkl s,a 
(V ) = max λ≥0 
(−crλ− λ log(P os,a exp(−V/λ))), σP̂kl s,a 
(V ) = max λ≥0 
(−crλ− λ log(P̂s,a exp(−V/λ))), (46) 
where exp(−V/λ) is an element-wise exponential function. It is straight forward to show that (−crλ − λ log(P os,a exp(−V/λ))) is a concave function in λ. So, there exists an optimal solution λ∗. Similarly, let λ̂∗ 
be the optimal solution of the second problem above. 
We can now give an upperbound for λ∗, λ̂∗ as follows: Since σPkl s,a 
(V ) ≥ 0, we have 
0 ≤ −crλ∗ − λ∗ log(P os,a exp(−V/λ∗)) (a) 
≤ −crλ∗ − λ∗ log(exp(−1/(λ∗(1− γ)))) ≤ −crλ∗ + 1/(1− γ), 
from which we can conclude that λ∗ ≤ 1/(cr(1− γ)). Same argument applies for the case of λ̂∗. 
From (Nilim and El Ghaoui, 2005, Appendix C) it follows that whenever the maximizer λ∗ is 0 ( λ̂∗ is 0), we have
Kishan Panaganti, Dileep Kalathil 
σPkl s,a 
(V ) = Vmin ( σP̂kl s,a 
(V ) = Vmin) where Vmin = minj∈S V (j). We include this part in detail for completeness. 
lim λ↓0 −crλ− λ log(P os,a exp(−V/λ)) = lim 
λ↓0 −crλ− λ log(exp(−Vmin/λ) 
∑ s′ 
P os,a(s′) exp((Vmin − V (s′))/λ)) 
= lim λ↓0 
Vmin − crλ− λ log( ∑ s′ 
P os,a(s′) exp((Vmin − V (s′))/λ)) 
= lim λ↓0 
Vmin − crλ− λ log( ∑ 
s′:V (s′)=Vmin 
P os,a(s′) + ∑ 
s′:V (s′)>Vmin 
P os,a(s′) exp((Vmin − V (s′))/λ)) 
(a) = lim 
λ↓0 Vmin − crλ− λ log( 
∑ s′:V (s′)=Vmin 
P os,a(s′) +O(exp(−t/λ))) 
(b) = lim 
λ↓0 Vmin − crλ− λ log( 
∑ s′:V (s′)=Vmin 
P os,a(s′))− λ log(1 +O(exp(−t/λ))) 
(c) = lim 
λ↓0 Vmin − λ(cr + log( 
∑ s′:V (s′)=Vmin 
P os,a(s′)))−O(λ exp(−t/λ)) = Vmin, 
where (a) follows by taking t = mins′:V (s′)>Vmin V (s′)− Vmin > 0, and (b) and (c) follows from the Taylor series 
expansion. Thus when λ∗ is 0, we have σPkl s,a 
(V ) = Vmin. A similar argument applies for σP̂kl s,a 
(V ). 
Now consider the case when λ∗ = 0. From Lemma 12, it follows that, with probability at least 1− δ/(4|S||A|), λ̂∗ = 0 for N ≥ N ′(δ/(4|S||A|), cr, P os,a), where N ′ is defined in Lemma 12. Thus, whenever λ∗ = 0, we have |σP̂s,a(V )− σPs,a(V )| = |Vmin − Vmin| = 0, with probability at least 1− δ/(4|S||A|). Thus having resolving this 
trivial case, we now focus on the case when λ∗ > 0. 
Consider the case when λ∗ > 0. Let λkl := λ∗/2 > 0 (dependent on P os,a, V, and cr but independent of N). Again from Lemma 12, if λ∗ ∈ [λkl, 1/(cr(1− γ))], then with probability at least 1 − δ/(4|S||A|) we have 
λ̂∗ ∈ [λkl, 1/(cr(1− γ))] for N ≥ N ′′(δ/(4|S||A|), cr, P os,a), where N ′′ is defined in Lemma 12. 
From these arguments, it is clear that we can restrict the optimization problem (46) to the set λ ∈ [λkl, 1/(cr(1− γ)). Using this, with the additional fact that |maxx f(x)−maxx g(x)| ≤ maxx |f(x)− g(x)|, we get 
|σP̂kl s,a 
(V )− σPkl s,a 
(V )| ≤ max λ∈[λkl, 
1 cr(1−γ) 
] |λ log( 
P̂s,a exp(−V/λ) 
P os,a exp(−V/λ) )|. (47) 
Now, ∣∣∣∣∣log( P̂s,a exp(−V/λ) 
P os,a exp(−V/λ) ) 
∣∣∣∣∣ = 
∣∣∣∣∣log(1 + (P̂s,a − P os,a) exp(−V/λ) 
P os,a exp(−V/λ) ) 
∣∣∣∣∣ ≤ |(P os,a − P̂s,a) exp(−V/λ)| |P os,a exp(−V/λ)| 
(d) 
≤ |(P os,a − P̂s,a) exp(−V/λ)| 
exp( −1 λkl(1−γ) ) 
, (48) 
where (d) follows since λ ≥ λkl and ‖V ‖ ≤ 1/(1−γ). Using (48) in (47) along with the fact that λ ≤ 1/(cr(1−γ)), we get the desired result. 
Proof of Theorem 3. The basic steps of the proof is similar to that of Theorem 1. So, we present only the important steps. 
Following the same steps as given before (25) and (29) , we get 
‖V ∗ − V̂ ∗‖+ ‖V πk − V̂ πk‖ ≤ 2γ 
(1− γ) max V ∈V 
max s,a |σP̂kl 
s,a (V )− σPkl 
s,a (V )|. (49) 
Similarly, following the steps as given before (28), we get 
‖V̂ πk − V̂ ∗‖ ≤ 2γk+1 
(1− γ)2 . (50)
Sample Complexity of Robust Reinforcement Learning with a Generative Model 
Using Lemma 13 in (49), we get 
‖V ∗ − V̂ ∗‖+ ‖V πk − V̂ πk‖ ≤ 2γ 
(1− γ) 
exp(1/(λkl(1− γ))) 
cr(1− γ) max s,a 
max V ∈V 
max λ∈[λkl, 
1 cr(1−γ) 
] |(P os,a − P̂s,a) exp(−V/λ)|. 
(51) 
We now bound the max term in (51). We reparameterize 1/λ as θ and consider the set Θ = [cr(1−γ), 1 λkl 
]. Also, 
consider the minimal η-cover NΘ(η) of Θ and fix a V ∈ V. Then, for any given θ ∈ Θ, there exits a θ′ ∈ NΘ(η) such that |θ − θ′| ≤ η. Now, for this particular θ, θ′, 
|(P os,a − P̂s,a) exp(−V θ)| = |(P̂s,a − P os,a)(exp(−V θ′) ◦ exp(−V (θ − θ′))| (c) 
≤ |(P̂s,a − P os,a) exp(−V θ′)| exp(η/(1− γ)) ≤ max s,a 
max θ′∈NΘ(η) 
|(P̂s,a − P os,a) exp(−V θ′)| exp(η/(1− γ)), 
where (c) follows because V is non-negative and ‖V ‖ ≤ 1/(1− γ). Now consider a minimal η-cover NV(η) of the set V. By definition, there exists V ′ ∈ NV(η) such that ‖V − V ′‖ ≤ η. So, we get 
|(P os,a − P̂s,a) exp(−V θ)| ≤ |(P̂s,a − P os,a) exp(−V θ′)| exp(η/(1− γ)) 
= |(P̂s,a − P os,a)(exp(−V ′θ′) ◦ exp(θ′(V ′ − V )))| exp(η/(1− γ)) 
(d) 
≤ |(P̂s,a − P os,a)(exp(−V ′θ′))| exp(η/(1− γ)) exp(η/λkl) 
≤max s,a 
max V ′∈V 
max θ′∈NΘ(η) 
|(P̂s,a − P os,a)(exp(−V ′θ′))| exp(η/(1− γ)) exp(η/λkl) 
where (d) follows because θ′ ∈ NΘ(η) ⊆ Θ. Now, taking maximum on both sides with respect to (s, a), θ, and V , we get 
max s,a 
max θ∈Θ 
max V ∈V |(P̂s,a − P os,a) exp(−V θ)| ≤ exp(η/(1− γ)) exp(η/λkl) max 
s,a max V ′∈V 
max θ′∈NΘ(η) 
|(P̂s,a − P os,a) exp(−V ′θ′)| 
(e) 
≤ exp(η/(1− γ)) exp(η/λkl) 
√ log(2|S||A||NΘ(η)||NV(η)|/δ) 
2N (f) 
≤ exp(η/(1− γ)) exp(η/λkl) 
√ |S| log(18|S||A|/(δη2(1− γ)λkl)) 
2N (52) 
with probability greater than 1− δ. Here, (e) follows from Lemma 9 with a union bound accounting for |NΘ(η)|, |NV(η)| and the fact that ‖ exp(−V ′θ′)‖ ≤ 1, and (f) follows from Lemmas 7 and 8. 
Using (49) - (52), we get, with probability greater than 1− δ, 
‖V ∗ − V πk‖ ≤ 2γk+1 
(1− γ)2 + 
2γ 
(1− γ) 
exp(1/(λkl(1− γ))) 
cr(1− γ) exp(η/(1− γ)) exp(η/λkl) 
√ |S| log(18|S||A|/(δη2(1− γ)λkl)) 
2N . 
We can now choose k, ε, η to make each of the term on the RHS of the above inequality small. In particular, choosing η = 1, ε ∈ (0, 1/(1− γ)), and k,N satisfying the conditions 
k ≥ K0 = 1 
log(1/γ) · log( 
4 
ε(1− γ)2 ) and 
N ≥ Nkl = max 
{ max s,a 
N ′(δ/(4|S||A|), cr, P os,a), max s,a 
N ′′(δ/(4|S||A|), cr, P os,a), 
8γ2|S| c2r(1− γ)4ε2 
exp( 4 + 2λkl 
λkl(1− γ) ) log( 
18|S||A| δλkl(1− γ) 
) 
} , 
we get ‖V ∗ − V πk‖ ≤ ε with probability greater than 1− δ.
Kishan Panaganti, Dileep Kalathil 
B.5 Proof of Theorem 4 
Proof. We consider the deterministic MDP (S,A, r, P o, γ) shown in Fig.3 to be the nominal model. We fix γ ∈ (0.01, 1] and s1 = 0. The state space is S = {0, 1} and action space is A = {al, ar}, where al denotes ‘move left’ and ar denotes ‘move right’ action. Reward for state 1 and action ar pair is r(1, ar) = 1, for state 0 and action ar pair is r(0, ar) = −100γ/99, and the reward is 0 for all other (s, a). Transition function P o is deterministic, as indicated by the arrows. 
10 
$%, −100*/99 
$(, 0 $%, 1$(, 0 
Figure 3: Transitions and rewards corresponding to the nominal model P o. The states {0, 1} are given inside the circles, and the actions {al, ar} and associated rewards are given on the corresponding transitions. 
10 
$%, −100*/99 
$(, 0 
$%, 1 
$(, 0 
Figure 4: Transitions and rewards corresponding to the model P ′. 
Similarly, we consider another deterministic model P ′, as shown in Fig.4. We consider the set P = {P o, P ′}. 
It is straight forward to show that taking action ar in any state is the optimal non-robust policy πo corresponding to the nominal model P o. This is obvious if for state s = 1. For s = 0, notice that taking action al will give a value zero and taking action ar will give a value γ 
1−γ − 100γ 99 . Since γ > 0.01, taking action ar will give a positive 
value and hence is optimal. So, we get 
Vπo,P o(0) = γ 
1− γ − 100γ 
99 . 
We can now compute Vπo,P ′(0) using the recursive equation 
Vπo,P ′(0) = −100γ 
99 + γ + γ2Vπo,P ′(0). 
Solving this, we get Vπo,P ′(0) = −γ/(99(1− γ2)). 
Now the robust value of πo is given by 
V π o 
(0) = min{Vπo,P o(0), Vπo,P ′(0)} = −γ/(99(1− γ2)). 
We will now compute the optimal non-robust value from state 0 of model P ′. 
max π 
Vπ,P ′(0) = max{V(π(0)=ar,π(1)=ar),P ′(0), V(π(0)=al,π(1)=al),P ′(0), 
V(π(0)=ar,π(1)=al),P ′(0), V(π(0)=al,π(1)=ar),P ′(0)} 
= max{ − γ 
99(1− γ2) , 0, − 100γ 
99(1 + γ2) , 0} = 0. 
Now, we find the optimal robust value V ∗(0). From the perfect duality result of robust MDP (Nilim and El Ghaoui, 2005, Theorem 1), we have 
V ∗(0) = min{max π 
Vπ,P o(0),max π 
Vπ,P ′(0)} = min{Vπo,P o(0),max π 
Vπ,P ′(0)} = 0. 
We finally have 
V ∗(0)− V π o 
(0) = γ 
99(1− γ2) ≥ γ 
198(1− γ) , 
where the inequality follows since 1 + γ ≤ 2. Thus, setting c = γ/198 and γo = 0.01, completes the proof of this theorem.