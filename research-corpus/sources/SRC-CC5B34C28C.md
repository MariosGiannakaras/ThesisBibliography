> Source: https://ojs.aaai.org/index.php/AAAI/article/view/40929/44890

Best-Effort Policies for Robust Markov Decision Processes 
Alessandro Abate, Thom Badings, Giuseppe De Giacomo, Francesco Fabiano Department of Computer Science, University of Oxford, Oxford, United Kingdom 
{alessandro.abate, thom.badings, giuseppe.degiacomo, francesco.fabiano}@cs.ox.ac.uk 
Abstract 
We study the common generalization of Markov decision processes (MDPs) with sets of transition probabilities, known as robust MDPs (RMDPs). A standard goal in RMDPs is to compute a policy that maximizes the expected return under an adversarial choice of the transition probabilities. If the uncertainty in the probabilities is independent between the states, known as s-rectangularity, such optimal robust policies can be computed efficiently using robust value iteration. However, there might still be multiple optimal robust policies, which, while equivalent with respect to the worst-case, reflect different expected returns under non-adversarial choices of the transition probabilities. Hence, we propose a refined policy selection criterion for RMDPs, drawing inspiration from the notions of dominance and best-effort in game theory. Instead of seeking a policy that only maximizes the worst-case expected return, we additionally require the policy to achieve a maximal expected return under different (i.e., not fully adversarial) transition probabilities. We call such a policy an optimal robust best-effort (ORBE) policy. We prove that ORBE policies always exist, characterize their structure, and present an algorithm to compute them with a manageable overhead compared to standard robust value iteration. ORBE policies offer a principled tie-breaker among optimal robust policies. Numerical experiments show the feasibility of our approach. 
Code — https://github.com/tbadings/best-effort-rmdps Extended version — https://arxiv.org/abs/2508.07790 
1 Introduction Markov decision processes (MDPs) are the standard model for sequential decision making in stochastic environments and are ubiquitous in artificial intelligence (AI) (Russell and Norvig 2010), operations research (Davis 2018), control theory (Åström 2012), and robotics (Hanheide et al. 2017). Within AI, MDPs are at the core of many model-based reinforcement learning methods (Moerland et al. 2023). Solving an MDP amounts to computing a policy (or strategy) for the agent, i.e., a mapping from states to actions, that maximizes a particular performance value, such as the expected (discounted) cumulative reward (Puterman 1994). 
Copyright © 2026, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 
Robust MDPs. A fundamental limitation of MDPs is the requirement to specify transition probabilities precisely. In practice, accurately determining these probabilities can be challenging, especially if parameters are uncertain or if the model is learned from data (Badings et al. 2023b). Moreover, optimal policies may be sensitive to small changes in the transition probabilities (Mannor et al. 2004). To address this issue, robust MDPs (RMDPs) generalize MDPs by allowing for sets of transition probabilities (Iyengar 2005; Nilim and Ghaoui 2005; Wiesemann, Kuhn, and Rustem 2013). That is, instead of assigning precise probabilities between 0 and 1, the transitions in an RMDP are described by a set of feasible probabilities, called the uncertainty set of the RMDP. 
The standard objective in an RMDP is to compute an optimal robust policy, defined as a policy that maximizes the expected return under the minimizing (i.e., worst-case) transition probabilities in the uncertainty set. Unfortunately, computing optimal robust policies under general uncertainty sets is NP-hard (Wiesemann, Kuhn, and Rustem 2013). To ensure tractability, uncertainty sets are commonly assumed to be convex as well as independent between the states and/or actions of the RMDP, referred to as rectangularity of the uncertainty set. Under these assumptions, optimal robust policies can be computed, e.g., using robust value iteration. 
The adversarial nature of RMDPs. When computing an optimal robust policy, the choice of transition probabilities is inherently adversarial. However, in many scenarios, the choice of transition probabilities is not actively working against the agent, making this assumption overly conservative. Take, for example, an autonomous drone flying through uncertain wind conditions. Clearly, the wind conditions do not depend on the drone’s control policy, so reasoning solely about the worst-case conditions might be too conservative. Moreover, multiple optimal robust policies may exist, even though their performance under non-adversarial conditions may differ. We thus raise the vital question: can we compute a policy that is optimal in the worst case, but also “is best” when the environment does not act fully adversarially? 
Best-effort policies. To address the limitations of purely adversarial reasoning in RMDPs, we draw inspiration from advances in reactive stochastic games (Aminof et al. 2023; Giacomo, Favorito, and Silo 2024). In this framework, a policy is deemed winning, dominant, or best-effort if it succeeds 
The Fortieth AAAI Conference on Artificial Intelligence (AAAI-26) 
36120
against all, the maximum subset, or a maximal subset of the environment policies, respectively. Yet, these papers consider games where only the graph of the model is known and the probabilities are unconstrained, as opposed to RMDPs, where the uncertainty is captured by bounded sets of distributions. 
In this paper, we leverage the concepts of dominance and best-effort to define a refined policy selection criterion for RMDPs, which we term optimal robust best-effort (ORBE). An ORBE policy satisfies two properties: (1) it achieves an optimal expected return under the worst-case transition probabilities; and (2) it is not dominated by any other policy, i.e., is best-effort. Here, one policy is said to dominate another if it performs at least as well across the entire uncertainty set and strictly better in at least one instance of the transition probabilities from the uncertainty set. This best-effort perspective offers a principled tie-breaker among optimal robust policies, favoring those achieving a maximal expected return under non-adversarial transition probabilities. Thus, ORBE policies preserve robust optimality—unlike approaches that update the uncertainty set—while also improving performance in non–fully adversarial environments. 
Contributions. We introduce the class of optimal robust best-effort (ORBE) policies for RMDPs. These policies combine the worst-case guarantees of standard robust policies with the refinement offered by best-effort reasoning, ensuring strong performance even when the environment is not fully adversarial. Specifically, our key contributions are as follows: 
 We formalize the notions of dominant and best-effort 
policies within the context of RMDPs (Sect. 3). 
 We present a full characterization of ORBE policies and 
an efficient algorithm to compute them with small overhead to standard robust value iteration (Sects. 4 and 5). 
 We empirically demonstrate the feasibility of our techniques as a tie-breaker in robust value iteration (Sect. 6). 
We postpone a detailed discussion of related work to Sect. 7. 
2 Preliminaries We write ⟨u, v⟩ := 
∑ x∈X u(x)v(x) for the dot product be-
tween the functions u, v : X → R. The cardinality of a set X is written as |X|. A probability distribution over a set X is a function µ : X → [0, 1] such that 
∑ x∈X µ(x) = 1. The 
set of all probability distributions over X is denoted by ∆X . 
2.1 Markov Decision Processes We consider Markov decision processes (MDPs) with discounted rewards, defined as follows (Puterman 1994). Definition 1 (MDP). An MDP is a tuple (S, sI , A, P,R, γ), where S is a finite set of states, sI ∈ ∆S is the initial distribution, A is a finite set of actions, P : S × A → ∆S is a transition function, R : S × A → R≥0 is a state-action reward function, and γ ∈ (0, 1) is a discount factor. 
The actions in an MDP are chosen by a (randomized) policy π : S → ∆A. We write Π for the set of all policies and simplify π(s)(a) as π(s, a). The objective in an MDP is to compute a policy π that maximizes the expected return ρπP : 
ρπP := ∑ 
s∈S sI(s)V 
π P (s) = ⟨sI , V π 
P ⟩, (1) 
where the value function V π P : S → R is defined as 
V π P (s) := E 
[∑∞ 
t=0 γtRπ(st) 
∣∣∣ s0 = s, st+1 ∼ Pπ(st) ] , 
with the transition and rewards functions for π given as 
Pπ(s) := ∑ 
a∈A π(s, a)P (s, a) ∈ ∆S , (2) 
Rπ(s) := ∑ 
a∈A π(s, a)R(s, a) ∈ R≥0. (3) 
This value function is the fixed point of the Bellman operator T π P (Puterman 1994), which is defined for all states s ∈ S as 
(T π P V )(s) := [Rπ(s) + ⟨γP π(s), V ⟩] , 
whereas the optimal value V ⋆ P := maxπ∈Π V π 
P is the fixed point of the optimal Bellman operator T ⋆ 
P defined as (T ⋆ 
P V )(s) := max π∈Π T π P V (s). 
Thus, the sequences V π n+1 := T π 
P V π n and V ⋆ 
n+1 := T ⋆ P V ⋆ 
n converge to their respective fixed points, i.e., limn→∞ V π 
n = V π P and limn→∞ V ⋆ 
n = V ⋆ P . Subsequently, an optimal policy 
can be computed as π⋆ P ∈ argmaxπ∈Π T π 
P V ⋆ P . 
2.2 Robust Markov Decision Processes Robust MDPs (RMDPs) extend MDPs with sets of transition probabilities (Iyengar 2005; Nilim and Ghaoui 2005). In an RMDP, the transition function is chosen from a set P ⊆ {P : S ×A→ ∆S} of transition functions, called the uncertainty set (also known as the ambiguity set). Definition 2 (RMDP). A robust MDP (RMDP) is a tuple (S, sI , A,P, R, γ), where S, sI , A, R, and γ are defined as in an MDP, and where P ⊆ {P : S × A→ ∆S} is a set of transition functions, called the uncertainty set. 
The robust expected return ρπP for the policy π is defined as the worst-case expected return over the uncertainty set P: 
ρπP := min P∈P 
ρπP . (4) 
The standard objective in an RMDP is to find an optimal robust policy π⋆ 
P maximizing the robust expected return ρ⋆P : π⋆ P ∈ argmax 
π∈Π ρπP , ρ⋆P := max 
π∈Π ρπP . (5) 
Unfortunately, solving Eqs. (4) and (5) is NP-hard for general uncertainty sets P , even if they are convex (Wiesemann, Kuhn, and Rustem 2013). Thus, P is commonly assumed to be decomposable over states and/or state-action pairs, which is also known as rectangularity of the uncertainty set. Definition 3 (Rectangularity). The uncertainty set P is s-rectangular if it can be decomposed state-wise as P = ×s∈S Ps, where Ps ⊆ {P : Act → ∆S}. Moreover, P is (s, a)-rectangular if it can be decomposed state-action-wise as P =×s∈S,a∈A Ps,a, where Ps,a ⊆ ∆S . 
(s, a)-rectangularity is a special case of s-rectangularity. Assumption 1. Throughout the paper, the uncertainty set P of an RMDP is assumed to be s-rectangular. 
Under s-rectangularity, optimal policies may need to be randomized (Wiesemann, Kuhn, and Rustem 2013, Prop. 1). Our definitions follow the usual semantics that the environment knows the stochastic policy of the agent but not the actual actions sampled from this policy, known as the environment first (or nature first) semantics (Suilen et al. 2024). 
36121
Robust value iteration. Under s-rectangularity, for every policy π, there is a robust value function V π 
P : S → R that satisfies V π 
P (s) := minP∈P V π P (s) for all s ∈ S (Wiesemann, 
Kuhn, and Rustem 2013). This value function V π P is the fixed 
point of the robust Bellman operator T π P for every s ∈ S: 
(T π P V )(s) := min 
P∈PS 
[Rπ(s) + ⟨γP π(s), V ⟩] . 
Similarly, there exists an optimal robust value function V ⋆ P := 
maxπ∈Π V π P , which is the fixed point of the optimal robust 
Bellman operator T ⋆ P , defined for all s ∈ S as 
(T ⋆ PV )(s) := max 
π∈Π T π P V (s). 
Robust value iteration leverages these fixed points so that the sequences V π 
n+1 := T π P V π 
n and V ⋆ n+1 := T ⋆ 
PV ⋆ n converge 
to their respective fixed points, i.e., limn→∞ V π n = V π 
P and limn→∞ V ⋆ 
n = V ⋆ P . Subsequently, an optimal robust policy 
can be computed as π⋆ P ∈ argmaxπ T π 
P V ⋆ P . 
3 Best-Effort Policies in RMDPs The optimal robust policy in Eq. (5) assumes the choice of transition function from the uncertainty set to be fully adversarial. Here, we introduce dominance and best-effort as the basis for a policy selection criterion that also considers non-adversarial scenarios. These notions have been used in uncertain stochastic games (Aminof et al. 2023), but, as we discuss in Sect. 7, these results do not carry over to RMDPs. 
3.1 Dominant and Best-Effort Policies In this section, we tailor the definitions of dominant and besteffort policies from Aminof et al. (2023) to RMDPs. The first concept is that of dominance between policies. Definition 4 (Dominance). Let π, π′ ∈ Π be policies for the RMDPMR. The policy π dominates π′, written π ≥P π′, if and only if ρπP ≥ ρπ 
′ 
P for all P ∈ P . Intuitively, π dominates π′ if π does not perform worse 
than π′ under any transition function P ∈ P . If, in addition, the policy π also attains a strictly higher expected return in some P ∈ P , then π strictly dominates π′: Definition 5 (Strict dominance). Let π, π′ ∈ Π be policies for RMDPMR. Policy π dominates π′, written π >P π′, if and only if π ≥P π′ and there exists P ′ ∈ P s.t. ρπP ′ > ρπ 
′ 
P ′ . We say that the policy π is (strictly) dominant in the RMDP MR if it (strictly) dominates every other policy π′ ∈ Π\{π}. Next, we say that a policy is best-effort if there is no other policy that dominates it. Definition 6 (Best-effort). A policy π ∈ Π for the RMDP MR is best-effort if there is no π′ ∈ Π such that π′ >P π. We denote by ΠBE ⊆ Π the set of all best-effort policies. 
A policy is best-effort if there is no other policy that is strictly better for some P ∈ P and not worse for all P ∈ P . In other words, a best-effort policy cannot be improved without also decreasing the expected return under some transition function. Best-effort policies are incomparable with respect to the dominance order, i.e., for all π, π′ ∈ ΠBE, π ̸= π′, we have both π ̸≥P π′ and π ̸≤P π′. 
s1 s2 sI 
a1 ξ 
1− ξ 
a2 2ξ 
1− 2ξ a 
0.5 0.5 
0 0.5 
1 0 0.2 
0.40 
3 
6 
β ξ 
ρβξ 
Figure 1: Left: An RMDP with two states, where the policy is fully defined by the probability β := π(s1, a1) of choosing a1 in s1. The reward function is defined as R(s1, a1) = R(s1, a2) = 0 and R(s2, a) = 1. Right: The expected return ρβξ as a function of β and ξ ∈ [0, 0.5]. All policies are optimal robust, but only the policy with β = 0 is best-effort. 
3.2 Optimal Robust Does Not Imply Best-Effort In general, optimal robust policies for RMDPs are not besteffort, as shown by the two-state RMDP in Fig. 1 with reward function R(s1, a1) = R(s1, a2) = 0, R(s2, a) = 1. In this RMDP, the only action choice is between a1 and a2 in state s1, so the stochastic policy π is completely defined by the probability β := π(s1, a1) ∈ [0, 1] of choosing a1 in s1. Similarly, the (s-rectangular) uncertainty set P is fully defined by the parameter ξ ∈ Ξ = [0, 0.5]. As a result, we may simplify the notations from the preceding definitions by replacing π with β, P with ξ, and P with Ξ. The value function V β ξ : {s1, s2} → R depends on β and ξ and is defined as 
V β ξ (s1) = γ 
( β [ ξV β 
ξ (s2) + (1− ξ)V β ξ (s1) 
] + (1− β) 
[ 2ξV β 
ξ (s2) + (1− 2ξ)V β ξ (s1) 
]) , 
V β ξ (s2) = 1 + γ 
[ 0.5V β 
ξ (s1) + 0.5V β ξ (s2) 
] . 
Solving for the value ρβξ = V β ξ (s1) with γ = 0.9 yields the 
surface in the right half of Fig. 1. This surface shows the expected return ρβξ for all β ∈ [0, 1] and ξ ∈ [0, 0.5]. The worst-case expected return is zero and is attained at ξ = 0, regardless of the value of β. Thus, all policies in this RMDP are optimal robust. Nevertheless, only the policy for β = 0 is best-effort, because for all ξ > 0, the expected return for β = 0 is strictly higher than for any β > 0. In other words, the policy defined as π(s1, a1) = 0, π(s1, a2) = 1 strictly dominates all other policies π′ ̸= π, that is, π >Ξ π′. 
3.3 Problem Statement Above, we have shown that not all optimal robust policies are also best-effort. This observation motivates the next core problem, which we shall solve in the remainder of this paper. Problem 1. For a given RMDPMR, compute a policy π⋆ 
BE that is optimal robust and best-effort, i.e., π⋆ BE ∈ argmax 
π∈Π ρπP such that ∄π′ ∈ Π\{π⋆ 
BE}, π′ >P π⋆ BE. 
We call a policy that satisfies Problem 1 optimal robust best-effort (ORBE). In RMDPs with multiple optimal robust policies (as in Fig. 1), the best-effort criterion offers a principled tiebreaker, favoring a policy that attains a maximal performance under non-adversarial transition probabilities. 
36122
Remark 1. For clarity and due to space constraints, all proofs are provided in the appendix of the extended version of this paper (Abate et al. 2025, Appendix A). 
4 Representation of Robust Value Functions We first introduce a change in perspective to the value function, which we will use in Sect. 5 to solve Problem 1. Instead of using shared variables to represent dependencies between probabilities (such as ξ in Fig. 1), we label each transition with its own probability p(s, a)(s′) and encode dependencies in the uncertainty set P . For instance, we can equally represent the RMDP in Fig. 1 using the uncertainty set 
Ps1 = {(Ps1 : A→ ∆S) : p(a1)(s1) + p(a1)(s2) = 1, 
p(a2)(s1) + p(a2)(s2) = 1, p(a1)(s2) = 0.5p(a2)(s2)}. 
We aim to reason about the expected return when the transition function is fixed in all but one state. To this end, we introduce the notion of a partial transition function. Definition 7 (Partial transition function). Let P be an s-rectangular uncertainty set and let s̄ ∈ S be a state. A partial transition function P−s̄ for state s̄ is defined as P−s̄ =×s∈S\{s̄} Ps, where Ps ∈ P for all s ∈ S \ {s̄}. 
A partial transition function has the form P−s̄ : (S\{s̄})× Act → ∆S . Thus, to complete P−s̄ with Ps̄ ∈ Ps̄ for the missing state s̄, we take the product P−s̄ × Ps̄. Similarly, we write P−s̄ × Ps̄ for the set of all completions, such that P−s̄ × Ps̄ ∈ P−s̄ × Ps̄. Using this notation, we define the following value function in a fixed state s̄, when the transition probabilities are fixed in all states but s̄. Definition 8 (Parametric value function). The value in state s̄ is a function of the completion Ps̄ ∈ Ps̄ of the partial transition function P−s̄ and is defined as Zπ 
P,s̄(Ps̄) = V π P−s̄×Ps̄ 
(s̄). 
Example 1. Consider again the RMDP from Fig. 1 with the policies given by β = 0 and β = 1. The value functions Zπ 
P,s1 for these two policies are, respectively, shown in the left and right halves of Fig. 2. For β = 1, the value depends only of the transition probabilities related to action a1 (and for β = 0 only of those related to a2). In both plots, the dashed line in the bottom plane shows the set of valid distributions in Ps1 , where the marked points coincide with those on the ξ-axis in Fig. 1. The green (left) and purple (right) curved lines show the expected return for the policies with β = 1 and β = 0, respectively, as a function of ξ and coincide with the lines of the same color in Fig. 1. As in Fig. 1, we observe that, for any ξ > 0, the policy for β = 1 strictly dominates all other policies and is, thus, best-effort. 
5 Finding Optimal Robust Best-Effort Policies We now use the representation of the value function from Def. 8 to determine whether an optimal robust policy for a fixed RMDPMR = (S, sI , A,P, R, γ) is best-effort. 
5.1 Existence of ORBE Policies We first establish in Theorem 1 that, for any s-rectangular RMDP, the set of ORBE policies is nonempty. Intuitively, this result holds because the dominance relation imposes a 
0 0.5 
1 
0 0.5 
1 0 
3 
6 ξ = 0.5 
P (s1, a1 )(s1) 
P (s1 , a 1 )(s2 ) 
Zπ P,s1 
0 0.5 
1 
0 0.5 
1 0 
3 
6 ξ = 0.5 
P (s1, a2 )(s1) 
P (s1 , a 2 )(s2 ) 
Zπ′ 
P,s1 
Figure 2: The value function Zπ P,s1 
in state s1 for the RMDP from Fig. 1, shown for the policies with β = 1 (left) and β = 0 (right). The curved lines show the expected return as the parameter ξ in Fig. 1 ranges from 0 to 0.5 (the line markers correspond with those on the ξ-axis in Fig. 1). 
partial order over policies, ensuring the existence of maximal (i.e., best-effort) ones that under an adversarial environment must also be optimal robust. Furthermore, any optimal robust policy π ∈ Π⋆ cannot be dominated by a policy that is not optimal robust. Thus, an ORBE policy always exists. Theorem 1 (Existence of ORBE policies). For any RMDP, the intersection of the sets of optimal robust policies Π⋆ and best-effort policies ΠBE is nonempty. 
Note that the existence of best-effort policies in RMDPs does not directly follow from the results for synthesis in stochastic environments in Aminof et al. (2023); see Sect. 7. 
5.2 Characterizing ORBE policies In Theorem 2, we provide a sufficient condition for ORBE policies, used as a foundation in the remainder of the section. Theorem 2 (ORBE policy). Given an optimal robust policy π⋆ ∈ Π⋆ := argmaxπ∈Π ρπP , if there exists P ∈ P such that ρπ 
⋆ 
P > ρπ ′ 
P for all π′ ∈ Π⋆ \ {π⋆}, then π⋆ is ORBE. 
Proof. First, π⋆ is optimal robust by definition. Second, to show that π⋆ is also best-effort, we must show there is no other policy π′ ∈ Π \ {π⋆} that strictly dominates π⋆. By construction, π⋆ cannot be dominated by any π′ ∈ Π⋆ \{π⋆}. For any other policy π′′ ∈ Π \Π⋆, we have ρπ 
⋆ 
P > ρπ ′′ 
P and, moreover, as ρπ 
⋆ 
P = minP∈P ρπP (cf. Eq. (4)), it holds that ρπ 
⋆ 
P ′ ≥ ρπ ⋆ 
P for all P ′ ∈ P . By letting P ′ ∈ argminP∈P ρπ ′′ 
P , we thus obtain ρπ 
⋆ 
P ′ ≥ ρπ ⋆ 
P > ρπ ′′ 
P = ρπ ′′ 
P ′ , which proves that π′′ ̸>P π⋆. Thus, the policy π⋆ is ORBE. 
In the remainder of this section, we use Theorem 2 to derive conditions under which an optimal robust policy is also best-effort (and thus ORBE). First of all, if an optimal robust policy is unique, then this policy is also best-effort. Corollary 1. Let Π⋆ = argmaxπ∈Π ρπP be the set of optimal robust policies. If Π⋆ is a singleton, then π⋆ ∈ Π⋆ is ORBE. 
ORBE via optimistic RVI. The second observation is that, if an optimal robust policy is not unique but further optimizing via robust value iteration (RVI) for the optimistic (i.e., maximizing) transition function does yield a unique optimum, then the resulting policy is also best-effort. 
36123
0 0.5 
1 
0 0.5 
1 0 
3 
6 
v 
∇vZ 
P (s1, a1 )(s1) 
P (s1 , a 1 )(s2 ) 
Zπ P,s1 
0 0.5 
1 
0 0.5 
1 0 
3 
6 
v 
∇vZ 
P (s1, a2 )(s1) 
P (s1 , a 2 )(s2 ) 
Zπ′ 
P,s1 
Figure 3: The directional derivative ∇vZ π P,s1 
for β = 0 (shown in the right half) is strictly larger than for any β > 0. Hence, we conclude that the policy for β = 0 is ORBE. 
Corollary 2. Let Π̌⋆ = argmaxπ∈Π ρπP and let Π̂⋆ = argmaxπ∈Π̌⋆ maxP∈P ρπP be the set of policies that (within Π̌⋆) maximize the expected return under the maximizing P ∈ P . If Π̂⋆ is a singleton, then π⋆ ∈ Π̂⋆ is ORBE. 
Example 2. Consider again the RMDP in Fig. 1. Even though all policies are optimal robust, only the policy for β = 0 is optimal under the maximizing transition function (which is attained for ξ = 0.5). Thus, the policy for β = 0, i.e., always choosing action a2, is ORBE. 
ORBE via derivatives. Another way to determine if a policy is best-effort is to reason about the derivative of the value function. Let ∇vf(x) = v⊤ · ∂f(x)∂x be the directional derivative of the function f : Rn → R in the direction v ∈ Rn. Recall from Def. 8 that Zπ 
P,s̄ is the value function in state s̄ when the transition function is fixed in all states except s̄. The next result states that, if an optimal robust policy π⋆ 
leads, for every state s̄, to a strictly higher derivative of Zπ P,s̄(Ps̄) than all other optimal robust policies, then π⋆ is 
best-effort. This derivative can be taken in any direction such that the perturbed Ps̄ is still within the uncertainty set Ps̄. 
Corollary 3. Let π̄ ∈ Π⋆ = argmaxπ∈Π ρπ̄P be an optimal robust policy with minimizer P ⋆ ∈ argminP∈P ρπ̄P . Define Π⋆ 
(1) = argmaxπ∈Π⋆ ρπP⋆ and pick a policy π⋆ ∈ Π⋆ (1). The 
policy π⋆ is ORBE if, for all states s̄, there exists a vector v ∈ R|S| such that ∃ϵ > 0, P ⋆ 
s̄ + ϵv ∈ Ps̄ and 
∇vZ π⋆ 
P⋆,s̄(P ⋆ s̄ ) > ∇vZ 
π′ 
P⋆,s̄(P ⋆ s̄ ) ∀π′ ∈ Π⋆ 
(1) \ {π ⋆}. (6) 
Intuitively, the condition that there exists ϵ > 0 such that P ⋆ s̄ + ϵv ∈ Ps̄ encodes that the vector v at the minimizing 
transition function P ⋆ points inside the uncertainty set Ps̄. 
Example 3. Another way to characterize the ORBE policy of β = 0 in Fig. 1 is to compare the derivatives of Zπ P,s1 
at the minimizing transition function ξ = 0. In this example, the only feasible direction is v = [−α, α], α > 0, as shown in Fig. 3. Any change in P (s1, a1)(s1) and P (s1, a1)(s2) causes a change twice as big in P (s1, a2)(s1) and P (s1, a2)(s1), visualized by the longer vectors in Fig. 3. Thus, the directional derivative for the policy with β = 0 (i.e., always choosing action a2) is strictly larger than for all β > 0. Therefore, the policy with β = 0 is ORBE. 
Conversely, we can consider the derivative of the value function under the policies π⋆ ∈ Π̂⋆ (as defined in Corol-lary 2) that are, besides being optimal robust, also optimal under the maximizing transition function. In this case, if π⋆ 
leads to a strictly lower directional derivative ∇vZ π⋆ 
P,s̄(Ps̄) 
than all other policies π′ ∈ Π⋆ \ {π⋆}, then π⋆ is best-effort. This result and the proof are analogous to Corollary 3, so we omit a formal statement due to space limitations. 
Completeness. So far, we have shown that an optimal robust policy π⋆ is best-effort if either of the following holds: 1. π⋆ is uniquely optimal (in the minimizing or maximizing 
sense with respect to the transition function). 2. π⋆ yields a uniquely highest (resp. lowest) directional 
derivative at the minimizing (resp. maximizing) P ⋆ ∈ P . In this section, we complete the characterization by showing that any policy that satisfies these conditions up to this uniqueness is also best-effort. Theorem 3 formalizes this non-trivial result. For conciseness, we defer the preliminaries needed for the proof of Theorem 3 to Abate et al. (2025, Appendix A). Theorem 3 (Computing ORBE policies). Let Π⋆ = argmaxπ∈Π ρπP be the optimal robust policies. Pick two transition functions P (1), P (2) ∈ P such that P (1) ̸= P (2) and, for all s̄ ∈ S, the line gs̄(λ) = λP 
(1) s̄ +(1−λ)P (2) 
s̄ intersects the relative interior1 of Ps̄, or Ps̄ ∩ {gs̄(λ)} = Ps̄. Define 
Π⋆ (1) = argmax 
π∈Π⋆ 
ρπP (1) , Π⋆ (2) = argmax 
π∈Π⋆ (1) 
ρπP (2) . 
Choose a policy π⋆ ∈ Π⋆ (2) s.t., for all s̄ ∈ S, it holds that 
∇vZ π⋆ 
P (1),s̄(P (1) s̄ ) ≥ ∇vZ 
π′ 
P (1),s̄(P (1) s̄ ) ∀π′ ∈ Π⋆ 
(2), (7a) 
∇vZ π⋆ 
P (2),s̄(P (2) s̄ ) ≤ ∇vZ 
π′ 
P (2),s̄(P (2) s̄ ) ∀π′ ∈ Π⋆ 
(2), (7b) 
where the vector v ∈ R|S| is defined as 
v = 
{ P (2) − P (1) if ρπ 
⋆ 
P (2) > ρπ ⋆ 
P (1) , 
P (1) − P (2) otherwise. Then, the policy π⋆ is ORBE 
In the proof, presented in Abate et al. (2025, Appendix A), we show that there always exists a policy π⋆ ∈ Π⋆ 
(2) that satisfies Eqs. (7a) and (7b). As discussed next, a practical implementation of Theorem 3 is to choose P (1) and P (2) as worst- and best-case transition functions. 
5.3 Algorithm Theorem 3 leads to Algorithm 1 for computing an ORBE policy. In particular we iteratively refine Π by applying the criteria presented above to obtain an ORBE policy. 
We first use robust value iteration to compute the set of optimal robust policies (Line 1), which, if a singleton2, consists 
1The relative interior of a convex set X is defined as relint(X) := {x ∈ X : ∀y ∈ X, ∃λ > 1. λx+ (1− λ)y ∈ X}. 
2An optimal policy π⋆ is unique if, for every state s ∈ S, the robust value V π⋆ 
P (s) is strictly higher than R(s, a)+⟨γP (s, a), V π⋆ 
P ⟩ for all other actions a ̸= π⋆(s) (Puterman 1994). For randomized policies, we instead must check for strict concavity of the value function with respect to the policy, e.g., by deriving the optimal robust Bellman operator explicitly as in Kumar et al. (2024). 
36124
Algorithm 1: Computation of ORBE policy. 
Input: s-rectangular RMDP (S,A,P, r, γ) Output: ORBE policy π⋆ ∈ Π⋆ 
BE 1: Π← argmaxπ minP∈P ρπP 2: if |Π| > 1 then 3: Π← argmaxπ∈Π maxP∈P ρπP 4: if |Π| > 1 then 5: π ← Π 6: P (1) ← argminP∈P ρπP 7: P (2) ← argmaxP∈P ρπP 8: Π← argmaxπ∈Π ρπ 
P (1) 
9: Π← argmaxπ∈Π ρπ P (2) 
10: v← P (2) − P (1) ∀s̄ 11: Π←×s̄∈S argmaxπ(s̄)∈Π∇vZ 
π P (1),s̄ 
(P (1) s̄ ) 
12: if |Π| > 1 then 13: Π←×s̄∈S argminπ(s̄)∈Π∇vZ 
π P (2),s̄ 
(P (2) s̄ ) 
14: return any π⋆ ∈ Π 
of an ORBE policy by Corollary 1, thus solving Problem 1. Otherwise, we analogously compute the set of optimal policies under the maximizing transition function (Line 3), which, if a singleton, contains an ORBE policy by Corollary 2. 
If this set is still not a singleton, we arbitrarily select a policy π from the remaining updated set Π (Line 5) and compute the minimizing and maximizing transition functions P (1) and P (2) (Lines 6 and 7). We then refine the policy set by keeping only those that first maximize the expected return for P (1) 
and then for P (2) (Lines 8 and 9). For every s̄ ∈ S, we define v← P (2)−P (1) as per Theorem 3 (Line 10). Next, we refine the set of policies by, in every state s̄ ∈ S, only selecting actions that maximize the directional derivative at the minimizer P (1) (Line 11). The Cartesian product Π←×s̄∈S · · · of these actions gives the set of policies that satisfy Eq. (7a). If Π is now a singleton, then it satisfies Corollary 3 and, thus, π⋆ ∈ Π is ORBE. Otherwise, if multiple policies remain, we perform the analogous refinement—over the set of policies obtained in Line 11—to minimize the directional derivative at the maximizing transition function P (2) (Line 13). 
Any returned policy π⋆ satisfies at least one of the Corol-laries 1 to 3 or Theorem 3, thus showing that the algorithm always returns a ORBE policy. 
Remark 2. We can easily amend Algorithm 1 for a policy that minimizes expected return under the maximizing probabilities. In this case, we replace all min with max and vice versa. We shall see such an application in Sect. 6. 
Complexity. The computations in Algorithm 1 lead to a manageable overhead compared to the standard robust value iteration in Line 2. First, Line 3 amounts to running robust value iteration again, but over a potentially smaller subset of actions per state, increasing complexity by a constant smaller than 2. Next, Lines 6 to 9 compute the minimizer and maximizer, and solve the two associated MDPs using standard value iteration. Finally, maximizing the derivatives (Line 11) amounts to solving a linear equation system of size |S| for ev-
ery state and action (Heck et al. 2022; Badings et al. 2023a). Solving each equation system has worst-case complexity O(|S|3), yielding an overall complexity of O(|S|4 · |A|) for Line 11 (and, by symmetry, also for Line 13). Thus, whenever computing an optimal robust policy is feasible, the additional overhead of Algorithm 1 is also manageable. 
6 Empirical Evaluation In Sect. 5, we presented an efficient and complete algorithm for computing ORBE policies. In this section, we experimentally show the applicability of our algorithm within different implementations of robust value iteration. Our primary objective is to provide a proof of concept to confirm the theoretical results from Sect. 5. The experiments ran on an Apple Mac-Book with an M4 Pro chip and 24GB of RAM. The code is available on https://github.com/tbadings/best-effort-rmdps. 
6.1 Best-Effort Policies for Interval MDPs We consider robust value iteration within PRISM, a popular tool for MDPs (Kwiatkowska, Norman, and Parker 2011). PRISM only supports interval MDPs (IMDPs), i.e., (s, a)-rectangular RMDPs with interval-valued probabilities. We consider variants of a slippery gridworld IMDP (see Abate et al. (2025, Appendix B) for details). The objective is to minimize the expected number of steps to reach the goal state. When the agent slips, it remains in the same state. The agent can move in each direction with two actions: one where the slipping probability p is fixed, and one where it belongs to the interval [q, p]. Since the goal is to minimize the number of steps, the worst-case slipping probability is p, so the robust value of both action types is the same. However, only a policy that always picks the interval-valued action is best-effort. 
To show that PRISM returns an arbitrary optimal robust (but not necessarily ORBE) policy, we define the IMDP’s actions in different orders. Let ν ∈ [0, 1] be the fraction of states in which the best-effort action is defined first. We consider ν = 0 (non-best-effort always defined first), ν = 1 (best-effort defined first), and ν = 0.5 (a coin-flip decides which action is defined first). We repeat each experiment over 10 seeds. The results in Table 1 show the percentage of states where the optimal robust policy returned by PRISM chooses the best-effort action (i.e., the action with an interval for the slipping probability). Essentially, the PRISM policy sticks to the first action it finds to be optimal robust, so the fraction of best-effort actions is roughly proportional to ν. Thus, PRISM finds optimal robust policies, but not necessarily ORBE ones. 
Conversely, for our method, we apply Corollary 2 by again running robust value iteration with PRISM, but this time over the optimal robust policies and for the best-case slipping probability. This second run of value iteration is over a smaller set of policies and less than doubles the runtime (especially for |S| = 104), thus confirming our results from Sect. 5: the complexity for computing ORBE policies is still dominated by that of robust value iteration, making the process feasible whenever robust optimal policies can be computed. The policy obtained using our approach always chooses actions with the interval-valued slipping probabilities. Thus, and as confirmed by the rightmost column of Table 1, the use of Corollary 2 indeed always leads to ORBE policies. 
36125
PRISM + Best-case (Corr. 2) 
|S| ν Time [s] BE [%] Time [s] BE [%] 
100 0.0 2.0 21.9 3.9 100.0 0.5 1.9 59.6 3.8 100.0 1.0 1.9 89.9 3.9 100.0 
900 0.0 2.1 23.3 4.0 100.0 0.5 2.1 62.0 4.1 100.0 1.0 2.1 87.4 4.2 100.0 
10 000 0.0 48.9 21.2 54.4 100.0 0.5 54.9 39.3 61.2 100.0 1.0 51.0 85.4 56.5 100.0 
Table 1: Comparison to PRISM on the gridworld IMDPs, showing the grid sizes, probability ν to define the best-effort action first, runtimes, and percentage of states in which the resulting optimal policy chooses a best-effort (BE) action. 
RVI + Best-case (Corr. 2) + Deriv. (Corr. 3) 
|S| ν Time [s] BE [%] Time [s] BE [%] Time [s] BE [%] 
100 0.0 7.0 0.0 11.7 100.0 7.1 100.0 0.5 7.0 49.2 11.7 100.0 7.1 100.0 1.0 7.6 100.0 12.7 100.0 7.6 100.0 
400 0.0 49.5 0.0 83.4 100.0 50.1 100.0 0.5 50.1 48.0 84.4 100.0 50.6 100.0 1.0 48.4 100.0 81.7 100.0 48.9 100.0 
900 0.0 163.6 0.0 274.4 100.0 172.0 100.0 0.5 163.4 50.1 273.8 100.0 171.9 100.0 1.0 164.1 100.0 275.0 100.0 172.6 100.0 
Table 2: Results on the gridworld RMDPs, for robust value iteration (RVI), RVI plus optimizing for the best-case probabilities, and RVI plus optimizing for the derivatives. 
6.2 Best-Effort Policies for s-Rectangular RMDPs 
To show the applicability of our methods beyond IMDPs, we create a basic implementation of robust value iteration and the derivative computation for s-rectangular RMDPs (see Abate et al. (2025, Appendix B) for details). We consider variants of the same slippery gridworld as in Sect. 6 but now with an s-rectangular uncertainty set. For this RMDP, either Corollary 2 or 3 is sufficient to obtain an ORBE policy. Therefore, instead of implementing Algorithm 1 sequentially, we test both separately on top of robust value iteration. 
The results in Table 2 give the same picture as in Sect. 6: if multiple optimal robust policies exist, robust value iteration returns the first optimal actions it finds. By contrast, our methods provide simple yet effective tie-break rules, either by returning a policy that is also optimal under the best-case transition probabilities (RVI + Corollary 2), or by returning a policy with the highest derivatives (RVI + Corollary 3). The former less than doubles the total runtime (especially for the larger models), while computing derivatives is even cheaper, increasing the total runtime by less than 10%. 
7 Related Work The notion of best-effort was first introduced in a game theoretic context by Faella (2009) as a relaxation of “winning” policies (or strategies). These ideas have been adapted to reactive synthesis, where in the absence of a winning strategy, best-effort policies can be computed at the same cost (Aminof et al. 2019, 2020; De Giacomo, Parretti, and Zhu 2025). Clos-est to our work are Aminof et al. (2023) and Giacomo, Fa-vorito, and Silo (2024), who study best-effort for stochastic games where each transition probability is only constrained to lie within the open interval (0, 1). Crucially, Aminof et al. (2023); Giacomo, Favorito, and Silo (2024) exploit this lack of probability bounds to construct a three-valued abstraction of policies (winning, losing, and pending) which is central to their characterization of best-effort policies. However, this does not carry over to RMDPs, where probabilities are bounded subsets of [0, 1], thus breaking a direct translation of their characterization to the RMDP setting. 
Related are lexicographic orderings over objectives for MDPs (Wray, Zilberstein, and Mouaddib 2015) and algorithms for stochastic games that progressively prune suboptimal actions per objective (Chatterjee et al. 2024). While our algorithm is conceptually similar, the refinement to best-effort policies requires different reasoning over the dominance order over policies. In multi-objective MDPs (MOMDPs), multiple objectives are combined, leading to Pareto optimality (Delgrange et al. 2020; Etessami et al. 2008). While MOMDPs require a trade-off between the objectives, our setting uses best-effort as a hard refinement within the optimal robust policies. Finally, weakly related are partial orders over states of MDPs (Roux and Pérez 2018) and monotonicity in parametric Markov chains (Spel, Junges, and Katoen 2019). 
While we focus on s-rectangular RMDPs, our definitions of best-effort and dominance carry over to other models, such as k- or non-rectangular RMDPs (Mannor et al. 2004; Goyal and Grand-Clément 2023; Gadot et al. 2024) and parametric MDPs (Quatmann et al. 2016). However, computing optimal policies for these models is much harder—up to NP-hard for general non-rectangular RMDPs (Wiesemann, Kuhn, and Rustem 2013). Thus, adapting dynamic programming methods to these models is still an open problem. 
8 Conclusion We presented a principled tie-breaker among optimal robust policies in RMDPs based on best-effort. Our proposed ORBE policies maximize the worst-case expected return but also achieve a maximal expected return under non-adversarial transition probabilities. We fully characterized ORBE policies and presented an algorithm for computing them. Our experiments showed how to use our methods as an effective and efficient tie-breaker within robust value iteration. 
Future work includes generalizing our methods to nonrectangular RMDPs or parametric MDPs. Moreover, our methods still rely on first computing a policy under adversarial transition probabilities. A next step is to consider ε-close optimal robust policies and optimize for best-effort within this broader context. Finally, we aim to study settings with a Bayesian prior over the uncertainty set (Murphy 2001). 
36126
Acknowledgments This research is supported by the EPSRC grant EP/Y028872/1, Mathematical Foundations of Intelli-gence: An “Erlangen Programme” for AI. 
References Abate, A.; Badings, T.; Giacomo, G. D.; and Fabiano, F. 2025. Best-Effort Policies for Robust Markov Decision Processes (Extended Version with Appendix). CoRR, abs/2508.07790. Aminof, B.; Giacomo, G. D.; Lomuscio, A.; Murano, A.; and Rubin, S. 2020. Synthesizing strategies under expected and exceptional environment behaviors. In IJCAI, 1674–1680. ijcai.org. Aminof, B.; Giacomo, G. D.; Murano, A.; and Rubin, S. 2019. Planning under LTL Environment Specifications. In ICAPS, 31–39. AAAI Press. Aminof, B.; Giacomo, G. D.; Rubin, S.; and Zuleger, F. 2023. Stochastic Best-Effort Strategies for Borel Goals. In LICS, 1–13. IEEE. Åström, K. J. 2012. Introduction to stochastic control theory. Courier Corporation. Badings, T. S.; Junges, S.; Marandi, A.; Topcu, U.; and Jansen, N. 2023a. Efficient Sensitivity Analysis for Para-metric Robust Markov Chains. In CAV (3), volume 13966 of Lecture Notes in Computer Science, 62–85. Springer. Badings, T. S.; Simão, T. D.; Suilen, M.; and Jansen, N. 2023b. Decision-making under uncertainty: beyond probabilities. Int. J. Softw. Tools Technol. Transf., 25(3): 375–391. Chatterjee, K.; Katoen, J.; Mohr, S.; Weininger, M.; and Win-kler, T. 2024. Stochastic games with lexicographic objectives. Formal Methods Syst. Des., 63(1): 40–80. Davis, M. H. 2018. Markov models & optimization. Rout-ledge. De Giacomo, G.; Parretti, G.; and Zhu, S. 2025. Symbolic LTLf Synthesis: A Unified Approach for Synthesizing Win-ning, Dominant, and Best-Effort Strategies. SN Computer Science, 6(2): 147. Delgrange, F.; Katoen, J.; Quatmann, T.; and Randour, M. 2020. Simple Strategies in Multi-Objective MDPs. In TACAS (1), volume 12078 of Lecture Notes in Computer Science, 346–364. Springer. Etessami, K.; Kwiatkowska, M. Z.; Vardi, M. Y.; and Yan-nakakis, M. 2008. Multi-Objective Model Checking of Markov Decision Processes. Log. Methods Comput. Sci., 4(4). Faella, M. 2009. Admissible Strategies in Infinite Games over Graphs. In MFCS, volume 5734 of Lecture Notes in Computer Science, 307–318. Springer. Gadot, U.; Derman, E.; Kumar, N.; Elfatihi, M. M.; Levy, K.; and Mannor, S. 2024. Solving Non-rectangular Reward-Robust MDPs via Frequency Regularization. In AAAI, 21090– 21098. AAAI Press. Giacomo, G. D.; Favorito, M.; and Silo, L. 2024. Composi-tion of Stochastic Services for LTLf Goal Specifications. In FoIKS, volume 14589 of Lecture Notes in Computer Science, 298–316. Springer. 
Goyal, V.; and Grand-Clément, J. 2023. Robust Markov Decision Processes: Beyond Rectangularity. Math. Oper. Res., 48(1): 203–226. Hanheide, M.; Göbelbecker, M.; Horn, G. S.; Pronobis, A.; Sjöö, K.; Aydemir, A.; Jensfelt, P.; Gretton, C.; Dearden, R.; Janı́cek, M.; Zender, H.; Kruijff, G. M.; Hawes, N.; and Wyatt, J. L. 2017. Robot task planning and explanation in open and uncertain worlds. Artif. Intell., 247: 119–150. Heck, L.; Spel, J.; Junges, S.; Moerman, J.; and Katoen, J. 2022. Gradient-Descent for Randomized Controllers Under Partial Observability. In VMCAI, volume 13182 of Lecture Notes in Computer Science, 127–150. Springer. Iyengar, G. N. 2005. Robust Dynamic Programming. Math. Oper. Res., 30(2): 257–280. Kumar, N.; Wang, K.; Levy, K. Y.; and Mannor, S. 2024. Efficient Value Iteration for s-rectangular Robust Markov Decision Processes. In ICML. OpenReview.net. Kwiatkowska, M. Z.; Norman, G.; and Parker, D. 2011. PRISM 4.0: Verification of Probabilistic Real-Time Systems. In CAV, volume 6806 of Lecture Notes in Computer Science, 585–591. Springer. Mannor, S.; Simester, D.; Sun, P.; and Tsitsiklis, J. N. 2004. Bias and variance in value function estimation. In ICML, volume 69 of ACM International Conference Proceeding Series. ACM. Moerland, T. M.; Broekens, J.; Plaat, A.; and Jonker, C. M. 2023. Model-based Reinforcement Learning: A Survey. Found. Trends Mach. Learn., 16(1): 1–118. Murphy, K. 2001. An introduction to graphical models. Rap. tech, 96: 1–19. Nilim, A.; and Ghaoui, L. E. 2005. Robust Control of Markov Decision Processes with Uncertain Transition Matrices. Oper. Res., 53(5): 780–798. Puterman, M. L. 1994. Markov Decision Processes: Dis-crete Stochastic Dynamic Programming. Wiley Series in Probability and Statistics. Wiley. Quatmann, T.; Dehnert, C.; Jansen, N.; Junges, S.; and Ka-toen, J. 2016. Parameter Synthesis for Markov Models: Faster Than Ever. In ATVA, volume 9938 of Lecture Notes in Com-puter Science, 50–67. Roux, S. L.; and Pérez, G. A. 2018. The Complexity of Graph-Based Reductions for Reachability in Markov Deci-sion Processes. In FoSSaCS, volume 10803 of Lecture Notes in Computer Science, 367–383. Springer. Russell, S. J.; and Norvig, P. 2010. Artificial Intelligence -A Modern Approach, Third International Edition. Pearson Education. Spel, J.; Junges, S.; and Katoen, J. 2019. Are Parametric Markov Chains Monotonic? In ATVA, volume 11781 of Lecture Notes in Computer Science, 479–496. Springer. Suilen, M.; Badings, T. S.; Bovy, E. M.; Parker, D.; and Jansen, N. 2024. Robust Markov Decision Processes: A Place Where AI and Formal Methods Meet. In Principles of Verification (3), volume 15262 of Lecture Notes in Computer Science, 126–154. Springer. 
36127
Wiesemann, W.; Kuhn, D.; and Rustem, B. 2013. Robust Markov Decision Processes. Math. Oper. Res., 38(1): 153– 183. Wray, K. H.; Zilberstein, S.; and Mouaddib, A. 2015. Multi-Objective MDPs with Conditional Lexicographic Reward Preferences. In AAAI, 3418–3424. AAAI Press. 
36128