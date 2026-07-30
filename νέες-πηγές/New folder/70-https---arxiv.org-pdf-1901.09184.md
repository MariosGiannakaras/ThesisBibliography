> Source: https://arxiv.org/pdf/1901.09184

Action Robust Reinforcement Learning and Applications in Continuous Control 
Chen Tessler * 1 Yonathan Efroni * 1 Shie Mannor 1 
Abstract 
A policy is said to be robust if it maximizes the reward while considering a bad, or even adversarial, model. In this work we formalize two new criteria of robustness to action uncertainty. Specifically, we consider two scenarios in which the agent attempts to perform an action a, and (i) with probability α, an alternative adversarial action ā is taken, or (ii) an adversary adds a perturbation to the selected action in the case of continuous action space. We show that our criteria are related to common forms of uncertainty in robotics domains, such as the occurrence of abrupt forces, and suggest algorithms in the tabular case. Building on the suggested algorithms, we generalize our approach to deep reinforcement learning (DRL) and provide extensive experiments in the various Mu-JoCo domains. Our experiments show that not only does our approach produce robust policies, but it also improves the performance in the absence of perturbations. This generalization indicates that action-robustness can be thought of as implicit regularization in RL problems. 
1. Introduction Recent advances in Reinforcement Learning (RL) have demonstrated its potential in real-world deployment. How-ever, since in RL it is normally assumed that the train and test domains are identical, it is not clear how a learned policy would generalize under small perturbations. For example, consider the task of robotic manipulation in which the task is to navigate towards a goal. As the policy is trained on a specific parameter set (mass, friction, etc...), it is not clear what would happen when these parameters change, e.g., if the robot is slightly lighter/heavier. 
*Equal contribution 1Department of Electrical Engineering, Technion Institute of Technology, Haifa, Israel. Correspondence to: Chen Tessler <chen.tessler@campus.technion.ac.il>, Yonathan Efroni <jonathan.e@campus.technion.ac.il>. 
Proceedings of the 36 th International Conference on Machine Learning, Long Beach, California, PMLR 97, 2019. Copyright 2019 by the author(s). 
The advantage of robust policies is highlighted when considering imperfect models, a common scenario in real world tasks such as autonomous vehicles. Even if the model is trained in the real world, certain variables such as traction, tire pressure, humidity, vehicle mass and road conditions may vary over time. These changes affect the dynamics of our model, a property which should be considered during the optimization process. Robust MDPs (Nilim & El Ghaoui, 2005; Iyengar, 2005; Wiesemann et al., 2013) tackle this issue by solving a max-min optimization problem over a set of possible model parameters, an uncertainty set, e.g., the range of values which the vehicle’s mass may take - the goal is thus to maximize the reward, with respect to (w.r.t.) the worst possible outcome. 
Previously, Robust MDPs have been analyzed extensively in the theoretical community, in the tabular case (Nilim & El Ghaoui, 2005; Iyengar, 2005; Xu & Mannor, 2007; Man-nor et al., 2012; Wiesemann et al., 2013) and under linear function approximation (Tamar et al., 2013). However, as these works analyze uncertainty in the transition probabilities: (i) it is not clear how to obtain these uncertainty sets, and (ii) it is not clear if and how these approaches may be extended to non-linear function approximation schemes, e.g., neural networks. Recently, this problem has been tackled, empirically, by the Deep RL community (Pinto et al., 2017; Peng et al., 2018). While these approaches seem to work well in practice, they require access and control of a simulator and are not backed by theoretical guarantees - a well known problem in adversarial training (Barnett, 2018). 
Our approach tackles these problems by introducing a natural way to define robustness - robustness w.r.t. action perturbations - a scenario in which the agent attempts to perform an action and due to disturbances, such as noise or model uncertainty, acts differently than expected. In this work, we consider two distinct robustness criteria: given an action provided by the policy (i) the Probabilistic Action Robust MDP (PR-MDP, Section 3) criterion considers the case in which, with probability α, a different possibly adversarial action is taken; and (ii) the Noisy Action Robust MDP (NR-MDP, Section 4) criterion, in which a perturbation is added to the action itself. These two criteria are strongly correlated to real world uncertainty; the former correlates to abrupt interruptions such as a sudden push and the latter correlates to a constant interrupting force. For instance, if the 
 
 
 
 
 
 
 
 
 
 
Action Robust Reinforcement Learning and Applications in Continuous Control 
robot is heavier, this may be seen as an adversary applying force in the opposite direction (Başar & Bernhard, 2008). 
In Section 6, we extend our approach to Deep RL, perform extensive evaluation across several MuJoCo (Todorov et al., 2012) environments and show the ability of our approach to produce robust policies. We empirically analyze the differences between the PR-MDP and NR-MDP approaches, and demonstrate their ability to produce robust policies under abrupt perturbations and mass uncertainty. Surprisingly, we observe that even in the absence of perturbations, solving for the action robust criteria results in improved performance1. 
2. Preliminaries 2.1. Markov Decision Process 
We consider the framework of infinite-horizon discounted Markov Decision Process (MDP) with continuous action space. An MDP is defined as the 5-tuple (S,A, P,R, γ) (Puterman, 1994), where S is a finite state space, A is a compact and convex action metric space. We assume P ≡ P (s′ | s,a) is a transition kernel and is weakly continuous in a, R ≡ r(s,a) is a reward function continuous in a, and γ ∈ (0, 1). Let π : S → P(A) be a stationary policy, where P(A) is the set of probability measures on the Borel sets of A. We denote Π as the set of stationary deterministic policies on A, i.e., if π ∈ Π then π : S → A, and P(Π) as the set of stationary stochastic policies. Let vπ ∈ R|S| be the value of a policy π, defined in state s as vπ(s) ≡ Eπ[ 
∑∞ t=0 γ 
tr(st,at) | s0 = s], where at ∼ π(st) is a random-variable, Eπ denotes expectation w.r.t. the distribution induced by π and conditioned on the event {s0 = s}. 
The goal is to find a policy π∗, yielding the optimal value v∗, i.e., for all s ∈ S, π∗(s) ∈ arg maxπ′∈P(Π) Eπ 
′ [ ∑∞ t=0 γ 
tr(st,at) | s0 = s], 
and the optimal value is v∗(s) = vπ ∗ (s). It is known, and 
quite surprising, that there always exists an optimal policy which is stationary and deterministic, meaning π∗ ∈ Π, e.g., (Puterman, 1994)[Theorem 6.2.10]. 
We note that in all following results we assume continuity of the dynamics and reward in actions. For the exact definitions see Appendix A.1 , Assumption 1. 
2.2. Zero-Sum Games 
As opposed to the standard MDP framework, in a two player zero-sum game, the reward function and transition kernels are functions of both players a ∈ A and ā ∈ Ā, where A, Ā are compact sets. Assuming the policy of player 1 is π and π̄ of player 2, the value of the game is defined ∀s ∈ S, vπ,π̄(s) ≡ Eπ,π̄[ 
∑∞ t=0 γ 
tr(st, at, āt) | s0 = s]. Maitra & Parthasarathy (1970) generalized result of Shapley 
1Our code can be found in the following repository: https://github.com/tesslerc/ActionRobustRL 
(1953) and established that, under proper conditions, the zero sum game has value for any s ∈ S, i.e., 
v∗(s) = max π∈P(Π) 
min π̄∈Π 
Eπ,π̄[ 
∞∑ t=0 
γtr(st, at, āt) | s0 = s], 
= min π̄∈P(Π) 
max π∈Π 
Eπ,π̄[ 
∞∑ t=0 
γtr(st, at, āt) | s0 = s]. 
Note that, in the general case, the optimal maximizing policy is selected from the set of stochastic policies. Policies which attain this value, π∗ and π̄∗ for the maximizer and minimizer players, respectively, are said to be in Nash-Equilibrium. In such a scenario, neither player may improve it’s outcome further, e.g., ∀π, π̄ ∈ P(Π), vπ,π̄ 
∗ ≤ v∗ ≤ vπ∗,π̄. 
3. Probabilistic Action Robust MDP In this section we introduce the Probabilistic Action Robust MDP (PR-MDP), which can be viewed as a zero-sum game between an agent and an adversary. We refer to the optimal policy of the max-agent in PR-MDP as the optimal probabilistic robust policy. Furthermore, we establish that the game has a well defined value and analyze some properties of this criterion. Lastly, we formulate Policy Iteration (PI) schemes that solve the PR-MDP, and show that they inherit properties corresponding to single agent PI schemes. Definition 1. Let α ∈ [0, 1]. A Probabilistic Action Robust MDP is defined by the 5-tuple of an MDP (see Section 2.1). Let π, π̄ be policies of an agent an adversary. We define their probabilistic joint policy πmix 
P,α(π, π̄) as ∀s ∈ S, πmix P,α(a | 
s) ≡ (1− α)π(a | s) + απ̄(a | s). 
Let π be an agent policy. As opposed to standard MDPs, the value of the policy is defined by vπP,α = minπ̄∈Π Eπ 
mix P,α(π,π̄)[ 
∑ t γ 
tr(st,at)], where at ∼ πmix 
P,α(π(st), π̄(st)). The optimal probabilistic robust policy is the optimal policy of the PR-MDP 
π∗P,α ∈ arg max π∈P(Π) 
min π̄∈Π 
Eπ mix P,α(π,π̄)[ 
∑ t 
γtr(st,at)]. (1) 
The optimal probabilistic robust value is v∗P,α = v π∗P,α P,α . 
Simply put, an optimal probabilistic robust policy is optimal w.r.t. a scenario in which, with probability α, an adversary takes control and performs the worst possible action. This approach formalizes a possible inability to control the system and to perform the wanted actions. 
In-order to obtain the optimal probabilistic robust policy, one needs to solve the zero-sum game as defined in (1) (see Appendix B.1 for a formal mapping). It is well known (Straffin, 1993) that any zero-sum game has a well defined value on the set of stochastic policies, but not always on the set of deterministic policies. Interestingly, and similarly to regular MDPs, the optimal policy of the PR-MDP is a
Action Robust Reinforcement Learning and Applications in Continuous Control 
deterministic one as the following proposition asserts (see proof in Appendix B.2). Proposition 1. For PR-MDP, there exists an optimal policy which is stationary and deterministic, and strong duality holds in Π, 
v∗P,α = max π∈Π 
min π̄∈Π 
Eπ mix P,α(π,π̄)[ 
∑ t 
γtr(st,at)] 
= min π̄∈Π 
max π∈Π 
Eπ mix P,α(π,π̄)[ 
∑ t 
γtr(st,at)]. 
3.1. Probabilistic Action Robust and Robust MDPs 
Although the approach of PR-MDP might seem orthogonal to the that of Robust MDPs, the former is a specific case of the latter. By using the PR-MDP criterion, a class of models is implicitly defined, and the probabilistic robust policy is optimal w.r.t. the worst possible model in this class. 
To see the equivalence, define the following class of models, 
Pα = {(1− α)P + αPπ : P(Π)} Rα = {(1− α)r + αrπ : π ∈ P(Π)}. 
A probabilistic robust policy, which solves (1), is also the solution to the following RMDP (see Appendix B.3), 
π∗P,α ∈ arg max π′∈Π 
min P∈Pα,r∈Rα 
Eπ ′ 
P [ ∑ t 
γtr(st,at)], 
where EπP is the expectation of policy π when the dynamics are given by P . This relation explicitly shows that π∗P,α is also optimal w.r.t. the worst model in the class Pα,Rα, which is convex and rectangular uncertainty set (Epstein & Schneider, 2003), and formalizes the fact that PR-MDP is a specific instance of RMDP. 
3.2. Policy Iteration Schemes for PR-MDP 
In this section, we analyze Policy Iteration (PI) schemes that solve (1). Although a Value-Iteration procedure can be easily derived, we focus on the possible PI schemes. PI schemes are central to the currently used actor-critic approaches in continuous control, which we focus on in our experiments. We present two algorithms, Probabilistic Robust PI (Algorithm 1) and Soft Probabilistic Robust PI (Algorithm 2), and discuss the relation between the two. 
The Probabilistic Robust PI (PR-PI, Algorithm 1) is a two player PI scheme adjusted to solving a PR-MDP (e.g., Rao et al. (1973); Hansen et al. (2013)). PR-PI repeats two stages, (i) given a fixed adversary strategy, it calculates the optimal counter strategy, and (ii) it solves the 1-step greedy policy w.r.t. the value of the agent and adversary mixture policy. As suggested in Shani et al. (2018), Section 3.1, stage (i) may be performed by any MDP solver. 
The Soft Probabilistic Robust PI (Soft PR-PI, Algorithm 2) is updated using gradient information, unlike the PR-PI. In-stead of updating the adversary policy using a 1-step greedy 
update, the adversary policy is updated using a Frank-Wolfe update (Frank & Wolfe, 1956). The Franke-Wolfe update, similar to the gradient-projection method, finds a policy which is within the set of feasible policies; as, for instance, the gradient may produce policies out of the simplex. It works by finding the valid policy with the highest correlation, i.e., inner product, with the direction of gradient descent and performs a step towards it. As a convex mixture of two policies is a valid policy, the new policy is ensured to be a valid one. 
Although the two algorithms might seem disparate, Soft PR-PI merely generalizes the ‘hard’ updates of PR-PI to ‘soft’ ones. This statement is formalized in the following proposition, which is a direct consequence of Theorem 1 in Scherrer & Geist (2014), see proof in Appendix B.4. 
Proposition 2. Let π, π̄ be general policies. Then, 
arg min π̄′∈Π 
rπ̄ ′ + γP π̄ 
′ vπ 
mix P,α(π,π̄) 
= arg min π̄′∈Π 
〈 π̄′,∇π̄vπ 
mix P,α(π,π̃) |π̃=π̄ 
〉 . 
Notice that the first single agent, 1-step improvement, has a solution in the set of deterministic policies (since the action space is a compact set and the argument is continuous in the action). Thus, π̄ in Algorithm 2 is exactly the 1-step greedy policy used in Algorithm 1. This suggests that for η = 1 Algorithm 2 is completely equivalent to Algorithm 1. 
Generally, in two-player PI, the improvement stage amounts to solving a max-min, 1-step, decision problem. In PR-PI it is clearly not the case; in the improvement stage, a single agent, 1-step-greedy policy, is solved. Solving the latter is easier than solving the former, and it is a result of the specific structure of PR-MDP which does not generally hold, as will be demonstrated in Section 4. 
The following result shows that in both algorithms the value converges to the unique optimal value of the Nash-Equilibrium (see proof in Appendix B.5). 
Theorem 3. Denote by vk def = vπ 
mix P,α(πk,π̄k). Then, for any 
η ∈ (0, 1], in Algorithm 2, vk contracts toward v∗P,α with coefficient (1− η + γη), i.e., 
||vk − v∗P,α||∞ ≤ (1− η + γη)||vk−1 − v∗P,α||∞ . 
Due to the equivalence of Algorithms 1 and 2 (when η = 1), we get as a corollary that PR-PI converges toward the unique Nash-Equilibrium. 
Remark 1. The solution method of the arg max and arg min in both Algorithms 1 and 2 can be swapped and the convergence guarantees remain, e.g., π̄ is the optimal solution to the MDP given π, whereas π is updated using the 1-step greedy approach w.r.t. π̄.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Algorithm 1 Probabilistic Robust PI Initialize: α, π̄0, k = 0 while not changing do πk ∈ arg maxπ′ v 
πmix P,α(π′,π̄k) 
π̄k+1 ∈ arg minπ̄ r π̄ + γP π̄vπ 
mix P,α(πk,π̄k) 
k ← k + 1 end while Return πk−1 
Algorithm 2 Soft Probabilistic Robust PI Initialize: α, η, π̄0, k = 0 while criterion is not satisfied do πk ∈ arg maxπ′ v 
πmix P,α(π′,π̄k) 
π̄ ∈ arg minπ̄′ 〈 π̄′,∇π̄vπ 
mix P,α(πk,π̄) |π̄=π̄k 
〉 π̄k+1 = (1− η)π̄k + ηπ̄ k ← k + 1 
end while Return πk−1 
Remark 2. Although Soft PR-PI converges slower than the non-soft version, it is reasonable to assume the former will be less sensitive to errors than the latter. Soft PR-PI can be seen as a generalization of Conservative PI (CPI) to solving PR-MDPs. CPI is known to be less sensitive to errors than other PI schemes (Scherrer & Geist, 2014). Nonetheless, the error analysis for Soft PR-PI is substantially different than the one CPI (Kakade & Langford, 2002; Scherrer, 2014). In Soft PR-PI, small changes in the adversarial policy may result in dramatic changes in the agent’s policy. Thus, the γ-weighted state occupancy under a mea-
sure ν, d πmix P,α(πk,π̄k) ν = 
∑ t γ 
tνPπ mix P,α(πk,π̄k), may change 
dramatically between iterations, whereas in CPI the change is smooth. We leave the error analysis for future work. 
4. Noisy Action Robust MDP In this section we consider an alternative definition for action robustness. Instead of a stochastic perturbation in the policy space, as in Section 3, we consider a perturbation in the action space. To formally study such a perturbation we define the Noisy Action Robust MDP (NR-MDP), which, similarly to the PR-MDP, can be viewed as a zero-sum game (see Appendix C.1 for a formal mapping). We continue by establishing some properties of this MDP while highlighting important differences relative to the approach of PR-MDP. Definition 2. Let α ∈ [0, 1]. A Noisy Action Robust MDP is defined by the 5-tuple of an MDP (see Section 2.1). Let π, π̄ be policies of an agent and an adversary. We define their noisy joint policy πmix 
N,α(π, π̄) as 
∀s ∈ S,a ∈ A, πmix N,α(a | s) ≡ Eb∼π(·|s) 
b̄∼π̄(·|s) [1a=(1−α)b+αb̄], 
the relation is obtained by the fact that a ∼ π, ā ∼ π̄. 
Let π be an agent policy. For NR-MDP, its value is defined by vπN,α = minπ̄∈Π Eπ 
mix N,α(π,π̄)[ 
∑ t γ 
tr(st,at)], 
where at ∼ πmix N,α(π(st), π̄(st)). The optimal α-noisy ro-
bust policy is the optimal policy of the NR-MDP 
π∗N,α ∈ arg max π∈P(Π) 
min π̄∈Π 
Eπ mix N,α(π,π̄)[ 
∑ t 
γtr(st,at)]. (2) 
The optimal noisy robust value is v∗N,α = v π∗N,α N,α . 
In simple terms; an optimal noisy robust policy is optimal w.r.t. a scenario, in which an adversary may change the agent’s actions by adding bounded perturbations; the action performed on the system is (1 − α)a+αā, where ā is an action drawn from possibly adverserial distribution π̄. The adversary’s ability to add perturbations is controlled through the parameter α. Each value of α defines a new continuousaction NR-MDP, where for α = 0 the adversary is unable to affect the system and the decision problem collapses to the standard, non-robust, MDP formulation. 
The assumption on the structure of A is required, in order to ensure that the α-mixture actions are valid actions, an assumption which holds naturally in the domain of continuous control. This approach formalizes a specific meaning for perturbation in the action space. 
Although the approach of PR-MDP (Section 3) and NR-MDP are closely related, they are not equivalent and important differences exist between the two. Unlike PR-MDP, for which a deterministic stationary optimal policy exists, generally, for NR-MDP it is not the case. The optimal noisy robust policy, in the general case, is a stochastic policy (see proof in Appendix C.2). 
Proposition 4. There exists an NR-MDP such that, 
max π∈Π 
min π̄∈Π 
Eπ mix N,α(π,π̄)[ 
∑ t 
γtr(st,at)] 
< max π∈P(Π) 
min π̄∈Π 
Eπ mix N,α(π,π̄)[ 
∑ t 
γtr(st,at))]. 
Furthermore, strong duality does not necessarily hold on the class of deterministic policies, Π. 
The above proposition tells us that while it is often easier to focus on deterministic strategies (policies), when considering the NR-MDP scenario the optimal strategy may be stochastic. A similar notion has been shown to hold in non-cooperative matrix games (Nash, 1951), in which the optimal strategy is stochastic.
Action Robust Reinforcement Learning and Applications in Continuous Control 
4.1. Policy Iteration for NR-MDPs 
In section 3.2, we formulated PI schemes to solve PR-MDPs. Unlike two-player zero-sum PI (Rao et al., 1973; Hansen et al., 2013), in PR-PI (Algorithm 1) a single agent decision problem is solved, when the adversary policy π̄k+1 is updated. This structure is indeed unique to the PR-MDP, and does not hold when generalizing two-player zero-sum PI to solve NR-MDP. 
Specifically, consider the two-player zero-sum PI that repeats the following two stages: 
1.πk ∈ arg max π∈Π 
vπ mix N,α(π,π̄k), 
2.πk ∈ arg min π̄∈P(Π) 
max π∈Π 
rπ mix N,α(π,π̄) + Pπ 
mix N,α(π,π̄)vπ 
mix N,α(πk,π̄k). 
vπ mix N,α(π,π̄k) is the value of the joint policy πmix 
N,α(π, π̄k), 
rπ mix N,α(π,π̄)(s) = Ea∼π,ā∼π̄[r(s, (1− α)a+αā)], and 
Pπ mix N,α(π,π̄)(s, s′) = Ea∼π,ā∼π̄[P (s | s, (1 − α)a+αā)] 
are the induced reward and dynamics from by πmix N,α(π, π̄). Following similar lines of proof as in 
Hansen et al. (2013) or as in Theorem 3, a similar γ-contraction result may be achieved for the NR-MDP, e.g., ||vk − v∗N,α||∞ ≤ γ||vk−1 − v∗N,α||∞. 
In such an algorithm, stage (1) is performed by solving an MDP, as in PR-PI. However, stage (2) requires solving a 1-step min-max problem. For general reward and transition probabilities it cannot be solved by solving a single-agent decision problem, as in the second stage of PR-PI (Algo-rithm 1). Furthermore, the solution of stage (2) cannot be achieved by a single-call to a gradient oracle as in Proposi-tion 2 (we elaborate the discussion in Appendix C.3). 
Regardless of these differences, in Section 6, we will use the approach of Soft PR-PI and offer DRL algorithms to solve both the PR and NR MDPs. While the approach we consider in Section 6 should be understood as a heuristic for solving NR-MDP, it is based on Algorithm 2, which guarantees convergence for PR-MDP in the error-free case. 
5. Related Work Robust RL: Traditional works in RL, such as Nilim & El Ghaoui (2005) and Iyengar (2005) have provided efficient algorithms for solving Robust MDPs, with uncertainty in the transition probabilities. Mannor et al. (2012) extended their approach to non-rectangular uncertainty sets, e.g., coupled uncertainty sets. However, these approaches are limited to solutions in the tabular case. Additionally, a connection between robustness and generalization has been suggested (Xu et al., 2009; Xu & Mannor, 2012), while it is not clear how this holds in RL, we believe that there lies a similar yet complex connection between the two concepts. 
Control: Obtaining robust policies in continuous control 
problems has been extensively investigated in the past. Most closely related to our work, are max-min Robust Control approaches (e.g., Bemporad et al. (2003); Kerrigan & Ma-ciejowski (2004); de la Pena et al. (2006). In this line of work, a control policy which is robust w.r.t. deterministic perturbations is calculated. There, the max-min problem is solved via Linear program, Quadratic program or by an explicit tree-search. Here, we focus on PI, and gradient based, schemes to solve a more specific problem; action robust policies. Furthermore, and to the best of our knowledge, in this line of works, discussion on the existence of strong-duality does not exists (i.e., as Proposition 1 and 4 assert for PR- and NR-MDPs). 
Robust Supervised Learning: Similar to the Ro-bust MDPs framework, robustness to adversarial exam-ples/attacks (Szegedy et al., 2013) is a measure of robustness in supervised learning. A method of learning robust classifiers is through Generative Adversarial Networks (Good-fellow et al., 2014). Similar to our approach, when using GANs for robustness, an adversary learns to create small perturbations in the input data in an attempt to cause a misclassification (Xiao et al., 2018; Samangouei et al., 2018; Kurakin et al., 2018). While these methods work well in practice, they generally lack convergence proofs and should thus be treated as heuristics. 
6. Experiments 6.1. Method 
Our approach adapts the Soft PR-PI algorithm to the high dimensional scenario. While in the tabular case we may use an MDP solver, which produces the optimal policy; when considering parametrized policies, e.g., neural networks, a dual-gradient approach is taken. In this approach, both the Actor and the Adversary are trained using gradient descent; as it is hard to measure convergence - we train the actor for N gradient steps followed by a single adversary step. 
We focus on a robust variant of DDPG which we call Action-Robust DDPG (AR-DDPG, see Appendix D, Algorithm 5). DDPG (Lillicrap et al., 2015) trains an actor to predict an action for each state µθ : S → A (i.e., a deterministic policy). In AR-DDPG we train two networks, deterministic policies, the actor and adversary, denoted by µθ and µ̄θ̄. Similarly to DDPG, a critic is trained to estimate the q-function of the joint-policy. For PR-MDP (Definition 1), the joint policy is 
πmix P,α(u |s; θ, θ̄)=(1− α)δ(u− µθ(s)) + αδ(u− µ̄θ̄(s)), 
(3) whereas for NR-MDP (Definition 2), the joint policy is, 
πmix N,α(u |s; θ, θ̄)=δ(u− ((1− α)µθ(s) + αµ̄θ̄(s))), (4) 
where δ(·) is the Dirac delta function. 
The following result generalizes DPG (Silver et al., 2014)
Action Robust Reinforcement Learning and Applications in Continuous Control 
for both PR and NR-MDPs. i.e., it establishes how to update θ and θ̄ using a deterministic gradient based method. Proposition 5. Let µθ, µ̄θ̄ be the agent’s and adversary’s deterministic policies, respectively. Let π(µθ, µ̄θ̄) be the joint policy given the agent and adversary policies. i.e., for PR-MDP π = πmix 
P,α (3), and for NR-MDP π = πmix N,α (4). 
Let J(π(µθ, µ̄θ̄)) = Es∼ρπ [vπ(s)] be the performance objective. The gradient of the actor and adversary parameters, for both PR- and NR-MDP is: 
∇θJ(π(µθ, µ̄θ̄)) = (1−α)Es∼ρπ [∇θµθ(s)∇aQ π(s,a)] , 
∇θ̄J(π(µθ, µ̄θ̄)) = αEs∼ρπ [∇θ̄µ̄θ̄(s)∇āQ π(s, ā)] . 
where for the PR-MDP we have a = µθ(s) and ā = µ̄θ̄(s), and for the NR-MDP a = ā = (1− α)µθ(s) + αµ̄θ̄(s). 
A proof, example algorithm and block diagram are provided in Appendix D. 
In order to validate our approach, we consider several Mu-JoCo domains (Todorov et al., 2012). MuJoCo contains several continuous control problems, such as robotic manipulation, in which we may test the ability of our approach to produce robust policies. Intuitively, our Probabilistic operator is correlative to the occurrence of large abrupt forces, e.g., someone suddenly pushes the robot, whereas the Noisy operator is correlative to mass uncertainty, e.g., the robot is heavier or lighter. 
Our evaluation is split into two parts, we begin by comparing the various hyper-parameters and how they affect the performance of both the NR and PR-MDP approaches. This evaluation is performed extensively on a single domain, the Hopper-v2 task, and the figures are provided in the appendix. We then compare the best performing variants across unseen domains. By doing so we test the transferability of these hyper-parameters across domains. 
6.2. Theory versus Practice 
Our theoretical approach, Soft PR-PI (Algorithm 2), is proven for the PR-MDP. The algorithm is based on a dynamic programming approach, (i) given a fixed adversary policy, solves the optimal agent’s policy, (ii) updates the adversary policy using gradients. 
1. While in theory, for the PR criterion, there exists a deterministic optimal policy - this does not necessarily hold for the NR case (Proposition 4). Thus searching over the space of deterministic policies is sub-optimal. 
2. Theoretical approaches in general require exact computation, however, in practice, we use function approximation schemes, e.g., deep neural networks. As such, convergence can not be ensured and the approach should be seen as a heuristic. 
Regardless of these differences, we based the empirical approach for both PR and NR-MDPs on Algorithm 2. 
NR-MDP PR-MDP 
Figure 1. Hopper-v2: Performance of both the NR and PR-MDP criteria as a function of the uncertainty α. 
6.3. Hyperparameter Ablation 
Table 1. Hyper-parameters considered. α values 0.01, 0.05, 0.1, 0.15 and 0.2 Actor update steps N 2, 5, 10 and 20 
The hyper-parameters we consider are shown in Table 1. In addition, we consider 3 exploration schemes: noiseless (onpolicy exploration), Ornstein Ulenbeck (OU, Uhlenbeck & Ornstein (1930)) and Parameter space noise (Plappert et al., 2017). Each configuration, is trained on 5 random seeds and the final policy, once the training is concluded, is evaluated across 100 episodes. The evaluation is performed without adversarial perturbations, on a range of mass values not encountered during training, i.e., we test the ability of the action robust approach to produce policies which are robust to model uncertainty. The baseline we compare to, is DDPG with parameter space noise for exploration, which performed best in our experiments. 
The extensive comparison is presented in the appendix, however the main conclusion is shown in Figure 1. While there is a clear correlation between the value of α and the performance of the PR-MDP criteria, e.g., an optimal value is attained at α ∈ [0.1, 0.15] and deviating from this range results in performance deterioration - this is not the case for the NR-MDP. Although the NR-MDP often attains competitive results, it is not clear how the various parameters affect it. We conclude that the for our simple gradient based approach, the PR approach exhibits a more stable behavior than the NR approach. 
Specifically, for the PR-MDP we decided to use Parameter space noise with α = 0.1 and a ratio of 10:1. Even though there are certain configurations under which the OU noise variant outperformed the Parameter space noise, we decided on the latter as it exhibited higher stability and is thus more likely to transfer easily to new domains. Similarly, a large α provides greater control to the adversary, as such we decided on a more conservative value of 0.1. 
For the NR-MDP this selection process is somewhat harder;
Action Robust Reinforcement Learning and Applications in Continuous Control 
Baseline NR-MDP PR-MDP 
Hopper 
Walker2d 
Humanoid 
InvertedPendulum 
Figure 2. Robustness to model uncertainty. Noise probability denotes the probability of a randomly sampled noise being played instead of the selected action. 
as slight changes in the hyper-parameters may result in radical changes in the performance. We selected the OU noise combined with α = 0.1 and a training ratio of 1:1. 
An interesting insight is that in the PR-MDP criteria, the adversary induces enough noise for exploration (Figure 1, PR-MDP - No Noise plot). This can be seen when observing the ‘no noise’ experiments, which show that the PR-MDP approach outperforms the baseline even without additional exploration noise. 
6.4. Testing on various MuJoCo domains 
Figure 2 presents our results, on various MuJoCo domains (additional results in Appendix E). It is apparent that while in the Hopper-v2 domain, the PR-MDP outperformed the NR-MDP criterion; this does not hold on all domains. More-
over, in most of the domains, both operators outperform the baseline, both in terms of robustness and in terms of performance in the absence of perturbations. While the optimal parameters may differ across domains; our results show that, in most cases, the parameters transfer across domains and result in improved performance without additional tuning. 
Failures: It is also important to acknowledge the scenarios in which our algorithm does not outperform the baseline. Such an example is the InvertedPendulum domain, in which the performance of the PR-MDP was found to be inferior to that of its non-robust counterpart. We find two possible explanations for this phenomenon (i) the parameter tuning is performed on the Hopper domain (as opposed to selecting the optimal hyper-parameters per each domain). As each domain is different, it is plausible that good hyper-parameters in a certain domain would not be good in all domains. (ii)
Action Robust Reinforcement Learning and Applications in Continuous Control 
Specifically in the InvertedPendulum domain, where the task is to balance a pole, an adversary which is too strong (large α value) prevents the agent from successfully solving the task. 
NR-MDP PR-MDP 
Figure 3. Diving Deeper: (Up) Testing Off-Policy Action-Robustness, and (Down) Solving the MaxMin operator. 
6.5. Diving Deeper 
We attempt to analyze the behavior of our criteria (Figure 3) by asking two questions: (i) Does the performance increase due to the added perturbations from the adversary, or does the operator itself induce a prior, e.g., regularization, on the policy which leads to improved performance. (ii) How close is the empirical behavior to its theoretical counterpart. 
Off-Policy Action Robustness: In previous experiments, during training, the action was drawn from the joint policy of the agent and adversary, where the joint policy is specified in the PR and NR-MDP approaches (see Definition 1,2). 
A natural alternative approach is to act with the actor’s policy, yet, to acquire an action-robust policy in an off-policy fashion. Meaning, use the same algorithms while obtaining the data without the effect of the adversary. A possible advantage of such an approach is minimizing the number of bad actions (since the adversary does not intervene), while still benefiting from the presence of robust learning. 
Figure 3 presents the results of this experiment. For the NR-MDP, it seems that the operator itself, i.e., the training is what results in the performance improvement; whereas the adversarial exploration amount to a small increase in stability. Surprisingly, an opposite effect is observed for the PR-MDP. There, the combination of adversarial exploration 
and the operator are both required in order to attain the performance increase. 
Does MaxMin equal MinMax? While so far we trained our agent through N actor updates followed by a single adversary gradient update, this corresponds to the MinMax operator, in theory the opposite should result in an identical performance (Proposition 1) for the PR-MDP approach, and to deteriorate the performance for the NR-MDP approach (Proposition 4). 
Experimentally (Figure 3) the results show that as opposed to the theoretical analysis, a ‘stronger’ adversary does result in performance degradation. This could be due to two possible factors: (i) as we trained for the same number of steps for both scenarios, it means that in this case the actor receives less gradient update steps, and/or (ii) it could be that increasing the convergence of the adversary results in faster convergence to a sub-optimal solution (w.r.t. the actor). 
7. Summary We have presented two new criteria for robustness, the Prob-abilistic and Noisy action Robust MDP, related each to real world scenarios of uncertainty and discussed the theoretical differences between both approaches. Additionally; we developed the Soft PR-PI (Algorithm 2), a policy iteration scheme for solving PR-MDPs. Building upon the Soft PR-PI algorithm, we presented a deep reinforcement learning approach, which is capable of solving our criteria. We compared both criteria, analyzed how the various hyper-parameters affect the behavior and how the empirical results correlate (and occasionally contradict) with the theoretical approach. Most importantly, we notice that not only does training with our criteria result in robust policies, but our approach improves performance even in the absence of perturbations. 
Lastly, for solving an action-robust policy, there is no need in providing an uncertainty set. The approach requires only a scalar value, namely α (or possibly a state-dependent α(s)), which implicitly defines an uncertainty set (see Sec-tion 3.1). This is a major advantage compared to standard robust approaches in RL and control, which, to the best of our knowledge, require a distribution over models or perturbations. Of course, this benefit is also a restriction - the Action Robust approach is unable to handle any kind of worst-case perturbations. Yet, due to its simplicity, and its demonstrated performance, it is worthwhile to be considered by an algorithm designer. 
8. Acknowledgements The authors would like to thank Bruno Scherrer, Esther Derman and Nadav Merlis for the fruitful discussions and help during the work on this paper.
Action Robust Reinforcement Learning and Applications in Continuous Control 
References Barnett, S. A. Convergence problems with generative adver-
sarial networks (gans). arXiv preprint arXiv:1806.11382, 2018. 
Başar, T. and Bernhard, P. H-infinity optimal control and related minimax design problems: a dynamic game approach. Springer Science & Business Media, 2008. 
Baydin, A. G., Pearlmutter, B. A., Radul, A. A., and Siskind, J. M. Automatic differentiation in machine learning: a survey. Journal of Marchine Learning Research, 18:1–43, 2018. 
Bemporad, A., Borrelli, F., and Morari, M. Min-max control of constrained uncertain discrete-time linear systems. IEEE Transactions on automatic control, 48(9):1600– 1606, 2003. 
de la Pena, D. M., Alamo, T., Bemporad, A., and Cama-cho, E. F. Feedback min-max model predictive control based on a quadratic cost function. In American Control Conference, 2006, pp. 6–pp. IEEE, 2006. 
Epstein, L. G. and Schneider, M. Recursive multiple-priors. Journal of Economic Theory, 113(1):1–31, 2003. 
Frank, M. and Wolfe, P. An algorithm for quadratic programming. Naval research logistics quarterly, 3(1-2): 95–110, 1956. 
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y. Generative adversarial nets. In Advances in neural information processing systems, pp. 2672–2680, 2014. 
Hansen, T. D., Miltersen, P. B., and Zwick, U. Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a constant discount factor. Journal of the ACM (JACM), 60(1):1, 2013. 
Hoffman, A. J. and Karp, R. M. On nonterminating stochastic games. Management Science, 12(5):359–370, 1966. 
Iyengar, G. N. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005. 
Kakade, S. and Langford, J. Approximately optimal approximate reinforcement learning. In ICML, volume 2, pp. 267–274, 2002. 
Kerrigan, E. C. and Maciejowski, J. M. Feedback min-max model predictive control using a single linear program: robust stability and the explicit solution. International Journal of Robust and Nonlinear Control: IFAC-Affiliated Journal, 14(4):395–413, 2004. 
Kurakin, A., Goodfellow, I., Bengio, S., Dong, Y., Liao, F., Liang, M., Pang, T., Zhu, J., Hu, X., Xie, C., et al. Adver-sarial attacks and defences competition. arXiv preprint arXiv:1804.00097, 2018. 
Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning. arXiv preprint arXiv:1509.02971, 2015. 
Maitra, A. and Parthasarathy, T. On stochastic games. Jour-nal of Optimization Theory and Applications, 5(4):289– 300, 1970. 
Mannor, S., Mebel, O., and Xu, H. Lightning does not strike twice: Robust mdps with coupled uncertainty. arXiv preprint arXiv:1206.4643, 2012. 
Nash, J. Non-cooperative games. Annals of mathematics, pp. 286–295, 1951. 
Nilim, A. and El Ghaoui, L. Robust control of markov decision processes with uncertain transition matrices. Op-erations Research, 53(5):780–798, 2005. 
Patek, S. D. Stochastic and shortest path games: theory and algorithms. PhD thesis, Massachusetts Institute of Technology, 1997. 
Peng, X. B., Andrychowicz, M., Zaremba, W., and Abbeel, P. Sim-to-real transfer of robotic control with dynamics randomization. In 2018 IEEE International Confer-ence on Robotics and Automation (ICRA), pp. 1–8. IEEE, 2018. 
Pinto, L., Davidson, J., Sukthankar, R., and Gupta, A. Ro-bust adversarial reinforcement learning. In International Conference on Machine Learning, pp. 2817–2826, 2017. 
Plappert, M., Houthooft, R., Dhariwal, P., Sidor, S., Chen, R. Y., Chen, X., Asfour, T., Abbeel, P., and Andrychow-icz, M. Parameter space noise for exploration. arXiv preprint arXiv:1706.01905, 2017. 
Puterman, M. L. Markov decision processes: discrete stochastic dynamic programming. John Wiley & Sons, 1994. 
Rao, S., Chandrasekaran, R., and Nair, K. Algorithms for discounted stochastic games. Journal of Optimization Theory and Applications, 11(6):627–637, 1973. 
Samangouei, P., Kabkab, M., and Chellappa, R. Defense-gan: Protecting classifiers against adversarial attacks using generative models. arXiv preprint arXiv:1805.06605, 2018. 
Scherrer, B. Approximate policy iteration schemes: a comparison. In International Conference on Machine Learn-ing, pp. 1314–1322, 2014. 
Scherrer, B. and Geist, M. Local policy search in a convex space and conservative policy iteration as boosted policy search. In Joint European Conference on Machine Learn-ing and Knowledge Discovery in Databases, pp. 35–50. Springer, 2014.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Shani, L., Efroni, Y., and Mannor, S. Revisiting exploration-conscious reinforcement learning. arXiv preprint arXiv:1812.05551, 2018. 
Shapley, L. S. Stochastic games. Proceedings of the national academy of sciences, 39(10):1095–1100, 1953. 
Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and Riedmiller, M. Deterministic policy gradient algorithms. In ICML, 2014. 
Sion, M. et al. On general minimax theorems. Pacific Journal of mathematics, 8(1):171–176, 1958. 
Straffin, P. D. Game theory and strategy, volume 36. MAA, 1993. 
Sutton, R. S., McAllester, D. A., Singh, S. P., and Mansour, Y. Policy gradient methods for reinforcement learning with function approximation. In Advances in neural information processing systems, pp. 1057–1063, 2000. 
Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., and Fergus, R. Intriguing properties of neural networks. arXiv preprint arXiv:1312.6199, 2013. 
Tamar, A., Xu, H., and Mannor, S. Scaling up robust mdps by reinforcement learning. arXiv preprint arXiv:1306.6189, 2013. 
Todorov, E., Erez, T., and Tassa, Y. Mujoco: A physics engine for model-based control. In Intelligent Robots and Systems (IROS), 2012 IEEE/RSJ International Con-ference on, pp. 5026–5033. IEEE, 2012. 
Uhlenbeck, G. E. and Ornstein, L. S. On the theory of the brownian motion. Physical review, 36(5):823, 1930. 
Wiesemann, W., Kuhn, D., and Rustem, B. Robust markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013. 
Xiao, C., Li, B., Zhu, J.-Y., He, W., Liu, M., and Song, D. Generating adversarial examples with adversarial networks. arXiv preprint arXiv:1801.02610, 2018. 
Xu, H. and Mannor, S. The robustness-performance tradeoff in markov decision processes. In Advances in Neural Information Processing Systems, pp. 1537–1544, 2007. 
Xu, H. and Mannor, S. Robustness and generalization. Machine learning, 86(3):391–423, 2012. 
Xu, H., Caramanis, C., and Mannor, S. Robustness and regularization of support vector machines. Journal of Machine Learning Research, 10(Jul):1485–1510, 2009.
Action Robust Reinforcement Learning and Applications in Continuous Control 
A. Discounted Markov Games A.1. Preliminaries 
We define the framework of discounted, two-player zero-sum Markov Games (MG) with finite state space and continuous action space. A MG is determined by the 5-tuple (S,A,B, P,R, γ) (Patek, 1997). Here S is a finite state space, A and B are compact subsets of RA, which represent the agent and adversary, respectively. For any (s, a, b) ∈ S × A× B let the dynamics P = P (· | s, a, b) be a probability measure on S , and let the reward function r(s, a, b) be a bounded measureable function on A× B for any s ∈ S. Consider a strategy of the players µ, ν, where both are probability measures over Borel sets of A,B, respectively. Let rµ,ν ∈ R|S| where rµ,ν(s) 
def = Ea∼µ,b∼ν [r(s, µ, ν)], and the dynamics Pµ,ν ∈ R|S|×|S|, 
where Pµ,νi,j def = Ea∼µ,b∼ν [P (sj | si, µ, πB)] and is a stochastic matrix. Following notation from Maitra & Parthasarathy 
(1970), we denote PA and PB as the set of probability measures on the Borel sets of A and B, respectively. 
Definition 3. The value of fixed strategy µ, ν is given by vµ,ν = ∑∞ t=0 γ 
t(Pµ,ν)trµ,ν . Given a fixed ν ∈ PB the value of the optimal counter strategy of player A is vν = supµ∈PA v 
µ,ν . Accordingly, for a fixed µ ∈ PA the value of the optimal counter strategy of player B is vµ = infν∈PB v 
µ,ν . Furthermore, if the sup and inf are attainable, we refer to arg minν∈PB v 
µ,ν and arg maxµ∈PA v µ,ν as optimal counter strategies to µ and ν, respectively. 
We make the following assumptions on the dynamics and reward functions. 
Assumption 1. 
 Both A,B are compact metric spaces. 
 For any s ∈ S the reward r is continuous and bounded function on A× B. 
 For any s ∈ S , whenever (an, bn)→ (a, b), where (an, bn), (a, b) ∈ A× B, then P (· | s, an, bn) converges weakly to P (· | s, a, b). 
In the rest of the section we follow (Patek, 1997)[Section 2-3] that analyzed zero-sum MG for stochastic shortest paths, while performing minor modifications for the discounted and continuous action-space setup. 
Define the following Bellman operators. 
Definition 4. Let PA and PB be the set of all probability measures on the Borel Sets of A and B, respectively, µ ∈ PA, ν ∈ PB , and let v ∈ R|S|. The Bellman operator, and Fixed-Policy Bellman operators are according to the following. 
Tµ,νv = rµ,ν + γPµ,νv, 
Tµv = min ν∈PB 
(rµ,ν + γPµ,νv) , T̄ νv = max µ∈PA 
(rµ,ν + γPµ,νv) 
Tv = max µ∈PA 
min ν∈PB 
(rµ,ν + γPµ,νv) , T̄ v = min ν∈PB 
max µ∈PA 
(rµ,ν + γPµ,νv) , 
where equality holds component-wise. 
Notice that the max and min are attainable since PA, PB are compact sets. Furthermore, by Maitra & Parthasarathy (1970)[Lemma 2.2] and under Assumption 1, both the max and min are continuous and bounded. Thus, we can replace sup inf and inf sup by corresponding max and min. 
We have the following important lemma. 
Lemma 6. For any bounded v ∈ R|S|, Tv = T̄ v. 
Proof. Following similar arguments as in Maitra & Parthasarathy (1970), Equation 2, and using Sion’s minimax theorem (Sion et al., 1958)[Theorem 3.4], for any s ∈ S we have that, 
sup µ∈PA 
inf ν∈PB 
rµ,ν(s) + Pµ,νv(s) = inf ν∈PB 
sup µ∈PA 
rµ,ν(s) + Pµ,νv(s). 
Since PA, PB are compact and rµ,ν + Pµ,νv is bounded and continuous on A × B for any s ∈ S, the sup, inf can be replaced by min,max (e.g., by Maitra & Parthasarathy (1970)[Lemma 2.2]).
Action Robust Reinforcement Learning and Applications in Continuous Control 
The analysis in Patek (1997) is based on assumption R, which results in Tv = T̄ v. Since we allow the agents to use mixed-strategies, according to Lemma 6, we obtain Tv = T̄ v in our setup as well. Furthermore, since we use discounted MG, assumption SSP in Patek (1997) is also satisfied. Every strategy (µ, ν) is proper; it terminates with probability one, as the discount factor (γ) is smaller than 1. 
Lemma 7. Tµ,ν , Tµ, T̄ ν , T are γ contractions in the sup-norm. 
Proof. We follow similar technique as in Patek (1997), adjusted to our setup. Let v1, v2 ∈ R|S|. Then, 
Tµ,νv1 − Tµ,νv2 = γPµ,ν(v1 − v2) ≤ γPµ,ν1||v1 − v2||∞ = γ1||v1 − v2||∞, 
where 1 is the one vector. The last relation holds since Pµ,ν is a stochastic matrix and thus Pµ,ν1 = 1. By repeating the same argument for Tµ,νv2 − Tµ,νv1 and taking the sup-norm we conclude that ||Tµ,νv1 − Tµ,νv2||∞ ≤ γ||v1 − v2||∞. 
We now prove similar result on Tµ. Let ν, ν′ ∈ PB such that Tµv1 = Tµ,νv1, T µv2 = Tµ,ν 
′ v2. Then, 
Tµv1 − Tµv2 ≤ Tµ,νv1 − Tµ,νv2, 
Tµv2 − Tµv1 ≤ Tµ,ν ′ v1 − Tµ,ν 
′ v2. 
By taking the sup-norm and using the fact Tµ,ν is a γ-contraction, we conclude that Tµ is also a γ-contraction. Similar argument establishes that T̄ ν is a γ-contraction. 
Lastly, let µ ∈ PA such that Tv2 = Tµv2, and ν ∈ PB such that Tµv1 = Tµ,νv1. Then, 
Tv1 − Tv2 = Tv1 − Tµv2 
≤ Tµv1 − Tµv2 
= Tµ,νv1 − Tµv2 
≤ Tµ,νv1 − Tµ,νv2. 
Similar argument leads to Tv2 − Tv1 ≤ Tµ,νv2 − Tµ,νv1 for properly defined µ, ν. Again, by taking the sup norm and using the fact that Tµ,ν is a γ-contraction we conclude the proof. 
The following propositions relate the fixed-point of Tµ, T̄ ν to the values and policies defined in 3. Furthermore, the last one establishes the fact the zero-sum MG has value. 
Proposition 8. The following claims hold. 
 Let µ ∈ PA, ν ∈ PB be stationary policies. The value vµ,ν is the fixed point of the operator Tµ,ν , vµ,ν = Tµ,νvµ,ν . 
 Given a policy ν ∈ PB , vν = supµ∈PA is the unique fixed point of T̄ ν . Furthermore, the sup is attainable in the set A. 
 Given a policy µ ∈ PA, vµ = infν∈PB is the unique fixed point of Tµ. Furthermore, the inf is attainable in the set B. 
Proof. The proof of the first claim is standard, e.g., Puterman (1994)[Section 6.1]. By fixing a policy for any of the players the problem amounts for solving a single agent MDP (e.g., Puterman (1994)). Due to Assumption 1, the reward and dynamics of the MDP are also continuous and bounded. Since the action set in compact for both player A and B, we can use Puterman (1994)[Theorem 6.2.10] and conclude the proof. 
Proposition 9. The unique fixed point v∗ = Tv∗ is also the equilibrium value of the zero-sum MG, v∗ = supµ∈PA infν∈PB v 
µ,ν = infν∈PB supµ∈PA v µ,ν , thus, the MG has a well defined value. 
Furthermore, the stationary policies µ ∈ PA, ν ∈ PB for which v∗ = T̄ v∗ = Tv∗ = Tµ,νv∗ are in Nash-Equilibrium, and satisfy vµ 
′,ν∗ ≤ v∗ ≤ vµ∗,ν for any ν′ ∈ PB , µ′ ∈ PA. 
Proof. See proof Patek (1997)[Proposition 3.2].
Action Robust Reinforcement Learning and Applications in Continuous Control 
Algorithm 3 Zero-Sum Markov-Game PI Initialize: ν0, k = 0 while stopping criterion is not satisfied do µk ∈ arg maxµ v 
µ,νk 
νk+1 ∈ arg minν T̄ νvµk,νk 
k ← k + 1 end while Return πk−1 
Algorithm 4 Soft Zero-Sum Markov-Game PI Initialize: ν0, k = 0, η ∈ (0, 1] while stopping criterion is not satisfied do µk ∈ arg maxµ v 
µ,νk 
ν′ ∈ arg minν T̄ νvµk,νk 
νk+1 = (1− η)νk + ην′ 
k ← k + 1 end while Return πk−1 
A.2. Policy Iteration and Soft Policy Iteration for Zero-Sum Markov Games 
In this section, we formulate two PI schemes that solve a zero-sum MG. The Zero-Sum MG PI scheme (see Alg. 3) is a well known one (Hoffman & Karp, 1966; Rao et al., 1973; Hansen et al., 2013). 
The Soft Zero-Sum MG PI (see Alg. 4) generalizes the usual PI. Instead of updating with a 1-step greedy policy it updates softly w.r.t. the 1-step greedy policy. Although this generalization has been analyzed extensively for a single-agent PI (e.g., (Kakade & Langford, 2002; Scherrer, 2014)), to the best of our knowledge, it was not analyzed in the context of Markov-Games. 
By generalizing arguments from (Scherrer, 2014) to framework of Zero-Sum MG (defined in Section A.1) we prove the following result. 
Theorem 10. The sequence vk def = vµk,νk contracts toward v∗ with rate of 1− η + γη, i.e., 
||vk − v∗α|| ≤ (1− η + γη)||vk−1 − v∗α|| . 
As a corollary, and by plugging η = 1, we get the convergence rate of Zero-Sum MG PI. Notice that although the action space is continuous the proof follows using standard machinery, since the state space is still finite. We now give the proof of the theorem. 
The proof has two steps. We first show v∗ ≤ vk+1 ≤ vk, where vk def = vµk,νk . Building on this fact, we prove the contraction 
property by generalizing technique from (Scherrer, 2014)[Theorem 1], to two player game. 
Lemma 11. v∗ ≤ vk+1 ≤ vk. 
Proof. We have that vk = vµk,νk . 
vµk,νk = T̄ νkvµk,νk 
= (1− η)T̄ νkvµk,νk + ηT̄ νkvµk,νk 
≥ (1− η)T̄ νkvµk,νk + min ν∈PB 
ηT̄ νvµk,νk 
= (1− η)T̄ νkvµk,νk + ηT̄ ν ′ vµk,νk 
= max µ∈PA 
((1− η)Tµ,νkvµk,νk) + max µ∈PA 
( ηT̄µ,ν 
′ vµk,νk 
) ≥ max µ∈PA 
( (1− η)Tµ,νkvµk,νk + ηT̄µ,ν 
′ vµk,νk 
) = max µ∈PA 
Tµ,(1−η)νk+ην′vµk,νk = T̄ (1−η)νk+ην′vµk,νk . (5) 
The first relation holds due to Proposition 8, the forth relation holds by construction of ν′, minν∈PB T̄ νvµk,νk = 
T̄ ν ′ vµk,νk , the fifth relation is by Definition 4, the sixth relation holds since sum of maximum elements is big-
ger than the maximum of a sum, and the seventh relation holds since the fixed-policy Bellman operator satisfies Tµ,(1−η)ν1+ην2 = (1− η)Tµ,ν1 + ηTµ,ν2 .
Action Robust Reinforcement Learning and Applications in Continuous Control 
Due to the monotonicity of T̄ (1−η)νk+ην′ (e.g, Patek (1997)[Appendix A]), we can repeatedly use (5), 
vk ≥ T̄ (1−η)νk+ην′vk ≥ · · · ≥ lim n→∞ 
(T̄ (1−η)νk+ην′)nvk = vk+1, 
where vk+1 = vµk+1,νk+1 . Indeed, T̄ (1−η)νk+ην′ is the optimal Bellman operator given a fixed adversary strategy, (1− η)νk + ην′. 
Lastly, we show that in each iteration v∗ ≤ vk. For any adversarial strategy νk, 
vk = max µ∈PA 
vµ,νk ≥ min ν∈PB 
max µ∈PA 
vµ,ν = v∗. 
Where the third relation holds by Proposition 9. 
We are now ready to prove Theorem 10. 
Proof. As before, define vk def = vµk,νk . We have that, 
v∗ − vk+1 = v∗ − Tµk+1,(1−η)νk+ην′vk+1 
≥ v∗ − Tµk+1,(1−η)νk+ην′vk 
= (1− η)(v∗ − Tµk+1,νkvk) + η(v∗ − Tµk+1,ν ′ vk), (6) 
where the first relation holds since vk+1 = vµk+1,(1−η)νk+ην′ and the second relation holds since Tµ,ν is a monotone operator and vk+1 ≤ vk by Lemma 11. 
Consider the first term in (6). 
v∗ − Tµk+1,νkvk ≥ v∗ − Tµk,νkvk = vk. (7) 
The first relation holds since Tµk,νkvk = maxµ∈PA T µ,νkvk and the second relation holds since by definition vk = vµk,νk = 
Tµk,νkvµk,νk (due to Proposition 8). 
Remember that ν′ ∈ arg minν∈PB T̄ νvk (as in the update of Alg. 4). Thus, 
T̄ ν ′ vk = min 
ν∈PB T̄ νvk = min 
ν∈PB max µ∈PA 
Tµ,νvk = max µ∈PA 
min ν∈PB 
Tµ,ν = Tvk, (8) 
where the third relation is due to Lemma 6. 
Now, for the second term in (6) we have that, 
v∗ − Tµk+1,ν ′ vk = Tv∗ − Tµk+1,ν 
′ vk 
≥ Tµ ∗,ν∗v∗ − max 
µ∈PA Tµ,ν 
′ vk 
= Tv∗ − Tvk. (9) 
The first relation holds since v∗ is the fixed point of T , and the third relation holds by (8). 
Plugging (7) and (9) to (6) yields, 
v∗ − vk+1 ≥ (1− η)(v∗ − vk) + η(Tv∗ − Tvk). 
Since 0 ≥ v∗ − vk+1 by Lemma 11, we can take the max-norm and conclude the proof, 
||v∗ − vk+1||∞ ≤ (1− η)||v∗ − vk||∞ + η||Tv∗ − Tvk||∞ ≤ (1− η)||v∗ − vk||∞ + ηγ||v∗ − vk||∞, 
where the first relation holds by the triangle inequality and the second holds since T is a γ-contraction by Proposition 7.
Action Robust Reinforcement Learning and Applications in Continuous Control 
B. Probabilistic Action Robust MDP In this section, we focus on PR-MDPs (Section 3) and map the problem of solving the optimal probabilistic robust policy to solving a Zero-Sum MG. We then continue and provide the proofs of Section 3, which are mostly corollaries to the results in Section A. 
For simplicity, we provide the definition of PR-MDPs as given in Section 3. Definition 1. Let α ∈ [0, 1]. A Probabilistic Action Robust MDP is defined by the 5-tuple of an MDP (see Section 2.1). Let π, π̄ be policies of an agent an adversary. We define their probabilistic joint policy πmix 
P,α(π, π̄) as ∀s ∈ S, πmix P,α(a | s) ≡ 
(1− α)π(a | s) + απ̄(a | s). 
Let π be an agent policy. As opposed to standard MDPs, the value of the policy is defined by vπP,α = minπ̄∈Π Eπ 
mix P,α(π,π̄)[ 
∑ t γ 
tr(st,at)], where at ∼ πmix P,α(π(st), π̄(st)). The optimal probabilistic robust policy is 
the optimal policy of the PR-MDP 
π∗P,α ∈ arg max π∈P(Π) 
min π̄∈Π 
Eπ mix P,α(π,π̄)[ 
∑ t 
γtr(st,at)]. (1) 
The optimal probabilistic robust value is v∗P,α = v π∗P,α P,α . 
B.1. Probabilistic Action Robust MDP as a Zero-Sum Markov Game 
Consider the single agent MDP on which the PR-MDP is defined,M = (S,A, P,R, γ). Assumption 2. 
 A is compact metric space. 
 For any s ∈ S the reward r is continuous and bounded function on A. 
 For any s ∈ S, whenever (an)→ (a), where (an), (a) ∈ A, then P (· | s, an) converges weakly to P (· | s, a). 
Solving the optimal probabilistic robust policy can be equivalently viewed as solving a Zero-Sum MG MP,α. Let MP,α = (S,A,A, PP,α, RP,α, γ). Meaning, its state-space is equal to that of the original MDP, the action space of the two players is the action space of the original MDP, and its discount factor is equal to the discount factor ofM. Its reward and dynamics are given as follows, 
rP,α(s, a, b) = (1− α)r(s, a) + αr(s, b), PP,α(s′ | s, a, b) = (1− α)P (s′ | s, a) + αP (s′ | s, b). (10) 
By Assumption 2 onM, Assumption 1 on the MG is satisfied. 
It is easy to prove that a value vπ mix P,α(π1,π2) defined onM is equal to the value vπ1,π2 defined onMP,α. Since there is a 
one-to-one correspondence between the problems, solving the later is equivalent to solving the first. 
B.2. Proof of Proposition 1 
Consider the Zero-Sum MGMP,α, and let PA be the set of all probability measures on the Borel Sets of A. We see that the Bellman operators ofMP,α (Definition 4) decouples to two terms due to (10), 
Tv = max µ∈PA 
min ν∈PA 
rµ,ν + γPµ,νv 
= (1− α) 
( max µ∈PA 
rµ + Pµv 
) + α 
( min ν∈PA 
rµ + Pµv 
) , (11) 
and similarly for Tµ, T̄ ν and Tµ,ν . 
According to Proposition 9 the the optimal policy for the max-agent µ∗ satisfies v∗ = Tv∗ = Tµ ∗ v∗. Thus, µ∗ should 
satisfy 
(1− α) 
( max µ∈PA 
rµ + Pµv∗ ) 
+ α 
( min ν∈PA 
rµ + Pµv∗ ) 
= (1− α) ( rµ ∗ 
+ Pµ ∗ v∗ ) 
+ α 
( min ν∈PA 
rµ + Pµv∗ ) 
⇐⇒ max µ∈PA 
rµ + Pµv∗ = rµ ∗ 
+ Pµ ∗ v∗
Action Robust Reinforcement Learning and Applications in Continuous Control 
meaning, µ∗ ∈ maxµ∈PA r µ + Pµv∗ which can always be solved by a deterministic policy. 
B.3. Probabilistic Action Robust and Robust MDPs 
Based on the mapping between a PR-MDP to a corresponding Zero-Sum MG B.1 the relation to Robust MDPs becomes apparent. Instead for the adversary to pick an action which induces a change in the dynamics and reward 10, the adversary can directly choose the dynamics and reward. Obviously, the value of such a policy is similar under this equivalent view. We conclude the result since the adversary is defined on the class of stochastic policies P(Π). 
B.4. Proof of Proposition 2 
Repeating the same arguments as in Policy Gradient Theorem (Sutton et al., 2000)[Theorem 1] for continuous action space we have that for any s ∈ S and π ∈ P(Π), i.e., any stochastic stationary policy, 
∇πvπ(s) = ∑ s 
dπ(s) 
∫ a∈A ∇ππ(s,a)qπ(s,a)da 
Notice that we can replace the integration and differentiation order by Leibniz integral rule since ∇πvπ(s) exists and is bounded. Let h(· | s) be a deterministic probability measure on A. Similarly to (Scherrer & Geist, 2014) for any s ∈ S, 
〈∇πvπ(s), h〉 = ∑ s 
dπ(s) 
∫ a∈A 〈∇ππ(s,a), h〉qπ(s,a)da 
= ∑ s 
dπ(s)qπ(s, h(s)). 
To minimize 〈∇πvπ(s), h〉 we choose for any s ∈ S, ah ∈ arg mina q π(·, a) = arg minπ′ r 
π′ + γPπ ′ vπ . 
B.5. Proof of Theorem 3 
The theorem is a corollary of Theorem 10 and Proposition 2, while using the structure of the defined zero-sum MG for PR-MDP in Section B.1,MP,α. 
Specifically, the first stage of the general Soft Zero-Sum MG PI 4 is similar to the first stage of Soft Probabilistic Robust PI 2. Furthermore, forMP,α it holds for any bounded v ∈ R|S|, 
arg min ν∈PA 
T̄ νv = arg min ν∈PA 
max µ∈PA 
Tµ,νv 
= arg min ν∈PA 
max µ∈PA 
(1− α)(rµ + γPµv) + α(rν + γP νv) 
= arg min ν∈PA 
(rν + γP νv) , 
where the first relation holds by definition 4, the second relation holds due to the specific form of the Bellman operators similarly to (11), and the third relation holds since the first term does not depend on ν. 
By using Proposition 2 we get that Soft Probabilistic Robust PI 2 is an instance of the more general Soft Zero-Sum MG PI 4, and prove the Theorem as a corollary of Theorem 10. 
C. Noisy Action Robust MDP as a Zero-Sum Markov Game We focus on NR-MDPs (Section 4) and map the problem of solving the optimal noisy robust policy to solving a Zero-Sum MG. As in previous section, the proofs of Section 4, are mostly corollaries to the results in Section A. 
For simplicity, we provide the definition of NR-MDPs as given in Section 3. Definition 2. Let α ∈ [0, 1]. A Noisy Action Robust MDP is defined by the 5-tuple of an MDP (see Section 2.1). Let π, π̄ be policies of an agent and an adversary. We define their noisy joint policy πmix 
N,α(π, π̄) as 
∀s ∈ S,a ∈ A, πmix N,α(a | s) ≡ Eb∼π(·|s) 
b̄∼π̄(·|s) [1a=(1−α)b+αb̄],
Action Robust Reinforcement Learning and Applications in Continuous Control 
the relation is obtained by the fact that a ∼ π, ā ∼ π̄. 
Let π be an agent policy. For NR-MDP, its value is defined by vπN,α = minπ̄∈Π Eπ mix N,α(π,π̄)[ 
∑ t γ 
tr(st,at)], where at ∼ πmix N,α(π(st), π̄(st)). The optimal α-noisy robust policy is the optimal policy of the NR-MDP 
π∗N,α ∈ arg max π∈P(Π) 
min π̄∈Π 
Eπ mix N,α(π,π̄)[ 
∑ t 
γtr(st,at)]. (2) 
The optimal noisy robust value is v∗N,α = v π∗N,α N,α . 
C.1. Noisy Action Robust MDP as a Zero-Sum Markov Game 
Consider the single agent MDP on which the NR-MDP is defined,M = (S,A, P,R, γ) and assume it satisfies Assumption 2. Solving the optimal probabilistic robust policy can be equivalently viewed as solving a Zero-Sum MGMN,α. Let MN,α = (S,A,A, PN,α, RN,α, γ). Meaning, its state-space is equal to that of the original MDP, the action space of the two players is the action space of the original MDP, and its discount factor is equal to the discount factor ofM. Its reward and dynamics are given as follows, 
rN,α(s, a, b) = r(s, (1− α)a+ αb), PP,α(s′ | s, a, b) = P (s′ | s, (1− α)a+ αb). (12) 
Since the single agent MDP satisfies Assumption Assumption 2, the MG game defined byMN,α satisfies 1. 
It is easy to prove that a value vπ mix N (π1,π2) defined on the induced NR-MDP fromM is equal to the value vπ1,π2 defined on 
the MGMN,α. Since there is a one-to-one correspondence between the problems, solving the later is equivalent to solving the first. 
C.2. Proof of Proposition 4 
Consider an MDP with a single state a quadratic reward of the form r(a) = a2 where a ∈ [−1, 1]. In this case, the solution does not depend on the horizon and an optimal action w.r.t. a single time step will be the solution for the discounted reward. Denote P([−1, 1]) as the set of all probability measures on the Borel sets of [−1, 1]. 
If both of the players are only allowed to take deterministic actions, then the min-max and max-min values are not equivalent, 
max a∈[−1,1] 
min b∈[−1,1] 
((1− α)a+ αb)2 = 
{ (1− 2α)2, α ≤ 0.5 
0, α > 0.5 
min b∈[−1,1] 
max a∈[−1,1] 
((1− α)a+ αb)2 = (1− α)2. 
Thus, for this example, strong duality on the sets of deterministic policies does not hold, 
max a∈[−1,1] 
min b∈[−1,1] 
((1− α)a+ αb)2 < min b∈[−1,1] 
max a∈[−1,1] 
((1− α)a+ αb)2 = (1− α)2. 
Furthermore, we now show that considering random policies can increase the value. Let the policy of the max-player be P (a = −1) = P (a = 1) = 0.5, obviously, P ∈ P([−1, 1]). For this policy, we have that, 
min b∈[−1,1] 
Ea∼P (·)[(1− α)a+ αb)2] = min b∈[−1,1] 
(1− α)2 + α2b = (1− α)2. 
We conclude that for this example 
max a∈[−1,1] 
min b∈[−1,1] 
((1− α)a+ αb)2 < max P∈P([−1,1]) 
min b∈[−1,1] 
Ea∼P [((1− α)a+ αb)2]. 
C.3. Policy Iteration of NR-MDP 
We can use the Soft Zero-Sum MG PI (see Algorithm 4), or, by fixing η = 1, Zero-Sum MG PI.
Action Robust Reinforcement Learning and Applications in Continuous Control 
The algorithm repeats two stages of (i) solving an MDP by fixing the adversary policy, (ii) solving a 1-step greedy minimax decision problem on the set of stochastic policies. This comes in contrast to the corresponding PI algorithm that solves PR-MDP. There, stage (ii) involved in solving a single agent, 1-step greedy, decision problem. This problem can be more easily solved by function maximization. 
Furthermore, this fact suggest that a simple Frank-Wolfe update (Frank & Wolfe, 1956), as was performed in Soft Probabilistic Robust PI (Algorithm 2) would not work, at least not using the analysis we suggested here. Meaning, a relation between the maximal projection on the gradient ∇πvπ and the 1-step greedy minimax decision problem, as shown to hold in Proposition 2, would not exists. 
D. Actor Gradients Proof Proof. Our proof follows the proof of the deterministic policy gradients (DPG) (Silver et al., 2014). 
In order to retain consistency with (Silver et al., 2014), we denote the deterministic policy π by µ : S 7→ A. The parametrized policies µθ and µ̄θ̄ are, respectively, the actor and adversary policies. We refer to the α-mixture policy πmix 
N/P,α(µθ, µ̄θ̄) 
simply as πmix N/P,α(θ, θ̄), for ease of notation. 
Assumption 3. p(s′ | s,a),∇ap(s ′ | s,a), µθ(s),∇θµθ(s), µ̄θ̄(s),∇θ̄µ̄θ̄(s), r(s,a),∇ar(s,a), p1(s) are continuous in 
all parameters and variables s,a, s′ and x. 
Assumption 4. There exists a b and L such that sups p1(s) < b, supa,s,s′ p(s ′ | s,a) < b, supa,s r(s,a) < 
b, supa,s,s′ ||∇ap(s ′ | s,a)|| < L, and sups,a ||∇ar(s,a)|| < L. 
NR-MDP: 
∇θvπ mix N,α(θ,θ̄) = ∇θQπ 
mix N,α(θ,θ̄)(s, πmix 
N,α(θ, θ̄)(s)) 
= ∇θ ( r(s, πmix 
N,α(θ, θ̄)(s)) + 
∫ S 
γp(s′ | s, πmix N,α(θ, θ̄)(s))vπ 
mix N,α(θ,θ̄)(s′) 
) d s′ 
= ∇θπmix N,α(θ, θ̄)(s)∇ar(s,a) |a=πmix 
N,α(θ,θ̄)(s) +∇θ ∫ S 
γp(s′ | s, πmix N,α(θ, θ̄)(s))vπ 
mix N,α(θ,θ̄)(s′)d s′ 
= ∇θπmix N,α(θ, θ̄)(s)∇θr(s,a) |a=πmix 
N,α(θ,θ̄)(s) 
+ 
∫ S 
γ ( p(s′ | s, πmix 
N,α(θ, θ̄)(s))∇θvπ mix N,α(θ,θ̄)(s′) +∇θπmix 
N,α(θ, θ̄)(s)∇ap(s ′ | s,a) |a=πmix 
N,α(θ,θ̄)(s) v πmix N,α(θ,θ̄)(s′) 
) d s′ 
= ∇θπmix N,α(θ, θ̄)(s)∇a 
( r(s,a) + 
∫ S 
γp(s′ | s,a)vπ mix N,α(θ,θ̄)(s′)d s′ 
) |a=πmix 
N,α(θ,θ̄)(s) 
+ 
∫ S 
γp(s′ | s, πmix N,α(θ, θ̄)(s))∇θvπ 
mix N,α(θ,θ̄)(s′)d s′ 
= ∇θπmix N,α(θ, θ̄)(s)∇aQ 
πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) + 
∫ S 
γp(s→ s′, 1, πmix N,α(θ, θ̄))∇θvπ 
mix N,α(θ,θ̄)(s′)d s′ . 
Where p(s→ s′, t, π) denotes the density at state s′ after transitioning for t steps from state s. Iterating this formula leads
Action Robust Reinforcement Learning and Applications in Continuous Control 
to the following result: 
∇θvπ mix N,α(θ,θ̄) = ∇θπmix 
N,α(θ, θ̄)(s)∇aQ πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) 
+ 
∫ S 
γp(s→ s′, 1, πmix N,α(θ, θ̄))∇θπmix 
N,α(θ, θ̄)(s′)∇aQ πmix N,α(θ,θ̄)(s′,a) |a=πmix 
N,α(θ,θ̄)(s′) d s ′ 
+ 
∫ S 
γp(s→ s′, 1, πmix N,α(θ, θ̄)) 
∫ S 
γp(s′ → s′′, 1, πmix N,α(θ, θ̄))∇θvπ 
mix N,α(θ,θ̄)(s′′)d s′′ d s′ 
= ∇θπmix N,α(θ, θ̄)(s)∇aQ 
πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) 
+ 
∫ S 
γp(s→ s′, 1, πmix N,α(θ, θ̄))∇θπmix 
N,α(θ, θ̄)(s′)∇aQ πmix N,α(θ,θ̄)(s′,a) |a=πmix 
N,α(θ,θ̄)(s′) d s ′ 
+ 
∫ S 
γ2p(s→ s′, 2, πmix N,α(θ, θ̄))∇θvπ 
mix N,α(θ,θ̄)(s′)d s′ 
= 
∫ S 
∞∑ t=0 
γtp(s→ s′, t, πmix N,α(θ, θ̄))∇θπmix 
N,α(θ, θ̄)(s′)∇aQ πmix N,α(θ,θ̄)(s′,a) |a=πmix 
N,α(θ,θ̄)(s′) d s ′ . 
Taking the expectation over S1: 
∇θJ(πmix N,α(θ, θ̄)) = ∇θ 
∫ S 
p1(s)vπ mix N,α(θ,θ̄)(s)d s 
= 
∫ S 
p1(s)∇θvπ mix N,α(θ,θ̄)(s)d s 
= 
∫ S 
∫ S 
∞∑ t=0 
γtp1(s)p(s→ s′, t, πmix N,α(θ, θ̄))∇θπmix 
N,α(θ, θ̄)(s′)∇aQ πmix N,α(θ,θ̄)(s′,a) |a=πmix 
N,α(θ,θ̄)(s′) d s ′ d s 
= 
∫ S 
ρπ mix N,α(θ,θ̄)∇θπmix 
N,α(θ, θ̄)(s)∇aQ πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) d s 
= 
∫ S 
ρπ mix N,α(θ,θ̄)∇θ((1− α)µθ(s) + αµ̄θ̄(s))∇aQ 
πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) d s 
= (1− α) 
∫ S 
ρπ mix N,α(θ,θ̄)∇θµθ(s)∇aQ 
πmix N,α(θ,θ̄)(s,a) |a=πmix 
N,α(θ,θ̄)(s) d s 
notice that compared to the standard DPGs (Silver et al., 2014), the gradient is w.r.t. the actor’s (adversary’s) policy and is weighted by 1− α (α). Similar to the DPG, the gradient of the action-value function is taken w.r.t. the action taken (the mixture policy). 
PR-MDP: The PR-MDP, constructed by two deterministic policies µθ and µ̄θ̄ can be defined as follows: 
πmix P,α(u | s; θ, θ̄) = (1− α)δ(u− µθ(s)) + αδ(u− µ̄θ̄(s)). 
vπ mix P,α(θ,θ̄) = 
∫ A 
πmix P,α(u | s; θ, θ̄)Qπ 
mix P,α(θ,θ̄)(s, πmix 
P,α(θ, θ̄)(s))du 
∇θvπ mix P,α(θ,θ̄) = ∇θ 
∫ A 
πmix P,α(u | s; θ, θ̄)Qπ 
mix P,α(θ,θ̄)(s, u)du 
= ∇θ[(1− α)Qπ mix P,α(θ,θ̄)(s, µθ(s)) + αQπ 
mix P,α(θ,θ̄)(s, µ̄θ̄(s))] 
= (1− α)∇θQπ mix P,α(θ,θ̄)(s, µθ(s)) + α∇θQπ 
mix P,α(θ,θ̄)(s, µ̄θ̄(s)) 
we address each element, (1)∇θQπ mix P,α(θ,θ̄)(s, µθ(s)) and (2) Qπ 
mix P,α(θ,θ̄)(s, µ̄θ̄(s)), individually:
Action Robust Reinforcement Learning and Applications in Continuous Control 
(1): 
∇θQπ mix P,α(θ,θ̄)(s, µθ(s)) = ∇ 
( r(s, µθ(s)) + 
∫ S 
γp(s′ | s, µθ(s))vπ mix P,α(θ,θ̄)(s′) 
) d s′ 
= ∇θµθ(s)∇ar(s,a) |a=µθ(s) +∇θ ∫ S 
γp(s′ | s, µθ(s))vπ mix P,α(θ,θ̄)(s′)d s′ 
= ∇θµθ(s)∇θr(s,a) |a=µθ(s) 
+ 
∫ S 
γ ( p(s′ | s, µθ(s))∇θvπ 
mix P,α(θ,θ̄)(s′) +∇θµθ(s)∇ap(s 
′ | s,a) |a=µθ(s) v πmix P,α(θ,θ̄)(s′) 
) d s′ 
= ∇θµθ(s)∇a 
( r(s,a) + 
∫ S 
γp(s′ | s,a)vπ mix P,α(θ,θ̄)(s′)d s′ 
) |a=µθ(s) 
+ 
∫ S 
γp(s′ | s, µθ(s))∇θvπ mix P,α(θ,θ̄)(s′)d s′ 
= ∇θµθ(s)∇aQ πmix P,α(θ,θ̄)(s,a) |a=µθ(s) + 
∫ S 
γp(s→ s′, 1, µθ)∇θvπ mix P,α(θ,θ̄)(s′)d s′ . 
Where p(s→ s′, t, π) denotes the density at state s′ after transitioning for t steps from state s. 
(2): 
∇θQπ mix P,α(θ,θ̄)(s, µ̄θ̄(s)) = ∇θ 
( r(s, µ̄θ̄(s)) + 
∫ S 
γp(s′ | s, µ̄θ̄(s))vπ mix P,α(θ,θ̄)(s′) 
) d s′ 
= ∇θµ̄θ̄(s)∇ar(s,a) |a=µ̄θ̄(s) +∇θ ∫ S 
γp(s′ | s, µ̄θ̄(s))vπ mix P,α(θ,θ̄)(s′)d s′ 
= 
∫ S 
γ ( p(s′ | s, µ̄θ̄(s))∇θvπ 
mix P,α(θ,θ̄)(s′) +∇θµ̄θ̄(s)∇ap(s 
′ | s,a) |a=µ̄θ̄(s) v πmix P,α(θ,θ̄)(s′) 
) d s′ 
= 
∫ S 
γp(s′ | s, µ̄θ̄(s))∇θvπ mix P,α(θ,θ̄)(s′)d s′ . 
Hence: 
∇θvπ mix P,α(θ,θ̄) = (1− α)∇θQπ 
mix P,α(θ,θ̄)(s, µθ(s)) + α∇θQπ 
mix P,α(θ,θ̄)(s, µ̄θ̄(s)) 
= (1− α)∇θµθ(s)∇aQ πmix P,α(θ,θ̄)(s,a) |a=µθ(s) 
+ (1− α) 
∫ S 
γp(s→ s′, 1, µθ)∇θvπ mix P,α(θ,θ̄)(s′)d s′+α 
∫ S 
γp(s′ | s, µ̄θ̄(s))∇θvπ mix P,α(θ,θ̄)(s′)d s′ 
= (1− α)∇θµθ(s)∇aQ πmix P,α(θ,θ̄)(s,a) |a=µθ(s) + 
∫ S 
γp(s′ | s, πmix P,α(θ, θ̄)(s))∇θvπ 
mix P,α(θ,θ̄)(s′)d s′ 
Applying this iteratively:
Action Robust Reinforcement Learning and Applications in Continuous Control 
∇θvπ mix P,α(θ,θ̄) = (1− α)∇θµθ(s)∇aQ 
πmix P,α(θ,θ̄)(s,a) |a=µθ(s) 
+ 
∫ S 
γp(s′ | s, πmix P,α(θ, θ̄)(s))∇θvπ 
mix P,α(θ,θ̄)(s′)d s′ 
= (1− α)∇θµθ(s)∇aQ πmix P,α(θ,θ̄)(s,a) |a=µθ(s) 
+ 
∫ S 
γp(s→ s′, 1, πmix P,α(θ, θ̄))∇θµθ(s′)∇aQ 
πmix N,α(θ,θ̄)(s′,a) |a=µθ(s′) d s 
′ 
+ 
∫ S 
γp(s→ s′, 1, πmix P,α(θ, θ̄)) 
∫ S 
γp(s′ → s′′, 1, πmix P,α(θ, θ̄))∇θvπ 
mix N,α(θ,θ̄)(s′′)d s′′ d s′ 
= (1− α)∇θµθ(s)∇aQ πmix P,α(θ,θ̄)(s,a) |a=µθ(s) 
+ (1− α) 
∫ S 
γp(s→ s′, 1, πmix P,α(θ, θ̄))∇θµθ(s′)∇aQ 
πmix P,α(θ,θ̄)(s′,a) |a=µθ(s′) d s 
′ 
+ 
∫ S 
γ2p(s→ s′, 2, πmix P,α(θ, θ̄))∇θvπ 
mix P,α(θ,θ̄)(s′)d s′ 
= (1− α) 
∫ S 
∞∑ t=0 
γtp(s→ s′, t, πmix P,α(θ, θ̄))∇θµθ(s′)∇aQ 
πmix P,α(θ,θ̄)(s′,a) |a=µθ(s′) d s 
′ . 
Taking the expectation over S1: 
∇θJ(πmix P,α(θ, θ̄)) = ∇θ 
∫ S 
p1(s)vπ mix P,α(θ,θ̄)(s)d s 
= 
∫ S 
p1(s)∇θvπ mix P,α(θ,θ̄)(s)d s 
= (1− α) 
∫ S 
∫ S 
∞∑ t=0 
γtp1(s)p(s→ s′, t, πmix P,α(θ, θ̄))∇θπθ(s′)∇aQ 
πmix P,α(θ,θ̄)(s′,a) |a=πθ(s′) d s 
′ d s 
= (1− α) 
∫ S 
ρπ mix P,α(θ,θ̄)∇θπθ(s)∇aQ 
πmix P,α(θ,θ̄)(s,a) |a=πθ(s) d s 
the resulting gradient update for the actor does not directly take into consideration the policy of the adversary, thus resulting in a gradient rule similar (weighted by (1− α) for the actor and α for the adversary) to that seen in Silver et al. (2014). 
Intuitively, as the action is sampled w.p. (1− α) from the actor and w.p, α from the adversary, each player acts greedily at the immediate step ignoring potential perturbations. The mutual effect of the actor and adversary is attained through the Q value which captures the long term return of the mixture policy.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Algorithm 5 Action-Robust DDPG Input: Actor update steps (N ), uncertainty value α and discount factor γ Randomly initialize critic network Q(s,a;φ), actor f(s; θ) and adversary f̄(s; θ̄) Initialize target networks with weights φ−, θ−, θ̄− 
Initialize replay buffer R for episode in 0...M do 
Receive initial state s0 
for t in 0...T do 
Sample action at = 
{ f(s; θπ) w.p. (1− α) and f̄(s; θπ̄) otherwise , PR-MDP (1− α)f(s; θπ) + αf̄(s; θ̄π̄) , NR-MDP 
ãt = at + exploration noise Execute action ãt and observe reward rt and new state st+1 
Store transition (st, ãt, rt, st+1) in R for i in 0...N do 
Sample batch from replay buffer Update actor: 
θ ← 
{ ∇θ(1− α)Q(s, f(s; θ)) ,PR-MDP ∇θQ(s, (1− α)f(s; θ) + αf̄(s; θ̄)) ,NR-MDP 
Update critic: 
φ← 
{ ∇φ||r + γ[(1− α)Q(s′, f(s′; θ−)) + αQ(s′, f(s′; θ̄−))]||22 ,PR-MDP ∇φ||r + γ[Q(s′, (1− α)f(s′; θ−) + αf(s′; θ̄−))]||22 ,NR-MDP 
end for Sample batch from replay buffer Update adversary: 
θ̄ ← 
{ ∇θ̄αQ(s, f̄(s; θ̄)) ,PR-MDP ∇θ̄Q(s, (1− α)f(s; θ) + αf̄(s; θ̄)) ,NR-MDP 
Update critic Update the target networks: 
θ− ← τθ + (1− τ)θ− 
θ̄− ← τ θ̄ + (1− τ)θ̄− 
φ− ← τφ+ (1− τ)φ− 
end for end for 
Algorithm 5 presents our Action Robust approach adapted to the DDPG algorithm (Lillicrap et al., 2015). The action we play during exploration is based on the exploration scheme selected, OU noise adds noise at the action level whereas in parameter space noise we pertube the parameters θ and θ̄. 
Notice that the critic update is different, in both scenarios, from the default DDPG update rule. The reason is that the critic is updated based on the expectation over the policy, which in the NR-MDP results in the α mixture policy and in the PR-MDP a convex sum of Q values.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Figure 4 presents a block diagram of our approach for the NR-MDP scenario: 
Figure 4. Action Robust DDPG, NR-MDP 
Actor 
+ 
Adversary 
Critic 
Q(s, πmix N (s)) 
s 
s 
µ(s) µ̄(s) 
πmix N (µ, µ̄)(s) 
We improve the actor (adversary) by taking the gradient of Q w.r.t. θ(θ̄) and performing backpropagation through the critic. Autograd engines (Baydin et al., 2018) automatically ensure that the gradients propagate directly to the actor (adversary) without affecting the adversary (actor) or the critic. During exploration we simply play πmix 
N a deterministic policy (as it is a convex sum of two deterministic values). 
For the PR-MDP the schema is similar to the standard DDPG approach. 
Figure 5. Action Robust DDPG, PR-MDP 
Actor 
+ 
Adversary 
s 
µ(s) µ̄(s) 
πmix P (µ, µ̄)(s) 
Figure 5 depicts the block diagram during exploration. πmix P defines a stochastic policy over µ and µ̄. Thus, with probability 
1− α we sample action µ(s) and otherwise µ̄(s).
Action Robust Reinforcement Learning and Applications in Continuous Control 
Figure 6. Action Robust DDPG, PR-MDP 
Actor 
Critic 
Q(s, µ(s)) 
s 
s 
µ(s) 
Figure 6 presents the approach during training. This approach is identical to the standard DDPG approach, except that once taking the gradient∇θQ(s, µθ(s)), we multiply the loss (similar to a change of learning rate) by 1− α. 
The critic is trained on the expectation over the mixture policies, which in the case of DDPG results in Q(s,a) = r(s,a) + γ[(1− α)Q(s′, µ(s′)) + αQ(s′, µ̄(s′))].
Action Robust Reinforcement Learning and Applications in Continuous Control 
E. Empirical Results 
No Noise OU Noise Param Noise 
Figure 7. NR-MDP: exploration and α ablation. 
Figure 8. NR-MDP: α and training ratio ablation.
Action Robust Reinforcement Learning and Applications in Continuous Control 
No Noise OU Noise Param Noise 
Figure 9. PR-MDP: exploration and α ablation. 
Figure 10. PR-MDP: α and training ratio ablation.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Baseline NR-MDP PR-MDP 
Hopper 
Walker2d 
Humanoid 
InvertedPendulum 
Figure 11. Robustness to model uncertainty. Noise probability denotes the probability of a randomly sampled noise being played instead of the selected action.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Baseline NR-MDP PR-MDP 
Swimmer 
HalfCheetah 
Ant 
Figure 12. Robustness to model uncertainty continued. Noise probability denotes the probability of a randomly sampled noise being played instead of the selected action.
Action Robust Reinforcement Learning and Applications in Continuous Control 
Figure 13. Robustness to mass uncertainty.