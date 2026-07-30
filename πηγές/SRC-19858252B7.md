> Source: https://arxiv.org/pdf/2307.14316

Reinforcement Learning by Guided Safe Exploration 
Qisong Yanga;*, Thiago D. Simãob; *, Nils Jansenb, Simon H. Tindemansa and Matthijs T. J. Spaana 
aDelft University of Technology – The Netherlands bRadboud University, Nijmegen – The Netherlands 
Abstract. Safety is critical to broadening the application of reinforcement learning (RL). Often, we train RL agents in a controlled environment, such as a laboratory, before deploying them in the real world. However, the real-world target task might be unknown prior to deployment. Reward-free RL trains an agent without the reward to adapt quickly once the reward is revealed. We consider the constrained reward-free setting, where an agent (the guide) learns to explore safely without the reward signal. This agent is trained in a controlled environment, which allows unsafe interactions and still provides the safety signal. After the target task is revealed, safety violations are not allowed anymore. Thus, the guide is leveraged to compose a safe behaviour policy. Drawing from transfer learning, we also regularize a target policy (the student) towards the guide while the student is unreliable and gradually eliminate the influence of the guide as training progresses. The empirical analysis shows that this method can achieve safe transfer learning and helps the student solve the target task faster. 
1 Introduction Despite the numerous achievements of reinforcement learning (RL) [45, 35], safety concerns still prevent the wide adoption of RL [11]. The lack of knowledge about the environment forces standard agents to rely on trial-and-error strategies. However, this approach is incompatible with safety-critical scenarios [15]. For instance, recommender systems should not suggest extremist content [10]. Constrained Markov decision processes (CMDP) [4] express such safety constraints with a cost signal indicating unsafe interactions. Such costs are decoupled from the rewards to facilitate the learning of safe behaviours. 
Developments in safe RL have allowed us to learn safe policies in CMDPs. For instance, SAC-Lagrangian [19] combines the Soft Actor-Critic (SAC) [21, 22] algorithm with Lagrangian methods to learn a safe policy in an off-policy way. This algorithm solves high-dimensional problems with a sample complexity lower than onpolicy algorithms. Unfortunately, it only finds a safe policy at the end of the training process and may be unsafe while learning. In terms of safety, we consider episode-wise constraints instead of step-wise constraints, so a few unsafe actions are allowed in an episode. 
Some knowledge about the safety dynamics can ensure safety during learning. One can pre-compute unsafe behaviour and mask unsafe actions using a so-called shield [3, 26, 8], or start from an initially safe baseline policy and gradually improve its performance while remaining safe [2, 49, 56]. However, these approaches may necessitate numerous interactions with the environment before they 
∗ Equal contribution. 
s, c 
a 
s, r, c 
πb a 
π⋄ π⋄ 
source (controlled environment) target (real world) 
π⋄ π⊙ M⋄ M⊙ 
transfer distillation composition 
Figure 1. Transferring the Safe Guide (SaGui) policy π⋄ from the source task (⋄) to the target task (⊙) with three steps. 
find an adequate policy [59]. Moreover, reusing a pre-trained policy can have a detrimental effect, since the agent encounters a new trajectory distribution as the policy changes [24]. Therefore, we investigate how to efficiently solve a task without violating the safety constraints. 
We make two key observations. First, RL agents often learn in a controlled environment, such as a laboratory or a simulator, before being deployed in the real world [15]. Second, an agent can often benefit from expert guidance instead of solely relying on trial and error [36]. For instance, in autonomous driving, the driver agent can quickly learn by mimicking an expert’s behaviour to handle dangerous situations. Such a process is referred to as policy distillation. Fur-thermore, under expert guidance, the agent can safely explore before taking dangerous actions. 
Transfer learning [48] investigates how to improve the learning of a target task with some knowledge from a source task. In these settings, the source task may provide only partial knowledge of the target task. We adopt a transfer learning framework and refer to (i) the controlled environment as the source task (⋄) and (ii) the real world as the target task (⊙). In our setting, the controlled environment provides only the cost signals related to safety but not the reward signals of the target task in the real world. The central problem is then to avoid safety violations after the target task has been revealed. 
Our approach. We show how to transfer knowledge encoded by a policy to enhance safety. Here, we refer to the policy that has been learned in the source task as the safe guide (SaGui, Figure 1). The intuition is that, in the real world, the agent is guided to accomplish the target task in a safe manner. We propose to transfer SaGui from the source task to the target task. Our approach has three central steps: i) train the SaGui policy and transfer it to the target task; ii) distill the guide’s policy into a student policy which is dedicated to the target task, and iii) compose a behaviour policy that balances safe exploration (using the guide) and exploitation (using the student). 
As we train the guide in a reward-free constrained RL setting [34], the agent only observes the costs related to safety, and it does not access reward signals. This task-agnostic approach allows us to train a guide independently of the reward of the target task, so this guide can 
 
 
 
 
 
 
 
 
 
 
be useful for different reward functions. Furthermore, we assume the source task preserves the dynamics related to safety, which allows us to train a guide that can act safely when transferred to the target task. Inspired by advances in robotics where an agent is trained under strict supervision, we assume the source task is a simulated/controlled environment [40, 53]. Therefore, safety is not required while training the SaGui policy. Once the target task is revealed, SaGui safely collects the initial trajectories in the target environment and the student starts learning based on these trajectories. To ensure that the new policy quickly learns how to act safely, we also employ a policy distillation method, encouraging the student to imitate the guide. 
Contributions. Our main contributions are: we i) formalize transfer learning for RL from a safety perspective; ii) propose to guide learning using a task-agnostic agent with exploration benefits; iii) show how to adaptively regularize the student policy to the guide policy based on the student’s safety; iv) investigate when to sample from the student or from the guide to ensure safe behaviour in the target environment and fast convergence of the student policy; and v) demonstrate empirically that, compared to learning from scratch and adapting a pre-trained policy, our method can solve the target task faster without violating the safety constraints in the target task. 
2 Related Work Safe RL has multiple facets [15], ranging from alternative optimization criteria [54, 9] to safe exploration based on some prior knowledge [2, 3, 26, 44, 57, 42]. We review methods to train the guide and solve new tasks using a pre-trained policy. 
Multiple algorithms have been proposed for generalizing policies from reward-free RL for better performance in target tasks [60, 17, 43]. However, only a few works have considered reward-free RL with constraints [34, 39]. They focus on tabular and linear settings while we consider general function approximation algorithms. 
Work in transfer learning has leveraged meta-RL [14] for safe adaptation [18, 32, 30]. Our work is also related to curriculum learning [5, 51, 33]. We first train an agent to be safe and later solve a target task. However, our approach focuses on safe exploration and is able to transfer to tasks with different reward functions, so the guide’s training is ignored. 
Our work resembles certain safe transfer-RL frameworks [27, 57], which also leverage prior knowledge to aid learning in a target task. However, the SaGui framework differs from them in terms of safety definition, knowledge acquisition in the source task, or knowledge usage in the target task. Our prior knowledge is more effective for various downstream tasks, and SaGui is the only framework that is safe while learning in the target task. 
3 Background We formalize the safe RL problem and describe typical approaches. 
3.1 Constrained Markov Decision Processes 
We consider tasks formulated by constrained Markov decision processes (CMDPs) [4, 7]. A CMDP is defined as a tuple M = ⟨S,A,P, r, c, d, γ⟩: a state space S, an action space A, a probabilistic transition function P : S × A 7→ Dist(S), a reward function r : S × A 7→ [rmin, rmax], a cost function c : S × A 7→ [cmin, cmax], a safety threshold d ∈ R+, and a discount factor γ ∈ [0, 1). We also consider an initial state distribution ι : S 7→ [0, 1]. In a constrained RL problem, an agent interacts with a CMDP without 
knowledge about the transition, reward, and cost functions, generating a trajectory τ = ⟨(s0, a0, r0, c0, s 
′ 0), (s1, a1, r1, c1, s 
′ 1), · · · ⟩. A 
trajectory starts from s0 ∼ ι(·). Then, at each timestep t the agent is in a state st ∈ S, and takes an action at ∈ A. It subsequently gets a reward rt = r(st, at), a cost ct = c(st, at), and steps into a new state s′t ∼ P(· | st, at). This process repeats starting from st+1 = s′t until a terminal condition is met and a new trajectory starts. The goal is to learn a policy π that maximizes the expected discounted return such that the expected discounted cost-return remains below d: 
max π 
Eρπ 
[ ∞∑ t=0 
γtrt 
] s.t. Eρπ 
[ ∞∑ t=0 
γtct 
] ≤ d, (1) 
where ρπ indicates the trajectory distribution induced by s0 ∼ ι(·), at ∼ π(· | st), and st+1 ∼ P(· | st, at). We define the discounted return starting from s, a and following π as Qr 
π(s, a) = Eρπ 
[∑∞ t=0 γ 
trt ∣∣s0 = s, a0 = a 
] , and, similarly, the discounted 
cost-return Qc π(s, a). 
From the safe RL perspective, if a policy has an expected costreturn lower than the safety-threshold d, then this policy is considered safe. Therefore, the objective of a safe RL agent is to find a policy, among the safe policies, that has the highest expected return. 
3.2 Maximum Entropy Reinforcement Learning 
A common strategy to improve the exploration and robustness of RL agents is to favour policies that induce diverse behaviours [62, 13]. We can incorporate it in the safe RL main objective by augmenting the problem with a term that aims to maximize the policy entropy [20]: 
max π 
Eρπ 
[ ∞∑ t=0 
γt (rt+αH(π(st))) 
] s.t.Eρπ 
[ ∞∑ t=0 
γtct 
] ≤d, (2) 
where H(·) is the entropy of a distribution over a random variable, and α is the entropy weight. In general, this objective encourages the agent to use maximally stochastic policies. Alternatively, we can encourage the policy to have at least a minimum entropy H [22] by adding the following constraint to (1): 
Eρπ [− log(π(at | st))] ≥ H, ∀t, (3) 
where H is the given entropy threshold to ensure a minimum degree of randomness. This approach allows the policy to converge to a more deterministic behaviour than (2). Besides, it only requires the system’s designer to define H and it lets the RL agent automatically find a trade-off between the policy’s entropy and rewards. Therefore, α becomes an intrinsic parameter of the RL algorithm. 
The maximum entropy RL with safety constraint (2) can be solved by the SAC-Lagrangian (SAC-λ) [19] method. SAC-λ is a SAC-based method that has two critics and uses an adaptive entropy weight α (parameterized by θα) and an adaptive safety weight β (parameterized by θβ) to manage a trade-off among exploration, reward, and safety. The reward critic estimates the expected return Qr (parameterized by θR), possibly with an entropy bonus to promote exploration, while the safety critic estimates the cost-return Qc (parameterized by θC ) to encourage safety. The policy π is parameterized by θπ . Appendix A provides a detailed description of how to learn each component, including the losses. Throughout the paper, we represent learning rates with η, replay buffers with D, and losses with J . We only update α when a desirable H is given, so α is fixed whenever we use the formulation (2).
cost-return 
episode ∆ time to safety 
safety jump-start 
learning from scratch 
transfer safety 
threshold 
(a) Unsafe transfer 
cost-return 
episode 
safety threshold∆ time to safety 
transfer 
safety jump-start 
learning from scratch 
(b) Fully safe transfer. 
guided exploration 
episode 
∆ time to optimum 
return 
return jump-start 
conservative exploration 
optimal performance 
(c) Return transfer. 
Figure 2. Transfer metrics for safe reinforcement learning. Usually, we consider safety jump-start and ∆ time to safety. If we can develop agents that learn without violating the safety requirements, we can also consider return jump-start and ∆ time to optimum. 
4 Safe and Efficient Exploration Naturally, to train RL agents without violating the safety constraints, some prior knowledge is required [44]. Often, a safe initial policy collects the initial trajectories [2, 49, 56]. However, these approaches largely neglect how this policy is computed or what makes it effective. Therefore, we consider the problem of how to obtain an initial policy that can safely expedite learning in the target task. Next, we formalize the problem and provide an overview of our approach. 
4.1 Problem Setting 
We formalize our problem setting using the transfer learning (TL) framework. In general, TL allows RL agents to use expertise from source tasks to speed up the learning process on a target task [48, 61]. The source tasks {M⋄} should provide some knowledge K⋄ to an agent learning in the target task M⊙, such that, by leveraging K⋄, the agent learns the target taskM⊙ faster. 
As we are particularly interested in the safety properties of the transfer, we consider a reward-free source task, which only provides information about the safety dynamics. Moreover, we use a policy to encode the knowledge transferred. Formally, given a source task M⋄ = ⟨S⋄,A⋄,P⋄, ∅, c⋄, d⋄, ι⋄, γ⟩, we compute the policy π⋄ in the absence of a reward signal. This provides knowledge K⋄ = {π⋄} to help solving the target task M⊙ = ⟨S⊙,A⊙,P⊙, r⊙, c⊙, d⊙, ι⊙, γ⟩. 
To apply the source policy π⋄ in the target task S⊙, we have a mapping from the source state space to the target state space Ξ : S⊙ → S⋄. Then, we can define a target policy π⋄→⊙ as follows: π⋄→⊙(s) = π⋄(Ξ(s)). Furthermore, we assume the source taskM⋄ 
and target taskM⊙ share the same action space. Appendix B.1 describes how to obtain the source task based on Ξ and the target task. 
Assumption 1. A⋄ = A⊙ = A. 
To enable the knowledge transferable between tasks, having the same action spaces ensures that the policy learned in the source task is directly applicable to the target task. 
4.2 Transfer Metrics 
To evaluate a safe transfer RL algorithm, Figure 2(a) presents a schematic of metrics related to safety (inspired by transfer in RL [48]): safety jump-start indicates how much closer to the safety threshold the expected cost-return of an agent learning with the source knowledge is compared to the expected cost-return of an agent learning from scratch in the first episodes, and ∆ time to safety is the difference in the number of interactions required to become safe. 
Notice that a trained agent might start with an expected cost-return lower than the safety threshold, for instance, when the safety threshold in the source task is lower than in the target task (Figure 2(b)). 
In this case, safety jump-start would be the difference between the safety threshold and the cost-return of an agent learning from scratch. Similarly, the ∆ time to safety would be the number of interactions an agent learning from scratch needs to become safe. 
In the case of two methods that can solve the target task without violating the safety constraints, we can also consider the usual metrics of transfer learning with respect to the reward [48]. For instance, Figure 2(c) shows the initial improvement in terms of performance which we call return jump-start, and the time necessary to reach an optimum performance, which we call the ∆ time to optimum. 
Problem statement. We aim to maximize the safety jump-start (potentially preventing safety violations in the target task) and to reduce the time to optimum (improving exploration) when transferring a policy π⋄ from a source taskM⋄ to a target taskM⊙. 
4.3 Method Overview 
Recall that for our transfer setting, we consider a single source task that only provides the safety signals, which we use to train the guide. Without the reward signal, the guide aims to explore the world safely and efficiently. We are interested in using the guide’s safe exploration capabilities to train the student on the target task without violating the safety constraints. Notably, i) the guide and the student are trained separately; ii) the guide is only trained once and can support the training of different students; and iii) the guide only has access to safety information and no knowledge about the student’s task. 
To ensure the source policy is safe when deployed in the target task, we assume that the source task has a safety threshold lower than or equal to the target task, and Ξ is a state abstraction that preserves the safety dynamics, as formalized next. 
Assumption 2. The safety threshold of the target task upper bounds the safety threshold of the source task: d⋄ ≤ d⊙. 
Assumption 3. Ξ is a Qc π-irrelevance abstraction [31], therefore 
Ξ(s)=Ξ(s′)⇒ Qc π⊙(s, a) = Qc 
π⊙(s′, a), ∀s, s′ ∈ S⊙, a ∈ A, π⊙. 
Now, we can connect the expected cost-return of a policy on the source task to the expected cost-return on the target task. 
Lemma 1. Given Assumption 1 and Assumption 3, we have 
Qc,⋄ π⋄ (Ξ(s), a) = Qc,⊙ 
π⋄→⊙(s, a) ∀s ∈ S⊙, a ∈ A, π⋄. 
That is, the expected cost of a source policy is the same in the source task and in the target task. 
Proof. Appendix B.2 provides the proof.
Theorem 1. If Ξ is a Qc π-irrelevant state abstraction, then any pol-
icy that is safe on the source taskM⋄ is also safe when deployed on the target taskM⊙. 
Proof. 
Qc,⊙ π⋄→⊙(s, a) 
Lemma 1 = Qc,⋄ 
π⋄ (Ξ(s), a) Premise ≤ d⋄ 
Assumption 2 ≤ d⊙. 
It is important to note, however, that the reward function r⊙ in the target task may be unrelated to the state space of the source task S⋄. Therefore, although a policy that is safe on the source task is also safe on the target task, the behaviour required to accomplish the target task may not be defined on the source task. Consider, for instance, an agent with access to its position and the position of a threat. In each target task, the agent might need to visit a different goal position, which is not defined in the source task. Then, a safe policy may be conditioned only on the positions of the agent and the threat, but to achieve the target, the agent must consider the goal position. This highlights the need to compute a policy dedicated to the target task. 
5 Guided Safe Exploration 
In this section, we consider how to train the safe guide (SaGui) policy. Then, we describe how the student learns to imitate the SaGui policy after the task is revealed while learning to complete the target task. Finally, we investigate how to prevent safety violations while the student has not yet learned how to act safely. 
5.1 Training the Safe Guide 
Since the source task does not provide information regarding the reward of the target task, we adopt a reward-free exploration approach to train the guide. To efficiently explore the world, we first consider maximizing the policy entropy under safety constraints. Then, we can solve the problem defined in Equation 2 with r(s, a) = 0 : ∀s ∈ S, a ∈ A to get a guide MAXENT. However, although MAXENT 
tends to have diverse behaviours, that does not imply efficient exploration of the environment. Especially for continuous state and action spaces, it is possible that a policy provides limited exploration even if it has high entropy. 
To enhance the exploration of the guide, we adopt an auxiliary reward that motivates the agent to visit novel states. To measure the novelty, we first define the metric space (S‡, δ), where S‡ is an abstracted state space and δ : S‡×S‡ → [0,∞) is a distance function: 
δ(s, s′) = 0⇔ s = s′, 
δ(s, s′) = δ(s′, s), and 
δ(s′, s′′) ≤ δ(s, s′) + δ(s, s′′), ∀s, s′, s′′ ∈ S. 
Note that S‡ may not be the original state space S. Especially when S is high-dimensional, S‡ can be some selected dimensions from S, or a latent space from representation learning. Next, we define the auxiliary rewards as the expected distance between the current state and the successor state: 
rδt (st, at) = Est+1∼P(·|st,at) 
[ δ(f‡(st), f 
‡(st+1)) ] , (4) 
where we may apply a potential abstraction f‡ : S → S‡. So, we train the guide agent by solving the constraint optimization problem (2) based on the auxiliary reward rδ . Then, we can use SAC-λ directly employed to solve (2), as Algorithm 2 shows (Appendix A). In 
Algorithm 1 Guided Safe Exploration 
Input:M⊙, π⋄,H, d Initialize: D ← ∅, θ⊙χ for χ ∈ {π,R,C, α, β} Output: Optimized parameters θ⊙π for π⊙ 
1: for each iteration do 2: for each environment step do 3: if linear-decay then 4: b← fld(⋄,⊙) ▷ linearly eliminate the effect of π⋄ 
5: else if control-switch then 6: b← fcs(⋄,⊙) ▷ π⋄ takes control if unsafe 7: end if 8: at ∼ πb(· | st) ▷ Composite sampling (6) 9: It ← I(st, at) ▷ IS ratio (7) 
10: r⊙t ← r⊙(st, at) 11: r⋄t ← log π⋄(at | Ξ(st)) 12: c⊙t ← c⊙(st, at) 13: st+1 ∼ P⊙(· | st, at) 14: D ← D ∪ {(st, at, r 
⊙ t , r⋄t , c 
⊙ t , It, st+1)} 
15: end for 16: for each gradient step do 17: Sample experience from D 18: for χ ∈ {π,R,C, α, β} do 19: θ⊙χ ← θ⊙χ − ηχ∇̂θ⊙χ 
IJχ(θ ⊙ χ ) ▷ Updating θ⊙χ 
20: end for 21: end for 22: end for 
future research, we will also investigate different distance functions to understand their effects on exploration. 
This auxiliary reward does not explicitly promote exploration, but we find that increasing the step size and policy entropy significantly improves exploration in practice. Overall, our experiment with the auxiliary reward aimed to evaluate the impact of the exploration of the guide on how safely and quickly the student learns. 
We could also consider more sophisticated reward-free exploration strategies such as maximizing the entropy of the state occupancy distribution [41, 47, 23]. We leave this as future work and focus on using the guide to improve how the student learns. 
5.2 Policy Distillation From the Safe Guide 
When the agent is trained for a certain task, it is difficult to generalize when faced with a new task [24]. Similarly, it is not trivial to adjust the guide’s policy that was trained to explore the environment to perform the target task. Therefore, we train a new policy, referred as the student, dedicated to the target task. 
We can leverage the guide to quickly learn how to act safely. Through the mapping function Ξ, the transferred policy can be used by most constrained RL algorithms to regularize the student policy π⊙ towards the guide policy π⋄ using KL divergences, as shown in Figure 3. So, with π⋄ fixed, we have an augmented reward function r′t = r⊙t + ωrKL 
t + αrHt , where rKL t = log π⋄(at|Ξ(st)) 
π⊙(at|st) 
and rHt = − log π⊙(at | st). The weights ω and α indicate the strengths of the KL and entropy regularization (respectively). Ap-pendix C shows that setting r⋄t = log π⋄(at | Ξ(st)) we obtain ωrKL+αrH = ωr⋄ + (ω + α)rH. Therefore, we can define the student’s objective: 
max π⊙ 
Eτ∼ρ π⊙ 
∞∑ t=0 
γt [ r⊙t + ωr⋄t + (α+ ω)rHt 
] . (5)
Student 
Guide 
s⋄ 
s⊙ Ξ(s⊙) 
Observation Reward 
r⊙ 
r⊙ + ωrKL 
DKL(π ⋄(·|s⋄)∥π⊙(·|s⊙)) 
Distillation Bonus 
safety-related 
safety-related 
reward-related 
π⊙(· | s⊙) 
π⋄(· | s⋄) 
rKL 
Figure 3. Overview of the policy distillation. Through the mapping function Ξ, the transferred policy can be used to regularize the student policy π⊙ 
towards the guide policy π⋄. 
To find an appropriate ω, our goal is to follow the guide more for safer exploration if the student’s policy is unsafe, but eliminate the influence from the guide and focus more on the performance if the student’s policy is safe. Therefore, we propose to set ω = β to determine the strength of the KL regularization since the adaptive safety weight β reflects the safety of the current policy. 
In summary, we have an entropy regularized expected return with redefined (regularized) reward r′′t = r⊙t + βr⋄t . This augmented reward encourages the student to yield actions that are more likely to be generated by the guide. Then, SAC-λ can be directly used to solve (5) with the additional entropy constraint (Algorithm 1, lines 16-19). 
5.3 Composite Sampling 
To enhance safety and improve the student during training (Algo-rithm 1, lines 2-14), we leverage a composite sampling strategy, which means our behaviour policy (πb) is a mixture of the guide’s policy (π⋄) and the student’s policy (π⊙). So, at each environment step, at ∼ πb(· | st), st ∈ S⊙ where 
πb(· | st) = 
{ π⋄(· | Ξ(st)), if b = ⋄, π⊙(· | st), otherwise. 
(6) 
We investigate two strategies to define b. Linear-decay (Algorithm 3 in Appendix D). This strategy, de-
noted as b = fld(⋄,⊙), linearly decreases the probability of using π⋄ 
with a constant decay rate after each iteration of the algorithm, conversely increasing the probability of using π⊙. We have two modes with linear-decay: step-wise, where in each time step we may change πb; and trajectory-wise, where πb only changes at the start of a trajectory. The mode is decided before executing an episode, and smoothly switches from the complete step-wise to the complete trajectory-wise over the training process. 
Control-switch (Algorithm 4 in Appendix D). To balance between the safe exploration and the sample efficiency (the samples from the target policy is relatively more valuable), the student policy keeps sampling, i.e., πb = π⊙ at the start of a trajectory; after we meet the first ct−1 > 0, we have πb = π⋄ until the end of the trajectory. Therefore, the guide policy serves as a rescue policy to improve safety during sampling. We denote this strategy as b = fcs(⋄,⊙). 
With the composite sampling strategy, the function approximation may diverge, because π⊙ and πb are too different, especially when we collect most data following π⋄. This phenomenon is related to the deadly triad [46]. To eliminate its negative effect, we endow each sample with an importance sampling (IS) ratio: 
I(s, a) = min 
( max 
( π⊙(a | s) πb(a | s) 
, Il ) , Iu 
) . (7) 
The clipping hyper-parameters Iu and Il are introduced to reduce the variance of the off-policy TD target. Notice that if πb is using the 
Figure 4. Navigation tasks with different complexity levels: static where all objects are fixed (left), semi-dynamic where the goal is randomly initialized before each episode (center), and dynamic where all objects are randomly initialized locations before each episode (right). 
student π⊙ then I(s, a) = 1. Here, in addition to use the IS ratio I for learning values (the critics), we also use it in the policy update, as shown in line 19 of Algorithm 1. 
6 Empirical Analysis 
We evaluate how well our method transfers from the reward-free setting using the SafetyGym engine [38], where a random-initialized robot navigates in a 2D map to reach target positions while trying to avoid dangerous areas and obstacles (Figure 4). These tasks are particularly complex due to the observation space; instead of observing its location, the agent observes the relative location of other objects with a lidar sensor. We considered three environments with different complexity levels. A static environment with a point robot and a hazard. The locations of the hazard and goal are fixed in all episodes. A semi-dynamic environment with a car robot, four hazards, and four vases. The locations of the hazards and vases are the same in all episodes. The location of the goal is randomly-initialized in each episode. A dynamic environment with a point robot, eight hazards, and a vase. The locations of the goal, vase, and hazards are randomlyinitialized in each episode. 
The guide agent is trained without the goals, and its auxiliary reward is the magnitude of displacement at each time step. We provide a detailed description of the safety-mapping function in Appendix G. Since our focus is on the target task and the guide is trained in a controlled environment, we do not consider the guide’s training in the evaluation. In the target tasks, we use the original reward signal from Safety Gym, i.e., the distance towards the goal plus a constant for finishing the task [38]. In all environments: c = 1, if an unsafe interaction happens, and c = 0, otherwise. We repeat each experiment 10 times with different random seeds and the plots show the mean and standard deviation of all runs. 
To evaluate the performance during training, we use the following metrics: safety of the behaviour policy (Cost-Return πb), performance of the behaviour policy (Return πb), safety of the target policy (Cost-Return π⊙), and performance of the target policy (Return π⊙). To check the convergence of the target policy, we have a test process with 100 episodes after each epoch (in parallel to the training) to evaluate Return π⊙ and Cost-Return π⊙. Appendix F reports the evaluation of π⊙ and Appendix G the hyperparameters used. The supplemental material provides the code of the experiments. 
6.1 Ablation Study 
We investigate each component of the proposed SAGUI algorithm individually to answer the following questions: i) Does the auxiliary reward enlarge the exploration range? ii) Does a better guide agent result in a better student in the target task? iii) How does the adaptive
Static Semi-Dynamic 
MAXENT SAGUI MAXENT SAGUI 
Figure 5. Exploration analysis with trajectories collected by the different guide agents in Static and Semi-Dynamic. 
strength of the KL regularization affect the performance? iv) How does the composite sampling benefit the safe transfer learning? 
i) Auxiliary reward leads to more diverse trajectories. We performed an ablation of our approach where no auxiliary reward is added while training the guide agent, called MAXENT. We refer to the agent with the auxiliary reward as SAGUI. This teases apart the role the designed auxiliary task plays in the exploration. In Figure 5, we can see that SAGUI can explore larger areas in Static and Semi-Dynamic, which have the same layout in each episode. We notice that MAXENT is safe, but the explored space is limited. That is also the case in Dynamic, as shown in the attached videos. 
ii) An effective guide can speed up the student’s training. We compare how these guides (MAXENT and SAGUI) affect the learning in the target task. In Figure 7 (Appendix E), we notice that both methods can collect samples safely, but the agent using the auxiliary reward needs fewer interactions to find high-performing policies. 
iii) Safety-adaptive regularization improves the student’s convergence rate. To combine the original reward with the bonus to follow the guide (ω), we have the following choices: fix the weights of the bonus and make it to be a hyperparameter to tune (FIXREG); apply a decay rate to linearly decrease the weights during training (DECREG); and, adapt the weights of the bonus based on the safety performance (SAGUI). In Figure 7(a) (Appendix E) we observe that this weight does not affect the safety of the agent, but both FIXREG and DECREG cause the student to converge slower in terms of performance (Figure 7(b) in Appendix E). 
iv) Composite sampling enhances safety and final performance. We modify the composite sampling approach, sampling only from the guide (GUISAM) or the student (STUSAM) instead. From the results in Figure 7(a) (Appendix E), we can see that GUISAM 
can ensure safety, but the student does not learn a safe optimal policy (Figure 7(b) in Appendix E). Compared to our method, STUSAM performs similarly converging to a safe target policy, but fails to satisfy the constraint at the early stage of training. So, composite sampling is necessary to avoid the dangerous actions from a naive policy and to ensure the target task is solved. 
6.2 Comparison with Baselines 
Finally, we compare □ SAGUI (control-switch) and □ SAGUI 
(linear-decay) with five baselines, divided into three groups. 
Learning from scratch. (1) □ SAC-λ [19] shows the performance when starting to learn from scratch, representing an off-policy algorithm. Similarly, (2) □ CPO [2] is an on-policy algorithm that maximizes the reward in a small neighbourhood to enforce the safety constraints. 
Pre-training. (3) □ CPO-PRE and (4) □ SAC-λ-PRE demonstrate how CPO and SAC-λ perform after being pre-trained in a task that replaces the target reward by the auxiliary reward. So, we also 
encourage exploration in the task for pre-training, which shares the same observation space with the target task. 
Expert-in-the-loop. (5) As an upper bound, we also consider the Expert Guided Policy Optimization (□ EGPO) [36] algorithm, which uses knowledge from the target task in the form of an expert to train a student policy. EGPO proposes a guardian mechanism that replaces the actions of the student by the expert when the student takes actions too different from the expert. In summary, EGPO uses an expert policy as a demonstrator as well as a safety guardian (see Appendix H for more details). 
Notice, for CPO-PRE, SAC-λ-PRE and EGPO we adapt the source task to have the same observation space as the target task, which gives them an advantage compared to SAGUI. Furthermore, EGPO has access to a policy trained on the target task, while SAGUI 
only has access to the source task without the goal observations. Safety during training. In Figure 6, we observe that SAGUI 
(control-switch) and EGPO are the only methods that exhibit safe behaviour during the full training process. 
Learning from scratch is unsafe and may converge to suboptimal and even unsafe policies. SAC-λ and CPO can learn safe policies in relatively simpler environments (Static and Semi-Dynamic) but they violate the safety constraints at the beginning of training, which is expected. In Dynamic, SAC-λ and CPO fail to attain safe performance. However, with benefits from the guide, SAGUI (control-switch), on the basis of SAC-λ, attains a better balance between safety and performance. 
Pre-training is insufficient. With pre-training, a safe initialization cannot benefit CPO-PRE and SAC-λ-PRE in safety, and may have negative effects. We infer that it is difficult to generalize a task when faced with a new reward signal [24]. Especially for SAC-λ-PRE with an initialized Qr , the difficulty to adapt is evident. 
Fast convergence rates. Benefiting from the targeted expert policy, the behaviour policy of EGPO has a high return throughout the training in the target environment. But SAGUI (controlswitch) quickly finds policies with similar performance despite lack of knowledge of the target task (Figure 6). 
The distillation mechanism ensures the safety of the target policy. Figure 8 (Appendix F) shows that SAGUI (control-switch) can learn a well-performing target policy in a safe way. Without the policy distillation mechanism like SAGUI, EGPO (learning only from the expert demonstrations) fails to find a safe target policy. This indicates that the target policy computed with SAGUI may eventually take full control of the target task, while the policy computed by EGPO may still require interventions from the expert. 
Control-switch can be more effective than linear-decay. SAGUI 
(linear-decay), which lacks samples from π⊙ at the early stage of training, does not achieve similar performance as SAGUI (controlswitch). Figures 6(b) and 6(c) show that linear-decay fails to compose the behaviour policy πb safely. 
Summary. Overall, SAGUI does not violate the safety constraints on the target environment, quickly finds high-performing policies, and can train a student able to act independently from the guide. 
7 Conclusion This work handles multiple challenges of reinforcement learning with safety constraints. It shows how we can use a safe exploration policy (the guide) during data collection and gradually switch to a policy that is dedicated to the target task (the student). It tackles the off-policy issue that arises from collecting data with a policy different from the target policy. It shows how the student can make the
0 100 
200 
300 
 
 
 
CPO CPO-PRE SAC-λ SAC-λ-PRE EGPO SaGui (linear-decay) SaGui (control-switch) 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
−1 
0 
1 
2 
3 
 
 
 
(a) Static 
0 
20 
40 
60 
80 
0.5 1.0 1.5 2.0 2.5 TotalEnvInteracts 1e6 
−4 
−2 
0 
2 
(b) Semi-Dynamic 
20 
40 
60 
80 
1 2 3 4 TotalEnvInteracts 1e6 
0 
10 
20 
30 
(c) Dynamic 
Figure 6. Evaluation of πb for CPO, CPO-PRE, SAC-λ, SAC-λ-PRE, EGPO, and SAGUI over 10 seeds. The solid lines are the average of all runs, and the shaded area is the standard deviation. The black dashed lines indicate the safety thresholds. 
best use of the guide’s policy using an incentive to imitate the guide, which makes the student learn faster how to behave safely. It demonstrates that simply initializing an agent with a safe policy may not be as effective as learning a new policy dedicated to the target task through policy distillation. Finally, it proposes a method that can collect diverse trajectories, which reduces the sample complexity of the student on the target task. In summary, the framework proposed is a safe and sample-efficient way of training the agent on a target task. 
Limitations. Our framework assumes that the source task provides information on the cost function, allowing the guide policy to accumulate the same cost in the target task as in the source task (Sec-tion 4.3). This assumption enables safe learning in the target task. However, if the cost function or trajectory distribution changes, the source task may not provide useful safety information for the target task. In such cases, alternative methods should be considered to ensure safe exploration. We focus on downstream tasks where pre-trained agents are utilized for safe exploration knowledge, disregarding the interactions used to train the SaGui policy. Sample efficiency in the target task is emphasized, not including samples used for source task learning. Nevertheless, the pre-trained policy can be reused for multiple target tasks, enabling us to amortize the guide’s training across them, making the number of samples required to train the guide negligible as the number of downstream tasks increases. While efficient learning of a SaGui policy is a significant challenge, we view it as a separate research direction [23]. 
Future work. While we consider a relatively simple strategy to achieve rich exploration, our framework allows the translation of any progress in reward-free RL into training the guide agent. For instance, we could adopt works with the entropy of the state density [23, 29, 41, 25, 60, 47, 52, 37, 55], or with the adaptive reward functions to explore various skills [12]. Another option to improve exploration is to find a set of diverse policies to the same problem [16, 28, 58]. Our framework could easily combine multiple guides. As to composite sampling strategies, recovery and shielding mechanisms [3, 50] could be further explored to combine with a safe guide, in particular using the control-switch mechanism that we evaluated. Nevertheless, we highlight that while a student using a recovery policy must explore alone, the safe guide can enhance the student’s exploration, accelerating the learning of the target task. 
Acknowledgements We thank the reviewers for their insightful comments. This work has been partially funded by the ERC Starting Grant 101077178 (DEUCE) and the NWO grant NWA.1160.18.238 (PrimaVera). Qisong Yang is supported by Xidian University. 
References [1] David Abel, D. Ellis Hershkowitz, and Michael L. Littman, ‘Near op-
timal behavior via approximate state abstraction’, in ICML, pp. 2915– 2923, (2016). 
[2] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel, ‘Con-strained Policy Optimization’, in ICML, pp. 22–31, (2017). 
[3] Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu, ‘Safe Reinforcement Learning via Shielding’, in AAAI, pp. 2669–2678, (2018). 
[4] Eitan Altman, Constrained Markov decision processes, volume 7, CRC Press, 1999. 
[5] Yoshua Bengio, Jérôme Louradour, Ronan Collobert, and Jason We-ston, ‘Curriculum learning’, in ICML, pp. 41–48, (2009). 
[6] Dimitri P Bertsekas, Constrained Optimization and Lagrange Multi-plier Methods, volume 1, Academic press, 1982. 
[7] Vivek S Borkar, ‘An actor-critic algorithm for constrained Markov decision processes’, Systems & control letters, 54(3), 207–213, (2005). 
[8] Steven Carr, Nils Jansen, Sebastian Junges, and Ufuk Topcu, ‘Safe reinforcement learning via shielding under partial observability’, in AAAI, pp. 14748–14756, (2023). 
[9] Yinlam Chow, Mohammad Ghavamzadeh, Lucas Janson, and Marco Pavone, ‘Risk-constrained reinforcement learning with percentile risk criteria’, JMLR, 18(1), 6070–6120, (2017). 
[10] Tommaso Di Noia, Nava Tintarev, Panagiota Fatourou, and Markus Schedl, ‘Recommender systems under european ai regulations’, Com-munications of the ACM, 65(4), 69–73, (2022). 
[11] Gabriel Dulac-Arnold, Nir Levine, Daniel J. Mankowitz, Jerry Li, Cos-min Paduraru, Sven Gowal, and Todd Hester, ‘Challenges of real-world reinforcement learning: definitions, benchmarks and analysis’, Mach. Learn., 110(9), 2419–2468, (2021). 
[12] Benjamin Eysenbach, Abhishek Gupta, Julian Ibarz, and Sergey Levine, ‘Diversity is all you need: Learning skills without a reward function’, in ICLR, (2019). 
[13] Benjamin Eysenbach and Sergey Levine, ‘Maximum entropy RL (provably) solves some robust RL problems’, in ICLR, (2022). 
[14] Chelsea Finn, Pieter Abbeel, and Sergey Levine, ‘Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks’, in ICML, pp. 1126–1135, (2017).
[15] Javier García and Fernando Fernández, ‘A Comprehensive Survey on Safe Reinforcement Learning’, JMLR, 16(1), 1437–1480, (2015). 
[16] Mahsa Ghasemi, Evan Scope Crafts, Bo Zhao, and Ufuk Topcu, ‘Multi-ple Plans are Better than One: Diverse Stochastic Planning’, in ICAPS, pp. 140–148, (2021). 
[17] Michael Gimelfarb, Andre Barreto, Scott Sanner, and Chi-Guhn Lee, ‘Risk-aware transfer in reinforcement learning using successor features’, in NeurIPS, pp. 17298–17310, (2021). 
[18] Djordje Grbic and Sebastian Risi, ‘Safe Reinforcement Learning through Meta-learned Instincts’, in ALIFE, pp. 183–291, (2020). 
[19] Sehoon Ha, Peng Xu, Zhenyu Tan, Sergey Levine, and Jie Tan, ‘Learn-ing to Walk in the Real World with Minimal Human Effort’, in CoRL, pp. 1110–1120, (2020). 
[20] Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine, ‘Reinforcement Learning with Deep Energy-Based Policies’, in ICML, pp. 1352–1361, (2017). 
[21] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine, ‘Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor’, in ICML, pp. 1861–1870, (2018). 
[22] Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan, Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, and Sergey Levine. Soft Actor-Critic Algorithms and Applica-tions, 2018. arXiv:1812.05905. 
[23] Elad Hazan, Sham Kakade, Karan Singh, and Abby Van Soest, ‘Prov-ably Efficient Maximum Entropy Exploration’, in ICML, pp. 2681– 2691, (2019). 
[24] Maximilian Igl, Gregory Farquhar, Jelena Luketina, Wendelin Boehmer, and Shimon Whiteson, ‘Transient Non-stationarity and Gen-eralisation in Deep Reinforcement Learning’, in ICLR, (2021). 
[25] Riashat Islam, Zafarali Ahmed, and Doina Precup. Marginalized State Distribution Entropy Regularization in Policy Optimization, 2019. arXiv:1912.05128. 
[26] Nils Jansen, Bettina Könighofer, Sebastian Junges, Alex Serban, and Roderick Bloem, ‘Safe Reinforcement Learning Using Probabilistic Shields (Invited Paper)’, in CONCUR, pp. 1–16, (2020). 
[27] Thommen George Karimpanal, Santu Rana, Sunil Gupta, Truyen Tran, and Svetha Venkatesh, ‘Learning transferable domain priors for safe exploration in reinforcement learning’, in IJCNN, pp. 1–10. IEEE, (2020). 
[28] Saurabh Kumar, Aviral Kumar, Sergey Levine, and Chelsea Finn, ‘One Solution is Not All You Need: Few-Shot Extrapolation via Structured MaxEnt RL’, in NeurIPS, p. 8198–8210, (2020). 
[29] Lisa Lee, Benjamin Eysenbach, Emilio Parisotto, Eric Xing, Sergey Levine, and Ruslan Salakhutdinov. Efficient Exploration via State Marginal Matching, 2019. arXiv:1906.05274. 
[30] Thomas Lew, Apoorva Sharma, James Harrison, Andrew Bylard, and Marco Pavone, ‘Safe Active Dynamics Learning and Control: A Se-quential Exploration–Exploitation Framework’, IEEE Transactions on Robotics, 38(5), 2888–2907, (2022). 
[31] Lihong Li, Thomas J Walsh, and Michael L Littman, ‘Towards a Uni-fied Theory of State Abstraction for MDPs’, in AI&M, pp. 1–10, (2006). 
[32] Michael Luo, Ashwin Balakrishna, Brijen Thananjeyan, Suraj Nair, Julian Ibarz, Jie Tan, Chelsea Finn, Ion Stoica, and Ken Goldberg. MESA: Offline Meta-RL for Safe Adaptation and Fault Tolerance, 2021. arXiv:2112.03575. 
[33] Luca Marzari, Davide Corsi, Enrico Marchesini, and Alessandro Farinelli, ‘Curriculum learning for safe mapless navigation’, in SAC, pp. 766–769, (2022). 
[34] Sobhan Miryoosefi and Chi Jin, ‘A simple reward-free approach to constrained reinforcement learning’, in ICML, pp. 15666–15698, (2022). 
[35] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin A. Riedmiller, Andreas Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis, ‘Human-level control through deep reinforcement learning’, Nature, 518(7540), 529– 533, (2015). 
[36] Zhenghao Peng, Quanyi Li, Chunxiao Liu, and Bolei Zhou, ‘Safe driving via expert guided policy optimization’, in CoRL, pp. 1554–1563, (2022). 
[37] Zengyi Qin, Yuxiao Chen, and Chuchu Fan, ‘Density Constrained Re-inforcement Learning’, in ICML, pp. 8682–8692, (2021). 
[38] Alex Ray, Joshua Achiam, and Dario Amodei. Benchmarking Safe Exploration in Deep Reinforcement Learning, 2019. https://cdn.openai. com/safexp-short.pdf. 
[39] Yagiz Savas, Melkior Ornik, Murat Cubuktepe, and Ufuk Topcu, ‘En-tropy Maximization for Constrained Markov Decision Processes’, in 56th Annual Allerton Conference on Communication, Control, and Computing, pp. 911–918, (2018). 
[40] Erik Schuitema, Martijn Wisse, Thijs Ramakers, and Pieter Jonker, ‘The design of LEO: A 2D bipedal walking robot for online autonomous Reinforcement Learning’, in IROS, pp. 3238–3243, (2010). 
[41] Younggyo Seo, Lili Chen, Jinwoo Shin, Honglak Lee, Pieter Abbeel, and Kimin Lee, ‘State Entropy Maximization with Random Encoders for Efficient Exploration’, in ICML, pp. 9443–9454, (2021). 
[42] Thiago D. Simão, Nils Jansen, and Matthijs T. J. Spaan, ‘AlwaysSafe: Reinforcement Learning Without Safety Constraint Violations During Training’, in AAMAS, p. 1226–1235, (2021). 
[43] Krishnan Srinivasan, Benjamin Eysenbach, Sehoon Ha, Jie Tan, and Chelsea Finn. Learning to be Safe: Deep RL with a Safety Critic, 2020. arXiv:2010.14603. 
[44] Yanan Sui, Alkis Gotovos, Joel Burdick, and Andreas Krause, ‘Safe Exploration for Optimization with Gaussian Processes’, in ICML, pp. 997–1005, (2015). 
[45] Richard S. Sutton and Andrew G. Barto, Reinforcement Learning: An Introduction, volume 2, MIT press, 2018. 
[46] Richard S. Sutton, A. Rupam Mahmood, and Martha White, ‘An Em-phatic Approach to the Problem of Off-policy Temporal-Difference Learning’, JMLR, 17(1), 2603–2631, (2016). 
[47] Oleg Svidchenko and Aleksei Shpilman. Maximum Entropy Model-based Reinforcement Learning, 2021. arXiv:2112.01195. 
[48] Matthew E. Taylor and Peter Stone, ‘Transfer Learning for Rein-forcement Learning Domains: A Survey’, JMLR, 10(56), 1633–1685, (2009). 
[49] Chen Tessler, Daniel J. Mankowitz, and Shie Mannor, ‘Reward Con-strained Policy Optimization’, in ICLR, (2019). 
[50] Brijen Thananjeyan, Ashwin Balakrishna, Suraj Nair, Michael Luo, Kr-ishnan Srinivasan, Minho Hwang, Joseph E Gonzalez, Julian Ibarz, Chelsea Finn, and Ken Goldberg, ‘Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones’, IEEE Robotics and Automa-tion Letters, 6(3), 4915–4922, (2021). 
[51] Matteo Turchetta, Andrey Kolobov, Shital Shah, Andreas Krause, and Alekh Agarwal, ‘Safe Reinforcement Learning via Curriculum Induc-tion’, in NeurIPS, pp. 12151–12162, (2020). 
[52] Giulia Vezzani, Abhishek Gupta, Lorenzo Natale, and Pieter Abbeel. Learning latent state representation for speeding up exploration, 2019. arXiv:1905.12621. 
[53] Zhaoming Xie, Patrick Clary, Jeremy Dao, Pedro Morais, Jonathan W. Hurst, and Michiel van de Panne, ‘Learning Locomotion Skills for Cassie: Iterative Design and Sim-to-Real’, in CoRL, pp. 317–329, (2019). 
[54] Qisong Yang, Thiago D. Simão, Simon H. Tindemans, and Matthijs T. J. Spaan, ‘WCSAC: Worst-Case Soft Actor Critic for Safety-Constrained Reinforcement Learning’, in AAAI, pp. 10639–10646, (2021). 
[55] Qisong Yang and Matthijs T. J. Spaan, ‘CEM: Constrained En-tropy Maximization for Task-Agnostic Safe Exploration’, in AAAI, pp. 10798–10806, (2023). 
[56] Tsung-Yen Yang, Justinian Rosca, Karthik Narasimhan, and Peter J. Ramadge, ‘Projection-Based Constrained Policy Optimization’, in ICLR, (2020). 
[57] Tsung-Yen Yang, Justinian Rosca, Karthik Narasimhan, and Peter J Ramadge, ‘Accelerating safe reinforcement learning with constraintmismatched baseline policies’, in ICML, pp. 11795–11807, (2021). 
[58] Tom Zahavy, Brendan O’Donoghue, André Barreto, Sebastian Flenner-hag, Volodymyr Mnih, and Satinder Singh. Discovering Diverse Nearly Optimal Policies with Successor Features, 2021. arXiv:2106.00669. 
[59] Moritz A. Zanger, Karam Daaboul, and J. Marius Zöllner, ‘Safe Con-tinuous Control with Constrained Model-Based Policy Optimization’, in IROS, pp. 3512–3519, (2021). 
[60] Jesse Zhang, Brian Cheung, Chelsea Finn, Sergey Levine, and Di-nesh Jayaraman, ‘Cautious Adaptation For Reinforcement Learning in Safety-Critical Settings’, in ICML, p. 11055–11065, (2020). 
[61] Zhuangdi Zhu, Kaixiang Lin, Anil K. Jain, and Jiayu Zhou, ‘Transfer learning in deep reinforcement learning: A survey’, IEEE Transactions on Pattern Analysis and Machine Intelligence, 1–20, (2023). 
[62] Brian D Ziebart, Modeling Purposeful Adaptive Behavior with the Prin-ciple of Maximum Causal Entropy, Ph.D. dissertation, Carnegie Mellon University, 2010.
A SAC-Lagrangian In this section, we present how we learn the parameters in SAC-λ. In SAC-λ, the constrained optimization problem is solved by Lagrangian methods [6], where an entropy weight α and a safety weight β (Lagrange-multipliers) are introduced to the constrained optimization: 
max π 
min α≥0 
min β≥0 
f(π)− αe(π)− βg(π), (8) 
where f(π) = Es0∼ι(·),a0∼π(·|s0) [Q r π(s0, a0)], e(π) = Est∼ρπ 
[ log(π(· | st)) +H 
] , and g(π) = Es0∼ι(·),a0∼π(·|s0) [Q 
c π(s0, a0)− d]. In 
(8), the max-min optimization problem can be solved by gradient ascent on π, and descent on α and β. Initially, SAC-λ was developed for local constraints, which means that the safety cost is constrained at each timestep [19]. However, it can 
be easily generalized to constrain the expected cost-return1. Using a similar formulation [22], we can get the actor loss: 
Jπ(θπ) = −E st∼D at∼π(·|st) 
[Qr π(st, at)− α log π(at | st)− βQc 
π(st, at)] , (9) 
where D is the replay buffer and θπ indicates the parameters of the policy π. The safety and reward critics (including a bonus for the policy entropy) are, respectively, trained to minimize 
JC(θC)=E(st,at)∼D 
[ 1 
2 
( Qc 
θC (st, at)− (ct+γQc θC (st+1, at+1)) 
)2] (10) 
and JR(θR) = E(st,at)∼D 
[1 2 (Qr 
θR(st, at)− (rt + γ(Qr θR(st+1, at+1)− α log(π(at+1 | st+1))))) 
2 ] , (11) 
where at+1 ∼ π(· | st+1), Qc and Qr are parameterized by θC and θR, respectively. 
Algorithm 2 Maximum exploration RL for safe guide Input:M⋄, α, d Initialize: D ← ∅, θ⋄χ for χ ∈ {π,R,C, β} Output: Optimized parameters θ⋄π for π⋄ 
1: for each iteration do 2: for each environment step do 3: at ∼ π⋄(· | st) 4: st+1 ∼ P(· | st, at) 5: rδt ← δ(f‡(st), f 
‡(st+1)) ▷ Auxiliary task (4) 6: c⋄t ← c⋄(st, at) 7: D ← D ∪ {(st, at, r 
δ t , c 
⋄ t , st+1)} ▷ Replay buffer 
8: end for 9: for each gradient step do 
10: Sample experience from replay buffer D 11: for χ ∈ {π,R,C, β} do 12: θ⋄χ ← θ⋄χ − ηχ∇̂θ⋄χJχ(θ 
⋄ χ) ▷ Parameter updating 
13: end for 14: end for 15: end for 
Finally, let θα and θβ be the parameters learned for the exploration and safety weight such that α = softplus(θα) and β = softplus(θβ), where 
softplus(x) = log(exp(x) + 1). 
We can learn α and β by minimizing the loss functions: 
Jα(θα) = E st∼D at∼π(·|st) 
[ −α(log(π(at | st)) +H) 
] , (12) 
and 
Jβ(θβ) = E st∼D at∼π(·|st) 
[β(d−Qc π(st, at))] . (13) 
So the corresponding weight will be adjusted if the constraints are violated, that is, if we estimate that the current policy is unsafe or if it does not have enough entropy. 
In this paper, we train the guide agent by solving the constraint optimization problem (2) based on the auxiliary reward rδ , defined by (4). Then, we can use SAC-λ directly employed to solve (2), as Algorithm 2 shows. 
1 A similar approach can be found at https://github.com/openai/safety-starter-agents.
B Relation between source and target tasks In this section, we describe the source task given a target task and the mapping from the target task to the source task. 
B.1 State Abstraction 
To build the source task based on a target task and a mapping Ξ from the target state space to the source state space, we assume Ξ is a state abstraction function [31]. 
LetM⊙ = ⟨S⊙,A⊙,P⊙, r⊙, c⊙, d⊙, ι⊙, γ⟩ be the target task,M⋄ = ⟨S⋄,A⋄,P⋄, ∅, c⋄, d⋄, ι⋄, γ⟩ be the source task, and Ξ : S⊙ → S⋄ 
the state abstraction function. We define Ξ−1 as the inverse of the abstraction function such that Ξ−1(s⊙) = {s⋄ ∈ S⋄|Ξ(s⋄) = s⊙}. We assume a weighting function w : S 7→ [0, 1], where ∑ 
s⊙∈Ξ−1(s⋄) 
w(s⊙) = 1,∀s⋄ ∈ S⋄. (14) 
Now we can define the transition and cost function of the target task: 
P⋄(s⋄ ′ | s⋄, a) = 
∑ s⊙∈Ξ−1(s⋄) 
∑ s⊙′∈Ξ−1(s⋄′ ) 
w(s⊙)P⊙(s⊙ ′ | s⊙, a) (15) 
c⋄(s⋄, a) = ∑ 
s⊙∈Ξ−1(s⋄) 
w(s⊙)c⊙(s⊙, a) (16) 
ι⋄(s⋄) = ∑ 
s⊙∈Ξ−1(s⋄) 
w(s⊙)ι⊙(s⊙). (17) 
B.2 Proof of Lemma 1 
In this section, we show that if Ξ is a Qc π-irrelevance state abstraction, then the expected cost of any source policy is the same in the source 
task and in the target task. For the convenience of the reader, we restate our assumption and lemma. 
Assumption 3. Ξ is a Qc π-irrelevance abstraction [31], therefore 
Ξ(s) = Ξ(s′)⇒ Qc π⊙(s, a) = Qc 
π⊙(s′, a), ∀s, s′ ∈ S⊙, a ∈ A, π⊙. 
Lemma 1. Given Assumption 1 and Assumption 3, we have 
Qc,⋄ π⋄ (Ξ(s), a) = Qc,⊙ 
π⋄→⊙(s, a) ∀s ∈ S⊙, a ∈ A, π⋄. 
That is, the expected cost of a source policy is the same in the source task and in the target task. Our proof follows an induction strategy inspired by previous work [1, Claim 1]. 
Proof. Let us consider a non-Markovian constrained decision process MT = ⟨ST ,A,PT , ∅, cT , d⋄, ιT , γ⟩ which is parameterized by an integer T . In this process, the agent takes T steps on the source task and then switches to the target task. Thus, 
ST = 
{ S⊙ if T = 0 
S⋄ otherwise. (18) 
cT (s, a) = 
{ c⊙(s, a) if T = 0 
c⋄(s, a) otherwise. (19) 
PT (s ′ | s, a) = 
 P⊙(s′ | s, a) if T = 0∑ 
s⊙∈Ξ−1(s) w(s⊙)P⊙(s′ | s⊙, a) if T = 1 
P⋄(s′ | s, a) otherwise. 
(20) 
ιT (s) = 
{ ι⊙(s) if T = 0 
ι⋄(s) otherwise. (21) 
The Qc,⊙ π (s, a)-value for taking action a ∈ A in state s ∈ ST and follow the policy π is: 
Qc T,π(s, a) = 
 Qc,⊙ 
π (s, a) if T = 0∑ s⊙∈Ξ−1(s) w(s⊙)Qc,⊙ 
π (s⊙, a) if T = 1 
c⋄(s, a) + γ ∑ 
s′∈S⋄ P⋄(s′ | s, a) ∑ 
a′∈A π(a′ | s′)Qc T−1,π(s 
′, a′) otherwise. 
(22) 
We proceed by induction on T to show that ∀T, s⊙, a, π : Qc,⊙ 
π (sT , a) = Qc,⊙ π (s⊙, a), 
where sT = s⊙ if T = 0 and sT = Ξ(s⊙) otherwise.
Base case: T = 0. As Qc 0 = Qc,⊙ this case follows trivially. 
Base case: T = 1. From the definition of Qc 1,π , we have: 
Qc 1,π(sT , a) = 
∑ s⊙′∈Ξ−1(sT ) 
w(s⊙ ′ )Qc,⊙ 
π (s⊙ ′ , a) (23) 
= ∑ 
s⊙′∈Ξ−1(sT ) 
w(s⊙ ′ )Qc,⊙ 
π (s⊙, a) (24) 
= Qc,⊙ π (s⊙, a) 
∑ s⊙′∈Ξ−1(s) 
w(s⊙ ′ ) (25) 
= Qc,⊙ π (s⊙, a). (26) 
In Equation (24), we replace every s⊙ ′ 
by the state s⊙ applying Assumption 3. As s⊙ is independent of s⊙ ′ , in Equation (25), we can move 
the Q-values out of the summation. Finally, in Equation (26), we can use Equation (14) to replace the summation by 1, which concludes this case. 
Incuctive case: T > 1. We assume as our inductive hypothesis that: 
∀s⊙, a, π : Qc T−1,π(sT , a) = Qc,⊙ 
π (s⊙, a). 
We start applying the definition of QT for T > 1: 
Qc T,π(sT , a) = c⋄(sT , a) + γ 
∑ s′∈S⋄ 
P⋄(s′ | sT , a) ∑ a′∈A 
π(a′ | s′)Qc T−1,π(s 
′, a′) (27) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙)c⊙(s⊙, a) + γ ∑ 
s′∈S⋄ 
∑ s⊙∈Ξ−1(sT ) 
∑ s⊙′∈Ξ−1(s′) 
w(s⊙)P⊙(s⊙ ′ | s⊙, a) 
∑ a′∈A 
π(a′ | s′)Qc T−1,π(s 
′, a′) (28) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙)c⊙(s⊙, a) + ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙)γ ∑ 
s′∈S⋄ 
∑ s⊙′∈Ξ−1(s′) 
P⊙(s⊙ ′ | s⊙, a) 
∑ a′∈A 
π(a′ | s′)Qc T−1,π(s 
′, a′) (29) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙) 
c⊙(s⊙, a) + γ ∑ 
s′∈S⋄ 
∑ s⊙′∈Ξ−1(s′) 
P⊙(s⊙ ′ | s⊙, a) 
∑ a′∈A 
π(a′ | s′)Qc T−1,π(s 
′, a′) 
 (30) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙) 
c⊙(s⊙, a) + γ ∑ 
s′∈S⋄ 
∑ s⊙′∈Ξ−1(s′) 
P⊙(s⊙ ′ | s⊙, a) 
∑ a′∈A 
π(a′ | s′)Qc,⊙ π (s⊙ 
′ , a′) 
 (31) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙) 
c⊙(s⊙, a) + γ ∑ 
s⊙′∈S⊙ 
P⊙(s⊙ ′ | s⊙, a) 
∑ a′∈A 
π(a′ | s′)Qc,⊙ π (s⊙ 
′ , a′) 
 (32) 
= ∑ 
s⊙∈Ξ−1(sT ) 
w(s⊙)Qc,⊙ π (s⊙, a) (33) 
= Qc,⊙ π (s⊙, a). (34) 
In this derivation, Equation (28) applies the definitions of c⋄ and P⋄, Equations (29) and (30) rearrange our terms, Equation (31) applies our inductive hypothesis, Equation (32) join the two summations as we are considering all possible states in S⊙, and Equation (33) we apply the Q-value definition. Finally, in Equation (34) we can choose any arbitrary state s⊙ ∈ Ξ−1(sT ), which concludes our proof. 
C Regularized Reward 
ωrKL+αrH =ω log π⋄(at | Ξ(st)) π⊙(at | st) 
+ ωrH 
=ω(log(π⋄(a|Ξ(s)))− log(π⊙(a|s))) + αrH 
=ω log(π⋄(a|Ξ(s))) + ω(− log(π⊙(a|s))) + αrH 
=ω log(π⋄(a|Ξ(s))) + ωrH + αrH 
=ωr⋄ + (ω + α)rH. 
(35)
Algorithm 3 Composite sampling (linear-decay) 
Input: π⋄, π⊙, υ Initialize: Pπ ← 1, Pwise ← 1 Output: πb 
1: for each iteration do 2: Pb(⋄) = Pπ ▷ The probability of using π⋄ 
3: Pb(⊙) = 1− Pπ ▷ The probability of using π⊙ 
4: Sample κwise ∼ U(0, 1) 5: if κwise < Pwise then 6: step-wise← true 7: else 8: step-wise← false 9: b ∼ Pb ▷ Choose behaviour policy 
10: end if 11: Pwise = Pwise − υ ▷ Decrease the probability of step-wise 12: for each environment step do 13: if step-wise then 14: b ∼ Pb ▷ Choose behaviour policy 15: end if 16: end for 17: Pπ = Pπ − υ ▷ Decrease the probability of using π⋄ 
18: end for 
D Two strategies in composite sampling Linear-decay (Algorithm 3). This strategy linearly decreases the probability of using π⋄ with a constant decay rate after each iteration 
of the algorithm, conversely increasing the probability of using π⊙. We have two modes with linear-decay: step-wise, where in each time step we may change πb; and trajectory-wise, where πb only changes at the start of a trajectory. The mode is decided before executing an episode and smoothly switches from the complete step-wise to the complete trajectory-wise over the training process. We linearly decrease the probability of executing the step-wise and use the guide with a constant decay rate after each iteration of the algorithm, conversely increasing the probability of executing the trajectory-wise and using the student policy. So, we initialize the probabilities Pπ = 1 to determine πb, and Pwise = 1 to determine the mode at the beginning (line 3). We linearly decrease them with a constant decay rate υ (lines 11 and 17), determined by the training length. At the beginning of each episode, we sample κwise ∼ U(0, 1), so if κwise < Pwise, we will execute step-wise, or we are in trajectory-wise (lines 4-10). Under step-wise, at each time step, we sample from the guide π⋄ with probability Pπ , and sample from the student π⊙ with probability 1 − Pπ (lines 13-14). Under trajectory-wise, we only make a decision once at the beginning of the trajectory (line 9). 
Control-switch (Algorithm 4). To balance between the safe exploration and the sample efficiency (the samples from the target policy are relatively more valuable), the student policy keeps sampling, i.e., πb = π⊙ at the start of a trajectory (line 2); after we meet the first ct−1 > 0, we have πb = π⋄ until the end of the trajectory (lines 12-14). Therefore, the guide policy serves as a rescue policy to improve safety during sampling. In addition, we leverage two replay buffers D⋄ and D⊙ to save the guide and student samples separately (lines 7-11), so as to control the probability PD⊙ to use the more on-policy samples in D⊙. Thus, we have the probability PD⋄ = 1− PD⊙ to sample from D⋄. In practice, we train the safe guide to achieve Qc 
π⋄(s, a) ≤ d, s ∼ D, a ∼ π⋄(· | s). From the definition of Qc π⋄(s, a), we can basically ensure 
Eτ∼ρπ⋄ 
[∑∞ t=0 γ 
tct ∣∣s0 = s, a0 = a 
] ≤ d even starting with c0 > 0. 
Main difference. The key distinction between linear-decay and control-switch approaches lies in the number of off-policy interactions from the student’s perspective. Linear-decay entails the collection of more samples from the guide during early episodes, whereas controlswitch enables the agent to collect more on-policy samples and only occasionally relies on off-policy samples from the guide following unsafe interactions. Additionally, linear-decay necessitates predefined schedules for the behaviour policy, while control-switch is adaptive. The pursuit of novel adaptive schedules presents a promising avenue for future research.
Algorithm 4 Composite sampling (control-switch) 
Input: π⋄, π⊙ 
Initialize: D⋄ ← ∅, D⊙ ← ∅ Output: πb 
1: for each iteration do 2: b← ⊙ ▷ Start sampling from the student 3: control-switch(t)← false 4: for each environment step do 5: at ∼ πb(· | st) 6: E ← (st, at, r 
⊙ t , r⋄t , ct, It, st+1) ▷ Generate experience 
7: if b = ⋄ then 8: D⋄ ← D⋄ ∪ {E} ▷ Save the guide samples 9: else 
10: D⊙ ← D⊙ ∪ {E} ▷ Save the student samples 11: end if 12: if ¬ control-switch(t) ∧ ct > 0 then 13: b← ⋄ ▷ Switch behaviour policy 14: control-switch(t)← true 15: end if 16: end for 17: end for 
E Ablation Study 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
0 
10 
20 
30 
40 
Co st 
-R et 
ur n π b 
FixReg DecReg MaxEnt StuSam GuiSam SaGui (control-switch) 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
0 
1 
2 
3 
Re tu 
rn  π 
b 
(a) Behaviour policy 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
0 
50 
100 
150 
Co st 
-R et 
ur n π 
⊙ 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
−6 
−4 
−2 
0 
2 
4 
Re tu 
rn  π 
⊙ 
(b) Target policy 
Figure 7. Ablation study in Static showing the safety and performance of the behaviour policy (a) and target policy (b). The black dashed line indicates the safety threshold.
F Evaluation of the target policy 
Comparison with baselines In Figure 6, we evaluate the behaviour policy πb for all algorithms: CPO, SAC-λ, CPO-PRE, SAC-λ-PRE, EGPO, and SAGUI. So, in Figure 8, we show how their resulted target policy will perform during training. In all these algorithms, SAGUI 
(control-switch) is the only one that can find a safe optimal target policy in all environments. However, SAGUI (linear-decay) cannot achieve similar performance, especially in Semi-dynamic and Dynamic. We infer that SAGUI (linear-decay) lack samples from the target policy, especially at the early stage of training. The behaviour policy of EGPO (with benefits from the targeted expert policy) has outstanding performance during training (Figure 6), but EGPO fails to find a safe target policy finally. As to the pre-training baselines, CPO-PRE and SAC-λ-PRE do not attain obvious improvement compared to CPO and SAC-λ that are trained from scratch. Instead, pre-training may have some negative impacts on getting a good target policy. The only exception is that CPO-PRE is largely improved in the relatively simple environment Static. 
0 
50 
100 
150 
 
 
 
 
0.25 0.50 0.75 1.00 1.25 TotalEnvInteracts 1e6 
−10.0 
−7.5 
−5.0 
−2.5 
0.0 
2.5 
 
 
 
CPO CPO-PRE SAC-λ SAC-λ-PRE EGPO SaGui (linear-decay) SaGui (control-switch) 
(a) Static 
0 
25 
50 
75 
100 
125 
0.5 1.0 1.5 2.0 2.5 TotalEnvInteracts 1e6 
−2 
0 
2 
(b) Semi-Dynamic 
20 
40 
60 
80 
1 2 3 4 TotalEnvInteracts 1e6 
0 
10 
20 
30 
(c) Dynamic 
Figure 8. Evaluation of π⊙ for CPO, CPO-PRE, SAC-λ, SAC-λ-PRE, EGPO, SAGUI (linear-decay), and SAGUI (control-switch) over ten seeds. The solid lines are the average of all runs, and the shaded area is the standard deviation. The black dashed lines indicate the safety thresholds. 
G Hyperparameters 
We list the hyperparameters used in SAGUI, which are summarized in Table 1. As to the baselines, we use the default hyperparameters in https://github.com/openai/safety-starter-agents. All runs in the experiment use separate feedforward Multilayer Perceptron (MLP) actor and critic networks. The size of the neural network (all actors and critics of the algorithms) depend on the complexity of the tasks. We use a replay buffer of size 106 for each off-policy algorithm to store the experience. The discount factor is set to be γ = 0.99, the target smoothing coefficient is set to be 0.005 to update the target networks, and the learning rate to 0.001. The clipping intervale hyper-parameters [Il, Iu] is set to [0.1, 2.0], while the sampling probabilities PD⋄ and PD⊙ are set to 0.25 and 0.75, respectively. The maximum episode length is 1000 steps in all experiments. We set the safety constraint d based on the problem. The rest of the hyperparameters are explained in the Empirical Analysis part of the paper. All experiments are performed on an Intel(R) Xeon(R) CPU@3.50GHz with 16 GB of RAM. 
Parameter Static Semi-Dynamic Dynamic Note 
Size of networks (32, 32) (64, 64) (256, 256) Size of replay buffer 106 106 106 |D| Batch size 32 64 256 Number of epochs 50 100 150 Safety constraint 5 8 25 d 
Table 1. Summary of hyperparameters in SAGUI. 
Safety-mapping function. The state spaces of the source and target task differ by the presence of the LiDAR observation of the target location. While the source task only has a safety-related signal xc, the target task has an additional goal-related signal xr . Thus, following the definition in Section 4.2, we can map the target state [xc, xr] to the source state ignoring the target-related signal: Ξ([xc, xr]) = [xc].
H Expert Guided Policy Optimization We also compare our algorithms to an Expert-in-the-loop RL method called Expert Guided Policy Optimization (EGPO) that incorporates a well-performing expert policy as a demonstrator as well as a safety guardian [36]. However, EGPO constrains safety behaviours at each timestep, which is different from our safety defined on long-term cost-return. In terms of the safe guide, EGPO assumes the access to the wellperforming expert policy, but our safe guide is task-agnostic. Thus, the expert in EGPO depends on the target task and does not undertake the task of exploration, while our safe guide can be useful for different reward functions and enhance the exploration capabilities of the student. Even though, EGPO can be easily adapted to our setting. The constraint of EGPO on the guardian intervention frequency can be directly transferred to be our safety constraint. Also, we do not minimize intervention anymore. Once the EGPO agent starts to take unsafe actions, the expert policy can take over the control until the end.