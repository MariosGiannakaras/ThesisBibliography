> Source: https://arxiv.org/pdf/1902.05795

Robust Reinforcement Learning in POMDPs with Incomplete and Noisy Observations 
Yuhui Wang1, Hao He1, Xiaoyang Tan1* 
1Nanjing University of Aeronautics and Astronautics, China 1{y.wang, hugo, x.tan}@nuaa.edu.cn 
Abstract In real-world scenarios, the observation data for reinforcement learning with continuous control is commonly noisy and part of it may be dynamically missing over time, which violates the assumption of many current methods developed for this. We addressed the issue within the framework of partially observable Markov Decision Process (POMDP) using a model-based method, in which the transition model is estimated from the incomplete and noisy observations using a newly proposed surrogate loss function with local approximation, while the policy and value function is learned with the help of belief imputation. For the latter purpose, a generative model is constructed and is seamlessly incorporated into the belief updating procedure of POMDP, which enables robust execution even under a significant incompleteness and noise. The effectiveness of the proposed method is verified on a collection of benchmark tasks, showing that our approach outperforms several compared methods under various challenging scenarios. 
1 Introduction Significant progress has been made in reinforcement learning (RL) to solve a large number of tasks, such as Atari games (Mnih et al., 2015), board games (Silver et al., 2017b,a) and robotic control (Schulman et al., 2016). On tasks like robotic control, the agent acquires full observation through sensors from the environment to make decisions. For example, a bipedal robot perceives data through sensors such as position sensor and velocity sensor. However, in real-world scenarios, the agent could receive incomplete observation data for some reasons, namely, part of the sensor data is missing. For example, any malfunction in the sensor, too much time of preprocessing, or intrinsically, the sensors’ different sampling frequency from each other, could result in this issue (Randlv and Alstrm, 1997). Furthermore, realworld applications usually involve noise coming from sensors, non-deterministic actions and environment (Främling, 2004). Current RL systems are not robust against these incomplete and noisy data. For example, the Proximal Pol-icy Optimization (PPO) algorithm, involving policy network and value network, which requires complete observation to output actions, and the learning process could be damaged by the noise. 
In this paper we are interested in RL method under incomplete and noisy observation. Incomplete means part of ob-
servation is dynamically missing over timestep, namely the dimension and time that observation missing occurs could not be known in advance by agent. 
A passive countermeasure against the incomplete observations is to stop the executing process. However, this arrangement suffers from high cost or even is dangerous under some circumstances, e.g., for an automatic drive car driving in high speed, stopping action when data missing occurs is fatal. Another typical solution is to fill the missing components with the adjacent earlier data. However, this method is trustless especially in a rapidly changing system. A plausible method is to predict values of missing components. However, since the environments involve noise, predicting the latent state accurately is a non-trivial task. 
Our work is part-in inspired by the approaches of POMDPs (Kaelbling, Littman, and Cassandra, 1998; McAl-lister and Rasmussen, 2017). During the execution phase of the agent, we maintain a belief state, which is the posterior distribution over latent state based on the historical incomplete and noisy observations. The belief state is employed by the policy to make decision. Our contributions are threefolds. First, we model the incomplete and noisy observations problem within the framework of POMDPs, and make several approximations to conduct a tractable and efficient belief updating. Second, we propose a new surrogate loss function with local approximation, which learns the transition model of MDP from incomplete and noisy observations. Last but not least, we propose a robust RL method with a belief imputation mechanism, which enables robust execution when the input is corrupted or partially missing. Extensive experiments on several benchmark tasks show that our approach outperforms several compared methods under various challenging scenarios. 
The remainder of the paper is organized as follows. First, we give a brief outline of related work, RL and the generative model. Then we detail the new algorithm, BI-PPO, and the generative model of the incomplete and noisy observations is presented. After that, experimental results on RL benchmark tasks with incomplete and noisy observations are demonstrated. The paper concludes with conclusions and directions for future work. 
 
 
 
 
 
 
 
 
 
 
2 Related Work Concerning the methods handling missing data in RL. Ran-dlv and Alstrm (1997) first present a data complement method by setting up an exception network whose output is used to impute the missing values. Their method work in a MDP framework, and they impute missing data with the prediction based only on the imputed-state at last timestep. This differs from our approach, which works in a POMDP framework and employ the belief state to act based on the whole history observations and actions besides the current one. 
Lizotte et al. (2008) proposed a method for batch Q-learning with missing data. They model the posterior distribution of missing data Xmiss given observed data Xobs, where X is a set of trajectories. Then they sample X 
(1) miss, X 
(2) miss, . . . , X 
(N) miss from Xmiss|Xobs to construct 
multiple imputed datasets. The finally Q function is integrated with Q functions trained with these imputed data. Their method depends on proper assumption of the generative model and does not work well on high dimensional continuous control. 
For the methods working in POMDPs, the approach of maintaining a belief state is widely used. McAllister and Rasmussen (2017) studied a special case where the partial observability has the form of additive Gaussian noise on the unobserved state. The belief is used to filter the noisy observations. Igl et al. (2018) proposed the Deep Variational RL, which directly uses a network to output distribution of the belief state from the observation, and relies on a particle filter to approximate the intractable computation of the belief updating. Their method is more like a DNN-based ’black-box’ which trying to directly output the belief state from current observation. While our method sufficiently exploits the prior knowledge of the problem structure under the incomplete and noisy observation setting by explicitly imputing the missing components from the observed part. 
Many other approaches solve POMDPs by Recurrent Neural Networks (RNNs). Hausknecht and Stone (2015) proposed the Deep Recurrent Q-network (DRQN), which employ RNNs to integrate historical trajectory and is robust to partial observability on Atari games. Zhu, Li, and Poupart (2017) extended DRQN by explicitly including actions as input to the RNNs, which is called Action-specific DRQN (ADRQN). These works utilize RNNs to recurrently aggregate the history observations, while we maintain a belief state which is propagate forward by exploiting the problem structure. 
3 Preliminaries 3.1 Reinforcement Learning In RL, the decision process is modelled as a Markov Decision Process (MDP) described by the tuple M = (S,A, T , r, ρ1, γ). S, A, T : S ×A → P(S), r : S ×A→ R are the set of states, set of actions, stochastic transition function and the reward function respectively. ρ1 is the distribution of the initial state s0, and γ ∈ (0, 1) is the discount factor. Value function V π(s) = E[Rγt |st = s] and action-
value function Qπ(s, a) = E[Rγt |st = s, at = a], where Rγt = 
∑∞ k=0 γ 
krt+k+1 , are often used in RL algorithms. The main idea of RL methods is to update the parame-
ter of policy πθ towards the direction of maximizing performance objective, 
Lpolicy(θ) = 
∫ 
S×A ρπθ (s)πθ(a|s)r(s, a)dsda, 
where ρπθ (s) = (1 − γ) ∑∞ t=1 γ 
t−1ρπθt (s), ρπθt (s) is the density of s at time t. The most commonly used gradient estimator has the form 
∇θLpolicy(θ) = Es,a [∇θ log πθ(a|s)Aπθ (s, a)] , 
whereAπθ (st, at) = Qπθ (st, at)−V πθ (st) is the advantage function of policy πθ. The up to date algorithm to estimate Aπθ (st, at) is the Generalized Advantage Estimator Â(γ,λ) 
t (Schulman et al., 2016), which has the form 
Â (γ,λ) t = 
∞∑ 
k=0 
(γλ) k [ rt + γV̂φ(st+k+1)− V̂φ(st+k) 
] , 
where 0 < λ < 1 is a trade-off coefficient, and V̂φ is the estimated value function trained by 
Lvalue(φ) = Est ∥∥∥Vφ(st)− V̂t 
∥∥∥ 2 
, (1) 
where V̂t = ∑∞ k=0 γ 
krt+k is the discounted accumulated reward of from timestep t. PPO (Schulman et al., 2017) tactfully plug the idea of constraint on policy into the objective, by optimizing the ”surrogate” objective 
(2) Lpolicy(θ) = Est,at 
[ min 
( ωθ(at, st)Â 
(γ,λ) t , 
clip (ωθ(at|st), 1− δ, 1 + δ) Â (γ,λ) t 
)] , 
where ωθ(at, st) = πθ(at|st) πθold (at|st) , δ is the clipping parameter. 
3.2 Generative Model of Incomplete and Noisy Observations 
Let the state at timestep t to be st ∈ RD, which is noisily and partially observed as xt = (st + εt)  wt, where εt ∼ N (0,Σε), wt ∈ {0, 1}D is the observable indicator vector (1 for observed, 0 for missing), and the operator  is defined as (s  w)(i) , 
{ s(i) w(i) = 1 o w(i) = 0 
, where a com-
ponent possesses value o means the data is missing; thus xt ∈ (R ∪ {o})D. 
Note that the entries of wt are sampled at each timestep, which make the observation dynamically missing over time. We refer missing part the ones whose values are missing, denoted as xmt ∈ RMt , Mt is the number of components of the missing part, and available part are the ones that possess values, denoted as xat ∈ RD−Mt . Current RL systems could not deal with these incomplete observations directly, especially the case where the available part is dynamically changing over time.
The missing mechanism could be characterized by the conditional distribution P (wt|st, xt, at; ζt), where ζt denotes unknown parameter that partly determine missingness. Our method works as long as wt is independent of st. Specifically, we assume that the observation data are either Missingness Completely At Random (MCAR) or Missing-ness At Random (MAR) (Little and Rubin, 1987). MCAR means the missingness only depends on unknown parameters ζt, while MAR is less restrictive in that the missingness could also depend on other available components, i.e.,P (wt|st, xt, at; ζt) = P (wt|xat , at; ζt). Since MCAR case is a particular case of MAR, we would derive our method under the MAR case throughout the paper. 
4 Methods In this section, we present the modifications on two subroutines of RL methods, which are execution and training phase respectively. During the execution phase, we conduct belief state propagation, which is employed by the policy to decide action. While in training phase, we learn the transition model of MDP, which is required by updating of the belief state and jointly trained with policy searching. 
4.1 Belief State Propagation In the execution phase, we divert the impracticable planning in original state space into belief space. In belief space, a belief state is a posterior distribution over possible original state space based on the history trajectory data, i.e., bt(st) , P (st|x1:t, a1:t−1). The updating of belief state bt(st) has the form by using Bayes rule, 
bt(st) = P (xt|st, at; ζt)b̃t(st)∫ P (xt|s′t, at; ζt)b̃t(s′t)ds′t 
, for t = 1, 2, . . . 
(3) 
where b̃t(st) = 
∫ bt−1(st−1)T (st|st−1, at−1)dst−1 
for t = 2, 3, . . . 
(4) 
where T is the transition probability function in original state space. To clarify the updating process, we introduce b̃t(st) which is called an ”intermediate” belief state. The execution starts with a prior intermediate belief state b̃1(s1) and an initial observation x1, the belief state bt(st) is computed using (3), then the action at is decided according to this belief state and receive an incomplete observation xt+1, finally we yield the next belief state bt+1 by computing (4) and (3) alternatively, and keeps iterating until end of the episode. We detail this process in the following. 
First, we compute the intermediate belief state b̃t(st) 
using (4) (the initial intermediate belief state b̃1 is a parameterized distribution), which is intractable since the transition probability function T (st|st−1, at−1) is nonlinear. However, (4) could be approximated by replacing the nonlinear T (st|st−1, at−1) with first-order (linear) approximation of T w.r.t. st−1 at Est−1∼bt−1 
[st−1], which reduces to b̃t(st) 
. = T (st|Est−1∼bt−1 
[st−1], at−1). For 
tractability, we approximate the transition function by using Laplace Approximation, formulated as T (st|st−1, at−1) = N ( st|fµ(st−1, at−1), fΣ(st−1, at−1) 
) , where fµ and fΣ 
is approximated by DNNs, detailed in next section. Thus, for an intermediate state space b̃t(st), the mean µ̃t and variance Σ̃t are computed by 
(5) b̃t(st) 
. = N 
( st|µ̃t = fµ 
( Est−1∼bt−1 
[st−1], at−1 
) , 
Σ̃t = fΣ ( Est−1∼bt−1 
[st−1], at−1 
)) 
Here we approximate the transition distribution as a multivariate Gaussian but focus on modeling the dynamic with a highly non-linear DNN, which helps to capture the complex dynamics of the environment. Although more general density models such as mixture of Gaussians or non-parametric models could be adopted, this could increase the difficulty of belief inference. 
Then, the belief state bt is computed using (3). For the likelihood part P (xt|st, at; ζt), where xt ∈ (R ∪ {o})D is an incomplete and noisy observation in which some components possess value o. We denote Iat = {i|x(i) 
t 6= o}, Imt = {i|x(i) 
t = o} as the available and missing indexes respectively. A sub-permutation matrix, which is used for filter and leave the available part of xt, is constructed by 
Ht ∈ R(D−Mt)×D by H (j,Iot 
(j)) t = 1, j = 1, . . . , D −Mt 
while other entries are 0. For example, for a D = 3 observation xt = (1, o, 2)>, the sub-permutation matrix is 
Ht = 
( 1 0 0 0 0 1 
) . Following the generative model, we 
have 
P (xt|st, at; ζt) = P (wt|xat , at; ζt)P (xat |st) (6) 
where P (wt|xat , at; ζt) emerges due to the MAR assumption, P (xat |st) = N (Htxt|Htst,HtΣεH>t ) is marginal likelihood of the available part xat and has the form of linear Gaussian model (derived in Appendix A.1). 
In addition, we adopt Gaussian as the initial intermediate belief state b̃1(s1) , N (s1|µ̃1, Σ̃1). Thus by employing (3), b1(s1) is still Gaussian, and also does b̃2(s2), b2(s2), . . . , b̃t(st), bt(st) by employing (5) and (3) alternatively. Specifically, given an intermediate belief state b̃t(st) = N (st|µ̃t, Σ̃t), updating of belief state bt in (3) is computed by 
(7) bt(st) = N 
( st|µt = µ̃t + Ft (xt − µ̃t) , 
Σt = Σ̃t − FtΣ̃t ) , 
where Ft = Σ̃tH > t 
[ Ht(Σ̃t + Σε)H>t 
]−1 
Ht. (8) 
Note that the missing distribution P (wt|xat , at; ζt) in (6) is cancelled out in (3) since it doesn’t depend on state st. The derivation is detailed in Appendix A.2. 
In some special cases, for example, when there is no data missing occurs (but noise exists), we have Ht = I and Eq
(8) reduces to Ft = Σ̃t 
[ (Σ̃t + Σε) 
]−1 
. We could see that the larger the noise covariance Σε the smaller the term Ft, which reduces the impact of current observation xt on the expectation µt, and enlarges the uncertainty Σt (see Eq (7)). Furthermore, when the noise is also removed (and no data missing occurs), we have Σε = 0 and thus Ft = I , hence µt will collapse to xt and Σt to 0. 
Finally, the belief state bt is employed by the policy π to decide action, where we can use the exception µt of belief state for decision directly, π(bt) , π(µt), or include the uncertainty term Σt as input, 
π(bt) , π(µt,Σt), (9) 
4.2 Learning Transition Model from Incomplete and Noisy Observations 
The belief state propagation in (5) requires a transition model, and the initial intermediate belief state b̃1 also need to be learned. Some methods assume the transition model is already known (Egorov, 2015) or is approximated by a generative network, which requires a lot of data to train especially in highdimensional tasks. However, we adopt Gaussian, which is parameterized by a highly non-linear transition network, i.e., T̂ (st+1|st, at) = N 
( st+1|fµψp(st, at), f 
Σ ψp 
(st, at) ) 
. 
ψp is parameter of the DNN, fΣ ψp 
(st, at) is a state-action-dependent, positive-definite square matrix, which is parametrized by fΣ 
ψp (st, at) = Gψp(st, at)G 
> ψp 
(st, at), where Gψp(st, at) is a lower-triangular matrix whose entries come from a linear output layer of a DNN. The initial intermediate belief state is also a Gaussian distribution b̃1(s1) , N (s1|µ̃1, Σ̃1). For simplification, we denote ψ , (ψp, µ̃1, Σ̃1). The log-likelihood of observations given actions, i.e., logP (x1:T |a1:T ;ψ), is 
L(ψ) = log 
∫ b̃(s1;ψ)P (x1|s1, a1; ζ1)· 
T−1∏ 
t=1 
T̂ (st+1|st, at;ψ)P (xt+1|st+1, at+1; ζt+1)ds1:T 
(10) Note that the unknown parameter ζt (which partly determines the missing vector) doesn’t need to be learned (is not employed by belief updating) and doesn’t influence the learning of other parameters since it is independent of st (see Eq (6)). The multiple production in (10) makes the objective difficult to optimize directly. Instead, we introduce the following local approximation, 
(11) 
L̂ψ′(ψ) = log 
∫ b̃1(s1;ψ)P (x1|s1, a1; ζ1)ds1 
+ 
T−1∑ 
t=1 
[ log 
∫ bt(st;ψ 
′)T̂ (st+1|st, at;ψ)· 
P (xt+1|st+1, at+1; ζt+1)dstdst+1 
] , 
where ψ′ is a value of variable ψ. 
Due to the intractable nonlinear T̂ , Eq (11) is approximated by replacing the nonlinear g(st, xt+1, at) =∫ T̂ (st+1|st, at;ψ)P (xt+1|st+1)dst+1 with first-order (lin-
ear) approximation w.r.t. st at Est∼bt(st;ψ′)[st] = µt. Thus the final objective function has the form 
L̂model ψ′ (ψ) = logN 
( H1x1|H1µ̃1,H1 
( Σ̃1 + Σε 
) H>1 ) 
+ 
T−1∑ 
t=1 
[ logN 
( Ht+1xt+1|Ht+1f 
µ ψp 
(µt, at), 
Ht+1 
( fΣ ψp(µt, at) + Σε 
) H>t+1 
)] 
(12) 
The parameters of the noise model could be learned in principle, e.g., by imposing extra regularization terms (e.g., lowrank constraints, l2-norm) over the parameters. 
4.3 Jointly Learning with Policy Searching We extend PPO from MDPs to a special-case of POMDPs (where the observations are incomplete and noisy), which we call Belief Imputation PPO (BI-PPO). The input to the policy and value network of PPO is modified to be belief state, i.e., (µt,Σt), as Eq (9) shows. Whereas we only implement our method by extending PPO, it could also be generally extended to other DNN-based RL algorithms. We integrate the objectives by minimizing the following objective function, 
J(θ, φ, ψ) = −Lpolicy(θ) + λvL value(φ)− λpL̂model 
ψ′ (ψ) 
(13) 
where λv and λp are the coefficients. The transition network shares parameter with the policy and value networks, and these three networks are trained jointly. This architecture could assist in learning a more robust representation and promote the performance of RL, as we will evaluate in experiments. Since we adopt the normalized advantage values and rewards to train policy and value network, all the three terms have the same magnitude across different tasks (the term L̂model ψ′ (ψ) could be seen as a likelihood term). Thus we could 
use the same setting of the hyper-parameters across different tasks in principle.The BI-PPO algorithm is presented in Al-gorithm 1. 
5 Experiments 5.1 Experiments Setting We designed our experiments to investigate the following questions: 
1. Could BI-PPO be robust to the incomplete and noisy observations issue for control tasks? To what extent of missing and noise could it be robust? 
2. Could BI-PPO contribute to learning regarding episode rewards and data efficiency? 
To answer 1, we evaluate BI-PPO under different missing and noise settings on benchmark continuous control tasks. Specially, each component of observation has a probability
Algorithm 1 BI-PPO 
1: for i = 1 to TIMESTEPS MAX/T do 2: // Execution Phase 3: Receive observation x1 from environment 4: Start with b̃1 = N (µ̃1, Σ̃1) 5: for t = 1 to T do 6: Update the belief state bt = N (µt,Σt) by (7) 7: Perform at according to π(bt) by (9) 8: Receive reward rt and incomplete observation 
xt+1 
9: Update the intermediate belief state b̃t+1 by (5) 10: end for 11: // Training Phase 12: for k = 1 to Epoches Max do 13: Compute advantage Â(λ,γ) 
t , for t = 1, . . . , T 14: for t = 1 to T do 15: Update belief state bt = N (µt,Σt) by (7) with 
b̃t and xt 16: Train networks with the tuple 
(µt,Σt, at, A (λ,γ) t , xt+1) by (13) 
17: Update the intermediate belief state b̃t+1 by (5) 18: end for 19: end for 20: end for 
of rate to be missing and is contaminated with additive Gaus-sian noise. Concerning 2, we compare BI-PPO with several prior policy optimization algorithms, regarding episode rewards and the required timestep to hit a threshold. The following two sections discuss these two questions respectively. Simulated Tasks. We evaluated our methods on 8 benchmarks simulated locomotion tasks, which is implemented in OpenAI Gym v0.9.3. (Brockman et al., 2016) using the Mu-JoCo (Todorov, Erez, and Tassa, 2012) physics engine. The 8 benchmark tasks are HalfCheetah, Hopper, Walker2d, Ant, Swimmer, Reacher, InvertedDoublePendulum, InvertedPen-dulum respectively. Implementation Details. We implemented our algorithms based on the implementations of PPO (Dhariwal et al., 2017). Similarly in Schulman et al. (2017), we used discount factor γ = 0.99, GAE parameter λ = 0.95, PPO clipping parameter is setting to be 0.2, and Adam is used to for learning the weights of deep networks with a base learning rate of lr = 3 × 10−4, Adam epsilon εadam = 1 × 10−5. Em-pirically, we set the penalty coefficient λv = 1.0, λp = 1.0. All three DNNs has two hidden layers of 64 units each and shares the first layer. 
5.2 Evaluation with Incomplete and Noisy Observations 
To investigate robustness against incomplete and noisy observations, we investigate methods under different missing ratio and noise level. For missing mechanism, we design for the MAR case, the probability function of i-th observable 
indicator (i = 1, . . . , D) is 
P (w (i) t = 1|xat , at; ζt) , P (w 
(i) t = 1|xat , at, ζ)P (w 
(i) t = 1|ζ) 
The two terms in RHS represent the missing conditioned on observed and unknown variables, jointly impact w(i) 
t . Only both two distributions output 1 could component i be observable. They have forms 
P (w (i) t =1|xat , at, ζ) , 1−min 
( g(xat 
>β1,i + a>t β2,i + β3,i), ζ ) 
P (w (i) t = 1|ζ) , 1− ζ, 
where g is the sigmoid function, β1,i, β2,i, β3,i are random variable sampled from Gaussian distribution, 0 < ζ < 1 is the parameter of Bernoulli distribution. We use min operation to manually control the missing level in our experiments. To explicitly compare the result under different missing level, we refer η = maxxat ,at P (w 
(i) t = 0|xat , at; ζt) 
to the missing ratio, and we set η = 0, 0.1, 0.2, 0.3 for different settings by tuning ζ. The noise levels are controlled by a noise factor σ = 0.1, 1, such that the noises are√ 
Σε = σ×0.01×I . We run each trial for 2×106 timesteps (except for RNN-based comparison methods, which require more timesteps and is trained with 2 × 107 timesteps) and save the trained model every 2048 timesteps, then the model which achieves the best performance during the training process is employed to execute for 10 episodes. We measure the episode rewards, imputed state precision and execution time of each method. 
We compare our method against the following algorithms. 1) The naive Fill Adjacent (FA) method is baseline, where the missing value is imputed with adjacent earlier value. 2) Bayesian Multiple Imputation (BMI) method (Lizotte et al., 2008), which imputes missing values with posterior of observed data to build policies. 3) Exception Imputation (EI) (Randlv and Alstrm, 1997), which complement the missing values with a predictive state directly. 4) Deep Recurrent Q-network (DRQN) (Hausknecht and Stone, 2015), which add recurrent LSTM architecture to the networks. 5) Action-specific DRQN (ADRQN) (Zhu, Li, and Poupart, 2017), which extra including the action as input of RNNs. We implement these methods using PPO, thus are called FA-PPO, BMI-PPO, EI-PPO, DR-PPO, ADR-PPO respectively. Episode Rewards: Fig. 1 shows episode rewards results under different missing ratio and noise level on benchmark tasks. At low noise without missing, all methods work relatively well. However, as missing ratio increase, FA-PPO works poorly, while BMI-PPO works slightly better than FA-PPO but a lot worse than BI-PPO. DR-PPO, ADR-PPO performs better than EI-PPO, but much worse than BI-PPO. This is partly due to the reason that the hidden representation yielded by a RNN network is not stable when the input contains corrupted or missing values. BI-PPO outperform EI-PPO by a large margin, especially on HalfCheetah, Ant, Swimmer, Walker2d. All methods don’t work well on In-vertedDoublePendulum with high missing ratio. We speculate that the state in this task is compact and all components have critical information for decision. Nevertheless,
overall BI-PPO shows robustness against significant incompleteness and noise, and work pretty well especially on high dimensional tasks like HalfCheetah, Hopper, and Ant. 
Imputed State Precision: The imputed state precision could partly reflect why the algorithms perform in the level. We measure MSE between the imputed state and the latent 
system state, which could be obtained in the simulator. The imputed state precision results are almost consistent with rewards results in Fig. 1, and are provided in Appendix B. 
Execution Time Complexity: We report model run time for EI-PPO, DR-PPO, ADR-PPO and BI-PPO. The former three ones run for average 2.7s in an episode over all tasks, 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
10 
20 
30 
40 
reward(×102) HalfCheetah 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
15 
20 
25 
30 
35 
40 reward(×102) Hopper 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 5 
10 
15 
20 
25 
30 
reward(×102) Ant 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
20 
40 
60 
80 
100 
reward(×102)InvertedDoublePendulum 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
2 
4 
6 
8 
10 
reward(×102) InvertedPendulum 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
20 
40 
60 
80 
100 
120 reward Swimmer 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) −16 
−14 
−12 
−10 
−8 
−6 
−4 
−2 
re−ard Reacher 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 5 
10 
15 
20 
25 
30 
35 
40 
45 reward(×102) Walker2d 
FA-PPO 
BMI-PPO 
EI-PPO 
DR-PPO 
ADR-PPO 
BI-PPO 
Figure 1: Episode rewards under different missing ratio η and noise factor σ settings on benchmark tasks. The error bars show ±1 standard deviation of the mean reward given 10 episodes of the trained model. The horizontal axis shows different combination of missing ratio η and noise level σ, while the vertical axis shows the rewards. The rewards of different methods are shown for each setting.
Table 1: Results of maximum attained episode rewards and timesteps to hit a threshold within 2 million timesteps, averaged over 3 random seeds. (a) shows the maximum attained episode reward. (b) shows the timesteps to hit a prescribed threshold. The thresholds for all environment were chosen according to Wu et al. (2017) except Ant and HalfCheetah since we evaluate algorithms within 1/15 of their limiting timesteps. 
(a) Maximum Rewards (b) Timesteps (×103) to hit threshold BI-PPO EI-PPO PPO ACKTR Threshold BI-PPO EI-PPO PPO ACKTR 
HalfCheetah 4156 3735 1549 3233 2100 235 425 ∞1 850 Hopper 3828 3595 3622 3309 2000 184 231 209 502 
Ant 2988 1628 2448 3566 2500 1220 ∞ ∞ 825 Inverted 
DoublePendulum 9345 9342 9333 9342 9100 104 137 155 348 
InvertedPendulum 1000 1000 1000 1000 950 18 22 18 110 Swimmer 115 105 118 47 90 493 1073 550 ∞ Reacher -5 -4 -1 -3 -7 176 268 137 250 
Walker2d 4352 4034 4285 2398 3000 489 456 252 ∞ 
with constant time complexity w.r.t. the number of timetsteps T . While BI-PPO runs for average 5.1s and scales with O ( T (D(1− η))3 
) time complexity. 
5.3 Evaluation with Complete and Clean Observations 
In this section, we investigate whether BI-PPO could assist in learning better policy, regarding rewards and sample efficiency. Thus we evaluate them with complete and clean observations. We compared BI-PPO and EI-PPO against the following methods: the original PPO (Schulman et al., 2017), Actor Critic using Kronecker-Factored Trust Region (ACKTR) (Wu et al., 2017). Both of BI-PPO and EI-PPO set up an additional transition network, but approximate the transition model in a different way. We use OpenAI Base-lines (Dhariwal et al., 2017) implementations of these algorithms. Each algorithm runs for 2 million timesteps, and is averaged over the 3 random seeds. Maximum Episode Rewards: Table 1 (a) shows maximum episode rewards within 2 million timesteps. Table 1 (a) shows that both BI-PPO and EI-PPO significantly outperform the original PPO. Especially on HalfCheetah and Ant, BI-PPO achieves 268% and 120% of the original PPO maximum reward. This shows that our approach of jointly learning the required model for computing the belief state with the policy is beneficial to improve the overall generalization capability of the system. On HalfCheetah, Hopper, InvertedDoublePendulum, and Walker2d, BI-PPO performs better than ACKTR. BI-PPO outperform EI-PPO on almost all tasks except Reacher, which shows that the probabilistic approximation to transition function is necessary. Sample Efficiency: Table 1 (b) shows the timesteps required by algorithms to hit a prescribed threshold within 2 million timesteps. The thresholds for all environments were chosen according to Wu et al. (2017) except Ant and HalfCheetah since we evaluate algorithms within 1/15 of their timesteps. Table 1 (b) shows that BI-PPO significantly 
1∞ means that the method did not reach the reward threshold within 2 million timesteps. 
outperform ACKTR on HalfCheetah, Hopper, InvertedDou-blePendulum, Reacher. We could also observe that BI-PPO requires fewer timesteps than EI-PPO and the original PPO on almost all tasks except Swimmer and Reacher. 
6 Conclusions In this paper, we propose a new algorithm, BI-PPO, addressing the incomplete and noisy observations problem for continuous control using a model-based method, in which the transition model is estimated from the incomplete and noisy observations using a newly proposed surrogate loss function with local approximation. To implement belief imputation for execution and training, we construct a generative model and seamlessly incorporate it into the belief updating procedure of POMDP. Furthermore, we propose a robust RL method with belief imputation, which enables robust execution even under a significant incompleteness and noise. Ex-periments verify the effectiveness of the proposed method, showing that our approach outperforms several compared methods under various challenging scenarios. Besides, BI-PPO could also improve the original PPO by a large margin regarding rewards and data efficiency, and is competitive with the state-of-the-art policy gradient methods. 
As part of our future work, we plan to handle a slightly different but more difficult case where some sensors suddenly produce totally different values. An approach to handle this case, based on this work, is to treat such values as outliers, and weight down their influence on the belief imputation or just throw them away. 
References Brockman, G.; Cheung, V.; Pettersson, L.; Schneider, J.; 
Schulman, J.; Tang, J.; and Zaremba, W. 2016. Openai gym. 
Dhariwal, P.; Hesse, C.; Klimov, O.; Nichol, A.; Plappert, M.; Radford, A.; Schulman, J.; Sidor, S.; and Wu, Y. 2017. Openai baselines. https://github.com/ openai/baselines.
Egorov, M. 2015. Deep reinforcement learning with pomdps. 
Främling, K. 2004. Reinforcement learning in a noisy environment: light-seeking robot. WSEAS Transactions on Systems 3(2):714–719. 
Hausknecht, M. J., and Stone, P. 2015. Deep recurrent q-learning for partially observable mdps. arXiv preprint arXiv:1507.06527. 
Igl, M.; Zintgraf, L. M.; Le, T. A.; Wood, F.; and White-son, S. 2018. Deep variational reinforcement learning for pomdps. international conference on machine learning 2122–2131. 
Kaelbling, L. P.; Littman, M. L.; and Cassandra, A. R. 1998. Planning and acting in partially observable stochastic domains. Artificial Intelligence 101(1):99–134. 
Little, R. J. A., and Rubin, D. B. 1987. Statistical analysis with missing data. 
Lizotte, D. J.; Gunter, L.; Laber, E. B.; and Murphy, S. A. 2008. Missing Data and Uncertainty in Batch Reinforce-ment Learning. NIPS-08 Workshop on Model Uncertainty and Risk in Reinforcement Learning 1–8. 
McAllister, R., and Rasmussen, C. E. 2017. Data-efficient reinforcement learning in continuous state-action gaussian-pomdps. In NIPS 2017, 2040–2049. 
Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A. A.; Ve-ness, J.; Bellemare, M. G.; Graves, A.; Riedmiller, M.; Fidjeland, A. K.; Ostrovski, G.; et al. 2015. Human-level control through deep reinforcement learning. Nature 518(7540):529. 
Randlv, J., and Alstrm, P. 1997. Reinforcement learning based on incomplete state data. 
Schulman, J.; Moritz, P.; Levine, S.; Jordan, M. I.; and Abbeel, P. 2016. High-dimensional continuous control using generalized advantage estimation. international conference on learning representations. 
Schulman, J.; Wolski, F.; Dhariwal, P.; Radford, A.; and Klimov, O. 2017. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347. 
Silver, D.; Hubert, T.; Schrittwieser, J.; Antonoglou, I.; Lai, M.; Guez, A.; Lanctot, M.; Sifre, L.; Kumaran, D.; Grae-pel, T.; et al. 2017a. Mastering chess and shogi by self-play with a general reinforcement learning algorithm. arXiv preprint arXiv:1712.01815. 
Silver, D.; Schrittwieser, J.; Simonyan, K.; Antonoglou, I.; Huang, A.; Guez, A.; Hubert, T.; Baker, L.; Lai, M.; Bolton, A.; et al. 2017b. Mastering the game of go without human knowledge. Nature 550(7676):354. 
Todorov, E.; Erez, T.; and Tassa, Y. 2012. Mujoco: A physics engine for model-based control. In Ieee/rsj Inter-national Conference on Intelligent Robots and Systems, 5026–5033. 
Wu, Y.; Mansimov, E.; Grosse, R. B.; Liao, S.; and Ba, J. 2017. Scalable trust-region method for deep reinforcement learning using kronecker-factored approximation. neural information processing systems 5279–5288. 
Zhu, P.; Li, X.; and Poupart, P. 2017. On improving deep reinforcement learning for pomdps. arXiv preprint arXiv:1804.06309.
A Execution phase 
A.1 Observation Likelihood 
We give the derivation of observation likelihood P (xt|st, at; ζt) here. First we would repeat the probability model of observation. The state of the system st is noisily and partially observed as xt = (st + εt)  wt, where εt ∼ N (0,Σε), wt ∈ {0, 1}D is the observable indicator vector, xt ∈ (R ∪ {o})D, in which o means the data is missing. We make the MAR assumption that P (wt|st, xt, at; ζt) = P (wt|xat , at; ζt). Denote xmt ∈ RMt as the missing part whose values are missing, where Mt is the number of the missing part, and xat ∈ RD−Mt as the available part that possess values. Besides, Iat = {i|x(i) 
t 6= o}, Imt = {i|x(i) t = o} are the available and missing indexes 
respectively, Ht ∈ R(D−Mt)×D is the sub-permutation matrix. The observation likelihood is 
P (xt|st, at; ζt) = P (xat , wt|st, at; ζt) (1) = P (wt|st, xat , at; ζt)P (xat |st) = P (wt|xat , at; ζt)P (xat |st) (2) 
(1): We could construct missing vector wt by w(i) t = 1{x(i) 
t 6= o}. 
A.2 Updating Belief State during Execution 
Following the approximations in the paper for computing intermediate belief state b̃t(st) =∫ bt−1(st−1)T (st|st−1, at−1)dst−1, we have 
b̃t(st) . = N 
( st|µ̃t = fµ 
( Est−1∼bt−1 
[st−1], at−1 
) , Σ̃t = fΣ 
( Est−1∼bt−1 
[st−1], at−1 
)) . (3) 
The belief state is updated by 
bt(st) = P (xt|st, at; ζt)b̃t(st)∫ P (xt|s′t, at; ζt)b̃t(s′t)ds′t 
(4) 
Following the probability model of incomplete and noisy observation in the paper, we have P (xt|st) = P (wt|xat , ηt)P (xat |st), where P (xat |st) = N (Htxt|Htst,HtΣεH>t ) is the likelihood of the available part xat , η(i) is the missing ratio of component i, Imt and Iat are indexes of missing part and available part respectively, Wt ∈ R(D−Mi)×D is the permutation matrix, D and Mi are dimension and number of available part respectively. Thus (4) could be written as 
bt(st) = P (wt|xat , at; ζt)P (xat |st)b̃t(st)∫ P (wt|xat , at; ζt)P (xat |s′t)b̃t(s′t)ds′t 
= P (xat |st)b̃t(st)∫ P (xat |s′t)b̃t(s′t)ds′t 
(5) 
Since P (xat |st) = N (Htxt|Htst,HtΣεH>t ), and given an intermediate belief state b̃t(st) = 
N (st|µ̃t, Σ̃t) which is also Gaussian distribution, thus updating of belief state bt in (5) could be derived from the conditional distribution of linear Gaussian model, 
bt(st) = N ( st|µt = µ̃t + Ft (xt − µ̃t) ,Σt = Σ̃t − FtΣ̃t 
) , (6) 
where Ft = Σ̃tH > t 
[ Ht(Σ̃t + Σε)H>t 
]−1 
Ht. 
B Experiment: Imputed State Precision 
The imputed state precision could partly reflect why the algorithms perform in the level since the more accurate imputation would provide more information for the agent to output correct action. We measure the mean squared error of the imputed state between the latent system state, which could be obtained in the simulator. Fig. 1 shows the results. BI-PPO has a lower error than EI-PPO methods on most of the tasks, and the imputed state is robust against significant incompleteness and noise observations. The results in Fig. 1 are almost consistent with rewards results showed in the main content. 
1
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
5 
10 
15 
20 
25error(×10 01) HalfCheetah 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
5 
10 
15 
20 
error(×1002) Ho))er 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
5 
10 
15 
20 
25 
30 
35 
40 error(×1002) Ant 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) -20 
0 
20 
40 
60 
80 
100 
120 error(×1002) In−ertedD(ublePendulum 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) -10 
0 
10 
20 
30 
40 
50 error(×10−2) In−ertedPendulum 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) -5 
1 
7 
13 
20error(×10 −2) Swimmer 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
5 
10 
15 
20 
25 
err(r(×1002) Reacher 
(0,0.1) (0,1) (0.1,0.1)(0.1,1)(0.2,0.1)(0.2,1)(0.3,0.1)(0.3,1)(η, σ) 
0 
10 
20 
30 
40 
50 
60err(r(×10 02) Walker2d 
FA-PPO 
BMI-PPO 
EI-PPO 
DR-PPO 
ADR-PPO 
BI-PPO 
Figure 1: The MSE between imputed state and latent state under different missing ratio η and noise factor σ settings on benchmark tasks. The error bars show ±1 standard deviation of the mean squared error given 10 episodes of the trained model. The horizontal axis shows different combination of missing ratio η and noise level σ, while the vertical axis shows squared error of (filtered) imputed observation between latent state. The squared error of different methods are shown for each setting. 
2