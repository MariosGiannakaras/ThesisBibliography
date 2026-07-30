> Source: https://arxiv.org/pdf/2404.03578

Distributionally Robust Reinforcement Learning with Interactive Data Collection: Fundamental Hardness and Near-Optimal 
Algorithms 
Miao Lu∗† Han Zhong∗‡ Tong Zhang§ Jose Blanchet† 
April 5, 2024; Revised: July 13, 2026 
Abstract 
The sim-to-real gap, which represents the disparity between training and testing environments, poses a significant challenge in reinforcement learning (RL). A promising approach to addressing this challenge is distributionally robust RL, often framed as a robust Markov decision process (RMDP). In this framework, the objective is to find a robust policy that achieves good performance under the worst-case scenario among all environments within a pre-specified uncertainty set centered around the training environment. Unlike previous work, which relies on a generative model or a pre-collected offline dataset enjoying good coverage of the deployment environment, we tackle robust RL via interactive data collection, where the learner interacts with the training environment only and refines the policy through trial and error. In this robust RL paradigm, two main challenges emerge: managing distributional robustness while striking a balance between exploration and exploitation during data collection. Initially, we establish that sampleefficient learning without additional assumptions is unattainable owing to the curse of support shift; i.e., the potential disjointedness of the distributional supports between the training and testing environments. To circumvent such a hardness result, we introduce the vanishing minimal value assumption to RMDPs with a total-variation (TV) distance robust set, postulating that the minimal value of the optimal robust value function is zero. We prove that such an assumption effectively eliminates support shift pathologies for RMDPs with a TV distance robust set, and present an algorithm with near-optimal sample complexity. To demonstrate the breadth of our framework, we further extend our algorithm and theory to new robust set formulations and robust Markov game settings. Finally, to illustrate the operational relevance of our framework, we apply our algorithm to the data-driven robust inventory control, yielding explicit learning guarantees for robust decision-making under demand shifts. Our work makes the initial step to uncovering the inherent difficulty of robust RL via interactive data collection and sufficient conditions for designing a sample-efficient algorithm accompanied by sharp sample complexity analysis. 
Keywords: distributionally robust reinforcement learning, interactive data collection, robust Markov decision process, robust Markov game, sample complexity, online regret 
∗Equal contributions. Email to miaolu@stanford.edu, hanzhong@stu.pku.edu.cn †Department of Management Science and Engineering, Stanford University. ‡Center for Data Science, Peking University. §Department of Computer Science, University of Illinois Urbana-Champaign. 
1 
 
 
 
 
 
 
 
 
 
 
Contents 
1 Introduction 4 1.1 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 1.2 Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 1.3 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 
2 Preliminaries 9 2.1 Robust Markov Decision Processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 2.2 Robust RL with Interactive Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 
3 A Hardness Result: The Curse of Support Shift 12 
4 A Solvable Case, Efficient Algorithm, and Sharp Analysis 14 4.1 Vanishing Minimal Value: Eliminating Support Shift . . . . . . . . . . . . . . . . . . . . . . . 14 4.2 Algorithm Design: OPROVI-TV . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 
4.2.1 Training Environment Transition Estimation . . . . . . . . . . . . . . . . . . . . . . . 16 4.2.2 Optimistic Robust Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 
4.3 Theoretical Guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 
5 Extension I: Robust Set with Bounded Transition Probability Ratio 19 
6 Extension II: Robust Decision Making in Multi-Agent Systems 20 6.1 Learning against an Adversarial Opponent under Environment Ambiguity . . . . . . . . . . . 20 6.2 Algorithm and Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 
7 Application: Data-Driven Robust Inventory Control 25 7.1 Inventory Control as a Finite-horizon MDP . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 7.2 Distributional Robustness via an S ×A-rectangular TV Uncertainty Set . . . . . . . . . . . . 26 7.3 Theoretical Guarantee for Robust Inventory Learning . . . . . . . . . . . . . . . . . . . . . . 27 
8 Conclusions and Discussions 28 
A Proofs for Properties of RMDPs with TV Robust Sets 35 A.1 Proof of Proposition 2.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35 A.2 Proof of Proposition 2.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 A.3 Proof of Proposition 4.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 
B Proofs for Hardness Results 39 B.1 Proof of Theorem 3.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39 B.2 Proof of Lemma B.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41 
C Proofs for Theoretical Analysis of OPROVI-TV 42 C.1 Proof of Theorem 4.6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 C.2 Key Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45 C.3 Proof of Lemma C.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 C.4 Proof of Lemma C.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 C.5 Proof of Lemma C.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 C.6 Proof of Lemma C.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 C.7 Proof of Lemma C.6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 C.8 Other Technical Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 
C.8.1 Concentration Inequalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51 C.8.2 Variance Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54 C.8.3 Other Auxiliary Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55 
2
D Proofs for Extension I (Section 5) 55 D.1 Proof of Corollary 5.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55 
E Proofs for Extension II (Section 6) 57 E.1 Proof of Proposition 6.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 E.2 Proof of Theorem 6.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 
3
1 Introduction 
Reinforcement learning (RL) serves as a framework for addressing complex decision-making problems through iterative interactions with environments. Recent advancements in deep reinforcement learning have enabled the successful application of the general RL framework across various domains, including mastering strategic games, such as Go (Silver et al., 2017), robotics (Kober et al., 2013), and aligning large language models (LLMs; Ouyang et al., 2022). The critical factors contributing to these successes encompass not only the potency of deep neural networks and modern deep RL algorithms but also the availability of substantial training data. However, there are scenarios, such as healthcare (Wang et al., 2018), inventory control (Boute et al., 2022), and autonomous driving (Kiran et al., 2021), among others, where collecting RL data in the target domain is challenging, costly, or even infeasible. In such cases, the sim-to-real transfer (Kober et al., 2013; Sadeghi and Levine, 2016; Peng et al., 2018; Zhao et al., 2020) becomes a remedy, where the RL agent is trained in simulated environments and subsequently deployed in the real world. Nevertheless, the discrepancy between the training environments and the testing environments, also known as the sim-to-real gap, will typically result in suboptimal performance of RL agents in real-world applications. One promising strategy to mitigate performance degradation due to the sim-to-real gap is robust RL (Iyengar, 2005; Pinto et al., 2017; Hu et al., 2022), which aims to learn policies exhibiting strong (i.e. robust) performance under environmental deviations from the training environment. It effectively hedges the epistemic uncertainty arising from the differences between the training environment and the unknown testing environments. 
A robust RL problem is formulated as a robust Markov decision process (RMDP), with different types of robust sets characterizing different environment shifts. Prior theoretical works on robust RL have developed algorithms with provable sample complexity guarantees, but they typically rely on either a generative model1 
(Yang et al., 2022; Panaganti and Kalathil, 2022; Xu et al., 2023; Shi et al., 2023) or offline datasets with good coverage of the deployment environment (Zhou et al., 2021b; Panaganti et al., 2022; Shi and Chi, 2022; Ma et al., 2022; Blanchet et al., 2023). Notably, the current literature does not explicitly address the exploration problem, which stands as one of the fundamental challenges in reinforcement learning through trial-and-error (Sutton and Barto, 2018). Meanwhile, the empirical success of robust RL methods (Pinto et al., 2017; Kuang et al., 2022; Moos et al., 2022) typically relies on reinforcement learning through interactive data collection in the training environment, where the agent iteratively and actively interacts with the environment, collecting data, optimizing and robustifying its policy. Given that all of the existing literature on the theory of robust RL relies on a generative model or a pre-collected offline dataset, it is natural to ask: 
Can we design a provably sample-efficient robust RL algorithm that relies on interactive data collection in the training environment? 
Answering this question faces a fundamental challenge: during interactive data collection, the learner no longer has oracle control over the training data distributions that are induced by the policy learned through the interaction process. In particular, it could be the case that certain data patterns that are crucial for the policy to be robust across all testing environments are not accessible through interactive data collection, even with a sophisticated exploration mechanism. For example, specific states may not be accessible within the training environment dynamics but could be reached in the testing environment dynamics. 
In contrast, previous work has demonstrated that robust RL through a generative model or a pre-collected offline dataset with good coverage does not face such difficulties. For the generative model setup, fortunately, the learner can directly query any state-action pair and observe the sampled next state from the generator. Intuitively, once the states that could appear in the testing environment trajectory are queried enough times, it is then possible to guarantee the performance of the learned policy in testing environments. The situation is similar if one has a pre-collected offline dataset that enjoys good coverage of testing environments. In this work, we make the initial step towards studying the theory and applications of robust RL with interactive data collection. At a high level, our results and contributions are three-fold. 
 (Fundamental hardness.) We first prove a hardness result for robust RL with interactive data collection. Precisely, certain RMDPs that are solvable sample-efficiently with a generative model or with sufficient offline data with good coverage properties are, in contrast, intractable for robust RL through interactive data collection. This shows a gap between robust RL with these two different kinds of data-type oracles. 
1A generative model here means a mechanism that when queried at some state, action, and time step, returns a sample of next state. Here we distinguish this notion with the notion of simulator or simulated environment which generally refers to a human-made training environment that mimics the real-world environment. 
4
 (Solvable class and sample-efficient algorithm.) We identify a tractable subclass of RMDPs, for which we further propose a novel robust RL algorithm that can provably learn a near-optimal robust policy through interactive data collection. This implies that robust RL with interactive data collection is still possible for certain subclasses of RMDPs. 
 (Extensions and applications.) To demonstrate the breadth of our theory, we extend it to two additional robust RL settings: a different robust-set formulation and a multi-agent extension. Finally, to showcase the practical relevance of our framework, we instantiate it in a representative operations research application that naturally exhibits sim-to-real (model-shift) concerns. 
Together, our work answers the above question and shows that robust RL with interactive data collection is not only theoretically characterizable, but also directly applicable to canonical operations problems. In the following section, we explain more explicitly the problem setup and the contributions we make. 
1.1 Contributions 
This work primarily studies robust RL in a finite-horizon RMDP with an S ×A-rectangular total-variation distance (TV) robust set (see Assumption 2.1 and Definition 2.4)2 with interactive data collection. 
Fundamental hardness. We construct a class of hard-to-learn RMDPs (see Example 3.1 and Figure 1) and demonstrate that any learning algorithm inevitably incurs an Ω(ρ·HK)-online regret (see (2.4)) under at least one RMDP instance. Here, ρ signifies the radius of the TV robust uncertainty set, H is the horizon, and K denotes the number of interactive episodes. This linear regret lower bound underscores the impossibility of sample-efficient robust RL via interactive data collection in general. 
Identifying a tractable case. Upon close examination of the challenging instance, we recognize that the primary obstacle to achieving sample-efficient learning lies in the curse of support shift, i.e., the disjointedness of distributional support between the training environment and the testing environments. In a broader sense, the curse of support shift also refers to situations where states that often appear in testing environments are extremely hard to reach in the training environment3. 
To rule out these pathological instances, we propose the vanishing minimal value assumption (Assump-tion 4.1), positing that the optimal robust value function reaches zero at a specific state. Such an assumption naturally applies to the sparse reward RL paradigm and offers a broader scope compared to the “fail-state” assumption utilized in prior studies on offline RMDPs with function approximation (Panaganti et al., 2022). For a comprehensive discussion on this comparison, please refer to Remark 4.4. On the theoretical front, we establish that the vanishing minimal value assumption effectively mitigates the support shift issues between training and the testing environments (Proposition 4.2), rendering robust RL with interactive data collection feasible for RMDPs equipped with TV robust sets. 
Efficient algorithm with sharp sample complexity. Under the vanishing minimal value assumption, we develop an algorithm named OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV, Algo-
rithm 1). We first prove that OPROVI-TV achieves sublinear online robust regret of order Õ( √ K) over K 
episodes of interactive data collection (Theorem 4.6). By a standard online-to-batch conversion, this regret 
2We notice that all of the previous work on sample-efficient robust RL in RMDPs with TV robust sets (Yang et al., 2022; Panaganti and Kalathil, 2022; Panaganti et al., 2022; Xu et al., 2023; Blanchet et al., 2023; Shi et al., 2023) relies on defining the TV distance through the general f -divergence so that a strong duality representation holds. But this implicitly requires the testing environment transition probability to be absolutely continuous w.r.t. the training environment transition probability. In this paper, we do not make such a restriction. We prove the same strong duality even if the absolute continuity does not hold. In fact, all the previous work can be directly extended to such TV distance definition via our more general strong duality result. 
3We remark that an existing work of Dong et al. (2022) also studies the problem of robust RL with interactive data collection. They consider S×A-rectangular RMDPs with a TV robust set, assuming that the support of the training environment transition is the full state space. They claim the existence of an algorithm that enjoys a Õ( 
√ K)-online regret. We point out that their 
proof exhibits an essential flaw (misuse of Lemma 12 therein) and therefore the regret they claim is invalid. 
5
guarantee further implies that OPROVI-TV can find an ε-optimal robust policy within 
Õ 
( min{H, ρ−1} · H 
2SA 
ε2 
) (1.1) 
interactive samples (Corollary 4.7). Here S and A denote the number of states and actions, ρ represents the radius of the TV robust set, and H is the horizon length of each episode. To the best of our knowledge, this is the first provably sample-efficient algorithm for robust RL with interactive data collection. 
According to (1.1), the sample complexity of finding an ε-optimal robust policy decreases as the radius ρ of the robust set increases. This coincides with the findings of Shi et al. (2023) who consider robust RL in infinite-horizon discounted RMDPs with TV robust sets within the generative model setup. When the radius ρ = 0, an RMDP reduces to a standard MDP, and the sample complexity (1.1) recovers the minimax-optimal 
sample complexity for online RL in standard MDPs up to logarithm factors, i.e., Õ(H3SA/ε2). At the other extreme, when ρ → 14, finding an ε-optimal robust policy turns out to require nearly a factor of H fewer samples, up to logarithmic factors, than finding the optimal policy in a standard MDP. 
Extensions to other robust RL setups. Going beyond the main results on robust RL in finite-horizon RMDPs with S ×A-rectangular TV robust sets, we further extend our algorithm and theory to other types of robust decision-making setups. Specifically: 
 (Robust RL with other robust sets.) We first study the problem of robust RL in another type of RMDPs, S ×A-rectangular discounted RMDPs equipped with robust sets consisting of transition probabilities with bounded ratio to the nominal kernel (Section 5). This class of RMDPs naturally does not suffer from the support shift issue, and we prove that it is equivalent to the S × A-rectangular RMDP with TV robust set and vanishing minimal value assumption in an appropriate sense due to Proposition 4.2. Consequently, using Algorithm 1 through the auxiliary construction, we can also solve robust RL for this new model sample-efficiently (Corollary 5.1). Such a result also echoes our intuition on the curse of support shift. 
 (Robust multi-agent RL in robust Markov games.) We further extend our framework to robust Markov games (Kardes, 2005) that jointly capture strategic opponents and environment ambiguity (Section 6). This setting is motivated by multi-agent decision-making problems in operations research (e.g., security games, competitive resource allocation), where one must simultaneously hedge against the worst-case opponent behavior and the worst-case transition. We introduce the robust Nash value with Bellman– Shapley recursion and establish its existence and strong duality under S × A × B-rectangular TV robust set (Proposition 6.2). Here A and B denote the action spaces of the two players in the game with A and B denoting their cardinalities. Building on this structure, we develop OPROVI-TV-MG 
(Algorithm 2), a game-theoretic extension of OPROVI-TV that estimates the joint-action transition kernels and performs optimistic robust max–min planning by solving per-state matrix games in each backward pass. Under the vanishing minimal value assumption for RMGs, our Theorem 6.5 proves that OPROVI-TV-MG achieves a sublinear online robust regret over K episodes of interactive data collection of order 
Õ ( min{H, ρ−1}HS 
√ ABK 
) against any adaptive Markov opponent sequence, showing that Player 1 can approach the robust Nash value through online interaction. 
Applications to data-driven inventory control. To demonstrate the practical relevance of our framework, we apply our algorithm and theory to a canonical operations-management problem: 
 (Data-driven robust inventory control under demand distribution shifts.) We apply our framework to data-driven robust inventory control under demand distribution shift (Section 7). Motivated by the fact that the actual demand law may deviate from the training demand law simulating the real-world inventory or representing the historical pattern, we model demand perturbations via an S × A-rectangular 
4We do not signify the situation when ρ = 1 since in that case the TV robust set contains all possible transition probabilities, making the problem statistically trivial. In that case, no sample is needed. 
6
TV ambiguity set, which induces a conservative TV ball on the transition kernel (Lemma 7.1). Exploit-ing that the induced inventory system forms a finite-horizon RMDP equipped with S ×A-rectangular TV robust set and satisfies the vanishing minimal value condition due to the existence of absorbing aggregated emergency (fail) state, we are able to directly apply OPROVI-TV (Algorithm 1) to learn a distributionally robust ordering policy from interactive data collection in the training environment only. In particular, Theorem 7.2 establishes that OPROVI-TV finds an ε-optimal robust inventory policy within 
Õ ( min{H, ρ−1} · H 
2(B + I)Q 
ε2 
) episodes of interactive data collection in the training environment. Here ρ signifies the robust set size reflecting the demand shift, I denotes the inventory capacity, B denotes the backlog threshold, and Q is the order capacity (see more concrete definitions in Section 7). 
1.2 Related Works 
Robust reinforcement learning in robust Markov decision processes. Robust RL is usually framed as a robust Markov decision process (RMDP) (Iyengar, 2005; El Ghaoui and Nilim, 2005; Wiesemann et al., 2013). There is a long line of work dedicated to the problem of how to solve for the optimal robust policy of a given RMDP, i.e., planning (Iyengar, 2005; El Ghaoui and Nilim, 2005; Xu and Mannor, 2010; Wang and Zou, 2022; Wang et al., 2022; Kuang et al., 2022; Wang et al., 2023a; Yu et al., 2023; Zhou et al., 2023; Li and Lan, 2023; Wang et al., 2023c; Ding et al., 2024). Recently, the community has also witnessed a growing body of work on sample-efficient robust RL in RMDPs with different data collection oracles, including the generative model setup (Yang et al., 2022; Panaganti and Kalathil, 2022; Si et al., 2023; Wang et al., 2023b; Yang et al., 2023; Xu et al., 2023; Clavier et al., 2023; Wang et al., 2023d; Shi et al., 2023), offline setting (Zhou et al., 2021b; Panaganti et al., 2022; Shi and Chi, 2022; Ma et al., 2022; Blanchet et al., 2023; Liu and Xu, 2024b; Wang et al., 2024), and interactive data collection setting (Badrinath and Kalathil, 2021; Wang and Zou, 2021; Liu and Xu, 2024a). 
Our work falls into the paradigm of sample-efficient robust RL through interactive data collection. Wang and Zou (2021) and Badrinath and Kalathil (2021) propose efficient online learning algorithms to obtain the optimal robust policy of an infinite horizon RMDP, but none of them handle the challenge of exploration in online RL by assuming the access to explorative policies. This assumption enables the learner to collect highquality data essential for effective learning and decision-making. In contrast, our work focuses on developing efficient algorithms for the fully online setting, where there is no predefined exploration policy to use. Under this more challenging setting, we address the exploration challenge through algorithmic design rather than relying on assumed access to explorative policies. 
During the preparation of this work, we are aware of several concurrent and independent works (Liu and Xu, 2024a,b; Wang et al., 2024), which study a different type of RMDPs known as d-rectangular linear MDPs (Ma et al., 2022; Blanchet et al., 2023). In particular, Liu and Xu (2024b) and Wang et al. (2024) consider the offline setting, while Liu and Xu (2024a) investigate robust RL through interactive data collection (offdynamics learning), thus bearing closer relevance to our work. More specifically, under the existence of a “fail-state”, the algorithm in Liu and Xu (2024a) can learn an ε-optimal robust policy with provable sample efficiency. In contrast, our work first explicitly uncovers the fundamental hardness of robust RL in RMDPs with TV robust set and without additional assumptions. To overcome the inherent difficulty, we adopt a vanishing minimal value assumption that strictly generalizes the “fail-state” assumption used in Liu and Xu (2024a). Moreover, our focus is on tabular S × A-rectangular RMDPs, with customized algorithmic design and theoretical analysis which allow us to obtain a sharp sample complexity bound. 
Finally, in Table 1, we compare the learning guarantees of our algorithms with those of prior work on robust RL for RMDPs with S×A-rectangular TV robust sets under various settings (generative model/offline dataset), and report the regret guarantee for our robust Markov game extension. 
Sample-efficient online non-robust reinforcement learning. Our work is also closely related to online non-robust RL, which is often formulated as a Markov decision process (MDP) with online data collection. For non-robust online RL, the key challenge is the exploration-exploitation tradeoff. There has been a long line of work (Azar et al., 2017; Dann et al., 2017; Jin et al., 2018; Zanette and Brunskill, 2019; Zhang et al., 
7
Model Assump. Algorithm Data oracle Sample complexity 
/ regret 
general case 
RPVL (Xu et al., 2023) generative model Õ ( 
H5SA ε2 
) DRVI (Shi et al., 2023) generative model Õ 
( min{Hγ ,ρ−1}H2 
γSA 
ε2 
) lower bound (Shi et al., 2023) generative model Ω 
( min{Hγ ,ρ−1}H2 
γSA 
ε2 
) P2MPO (Blanchet et al., 2023) offline dataset Õ 
( C⋆ robH 
4S2A 
ε2 
) lower bound (this work) interactive data collection intractable 
“fail-state” assumption 
RFQI (Panaganti et al., 2022) offline dataset Õ ( 
CfullH 4 γSA 
ρ2ε2 
) vanishing 
minimal value (Assumption 4.1) 
OPROVI-TV (this work) interactive data collection Õ ( 
min{H,ρ−1}H2SA 
ε2 
) vanishing 
minimal value (Assumption 6.4) 
OPROVI-TV-MG (this work) interactive data collection Õ ( min{H, ρ−1}HS 
√ ABK 
) 
Table 1: Comparison of learning guarantees for robust RL with TV ambiguity and its Markov-game extension. For the RMDP rows, the last column reports the sample complexity for learning an ε-optimal robust policy; for the RMG row, it reports online regret against adaptive Markov opponents. The rows involving infinite-horizon γ-discounted RMDPs use Hγ := (1 − γ)−1 as the effective horizon. The quantities C⋆ 
rob and Cfull denote robust partial and full coverage coefficients. 
2020c, 2021; Ménard et al., 2021; Wu et al., 2022; Li et al., 2023; Zhang et al., 2023) addressing this challenge in the context of tabular MDPs, where the state space and action space are finite and also relatively small. In particular, many algorithms (e.g., UCBVI in Azar et al. (2017)) have been proven capable of finding an ε-
optimal policy within Õ(H3SA/ε2) sample complexity. Notably, a standard MDP corresponds to an RMDP with a TV robust set and ρ = 0, suggesting that OPROVI-TV can naturally achieve nearly minimax-optimality for non-robust RL. Moving beyond the tabular setups, recent works also investigate online non-robust RL with linear function approximation (Jin et al., 2020; Ayoub et al., 2020; Zhou et al., 2021a; Zhong and Zhang, 2023; Huang et al., 2023b; He et al., 2023; Agarwal et al., 2023) and even general function approximations (Jiang et al., 2017; Sun et al., 2019; Du et al., 2021; Jin et al., 2021; Foster et al., 2021; Liu et al., 2022; Zhong et al., 2022; Liu et al., 2023; Huang et al., 2023a; Xu and Zeevi, 2023; Agarwal et al., 2023). 
Robust RL in robust Markov games. Robust Markov games, also known as robust stochastic games, extend robust Markov decision process to multi-agent settings with both strategic interaction between agents and environment ambiguity (Kardes, 2005). On the offline and generative model side, Blanchet et al. (2023) study offline RL in robust Markov games under general function approximations and propose the robust Nash equilibrium gap (RNE gap) as the performance criterion for a learned joint policy profile. Shi et al. (2024b) consider the tabular robust Markov games with a generative model oracle, studying the sample complexity of learning robust variants of Nash, correlated, and coarse correlated equilibria using equilibrium-gap metrics. Shi et al. (2024a) propose a different model of robust Markov games and obtain improved sample complexity guarantees that avoid the curse of dimensionality in the joint action space. All these works differ from ours in both data access and learning objective: they focus on robust equilibrium learning for a jointly controlled policy profile, whereas we study online interactive data collection with unknown transitions and an external adversarial opponent. Our goal is not to learn an approximate RNE for all players, but to control the regret of Player 1 against robust Nash value. On the online side, recent works (Farhat et al., 2025; Zheng and Lin, 2025) also study learning in robust Markov games. However, as discussed in Remark 6.3, they use cumulative equilibrium-gap objectives that are closer to the online analogue of the RNE gap, whereas our formulation uses a robust regret benchmark against the realized opponent policies, tailored to the setting where only Player 1 is under our control. 
8
Data-driven inventory control. Learning-based inventory control for unknown demand has been studied extensively in non-robust settings (e.g., Huh et al., 2011; Shi et al., 2016; Agrawal and Jia, 2019; Zhang et al., 2020a; Yuan et al., 2021; Lyu et al., 2024; Fan et al., 2024). On the robustness side, the classical work goes back to Scarf’s minimax formulation (Scarf et al., 1957) and subsequent robust and distributionally robust approaches to inventory control (Bertsimas and Thiele, 2006; Klabjan et al., 2013; Xin and Goldberg, 2022), which primarily focus on modeling demand ambiguity and solving the corresponding robust optimization or control problem. Our setting is different from both lines of prior work: we consider finite-sample learning from interactive data collected in a training environment, seeking a policy robust to demand shifts at deployment. 
Additional follow-up works. Following the initial version of this paper, several subsequent works extend the scope of the problem into different directions. Liu et al. (2024) study the linear function approximation setting and improve upon the earlier result from Liu and Xu (2024a). He et al. (2025); Ghosh et al. (2025a) consider online distributionally robust RL under other robust sets beyond the TV-based model studied here. Ghosh et al. (2025b) further investigates the problem under general function approximation. Finally, Zheng and Lin (2025); Farhat et al. (2025) extend the interactive robust RL problem to robust Markov games. 
1.3 Notations 
For any positive integer H ∈ N+, we denote {1, 2, . . . ,H} by [H]. Given a set X , we denote ∆(X ) as the set of probability distributions over X . For any distribution p ∈ ∆(X ), we define the shorthand for expectation and variance as 
Ep(·)[f ] := EX∼p(·)[f(X)], Vp(·)[f ] = Ep(·)[f 2]− (Ep(·)[f ]) 
2. 
For any set Q ⊆ ∆(X ), we define the robust expectation operator as 
EQ[f ] := inf p(·)∈Q 
EX∼p(·)[f(X)]. 
For any x, a ∈ R, we denote (x)+ = max{x, 0} and x∨a = max{x, a}. We use O(·) to hide absolute constant 
factors and use Õ to further hide logarithmic factors. 
2 Preliminaries 
2.1 Robust Markov Decision Processes 
We first introduce our underlying model for doing robust RL, the episodic robust Markov decision process (RMDP), denoted by a tuple (S,A,H, P ⋆, R,Φ). Here the set S is the state space and the set A is the action space, both with finite cardinality. The integer H is the length of each episode. The set P ⋆ = {P ⋆ 
h}Hh=1 is the collection of nominal transition kernels where P ⋆ 
h : S × A 7→ ∆(S). The set R = {Rh}Hh=1 is the collection of reward functions where Rh : S × A 7→ [0, 1]. For simplicity, we denote P = {P (·|·, ·) : S × A 7→ ∆(S)} as the space of all possible transition kernels, and we denote S = |S| and A = |A|. 
Most importantly and different from standard MDPs, the RMDP is equipped with a mappingΦ : P 7→ 2P 
that characterizes the robust set of any transition kernel in P. Formally, for any transition kernel P ∈ P, we call Φ(P ) the robust set of P . One could interpret the nominal transition kernel P ⋆ 
h as the transition of the training environment, while Φ(P ⋆ 
h ) contains all possible transitions of the testing environments. Given an RMDP (S,A,H, P ⋆, R,Φ), we consider using a Markovian policy to make decisions. A Marko-
vian decision policy (or simply, policy) is defined as π = {πh}Hh=1 with πh : S 7→ ∆(A) for each step h ∈ [H]. To measure the performance of a policy π in the RMDP, we introduce its robust value function, defined as 
V π h,P⋆,Φ(s) := inf 
P̃h∈Φ(P⋆ h ),1≤h≤H 
E{P̃h}H h=1,{πh}H 
h=1 
[ H∑ i=h 
Ri(si, ai) 
∣∣∣∣∣ sh = s 
] , ∀s ∈ S, 
Qπ h,P⋆,Φ(s, a) := inf 
P̃h∈Φ(P⋆ h ),1≤h≤H 
E{P̃h}H h=1,{πh}H 
h=1 
[ H∑ i=h 
Ri(si, ai) 
∣∣∣∣∣ sh = s, ah = a 
] , ∀(s, a) ∈ S ×A. 
9
Here the expectation is taken w.r.t. the state-action trajectories induced by policy π under the transition P̃ . One can also extend the definition of the robust value functions in terms of any collection of transition kernel P = {Ph}Hh=1 ⊂ P as V π 
h,P,Φ and Qπ h,P,Φ, which we usually use in the sequel. 
Among all the policies, we define the optimal robust policy π⋆ as the policy that can maximize the robust value function at the initial time step h = 1, i.e., 
π⋆ = argmax π={πh}H 
h=1 
V π 1,P⋆,Φ(s1), ∀s1 ∈ S. (2.1) 
In other words, the optimal robust policy π⋆ maximizes the worst case expected total rewards in all possible testing environments. For simplicity and without loss of generality, we assume in the sequel that the initial state s1 ∈ S is fixed. Our results could be directly generalized to s1 ∼ p0(·) ∈ ∆(S). Similarly, we can also define the optimal robust policy associated with a given stochastic process defined through any collection of transition kernels P = {Ph}Hh=1 ⊂ P in the same way as (2.1). We denote the optimal robust value functions associated with P as V ⋆ 
h,P,Φ and Q⋆ h,P,Φ respectively. 
S×A-rectangularity and robust Bellman equations. We consider robust sets Φ that have the S×A-rectangular structure (Iyengar, 2005), which requires that the robust set is decoupled and independent across different (s, a)-pairs. This kind of structure results in a dynamic programming representation of the robust value functions (efficient planning), and is thus commonly adopted in the literature of distributionally robust RL. More specifically, we assume the following. 
Assumption 2.1 (S ×A-rectangularity). We assume that, for any transition kernel P ∈ P, the robust set Φ(P ) takes the form 
Φ(P ) = ⊗ 
(s,a)∈S×A 
P(s, a;P ), where P(s, a;P ) ⊆ ∆(S). 
Under the S×A-rectangularity (Assumption 2.1), we have the so-called robust Bellman equation (Iyengar, 2005; Blanchet et al., 2023) which gives a dynamic programming representation of robust value functions. 
Proposition 2.2 (Robust Bellman equation). Under Assumption 2.1, for any transition P = {Ph}Hh=1 ⊆ P and any policy π = {πh}Hh=1 with πh : S 7→ ∆(A), it holds that for any (s, a, h) ∈ S ×A× [H], 
V π h,P,Φ(s) = Eπh(·|s) 
[ Qπ 
h,P,Φ(s, ·) ] , Qπ 
h,P,Φ(s, a) = Rh(s, a) + EP(s,a;Ph) 
[ V π h+1,P,Φ 
] . 
For the robust value functions of the optimal robust policy, we also have the following dynamic programming solution which plays a key role in our algorithm design and theoretical analysis. 
Proposition 2.3 (Robust Bellman optimal equation). Under Assumption 2.1, for any P = {Ph}Hh=1 ⊆ P, the robust value functions of any optimal robust policy of P satisfy that, for any (s, a, h) ∈ S ×A× [H], 
V ⋆ h,P,Φ(s) = max 
a∈A Q⋆ 
h,P,Φ(s, a), Q⋆ h,P,Φ(s, a) = Rh(s, a) + EP(s,a;Ph) 
[ V ⋆ h+1,P,Φ 
] . 
By taking π⋆ h(·|s) = argmaxa∈AQ 
⋆ h,P,Φ(s, a), then π 
⋆ = {π⋆ h}Hh=1 is an optimal robust policy under P . 
We remark that the original version of the robust Bellman equation (Iyengar, 2005) is for infinite horizon RMDPs and a customized proof of robust Bellman equation for finite horizon RMDPs (Proposition 2.2) can be found in Appendix A.1 of Blanchet et al. (2023). The robust Bellman optimal equation (Proposition 2.3) is then a corollary or can be directly proved in a similar manner. 
Total-variation distance robust set. In Assumption 2.1, the robust set P(s, a;P ) is often modeled as a “distribution ball” centered at P (·|s, a). In this paper, we mainly consider this type of robust sets specified by a total-variation distance ball. We put it in the following definition. 
Definition 2.4 (Total-variation distance robust set). Total-variation distance (TV) robust set is defined as 
Pρ(s, a;P ) := { P̃ (·) ∈ ∆(S) : DTV 
( P̃ (·) 
∥∥P (·|s, a)) ≤ ρ } , 
10
for some ρ ∈ [0, 1), where DTV(·∥·) denotes the total variation distance defined as 
DTV 
( p(·)∥q(·) 
) := 
1 
2 
∑ s∈S 
∣∣p(s)− q(s) ∣∣, ∀p(·), q(·) ∈ ∆(S). (2.2) 
Throughout the paper, when ρ = 0 we use the convention 1/0 := +∞. Hence min{H, ρ−1} = H at ρ = 0; products such as ρmin{H, ρ−1} are interpreted as 0. 
The TV robust set has recently been extensively studied by Yang et al. (2022); Panaganti and Kalathil (2022); Panaganti et al. (2022); Xu et al. (2023); Blanchet et al. (2023); Shi et al. (2023), which all focus on robust RL with a generative model or with a pre-collected offline dataset. Our work follows this RMDP setup and studies robust RL via interactive data collection (see Section 2.2). 
More importantly, we emphasize that by (2.2) in Definition 2.4, we do not define the TV distance through the notion of f -divergence which requires that the distribution p is absolutely continuous w.r.t. q, as is generally adopted by the above previous works on RMDP with TV robust sets. According to (2.2), we allow p to have a different support than q. That is, there might exist an s ∈ S such that p(s) > 0 and q(s) = 0. Given that, the TV robust set in Definition 2.4 could contain transition probabilities that have different supports than the nominal transition probability P ⋆(·|s, a). 
An essential property of the TV robust set is that the robust expectation involved in the robust Bellman equations (Propositions 2.2 and 2.3) has a duality representation that only uses the expectation under the nominal transition kernel. Previous works, e.g., Yang et al. (2022), have proved such a result when the TV distance is defined through f -divergence. Here we extend such a result to the TV distance defined directly through (2.2) that allows different supports between p and q. 
Proposition 2.5 (Strong duality representation). Under Definition 2.4, the following duality representation for the robust expectation holds, for any V : S 7→ [0, H] and Ph : S ×A 7→ ∆(S), 
EPρ(s,a;Ph) 
[ V ] = sup 
η∈[0,H] 
{ −EPh(·|s,a) 
[ (η − V )+ 
] − ρ · 
( η −min 
s∈S V (s) 
) + 
+ η 
} . (2.3) 
Proof of Proposition 2.5. Please refer to Appendix A.1 for a detailed proof of Proposition 2.5. 
Remark 2.6. Despite all previous works on RMDPs with TV robust sets relying on the definition of TV distance DTV(p(·)∥q(·)) with absolute continuity of p with respect to q to obtain the strong duality representation in the form of (2.3), their results can be directly extended to TV distance that allows for different support between p and q thanks to Proposition 2.5. 
Finally, another useful property of the robust value functions of an RMDP with TV robust sets is a fine characterization of the gap between the maximum and the minimum of the robust value function, which is first identified and utilized by Shi et al. (2023) for an infinite horizon RMDP with TV robust sets. In this work, we prove and use a similar result for the finite horizon case, concluded in the following proposition. 
Proposition 2.7 (Gap between maximum and minimum). Under Assumption 2.1 with the robust set specified by Definition 2.4, the robust value functions satisfy that 
max (s,a)∈S×A 
Qπ h,P,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P,Φ(s, a) ≤ min { H, ρ−1 
} , 
max s∈S 
V π h,P,Φ(s)−min 
s∈S V π h,P,Φ(s) ≤ min 
{ H, ρ−1 
} , 
for any transition P = {Ph}Hh=1 ⊂ P, any policy π, and any step h ∈ [H]. 
Proof of Proposition 2.7. Please refer to Appendix A.2 for a detailed proof of Proposition 2.7. 
We note that in the proof of Proposition 2.7, we actually show a tighter form of bound of the gap between the maximum and minimum as 
1 
ρ · ( 1− (1− ρ)H 
) . 
11
But in the sequel, we mainly use the form of min{H, ρ−1} for its brevity and the fact of (1− (1− ρ)H)/ρ = Θ(min{H, ρ−1}) in the sense that 
c ·min { H, ρ−1 
} ≤ (1− (1− ρ)H)/ρ ≤ min 
{ H, ρ−1 
} for any H ≥ H0 ∈ N+ and ρ ∈ [0, 1) with some absolute constant c > 0 that is independent of (H, ρ); when ρ = 0, the ratio (1− (1− ρ)H)/ρ is interpreted as its limit H. 
In contrast with a crude bound of H, such a fine upper bound decreases when ρ is large, which is essential to understanding the statistical limits of doing robust RL in RMDPs with TV robust sets. 
2.2 Robust RL with Interactive Data Collection 
In this paper, we study how to learn the optimal robust policy π⋆ in (2.1) from interactive data collection. Specifically, the learner is required to interact with only the training environment, i.e., P ⋆, for some K ∈ N episodes. In each episode k ∈ [K], the learner adopts a policy πk to interact with the training environment P ⋆ and to collect data. When the k-th episode ends, the learner updates its policy to πk+1 based on historical data and proceeds to the subsequent k+1-th episode. The learning process ends after a total of K episodes. 
Sample complexity. We use the notion of sample complexity as the key evaluation metric. For any given algorithm and predetermined accuracy level ε > 0, the sample complexity is the minimum number of episodes K required for the algorithm to output an ε-optimal robust policy π̂ which satisfies 
V ⋆ 1,P⋆,Φ(s1)− V π̂ 
1,P⋆,Φ(s1) ≤ ε. 
The goal is to design algorithms whose sample complexity has small or even optimal dependence on S,A,H, ρ, and 1/ε. Such a metric is connected with the sample complexity used in robust RL with generative models and offline settings (see related works for the references), wherein the sample complexity means the minimum number of generative samples or pre-collected offline data required to achieve ε-optimality. In contrast, here the sample complexity is measuring the least number of interactions with the training environment needed to learn π⋆, where no generative or offline sample is available. Such a learning protocol casts unique challenges on the algorithmic design and theoretical analysis to get the optimal sample complexity. 
Online regret. Another evaluation metric that is related to the minimization of sample complexity is the online regret. For online RL in standard non-robust MDPs, the notion of regret refers to the cumulative gaps between the non-robust optimal value functions and the non-robust value functions of the policies executed during each episode (Auer et al., 2008). Here for robust RL in RMDPs, we similarly define the regret as the cumulative difference between the optimal robust policy π⋆ and the executed policies {πk}Kk=1, but in terms of their robust value functions V π 
1,P⋆,Φ. Its formal definition is given as follows: 
RegretΦ(K) := 
K∑ k=1 
V ⋆ 1,P⋆,Φ(s1)− V πk 
1,P⋆,Φ(s1). (2.4) 
The goal is to design algorithms that can achieve a sublinear-in-K regret with small dependence on S,A,H, ρ. Intuitively, a sublinear-regret algorithm would approximately learn the optimal robust policy π⋆ purely from interacting with the training environment P ⋆. It turns out that any sublinear-regret algorithm can be easily converted to a polynomial-sample complexity algorithm by applying the standard online-to-batch conversion (Jin et al., 2018), which we show in detail in our theoretical analysis part. 
3 A Hardness Result: The Curse of Support Shift 
Unfortunately, we show in this section that in general such a problem of robust RL with online data collection is impossible – there exists a simple class of two RMDPs such that any algorithm suffers an Ω(K) online regret lower bound. However, previous works on robust RL with a generative model or offline data with 
12
sgood sgood sgood 
sbad sbad 
R1 = 1 R2 = 1 R3 = 1 
R2 = 0 R3 = 0 
Figure 1: Illustration of the hard example in Example 3.1. The solid lines represent possible transitions of the nominal transition kernel. The dashed lines represent the transitions induced by the worst case transition kernel in the robust set. The red solid line represents the transition where the two RMDP instances differ in that different actions lead to higher transition probability from sbad to sgood. We notice that when starting from s1 = sgood, the nominal transition kernel keeps the agent at sgood and no information at sbad is revealed. 
good coverage do provide sample-efficient ways to find the optimal robust policy for this class of RMDPs. This is a separation between robust RL with interactive data collection and generative model/offline data. 
We first explicitly present the hard example, which is a two-state, two-action RMDP with total-variation distance robust set. Please see also Figure 1 for an illustration of the example. 
Example 3.1 (Hard example of robust RL with interactive data collection). Consider two RMDPs M0 
and M1 which only differ in their nominal transition kernels. The state space is S = {sgood, sbad}, and the action space is A = {0, 1}. The horizon length H = 3. The reward function R is always 1 at the good state sgood and is 0 at the bad state sbad, i.e., 
Rh(s, a) = 
{ 1, s = sgood 
0, s = sbad , ∀(a, h) ∈ A× [H]. 
For the good state sgood, the next state is always sgood. For the bad state sbad, there is a chance to get to the good state sgood, with the transition probability depending on the action it takes. Formally, 
P ⋆,Mθ 
h (sgood|sgood, a) = 1, ∀(a, h) ∈ A× {1, 2}, ∀θ ∈ {0, 1}, 
P ⋆,Mθ 
2 (sgood|sbad, a) = 
{ p, a = θ 
q, a = 1− θ , ∀θ ∈ {0, 1}, 
where p, q are two constants satisfying 0 < q < p < 1. Intuitively, when at the bad state, the optimal action would result in a higher transition probability p to the good state than the transition probability q induced by the other action. Finally, we consider the robust set being specified by a total-variation distance ball centered at the nominal transition kernel, that is, for any P , 
Φ(P ) = ⊗ 
(s,a)∈S×A 
Pρ(s, a;P ), where Pρ(s, a;P ) = { P̃ (·) ∈ ∆(S) : DTV 
( P̃ (·) 
∥∥P (·|s, a)) ≤ ρ } , (3.1) 
where ρ ∈ [0, q] is the parameter characterizing the size of the robust set. We set s1 = sgood. 
For this class of RMDPs, we have the following hardness result for doing robust RL with interactive data collection, an Ω(ρ ·K)-online regret lower bound. 
Theorem 3.2 (Hardness result (based on Example 3.1)). There exist two RMDPs {M0,M1} such that the following regret lower bound holds: 
inf ALG 
sup θ∈{0,1} 
E [ RegretMθ,ALG 
Φ (K) ] ≥ Ω 
( ρ ·HK 
) , 
where RegretMθ,ALG Φ (K) refers to the online regret of algorithm ALG for RMDP Mθ. 
13
Proof of Theorem 3.2. We intuitively explain why robust RL with interactive data collection may fail in the Example 3.1 in this section. We refer the readers to a rigorous proof of Theorem 3.2 in Appendix B.1. 
The reason why any algorithm fails for this class of RMDPs is the support shift of the worst-case transition kernel. In robust RL, the performance of a policy π is evaluated via the robust expected total rewards, or equivalently, the expected return under the most adversarial transition kernel P †,π. In this example, as we explicitly show in the proof, when in the good state sgood, the worst-case transition kernel P †,π would transit the state to sbad with a constant probability ρ. But the state sbad is out of the scope of the data collection process because starting from s1 = sgood the nominal transition kernel always transits the state to sgood. As a result, the performance of the learned policy at the bad state sbad is not guaranteed, and inevitably incurs an Ω(ρ · K)-lower bound of regret, a hardness result. Furthermore, by strategically constructing RMDPs with the horizon 3H based on Example 3.1, we can derive a lower bound of Ω(ρ ·HK). 
In contrast, doing robust RL with a generative model or an offline dataset with good coverage properties does not face such difficulty. It turns out that any RMDP with S ×A-rectangular total-variation robust set (including Example 3.1) can be solved in a sample-efficient manner therein, see Yang et al. (2022); Panaganti and Kalathil (2022); Panaganti et al. (2022); Xu et al. (2023); Blanchet et al. (2023); Shi et al. (2023) and Remark 2.6. The intuitive reason is that, for the generative model setting, the learner can directly query any state-action pair to estimate the nominal transition kernel P ⋆, and thus no support shift problem happens. The same reason holds for the offline setup with a good-coverage dataset. 
There is a broader understanding of the curse of support shift that hinders the tractability of robust RL via interactive data collection. The concept of support shift can be comprehended within a broader context beyond the disjointness of certain parts of the support sets of the training and testing environments. Instead, ensuring a “high probability of disjointness” is enough to maintain the integrity of the hardness result. For instance, we can modify the state sgood in Example 3.1 so that it is no longer an absorbing state. Rather, sgood could transit to sbad with a small probability, such as 2−H . This modification expands the support of the training environment to encompass the entire state space. Nevertheless, acquiring information about sbad necessitates exponential samples, thereby preserving the hardness result. 
In the next section of this paper, we aim to figure out that for specific types of RMDPs, e.g., the RMDP with total-variation robust set as in Example 3.1, under what kind of structural assumptions can we perform sample-efficient robust RL with interactive data collection. 
4 A Solvable Case, Efficient Algorithm, and Sharp Analysis 
Motivated by the hard instance (Example 3.1) in the previous section, in this section, we consider a special subclass of RMDP with S ×A-rectangular total variation robust set that we show allows for sample-efficient robust RL through interactive data collection. In Section 4.1, we introduce the assumption we impose on the RMDP we consider. We propose our algorithm design in Section 4.2, with theoretical analysis in Section 4.3. Throughout this section, our choice of the mapping Φ is always given by (3.1). 
4.1 Vanishing Minimal Value: Eliminating Support Shift 
To overcome the difficulty of support shift identified in Section 3, we make the following vanishing minimal value assumption on the underlying RMDP. 
Assumption 4.1 (Vanishing minimal value). We assume that the underlying RMDP satisfies that 
min s∈S 
V ⋆ 1,P⋆,Φ(s) = 0. 
Also, without loss of generality, we assume that the initial state s1 /∈ argmins∈S V ⋆ 1,P⋆,Φ(s). 
Assumption 4.1 imposes that the minimal robust expected total rewards over all possible initial states is 0. Assuming that the initial state s1 /∈ argmins∈S V 
⋆ 1,P⋆,Φ(s) avoids making the problem trivial. A close look 
at Assumption 4.1 actually gives that the minimal robust value function of any policy π at any step is zero, that is, mins∈S V 
π h,P⋆,Φ(s) = 0 for any policy π and any step h ∈ [H]. With this observation, the following 
proposition explains why such an assumption can help to overcome the difficulty. 
14
Proposition 4.2 (Equivalent expression of TV robust set with vanishing minimal value). For any function V : S 7→ [0, H] with mins∈S V (s) = 0, we have that 
EPρ(s,a;P⋆ h ) [V ] = ρ′ · EBρ′ (s,a;P 
⋆ h )[V ], where ρ′ = 1− ρ ∈ (0, 1], 
where the total-variation robust set Pρ(s, a;P ⋆ h ) is defined in (3.1) and the set Bρ′(s, a;P ⋆ 
h ) is defined as5 
Bρ′(s, a;P ⋆ h ) = 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} . 
Proof of Proposition 4.2. Please refer to Appendix A.3 for a detailed proof of Proposition 4.2. 
As Proposition 4.2 indicates, under Assumption 4.1, the robust Bellman equations (Propositions 2.2 and 2.3) at step h ∈ [H] are equivalent to taking an infimum over another robust set Bρ′(s, a;P ⋆ 
h ) that shares the same support as the nominal transition kernel P ⋆(·|s, a), discounted by a constant ρ′ ≤ 1. Intuitively, this new robust set rules out the difficulty originated in unseen states in training environments and the discount factor ρ′ hedges the difficulty from prohibitively small probability of reaching certain states that may appear often in the testing environments. This renders robust RL with interactive data collection possible. 
To understand this from another perspective, it could be shown that under the conclusions of Proposi-tion 4.2, the robust value functions of any policy π are equivalent to the robust value functions of this policy under another discounted RMDP (S,A,H, P ⋆, R′,Φ′) with R′ 
h(s, a) = (ρ′)h−1Rh(s, a) and Φ′ given by 
Φ′(P ) = ⊗ 
(s,a)∈S×A 
Bρ′(s, a;P ). (4.1) 
And therefore we are equivalently considering this new type of RMDPs. Please refer to Section 5 for more discussions on the connections between the two types of RMDPs. 
Examples of Assumption 4.1. In the sequel, we provide a concrete condition that makes Assumption 4.1 hold, which imposes that the state space of the RMDP has a “closed” subset of “fail-states” with zero rewards. 
Condition 4.3 (Fail-states). There exists a subset Sf ⊂ S of fail states such that 
Rh(s, a) = 0, P ⋆ h (Sf |s, a) = 1, ∀(s, a, h) ∈ Sf ×A× [H]. 
This type of “fail-states” condition is first proposed by Panaganti et al. (2022) (with |Sf | = 1) to handle the computational issues for robust offline RL under function approximations (out of the scope of our work). In contrast, here we make the vanishing minimal value assumption in order to tackle the support shift or extrapolation issue for the interactive data collection setup. The comparison between the vanishing minimal value assumption (Assumption 4.1) and the “fail-states” condition (Condition 4.3) is given below. 
Remark 4.4 (Comparison between Assumption 4.1 and Condition 4.3). We first observe that Condition 4.3 implies that mins∈S V 
π h,P⋆,Φ(s) = 0 for any policy π and step h ∈ [H], therefore satisfying the minimal value 
assumption (Assumption 4.1). Conversely, the vanishing minimal value assumption in Assumption 4.1 is strictly more general than the fail-state condition in Condition 4.3. To illustrate, one can consider an RMDP characterized by the state space S = {s1, s2}, action space A = {a1}, time horizon H = 2, reward function Rh(s, a) = 1{s = s2}, and transition probabilities defined as follows: 
P ⋆ 1 (s1|s1, a1) = 1− ρ, P ⋆ 
1 (s2|s1, a1) = ρ, P ⋆ 1 (s1|s2, a1) = 0, P ⋆ 
1 (s2|s2, a1) = 1, 
where ρ is the radius of the robust set. It is evident that no fail-state emerges within such an RMDP structure. However, this RMDP satisfies the vanishing minimal value assumption since V ⋆ 
1,P⋆,Φ(s1) = 0. 
Remark 4.5 (Reduction to non-robust MDP without loss of generality). It is noteworthy that assuming the vanishing minimal value (Assumption 4.1) or the presence of fail-states (Condition 4.3) in the non-robust case (ρ = 0) is without loss of generality. This is achievable by expanding the prior state space S of MDP 
5Here we implicitly define 0 0 = 0 and a 
0 = ∞ for any a > 0. 
15
Algorithm 1 OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV) 
1: Initialize: dataset D = ∅. 2: for episode k = 1, · · · ,K do 3: Training environment transition estimation: 
4: Update the count functions Nk h (s, a, s 
′) and Nk h (s, a) based on D according to (4.3). 
5: Calculate the transition kernel estimator P̂ k h according to (4.2). 
6: Optimistic robust planning: 
7: Set V k 
H+1 = V k H+1 = 0. 
8: for step h = H, · · · , 1 do 
9: Set Q k 
h(·, ·) and Q k 
h (·, ·) as (4.5) and (4.6), with the bonus function bonuskh(·, ·) defined in (4.8). 
10: Set πk h(·|·) = argmaxa∈A Q 
k 
h(·, a), V k 
h(·) = Eπk h(·|·) 
[Q k 
h(·, ·)], and V k h(·) = Eπk 
h(·|·) [Qk 
h (·, ·)]. 
11: end for 12: Execute the policy in training environment and collect data: 
13: Receive the initial state sk1 ∈ S. 14: for step h = 1, · · · , H do 15: Take action akh ∼ πk 
h(·|skh), observe reward Rh(s k h, a 
k h) and the next state skh+1. 
16: end for 17: Set D as D ∪ {(skh, akh, skh+1)}Hh=1. 18: end for 19: Output: Randomly (uniformly) return a policy from {πk}Kk=1. 
to include an additional state sf , denoted as the fail-state. More importantly, this augmentation does not alter the optimal value or the optimal value function of the original MDP. Consequently, it becomes sufficient to seek the optimal policy within the augmented MDP, which satisfies the conditions of vanishing minimal value (Assumption 4.1) or the existence of fail-states (Condition 4.3). This indicates that our algorithm and theoretical analysis in the sequel can be directly reduced to non-robust MDPs without additional assumptions. 
4.2 Algorithm Design: OPROVI-TV 
In this section, we propose our algorithm that solves robust RL with interactive data collection for RMDPs with S×A-rectangular total-variation (TV) robust sets (Assumption 2.1 and Definition 2.4) and satisfying the vanishing minimal value assumption (Assumption 4.1). Our algorithm, OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV, Algorithm 1), can automatically balance exploitation and exploration during the interactive data collecting process while managing the distributional robustness of the learned policy. 
In each episode k, the algorithm operates in three stages: (i) training environment transition estimation (Line 3 to 5); (ii) optimistic robust planning based on the training environment transition estimator (Line 6 to 11); and finally (iii) executing the policy in the training environment and collecting data (Line 12 to 18). In the following, we elaborate more on the first two parts of Algorithm 1. 
4.2.1 Training Environment Transition Estimation 
At the beginning of each episode k ∈ [K], we maintain an estimate of the transition kernel P ⋆ of the training 
environment by using the historical data D = {(sτh, aτh, sτh+1)} k−1,H τ=1,h=1 collected from the interaction with the 
training environment. Specifically, we simply adopt a vanilla empirical estimator, defined as 
P̂ k h (s 
′|s, a) = 
 Nk 
h (s, a, s ′) 
Nk h (s, a) 
, Nk h (s, a) > 0, 
1 
S , Nk 
h (s, a) = 0, 
∀(s, a, h, s′) ∈ S ×A× [H]× S, (4.2) 
16
where the count functions Nk h (s, a, s 
′) and Nk h (s, a) are calculated on the current dataset D by 
Nk h (s, a, s 
′) = 
k−1∑ τ=1 
1 { (sτh, a 
τ h, s 
τ h+1) = (s, a, s′) 
} , Nk 
h (s, a) = ∑ s′∈S 
Nk h (s, a, s 
′), (4.3) 
for any (s, a, h, s′) ∈ S ×A× [H]×S. This just coincides with the transition estimator adopted by existing non-robust online RL algorithms (Auer et al., 2008; Azar et al., 2017; Zhang et al., 2021). 
4.2.2 Optimistic Robust Planning 
Given P̂ k that estimates the training environment, we perform an optimistic robust planning to construct the policy πk to execute. Basically, the optimistic robust planning follows the robust Bellman optimal equation (Proposition 2.3) to approximate the optimal robust policy, but differs in that it maintains an upper bound and a lower bound of the optimal robust value function and chooses the policy that maximizes the optimistic estimate to incentivize exploration during data collection. Here the purpose of maintaining the lower bound estimate is to facilitate the construction of the variance-aware optimistic bonus (see following), which helps to sharpen our theoretical analysis. 
Simplifying the robust expectation. To better utilize the vanishing minimal value condition (Assump-tion 4.1), we take a closer look into the robust Bellman equation. Due to the strong duality (Proposition 2.5), the robust expectation EPρ(s,a;P )[V ] for any V ∈ [0, H] satisfying mins∈S V (s) = 0 is equivalent to 
EPρ(s,a;P ) 
[ V ] = sup 
η∈[0,H] 
{ − EP (·|s,a) 
[( η − V 
) + 
] − ρ · 
( η − min 
s′∈S V (s′) 
) + + η 
} = sup 
η∈[0,H] 
{ − EP (·|s,a) 
[( η − V 
) + 
] + (1− ρ) · η 
} . (4.4) 
Consequently, in the algorithmic recursions below, whenever the notation EPρ(s,a;P )[V ] is applied to an estimated value function, it is understood as the dual-form backup on the right hand side of (4.4). When mins∈S V (s) = 0, Proposition 2.5 implies that this dual-form backup coincides with the true TV robust expectation. Thus, under Assumption 4.1, the robust Bellman equations for the true robust value functions remain unchanged, while the same dual-form backup is used for the optimistic and pessimistic value estimates in the algorithm. 
Optimistic robust planning. With this in mind, the optimistic robust planning goes as follows. Starting 
from V k 
H+1 = V k H+1 = 0, we recursively define that 
Q k 
h(s, a) = min { Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a),min 
{ H, ρ−1 
}} , ∀(s, a) ∈ S ×A, (4.5) 
Qk 
h (s, a) = max 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − bonuskh(s, a), 0 
} , ∀(s, a) ∈ S ×A, (4.6) 
where EPρ(s,a;P̂k h ) is understood in the dual-form sense specified above, and the bonus function bonuskh(s, a) ≥ 
0 is defined later. Here we truncate the optimistic estimate Q k 
h via the upper bound min{H, ρ−1} of the true optimal robust value function Q⋆ 
h,P⋆,Φ. This truncation arises from the combined implication of Propo-sition 2.7 and the fact that min(s,a)∈S×AQ 
⋆ h,P⋆,Φ(s, a) = 0 under Assumption 4.1. 
As we establish in Lemma C.2, Q k 
h and Qk 
h form upper and lower bounds for Q⋆ 
h,P⋆,Φ and Qπk 
h,P⋆,Φ under 
a proper choice of the bonus. After performing (4.5) and (4.6), we choose the data collection policy πk h to 
be the optimal policy with respect to the optimistic estimator Q k 
h and define V k 
h and V k h accordingly by 
πk h(·|·) = argmax 
a∈A Q 
k 
h(·, a), V k 
h(s) = Eπk h(·|s) 
[ Q 
k 
h(s, ·) ] , V k 
h(s) = Eπk h(·|s) 
[ Qk 
h (s, ·) 
] . (4.7) 
We remark that the purpose of maintaining the lower bound estimate (4.6) is to facilitate the construction of the bonus and to help to sharpen our theoretical analysis. The construction of the policy πk is still based 
17
on the optimistic estimator, which is why we name it optimistic robust planning. As indicated by theory, the optimistic robust planning effectively guides the policy to explore uncertainty robust value function estimates, striking a balance between exploration and exploitation while managing distributional robustness. 
Bonus function. In Algorithm 1, the bonus function bonuskh(s, a) is a Bernstein-style bound defined as 
bonuskh(s, a) = 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K 
(4.8) 
where ι = log(S3AH2K3/2/δ), c1, c2 > 0 are absolute constants, and δ signifies a pre-selected fail probability. 
Under (4.8), Q k 
h and Qk 
h become upper and lower bounds of the optimal robust value functions (Lemma C.2). 
More importantly, the bonus (4.8) is carefully designed for robust value functions such that the summation of this bonus term (especially the leading variance term in (4.8)) over time steps is well controlled, for which we also develop new analysis methods. This is critical for obtaining a sharp sample complexity of Algorithm 1. 
4.3 Theoretical Guarantees 
This section establishes the online regret and the sample complexity of OPROVI-TV (Algorithm 1). Our main result is the following theorem, upper bounding the online regret of Algorithm 1. 
Theorem 4.6 (Online regret of OPROVI-TV). Given an RMDP with S×A-rectangular total-variation robust set of radius ρ ∈ [0, 1) (Assumption 2.1 and Definition 2.4) satisfying Assumptions 4.1, choosing the bonus function as (4.8) with sufficiently large c1, c2 > 0, then with probability at least 1− δ, Algorithm 1 satisfies 
RegretΦ(K) ≤ O (√ 
min { H, ρ−1 
} H2SAKι′ 
) , 
where ι′ = log2(SAHK/δ) and O(·) hides absolute constants and lower order terms in K. 
Proof of Theorem 4.6. See Appendix C for a detailed proof of Theorem 4.6. 
Theorem 4.6 shows that Algorithm 1 enjoys a sublinear online regret of Õ( √ K), meaning that it is able 
to approximately find the optimal robust policy through interactive data collection. This is in contrast with the general hardness result in Section 3 where sample-efficient learning is impossible in the worst case. Thus we show the effectiveness of the minimal value assumption for robust RL with interactive data collection. 
As a corollary, we have the following sample complexity bound for Algorithm 1. 
Corollary 4.7 (Sample complexity of OPROVI-TV). Under the same setup and conditions as in Theorem 4.6, with probability at least 1− δ, Algorithm 1 can output an ε-optimal policy within 
O 
( min 
{ H, ρ−1 
} H2SAι′′ 
ε2 
) (4.9) 
episodes, where ι′′ = log(SAH/εδ) and O(·) hides absolute constants. Here the valid range of ε is given by ε ∈ (0, c ·min{1, 1/(ρH)}] for some constant c > 0. 
Proof of Corollary 4.7. This follows from Theorem 4.6 and a standard online to batch conversion. 
This further shows that Algorithm 1 is able to find ε-optimal robust policy within polynomial interactive samples in H, S, A, and ε−1. We note that as the radius ρ of the TV robust set increases, the sample needed to be ε-optimal decreases. When ρ tends to 1, the sample complexity reduces to nearly Õ(H2SA/ε2). Thus, we observe that robust RL through interactive data collection for this RMDP example is statistically easier when the radius ρ increases, which matches the conclusion in the generative model setup (Yang et al., 2022; Shi et al., 2023) as well as the offline learning setup (Panaganti et al., 2022). 
18
Finally, we compare the sample complexity (4.9) with prior arts on non-robust online RL and robust RL with a generative model. On the one hand, (4.9) with ρ = 0 equals to 
Õ ( H3SA 
ε2 
) , 
which matches the minimax sample complexity lower bound for online RL in non-robust MDPs (Azar et al., 2017). This means that our algorithm design can naturally handle non-robust MDPs as a special case (please also see Remark 4.5 for why one can reduce Algorithm 1 to general non-robust MDPs under Assumption 4.1). On the other hand, the previous work of Shi et al. (2023) for robust RL in infinite horizon RMDPs with a TV robust set and a generative model showcases a minimax optimal sample complexity of 
Õ 
( min 
{ Hγ , ρ 
−1 } H2 
γSA 
ε2 
) , 
for ρ ∈ [0, 1), where we define Hγ := 1/(1− γ) as the effective horizon of the infinite γ-discounted RMDPs. As a result, the sample complexity (4.9) of Algorithm 1 matches their result. We highlight that our algorithm does not rely on a generative model and operates purely through interactive data collection. 
5 Extension I: Robust Set with Bounded Transition Probability Ratio 
In this section, we show that our algorithm design (Algorithm 1) can also be applied to S × A-rectangular discounted RMDPs with robust sets given by (4.1) (i.e., bounded ratio between training and testing transition probabilities). We establish that our main theoretical result in Section 4.3 can imply a sublinear regret upper bound for this model, which means that this type of RMDPs can also be solved sample-efficiently through the auxiliary construction based on Algorithm 1. This coincides with our intuition on support shift in Section 4.1. 
S ×A-rectangular discounted RMDPs with robust set (4.1). We first define the model formally. A finite-horizon discounted RMDP is specified by Mγ = (S,A, H, P ⋆, Rγ ,Φ 
′), where the robust set Φ′ is given by (4.1), i.e., 
Φ′(P ) = ⊗ 
(s,a)∈S×A 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P (s′|s, a) ≤ 1 
ρ′ 
} := 
⊗ (s,a)∈S×A 
Bρ′(s, a;P ). (5.1) 
This robust set contains transition probabilities that share the same support as the nominal transition kernel. The reward function Rγ = {γh−1 ·Rh}Hh=1, where γ ∈ (0, 1) is the discount factor and Rh ∈ [0, 1] is the true reward at step h. That is, the robust value function is now the worst case expected discounted total reward. 
Algorithm and regret bound. Now we theoretically show that we can apply Algorithm 1 to solve robust RL in S ×A-rectangular discounted RMDPs with robust set (5.1) via interactive data collection. 
As motivated by the discussions under Proposition 4.2, we define an auxiliary finite-horizon TV-RMDP M̃ as M̃ = (S̃,A,H, P̃ ⋆, R̃, Φ̃) which includes an additional “fail-state” sf . More specifically, the state 
space S̃ = S ∪ {sf}. The transition kernel P̃ ⋆ is defined as, for any step h ∈ [H], 
P̃ ⋆ h (·|s, a) = P ⋆ 
h (·|s, a), ∀(s, a) ∈ S ×A and P̃ ⋆ h (·|sf , a) = δsf (·), ∀a ∈ A. (5.2) 
The reward function R̃ is defined as, for any step h ∈ [H], 
R̃h(s, a) = 
( γ 
ρ′ 
)h−1 
·Rh(s, a), ∀(s, a) ∈ S ×A and R̃h(sf , a) = 0, ∀a ∈ A. 
19
We suppose that the discount factor γ ≤ ρ′ so that the reward function R̃h ∈ [0, 1]. The robust mapping Φ̃ 
is defined as, for any P : S̃ × A 7→ ∆(S̃), 
Φ̃(P ) = ⊗ 
(s,a)∈S̃×A 
{ P̃ (·) ∈ ∆(S̃) : DTV 
( P̃ (·) 
∥∥P (·|s, a)) ≤ ρ } := 
⊗ (s,a)∈S̃×A 
P̃ρ(s, a;P ), ρ = 1− ρ′. 
Therefore, M̃ is an RMDP with S̃ ×A-rectangular TV robust set of radius ρ and satisfying Assumption 4.1 (because it satisfies the “fail-state” Condition 4.3). Furthermore, for any initial state s1 ∈ S̃ \ {sf} = S, the interaction with the transition kernel P̃ ⋆ is equivalent to the interaction with the transition kernel P ⋆ of the original RMDP Mγ , since by the definition (5.2), starting from any s ̸= sf the agent would follow the same 
dynamics as P ⋆. What’s more, for any policy π̃h : S̃ 7→ ∆(A) for M̃, it naturally induces the unique policy π̃S,h : S 7→ ∆(A) for the original RMDP Mγ . 
Therefore, we can run Algorithm 1 on the auxiliary RMDP M̃, starting from the initial state s1 ∈ S̃\{sf}, which only needs the interaction with P ⋆. Suppose the output policy by the algorithm is {π̃k}Kk=1, then the following corollary shows the induced policy {π̃k 
S}Kk=1 for the original RMDP Mγ enjoys a sublinear regret. 
Corollary 5.1 (Online regret of Algorithm 1 for discounted RMDPs with robust sets (5.1)). Consider an S × A-rectangular γ-discounted RMDP with robust set (5.1) satisfying 0 ≤ γ ≤ ρ′ ∈ (0, 1]. There exists an algorithm ALG (specified by the above discussion) such that its online regret for this RMDP is bounded by 
RegretALG Φ′ (K) ≤ O 
(√ min 
{ H, (1− ρ′)−1 
} H2SAKι′ 
) , 
where ι′ = log2(SAHK/δ) and (1−ρ′)−1 is interpreted as +∞ when ρ′ = 1 and O(·) hides absolute constants and lower order terms in K. 
Proof of Corollary 5.1. See Appendix D.1 for a detailed proof of Corollary 5.1. 
Corollary 5.1 shows that besides S × A-rectangular RMDPs with TV robust set and vanishing minimal value assumption, the S×A-rectangular discounted RMDP with robust set of bounded transition probability ratio (5.1) can also be solved sample-efficiently by robust RL via interactive data collection. This also echoes our intuition on the support shift issue in Section 4.1. Furthermore, the regret decays as ρ′ decays in which case the transition probability ratio bound becomes higher, i.e., the robust set becomes larger. 
Remark 5.2. The upper bound in Corollary 5.1 does not depend on the discount factor γ since Algorithm 1 adopts a coarse bound of R̃h ≤ 1. The upper bound can be directly improved to be γ-dependent using a tighter truncation in step (4.5) of Algorithm 1. 
6 Extension II: Robust Decision Making in Multi-Agent Systems 
Many operations research problems involve strategic interaction among opponents, e.g., competition, security, and markets, and the underlying model may shift between training and deployment environments. This section extends our distributionally robust RL framework from single-agent RMDPs to multi-agent robust Markov games. 
6.1 Learning against an Adversarial Opponent under Environment Ambiguity 
Consider a sequential decision-making problem where a learning agent (Player 1) competes against an adversarial opponent (Player 2) while simultaneously facing ambiguity in the underlying environment dynamics. This is motivated by a wide range of operations research applications—including robust operations planning, security games, and competitive resource allocation—where a decision-maker must account for both strategic behavior of other agents and the uncertainty stemming from exogenous factors such as demand volatility, model misspecification, or incomplete system knowledge. 
Existing formulations of multi-agent reinforcement learning (MARL) and Markov games (MG) typically presume a known or stationary environment and thus fail to capture robustness requirements against model 
20
uncertainty. In contrast, our formulation explicitly integrates the adversarial interaction and the environment ambiguity within a unified robust Markov game (RMG). This integration enables the study of policies that are resilient to worst-case opponent strategies as well as worst-case perturbations of the transition dynamics, thereby providing a principled benchmark for robustness, stability, and performance guarantees in complex and uncertain multi-agent operational systems. 
Robust Markov game. Specifically, we consider a two-player robust Markov game (S,A,B,H, P ⋆, R,Φ), where S is the state space, A and B are the action spaces of Player 1 and Player 2, respectively, H denotes the horizon, and Rh : S×A×B → [0, 1] denotes the stage-h reward. Player 1 wants to maximize its expected reward, while Player 2 wants to minimize it. The training environment is governed by the transition kernel P ⋆ h (·|s, a, b), which is unknown to the learner but accessible through online interaction, as in the single-agent 
setup. The robust set mapping is denoted by Φ. Following the single-agent setup, we assume the following. 
Assumption 6.1 (S ×A×B-rectangularity and TV robust set). We assume that, for any transition kernel P ∈ P, the robust set Φ(P ) takes the form 
Φ(P ) = ⊗ 
(s,a,b)∈S×A×B 
Pρ(s, a, b;P ), 
where Pρ(s, a, b;P ) is the TV-robust set for the transition kernel P (·|s, a, b), defined as 
Pρ(s, a, b;P ) := { P̃ (·) ∈ ∆(S) : DTV 
( P̃ (·) 
∥∥P (·|s, a, b)) ≤ ρ } . 
When Player 2 has a singleton action set B = {b0}, Φ reduces to the S × A-rectangular TV-robust set of the RMDP as defined in Section 2.1. Moreover, when ρ = 0, each ambiguity set collapses to the nominal transition kernel, and the model reduces to the standard zero-sum Markov game (Shapley, 1953; Littman, 1994). 
Robust Nash value and Bellman-Shapley recursion. For any Markovian policy pair (π, ν) with π = {πh : S → ∆(A)}Hh=1 and ν = {νh : S → ∆(B)}Hh=1, we define the robust value function as 
V π,ν h,P⋆,Φ(s) := inf 
{P̃i∈Φ(P⋆ i )}H 
i=h 
E{P̃i}H i=h,π,ν 
[ H∑ i=h 
Ri(si, ai, bi) 
∣∣∣∣∣ sh = s 
] , 
Qπ,ν h,P⋆,Φ(s, a, b) := inf 
{P̃i∈Φ(P⋆ i )}H 
i=h 
E{P̃i}H i=h,π,ν 
[ H∑ i=h 
Ri(si, ai, bi) 
∣∣∣∣∣ sh = s, ah = a, bh = b 
] . 
Here the expectation is taken w.r.t. the state-action trajectories induced by the policies π and ν under the transition P̃ = {P̃h}Hh=1. The associated robust Bellman recursion is given by 
Qπ,ν h,P⋆,Φ(s, a, b) = Rh(s, a, b) + EPρ(s,a,b;P⋆ 
h ) 
[ V π,ν h+1,P⋆,Φ 
] , V π,ν 
h,P⋆,Φ(s) = Eπh,νh 
[ Qπ,ν 
h,P⋆,Φ(s, ·, ·) ] , (6.1) 
where the worst-case expectation over the robust set Pρ corresponds to the worst-case transition within the TV ball (6.1). Now we define the robust Nash value (Zhang et al., 2020b; Blanchet et al., 2023), which serves as the natural performance benchmark under simultaneous adversarial opposition and environment ambiguity. The following proposition shows the existence of the robust Nash value and the strong duality property. 
Proposition 6.2 (Robust Bellman equation, minimax value, and Markov perfect robust saddle). Define V ⋆ H+1,P⋆,Φ(·) ≡ 0 and, for h = H,H − 1, . . . , 1, 
Q⋆ h,P⋆,Φ(s, a, b) := Rh(s, a, b) + EPρ(s,a,b;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] , 
V ⋆ h,P⋆,Φ(s) := max 
π∈∆(A) min 
ν∈∆(B) Ea∼π, b∼ν 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] . 
(6.2) 
Then the following holds: 
21
1. (Robust Nash equilibrium.) There exists a Markovian policy pair (π⋆, ν⋆) such that for all h ∈ [H] and s ∈ S, and any Markovian policy pair (π, ν), 
V π,ν⋆ 
h,P⋆,Φ(s) ≤ V π⋆,ν⋆ 
h,P⋆,Φ(s) ≤ V π⋆,ν h,P⋆,Φ(s), (6.3) 
and V π⋆,ν⋆ 
h,P⋆,Φ(s) = V ⋆ h,P⋆,Φ(s). Moreover, for each (h, s) ∈ [H]×S, (π⋆ 
h(·|s), ν⋆h(·|s)) is a Nash equilibrium of the one-shot zero-sum matrix game with payoff matrix Q⋆ 
h,P⋆,Φ(s, ·, ·). 
2. (Strong duality.) For every h ∈ [H] and s ∈ S, it holds that 
max π 
min ν 
V π,ν h,P⋆,Φ(s) = V ⋆ 
h,P⋆,Φ(s) = min ν 
max π 
V π,ν h,P⋆,Φ(s). (6.4) 
Proof of Proposition 6.2. See Appendix E.1 for a detailed proof. 
Learning objective. The learner interacts only with the training kernel P ⋆ for K episodes. At the beginning of episode k, Player 2 may choose a Markov policy νk based on the history before episode k. At step h, Player 1 samples akh ∼ πk 
h(·|skh), Player 2 samples bkh ∼ νkh(·|skh) without observing Player 1’s current sampled action, and the next state skh+1 is generated from P ⋆ 
h (·|skh, akh, bkh). Player 2’s actions are observable to the learner. 
For any adaptive Markov opponent sequence {νk}Kk=1 and any learner policy sequence {πk}Kk=1 executed during the interaction, we measure the performance of {πk}Kk=1 via the following definition of robust regret 
RegretΦ,{νk}K k=1 
(K) := 
K∑ k=1 
V ⋆ 1,P⋆,Φ(s1)− V πk,νk 
1,P⋆,Φ(s1). (6.5) 
Intuitively, it quantifies the cumulative regret of the learner (Player 1) relative to the robust Nash value. This benchmark is the robust analogue of the online regret notions used in non-robust zero-sum Markov games, e.g., Xie et al. (2020); Tian et al. (2020). The key point is that the learner controls only Player 1, while Player 2 may adapt its Markov policy to past episodes, so the comparator should be a value level that the learner could secure before seeing the opponent’s future policies. By Proposition 6.2, 
V ⋆ 1,P⋆,Φ(s1) = max 
π min ν V π,ν 1,P⋆,Φ(s1), 
namely, the robust Nash value is exactly the largest reward guarantee that Player 1 can secure simultaneously against the worst-case opponent policies and the worst-case transition kernels in the robust set. In particular, 
for the robust Nash policy π⋆, we have V π⋆,ν 1,P⋆,Φ(s1) ≥ V ⋆ 
1,P⋆,Φ(s1) for any ν. Thus the comparator is valid and is achievable by a fixed policy, instead of relying on hindsight knowledge of the realized opponent sequence. 
The term V πk,νk 
1,P⋆,Φ(s1) then evaluates the learner’s policy under the actual opponent policy νk faced in episode k, while still allowing nature to pick the worst-case transition kernel in Φ(P ⋆). Therefore, the regret in (6.5) characterizes the two aspects of our problem: strategic opposition from Player 2 and distributional ambiguity in the environment. This is consistent with regret notions in prior non-robust Markov games. Specifically, Xie et al. (2020) studies the online learning setting against an external opponent using a similar value benchmark, while Tian et al. (2020) explicitly advocates the minimax-value benchmark as a statistically meaningful weakening of the stronger best-policy-in-hindsight regret. 
Although the robust Nash value can be informally viewed as a maxPlayer 1 minPlayer 2 minenvironment problem, the last minimization over the environment should not be absorbed into the minimization of Player 2 so as to reduce the problem to a standard zero-sum Markov game. The key point is that the environment minimization is performed entrywise: for each fixed (s, a, b), the environment may choose a different worst-case kernel in Pρ(s, a, b;P 
⋆ h ). Therefore, if one tries to absorb the environment minimization into Player 2, the 
minimizing player would have to choose a transition perturbation that depends on Player 1’s action a. This is not the same as a standard zero-sum game, where Player 2 only chooses an action b without observing a. In this sense, absorbing the environment minimization into Player 2 changes the information structure of the game. At the same time, the environment is still restricted to the fixed rectangular ambiguity set, rather than choosing an arbitrary perturbation after observing Player 1’s action, and this restriction is what keeps the problem tractable in our setting. 
22
Remark 6.3 (Comparison with recent works on online robust Markov games). During the preparation of this work, we became aware of two recent works (Farhat et al., 2025; Zheng and Lin, 2025) on online learning in robust Markov games under a different performance criterion. Their regret is closer to the online counterpart of the robust Nash equilibrium gap (RNE gap) introduced by Blanchet et al. (2023): in each episode, it measures the gain that a player could obtain by unilaterally deviating to the robust best response against the current joint policy, and then accumulates this equilibrium-gap quantity over episodes. By contrast, our regret in (6.5) is tailored to learning against an external adversarial opponent: it compares the learner’s robust value under the realized opponent policy νk with the robust Nash value V ⋆ 
1,P⋆,Φ(s1). These two notions emphasize different objectives: their criterion is symmetric and equilibrium-gap based, requiring the centralized control of all agents, whereas ours is minimax-value based and directly evaluates the controlled learner’s performance against the realized opponent sequence. This distinction is why the analysis below targets the regret in (6.5) rather than the cumulative equilibrium-gap. 
6.2 Algorithm and Theory 
In this subsection, we propose a game-theoretic extension of OPROVI-TV for RMGs introduced in Section 6.1. As in the single-agent setting, the goal is to manage exploration as well as robust planning so that the learner can approach the robust Nash value purely through interactive data collection with the environment and the opponent. To make this possible, we impose the following vanishing minimal value assumption, which is the natural counterpart of the vanishing minimal value condition in Section 4.1. 
Assumption 6.4 (Vanishing minimal value for RMG). For every Markov policy pair (π, ν), 
min s∈S 
V π,ν 1,P⋆,Φ(s) = 0. 
Because rewards are nonnegative, this step-1 condition implies mins∈S V π,ν h,P⋆,Φ(s) = 0 for every Markov 
policy pair (π, ν) and every step h ∈ [H]. This follows by a Bellman-induction argument: at a zero-value state, all nonnegative Bellman terms must vanish, and compactness of the TV ball gives a zero-valued successor state. This condition is imposed so that the TV-dual representation used in our robust Bellman updates remains valid throughout the analysis. In contrast to the single-agent setting, Player 2 may adapt its Markov policy across episodes. Therefore, the analysis must apply not only to the robust Nash value, but also to the value functions induced by the learner’s policy together with any realized opponent policy. A simple sufficient condition is the existence of an absorbing zero-reward fail state sf such that Rh(sf , a, b) = 0 and P ⋆ 
h (sf | sf , a, b) = 1 for all h ∈ [H] and (a, b) ∈ A × B. Then every policy pair has value zero at sf , so Assumption 6.4 holds. 
Under Assumption 6.4, we now extend OPROVI-TV from the single-agent robust MDP setting to the twoplayer zero-sum robust Markov game given in Section 6.1. Compared to the single-agent case, the game extension differs in two respects: (i) we estimate the joint-action transition kernel P ⋆ 
h (·|s, a, b) from observed tuples (skh, a 
k h, b 
k h, s 
k h+1), where the opponent’s actions bkh are observable, and (ii) we replace the state-wise 
max backup in value iteration by an upper-only robust minimax backup, implemented by solving a matrix game at each state. In each episode k, the learner constructs an estimated nominal model P̂ k and computes an optimistic robust max–min plan by solving S independent matrix games per stage in the backward pass. 
Our algorithm OPROVI-TV-MG is a direct game-theoretic extension of the single-agent algorithm OPROVI-TV 
(Algorithm 1). At a high level, both algorithms share the same episodic “estimate–plan–execute” template. The game-specific modifications are: 
1. Joint-action model estimation: replace the empirical kernel P̂ k h (·|s, a) by the joint-action estimator 
P̂ k h (·|s, a, b) using the observed opponent actions bkh. 
2. Robust minimax planning: replace the state-wise greedy maximization in OPROVI-TV by a statewise zero-sum matrix game in each Bellman backup, i.e., replace maxa∈A with maxπ∈∆(A) minν∈∆(B) 
as suggested by the Bellman recursion (Proposition 6.2). Unlike the single-agent case, where optimistic and pessimistic recursions bracket the value of the same learner policy, a game value also depends on the opponent policy. The optimistic recursion remains useful because it upper bounds the robust Nash value via monotonicity of the max–min operator; see (E.6). In contrast, a max–min pessimistic update would minimize over an internally selected opponent distribution, while the episode is played against 
23
Algorithm 2 OPtimistic RObust Value Iteration for TV Robust Set (OPROVI-TV-MG) 
1: Initialize: dataset D = ∅. 2: for episode k = 1, · · · ,K do 3: Training environment transition estimation: 
4: Set Nk h (s, a, b, s 
′) := ∑k−1 
τ=1 1 { (sτh, a 
τ h, b 
τ h, s 
τ h+1) = (s, a, b, s′) 
} ; Nk 
h (s, a, b) := ∑ 
s′∈S N k h (s, a, b, s 
′). 
5: Calculate P̂ k h by setting P̂ k 
h (s ′|s, a, b) = Nk 
h (s, a, b, s ′)/Nk 
h (s, a, b) if Nk h (s, a, b) > 0, and setting 
P̂ k h (·|s, a, b) to the uniform distribution over S otherwise. 
6: Optimistic robust planning: 
7: Set V k 
H+1 = 0. 8: for step h = H, · · · , 1 do 
9: Set Q k 
h(·, ·, ·) as (6.7), with the bonus function bonuskh(·, ·, ·) defined in (6.6). 
10: Compute πk h(·|s) ∈ argmaxπ∈∆(A) minν∈∆(B) Ea∼π,b∼ν 
[ Q 
k 
h(s, a, b) ] and a best response ν̃kh(·|s) ∈ 
argminν∈∆(B) Ea∼πk h(·|s),b∼ν 
[ Q 
k 
h(s, a, b) ] . 
11: Set V k 
h(s) = Ea∼πk h(·|s),b∼ν̃k 
h(·|s) [Q 
k 
h(s, a, b)]. 12: end for 13: Execute the policy in training environment and collect data: 
14: Receive the fixed initial state sk1 = s1 ∈ S. 15: for step h = 1, · · · , H do 16: Player 1 takes action akh ∼ πk 
h(·|skh); Player 2 takes action bkh ∼ νkh(·|skh). 17: Observe reward Rh(s 
k h, a 
k h, b 
k h) and the next state skh+1 ∼ P ⋆ 
h (·|skh, akh, bkh). 18: end for 19: Set D as D ∪ {(skh, akh, bkh, skh+1)}Hh=1. 20: end for 
the external policy νk, which may adapt across episodes. We therefore specify the optimistic robust minimax backup below. 
Optimistic robust minimax planning. Given the estimated nominal model P̂ k h (·|s, a, b), we use the 
following bonus, 
bonuskh(s, a, b) = cb ·min{H, ρ−1} · 
√ Sι 
Nk h (s, a, b) ∨ 1 
, (6.6) 
where cb > 0 is a sufficiently large absolute constant and ι = log(SABHK/δ). We use a TV-dual convention analogous to (4.4), with η restricted to [0,min{H, ρ−1}], which is without loss for the clipped value functions used below. For any transition kernel P , tuple (s, a, b), and V : S → [0,min{H, ρ−1}], set 
EPρ(s,a,b;P )[V ] := sup η∈[0,min{H,ρ−1}] 
{ − EP (·|s,a,b)[(η − V )+] + (1− ρ)η 
} . 
Under Assumption 6.4, this notation agrees with the true TV-robust Bellman term whenever V is V ⋆ or a realized value function. With this convention, the optimistic Q-estimate is 
Q k 
h(s, a, b) = min { Rh(s, a, b) + EPρ(s,a,b;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a, b),min 
{ H, ρ−1 
}} . (6.7) 
The policy update is the state-wise matrix-game step in Algorithm 2: for each s, solve the zero-sum game 
with payoff matrix Q k 
h(s, ·, ·) to obtain πk h, the planning best response ν̃kh , and the value V 
k 
h. For finite action spaces, this matrix game reduces to a standard linear program. 
Theoretical Results. We now state our results on the regret (6.5) for OPROVI-TV-MG. 
Theorem 6.5 (Online regret (6.5) of OPROVI-TV-MG). Consider an RMG with S × A × B-rectangular TV robust set of radius ρ ∈ [0, 1) (Assumption 6.1) satisfying Assumption 6.4. Fix any adaptive Markov opponent 
24
sequence ν = {νk}Kk=1 that is non-anticipating with respect to Player 1’s current action, and use the bonus function in (6.6). Then, with probability at least 1−δ, the online robust regret of OPROVI-TV-MG (Algorithm 2) is bounded by 
RegretΦ,{νk}K k=1 
(K) ≤ Õ ( min 
{ H, ρ−1 
} ·HS 
√ ABK 
) . 
Here Õ hides absolute constants and logarithmic factors in (S,A,B,H,K, 1/δ) and lower order terms in K. 
Proof of Theorem 6.5. See Appendix E.2 for a detailed proof. 
Theorem 6.5 gives sublinear online robust regret against any non-anticipating adaptive Markov opponent sequence. The rate is weaker than the single-agent bound because the regret is measured along the opponent sequence that is actually realized. Such a sequence may adapt to past data and need not coincide with the worst response used in the max–min planning problem. Thus a state-wise pessimistic max–min recursion would not give the trajectory-wise optimistic–pessimistic width used in the single-agent Bernstein argument. Accordingly, OPROVI-TV-MG uses only the optimistic recursion and controls the robust Bellman error through a uniform L1 transition-estimation bound. The price is the extra factor coming from this uniform concentration step, rather than from a variance-sensitive width recursion. 
7 Application: Data-Driven Robust Inventory Control 
Inventory control is a canonical operations research problem where a decision maker repeatedly trades off ordering costs against service and shortage risks under stochastic demand. In modern practice, data-driven inventory policies are often trained or tuned in a training environment (e.g., a model calibrated from historical data) and then deployed under demand shifts and model misspecification. This motivates a distributionally robust formulation: seeking inventory policy that performs well under worst-case perturbations of the demand law around the training environment. In this section, we present that a standard periodic-review inventory model can be written as a finite-horizon MDP; therefore, our robust RL framework and guarantees apply. 
7.1 Inventory Control as a Finite-horizon MDP 
We consider a single-item, periodic-review inventory system over a planning horizon of length H. The system state xh represents the inventory level. State xh is possibly negative, representing backlog at period h ∈ [H]. At each period h, the decision maker chooses an order quantity qh, observes a stochastic demand realization Dh, incurs a cost, and transits to the next inventory level xh+1. We formulate this problem as a finite-horizon tabular MDP (Sinv,Ainv, H, P 
⋆, R), whose components are defined as follows. 
1. State and action spaces. We adopt standard capacity and service-level truncations, 
Sinv := {−B,−B + 1, · · · , I} ∪ {sf}, Ainv := {0, 1, · · · , Q}. 
Here I ∈ N+ is the inventory capacity, Q ∈ N+ is the order capacity, and B ∈ N+ is the backlog threshold. We introduce sf as an aggregated fail-state representing all inventory positions below −B, namely exceptional operating regimes that are not modeled explicitly in the truncated state space. These truncations are common in practice when inventory or backlog is constrained by storage limits, service-level requirements, or contractual considerations. 
2. Nominal transition kernel induced by demand. Given an inventory state xh ∈ {−B, . . . , I} and an order quantity qh, the post-order inventory is x′h := min{xh + qh, I}. Let the (truncated) demand support be D := {0, 1, . . . , D}, and let Dh ∈ D denote the demand realized in the period h. Then the pre-truncation next inventory state is xpreh+1 := x′h −Dh. We then apply a service truncation, 
xh+1 = Th(xh, qh, Dh) := 
{ xpreh+1, if xpreh+1 ≥ −B, sf , if xpreh+1 < −B. 
We make sf absorbing in the truncated MDP: once the backlog threshold is violated, the subsequent dynamics over the remaining horizon are no longer modeled explicitly and are instead aggregated 
25
into this sink state. Thus the model does not distinguish among different post-violation paths after the system enters this exceptional operating regime. For any (q,Dh) ∈ Ainv × D, we therefore set Th(sf , q,Dh) = sf . If the conditional demand law is d⋆h(·|x, q) ∈ ∆(D) for each (h, x, q), then the induced transition kernel is the pushforward, 
P ⋆ h (·|x, q) = d⋆h(·|x, q) ◦ Th(x, q, ·)−1. 
3. Reward function induced by a cost transformation. Let the one-period cost at step h be 
ch(xh, qh, Dh) := corder · 1{qh > 0}+ chold · (xpreh+1) + + cback · (−xpreh+1) 
+, 
where corder > 0 is a fixed ordering/setup cost, chold > 0 is a holding cost coefficient, and cback > 0 is a backlog cost coefficient. When xh+1 ̸= sf , we have xh+1 = xpreh+1, so the cost can be written exactly as a deterministic transition-cost function of (xh, qh, xh+1): 
ch(xh, qh, xh+1) := corder · 1{qh > 0}+ chold · (xh+1)+ + cback · (−xh+1)+, for xh+1 ̸= sf . 
For the transition xh+1 = sf , which represents the event of xpreh+1 < −B, the exact overflow magnitude and the subsequent post-violation dynamics are no longer tracked in the truncated model. To keep the finite MDP well defined without introducing additional parameters, we assign the maximal cost cmax 
to this aggregated fail-state, which serves as a conservative reduced-form representation of leaving the normal operating regime. We define ch(xh, qh, sf ) := cmax for all (xh, qh), where a valid uniform cost upper bound cmax is 
cmax := corder + chold · I + cback · (D +B). 
Finally, to align with the reward-maximization convention in our framework, we define the reward 
Rh(xh, qh, xh+1) := 1− ch(xh, qh, xh+1) 
cmax ∈ [0, 1]. 
In particular, Rh(·, ·, sf ) = 0, and since sf is absorbing, the inventory MDP satisfies the vanishing minimal value condition. Also, we assume that x1 ̸= sf . Thus one can show that Assumption 4.1 holds. 
7.2 Distributional Robustness via an S ×A-rectangular TV Uncertainty Set 
In inventory control, we consider the distribution shift induced by the demand distribution. Specifically, we model demand shift given inventory state x and order quantity q by a TV robust set, 
UD h,ρ(x, q) := 
{ d̃h(·|x, q) ∈ ∆(D) : DTV 
( d̃h(·|x, q) 
∥∥d⋆h(·|x, q)) ≤ ρ } . 
Each d̃h(·|x, q) ∈ UD h,ρ(x, q) induces a transition kernel 
P̃h(·|x, q) = d̃h(·|x, q) ◦ Th(x, q, ·)−1. 
Hence, the induced transition robust set is 
UP h,ρ(x, q) = 
{ P̃h(·|x, q) = d̃h(·|x, q) ◦ Th(x, q, ·)−1 : d̃h(·|x, q) ∈ UD 
h,ρ(x, q) } . 
We also define the TV ball around the nominal transition kernel as follows, 
Pρ(x, q;P ⋆ h ) := 
{ P̃h(·|x, q) : DTV 
( P̃h(·|x, q) 
∥∥P ⋆ h (·|x, q) 
) ≤ ρ } . 
Lemma 7.1. For any (h, x, q) ∈ [H]× Sinv ×Ainv, it holds that UP h,ρ(x, q) ⊆ Pρ(x, q;P 
⋆ h ). 
Proof of Lemma 7.1. This follows directly from the data-processing inequality for TV distance under measurable maps: for any distributions µ, ν on D and any measurable g, 
DTV 
( µ ◦ g−1 
∥∥ν ◦ g−1 ) ≤ DTV(µ∥ν). 
Applying it with g(d) = Th(x, q, d) proves Lemma 7.1. 
26
Next, we explain why we only model transition ambiguity, and not reward ambiguity. Under any demand law d̃h(·|x, q), the induced next-state transition is P̃h(·|x, q) = d̃h(·|x, q) ◦ Th(x, q, ·)−1. Because the one-step reward is a deterministic function of the realized next state, namely Rh(x, q, x 
′) with x′ = Th(x, q,Dh), the 
conditional law of the reward given (x, q) is fully determined by P̃h(·|x, q). Therefore, demand perturbations do not introduce independent degrees of freedom in the reward: all reward variability is characterized by the next-state distribution. Meanwhile, for any bounded Vh+1 : Sinv → R and (x, q) ∈ Sinv ×Ainv, we have, 
inf d̃h∈UD 
h,ρ(x,q) E Dh∼d̃h(·|x,q) x′=Th(x,q,Dh) 
[Rh(x, q, x ′) + Vh+1(x 
′)] = inf P̃h∈UP 
h,ρ(x,q) Ex′∼P̃h(·|x,q)[Rh(x, q, x 
′) + Vh+1(x ′)] ; 
and due to Lemma 7.1, we have UP h,ρ(x, q) ⊆ Pρ(x, q;P 
⋆ h ). Therefore, it suffices (and is conservative) to work 
with the S×A-rectangular TV ball Pρ(·, ·;P ⋆ h ) at the transition level, without introducing a separate reward 
ambiguity set. Returning to our framework of RMDPs in Section 2.1, the corresponding S×A-rectangular TV robust-set 
mapping is defined by 
Φinv(P ⋆ h ) = 
⊗ (x,q)∈Sinv×Ainv 
Pρ(x, q;P ⋆ h ). 
Thus we define the corresponding RMDP for inventory control as Minv = (Sinv,Ainv, H, P ⋆, R,Φinv), where 
R = {Rh(x, q, x ′)}h∈[H] is a known transition-dependent reward. 
Our robust inventory control objective. A Markovian inventory policy π = {πh}Hh=1 with πh : Sinv 7→ ∆(Ainv) induces the robust value function 
V π h,P⋆,Φinv 
(x) = inf P̃h∈Φinv(P⋆ 
h ),1≤h≤H EP̃ ,π 
[ H∑ i=h 
Ri(xi, qi, xi+1) 
∣∣∣∣∣xh = x 
] , ∀x ∈ Sinv. 
Under rectangularity, the corresponding robust Bellman recursion uses the same TV ambiguity set, with the known one-period reward kept inside the robust expectation: 
Qπ h,P⋆,Φinv 
(x, q) = inf P̃h∈Pρ(x,q;P⋆ 
h ) Ex′∼P̃h(·|x,q) 
[ Rh(x, q, x 
′) + V π h+1,P⋆,Φinv 
(x′) ] . 
The optimal robust inventory policy π⋆ = {π⋆ h}Hh=1 is 
π⋆ ∈ argmax π 
V π 1,P⋆,Φinv 
(x1). 
Let V ⋆ 1,P⋆,Φinv 
:= V π⋆ 
1,P⋆,Φinv be the optimal robust value function. By construction, V ⋆ 
1,P⋆,Φinv (sf ) = 0, so the 
vanishing minimal value condition (Assumption 4.1) holds. 
Interactive learning protocol and regret objective. We adopt the interactive data-collection protocol in Section 2.1. Across episodes k = 1, . . . ,K, the learner interacts only with the training inventory transition P ⋆. In episode k, it executes a policy πk, observes realized rewards and state transitions, updates its estimate of P ⋆, and proceeds to the next episode. The performance criterion is the online regret 
RegretΦinv (K) := 
K∑ k=1 
V ⋆ 1,P⋆,Φinv 
(x1)− V πk 
1,P⋆,Φinv (x1). 
The goal is to design an algorithm that achieves sublinear regret in K (or equivalently, via an online-to-batch conversion, to output an ε-optimal robust inventory policy). 
7.3 Theoretical Guarantee for Robust Inventory Learning 
Since Minv is a finite-horizon RMDP with S ×A-rectangular TV robust set (Assumption 2.1), the vanishing minimal value condition (Assumption 4.1) also holds. The transition-dependent reward only changes the one-step planning operator: in OPROVI-TV (Algorithm 1), the robust expectation of Vh+1 is replaced by the 
27
robust expectation of the known bounded function Rh(x, q, ·) + Vh+1(·). No additional reward parameter is learned. Moreover, in the true robust recursion, Rh(x, q, sf )+Vh+1(sf ) = 0 because sf is absorbing and has zero reward, so the TV-duality simplification under Assumption 4.1 continues to apply. Hence the regret bound (Theorem 4.6) and sample complexity guarantee (Corollary 4.7) carry over with the same order. 
Theorem 7.2 (Sample-efficient robust learning for inventory control). Let Minv be the inventory RMDP with TV radius ρ ∈ [0, 1). Then, with probability at least 1−δ, OPROVI-TV with the transition-reward Bellman update above achieves 
RegretΦinv (K) ≤ Õ 
(√ min 
{ H, ρ−1 
} ·H2(I +B)QK 
) , 
and outputs an ε-optimal robust inventory policy using 
Õ 
( min 
{ H, ρ−1 
} ·H2(I +B)Q 
ε2 
) 
episodes. Here Õ omits absolute constants and logarithmic factors in (I,B,Q,H,K, 1/δ). 
Proof of Theorem 7.2. The statement follows by applying the proof of Theorem 4.6 and Corollary 4.7 to Minv, replacing each continuation value Vh+1(·) in the one-step robust expectation by the known bounded function Rh(x, q, ·) + Vh+1(·). 
Theorem 7.2 provides a finite-sample guarantee for learning the distributionally robust inventory policy via interactive data collection from the training inventory environment only, and without assuming access to a generative model of the inventory transition. The complexity bound scales only with the tabular size I+B and Q, without scaling with the demand bound D due to the truncation-based transition design. It becomes smaller as ρ increases, reflecting that larger ambiguity sets lead to smaller value spans and statistically easier robust learning in our framework. 
8 Conclusions and Discussions 
In this work, we show that without any structural assumptions, robust RL through interactive data collection necessarily induces a linear regret lower bound in the worst case due to the curse of support shift. Meanwhile, under the vanishing minimal value assumption, which effectively rules out the support-shift pathology for RMDPs with a TV robust set, we develop a sample-efficient robust RL algorithm for this class of problems. Beyond the main finite-horizon RMDP setup, we further extend our algorithm and theory to (i) discounted RMDPs with ratio-bounded robust sets, (ii) robust Markov games. To demonstrate the operational relevance of our theory, we instantiate the framework for data-driven robust inventory control under demand shifts. Together, these extensions and applications show that the ideas developed in this paper form a broader framework for robust sequential decision-making with interactive data collection. 
Acknowledgement 
The authors would like to thank the anonymous reviewers for their helpful comments. The authors would also like to thank Pan Xu and Zhishuai Liu for their feedback on an early draft of this work. 
References 
Agarwal, A., Jiang, N., Kakade, S. M. and Sun, W. (2019). Reinforcement learning: Theory and algorithms. CS Dept., UW Seattle, Seattle, WA, USA, Tech. Rep 10–4. 55 
Agarwal, A., Jin, Y. and Zhang, T. (2023). Vo q l: Towards optimal regret in model-free rl with nonlinear function approximation. In The Thirty Sixth Annual Conference on Learning Theory. PMLR. 8 
28
Agrawal, S. and Jia, R. (2019). Learning in structured mdps with convex cost functions: Improved regret bounds for inventory management. In Proceedings of the 2019 ACM Conference on Economics and Computation. 9 
Auer, P., Jaksch, T. and Ortner, R. (2008). Near-optimal regret bounds for reinforcement learning. Advances in neural information processing systems 21. 12, 17 
Ayoub, A., Jia, Z., Szepesvari, C., Wang, M. and Yang, L. (2020). Model-based reinforcement learning with value-targeted regression. In International Conference on Machine Learning. PMLR. 8 
Azar, M. G., Osband, I. and Munos, R. (2017). Minimax regret bounds for reinforcement learning. In International Conference on Machine Learning. PMLR. 7, 8, 17, 19, 53 
Badrinath, K. P. and Kalathil, D. (2021). Robust reinforcement learning using least squares policy iteration with provable performance guarantees. In International Conference on Machine Learning. PMLR. 7 
Bertsimas, D. and Thiele, A. (2006). A robust optimization approach to inventory theory. Operations research 54 150–168. 9 
Blanchet, J., Lu, M., Zhang, T. and Zhong, H. (2023). Double pessimism is provably efficient for distributionally robust offline reinforcement learning: Generic algorithm and robust partial coverage. arXiv preprint arXiv:2305.09659 . 4, 5, 7, 8, 10, 11, 14, 21, 23, 35, 38, 57 
Boute, R. N., Gijsbrechts, J., Van Jaarsveld, W. and Vanvuchelen, N. (2022). Deep reinforcement learning for inventory control: A roadmap. European journal of operational research 298 401–412. 4 
Clavier, P., Pennec, E. L. and Geist, M. (2023). Towards minimax optimality of model-based robust reinforcement learning. arXiv preprint arXiv:2302.05372 . 7 
Dann, C., Lattimore, T. and Brunskill, E. (2017). Unifying pac and regret: Uniform pac bounds for episodic reinforcement learning. Advances in Neural Information Processing Systems 30. 7 
Ding, W., Shi, L., Chi, Y. and Zhao, D. (2024). Seeing is not believing: Robust reinforcement learning against spurious correlation. Advances in Neural Information Processing Systems 36. 7 
Dong, J., Li, J., Wang, B. and Zhang, J. (2022). Online policy optimization for robust mdp. arXiv preprint arXiv:2209.13841 . 5 
Du, S., Kakade, S., Lee, J., Lovett, S., Mahajan, G., Sun, W. and Wang, R. (2021). Bilinear classes: A structural framework for provable generalization in rl. In International Conference on Machine Learning. PMLR. 8 
El Ghaoui, L. and Nilim, A. (2005). Robust solutions to markov decision problems with uncertain transition matrices. Operations Research 53 780–798. 7 
Fan, X., Chen, B., Lennon Olsen, T., Qin, H. and Zhou, Z. (2024). Don’t follow rl blindly: Lower sample complexity of learning optimal inventory control policies with fixed ordering costs. Available at SSRN 4828001 . 9 
Farhat, Z. U., Ghosh, D., Atia, G. K. and Wang, Y. (2025). Sample-efficient distributionally robust multi-agent reinforcement learning via online interaction. arXiv preprint arXiv:2508.02948 . 8, 9, 23 
Foster, D. J., Kakade, S. M., Qian, J. andRakhlin, A. (2021). The statistical complexity of interactive decision making. arXiv preprint arXiv:2112.13487 . 8 
Ghosh, D., Atia, G. K. and Wang, Y. (2025a). Orvit: Near-optimal online distributionally robust reinforcement learning. arXiv preprint arXiv:2508.03768 . 9 
Ghosh, D., Atia, G. K. and Wang, Y. (2025b). Scaling online distributionally robust reinforcement learning: Sample-efficient guarantees with general function approximation. arXiv preprint arXiv:2512.18957 . 9 
29
He, J., Zhao, H., Zhou, D. and Gu, Q. (2023). Nearly minimax optimal reinforcement learning for linear markov decision processes. In International Conference on Machine Learning. PMLR. 8 
He, Y., Liu, Z., Wang, W. and Xu, P. (2025). Sample complexity of distributionally robust off-dynamics reinforcement learning with online interaction. arXiv preprint arXiv:2511.05396 . 9 
Hu, J., Zhong, H., Jin, C. and Wang, L. (2022). Provable sim-to-real transfer in continuous domain with partial observations. arXiv preprint arXiv:2210.15598 . 4 
Huang, J., Zhong, H., Wang, L. and Yang, L. F. (2023a). Horizon-free and instance-dependent regret bounds for reinforcement learning with general function approximation. arXiv preprint arXiv:2312.04464 . 8 
Huang, J., Zhong, H.,Wang, L. andYang, L. F. (2023b). Tackling heavy-tailed rewards in reinforcement learning with function approximation: Minimax optimal and instance-dependent regret bounds. arXiv preprint arXiv:2306.06836 . 8 
Huh, W. T., Levi, R., Rusmevichientong, P. and Orlin, J. B. (2011). Adaptive data-driven inventory control with censored demand based on kaplan-meier estimator. Operations Research 59 929–941. 9 
Iyengar, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research 30 257–280. 4, 7, 10 
Jiang, N., Krishnamurthy, A., Agarwal, A., Langford, J. and Schapire, R. E. (2017). Contextual decision processes with low bellman rank are pac-learnable. In International Conference on Machine Learning. PMLR. 8 
Jin, C., Allen-Zhu, Z., Bubeck, S. and Jordan, M. I. (2018). Is q-learning provably efficient? Advances in neural information processing systems 31. 7, 12 
Jin, C., Liu, Q. and Miryoosefi, S. (2021). Bellman eluder dimension: New rich classes of rl problems, and sample-efficient algorithms. Advances in neural information processing systems 34 13406–13418. 8 
Jin, C., Yang, Z., Wang, Z. and Jordan, M. I. (2020). Provably efficient reinforcement learning with linear function approximation. In Conference on Learning Theory. PMLR. 8 
Kardes, E. (2005). Robust stochastic games and applications to counter-terrorism strategies. CREATE report . 6, 8 
Kiran, B. R., Sobh, I., Talpaert, V., Mannion, P., Al Sallab, A. A., Yogamani, S. and Pérez, P. (2021). Deep reinforcement learning for autonomous driving: A survey. IEEE Transactions on Intelligent Transportation Systems 23 4909–4926. 4 
Klabjan, D., Simchi-Levi, D. and Song, M. (2013). Robust stochastic lot-sizing by means of histograms. Production and Operations Management 22 691–710. 9 
Kober, J., Bagnell, J. A. and Peters, J. (2013). Reinforcement learning in robotics: A survey. The International Journal of Robotics Research 32 1238–1274. 4 
Kuang, Y., Lu, M., Wang, J., Zhou, Q., Li, B. and Li, H. (2022). Learning robust policy against disturbance in transition dynamics via state-conservative policy optimization. In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36. 4, 7 
Li, G., Cai, C., Chen, Y., Wei, Y. and Chi, Y. (2023). Is q-learning minimax optimal? a tight sample complexity analysis. Operations Research . 8 
Li, Y. and Lan, G. (2023). First-order policy optimization for robust policy evaluation. arXiv preprint arXiv:2307.15890 . 7 
Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. In Machine learning proceedings 1994. Elsevier, 157–163. 21 
30
Liu, Z., Lu, M., Wang, Z., Jordan, M. and Yang, Z. (2022). Welfare maximization in competitive equilibrium: Reinforcement learning for markov exchange economy. In International Conference on Machine Learning. PMLR. 8 
Liu, Z., Lu, M., Xiong, W., Zhong, H., Hu, H., Zhang, S., Zheng, S., Yang, Z. and Wang, Z. (2023). One objective to rule them all: A maximization objective fusing estimation and planning for exploration. arXiv preprint arXiv:2305.18258 . 8 
Liu, Z., Wang, W. and Xu, P. (2024). Upper and lower bounds for distributionally robust off-dynamics reinforcement learning. arXiv preprint arXiv:2409.20521 . 9 
Liu, Z. and Xu, P. (2024a). Distributionally robust off-dynamics reinforcement learning: Provable efficiency with linear function approximation. arXiv preprint arXiv:2402.15399 . 7, 9 
Liu, Z. and Xu, P. (2024b). Minimax optimal and computationally efficient algorithms for distributionally robust offline reinforcement learning. arXiv preprint arXiv:2403.09621 . 7 
Lyu, C., Zhang, H. and Xin, L. (2024). Ucb-type learning algorithms with kaplan–meier estimator for lost-sales inventory models with lead times. Operations Research 72 1317–1332. 9 
Ma, X., Liang, Z., Xia, L., Zhang, J., Blanchet, J., Liu, M., Zhao, Q. and Zhou, Z. (2022). Distributionally robust offline reinforcement learning with linear function approximation. arXiv preprint arXiv:2209.06620 . 4, 7 
Maurer, A. and Pontil, M. (2009). Empirical bernstein bounds and sample variance penalization. arXiv preprint arXiv:0907.3740 . 42 
Ménard, P., Domingues, O. D., Shang, X. and Valko, M. (2021). Ucb momentum q-learning: Cor-recting the bias without forgetting. In International Conference on Machine Learning. PMLR. 8 
Moos, J., Hansel, K., Abdulsamad, H., Stark, S., Clever, D. and Peters, J. (2022). Robust reinforcement learning: A review of foundations and recent advances. Machine Learning and Knowledge Extraction 4 276–315. 4 
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A. et al. (2022). Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems 35 27730–27744. 4 
Panaganti, K. and Kalathil, D. (2022). Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics. PMLR. 4, 5, 7, 11, 14 
Panaganti, K., Xu, Z., Kalathil, D. and Ghavamzadeh, M. (2022). Robust reinforcement learning using offline data. arXiv preprint arXiv:2208.05129 . 4, 5, 7, 8, 11, 14, 15, 18 
Peng, X. B., Andrychowicz, M., Zaremba, W. and Abbeel, P. (2018). Sim-to-real transfer of robotic control with dynamics randomization. In 2018 IEEE international conference on robotics and automation (ICRA). IEEE. 4 
Pinto, L., Davidson, J., Sukthankar, R. and Gupta, A. (2017). Robust adversarial reinforcement learning. In International Conference on Machine Learning. PMLR. 4 
Sadeghi, F. and Levine, S. (2016). Cad2rl: Real single-image flight without a single real image. arXiv preprint arXiv:1611.04201 . 4 
Scarf, H. E., Arrow, K. and Karlin, S. (1957). A min-max solution of an inventory problem. Tech. rep., Rand Corporation Santa Monica. 9 
Shapley, L. S. (1953). Stochastic games. Proceedings of the national academy of sciences 39 1095–1100. 21 
31
Shi, C., Chen, W. and Duenyas, I. (2016). Nonparametric data-driven algorithms for multiproduct inventory systems with censored demand. Operations Research 64 362–370. 9 
Shi, L. and Chi, Y. (2022). Distributionally robust model-based offline reinforcement learning with nearoptimal sample complexity. arXiv preprint arXiv:2208.05767 . 4, 7 
Shi, L., Gai, J., Mazumdar, E., Chi, Y. and Wierman, A. (2024a). Breaking the curse of multiagency in robust multi-agent reinforcement learning. arXiv preprint arXiv:2409.20067 . 8 
Shi, L., Li, G., Wei, Y., Chen, Y., Geist, M. and Chi, Y. (2023). The curious price of distributional robustness in reinforcement learning with a generative model. arXiv preprint arXiv:2305.16589 . 4, 5, 6, 7, 8, 11, 14, 18, 19, 37 
Shi, L., Mazumdar, E., Chi, Y. and Wierman, A. (2024b). Sample-efficient robust multi-agent reinforcement learning in the face of environmental uncertainty. arXiv preprint arXiv:2404.18909 . 8 
Si, N., Zhang, F., Zhou, Z. and Blanchet, J. (2023). Distributionally robust batch contextual bandits. Management Science . 7 
Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M., Bolton, A. et al. (2017). Mastering the game of go without human knowledge. nature 550 354–359. 4 
Sun, W., Jiang, N., Krishnamurthy, A., Agarwal, A. and Langford, J. (2019). Model-based rl in contextual decision processes: Pac bounds and exponential improvements over model-free approaches. In Conference on learning theory. PMLR. 8 
Sutton, R. S. and Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press. 4 
Tian, Y., Wang, Y., Yu, T. and Sra, S. (2020). Provably efficient online agnostic learning in markov games. arXiv preprint arXiv:2010.15020 . 22 
Wang, H., Shi, L. and Chi, Y. (2024). Sample complexity of offline distributionally robust linear markov decision processes. arXiv preprint arXiv:2403.12946 . 7 
Wang, L., Zhang, W., He, X. and Zha, H. (2018). Supervised reinforcement learning with recurrent neural network for dynamic treatment recommendation. In Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining. 4 
Wang, Q., Ho, C. P. and Petrik, M. (2022). On the convergence of policy gradient in robust mdps. arXiv preprint arXiv:2212.10439 . 7 
Wang, Q., Ho, C. P. and Petrik, M. (2023a). Policy gradient in robust MDPs with global convergence guarantee. In Proceedings of the 40th International Conference on Machine Learning (A. Krause, E. Brun-skill, K. Cho, B. Engelhardt, S. Sabato and J. Scarlett, eds.), vol. 202 of Proceedings of Machine Learning Research. PMLR. 7 
Wang, S., Si, N., Blanchet, J. and Zhou, Z. (2023b). A finite sample complexity bound for distributionally robust q-learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 7 
Wang, S., Si, N., Blanchet, J. and Zhou, Z. (2023c). On the foundation of distributionally robust reinforcement learning. arXiv preprint arXiv:2311.09018 . 7 
Wang, S., Si, N., Blanchet, J. and Zhou, Z. (2023d). Sample complexity of variance-reduced distributionally robust q-learning. arXiv preprint arXiv:2305.18420 . 7 
Wang, Y. and Zou, S. (2021). Online robust reinforcement learning with model uncertainty. Advances in Neural Information Processing Systems 34 7193–7206. 7 
32
Wang, Y. and Zou, S. (2022). Policy gradient method for robust reinforcement learning. In International Conference on Machine Learning. PMLR. 7 
Wiesemann, W., Kuhn, D. and Rustem, B. (2013). Robust markov decision processes. Mathematics of Operations Research 38 153–183. 7 
Wu, T., Yang, Y., Zhong, H., Wang, L., Du, S. and Jiao, J. (2022). Nearly optimal policy optimization with stable at any time guarantee. In International Conference on Machine Learning. PMLR. 8 
Xie, Q., Chen, Y., Wang, Z. and Yang, Z. (2020). Learning zero-sum simultaneous-move markov games using function approximation and correlated equilibrium. arXiv preprint arXiv:2002.07066 . 22 
Xin, L. and Goldberg, D. A. (2022). Distributionally robust inventory control when demand is a martingale. Mathematics of Operations Research 47 2387–2414. 9 
Xu, H. and Mannor, S. (2010). Distributionally robust markov decision processes. Advances in Neural Information Processing Systems 23. 7 
Xu, Y. and Zeevi, A. (2023). Bayesian design principles for frequentist sequential learning. In International Conference on Machine Learning. PMLR. 8 
Xu, Z., Panaganti, K. and Kalathil, D. (2023). Improved sample complexity bounds for distributionally robust reinforcement learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 4, 5, 7, 8, 11, 14 
Yang, W., Wang, H., Kozuno, T., Jordan, S. M. and Zhang, Z. (2023). Avoiding model estimation in robust markov decision processes with a generative model. arXiv preprint arXiv:2302.01248 . 7 
Yang, W., Zhang, L. and Zhang, Z. (2022). Toward theoretical understandings of robust markov decision processes: Sample complexity and asymptotics. The Annals of Statistics 50 3223–3248. 4, 5, 7, 11, 14, 18, 35 
Yu, Z., Dai, L., Xu, S., Gao, S. and Ho, C. P. (2023). Fast bellman updates for wasserstein distributionally robust mdps. In Thirty-seventh Conference on Neural Information Processing Systems. 7 
Yuan, H., Luo, Q. and Shi, C. (2021). Marrying stochastic gradient descent with bandits: Learning algorithms for inventory systems with fixed costs. Management Science 67 6089–6115. 9 
Zanette, A. and Brunskill, E. (2019). Tighter problem-dependent regret bounds in reinforcement learning without domain knowledge using value function bounds. In International Conference on Machine Learning. PMLR. 7 
Zhang, H., Chao, X. and Shi, C. (2020a). Closing the gap: A learning algorithm for lost-sales inventory systems with lead times. Management Science 66 1962–1980. 9 
Zhang, H., Chen, H., Xiao, C., Li, B., Liu, M., Boning, D. and Hsieh, C.-J. (2020b). Robust deep reinforcement learning against adversarial perturbations on state observations. Advances in Neural Information Processing Systems 33 21024–21037. 21 
Zhang, Z., Chen, Y., Lee, J. D. and Du, S. S. (2023). Settling the sample complexity of online reinforcement learning. arXiv preprint arXiv:2307.13586 . 8 
Zhang, Z., Ji, X. and Du, S. (2021). Is reinforcement learning more difficult than bandits? a near-optimal algorithm escaping the curse of horizon. In Conference on Learning Theory. PMLR. 8, 17 
Zhang, Z., Zhou, Y. and Ji, X. (2020c). Almost optimal model-free reinforcement learningvia referenceadvantage decomposition. Advances in Neural Information Processing Systems 33 15198–15207. 7 
Zhao, W., Queralta, J. P. and Westerlund, T. (2020). Sim-to-real transfer in deep reinforcement learning for robotics: a survey. In 2020 IEEE Symposium Series on Computational Intelligence (SSCI). IEEE. 4 
33
Zheng, Z. and Lin, Y. (2025). Distributionally robust online markov game with linear function approximation. arXiv preprint arXiv:2511.07831 . 8, 9, 23 
Zhong, H., Xiong, W., Zheng, S., Wang, L., Wang, Z., Yang, Z. and Zhang, T. (2022). Gec: A unified framework for interactive decision making in mdp, pomdp, and beyond. arXiv preprint arXiv:2211.01962 . 8 
Zhong, H. and Zhang, T. (2023). A theoretical analysis of optimistic proximal policy optimization in linear markov decision processes. arXiv preprint arXiv:2305.08841 . 8 
Zhou, D., Gu, Q. and Szepesvari, C. (2021a). Nearly minimax optimal reinforcement learning for linear mixture markov decision processes. In Conference on Learning Theory. PMLR. 8 
Zhou, R., Liu, T., Cheng, M., Kalathil, D., Kumar, P. and Tian, C. (2023). Natural actor-critic for robust reinforcement learning with function approximation. In Thirty-seventh Conference on Neural Information Processing Systems. 7 
Zhou, Z., Zhou, Z., Bai, Q., Qiu, L., Blanchet, J. and Glynn, P. (2021b). Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics. PMLR. 4, 7 
34
A Proofs for Properties of RMDPs with TV Robust Sets 
A.1 Proof of Proposition 2.5 
To simplify the notations, we present the following lemma, which directly implies Proposition 2.5. 
Lemma A.1 (Strong duality for TV robust set). The following duality for total variation robust set holds, for f : S 7→ [0, H], 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈[0,H] 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ · 
( η −min 
s∈S f(s) 
) + 
+ η 
} , 
where σ ∈ [0, 1] and the TV distance DTV(Q(·)∥Q⋆(·)) is defined as 
DTV(Q(·)∥Q⋆(·)) = 1 
2 
∑ s∈S 
|Q(s)−Q⋆(s)|. 
Proof of Lemma A.1. First, we note that when Q⋆(s) > 0 for any s ∈ S, i.e., any Q(·) ∈ ∆(S) is absolute continuous w.r.t. Q⋆(·), adapting the TV convention in Yang et al. (2022) to Definition 2.4, we have that 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈R 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ · 
( η −min 
s∈S f(s) 
) + 
+ η 
} . 
Furthermore, as is shown in Lemma H.8 in Blanchet et al. (2023), the optimal dual variable η⋆ lies in [0, H] when f ∈ [0, H]. Therefore, for Q⋆(·) such that Q⋆(s) > 0 for any s ∈ S, we have 
inf Q(·):DTV(Q(·)∥Q⋆(·))≤σ 
EQ(·)[f ] = sup η∈[0,H] 
{ −EQ⋆(·) 
[ (η − f)+ 
] − σ · 
( η −min 
s∈S f(s) 
) + 
+ η 
} . 
Now for any Q⋆(·) ∈ ∆(S), we can prove the same result by averaging Q⋆(·) with a uniform distribution and taking the limit. More specifically, denote U(·) ∈ ∆(S) as the uniform distribution on S, i.e., U(s) = 1/|S| for any s ∈ S. Consider the following distributionally robust optimization problem, for any ϵ ∈ [0, 1], 
P(ϵ) := inf Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ]. 
By our previous discussions, since (1− ϵ)Q⋆(s) + ϵ · U(s) > 0 for any s ∈ S and ϵ > 0, we have that 
P(ϵ) = D(ϵ), ∀ϵ ∈ (0, 1], (A.1) 
where the function D(·) : [0, 1] 7→ R+ is defined as 
D(ϵ) := sup η∈[0,H] 
{ −(1− ϵ) · EQ⋆(·) 
[ (η − f)+ 
] − ϵ · EU(·) 
[ (η − f)+ 
] − σ · 
( η −min 
s∈S f(s) 
) + 
+ η 
} . 
By the definition of P(·) and D(·), our goal is to prove that P(0) = D(0). To this end, it suffices to prove that (i) limϵ→0+ D(ϵ) exists and limϵ→0+ D(ϵ) = D(0); and (ii) limϵ→0+ P(ϵ) = P(0). To prove (i), consider that for any ϵ > 0, by the definition of D(·), 
|D(0)− D(ϵ)| ≤ sup η∈[0,H] 
{ ϵ · EQ⋆(·) 
[ (η − f)+ 
] + ϵ · EU(·) 
[ (η − f)+ 
]} ≤ ϵ · 2H. 
Since the right hand side tends to 0 as ϵ tends to 0, we know that limϵ→0+ D(ϵ) exists, limϵ→0+ D(ϵ) = D(0). This also indicates that limϵ→0+ P(ϵ) exists due to (A.1). This proves (i). Now we prove (ii). Notice that since the set { 
Q(·) ∈ ∆(S) : DTV 
( Q(·)∥(1− ϵ)Q⋆(·) + ϵ · U(·) 
) ≤ σ 
} 35
is a closed subset of R|S|, and EQ(·)[f ] is a continuous function of Q(·) ∈ R|S| w.r.t. the ∥ · ∥2-norm, we can denote the optimal solution to the optimization problem involved in P(ϵ) as 
Q† ϵ(·) = arginf 
Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ], 
which also gives that 
P(ϵ) = EQ† ϵ(·)[f ] = 
∑ s∈S 
Q† ϵ(s)f(s). 
With these preparations, we are able to prove (ii). On the one hand, consider for any ϵ ∈ (0, 1], 
DTV 
( (1− ϵ) ·Q† 
0(·) + ϵ · U(·) ∥∥(1− ϵ) ·Q⋆(·) + ϵ · U(·) 
) ≤ (1− ϵ) · σ ≤ σ. 
Therefore, for any ϵ ∈ (0, 1], it holds that 
P(ϵ) = inf Q(·):DTV 
( Q(·)∥(1−ϵ)Q⋆(·)+ϵ·U(·) 
) ≤σ 
EQ(·)[f ] ≤ E(1−ϵ)·Q† 0(·)+ϵ·U(·)[f ] = (1− ϵ) · EQ† 
0 [f ] + ϵ · EU(·)[f ], 
which implies that 
lim ϵ→0+ 
P(ϵ) ≤ EQ† 0 [f ] = P(0). (A.2) 
On the other hand, for any ϵ ∈ (0, 1], 
σ ≥ 1 
2 
∑ s∈S 
∣∣∣Q† ϵ(s)− (1− ϵ) ·Q⋆(s)− ϵ · U(s) 
∣∣∣ ≥ (1− ϵ) ·DTV(Q † ϵ(·)∥Q⋆(·))− ϵ ·DTV(Q 
† ϵ(·)∥U(·)), 
and by using DTV(Q † ϵ(·)∥U(·)) ≤ 1, we obtain that 
DTV(Q † ϵ(·)∥Q⋆(·)) ≤ σ + ϵ 
1− ϵ . (A.3) 
Consider a sequence of {ϵi}∞i=1 converging to 0, i.e., limi→∞ ϵi = 0. Since {Q† ϵi(·)} 
∞ i=1 is a sequence contained 
in a compact subset of R|S|, it has a converging (w.r.t. ∥ · ∥2) subsequence denoted by {Q† ϵik 
(·)}∞k=1 whose 
limit is denoted as Q†(·) ∈ ∆(S). By (A.3), we know that 
DTV(Q † ϵik 
(·)∥Q⋆(·)) ≤ σ + ϵik 1− ϵik 
. (A.4) 
Taking limit on both sides of (A.4) (limit of LHS exists since the TV distance is a continuous function (w.r.t. ∥ · ∥2) of its first entry and the limit of RHS obviously exists), we obtain that 
DTV(Q †(·)∥Q⋆(·)) ≤ σ. (A.5) 
Now we can arrive at the following, 
lim ϵ→0+ 
P(ϵ) = lim ϵ→0+ 
EQ† ϵ(·)[f ] = lim 
k→∞ EQ† 
ϵik (·)[f ] = EQ†(·)[f ] ≥ inf 
Q(·):DTV(Q(·)∥Q⋆(·))≤σ EQ(·)[f ] = P(0), (A.6) 
where the first and the last equality follows from the definition of P(·), the second equality follows from the choice of the sequence {ϵik}∞k=1 that converges to 0, the third equality is due to the continuity of EQ(·)[f ] of Q(·) (w.r.t. ∥ · ∥2), and the inequality follows from (A.5). Finally, with (A.2) and (A.6), we conclude that 
lim ϵ→0+ 
P(ϵ) = P(0), 
which proves (ii). Consequently, by (i) and (ii) 
P(0) = lim ϵ→0+ 
P(ϵ) = lim ϵ→0+ 
D(ϵ) = D(0). 
Recalling the definitions of P(·) and D(·), we conclude the proof of Lemma A.1. 
36
A.2 Proof of Proposition 2.7 
Proof of Proposition 2.7. Here we prove a stronger result that for any policy π and step h ∈ [H] 
max (s,a)∈S×A 
Qπ h,P,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P,Φ(s, a) ≤ 1 
ρ · ( 1− (1− ρ)H−h+1 
) , (A.7) 
max s∈S 
V π h,P,Φ(s)−min 
s∈S V π h,P,Φ(s) ≤ 
1 
ρ · ( 1− (1− ρ)H−h+1 
) . (A.8) 
First, we note that for the last step h = H, (A.7) and (A.8) naturally hold since RH ∈ [0, 1]. Now suppose that (A.8) hold for some step h+ 1. By robust Bellman equation (Proposition 2.2), we have that 
Qπ h,P⋆,Φ(s, a) = Rh(s, a) + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] ≤ 1 + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] , ∀(s, a) ∈ S ×A, (A.9) 
where the inequality uses the fact that Rh ≤ 1. Now we denote the state with the least robust value as 
s0 ∈ argmin s∈S 
V π h+1,P⋆,Φ(s). (A.10) 
Inspired by Shi et al. (2023), we choose a transition kernel P̃h satisfying that∥∥∥P̃h(·|s, a) ∥∥∥ 1 = 1− ρ, P ⋆ 
h (s ′|s, a) ≥ P̃h(s 
′|s, a) ≥ 0, ∀(s, a, s′) ∈ S ×A× S, 
which implies that 
DTV 
( P̃h(·|s, a) + ρ · δs0(·) 
∥∥∥P ⋆ h (·|s, a) 
) ≤ ρ, ∀(s, a) ∈ S ×A. 
Here δs0(·) is the point measure centered at s0 defined in (A.10). Combined with (A.9), we have that 
Qπ h,P⋆,Φ(s, a) ≤ 1 + EP̃h(·|s,a)+ρ·δs0 (·) 
[ V π h+1,P⋆,Φ 
] = 1 + EP̃h(·|s,a) 
[ V π h+1,P⋆,Φ 
] + ρ · V π 
h+1,P⋆,Φ(s0) 
≤ 1 + (1− ρ) ·max s∈S 
V π h+1,P⋆,Φ(s) + ρ ·min 
s∈S V π h+1,P⋆,Φ(s). (A.11) 
Consequently from (A.11), we further obtain that for any (s, a) ∈ S ×A, 
Qπ h,P⋆,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
≤ 1 + (1− ρ) ·max s∈S 
V π h+1,P⋆,Φ(s) + ρ ·min 
s∈S V π h+1,P⋆,Φ(s)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
= 1 + (1− ρ) · ( max s∈S 
V π h+1,P⋆,Φ(s)−min 
s∈S V π h+1,P⋆,Φ(s) 
) +min 
s∈S V π h+1,P⋆,Φ(s)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) 
≤ 1 + (1− ρ) · ( max s∈S 
V π h+1,P⋆,Φ(s)−min 
s∈S V π h+1,P⋆,Φ(s) 
) , (A.12) 
where the first inequality uses (A.11) and the last inequality uses the following fact, 
min (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a) = min 
(s,a)∈S×A 
{ Rh(s, a) + EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
]} ≥ min 
s∈S V π h+1,P⋆,Φ(s). 
Now applying the assumption that (A.8) holds at step h+1 to the right hand side of (A.12), we obtain that 
max (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a)− min 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a) ≤ 1 + 1− ρ 
ρ · ( 1− (1− ρ)H−h 
) = 
1 
ρ · ( 1− (1− ρ)H−h+1 
) . 
Thus given (A.8) at step h+ 1, we can derive (A.7) at step h. Now by noticing that 
min (s,a)∈S×A 
Qπ h,P⋆,Φ(s, a) ≤ min 
s∈S V π h,P⋆,Φ(s) ≤ max 
s∈S V π h,P⋆,Φ(s) ≤ max 
(s,a)∈S×A Qπ 
h,P⋆,Φ(s, a), 
we can conclude that (A.8) also holds at step h. As a result, by an induction argument, we finish the proof of Proposition 2.7. 
37
A.3 Proof of Proposition 4.2 
Proof of Proposition 4.2. We fix (s, a, h) ∈ S ×A× [H] throughout the proof. By Lemma A.1, we have that 
EPρ(s,a;P⋆ h ) [V ] = sup 
η∈R 
{ −EP⋆ 
h (·|s,a) [ (η − V )+ 
] − ρ · 
( η −min 
s∈S V (s) 
) + 
+ η 
} 
= sup η∈[0,H] 
{ −EP⋆ 
h (·|s,a) [ (η − V )+ 
] − ρ · 
( η −min 
s∈S V (s) 
) + 
+ η 
} 
= sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + (1− ρ) · η 
} , (A.13) 
where the second equality follows from the fact the optimal dual variable η⋆ is in [0, H] when V ∈ [0, H] (see e.g., Lemma H.8 in Blanchet et al. (2023)), and the last equality is obtained by the fact that mins∈S V (s) = 0. 
Part (i). For any η ∈ [0, H] and Q ∈ Bρ′(s, a;P ⋆ h ), we have that 
−EP⋆ h (·|s,a) 
[ (η − V )+ 
] + (1− ρ) · η ≤ (1− ρ) · 
( − EQ(·) 
[ (η − V )+ 
] + η ) 
≤ (1− ρ) · ( − EQ(·) 
[ η − V 
] + η ) 
= (1− ρ) · EQ(·) [ V ] , (A.14) 
where the first inequality uses the definition of Bρ′(s, a;P ⋆ h ), and the second inequality follows from (x)+ ≥ x. 
Furthermore, since (A.14) holds for any η ∈ [0, H] and Q ∈ Bρ′(s, a;P ⋆ h ), we have that 
sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + (1− ρ) · η 
} ≤ (1− ρ) · inf 
Q∈Bρ′ (s,a;P ⋆ h ) 
EQ(·) [ V ] . (A.15) 
Combining (A.13) and (A.15), we conclude that 
EPρ(s,a;P⋆ h ) 
[ V ] ≤ ρ′ · EBρ′ (s,a;P 
⋆ h ) 
[ V ] . 
Part (ii). Since ρ ∈ [0, 1), we know that there exists a η̃ ∈ [0,H] such that∑ s′:V (s′)<η̃ 
P ⋆ h (s 
′|s, a) ≤ 1− ρ ≤ ∑ 
s′:V (s′)≤η̃ 
P ⋆ h (s 
′|s, a), 
which further implies that we have the following interpolation for some λ ∈ [0, 1]: 
1− ρ = λ ∑ 
s′:V (s′)<η̃ 
P ⋆ h (s 
′|s, a) + (1− λ) ∑ 
s′:V (s′)≤η̃ 
P ⋆ h (s 
′|s, a). 
We define a probability measure P̃ ⋆ h (·) ∈ ∆(S) as 
P̃ ⋆ h (s 
′) = λP ⋆ 
h (s ′|s, a) · 1{V (s′) < η̃}+ (1− λ)P ⋆ 
h (s ′|s, a) · 1{V (s′) ≤ η̃} 
1− ρ . (A.16) 
It is not difficult to verify that P̃ ⋆ h ∈ Bρ′(s, a;P ⋆ 
h ). Hence, we have 
(1− ρ) · EBρ′ (s,a;P ⋆ h )[V ] ≤ (1− ρ) · EP̃⋆ 
h (·) [ V ] 
= (1− ρ) · EP̃⋆ h (·) [ V − η̃ 
] + (1− ρ) · η̃ 
= −EP⋆ h (·|s,a) 
[ (η̃ − V )+ 
] + (1− ρ) · η̃, (A.17) 
where the last equality uses the definition of P̃ ⋆ h in (A.16). Furthermore, by (A.17) we have that 
ρ′ · EBρ′ (s,a;P ⋆ h ) 
[ V ] ≤ sup 
η∈[0,H] 
{ − EP⋆ 
h (·|s,a) [ (η − V )+ 
] + (1− ρ) · η 
} (A.18) 
= EPρ(s,a;P⋆ h ) 
[ V ] , 
where the equality follows from (A.13). 
38
Combining Part (i) and Part (ii). Finally, combining (A.15) and (A.18), we prove Proposition 4.2. 
B Proofs for Hardness Results 
B.1 Proof of Theorem 3.2 
Proof of Theorem 3.2. We first explicitly give the expressions of the robust value functions in Example 3.1, based on which we derive the desired online regret lower bound. 
Robust value function. Firstly, we can explicitly write down the expression of the robust value functions for any policy π under Example 3.1, i.e., V π 
h,P⋆,Mθ ,Φ and Qπ 
h,P⋆,Mθ ,Φ . From now on we fix a policy π. 
For step h = 3, the robust value function is the reward received. We can directly obtain for any a ∈ A, 
Qπ 3,P⋆,Mθ ,Φ(sgood, a) = V π 
3,P⋆,Mθ ,Φ(sgood) = 1, Qπ 3,P⋆,Mθ ,Φ(sbad, a) = V π 
3,P⋆,Mθ ,Φ(sbad) = 0. (B.1) 
For step h = 2, by the robust Bellman equation (Proposition 2.2), we have that for the good state sgood, 
Qπ 2,P⋆,Mθ ,Φ(sgood, a) = 1 + inf 
P∈Pρ(sgood,a;P ⋆,Mθ 2 ) 
EP (·) [ V π 3,P⋆,Mθ ,Φ 
] = 1 + (1− ρ), ∀a ∈ A, (B.2) 
where the last equality is because V π 3,P⋆,Mθ ,Φ 
takes the minimal value 0 at the bad state sbad and thus the 
most adversarial transition distribution is achieved at 
P †(s′) = (1− ρ) · 1{s′ = sgood}+ ρ · 1{s′ = sbad}. 
Similarly, we have that for the bad state sbad, 
Qπ 2,P⋆,Mθ ,Φ(sbad, a) = 0 + inf 
P∈Pρ(sbad,a;P ⋆,Mθ 2 ) 
EP (·) [ V π 3,P⋆,Mθ ,Φ 
] = 
{ p− ρ, a = θ 
q − ρ, a = 1− θ . (B.3) 
Finally by the robust Bellman equation again, we have that 
V π 2,P⋆,Mθ ,Φ(sgood) = 1 + (1− ρ), V π 
2,P⋆,Mθ ,Φ(sbad) = π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ). 
Notice that by q < p we know that V π 2,P⋆,Mθ ,Φ 
(sbad) < p− ρ < 1 + (1− ρ) < V π 2,P⋆,Mθ ,Φ 
(sgood). 
For step h = 1, we consider the robust values on the initial state s1 = sgood, by robust Bellman equation, 
Qπ 1,P⋆,Mθ ,Φ(sgood, a) = 1 + inf 
P∈Pρ(sgood,a;P ⋆,Mθ 1 ) 
EP (·) [ V π 2,P⋆,Mθ ,Φ 
] (B.4) 
= 1 + (1− ρ) · [ 1 + (1− ρ) 
] + ρ · 
[ π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
] , 
for any action a ∈ A. By robust Bellman equation, we also derive V π 1,P⋆,Mθ ,Φ 
(sgood) = Qπ 1,P⋆,Mθ ,Φ 
(sgood, a). 
Lower bound the online regret under Example 3.1. With all the previous preparation, we can lower bound the online regret for robust RL with interactive data collection in Example 3.1. But first, we present the following general lemma. 
Lemma B.1 (Performance difference lemma for robust value function). For any RMDP satisfying Assump-tion 2.1 and any policy π, the following inequality holds, 
V π⋆ 
1,P⋆,Φ(s)− V π 1,P⋆,Φ(s) ≥ E(Pπ⋆,†,π⋆) 
[ H∑ 
h=1 
∑ a∈A 
( π⋆ h(a|sh)− πh(a|sh) 
) ·Qπ 
h,P⋆,Φ(sh, a) 
∣∣∣∣∣s1 = s 
] , 
where the expectation is taken with respect to the trajectories induced by policy π⋆, transition kernel Pπ⋆,†. Here the transition kernel Pπ⋆,† is defined as 
Pπ⋆,† h (·|s, a) = arginf 
P∈P(s,a;P⋆ h ) 
EP (·) [ V π⋆ 
h+1,P⋆,Φ 
] , 
where P(s, a;P ⋆ h ) is the robust set for state-action pair (s, a) (see Assumption 2.1). 
39
Proof of Lemma B.1. Please refer to Appendix B.2 for a detailed proof of Lemma B.1. 
Now back to Example 3.1, our previous calculation actually shows that, by (B.1) for step h = 3,∑ a∈A 
( π⋆,Mθ 
3 (a|s3)− π3(a|s3) ) ·Qπ 
3,P⋆,Mθ ,Φ(s3, a) = 0, ∀s3 ∈ {sgood, sbad}. (B.5) 
and by (B.4) we also have that for step h = 1,∑ a∈A 
( π⋆,Mθ 
1 (a|s1)− π1(a|s1) ) ·Qπ 
1,P⋆,Mθ ,Φ(s1, a) = 0, where s1 = sgood. (B.6) 
Finally, let’s consider step h = 2. By (B.2), we have that for the good state, it holds that∑ a∈A 
( π⋆,Mθ 
2 (a|sgood)− π2(a|sgood) ) ·Qπ 
2,P⋆,Mθ ,Φ(sgood, a) = 0, (B.7) 
Meanwhile, by (B.3), we have that for the bad state, it holds that (recall that q < p)∑ a∈A 
( π⋆,Mθ 
2 (a|sbad)− π2(a|sbad) ) ·Qπ 
2,P⋆,Mθ ,Φ(sbad, a) 
= max { p− ρ, q − ρ 
} − ( π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
) = p− ρ− 
( π2(θ|sbad) · (p− ρ) + π2(1− θ|sbad) · (q − ρ) 
) = p− q 
2 · ( ∣∣∣π⋆,Mθ 
2 (θ|sbad)− π2(θ|sbad) ∣∣∣+ ∣∣∣π⋆,Mθ 
2 (1− θ|sbad)− π2(1− θ|sbad) ∣∣∣ ) 
= (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) , (B.8) 
where according to (B.3) the optimal policy of Mθ at h = 2 and sbad is π⋆,Mθ 
2 (θ|sbad) = 1. Now combining (B.5), (B.6), (B.7), and (B.8) with Lemma B.1, we can conclude that 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V π 1,P⋆,Mθ ,Φ(sgood) 
≥ E a1∼π 
⋆,Mθ 1 (·|sgood),s2∼Pπ⋆,Mθ ,† 
1 (·|sgood,a1) 
[∑ a∈A 
( π⋆ 2(a|s2)− π2(a|s2) 
) ·Qπ 
2,P⋆,Mθ ,Φ(s2, a) 
] = Pπ⋆,Mθ ,† 
1 (sbad|sgood, 0) · (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) , (B.9) 
where the adversarial transition kernel Pπ⋆,Mθ ,† 1 is given by 
Pπ⋆,Mθ ,† 1 (·|sgood, 0) = argmin 
P∈P(sgood,0;P ⋆,Mθ 1 ) 
EP (·) 
[ V π⋆,Mθ 
2,P⋆,Mθ ,Φ 
] = (1− ρ) · 1{· = sgood}+ ρ · 1{· = sbad}. (B.10) 
Consequently, taking (B.10) back into (B.9), we have that 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V π 1,P⋆,Mθ ,Φ(sgood) ≥ ρ · (p− q) ·DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥π2(·|sbad)) . 
This implies that for any algorithm executing π1, · · · , πK , its online regret is lower bounded by the following, 
RegretMθ,ALG Φ (K) = 
K∑ k=1 
V π⋆,Mθ 
1,P⋆,Mθ ,Φ(sgood)− V πk 
1,P⋆,Mθ ,Φ(sgood) 
≥ ρ · (p− q) · K∑ 
k=1 
DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥πk 
2 (·|sbad) ) . 
40
However, since in RMDPs of Example 3.1, the online interaction process is always kept in sgood and there is no information on θ which can only be accessed at (s, h) = (sbad, 2). As a result, the estimates πk 
2 (·|sbad) of π⋆,Mθ 
2 (·|sbad) = 1{· = θ} can do no better than a random guess. Put it formally, consider that 
sup θ∈{0,1} 
EMθ,ALG 
[ RegretMθ,ALG 
Φ (K) ] 
≥ ρ · (p− q) · sup θ∈{0,1} 
EMθ,ALG 
[ K∑ 
k=1 
DTV 
( π⋆,Mθ 
2 (·|sbad) ∥∥∥πk 
2 (·|sbad) )] 
= ρ · (p− q) · sup θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] . (B.11) 
Here in the last equality we can drop the subscription of Mθ because the algorithm outputs πk 2 independent 
of the θ due to our previous discussion. Notice that 
∑ θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] = 
K∑ k=1 
∑ θ∈{0,1} 
EALG [ πk 2 (1− θ|sbad) 
] = 
K∑ k=1 
1 = K, 
which further indicates that 
sup θ∈{0,1} 
K∑ k=1 
EALG [ πk 2 (1− θ|sbad) 
] ≥ K 
2 . (B.12) 
Therefore, by combining (B.11) and (B.12), we conclude that 
inf ALG 
sup θ∈{0,1} 
EMθ,ALG 
[ RegretMθ,ALG 
Φ (K) ] ≥ (p− q) · ρK 
2 . 
This is the desired online regret lower bound of Ω(ρ ·K) for the RMDPs presented in Example 3.1. Further-
more, we can construct two RMDPs {M̃0,M̃1} with horizon 3H by concatenating H RMDPs {M0,M1} presented in Example 3.1. Notably, at any steps {3i+ 1}H−1 
i=0 , we define 
R3i+1(sbad, a) = 1, P ⋆,M̃θ 
3i+1 (sgood|sbad, a) = 1, ∀(a, θ) ∈ A× {0, 1}. 
Then we have 
inf ALG 
sup θ∈{0,1} 
EM̃θ,ALG 
[ RegretM̃θ,ALG 
Φ (K) ] ≥ H · Ω(ρ ·K) = Ω(ρ ·HK), 
which completes the proof of Theorem 3.2. 
B.2 Proof of Lemma B.1 
Proof of Lemma B.1. For any step h ∈ [H], we have that by robust Bellman equation (Proposition 2.2), 
Qπ⋆ 
h,P⋆,Φ(s, a)−Qπ h,P⋆,Φ(s, a) = EPρ(s,a;P⋆ 
h ) 
[ V π⋆ 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V π h+1,P⋆,Φ 
] . 
By the definition of the transition kernel Pπ⋆,† in Lemma B.1 and the property of infimum, we have that 
Qπ⋆ 
h,P⋆,Φ(s, a)−Qπ h,P⋆,Φ(s, a) ≥ E 
Pπ⋆,† h (·|s,a) 
[ V π⋆ 
h+1,P⋆,Φ 
] − E 
Pπ⋆,† h (·|s,a) 
[ V π h+1,P⋆,Φ 
] = E 
Pπ⋆,† h (·|s,a) 
[ V π⋆ 
h+1,P⋆,Φ − V π h+1,P⋆,Φ 
] . (B.13) 
41
By robust Bellman equation (Proposition 2.2) and (B.13), we further obtain that 
V π⋆ 
h,P⋆,Φ(s)− V π h,P⋆,Φ(s) = Eπ⋆ 
h(·|s) [ Qπ⋆ 
h,P⋆,Φ(s, ·) ] − Eπh(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] 
= Eπ⋆ h(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] − Eπh(·|s) 
[ Qπ 
h,P⋆,Φ(s, ·) ] 
+ Eπ⋆ h(·|s) 
[ Qπ⋆ 
h,P⋆,Φ(s, ·) ] − Eπ⋆ 
h(·|s) [ Qπ 
h,P⋆,Φ(s, ·) ] 
≥ ∑ a∈A 
( π⋆ h(a|s)− πh(a|s) 
) ·Qπ 
h,P⋆,Φ(s, a) 
+ E a∼π⋆ 
h(·|s),P π⋆,† h (·|s,a) 
[ V π⋆ 
h+1,P⋆,Φ − V π h+1,P⋆,Φ 
] . (B.14) 
Thus by recursively applying (B.14) over h ∈ [H], we can conclude that 
V π⋆ 
1,P⋆,Φ(s)− V π 1,P⋆,Φ(s) ≥ E(Pπ⋆,†,π⋆) 
[ H∑ 
h=1 
∑ a∈A 
( π⋆ h(a|sh)− πh(a|sh) 
) ·Qπ 
h,P⋆,Φ(sh, a) 
∣∣∣∣∣s1 = s 
] , 
which completes the proof of Lemma B.1. 
C Proofs for Theoretical Analysis of OPROVI-TV 
In this section, we prove our main theoretical results (Theorem 4.6). In Appendix C.1, we outline the proof of the theorem. In Appendix C.2, we list all the key lemmas used in the proof of the theorem. We defer the proof of all the lemmas to subsequent sections (Appendices C.3 to C.8). 
Before presenting all the proofs, we define the typical event E as 
E = 
 ∣∣∣∣ (EP⋆ 
h (·|s,a) − EP̂k h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ √√√√VP̂k 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
∣∣∣P ⋆ h (s 
′|s, a)− P̂ k h (s 
′|s, a) ∣∣∣ ≤ 
√√√√min { P ⋆ h (s 
′|s, a), P̂ k h (s 
′|s, a) } · c1ι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
, 
∀(s, a, s′, h, k) ∈ S ×A× S × [H]× [K], ∀η ∈ N1/(S √ K) 
( [0, H] 
), ι = log ( S3AH2K3/2/δ 
) , (C.1) 
where c1, c2 > 0 are two absolute constants, N1/S √ K([0, H]) denotes an 1/S 
√ K-cover of the interval [0,H]. 
Lemma C.1 (Typical event). For the typical event E defined in (C.1), it holds that P(E) ≥ 1− δ. 
Proof of Lemma C.1. This is a direct application of Bernstein inequality and its empirical version (Maurer and Pontil, 2009), together with a union bound over (s, a, s′, h, k, η) ∈ S×A×S×[H]×[K]×N1/(S 
√ K)([0, H]). 
Note that the size of N1/(S √ K)([0, H]) is of order SH 
√ K. 
In this section, we always let the event E hold, which by Lemma C.1 is of probability at least 1− δ. 
C.1 Proof of Theorem 4.6 
Proof of Theorem 4.6. With Lemma C.2 (optimism and pessimism), we can upper bound the regret as 
RegretΦ(K) = 
K∑ k=1 
V ⋆ 1,P⋆,Φ(s1)− V πk 
1,P⋆,Φ(s1) ≤ K∑ 
k=1 
V k 
1(s1)− V k 1(s1). (C.2) 
In the sequel, we break our proof into three steps. 
42
Step 1: upper bounding (C.2). According to the choice of Q k 
h, Q k 
h , V 
k 
h, V k h in (4.5), (4.6), and (4.7), 
let’s consider that for any (h, k) ∈ [H]× [K] and (s, a) ∈ S ×A, 
Q k 
h(s, a)−Qk 
h (s, a) = min 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a), min 
{ H, ρ−1 
}} −max 
{ Rh(s, a) + EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − bonuskh(s, a), 0 
} ≤ EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] + 2 · bonuskh(s, a) 
= EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] ︸ ︷︷ ︸ 
Term (i) 
+ EPρ(s,a;P⋆ h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] ︸ ︷︷ ︸ 
Term (ii) 
+ 2 · bonuskh(s, a). (C.3) 
Step 1.1: upper bounding Term (i). By using a Bernstein-style concentration argument customized for TV robust expectations (Lemma C.3), we can bound Term (i) by the bonus function, i.e., 
Term (i) ≤ 2 · bonuskh(s, a). (C.4) 
Step 1.2: upper bounding Term (ii). By our definition of the operator EPρ(s,a;P⋆ h )[V ] in (4.4), we have 
Term (ii) = sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V 
k 
h+1 
) + 
] + (1− ρ) · η 
} − sup 
η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V k 
h+1 
) + 
] + (1− ρ) · η 
} ≤ sup 
η∈[0,H] 
{ EP⋆ 
h (·|s,a) 
[( η − V k 
h+1 
) + − ( η − V 
k 
h+1 
) + 
]} . (C.5) 
By Lemma C.2 which shows that V k 
h+1 ≥ V k h+1 and the fact that (η−x)+ − (η− y)+ ≤ y−x for any y > x, 
we can further upper bound the right hand side of (C.5) by 
Term (ii) ≤ EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . (C.6) 
Step 1.3: combining the upper bounds. Now combining (C.4) and (C.6) with (C.3), we have that 
Q k 
h(s, a)−Qk 
h (s, a) ≤ EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 4 · bonuskh(s, a). 
By Lemma C.4, we can upper bound the bonus function, and after rearranging terms we further obtain that 
Q k 
h(s, a)−Qk 
h (s, a) ≤ 
( 1 + 
12 
H 
) · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] 
+ 4 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 4c3 
√ ι 
Nk h (s, a) ∨ 1 
+ 4√ K ,(C.7) 
where c1, c2, c3 > 0 are absolute constants. For the sake of brevity, we introduce the following notations of differences, for any (h, k) ∈ [H]× [K], 
∆k h := V 
k 
h(s k h)− V k 
h(s k h), 
ζkh := ∆k h − 
( Q 
k 
h(s k h, a 
k h)−Qk 
h (skh, a 
k h) ) , (C.8) 
43
ξkh := EP⋆ h (·|skh,a 
k h) 
[ V 
k 
h+1 − V k h+1 
] −∆k 
h+1. (C.9) 
If we further define the filtration {Fh,k}(h,k)∈[H]×[K] as 
Fh,k = σ ( {(sτi , aτi )}(i,τ)∈[H]×[k−1] 
⋃ {(ski , aki )}i∈[h−1] 
⋃ {skh} 
) , 
then we can find that {ζkh}(h,k)∈[H]×[K] is a martingale difference sequence with respect to {Fh,k}(h,k)∈[H]×[K] 
and {ξkh}(h,k)∈[H]×[K] is a martingale difference sequence with respect to {Fh,k ∪ {akh}}(h,k)∈[H]×[K]. Also, we further have that 
∆k h = ζkh + 
( Q 
k 
h(s k h, a 
k h)−Qk 
h (skh, a 
k h) ) 
(C.10) 
≤ ζkh + 
( 1 + 
12 
H 
) · EP⋆ 
h (·|skh,a k h) 
[ V 
k 
h+1 − V k h+1 
] 
+ 4 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c3 
√ ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4√ K 
= ζkh + 
( 1 + 
12 
H 
) · ξkh + 
( 1 + 
12 
H 
) ·∆k 
h+1 
+ 4 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c2H 
2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4c3 
√ ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 4√ K , 
where the inequality applies (C.7). Recursively applying (C.10) and using the fact that (1 + 12 H )h ≤ (1 + 
12 H )H ≤ c for some absolute constant c > 0, we can upper bound the right hand side of (C.2) as 
RegretΦ(K) ≤ K∑ 
k=1 
∆k 1 
≤ C1 · K∑ 
k=1 
H∑ h=1 
( ζkh + ξkh + 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] · ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ H2Sι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 
√ ι 
Nk h (s 
k h, a 
k h) ∨ 1 
+ 1√ K 
) . (C.11) 
where C1 > 0 is an absolute constant. 
Step 2: controlling the summation of variance terms. In view of (C.11), it suffices to upper bound its right hand side. The key difficulty is the analysis of the summation of the variance terms, which we focus on now. By Cauchy-Schwartz inequality, 
K∑ k=1 
H∑ h=1 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] Nk 
h (s k h, a 
k h) ∨ 1 
≤ 
√√√√ K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] · 
K∑ k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
.(C.12) 
On the right hand side of (C.12), the summation of the inverse of the count function is a well bounded term (Lemma C.13). So the key is to upper bound the the summation of the variance of the robust value functions to obtain a sharp bound. To this end, we invoke Lemma C.5 to obtain that with probability at least 1− δ, 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ C2 · 
( min 
{ H, ρ−1 
} ·HK +min 
{ H, ρ−1 
}3 ·Hι), (C.13) 
where C2 > 0 is an absolute constant. With inequality (C.13) and Lemma C.13 that 
K∑ k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ C ′ 2 ·HSAι, 
44
with C ′ 2 > 0 being another constant, we can upper bound the summation of the variance terms (C.12) as 
K∑ k=1 
H∑ h=1 
√√√√VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] Nk 
h (s k h, a 
k h) ∨ 1 
≤ C3 
√ min 
{ H, ρ−1 
} ·H2SAKι+min 
{ H, ρ−1 
}3 ·H2SAι2. (C.14) 
where C3 > 0 is also an absolute constant. 
Step 3: finishing the proof. With (C.11) and (C.14), it suffices to control the remaining terms. For the summation of the martingale difference terms, notice that by the definitions in (C.8) and (C.9), both ζkh and ξkh are bounded by min{H, ρ−1} according to (4.5) and Lemma C.2 (optimism and pessimism). As a result, using Azuma-Hoeffding inequality, with probability at least 1− δ 
K∑ k=1 
H∑ h=1 
(ζkh + ξkh) ≤ C4 ·min { H, ρ−1 
} · √ HKι, 
where C4 > 0 is an absolute constant. For the summation of the inverse of the count function in (C.11), it suffices to invoke again Lemma C.13. For the additional square-root count term in (C.11), Cauchy–Schwarz and Lemma C.13 give 
K∑ k=1 
H∑ h=1 
√ ι 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ 
√√√√HKι · K∑ 
k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ C ′ 4H 
√ SAKι2, 
for an absolute constant C ′ 4 > 0, which is absorbed by the leading term after adjusting logarithmic factors. 
Combining all together, with probability at least 1− 3δ, we have 
RegretΦ(K) ≤ C5 · (√ 
min { H, ρ−1 
} ·H2SAKι2 +min 
{ H, ρ−1 
}3 ·H2SAι3 
+min { H, ρ−1 
} · √ HKι+H3S2Aι2 +H 
√ SAKι2 +H 
√ K 
) = O 
(√ min 
{ H, ρ−1 
} ·H2SAKι′ 
) , 
where C5 > 0 is an absolute constant and ι′ = log2(SAHK/δ). This completes the proof of Theorem 4.6. 
C.2 Key Lemmas 
Lemma C.2 (Optimistic and pessimistic estimation of the robust values). By setting the bonuskh as in (4.8), then under the typical event E, it holds that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a), V k h(s) ≤ V πk 
h,P⋆,Φ(s) ≤ V ⋆ h,P⋆,Φ(s) ≤ V 
k 
h(s), (C.15) 
for any (s, a, h, k) ∈ S ×A× [H]× [K]. 
Proof of Lemma C.2. See Appendix C.3 for a detailed proof. 
Lemma C.3 (Proper bonus for TV robust sets and optimistic and pessimistic value estimators). By setting the bonuskh as in (4.8), then under the typical event E, it holds that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] ≤ 2 · bonuskh(s, a), 
Proof of Lemma C.3. See Appendix C.4 for a detailed proof. 
45
Lemma C.4 (Control of the bonus term). Under the typical event E, the bonuskh in (4.8) is bounded by 
bonuskh(s, a) ≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 4 · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1−V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ c3 
√ ι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c2, c3 > 0 are absolute constants. 
Proof of Lemma C.4. See Appendix C.5 for a detailed proof. 
Lemma C.5 (Total variance law for robust MDP with TV robust sets). With probability at least 1− δ, the following inequality holds 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ c3 · 
( min{H, ρ−1} ·HK +min{H, ρ−1}3 ·Hι 
) . 
where ι = log(S3AH2K3/2/δ) and c3 > 0 is an absolute constant. 
Proof of Lemma C.5. See Appendix C.6 for a detailed proof. 
C.3 Proof of Lemma C.2 
Proof of Lemma C.2. We prove Lemma C.2 by induction. Suppose the conclusion (C.15) holds at step h+1. For step h, let’s first consider the robust Q function part. Specifically, by using the robust Bellman optimal equation (Proposition 2.3) and (4.5), we have that 
Q⋆ h,P⋆,Φ(s, a)−Q 
k 
h(s, a) 
≤ max 
{ EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V 
k 
h+1 
] − bonuskh(s, a), Q 
⋆ h,P⋆,Φ(s, a)−min 
{ H, ρ−1 
}} ≤ max 
{ EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − bonuskh(s, a), 0 
} , (C.16) 
where the second inequality follows from the induction of V ⋆ h+1,P⋆,Φ ≤ V 
k 
h+1 at step h+ 1 and the fact that 
Q⋆ h,P⋆,Φ ≤ min{H, ρ−1} (by Proposition 2.7 and Assumption 4.1). By Lemma C.7, we have that 
EPρ(s,a;P⋆ h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
Now by further applying Lemma C.11 to the variance term in the above inequality, we can obtain that 
EPρ(s,a;P⋆ h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] 
≤ 
√√√√(VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] + 4H · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
]) · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√√√√EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] · 4Hc1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 1√ K , (C.17) 
46
where the first inequality is due to Lemma C.11, the second inequality is due to √ a+ b ≤ 
√ a+ 
√ b, and the 
last inequality is from √ ab ≤ a+ b where c′2 > 0 is an absolute constant. Therefore, combining (C.16) and 
(C.17), and the choice of bonuskh(s, a) in (4.8), we can conclude that 
Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a). 
Furthermore, it holds that Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a). Thus it reduces to prove Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a). Again, by using the robust Bellman equation (Proposition 2.2) and (4.6), we have that 
Qk 
h (s, a)−Qπk 
h,P⋆,Φ(s, a) 
≤ max 
{ EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − bonuskh(s, a), 0 
} ≤ max 
{ EPρ(s,a;P̂k 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − bonuskh(s, a), 0 
} , (C.18) 
where the second inequality follows from the induction of V k h+1 ≤ V πk 
h+1,P⋆,Φ at step h+ 1 and the fact that 
Qπk 
h,P⋆,Φ ≥ 0. By Lemma C.8, we have that 
EPρ(s,a;P̂k h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
Now by applying Lemma C.11 to the variance term, with an argument similar to (C.17), we can obtain that 
EPρ(s,a;P̂k h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
] (C.19) 
≤ 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
Thus by combining (C.18) and (C.19), and the choice of bonuskh(s, a) in (4.8), we can conclude that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a). 
Therefore, we have proved that at step h, it holds that 
Qk 
h (s, a) ≤ Qπk 
h,P⋆,Φ(s, a) ≤ Q⋆ h,P⋆,Φ(s, a) ≤ Q 
k 
h(s, a). 
Finally for the robust V function part, consider that by robust Bellman equation (Proposition 2.2) and (4.7), 
V k h(s) = Eπk 
h(·|s) 
[ Qk 
h (s, ·) 
] ≤ Eπk 
h(·|s) 
[ Qπk 
h,P⋆,Φ(s, ·) ] = V πk 
h,P⋆,Φ(s), 
and that by robust Bellman optimal equation (Proposition 2.3), the choice of πk, and (4.7), 
V ⋆ h,P⋆,Φ(s) = max 
a∈A Q⋆ 
h,P⋆,Φ(s, a) ≤ max a∈A 
Q k 
h(s, a) = V k 
h(s), 
which proves that 
V k h(s) ≤ V πk 
h,P⋆,Φ(s) ≤ V ⋆ h,P⋆,Φ(s) ≤ V 
k 
h(s). 
Since the conclusion (C.15) holds for the V function part at step H+1, an induction proves Lemma C.2. 
47
C.4 Proof of Lemma C.3 
Proof of Lemma C.3. We upper bound the required signed sum by applying Lemma C.9 to the two absolute differences, 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] 
≤ 2 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 2 · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 2c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 2√ K , (C.20) 
where c1, c ′ 2 > 0 are absolute constants. Then applying Lemma C.11 to the variance term in (C.20), with an 
argument the same as (C.17) in the proof of Lemma C.2, we can obtain that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] 
≤ 2 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 4 · EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 2c′′2H 
2ι 
Nk h (s, a) ∨ 1 
+ 2√ K . 
Therefore, by looking into the choice of bonuskh(s, a) in (4.8), we can conclude that 
EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
] + EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
] − EPρ(s,a;P̂k 
h ) 
[ V k 
h+1 
] ≤ 2 · bonuskh(s, a), 
This finishes the proof of Lemma C.3. 
C.5 Proof of Lemma C.4 
Proof of Lemma C.4. Recall that the bonuskh(s, a) is defined as 
bonuskh(s, a) = 
√√√√VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
+ 2EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
The main thing we need to consider is to control the first term and the second term. We first deal with the second term of bonuskh(s, a) by invoking Lemma C.10, which gives 
2EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
≤ ( 
2 
H + 
2 
H2 
) · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′2HSι 
Nk h (s, a) ∨ 1 
≤ 3EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2HSι 
Nk h (s, a) ∨ 1 
, (C.21) 
where the second inequality is from H ≥ 2. Then we deal with the first term (variance term) of bonuskh(s, a) by invoking Lemma C.12, which gives√√√√VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] · c1ι 
Nk h (s, a) ∨ 1 
(C.22) 
≤ 
√√√√(VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] + 4H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′′2 H 4Sι 
Nk h (s,a)∨1 
+ 1 ) · c1ι 
Nk h (s, a) ∨ 1 
≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√√√√4H · EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] · c1ι 
Nk h (s, a) ∨ 1 
+ 
√ c1c′′2SH 
2ι 
Nk h (s, a) ∨ 1 
+ 
√ c1ι 
Nk h (s, a) ∨ 1 
≤ 
√√√√VP⋆ h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
] · c′1ι 
Nk h (s, a) ∨ 1 
+ EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ 
( 4c1 + 
√ c1c′′2S 
) H2ι 
Nk h (s, a) ∨ 1 
+ c3 
√ ι 
Nk h (s, a) ∨ 1 
Thus by combining (C.21) and (C.22) with the choice of bonuskh, we can conclude the proof of Lemma C.4. 
48
C.6 Proof of Lemma C.5 
Proof of Lemma C.5. The key idea is to relate the visitation distribution (w.r.t. P ⋆) and the variance (w.r.t. P ⋆) to the value function of πk, after which we can derive an upper bound for the total variance. Throughout this proof, we use the shorthand 
H = min { H, ρ−1 
} . 
Under the convention stated after Definition 2.4, when ρ = 0 we have H = H. According to Proposition 2.7 and Assumption 4.1, for any policy π and any step h, the robust value function of π holds that 
max s∈S 
V π h,P⋆,Φ(s) ≤ H, (C.23) 
which we usually apply in the sequel. Now consider the following decomposition of our target, 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] = 
K∑ k=1 
{ H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] − E(skh,a 
k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣∣Gk−1 
]} ︸ ︷︷ ︸ 
Term (i): martingale difference term 
+ 
K∑ k=1 
E(skh,a k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣∣Gk−1 
] ︸ ︷︷ ︸ 
Term (ii): total variance law under P ⋆ 
. 
where we denote the filtration Gk = σ({(sτh, aτh, sτh+1)}(h,τ)∈[H]×[k]) with G0 understood as the trivial sigmafield. In the sequel, we upper bound each of the two terms respectively. 
Term (i): martingale difference term. This is a summation of martingale difference term (with respect to filtration Gk = σ({(sτh, aτh, sτh+1)}(h,τ)∈[H]×[k])). By Azuma-Hoeffding’s inequality, with probability at least 1− δ, 
Term (i) ≤ c ·H ·H2 · √ Kι, (C.24) 
where c > 0 is an absolute constant. We have utilized the fact of (C.23) to obtain the upper bound HH 2 on 
each martingale difference term in the summation. 
Term (ii): total variance law under P ⋆. The upper bound of this term is the core part of the analysis, for which we summarize it in the following lemma. 
Lemma C.6 (Total variance law under P ⋆). Under the same settings as Theorem 4.6, given any deterministic policy π, define 
T̃h(·|s, a) ∈ argmin P (·)∈Pρ(s,a;P⋆ 
h ) 
EP (·) [ V π h+1,P⋆,Φ 
] , ∀(s, a, h) ∈ S ×A× [H], (C.25) 
and set T̃ = {T̃h}Hh=1. Then we have that 
E(sh,ah)∼(P⋆,π) 
[ H∑ 
h=1 
VP⋆ h (·|sh,ah) 
[ V π h+1,P⋆,Φ 
]] ≤ 2H ·H, 
Consequently, it holds that 
E(skh,a k h)∼(P⋆,πk) 
[ H∑ 
h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣∣Gk−1 
] ≤ 2H ·H. 
49
We defer the proof of Lemma C.6 to Appendix C.7. With Lemma C.6, conditional on Gk−1, the policy πk is fixed and deterministic by (4.7); taking π = πk for k ∈ [K] therein, we obtain that the Term (ii) is upper bounded by 
Term (ii) ≤ 2H ·H ·K. (C.26) 
Finishing the proof. Finally, combining the upper bounds for Terms (i) and (ii) i.e., (C.24) and (C.26), we conclude that with probability at least 1− δ, it holds that 
K∑ k=1 
H∑ h=1 
VP⋆ h (·|skh,a 
k h) 
[ V πk 
h+1,P⋆,Φ 
] ≤ c ·H ·H2 · 
√ Kι+ 2H ·H ·K 
≤ c′ ·H ·H ·K + c′′ ·H ·H3 · ι, 
where in the last inequality we use √ ab ≤ a+ b for any a, b > 0. Plug in the notation that H = min{H, ρ−1} 
and finish the proof of Lemma C.5. 
C.7 Proof of Lemma C.6 
Proof of Lemma C.6. For notational simplicity, given policy π, we denote 
Vh(·) := V π h,P⋆,Φ(·), h ∈ [H + 1]. 
According to Proposition 2.7 and Assumption 4.1, for any step h, it holds that 
0 ≤ Vh(s) ≤ H, ∀(s, h) ∈ S × [H + 1]. (C.27) 
Using the property of variance, we have that for any sh ∈ S and ah = πh(sh), 
VP⋆ h (·|sh,ah) [Vh+1] = EP⋆ 
h (·|sh,ah) 
[ V 2 h+1 
] − ( EP⋆ 
h (·|sh,ah) [Vh+1] )2 . (C.28) 
By the robust Bellman equation and the definition of T̃h in (C.25), we have that 
Vh(sh) = Rh(sh, ah) + ET̃h(·|sh,ah) [Vh+1] . (C.29) 
We further define 
∆h(s, a) := EP⋆ h (·|s,a) [Vh+1]− ET̃h(·|s,a) [Vh+1] . (C.30) 
Since P ⋆ h (· | s, a) belongs to robust set Pρ(s, a;P 
⋆ h ) and T̃h minimizes the expectation of Vh+1, we have 
∆h(s, a) ≥ 0, ∀(s, a, h) ∈ S ×A× [H]. 
Combining (C.29) and (C.30), we obtain that 
EP⋆ h (·|sh,ah) [Vh+1] = Vh(sh)−Rh(sh, ah) + ∆h(sh, ah). (C.31) 
Thus, by (C.28) and (C.31), we have 
VP⋆ h (·|sh,ah) [Vh+1] = EP⋆ 
h (·|sh,ah) 
[ V 2 h+1 
] − (Vh(sh)−Rh(sh, ah) + ∆h(sh, ah)) 
2 
= EP⋆ h (·|sh,ah) 
[ V 2 h+1 
] − (Vh(sh)) 
2 + 2Vh(sh) (Rh(sh, ah)−∆h(sh, ah)) 
− (Rh(sh, ah)−∆h(sh, ah)) 2 
≤ EP⋆ h (·|sh,ah) 
[ V 2 h+1 
] − (Vh(sh)) 
2 + 2H. 
50
Here the last inequality follows from (C.27), 0 ≤ Rh(sh, ah) ≤ 1, and ∆h(sh, ah) ≥ 0. Specifically, let x = Rh(sh, ah)−∆h(sh, ah). If x ≤ 0, then 2Vh(sh)x−x2 ≤ 0; otherwise 0 < x ≤ 1, and 2Vh(sh)x−x2 ≤ 2H. Taking expectation with respect to the trajectory generated by (P ⋆, π), we have for each h ∈ [H] that 
E(sh,ah)∼(P⋆,π) 
[ VP⋆ 
h (·|sh,ah) [Vh+1] ] ≤ Esh+1∼(P⋆,π) 
[ (Vh+1(sh+1)) 
2 ] − Esh∼(P⋆,π) 
[ (Vh(sh)) 
2 ] + 2H. 
Taking summation over h ∈ [H] gives that 
E(sh,ah)∼(P⋆,π) 
[ H∑ 
h=1 
VP⋆ h (·|sh,ah) [Vh+1] 
] 
≤ H∑ 
h=1 
{ Esh+1∼(P⋆,π) 
[ (Vh+1(sh+1)) 
2 ] − Esh∼(P⋆,π) 
[ (Vh(sh)) 
2 ]} 
+ 2H ·H 
= EsH+1∼(P⋆,π) 
[ (VH+1(sH+1)) 
2 ] − Es1 
[ (V1(s1)) 
2 ] + 2H ·H 
≤ 2H ·H, 
where the equality follows from telescoping and the last inequality uses VH+1 ≡ 0 and the nonnegativity of (V1(s1)) 
2. This concludes the proof of Lemma C.6. 
C.8 Other Technical Lemmas 
Before presenting all lemmas, we recall that the typical event E is defined as 
E = 
∣∣∣(EP⋆ h (·|s,a) − EP̂k 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣ ≤ √√√√VP̂k 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
∣∣∣P ⋆ h (s 
′|s, a)− P̂ k h (s 
′|s, a) ∣∣∣ ≤ 
√√√√min { P ⋆ h (s 
′|s, a), P̂ k h (s 
′|s, a) } · c1ι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
, 
∀(s, a, s′, h, k) ∈ S ×A× S × [H]× [K], ∀η ∈ N1/(S √ K) 
( [0, H] 
), ι = log ( S3AH2K3/2/δ 
) . (C.32) 
where c1, c2 > 0 are two absolute constants, N1/S √ K([0, H]) denotes an 1/S 
√ K-cover of the interval [0,H]. 
C.8.1 Concentration Inequalities 
Lemma C.7 (Bernstein bound for TV robust sets and the optimal robust value function). Under event E in (C.32), it holds that 
∣∣∣∣EPρ(s,a;P̂k h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ √√√√VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ). 
Proof of Lemma C.7. By our definition of the operator EPρ(s,a;P̂k h )[V 
⋆ h+1,P⋆,Φ] in (4.4), we can arrive that∣∣∣∣EPρ(s,a;P̂k 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ = 
∣∣∣∣∣ sup η∈[0,H] 
{ − EP̂k 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] + (1− ρ) · η 
} 
51
− sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] + (1− ρ) · η 
}∣∣∣∣∣ ≤ sup 
η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } , (C.33) 
Now according to the first inequality of event E , we have that 
∣∣∣∣ (EP⋆ h (·|s,a) − EP̂k 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ √√√√VP̂k 
h (·|s,a) 
[( η − V ⋆ 
h+1,P⋆,Φ 
) + 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
, 
for any η ∈ N1/(S √ K)([0, H]). Here the second inequality is because Var[(a−X)+] ≤ Var[X]. Therefore, by 
a covering argument, for any η ∈ [0,H], it holds that 
∣∣∣∣ (EP⋆ h (·|s,a) − EP̂k 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ ≤ √√√√VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K . 
This finishes the proof of Lemma C.7. 
Lemma C.8 (Bernstein bound for TV robust sets and the robust value function of πk). Under event E in (C.32), suppose that the optimism and pessimism (C.15) holds at (h+ 1, k), then it holds that∣∣∣∣EPρ(s,a;P̂k 
h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c ′ 2 are absolute constants. 
Proof of Lemma C.8. By our definition of the operator EPρ(s,a;P )[V πk 
h+1,P⋆,Φ] in (4.4), we can arrive that,∣∣∣∣EPρ(s,a;P̂k h ) 
[ V πk 
h+1,P⋆,Φ 
] − EPρ(s,a;P⋆ 
h ) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ = 
∣∣∣∣∣ sup η∈[0,H] 
{ − EP̂k 
h (·|s,a) 
[( η − V πk 
h+1,P⋆,Φ 
) + 
] + (1− ρ) · η 
} 
− sup η∈[0,H] 
{ − EP⋆ 
h (·|s,a) 
[( η − V πk 
h+1,P⋆,Φ 
) + 
] + (1− ρ) · η 
}∣∣∣∣∣ ≤ sup 
η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V πk 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
≤ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
︸ ︷︷ ︸ Term (i) 
+ sup η∈[0,H] 
{∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [( η − V πk 
h+1,P⋆,Φ 
) + − ( η − V ⋆ 
h+1,P⋆,Φ 
) + 
]∣∣∣∣ } 
︸ ︷︷ ︸ Term (ii) 
, 
52
We deal with Term (i) and Term (ii) respectively. For Term (i), this is exactly the same as the right hand side of (C.33). Therefore, applying the same argument as Lemma C.7 gives the following upper bound, 
Term (i) ≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ c2Hι 
Nk h (s, a) ∨ 1 
+ 1√ K . (C.34) 
For Term (ii), we first apply the second inequality of event E to obtain that, 
Term (ii) (C.35) 
≤ sup η∈[0,H] 
∑ s′∈S 
√ P̂ k h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
 · ∣∣∣(η − V πk 
h+1,P⋆,Φ(s ′) ) + − ( η − V ⋆ 
h+1,P⋆,Φ(s ′) ) + 
∣∣∣  . 
By the assumption that (C.15) holds at (h+ 1, k), we can upper bound the absolute value above by∣∣∣(η − V πk 
h+1,P⋆,Φ(s ′) ) + − ( η − V ⋆ 
h+1,P⋆,Φ(s ′) ) + 
∣∣∣ ≤ ∣∣∣V πk 
h+1,P⋆,Φ(s ′)− V ⋆ 
h+1,P⋆,Φ(s ′) ∣∣∣ 
≤ V k 
h+1(s ′)− V k 
h+1(s ′). (C.36) 
where the first inequality is due to the 1-Lipschitz continuity of ψη(x) = (η−x)+, and the second inequality is due to (C.15). Thus combining (C.35) and (C.36), we know that 
Term (ii) ≤ ∑ s′∈S 
√ P̂ k h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
 · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) . (C.37) 
Now following the argument first identified by Azar et al. (2017), we proceed to upper bound (C.37) as 
Term (ii) ≤ ∑ s′∈S 
( P̂ k h (s 
′|s, a) H 
+ c1Hι 
Nk h (s, a) ∨ 1 
+ c2ι 
Nk h (s, a) ∨ 1 
) · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) 
≤ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
, (C.38) 
where c′2 > 0 is another absolute constant. The first inequality is by √ ab ≤ a+ b and the second inequality 
is due to V k 
h+1, V k h+1 ∈ [0,H]. Finally, combining (C.34) and (C.38), we prove Lemma C.8. 
Lemma C.9 (Bernstein bounds for TV robust sets and optimistic and pessimistic robust value estimators). Under event E in (C.32), suppose that the optimism and pessimism (C.15) holds at (h+ 1, k), it holds that 
max 
{ ∣∣∣EPρ(s,a;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V 
k 
h+1 
]∣∣∣ , ∣∣∣EPρ(s,a;P̂k h ) 
[ V k 
h+1 
] − EPρ(s,a;P⋆ 
h ) 
[ V k 
h+1 
]∣∣∣ } 
≤ 
√√√√VP̂k h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
] · c1ι 
Nk h (s, a) ∨ 1 
+ EP̂k 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] H 
+ c′2H 
2Sι 
Nk h (s, a) ∨ 1 
+ 1√ K , 
where ι = log(S3AH2K3/2/δ) and c1, c ′ 2 are absolute constants. 
Proof of Lemma C.9. This follows from the same proof as Lemma C.8 and is thus omitted. 
Lemma C.10 (Non-robust concentration). Under event E in (C.32), suppose that the optimism and pessimism (C.15) holds at (h+ 1, k), then it holds that∣∣∣∣ (EP̂k 
h (·|s,a) − EP⋆ h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ 1 
H · EP⋆ 
h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′2H 2Sι 
Nk h (s, a) ∨ 1 
. 
where ι = log(S2AH2K3/2/δ) and c′2 is an absolute constant. 
53
Proof of Lemma C.10. According to the second inequality of event E , we have that∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ ∑ s′∈S 
(√ P ⋆ h (s 
′|s, a) · c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
) · ( V 
k 
h+1(s ′)− V k 
h+1(s ′) ) , 
where we also apply (C.15) that V k 
h+1(s ′) ≥ V k 
h+1(s ′). Now using the same argument as (C.38) in the proof 
of Lemma C.8, we can arrive at∣∣∣∣ (EP̂k h (·|s,a) − EP⋆ 
h (·|s,a) 
) [ V 
k 
h+1 − V k h+1 
]∣∣∣∣ ≤ EP⋆ h (·|s,a) 
[ V 
k 
h+1(s ′)− V k 
h+1(s ′) ] 
H + 
c′2H 2Sι 
Nk h (s, a) ∨ 1 
, 
which finishes the proof of Lemma C.10. 
C.8.2 Variance Analysis 
Lemma C.11 (Variance analysis 1). Suppose that the optimism and pessimism (C.15) holds at (h + 1, k), then the following inequality holds,∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . 
Proof of Lemma C.11. Directly consider that the left hand side can be upper bounded by the following,∣∣∣∣VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 
∣∣∣∣∣EP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
)2 /4 
] − EP̂k 
h (·|s,a) 
[( V ⋆ h+1,P⋆,Φ 
)2]∣∣∣∣∣ + 
∣∣∣∣ (EP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ])2 
− ( EP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
])2 ∣∣∣∣. (C.39) 
Since all of V k 
h+1, V k h+1, V 
⋆ h+1,P⋆,Φ ∈ [0,H] (by the correctness of (C.15) and the definitions of V 
k 
h+1, V k h+1), 
we can further upper bound the right hand side of (C.39) as∣∣∣∣VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP̂k 
h (·|s,a) 
[ V ⋆ h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP̂k h (·|s,a) 
[∣∣∣(V k 
h+1 + V k h+1 
) /2− V ⋆ 
h+1,P⋆,Φ 
∣∣∣] 
≤ 4H · EP̂k h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] , 
where the last inequality is due to the correctness of (C.15) at (h+ 1, k). This proves Lemma C.11. 
Lemma C.12 (Variance analysis 2). Under event E in (C.32), suppose that optimism and pessimism (C.15) holds at (h+ 1, k), then it holds that∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] + 
c′2H 4Sι 
Nk h (s, a) ∨ 1 
+ 1. 
Proof of Lemma C.12. We first compare the variance under the empirical kernel with the variance under the 
true kernel. Since ( V 
k 
h+1 + V k h+1 
) /2 ∈ [0,H],∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ]∣∣∣∣ 
≤ 3H2 ∑ s′∈S 
∣∣∣P̂ k h (s 
′|s, a)− P ⋆ h (s 
′|s, a) ∣∣∣ . 
54
Under event E , the last display is further bounded by 
3H2 ∑ s′∈S 
(√ P ⋆ h (s 
′|s, a)c1ι Nk 
h (s, a) ∨ 1 + 
c2ι 
Nk h (s, a) ∨ 1 
) ≤ 3H2 
(√ c1Sι 
Nk h (s, a) ∨ 1 
+ c2Sι 
Nk h (s, a) ∨ 1 
) . 
Using √ x ≤ x+ 1 after adjusting constants yields∣∣∣∣VP̂k 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ]∣∣∣∣ ≤ 1 + 
c′2H 4Sι 
Nk h (s, a) ∨ 1 
. (C.40) 
Thus by (C.40), we can bound our target as∣∣∣∣VP̂k h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ ∣∣∣∣VP⋆ 
h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣+ c′2H 4Sι 
Nk h (s, a) ∨ 1 
+ 1. (C.41) 
Now by the same proof of Lemma C.11, using the correctness of (C.15) at (h+ 1, k), we can show that∣∣∣∣VP⋆ h (·|s,a) 
[( V 
k 
h+1 + V k h+1 
) /2 ] − VP⋆ 
h (·|s,a) 
[ V πk 
h+1,P⋆,Φ 
]∣∣∣∣ ≤ 4H · EP⋆ h (·|s,a) 
[ V 
k 
h+1 − V k h+1 
] . (C.42) 
Combining (C.41) and (C.42), we can finish the proof of Lemma C.12. 
C.8.3 Other Auxiliary Lemmas 
Lemma C.13 (Lemma 7.5 in Agarwal et al. (2019)). For the sequences of {skh, akh} H,K h,k=1, it holds that 
K∑ k=1 
H∑ h=1 
1 
Nk h (s 
k h, a 
k h) ∨ 1 
≤ c ·HSA log(K). 
where c > 0 is an absolute constant. 
Proof of Lemma C.13. See Lemma 7.5 in Agarwal et al. (2019) for a detailed proof. 
D Proofs for Extension I (Section 5) 
In this section, we prove the theoretical results in Section 5. 
D.1 Proof of Corollary 5.1 
Proof of Corollary 5.1. We consider applying Algorithm 1 on the auxiliary S̃ ×A-rectangular RMDP with a TV robust set M̃ (see Section 5) which satisfies the vanishing minimal value assumption (Assumption 4.1). Suppose the algorithm outputs π̃1, · · · , π̃K for the K episodes. Then Theorem 4.6 shows that by a proper choice of the hyperparameters, with probability at least 1− δ 
RegretΦ̃(K) = 
K∑ k=1 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1)− V π̃k 
1,P̃⋆,Φ̃ (s1) ≤ O 
(√ min 
{ H, ρ−1 
} H2(S + 1)AKι′ 
) , . (D.1) 
where ι′ = log2(SAHK/δ) and ρ = 1 − ρ′ ∈ [0, 1). In the sequel, we prove that for any policy π̃ of M̃ and its induced policy π̃S of Mγ , their robust value functions coincide at the initial state s1 ∈ S, that is, 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = V π̃S 1,P⋆,Φ′(s1), 
55
where V π̃ 1,P̃⋆,Φ̃ 
is the robust value function of π̃ in M̃ = (S̃,A,H, P̃ ⋆, R̃, Φ̃), and V π̃S 1,P⋆,Φ′ is the robust value 
function of π̃S in Mγ = (S,A, H, P ⋆, Rγ ,Φ ′). To this end, we actually prove a stronger result that for any 
step h ∈ [H], it holds that 
(ρ′)h−1 · V π̃ h,P̃⋆,Φ̃ 
(s) = V π̃S h,P⋆,Φ′(s), ∀s ∈ S. (D.2) 
We prove (D.2) by induction. For step H, by robust Bellman equation, we have that, for any (s, a) ∈ S ×A, 
(ρ′)H−1 ·Qπ̃ H,P̃⋆,Φ̃ 
(s, a) = (ρ′)H−1 · ( γ 
ρ′ 
)H−1 
·RH(s, a) = Rγ,H(s, a) = Qπ̃S H,P⋆,Φ′(s, a), 
and thus for any s ∈ S, 
(ρ′)H−1 · V π̃ H,P̃⋆,Φ̃ 
(s) = Eπ̃(·|s) 
[ (ρ′)H−1 ·Qπ̃ 
H,P̃⋆,Φ̃ (s, ·) 
] = Eπ̃S(·|s) 
[ Qπ̃S 
H,P⋆,Φ′(s, ·) ] = V π̃S 
H,P⋆,Φ′(s). 
This proves (D.2) for step H. Suppose that (D.2) holds at some step h+ 1, that is, 
(ρ′)h · V π̃ h+1,P̃⋆,Φ̃ 
(s) = V π̃S h+1,P⋆,Φ′(s), ∀s ∈ S. (D.3) 
Then for step h, by robust Bellman equation and Proposition 4.2, we have that 
(ρ′)h−1 ·Qπ̃ h,P̃⋆,Φ̃ 
(s, a) = (ρ′)h−1 · ( γ 
ρ′ 
)h−1 
·Rh(s, a) + (ρ′)h−1 · EP̃ρ(s,a;P̃⋆ h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] = Rγ,h(s, a) + (ρ′)h−1 · ρ′ · EB̃ρ′ (s,a;P̃ 
⋆ h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] , (D.4) 
where the last equality utilizes Proposition 4.2 since mins∈S̃ V π̃ h+1,P̃⋆,Φ̃ 
(s) = 0, and we adopt the notation 
B̃ρ′(s, a; P̃ ⋆ h ) = 
{ P̃ (·) ∈ ∆(S̃) : sup 
s′∈S̃ 
P̃ (s′) 
P̃ ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} . 
Notice that by the definition (5.2), we know for (s, a) ∈ S × A it holds that P̃ ⋆ h (·|s, a) = P ⋆ 
h (·|s, a) which is supported on S. Therefore, we can equivalently write 
B̃ρ′(s, a; P̃ ⋆ h ) = 
{ P̃ (·) ∈ ∆(S̃) : sup 
s′∈S 
P̃ (s′) 
P̃ ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} 
= 
{ P̃ (·) ∈ ∆(S) : sup 
s′∈S 
P̃ (s′) 
P ⋆ h (s 
′|s, a) ≤ 1 
ρ′ 
} = Bρ′(s, a;P ⋆ 
h ). (D.5) 
Thus by (D.4) and (D.5) and the induction hypothesis (D.3), we obtain that for any (s, a) ∈ S ×A, 
(ρ′)h−1 ·Qπ̃ h,P̃⋆,Φ̃ 
(s, a) = Rγ,h(s, a) + (ρ′)h · EBρ′ (s,a;P ⋆ h ) 
[ V π̃ h+1,P̃⋆,Φ̃ 
] = Rγ,h(s, a) + EBρ′ (s,a;P 
⋆ h ) 
[ V π̃S h+1,P⋆,Φ′ 
] = Qπ̃S 
h,P⋆,Φ′(s, a), 
where the second equality applies (D.3) and the last equality is from robust Bellman equation. Consequently, for any s ∈ S, we have that 
(ρ′)h−1 · V π̃ h,P̃⋆,Φ̃ 
(s) = Eπ̃(·|s) 
[ (ρ′)h−1 ·Qπ̃ 
h,P̃⋆,Φ̃ (s, ·) 
] = Eπ̃S(·|s) 
[ Qπ̃S 
h,P⋆,Φ′(s, ·) ] = V π̃S 
h,P⋆,Φ′(s), 
which finishes the induction argument, proving our claim (D.2). By taking h = 1, we can derive that for any 
initial state s1 ∈ S, it holds that for any policy π̃ of M̃ and its induced policy π̃S of Mγ , 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = V π̃S 1,P⋆,Φ′(s1). 
56
This indicates two facts: the first is that 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1) = max π 
V π 1,P⋆,Φ′(s1), (D.6) 
where on the right hand side the maximization is with respect to all the policies for Mγ ; the second is that 
V π̃k 
1,P̃⋆,Φ̃ (s1) = V 
π̃k S 
1,P⋆,Φ′(s1), (D.7) 
for each k ∈ [K], where we recall that π̃k is the policy output by Algorithm 1 for episode k. As a result, the K policies {π̃k 
S}Kk=1 of Mγ during interactive data collection satisfy with probability at least 1− δ, 
RegretΦ′(K) = 
K∑ k=1 
max π 
V π 1,P⋆,Φ′(s1)− V 
π̃k S 
1,P⋆,Φ′(s1) 
= 
K∑ k=1 
max π̃ 
V π̃ 1,P̃⋆,Φ̃ 
(s1)− V π̃k 
1,P̃⋆,Φ̃ (s1) 
≤ O (√ 
min { H, (1− ρ′)−1 
} H2SAKι′ 
) , 
where in the second equality we apply the facts (D.6) and (D.7), and the last inequality follows from (D.1) and that ρ = 1− ρ′. This completes the proof of Corollary 5.1. 
E Proofs for Extension II (Section 6) 
E.1 Proof of Proposition 6.2 
Proof of Proposition 6.2. This proposition is a finite-horizon robust analogue of Shapley’s recursion for zerosum stochastic games, where S ×A×B-rectangular uncertainty ensures time consistency and enables backward induction (Blanchet et al., 2023). Our proof is based on the backward induction method. 
Step 1: stage-game minimax at each (h, s). Fix (h, s) and treat V ⋆ h+1,P⋆,Φ as given. By finiteness of 
S and compactness of the TV-ball, the infimum defining the robust expectation in (6.2) is attained for every (s, a, b), hence Q⋆ 
h,P⋆,Φ(s, a, b) is well-defined. Thus, for fixed (h, s), Q⋆ h,P⋆,Φ(s, ·, ·) defines a finite two-player 
zero-sum matrix game. By von Neumann’s minimax theorem, there exist mixed actions π⋆ h(·|s) ∈ ∆(A) and 
ν⋆h(·|s) ∈ ∆(B) such that 
max π∈∆(A) 
min ν∈∆(B) 
Eπ,ν 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] = Eπ⋆ 
h,ν ⋆ h 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] = min 
ν∈∆(B) max 
π∈∆(A) Eπ,ν 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] . 
(E.1) Collecting {π⋆ 
h(·|s)}h,s and {ν⋆h(·|s)}h,s yields Markov policies (π⋆, ν⋆). 
Step 2: backward induction. We now show (6.3) holds by backward induction on h. The claim is trivial at h = H + 1 since V π,ν 
H+1,P⋆,Φ ≡ 0. Assume (6.3) holds at stage h+ 1 for all states. Fix any opponent policy ν. By (6.1), 
V π⋆,ν h,P⋆,Φ(s) = Ea∼π⋆ 
h(·|s), b∼νh(·|s) 
[ Rh(s, a, b) + EPρ(s,a,b;P⋆ 
h ) 
[ V π⋆,ν h+1,P⋆,Φ 
] ] . 
Since V π⋆,ν h+1,P⋆,Φ(s 
′) ≥ V ⋆ h+1,P⋆,Φ(s 
′) for all s′ by the induction hypothesis, monotonicity of the robust expectation yields 
EPρ(s,a,b;P⋆ h ) 
[ V π⋆,ν h+1,P⋆,Φ 
] ≥ EPρ(s,a,b;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] . 
Therefore 
V π⋆,ν h,P⋆,Φ(s) ≥ Ea∼π⋆ 
h, b∼νh 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] ≥ min 
λ∈∆(B) Ea∼π⋆ 
h, b∼λ 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] = V ⋆ 
h,P⋆,Φ(s), 
57
where the last equality follows from the maximin optimality of π⋆ h(·|s) in (E.1). 
Fix any Player 1 policy π. Similarly, by (6.1) and induction, V π,ν⋆ 
h+1,P⋆,Φ(s ′) ≤ V ⋆ 
h+1,P⋆,Φ(s ′) for all s′, 
hence (by monotonicity) 
EPρ(s,a,b;P⋆ h ) 
[ V π,ν⋆ 
h+1,P⋆,Φ 
] ≤ EPρ(s,a,b;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] , 
which yields 
V π,ν⋆ 
h,P⋆,Φ(s) ≤ Ea∼πh, b∼ν⋆ h 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] ≤ max 
µ∈∆(A) Ea∼µ, b∼ν⋆ 
h 
[ Q⋆ 
h,P⋆,Φ(s, a, b) ] = V ⋆ 
h,P⋆,Φ(s), 
where the last equality is the minimax optimality of ν⋆h(·|s) in (E.1). Combining the two bounds gives (6.3) 
and, by taking ν = ν⋆ (or π = π⋆), also V π⋆,ν⋆ 
h,P⋆,Φ(s) = V ⋆ h,P⋆,Φ(s). 
Step 3: strong duality. The saddle inequalities (6.3) directly imply (6.4). 
E.2 Proof of Theorem 6.5 
Proof of Theorem 6.5. We recall the bonus choice in (6.6): 
bonuskh(s, a, b) = cb min{H, ρ−1} 
√ Sι 
Nk h (s, a, b) ∨ 1 
, ι = log(SABHK/δ), (E.2) 
where cb > 0 is a sufficiently large absolute constant. The proof uses a positive-part regret decomposition and controls the robust Bellman error uniformly through an L1 transition-estimation bound. 
Minimax operator. For any Q : S ×A× B → R, define the state-wise minimax operator 
(MM[Q])(s) := max π∈∆(A) 
min ν∈∆(B) 
Ea∼π, b∼ν [Q(s, a, b)]. 
It is standard that MM is monotone: if Q ≤ Q′ entrywise, then MM[Q] ≤ MM[Q′] entrywise. 
Step 1: a uniform transition-estimation event. We use a standard multinomial concentration event. There exists an event E with P(E) ≥ 1− δ/2 such that, for all (k, h, s, a, b) ∈ [K]× [H]× S ×A× B, 
∥∥∥P̂ k h (·|s, a, b)− P ⋆ 
h (·|s, a, b) ∥∥∥ 1 ≤ ce 
√ Sι 
Nk h (s, a, b) ∨ 1 
, (E.3) 
where ce > 0 is an absolute constant and ι = log(SABHK/δ). The deterministic inequalities below are derived on E ; the martingale concentration step is applied separately and then combined with E by a union bound. 
We also use the game analogue of Proposition 2.7: under the same TV ambiguity, the robust value and Q-functions have span at most min{H, ρ−1}. The proof is identical to the single-agent backward-induction argument, with (s, a) replaced by (s, a, b) and the state-wise maximization replaced by the monotone max– min operator. Together with Assumption 6.4 and nonnegative rewards, this span bound implies that all true robust values and Q-values appearing below lie in [0,min{H, ρ−1}]; the optimistic iterates lie in the same interval by the clipping in (6.7). 
We next record the consequence of (E.3) for the TV-dual operator used in the robust Bellman updates. For any function f : S → [0,min{H, ρ−1}], this operator is 
EPρ(s,a,b;P )[f ] = sup η∈[0,min{H,ρ−1}] 
{ −EP (·|s,a,b)[(η − f)+] + (1− ρ)η 
} . 
The restriction of η to [0,min{H, ρ−1}] is without loss because 0 ≤ f ≤ min{H, ρ−1}. Following the convention in (4.4), we use this display as the dual operator in the algorithm. When f is V ⋆ 
h,P⋆,Φ or 
58
a realized value function V π,ν h,P⋆,Φ, Assumption 6.4 ensures the required vanishing condition, so the same 
display is the true TV-robust Bellman term. Therefore, on E ,∣∣∣EPρ(s,a,b;P̂k h )[f ]− EPρ(s,a,b;P⋆ 
h )[f ] ∣∣∣ 
≤ sup η∈[0,min{H,ρ−1}] 
∣∣∣EP̂k h (·|s,a,b)[(η − f)+]− EP⋆ 
h (·|s,a,b)[(η − f)+] ∣∣∣ 
≤ min{H, ρ−1} ∥∥∥P̂ k 
h (·|s, a, b)− P ⋆ h (·|s, a, b) 
∥∥∥ 1 
≤ bonuskh(s, a, b), (E.4) 
where the last inequality follows by choosing cb sufficiently large. 
Step 2: proper bonus for TV-robust expectations. By construction, the optimistic value iterates 
satisfy 0 ≤ V k 
h ≤ min{H, ρ−1} for all (h, k). Thus (E.4) implies that, on E , for all (k, h, s, a, b),∣∣∣EPρ(s,a,b;P̂k h ) 
[ V 
k 
h+1 
] − EPρ(s,a,b;P⋆ 
h ) 
[ V 
k 
h+1 
]∣∣∣ ≤ bonuskh(s, a, b). (E.5) 
Step 3: optimism by backward induction. We next establish the optimism property needed for regret analysis. On event E , for all k ∈ [K], h ∈ [H], and s ∈ S, 
V ⋆ h,P⋆,Φ(s) ≤ V 
k 
h(s), (E.6) 
and entrywise, for all (s, a, b) ∈ S ×A× B, 
Q⋆ h,P⋆,Φ(s, a, b) ≤ Q 
k 
h(s, a, b). (E.7) 
The proof is by backward induction on h. For h = H + 1, the claim is immediate. Suppose the claim holds at step h + 1. For every (s, a, b), the robust Bellman recursion, the induction hypothesis, monotonicity of the dual TV operator, and (E.5) imply 
Q⋆ h,P⋆,Φ(s, a, b) = Rh(s, a, b) + EPρ(s,a,b;P⋆ 
h ) 
[ V ⋆ h+1,P⋆,Φ 
] ≤ Rh(s, a, b) + EPρ(s,a,b;P⋆ 
h ) 
[ V 
k 
h+1 
] ≤ Rh(s, a, b) + EPρ(s,a,b;P̂k 
h ) 
[ V 
k 
h+1 
] + bonuskh(s, a, b). 
Since Q⋆ 
h,P⋆,Φ(s, a, b) ≤ min{H, ρ−1}, 
the clipping in the definition of Q k 
h is harmless, and hence 
Q⋆ h,P⋆,Φ(s, a, b) ≤ Q 
k 
h(s, a, b). 
The monotonicity of MM then implies 
V ⋆ h,P⋆,Φ(s) = (MM[Q⋆ 
h,P⋆,Φ])(s) ≤ (MM[Q k 
h])(s) = V k 
h(s). 
This proves (E.6)–(E.7). 
Step 4: episode-wise regret decomposition. Fix an adaptive Markov opponent sequence ν = {νk}Kk=1 
that is non-anticipating. By the fixed-initial-state convention, sk1 = s1 for every episode k. Define the realized-opponent optimistic gap 
Dk h(s) := 
( V 
k 
h(s)− V πk,νk 
h,P⋆,Φ(s) ) + , ∀(h, k, s) ∈ [H]× [K]× S. 
59
By (E.6), for each episode k, 
V ⋆ 1,P⋆,Φ(s 
k 1)− V πk,νk 
1,P⋆,Φ(s k 1) ≤ V 
k 
1(s k 1)− V πk,νk 
1,P⋆,Φ(s k 1) ≤ Dk 
1 (s k 1). 
Thus it suffices to upper bound ∑K 
k=1D k 1 (s 
k 1). 
Now fix (h, k, s, a, b). By the definition of Q k 
h, the robust Bellman recursion for Qπk,νk 
h,P⋆,Φ, and (E.5), 
Q k 
h(s, a, b)−Qπk,νk 
h,P⋆,Φ(s, a, b) 
≤ EPρ(s,a,b;P⋆ h ) 
[ V 
k 
h+1 
] − EPρ(s,a,b;P⋆ 
h ) 
[ V πk,νk 
h+1,P⋆,Φ 
] + 2bonuskh(s, a, b). (E.8) 
For the robust-expectation difference, the TV dual form gives 
EPρ(s,a,b;P⋆ h ) 
[ V 
k 
h+1 
] − EPρ(s,a,b;P⋆ 
h ) 
[ V πk,νk 
h+1,P⋆,Φ 
] ≤ sup 
η∈[0,min{H,ρ−1}] EP⋆ 
h (·|s,a,b) 
[ (η − V πk,νk 
h+1,P⋆,Φ)+ − (η − V k 
h+1)+ 
] ≤ EP⋆ 
h (·|s,a,b) 
[( V 
k 
h+1 − V πk,νk 
h+1,P⋆,Φ 
) + 
] = EP⋆ 
h (·|s,a,b)[D k h+1], (E.9) 
where the second inequality uses (η − x)+ − (η − y)+ ≤ (y − x)+. Combining (E.8) and (E.9),( Q 
k 
h(s, a, b)−Qπk,νk 
h,P⋆,Φ(s, a, b) ) + ≤ EP⋆ 
h (·|s,a,b)[D k h+1] + 2bonuskh(s, a, b). (E.10) 
For each (h, k), define 
∆k h := Ea∼πk 
h(·|s k h), b∼νk 
h(·|s k h) 
[( Q 
k 
h(s k h, a, b)−Qπk,νk 
h,P⋆,Φ(s k h, a, b) 
) + 
] , 
ζkh := ∆k h − 
( Q 
k 
h(s k h, a 
k h, b 
k h)−Qπk,νk 
h,P⋆,Φ(s k h, a 
k h, b 
k h) ) + , 
ξkh := EP⋆ h (·|skh,a 
k h,b 
k h) [Dk 
h+1]−Dk h+1(s 
k h+1). 
By the minimax update of V k 
h, 
V k 
h(s k h) ≤ Ea∼πk 
h(·|s k h), b∼νk 
h(·|s k h) [Q 
k 
h(s k h, a, b)], 
and by the robust Bellman recursion under (πk, νk), 
V πk,νk 
h,P⋆,Φ(s k h) = Ea∼πk 
h(·|s k h), b∼νk 
h(·|s k h) [Qπk,νk 
h,P⋆,Φ(s k h, a, b)]. 
Therefore, 
Dk h(s 
k h) ≤ 
( Ea∼πk 
h(·|s k h), b∼νk 
h(·|s k h) [Q 
k 
h(s k h, a, b)−Qπk,νk 
h,P⋆,Φ(s k h, a, b)] 
) + ≤ ∆k 
h. 
The last inequality uses Jensen’s inequality and the convexity of x 7→ x+. Consequently, 
RegretΦ,{νk}(K) ≤ K∑ 
k=1 
Dk 1 (s 
k 1) ≤ 
K∑ k=1 
∆k 1 . (E.11) 
Let Fh,k := σ 
( {(sτi , aτi , bτi , sτi+1)}i∈[H], τ<k ∪ {(ski , aki , bki , ski+1)}i<h ∪ {skh} 
) . 
The policies πk h(·|skh) and νkh(·|skh) are Fh,k-measurable, and the opponent is non-anticipating with respect 
to Player 1’s current randomization. Thus 
E[ζkh | Fh,k] = 0, E[ξkh | σ(Fh,k, a k h, b 
k h)] = 0. 
60
The martingale concentration below is applied to this natural sequential filtration, which first reveals the history, then the sampled action pair, and then the next state. Using (E.10), 
∆k h = ζkh + 
( Q 
k 
h(s k h, a 
k h, b 
k h)−Qπk,νk 
h,P⋆,Φ(s k h, a 
k h, b 
k h) ) + 
≤ ζkh + EP⋆ h (·|skh,a 
k h,b 
k h) [Dk 
h+1] + 2bonuskh(s k h, a 
k h, b 
k h) 
= ζkh + ξkh +Dk h+1(s 
k h+1) + 2bonuskh(s 
k h, a 
k h, b 
k h) 
≤ ζkh + ξkh +∆k h+1 + 2bonuskh(s 
k h, a 
k h, b 
k h), (E.12) 
where the last inequality uses Dk h+1(s 
k h+1) ≤ ∆k 
h+1. Recursively applying (E.12) from h = 1 to H and using 
the convention Dk H+1 ≡ 0 and ∆k 
H+1 = 0 yields 
K∑ k=1 
∆k 1 ≤ 
K∑ k=1 
H∑ h=1 
(ζkh + ξkh) + 2 
K∑ k=1 
H∑ h=1 
bonuskh(s k h, a 
k h, b 
k h). (E.13) 
Step 5: summing up the bonuses. By the value bound 0 ≤ Dk h ≤ min{H, ρ−1} and the clipped Q-
updates, both ζkh and ξkh are uniformly bounded by min{H, ρ−1} up to an absolute constant. Thus a separate application of the Azuma–Hoeffding inequality implies that, with probability at least 1− δ/2, 
K∑ k=1 
H∑ h=1 
(ζkh + ξkh) ≤ C1 min{H, ρ−1} √ HKι, (E.14) 
where C1 > 0 is an absolute constant. It remains to control the bonus sum. By (E.2), 
K∑ k=1 
H∑ h=1 
bonuskh(s k h, a 
k h, b 
k h) 
≤ cb min{H, ρ−1} √ Sι 
K∑ k=1 
H∑ h=1 
1√ Nk 
h (s k h, a 
k h, b 
k h) ∨ 1 
. (E.15) 
For each fixed h, summing over the SAB state-action-opponent-action triples and using ∑n−1 
j=0 (j ∨ 1)−1/2 ≤ 2 √ n+ 1 gives 
K∑ k=1 
1√ Nk 
h (s k h, a 
k h, b 
k h) ∨ 1 
≤ C2 
√ SABK 
for an absolute constant C2 > 0. Summing over h ∈ [H] and substituting into (E.15), we get 
K∑ k=1 
H∑ h=1 
bonuskh(s k h, a 
k h, b 
k h) ≤ C3 min{H, ρ−1}HS 
√ ABKι, (E.16) 
where C3 > 0 is an absolute constant. Combining (E.11), (E.13), (E.14), and (E.16), and absorbing logarithmic factors into Õ(·), we obtain by 
a union bound that, with probability at least 1− δ, 
RegretΦ,{νk}(K) ≤ Õ ( min{H, ρ−1}HS 
√ ABK 
) . 
This completes the proof of Theorem 6.5. 
61