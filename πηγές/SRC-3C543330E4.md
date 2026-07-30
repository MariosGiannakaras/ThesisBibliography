> Source: https://proceedings.mlr.press/v237/peng24a/peng24a.pdf

Proceedings of Machine Learning Research vol 237:1–25, 2024 35th International Conference on Algorithmic Learning Theory 
The complexity of non-stationary reinforcement learning 
Binghui Peng BP2601@COLUMBIA.EDU Columbia University 
Christos Papadimitriou CHRISTOS@COLUMBIA.EDU 
Columbia University 
Editors: Claire Vernade and Daniel Hsu 
Abstract The problem of continual learning in the domain of reinforcement learning, often called nonstationary reinforcement learning, has been identified as an important challenge to the application of reinforcement learning. We prove a worst-case complexity result, which we believe captures this challenge: Modifying the probabilities or the reward of a single state-action pair in a reinforcement learning problem requires an amount of time almost as large as the number of states in order to keep the value function up to date, unless the strong exponential time hypothesis (SETH) is false; SETH is a widely accepted strengthening of the P ̸= NP conjecture. Recall that the number of states in current applications of reinforcement learning is typically astronomical. In contrast, we show that just adding a new state-action pair is considerably easier to implement. Keywords: Non-stationary reinforcement learning, fine-grained complexity 
1. Introduction 
Reinforcement learning (RL) (Sutton and Barto, 2018), the branch of machine learning seeking to create machines that react to a changing environment so as to maximize long-term utility, has recently seen tremendous advances through deep learning (Silver et al., 2017, 2018), as well as a vast expansion of its applicability and reach to many application domains, including board games, robotics, self-driving cars, control, and many more. As with most aspects of deep learning, one of the most important current challenges in deep RL lies in handling situations in which the model undergoes changes. Variably called non-stationary RL, continual RL, multi-task RL, or life-long RL, the problem of enabling RL to react effectively and gracefully to sequences of changes in the underlying Markov model has been identified as an important open problem in practice, see the prior work subsection for many references, and Khetarpal et al. (2022) for a recent survey of the challenge and the available remedies. 
When it becomes clear that a particular computational problem is difficult, the field of computational complexity (Papadimitriou and Steiglitz, 1998; Papadimitriou, 2003; Arora and Barak, 2009) comes into play: the search for mathematical obstacles to the efficient solution of problems. The identification of such obstacles is often informative about the kinds of remedies one needs to apply to the problem. As far as we can tell, the computational complexity of non-stationary RL (NSRL) has not been explored in the past; in contrast, see Chen et al. (2022) for an example of recent progress in identifying complexity obstacles in continual learning of classification tasks. 
In this paper, we initiate the analysis of NSRL from the standpoint of computational complexity. We consider finite horizon MDPs — it is easy to see that our results can be extended very easily to infinite horizon MDPs. We ask the following question: Suppose that we have already solved a finite-horizon MDP, and that the MDP changes in some small way; how difficult is it to modify the 
© 2024 B. Peng & C. Papadimitriou.
PENG PAPADIMITRIOU 
solution? If the solution we want to update is an explicit mapping from states to actions, then it is not hard to see that this problem is hopeless: a small local change can cause a large proportion of the values of this map to change1. In practice, however, deep RL is not about computing explicitly the optimum solution of the problem; it is about maintaining an implicit, deep-net representation of a good approximation of the optimum solution, and only the parameters of this representation are updated. Our results address precisely this aspect of the difficulty. 
We consider elementary local changes to the RL problem, which we believe capture well the nature of the NSRL problem: We choose a state-action pair and we modify somehow its parameters: the reward, and the transition probability distribution. Our results hold for the most elementary possible change: We only modify two transition probabilities in one state-action pair. (Naturally, it is impossible to modify only one probability in a distribution...) We prove that, under widely accepted complexity assumptions to be explained soon, the amount of computation needed to update an ϵ-optimal value approximation in the face of such an elementary change is, in the worst case, comparable to the number of states (the precise result is stated below). Since in the problems currently solved by deep RL the number of states of the underlying MDP is typically astronomical, such a prediction is bad indeed — it means that we essentially have to start all over because of a small change. Now, in deep learning we know well that a worst-case result is never the last word on the difficulty of a problem. However, we believe that an alarming worst-case result, established for an aspect of the problem which has been identified in practice to be a challenge, is a warning sign which may yield valuable hints about the corrective action that needs to be taken in order to overcome the current bottleneck. 
We complement this lower bound with a positive result for a different kind of change: adding a new action to a state. It turns out that this is a simpler problem, and an ϵ-approximate solution can be updated in time polynomial in 1 
ϵ and the horizon. 
Related work 
Non-stationary MDPs have been studied extensively in recent years from the point of view of dynamic regret (Auer et al., 2008; Dick et al., 2014; Ortner et al., 2020; Cheung et al., 2020; Zhou et al., 2022; Li and Li, 2019; Touati and Vincent, 2020; Wei and Luo, 2021; Domingues et al., 2021; Mao et al., 2021; Jiang et al., 2023; Feng et al., 2023); In Mao et al. (2021) an algorithm with total regret Õ(S1/3A1/3∆1/3HT 2/3) is provided, where T is the total number of iteration, ∆ is the variational budget that measures the total change of MDP. Another line of work (Da Silva et al., 2006; Banerjee et al., 2017; Padakandla et al., 2020; Ornik and Topcu, 2021) focuses on the statistical problem of detecting the changes in the environment. We refer interested reader to Padakandla (2021); Khetarpal et al. (2022) for recent surveys; in particular, Padakandla (2021) mentions the computational difficulty of the change problem, which is an important yet unresolved open question in the literature. Several approaches to NSRL — e.g Wei and Luo (2021); Mao et al. (2021) — resort to restarting the learning process if enough change has accumulated; our results suggest that, indeed, restarting may be preferable to updating. Additional literature can be found at Appendix A. 
1. For example, consider the extreme example where a change in an action increases the value of the next state, and this in turn changes the optimum actions in almost all other states. 
2
NON-STATIONARY REINFORCEMENT LEARNING 
A brief overview of the main result 
In the rest of the paper we use the o(1) notation; in particular, Ω(n1−o(1)) is the class of functions that is at least n1−ϵ for any ϵ > 0 when n→ +∞, and no(1) is the class of functions that is no more than nϵ for any ϵ > 0 when n→ +∞ 
Our main result (Theorem 1) states that, in the worst case, an elementary change in an MDP — just updating two transition probabilities in one action at one state of the MDP — requires time Ω((SAH)1−o(1)), where S is the number of states, A is the number of actions and H is the horizon. The proof is based on the Strong Exponential Time Hypothesis (SETH), which is a central conjecture in complexity, a refinement of P ̸= NP. SETH has many applications in graph algorithms (Roditty and Vassilevska Williams, 2013; Abboud and Williams, 2014; Backurs et al., 2018; Li, 2021; Dalirrooyfard et al., 2022), edit distance (Backurs and Indyk, 2015), nearest neighbor search (Rubinstein, 2018), kernel estimation (Charikar and Siminelakis, 2017; Alman et al., 2020) and many other domains; see (Rubinstein and Williams, 2019) for a comprehensive survey. SETH states that, if the k-SAT problem (the Boolean satisfiability problem when each clause contains at most k literals) can be solved in time O(2ckn), then the limit of ck as k grows is one. Our work is based on the important result of (Abboud et al., 2017) on the hardness, under SETH, of approximating the bichromatic Maximum Inner Product (MAX-IP) problem. Subsequent work has improved the approximation parameter (Rubinstein, 2018; Chen, 2020) and applied the technique to the Dynamic Coverage problem (Abboud et al., 2019; Peng, 2021). 
We reduce from the MAX-IP problem, where we are given two collections of sets B1, . . . , Bn 
and C1, . . . , Cn, over a small universe [m] with m = no(1). It is known from Abboud et al. (2017) that it is hard to distinguish between the following two scenaria: (a) Bi ⊆ Cj for some i, j ∈ [n], and (b) |Bi ∩ Cj | ≤ |Cj |/2log(n) 
1−o(1) for all i, j ∈ [n]. That is, it is hard to tell the difference between 
the case of a complete containment and the case of tiny intersections. The first step of our reduction is to construct a finite-horizon MDP such that the state of the first step (h = 1) corresponds to the sets B1, . . . , Bn and the state of the second step (h = 2) corresponds to the universe [m]. The state of the second step has either high reward or low reward, depending on the time t. By applying a sequence of changes to the state-action transition in the second step, based on the structure of the sets C1, . . . , Cn, one obtains a reduction from MAX-IP establishing a lower bound of Ω(S2−o(1)) for this sequence. However, since this sequence is of length S1+o(1) (because of the size of the Cj sets), we obtain an Ω(S1−o(1)) amortized lower bound for each step of the sequence, and this completes the reduction to the NSRL problem. 
The construction so far yields an approximation ϵ that is very small (i.e., S−0.001). We need a second stage of our construction to amplify ϵ to some constant such as 0.1. This is achieved by stacking multiple layers of the basic construction outlined above. Finally, by spreading the stateactions across multiple steps, we improve the lower bound to Ω((SAH)1−o(1)). 
The complete proof can be found at Section 3. 
2. Preliminary Definitions 
Here we shall define non-stationary MDPs. Let S be a state space (|S| = S), A an action space (|A| = A), H ∈ Z+ the planning horizon. Next let T ∈ Z+ be the number of rounds: The intention is that the MDP will repeat T times, with action parameters changed between rounds. 
A non-stationary finite horizon MDP is a set of T MDPs ({Sh,Ah, Pt,h, rt,h}t∈[T ],h∈[H], sinit). Sh ⊆ S is the state space and Ah ⊆ A is the action space at the h-th step (h ∈ [H]), and Pt,h : 
3
PENG PAPADIMITRIOU 
Sh × Ah → ∆Sh+1 is the transition function, where ∆Sh 
is the set of all probability distributions over Sh, and rt,h : Sh × Ah → [0, 1] is the reward function at the h-th step of the t-th round (h ∈ [H], t ∈ [T ]). We use sinit ∈ S1 to denote the initial state. 
We focus on deterministic non-stationary policies π = (π1, . . . , πT ), though our results can be applied to randomized policies as well. Let πt = (πt,1, . . . , πt,H) be the policy of the t-th round (t ∈ [T ]) and πt,h : Sh → Ah (h ∈ [H]) be the decision at the h-th step. Given a policy π, the Q-value of a state-action pair (s, a) ∈ Sh ×Ah at the t-round can be determined 
Qπt t,h(s, a) = rt,h(s, a) + E 
[ H∑ 
ℓ=h+1 
rt,h(st,ℓ, πt,ℓ(st,ℓ)) | st,h = s, at,h = a 
] ∀s ∈ Sh, a ∈ Ah 
and the V -value 
V πt t,h(s) = E 
[ H∑ ℓ=h 
rt,h(st,ℓ, πt,ℓ(st,ℓ)) | st,h = s 
] ∀s ∈ St,h. 
Let π∗ t be the optimal policy at the t-round, and Q∗ 
t , V ∗ t be its Q-value and V -value. The goal is 
to maintain an ϵ-approximate value function. In particular, we require that an approximation Vt of the value of the initial state sinit be maintained, such that for all rounds t ∈ [T ],∣∣Vt − V ∗ 
t,1(sinit) ∣∣ ≤ ϵ. 
Updates. All T MDPs of our definition must be solved, one after the other, in the face of parameter changes that are meant to be extremely simple and local: For the t-th update, an adversary picks an arbitrary state-action pair (sh, ah) ∈ Sh × Ah, and changes the transition function from Pt−1,h(sh, ah) to Pt,h(sh, ah) and the reward from rt−1,h(sh, ah) to rt,h(sh, ah). It also changes the transition function from Pt−1,h(sh, ah) to Pt,h(sh, ah), such that these two distributions differ in exactly two states. That is, the change in the distribution is the smallest kind imaginable: Two next states are chosen, and the probability mass of the first is transferred to the second. Since the changes we consider are the simplest possible, our proof that even these changes are computationally intractable leaves little hope for the worst-case of NSRL. 
3. Hardness of NSRL 
The main result is the following: 
Theorem 1 (Main result, hardness of NRSL) Let S,A,H be sufficiently large integers, and T is bounded by arbitrarily large polynomials T ≤ poly(SAH), while the horizon H ≥ (SA)o(1). Then, unless SETH is false, there is no algorithm with amortized runtime O((SAH)1−o(1)) per update that can approximate the optimal value of a non-stationary MDP over a sequence of T updates. In particular, any algorithm with better runtime fails to distinguish between these two cases: 
 The optimal policy has value at least H 4 at some round t ∈ [T ]; 
 The optimal policy has value at most H 100 for all T rounds. 
4
NON-STATIONARY REINFORCEMENT LEARNING 
Remark 2 (Sequence length and horizon) In the statement of Theorem 1 we assume that T is polynomially bounded. Since T is the sequence of MDPs presented for solution, it would be unreasonable to be exponential, especially in S, which is typically huge. Furthermore, proving lower bounds in the face of exponential T would be impossible, for example, through the slow design of a look-up table that solves the problem. The assumption H ≥ (SA)o(1) is not needed, and our result holds even if H is a constant, but the gap would be smaller than H 
4 vs. H 100 . 
Our result is based on the widely accepted Strong Exponential Time Hypothesis (SETH). 
Conjecture 3 (Strong Exponential Time Hypothesis (SETH), Impagliazzo and Paturi (2001)) For any δ > 0, there exists k ≥ 3 such that the k-SAT problem on n variables cannot be solved in time O(2(1−δ)n). 
Remark 4 (Why we need SETH) The use of a hypothesis stronger than “P ̸= NP” is needed, because it is known that “P ̸= NP” cannot yield any complexity lower bounds within P (where NSRL belongs), see the survey of Williams (2018). 
The starting point of our reduction is the following hardness result for the Bichromatic Maxi-mum Inner Product (MAX-IP) problem, whose proof is based on the machinery of distributed PCP. 
Theorem 5 (Bichromatic Maximum Inner Product (MAX-IP) Abboud et al. (2017)) Let γ > 0 be any constant, and let n ∈ Z+, m = no(1), w = 2(log(n)) 
1−o(1) . Given two collections of sets 
B = {B1, . . . , Bn} and C = {C1, . . . , Cn} over universe [m], satisfying |B1| = · · · = |Bn| = b and |C1| = · · · = |Cn| = c for some b, c ∈ [m]. Unless SETH is false, no algorithm can distinguish the following two cases in time O(n2−γ): 
 YES instance. There exists two sets B ∈ B, C ∈ C such that C ⊆ B; 
 NO instance. For every B ∈ B and C ∈ C, |B ∩ C| ≤ c/w. 
Parameters. We reduce MAX-IP to NSRL. For any sufficiently large parameters S,A,H, T , let 
n = T 1/2−o(1) · (SAH)1/2 and m = no(1) 
be the input parameters of MAX-IP. Given a MAX-IP instance with sets B1, . . . , Bn and C1, . . . , Cn 
over a ground set [m], recall b, c ∈ [m] are the size of set {Bi}i∈[n] and {Ci}i∈[n] . Let 
L = ⌈b/c⌉ and N = SAH 
16L(log2(S) + 2) . 
We shall divide {Bi}i∈[n] into K = n/N batches and each batch contains N sets. That is, {Bi}i∈[n] = {Bk,ν}k∈[K],ν∈[N ]. 
3.1. Construction of a hard instance 
We first describe the MDP at the initial stage (t = 0), with state space {Sh}h∈[H], action space {Ah}h∈[H], transition function {Ph}h∈[H] and reward function {rh}h∈[H]. A (simplified) illustration can be found at Figure 1. We omit the subscript of t = 0 for simplicity. 
5
PENG PAPADIMITRIOU 
Figure 1: A snapshot of the hard instance 
Horizon. We divide the entire horizon into two phases 
[H] = H1 ∪H2, where H1 = [H/2] and H2 = [H/2 : H] . 
The second phase is relatively simple and involves only two terminal states that provide rewards. The first phase is more involved and determines the destination state. 
The first phase contains L layers, and each layer contains H/2L steps 
H1 = H1,1 ∪ · · · ∪ H1,L, where H1,ℓ = 
[ (ℓ− 1) · H 
2L + 1 : ℓ · H 
2L 
] ∀ℓ ∈ [L]. 
The layers are used for amplifying the difference between good and bad policies. The structure of the MDP is for identical for each layer, except the last step at the last layer. 
For each layer ℓ ∈ [L], we further divide it into G := H 2L(log2(S)+2) groups, and each group 
contains log2(S) + 2 steps, H1,ℓ = H1,ℓ,1 ∪ · · · ∪ H1,ℓ,G 
where 
H1,ℓ,g = 
[ (ℓ− 1) · H 
2L + (g − 1)(log2(S) + 2) + 1 : (ℓ− 1) · H 
2L + g · (log2(S) + 2) 
] ∀g ∈ [G]. 
We set h(ℓ, g, τ) := (ℓ − 1)(H/2L) + (g − 1)(log2(S) + 2) + τ be the τ -step, at the g-th group of the ℓ-th layer, where τ ∈ [log2(S) + 2], g ∈ [G], ℓ ∈ [L]. For simplicity, we also write h(ℓ, g) = h(ℓ, g, log2(S) + 2) and h(ℓ) = h(ℓ,G) be the last step of each group and layer. 
States. There are five types of states: terminal states, element states, set states, routing states and the pivotal state. 
 Terminal states. There are two terminal states st1 and st2, and they appear at every steps h ∈ [H]. We use sth,1, s 
t h,2 to denote the terminal states at Sh. 
 Element states. There are m element states {seu}u∈[m] that appear at every step h ∈ H1 of phase one. We use seh,u to denote the u-th element state at Sh. 
6
NON-STATIONARY REINFORCEMENT LEARNING 
 Set states. There are S/4 set states {sbi }i∈[S/4]. The set states only appear on the second last step of each group Hℓ,g. In particular, for each layer ℓ ∈ [L], group g ∈ [G], let sbh(ℓ,g)−1,i 
denote the i-th (i ∈ [S/4]) set state at Sh(ℓ,g)−1. 
 Pivotal state There is one pivotal state sp that appears at every step h ∈ H1 of Phase 1, denoted as sph. The MDP start with the pivotal state, i.e., sinit := sp1. 
 Routing states. The routing states are used for reaching set states. There S/4 routing states {srα}α∈[S/4] that appear at the [2 : log2(S)]-th step of each group. In particular, at layer ℓ ∈ [L], group g ∈ [G], step τ ∈ [2 : log2(S)], let {srh(ℓ,g,τ),α}α∈[1:2τ−2] be the collection of routing states at Sh(ℓ,g,τ). 
The total number of possible states is at most 2 +m+ S/4 + S/4 + 1 ≤ S. 
Actions There are five types of actions. The terminal action at, the element actions ae, the set actions {abj}j∈[A/2], the pivotal action {ap1, a 
p 2} and the routing actions {ar1, ar2}. The total number 
of action is at most A/2 + 6 ≤ A, and we assume these actions appear at every step h ∈ [H]. 
Reward The only state that returns non-zero reward is the terminal state {sth,1}h∈H2 . Formally, we set 
rh(s, a) = 0 when h ∈ H1 and rh(s, a) = 
{ 1 s = sth,1 0 otherwise 
when h ∈ H2. (1) 
Transitions We next specify the transition probability of the initial MDP. (a) Terminal states. The transition of terminal states is deterministic and always keeps the state 
terminal, that is 
Ph(s t h,1, a) = 1{sth+1,1} and Ph(s 
t h,2, a) = 1{sth+1,2} ∀h ∈ [H − 1], a ∈ A. (2) 
Here we use 1{s} ∈ ∆Sh+1 to denote the one-hot vector that is 1 at state s and 0 otherwise. 
Combining with the definition of reward functions, the MDP guarantees that a policy receives H/2 reward once it goes to the first terminal state sth,1 at some step h ∈ H2. Meanwhile, it receives 0 reward if it ever goes to the second terminal state sth,2. 
(b) Element states. At step h < H/2, for any element u ∈ [m], the transition function of seh,u equals 
Ph(s e h,u, a 
e) = 
{ 1{sph+1} h = h(ℓ) for some ℓ ∈ [L− 1] 
1{seh+1,u} otherwise (3) 
and 
Ph(s e h,u, a) = 1{seh+1,u}, ∀a ∈ A\{ae}. (4) 
That is, the element state seh,u always stays on itself, except at the end of each layer ℓ ∈ [L], it can go to the pivotal state. 
At the end of the first phase, the transition of element state is determined by the set C. In the initialization stage (t = 0), let C0 ⊆ [m] be an arbitrary set of size c and it would be replace later, let 
PH/2(s e H/2,u, a 
e) = 
{ 1{stH/2+1,1} u ∈ C0 
1{stH/2+1,2} u /∈ C0 
7
PENG PAPADIMITRIOU 
and PH/2(s 
e H/2,u, a) = 1{stH/2+1,2}, ∀a ∈ A\{ae}. 
That is, if the element u ∈ C0, then it can go to a high reward terminal state stH/2+1,1; otherwise it goes to the no-reward terminal stH/2+1,2. Looking ahead, we would update the state-action pairs {(seH/2,u, a 
e)}u∈[m] according to sets {Ci}i∈[n] periodically. (c) Set states. The transition function of set states is determined by the sets {Bk,ν}k∈[K],ν∈[N ]. 
In the initialization stage (t = 0), let {B0,ν}ν∈[N ] be arbitrary sets of size b and they would be replaced later in the update sequence. Recall that a set state would appear at the second last step of a groupHℓ,g, for some layer ℓ ∈ [L] and group g ∈ [G]. Let 
N(g, i, j) := (g − 1)(S/4)(A/2) + (i− 1)(A/2) + j, 
and therefore, {N(g, i, j) : g ∈ [G], i ∈ [S/4], j ∈ [A/2]} = [N ]. 
The transition function of state-action pair (sbh(ℓ,g)−1,i, a b j ) equals 
Ph(ℓ,g)−1(s b h(ℓ,g)−1,i, a 
b j ) = unif(seh(ℓ,g),u : u ∈ B0,N(g,i,j)) ∀g ∈ [G], i ∈ [S/4], j ∈ [A/2]. (5) 
Here the RHS is the uniform distribution over the element states seh(ℓ,g),u for element u ∈ B0,N(g,i,j). For the rest of actions, it goes to the no-reward terminal sth(ℓ,g),2: 
Ph(ℓ,g)−1(s b h(ℓ,g)−1,i, a) = 1{sth(ℓ,g),2} ∀a ∈ A\{a 
e j}j∈[A/2] 
(d) Pivotal states. The pivotal state sph appears at every step h ∈ H1, and for h < H/2− 1, the transition function equals 
Ph(s p h, a) = 
{ 1{srh+1,1} a = ap, h = h(ℓ, g, 1) for some ℓ ∈ [L], g ∈ [G] 
1{sph+1} otherwise (6) 
That is, the pivotal state stays on itself, except at the first step ofHℓ,g, it could go to the routing state srh(ℓ,g,2),1. 
At the H/2-th step, it goes to the no-reward terminal stH/2+1,2, 
PH/2(s p H/2, a) = 1{stH/2+1,2} ∀a ∈ A. 
(e) Routing states. Recall {srh(ℓ,g,τ),α}α∈[1:2τ−2] is the collection of routing states at the α-th step (α ∈ [2 : log2(S)]), g-th group (g ∈ [G]) and ℓ-th layer (ℓ ∈ [L]). 
When τ ∈ [2 : log2(S)− 1], the transition function equals 
Ph(ℓ,g,τ)(s r h(ℓ,g,τ),α, a) = 
 1{srh(ℓ,g,τ+1),2α−1} a = ar1 1{srh(ℓ,g,τ+1),2α} a = ar2 1{sth(ℓ,g,τ+1),2} otherwise 
, ∀α ∈ [2τ−2]. (7) 
In other words, the routing state srh(ℓ,g,τ),α goes to either srh(ℓ,g,τ+1),2α−1 or srh(ℓ,g,τ+1),2α−1, depending on the choice of actions (unless it goes to the no-reward terminal srh(ℓ,g,τ+1),2). 
8
NON-STATIONARY REINFORCEMENT LEARNING 
When τ = log2(S), the routing state srh(ℓ,g,log2(S)),α goes to the set state sbh(ℓ,g)−1,α (α ∈ [S/4]), that is, 
Ph(ℓ,g,log2(S)) (srh(ℓ,g,log2(S)),α, a) = sbh(ℓ,g)−1,α, ∀α ∈ [S/4], a ∈ A. (8) 
The entire transition of routing states within a group works like a binary search tree: it comes from the pivotal state and goes to one of the set states. We note that if S ≤ A the construction could be simplified: we can remove routing states and have a pivotal state directly go to set states. This completes the description of the initial MDP. 
Update sequence. We next specify the sequence of updates to the MDP. The sequence of updates is divided into K = n/N stages, and each stage contains n-epochs. 
At the beginning of each stage, the update occurs on the state-action pairs for set-states: 
{(sbh(ℓ,g)−1,i, a b j )}ℓ∈[L],g∈[G],i∈[S/4],j∈[A/2] 
Concretely, there is an initialization phase at the beginning of the k-th stage (k ∈ [K]). Let t(k) ∈ [T ] be the end of initiazation phase, and the nature sets 
Pt(k),h(ℓ,g)−1(s b h(ℓ,g)−1,i, a 
b j ) = unif(seh(ℓ,g),u : u ∈ Bk,N(g,i,j)) ∀ℓ ∈ [L], g ∈ [G], i ∈ [S/4], j ∈ [A/2]. 
Each stage contains n-epochs, and during each epoch, the update occurs on the state-action pairs {(seH/2,u, a 
e)}u∈[m] of element state-action, in the H/2-th step. Let t(k, τ) ∈ [T ] be the end of k-th (k ∈ [K]) stage and τ -th (τ ∈ [n]) epoch. In the τ -th epoch (τ ∈ [n]), for each element u ∈ [m], the transition function is updated to 
Pt(k,τ),H/2(s e H/2,u, a 
e) = 
{ 1{stH/2+1,1} u ∈ Cτ 
1{stH/2+1,2} u /∈ Cτ . (9) 
To count the total number of updates, there are K = n/N stages. The initialization takes at most O(SAHm) updates; there are n epochs, and each epoch contains at most 2m updates. Hence the total number of updates equals (n/N) ·O(SAHm+ 2mn) ≈ T . 
3.2. Analysis 
We now proceed to prove Theorem 1. For any stage k ∈ [K] and epoch τ ∈ [n], we compute the V -value of the optimal policy. The proof can be found at the Appendix B 
Lemma 6 (V -value, terminal states) At the end of stage k ∈ [K] and epoch t ∈ [n], for any step h ∈ [H], the V -value of optimal policy at terminal states satisfies V ∗ 
t(k,τ),h(s t h,1) = min{H + 1 − 
h,H/2} and V ∗ t(k,τ),h(s 
t h,2) = 0. 
Lemma 7 (V -value, element states) At the end of stage k ∈ [K] and epoch τ ∈ [n], for any layer ℓ ∈ [L] and any step h ∈ H1,ℓ 
 For any element u ∈ Cτ , V ∗ t(k,τ),h(s 
e h,u) = H/2; and 
 For any element u /∈ Cτ , we have V ∗ t(k,τ),h(s 
e h,u) = V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1). 
9
PENG PAPADIMITRIOU 
Here we take Vt(k,τ),H/2+1(s p H/2+1) := 0. 
Lemma 8 (V -value, set states) At the end of stage k ∈ [K] and epoch τ ∈ [n], for each level ℓ ∈ [L], group g ∈ [G], we have 
V ∗ t(k,τ),h(ℓ,g)−1(s 
b h(ℓ,g)−1,i) 
= max j∈[A/2] 
{ |Cτ ∩Bk,N(g,i,j)| b 
· H 2 
+ 
( 1− |Cτ ∩Bk,N(g,i,j)| 
b 
) · V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1) 
} Lemma 9 (V -value, pivotal state) At the end of stage k ∈ [K] and epoch τ ∈ [n], for each level ℓ ∈ [L], the V -value of the pivotal state satisfies 
V ∗ t(k,τ),h(ℓ−1)+1(s 
p h(ℓ−1)+1) 
= max ν∈[N ] 
{ |Cτ ∩Bk,ν | 
b · H 2 
+ 
( 1− |Cτ ∩Bk,ν | 
b 
) · V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1) 
} . 
As a corollary, we can compute the V -value of the initial state. 
Lemma 10 (V -value, initial state) Let κk,τ = maxν∈[N ] |Cτ∩Bk,ν | 
b , then at the end of stage k and epoch τ ∈ [n], one has 
V ∗ t(k,τ),1(sinit) = (1− (1− κk,τ ) 
L) · H 2 . 
Now we can complete the proof of Theorem 1 Proof [Proof of Theorem 1] If the input of MAX-IP is a YES instance, suppose Cτ ⊆ Bk,ν for some τ ∈ [n], k ∈ [K], ν ∈ [N ]; then κk,τ = c/b = 1/L. By Lemma 10, the value of sinit at the end of epoch t satisfies 
V ∗ t(k,τ),1(sinit) = (1− (1− κk,τ ) 
L) · H 2 
= (1− (1− 1/L)L) · H 2 ≥ H 
4 . 
In the NO instance case, we have 
κk,τ ≤ c/wb where w = 2log(n) 1−o(1) 
= Ω(1), 
then the value of sinit at the end of any stage k ∈ [K], epoch τ ∈ [n] is at most 
V ∗ t(k,τ),1(sinit) = (1− (1− κk,τ ) 
L) ·H/2 ≤ (1− (1− 1/wL)L) · H 2 ≤ 1 
w · H 2 ≤ H 
100 . 
Now we bound the amortized runtime. By Theorem 5, assuming SETH, the total runtime of any NSRL algorithm should be at least n2−o(1), and therefore, the amortized runtime per update should be at least n2−o(1)/T = (SAH)1−o(1) · T−o(1) ≈ (SAH)1−o(1) when T = poly(SAH). This completes the proof. 
Finally, we leave remarks on the generality of our hardness results. 
Remark 11 (Hardness for maintaining value functions or policies) The statement of Theorem 1 asserts the decision version of NSRL requires (SAH)1−o(1) time per update. The same lower bound translates directly to the task of maintaining an approximate V -value or maintaining an approximately optimal policy. 
10
NON-STATIONARY REINFORCEMENT LEARNING 
Remark 12 (Hardness for restricted changes) In our construction, we allow the change for both reward and transition kernel, for all states, but indeed, this can be relaxed. For example, similar complexity results follow rather easily if only the reward changes or if only the transition changes. In fact, the lower bound also holds if the changes are restricted to occur on a tiny fraction of the states. 
4. Incremental action changes 
When the MDP changes only through the introduction of new actions, then we can maintain an ϵ-approximation to value with amortized runtime that depends, polynomially, only on H and 1 
ϵ (and not S). 
Theorem 13 (Efficient algorithm, incremental changes) There is an algorithm with amortized runtime Õ(H5/ϵ3) per update that maintains an ϵ-approximation of the value over any sequence of T insertions of actions. 
The approach is given as Algorithm 1. It combines the classic Q-value iteration with lazy updates on V -value. For each new state-action pair (sh, ah), it constructs the empirical transition kernel using samples from Ph(sh, ah). The newly added action could potentially affect the state value, and our algorithm propagates the change — lazily — to downstream states. That is, a change to V -value is triggered only if it significantly exceeds the previous estimate. The key mathematical intuition is the monotonicity of V -value under incremental action changes. The amortized runtime of Algorithm 1 is bounded because the Q-value of each state-action is updated rarely, at most Õ(H3/ϵ2 ·H2/ϵ) = Õ(H5/ϵ3) times, due to the sparsity of the empirical transition kernel and the lazy updates. The correctness of our algorithm follows from the standard Bernstein type bound and a robust analysis of Q-value iteration. The detailed proof can be found at Appendix C. 
Algorithm 1 Lazy updated Q-value iteration (Lazy-QVI) 
1: Initialize N ← H3 log3(SHT )/ϵ2, V̂h(sh)← 0, Ṽh(sh)← 0, ∀sh ∈ Sh, h ∈ [H] 2: procedure INSERT(sh, ah) 3: Generate N samples {ŝh+1,1, . . . , ŝh+1,N} from Ph(sh, ah) and reward rh(sh, ah) 
4: P̂h(sh, ah)← unif{ŝh+1,1, . . . , ŝh+1,N} 5: Call PROPAGATE 
6: end procedure 7: procedure PROPAGATE 
8: for h = H,H − 1, . . . , 1 do 9: for state-action pair (sh, ah) ∈ Sh ×Ah do ▷ Update only if there is a change 
10: Q̂h(sh, ah)← rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
Ṽh+1(sh+1) 
11: V̂h(sh)← maxah Q̂(sh, ah) 
12: If Ṽh(sh) ≤ V̂h(sh)− ϵ/4H then Ṽh(sh)← V̂h(sh) 13: end for 14: end for 15: end procedure 
Theorem 13 provides an efficient algorithm for approximately optimal policy, one natural question is whether one can maintain the exact optimal policy (or value function) under incremental 
11
PENG PAPADIMITRIOU 
action changes. We give a negative answer, showing that T 1−o(1) runtime is necessary if one wants to maintain an O(1/T )-approximation to the value of optimal policy. 
Theorem 14 (Lower bound, exact optimal policy) Unless SETH is false, there is a sequence of T action insertions such that no algorithm with amortized runtime T 1−o(1) per update can maintain an O(1/T )-approximation to the value of optimal policy. 
5. Discussion 
Ideally, a complexity result should give some hints on the kind of new algorithms that will bypass it. Our result seems to suggest that a successful heuristic approach to NSRL may be one that alternates between additional exploration after each change in parameters and, when this brings diminishing benefits, a restart from scratch. This is not unlike some of the approaches taken by some state-of-the-art applications (Padakandla, 2021). By further developing this and similar approaches, the current challenge of NSRL may be eventually tamed. We also note that our negative result leaves open the NSRL problem in the case of function approximation (Jin et al., 2020; Agarwal et al., 2019); we conjecture that a similar negative result can be proved for this case as well. 
Acknowledgments 
The research is supported by NSF CCF-1703925, IIS-1838154, CCF-2106429, CCF-2107187, CCF-1763970, AF2212233, COLL2134095, COLL2212745 
References 
Amir Abboud and Virginia Vassilevska Williams. Popular conjectures imply strong lower bounds for dynamic problems. In 2014 IEEE 55th Annual Symposium on Foundations of Computer Science, pages 434–443. IEEE, 2014. 
Amir Abboud, Aviad Rubinstein, and Ryan Williams. Distributed pcp theorems for hardness of approximation in p. In 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS), pages 25–36. IEEE, 2017. 
Amir Abboud, Raghavendra Addanki, Fabrizio Grandoni, Debmalya Panigrahi, and Barna Saha. Dynamic set cover: improved algorithms and lower bounds. In Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, pages 114–125, 2019. 
Alekh Agarwal, Nan Jiang, Sham M Kakade, and Wen Sun. Reinforcement learning: Theory and algorithms. CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep, pages 10–4, 2019. 
Josh Alman, Timothy Chu, Aaron Schild, and Zhao Song. Algorithms and hardness for linear algebra on geometric graphs. In 2020 IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS), pages 541–552. IEEE, 2020. 
Sanjeev Arora and Boaz Barak. Computational complexity: a modern approach. Cambridge Uni-versity Press, 2009. 
12
NON-STATIONARY REINFORCEMENT LEARNING 
Peter Auer, Thomas Jaksch, and Ronald Ortner. Near-optimal regret bounds for reinforcement learning. Advances in neural information processing systems, 21, 2008. 
Mohammad Azar, Rémi Munos, and Hilbert J Kappen. Minimax pac bounds on the sample complexity of reinforcement learning with a generative model. Machine learning, 91:325–349, 2013. 
Arturs Backurs and Piotr Indyk. Edit distance cannot be computed in strongly subquadratic time (unless seth is false). In Proceedings of the forty-seventh annual ACM symposium on Theory of computing, pages 51–58, 2015. 
Arturs Backurs, Liam Roditty, Gilad Segal, Virginia Vassilevska Williams, and Nicole Wein. To-wards tight approximation bounds for graph diameter and eccentricities. In Proceedings of the 50th Annual ACM SIGACT Symposium on Theory of Computing, pages 267–280, 2018. 
Taposh Banerjee, Miao Liu, and Jonathan P How. Quickest change detection approach to optimal control in markov decision processes with model changes. In 2017 American control conference (ACC), pages 399–405. IEEE, 2017. 
Richard E Bellman. Dynamic programming. Princeton university press, 1957. 
Dimitri Bertsekas. Dynamic programming and optimal control: Volume I, volume 1. Athena scientific, 2012. 
Moses Charikar and Paris Siminelakis. Hashing-based-estimators for kernel density in high dimensions. In 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS), pages 1032–1043. IEEE, 2017. 
Lijie Chen. On the hardness of approximate and exact (bichromatic) maximum inner product. Theory of Computing, 16(4):1–50, 2020. 
Xi Chen, Christos Papadimitriou, and Binghui Peng. Memory bounds for continual learning. In 2022 IEEE 63th Annual Symposium on Foundations of Computer Science (FOCS), 2022. 
Wang Chi Cheung, David Simchi-Levi, and Ruihao Zhu. Reinforcement learning for non-stationary markov decision processes: The blessing of (more) optimism. In International Conference on Machine Learning, pages 1843–1854. PMLR, 2020. 
Bruno C Da Silva, Eduardo W Basso, Ana LC Bazzan, and Paulo M Engel. Dealing with nonstationary environments using context detection. In Proceedings of the 23rd international conference on Machine learning, pages 217–224, 2006. 
Mina Dalirrooyfard, Ray Li, and Virginia Vassilevska Williams. Hardness of approximate diameter: Now for undirected graphs. In 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS), pages 1021–1032. IEEE, 2022. 
Travis Dick, Andras Gyorgy, and Csaba Szepesvari. Online learning in markov decision processes with changing cost sequences. In International Conference on Machine Learning, pages 512– 520. PMLR, 2014. 
13
PENG PAPADIMITRIOU 
Omar Darwiche Domingues, Pierre Ménard, Matteo Pirotta, Emilie Kaufmann, and Michal Valko. A kernel-based approach to non-stationary reinforcement learning in metric spaces. In Interna-tional Conference on Artificial Intelligence and Statistics, pages 3538–3546. PMLR, 2021. 
Songtao Feng, Ming Yin, Ruiquan Huang, Yu-Xiang Wang, Jing Yang, and Yingbin Liang. Non-stationary reinforcement learning under general function approximation. arXiv preprint arXiv:2306.00861, 2023. 
Dylan J Foster, Sham M Kakade, Jian Qian, and Alexander Rakhlin. The statistical complexity of interactive decision making. arXiv preprint arXiv:2112.13487, 2021. 
Ronald A Howard. Dynamic programming and markov processes. 1960. 
Russell Impagliazzo and Ramamohan Paturi. On the complexity of k-sat. Journal of Computer and System Sciences, 62(2):367–375, 2001. 
Haozhe Jiang, Qiwen Cui, Zhihan Xiong, Maryam Fazel, and Simon S Du. A black-box approach for non-stationary multi-agent reinforcement learning. arXiv preprint arXiv:2306.07465, 2023. 
Chi Jin, Zeyuan Allen-Zhu, Sebastien Bubeck, and Michael I Jordan. Is q-learning provably efficient? Advances in neural information processing systems, 31, 2018. 
Chi Jin, Zhuoran Yang, Zhaoran Wang, and Michael I Jordan. Provably efficient reinforcement learning with linear function approximation. In Conference on Learning Theory, pages 2137– 2143. PMLR, 2020. 
Khimya Khetarpal, Matthew Riemer, Irina Rish, and Doina Precup. Towards continual reinforcement learning: A review and perspectives. Journal of Artificial Intelligence Research, 75:1401– 1476, 2022. 
Yin Tat Lee and Aaron Sidford. Path finding methods for linear programming: Solving linear programs in o( 
√ rank) iterations and faster algorithms for maximum flow. In 2014 IEEE 55th 
Annual Symposium on Foundations of Computer Science, pages 424–433. IEEE, 2014. 
Gen Li, Yuting Wei, Yuejie Chi, Yuantao Gu, and Yuxin Chen. Breaking the sample size barrier in model-based reinforcement learning with a generative model. Advances in neural information processing systems, 33:12861–12872, 2020. 
Ray Li. Settling seth vs. approximate sparse directed unweighted diameter (up to (nu) nseth). In Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing, pages 1684– 1696, 2021. 
Yingying Li and Na Li. Online learning for markov decision processes in nonstationary environments: A dynamic regret analysis. In 2019 American Control Conference (ACC), pages 1232– 1237. IEEE, 2019. 
ML Littman. On the complexity of solving markov decision problems. Proceedings of the 11th International Comference on Uncertainty in Artificial Intelligence, 1995. 
14
NON-STATIONARY REINFORCEMENT LEARNING 
Weichao Mao, Kaiqing Zhang, Ruihao Zhu, David Simchi-Levi, and Tamer Basar. Near-optimal model-free reinforcement learning in non-stationary episodic mdps. In International Conference on Machine Learning, pages 7447–7458. PMLR, 2021. 
Melkior Ornik and Ufuk Topcu. Learning and planning for time-varying mdps using maximum likelihood estimation. The Journal of Machine Learning Research, 22(1):1656–1695, 2021. 
Ronald Ortner, Pratik Gajane, and Peter Auer. Variational regret bounds for reinforcement learning. In Uncertainty in Artificial Intelligence, pages 81–90. PMLR, 2020. 
Sindhu Padakandla. A survey of reinforcement learning algorithms for dynamically varying environments. ACM Computing Surveys (CSUR), 54(6):1–25, 2021. 
Sindhu Padakandla, Prabuchandran KJ, and Shalabh Bhatnagar. Reinforcement learning algorithm for non-stationary environments. Applied Intelligence, 50:3590–3606, 2020. 
Christos H Papadimitriou. Computational complexity. In Encyclopedia of computer science, pages 260–265. 2003. 
Christos H Papadimitriou and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998. 
Christos H Papadimitriou and John N Tsitsiklis. The complexity of markov decision processes. Mathematics of operations research, 12(3):441–450, 1987. 
Binghui Peng. Dynamic influence maximization. Advances in Neural Information Processing Sys-tems, 34:10718–10731, 2021. 
Martin L Puterman. Markov decision processes: discrete stochastic dynamic programming. John Wiley & Sons, 2014. 
Liam Roditty and Virginia Vassilevska Williams. Fast approximation algorithms for the diameter and radius of sparse graphs. In Proceedings of the forty-fifth annual ACM symposium on Theory of computing, pages 515–524, 2013. 
Aviad Rubinstein. Hardness of approximate nearest neighbor search. In Proceedings of the 50th annual ACM SIGACT symposium on theory of computing, pages 1260–1268, 2018. 
Aviad Rubinstein and Virginia Vassilevska Williams. Seth vs approximation. ACM SIGACT News, 50(4):57–76, 2019. 
Bruno Scherrer. Improved and generalized upper bounds on the complexity of policy iteration. Advances in Neural Information Processing Systems, 26, 2013. 
Aaron Sidford, Mengdi Wang, Xian Wu, Lin Yang, and Yinyu Ye. Near-optimal time and sample complexities for solving markov decision processes with a generative model. Advances in Neural Information Processing Systems, 31, 2018a. 
Aaron Sidford, Mengdi Wang, Xian Wu, and Yinyu Ye. Variance reduced value iteration and faster algorithms for solving markov decision processes. In Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 770–787. SIAM, 2018b. 
15
PENG PAPADIMITRIOU 
Aaron Sidford, Mengdi Wang, Lin Yang, and Yinyu Ye. Solving discounted stochastic two-player games with near-optimal time and sample complexity. In International Conference on Artificial Intelligence and Statistics, pages 2992–3002. PMLR, 2020. 
David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al. Mastering the game of go without human knowledge. nature, 550(7676):354–359, 2017. 
David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, et al. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. Science, 362(6419):1140– 1144, 2018. 
Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
Ahmed Touati and Pascal Vincent. Efficient learning in non-stationary linear markov decision processes. arXiv preprint arXiv:2010.12870, 2020. 
Paul Tseng. Solving h-horizon, stationary markov decision problems in time proportional to log (h). Operations Research Letters, 9(5):287–297, 1990. 
Jan Van Den Brand, Yin Tat Lee, Yang P Liu, Thatchaphol Saranurak, Aaron Sidford, Zhao Song, and Di Wang. Minimum cost flows, mdps, and ℓ1-regression in nearly linear time for dense instances. In Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing, pages 859–869, 2021. 
Chen-Yu Wei and Haipeng Luo. Non-stationary reinforcement learning without prior knowledge: An optimal black-box approach. In Conference on Learning Theory, pages 4300–4354. PMLR, 2021. 
Virginia Vassilevska Williams. On some fine-grained questions in algorithms and complexity. In Proceedings of the international congress of mathematicians: Rio de janeiro 2018, pages 3447– 3487. World Scientific, 2018. 
Yinyu Ye. A new complexity result on solving the markov decision problem. Mathematics of Operations Research, 30(3):733–749, 2005. 
Yinyu Ye. The simplex and policy-iteration methods are strongly polynomial for the markov decision problem with a fixed discount rate. Mathematics of Operations Research, 36(4):593–603, 2011. 
Huozhi Zhou, Jinglin Chen, Lav R Varshney, and Ashish Jagmohan. Nonstationary reinforcement learning with linear function approximation. Transactions on Machine Learning Research, 2022. 
16
NON-STATIONARY REINFORCEMENT LEARNING 
Appendix A. Additional related work 
Computational complexity of reinforcement learning The computational complexity of (stationary) MDP has been a central topic across multiple disciplines. The study of MDP dates back to Bellman (1957) in 1950s, and since then, there is a long line of work concerning the computational efficiency of MDP (Tseng, 1990; Littman, 1995; Howard, 1960; Ye, 2011; Scherrer, 2013; Ye, 2005; Sidford et al., 2018b,a, 2020; Lee and Sidford, 2014; Van Den Brand et al., 2021; Papadim-itriou and Tsitsiklis, 1987). The classical approaches include value iteration, policy iteration and linear programming, see Puterman (2014); Bertsekas (2012) for reference. For a finite horizontal MDP with S states, A actions and H steps, the value iteration could return the optimal policy with runtime O(S2AH) that is linear in the input size. If the algorithm could sample from the transition function (a.k.a. the generative model), then Azar et al. (2013) provide an algorithm that returns an ϵ-approximation to the V -value with runtime Õ(SAH3/ϵ2). For non-stationary MDP, it implies an algorithm with runtime Õ(S2AH + SAH3T/ϵ2) for ϵ-value approximation over a sequence of T updates. This is because the algorithm could always re-compute from scratch, and it can sample the transition function in O(log(S)) time using a binary tree data structure, after reading the input initially. 
Besides computation complexity, a large number of work concern about the sample complexity in generative model (e.g. Azar et al. (2013); Li et al. (2020)) and regret in model-free RL (e.g. Jin et al. (2018)), in tabular setting as well as functional approximation setting (Foster et al., 2021). 
Appendix B. Missing proof from Section 3 
Proof [Proof of Lemma 6] This is quite obvious, as the terminal state always stays on itself (Eq. (2)), the reward of sth,2 is always 0, while the reward of sth,1 is 0 in phase one and 1 in phase two (Eq. (1)). 
Proof [Proof of Lemma 7] For an element u ∈ Cτ , a policy could choose to never leave seu (Eq. (3)), and it receives the maximum H/2 reward (see Eq. (9)(1)). For an element u /∈ Cτ , the policy needs to stay at seu until the end of layer ℓ (see Eq. (3)). While at the end of layer ℓ, it could move to pivotal state sph(ℓ)+1 or stay on itself (Eq. (4)). The later obtains strictly less reward, because the pivotal state could always stay on itself (Eq. (6)), and the value V ∗ 
t(k,τ),H/2(s e H/2,u) = 0 at the end 
of phase 1 (see Eq. (9)(1)). This completes the proof. 
Proof [Proof of Lemma 8] The Q-value of choosing action abj (j ∈ [A/2]) equals 
Q∗ t(k,τ),h(ℓ,g)−1(s 
b h(ℓ,g)−1,i, a 
b j ) 
= ∑ u∈[m] 
Pr[sh(ℓ,g) = seh(ℓ,g),u] · V ∗ t(k,τ),h(ℓ,g)(s 
b h(ℓ,g),u) 
= ∑ u∈Cτ 
Pr[sh(ℓ,g) = seh(ℓ,g),u] · H 
2 + 
∑ u∈[m]\Cτ 
Pr[sh(ℓ,g) = seh(ℓ,g),u] · V ∗ t(k,τ),h(ℓ)+1(s 
p h(ℓ)+1) 
= |Cτ ∩Bk,N(g,i,j)| 
b · H 2 
+ 
( 1− |Cτ ∩Bk,N(g,i,j)| 
b 
) · V ∗ 
t(k,τ),ℓ+1(s p h(ℓ)+1). 
17
PENG PAPADIMITRIOU 
The first step follows from Bellman’s equation and the state-action pair (sbh(ℓ,g)−1,i, a b j ) receives 0 
reward (Eq. (1)), the second step follows from Lemma 7, the last step follows from Eq. (5). The proof follows by taking the maximum over action {abj}j∈[A/2]. 
Proof [Proof of Lemma 9] For each level ℓ ∈ [L], the transition functions of the pivotal state and routing states guarantee that a policy can visit exactly one set state in Hℓ. To see this, it can visit at most one set state because the element state stays on itself till the end of the layer (Eq. (3)). Meanwhile, it can go to any set state ν ∈ [N ] with ν = N(g, i, j) for some i ∈ [S/2] and g ∈ [G], because it can first go to the pivotal state sph(ℓ,g−1)+1,0 at the beginning of group g, then move to srh(ℓ,g)−1,i through routing states (see Eq. (7)(8)). Combining Lemma 8, we have 
V ∗ t(k,τ),h(ℓ−1)+1(s 
p h(ℓ−1)+1) 
= max g∈[G] 
max i∈[S/4] 
V ∗ t(k,τ),h(ℓ,g)−1(s 
b h(ℓ,g)−1,i) 
= max g∈[G] 
max i∈[S/4] 
max j∈[A/2] 
{ |Cτ ∩Bk,N(g,i,j)| b 
· H 2 
+ 
( 1− |Cτ ∩Bk,N(g,i,j)| 
b 
) · V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1) 
} = max 
ν∈[N ] 
{ |Cτ ∩Bk,ν | 
b · H 2 
+ 
( 1− |Cτ ∩Bk,ν | 
b 
) · V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1) 
} . 
This completes the proof of the lemma. 
Proof [Proof of Lemma 10] By Lemma 9, for any ℓ ∈ [L], we have 
V ∗ t(k,τ),h(ℓ−1)+1(s 
p h(ℓ−1)+1) 
= max ν∈[N ] 
{ |Cτ ∩Bk,ν | 
b · H 2 
+ 
( 1− |Cτ ∩Bk,ν | 
b 
) · V ∗ 
t(k,τ),h(ℓ)+1(s p h(ℓ)+1) 
} = κk,τ · 
H 
2 + (1− κk,τ )V 
∗ t(k,τ),h(ℓ)+1(s 
p h(ℓ)+1). 
Solving the above recursion, one has 
V ∗ t(k,τ),1(sinit) = V ∗ 
t(k,τ),1(s p 1) = 
L∑ ℓ=1 
κk,τ (1− κk,τ ) ℓ−1 · H 
2 = (1− (1− κk,τ ) 
L) · H 2 . 
This completes the proof of the lemma. 
Appendix C. Missing proof from Section 4 
We first state the concentration bounds used in the paper. 
Lemma 15 (Hoeffding bound) Let X1, · · · , Xn be n independent bounded variables in [ai, bi]. Let X = 
∑n i=1Xi, then we have 
Pr[|X − E[X]| ≥ t] ≤ 2 exp 
( − 2t2∑n 
i=1(bi − ai)2 
) . 
18
NON-STATIONARY REINFORCEMENT LEARNING 
Lemma 16 (Bernstein bound) Let X1, · · · , Xn be n independent zero mean random variables and |Xi| ≤M . Let X = 
∑n i=1Xi, σ = 
∑n i=1 E[X2 
i ] then we have 
Pr[|X| ≥ t] ≤ 2 exp 
( − 2t2 
Mt/3 + σ2 
) . 
In particular, with probability at least 1− δ, one has 
|X| ≤ (M/3 + σ) · log(1/δ). 
We prove Algorithm 1 gives ϵ-approximation to both V -value and Q-value. For notation convenience, we drop the subscript of round number t in the proof. 
Lemma 17 (Value approximation) At the end of t-th update (t ∈ [T ]), for any step h ∈ [H], state sh ∈ Sh and action ah, with probability at least 1− (SHT )−ω(1), we have 
|V ∗ h (sh)− V̂h(sh)| ≤ ϵ/2 and |Q∗ 
h(sh, ah)− Q̂h(sh, ah)| ≤ ϵ 
Proof We prove the claim by induction. The base case of h = H holds trivially, as there is no error. Suppose the claim holds up to step h+ 1, then for the h-th step, we have 
Q̂h(sh, ah) = rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
Ṽh+1(sh+1) 
= rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
V̂h+1(sh+1)± ϵ 
4H 
= rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
[V ∗ h+1(sh+1)] 
+ E sh+1∼P̂h(sh,ah) 
[V̂h+1(sh+1)− V ∗ h+1(sh+1)]± 
ϵ 
4H , (10) 
where the first step follows from the update rule of Algorithm 1, the second step holds since that the propagate value Ṽh+1(sh+1) satisfies∣∣∣V̂h+1(sh+1)− Ṽh+1(sh+1) 
∣∣∣ ≤ ϵ 
4H , ∀sh+1 ∈ Sh+1. 
We bound the second term of Eq. (10) in terms of variance. Define 
σh(sh, ah) 2 := E 
sh+1∼Ph(sh,ah) [V ∗ 
h+1(sh+1) 2]− 
( E 
sh+1∼Ph(sh,ah) [V ∗ 
h+1(sh+1)] 
)2 
. 
By Bernstein inequality, we have with probability at least 1− (SHT )−ω(1),∣∣∣∣∣ E sh+1∼P̂h(sh,ah) 
[V ∗ h+1(sh+1)]− E 
sh+1∼Ph(sh,ah) [V ∗ 
h+1(sh+1)] 
∣∣∣∣∣ ≲ H + √ Nσh(sh, ah) 
N · log(SHT ) 
≤ ϵ2 
H2 + 
ϵ 
16H3/2 · σh(sh, ah). 
19
PENG PAPADIMITRIOU 
Plugging into Eq. (10), we have 
Q̂h(sh, ah) 
= rh(sh, ah) + E sh+1∼Ph(sh,ah) 
[V ∗ h+1(sh+1)] + E 
sh+1∼P̂h(sh,ah) [V̂h+1(sh+1)− V ∗ 
h+1(sh+1)] 
± ϵ 
16H3/2 · σh(sh, ah)± 
ϵ 
3H 
= Q∗ h(sh, ah) + E 
sh+1∼P̂h(sh,ah) [V̂h+1(sh+1)− V ∗ 
h+1(sh+1)]± ϵ 
16H3/2 · σh(sh, ah)± 
ϵ 
3H . (11) 
We bound the V -value difference V̂h(sh) − V ∗ h (sh) and provide upper and lower bounds sepa-
rately. Upper bound V̂h(sh)−V ∗ 
h (sh). Let π̂ be the policy induced by Q̂, that is, for any state sℓ ∈ Sℓ, π̂(sℓ) = argmaxaℓQ̂ℓ(sℓ, aℓ). Then for any state sh ∈ Sh, one has 
V̂h(sh)− V ∗ h (sh) 
= Q̂h(sh, π̂(sh))−Q∗ h(sh, π 
∗(sh)) 
= Q̂h(sh, π̂(sh))−Q∗ h(sh, π̂(sh)) +Q∗ 
h(sh, π̂(sh))−Q∗ h(sh, π 
∗(sh)) 
≤ Q̂h(sh, π̂(sh))−Q∗ h(sh, π̂(sh)) 
≤ E sh+1∼P̂h(sh,π̂(sh)) 
[V̂h+1(sh+1)− V ∗ h+1(sh+1)]± 
ϵ 
16H3/2 σh(sh, π̂(sh)) + 
ϵ 
3H , (12) 
where the third step follows from the optimality of π∗, the fourth step follows from Eq. (11). Fix the state sh ∈ Sh, for any step ℓ ∈ [h : H] and state sℓ ∈ Sℓ, let p̂(sℓ) be the probability 
that policy π̂ goes to state sℓ, starting from sh. Recurring Eq. (12), we obtain 
V̂h(sh)− V ∗ h (sh) ≤ 
ϵ 
16H3/2 · 
H∑ ℓ=h 
∑ sℓ∈Sℓ 
p̂(sℓ)σℓ(sℓ, π̂(sℓ)) + ϵ 
3 
≤ ϵ 
16H 
√√√√ H∑ ℓ=h 
p̂(sℓ)σℓ(sℓ, π̂(sℓ))2 + ϵ 
3 . (13) 
Here the first step follows Eq. (12), the second step follows from Cauchy Schwarz inequality and∑ sℓ∈Sℓ 
p̂(sℓ) = 1 holds for any ℓ ≥ h. We need the following two technical Lemmas. 
Lemma 18 (Connection with empirical variance) Define the empirical variance 
σ̂h(sh, ah) 2 := E 
sh+1∼P̂h(sh,ah) [V̂h+1(sh+1) 
2]− 
( E 
sh+1∼P̂h(sh,ah) [V̂h+1(sh+1)] 
)2 
Then with probability at least 1− (SHT )−ω(1), one has 
|σh(sh, ah)2 − σ̂h(sh, ah) 2| ≤ H. 
20
NON-STATIONARY REINFORCEMENT LEARNING 
Proof First, by Hoeffding inequality, with probability at least 1− (SHT )−ω(1), one has∣∣∣∣∣ E sh+1∼P̂h(sh,ah) 
[V̂h+1(sh+1) 2]− E 
sh+1∼Ph(sh,ah) [V̂h+1(sh+1) 
2] 
∣∣∣∣∣ ≤ 4H2 √ N log(SHT ) 
N ≤ H/4. 
By induction hypothesis, one has |V̂h+1(sh+1) − Vh+1(sh+1)| ≤ ϵ for any state sh+1 ∈ Sh+1, and therefore, ∣∣∣∣ E 
sh+1∼Ph(sh,ah) [V̂h+1(sh+1) 
2 − Vh+1(sh+1) 2] 
∣∣∣∣ ≤ 2ϵH ≤ H/4 
Similarly, by Hoeffding bound, we have with probability at least 1− (SHT )−ω(1),∣∣∣∣∣ E sh+1∼P̂h(sh,ah) 
[V̂h+1(sh+1)]− E sh+1∼Ph(sh,ah) 
[V̂h+1(sh+1)] 
∣∣∣∣∣ ≤ 4 √ NH log(SHT ) 
N ≤ ϵ 
and by induction hypothesis,∣∣∣∣ E sh+1∼Ph(sh,ah) 
[V̂h+1(sh+1)− Vh+1(sh+1)] 
∣∣∣∣ ≤ ϵ 
Combining the above four inequalities, one can conclude the proof. 
Lemma 19 (Upper bound on empirical variance) We have 
H∑ ℓ=h 
p̂(sℓ)σ̂ℓ(sℓ, π̂(sℓ)) 2 ≤ 3H2 
Proof We have 
H∑ ℓ=h 
∑ sℓ∈Sℓ 
p̂(sℓ)σ̂ℓ(sℓ, π̂(sℓ)) 2 
= 
H∑ ℓ=h 
∑ sℓ∈Sℓ 
p̂(sℓ) · 
 E sℓ+1∼P̂ℓ(sℓ,π̂(sℓ)) 
[V̂ℓ+1(sℓ+1) 2]− 
( E 
sℓ+1∼P̂ℓ(sℓ,π̂(sℓ)) [V̂ℓ+1(sℓ+1)] 
)2  
≤ H∑ 
ℓ=h+1 
∑ sℓ∈Sℓ 
p̂(sℓ) 
V̂ℓ(sℓ) 2 − 
( E 
sℓ+1∼P̂ (sℓ,π̂(sℓ)) [V̂ℓ+1(sℓ+1)] 
)2 + 1 
= 
H∑ ℓ=h+1 
∑ sℓ∈Sℓ 
p̂(sℓ) 
( E sℓ+1∼P̂ (sℓ,π̂(sℓ)) 
[Ṽℓ+1(sℓ+1) + rℓ(sℓ, π̂(sℓ))] 
)2 
− 
( E 
sℓ+1∼P̂ (sℓ,π̂(sℓ)) [V̂ℓ+1(sℓ+1)] 
)2 + 1 
≤ H∑ 
ℓ=h+1 
∑ sℓ∈Sℓ 
p̂(sℓ) · 2H · (1 + ϵ/H) + 1 ≤ 3H2. 
The first step follows from the definition of empirical variance σ̂ℓ. The second step is important and it holds due to the definition of visiting probability p̂ℓ, and we use the naive bound of V̂H(sH) ≤ 1 
21
PENG PAPADIMITRIOU 
for any state sH ∈ SH in last step. The third step holds due to the definition of V̂ℓ(sℓ). The last step holds due to ∣∣∣∣∣ E 
sℓ+1∼P̂ (sℓ,π̂(sℓ)) Ṽℓ+1(sℓ+1) + rℓ(sℓ, π̂(sℓ))− V̂ℓ+1(sℓ+1) 
∣∣∣∣∣ ≤ 1 + ϵ/H 
as |Ṽℓ+1(sℓ+1)− V̂ℓ+1(sℓ+1)| ≤ ϵ/H and rℓ(sℓ, π̂(sℓ)) ≤ 1. 
Combining Lemma 18, Lemma 19 and Eq. (13), we have that 
V̂h(sh)− V ∗ h (sh) ≤ 
ϵ 
16H 
√√√√ H∑ ℓ=h 
p̂(sℓ)σℓ(sℓ, π̂(sℓ))2 + ϵ 
3 
= ϵ 
16H 
√√√√ H∑ ℓ=h 
p̂(sℓ)σ̂ℓ(sℓ, π̂(sℓ))2 +H2 + ϵ 
3 
≤ ϵ 
16H · √ 3H2 +H2 + 
ϵ 
3 ≤ ϵ 
2 (14) 
Lower bound V̂h(sh)− V ∗ h (sh). The proof for lower bound is similar. First, we have 
V ∗ h (sh)− V̂h(sh) 
= Q∗ h(sh, π 
∗(sh))− Q̂h(sh, π̂(sh)) 
= Q∗ h(sh, π 
∗(sh))− Q̂h(sh, π ∗(sh)) + Q̂h(sh, π 
∗(sh))− Q̂h(sh, π̂(sh)) 
≤ Q∗ h(sh, π 
∗(sh))− Q̂h(sh, π ∗(sh)) 
≤ E sh+1∼P̂h(sh,π∗(sh)) 
[V ∗ h+1(sh+1)− V̂h+1(sh+1)] + 
ϵ 
16H3/2 σh(sh, π 
∗(sh)) + ϵ 
3H , (15) 
where the third step follows from the optimality of π̂, the fourth step follows from Eq. (11). Using Hoeffding bound and the induction hypothesis |V ∗ 
h+1(sh+1) − V̂h+1(sh+1)| ≤ ϵ, with probability at least 1− (SHT )−ω(1), we have 
E sh+1∼P̂h(sh,π∗(sh)) 
[V ∗ h+1(sh+1)− V̂h+1(sh+1)]− E 
sh+1∼Ph(sh,π∗(sh)) [V ∗ 
h+1(sh+1)− V̂h+1(sh+1)] 
≤ 2ϵ √ N log(SHT ) 
N ≤ ϵ 
24H . 
Plug into Eq. (15), we have 
V ∗ h (sh)− V̂h(sh) ≤ E 
sh+1∼Ph(sh,π∗(sh)) [V ∗ 
h+1(sh+1)− V̂h+1(sh+1)] 
+ ϵ 
16H3/2 σh(sh, π 
∗(sh)) + 3ϵ 
8H . 
22
NON-STATIONARY REINFORCEMENT LEARNING 
Fix the state sh ∈ Sh, for any step ℓ ∈ [h : H] and state sℓ ∈ Sℓ, let p∗(sℓ) be the probability that policy π∗ goes to state sℓ, starting from sh. Recurring the above equation, we obtain 
V ∗ h (sh)− V̂h(sh) ≤ 
ϵ 
16H3/2 · 
H∑ ℓ=h 
∑ sℓ∈Sℓ 
p∗(sℓ)σℓ(sℓ, π ∗(sℓ)) + 
3ϵ 
8 
≤ ϵ 
16H 
√√√√ H∑ ℓ=h 
p∗(sℓ)σℓ(sℓ, π∗(sℓ))2 + 3ϵ 
8 . 
≤ ϵ 
16H 
√ 3H2 + 
ϵ 
3 ≤ ϵ/2. (16) 
We use Cauchy Schwarz in the second step, the third step follows from the following Lemma (the proof is similar to Lemma 19 and we omit it here). 
Lemma 20 (Upper bound on variance) We have 
H∑ ℓ=h 
p∗(sℓ)σℓ(sℓ, π ∗(sℓ)) 
2 ≤ 3H2. 
Combining Eq. (14) and Eq. (16), we conclude the proof for V -value. For Q-value, we have with probability at least 1− (SHT )−ω(1), 
Q̂h(sh, ah) = rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
Ṽh+1(sh+1) 
= rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
V̂h+1(sh+1)± ϵ 
4H 
= rh(sh, ah) + E sh+1∼P̂h(sh,ah) 
V ∗ h+1(sh+1)± ϵ/2± ϵ 
4H 
= rh(sh, ah) + E sh+1∼Ph(sh,ah) 
V ∗ h+1(sh+1)± ϵ 
= Q∗ h(sh, ah)± ϵ. 
The first step uses the update rule of Algorithm 1, the second step holds since |Ṽh+1(sh+1) − V̂h+1(sh+1)| ≤ ϵ/4H . The third follows from the guarantee of V -value, and the fourth step follows from Hoeffding bounds and the last step follows from Bellman equation. We finish the induction and complete the proof here. 
We next bound the total update time of Algorithm 1. 
Lemma 21 (Total update time) The total update time of Algorithm 1 is at most Õ(TH5/ϵ3) over a sequence of T action insertions. 
Proof For each new action (sh, ah), the construction of P̂h(sh, ah) takes Õ(N) = Õ(H3/ϵ2) time. The major overhead comes from the PROPAGATE part. First, note the propagated V -value Ṽh(sh) of a state sh can change at most H/(ϵ/4H) = O(H2/ϵ) times. Next, for each state-action pair (sh, ah), the Q-value Q̂h(sh, ah) = rh(sh, ah) + E 
sh+1∼P̂h(sh,ah) Ṽh+1(sh+1) can change at most 
23
PENG PAPADIMITRIOU 
O(N ·H2/ϵ) = Õ(H5/ϵ3) times, because the support of P̂h(sh, ah) has size at most N , and each estimate Ṽh+1(sh+1) changes at O(H2/ϵ) times as stated above. The total number of state-action pair is bounded by T . We conclude the proof. 
The proof of Theorem 13 follows directly from Lemma 17 and Lemma 21. We next prove the lower bound. 
Proof [Proof of Theorem 14] Let n = T 1−o(1), m = no(1). We reduce from MAX-IP with sets B1, . . . , Bn and C1, . . . , Cn defined over ground element [m]. The MDP contains H = 3 steps. There is one single initial state s1 at the first step h = 1. In the second step (h = 2), there are m = no(1) states s2,1, . . . , s2,m, and at the last step (h = 3), there are two states s3,1, s3,2. 
The sequence of new actions is as follow. There is one action a3 for the last step, and the reward satisfies r3(s3,1, a3) = 1 and r3(s3,1, a3) = 0, i.e., the reward is 1 for s3,1 and 0 for s3,2. There are n actions a1,1, . . . , a1,n for the initial state at the first step, and we have 
P1(s1, a1,i) = unif({s2,k : k ∈ Bi}) and r1(s1, a1,i) = 0 ∀i ∈ [n]. 
The rest sequence divides into n epochs, and in the j-th epoch (j ∈ [n]), there is one new action a2,j for each state {s2,k}k∈[m]. Let δ = 1/4n. At the end of j-th epoch, t(j) ∈ [T ], the transition and the reward of the new action a2,j satisfies 
P2(sk, a2,j) = 
{ ( j n+1 + δ, 1− j 
n+1 − δ) k ∈ Cj 
( j n+1 , 1− 
j n+1) k /∈ Cj 
and r2(sk, a2,j) = 0. 
In summary, the total number of state-action pairs at the end is 2 + n+mn = n1+o(1) = T . First, a simple observation on the value function 
Lemma 22 At the end of epoch j ∈ [n], the optimal policy satisfies 
 V ∗ t(j)(s3,1) = 1 and V ∗ 
t(j)(s3,1) = 0 
 V ∗ t(j)(s2,k) = 
j n+1 + δ when k ∈ Cj and V ∗ 
t(j)(s2,k) = j 
n+1 otherwise 
 V ∗ t(j)(s1) = 
j n+1 + κj · δ, where κj = maxi∈[n] 
|Cj∩Bi| b 
Proof The first claim is trivial. The second claim holds since the action a2,j is the optimal choice by the end of epoch j, and its value equals Q∗ 
t(j)(s2,k, aj) = j 
n+1+δ when k ∈ Cj and Q∗ t(j)(s2,k, aj) = 
j n+1 when k /∈ Cj . For the last claim, for any i ∈ [n], we have 
Q∗ t(j)(s1, a1,i) = 
∑ k∈[m] 
Pr[s2 = s2,k] · V ∗ t(j)(s2,k) 
= ∑ k∈Cj 
Pr[s2 = s2,k] · V ∗ t(j)(s2,k) + 
∑ k∈[m]\Cj 
Pr[s2 = s2,k] · V ∗ t(j)(s2,k) 
= |Bi ∩ Cj | 
b · ( 
j 
n+ 1 + δ 
) + 
( 1− |Bi ∩ Cj | 
b 
) · j 
n+ 1 
= j 
n+ 1 + δ · |Bi ∩ Cj | 
b . 
24
NON-STATIONARY REINFORCEMENT LEARNING 
Taking maximum over i ∈ [n], we have V ∗ t(j)(s1) = 
j n+1 + κj · δ. 
Hence, any algorithm that returns δ/b = O(1/mn) = O(1/T ) approximation to optimal V -value could distinguish between YES/NO instance of MAX-IP, and therefore, assuming SETH is true, there is no algorithm with n2−o(1)/T = T 1−o(1) amortized runtime per update. 
25