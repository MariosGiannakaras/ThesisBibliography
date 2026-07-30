> Source: https://arxiv.org/pdf/1901.10031

Lyapunov-based Safe Policy Optimization for Continuous Control 
Yinlam Chow 1 Ofir Nachum 2 Aleksandra Faust 2 Edgar Duenez-Guzman 1 Mohammad Ghavamzadeh 3 
Abstract We study continuous action reinforcement learning problems in which it is crucial that the agent interacts with the environment only through safe policies, i.e., policies that do not take the agent to undesirable situations. We formulate these problems as constrained Markov decision processes (CMDPs) and present safe policy optimization algorithms that are based on a Lyapunov approach to solve them. Our algorithms can use any standard policy gradient (PG) method, such as deep deterministic policy gradient (DDPG) or proximal policy optimization (PPO), to train a neural network policy, while guaranteeing near-constraint satisfaction for every policy update by projecting either the policy parameter or the action onto the set of feasible solutions induced by the state-dependent linearized Lyapunov constraints. Compared to the existing constrained PG algorithms, ours are more data efficient as they are able to utilize both on-policy and off-policy data. Moreover, our action-projection algorithm often leads to less conservative policy updates and allows for natural integration into an end-to-end PG training pipeline. We evaluate our algorithms and compare them with the state-of-the-art baselines on several simulated (MuJoCo) tasks, as well as a real-world indoor robot navigation problem, demonstrating their effectiveness in terms of balancing performance and constraint satisfaction. Videos of the experiments can be found in the following link: https://drive.google.com/file/d/ 1pzuzFqWIE710bE2U6DmS59AfRzqK2Kek/ view?usp=sharing 
1. Introduction The field of reinforcement learning (RL) has witnessed tremendous success in many high-dimensional control problems, including video games (Mnih et al., 2015), board games (Silver et al., 2016), robot locomotion (Lillicrap et al., 
*Equal contribution 1DeepMind 2Google Brain 3Facebook AI Research. Correspondence to: Yinlam Chow <yinlam-chow@google.com>. 
Technical Report, Submitted to ICML 2019. Copyright 2019 by the author(s). 
2016), manipulation (Levine et al., 2016; Kalashnikov et al., 2018), navigation (Faust et al., 2018), and obstacle avoidance (Chiang et al., 2019). In standard RL, the ultimate goal is to optimize the expected sum of rewards/costs, and the agent is free to explore any behavior as long as it leads to performance improvement. Although this freedom might be acceptable in many problems, including those involving simulated environments, and could expedite learning a good policy, it might be harmful in many other problems and could cause damage to the agent (robot) or to the environment (plant or the people working nearby). In such domains, it is absolutely crucial that while the agent (RL algorithm) optimizes its long-term performance, it also maintains safe policies both during training and at convergence. 
A natural way to incorporate safety is via constraints. A standard model for RL with constraints is constrained Markov decision process (CMDP) (Altman, 1999), where in addition to its standard objective, the agent must satisfy constraints on expectations of auxiliary costs. Although optimal policies for finite CMDPs with known models can be obtained by linear programming (Altman, 1999), there are not many results for solving CMDPs when the model is unknown or the state and/or action spaces are large or infinite. A common approach to solve CMDPs is to use the Lagrangian method (Altman, 1998; Geibel & Wysotzki, 2005) that augments the original objective function with a penalty on constraint violation and computes the saddlepoint of the constrained policy optimization via primal-dual methods (Chow et al., 2017). Although safety is ensured when the policy converges asymptotically, a major drawback of this approach is that it makes no guarantee with regards to the safety of the policies generated during training. 
A few algorithms have been recently proposed to solve CMDPs at scale, while remaining safety during training. One such algorithm is constrained policy optimization (CPO) (Achiam et al., 2017). CPO extends the trust-region policy optimization (TRPO) algorithm (Schulman et al., 2015a) to handle the constraints in a principled way and has shown promising empirical results in terms scalability, performance, and constraint satisfaction, both during training and after convergence. Another class of algorithms of this sort is by Chow et al. (2018). These algorithms use the notion of Lyapunov functions that have a long history in control theory to analyze the stability of dynamical systems (Khalil, 1996). Lyapunov functions have been used in RL to guarantee closed-loop stability of the agent (Perkins & 
 
 
 
 
 
 
 
 
 
 
Lyapunov-based Safe Policy Optimization for Continuous Control 
Barto, 2002; Faust et al., 2014). They also have been used to guarantee that a model-based RL agent can be brought back to a “region of attraction” during exploration (Berkenkamp et al., 2017). Chow et al. (2018) use the theoretical properties of the Lyapunov functions and propose safe approximate policy and value iteration algorithms. They prove theories for their algorithms, when the CMDP is finite and known, and empirically evaluate them when it is large and/or unknown. However, since their algorithms are value-function-based, applying them to continuous action problems is not straightforward, and was left as a future work. 
In this paper, we build on the problem formulation and theoretical findings of the Lyapunov-based approach to solve CMDPs, and extend it to tackle continuous action problems that play an important role in control theory and robotics. We propose Lyapunov-based safe RL algorithms that can handle problems with large or infinite action spaces, and return safe policies both during training and at convergence. To do so, there are two major difficulties which we resolve: 1) the policy update becomes an optimization problem over the large or continuous action space (similar to standard MDPs with large actions), and 2) the policy update is a constrained optimization problem in which the (Lyapunov) constraints involve integration over the action space, and thus, it is often impossible to have them in closed-form. Since the number of Lyapunov constraints is equal to the number of states, the situation is even more challenging when the problem has a large or an infinite state space. To address the first difficulty, we switch from value-function-based to policy gradient (PG) and actor-critic algorithms. To address the second difficulty, we propose two approaches to solve our constrained policy optimization problem (a problem with infinite constraints, each involving an integral over the continuous action space) that can work with any standard on-policy (e.g., proximal policy optimization (PPO) Schulman et al. 2017) and off-policy (e.g., deep deterministic policy gradient (DDPG) Lillicrap et al. 2015) PG algorithm. Our first approach, which we call policy parameter projection or θ-projection, is a constrained optimization method that combines PG with a projection of the policy parameters onto the set of feasible solutions induced by the Lyapunov constraints. Our second approach, which we call action projection or a-projection, uses the concept of a safety layer introduced by Dalal et al. (2018) to handle simple single-step constraints, extends this concept to general trajectory-based constraints, solves the constrained policy optimization problem in closed-form using Lyapunov functions, and integrates this closed-form into the policy network via safety-layer augmentation. Since both approaches guarantee safety at every policy update, they manage to maintain safety throughout training (ignoring errors resulting from function approximation), ensuring that all intermediate policies are safe to be deployed. To prevent constraint violations due to function approximation and modeling errors, similar to CPO, we offer a safeguard policy update rule that decreases constraint cost and ensures 
near-constraint satisfaction. 
Our proposed algorithms have two main advantages over CPO. First, since CPO is closely connected to TRPO, it can only be trivially combined with PG algorithms that are regularized with relative entropy, such as PPO. This restricts CPO to on-policy PG algorithms. On the contrary, our algorithms can work with any on-policy (e.g., PPO) and off-policy (e.g., DDPG) PG algorithm. Having an off-policy implementation is beneficial, since off-policy algorithms are potentially more data-efficient, as they can use the data from the replay buffer. Second, while CPO is not a backpropagatable algorithm, due to the backtracking line-search procedure and the conjugate gradient iterations for computing natural gradient in TRPO, our algorithms can be trained end-to-end, which is crucial for scalable and efficient implementation (Hafner et al., 2017). In fact, we show in Section 3.1 that CPO (minus the line search) can be viewed as a special case of the on-policy version (PPO version) of our θ-projection algorithm, corresponding to a specific approximation of the constraints. 
We evaluate our algorithms and compare them with CPO and the Lagrangian method on several continuous control (MuJoCo) tasks and a real-world robot navigation problem, in which the robot must satisfy certain constraints, while minimizing its expected cumulative cost. Results show that our algorithms outperform the baselines in terms of balancing the performance and constraint satisfaction (during training), and generalize better to new and more complex environments, including transfer to a real Fetch robot. 
2. Preliminaries We consider the RL problem in which the agent’s interaction with the environment is modeled as a Markov decision process (MDP). A MDP is a tuple (X ,A, γ, c, P, x0), where X and A are the state and action spaces; γ ∈ [0, 1) is a discounting factor; c(x, a) ∈ [0, Cmax] is the immediate cost function; P (·|x, a) is the transition probability distribution; and x0 ∈ X is the initial state. Although we consider deterministic initial state and cost function, our results can be easily generalized to random initial states and costs. We model the RL problems in which there are constraints on the cumulative cost using CMDPs. The CMDP model extends MDP by introducing additional costs and the associated constraints, and is defined by (X ,A, γ, c, P, x0, d, d0), where the first six components are the same as in the unconstrained MDP; d(x) ∈ [0, Dmax] is the (state-dependent) immediate constraint cost; and d0 ∈ R≥0 is an upper-bound on the expected cumulative constraint cost. 
To formalize the optimization problem associated with CMDPs, let ∆ be the set of Markovian stationary policies, i.e., ∆ = 
{ π : X × A → [0, 1], 
∑ a π(a|x) = 1 
} . At 
each state x ∈ X , we define the generic Bellman operator w.r.t. a policy π ∈ ∆ and a cost function h as Tπ,h[V ](x) =∑ 
a π(a|x)[h(x, a) +γ ∑ x′∈XP (x′|x, a)V (x′)]. Given a 
policy π ∈ ∆, we define the expected cumulative cost and
Lyapunov-based Safe Policy Optimization for Continuous Control 
the safety constraint function (expected cumulative constraint cost) as Cπ(x0) := E 
[∑∞ t=0 γ 
tc(xt, at) | π, x0 
] and Dπ(x0) := E 
[∑∞ t=0 γ 
td(xt) | π, x0 
] . The safety con-
straint is then defined asDπ(x0) ≤ d0. The goal in CMDPs is to solve the constrained optimization problem 
π∗ ∈ min π∈∆ 
{ Cπ(x0) : Dπ(x0) ≤ d0 
} . (1) 
It has been shown that if the feasibility set is non-empty, then there exists an optimal policy in the class of stationary Markovian policies ∆ (Altman, 1999, Theorem 3.1). 
2.1. Policy Gradient Algorithms Policy gradient (PG) algorithms optimize a policy by computing a sample estimate of the gradient of the expected cumulative cost induced by the policy, and then updating the policy parameter in the gradient direction. In general, stochastic policies that give a probability distribution over actions are parameterized by a κ-dimensional vector θ, so the space of policies can be written as 
{ πθ, θ ∈ Θ ⊂ Rκ 
} . 
Since in this setting a policy π is uniquely defined by its parameter θ, policy-dependent functions can be written as a function of θ or π interchangeably. 
Deep deterministic policy gradient (DDPG) (Lillicrap et al., 2015) and proximal policy optimization (PPO) (Schulman et al., 2017) are two PG algorithms that have recently gained popularity in solving continuous control problems. DDPG is an off-policy Q-learning style algorithm that jointly trains a deterministic policy πθ(x) and a Q-value approximator Q(x, a;φ). The Q-value approximator is trained to fit the true Q-value function and the deterministic policy is trained to optimize Q(x, πθ(x);φ) via chain-rule. The PPO algorithm we use is a penalty form of the trust region policy optimization (TRPO) algorithm (Schulman et al., 2015a) with an adaptive rule to tune the DKL penalty weight βk. PPO trains a policy πθ(x) by optimizing a loss function that consists of the standard policy gradient objective and a penalty on the KL-divergence between the current θ and previous θ′ policies, i.e., DKL(θ, θ′) = E[ ∑ t γ 
tDKL(πθ′(·|xt)||πθ(·|xt))|πθ′ , x0]. 
2.2. Lagrangian Method The Lagrangian method is a straightforward way to address the constraint Dπθ (x0) ≤ d0 in CMDPs. In this approach, we add the constraint costs d(x) to the task costs c(x, a) and transform the constrained optimization problem to a penalty form, i.e., minθ∈Θ maxλ≥0 E 
[∑∞ t=0 c(xt, at) + λd(xt)|πθ, x0 
] − 
λd0. We then jointly optimizes θ and λ to find a saddlepoint of the penalized objective. The optimization of θ may be performed by any PG algorithm, such as DDPG or PPO, on the augmented cost c(x, a) + λd(x), while λ is optimized by stochastic gradient descent. As described in Section 1, although the Lagrangian approach is easy to implement (see Appendix B for the details), in practice, it often violates the constraints during training. While at each step during training, the objective encourages finding a safe 
solution, the current value of λ may lead to an unsafe policy. This is why the Lagrangian method may not be suitable for solving problems in which safety is crucial during training. 
2.3. Lyapunov Functions Since in this paper, we extend the Lyapunov-based approach to CMDPs to PG algorithms, we end this section by introducing some terms and notations from Chow et al. (2018) that are important in developing our safe PG algorithms. We refer the reader to Appendix A for more details. 
We define a set of Lyapunov functions w.r.t. initial state x0 ∈ X and constraint threshold d0 as LπB (x0, d0) = {L : X → R≥0 | TπB ,d[L](x) ≤ L(x), ∀x ∈ X , L(x0) ≤ d0}, where πB is a feasible policy of (1), i.e., DπB (x0) ≤ d0. We refer to the constraints in this feasibility set as the Lyapunov constraints. For any arbitrary Lyapunov function L ∈ LπB (x0, d0), we denote by FL = 
{ π ∈ ∆ : Tπ,d[L](x) ≤ L(x), ∀x ∈ X 
} , the set 
of L-induced Markov stationary policies. The contraction property of Tπ,d, together with L(x0) ≤ d0, imply that any L-induced policy is a feasible policy of (1). However, FL(x) does not always contain an optimal solution of (1), and thus, it is necessary to design a Lyapunov function that provides this guarantee. In other words, the main goal of the Lyapunov approach is to construct a Lyapunov function L ∈ LπB (x0, d0), such that FL contains an optimal policy π∗, i.e., L(x) ≥ Tπ∗,d[L](x). Chow et al. (2018) show in their Theorem 1 that without loss of optimality, the Lyapunov function that satisfies the above criterion can be expressed as LπB ,ε(x) := E 
[∑∞ t=0 γ 
t ( d(xt) + ε(xt) 
) | πB , x 
] , in 
which ε(x) ≥ 0 is a specific immediate auxiliary constraint cost that keeps track of the maximum constraint budget available for policy improvement (from πB to π∗). They propose ways to construct such ε, as well as an auxiliary constraint cost surrogate ε̃, which is a tight upper-bound on ε and can be computed more efficiently. They use this construction to propose their safe (approximate) policy and value iteration algorithms, in which the goal is to solve the following LP problem (Chow et al., 2018, Eq. 6) at each policy improvement step: 
π+(·|x) = arg min π∈∆ 
∫ a∈A 
QVπB (x, a)π(a|x), subject to (2)∫ a∈A 
QLπB (x, a) ( π(a|x)− πB(a|x) 
) ≤ ε̃(x), ∀x ∈ X , 
where VπB (x) = TπB ,c[VπB ](x) and QVπB (x, a) = 
c(x, a) + γ ∑ x′ P (x′|x, a)VπB (x′) are the value func-
tion and state-action value function (w.r.t. the cost function c), and QLπB (x, a) = d(x) + ε̃(x) + 
γ ∑ x′ P (x′|x, a)LπB ,ε̃(x 
′) is the Lyapunov function. Note that in an iterative policy optimization method, such as those we will present in this paper, the feasible policy πB can be set to the policy at the previous iteration. 
In (2), there are as many constraints as the number of states and each constraint involves an integral over the entire action space A. When the state space is large or continuous, even
Lyapunov-based Safe Policy Optimization for Continuous Control 
if the integral in the constraint has a closed-form (e.g., when the number of actions is finite), solving LP (2) becomes numerically intractable. Since Chow et al. (2018) assume that the number of actions is finite, they focus on value-function-based RL algorithms and address the large state issue by policy distillation. However, in this paper, we are interested in problems with large action spaces. In our case, solving (2) will be even more challenging. To address this issue, in the next section, we first switch from value-function-based algorithms to PG algorithms, then propose an optimization problem with Lyapunov constraints, analogous to (2), that is suitable for the PG setting, and finally present two methods to solve our proposed optimization problem efficiently. 
3. Safe Lyapunov-based Policy Gradient We now present our approach to solve CMDPs in a way that guarantees safety both at convergence and during training. Similar to Chow et al. (2018), our Lyapunov-based safe PG algorithms solve a constrained optimization problem analogous to (2). In particular, our algorithms consist of two components, a baseline PG algorithm, such as DDPG or PPO, and an effective method to solve the general Lyapunov-based policy optimization problem (the analogous to (2)) θ+ = arg min 
θ∈Θ Cπθ (x0), subject to (3)∫ 
a∈A 
( πθ(a|x)− πB(a|x) 
) QLπB (x, a) da ≤ ε̃(x), ∀x ∈ X . 
In the next two sections, we present two approaches to solve (3) efficiently. We call these approaches 1) θ-projection, a constrained optimization method that combines PG with projecting the policy parameter θ onto the set of feasible solutions induced by the Lyapunov constraints, and 2) a-projection, in which we embed the Lyapunov constraints into the policy network via a safety layer. 
3.1. The θ-projection Approach 
In this section, we show how a safe Lyapunov-based PG algorithm can be derived using the θ-projection approach. This machinery is based on the minorizationmaximization technique in conservative PG (Kakade & Langford, 2002) and Taylor series expansion, and it can be applied to both on-policy and off-policy algorithms. Following Theorem 4.1 in Kakade & Langford (2002), we first have the following bound for the cumulative cost: −βDKL(θ, θB) ≤ Cπθ (x0) − CπθB (x0) − Ex∼µθB,x0 
,a∼πθ [ QVθB (x, a) − VθB (x) 
] ≤ βDKL(θ, θB), 
where µθB ,x0 is the γ-visiting distribution of πθB starting at 
the initial state x0, and β is the weight for the entropy-based regularization.1 Using the above result, we denote by C′πθ (x0;πθB ) =CπθB (x0) + βDKL(θ, θB)+ 
Ex∼µθB,x0 ,a∼πθ 
[ QVθB (x, a)− VθB (x) 
] 1Theorem 1 in Schulman et al. (2015a) provides a recipe for 
computing β such that the minorization-maximization inequality holds. But in practice, β is treated as a tunable hyper-parameter for entropy-based regularization. 
the surrogate cumulative cost. It has been shown in Eq. 10 of Schulman et al. (2015a) that replacing the objective function Cπθ (x0) with its surrogate C′πθ (x0;πθB ) in solving (3) will still lead to policy improvement. In order to effectively compute the improved policy parameter θ+, one further approximates the function C′πθ (x0;πθB ) with its Tay-lor series expansion (around θB). In particular, the term Ex∼µθB,x0 
,a∼πθ [ QVθB (x, a)−VθB (x) 
] is approximated up 
to its first order, and the term DKL(θ, θB) is approximated up to its second order. Altogether this allows us to replace the objective function in (3) with the following surrogate: 
〈(θ − θB),∇θEx∼µθB,x0 ,a∼πθ 
[ QVθB (x, a) 
] 〉 
+ β 
2 〈(θ − θB),∇2 
θDKL(θ, θB) |θ=θB (θ − θB)〉. 
Similarly, regarding the constraints in (3), we can use the Taylor series expansion (around θB) to approximate the LHS of the Lyapunov constraints as∫ 
a∈A 
( πθ(a|x)− πB(a|x) 
) QL(x, a) da ≈〈 
(θ − θB),∇θEa∼πθ [ QLθB (x, a) 
] |θ=θB 
〉 . 
Using the above approximations, at each iteration, our safe PG algorithm updates the policy by solving the following constrained optimization problem with semi-infinite dimensional Lyapunov constraints: 
θ+ ∈ arg min θ∈Θ 
〈 (θ − θB),∇θEx∼µθB,x0 
,a∼πθ [ QVθB (x, a) 
]〉 + β 
2 
〈 (θ − θB),∇2 
θDKL(θ, θB) |θ=θB (θ − θB) 〉 , (4) 
s.t. 〈 (θ − θB),∇θEa∼πθ 
[ QLθB (x, a) 
] |θ=θB 
〉 ≤ ε̃(x), ∀x ∈ X . 
It can be seen that if the errors resulted from the neural network parameterizations of QVθB and QLθB , and the Taylor series expansions are small, then an algorithm that updates the policy parameter by solving (4) can ensure safety during training. However, the presence of infinitedimensional Lyapunov constraints makes solving (4) numerically intractable. A solution to this is to write the Lyapunov constraints in (4) (without loss of optimality) as maxx∈X 〈(θ−θB),∇θEa∼πθ [QLθB (x, a)] |θ=θB 〉−ε̃(x) ≤ 0. Since the above max-operator is non-differentiable, this may still lead to numerical instability in gradient descent algorithms. Similar to the surrogate constraint used in TRPO (to transform the maxDKL constraint to an average DKL constraint, see Eq. 12 in Schulman et al. 2015a), a more numerically stable way is to approximate the Lyapunov constraint using the following average constraint surrogate:〈 (θ−θB), 
1 
M 
M∑ i=1 
∇θEa∼πθ [ QLθB (xi, a) 
] |θ=θB 
〉 ≤ 1 
M 
M∑ i=1 
ε̃(xi), 
(5) where M is the number of on-policy sample trajectories of πθB . In practice, when the auxiliary constraint surrogate is chosen as ε̃ = (1 − γ) 
( d0 − DπθB (x0) 
) (see Appendix 
A for the justification of this choice), the gradient term
Lyapunov-based Safe Policy Optimization for Continuous Control 
in (5) can be simplified as ∇θEa∼πθ [ QLθB (xi, a) 
] = 
∇θ ∫ a πθ(a|x)∇θ log πθ(a|x)QWθB 
(xi, a)da, where WθB (x) = TπB ,d[WθB ](x) and QWθB 
(x, a) = 
d(x) + γ ∑ x′ P (x′|x, a)WθB (x′) are the constraint 
value function and constraint state-action value function, respectively. Combining with the fact that ε̃ is state independent, the above arguments further imply that the average constraint surrogate in (5) can be approximated by the inequality DπθB (x0) + 1 
1−γ 〈(θ − θB), 1 
M 
∑M i=1∇θEa∼πθ 
[ QWθB 
(xi, a) ] |θ=θB 〉 ≤ d0, which 
is equivalent to the constraint used in CPO (see Sec. 6.1 in Achiam et al. 2017). This shows a clear connection between CPO (minus the line search) and our Lyapunov-based PG with θ-projection. Algorithm 4 in Appendix E contains the pseudo-codes of our safe Lyapunov-based PG algorithms with θ-projection. We refer to the DDPG and PPO versions of this algorithm as SDDPG and SPPO. 
3.2. The a-projection Approach 
Note that the main characteristic of the Lyapunov approach is to break down a trajectory-based constraint into a sequence of single-step state dependent constraints. However, when the state space X is infinite, the feasibility set is characterized by infinite dimensional constraints, and thus, it is actually counter-intuitive to directly enforce these Lyapunov constraints (as opposed to the original trajectory-based constraint) into the policy update optimization. To address this issue, we leverage the idea of a safety layer from Dalal et al. (2018), that was applied to simple single-step constraints, and propose a novel approach to embed the set of Lyapunov constraints into the policy network. This way, we reformulate the CMDP problem (1) as an unconstrained optimization problem and optimize its policy parameter θ (of the augmented network) using any standard unconstrained PG algorithm. At every given state, the unconstrained action is first computed and then passed through the safety layer, where a feasible action mapping is constructed by projecting the unconstrained actions onto the feasibility set w.r.t. the corresponding Lyapunov constraint. Therefore, safety during training w.r.t. the CMDP problem can be guaranteed by this constraint projection approach. 
For simplicity, we only describe how the action mapping (to the set of Lyapunov constraints) works for deterministic policies. Using identical machinery, this procedure can be extended to guarantee safety for stochastic policies. Recall from the policy improvement problem in (3) that the Lya-punov constraint is imposed at every state x ∈ X . Given a baseline feasible policy πB = πθB , for any arbitrary policy parameter θ ∈ Θ, we denote by Ξ(πB , θ) = 
{ θ′ ∈ Θ : 
QLπB (x, πθ′(x)) − QLπB (x, πB(x)) ≤ ε̃(x), ∀x ∈ X } 
, the projection of θ onto the feasibility set induced by the Lyapunov constraints. One way to construct a feasible policy πΞ(πB ,θ) from a parameter θ is to solve the following 
`2-projection problem at each state x ∈ X : 
πΞ(πB ,θ)(x) ∈ arg min a 
1 
2 ‖a− πθ(x)‖2, (6) 
s.t. QLπB (x, a)−QLπB (x, πB(x)) ≤ ε̃(x). 
We refer to this operation as the Lyapunov safety layer. In-tuitively, this projection perturbs the unconstrained action as little as possible in the Euclidean norm in order to satisfy the Lyapunov constraints. Since this projection guarantees safety (in the Lyapunov sense), if we have access to a closed form of the projection, we may insert it into the policy parameterization and simply solve an unconstrained policy optimization problem, i.e., θ+ ∈ arg minθ∈Θ CπΞ(πB,θ) 
(x0), using any standard PG algorithm. 
To simplify the projection (6), we can approximate the LHS of the Lyapunov constraint with its first-order Taylor series (w.r.t. action a = πB(x)). Thus, at any given state x ∈ X , the safety layer solves the following projection problem: 
πΞ(πB ,θ)(x) ∈ arg min a 
1 
2 ‖a− πθ,unc(x)‖2, (7) 
s.t. ( a− πB(x) 
)> gLπB (x) ≤ ε̃(x), 
where gLπB (x) := ∇aQLπB (x, a) |a=πB(x) is the actiongradient of the state-action Lyapunov function induced by the baseline action a = πB(x). 
Similar to the analysis of Section 3.1, if the auxiliary cost ε̃ is state independent, one can readily find gLπB (x) by computing the gradient of the constraint action-value function ∇aQWθB 
(x, a) |a=πB(x). Note that the objective function in (7) is positive-definite and quadratic, and the constraint approximation is linear. Therefore, the solution of this (convex) projection problem can be effectively computed by an in-graph QP-solver, such as OPT-Net (Amos & Kolter, 2017). Combined with the above projection procedure, this further implies that the CMDP problem can be effectively solved using an end-to-end PG training pipeline (such as DDPG or PPO). Furthermore, when the CMDP has a single constraint (and thus a single Lyapunov constraint), the policy πΞ(πB ,θ)(x) has the following analytical solution. Proposition 1. At any given state x ∈ X , the solution to the optimization problem (7) has the form πΞ(πB ,θ)(x) = πθ(x) + λ∗(x) · gLπB (x), where 
λ∗(x) = 
( gLπB (x)> 
( πθ(x)− πB(x) 
) − ε̃(x) 
gLπB (x)>gLπB (x) 
) + 
. 
The closed-form solution is essentially a linear projection of the unconstrained action πθ(x) to the Lyapunov-safe hyperplane characterized with slope gLπB (x) and intercept ε̃(x) = (1−γ)(d0−DπB (x0)). Extending this closed-form solution to handle multiple constraints is possible, if there is at most one constraint active at a time (see Proposition 1 in Dalal et al. 2018 for a similar extension). 
Without loss of generality, this projection step can also be extended to handle actions generated by stochastic policies
Lyapunov-based Safe Policy Optimization for Continuous Control 
0 10 20 30 40 50 100 
50 
0 
50 
100 
(a) HalfCheetah-Safe, Return (b) HalfCheetah-Safe, Constraint 
0 10 20 30 40 50 0 
2 
4 
6 
8 
10 
12 
14 
(c) Point-Gather, Return (d) Point-Gather, Constraint 
0 5 10 15 20 25 30 6 
4 
2 
0 
2 
4 
6 
8 
10 
12 
(e) Ant-Gather, Return (f) Ant-Gather, Constraint 
0 10 20 30 40 50 0 
200 
400 
600 
800 
1000 
1200 
1400 
(g) Point-Circle, Return (h) Point-Circle, Constraint 
Figure 1. DDPG (red), DDPG-Lagrangian (cyan), SDDPG (blue), DDPG a-projection (green) on HalfCheetah-Safe and Point-Gather. Ours (SDDPG, SDDPG a-projection) perform stable and safe learning, although the dynamics and cost functions are not known, control actions are continuous, and deep function approximations are necessary. Unit of x-axis is in thousands of episodes. Shaded areas represent the 1-SD confidence intervals (over 10 random seeds). The dashed purple line represents the constraint limit. 
with bounded first and second order moments (Yu et al., 2009). For example when the policy is parameterized with a Gaussian distribution, then one needs to project both the mean and standard-deviation vector onto the Lyapunov-safe hyperplane, in order to obtain a feasible action probability. Algorithm 5 in Appendix E contains the pseudo-code of our safe Lyapunov-based PG algorithms with a-projection. We refer to the DDPG and PPO versions of this algorithm as SDDPG-modular and SPPO-modular, respectively. 
4. Experiments on MuJoCo Benchmarks We empirically evaluate the Lyapunov-based PG algorithms to assess: (i) the performance in terms of cost and safety during training, and (ii) robustness with respect to constraint violations in the presence of function approximation errors. To that end, we design three interpretable experiments in simulated robot locomotion continuous control tasks us-
ing the MuJoCo simulator (Todorov et al., 2012). The tasks notions of safety are motivated by physical constraints: (i)HalfCheetah-Safe: The HalfCheetah agent is rewarded for running, but its speed is limited for stability and safety; (ii) Point-Circle: The Point agent is rewarded for running in a wide circle, but is constrained to stay within a safe region defined by |x| ≤ xlim (Achiam et al., 2017); (iii) Point-Gather & Ant-Gather: Point or Ant Gatherer agent, is rewarded for collecting target objects in a terrain map, while being constrained to avoid bombs (Achiam et al., 2017). Visualizations of these tasks as well as more details of the network architecture used in training the algorithms are given in Appendix C. 
We compare the presented methods with two state-of-the-art unconstrained reinforcement learning algorithms, DDPG (Lillicrap et al., 2015) and PPO (Schulman et al., 2017), and two constrained methods, Lagrangian approach with optimized hyper-parameters for fairness (Appendix B) and on-policy CPO algorithm (Achiam et al., 2017). The original CPO is based on TRPO (?). We use its PPO alternative (which coincides with the SPPO algorithm derived in Section 4.1) as the safe RL baseline. SPPO preserves the essence of CPO by adding the first order constraint and the relative entropy regularization to the policy optimization problem. The main difference between CPO and SPPO is that the latter does not perform backtracking line-search in learning rate. The decision to compare with SPPO instead of CPO is 1) to avoid the additional computational complexity of line-search in TRPO, while maintaining the performance of PG using the popular PPO algorithm, 2) to have a back-propagatable version of CPO, and 3) to have a fair comparison with other back-propagatable safe RL algorithms, such as the DDPG and safety layer counterparts. 
Comparisons with baselines: The Lyapunov-based PG algorithms are stable in learning and all methods converge to feasible policies with reasonable performance (Figures 1a, 1c, 1e, 1g, 2a, 2c, 2e, 2g). In contrast, when examining the constraint violation (Figures 1b, 1d, 1f, 1h, 2b, 2d, 2f, 2g), the Lyapunov-based PG algorithms quickly stabilize the constraint cost to be below the threshold, while the unconstrained DDPG and PPO agents violate the constraints in these environments, and the the Lagrangian approach tends to jiggle around the constrain threshold. Furthermore it is worth-noting that the Lagrangian approach can be sensitive to the initialization of the Lagrange multiplier λ0. If λ0 is too large, it would make policy updates overly conservative, while if λ0 is too small then constraint violation will be more pronounced. Without further knowledge about the environment, here we treat λ0 as a hyper-parameter and optimize it via grid-search. See Appendix C for more detail. 
a-projection vs. θ-projection: In many cases the a-projection (DDPG and PPO a-projections) converges faster and has lower constraint violation than its θ-projection counterpart (SDDPG, SPPO). This corroborates with the hypothesis that the a-projection approach is less conservative dur-
Lyapunov-based Safe Policy Optimization for Continuous Control 
0 20 40 60 80 100 100 
50 
0 
50 
100 
(a) HalfCheetah-Safe, Return (b) HalfCheetah-Safe, Constraint 
0 20 40 60 80 100 0 
2 
4 
6 
8 
10 
12 
14 
(c) Point-Gather, Return (d) Point-Gather, Constraint 
0 10 20 30 40 50 60 70 80 90 10 
8 
6 
4 
2 
0 
2 
4 
(e) Ant-Gather, Return (f) Ant-Gather, Constraint 
0 20 40 60 80 100 0 
200 
400 
600 
800 
1000 
1200 
1400 
(g) Point-Circle, Return (h) Point-Circle, Constraint 
Figure 2. PPO (red), PPO-Lagrangian (cyan), SPPO (blue), SPPO a-projection (green) on HalfCheetah-Safe and Point-Gather. Ours (PPO, SPPO a-projection) perform stable and safe learning, when the dynamics and cost functions are not known, control actions are continuous, and deep function approximations are necessary. 
ing policy updates than the θ-projection approach (which is what CPO is based on) and generates smoother gradient updates during end-to-end training, resulting in more effective learning than CPO (θ-projection). 
DDPG vs. PPO: Finally, in most experiments (HalfCheetah, PointGather, and AntGather) the DDPG algorithms tend to have faster learning than the PPO counterpart, while the PPO algorithms have better control on constraint violations (which are able to satisfy lower constraint thresholds). The faster learning behavior is potentially due to the improved data-efficiency when using off-policy samples in PG updates, however the covariate-shift in off-policy data makes tight constraint control more challenging. 
5. Safe Policy Gradient for Robot Navigation We now evaluate the safe policy optimization on a real robot task – point to point (P2P) navigation (Chiang et al., 2019) – where a noisy differential drive robot with limited sensors (Fig. 3a), is required to navigate to a goal outside of its 
(a) Noisy Lidar observation in a corridor 
22x18 m 
Velocity and orientation @ 5 Hz 
Reward: Distance to reach goal Constraint: Total energy on collision Robot Agent                Training Environment: 22 x 18m 
Observations: Noisy 1D lidar + Goal + Robot orientation 
 Safe-DDPG 
Parameters, θ Policy, 
𝛑θ(o, a) = P(a|o) 
ActionActor 
Critic 
(b) SDDPG for point to point task 
Figure 3. Robot navigation task details. 
visual field of view while avoiding collisions with obstacles. The agent’s observations consist of the relative goal position, the relative goal velocity, and the Lidar measurements (Fig. 3a). The actions are the linear and angular velocity vector at the robot’s center of the mass. The transition probability captures the noisy differential drive robot dynamics, whose exact formulation is not known to the robot. The robot must navigate to arbitrary goal positions collision-free and without memory of the workspace topology. 
Here the CMDP is non-discounting and has a fixed horizon. We reward the agent for reaching the goal, which translates to an immediate cost that measures the relative distance to goal. To measure the impact energy of obstacle collisions, we impose an immediate constraint cost to account for the speed during collision, with a constraint threshold d0 that characterizes the agent’s maximum tolerable collision impact energy to any objects. This type of constraint allows the robot to touch the obstacle (such as walls) but prevent it from ramming into any objects. Under this CMDP framework (Fig. 3b), the main goal is to train a policy π∗ that drives the robot along the shortest path to the goal and to limit the total impact energy of obstacle collisions. Furthermore, we note that due to limited data, in practice intermediate point-to-point policies are deployed on the real-world robot to collect more samples for further training. Therefore, guaranteeing safety during training is critical in this application. Descriptions about the robot navigation problem, including training and evaluation environments are in Appendix D. 
Experimental Results: We evaluate the learning algorithms in terms of average mission success percentage and constraint control. The task is successful if the robot reaches the goal before the constraint threshold (total energy of collision) is exhausted, and the success rate is averaged over 100 evaluation episodes with random initialization. While all methods converge to policies with reasonable performance, Figure 4a and 4b shows that the Lyapunov-based PG algorithms have higher success rates, due to their robust abilities of controlling the total constraint, as well minimizing the distance to goal. Although the unconstrained method often yields a lower distance to goal, it violates the constraint more frequently and thus leads to a lower success
Lyapunov-based Safe Policy Optimization for Continuous Control 
(a) Navigation, Mission Success % (b) Navigation, Constraint 
Figure 4. DDPG (red), DDPG-Lagrangian (cyan), SDDPG (blue), DDPG a-projection (green) on Robot Navigation. Ours (SDDPG, SDDPG a-projection) balance between reward and constraint learning. Unit of x-axis is in thousands of steps. The shaded areas represent the 1-SD confidence intervals (over 50 runs). The dashed purple line represents the constraint limit. 
(a) Lagrangian policy (b) SDDPG (a-proj.) (c) SDDPG (a-proj.) on robot 
Figure 5. Navigation routes of two policies on a similar setup (a) and (b). Log of on-robot experiments (c). Larger version in Ap-pendix D and the video is available in the supplementary materials. 
rate. Furthermore, note that the Lagrangian approach is less robust to initialization of parameters, and therefore it generally has lower success rate and higher variability than the Lyapunov-based methods. Unfortunately due to function approximation error and stochasticity of the problem, all the algorithms converged pre-maturely with constraints above the threshold. One reason is due to the constraint threshold (d0 = 100) being overly-conservative. In real-world problems guaranteeing constraint satisfaction is more challenging than maximizing return, and that usually requires much more training data. Finally, Figures 5a and 5b illustrate the navigation routes of two policies. On similar goal configurations, the Lagrangian method tends to zigzag and has more collisions, while the Lyapunov-based algorithm (SDDPG) chooses a safer path to reach the goal. 
Next, we evaluate how well the methods generalize to (i) longer trajectories, and (ii) new environments. P2P tasks are trained in a 22 by 18 meters environment (Fig. 7) with goals placed within 5 to 10 meters from the robot initial state, Figure 6 depicts the results evaluations, averaged over 100 trials, on P2P tasks in a much larger evaluation environment (60 by 47 meters) with goals placed up to 15 meters away from the goal. The success rate of all methods degrades as the goals are further away (Fig. 6a), and the safety methods (a-projection – SL-DDPG, and θ-projection – SG-DDPG) 
outperform unconstrained and Lagrangian (DDPG and LA-DDPG) as the task becomes more difficult. At the same time, our methods retain the lower constraints even when the task is difficult (Fig. 6b). 
(a) Navigation, Mission Success % (b) Navigation, Constraint 
Figure 6. Robot navigation generalization over success rate (a) and constraint satisfaction (b) on a different environment. 
Finally, we deployed the SL-DDPG policy onto the real Fetch robot (Melonee Wise & Dymesich, 2016) in an everyday office environment. Figure 5c shows the top down view of the robot log. Robot travelled a total of 500 meters to complete five repetitions of 12 tasks, each averaging about 10 meters to the goal. The experiments included narrow corridors and people walking through the office. The robot robustly avoids both static and dynamic (humans) obstacles coming into its path. We observed additional ”wobbling” effects, that was not present in simulation. This is likely due to the wheel slippage at the floor that the policy was not trained for. In several occasions when the robot could not find a clear path, the policy instructed the robot to stay put instead of narrowly passing by the obstacle. This is precisely the safety behavior we want to achieve with the Lyapunov-based algorithms. 
6. Conclusions We formulated safe RL as a continuous action CMDP and developed two classes, θ-projection and a-projection, of policy optimization algorithms based on Lyapunov functions to learn safe policies with high expected cumulative return. We do so by combining both on and off-policy optimization (DDPG or PPO) with a critic that evaluates the policy and computes its corresponding Lyapunov function. We evaluated our algorithms on four high-dimensional simulated robot locomotion tasks and compared them with several baselines. To demonstrate the effectiveness of the Lyapunov-based algorithms in solving real-world problems, we also apply these algorithms to indoor robot navigation, to ensure that the agent’s path is optimal and collision-free. Our results indicate that our Lyapunov-based algorithms 1) achieve safe learning, 2) have better data-efficiency, 3) can be more naturally integrated within the standard end-to-end differentiable policy gradient training pipeline, and 4) are scalable to tackle real-world problems. Our work is a step forward in deploying RL to real-world problems in which safety guarantees are of paramount importance. Future work includes 1) further exploration of Lyapunov function properties to improve training stability and safety, 2) more efficient
Lyapunov-based Safe Policy Optimization for Continuous Control 
use of Lyapunov constraints in constrained policy optimization, and 3) extensions of the Lyapunov-approach to the model-based setting to better utilize the agent’s dynamics. 
References Achiam, J., Held, D., Tamar, A., and Abbeel, P. Constrained 
policy optimization. arXiv preprint arXiv:1705.10528, 2017. 
Altman, E. Constrained Markov decision processes with total cost criteria: Lagrangian approach and dual linear program. Mathematical methods of operations research, 48(3):387–417, 1998. 
Altman, E. Constrained Markov decision processes, volume 7. CRC Press, 1999. 
Amos, B. and Kolter, Z. Optnet: Differentiable optimization as a layer in neural networks. arXiv preprint arXiv:1703.00443, 2017. 
Berkenkamp, F., Turchetta, M., Schoellig, A., and Krause, A. Safe model-based reinforcement learning with stability guarantees. In Advances in Neural Information Processing Systems, pp. 908–918, 2017. 
Bertsekas, D. Nonlinear programming. Athena scientific Belmont, 1999. 
Bertsekas, D. Dynamic programming and optimal control, volume 1-2. Athena scientific Belmont, MA, 2005. 
Chiang, H. L., Faust, A., Fiser, M., and Francis, A. Learn-ing navigation behaviors end to end with autorl. IEEE Robotics and Automation Letters, to appear, 2019. URL http://arxiv.org/abs/1809.10124. 
Chow, Y., Ghavamzadeh, M., Janson, L., and Pavone, M. Risk-constrained reinforcement learning with percentile risk criteria. The Journal of Machine Learning Research, 18(1):6070–6120, 2017. 
Chow, Y., Nachum, O., Ghavamzadeh, M., and Duenez-Guzman, E. A Lyapunov-based approach to safe reinforcement learning. In Accepted at NIPS, 2018. 
Dalal, G., Dvijotham, K., Vecerik, M., Hester, T., Paduraru, C., and Tassa, Y. Safe exploration in continuous action spaces. arXiv preprint arXiv:1801.08757, 2018. 
Faust, A., Ruymgaart, P., Salman, M., Fierro, R., and Tapia, L. Continuous action reinforcement learning for controlaffine systems with unknown dynamics. Acta Automat-ica Sinica Special Issue on Extensions of Reinforcement Learning and Adaptive Control, IEEE/CAA Journal of, 1 (3):323–336, July 2014. 
Faust, A., Ramirez, O., Fiser, M., Oslund, K., Francis, A., Davidson, J., and Tapia, L. PRM-RL: Long-range robotic navigation tasks by combining reinforcement learning and sampling-based planning. In Proc. IEEE Int. Conf. Robot. Autom. (ICRA), pp. 5113–5120, Brisbane, Australia, 2018. URL https://arxiv.org/abs/ 1710.03937.
Lyapunov-based Safe Policy Optimization for Continuous Control 
Geibel, P. and Wysotzki, F. Risk-sensitive reinforcement learning applied to control under constraints. Journal of Artificial Intelligence Research, 24:81–108, 2005. 
Hafner, D., Davidson, J., and Vanhoucke, V. TensorFlow Agents: Efficient batched reinforcement learning in tensorflow. arXiv preprint arXiv:1709.02878, 2017. 
Kakade, S. and Langford, J. Approximately optimal approximate reinforcement learning. In ICML, volume 2, pp. 267–274, 2002. 
Kalashnikov, D., Irpan, A., Sampedro, P. P., Ibarz, J., Her-zog, A., Jang, E., Quillen, D., Holly, E., Kalakrishnan, M., Vanhoucke, V., and Levine, S. QT-Opt: Scalable deep reinforcement learning for vision-based robotic manipulation. 2018. URL https://arxiv.org/pdf/ 1806.10293. 
Khalil, H. Noninear systems. Prentice-Hall, New Jersey, 2 (5):5–1, 1996. 
Levine, S., Finn, C., Darrell, T., and Abbeel, P. End-to-end training of deep visuo-motor policies. Journal of Machine Learning Research, 17:1–40, 2016. 
Lillicrap, T., Hunt, J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971, 2015. 
Lillicrap, T., Hunt, J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning. In International Conference on Learning Representations, 2016. 
Melonee Wise, Michael Ferguson, D. K. E. D. and Dymesich, D. Fetch & freight: Standard platforms for service robot applications. In Workshop on Autonomous Mobile Service Robots held at the 2016 International Joint Conference on Artificial Intelligence, 2016. 
Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013. 
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A., Veness, J., Bellemare, M., Graves, A., Riedmiller, M., Fidjeland, A., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., Antonoglou, I., King, H., Kumaran, D., Wierstra, D., Legg, S., and Hassabis, D. Human-level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015. 
Perkins, T. and Barto, A. Lyapunov design for safe reinforcement learning. Journal of Machine Learning Research, 3 (Dec):803–832, 2002. 
Schaul, T., Quan, J., Antonoglou, I., and Silver, D. Priori-tized experience replay. arXiv preprint arXiv:1511.05952, 2015. 
Schulman, J., Levine, S., Moritz, P., Jordan, M., and Abbeel, P. Trust region policy optimization. In Proceedings of the 32nd International Conference on Machine Learning, pp. 1889–1897, 2015a. 
Schulman, J., Moritz, P., Levine, S., Jordan, M., and Abbeel, P. High-dimensional continuous control using generalized advantage estimation. arXiv preprint arXiv:1506.02438, 2015b. 
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., and Klimov, O. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017. 
Silver, D., Huang, A., Maddison, C., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J., Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., and Hassabis, D. Mastering the game of Go with deep neural networks and tree search. Nature, 529(7587):484–489, 2016. 
Sutton, R., McAllester, D., Singh, S., and Mansour, Y. Pol-icy gradient methods for reinforcement learning with function approximation. In Proceedings of Advances in Neural Information Processing Systems 12, pp. 1057– 1063, 2000. 
Todorov, E., Erez, T., and Tassa, Y. Mujoco: A physics engine for model-based control. In Intelligent Robots and Systems (IROS), 2012 IEEE/RSJ International Con-ference on, pp. 5026–5033. IEEE, 2012. 
Yu, Y., Li, Y., Schuurmans, D., and Szepesvári, C. A general projection property for distribution families. In Ad-vances in Neural Information Processing Systems, pp. 2232–2240, 2009.
Lyapunov-based Safe Policy Optimization for Continuous Control 
A. The Lyapunov Approach to Solve CMDPs In this section, we revisit the Lyapunov approach to solving CMDPs that was proposed by Chow et al. (2018) and report the mathematical results that are important in developing our safe policy optimization algorithms. To start, without loss of generality, we assume that we have access to a baseline feasible policy of Equation 1, πB ; i.e. πB satisfies DπB (x0) ≤ d0. We define a set of Lyapunov functions w.r.t. initial state x0 ∈ X and constraint threshold d0 as 
LπB (x0, d0)={L : X →R≥0 : TπB ,d[L](x)≤L(x),∀x ∈ X ; L(x0) ≤ d0}, 
and call the constraints in this feasibility set the Lyapunov constraints. For any arbitrary Lyapunov function L ∈ LπB (x0, d0), we denote by 
FL(x) = { π(·|x) ∈ ∆ : Tπ,d[L](x) ≤L(x) 
} the set of L-induced Markov stationary policies. Since Tπ,d is a contraction mapping (Bertsekas, 2005), any L-induced policy π has the propertyDπ(x) = limk→∞ T kπ,d[L](x) ≤ L(x), ∀x ∈ X . Together with the property that L(x0) ≤ d0, they imply that any L-induced policy is a feasible policy of Equation 1. However, in general, the set FL(x) does not necessarily contain an optimal policy of Equation 1, and thus it is necessary to design a Lyapunov function (w.r.t. a baseline policy πB) that provides this guarantee. In other words, the main goal is to construct a Lyapunov function L ∈ LπB (x0, d0) such that 
L(x) ≥ Tπ∗,d[L](x), L(x0) ≤ d0. (8) 
Chow et al. (2018) show in their Theorem 1 that 1) without loss of optimality, the Lyapunov function can be expressed as 
Lε(x) := E 
 ∞∑ t=0 
γt(d(xt) + ε(xt)) | πB , x 
 , where ε(x) ≥ 0 is some auxiliary constraint cost uniformly upper-bounded by 
ε∗(x) := 2DmaxDTV (π∗||πB)(x)/(1− γ), 
and 2) if the baseline policy πB satisfies the condition 
max x∈X 
ε∗(x) ≤ Dmax ·min 
{ (1− γ) 
d0 −DπB (x0) 
Dmax , Dmax − (1− γ)D Dmax + (1− γ)D 
} , 
where D = maxx∈X maxπ Dπ(x) is the maximum constraint cost, then the Lyapunov function candidate Lε∗ also satisfies the properties of Equation 8, and thus, its induced feasible policy set FLε∗ contains an optimal policy. Furthermore, suppose that the distance between the baseline and optimal policies can be estimated effectively. Using the set of Lε∗ -induced feasible policies and noting that the safe Bellman operator T [V ](x) = minπ∈FLε∗ (x) Tπ,c[V ](x) is monotonic and contractive, one can show that T [V ](x) = V (x), ∀x ∈ X has a unique fixed point V ∗, such that V ∗(x0) is a solution of Equation 1, and an optimal policy can be constructed via greedification, i.e., π∗(·|x) ∈ arg minπ∈FLε∗ (x) Tπ,c[V 
∗](x). This shows that under the above assumption, Equation 1 can be solved using standard dynamic programming (DP) algorithms. While this result connects CMDP with Bellman’s principle of optimality, verifying whether πB satisfies this assumption is challenging when a good estimate of DTV (π∗||πB) is not available. To address this issue, Chow et al. (2018) propose to approximate ε∗ with an auxiliary constraint cost ε̃, which is the largest auxiliary cost satisfying the Lyapunov condition Lε̃(x) ≥ TπB ,d[Lε̃](x), ∀x ∈ X and the safety condition Lε̃(x0) ≤ d0. The intuition here is that the larger ε̃, the larger the set of policies FLε̃ . Thus, by choosing the largest such auxiliary cost, we hope to have a better chance of including the optimal policy π∗ in the set of feasible policies. Specifically, ε̃ is computed by solving the following linear programming (LP) problem: 
ε̃ ∈ arg max ε:X→R≥0 
{∑ x∈X 
ε(x) : d0 −DπB (x0) ≥ 1(x0)> ( I − γ 
{ P ( x′|x, πB(x) 
)} x,x′∈X 
)−1 
ε 
} , (9) 
where 1(x0) represents a one-hot vector in which the non-zero element is located at x = x0. When πB is a feasible policy, this problem has a non-empty solution. Furthermore, according to the derivations in Chow et al. (2018), the maximizer of (9) has the following form: 
ε̃(x) = 
( d0 −DπB (x0) 
) · 1{x = x} 
E [∑∞ 
t=0 γ t1{xt = x} | x0, πB 
] ≥ 0,
Lyapunov-based Safe Policy Optimization for Continuous Control 
where x ∈ arg minx∈X E [∑∞ 
t=0 γ t1{xt = x} | x0, πB 
] . They also show that by further restricting ε̃(x) to be a constant 
function, the maximizer is given by 
ε̃(x) = (1− γ) · (d0 −DπB (x0)), ∀x ∈ X . 
Using the construction of the Lyapunov function Lε̃, Chow et al. (2018) propose the safe policy iteration (SPI) algorithm (see Algorithm 1) in which the Lyapunov function is updated via bootstrapping, i.e., at each iteration Lε̃ is recomputed using Equation 9 w.r.t. the current baseline policy. At each iteration k, this algorithm has the following properties: 1) Consistent Feasibility, i.e., if the current policy πk is feasible, then πk+1 is also feasible; 2) Monotonic Policy Improvement, i.e., Cπk+1 
(x) ≤ Cπk(x) for any x ∈ X ; and 3) Asymptotic Convergence. Despite all these nice properties, SPI is still a value-function-based algorithm, and thus it is not straightforward to use it in continuous action problems. The main reason is that the greedification step becomes an optimization problem over the continuous set of actions that is not necessarily easy to solve. In Section 3, we show how we use SPI and its nice properties to develop safe policy optimization algorithms that can handle continuous action problems. Our algorithms can be thought as combinations of DDPG or PPO (or any other on-policy or off-policy policy optimization algorithm) with a SPI-inspired critic that evaluates the policy and computes its corresponding Lyapunov function. The computed Lyapunov function is then used to guarantee safe policy update, i.e., the new policy is selected from a restricted set of safe policies defined by the Lyapunov function of the current policy. 
Algorithm 1 Safe Policy Iteration (SPI) Input: Initial feasible policy π0; for k = 0, 1, 2, . . . do 
Step 0: With πb = πk, evaluate the Lyapunov function Lεk , where εk is a solution of Equation 9 Step 1: Evaluate the cost value function Vπk (x) = Cπk (x); Then update the policy by solving the following problem: πk+1(·|x) ∈ argminπ∈FLεk (x) Tπ,c[Vπk ](x),∀x ∈ X 
end for Return Final policy πk∗
Lyapunov-based Safe Policy Optimization for Continuous Control 
B. Lagrangian Approach to Safe RL There are a number of mild technical and notational assumptions which we will make throughout this section, so we state them here. 
Assumption 1 (Differentiability). For any state-action pair (x, a), πθ(a|x) is continuously differentiable in θ and∇θπθ(a|x) is a Lipschitz function in θ for every a ∈ A and x ∈ X . 
Assumption 2 (Strict Feasibility). There exists a transient policy πθ(·|x) such that Dπθ (x0) < d0 in the constrained problem. 
Assumption 3 (Step Sizes). The step size schedules {α3,k}, {α2,k}, and {α1,k} satisfy∑ k 
α1,k = ∑ k 
α2,k = ∑ k 
α3,k =∞, (10)∑ k 
α2 1,k, 
∑ k 
α2 2,k, 
∑ k 
α2 3,k <∞, (11) 
α1,k = o ( α2,k 
) , ζ2(i) = o 
( α3,k 
) . (12) 
Assumption 1 imposes smoothness on the optimal policy. Assumption 2 guarantees the existence of a local saddle point in the Lagrangian analysis introduced in the next subsection. Assumption 3 refers to step sizes corresponding to policy updates that will be introduced for the algorithms in this paper, and indicates that the update corresponding to {α3,k} is on the fastest time-scale, the updates corresponding to {α2,k} is on the intermediate time-scale, and the update corresponding to {α1,k} is on the slowest time-scale. As this assumption refer to user-defined parameters, they can always be chosen to be satisfied. 
To solve the CMDP, we employ the Lagrangian relaxation procedure (Bertsekas, 1999) to convert it to the following unconstrained problem: 
max λ≥0 
min θ 
( L(θ, λ) 
4 = Cπθ (x0) + λ 
( Dπθ (x0)− d0 
)) , (13) 
where λ is the Lagrange multiplier. Notice that L(θ, λ) is a linear function in λ. Then there exists a local saddle point (θ∗, λ∗) for the minimax optimization problem maxλ≥0 minθ L(θ, λ), such that for some r > 0, ∀θ ∈ Rκ ∩ Bθ∗(r) and ∀λ ∈ [0, λmax], we have 
L(θ, λ∗) ≥ L(θ∗, λ∗) ≥ L(θ∗, λ), (14) 
where Bθ∗(r) is a hyper-dimensional ball centered at θ∗ with radius r > 0. 
In the following, we present a policy gradient (PG) algorithm and an actor-critic (AC) algorithm. While the PG algorithm updates its parameters after observing several trajectories, the AC algorithms are incremental and update their parameters at each time-step. 
We now present a policy gradient algorithm to solve the optimization problem Equation 13. The idea of the algorithm is to descend in θ and ascend in λ using the gradients of L(θ, λ) w.r.t. θ and λ, i.e., 
∇θL(θ, λ) = ∇θ ( Cπθ (x0) + λDπθ (x0) 
) , ∇λL(θ, λ) = Dπθ (x0)− d0. (15) 
The unit of observation in this algorithm is a system trajectory generated by following policy πθk . At each iteration, the algorithm generates N trajectories by following the current policy, uses them to estimate the gradients in Equation 15, and then uses these estimates to update the parameters θ, λ. 
Let ξ = {x0, a0, c0, x1, a1, c1, . . . , xT−1, aT−1, cT−1, xT } be a trajectory generated by following the policy θ, where xT = xTar is the target state of the system and T is the (random) stopping time. The cost, constraint cost, and probability of ξ are defined as C(ξ) = 
∑T−1 k=0 γ 
kc(xk, ak),D(ξ) = ∑T−1 k=0 γ 
kd(xk), and Pθ(ξ) = P0(x0) ∏T−1 k=0 πθ(ak|xk)P (xk+1|xk, ak), 
respectively. Based on the definition of Pθ(ξ), one obtains∇θ log Pθ(ξ) = ∑T−1 k=0 ∇θ log πθ(ak|xk). 
Algorithm 2 contains the pseudo-code of our proposed policy gradient algorithm. What appears inside the parentheses on the right-hand-side of the update equations are the estimates of the gradients of L(θ, λ) w.r.t. θ, λ (estimates of the expressions in 15). Gradient estimates of the Lagrangian function are given by 
∇θL(θ, λ) = ∑ ξ 
Pθ(ξ) · ∇θ log Pθ(ξ) ( Cπθ (ξ) + λDπθ (ξ) 
) , ∇λL(θ, λ) = −d0 + 
∑ ξ 
Pθ(ξ) · D(ξ),
Lyapunov-based Safe Policy Optimization for Continuous Control 
where the likelihood gradient is 
∇θ log Pθ(ξ) =∇θ 
 T−1∑ k=0 
logP (xk+1|xk, ak) + log πθ(ak|xk) + log 1{x0 = x0} 
 = 
T−1∑ k=0 
∇θ log πθ(ak|xk) = 
T−1∑ k=0 
1 
πθ(ak|xk) ∇θπθ(ak|xk). 
In the algorithm, ΓΛ is a projection operator to [0, λmax], i.e., ΓΛ(λ) = arg minλ̂∈[0,λmax] ‖λ − λ̂‖ 2 2, which ensures the 
convergence of the algorithm. Recall from Assumption 3 that the step-size schedules satisfy the standard conditions for stochastic approximation algorithms, and ensure that the policy parameter θ update is on the fast time-scale 
{ ζ2,i } 
, and the Lagrange multiplier λ update is on the slow time-scale 
{ ζ1,i } 
. This results in a two time-scale stochastic approximation algorithm, which has shown to converge to a (local) saddle point of the objective function L(θ, λ). This convergence proof makes use of standard in many stochastic approximation theory, because in the limit when the step-size is sufficiently small, analyzing the convergence of PG is equivalent to analyzing the stability of an ordinary differential equation (ODE) w.r.t. its equilibrium point. 
In policy gradient, the unit of observation is a system trajectory. This may result in high variance for the gradient estimates, especially when the length of the trajectories is long. To address this issue, we propose two actor-critic algorithms that use value function approximation in the gradient estimates and update the parameters incrementally (after each state-action transition). We present two actor-critic algorithms for optimizing Equation 13. These algorithms are still based on the above gradient estimates. Algorithm 3 contains the pseudo-code of these algorithms. The projection operator ΓΛ is necessary to ensure the convergence of the algorithms. Recall from Assumption 3 that the step-size schedules satisfy the standard conditions for stochastic approximation algorithms, and ensure that the critic update is on the fastest time-scale 
{ α3,k 
} , the 
policy and θ-update { α2,k 
} is on the intermediate timescale, and finally the Lagrange multiplier update is on the slowest 
time-scale { α1,k 
} . This results in three time-scale stochastic approximation algorithms. 
Using the policy gradient theorem from Sutton et al. (2000), one can show that 
∇θL(θ, λ) = ∇θVθ(x0) = 1 
1− γ ∑ x,a 
µθ(x, a|x0) ∇ log πθ(a|x) Qθ(x, a), (16) 
where µθ is the discounted visiting distribution and Qθ is the action-value function of policy θ. We can show that 1 
1−γ∇ log πθ(ak|xk) · δk is an unbiased estimate of∇θL(θ, λ), where 
δk = cλ(xk, ak) + γV̂θ(xk+1)− V̂θ(xk) 
is the temporal-difference (TD) error, and V̂θ is the value estimator of Vθ. 
Traditionally, for convergence guarantees in actor-critic algorithms, the critic uses linear approximation for the value function Vθ(x) ≈ v>ψ(x) = V̂θ,v(x), where the feature vector ψ(·) belongs to a low-dimensional space Rκ2 . The linear approximation V̂θ,v belongs to a low-dimensional subspace SV = 
{ Ψv|v ∈ Rκ2 
} , where Ψ is a short-hand notation for 
the set of features, i.e., Ψ(x) = ψ>(x). Recently with the advances of deep neural networks, it has become increasingly popular to model the critic with a deep neural network architecture, based on the objective function of minimizing the MSE of Bellman residual w.r.t. Vθ or Qθ (Mnih et al., 2013).
Lyapunov-based Safe Policy Optimization for Continuous Control 
C. Experimental Setup in MuJoCo Tasks Our experiments are performed on safety-augmented versions of standard MuJoCo domains (Todorov et al., 2012). 
HalfCheetah-Safe. The agent is a the standard HalfCheetah (a 2-legged simulated robot rewarded for running at high speed) augmented with safety constraints. We choose the safety constraints to be defined on the speed limit. We constrain the speed to be less than 1, i.e., constraint cost is thus 1[|v| > 1] . Episodes are of length 200. The constraint threshold is 50. 
Point Circle. This environment is taken from (Achiam et al., 2017). The agent is a point mass (controlled via a pivot). The agent is initialized at (0, 0) and rewarded for moving counter-clockwise along a circle of radius 15 according to the reward −dx·y+dy·x 
1+| √ x2+y2−15| 
, for position x, y and velocity dx, dy. The safety constraint is defined as the agent staying in a position 
satisfying |x| ≤ 2.5. The constraint cost is thus 1[|x| > 2.5]. Episodes are of length 65. The constraint threshold is 7. 
Point Gather. This environment is taken from (Achiam et al., 2017). The agent is a point mass (controlled via a pivot) and the environment includes randomly positioned apples (2 apples) and bombs (8 bombs). The agent given a reward of 10 for each apple collected and a penalty of −10 for each bomb. The safety constraint is defined as number of bombs collected during the episode. Episodes are of length 15. The constraint threshold is 4 for DDPG and 2 for PPO. 
Ant Gather. This environment is is the same as Point Circle, only with an ant agent (quadrapedal simulated robot). Each episode is initialized with 8 apples and 8 bombs. The agent given a reward of 10 for each apple collected, a penalty reward of −20 for each bomb collected, and a penalty reward of −20 is incurred if the episode terminates prematurely (because the ant falls). Episodes are of length at most 500. The constraint threshold is 10 for DDPG algorithms and is 5 for PPO algorithms. 
Figure 7 shows the visualization of the above domains used in our experiments. 
HalfCheetah-Safe Point-Circle Ant-Gather Point-Gather 
Figure 7. The Robot Locomotion Control Tasks 
In these experiments there are three different agents: (1) a point-mass (X ⊆ R9, A ⊆ R2); an ant quadruped robot (X ⊆ R32, A ⊆ R8); (3) a half-cheetah (X ⊆ R18, A ⊆ R6). For all experiments, we use two neural networks with two hidden layers of size (100, 50) and ReLU activation to model the mean and log-variance of the Gaussian actor policy, and two neural networks with two hidden layers of size (200, 50) and tanh activation to model the critic and constraint critic. To build a low variance sample gradient estimate, we use GAE-λ (Schulman et al., 2015b) to estimate the advantage and constraint advantage functions, with a hyper-parameter λ ∈ (0, 1) optimized by grid-search. 
On top of the GAE parameter λ, in all numerical experiments and for each algorithm (SPPO θ-projection, SDDPG θ-projection, SPPO a-projection, SDDPG a-projection, CPO, Lagrangian, and the unconstrained PG counterparts), we systematically explored different parameter settings by doing grid-search over the following factors: (i) learning rates in the actor-critic algorithm, (ii) batch size, (iii) regularization parameters of the policy relative entropy term, (iv) with-or-without natural policy gradient updates, (v) with-or-without the emergency safeguard PG updates (see Appendix E.1 for more details). Although each algorithm might have a different parameter setting that leads to the optimal performance in training, the results reported here are the best ones for each algorithm, chosen by the same criteria (which is based on value of return plus certain degree of constraint satisfaction). To account for the variability during training, in each learning curve a 1-SD confidence interval is also computed over 10 separate random runs (under the same parameter setting).
Lyapunov-based Safe Policy Optimization for Continuous Control 
C.1. More Explanations on MuJoCo Results 
In all numerical experiments and for each algorithm (SPPO θ-projection, SDDPG θ-projection, SPPO a-projection, SDDPG a-projection, CPO, Lagrangian, and the unconstrained PG counterparts), we systematically explored various hyper-parameter settings by doing grid-search over the following factors: (i) learning rates in the actor-critic algorithm, (ii) batch size, (iii) regularization parameters of the policy relative entropy term, (iv) with-or-without natural policy gradient updates, (v) with-or-without the emergency safeguard PG updates (see Appendix E.1 for more details). Although each algorithm might have a different parameter setting that leads to the optimal training performance, the results reported in the paper are the best ones for each algorithm, chosen by the same criteria (which is based on value of return + certain degree of constraint satisfaction). 
In our experiments, we compare the two classes of safe RL algorithms, one derived from θ-projection (constrained policy optimization) and one from the a-projection (safety layer), with the unconstrained and Lagrangian baselines in four problems: PointGather, AntGather, PointCircle, and HalfCheetahSafe. We perform these experiments with both off-policy (DDPG) and on-policy (PPO) versions of the algorithms. 
In PointCircle DDPG, although the Lagrangian algorithm significantly outperforms the safe RL algorithms in terms of return, it violates the constraint more often. The only experiment in which Lagrangian performs similarly to the safe algorithms in terms of both return and constraint violation is PointCircle PPO. In all other experiments that are performed in the HalfCheetahSafe, PointGather and AntGather domains, either (i) the policy learned by Lagrangian has a significantly lower performance than that learned by one of the safe algorithms (see HalfCheetahSafe DDPG, PointGather DDPG, AntGather DDPG), or (ii) the Lagrangian method violates the constraint during training, while the safe algorithms do not (see HalfCheetahSafe PPO, PointGather PPO, AntGather PPO). This clearly illustrates the effectiveness of our Lyapunov-based safe RL algorithms, when compared to Lagrangian method.
Lyapunov-based Safe Policy Optimization for Continuous Control 
D. Experimental Setup in Robot Navigation P2P is a continuous control task with a goal of navigating a robot to any arbitrary goal position collision-free and without memory of the workspace topology. The goal is usually within 5− 10 meters from the robot agent, but it is not visible to the agent before the task starts, due to both limited sensor range and the presence of obstacles that block a clear line of sight. The agent’s observations, x = (g, ġ, l) ∈ R68, consists of the relative goal position, the relative goal velocity, and the Lidar measurements. Relative goal position, g, is the relative polar coordinates between the goal position and the current robot pose, and ġ is the time derivative of g, which indicates the speed of the robot navigating to the goal. This information is available from the robot’s localization sensors. Vector l is the noisy Lidar input (Fig. 3a), which measures the nearest obstacle in a direction within a 220◦ field of view split in 64 bins, up to 5 meters in depth. The action is given by a ∈ R2, which is linear and angular velocity vector at the robot’s center of the mass. The transition probability P : X ×A → X captures the noisy differential drive robot dynamics. Without knowing the full non-linear system dynamics, we here assume knowledge of a simplified blackbox kinematics simulator operating at 5Hz in which Gaussian noise, N (0, 0.1), is added to both the observations and actions in order to model the noise in sensing, dynamics, and action actuations in real-world. The objective of the P2P task is to navigate the robot to reach within 30 centimeters from any real-time goal. While the dynamics of this system is simpler than that of HalfCheetah. But unlike the MuJoCo tasks where the underlying dynamics are deterministic, in this robot experiment the sensor, localization, and dynamics noise paired with partial world observations and unexpected obstacles make this safe RL much more challenging. More descriptions about the indoor robot navigation problem and its implementation details can be found in Section 3 and 4 of Chiang et al. (2019). 
Here the CMDP is non-discounting and has a finite-horizon of T = 100. We reward the agent for reaching the goal, which translates to an immediate cost of c(x,a) = ‖g‖2, which measures the relative distance to goal. To measure the impact energy of obstacle collisions, we impose an immediate constraint cost of d(x,a) = ‖ġ‖ · 1{‖l‖ ≤ rimpact}/T , where rimpact is the impact radius w.r.t. the Lidar depth signal, to account for the speed during collision, with a constraint threshold d0 
that characterizes the agent’s maximum tolerable collision impact energy to any objects. (Here the total impact energy is proportional to the robot’s speed during any collisions.) Under this CMDP framework (Fig. 3b), the main goal is to train a policy π∗ that drives the robot along the shortest path to the goal and to limit the average impact energy of obstacle collisions. Furthermore, due to limited data any intermediate point-to-point policy is deployed on the robot to collect more samples for further training, therefore guaranteeing safety during training is critical in this application. 
(a) Training, 23 by 18m (b) Building 2, 60 by 47m 
Figure 8. (a) Training and (b) evaluation environments, generated from real office building plans. The evaluation environment is an order of magnitude bigger.
Lyapunov-based Safe Policy Optimization for Continuous Control 
(a) Lagrangian policy (b) SDDPG (a-proj.) (c) SDDPG (a-proj.) on robot 
Figure 9. Navigation routes of two policies on a similar setup (a) and (b). Log of on-robot experiments (c). 
E. Pseudo-code of the Safe Policy Gradient Algorithms 
Algorithm 2 Lagrangian Trajectory-based Policy Gradient Algorithm Input: parameterized policy π(·|·; θ) Initialization: policy parameter θ = θ0, and the Lagrangian parameter λ = λ0 
for i = 0, 1, 2, . . . do for j = 1, 2, . . . do 
Generate N trajectories {ξj,i}Nj=1 by starting at x0 and following the policy θi. end for 
θ Update: θi+1 = θi − α2,i 1 
N 
N∑ j=1 
∇θ log Pθ(ξj,i)|θ=θi ( C(ξj,i) + λiD(ξj,i) 
) λ Update: λi+1 = ΓΛ 
[ λi + α1,i 
( − d0 + 
1 
N 
N∑ j=1 
D(ξj,i) 
)] end for 
E.1. Practical Implementations of Safe PG 
Due to function approximation errors, even with the Lyapunov constraints in practice the safe PG algorithm may take a bad step and produce an infeasible policy update and cannot automatically recover from such a bad step. To tackle this issue, similar to Achiam et al. (2017) we propose the following safeguard policy update rule to purely decrease the constraint cost: θk+1 = θk − αsg,k∇θDπθ (x0)θ=θk , where αsg,k is the learning rate for safeguard update. If αsg,k >> αk (learning rate of PG), then with the safeguard update θ will quickly recover from the bad step but it might be overly conservative. This approach is principled because as soon as πθk is unsafe/infeasible w.r.t. CMDP, the algorithm uses a limiting search direction. One can directly extend this safeguard update to the multiple-constraint scenario by doing gradient descent over the constraint that has the worst violation. Another remedy to reduce the chance of constraint violation is to do constraint tightening on the constraint cost threshold. Specifically, instead of d0, one may pose the constraint based on d0 · (1− δ), where δ ∈ (0, 1) is the factor of safety for providing additional buffer to constraint violation. Additional techniques in cost-shaping have been proposed in Achiam et al. (2017) to smooth out the sparse constraint costs. While these techniques can further ensure safety, construction of the cost-shaping term requires knowledge from the environment, which makes the safe PG algorithms more complicated.
Lyapunov-based Safe Policy Optimization for Continuous Control 
Algorithm 3 Lagrangian Actor-Critic Algorithm Input: Parameterized policy π(·|·; θ) and value function feature vector φ(·) Initialization: policy parameters θ = θ0; Lagrangian parameter λ = λ0; value function weight v = v0 
while TRUE do for k = 0, 1, 2, . . . do 
Sample ak ∼ π(·|xk; θk); cλk (xk, ak) = c(xk, ak) + λkd(xk); xk+1 ∼ P (·|xk, ak); // AC Algorithm: 
TD Error: δk(vk) = cλk (xk, ak) + γV̂φk (xk+1)− V̂φk (xk) (17) 
Critic Update: vk+1 = vk + ζ3(k)δk(vk)ψ(xk) (18) 
θ Update: θk+1 = θk − ζ2(k)∇θ log πθ(ak|xk) · δk(vk)/1− γ (19) 
λ Update: λk+1 = ΓΛ 
( λk + ζ1(k) 
( − d0 + 
1 
N 
N∑ j=1 
D(ξj,i) )) 
(20) 
// NAC Algorithm: 
Critic Update: wk+1 = ( I − ζ3(k)∇θ log πθ(ak|xk)|θ=θk 
( ∇θ log πθ(ak|xk)|θ=θk 
)>) wk 
+ ζ3(k)δk(vk)∇θ log πθ(ak|xk)|θ=θk (21) 
θ Update: θk+1 = θk − ζ2(k)wk/1− γ (22) Other Updates: Follow from Eqs. 17, 18, and 20. 
end for end while
Lyapunov-based Safe Policy Optimization for Continuous Control 
Algorithm 4 Lyapunov-based Policy Gradient with θ-projection (SDDPG and SPPO) Input: Initial feasible policy π0; for k = 0, 1, 2, . . . do 
Step 0: With πb = πθk , generate N trajectories {ξj,k}Nj=1 of T steps by starting at x0 and following the policy θk Step 1: Using the trajectories {ξj,k}Nj=1, estimate the critic Qθ(x, a) and the constraint critic QD,θ(x, a); 
 For DDPG, these functions are trained by minimizing the MSE of Bellman residual, and one can also use off-policy samples from replay buffer (Schaul et al., 2015); 
 For PPO these functions can be estimated by the generalized advantage function technique from (Schulman et al., 2015b) 
Step 2: Based on the closed form solution of a QP problem with an LP constraint in Section 10.2 of (Achiam et al., 2017), calculate λ∗k with the following formula: 
λ∗k = 
−βk ε̃− (∇θQθ(x̄, ā) |θ=θk )> H(θk)−1∇θQD,θ(x̄, ā) |θ=θk( 
∇θQD,θ(x̄, ā) |θ=θk )> H(θk)−1∇θQD,θ(x̄, ā) |θ=θk 
 + 
, 
where 
∇θQθ(x̄, ā) = 1 
N 
∑ x,a∈ξj,k,1≤j≤N 
T−1∑ t=0 
γt∇θ log πθ(a|x)Qθ(x, a), 
∇θQD,θ(x̄, ā) = 1 
N 
∑ x,a∈ξj,k,1≤j≤N 
T−1∑ t=0 
γt∇θ log πθ(a|x)Qθ(x, a), 
βk is the adaptive penalty weight of the DKL(π||πθk ) regularizer, and H(θk) = ∇2 θDKL(π||πθ) |θ=θk is the Hessian of this term 
Step 3: Update the policy parameter by following the objective gradient; 
 For DDPG 
θk+1 ← θk − αk · 1 
N · T ∑ 
x∈ξj,k,1≤j≤N 
∇θπθ(x) |θ=θk ·(∇aQθk (x, a) + λ∗k∇aQD,θk (x, a)) |a=πθk (x) 
 For PPO, 
θk+1 ← θk − αk Nβk 
( H(θk) 
)−1 ∑ 
xj,t,aj,t∈ξj,k,1≤j≤N 
T−1∑ t=0 
γt · ∇θ log πθ(aj,t|xj,t) |θ=θk · 
(Qθk (xj,t,aj,t) + λ∗kQD,θk (xj,t,aj,t)) 
Step 4: At any given state x ∈ X , compute the feasible action probability a∗(x) via action projection in the safety layer, that takes inputs∇aQL(x, a) = ∇aQD,θk (x, a) and ε(x) = (1− γ)(d0 −QD,θk (x0, πk(x0))), for any a ∈ A. 
end for Return Final policy πθk∗ ,
Lyapunov-based Safe Policy Optimization for Continuous Control 
Algorithm 5 Lyapunov-based Policy Gradient with a-projection (SDDPG-modular and SPPO-modular) Input: Initial feasible policy π0; for k = 0, 1, 2, . . . do 
Step 0: With πb = πθk , generate N trajectories {ξj,k}Nj=1 of T steps by starting at x0 and following the policy θk Step 1: Using the trajectories {ξj,k}Nj=1, estimate the critic Qθ(x, a) and the constraint critic QD,θ(x, a); 
 For DDPG, these functions are trained by minimizing the MSE of Bellman residual, and one can also use off-policy samples from replay buffer (Schaul et al., 2015); 
 For PPO these functions can be estimated by the generalized advantage function technique from (Schulman et al., 2015b) 
Step 2: Update the policy parameter by following the objective gradient; 
 For DDPG θk+1 ← θk − αk · 
1 
N · T ∑ 
x∈ξj,k,1≤j≤N 
∇θπθ(x) |θ=θk ·∇aQθk (x, a) |a=πθk (x); 
 For PPO, 
θk+1 ← θk − αk Nβk 
( H(θk) 
)−1 ∑ 
xj,t,aj,t∈ξj,k,1≤j≤N 
T−1∑ t=0 
γt · ∇θ log πθ(aj,t|xj,t) |θ=θk ·Qθk (xj,t,aj,t) 
where βk is the adaptive penalty weight of the DKL(π||πθk ) regularizer, and H(θk) = ∇2 θDKL(π||πθ) |θ=θk is the Hessian of 
this term 
Step 3: At any given state x ∈ X , compute the feasible action probability a∗(x) via action projection in the safety layer, that takes inputs∇aQL(x, a) = ∇aQD,θk (x, a) and ε(x) = (1− γ)(d0 −QD,θk (x0, πk(x0))), for any a ∈ A. 
end for Return Final policy πθk∗ ,