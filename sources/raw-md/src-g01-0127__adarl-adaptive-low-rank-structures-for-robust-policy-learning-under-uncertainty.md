> Source: https://arxiv.org/html/2510.11899v1

ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty
logo Back to arXiv  
logo Back to arXiv
This is experimental HTML to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more about this project and help improve conversions.
Why HTML? Report Issue Back to Abstract Download PDF 
Table of Contents
Abstract
1 Introduction
2 Preliminary and Related Works
2.1 Notation
2.2 Robust Reinforcement Learning
2.3 Reinforcement Learning with low rank structure
3 Bias-Variance Tradeoff in RL with Epistemic Uncertainty
4 Adaptive Rank Representation Reinforcement Learning
4.1 A Bi-level Optimization Formulation
4.2 Algorithm
5 Experiment
6 Conclusion
A Appendix
A.1 Proof of Theorem 1
A.2 Additional Result
A.2.1 Basic Settings
A.2.2 Model Uncertainty Setting
A.2.3 Rank Convergence of the Alternative Algorithm
A.2.4 Policy performance under varying dynamics
References
License: CC BY 4.0
arXiv:2510.11899v1 [cs.LG] 13 Oct 2025
ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty
Report issue for preceding element
Chenliang Li 1, Junyu Leng 1, Jiaxiang Li 2, Youbang Sun 3,
Shixiang Chen 4, Shahin Shahrampour 5, Alfredo Garcia 1 1
Texas A&M University 2 University of Minnesota 3 Tsinghua University 4
University of Science and Technology of China 5 Northeastern University
{chenliangli, levileng, alfredo.garcia}@tamu.edu
ybsun@mail.tsinghua.edu.cn jiaxiangli@umn.edu
shxchen@ustc.edu.cn s.shahrampour@northeastern.edu
Report issue for preceding element
Abstract
Report issue for preceding element
Robust reinforcement learning (Robust RL) seeks to handle epistemic uncertainty in environment dynamics, but existing approaches often rely on nested min–max optimization, which is computationally expensive and yields overly conservative policies. We propose Adaptive Rank Representation (AdaRL), a bi-level optimization framework that improves robustness by aligning policy complexity with the intrinsic dimension of the task. At the lower level, AdaRL performs policy optimization under fixed-rank constraints with dynamics sampled from a Wasserstein ball around a centroid model. At the upper level, it adaptively adjusts the rank to balance the bias–variance trade-off, projecting policy parameters onto a low-rank manifold. This design avoids solving adversarial worst-case dynamics while ensuring robustness without over-parameterization. Empirical results on MuJoCo continuous control benchmarks demonstrate that AdaRL not only consistently outperforms fixed-rank baselines (e.g., SAC) and state-of-the-art robust RL methods (e.g., RNAC, Parseval), but also converges toward the intrinsic rank of the underlying tasks. These results highlight that adaptive low-rank policy representations provide an efficient and principled alternative for robust RL under model uncertainty.
Report issue for preceding element
1 Introduction
Report issue for preceding element
The goal of a reinforcement learning (RL) agent is to learn a policy that maximizes its expected discounted cumulative reward (Sutton et al., 1998) . Recent advances have enabled RL agents to master complex games and robotic control tasks in both simulation and the real world (Mnih et al., 2015; Silver et al., 2017) . However, policies that perform well in such controlled settings often fail to transfer to practice, where transition dynamics are rarely fixed and may shift due to modeling inaccuracies (Lanzani, 2025) , external disturbances, or changing conditions (Pattanaik et al., 2017) . To address this gap, robust reinforcement learning (robust RL) (Zhou et al., 1996) formalizes uncertainty by considering a set of possible transition kernels and casting policy optimization as a minmax problem: the agent seeks a policy that maximizes expected return under the worst-case dynamics. This formulation reduces the sensitivity of RL to model misspecification and aims to produce policies that stay reliable when the environment differs from training.
Report issue for preceding element
Robust RL provide a principled framework to handle model uncertainty by optimizing for policies that perform well under the worst-case transition models within a prescribed uncertainty set (Iyengar, 2005; Wiesemann et al., 2013) . Classical solutions extend Bellman's principle to robust settings (Satia & Lave Jr, 1973) , while more recent work has focused on robust policy learning via model-based planning (Clavier et al., 2023) or online interaction with a nominal environment (Wang & Zou, 2021) . Despite these advances, robust RL faces severe scalability issues when applied to continuous and high-dimensional domains. In particular, updating the robust value function via the robust Bellman operator requires solving a nested inner-loop optimization at every step, i.e., identifying the worst-case transition, which becomes computationally prohibitive as the state and action spaces grow or when the uncertainty set is large or unbounded (Wang & Zou, 2022) . Moreover, existing approaches often assume access to oracle solvers or rely on fixed uncertainty sets that may yield overly conservative policies (Mannor et al., 2012, 2016; Xu & Mannor, 2012) . Beyond these computational bottlenecks, another key challenge lies in function approximation. Existing analyzes are mostly restricted to the tabular setting, which cannot achieve parameterized neural network approximations to the optimal solution of the robust Bellman equation. Our approach, in contrast, explicitly accommodates parameterization, thereby enabling robust generalization in high-dimensional environments.
Report issue for preceding element
In this work, we introduce an alternative perspective to overcome the limitations of existing robust RL approaches. Instead of directly tackling worst-case dynamics through nested min–max optimization, we enhance robustness by controlling over-parameterization and improving the generalization of fixed-rank policy and value models under perturbed transition dynamics. A key insight (Li et al., 2018) ) is that the effective complexity of a policy should match the intrinsic dimension of the task under epistemic uncertainty—uncertainty in environment dynamics arising from limited data or partial observability, which is prevalent in real-world domains such as robotics, control, environmental policy, and economics (Nagami & Schwager, 2023; Zhou et al., 1996; Lemoine & Traeger, 2014; Hansen & Sargent, 2008) . Building on this idea, we propose a new algorithm that jointly learns both the policy models and its rank, formulated as a bi-level optimization problem: the lower-level learns a policy under low-rank constraints, while the upper-level adapts the rank to balance robustness and expressiveness.
Report issue for preceding element 
Figure 1: Comparison of robust RL and the proposed AdaRL framework. Robust RL relies on repeatedly solving a nested min–max problem, while AdaRL formulates training as a bi-level optimization that alternates between policy optimization and adaptive rank adjustment to balance the bias–variance trade-off under epistemic uncertainty. Report issue for preceding element
This perspective aligns with and extends prior work on exploiting low-rank structures in reinforcement learning. In the model-based setting, algorithms for joint feature and policy learning have been developed when the dynamics admit a low-rank decomposition (Agarwal et al., 2020; Bose et al., 2024) . In the model-free setting, Jiang et al. ( 2017) introduced the concept of Bellman rank to capture the intrinsic complexity of value function approximation, and subsequent work (Modi et al., 2021, 2024; Yang et al., 2020) sought to encourage small Bellman rank during training. More recently, Tiwari et al. ( 2025) showed that wide two-layer neural networks yield reachable states concentrated on a low-dimensional manifold whose dimension scales with the action space. Overall, these works show that low-rank structures can improve performance in standard RL settings. Yet, no existing approach provides a practical algorithm for leveraging low-rank advantages under model uncertainty, and it remains inherently difficult to determine a suitable rank for parameterizing policy models in uncertain environments.
Report issue for preceding element
Our Contribution. We propose Adaptive Rank Representation for Reinforcement Learning (AdaRL, Figure 1), an adaptive framework that integrates conservatism into the learning process in MDPs with epistemic uncertainty. The algorithm alternates between standard policy optimization under a fixed rank and an adaptive step that adjusts the rank to balance robustness and expressiveness. Our main contributions are:
Report issue for preceding element
We provide a theoretical analysis of the bias–variance trade-off in entropy-regularized RL with linear parameterization under epistemic uncertainty, showing that low-rank representations can reduce variance in the presence of model uncertainty (Section 3, Theorem. 1). Report issue for preceding element
We formulate policy rank selection as a bi-level optimization problem and present the AdaRL algorithm, which adaptively adjusts policy rank for robust learning (Section 4). Report issue for preceding element
We empirically evaluate AdaRL on standard MuJoCo continuous control benchmarks, demonstrating consistent improvements over robust baselines (e.g., RNAC Zhou et al. ( 2023) , Parseval Chung et al. ( 2024) ) and non-robust methods such as SAC (Haarnoja et al., 2018) and Tiwari et al. ( 2025) (see Section 5). Report issue for preceding element
2 Preliminary and Related Works
Report issue for preceding element
2.1 Notation
Report issue for preceding element
Markov Decision Process. A Markov decision process (MDP) is represented by the tuple ( 𝒮 , 𝒜 , 𝒫 , ρ , r , γ ) (\mathcal{S},\mathcal{A},\mathcal{P},\rho,r,\gamma) wherein 𝒮 \mathcal{S} is the state space 𝒜 \mathcal{A} is the action space (with both 𝒮 ⊂ ℝ n , 𝒜 ⊂ ℝ m \mathcal{S}\subset\mathbb{R}^{n},\mathcal{A}\subset\mathbb{R}^{m} assumed compact), P s , a ∈ Δ 𝒮 P_{s,a}\in\Delta_{\mathcal{S}} , is the transition kernel for a ∈ 𝒜 , s ∈ 𝒮 a\in\mathcal{A},s\in\mathcal{S} . (where Δ 𝒮 \Delta_{\mathcal{S}} denotes the space of probability measures with support 𝒮 \mathcal{S} ), ρ  ( ⋅ ) \rho(\cdot) is the initial state distribution, R : 𝒮 × 𝒜 → ℝ R:\mathcal{S}\times\mathcal{A}\to\mathbb{R} is the the reward function γ ∈ [ 0 , 1 ) \gamma\in[0,1) is the discount factor. Given s ∈ 𝒮 s\in\mathcal{S} , a policy π \pi is a map π ( ⋅ | s ) : 𝒮 → Δ 𝒜 \pi(\cdot|s):\mathcal{S}\to\Delta_{\mathcal{A}} , where Δ 𝒜 \Delta_{\mathcal{A}} denotes the space of probability measures with support 𝒜 \mathcal{A} .
Report issue for preceding element
Epistemic Uncertainty in State Dynamics. To model uncertainty in the environment dynamics, we introduce an ambiguity set of possible transition kernels:
Report issue for preceding element
𝒫 s , a := { P s , a ∈ Δ 𝒮 ∣ W  ( P ^ s , a ∘ , P s , a ) ≤ ϵ } , \mathcal{P}{s,a}:={P{s,a}\in\Delta_{\mathcal{S}};\mid;W(\hat{P}^{\circ}{s,a},P{s,a})\leq\epsilon},
where P ^ s , a ∘ \hat{P}^{\circ}{s,a} is a reference transition kernel (e.g., a maximum likelihood estimator obtained from a finite demonstration dataset), W  ( P ^ s , a ∘ , P s , a ) W(\hat{P}^{\circ}{s,a},P_{s,a}) denotes the Wasserstein distance (Villani et al., 2008) , and ϵ > 0 \epsilon>0 is the uncertainty radius. We refer to P s , a ∘ P^{\circ}{s,a} as the centroid of the uncertainty set, representing the true but unobserved transition kernel that governs the system dynamics. Throughout, we assume that epistemic uncertainty is well captured by the Wasserstein ball (Mohajerin Esfahani & Kuhn, 2018) , i.e., P s , a ∘ ∈ 𝒫 s , a P^{\circ}{s,a}\in\mathcal{P}_{s,a} for all ( s , a ) ∈ 𝒮 × 𝒜 (s,a)\in\mathcal{S}\times\mathcal{A} .
Report issue for preceding element
Singular Value Decomposition (SVD) Let θ ∈ ℝ d 1 × d 2 \theta\in\mathbb{R}^{d_{1}\times d_{2}} . A thin singular value decomposition (SVD) is given by θ = 𝐔  𝚺  𝐕 ⊤ \theta=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\top} , where 𝐔 \mathbf{U} is a d 1 × r d_{1}\times r matrix with orthogonal columns, that is, an element of the Stiefel manifold (Chakraborty & Vemuri, 2019; Atiyah & Todd, 1960)
Report issue for preceding element
St  ( r , d 1 ) = { 𝐔 ∈ ℝ d 1 × r : 𝐔 T  𝐔 = 𝐈 } , \mathrm{St}(r,d_{1})={\mathbf{U}\in\mathbb{R}^{d_{1}\times r}:\mathbf{U}^{T}\mathbf{U}=\mathbf{I}},
𝚺 \boldsymbol{\Sigma} is a r × r r\times r diagonal matrix with positive entries σ 1 ≥ σ 2 ≥ ⋯  σ r > 0 \sigma_{1}\geq\sigma_{2}\geq\cdots\sigma_{r}>0 (referred to as singular values) and 𝐕 ∈ St  ( r , d 2 ) \mathbf{V}\in\mathrm{St}(r,d_{2}) . The singular value decomposition exists for any matrix θ ∈ ℝ d 1 × d 2 \theta\in\mathbb{R}^{d_{1}\times d_{2}} . We refer to a truncated SVD whenever r < rank  ( θ ) r<\mbox{rank}(\theta) .
Report issue for preceding element
2.2 Robust Reinforcement Learning
Report issue for preceding element
In MDPs, the system dynamics P P is usually assumed to be constant over time. However, in the real world, it is subject to perturbations that can significantly impact performance in deployment (Zhang et al., 2023; Moos et al., 2022) . Robust MDPs provide a theoretical framework for taking this uncertainty into account, taking P P as not fixed but chosen adversarially from an uncertainty set 𝒫 \mathcal{P} (Iyengar, 2005; Nilim & El Ghaoui, 2005) . where 𝒫 \mathcal{P} denotes a set of plausible transition models known as the uncertainty set. The objective of robust RL is to find a policy that performs well under the worst-case dynamics within this set. Formally, the robust objective 𝒥 𝒫 , π \mathcal{J}_{\mathcal{P},\pi} is defined as:
Report issue for preceding element
𝒥 robust  ( π ) = max π  min P ∈ 𝒫  𝔼 P , π  [ ∑ t ≥ 0 γ t  R  ( s t , a t ) | s 0 ∼ ρ 0 ] \mathcal{J}{\rm robust}(\pi)=\max{\pi}\min_{P\in\mathcal{P}}\mathbb{E}{P,\pi}\Big[\sum{t\geq 0}\gamma^{t}R(s_{t},a_{t}),\Big|s_{0}\sim\rho_{0}\Big]
(1)
The optimal policy π 𝒫 ∗ \pi_{\mathcal{P}}^{*} is defined as the solution to the outer-loop problem, which maximizes 𝒥 𝒫 , π \mathcal{J}_{\mathcal{P},\pi} by accounting for the worst-case transition model at each time step. This leads to the inner-loop problem of identifying the worst-case dynamics, for which several approaches have been developed, including value iteration (Nilim & El Ghaoui, 2005; Iyengar, 2005; Wiesemann et al., 2013; Grand-Clément & Kroer, 2021; Kumar et al., 2023a) , policy iteration (Kumar et al., 2022; Badrinath & Kalathil, 2021) , and policy gradient methods (Li et al., 2022; Wang & Zou, 2022; Wang et al., 2023; Kumar et al., 2023b) . However, the problem remains NP-hard for general uncertainty sets, and optimal policies may even be non-stationary (Wiesemann et al., 2013) . Most existing methods sidestep this difficulty by assuming that the inner-loop optimization can be solved efficiently—a reasonable assumption in tabular settings with small uncertainty sets, where one can exhaustively evaluate all transition kernels P ∈ 𝒫 P\in\mathcal{P} . Yet, when the uncertainty set is continuous, the inner-loop problem becomes substantially more challenging and computationally expensive. To address this challenge, Zhou et al. ( 2023); Gadot et al. ( 2024) propose the RNAC and EWoK algorithms, which rely on sampling-based techniques to estimate value functions under worst-case dynamics. Although theoretically sound, these methods require drawing multiple next states for each state-action pair, leading to high sample complexity and considerable computational overhead.
Report issue for preceding element
2.3 Reinforcement Learning with low rank structure
Report issue for preceding element
Another direction of research to address this uncertainty is to take advantage of low-rank structures in dynamics. In many stochastic control tasks, the transition dynamics admit a low-rank decomposition over a finite set of state-action features (Rozada et al., 2024, 2021; Yang et al., 2019) . For example, Tiwari et al. ( 2025) show that under suitable assumptions, the set of attainable states lies on a low-dimensional manifold. In fixed environments, the dimension of this manifold grows only linearly with the size of the action space and is independent of the state-space dimension. Building on this observation, they employ a ( 2  d a + 1 ) (2d_{a}+1) -dimensional low-rank manifold and apply sparse reinforcement learning methods to solve MuJoCo control tasks. More generally, low-rank structure can be imposed either on the transition kernel or directly on the optimal action-value function Q ∗ Q^{} , and empirical evidence suggests that Q ∗ Q^{} and near-optimal Q-functions in common stochastic control tasks indeed exhibit low-rank properties (Sam et al., 2023; Rozada et al., 2024, 2021; Yang et al., 2019) .
Report issue for preceding element
Motivated by these findings, algorithms for joint feature and policy learning in model-based RL have been developed (Agarwal et al., 2020; Bose et al., 2024) , though they typically assume the rank is known a priori. For model-free RL, Jiang et al. ( 2017) introduced the notion of Bellman rank to quantify the intrinsic complexity of value function approximation. More recent approaches exploit low-rank factorizations or representations to implicitly encourage small Bellman rank while optimizing the policy or value function (Modi et al., 2021, 2024; Yang et al., 2020) . However, the theoretical guarantees in these works generally rely on fixed dynamics, and to date there is no algorithm that simultaneously recovers the exact Bellman rank while learning the optimal policy under uncertain or time-varying environments.
Report issue for preceding element
3 Bias-Variance Tradeoff in RL with Epistemic Uncertainty
Report issue for preceding element
As highlighted in the related work section, many control tasks naturally admit low-rank structures in their transition dynamics, which has motivated a line of methods leveraging fixed-rank representations. However, when moving to the robust MDP setting, the presence of epistemic uncertainty fundamentally changes the picture. On the one hand, adopting an excessively low rank may fail to capture the variability introduced by uncertain dynamics, leading to biased estimates and brittle policies. On the other hand, employing a large rank increases model expressiveness but also amplifies variance, making the policy highly sensitive to perturbations and prone to over-parameterization. This tension suggests that selecting an appropriate rank is crucial: the rank must be sufficiently rich to encode uncertainty, yet controlled enough to mitigate overfitting. In this section, we formally analyze this bias–variance tradeoff in reinforcement learning under epistemic uncertainty, beginning with the model-free setting of entropy-regularized reinforcement learning (Haarnoja et al., 2018) . The objective function of entropy-regularized reinforcement learning is given by:
Report issue for preceding element
J ( π ) = 𝔼 π [ ∑ t = 0 ∞ γ t ( R ( s t , a t ) + ℋ ( π ( ⋅ | s t ) ) ) ] , J(\pi)=\mathbb{E}{\pi}\Bigg[\sum{t=0}^{\infty}\gamma^{t}\Big(R(s_{t},a_{t})+,\mathcal{H}(\pi(\cdot|s_{t}))\Big)\Bigg],
(2)
For any given policy π \pi , we define the corresponding (entropy regularized) Q π Q^{\pi} function and V π V^{\pi} function as follows:
Report issue for preceding element
V π  ( s ) \displaystyle V^{\pi}(s)
= 𝔼 a t ∼ π ( ⋅ | s t ) , s t + 1 ∼ 𝒫 s t , a t [ ∑ t ≥ 0 γ t ( R ( s t , a t ) + ℋ ( π ( ⋅ | s t ) ) | s 0 = s ] \displaystyle=\mathbb{E}{a{t}\sim\pi(\cdot|s_{t}),s_{t+1}\sim\mathcal{P}{s{t},a_{t}}}\Big[\sum_{t\geq 0}\gamma^{t}\Big(R(s_{t},a_{t})+\mathcal{H}(\pi(\cdot|s_{t})\Big)\Big|s_{0}=s\Big]
(3)
Q π  ( s , a ) \displaystyle Q^{\pi}(s,a)
= 𝔼 a t ∼ π ( ⋅ | s t ) , s t + 1 ∼ 𝒫 s t , a t [ ∑ t ≥ 0 γ t ( R ( s t , a t ) + ℋ ( π ( ⋅ | s t ) ) | s 0 = s , a 0 = a ] \displaystyle=\mathbb{E}{a{t}\sim\pi(\cdot|s_{t}),s_{t+1}\sim\mathcal{P}{s{t},a_{t}}}\Big[\sum_{t\geq 0}\gamma^{t}\Big(R(s_{t},a_{t})+\mathcal{H}(\pi(\cdot|s_{t})\Big)\Big|s_{0}=s,a_{0}=a\Big]
(4)
where we write s t + 1 ∼ 𝒫 s t , a t s_{t+1}\sim\mathcal{P}{s{t},a_{t}} to indicate that a transition kernel P s t , a t P_{s_{t},a_{t}} is uniformly randomly sampled from the uncertainty set 𝒫 s t , a t \mathcal{P}{s{t},a_{t}} and s t + 1 ∼ P s t , a t s_{t+1}\sim P_{s_{t},a_{t}} and the entropy term is defined as ℋ ( π ( ⋅ | s t ) ) := − ∑ a ∈ 𝒜 π ( a | s t ) log π ( a | s t ) . \mathcal{H}(\pi(\cdot|s_{t})):=-\sum_{a\in\mathcal{A}}\pi(a|s_{t})\log\pi(a|s_{t}). Let π ∗ \pi^{*} denote the optimal policy. We begin by re-stating a well known characterization of the solution to the entropy regularized MDP. According to Haarnoja et al. ( 2018) , the optimal policy takes the following form:
Report issue for preceding element
π ∗  ( a | s ) = exp  ( Q ∗  ( s , a ) − V ∗  ( s ) ) \pi^{}(a|s)=\exp{\big(Q^{}(s,a)-V^{*}(s)\big)}
(5)
where Q ∗ Q^{*} is the unique fixed point of the soft Bellman operator
Report issue for preceding element
ℬ  Q  ( s , a ) \displaystyle\mathcal{B}Q(s,a)
:= R  ( s , a ) + γ  𝔼 s ′ ∼ 𝒫 s , a  [ log  ∑ a ′ ∈ 𝒜 exp  Q  ( s ′ , a ′ ) ] \displaystyle:=R(s,a)+\gamma\mathbb{E}{s^{\prime}\sim\mathcal{P}{s,a}}\Big[\log\sum_{a^{\prime}\in\mathcal{A}}\exp{Q(s^{\prime},a^{\prime})}\Big]
(6)
and V ∗  ( s ′ ) := log  ∑ a ′ ∈ 𝒜 exp  Q  ( s ′ , a ′ ) V^{*}(s^{\prime}):=\log\sum_{a^{\prime}\in\mathcal{A}}\exp{Q(s^{\prime},a^{\prime})} . We consider linear function approximations for Q  ( s , a ) Q(s,a) and V  ( s ) V(s) functions for the simplicity of analysis, i.e.:
Report issue for preceding element
Q θ  ( s , a ) = ϕ  ( s , a ) ⊤  θ and V ω  ( s ) = ψ  ( s ) ⊤  ω Q_{\theta}(s,a)=\phi(s,a)^{\top}\theta\quad\text{and}\quad V_{\omega}(s)=\psi(s)^{\top}\omega
where ϕ  ( s , a ) \phi(s,a) and ψ  ( s ) \psi(s) are feature mappings.
Report issue for preceding element
Assumption 1
Report issue for preceding element
We assume the training data in the form of triplets ( s , a , s ′ ) (s,a,s^{\prime}) is generated as follows: a ∼ π b ( ⋅ ∣ s ) > 0 a\sim\pi_{b}(\cdot\mid s)>0 where π b \pi_{b} is a behavioral policy and s ′ ∼ 𝒫 s , a s^{\prime}\sim\mathcal{P}{s,a} . We assume the induced Markov chain is ergodic and the steady-state distribution of triplets ( s , a , s ′ ) (s,a,s^{\prime}) is denoted by 𝒫 \mathcal{P} . Similarly, we denote by 𝒫 ∘ \mathcal{P}^{\circ} the steady-state distribution of ( s , a , s ′ ) (s,a,s^{\prime}) when a ∼ π b ( ⋅ ∣ s ) , s ′ ∼ P s , a ∘ a\sim\pi{b}(\cdot\mid s),s^{\prime}\sim P^{\circ}_{s,a} .
Report issue for preceding element
Assumption 2
Report issue for preceding element
(Discrete Picard Condition) The linear system A 𝒫 ∘  θ = b 𝒫 ∘ , ω ∘ A_{\mathcal{P}^{\circ}}\theta=b_{\mathcal{P}^{\circ},\omega^{\circ}} with r ∘ := rank  ( A 𝒫 ∘ ) {r^{\circ}}:=\operatorname{rank}(A_{\mathcal{P}^{\circ}}) satisfies the discrete Picard condition, i.e. the SVD A 𝒫 ∘ = U ∘  Σ 𝒫 ∘  V ∘ ⊤ A_{\mathcal{P}^{\circ}}=U^{\circ}\Sigma_{\mathcal{P}^{\circ}}{V^{\circ}}^{\top} is such that there exists p > 1 p>1 with:
Report issue for preceding element
| u i ∘ ⊤  b 𝒫 ∘ , ω ∘ | ≤ σ 𝒫 ∘ , i p for  i = 1 , … , r ∘ , |{u^{\circ}{i}}^{\top}b{\mathcal{P}^{\circ},\omega^{\circ}}|\leq\sigma_{\mathcal{P}^{\circ},i}^{p}\quad\text{for }i=1,\ldots,{r^{\circ}},
| u ∘ i ⊤  b 𝒫 ∘ , ω ∘ | ≤ σ 𝒫 ∘ , r ∘ p for  i = r ∘ + 1 , … , d . |{u^{\circ}}{i}^{\top}b{\mathcal{P}^{\circ},\omega^{\circ}}|\leq\sigma_{\mathcal{P}^{\circ},{r^{\circ}}}^{p}\quad\text{for }i={r^{\circ}}+1,\ldots,d.
The discrete Picard condition (Hansen, 1990; Levin & Meltzer, 2017) states that the magnitude of the inner product | u ∘ i ⊤  b 𝒫 ∘ , ω ∘ | |{u^{\circ}}{i}^{\top}b{\mathcal{P}^{\circ},\omega^{\circ}}| shrinks faster that σ i p \sigma_{i}^{p} , accounting for the ill-condition in the system dynamics. Here p > 1 p>1 describes the shrinking speed.
Report issue for preceding element
Assumption 3
Report issue for preceding element
(2.1) ‖ ϕ  ( s , a ) ‖ ≤ 1 , \left|\phi(s,a)\right|\leq 1, ∀ ( s , a ) ∈ 𝒮 × 𝒜 \forall(s,a)\in\mathcal{S}\times\mathcal{A} .
(2.2) The feature covariance matrices with respect to ground truth dynamics are non-singular:
Report issue for preceding element
𝔼 𝒫 ∘  [ ϕ  ( s , a )  ϕ  ( s , a ) ⊤ ] ≻ 0 \mathbb{E}_{\mathcal{P}^{\circ}}[\phi(s,a)\phi(s,a)^{\top}]\succ 0
(2.3) (Lipschitz) ∀ ( s , a ) ∈ 𝒮 × 𝒜 \forall(s,a)\in\mathcal{S}\times\mathcal{A} , it holds that:
Report issue for preceding element
where L > 0 L>0 . These are standard assumptions in reinforcement learning with linear function approximation Tsitsiklis & Van Roy ( 1996); Munos ( 2003) .
Report issue for preceding element
Hence, in an off-policy setting, the optimal policy with linear function approximation can be described as the solution to the following optimization problem:
Report issue for preceding element
min ω \displaystyle\min_{\omega}~~
𝔼 𝒫  [ ‖ ψ  ( s ′ ) ⊤  ω − log  ∑ a ′ ∈ 𝒜 exp  ϕ  ( s ′ , a ′ ) ⊤  θ ∗  ( ω ) ‖ 2 ] \displaystyle~~\mathbb{E}{\mathcal{P}}\Big[|\psi(s^{\prime})^{\top}\omega-\log\sum{a^{\prime}\in\mathcal{A}}\exp{\phi(s^{\prime},a^{\prime})^{\top}\theta^{*}(\omega)}|^{2}\Big]
(8)
s.t
θ ∗  ( ω ) = arg  min θ  𝔼 𝒫  [ ‖ R  ( s , a ) + γ  ψ  ( s ′ ) ⊤  ω − ϕ  ( s , a ) ⊤  θ ‖ 2 ] \displaystyle~~\theta^{*}(\omega)=\arg\min_{\theta}\mathbb{E}_{\mathcal{P}}\Big[|R(s,a)+\gamma\psi(s^{\prime})^{\top}\omega-\phi(s,a)^{\top}\theta|^{2}\Big]
(9)
where 𝒫 \mathcal{P} refers to the steady-state distribution on ( s , a , s ′ ) (s,a,s^{\prime}) associated with uniformly sampling the transition kernel from the Wasserstein ball and selecting actions according to fixed behavioral policy. The first order (sufficient) conditions for lower level optimality can be written as:
Report issue for preceding element
− 𝔼 𝒫  [ ϕ  ( s , a )  ( R  ( s , a ) + γ  ψ  ( s ′ ) ⊤  ω − ϕ  ( s , a ) ⊤  θ ) ] \displaystyle-\mathbb{E}_{\mathcal{P}}\big[\phi(s,a)(R(s,a)+\gamma\psi(s^{\prime})^{\top}\omega-\phi(s,a)^{\top}\theta)\big]
= 0 \displaystyle=0
(10)
wherein we write 𝔼 𝒫 \mathbb{E}{\mathcal{P}} as shorthand for 𝔼 ( s , a , s ′ ) ∈ 𝒫 \mathbb{E}{(s,a,s^{\prime})\in\mathcal{P}} . This system of equations can be re-written as A 𝒫  θ = b 𝒫 , ω A_{\mathcal{P}}\theta=b_{\mathcal{P},\omega} where
Report issue for preceding element
A 𝒫 := 𝔼 𝒫  [ ϕ  ( s , a )  ϕ  ( s , a ) ⊤ ] b 𝒫 , ω := 𝔼 𝒫  [ ϕ  ( s , a )  ( R  ( s , a ) + γ  ψ  ( s ′ ) ⊤  ω ) ] \displaystyle A_{\mathcal{P}}:=\mathbb{E}{\mathcal{P}}[\phi(s,a)\phi(s,a)^{\top}]~~~~~b{\mathcal{P},\omega}:=\mathbb{E}_{\mathcal{P}}[\phi(s,a)\big(R(s,a)+\gamma\psi(s^{\prime})^{\top}\omega\big)]
Similarly for the ground-truth kernel 𝒫 ∘ \mathcal{P}^{\circ} we define the system:
Report issue for preceding element
A 𝒫 ∘ := 𝔼 𝒫 ∘  [ ϕ  ( s , a )  ϕ  ( s , a ) ⊤ ] b 𝒫 ∘ , ω := 𝔼 𝒫 ∘  [ ϕ  ( s , a )  ( R  ( s , a ) + γ  ψ  ( s ′ ) ⊤  ω ) ] \displaystyle A_{\mathcal{P}^{\circ}}:=\mathbb{E}{\mathcal{P}^{\circ}}[\phi(s,a)\phi(s,a)^{\top}]~~~~~b{\mathcal{P}^{\circ},\omega}:=\mathbb{E}_{\mathcal{P}^{\circ}}[\phi(s,a)\big(R(s,a)+\gamma\psi(s^{\prime})^{\top}\omega\big)]
where 𝒫 ∘ \mathcal{P}^{\circ} refers to the ground truth steady-state distribution.
Report issue for preceding element
Our analysis investigates the consequences of using high-rank parametrized policies when the underlying ground-truth environment dynamics are of lower rank. Let ( θ ∘ , ω ∘ ) (\theta^{\circ},\omega^{\circ}) denote the solution of the optimization problem defined by Eq. 8 and Eq. 9 when the expectations are taken with ground-truth dynamics. To formalize this setting, we characterize the low-rank structure of the environment dynamics under a set of regularity conditions. In particular, we assume bounded feature mappings, nonsingular covariance matrices, and a discrete Picard condition, which are standard in reinforcement learning with linear function approximation (see Appendix LABEL:app:sec_assumption for the full statements of Assumptions 2 and 3).
Report issue for preceding element
Building on these assumptions, we next examine the effect of approximating the system A 𝒫  θ = b 𝒫 A_{\mathcal{P}}\theta=b_{\mathcal{P}} using an r r -truncated SVD decomposition of A 𝒫 A_{\mathcal{P}} , denoted A 𝒫 , r A_{\mathcal{P},r} . This result highlights the fundamental bias–variance trade-off: choosing too small an r r induces approximation bias, whereas choosing too large an r r amplifies estimation variance.
Report issue for preceding element
Theorem 1
Report issue for preceding element
Bias-Variance Trade-off of Rank-r Approximation: Assume the ground-truth dynamics are given by 𝒫 ∘ \mathcal{P}^{\circ} and Assumptions 2 and 3 hold. Let ( θ ∘ , ω ∘ ) (\theta^{\circ},\omega^{\circ}) denote the solution of the optimization problem defined by Eq. 8, Eq. 9 when the expectations are taken with ground-truth dynamics (i.e. A 𝒫 ∘  θ = b 𝒫 ∘ , ω ∘ A_{\mathcal{P}^{\circ}}\theta=b_{\mathcal{P}^{\circ},\omega^{\circ}} ). Consider a truncated SVD A 𝒫 , r = U  Σ 𝒫 , r  V ⊤ A_{\mathcal{P},r}=U\Sigma_{{\mathcal{P},r}}V^{\top} for r ≤ rank  ( A 𝒫 ) r\leq\operatorname{rank}(A_{\mathcal{P}}) and θ r \theta_{r} be the solution A 𝒫 , r  θ = b 𝒫 , ω ∘ A_{\mathcal{P},r}\theta=b_{\mathcal{P},\omega^{\circ}} . It holds that:
Report issue for preceding element
‖ θ r − θ ∘ ‖ 2 ≤ 1 σ 𝒫 , r  ‖ b 𝒫 , ω ∘ − b 𝒫 ∘ , ω ∘ ‖ 2 ⏟ v  a  r  i  a  n  c  e + ( d − r )  σ 𝒫 ∘ , r p − 1 + ( d − r )  r ∘  σ 𝒫 ∘ , 1 p − 1 ⏟ b  i  a  s + 2  𝒪  ( L  ϵ ) \displaystyle|\theta_{r}-\theta^{\circ}|{2}\leq\underbrace{\frac{1}{\sigma{\mathcal{P},r}}|b_{\mathcal{P},\omega^{\circ}}-b_{\mathcal{P}^{\circ},\omega^{\circ}}|{2}}{variance}+\underbrace{(d-r)\sigma_{\mathcal{P}^{\circ},r}^{p-1}+(d-r){r^{\circ}}\sigma_{\mathcal{P}^{\circ},1}^{p-1}}_{bias}+2\mathcal{O}(L\epsilon)
(11)
where r ∘ := rank  ( A 𝒫 ∘ ) r^{\circ}:=\operatorname{rank}(A_{\mathcal{P}^{\circ}}) , and ϵ > 0 \epsilon>0 denotes the radius of the Wasserstein ball (Mohajerin Esfahani & Kuhn, 2018) .
Report issue for preceding element
Remark The upper bound of the performance gap between the estimated parameter θ r \theta_{r} and the optimal solution θ ∘ \theta^{\circ} in Theorem. 1 can be decomposed into two components related to variance and bias respectively. Thus for example, the choice of r > r ∘ r>r^{\circ} introduces higher variance since σ 𝒫 , r < σ 𝒫 , r ∘ \sigma_{\mathcal{P},r}<\sigma_{\mathcal{P},r^{\circ}} . Conversely, the choice of r < r ∘ r<r^{\circ} introduces higher bias since
Report issue for preceding element
( d − r )  σ 𝒫 ∘ , r p − 1 + ( d − r )  r ∘  σ 𝒫 ∘ , 1 p − 1 > ( d − r ∘ )  σ 𝒫 ∘ , r ∘ p − 1 + ( d − r ∘ )  r ∘  σ 𝒫 ∘ , 1 p − 1 (d-r)\sigma_{\mathcal{P}^{\circ},r}^{p-1}+(d-r){r^{\circ}}\sigma_{\mathcal{P}^{\circ},1}^{p-1}>(d-r^{\circ})\sigma_{\mathcal{P}^{\circ},r^{\circ}}^{p-1}+(d-r^{\circ}){r^{\circ}}\sigma_{\mathcal{P}^{\circ},1}^{p-1}
Discussion To confirm that bias-variance tradeoff also exists in settings with non-linear representation, we perform a sanity check on a MuJoCo control task (Todorov et al., 2012) . Specifically, we employ a three-layer neural network and adopt a rank-control mechanism similar to (Hu et al., 2022; Xu et al., 2019) (see details in Sec. 4.2). Our experiments reveal a clear bias–variance tradeoff in nonlinear control models, as illustrated in Figure 2: models with extremely low-rank representations exhibit high bias, while high-rank models suffer from large approximation errors due to transition samples drawn from uncertain dynamics.
Report issue for preceding element  
Figure 2: Performance of policy models under high model uncertainty in Walker2d-v3 ( Left) and Hopper-v3 ( Right). Results indicate that extremely low-rank representations lead to high bias, while overly high-rank models incur large approximation errors due to transition samples drawn from uncertain dynamics. Report issue for preceding element
4 Adaptive Rank Representation Reinforcement Learning
Report issue for preceding element
4.1 A Bi-level Optimization Formulation
Report issue for preceding element
The analysis in previous Section highlights that selecting the policy rank involves a delicate balance: too small a rank induces bias, while too large a rank amplifies variance. This trade-off suggests the need for an adaptive mechanism that can automatically adjust the rank during learning. Motivated by this insight, we introduce a bi-level (Colson et al., 2007) optimization formulation, where the lower-level problem identifies the optimal policy with uniformly sampled environment dynamics (from a Wasserstein ball around a centroid model) under a fixed rank, and the upper-level problem searches for the representation that optimizes a measure of fit to the lower-level model while regularizing by rank. To begin with, We consider a parameterized policy π θ \pi_{\theta} , where θ ∈ ℝ d 1 × d 2 \theta\in\mathbb{R}^{d_{1}\times d_{2}} with d 1 , d 2 > 0 d_{1},d_{2}>0 . And we respectively denote by
Report issue for preceding element
ℳ r := { θ ∈ ℝ d 1 × d 2 | rank  ( θ ) = r } \displaystyle\mathcal{M}{r}:={\theta\in\mathbb{R}^{d{1}\times d_{2}}~|~{\rm rank}(\theta)=r}
ℳ ≤ r ¯ := { θ ∈ ℝ d 1 × d 2 | rank  ( θ ) ≤ r ¯ } \displaystyle~~~\mathcal{M}{\leq\bar{r}}:={\theta\in\mathbb{R}^{d{1}\times d_{2}}~|~{\rm rank}(\theta)\leq\bar{r}}
the smooth manifold of matrices with rank r r . and the algebraic variety of matrices with rank less than or equal to r ¯ > 0 \bar{r}>0 .
Report issue for preceding element
Formulation: Towards developing an approach that simultaneously learns the policy and adaptively adjusts its rank, we introduce the following bi-level formulation:
Report issue for preceding element
min r \displaystyle\min_{r};
𝔼 ( s , a ) ∼ 𝒫 θ ∗ ∥ Proj ℳ r ( π θ ∗ ) ( a | s ) − π θ ∗ ( a | s ) ∥ 2 + λ r \displaystyle\mathbb{E}{(s,a)\sim\mathcal{P}{\theta^{}}}|{\rm Proj_{\mathcal{M}{r}}}(\pi{\theta^{}})(a|s)-\pi_{\theta^{*}}(a|s)|_{2}+\lambda r
(12)
s . t . \displaystyle{\rm s.t.}~~
θ ∗ := arg max θ ∈ ℳ r 𝔼 τ ∼ 𝒫 π θ [ ∑ t ≥ 0 γ t ( R ( s t , a t ) + ℋ ( π θ ( ⋅ | s t ) ) ) ] \displaystyle\theta^{*}:=\arg\max_{\theta\in\mathcal{M}{r}}\mathbb{E}{\tau\sim\mathcal{P}{\pi{\theta}}}\Big[\sum_{t\geq 0}\gamma^{t}\Big(R(s_{t},a_{t})+\mathcal{H}(\pi_{\theta}(\cdot|s_{t}))\Big)\Big]
(13)
where 𝒫 θ ∗ \mathcal{P}{{\theta^{*}}} denotes the steady-state distribution obtained by uniformly sampling the transition kernel from the Wasserstein ball and selecting actions according to the policy π θ ∗ \pi{\theta^{}} , the operator Proj ℳ r  ( π θ ∗ ) \textrm{Proj}{\mathcal{M}{r}}(\pi_{\theta^{}}) denotes the projection of the policy onto the low-rank manifold ℳ r \mathcal{M}_{r} , λ \lambda serves as a weight for rank regularization r r .
Report issue for preceding element
Discussion The bi-level formulation in Eq. 12–Eq. 13 plays two complementary roles. The lower-level problem Eq. 13 optimizes the policy parameters under a fixed rank constraint, aiming to maximize the entropy-regularized return and thus capture the best achievable policy representation at that rank. However, the optimal solution π θ ∗ \pi_{\theta^{}} of the lower-level problem may not align with the intrinsic task complexity and can overfit by exploiting the full representation power. To address this, the upper-level problem Eq. 12 explicitly searches for an appropriate rank that balances bias and variance, as motivated in the previous section. It seeks the best low-dimensional representation (bounded by r ¯ > 0 \bar{r}>0 ) of the state–action value associated with π θ ∗ \pi_{\theta^{}} , while controlling model capacity through the rank regularization term. In this way, the upper-level problem enforces a bias–variance tradeoff, ensuring that the learned representation achieves robustness without unnecessary over-parameterization.
Report issue for preceding element
4.2 Algorithm
Report issue for preceding element
We are now ready to design algorithms for the proposed formulation. Note that our formulation has a hierarchical structure and falls into the class of bi-level optimization problems Hong et al. ( 2023); Colson et al. ( 2007) . In general, bi-level problems are challenging to solve; in our case, the upper-level objective Eq. 12 depends explicitly on the optimal solution of the lower-level problem. Furthermore, the rank regularizer C  ( ⋅ ) C(\cdot) is non-differentiable, which precludes the use of (stochastic) first-order methods for the upper-level optimization. Fortunately, as we will show, a simple yet effective adaptive greedy search algorithm can be employed to obtain an empirical solution to the upper-level problem. At a high level, the proposed algorithm alternates between two steps: a Rank Adaptation Step, which updates the rank r r via a greedy search procedure, and a Policy Optimization Step, which optimizes the parameters under the rank constraint θ ∈ ℳ ≤ r \theta\in\mathcal{M}_{\leq r} . We now examine each step in detail.
Report issue for preceding element
Rank Adaptation Step From the discussion in Section 3, we know that extremely low-rank models are limited in their representation power and thus fail to capture sufficient information under model uncertainty. In contrast, high-rank models tend to overfit, resulting in poor generalization. Hence, it is crucial to carefully select an appropriate rank for policies in MDPs with uncertain dynamics. Although Theorem 1 provides useful insights, in practice it is difficult to explicitly solve this tradeoff and obtain the optimal rank. To address this, we adopt a greedy strategy: starting from a high-rank model, we gradually reduce the rank until reaching a stable value that yields consistent performance under model uncertainty. This procedure operationalizes the bias–variance tradeoff characterized in Theorem 1 and forms the core of the Rank Adaptation Step in our algorithm.
Report issue for preceding element
Specifically, the upper-level problem Eq. 12 requires us to identify suitable representations for both the policy and value models while keeping their ranks as low as possible. If no lower-rank model with sufficient approximation quality can be found, we simply retain the previous rank, i.e., r new = r old r_{\rm new}=r_{\rm old} . To do the greedy search, we consider using the following criterion to decide the new rank r ^ \hat{r} . Note there are many ways to decide the target rank; in the ablation study, we show that using this criterion achieves a smooth truncation and makes the rank converge to the intrinsic rank of the environment.
Report issue for preceding element
r ^ = max  { ℓ ∈ { 1 , 2 , … , d } : ∑ i = 1 ℓ σ i ∑ i = 1 d σ i ≤ β } \hat{r}=\max{\ell\in{1,2,\dots,d}:\frac{\sum_{i=1}^{\ell}\sigma_{i}}{\sum_{i=1}^{d}\sigma_{i}}\leq\beta}
(14)
To implement this efficiently, we adopt a low-rank factorization approach (Xu et al., 2019; Zhang et al., 2015) that operates directly on the weight matrices of neural networks. Since the rank of a neural network layer is inherently constrained by the number of hidden units, we follow the idea of inserting an intermediate linear layer between consecutive layers, thereby controlling the rank through the size of this hidden layer (see Figure 5 and Appendix A.2.1 for details). After obtaining the optimized policy π θ k \pi_{\theta}^{k} from several policy optimization steps, we refine this low-rank representation by performing SVD.
Report issue for preceding element
Policy Optimization Step One can adopt the standard approaches, such as the well-known soft actor critic (SAC) (Haarnoja et al., 2018) algorithm to obtain an approximate optimal policy that solves Eq. 13. Notice that after reconstructing the neural network, the rank of parameter θ \theta is no larger than r ^ \hat{r} due to the existence of the intermediate layer. In this way, the rank constraint is automatically enforced during optimization without requiring explicit SVD at every update.
Report issue for preceding element
We summarize the proposed algorithm in Algorithm 1, corresponding to the rank adaptation step and policy improvement step. We conclude this section with a brief remark on the advantages of AdaRL.
Report issue for preceding element
Low Computational Complexity Unlike previous methods (Gehring et al., 2015) that require repeated SVD with complexity 𝒪  ( d 3 ) \mathcal{O}(d^{3}) per update, AdaRL uses a single rank adaptation step to estimate a feasible rank. It operates on two timescales: the inner loop optimizes policies under a low-rank constraint, while the outer loop infrequently adjusts the rank by projecting parameters onto a lower-rank manifold. This design avoids costly worst-case value estimation and yields an efficient training procedure.
Report issue for preceding element
Convergence Control dynamical systems governed by Newtonian mechanics naturally exhibit a low-rank structure (Tiwari et al., 2025) . Although deriving theoretical convergence guarantees is nontrivial, our experiments empirically show that the solution of the upper-level problem converges to a stable rank, thereby balancing model robustness with representational capacity.
Report issue for preceding element
Input: Initialize parameters: for state-action value ω 0 \omega^{0} and policy θ 0 \theta^{0} . Truncation threshold β ∈ ( 0 , 1 ) \beta\in(0,1) , and truncate interval d t d_{t} .
for k = 0 , 1 , … , K − 1 k=0,1,\ldots,K-1 do
Data Sampling: Sample trajectories τ 1 , … , τ N \tau_{1},\dots,\tau_{N} from the current policy π θ k \pi_{\theta}^{k} ,and add them to the replay buffer: D ← D ∪ { τ 1 , … , τ N } D\leftarrow D\cup{\tau_{1},\dots,\tau_{N}}
Policy Evaluation: Compute Q ω k  ( ⋅ , ⋅ ) Q_{\omega}^{k}(\cdot,\cdot) with sampled data D D .
Policy Improvement: π θ k + 1 ( ⋅ | s ) ∝ exp ( Q ω k ( s , ⋅ ) ) , ∀ s ∈ 𝒮 \pi_{\theta}^{k+1}(\cdot|s)\propto\exp(Q_{\omega}^{k}(s,\cdot)),\forall s\in\mathcal{S} .
Rank Adaptation Step: if k %  d t = 0 k~%~d_{t}=0 , Search the suitable rank by Eq. 14 and project θ k \theta_{k} into a lower rank manifold ℳ r ^ \mathcal{M}_{\hat{r}} .
end for
Algorithm 1 Adaptive Rank Representation (AdaRL) Report issue for preceding element
5 Experiment
Report issue for preceding element
In this section, we present numerical evaluations of the proposed method AdaRL (Alg. 1) and compare it against several robust RL baselines, including RNAC, Parseval regularization, fixed-rank SAC, and the algorithm from Tiwari et al. ( 2025) . Our experiments highlight the advantages of AdaRL in two key aspects: (1) it achieves a favorable trade-off between the bias and variance induced by model uncertainty, thereby enabling more robust policy learning; and (2) it identifies a suitable low-rank manifold, within which constraining the policy model yields a representation that remains robust under model uncertainty. More details are given in the Appendix A.2.1.
Report issue for preceding element
We focus on robotic control tasks with continuous action spaces, using four widely adopted OpenAI Gym environments and their variants: Hopper-v3, Walker2d-v3, Ant-v3, and Humanoid-v3. Following the setup in Luo et al. ( 2024) , we introduce model uncertainty by modifying the source dynamics for each task. In Hopper and Walker2d, this involves structural changes such as adjusting torso and foot sizes, while in Ant and Humanoid we alter physical parameters including gravity or add external forces such as wind with a specified velocity. During training, the environment dynamics vary across episodes to simulate epistemic uncertainty.
Report issue for preceding element
The baselines considered in this scenario are: (1) SAC (Haarnoja et al., 2018) with a fixed-rank parameterization; (2) RNAC (Zhou et al., 2023) , which employs double sampling within newly defined uncertainty sets and uses function approximation to solve the robust Bellman equation; (3) Parseval regularization (Chung et al., 2024) , which enforces orthogonality in weight matrices to preserve optimization properties and improve training stability in continual reinforcement learning; and (4) the method of Tiwari et al. ( 2025) , which incorporates a fully connected sparsification MLP layer for reinforcement learning.
Report issue for preceding element
In Figure 3 and Table 1, we report numerical results comparing the proposed AdaRL algorithm with several baselines. As shown in Figure 3, both AdaRL and standard SAC achieve similar performance in the first iteration; however, once the model rank is adjusted, AdaRL consistently outperforms the standard methods by mitigating the impact of model uncertainty. It is worth noting that immediately after each rank adaptation step, the optimizer's momentum is reset and the model must adjust to the new parameterization, leading to a temporary performance drop before recovery. Further, in Table 1, the results show that AdaRL consistently outperforms the baselines by a significant margin in most scenarios. As discussed in Section 2.2, robust RL algorithms typically perform policy improvement based on worst-case value functions, which enhances robustness but often yields overly conservative policies and incurs high approximation errors in continuous control environments (Mannor et al., 2012, 2016; Xu & Mannor, 2012) . For regularization-based approaches, Parseval regularization can partially mitigate value-function overfitting, but it remains less effective than the low-rank constraint imposed in AdaRL. To fairly assess policy generalization, all evaluations are conducted under the fixed nominal dynamics 𝒫 ∘ \mathcal{P}^{\circ} , enabling us to examine whether the learned policies remain effective and robust in the presence of model uncertainty. In Appendix A.2.4, we further demonstrate the robustness of the trained policy in different perturbed dynamics.
Report issue for preceding element
Table 1: MuJoCo Results. The performance of the benchmark algorithms. Bolded numbers indicate the best results among AdaRL, RNAC, Parseval regularization, and the algorithm in Tiwari et al. ( 2025) for each task. Report issue for preceding element
In Figure 4, we report an additional experiment showing that the rank estimated by the AdaRL algorithm in Eq. 12 gradually converges to the intrinsic rank identified by Tiwari et al. ( 2025) , given an appropriate choice of β \beta in Alg. 1 (set to 0.98 0.98 in our experiments). This result demonstrates that AdaRL can effectively search for a suitable rank for environment with model uncertainty.
Report issue for preceding element  
Figure 3: Training performance on MuJoCo tasks. The proposed AdaRL consistently outperforms standard SAC baselines under model uncertainty. The red dashed vertical lines indicate the boundaries between different iteration intervals. Report issue for preceding element  
Figure 4: We plot the estimated rank from AdaRL throughout training. The intrinsic rank refers to the value identified by Tiwari et al. ( 2025) . Left: Walker2d. Right: Hopper. Report issue for preceding element
6 Conclusion
Report issue for preceding element
In this paper, we propose a novel framework for reinforcement learning under epistemic uncertainty by integrating the low-rank structure into policy representation. We begin by establishing a theoretical bias-variance trade-off that arises when applying low-rank approximations with uncertain dynamics. Motivated by this insight, we formulate a bi-level optimization problem and develop the Adaptive Low-Rank Representation algorithm, which dynamically adjusts the policy's representational rank to balance generalization and robustness. Our extensive experiments on MuJoCo benchmarks demonstrate that AdaRL consistently outperforms both fixed-rank RL methods and state-of-the-art robust RL algorithms.
Report issue for preceding element
References
Report issue for preceding element
Agarwal et al. (2020) ↑ Alekh Agarwal, Sham Kakade, Akshay Krishnamurthy, and Wen Sun. Flambe: Structural complexity and representation learning of low rank mdps. Advances in neural information processing systems, 33:20095–20107, 2020.
Atiyah & Todd (1960) ↑ MF Atiyah and JA Todd. On complex stiefel manifolds. In Mathematical Proceedings of the Cambridge Philosophical Society, volume 56, pp. 342–353. Cambridge University Press, 1960.
Badrinath & Kalathil (2021) ↑ Kishan Panaganti Badrinath and Dileep Kalathil. Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In International Conference on Machine Learning, pp. 511–520. PMLR, 2021.
Bose et al. (2024) ↑ Avinandan Bose, Simon Shaolei Du, and Maryam Fazel. Offline multi-task transfer rl with representational penalization, 2024. URL https://arxiv.org/abs/2402.12570.
Chakraborty & Vemuri (2019) ↑ Rudrasis Chakraborty and Baba C Vemuri. Statistics on the stiefel manifold: Theory and applications. 2019.
Chung et al. (2024) ↑ Wesley Chung, Lynn Cherif, Doina Precup, and David Meger. Parseval regularization for continual reinforcement learning. Advances in Neural Information Processing Systems, 37:127937–127967, 2024.
Clavier et al. (2023) ↑ Pierre Clavier, Erwan Le Pennec, and Matthieu Geist. Towards minimax optimality of model-based robust reinforcement learning. arXiv preprint arXiv:2302.05372, 2023.
Colson et al. (2007) ↑ Benoît Colson, Patrice Marcotte, and Gilles Savard. An overview of bilevel optimization. Annals of operations research, 153(1):235–256, 2007.
Falini (2022) ↑ Antonella Falini. A review on the selection criteria for the truncated svd in data science applications. Journal of Computational Mathematics and Data Science, 5:100064, 2022.
Gadot et al. (2024) ↑ Uri Gadot, Kaixin Wang, Navdeep Kumar, Kfir Yehuda Levy, and Shie Mannor. Bring your own (non-robust) algorithm to solve robust mdps by estimating the worst kernel. In Forty-first International Conference on Machine Learning, 2024.
Gehring et al. (2015) ↑ Clement Gehring, Yangchen Pan, and Martha White. Incremental truncated lstd. arXiv preprint arXiv:1511.08495, 2015.
Grand-Clément & Kroer (2021) ↑ Julien Grand-Clément and Christian Kroer. Scalable first-order methods for robust mdps. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, pp. 12086–12094, 2021.
Haarnoja et al. (2018) ↑ Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International conference on machine learning, pp. 1861–1870. Pmlr, 2018.
Hansen & Sargent (2008) ↑ Lars Peter Hansen and Thomas J. Sargent. Robustness. Princeton University Press, Princeton, NJ, 2008. ISBN 9780691132150.
Hansen (1990) ↑ Per Christian Hansen. The discrete picard condition for discrete ill-posed problems. BIT Numerical Mathematics, 30(4):658–672, 1990.
Hong et al. (2023) ↑ Mingyi Hong, Hoi-To Wai, Zhaoran Wang, and Zhuoran Yang. A two-timescale stochastic algorithm framework for bilevel optimization: Complexity analysis and application to actor-critic. SIAM Journal on Optimization, 33(1):147–180, 2023.
Hu et al. (2022) ↑ Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al. Lora: Low-rank adaptation of large language models. ICLR, 1(2):3, 2022.
Iyengar (2005) ↑ Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, 2005.
Jiang et al. (2017) ↑ Nan Jiang, Akshay Krishnamurthy, Alekh Agarwal, John Langford, and Robert E Schapire. Contextual decision processes with low bellman rank are pac-learnable. In Proceedings of the 34th International Conference on Machine Learning (ICML), volume 70 of Proceedings of Machine Learning Research, pp. 1704–1713. PMLR, 2017.
Kumar et al. (2022) ↑ Navdeep Kumar, Kfir Levy, Kaixin Wang, and Shie Mannor. Efficient policy iteration for robust markov decision processes via regularization. arXiv preprint arXiv:2205.14327, 2022.
Kumar et al. (2023a) ↑ Navdeep Kumar, Kfir Levy, Kaixin Wang, and Shie Mannor. An efficient solution to s-rectangular robust markov decision processes. arXiv preprint arXiv:2301.13642, 2023a.
Kumar et al. (2023b) ↑ Navdeep Kumar, Ilnura Usmanova, Kfir Yehuda Levy, and Shie Mannor. Towards faster global convergence of robust policy gradient methods. In Sixteenth European Workshop on Reinforcement Learning, 2023b.
Lanzani (2025) ↑ Giacomo Lanzani. Dynamic concern for misspecification. Econometrica, 93(4):1333–1370, 2025.
Lemoine & Traeger (2014) ↑ Derek Lemoine and Christian P. Traeger. Watch your step: Optimal policy in a tipping climate. American Economic Journal: Economic Policy, 6(1):137–166, 2014.
Levin & Meltzer (2017) ↑ Eitan Levin and Alexander Y Meltzer. Estimation of the regularization parameter in linear discrete ill-posed problems using the picard parameter. SIAM Journal on Scientific Computing, 39(6):A2741–A2762, 2017.
Li et al. (2018) ↑ Chunyuan Li, Heerad Farkhoor, Rosanne Liu, and Jason Yosinski. Measuring the intrinsic dimension of objective landscapes. arXiv preprint arXiv:1804.08838, 2018. Published: ICLR 2018 Workshop / International Conference on Learning Representations.
Li et al. (2022) ↑ Yan Li, Guanghui Lan, and Tuo Zhao. First-order policy optimization for robust markov decision process. arXiv preprint arXiv:2209.10579, 2022.
Lialin et al. (2023) ↑ Vladislav Lialin, Namrata Shivagunde, Sherin Muckatira, and Anna Rumshisky. Relora: High-rank training through low-rank updates. arXiv preprint arXiv:2307.05695, 2023.
Luo et al. (2024) ↑ Yu Luo, Tianying Ji, Fuchun Sun, Jianwei Zhang, Huazhe Xu, and Xianyuan Zhan. Ompo: A unified framework for rl under policy and dynamics shifts. arXiv preprint arXiv:2405.19080, 2024.
Mannor et al. (2012) ↑ Shie Mannor, Ofir Mebel, and Huan Xu. Lightning does not strike twice: Robust mdps with coupled uncertainty. In Proceedings of the 29th International Conference on Machine Learning (ICML), pp. 385–392, 2012. URL https://arxiv.org/abs/1206.4643.
Mannor et al. (2016) ↑ Shie Mannor, Ofir Mebel, and Huan Xu. Robust mdps with k-rectangular uncertainty. Mathematics of Operations Research, 41(4):1484–1509, 2016. doi: 10.1287/moor.2016.0786. URL https://pubsonline.informs.org/doi/10.1287/moor.2016.0786.
Mnih et al. (2015) ↑ Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland, Georg Ostrovski, et al. Human-level control through deep reinforcement learning. nature, 518(7540):529–533, 2015.
Modi et al. (2024) ↑ Aditya Modi, Jinglin Chen, Akshay Krishnamurthy, Nan Jiang, and Alekh Agarwal. Model-free representation learning and exploration in low-rank mdps. Journal of Machine Learning Research, 25(6):1–76, 2024.
Modi et al. (2021) ↑ Ishaan Modi, Adrien Bembom, John Schulman, Sergey Levine, and Pieter Abbeel. Model-based reinforcement learning via structural constraint on value functions. In Advances in Neural Information Processing Systems, 2021. URL https://arxiv.org/abs/2110.08708.
Mohajerin Esfahani & Kuhn (2018) ↑ Peyman Mohajerin Esfahani and Daniel Kuhn. Data-driven distributionally robust optimization using the wasserstein metric: Performance guarantees and tractable reformulations. Mathematical Programming, 171(1):115–166, 2018.
Moos et al. (2022) ↑ Janosch Moos, Kay Hansel, Hany Abdulsamad, Svenja Stark, Debora Clever, and Jan Peters. Robust reinforcement learning: A review of foundations and recent advances. Machine Learning and Knowledge Extraction, 4(1):276–315, 2022.
Munos (2003) ↑ Rémi Munos. Error bounds for approximate policy iteration. In Proceedings of the Twentieth International Conference on International Conference on Machine Learning, pp. 560–567, 2003.
Nagami & Schwager (2023) ↑ Keiko Nagami and Mac Schwager. Epistemic uncertainty in state estimation and belief space planning with learning-based perception systems. In First Workshop on Out-of-Distribution Generalization in Robotics at CoRL 2023, 2023. URL https://openreview.net/forum?id=CPZaavSwXg.
Nilim & El Ghaoui (2005) ↑ Arnab Nilim and Laurent El Ghaoui. Robust control of markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005.
Pattanaik et al. (2017) ↑ Anay Pattanaik, Zhenyi Tang, Shuijing Liu, Gautham Bommannan, and Girish Chowdhary. Robust deep reinforcement learning with adversarial attacks. arXiv preprint arXiv:1712.03632, 2017.
Rozada et al. (2021) ↑ Sergio Rozada, Victor Tenorio, and Antonio G Marques. Low-rank state-action value-function approximation. In 2021 29th European Signal Processing Conference (EUSIPCO), pp. 1471–1475. IEEE, 2021.
Rozada et al. (2024) ↑ Sergio Rozada, Santiago Paternain, and Antonio G Marques. Tensor and matrix low-rank value-function approximation in reinforcement learning. IEEE Transactions on Signal Processing, 2024.
Sam et al. (2023) ↑ Tyler Sam, Yudong Chen, and Christina Lee Yu. Overcoming the long horizon barrier for sample-efficient reinforcement learning with latent low-rank structure. Proceedings of the ACM on Measurement and Analysis of Computing Systems, 7(2):1–60, 2023.
Satia & Lave Jr (1973) ↑ Jay K Satia and Roy E Lave Jr. Markovian decision processes with uncertain transition probabilities. Operations Research, 21(3):728–740, 1973.
Silver et al. (2017) ↑ David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al. Mastering the game of go without human knowledge. nature, 550(7676):354–359, 2017.
Sutton et al. (1998) ↑ Richard S Sutton, Andrew G Barto, et al. Reinforcement learning: An introduction, volume 1. MIT press Cambridge, 1998.
Tiwari et al. (2025) ↑ Saket Tiwari, Omer Gottesman, and George Konidaris. Geometry of neural reinforcement learning in continuous state and action spaces. In The Second Conference on Parsimony and Learning (Recent Spotlight Track), 2025.
Todorov et al. (2012) ↑ Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, pp. 5026–5033. IEEE, 2012.
Touvron et al. (2023) ↑ Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.
Tsitsiklis & Van Roy (1996) ↑ John Tsitsiklis and Benjamin Van Roy. Analysis of temporal-diffference learning with function approximation. Advances in neural information processing systems, 9, 1996.
Villani et al. (2008) ↑ Cédric Villani et al. Optimal transport: old and new, volume 338. Springer, 2008.
Wang et al. (2023) ↑ Qiuhao Wang, Chin Pang Ho, and Marek Petrik. Policy gradient in robust mdps with global convergence guarantee. In International Conference on Machine Learning, pp. 35763–35797. PMLR, 2023.
Wang & Zou (2021) ↑ Yue Wang and Shaofeng Zou. Online robust reinforcement learning with model uncertainty. Advances in Neural Information Processing Systems, 34:7193–7206, 2021.
Wang & Zou (2022) ↑ Yue Wang and Shaofeng Zou. Policy gradient method for robust reinforcement learning. In International conference on machine learning, pp. 23484–23526. PMLR, 2022.
Wiesemann et al. (2013) ↑ Wolfram Wiesemann, Daniel Kuhn, and Berç Rustem. Robust markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013.
Xu & Mannor (2012) ↑ Huan Xu and Shie Mannor. Distributionally robust markov decision processes. Mathematics of Operations Research, 37(2):288–300, 2012. doi: 10.1287/moor.1120.0540. URL https://doi.org/10.1287/moor.1120.0540.
Xu et al. (2019) ↑ Yuhui Xu, Yuxi Li, Shuai Zhang, Wei Wen, Botao Wang, Wenrui Dai, Yingyong Qi, Yiran Chen, Weiyao Lin, and Hongkai Xiong. Trained rank pruning for efficient deep neural networks. In 2019 Fifth Workshop on Energy Efficient Machine Learning and Cognitive Computing-NeurIPS Edition (EMC2-NIPS), pp. 14–17. IEEE, 2019.
Yang et al. (2019) ↑ Yuzhe Yang, Guo Zhang, Zhi Xu, and Dina Katabi. Harnessing structures for value-based planning and reinforcement learning. arXiv preprint arXiv:1909.12255, 2019.
Yang et al. (2020) ↑ Zichuan Yang, George Tucker, Tom Zahavy, Mohammad Ghavamzadeh, and Ofir Nachum. Representation learning for reinforcement learning via bellman error minimization. In International Conference on Machine Learning (ICML), 2020. URL https://arxiv.org/abs/2001.07301.
Zhang et al. (2015) ↑ Xiangyu Zhang, Jianhua Zou, Kaiming He, and Jian Sun. Accelerating very deep convolutional networks for classification and detection. IEEE transactions on pattern analysis and machine intelligence, 38(10):1943–1955, 2015.
Zhang et al. (2023) ↑ Yuan Zhang, Jianhong Wang, and Joschka Boedecker. Robust reinforcement learning in continuous control tasks with uncertainty set regularization. In Conference on Robot Learning, pp. 1400–1424. PMLR, 2023.
Zhou et al. (1996) ↑ Kemin Zhou, John C. Doyle, and Keith Glover. Robust and Optimal Control. Prentice Hall, 1996.
Zhou et al. (2023) ↑ Ruida Zhou, Tao Liu, Min Cheng, Dileep Kalathil, PR Kumar, and Chao Tian. Natural actor-critic for robust reinforcement learning with function approximation. Advances in neural information processing systems, 36:97–133, 2023.
Appendix A Appendix
Report issue for preceding element
A.1 Proof of Theorem 1
Report issue for preceding element
For the ease of notation, we denote the gap between the sampled system dynamics with uncertainty A 𝒫 A_{\mathcal{P}} and the reference system A 𝒫 ∘ A_{\mathcal{P}^{\circ}} as ϵ A := A 𝒫 ∘ − A 𝒫 \epsilon_{A}:=A_{\mathcal{P}^{\circ}}-A_{\mathcal{P}} . Recall that A 𝒫 , r A_{\mathcal{P},r} denotes the low-rank manifold projection of A 𝒫 A_{\mathcal{P}} using truncated SVD. Let A 𝒫 ∘ † A_{\mathcal{P}^{\circ}}^{\dagger} and A 𝒫 , r † A_{\mathcal{P},r}^{\dagger} respectively denote the pseudo-inverses. With θ ∘ = A 𝒫 ∘ †  b 𝒫 ∘ \theta^{\circ}=A_{\mathcal{P}^{\circ}}^{\dagger}b_{\mathcal{P}^{\circ}} and θ r = A 𝒫 , r †  b 𝒫 \theta_{r}=A_{\mathcal{P},r}^{\dagger}b_{\mathcal{P}} , the difference can then be written as:
Report issue for preceding element
θ r − θ ∘ \displaystyle\theta_{r}-\theta^{\circ}
= A 𝒫 , r †  b 𝒫 − θ ∘ \displaystyle=A_{\mathcal{P},r}^{\dagger}b_{\mathcal{P}}-\theta^{\circ}
= A 𝒫 , r †  ( b 𝒫 − b 𝒫 ∘ ) + A 𝒫 , r †  A 𝒫 ∘  θ ∘ − θ ∘ \displaystyle=A_{\mathcal{P},r}^{\dagger}(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})+A_{\mathcal{P},r}^{\dagger}A_{\mathcal{P}^{\circ}}\theta^{\circ}-\theta^{\circ}
= A 𝒫 , r †  ( b 𝒫 − b 𝒫 ∘ ) + A 𝒫 , r †  A 𝒫  θ ∘ + A 𝒫 , r †  ϵ A  θ ∘ − θ ∘ \displaystyle=A_{\mathcal{P},r}^{\dagger}(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})+A_{\mathcal{P},r}^{\dagger}A_{\mathcal{P}}\theta^{\circ}+A_{\mathcal{P},r}^{\dagger}\epsilon_{A}\theta^{\circ}-\theta^{\circ}
= A 𝒫 , r †  ( b 𝒫 − b 𝒫 ∘ ) + ∑ i = 1 r v i  v i T  θ ∘ − ∑ i = 1 d v i  v i T  θ ∘ + A 𝒫 , r †  ϵ A  θ ∘ \displaystyle=A_{\mathcal{P},r}^{\dagger}(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})+\sum_{i=1}^{r}v_{i}v_{i}^{T}\theta^{\circ}-\sum_{i=1}^{d}v_{i}v_{i}^{T}\theta^{\circ}+A_{\mathcal{P},r}^{\dagger}\epsilon_{A}\theta^{\circ}
= A 𝒫 , r †  ( b 𝒫 − b 𝒫 ∘ ) − ∑ i = r + 1 d v i  v i T  θ ∘ + A 𝒫 , r †  ϵ A  θ ∘ \displaystyle=A_{\mathcal{P},r}^{\dagger}(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})-\sum_{i=r+1}^{d}v_{i}v_{i}^{T}\theta^{\circ}+A_{\mathcal{P},r}^{\dagger}\epsilon_{A}\theta^{\circ}
where the fourth equation above follows from the fact that:
Report issue for preceding element
A 𝒫 , r †  A 𝒫 = V  Σ 𝒫 , r − 1  U ⊤  U  Σ 𝒫  V ⊤ = ∑ i = 1 r v i  v i T and ∑ i = 1 d v i  v i T = I . A_{\mathcal{P},r}^{\dagger}A_{\mathcal{P}}=V\Sigma_{\mathcal{P},r}^{-1}U^{\top}U\Sigma_{\mathcal{P}}V^{\top}=\sum_{i=1}^{r}v_{i}v_{i}^{T}\quad\text{and}\quad\sum_{i=1}^{d}v_{i}v_{i}^{T}=I.
Since the feature functions ψ , ϕ \psi,\phi are Lipschitz with constant L > 0 L>0 , and that the uncertainty in environment dynamics are bounded from the underlying reference system with Wasserstein distance W  ( 𝒫 ^ s , a ∘ , P s , a ) ≤ ϵ W(\hat{\mathcal{P}}^{\circ}{s,a},P{s,a})\leq\epsilon , all the components of matrix A 𝒫 A_{\mathcal{P}} , say for example 𝔼 𝒫  [ ψ  ( s ′ )  ψ  ( s ′ ) ⊤ ] \mathbb{E}_{\mathcal{P}}[\psi(s^{\prime})\psi(s^{\prime})^{\top}] , can be upper bounded as follows,
Report issue for preceding element
sup 𝒫 ∈ ℬ W  ( 𝒫 ^ ∘ , ϵ ) ‖ 𝔼 𝒫  [ ψ  ( s ′ )  ψ  ( s ′ ) ⊤ ] − 𝔼 𝒫 ^ ∘  [ ψ  ( s ′ )  ψ  ( s ′ ) ⊤ ] ‖ = 𝒪  ( L  ϵ ) \sup_{\mathcal{P}\in\mathcal{B}{W}(\hat{\mathcal{P}}^{\circ},\epsilon)}\left|\mathbb{E}{\mathcal{P}}[\psi(s^{\prime})\psi(s^{\prime})^{\top}]-\mathbb{E}_{\hat{\mathcal{P}}^{\circ}}[\psi(s^{\prime})\psi(s^{\prime})^{\top}]\right|=\mathcal{O}(L\epsilon)
where ℬ W  ( 𝒫 ^ ∘ , ϵ ) \mathcal{B}{W}(\hat{\mathcal{P}}^{\circ},\epsilon) is the Wassertein ball with radius ϵ > 0 \epsilon>0 . By Assumption 0, 𝒫 ∘ ∈ ℬ W  ( 𝒫 ^ ∘ , ϵ ) \mathcal{P}^{\circ}\in\mathcal{B}{W}(\hat{\mathcal{P}}^{\circ},\epsilon) , hence by triangle inequality:
Report issue for preceding element
‖ 𝔼 𝒫  [ ψ  ( s ′ )  ψ  ( s ′ ) ⊤ ] − 𝔼 𝒫 ∘  [ ψ  ( s ′ )  ψ  ( s ′ ) ⊤ ] ‖ ≤ 2  𝒪  ( L  ϵ ) \left|\mathbb{E}{\mathcal{P}}[\psi(s^{\prime})\psi(s^{\prime})^{\top}]-\mathbb{E}{\mathcal{P}^{\circ}}[\psi(s^{\prime})\psi(s^{\prime})^{\top}]\right|\leq 2\mathcal{O}(L\epsilon)
It follows that:
Report issue for preceding element
‖ θ r − θ ∘ ‖ 2 \displaystyle|\theta_{r}-\theta^{\circ}|_{2}
≤ ‖ A 𝒫 , r †  ( b 𝒫 − b 𝒫 ∘ ) ‖ 2 + ‖ ∑ i = r + 1 d v i  v i T  θ ∘ ‖ 2 + 2  𝒪  ( L  ϵ ) \displaystyle\leq|A_{\mathcal{P},r}^{\dagger}(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})|{2}+|\sum{i=r+1}^{d}v_{i}v_{i}^{T}\theta^{\circ}|_{2}+2\mathcal{O}(L\epsilon)
≤ 1 σ 𝒫 , r  ‖ ( b 𝒫 − b 𝒫 ∘ ) | | 2 + ‖ ∑ i = r + 1 d v i  v i T  θ ∘ ‖ 2 + 2  𝒪  ( L  ϵ ) \displaystyle\leq\frac{1}{\sigma_{\mathcal{P},r}}|(b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}})||{2}+|\sum{i=r+1}^{d}v_{i}v_{i}^{T}\theta^{\circ}|_{2}+2\mathcal{O}(L\epsilon)
For the second term, we use θ ∘ = V ∘  Σ 𝒫 ∘ − 1  U ∘ − 1  b 𝒫 ∘ , ω \theta^{\circ}=V^{\circ}\Sigma^{-1}{\mathcal{P}^{\circ}}{U^{\circ}}^{-1}b{\mathcal{P}^{\circ},\omega} to get:
Report issue for preceding element
‖ ∑ i = r + 1 d v i  v i ⊤  θ ∘ ‖ 2 \displaystyle\left|\sum_{i=r+1}^{d}v_{i}v_{i}^{\top}\theta^{\circ}\right|_{2}
= ‖ ∑ i = r + 1 d v i  ∑ j = 1 r ∘ v i ⊤  v j ∘  σ 𝒫 ∘ , j − 1  u ∘ j ⊤  b 𝒫 ∘ ‖ 2 \displaystyle=\left|\sum_{i=r+1}^{d}v_{i}\sum_{j=1}^{{r^{\circ}}}v_{i}^{\top}v^{\circ}{j}\sigma{\mathcal{P}^{\circ},j}^{-1}{u^{\circ}}{j}^{\top}b{\mathcal{P}^{\circ}}\right|_{2}
≤ ‖ ∑ i = r + 1 d ∑ j = 1 r ∘ v i ⊤  v j ∘  σ 𝒫 ∘ , j − 1  u ∘ j ⊤  b 𝒫 ∘ ‖ 2 \displaystyle\leq\left|\sum_{i=r+1}^{d}\sum_{j=1}^{{r^{\circ}}}v_{i}^{\top}v^{\circ}{j}\sigma{\mathcal{P}^{\circ},j}^{-1}{u^{\circ}}{j}^{\top}b{\mathcal{P}^{\circ}}\right|_{2}
= ∑ i = r + 1 d ‖ v i ⊤  v i ∘  σ 𝒫 ∘ , i − 1  u ∘ i ⊤  b 𝒫 ∘ + ∑ j ≠ i r ∘ v i ⊤  v j ∘  σ 𝒫 ∘ , j − 1  u ∘ j ⊤  b 𝒫 ∘ ‖ 2 \displaystyle=\sum_{i=r+1}^{d}\left|v_{i}^{\top}v^{\circ}{i}\sigma{\mathcal{P}^{\circ},i}^{-1}{u^{\circ}}{i}^{\top}b{\mathcal{P}^{\circ}}+\sum_{j\neq i}^{{r^{\circ}}}v_{i}^{\top}v^{\circ}{j}\sigma{\mathcal{P}^{\circ},j}^{-1}{u^{\circ}}{j}^{\top}b{\mathcal{P}^{\circ}}\right|_{2}
≤ ∑ i = r + 1 d ‖ v i ⊤ ‖ 2  ‖ v i ∘ ‖ 2  σ 𝒫 ∘ , i p − 1 + ∑ i = r + 1 d ∑ j ≠ i r ∘ ‖ v i ⊤  v j ∘  σ 𝒫 ∘ , j − 1  u ∘ j ⊤  b 𝒫 ∘ ‖ 2 \displaystyle\leq\sum_{i=r+1}^{d}|v_{i}^{\top}|{2}|v^{\circ}{i}|{2}\sigma{\mathcal{P}^{\circ},i}^{p-1}+\sum_{i=r+1}^{d}\sum_{j\neq i}^{{r^{\circ}}}|v_{i}^{\top}v^{\circ}{j}\sigma{\mathcal{P}^{\circ},j}^{-1}{u^{\circ}}{j}^{\top}b{\mathcal{P}^{\circ}}|_{2}
≤ ( d − r )  σ 𝒫 ∘ , r p − 1 + ∑ i = r + 1 d ∑ j ≠ i r ∘ ‖ v i ⊤  v j ∘ ‖ 2  σ 𝒫 ∘ , j p − 1 \displaystyle\leq(d-r)\sigma_{\mathcal{P}^{\circ},r}^{p-1}+\sum_{i=r+1}^{d}\sum_{j\neq i}^{{r^{\circ}}}|v_{i}^{\top}v^{\circ}{j}|{2}\sigma_{\mathcal{P}^{\circ},j}^{p-1}
≤ ( d − r )  σ 𝒫 ∘ , r p − 1 + ( d − r )  r ∘  σ 𝒫 ∘ , 1 p − 1 \displaystyle\leq(d-r)\sigma_{\mathcal{P}^{\circ},r}^{p-1}+(d-r){r^{\circ}}\sigma_{\mathcal{P}^{\circ},1}^{p-1}
It follows that:
Report issue for preceding element
‖ θ r − θ ∘ ‖ 2 ≤ 1 σ 𝒫 , r  ‖ b 𝒫 − b 𝒫 ∘ ‖ 2 + ( d − r )  σ 𝒫 ∘ , r p − 1 + ( d − r )  r ∘  σ 𝒫 ∘ , 1 p − 1 + 2  𝒪  ( L  ϵ ) \displaystyle|\theta_{r}-\theta^{\circ}|{2}\leq\frac{1}{\sigma{\mathcal{P},r}}|b_{\mathcal{P}}-b_{\mathcal{P}^{\circ}}|{2}+(d-r)\sigma{\mathcal{P}^{\circ},r}^{p-1}+(d-r){r^{\circ}}\sigma_{\mathcal{P}^{\circ},1}^{p-1}+2\mathcal{O}(L\epsilon)
(15)
A.2 Additional Result
Report issue for preceding element
A.2.1 Basic Settings
Report issue for preceding element
In all experiments, we evaluate the performance of benchmark algorithms on the Hopper-v3, Walker2d-v3, Humanoid-v3, and Ant-v3 environments from OpenAI Gym. To ensure a fair comparison, we use the open-source implementation 1 1 1 https://github.com/openai/spinningup of SAC as the base RL algorithm for all methods, and for RNAC we adopt its original PPO-based trainer without modification. We use Adam as the optimizer in SAC, where both the policy and Q-networks are implemented as two-layer MLPs with hidden sizes ( 64 , 64 ) (64,64) and ReLU activation functions. The learning rate for both networks is fixed at 3 × 10 − 3 3\times 10^{-3} . For our proposed algorithm, we set the truncation interval d t d_{t} to 0.7 × 10 6 0.7\times 10^{6} for Walker2d and 10 6 10^{6} for Hopper, Humanoid, and Ant, meaning the model is truncated every d t d_{t} policy optimization steps. This choice ensures that rank adaptation occurs much less frequently than policy updates.
Report issue for preceding element
To impose a rank constraint on a weight matrix W W , we first factorize it as W = W 1  W 2 W=W_{1}W_{2} and apply singular value decomposition (SVD) to the product W 1  W 2 = U  Σ  V ⊤ W_{1}W_{2}=U\Sigma V^{\top} . We then reparameterize as
Report issue for preceding element
W 1 = U [ : , : r ^ ]  Σ [ : r ^ ] , W 2 = Σ [ : r ^ ]  V [ : r ^ , : ] , W_{1}=U_{[:,:\hat{r}]}\sqrt{\Sigma_{[:\hat{r}]}},\quad W_{2}=\sqrt{\Sigma_{[:\hat{r}]}}V_{[:\hat{r},:]},
where r ^ ≤ r \hat{r}\leq r is the target rank. This projects W W onto a lower-rank manifold, thereby enforcing the constraint. As shown in Figure 5, inserting an intermediate linear layer (yellow, within the red region) provides an explicit implementation of this rank reduction.
Report issue for preceding element 
Figure 5: To impose the low-rank constraint, we insert an intermediate linear layer (without activation functions or bias) between the original two layers. This layer acts as a bottleneck that enforces a low-rank factorization of the weight matrix via SVD approximation. Report issue for preceding element
Additionally, to avoid loss of momentum after optimizer resets, we apply a standard cosine decay schedule with warm-up, as in (Lialin et al., 2023; Touvron et al., 2023) . Specifically, upon each reset, we set the learning rate to zero, gradually warm it up to the target value over 2000 steps, and then resume following the cosine schedule.
Report issue for preceding element
We present the practical implementation of our proposed algorithm in Alg. 1. At each iteration, we warm-start both the policy network and Q-network in SAC using the trained neural networks from the previous iteration, and then run SAC in the corresponding MuJoCo environment to continue training.
Report issue for preceding element
For the robust RL baselines, we use their official open-source implementations. The implementation of RNAC is available at https://github.com/tliu1997/RNAC. To modify the dynamics kernel, we follow the setting in OMPO Luo et al. ( 2024) , using their codebase at https://github.com/Roythuly/OMPO. For Parseval regularization, we use the implementation provided at https://github.com/wechu/parseval_reg. In MuJoCo experiments with Parseval regularization, we adopt the same setup, tuning the regularization coefficient from { 0.001 , 0.0001 , 0.00001 } {0.001,0.0001,0.00001} and selecting the best-performing value. We also follow the original implementation by setting s = 2 s=2 in the Parseval constraint ‖ W  W ⊤ − s  I ‖ F |WW^{\top}-sI|_{F} . For Tiwari et al. ( 2025) , we follow their default configuration with a sparsification layer and set the hidden layer size to 1024 neurons, consistent with their original setting.
Report issue for preceding element
A.2.2 Model Uncertainty Setting
Report issue for preceding element
Following the setup in Luo et al. ( 2024) , we simulate model uncertainty by introducing continuously varying environment parameters during training. This design encourages policies to generalize across dynamic variations rather than overfitting to a fixed set of dynamics. The specific parameter schedules for each environment are as follows:
Report issue for preceding element
• Hopper: The torso and foot lengths vary with the episode index i i as Report issue for preceding element L torso  ( i ) = 0.4 + 0.2 ⋅ sin  ( 0.2  i ) , L foot  ( i ) = 0.39 + 0.2 ⋅ sin  ( 0.2  i ) . L_{\text{torso}}(i)=0.4+0.2\cdot\sin(0.2i),\quad L_{\text{foot}}(i)=0.39+0.2\cdot\sin(0.2i).
• Walker2d: The torso and foot lengths follow a similar pattern with Report issue for preceding element L torso  ( i ) = 0.2 + 0.1 ⋅ sin  ( 0.3  i ) , L foot  ( i ) = 0.1 + 0.05 ⋅ sin  ( 0.3  i ) . L_{\text{torso}}(i)=0.2+0.1\cdot\sin(0.3i),\quad L_{\text{foot}}(i)=0.1+0.05\cdot\sin(0.3i).
• Ant: Gravity g g and wind speed W W change across episodes according to Report issue for preceding element g  ( i ) = 14.715 + 4.905 ⋅ sin  ( 0.5  i ) , W  ( i ) = 1 + 0.2 ⋅ sin  ( 0.5  i ) . g(i)=14.715+4.905\cdot\sin(0.5i),\quad W(i)=1+0.2\cdot\sin(0.5i).
• Humanoid: The same variation as Ant is applied, but the wind effect is amplified due to the humanoid's larger mass and drag: Report issue for preceding element g  ( i ) = 14.715 + 4.905 ⋅ sin  ( 0.5  i ) , W  ( i ) = 1 + 0.5 ⋅ sin  ( 0.5  i ) . g(i)=14.715+4.905\cdot\sin(0.5i),\quad W(i)=1+0.5\cdot\sin(0.5i). 
Figure 6: Visualization of uncertain dynamics in the Hopper-v3 task, where the torso and foot lengths vary across episodes. Report issue for preceding element
A.2.3 Rank Convergence of the Alternative Algorithm
Report issue for preceding element
In this subsection, we conduct an ablation study to examine alternative strategies for selecting the cut-off rank of the SVD beyond Eq. 14. As reviewed by Falini ( 2022) , numerous criteria have been proposed for truncated SVD. Here, we consider a simple hard-thresholding approach based on the ratio between singular values. Specifically, we define the cut-off rank as
Report issue for preceding element
r ^ = min  { ℓ ∈ { 1 , 2 , … , d } | σ ℓ σ 1 ≤ β } . \hat{r};=;\min\Bigl{,\ell\in{1,2,\dots,d};\big|;\frac{\sigma_{\ell}}{\sigma_{1}}\leq\beta\Bigr}.
(16)
Figure 7 illustrates a fundamental limitation of this criterion. After the initial iteration, the rank selection process stagnates because the rule in Eq. 16 depends only on the largest singular value. As a result, it ignores the broader spectral structure of the parameters and fails to adapt dynamically to spectral variations during training. Therefore, we continue to use Eq. 14 as our primary rule for selecting the cut-off rank.
Report issue for preceding element 
(a) Walker2d Report issue for preceding element 
(b) Hopper Report issue for preceding element
Figure 7: Comparison of Rank Selection by hard-thresholding method. Report issue for preceding element
A.2.4 Policy performance under varying dynamics
Report issue for preceding element
In this subsection, we present additional experimental results under perturbations of physical hyperparameters (e.g., torso length, foot length) in the Hopper-v3 and Walker2d-v3 environments. As shown in Figure 8, the proposed AdaRL algorithm exhibits superior robustness and outperforms the strongest baseline (Tiwari et al., 2025) in the majority of cases.
Report issue for preceding element 
(a) Walker2d-v3: Varying torso length with fixed foot length Report issue for preceding element 
(b) Walker2d-v3: Varying foot length with fixed torso length Report issue for preceding element 
(c) Hopper-v3: Varying torso length with fixed foot length Report issue for preceding element 
(d) Hopper-v3: Varying foot length with fixed torso length Report issue for preceding element
Figure 8: Policy performance under perturbations of physical hyperparameters in Walker2d-v3 and Hopper-v3. Subfigures (a) and (c) show results when torso length is varied with fixed foot length, while (b) and (d) correspond to varying foot length with fixed torso length. The proposed AdaRL algorithm outperforms the strongest baseline (Tiwari et al., 2025) in the majority of cases, demonstrating superior robustness under perturbed dynamics. Report issue for preceding element
Report Issue
Report GitHub Issue
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub
Report Issue for Selection
Generated by L A T E xml[LOGO]
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" button.
Open a report feedback form via keyboard, use " Ctrl + ?".
Make a text selection and click the "Report Issue for Selection" button near your cursor.
You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.