> Source: https://arxiv.org/pdf/2310.03225

Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms 
Akifumi Wachi LINE Corporation 
akifumi.wachi@linecorp.com 
Wataru Hashimoto Osaka University 
hashimoto@is.eei.eng.osaka-u.ac.jp 
Xun Shen Osaka University 
shenxun@eei.eng.osaka-u.ac.jp 
Kazumune Hashimoto Osaka University 
hashimoto@eei.eng.osaka-u.ac.jp 
Abstract 
Safe exploration is essential for the practical use of reinforcement learning (RL) in many real-world scenarios. In this paper, we present a generalized safe exploration (GSE) problem as a unified formulation of common safe exploration problems. We then propose a solution of the GSE problem in the form of a meta-algorithm for safe exploration, MASE, which combines an unconstrained RL algorithm with an uncertainty quantifier to guarantee safety in the current episode while properly penalizing unsafe explorations before actual safety violation to discourage them in future episodes. The advantage of MASE is that we can optimize a policy while guaranteeing with a high probability that no safety constraint will be violated under proper assumptions. Specifically, we present two variants of MASE with different constructions of the uncertainty quantifier: one based on generalized linear models with theoretical guarantees of safety and near-optimality, and another that combines a Gaussian process to ensure safety with a deep RL algorithm to maximize the reward. Finally, we demonstrate that our proposed algorithm achieves better performance than state-of-the-art algorithms on grid-world and Safety Gym benchmarks without violating any safety constraints, even during training. 
1 Introduction 
Safe reinforcement learning (RL) is a promising paradigm that enables policy optimizations for safety-critical decision-making problems (e.g., autonomous driving, healthcare, and robotics), where it is necessary to incorporate safety requirements to prevent RL policies from posing risks to humans or objects [14]. As a result, safe exploration has received significant attention in recent years as a crucial issue for ensuring the safety of RL during both the learning and execution phases [6]. 
Safe exploration in RL has typically been addressed by formulating a constrained RL problem in which the policy optimization is subject to safety constraints [9, 18]. While there have been many attempts under different types of constraint representations (e.g., expected cumulative cost [3], CVaR [29]), satisfying constraints almost surely or with high probability received less attention to date. Imagine safety-critical applications such as planetary exploration where even a single constraint violation may result in catastrophic failure. NASA’s engineers hope Mars rovers to ensure safety at least with high probability [8]; thus, constraint satisfaction “on average” does not fit their purpose. 
While several algorithms have addressed this problem with this stricter notion of safety, there are several formulations in terms of how the constraints are represented, including cumulative [32], state [39], and instantaneous constraints [41], which respectively correspond to Problems 1, 2, and 3 
37th Conference on Neural Information Processing Systems (NeurIPS 2023). 
 
 
 
 
 
 
 
 
 
 
as we will discuss shortly in Section 2. Unfortunately, there has been limited discussion on the relationships between these approaches, making it challenging for researchers to acquire a systematic understanding of the field as a whole. If a generalized problem were to be formulated, then the research community could pool their efforts to develop suitable algorithms. 
A closer examination of existing algorithms that span the entire theory-to-practice spectrum reveals several areas for improvement. Practical algorithms using deep RL (e.g., [32],[39],[40]) may provide satisfactory performance after convergence, but do not usually guarantee safety during training. In contrast, theoretical studies (e.g., [4], [41]) that guarantee safety with high probability during training often have limitations, such as relying on strong assumptions (e.g., known state transition) or experiencing decreased performance in complex environments. In summary, many algorithms have been proposed in various safe RL formulations, but the creation of a safe exploration algorithm that is both practically useful and supported by theoretical foundations remains an open problem. 
Contributions. We first present a generalized safe exploration (GSE) problem and prove its generality compared with existing safe exploration problems. By taking advantage of the tractable form of the safety constraint in the GSE problem, we establish a meta-algorithm for safe exploration, MASE. This algorithm employs an uncertainty quantifier for a high-probability guarantee that the safety constraints are not violated and penalizes the agent before safety violation, under the assumption that the agent has access to an “emergency stop” authority. Our MASE is both practically useful and theoretically well-founded, which allows us to optimize a policy via an arbitrary RL algorithm under the high-probability safety guarantee, even during training. We then provide two specific variants of MASE with different uncertainty quantifiers. One is based on generalized linear models (GLMs), for which we theoretically provide high-probability guarantees of safety and near-optimality. The other is more practical, combining a Gaussian process (GP, [27]) to ensure safety with a deep RL algorithm to maximize the reward. Finally, we show that MASE performs better than state-of-the-art algorithms on the grid-world and Safety Gym [28] without violating any safety constraints, even during training. 
2 Preliminaries 
Definitions. We consider an episodic safe RL problem in a constrained Markov decision process (CMDP, [3]), M = ⟨ S,A, H,P, r, g, s1 ⟩, where S is a state space, A is an action space, H ∈ Z>0 
is a (fixed) length of each episode, P : S × A × S → [0, 1] is a state transition probability, r : S ×A → [0, 1] is a reward function, g : S ×A → [0, 1] is a safety (cost) function, and s1 ∈ S is an initial state. At each discrete time step, with a given (fully-observable) state s, the agent selects an action a with respect to its policy π : S → A, receiving the new state s′, reward r, and safety cost g. Though we assume a deterministic policy, our core ideas can be extended to stochastic policy settings. Given a policy π, the value and action-value functions in a state s at time h are respectively defined as 
V π r,h(s) := Eπ 
[ H∑ 
h′=h 
γh′ 
r r(sh′ , ah′) 
∣∣∣∣∣ sh = s 
] and Qπ 
r,h(s, a) := Eπ 
[∑H h′=h γ 
h′ 
r r(sh′ , ah′) | sh = s, ah = a ] , where the expectation Eπ is taken 
over the random state-action sequence {(sh′ , ah′)}Hh′=h induced by the policy π. Additionally, γr ∈ (0, 1] is a discount factor for the reward function. In the remainder of this paper, we define Vmax := 
1−γH r 
1−γr and let Th : (S × A → R) → (S × A → R) denote the Bellman update operator 
Th(Q)(s, a) := E [r(sh, ah) + γrVQ(sh+1) | sh = s, ah = a], where VQ(s) := maxa∈A Q(s, a). 
Three common safe RL problems. We tackle safe RL problems where constraints must be satisfied almost surely, even during training. While such problems have garnered attention in the research community, there are several types of formulations, and their relations are yet to be fully investigated. 
One of the most popular formulations for safe RL problems involves maximizing V π r := V π 
r,1(s1) under the constraint that the cumulative cost is less than a threshold, which is described as follows: Problem 1 (Almost surely safe RL with cumulative constraint [32]). 
max π 
V π r subject to Pr 
[ H∑ 
h=1 
γh g g(sh, ah) ≤ ξ1 
∣∣∣∣∣P, π 
] = 1, 
where ξ1 ∈ R≥0 is a constant representing a threshold, and γg ∈ (0, 1] is a discount factor for g. 
2
Observe that, the expectation is not taken regarding the safety constraint in Problem 1. This problem was studied in [32], which is stricter than the conventional one where the expectation is taken with respect to the cumulative safety cost function (i.e., Eπ[ 
∑H h=1 γ 
h g g(sh, ah) ] ≤ ξ1). 
Another popular formulation involves leveraging the state constraints so that safety corresponds to avoiding visits to a set of unsafe states. This type of formulation has been widely adopted by previous studies on safe-critical robotics tasks [38–40, 45], which is written as follows: 
Problem 2 (Safe RL with state constraints). 
max π 
V π r subject to E 
[ H∑ 
h=1 
γh g I(sh ∈ Sunsafe) 
∣∣∣∣∣P, π 
] ≤ ξ2, 
where ξ2 ∈ R≥0 is a threshold, I(·) is the indicator function, and Sunsafe ⊂ S is a set of unsafe states. 
Finally, some existing studies formulate safe RL problems via an instantaneous constraint, attempting to ensure safety even during the learning stage while aiming for extremely safety-critical applications such as planetary exploration [42] or healthcare [36]. Such studies typically require the agent to satisfy the following instantaneous safety constraint at every time step. 
Problem 3 (Safe RL with instantaneous constraints). 
max π 
V π r subject to Pr 
[ g(sh, ah) ≤ ξ3 | P, π 
] = 1, ∀h ∈ [ 1, H ], 
where ξ3 ∈ R≥0 is a time-invariant safety threshold. 
3 Problem Formulation 
This paper also requires an agent to optimize a policy under a safety constraint, as in the three common safe RL problems. We seek to find the optimal policy π⋆ : S → A of the following problem, which will hereinafter be referred to as the “generalized” safe exploration (GSE) problem: 
Problem 4 (GSE problem). Let bh ∈ R denote a time-varying threshold. 
max π 
V π r subject to Pr 
[ g(sh, ah) ≤ bh | P, π 
] = 1, ∀h ∈ [ 1, H ]. 
This constraint is instantaneous, which requires the agent to learn a policy without a single constraint violation not only after convergence but also during training. We assume that the threshold is myopically known; that is, bh is known at time h, but unknown before that. Crucially, at every time step h, since sh is a fully observable state and the agent’s policy is deterministic, we will use a simplified inequality represented as g(sh, ah) ≤ bh in the rest of this paper. This constraint is akin to that in Problem 3, with the difference that the safety threshold is time-varying. 
Importance of the GSE problem. Though our problem may not seem relevant to Problems 1 and 2, we will shortly present and prove a theorem on the relationship between the GSE problem and the three common safe RL problems. 
Theorem 3.1. Problems 1, 2, and 3 can be transformed into the GSE problem (i.e., Problem 4). 
See Appendix B for the proof. In other words, the feasible policy space in the GSE problem can be identical to those in the other three problems by properly defining the safety cost function and threshold. Crucially, Problem 1 is a special case of the GSE problem with bh = ηh for all h, where ηh+1 = γ−1 
g · (ηh − g(sh, ah)) with η0 = ξ1. It is particularly beneficial to convert Problems 1 and 2, which have additive constraint structures, to the GSE problem, which has an instantaneous constraint. The accurate estimation of the cumulative safety value in Problems 1 and 2 is difficult because they depend on the trajectories induced by a policy. Dealing with the instantaneous constraint in the GSE problem is easier, both theoretically and empirically. Also, especially when the environment is time-varying (e.g., there are moving obstacles), the GSE problem is more useful than Problem 3. 
Typical CMDP formulations with expected cumulative (safety) cost are out of the scope of the GSE problem. In such problems, the safety notion is milder; hence, although many advanced deep RL algorithms have been actively proposed that perform well in complex environments after convergence, 
3
their performance in terms of safety during learning is usually low, as reported by Stooke et al. [33] or Wachi et al. [43]. Risk-constrained MDPs are also important safe RL problems that are not covered by the GSE problem; they have been widely studied by representing risk as a constraint on some conditional value-at-risk [11] or using chance constraints [24, 26].1 
Difficulties and Assumptions. Theorem 3.1 insists that the GSE problem covers a wide range of safe RL formulations and is worth solving, but the problem is intractable without assumptions. We now discuss the difficulties in solving the GSE problem, and then list the assumptions in this paper. 
The biggest difficulty with the GSE problem lies in the fact that there may be no viable safe action given the current state sh, safety cost g, and threshold bh. When bh = 0.1 and g(sh, a) = 0.5,∀a ∈ A, the agent has no viable action for ensuring safety. The agent needs to guarantee safety, even during training, where little environmental information is available; hence, it is significant for the agent to avoid such situations where there is no action that guarantees safety. Another difficulty is related to the regularity of the safety cost function and the strictness of the safety constraint. In this paper, the safety cost function is unknown a priori.; thus, when the safety cost does not exhibit any regularity, the agent can neither infer the safety of decisions nor guarantee safety almost surely. 
To address the first difficulty mentioned above, we use Assumptions 3.2 and 3.3. Assumption 3.2 (Safety margin). There exists ζ ∈ R>0 such that Pr[ g(sh, ah) ≤ bh− ζ | P, π⋆ ] = 1,∀h ∈ [1, H]. Assumption 3.3 (Emergency stop action). Let â be an emergency stop action such that P(s1 | s, â) = 1 for all s ∈ S. The agent is allowed to execute the emergency stop action and reset the environment if and only if the probability of guaranteed safety is not sufficiently high. 
Assumption 3.2 is mild; this is similar to the Slater condition, which is widely adopted in the CMDP literature [13, 25]. We consider Assumption 3.3 is also natural for safety-critical applications because it is usually better to guarantee safety, even with human interventions, if the agent requires help in emergency cases. In some applications (e.g., the agent is in a hazardous environment), however, emergency stop actions should often be avoided because of the expensive cost of human intervention. In such cases, the agent needs to learn a reset policy allowing them to return to the initial state as in Eysenbach et al. [15], rather than asking for human help, which we will leave to future work. 
As for the second difficulty, we assume that the safety cost function belongs to a class where uncertainty can be estimated and guarantee the satisfaction of the safety constraint with high probability. We present an assumption regarding an important notion called an uncertainty quantifier: Assumption 3.4 (δ-uncertainty quantifier). Let µ : S×A → R denote the estimated mean function of safety. There exists a δ-uncertainty quantifier Γ : S ×A → R such that | g(s, a)−µ(s, a) | ≤ Γ(s, a) for all (s, a) ∈ S ×A, with a probability of at least 1− δ. 
4 Method 
We propose MASE for the GSE problem, which combines an unconstrained RL algorithm with additional mechanisms for addressing the safety constraints. The pseudo-code is provided in Algorithm 1, and a conceptual illustration can be seen in Figure 1. 
The most notable feature of MASE is that safety is guaranteed via the δ-uncertainty quantifier and the emergency stop action (lines 3 – 9). The δ-uncertainty quantifier is particularly useful because we can guarantee that the confidence bound contains the true safety cost function, that is, g(s, a) ∈ [µ(s, a)± Γ(s, a) ] for all s ∈ S and a ∈ A. This means that, if the agent chooses actions such that µ(sh, ah) + Γ(sh, ah) ≤ bh, then g(sh, ah) ≤ bh holds with a probability of at least 1− δ. Regarding the first difficulty mentioned in Section 3, it is crucial that there is at least one safe action. Thus, at every time step h, the agent computes a set of actions that are considered to satisfy the safety constraints with a probability at least 1− δ given the state sh and threshold bh. This is represented as 
A+ h := { a ∈ A | min{ 1, µ(sh, a) + Γ(sh, a) } ≤ bh }. 
Whenever the agent identifies that at least one action will guarantee safety, the agent is required to choose an action within A+ 
h (line 3). The emergency stop action is executed if and only if there is no 
1The solution in the GSE problem is guaranteed to be a conservative approximation of that in safe RL problems with chance constraints. For more details, see Appendix C. 
4
Algorithm 1 Meta-Algorithm for Safe Exploration (MASE) 
1: for episode t = 1, 2, . . . , T do 2: for time h = 1, 2, . . . ,H do 3: Take “safe” action ah = π(sh) within A+ 
h ▷ Execute only safe actions 4: Receive reward r(sh, ah), safety cost g(sh, ah), and next state sh+1 
5: Update safety threshold bh+1 
6: if A+ h+1 = ∅ then 
7: Compute r̂(sh, ah) = − c mina∈A Γ(sh+1,a) 
▷ Penalty for the emergency stop action 8: Append (sh, ah, r̂(sh, ah), sh+1) to D 9: break (i.e., take action â) ▷ Execute the emergency stop action 
10: else 11: Append (sh, ah, r(sh, ah), sh+1) to D 12: Optimize a policy π based on D via an (unconstrained) RL algorithm 13: Update the uncertainty quantifier Γ and rewrite D 
viable action satisfying the safety constraint (i.e., A+ h+1 ̸= ∅); that is, the agent is allowed to execute 
â and start a new episode from an initial safe state (lines 6 – 9). The safety cost is upper-bounded by 1 because g ∈ [0, 1] by definition. Note that MASE proactively avoids unsafe actions by selecting the emergency action to take beforehand; this is in contrast to Sun et al. [37], whose method terminates the episode immediately after the agent has already violated a safety constraint. 
When safety is guaranteed in the manner described above, the question remains as to how to obtain a policy that maximizes the expected cumulative reward. As such, we first convert the original CMDP M to the following unconstrained MDP 
M̂ := ⟨ S, {A, â}, H,P, r̂, ρ ⟩. The changes from M lie in the action space and the reward function, as well as in the absence of the safety cost function. First, the action space is augmented so that the agent can execute the emergency stop action, â. The second modification concerns the reward function. When executing the emergency stop action â, the agent is penalized as its sacrifice so that the same situation will not occur in future episodes; hence, we modify the reward function as follows: 
r̂(sh, ah) = 
{ − c/mina∈A Γ(sh+1, a) if A+ 
h+1 = ∅, r(sh, ah) otherwise, 
(1) 
where c ∈ R>0 is a positive scalar representing a penalty for performing the emergency stop. This penalty is assigned to the state-action pair (sh, ah) that placed the agent into the undesirable situation at time step h+ 1, represented as A+ 
h+1 = ∅ (see Figure 1). 
sh sh+1 
sh+1 sh+2 
ah 
ah+1 
× × 
r̂ ≪ 0 
r̂ = r 
No viable action (i.e., A+ h+1 = ∅) 
ah 
â 
Figure 1: Conceptual illustration of MASE. At every time step h, the agent chooses action ah within A+ 
h . If there is no safe action at state sh+1 satisfying the constraint, the emergency stop action â is executed and the agent receives a large penalty for (sh, ah). 
To show that MASE is a reasonable safe RL algorithm, we express the following intuitions. Consider the ideal situation in which the safety cost function is accurately estimated for any state-action pairs; that is, Γ(s, a) = 0 for all (s, a). In this case, all emergency stop actions are properly executed, and the safety constraint will be violated at the next time step if the agent executes other actions. It is reasonable for the agent to receive a penalty of r̂(s, a) = −∞ because this state-action pair surely causes a safety violation without the emergency stop action. Unfortunately, however, the safety cost is uncertain and the agent conservatively executes â although there are still actions satisfying the safety constraint, especially in the early phase of training; hence, we increase or reduce the penalty according to the magnitude of uncertainty in (1) to avoid an excessively large penalty. 
We must carefully consider the fact that the quality of information regarding the modified reward function r̂ is uneven in the replay buffer D. Specifically, in the early phase of training, the δ-
5
uncertainty quantifier is loose. Hence, the emergency stop action is likely to be executed even if viable actions remain; that is, the agent will receive unnecessary penalties. In contrast, the emergency stop actions in later phases are executed with confidence, as reflected by the tight δ-uncertainty quantifier. Thus, as in line 15, we rewrite the replay buffer D while updating Γ depending on the model in terms of the safety cost function (as for specific methods to update Γ, see Sections 5 and 6). 
Connections to shielding methods. The notion of the emergency stop action is akin to shielding [2, 20] which has been actively studied in various problem settings including partially-observable environments [10] or multi-agent settings [23]. Thus, MASE can be regarded as a variant of shielding methods (especially, preemptive shielding in [2]) that is specialized for the GSE problem. On the other hand, MASEdoes not only block unsafe actions but also provides proper penalties for executing the emergency stop actions based on the uncertainty quantifier, which leads to rigorous theoretical guarantees presented shortly. Such theoretical advantages can be enjoyed in many safe RL problems because of the wide applicability of the GSE problem backed by Theorem 3.1. 
Advantages of MASE. Though certain existing algorithms for Problem 3 (i.e., the closest problem to the GSE problem) theoretically guarantee safety during learning, several strong assumptions are needed, such as a known and deterministic state transition and regular safety function as in [41] and a known feature mapping function that is linear with respect to transition kernels, reward, and safety as in [5]. Such algorithms have little affinity with deep RL; thus, their actual performance in complex environments tends to be poor. In contrast, MASE is compatible with any advanced RL algorithms, which can also handle various constraint formulations while maintaining the safety guarantee. 
Validity of MASE. We conclude this section by presenting the following two theorems to show that our MASE produces reasonable operations in solving the GSE problem. Theorem 4.1. Under Assumption 3.4, MASE guarantees safety with a probability of at least 1− δ. Theorem 4.2. Assume that the safety cost function is estimated for any state-action pairs with an accuracy of better than ζ 
2 ; that is, Γ(s, a) ≤ ζ 2 for all (s, a). Set c ∈ R to be a sufficiently large 
scalar such that c > ζVmax 
2γH r 
. Then, the optimal policy in M̂ is identical to that in M. 
See Appendix D for the proofs. Unfortunately, obtaining a δ-uncertainty qualifier that works in general cases is highly challenging. To develop a feasible model for the uncertainty quantification, we assume that the safety cost can be modeled via a GLM in Section 5 and via a GP in Section 6. 
5 A Provable Algorithm under Generalized Linear CMDP Assumptions 
In this section, we focus on CMDPs with generalized linear structures and analyze the theoretical properties of MASE. Specifically, we provide a provable algorithm to use a class of GLMs denoted as F for modeling Q⋆ 
r,h := Qπ⋆ 
r,h and g, and then provide theoretical results on safety and optimality. 
5.1 Generalized Linear CMDPs 
We extend the assumption in Wang et al. [44] from unconstrained MDPs to CMDPs settings. Our assumption is based on GLMs as with [44] that makes a strictly weaker assumption than their Linear MDP assumption [19, 46]. As preliminaries, we first list the necessary definitions and assumptions. Definition 5.1 (GLMs). Let d ∈ Z>0 be a feature dimension and let Bd := {x ∈ Rd : ∥x∥2 ≤ 1} be the l2 ball in Rd. For a known feature mapping function ϕ : S × A → Bd and a known link function f : [−1, 1] → [−1, 1], the class of generalized linear model is denoted as F := {(s, a) → f(⟨ϕs,a, θ⟩) : θ ∈ Bd} where ϕs,a := ϕ(s, a). Assumption 5.2 (Regular link function). The link function f(·) is twice differentiable and is either monotonically increasing or decreasing. Furthermore, there exist absolute constants 0 < κ < κ < ∞ and M < ∞ such that κ < |f ′(x)| < κ and |f ′′(x)| < M for all |x| ≤ 1. 
This assumption on the regular link function is standard in previous studies (e.g., [16], [21]). Linear and logistic models are the special cases of the GLM where the link functions are defined as f(x) = x and f(x) = 1/(1 + e−x). In both cases, the link functions satisfy Assumption 5.2. 
We finally make the assumption of generalized linear CMDPs (GL-CMDPs), which extends the notion of the optimistic closure for unconstrained MDP settings in Wang et al. [44]. 
6
Assumption 5.3 (GL-CMDP). For any 1 ≤ h < H and u ∈ Fup, we have Th(u) ∈ F and g ∈ F . 
Recall that Th is the Bellman update operator. In Assumption 5.3, with a positive semi-definite matrix A ∈ Rd×d ≻ 0 and a fixed positive constant αmax ∈ R>0, we define 
Fup := {(s, a) → min{Vmax, f(⟨ϕs,a, θ⟩) + α∥ϕs,a∥A} : θ ∈ Bd, 0 ≤ α ≤ αmax, ∥A∥op ≤ 1}, 
where ∥x∥A := √ x⊤Ax is the matrix Mahalanobis seminorm, and ∥A∥op is the matrix operator norm. 
For simplicity, we suppose the same link functions for the Q-function and the safety cost function, but it is acceptable to use different link functions. Note that Assumption 5.3 is a more general assumption than Amani et al. [5] that assumes linear transition kernel, reward, and safety cost functions or Wachi et al. [43] that assumes a known transition and GLMs in terms of reward and safety cost functions. 
5.2 GLM-MASE Algorithm 
We introduce an algorithm GLM-MASE under Assumptions 5.2 and 5.3. Hereinafter, we explicitly denote the episode for each variable. For example, we let s(t)h or a(t)h denote a state or action at the time step h of episode t. We also let ϕ̃(t) 
h := ϕ(s (t) h , a 
(t) h ) for more concise notations. 
Uncertainty quantifiers. To actualize MASE in the generalized linear CMDP settings, we first need to consider how to obtain the δ-uncertainty quantifier in terms of the safety cost function. Since we assume g ∈ F , we can define the δ-uncertainty quantifier based on the existing studies on GLMs, especially in the field of multi-armed bandit [22, 16]. Based on Assumptions 5.2 and 5.3, we now provide a lemma regarding the δ-uncertainty quantifier on safety. Lemma 5.4. Suppose Assumptions 5.2 and 5.3 hold. Set δ = 1 
TH . With a universal constant 
C ∈ R>0, let Cg := Cκκ−1 √ 1 +M + κ+ d2 ln 
( 1+κ+αmax 
δ 
) . Define 
Γ(s, a) := Cg · ∥ϕs,a∥Λ−1 h,t 
with Λh,t := ∑ 
τ≤t ϕ̃ (τ) h ϕ̃ 
(τ) h + I, 
where I is the identity matrix. Let θ̂gh,t ∈ Rd be the ridge estimate, which is computed by θ̂gh,t := 
argmin∥θ∥2≤1 
∑ τ≤t 
( g(s 
(τ) h , a 
(τ) h )−f(⟨ ϕ̃(τ) 
h , θ ⟩) )2 
. Then, the following inequality holds 
| g(s(t)h , a (t) h )− f(⟨ ϕ̃(t) 
h , θ̂gh,t ⟩) | ≤ Γ(s (t) h , a 
(t) h ) 
for all (s, a) ∈ S ×A, with a probability at least 1− δ. 
For the purpose of qualifying uncertainty in GLMs, the weighted l2-norm of ϕ (i.e., ∥ϕs,a∥Λ−1 h,t 
) plays an important role. Because we assume that the Q-function and safety cost function share the same feature, we have a similar lemma on the uncertainty quantifier regarding the Q-function as follows: 
Lemma 5.5. Suppose Assumptions 5.2 and 5.3 hold. Let θ̂Qh,t ∈ Rd denote the ridge esti-
mate; that is, θ̂Qh,t := argmin∥θ∥2≤1 
∑ τ≤t 
( y (τ) h − f(⟨ ϕ̃(τ) 
h , θ ⟩) )2 
, where y (τ) h := r(s 
(τ) h , a 
(τ) h ) + 
maxa′∈A Q̂ (τ) r,h+1(s 
(τ) h+1, a 
′) for all τ ≤ t with 
Q̂ (t) r,h(s, a) := min 
{ Vmax, f(⟨ϕs,a, θ̂ 
Q h,t⟩) + CQ/gΓ(s, a) 
} that is initialized with Q̂ 
(0) r,h = 0 for all h ≤ H and Q̂ 
(t) r,H+1 = 0 for all 1 ≤ t ≤ T . Then, with a 
universal constant CQ/g ∈ R>0, the following inequalities holds 
|Q⋆ r,h(s 
(t) h , a 
(t) h )− f(⟨ ϕ̃(t) 
h , θ̂Qh,t ⟩) | ≤ CQ/g · Γ(s (t) h , a 
(t) h ) 
for all (s, a) ∈ S ×A, with a probability at least 1− δ. 
Note that Γ(s(t)h , a (t) h ) is the δ-uncertainty quantifier with respect to the safety cost function. One of 
the biggest advantages of the generalized linear CMDPs is that the magnitude of uncertainty for the Q-function is proportional to that for the safety cost function. Hence, by exploring the Q-function 
7
based on the optimism in the face of the uncertainty principle [7, 35], the safety cost function is also explored simultaneously, which contributes to the efficient exploration of state-action spaces. 
Integration into MASE. The GLM-MASE is an algorithm to integrate the δ-uncertainty quantifiers inferred by the GLM into the MASE sequence. Detailed pseudo code is presented in Appendix E. 
To deal with the safety constraint, GLM-MASE leverages the upper bound inferred by the GLM; that is, for all h and t, the agent takes only actions that satisfy 
f ( ⟨ ϕ̃(t) 
h , θ̂gh,t ⟩ ) + Γ 
( s (t) h , a 
(t) h 
) ≤ bh. 
By Lemma 5.4, such state-action pairs satisfy the safety constraint, i.e. g(s (t) h , s 
(t) h ) ≤ bh, for all 
h and t, with a probability at least 1 − δ. If there is no action satisfying the safety constraint (i.e., A+ 
h = ∅), the emergency stop action â is taken, and then the agent receives a penalty defined in (1). 
As for policy optimization, we follow the optimism in the face of the uncertainty principle. Specifi-cally, the policy π is optimized so that the upper-confidence bound of the Q-function characterized by r̂ is maximized; that is, for any state s ∈ S, the policy is computed as follows: 
π (t) h (s) = argmax 
a∈A Q̂ 
(t) r̂,h(s, a). 
Intuitively, this equation enables us to 1) solve the exploration and exploitation dilemma by incorporating the optimistic estimates of the Q-function and 2) make the agent avoid generating trajectories to violate the safety constraint via the modified reward function. 
Theoretical results. We now provide two theorems regarding safety and near-optimality. For both theorems, see Appendix E for the proofs. Theorem 5.6. Suppose the assumptions in Lemma 5.4 hold. Then, the GLM-MASE satisfies g(s 
(t) h , a 
(t) h ) ≤ bh for all t ∈ [1, T ] and h ∈ [1, H], with a probability at least 1− δ. 
Theorem 5.7. Suppose the assumptions in Lemmas 5.4 and 5.5 hold. Let C1 and C2 be positive, universal constants. Also, with a sufficiently large T , let t⋆ denote the smallest integer satisfying λmin(Σ)tH − C1 
√ tHd− C2 
√ tH ln δ−1 ≥ 2Cg · ζ−1, where λmin(Σ) is the minimum eigenvalue 
of the second moment matrix Σ. Then, the policy π(t) obtained by GLM-MASE at episode t satisfies 
T∑ t=t⋆ 
[ V π⋆ 
r − V π(t) 
r 
] ≤ Õ 
( H √ d3(T − t∗) 
) with probability at least 1− δ. 
Theorem 5.6 shows that the GLM-MASE guarantees safety with high probability for every time step and episode, which is a variant of Theorem 4.1 under the generalized linear CMDP assumption and corresponding δ-uncertainty quantifier. Theorem 5.7 demonstrates the agent’s ability to act near-optimally after a sufficiently large number of episodes. The proof is based on the following idea. After t⋆ episodes, the safety cost function and the Q-function are estimated with an accuracy better than ζ 
2 . Then, based on Theorem 4.2, the optimal policy in M̂ is identical to that in M; thus, the agent achieves a near-optimal policy by leveraging the (well-estimated) optimistic Q-function. 
6 A Practical Algorithm 
Though we established an algorithm backed by theory under the generalized linear CMDP assumption in Section 5, it is often challenging to obtain proper feature mapping functions in complicated environments. Thus, in this section, we propose a more practical algorithm combining a GP-based estimator to guarantee safety with unconstrained deep RL algorithms to maximize the reward. 
Guaranteeing safety via GPs. As shown in the previous sections, the δ-uncertainty quantifier plays a critical role in MASE. To qualify the uncertainty in terms of the safety cost function g, we consider modeling it as a GP: g(z) ∼ GP(µ(z), k(z, z′)), where z := [s, a], µ(z) is a mean function, and k(z, z′) is a covariance function. The posterior distribution over g(·, ·) is computed based on n ∈ Z>0 observations at state-action pairs (z1, z2, . . . ,zn) with safety measurements yn := { y1, y2, . . . , yn }, where yn := g(zn)+Nn and Nn ∼ N (0, ω2) is zero-mean Gaussian noise 
8
with a standard deviation of ω ∈ R≥0. We consider episodic RL problems, and so n ≈ tH + h for episode t and time step h, although the equality does not hold because of the episode cutoffs. Using the past measurements, the posterior mean, variance, and covariance are computed analytically as µn(z) = k⊤ 
n (z)(Kn + ω2I)−1yn, σn(z) = kn(z, z), and kn(z, z ′) = k(z, z′) − k⊤ 
n (z)(Kn + ω2I)−1kn(z 
′), where kn(z) = [k(z1, z), . . . , k(zn, z)] ⊤ and Kn is the positive definite kernel 
matrix. We now present a theorem on the safety guarantee. 
Theorem 6.1. Assume ∥g∥2k ≤ B and Nn ≤ ω for all n ≥ 1. Set β1/2 n := B+4ω 
√ νn + 1 + ln(1/δ) 
and construct the δ-uncertainty quantifier by 
Γ(s, a) := βn · σn(s, a), ∀(s, a) ∈ S ×A, (2) 
where νn is the information capacity associated with kernel k. Then, MASE based on (2) satisfies the safety constraint g(s(t)h , a 
(t) h ) ≤ bh for all t and h with a probability of at least 1− δ. 
See Appendix F for the proofs. Theorem 6.1 guarantees that the safety constraint is satisfied by combining the GP-based δ-uncertainty quantifier in (2) and the emergency stop action. 
Maximizing reward via deep RL. The remaining task is to optimize the policy via the modified reward function r̂ in (1), whereby the agent is penalized for emergency stop actions. This problem is decoupled from the safety constraint and can be solved as the following unconstrained RL problem: 
π := argmax π 
V π r̂ . (3) 
There are many excellent algorithms for solving (3) such as trust region policy optimization (TRPO, [31]) and twin delayed deep deterministic policy gradient (TD3, [17]). One of the key benefits of our MASE is such compatibility with a broad range of unconstrained (deep) RL algorithms. 
7 Experiments 
We conduct two experiments. The first is on Safety Gym [28], where an agent must maximize the expected cumulative reward under a safety constraint with additive structures as in Problems 1 and 2. The safety cost function g is binary (i.e., 1 for an unsafe state-action pair and 0 otherwise), and the safety threshold is set to ξ1 = 20. The reason for choosing Safety Gym is that this benchmark is complex and elaborate, and has been used to evaluate a variety of excellent algorithms. The second is a grid world where a safety constraint is instantaneous as in Problem 3. Due to the page limit, we present the settings and results of the grid-world experiment in Appendix H. 
To solve the Safety Gym tasks, we implement the practical algorithm presented in Section 6 as follows. First, we convert the problem into a GSE problem by defining bh := γ−1 
g ·(ξ1− ∑h−1 
h′=0 γ h′ 
g g(sh′ , ah′)) and enforcing the safety constraint represented as g(sh, ah) ≤ bh for every time step h in each episode. Second, to infer the safety cost, we use deep GP to conduct training and inference, as in [30] when dealing with high-dimensional input spaces. Finally, as for the policy optimization in M̂, we leverage the TRPO algorithm. We delegate other details to Appendix G. 
Baselines and metrics. We use the following four algorithms as baselines. The first is TRPO, which is a safety-agnostic deep RL algorithm that purely optimizes a policy without safety consideration. The second and third are CPO [1] and TRPO-Lagrangian [28], which are well-known algorithms for solving CMDPs. The final algorithm is Sauté RL [32], which is a recent, state-of-the-art algorithm for solving safe RL problems where constraints must be satisfied almost surely. We employ the following three metrics to evaluate our MASE and the aforementioned four baselines: 1) the expected cumulative reward, 2) the expected cumulative safety, and 3) the maximum cumulative safety. We execute each algorithm with five random seeds and compute the means and confidence intervals. 
Results. The experimental results are summarized in Figure 2. In both environments, the figures show that TRPO, TRPO-Lagrangian, and CPO successfully learn the policies, but violate the safety constraints during training and even after convergence. Sauté RL is much safer than those three algorithms, but the safety constraint is not satisfied in some episodes, and the performance of the policy significantly deteriorates in terms of the the cumulative reward during training. Our MASE obtains better policies in a smaller number of samples compared with Sauté RL, while also satisfying the safety constraints with respect to both the average and the worst-case. Note that, after convergence, the policy given by MASE performs worse than those produced by the baseline algorithms in terms of 
9
0 100 200 300 400 500 Epoch 
−0.5 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
TRPO TRPO Lag CPO Saute TRPO MASE 
(a) Average episode return. 
0 100 200 300 400 500 Epoch 
0 
10 
20 
30 
40 
50 TRPO TRPO Lag CPO Saute TRPO MASE Safety threshold 
(b) Average episode safety. 
0 100 200 300 400 500 Epoch 
0 
20 
40 
60 
80 
100 
120 
140 TRPO TRPO Lag CPO Saute TRPO MASE Safety threshold 
(c) Maximum episode safety. 
0 100 200 300 400 500 Epoch 
−0.5 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
TRPO TRPO Lag CPO Saute TRPO MASE 
(d) Average episode return. 
0 100 200 300 400 500 Epoch 
0 
5 
10 
15 
20 
25 
30 
35 
40 TRPO TRPO Lag CPO Saute TRPO MASE Safety threshold 
(e) Average episode safety. 
0 100 200 300 400 500 Epoch 
0 
20 
40 
60 
80 
100 
120 
140 
160 TRPO TRPO Lag CPO Saute TRPO MASE Safety threshold 
(f) Maximum episode safety. 
Figure 2: Experimental results on Safety Gym (Top: PointGoal1, Bottom: CarGoal1). The proposed MASE satisfies the safety constraint in every episode and achieves better performance in terms of the reward than the state-of-the-art method called Sauté RL. Conventional methods (i.e., TRPO, TRPO-Lagrangian, and CPO) repeatedly violate the safety constraint, especially in the early phase of training. Shaded areas represent 1σ confidence intervals across five different random seeds. 
TRPO TRPO Lag CPO Saute TRPO MASE 
2.70 
2.75 
2.80 
2.85 
2.90 
2.95 
3.00 
(a) Average episode return. 
TRPO TRPO Lag CPO Saute TRPO MASE 
5 
10 
15 
20 
25 Safety threshold 
(b) Average episode safety. 
TRPO TRPO Lag CPO Saute TRPO MASE 
20 
40 
60 
80 
100 Safety threshold 
(c) Maximum episode safety. 
Figure 3: Experimental results on Safety Gym (CarGoal1) with the epoch of 1000. The box plots show the converged performance. Though MASE performs worse than other baselines in terms of reward, the acquired policy is still near-optimal. As for safety, while baselines violate the safety constraint in most of the episodes, MASE guarantees the satisfaction of the severe safety constraint. 
reward, as shown in Figure 3. The emergency stop action is a variant of resetting actions that are common in episodic RL settings, which prevent the agent from exploring the state-action spaces since the uncertainty quantifier is sometimes quite conservative. We consider that this is a reason why the converged reward performance of MASE is worse than other methods. However, because we require the agent to solve difficult problems where safety is guaranteed at every time step and episode, we consider that this result is reasonable, and further performance improvements are left to future work. 
8 Conclusion 
In this article, we first introduced the GSE problem and proved that it is more general than three common safe RL problems. We then proposed MASE to optimize a policy under safety constraints that allow the agent to execute an emergency stop action at the sacrifice of a penalty based on the δ-uncertainty qualifier. As a specific instance of MASE, we first presented GLM-MASE to theoretically guarantee the near-optimality and safety of the acquired policy under generalized linear CMDP assumptions. Finally, we provided a practical MASE and empirically evaluated its performance in comparison with several baselines on the Safety Gym and grid-world. 
10
Acknowledgments and Disclosure of Funding 
We would like to thank the anonymous reviewers for their helpful comments. This work is partially supported by JST CREST JPMJCR201 and by JSPS KAKENHI Grant 21K14184. 
References [1] Achiam, J., Held, D., Tamar, A., and Abbeel, P. (2017). Constrained policy optimization. In 
International Conference on Machine Learning (ICML). 
[2] Alshiekh, M., Bloem, R., Ehlers, R., Könighofer, B., Niekum, S., and Topcu, U. (2018). Safe reinforcement learning via shielding. In AAAI Conference on Artificial Intelligence (AAAI). 
[3] Altman, E. (1999). Constrained Markov decision processes, volume 7. CRC Press. 
[4] Amani, S., Alizadeh, M., and Thrampoulidis, C. (2019). Linear stochastic bandits under safety constraints. In Neural Information Processing Systems (NeurIPS). 
[5] Amani, S., Thrampoulidis, C., and Yang, L. (2021). Safe reinforcement learning with linear function approximation. In International Conference on Machine Learning (ICML). 
[6] Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., and Mané, D. (2016). Concrete problems in AI safety. arXiv preprint arXiv:1606.06565. 
[7] Auer, P. and Ortner, R. (2007). Logarithmic online regret bounds for undiscounted reinforcement learning. In Neural Information Processing Systems (NeurIPS). 
[8] Bajracharya, M., Maimone, M. W., and Helmick, D. (2008). Autonomy for mars rovers: Past, present, and future. Computer, 41(12):44–50. 
[9] Brunke, L., Greeff, M., Hall, A. W., Yuan, Z., Zhou, S., Panerati, J., and Schoellig, A. P. (2022). Safe learning in robotics: From learning-based control to safe reinforcement learning. Annual Review of Control, Robotics, and Autonomous Systems, 5:411–444. 
[10] Carr, S., Jansen, N., Junges, S., and Topcu, U. (2023). Safe reinforcement learning via shielding under partial observability. In AAAI Conference on Artificial Intelligence. 
[11] Chow, Y., Ghavamzadeh, M., Janson, L., and Pavone, M. (2017). Risk-constrained reinforcement learning with percentile risk criteria. Journal of Machine Learning Research (JMLR), 18(1):6070– 6120. 
[12] Chowdhury, S. R. and Gopalan, A. (2017). On kernelized multi-armed bandits. In International Conference on Machine Learning (ICML). 
[13] Ding, D., Zhang, K., Basar, T., and Jovanovic, M. (2020). Natural policy gradient primal-dual method for constrained Markov decision processes. In Neural Information Processing Systems (NeurIPS). 
[14] Dulac-Arnold, G., Levine, N., Mankowitz, D. J., Li, J., Paduraru, C., Gowal, S., and Hester, T. (2021). Challenges of real-world reinforcement learning: definitions, benchmarks and analysis. Machine Learning. 
[15] Eysenbach, B., Gu, S., Ibarz, J., and Levine, S. (2018). Leave no trace: Learning to reset for safe and autonomous reinforcement learning. In International Conference on Learning Representations (ICLR). 
[16] Filippi, S., Cappe, O., Garivier, A., and Szepesvári, C. (2010). Parametric bandits: The generalized linear case. In Neural Information Processing Systems (NeurIPS). 
[17] Fujimoto, S., van Hoof, H., and Meger, D. (2018). Addressing function approximation error in actor-critic methods. In International Conference on Machine Learning (ICML). 
[18] Garcıa, J. and Fernández, F. (2015). A comprehensive survey on safe reinforcement learning. Journal of Machine Learning Research (JMLR), 16(1):1437–1480. 
11
[19] Jin, C., Yang, Z., Wang, Z., and Jordan, M. I. (2020). Provably efficient reinforcement learning with linear function approximation. In Conference on Learning Theory (COLT). 
[20] Könighofer, B., Bloem, R., Junges, S., Jansen, N., and Serban, A. (2020). Safe reinforcement learning using probabilistic shields. In International Conference on Concurrency Theory: CONCUR. 
[21] Li, L., Chu, W., Langford, J., and Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. In International Conference on World Wide Web (WWW). 
[22] Li, L., Lu, Y., and Zhou, D. (2017). Provably optimal algorithms for generalized linear contextual bandits. In International Conference on Machine Learning (ICML), pages 2071–2080. 
[23] Melcer, D., Amato, C., and Tripakis, S. (2022). Shield decentralization for safe multi-agent reinforcement learning. In Neural Information Processing Systems (NeurIPS). 
[24] Ono, M., Pavone, M., Kuwata, Y., and Balaram, J. (2015). Chance-constrained dynamic programming with application to risk-aware robotic space exploration. Autonomous Robots, 39(4):555–571. 
[25] Paternain, S., Chamon, L., Calvo-Fullana, M., and Ribeiro, A. (2019). Constrained reinforcement learning has zero duality gap. Neural Information Processing Systems (NeurIPS). 
[26] Pfrommer, S., Gautam, T., Zhou, A., and Sojoudi, S. (2022). Safe reinforcement learning with chance-constrained model predictive control. In Learning for Dynamics and Control Conference (L4DC), pages 291–303. 
[27] Rasmussen, C. E. (2003). Gaussian processes in machine learning. In Summer school on machine learning, pages 63–71. Springer. 
[28] Ray, A., Achiam, J., and Amodei, D. (2019). Benchmarking safe exploration in deep reinforcement learning. OpenAI. 
[29] Rockafellar, R. T., Uryasev, S., et al. (2000). Optimization of conditional value-at-risk. Journal of risk, 2:21–42. 
[30] Salimbeni, H. and Deisenroth, M. (2017). Doubly stochastic variational inference for deep Gaussian processes. In Neural Information Processing Systems (NeurIPS). 
[31] Schulman, J., Levine, S., Abbeel, P., Jordan, M., and Moritz, P. (2015). Trust region policy optimization. In International Conference on Machine Learning (ICML). 
[32] Sootla, A., Cowen-Rivers, A. I., Jafferjee, T., Wang, Z., Mguni, D. H., Wang, J., and Ammar, H. (2022). Sauté RL: Almost surely safe reinforcement learning using state augmentation. In International Conference on Machine Learning (ICML). 
[33] Stooke, A., Achiam, J., and Abbeel, P. (2020). Responsive safety in reinforcement learning by pid Lagrangian methods. In International Conference on Machine Learning (ICML), pages 9133–9143. 
[34] Strehl, A. L. and Littman, M. L. (2005). A theoretical analysis of model-based interval estimation. In International Conference on Machine Learning (ICML). 
[35] Strehl, A. L. and Littman, M. L. (2008). An analysis of model-based interval estimation for Markov decision processes. Journal of Computer and System Sciences, 74(8):1309–1331. 
[36] Sui, Y., Gotovos, A., Burdick, J. W., and Krause, A. (2015). Safe exploration for optimization with Gaussian processes. In International Conference on Machine Learning (ICML). 
[37] Sun, H., Xu, Z., Fang, M., Peng, Z., Guo, J., Dai, B., and Zhou, B. (2021). Safe exploration by solving early terminated MDP. arXiv preprint arXiv:2107.04200. 
12
[38] Thananjeyan, B., Balakrishna, A., Nair, S., Luo, M., Srinivasan, K., Hwang, M., Gonzalez, J. E., Ibarz, J., Finn, C., and Goldberg, K. (2021). Recovery RL: Safe reinforcement learning with learned recovery zones. IEEE Robotics and Automation Letters, 6(3):4915–4922. 
[39] Thomas, G., Luo, Y., and Ma, T. (2021). Safe reinforcement learning by imagining the near future. In Neural Information Processing Systems (NeurIPS). 
[40] Turchetta, M., Kolobov, A., Shah, S., Krause, A., and Agarwal, A. (2020). Safe reinforcement learning via curriculum induction. In Neural Information Processing Systems (NeurIPS), volume 33, pages 12151–12162. 
[41] Wachi, A. and Sui, Y. (2020). Safe reinforcement learning in constrained Markov decision processes. In International Conference on Machine Learning (ICML). 
[42] Wachi, A., Sui, Y., Yue, Y., and Ono, M. (2018). Safe exploration and optimization of constrained MDPs using Gaussian processes. In AAAI Conference on Artificial Intelligence (AAAI). 
[43] Wachi, A., Wei, Y., and Sui, Y. (2021). Safe policy optimization with local generalized linear function approximations. In Neural Information Processing Systems (NeurIPS). 
[44] Wang, Y., Wang, R., Du, S. S., and Krishnamurthy, A. (2020). Optimism in reinforcement learning with generalized linear function approximation. In International Conference on Learning Representations (ICLR). 
[45] Wang, Y., Zhan, S. S., Jiao, R., Wang, Z., Jin, W., Yang, Z., Wang, Z., Huang, C., and Zhu, Q. (2023). Enforcing hard constraints with soft barriers: Safe reinforcement learning in unknown stochastic environments. In International Conference on Machine Learning, pages 36593–36604. PMLR. 
[46] Yang, L. and Wang, M. (2019). Sample-optimal parametric Q-learning using linearly additive features. In International Conference on Machine Learning (ICML). 
13
Appendices 
A Limitations and Potential Negative Societal Impacts 
We will first discuss limitations and potential negative societal impacts regarding our work. 
A.1 Limitations 
One of the major limitations of this study is that emergency stop actions are allowed for agents. Emergency stop actions should often be avoided because of the expensive cost of human intervention in many applications (e.g., the agent is in a hazardous or remote environment). In future work, we will investigate an algorithm that requires the agent to learn a reset policy allowing them to return to the initial state as in [15], rather than asking for human intervention via emergency stop actions. 
Another limitation is how to construct the uncertainty quantifier. In our experiment, because we used a computationally-inexpensive deep GP algorithm [30] and the uncertainty quantifier is updated at the end of the episode (see Line 13 in Algorithm 1), the computational time of the GP part was much smaller than the RL part in our experiment settings. However, since GP is a computationally-expensive algorithm in general, GP can be a computational bottleneck in some cases. 
A.2 Potential Negative Societal Impacts 
We believe that safety is an essential requirement for applying RL in many real problems. While we have not found any potential negative societal impact of our proposed method, we must remain aware that any RL algorithms are vulnerable to misuse and ours is no exception. 
B Proof of Theorem 3.1 
We first present lemmas regarding the relationship between the GSE problem and Problems 1, 2, and 3. After that, we present the proof for the Theorem 3.1 in Appendix B.4 by combining them. 
B.1 Relationship between the GSE problem and Problem 1 
Lemma B.1. Problem 1 can be transformed into the GSE problem. 
Proof. We first utilize a safety state augmentation technique presented in Sootla et al. [32] by defining a new variable ηh such that 
ηh := γ−h g · 
( ξ1 − 
h−1∑ h′=1 
γh′ 
g g(sh′ , ah′) 
) , ∀h ∈ [1, H]. (4) 
This new variable ηh means the remaining safety budget associated with the discount factor γg , which is updated as follows: 
ηh+1 = γ−1 g · ( ηh − g(sh, ah) ) with η0 = ξ1. (5) 
By (4), the necessary and sufficient condition for satisfying the constraint in Problem 1 is 
ηh ≥ 0, ∀h ∈ [1, H]. (6) 
By (5), we have 
ηh+1 ≥ 0, ∀h ∈ [1, H] ⇐⇒ ηh − g(sh, ah) ≥ 0, ∀h ∈ [1, H]. (7) 
In summary, by introducing the new variable ηh, Problem 1 is rewritten to the following problem: 
max π 
V π r subject to Pr[ g(sh, ah) ≤ ηh | P, π ] = 1, ∀h ∈ [1, H]. (8) 
The aforementioned problem (8) is a special case of the GSE problem with bh := ηh. Therefore, we obtain the desired lemma. 
14
B.2 Relationship between the GSE problem and Problem 2 
Lemma B.2. Problem 2 can be transformed into the GSE problem. 
Proof. The following chain of inequalities holds: 
E 
[ H∑ 
h=1 
γh g I(sh ∈ Sunsafe) 
∣∣∣∣∣ P, π 
] ≤ ξ2 
⇐⇒ E 
[ h∑ 
h′=1 
γh′ 
g I(sh′ ∈ Sunsafe) 
∣∣∣∣∣ P, π 
] ≤ ξ2, ∀h ∈ [1, H] 
⇐⇒ E [ γh g I(sh ∈ Sunsafe) 
∣∣ P, π ] ≤ ξ2 − E 
[ h−1∑ h′=1 
γh′ 
g I(sh′ ∈ Sunsafe) 
∣∣∣∣∣ P, π 
] , ∀h ∈ [2, H] 
⇐⇒ E [ I(sh ∈ Sunsafe) | P, π ] ≤ γ−h g 
{ ξ2 − E 
[ h−1∑ h′=1 
γh′ 
g I(sh′ ∈ Sunsafe) 
∣∣∣∣∣ P, π 
]} , ∀h ∈ [2, H] 
Because we assume Markov property, we simply define the safety cost function g : S ×A → R as 
g(sh, a) := E[ I(sh ∈ Sunsafe) | P, π ], ∀a ∈ A. 
We now set 
bh := γ−h g 
{ ξ2 − E 
[ h−1∑ h′=1 
γh′ 
g I(sh′ ∈ Sunsafe) 
∣∣∣∣∣ P, π 
]} , 
then the Problem 2 can be transformed into 
Pr[ g(s, a) ≤ bh | P, π ] = 1. 
Finally, we obtained the desired lemma. 
B.3 Relationship between the GSE problem and Problem 3 
Lemma B.3. Problem 3 can be transformed into the GSE problem. 
Proof. Set bh = ξ3 for all h. Then, the GSE problem is identical to Problem 3. 
B.4 Summary 
Proof. Combining Lemma B.1, B.2, and B.3, we obtain the desired Theorem 3.1. 
C Connections to Safe RL Problems with Chance Constraints 
As a strongly related formulation to Problem 2, policy optimization under joint chance-constraints has been studied especially in the field of control theory such as Ono et al. [24] and Pfrommer et al. [26], which is written as 
Problem 5 (Safe RL with joint chance constraints). Let ξ5 ∈ R≥0 be a constant representing a safety threshold. Also, let Sunsafe ⊂ S denote a set of unsafe states. Find the optimal policy π⋆ such that 
maxπ V π r subject to Pr 
[∨H h=1 sh ∈ Sunsafe 
∣∣∣ P, π ] ≤ ξ5. 
Lemma C.1. Problem 2 is a conservative approximation of Problem 5. 
15
Proof. This lemma mostly follows from Theorem 1 in Ono et al. [24]. Regarding the constraint in Problem 5, we have the following chain of equations: 
Pr 
[ H∨ 
h=1 
sh ∈ Sunsafe 
∣∣∣∣∣ P, π 
] ≤ 
H∑ h=1 
Pr [sh ∈ Sunsafe | P, π] 
= 
H∑ h=1 
E [ I(sh ∈ Sunsafe) | P, π ] (9) 
= E 
[ H∑ 
h=1 
I(sh ∈ Sunsafe) 
∣∣∣∣∣ P, π 
] . (10) 
In the first step, we used Boole’s inequality (i.e., Pr[A ∪ B] ≤ Pr[A] + Pr[B]). The final term in (10) is the LHS of the constraint in Problem 2, which implies that Problem 2 is a conservative approximation of Problem 5. Therefore, the GSE problem is also a conservative approximation of Problem 5. 
Corollary C.2. Suppose we solve the GSE problem by properly defining the safety function g(·, ·) and the threshold bh. Then, the obtained policy is a conservative solution of Problem 5. Remark C.3. It is extremely challenging to directly solve the Problem 5 characterized by joint chance-constraints without approximation, as discussed in Ono et al. [24]. Practically, it would be a promising and realistic approach to solve Problem 5 by converting it into the GSE problem. 
More detailed explanations for the aforementioned remark are as follows. It is extremely challenging to directly solve the Problem 5 characterized by joint chance-constraints. Most of the previous work does not directly deal with this type of constraint and uses some approximations or assumptions. For example, Pfrommer et al. [26] assume a known linear time-invariant dynamics. Also, Ono et al. [24] approximate the joint chance constraint as in the above procedure and obtain 
Pr 
[ H∨ 
h=1 
sh ∈ Sunsafe 
∣∣∣∣∣ P, π 
] ≤ E 
[ H∑ 
h=1 
I(sh ∈ Sunsafe) 
∣∣∣∣∣ P, π 
] . 
This is a conservative approximation with an additive structure, which is easier to solve than the original joint chance constraint. Ono et al. [24] deals with the above constraints with additive safety structure. By additionally transforming the conservatively-approximated problem into the GSE problem, the problem would become easier to handle because the safety constraint is instantaneous. 
D Proof of Theorems 4.1 and 4.2 
D.1 Proof of Theorem 4.1 
Proof. Recall that, at every time step h, the MASE chooses actions satisfying 
µ(sh, ah) + Γ(sh, ah) ≤ bh. (11) 
By definition of the δ-uncertainty quantifier, the actions that are conservatively chosen based on (11) also satisfy the safety constraint, with a probability of at least 1− δ; that is, 
g(sh, ah) ≤ bh. (12) 
In addition, when there is no action satisfying (11), the emergency stop action is executed; that is, safety is guaranteed with a probability of 1. Hence, the desired theorem is now obtained. 
D.2 Proof of Theorem 4.2 
Proof. Assumption 3.2 implies that there exists a policy that satisfies a more conservative safety constraint written as 
g(sh, ah) ≤ bh − ζ, ∀h ∈ [1, H]. (13) 
By combining (13) and the assumption Γ(s, a) ≤ 1 2ζ,∀(s, a) ∈ S ×A, we have 
µ(sh, ah) + Γ(sh, ah) ≤ g(sh, ah) + ζ ≤ bh, ∀h ∈ [1, H], (14) 
16
Algorithm 2 GLM-MASE 
1: for episode t = 1, 2, · · · , T do 2: for time h = 1, . . . ,H do 3: Take action ah = π(sh) within A+ 
h 4: Receive reward r(sh, ah) and next state sh+1 
5: Receive safety cost g(sh, ah) and update safety threshold bh+1 
6: if A+ h = ∅ then 
7: Compute r̂(sh, ah) = − c mina∈A Γ(sh+1,a) 
8: Append (sh, ah, r̂(sh, ah), sh+1) to D 9: break (i.e., emergency stop action â) 
10: else 11: Append (sh, ah, r(sh, ah), sh+1) to D 12: Update θ̂gh,t and θ̂Qh,t 13: Compute the optimistic Q-estimate 
Q̂ (t) r̂,h(s, a) = min{Vmax, f(⟨ϕs,a, θ̂ 
Q h,t⟩) + CQ/gΓ(s, a)} 
14: Optimize the policy by π (t) h (s) = argmax 
a∈A Q̂ 
(t) r̂,h(s, a). 
15: Update Γ(s, a) := Cg · ∥ϕs,a∥Λ−1 h,t 
and then rewrite D 
which guarantees that there exists a policy that conservatively satisfies the safety constraint via the δ-uncertainty quantifier Γ(·, ·) at every time step h, with a probability of at least 1− δ. 
When we set c to be a sufficiently large scalar such that c > ζ 2γH 
r Vmax, the penalty r̂ satisfies 
r̂(sh, ah) = −c 
mina∈A Γ(sh+1, a) 
< − 1 
2ζ · 1 
γH r Vmax 
1 2ζ 
< −γ−H r Vmax. 
This means that, when the constraint violation happens even a single time, the value by a policy obtained in M̂ becomes negative because maxs V 
π r (s) ≤ Vmax. 
Under Assumption 3.2, after convergence, the optimal policy in M̂ will not violate the safety constraint, and thus the emergency stop action â will not be executed. In this case, the modified (unconstrained) MDP M̂ is identical to the original CMDP M. Therefore, we now obtain the desired theorem. 
E Supplementary materials regarding GLM-MASE 
E.1 Pseudo-code for GLM-MASE 
We first present the pseudo-code for GLM-MASE in Algorithm 2. 
E.2 Proofs of Lemmas 5.4 and 5.5 
Proof. See Lemma 1 (and Lemma 7) in Wang et al. [44]. 
E.3 Preliminary Lemmas 
Lemma E.1. Suppose the assumptions in Lemma 5.4 and 5.5 hold. Let C1 and C2 be positive, universal constants. Also, with a sufficiently large T , let t⋆ denote the smallest integer satisfying 
λmin(Σ)tH − C1 
√ tHd− C2 
√ tH ln δ−1 ≥ 2 · Cg · ζ−1 (15) 
17
where λmin(Σ) is the minimum eigenvalue of the second moment matrix Σ. Then, we have 
Γ(s (t) h , a 
(t) h ) ≤ 1 
2 · ζ. (16) 
Proof. By Proposition 1 of Li et al. [22], 
λmin(Λh,t) ≥ λmin(Σ)tH − C1 
√ tHd− C2 
√ tH ln δ−1. 
By combining the aforementioned inequality with (15), we have 
λmin(Λh,t) ≥ 2 · Cg · ζ−1. 
Using the definition of λmax(Λ −1 h,t) = 1 
λmin(Λh,t) , the following chain of equations hold for all 
t ∈ [t⋆, T ] and h ∈ [1, H]: 
Γ(s (t) h , a 
(t) h ) = Cg · ∥ϕs,a∥Λ−1 
h,t 
≤ Cg · λmax(Λ −1 h,t) 
= Cg · λ−1 min(Λh,t) 
≤ 1 
2 ζ. 
Therefore, we have the desired lemma. 
E.4 Proof of Theorem 5.6 
Proof. By definition, the GLM-MASE chooses actions satisfying 
f(⟨ ϕ̃(τ) h , θ̂gh,t ⟩) + Γ(s 
(t) h , a 
(t) h ) ≤ bh. (17) 
By Lemma 5.4, the actions that are conservatively chosen based on (17) also satisfy the actual safety constraint, with a probability at least 1− δ; that is, 
g(s (t) h , a 
(t) h ) ≤ bh. (18) 
In addition, when there is no action satisfying (17), the emergency stop action is executed where no unsafe action will be executed. Hence, the desired theorem is now obtained. 
E.5 Proof of Theorem 5.7 
By Assumption 3.2, the optimal policy π⋆ satisfies 
g(sh, π ⋆(sh)) ≤ bh − ζ, ∀h ∈ [1, H]. (19) 
Thus, the set of state-action pairs that are potentially visited by π⋆ are written as 
{ (s, a) ∈ S ×A | g(s, a) ≤ bh − ζ }, which satisfies the following chain of inequalities: 
{ (s, a) | g(s, a) ≤ bh − ζ } ⊆ { (s, a) | µ(s, a)− Γ(s, a) ≤ bh − ζ } ⊆ { (s, a) | µ(s, a) + Γ(s, a) ≤ bh }. 
The state and action spaces in the last line represent the set of state-action pairs that may be visited by the policy obtained by the MASE algorithm. We used Lemma 5.4 in the first line and Γ(s, a) < ζ 
2 in the second line. 
By Lemma 8 in Strehl and Littman [34], the total regret can be decomposed into two parts as follows: T∑ 
t=t⋆ 
[ V π⋆ 
r − V πt r 
] = R(T ) + 
∑ t=t⋆ 
Vmaxδ, (20) 
where the first term is the regret under the condition that the confidence bound based on δ-uncertainty quantifier successfully contains the true safety function. Also, the second term is the regret under the opposite condition, which occurs with a probability δ. 
18
The first term in (20) is upper-bounded based on Wang et al. [44] as follows: 
R(T ) ≤ O 
( H √ (T − t⋆) ln((T − t⋆)H) 
+Hκκ−1 
√ M + κ+ d2 ln 
( κ+ αmax 
(T − t⋆)H 
) · (T − t⋆)d ln 
( 1 + 
(T − t⋆) 
d 
)) ≤ Õ(H 
√ d3(T − t⋆)). 
As for the second term in (20), set δ = 1 TH and then we have 
T∑ t=t⋆ 
Vmax · δ = 
T∑ t=t⋆ 
Vmax · 1 
TH 
= 
T∑ t=t⋆ 
1− γH 
1− γ · 1 
TH 
≤ T∑ 
t=t⋆ 
H · 1 
TH 
≤ O(1). 
In summary, the regret can be upper bounded by Õ(H √ 
d3(T − t⋆)). We now obtain the desired theorem. 
F Proof of Theorem 6.1 
Lemma F.1 (δ-uncertainty quantifier). Assume ∥g∥2k ≤ B and Nn ≤ ω for all n ≥ 1. Set 
Γ(s, a) := βn · σn(s, a), ∀(s, a) ∈ S ×A (21) 
with β 1/2 n := B + 4ω 
√ νn + 1 + ln δ−1, where νn is the information capacity associated with kernel 
k. Then, Γ is a δ-uncertainty quantifier. 
Proof. Recall the assumption that ∥g∥2k ≤ B and Nn ≤ ω, ∀n ≥ 1. Also, set 
β1/2 n := B + 4ω 
√ νn + 1 + ln δ−1. 
By Theorem 2 in Chowdhury and Gopalan [12], we have 
| g(s, a)− µn(s, a) | ≤ βn · σn(s, a), ∀(s, a) ∈ S ×A 
for all n ≥ 1, with probability at least 1− δ. Now, define 
Γ(s, a) := βn · σn(s, a), ∀(s, a) ∈ S ×A (22) 
then we interpret that Γ : S ×A → R is a δ-uncertainty quantifier based on GP. 
F.1 Proof of Theorem 6.1 
Proof. Based on Lemma F.1, when there is at least one safe action (i.e., A+ h ̸= ∅), the satisfaction of 
the safety constraint is guaranteed based on the δ-uncertainty quantifier with a probability at least 1− δ. Also, if there is no safe action (i.e., A+ 
h = ∅), the emergency stop action is executed. In both cases, MASE guarantees the satisfaction of the safety constraint with probability at least 1− δ. 
19
Table 1: Hyper-parameters for Safety Gym experiments. 
NAME VALUE 
COMMON PARAMETERS 
NETWORK ARCHITECTURE [64, 64] ACTIVATION FUNCTION tanh LEARNING RATE (CRITIC) 5× 10−3 
LEARNING RATE (POLICY) 3× 10−4 
LEARNING RATE (PENALTY) 3× 10−2 
DISCOUNT FACTOR (REWARD) 0.99 DISCOUNT FACTOR (SAFETY) 0.99 STEPS PER EPOCH 10, 000 NUMBER OF GRADIENT STEPS 80 NUMBER OF EPOCHS 500 TARGET KL 0.01 
TRPO & CPO 
DAMPING COEFFICIENT 0.1 BACKTRACK COEFFICIENT 0.8 BACKTRACK ITERATIONS 10 LEARNING MARGIN FALSE 
MASE 
PENALTY FOR EMERGENCY STOP ACTIONS −1 DEEP GP NETWORK ARCHITECTURE [16, 16] NUMBER OF INDUCING POINTS 128 KERNEL FUNCTION RADIAL BASIS FUNCTION 
G Details of Safety-Gym Experiment 
We present the details regarding our experiments using Safety-Gym. Our experimental setting is based on Sootla et al. [32], which is slightly different from the original Safety Gym in that the obstacles (i.e., unsafe region) are replaced deterministically so that the environment is solvable and there is a viable solution. In this experiment, we used a machine with Intel(R) Xeon(R) Silver 4210 CPU, 128GB RAM, and NVIDIA A100 GPU. For a fair comparison, we basically used the same hyper-parameter as in Sootla et al. [32], which is summarized in Table 1. 
In our experiment, when the agent identified that there was no safe action based on the GP-based uncertainty quantifier, we simply terminated the current episode (i.e., resetting) immediately after the emergency stop action and started the new episode. The frequency of the emergency stop actions is shown in the Table 2. 
Table 2: Frequency of the emergency stop actions. 
TASK TOTAL LAST 100 EPISODES 
POINTGOAL1 154/500 24/100 CARGOAL1 397/500 46/100 
The emergency stop action is a variant of so-called resetting actions that are common in episodic RL settings, which prevent the agent from exploring the state-action spaces since the uncertainty quantifier is sometimes quite conservative. We consider that this is the reason why the reward performance of our MASE is worse than other methods (e.g., TRPO-Lagrangian, CPO). However, because we require the agent to solve more difficult problems where safety is guaranteed at every time step and episode, we consider that this result is reasonable to some extent. Though it is better for an algorithm for such a severe safety constraint to have a comparable performance as CPO, we will leave it for future work. 
We also conducted an experiment to compare the performance of MASE with the early-terminated MDP (ET-MDP, [37]) algorithm. The ET-MDP is an algorithm to execute emergency stop actions immediately after safety constraints are violated. Figure 4 shows the experimental results. The ET-MDP and MASE exhibit similar learning curves on the average episode reward and average episode safety. However, while ET-MDP violated the safety constraint in most episodes (i.e., almost 
20
0 100 200 300 400 500 Epoch 
−0.5 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE 
(a) Average episode return. 
0 100 200 300 400 500 Epoch 
0 
10 
20 
30 
40 
50 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE Safety threshold 
(b) Average episode safety. 
0 100 200 300 400 500 Epoch 
0 
20 
40 
60 
80 
100 
120 
140 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE Safety threshold 
(c) Maximum episode safety. 
0 100 200 300 400 500 Epoch 
−0.5 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE 
(d) Average episode return. 
0 100 200 300 400 500 Epoch 
0 
5 
10 
15 
20 
25 
30 
35 
40 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE Safety threshold 
(e) Average episode safety. 
0 100 200 300 400 500 Epoch 
0 
20 
40 
60 
80 
100 
120 
140 
160 TRPO TRPO Lag CPO ET MDP Saute TRPO MASE Safety threshold 
(f) Maximum episode safety. 
Figure 4: Experimental results on Safety Gym (Top: PointGoal1, Bottom: CarGoal1) with an additional implementation of the Early-terminated MDP (ET-MDP) algorithm (Sun et al. [37]). 
all episodes are terminated after an unsafe action is executed), MASE did not violate any safety constraint. 
H Grid-world Experiment 
We also conduct an experiment using the grid-world problem as in Wachi and Sui [41]. Experimental settings are based on their original implementation (https://github.com/akifumi-wachi-4/ safe_near_optimal_mdp). We consider a 20×20 square grid in which reward and safety functions are randomly generated. There are two types regarding the safety threshold: one is time-invariant as in [41] and the other is time-variant as in the GSE problem. 
We run SNO-MDP [41] and MASE in 100 randomly generated environments, and we compute the reward collected by the algorithms and count the number of episodes in which the safety constraint is violated at least once. The reward is normalized with respect to that by SNO-MDP. 
Table 3: Experimental results for grid-world experiments. 
TIME-INVARIANT SAFETY THRESHOLD TIME-VARIANT SAFETY THRESHOLD 
REWARD SAFETY VIOLATION REWARD SAFETY VIOLATION 
SNO-MDP [41] 1.0± 0.0 0 1.0± 0.0 87 MASE (OURS) 1.0± 0.0 0 2.4± 1.0 0 
The experimental results are shown in Table 3. When the safety threshold is time-invariant, MASE behaves identically with SNO-MDP; thus, the performance of the MASE is comparable with that of SNO-MDP. When the safety threshold is time-variant, SNO-MDP cannot deal with it by nature; hence, the safety constraint is not satisfied in most of the episodes. In contrast, our MASE satisfies the safety constraint in every episode, which also contributes to the larger reward. 
21