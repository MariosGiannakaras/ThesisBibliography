> Source: https://aaltodoc.aalto.fi/bitstreams/ad6a569f-e242-4e6f-8976-61a242efe719/download

Master’s Programme in Master’s Programme in ICT Innovation 
Generalizing Offline Reinforcement Learning to Unseen Dynamics Parameters with Synthetic Data 
Boxu Liu 
Master’s Thesis 2024
© 2024 
This work is licensed under a Creative Commons “Attribution-NonCommercial-ShareAlike 4.0 Interna-tional” license.
Author Boxu Liu 
Title Generalizing Offline Reinforcement Learning to Unseen Dynamics Parameters with Synthetic Data 
Degree programme Master’s Programme in ICT Innovation 
Major Cloud and Network Infrastructures 
Supervisor Prof. Joni Pajarinen 
Advisors Dr Aidan Scannell, Jatan Shrestha 
Date 23 August 2024 Number of pages 37+2 Language English 
Abstract Reinforcement Learning (RL) has achieved remarkable performance in real-world industrial applications like robotics and logistics. RL often struggles with adapting to diverse and changing contexts due to limited training data and poor generalization capabilities. Collecting sufficient real-world data is both costly and time-consuming, which hampers the development of adaptable RL systems. To alleviate this problem, Context-Aware RL algorithms address these issues by incorporating contextual information. However, their ability to generalize to out-of-distribution (OOD) scenarios remains limited. On the other hand, diffusion models, known for their strong generative capabilities, offer a promising solution to enhance RL. In this thesis, we propose a method that leverages diffusion models to improve the sample efficiency and generalization ability of RL agents. We collect real data from online RL agents training and we train diffusion models on the real data with varying contexts. We use specific contexts to guide the diffusion model in generating transitions. We use these synthetic transitions to train offline RL agents, enabling them to perform effectively across diverse and unseen environments. Experimental results demonstrate that our method improves RL performance in OOD contexts while maintaining performance within in-distribution scenarios. 
Keywords Reinforcement Learning, Diffusion Models, Synthetic Experience Replay, Sample-Efficient Learning, Generalization, Dynamic Environments
Preface 
I would like to express my deepest gratitude to Professor Joni Pajarinen for providing me with such a precious opportunity. Despite not being a student specializing in machine learning, Professor Pajarinen kindly accepted me and offered immense support throughout my research. 
I am sincerely thankful to my thesis advisors, Dr. Aidan Scannell, and Jatan Shrestha, for their invaluable advice and guidance. In particular, I would like to especially thank Dr. Aidan Scannell, who patiently guided me onto the correct path. 
My heartfelt thanks go to all my friends who have always been by my side. Some unfortunate events occurred during my thesis, but I managed to overcome them with the collective help and companionship of my friends. 
I am also grateful to Prof. Jukka Manner. As my major professor, he provided significant assistance with my course selections and helped me settle my thesis topic. 
Completing this thesis has taught me a great deal, especially as a student not majoring in machine learning. I am truly grateful for this opportunity, which has led me onto a completely different path. Thank you to all the people who have helped me throughout this journey. It will remain one of the most beautiful and unforgettable memories of my life. 
Otaniemi, 23 September 2024 
Boxu Liu 
4
Contents 
Abstract 3 
Preface 4 
Contents 5 
Symbols and abbreviations 7 
1 Introduction 9 
2 Background 11 
2.1 Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . 11 
2.2 Soft Actor-Critic (SAC) . . . . . . . . . . . . . . . . . . . . . . . . 12 
2.3 Context-Aware Reinforcement Learning . . . . . . . . . . . . . . . 12 
2.4 Offline Reinforcement Learning . . . . . . . . . . . . . . . . . . . 13 
2.5 Twin Delayed Deep Deterministic Policy Gradient with Behavior Cloning (TD3-BC) . . . . . . . . . . . . . . . . . . . . . . . . . . 14 
2.6 Diffusion Models . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 
3 Related Work 17 
3.1 Data Augmentation . . . . . . . . . . . . . . . . . . . . . . . . . . 17 
3.2 Synthetic Data Generation . . . . . . . . . . . . . . . . . . . . . . 17 
4 Methods 19 
4.1 Pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 
4.2 Data collection and Processing . . . . . . . . . . . . . . . . . . . . 19 
4.3 Model Architecture and Training . . . . . . . . . . . . . . . . . . . 20 
5
4.4 Model Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 
5 Results 25 
5.1 Training with Synthetic Data Compared to Training without Synthetic Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 
5.2 OOD Performance . . . . . . . . . . . . . . . . . . . . . . . . . . 27 
5.3 Varying number of episodes of each context . . . . . . . . . . . . . 28 
6 Potential Industrial Applications 30 
6.1 Robotic Control and Automation . . . . . . . . . . . . . . . . . . . 30 
6.2 Fault Diagnosis and Maintenance . . . . . . . . . . . . . . . . . . . 30 
6.3 Logistics and Warehouse Optimization . . . . . . . . . . . . . . . . 30 
7 Conclusion and Limitation 32 
References 33 
A Hyper Parameters of SAC Agent 38 
B Hyper Parameters of Diffusion model 39 
6
Symbols and abbreviations 
Symbols 
J Objective function L Loss function D Dataset π Policy s State a Action s′ Next state c Context r Reward γ Discount factor θ Neural network parameters x Diffusion model input ϵ Noise N Gaussian distribution I Identity matrix µ Distribution mean βt Variance schedule H Entropy α Temperature factor 
Operators 
E expectation∑︁ sum 
7
Abbreviations 
RL Reinforcement Learning MDP Markov Decision Process SAC Soft Actor-Critic CARL Context-Aware Reinforcement Learning CQL Conservative Q-learning TD3 Twin Delayed Deep Deterministic Policy Gradient BC Behavior Cloning RB Replay Buffer OOD Out-Of-Distribution DDPG Deep Deterministic Policy Gradient SynthER Synthetic Experience Replay MMD Maximum Mean Discrepancy RAD Reinforcement Learning with Augmented Data UCB Upper Confidence Bound algorithm DrAC Data-regularized Actor-Critic SODA SOft Data Augmentation EGAN Enhanced Generative Adversarial Network GAN Generative Adversarial Network VAE Variational Auto Encoders AGVs Autonomous Guided Vehicles 
8
1 Introduction 
Reinforcement Learning (RL) is an algorithm that explores the environment and determines the optimal actions to maximize cumulative rewards [1]. Over the past few decades, RL has achieved remarkable performance in multiple areas, including games, and autonomous driving. 
Significant progress has been made in improving sample efficiency to achieve optimal performance with limited data. However, in real-world industrial applications such as robotics, logistics, and energy management, reinforcement learning (RL) often struggles to adapt to diverse and changing contexts. Meanwhile, collecting sufficient real-world data is costly and time-consuming. Traditional RL methods struggle when faced with changes in environmental contexts, leading to poor generalization across different scenarios [7]. Some research tried to address this issue by introducing Context-Aware RL algorithms, which incorporate contextual information as part of the input, making the learning process more adaptable to different environments within the training distribution [7]. Nevertheless, adapting to contexts outside the training distribution remains challenging, and sample efficiency is still low due to limited context data in training. 
Diffusion models have emerged as state-of-the-art generative models, used in areas such as robotics for dynamics modeling [8]. With their strong expressive power, diffusion models can generate high-quality data for RL agents, enhancing training. Furthermore, their interpolation ability provides better generalization across contexts [9]. 
In this paper, we seek to answer the questions: 
 Does incorporating synthetic data for unseen pole lengths in contextual reinforcement learning, where pole length serves as the context, improve an agent’s generalization capability compared to training solely on real data? 
 Does training offline RL agents with synthetic data improve their out-of-distribution (OOD) performance compared to using only real data? How does the performance change as test contexts (OOD) deviate further from training contexts in-distribution (ID)? 
To answer these questions, we propose a method that leverages diffusion models to improve RL sample efficiency by fully utilizing explored data. First, we train a diffusion model on explored data with different contexts as input. Then, we guide the diffusion model by contexts and make it generate synthetic data. We use the synthetic data to train offline RL agents for testing.
Figure 1: Our method enables the agent to adapt to environments beyond the explored environment. Firstly, We collect transitions from agents’ interactions with multiple environments. Then we use these collected data to train a diffusion model with contexts and make it generate synthetic data for any context. Finally, synthetic data can be used for RL agent training and help the agent adapt to different environments. 
To summarize the contributions of this thesis: 
 We propose a method that utilizes diffusion models to generate synthetic transitions for unseen contexts. 
 We demonstrate that diffusion models can generate high-quality data suitable for reinforcement learning training across different contexts. 
 We show that diffusion models can help reinforcement learning algorithms adapt to different contexts compared with the Context-Aware method. 
The remainder of this thesis is organized as follows: 
Section 2 introduces the necessary background and related work. Section 3 describes the methods used in this study, including data collection, model training, and evaluation. Section 4 presents the results of our experiments, followed by a detailed discussion in Section 5. Section 6 introduced the potential future industrial applications. Finally, Section 7 concludes the thesis and outlines potential future work. 
10
2 Background 
In this section, we introduce the background knowledge related to this thesis. Firstly, we introduce the basic concept and type of RL. Then we extend it to SAC and CARL, Offline RL, and TD3-BC. Moreover, we introduce how the diffusion model and conditioned diffusion model work. Finally, we introduce SynthER which inspires this thesis. 
2.1 Reinforcement Learning 
Reinforcement Learning (RL) is a machine learning paradigm that focuses on training agents to make sequential decisions by interacting with an environment [1]. Unlike supervised learning, where an agent learns from labeled data, RL learns through trial and is guided by a reward signal. The agent aims to learn a policy that maximizes the cumulative reward over time by choosing actions based on the current state of the environment. 
In a typical RL setup, the problem is formulated as a Markov Decision Process (MDP), represented by the tuple (S,A, P, R, γ) [1]. Here, S is the state space, A is the action space, P (s′|s, a) is the transition probability from state s to s′ given action a, R(s, a) is the reward function, and γ ∈ [0, 1) is the discount factor that determines the importance of future rewards and make sure the solution to converge. The agent’s objective is to learn an optimal policy π(a|s) that maximizes the expected cumulative reward, defined as [1]: 
J (π) = Eπ 
[︄ ∞∑︂ t=0 
γtr(st,at) 
]︄ , (1) 
To solve this optimization problem, RL algorithms can be broadly categorized into value-based, policy-based, and actor-critic methods [44]. Value-based methods, such as Q-learning, focus on estimating the value of each state-action pair and derive the policy by selecting actions with the highest value [14]. Policy-based methods, such as REINFORCE, directly optimize the policy by updating it in the direction that increases the expected reward [44]. Actor-critic methods, such as Soft Actor-Critic (SAC), combine the strengths of both value-based and policy-based approaches by using an actor to update a critic to evaluate the actions taken [35]. 
In recent years, RL has achieved remarkable success in a variety of complex tasks. However, RL also faces several challenges, such as sample inefficiency, explorationexploitation trade-offs, and instability during training [11]. To address these issues, various techniques, such as experience replay [2], entropy regularization [3], and reward shaping [4], have been proposed, enhancing RL’s ability to solve increasingly complex problems. 
11
Overall, RL provides a powerful framework for sequential decision-making, allowing agents to automatically learn complex behaviors and adapt to dynamic environments. 
2.2 Soft Actor-Critic (SAC) 
Soft Actor-Critic (SAC) is an off-policy, model-free, reinforcement learning algorithm that combines both policy improvement and entropy maximization to achieve highperformance learning in continuous action spaces [35]. SAC was introduced to address some of the limitations in traditional reinforcement learning algorithms, such as instability and low sample efficiency, particularly in high-dimensional environments [18]. 
SAC operates within the actor-critic framework, where the actor is responsible for selecting actions based on a learned policy, and the critic estimates the value function to evaluate the quality of actions. Unlike conventional algorithms, SAC incorporates a soft value function that includes an entropy term in the objective. The entropy term encourages exploration by favoring stochastic policies, allowing the agent to explore more diverse actions rather than prematurely converging to deterministic policies [15]. This entropy regularization is controlled by a temperature parameter, which balances exploration and exploitation [15]. 
The objective function of SAC maximizes both the expected cumulative reward and the entropy of the policy. Formally, the soft Q-function is defined as [35]: 
Qπ(s, a) = Eπ 
[︄ ∞∑︂ t=0 
γt (r(st,at) + αH(π(·|st))) 
]︄ , (2) 
where α is the temperature parameter that determines the trade-off between reward and entropy, r(st, at) is the reward function, and H(π(·|st)) represents the entropy of the policy at state st. 
SAC has demonstrated significant performance improvements over traditional actorcritic algorithms, particularly in terms of sample efficiency and stability [35]. This is largely due to its entropy-driven exploration strategy, which helps prevent the policy from becoming overly deterministic too early, thereby avoiding poor local optima. SAC has been widely used in complex robotic control tasks, autonomous driving, and other applications requiring robust and efficient learning in continuous action spaces [19]. 
2.3 Context-Aware Reinforcement Learning 
Context-Aware Reinforcement Learning (CARL) is an extension of traditional reinforcement learning (RL) that aims to improve an agent’s adaptability and performance 
12
by incorporating additional contextual information into the decision-making process [7]. In standard RL, an agent interacts with an environment to learn a policy that maximizes cumulative rewards. However, traditional RL often assumes a fixed environment or ignores external factors that could influence the agent’s performance. CARL addresses this limitation by considering context as an essential part of the environment, enabling the agent to adapt its policy based on varying external conditions [7]. 
In CARL, context is typically defined as any auxiliary information about the environment that is relevant to the agent’s decision-making process but is not directly part of the observable state [12]. This contextual information can include environmental variables, external conditions, or latent factors that impact the agent’s reward or state transitions. By utilizing context, CARL allows the agent to make more informed decisions, particularly in environments where conditions may change over time or differ across scenarios. 
The core idea behind CARL is to learn a context-dependent policy π(a|s, c), where s represents the state, a the action, and c the context [7]. The Context-Aware policy enables the agent to adjust its actions based on both the state and the context, leading to more flexible and adaptive behavior. The value function in CARL can be expressed as [7]: 
J (π) = E 
[︄ ∞∑︂ t=0 
γtr(st, at, c) 
]︄ (3) 
Recent advances in CARL have focused on effective methods for context representation, efficient context sampling strategies, and techniques to integrate context into deep RL algorithms. These developments make CARL a promising approach for tackling complex real-world tasks where environmental variability plays a significant role [12]. 
2.4 Offline Reinforcement Learning 
Offline RL is a variant of traditional reinforcement learning where the agent learns solely from a fixed dataset collected from previous interactions with the environment, without any additional online interaction during training [41]. This setting is particularly useful in scenarios where real-time data collection is expensive, time-consuming, or risky, such as healthcare, autonomous driving, and robotics [6, 41]. 
In a typical RL setting, an agent learns by interacting with the environment in real-time, which allows the agent to gather new data and refine its policy. However, in Offline RL, the agent must rely on a static dataset D = {(s, a, r, s′)}, where s and s′ represent the states before and after taking action a, and r is the reward obtained. The goal of Offline RL is to learn an optimal policy π(a|s) that maximizes the expected cumulative reward using only the given dataset, without any additional exploration [37, 6]. 
13
One of the main challenges in Offline RL is the issue of distributional shift, which arises because the data in D may not cover all possible states and actions, particularly those that could be relevant for an optimal policy. When the agent encounters states or actions that are not well represented in the dataset, the policy learned during offline training may perform poorly in deployment. This distributional shift can lead to extrapolation errors, where the model makes overly optimistic estimates for unseen state-action pairs, resulting in suboptimal policies [40, 39]. 
Offline RL has shown promising results in fields where data is plentiful but exploration is costly or impractical, such as medical decision-making, recommendation systems, and industrial control. By enabling agents to leverage pre-collected datasets, Offline RL offers a viable path toward deploying reinforcement learning in real-world applications that demand safety and efficiency [38, 6]. 
2.5 Twin Delayed Deep Deterministic Policy Gradient with Be-havior Cloning (TD3-BC) 
Twin Delayed Deep Deterministic Policy Gradient with Behavior Cloning (TD3-BC) is an extension of the Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm [18], specifically designed to improve the performance of Offline RL by incorporating behavior cloning techniques [20]. TD3 is a popular reinforcement learning algorithm for continuous control tasks, which builds upon the Deep Deterministic Policy Gradient (DDPG) framework [21] but addresses several of its limitations, such as overestimation bias and sensitivity to hyperparameters [18]. 
TD3 improves upon DDPG by introducing three key components: clipped double Q-learning, delayed policy updates, and target policy smoothing [18]. Clipped double Q-learning mitigates the overestimation bias by employing two Q-networks and taking the minimum of their estimates to update the policy [18]. Delayed policy updates reduce the frequency of policy updates relative to Q-function updates, providing a more stable learning process. Target policy smoothing, which applies noise to target actions, helps to prevent the policy from exploiting narrow peaks in the Q-function, thus enhancing robustness [18]. 
While TD3 has been shown to perform well in online settings, it often struggles in the Offline RL setting, where the agent must learn solely from a static dataset without additional interaction with the environment [6]. This limitation arises because traditional TD3 does not account for the distributional shift between the static dataset and the optimal policy, leading to poor generalization when the learned policy deviates significantly from the behavior policy that generated the data [6]. 
To address this issue, TD3-BC incorporates behavior cloning (BC) into the TD3 framework, encouraging the agent to mimic actions from the dataset [20]. Behavior 
14
cloning helps to regularize the policy by minimizing the deviation from the behavior policy, which mitigates the risks associated with distributional shifts [28]. Specifically, TD3-BC introduces an additional loss term that penalizes the difference between the agent’s actions and the actions observed in the dataset. The resulting objective function is defined as [20]: 
LTD3-BC = LTD3 + λ · E(s,a)∼D [︁ ∥π(s)− a∥2 
]︁ , (4) 
where LTD3 is the original TD3 loss, π(s) represents the action chosen by the policy, a is the action in the dataset, and λ is a hyperparameter that balances the behavior cloning loss and the original TD3 loss [20]. 
TD3-BC has demonstrated superior performance in various Offline RL tasks, particularly in settings where limited data or exploration is costly [20]. By combining the strengths of TD3 with behavior cloning, TD3-BC provides a robust approach for leveraging pre-collected datasets to learn effective policies in complex continuous action environments. 
2.6 Diffusion Models 
Diffusion models are a class of probabilistic generative models that have gained significant attention recently due to their impressive performance in high-quality image and data generation tasks [16, 8]. Inspired by non-equilibrium thermodynamics [16], diffusion models generate data by simulating a gradual noise reduction process, starting from pure noise and refining the noise to obtain structured, meaningful outputs. This process is typically formulated as a Markov chain that iteratively denoises a data sample, making diffusion models suitable for generating high-dimensional, complex data. 
The diffusion process consists of two primary phases: the forward process and the reverse process [8]. In the forward process, noise is incrementally added to the data over several steps, transforming the real data distribution into a standard Gaussian distribution. Given a data point x0, the forward process produces a series of noisy samples x1,x2, . . . ,xT by gradually adding Gaussian noise. This process can be mathematically expressed as [8]: 
q(xt|xt−1) = N (xt; √︁ 1− βtxt−1, βtI), (5) 
where βt is a variance schedule that controls the amount of noise added at each step [8]. 
The reverse process, on the other hand, learns to gradually denoise the noisy data back to the real data distribution. This is achieved by parameterizing the reverse process as a neural network pθ(xt−1|xt) trained to predict the real data distribution given a noisy 
15
sample. The reverse diffusion steps are defined as [8]: 
pθ(xt−1|xt) = N (xt−1;µθ(xt, t),Σθ(xt, t)), (6) 
where µθ and Σθ are the mean and variance parameters learned by the model [8]. 
The training objective for diffusion models typically involves minimizing a loss function. A commonly used objective is the mean squared error (MSE) between the true noise ϵ and the predicted noise ϵθ [8]: 
Lsimple(θ) = Ex0,ϵ,t 
[︁ ∥ϵ− ϵθ(xt, t)∥2 
]︁ (7) 
Where ϵ represents the Gaussian noise added to the data. This loss function guides the model to learn the denoising process. 
One of the key advantages of diffusion models is their ability to generate high-quality samples without adversarial training, which is often required in GANs (Generative Adversarial Networks) but can be unstable and prone to mode collapse [17, 29]. Diffusion models are also highly flexible and can be conditioned on various forms of input data, making them applicable to a wide range of tasks, including image synthesis [30], text-to-image generation [31], and data augmentation for reinforcement learning [32]. 
In recent years, diffusion models have demonstrated state-of-the-art results in image generation benchmarks, rivaling or even surpassing GANs in certain domains [30, 33]. Their robustness and scalability make them an attractive choice for complex data generation tasks in machine learning and artificial intelligence. 
16
3 Related Work 
The application of reinforcement learning (RL) in real-world scenarios often faces challenges related to generalization, data efficiency, and adaptability to diverse environments. This section reviews prior works that inform our approach, particularly in using data augmentation and synthetic data generation to enhance generalization and efficiency. 
3.1 Data Augmentation 
RL agents are trained with their explored data, while the distribution of the explored data usually differs from the real environments. It leads to RL agents struggling to generalize to unseen environments. 
Previous research, especially for visual RL tasks, tried to mitigate this problem by implementing data augmentation of observations. e.g., RAD [26] uses grid search and performs a comparative analysis of various data augmentation operators, demonstrating that each operator offers distinct advantages for reinforcement learning tasks. UCB-DrAC [27] introduces an approach for automatic data augmentation by framing data augmentation operators as an action space and leveraging methods like UCB to dynamically select the most effective operator during training. 
As additional factors of variation are introduced during training, the optimization process becomes more complex, often leading to reduced sample efficiency and increased instability in training. SODA [23] decouples augmentation from policy learning and significantly increases sample efficiency and stability of RL training with data augmentation. 
3.2 Synthetic Data Generation 
Data augmentation partially solves the problem of generalization and sample efficiency since it only expands the observations of RL training transitions. RL agents are still hard to generalize to unseen actions and rewards. Modern RL algorithms use RB (replay buffer), which decouples the policy updates and data sampling. RB makes expanding the whole transition meaningful. On the other hand, the generative model developed fast and started to able to generate high-quality data for many tasks. EGAN [24] utilizes GAN (Generative Adversarial Network) to generate transitions for RL tasks, which speeds up the early phases of the training process. B. Imre et al. explored the way to use VAE (Variational Auto Encoders) for RL data generation [25] and showed the potential of a generative model for helping RL tasks. 
17
Synthetic Experience Replay (SynthER) [34] uses Score-Text formulation of Diffusion models, which enhance the data efficiency of RL algorithms by generating synthetic experience data. SynthER employs a diffusion model to upsample the agent’s experiences. The diffusion model creates synthetic samples that resemble real experiences, effectively augmenting the replay buffer. In Offline RL, where an agent cannot gather new data during training, SynthER can generate synthetic data that expands small datasets, allowing for more robust training of larger networks. Similarly, in online settings, SynthER enables agents to maintain a higher update-to-data ratio by continually upsampling the experience data. Experimental result shows that SynthER significantly improves sample efficiency without requiring additional interactions with the environment. 
18
4 Methods 
In this section, we list the way we collect the data and how we process it. We also introduce the architecture of our model and how we train and evaluate it. 
4.1 Pipeline 
We first collect data by running an RL algorithm in an environment and train the diffusion model with collected transitions and contexts. Then we use specific context to guide diffusion to generate synthetic transitions and use the synthetic transitions to train an Offline RL algorithm. 
Figure 2: Complete Pipeline for training and evaluation of Diffusion model. 
We separate the training and testing into 4 different kinds according to their contexts range (the whole training contexts range is 0.1-0.7) and test each of them in environments with different contexts: 
 "Front" indicates that we train the model using the real transitions with the front part of contexts (0.1-0.25). 
 "Middle" indicates that we train the model using the real transitions with the middle part of contexts (0.35-0.45). 
 "Extremes" indicates that we train the model using the real transitions with the extremes parts of contexts (0.1–0.15 or 0.65–0.7). 
 "Rear" indicates that we train the model using the real transitions with the rear part of contexts (0.55-0.7). 
4.2 Data collection and Processing 
Figure 3: Data collection pipeline 
19
We conduct the data collection process using the cart pole environment of DeepMind Control Suite, a commonly used environment for continuous control tasks. We modify the pole length of environments to reflect different contexts. We uniformly sample 1000 pole lengths from 0 to 1 as the training data contexts. 
We use the Soft Actor-Critic (SAC) algorithm to explore the environment under each context, gathering episodes that comprise state, action, reward, and next state tuples along with the contextual attributes of the environment. We collect 250 episodes of each context. Each episode has 1000 transitions. We pick the episodes with the top 50 returns as our training data. 
Both states and next states contain 5 different dimensions including positions on the horizontal axis (Pos1), cosine value of pole angle (Pos2), sine value of pole angle (Pos3), velocities of the cart (Vel1), angular velocities of the pole (Vel2). 
We separate the dataset into subsets according to context which ensured an equal representation of contexts in the training datasets. 
4.3 Model Architecture and Training 
SynthER proved that diffusion model generated data is able to make the RL agent perform better in most cases [34]. While, SynthER aims to expand the dataset to its original space. Transitions generated by SynthER only need to follow the same distribution of real data [34], which means SynthER doesn’t need to intensionally guide the diffusion model. 
We want to explore how the diffusion model fits in different contexts. If we don’t intentionally guide the diffusion model, it will only generate the data that has the same distribution of context as the real data. So, we need to utilize a conditioned diffusion model trained by the data with specific contexts. This conditioning enables the diffusion model to not only recreate experiences within the context of the real data but also to generate experiences for novel context combinations. 
Figure 4: Pipeline of training the diffusion model 
We separate the training dataset into in-distribution and out-of-distribution datasets according to their contexts and separation range. After that, we use the in-distribution dataset for training and make the diffusion model train on a small batch of out-of-distribution data as OOD loss. Specifically, the diffusion model will randomly choose 
20
a scheduled step to noise and denoise the input. We take the loss of the denoising process as an indicator to help us observe the training situation. 
Evaluation Metrics for Diffusion model training: simulator score: We implement a cart pole simulator, which takes in states and actions of a transition and outputs its next state and rewards. We use this simulator to generate the next state and rewards and compare them with synthetic data (We choose 0.2, 0.4, and 0.6 as contexts). Their MSE loss indicate the actual OOD synthetic data quality. 
Figure 5: Training log of "Front" training. The simulator score and evaluation loss grow quickly after some points, while the training loss keeps going down continuously. It shows a serious overfitting problem 
Both the simulator score and evaluation grow quickly after some points while training loss still drops down. So, it shows a serious overfitting problem when training the diffusion model. We implement an early stop mechanism to mitigate it. We stop the training when OOD loss and simulator score grow high. 
We also use Optuna to optimize the hyperparameters of diffusion training. We use the combination of OOD loss and simulator score as Optuna’s optimized objective to minimize. The related hyperparameters include: 
21
Hyper parameter Value normalizer_type {’standard’, ’minmax’} diffusion.mlp_width {128, 256, 512} 
diffusion.num_layers {4, 6, 8} 
train_rl [1e-6, 1e-3] 
weight_decay [1e-4, 1e-2] 
Table 1: Optuna optimized hyperparameters 
For diffusion model sampling, the diffusion model generates transitions guided by specific contexts. Guided by contexts allows the diffusion model to generate synthetic datasets covering a broader range of contexts. 
Algorithm 1 Diffusion sampling [8] Require: θ, N 
Input: λ1, . . . , λT : increasing log SNR sequence with λ1 = λmin, λT = λmax for i = 1, . . . , N do z1 ∼ N (0, I) for t = 1, . . . , T do 
x̃t = (zt − σλtϵθ(zt, c)/αλt 
zt+1 ∼ N (µ̃λt+1 |λt, x̃t), (σ̃2 
λt+1|λt )1−v(σ2 
λt|λt+1 )v) if t < T else zT+1 = x̃t 
end for Ddiffusion += (zT+1, c) 
end for 
Evaluation Metrics for Diffusion data sampling: MMD of synthetic data and real data: We calculate the Maximum Mean Discrepancy (MMD) between synthetic data and real data as the metric to evaluate the quality of synthetic data. MMD gives us a preview of the quality of synthetic data which can be used to test the synthetic data before we test it on Offline RL. 
22
Figure 6: Maximum Mean Discrepancy between synthetic data and training data . 
As we see from the figure. MMD values grow higher when they are far from indistribution. This observation follows our intuition that the closer to in-distribution, the better quality synthetic data will have. 
4.4 Model Evaluation 
To evaluate synthetic data in strengthening the generalizability of RL agents, a series of experiments were designed. The augmented dataset, comprising both real and synthetic experience samples, was used to train a TD3-BC agent. We choose TD3-BC for its ability to leverage offline data, which aligns well with the synthetic experiences generated by the diffusion model. 
Evaluation Metrics for Diffusion data Evaluation: Cumulative Reward: The final return after the convergent that the RL agent reaches can be regarded as the quality of the synthetic data. 
We train TD3-BC on the synthetic dataset. As a control, we implement a Context-Aware TD3-BC algorithm that takes both transitions and contexts as inputs. We also implemented a method that makes RL agents trained on both synthetic and real datasets. In conclusion, there are three different types of testing, and each of them will be trained in multiple different contexts: 
23
 Context-Aware Algorithm on Real Data: The RL agent was trained on the real dataset with context information integrated, establishing a benchmark for Context-Aware learning. 
 Non-Context-Aware Algorithm on the synthetic Data: In this setup, the agent was trained exclusively on synthetic data generated by the diffusion model, testing the quality of synthetic data in isolation. 
 Context-Aware Algorithm on the synthetic and the real Data: This setup combined Context-Aware RL with synthetic data, aiming to assess the maximum potential of context-driven synthetic data augmentation in promoting generalization. Training datasets are made of both synthetic data and real data in a 50/50 ratio. 
The testing process uses the same separations of diffusion model training separations. We train the diffusion model on datasets with different contexts. Specifically, we train each combination on "Front", "Middle", "Extremes", and "Rear" datasets and different pole lengths across 0.1 to 0.7. So there are 84 different kinds of combinations of experiments. These experiments will show how diffusion performs when it’s working in situations of both in-distribution and out-of-distribution. 
24
5 Results 
This section presents the experimental results obtained by evaluating the proposed methods under varying contexts. The experiments are structured to analyze the performance of diffusion models generated data for reinforcement learning (RL). 
5.1 Training with Synthetic Data Compared to Training without Synthetic Data 
This experiment aim to answer the question: Does incorporating synthetic data for unseen pole lengths in contextual reinforcement learning, where pole length serves as the context, improve an agent’s generalization capability compared to training solely on real data? 
Training and Testing Data Separations: Training datasets were categorized into four separations: "Front", "Rear", "Middle", and "Extremes". These separations vary by the range of environmental contexts (pole lengths in the cart-pole environment) used for both training and testing. Testing datasets consist of seven predefined pole lengths: {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7}. We test each of them with 10 seeds. 
Total training data for all the separations consists of 300 unique pole lengths across (0.1,0.7), each with 10 episodes. Each separation uses only the data that is in the range as training data. 
Separation Training Context Testing Context Front {ci | 0.1 < ci < 0.25, i ∈ {1, 2, . . . , 100}} {0.1, 0.2, ..., 0.7} Rear {ci | 0.55 < ci < 0.7, i ∈ {1, 2, . . . , 100}} {0.1, 0.2, ..., 0.7} Middle {ci | 0.35 < ci < 0.45, i ∈ {1, 2, . . . , 100}} {0.1, 0.2, ..., 0.7} Extremes {ci | 0.1 < ci < 0.15 or 0.65 < ci < 0.7, . . . } {0.1, 0.2, ..., 0.7} 
Table 2: Setup of 300 contexts and 10 episodes training experiment. 
Evaluation Metrics: Cumulative Reward: Cumulative reward achieved by the TD3-BC agent after convergence. 
25
Figure 7: Box plot of returns of different methods for 300 contexts with 10 episodes. The vertical axis represents the return of the test, the horizontal axis represents the distance to the in-distribution range. The grey area represents the in-distribution range. The red boxes represent the diffusion method, the blue boxes represent the Context-Aware method, and the green boxes represent the combination of diffusion and Context-Aware methods. The lines in the boxes represent the median of the test results. 
Due to big variance of rewards of each point, it’s hard to ensure the effects of Method (Diffusion, Context-Aware, Diffusion and Context-Aware) and Distance on the reward. So, we conducted a repeated-measures ANOVA for statistical significance testing. This test use each seed as a within-subject factor. 
Table 3: Repeated-Measures ANOVA Results 
Source df F p-unc p-GG-corr ng2 method 2, 18 30.625169 1.608579e-06 1.598710e-05 0.380268 distance 5, 45 462.030109 1.797350e-37 1.679194e-21 0.934296 
Table 4: Pairwise T-tests of Method with Bonferroni Correction 
A B T dof p-unc p-corr hedges C D -5.212330 9.0 0.000555 0.001665 -2.184085 C C & D -4.896894 9.0 0.000851 0.002554 -2.382290 D C & D -0.476146 9.0 0.645317 1.000000 -0.200633 
C = Context-Aware; D = Diffusion; C & D = Context-Aware & Diffusion. 
26
The result shows that both method and distance are highly related to the reward (their p value lower than 0.001). Diffusion related methods (Diffusion, Context-Aware & Diffusion) outperform Context-Aware method. Diffusion and Context-Aware & Diffusion did not differ from each other to a statistically significant extent. 
5.2 OOD Performance 
This experiment use the same setup as experiment 5.1 to show the relation ship between distance and return of all the separations ("Front", "Extremes", "Middle", "Rear"). We calculate the return by average the returns of all the related points. 
This experiment aim to answer the question: Does training offline RL agents with synthetic data improve their out-of-distribution (OOD) performance compared to using only real data? How does the performance change as test contexts (OOD) deviate further from training contexts (ID)? 
Figure 8: This figure shows the relationship between average return and context distance to training data of all the methods. The horizontal axis represents the distance to the in-distribution range. And vertical axis represents the average return. The red line represents the diffusion method, the blue line represents the Context-Aware method, and the green line represents the combination of diffusion and Context-Aware methods. 
Combining the previous experiment 5.1, the results show that: 
27
 Diffusion methods outperformed Context-Aware for most of the OOD testing contexts. 
 For in-distribution situations, RL agents trained with synthetic data achieve performance comparable to Context-Aware agents trained with real data. 
 Diffusion methods get better performance when the test context is far from in-distribution 
5.3 Varying number of episodes of each context 
Setup: Training data includes 300 pole lengths, each with 50 episodes for all the separations. The number of episodes in each context increases to 50 to explore how different numbers of episodes affect the performance of these RL algorithms. All the other hyperparameters remain the same. 
Figure 9: Box plot of returns of different methods for 300 contexts with 50 episodes. The vertical axis represents the return of the test, the horizontal axis represents the distance to the in-distribution range. The grey area represents the in-distribution range. The red boxes represent the diffusion method, the blue boxes represent the Context-Aware method, and the green boxes represent the combination of diffusion and Context-Aware methods. The lines in the boxes represent the median of the test results. 
28
Figure 10: Diffusion Method Performance comparison of 50 episodes and 10 episodes. 
For Context-Aware Off & Diffusion On cases, 50 episodes case performs similarly to 10 episodes case when it’s close to in-distribution. When it’s far from in-distribution, more episodes case performs even worse. So, increasing the number of episodes alone will not improve the performance of the Diffusion model method. 
29
6 Potential Industrial Applications 
The ability of diffusion models to generate reliable synthetic data can significantly reduce the cost of data collection in industrial robotics [45, 47]. This section shows the potential industrial applications of our method that uses diffusion models for contextual transition generation in reinforcement learning. 
6.1 Robotic Control and Automation 
Robots in industrial environments often face dynamic and changing conditions, such as varying task requirements, environmental layouts, or operational parameters. Traditional reinforcement learning (RL) struggles to generalize under these conditions due to its dependency on fixed training datasets [45, 46]. The synthetic data generated by diffusion models can provide diverse training scenarios, enabling RL agents to perform reliably in a range of industrial tasks. In addition, domain randomization-based strategies have proven successful in bridging simulation and real-world robotics [47], which further motivates the use of synthetic data for robust robot training. 
Example: Robots can be trained with synthetic data to adapt to different arm lengths or payload variations, enhancing their versatility in manufacturing environments [48]. 
6.2 Fault Diagnosis and Maintenance 
Industrial equipment must be monitored for potential failures to minimize downtime and optimize maintenance schedules. However, collecting sufficient fault-related data is expensive and time-intensive, especially for rare or critical failure modes [49]. Diffusion models can address this challenge by generating realistic fault simulation data, which RL algorithms can use to improve their predictive maintenance capabilities [50]. By training on both real and synthetic fault scenarios, RL models can detect anomalies more reliably and reduce false alarms. 
Example: Synthetic data can simulate rare fault patterns, enabling RL models to generalize to previously unseen equipment conditions and predict failures more accurately [51, 49]. 
6.3 Logistics and Warehouse Optimization 
The efficiency of logistics and warehousing operations is critical in industries like e-commerce and manufacturing [52, 53]. Automated systems, such as autonomous 
30
guided vehicles (AGVs), need to handle diverse challenges like changing storage layouts, variable item dimensions, and dynamic task scheduling [54]. By generating synthetic data for a variety of scenarios, diffusion models can enhance the robustness and adaptability of RL models in these contexts. 
Example: Synthetic data can help train RL models for efficient route planning and task allocation in warehouses with evolving layouts [52]. 
31
7 Conclusion and Limitation 
In this thesis, we propose and validate a novel approach to leveraging diffusion models for generating synthetic data to help RL agents adapt to new environments. We train diffusion models on contextualized data and demonstrate diffusion model can generate transitions that enable RL algorithms to generalize effectively across diverse and previously unseen environments. 
Our experimental results reveal that synthetic data significantly enhances the performance of RL agents, particularly in out-of-distribution tasks. Notably, the greater the deviation between the training and testing contexts, the more pronounced the advantage of diffusion method over Context-Aware method. 
This work also demonstrates the potential of diffusion models to improve RL generalization in industrial applications where adaptability and efficiency are critical. 
However, This thesis only compared the diffusion method with the Context-Aware method and did not verify the diffusion method in real-world applications. Future work may compare the diffusion method with other related methods that try to make RL agents adapt to unseen environments. And explore extending this approach to more complex, real-world applications. 
32
References 
[1] Sutton, R. S., & Barto, A. G. (2018). *Reinforcement learning: An introduction*. MIT Press. 
[2] Lin, L.-J. (1992). Self-improving reactive agents based on reinforcement learning, planning, and teaching. *Machine Learning, 8*(3), 293–321. https: //doi.org/10.1007/BF00992699 
[3] Williams, R. J. (1991). Function optimization using connectionist reinforcement learning algorithms. *Connection Science, 3*(3), 241–268. https://doi.org/ 10.1080/09540099108946587 
[4] Ng, A. Y., Harada, D., & Russell, S. J. (1999). Policy invariance under reward transformations: Theory and application to reward shaping. In *Proceedings of the 16th International Conference on Machine Learning (ICML)* (pp. 278–287). 
[5] Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2015). Prioritized experience replay. *arXiv preprint arXiv:1511.05952*. 
[6] Levine, S., Kumar, A., Tucker, G., & Fu, J. (2020). Offline reinforcement learning: Tutorial, review, and perspectives on open problems. *arXiv preprint arXiv:2005.01643*. 
[7] Rakelly, K., Zhou, A., Quillen, D., Finn, C., & Levine, S. (2019). Efficient off-policy meta-reinforcement learning via probabilistic context variables. In *Proceedings of the International Conference on Machine Learning (ICML)*. 
[8] Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. In *Advances in Neural Information Processing Systems (NeurIPS)*. 
[9] Nichol, A. Q., & Dhariwal, P. (2021). Improved denoising diffusion probabilistic models. *arXiv preprint arXiv:2102.09672*. 
[10] Preechakul, T., Chuang, C.-Y., Denize, J., Hennigan, T., Mahajan, A., & Roy, S. (2022). Diffusion autoencoders: Toward a meaningful and decodable representation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 10619–10629). https://doi.or g/10.1109/CVPR52688.2022.01037 
[11] Henderson, P., Islam, R., Bachman, P., Pineau, J., Precup, D., & Meger, D. (2018). Deep reinforcement learning that matters. In *Proceedings of the AAAI Conference on Artificial Intelligence* (Vol. 32, No. 1). https: 
//doi.org/10.1609/aaai.v32i1.11411 
[12] Zhou, D., Pinto, L., & Gupta, A. (2019). Environment probing interaction policies. In *Proceedings of the International Conference on Learning Repre-sentations (ICLR)*. https://openreview.net/forum?id=HJfSe2A5KX 
33
[13] Wang, X., Chen, M., Zhang, Y., Wang, B., & Xu, W. (2018). Deep reinforcement learning for autonomous driving: A survey. *IEEE Transactions on Neural Networks and Learning Systems, 29*(12), 3833–3848. https://doi.org/10.1 109/TNNLS.2018.2830776 
[14] Watkins, C. J. C. H., & Dayan, P. (1992). Q-learning. *Machine Learning, 8*(3–4), 279–292. https://doi.org/10.1007/BF00992698 
[15] Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). *Soft actor-critic algorithms and applications*. arXiv preprint arXiv:1812.05905. 
[16] Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., & Ganguli, S. (2015). Deep unsupervised learning using nonequilibrium thermodynamics. In *Proceedings of the International Conference on Machine Learning (ICML)* (pp. 2256–2265). PMLR. 
[17] Goodfellow, I., Pouget-Abadie, J., Mirza, M., et al. (2014). Generative adversarial nets. In *Advances in Neural Information Processing Systems (NeurIPS)* (pp. 2672–2680). 
[18] Fujimoto, S., van Hoof, H., & Meger, D. (2018). Addressing function approximation error in actor-critic methods. In *Proceedings of the 35th International Conference on Machine Learning (ICML)* (pp. 1587–1596). 
[19] Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). *Soft actor-critic algorithms and applications*. arXiv preprint arXiv:1812.05905. 
[20] Fujimoto, S., & Gu, S. (2021). A minimalist approach to offline reinforcement learning. In *Advances in Neural Information Processing Systems (NeurIPS)*. 
[21] Lillicrap, T. P., Hunt, J. J., Pritzel, A., et al. (2015). Continuous control with deep reinforcement learning. *arXiv preprint arXiv:1509.02971*. 
[22] Your Article Authors, "Learning Visual Invariance with Self-Supervision," Journal Name, vol. Volume Number, pp. Page Numbers, 2024. 
[23] A. Srinivas, M. Laskin, and P. Abbeel, "Generalization in Reinforcement Learning by Soft Data Augmentation," Conference on Computer Vision and Pattern Recognition (CVPR), 2020. 
[24] S. Fedus, J. Gelada, N. Heess, T. Lillicrap, M. Norouzi, and G. E. Hinton, "Replay-Guided Adversarial Reinforcement Learning," in Advances in Neural Information Processing Systems (NeurIPS), 2020. 
[25] B. Imre," An Investigation of Generative Replay in Deep Reinforcement Learning," in 34th Twente Student Conference on IT, 2021. 
34
[26] M. Laskin, K. Lee, A. Stooke, L. Pinto, P. Abbeel, and A. Srinivas, "Reinforcement Learning with Augmented Data," Advances in Neural Information Processing Systems (NeurIPS), 2020. Available at: https://github.com/Misha Laskin/rad. 
[27] R. Raileanu, M. Goldstein, D. Yarats, I. Kostrikov, and R. Fergus, "Automatic Data Augmentation for Generalization in Reinforcement Learning," Advances in Neural Information Processing Systems (NeurIPS), 2021. Available at: https://github.com/rraileanu/auto-drac. 
[28] Pomerleau, D. A. (1989). ALVINN: An autonomous land vehicle in a neural network. In *Advances in Neural Information Processing Systems (NeurIPS)* (pp. 305–313). 
[29] Arjovsky, M., Chintala, S., & Bottou, L. (2017). Wasserstein GAN. In *Proceedings of the International Conference on Machine Learning (ICML)* (pp. 214–223). PMLR. 
[30] Dhariwal, P., & Nichol, A. (2021). Diffusion models beat GANs on image synthesis. In *Advances in Neural Information Processing Systems (NeurIPS)*. 
[31] Nichol, A., Jun, H., Dhariwal, P., et al. (2021). GLIDE: Towards photorealistic image generation and editing with text-guided diffusion models. In *Proceedings of the 38th International Conference on Machine Learning (ICML)*. 
[32] Janner, M., Li, Q., & Levine, S. (2022). Planning with diffusion for flexible behavior synthesis. In *Advances in Neural Information Processing Systems (NeurIPS)*. 
[33] Song, Y., Sohl-Dickstein, J., Kingma, D. P., et al. (2021). Score-based generative modeling through stochastic differential equations. In *Proceedings of the International Conference on Learning Representations (ICLR)*. 
[34] Preechakul, T., Chuang, C.-Y., Denize, J., et al. (2023). SynthER: Online replay-based algorithms with synthetic experience. *arXiv preprint arXiv:2303.06614*. https://arxiv.org/abs/2303.06614 
[35] Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. *arXiv preprint arXiv:1801.01290*. https://arxiv.org/abs/1801.01290 
[36] Agarwal, R., Schuurmans, D., & Norouzi, M. (2020). An optimistic perspective on offline reinforcement learning. In *Proceedings of the 37th International Conference on Machine Learning (ICML)*. https://arxiv.org/abs/1907.045 43 
[37] Fujimoto, S., Meger, D., & Precup, D. (2019). Off-policy deep reinforcement learning without exploration. In *Proceedings of the 36th International Confer-ence on Machine Learning (ICML)*. https://arxiv.org/abs/1812.02900 
35
[38] Fu, J., Kumar, A., Nachum, O., et al. (2021). Benchmarks for deep off-policy evaluation. In *Advances in Neural Information Processing Systems (NeurIPS)*. https://arxiv.org/abs/2103.16596 
[39] Kidambi, R., Rajeswaran, A., Netrapalli, P., & Joachims, T. (2020). MOReL: Model-based offline reinforcement learning. In *Advances in Neural Information Processing Systems (NeurIPS)*. https://arxiv.org/abs/2005.05951 
[40] Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020). Conservative Q-Learning for offline reinforcement learning. In *Advances in Neural Information Processing Systems (NeurIPS)*. https://arxiv.org/abs/2006.04779 
[41] Lange, S., Gabel, T., & Riedmiller, M. (2012). Batch reinforcement learning. In *Reinforcement Learning: State-of-the-Art*. Springer. https://doi.org/10.1 007/978-3-642-27645-3_11 
[42] Pinsler, R., et al. (2021). Medical image synthesis with conditional diffusion models. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*. 
[43] Li, H., et al. (2021). Text-to-image generation using conditioned diffusion models. In *Proceedings of the International Conference on Computer Vision (ICCV)*. 
[44] Arulkumaran, K., Deisenroth, M. P., Brundage, M., & Bharath, A. A. (2017). A brief survey of deep reinforcement learning. *arXiv preprint arXiv:1708.05866*. 
[45] J. Kober, J. A. Bagnell, and J. Peters, “Reinforcement learning in robotics: A survey,” The International Journal of Robotics Research, vol. 32, no. 11, pp. 1238–1274, 2013. 
[46] S. Levine, C. Finn, T. Darrell, and P. Abbeel, “End-to-end training of deep visuomotor policies,” The Journal of Machine Learning Research, vol. 17, no. 1, pp. 1334–1373, 2016. 
[47] J. Tobin, L. Biewald, E. Duan, et al., “Domain randomization for transferring deep neural networks from simulation to the real world,” in Proc. of the 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Vancouver, BC, Canada, 2017, pp. 23–30. 
[48] Y. Chebotar, A. Handa, V. Makoviychuk, et al., “Closing the sim-to-real loop: Adapting simulation randomization with real world experience,” in Proc. of the 2019 IEEE International Conference on Robotics and Automation (ICRA), Montreal, QC, Canada, 2019, pp. 8973–8979. 
[49] Y. Lei, B. Yang, X. Jiang, et al., “Machinery health prognostics: A systematic review from data acquisition to RUL prediction,” Mechanical Systems and Signal Processing, vol. 104761, pp. 1–37, 2020. 
36
[50] G. A. Susto, A. Schirru, S. Pampuri, S. McLoone, and A. Beghi, “Machine learning for predictive maintenance: A multiple classifier approach,” IEEE Transactions on Industrial Informatics, vol. 11, no. 3, pp. 812–820, 2015. 
[51] G. Li, Y. Wang, Y. Wei, and R. Stoean, “An improved multi-scale radial basis function neural network for fault diagnosis under varying conditions,” Applied Soft Computing, vol. 82, art. 105567, 2019. 
[52] P. R. Wurman, R. D’Andrea, and M. Mountz, “Coordinating hundreds of cooperative, autonomous vehicles in warehouses,” AI Magazine, vol. 29, no. 1, pp. 9–19, 2008. 
[53] N. Boysen, R. de Koster, and F. Weidinger, “Warehousing in the e-commerce era: A survey,” European Journal of Operational Research, vol. 277, no. 2, pp. 396–411, 2019. 
[54] J. Gu, H. Zhou, M. Nawaz, et al., “Deep reinforcement learning for warehouse order fulfillment,” in Proc. of the 2017 IEEE International Conference on Big Data (Big Data), Boston, MA, USA, 2017, pp. 3332–3339. 
37
A Hyper Parameters of SAC Agent 
Parameter Value torch_deterministic True 
cuda True 
capture_video False 
env_id "CartPole-v1" 
cond_low 0.1 
cond_high 0.7 
num_envs 1 
total_timesteps 250,000 
buffer_size 1e6 
gamma 0.99 
tau 0.005 
batch_size 256 
learning_starts 5,000 
policy_lr 3e-4 
q_lr 1e-3 
policy_frequency 2 
target_network_frequency 1 
noise_clip 0.5 
alpha 0.2 
autotune True 
Table A1: SAC Hyper parameters 
38
B Hyper Parameters of Diffusion model 
Parameter Value modelled_terminals True 
make_inputs.modelled_terminals %modelled_terminals 
split_diffusion_samples.modelled_terminals %modelled_terminals 
split_diffusion_samples.terminal_threshold 0.5 
construct_diffusion_model.normalizer_type ’minmax’ 
construct_diffusion_model.denoising_network @ResidualMLPDenoiser 
construct_diffusion_model.disable_terminal_norm False 
ResidualMLPDenoiser.dim_t 128 
ResidualMLPDenoiser.mlp_width 128 
ResidualMLPDenoiser.num_layers 6 
ResidualMLPDenoiser.learned_sinusoidal_cond False 
ResidualMLPDenoiser.random_fourier_features True 
ResidualMLPDenoiser.learned_sinusoidal_dim 16 
ResidualMLPDenoiser.activation ’relu’ 
ResidualMLPDenoiser.layer_norm True 
ElucidatedDiffusion.num_sample_steps 128 
ElucidatedDiffusion.sigma_data 1.0 
ElucidatedDiffusion.S_churn 80 
ElucidatedDiffusion.S_tmin 0.05 
ElucidatedDiffusion.S_tmax 50 
ElucidatedDiffusion.S_noise 1.003 
Trainer.train_batch_size 512 
Trainer.small_batch_size 256 
Trainer.train_lr 6e-4 
Trainer.lr_scheduler ’cosine’ 
Trainer.weight_decay 1e-2 
Trainer.train_num_steps 100,000 
Trainer.save_and_sample_every 50,000 
SimpleDiffusionGenerator.num_sample_steps 128 
SimpleDiffusionGenerator.sample_batch_size 100,000 
Table B1: Diffusion model Parameters 
39