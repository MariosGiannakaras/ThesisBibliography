> Source: https://arxiv.org/pdf/2602.12444

Safe Reinforcement Learning via Recovery-based Shielding with Gaussian Process Dynamics Models 
Alexander W. Goodall 
Imperial College London, Department of Computing 
London, United Kingdom 
a.goodall22@imperial.ac.uk 
Francesco Belardinelli 
Imperial College London, Department of Computing 
London, United Kingdom 
francesco.belardinelli@imperial.ac.uk 
ABSTRACT Reinforcement learning (RL) is a powerful framework for optimal 
decision-making and control but often lacks provable guarantees 
for safety-critical applications. In this paper, we introduce a novel 
recovery-based shielding framework that enables safe RL with a 
provable safety lower bound for unknown and non-linear continu-
ous dynamical systems. The proposed approach integrates a backup 
policy (shield) with the RL agent, leveraging Gaussian process (GP) 
based uncertainty quantification to predict potential violations of 
safety constraints, dynamically recovering to safe trajectories only 
when necessary. Experience gathered by the ‘shielded’ agent is 
used to construct the GP models, with policy optimization via in-
ternal model-based sampling – enabling unrestricted exploration 
and sample efficient learning, without compromising safety. Em-
pirically our approach demonstrates strong performance and strict 
safety-compliance on a suite of continuous control environments. 
KEYWORDS Safe Control; Reinforcement Learning; Gaussian Process 
1 INTRODUCTION Safe reinforcement learning (RL) [22] is an active research area 
focused on training policies that strictly respect safety constraints 
during both learning and deployment. In high-stakes domains like 
robotics, autonomous driving, and healthcare, adhering to safety 
constraints is crucial, as even a single policy failure can lead to 
catastrophic consequences [5]. Provably safe RL [36] is a promis-
ing paradigm for these safety-critical settings, aiming to provide 
formal guarantees on an agent’s performance. Such guarantees 
typically fall into two categories: probabilistic guarantees or hard (deterministic) guarantees. Probabilistic approaches leverage either 
known stochastic models of the environment [34, 59] or learned 
models of the environment to verify safety with high confidence 
[12, 25, 63], whereas hard-guarantee approaches incorporate strong 
prior knowledge (e.g. exact system dynamics or formal abstractions) 
to ensure absolute constraint satisfaction [3, 11]. Despite substantial 
progress, ensuring safety in unknown or uncertain environments re-
mains highly challenging – existing methods often rely on idealized 
assumptions or suffer from scalability issues. 
A widely-used paradigm for enforcing safety at runtime is shielding [3, 13]. In this paradigm, each action proposed by the RL agent 
is checked against safety constraints before execution; if an action 
is deemed unsafe, it is overridden by a backup (safe) action that 
keeps the system within a designated safe set. The backup policy is 
typically a simpler, trusted controller that ensures the state remains 
in an operationally safe region. This scheme allows the learned pol-
icy to operate freely when far from danger, and invokes the backup 
policy only near the boundary of the safe region. An important 
benefit of shielding is that formal guarantees can be obtained by 
verifying the backup policy (which is designed for safety) instead 
of the learned policy, greatly simplifying the verification burden, if 
for example, the backup policy is simpler (e.g., linear controller). 
In the context of continuous control, shielding has been used 
in many prior works [8, 10, 11, 38, 60] and even extended to high-
dimensional visual-input scenarios [24]. Model Predictive Shield-ing (MPS) [10] is a classic example of this approach: it combines 
a stabilizing linear controller with a recovery strategy to verify 
“recoverable” safe states on-the-fly. MPS demonstrated that high-
performance RL is achievable with a safety net, but it also high-
lighted key limitations of prior shielding methods. Notably, MPS 
(and extensions thereof, e.g., Robust MPS [38], Dynamic MPS [8]) assumes the environment is known and deterministic; or relies on 
heuristics that break safety guarantees [38]. For stochastic systems, 
Statistical MPS [11], uses samples from a known stochastic model 
of the environment, for high levels of safety, these sampling based 
approaches scale poorly and loose any meaningful guarantees. For-
mal methods based on Hamilton-Jacobi (HJ) reachability analysis 
[2] compute invariant safe sets for continuous control tasks and 
use them to enforce safety via action replacement. While HJ-based 
approaches [21, 58] provide strong safety guarantees they scale 
exponentially in the state dimension, making them impractical for 
high-dimensional systems [39]. Other approaches to safe RL may 
encode safety as a constraint in the learning objective, e.g., via 
Constrained Markov Decision Process (CMDP) [4], however these 
methods only guarantee constraint satisfaction in expectation and 
are unsuitable for highly safety-critical domains [57]. 
Contributions. In this paper we deal with some of the limitations 
highlighted above; we introduce a novel recovery-based shielding framework for safe RL with a provable lower bound on safety 
probability. We summarize our key contributions as follows: 
(1) We combine shielding with online model learning, where 
the unknown dynamics of the system are and modelled directly via 
Gaussian process (GP) dynamics models [19], and a pre-computed 
safe backup policy is used to intervene on the agent’s actions only 
when necessary. Our method does not require full knowledge of 
the system’s dynamics, assuming only an initial backup controller, 
invariant set and standard smoothness conditions on the dynamics. 
(2) We leverage analytic GP uncertainty estimates to predict po-
tential constraint violations in advance, forgoing sampling entirely, 
and analytically verifying actions on-the-fly. This design enables 
provable safety guarantees up to an arbitrary level of safety without 
additional computational burden. 
(3) We provide a concrete proof that our shielded RL agent main-
tains safety with high probability throughout learning and after 
 
 
 
 
 
 
 
 
 
 
proper calibration of the GP dynamics model (which is often quick, 
both in theory and in practice). In particular, we establish a formal 
lower bound on the probability of constraint satisfaction at all times, 
subject to the usual regularity assumptions for GP-based learning. 
(4) We evaluate our approach on a suite of continuous control 
environments. The results show that our method can learn high-
performing policies while strictly respecting safety constraints, 
outperforming a variety of baseline safe RL techniques in terms of 
both safety (zero constraint violations) and reward optimization. 
2 PRELIMINARIES We consider discrete time non-linear continuous-state dynamical systems, with both observation noise and bounded disturbances 
[32], 
𝑥 (𝑡 + 1) = 𝑓 (𝑥 (𝑡), 𝑢 (𝑡),𝑤 (𝑡)) (1) 
where 𝑥 (𝑡) ∈ R𝑛 is a system state, 𝑢 (𝑡) ∈ R𝑚 is a control input or action, and𝑤 (𝑡) ∈ R𝑘 is a system disturbance, and 𝑓 : R𝑛+𝑚+𝑘 → R𝑛 
is an unknown Lipschitz continuous transition function. We let X ⊆ R𝑛 denote the state constraints,U ⊆ R𝑚, denote the 
control constraints, andW ⊆ R𝑘 denote the set of disturbances. The disturbances are can be drawn from an arbitrary distribution PW but the support is assumed to be bounded and known. Furthermore, 
we denote X0 ⊂ X as the set of initial system states. The observed 
system state 𝑥 (𝑡) ∈ R𝑛 is subject to observation noise 𝑣 (𝑡) ∈ R𝑛 , such that, 𝑥 (𝑡) = 𝑥 (𝑡)+𝑣 (𝑡), we assume that that 𝑣 (𝑡) is drawn from the multivariate Gaussian distribution PV =N(0, Σ), where Σ = 
diag( [𝜎2 
1 , . . . , 𝜎2 
𝑛]) ∈ R𝑛×𝑛 and 𝜎2 
1 , . . . 𝜎2 
𝑛 are known noise variances 
for each state dimension (e.g., small sensor noise). 
2.1 Problem setup Safety semantics. We formalize the safety semantics of our frame-
work using a flexible class of state constraints. Let X ⊆ R𝑛 be the state space and Xsafe ⊆ X the admissible (safe) set. We consider 
four basic constraint types: 
 Box constraints. Each dimension 𝑖 of the state vector 𝑥 ∈ R𝑛 is bounded by an interval [𝑎𝑖 , 𝑏𝑖 ]: 
Xbox = {𝑥 ∈ R𝑛 : 𝑎𝑖 ≤ 𝑥𝑖 ≤ 𝑏𝑖 , ∀𝑖 = 1, . . . , 𝑛} (2) 
 Convex hull constraints.More generally, the safe set may be 
defined as a convex polytope represented by a finite set of ℓ linear 
inequalities, where 𝐴 ∈ Rℓ×𝑛 and 𝑏 ∈ Rℓ : 
Xhull = {𝑥 ∈ R𝑛 : 𝐴𝑥 ≤ 𝑏} (3) 
 Inclusion (boundary) constraints. For either box or convex hull regions, wemay require that the state remains inside the region, 
i.e. 𝑥 (𝑡) ∈ Xincl ⊆ R𝑛 . 
 Exclusion (obstacle) constraints. To represent obstacles, we 
may require that the state avoids certain forbidden sets Xobs, such as boxes or convex hulls. Formally, 
Xexcl = X \ Xobs (4) 
The overall safe set Xsafe, is then defined as the intersection of 
inclusion constraints and the complement of exclusion constraints. 
This naturally yields non-convex feasible regions, e.g. by combining 
multiple disjoint polytopes with obstacle regions removed. 
Safe RL objective. We consider a deterministic reward function 𝑅 : X×U×X → R and a discount factor 𝛾 ∈ [0, 1). LetΠ be the set of 
all policies, where 𝜋 ∈ Π is a function from system states to actions 
𝜋 : X → U. The goal is to maximize an objective function 𝐽 (𝜋), while ensuring that, from any initial state 𝑥 (0) ∈ X0 ⊆ Xsafe and for any sequence of disturbances ®𝑤 = (𝑤 (0),𝑤 (1), . . .) ∈ W∞ 
and 
noise ®𝑣 = (𝑣 (0), 𝑣 (1), . . .) ∈ V∞, we have 𝑥 (𝑡) ∈ Xsafe, for all 𝑡 = 0, 1, . . ., where 𝑥 (𝑡 + 1) = 𝑓 (𝑥 (𝑡), 𝜋 (𝑥 (𝑡)),𝑤 (𝑡)), and 𝑤 (𝑡) ∼ PW and 𝑣 (𝑡) ∼ PV are drawn i.i.d. In this paper we consider the usual 
objective of expected discounted return: 𝐽 (𝜋) = E𝜋 [∑∞ 
𝑡=0 𝛾𝑡𝑟 (𝑡) 
] , if 
we denote Πsafe ⊆ Π as the set of all safe policies, then our goal is 
to find a policy 𝜋∗ = arg max𝜋 ∈Π safe 
𝐽 (𝜋). Safety is enforced with high-probability due to the unavoid-
able observation noise, state disturbances and epistemic GP uncer-
tainty. We adopt of the notion of 𝜖-safe policies [11]. Concretely, 
let 𝜉 (𝑥 (0), 𝜋, ®𝑤, ®𝑣) = (𝑥 (0), 𝑥 (1), . . .) ∈ X∞ denote a sequence of 
system states under policy 𝜋 and from state 𝑥 (0) ∈ X0, then, 
Definition 2.1 (𝜖-safe policy). A policy 𝜋 ∈ Π is 𝜖-safe if, 
P ®𝑤∼PW ,®𝑣∼PV (𝜉 (𝑥 (0), 𝜋, ®𝑤, ®𝑣) ⊆ Xsafe) ≥ 1 − 𝜖 ∀𝑥 (0) ∈ X0 
The admissible safe policy set Πsafe therefore consists of all 𝜖-
safe policies from the initial states, this is the standard requirement 
introduced in prior works [11]. 
2.2 Dynamics modelling For modelling the unknown dynamics of the system 𝑓 we use 
the same methodology as PILCO [19]. The dynamics model is im-
plemented as a Gaussian process (GP) model with input 𝑥 (𝑡) = (𝑥 (𝑡), 𝑢 (𝑡)) ∈ X×U and output targets Δ(𝑡) = 𝑥 (𝑡) −𝑥 (𝑡 −1) ∈ R𝑛 which model the next step deltas. The GP model provides the fol-
lowing one-step predictions, 
𝑝 (𝑥 (𝑡) | 𝑥 (𝑡 − 1), 𝑢 (𝑡 − 1)) =N(𝑥 (𝑡) | 𝜇 (𝑡), Σ(𝑡)) 𝜇 (𝑡) = 𝑥 (𝑡 − 1) + E𝑓 [Δ(𝑡)] Σ(𝑡) = var𝑓 (Δ(𝑡)) 
In this paper we only consider the zero-mean prior function and 
radial basis function (RBF) kernel, whose covariance is given by, 
𝑘 (𝑥 (·), 𝑥 ′ (·)) = 𝛼2 exp 
( −1 
2 
(𝑥 (·) − 𝑥 ′ (·))𝑇Λ(𝑥 (·) − 𝑥 ′ (·)) ) 
where 𝛼2 models the variance of the transition function 𝑓 , and Λ = 
diag( [𝑙2 1 , . . . 𝑙2𝑛]) corresponds to the length-scales 𝑙𝑖 for automatic 
relevance determination. The posterior hyperparameters, which 
include the signal variance 𝛼2 , length scales 𝑙𝑖 and noise variances 
Σ𝜀 , are trained by evidence maximization [45]. For training and 
prediction we use GPJAX [41] a flexible library for GP implemented 
in JAX [14], which benefits from just-in-time (JIT) compilation and 
GPU compatibility. 
Let �̃� = [𝑥1 (·), . . . , 𝑥𝐷 (·)] denote the 𝐷 training inputs and 
𝑦 = [Δ1 (·), . . . Δ𝐷 (·)] denote the 𝐷 training outputs. The posterior 
predictive distribution 𝑝 (Δ(·) | 𝑥 (·)) for a known test input 𝑥 (·), is Gaussian with mean and variance given by, 
𝑚𝑓 (𝑥 (·)) = E𝑓 [Δ(·)] = 𝑘𝑇∗ (𝐾 + 𝜎2 
𝜀 I)−1𝑦 = 𝑘𝑇∗ 𝛽 (5) 
𝜎2 
𝑓 = var𝑓 (Δ(·)) = 𝑘∗∗ − 𝑘𝑇∗ (𝐾 + 𝜎2 
𝜀 I)𝑘∗ (6)
where 𝑘∗ := 𝑘 (�̃� , 𝑥 (·)), 𝑘∗∗ := 𝑘 (𝑥 (·), 𝑥 (·)), 𝛽 = (𝐾 + 𝜎2 
𝜀 I)−1𝑦 
and 𝐾 is the gram matrix with entries 𝐾𝑖 𝑗 = 𝑘 (𝑥𝑖 (·), 𝑥 𝑗 (·)). In the case where the output targets are multivariate (i.e., the state 
dimension 𝑛 > 1), we train 𝑛 conditionally independent GP models. 
Conditional independence holds for a known (deterministic) test 
input 𝑥 (·), however, the joint predicative covariance becomes non-
diagonal under uncertain inputs due to shared input uncertainty 
and cross-covariance terms, these details are covered in Sec. 4. 
3 RECOVERY-BASED SHIELDING Overview. For a candidate policy 𝜋 ∈ Π, our goal is to construct a 
shielded policy 𝜋shield that is provably 𝜖-safe. In this paper, shielding 
is implemented by carefully switching between the learned policy 
𝜋 and backup controller 𝜋backup. The “switching criterion” depends 
only on the system state and analytic safety verification conditions 
derived from the GP uncertainty sets. The key advantage is that 
safety is certified without making assumptions about the structure 
of 𝜋 ; the shield can enforce constraints even if 𝜋 is an arbitrary 
neural network policy. Formally, 𝜋shield coincides with 𝜋 whenever 
the state is judged 𝜖𝑡 -recoverable; otherwise, it defers to 𝜋backup to 
drive the system back into a verified invariant set. This separation 
makes the safety proof policy-agnostic, relying only on the backup 
controller and uncertainty analysis, as alluded to earlier this is often 
easier if the backup policy comes from a restricted policy class (e.g., 
linear controller). 
Control invariant sets. For proving infinite horizon safety for 
systems defined in terms of (1), a standard approach is to consider 
stable equilibrium points and control invariant sets. Formally, a state 
𝑥𝑒𝑞 ∈ X is a (stable) equilibrium point iff there exists 𝑢𝑒𝑞 ∈ U such 
that 𝑓 (𝑥𝑒𝑞, 𝑢𝑒𝑞, 0) = 𝑥𝑒𝑞 . A (nominal) control invariant set Xinv ⊆ X is a set of states such that if 𝑥 (·) ∈ Xinv then there exists 𝑢𝑥 ∈ U such that 𝑓 (𝑥 (·), 𝑢𝑥 , 0) ∈ Xinv. In words, the control invariant set 
is a subset of system states for which there exists corresponding 
control inputs that can keep the system within this set indefinitely. 
For simply providing safety guarantees it is enough to determine 
an invariant set Xinv for the control policy and then establish that 
Xinv ⊆ Xsafe. The computation of control invariant sets of general 
non-linear dynamics is usually based on Hamilton-Jacobi analysis 
[21, 39], which scale exponentially in the dimension of the state 
space𝑛. In this paper we consider the class of linear (or RBF) backup 
controllers, for which more scalable methods exist [26, 47]. 
Backup policy. The goal of the backup policy 𝜋backup is to drive 
the current system state 𝑥 (𝑡) ∈ X back into the control invariant 
set Xinv. Crucially the backup policy 𝜋backup should satisfy, 
𝑥 (·) ∈ Xinv ⇒ 𝜉 (𝑥 (·), 𝜋backup (𝑥 (·)), ®𝑤, ®𝑣) ⊆ Xinv (∀ ®𝑤, ®𝑣 ∈ W∞ ×V∞) 
(7) 
In this paper, we consider a Zonotope-based approach [47] pro-
vided by AROC [32] for computation of control invariant sets with 
maximum volume around a given stable equilibrium point 𝑥𝑒𝑞 . The 
corresponding backup policy 𝜋backup is constructed with Linear 
Quadratic Regulator (LQR) [6], and is defined by the feedback ma-
trix 𝐾 ∈ R𝑛×𝑛 , formally, 
𝜋backup (𝑥 (·)) = 𝑢𝑒𝑞 − 𝐾 (𝑥 (·) − 𝑥𝑒𝑞) (8) 
so that 𝜋backup satisfies, 𝑓 (𝑥𝑒𝑞, 𝜋backup (𝑥𝑒𝑞), 0) = 𝑥𝑒𝑞 . The control 
invariant set Xinv is then calculated by iteratively applying the 
control law in (8) and over-approximating the reachable sets by 
successive convexification, we refer the reader to [32, 47] for full 
details. Mathematically the control invariant set Xinv is represented as a convex polytope (or convex hull), c.f., (3) from earlier. We state 
our main assumptions here. 
Assumption. We assume privileged access to a linear backup policy 
𝜋backup; and a corresponding control invariant set Xinv for which 𝜋backup is invariant, i.e., (7) holds. 
Recoverable states. Provided that 𝑥𝑒𝑞 ∈ Xsafe and Xinv ⊆ Xsafe and ensuring that the system never leaves Xinv is sufficient for 
maintaining safety. However, since the computation of Xinv relies on convex over-approximations and linear controllers, the actual 
set of admissible states might be much larger. Rather we allow for 
states that are recoverable within some fixed time horizon 𝑁 ∈ N. Definition 3.1 (Recoverable state). For a given horizon 𝑁 , distur-
bances ®𝑤 ∈ W𝑁+1 and observation noise ®𝑣 ∈ V𝑁+1 
a state 𝑥 (·) ∈ X is recoverable if for the sequence 𝑥 (0), 𝑥 (1), . . . , 𝑥 (𝑁 ) ∈ X𝑁+1 
, 
given by, 
𝑥 (0) = 𝑥 (·) 𝑥 (𝑡) = 𝑥 (𝑡) + 𝑣 (𝑡) ∀𝑡 = 0, . . . , 𝑁 
𝑥 (1) = 𝑓 (𝑥 (0), 𝜋 (𝑥 (0)),𝑤 (𝑡)) 𝑥 (𝑡 + 1) = 𝑓 (𝑥 (𝑡), 𝜋backup (𝑥 (𝑡)),𝑤 (𝑡)) ∀𝑡 = 1, . . . , 𝑁 
we have 𝑥 (𝑡) ∈ Xsafe for all 𝑡 = 0, . . . , 𝑁 , and there exists 𝑡 ′ = 0, . . . , 𝑁 , such that 𝑥 (𝑡 ′) ∈ Xinv. 
Intuitively, a state 𝑥 (·) ∈ X is recoverable if for the control 
𝑢 (·) = 𝜋 (𝑥 (·)) determined by the learned policy 𝜋 , we can re-
cover the system state within 𝑁 timesteps (using the backup policy 
𝜋backup), back to the control invariant set Xinv (from which we have 
already established safety). Fig. 1 illustrates this phenomenon; not-
ing both the recoverable (blue) and irrecoverable (red) start outside the control invariant set Xinv and inside the box constraint Xsafe; the backup policy drives the recoverable trajectory back into the 
control invariant set Xsafe – establishing a high-probability safety 
certification, whereas the irrecoverable trajectory leaves the safe 
set Xsafe, intersecting with the explicit box constraint. 
We denote X ®𝑤,®𝑣 rec (𝑁 ) ⊆ Xsafe as the set of all recoverable states 
given ®𝑤, ®𝑣 ∈ W𝑁+1 ×V𝑁+1 and within time horizon 𝑁 . Given the 
randomness associated with the disturbances ®𝑤 and the observation 
noise ®𝑣 , it becomes challenging to check whether the current system 
state is recoverable given all possible realizations of ®𝑤 and ®𝑣 . Rather we allow for states that are recoverable with high probability. 
Definition 3.2 (𝜖-Recoverable state). For a given horizon 𝑁 ∈ N and tolerance 𝜖 ∈ [0, 1] a state 𝑥 (·) ∈ X is 𝜖-recoverable if, 
P ®𝑤∼PW ,®𝑣∼PV (𝑥 (·) ∈ X ®𝑤,®𝑣 rec (𝑁 )) ≥ 1 − 𝜖 
We denote X𝜖 rec (𝑁 ) ⊆ Xsafe as the set of 𝜖-recoverable states 
for some horizon 𝑁 . The shielded policy 𝜋shield is constructed by 
fixing a step-wise safety constraint 𝜖𝑡 ≤ 𝜖 . Therefore, we write an expression for 𝜋shield in terms of the 𝜖𝑡 -recoverable states. Formally, 
𝜋shield (𝑥 (·)) = { 𝜋 (𝑥 (·)) if 𝑥 (·) ∈ X𝜖𝑡 
rec (𝑁 ) 
𝜋backup (𝑥 (·)) otherwise 
(9)
Figure 1: 99.99%-CI uncertainty sets for recoverable (blue) and irrecoverable (red) trajectories under the backup policy for cartpole (i)/(ii) environment. 
Intuitively, if each state encountered during execution is verified 
to be 𝜖𝑡 -recoverable and the backup controller guarantees invari-
ance within its certified region, then the resulting shielded policy 
𝜋shield is 𝜖-safe. This is formalized in the following theorem. 
Theorem 3.1 (𝜖-safe policy). Assume: (i) Xinv is an invariant set for 𝜋backup, (ii) X0 ⊆ Xinv ⊆ Xsafe and (iii) 
∑𝑇 𝑡=0 
𝜖𝑡 = 𝜖 , then, 𝜋shield is 𝜖-safe for the time horizon 𝑇 ∈ N. 
Remark. The proof of Theorem 3.1 (c.f., Appendix B) is obtained by 
establishing the following invariant: “we can always return to Xinv with probability at least 1 − 𝜖𝑡 by using the backup policy 𝜋backup for 𝑁 timesteps”. After establishing this invariant (via recursive 
feasibility), a union bound over the per-step safety tolerances 𝜖𝑡 is 
then taken. In practicewe use either a constant 𝜖𝑡 ≡ 𝜖/𝑇 over a finite 
time horizon 𝑇 , or a decreasing sequence satisfying 
∑∞ 𝑡=0 
𝜖𝑡 ≤ 𝜖 .1 This permits extending the guarantee to infinite horizons while 
keeping 𝜖 arbitrarily small. 
In practice, both the recovery horizon 𝑁 and step-wise toler-
ance 𝜖𝑡 are treated as hyperparameters, the choice of 𝑁 has no 
consequences on the proof of 𝜖-safety, whereas 𝜖𝑡 directly dictates 
the theoretical safety bound that can be obtained. The choice of 
𝑁 will however, directly impact the computational overhead of 
action selection and the restrictiveness of the shield. This over-
head dominates training time when shielding is invoked at every 
timestep during training. Concrete runtime details can be found in 
Appendix F.1. We note that the overhead grows roughly linearly 
in 𝑁 for our analytic method, compared to 𝑂 (𝑁𝐾) for sampling 
baselines, where 𝐾 is the number of samples. 𝑁 should be treated 
as a compute-conservatism trade-off, smaller 𝑁 will reduce the 
overhead, but might make the shield more conservative (less time 
to return toXinv). There is usually a sweet spot, which once reached, increasing 𝑁 has no significant impact on the shield. 
1 E.g., setting 𝜖𝑡 = 𝜖/( (𝑡 + 1)2𝜋2 ) yields∑∞𝑡=0 
𝜖𝑡 ≤ 𝜖 . 
4 GP UNCERTAINTY PREDICTION As detailed in Sec. 2.2 the unknown system dynamics 𝑓 are mod-
elled using 𝑛 GP models. We now detail how the uncertainty sets 
(c.f., Fig. 1) are analytically computed and propagated through the 
dynamics model for robustly identifying 𝜖𝑡 -recoverable states (i.e., 
checking that 𝑥 (·) ∈ X𝜖𝑡 rec ). 
Prediction at uncertain inputs. We model each output dimension 
with an independent GP; when inputs are uncertain, output corre-
lations arise through uncertainty propagation (moment matching). 
In particular, the goal is to predict 𝑥 (𝑡) given 𝑝 (𝑥 (𝑡 − 1)), to do this we require the joint 𝑝 (𝑥 (𝑡 − 1), 𝑢 (𝑡 − 1)). This can be calculated by 
first integrating out the state 𝑥 (𝑡 − 1), giving mean 𝜇𝑢 (𝑡 − 1) and covariance Σ𝑢 (𝑡 − 1). The cross covariance cov[𝑥 (𝑡 − 1), 𝑢 (𝑡 − 1)] is computed and then the joint 𝑝 (𝑥 (𝑡 − 1)) = 𝑝 (𝑥 (𝑡 − 1), 𝑢 (𝑡 − 1)) is approximated as a Gaussian with correct mean �̃� (𝑡 − 1) and co-
variance Σ̃(𝑡 − 1). For linear controllers this computation can be 
done analytically [20]. 
We now assume a joint Gaussian distribution 𝑝 (𝑥 (𝑡 − 1)) = 
N(𝑥 (𝑡 − 1) | �̃� (𝑡 − 1), Σ̃(𝑡 − 1)) at timestep 𝑡 − 1. The distribution 
of the next step deltas is given by the integral, 
𝑝 (Δ(𝑡)) = ∫ 
𝑝 (𝑓 (𝑥 (𝑡 − 1)) | 𝑥 (𝑡 − 1))𝑝 (𝑥 (𝑡 − 1))𝑑𝑥 (𝑡 − 1) (10) 
This integral (10) is intractable, however a common approach is to 
approximate it as a Gaussian via moment matching [16]. The first 
two moments of Δ(𝑡) are analytically computed, ignoring all higher 
order moments, furthermore, this makes predicting Δ(𝑡 + 1) much 
easier as our distribution over Δ(𝑡) is still Gaussian. Assuming 
the mean 𝜇Δ (𝑡) and covariance ΣΔ (𝑡) of the predictive distribu-
tion 𝑝 (Δ(𝑡)) are known then the Gaussian approximation of the 
distribution 𝑝 (𝑥 (𝑡)) is given by N(𝑥 (𝑡) | 𝜇 (𝑡), Σ(𝑡)), where, 𝜇 (𝑡) = 𝜇 (𝑡 − 1) + 𝜇Δ (𝑡) (11) 
Σ(𝑡) = Σ(𝑡 − 1) + ΣΔ (𝑡) + cov[Δ(𝑡), 𝑥 (𝑡 − 1)] + cov[𝑥 (𝑡 − 1),Δ(𝑡)] (12) 
cov[𝑥 (𝑡 − 1),Δ(𝑡)] = cov[𝑥 (𝑡 − 1), 𝑢 (𝑡 − 1)]Σ−1 
𝑢 (𝑡 − 1)cov[𝑢 (𝑡 − 1),Δ(𝑡)] (13) 
Again, the computation of the cross-covariances (13) here is 
dependent on the parametrization of the policy, e.g., for linear con-
trollers the computation is analytical [20]. For more sophisticated 
policy parametrizations we would need to resort to sampling and 
approximate (10) directly. When we demand high-level of safety, 
sampling, e.g., Monte Carlo methods, can suffer from poor sample 
complexity and are known to be inefficient for assessing the proba-
bility of rare events. For the analytic computation of the mean 𝜇Δ (𝑡) and covariance ΣΔ (𝑡) we refer the reader to [19], for completeness 
we also provide our own derivation in Appendix C. 
Uncertainty propagation. Combined with the linear backup pol-
icy, the 𝑛 GP dynamics models can now provide analytic Gaussian 
confidence ellipsoids E(0), . . . , E(𝑁 ) ⊆ X. The ellipsoids capture both aleatoric uncertainty (observed disturbances and noise) and 
epistemic uncertainty (lack of data), that enclose the state trajectory 
with probability 1 − 𝜖𝑡 . Formally, we let 𝜇 (0) = 𝑥 (0) and Σ(0) = diag( [𝜎2 
1 , . . . 𝜎2 
𝑛]), then the analytic means 𝜇 (0), 𝜇 (1), . . . 𝜇 (𝑁 ) and covariances Σ(0), Σ(1), . . . Σ(𝑁 ) computed as described above, form
the uncertainty sets E(0), . . . , E(𝑁 ) ⊆ X, that are defined in terms 
of the 𝑧-sigma confidence ellipsoids, 
E(𝑡) = {𝑥 ∈ R𝑛 : (𝑥 − 𝜇 (𝑡))𝑇 Σ(𝑡)−1 (𝑥 − 𝜇 (𝑡)) ≤ 𝑧2} (14) 
where 𝑧 > 0 satisfies Φ(𝑧) ≥ 1 − 𝜖𝑡 (where Φ is the CDF of the std. 
normal), and 𝜖𝑡 is the desired step-wise tolerance from (9). To certify 
that a state is 𝜖𝑡 -recoverable, we must check that these ellipsoids 
remain in Xsafe and are eventually fully contained in 𝑋inv. 
Containment and exclusion checks. Given an ellipsoid E(𝑡) with mean 𝜇 (𝑡) and covariance Σ(𝑡): 
 Box inclusion: E(𝑡) ⊆ Xbox iff, 
𝑎𝑖 ≤ 𝜇𝑖 (𝑡) − 𝑧 √︁ Σ𝑖𝑖 (𝑡), 𝜇𝑖 (𝑡) + 𝑧 
√︁ Σ𝑖𝑖 (𝑡) ≤ 𝑏𝑖 (15) 
for all 𝑖 = 1, . . . , 𝑛. 
 Convex hull inclusion: E(𝑡) ⊆ {𝑥 : 𝐴𝑥 ≤ 𝑏} iff, max 
𝑥∈E (𝑡 ) 𝐴 𝑗𝑥 − 𝑏 𝑗 ≤ 0 ∀𝑗 = 1, . . . , 𝑙 (16) 
which can be solved with the following quadratic program (QP) via 
Sequential Least Squares Programming (SLSQP) [35]: 
max 
𝑥 (𝐴𝑖𝑥 − 𝑏𝑖 ) subject to (𝑥 − 𝜇 (𝑡))𝑇 Σ(𝑡)−1 (𝑥 − 𝜇 (𝑡)) ≤ 𝑧2 
(17) 
 Exclusion (obstacle avoidance): For an obstacle region Xobs, we require 
E(𝑡) ∩ Xobs = ∅ (18) 
For convex Xobs, this is checked by solving (17) with the reversed 
inequality. 
 Non-convex combinations: If Xsafe is a union/intersection of convex sets, containment reduces to checking each constituent. 
We outline the full procedure in Algorithm 1. Starting from 
the current state distribution, uncertainty sets E(0), . . . , E(𝑁 ) are propagated under the 𝑛 GPmodels and backup controller (lines 1-4), 
see also Fig. 1. Lines 5-6 implement box and convex hull inclusion, 
and/or line 5 also implicitly encodes obstacle exclusion exclusion 
checks. Line 7 verifies recoverability before deferring to 𝜋 or 𝜋backup. 
We now state the central theorem of our paper. 
Theorem 4.1. Assume: (i) the unknown dynamics 𝑓 and 𝜋backup are both Lipschitz continuous in the 𝐿1-norm, (ii) the 𝑛 GP dynamics models are well calibrated in the sense that with probability (w.p.) at least 1 − 𝛿 there exists 𝛽 (𝜏) > 0 such that ∀𝑡 = 0 . . . 𝑁 and ∀𝑤 (𝑡) ∈ W we have ∥ 𝑓 (𝑥 (𝑡), 𝑢 (𝑡),𝑤 (𝑡)) − 𝜇 (𝑡)∥1 ≤ 𝛽 (𝜏)tr(Σ(𝑡)), (iii) ∀𝑡 = 0 . . . 𝑁 the higher order terms (e.g., skewness, kurtosis) of the true distribution 𝑝 (𝑥 (𝑡)) are negligible and can be ignored. Then if E(0), . . . , E(𝑁 ) ⊆ Xsafe and if there exists 𝑡 ∈ {0, . . . 𝑁 } such that E(𝑡) ⊆ Xinv then 𝑥 (0) is 𝜖𝑡 -recoverable with probability at least 1−𝛿 . Thus 𝜋shield is 𝜖-safe by Theorem 3.1 (w.p., 1 − 𝛿). 
Remark. We comment on the assumptions for Theorem 4.1, which 
generally hold in our experimental evaluation and analyses. First, (i) 
holds for many interesting control systems and 𝜋backup is linear and 
thus Lipschitz; (ii) follows from [12] to ensure the confidence in-
tervals we build are robust to the disturbance setW, GPs typically 
satisfy this assumption under the usual regularity assumptions, 
more details are provided in Appendix D; (iii) ensures that our ana-
lytic Gaussian approximation of the uncertainty sets E(𝑡) capture at least 1−𝜖𝑡 of the probability pass of the true integral (10), which is not always Gaussian [19], we provide a thorough empirical analysis 
Algorithm 1 Shield (𝑥 (0), 𝜋 , 𝜋backup, 𝜖𝑡 , 𝑁 ). 
Input: 𝑥 (0) ∈ X, 𝜋 , 𝜋backup, 𝜖𝑡 ∈ [0, 1], 𝑁 ∈ N Output: Safe action 𝑢 ∈ U 1: 𝑧 ← Φ−1 (1 − 𝜖𝑡 ) 2: 𝜇 (0) ← 𝑥 (0), Σ(0) ← diag( [𝜎2 
1 , . . . , 𝜎2 
𝑛]) 3: for 𝑡 = 1, . . . 𝑁 do 4: Compute E(𝑡) with (14). 
5: Check E(𝑡) ⊆ Xsafe via (15), (16) or (18). 6: Check E(𝑁 ) ⊆ Xinv via (15) or (16). 7: if E(0), . . . , E(𝑁 ) ⊆ Xsafe ∧ E(𝑁 ) ⊆ Xinv then 8: return 𝜋 (𝑥 (0)) 9: else 10: return 𝜋backup (𝑥 (0)) 
in Appendix F.2 suggesting that the uncertainty sets broadly follow 
multivariate Gaussian distributions in most of our environments, 
thus validating this assumption in practice. 
5 IMPLEMENTATION Due to space constraints we defer the pseudocode of the full learn-
ing algorithm to Appendix A However, in this section, we outline 
the key implementation details and relevant technical definitions. 
Replay buffer and policy optimization. During training we store 
all environment interactions of the shielded policy 𝜋shield in a replay 
buffer D = {(𝑥𝑡 , 𝑢𝑡 , 𝑟𝑡 , 𝑥𝑡+1)} consisting of tuples of state, action, 
reward and next state. During policy optimization, we sample starting states 𝑥 ∼ D, from which we rollout the unshielded policy 𝜋 for 
a relatively short time horizon 𝐻 inside the 𝑛 GP dynamics mod-
els. These simulated rollouts provide on-policy samples without 
risking safety violations, since they do not interact with the real 
environment. Since policy optimization is done on relatively short 
rollouts we train 𝜋 with advantage actor-critic (A2C) [53]. A2C is 
often trained on shorter horizon rollouts and preferred here over 
other methods such as, PPO [51] and TRPO [49], which expect long 
horizon rollouts that may accumulate significant noise in the 𝑛 GP 
models, thus, destabilising learning. 
For a trajectory {(𝑥𝑡 , 𝑢𝑡 , 𝑟𝑡 , 𝑥𝑡+1)}𝑇𝑡=0 , the temporal-difference 
residual is, 
𝛿𝑡 = 𝑟𝑡 + 𝛾𝑉𝜙 (𝑥𝑡+1) −𝑉𝜙 (𝑥𝑡 ), (19) 
where𝑉𝜙 is the critic network and 𝛾 the discount factor. The gener-
alized advantage estimate (GAE) [50] is defined as, 
𝐴𝜆𝑡 = 
∞∑︁ 𝑙=0 
(𝛾𝜆)𝑙 𝛿𝑡+𝑙 (20) 
with 𝜆 ∈ [0, 1] controlling the bias-variance trade-off. The policy 𝜋 
is updated via policy gradient, i.e.,∇𝐽 (𝜋) = 𝐴𝜆𝑡 ·∇ log𝜋 (𝑢𝑡 | 𝑥𝑡 ), and the critic parameters 𝜙 are optimized by minimizing the squared 
Bellman error: (𝑉𝜙 (𝑥𝑡 ) − 𝑅𝜆𝑡 )2, where 𝑅𝜆𝑡 is the bootstrapped TD-𝜆 
return. Both the actor and critic are implemented as a two-layer 
feed-forward neural network with tanh activations. To improve 
stability, we use a target network 𝑉𝜙 ′ and Polyak averaging [42] to 
update a target network parameters: 𝜙 ′ ← 𝜏𝜙 + (1 − 𝜏)𝜙 ′. We also 
use symlog predictions [27] to manage large or varying magnitude
rewards. Given a raw return 𝑅, the symlog transform is, 
symlog(𝑅) = sign(𝑅) log(1 + |𝑅 |), (21) 
with inverse symexp(𝑧) = sign(𝑧) (exp( |𝑧 |)−1). The critic is trained on the symlog(𝑅) targets, and regularized towards its target net-
work predictions, reducing both sensitivity to reward magnitudes 
and critic overestimation. 
GP Inference. Computing the exact GP posterior has cubic com-
plexity O(|D|3) in the dataset size |D|. We therefore use sparse ap-
proximations: Sparse GP regression (SGPR) [54] introduces𝑀 ≪ |D| inducing inputs 𝑍 = {𝑧𝑚}𝑀𝑚=1 
with corresponding inducing outputs 
𝑢, yielding a low-rank approximation to the kernel Gram matrix; 
Sparse variational GP regression (SVGP) [30] maintains a variational 
distribution 𝑞(𝑢) = N(𝑚, 𝑆) over inducing outputs, minimizing 
KL[𝑞(𝑢) ∥ 𝑝 (𝑢 | 𝑦)]. We found SGPR to be more effective in prac-
tice, but include both implementations for flexibility. The inducing 
inputs and other GP hyperparameters (e.g., length-scales, signal 
variance, noise variance) are jointly trained by marginal likelihood 
maximization [20]. 
Additional Features. To encourage better explorationwe explored the use of Prioritized replay, inspired by [48], we implemented a 
novelty-based prioritized replay buffer. The state space is discretized 
into bins; the probability of sampling a starting state 𝑥 for policy 
optimization is set inversely proportional to the number of visits 
to its bin. Furthermore, we dealt with unsafe simulated rollouts 
(under 𝜋 ), by zeroing out subsequent rewards and terminating the 
trajectory early. This corresponds to zeroing out the gradients from 
beyond the first unsafe timestep, preventing conflict between the 
learned policy and the shield, and biasing towards safe exploration. 
6 EXPERIMENTAL EVALUATION We now present our experimental results. We first summarize the 
environment and baselines used in this paper. For additional envi-
ronment details we refer the reader to Appendix H. 
Environments. We evaluate our method on four types of contin-
uous control tasks: (1) cartpole [9]: the goal is balance a pole on a moving cart; the safety constraint corresponds to preventing the 
pole from falling. For cartpolewe consider two rewards: the usual +1 for maintaining upright balance, and cartpole2, where +1 is 
given for achieving a target velocity of +0.1. (2) mountain_car [40]: the goal is drive an under-actuated car to the top of a mountain 
(delayed reward); the safety constraint corresponds to avoiding a 
collision with a wall on the opposite side of the valley. (3) obstacle: a 2D navigation task where the goal is to reach a target position 
while avoiding a single obstacle; obstacle2 is more challenging 
due to obstacle placement, obstacle3 and obstacle4 are more 
challenging still with a non-convex combination of constraints. (4) 
road, road_2d: are 1D and 2D road environments requiring the 
agent to reach a target location with a fixed speed limit. 
Baselines. Due to assumption and guarantee mismatch we found 
it challenging to find relevant baselines. Regardless, we consider 
two model-free CMDP-based approaches: Constrained Policy Opti-mization (CPO) [1] and PPO with Lagrangian relaxation (PPO-Lag) 
[46]. These algorithms assume no knowledge of system dynamics, 
making them natural references for sample efficiency. However, 
since our approach leverages a precomputed backup controller and 
control invariant set, we make strictly stronger assumptions; thus 
the comparison is not directly fair, but favours the baselines in terms 
of assumptions. We also consider two model-based approaches: 
MPS [10] and a recent extension DMPS [8]. These methods assume 
knowledge of the deterministic dynamics of the system, a much 
stronger assumption than ours. To ensure compatibility, we omit 
disturbances and observation noise when running MPS/DMPS, ef-
fectively simplifying the environments. This adjustment makes the 
comparison unfair in the opposite direction; our method operates 
under strictly harder conditions. 
Results. We summarize the results for our approach (A2C-GP-
Shield), CPO, PPO-Lag, MPS and DMPS in Tab. 1. In all environ-
ments, A2C-GP-Shield achieves perfect safety probability once the 𝑛 
GP models are properly calibrated, demonstrating the effectiveness 
of our analytic shielding framework in enforcing strict safety. Im-
portantly, this is achieved without sacrificing return: in 7/10 cases 
our method achieves the highest mean reward across the baselines 
that strictly enforce the safety constraint with probability 1. There 
is a clear trade-off in some environments; the CMDP-based ap-
proaches (CPO and PPO-Lag) optimize constraint satisfaction only 
in expectation; as a result, they often achieve higher raw returns 
(e.g., cartpole2, obstacle2) but at the cost of non-negligible safety violations (> 0 unsafe probability). This highlights their inability 
to prevent irrecoverable failures during training. In contrast, our 
approach guarantees strict constraint satisfaction at every timestep, 
effectively ruling out unsafe trajectories. On the other hand, MPS 
and DMPS also achieve perfect safety but under much stronger 
assumptions (e.g., known deterministic dynamics). Overall, A2C-
GP-Shield closes the gap between the two extremes: unlike CMDP 
methods, it enforces safety strictly (not just in expectation), and un-
like MPS/DMPS, it does not require access to exact dynamics. This 
balance explains why A2C-GP-Shield consistently achieves both 
high safety and competitive return across all tested environments. 
Assessing sample efficiency. To fairly assess sample efficiency 
we compare only against model-free baselines (CPO, PPO-Lag), 
excluding MPS and DMPS since they assume full knowledge of 
deterministic dynamics. We also report A2C-Eval, which simply 
executes the learned policy 𝜋 without shielding after each policy 
update. Although unsafe in practice (as 𝜋 cannot be verified), this 
baseline is useful to monitor the learning progress of the underly-
ing policy. Results in Fig. 2 show that A2C-GP-Shield converges 
substantially faster than both CPO and PPO-Lag: in cartpole, 𝜋 reaches optimal performance more than one order of magnitude 
quicker, while in mountain_car it achieves rapid convergence after the 𝑛 GP models become well calibrated. However, during early 
training, imperfect calibration leads to temporary safety violations. 
At the end of training, even though the underlying policy 𝜋 is un-
safe while optimizing for rewards (demonstrating a clear trade-off), 
the shield prevents safety violations entirely. Full learning curves, 
including override statistics are provided in Appendix E. 
Higher-dimensional systems. We further evaluated our approach 
on the Hopper-v5 environment from Gymnasium [56], a standard 
MuJoCo [55] benchmark featuring a simulated 2D robot that must 
hop forward without falling. The observation and action spaces
Table 1: Empirical mean return and safety probability (at the end of training), bold text denotes the best score, asterisk (*) denoted the best reward that also satisfies the safety constraint with probability 1, standard error (SE) bars (averaged over 5 independent runs) are reported. We also include the theoretical lower bound established by Thm. 3.1 (based on 𝜖𝑡 = 10 
−5). 
Env. Metric A2C-GP-Shield MPS DMPS CPO PPO-Lag Thm. 3.1 
cartpole Return 200.0 ± 0.00 200.0 ± 0.00 200.0 ± 0.00 200.0 ± 0.00 188.0 ± 5.53 1 − 𝜖 = 0.98 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.910 ± 0.04 
cartpole2 Return 30.7 ± 10.4 43.2 ± 11.1 65.1 ± 23.1* 152.0 ± 31.2 171.0 ± 7.53 1 − 𝜖 = 0.98 
Safety prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.980 ± 0.01 0.811 ± 0.12 
mountain_car Return 91.3 ± 1.08* 85.1 ± 8.17 81.2 ± 0.28 −30.4 ± 6.74 73.2 ± 18.7 1 − 𝜖 = 0.9 
Safety prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.995 ± 0.00 0.884 ± 0.05 
obstacle Return 32.2 ± 0.10 8.31 ± 34.5 32.7 ± 0.21 32.5 ± 0.30 32.9 ± 0.01* 1 − 𝜖 = 0.98 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 
obstacle2 Return 22.9 ± 5.76* −1.82 ± 3.24 20.2 ± 13.9 15.3 ± 6.08 34.2 ± 0.01 1 − 𝜖 = 0.98 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.939 ± 0.02 0.000 ± 0.00 
obstacle3 Return 4.69 ± 6.40* −0.67 ± 2.12 4.28 ± 5.92 8.56 ± 12.3 33.4 ± 0.114 1 − 𝜖 = 0.98 
(non-convex) Safety Prob. 1.00 ± 0.00 1.00 ± 0.00 1.00 ± 0.00 0.900 ± 0.141 0.148 ± 0.296 
obstacle4 Return 15.5 ± 6.11* −1.12 ± 3.13 11.3 ± 8.04 8.56 ± 12.3 33.4 ± 0.114 1 − 𝜖 = 0.98 
(non-convex) Safety Prob. 1.00 ± 0.00 1.00 ± 0.00 1.00 ± 0.00 0.924 ± 0.0833 0.00 ± 0.00 
road Return 23.0 ± 0.01* 22.7 ± 0.04 22.8 ± 0.02 22.9 ± 0.05 22.9 ± 0.01 1 − 𝜖 = 0.99 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.974 ± 0.01 0.000 ± 0.00 
road_2d Return 23.9 ± 0.26 24.0 ± 0.22* 24.0 ± 0.22* 24.0 ± 0.09 24.1 ± 0.02 1 − 𝜖 = 0.99 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.969 ± 0.01 0.073 ± 0.07 
Hopper-v5 Return 1000 ± 0* 1000 ± 0* 1000 ± 0* 1005 ± 9.98 624 ± 162 1 − 𝜖 = 0.90 
Safety Prob. 1.000 ± 0.00 1.000 ± 0.00 1.000 ± 0.00 0.976 ± 0.0150 0.00 ± 0.00 
are 𝑛 = 11 and𝑚 = 3, respectively, with rewards consisting of a 
healthy survival bonus and forward velocity term. Each episode is 
limited to 𝑇 = 1000 timesteps. We designed a linear feedback con-
troller around the nominal equilibrium configuration using discrete-
time LQR, with (𝐴, 𝐵) matrices obtained from a finite-difference 
linearization of the MuJoCo dynamics (c.f., Appendix H.5). The 
corresponding control invariant set was computed via ellipsoidal 
expansion and convex-hull verification. With 𝜖𝑡 = 10 −4 
and recov-
ery horizon 𝐻 = 100, the shield intervened at every step, main-
taining perfect safety and achieving the maximum healthy reward 
of +1000.0 as detailed in Tab. 1. These results demonstrate that 
while our framework is theoretically sound and guarantees safety 
by construction, its practical performance depends critically on the 
quality of the backup controller and the size of the verified control 
invariant set. For complex high-dimensional systems with contact 
dynamics, limit cycles, and other non-linear effects, verifying suffi-
ciently large invariant sets remains an open challenge orthogonal 
to our approach. Developing richer or learned backup controllers 
capable of stabilizing over larger regions may therefore be essential 
for extending recovery-based shielding to such settings. 
7 RELATEDWORK Constrained RL. The most widely adopted formulation for safe 
RL is the CMDP framework [4]. In a CMDP, the agent optimizes 
its policy to maximize reward while satisfying a cost constraint 
(typically an expected cost or chance constraint) at each step or 
over each episode. A number of safe RL algorithms build on this 
framework, for example by using Lagrange relaxations [7, 46], or 
policy projection (e.g., Constrained Policy Optimization [1]). While 
CMDP-based methods can improve the average safety of learning, 
100.0 1000.0 10000.0 100000.0 Step 
50 
100 
150 
200 
Re wa 
rd 
100.0 1000.0 10000.0 100000.0 Step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  p 
ro b 
A2C-GP-Shield (ours) A2C-Eval (ours) 
PPO-Lag CPO backup 
(a) cartpole 
100.0 1000.0 10000.0 100000.0 Step 
50 
0 
50 
100 
Re wa 
rd 
100.0 1000.0 10000.0 100000.0 Step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  p 
ro b 
(b) mountain_car 
Figure 2: Learning curves (log scale on the x-axis). 
they provide only indirect convergence guarantees, they often en-
sure constraints in expectation or asymptotically, which means they 
may still allow occasional, potentially dangerous violations during 
training. There exists GP methods that fall within this category, 
i.e., which model an unknown safety cost function through GPs 
[61, 62]. These methods are not without their limitations, making 
often unrealistic assumptions, e.g., assuming known deterministic 
dynamics or access to a privileged “emergency reset” button [60].
In summary, CMDP guarantees tend to be weaker and not suited for highly safety-critical environments [57]. 
Shielding. In contrast to CMDP methods, shielding often offers 
more rigorous guarantees. For RL, shielding was first introduced 
by Alshiekh et al. [3] for safeguarding against formal logic specifi-
cations in discrete-state systems. Provided with a suitable (logical) 
safety-abstraction of the environment, shielding filters out unsafe 
actions proposed by the agent, enjoying key properties, such as 
correctness and minimal interference. For stochastic environments, 
this approach has recently been extended to optimality preserv-
ing probabilistic guarantees for generic reachability properties [28]. In continuous control domains, implementing shielding requires 
computing a safe region of the state space and a policy to keep the 
agent within it. One line of work employs Hamilton-Jacobi (HJ) 
reachability analysis [2] to derive the maximal safe set and a corre-
sponding safe controller. Fisac et al. [21] generalized this idea to RL 
with uncertain dynamics by formulating a safety value function (via 
an HJ partial differential equation) that triggers an override when 
the agent is about to exit the safe set. HJ-based shielding methods 
offer strong safety guarantees for nonlinear systems, including the 
ability to handle non-convex state constraints [58]. However, as 
noted earlier, they suffer from poor scalability. To improve scalabil-
ity, other works focus on computing control invariant sets (often 
convex approximations of the safe region) for complex dynamics 
[10, 11, 38]. For instance, robust invariant set computation tech-
niques have been applied to design shields that work for certain 
classes of non-linear systems [38]. Furthermore, The concept of 
shielding has also been extended to higher dimensional systems 
with learned world models [23, 29], although these methods come 
with some theory [23] they often any lack strict guarantees. Our 
work addresses this more general case where the system dynamics 
are initially unknown, requiring the agent to learn them, and thus 
we build on the concept of shielding combined with online model 
learning. Sampling based techniques, e.g., Statistical MPS [11], can be used for stochastic models of the environment; for a step-wise 
safety probability 𝜖𝑡 and confidence 𝛿𝑡 Bastani et al. [11] show that 
the required number of samples satisfies,𝐾 (𝜖𝑡 , 𝛿) ≥ log(1/𝛿𝑡 ) log(1/(1−𝜖𝑡 ) ) +1. 
Substituting 𝜖𝑡 = 10 −5 
(which was used in our experiments) and 
𝛿𝑡 = 0.01 yields 𝐾 ≈ 46,000 samples per check, which is computa-
tionally infeasible, even with approximate sampling regimes [41] 
(c.f., Appendix F.1). Notably, our method does away with the con-
fidence 𝛿𝑡 (essentially absorbing it into the GP learning) and as 
discussed earlier can handle arbitrarily small 𝜖𝑡 without additional 
overhead. 
Gaussian Process (GP) models have long been used in RL for 
data-efficient learning of dynamics and rewards. PILCO [19] is a 
landmark model-based RL approach that uses GP dynamics models 
to achieve impressive sample efficiency. However, PILCO’s original 
formulation had no safety considerations. An extension by Poly-
menakos et al. [43] incorporated a safety constraint into the PILCO 
framework; this approach is limited by considering only a small, 
specific class of policies (e.g., linear and RBF) and did not provide 
rigorous safety guarantees for those policies. More generally, GPs 
have been integrated into safe RL algorithms primarily through 
the CMDP lens discussed above [60–62]. A different approach is 
to use learned models within a control-theoretic safety scheme. 
Learning-based Model Predictive Control (MPC) has been explored 
as a way to enforce safety during RL. Koller et al. [33] pioneered a 
GP-based MPC for safe exploration, which uses GPs to construct 
high-confidence bounds on the system’s behaviour and then opti-
mizes a control sequence that satisfies state constraints with high 
probability. Although, their framework only considers optimization 
over a sequence of time-dependent linear controllers. Similar work 
from Cheng et al. [17] consider control barrier functions (CBF) 
with GP uncertainty estimates, solving a QP for high-probability 
guarantees. More recently, Zhao et al. [64] proposed a Probabilistic Safeguard framework that also leverages GP models for safety. In 
their approach, the agent first gathers an offline dataset of safe trajectories to train a GP model, then defines a safety index (anal-
ogous to a CBF). This safeguard method shares our philosophy 
of combining learning with a safety filter; however, it relies on 
designing an appropriate safety index and primarily addresses the 
offline training phase, whereas our work emphasizes online safe 
exploration and learning. 
8 CONCLUSION We proposed a recovery-based shielding framework that integrates 
Gaussian process (GP) dynamics models with formal safety se-
mantics to guarantee a probabilistic lower bound on safety. Our 
approach propagates analytic uncertainty sets through the GP 
model and leverages a precomputed backup policy to certify 𝜖-
recoverability of states. This expands the set of operationally safe states beyond the control invariant set, while avoiding sampling-
based verification and thus remaining efficient even under strict 
safety requirements. Our implementation, A2C-GP-Shield, supports 
both SGPR [54] and SVGP [30], enabling scalable training with large 
replay buffers. Nonetheless, GP inference can become computation-
ally demanding in higher dimensions (e.g., 𝑛 > 20), suggesting that 
deep kernel learning may be a promising direction for future work. 
Extending our framework to handle moving or dynamic obstacles 
is another natural step: while our method applies directly when 
obstacle dynamics are known, learning or estimating unknown 
obstacle dynamics presents an open challenge. Finally, removing 
the reliance on an a priori backup policy, by computing or opti-
mizing the backup controller online, could make the framework 
more broadly applicable in scenarios where such a controller is 
unavailable. 
ACKNOWLEDGMENTS The research described in this paper was partially supported by the 
EPSRC (grant number EP/X015823/1). 
REFERENCES [1] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. 2017. Constrained 
policy optimization. In International conference on machine learning. PMLR, 22– 
31. 
[2] Anayo KAkametalu, Jaime F Fisac, JeremyHGillula, Shahab Kaynama, Melanie N 
Zeilinger, and Claire J Tomlin. 2014. Reachability-based safe learning with 
Gaussian processes. In 53rd IEEE conference on decision and control. IEEE, 1424– 1431. 
[3] Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott 
Niekum, and Ufuk Topcu. 2018. Safe reinforcement learning via shielding. In 
Proceedings of the AAAI conference on artificial intelligence, Vol. 32. [4] Eitan Altman. 1999. Constrained Markov decision processes: stochastic modeling. 
Routledge.
[5] Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and 
Dan Mané. 2016. Concrete problems in AI safety. arXiv preprint arXiv:1606.06565 (2016). 
[6] Brian DO Anderson and John B Moore. 2007. Optimal control: linear quadratic methods. Courier Corporation. 
[7] Yarden As, Ilnura Usmanova, Sebastian Curi, and Andreas Krause. 2022. Con-
strained policy optimization via bayesian world models. arXiv preprint arXiv:2201.09802 (2022). 
[8] Arko Banerjee, Kia Rahmani, Joydeep Biswas, and Isil Dillig. 2024. Dynamic 
Model Predictive Shielding for Provably Safe Reinforcement Learning. arXiv preprint arXiv:2405.13863 (2024). 
[9] Andrew G. Barto, Richard S. Sutton, and Charles W. Anderson. 1983. Neu-
ronlike adaptive elements that can solve difficult learning control problems. 
IEEE Transactions on Systems, Man, and Cybernetics SMC-13, 5 (1983), 834–846. 
https://doi.org/10.1109/TSMC.1983.6313077 
[10] Osbert Bastani. 2021. Safe reinforcement learning with nonlinear dynamics 
via model predictive shielding. In 2021 American control conference (ACC). IEEE, 3488–3494. 
[11] Osbert Bastani, Shuo Li, and Anton Xu. 2021. Safe Reinforcement Learning via 
Statistical Model Predictive Shielding.. In Robotics: Science and Systems. 1–13. [12] Felix Berkenkamp, Matteo Turchetta, Angela Schoellig, and Andreas Krause. 2017. 
Safe model-based reinforcement learning with stability guarantees. Advances in neural information processing systems 30 (2017). 
[13] Roderick Bloem, Bettina Könighofer, Robert Könighofer, and Chao Wang. 2015. 
Shield synthesis: Runtime enforcement for reactive systems. In International conference on tools and algorithms for the construction and analysis of systems. Springer, 533–548. 
[14] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris 
Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye 
Wanderman-Milne, and Qiao Zhang. 2018. JAX: composable transformations of 
Python+NumPy programs. http://github.com/jax-ml/jax 
[15] Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schul-
man, Jie Tang, and Wojciech Zaremba. 2016. Openai gym. arXiv preprint arXiv:1606.01540 (2016). 
[16] Joaquin Quinonero Candela, Agathe Girard, Jan Larsen, and Carl Edward Ras-
mussen. 2003. Propagation of uncertainty in bayesian kernel models-application 
to multiple-step ahead forecasting. In 2003 IEEE International Conference on Acous-tics, Speech, and Signal Processing, 2003. Proceedings.(ICASSP’03)., Vol. 2. IEEE, II–701. 
[17] Richard Cheng, Gábor Orosz, Richard M Murray, and Joel W Burdick. 2019. End-
to-end safe reinforcement learning through barrier functions for safety-critical 
continuous control tasks. In Proceedings of the AAAI conference on artificial intelligence, Vol. 33. 3387–3395. 
[18] Sayak Ray Chowdhury and Aditya Gopalan. 2017. On kernelized multi-armed 
bandits. In International Conference on Machine Learning. PMLR, 844–853. 
[19] Marc Deisenroth and Carl E Rasmussen. 2011. PILCO: A model-based and 
data-efficient approach to policy search. In Proceedings of the 28th International Conference on machine learning (ICML-11). 465–472. 
[20] Marc Peter Deisenroth. 2010. Efficient reinforcement learning using Gaussian processes. Vol. 9. KIT Scientific Publishing. 
[21] Jaime F Fisac, Anayo K Akametalu, Melanie N Zeilinger, Shahab Kaynama, Jeremy 
Gillula, and Claire J Tomlin. 2018. A general safety framework for learning-based 
control in uncertain robotic systems. IEEE Trans. Automat. Control 64, 7 (2018), 2737–2752. 
[22] Javier Garcıa and Fernando Fernández. 2015. A comprehensive survey on safe 
reinforcement learning. Journal of Machine Learning Research 16, 1 (2015), 1437– 
1480. 
[23] Alexander W Goodall and Francesco Belardinelli. 2023. Approximate Model-
Based Shielding for Safe Reinforcement Learning. In ECAI 2023. IOS Press, 
883–890. 
[24] Alexander W Goodall and Francesco Belardinelli. 2024. Leveraging Approximate 
Model-based Shielding for Probabilistic Safety Guarantees in Continuous En-
vironments. In Proceedings of the 23rd International Conference on Autonomous Agents and Multiagent Systems. 2291–2293. 
[25] Sven Gronauer, Tom Haider, Felippe Schmoeller da Roza, and Klaus Diepold. 2024. 
Reinforcement Learning with Ensemble Model Predictive Safety Certification. 
arXiv preprint arXiv:2402.04182 (2024). [26] Felix Gruber and Matthias Althoff. 2020. Computing safe sets of linear sampled-
data systems. IEEE Control Systems Letters 5, 2 (2020), 385–390. [27] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. 2023. Mas-
tering diverse domains through world models. arXiv preprint arXiv:2301.04104 (2023). 
[28] Edwin Hamel-De le Court, Francesco Belardinelli, and Alexander W Goodall. 
2025. Probabilistic Shielding for Safe Reinforcement Learning. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 39. 16091–16099. 
[29] Chloe He, Borja G León, and Francesco Belardinelli. 2022. Do Androids Dream 
of Electric Fences? Safety-Aware Reinforcement Learning with Latent Shielding. 
(2022). https://ceur-ws.org/Vol-3087/paper_50.pdf 
[30] James Hensman, Alexander G Matthews, Maurizio Filippone, and Zoubin 
Ghahramani. 2015. MCMC for Variationally Sparse Gaussian Pro-
cesses. In Advances in Neural Information Processing Systems, C. Cortes, 
N. Lawrence, D. Lee, M. Sugiyama, and R. Garnett (Eds.), Vol. 28. Curran 
Associates, Inc. https://proceedings.neurips.cc/paper_files/paper/2015/file/ 
6b180037abbebea991d8b1232f8a8ca9-Paper.pdf 
[31] Jiaming Ji, Jiayi Zhou, Borong Zhang, Juntao Dai, Xuehai Pan, Ruiyang Sun, 
Weidong Huang, Yiran Geng, Mickel Liu, and Yaodong Yang. 2023. OmniSafe: 
An Infrastructure for Accelerating Safe Reinforcement Learning Research. arXiv preprint arXiv:2305.09304 (2023). 
[32] Niklas Kochdumper, Felix Gruber, Bastian Schürmann, Victor Gaßmann, Moritz 
Klischat, and Matthias Althoff. 2021. AROC: A toolbox for automated reachset 
optimal controller synthesis. In Proceedings of the 24th International Conference on Hybrid Systems: Computation and Control. 1–6. 
[33] Torsten Koller, Felix Berkenkamp, Matteo Turchetta, and Andreas Krause. 2018. 
Learning-based model predictive control for safe exploration. In 2018 IEEE conference on decision and control (CDC). IEEE, 6059–6066. 
[34] Bettina Könighofer, Julian Rudolf, Alexander Palmisano, Martin Tappler, and 
Roderick Bloem. 2021. Online shielding for stochastic systems. In NASA Formal Methods Symposium. Springer, 231–248. 
[35] Dieter Kraft. 1988. A software package for sequential quadratic programming. 
Forschungsbericht- Deutsche Forschungs- und Versuchsanstalt fur Luft- und Raum-fahrt (1988). 
[36] Hanna Krasowski, Jakob Thumm, Marlon Müller, Lukas Schäfer, Xiao Wang, 
and Matthias Althoff. 2023. Provably safe reinforcement learning: Conceptual 
analysis, survey, and benchmarking. Transactions on Machine Learning Research (2023). 
[37] Armin Lederer, Jonas Umlauft, and Sandra Hirche. 2019. Uniform error bounds 
for Gaussian process regression with application to safe control. Advances in Neural Information Processing Systems 32 (2019). 
[38] Shuo Li and Osbert Bastani. 2020. Robust model predictive shielding for safe 
reinforcement learning with stochastic dynamics. In 2020 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 7166–7172. 
[39] Ian MMitchell, Alexandre M Bayen, and Claire J Tomlin. 2005. A time-dependent 
Hamilton-Jacobi formulation of reachable sets for continuous dynamic games. 
IEEE Transactions on automatic control 50, 7 (2005), 947–957. [40] Andrew William Moore. 1990. Efficient Memory-based Learning for Robot Control. 
Technical Report. University of Cambridge. 
[41] Thomas Pinder and Daniel Dodd. 2022. GPJax: A Gaussian Process Framework 
in JAX. Journal of Open Source Software 7, 75 (2022), 4455. https://doi.org/10. 
21105/joss.04455 
[42] Boris T Polyak and Anatoli B Juditsky. 1992. Acceleration of stochastic approx-
imation by averaging. SIAM journal on control and optimization 30, 4 (1992), 
838–855. 
[43] Kyriakos Polymenakos, Alessandro Abate, and Stephen Roberts. 2019. Safe policy 
search using Gaussian process models. In Proceedings of the 18th international conference on autonomous agents and multiagent systems. 1565–1573. 
[44] Antonin Raffin, AshleyHill, AdamGleave, Anssi Kanervisto, Maximilian Ernestus, 
and Noah Dormann. 2021. Stable-Baselines3: Reliable Reinforcement Learning 
Implementations. Journal of Machine Learning Research 22, 268 (2021), 1–8. 
http://jmlr.org/papers/v22/20-1364.html 
[45] Carl Edward Rasmussen. 2003. Gaussian processes in machine learning. In 
Summer school on machine learning. Springer, 63–71. [46] Alex Ray, Joshua Achiam, and Dario Amodei. 2019. Benchmarking safe explo-
ration in deep reinforcement learning. arXiv preprint arXiv:1910.01708 7, 1 (2019), 2. 
[47] Lukas Schäfer, Felix Gruber, and Matthias Althoff. 2023. Scalable computation of 
robust control invariant sets of nonlinear systems. IEEE Trans. Automat. Control 69, 2 (2023), 755–770. 
[48] Tom Schaul. 2015. Prioritized Experience Replay. arXiv preprint arXiv:1511.05952 (2015). 
[49] John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. 
2015. Trust region policy optimization. In International conference on machine learning. PMLR, 1889–1897. 
[50] John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. 
2015. High-dimensional continuous control using generalized advantage estima-
tion. arXiv preprint arXiv:1506.02438 (2015). [51] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 
2017. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 (2017). 
[52] Niranjan Srinivas, Andreas Krause, Sham M Kakade, and Matthias Seeger. 2009. 
Gaussian process optimization in the bandit setting: No regret and experimental 
design. arXiv preprint arXiv:0912.3995 (2009). [53] Richard S Sutton. 2018. Reinforcement learning: An introduction. A Bradford 
Book (2018). 
[54] Michalis Titsias. 2009. Variational learning of inducing variables in sparse Gauss-
ian processes. In Artificial intelligence and statistics. PMLR, 567–574.
[55] Emanuel Todorov, Tom Erez, and Yuval Tassa. 2012. Mujoco: A physics engine 
for model-based control. In 2012 IEEE/RSJ international conference on intelligent robots and systems. IEEE, 5026–5033. 
[56] Mark Towers, Ariel Kwiatkowski, Jordan Terry, John U Balis, Gianluca De Cola, 
Tristan Deleu, Manuel Goulão, Andreas Kallinteris, Markus Krimmel, Arjun 
KG, et al. 2024. Gymnasium: A Standard Interface for Reinforcement Learning 
Environments. arXiv preprint arXiv:2407.17032 (2024). [57] Cameron Voloshin, Hoang Le, Swarat Chaudhuri, and Yisong Yue. 2022. Pol-
icy optimization with linear temporal logic constraints. Advances in Neural Information Processing Systems 35 (2022), 17690–17702. 
[58] Kim P Wabersich, Andrew J Taylor, Jason J Choi, Koushil Sreenath, Claire J 
Tomlin, Aaron D Ames, and Melanie N Zeilinger. 2023. Data-driven safety filters: 
Hamilton-jacobi reachability, control barrier functions, and predictive methods 
for uncertain systems. IEEE Control Systems Magazine 43, 5 (2023), 137–177. [59] Kim P Wabersich and Melanie N Zeilinger. 2018. Linear model predictive safety 
certification for learning-based control. In 2018 IEEE Conference on Decision and Control (CDC). IEEE, 7130–7135. 
[60] Akifumi Wachi, Wataru Hashimoto, Xun Shen, and Kazumune Hashimoto. 2024. 
Safe exploration in reinforcement learning: A generalized formulation and algo-
rithms. Advances in Neural Information Processing Systems 36 (2024). [61] Akifumi Wachi and Yanan Sui. 2020. Safe reinforcement learning in constrained 
markov decision processes. In International Conference on Machine Learning. PMLR, 9797–9806. 
[62] Akifumi Wachi, Yanan Sui, Yisong Yue, and Masahiro Ono. 2018. Safe exploration 
and optimization of constrained mdps using gaussian processes. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 32. 
[63] Yixuan Wang, Simon Sinong Zhan, Ruochen Jiao, Zhilu Wang, Wanxin Jin, Zhuo-
ran Yang, Zhaoran Wang, Chao Huang, and Qi Zhu. 2023. Enforcing hard 
constraints with soft barriers: Safe reinforcement learning in unknown stochastic 
environments. In International Conference on Machine Learning. PMLR, 36593– 
36604. 
[64] Weiye Zhao, Tairan He, and Changliu Liu. 2023. Probabilistic safeguard for 
reinforcement learning using safety index guided gaussian process models. In 
Learning for Dynamics and Control Conference. PMLR, 783–796.
A ALGORITHMS 
Algorithm 2 Recovery-based Shielding with GP 
Input: Xsafe, 𝜋backup, Xinv, 𝜖𝑡 ∈ [0, 1], 𝑁 ∈ N Output: Policy 𝜋 , value function 𝑉𝜙 (and target network 𝑉𝜙 ′ ) and 𝑛 GP dynamics models 𝑝𝜃 . 
1: Initialize 𝜋 , 𝜙 , 𝜙 ′ and 𝜃 appropriately and replay buffer D with random experience. 
2: Observe the initial state 𝑥 (0). 3: for 𝑡 = 0, . . . , num_steps do 4: 𝑢 (𝑡) ← Shield(𝑥 (𝑡), 𝜋, 𝜋backup, 𝜖𝑡 , 𝑁 ) 5: Use 𝑢 (𝑡) and observe 𝑥 (𝑡 + 1). 6: Append ⟨𝑢 (𝑡), 𝑥 (𝑡), 𝑥 (𝑡 + 1)⟩ to D. 
7: if time_to_update then 8: Update GP parameters 𝜃 with dataset D. 
9: Sample a batch of starting states 𝐵 ∈ D. 
10: From each 𝑥 (·) ∈ 𝐵 rollout 𝜋 with 𝑝𝜃 . 
11: Compute GAE (𝐴𝜆𝑡 ) and TD-𝜆 returns (𝑅𝜆𝑡 ) from rollouts. 
12: Update 𝜙 via MSE with symlog(𝑅𝜆𝑡 ) and target network regularization. 
13: Update 𝜙 ′ via Polyak averaging [42]. 
14: Update 𝜋 via policy gradient. 
15: return 𝜋 and 𝑝𝜃 . 
B PROOF OF THEOREM 3.1 Theorem 3.1 (restated) (𝜖-Safe Policy). Assume: (i) Xinv is an invariant set for 𝜋backup, (ii) X0 ⊆ Xinv ⊆ Xsafe and (iii) 
∑𝑇 𝑡=0 
𝜖𝑡 = 𝜖 , then, 𝜋shield is 𝜖-safe for the time horizon 𝑇 ∈ N. 
Proof. The proof of Theorem 3.1 is obtained by establishing the following invariant: “we can always return to Xinv with probability at 
least 1 − 𝜖𝑡 by using the backup policy 𝜋backup for 𝑁 timesteps”. Since the initial state 𝑥 (0) ∈ Xinv and Xinv is invariant for 𝜋backup, then this 
holds for 𝑡 = 0. By the inductive assumption we assume that the invariant has been established for 𝑡 − 1, if 𝑥 (𝑡) ∈ X𝜖𝑡 rec (𝑁 ) we are safe to 
use the learned policy 𝜋 and by definition of X𝜖𝑡 rec (𝑁 ) we have established the invariant. If 𝑥 (𝑡) ∉ X𝜖𝑡 
rec (𝑁 ) then we use the backup policy 
𝜋backup, which will return us to Xinv within 𝑁 timesteps as we have established the invariant in timestep 𝑡 − 1. The remainder of the proof is 
obtained by a union bound over the step-wise safety constraints 𝜖0, 𝜖1, . . . , 𝜖𝑇 . □ 
C MEAN AND COVARIANCE PREDICTION (PILCO) Here we detail the analytic mean and covariance prediction proposed in PILCO [20]. 
Mean prediction (𝜇Δ). For the state dimensions 𝑖 = 1, . . . , 𝑛, we let 𝜇Δ (𝑡) = [𝜇1, . . . 𝜇𝑛]𝑇 . Following the law of iterated expectations, we 
then obtain, 
𝜇𝑖 = E�̃� (𝑡−1) [E𝑓 [𝑓 (𝑥 (𝑡 − 1)) | 𝑥 (𝑡 − 1)]] (22) 
= E�̃� (𝑡−1) [𝑚𝑓 (𝑥 (𝑡 − 1))] (23) 
= 
∫ 𝑚𝑓 (𝑥 (𝑡 − 1))N (𝑥 (𝑡 − 1) | �̃� (𝑡 − 1), Σ̃(𝑡 − 1))𝑑𝑥 (𝑡 − 1) (24) 
= 𝛽𝑇𝑖 𝑄𝑖 (25) 
with 𝛽𝑖 = (𝐾𝑖 + 𝜎2 
𝜀𝑖 )−1𝑦𝑖 and 𝑄𝑖 = [𝑞1𝑖 
, . . . 𝑞𝐷𝑖 ]𝑇 . Here𝑚𝑓 is given by (5), see Sec. 2.2. For 𝑎 = 1, . . . , 𝐷 , the entries of 𝑄𝑖 ∈ R𝐷 are then given 
by, 
𝑞𝑎𝑖 = 
∫ 𝑘𝑖 (𝑥𝑎 (·), 𝑥 (𝑡 − 1))N (𝑥 (𝑡 − 1) | �̃� (𝑡 − 1), Σ̃(𝑡 − 1))𝑑𝑥 (𝑡 − 1) (26) 
= 𝛼2 
𝑖√︃ |Σ̃(𝑡 − 1)Λ−1 
𝑖 + I| 
exp(−1 
2 
𝑣𝑇𝑎 (Σ̃(𝑡 − 1) + Λ𝑖 )−1𝑣𝑎) (27) 
where 𝑣𝑎 := (𝑥𝑎 (·) − �̃� (𝑡 − 1)) (28) 
The value 𝑣𝑎 is the difference between the 𝑎 th training input, i.e., 𝑥𝑎 (·) and the mean of the input distribution 𝑝 (𝑥 (𝑡 −1)) = 𝑝 (𝑥 (𝑡 −1), 𝑢 (𝑡 −1)) 
calculated earlier, see Sec. 2.2.
Covariance prediction (ΣΔ). To present the computation the covariance matrix ΣΔ (𝑡) ∈ R𝑛×𝑛 it is convenient to distinguish between 
diagonal 𝜎2 
𝑖𝑖 and off diagonal elements 𝜎2 
𝑖 𝑗 (𝑖 ≠ 𝑗 ) of ΣΔ (𝑡). Using the law of iterated variances for the state dimensions 𝑖, 𝑗 = 1, . . . 𝑛, we 
obtain, 
𝜎2 
𝑖𝑖 = E�̃� (𝑡−1) [var𝑓 [Δ𝑖 | 𝑥 (𝑡 − 1)] + E𝑓 ,�̃� (𝑡−1) [Δ2 
𝑖 ] − 𝜇2 
𝑖 (29) 
𝜎2 
𝑖 𝑗 = E𝑓 ,�̃� (𝑡−1) [Δ𝑖Δ 𝑗 ] − 𝜇𝑖𝜇 𝑗 (𝑖 ≠ 𝑗) (30) 
where 𝜇𝑖 is computed using (22) from before. We note that the usual covariance term is missing, in this case E�̃� (𝑡−1) [cov𝑓 [Δ𝑖 ,Δ 𝑗 | 𝑥 (𝑡 − 1)]], this is because given 𝑥 (𝑡 − 1) output dimensions are independent. Continuing, we have, 
E𝑓 ,�̃� (𝑡−1) [Δ𝑖Δ 𝑗 ] = 𝛽𝑇𝑖 𝑄𝛽 𝑗 (31) 
where 
𝑄 := 
∫ 𝑘𝑖 (�̃� , 𝑥 (𝑡 − 1))𝑘 𝑗 (�̃� , 𝑥 (𝑡 − 1))𝑇𝑝 (𝑥 (𝑡 − 1))𝑑𝑥 (𝑡 − 1) (32) 
For 𝑎, 𝑏 = 1, . . . 𝐷 , The entries of 𝑄𝑎𝑏 of 𝑄 ∈ R𝐷×𝐷 are given by standard integration results for Gaussian distributions, 
𝑄𝑎𝑏 = 𝑘𝑖 (𝑥𝑎 (·), �̃� (𝑡 − 1))𝑘 𝑗 (𝑥𝑏 (·), �̃� (𝑡 − 1))√︁ 
|𝑅 | · exp 
( 1 
2 
𝑧𝑇 𝑎𝑏 𝑅−1Σ̃(𝑡 − 1)𝑧𝑎𝑏 
) (33) 
where 𝑅 := Σ̃(𝑡 − 1) (Λ−1 
𝑖 + Λ−1 
𝑗 ) + I and 𝑧𝑎𝑏 = Λ−1 
𝑖 𝑣𝑎 + Λ−1 
𝑗 𝑣𝑏 , where 𝑣𝑎 defined in (28). This concludes the computation of the off diagonals, 
which are now fully determined by Eqs. (22)-(28) and Eqs. (30)-(33). For the diagonal entries of ΣΔ, it remains to compute the additional term, 
E�̃� (𝑡−1) [var𝑓 [Δ𝑖 | 𝑥 (𝑡 − 1)] = 𝛼2 
𝑖 − tr((𝐾𝑖 + 𝜎2 
𝜀𝑖 I)−1𝑄) (34) 
with 𝑄 given by (33), and tr((𝐾𝑖 + 𝜎2 
𝜀𝑖 I)−1𝑄) denoting the trace of the matrix (𝐾𝑖 + 𝜎2 
𝜀𝑖 I)−1𝑄 . 
D GAUSSIAN PROCESS THEORY (THEOREM 4.1) Theorem 3.1 (restated). Assume: (i) the unknown dynamics 𝑓 and 𝜋backup are both Lipschitz continuous in the 𝐿1-norm, (ii) the 𝑛 GP dynamics models are well calibrated in the sense that with probability (w.p.) at least 1 − 𝛿 there exists 𝛽 (𝜏) > 0 such that ∀𝑡 = 0 . . . 𝑁 and ∀𝑤 (𝑡) ∈ W we have ∥ 𝑓 (𝑥 (𝑡), 𝑢 (𝑡),𝑤 (𝑡)) − 𝜇 (𝑡)∥1 ≤ 𝛽 (𝜏)tr(Σ(𝑡)), (iii) ∀𝑡 = 0 . . . 𝑁 the higher order terms (e.g., skewness, kurtosis) of the true distribution 𝑝 (𝑥 (𝑡)) are negligible and can be ignored. Then if E(0), . . . , E(𝑁 ) ⊆ Xsafe and if there exists 𝑡 ∈ {0, . . . 𝑁 } such that E(𝑡) ⊆ Xinv then 𝑥 (0) is 𝜖𝑡 -recoverable with probability at least 1 − 𝛿 . Thus 𝜋shield is 𝜖-safe by Theorem 3.1 (w.p., 1 − 𝛿). 
Proof. To enable the use of Gaussian process and satisfy the Lipschitz continuity property of the unknown function 𝑓 a common 
technique is used, which assume the disturbances𝑤 (𝑡) ∈ W live in some reproducing kernel Hilbert space, corresponding to a differential 
kernel 𝑘 and have RKHS norm smaller and 𝐵W . This is a model agnostic approach that does not restrict the true function 𝑓 to the space of 
Gaussian process priors [52]. 
Lemma D.1 ([52] Theorem 6). For some arbitrary function 𝑓 : Z → R with zero mean prior and kernel 𝑘 in some RKHS with norm smaller than 𝐵, with observations 𝑦 = 𝑓 (𝑧) + 𝜎 assuming sub-Gaussian noise in the range [−𝜎max, 𝜎max]. Letting 𝜇𝑛 (𝑧) and 𝜎2 
𝑛 (𝑧) denote the mean and variance given 𝑛 noisy observations. Pick 𝛽𝑛 = 𝐵W + 4𝜎 
√︁ 𝜏𝑛 + 1 + ln(1/𝛿). Then with probability at least 1 − 𝛿 , for 𝛿 ∈ (0, 1), for all 𝑛 ≥ 1, 
𝑧 ∈ Z and 𝑢 (·) ∈ U it holds that ∥ 𝑓 (𝑧) − 𝜇𝑛−1 (𝑧)∥ ≤ 𝛽𝑛𝜎𝑛−1 (𝑧) 
Remark. Lemma D.1 can be easily extended to an extended parameter space of X ×U [12] and extended to multi output functions using the 
proof techniques in ([18] Theorem 2). While Lemma D.1 makes different assumptions than usual GP assumptions (e.g. 𝑓 ∼ GP(0, 𝑘 (·, ·)), Gaussian noise variances), it demonstrates that the error bounds are conservative enough to capture the true function with high probability. 
We further note that the bound in D.1 depends on the information capacity parameter 𝜏𝑛 , which corresponds to the maximum mutual 
information that could be gained about the unknown function 𝑓 from samples. For many commonly used kernels, including the squared 
exponential kernel (which we consider in this paper), the parameter 𝜏𝑛 is sub-linear in the number of samples 𝑛 and can be accurately 
approximated [52]. 
Another approach is to directly assume the unknown function 𝑓 is a sample from a Gaussian process GP(0, 𝑘 (·, ·)), using the Lipschitz constant of 𝑘 and 𝑓 on the closed set X × U we can uniformly bound the error of 𝑓 (confidence interval) with high probability for all 
(𝑥 (·), 𝑢 (·)) ∈ X ×U. This requires knowledge of the Lipschitz constant of 𝑓 , which can robustly estimated [37]. 
In either cases we have that assumption (ii) holds with high probability, then by assumption (iii) the result of Thm. 4.1 holds since the 
uncertainty sets E(0), . . . , E(𝑁 ) now contain at least 1 − 𝜖𝑡 of the probability mass of the true distributions 𝑝 (𝑥 (0)), . . . 𝑝 (𝑥 (𝑁 )) which implies that 𝑥 (𝑡) is 𝜖𝑡 -recoverable by the definition of 𝜖-recoverable states. □
E ADDITIONAL PLOTS 
0 1000 2000 3000 4000 5000 step 
50 
100 
150 
200 
 
 
A2C-GP-Shield A2C-Eval backup 
0 1000 2000 3000 4000 5000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(a) cartpole (i) 
0 1000 2000 3000 4000 5000 6000 step 
0 
25 
50 
75 
100 
125 
Re wa 
rd 
A2C-GP-Shield A2C-Eval backup 
0 1000 2000 3000 4000 5000 6000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(b) cartpole (ii) 
0 2000 4000 6000 8000 10000 step 
25 
0 
25 
50 
75 
100 
 
 
A2C-GP-Shield A2C-Eval backup 
0 2000 4000 6000 8000 10000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(c)mountain_car 
0 1000 2000 3000 4000 5000 step 
0 
10 
20 
30 
Re wa 
rd 
A2C-GP-Shield A2C-Eval backup 
0 1000 2000 3000 4000 5000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(d) obstacle 
0 2000 4000 6000 8000 10000 step 
0 
10 
20 
30 
 
 
A2C-GP-Shield A2C-Eval backup 
0 2000 4000 6000 8000 10000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(e) obstacle2 
0 2000 4000 6000 8000 10000 step 
0 
10 
20 
30 Re 
wa rd 
A2C-GP-Shield A2C-Eval backup 
0 2000 4000 6000 8000 10000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(f) obstacle3 
0 2000 4000 6000 8000 10000 step 
0 
10 
20 
30 
 
 
A2C-GP-Shield A2C-Eval backup 
0 2000 4000 6000 8000 10000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(g) obstacle4 
0 1000 2000 3000 4000 5000 step 
10 
0 
10 
20 
Re wa 
rd 
A2C-GP-Shield A2C-Eval backup 
0 1000 2000 3000 4000 5000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(h) road 
0 1000 2000 3000 4000 5000 step 
60 
40 
20 
0 
20 
Re wa 
rd 
A2C-GP-Shield A2C-Eval backup 
0 1000 2000 3000 4000 5000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
A2C-GP-Shield A2C-Eval backup 
(i) road_2d 
Figure 3: Learning curves (reward and safety probability) for A2C-Shield and A2C-Eval.
0 1000 2000 3000 4000 5000 step 
0 
20 
40 
60 
80 
Ov er 
rid es 
A2C-GP-Shield 
(a) cartpole (i) 
0 1000 2000 3000 4000 5000 6000 step 
100 
120 
140 
160 
180 
200 
Ov er 
rid es 
A2C-GP-Shield 
(b) cartpole (ii) 
2000 4000 6000 8000 10000 step 
0 
100 
200 
300 
400 
500 
Ov er 
rid es 
A2C-GP-Shield 
(c) mountain_car 
0 1000 2000 3000 4000 5000 step 
0 
50 
100 
150 
Ov er 
rid es 
A2C-GP-Shield 
(d) obstacle 
0 2000 4000 6000 8000 10000 step 
0 
100 
200 
300 
 
 
A2C-GP-Shield 
(e) obstacle2 
0 2000 4000 6000 8000 10000 step 
100 
200 
300 
Ov er 
rid es 
A2C-GP-Shield 
(f) obstacle3 
0 2000 4000 6000 8000 10000 step 
0 
100 
200 
300 
Ov er 
rid es 
A2C-GP-Shield 
(g) obstacle4 
0 1000 2000 3000 4000 5000 step 
0 
20 
40 
60 
80 
Ov er 
rid es 
A2C-GP-Shield 
(h) road 
0 1000 2000 3000 4000 5000 step 
25 
50 
75 
100 
125 
150 
Ov er 
rid es 
A2C-GP-Shield 
(i) road_2d 
Figure 4: Overrides (per episode) for A2C-Shield
0 20000 40000 60000 80000 100000 step 
50 
100 
150 
200 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(a) cartpole (i) 
0 20000 40000 60000 80000 100000 step 
0 
50 
100 
150 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(b) cartpole (ii) 
0 20000 40000 60000 80000 100000 step 
50 
0 
50 
100 
 
 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(c) mountain_car 
0 20000 40000 60000 80000 100000 step 
0 
10 
20 
30 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.75 
0.80 
0.85 
0.90 
0.95 
1.00 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(d) obstacle 
0 20000 40000 60000 80000 100000 step 
0 
10 
20 
30 
 
 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(e) obstacle2 
0 20000 40000 60000 80000 100000 step 
0 
10 
20 
30 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(f) obstacle3 
0 20000 40000 60000 80000 100000 step 
0 
10 
20 
30 
 
 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(g) obstacle4 
0 20000 40000 60000 80000 100000 step 
0 
5 
10 
15 
20 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(h) road 
0 20000 40000 60000 80000 100000 step 
0 
10 
20 
 
 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(i) road_2d 
0 20000 40000 60000 80000 100000 step 
0 
200 
400 
600 
800 
1000 
Re wa 
rd 
CPO PPO-Lag 
0 20000 40000 60000 80000 100000 step 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
Sa fe 
ty  P 
ro b 
CPO PPO-Lag 
(j) Hopper-v5 
Figure 5: Learning curves (reward and safety probability) for CPO and PPO-Lag.
F ADDITIONAL ANALYSES F.1 Comparison to Sampling 
Effective number of samples. We first conduct a quick analyses to identify the effective number of samples required to reach a step-wise 
safety guarantee of 1 − 𝜖𝑡 = 0.9999 (with high probability 1 − 𝛿𝑡 ), where we conservatively set 𝛿𝑡 = 0.01. Bastani et al. [11] show that the 
number of samples required is, 
𝐾 (𝜖𝑡 , 𝛿) ≥ log(1/𝛿𝑡 ) 
log(1/(1 − 𝜖𝑡 )) + 1 
Plugging in 𝜖𝑡 = 0.00001 and 𝛿𝑡 = 0.01 gives 𝐾 ≈ 46000. We could not practically check this number of samples in a reasonable time, rather 
we tried 𝐾 ∈ {5, 10, 50, 100, 500, 1000, 5000}, noting that 𝑘 = 5000 gives an effective guarantee of 1 − 𝜖𝑡 ≈ 0.999 (with high probability 1 − 𝛿𝑡 ). 
Runtime comparison. We now conduct a runtime comparison for action selection when using our analytic Gaussian approximation 
detailed in Sec. 4, compared to (approximately) sampling from the posterior distribution. Rather than draw exact samples from the posterior 
distribution (which scales cubically in the number of inputs 𝐷 and is far too slow) we approximate the model’s kernel with a Fourier function 
decomposition ˆ𝑓 (𝑥 (·)) =∑𝑚 
𝑖=1 𝜙𝑖 (𝑥 (·)) · 𝜃𝑖 , where 𝜙𝑖 is the 𝑖th Fourier feature sampled from the model’s kernel and 𝜃𝑖 is a sample from the 
standard Gaussian [41], by default𝑚 = 500. 
Functionally, this form of the posterior distribution uses the same Fourier feature samples to evaluate all queries, meaning evaluating the 
posterior has a constant cost regardless of the number of posterior samples that are drawn. While the computational complexity of drawing 
samples is significantly reduced, the practical containment checks still scale 𝑂 (𝑁𝐾) where 𝑁 is the recovery horizon and 𝐾 is the number 
of samples, at some point this term dominates the complexity of drawing samples, revealing an inherent limitation with sampling-based 
approaches, see Tab. 2 and Tab. 3 
Table 2: Runtime comparison (seconds) for gaussian_approx and posterior_sampling_approx on cartpole (𝑛 = 4), with GP posterior with 𝐷 = 1000 inputs. 
Recovery Horizon 
gaussian_approx posterior_sampling_approx (𝜖𝑡 = 0.9999) 𝐾 = 5 𝐾 = 10 𝐾 = 50 𝐾 = 100 𝐾 = 500 𝐾 = 1000 𝐾 = 5000 
𝑁 = 5 0.749 0.537 0.533 0.648 0.619 0.683 0.910 6.890 
𝑁 = 10 1.090 0.985 1.015 1.151 1.149 1.241 1.659 12.614 
𝑁 = 20 1.652 1.857 1.911 2.221 2.159 2.358 3.155 35.563 
𝑁 = 40 2.788 3.634 3.804 4.247 4.278 4.649 6.162 47.005 
𝑁 = 100 6.495 8.857 8.764 10.566 10.482 11.294 15.187 115.771 
Table 3: Runtime comparison (seconds) for gaussian_approx and posterior_sampling_approx on cartpole (𝑛 = 4), with SGPR posterior [54] with 𝐷 = 5000 inputs and 𝑍 = 500 inducing points. 
Recovery Horizon 
gaussian_approx posterior_sampling_approx (𝜖𝑡 = 0.9999) 𝐾 = 5 𝐾 = 10 𝐾 = 50 𝐾 = 100 𝐾 = 500 𝐾 = 1000 𝐾 = 5000 
𝑁 = 5 0.703 15.752 15.794 16.135 16.284 17.591 19.841 47.535 
𝑁 = 10 1.230 28.854 28.943 29.562 29.845 32.243 36.369 87.142 
𝑁 = 20 2.384 55.087 55.253 56.441 56.992 61.547 69.431 166.362 
𝑁 = 40 4.353 107.614 107.881 110.180 111.251 120.161 135.552 324.794 
𝑁 = 100 10.4313 264.880 265.655 271.443 274.051 296.042 333.899 800.059 
F.2 Skew and kurtosis To verify assumption (iii) in Theorem 4.1, we conduct a skewness and kurtosis analysis for each of our environments used in our experimental 
evaluation (Sec. 6). In particular, we first train a GP posterior 𝑓 using data collected during the training dynamics of a given run. We then 
sample a random initial point and run the posteror_sampling_approx subroutine to generate an empirical distribution of 𝐾 points for 
each 𝑡 = 0, 1, . . . 𝑁 . We denote �̃� (𝑡) = [𝑥1 (𝑡), . . . , 𝑥𝐾 (𝑡)] as the empirical set of points for each 𝑡 = 0, 1, . . . 𝑁 . We then compute Mardia’s 
skewness and kurtosis, i.e., for some 𝑡 = 0, 1, . . . 𝑁 we have, 
skew(𝑡) = 1 
𝐾2 
𝐾∑︁ 𝑖=1 
𝐾∑︁ 𝑗=1 
𝑚3 
𝑖 𝑗 (𝑡), kurt(𝑡) = 1 
𝐾 
𝐾∑︁ 𝑖=1 
𝑚2 
𝑖𝑖 (𝑡)
where, 
𝑚𝑖 𝑗 (𝑡) = (�̃�𝑖 (𝑡) − 𝑋 (𝑡))𝑆 (𝑡)−1 (�̃�𝑖 (𝑡) − 𝑋 (𝑡)) (Mahalanobis distance) 
𝑆 (𝑡) = 1 
𝐾 
𝐾∑︁ 𝑖=0 
(𝑥𝑖 (𝑡) − 𝑋 (𝑡)) (𝑥𝑖 (𝑡) − 𝑋 (𝑡))𝑇 
𝑋 (𝑡) = 1 
𝐾 
𝐾∑︁ 𝑖=0 
𝑥𝑖 (𝑡) 
For truly multivariate distributions we should see, 
skew(𝑡) → 0, kurt(𝑡) → 𝑛(𝑛 + 2) as 𝐾 →∞. Since we can only (approximately) sample a finite number of points 𝐾 we setup the usual test statistics. For Mardia’s skewness if 
the empirical sample comes from a multivariate normal distribution then, 
𝐾 
6 
skew(𝑡) ∼ 𝜒2 
( 𝑛(𝑛 + 1(𝑛 + 2)) 
6 
) the skewness is considered negligible here if the 𝑝-value > 0.05. For Mardia’s kurtosis if the empirical sample comes from a multivariate 
normal distribution then, 
|kurt(𝑡) − 𝑛(𝑛 + 2) | 
√︄ 𝐾 
8𝑛(𝑛 + 2) ∼ 𝑁 (0, 1) 
Thus if kurt(𝑡) is within 1-2 standard errors of 𝑛(𝑛 + 2) this is acceptable, we can setup the usual test statistic for the standard normal 
distribution and check if the 𝑝-value > 0.05. We present the following skewness and kurtosis analysis for each environment below in tabular 
format. For the most part the skewness and kurtosis is negligible across all of our environments, passing the statistical tests (or marginally 
failing some). We note that any discrepancies could also be down to the bias introduced in the approximate sampling procedure used (see 
Sec. F.1). 
Tabular results. We present all the results in tabular form, in each instance 𝐾 = 5000 samples were taken for highly robust estimates of the 
skewness and kurtosis. 
Table 4: Skewness and kurtosis analysis on cartpole (𝑛 = 4) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 0 Pass 0.0228 0.5245 Pass 24.0808 0.6803 Pass 
𝑡 = 1 Pass 0.0244 0.4374 Pass 24.0433 0.8252 Pass 
𝑡 = 2 Pass 0.0313 0.1629 Pass 24.0392 0.8416 Pass 
𝑡 = 3 Pass 0.0339 0.1038 Pass 24.1253 0.5225 Pass 
𝑡 = 4 Pass 0.0280 0.2745 Pass 24.0372 0.8495 Pass 
𝑡 = 5 Pass 0.0287 0.2456 Pass 24.2263 0.2482 Pass 
𝑡 = 6 Pass 0.0367 0.0607 Pass 24.1273 0.5160 Pass 
𝑡 = 7 Pass 0.0354 0.0786 Pass 24.0859 0.6613 Pass 
𝑡 = 8 Fail 0.0410 0.0250 Fail 24.2315 0.2374 Pass 
𝑡 = 9 Fail 0.0299 0.2054 Pass 24.4235 0.0307 Fail 
𝑡 = 10 Fail 0.0232 0.5016 Pass 24.5831 0.0029 Fail 
... 
𝑡 = 90 Pass 0.0202 0.6647 Pass 23.8474 0.4361 Pass 
𝑡 = 91 Pass 0.0244 0.4350 Pass 24.0161 0.9345 Pass 
𝑡 = 92 Pass 0.0286 0.2499 Pass 24.1215 0.5352 Pass 
𝑡 = 93 Pass 0.0326 0.1303 Pass 24.2817 0.1506 Pass 
𝑡 = 94 Pass 0.0287 0.2476 Pass 24.2922 0.1359 Pass 
𝑡 = 95 Pass 0.0247 0.4220 Pass 24.0463 0.8131 Pass 
𝑡 = 96 Pass 0.0301 0.1972 Pass 23.9203 0.6844 Pass 
𝑡 = 97 Pass 0.0306 0.1839 Pass 23.9490 0.7947 Pass 
𝑡 = 98 Pass 0.0295 0.2174 Pass 23.9738 0.8934 Pass 
𝑡 = 99 Pass 0.0260 0.3601 Pass 23.8628 0.4838 Pass 
𝑡 = 100 Pass 0.0175 0.8001 Pass 23.9352 0.7407 Pass
Table 5: Skewness and kurtosis analysis on mountain_car (𝑛 = 2) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 0 Pass 0.0049 0.3999 Pass 8.1132 0.3169 Pass 
𝑡 = 1 Fail 0.0132 0.0269 Fail 8.0025 0.9824 Pass 
𝑡 = 2 Fail 0.0141 0.0191 Fail 7.8566 0.2050 Pass 
𝑡 = 3 Pass 0.0095 0.0935 Pass 7.9025 0.3889 Pass 
𝑡 = 4 Pass 0.0109 0.0595 Pass 7.9244 0.5043 Pass 
𝑡 = 5 Pass 0.0099 0.0834 Pass 8.0009 0.9938 Pass 
𝑡 = 6 Pass 0.0017 0.8399 Pass 7.9185 0.4714 Pass 
𝑡 = 7 Pass 0.0013 0.8930 Pass 7.9599 0.7228 Pass 
𝑡 = 8 Pass 0.0009 0.9413 Pass 7.9219 0.4899 Pass 
𝑡 = 9 Pass 0.0068 0.2285 Pass 7.8764 0.2745 Pass 
𝑡 = 10 Pass 0.0072 0.2002 Pass 8.0056 0.9608 Pass 
... 
𝑡 = 70 Pass 0.0014 0.8863 Pass 8.0283 0.8025 Pass 
𝑡 = 71 Pass 0.0006 0.9720 Pass 7.9748 0.8235 Pass 
𝑡 = 72 Pass 0.0007 0.9658 Pass 8.0059 0.9584 Pass 
𝑡 = 73 Pass 0.0002 0.9978 Pass 7.9946 0.9621 Pass 
𝑡 = 74 Pass 0.0011 0.9268 Pass 8.0131 0.9081 Pass 
𝑡 = 75 Pass 0.0019 0.8148 Pass 8.0321 0.7764 Pass 
𝑡 = 76 Pass 0.0029 0.6525 Pass 8.0448 0.6922 Pass 
𝑡 = 77 Pass 0.0025 0.7221 Pass 8.0364 0.7479 Pass 
𝑡 = 78 Pass 0.0019 0.8191 Pass 7.8971 0.3631 Pass 
𝑡 = 79 Pass 0.0018 0.8222 Pass 7.9648 0.7560 Pass 
𝑡 = 80 Pass 0.0026 0.7002 Pass 7.9582 0.7117 Pass 
Table 6: Skewness and kurtosis analysis on obstacle (𝑛 = 4) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 0 Pass 0.0222 0.5542 Pass 24.2452 0.2108 Pass 
𝑡 = 1 Pass 0.0297 0.2123 Pass 23.8672 0.4980 Pass 
𝑡 = 2 Fail 0.0487 0.0042 Fail 23.7801 0.2618 Pass 
𝑡 = 3 Pass 0.0368 0.0595 Pass 23.8696 0.5057 Pass 
𝑡 = 4 Pass 0.0361 0.0684 Pass 23.7830 0.2681 Pass 
𝑡 = 5 Pass 0.0262 0.3484 Pass 23.7300 0.1682 Pass 
𝑡 = 6 Pass 0.0351 0.0826 Pass 23.7324 0.1721 Pass 
𝑡 = 7 Fail 0.0465 0.0072 Fail 24.1845 0.3465 Pass 
𝑡 = 8 Fail 0.0591 0.0003 Fail 24.1589 0.4174 Pass 
𝑡 = 9 Fail 0.0702 0.0000 Fail 23.7868 0.2765 Pass 
𝑡 = 10 Pass 0.0284 0.2575 Pass 23.6276 0.0574 Pass 
𝑡 = 11 Pass 0.0298 0.2084 Pass 23.8470 0.4349 Pass 
𝑡 = 12 Fail 0.0497 0.0033 Fail 23.9000 0.6099 Pass 
𝑡 = 13 Fail 0.0967 0.0000 Fail 24.1875 0.3385 Pass 
𝑡 = 14 Fail 0.0750 0.0000 Fail 24.1454 0.4580 Pass 
𝑡 = 15 Fail 0.0797 0.0000 Fail 24.0992 0.6128 Pass 
𝑡 = 16 Fail 0.0880 0.0000 Fail 24.0947 0.6289 Pass 
𝑡 = 17 Fail 0.1005 0.0000 Fail 24.2734 0.1630 Pass 
𝑡 = 18 Fail 0.0894 0.0000 Fail 24.1385 0.4798 Pass 
𝑡 = 19 Fail 0.1050 0.0000 Fail 24.5370 0.0061 Fail 
𝑡 = 20 Fail 0.1182 0.0000 Fail 24.5583 0.0044 Fail
Table 7: Skewness and kurtosis analysis on obstacle2/3/4 (𝑛 = 4) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 1 Pass 0.0139 0.9291 Pass 24.0364 0.8525 Pass 
𝑡 = 2 Pass 0.0313 0.1639 Pass 24.0531 0.7862 Pass 
𝑡 = 3 Pass 0.0352 0.0810 Pass 24.0604 0.7580 Pass 
𝑡 = 4 Pass 0.0303 0.1912 Pass 24.0422 0.8295 Pass 
𝑡 = 5 Fail 0.0463 0.0075 Fail 24.4101 0.0364 Fail 
𝑡 = 6 Fail 0.0676 0.0000 Fail 24.2153 0.2719 Pass 
𝑡 = 7 Fail 0.0485 0.0045 Fail 24.2753 0.1601 Pass 
𝑡 = 8 Pass 0.0371 0.0567 Pass 24.2335 0.2335 Pass 
𝑡 = 9 Pass 0.0359 0.0713 Pass 24.0308 0.8750 Pass 
𝑡 = 10 Pass 0.0351 0.0822 Pass 23.8916 0.5803 Pass 
𝑡 = 11 Fail 0.0517 0.0020 Fail 24.1671 0.3939 Pass 
𝑡 = 12 Fail 0.0566 0.0006 Fail 24.1577 0.4211 Pass 
𝑡 = 13 Fail 0.0594 0.0003 Fail 24.1114 0.5698 Pass 
𝑡 = 14 Fail 0.0688 0.0000 Fail 24.2100 0.2838 Pass 
𝑡 = 15 Fail 0.0789 0.0000 Fail 24.0984 0.6156 Pass 
𝑡 = 16 Fail 0.0956 0.0000 Fail 24.2683 0.1710 Pass 
𝑡 = 17 Fail 0.0851 0.0000 Fail 24.2325 0.2354 Pass 
𝑡 = 18 Fail 0.0848 0.0000 Fail 24.2235 0.2540 Pass 
𝑡 = 19 Fail 0.1003 0.0000 Fail 24.3562 0.0691 Pass 
𝑡 = 20 Fail 0.1063 0.0000 Fail 24.3329 0.0894 Pass 
Table 8: Skewness and kurtosis analysis on road (𝑛 = 2) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 0 Pass 0.0047 0.4179 Pass 8.1394 0.2179 Pass 
𝑡 = 1 Pass 0.0050 0.3840 Pass 8.0203 0.8577 Pass 
𝑡 = 2 Pass 0.0075 0.1803 Pass 7.8849 0.3090 Pass 
𝑡 = 3 Pass 0.0067 0.2320 Pass 7.8799 0.2885 Pass 
𝑡 = 4 Pass 0.0105 0.0673 Pass 8.0387 0.7323 Pass 
𝑡 = 5 Fail 0.0181 0.0045 Fail 8.0728 0.5198 Pass 
Table 9: Skewness and kurtosis analysis on road_2d (𝑛 = 4) with GP posterior with 𝐷 = 1000 inputs. 
overall pass skew(𝑡 ) skew 𝑝-value skew pass kurt(𝑡 ) kurt 𝑝-value kurt pass 
𝑡 = 0 Pass 0.0213 0.6065 Pass 24.1454 0.4582 Pass 
𝑡 = 1 Pass 0.0232 0.4977 Pass 23.6600 0.0827 Pass 
𝑡 = 2 Pass 0.0202 0.6635 Pass 23.8459 0.4317 Pass 
𝑡 = 3 Fail 0.0233 0.4936 Pass 24.4087 0.0370 Fail 
𝑡 = 4 Pass 0.0217 0.5827 Pass 23.9153 0.6657 Pass 
𝑡 = 5 Pass 0.0111 0.9799 Pass 24.0857 0.6618 Pass 
Qualitative results. We present a direct comparison between gaussian_approx and posterior_sampling_approx in Fig. 6. We start 
from an 𝜖-recoverable state [0.0, 0.0,−0.15, 0.3]𝑇 ∈ X in cartpole, computing the uncertainty sets E(0), . . . E(𝑁 ) with gaussian_approx and plotting the corresponding 1 − 𝜖𝑡 = 99.99% confidence intervals, in addition we (approximately) sample points with the subroutine 
posterior_sampling_approx. We see for all 𝑡 = 0, 1, . . . , 𝑁 the uncertainty sets E(0), . . . E(𝑁 ) capture the empirical samples and to the 
naked eye the empirical samples broadly follow multivariate Gaussian distributions with correct mean and variance.
0.20 0.15 0.10 0.05 0.00 pole angle 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
po le 
 a ng 
ul ar 
 v el 
co ity 
gaussian_approx v.s. posterior_sample_approx 
Figure 6: 𝐾 = 50 empirical samples and 99.99%-CI uncertainty sets E(0), . . . E(𝑁 ) for cartpole (i)/(ii), with GP posterior with 𝐷 = 400 inputs. 
G HYPERPARAMETERS AND ACCESS TO CODE Access to code. Code for the paper is not currently available publicly but will soon be made public via GitHub. All of our environments are 
implemented with the OpenAI Gym interface [15] 
Training details. For collecting all sets of experiments we has access to 2 NVIDIA Tesla A40 (48GB RAM) GPU and a 24-core/48 thread 
Intel Xeon CPU each with 32GB of additional CPU RAM. For computation of the linear backup policies and control invariant sets we use 
AROC [32] which is released under the GPLv3 license. Each run can typically take several hours to a day, depending on the environment 
and hyperparameters used. Our own implementation of A2C is written in Python with JAX [14] and inspired by Stable Baselines JAX 
(SBX) [44]. For GP dynamics learning (as mentioned in the paper) we use GPJAX [41]. For key dependencies we refer the reader to 
https://docs.jaxgaussianprocesses.com/ (MIT License). For CPO [1] and PPO-Lag [46], we use the implementations provided by Omnisafe 
[31], the code for running these benchmarks can also be found in the supplementary material however, for setup instructions please refer to 
the Omnisafe code base https://github.com/PKU-Alignment/omnisafe (Apache-2.0 license). 
Statistical significance. We report standard error bars for each of our experiments (c.f., Tab. 1). In particular, we used 5 random initializations 
(seeds) for each experiment. For the learning curves (plots) the error bars are non-parametric (bootstrap) 95% confidence intervals, provided 
by seaborn.lineplot with default parameters: errorbar=(‘ci’, 95), n_boot=1000. The error bars capture the randomness in the 
initialization of the task policy parameters, the randomness of the environment (observation noise and disturbances) and any randomness in 
the batch sampling. 
Hyperparameters. Tab. 10 details the default hyperparameters used for our approach. The hyperparameters vary across environments, 
in particular the recovery horizon 𝑁 ∈ [0, 100] varies depending on how quickly we expect the backup policy to recover the system 
state. For environment specific hyperparameters please refer to the configs.yaml provided in our implementation. We also provide the 
hyperparameters used as input to Omnisafe [31] for collecting the results for CPO [1] and PPO-Lag [46] in Tab. 11, anything not specified is 
assumed to be the default for Omnisafe. For hyperparameter for MPS and DMPS we refer the reader to [8].
Table 10: Default hyperparameters for A2C-Shield 
Name Symbol Value 
Shield 
Recovery horizon 𝑁 20 
Sigma coef. 𝑧 (𝜖𝑡 ) 3.82 (0.9999) 
Gaussian process 
Learning rate - 0.01 
Optim. iters. - 100 
Batch size - 64 
Buffer size |𝐸 | or 𝐷 1000 
Sparse - False 
Collapsed - False 
Num. inducing inp. - 500 
Actor-critic 
num. layers - 2 
num. units - 64 
actor opt. - adam 
actor lr - 3 × 10 −4 
actor clip norm - 0.5 
actor ent. coef. - 0.05 
critic opt. - adam 
critic lr - 1 × 10 −3 
critic clip norm - 0.5 
critic reg. coef - 1.0 
discount 𝛾 0.99 
gae lambda 𝜆gae 0.95 
polyak tau 𝜏polyak 0.02 
rollout horizon 𝐻 16 
num. posterior samples - 5 
num. starting states |𝐵 | 32 
(effective) batch size - 2560 
Optim. iters - 10
Table 11: Hyperparameter details for CPO and PPO-Lag. 
Name Symbol Value 
Shared 
Actor learning rate 𝜂 3 × 10 −4 
Discount factor 𝛾 {0.99, 0.997} Cost coefficient 𝑐 1.0 
Cost threshold - 0.01 
Cost gamma 𝛾𝑐 {0.99, 0.997} TD-lambda 𝜆 0.95 
Cost TD-lambda 𝜆𝑐 0.95 
Max grad norm - 0.5 
Entropy coefficient - 0.0 
Steps per epoch 𝑛 2048 
Update iterations (per epoch) 𝑘 10 
Batch size 𝐵 64 
CPO 
... 
PPO-Lag 
Initial Lagrangian multiplier 𝜆init 10.0 
Epsilon clip 𝜖clip 0.2 
H ENVIRONMENT DESCRIPTIONS H.1 Cartpole The cartpole problem (cartpole) [9] is a classic benchmark for non-linear dynamical systems, where the task is to balance the pole upright 
towards its stable equilibrium point. Fig. 7 visualizes the problem. 
Figure 7: Visualization of the cartpole dynamical system 
Dynamics. The system dynamics are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)3 (35) 
𝑥 (𝑡 + 1)2 = 𝑥 (𝑡)4 (36) 
𝑥 (𝑡 + 1)3 = 𝑚𝑝𝑙𝑥 (𝑡)24 sin(𝑥 (𝑡)2) cos(𝑥 (𝑡)2)2 
(4/3) (𝑚𝑐 +𝑚𝑝 )2𝑙 −𝑚𝑝 (𝑚𝑐 +𝑚𝑝 )𝑙 cos(𝑥 (𝑡)2)2 
− (𝑚𝑐 +𝑚𝑝 )𝑔 cos(𝑥 (𝑡)2) sin(𝑥 (𝑡)2) + cos(𝑥 (𝑡)2)2𝐹𝑢 (𝑡) (4/3) (𝑚𝑐 +𝑚𝑝 )2𝑙 −𝑚𝑝 (𝑚𝑐 +𝑚𝑝 )𝑙 cos(𝑥 (𝑡)2)2 
+ 𝐹𝑢 (𝑡) +𝑚𝑝𝑙𝑥 (𝑡)24 sin(𝑥 (𝑡)2) 
𝑚𝑐 +𝑚𝑝 
+𝑤 (𝑡)1 
(37) 
𝑥 (𝑡 + 1)4 = (𝑚𝑐 +𝑚𝑝 )𝑔 sin(𝑥 (𝑡) − 2) 
(4/3) (𝑚𝑐 +𝑚𝑝 )𝑙 −𝑚𝑝𝑙 cos(𝑥 (𝑡)2)2 
− 𝑚𝑝𝑙𝑥 (𝑡)24 sin(𝑥 (𝑡)2) cos(𝑥 (𝑡)2) + cos(𝑥 (𝑡)2)𝐹𝑢 (𝑡) 
(4/3) (𝑚𝑐 +𝑚𝑝 )𝑙 −𝑚𝑝𝑙 cos(𝑥 (𝑡)2)2 +𝑤 (𝑡)2 
(38) 
where 𝑥 (𝑡)1 is the position of the cart, 𝑥 (𝑡)3 is the velocity of the cart, 𝑥 (𝑡)2 is the angle of the pole and 𝑥 (𝑡)4 is the angular velocity of the 
pole. In addition, 𝑢 (𝑡) is the force applied, with 𝐹 = 10 being the force magnifier,𝑚𝑐 = 1 is the mass of the car,𝑚𝑝 = 0.1 is the mass of the 
pole, 𝑙 = 0.5 is the length of the pole and 𝑔 = 9.8 is gravity.
Constraints. The state and action constraints areX = [−4.8, 4.8]×[−0.4190, 0.4190]×[−∞,∞]×[−∞,∞] ⊂ R4 andU = {[−1.0, 1.0]} ⊂ R. 
The safety constraints are given by the box constraints, Xsafe = [−2.4, 2.4] × [−0.2095, 0.2095] × [−∞,∞] × [−∞,∞] ⊂ R4 . The disturbances 
are drawn uniformly from the setW = [−0.001, 0.001] × [−0.001, 0.001] ⊂ R2 , the observed noise variances are 𝜎2 
𝑖 = 1 × 10 −6 
for all 
𝑖 = 1, · · · , 𝑛. Initial state. The initial state is sampled uniformly from X0 = [−0.5, 0.5]4 Reward. We consider 3 different reward functions in this environment: (i) 𝑟 (𝑡) = +1 if 𝑥 (𝑡 + 1) ∈ Xsafe otherwise 0, (ii) 𝑟 (𝑡) = +1 if 𝑥 (𝑡 + 
1)1 ≥ 0.1 otherwise 0, (iii) 𝑟 (𝑡) = +1 if 𝑥 (𝑡 + 1)2 ≥ 0.1 otherwise 0 
Termination condition. The episode terminates either after 200 timesteps or when the current system state leaves Xsafe. Backup policy. The backup policy 𝜋backup is given by the feedback matrix, 𝐾 = [−0.7488,−1.2280,−7.2758,−1.7787]𝑇 , computed via LQR 
using a linearization (matrices 𝐴,𝑏) of the environment dynamics around the stable equilibrium point 𝑥𝑒𝑞 . The equilibrium state control is 
also 𝑢𝑒𝑞 = 0. Control invariant set. Computed using AROC [32], with feedback matrix 𝐾 (see above) around the equilibrium point 𝑥𝑒𝑞 = 0 taking 
into account the disturbancesW and observation noiseV = diag( [𝜎2 
1 , . . . , 𝜎2 
𝑛]) (with each 𝜎2 
𝑖 = 1 × 10 −6 ). 
H.2 Mountain car Mountain car (mountain_car) [40] is another classical control problem, the goal is to escape a sinusoidal valley to the top of the ‘mountain’, 
where the only possible actions that can be taken are to accelerate the car left or right. The car is under-actuated, meaning it cannot escape 
the valley by simply going right, it must plan a long trajectory using the valley to build up momentum before progressing to the top of the 
mountain. Fig. 8 visualizes the problem. 
Figure 8: Visualization of the mountain car problem 
Dynamics. The system dynamics are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)1 + 𝑥 (𝑡 + 1)2 (39) 
𝑥 (𝑡 + 1)2 = 𝑥 (𝑡)2 + 𝐹𝑢 (𝑡) − 𝑔 cos(3𝑥 (𝑡)1) +𝑤 (𝑡) (40) 
where, 𝑥 (𝑡)1 is the position of the car and 𝑥 (𝑡)2 is the velocity of the car, 𝑢 (𝑡) is the force applied, with 𝐹 = 0.00015 being the force dampener, 
and 𝑔 = 0.0025 representing ‘gravity’. 
Constraints. The state and action constraints are X = [−1.2, 0.6] × [−0.07, 0.07] ⊂ R2 andU = {[−1.0, 1.0]} ⊂ R. The safety constraints 
are given by the box constraints, Xsafe = [−1.2,∞] × [−∞,∞] ⊂ R2 , this corresponds to not ‘hitting’ or ‘falling off’ the left hand side of the 
valley. The disturbances are drawn uniformly from the setW = [−0.001, 0.001] ⊂ R2 , the observed noise variances are 𝜎2 
𝑖 = 1 × 10 −6 
for all 
𝑖 = 1, · · · , 𝑛. Initial state. The initial velocity is always 0.0, but the initial car position state is sampled uniformly from [−0.6,−0.4], i.e., X0 = 
[0.0, 0.0] × [−0.6,−0.4] Reward. A reward of +100 is achieved by reaching the goal position 0.45 at the top of the mountain, otherwise the agent is penalized for 
the magnitude of its actions. Formally, 𝑟 (𝑡) = 100 if 𝑥 (𝑡 + 1)1 ≥ 0.45 otherwise − 0.1 · ∥𝑢 (𝑡)∥. Termination condition. The episode terminates either after 1000 timesteps or after reaching the target position 0.45. 
Backup policy. The backup policy 𝜋backup is given by the feedback matrix, 𝐾 = [0.7625, 34.5971]𝑇 , computed via LQR using a linearization 
(matrices 𝐴,𝑏) of the environment dynamics around the stable equilibrium point 𝑥𝑒𝑞 = [0.0,−𝜋/6]𝑇 . The equilibrium state control here is 
𝑢𝑒𝑞 = 0. Control invariant set. Computed using AROC [32], with feedback matrix 𝐾 (see above) around the equilibrium point 𝑥𝑒𝑞 taking into 
account the disturbancesW and observation noiseV = diag( [𝜎2 
1 , . . . , 𝜎2 
𝑛]) (with each 𝜎2 
𝑖 = 1 × 10 −6 ). 
H.3 Obstacle (2/3/4) We consider two simple obstacle navigation scenarios (obstacle and obstacle2/3/4). The agent is point that must navigate a 2D plane to 
reach a goal position, while avoiding an unsafe zone which corresponds on an obstacle. The agent can apply force to accelerate (or decelerate) 
along each of the two axes.
Dynamics. The system dynamics for obstacle are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)1 + 2𝑥 (𝑡 + 1)3 (41) 
𝑥 (𝑡 + 1)2 = 𝑥 (𝑡)2 + 2𝑥 (𝑡 + 1)4 (42) 
𝑥 (𝑡 + 1)3 = 𝑥 (𝑡)3 + 5𝐹𝑢 (𝑡)1 +𝑤 (𝑡)1 (43) 
𝑥 (𝑡 + 1)4 = 𝑥 (𝑡)4 + 5𝐹𝑢 (𝑡)2 +𝑤 (𝑡)2 (44) 
(45) 
where, 𝑥 (𝑡)1 and 𝑥 (𝑡)2 are the x/y position of the agent, 𝑥 (𝑡)3 and 𝑥 (𝑡)4 are the x/y velocity of the agent, 𝑢 (𝑡)1 and 𝑢 (𝑡)2 are the x/y force 
applied to the agent, 𝐹 = 0.001 is the force dampener. 
The system dynamics for obstacle2/3/4 are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)1 + 𝑥 (𝑡 + 1)3 (46) 
������ (𝑡 + 1)2 = 𝑥 (𝑡)2 + 𝑥 (𝑡 + 1)4 (47) 
𝑥 (𝑡 + 1)3 = 𝑥 (𝑡)3 + 2𝐹𝑢 (𝑡)1 +𝑤 (𝑡)1 (48) 
𝑥 (𝑡 + 1)4 = 𝑥 (𝑡)4 + 2𝐹𝑢 (𝑡)2 +𝑤 (𝑡)2 (49) 
(50) 
where, 𝑥 (𝑡)1 and 𝑥 (𝑡)2 are the x/y position of the agent, 𝑥 (𝑡)3 and 𝑥 (𝑡)4 are the x/y velocity of the agent, 𝑢 (𝑡)1 and 𝑢 (𝑡)2 are the x/y force 
applied to the agent, 𝐹 = 0.001 is the force dampener. 
Constraints. For both obstacle and obstacle2 the state and action constraints are X = [−0.5, 3.5]2 × [−0.05, 0.05]2 ⊂ R4 and 
U = [−2.0, 2.0]2 ⊂ R2 . For obstacle the obstacle (unsafe zone) is in the position [0.0, 1.0] × [2.0, 3.0], for obstacle2 the obstacle (unsafe 
zone) is in the position [1.0, 2.0] × [1.0, 2.0]. The disturbances are drawn uniformly from the setW = [−0.001, 0.001]2 ⊂ R2 , the observed 
noise variances are 𝜎2 
𝑖 = 1 × 10 6 for all 𝑖 = 1, · · · , 𝑛. obstacle3 includes a non-convex combination of one elongated obstacle (unsafe 
zone) in position [1.5, 2.0] × [0.5, 2.0] and one boundary condition 𝑥4 (𝑡) < 2.5. obstacle4 is more complex still, it includes a non-convex 
combination of two obstacles at positions [1.5, 2.0] × [0.5, 2.0] Initial state. The initial is fixed at 0 ∈ R4 
Reward. Each environment has different goal regions: 
 For obstacle the goal is to reach 𝑥 (𝑡)1 ≥ 3.0 and 𝑥 (𝑡)2 ≥ 0.0, where the agent receives a reward +30. 
 For obstacle2 the goal is to reach 𝑥 (𝑡)1 ≥ 3.0 and 𝑥 (𝑡)2 ≥ 3.0, where the agent receives a reward +30. 
 For obstacle3 the goal is to reach 𝑥 (𝑡)1 ≥ 3.0 and 𝑥 (𝑡)2 ≥ 1.5, where the agent receives a reward +30. 
 For obstacle4 the goal is to reach 𝑥 (𝑡)1 ≥ 3.0 and 𝑥 (𝑡)2 ≥ 2.0, where the agent receives a reward +30. 
In addition, the agent is provided with a dense reward e.g., ∥𝑥 (𝑡 + 1)1 − 3.0∥ − ∥𝑥 (𝑡)1 − 3.0∥ (obstacle) to incentivise the agent to seek out 
the goal position. 
Termination condition. The episode terminates after 200 timesteps. 
Backup policy. The backup policy 𝜋backup is given by the feedback matrix, 
𝐾 = 
 0.0 0.0 
0.0 0.0 
30.6386 0.0 
0.0 30.6386 
 computed via LQR using a linearization (matrices 𝐴,𝑏) of the environment dynamics around the stable equilibrium point 𝑥𝑒𝑞 = 0. The equilibrium state control here is 𝑢𝑒𝑞 = 0. 
Control invariant set. Is the trivially the full state space. If the point mass can slow to a stationary position without intersecting with an 
unsafe zone (obstacle) or boundary condition within 𝑁 timesteps, then this is sufficient for safety checks. 𝑁 just needs to be large enough 
so that the agent halts in this time to stationary even from its top speed, for obstacle 𝑁 = 20 is sufficient for obstacle2/3/4 𝑁 = 40 is 
sufficient. 
H.4 Road We consider a simple road environment, in both along both the 1D line (road) and in the 2D plane (road_2d). The agent must navigate to a 
goal position in both of these environments, while adhering to a given speed limit. The agent can accelerate (or decelerate) along each of the 
axes.
Dynamics. The system dynamics for road are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)1 + 10𝑥 (𝑡 + 1)2 (51) 
𝑥 (𝑡 + 1)2 = 𝑥 (𝑡)2 + 10𝐹𝑢 (𝑡) +𝑤 (𝑡) (52) 
(53) 
where, 𝑥 (𝑡)1 is the position of the agent and 𝑥 (𝑡)2 is the velocity of the agent, 𝑢 (𝑡) is the force applied to the agent and 𝐹 = 0.0001 is the 
force dampener. 
The system dynamics for road_2d are governed by the equations: 
𝑥 (𝑡 + 1)1 = 𝑥 (𝑡)1 + 10𝑥 (𝑡 + 1)3 (54) 
𝑥 (𝑡 + 1)2 = 𝑥 (𝑡)2 + 10𝑥 (𝑡 + 1)4 (55) 
𝑥 (𝑡 + 1)3 = 𝑥 (𝑡)3 + 5𝐹𝑢 (𝑡)1 +𝑤 (𝑡)1 (56) 
𝑥 (𝑡 + 1)4 = 𝑥 (𝑡)4 + 5𝐹𝑢 (𝑡)2 +𝑤 (𝑡)2 (57) 
(58) 
where, 𝑥 (𝑡)1 and 𝑥 (𝑡)2 are the x/y position of the agent, 𝑥 (𝑡)3 and 𝑥 (𝑡)4 are the x/y velocity of the agent, 𝑢 (𝑡)1 and 𝑢 (𝑡)2 are the x/y force 
applied to the agent, 𝐹 = 0.0001 is the force dampener. 
Constraints. For road the state and action constraints are X = [−4.0, 4.0] × [−0.1, 0.1] ⊂ R and U = [−2.0, 2.0] ⊂ R. Similarly, for 
road_2d the state and action constraints are X = [−4.0, 4.0]2 × [−0.1, 0.1]2 ⊂ R2 andU = [−2.0, 2.0]2 ⊂ R2 
. The safety constraints are to 
ensure the absolute velocity in either direction is bounded by 0.01, in particular, for road we have Xsafe = [−∞,∞] × [−0.01, 0.01] ⊂ R2 and 
for road_2d we have Xsafe = [−∞,∞]2 × [−0.01, 0.01]2 ⊂ R2 . The disturbances are drawn uniformly from the setW = [−0.001, 0.001] ⊂ R 
orW = [−0.001, 0.001]2 ⊂ R2 , the observed noise variances are 𝜎2 
𝑖 = 1 × 10 −6 
for all 𝑖 = 1, · · · , 𝑛. Initial state. The initial is fixed at 0 ∈ R2 
or 0 ∈ R4 
Reward. For road the goal is to reach 𝑥 (𝑡)1 ≥ 3.0, where the agent receives a reward +20. For road_2d the goal is to reach 𝑥 (𝑡)1 ≥ 3.0 
and 𝑥 (𝑡)2 ≥ 3.0, where the agent receives a reward +20. In addition, for road the agent is provided with a dense reward ∥𝑥 (𝑡 + 1)1 − 3.0∥ − ∥𝑥 (𝑡)1 − 3.0∥ to incentivise the agent to seek out the goal position. Similarly, for road_2d the agent is provided with the dense reward 
∥𝑥 (𝑡 + 1)1:2 − [3.0, 3.0] ∥ − ∥𝑥 (𝑡)1:2 − [3.0, 3.0] ∥. Termination condition. The episode terminates either after 200 timesteps or after reaching the goal position. 
Backup policy. The backup policy 𝜋backup for road is given by the feedback matrix, 
𝐾 = [0.0, 14.0425]⊤ 
and for road2d analogously, 
𝐾 = 
 0.0 0.0 
0.0 0.0 
14.0425 0.0 
0.0 14.0425 
 computed via LQR using a linearization (matrices 𝐴,𝑏) of the environment dynamics around the stable equilibrium point 𝑥𝑒𝑞 = 0. The equilibrium state control here is 𝑢𝑒𝑞 = 0. 
Control invariant set. Here it is the full safe set Xsafe. This can be easily seen as for any velocity within the safe set Xsafe there exists some control 𝑢∗ that can decelerate the point mass. 
H.5 Hopper-v5: Environment setup and invariant set computation The Hopper-v5 environment simulates a 2D single-leg robot in MuJoCo with an 11-dimensional observation vector (joint angles and 
velocities excluding the horizontal root position) and a 3-dimensional torque control input (c.f., Fig. 9). 
Figure 9: Visualization of Hopper-v5
Dynamics. See [56]. Constraints. The state and action constraints are X = [−∞,∞]11 
andU = [−1.0, 1.0]3 respectively. The safety constraints Xsafe are used to ensure the hopper stays “healthy” and upright and no extreme values. In particular, all values of the state vector must remain in the 
range [−100, 100], the z-coordinate of the torse must lie in the range [0.7,∞] and the angle of the torse must lie in the range [−0.2, 0.2]. Disturbances are not considered here as the problem is complex, although the usual observation noise with assumed noise variances 
𝜎2 
𝑖 = 1 × 10 −6 
for all 𝑖 = 1, · · · , 𝑛 is present. 
Initial state. The initial state is sampled uniformly from X0 = [−0.005, 0.005]11 plus the 1.25 for the torso z-coordinate. 
Reward. The agent receives a reward of +1 for remaining healthy (safe), in addition they receive a bonus for moving forward, see [56] for 
precise details. 
Terminal condition. The episode terminates after either the agent is unhealthy or after 1000 timesteps. 
Backup policy. To construct the required control invariant set Xinv and backup controller 𝜋backup, we first linearized the MuJoCo dynamics 
about the nominal equilibrium 𝑥𝑒𝑞 , obtaining 𝐴,𝑏 matrices, the backup policy 𝜋backup is then obtained via LQR and is defined by the feedback 
matrix 𝐾 and further improved with Newton refinement to obtain 𝑢𝑒𝑞 and maintain the equilibrium state (𝑓 (𝑥𝑒𝑞, 𝑢𝑒𝑞) ≈ 𝑥𝑒𝑞). Thus, the linear feedback gain 𝐾 defines the local stabilizing law 𝑢 = 𝑢𝑒𝑞 − 𝐾 (𝑥 − 𝑥𝑒𝑞). 
Control invariant set.We then estimated Xinv as the largest verified ellipsoidal level set 
E(𝑃, 𝑐) = {𝑥 : (𝑥 − 𝑥𝑒𝑞)⊤𝑃 (𝑥 − 𝑥𝑒𝑞) ≤ 𝑐} such that trajectories under 𝑢 = 𝑢𝑒𝑞 − 𝐾 (𝑥 − 𝑥𝑒𝑞) remain within E(𝑃, 𝑐). The set radius parameter 𝑐 was expanded geometrically by a factor 
of two each iteration, up to MAX_GROW_STEPS = 8, using 256 Monte Carlo rollouts per candidate. Expansion was halted after three 
successful iterations, beyond which verification failed, indicating that the controller could no longer guarantee invariance. The final verified 
ellipsoid was converted to an inscribed axis-aligned box and convex hull to form the invariant polytope Xinv used by the shield. 
Although the computedXinv sufficed for local stabilization, it was extremely small relative to the Hopper’s operational range. Consequently, 
the shield classified nearly all encountered states as unrecoverable, leading to frequent interventions that prevented the learned policy from 
acting. This illustrates a key dependency of our framework: while only 𝜋backup and Xinv are needed for safety certification, the practical 
performance and permissiveness of the shield depend critically on the quality of these components.