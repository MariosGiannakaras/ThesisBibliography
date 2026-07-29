> Source: https://papers.nips.cc/paper_files/paper/2018/file/7ec0dbeee45813422897e04ad8424a5e-Paper.pdf

Policy-Conditioned Uncertainty Sets for Robust Markov Decision Processes 
Andrea Tirinzoni Politecnico di Milano 
andrea.tirinzoni@polimi.it 
Xiangli Chen Amazon Robotics 
cxiangli@amazon.com 
Marek Petrik University of New Hampshire 
mpetrik@cs.unh.edu 
Brian D. Ziebart University of Illinois at Chicago 
bziebart@uic.edu 
Abstract 
What policy should be employed in a Markov decision process with uncertain parameters? Robust optimization’s answer to this question is to use rectangular uncertainty sets, which independently reflect available knowledge about each state, and then to obtain a decision policy that maximizes the expected reward for the worst-case decision process parameters from these uncertainty sets. While this rectangularity is convenient computationally and leads to tractable solutions, it often produces policies that are too conservative in practice, and does not facilitate knowledge transfer between portions of the state space or across related decision processes. In this work, we propose non-rectangular uncertainty sets that bound marginal moments of state-action features defined over entire trajectories through a decision process. This enables generalization to different portions of the state space while retaining appropriate uncertainty of the decision process. We develop algorithms for solving the resulting robust decision problems, which reduce to finding an optimal policy for a mixture of decision processes, and demonstrate the benefits of our approach experimentally. 
1 Introduction 
Policies with high expected reward are often desired for uncertain decision processes with which little experience exists. Specifically, we consider the setting in which only a limited number of trajectories from a sub-optimal control policy through a decision process are available. Robust control approaches for this task [1, 2, 3, 4] define uncertainty sets for the decision process based on the limited outcome samples and seek the policy that maximizes this expected reward for the worst possible choice of decision process parameters in these sets. 
When the uncertainty sets relating to different decision process states are jointly constrained in seemingly natural ways, the robust control problem becomes NP-hard (e.g., [5, 6]). To avoid these computationally intractable robust control problems, uncertainty sets have often been independently constructed for parameters associated with a particular state-action pair or particular state—s, a-rectangularity or s-rectangularity [7, 8, 4], respectively. Unfortunately, independently assuming the worst-case in every encountered state is often too conservative in practice to be useful [9]. 
Leveraging ideas from distributionally robust optimization [10, 11, 12], we construct policyconditioned marginal uncertainty sets for robustly learning a decision policy that optimizes the reward given trajectory samples produced by a sub-optimal policy. State transition dynamics under our formulation are estimated based on two competing objectives. First, the estimated dynamics must 
32nd Conference on Neural Information Processing Systems (NeurIPS 2018), Montréal, Canada.
(approximately) match measured properties observed under the sub-optimal reference policy. Second, the estimated dynamics must be the worst case for the simultaneously-hypothesized optimal policy. 
This formulation has three main benefits: (1) Non-rectangularity: Our uncertainty sets are defined by feature-based statistics of distributions over entire trajectories, enabling generalization across states; (2) Off-policy robustness: We define our performance objective using the desired control policy and the uncertainty set using the sub-optimal data generation policy; and (3) Convex parameter optimization: We avoid the nonconvex parameter optimization pitfalls of other nonrectangular formulations by shifting the main computational difficulties to parameterized prediction/control problems (which can be efficiently approximated). Together, these properties aid in addressing a number of existing concerns for robust control, including settings in which the state definition violates the Markov assumption [13] or the transition probabilities are derived from limited data sets [3, 9]. 
In the remainder of this paper, we review existing robust control methods and directed information theory concepts in Section 2. Using these concepts, we formulate the robust control task using feature-based marginal constraints in Section 3. We reformulate this problem and present algorithms for solving it using a combination of convex optimization and dynamic programming to optimize a non-Markovian mixed decision process optimal control problem that arises from the formulation. We evaluate our approach in Section 4 to demonstrate its comparative benefits over rectangular robust control methods. Lastly, we provide concluding thoughts and discuss future work in Section 5. 
2 Background and Related Work 
2.1 Robust control 
The Markov Decision Process (MDP) with state set S and action setA povides a common formulation of discrete control problems. In the MDP, the transition probabilities are given by τ(st+1 | st, at) and the reward is R(st, at, st+1). Though consideration is often restricted to deterministic Markovian policies, π : S → A, the generalization to randomized Markovian policies ΠM = {π : S → ∆A} provides stochastic mappings from the current state to actions. Even more generally, we will consider non-Markovian, history-dependent, randomized policies ΠH = {π : St ×At → ∆A} in this work. 
The expected sum of rewards or return ρ of a policy π applied to an MDP with dynamics τ and reward function R is: ρR(π, τ) = Eτ,π[ 
∑T−1 t=1 R(St, At, St+1)]. For decision problems, the standard 
objective is to choose a policy that maximizes the expected sum of rewards: maxπ ρR(π, τ). Since a Markovian and deterministic policy always exists that maximizes this quantity, one with those characteristics is typically sought when solving this optimization problem by many well-known algorithms, such as value iteration or policy iteration [14]. 
Unfortunately, in many settings the dynamics τ are not entirely known. Control policies are needed that can perform well despite this uncertainty about the decision process. One option is to formally define the uncertainty as a set of possibilities and assume the worst case (Definiton 1). Definition 1. The robust control problem is to find a control policy π ∈ Π that performs best for the worst-case choice of state transition dynamics, τ ∈ Ξ: 
max π∈Π 
min τ∈Ξ 
ρ(π, τ) = max π∈Π 
min τ∈Ξ 
Eτ,π 
[ T−1∑ t=1 
R(St, At, St+1) 
] . (1) 
The specification of the uncertainty set(s), Ξ, has significant implications for the tractability of this problem. Robust MDPs [7] are typically used to represent uncertainty in transition probabilities and rewards in regular MDPs. When the state-transition probabilities for different states are jointly constrained in arbitrary ways, the robust control problem becomes NP-hard [5, 6]. Two common forms of constraints that enable efficient solutions are s,a-rectangular and s-rectangular [4] constraint sets. This form arises when transition probabilities are not known precisely, but are known to be bounded in terms of an L1 norm. A corresponding robust MDP has uncertain transition probabilities: 
Ξ = {τ : ∀s, a ∈ S ×A, ‖τ(·|s, a)− p(· | s, a)‖1 ≤ c}. This is an s, a-rectangular set. It employs independent constraints for each state-action pair or state (s-rectangular set). A convenient way to model a robust MDP is to introduce a set of outcomes B to represent the uncertainty in transitions and rewards. The transition probabilities are then defined 
2
as p(st+1 | st, at, bt) and rewards become r(st, at, bt, st+1), while ξ(bt|st, at) denotes the nature’s policy, i.e., a distribution over outcomes. 
The optimal value function v? in a robust MDP with s-rectangular and s, a-rectangular uncertainty sets (and discount factor γ) satisfies the Bellman optimality equation for each s ∈ S as follows: 
v?(s) = max π∈Π 
min ξ∈Ξ 
∑ 
a∈A 
∑ 
b∈B 
π(a|s)ξ(b|s, a) ( r(s, a, b, s′) + γ 
∑ 
s′∈S p(s′ | s, a, b)v?(s′) 
) . (2) 
In our formulation, we consider state-action feature-based constraints over the marginals of stateaction sequences to define our uncertainty sets. When the sum of rewards and the constraints are defined in terms of different policies, this naturally induces a “belief state” that is similar to the augmenting set of outcomes B previously described. In our case, this augmenting information tracks the relative significance of the policies for providing robustness based on the sum of rewards versus matching feature-based measurements from training trajectories. 
2.2 Directed information theory for processes 
We make extensive use of ideas and notation from directed information theory [15, 16, 17, 18, 19]. Under this theory, processes—the products of T conditional probabilities over a sequence of T variables—are treated as first-order objects. The causally conditioned probability distribution [20], p(y1:T ||x1:T ) , 
∏T t=1 p(yt|y1:t−1,x1:t), illustrates the notation for this process of generating the 
sequence of y1:T variables given the sequence of x1:T variables. It differs from the conditional probability distribution, p(y1:T |x1:T ) = 
∏T t=1 p(yt|x1:T ,y1:t−1), in the limited history of x variables 
each yt variable is conditioned upon. 
Both (stochastic) control policies, π(a1:T ||s1:T ) , ∏T t=1 π(at|a1:t−1, s1:t), and (stochastic) state 
transition dynamics, τ(s1:T ||a1:T−1) , ∏T t=1 τ(st|s1:t−1,a1:t−1), can be expressed using this 
notation. The joint probability distribution over states and actions is then p(a1:T , s1:T ) = π(a1:T ||s1:T )τ(s1:T ||a1:T−1), and the expected reward can be expressed as an affine combination of bilinear functions of these processes: 
ρR(π, τ) = ∑ 
a1:T 
∑ 
s1:T 
π(a1:T ||s1:T )τ(s1:T ||a1:T−1) 
T−1∑ 
t=1 
R(st, at, st+1). (3) 
Additionally, the uncertainty of state sequence outcomes can be quantified using the causally conditioned entropy: 
Hτ,π(S1:T ||A1:T−1) = − ∑ 
a1:T ,s1:T 
π(a1:T ||s1:T )τ(s1:T ||a1:T−1) log τ(s1:T ||a1:T−1). (4) 
Of crucial importance for optimization purposes, the set of causally conditioned probability distributions is convex and the causal entropy is a convex function of those probabilities [21]. 
3 Marginally-Constrained Robust Control Processes 
We define constraints on uncertainties about a decision process based on its interactions with a reference policy. In other words, state-action trajectories through the decision process are available that were produced from a policy that may be quite different from the optimal one. Similarly to previous works [5, 22], we propose practical algorithms for this problem by augmenting the state space. 
3.1 Defining Uncertainty Sets with Marginal Features 
We consider a feature function φ : S ×A× S → Rd characterizing the relationships between states and actions to restrict the set of possible realizations of uncertain MDP parameters. We denote the first moment of the occupancy frequencies with respect to φ (also known as feature expectations in the inverse reinforcement learning literature [23, 24]) as κφ(π, τ) := Eτ,π 
[∑T−1 t=1 φ(St, At, St+1) 
] , 
while we denote the empirical sample statistics, which are measured from N sample trajectories, 
3
as κ̂ = 1 N 
∑N i=1 
∑T−1 t=1 φ(s 
(i) t , a 
(i) t , s 
(i) t+1). Based on these quantities, we can now define the robust 
control problem with constraints using marginal statistics of the state-action sequence to define the uncertainty set Ξ. Definition 2. The marginally-constrained robust control problem given reference policy π̃ is: 
max π∈Π 
min τ∈Ξ 
ρ(π, τ)− 1 
λ Hτ,π̄(S1:T ||A1:T−1), (5) 
where Ξ is the set of all transition probabilities whose feature expectations match the empirical sample statistics, i.e., Ξ = {τ | κφ(π̃, τ) = κ̂}. In general, and of practical significance, slack can also be added to the constraints, leading to a relaxed uncertainty set Ξ̃ = {τ | ||κφ(π̃, τ)− κ̂|| ≤ β}1. We include an optional causal entropy (Equation 4) regularization penalty term, 1 
λHτ,π̄(S1:T ||A1:T−1), where λ ∈ (0,∞) is a provided parameter and π̄(a1:T ||s1:T ) is an arbitrary distribution. 
Intuitively, our formulation allows constraints for whole trajectories rather single state-action pairs, as with rectangular constraints. Furthermore, features φ allow us to specify properties of the unknown transition dynamics that generalize globally across the state-action space, which is not possible using local constraints, such as rectangular ones. When limited data is available and generalization is therefore required to achieve good performance, this constitutes a significant advantage. Finally, our optional entropy regularization term leads to smoother solutions, where the smoothness is controlled by parameter λ. Many previous works have shown the benefits of having entropy-based smoothing [2, 25]. 
In practice, the design of the feature function φ is fundamental for properly constraining the estimated transition probabilities. Although a specific choice is highly application dependent, the features should in general encode known properties of the underlying MDP. Since our solution reduces to finding dynamics that induce a behavior on the reference policy, specified through κφ, that approximately matches the one observed from the given trajectories, many analogies exist with feature design in the IRL literature (see, e.g., chapter 6 of [26]). Common choices thus include indicator functions over important properties/events, such as reaching certain goal states, entering dangerous zones, taking very likely (or unlikely) transitions, and so on. The key consequence of adding these kinds of features is that the probability of these events occurring under the estimated dynamics will be (approximately) the same as the one observed in the given trajectories. Consider, for instance, an MDP where s, a, s′ triples with some known property P(s, a, s′) have zero probability (e.g., in a gridworld or a chain-walk domain, a transition is impossible if s and s′ are not adjacent). Then, using a feature φ(s, a, s′) = 1[P(s, a, s′)], i.e., an indicator function over P , will constrain the estimated transition probabilities to be zero for all triples where such property holds. In fact, κφ(τ, π̃) = 0 and κ̂φ = 0 for any reference policy. More generally, most MDPs of practical interest have properties that couple the transition probabilities of several state-action pairs. Capturing these global properties using moment-based constraints is typically much better than focusing on single states or state-action pairs, which is more prone to overfitting the given trajectories. In the limiting case, one could consider a separate feature (e.g., an indicator) over each s, a, s′ triple. However, similarly to rectangular solutions, having separate constraints for different state-action pairs is likely to lead to very conservative solutions in the presence of limited data. Finally, notice that using an indicator function over each s, a, s′ triple is equivalent to matching the (empirical) joint distribution p(St, At, St+1) induced by the reference policy and the true dynamics. Thus, even when we consider a different constraint for each triple, our solution implicitly couples the transition probabilities of different state-action pairs and differs from a rectangular formulation which focuses on matching the conditional distribution p(St+1|St, At). 
A key characteristic of this formulation is the difference in control policies: the expected reward is defined in terms of π, while the constraints are defined in terms of π̃. Unfortunately, treating the marginally-constrained robust control problem (Definition 1) as an optimization problem over the individual state transition probabilities, τ(st+1|st, at), appears daunting. This is because the constraints in Equation (5) are not convex functions of those transition probabilities. We instead consider optimizing the control policy and state transition dynamics as causally conditioned probability distributions in the following section. Though the solution for this formulation does not naturally have a Markovian property, our process estimation leads to an augmented-Markovian representation in Section 3.3. 
1Notice that τ must also belong to the set of valid probability distributions. We omit the corresponding constraints for the sake of clarity. 
4
3.2 Reformulation as Process Estimation 
We re-express the optimization problem of Definition 2 using processes—the causally conditioned probabilities of Section 2.2—for the control policy π(a1:T−1||s1:T−1) and state transition dynamics τ(s1:T ||a1:T−1), which conveniently combine the individual conditional probabilities over the stateaction sequence. Notice that we consider stochastic processes ending with a state at time T and an action at time T − 1. Using this new notation, we now reformulate our main optimization problem in a more convenient manner. Theorem 1. The marginally-constrained robust control problem of Definition 2 can be solved by posing it as an unconstrained zero-sum game parameterized by a vector of Lagrange multipliers, ω: 
max ω∈Rd 
max π∈Π 
softmin τ∈Ξ 
( Eτ,π 
[ T−1∑ 
t=1 
R(St, At, St+1) 
] + Eτ,π̃ 
[ T−1∑ 
t=1 
ω · φ(St, At, St+1) 
]) −ω·κ̂, (6) 
where softminx∈X f(x) = − 1 λ log 
∑ x∈X e 
−λf(x) and · denotes the dot product. 
The proof is given in Appendix A. Notice that Theorem 1 holds for the slack-free uncertainty set Ξ of Definition 2. Using the slack-based version leads to regularization of the dual parameters ω. As shown by [27], adding l1 regularization −β||ω||1 to the dual objective is equivalent to a constraint ||κφ(π̃, τ) − κ̂||1 ≤ β in the primal, while adding l22 regularization −α2 ||ω||22 is equivalent to an l22 potential on the constraint values in the primal. In practice, it is important to add l1 and/or l22 regularization to ensure proper convergence of the algorithm. Both types of regularization enjoy similar theoretical guarantees [28]. 
We now address the inner minimax game for choosing τ and π in Section 3.3 and the outer optimization of ω from Equation (6) in Section 3.4. 
3.3 Mixed Objective Minimax Optimal Control 
Choosing state transition dynamics to optimize a mixture of expected returns under different control policies, π and π̃ (Definition 3)2 is an important subproblem arising from our formulation of robust control as a process estimation task with robustness properties and uncertainty sets defined by different control policies. To the best of our knowledge, this problem has not been previously investigated in the literature. Definition 3. Given two control policies π and π̃, and two reward functions R and R̃, the mixed objective optimization problem seeks state transition dynamics τ that minimizes a mixture of these weighted by θ ≥ 0 : minτ {θρR(π, τ) + (1− θ)ρR̃(π̃, τ)}. 
Notice that the inner minimization of Equation (6) is an entropy-regularized instance of this problem. In fact, we can set R̃(st, at, st+1) ← ω · φ(st, at, st+1) and θ = 1 
2 (provided that rewards are properly rescaled). As we already know from Theorem 1, the entropy leads to a softmin solution and does not pose any additional complication in solving the optimization problem of Definition 3. Furthermore, in the inner zero-sum game of Equation (6), π is chosen as the maximizer of ρ(π, τ). Thus, we can see Definition 3 as a special case where π is fixed rather than chosen dynamically. 
An important observation for this problem is that the optimal transition dynamics are not Markovian. Indeed, the influence of ρR and ρR̃ on choosing the next-state distribution at some decision point depends on how probable it is for that decision point to be realized under π and under π̃. This, in turn, depends on the entire history of states and actions leading to the current decision point. However, we establish that this non-Markovian problem can be Markovianized by augmenting the current state-action pair with a continuous “belief state” as follows: 
b(a1:t||s1:t) , 
∏t i=1 π(ai|a1:i−1, s1:i)∏t 
i=1 π(ai|a1:i−1, s1:i) + ∏t i=1 π̃(ai|a1:i−1, s1:i) 
= π(a1:t||s1:t) 
π(a1:t||s1:t) + π̃(a1:t||s1:t) . (7) 
The belief state tracks the relative probability of the decision point under π and π̃. Defining it in this manner is convenient because it limits the domain for b to [0, 1]. It can also be updated to incorporate 
2Without any loss of generality, this problem could be equivalently posed as finding the control policy π that maximizes a mixture of rewards θρR(π, τ) + (1− θ)ρR̃(π, τ̃) for two different decision processes with dynamics/reward (τ,R) and (τ̃ , R̃). 
5
a new action at+1 in state st+1 as: 
b(a1:t+1||s1:t+1) = b(a1:t||s1:t)π(at+1|a1:t, s1:t+1) 
b(a1:t||s1:t)π(at+1|a1:t, s1:t+1) + (1− b(a1:t||s1:t))π̃(at+1|a1:t, s1:t+1) . (8) 
Augmenting with the belief state of Equation (7), we prove that it is possible to compute a Markovian solution to the inner zero-sum game of Equation (6) and, thus, to the optimization problem of Definition 3. Theorem 2. Let π̃ be a given randomized Markovian policy and Z(st, at, bt−1) = bt−1 + (1 − bt−1)π̃(at|st), where bt is the belief state defined in Equation (7). Then, a solution (π∗, τ∗) to the inner zero-sum game of Equation (6) is: 
τ∗(st+1|st, at, bt) = e−λQ(st,at,bt,st+1)∑ s′ e −λQ(st,at,bt,s′) 
; π∗(st, bt−1) = argmax at 
QR 
( st, at, 
bt−1 
Z(st, at, bt−1) 
) , (9) 
with Q as the value of a transition to state st+1, V as the value of state st and belief state bt−1, and QR as the expected return from R obtained by taking action at in state st and belief state bt: Q(st, at, bt, st+1) = btR(st, at, st+1) + (1− bt)R̃(st, at, st+1) + V (st+1, bt), (10) 
V (st, bt−1) = Z′(st, bt−1) softmin st+1 
Q 
( st, π 
∗(st, bt−1), bt−1 
Z′(st, bt−1) , st+1 
) , (11) 
QR(st, at, bt) = ∑ st+1 
τ∗(st+1|st, at, bt) 
( R(st, at, st+1) +QR 
( st+1, π 
∗(st+1, bt), bt 
Z′(st+1, bt) 
)) (12) 
where Z ′(st, bt−1) = Z(st, π ∗(st, bt−1), bt−1). 
The proof is given in Appendix A. 
Since we have a maximum causal entropy estimation problem, τ∗ (Equation 9) takes the form of a Boltzmann distribution with temperature λ−1 and energy given by Q(st, at, bt, st+1). Function Q (Equation 10) specifies the value of a transition from st, at, bt to state st+1. Intuitively, it is a sum of (i) the immediate return, which in turn is a mixture of rewards from R and R̃ weighted by the current belief state, and (ii) the value of the next state st+1 given that the current belief is bt. We have the additional complication that π is chosen dynamically as the maximizer of ρR(π, τ) rather than statically. Given τ∗, the optimal policy π∗ (Equation 9) aims at maximizing the expected future return from R defined in (12). Notice that since the optimal policy π∗ is deterministic and π̃ is Markovian, the belief state update rule of (8) can be written in the more concise form: bt+1 = bt 
Z′(st+1,bt) . Finally, 
given τ∗ and π∗, we can compute the optimal value V obtained from state st and belief state bt−1 as defined in (11). Algorithm 1 summarizes our Markovian dynamic program. 
Algorithm 1 Min-max Dynamic Programming Require: Reference policy π̃, reward function R(st, at, st+1), feature function φ(st, at, st+1), Lagrange multiplier ω, entropy regularization weight λ 
Ensure: Robust dynamics τ∗, optimal policy π∗ 
V (sT , bT−1)←0; R̃(st, at, st+1)←ω ·φ(st, at, st+1) for t = T − 1 to 1 do 
Set Q(st, at, bt, st+1) from V using (10) Set τ∗(·|st, at, bt) ∝ e−λQ(st,at,bt,·) 
Set QR(st, at, bt) from τ∗ and QR using (12) Set π∗(st, bt−1) = argmaxat QR(st, at, bt) Set V (st, bt−1) from Q and π∗ using (11) 
end for 
In contrast to typical value iteration in discrete MDPs, the belief states are continuous variables in Algorithm 1. In practice, we discretize them by considering a set B of values in the range [0, 1] and then interpolate between these points. Notice that since π∗ is deterministic, values in (0, 0.5) are not possible and can be safely neglected. This discretization allows for a compact tabular representation of all functions defined in Theorem 2. The asymptotic complexity of this procedure (Algorithm 1) is then O(|S|2|A| |B| T ). 
The robust policy π∗ returned by Algo-rithm 1 is, for each time-step t, a function π∗t : S × B → A mapping state-belief state couples to actions. For the sake of completeness, we show how such a policy can be used in a regular MDP with dynamics τ . Notice that, since belief states are updated according to Equation (8), we need to keep track of the reference policy π̃. At the first time-step, state s1 is drawn from the MDP’s initial state distribution, while the initial belief state b0 is set to 0.5, as can be seen from Equation (7). Then, action a1 = π∗1(s1, b0) is taken, and the system transitions to the next state s2 ∼ τ(·|s1, a1). Finally, the belief state is updated to account for the choice of action a1: b1 = b0 / N(s1, b0). Then, this process is repeated until the maximum time-step is reached. 
6
3.4 Parameter Optimization 
Standard gradient-based methods can be used to optimize the choice of model parameters ω, since the unconstrained dual objective function is a concave function of ω. Any such method is required to repeatedly solve the inner minimax problem of Equation (6) as specified in the previous section, obtaining (π∗, τ∗), compute the feature expectations of the reference policy π̃ under τ∗, and use these to update ω. Conceptually, model parameters ω are chosen to motivate the adversary’s dynamics to satisfy the constraints from the reference policy—(approximately) matching the state-action feature statistics of the training trajectories. Hence, under the assumption that matching features is feasible, following the gradient update rule, ωi+1 ← ωi + ηi(κφ(π̃, τ∗)− κ̂), converges when the statistics match, i.e., when κφ(π̃, τ∗) = κ̂3. 
Computing the expected features under the adversary’s non-Markovian dynamics, τ∗, requires an extension of the dynamic programming algorithm used to obtain τ∗ itself. The next result follows almost straightforwardly from Theorem 2. For the sake of completeness, we include a proof in Appendix A. 
Corollary 1. Let (π∗, τ∗) be the belief-augmented solution of Theorem 2, p(s1) be the initial state distribution of the given MDP, and π̃ be a randomized Markovian policy. Then: 
κφ(π̃, τ∗) = ∑ 
s1 
p(s1)Ψ(s1, b0), (13) 
where Ψ is defined recursively for t = 1, . . . , T − 1 as: 
Ψ(st, bt−1) = ∑ 
at 
π̃(at|st) ∑ 
st+1 
τ∗(st+1|st, at, bt) [φ(st, at, st+1) + Ψ(st+1, bt)] , (14) 
with Ψ(sT , bT−1) = 0 and bt = bt−1 
Z(st,at,bt−1)1 [at = π∗(st, bt−1)]. 
Notice that the computation of κφ(π̃, τ∗), as given by Corollary 1, can be efficiently included in the dynamic program of Algorithm 1 by updating Ψ as the last step of each iteration according to (14). 
4 Experiments 
In this section, we empirically evaluate our robust approach for control using uncertainty sets defined by marginal state-action statistics. We consider two different experiments. The first one is a classic grid navigation problem and the second one is a more challenging domain in which the goal is to control the population change of an invasive species. In all experiments, we compare our marginallyconstrained approach (MC) to three other methods for estimating the state-transition dynamics: (1) a supervised approach using logistic regression (LR); (2) a robust MDP with s,a-rectangular uncertainty sets (RECT); and (3) a simple maximum likelihood estimation (MLE) of the conditional transition probabilities for all state-action pairs. Furthermore, due to the similarity between our settings and batch reinforcement learning, we also compare to fitted Q-iteration (FQI) [29]. 
4.1 Gridworld 
We consider an agent navigating through an N ×N grid in order to reach a goal position. The agent’s location is described by its horizontal and vertical coordinates (x, y). At each time-step, the agent can attempt to move in each of the four cardinal directions. With probability p = 0.3, the action fails and the agent moves in a random direction instead. Attempts to move off the grid have no effect. The agent’s initial position is (1, 1), while the goal is to reach state (N,N). The horizon is set to T = 2N , while the reward function is the negative l1 distance between the next state and the goal. 
In this experiment, we prove the generalization capabilities of our approach. We consider a sequence of gridworlds with increasing size. For each of them, we collect 50 trajectories under a uniform reference policy and we run all algorithms on such data. Intuitively, for small grids, such trajectories provide enough exploration to allow all methods to accurately approximate the state-transition 
3When l1 or l22 regularization of ω is used, this procedure converges when the feature expectations are close to the sample statistics, where the closeness depends on the amount of regularization used (see Section 3.2). 
7
8 10 12 14 16 
−800 
−600 
−400 
−200 
Grid Size 
E x p ec te d R et u rn 
Optimal LR MLE FQI 
RECT MC 
(a) 
8 10 12 14 16 
−800 
−600 
−400 
−200 
Grid Size 
E x p ec te d R et u rn 
Optimal LR MLE RECT MC 
(b) 
20 40 60 80 
0 
0.5 
1 
1.5 
2 
Number of Belief States 
A p p ro x im 
at io n E rr or 
Uniform π̃ Random π̃ 
(c) 
Figure 1: Results of the gridworld experiments, each with 95% confidence intervals. (a) Expected return under the true dynamics as a function of the grid size. (b) Expected return under the estimated (robust) dynamics as function of the grid size. (c) Approximation error incurred by our algorithm due to the discretization of the belief space. 
dynamics. However, as the grid grows larger, only a small portion of the state-space is observed in the training data. Thus, generalization is required to achieve good performance. Additional details on the adopted parameters are given in Appendix C.1. 
Figure 1a shows the expected return achieved by all algorithms as a function of the grid size N . Results are averaged over 20 runs. As expected, for small grids (e.g., N ≤ 7) all approaches obtain nearly-optimal performance. However, as the grid size increases, only our method is able to estimate dynamics that generalize across unseen regions of the state-space, thus maintaining nearly-optimal performance. FQI is also able to generalize and achieves a significant improvement over the other alternatives, but is not able to compete with our method due to the small number of trajectories available. LR is likely to estimate very optimistic dynamics, thus leading to worse performance. Finally, RECT obtains results comparable to LR even without generalizing. However, rectangular uncertainty sets are too conservative to compete with our method. To better demonstrate this fact, Figure 1b shows the performance achieved by the optimal policy computed by each algorithm under their own estimated dynamics (except for FQI, which is model-free). We clearly notice that the worst-case expected return obtained by the rectangular solution is, as claimed, very conservative. Our approach, on the other hand, shows robust performance comparable to the true ones of the other methods. Due to their optimistic estimates, both LR and MLE obtain an expected return even larger than the optimal one. 
Finally, we analyze the approximation error incurred from discretizing the belief states in our approach. We consider a 5× 5 gridworld with the same parameters as before and run the dynamic program of Algorithm 1 for 50 random values ofw using two different reference policies: the uniform one and a random one. Figure 1c shows the average absolute deviation of the objective function from its true value as a function of the number of discrete belief states Nb. Since, as we can observe from (7), the total number of belief states that are reachable in a finite horizon depends on the number of different probability values assigned by π̃, the uniform reference policy achieves a very small approximation error even with few belief states. Interestingly, the approximation error for a random reference policy, which can be regarded as a ’worst-case’ scenario, can also be reduced using a relatively small number of belief states. 
4.2 Invasive Species 
We next consider modeling the population change of an invasive species in an ecosystem with a single action available for mitigating its spread (e.g., introducing a predator). Our starting point is a state-space model with exponential dynamics adapted from Chapter 5 of [30]. Each state captures the current abundance of the invasive species, which we denote as Nt at time t. The population evolves according to exponential dynamics, so that Nt+1 = min{νtNt,K}, where K is the maximum carrying capacity. The growth rate ν depends on (i) whether the control action at has been applied, (ii) the current population level Nt, and (iii) random noise. When the control action is not applied (at = 0), the growth rate is: νt = max{0, ν̄ + N (0, σ2 
ν)}, where ν̄ is the mean growth rate. In this case, the growth rate is independent of the current population level. When the control action is applied (at = 1), the growth rate is: νt = ν̄ − β1Nt − β2 max{0, Nt − N̂}2 +N (0, σ2 
ν), where 
8
Table 1: Negative expected return for different numbers of trajectories M and reference policy’s control probabilities p in the invasive species experiment. Each value is the average of 20 independent runs. 95% confidence intervals are shown. The best algorithms are highlighted in bold. 
Alg. M p = 0.1 p = 0.2 p = 0.3 p = 0.4 p = 0.5 
MLE 50 121.74± 0.82 128.34± 2.06 140.36± 1.28 147.189± 1.78 149.82± 2.12 LR 50 152.95± 13.5 106.77± 2.21 117.43± 5.09 122.756± 5.94 123.28± 4.82 MC 50 99.37± 0.96 102.38± 1.82 98.36± 0.78 107.39± 3.44 124.47± 1.81 RECT 50 111.91± 5.33 107.71± 4.13 117.15± 6.76 123.55± 7.95 142.26± 8.28 FQI 50 140.85± 6.11 133.08± 5.36 133.77± 4.70 134.05± 6.22 140.25± 5.04 
MLE 100 120.91± 0.63 125.21± 1.25 134.23± 1.33 140.96± 1.76 145.42± 1.72 LR 100 169.27± 8.72 104.70± 3.43 110.09± 2.57 114.23± 2.49 124.53± 4.98 MC 100 98.25± 0.88 103.66± 1.05 96.20± 0.95 105.17± 1.95 115.04± 6.18 RECT 100 100.98± 3.33 103.80± 3.22 108.69± 4.95 106.18± 4.02 136.24± 8.41 FQI 100 126.66± 5.84 121.93± 6.27 119.85± 4.30 125.65± 5.08 131.51± 4.92 
β1 and β2 are the coefficients of effectiveness and N̂ is the population at which the effectiveness peaks. That is, the effectiveness of the control method may increase or decrease depending on the population of the invasive species. This dependence is modeled using a simplified quadratic spline. The precise population Nt of the species cannot be directly observed. Instead, one can observe a noisy estimate yt = Nt +N (0, σ2 
y). The exact values of the parameters used in this experiment are K = 500, T = 100, K̂ = 300, ν̄ = 1.02, β1 = 0.001, β2 = −0.0000021, σ2 
ν = 0.02, σ2 y = 20. 
Notice that due to its highly unstable dynamics and noisy observations, this domain represents a very challenging control problem. 
In this experiment, we analyze the behavior of all algorithms when given different amounts of trajectories collected under different reference policies. In particular, we consider five reference policies, where each chooses to apply the control action with a fixed probability p ∈ {0.1, 0.2, 0.3, 0.4, 0.5}. For each reference policy, we generate two datasets of M1 = 50 trajectories and M2 = 100 trajectories, respectively. Additional details are given in Appendix C.2. 
Results of our experiments in these settings are reported in Table 1. Each datapoint is obtained as the result of an average over 20 runs, We notice that MC outperforms all alternatives when p < 0.5 and M = 50. As before, this is due to its generalization capabilities. When considering M = 100 trajectories, all other approaches significantly improve their performance. However, MC is still able to achieve better results for most values of p. The rectangular solution (RECT) also achieves good performance, but shows a much higher variability. Finally, we note that all algorithms suffer from the very limited exploration provided by a reference policy with p = 0.5. In such cases, the performance of the feature-based approaches are superior. 
5 Conclusion & Future Work 
In this paper, we have proposed a new approach to robust control based on causally conditioned probability distribution estimation that defines uncertainty sets using features of the interaction with the decision process with a different policy. Though the solution to the corresponding robust control problem is non-Markovian, we show that it can be closely approximated by augmenting the typical Markovian robust MDP formulation [31, 5] with a continuous-valued “belief state” that can then be discretized. We have empirically tested our approach on a synthetic experiment and a real-world control problem, highlighting its advantages over methods that form rectangular uncertainty sets. 
We plan to extend our formulation to incorporate constraints that are obtained from multiple separate reference control policies. This could also allow episodic reinforcement learning [32] where the robust optimal control policy is employed and then updated based on the trajectories that are observed from its application. Incorporating more sophisticated ideas for solving POMDPs using belief state compression will likely be required, since discretizing the belief space scales poorly with the number of different reference policies. 
9
Acknowledgments 
We thank the anonymous reviewers whose comments helped to improve the paper significantly. This work was supported, in part, by the National Science Foundation under Grant No. 1652530 and Grant No. 1717368, and by the Future of Life Institute (futureoflife.org) FLI-RFP-AI1 program. 
References [1] J. Andrew (Drew) Bagnell. Learning Decisions: Robustness, Uncertainty, and Approximation. 
PhD thesis, Carnegie Mellon University, Pittsburgh, PA, August 2004. 
[2] A. Nilim and L. El Ghaoui. Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005. 
[3] Grani Adiwena Hanasusanto and Daniel Kuhn. Robust data-driven dynamic programming. In Advances in Neural Information Processing Systems, pages 827–835, 2013. 
[4] Wolfram Wiesemann, Daniel Kuhn, and Berç Rustem. Robust markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013. 
[5] Shie Mannor, Ofir Mebel, and Huan Xu. Lightning does not strike twice: Robust mdps with coupled uncertainty. In Proceedings of the 29th International Conference on Machine Learning, ICML 2012, Edinburgh, Scotland, UK, June 26 - July 1, 2012, 2012. 
[6] J. Andrew (Drew) Bagnell, Andrew Y. Ng, and Jeff Schneider. Solving uncertain markov decision problems. Technical Report CMU-RI-TR-01-25, Carnegie Mellon University, Pittsburgh, PA, August 2001. 
[7] Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005. 
[8] Yann Le Tallec. Robust, Risk-Sensitive, and Data-driven Control of Markov Decision Processes. PhD thesis, MIT, 2007. 
[9] Marek Petrik, Mohammad Ghavamzadeh, and Yinlam Chow. Safe Policy Improvement by Minimizing Robust Baseline Regret. In Advances in Neural Information Processing Systems, 2016. 
[10] Erick Delage and Yinyu Ye. Distributionally robust optimization under moment uncertainty with application to data-driven problems. Operations research, 58(3):595–612, 2010. 
[11] Huan Xu and Shie Mannor. Distributionally robust markov decision processes. In Advances in Neural Information Processing Systems, pages 2505–2513, 2010. 
[12] Wolfram Wiesemann, Daniel Kuhn, and Melvyn Sim. Distributionally robust convex optimization. Operations Research, 62(6):1358–1376, 2014. 
[13] Marek Petrik and Dharmashankar Subramanian. RAAM : The benefits of robustness in approximating aggregated MDPs in reinforcement learning. In Neural Information Processing Systems (NIPS), 2014. 
[14] Martin L Puterman. Markov decision processes: Discrete stochastic dynamic programming. John Wiley & Sons, Inc., 2005. 
[15] G. Kramer. Directed Information for Channels with Feedback. PhD thesis, Swiss Federal Institute of Technology (ETH) Zurich, 1998. 
[16] Hans Marko. The bidirectional communication theory – a generalization of information theory. In IEEE Transactions on Communications, pages 1345–1351, 1973. 
[17] James L. Massey. Causality, feedback and directed information. In Proc. IEEE International Symposium on Information Theory and Its Applications, pages 27–30, 1990. 
10
[18] Haim H. Permuter, Young-Han Kim, and Tsachy Weissman. On directed information and gambling. In Proc. IEEE International Symposium on Information Theory, pages 1403–1407, 2008. 
[19] S. Tatikonda. Control under Communication Constraints. PhD thesis, Massachusetts Institute of Technology, 2000. 
[20] G. Kramer. Capacity results for the discrete memoryless network. Proc. IEEE Transactions on Information Theory, 49(1):4–21, Jan 2003. 
[21] Brian D. Ziebart, J. Andrew Bagnell, and Anind K. Dey. Modeling interaction via the principle of maximum causal entropy. In Proc. International Conference on Machine Learning, pages 1255–1262, 2010. 
[22] Bita Analui and Georg Ch Pflug. On distributionally robust multiperiod stochastic optimization. Computational Management Science, 11(3):197–220, 2014. 
[23] P. Abbeel and A. Y. Ng. Apprenticeship learning via inverse reinforcement learning. In Proc. International Conference on Machine Learning, pages 1–8, 2004. 
[24] Brian D. Ziebart, Andrew Maas, J. Andrew Bagnell, and Anind K. Dey. Maximum entropy inverse reinforcement learning. In Proc. AAAI Conference on Artificial Intelligence, pages 1433–1438, 2008. 
[25] Zhaolin Hu and L Jeff Hong. Kullback-leibler divergence constrained distributionally robust optimization. 2013. 
[26] B. D. Ziebart. Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy. PhD thesis, Carnegie Mellon University, 2010. 
[27] Jun’ichi Kazama and Jun’ichi Tsujii. Evaluation and extension of maximum entropy models with inequality constraints. In Proceedings of the 2003 conference on Empirical methods in natural language processing, pages 137–144. Association for Computational Linguistics, 2003. 
[28] Miroslav Dudík, Steven J. Phillips, and Robert E. Schapire. Maximum entropy density estimation with generalized regularization and an application to species distribution modeling. J. Mach. Learn. Res., 8:1217–1260, 2007. 
[29] Damien Ernst, Pierre Geurts, and Louis Wehenkel. Tree-Based Batch Mode Reinforcement Learning. Journal of Machine Learning Research, 6(1):503–556, 2005. 
[30] M. Kery and M. Schaub. Bayesian Population Analysis using WinBUGS: A Hierarchical Perspective. Elsevier Science, 2011. 
[31] A B Philpott, V de Matos, and V L De Matos. Dynamic sampling algorithms for multi-stage stochastic programs with risk aversion. European Journal of Operations Research, 218(2):470– 483, 2012. 
[32] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT Press, Cambridge, 1998. 
[33] Stephen Boyd and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004. 
11