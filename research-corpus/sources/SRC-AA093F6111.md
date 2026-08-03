> Source: https://arxiv.org/pdf/2601.07118

Reward-Preserving Attacks For Robust Reinforcement Learning 
Lucas Schott 1 2 Elies Gherbi 1 Hatem Hajri 3 Sylvain Lamprier 4 2 
Abstract Adversarial training in reinforcement learning (RL) is challenging because perturbations cascade through trajectories and compound over time, making fixed-strength attacks either overly destructive or too conservative. We propose reward-preserving attacks, which adapt adversarial strength so that an α fraction of the nominal-to-worst-case return gap remains achievable at each state. In deep RL, perturbation magnitudes η are selected dynamically, using a learned critic Q((s, a), η) that estimates the expected return of α-reward-preserving rollouts. For intermediate values of α, this adaptive training yields policies that are robust across a wide range of perturbation magnitudes while preserving nominal performance, outperforming fixed-radius and uniformly sampled-radius adversarial training. 
1. Introduction Adversarial attacks in machine learning refer to deliberately crafted perturbations, that are designed to cause learned models to fail in unexpected or worst-case ways (Goodfel-low et al., 2014). These attacks reveal fundamental limitations in the generalization and stability of neural networks, motivating a wide range of defenses and training procedures collectively known as adversarial robustness (Madry et al., 2017). While the phenomenon first received attention in supervised image classification, its implications extend far beyond static prediction problems, particularly to sequential decision-making systems such as reinforcement learning (RL) (Schott et al., 2024). 
When attacking a classifier, one is typically interested in inducing a pointwise divergence in its prediction, while remaining undetectable. This makes it possible to specify attack strengths in a relatively simple way, using classi-
1IRT SystemX, Palaiseau, France 2MLIA, ISIR, Sorbonne Uni-versité, Paris, France 3Safran Electronics and Defense, Palaiseau, France 4LERIA, Université d’Angers, France. Correspondence to: Lucas Schott <lucas.schott@irt-systemx.fr>, Sylvain Lamprier <sylvain.lamprier@universite-angers.fr>. 
Preliminary work. 
cal perturbation norms (e.g., L0, L1, L2, or L∞), which produce imperceptible modifications, at least to a human observer, and do not alter the semantic content of the input (Goodfellow et al., 2014; Carlini & Wagner, 2017). In adversarial training for classifiers, such attack strength can moreover be globally tuned, taking into account the model’s current ability to defend itself. 
In the context of adversarial training for robust RL, the situation becomes substantially more complex. Beyond a pointwise divergence, the objective is long-term: the agent seeks to maximize cumulative reward despite perturbations occurring along entire trajectories. If perturbations become too strong, the agent may be unable to solve the task at all, thereby losing the feedback signal required to improve. More subtly, the agent may remain trapped in a suboptimal region of the state space without a means of escaping it. Beyond these learning difficulties, certain attacks may even make the task unsolvable even for an optimal policy adapted to the attack. Conversely, if perturbations are too weak, they fail to induce meaningful distribution shifts or information loss, and adversarial training no longer promotes meaningful robustness (Morimoto & Doya, 2005; Huang et al., 2017; Pinto et al., 2017). 
Consider a simple illustrative example involving a narrow bridge, as depicted in the toy gridworld environment from figure 1. In regions of the environment where many nearby states share similar futures, one may remove nearly all information from the observation vector, or induce strong perturbations of specific components or dynamics, without destroying the agent’s ability to recover. However, if the observation or dynamics are fully corrupted precisely when the agent is on the narrow bridge, then crossing becomes virtually impossible, even with unlimited training. This highlights two qualitatively different situations: (1) if the critical region can be avoided via an alternative path with only a small reduction in cumulative reward, a robust policy should steer the agent away from danger, which can be encouraged by targeted attacks at the approach to the bridge; (2) if crossing the bridge is mandatory, perturbations must remain weak enough to preserve a viable recovery strategy, otherwise adversarial training fails. Motivated by this, we aim at ensuring two complementary forms of robustness in RL policies: local robustness, the ability to recover from perturbations while maintaining long-term performance; and 
1 
 
 
 
 
 
 
 
 
 
 
Reward-Preserving Attacks For Robust Reinforcement Learning 
Figure 1. Comparison of value functions and induced optimal trajectories on a deterministic GridWorld environment for: (left) classical Value Iteration, (middle) Robust Value Iteration (RVI), and (right) our α-reward-preserving extension of RVI (α = 0.3). The environment contains a single positively rewarded goal state located in the top-left corner, while black cells correspond to terminal states with reward −1. A discount factor γ = 0.999 is used. Robustness is enforced through an uncertainty set B over transition kernels, where the ambiguity radius ηB is computed via a Sinkhorn-regularized W2 transportation cost between next-state distributions, with ground costs defined as Euclidean distances between successor states. Implementation details are provided in Appendix A.5. 
global robustness, the ability to favor safer over excessively risky trajectories without invalidating the task. 
To achieve this, we propose a new approach for robust reinforcement learning that dynamically adjusts attack magnitudes based on an estimate of state criticality, with the aim of preserving task solvability from any situation. After giving background on adversarial training in RL, Section 2 introduces our α-reward-preserving attacks and analyzes them in the tabular setting. Section 3 extends our α-reward-preserving training approach for the deep RL setting. Fi-nally, experiments in Section 4 demonstrate the effectiveness of our approach in training policies that are resilient to diverse perturbations in their deployment environment. 
2. Toward Robust RL with Reward-Preserving Attacks 
2.1. Robust RL through Adversarial Training 
In this work, we consider Markov Decision Process Ω = (S,A, T,R,X,O, γ), where: S is the set of states in the environment; A is the set of actions available to the agent; T : S ×A×S → [0, 1] is the stochastic transition function, with T (s+|s, a) denoting the probability of transitioning to state s+ given state s and action a;R : S×A×S → R is the reward function, with R(st, at, st+1) the reward received by the agent for taking action at in state st and moving to state st+1; X is the set of observations as perceived by the agent; O : S ×X → [0, 1] is the observation function, with O(x|s) denoting the probability of observing x ∈ X given state s. For simplicity, we consider in the following that O is information preserving (i.e., it is a deterministic bijective mapping from S to X), while it could be extended to partially observable problems (POMDP). We also consider that any x ∈ X is a vector of k real values ϕ(s), with ϕ the mapping from s ∈ S to its corresponding encoding vector. 
In Ω, we consider policies π : S × A → [0, 1], where π(a|s) denotes the probability of selecting action a given state s. The classical goal in RL is to discover policies that maximize the expected cumulative discounted reward Eτ∼πΩ [ 
∑|τ |−1 t=0 γtR(st, at, st+1)], with 
τ = ( (s0, a0), (s1, a1), ..., (s|τ |, ) 
) a trajectory in Ω and 
πΩ(τ) the probability of τ in Ω when using policy π for selecting actions at each step. The discount factor γ ∈]0; 1[ weights the importance of future rewards. We note V π,Ω(s) = Eτ∼πΩ [ 
∑|τ |−1 t=0 γtR(st, at, st+1)|s0 = 
s] the value function associated to π for rollouts starting from s0, π∗,Ω the optimal policy in Ω and V ∗,Ω(s) its associated value function. Similarly, Qπ,Ω(s, a) = 
Eτ∼πΩ [ ∑|τ |−1 t=0 γtR(st, at, st+1)|s0 = s, a0 = a] is the 
state-action value function for π in Ω. 
For achieving robust agents, adversarial training introduces adversarial agents (or attackers) ξ, which produce perturbations for the situations encountered by the protagonist agent π. The adversarial actions taken by ξ are denoted Aξ,Ω = (aξ,Ωi )ki=1 ∈ 
∏k i=1A 
ξ,Ω i , where each aξ,Ωi corre-
sponds to a component (e.g., a parameter of the MDP) and Aξ,Ωi represents the set of values that the environment Ω allows for this component. Usually, the goal is to consider worst-case distributions in an uncertainty set B, to promote robustness of the protagonist agent π. The radius ηB of B is defined according to a given metric (e.g., in term of f-divergence or in term of L1, L2 or L∞ distances), either on the parameters of the nominal MDP Ω or directly on its distributions, and determines the maximal magnitude of perturbations allowed inside B. The adversarial training setting can then be formalized as: 
π∗ = argmax π 
E τ∼πΩξ∗ [R(τ)] 
s.t. ξ∗ = argmin ξ∈B 
∆π,Ω(ξ) (1) 
2
Reward-Preserving Attacks For Robust Reinforcement Learning 
where we note Ωξ the environment under attacks from adversary ξ. By a slight abuse of notation, ξ ∈ B stands as an attacker that is constrained to produce only perturbed distributions within B. ∆π,Ω(ξ) stands as the optimization objective of the adversarial agent given π and the training environment Ω. In the following, we consider the setting where the attacker aims at minimizing the cumulative discounted reward: ∆π,Ω(ξ) = E 
τ∼πΩξ∗ [R(τ)], while our proposal could be applied for other settings. Given a worstcase objective, the attacker can act on any component of the MDP, ranging from the observation function to the transition kernel. When acting on the transition function, the Robust Value Iteration algorithm is shown to converge asymptotically toward the optimal policy under the optimal worst-case attack for the tabular setting (Wiesemann et al., 2013). 
2.2. Reward-Preserving Attacks 
From formulation in (1), we note that the shape of the uncertainty set B is highly impactful regarding the optimal policy under Ωξ 
∗ . It is known that sa-rectangular uncertainty 
sets (i.e., B allows independent perturbations for each stateaction pair of the MDP) usually leads to very hard attacks, inducing too difficult or even impossible problems Ωξ 
∗ , 
which in turn results in too conservative policies (Zouitine et al., 2024). Hence, many approaches propose to regularize the attacks inside B, with constrained perturbations. For instance, Active Domain Randomization (Mehta et al., 2020) propose to discover the worst-case global parametrization of the MDP rather than relying on sa-rectangular attacks. However, this induces difficult worst-case identification in subsets of B that are no longer convex w.r.t. the MDP parametrization (e.g., implying convex hull approximation). Other approaches propose to apply regularization through time (e.g., as in (Zouitine et al., 2024)), to act on the timing of the attacks (Fan et al., 2025), or to consider restrictions over the radius of B to lower the power of the resulting attacks (Ma et al., 2018)1. However, these approaches do not allow for local adaptation of attacks regarding the current state area of the agent. We claim this is crucial for effectively coping with both kinds of robustness mentioned in the introduction. To close that gap, we propose to introduce a new kind of ”reward-preserving” attacks, as defined below. Definition 2.1 (Reward-Preserving Attack) Given a MDP Ω and an uncertainty set B in that MDP, an attack ξ ∈ B on this MDP is said α-Reward-Preserving for a state s ∈ S and an action a ∈ A(s) iff there exists an optimal policy π∗,Ωξ 
adapted to ξ such that: Q∗,Ωξ 
(s, a) ≥Q∗,Ωξ∗ 
(s, a)+ 
α ( Q∗,Ω(s, a)−Q∗,Ωξ∗ 
(s, a) ) 
, where Q∗,Ωξ∗ 
(s, a) stands 
as the value at s, a using the optimal policy π∗,Ωξ∗ 
against 
1Further discussion about related work is given in appendix A.1. 
the optimal attacker ξ∗ for Ω. 
The set of α-Reward-Preserving attacks for a state-action pair (s, a) is noted Ξα(s, a). An attack ξ is also said α-Reward-Preserving for an MDP Ω iff for any state-action pair (s, a) of Ω, ξ ∈ Ξα(s, a). The set of α-Reward-Preserving attacks for an MDP Ω is denoted as Ξα(Ω). For any pair (s, a), we have Ξα(Ω) ⊆ Ξα(s) ⊆ B. 
That is, an α-reward-preserving attack ξα ∈ Ξα(Ω) is an attack that guarantees that a proportion α of the gap between the best expected cumulative reward in the original MDP Ω and the one in the worst-case modified MDP in B remains reachable in the resulting perturbed MDP Ωξα . Importantly, this definition differs fundamentally from a convex mixture αΩ + (1 − α) Ωξ 
∗ , which merely constrains Ωξ to stay 
close to the nominal MDP Ω, and offers no guarantee that a fixed proportion of the reward gap is preserved at each state– action pair. Our definition, instead, constrains the optimal Q-values, effectively combining the policies of the nominal and worst-case MDPs at the value-function level—an objective that cannot generally be realized by simple MDP interpolation. 
Given a policy π, the worst case α-reward-preserving attack ξ∗,πα is defined for each state s and action a as belonging to: 
Ξ∗,π α (s, a) = arg min 
ξ∈Ξα(s,a) Qπ,Ω 
ξ 
(s, a) (2) 
We also note Ξ∗,∗ α (s, a) the set of optimal worst-case α-
reward-preserving attacks set for an optimal policy against them: ξ∗α(s, a) = argminξ∈Ξα(s,a) maxπ Q 
π,Ωξ 
(s, a), and 
Q∗,Ωξ∗α (s, a) the associated value function for the corresponding optimal policy. Note that Ξ∗,∗ 
α (s, a) is typically not convex in the space of admissible attacks, even under SA-rectangularity, because the mapping ξ 7→ Q∗,Ωξ 
(s, a) is highly non-linear in the perturbed MDP. As a result, convex combinations of two attacks in Ξ∗,∗ 
α (s, a) do not generally satisfy the α-reward-preserving constraints. 
Extending classical Robust Value Iteration (RVI) (Wiese-mann et al., 2013) to α-reward-preserving uncertainty sets in the tabular setting is non-trivial, as it requires optimizing admissible attacks whose constraints depend on the optimal policies adapted to them. A naive approach would define worst-case α-reward-preserving Q-values as 
Q̂(s, a) := Q∗,Ωξ∗ 
(s, a) + α ( Q∗,Ω(s, a)−Q∗,Ωξ∗ 
(s, a) ) , 
interpolating between nominal and worst-case solutions. However, such Q̂ generally fails to satisfy the Bellman optimality equations for any realizable MDP, and therefore cannot be used directly within a Bellman iteration. Sec-tion A.4.2 discusses this limitation and presents an extension of RVI with weaker guarantees, which serves as a foundation for our deep robust approach in Section 3. 
3
Reward-Preserving Attacks For Robust Reinforcement Learning 
Worst-case α-reward-preserving attacks also preserve the reward structure for sufficiently large B (Section A.6). Property 1 Reward Structure Preservation Given a sufficiently large uncertainty set B, Q∗,ξ∗ is equal to a given constant minimal value Rmin for every state s ∈ S and action a ∈ A(s) (i.e., the worst-case attacks fully destroy the reward signal). In that setting, worst-case α-reward-preserving attacks preserve the structure of the reward: 
∀((s, a), (s′, a′)) ∈ (S ×A)2 : Q∗,Ω(s, a) > 
Q∗,Ω(s′, a′) =⇒ Q∗,Ωξ∗α (s, a) > Q∗,Ωξ∗α 
(s′, a′) (3) 
Thus, for sufficiently large B, there exists an optimal policy for Ωξ 
∗ α that coincides with the optimal policy of the 
nominal MDP Ω. In non-tabular settings with stochastic neural policies, agents can acquire local robustness with such attacks, by learning to recover from complex or misleading situations without biasing the nominal optimal policy (which may occur with classical uncertainty sets). Under observation attacks, this manifests as learning to denoise inputs and reduce sensitivity to isolated perturbations, while under dynamics attacks it encourages actions that keep the agent away from risky states — such as the edge of a bridge —, even when transitions are manipulated. Importantly, such robustness is achieved without altering the optimal policy path, as recovery strategies remain feasible. 
However, this does not address global robustness: preserving the reward structure does not enable the agent to prefer safer paths over riskier ones when the latter yield higher nominal returns. In contrast, such preferences can be recovered in classical settings with constrained uncertainty sets B, as formalized by the following property (Section A.6). Property 2 (Condition for Preferred State–Action Change) Consider two state–action pairs (s, a) and (s′, a′) such that 
dΩ ( (s, a), (s′, a′) 
) := Q∗,Ω(s, a)−Q∗,Ω(s′, a′) > 0. 
Under a worst-case α-reward-preserving attack ξ∗α defined for a given uncertainty set B, the preference between (s, a) and (s′, a′) is reversed if and only if: dΩξ∗ 
( (s′, a′), (s, a) 
) > α 
1−α dΩ ( (s, a), (s′, a′) 
) + 
δ ( (s′, a′), (s, a) 
) , where δ((s′, a′), (s, a)) := (ϵs′,a′ − 
ϵs,a)/(1 − α), with ϵs,a denotes the gap between Q∗,Ωξ∗α (s, a) and its α-reward-preserving lower bound Q̂(s, a) := (1 − α)Q∗,Ωξ∗α (s, a) + αQ∗,Ω(s, a). While δ((s′, a′), (s, a)) → 0 as ηB → 0, the actual variation of Q∗,Ωξ∗ 
(s, a) can be amplified by local gaps in successor actions, so δ variations may be dominated by the effective sensitivity of Q in “dangerous” zones, which induce preference changes under α-reward-preserving attacks. 
In other words, for any given state s, the optimal action changes from a to a′ under a worst-case α-reward-
preserving attack whenever the resulting increase in worstcase performance outweighs a proportion α 
1−α of the nomi-
nal performance loss (assuming that both Q∗,Ωξ∗α are close enough to their respective bounds Q̂). This effect also propagates through distant states: α-reward-preserving attacks may modify optimal trajectories over long horizons, as safer routes become preferable when their nominal performance loss is offset by improved worst-case robustness within the uncertainty set B. 
We remark that α acts as a weighting factor that balances nominal performance against worst-case performance under attacks in B. When α < 0.5, robustness to worst-case scenarios dominates the decision-making process, making worst-case performance more important than nominal performance. Conversely, when α > 0.5, the situation is reversed: nominal performance becomes more influential than worst-case robustness. 
This also highlights the importance of the shape of B, as it directly influences the resulting behaviors. Under α-reward-preserving attacks with α > 0, some amount of the nominal reward signal is always preserved, ensuring that efficient policies can still be learned. However, since deviations toward safer trajectories are only allowed when they improve worst-case values within B, global robustness is encouraged only when the uncertainty set is well structured. In particular, the worst-case performance Q∗,Ωξ∗ 
should vary on a scale comparable to nominal performance differences so that robustness incentives align with meaningful behavioral changes. To illustrate this, figure 1 compares Value Iteration (VI), Robust Value Iteration (RVI) and our α-reward-preserving extension of RVI on a deterministic GridWorld environment with attacks on the dynamics. It highlights a setting, with rather large B, where classical RVI exhibits strong risk aversion. It becomes excessively conservative and avoids the path to the goal. In contrast, our α-reward-preserving extension reshapes the value landscape to downweight excessively pessimistic transitions, enabling the agent to reach the goal while still accounting for model uncertainty. 
2.3. Magnitude–Direction Decomposition of Perturbations 
Following observations from the previous section, we need to control the shape of the uncertainty set B and the scope of the attacks in order to obtain an effective training approach under α-reward preserving attacks. To do so, we propose to consider attacks of the nominal MDP Ω that decouple (i) the choice of the magnitude η ≤ ηB, where ηB stands for the maximal magnitude allowed for attacks (which defines the radius of the convex set B(s, a) that includes all allowed perturbations of the attacked MDP component for state s and action a), and (ii) the choice of the direction A of the 
4
Reward-Preserving Attacks For Robust Reinforcement Learning 
crafted perturbation for each state-action pair. Following this, an attack is defined as ξα := (ξηα, ξ 
A ) , where: 
 ξA : S × A → Aξ,Ω is the direction selector, which, given a state s, and (optionally) an action a, produces a normalized perturbation direction over the parameters of the perturbed component. 
 ξηα : S × A → R+ is the magnitude selector, assigning to each state s and (optionally) action a a perturbation magnitude η := ξηα(s, a) within R+. This selector aims to scale the attack so that its corresponding perturbation maintains the MDP component inside Ξα(s, a) ⊆ B(s, a), with B(s, a) the whole set of possible attacks for (s, a) and Ξα(s, a) the subset of those that are α-reward-preserving. Thus, η := ξη(s, a) stands as the radius of the convex core Bα(s, a) of Ξα(s, a). 
Thus, for any state s ∈ S and action a ∈ A(s), an attack is fully specified by ξ(s, a) = (η,A) with η = ξηα(s, a) and A = ξA(s, a), and acts on a perturbed MDP component ω as ω̂(s, a) ∝ ω(s, a) + ηA. For dynamics attacks, taking Aξ,Ω = ∆(S) and defining Pξ(· | s, a) ∝ PΩ(· | s, a)+ηA(·) yields a convex s–a rectangular uncertainty set Bα(s, a) corresponding to the convex core of Ξα(s, a). Sim-ilarly, when perturbing a global parameter vector ω ∈ Rd of the dynamics (e.g., some factors of physical forces in a simulator), we set ω = ω0 + ηA with A ∈ {−1,+1}d, subject to admissible bounds. Observation attacks can be handled analogously, e.g., by defining Oξ(s) = δ(ϕ(s) + ηA) with ∥A∥2 = 1. In all cases, Bα(s, a) contains at least one boundary point of Ξα(s, a), corresponding to a worst-case attack in Ξ∗,∗ 
α (s, a). 
In this work, we mainly focus on the definition of accurate magnitude selectors, as it is core for building α-reward-preserving attacks. The direction selector can be defined from any given classical approach from the literature. For a given state-action pair (s, a), we consider the Q value from the attacker perspective, setting η as its first action and following an α-reward-preserving attacker ξα ∈ Ξα(Ω) in the subsequent steps: 
Qπα((s, a), η) = E τ∼πΩξα [R(τ)|s0 = s, a0 = a, η0 = η] 
where η0 corresponds to the magnitude of attack applied on the first state-action s0, a0 from the trajectory. At each state-action pair, the worst-case identification problem thus comes down at taking the highest η that satisfies (2), then considering the worst-case direction within the corresponding ball. Specifically, we can note that all attacks ξα from Bα(s, a) respect: Q∗ 
α((s, a), ξ η α(s, a)) ≥ 
(1 − α)Q∗ 0((s, a), ηB) + αQ∗ 
1((s, a), 0) 2. Our general ap-
proach of approximated α-preserving-attacks for deep reinforcement learning presented in next section builds on this magnitude-parametrized value function. 
2We can remark that this is not necessarily true in Ξα(s, a) 
3. Approximated Reward-Preserving Attacks for Robust Deep RL 
Moving from the tabular setting with a known MDP to the more practical deep RL regime introduces several additional challenges for the use of α-reward-preserving attacks: 1) The construction of Ξα relies on optimal policies adapted to worst-case attacks, which are no longer accessible in the deep RL setting and must therefore be approximated using reference policies that lag behind the current policy π; 2) Q-values must be approximated (typically via neural networks) from rollouts collected under a sufficiently diverse set of attacks to enable reliable magnitude selection; 3) These Q-value estimates must be continuously updated to track the evolving state–action occupancy induced by the learning policy. We discuss each of these challenges in the remainder of this section. 
3.1. Reference Policies 
Since optimal policies under attack are not accessible in deep RL, we approximate α-reward-preserving attacks using a reference policy π̃. We define Ξ̃α(Ω) as the set of attacks under which π̃ preserves at least an α fraction of the reward gap between its minimal and maximal achievable returns. That is, for each (s,a), we consider attacks within: 
Q̂α(s, a) := (1− α)Qπ̃0 ( (s, a), ηB 
) + αQπ̃1 
( (s, a), 0 
) , 
B̃α(s, a) := { ξ : Qπ̃α 
( (s, a), ξηα(s, a) 
) ≥ Q̂α(s, a) 
} . (4) 
which corresponds to the convex core of the corresponding set Ξ̃α(s, a), which includes all so-called (π̃, α)-reward-preserving attacks. In the following, we use B̃ηα(s, a) as the set of allowed magnitudes in Bα(s, a). 
We have: Ξα ⊆ Ξ̃α and Ξπ,∗α ⊆ Ξ̃π,∗α . That is, approximate α-reward-preserving attacks that are based on a reference policy π̃ are less conservative than attacks from Ξ̃π,∗α . How-ever, assuming that π′ is a policy lagging behind the currently trained policy π, inducing a two-timescale learning process, we claim we can define a process that approximately concentrates on Ξ∗,∗ 
α , to obtain an α-robust policy. In the following, policy π and π̃ are defined as neural networks with the same architecture, with parameters from π̃ that are periodically updated via polyak updates using weights from π. 
3.2. Approximation of Q-values for the full range of magnitudes in [0, ηB] 
In this setting, Q-values for magnitude selection are approximated with a neural network taking as input the state-action pair, the candidate magnitude η, and a target level of reward preservation – typically one of α, 0, or 1 as in (4). To obtain accurate Q-value estimates for π̃, it is necessary to sample 
5
Reward-Preserving Attacks For Robust Reinforcement Learning 
attack magnitudes across the full range [0, ηB], rather than greedily from Ξ̃α, to ensure sufficient diversity in the training transitions. This allows the Q-network to predict reliably not only the value for Qπ̃α((s, a), ξ 
η α(s, a)), but also at the 
extrema, Qπ̃1 ((s, a), 0) and Qπ̃0 ((s, a), ηB), which are used as effective bounds for magnitude selection. To achieve this, we define an (ϵ, α)-reward-preserving sampling distribution pπ̃α(· | st, at) over [0, ηB], allocating (1 − ϵ) of its mass inside B̃α(st, at). At each step, with direction At := ξA(st, at) and magnitude ηt ∼ pπ̃α(· | st, at), we ensure that P ( ξt = (ηt, At) ∈ B̃α(st, at) 
∣∣ ξt ∈ B(st, at)) = 1− ϵ. 
In practice, we first identify the magnitude η∗(st, at) corresponding to the worst Q-value Qπ̃α(st, at) within B̃ηα(st, at) by evaluating a discrete set of candidates in [0, ηB] and selecting the largest one satisfying (4)3. We then sample ηt from an exponential distribution with rate λt = − log(ϵ)/η∗(st, at), ensuring both coverage of the full admissible range and adherence to the (ϵ, α)-reward-preserving requirement. Finally, sampled magnitudes are clipped to [0, ηB+], with ηB+ the radius of an extended uncertainty set. In our experiments, using ηB+ > ηB proved beneficial: it allows occasional very challenging attacks during training while still leveraging the reward-reshaping effects induced by the use of a narrow set B (see Property 2). This approach is of course more conservative than always using η∗(st, at), though this effect can be mitigated by lowering α. Alternative distributions (e.g., truncated Gaussian, mixtures, epsilon-greedy with noise) could also be considered. 
3.3. Off-policy Updates for non-Stationary State-Action Occupancy 
As π evolves during training on the perturbed MDP, its stateoccupancy distribution gradually diverges from that of the reference policy π̃, on which the Q-network was trained. Consequently, Qπ̃α, Qπ̃0 , and Qπ̃1 can become inaccurate on new state-action pairs, causing the selected attacks ξ to either collapse to null actions or saturate at ηB, which may result in catastrophic forgetting of acquired robustness or even nominal performance. To prevent this, the Q-network defining the attacks must be continuously fine-tuned throughout training. 
To adapt the Q-networks during training, we use off-policy updates from transitions (st, at, ηt, At, rt, st+1) collected under π. For each transition, we minimize the squared α-reward-preserving temporal difference 
δt := Qπ̃α(·)− rt − γ E[Qπ̃α(·)] 
weighted by the importance ratio wt = π̃/π to account for 
3We use a geometric sequence of 40 candidates starting from ηB with common ratio 0.75, giving more precision for small magnitudes. 
the fact that the Q-networks encode values for π̃ rather than π. We distinguish two settings: 
 Observation attacks: the attack acts on the policy input and is agnostic to at, so Qπ̃α((st, at), ηt) reduces to Qπ̃α(st, ηt), with 
δt := Qπ̃α(st, ηt)− rt − γEηt+1 
[ Qπ̃α(st+1, ηt+1) 
] , 
wt = π̃(at|ϕ(st) + ηtAt) 
π(at|ϕ(st) + ηtAt) . 
where the expectation on ηt+1 is taken according to pπ̃α(.|st+1). 
 Dynamics attacks: the attack can exploit the agent’s action, so 
δt := Qπ̃α ( (st, at), ηt 
) − rt 
− γ Eat+1 Eηt+1 
[ Qπ̃α 
( (st+1, at+1), ηt+1 
)] , 
wt = π̃(at|st) π(at|st) 
. 
where at+1 ∼ π̃(.|st+1) and the expectation on ηt+1 
is taken according to pπ̃α(.|st+1, at+1). 
We remark that, rather than using the magnitude ηt+1 from the stored transition, we define δt with a target that considers a recomputed ηt+1. This is important in order to account for the evolution of the Q-networks and to maintain consistency of the Bellman updates. Next, while we could use a single sample of ηt+1 at each step, we instead approximate the full expectation to reduce variance. In our setting, this can be done using the same sequence of magnitude candidates already used to define η∗t (see Section 3.2): We approximate Eη∼pπ̃α [Q 
π̂ α((st, at), η)] by applying a trapezoidal rule on 
our geometric grid {ηi} for the clipped exponential density on [0, ηB+], and adding the point mass at ηB+ of size e−λtηB+ . 
Finally, we update the dynamic Q-network Qψα for Qπ̃α 
by performing gradient descent on wt δ2t . While Qπ̃0 and Qπ̃1 could in principle be optimized similarly by restricting transitions to ηt = ηB and ηt = 0, respectively, and setting ηt+1 = ηt, this filtering is highly inefficient in practice. In-stead, we employ two separate Q-networks: (1) a dynamic network Qψα 
(·, η) modeling the expected return under variable α-reward-preserving magnitudes, and (2) a static network Qψc(·, η) conditioned on a fixed magnitude, such that Qψc 
(·, ηB) ≈ Qπ̃0 (·, ηB) and Qψc (·, 0) ≈ Qπ̃1 (·, 0). 
The static network allows sharing information across all constant-magnitude transitions in [0, ηB], leveraging every collected transition even though only the extremes are needed to define the α-reward-preserving magnitude sets. 
Algorithms 3 and 4 (in Appendix A.7) present the complete procedures for dynamics and observation attacks respectively, following all the main steps described in this section. 
6
Reward-Preserving Attacks For Robust Reinforcement Learning 
4. Experiments We study robustness to adversarial perturbations of bounded magnitude η, starting from a pre-trained (baseline) agent. We begin by validating the behavior of α-preserving attacks for a fixed policy. Next, we experience adversarial finetuning of agents using our dynamic α-preserving attacks. Finally, we compare robustness of our obtained policies against agents trained using non-adaptive baselines, using either a constant or a uniformly sampled magnitude. Exper-iments reported focus only on observation attacks, experiments for dynamics attacks are left for future work. 
4.1. Experimental setup 
We evaluate on HalfCheetah-v5 using a pre-trained SAC (Haarnoja et al., 2018) agent as our baseline. The adversary applies observation perturbations constrained by L2 radius η ≤ ηB using the FGM QAC attack (results with other attacks are given in appendix A.3.1). This attack method is a variant of the FGSM attack (Goodfellow et al., 2014) for actor attacks of Q actor-critic agents. It targets both networks jointly by back-propagating gradients from the critic network q̃ through the actor network π̃ to the input observation x of the actor: 
x′ = x−η ∇xq̃ 
( x⊥, µπ̃(x) 
)∥∥∇xq̃(x⊥, µπ̃(x))∥∥2 , x⊥ := stopgrad(x) 
where µπ̃ stands as the mean parameter of the gaussian distribution produced by the reference SAC actor policy π̃. That is, it seeks at the direction in the observation space that results in an action that most decreases the expected return. Note that q̃ is trained from a buffer of non-perturbed observations, while the actor π̃ uses perturbed ones. 
We report episodic return under either no perturbation (η = 0) or under test-time attacks at magnitude η, averaging over 20 evaluation episodes per checkpoint (plots show rolling average evaluation over the 5 last checkpoints) and per training seed (3 seeds per setting used in our experiments). Experiments were performed on Nvidia V100 GPU devices. The code will be publicly released after acceptance. All hyper-parameters used are given in appendix A.2. 
4.2. Reward-preserving attacks via a learned Qπ̃α((s, a), η) and reward preservation target α 
We first analyze the behavior of reward-preserving attacks for a fixed baseline agent (i.e., π̃ = π is constant over the whole training process). In these experiments, we train critics of the form Qπ̃α((s, a), η) for various preservation levels α, in order to assess the impact of α on selected attack magnitudes and policy performances. 
Figure 2 reports the performance of the baseline agent under various values of α for reward-preserving at-
0. 00 
0. 10 
0. 20 
0. 30 
0. 40 
0. 50 
0. 60 
0. 70 
0. 80 
0. 90 
0. 95 
1. 00 
reward-preserving proportion 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
d 
mean reward (±std) mean perturbation radius  (±std) 
0.00 
0.02 
0.04 
0.06 
0.08 
0.10 
0.12 
m ea 
n pe 
rt ur 
ba ti 
on  r 
ad iu 
s 
Figure 2. Calibration of reward-preserving α-attacks on a pretrained agent using Qπ̃ 
α((s, a), η). Smaller values of α induce larger average perturbation magnitudes and lower returns, while α → 1 recovers nominal performance. 
tacks (using ηB = ηB+ = 0.3). The results validate that the mechanism behaves as intended: for smaller α, the attack is more aggressive, yielding lower achieved return and larger average chosen magnitude; as α → 1, attacks become mild, returns increase, and the average chosen magnitude decreases. 
4.3. Adversarial α-reward-preserving training 
In this section, we consider the full α-reward-preserving adversarial training process introduced in Section 3.2. Starting from a pre-trained agent π, we fine-tune it against adversaries enforcing different levels of reward preservation α, which are trained jointly with π. The complete training procedure is summarized in Algorithm 4. 
All fine-tuning learning curves are reported in Ap-pendix A.3.1. They show that best performances are consistently obtained using ηB = 0.3 and ηB+ = 0.5. These values are thus used for all reward-preserving results presented in the following. 
Figure 3 shows the performance of the α-trained agents after 30M environment steps, evaluated across the full range of test-time perturbation magnitudes η. Agents trained with intermediate α (within [0.3; 0.7]) maintain strong performance throughout the range, with the best results observed for α = 0.6. Intermediate α-reward-preserving attacks provide a level of challenge adapted to the agent’s capabilities across different regions of the environment, avoiding overly aggressive perturbations in difficult areas while still encouraging exploration in easier or more regular regions. 
4.4. Comparison with non-adaptive approaches 
We then compare our method to standard adversarial training baselines with constant or random perturbation magnitudes. Starting from the pre-trained agent, we fine-tune agents against FGM QAC using either (i) a constant perturbation magnitude η, or (ii) a training magnitude sampled uniformly 
7
Reward-Preserving Attacks For Robust Reinforcement Learning 
0.00.01 0.05 0.1 0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m 
ea n 
re w 
ar ds 
agents trained with: 
=0.1 
=0.3 
=0.5 
=0.6 
=0.7 
=0.8 
=0.9 
=0.95 
Figure 3. Robustness profiles of α-trained agents under varying evaluation η: Agents trained with intermediate α are the more robust over a broader range of magnitudes η. 
as η ∼ U(0, ηB) to encourage robustness across perturbation magnitudes at test-time. Fine-tuning curves for these baselines are reported in Appendix A.3.2. 
To summarize cross-η robustness, Figure 4 evaluates the agents against a range of perturbation magnitudes η. We find that constant-η adversarial training produces specialized policies: each agent is robust for evaluation settings using the same perturbation magnitude as the one it was trained on, and robustness does not transfer well to significantly smaller or larger attack strengths. In contrast, training with uniformly sampled attack magnitudes yields policies that are robust over a broader range of settings for η in test environments. 
However, despite this improved coverage, these uniformlytrained agents remain consistently below our best rewardpreserving α-trained policies. The figure reports the performances of an agent trained with our α-reward-preserving process, using α = 0.6, which achieves significantly higher returns under perturbation (for any constant η > 0 at testtime) and also maintains stronger nominal performance (when η = 0). 
Experiments conducted with other adversarial attack methods, whose results are reported in Appendix A.3 report the same tendencies. 
Overall, reward-preserving α-training yields the best ro-bustness/nominal trade-off: it avoids over-specialization for a specific η, while preserving strong performance in the nominal setting. 
5. Conclusion We introduced reward-preserving attacks as a principled way to control adversarial strength in reinforcement learning 
0.0 0.05 0.1 0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 
B=0.02 
B=0.04 
B=0.06 
B=0.08 
B=0.1 
B=0.15 
B=0.2 
=0.02 
=0.05 
=0.1 
=0.2 
=0.5 
Figure 4. Robustness profiles under varying evaluation η. Agents trained with a constant magnitude η, are denoted η in the legend. Agents trained with random magnitude η ∼ U(0, ηB) are denoted ηB in the legend. Our reward-preserving approach with α = 0.6 achieves higher return across perturbed cases and preserves better nominal performance. 
without collapsing the learning signal. Our formulation constrains the adversary so that, at each state-action pair, an α-fraction of the nominal-to-worst-case return gap remains achievable for a policy adapted to the attack. To apply this idea in deep RL, we proposed a magnitude-direction decomposition and an approximate procedure that learns a critic Q((s, a), η) to adapt attack strength online to meet a reward-preservation target. 
Empirically, α-reward-preserving attacks behave as intended: decreasing α increases the average attack magnitude and reduces returns in a controlled way. Adversarial finetuning against these attacks preserves strong nominal performance while producing policies robust across a wide range of perturbations, whereas constant-magnitude or uniformly sampled attacks either overfit or sacrifice performance. In-termediate levels of preservation provide the best trade-off. 
These results demonstrate the potential of α-reward-preserving attacks as a principled mechanism for adaptive robustness, exposing agents to challenges matched to their capabilities while avoiding catastrophic failures. Beyond the current benchmarks, these attacks offer a promising tool for improving generalization, safe exploration, and transfer to novel environments, as they expose the agent to controlled yet meaningful stress-tests. Future work will extend this approach to high-dimensional continuous control, multiagent scenarios, and other types of perturbations, including dynamics perturbations, further leveraging the balance between challenge and task solvability. 
8
Reward-Preserving Attacks For Robust Reinforcement Learning 
Impact Statement This work introduces α-reward-preserving attacks as a principled mechanism for adaptive robustness in reinforcement learning. By controlling the magnitude of adversarial perturbations according to the agent’s capabilities, these attacks allow policies to experience meaningful challenges without compromising the solvability of the task. 
The immediate societal impact is primarily positive: this method can improve the reliability, safety, and generalization of RL agents in real-world applications, including robotics, autonomous systems, and other safety-critical domains. By training agents under controlled, adaptive perturbations, the approach reduces the likelihood of catastrophic failures when deployed in unpredictable environments. 
Potential risks include misuse in settings where robust agents are deployed for harmful purposes, and the fact that α-reward-preserving attacks can make the agent perceive normal conditions while it is actually being perturbed, which could be exploited in adversarial or deceptive scenarios. Overall, our work highlights a tool for safer and more resilient RL, emphasizing responsible usage. 
Acknowledgments This work has been supported by the French government under the “France 2030” program, as part of the SystemX Technological Research Institute within the Confiance.ai program. This work was granted access to the HPC resources of IDRIS under the allocation AD011015866 made by GENCI. 
References Abdullah, M. A., Ren, H., Ammar, H. B., Milenkovic, V., 
Luo, R., Zhang, M., and Wang, J. Wasserstein robust reinforcement learning. arXiv preprint arXiv:1907.13196, 2019. 
Borkar, V. S. Stochastic approximation with two time scales. Systems & Control Letters, 29(5):291–294, 1997. 
Borkar, V. S. and Borkar, V. S. Stochastic approximation: a dynamical systems viewpoint, volume 100. Springer, 2008. 
Carlini, N. and Wagner, D. Towards evaluating the robustness of neural networks. In 2017 ieee symposium on security and privacy (sp), pp. 39–57. Ieee, 2017. 
Dennis, M., Jaques, N., Vinitsky, E., Bayen, A., Russell, S., Critch, A., and Levine, S. Emergent complexity and zero-shot transfer via unsupervised environment design. Advances in neural information processing systems (NeurIPS), 33:13049–13061, 2020. 
Fan, J., Lei, X., Chang, X., Mišić, J., Mišić, V. B., and Yao, Y. Less is more: A stealthy and efficient adversarial attack method for drl-based autonomous driving policies. In IEEE Internet of Things Journal, volume 12, pp. 30215– 30227, 2025. 
Goodfellow, I. J., Shlens, J., and Szegedy, C. Explain-ing and harnessing adversarial examples. arXiv preprint arXiv:1412.6572, 2014. 
Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning (ICML), 2018. 
Huang, S., Papernot, N., Goodfellow, I., Duan, Y., and Abbeel, P. Adversarial attacks on neural network policies. arXiv preprint arXiv:1702.02284, 2017. 
Konda, V. and Tsitsiklis, J. Actor-critic algorithms. Ad-vances in neural information processing systems, 12, 1999. 
Liu, Q., Kuang, Y., and Wang, J. Robust deep reinforcement learning with adaptive adversarial perturbations in action space. In International Joint Conference on Neural Networks (IJCNN), pp. 1–8. IEEE, 2024. 
Ma, X., Driggs-Campbell, K., and Kochenderfer, M. J. Im-proved robustness and safety for autonomous vehicle control with adversarial reinforcement learning. In 2018 IEEE Intelligent Vehicles Symposium (IV). IEEE, 2018. 
Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. Towards deep learning models resistant to adversarial attacks. arXiv preprint arXiv:1706.06083, 2017. 
Mehta, B., Diaz, M., Golemo, F., Pal, C. J., and Paull, L. Active domain randomization. In Conference on Robot Learning, pp. 1162–1176. PMLR, 2020. 
Morimoto, J. and Doya, K. Robust reinforcement learning. Neural computation, 17(2):335–359, 2005. 
Pinto, L., Davidson, J., Sukthankar, R., and Gupta, A. Ro-bust adversarial reinforcement learning. In International conference on machine learning (ICML), pp. 2817–2826. PMLR, 2017. 
Ren, A. Z. and Majumdar, A. Distributionally robust policy learning via adversarial environment generation. IEEE Robotics and Automation Letters, 7(2):1379–1386, 2022. 
Robbins, H. and Monro, S. A stochastic approximation method. The annals of mathematical statistics, pp. 400– 407, 1951. 
9
Reward-Preserving Attacks For Robust Reinforcement Learning 
Russo, A. and Proutiere, A. Towards optimal attacks on reinforcement learning policies. In 2021 American Control Conference (ACC), pp. 4561–4567. IEEE, 2021. 
Schott, L., Delas, J., Hajri, H., Gherbi, E., Yaich, R., Boulahia-Cuppens, N., Cuppens, F., and Lamprier, S. Robust deep reinforcement learning through adversarial attacks and training: A survey. arXiv preprint arXiv:2403.00420, 2024. 
Tanabe, T., Sato, R., Fukuchi, K., Sakuma, J., and Aki-moto, Y. Max-min off-policy actor-critic method focusing on worst-case robustness to model misspecification. Advances in neural information processing systems (NeurIPS), 35:6967–6981, 2022. 
Wiesemann, W., Kuhn, D., and Rustem, B. Robust markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013. 
Yu, M. and Sun, S. Natural black-box adversarial examples against deep reinforcement learning. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 36, pp. 8936–8944, 2022. 
Zhang, H., Chen, H., Boning, D., and Hsieh, C.-J. Ro-bust reinforcement learning on state observations with learned optimal adversary. In International Conference on Learning Representation (ICLR), 2021. 
Zouitine, A., Bertoin, D., Clavier, P., Geist, M., and Rachel-son, E. Time-constrained robust mdps. Advances in Neu-ral Information Processing Systems, 37:35574–35611, 2024. 
10
Reward-Preserving Attacks For Robust Reinforcement Learning 
A. Appendix A.1. Related Work: Regulating Adversarial Attacks for Robust RL 
This appendix complements Section 2 by situating our reward-preserving attacks within the literature on adversarial robustness in RL. A recurring theme is that, unlike supervised learning, adversarial perturbations in RL compound along trajectories: overly aggressive attacks can make the task effectively unsolvable and collapse the learning signal, while overly weak attacks fail to induce meaningful robustness (Huang et al., 2017; Pinto et al., 2017; Morimoto & Doya, 2005). We organize prior work along three axes aligned with Section 2: (1) observation vs. dynamics attacks, (2) local vs. global control of perturbations, including sa-rectangularity and step-level perturbations vs. episode-level perturbations, and (3) regularizations that explicitly regulate attack strength. 
A.1.1. OBSERVATION VS. DYNAMICS ATTACKS 
Observation-space attacks. Observation attacks perturb the agent’s inputs, e.g., by adding norm-bounded noise to state features or pixels. Early work adapted supervised adversarial examples to RL and showed that policies can be highly sensitive to small input perturbations, motivating adversarial training in the observation space (Huang et al., 2017; Goodfellow et al., 2014; Carlini & Wagner, 2017). In deep actor-critic settings, gradient-based perturbations are natural when the attacker has white-box access, yielding FGSM/PGD-style attacks or variants that backpropagate critic signals through the actor to craft damaging perturbations (as in our FGM QAC setting). Beyond gradient-based attacks, observation perturbations can also be generated by adversarial policies trained with RL in a black-box manner: an attacker network observes xt (and optionally additional side information) and outputs an additive perturbation aξ,Xt , producing x′t = xt + aξ,Xt . Concurrent works such as OARLP (Russo & Proutiere, 2021), AdvRL-GAN (Yu & Sun, 2022), and ATLA (Zhang et al., 2021) follow this principle, typically optimizing an untargeted adversarial objective (often the negative of the protagonist return) without requiring access to gradients of the victim policy. 
Dynamics (transition) attacks and robust MDPs. A second family targets the transition kernel (or a parameterization of it) and is closely related to robust MDPs (Wiesemann et al., 2013). Robust value iteration and related dynamic-programming methods provide guarantees under structured uncertainty sets, but their conservatism and the realism of the induced worstcase dynamics strongly depend on the geometry and rectangularity assumptions of the uncertainty set (Wiesemann et al., 2013). In deep RL, dynamics perturbations are often implemented through adversarial policies that inject disturbances (forces, parameter shifts, etc.) based on the current state, resulting in a minimax game between a protagonist and an antagonist (Pinto et al., 2017). RARL (Pinto et al., 2017) is a canonical example: the adversary is trained with reward rξ = −r to apply disturbances that reduce the protagonist’s return. Extensions refine the adversary objective (e.g., risk-aware variants) or the perturbation mechanism, but share the same core idea: the transition dynamics are modified online by an adversarial agent. A complementary line of work attacks dynamics via adversarial domain randomization, where an environment parameter vector is sampled (typically per episode) from an uncertainty set. ADR (Mehta et al., 2020) learns a challenging sampling distribution over parameters (e.g., via particles and SVPG), and M2TD3 (Tanabe et al., 2022) conditions the critic on environment parameters to enable gradient-based search for worst-case configurations within the parameter set. Compared to per-step adversarial policies, these approaches often yield more “plausible” dynamics shifts by restricting perturbations to a low-dimensional parameterization. 
A.1.2. LOCAL VS. GLOBAL CONTROL OF PERTURBATIONS, SA-RECTANGULARITY 
A key distinction for robust RL is whether perturbations can be chosen locally at each time step and state-action pair, or only globally at the episode (or slower) timescale. 
Local (per-step) adversaries and sa-rectangularity. When the adversary can select perturbations at every step conditioned on the current state (and possibly action), the induced uncertainty is effectively sa-rectangular: the adversary can independently choose worst-case disturbances for each encountered state-action pair. This is the implicit setting of many adversarial-policy methods (including RARL) and of robust MDP formulations with sa-rectangular uncertainty sets (Pinto et al., 2017; Wiesemann et al., 2013). While this yields strong worst-case robustness, it can be excessively pessimistic: compounding, locally worst-case perturbations may drive the agent into unrecoverable regions and make training unstable or uninformative. 
11
Reward-Preserving Attacks For Robust Reinforcement Learning 
Global (episode-level or slowly varying) perturbations. In contrast, domain randomization methods typically choose an environment configuration once per episode, reducing the adversary’s ability to “chase” the agent online. Adversarial domain randomization (ADR) (Mehta et al., 2020) and worst-parameter search methods such as M2TD3 (Tanabe et al., 2022) fall into this category. These global perturbations often preserve solvability more readily, but they may miss critical state-local vulnerabilities that only appear when an attacker can time perturbations precisely. A middle ground constrains how quickly perturbations can change over time, producing disturbances that are neither fully local nor fully global; for instance, TC-RMDP bounds the rate of change of an adversarially controlled dynamics parameter, enforcing temporally correlated perturbations and mitigating the drawbacks of fully rectangular uncertainty (Zouitine et al., 2024). 
A.1.3. REGULARIZATIONS THAT PREVENT OVERLY AGGRESSIVE ATTACKS 
The above distinctions motivate a third axis: how methods regulate the adversary so it remains challenging yet does not break learnability. 
Magnitude penalties and constrained adversaries. A direct approach is to penalize attack magnitude or constrain adversary updates. SC-RARL adds a penalty term to the adversary objective to discourage large perturbations while still minimizing the protagonist return, thereby reducing training collapse under overly aggressive disturbances (Ma et al., 2018). Related ideas in distributionally robust RL constrain the adversary within a Wasserstein ball (or similar trust-region) around previous dynamics, producing adversarial-yet-plausible shifts rather than arbitrarily destructive ones (Abdullah et al., 2019). In generative environment design, DRAGEN learns a generator of environments and performs adversarial search under a distributional constraint, again aiming to avoid unrealistic worst-case jumps (Ren & Majumdar, 2022). 
Adaptive curricula and performance-based regulation. Another family regulates attack strength according to the protagonist’s learning progress. For example, A2P-SAC adaptively modulates the effective attacker influence so that attacks strengthen when the agent is performing well and weaken when training destabilizes, reducing the need for manual tuning and avoiding loss of learning signal (Liu et al., 2024). More broadly, curriculum and teacher-student environment design methods propose tasks/environments of increasing difficulty, attempting to keep training near the frontier of the agent’s capabilities; in UED/PAIRED, a teacher proposes environments that maximize regret between agents, implicitly controlling difficulty to remain informative (Dennis et al., 2020). 
Positioning reward-preserving attacks. Most prior regulation mechanisms act either (i) globally (episode-level parameter shifts, slowly varying disturbances), or (ii) via generic regularizers (penalizing magnitude or constraining adversary updates) that do not explicitly account for state criticality. Our setting highlights that solvability can be destroyed in specific regions (e.g., on a narrow bridge), while large perturbations may be tolerable elsewhere. Reward-preserving attacks address this by regulating adversarial strength locally through a value-based feasibility constraint: at each state-action pair, the adversary is restricted so that an α fraction of the nominal-to-worst-case return gap remains achievable (Definition 2.1). This yields a state-conditional attack magnitude that is strong in “safe” regions and automatically reduced in critical regions where aggressive perturbations would eliminate any viable recovery strategy. In this sense, our approach can be seen as a learnability-preserving alternative to fixed-radius (often too destructive) and uniformly sampled-radius (often too diffuse) adversarial training, while remaining compatible with both observation attacks (as in our experiments) and dynamics uncertainty sets (as in robust MDP formulations). 
12
Reward-Preserving Attacks For Robust Reinforcement Learning 
A.2. Hyper-parameters 
Table 1. Environment, initialization, and training budgets. 
Item Value 
Environment HalfCheetah-v5 RL framework StableBaselines3 RL algorithm SAC Nominal pre-training steps 20M 
Table 2. Architecture of the base SAC agent and optimizer settings 
Hyper-parameter Value 
Policy MlpPolicy Actor/Critic MLP net arch=[256,256,256] Activations ReLU Log std init -3 Discount 0.99 Batch size 256 Train envs 8 Replay buffer size 1e6 Polyak 0.005 Entropy coef auto Train freq 1 grad steps 1 SDE exploration True Learning rate 1e-3 
Table 3. Cycle-based training, and Qα-learning settings. 
Hyper-parameter Value 
Q MLP net arch=[256,256,256,256] Adversarial training steps 30M Train envs 8 Replay buffer 1e5 Q sample reuse 10 Q batch size 1,000 Protagonist LR 1e-3 Q-network LR 1e-3 Polyak (target Q) tau q=0.1 Polyak (reference protagonist) tau ref=0.1 Reward-preservation tail prob. ϵ = 0.01 
13
Reward-Preserving Attacks For Robust Reinforcement Learning 
A.3. Additional results 
To better understand which design choices drive performance and robustness, we report a set of supplementary studies. All runs use the same environment HalfCheetah-v5 and the same pre-trained SAC agent. We compare methods using evaluation curves recorded during training as well as the final-policy evaluation over a grid of perturbation magnitudes. 
Attacks considered. We evaluate robustness under three observation-space attacks : 
RUA denotes a random baseline where we sample a uniform random perturbation direction : 
x′ = x+ η u 
∥u∥2 with u ∼ U 
( −1, 1 
)dim(x) (5) 
FGM C is a variant of the FGSM attack for continuous-action policies: it perturbs the observation in the direction that minimizes an MSE loss between the deterministic actor output µπ̃(x) and a target action a. In our experiments, we use a random target sampled uniformly around the original action of the actor output : 
x′ = x− η ∇x∥µπ̃(x)− a∥22∥∥∥∇x∥µπ̃(x)− a∥22∥∥∥ 2 
with a ∼ U ( µπ̃(x)−5e−5 , µπ̃(x)+5e−5 
) (6) 
This produces perturbations with high stochasticity, while focusing on noise directions that have impacts on the policy’s decision. 
FGM QAC is an untargeted gradient-based attack. It is a variant of the FGSM attack for Q Actor-Critic architectures: it back-propagates the critic signal through the actor (freezing the critic observation input) to decrease the estimated q-value of the actor’s action : 
x′ = x− η ∇xq̃(x⊥, µπ̃(x)) ∥∇xq̃(x⊥, µπ̃(x))∥2 
with x⊥ := stopgrad(x) (7) 
This attack thus produces perturbations in the direction that looks the most detrimental from the critic point of view (hence, with long term impact). 
A.3.1. TRAINING WITH ALPHA REWARD PRESERVING STRATEGY FOR DIFFERENT ATTACK METHODS 
In this first ablation, we study the effect of the α-reward-preserving training strategy under different adversarial attack models. For each attack (FGM QAC, FGM C and RUA), we perform a grid search over α, ηB , and ηB+, and report in Figures 5, 6 and 7 evaluation curves collected during training at fixed perturbation magnitudes η ∈ {0, 0.05, 0.15}, and in Figure 8 evaluation of the final agent over a broader range η ∈ {0, 0.01, 0.05, 0.1, 0.15, 0.2}. 
We observe that using α = 0.6 with ηB = 0.3 and ηB+ = 0.5 consistently yields strong performance across all attack settings. This configuration provides a favorable trade-off between challenging the policy and preserving task solvability. 
14
Reward-Preserving Attacks For Robust Reinforcement Learning 
Figure 5. Evaluation curves during training with alpha reward preserving strategy under FGM-QAC attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(a) training; eval η = 0 
0 5 10 15 20 25 
million training steps 
2500 
0 
2500 
5000 
7500 
10000 
12500 
15000 
m ea 
n re 
w ar 
ds agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(b) training; eval η = 0.05 
0 5 10 15 20 25 
million training steps 
2500 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(c) training; eval η = 0.15 
Figure 6. Evaluation curves during training with alpha reward preserving strategy under FGM-C attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 5 10 15 20 25 
million training steps 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(a) training; eval η = 0 
0 5 10 15 20 25 
million training steps 
0 
2500 
5000 
7500 
10000 
12500 
15000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(b) training; eval η = 0.05 
0 5 10 15 20 25 
million training steps 
2000 
0 
2000 
4000 
6000 
8000 
10000 
12000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(c) training; eval η = 0.15 
15
Reward-Preserving Attacks For Robust Reinforcement Learning 
Figure 7. Evaluation curves during training with alpha reward preserving strategy under RUA attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(a) training; eval η = 0 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(b) training; eval η = 0.05 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(c) training; eval η = 0.15 
Figure 8. Evaluation of the agents trained with alpha reward preserving strategy against FGM QAC, FGM C and RUA for η ∈ {0, 0.01, 0.05, 0.1, 0.15, 0.2}. 
0.0 0.01 
0.05 0.1 0.15 0.2 
perturbation radius 
0 
5000 
10000 
15000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(a) FGM QAC : eval η ∈ [0, 0.2] 
0.0 0.01 
0.05 0.1 0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(b) FGM C : eval η ∈ [0, 0.2] 
0.0 0.01 
0.05 0.1 0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.3 B + =0.3 =0.6 B=0.3 B + =0.5 =0.6 B=0.3 B + =1.0 =0.6 B=0.5 B + =0.5 =0.6 B=0.5 B + =1.0 
=0.6 B=1.0 B + =1.0 =0.7 B=0.3 B + =0.3 =0.7 B=0.3 B + =0.5 =0.7 B=0.3 B + =1.0 =0.7 B=0.5 B + =0.5 
=0.7 B=0.5 B + =1.0 =0.7 B=1.0 B + =1.0 =0.8 B=0.3 B + =0.3 =0.8 B=0.3 B + =0.5 
=0.8 B=0.3 B + =1.0 =0.8 B=0.5 B + =0.5 =0.8 B=0.5 B + =1.0 =0.8 B=1.0 B + =1.0 
(c) RUA : eval η ∈ [0, 0.2] 
16
Reward-Preserving Attacks For Robust Reinforcement Learning 
A.3.2. TRAINING WITH CONSTANT AND RANDOM PERTURBATION STRENGTH FOR DIFFERENT ATTACK METHODS 
We then compare the α-reward-preserving strategy against simpler baselines that use a random uniform perturbation radius during training. For each attack (FGM QAC, FGM C and RUA), we grid-search over the perturbation parameters ηB and include, as a reference point, the best α configuration identified in the previous ablation. As above, we report in Figures 9, 10 and 11 evaluation curves collected during training at fixed perturbation magnitudes η ∈ {0, 0.05, 0.15}, and in Figure 12 evaluation of the final agent over a broader range η ∈ {0, 0.01, 0.05, 0.1, 0.15, 0.2}. 
We observe that our α-reward-preserving trained agent performs among the best across most settings. In some specific test attack magnitudes, it is slightly outperformed by baselines tailored to those particular conditions. However, these specialized baselines are then outperformed by our agent in the nominal environment or under stronger attacks, highlighting the overall robustness and generality of α-reward-preserving training. 
Figure 9. Evaluation curves during training with random uniform perturbation radius strategy under FGM-QAC attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(a) eval η = 0 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(b) eval η = 0.05 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(c) eval η = 0.15 
Figure 10. Evaluation curves during training with random uniform perturbation radius strategy under FGM-C attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(a) eval η = 0 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(b) eval η = 0.05 
0 5 10 15 20 25 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(c) eval η = 0.15 
17
Reward-Preserving Attacks For Robust Reinforcement Learning 
Figure 11. Evaluation curves during training with random uniform perturbation radius strategy under RUA attacks for evaluation settings η ∈ {0, 0.05, 0.15}. 
0 10 20 30 40 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(a) eval η = 0 
0 10 20 30 40 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
14000 
16000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(b) eval η = 0.05 
0 10 20 30 40 
million training steps 
0 
2000 
4000 
6000 
8000 
10000 
12000 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(c) eval η = 0.15 
Figure 12. Evaluation of the agents trained with constant or random uniform perturbation radius strategy against FGM QAC, FGM C and RUA for η ∈ {0, 0.01, 0.05, 0.1, 0.15, 0.2}. 
0.0 0.05 0.1 
0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(a) FGM QAC : eval η ∈ [0, 0.2] 
0.0 0.05 0.1 
0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(b) FGM C : eval η ∈ [0, 0.2] 
0.0 0.05 0.1 
0.15 0.2 
perturbation radius 
0 
2500 
5000 
7500 
10000 
12500 
15000 
17500 
m ea 
n re 
w ar 
ds 
agents trained with: 
=0.6 B=0.02 
B=0.04 B=0.06 
B=0.08 B=0.1 
B=0.15 B=0.2 
(c) RUA : eval η ∈ [0, 0.2] 
18
Reward-Preserving Attacks For Robust Reinforcement Learning 
A.4. Extension of RVI for α-reward-preserving attacks 
This section first recalls the classical Robust Value Iteration algorithm and then presents its extension for α-reward-preserving attacks. 
A.4.1. ROBUST VALUE ITERATION 
First, we recall the classical Robust Value Iteration in algorithm 1. 
Algorithm 1 Robust Value Iteration with r(s, a, s′) and action-value function Q 
Require: State space S, action space A, reward r(s, a, s′), nominal MDP Ω, uncertainty set B(s, a), discount γ Ensure: Robust Q-function Q∗,Ωξ∗ 
1: Initialize Q(s, a)← 0 for all (s, a) 2: for each iteration k = 0, 1, 2, . . . do 3: for each state s ∈ S do 4: for each action a ∈ A do 5: Compute worst-case expected Q over uncertainty set: 6: Qnew(s, a)← min 
P∈B(s,a) 
∑ s′ P (s′ | s, a) 
[ r(s, a, s′) + γmax 
a′ Q(s′, a′) 
] 7: end for 8: end for 9: Update Q(s, a)← Qnew(s, a) for all (s, a) 
10: end for 11: return Q 
This algorithm is guaranteed to converge asymptotically towards Q∗,Ωξ∗ 
(i.e., the robust Q-value for the optimal policy in the worst-case MDP for this policy given uncertainty sets B(s, a) in each pair s, a). For completeness, we recall the proof of convergence of this algorithm below. 
Convergence of Robust Value Iteration. Consider a discounted MDP with state space S, action space A, reward r(s, a, s′) and uncertainty sets B(s, a). Define the robust Bellman operator for action-values: 
(T Q)(s, a) = min P∈B(s,a) 
∑ s′ 
P (s′|s, a) [ r(s, a, s′) + γmax 
a′ Q(s′, a′) 
] , γ ∈ [0, 1). 
Proposition A.1 T is a γ-contraction in the supremum norm ∥ · ∥∞, hence it admits a unique fixed point Q∗,Ωξ∗ 
, and iterating 
Qk+1 = T Qk 
converges to Q∗,Ωξ∗ 
with 
∥Qk −Q∗,Ωξ∗ 
∥∞ ≤ γk∥Q0 −Q∗,Ωξ∗ 
∥∞. 
Proof. For any fixed transition P ∈ B(s, a), define the classical Bellman operator 
(T PQ)(s, a) = ∑ s′ 
P (s′|s, a) [ r(s, a, s′) + γmax 
a′ Q(s′, a′) 
] . 
It is well-known that T P is γ-contractant in ∥ · ∥∞, since for any Q1, Q2: 
∥T PQ1 − T PQ2∥∞ ≤ γ∥Q1 −Q2∥∞. 
Then, we remark that the robust operator is the pointwise minimum over P ∈ B(s, a): 
(T Q)(s, a) = min P∈B(s,a) 
(T PQ)(s, a). 
19
Reward-Preserving Attacks For Robust Reinforcement Learning 
For any two functions Q1, Q2 and for each (s, a), we thus have∣∣min P 
(T PQ1)(s, a)−min P 
(T PQ2)(s, a) ∣∣ ≤ max 
P 
∣∣(T PQ1)(s, a)− (T PQ2)(s, a) ∣∣ 
≤ γ∥Q1 −Q2∥∞. 
Therefore, T is also γ-contractant in ∥ · ∥∞. 
By the Banach fixed-point theorem, T has a unique fixed point Q∗,Ωξ∗ 
and the iterates Qk converge to Q∗,Ωξ∗ 
exponentially fast. 
A.4.2. α-REWARD-PRESERVING RVI FOR DYNAMICS SA-RECTANGULAR ATTACKS WITH KNOWN MDP 
In this section, we give an extension of the classical RVI presented in previous section, for our case of α-reward-preserving attacks. First, we can remark that the bound Q̂α(s, a) = (1−α)Q∗,Ωξ∗ 
(s, a)+αQ∗,Ω(s, a) that is used to define α-reward-preserving sets as defined in definition 2.1 only uses static components, which can be obtained by an initial application of the classical value iteration algorithm (i.e., for Q∗,Ω) and the classical robust value iteration algorithm (i.e., for Q∗,Ωξ∗ 
) respectively. This allows to get thresholds on admissible Q-values during the process. However, explicitly characterizing the uncertainty sets Ξα(s, a) ⊆ B(s, a) using these bounds is intractable, as it would require solving a complete robust planning problem for each candidate perturbed transition model. 
Rather, we adopt an incremental process in our proposed algorithm 2, that employs a two-timescale stochastic approximation (Borkar, 1997), in order to craft attacks that lie in the convex core Bα of Ξα (see section 2.3), by progressively tuning admissible magnitudes of attacks throughout the process, starting with all magnitudes η(s, a) set to ηB. On the fast timescale, Q-values are updated, with a decreasing rate ck, using a robust Bellman operator restricted to transition kernels within distance η(s, a) of the nominal dynamics (given a specific metric d(., P ) regarding nominal dynamics P ). On the slow timescale, the admissible magnitudes η(s, a) are adjusted so as to enforce the α-reward-preserving constraint defined by Q̂α(s, a). At each step, every η(s, a) is updated with quantity βk∆η(s,a), with βk a decreasing learning rate and ∆η(s,a) the update direction. In algorithm 2, we set ∆η(s,a) = −1 if the attack for (s, a) is too strong regarding the threshold Q̂α (i.e., the result of the robust bellman operator with magnitude η(s, a) is lower than Q̂α) and ∆η(s,a) = −1 otherwise. 
This separation of timescales allows the Q-iterates to track, almost surely, the fixed point of the robust Bellman operator corresponding to quasi-static values of η, while η is progressively tuned to identify the largest admissible subset of B compatible with α-reward preservation. 
The stepsizes (ck) and (βk) are chosen to satisfy the Robbins–Monro conditions (Robbins & Monro, 1951), with an explicit two-timescale separation: 
∑ k 
ck =∞, ∑ k 
c2k <∞, ∑ k 
βk =∞, ∑ k 
β2 k <∞, 
βk ck → 0. 
A canonical choice is ck = k−τQ , βk = k−τη , 
with 1/2 < τQ < τη ≤ 1. Such two-timescale schemes are standard in stochastic approximation and reinforcement learning (Borkar, 1997; Konda & Tsitsiklis, 1999). Under these conditions, the fast-timescale recursion sees η(s, a) as quasi-static, and the Q-updates track the fixed point of the robust Bellman operator associated with the current admissible radius η(s, a). Conversely, the slow-timescale recursion for η(s, a) sees the Q-values as essentially equilibrated, and adjusts the admissible attack magnitude so as to satisfy the α-reward-preservation constraints. 
Because of the nonlinear and nonconvex mapping η 7→ Q∗,η (arising from the argmin over adversarial transitions and the max over actions), global convergence cannot be guaranteed. However, by classical results on two-timescale stochastic approximation (Borkar & Borkar, 2008), the joint iterates (Qk, ηk) converge to locally stable equilibria, corresponding to solutions that satisfy the α-reward-preserving constraints. While we do not claim global optimality, these locally stable solutions ensure that the resulting policy respects the desired fraction of reward preservation and adapts to safer regions of the state-action space. 
20
Reward-Preserving Attacks For Robust Reinforcement Learning 
Algorithm 2 α-reward-preserving Robust Value Iteration with r(s, a, s′) and action-value function Q 
Require: State space S , action space A, reward r(s, a, s′), nominal MDP Ω, uncertainty set B(s, a), discount γ, preservation rate α, scheduled magnitude learning rates βk, scheduled Q update rates ck. 
Ensure: Robust α-reward-preserving Q-function Q∗,Ωξ∗α 
1: Compute Q∗,Ω using classical Value Iteration until convergence 2: Compute Q∗,Ωξ∗ 
using Robust Value Iteration until convergence 3: Define α-reward-preserving uncertainty sets Ξα(s, a) ⊆ B(s, a) implicitly, by computing the thresholds: 4: 
Q̂α(s, a) = (1− α)Q∗,Ωξ∗ 
(s, a) + αQ∗,Ω(s, a) 
5: Initialize Q(s, a)← 0 for all (s, a) 6: Initialize η(s, a)← ηB for all (s, a) 7: for each iteration k = 0, 1, 2, . . . do 8: for each state s ∈ S do 9: for each action a ∈ A do 
10: Compute worst-case expected Q over uncertainty sets of radius η(s, a): 11: Qnew(s, a)← min 
P ξ∈B(s,a) 
d(P ξ,P )≤η(s,a) 
∑ s′ P ξ(s′ | s, a) 
[ r(s, a, s′) + γmax 
a′ Q(s′, a′) 
] 12: ∆η(s,a) ← +1 
13: if Qnew(s, a) < Q̂α(s, a) then 14: ∆η(s,a) ← −1 15: end if 16: η(s, a)← η(s, a) + βk∆η(s,a) 
17: end for 18: end for 19: Update Q(s, a)← Q(s, a) + ck 
( Qnew(s, a)−Q(s, a) 
) for all (s, a) 
20: end for 21: return Q 
A.5. Robust Value Iteration and α-reward-preserving RVI via Sinkhorn in Gridworlds 
This section details the experimental setting used to produce figure 1, in particular the way worst-case attacks are computed over each uncertainty set in our experimental design for dynamics attacks in the tabular setting with known nominal dynamics. The environment is a deterministic discrete Gridworld where the agent navigates from the bottom-left corner to the upper-left corner, receiving a reward +1, while avoiding terminal states with reward −1 along its path. 
We consider a robust Markov Decision Process (RMDP) on this environment, under uncertainty in the transition dynamics, modeled via a Wasserstein ball of radius ηB around the nominal distribution. 
Classical Robust Minimization. For each state-action pair (s, a), the robust Q-value is defined by minimizing the expected return over all admissible distributions in the uncertainty set: 
Qrobust(s, a) = min P ξ∈B(s,a) 
∑ s′ 
P ξ(s′|s, a) [ r(s, a, s′) + γmax 
a′ Q(s′, a′) 
] , (8) 
subject to d(P ξ, P ) ≤ η(s, a), (9) 
where d(P ξ, P ) is the Wasserstein-2 distance with squared Euclidean transport costs between successor states. 
While this formulation directly captures the worst-case expectation, it is computationally challenging: multiple distributions may achieve the same minimal value, leading to discontinuities and instability in iterative algorithms. 
Approximate Optimization via Entropic Sinkhorn. To address this issue, we replace the classical robust minimization with a smooth entropic-regularized optimal transport problem. For each state-action pair (s, a), the worst-case transition 
21
Reward-Preserving Attacks For Robust Reinforcement Learning 
distribution is approximated by solving the following optimization over transport plans: 
π∗ = argmin π≥0 
∑ s′,s′′ 
π(s′, s′′) [ V ′ + ωD(s′, s′′) 
] − λ 
∑ s′,s′′ 
π(s′, s′′) log π(s′, s′′) 
s.t. ∑ s′ 
π(s′, s′′) = p0(s ′′|s, a), 
(10) 
where π(s′, s′′) is the transport plan from s′′ to s′ and V ′ = r(s, a, s′) + γV (s′), p0(·|s, a) is the nominal transition distribution, D is the squared Euclidean distance between successor states, λ > 0 is the entropic regularization parameter, and ω = 1/η(s, a) controls the strength of the transport cost. 
The resulting worst-case transition distribution is given by the first marginal of the optimal transport plan: 
p∗(s′|s, a) = ∑ s′′ 
π∗(s′, s′′). (11) 
This formulation yields a smooth approximation of the original Wasserstein-robust minimization, avoiding discontinuities caused by multiple equivalent worst-case distributions while still favoring transitions toward low-value successor states. 
Sinkhorn Iterations. The entropic optimal transport problem is solved via the classical Sinkhorn algorithm. Let 
K = exp(−ωD/λ) (12) 
be the entropic transport kernel, and w = exp(−V/λ) (13) 
encode the influence of the value function on the final distribution. 
The algorithm introduces two multiplicative vectors u and v to enforce the marginal constraints and incorporate the value weighting: 
 v adjusts the plan to satisfy the fixed nominal marginal p0 (i.e., the distribution from which the mass originates), 
 u adjusts the plan to produce a final marginal weighted by V , yielding the soft-min distribution. 
Starting from u = 1 and v = 1, the updates are iterated as 
u← w 
Kv + ϵ , (14) 
v ← p0 K⊤u+ ϵ 
, (15) 
where ϵ > 0 prevents division by zero. After convergence, the robust transition distribution is recovered as the first marginal of the transport plan: 
p∗ = u · (Kv)∑ s′ u · (Kv) 
. (16) 
Intuitively, the alternating updates of u and v ensure that p∗ both respects the nominal distribution p0 and shifts probability mass toward low-value successor states, while maintaining smoothness due to the entropic regularization. 
Finally, this p∗ distribution is the transition kernel used in the robust Bellman operators in algorithms 1 and 2. 
A.6. Properties of α-Reward-Preserving MDPs 
Property 3 Reward Structure Preservation Suppose that for a sufficiently large uncertainty set B, Q∗,ξ∗ is equal to a given constant minimal value Rmin for every state s ∈ S and action a ∈ A(s) (i.e., the worst-case attacks fully destroy the reward signal). In that setting, worst-case α-reward-preserving attacks preserve the structure of the reward: ∀((s, a), (s′, a′)) ∈ (S × A)2 : Q∗,Ω(s, a) > Q∗,Ω(s′, a′) =⇒ Q∗,Ωξ∗α (s, a) > Q∗,Ωξ∗α (s′, a′) 
22
Reward-Preserving Attacks For Robust Reinforcement Learning 
Proof. Assuming that for a given large uncertainty set B, the worst case attack fully destroys the reward signal. That is, Q∗,ξ∗(s, a) = Rmin for every state s ∈ S and action a ∈ A(s). In that setting, we get for every s ∈ S and a ∈ A(s) that: 
Ξα(s, a) := { ξ ∈ B(s, a) : 
Q∗,Ωξ 
(s, a) ≥ Q∗,Ωξ∗ 
(s, a) + α ( Q∗,Ω(s, a)−Q∗,Ωξ∗ 
(s, a) )} 
, 
can be rewritten as: 
Ξα(s, a) := { ξ ∈ B(s, a) : Q∗,Ωξ 
(s, a) ≥ Rmin + α ( Q∗,Ω(s, a)−Rmin 
)} , 
Let us define for any (s, a): 
Q̂(s, a) := Q∗,Ωξ∗ 
(s, a) + α ( Q∗,Ω(s, a)−Q∗,Ωξ∗ 
(s, a) ) 
. 
Contrary to the general case where we cannot guarantee that there exists an attack ξα from Ξα that respects Q∗,Ωξ 
(s, a) = 
Q̂(s, a) for any (s, a), we show below that this is the case when Q∗,Ωξ∗ 
(s, a) = Rmin. 
In that setting we have for any (s, a): 
Q̂(s, a) = Q∗,Ωξ∗ 
(s, a) + α ( Q∗,Ω(s, a)−Q∗,Ωξ∗ 
(s, a) ) 
= Rmin+ α ( Q∗,Ω(s, a)−Rmin 
) = (1− α)Rmin+ αQ∗,Ω(s, a) 
Thus, we have: Q∗,Ω = (Q̂(s, a) − (1 − α)Rmin)/α, and thus, using the fixed point property of the optimal bellman operator for Q∗,Ω: 
Q̂(s, a) = (1− α)Rmin+ αEs′∼Ω 
[ R(s, a, s′) + γmax 
a′ Q∗,Ω(s′, a′) 
] = (1− α)Rmin+ αEs′∼Ω 
[ R(s, a, s′) + γmax 
a′ 
(Q̂(s′, a′)− (1− α)Rmin) α 
] = (1− α)(1− γ)Rmin+ Es′∼Ω 
[ αR(s, a, s′) + γmax 
a′ Q̂(s′, a′) 
] = Es′∼Ω 
[ R̂α(s, a, s 
′) + γmax a′ 
Q̂(s′, a′) ] 
where R̂α(s, a, s′) := αRα(s, a, s ′) + (1 − α)(1 − γ)Rmin. Thus, the use of an α-reward-preserving attack in large B 
comes down to acting in the nominal MDP with rescaled rewards. 
Since Q̂(s, a) is the lower bound of the Q-value for any ξ ∈ Ξα, and since it can be reached for all (s, a) using iterative classical bellman updates using rescaled rewards for γ ∈ [0; 1), we can state that all ξ∗α ∈ Ξ∗,∗ 
α (s, a) respect Q∗,Ωξ∗α (s, a) = Q̂(s, a). 
To conclude, we can remark that the reward rescaling R̂α is the same for any (s, a). Thus, if for any pair (s, a) and (s′, a′) 
we have that Q∗,Ω(s, a) > Q∗,Ω(s′, a′), we also have Q̂(s, a) > Q̂(s′, a′), or equivalently Q∗,Ωξ∗α (s, a) > Q∗,Ωξ∗α (s′, a′). 
For sufficiently large sets B, α-reward-preserving attacks preserve the structure of the reward. There exists an optimal policy for Ωξ 
∗ α that is also the optimal policy for the nominal MDP Ω. 
Property 4 Condition for Preferred State–Action Change Consider two state–action pairs (s, a) ∈ S × A(s) and (s′, a′) ∈ S × A(s′). Assume that, in the nominal MDP Ω, (s, a) is preferred to (s′, a′), i.e., dΩ((s, a), (s, a′)) := Q∗,Ω(s, a)−Q∗,Ω(s′, a′) > 0. Under any worst-case α-reward-preserving attack ξ∗α defined for a given uncertainty set B, 
23
Reward-Preserving Attacks For Robust Reinforcement Learning 
the preference is reversed — namely, (s′, a′) becomes preferred to (s, a) (i.e., Q∗,Ωξ∗α (s′, a′) > Q∗,Ωξ∗α (s, a)) — if and only if 
dΩξ∗ ((s′, a′), (s, a)) > α 
1− α dΩ((s, a), (s 
′, a′)) + δ((s′, a′), (s, a)), 
where dΩξ∗ ((s′, a′), (s, a)) := Q∗,Ωξ∗ 
(s′, a′) − Q∗,Ωξ∗ 
(s, a), and δ((s′, a′), (s, a)) := (ϵs′,a′−ϵs,a) 
1−α , with ϵs,a the gap 
between Q∗,Ωξ∗α (s, a) and its α-reward-preserving lower-bound Q̂(s, a) := (1− α)Q∗,Ωξ∗α (s, a) + αQ∗,Ω(s, a). Defining the total-variation diameter of B at any (s, a) by ηB, standard Lipschitz bounds imply δ((s′, a′), (s, a)) = O(ηB). While δ((s′, a′), (s, a))→ 0 as ηB → 0, the actual variation of Q∗,Ωξ∗ 
(s, a) can be amplified by local gaps in successor actions, so δ variations may be dominated by the effective sensitivity of Q in “dangerous” zones, which induce preference changes under α-reward-preserving attacks. 
Proof. By definition of an α-reward-preserving attack ξ∗α, we have for any state-action pair (x, u): 
Q∗,Ωξ∗α (x, u) ≥ Q̂(x, u) := (1− α)Q∗,Ωξ∗ 
(x, u) + αQ∗,Ω(x, u). 
Define the gap 
ϵx,u := Q∗,Ωξ∗α (x, u)− Q̂(x, u) ≥ 0. 
Consider two state-action pairs (s, a) and (s′, a′). Let 
δ((s′, a′), (s, a)) := ϵs′,a′ − ϵs,a 
1− α . 
The preference of (s′, a′) over (s, a) under ξ∗α is expressed as 
Q∗,Ωξ∗α (s′, a′) > Q∗,Ωξ∗α 
(s, a). 
Using the definition of ϵ and Q̂, we can rewrite this as 
Q̂(s′, a′) + ϵs′,a′ > Q̂(s, a) + ϵs,a. 
Subtracting Q̂(s, a) from both sides and rearranging terms gives 
Q̂(s′, a′)− Q̂(s, a) > ϵs,a − ϵs′,a′ = −(ϵs′,a′ − ϵs,a) = −(1− α)δ((s′, a′), (s, a)). 
By definition of Q̂, we have 
Q̂(s′, a′)− Q̂(s, a) = (1− α) ( Q∗,Ωξ∗ 
(s′, a′)−Q∗,Ωξ∗ 
(s, a) ) + α 
( Q∗,Ω(s′, a′)−Q∗,Ω(s, a) 
) . 
Let dΩ := Q∗,Ω(s, a)−Q∗,Ω(s′, a′) > 0. Then 
Q∗,Ω(s′, a′)−Q∗,Ω(s, a) = −dΩ. 
Plugging this in gives 
(1− α) ( Q∗,Ωξ∗ 
(s′, a′)−Q∗,Ωξ∗ 
(s, a) ) − αdΩ > −(1− α)δ((s′, a′), (s, a)). 
Dividing both sides by (1− α) yields the stated condition: 
dΩξ∗ ((s′, a′), (s, a)) > α 
1− α dΩ((s, a), (s 
′, a′)) + δ((s′, a′), (s, a)). 
24
Reward-Preserving Attacks For Robust Reinforcement Learning 
The following of the proof relies on the decomposition of ϵs,a relative to the linear lower-bound Q̂: 
ϵs,a = Q∗,Ωξ∗α (s, a)− Q̂(s, a) = (1− α) 
( Q∗,Ωξ∗α 
(s, a)−Q∗,Ωξ∗ 
(s, a) ) + α 
( Q∗,Ωξ∗α 
(s, a)−Q∗,Ω(s, a) ) . 
Each term measures the sensitivity of the robust Q-value under ξ∗α to changes in transitions (or observations) compared to the reference MDPs. Using standard results (e.g., from (Wiesemann et al., 2013)): 
|Q∗,Ωξ∗α −Q∗,Ωξ∗ 
| ≤ L1ηB, |Q∗,Ωξ∗α −Q∗,Ω| ≤ L2ηB, 
where the constants L1, L2 depend on Rmax, γ, and the propagation of the max over successors. Therefore, 
|ϵs,a| ≤ (1− α)L1ηB + αL2ηB = O(ηB). 
Consequently, 
δ((s′, a′), (s, a)) = ϵs′,a′ − ϵs,a 
1− α = O(ηB), 
and δ((s′, a′), (s, a))→ 0 as ηB → 0. 
Remark: The bound holds for attacks on transitions (SA-rectangular), on observations, or combined, as long as ηB correctly measures the total-variation diameter of the perturbed distributions. For non-SA-rectangular transition sets, the same order-of-magnitude bound remains an approximation; correlations between state-action perturbations may amplify the effective variation of Q, so δ can underestimate local sensitivity in “dangerous zones.” 
A.7. Approximated Reward-Preserving Robust Deep RL Algorithms 
This section presents the complete robust training procedures proposed in this work, for both dynamics and observation attacks, following all the main steps described in section 3 of the paper, and used for our experiments. 
25
Reward-Preserving Attacks For Robust Reinforcement Learning 
Algorithm 3 α-Reward-Preserving Training (on dynamics) 
Require: Environment with unknown dynamics Ω; Maximal attack magnitude ηB; Reward preservation rate α; Protagonist agent πθ; discount γ; Dynamic Q-network Qψα ; Static Q-network Qψc ; Tail of the magnitude distribution ϵ; Capacity of the replay buffer c; Number of cycles nb cycles; Batch size bsize; Number of steps nsteps; Number of Q updates per cycle nQiter; Attack direction crafter ξAπ̃ ; Polyak update parameters τπ and τQ; Learning rates βπ and βQ. 
1: θ̃ ← copy(θ) // Reference policy π̃ 2: ψ̂α ← copy(ψα) // Target Dynamic Q-network Qπ̃α 3: ψ̂c ← copy(ψc) // Target Static Q-network Qπ̃c 4: Initialize buffer B ← ∅ 5: for each nb cycles cycles do 6: // Collect nsteps transitions in Ωξα 
7: s′ ← first state from Ω 8: for nsteps environment interactions do 9: s← s′ 
10: Sample a ∼ πθ(· | s) 11: // α-reward-preserving set 12: Define B̃ηα(s, a) using (4) with Qψα and Qψc 
13: η∗(s, a)← arg min η∈B̃η 
α(s,a) Qπ̃α((s, a), η) 
14: λ← − log(ϵ)/η∗(s, a) 15: Sample η ∼ pπ̃α(· | s, a) ∝ λe−λη 16: Craft attack direction A← ξAπ̃ (s, a) for π̃ 17: (s′, r, done)← Ωξ=(η,A)(s, a) // Perform adversarial step 18: B ← B ∪ {(s, a, η, A, r, s′, πθ(a | s))} 19: end for 20: Improve πθ on new transitions using any RL algorithm (e.g., SAC) 21: for nQiter iterations do 22: Sample a batch {(si, ai, ηi, Ai, ri, s′i, pi)}bsizei=1 from B 23: Sample next actions {a′i ∼ πθ̃(· | si)}bsizei=1 
24: {wi}bsizei=1 ← { πθ̃(ai|si) 
pi }bsizei=1 // Importance Sampling Weights 
25: {δαi }bsizei=1 ← {Qψα ((si, ai), ηi)− ri − γEη′i 
[ Qψ̃α 
((s′i, a ′ i), η 
′ i) ] }bsizei=1 
26: {δci }bsizei=1 ← {Qψc((si, ai), ηi)− ri − γQψ̃c ((s′i, a 
′ i), ηi)}bsizei=1 
27: ψα ← ψα − βQ ∑bsize i=1 ∇ψαwi(δ 
α i ) 
2 
28: ψc ← ψc − βQ ∑bsize i=1 ∇ψcwi(δ 
c i ) 
2 
29: end for 30: θ̃ ← (1− τπ) θ̃ + τπ θ // Polyak update of π̃ 31: ψ̂α ← (1− τQ) ψ̂α + τQ ψα // Polyak update of Qπ̃α 32: ψ̂c ← (1− τQ) ψ̂c + τQ ψc // Polyak update of Qπ̃c 33: end for 34: return Q 
26
Reward-Preserving Attacks For Robust Reinforcement Learning 
Algorithm 4 α-Reward-Preserving Training (on observations) 
Require: Environment with unknown dynamics Ω; Maximal attack magnitude ηB; Reward preservation rate α; Protagonist agent πθ; discount γ; Dynamic Q-network Qψα ; Static Q-network Qψc ; Tail of the magnitude distribution ϵ; Capacity of the replay buffer c; Number of cycles nb cycles; Batch size bsize; Number of steps nsteps; Number of Q updates per cycle nQiter; Attack direction crafter ξAπ̃ ; Polyak update parameters τπ and τQ; Learning rates βπ and βQ. 
1: θ̃ ← copy(θ) // Reference policy π̃ 2: ψ̂α ← copy(ψα) // Target Dynamic Q-network Qπ̃α 3: ψ̂c ← copy(ψc) // Target Static Q-network Qπ̃c 4: Initialize buffer B ← ∅ 5: for each nb cycles cycles do 6: // Collect nsteps transitions in Ωξα 
7: s′ ← first state from Ω 8: for nsteps environment interactions do 9: s← s′ 
10: // α-reward-preserving set 11: Define B̃ηα(s) using (4) with Qψα and Qψc 
12: η∗(s)← arg min η∈B̃η 
α(s) Qπ̃α((s, a), η) 
13: λ← − log(ϵ)/η∗(s) 14: Sample η ∼ pπ̃α(· | s, a) ∝ λe−λη 15: Craft attack direction A← ξAπ̃ (s, a) for π̃ 16: Sample a ∼ πθ(· | ϕ(s) + ηA) 17: s′, r, done← Ωξ=(η,A)(s) // Perform adversarial step 18: B ← B ∪ {(s, a, η, A, r, s′, πθ(a | ϕ(s) + ηA))} 19: end for 20: Improve πθ on new transitions using any RL algorithm (e.g., SAC) 21: for nQiter iterations do 22: Sample a batch {(si, ai, ηi, Ai, ri, s′i, pi)}bsizei=1 from B 
23: {wi}bsizei=1 ← { πθ̃(ai|ϕ(si) + ηiAi) 
pi }bsizei=1 // Importance Sampling Weights 
24: {δαi }bsizei=1 ← {Qψα (si, ηi)− ri − γEη′i 
[ Qψ̃α 
(s′i, η ′ i) ] }bsizei=1 
25: {δci }bsizei=1 ← {Qψc (si, ηi)− ri − γQψ̃c 
(s′i, ηi)}bsizei=1 
26: ψα ← ψα − βQ ∑bsize i=1 ∇ψα 
wi(δ α i ) 
2 
27: ψc ← ψc − βQ ∑bsize i=1 ∇ψc 
wi(δ c i ) 
2 
28: end for 29: θ̃ ← (1− τπ) θ̃ + τπ θ // Polyak update of π̃ 30: ψ̂α ← (1− τQ) ψ̂α + τQ ψα // Polyak update of Qπ̃α 31: ψ̂c ← (1− τQ) ψ̂c + τQ ψc // Polyak update of Qπ̃c 32: end for 33: return Q 
27