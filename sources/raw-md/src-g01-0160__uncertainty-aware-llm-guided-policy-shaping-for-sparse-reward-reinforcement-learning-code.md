> Source: https://arxiv.org/html/2606.06673v1

Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning Code: github.com/USD-AI-ResearchLab/uncertainty-aware-llm-rl
Report GitHub Issue
×
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub 
arXiv is now an independent nonprofit! Learn more ×
arXiv logo Back to arXiv
Why HTML? Report Issue Back to Abstract Download PDF  
Abstract
I Introduction
II Methodology
II-A Problem Formulation
II-B System Architecture
II-C Generating Optimal Trajectories with A*
II-D Fine-Tuning a BERT-Based LLM
III Experiments, Results, and Discussion
III-A Implementation details
III-B Environment and Reward Structure
III-C Results
III-D Ablation Study
III-E Discussion
III-F Comparative Analysis of Calibrated LLM Performance
III-F 1 MC Dropout Computational Cost
III-F 2 Sample Efficiency vs Computational Trade-off
III-F 3 Environment Complexity Scaling
III-F 4 Comparison with 4×4 Linear RL using PPO
III-F 5 Comparison with 4×4 Uncalibrated LLM
III-F 6 Comparison with 4×4 Unguided RL using PPO
III-F 7 Comparison with 4×4 Q-Learning using Group Relative Policy Optimization (GRPO)
III-F 8 Comparison with DQN using GRPO
IV Conclusion
References
License: arXiv.org perpetual non-exclusive license
arXiv:2606.06673v1 [cs.LG] 04 Jun 2026
Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning † † thanks: Code: github.com/USD-AI-ResearchLab/uncertainty-aware-llm-rl
Ujjwal Bhatta1, Utsabi Dangol1, Sumaly Bajracharya1, Rodrigue Rizk, KC Santosh 1These authors contributed equally to this work.
Abstract
Sparse rewards and heterogeneous task sequences remain persistent challenges in Reinforcement Learning (RL), often resulting in slow convergence, weak generalization, and inefficient exploration. We propose Uncertainty-Aware LLM-Guided Policy Shaping (ULPS), a novel framework that integrates a calibrated Large Language Model (LLM) into the RL training loop to provide structured, uncertainty-modulated behavioral guidance. ULPS employs an A*-based oracle to synthesize optimal symbolic trajectories, which are used to fine-tune a BERT-based language model. During training, this model supplies action suggestions whose influence is conditioned on epistemic uncertainty estimated via Monte Carlo (MC) dropout. An entropy-based blending mechanism adaptively balances LLM guidance and the learned policy (via Proximal Policy Optimization, PPO), allowing the agent to prioritize reliable priors while preserving adaptability. We evaluate ULPS on the MiniGrid-UnlockPickup benchmark and observe consistent improvements in success rate, reward efficiency, and sample complexity over unguided, uncalibrated, and standard RL baselines. ULPS achieves more than 9% improvement in execution accuracy after fine-tuning, requires fewer environment interactions, and yields higher reward AUC. Our results demonstrate that integrating symbolic A* trajectories, pretrained language priors, and uncertainty-aware control offers a principled and effective approach to multi-task reinforcement learning in sparse-reward domains, with potential extensibility to partially observable and multi-agent settings.
I Introduction
Despite advances in Reinforcement Learning (RL) for sequential decision-making tasks like games, robotics, and navigation [ 12, 17, 9] , sparse rewards and diverse task sequences remain major challenges, limiting sample efficiency and generalization. In sparse-reward settings, agents receive feedback only after long sequences of correct actions, making exploration inefficient and frequently resulting in reliance on random exploration strategies, requiring thousands of episodes to discover successful trajectories [ 8, 13] . To address these challenges, prior work has explored incorporating external knowledge into the RL process for sparse-reward environments, relying on human expertise to guide agent. For example, agents can be trained to imitate actions that align with human-judged preferences, which accelerates learning in complex tasks [ 4] . This shows considerable success, but they face practical limitations in scaling it to collect human feedback across diverse environments [ 2] .
Recent advances in natural language processing show that Large Language Models (LLMs) can reason over multi-step information [ 14] , generate actions from textual or visual inputs to guide RL agents, and decompose complex tasks into context-aware subgoals and mid-level plans that can be translated into executable actions [ 5, 10, 11] . However, there are difficulties when directly incorporating LLMs into decision-making or learning systems [ 1] . Simply injecting language guidance into RL often leads to over-reliance on uncertain suggestions, degraded stability, or bias toward suboptimal heuristics. LLMs have a high degree of confidence in producing inaccurate or hallucinated outputs [ 18] . Language models are prone to overconfidence and may make unreliable suggestions that could impact learning compared to human experts [ 19] . Therefore, estimating the model's uncertainty and figuring out when to trust its judgment are crucial. A key challenge is to calibrate LLM-based priors and modulate their influence based on uncertainty. Shoaeinaeini and Harrison [ 16] introduced a more structured solution to this problem by designing a calibrated RL system guided by LLMs. Their method uses Monte Carlo (MC) dropout [ 7] along with entropy-based policy shaping to adjust how much the agent relies on LLM advice in multi-task settings.
Building on this foundation, we propose a unified framework, U ncertainty-Aware L LM-Guided P olicy S haping (ULPS), that uses an A*-based oracle to fine-tune LLM and then integrates LLM judgements into the Proximal Policy Optimization (PPO)-based RL training loop through an uncertainty-aware mechanism. Inspired by [ 16] , we extend their environment and prompting approach with improved policy combination and uncertainty integration for larger-scale tasks. Our contributions are twofold: a) a framework that combines LLM guidance with RL policies using uncertainty-aware, entropy-weighted blending for adaptive policy shaping, and b) a scalable self-supervised method using A*-generated trajectories to fine-tune BERT for multi-task sequential decision-making. We demonstrate its effectiveness with 99.17% accuracy, a 9% improvement over prior models, achieving higher reward efficiency and lower complexity in sparse-reward environments. 
Figure 1: Overview of the proposed ULPS framework. An A*-based oracle generates optimal trajectories for BERT fine-tuning. During training, the environment state (S) is encoded and fed into the calibrated LLM. MC dropout estimates uncertainty producing P L  L  M P_{LLM} and H n  o  r  m H_{norm} . The same BERT features are processed by PPO Agent to generate P a  g  e  n  t P_{agent} . These distributions are fused with entropy-based shaping. The environment executes action (A), returning reward (R) and next state (S'), and the transition tuple (S, A, R, S') is stored for PPO updates.
II Methodology
II-A Problem Formulation
We consider an episodic Markov Decision Process (MDP) M = { 𝒮 , 𝒜 , P , R , γ } M={\mathcal{S},\mathcal{A},P,R,\gamma} with sparse rewards, where the agent must solve multiple tasks in MiniGrid-UnlockPickup [ 3] :
• 𝒮 \mathcal{S} : State space representing the agent's position, orientation, and environment configuration;
• 𝒜 \mathcal{A} : Discrete action space, 𝒜 \mathcal{A} = {turn left, turn right, move forward, pick up, toggle};
• P P : Transition probability function defining environment;
• R (S, A): Reward function providing sparse feedback for task completion; and
• γ \gamma : Discount factor for future rewards.
Our environment has a sequence of subtasks T = { T 1 T_{1} , T 2 T_{2} , T 3 T_{3} }, navigating to and picking up the key, navigating to and unlocking the door, and finally navigating to the goal. The agent receives sparse rewards upon successful completion of each subtask, making traditional RL exploration inefficient, as reward R is non-zero for specific transitions ( S, A, R, S') where task objective is achieved. S' is a new state when agent performs an action A while on state S. The objective is to learn a policy P final  ( a | s ) P_{\text{final}}(a|s) maximizing expected discounted returns. ULPS augments PPO with an LLM-derived prior P LLM  ( a | s ) P_{\text{LLM}}(a|s) .
II-B System Architecture
Our model uses a calibrated LLM-based RL system with a PPO agent. The proposed architecture is depicted in Fig. 1. The agent learns by combining its own policy with the guidance of a language model, modulated by the model's confidence. At the start of each episode, the environment state S S is translated into a textual prompt, which is passed through the fine-tuned BERT model T T times using MC dropout. This produces a distribution over possible actions P LLM P_{\text{LLM}} , along with an associated entropy H H that captures the model's uncertainty. We then normalize the entropy to obtain H norm ∈ [ 0 , 1 ] H_{\text{norm}}\in[0,1] , which determines how much weight to assign to the LLM versus the PPO policy. The PPO agent's policy, P agent P_{\text{agent}} , is obtained by passing BERT-extracted features through a small actor-critic network. The final policy is a convex combination:
P final = ( 1 − H norm ) ⋅ P LLM + H norm ⋅ P agent . P_{\text{final}}=(1-H_{\text{norm}})\cdot P_{\text{LLM}}+H_{\text{norm}}\cdot P_{\text{agent}}.
(1)
An action A ∼ P final A\sim P_{\text{final}} is then sampled and executed in the environment. The resulting experience tuple ( S, A, R, S') is stored in the PPO buffer for future updates. Over time, the PPO agent is updated using these collected trajectories. This adaptive training procedure enables the agent to leverage its own learning and the structured priors embedded in the language model. The algorithm 1 summarizes the full process.
Algorithm 1 Training with Uncertainty-Aware LLM Guidance
0: Fine-tuned BERT model ℬ \mathcal{B} , PPO agent, environment ℰ \mathcal{E} , number of episodes N N , forward passes T = 8 T=8 , dropout rate p = 0.1 p=0.1
0: Trained PPO policy P agent P_{\text{agent}} , experience buffer for policy updates
1: for each episode e = 1 e=1 to N N do
2: Initialize S ← S 0 S\leftarrow S_{0}
3: while episode not terminated do
4: τ ← ϕ  ( S ) \tau\leftarrow\phi(S) {state to text prompt}
5: P LLM ← 1 T  ∑ k = 1 T ℬ ( k )  ( τ ; p ) P_{\text{LLM}}\leftarrow\frac{1}{T}\sum_{k=1}^{T}\mathcal{B}^{(k)}(\tau;,p) { T T stochastic forward passes}
6: H ← − ∑ a ∈ 𝒜 P LLM  ( a )  log  P LLM  ( a ) H\leftarrow-\sum_{a\in\mathcal{A}}P_{\text{LLM}}(a)\log P_{\text{LLM}}(a)
7: H norm ← ( H − H min ) / ( H max − H min ) H_{\text{norm}}\leftarrow(H-H_{\min})/(H_{\max}-H_{\min})
8: P final ← ( 1 − H norm ) ⋅ P LLM + H norm ⋅ P agent P_{\text{final}}\leftarrow(1-H_{\text{norm}})\cdot P_{\text{LLM}}+H_{\text{norm}}\cdot P_{\text{agent}}
9: A ∼ P final A\sim P_{\text{final}} ; R , S ′ ← ℰ  ( S , A ) R,S^{\prime}\leftarrow\mathcal{E}(S,A)
10: buffer ← \leftarrow buffer ∪ { ( S , A , R , S ′ ) } \cup\ {(S,A,R,S^{\prime})} ; S ← S ′ S\leftarrow S^{\prime}
11: end while
12: end for
13: Update PPO using buffer with GAE λ = 0.95 \lambda=0.95 , clipping ϵ = 0.2 \epsilon=0.2
II-C Generating Optimal Trajectories with A*
We employ an A* planner over the grid-world transition graph to compute optimal action sequences. The A* pathfinding algorithm computes the shortest feasible path while looking for obstacles such as walls and locked doors. We use the Manhattan distance heuristic, defined as h  ( pos , target ) = | pos x − target x | + | pos y − target y | h(\text{pos},\text{target})=|\text{pos}{x}-\text{target}{x}|+|\text{pos}{y}-\text{target}{y}| . Each trajectory consists of structured state representations (semantic maps and relative positions) and symbolic actions (e.g., turn left, move forward, pickup).
II-D Fine-Tuning a BERT-Based LLM
We convert state representations into textual prompts (e.g., encoded grid layout) and train a BERT-based next-action predictor using entropy H norm H_{\text{norm}} to obtain a blending weight, and final policy ( P final P_{\text{final}} ) is determined by combining LLM and PPO policies as described in algorithm 1.
III Experiments, Results, and Discussion
III-A Implementation details
The architecture integrates a calibrated LLM, fine-tuned on 21,500 samples using bert-base-uncased embeddings, an input length of maximum of 100 tokens, dropout value of 0.1, and A* pathfinding-generated data, with a PPO agent. PPO agent employs an actor-critic network optimized with AdamW optimizer with a learning rate of 5e-5, batch size of 16, and 5 epochs. The agent is trained for 1,000 episodes, each with a maximum of 50 steps. The policy-shaping mechanism combines probability distributions of both the LLM and the PPO agents based on the normalized entropy of the current state. The entropy coefficient is set to 0.01, value loss coefficient to 0.5, and the GAE-lambda parameter to 0.95. These hyperparameters were selected based on insights from previous research and validated through initial experiments. While [ 16] used 4×8 configuration, we adopt 8×4 grid for LLM fine-tuning phase until reaching at least 90% accuracy and RL training phase with calibrated guidance for 1000 episodes in the 4×4 and 8×8 environments.
After every 50 episodes, PPO updates are performed using clipped policy gradients, value loss, and entropy regularization. This exhibits how uncertainty-calibrated LLMs can guide RL agents, with a smooth transition from LLM guidance to learned policy control as training progresses. 
Figure 2: Training performance comparison showing average reward. Our model shows a significantly higher and stable reward trajectory than other baselines. Traditional RL methods like Q-Learning, DQN, and unguided RL show slower learning and lower final rewards. Uncalibrated LLM improves performance but remains less effective than calibrated version. 
Figure 3: Model comparison based on reward, success rate, steps, and AUC. Our calibrated model achieves the highest scores across all metrics, indicating superior performance. The uncalibrated LLM performs better than traditional methods but falls short of the calibrated model due to its lack of uncertainty awareness.
III-B Environment and Reward Structure
We evaluate our proposed ULPS framework on MiniGrid-UnlockPickup [ 3] , a sparse-reward benchmark for sequential multitask RL. The LLM oracle is trained in an 8×4 environment, while RL is evaluated on 4×4 and 8×8 settings [ 6] . The UnlockPickup environment consists of picking up a key, unlocking a door, and reaching the goal. The observation space includes a 7×7 view, and the action space A t A_{t} is discrete with five actions: 0 (turn left), 1 (turn right), 2 (move forward), 3 (pick up), and 5 (toggle). The key, door, and goal are located at ( w − 2 , 1 ) (w-2,1) , ( w − 2 , h − 2 ) (w-2,h-2) , and ( w − 1 , h − 2 ) (w-1,h-2) respectively, where w w and h h denote width and height of the environment. Rewards are based on task performance. The reward function assigns 0.5 for key pickup, 0.5 for door opening, and 0.2 for reaching the goal, with a penalty of − 0.02 -0.02 for invalid actions. An additional bonus is added when the goal is reached, where AdditionalBonus = 1 − ( stepscount / maxsteps ) \textit{AdditionalBonus}=1-(\textit{stepscount}/\textit{maxsteps}) . The formula for reward is given by Reward = KeyPickup + OpenDoor + ReachGoal + AdditionalBonus + CumulativePenalty \textit{Reward}=\textit{KeyPickup}+\textit{OpenDoor}+\textit{ReachGoal}+\textit{AdditionalBonus}+\textit{CumulativePenalty} .
The environment ends either upon reaching the goal or exceeding maximum steps (50). This setup shows there is a balanced challenge for exploration and execution of the sequential tasks. The textual prompt format provides a description of the environment at each step with agent locations, orientations, and goals. All experiments were carried out on a fixed random seed (42).
TABLE I: Comparison of model calibration and performance metrics. The proposed model achieves higher fine-tuning accuracy, lower bs, and perfect da, indicating superior prediction confidence and reliability compared to prior work.
III-C Results
Our model's performance for a 4×4 Mini-grid environment has achieved an accuracy of 99.17% after fine-tuning, outperforming [ 16] , which has 90% accuracy for 21,500 states as shown in Table I. This accuracy measures how often our fine-tuned LLM picks the same action as the oracle for a given state.
We employed three standard metrics. Brier Score (BS) measures probabilistic prediction accuracy: B  S = 1 N  ∑ i = 1 N ( p i − y i ) 2 BS=\frac{1}{N}\sum_{i=1}^{N}(p_{i}-y_{i})^{2} , where p i p_{i} is the predicted probability and y i y_{i} is the actual outcome. Expected Calibration Error (ECE) quantifies calibration: E  C  E = ∑ m = 1 M | B m | N  | a  c  c  ( B m ) − c  o  n  f  ( B m ) | ECE=\sum_{m=1}^{M}\frac{|B_{m}|}{N}|acc(B_{m})-conf(B_{m})| , where B m B_{m} represents samples in bin m m . Discrimination analysis (DA) is measured via AUC-ROC: A  U  C = ∫ 0 1 TPR  ( FPR − 1  ( t ) )  𝑑 t AUC=\int_{0}^{1}\mbox{TPR}(\mbox{FPR}^{-1}(t)),dt where TPR and FPR are true and false positive rates, respectively. The evaluation framework uses ECE with a 10-bin calculation, and DA with a 0.5 threshold.
Our model achieved superior performance with BS of 0.06 (vs. 0.20), DA of 1.0 (vs. 0.8), and ECE of 0.20, indicating better-aligned probabilistic predictions, reduced overconfidence, while higher DA shows model's ability to separate correct and incorrect action predictions.
The experiments performed on different minigrid environment sizes using calibrated LLM, uncalibrated LLM, unguided RL, linear RL, Q-Learning, and DQN have shown several important insights, as shown in Table II and Fig. 2. Our proposed model (calibrated LLM in a 4×4 environment) significantly outperforms all other approaches with the highest reward Area Under the Curve (AUC) of 2055.08 and the least average steps to the goal (7.24). The average reward is higher than in other experiments, while the total steps taken are only 7286 for 1000 episodes. Comparatively, the 4×4 uncalibrated LLM showed slightly reduced performance (94.00% success, 1706.43 AUC, 18.39 steps), while traditional RL methods exhibited greater limitations: Q-Learning attained 82.40% success and 16.19 steps (1515.71 AUC), and DQN managed 11.60% success with 31.66 steps (317.46 AUC). The 4×4 Unguided RL baseline performed poorest (5.90% success, 35.54 steps, 221.31 AUC), emphasizing the value of guided exploration.
TABLE II: Ablation study and performance comparison of various rl methods in 4×4 and 8×8 MiniGrid UnlockPickup environments. The proposed ULPS model outperforms traditional rl baselines, including q-learning, dqn, and uncalibrated llm variants, demonstrating superior sample efficiency, reward accumulation, and task success.
The reward AUC is computed as AUC reward ≈ ∑ i = 1 n − 1 ( ( avg_reward i + avg_reward i + 1 ) / 2 ) ⋅ ( ep i + 1 − ep i ) \textit{AUC}{\textit{reward}}\approx\sum{i=1}^{n-1}\left((\textit{avg_reward}{i}+\textit{avg_reward}{i+1})/{2}\right)\cdot(\textit{ep}{i+1}-\textit{ep}{i}) . Success rate is defined as ∑ i = 1 n goal i / n × 100 {\sum_{i=1}^{n}\textit{goal}{i}}/{n}\times 100 , average steps to goal as ∑ i = 1 m length i / m {\sum{i=1}^{m}\textit{length}{i}}/{m} , and average reward as ∑ i = 1 n reward i / n {\sum{i=1}^{n}\textit{reward}{i}}/{n} . Total wins and total steps are simply ∑ i = 1 n goal i \sum{i=1}^{n}\textit{goal}{i} and ∑ i = 1 n length i \sum{i=1}^{n}\textit{length}{i} , respectively. The goal i ∈ { 0 , 1 } \textit{goal}{i}\in{0,1} indicates whether the goal was reached in episode i i , n n is the total number of episodes, m m is the number of successful episodes ( goal i = 1 \textit{goal}{i}=1 ), length i \textit{length}{i} is the number of steps taken in episode i i , reward i \textit{reward}{i} is the reward received in episode i i , and ep i \textit{ep}{i} is the episode index.
As depicted in Table III, all models reached a near perfect success rate and usually converged in about 7 steps, except for a dropout rate of 0.05 and 4 forward passes. The highest reward (2055.88) came from a dropout rate of 0.2 with 12 forward passes. However, using a dropout rate of 0.1, 8 forward passes gave nearly the same reward (2055.08) while being computationally cheaper. This means that although larger settings can push performance slightly higher, more moderate settings often provide a better balance between accuracy and efficiency.
TABLE III: The effects of varying dropout rates and forward passes. The metrics evaluated include average steps to goal, and reward auc, providing how these hyperparameters influence model's ability.
III-D Ablation Study
When comparing PPO, uncalibrated LLMs, and our combined model in Table II, clear differences emerge. In 4×4 environment, PPO alone achieved 74.9% success, but it needed many steps, while uncalibrated LLM reached 94%, but was still inefficient. Our RL + LLM model achieved 99.9% success with fewer steps. In an 8×8 environment, PPO alone failed almost completely, and the uncalibrated LLM reached 72.3%, while our model achieved 99.7% success with much lower cost. This shows that combining both components with uncertainty awareness works better than using either one alone.
III-E Discussion
Our experimental results demonstrate fundamental advances in LLM-guided RL. The uncertainty-aware calibration mechanism is critical for achieving high reliability and exploration efficiency. While both calibrated models (4×4, 8×8) achieved remarkable success rates exceeding 99%, the 4×4 model's lower step count (7.24 vs 15.37) reveals that proper confidence calibration enables more optimal path planning and successfully mitigates over-exploration problem common in traditional approaches. Comparative analysis exposes clear limitations in existing methods. Unguided RL and DQN exhibited 4 to 5 times higher steps despite lower success rates. This performance hierarchy, visually confirmed in a radar chart (Fig. 3), strongly supports our hypothesis that LLM guidance provides crucial priors for efficient exploration.
III-F Comparative Analysis of Calibrated LLM Performance
III-F 1 MC Dropout Computational Cost
Our uncertainty estimation requires 8 forward passes through the BERT model per action. This introduces an 8 × \times computational overhead compared to single-pass inference, showing notable per-action cost increase.
III-F 2 Sample Efficiency vs Computational Trade-off
The calibrated LLM with MC dropout increases per-action computation but requires only 7,286 total steps compared to 49,147 steps for unguided RL (86% reduction in environment interactions). This suggests that even if there is a higher per-step computational cost, overall training efficiency is improved due to the reduced exploration.
III-F 3 Environment Complexity Scaling
While in the 8×8 environment, it requires 15.37 steps with 99.70% success, and in the 4×4 environment, it achieves 99.90% success with 7.24 steps, the increase in average steps for the larger environment shows that computational overhead scales approximately linearly with environment complexity.
III-F 4 Comparison with 4×4 Linear RL using PPO
Linear RL shows reward AUC 1865.57 and requires nearly twice as many steps (15.84 vs 7.24). The main problem is it starts with full LLM control and gradually hands control to the agent as training progresses, while our context-aware calibration provides the right support when it's needed.
III-F 5 Comparison with 4×4 Uncalibrated LLM
Since MC dropout is not used, the uncalibrated model often shows overconfidence in ambiguous situations and under-confident guidance in straightforward situations, leading to nearly double the average steps to the goal (18.39 vs 7.24). This difference supports our main idea that accurately estimating confidence is also as important as making correct predictions for successful LLM-guided RL.
III-F 6 Comparison with 4×4 Unguided RL using PPO
Unguided RL performs poorly with a minimal reward AUC of 221.31 and a success rate of 5.90%. This is due to the difficulty of learning in sparse-reward environments with strictly ordered subtasks, where the uninformed exploration leads to inefficient and penalized action sequences.
III-F 7 Comparison with 4×4 Q-Learning using Group Relative Policy Optimization (GRPO)
Q-learning with GRPO [ 15] shows a reward AUC of 1515.71 and a success rate of 82.40%. It lacks consistency due to its reliance on a Q-table and the Markov property, struggling with temporal dependencies and linguistic understanding in sequential tasks which results in poor policy development, requiring nearly double the steps (16.19 vs. 7.24), highlighting the benefit of combining semantic reasoning with RL.
III-F 8 Comparison with DQN using GRPO
DQN with GRPO has reward AUC of 317.46 and a success rate of 11.60%, showing it struggles with sequential tasks. Although we implemented improvements like Double DQN, dueling networks, and prioritized replay, it needs more training data for ordered task. Without guidance, it wastes time exploring unhelpful areas, explaining why it takes 47,873 steps but succeeds only 116 times.
IV Conclusion
In this work, we introduced ULPS, a unified framework that integrates calibrated language-model priors, symbolic A* guidance, and uncertainty-aware policy for sparse rewards RL, which provides reliable, interpretable action suggestions that enhance exploration while preserving the adaptability of PPO. Our entropy-based blending mechanism ensures stable training and mitigates over-reliance on uncertain LLM outputs. Empirical results on the MiniGrid UnlockPickup benchmark demonstrate that ULPS improves success rate, sample efficiency, and reward AUC compared with unguided, uncalibrated, Q-learning, and DQN. The calibrated LLM component improves symbolic action accuracy by more than 9% after fine-tuning and consistently accelerates convergence across training regimes. These findings highlight the effectiveness of combining symbolic planning, pretrained language priors, and uncertainty estimation in a principled RL pipeline. Looking forward, our framework exhibits strong potential for scaling to partially observable scenarios and multi-agent coordination environments. Further exploration of hierarchical prompting, multimodal representations, and tighter integration between planning and language-model reasoning represents a promising direction for advancing robust, generalizable RL systems.
Acknowledgment
This work was supported by the National Science Foundation under Grant No. #2346643, the U.S. Department of Defense under Award No. #FA9550-23-1-0495, and the U.S. Department of Education under Grant No. P116Z240151. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation, the U.S. Department of Defense, or the U.S. Department of Education.
References
[1] Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, et al. (2022) Constitutional ai: harmlessness from ai feedback. arXiv preprint arXiv:2212.08073. Cited by: §I.
[2] S. Casper, X. Davies, C. Shia, T. K. Gibert, J. Scherrer, J. Rando, et al. (2023) Open problems and fundamental limitations of reinforcement learning from human feedback. arXiv preprint arXiv:2307.15217. Cited by: §I.
[3] M. Chevalier-Boisvert, B. Dai, M. Towers, R. de Lazcano, L. Willems, S. Lahlou, et al. (2023) Minigrid & miniworld: modular & customizable reinforcement learning environments for goal-oriented tasks. ArXiv abs/2306.13831. Cited by: § II-A, § III-B.
[4] P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, and D. Amodei (2017) Deep reinforcement learning from human preferences. ArXiv abs/1706.03741. Cited by: §I.
[5] Y. Du, O. Watkins, Z. Wang, C. Colas, T. Darrell, P. Abbeel, et al. (2023) Guiding pretraining in reinforcement learning with large language models. In International Conference on Machine Learning, Cited by: §I.
[6] Farama Foundation (2025) MiniGrid-UnlockPickup-v0 Environment. Note: MiniGrid Documentation Cited by: § III-B.
[7] Y. Gal and Z. Ghahramani (2015) Dropout as a bayesian approximation: representing model uncertainty in deep learning. In International Conference on Machine Learning, Cited by: §I.
[8] Y. Guo, J. Choi, M. Moczulski, S. Feng, S. Bengio, M. Norouzi, et al. (2020) Memory based trajectory-conditioned policies for learning from sparse rewards. In Neural Information Processing Systems, Cited by: §I.
[9] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine (2018) Soft actor-critic: off-policy maximum entropy deep reinforcement learning with a stochastic actor. ArXiv abs/1801.01290. Cited by: §I.
[10] W. Huang, P. Abbeel, D. Pathak, and I. Mordatch (2022) Language models as zero-shot planners: extracting actionable knowledge for embodied agents. ArXiv abs/2201.07207. Cited by: §I.
[11] M. Kwon, S. M. Xie, K. Bullard, and D. Sadigh (2023) Reward design with language models. ArXiv abs/2303.00001. Cited by: §I.
[12] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wierstra, et al. (2013) Playing atari with deep reinforcement learning. ArXiv abs/1312.5602. Cited by: §I.
[13] T. Salimans and R. J. Chen (2018) Learning montezuma's revenge from a single demonstration. ArXiv abs/1812.03381. Cited by: §I.
[14] Y. Shalev, A. Feder, and A. Goldstein (2024) Distributional reasoning in llms: parallel reasoning processes in multi-hop reasoning. ArXiv abs/2406.13858. Cited by: §I.
[15] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, et al. (2024) DeepSeekMath: pushing the limits of mathematical reasoning in open language models. ArXiv abs/2402.03300. Cited by: § III-F 7.
[16] M. Shoaeinaeini and B. Harrison (2024) Guiding reinforcement learning using uncertainty-aware large language models. 2025 IEEE 7th International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (TPS-ISA), pp. 363–371. Cited by: §I, §I, § III-A, § III-C, TABLE I, TABLE I.
[17] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche, et al. (2016) Mastering the game of go with deep neural networks and tree search. Nature 529, pp. 484–489. Cited by: §I.
[18] F. Sun, N. Li, K. Wang, and L. Goette (2025) Large language models are overconfident and amplify human bias. ArXiv abs/2505.02151. Cited by: §I.
[19] K. Zhou, J. D. Hwang, X. Ren, and M. Sap (2024) Relying on the unreliable: the impact of language models' reluctance to express uncertainty. ArXiv abs/2401.06730. Cited by: §I.
Experimental support, please view the build logs for errors. Generated by L A T E xml[LOGO]
.
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" ( ) button, located in the page header.
Tip: You can select the relevant text first, to include it in your report.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.
We gratefully acknowledge support from our major funders, member institutions, , and all contributors.
About
· Help
· Contact
· Subscribe
· Copyright
· Privacy
· Accessibility
· Operational Status (opens in new tab)
Major funding support from
   