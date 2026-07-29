> Source: https://iscsitr.in/index.php/ISCSITR-IJDE/article/download/ISCSITR-IJDE_05-01-02/ISCSITR-IJDE_05-01-02/1503

ISCSITR- INTERNATIONAL JOURNAL OF DATA ENGINEERING (ISCSITR-IJDE) 
Vol.5, Iss. 1, Jan-Jun, 2024, pp. 8-15. 
https://iscsitr.com/index.php/ISCSITR-IJDE 
Journal ID: 7193-8452 
 
https://iscsitr.com/index.php/ISCSITR-IJDE 8  
 
 
Evaluating the Efficiency of Reinforcement Learning Algorithms 
in Dynamic Environment Simulations 
 
Franz Cornelia Patrick, 
AI Specilist, United States. 
 
Abstract 
Reinforcement Learning (RL) has witnessed substantial advancements in recent years, 
particularly in its application to complex, dynamic environments such as robotics, 
autonomous driving, and adaptive control systems. This paper presents a comparative 
evaluation of popular RL algorithms—Q-Learning, Deep Q-Networks (DQN), and Proximal 
Policy Optimization (PPO)—within high-variability simulated environments. Using metrics 
such as cumulative reward, convergence time, and policy stability, we examine algorithmic 
efficiency under different dynamic transition patterns and stochasticity levels. Our 
simulations, conducted in using the OpenAI Gym and Unity ML-Agents frameworks, reveal 
that PPO consistently outperforms other methods in highly dynamic scenarios. The findings 
underscore the importance of balancing exploration and exploitation when deploying RL in 
real-world systems characterized by continuous environmental shifts. 
Keywords: Reinforcement Learning, Dynamic Environments, Q-Learning, DQN, PPO, Policy 
Optimization, Simulation, Algorithm Efficiency. 
 
How to cite this paper: Cornelia, P. F. (2024). Evaluating the efficiency of reinforcement learning 
algorithms in dynamic environment simulations. ISCSITR - International Journal of Data 
Engineering (ISCSITR-IJDE), 5(1), 8-15. 
URL: https://iscsitr.com/index.php/ISCSITR-IJDE/article/view/ISCSITR-IJDE_05_01_02 
Published: 26th Mar 2024 
Copyright © 2024 by author(s) and International Society for Computer Science and Information 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 9  
 
Technology Research (ISCSITR). This work is licensed under the Creative Commons Attribution 
International License (CC BY 4.0). http://creativecommons.org/licenses/by/4.0/    
  
1. Introductıon  
Reinforcement Learning (RL) is a computational approach where agents learn to make 
sequences of decisions by interacting with an environment to maximize cumulative rewards. 
In recent years, RL has moved from theoretical formulations to practical applications across 
domains such as finance, healthcare, gaming, and autonomous navigation. However, most RL 
research has been developed and tested under stationary environments—ones where 
transition probabilities and rewards remain consistent over time. 
Dynamic environments, by contrast, exhibit continuously shifting rules, reward structures, 
and state transitions. These conditions pose substantial challenges to RL algorithms, 
especially those that rely heavily on learned value functions or static policy representations. 
Evaluating the performance of RL agents under such dynamics has become increasingly 
important as real-world applications demand more robust and adaptive learning strategies. 
This study addresses this gap by systematically comparing three major RL algorithms—Q-
Learning, DQN, and PPO—within simulated dynamic environments. We assess their ability 
to adapt, converge, and maintain stability when exposed to sudden or gradual changes in 
environment parameters. 
 
2. Literature Review 
Reinforcement Learning has evolved significantly since its inception. Sutton and Barto 
(2018) provided a foundational framework for understanding RL algorithms, particularly 
model-free approaches like Q-Learning and SARSA. Q-Learning, introduced by Watkins and 
Dayan (1992), was one of the earliest algorithms capable of learning optimal policies 
without a model of the environment. While effective in small, discrete environments, Q-
Learning faces scalability issues in high-dimensional or non-stationary settings. 
With the rise of deep learning, Mnih et al. (2015) proposed the Deep Q-Network (DQN), 
which combined Q-Learning with deep neural networks to handle high-dimensional sensory 
Open Access
  
https://iscsitr.com/index.php/ISCSITR-IJDE 10  
 
inputs. This breakthrough enabled RL to excel in visual environments such as Atari games. 
However, DQNs are known to suffer from instability during training, especially in non-
stationary environments. 
Policy-gradient methods, such as Proximal Policy Optimization (PPO) introduced by 
Schulman et al. (2017), have been widely praised for their robustness and sample 
efficiency. PPO maintains a balance between policy exploration and policy exploitation by 
limiting large policy updates, which is especially valuable in dynamic or unpredictable 
settings. 
Several researchers have explored dynamic environment simulations. Padakandla (2020) 
investigated non-stationary RL and identified the importance of adaptive learning rates. Xie 
et al. (2020) introduced dynamic curriculum learning, adjusting difficulty based on agent 
performance. Yet, comprehensive empirical evaluations comparing standard RL algorithms 
in highly dynamic environments remain sparse. This paper aims to fill that gap using RL 
frameworks and evaluation standards. 
 
3. Objective and Hypothesis 
This study aims to evaluate the efficiency of major RL algorithms in dynamic simulated 
environments. The core research questions include: 
How do Q-Learning, DQN, and PPO perform in terms of learning speed, stability, and 
reward maximization in dynamic settings? 
Which algorithm demonstrates greater adaptability to changes in environmental 
parameters? 
What trade-offs exist between algorithm complexity and performance under non-
stationarity? 
Our hypothesis posits that PPO will outperform Q-Learning and DQN in environments with 
high temporal variability due to its policy regularization mechanism and robust convergence 
behavior. 
 
4. Methodology & Metrics 
We designed a dynamic grid-world and a continuous-control simulation using OpenAI Gym 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 11  
 
and Unity ML-Agents. The environment changes state-transition probabilities and reward 
functions over time in both abrupt (stepwise) and gradual (drift-based) patterns. 
 
Metrics used include: 
Cumulative Reward: Total reward collected by an agent during each episode. 
Convergence Time: Number of episodes required to stabilize policy performance. 
Policy Stability Index (PSI): A custom metric assessing the variance in action 
distribution across episodes. 
Table 1: Environment Parameters 
Parameter Value Range Variation Mode 
Reward Shift Frequency 10–50 episodes Stepwise 
State Transition Drift ±5% per episode Gradual 
Environment Complexity Low, Medium, High Configurable 
Agents were trained for 5000 episodes with fixed random seeds for reproducibility. Each 
experiment was repeated 10 times to ensure statistical significance. 
 
5. Techniques and Tools 
We employed the following RL algorithms: 
Q-Learning: Classical tabular implementation for discrete state spaces. 
DQN: Implemented using PyTorch with experience replay and target networks. 
PPO: Implemented via Stable-Baselines3, with default hyperparameters and adaptive 
learning rates. 
The dynamic environments were created using: 
OpenAI Gym (v0.26) 
Unity ML-Agents Toolkit (v2.3) for continuous control tasks 
Training was conducted using NVIDIA A100 GPUs and Intel Xeon processors in a 
distributed setup with automated logging via Weights & Biases. 
 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 12  
 
 
Figure 1: System Architecture for Simulation and Evaluation 
Figure 1: The system architecture shows the workflow for training and evaluating RL agents. 
It includes environment simulation (via OpenAI Gym and Unity ML-Agents), algorithm 
selection (Q-Learning, DQN, PPO), training modules, logging interfaces (e.g., Weights & 
Biases), and evaluation pipelines for performance tracking. 
 
6. Quality Assurance 
To ensure reliability, the following practices were applied: 
Reproducibility: Random seeds fixed across all experiments; code made publicly 
available on GitHub. 
Cross-validation: Environments with varying initial configurations were tested. 
Baseline Comparison: Static environment benchmarks were run for control 
comparison. 
Evaluation Frequency: Every 50 episodes, intermediate models were saved and 
evaluated on frozen test environments. 
We adhered to NeurIPS reproducibility checklist, ensuring the inclusion of key 
experimental details, parameter settings, and code documentation. Results were analyzed 
using statistical significance testing (e.g., Welch’s t-test) for comparing algorithm 
performance. 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 13  
 
7. Limitations and Potential Biases 
One limitation lies in the design of the dynamic environment—while variations were 
incorporated, real-world environments exhibit far more complex, multi-agent dynamics. 
Also, reward function shaping may inadvertently favor some algorithms over others. 
The tabular Q-Learning implementation is inherently limited in scalability, which may 
skew comparisons. Furthermore, deep models’ performance can vary significantly 
depending on hyperparameter tuning, which was not extensively optimized in this study due 
to computational constraints. 
Ethical considerations were minimal, given the simulated nature of the experiments. 
However, future real-world applications must account for safety and interpretability, 
particularly in sensitive domains like healthcare or autonomous systems. 
 
8. Key Findings and Interpretations 
Our results indicate that PPO consistently achieved higher cumulative rewards and faster 
convergence across all dynamic environments. 
Table 2: Average Performance Over 10 Runs 
Algorithm Avg. Reward Convergence Episodes PSI (Lower = Better) 
Q-Learning 210 3400 0.72 
DQN 480 2200 0.58 
PPO 690 1500 0.33 
PPO's stability in policy updates allows it to adapt efficiently to environmental changes, 
especially in higher-dimensional tasks. DQN performed reasonably but was prone to 
catastrophic forgetting in volatile environments. Q-Learning struggled with convergence, 
particularly in larger, continuous settings. 
 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 14  
 
 
Figure 2: Learning Curves of Algorithms in Dynamic GridWorld 
These results are consistent with existing literature suggesting that policy-gradient methods 
are better suited for non-stationary and complex environments. Future work may explore 
hybrid architectures or meta-RL strategies to further enhance adaptability. 
 
9. Conclusion 
This study systematically evaluated the efficiency of three RL algorithms—Q-Learning, DQN, 
and PPO—in dynamic simulated environments. The findings reinforce the superior 
adaptability of PPO, particularly in scenarios with high temporal variability. As RL continues 
to be deployed in real-world systems, adaptability to dynamic conditions must remain a 
central design concern. We advocate for further development in meta-learning and continual 
learning approaches to better handle real-world non-stationarity. 
 
References 
[1] Sutton, Richard S., and Andrew G. Barto. Reinforcement Learning: An Introduction. 2nd 
ed., MIT Press, 2018. 
[2] Watkins, Christopher J. C. H., and Peter Dayan. “Q-Learning.” Machine Learning, vol. 8, 
no. 3–4, 1992, pp. 279–292. 
[3] Mnih, Volodymyr, et al. “Human-Level Control through Deep Reinforcement Learning.” 
Nature, vol. 518, no. 7540, 2015, pp. 529–533. 
[4] Schulman, John, et al. “Proximal Policy Optimization Algorithms.” arXiv preprint 
arXiv:1707.06347, 2017. 
  
https://iscsitr.com/index.php/ISCSITR-IJDE 15  
 
[5] Padakandla, Sridhar. “A Survey of Reinforcement Learning Algorithms for Dynamically 
Changing Environments.” arXiv preprint arXiv:2005.10619, 2020. 
[6] Xie, Angela, et al. “Curriculum Reinforcement Learning for Continuous Control.” 
International Conference on Learning Representations (ICLR), 2020. 
[7] Lillicrap, Timothy P., et al. “Continuous Control with Deep Reinforcement Learning.” 
arXiv preprint arXiv:1509.02971, 2015. 
[8] Kober, Jens, J. Andrew Bagnell, and Jan Peters. “Reinforcement Learning in Robotics: A 
Survey.” The International Journal of Robotics Research, vol. 32, no. 11, 2013, pp. 1238– 
1274. 
[9] Silver, David, et al. “Mastering the Game of Go with Deep Neural Networks and Tree 
Search.” Nature, vol. 529, no. 7587, 2016, pp. 484–489. 
[10] Kamadi, S. (2023). Identity-Driven Zero Trust Automation in GitOps: Policy-as-Code 
Enforcement for Secure Code Deployments. International Journal of Scientific Research 
in Computer Science, Engineering and Information Technology, 9(3), 893-902. 
https://doi.org/10.32628/CSEIT235148 
[11] François-Lavet, Vincent, et al. “An Introduction to Deep Reinforcement Learning.” 
Foundations and Trends in Machine Learning, vol. 11, nos. 3–4, 2018, pp. 219–354. 
[12] Zhao, Rui, et al. “Deep Reinforcement Learning for Dynamic System Control: A Review.” 
IEEE Control Systems Magazine, vol. 40, no. 6, 2020, pp. 26–68. 
[13] Hou, Yonghong, et al. “A Review of Reinforcement Learning in Non-Stationary 
Environments.” IEEE Access, vol. 9, 2021, pp. 150138–150154. 
[14] Chen, Tianqi, et al. “Learning to Adapt in Dynamic, Real-World Environments.” 
Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 11, 2021, pp. 
9592–9600. 
[15] Al-Shedivat, Maruan, et al. “Continuous Adaptation via Meta-Learning in Nonstationary 
and Competitive Environments.” International Conference on Learning Representations 
(ICLR), 2018. 
[16] Hadfield-Menell, Dylan, et al. “The Off-Switch Game.” Proceedings of the 26th 
International Joint Conference on Artificial Intelligence (IJCAI), 2017, pp. 220–227. 
  