> Source: https://proceedings.mlr.press/v119/wachi20a/wachi20a.pdf

Safe Reinforcement Learning in Constrained Markov Decision Processes 
Akifumi Wachi 1 Yanan Sui 2 
Abstract Safe reinforcement learning has been a promising approach for optimizing the policy of an agent that operates in safety-critical applications. In this paper, we propose an algorithm, SNO-MDP, that explores and optimizes Markov decision processes under unknown safety constraints. Specifi-cally, we take a stepwise approach for optimizing safety and cumulative reward. In our method, the agent first learns safety constraints by expanding the safe region, and then optimizes the cumulative reward in the certified safe region. We provide theoretical guarantees on both the satisfaction of the safety constraint and the near-optimality of the cumulative reward under proper regularity assumptions. In our experiments, we demonstrate the effectiveness of SNO-MDP through two experiments: one uses a synthetic data in a new, openlyavailable environment named GP-SAFETY-GYM, and the other simulates Mars surface exploration by using real observation data. 
1. Introduction In many real applications, environmental hazards are first detected in situ. For example, a planetary rover exploring Mars does not obtain high-resolution images at the time of its launch. In usual cases, after landing on Mars, the rover takes close-up images or observes terrain data. Leverag-ing the acquired data, ground operators identify whether each position is safe. Hence, for fully automated operation, an agent must autonomously explore the environment and guarantee safety. 
In most cases, however, guaranteeing safety (i.e., surviving) is not the primary objective. The optimal policy for ensuring safety is often extremely conservative (e.g., stay at the current position). Even though avoiding hazards is an 
1IBM Research AI, Tokyo, Japan 2Tsinghua University, Beijing, China. Correspondence to: Akifumi Wachi <aki-fumi.wachi@ibm.com>, Yanan Sui <ysui@tsinghua.edu.cn>. 
Proceedings of the 37 th International Conference on Machine Learning, Online, PMLR 119, 2020. Copyright 2020 by the author(s). 
essential requirement, the primary objective is nonetheless to obtain rewards (e.g., scientific gain). 
As a framework to solve this problem, safe reinforcement learning (safe RL, Garcıa & Fernández (2015)) has recently been noticed by the research community. The objective of safe RL is to maximize the cumulative reward while guaranteeing or encouraging safety. Especially in problem settings in which the reward and safety functions are unknown a priori, however, a great deal of previous work (e.g., Wachi et al. (2018)) theoretically guarantees the satisfaction of the safety constraint, but the acquired policy is not necessarily near-optimal in terms of the cumulative reward. In this paper, we propose a safe RL algorithm that guarantees a near-optimal cumulative reward while guaranteeing the satisfaction of the safety constraint as well. 
Related work. Conventional reinforcement learning literature has been agnostic with respect to safety, while pursuing efficiency and optimality of the cumulative reward. Representatives of such work are probably approximately correct Markov decision process (PAC-MDP) algorithms (Brafman & Tennenholtz, 2002; Kearns & Singh, 2002; Strehl et al., 2006). Algorithms with the PAC-MDP property enable an agent to learn a near-optimal behavior with a polynomial number of samples. In addition, Kolter & Ng (2009) and Araya et al. (2012) proposed algorithms to obtain an ε-close solution to the Bayesian optimal policy. 
As the research community tries to apply RL algorithms to real-world systems, however, safety issues have been highlighted. RL algorithms inherently require an agent to explore unknown state-action pairs, and algorithms that are agnostic with respect to safety may execute unsafe actions without deliberateness. Hence, it is important to develop algorithms that guarantee safety even during training, at least with high probability. 
A notable approach is safe model-based RL (Berkenkamp et al., 2017; Fisac et al., 2018). In this domain, safety is associated with a state constraint; thus, the resulting algorithm is well suited for such contexts as a drone learning how to hover. The parameters of a drone are not perfectly known a priori, but we have prior knowledge on what states are unsafe (e.g., a pitch angle of more than 50 degrees is unsafe). In the field of control theory, constrained model predictive
Safe Reinforcement Learning in Constrained Markov Decision Processes 
control (Mayne et al., 2000) has been popular. For example, Aswani et al. (2013) proposed an algorithm for guaranteeing robust feasibility and constraint satisfaction for a learned model using constrained model predictive control. 
On the other hand, safe model-free RL has also been successful, especially in continuous control tasks. For example, Achiam et al. (2017) proposed the constrained policy optimization (CPO) algorithm while guaranteeing safety in terms of constraint satisfaction. Moreover, Chow et al. (2019) leveraged Lyapunov functions to learn policies with high expected cumulative reward, while guaranteeing the satisfaction of safety constraints. 
Finally, several previous studies have addressed how to explore a safe space in an environment that is unknown a priori (Sui et al., 2015; Turchetta et al., 2016). This type of problem setting is well-suited for cases such as a robot exploring an uncertain environment (e.g., a planetary surface, a disaster site). In particular, under the safety constraint, Sui et al. (2018) proposed a stepwise algorithm for finding the maximum value of the reward function in a state-less setting (i.e., the bandit problem), while Wachi et al. (2018) proposed an algorithm for maximizing the cumulative reward in an MDP setting (i.e., the planning problem). 
Our contributions. We propose a safe near-optimal MDP, SNO-MDP algorithm, for achieving a near-optimal cumulative reward while guaranteeing safety in a constrained MDP. This algorithm first explores the safety function and then optimizes the cumulative reward in the certified safe region. We further propose an algorithm called Early Stopping of Exploration of Safety (ES2) to achieve faster convergence while maintaining probabilistic guarantees with respect to both safety and reward. We examine SNO-MDP by applying PAC-MDP analysis and prove that, with high probability, the acquired policy is near-optimal with respect to the cumulative reward while guaranteeing safety. We build an openly-available test-bed called GP-SAFETY-GYM for synthetic experiments.1 The safety and efficiency of SNO-MDP are then evaluated with two experiments: one in the GP-SAFETY-GYM synthetic environment, and the other using real Mars terrain data. 
2. Problem Statement A safety constrained MDP is defined as a tuple 
M = 〈S,A, f, r, g, γ〉, 
where S is a finite set of states {s},A is a finite set of actions {a}, f : S × A → S is a deterministic state transition function, r : S → (0, Rmax] is a bounded reward function, 
1https://github.com/akifumi-wachi-4/safe_ near_optimal_mdp 
g : S → R is a safety function, and γ ∈ R is a discount factor. We assume that both the reward function r and the safety function g are not known a priori. At every time step t ∈ N, the agent must be in a “safe” state. More concretely, for a state st, the safety function value g(st) must be above a threshold h ∈ R; that is, the safety constraint is represented as g(st) ≥ h. 
A policy π : S → A maps a state to an action. The value of a policy is evaluated according to the discounted cumulative reward under the safety constraint. Let VM denote the value function in the MDP, M. In summary, we represent our problem as follows: 
maximize: V πM(st) = E 
[ ∞∑ τ=0 
γτr(st+τ ) 
∣∣∣∣∣ st ] 
subject to: g(st+τ ) ≥ h, ∀τ = [0,∞]. 
Difficulties. In conventional safety-constrained RL algorithms, the safety function is assumed to be known a priori. The key difference lies in the fact that we need to explore a safety function that is unknown a priori while guaranteeing satisfaction of the safety constraint. 
However, it is intractable to solve the above problem without further assumptions. First of all, without prior information on the state-and-action pairs known to be safe, an agent cannot take any viable action at the very beginning. Second, if the safety function does not exhibit any regularity, then the agent cannot infer the safety of decisions. 
Assumptions. To overcome the difficulties mentioned above, we adopt two assumptions from Sui et al. (2015) and Turchetta et al. (2016). For the first difficulty, we simply assume that the agent starts in an initial set of states, S0, that is known a priori to be safe. Second, we assume regularity for the safety function. Formally speaking, we assume that the state space S is endowed with a positive definite kernel function, kg, and that the safety function has a bounded norm in the associated reproducing kernel Hilbert space (RKHS, Schölkopf & Smola (2001)). The kernel function, kg is employed to capture the regularity of the safety function. Finally, we further assume that the safety function g is L-Lipschitz continuous with respect to some distance metric d(·, ·) on S. 
As with the safety function, we also assume that the reward function has a bounded norm in the associated RKHS, and that its regularity is captured by another positive definite kernel function, kr. 
The above assumptions allow us to characterize the reward and safety functions by using Gaussian processes (GPs, see Rasmussen (2004)). By using the GP models, the values of r and g at unobserved states are predicted according to
Safe Reinforcement Learning in Constrained Markov Decision Processes 
previously observed functions’ values. An advantage of leveraging GPs is that we can obtain both optimistic and pessimistic measurements of the two functions by using the inferred means and variances. A GP is specified by its mean, µ(s), and covariance, k(s, s′). The reward and safety functions are thus modeled as 
r(s) = GP(µr(s), kr(s, s′)), 
g(s) = GP(µg(s), kg(s, s′)). 
Without loss of generality, let µ(s) = 0 for all s ∈ S. For the reward and safety functions, we respectively model the observation noise as yr = r(s) + nr and yg = g(s) + ng, where nr ∼ N (0, σ2 
r) and ng ∼ N (0, σ2 g). The posteriors 
over r and g are computed on the basis of t observations at states {s1, . . . , st}. Then, for both the reward and safety functions, the posterior mean, variance, and covariance are respectively represented as 
µt(s) = k>t (s)(Kt + σ2I)−1yt, 
σt(s) = kt(s, s), 
kt(s, s ′) = k(s, s′)− k>t (s)(Kt + σ2I)−1kt(s 
′), 
where kt(s) = [k(s1, s), . . . , k(st, s)] >, and Kt is the 
positive definite kernel matrix. 
3. Background We define two kinds of predicted safe spaces inferred by a GP as in Turchetta et al. (2019). First, we consider a pessimistic safe space, which contains states identified as safe with a greater probability than a pre-defined confidence level. Second, we derive an optimistic safe space that includes all states that may be safe with even a small probability. 
Predicted pessimistic safe space. We use the notion of a safe space in Turchetta et al. (2016) as a predicted pessimistic safe space. For the probabilistic safety guarantee, two sets are defined. The first set, S−t , simply contains the states that satisfy the safety constraint with high probability. The second one, X−t , additionally considers the ability to reach states in S−t (i.e., reachability) and the ability to return to the previously identified safe set, X−t−1 (i.e., returnability). The algorithm probabilistically guarantees safety by allowing the agent to visit only states in X−t . 
Safety is evaluated in terms of the confidence interval inferred by the GP, which is represented as 
Qt(s) := [µgt−1(s)± β1/2 t σgt−1(s)], 
where βt ∈ R is a scaling factor for the required level of safety. We consider the intersection of Qt up to iteration t, which is defined as Ct(s) = Qt(s) ∩ Ct−1(s), where C0(s) = [h,∞] for all s ∈ S0. The lower and upper 
bounds on Ct(s) are denoted by lt(s) := minCt(s) and ut(s) := maxCt(s), respectively. 
The first set S−t contains states such that the safety constraint is satisfied with high probability. It is formulated using the lower bound of the safety function, l and the Lipshitz constant, L, as follows: 
S−t = {s ∈ S | ∃s′ ∈ X−t−1 : lt(s ′)− L · d(s, s′) ≥ h}. 
Next, the reachable and returnable sets are considered. Even though a state is in S−t , it might be surrounded by unsafe states. Given a set X , the states reachable from X in one step are given by Rreach(X) = X ∪ {s ∈ S | ∃s′ ∈ X, a ∈ A : s = f(s′, a)}. Even after arriving at a state with reachability, the agent may not be able to move to another state because of a lack of safe actions. Hence, before moving to a state s, we consider whether or not there is at least one viable path from s. The set of states from which the agent can return to a set X̄ through another set of states X in one step is given by Rret(X, X̄) = X̄ ∪ {s ∈ X | ∃a ∈ A : f(s, a) ∈ X̄}. Thus, an n-step returnability operator is given by Rnret(X, X̄) = Rret(X,R 
n−1 ret (X, X̄)),with R1 
ret(X, X̄) = Rret(X, X̄). Finally, the set containing all the states that can reach X̄ along an arbitrary long path in X is defined as R̄ret(X, X̄) = limn→∞Rnret(X, X̄). 
Finally, the desired pessimistic safe space, X−t is a subset of S−t and also satisfies the reachability and returnability constraints; that is, 
X−t = {s ∈ S−t | s ∈ Rreach(X−t−1) ∩ R̄ret(S − t ,X−t−1)}. 
Predicted optimistic safe space. As defined in Wachi et al. (2018) and Turchetta et al. (2019), an optimistic safe space has rich information for inferring the safety function. LetX+ 
t denote the predicted optimistic safe space. Similarly to X−t , the optimistic safe space, X+ 
t , is defined as 
X+ t = {s ∈ S+ 
t | s ∈ Rreach(X+ t−1) ∩ R̄ret(S 
+ t ,X+ 
t−1)}, 
where S+ t is the set of states that may satisfy the safety 
constraint, which is written as 
S+ t = {s ∈ S | ∃s′ ∈ X+ 
t−1 : ut(s ′)− L · d(s, s′) ≥ h}. 
Intuitively, X+ t contains all states that may turn out to be 
safe even if the probability is low. In other words, S \ X+ t 
contains states that are unsafe with high probability. 
Confidence interval. The correctness of X+ t and X−t de-
pends on the accuracy of the confidence interval inferred by the GP. The conservativeness can be tuned by using the parameter β, and the choice of this parameter was well-studied in Srinivas et al. (2010) and Chowdhury & Gopalan (2017).
Safe Reinforcement Learning in Constrained Markov Decision Processes 
In the rest of this paper, we set the parameter to 
βt = Bg + σg 
√ 2(Γgt−1 + 1 + log(1/∆g)), 
where Bg is a bound on the RKHS norm of g, ∆g is the allowed failure probability, and the observation noise is σg-sub-Gaussian. Also, Γg quantifies the effective degrees of freedom associated with the kernel function, which represents the maximal mutual information that can be obtained about the GP prior. 
Under the above definitions and assumptions, we have the following lemma regarding the correctness of the confidence intervals. 
Lemma 1. Assume that ‖g‖2k ≤ Bg and ngt ≤ σg, ∀t ≥ 1. 
If βt = Bg + σg 
√ 2(Γgt−1 + 1 + log(1/∆g)), then 
|g(s)− µgt−1(s)| ≤ β1/2 t σgt−1(s) 
holds for all t ≥ 1 with probability at least 1−∆g . 
The above paradigm for the safety function can also be applied to the reward function. Hence, we have a similar lemma for the reward function as well. 
Lemma 2. Assume that ‖r‖2k ≤ Br and nrt ≤ σr, ∀t ≥ 1. If αt = Br + σr 
√ 2(Γrt−1 + 1 + log(1/∆r)), then 
|r(s)− µrt−1(s)| ≤ α1/2 t σrt−1(s) 
holds for all t ≥ 1 with probability at least 1−∆r. 
These lemmas follow from Theorem 2 in Chowdhury & Gopalan (2017). 
Optimal solution. Here, we define the optimal policy in our problem setting. Under the optimal policy, π∗, the value function, VM, satisfies the following Bellman equation: 
V ∗M(st) = max st+1∈R̄εg (S0) 
[ r(st+1) + γV ∗M(st+1) ] , 
where R̄εg (S0) is the largest set that can be safely learned up to εg accuracy (for a formal definition, see Appendix A or Turchetta et al. (2016)). In our problem setting, in which the reward and safety functions are unknown a priori, the above Bellman equation cannot be solved directly. Our ultimate objective is to obtain a policy whose value is close to V∗M while guaranteeing satisfaction of the safety constraint. 
4. Algorithm We now introduce our proposed algorithm, SNO-MDP, for achieving a near-optimal policy with respect to the cumulative reward while guaranteeing safety. 
Algorithm 1 SNO-MDP with ES2 
Input: states S, actions A, transition function f , kernel kr for reward, kernel kg for safety, GP prior for reward, GP prior for safety, safety threshold h, discount factor γ, Lipschitz constant L, initial safe space S0. 1: C0(s)← [h,∞) for all s ∈ S0 
2: // Exploration of safety 3: loop 4: S−t ← {s ∈ S | ∃s′ ∈ X−t−1 : lt(s 
′)− L · d(s, s′) ≥ h} 5: S+ 
t ← {s ∈ S | ∃s′ ∈ X+ t−1 : ut(s 
′)−L · d(s, s′) ≥ h} 6: X−t ← {s ∈ S−t | s ∈ Rreach(X−t−1) ∩ R̄ret(S 
− t ,X−t−1)} 
7: X+ t ← {s ∈ S+ 
t | s ∈ Rreach(X+ t−1) ∩ R̄ret(S 
+ t ,X+ 
t−1)} 8: Gt ← {s ∈ X−t | et(s) > 0} 9: ξ ← arg maxs∈Gt wt(s) 
10: Update GPs for both reward and safety on way to ξ 11: t← t+ Tst−1→ξ and st ← ξ 
12: // ES2 algorithm 13: Yt ← {s′ ∈ S+ | ∀s ∈ X−t : s′ = f(s, π∗y(a | s))} 14: if Yt ⊆ X−t then break 15: // Typical termination condition 16: if maxs∈Gt wt(s) < εg then break 17: end loop 18: // Exploration and exploitation of reward 19: loop 20: Ut ← µrt + αt+1 · σrt 21: J∗Y(st)← maxst+1∈Yt 
[ Ut(st+1) + γJ∗Y(st+1) 
] 22: st+1 ← arg maxst+1∈Yt J 
∗ Y(st) 
23: end loop 
We first give an overview of SNO-MDP, which is outlined as Algorithm 1. We extend a stepwise approach in Sui et al. (2018) from state-less to stateful settings. Basically, our algorithm consists of two steps. In the first step, the agent expands the pessimistic safe region while guaranteeing safety (lines 2−17). Next, it explores and exploits the reward in the safe region certified in the first step (lines 18−23). The reason for this stepwise approach is that we can neglect uncertainty related to the a priori unknown safety function once the safe region is fixed. 
However, a pure stepwise approach does not stop exploring the safe region until the convergence of the GP confidence interval (lines 15−16). This formulation often requires the agent to execute a great number of actions for exploring safety. Hence, to achieve near-optimality while executing a smaller number of actions, we also propose the ES2 algorithm.2 This algorithm checks whether the current safe region is sufficient for achieving near-optimality (lines 12−14), which maintains the theoretical guarantee with respect to both the satisfaction of the safety constraint and the near-optimality of the cumulative reward. We further propose a practical ES2 algorithm, called P-ES2, with better empirical performance, although it does not provide a theoretical guarantee in terms of the near-optimality of the cumulative reward. 
2Both ES2 and P-ES2 do not affect the agent’s safety.
Safe Reinforcement Learning in Constrained Markov Decision Processes 
4.1. Exploration of Safety (Step 1) 
First, we consider how to explore the safety function. As a scheme to expand the safe region, we consider “expanders” as in Sui et al. (2015) and Turchetta et al. (2016). Expanders are states that may expand the predicted safe region, which is defined as Gt = {s ∈ X−t | et(s) > 0}, where et(s) = |s′ ∈ S \ S−t | ut(s)− Ld(s, s′) ≥ h|. 
The efficiency of expanding the safe region is measured by the width of the safety function’s confidence interval, defined as 
wt(s) = ut(s)− lt(s). 
The agent safely and efficiently expands the safe region by sampling the state with the maximum value of w among the expanders, Gt. Hence, the agent sets the temporal goal according to 
ξ = arg max s∈Gt 
wt(s). 
Then, within the predicted safe space X−t , it chooses a path to get to ξ from the current state st−1 so as to minimize the cost (e.g., the path length). In our experiment, we simply minimized the path length. By defining the cost as related to w (e.g., 1/w), however, the agent could explore safety more actively on the way to ξ. 
The previous work (Sui et al., 2015; Turchetta et al., 2016; Sui et al., 2018) terminated safety exploration when the desired accuracy was achieved for every state in Gt; that is, 
max s∈Gt 
wt(s) ≤ εg. (1) 
Unfortunately, this termination condition often requires a great number of iterations. For the purpose of maximizing the cumulative reward, it often leads to the loss of reward. Therefore, in Section 4.3, we propose the ES2 algorithm to improve this point. 
4.2. Exploration and Exploitation of Reward (Step 2) 
Once expansion of the safe region is completed, the agent guarantees safety as long as it is in X− and does not have to expand the safe region anymore. Hence, all we have to do is optimize the cumulative reward in X−. As such, a simple approach is to follow the optimism in the face of uncertainty principle as in Strehl & Littman (2008) and Auer & Ortner (2007), then to consider the “exploration bonus” represented by R-MAX (Brafman & Tennenholtz, 2002) and Bayesian Exploration Bonus (BEB, Kolter & Ng (2009)). 
Specifically, in accordance with Lemma 2, we optimize the policy by optimistically measuring the reward with the (probabilistic) upper confidence bound, 
Ut(s) := µrt (s) + α 1/2 t+1 · σrt (s). 
Optimistic safe space 
Pessimistic safe space 
Unsafe space 
Figure 1. Illustration of My , used in the ES2 algorithm. The yellow and blue regions represent X+ 
t and X−t , respectively. The red region (i.e., X \ X+ 
t ) is unsafe with high probability. 
In this reward setting, the second term on the right-hand side corresponds to the exploration bonus. For balancing the exploration and exploitation in terms of reward, we solve the following Bellman equation: 
J∗X (st, b r t , b 
g t ) = max 
st+1∈X− t∗ 
[ Ut(st+1) + γJ∗X (st+1, b 
r t , b 
g t ) ] , 
where br = (µr, σr) and bg = (µg, σg) are the beliefs over reward and safety, respectively. Also, t∗ is the time step when the termination condition (1) is satisfied. Note that br and bg are not updated; hence, we can solve the above equation with standard algorithms (e.g., value iteration). 
4.3. Early Stopping of Exploration of Safety (ES2) 
We have proposed a stepwise approach for exploring and optimizing the constrained MDP. In the first step when the safe region is expanded, however, the existing safe exploration algorithms (Sui et al., 2015; Turchetta et al., 2016; Sui et al., 2018) continue exploring the state space until convergence of the confidence interval, w, which generally leads to a large number of iterations. Our primary objective is to maximize the cumulative reward; hence, we should stop exploring safety if further exploration will not lead to maximizing the cumulative reward. 
While exploring the safety function, we check whether the step can be migrated. As such, we consider the following additional MDP, 
My = 〈X+,A, f, r′, g, γ〉. 
As shown in Figure 1, the differences from the original MDP, M, lie in the state space and the reward function. The state space of My is defined as the optimistic safe space (i.e., X+), while the reward function is defined as follows: 
r′ := 
{ µr + α1/2σr if s ∈ X+ 
t \ X−t , µr − α1/2σr if s ∈ X−t . 
(2) 
In the pessimistic safe space, the reward is defined as the lower bound; otherwise, it is defined as the upper bound. This definition of the reward function encourages the agent
Safe Reinforcement Learning in Constrained Markov Decision Processes 
to explore outside the predicted safe space, X−t . Using the new MDP above, we consider the set of states that the agent will visit at the next time step, defined as 
Yt = {s′ ∈ S+ | ∀s ∈ X−t : s′ = f(s, π∗y(a | s))}, 
where π∗y is the optimal policy forMy, obtained by maximizing the following value function: 
VMy (st) = max 
st+1∈X+ t 
[ r′(st+1) + γVMy (st+1) ]. (3) 
Finally, we stop exploring the safety function if the following equation holds: 
Yt ⊆ X−t . (4) 
Intuitively, we stop expanding the safe space if the direction of the optimal policy forMy heads for the inside of X−t . If the agent tries to stay in X−t even under the condition that the reward is defined as in (2), then we do not have to expand the safe region anymore. 
When the ES2 algorithm confirms satisfaction of the above condition, we move on to the next step and then optimize the cumulative reward in Yt; that is, 
J∗Y(st, b r t , b 
g t ) = max 
st+1∈Yt 
[ Ut(st+1) + γJ∗Y(st+1, b 
r t , b 
g t ) ] . 
4.4. More Practical ES2 Algorithm (P-ES2) 
As we will prove in Section 5, the ES2 algorithm provides us with a theoretical guarantee with respect to the cumulative reward. Unfortunately, this guarantee is achieved at the expense of empirical performance. The issue with the pure ES2 algorithm lies in the state constraint in (3); that is, the value function is calculated under the assumption that all the states in the optimistic safe space, X+, will be identified as safe. This assumption is necessary for the theoretical guarantee, but, in practice, it would be more reasonable to measure the probability of a state being identified as safe. Because the safety function is inferred as a Gaussian distribution for each state, an example of such a probability is a complementary error function; that is, we define the following probability, 
p(s, bg) = Pr [g(s) ≥ h | bg] ≈ 1− 1 
2 erfc 
( µg(s)− h√ 
2σg(s) 
) . 
Here, we introduce a new virtual state, z. Concretely, for z, the reward and transition probability are defined as r(z) = 0 and P (z | z, a, bg) = 1 for all a and bg, respectively. Hence, using z, we define a virtual transition probability P zx = Pr[x | st, at, bgt ] as follows: 
P zx := 
{ p(st+1, b 
g t ) if x = st+1, 
1− p(st+1, b g t ) if x = z. 
𝑠" 𝑠# 𝑠$ 
𝑝(𝑠#,𝑏)) 
𝑧 1.0 
𝑝(𝑠$,𝑏)) 
1 − 𝑝(𝑠#,𝑏)) 
State space 
1 − 𝑝(𝑠$,𝑏)) 
Figure 2. Illustration ofMz . This MDP is characterized by the virtual state z and the virtual transition probability P z . 
Hence, by introducing z and P z , we define the following MDP with the smooth, continuous transition probability: 
Mz = 〈X+ ∪ {z},A, P z, r′, g, γ〉. 
Figure 2 shows a conceptual image of this MDP. Intuitively, in Mz , the agent optimizes the policy under the virtual condition that a state-action pair may lead to the extremely undesirable state, z, with probability 1− p. Then, we solve the following equation instead of solving (3): 
VMz (st) = max 
st+1∈X+ t 
[P zst+1 · {r′(st+1) + γVMz 
(st+1)}]. 
For this equation, we used r(z) = 0 and V (z) = 0. For the optimal policy π∗z obtained by solving the above equation, we stop exploring the safety function if the following equation holds: 
Zt := {s′ ∈ S+ | ∀s ∈ X−t : s′ = f(s, π∗z(a |s))} ⊆ X−t . 
Then, we optimize the cumulative reward in Zt by solving the following equation: 
J∗Z(st, b r t , b 
g t ) = max 
st+1∈Zt 
[ Ut(st+1) + γJ∗Z(st+1, b 
r t , b 
g t ) ] . 
5. Theoretical Results We now provide theoretical guarantees on the safety and near-optimality of our proposed algorithm. Theorem 1 is associated with the safe expansion stage (i.e., step 1), which guarantees safety and convergence to the safe region. The-orem 2 ensures convergence toward the near-optimal cumulative reward. Theorem 3 ensures that SNO-MDP still achieves the near-optimal cumulative reward even when the ES2 algorithm is used. In the rest of this paper, let Vmax = Rmax/(1−γ). Also, letD :M→ R be a diameter of an MDP, defined as D(M) = minπ maxs1 6=s2 T 
π s1→s2 , 
where Tπs1→s2 is the expected number of time steps that policy π takes to move from s1 to s2. 
5.1. Safety Guarantee and Completeness 
We first present a theorem related to the safety guarantee and completeness.
Safe Reinforcement Learning in Constrained Markov Decision Processes 
Theorem 1. Assume that the safety function g satisfies ‖g‖2k ≤ Bg and is L-Lipschitz continuous. Also, assume that S0 6= ∅ and g(s) ≥ h for all s ∈ S0. Fix any εg > 0 and ∆g ∈ (0, 1). Suppose that we conduct the stage of “exploration of safety” with the noise ngt being σg-sub-Gaussian, and that βt = Bg + 
σg 
√ 2(Γgt−1 + 1 + log(1/∆g)) until maxs∈Gt wt(s) < εg 
is achieved. Finally, let t∗ be the smallest integer satisfying 
t∗ 
βt∗Γgt∗ ≥ Cg|R̄0(S0)| 
ε2g D(M), 
with Cg = 8/ log(1 + σ−2 g ). Then, the following statements 
jointly hold with probability at least 1−∆g: 
 ∀t ≥ 1, g(st) ≥ h, 
 ∃t0 ≤ t∗, R̄εg (S0) ⊆ X−t0 ⊆ R̄0(S0). 
A proof is presented in the supplemental material. Theo-rem 1 guarantees that SNO-MDP is safe in the stage of exploration of safety (i.e., step 1), as well as in the stage of optimization of reward (i.e., step 2), with high probability. In addition, after a sufficiently large number of time steps, X− is guaranteed to be a super-set of R̄εg (S0). 
5.2. Near-Optimality 
We next present a theorem on the near-optimality with respect to the cumulative reward. 
Theorem 2. Assume that the reward function r satisfies ‖r‖2k ≤ Br, and that the noise is σr-sub-Gaussian. Let πt denote the policy followed by SNO-MDP at time t, and let st and brt , b 
g t be the corresponding state and be-
liefs, respectively. Let t∗ be the smallest integer satisfying t∗ 
βt∗Γg t∗ ≥ Cg|R̄0(S0)| 
ε2g D(M), and fix any ∆r ∈ (0, 1). Fi-
nally, set αt = Br + σr √ 
2(Γrt−1 + 1 + log(1/∆r)) and 
ε∗V = Vmax · (∆g + Σrt∗/Rmax), 
with Σrt∗ = 1 2 
√ Crαt∗Γr 
t∗ t∗ . Then, with high probability, 
V πt(st, b r t , b 
g t ) ≥ V ∗(st)− ε∗V 
— i.e., the algorithm is ε∗V -close to the optimal policy — for all but t∗ time steps, while guaranteeing safety with probability at least 1−∆g . 
A detailed proof of Theorem 2 is presented in the supplemental material. The proof is based on the following idea. After the agent fully explores the safe space, X− satisfies R̄εg (S0) ≤ X− ≤ R̄0(S0), and states in X− are safe with high probability. Once X− converges, the probability of leaving the “known” safe space is small; hence, Theorem 2 
follows by adapting standard arguments from previous PAC-MDP results. The key condition that allows us to prove the near-optimality of SNO-MDP is that, at every time step, the agent is optimistic with respect to the reward, and this optimism decays given a sufficient number of samples. By optimizing the cumulative reward in X− according to the optimism in the face of uncertainty principle, the acquired policy is ε∗V -close to the optimal policy in the original safetyconstrained MDP. 
Finally, we present a theoretical result related to the ES2 
algorithm. Specifically, we prove that ES2 maintains the near-optimality of SNO-MDP. 
Theorem 3. Assume that the reward function r satisfies ‖r‖2k ≤ Br, and that the noise is σr-sub-Gaussian. Let πt denote the policy followed by SNO-MDP with the ES2 algorithm at time t, and let st and brt , b 
g t be the corresponding 
state and beliefs, respectively. Let t̃ be the smallest integer for which (4) holds, and fix any ∆r ∈ (0, 1). Finally, set αt = Br + σr 
√ 2(Γrt−1 + 1 + log(1/∆r)) and 
ε̃V = Vmax · (∆g + Σrt̃/Rmax), 
with Σr t̃ 
= 1 2 
√ Crαt̃Γ 
r t̃ 
t̃ . Then, with high probability, 
V πt(st, b r t , b 
g t ) ≥ V ∗(st)− ε̃V 
— i.e., the algorithm is ε̃V -close to the optimal policy — for all but t̃ time steps while guaranteeing safety with probability at least 1−∆g . 
The proof of Theorem 3 is presented in the supplemental material. The proof is based on the following idea. When the condition in (4) is satisfied, the agent will not leave Y , and a near-optimal policy is obtained by optimizing the cumulative reward only in Y with the optimistically measured reward. Also, as long as the agent is in Y (⊆ X−), safety is guaranteed with high probability. The proof is similar to that for Theorem 2. 
6. Experiment In this section, we evaluate the performance of SNO-MDP through two experiments. One used a synthetic environment, while the other simulated Mars surface exploration. We also show the effectiveness of our ES2 and P-ES2 algorithms. 
6.1. Synthetic GP-SAFETY-GYM Environment 
Settings. We constructed a new open-source environment for safe RL simulations named GP-SAFETY-GYM. This environment was built based on OpenAI Safety-Gym (Ray et al., 2019). As shown in Figure 3(a), GP-SAFETY-GYM represents the reward by a color (yellow: high; green: medium; blue: low), and the safety by height.
Safe Reinforcement Learning in Constrained Markov Decision Processes 
(a) GP-SAFETY-GYM. (b) Performance comparison. (c) Effects of ES2 and P-ES2. 
Figure 3. Experiment with synthetic data. (a) Example screen capture from the GP-SAFETY-GYM environment. (b) Average reward over the episodes, comparing the performance of SNO-MDP with ES2 and the baselines. (c) Average reward over the episodes, showing the effects of ES2 and P-ES2. The colored circles represent when the transition from safe exploration to reward optimization happens for each method. In both (b) and (c), the reward is normalized with respect to the SAFE/REWARD KNOWN case. 
We considered a 20 × 20 square grid in which the reward and safety functions were randomly generated. At every time step, an agent chose an action from stay, up, right, down, and left. The agent predicted the reward and safety functions by using different kernels on the basis of previous observations. In this simulation, we allowed the agent to observe the reward and safety function values of the current state and neighboring states. The kernel for reward was a radial basis function (RBF) with the length-scales of 2 and prior variance of 1. The kernel for safety was also an RBF with the length-scales of 2 and prior variance of 1. Finally, we set the discount factor to γ = 0.99, and confidence intervals parameters to αt = 3 and βt = 2 for all t ≥ 1. 
Baselines. We empirically compared the performance of our SNO-MDP with SAFEMDP (Turchetta et al., 2016) and SAFEEXPOPT-MDP (Wachi et al., 2018), as well as a case called SAFE/REWARD KNOWN. In SAFEMDP, the agent tries to expand the safe region without considering the reward. In SAFEEXPOPT-MDP, the agent attempts to maximize the cumulative reward while leveraging the difference between the value function in X+ 
t and that in X−t . Finally, SAFE/REWARD KNOWN is a non-exploratory case in which the safety and reward functions are known a priori. 
Metrics. We used the cumulative reward and the number of unsafe actions as comparison metrics. 
Results. Figure 3(b) compares the performance of SNO-MDP and the baselines in terms of the reward. For these results, the average reward was measured over the previous 50 time steps. SNO-MDP achieved the optimal reward after shifting to the stage of reward optimization, which outperforms SAFEMDP and SAFEEXPOPT-MDP in terms of the reward after a sufficiently large number of time steps. The SAFEMDP agent did not aim to maximize the cumulative reward, and the SAFEEXPOPT-MDP agent was sometimes 
stucked in a local optimum when the expansion of the safe region was insufficient. Figure 3(c) shows the empirical performance of the ES2 and P-ES2 algorithms. P-ES2 
achieved faster convergence in terms of the reward than the original ES2 did. Also, all methods, including the baselines, did not take any unsafe actions. 
6.2. Simulated Mars Surface Exploration 
Settings. We then conducted an experiment based on a Mars surface exploration scenario, as in Turchetta et al. (2016) and Wachi et al. (2018). In this simulation, we used a publicly available Mars digital elevation model (DEM) that was created from observation data captured by the highresolution imaging science experiment (HiRISE) camera (McEwen et al., 2007). 
0 10 20 30 x 
0 
5 
10 
15 
20 
25 
y 
−10.0 
−7.5 
−5.0 
−2.5 
0.0 
2.5 
5.0 
7.5 
10.0 
Figure 4. Mars terrain data. 
We created a 40 × 30 rectangular grid-world by clipping a region around latitude 30◦6’ south and longitude 202◦2’ east, as shown in Figure 4. At every time step, the rover took one of five actions: stay, up, down, left, and right. We assumed that any state in which the slope angle was greater than 25◦ were unsafe. The safety function g was defined as the slope angle calculated from the DEM, and the safety threshold was h = − tan(25◦). 
The rover predicted the elevation by using a GP with a Matérn kernel with ν = 5/2. The length-scales were 15 m, and the prior variance over elevation was 100 m2. We assumed a noise standard deviation of 0.075 m. For the reward, we randomly defined a smooth, continuous reward. To predict the reward function, the rover used a GP with RBF kernel having length-scales of 2 and a prior variance
Safe Reinforcement Learning in Constrained Markov Decision Processes 
Table 1. Experimental results with real Mars data. 
REWARD UNSAFE ACTIONS 
SNO-MDP W/ P-ES2 0.81 0 SNO-MDP W/ ES2 0.78 0 SNO-MDP 0.49 0 SAFEMDP 0.34 0 SAFEEXPOPT-MDP 0.59 0 SAFE/REWARD KNOWN 1.00 0 
over the reward of 2. We set the confidence levels as αt = 3 and βt = 2,∀t ≥ 0, and the discount factor as γ = 0.9. 
Baselines and metrics. We used the same baselines and metrics as in the previous synthetic experiment. 
Results. Table 1 summarizes the results. The reward was accumulated over the episode, which was normalized with respect to the SAFE/REWARD KNOWN case. Our SNO-MDP with either P-ES2 or ES2 outperformed SAFEMDP and SAFEEXPOPT-MDP in terms of the reward. This was expected, because SafeMDP does not aim to maximize the cumulative reward, and SAFEEXPOPT-MDP does not guarantee the near-optimality of the cumulative reward. Also, no unsafe action was executed by any of the tested algorithms. 
7. Conclusion We have proposed SNO-MDP, a stepwise approach for exploring and optimizing a safety-constrained MDP. The-oretically, we proved a bound of the sample complexity to achieve εV -closeness to the optimal policy while guaranteeing safety, with high probability. We also proposed the ES2 
and P-ES2 algorithms for improving the efficiency in obtaining rewards. We developed an open-source environment, GP-SAFETY-GYM, to test the effectiveness of SNO-MDP . We also demonstrated the advantages of SNO-MDP using the real Mars terrain data. 
Acknowledgement This work is sponsored by IBM Research AI and Toyota-Tsinghua joint project on health challenges for future city and smart health system design (20203910025). 
References Achiam, J., Held, D., Tamar, A., and Abbeel, P. Constrained 
policy optimization. In International Conference on Ma-chine Learning (ICML), 2017. 
Araya, M., Buffet, O., and Thomas, V. Near-optimal BRL 
using optimistic local transitions. In International Con-ference on Machine Learning (ICML), 2012. 
Aswani, A., Gonzalez, H., Sastry, S. S., and Tomlin, C. Provably safe and robust learning-based model predictive control. Automatica, 49(5):1216–1226, 2013. 
Auer, P. and Ortner, R. Logarithmic online regret bounds for undiscounted reinforcement learning. In Neural Infor-mation Processing Systems (NeurIPS), 2007. 
Berkenkamp, F., Turchetta, M., Schoellig, A., and Krause, A. Safe model-based reinforcement learning with stability guarantees. In Neural Information Processing Systems (NeurIPS), 2017. 
Brafman, R. I. and Tennenholtz, M. R-max - a general polynomial time algorithm for near-optimal reinforcement learning. Journal of Machine Learning Research (JMLR), pp. 213–231, 2002. 
Chow, Y., Nachum, O., Faust, A., Duenez-Guzman, E., and Ghavamzadeh, M. Lyapunov-based safe policy optimization for continuous control. arXiv preprint arXiv:1901.10031, 2019. 
Chowdhury, S. R. and Gopalan, A. On kernelized multiarmed bandits. In International Conference on Machine Learning (ICML), 2017. 
Fisac, J. F., Akametalu, A. K., Zeilinger, M. N., Kaynama, S., Gillula, J., and Tomlin, C. J. A general safety framework for learning-based control in uncertain robotic systems. IEEE Transactions on Automatic Control, 2018. 
Garcıa, J. and Fernández, F. A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research (JMLR), 16(1):1437–1480, 2015. 
Kearns, M. and Singh, S. Near-optimal reinforcement learning in polynomial time. Machine Learning, 49(2-3):209– 232, 2002. 
Kolter, J. Z. and Ng, A. Y. Near-Bayesian exploration in polynomial time. In International Conference on Ma-chine Learning (ICML), 2009. 
Mayne, D. Q., Rawlings, J. B., Rao, C. V., and Scokaert, P. O. Constrained model predictive control: Stability and optimality. Automatica, 36(6):789–814, 2000. 
McEwen, A. S., Eliason, E. M., Bergstrom, J. W., et al. Mars reconnaissance orbiter’s high resolution imaging science experiment (HiRISE). Journal of Geophysical Research: Planets, 112(E5), 2007. 
Rasmussen, C. E. Gaussian processes in machine learning. In Advanced Lectures on Machine Learning, pp. 63–71. Springer, 2004.
Safe Reinforcement Learning in Constrained Markov Decision Processes 
Ray, A., Achiam, J., and Amodei, D. Benchmarking safe exploration in deep reinforcement learning. 2019. 
Schölkopf, B. and Smola, A. J. Learning with kernels: support vector machines, regularization, optimization, and beyond. MIT press, 2001. 
Srinivas, N., Krause, A., Kakade, S. M., and Seeger, M. Gaussian process optimization in the bandit setting: No regret and experimental design. In International Confer-ence on Machine Learning (ICML), 2010. 
Strehl, A. L. and Littman, M. L. An analysis of model-based interval estimation for Markov decision processes. Journal of Computer and System Sciences, 74(8):1309– 1331, 2008. 
Strehl, A. L., Li, L., Wiewiora, E., Langford, J., and Littman, M. L. PAC model-free reinforcement learning. In Inter-national Conference on Machine Learning (ICML), 2006. 
Sui, Y., Gotovos, A., Burdick, J. W., and Krause, A. Safe exploration for optimization with Gaussian processes. In International Conference on Machine Learning (ICML), 2015. 
Sui, Y., Zhuang, V., Burdick, J. W., and Yue, Y. Stagewise safe Bayesian optimization with Gaussian processes. In International Conference on Machine Learning (ICML), 2018. 
Turchetta, M., Berkenkamp, F., and Krause, A. Safe exploration in finite Markov decision processes with Gaussian processes. In Neural Information Processing Systems (NeurIPS), 2016. 
Turchetta, M., Berkenkamp, F., and Krause, A. Safe exploration for interactive machine learning. In Neural Information Processing Systems (NeurIPS), 2019. 
Wachi, A., Sui, Y., Yue, Y., and Ono, M. Safe exploration and optimization of constrained MDPs using Gaussian processes. In AAAI Conference on Artificial Intelligence (AAAI), 2018.