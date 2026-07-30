> Source: https://arxiv.org/pdf/2209.15320

Bounded Robustness in Reinforcement Learning via Lexicographic Objectives 
Daniel Jarne Ornia D.JARNEORNIA@TUDELFT.NL Delft University of Technology 
Licio Romao LICIO.ROMAO@CS.OX.AC.UK University of Oxford 
Lewis Hammond LEWIS.HAMMOND@CS.OX.AC.UK University of Oxford 
Manuel Mazo Jr. M.MAZO@TUDELFT.NL Delft University of Technology 
Alessandro Abate ALESSANDRO.ABATE@CS.OX.AC.UK 
University of Oxford 
Abstract Policy robustness in Reinforcement Learning may not be desirable at any cost: the alterations caused by robustness requirements from otherwise optimal policies should be explainable, quantifiable and formally verifiable. In this work we study how policies can be maximally robust to arbitrary observational noise by analysing how they are altered by this noise through a stochastic linear operator interpretation of the disturbances, and establish connections between robustness and properties of the noise kernel and of the underlying MDPs. Then, we construct sufficient conditions for policy robustness, and propose a robustness-inducing scheme, applicable to any policy gradient algorithm, that formally trades off expected policy utility for robustness through lexicographic optimisation, while preserving convergence and sub-optimality in the policy synthesis. 
1. Introduction 
Consider a dynamical system where we need to synthesise a controller (policy) through a model-free Reinfrocement Learning (Sutton and Barto, 2018) approach. When using a simulator for training we expect the deployment of the controller in the real system to be affected by different sources of noise, possibly not predictable or modelled (e.g. for networked components we may have sensor faults, communication delays, etc). In safety-critical systems, robustness (in terms of successfully controlling the system under disturbances) should preserve formal guarantees, and plenty of effort has been put on developing formal convergence guarantees on policy gradient algorithms (Agar-wal et al., 2021; Bhandari and Russo, 2019). All these guarantees vanish under regularization and adversarial approaches, which are aimed to produce more robust policies. Therefore, for such applications one needs a scheme to regulate the robustness-utility trade-off in RL policies, that on the one hand preserves the formal guarantees of the original algorithms, and on the other attains sub-optimality conditions from the original problem. Additionally, if we do not know the structure of the disturbance (which holds in most applications), learning directly a policy for an arbitrarily disturbed environment will yield unexpected behaviours when deployed in the true system. 
1 
 
 
 
 
 
 
 
 
 
 
 
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Lexicographic Reinforcement Learning (LRL) Recently, lexicographic optimisation (Isermann, 1982; Rentmeesters et al., 1996) has been applied to the multi-objective RL setting (Skalse et al., 2022b). In an LRL setting some objectives may be more important than others, and so we may want to obtain policies that solve the multi-objective problem in a lexicographically prioritised way, i.e., “find the policies that optimise objective i (reasonably well), and from those the ones that optimise objective i+ 1 (reasonably well), and so on”. 
Previous Work In robustness against model uncertainty, the MDP may have noisy or uncertain reward signals or transition probabilities, as well as possible resulting distributional shifts in the training data (Heger, 1994; Xu and Mannor, 2006; Fu et al., 2018; Pattanaik et al., 2018; Pirotta et al., 2013; Abdullah et al., 2019), connecting to ideas on distributionally robust optimisation (Wiese-mann et al., 2014; Van Parys et al., 2015). For adversarial attacks or disturbances on policies or action selection in RL agents (Gleave et al., 2020; Lin et al., 2017; Tessler et al., 2019; Pan et al., 2019; Tan et al., 2020; Klima et al., 2019; Liang et al., 2022), recently Gleave et al. (2020) propose to attack RL agents by swapping the policy for an adversarial one at given times. For a detailed review on Robust RL see Moos et al. (2022). Our work focuses in robustness versus observational disturbances, where agents observe a disturbed state measurement and use it as input for the policy (Kos and Song, 2017; Huang et al., 2017; Behzadan and Munir, 2017; Mandlekar et al., 2017; Zhang et al., 2020, 2021). Zhang et al. (2020) propose a state-adversarial MDP framework, and utilise adversarial regularising terms that can be added to different deep RL algorithms to make the resulting policies more robust to observational disturbances, and Zhang et al. (2021) study how LSTM increases robustness with optimal state-perturbing adversaries. 
Contributions Most existing work on RL with observational disturbances proposes modifying RL algorithms at the cost of explainability (in terms of sub-optimality bounds) and verifiability, since the induced changes in the new policies result in a loss of convergence guarantees. Our main contributions are summarised in the following points. 
 We consider general unknown stochastic disturbances and formulate a quantitative definition of observational robustness that allows us to characterise the sets of robust policies for any MDP in the form of operator-invariant sets. We analyse how the structure of these sets depends on the MDP and noise kernel, and obtain an inclusion relation providing intuition into how we can search for robust policies more effectively.1 
 We propose a meta-algorithm that can be applied to any existing policy gradient algorithm, Lexicographically Robust Policy Gradient (LRPG) that (1) Retains policy sub-optimality up to a specified tolerance while maximising robustness, (2) Formally controls the utilityrobustness trade-off through this design tolerance, (3) Preserves formal guarantees. 
Figure 1 represents a qualitative interpretation of the results in this work. 
1.1. Preliminaries 
1. There are strong connections between Sections 2-3 in this paper and the literature on planning for POMDPs (Spaan and Vlassis, 2004; Spaan, 2012) and MDP invariances (Ng et al., 1999; van der Pol et al., 2020; Skalse et al., 2022a), as well as recent work concerning robustness misspecification (Korkmaz, 2023). 
2
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
Π 
Π0 
ΠD 
ΠT 
Π Π∗ 
πt 
? 
Π 
Π0 
ΠD 
ΠT 
Π Π∗ 
πt 
{π ∈ Π : J∗ − J(π) ≤ ϵ} 
Figure 1: Qualitative representation LRPG (right), compared to usual robustness-inducing algorithms. The sets in blue are the robust policies to be defined in the coming sections. LRPG induces robustness while guaranteeing that the policies will deviate a bounded distance from the optimal. 
Notation We use calligraphic letters A for collections of sets and ∆(A) as the space of probability measures over A. For two probability distributions P, P ′ defined on the same σ−algebra F , DTV (P∥P ′) = supA∈F |P (A) − P ′(A)| is the total variation distance. For two elements of a vector space we use ⟨·, ·⟩ as the inner product. We use 1n as a column-vector of size n that has all entries equal to 1. We say that an MDP is ergodic if for any policy the resulting Markov Chain (MC) is ergodic. We say that S is a n × n rowstochastic matrix if Sij ≥ 0 and each row of S sums 1. We assume all learning rates in this work αt(x, u) ∈ [0, 1] (βt, ηt...) satisfy the conditions 
∑∞ t=1 αt(x, u) =∞ and 
∑∞ t=1 αt(x, u) 
2 <∞. 
Lexicographic Reinforcement Learning Consider a parameterised policy πθ with θ ∈ Θ, and two objective functions K1 and K2. PB-LRL uses a multi-timescale optimisation scheme to optimise θ faster for higher-priority objectives, iteratively updating the constraints induced by these priorities and encoding them via Lagrangian relaxation techniques (Bertsekas, 1997). Let θ′ ∈ argmaxθ K1(θ). Then, PB-LRL can be used to find parameters θ′′ ∈ {argmaxθ K2(θ), s.t. K1(θ) ≥ K1(θ 
′)− ϵ}. This is done through the update: 
θ ←projΘ [ θ +∇θK̂(θ) 
] , λ← projR≥0 
[ λ+ ηt(k̂1 − ϵt −K1(θ)) 
] , (1) 
where K̂(θ) := (β1 t +λβ2 
t ) ·K1(θ)+β2 t ·K2(θ), λ is a Langrange multiplier, β1 
t , β 2 t , ηt are learning 
rates, and k̂1 is an estimate of K1(θ ′). Typically, we set ϵt → 0, though we can use other tolerances 
too, e.g., ϵt = 0.9 · k̂1. For more details see Skalse et al. (2022b). 
2. Observationally Robust Reinforcement Learning 
Robustness-inducing methods in model-free RL must address the following dilemma: How do we deal with uncertainty without an explicit mechanism to estimate such uncertainty during policy execution? Consider an example of an MDP where, at policy roll-out phase, there is a non-zero probability of measuring a “wrong” state. In such a scenario, measuring the wrong state can lead to executing unboundedly bad actions. This problem is represented by the following version of a noise-induced partially observable Markov Decision Process (Spaan, 2012). 
Definition 1 An observationally-disturbed MDP (DOMDP) is (a POMDP) defined by the tuple (X,U, P,R, T, γ) where X is a finite set of states, U is a set of actions, P : U × X 7→ ∆(X) is a probability measure of the transitions between states and R : X × U × X 7→ R is a reward function. The map T : X 7→ ∆(X) is a stochastic kernel induced by some unknown noise signal, such that T (y | x) is the probability of measuring y while the true state is x, and acts only on the state observations. At last γ ∈ [0, 1] is a reward discount. 
3
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
A (memoryless) policy for the agent is a stochastic kernel π : X 7→ ∆(U). For simplicity, we overload notation on π, denoting by π(x, u) as the probability of taking action u at state x. In a DOMDP2 agents can measure the full state, but the measurement will be disturbed by some unknown random signal in the policy deployment. The difficulty of acting in such DOMDP is that agents will have to act based on disturbed states x̃ ∼ T (· | x). We then need to construct policies that will be as robust as possible against such noise without the existance of a model to estimate, filter or reject disturbances. The value function of a policy π (critic), V π : X 7→ R, is given by V π(x0) = E[ 
∑∞ t=0 γ 
tR(xt, π(xt), xt+1)]. The action-value function of π (Q-function) is given by Qπ(x, u) = 
∑ y∈X P (x, u, y)(R(x, u, y) + γV π(y)). We then define the objective function as 
J(π) := Ex0∼µ0 [V π(x0)] with µ0 being a distribution of initial states, and we use J∗ := maxπ J(π) 
and π∗ as the optimal policy, and Π∗ ϵ := {π ∈ Π : J∗ − J(π) ≤ ϵ} is the set of ϵ-optimal policies. 
If a policy is parameterised by θ ∈ Θ we write πθ and J(θ). 
Assumption 1 For any DOMDP and policy π, the resulting MC is irreducible and aperiodic. 
We now formalise a notion of observational robustness. Firstly, due to the presence of the stochastic kernel T , the policy we are applying is altered as we are applying a collection of actions in a possibly wrong state. Then, ⟨π, T ⟩(x, u) := 
∑ y∈X T (y | x)π(y, u), where ⟨π, T ⟩ : X 7→ ∆(U) is the 
disturbed policy, which averages the current policy given the error induced by the presence of the stochastic kernel. Notice that ⟨·, T ⟩(x) : Π 7→ ∆(U) is an averaging operator yielding the alteration of the policy due to noise. We define the robustness regret3: ρ(π, T ) := J(π)− J(⟨π, T ⟩). 
Definition 2 (Policy Robustness) A policy π is κ-robust against a stochastic kernel T if ρ(π, T ) ≤ κ. If π is 0-robust it is maximally robust. The sets of κ-robust policies are Πκ := {π ∈ Π : ρ(π, T ) ≤ κ}, with Π0 being the maximally robust policies. 
One can motivate the characterisation and models above from a control perspective, where policies use as input discretised state measurements with possible sensor measurement errors. Formally ensuring robustness properties when learning RL policies will, in general, force the resulting policies to deviate from optimality in the undisturbed MDP. We propose then the following problem. 
Problem 1 Consider a DOMDP model as per Definition 1 and let ϵ be a non-negative tolerance level. Our goal is to find amongst all ϵ-optimal policies those that minimize the robustness level κ: 
minimize κ s.t. π ∈ Π⋆ ϵ ∩Πκ. 
Note that this is formulated as general as possible with respect to the robustness of the policies: We would like to find a policy that, trading off ϵ in terms of cumulative rewards, observes the same discounted rewards when disturbed by T . 
3. Characterisation of Robust Policies 
An important question to be addressed before trying to synthesise robust policies is what these robust policies look like, and how they are related to DOMDP properties. A policy π is said to be 
2. Definition 1 is a generalised form of the State-Adversarial MDP used by Zhang et al. (2020): the adversarial case is a particular form of DOMDP where T assigns probability 1 to one adversarial state. 
3. The robustness regret satisfies ρ(π∗, T ) ≥ 0 for all kernels T , and it allows us to directly compare the robustness regret with the utility regret of the policy. 
4
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
constant if π(x) = π(y) for all x, y ∈ X , and the collection of all constant policies is denoted by Π̄. A policy is called a fixed point of ⟨·, T ⟩ if π(x) = ⟨π, T ⟩(x) for all x ∈ X . The collection of all fixed points is ΠT . Observe furthermore that ΠT only depends on the kernel T and the set4 X . Let us assume we have a policy iteration algorithm that employs an action-value function Qπ and policy π. The advantage function for π is defined as Aπ(x, u) := Qπ(x, u) − V π(x). We can similarly define the noise disadvantage of policy π as: 
Dπ(x, T ) := V π(x)− Eu∼⟨π,T ⟩(x)[Q π(x, u)], (2) 
which measures the difference of applying at state x an action according to the policy π with that of playing an action according to ⟨π, T ⟩ and then continuing playing an action according to π. Our intuition says that if it happens to be the case that Dπ(x, T ) = 0 for all states in the DOMDP, then such a policy is maximally robust. And this is indeed the case, as shown in the next proposition. 
Proposition 3 Consider a DOMDP as in Definition 1 and the robustness notion as in Definition 2. If a policy π is such that Dπ(x, T ) = 0 for all x ∈ X , then π is maximally robust, i.e., let ΠD := {π ∈ Π : µπ(x)D 
π(x, T ) = 0∀x ∈ X}, then we have that ΠD ⊆ Π0. Proof We want to show that Dπ(x, T ) = 0 =⇒ ρ(π, T ) = 0. Taking Dπ(x, T ) = 0 one has a policy that produces an disadvantage of zero when noise kernel T is applied. Then, ∀x ∈ X, 
Dπ(x, T ) = 0 =⇒ Eu∼⟨π,T ⟩(x)[Q π(x, u)] = V π(x). (3) 
Now define the value of the disturbed policy as V ⟨π,T ⟩(x) = Eu∼⟨π,T ⟩(x), y∼P (·|x,u) 
[ r(x, u, y) + γV ⟨π,T ⟩(y) 
] . 
We will now show that V π(x) = V ⟨π,T ⟩(x), for all x ∈ X . Observe, from (3) using V π(x) = Eu∼⟨π,T ⟩(x)[Q 
π(x, u)], we have ∀x ∈ X: 
V π(x)− V ⟨π,T ⟩(x) = Eu∼⟨π,T ⟩(x)[Q π(x, u)]− Eu∼⟨π,T ⟩(x) 
y∼P (·|x,u) 
[ r(x, u, y) + γV ⟨π,T ⟩(y) 
] = 
= Eu∼⟨π,T ⟩(x) y∼P (·|x,u) 
[ γV π(y)− γV ⟨π,T ⟩(y) 
] = γEy∼P (·|x,u) 
[ V π(y)− V ⟨π,T ⟩(y) 
] . 
(4) 
Now, taking the sup norm at both sides of (4) we get 
∥V π(x)− V ⟨π,T ⟩(x)∥∞ = γ ∥∥∥Ey∼P (·|x,u) 
[ V π(y)− V ⟨π,T ⟩(y) 
]∥∥∥ ∞ . (5) 
Since the norm on the right hand side of (5) is over y ∈ X and γ < 1, it follows that ∥V π(x) − V ⟨π,T ⟩(x)∥∞ = 0. Finally, ∥V π(x) − V ⟨π,T ⟩(x)∥∞ = 0 =⇒ V π(x) − V ⟨π,T ⟩(x) = 0 ∀x ∈ X , and V π(x)− V ⟨π,T ⟩(x) = 0 ∀x ∈ X =⇒ J(π) = J(⟨π, T ⟩) =⇒ ρ(π, T ) = 0. 
So far we have shown that both the set of fixed points Π and the set of policies for which the disadvantage function is equal to zero ΠD are contained in the set of maximally robust policies. We now show how the defined robust policy sets can be linked in a single result through the following policy inclusions. 
4. There is a (natural) bijection between the set of constant policies and the space ∆(U). The set of fixed points of the operator ⟨·, T ⟩ also has an algebraic characterisation in terms of the null space of the operator Id(·)− ⟨·, T ⟩. We are not exploiting the later characterisation in this paper. 
5
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Theorem 4 (Policy Inclusions) For a DOMDP with noise kernel T , consider the sets Π,ΠT ,ΠD 
and Π0. Then, the following inclusion relation holds: Π ⊆ ΠT ⊆ ΠD ⊆ Π0. Additionally, the sets Π,ΠT are convex for all MDPs and kernels T , but ΠD,Π0 may not be. 
Proof If a policy π ∈ Π is a fixed point of the operator ⟨·, T ⟩, then ρ(π, T ) = J(π)− J(⟨π, T ⟩) = J(π) − J(π) = 0 =⇒ π ∈ Π0. Therefore, ΠT ⊆ Π0. Now, the space of stochastic kernels K : X 7→ ∆(X) is equivalent to the space of row-stochastic |X| × |X| matrices, therefore one can write T (y | x) ≡ Txy as the xy−th entry of the matrix T . Then, the representation of a constant policy as an X × U matrix can be written as π = 1|X|v 
⊤, where 1|X| where v ∈ ∆(U) is any probability distribution over the action space. Observe that, applying the operator ⟨π, T ⟩ to a constant policy yields ⟨π, T ⟩ = T1|X|v 
⊤. By the Perron-Frobenius Theorem (Horn and Johnson, 2012), since T is row-stochastic it has at least one eigenvalue eig(T ) = 1, and this admits a (strictly positive) eigenvector T1|X| = 1|X|. Therefore, ⟨π, T ⟩ = T1|X|v 
⊤ = 1|X|v ⊤ = π =⇒ Π ⊆ ΠT . 
Combining this result with Proposition 3, we simply need to show that ΠT ⊂ ΠD. Take π to be a fixed point of ⟨π, T ⟩. Then ⟨π, T ⟩ = π, and from the definition in (2): 
Dπ(x, T ) = V π(x)− Eu∼⟨π,T ⟩(x,·)[Q π(x, u)] = V π(x)− Eu∼π(x,·)[Q 
π(x, u)] = 0. 
Therefore, π ∈ ΠD, which completes the sequence of inclusions. Convexity of Π,ΠT follows from considering the convex hulls of two constant or fixed point policies. 
Let us reflect on the inclusion relations of Theorem 4. The inclusions are in general not strict, and in fact the geometry of the sets (as well as whether some of the relations are in fact equalities) is highly dependent on the reward function, and in particular on the complexity (from an informationtheoretic perspective) of the reward function. As an intuition, less complex reward functions (more uniform) will make the inclusions above expand to the entire policy set, and more complex reward functions will make the relations collapse to equalities. 
Corollary 5 For any ergodic DOMDP there exist reward functions R and R such that the resulting DOMDP satisfies A) ΠD = Π0 = Π (any policy is max. robust) if R = R, and B) ΠT = ΠD = Π0 
(only fixed point policies are maximally robust) if R = R. 
Proof [Corollary 5] For statement A) let R(·, ·, ·) = c for some constant c ∈ R. Then, J(π) = Ex0∼µ0 [ 
∑ t γ 
trt | π] = cγ 1−γ , which does not depend on the policy π. For any noise kernel T and 
policy π, J(π) − J⟨π, T ⟩ = 0 =⇒ π ∈ Π0. For statement B assume ∃π ∈ Π0 : π /∈ ΠT . Then, ∃x∗ ∈ X and u∗ ∈ U such that π(x∗, u∗) ̸= ⟨π, T ⟩(x∗, u∗). Let R(x, u, x′) := c if x = x∗ 
and u = u∗, 0 otherwise. Then, E[R(x, π(x), x′] < E[R(x, ⟨π, T ⟩(x), x′] and since the MDP is ergodic x is visited infinitely often and J(π)− J(⟨π, T ⟩) > 0 =⇒ π /∈ Π0, which contradicts the assumption. Therefore, Π0 \ΠT = ∅ =⇒ Π0 = ΠT . 
We can now summarise the insights from Theorem 4 and Corollary 5 in the following conclusions: (1) The set Π is maximally robust, convex and independent of the DOMDP, (2) The set ΠT is maximally robust, convex, includes Π, and its properties only depend on T , (3) The set ΠD includes ΠT and is maximally robust, but its properties depend on the DOMDP. 
6
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
4. Robustness through Lexicographic Objectives 
To be able to apply LRL results to our robustness problem we need to first cast robustness as a valid objective to be maximised, and then show that a stochastic gradient descent approach would indeed find a global maximum of the objective, therefore yielding a maximally robust policy. 5 
Algorithm 1 LRPG 
input Simulator, T̃ , ϵ initialise θ, critic (if using), λ, {β1 
t , β 2 t , η} 
set t = 0, xt ∼ µ0 
while t < max iterations do perform ut ∼ πθ(xt) observe rt, xt+1, sample y ∼ T̃ (· | x) if K̂1(θ) not converged then 
k̂1 ← K̂1(θ) end if update critic (if using) update θ using (8) and λ using (1) 
end while output θ 
Proposed approach Following the framework presented in previous sections, we propose the following approach to obtain lexicographic robustness. In the introduction, we emphasised that the motivation for this work comes partially from the fact that we may not know T in reality, or have a way to estimate it. However, the theoretical results until now depend on T . Our proposed solution to this lies in the results of Theorem 4. We can use a design generator T̃ to perturb the policy during training such that T̃ has the smallest possible fixed point set (i.e. the constant policy set, T̃ satisfies ΠT̃ = Π), and any algorithm that drives the policy towards the set of fixed points of T̃ will also drive the policy towards fixed points of T : from Theorem 4, ΠT̃ ⊆ ΠT . 
4.1. Lexicographically Robust Policy Gradient 
Consider then the objective to be minimised: 
KT̃ (θ) = 1 
2 
∑ x∈X 
µπθ (x) 
∑ u∈U 
( πθ(x, u)− ⟨πθ, T̃ ⟩(x, u) 
)2 , (6) 
Notice that optimising (6) projects the current policy onto the set of fixed points of the operator ⟨·, T̃ ⟩, and due to Assumption 1, which requires µπθ 
(x) > 0 for all x ∈ X , the optimal solution is equal to zero if and only if there exists a value of the parameter θ for which the corresponding πθ is a fixed point of ⟨·, T̃ ⟩. We present now the proposed LRPG meta-algorithm to achieve lexicographic robustness for any policy gradient algorithm at choice. From Skalse et al. (2022b), the convergence of PB-LRL algorithms is guaranteed as long as the original policy gradient algorithm for each single objective converges. 
Assumption 2 The policy is updated through an algorithm (e.g. A2C, PPO...) such that θt+1 ← projΘ 
[ θt + αt∇θtK̂1 
] converges a.s. to a (local or global) optimum θ∗. 
Theorem 6 Consider a DOMDP as in Definition 1 and let πθ be a parameterised policy. Take a design kernel T̃ ∈ {T : ΠT = Π}. Consider the following modified gradient for objective KT̃ (θ)(x) and sampled point y ∼ T̃ (· | x): 
∇θK̂ ′ T̃ (θ) = Ex∼µπθ 
[∑ u∈U 
(πθ(x, u)− πθ(y, u))∇θπθ(x, u) ] . (7) 
5. The advantage of using LRL is that we can formally bound the trade-off between robustness and optimality through ϵ, determinining how far we allow our resulting policy to be from an optimal policy in favour of it being more robust. 
7
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Given an ϵ > 0, if Assumptions 1 and 2 hold, then the following iteration (LRPG): 
θ ← projΘ [ θ + (β1 
t + λβ2 t ) · ∇θK̂1(θ) + β2 
t∇θK̂ ′ T̃ (θ) 
] (8) 
converges a.s. to parameters θϵ that satisfy θϵ ∈ argminθ∈Θ′ KT̃ (θ) such that K∗ 1 ≥ K1(θ 
ϵ) − ϵ, where Θ′ = Θ if θ∗ is globally optimal and a compact local neighbourhood of θ∗ otherwise. 
Proof To apply LRL results, we need to show that both gradient descent schemes converge (separately) to local or global maxima. Let us first show that θt+1 = projΘ 
[ θt−αt∇θK̂ 
′ T̃ (θt) 
] converges 
a.s. to parameters θ̃ satisfying KT̃ = 0. We prove this making use of fixed point iterations with non-expansive operators (specifically, Theorem 4, section 10.3 in Borkar (2008)). First, observe that for a tabular representation, πθ(x, u) = θxu, and ∇θπθ(x, u) is a vector of zeros, with value 1 for the position θxu. We can then write the SGD in terms of the policy for each state x, considering π(x) ≡ (θxu1 , θxu2 , ..., θxuk 
)T . Let y ∼ T̃ (· | x). Then: 
πt+1(x) = πt(x)− αt 
( πt(x)− πt(y) 
) = πt(x)− αt 
( πt(x)− ⟨πt, T̃ ⟩(x)− 
( πt(y)− ⟨πt, T̃ ⟩(x) 
)) . 
We now need to verify that the necessary conditions for applying Theorem 4, section 10.3 in Borkar (2008) hold. First, making use of the property ∥T̃∥∞ = 1 for any row-stochastic matrix T̃ , for any two policies π1, π2 ∈ Π: 
∥⟨π1, T̃ ⟩ − ⟨π2, T̃ ⟩∥∞ = ∥T̃ π1 − T̃ π2∥∞ = ∥T̃ (π1 − π2)∥∞ ≤ ∥T̃∥∞∥π1 − π2∥∞ = ∥π1 − π2∥∞. 
Therefore, the operator ⟨·, T̃ ⟩ is non-expansive with respect to the sup-norm. For the final condition: 
Ey∼T̃ (·|x) 
[ πt(y)− ⟨πt, T̃ ⟩(x) | πt, T̃ 
] = 
∑ y∈X 
T̃ (y | x)πt(y)− ⟨πt, T̃ ⟩(x) = 0. 
Therefore, the difference πt(y) − ⟨πt, T̃ ⟩(x) is a martingale difference for all x. One can then apply Theorem 4, sec. 10.3 (Borkar, 2008) to conclude that πt(x) → π̃(x) almost surely. Finally from Assumption 1, for any policy all states x ∈ X are visited infinitely often, therefore πt(x) → π̃(x)∀x ∈ X =⇒ πt → π̃ and π̃ satisfies ⟨π̃, T̃ ⟩ = π̃, and KT̃ (π̃) = 0. 
Now, from Assumption 2, the iteration θ ← projΘ [ θ + αt∇θK̂1 
] converges a.s. to a (local or 
global) optimum θ∗. Then, both objectives are invex Ben-Israel and Mond (1986b) (either locally or globally), and any linear combination of them will also be invex (again, locally or globally). Finally, we can directly apply the results from Skalse et al. (2022b), and 
θ ← projΘ [ θ + (β1 
t + λβ2 t ) · ∇θK̂1(θ) + β2 
t∇θK̂ ′ T̃ (θ) 
] converges a.s. to parameters θϵ that satisfy θϵ ∈ argminθ∈Θ′ KT̃ (θ) such that K∗ 
1 ≥ K1(θ ϵ) − ϵ, 
where Θ′ = Θ if θ∗ is globally optimal and a compact local neighbourhood of θ∗ otherwise. 
Remark 7 Observe that (7) is not the true gradient of (6), and θϵ ∈ argminθ∈Θ′ KT̃ (θ) if there exists a (local) minimum of KT̃ in Θϵ := {θ : K∗ 
1 ≥ K1(θ) − ϵ}. However, from Theorem 6 we know that the (pseudo) gradient descent scheme converges to a global minimum in the tabular case, therefore ⟨∇θK̂ 
′ T̃ (θ),∇θK̂T̃ (θ)⟩ < 0 (Borkar, 2008), and gradient-like descent schemes will 
converge to (local or) global minimisers, which motivates the choice of this gradient approximation. 
8
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
We reflect again on Figure 1. The main idea behind LRPG is that by formally expanding the set of acceptable policies with respect to K1, we may find robust policies more effectively while guaranteeing a minimum performance in terms of expected rewards. This addresses directly the premise behind Problem 1. In LRPG the first objective is still to minimise the distance J∗ − J(π) up to some tolerance. Then, from the policies that satisfy this constraint, we want to steer the learning algorithm towards a maximally robust policy, and we can do so without knowing T . 
5. Considerations on Noise Generators 
A natural question emerging is how to choose T̃ , and how the choice influences the resulting policy robustness towards any other true T . In general, for any arbitrary policy utility landscape in a given MDP, there is no way of bounding the distance of the resulting policies for two different noise kernels T1, T2. However, the optimality of the policy remains bounded: Through LRPG guarantees we know that, for both cases, the utility of the resulting policy will be at most ϵ far from the optimal. 
Corollary 8 Take T to be any arbitrary noise kernel, and T̃ to satisfy T̃ ∈ {T : ΠT = Π}. Let π be a policy resulting from a LRPG algorithm. Assume that minπ′∈ΠT̃ 
DTV (π∥π′) = a for some a < 1. Then, it holds for any T that minπ′∈ΠT 
DTV (π∥π′) ≤ a. 
Proof The proof follows by the inclusion results in Theorem 4. If ΠT̃ = Π, then ΠT̃ ⊆ ΠT for any other T . Then, the distance from π to the set ΠT is at most the distance to ΠT̃ . 
That is, when using LRPG to obtain a robust policy π, the resulting policy is at most a far from the set of fixed points (and therefore a maximally robust policy) with respect to the true T . This is the key argument behind our choices for T̃ : A priori, the most sensible choice is a kernel that has no other fixed point than the set of constant policies. This fixed point condition is satisfied in the discrete state case for any T̃ that induces an irreducible Markov Chain, and in continuous state for any T̃ that satisfies a reachability condition (i.e. for any x0 ∈ X , there exists a finite time for which the probability of reaching any ball B ⊂ X of radius r > 0 through a sequence xt+1 = T (xt) is measurable). This holds for (additive) uniform or Gaussian disturbances. 
6. Experiments 
We verify the theoretical results of LRPG in a series of experiments on discrete state/action safetyrelated environments (Chevalier-Boisvert et al., 2018) (for extended experiments in continuous control tasks, hyperparameters etc. see extended version). We use A2C (Sutton and Barto, 2018) (LR-A2C) and PPO (Schulman et al., 2017) (LR-PPO) for our implementations of LRPG. In all cases, the lexicographic tolerance was set to ϵ = 0.99k̂1 to deviate as little as possible from the primary objective. We compare against the baseline algorithms and against SA-PPO (Zhang et al., 2020) which is among the most effective (adversarial) robust RL approaches in literature. We trained 10 independent agents for each algorithm, and reported scores of the median agent (as in Zhang et al. (2020)) for 50 roll-outs. To simulate T̃ we disturb x as x̃ = x + ξ for (1) a uniform bounded noise signal ξ ∼ U[−b,b] (T̃ u) and (2) and a Gaussian noise (T̃ g) such that ξ ∼ N (0, 0.5). We test the resulting policies against a noiseless environment (∅), a kernel T1 = T̃ u, a kernel T2 = T̃ g 
and against two different state-adversarial noise configurations (T 2 adv) as proposed by Zhang et al. 
(2021) to evaluate how effective LRPG is at rejecting adversarial disturbances. 
9
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
PPO on MiniGrid Environments A2C on MiniGrid Environments 
Noise PPO LRPPO(Ku T ) LRPPO(K 
g T ) SA-PPO A2C LRA2C(K 
u T ) LRA2C(K 
g T ) LRA2C(KD) 
LavaGap ∅ 0.95±0.003 0.95±0.075 0.95±0.101 0.94±0.068 0.94±0.004 0.94±0.005 0.94±0.003 0.94±0.006 T1 0.80±0.041 0.95±0.078 0.93±0.124 0.88±0.064 0.83±0.061 0.93±0.019 0.89±0.032 0.91±0.088 T2 0.92±0.015 0.95±0.052 0.95±0.094 0.93±0.050 0.89±0.029 0.94±0.008 0.93±0.011 0.93±0.021 T2 adv 0.01±0.051 0.71±0.251 0.21±0.357 0.87±0.116 0.27±0.119 0.79±0.069 0.68±0.127 0.56±0.249 
LavaCrossing ∅ 0.95±0.023 0.93±0.050 0.93±0.018 0.88±0.091 0.91±0.024 0.91±0.063 0.90±0.017 0.92±0.034 T1 0.50±0.110 0.92±0.053 0.89±0.029 0.64±0.109 0.66±0.071 0.78±0.111 0.72±0.073 0.76±0.098 T2 0.84±0.061 0.92±0.050 0.92±0.021 0.85±0.094 0.78±0.054 0.83±0.105 0.86±0.029 0.87±0.063 T2 adv 0.0±0.004 0.50±0.171 0.38±0.020 0.82±0.072 0.06±0.056 0.04±0.030 0.01±0.008 0.09±0.060 
DynamicObstacles ∅ 0.91±0.002 0.91±0.008 0.91±0.007 0.91±0.131 0.91±0.011 0.88±0.020 0.89±0.009 0.91±0.013 T1 0.23±0.201 0.77±0.102 0.61±0.119 0.45±0.188 0.27±0.104 0.43±0.108 0.45±0.162 0.56±0.270 T2 0.50±0.117 0.75±0.075 0.70±0.072 0.68±0.490 0.45±0.086 0.53±0.109 0.52±0.161 0.67±0.203 T2 adv -0.49±0.312 0.51±0.234 0.33±0.202 0.55±0.170 -0.54±0.209 -0.21±0.192 -0.53±0.261 -0.51±0.260 
Table 1: Reward values gained by LRPG and baselines on discrete control tasks. 
Robustness Results We use objectives as defined in (6). Additionally, we aim to test the hypothesis: If we have an estimator for the critic Qπ we can obtain robustness without inducing regularity in the policy using Dπ, yielding a larger policy subspace to steer towards, and hopefully achieving policies closer to optimal. For this, we consider the objective KD(θ)(x) := 1 
2∥Dπθ(x, T )∥22 by modifying A2C to retain a Q critic. We investigate the impact of LRPG PPO and A2C for discrete action-space problems on Gymnasium (Brockman et al., 2016). Minigrid-LavaGap (fully observable), Minigrid-LavaCrossing (partially observable) are safe exploration tasks where the agent needs to navigate an environment with cliff-like regions. Minigrid-DynamicObstacles (stochastic, partially observable) is a dynamic obstacle-avoidance environment. See Table 1. 
7. Discussion 
Experiments We applied LRPG on PPO and A2C (and SAC algorithms), for a set of discrete and continuous control environments. These environments are particularly sensitive to robustness problems; the rewards are sparse, and applying a sub-optimal action at any step of the trajectory often leads to terminal states with zero (or negative) reward. LRPG successfully induces lower robustness regrets in the tested scenarios, and the use of KD as an objective (even though we did not prove the convergence of a gradient based method with such objective) yields a better compromise between robustness and rewards. When compared to recent observational robustness methods, LRPG obtains similar robustness results while preserving the original guarantees of the chosen algorithm. 
Shortcomings and Contributions The motivation for LRPG comes from situations where, when deploying a model-free controller in a dynamical system, we do not have a way of estimating the noise generation and we are required to retain convergence guarantees of the algorithms used. Although LRPG is a useful approach for learning policies in control problems where the noise sources are unknown, questions emerge on whether there are more effective methods of incorporating robustness into RL policies when guarantees are not needed. Specifically, since a completely model-free approach does not allow for simple alternative solutions such as filtering or disturbance rejection, there are reasons to believe it could be outperformed by model-based (or model learning) approaches. However, we argue that in completely model-free settings, LRPG provides a rational strategy to robustify RL agents. 
10
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
References 
Mohammed Amin Abdullah, Hang Ren, Haitham Bou Ammar, Vladimir Milenkovic, Rui Luo, Mingtian Zhang, and Jun Wang. Wasserstein robust reinforcement learning. arXiv preprint arXiv:1907.13196, 2019. 
Alekh Agarwal, Sham M Kakade, Jason D Lee, and Gaurav Mahajan. On the theory of policy gradient methods: Optimality, approximation, and distribution shift. J. Mach. Learn. Res., 22 (98):1–76, 2021. 
Vahid Behzadan and Arslan Munir. Vulnerability of deep reinforcement learning to policy induction attacks. In International Conference on Machine Learning and Data Mining in Pattern Recogni-tion, pages 262–275. Springer, 2017. 
A. Ben-Israel and B. Mond. What is invexity? The Journal of the Australian Mathematical Society. Series B. Applied Mathematics, 28(1):1–9, 1986a. 
Adi Ben-Israel and Bertram Mond. What is invexity? The ANZIAM Journal, 28(1):1–9, 1986b. 
Dimitri Bertsekas. Nonlinear Programming. Athena Scientific, 1999. 
Dimitri P Bertsekas. Nonlinear programming. Journal of the Operational Research Society, 48(3): 334–334, 1997. 
Jalaj Bhandari and Daniel Russo. Global optimality guarantees for policy gradient methods. arXiv preprint arXiv:1906.01786, 2019. 
Vivek S. Borkar. Stochastic Approximation. Hindustan Book Agency, 2008. 
V.S. Borkar and K. Soumyanatha. An analog scheme for fixed point computation. i. theory. IEEE Transactions on Circuits and Systems I: Fundamental Theory and Applications, 44(4):351–355, 1997. doi: 10.1109/81.563625. 
Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba. Openai gym. arXiv preprint arXiv:1606.01540, 2016. 
Maxime Chevalier-Boisvert, Lucas Willems, and Suman Pal. Minimalistic gridworld environment for openai gym. https://github.com/maximecb/gym-minigrid, 2018. 
Justin Fu, Katie Luo, and Sergey Levine. Learning robust rewards with adverserial inverse reinforcement learning. In International Conference on Learning Representations, 2018. 
Adam Gleave, Michael Dennis, Cody Wild, Neel Kant, Sergey Levine, and Stuart Russell. Adver-sarial policies: Attacking deep reinforcement learning. In International Conference on Learning Representations, 2020. 
Morgan A Hanson. On sufficiency of the kuhn-tucker conditions. Journal of Mathematical Analysis and Applications, 80(2):545–550, 1981. 
Matthias Heger. Consideration of risk in reinforcement learning. In Machine Learning Proceedings 1994, pages 105–111. Elsevier, 1994. 
11
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Roger A Horn and Charles R Johnson. Matrix analysis. Cambridge university press, 2012. 
Sandy Huang, Nicolas Papernot, Ian Goodfellow, Yan Duan, and Pieter Abbeel. Adversarial attacks on neural network policies. arXiv preprint arXiv:1702.02284, 2017. 
H Isermann. Linear lexicographic optimization. Operations-Research-Spektrum, 4(4):223–228, 1982. 
Richard Klima, Daan Bloembergen, Michael Kaisers, and Karl Tuyls. Robust temporal difference learning for critical domains. In Proceedings of the 18th International Conference on Autonomous Agents and MultiAgent Systems, AAMAS ’19, page 350–358, Richland, SC, 2019. International Foundation for Autonomous Agents and Multiagent Systems. ISBN 9781450363099. 
Ezgi Korkmaz. Adversarial robust deep reinforcement learning requires redefining robustness. arXiv preprint arXiv:2301.07487, 2023. 
Jernej Kos and Dawn Song. Delving into adversarial attacks on deep policies. arXiv preprint arXiv:1705.06452, 2017. 
Yongyuan Liang, Yanchao Sun, Ruijie Zheng, and Furong Huang. Efficient adversarial training without attacking: Worst-case-aware robust reinforcement learning. Advances in Neural Infor-mation Processing Systems, 35:22547–22561, 2022. 
Yen-Chen Lin, Zhang-Wei Hong, Yuan-Hong Liao, Meng-Li Shih, Ming-Yu Liu, and Min Sun. Tactics of adversarial attack on deep reinforcement learning agents. In Proceedings of the 26th International Joint Conference on Artificial Intelligence, pages 3756–3762, 2017. 
Ajay Mandlekar, Yuke Zhu, Animesh Garg, Li Fei-Fei, and Silvio Savarese. Adversarially robust policy learning: Active construction of physically-plausible perturbations. In 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 3932–3939. IEEE, 2017. 
Janosch Moos, Kay Hansel, Hany Abdulsamad, Svenja Stark, Debora Clever, and Jan Peters. Robust reinforcement learning: A review of foundations and recent advances. Machine Learning and Knowledge Extraction, 4(1):276–315, 2022. 
Andrew Y Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory and application to reward shaping. In Proc. of the Sixteenth International Conference on Machine Learning, 1999, 1999. 
Xinlei Pan, Daniel Seita, Yang Gao, and John Canny. Risk averse robust adversarial reinforcement learning. In 2019 International Conference on Robotics and Automation (ICRA), pages 8522– 8528. IEEE, 2019. 
Santiago Paternain, Luiz F. O. Chamon, Miguel Calvo-Fullana, and Alejandro Ribeiro. Constrained reinforcement learning has zero duality gap. In Proceedings of the 33rd International Conference on Neural Information Processing Systems, pages 7553–7563, 2019. 
12
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
Anay Pattanaik, Zhenyi Tang, Shuijing Liu, Gautham Bommannan, and Girish Chowdhary. Robust deep reinforcement learning with adversarial attacks. In Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems, AAMAS ’18, page 2040–2042, Richland, SC, 2018. International Foundation for Autonomous Agents and Multiagent Systems. 
Matteo Pirotta, Marcello Restelli, Alessio Pecorino, and Daniele Calandriello. Safe policy iteration. In International Conference on Machine Learning, pages 307–315. PMLR, 2013. 
Antonin Raffin, Ashley Hill, Adam Gleave, Anssi Kanervisto, Maximilian Ernestus, and Noah Dormann. Stable-baselines3: Reliable reinforcement learning implementations. Journal of Machine Learning Research, 22(268):1–8, 2021. URL http://jmlr.org/papers/v22/ 20-1364.html. 
Mark J Rentmeesters, Wei K Tsai, and Kwei-Jay Lin. A theory of lexicographic multi-criteria optimization. In Proceedings of ICECCS’96: 2nd IEEE International Conference on Engineering of Complex Computer Systems (held jointly with 6th CSESAW and 4th IEEE RTAW), pages 76–79. IEEE, 1996. 
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017. 
Joar Skalse, Matthew Farrugia-Roberts, Stuart Russell, Alessandro Abate, and Adam Gleave. In-variance in policy optimisation and partial identifiability in reward learning. arXiv preprint arXiv:2203.07475, 2022a. 
Joar Skalse, Lewis Hammond, Charlie Griffin, and Alessandro Abate. Lexicographic multiobjective reinforcement learning. In Proceedings of the Thirty-First International Joint Con-ference on Artificial Intelligence, pages 3430–3436, jul 2022b. doi: 10.24963/ijcai.2022/476. 
Morton Slater. Lagrange multipliers revisited. Cowles Commission Discussion Paper No. 403, 1950. 
Matthijs TJ Spaan. Partially observable markov decision processes. In Reinforcement Learning, pages 387–414. Springer, 2012. 
Matthijs TJ Spaan and N Vlassis. A point-based pomdp algorithm for robot planning. In IEEE Inter-national Conference on Robotics and Automation, 2004. Proceedings. ICRA’04. 2004, volume 3, pages 2399–2404. IEEE, 2004. 
Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
Kai Liang Tan, Yasaman Esfandiari, Xian Yeow Lee, Soumik Sarkar, et al. Robustifying reinforcement learning agents via action space adversarial training. In 2020 American control conference (ACC), pages 3959–3964. IEEE, 2020. 
Chen Tessler, Yonathan Efroni, and Shie Mannor. Action robust reinforcement learning and applications in continuous control. In International Conference on Machine Learning, pages 6215–6224. PMLR, 2019. 
13
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Elise van der Pol, Thomas Kipf, Frans A. Oliehoek, and Max Welling. Plannable approximations to mdp homomorphisms: Equivariance under actions. In Proceedings of the 19th International Con-ference on Autonomous Agents and MultiAgent Systems, AAMAS ’20, page 1431–1439, Rich-land, SC, 2020. International Foundation for Autonomous Agents and Multiagent Systems. ISBN 9781450375184. 
Bart PG Van Parys, Daniel Kuhn, Paul J Goulart, and Manfred Morari. Distributionally robust control of constrained stochastic systems. IEEE Transactions on Automatic Control, 61(2):430– 442, 2015. 
Wolfram Wiesemann, Daniel Kuhn, and Melvyn Sim. Distributionally robust convex optimization. Operations Research, 62(6):1358–1376, 2014. 
Huan Xu and Shie Mannor. The robustness-performance tradeoff in markov decision processes. Advances in Neural Information Processing Systems, 19, 2006. 
Huan Zhang, Hongge Chen, Chaowei Xiao, Bo Li, Mingyan Liu, Duane Boning, and Cho-Jui Hsieh. Robust deep reinforcement learning against adversarial perturbations on state observations. Ad-vances in Neural Information Processing Systems, 33:21024–21037, 2020. 
Huan Zhang, Hongge Chen, Duane Boning, and Cho-Jui Hsieh. Robust reinforcement learning on state observations with learned optimal adversary. In International Conference on Learning Representation (ICLR), 2021. 
Shangtong Zhang. Modularized implementation of deep rl algorithms in pytorch. https:// github.com/ShangtongZhang/DeepRL, 2018. 
14
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
Appendix A. Examples and Further Considerations 
We provide here two examples to show how we can obtain limit scenarios Π0 = Π (any policy is maximally robust) or Π0 = ΠT (Example 1), and how for some MDPs the third inclusion in Theorem 4 is strict (Example 2). 
Example 1 Consider the simple MDP in Figure 2. First, consider the reward function R1(x1, ·, ·) = 10, R1(x2, ·, ·) = 0. This produces a “dummy” MDP where all policies have the same reward sum. Then, ∀T, π, V ⟨π,T ⟩ = V π, and therefore we have ΠD = Π0 = Π. 
x1 x2 
{ 1 2 , 
1 2} 
{ 1 2 , 
1 2} 
{ 1 2 , 
1 2} 
{ 1 2 , 
1 2} 
Figure 2: Example MDP. Values in brackets represent {P (·, u1, ·), P (·, u2, ·)}. 
Now, consider the reward function R2(x1, u1, ·) = 10, R2(·, ·, ·) = 0 elsewhere. Take a nonconstant policy π, i.e., π(x1) ̸= π(x2). In the example DOMDP (assuming the initial state is drawn uniformly from X0 = {x1, x2}) one can show that at any time in the trajectory, there is a stationary probability Pr{xt = x1} = 1 
2 . Let us abuse notation and write π(xi) = ( π(xi, u1) π(xi, u2) )⊤ 
and R(xi) = ( R(xi, u1, ·) R(xi, u2, ·) )⊤. For the given reward structure we have R(x2) = ( 0 0 )⊤, and therefore: 
J(π) = Ex0∼µ0 
[ ∞∑ t=0 
γtRt 
] = 
1 
2 ⟨R(x1), π(x1)⟩ 
γ 
1− γ . (9) 
Since the transitions of the MDP are independent of the actions, following the same principle as in (9): J⟨π, T ⟩ = 1 
2⟨R(x1), ⟨·, T ⟩(π)(x1)⟩ γ 1−γ . For any noise map ⟨·, T ⟩ ≠ Id, for the two-state 
policy it holds that π /∈ ΠT =⇒ ⟨π, T ⟩ ≠ π. Therefore ⟨π, T ⟩(x1) ̸= π(x1) and: 
J(π)− J(⟨π, T ⟩) = 5γ 
1− γ · ( π(x1, 1)− ⟨π, T ⟩(x1, 1) 
) ̸= 0, 
which implies that π /∈ Π0. 
Example 2 Consider the same MDP in Figure 2 with reward function R(x1, u1, ·) = R(x2, u1, ·) = 10, and a reward of zero for all other transitions. Take a policy π(x1) = (1 0), π(x2) = (0 1). The policy yields a reward of 10 in state x1 and a reward of 0 in state x2. Again we assume the initial state is drawn uniformly from X0 = {x1, x2}. Then, observe: 
J(π) =Ex0∼µ0 
[ ∞∑ t=0 
γtRt 
] = 
1 
2 ⟨R(x1), π(x1)⟩ 
γ 
1− γ = 
= 1 
2 
10γ 
1− γ = 
5γ 
1− γ . 
15
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Define now noise map T (· | x1) = (12 1 2) and T (· | x2) = (12 
1 2). Observe this noise map 
yields a policy with non-zero disadvantage, Dπ(x1, T ) = 5γ 1−γ − 
( 5γ 1−γ − 2.5 
) = 2.5 and similarly 
Dπ(x2, T ) = −2.5, therefore π /∈ ΠD. However, the policy is maximally robust: 
J(⟨π, T ⟩) = 1 
2 ⟨R(x1), ⟨π, T ⟩(x1)⟩ 
γ 
1− γ + 
+ 1 
2 ⟨R(x2), ⟨π, T ⟩(x2)⟩ 
γ 
1− γ = 
1 
2 
γ 
1− γ 
( 5 + 5 
) = 
5γ 
1− γ . 
(10) 
Therefore, π ∈ Π0. 
Appendix B. Theoretical Results 
B.1. Auxiliary Results 
Theorem 9 (Stochastic Approximation with Non-Expansive Operator) Let {ξt} be a random sequence with ξt ∈ Rn defined by the iteration: 
ξt+1 = ξt + αt(F (ξt)− ξt +Mt+1), 
where: 
1. The step sizes αt satisfy standard learning rate assumptions. 
2. F : Rn 7→ Rn is a ∥ · ∥∞ non-expansive map. That is, for any ξ1, ξ2 ∈ Rn, ∥F (ξ1) − F (ξ2)∥∞ ≤ ∥ξ1 − ξ2∥∞. 
3. {Mt} is a martingale difference sequence with respect to the increasing family of σ−fields Ft := σ(ξ0,M0, ξ1,M1, ..., ξt,Mt). 
Then, the sequence ξt → ξ∗ almost surely where ξ∗ is a fixed point such that F (ξ∗) = ξ∗. 
Proof See Borkar and Soumyanatha (1997). 
Theorem 10 (PB-LRL Convergence with 2 objectives.(Skalse et al., 2022b)) LetM be a multiobjective MDP with objectives Ki, i ∈ {1, 2}. Assume a policy π is twice differentiable in parameters θ, and if using a critic Vi assume it is continuously differentiable on parameters wi. Choose a tolerance ϵ, and suppose that if PB-LRL is run for T steps, there exists some limit point wi → w∗ 
i (θ) when θ is held fixed. If for both objectives there exists a gradient descent scheme such that limT→∞ Et[θt] ∈ Θϵ 
i then combining the objectives as in (1) yields limT→∞ Et[θt] ∈ {argmaxθ K2(θ), s.t. K1(θ) ≥ K1(θ 
′)− ϵ}. Proof [Proof Sketch] We refer the interested reader to Skalse et al. (2022b) for a full proof, and here attempt to provide the intuition behind the result in the form of a proof sketch. 
Let us begin by briefly recalling the general problem statement: we wish to take a multiobjective MDP M with m objectives, and obtain a lexicographically optimal policy (one that optimises the first objective, and then subject to this optimises the second objective, and so on). More precisely, for a policy π parameterised by θ, we say that π is (globally) lexicographically ϵ-optimal if θ ∈ Θϵ 
m, where Θϵ 0 = Θ is the set of all policies in M, Θϵ 
i+1 := {θ ∈ Θϵ i | 
maxθ′∈Θϵ i Ki(θ 
′)−Ki(θ) ≤ ϵi}, and Rm−1 ∋ ϵ ≽ 0.6 
6. The proof in Skalse et al. (2022b) also considers local lexicographic optima, though for the sake of simplicity, we do not do so here. 
16
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
The basic idea behind policy-based lexicographic reinforcement learning (PB-LRL) is to use a multi-timescale approach to first optimise θ using K1, then at a slower timescale optimise θ using K2 while adding the condition that the loss with respect to K1 remains bounded by its current value, and so on. This sequence of constrained optimisations problems can be solved using a Lagrangian relaxation (Bertsekas, 1999), either in series or – via a judicious choice of learning rates – simultaneously, by exploiting a separation in timescales (Borkar, 2008). In the simultaneous case, the parameters of the critic wi (if using an actor-critic algorithm, if not this part of the argument may be safely ignored) for each objective are updated on the fastest timescale, then the parameters θ, and finally (i.e., most slowly) the Lagrange multipliers for each of the remaining constraints. 
The proof proceeds via induction on the number of objectives, using a standard stochastic approximation argument (Borkar, 2008). In particular, due to the learning rates chosen, we may consider those more slowly updated parameters fixed for the purposes of analysing the convergence of the more quickly updated parameters. In the base case where m = 1, we have (by assumption) that limT→∞ Et[θ] ∈ Θϵ 
1. This is simply the standard (non-lexicographic) RL setting. Before continuing to the inductive step, Skalse et al. (2022b) observe that because gradient descent on K1 converges to globally optimal stationary point when m = 1 then K1 must be globally invex (where the opposite implication is also true) (Ben-Israel and Mond, 1986a).7 
The reason this observation is useful is that because each of the objectives Ki shares the same functional form, they are all invex, and furthermore, invexity is conserved under linear combinations and the addition of scalars, meaning that the Lagrangian formed in the relaxation of each constrained optimisation problem is also invex. As a result, if we assume that limT→∞ Et[θ] ∈ Θϵ 
i as our inductive hypothesis, then the stationary point of the Lagrangian for optimising objective Ki+1 is a global optimum, given the constraints that it does not worsen performance on K1, . . . ,Ki. Via Slater’s condition (Slater, 1950) and standard saddle-point arguments (Bertsekas, 1999; Paternain et al., 2019), we therefore have that limT→∞ Et[θ] ∈ Θϵ 
i+1, completing the inductive step, and thus the overall inductive argument. 
This concludes the proof that limT→∞ Et[θ] ∈ Θϵ m. We refer the reader to Skalse et al. (2022b) 
for a discussion of the error ϵ, but intuitively it corresponds to a combination of the representational power of θ, the critic parameters wi (if used), and the duality gap due to the Lagrangian relaxation (Paternain et al., 2019). In cases where the representational power of the various parameters is sufficiently high, then it can be shown that ϵ = 0. 
B.2. On Adversarial Disturbances and other Noise Kernels 
A problem that remains open after this work is what constitutes an appropriate choice of T̃ , and what can we expect by restricting a particular class of T̃ . We first discuss adversarial examples, and then general considerations on T̃ versus T . 
Adversarial Noise As mentioned in the introduction, much of the previous work focuses on adversarial disturbances. We did not directly address this in the results of this work since our motivation lies in the scenarios where the disturbance is not adversarial and is unknown. However, following the results of Section 3, we are able to reason about adversarial disturbances. Consider 
7. A differentiable function f : Rn → R is (globally) invex if and only if there exists a function g : Rn × Rn → Rn 
such that f(x1)− f(x2) ≥ g(x1, x2) ⊤∇f(x2) for all x1, x2 ∈ Rn (Hanson, 1981). 
17
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
an adversarial map Tadv to be 
⟨π, Tadv⟩(x) = π(y), y ∈ argmaxy∈Xad(x) d ( π(x), π(y) 
) , 
with Xad(x) ⊆ X being a set of admissible disturbance states for x, and d(·, ·) is a distance measure between distributions (e.g. 2-norm). 
Proposition 11 Constant policies are a fixed point of Tadv, and are the only fixed points if for all pairs x0, xk there exists a sequence {x0, ..., xk} ⊆ X such that xi ∈ Xad(xi). 
Proof First, it is straight-forward that if π ∈ Π =⇒ ⟨π, Tadv⟩(x) = π(x). To show they are the only fixed points, assume that there is a non-constant policy π′ that is a fixed point of Tad. Then, there exists x, z such that π′(x) ̸= π′(z). However, by assumption, we can construct a sequence {x, ..., z} ⊆ X that connects x and z and every state in the sequence is in the admissible set of the previous one. Assume without loss of generality that this sequence is {x, y, z}. Then, if π′ is a fixed point, ⟨π′, Tadv⟩(x) = π′(x), ⟨π′, Tadv⟩(y) = π′(y) and ⟨π′, Tadv⟩(z) = π′(z). However, π′(x) ̸= π′(z), so either π′(x) ̸= π′(y) =⇒ d(π′(x), π′(y)) ̸= 0 or π′(y) ̸= π′(z) =⇒ d(π′(y), π′(z)) ̸= 0, therefore π′ cannot be a fixed point of Tadv. 
The main difference between an adversarial operator and the random noise considered throughout this work is that Tadv is not a linear operator, and additionally, it is time varying (since the policy is being modified at every time step of the PG algorithm). Therefore, including it as a LRPG objective would invalidate the assumptions required for LRPG to retain formal guarantees of the original PG algorithm used, and it is not guaranteed that the resulting policy gradient algorithm would converge. 
Appendix C. Experiment Methodology 
We use in the experiments well-tested implementations of A2C, PPO and SAC from Stable Base-lines 3 (Raffin et al., 2021) to include the computation of the lexicographic parameters in (1). All experiments were run on an Ubuntu 18.04 system, with a 16 core CPU and a graphic card Nvidia GeForce 3060. 
LRPG Parameters. The LRL parameters are initialised in all cases as β1 0 = 2, β2 
0 = 1, λ = 0 and η = 0.001. The LRL tolerance is set to ϵt = 0.99k̂1 to ensure we never deviate too much from the original objective, since the environments have very sparse rewards. We use a first order approximation to compute the LRL weights from the original LMORL implementation. 
C.1. Discrete Control 
The discrete control environments used can be seen in Figure 3. Since all the environments use a pixel representation of the observation, we use a shared representation for the value function and policy, where the first component is a convolutional network, implemented as in Zhang (2018). The hyper-parameters of the neural representations are presented in Table 2. 
18
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
Figure 3: Screenshots of the environments used, from left: LavaGap, LavaCrossing and Dynami-cObstables. 
Layer Output Func. 
Conv1 16 ReLu Conv2 32 ReLu Conv3 64 ReLu 
Table 2: Shared Observation Layers 
The actor and critic layers, for both algorithms, are a fully connected layer with 64 features as input and the corresponding output. We used in all cases an Adam optimiser. We optimised the parameters for each (vanilla) algorithm through a quick parameter search, and apply the same parameters for the Lexicographically Robust versions. 
LavaGap LavaCrossing DynObs Parallel Envs 16 16 16 Steps 2 · 106 2 · 106 8× 106 
γ 0.99 0.99 0.98 α 0.00176 0.00176 0.00181 ϵ(Adam) 10−8 10−8 10−8 
Grad. Clip 0.9 0.9 0.5 Gae 0.95 0.95 0.95 Rollout 64 64 64 E. Coeff 0.01 0.014 0.011 V. Coeff 0.05 0.05 0.88 
Table 3: A2C Parameters 
19
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
LavaGap LavaCrossing DynObs Parallel Envs 8 8 8 Steps 6 · 106 2 · 106 8× 105 
γ 0.95 0.99 0.97 α 0.001 0.001 0.001 ϵ(Adam) 10−8 10−8 10−8 
Grad. Clip 1 1 0.1 Ratio Clip 0.2 0.2 0.2 Gae 0.95 0.95 0.95 Rollout 256 512 256 Epochs 10 10 10 E. Coeff 0 0.1 0.01 
Table 4: PPO Parameters 
For the implementation of the LRPG versions of the algorithms, in all cases we allow the algorithm to iterate for 1/3 of the total steps before starting to compute the robustness objectives. In other words, we use K̂(θ) = K1(θ) until t = 1 
3 max steps, and from this point we resume the lexicographic robustness computation as described in Algorithm 1. This is due to the structure of the environments simulated. The rewards (and in particular the positive rewards) are very sparse in the environments considered. Therefore, when computing the policy gradient steps, the loss for the primary objective is practically zero until the environment is successfully solved at least once. If we implement the combined lexicographic loss from the first time step, many times the algorithm would converge to a (constant) policy without exploring for enough steps, leading to convergence towards a maximally robust policy that does not solve the environment. 
Noise Kernels. We consider two types of noise; a normal distributed noise T̃ g and a uniform distributed noise T̃ u. For the environments LavaGap and DynamicObstacles, the kernel T̃ u produces a disturbed state x̃ = x+ ξ where ∥ξ∥∞ ≤ 2, and for LavaCrossing ∥ξ∥∞ ≤ 1.5. The normal distributed noise is in all cases N (0, 0.5). The maximum norm of the noise is quite large, but this is due to the structure of the observations in these environments. The pixel values are encoded as integers 0 − 9, where each integer represents a different feature in the environment (empty space, doors, lava, obstacle, goal...). Therefore, any noise ∥ξ∥∞ ≤ 0.5 would most likely not be enough to confuse the agent. On the other hand, too large noise signals are unrealistic and produce pathological environments. All the policies are then tested against two “true” noise kernels, T1 = T̃ u and T2 = T̃ g. The main reason for this is to test both the scenarios where we assume a wrong noise kernel, and the case where we are training the agents with the correct kernel. 
Comparison with SA-PPO. One of the baselines included is the State-Adversarial PPO algorithm proposed in Zhang et al. (2020). The implementation includes an extra parameter that multiplies the regularisation objective, kppo. Since we were not able to find indications on the best parameter for discrete action environments, we implemented kppo ∈ {0.1, 1, 2} and picked the best result for each entry in Table 1. Larger values seemed to de-stabilise the learning in some cases. The rest of the parameters are kept as in the vanilla PPO implementation. 
20
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
PPO on MiniGrid Environments A2C on MiniGrid Environments 
Noise Vanilla LRPPO(Ku T ) LRPPO(K 
g T ) SA-PPO Vanilla LRA2C(K 
u T ) LRA2C(K 
g T ) LRA2C(KD) 
LavaGap ∅ 0.95±0.003 0.95±0.075 0.95±0.101 0.94±0.068 0.94±0.004 0.94±0.005 0.94±0.003 0.94±0.006 T1 0.80±0.041 0.95±0.078 0.93±0.124 0.88±0.064 0.83±0.061 0.93±0.019 0.89±0.032 0.91±0.088 T2 0.92±0.015 0.95±0.052 0.95±0.094 0.93±0.050 0.89±0.029 0.94±0.008 0.93±0.011 0.93±0.021 T0.5 adv 0.56±0.194 0.93±0.101 0.91±0.076 0.90±0.123 0.92±0.034 0.94±0.003 0.94±0.007 0.93±0.015 
T1 adv 0.20±0.243 0.90±0.124 0.68±0.190 0.90±0.135 0.75±0.123 0.94±0.006 0.92±0.038 0.88±0.084 
T2 adv 0.01±0.051 0.71±0.251 0.21±0.357 0.87±0.116 0.27±0.119 0.79±0.069 0.68±0.127 0.56±0.249 
LavaCrossing ∅ 0.95±0.023 0.93±0.050 0.93±0.018 0.88±0.091 0.91±0.024 0.91±0.063 0.90±0.017 0.92±0.034 T1 0.50±0.110 0.92±0.053 0.89±0.029 0.64±0.109 0.66±0.071 0.78±0.111 0.72±0.073 0.76±0.098 T2 0.84±0.061 0.92±0.050 0.92±0.021 0.85±0.094 0.78±0.054 0.83±0.105 0.86±0.029 0.87±0.063 T0.5 adv 0.29±0.098 0.91±0.081 0.91±0.054 0.87±0.045 0.56±0.039 0.51±0.089 0.43±0.041 0.68±0.126 
T1 adv 0.03±0.022 0.83±0.122 0.86±0.132 0.87±0.059 0.27±0.158 0.25±0.118 0.17±0.067 0.43±0.060 
T2 adv 0.0±0.004 0.50±0.171 0.38±0.020 0.82±0.072 0.06±0.056 0.04±0.030 0.01±0.008 0.09±0.060 
DynamicObstacles ∅ 0.91±0.002 0.91±0.008 0.91±0.007 0.91±0.131 0.91±0.011 0.88±0.020 0.89±0.009 0.91±0.013 T1 0.23±0.201 0.77±0.102 0.61±0.119 0.45±0.188 0.27±0.104 0.43±0.108 0.45±0.162 0.56±0.270 T2 0.50±0.117 0.75±0.075 0.70±0.072 0.68±0.490 0.45±0.086 0.53±0.109 0.52±0.161 0.67±0.203 T0.5 adv 0.74±0.230 0.89±0.118 0.85±0.061 0.90±0.142 0.46±0.214 0.55±0.197 0.51±0.371 0.62±0.249 
T1 adv 0.26±0.269 0.79±0.157 0.68±0.144 0.84±0.150 0.19±0.284 0.35±0.197 0.23±0.370 0.10±0.379 
T2 adv -0.49±0.312 0.51±0.234 0.33±0.202 0.55±0.170 -0.54±0.209 -0.21±0.192 -0.53±0.261 -0.51±0.260 
Table 5: Extended Reward Results. 
C.1.1. EXTENDED RESULTS: ADVERSARIAL DISTURBANCES 
Even though we do not use an adversarial attacker or disturbance in our reasoning through this work, we implemented a policy-based state-adversarial noise disturbance to test the benchmark algorithms against, and evaluate how well each of the methods reacts to such adversarial disturbances. 
Adversarial Disturbance We implement a bounded policy-based adversarial attack, where at each state x we maximise for the KL divergence between the disturbed and undisturbed state, such that the adversarial operator is: 
T ε adv(y | x) = 1 =⇒ y ∈ argmax 
x̃ DKL(π(x), π(x̃)) 
s.t. ∥x− x̃∥2 ≤ ε. 
The optimisation problem is solved at every point by using a Stochastic Gradient Langevin Dynam-ics (SGLD) optimiser. The results are presented in Table 5. 
This type of adversarial attack with SGLD optimiser was proposed in Zhang et al. (2020). As one can see, the adversarial disturbance is quite successful at severely lowering the obtained rewards in all scenarios. Additionally, as expected SA-PPO was the most effective at minimizing the disturbance effect (as it is trained with adversarial disturbances), although LRPG produces reasonably robust policies against this type of disturbances as well. At last, A2C appears to be much more sensitive to adversarial disturbances than PPO, indicating that the policies produced by PPO are by default more robust than A2C. 
C.2. Continuous Control 
The continuous control environments simulated are MountainCar, LunarLander and BipedalWalker. The policies used are in all cases MLP policies with ReLU gates and a (64, 64) feature extractor plus a fully connected layer to output the values and actions unless stated otherwise. The hyperparameters can be found in tables C.2 and 8. The implementation is based on Stable Baselines 3 
21
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Figure 4: Learning Plots for Discrete Control Environments. 
22
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
PPO on Continuous Environments SAC on Continuous Environments 
Noise Vanilla LRPPO (Ku T ) LRPPO (K 
g T ) SA-PPO Vanilla LRSAC (Ku 
T ) LRSAC (K g T ) 
MountainCar ∅ 94.77±0.26 93.17±0.89 94.66±1.61 88.69±3.93 93.52±0.05 94.43±0.19 93.84±0.05 T1 88.67±1.41 91.46±1.22 94.91±1.35 88.41±3.99 1.89±65.31 71.81±13.04 76.90±7.11 T2 92.22±1.11 92.40±1.28 94.76±1.42 89.32±3.79 -27.82±73.10 72.93±8.57 69.41±13.03 
LunarLander ∅ 267.99±38.04 269.76±22.93 243.08±37.03 220.18±98.78 268.96±51.52 275.17±14.04 282.24±15.95 T1 156.09±22.87 280.91±20.34 182.80±49.26 164.53 ±45.48 128.18±17.73 187.64±76.30 153.81±33.16 T2 158.02±46.57 276.76±16.20 212.62±37.56 221.84±73.61 140.92±20.61 187.82±25.27 158.18±28.60 
BipedalWalker ∅ 265.39±82.36 261.39±83.19 276.66±44.85 251.60±103.08 236.39 ±157.03 302.56±70.79 313.56±52.17 T1 174.15±170.30 253.56±72.66 220.28±118.61 264.69±61.63 203.93 ±167.83 241.45±124.54 241.60±139.93 T2 135.16±182.30 243.27±89.86 265.37±80.60 255.21±90.61 84.10 ±198.12 198.20±151.64 229.75±166.87 
Table 6: Reward values gained by LRPG and baselines on continuous control tasks. 
MountainCarContinuous LunarLanderContinuous BipedalWalker-v3 Parallel Envs 1 16 32 Steps 2× 104 1× 106 5× 106 
γ 0.9999 0.999 0.999 α 3× 10−4 3× 10−4 3× 10−4 
Grad. Clip 5 0.5 0.5 Ratio Clip 0.2 0.2 0.18 Gae 0.9 0.98 0.95 Epochs 10 4 10 E. Coeff 0.00429 0.01 0 
Table 7: PPO Parameters for Continuous Control 
(Raffin et al., 2021) tuned algorithms. Noise Kernels. We consider again two types of noise; a normal distributed noise T̃ g and a uniform distributed noise T̃ u. In all cases, algorithms are implemented with a state observation normalizer. That is, assimptotically all states will be observed to be in the set (−1, 1). For this reason, the uniform noise is bounded at lower values than for the discrete control environments. For BipedalWalker ∥ξ∥∞ ≤ 0.05 and for Lunarlander and MountainCar ∥ξ∥∞ ≤ 0.1. Larger values were shown to destabilize learning. 
MountainCarContinuous LunarLanderContinuous BipedalWalker-v3 Steps 5× 104 5× 105 5× 105 
γ 0.9999 0.99 0.98 α 3× 10−4 7.3× 10−4 7.3× 10−4 
τ 0.01 0.01 0.01 Train Freq. 32 1 64 Grad. Steps 32 1 64 MLP Arch (64,64) (400,300) (400,300) 
Table 8: SAC Parameters for Continuous Control 
23
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
Figure 5: Learning Plots for Continuous Control Environments. 
24
BOUNDED ROBUSTNESS IN REINFORCEMENT LEARNING 
Learning processes In general, learning was not severlely affected by the LRPG scheme. How-ever, it was shown to induce a larger variance in the trajectories observed, as seen in LunarLander with LR-SAC and BipedalWalker with LR-SAC. 
25
JARNE ORNIA ROMAO HAMMOND MAZO JR. ABATE 
26