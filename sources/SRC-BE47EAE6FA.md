UCLA 
UCLA Electronic Theses and Dissertations 
Title Uncertainty-Aware Unsupervised and Robust Reinforcement Learning 
Permalink https://escholarship.org/uc/item/79g536hk 
Author Zhang, Weitong 
Publication Date 2024  Peer reviewed|Thesis/dissertation 
eScholarship.org Powered by the California Digital Library 
UNIVERSITY OF CALIFORNIA 
Los Angeles 
Uncertainty-Aware Unsupervised and Robust Reinforcement Learning 
A dissertation submitted in partial satisfaction 
of the requirements for the degree 
Doctor of Philosophy in Computer Science 
by 
Weitong Zhang 
2024
© Copyright by 
Weitong Zhang 
2024
ABSTRACT OF THE DISSERTATION 
Uncertainty-Aware Unsupervised and Robust Reinforcement Learning 
by 
Weitong Zhang 
Doctor of Philosophy in Computer Science 
University of California, Los Angeles, 2024 
Professor Quanquan Gu, Chair 
This dissertation is centered around addressing several key concerns in reinforcement learning 
(RL). RL has been a popular topic in the design of autonomous intelligent agents that make 
decisions and learn optimal actions through interaction with the environment. Over the 
past decades, RL has achieved significant success in various domains. However, RL has 
consistently been criticized for its inefficiency in exploration and vulnerability to model 
errors or noise. This dissertation aims to tackle these challenges through uncertainty-aware 
methods. 
In the first part of this dissertation, we explore how an RL agent can efficiently explore the 
environment without human supervision. We begin with a theoretical framework on reward-
free exploration and establish a connection between reward-free exploration and unsupervised 
reinforcement learning. We provide both theoretical analyses and practical algorithms that 
exhibit competitive empirical performance. In the second part of this dissertation, we aim to 
develop robust RL algorithm in a misspecified setting, where the function class (e.g., Neural 
Networks) cannot adequately approximate the underlying ground truth function. We show 
how significant the approximation error needs to be in order to prevent the agent from 
ii
efficiently learning the environment and making good decisions. We also present several 
algorithms that ensure the agent will only make a finite number of mistakes over infinite 
runs when this approximation error is small. 
The methods and techniques discussed in this dissertation advance the theoretical un-
derstanding of key concerns and limitations in RL, particularly in scenarios that require 
performance guarantees. Additionally, these findings not only suggest further research di-
rections but also pose several open questions that would help better design more robust and 
efficient decision making processes in the future. 
iii
The dissertation of Weitong Zhang is approved. 
Richard E. Korf 
Lihong Li 
Baharan Mirzasoleiman 
Stanley J. Osher 
Quanquan Gu, Committee Chair 
University of California, Los Angeles 
2024 
iv
To my beloved ones. 
v
TABLE OF CONTENTS 
1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 
1.1 Organization of the Dissertation . . . . . . . . . . . . . . . . . . . . . . . . . 6 
1.2 Notation System in this Dissertation . . . . . . . . . . . . . . . . . . . . . . 6 
2 Uncertainty-Aware Reward-Free Exploration with Linear Function Ap-
proximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 
2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 
2.1.1 Organization of this Chapter . . . . . . . . . . . . . . . . . . . . . . . 10 
2.2 Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 
2.2.1 Reinforcement Learning with Linear Function Approximation . . . . 11 
2.2.2 Reward-free Exploration . . . . . . . . . . . . . . . . . . . . . . . . . 12 
2.2.3 The Curse of Horizon in Reinforcement Learning . . . . . . . . . . . 14 
2.3 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 
2.3.1 Episodic Markov Decision Processes . . . . . . . . . . . . . . . . . . . 15 
2.3.2 Formal Definition of Reward-Free Exploration . . . . . . . . . . . . . 16 
2.4 Theoretical Guaranteed Reward-Free Exploration . . . . . . . . . . . . . . . 17 
2.4.1 Proposed Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 
2.4.2 Sample Complexity Analysis . . . . . . . . . . . . . . . . . . . . . . . 21 
2.5 Improved Algorithm and Analysis with Variance Information . . . . . . . . . 22 
2.5.1 Exploration Phase Algorithm with Variance Information . . . . . . . 22 
2.5.2 Sample Complexity Analysis . . . . . . . . . . . . . . . . . . . . . . . 25 
2.6 Optimal Horizon-Free Reward-Free Exploration Algorithms . . . . . . . . . . 26 
vi
2.6.1 Proposed Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . 27 
2.6.2 Sample Complexity Analysis . . . . . . . . . . . . . . . . . . . . . . . 34 
2.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 
2.8 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 
2.8.1 Proof of Theorem 2.4.3 . . . . . . . . . . . . . . . . . . . . . . . . . . 38 
2.8.2 Proof of Theorem 2.5.1 . . . . . . . . . . . . . . . . . . . . . . . . . . 42 
2.8.3 Proof of Theorem 2.6.3 . . . . . . . . . . . . . . . . . . . . . . . . . . 43 
2.8.4 Proof of Theorem 2.6.8 . . . . . . . . . . . . . . . . . . . . . . . . . . 45 
2.8.5 Proofs in Section 2.8.1 and Section 2.8.2 . . . . . . . . . . . . . . . . 48 
2.8.6 Proof of Auxiliary Lemmas in Section 2.8.5 . . . . . . . . . . . . . . . 60 
2.8.7 Missing Proof in Section 2.8.3 . . . . . . . . . . . . . . . . . . . . . . 65 
2.8.8 Proof of Lemmas in Section 2.8.7 . . . . . . . . . . . . . . . . . . . . 73 
2.8.9 Auxiliary Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86 
3 Uncertainty-Aware Unsupervised Exploration in Deep Reinforcement Learn-
ing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87 
3.1.1 Organization of this Chapter . . . . . . . . . . . . . . . . . . . . . . . 89 
3.2 Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90 
3.2.1 Unsupervised Reinforcement Learning . . . . . . . . . . . . . . . . . 90 
3.2.2 Reinforcement Learning with General Function Approximation . . . . 91 
3.3 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91 
3.3.1 Time-Inhomogeneous Episodic MDPs . . . . . . . . . . . . . . . . . . 91 
3.3.2 General Function Approximation . . . . . . . . . . . . . . . . . . . . 92 
vii
3.4 Proposed Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 
3.4.1 Exploration Phase: Efficient Exploration via Uncertainty-aware In-
trinsic Reward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95 
3.4.2 Planning Phase: Effective Planning Using Weighted Regression . . . 98 
3.5 Sample Complexity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 
3.6 Numerical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101 
3.6.1 Experiment Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101 
3.6.2 Experiment Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 
3.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 
3.8 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104 
3.8.1 Proof of Theorems in Section 3.5 . . . . . . . . . . . . . . . . . . . . 104 
3.8.2 Proof of Lemmas in Section 3.8.1 . . . . . . . . . . . . . . . . . . . . 108 
3.8.3 Proofs of Lemmas in Section 3.8.2 . . . . . . . . . . . . . . . . . . . . 117 
3.8.4 Proof of Lemmas in Section 3.8.3 . . . . . . . . . . . . . . . . . . . . 123 
3.8.5 Auxiliary Lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124 
3.9 Experiment details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125 
3.9.1 Details of exploration algorithm . . . . . . . . . . . . . . . . . . . . . 125 
3.9.2 Details of offline training algorithm . . . . . . . . . . . . . . . . . . . 128 
3.9.3 Hyper-parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128 
3.9.4 Ablation Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128 
4 Uncertainty-Aware Robust Linear Contextual Bandits . . . . . . . . . . . 134 
4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 
4.1.1 Organization of this Chapter . . . . . . . . . . . . . . . . . . . . . . . 136 
viii
4.2 Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136 
4.2.1 Linear Contextual Bandits . . . . . . . . . . . . . . . . . . . . . . . . 136 
4.2.2 Misspecified Linear Bandits. . . . . . . . . . . . . . . . . . . . . . . . 137 
4.3 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138 
4.4 Constant Regret Bound with Known Sub-Optimality Gap . . . . . . . . . . 139 
4.4.1 Proposed Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 139 
4.4.2 Regret Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140 
4.4.3 Key Proof Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . 141 
4.5 Constant Regret Bound with Unknown Sub-Optimality Gap . . . . . . . . . 143 
4.5.1 Proposed Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 143 
4.5.2 Regret Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144 
4.5.3 Key Proof Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . 146 
4.6 Lower Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148 
4.7 Numerical Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149 
4.7.1 Synthetic Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150 
4.7.2 Real-world Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152 
4.7.3 Experiment Details and Additional Results . . . . . . . . . . . . . . . 153 
4.8 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155 
4.9 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155 
4.9.1 Detailed Proof of Theorem 4.4.1 . . . . . . . . . . . . . . . . . . . . . 155 
4.9.2 Proof of Technical Lemmas in Section 4.9.1 . . . . . . . . . . . . . . . 159 
4.9.3 Detailed Proof of Theorem 4.5.1 . . . . . . . . . . . . . . . . . . . . . 165 
4.9.4 Proof of Theorem 4.6.1 . . . . . . . . . . . . . . . . . . . . . . . . . . 169 
ix
5 Uncertainty-Aware Robust Reinforcement Learning via Certified Estima-
tor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174 
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174 
5.1.1 Organization of this Chapter . . . . . . . . . . . . . . . . . . . . . . . 175 
5.2 Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176 
5.3 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178 
5.4 Proposed Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180 
5.4.1 Main algorithm: Cert-LSVI-UCB . . . . . . . . . . . . . . . . . . . . 180 
5.4.2 Subroutine: Cert-LinUCB . . . . . . . . . . . . . . . . . . . . . . . . 182 
5.5 Constant Regret Guarantee . . . . . . . . . . . . . . . . . . . . . . . . . . . 184 
5.6 Highlight of Proof Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . 186 
5.6.1 Technical challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . 186 
5.6.2 A novel approach: Cert-LinUCB . . . . . . . . . . . . . . . . . . . . . 187 
5.6.3 Settling the gap between V ˚ ´ V π and V ˚ ´ Q˚ . . . . . . . . . . . . 191 
5.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192 
5.8 Additional Discussions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192 
5.8.1 Comparison with He et al. (2021b) . . . . . . . . . . . . . . . . . . . 192 
5.8.2 Discussion on Lower Bounds of Sample Complexity . . . . . . . . . . 193 
5.9 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194 
5.9.1 Constant Regret Guarantees for Cert-LSVI-UCB . . . . . . . . . . . 194 
5.9.2 Proof of Lemmas in Section 5.9.1 . . . . . . . . . . . . . . . . . . . . 201 
5.9.3 Proof of Lemmas in Section 5.9.2 . . . . . . . . . . . . . . . . . . . . 216 
5.9.4 Proof of Lemmas in Section 5.9.3 . . . . . . . . . . . . . . . . . . . . 227 
x
5.9.5 Technical Numerical Lemmas . . . . . . . . . . . . . . . . . . . . . . 231 
6 Conclusions and Future Directions . . . . . . . . . . . . . . . . . . . . . . . . 234 
xi
LIST OF FIGURES 
1.1 A screenshot of the Atari Breakout game. . . . . . . . . . . . . . . . . . . . . . 1 
1.2 A screenshot of the Atari Montezuma’s Revenge. . . . . . . . . . . . . . . . . . 2 
2.1 Comparison between (a) the “reward-aware” exploration and (b) the “reward-free” 
exploration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 
2.2 The transition kernel of the hard-to-learn linear mixture MDPs. . . . . . . . . . 36 
3.1 Diagram of the unsupervised reinforcement learning paradigm. . . . . . . . . . . 88 
3.2 Episode reward at different training steps for tasks on walker and quadruped. . . 132 
3.3 Episode reward with different exploration episodes on walker and quadruped. . . 133 
4.1 An illustration of the recommender system. . . . . . . . . . . . . . . . . . . . . 134 
4.2 Cumulative regret of DS-OFUL with different Γ. Results are averaged over 8 
runs. In Figure 4.2b for Asirra dataset, the cumulative regret of DS-OFUL (as 
well as OFUL) can be read from the y-axis on the left. The cumulative regret of 
SupLinUCB algorithm can be read from the y-axis on the right. . . . . . . . . . 149 
4.3 The performance of DS-OFUL under different misspecification levels ζ. Results 
are averaged over 8 runs, with standard errors shown as shaded areas. . . . . . . 154 
xii
LIST OF TABLES 
2.1 Comparison of episodic reward-free algorithms. . . . . . . . . . . . . . . . . . . 13 
3.1 Cumulative reward for various exploration algorithms across different environ-
ments and tasks. The cumulative reward is averaged over 8 individual runs for 
both online exploration and offline planning. The result for each individual run 
is obtained by evaluating the policy network using the last-iteration parameter. 
Standard deviation is calculated across these runs. Results presented in boldface 
denote the best performance for each task, and those underlined represent the 
second-best outcomes. The cyan background highlights results of our algorithms. 101 
3.2 The common set of hyper-parameters. . . . . . . . . . . . . . . . . . . . . . . . 129 
3.3 Hyper-parameters of for GFA-RFE and baseline (ICM, Disagreement, RND). . . 130 
3.4 Hyper-parameters of for baseline algorithms (APT, SMM, DIAYN, APS). . . . . 131 
4.1 Instance-dependent regret bounds for different algorithms under the linear MDP 
setting. Here d is the dimension of the linear function ϕps, aq, H is the horizon 
length, ∆ is the minimal suboptimality gap. All results in the table represent high 
probability regret bounds. The regret bound depends the number of episodes K 
in He et al. (2021a) and the minimum positive eigenvalue λ of features mapping 
in Papini et al. (2021b). Misspecified MDP? indicates if the algorithm can 
(✓) handle the misspecified linear MDP or not (ˆ). . . . . . . . . . . . . . . . . 138 
4.2 Averaged cumulative regret and elapsed time of DS-OFUL over 8 runs. The bold 
face value indicates the best (low regret or low elapsed time) for all the algorithm 
configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150 
4.3 The number of remaining data samples after data processing with expected mis-
specification level . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153 
xiii
5.1 Instance-dependent regret bounds for different algorithms under the linear MDP 
setting. Here d is the dimension of the linear function ϕps, aq, H is the horizon 
length, ∆ is the minimal suboptimality gap. All results in the table represent high 
probability regret bounds. The regret bound depends the number of episodes K 
in He et al. (2021a) and the minimum positive eigenvalue λ of features mapping 
in Papini et al. (2021b). Misspecified MDP? indicates if the algorithm can 
(✓) handle the misspecified linear MDP or not (ˆ). . . . . . . . . . . . . . . . . 176 
5.2 Notations used in algorithm and proof . . . . . . . . . . . . . . . . . . . . . . . 195 
xiv
ACKNOWLEDGMENTS 
First and foremost, I would like to express my gratitude to my advisor, Quanquan Gu, for 
his consistent support, encouragement, and guidance throughout my Ph.D. career. Prior 
to my Ph.D., my research experience was limited and my mathematical background was 
modest. Quanquan generously provided help and constructive suggestions that lead me into 
the research community. I vividly remember that during the initial months of my Ph.D., 
he devoted considerable time to teaching me statistical tools and methodologies to write 
rigorous proofs in my papers. This not only solidified my understanding of machine learning 
but also showed me how to mentor and collaborate with students. Furthermore, I treasure 
the opportunity to work with the talented individuals in Quanquan’s lab. He has also en-
couraged me to build more collaborative relationships, particularly with interdisciplinary 
researchers, to broaden the application of my research across various topics. Through these 
collaborations, I have learned how to engage with researchers from different fields and men-
tor junior Ph.D. students. These will be invaluable in my future academic career. I also 
appreciate his pioneering vision in research, which not only focuses on insightful theoretical 
analysis but also on developing practical algorithms. This vision has greatly influenced my 
own research interests and objectives for the future. Finally, I appreciate his consistent belief 
in my potential and his encouragement to develop as an independent researcher. I would 
like to extend my deepest gratitude for his advice and wholehearted support regarding my 
career plans and job search. This guidance has deepened my understanding of academic 
communities and the path to becoming a respected researcher and successful professor in the 
future. 
I would like to express my sincere appreciation to the members of my doctoral commit-
tee: Richard E. Korf, Lihong Li, Baharan Mirzasoleiman, and Stanley J. Osher for their 
invaluable feedback and suggestions on my research ideas and thesis writing. Special thanks 
to Prof. Korf for his suggestion to present my research to a broad computer science audience, 
xv
which has been beneficial not only in thesis writing but also in preparing for job talks during 
my academic job search. 
I extend heartfelt gratitude to Lihong Li, Chong Liu, Hongning Wang, Wei Wang and 
Amy Zhang for their support and guidance in various collaborative projects. I am particularly 
fortunate to have published my first paper with Lihong, a pioneering researcher in this field. 
I also treasure the opportunity to work with Chong on interdisciplinary tasks, which have 
broadened my vision and shown me the vast possibilities of applying machine learning across 
multiple areas. I am immensely thankful to Joe Eaton, Bradley Rees and Xiaoyun Wang for 
their mentorship and support during my internship at NVIDIA. The industry experience has 
greatly enhanced my understanding of how my research applies to real-world applications. 
Throughout my PhD journey, I have had the fortune of collaborating with many tal-
ented individuals in Quanquan’s research team. My deepest gratitude goes to Yuan Cao, 
Jinghui Chen, Zixiang Chen, Qiwei Di, Jiafan He, Kaixuan Ji, Xuheng Li, Lingxiao Wang, 
Yue Wu, Pan Xu, Heyang Zhao, Dongruo Zhou and Difan Zou. I also appreciate the ex-
traordinary efforts of Jinghui Chen, Yuanzhou Chen, Yihe Deng, Zhiyuan Fan, Jiafan He, 
Benjamin Hoar, Zijie Huang, Jeehyun Hwang, Kaixuan Ji, Yiling Jia, Hongyuan Sheng, 
Jingwen Sun, Lingxiao Wang, Yue Wu, Pan Xu, Junkai Zhang, Linxi Zhao, Qingyue Zhao, 
Dongruo Zhou and Difan Zou in our collaborative projects. I’d also like to thank Guorui Chen 
and Huaxiu Yao for their advice in my job-hunting. I’d like to extend special thanks to Don-
gruo and Difan for their support throughout my PhD. I treasure the memories with Dongruo, 
hiking through the mountains, beaches and streets of LA. 
Furthermore, I would like to extend my appreciation to a group of friends not previously 
mentioned. I am grateful to Peilin Chai, Fan Jin, Zifeng Kang, Yiwen Lu, Wenhao Qi, 
Pengwei Wang, Yang Wang, Xinyu Yao, Qiuyang Yin, Tao Zhang and Haiyuan Zou for 
their consistent support throughout my five-year PhD journey. I treasure the times we 
spent hiking, playing badminton and tennis, and engaging in late-night conversations about 
history, the future, and life. I cherish the memory of visiting UCSD in 2020, the first time 
xvi
I ventured out from home during COVID. You all warmly welcomed me despite the risks 
associated with the pandemic. A special thank you to Fan for accompanying me on a journey 
across the US continent; I cannot imagine having done it without you. 
Finally, I’d like to extend my deepest gratitude to my parents, Kai and Longhua and 
my grandparents, Shifang and Yixin, for their understanding and unconditional support 
throughout my life. I am also profoundly thankful to Yijun for filling my life with love and 
happiness. Your encouragement and love are the greatest support on this wonderful journey. 
xvii
VITA 
2019 Bachelor of Engineering in Automation, Tsinghua University 
2019–2021 Research Assistant, Computer Science Department, University of Califor-
nia, Los Angeles 
2021–2022 Teaching Assistant, Computer Science Department, University of Califor-
nia, Los Angeles 
2022 Master of Science in Computer Science, University of California, Los An-
geles 
2023–2024 Research Assistant, Computer Science Department, University of Califor-
nia, Los Angeles 
PUBLICATIONS 
We select the publications that are most related to this dissertation 
˚ indicates equal contribution. 
1. Weitong Zhang, Dongruo Zhou, and Quanquan Gu. 2021. Reward-free model-
based reinforcement learning with linear function approximation. Advances in Neural 
Information Processing Systems 34, (2021), 1582–1593. Presented in Chapter 2. 
xviii
2. Junkai Zhang, Weitong Zhang, and Quanquan Gu. 2023. Optimal horizon-free 
reward-free exploration for linear mixture mdps. In International Conference on Ma-
chine Learning, PMLR, 41902–41930. Presented in Chapter 2. 
3. Junkai Zhang˚, Weitong Zhang˚, and Quanquan Gu. 2024. Uncertainty-Aware 
Reward-Free Exploration with General Function Approximation. To appear in Inter-
national Conference on Machine Learning, PMLR,. Presented in Chapter 3. 
4. Weitong Zhang, Jiafan He, Zhiyuan Fan, and Quanquan Gu. 2023. On the inter-
play between misspecification and sub-optimality gap in linear contextual bandits. In 
International Conference on Machine Learning, PMLR, 41111–41132. Presented in 
Chapter 4. 
5. Weitong Zhang˚, Zhiyuan Fan˚, Jiafan He, and Quanquan Gu. 2024. Settling Con-
stant Regrets in Linear Markov Decision Processes. arXiv preprint arXiv:2404.10745 
(2024). Presented in Chapter 5. 
xix
CHAPTER 1 
Introduction 
Recent years have witnessed great success of reinforcement learning (RL) in excelling at a 
wide spectrum of games, such as Atari (Mnih et al., 2013), Go (Silver et al., 2016) and 
even more complex games (Berner et al., 2019; Vinyals et al., 2019). In order to achieve 
these objectives, reinforcement learning agents usually need to explore and interact with 
the environment. By receiving the rewards which encode information about the goal of the 
task, the RL agents can learn through trial and error. Taking the Breakout game as an 
example, as presented in Figure 1.11, the RL agent observes visual input from the screen, 
which encodes information about the positions of the ball and paddle, as well as the brick 
structure. It needs to control a paddle to hit the moving ball, receiving positive rewards 
Figure 1.1: A screenshot of the Atari 
Breakout game. 
when the ball hits the bricks and negative re-
wards when the ball falls off the screen. Through 
exploring by randomly moving the paddle, the 
RL agent will learn that moving the paddle to the 
right in Figure 1.1’s situation will lead to a pos-
itive reward, whereas moving the paddle to the 
left will cause the agent to lose the game, thus 
yield a negative reward. Therefore, RL agents 
can leverage this information and learn to con-
quer the Breakout game or eventually beat human experts (Mnih et al., 2013). Besides being 
1Image credit: https://en.wikipedia.org/w/index.php?title=Breakout_(video_game)&oldid= 1224017580 
1
applied in games, RL has also emerged as a new paradigm for automatically solving more 
practical tasks such as recommendation systems (Li et al., 2011), robotic systems (Kober 
et al., 2013), and autonomous driving (Sallab et al., 2017), which all rely on interacting 
with the environment and dynamically making decisions based on the observations from the 
environment, such as the user feedback or the system response. 
Despite these advances, since massive interaction with the environment is a must in 
reinforcement learning, there are a series of crucial concerns that prevent RL from being 
applied to more serious tasks, such as drug design, scientific discovery, and clinical treatment 
design. These concerns usually consist of the efficiency and robustness of exploration for RL 
agents, especially in the face of uncertainty. This dissertation focuses on studying these 
concerns through theoretical analysis. Inspired by these insights, we also develop a series 
of algorithms that not only offer theoretical guarantees but also demonstrate competitive 
empirical performance. 
Figure 1.2: A screenshot of the Atari 
Montezuma’s Revenge. 
The first concern we would like to address is 
the case when the reinforcement learning agent 
is facing the “extrinsic” uncertainty when explor-
ing the “unknown” environment. In particular, 
we would like to address the efficiency of explo-
ration in reinforcement learning, especially ex-
ploration without human supervision or human-
crafted rewards. Usually, reward functions are 
human-crafted to encode the expected behavior 
of the agent. For example, in the Atari game Montezuma’s Revenge, as presented in Fig-
ure 1.22, the agent is designed to receive a reward of 1 when obtaining the key and 0 otherwise. 
However, it has been demonstrated that RL agents cannot perform well in environments with 
these sparse rewards (Kang et al., 2022) because the reward in most of the collected data 
2Image credit: https://www.retrogames.cz/play_124-Atari2600.php 
2
is zero. Therefore, more complicated and nontrivial rewards (Dilokthanakul et al., 2019) 
are crafted to guide the behavior of the agent. However, these reward-design processes are 
inefficient because they require a lot of trial and error to train the agent and adjust the 
reward. This difficulty also arises when applying RL to environments with limited human 
knowledge. For instance, when applying RL to drug discovery tasks (Popova et al., 2018), 
current human knowledge may not adequately describe the detailed mechanisms of some 
new proteins, making reward design challenging and requiring additional efforts. Moreover, 
this inefficiency also appears in multi-task robotics (Kalashnikov et al., 2022), where RL 
agents are expected to excel in multiple objectives instead of a single task. In such cases, 
using the reward for a single task would lead to repeated exploration of the environment 
and be inefficient. Therefore, since exploration using a single human-crafted reward raises 
efficiency issues, the question “How to explore the environment without human supervision 
or human-crafted rewards” becomes a natural concern for these tasks. 
To answer the previous question, Jin et al. (2020a) provided a theoretical framework 
called reward-free exploration (RFE) to force the agent to explore without reward signals. 
Over the past few years, there has been a body of work (Ménard et al., 2020; Wang et al., 
2020b; Zhang et al., 2020) theoretically improving the efficiency of RFE in the regime of 
“tabular RL,” where the state and action spaces are finite. On the other hand, Laskin et al. 
(2020) proposed an empirical framework called unsupervised reinforcement learning (URL) 
to pre-train the RL agent to explore the environment without the reward signals for any 
specific tasks. Then these pretrained models are expected to behave well in a spectrum of 
downstream tasks with different reward functions by simply fine-tuning on these tasks. In 
parallel with the development of theoretical analysis of RFE, there has also been a series of 
works (Pathak et al., 2017, 2019; Burda et al., 2018b) on empirically designing exploration 
heuristics for URL. 
Both RFE and URL aim to improve the efficiency of multi-task decision-making sys-
tems, such as multi-task robotics. In particular, both methods explore the environment by 
3
either collecting data (RFE) or learning good representations of the environment through 
a pretraining process (URL). Then, with different reward functions representing various 
downstream tasks, both methods can efficiently output the optimal policy without extensive 
interaction with the environment. Additionally, these methods both encourage exploration 
in environments that inherently lack rich reward information, like the aforementioned Mon-
tezuma’s Revenge. In Chapter 2, we make the first step in connecting RFE and URL by 
studying RFE in a more general case where the state and action spaces are too large to 
apply the “tabular RL” method. In this case, we study RL with function approximations so 
that the action space and the state space can be represented compactly (Sutton et al., 1998). 
We start from linear mixture MDP (Ayoub et al., 2020) which assumes that the transition 
kernel can be approximated by a linear function. Through uncertainty measurement under 
linear function approximation, we are able to deliver an RFE strategy that is guaranteed 
to efficiently explore the environment. In the latter part of Chapter 2, we seek to further 
improve the analysis and the design of the algorithm to make it optimal in various settings, 
such as the sparse reward setting. In Chapter 3, we further push the analysis to general 
function approximation. We design a practical RFE algorithm that not only enjoys the the-
oretical RFE guarantee but also has competitive performance on a set of URL benchmarks. 
The result builds a connection between RFE from a theoretical perspective and URL from 
an empirical perspective. 
When function approximation is used to compress the state and action space, yet an-
other crucial concern is whether the function approximation is expressive enough for making 
good decisions. Therefore, the second concern we would like to address is the case when 
the reinforcement learning is facing the “intrinsic” uncertainty from the expressiveness of 
the function approximation. For example, when using linear functions and linear regression 
to approximate the data generated by some quadratic function, one will suffer from model 
misspecification. Intuitively, a larger model misspecification will potentially have a more 
negative impact on decision-making systems. Existing theoretical RL literature (Jin et al., 
4
2020b; Zanette et al., 2020a) usually assumes that the function can perfectly approximate 
the ground truth function. When model misspecification exists, their analysis will leave an 
“approximation error” term indicating that the model will always make mistakes, regardless 
of the number of interactions (Takemura et al., 2021; Vial et al., 2022). In Chapter 4, we 
improve this analysis by connecting the “required precision” with the “model misspecifica-
tion” in misspecified contextual bandits, where the agent is only required to make a one-step 
decision. The “required precision” can generally be viewed as the difference between the best 
action and the second best action (a.k.a., suboptimality gap (Lattimore and Szepesvári, 
2020)). Obviously, when the “required precision” is larger than the “model misspecification”, 
it would be easy to distinguish the optimal action from the rest of the actions; thus, the agent 
will easily make the correct decision. Based on that observation, we propose an algorithm 
that actively learns from the data with higher uncertainty while filtering out the data about 
which the agent is certain. Intuitively, through this process we can guarantee that the agent 
will not be significantly affected by the model misspecification. We also reveal the interplay 
between the “misspecification level” and the “suboptimality gap”, indicating how large mis-
specification will prevent us from making good decisions. This positive result matches the 
negative result proposed in Lattimore et al. (2020). In Chapter 5, we extend this result to a 
general RL setting, i.e., sequential decision processes. We show that through an active data 
selection regime, the agent suffers only a finite suboptimality (a.k.a., constant regret) when 
making decisions over an infinite run, even when the model misspecification exists. This con-
stant regret result requires no prior assumption as made in Papini et al. (2021a); Zhang et al. 
(2021a), and the interaction between the “required precision” and “model misspecification” 
provide an insightful vision on the development of empirical robustness algorithms. 
5
1.1 Organization of the Dissertation 
The rest of this dissertation is organized as follows. In Chapter 2, we discuss reward-
free exploration under linear function approximation, which improves the previous results 
in the tabular setting with finite state and action spaces. An improved algorithm leverag-
ing variance information and an algorithm working in the bound total reward setting are 
presented in the latter part of Chapter 2. In Chapter 3, we extend RFE with linear func-
tion approximation to RFE with general function approximation. In addition to theoretical 
analysis, numerical experiments demonstrate that our reward-free exploration algorithm has 
competitive performance on a set of unsupervised reinforcement learning benchmarks. In 
Chapter 4, we move on to the second topic regarding the robustness of misspecified lin-
ear bandits (Li et al., 2010; Chu et al., 2011; Abbasi-Yadkori et al., 2011). By proposing 
an active data selection algorithm and revisiting an improved version of Chu et al. (2011), 
we show the interplay between model misspecification and the suboptimality gap. We are 
also able to deliver a high-probability constant regret for misspecified linear bandits without 
prior assumptions on contextual vectors. In Chapter 5, we extend this result to linear 
MDP (Jin et al., 2020b). By introducing the “certified estimator”, we are able to provide 
robust estimation for sequential decision processes in linear MDP and deliver a similar con-
stant regret bound. The conclusions are drawn in Chapter 6, which also includes the future 
directions and open questions in the unsupervised, reward-free reinforcement learning and 
the misspecified, robust reinforcement learning algorithms. 
1.2 Notation System in this Dissertation 
In this dissertation, scalars are denoted by lowercase letters. Vectors are denoted by lowercase 
boldface letters x, and matrices by uppercase boldface letters A. We denote by rks the set 
t1, 2, ¨ ¨ ¨ , ku for positive integers k. We use log x to denote the logarithm of x to the base 
2. For two nonnegative sequences tanu, tbnu, an “ Opbnq means that there exists a positive 
6
constant C such that an ď Cbn. Notation an “ Õpbnq means that there exists a positive 
constant k such that an “ Opbn log k bnq. Notation an “ Ωpbnq means that there exists a 
positive constant C such that an ě Cbn. Notation an “ Ω̃pbnq means there exists a positive 
constant k such that an “ Ωpbn log ´k bnq. Notation an “ ωpbnq means that limnÑ8 bn{an “ 0. 
For a vector x P Rd and a positive semidefinite matrix A P Rdˆd, we define }x}2A “ xJAx. 
For any set C, we use |C| to denote its cardinality. We denote the identity matrix by I and 
the empty set by H. The total variation distance of two distribution measures Pp¨q and Qp¨q 
is denoted by }Pp¨q ´Qp¨q}TV. Remaining notations are defined before they are used in each 
chapter. 
7
CHAPTER 2 
Uncertainty-Aware Reward-Free Exploration with Linear 
Function Approximation 
2.1 Introduction 
In this chapter, we study a theoretical framework for unsupervised exploration in reinforce-
ment learning, which is called reward-free exploration. In reinforcement learning (RL), an 
agent sequentially interacts with an environment and receives rewards from it. In many 
real-world RL problems, the reward function is designed manually to encourage the desired 
behavior of the agent. Thus, engineers have to change the reward function time by time 
and train the agent to check whether it has achieved the desired behavior. In this case, RL 
algorithms need to be repeatedly executed with different reward functions and are sample 
inefficient or even intractable. To tackle this challenge, Jin et al. (2020a) proposed a new 
reinforcement learning paradigm called Reward-Free Exploration (RFE), which explores the 
environment without using any reward function. In detail, the reward-free RL algorithm 
consists of two phases. The first phase is called the Exploration Phase, where the algorithm 
explores the environment without receiving reward signals. The second phase is called the 
Planning Phase, where the algorithm is given a specific reward function and uses the data 
collected in the first phase to learn the policy. In Figure 2.1 we provide a comparison be-
tween the classical “reward-aware” exploration and the proposed “reward-free” exploration 
when the RL agent is asked to learn three tasks (e.g., ice skating, swimming and playing 
golf). Reward-aware exploration (Figure 2.1a) explores the environment with a single, spe-
8
Agent Environment 
Action a 
Observation  s 
Reward r1 
Online RL 
Agent Environment 
Action a 
Observation  s 
Reward r2 
Online RL 
Agent Environment 
Action a 
Observation  s 
Reward r3 
Online RL 
(a) Reward-aware exploration 
Agent Environment 
Action a 
Observation  s 
Dataset 𝒟 = {s, a, s′ } 
𝒟3 = {s, a, s′ , r3} 
𝒟1 = {s, a, s′ , r1} 
𝒟2 = {s, a, s′ , r2} 
Online data collection Offline RL 
(b) Reward-free exploration 
Figure 2.1: Comparison between (a) the “reward-aware” exploration and (b) the “reward-free” 
exploration. 
cific reward so when the reward changes, the agent needs to repeat the exploration to adapt 
the new reward function. Reward-free exploration, as presented in Figure 2.1b, aim to learn 
a dataset without the reward function, which can potentially transferred to any single reward 
without explore the environment again. 
As a first step for reward-free exploration, Jin et al. (2020a) has shown that this explo-
ration paradigm can learn a near-optimal policy in the planning phase given any reward 
function after collecting a polynomial number of episodes in the exploration phase. The 
subsequent work (Kaufmann et al., 2021a; Ménard et al., 2020; Zhang et al., 2020) proposed 
improved algorithms to achieve a better or nearly optimal sample complexity. 
All of the aforementioned works are focused on the tabular Markov decision process 
(MDP), where the number of states and the number of actions are finite. In practice, the 
9
number of states and actions can be large or even infinite, for example, in a Go game (Silver 
et al., 2016), the number of states is typically as large as 10360, making it impossible to apply 
tabular methods that store data as a table of states. In the Atari games (Mnih et al., 2013), 
the input is usually a 210 ˆ 160 image representing the visual input from the video game. 
In both of these cases, function approximations (usually neural networks) are required for 
the sake of computational tractability and generalization. However, the understanding of 
function approximation for reward-free exploration, even under the simplest linear function 
approximation, remains underexplored. To mention a few, Wang et al. (2020b) studied linear 
MDPs (Yang and Wang, 2019; Jin et al., 2020b), where both the transition probability and 
the reward function admit linear representations, and proposed a reward-free RL algorithm 
with a Õpd3H6ϵ´2q sample complexity, where d is the dimension of the linear representation, 
H is the planning horizon, and ϵ is the required accuracy. They also proved that if the 
optimal state-action function is linear, then the reward-free exploration needs an exponential 
number of episodes in the planning horizon H to learn an ϵ-optimal policy. Zanette et al. 
(2020d) considered a slightly larger class of MDPs with low inherent Bellman error (Zanette 
et al., 2020b), and proposed an algorithm with Õpd3H5ϵ´2q sample complexity. However, 
both works assume that the reward function is a linear function over some feature mapping. 
Moreover, the lower bound proved in (Wang et al., 2020b) is for a very large class of MDPs 
where the optimal state-action function is linear, thus it is too conservative and cannot 
determine the information-theoretic limits of reward-free exploration for linear MDPs or 
related models. 
2.1.1 Organization of this Chapter 
In this chapter, we seek a theoretical understanding of the statistical efficiency for reward-free 
RL with linear function approximation. This chapter is organized as follows. In Section 2.2, 
we review the related literature. In Section 2.3, we present the basic assumption of RL 
with linear function approximation and the rigorous definition of reward-free exploration. 
10
The preliminary algorithm and analysis are presented in Section 2.4. In Section 2.5, we 
seek to improve the sample complexity by incorporating the variance information into our 
algorithm. In Section 2.6, we further extend the algorithm to a long-horizon setting and 
present a nearly-minimax-optimal algorithm which does not suffer from curse of horizon in 
RL. The conclusion is drawn in Section 2.7 and we defer the detailed proof of the theorems 
to Section 2.8. 
2.2 Related Works 
2.2.1 Reinforcement Learning with Linear Function Approximation 
In recent years, a series of works have been devoted to the study of RL with linear function 
approximation (Jiang et al., 2017; Dann et al., 2018; Yang and Wang, 2019; Wang et al., 
2019; Du et al., 2019; Sun et al., 2019; Jin et al., 2020b; Zanette et al., 2020a,b; Yang and 
Wang, 2020a; Modi et al., 2020; Ayoub et al., 2020; Jia et al., 2020; Cai et al., 2020; Weisz 
et al., 2021; Zhou et al., 2021c,a; He et al., 2022a; Agarwal et al., 2022). Our work belongs 
to the linear mixture MDP setting (Yang and Wang, 2019; Modi et al., 2020; Ayoub et al., 
2020; Jia et al., 2020; Zhou et al., 2021a,c), where the transition kernel can be parame-
terized as a linear combination of some basic transition probability functions. Zhou et al. 
(2021a) firstly achieved minimax regret Õ ` 
dH ? T ˘ 
in linear mixture MDPs by proposing 
a Bernstein-type concentration inequality for self-normalized martingales. Another kind of 
popular linearly parameterized MDP is linear MDP (Wang et al., 2019; Du et al., 2019; 
Yang and Wang, 2020a; Jin et al., 2020b; Zanette et al., 2020a; Wang et al., 2020c; He 
et al., 2021a), which assumes that both transition probability and reward function are lin-
ear functions of known feature mappings in state-action pairs. In this setting, Jin et al. 
(2020b) first proposed the statistically and computationally efficient algorithm LSVI-UCB 
and achieved a Õ ´? 
d3H3T ¯ 
regret bound. Recent works (He et al., 2022a) further achieved 
nearly minimax optimal regret Õpd ? H3Kq by proposing the computationally efficient algo-
11
rithm LSVI-UCB++. Its concurrent work (Agarwal et al., 2022) achieves a similar result 
under assumption řH 
h“1 rhpsh, ahq ď 1 with regret upper bound of Õpd ? HT ` d6H5q. 
2.2.2 Reward-free Exploration 
Exploration efficiency has always been a popular topic in RL. sophisticated exploration 
strategies like E3 (Kearns and Singh, 2002) have been proposed to guide the exploration and 
these algorithms are proved to require only polynominal time to explore the environment. 
Unlike standard RL settings in which the agent interacts with the environment with reward 
signals, reward-free exploration (Jin et al., 2020a) in RL introduced a two-phase paradigm. 
In this approach, the agent initially explores the environment without any reward signals. 
Then, upon receiving the reward functions, it outputs a policy that maximizes the cumula-
tive reward, without any further interaction with the environment. Jin et al. (2020a) first 
achieved ÕpH5S2A{ϵ2q sample complexity in tabular MDPs by executing exploratory policy 
visiting states with probability proportional to its maximum visitation probability under any 
possible policy. Subsequent works (Kaufmann et al., 2021b; Ménard et al., 2021) proposed 
algorithms RF-UCRL and RF-Express to gradually improve the result to Õ pH3S2Aϵ´2q. 
The optimal sample complexity bound rOpH2S2Aϵ´2q was achieved by the algorithm SSTP 
proposed in Zhang et al. (2020), which matched the lower bound provided in Jin et al. (2020a) 
up to logarithmic factors. Recent years have witnessed a trend of reward-free exploration in 
RL with function approximations, while most of these works are considering linear function 
approximation: In the linear MDP setting, Wang et al. (2020b) proposes an exploration-
driven reward function, and the minimax optimal bound was achieved by Hu et al. (2022) 
by introducing weighted regression into the algorithm. In linear mixture MDPs, Zhang et al. 
(2021e) proposed the ‘pseudo reward’ to encourage exploration, Chen et al. (2021); Wagen-
maker et al. (2022) improved the sample complexity by introducing a more complicated, 
recursively defined pseudo reward. The minimax optimal sample complexity, Õpd2{ϵ2q was 
1Time means if the algorithm is time-homogeneous (✓) or not (ˆ). 
12
Table 2.1: Comparison of episodic reward-free algorithms. 
Setting Algorithm Rewards Scale Time1 Sample Complexity 
Jin et al. (2020a) rhpsh, ahq P r0, 1s ˆ rOpH5S2Aε´2q 
Kaufmann et al. (2021a) rhpsh, ahq P r0, 1s ˆ rOpH4S2Aε´2q 
Tabular Ménard et al. (2021) rhpsh, ahq P r0, 1s ˆ rOpH3S2Aε´2q 
MDP Zhang et al. (2020) řH 
h“1 rhpsh, ahq ď 1 ✓ rOpS2Aε´2q 
Lower bound 
(Jin et al., 2020a) rhpsh, ahq P r0, 1s ˆ ΩpH2S2Aε´2q 
Lower bound 
(Zhang et al., 2020) 
řH h“1 rhpsh, ahq ď 1 ✓ ΩpS2Aε´2q 
Linear Wang et al. (2020b) rhpsh, ahq P r0, 1s ˆ rO ` 
H6d3ε´2 ˘ 
MDP Zanette et al. (2020d) rhpsh, ahq P r0, 1s ˆ rO ` 
H5d3ε´2 ˘ 
Wagenmaker et al. (2022) rhpsh, ahq P r0, 1s ˆ rO ` 
H5d2ε´2 ˘ 
Theorem 2.5.1 rhpsh, ahq P r0, 1s ✓ rO ` 
H4dpH ` dqε´2 ˘ 
Linear Chen et al. (2021) rhpsh, ahq P r0, 1s ˆ rO ` 
H3dpH ` dqε´2 ˘ 
Mixture Corollary 2.6.4 řH 
h“1 rhpsh, ahq ď 1 ✓ rOpd2ε´2q 
MDP Corollary 2.6.6 řH 
h“1 rhpsh, ahq ď H ✓ ÕpH2d2ε´2q 
Lower bound (Thm. 2.6.8) řH 
h“1 rhpsh, ahq ď 1 ✓ Ω ` 
d2ε´2 ˘ 
Lower bound (Cor. 2.6.10) rhpsh, ahq P r0, 1s ✓ ΩpH2d2ε´2q 
achieved by Zhang et al. (2023a) in the horizon-free setting. Moving forward, in the general 
function approximation setting, Kong et al. (2021) used ‘online sensitivity score’ to esti-
mate the information gain. As a result, they were able to provide a sample complexity of 
Õpd4H6ϵ´2q. Here, d represents the dimension of contexts when the problem is reduced to 
linear function approximations. Yet another line of works (Chen et al., 2022a,b) aimed to 
follow the Decision-Estimation Coefficient (DEC, Foster et al. 2021) and provided a uni-
fied framework for reward-free exploration with general function approximations, achieving 
a ÕppolypHqd2ϵ´2q, nevertheless, all existing works with general function approximations 
13
leave a huge gap between their proposed upper bound and lower bound, even when reduced 
to linear settings. We record existing results in Table 2.1. 
2.2.3 The Curse of Horizon in Reinforcement Learning 
The long planning horizon has long been viewed as RL’s main challenge. However, a series 
of works have shown that RL is no more difficult than contextual bandits by removing the 
influence of the total reward scale. In tabular MDPs, the algorithm proposed in Wang 
et al. (2020a) first achieved the polylogarithmic H dependency sample complexity bound 
ÕpS5A4ε´2q by carefully reusing samples and avoiding unnecessary sampling. Zhang et al. 
(2021c) further proposed an improved algorithm MVP to achieve the near-optimal regret 
bound Õp ? SAK ` S2Aq based on a new Bernstein-type bonus. Similar polylogarithmic 
dependency bounds H had been established by Ren et al. (2021) for linear MDP with 
anchor points, Tarbouriech et al. (2021) for the stochastic shortest path. Li et al. (2022) 
achieved the surprising H independent sample complexity bound OppSAqOpSqε´5q by building 
a connection between discounted MDPs and episodic MDPs and a novel perturbation analysis 
in MDPs. The algorithm proposed by Zhang et al. (2022) further improved the sample 
complexity to OpS9A3ε´2polylogpS,A, ε´1qq only polynomially depending on the size of the 
state and the action spaces by exploiting the power of stationary policy. Thanks to the linear 
function approximation, Zhou and Gu (2022a) first achieves the horizon-free regret bound 
Õpd ? K`d2q independently of the size of the state and action spaces. However, all the above 
works are limited to standard RL settings. In the paradigm of reward-free exploration, the 
only horizon-free result was achieved by Zhang et al. (2021b) with sample complexity bound 
of ÕpS2Aε´2q, where the polynomial dependency on S and A is still unacceptable when the 
state space and action space are large. Our algorithm HF-UCRL-RFE++ establishes the 
first horizon-free sample complexity bound independent of the size of the state space and 
action space in reward-free exploration. 
14
2.3 Preliminaries 
2.3.1 Episodic Markov Decision Processes 
We consider episodic finite-horizon Markov Decision Processes (MDPs), which are denoted 
by a tuple MpS,A, H, trhuHh“1,Pq. Here S is the countable state space (may be infinite), A 
is the action space, H is the length of the episode, and rh : S ˆ A Ñ r0, 1s is the reward 
function. Without loss of generality, we assume that the reward function rh is deterministic. 
Pps1|s, aq is the transition probability function that denotes the probability for state s to 
transit to state s1 given the action a at step h. A policy πh : S Ñ A is a function that maps 
a state s to an action a. We define the action-value function (i.e., Q-function) Qπ hps, aq as 
follows: 
Qπ hps, a; trhuhq “ E 
„ H ÿ 
h1“h 
rh1psh1 , ah1q 
ˇ 
ˇ 
ˇ 
ˇ 
sh “ s, ah “ a 
ȷ 
, V π h ps; trhuhq “ Qπ 
hps, πhpsq; trhuhq. 
For simplicity, we denote Qπ hps, a; rq “ Qπ 
hps, a; trhuhq and V π h ps; rq “ V π 
h ps; trhuhq. We define 
the optimal value function tV ˚ h uHh“1 and the optimal state-action value function tQ˚ 
huHh“1 as 
V ˚ h ps; rq “ supπ V 
π h ps; rq and Q˚ 
hps, a; rq “ supπ Q π hps, a; rq respectively. For any function 
V : S Ñ R, we denote rPV sps, a; rq “ Es1„Pp¨|s,aqV ps1; rq, and denote the variance of V as 
rVf sps, aq “ rPf 2 sps, aq ´ 
` 
rPf sps, aq 2 ˘ 
. (2.3.1) 
In particular, we have the following Bellman equation, as well as the Bellman optimality 
equation: 
Qπ hps, a; rq “ rhps, aq ` rPV π 
h`1sps, a; rq, Q˚ hps, a; rq “ rhps, aq ` rPV ˚ 
h`1sps, a; rq. 
In this paper, we focus on model-based algorithms and consider the following linear mix-
ture/kernel MDP (Modi et al., 2020; Jia et al., 2020; Ayoub et al., 2020; Zhou et al., 2021d), 
which assumes that the transition probability P is a linear mixture of d signed basis measures. 
Meanwhile, for any function V , we assume that we can do the summation ř 
s1PS ϕps1|s, aqV psq 
efficiently, e.g., using the Monte Carlo method (Yang and Wang, 2020b). 
15
Definition 2.3.1 (Linear Mixture MDPs (Jia et al., 2020; Ayoub et al., 2020; Zhou et al., 
2021d)). The unknown transition probability P is a linear combination of d signed basis 
measures ϕips 1|s, aq, that is, Pps1|s, aq “ 
řd i“1 ϕips 
1|s, aqθ˚ i . Meanwhile, for any V : S Ñ r0, 1s, 
i P rds, ps, aq P S ˆA, the calculation of the summation ř 
s1PS ϕips 1|s, aqV ps1q is feasible. For 
simplicity, let ϕ “ rϕ1, . . . , ϕdsJ, θ˚ “ rθ˚ 1 , . . . , θ 
˚ d sJ and ψV ps, aq “ 
ř 
s1PS ϕps1|s, aqV ps1q. 
Without loss of generality, we assume }θ˚}2 ď B, }ψV ps, aq}2 ď 1 for all V : S Ñ r0, 1s and 
ps, aq P S ˆ A. 
Remark 2.3.2. A similar but notably different definition (i.e., linear MDPs (Yang and 
Wang, 2019; Jin et al., 2020b)) has been used in Wang et al. (2020b), which assumes that 
Pps1|s, aq “ xϕps, aq,µps1qy and rh “ xϕps, aq,θhy, µhp¨q is a measure and θh is an unknown 
vector. Comparing with linear MDPs, linear mixture MDPs do not need the reward function 
r to be linear, which makes our algorithms more general. 
With Definition 2.3.1, it is easy to verify that the expectation of any bounded function 
V is a linear function of ψ: 
rPV sps, aq “ xψV ps, aq,θ˚ y. (2.3.2) 
2.3.2 Formal Definition of Reward-Free Exploration 
For reward-free exploration, the algorithm can be divided into two phases: exploration phase 
and planning phase. In the exploration phase, the algorithm cannot access the reward 
function but collect K episodes by doing exploration. In the planning phase, the algorithm 
is given a series of reward functions and find the optimal policy based on these reward 
functions, using the K episodes collected in the exploration phase. We formally define pϵ, δq-
learn and sample complexity of the algorithm as follows (Jin et al., 2020a). 
Definition 2.3.3 (pϵ, δq-learnability). Given an MDP transition kernel set P , reward func-
tion set R and a initial state distribution µ, we say a reward-free algorithm can pϵ, δq-learn 
16
the problem pP ,Rq with sample complexity Kpϵ, δq, if for any transition kernel P P P , af-
ter receiving Kpϵ, δq episodes in the exploration phase, for any reward function r P R, the 
algorithm returns a policy π in planning phase, such that with probability at least 1 ´ δ, 
Es1„µrV ˚ 1 ps1; rq ´ V π 
1 ps1; rqs ď ϵ. 
2.4 Theoretical Guaranteed Reward-Free Exploration 
In this section, we propose a reward-free algorithm. This algorithm works as follows: Firstly, 
during the exploration phase, it samples the MDP episodes, build an estimator θ for the 
MDP parameter θ˚, and compute the covariance matrix Σ of the feature mappings, which 
characterizes the uncertainty of the estimator θ. Secondly, during the planning phase, the 
algorithm uses the collected θ and Σ in the exploration phase to find the optimal policy π 
based on the given reward functions. 
2.4.1 Proposed Algorithms 
2.4.1.1 Planning Phase Algorithm 
We first introduce the PLAN function (Algorithm 1), which is a common module in both 
planning phase and exploration phase. Given a series of reward functions trhuh, the goal of 
PLAN function is to output the optimal policies tπhuh and Q-functions tQhuh corresponding 
to trhuh. Suppose the parameter θ˚ is known, we can compute tQhuh recursively by the 
following Bellman equation: 
Qhps, a; rq “ rhps, aq ` rPVh`1sps, a; rq “ rhps, aq ` xψVh`1 ps, aq,θ˚ 
y, (2.4.1) 
Qhps, a; rq can be viewed as the summation of the reward function rhps, aq and a linear 
function xψVh`1 ps, aq,θ˚y. However, since θ˚ is unknown, we cannot compute Qh as in 
(2.4.1). Instead, PLAN takes the estimated parameter θ and the “covariance matrix” Σ as 
input. To calculate Qh, PLAN replaces θ˚ with the estimated θ and plus an additional 
17
Algorithm 1 UCRL-RFE Planning Module (PLAN) 
Input: Estimated parameter and covariance θ,Σ, reward trhuHh“1, parameter β. 
1: For consistency, set QH`1p¨, ¨q Ð VH`1p¨q Ð 0 
2: for h “ H,H ´ 1, ¨ ¨ ¨ , 1 do 
3: Compute Q function as Qhp¨, ¨q Ð “ 
rhp¨, ¨q ` @ 
ψVh`1 p¨, ¨q,θ 
D 
` β}ψVh`1 p¨, ¨q}Σ´1 
‰ 
p0,Hq 
4: Compute value function Vhp¨q Ð maxaPAQhp¨, aq 
5: Compute policy as πhp¨q Ð argmaxaPAQhp¨, aq. 
6: end for 
Output: Policy π Ð tπhuHh“1 and tVhuHh“1 
exploration bonus term β}ψVh`1 p¨, ¨q}Σ´1 to (2.4.1), as in Line 3 of Algorithm 1. Then PLAN 
takes the greedy policy of the calculated optimistic Qh and proceeds to the previous step. 
Finally, the algorithm returns policy π in Line 5 as well as the estimated value functions 
tVhuh. 
2.4.1.2 Exploration Phase Algorithm 
Based on the introduced PLAN function, we propose the UCRL-RFE algorithm in Algo-
rithm 2. In general, UCRL-RFE guides the agent to explore the unknown state space 
without the information of the reward functions. In detail, for the k-th episode, UCRL-RFE 
first defines the exploration driven reward function as follows: 
rkhps, aq “ min 
" 
1, 2β 
H 
c 
max fPS ÞÑr0,H´hs 
}ψf ps, aq}Σ´1 1,k 
* 
, (2.4.2) 
where Σ1,k is the “covariance matrix” of the feature mapping. Intuitively speaking, rkhps, aq 
represents the maximum possible uncertainty level of the state-action pair ps, aq caused by 
the randomness of the MDP transition function, which is independent of the true reward 
functions. Therefore, in order to obtain a good estimation of the optimal policy for any given 
reward functions, it suffices to obtain the optimal policy for rkhps, aq. Thus, after obtaining 
trkhuh, UCRL-RFE finds the corresponding near-optimal policies tπk huh using PLAN function, 
18
with the estimated parameter θk and the “covariance matrix” Σ1,k as input. UCRL-RFE 
uses tπk huh as its exploration policy and observes the new episode sk1, a 
k 1, . . . , s 
k H , a 
k H induced 
by tπk huh. 
Next, UCRL-RFE needs to compute the parameters θk`1 and Σ1,k`1 for planning in the 
next episode. Similar to UCRL-VTR proposed by (Jia et al., 2020; Ayoub et al., 2020), 
UCRL-RFE also uses a “value-targeted regression (VTR)" estimator, which computes θk`1 
as the minimizer to a ridge regression problem with the target being the past value functions. 
The main difference between UCRL-RFE and UCRL-VTR is that, due to the lack of true 
reward functions, UCRL-RFE can not use the estimated value functions as its regression 
targets. Instead, UCRL-RFE defines the following pseudo value function uk h: 
uk h “ argmax 
fPS ÞÑr0,H´hs 
ψJ f pskh, a 
k hqΣ´1 
1,kψf pskh, a k hq. (2.4.3) 
Here, uk h maximizes the “uncertainty" caused by the transition kernel, which will help the 
agent to explore the state space. Now given the pseudo value functions, Algorithm 2 com-
putes the estimated θk`1 as the minimizer to the following ridge regression problem: 
θk`1 Ð argmin θ 
λ}θ} 2 2 ` 
k ÿ 
k1“1 
H ÿ 
h“1 
´ 
@ 
θ,ψuk1 
h psk 
1 
h , a k1 
h q D 
´ uk1 
h psk 1 
h`1q 
¯2 
, (2.4.4) 
which has a closed-form solution as in Line 12. It also updates the covariance matrix Σ1,k`1 
as in Line 12, by the observed feature mapping tψuk h pskh, a 
k hquh in the current episode. In 
the end, after collecting HK state-action samples, UCRL-RFE calculates the policy tπhu as 
output based on θK`1 and Σ1,K`1. 
Remark 2.4.1. Here we do a comparison between our UCRL-RFE and the reward-free RL 
algorithm in Wang et al. (2020b). The main difference is that Wang et al. (2020b) estimates 
θk by regression with the value function V k h being the target, while our UCRL-RFE does 
regression with the pseudo-value function uk h being the target. That is mainly due to the 
different problem settings (linear MDP vs. linear mixture MDP). 
19
Algorithm 2 UCRL-RFE (Hoeffding Bonus) Input: Confident parameter β, regularization parameter λ 
1: Phase I: Exploration Phase 
2: Initialize Σ1,1 Ð λI,b1 Ð θ1 Ð 0 
3: for k “ 1, 2, ¨ ¨ ¨ , K do 
4: Compute the exploration driven reward function trkhp¨, ¨quHh“1 according to (2.4.2) 
5: Compute exploration policy and value function as ptπk hu 
H h“1, tV k 
h u H h“1q Ð 
PLANpθk,Σ1,k, trkhu H h“1, βq 
6: Receive the initial state sk1 „ µ 
7: for h “ 1, 2, ¨ ¨ ¨ , H do 
8: Take action akh Ð πk hpskhq and receive skh`1 
9: Calculate uk h for skh, a 
k h according to (2.4.3) 
10: Set Σh`1,k Ð Σh,k `ψuk h pskh, a 
k hqψuk 
h pskh, a 
k hqJ,bh`1,k Ð bh,k `ψuk 
h pskh, a 
k hquk 
hpskh`1q 
11: end for 
12: Set Σ1,k`1 Ð ΣH`1,k, b1,k`1 Ð bH`1,k,θk`1 Ð Σ´1 1,k`1b1,k`1 
13: end for 
14: Phase II: Planning Phase 
15: Receive target reward function trhuHh“1 
16: Compute policy as ptπhu H h“1, tVhu 
H h“1q Ð PLANpθK`1,Σ1,K`1, trhu 
H h“1, βq 
Output: Policy tπhuHh“1 
Remark 2.4.2 (Implementation Details). In general, solving the maximization problem 
(2.4.3) is hard. Here, we provide a simple approximate solution to the problem (2.4.2) 
and (2.4.3) for the finite state space case (|S| ă 8). Instead of maximizing the ℓ2 norm-
based objective › 
›Σ ´1{2 1,k ψf pskh, a 
k hq › 
› 
2 , we write ψf ps, aq “ Φps, aqf with 
Φps, aq “ pϕps, a, S1q, ¨ ¨ ¨ ,ϕps, a, S|S|qq, f “ pfpS1q, ¨ ¨ ¨ , fpS|S|qq J. 
By relaxing the ℓ2 norm into ℓ1 norm due to }x}2 ě }x1}1{ ? d for any x P Rd, we reach a 
20
surrogate objective: 
max f 
› 
›Σ ´1{2 1,k Φps, aqf 
› 
› 
1 subject to }f}8 ď H ´ h, (2.4.5) 
which can be further formulated as a linear programming problem, and solved by interior 
method (Karmarkar, 1984) or simplex method (Dantzig, 1965) efficiently. Since }x}1{ ? d ď 
}x}2 ď }x}1, the performance of this approximate solution is guaranteed. For the case where 
the state space is infinite, we can use state aggregation methods such as soft state aggregation 
(Michael and Jordan, 1995) to reduce the infinite state space to a finite state space and then 
apply the above approximate solution to solve it. 
2.4.2 Sample Complexity Analysis 
Now we provide the sample complexity for Algorithm 2. 
Theorem 2.4.3 (Sample complexity of UCRL-RFE). For Algorithm 2, setting parameter 
β “ H a 
d logp3p1 ` KH3B2q{δq`1, λ “ B´2, then for any 0 ă ϵ ă 1, if K “ ÕpH5d2ϵ´2q, 
we have with probability at least 1´δ that, for any reward function r, Algorithm 2 produces 
a policy π with Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď ϵ. 
Remark 2.4.4. Theorem 2.4.3 shows that UCRL-RFE only needs polypd,H, ϵ´1q sample 
complexity to find an ϵ-optimal policy, which suggests that model-based reward-free algo-
rithm is sample-efficient. Thanks to the linear function approximation, the sample complex-
ity depends only on the dimension of the feature mapping d and the length of the episode 
and does not depend on the cardinality of the state and action spaces. 
Corollary 2.4.5. Under the same conditions as in Theorem 2.4.3, if solving the relaxed 
optimization problem in (2.4.5), Algorithm 2 has K “ ÕpH5d3ϵ´2q sample complexity. 
21
2.5 Improved Algorithm and Analysis with Variance Information 
Theorem 2.4.3 suggests that UCRL-RFE in Algorithm 2 enjoys an ÕpH5d2ϵ´2q sample com-
plexity to find an ϵ-optimal policy. In this section, we seek to further improve the sample 
complexity. 
A key observation is that for any given reward function trhuh, the error between the 
exploration policy tπhuh and the optimal policy can be decomposed into two parts: the 
exploration error which is the difference between trhuh and the exploration-driven reward 
function trkhuh, and the approximation error which is the difference between the optimal 
value function V ˚ 1 p¨; rkhq and our estimated value function V 
πk h 
1 p¨; rkhq with respect to trkhuh. 
For the latter, our exploration strategy adapted from VTR is often too conservative since it 
does not distinguish different value functions and state-action pairs from different episodes 
and steps. Therefore, inspired by (Zhou et al., 2021a), we propose a variant of UCRL-RFE 
called UCRL-RFE+, which adopts a Bernstein-type bonus for exploration and achieves a 
better sample complexity. 
2.5.1 Exploration Phase Algorithm with Variance Information 
UCRL-RFE+ is presented in Algorithm 3. The structure of the algorithm is similar to that 
of UCRL-RFE, which can be decomposed into the exploration phase and the planning phase. 
There are two main differences. First, in contrast to UCRL-RFE which uses θk for the PLAN 
function in both exploration and planning phases, UCRL-RFE+ only uses θK`1 for the PLAN 
function in the planning phase. For the exploration phase, UCRL-RFE+ constructs a new 
estimator θ̂k based on tV k1 
h`1uk1ďk´1,h, which are the value functions of the exploration-driven 
rewards. Second, to build θ̂k, one way is to choose it as a solution to the ridge regression 
problem with contexts ψV k1 
h`1 psk 
1 
h , a k1 
h q and targets V k1 
h`1psk 1 
h`1q, similar to (2.4.4). However, 
since the targets V k1 
h`1ps k1 
h`1q have different variances at different steps and episodes, we are 
actually facing a heteroscedastic linear regression problem. Therefore, inspired by a recent 
22
Algorithm 3 UCRL-RFE+ (Bernstein Bonus) 
Input: Parameter β, β̂, β̃, β̌, regularization parameter λ 
1: Stage I: Exploration Phase 
2: Initialize Σ1,1 “ Σ̂1,1 “ Σ̃1,1 “ λI,b1 “ b̂1 “ b̃1 “ θ1 “ θ̂1 “ θ̃1 “ 0 
3: for k “ 1, 2, ¨ ¨ ¨ , K do 
4: Set trkhp¨, ¨quHh“1 to (2.4.2). 
5: Set ptπk hu 
H h“1, tV k 
h u H h“1q Ð PLANpθ̂k, Σ̂1,k, trkhu 
H h“1, β̂q 
6: Receive the initial state sk1 „ µ. 
7: for h “ 1, 2, ¨ ¨ ¨ , H do 
8: Take action akh “ πk hpskhq and receive skh`1 
9: Calculate uk h, ν 
k h for skh, a 
k h according to (2.4.3) and (2.5.2) separately 
10: Set Σh`1,k Ð Σh,k `ψuk h pskh, a 
k hqψuk 
h pskh, a 
k hqJ 
11: Set Σ̂h`1,k, Σ̃h`1,k, b̂h`1,k, b̃h`1,k using (2.5.4) 
12: end for 
13: Set Σ1,k`1 Ð ΣH`1,k 
14: Set Σ̂1,k`1 Ð Σ̂H`1,k, b̂1,k`1 Ð b̂H`1,k, θ̂k`1 Ð Σ̂´1 1,k`1b̂1,k`1 
15: Set Σ̃1,k`1 Ð Σ̃H`1,k, b̃1,k`1 Ð b̃H`1,k, θ̃k`1 Ð Σ̃´1 1,k`1b̃1,k`1 
16: end for 
17: Set θK`1 Ð Σ´1 1,K`1 
řK k“1 
řH h“1ψuk 
h pskh, a 
k hquk 
hpskh`1q 
18: Stage II: Planning Phase 
19: Receive target reward function trhuHh“1 
20: Compute the exploration policy as ptπhuHh“1, tVhuHh“1q Ð PLANpθK`1,Σ1,K`1, trhuHh“1, βq 
Output: Policy tπhuHh“1 
line of work Zhou et al. (2021a); Wu et al. (2021) using Bernstein inequality for vector-
valued self-normalized martingale to construct a tighter confidence ball for exploration, we 
also incorporate the variance to build choose θ̂k as the solution to the following weighted 
23
ridge regression problem, which is an enhanced estimator for the heteroscedastic case: 
θ̂k Ð argmin θ 
λ}θ} 2 2 ` 
k´1 ÿ 
k1“1 
H ÿ 
h“1 
´ 
@ 
θ,ψV k1 
h`1 psk 
1 
h , a k1 
h q D 
´ V k1 
h`1ps k1 
h`1q 
¯2 
{rσk1 
h s 2, (2.5.1) 
where rσk1 
h s2 is the variance of V k1 
h`1ps k1 
h`1q. The idea of using variances to improve the sample 
complexity is closely related to the use of “Bernstein bonus" in reward-free RL for the tab-
ular MDPs (Kaufmann et al., 2021a; Zhang et al., 2020; Ménard et al., 2020). Since σk1 
h is 
unknown, we will use νk1 
h “ rσ̄k1 
h s2 as a plug-in estimator to replace rσk1 
h s2 in (2.5.1). After ob-
taining θ̂k, UCRL-RFE+ sets Σ̂1,k as the covariance matrix of the features ψV k h`1 
pskh, a k hq{σ̄k 
h, 
and feeds it into the PLAN function with the exploration-driven reward functions and the con-
fidence radius β̂. UCRL-RFE+ takes the output tπk huh as the exploration policy and tV k 
h uh 
as the value functions to construct the estimator θ̂k`1 for the next episode. In the end, when 
it comes to the planning phase, after receiving the reward functions trhuh, UCRL-RFE+ 
takes θK`1 as the solution to the ridge regression problem with contexts tψuk h pskh, a 
k hquk,h and 
targets tuk hpskh`1quk,h, and the covariance matrix Σ1,K`1 as input, and uses PLAN to find the 
near-optimal policy tπhuh with confidence radius β. It remains to specify νk h in the weighted 
ridge regression. On the one hand, we need νk h to be an upper bound of rσk 
hs2. On the other 
hand, we require νk h to have a strictly positive lower bound to let (2.5.1) be valid. Therefore, 
we construct νk h as follows: 
νk h “ maxtα, V̄k 
hpskh, a k hq ` Eh 
k pskh, a k hqu, (2.5.2) 
where V̄k h is the estimated variance of value function V k 
h and Ek h is a correction term to 
calibrate the estimated variance, and α ą 0 is a positive constant. To compute V̄k hpskh, a 
k hq, 
consider the following fact: 
rVV k h`1sps, aq “ rPrV k 
h`1s 2 sps, aq ´ rPV k 
h`1sps, aq 2 
“ xθ˚,ψrV k h`1s2ps, aqy ´ xθ˚,ψV k 
h`1 ps, aqy 
2, 
it suffices to estimate xθ˚,ψrV k h`1s2ps, aqy and xθ˚,ψV k 
h`1 ps, aqy separately. For the first term, 
θ˚ can be regarded as the unknown parameter of a regression problem between contexts 
24
ψ rV k1 
h`1s2 psk 
1 
h , a k1 
h q and targets ψ rV k1 
h`1s2 psk 
1 
h , a k1 
h q. Therefore, the first term can be estimated by @ 
ψrV k h`1s2ps, aq, θ̃k 
D 
, where 
θ̃k Ð argmin θ 
λ}θ} 2 2 ` 
k´1 ÿ 
k1“1 
H ÿ 
h“1 
´ 
@ 
θ,ψ rV k1 
h`1s2 psk 
1 
h , a k1 
h q D 
´ rV k1 
h`1ps k1 
h`1qs 2 ¯2 
. 
In addition, the second term xθ˚,ψV k h`1 
ps, aqy can be approximated by xψV k h`1 
ps, aq, θ̂ky. 
Therefore, the final estimator rV̄V k h`1sps, aq is defined as 
V̄k hps, aq “ 
” 
@ 
ψrV k h`1s2ps, aq, θ̃k 
D 
ı 
p0,H2q ´ 
” 
@ 
ψV k h`1 
ps, aq, θ̂k D 
ı2 
p0,Hq . (2.5.3) 
For the correction terms Ek h, we define it as follows: 
Ek hps, aq “ min 
! 
H2, β̃ › 
›ψrV k h`1s2ps, aq 
› 
› 
Σ̃´1 1,k 
) 
` min ! 
H2, 2Hβ̌ › 
›ψV k h`1 
ps, aq 
› 
› 
› 
Σ̂´1 1,k 
) 
, 
where Σ̃1,k is the covariance matrix of the features ψ rV k1 
h`1s2 psk 
1 
h , a k1 
h q, β̃, β̌ are two confidence 
radius. It can be shown that, with these definitions, V̄k hps, aq ` Ek 
hps, aq is an upper bound 
of rσk hs2. 
Finally, to enable online update, UCRL-RFE+ updates its covariance matrices recursively 
as follows, along with sequences b̂k h, b̃ 
k h: 
Σ̂h`1,k Ð Σ̂h,k `ψV k h`1 
pskh, a k hqψV k 
h`1 pskh, a 
k hq 
J {νk 
h 
Σ̃h`1,k Ð Σ̃h,k `ψrV k h`1s2pskh, a 
k hqψrV k 
h`1s2pskh, a k hq 
J 
b̂h`1,k Ð b̂h,k `ψV k h`1 
pskh, a k hqV k 
h`1ps k h`1q{νk 
h 
b̃h`1,k Ð b̃h,k `ψrV k h`1s2pskh, a 
k hqrV k 
h`1pskh`1qs 2, (2.5.4) 
where uk h is the pseudo value function in (2.4.3) and νk 
h is defined in (2.5.2). Then UCRL-
RFE+ computes θ̂k, θ̃k as in Line 14 to Line 15 of Algorithm 3. 
2.5.2 Sample Complexity Analysis 
Now we present the sample complexity for Algorithm 3. 
25
Theorem 2.5.1 (Sample complexity of UCRL-RFE+). For Algorithm 3, setting λ “ B´2, 
α “ H2{d in (2.5.2), and the confidence radius as 
β̂ “ 8 a 
d logp1 ` KHB2q logp48K2H2{δq ` 4 ? d logp48K2H2 
{δq ` 1 
β̌ “ 8d a 
logp1 ` KHB2q logp48K2H2{δq ` 4 ? d logp48K2H2 
{δq ` 1 
β̃ “ 8H2 a 
d logp1 ` KHB2q logp48K2H2{δq ` 4H2 logp48K2H2 {δq ` 1 
β “ H a 
d logp12p1 ` KH3B2q{δq ` 1, 
then for any 0 ă ϵ ă 1, if K “ ÕpH4dpH ` dqϵ´2q, then with probability at least 1 ´ δ, for 
any reward function r, Algorithm 2 outputs a policy π with Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď ϵ. 
Remark 2.5.2. Theorem 2.5.1 suggests that when d ě H, the sample complexity of UCRL-
RFE+ is ÕpH4d2ϵ´2q, which improves the sample complexity of UCRL-RFE by a factor of 
H. On the other hand, when H ě d, the sample complexity of UCRL-RFE+ reduces to 
ÕpH5dϵ´2q, which is better than that of UCRL-RFE by a factor of d. At a high level, the 
sample complexity improvement is attributed to the Bernstein-type bonus. 
Corollary 2.5.3. Under the same conditions as in Theorem 2.5.1, if solving the relaxed 
optimization problem in (2.4.5), Algorithm 3 has K “ ÕpH5d3ϵ´2q sample complexity. 
2.6 Optimal Horizon-Free Reward-Free Exploration Algorithms 
In Section 2.4 and 2.5, we have discussed the reward-free exploration when the reward 
function is bounded by rhps, aq P r0, 1s. Therefore, the total reward collected over H steps 
is bounded by řH 
h“1 rhps, aq ď H and the sample complexity presented in Theorem 2.4.3 
and Theorem 2.5.1 have a high dependence on H. In this section, we extend the reward-free 
exploration algorithms to the bounded total reward setting and aim to remove the dependence 
of H in this situation. Therefore, we assume that the accumulated reward of an episode for 
any trajectory is upper bounded by 1, which ensures that the only factors affecting the final 
26
statistical complexity are difficulties brought by exploration and long planning horizon rather 
than the scale of the total reward. 
Assumption 2.6.1. (Bounded total reward) For any trajectory tsh, ahuHh“1, we have 0 ď 
řH h“1 rhpsh, ahq ď 1. We denote the set of reward functions that satisfy this by R. 
Following Zhou and Gu (2022b), we propose an exploration algorithm called HF-UCRL-
RFE++ using high-order estimation to get the horizon-free sample complexity in the regime 
of reward-free exploration. 
2.6.1 Proposed Algorithms 
In this section, we propose our reward-free exploration algorithm HF-UCRL-RFE++. This 
algorithm consists of two phases. In the exploration phase, it builds an estimator θ for the 
linear mixture MDP transition kernel parameter θ˚ based on the sampled episodes. At a 
high level, the estimation follows the value-targeted regression (VTR) framework proposed 
by Jia et al. (2020). The VTR is basically a ridge regression with value functions as responses 
and feature mappings as predictors. However, value functions do not have estimates since 
the reward function is not accessible. Therefore, the value functions and reward functions 
are replaced by well-designed exploration-driven pseudo-value functions and pseudo-reward 
functions. To achieve a better estimation, we further apply the high-order moment estimation 
(HOME) technique proposed by Zhou and Gu (2022a). Then, during the planning phase, 
the algorithm uses the estimator θ acquired in the exploration phase to find the optimal 
policy π for the given reward functions. Our algorithm is described in Algorithm 4. 
2.6.1.1 Exploration-driven Pseudo Value Function 
As mentioned above, in the paradigm of reward-free exploration, we have to construct the 
pseudo-reward function to guide the agent in taking actions in the absence of the real reward 
function. As we adopt in this work, the most natural idea is to construct the pseudo-reward 
27
Algorithm 4 HF-UCRL-RFE++ (High-order Estimation) Input: Confidence radius tβku, regularization λ, number of the high-order estimator M . 
1: Phase I: Exploration Phase 
2: Initialize Σ̂1,1,m “ Σ̃1,1,m “ λI, b̃1,1,m “ b̂1,1,m “ 0 for all m P rM s, U1 “ ␣ 
θ|θ P Rd ( 
. 
3: Set θ̂1,m Ð Σ̂´1 1,1,mb̂1,1,m, θ̃1,m Ð Σ̃´1 
1,1,mb̃1,1,m for all m P rM s. 
4: for k “ 1, 2, ¨ ¨ ¨ , K do 
5: Set πk,θk, rk “ argmaxπ,θPUk,rPR V̂k,1ps1;θ, π, rq, V̂k,1 is defined in (2.6.2). 
6: Denote ␣ 
Ṽk,hp¨q (H 
h“1 “ tVhp¨;θk, πk, rkqu 
H h“1. Receive initial state sk1 “ s1. 
7: for h “ 1, 2, ¨ ¨ ¨ , H do 
8: Execute akh “ πk h 
` 
skh ˘ 
, receive skh`1 „ P ` 
¨|skh, a k h 
˘ 
. 
9: For m P rM s, denote ϕ̂k,h,m “ ϕV̂ 2m k,h`1 
pskh, a k hq, ϕ̃k,h,m “ ϕṼ 2m 
k,h`1 pskh, a 
k hq. 
10: Set ␣ 
σ̂k,h,m 
( 
Ð HOMEAlg. 5 
´ 
␣ 
ϕ̂k,h,m, θ̂k,m, Σ̂k,h,m, 9̂ Σk,m 
( 
, βk, α, γ ¯ 
. 
11: Set ␣ 
σ̃k,h,m 
( 
Ð HOMEAlg. 5 
´ 
␣ 
ϕ̃k,h,m, θ̃k,m, Σ̃k,h,m, 9̃ Σk,m 
( 
, βk, α, γ ¯ 
. 
12: Set Σ̃k,h`1,m Ð Σ̃k,h,m ` ϕ̃k,h,mϕ̃ J k,h,mσ̃ 
´2 k,h,m for m P rM s. 
13: Set Σ̂k,h`1,m Ð Σ̂k,h,m ` ϕ̂k,h,mϕ̂ J k,h,mσ̂ 
´2 k,h,m for m P rM s. 
14: Set b̃k,h`1,m Ð b̃k,h,m ` ϕ̃k,h,mṼ 2m 
k,h`1pskh`1qσ̃ ´2 k,h,m for m P rM s. 
15: Set b̂k,h`1,m Ð b̂k,h,m ` ϕ̂k,h,mV̂ 2m 
k,h`1pskh`1qσ̂ ´2 k,h,m for m P rM s. 
16: end for 
17: 9̃ Σk`1,m Ð Σ̃k,H`1,m, 9̂ 
Σk`1,m Ð Σ̂k,H`1,m. 
18: Set Σ̃k`1,1,m Ð Σ̃k,H`1,m, b̃k`1,1,m Ð b̃k,H`1,m, θ̃k`1,m “ Σ̃´1 k`1,1,mb̃k`1,1,m. 
19: Set Σ̂k`1,1,m Ð Σ̂k,H`1,m, b̂k`1,1,m Ð b̂k,H`1,m, θ̂k`1,m “ Σ̂´1 k`1,1,mb̂k`1,1,m. 
20: Update the confidence set Uk to Uk`1 by adding constraints (2.6.5), (2.6.6). 
21: end for 
22: Phase II: Planning Phase 
23: Receive reward function r and return policy π̂r “ argmaxπ V1p¨;θK , π, rq. 
function related to uncertainty, which urges the agent to collect information about the most 
uncertain states and actions. Two approaches follow this idea: one is constructing the pseudo 
28
reward function directly measuring and maximizing the uncertainty of each stage, and the 
other is constructing the pseudo reward function maximizing the overall uncertainty along 
trajectories. Zhang et al. (2021e) took the first approach, constructing the pseudo-reward 
function in the form of 
rkhps, aq “ min ! 
1, 2β 
H 
c 
max V PSÑr0,H´hs 
}ϕV ps, aq}Σ´1 1,k 
) 
, 
and the pseudo-value function to be the argument of the maxima for the above uncertainty 
measure. Under this construction, the suboptimality in the planning phase can be bounded 
by the accumulation of uncertainty. This approach is straightforward but has the following 
two drawbacks. Firstly, without the truncation for accumulation of uncertainty, the upper 
bound of overall suboptimality in the planning phase will be in the scale of OpHq, which 
is meaningless since the value function lies in the interval of r0, 1s under our assumption. 
Second, since VTR utilizes value functions’ variance information for θ estimation, it requires 
a Bellman-equation-type equality between two consecutive stages h and h ` 1. However, 
the first approach does not satisfy this requirement, preventing us from acquiring a more 
accurate estimate. 
To address the above issues, we follow the design of pseudo value function proposed in 
Chen et al. (2021). In particular, we are constructing the pseudo-reward function aiming to 
maximize the overall uncertainty along trajectories. We view the uncertainty of states and 
actions as a function of (pseudo) reward function r, policy π, and transition kernel parameter 
θ defined as follows 
uk,hps, a;θ, π, rq “min ! 
1, β › 
›ϕVhp¨;θ,π,rqps, aq › 
› 
9̃ Σ 
´1 
k,0 
) 
, (2.6.1) 
where Vhp¨;θ, π, rq is the the value function of policy π for linear mixture MDP with tran-
sition kernel parameter θ and the reward function r, and the overall uncertainty along the 
trajectory is the truncated sum of each step uncertainty defined as 
V̄k,hps;θ, π, rq “ min ! 
1,uk,hps, πpsq;θ, π, rq ` ϕJ 
V̄k,h`1p¨;θ,π,rq ps, πpsqqθ˚ 
) 
. 
29
However, the definition of V̄k,hps;θ, π, rq involves θ˚ , which is unknown to the agent. Hence, 
we construct the optimistic estimation of V̄k,hps;θ, π, rq as V̂k,hps;θ, π, rq defined as 
V̂k,hps;θ, π, rq “ min ! 
1,uk,hps, πpsq;θ, π, rq ` 2β › 
›ϕV̂k,h`1p¨;θ,π,rq ps, πpsq 
˘ › 
› 
9̂ Σ 
´1 
k,0 
` ϕJ 
V̂k,h`1p¨;θ,π,rq ps, πpsqqθ 
) 
. (2.6.2) 
Notable, the definitions of uk,h and V̂k,h involve the covariance matrices 9̃ Σk,0 and 9̂ 
Σk,0, which 
are computed at the end of the preceding episode at Line 17 of Algorithm 4. In the following 
content, when there is no confusion, we may write V̂k,hp¨q “ V̂k,hp¨;θk, πk, rkq, uk,hp¨, ¨q “ 
uk,hp¨, ¨;θk, πk, rkq. In order to collect more information, the agent is expected to transit 
through the trajectory with the largest uncertainty V̂k,h. It is notable that V̂k,h is a function 
of (pseudo) reward function rk, policy πk, and transition kernel parameter θk. Thus, at 
the beginning of each episode, we set rk, πk, and θk to be arguments of the maxima, as 
presented in Line 5 in Algorithm 4. Through this process, we acquire the pseudo value 
function rk, which is essential for reward-free exploration. Afterward, the algorithm collects 
samples along trajectories induced by policy πk and improves the estimation of θk in Line 6 
to Line 21. In this stage, Algorithm 4 encounters two series of functions in the form of 
Bellman equations; one is the sum of pseudo rewards r, Ṽk,hp¨q “ Vhp¨;θk, πk, rkq, which we 
refer as pseudo value function, and one is the uncertainty along the trajectory, V̂k,h. These 
two series of functions are both eligible for refined VTR and thus help estimate θ, as we will 
explain in the following. 
30
Algorithm 5 High-order moment estimator (HOME) Input: Features tϕk,h,mumPrMs 
, vector estimators tθk,mumPrMs , covariance matrix 
! 
Σk,h,m, 9Σk,m 
) 
mPrMs , confidence radius βk, α, γ. 
1: for m “ 0, . . . ,M ´ 2 do 
2: Set “ 
Vk,mV 2m 
k,h`1 
‰ 
pskh, a k hq Ð 
“ 
ϕJ k,h,m`1θk,m`1 
‰ 
r0,1s ´ “ 
ϕJ k,h,mθk,m 
‰2 
r0,1s . 
3: Set Ek,h,m Ð 
” 
2βk }ϕk,h,m} 9Σ´1 k,m 
ı 
r0,1s ` 
” 
βk }ϕk,h,m`1} 9Σ´1 k,m`1 
ı 
r0,1s . 
4: Set σ2 k,h,m Ð max 
! 
γ2 }ϕk,h,m}Σ´1 k,h,m 
, “ 
Vk,mV 2m 
k,h`1 
‰ 
pskh, a k hq ` Ek,h,m, α 
2 ) 
. 
5: end for 
6: Set σ2 k,h,M´1 Ð max 
! 
γ2 }ϕk,h,M´1}Σ´1 k,h,M´1 
, 1, α2 ) 
. 
Output: tσk,h,mumPrMs . 
2.6.1.2 High-order Moment Estimation 
The key technique used in our algorithm consists of two series of high-order estimations 
for the transition kernel parameter θ. The algorithm for high-order moment estimation is 
stated in Algorithm 5. In the exploration phase, the agent learns the environment with 
the help of two series of value functions Ṽk,h and V̂k,h. They serve to characterize different 
aspects of the model, one for pseudo values and one for trajectory uncertainty. And thus, 
they rely on different estimations of transition kernel parameter θ. Two independent series 
of higher-order moment estimations are necessary for achieving accurate estimation. In the 
Algorithm 4, both estimations of θ are the solutions to the weighted regression problem in 
the following form: 
argmin θ 
ˆ 
λ}θ} 2 2 ` 
k´1 ÿ 
j“1 
H ÿ 
h“1 
` 
ϕJ j,h,0θ ´ Vj,hpsjh`1q 
˘2 {σ̄2 
j,h,0 
˙ 
, (2.6.3) 
where the regression weight σ̄j,h,0 is set as Equation (2.6.4). 
σ2 k,h,0 Ðmax 
! 
γ2 }ϕk,h,0}Σ´1 
k,h,0 , “ 
Vk,0Vk,h`1 
‰ 
pskh, a k hq ` Ek,h,0, α 
2 ) 
. (2.6.4) 
31
σ̄j,h,0 can be considered as an combination of aleatoric uncertainty and epistemic uncer-
tainty (Kendall and Gal, 2017; Mai et al., 2022). The first term γ2 }ϕk,h,m}Σ´1 k,h,0 
in (2.6.4) is 
the epistemic uncertainty caused by limited available data. And the second term in Equa-
tion (2.6.4) is supposed to be the aleatoric uncertainty Vk,0Vk,h`1 characterizing the inherent 
non-determinism of the transition kernel, which is irreducible. Here the Vk,mVk,h`1 is the vari-
ance of Vk,h`1 to 2m defined as rPV 2m`1 
k,h`1spskh, a k hq´rPV 2m 
k,h`1sps k h, a 
k hq2. Then, 
“ 
Vk,0Vk,h`1 
‰ 
pskh, a k hq 
is further replaced with its estimate “ 
Vk,0Vk,h`1 
‰ 
pskh, a k hq plus its error bound Ek,h,0 since 
real variance “ 
Vk,0Vk,h`1 
‰ 
pskh, a k hq is unknown to the agent. Because 
“ 
Vk,0Vk,h`1 
‰ 
pskh, a k hq is a 
quadratic function of the real transition kernel parameter θ˚, its estimate can be achieved 
as “ 
Vk,0Vk,h`1 
‰ ` 
skh, a k h 
˘ 
“ 
”A 
ϕk,h,1,θk,1 
Eı 
r0,1s ´ 
”A 
ϕ̂k,h,0,θk,0 
Eı2 
r0,1s , 
where θk,1 is again the solution to the weighted regression problem similar to (2.6.4) with 
predictors ϕk,h,1 “ ϕV 2 k,h`1 
pskh, a k hq, responses V 2 
k,h`1ps k h`1q and weight σk,h,1. Following the 
above idea, the value of weight σk,h,1 further relies on θk,2, which is the solution to a weighted 
regression problem involving another weight σk,h,2. The algorithm carried out this process 
recursively until σk,h,M´1, where its second term is replaced by the trivial upper bound of 
aleatoric uncertainty. 
Applying HOME to the reward-free setting brings additional difficulties in controlling 
the error of our estimate for the model, as the error introduced by using the pseudo reward 
function instead of the real reward function and the error introduced by estimating the 
true transition kernel must be controlled separately. To address this problem, we carefully 
estimate variables indicating different kinds of error into two series of HOME in Line 10 and 
Line 11. Since the separation of variables deeply exploits the inner structure of the problem, 
the two series of HOME can be merged in the end to achieve a unified control for both kinds 
of error. 
Previous work Chen et al. (2021) implemented the weighted value regression in a more 
crude way. The weights are constructed only on aleatoric uncertainty, totally ignoring epis-
32
temic uncertainty. In addition, they use the same instead of different transition kernel 
parameters to calculate different order moments of the value function and stop target value 
regression at second order moment, which increased avoidable error. As a result, Chen et al. 
(2021) can only replace factor Hd with factor H `d when trying to improve the dependency 
on d in the upper bound. In contrast, our work further improves factor H ` d to factor H 
through the well-designed target value regression, as we can see in Corollary 2.6.6. 
2.6.1.3 High Confidence Set 
At the end of each episode, we add the following constraints into Uk to update the high 
confidence set in Line 20 of Algorithm 4. 
› 
› 
› θ ´ θ̂k,m 
› 
› 
› 9̂ Σk,m 
ď βk, m P rM s, (2.6.5) › 
› 
› θ ´ θ̃k,m 
› 
› 
› 9̃ Σk,m 
ď βk, m P rM s. (2.6.6) 
High confidence set Uk ensures that the estimate θk lies in a neighborhood of real transition 
kernel parameter θ˚. Here the algorithm adds 2M inequalities to constraints in each episode. 
These inequalities guarantee that estimations of the variance of V̂k,h and Ṽk,h up to M -th 
order are near the real values. 
2.6.1.4 Planning Phase 
After finishing the exploration, the agent enters the planning phase and receives the real 
reward function. Depending on optimal Bellman equations, the agent is able to obtain the 
optimal policy backward from state H to state 1 by dynamic programming based on real 
reward function r and transition kernel parameter estimate θK . And then, the algorithm 
outputs the optimal policy. 
Remark 2.6.2 (Computational Complexity of HF-UCRL-RFE++). Similar with Chen 
et al. (2021), we assume that the optimization over θ, π, and r in Line 5 of Algorithm 4 
33
can be accomplished with an oracle which is obvious to be called for K times. At each 
episode k and each stage h, HF-UCRL-RFE++ computes tϕ̂k,h,mumPrMs , tϕ̃k,h,mumPrMs 
, ␣ 
σ̂k,h,m 
( 
mPrMs , ␣ 
σ̃k,h,m 
( 
mPrMs , and updates tΣ̂k,h,mumPrMs 
, tΣ̃k,h,mumPrMs . The computation 
of tϕ̂k,h,mumPrMs and tϕ̃k,h,mumPrMs 
require OpOMq times. According to Algorithm 5, calcu-
lating ␣ 
σ̂k,h,m 
( 
mPrMs and 
␣ 
σ̃k,h,m 
( 
mPrMs require OpMd2q time since the computation of the 
inner-product an inversion of matrix and a vector needs Opd2q. The updates of tΣ̂k,h,mumPrMs 
and tΣ̃k,h,mumPrMs further require OpMd2q time. Lastly, determining the optimal policy dur-
ing the planning phase takes OpHpSAd ` Oqq time. Therefore, the total time complexity of 
HF-UCRL-RFE++ is OpKHpOM ` Md2q ` HSAdq. 
2.6.2 Sample Complexity Analysis 
We provide the theoretical analysis for HF-UCRL-RFE++ in this section. In order to show 
the optimality of HF-UCRL-RFE++, we also provide lower bound of sample complexity for 
all reward-free exploration algorithms. 
2.6.2.1 Upper Bound of the Sample Complexity 
We first provide the suboptimality upper bound of our algorithm HF-UCRL-RFE++. 
Theorem 2.6.3. For Algorithm 4, set M “ logp7KHq{ logp2q, α “ H´1{2, γ “ d´1{4, 
λ “ d{B2, tβkukě1 as βk “ 12 ? dητ ` 30τ{γ2 ` 
? λB, and denote β “ βK , where η “ 
logp1 ` kH{pα2dλqq and τ “ logp32plogpγ2{αq ` 1qk2H2{δq. Then, for any 0 ă δ ă 1, we 
have with probability at least 1 ´ δ, after collecting K episodes of samples, algorithm 4 
returns a policy π̂r satisfying the following sub-optimality bound, 
V ˚ 1 ps1; rq ´ V1ps1;θ 
˚, π̂r, rq “ Õ 
ˆ 
d2 
K ` 
d ? K 
˙ 
. 
The next corollary specifies the sample complexity of our algorithm. 
Corollary 2.6.4. Under the same conditions as in Theorem 2.6.3, Algorithm 4 has sample 
34
complexity of 
mpε, δ1 q “ 
16 
ε2 
´ 
64max ! 
8β ? dι, 
a 
2ζ ) 
` 120β ? dιHα2 
¯2 
` 8 
ε 
´ 
2752max ␣ 
64β2dι, 2ζ ( 
` 24ζ ` 240dι ` 240βγ2dι ` 120βdι ? M ¯ 
(2.6.7) 
Moreover, setting α “ H´1{2, γ “ d´1{4, and λ “ d{B2, we have the reward-free sample 
complexity bound mpε, δ1q “ Õpd2ε´2q. 
Proof of Corollary 2.6.4. (2.6.7) is derived directly from Theorem 2.6.3 by setting the sub-
optimality to ε and solving the K. 
Remark 2.6.5. To the best of our knowledge, Corollary 2.6.4 provides the first horizon-free 
sample complexity upper bound independent of state space size S and action space size A 
for reward-free exploration. This result shows that long-horizon planning does not add extra 
difficulty to reward-free exploration. 
Corollary 2.6.6. When re-scaling the assumption řH 
h“1 rhpsh, ahq ď 1 to řH 
h“1 rhpsh, ahq ď 
H, under the same conditions as Theorem 2.6.3, Algorithm 4 has sample complexity of 
mpε, δ1 q “ 
16H2 
ε2 
´ 
64max ! 
8β ? dι, 
a 
2ζ ) 
` 120β ? dιHα2 
¯2 
` 8H 
ε 
´ 
2752max ␣ 
64β2dι, 2ζ ( 
` 24ζ ` 240dι ` 240βγ2dι ` 120βdι ? M ¯ 
(2.6.8) 
Moreover, setting α “ H´1{2, γ “ d´1{4, and λ “ d{B2, we have the reward-free sample 
complexity bound mpε, δ1q “ ÕpH2d2ε´2q. 
Proof of Corollary 2.6.6. (2.6.8) is a direct result of Corollary 2.6.4 by setting r1 hpsh, ahq “ 
rhpsh, ahq{H. 
Remark 2.6.7. The assumption řH 
h“1 rhpsh, ahq ď H covers the standard reward assump-
tion rhpsh, ahq P r0, 1s. Therefore, compared with Chen et al. (2021), our analysis does 
35
not require the d ą H assumption and achieves the same sample complexity bound up to 
logarithmic factors except for the trivial ÕpHq difference between time-homogeneous and 
time-inhomogeneous models with a milder assumption. This improvement can be attributed 
to the refined value target regression technique, high-order moment estimation (HOME), 
adopted in our approach. We provide a detailed analysis of this improvement in the “High-
order Moment Estimation” part in the Section 2.6.1. 
2.6.2.2 Lower Bound of the Sample Complexity 
The following results provide lower bounds of the sample complexity and suggest that our 
algorithm is minimax optimal. We will consider the hard-to-learn linear mixture MDPs 
constructed in Zhou and Gu (2022a). The state space is S “ tx1, x2, x3u and the action 
space is A “ tau “ t´1, 1ud´1. The reward function satisfies rpx1, ¨q “ rpx2, ¨q “ 0, and 
rpx3, ¨q “ 1 H 
. The transition probability is defined to be Ppx2 | x1,aq “ 1 ´ pδ ` xµ,ayq and 
Ppx3 | x1,aq “ δ ` xµ,ay, where δ “ 1{6 and µ P t´∆,∆ud´1 with ∆ “ a 
δ{K{p4 ? 2q. 
Theorem 2.6.8. Suppose B ą 1. Then for any algorithm ALGFree solving reward-free lin-
ear mixture MDP problems satisfying assumption 2.6.1, there exist a linear mixture MDP 
M such that ALGFree needs to collect at least Ω pd2ε´2q episodes of samples to output an 
ε-optimal policy with probability at least 1´ δ. This lower bound matches the sample com-
x1 
¨ ¨ ¨ ¨ ¨ ¨ 
x2 x3 
1 ´ pδ ` xµ,ayq δ ` xµ,ay 
1 1 
Figure 2.2: The transition kernel of the hard-to-learn linear mixture MDPs. 
36
plexity upper bound provided in Corollary 2.6.4, which shows our upper bound is optimal. 
Remark 2.6.9. The lower bound is similar to the lower bound provided in Chen et al. 
(2021). The first difference is that we rescale the non-zero reward in hard-to-learn cases 
from 1 to 1 H 
in order to satisfy Assumption 2.6.1. The second difference is that we consider 
the time-homogeneous model instead of the time-inhomogeneous one in theirs. By these 
changes, our lower bound for reward-free exploration provided in Theorem 2.6.8 removes the 
unnecessary polynomial dependency on episode length H introduced by the scale of total 
reward. 
Corollary 2.6.10. Under the same conditions as Theorem 2.6.8 and replacing the bounded 
total reward řH 
h“1 rhpsh, ahq ď 1 with rh P r0, 1s, for any algorithm ALGFree solving reward-
free linear mixture MDP problems satisfying assumption 2.6.1, there exist a linear mixture 
MDP M such that ALGFree needs to collect at least Ω̃ pH2d2ε´2q episodes to output an ε-
optimal policy with probability at least 1´δ, which suggests that the upper bound presented 
in Theorem 2.6.3 is optimal. 
Proof of Corollary 2.6.10. The result presented in Corollary 2.6.10 is directly obtained by 
letting rpx3, ¨q “ 1 in the hard case presented in Figure 2.2. 
2.7 Conclusion 
We study model-based reward-free exploration for learning the linear mixture MDPs. We 
propose an algorithm which is guaranteed to efficiently explore the environment with the 
help of the pseudo reward function. In order to improve the sample complexity of this 
exploration, we leverage the variance information in reinforcement learning and improve the 
algorithm using a Bernstein-type concentration inequality. 
We also extend the aforementioned algorithm into a bounded total reward setting. In this 
setting, our algorithm is guaranteed to have horizon-free sample complexity in the exploration 
37
phase to find a near-optimal policy in the planning phase for any given reward function. By 
providing sample complexity lower bound for reward-free exploration in linear mixture MDPs 
under our assumptions. We show that the sample complexity of our algorithm matches the 
lower bound up to logarithmic factors, indicating that our algorithm is optimal. 
2.8 Proofs 
In this section we present the detailed proof of Theorem 2.4.3, Theorem 2.5.1, Theorem 2.6.3 
and Theorem 2.6.8 and corollaries we claimed in this chapter. 
2.8.1 Proof of Theorem 2.4.3 
We will first introduce a lemma to show that for the planning module Algorithm 1, if it 
is guaranteed that the estimation θ is close to the true parameter θ˚, then the estimated 
value function is optimistic. Also the gap between the optimal value function and the value 
function of the output policy tπhuHh“1 could be controlled by the summation of UCB bonus 
term. 
Lemma 2.8.1. Let θ,Σ, β be as defined in Algorithm 1. Suppose there exists some event 
ξ such that }θ˚ ´ θ}Σ ď β on this event. Then on this event, for all s P S, V1psq ě V ˚ 1 ps; rq, 
where V1 is the output value function for Algorithm 1. We also have that 
V1psq ´ V π 1 psq ď E 
„ H ÿ 
h“1 
mintH, 2β}ψVh`1 psh, πhpshqq}Σ´1u 
ˇ 
ˇ 
ˇ s, π 
ȷ 
, 
where the policy π “ tπhuHh“1 is generated by the planning module Algorithm 1 and Vh is 
the value function calculated on Line 5 in Algorithm 1. 
Next we will give the lemmas on how to guarantee the condition of Lemma 2.8.1 and 
how to utilize the result of that lemma to control the final policy error V ˚ 1 ps1; rq ´ V π 
1 ps1; rq 
where the policy π is output of the planning phase. We start with Algorithm 2, which uses 
the Hoeffding bonus. 
38
Firstly, the next lemma shows how to guarantee the condition in Lemma 2.8.1. 
Lemma 2.8.2 (Confidence interval, Hoeffding). For Algorithm 2, let λ, β be as defined in 
Theorem 2.4.3, then with probability at least 1´ δ{3, }θ˚ ´ θk}Σ1,k ď β for any k P rK ` 1s. 
Secondly, based on the lemma above, we find that the policy error during the planning 
phase is controlled by a summation of the UCB terms. Since from the intuition, the explo-
ration driven reward function (2.4.2) is the UCB term divided by H, the policy error during 
the planning phase can be converted to the value function V k 1 in the exploration phase. The 
next lemma shows that the summation of V k 1 over K iterations is sub-linear to K, thus the 
policy error during the planning phase should be small. 
Lemma 2.8.3 (Summation, Hoeffding). Set the parameters of Algorithm 2 as that of The-
orem 2.4.3. If the condition in Lemma 2.8.2 holds, then with probability at least 1 ´ δ{3, 
the summation of the value function V k 1 psk1q during the exploration phase is controlled by 
K ÿ 
k“1 
V k 1 psk1q ď 8β 
a 
HKd logp1 ` KH3B2{dq ` 8βHd logp1 ` KH3B2 q ` 2H 
a 
2HK logp1{δq. 
Equipped with these lemmas, we are about to prove Theorem 2.4.3. 
Proof of Theorem 2.4.3. In the following proof, we condition on the events in Lemma 2.8.2 
and Lemma 2.8.3 which holds with probability at least 1´ 2δ{3 by taking the union bound. 
Applying Lemma 2.8.1 to the final planning phase, we have 
V ˚ 1 ps; rq ´ V π 
1 ps; rq ď V1ps; rq ´ V π 1 ps; rq ď E 
„ H ÿ 
h“1 
mintH, 2β}ψVh`1 psh, πhpshqq}Σ´1 
1,K`1 u 
ȷ 
loooooooooooooooooooooooooooomoooooooooooooooooooooooooooon 
I1 
, 
(2.8.1) 
where the expectation is taken condition on initial state s and policy π generated by the 
planning phase. Since Σ1,k ĺ Σ1,K`1 for all k P rKs, we can guarantee that 
}ψVh`1 psh, πhpshqq}Σ´1 
1,K`1 ď }ψVh`1 
psh, πhpshqq}Σ´1 1,k . 
39
Recall the exploration driven reward function is defined by 
rkhps, aq “ min 
" 
1, 2β 
H 
c 
max fPS ÞÑr0,H´hs 
}ψf ps, aq}Σ´1 1,k 
* 
, (2.8.3) (2.8.2) 
one can easily verify that mintH, 2β}ψVh`1 psh, πhpshqq}Σ´1 
1,k u ď Hrkhpsh, πhpshqq. Therefore 
for any k P rKs episode, we can bound the term I1 using the value function V π 1 ps; trkhuHh“1q 
of the output policy π in the planning phase given the trkhuHh“1 as the reward function, i.e. 
I1 ď E „ H ÿ 
h“1 
Hrkhpsh, πhpshqq 
ȷ 
“ HV π 1 ps; trkhu 
k h“1q. (2.8.3) 
Plugging the bound of I1 back into (2.8.1) then taking the expectation over the initial 
state distribution µ, we have for any k P rKs, 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď HEs„µrV π 1 ps; trkhu 
k h“1qs 
“ H ´ 
Es„µrV π 1 ps; trkhu 
k h“1qs ´ V π 
1 psk1; trkhu k h“1q 
¯ 
` HV π 1 psk1; trkhu 
k h“1q. 
Hence 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H 
K 
K ÿ 
k“1 
´ 
Es„µrV π 1 ps; trkhu 
k h“1qs ´ V π 
1 psk1; trkhu k h“1q 
` V π 1 psk1; trkhu 
k h“1q 
¯ 
. (2.8.4) 
Since V π 1 ps; trkhukh“1q ď H for all k P rKs, s P S, by Azuma-Hoeffding’s inequality, with 
probability at least 1 ´ δ{3, 
K ÿ 
k“1 
´ 
Es„µrV π 1 ps; trkhu 
k h“1qs ´ V π 
1 psk1; trkhu k h“1q 
¯ 
ď H a 
2K logp3{δq. (2.8.5) 
By plugging (2.8.5) into (2.8.4), we have 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H 
K 
K ÿ 
k“1 
V π 1 psk1; trkhu 
k h“1q ` H2 
a 
2 logp3{δq{K. 
40
Applying Lemma 2.8.1 to the exploration phase, for any k-th episode, V π 1 psk1; trkhukh“1q ď 
V ˚ 1 psk1; trkhukh“1q ď V k 
1 psk1q, thus replacing the value function V π 1 with the estimated value 
function V k 1 , we have 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H 
K 
K ÿ 
k“1 
V k 1 psk1q ` H2 
a 
2 logp3{δq{K. (2.8.6) 
Finally by Lemma 2.8.3 we can bound the summation over V k 1 , hence 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H2 a 
2 logp3{δq{K ` 8β a 
H3d logp1 ` KH3B2{dq{K 
` 8βdH2 logp1 ` KH3B2 q{K ` 2H2 
a 
2H logp1{δq{K 
and by taking union bound, the result holds with probability at least 1´δ. Recall the setting 
of β „ ÕpH ? dq as in Theorem 2.4.3, let K “ ÕpH5d2ϵ´2q, the policy error Es„µrV ˚ 
1 ps; rq ´ 
V π 1 ps; rqs is bounded by ϵ. 
2.8.1.1 Proof of Corollary 2.4.5 
Proof of Corollary 2.4.5. Following the proof of Theorem 2.4.3, since for all x P Rd, }x}1 ď 
}x}2 ď ? d}x}1 it follows that 
}ψVh`1 psh, πhpshqq}Σ´1 
1,K`1 “ }Σ 
´1{2 1,K`1ψVh`1 
psh, πhpshqq}2 
ď ? d}Σ 
´1{2 1,K`1ψVh`1 
psh, πhpshqq}1. (2.8.7) 
We denote ũk h as the result using the ℓ1 norm as the surrogate objective function in this 
optimization problem (2.4.5), i.e. 
ũk h :“ argmax 
fPS ÞÑr0,H´hs 
}Σ ´1{2 1,k ψf pskh, a 
k hq}1, 
41
then (2.8.7) yields 
}ψVh`1 psh, πhpshqq}Σ´1 
1,K`1 ď 
? d}Σ 
´1{2 1,K`1ψVh`1 
psh, πhpshqq}1 
ď ? d}Σ 
´1{2 1,K`1ψũk 
h psh, πhpshqq}1 
ď ? d}Σ 
´1{2 1,K`1ψũk 
h psh, πhpshqq}2 
ď ? d}Σ 
´1{2 1,K`1ψuk 
h psh, πhpshqq}2, 
where the second inequality comes from ũk h is the solution in (2.4.5), the third inequality 
comes from the fact that }x}1 ď }x}2 and the forth inequality comes from the definition that 
uk h. Then (2.8.3) is changed to be 
I1 ď H ? dV π 
1 ps, trkhu k h“1q. 
Noticing that comparing to the original result, there’s an additional ? d factor which yields 
(2.8.7) 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H 
? d 
K 
K ÿ 
k“1 
V k 1 psk1q ` H2 
a 
2d logp3{δq{K. 
Then it is easy to show that using ℓ1 as the surrogate objective function, the sample com-
plexity of Algorithm 2 turns out to be ÕpH5d3ϵ´2q 
2.8.2 Proof of Theorem 2.5.1 
We are going to analyze Algorithm 3 and provide the proof of Theorem 2.5.1. Following the 
proof of Theorem 2.4.3, we only need to revise Lemmas 2.8.2 and 2.8.3 to continue the proof 
of Theorem 2.5.1. 
Lemma 2.8.4 (Confidence interval, Bernstein). Let β, β̂, β̃, β̌ and λ be defined as Theo-
rem 2.5.1, then with probability at least 1 ´ δ{3, for all k P rK ` 1s, 
}θ˚ ´ θ̂k}Σ̂1,k 
ď β̂, }θ˚ ´ θ̂k}Σ̂1,k 
ď β̌, }θ˚ ´ θ̃k}Σ̃1,k 
ď β̃, }θ˚ ´ θK`1}Σ1,K`1 
ď β, (2.8.8) 
and |rVhV k h`1sps, aq ´ V̄k 
hps, aq| ď Ek hps, aq. 
42
Lemma 2.8.5 (Summation, Bernstein). For Algorithm 2, setting its parameters as in 
Lemma 2.8.2, with probability at least 1 ´ δ{3, the summation of the value function during 
exploration phase is controlled by 
K ÿ 
k“1 
V k 1 psk1q ď Õp 
? H3Kd ` Hd 
? Kq ` op 
? Kq. 
Proof of Theorem 2.5.1. The proof is almost the same as the proof of Theorem 2.4.3 by re-
placing Lemma 2.8.2 with Lemma 2.8.4, Lemma 2.8.3 with Lemma 2.8.5. In detail, following 
the same method, (2.8.6) works for Algorithm 3 under the condition in Lemma 2.8.4 holds. 
Therefore, by using Lemma 2.8.5 instead of Lemma 2.8.3, with probability at least 1 ´ δ, 
Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď H 
K 
K ÿ 
k“1 
V k 1 psk1q ` H2 
a 
2 logp3{δq{K 
ď Õ ´ 
p ? H4d2 ` 
? H5dq{ 
? K ¯ 
. 
Letting K “ ÕpH4dpH ` dqϵ´2q, the policy error for the planning phase could be controlled 
by Es„µrV ˚ 1 ps; rq ´ V π 
1 ps; rqs ď ϵ. 
2.8.2.1 Proof of Corollary 2.5.3 
Proof of Corollary 2.5.3. The proof is almost the same as proof of Corollary 2.4.5, by adding 
the additional dependency d into the regret bound achieved by Theorem 2.5.1, it’s easy to 
verify that the sample complexity using the ℓ1 norm as the surrogate function (2.4.5) is 
ÕpH4d2pH ` dqϵ´2q. 
2.8.3 Proof of Theorem 2.6.3 
We first define the good event such that the high-order estimator is well-bounded. 
Lemma 2.8.6. For all 0 ă δ ă 1, suppose βk is set as in Theorem 2.6.3, the following event 
43
happens with probability at least 1 ´ 2Mδ 
› 
› 
› θ̂k,m ´ θ˚ 
› 
› 
› 9̂ Σk,m 
ď βk (2.8.9) › 
› 
› θ̃k,m ´ θ˚ 
› 
› 
› 9̃ Σk,m 
ď βk (2.8.10) 
}θk ´ θ˚ } 9̂ Σk,0 
ď 2βk (2.8.11) 
}θk ´ θ˚ } 9̃ Σk,0 
ď 2βk. (2.8.12) 
We define the event that Lemma 2.8.6 holds to be E2.8.6. Then the following lemma 
controls the suboptimality gap between optimal value functions and our estimated value 
function in the planning phase with the uncertainty along trajectories. 
Lemma 2.8.7. Under event E2.8.6, for any reward function r in the planning phase, the 
suboptimality gap of the outputted policy π̂r can be bounded as 
V ˚ 1 ps1; rq ´ V1 ps1;θ 
˚, π̂r, rq ď 4V̂K,1 ps1q . (2.8.13) 
The next lemma shows that the uncertainty along trajectories decreases with respect to 
episodes. This lemma is intuitively right since the uncertainty should decrease with more 
information collected. 
Lemma 2.8.8. Under event E2.8.6, for uncertainty along trajectories, we have 
V̂K,1ps1;θK , πK , rKq ď 1 
K 
ˆ K ÿ 
k“1 
V̂k,1ps1;θk, πk, rkq 
˙ 
. 
The last lemma upper bounds the sum of the uncertainty along trajectories. 
Lemma 2.8.9. For any 0 ă δ ă 1, with probability at least 1 ´ 4Mδ, we have 
K ÿ 
k“1 
V̂k,1ps1;θk, π̂k, rkq “ Õpd ? K ` d2q. (2.8.14) 
44
Equipped with the above lemmas, we are ready to prove Theorem 2.6.3. 
Proof of Theorem 2.6.3. The following proof is conditioned on E2.8.6 X E2.8.27, which holds 
with probability at least 1 ´ 4Mδ “ 1 ´ δ1. We have 
V ˚ 1 ps1; rq ´ V1ps1;θ 
˚, π̂r, rq 
ď 4V̂K,1 ps1;θK , π̂K , rKq 
ď 4 
K 
K ÿ 
k“1 
Vk,1ps1;θk, π̂k, rkq 
ď 4 
K 
´ 
896max ␣ 
64β2dι, 2ζ ( 
` 24ζ ` 240dι ` 240βγ2dι ` 120βdι ? M ` 24 
a 
ζMdι ` Mdι ¯ 
` 4 
? K 
´ 
64max ! 
8β ? dι, 
a 
2ζ ) 
` 120β ? dιHα2 
¯ 
, 
where the first inequality holds due to Lemma 2.8.7, the second inequality holds due to 
Lemma 2.8.8, and the third equality holds due to Lemma 2.8.9. 
2.8.4 Proof of Theorem 2.6.8 
Reward-free exploration is more difficult than non-reward-free MDP by definitions since 
we can easily solve non-reward-free MDP by ignoring its reward and executing reward-free 
exploration. Thus, we will start with acquiring lower bounds under non-reward-free MDP 
settings and then obtain sample complexity lower bounds of reward-free exploration. The 
proof follows ideas of Zhou and Gu (2022a) and Chen et al. (2021). 
As noted in Section 2.6.2.2, we will consider the hard-to-learn linear mixture MDPs 
constructed in Zhou and Gu (2022a). The state space S “ tx1, x2, x3u and the action 
space A “ tau “ t´1, 1ud´1. The reward function satisfies rpx1, ¨q “ rpx2, ¨q “ 0, and 
rpx3, ¨q “ 1 H 
. The transition probability satisfies Ppx2 | x1,aq “ 1 ´ pδ ` xµ,ayq and 
Ppx3 | x1,aq “ δ` xµ,ay, where δ “ 1{6 and µ P t´∆,∆ud´1 with ∆ “ a 
δ{K 1 {p4 
? 2q. The 
45
transition kernel is formulated as 
ϕ ps1 | s,aq “ 
$ 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
& 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
’ 
% 
` 
αp1 ´ δq,´βaJ ˘J 
, s “ x1, s 1 “ x2; 
` 
αδ, βaJ ˘J 
, s “ x1, s 1 “ x3; 
` 
α,0J ˘J 
, s P tx2, x3u , s 1 “ s; 
0, otherwise. 
θ “ ` 
1{α,µJ {β ˘J 
The following lemma from Zhou and Gu (2022a) lower bounds the regret for linear 
mixture MDP. 
Lemma 2.8.10 (Theorem 5.4, Zhou and Gu (2022a)). Let B ą 1. Then for any algorithm, 
when K 1 ě max t3d2, pd ´ 1q{p192pB ´ 1qqu, there exists a B-bounded linear mixture MDP 
satisfying Assumptions 3.2 such that its expected regret ErRegretpK 1qs is lower bounded by 
Ω ` 
d ? K 1{p16 
? 3q ˘ 
. 
Given Lemma 2.8.10, we will use the regret lower bound of non-reward-free linear mixture 
MDPs to derive the sample coomplexity lower bound. 
Lemma 2.8.11. Suppose B ą 1. Then for any algorithm ALGNonFree solving non-reward-
free linear mixture MDP problems satisfying assumption 2.6.1, there exist a linear mixture 
M such that ALGNonFree needs to collect at least Cd2 
ε2 episodes to output an ε-policy with 
probability at least 1 ´ δ. Here C is an absolute constant. 
Proof of Lemma 2.8.11. For any algorithm ALGNonFree, we construct an algorithm ALG1 NonFree 
executing totally K1 “ cK episodes, where c is a constant integer larger than 1. The first 
K episodes of ALG1 NonFree are the same as ALGNonFree, and the rest episodes keep executing 
the policy at the end of episode K. By Lemma 2.8.10, we have 
K1 ÿ 
k“1 
E rV ps1;θ ˚, π˚, rq ´ V ps1;θ 
˚, πk, rqs ě c1d 
? K1 
16 ? 3 
, (2.8.15) 
46
for some constant c1. In addition, based on the construction of the hard-to-learn MDPs, 
where K 1 
“ K1, the per-episode regret is upper bounded by 
E rV ps1;θ ˚, π˚, rq ´ V ps1;θ 
˚, πk, rqs ď d 
4 ? 3K1 
. (2.8.16) 
Thus, calculating (2.8.15) - pK1 ´ Kqˆ (2.8.16), and choosingc “ max ␣ 
5{c1, 2 ( 
, we have 
K1 ÿ 
k“K`1 
E rV ps1;θ ˚, π˚, rq ´ V ps1;θ 
˚, πk, rqs ě d 
? K 
16 ? 3c 
. 
Since the policies in episode K ` 1 to episode K1 are same to πK , we have 
E rV ps1;θ ˚, π˚, rq ´ V ps1;θ 
˚, πK , rqs ě d 
16 ? 3cKc 
. 
Suppose the ALGNonFree return return a ε-optimal policy with probability 1 ´ δ. Then, 
p1 ´ δqε ` δ d 
4 ? 3cK 
ě d 
16 ? 3cKc 
. 
Setting δ ă mint1, 1{p4cqu, by solving the inequality, we have K ě Cd2 
ε2 for some constant 
C. 
Since reward-free MDP is more difficult than non-reward-free MDP, Lemma 2.8.11 di-
rectly indicates Theorem 2.6.8. 
Proof of Theorem 2.6.8. We will prove the theorem by contradiction. Assume all reward-free 
linear mixture MDPs can be solved with sample complexity of opd2 
ε2 q. Then, for any non-
reward-free MDP M, there exists an algorithm ALG1 pε, δq learning its reward-free counterpart 
M1 with sample complexity of opd2 
ε2 q. We define ALG solving M as follows: it collects K 
episodes of data and outputs the policy in the same way as ALG1 by ignoring the rewards. 
Then ALG can also pε, δq learning M with sample complexity of opd2 
ε2 q, which contradicts 
Theorem 2.8.11. 
Corollary 2.6.10 can be viewed as an direct result of Theorem 2.6.8. 
47
2.8.5 Proofs in Section 2.8.1 and Section 2.8.2 
2.8.5.1 Filtration 
For the simplicity of further proof, we define the event filtration here as 
Gh,k “ ␣ 
tsκi , a κ i u 
H,k´1 i“1,κ“1, tski , a 
k i u 
h´1 i“1 
( 
, 
it is easy to verify that skh is Gh`1,k-measurable. Also, since πk is Gh,k-measurable for all 
h P rHs, akh “ πk hpskhq is also Gh`1,k-measurable. Also, for any function f ď R built on Gh`1,k, 
such as V k h`1, u 
k h, fpskh`1q ´ rPf spskh, a 
k hq is Gh`1,k-measurable and it is also a zero-mean R-
sub-Gaussian conditioned on Gh`1,k. 
Since GH`1,k “ G1,k`1, we could arrange the filtration as 
G “ tG1,1, ¨ ¨ ¨ ,GH,1, ¨ ¨ ¨ ,G1,k, ¨ ¨ ¨ ,Gh,k, ¨ ¨ ¨GH,k, ¨ ¨ ¨ ,G1,k`1, ¨ ¨ ¨ ,GH,K ,G1,K`1u, 
and we will use G as the filtration set for all of the proofs in the following section and it is 
obvious that G1,K`1 contains all information we collect during the exploration phase. 
2.8.5.2 Proof of Lemma 2.8.1 
Proof of Lemma 2.8.1. We prove this lemma by induction on time step h. Indeed, when 
h “ H`1, VH`1psq “ V ˚ H`1ps; rq “ 0 by definition. Suppose for h P rHs, Vh`1psq ě V ˚ 
h`1ps; rq, 
then following the update rule of Q function in Algorithm 1, we have 
Qhps, aq ´ Q˚ hps, a; rq 
“ min ␣ 
H, rhps, aq ` xψVh`1 ps, aq,θy ` β}ψVh`1 
ps, aq}Σ´1 
( 
´ rhps, aq ´ rPV ˚ h`1sps, a; rq 
ě min ␣ 
H ´ Q˚ hps, a; rq, xψVh`1 
ps, aq,θy ` β}ψVh`1 ps, aq}Σ´1 ´ rPV ˚ 
h`1sps, a; rq ( 
. 
We need to show that Qhps, aq ě Q˚ hps, a; rq. Since it is obvious that the first term H ´ 
Q˚ hps, a; rq in min operator is greater than zero, we only need to verify that the second term 
48
is also positive where 
xψVh`1 ps, aq,θy ` β}ψVh`1 
ps, aq}Σ´1 ´ rPV ˚ h`1sps, a; rq 
ě xψVh`1 ps, aq,θy ` β}ψVh`1 
ps, aq}Σ´1 ´ rPVh`1sps, a; rq 
“ xψVh`1 ps, aq,θ ´ θ˚ 
y ` β}ψVh`1 ps, aq}Σ´1 
ě β}ψVh`1 ps, aq}Σ´1 ´ }ψVh`1 
ps, aq}Σ´1}θ ´ θ˚ }Σ, 
where the first inequality is from the induction assumption that V ˚ h`1ps; rq ď Vh`1psq. The 
second equality is from the expectation of value function is a linear function of ψVh`1 
shown in (2.3.2). Then the inequality on the third line is utilizing the fact that xx,yy ě 
´}x}A´1}y}A. Since it is guaranteed that β ě }θ ´ θ˚}Σ from the statement of this lemma, 
Qhps, aq ´ Q˚ hps, a; rq ě 0, which from induction we get our conclusion. 
For the second part controlling V1psq ´V π 1 psq, since aforementioned proof has shown that 
V ˚ h ps; rq ď Vhpsq for all h P rHs, we have V ˚ 
h ps; rq ´ V π h ps; rq ď Vhpsq ´ V π 
h ps; rq and 
Vhpsq ´ V π h ps; rq “ mintH, rhps, πhpsqq ` xψVh`1 
,θy ` β}ψVh`1 ps, πhpsqq}Σ´1u 
´ rhps, πhpsqq ´ rPV π h`1sps, πhpsq; rq 
ď mintH, xψVh`1 ,θy ` β}ψVh`1 
ps, πhpsqq}Σ´1 ´ rPVh`1sps, πhpsqqu 
` rPVh`1sps, πhpsqqu ´ rPV π h`1sps, πh; rq 
“ mintH, xψVh`1 ,θ ´ θ˚ 
y ` β}ψVh`1 ps, πhpsqq}Σ´1u 
` rPVh`1sps, πhpsqqu ´ rPV π h`1sps, πhpsq; rq 
ď mintH, 2β}ψVh`1 ps, πhpsqq}Σ´1u 
` rPVh`1sps, πhpsqqu ´ rPV π h`1sps, πhpsq; rq, 
where the first inequality is directly from moving term ´rhps, πhpsqq ´ rPVh`1sps, πhpsqq 
into the min operator, the second inequality uses the condition that }θ ´ θ˚}Σ ď β and 
49
xx,yy ď }x}A´1}y}A. Considering the first step h “ 1, we have 
V1ps1q ´ V π 1 ps1; rq ď mintH, 2β}ψV2ps1, π1ps1qq}Σ´1u ` Es2„Pp¨|s1,π1ps1qqrV2ps2q ´ V π 
2 ps2qs 
ď mintH, 2β}ψV2ps1, π1ps1qq}Σ´1u 
` Es2„Pp¨|s1,π1ps1qq 
” 
mintH, 2β}ψV3ps2, π2ps2qq}Σ´1u 
` Es3„Pp¨|s2,π2ps2qqrV3ps3q ´ V π 3 ps3qs 
ı 
ď ¨ ¨ ¨ 
ď E „ H ÿ 
h“1 
mintH, 2β}ψVh`1 psh, πhpshqq}Σ´1u 
ˇ 
ˇ 
ˇ 
ˇ 
s1, π 
ȷ 
, 
which concludes our proof. 
2.8.5.3 Proof of Lemma 2.8.2 
We introduce the classical confidence set lemma from (Abbasi-Yadkori et al., 2011). 
Lemma 2.8.12 (Theorem 2, Abbasi-Yadkori et al. (2011)). Let tFtu 8 t“0 be a filtration and 
tηtu is a real-valued stochastic process which is Ft-measurable and conditionally R-sub-
Gaussian. Set yt “ xxt,ψ ˚y ` ηt, Vt “ λI` 
řt i“1 xix 
J i where x P Rd. Denote the estimation 
of ψ˚ as ψt “ V´1 t 
řt i“1 yixi. If }ψ˚}2 ď S, }xt}2 ď L, then with probability at least 1 ´ δ, 
for all t ě 0 
}ψ˚ ´ψt}Vt ď R 
d 
d log 
ˆ 
1 ` tL2{λ 
δ 
˙ 
` S ? λ. 
Equipped with this lemma, we begin our proof. 
Proof of Lemma 2.8.2. Since rPuk hspskh, a 
k hq “ xψuk 
h pskh, a 
k hq,θ˚y due to (2.3.2) and uk 
hpsq ď H , 
uk hpsq´xψuk 
h pskh, a 
k hq,θ˚y is Gh,k-measurable and it is also a zero mean H-sub-Gaussian random 
variable conditioned on Gh,k. Also from Definition 2.3.1, }θ˚}2 ď B, }ψuk h pskh, a 
k hq}2 ď H. 
Therefore, recall the calculation of θk, according to Lemma 2.8.12, let t “ pk ´ 1qH we have 
}θk ´ θ˚ }Σ1,k 
ď H 
d 
d log 
ˆ 
1 ` pk ´ 1qH3{λ 
δ 
˙ 
` B ? λ. 
50
Let λ “ B´2, δ “ δ{3 and relax k with k “ K`1, we can get the β claimed in Theorem 2.4.3. 
2.8.5.4 Proof of Lemma 2.8.3 
We provide the proof to control the summation of the value function during the exploration 
phase. To start with, since rather than immediately updating the parameter after each time 
step, we can only update the estimation θ and its ‘covariance matrix’ Σ once after each 
episode. As a result, this ‘batched update rule’ make the UCB bonus term at step ph, kq be 
}ψuk h pskh, a 
k hq}U´1 
1,k instead of }ψuk 
h pskh, a 
k hq}U´1 
h,k in the vanilla linear bandit setting. Therefore, 
we need lemmas showing that these two UCB terms are close to each other. 
Lemma 2.8.13. For any txh,ku H,K h“1,k“1 Ă Rd satisfying that }xh,k}2 ď L, @ph, kq P rHsˆrKs, 
let Uh,k “ λI` řk´1 
κ“1 
řH i“1 xi,κx 
J i,κ ` 
řh´1 i“1 xi,kx 
J i,k, there exists at most 2Hd logp1`KHL2{λq 
pairs of ph, kq tuple such that detUh,k ď 2 detU1,k. 
Lemma 2.8.14 (Lemma 12, Abbasi-Yadkori et al. (2011)). Suppose A,B P Rdˆd are two 
positive definite matrices satisfying that A ľ B, then for any x P Rd, we have }x}A ď 
}x}B a 
detpAq{ detpBq. 
Following that, we also need to introduce the classical lemma to control the summation 
of the UCB bonus terms in vanilla linear bandit setting. 
Lemma 2.8.15 (Lemma 11, Abbasi-Yadkori et al. (2011)). For any txtu T t“1 Ă Rd satisfying 
that }xt}2 ď L, @t P rT s, let Ut “ λI ` řt´1 
τ“1 xτx J τ , we have 
T ÿ 
t“1 
mint1, }xt}U´1 t 
u 2 
ď 2d log 
ˆ 
dλ ` TL2 
dλ 
˙ 
. 
We also need to introduce the Azuma-Hoeffding’s inequality to build the concentration 
bound for martingale difference sequences. 
51
Lemma 2.8.16 (Azuma-Hoeffding’s inequality, Azuma (1967)). Let txiu n i“1 be a martingale 
difference sequence with respect to a filtration tGiu n i“1 (i.e. Erxi|Gis “ 0 a.s. and xi is Gi`1 
measurable) such that |xi| ď M a.s.. Then for any 0 ă δ ă 1, with probability at least 1´ δ, řn 
i“1 xi ď M a 
2n logp1{δq. 
Proof of Lemma 2.8.3. By Lemma 2.8.1, for the k-th episode, we have 
V k 1 psk1q ´ V πk 
psk1q “ E „ H ÿ 
h“1 
mintH, 2β}ψV k h`1 
psh, π k hpshqq}Σ´1 
1,k u 
ˇ 
ˇ 
ˇ 
ˇ 
sk1, π k 
ȷ 
ď E „ H ÿ 
h“1 
mintH, 2β}ψuk h psh, π 
k hpshqq}Σ´1 
1,k u 
ˇ 
ˇ 
ˇ 
ˇ 
sk1, π k 
ȷ 
(2.8.17) 
where the inequality comes from that the pseudo value function uk h defined in (2.4.3) is from 
maximizing the UCB term }ψV k h`1 
psh, π k hpshqq}Σ´1 
1,k and we denote tπk 
huHh“1 by πk in short. By 
the definition of rkh, we have 
V πk 
psk1q “ Er 
H ÿ 
h“1 
rkhpsh, π k hpshqq|sk1, π 
k s 
“ E „ H ÿ 
h“1 
mint1, 2β}ψuk h psh, π 
k hpshqq}Σ´1 
1,k {Hu 
ˇ 
ˇ 
ˇ 
ˇ 
sk1, π k 
ȷ 
. (2.8.18) 
Adding (2.8.17) and (2.8.18) together and taking summation over k, we have 
K ÿ 
k“1 
V k 1 psk1q ď 
H ` 1 
H 
K ÿ 
k“1 
E „ H ÿ 
h“1 
mintH, 2β}ψuk h psh, π 
k hpshqq}Σ´1 
1,k u 
ˇ 
ˇ 
ˇ 
ˇ 
sk1, π k 
ȷ 
loooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooon 
I1 
ď 2I1, (2.8.19) 
where the last inequality is due to pH ` 1q{H ď 2. Next we are going to control the 
expectation of summation I1. Consider the filtration tGh,ku H,K h“1,k“1 defined in Section 2.8.5.1, 
denote xh,k as follows: 
xh,k “ mintH, 2β}ψuk h pskh, a 
k hq}Σ´1 
1,k u ´ Esh 
“ 
mintH, 2β}ψuk h psh, π 
k hpshqq}Σ´1 
1,k u ‰ 
, 
then xh,k is obviously a martingale difference sequence bounded by H w.r.t. tGh,ku H,K h“1,k“1. 
Thus by Azuma-Hoeffding’s inequality in Lemma 2.8.16, we have with probability at least 
52
1 ´ δ, řK 
k“1 
řH h“1 xh ď H 
a 
2HK logp1{δq. Therefore, 
I1 “ 
K ÿ 
k“1 
H ÿ 
h“1 
mintH, 2β}ψuk h pskh, a 
k hq}Σ´1 
1,k u ` 
K ÿ 
k“1 
H ÿ 
h“1 
xh 
ď 2β K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}Σ´1 
1,k u ` H 
a 
2HK logp1{δq 
ď 2 ? 2β 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}Σ´1 
h,k u 
looooooooooooooooooomooooooooooooooooooon 
I2 
`4βHd logp1 ` KH3 {λq ` H 
a 
2HK logp1{δq, 
where the inequality on the second line is due to 2β ě 2H ? d log 3 ě H and the last 
inequality uses Lemma 2.8.14 with Σ´1 1,k ľ Σ´1 
h,k and detΣ´1 1,k ď 2 detΣ´1 
1,k expect for ÕpHdq 
cases by Lemma 2.8.13. By mint1, }ψuk h psh, π 
k hpshqq}Σ´1 
h,k u ď 1 and }ψuk 
h pskh, a 
k hq}2 ď H since 
uk h ď H, we can further bound the ÕpHdq terms where detΣ´1 
1,k ą 2 detΣ´1 1,k. To bound I2, 
by Lemma 2.8.15, using Cauchy-Schwarz inequality we have 
I2 ď ? KH 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}2 
Σ´1 h,k 
u ď a 
2KHd logp1 ` KH3{pdλqq, 
Plugging I2 into I1 then plugging I1 into (2.8.19). Let λ “ B´2, the summation of the 
value function V k 1 psk1q is bounded by 
K ÿ 
k“1 
V k 1 psk1q ď 8β 
´ 
a 
HKd logp1 ` KH3B2{dq ` dH logp1 ` KH3B2 q 
¯ 
` 2H a 
2HK logp1{δq. 
Taking δ “ δ{3, we can finalize the proof of Lemma 2.8.3. 
2.8.5.5 Proof of Lemma 2.8.4 
The proof of this lemma is similar to the proof of Lemma 5.2 in (Zhou et al., 2021a). We 
extend their proof to a time varying reward and homogeneous setting, where the rewards 
(i.e., the exploration-driven reward function rkh) are different in different episode k. To prove 
this lemma, we need to introduce the Bernstein inequality for vector-valued martingales. 
53
Lemma 2.8.17 (Theorem 4.1, Zhou et al. (2021a)). Let tGtu 8 t“1 be a filtration, txt, ηtutě1 a 
stochastic process so that xt P Rd is Gt-measurable and ηt is Gt`1-measurable. Fix R,L, σ, λ ą 
0,µ˚ P Rd. For t ě 1, let yt “ xµ˚,xty ` ηt. Suppose ηt,xt satisfy 
|ηt| ď R, Erηt|Gts “ 0, Erη2t |Gts ď σ2, }xt}2 ď L. 
Then for any 0 ă δ ă 1, with probability at least 1 ´ δ, we have 
@t ą 0, 
› 
› 
› 
› 
t ÿ 
τ“1 
xτητ 
› 
› 
› 
› 
U´1 τ 
ď βt, }µt ´ µ˚ }Ut ď βt ` 
? λ}µ˚ 
}2, 
where µt “ U´1 t bt,Ut “ λI ` 
řt τ“1 xτx 
J τ ,bt “ 
řt τ“i yτxτ , and 
βt “ 8σ a 
d logp1 ` tL2{dλq logp4t2{δq ` 4R logp4t2{δq. 
We also introduce the following lemma to analyze the error between the estimated vari-
ance V̄k h and the true variance Vk 
h. 
Lemma 2.8.18 (Lemma C.1, Zhou et al. (2021a)). Let Vk hps, aq be as defined in (2.3.1) and 
V̄k hps, aq be as defined in (2.5.3), then 
|Vk hps, aq ´ V̄k 
hps, aq| ď min ! 
H2, }ψrV k h`1s2ps, aq}Σ̃´1 
1,k }θ̃k ´ θ˚ 
}Σ̃1,k 
) 
` min ! 
H2, 2H}ψV k h`1 
ps, aq}Σ̂´1 1,k 
}θ̂k ´ θ˚ }Σ̂1,k 
) 
. 
Equipped with these lemmas, we can start the proof of Lemma 2.8.4. 
Proof of Lemma 2.8.4. Recall the regression in (2.5.4). For the regression on Σ̂, θ̂, let xk h “ 
ψV k h`1 
pskh, a k hq{σ̄k 
h, and ηkh “ V k h`1ps 
k h`1q{σ̄k 
h ´ xθ˚,xk hy. Since σ̄k 
h ě H{ ? d defined in (2.5.2), 
we get }xk h}2 ď 
? d, |ηkh| ď 
? d, thus one could verify that Errηkhs2|Gh,ks ď d, Erηkh|Gh,ks “ 0, 
from Lemma 2.8.17, taking t “ pk ´ 1qH we have 
}θ˚ ´ θ̂k}Σ̂1,k 
ď 8d a 
logp1 ` pk ´ 1qH{λq logp4pk ´ 1q2H2{δq 
` 4 ? d logp4pk ´ 1q 
2H2 {δq ` 
? λB. 
54
For the regression of Σ̃, θ̃, xk h “ ψrV k 
h`1s2pskh, a k hq which directly implies }xk 
h}2 ď H2. 
Let ηkh “ V k h`1ps 
k h`1q2 ´ xθ˚,xk 
hy, one can easily verify that |ηkh| ď H2 and Erηkh|Gh,ks “ 
0,Errηkhs2|Gh,ks ď H4, thus using Lemma 2.8.17 again we have 
}θ˚ ´ θ̃k}Σ̃1,k 
ď 8H2 a 
d logp1 ` pk ´ 1qH{λq logp4pk ´ 1q2H2{δq 
` 4H2 logp4pk ´ 1q 2H2 
{δq ` ? λB. 
Since λ “ B´2, if we select β̌ and β̃ as 
β̌ “ 8d a 
logp1 ` KHB2{q logp4K2H2{δq ` 4 ? d logp4pk ´ 1q 
2H2 {δq ` 1 
β̃ “ 8H2 a 
d logp1 ` KHB2q logp4K2H2{δq ` 4H2 logp4K2H2 {δq ` 1, 
then with probability at least 1´2δ, for all k P rK `1s, }θ˚ ´ θ̂k}Σ̂1,k ď β̌, }θ˚ ´ θ̃k}Σ̃1,k 
ď β̃. 
Next we are going to give the choice of β̂ to make sure that }θ˚ ´ θ̂k}Σ̂1,k ď β̌ holds 
with high probability. The following proof is conditioned on that the aforementioned event 
}θ˚ ´ θ̂k}Σ̂1,k ď β̌, }θ˚ ´ θ̃k}Σ̃1,k 
ď β̃ holds, then from Lemma 2.8.18 we have 
|Vk hps, aq ´ V̄k 
hps, aq| 
ď min ! 
H2, β̃}ψrV k h`1s2ps, aq}Σ̃´1 
1,k 
) 
` min ! 
H2, 2β̌H}ψV k h`1 
ps, aq}Σ̂´1 1,k 
) 
“ Ek hps, aq (2.8.20) 
Again, let xk h “ ψV k 
h`1 pskh, a 
k hq{σ̄k 
h to denote the context vector and ηkh “ V k h`1pskh`1q{σ̄k 
h ´ 
xθ˚,xk hy to denote the noise term, since }θ˚ ´ θ̂k}Σ̂1,k 
ď β̌, we have 
Errηkhs 2 |Gh,ks “ Vk 
hpskh, a k hq{νk 
h ď pEk hpskh, a 
k hq ` V̄k 
hpskh, a k hqq{νk 
h ď 1, 
where the first inequality is from (2.8.20), the second inequality holds because the definition 
of νk h in (2.5.2). 
Therefore we have verified that the noise term ηkh is a zero-mean random variable condi-
tioned on Gh,k and Errηkhs2|Gh,ks ď 1. In that case, using Lemma 2.8.17 again we could get 
55
with probability at least 1 ´ δ, 
}θ˚ ´ θ̂k}Σ̂1,k 
ď 8 a 
dp1 ` pk ´ 1qH{λq logp4pk ´ 1q2H2{δq (2.8.21) 
` 4 ? d logp4pk ´ 1q 
2H2 {δq ` 
? λB, (2.8.22) 
again, since λ “ B´2, if we select β̂ as 
β̂ “ 8 a 
dp1 ` KHB2q logp4K2H2{δq ` 4 ? d logp4K2H2 
{δq ` 1, 
then }θ˚ ´ θ̂k}Σ̂1,k ď β̂ with probability at least 1 ´ δ for all k P rK ` 1s. 
Next, for the regression of θK`1,Σ1,K`1, by Lemma 2.8.2, we obtain the same result with 
the selection of β as 
β “ H 
d 
d log 
ˆ 
1 ` KH3{λ 
δ 
˙ 
` B ? λ, 
which suggests that with probability at least 1´δ, }θK`1´θ˚}Σ1,K`1 ď β. Then taking union 
bound with all aforementioned event }θ˚ ´ θ̂k}Σ̂1,k ď β̌, }θ˚ ´ θ̃k}Σ̃1,k 
ď β̃, }θ˚ ´ θ̂k}Σ̂1,k ď β̂, 
we have all these events mentioned in this proof holds with probability at least 1 ´ 4δ. 
Replace δ with δ{12, we obtain our final results. 
Next, for the regression of θK`1,Σ1,K`1, by Lemma 2.8.2, we obtain the same result with 
the selection of β as 
β “ H 
d 
d log 
ˆ 
1 ` KH3{λ 
δ 
˙ 
` B ? λ, 
which suggests that with probability at least 1´ δ, }θK`1 ´θ˚}Σ1,K`1 ď β. Again, taking an 
additional union bound, with probability at least 1 ´ 4δ, all events mentioned in this proof 
hold. Replace δ with δ{12, we obtain our final results. 
2.8.5.6 Proof of Lemma 2.8.5 
The proof of this lemma borrows some intuition from the proof of Theorem 5.3 in (Zhou 
et al., 2021a). Unlike Zhou et al. (2021a) that deals the fixed reward and time-inhomogeneous 
56
setting, we need to extend their proof in order to deal with the time-varying reward and time-
homogeneous setting. 
The next lemmas shows the relationship between the summation of νk h and the difference 
between V k h psq calculated in Algorithm 3 and V πk 
h ps; trkhu H,K h“1,k“1q 
Lemma 2.8.19. Let V k h , ν 
k h be defined in Algorithm 3. Then if the condition in Lemma 2.8.4 
holds, the following inequality holds with probability at least 1 ´ 2δ, 
K ÿ 
k“1 
rV k 1 psk1q ´ V πk 
1 psk1qs ď 4 ? dβ̂ 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
a 
logp1 ` KHB2q 
` 2H2d logp1 ` KHB2dq ` H a 
2KH logp1{δq 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1qspskh, a k hq ď 4 
? dHβ̂ 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
a 
logp1 ` KHB2q 
` 2H3d logp1 ` KHB2dq ` 2H2 a 
2KH logp1{δq, 
Lemma 2.8.20. Let V k h , νk 
h be defined in Algorithm 3. Then if the condition in Lemma 2.8.4 
holds, with probability at least 1 ´ δ, 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ď 
H3K 
d ` 3H2K ` 3H3 logp1{δq ` 2H 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1sps k h, a 
k hq 
` 2β̃ a 
KHd logp1 ` KH5B2{dq ` 4β̃Hd logp1 ` KH5B2 {dq 
` 8H2β̌ a 
KHd logp1 ` KHB2q ` 8H3dβ̌ logp1 ` KHdB2 q. 
Equipped with these two lemmas, we can start to prove Lemma 2.8.5. 
Proof of Lemma 2.8.5. In this proof, we use Õp¨q to ignore all constant and log terms to 
simplify the results. Recall the selection of β, β̂, β̌, β̃, we have β “ ÕpH ? dq, β̂ “ Õp 
? dq, 
β̌ “ Õpdq, β̃ “ ÕpH2 ? dq. Therefore Lemma 2.8.19 could be simplified as 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1qspskh, a k hq ď Õ 
˜ 
Hd 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ` H3d ` 
? KH5 
¸ 
. (2.8.23) 
57
Lemma 2.8.20 could also be simplified as 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ď Õ 
˜ 
H3K 
d ` H2K ` H 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1qspskh, a k hq ` 
? KH5d3 ` H3d2 
¸ 
. 
(2.8.24) 
Let b 
řK k“1 
řH h“1 ν 
k h “ x, plugging (2.8.23) into (2.8.24), we have 
x2 ď ÕpH3Kd´1 
` H2K ` H2dx ` H4d ` ? KH7 ` 
? KH5d3 ` H3d2q, 
Since the quadratic inequality x2 ď Õpbx ` cq indicates that x ď Opb ` ? cq, setting 
b “ ÕpH2dq, c “ ÕpH3Kd´1 ` H2K ` H4d ` 
? KH7 ` 
? KH5d3 ` H3d2q, 
hence g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ď ÕpH2d ` 
a 
H3K{d ` H ? K ` H2 
? d ` d 
? H3 ` pKH7 
q 1{4 
` pKH5d3q 1{4 
q 
(2.8.25) 
“ Õp a 
H3K{d ` H ? Kq ` op 
? Kq. (2.8.26) 
Plugging (2.8.26) back to Lemma 2.8.19, we have 
K ÿ 
k“1 
rV k 1 psk1q ´ V πk 
1 psk1qs ď Õp ? H3Kd ` Hd 
? Kq ` op 
? Kq. (2.8.27) 
Next we are going to show the bound of the summation over V πk 
1 psk1q, note that this value 
function is bounded by H and from Bellman equality, we have 
V πk 
h psk1q “ rkhpsk1, a k 1q ` rPV πk 
h`1spskh, a k hq, 
taking summation over h P rHs, k P rKs then 
K ÿ 
k“1 
V πk 
1 psk1q “ 
K ÿ 
k“1 
H ÿ 
h“1 
rkhpsk1, a k 1q ` 
K ÿ 
k“1 
H ÿ 
h“1 
rPV πk 
h`1spskh, a k hq ´ V πk 
h`1pskh`1q 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, 2β}ψuk h pskh, a 
k hq}Σ´1 
1,k {Hu ` H 
a 
HK logp1{δq, 
58
where the last inequality holds due to Azuma-Hoeffding’s inequality i.e. Lemma 2.8.16. For 
the first term, 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, 2β}ψuk h pskh, a 
k hq}Σ´1 
1,k {Hu ď 
2β 
H 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}Σ´1 
1,k u 
looooooooooooooooooomooooooooooooooooooon 
I1 
, 
where the inequality is due to β ě H a 
logp12q ě H{2. Since Lemma 2.8.13 suggests 
that there are only up to ÕpHdq steps with detΣ´1 1,k ď 2 detΣ´1 
h,k, by Lemma 2.8.13 and 
Lemma 2.8.14 with Σ´1 1,k ľ Σ´1 
h,k and setting λ “ B´2, we have 
I1 ď 2Hd logp1 ` KH3B2 q ` 
? 2 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}Σ´1 
h,k u 
ď 2Hd logp1 ` KH3B2 q ` 
? 2HK 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψuk h pskh, a 
k hq}2 
Σ´1 h,k 
u 
ď 2Hd logp1 ` KH3B2 q ` 2 
a 
HKd logp1 ` KH3B2{dq. 
Therefore, since β “ ÕpH ? dq, then 
K ÿ 
k“1 
V πk 
1 psk1q ď 4βd logp1 ` KH3B2 q ` 4β 
a 
Kd logp1 ` KH3B2{dq{H ` a 
H3K logp1{δq 
(2.8.28) 
ď Õpd ? KH ` 
? KH3q ` op 
? Kq. (2.8.29) 
Adding (2.8.27) and (2.8.29) together, we have the following result, 
K ÿ 
k“1 
V k 1 psk1q ď Õp 
? H3Kd ` Hd 
? Kq ` op 
? Kq. 
By taking the union bound, this inequality holds with probability at least 1 ´ 4δ. Since δ 
only appears in the logarithmic terms, thus changing δ to δ{12 will not affect the result. 
59
2.8.6 Proof of Auxiliary Lemmas in Section 2.8.5 
2.8.6.1 Proof of Lemma 2.8.13 
Proof of Lemma 2.8.13. We bound the number of tuples ph, kq with detUh,k ě 2 detU1,k. 
To begin with, if there exists k P rKs such that detU1,k`1 ď 2 detU1,k, then it is obvious 
that for all h P rHs, we have detUh,k ď detU1,k`1 ď 2 detU1,k. 
Therefore, suppose there exists a set K Ă rKs such that for all k R K, detU1,k`1 ď 
2 detU1,k and for all k P K, detU1,k`1 ą 2 detU1,k, then the pair of ph, kq such that 
detUh,k ě 2 detU1,k is upper bounded by H|K|. 
Notice that for all k P K, detU1,k`1 ą 2 detU1,k, it is easy to show that 
detU1,K`1 ą 2|K| detU1,1 “ 2|K|λd, 
where the last inequality comes from U1,1 “ λI P Rdˆd. Notice that detU ď }U}d2, taking 
log we have 
d logp}U1,K`1}2q ě log detU1,K`1 ą |K| log 2 ` d log λ. (2.8.30) 
From the definition of U1,K`1, by triangle inequality, 
}U1,K`1}2 ď λ ` ÿ 
k“1 
K H ÿ 
h“1 
}xk hx 
kJ h }2 ď λ ` KH}xk 
h} 2 2 ď λ ` KHL2, (2.8.31) 
where the last inequality is due to }x}2 ď L from the statement of the lemma. Therefore we 
conclude our proof by merging (2.8.30) and (2.8.31) together to get 
|K| log 2 ă d logp1 ` HKL2 {λq, 
noticing log 2 ě 1{2 we can get the result claimed in the lemma. 
60
2.8.6.2 Proof of Lemma 2.8.19 
Proof of Lemma 2.8.19. Assume that the condition in Lemma 2.8.4 holds, then 
V k h pskhq ´ V πk 
h pskhq 
ď xθ̂k,ψV k h`1 
pskh, a k hqy ´ rPV πk 
h`1sps k h, a 
k hq ` β̂}ψV k 
h`1 pskh, a 
k hq}Σ̂´1 
1,k 
ď }θ̂k ´ θ˚ }Σ̂1,k 
}ψV k h`1 
pskh, a k hq}Σ̂´1 
1,k ` rPV k 
h`1 ´ V πk 
h`1spskh, a k hq ` β̂}ψV k 
h`1 pskh, a 
k hq}Σ̂´1 
1,k 
ď 2β̂}ψV k h`1 
pskh, a k hq}Σ̂´1 
1,k ` rPV k 
h`1 ´ V πk 
h`1sps k h, a 
k hq, 
where the first inequality holds due to the definition of V k h , the second inequality holds 
due to Cauchy-Schwarz inequality and the third one holds due to the condition (2.8.8) in 
Lemma 2.8.4. Notice that V k h ´ V πk 
h ď H, we have 
V k h pskhq ´ V πk 
h pskhq ď mintH, 2β̂}ψV k h`1 
pskh, a k hq}Σ̂´1 
1,k u ` rPV k 
h`1 ´ V πk 
h`1spskh, a k hq 
Taking summation over k P rKs and h P rHs, we have 
K ÿ 
k“1 
rV k 1 psk1q ´ V πk 
1 psk1qs ď 
K ÿ 
k“1 
H ÿ 
h“1 
mintH, 2β̂}ψV k h`1 
pskh, a k hq}Σ̂´1 
1,k u 
` 
K ÿ 
k“1 
H ÿ 
h“1 
” 
rPV k h`1 ´ V πk 
h`1spskh, a k hq ´ rV k 
h`1ps k h`1q ´ V πk 
h`1pskh`1qs 
ı 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
mintH, 2β̂}ψV k h`1 
pskh, a k hq}Σ̂´1 
1,k u 
looooooooooooooooooooooomooooooooooooooooooooooon 
I1 
`H a 
2KH logp1{δq, 
(2.8.32) 
where the second inequality is due to Azuma-Hoeffding’s inequality as in Lemma 2.8.16. 
Next we bound I1. Recall the update rule of Σ̂h,k, notice that σ̄k h ě H{ 
? d and the fact 
that }ψV k h`1 
psKh , a K h q}2 ď H from V k 
h`1 ď H, it is easy to verify that }ψV k h`1 
psKh , a K h q{σ̂k 
h}2 ď 
61
? d. Hence 
I1 ď ? 2 
K ÿ 
k“1 
H ÿ 
h“1 
mintH, 2β̂}ψV k h`1 
pskh, a k hq}Σ̂´1 
h,k u ` 2H2d logp1 ` KHd{λq 
ď ? 2maxt 
? d, 2β̂u 
K ÿ 
k“1 
H ÿ 
h“1 
σ̄k h mint1, }ψV k 
h`1 pskh, a 
k hq{σ̄k 
h}Σ̂´1 h,k 
u ` 2H2d logp1 ` KHd{λq 
ď 2 ? 2β̂ 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψV k h`1 
pskh, a k hq{σ̄k 
h}2 Σ̂´1 
h,k 
u ` 2H2d logp1 ` KHd{λq 
ď 4β̂ ? d 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
a 
logp1 ` KH{λq ` 2H2d logp1 ` KHd{λq, 
where the first inequality, similar to the corresponding proof in Lemma 2.8.3, is a direct 
implication of Lemma 2.8.13 and Lemma 2.8.14 with Σ̂´1 1,k ľ Σ̂´1 
h,k and detΣ´1 1,k ď 2 det Σ̂´1 
1,k 
except for ÕpHdq cases mentioned in Lemma 2.8.13, the second inequality moves σ̄k h outside, 
the third inequality holds because β̂ ě 4 ? d log 12 ě 
? d and Cauchy-Schwarz inequality, 
and the forth inequality holds due to Lemma 2.8.15. Plugging I1 into (2.8.32) and let 
h1 “ 1, λ “ B´2, we have 
K ÿ 
k“1 
rV k 1 psk1q ´ V πk 
1 psk1qs ď 4 ? dβ̂ 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
a 
logp1 ` KHB2q 
` 2H2d logp1 ` KHB2dq ` H a 
2KH logp1{δq. 
Furthermore, by Azuma-Hoeffding’s inequality as in Lemma 2.8.16, 
K ÿ 
k“1 
H ÿ 
h“1 
PrV k h`1 ´ V πk 
h`1spskh, a k hq “ 
K ÿ 
k“1 
H ÿ 
h“2 
rV k h ´ V πk 
h spskhq 
` 
K ÿ 
k“1 
H ÿ 
h“1 
” 
PpV k h`1 ´ V πk 
h`1sps k h, a 
k hq ´ rV k 
h`1 ´ V πk 
h`1qspskh`1q 
ď 4 ? dHβ̂ 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
νk h 
a 
logp1 ` KHB2q 
` 2H3d logp1 ` KHB2dq ` pH ` 1qH a 
2KH logp1{δq, 
62
which becomes the second part of the statement in the lemma. Using H ` 1 ď 2H we can 
get the result claimed in the lemma. 
2.8.6.3 Proof of Lemma 2.8.20 
To begin with, we will first show the total variance lemma originally introduced in (Jin et al., 
2018). 
Lemma 2.8.21 (Total variance lemma, Lemma C.5, Jin et al. (2018)). 2 With probability 
at least 1 ´ δ, we have 
K ÿ 
k“1 
H ÿ 
h“1 
rVV πk 
h p¨; trkhu H h“1qsps, aq ď 3H2K ` 3H3 logp1{δq. 
Proof of Lemma 2.8.20. Assume the condition in Lemma 2.8.4 holds, we have with proba-
bility at least 1 ´ δ, 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ď 
K ÿ 
k“1 
H ÿ 
h“1 
ˆ 
H2 
d ` V̄k 
hpskh, a k hq ` Ek 
hpskh, a k hq 
˙ 
“ H3K 
d ` 
K ÿ 
k“1 
H ÿ 
h“1 
´ 
rVhV k h`1sps 
k h, a 
k hq ´ rVhV 
πk 
h`1spskh, a k hq 
¯ 
looooooooooooooooooooooooooooomooooooooooooooooooooooooooooon 
I1 
`2 H ÿ 
k“1 
H ÿ 
h“1 
Ek hpskh, a 
k hq 
looooooooomooooooooon 
I2 
` 
K ÿ 
k“1 
H ÿ 
h“1 
rVhV πk 
h`1sps k h, a 
k hq 
looooooooooooomooooooooooooon 
I3 
` 
K ÿ 
k“1 
H ÿ 
h“1 
” 
V̄k hpskh, a 
k hq ´ rVhV 
k h`1sps 
k h, a 
k hq ´ Ek 
h 
ı 
loooooooooooooooooooooooooooomoooooooooooooooooooooooooooon 
I4 
ď H3K 
d ` I1 ` I2 ` 3H2K ` 3H3 logp1{δq, (2.8.33) 
where the value function V πk 
h psq is short for V πk 
h ps; trkhuHh“1q for simplicity. The first inequality 
is from the definition of νk h in (2.5.2), while the last inequality is from Lemma 2.8.21 to control 
I3. I4 ď 0 is due to Lemma 2.8.4. Next we are about to bound I1 and I2 separately. 
2The original Lemma C.5 in Jin et al. (2018) holds for the identical reward functions, i.e., r1h “ ¨ ¨ ¨ “ rKh . Their lemma also holds for the general case r1h ‰ ¨ ¨ ¨ ‰ rKh without changing their proof. 
63
Since the estimated value function V k h`1 and the real value function V πk 
h`1 are both bounded 
by r0, Hs, we have 
I1 ď 
K ÿ 
k“1 
H ÿ 
h“1 
“ 
PprV k h`1s 
2 ´ rV πk 
h`1s 2 q ‰ 
pskh, a k hq ď 2H 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1qspskh, a k hq. 
For term I2, we have 
I2 ď 
K ÿ 
k“1 
H ÿ 
h“1 
mintH2, β̃}ψrV k h`1s2pskh, a 
k hq}Σ̃´1 
1,k u ` 
K ÿ 
k“1 
H ÿ 
h“1 
mintH2, 2Hβ̌}ψV k h`1 
ps, aq}Σ̂´1 1,k 
u 
ď maxtH2, β̃u 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψrV k h`1s2pskh, a 
k hq}Σ̃´1 
1,k u 
` 
K ÿ 
k“1 
H ÿ 
h“1 
maxtH2, 2Hβ̌σ̄k humin 
␣ 
1, › 
›ψV k h`1 
ps, aq{σ̄k h 
› 
› 
Σ̂´1 1,k 
( 
. 
Noticing that from the definition of νk h , 
νh k “ maxtH2 
{d, V̄k hpskh, a 
k hq ` Ek 
hpskh, a k hqu ď maxtH2 
{d,H2 ` 2H2 
u “ 3H2, 
thus σ̄k h “ 
a 
νk h ď 2H. Recall that β̃ ě 4H2 logp12q ě H2 and β̌ ě 1, we have 
I2 ď β̃ K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψrV k h`1s2pskh, a 
k hq}Σ̃´1 
1,k u 
loooooooooooooooooooooomoooooooooooooooooooooon 
I5 
`4H2β̌ K ÿ 
k“1 
H ÿ 
h“1 
min ␣ 
1, › 
›ψV k h`1 
ps, aq{σ̄k h 
› 
› 
Σ̂´1 1,k 
( 
loooooooooooooooooooooomoooooooooooooooooooooon 
I6 
. 
For I5, using Lemmas 2.8.13 and 2.8.14 with Σ̃´1 1,k ľ Σ̃´1 
h,k and det Σ̃´1 1,k ď 2 det Σ̃´1 
1,k except 
for ÕpHdq cases mentioned in Lemma 2.8.13, we have 
I5 ď ? 2 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψrV k h`1s2pskh, a 
k hq}Σ̃´1 
h,k u ` 2Hd logp1 ` KH5 
{dλq 
ď ? 2KH 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
mint1, }ψrV k h`1s2pskh, a 
k hq}2 
Σ̃´1 h,k 
u ` 2Hd logp1 ` KH5 {dλq 
ď 2 a 
KHd logp1 ` KH5{dλq ` 2Hd logp1 ` KH5 {dλq, 
where the first inequality is a direct implication from Lemma 2.8.13 and the second inequality 
is due to Cauchy-Schwarz inequality. The third inequality utilizes Lemma 2.8.15. As for I6, 
64
we have 
I6 ď ? 2 
K ÿ 
k“1 
H ÿ 
h“1 
min ␣ 
1, › 
›ψV k h`1 
ps, aq{σ̄k h 
› 
› 
Σ̂´1 h,k 
( 
` 2Hd logp1 ` KHd{λq 
ď ? 2KH 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
min ␣ 
1, › 
›ψV k h`1 
ps, aq{σ̄k h 
› 
› 
Σ̂´1 h,k 
( 
` 2Hd logp1 ` KHd{λq 
ď 2 a 
KHd logp1 ` KH{λq ` 2Hd logp1 ` KHd{λq. 
Finally, plugging I5, I6 into I2 and I1, I2 into (2.8.33) we have 
K ÿ 
k“1 
H ÿ 
h“1 
νk h ď 
H3K 
d ` 3H2K ` 3H3 logp1{δq ` 2H 
K ÿ 
k“1 
H ÿ 
h“1 
rPpV k h`1 ´ V πk 
h`1sps k h, a 
k hq 
` 2β̃ a 
KHd logp1 ` KH5{dλq ` 4β̃Hd logp1 ` KH5 {dλq 
` 8H2β̌ a 
KHd logp1 ` KH{λq ` 8H3dβ̌ logp1 ` KHd{λq. 
Using λ “ B´2, we could get the result in the statement of the lemma. 
2.8.7 Missing Proof in Section 2.8.3 
2.8.7.1 Proof of Lemma 2.8.7 
To start with, we recall that event E2.8.6 is defined by the the case when Lemma 2.8.6 holds. 
And the following lemmas are conditioned on E2.8.6 by default. We define function Wh for 
certain sequence tRhu recursively as 
Wh ptRhuq “ min t1, Rh ` Wh`1 ptRhuqu . 
In addition we denote the trajectory of first h steps as trajh :“ ps1, a1, ¨ ¨ ¨ , sh´1, ah´1, shq, 
and the trajectory sampled from pπ,Pq conditioned on trajh as traj „ pπ,Pq|trajh. 
Lemma 2.8.22. For any policy π and reward function r P R, we have 
V1ps1;θK , π, rq ´ V1ps1;θ ˚, π, rq “ Etraj„pπ,Pq|traj1W1ptpPK ´ PqVh`1psh;θK , π, rquq 
(2.8.34) 
65
Lemma 2.8.23. For any policy π and reward function r P R, we have 
Etraj„pπ,Pq|traj1W1 ptuk,hpsh, πpshq;θK , π, rquq ď V̂K,1 ps1;θK , πK , rKq . 
Proof of Lemma 2.8.7. The proof follows the proof of Lemma 15 in Zhang et al. (2020). 
Firstly, 
V ˚ 1 ps1; rq ´ V1ps1;θ 
˚, π̂r, rq 
“ pV ˚ 1 ps1; rq ´ V1ps1;θK , π̂r, rqq ` pV1ps1;θK , π̂r, rq ´ V1ps1;θ 
˚, π̂r, rqq 
ď pV ˚ 1 ps1; rq ´ V1ps1;θK , π 
˚ r , rqq ` pV1ps1;θK , π̂r, rq ´ V1ps1;θ 
˚, π̂r, rqq, (2.8.35) 
where π˚ r is the optimal policy for pθ, rq, and π̂r is the optimal policy for pθK , rq. Then for 
any policy π P Π, 
|V1ps1;θK , π, rq ´ V1ps1;θ ˚, π, rq| 
“ ˇ 
ˇEtraj„pπ,Pq|traj1W1 ptpPK ´ PqVh`1psh, ah;θK , π, rquq ˇ 
ˇ 
“ ˇ 
ˇEtraj„pπ,Pq|traj1W1 
`␣ 
pθK ´ θ˚ qϕVh`1p¨;θK ,π,rqpsh, ahq 
(˘ ˇ 
ˇ 
ď Etraj„pπ,Pq|traj1W1 
ˆ" 
}θK ´ θ˚ } 9̃ Σk,0 
› 
›ϕVh`1p¨;θK ,π,rqpsh, ahq › 
› 
9̃ Σ 
´1 
k,0 
*˙ 
ď Etraj„pπ,Pq|traj1W1 
ˆ" 
2β › 
›ϕVh`1p¨;θK ,π,rqpsh, ahq › 
› 
9̃ Σ 
´1 
k,0 
*˙ 
“ 2Etraj„pπ,Pq|traj1W1 ptuhpsh, ah;θK , π, rquq 
ď 2V̂K,1ps1;θK , πK , rKq. (2.8.36) 
The first equality holds due to Lemma 2.8.22, the second inequality holds due to Cauchy-
Schwartz inequality, the third inequality holds due to Lemma 2.8.6, and the last inequality 
holds due to Lemma 2.8.23. Plugging (2.8.36) into (2.8.36), we obtain 
V ˚ 1 ps1; rq ´ V1ps1;θ 
˚, π̂r, rq ď 2V̂K,1ps1;θK , πK , rKq ` 2V̂K,1ps1;θK , πK , rKq 
“ 4V̂K,1ps1;θK , πK , rKq. 
66
2.8.7.2 Proof of Lemma 2.8.8 
Proof of Lemma 2.8.8. The proof follows the proof of Lemma 14 in Chen et al. (2021). 
Firstly, we prove that V̂k,1ps;θ, π, rq is non-increasing w.r.t. k for any fixed θ, π, r by in-
duction in h. Suppose for any k1 ď k2, V̂k1,h`1ps;θ, π, rq ě V̂k2,h`1ps;θ, π, rq for any s. By 
definition, 
V̂k,hps;θ, π, rq “ min 
" 
1, uk,hps, a;θ, π, rq ` 2β › 
› 
› ϕV̂k,h`1p¨;θ,π,rq 
ps, πpsqq 
› 
› 
› 9̂ Σ 
´1 
k,0 
` ϕJ 
V̂k,h`1p¨;θ,π,rq ps, πpsqqθ 
* 
uk,hps, a;θ, π, rq “ β › 
›ϕVhp¨;θ,π,rqps, aq › 
› 
9̃ Σ 
´1 
k,0 
Since 9̂ Σk1,0 ĺ 
9̂ Σk2,0 and 9̃ 
Σk1,0 ĺ 9̃ Σk2,0, we have 
uk1,hps, a;θ, π, rq ě uk2,hps, a;θ, π, rq › 
› 
› ϕV̂k1,h`1p¨;θ,π,rq 
ps, πpsqq 
› 
› 
› 9̂ Σ 
´1 
k,0 
ě 
› 
› 
› ϕV̂k2,h`1p¨;θ,π,rq 
ps, πpsqq 
› 
› 
› 9̂ Σ 
´1 
k,0 
ϕJ 
V̂k1,h`1p¨;θ,π,rq ps, πpsqqθ ě ϕJ 
V̂k2,h`1p¨;θ,π,rq ps, πpsqqθ 
Thus V̂k1,hps;θ, π, rq ě V̂k2,hps;θ, π, rq for any k1 ď k2. Furthermore, since Uk2 Ă Uk1 , and 
θk, πk, rk are argmax over Uk, we have 
V̂k1,1ps1;θk1 , πk1 , rk1q ě V̂k1,1ps1;θk2 , πk2 , rk2q ě V̂k2,1ps1;θk2 , πk2 , rk2q 
It follows that V̂k,1psk1;θk, πk, rkq is non-increasing w.r.t. k. Thus, 
KV̂K,1ps1;θK , πK , rKq ď 
K ÿ 
k“1 
V̂k,1ps1;θk, πk, rkq 
67
2.8.7.3 Proof of Lemma 2.8.9 
Lemma 2.8.24. Conditioned on the event E , let Ṽk,h, V̂k,h, 9̃ Σk,m, 9̂ 
Σk,m, ϕ̃k,h,m, ϕ̂k,h,m be 
defined in Algorithm 4, for any k P rKs, h P rHs, m P rM s, we have 
V̂k,hpskhq ´ uk,hpskh, a k hq ´ PV̂k,h`1ps 
k h, a 
k hq ď 4min 
" 
1, β › 
› 
› ϕ̂k,h,0 
› 
› 
› 9̂ Σ 
´1 
k,0 
* 
(2.8.37) 
Ṽk,hpskhq ´ rk,hpskh, a k hq ´ PṼk,h`1 ď 2min 
" 
1, β › 
› 
› ϕ̃k,h,0 
› 
› 
› 9̃ Σ 
´1 
k,0 
* 
(2.8.38) 
In order to prove Lemma 2.8.9, we introduce the following quantities used in Zhou and 
Gu (2022a) as 
R̂m “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ijhmin 
" 
1, β}ϕ̂k,h,m} 9̂ Σ 
´1 
k,m 
* 
, @m P rM s (2.8.39) 
R̃m “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ijhmin 
" 
1, β}ϕ̃k,h,m} 9̃ Σ 
´1 
k,m 
* 
, @m P rM s (2.8.40) 
Âm “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
”” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
´ V̂ 2m 
k,h`1 
` 
skh`1 
˘ 
ı 
, @m P rM s (2.8.41) 
Ãm “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
”” 
PṼ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
´ Ṽ 2m 
k,h`1 
` 
skh`1 
˘ 
ı 
, @m P rM s (2.8.42) 
Ŝm “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
VV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
, @m P rM s (2.8.43) 
S̃m “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
VṼ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
, @m P rM s (2.8.44) 
Ikh “ 1 
" 
@m P rM s, det 
ˆ 
9̂ Σ 
´1{2 
k,m 
˙ 
{ det ´ 
Σ̂ ´1{2 k,h,m 
¯ 
ď 4 
and det 
ˆ 
9̃ Σ 
´1{2 
k,m 
˙ 
{ det ´ 
Σ̃ ´1{2 k,h,m 
¯ 
ď 4 
* 
(2.8.45) 
G “ 
K ÿ 
k“1 
` 
1 ´ IkH ˘ 
, (2.8.46) 
Lemma 2.8.25. Let γ, α, be defined in Algorithm 5, tR̂mumPrMs , tR̃mumPrMs 
, tŜmumPrMs , 
68
tS̃mumPrMs be defined in (2.8.39), (2.8.40), (2.8.43), (2.8.44). Then for m P rM ´ 1s, we have 
R̂m ď min 
" 
KH, 4dι ` 4βγ2dι ` 2β ? dι 
b 
Ŝm ` 4R̂m ` 2R̂m`1 ` KHα2 
* 
(2.8.47) 
R̃m ď min 
" 
KH, 4dι ` 4βγ2dι ` 2β ? dι 
b 
S̃m ` 4R̃m ` 2R̃m`1 ` KHα2 
* 
, (2.8.48) 
where ι “ logp1`KH{pdλα2qq. For R̂M´1 and R̃M´1, we have the trivial bound R̂M´1 ď KH 
and R̃M´1 ď KH. 
Lemma 2.8.26. Let tR̂mumPrMs , tR̃mumPrMs 
, tŜmumPrMs , tS̃mumPrMs 
, tÂmumPrMs , tÃmumPrMs 
, 
G be defined as (2.8.39), (2.8.40), (2.8.43), (2.8.44), (2.8.41), (2.8.42), (2.8.46). Then, con-
ditioned on the event E , for m P rM ´ 1s, we have 
Ŝm ď 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
(2.8.49) 
S̃m ď 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
K ` 2R̃0 
¯ 
(2.8.50) 
Lemma 2.8.27. Let tŜmumPrMs , tS̃mumPrMs 
, tÂmumPrMs , tÃmumPrMs 
be defined as (2.8.43), 
(2.8.44), (2.8.41), (2.8.42). Then we have PpE2.8.27q ą 1 ´ 2Mδ, with E2.8.27 be defined as, 
E2.8.27 :“ " 
@m P rM s, ˇ 
ˇ 
ˇ Âm 
ˇ 
ˇ 
ˇ ď min 
" b 
2ζŜm ` ζ,KH 
* 
and ˇ 
ˇ 
ˇ Ãm 
ˇ 
ˇ 
ˇ ď min 
" b 
2ζS̃m ` ζ,KH 
** 
, (2.8.51) 
where ζ “ 4 logp4 logpKHq{δq. 
Lemma 2.8.28. Let G be defined in (2.8.46). Then we have 
G ď Mdι, (2.8.52) 
where ι “ log p1 ` KH{ pdλα2qq. 
Proof of Lemma 2.8.9. All the following proofs are conditioned on E2.8.6 XE2.8.27, which hap-
69
pens with probability at least 1 ´ 4Mδ. Firstly, we have 
K ÿ 
k“1 
V̂k,1ps k hq 
“ 
K ÿ 
k“1 
H ÿ 
h“1 
” 
Ikh 
” 
V̂k,hpskhq ´ V̂k,h`1ps k h`1q 
ı 
` ` 
1 ´ Ikh ˘ 
” 
V̂k,hpskhq ´ V̂k,h`1ps k h`1q 
ıı 
“ 
K ÿ 
k“1 
« 
H ÿ 
h“1 
Ikhuk,hpskh, a k hq ` 
H ÿ 
h“1 
Ikh 
” 
V̂h,kpskhq ´ uk,hpskh, a k hq ´ PV̂k,h`1ps 
k h, a 
k hq 
ı 
` 
H ÿ 
h“1 
Ikh 
” 
PV̂k,h`1ps k h, a 
k hq ´ V̂k,h`1ps 
k h`1q 
ı 
ff 
` 
K ÿ 
k“1 
H ÿ 
h“1 
p1 ´ Ikhq 
” 
V̂k,hpskhq ´ V̂k,h`1ps k h`1q 
ı 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
Ikhuk,hpskh, a k hq 
looooooooooomooooooooooon 
I1 
` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
V̂h,kpskhq ´ uk,hpskh, a k hq ´ PV̂k,h`1pskh, a 
k hq 
ı 
looooooooooooooooooooooooooooooooomooooooooooooooooooooooooooooooooon 
I2 
` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
PV̂k,h`1ps k h, a 
k hq ´ V̂h`1,kpskh`1q 
ı 
loooooooooooooooooooooooooomoooooooooooooooooooooooooon 
I3 
` 
K ÿ 
k“1 
` 
1 ´ Ikhk 
˘ 
V̂k,hk pskhk 
q 
looooooooooooomooooooooooooon 
I4 
, 
where hk is the smallest index such that Ikhk “ 0. Following the definition of uk,h, 
I1 “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh min 
" 
1, β › 
› 
› ϕ̃k,h,0 
› 
› 
› 9̃ Σ 
´1 
k,0 
* 
“ R̃0. 
By Lemma 2.8.24, 
I2 ď 4 K ÿ 
k“1 
H ÿ 
h“1 
Ikh min 
" 
1, β › 
› 
› ϕ̂k,h,0 
› 
› 
› 9̂ Σ 
´1 
k,0 
* 
“ 4R̂0 
By definitions, 
I3 “ Â0, 
I4 ď 
K ÿ 
k“1 
` 
1 ´ IkH ˘ 
“ G. 
Thus, 
K ÿ 
k“1 
V̂k,1ps k hq ď R̃0 ` 4R̂0 ` Â0 ` G (2.8.53) 
70
Substituting (2.8.49) in Lemma 2.8.26 into (2.8.47) in Lemma 2.8.25, we have 
R̂m ď 4dι ` 4βγ2dι ` 2β ? dι 
c 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
` 4R̂m ` 2R̂m`1 ` KHα2 
ď 2β ? dι 
c 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
` 4R̂m ` 2R̂m`1 
` 4dι ` 4βγ2dι ` 2β ? dι 
? G ` KHα2 
loooooooooooooooooooooomoooooooooooooooooooooon 
Ic 
, (2.8.54) 
where the second inequality holds due to ? a ` b ď 
? a ` 
? b. Substituting (2.8.49) in 
Lemma 2.8.26 into (2.8.51) in Lemma 2.8.27, we have 
ˇ 
ˇ 
ˇ Âm 
ˇ 
ˇ 
ˇ ď a 
2ζ 
c 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
` ζ 
ď a 
2ζ 
c 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
` a 
2ζG ` ζ (2.8.55) 
Substituting (2.8.50) in Lemma 2.8.26 into (2.8.48) in Lemma 2.8.25, we have 
R̃m ď 4dι ` 4βγ2dι ` 2β ? dι 
c 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
K ` 2R̃0 
¯ 
` 4R̃m ` 2R̃m`1 ` KHα2 
ď 2β ? dι 
c 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` 2m`1 
´ 
K ` 2R̃0 
¯ 
` 4R̃m ` 2R̃m`1 
` 4dι ` 4βγ2dι ` 2β ? dι 
? G ` KHα2 
loooooooooooooooooooooomoooooooooooooooooooooon 
Ic 
(2.8.56) 
Substituting (2.8.50) in Lemma 2.8.26 into (2.8.51) in Lemma 2.8.27, we have 
ˇ 
ˇ 
ˇ Ãm 
ˇ 
ˇ 
ˇ ď a 
2ζ 
c 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` G ` 2m`1 
´ 
K ` 2R̃0 
¯ 
` ζ 
ď a 
2ζ 
c 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` 2m`1 
´ 
K ` 2R̃0 
¯ 
` a 
2ζG ` ζ (2.8.57) 
Thus, calculating (2.8.56) + (2.8.57) + 4ˆ(2.8.54) + (2.8.55) and using ? a` 
? b` 
? c` 
? d ď 
71
2 ? a ` b ` c ` d, we have 
R̃m ` 
ˇ 
ˇ 
ˇ Ãm 
ˇ 
ˇ 
ˇ ` 4R̂m ` 
ˇ 
ˇ 
ˇ Âm 
ˇ 
ˇ 
ˇ 
ď 5Ic ` 2 a 
2ζG ` 2ζ ` 2max ! 
8β ? dι, 
a 
2ζ ) 
c 
2 ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ ` 2 ¨ 2m`1 
´ 
R̃0 ` 4R̂0 
¯ 
`4R̂m ` 2R̂m`1 ` 2 ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` 2 ¨ 2m`1 
´ 
K ` 2R̃0 
¯ 
` 4R̃m ` 2R̃m`1 
ď 5Ic ` `2 a 
2ζG ` 2ζ ` 4max ! 
8β ? dι, 
a 
2ζ ) 
c 
´ 
R̃m ` 
ˇ 
ˇ 
ˇ Ãm 
ˇ 
ˇ 
ˇ ` 4R̂m ` 
ˇ 
ˇ 
ˇ Âm 
ˇ 
ˇ 
ˇ 
¯ 
` 
´ 
R̃m`1 ` 
ˇ 
ˇ 
ˇ Ãm`1 
ˇ 
ˇ 
ˇ ` 4R̂m`1 ` 
ˇ 
ˇ 
ˇ Âm`1 
ˇ 
ˇ 
ˇ 
¯ 
` 2 ¨ 2m`1 ´ 
K ` R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ 
¯ 
. 
Then by Lemma 2.8.33 with am “ R̃m` 
ˇ 
ˇ 
ˇ Ãm 
ˇ 
ˇ 
ˇ `4R̂m` 
ˇ 
ˇ 
ˇ Âm 
ˇ 
ˇ 
ˇ ď 7KH and M “ logp7KHq{ log 2, 
R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ can be bounded as 
R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ 
ď 22 ¨ 16maxt64β2dι, 2ζu ` 30Ic ` 12 a 
ζG ` 12ζ 
` 32max ! 
8β ? dι, 
a 
2ζ ) 
c 
K ` R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ 
ď 352max ␣ 
64β2dι, 2ζ ( 
` 30Ic ` 12 a 
ζG ` 12ζ ` 32max ! 
8β ? dι, 
a 
2ζ )? 
K 
` 32max ! 
8β ? dι, 
a 
2ζ ) 
c 
R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ . (2.8.58) 
By the fact that x ď a ? x ` b ñ x ď 2a2 ` 2b, (2.8.58) implies that 
R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ 
ď 896max ␣ 
64β2dι, 2ζ ( 
` 60Ic ` 24 a 
ζG ` 24ζ ` 64max ! 
8β ? dι, 
a 
2ζ )? 
K. (2.8.59) 
72
Finally, plugging (2.8.59) into (2.8.53) and bounding G with Lemma 2.8.28, we have 
K ÿ 
k“1 
V̂k,1ps k hq 
ď R̃0 ` 
ˇ 
ˇ 
ˇ Ã0 
ˇ 
ˇ 
ˇ ` 4R̂0 ` 
ˇ 
ˇ 
ˇ Â0 
ˇ 
ˇ 
ˇ ` G 
ď 896max ␣ 
64β2dι, 2ζ ( 
` 24ζ ` 64max ! 
8β ? dι, 
a 
2ζ )? 
K (2.8.60) 
` 60 ´ 
4dι ` 4βγ2dι ` 2β ? dι 
? Mdι ` KHα2 
¯ 
` 24 a 
ζMdι ` Mdι 
ď 896max ␣ 
64β2dι, 2ζ ( 
` 24ζ ` 240dι ` 240βγ2dι ` 120βdι ? M ` 24 
a 
ζMdι ` Mdι 
` 
´ 
64max ! 
8β ? dι, 
a 
2ζ ) 
` 120β ? dιHα2 
¯? K 
2.8.8 Proof of Lemmas in Section 2.8.7 
2.8.8.1 Proof of Lemma 2.8.6 
Lemma 2.8.29 (Theorem 4.3, Zhou and Gu (2022a)). Let tGku 8 
k“1 be a filtration, and 
txk, ηkukě1 be a stochastic process such that xk P Rd is Gk-measurable and ηk P R is Gk`1-
measurable. Let L, σ, λ, ε ą 0,µ˚ P Rd. For k ě 1, let yk “ xµ˚,xky ` ηk and suppose that 
ηk,xk also satisfy 
E rηk | Gks “ 0,E “ 
η2k | Gk 
‰ 
ď σ2, |ηk| ď R, }xk}2 ď L (2.8.61) 
For k ě 1, let Zk “ λI ` řk 
i“1 xix J i ,bk “ 
řk i“1 yixi,µk “ Z´1 
k bk, and 
βk “12 a 
σ2d log p1 ` kL2{pdλqq log p32plogpR{εq ` 1qk2{δq ` 6 log ` 
32plogpR{εq ` 1qk2 {δ ˘ 
ε 
` 24 log ` 
32plogpR{εq ` 1qk2 {δ ˘ 
max 1ďiďk 
! 
|ηi|min ! 
1, }xi}Z´1 i´1 
)) 
. (2.8.62) 
Then, for any 0 ă δ ă 1, we have with probability at least 1 ´ δ that, 
@k ě 1, 
› 
› 
› 
› 
› 
k ÿ 
i“1 
xiηi 
› 
› 
› 
› 
› 
Z´1 k 
ď βk, }µk ´ µ˚ }Zk 
ď βk ` ? λ }µ˚ 
}2 
73
Lemma 2.8.30. Let Ṽk,h, V̂k,h, 9̃ Σk,m, 9̂ 
Σk,m, θ̃k,m, θ̂k,m, ϕ̃k,h,m, ϕ̂k,h,m be defined in Algo-
rithm 4, for any k P rKs, h P rHs, m P rM s. We have 
ˇ 
ˇ 
ˇ VV̂ 2m 
k,h`1 
` 
skh, a k h 
˘ 
´ V̂V̂ 2m 
k,h`1 
` 
skh, a k h 
˘ 
ˇ 
ˇ 
ˇ 
ď min 
" 
1, › 
› 
› ϕ̂k,h,m`1 
› 
› 
› 9̂ Σ 
´1 
k,m`1 
› 
› 
› θ̂k,m`1 ´ θ˚ 
› 
› 
› 9̂ Σk,m`1 
* 
` min 
" 
1, 2 › 
› 
› ϕ̂k,h,m 
› 
› 
› 9̂ Σ 
´1 
k,m 
› 
› 
› θ̂k,m ´ θ˚ 
› 
› 
› 9̂ Σk,m 
* 
, (2.8.63) 
and 
ˇ 
ˇ 
ˇ VṼ 2m 
k,h`1 
` 
skh, a k h 
˘ 
´ ṼṼ 2m 
k,h`1 
` 
skh, a k h 
˘ 
ˇ 
ˇ 
ˇ 
ď min 
" 
1, › 
› 
› ϕ̃k,h,m`1 
› 
› 
› 9̃ Σ 
´1 
k,m`1 
› 
› 
› θ̃k,m`1 ´ θ˚ 
› 
› 
› 9̃ Σk,m`1 
* 
` min 
" 
1, 2 › 
› 
› ϕ̃k,h,m 
› 
› 
› 9̃ Σ 
´1 
k,m 
› 
› 
› θ̃k,m ´ θ˚ 
› 
› 
› 9̃ Σk,m 
* 
. (2.8.64) 
Proof of Lemma 2.8.30. The proof follows the proof of Lemma C.1 in Zhou et al. (2021b). 
We first prove (2.8.63), and the proof of (2.8.64) is similar. We have 
|rV̂k,hV̂ 2m 
k,h`1sps k h, a 
k hq ´ rVk,hV̂k,h`1spskh, a 
k hq| 
“ |rxϕ̂k,h,m`1, θ̂k,m`1ysr0,1s ´ xϕ̂k,h,m`1,θ ˚ y 
` pxϕ̂k,h,m,θ ˚ yq 
2 ´ rxϕ̂k,h,m, θ̂k,mys 
2 r0,1s| 
ď |rxϕ̂k,h,m`1, θ̂k,m`1ysr0,1s ´ xϕ̂k,h,m`1,θ ˚ y| 
loooooooooooooooooooooooooomoooooooooooooooooooooooooon 
I1 
` |pxϕ̂k,h,m,θ ˚ yq 
2 ´ rxϕ̂k,h,m, θ̂k,mys 
2 r0,1s| 
looooooooooooooooooooooomooooooooooooooooooooooon 
I2 
(2.8.65) 
where the inequality holds due to triangle inequality. We have I1 ď 1 since both terms in I1 
74
lie in the interval r0, 1s. Furthermore, 
I1 ď |rxϕ̂k,h,m`1, θ̂k,m`1ys ´ xϕ̂k,h,m`1,θ ˚ y| 
“ |rxϕ̂k,h,m`1, θ̂k,m`1 ´ θ˚ y| 
ď }ϕk,h,m`1} 9̂ Σ 
´1 
k,m`1 
}θ̂k,m`1 ´ θ˚ } 9̂ Σk,m`1 
, 
where the first inequality holds due to xϕ̂k,h,m`1pskh, a k hq,θ˚y P r0, 1s, the second inequality 
holds due to Cauchy-Schwarz inequality. Thus, we obtain 
I1 ď mint1, }ϕk,h,m`1} 9̂ Σ 
´1 
k,m`1 
}θ̂k,m`1 ´ θ˚ } 9̂ Σk,m`1 
u (2.8.66) 
For I2, we have 
I2 “ 
ˇ 
ˇ 
ˇ pxϕ̂k,h,mpskh, a 
k hq,θ˚ 
yq ´ rxϕ̂k,h,m, θ̂k,mysr0,1s 
ˇ 
ˇ 
ˇ 
ˆ 
ˇ 
ˇ 
ˇ pxϕ̂k,h,mpskh, a 
k hq,θ˚ 
yq ` rxϕ̂k,h,m, θ̂k,mysr0,1s 
ˇ 
ˇ 
ˇ 
ď 2 ˇ 
ˇ 
ˇ pxϕ̂k,h,mpskh, a 
k hq,θ˚ 
yq ´ xϕ̂k,h,m, θ̂k,m, y 
ˇ 
ˇ 
ˇ 
ď 2}ϕk,h,mpskh, a k hq} 9̂ 
Σ ´1 
k,m 
}θ̂k,m ´ θ˚ } 9̂ Σk,m 
where the first inequality holds due to that both xϕ̂k,h,mpskh, a k hq,θ˚y and rxϕ̂k,h,m, θ̂k,mysr0,1s 
lie in the interval r0, 1s, and the second inequality holds due to Cauchy-Schwarz inequality. 
Since I2 belongs to the interval r0, 1s, we have 
I2 ď mint1, 2}ϕk,h,mpskh, a k hq} 9̂ 
Σ ´1 
k,m 
}θ̂k,m ´ θ˚ } 9̂ Σk,m 
u (2.8.67) 
Substituting (2.8.66) and (2.8.67) into (2.8.65), we obtain (2.8.63). The proof of 2.8.64 is 
nearly identical to the proof of (2.8.65). The only difference is to replace ϕ̂ with ϕ̃, θ̂ with 
θ̃, 9̂ Σ with 9̃ 
Σ. 
Proof of Lemma 2.8.6. The proof follows Lemma C.2 in Zhou and Gu (2022a). Symbols we 
used here may have small intuitively understandable modification compared to Algorithm 5 
75
since we have to distinguish between Algorithm 5 applied to Ṽk,h and V̂k,h. We first prove 
that Equation (2.8.9) holds with high probability. By definitions, 
σ̂2 k,h,m “ max 
" 
γ2 › 
› 
› ϕ̂k,h,m 
› 
› 
› 
Σ̂´1 k,h,m 
, ” 
V̂k,mV̂ 2m 
k,h`1 
ı 
pskh, a k hq ` Êk,h,m, α 
2 
* 
σ̂2 k,h,m “ max 
" 
γ2 › 
› 
› ϕ̂k,h,M´1 
› 
› 
› 
Σ̂´1 k,h,M´1 
, 1, α2 
* 
. 
We define Ck,m as 
Ĉk,m :“ tθ : }θ ´ θ̂k,m} 9̂ Σk,m 
ď βku. 
For each m, let 
xk,h,m “ σ̂´1 k,h,mϕ̂k,h,m, 
ηk,h,m “ σ̂´1 k,h,m 1tθ˚ 
P Ĉk,m X Ĉk,m`1urV̂ 2m 
k,h`1ps k h`1q ´ xϕ̂k,h,m,θ 
˚ ys, 
ηk,h,M´1 “ σ̂´1 k,h,M´1rV̂ 2M´1 
k,h`1 ´ xϕ̂k,h,M´1,θ ˚ ys, 
Gk,h “ Fk,h, 
µ˚ “ θ˚. 
We have 
Erηk,h,m|Gk,hs “ 0, }xk,h,m}2 ď σ̂´1 k,h,m ď 1{α, |ηk,h,m| ď 1{α 
Since 1tθ˚ P Ĉk,m X Ĉk,m`1u is Gk,h-measurable, then we can bound the variance for m P rM s 
76
as follows: 
Erη2k,h,m|Gk,hs “ σ̂´2 k,h,m 1tθ˚ 
P Ĉk,m X Ĉk,m`1urVV̂ 2m 
k,h`1sps k h, a 
k hq 
ď σ̂´2 k,h,m 1tθ˚ 
P Ĉk,m X Ĉk,m`1u 
« 
V̂V̂ 2m 
k,h`1 
` 
skh, a k h 
˘ 
` min 
" 
1, › 
› 
› ϕ̂k,h,m`1 
› 
› 
› 9̂ Σ 
´1 
k,m`1 
› 
› 
› θ̂k,m`1 ´ θ˚ 
› 
› 
› 9̂ Σk,m`1 
* 
` min 
" 
1, 2 › 
› 
› ϕ̂k,h,m 
› 
› 
› 9̂ Σ 
´1 
k,m 
› 
› 
› θ̂k,m ´ θ˚ 
› 
› 
› 9̂ Σk,m 
* 
ff 
ď σ̂´2 k,h,m 
« 
V̂V̂ 2m 
k,h`1 
` 
skh, a k h 
˘ 
` min 
" 
1, βk 
› 
› 
› ϕ̂k,h,m`1 
› 
› 
› 9̂ Σ 
´1 
k,m`1 
* 
` min 
" 
1, 2βk 
› 
› 
› ϕ̂k,h,m 
› 
› 
› 9̂ Σ 
´1 
k,m 
* 
ff 
ď 1, 
where the first inequality holds due to Lemma 2.8.30, the second inequality holds due to the 
definition of the indicator function, and the third inequality holds due to the definition of 
σ̂´2 k,h,m. For m “ M ´ 1, we have Erη2k,h,m|Gk,hs ď 1 directly by the definition of σ̂2 
k,h,m. For 
any m P rM s, we have 
|ηk,h,m|maxt1, }xk,h,m}Σ̂´1 k,h´1,m 
u ď σ̂´2 k,h,m}ϕ̂k,h,m}Σ̂´1 
k,h´1,m ď 1{γ2, 
where the first inequality follows from the definition of ηk,h,m and xk,h,m, and the second 
inequality follows from the definition of σ̂k,h,m. Let 
yk,h,m “ xµ˚,xx,h,my ` ηk,h,m, 
Zk,m “ λI ` 
k ÿ 
i“1 
H ÿ 
h“1 
xi,h,mx J i,h,m “ 
9̂ Σk`1,m, 
bk,m “ 
k ÿ 
i“1 
H ÿ 
h“1 
xi,h,myi,h,m, 
µk,m “ Z´1 k,mbk,m, 
ε “ 1{γ2. 
77
Then, by Lemma 2.8.29, for each m P rM s, with probability at least 1 ´ δ, @k P rK ` 1s, 
}µk´1,m ´ θ˚ } 9̂ Σk,m 
ď12 a 
d logp1 ` kH{pα2dλqq logp32plogpγ2{αq ` 1qk2H2{δq 
` 30 logp32plogpγ2 {αq ` 1qk2H2 
{δq{γ2 ` 
? λB 
“ βk (2.8.68) 
Define the event that (2.8.68) happens for all k and m as Ê . Conditioned on Ê , the following 
properties hold: 
‚ For k “ 1, m P rM s, by the definition of θ̂1,m and 9̂ Σ1,m, we have }θ˚ ´ θ̂1,m} 9̂ 
Σ1,m “ 
}θ˚}λI ď ? λB “ β1, which implies 
θ˚ P Ĉ1,m (2.8.69) 
‚ For k P rKs and m “ M ´ 1, we directly have µk,M´1 “ θ̂k`1,M´1, which implies 
θ˚ P Ĉk`1,M´1. (2.8.70) 
‚ For k P rKs and m P rM ´ 1s, we have 
θ˚ P Ĉk,m X Ĉk,m`1 ñ yk,h,m “ σ̂´1V̂ 2m 
k,h`1ps k h`1q ñ µk,m “ θ̂k`1,m ñ θ˚ 
P Ĉk`1,m. 
(2.8.71) 
Therefore, by induction based on initial conditions (2.8.69) and (2.8.70), induction rule 
(2.8.71), we have for k P rKs and m P rM s, θ˚ P Ĉk,m. Taking the union bound gives that 
(2.8.9) happens with probability at least 1 ´ Mδ. We can use the nearly identical argument 
to prove that (2.8.10) holds with probability at least 1´Mδ. The only difference is to replace 
σ̂ with σ̃, ϕ̂ with ϕ̃, V̂ with Ṽ, V̂ with Ṽ, Σ̂ with Σ̃, 9̂ Σ with 9̃ 
Σ, θ̂ with θ̃. By taking the 
union bound, we obtain that with probability at least 1 ´ 2Mδ, Equations (2.8.9) (2.8.10) 
both hold. For (2.8.11) and (2.8.12), we have 
}θk ´ θ˚ } 9̂ Σk,0 
ď 
› 
› 
› θk ´ θ̂k,m 
› 
› 
› 9̂ Σk,0 
` 
› 
› 
› θ̂k,m ´ θ˚ 
› 
› 
› 9̂ Σk,0 
ď 2βk, 
}θk ´ θ˚ } 9̃ Σk,0 
ď 
› 
› 
› θk ´ θ̃k,m 
› 
› 
› 9̃ Σk,0 
` 
› 
› 
› θ̃k,m ´ θ˚ 
› 
› 
› 9̃ Σk,0 
ď 2βk 
78
2.8.8.2 Proof of Lemma 2.8.22 
Proof of Lemma 2.8.22. We prove this inequality by induction. Suppose 
Vh`1psh`1;θK , π, rq´Vh`1psh`1;θ ˚, π, rq 
“ Etraj„pπ,Pq|trajh`1 Wh`1ptpPK ´ PqVh`1psh, ah;θK , π, rquq, (2.8.72) 
which is true for h “ H. Then, we have 
Vhpsh;θK , π, rq ´ Vhpsh;θ ˚, π, rq 
“ min ␣ 
1, rhpsh, ahq ` PKVh`1psh, ah;θK , π, rq ´ ` 
rhpsh, ahq ` PVh`1psh, ah;θ ˚, π, rq 
˘( 
“ min ␣ 
1,PKVh`1psh, ah;θK , π, rq ´ PVh`1psh, ah;θ ˚, π, rq 
( 
“ mint1, pPK ´ PqVh`1psh, ah;θK , π, rq ` PpVh`1psh, ah;θK , π, rq ´ Vh`1psh, ah;θ ˚, π, rqqu 
“ mint1, pPK ´ PqVh`1psh, ah;θK , π, rq 
` Esh`1„Pp¨|sh,ahqEtraj„pπ,Pq|trajh`1 Wh`1ptpPK ´ PqVh`1psh;θK , π, rququ 
“ Etraj„pπ,Pq|trajh mint1, pPK ´ PqVh`1psh, ah;θK , π, rq 
` Wh`1ptpPk ´ PqVh`1psh, ah;θK , π, rququ 
“ Etraj„pπ,Pq|trajhWhptpPk ´ PqVh`1psh, ah;θK , π, rquq. 
The first equality holds due to that Vhpsh;θK , π, rq and Vhpsh;θ ˚, π, rq both belong to 
r0, 1s, the third equality holds due to (2.8.72), and the forth equality holds due to that 
Etraj„pπ,Pq|trajh “ Esh`1„Pp¨|sh,ahqEtraj„pπ,Pq|trajh`1 . Thus, by induction, we obtain the desired 
result (2.8.34). 
2.8.8.3 Proof of Lemma 2.8.23 
Proof of Lemma 2.8.23. We first prove (2.8.73) by induction. 
Etraj„pπ,Pq|traj1W1 ptuK,hpsh, πpshq;θK , π, rquq ď V̂K,1 ps1;θK , π, rq . (2.8.73) 
79
Suppose 
Etraj„pπ,Pq|trajh`1 Wh`1ptuK,hpsh, πpshq;θK , π, rquq ď V̂K,h`1ps1;θK , π, rq, (2.8.74) 
which is true for h “ H. Then, 
V̂K,hpsh;θK , π, rq ´ Etraj„pπ,Pq|trajhWhptuK,hpsh, πpahq;θK , π, rquq 
ě min 
" 
0, uK,hpsh, πpshq;θK , π, rq ` 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
`ϕJ 
V̂K,h`1p¨;θK ,π,rq psh, πpshqqθK ´ Etraj„pπ,Pq|trajhWhptuK,hpsh, πpshq;θK , π, rqqu 
) 
ě min 
" 
0, uK,hpsh, πpshq;θK , π, rq ` 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
` ϕJ 
V̂K,h`1p¨;θK ,π,rq psh, πpshqqθK ´ uK,hpsh, πpshq;θK , π, rq 
´ Esh`1„Pp¨|sh,πpshqqEtraj„pπ,Pq|trajh`1 Wh`1ptuK,hpsh, πpshq;θK , π, rqq 
* 
ě min 
" 
0, 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
` ϕJ 
V̂K,h`1p¨;θK ,π,rq psh, πpshqqθK 
´Esh`1„Pp¨|sh,πpshqqV̂K,h`1psh`1;θK , π, rq 
) 
ě min 
" 
0, 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
` ϕJ 
V̂K,h`1p¨;θK ,π,rq psh, πpshqqpθK ´ θ˚ 
q 
* 
ě min 
" 
0, 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
´ 2β › 
› 
› ϕV̂K,h`1p¨;θK ,π,rq 
psh, πpshqq 
› 
› 
› 9̂ ΣK,0 
* 
ě 0, 
where the first inequality holds due to the definition of V̂K,h, the second inequality holds 
due to the definition of Whp¨q and Etraj„pπ,Pq|trajh “ Esh`1„Pp¨|sh,πpshqqEtraj„pπ,Pq|trajh`1 , the 
third inequality holds due to 2.8.74, the fifth inequality holds due to Lemma 2.8.6. Thus, by 
induction, 2.8.73 holds. Thanks to the optimism of V̂K,1ps1;θK , πK , rKq, we have 
V̂K,1ps1;θK , π, rq ď V̂K,1ps1;θK , πK , rKq, 
which concludes the proof. 
80
2.8.8.4 Proof of Lemma 2.8.24 
Proof of Lemma 2.8.24. For the equation (2.8.37), we have 
V̂k,hpskhq ´ uk,hpskh, a k hq ´ PV̂k,h`1pskh, a 
k hq 
ď min 
" 
1, 2β › 
› 
› ϕ̂k,h,0ps 
k h, a 
k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
` ϕ̂J k,h,0pskh, a 
k hqθk ´ ϕ̂J 
k,h,0ps k h, a 
k hqθ 
* 
“ min 
" 
1, 2β › 
› 
› ϕ̂k,h,0pskh, a 
k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
` ϕ̂J k,h,0pskh, a 
k hqpθk ´ θq 
* 
ď min 
" 
1, 2β › 
› 
› ϕ̂k,h,0pskh, a 
k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
` 
› 
› 
› ϕ̂J 
k,h,0pskh, a k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
}θk ´ θ} 9̂ Σk,0 
* 
ď min 
" 
1, 4β › 
› 
› ϕ̂k,h,0pskh, a 
k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
* 
ď 4min 
" 
1, β › 
› 
› ϕ̂k,h,0ps 
k h, a 
k hq 
› 
› 
› 9̂ Σ 
´1 
k,0 
* 
where the first inequality holds due to that each term lies in the interval r0, 1s, the second 
inequality holds due to Cauchy-Schwartz inequality, and the third inequality holds due to 
lemma 2.8.6. For the equation (2.8.38), we have 
Ṽk,hpskhq ´ rk,hpskh, a k hq ´ PṼk,h`1ps 
k h, a 
k hq 
ď min ! 
1, ϕ̃J k,h,0pskh, a 
k hqθk ´ ϕ̃J 
k,h,0ps k h, a 
k hqθ 
) 
“ min ! 
1, ϕ̃J k,h,0pskh, a 
k hqpθk ´ θq 
) 
ď min 
" 
1, › 
› 
› ϕ̃J 
k,h,0pskh, a k hq 
› 
› 
› 9̃ Σ 
´1 
k,0 
}θk ´ θ} 9̃ Σk,0 
* 
ď min 
" 
1, 2β › 
› 
› ϕ̃J 
k,h,0ps k h, a 
k hq 
› 
› 
› 9̃ Σ 
´1 
k,0 
* 
ď 2min 
" 
1, β › 
› 
› ϕ̃J 
k,h,0ps k h, a 
k hq 
› 
› 
› 9̃ Σ 
´1 
k,0 
* 
, 
where the first inequality holds due to that each term lies in the interval r0, 1s, the second 
inequality holds due to the Cauchy-Schwartz inequality, and the third inequality holds due 
to Lemma 2.8.6. 
81
2.8.8.5 Proof of Lemma 2.8.25 
Lemma 2.8.31 (Lemma B.1, Zhou and Gu (2022a)). Let tσk, βkukě1 be a sequence of non-
negative numbers, α, γ ą 0, txkukě1 Ă Rd and }xk}2 ď L. Let tZkukě1 and tσ̄kukě1 be 
recursively defined as follows: Z1 “ λI 
@k ě 1, σ̄k “ max ! 
σk, α, γ }xk} 1{2 
z´1 k 
) 
,Zk`1 “ Zk ` xkx J k {σ̄2 
k. 
Let ι “ log p1 ` KL2{ pdλα2qq. Then we have 
K ÿ 
k“1 
min ! 
1, βk }xk}Z´1 k 
) 
ď 2dι ` 2 max kPrKs 
βkγ 2dι ` 2 
? dι 
g 
f 
f 
e 
K ÿ 
k“1 
β2 k pσ2 
k ` α2q. 
Proof of Lemma 2.8.25. The proof is nearly identical to the proof of Lemma C.5 in Zhou 
and Gu (2022a). The only difference is to replace Σ̂k,m with 9̂ Σk,m (or 9̃ 
Σk,m), Σ̃k,h,m with 
Σ̂k,h,m (or still Σ̃k,h,m), ϕk,h,m with ϕ̂k,h,m (or ϕ̃k,h,m). 
2.8.8.6 Proof of Lemma 2.8.26 
Proof of Lemma 2.8.26. The proof follows the proof of Lemma 25 in Zhang et al. (2021d) 
and Lemma C.6 in Zhou and Gu (2022a). We have, 
Ŝm “ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
” 
PV̂ 2m`1 
k,h`1 
ı 
` 
skh, a k h 
˘ 
´ 
´” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
“ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
”” 
PV̂ 2m`1 
k,h`1 
ı 
` 
skh, a k h 
˘ 
´ V̂ 2m`1 
k,h`1 
` 
skh`1 
˘ 
ı 
` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
V̂ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
´ 
V̂ 2m`1 
k,h`1 
` 
skh`1 
˘ 
´ V̂ 2m`1 
k,h 
` 
skh ˘ 
¯ 
ďÂm`1 ` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
V̂ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
` 
K ÿ 
k“1 
Ikhk V̂ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
, 
(2.8.75) 
82
where hk is the largest index satisfying Ikh “ 1. For the second term, we have 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
V̂ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
V̂ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PV̂k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2m`1 ȷ 
“ 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
´ 
V̂k,h 
` 
skh ˘ 
´ 
” 
PV̂k,h`1 
ı 
` 
skh, a k h 
˘ 
¯ 
m ź 
i“0 
´ 
V̂ 2i 
k,h 
` 
skh ˘ 
` 
” 
PV̂k,h`1 
ı 
` 
skh, a k h 
˘2i ¯ 
ď 2m`1 K ÿ 
k“1 
H ÿ 
h“1 
Ikh max ! 
V̂k,h 
` 
skh ˘ 
´ 
” 
PV̂k,h`1 
ı 
` 
skh, a k h 
˘ 
, 0 ) 
ď 2m`1 K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
uk,h 
` 
skh, a k h 
˘ 
` 4min 
" 
1, β › 
› 
› ϕ̂k,h,0 
› 
› 
› 9̂ Σ 
´1 
k,0 
*ȷ 
ď 2m`1 ´ 
R̃0 ` 4R̂0 
¯ 
, (2.8.76) 
where the first inequality holds due to using EX2 ě pEXq2 recursively, the first equality 
holds due to the fact x2m`1 ´ y2 
m`1 “ px ´ yq 
śm i“0px 
2m ´ y2 m 
q, the second inequality holds 
due to V̂k,h belongs to the interval r0, 1s, the third inequality holds due to Lemma 2.8.24, and 
the last inequality holds due to uk,hpskh, a k hq “ β}ϕVh`1p¨;θk,πk,rkqps 
k h, a 
k hq} 9̃ 
Σk,0 “ β}ϕ̃k,h,0} 9̃ 
Σk,0 . 
If hK ď H, we have Ikhk V̂ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
ď 1 “ 1 ´ IkH , and if hK “ H, Ikhk V̂ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
“ 
0 “ 1 ´ IkH , which both give 
K ÿ 
k“1 
Ikhk V̂ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
ď 
K ÿ 
k“1 
p1 ´ IkHq “ G (2.8.77) 
Substituting Equations (2.8.75), (2.8.76),(2.8.77) into (2.8.75), we can get (2.8.49). For 
Equation (2.8.44), similarly, we have 
S̃m ď Ãm`1 ` 
K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
Ṽ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PṼ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
` 
K ÿ 
k“1 
Ikhk Ṽ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
, 
(2.8.78) K ÿ 
k“1 
Ikhk Ṽ 2m`1 
k,hk`1 
` 
skhk`1 
˘ 
ď 
K ÿ 
k“1 
` 
1 ´ IkH ˘ 
“ G. (2.8.79) 
83
And we have K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
V̂ 2m`1 
k,h 
` 
skh ˘ 
´ 
´” 
PV̂ 2m 
k,h`1 
ı 
` 
skh, a k h 
˘ 
¯2 ȷ 
ď 2m`1 K ÿ 
k“1 
H ÿ 
h“1 
Ikh max ! 
Ṽk,h 
` 
skh ˘ 
´ 
” 
PṼk,h`1 
ı 
` 
skh, a k h 
˘ 
, 0 ) 
ď 2m`1 K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
„ 
rk,hpskh, s k hq ` min 
" 
1, 2β › 
› 
› ϕ̃k,h,0 
› 
› 
› 9̃ Σ 
´1 
k,0 
*ȷ 
ď 2m`1 ´ 
K ` 2R̃0 
¯ 
(2.8.80) 
where the first inequality holds similar to the derivation of (2.8.76), second inequality fol-
lows Lemma 2.8.24, and the third inequality holds due to řH 
h“1 rk,hpskh, a k hq ď 1. Plugging 
Equations (2.8.79) (2.8.80) into 2.8.78, we obtain 2.8.50 
2.8.8.7 Proof of Lemma 2.8.27 
Proof of Lemma 2.8.27. The proof follows the proof of Lemma 25 in Zhang et al. (2021d) 
and Lemma C.7 in Zhou and Gu (2022a). We use Lemma 2.8.32 for Âm and Ãm for each m. 
To avoid confusion, we write ϵ, δ in Lemma 2.8.32 as ϵ1, δ1. 
Let xk,h “ Ikh 
”” 
PV̂ 2m 
k,h`1 
ı 
pskh, a k hq ´ V̂ 2m 
k,h`1ps k h`1q 
ı 
, n “ KH, ϵ1 “ a 
logp1{δ1q, and δ1 “ 
δ{p4 logpKHqq. Thus, E rx̂k,h|Fk,hs “ 0 and E “ 
x̂2 k,h 
ˇ 
ˇFk,h 
‰ 
“ Ikh “ 
VV 2m 
k,h`1 
‰ 
pskh, a k hq. Therefore, 
for each m P rM s, with probability at least 1 ´ δ, we have 
|Âm| “ 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
K ÿ 
k“1 
H ÿ 
h“1 
xk,h 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď 
g 
f 
f 
e2ζ K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
VV̂ 2m k,h`1 
ı 
pskh, a k hq ` ζ. 
Similarly, let xk,h “ Ikh 
”” 
PṼ 2m 
k,h`1 
ı 
pskh, a k hq ´ Ṽ 2m 
k,h`1ps k h`1q 
ı 
, n “ KH, ϵ1 “ a 
logp1{δ1q, and 
δ1 “ δ{p4 logpKHqq. With probability at least 1 ´ δ, we have 
|Ãm| “ 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
K ÿ 
k“1 
H ÿ 
h“1 
xk,h 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď 
g 
f 
f 
e2ζ K ÿ 
k“1 
H ÿ 
h“1 
Ikh 
” 
VṼ 2m k,h`1 
ı 
pskh, a k hq ` ζ. 
Taking union bound over m P rM s completes the proof. 
84
2.8.8.8 Proof of Lemma 2.8.28 
Proof of Lemma 2.8.28. By the fact that det 
ˆ 
9̂ Σ 
´1{2 
k`1,m 
˙ 
ă det ´ 
Σ̂ ´1{2 k,H,m 
¯ 
and det 
ˆ 
9̃ Σ 
´1{2 
k`1,m 
˙ 
ă det ´ 
Σ̃ ´1{2 k,H,m 
¯ 
, we have 
p1 ´ IkHq “ 1 ô Dm P rM s, det 
ˆ 
9̂ Σ 
´1{2 
k,m 
˙ 
{ det ´ 
Σ̂ ´1{2 k,H,m 
¯ 
ą 4 
or det 
ˆ 
9̃ Σ 
´1{2 
k,m 
˙ 
{ det ´ 
Σ̃ ´1{2 k,H,m 
¯ 
ą 4 
ñ Dm P rM s, det 
ˆ 
9̂ Σ 
´1{2 
k,m 
˙ 
{ det 
ˆ 
9̂ Σ 
´1{2 
k`1,m 
˙ 
ą 4 
or det 
ˆ 
9̃ Σ 
´1{2 
k,m 
˙ 
{ det 
ˆ 
9̃ Σ 
´1{2 
k`1,m 
˙ 
ą 4 (2.8.81) 
Let D̂m and D̃m denote the indices k such that 
D̂m :“ ! 
k P rKs : det ´ 
9̂ Σk`1,m 
¯ 
{ det ´ 
9̂ Σk,m 
¯ 
ą 16 ) 
D̃m :“ ! 
k P rKs : det ´ 
9̃ Σk`1,m 
¯ 
{ det ´ 
9̃ Σk,m 
¯ 
ą 16 ) 
Then we have 
G ď 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
M´1 ď 
m“0 
D̂m Y 
M´1 ď 
m“0 
D̃m 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď 
M´1 ÿ 
m“0 
ˇ 
ˇ 
ˇ D̂m 
ˇ 
ˇ 
ˇ ` 
M´1 ÿ 
m“0 
|D̃m| 
For each m, we have 
2 ˇ 
ˇ 
ˇ D̂m 
ˇ 
ˇ 
ˇ ă 
ÿ 
kPD̂m 
log 16 ă ÿ 
kPD̂m 
log ´ 
det ´ 
9̂ Σk`1,m 
¯ 
{ det ´ 
9̂ Σk,m 
¯¯ 
ď 
K ÿ 
k“1 
log ´ 
det ´ 
9̂ Σk`1,m 
¯ 
{ det ´ 
9̂ Σk,m 
¯¯ 
Furthermore, since det ´ 
9̂ ΣK`1,m 
¯ 
ď 
´ 
tr ´ 
9̂ ΣK`1,m 
¯ 
{d ¯d 
and tr ´ 
9̂ ΣK`1,m 
¯ 
ď tr pλIq ` 
ř 
k,h 
› 
› 
› ϕ̂k,h.m 
› 
› 
› 
2 
2 {σ̂2 
k,h,m ď dλ ` KH{α2 
K ÿ 
k“1 
log ´ 
det ´ 
9̂ Σk`1,m 
¯ 
{ det ´ 
9̂ Σk,m 
¯¯ 
“ log ´ 
det ´ 
9̂ ΣK`1,m 
¯ 
{ det ´ 
9̂ Σ1,m 
¯¯ 
ď d ` 
log ` 
λ ` KH{pdα2 q ˘ 
´ logpλq ˘ 
85
Therefore |D̂m| is upper bounded by 
|D̂m| ă d{2 logp1 ` KH{pdλα2 qq. 
And same for |D̃m|. Taking summation gives the upper bound of G. 
2.8.9 Auxiliary Lemmas 
Lemma 2.8.32 (Lemma 11, Zhang et al. 2021e). Let M ą 0 be a constant. Let txiu n i“1 be a 
stochastic process, Gi “ σ px1, . . . , xiq be the σ-algebra of x1, . . . , xi. Suppose E rxi | Gi´1s “ 
0, |xi| ď M and E rx2 i | Gi´1s ă 8 almost surely. Then, for any δ, ε ą 0, we have 
P 
˜ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
n ÿ 
i“1 
xi 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď 2 
d 
2 logp1{δq 
n ÿ 
i“1 
E rx2 i | Gi´1s ` 2 
a 
logp1{δqε ` 2M logp1{δq 
¸ 
ą 1 ´ 2 ` 
log ` 
M2n{ε2 ˘ 
` 1 ˘ 
δ. (2.8.82) 
Lemma 2.8.33 (Lemma 12, Zhang et al. (2021d)). Let λ1, λ2, λ4 ą 0, λ3 ě 1 and κ “ 
max tlog2 λ1, 1u. Let a1, . . . , aκ be non-negative real numbers such that 
ai ď min ! 
λ1, λ2 
a 
ai ` ai`1 ` 2i`1λ3 ` λ4 
) 
for any 1 ď i ď κ. Let aκ`1 “ λ1. Then we have a1 ď 22λ2 2 ` 6λ4 ` 4λ2 
? 2λ3. 
86
CHAPTER 3 
Uncertainty-Aware Unsupervised Exploration in Deep 
Reinforcement Learning 
3.1 Introduction 
In Chapter 2, we discussed the theoretical framework of reward-free exploration, especially 
with linear function approximation. In this chapter, we aim to extend this analysis and 
algorithm in a more general and practical setting, which is aligned with the current prac-
tice of deep reinforcement learning. We also seek to build the foundation of unsupervised 
reinforcement learning through the lens of reward-free exploration. 
Deep reinforcement learning (RL) has been the source of many breakthroughs in games 
(e.g., Atari game (Mnih et al., 2013) and Go game (Silver et al., 2016)) and robotic control 
(Levine et al., 2016) over the last ten years. A key component of RL is exploration, which 
requires the agent to explore different states and actions before finding a near-optimal policy. 
Traditional exploration strategy involves iteratively executing a policy guided by a specific 
reward function, limiting the trained agent to solving only the single task for which it was 
trained. Designing an efficient exploration strategy agnostic to reward functions is crucial, 
as it prevents the agent from repeated learning under different reward functions, thereby 
avoiding inefficiency and potential intractability in sample complexity. 
Therefore, as discussed in Chapter 2, reward-free exploration (Jin et al., 2020a) is pro-
posed to improve the efficiency of exploration without reward functions. A series of theo-
retical works have presented efficient exploration strategies with performance guarantees, as 
87
Agent Environment 
Action a 
Observation  s 
Dataset 𝒟 = {s, a, s′ } 
𝒟3 = {s, a, s′ , r3} 
𝒟1 = {s, a, s′ , r1} 
𝒟2 = {s, a, s′ , r2} 
Online pre-training with intrinsic reward Offline RL / Online Finetuning 
Neural Networks 
Intrinsic reward rint 
Training process 
Figure 3.1: Diagram of the unsupervised reinforcement learning paradigm. 
we discussed in Chapter 2. On the other hand, from the empirical perspective, unsupervised 
reinforcement learning (Laskin et al., 2021) has emerged as a new paradigm for encouraging 
the agent to explore without predefined supervision. Unsupervised RL diverges from classical 
RL approaches by not relying on a specific reward function for exploration. Instead, Unsu-
pervised RL utilizes an “intrinsic reward”, a.k.a., pseudo-reward function, defined based on 
all previously explored samples. This encourages the agent to venture into unexplored states 
and actions. In particular, in the realm of deep RL where no linear structural assumptions 
are made, recent studies (Pathak et al., 2017; Burda et al., 2018b; Eysenbach et al., 2018; 
Lee et al., 2019; Pathak et al., 2019; Liu and Abbeel, 2021a,b) have developed unsupervised 
RL algorithms by employing various intrinsic reward functions, demonstrating promising 
performance in finding the near-optimal policy. As presented in Figure 3.1, unsupervised 
reinforcement learning is similar with the reward-free exploration discussed in Chapter 2. 
Compared with the reward-free RL, empirical unsupervised reinforcement learning uses the 
intrinsic reward to motivate exploration and the additional application of online fine-tuning 
to learn the different rewards or objectives. 
88
Despite the success of these heuristics on designing the intrinsic rewards for unsupervised 
RL, these empirical results lack rigorous justification and could be further optimized. From 
the theoretical analysis perspective, for example, Kong et al. (2021) defined an intrinsic re-
ward based on the maximum difference between function pairs that show similarity in past 
data. This approach essentially treats each collected sample equally. It is a well-established 
principle in RL that in order to achieve optimal sample efficiency, different samples should 
be treated distinctively based on their importance. Notably, Zhang et al. (2023a) utilized 
variance-dependent weights to address the heteroscedasticity observed in samples, thereby 
achieving optimal sample complexity in linear mixture MDPs. However, this approach cal-
culates its intrinsic reward by nested iterative optimization, which hampers computational 
efficiency and practical applicability. Therefore, for the unsupervised reinforcement learning 
tasks, we are faced with the following question: 
Is it possible to craft an intrinsic reward function to explore the environment without 
supervision? 
3.1.1 Organization of this Chapter 
In this chapter, we will answer the above question affirmatively from both a theoretical 
perspective and an empirical perspective. This chapter is organized as follows. We first 
present the related works in Section 3.2 and preliminaries in Section 3.3. In in Section 3.4, 
we propose a variance-adaptive intrinsic reward for unsupervised reinforcement learning. In 
Section 3.5, we show that our method enjoys a finite sample complexity in finding the near-
optimal policy for any given reward, and our theoretical guarantee is tighter than that of 
existing methods. In Section 3.6, we conduct experiments and show that by incorporating 
variance information, a series of existing baselines can be further improved in terms of sample 
efficiency. The conclusion is drawn in Section 3.7 and we defer detailed proof of the algorithm 
to Section 3.8. 
89
3.2 Related Works 
3.2.1 Unsupervised Reinforcement Learning 
With recent advances in unsupervised CV and NLP tasks, unsupervised reinforcement learn-
ing has emerged as a new paradigm trying to learn the environment without supervision, 
such as the reward signals. As suggested in Laskin et al. (2021), these works are mainly sepa-
rated into two lines: unsupervised representation learning in RL and unsupervised behavioral 
learning. 
Unsupervised representation learning in RL mainly addresses issues on how to learn good 
representations for different states s, which can facilitate efficient learning of a policy πpa|sq. 
From the theoretical side, a list of works have identified how to select or learn good repre-
sentations for various RL tasks with linear function approximations, by using MLE (Uehara 
et al., 2021), contrastive learning (Qiu et al., 2022) or model selection (Papini et al., 2021a; 
Zhang et al., 2021a). From the empirical side, various methods in unsupervised learning 
or self-supervised learning are applied to RL tasks, including contrastive learning (Laskin 
et al., 2020; Stooke et al., 2021; Yarats et al., 2021a), autoencoders (Yarats et al., 2021b) 
and world models (Hafner et al., 2019a,b). 
Unsupervised behavioral learning in RL aims to eliminate this reward signal during explo-
ration. Therefore, the agent can be adapted to different tasks in the downstream fine-tuning. 
To replace the ‘extrinsic’ reward signals, these methods usually leverage different ‘intrinsic 
rewards’ during exploration. Many recent algorithms have been proposed to learn from dif-
ferent types of intrinsic reward, which is based on the prediction error (Pathak et al., 2017; 
Burda et al., 2018a; Pathak et al., 2019), information gain (Eysenbach et al., 2018; Hansen 
et al., 2019; Sharma et al., 2019) and entropy (Liu and Abbeel, 2021a,b; Seo et al., 2021) 
of the observations. URLB (Laskin et al., 2021) provided a unified framework providing 
benchmarks for all these intrinsic rewards. 
90
3.2.2 Reinforcement Learning with General Function Approximation 
RL with general function approximation has been widely studied in recent years, due to its 
ability to describe a wide range of existing RL algorithms. To explore the theoretical limits 
of RL and understand the practical DRL algorithms, various statistical complexity measure-
ments for general function approximation have been proposed and developed. For instance, 
Bellman rank (Jiang et al., 2017), Witness rank (Sun et al., 2019), eluder dimension (Russo 
and Van Roy, 2013), Bellman eluder dimension (Jin et al., 2021), Decision-Estimation Coeffi-
cient (DEC) (Foster et al., 2021), Admissible Bellman Characterization (Chen et al., 2022c), 
generalized eluder dimension (Agarwal et al., 2022), etc. Among different statistical com-
plexity measurements, Foster et al. (2021) showed a DEC-based lower bound of regret which 
holds for any function class. Specifically, our algorithm falls into the category of generalized 
eluder dimension function class, which includes linear MDPs (Jin et al., 2020b) as its special 
realization. 
3.3 Preliminaries 
3.3.1 Time-Inhomogeneous Episodic MDPs 
We model the sequential decision making problem via time-inhomogeneous episodic Markov 
decision processes (MDPs), which can be denoted as tuple M “ pS,A, H,P “ tPhuHh“1, r “ 
trhuHh“1q by convention. Here, S and A are state and action spaces, H is the length of each 
episode, Ph : S ˆ A ˆ S Ñ r0, 1s is the transition probability function at stage h for state s 
to transit to state s1 after executing action a, and rh : S ˆ A Ñ r0, 1s is the deterministic 
reward function at stage h. For any policy π “ tπhuHh“1, reward r “ trhuHh“1, and stage 
h P rHs, the value function V π h ps; rq and the state-action value function Qπ 
hps, a; rq is defined 
91
as: 
Qπ hps, a; rq “ E 
„ H ÿ 
h1“h 
rh1 
` 
sh1 , ah1 
˘ 
ˇ 
ˇ 
ˇ 
ˇ 
sh “ s, ah “ a, sh1`1 „ Ph1p¨|sh1 , ah1q, ah1`1 “ πpsh1`1q 
ȷ 
, 
V π h ps; rq “ Qπ 
hps, πhpsq; rq. 
Furthermore, the optimal value function V ˚ h ps; rq is defines as maxπ V 
π h ps; rq, and the optimal 
action-value function Q˚ hps, a; rq is defined as maxπ Q 
π hps, a; rq. For simplicity, we utilize the 
following bounded total reward assumption: 
Assumption 3.3.1. The total reward for every possible trajectory is assumed to be within 
the interval of p0, 1q. 
Up to rescaling, Assumption 3.3.1 is more general than the standard reward scale as-
sumption where rh P r0, 1s for all h P rHs. Assumption 3.3.1 also ensures that the value 
function V π h psq and action-value function Qπ 
hps, a; rq belong to the interval r0, 1s. 
For any function V : S Ñ R and stage h P rHs, the first-order Bellman operator Th is 
defined as: 
ThV ps, a; rq “ Es1„Pp¨|s,aq 
” 
rhps, aq ` V ps1; rq 
ı 
. 
For simplicity, we further define the shorthand: 
rPhV sps, a; rq “ Es1„Php¨|s,aqV ps1; rq, rVhV sps, a; rq “ rPhV 2 sps, a; rq ´ rPhV s 
2 ps, a; rq. 
Throughout the paper, if the reward r is clear in the context, we omit the notation r in Q 
and V for simplicity. 
3.3.2 General Function Approximation 
In this work, we focus on the model-free value-based RL methods, which require us to use a 
predefined function class to estimate the optimal value function Q˚ hps, a; rq for any reward r. 
We use F :“ tFhuHh“1 to denote the function class we will use during all H stages. To build 
92
the statistical complexity of using F to learn Q˚ hps, a; rq, we require several assumptions and 
definitions that characterize the cardinality of the function class. 
Assumption 3.3.2 (Completeness, Zhao et al. (2023)). Given F :“ tFhuHh“1 which is com-
posed of bounded functions fh : S ˆ A Ñ r0, Ls. We assume that for any h and function 
V : S Ñ r0, 1s and r : S ˆA Ñ r0, 1s, there exist f1, f2 P Fh such that for any ps, aq P S ˆA, 
f1ps, aq “ Es1„Php¨|s,aq 
“ 
rps, aq ` V ps1 q ‰ 
, f2ps, aq “ Es1„Php¨|s,aq 
” 
` 
rps, aq ` V ps1 q ˘2 ı 
. 
We assume that L “ Op1q throughout the paper. 
Definition 3.3.3 (Generalized eluder dimension, Agarwal et al. 2022). Let λ ě 0 and 
h P rHs, a sequence of state-action pairs Zh “ tzi,h “ psih, a i hquiPrKs and a sequence of positive 
numbers σh “ tσi,huiPrKs. The generalized eluder dimension of a function class Fh : S ˆA Ñ 
r0, Ls with respect to λ is defined by dimα,KpFhq :“ supZh,σh:|Zh|“K,σhěα dimpFh, Zh,σhq 
dimpFh, Zh,σhq :“ K ÿ 
i“1 
min 
ˆ 
1, 1 
σ2 i 
D2 Fh 
pzi,h; zri´1s,h, σri´1s,hq 
˙ 
, 
D2 Fh 
pz; zri´1s,h, σri´1s,hq :“ sup f1,f2PFh 
pf1pzq ´ f2pzqq2 ř 
sPri´1s 1 
σ2 s,h 
pf1pzs,hq ´ f2pzs,hqq2 ` λ . 
We write dimα,KpFq :“ H´1 ¨ ř 
hPrHs dimα,KpFhq for short when F is a collection of function 
classes F “ tFhuHh“1 in the context. 
Remark 3.3.4. Kong et al. (2021) introduced a similar definition called “sensitivity". In 
particular, it is defined by 
sensitivityZ,Fpzq :“ sup f1,f2PF 
pf1pzq ´ f2pzqq2 
mint ř 
ps,aqPZpf1ps, aq ´ f2ps, aqq2, λu , 
where λ is defined by T pH ` 1q2 for the RL task with rhps, aq P r0, 1s 1. The major differ-
ence between the generalized eluder dimension and sensitivity is that the generalized eluder 
dimension incorporates the variance σ2 s into the historical observation Z to craft the hetero-
geneous variance in Z. 
1We ignore the clipping process making sensitivityZ,F pzq Ð mintsensitivityZ,F pzqu for the clarity of demonstration 
93
Since D2 Fh 
in Definition 3.3.3 is not computationally efficient in some circumstances, we 
approximate it via an oracle D 2 
Fh , which is formally defined in Definition 3.3.5. 
Definition 3.3.5 (Bonus oracle D 2 
Fh ). The bonus oracle returns a computable function 
D 2 
Fh pz; zrts,h, σrts,hq, which computes the estimated uncertainty of a state-action pair z “ 
ps, aq P S ˆ A with respect to historical data zrts,h and corresponding weights σrts,h. It 
satisfies 
DFh pz; zrts,h, σrts,hq ď DFh 
pz; zrts,h, σrts,hq ď C ¨ DFh pz; zrts,h, σrts,hq, 
where C is a fixed constant. 
The covering numbers of the value function class and the bonus function class are intro-
duced in the following definition. 
Definition 3.3.6 (Covering numbers of function classes). For any ϵ ą 0, we define the 
following covering numbers of involved function classes: 
1. For each h P rHs, there exists an ϵ-cover CpFh, ϵq Ď Fh with size |CpFh, ϵq| ď NFh pϵq, 
such that for any f P Fh, there exists f 1 P CpFh, ϵq satisfying }f ´ f 1}8 ď ϵ. For 
any ϵ ą 0, we define the uniform covering number of F with respect to ϵ as NFpϵq :“ 
maxhPrHs NFh pϵq. 
2. There exists a bonus function class B “ tB : S ˆ A Ñ Ru such that for any t ě 0, 
zrts P pS ˆ Aqt, σrts P Rt, h P rHs, the bonus function DFp¨; zrts, σrtsq returned by the 
bonus oracle in Definition 3.3.5 belongs to B. 
3. For the bonus function class B, there exists an ϵ-cover CpB, ϵq Ď B with size |CpB, ϵq| ď 
NBpϵq, such that for any b P B, there exists b1 P CpB, ϵq, such that }b ´ b1}8 ď ϵ. 
4. The optimistic function class at stage h P rHs is: 
Vh “ 
! 
V p¨q “ max aPA 
min ´ 
1, fp¨, aq ` β ¨ bp¨, aq 
¯ 
ˇ 
ˇ 
ˇ 
ˇ 
f P Fh, b P B ) 
. 
94
There exists an ϵ-cover CpVh, ϵq with size |CpVh, ϵq| ď NVh pϵq. For any ϵ ą 0, we define 
the uniform covering number of V with respect to ϵ as NVpϵq :“ maxhPrHs NVh pϵq. 
3.4 Proposed Algorithm 
In this section, we introduce our algorithm GFA-RFE as presented in Algorithm 6 and 
Algorithm 7. GFA-RFE consists of two phases, where in the first exploration phase as 
Algorithm 6, GFA-RFE collects K episodes without reward signal. Then in the second 
planning phase as presented in Algorithm 7, GFA-RFE leverages the collected K episodes 
to learn a policy trying to maximize the cumulative reward given a specific reward function 
r. The details of these two phases are presented in the following subsections. 
3.4.1 Exploration Phase: Efficient Exploration via Uncertainty-aware Intrinsic 
Reward 
The ultimate goals of the exploration phase are exploring environments and collecting data 
in the absence of reward to facilitate finding the near-optimal policy in the next phase. At 
a high level, GFA-RFE achieves these goals by encouraging the agent to explore regions 
containing higher uncertainty, which intuitively guarantees the maximal information gained 
in each episode. 
3.4.1.1 Intrinsic Reward 
GFA-RFE evaluate the uncertainty by DFh in Definition 3.3.3, and uses its oracle DFh 
as 
the intrinsic reward rk,h in Line 4 to generate an uncertainty-target policy in Line 8. Recall 
that D2 Fh 
pz; zrk´1s,h, σrk´1s,hq is defined as 
sup f1,f2PFh 
pf1pzq ´ f2pzqq2 ř 
sPri´1s 1 
σ2 s,h 
pf1pzs,hq ´ f2pzs,hqq2 ` λ . 
95
In particular, a high reward signal means that there exist functions in Fh close to each 
other on all historical observations but divergent for the current state and action pair. This 
further suggests that the past observations are not enough for the agent to make a precise 
value estimation for the current state-action pair. 
3.4.1.2 Weighted Regression 
The usage of the intrinsic reward rk,h induces an intrinsic action-value function Q˚ k,hp¨, ¨; rkq, 
which serves as a metric for cumulative uncertainty of remaining stages. As in model-free 
approaches, GFA-RFE aims to estimate Q˚ k,hp¨, ¨; rkq and further finds a policy πk 
h that would 
maximize the cumulative uncertainty over H stages. This part is presented in Algorithm 6 
through Line 5 to Line 8. 
To reduce the estimation error, GFA-RFE incorporates the weighted regression proposed 
in Zhao et al. (2023) into estimating Q˚ k,hps, a; rkq. The algorithm starts at final stage h “ H 
and estimating the Q˚ k,hps, a; rkq approximated by function f̂k,h using Bellman equation: 
f̂k,hpsh, ahq “ rk,hpsh, ahq ` rPhVk,h`1spsh, ahq « rk,hpsh, ahq ` Vk,h`1psh`1q. 
However, estimating rPhVk,h`1spsh, ahq using Vk,h`1psh`1q may also introduce error since the 
variance of distribution Php¨|s, aq varies among different state-action pair. Therefore, we 
tackle this heterogeneous variance issue by minimizing the Bellman residual loss weighted 
by using the estimated variance σ̄k,h of observed state-action pairs sih, a i h: 
ÿ 
iPrk´1s 
pfi,hpsih, a i hq ´ ri,hpsih, a 
i hq ´ Vi,h`1ps 
i h`1qq2 
σ̄2 i,h 
. 
Obviously, a lower variance σ̄i,h yields a larger weight during the regression. The calculation 
of variances σ̄i,h involves both aleatoric uncertainty and epistemic uncertainty (Kendall and 
Gal, 2017; Mai et al., 2022), where the aleatoric uncertainty is σk,h calculated in Line 13 
caused by indeterminism of the transition and epistemic uncertainty is D1{2 
Fh caused by limited 
data. Such an approach can be proved to improve the sample efficiency of our algorithm 
96
GFA-RFE (see Theorem 3.5.1 and its discussion). Similar approaches have been used 
in Zhou et al. (2021b); Ye et al. (2023) to provide more robust and efficient estimation. 
After obtaining the f̂k,h function through weighted regression, GFA-RFE follows the 
standard optimism design in online exploration methods to add the bonus term bk,h for 
overestimating the Q˚ k,hps, a; rq function in Line 6. Using this optimistic estimation, GFA-
RFE thus takes the greedy policy and estimates the value function Vk,h in Line 7 before 
proceeding to the previous stage h ´ 1. 
Algorithm 6 GFA-RFE – Phase I: Exploration Phase Input: Confidence radius βE, regularization parameter λ 
1: for k “ 1, 2, ¨ ¨ ¨ , K do 
2: for h “ H,H ´ 1, ¨ ¨ ¨ , 1 do 
3: bk,hp¨, ¨q Ð 2βE ¨ DFh p¨, ¨; zrk´1s,h, σ̄rk´1s,hq. 
4: rk,hp¨, ¨q Ð bk,hp¨.¨q{2. 
5: f̂k,h Ð argminfhPFh 
ř 
iPrk´1s 1 
σ̄2 i,h 
pfhpsih, a i hq ´ rk,hpsih, a 
i hq ´ Vk,h`1ps 
i h`1qq2. 
6: Qk,hps, aq Ð min ! 
f̂k,hps, aq ` bk,hps, aq, 1 ) 
. 
7: Vk,hpsq Ð maxa Qk,hps, aq. 
8: Set the policy πk hp¨q Ð argmaxaPAQk,hp¨, aq. 
9: end for 
10: Receive the initial state sk1. 
11: for stage h “ 1, . . . , H do 
12: Take action akh Ð πk hpskhq, receive next state skh`1. 
13: σk,h Ð 2 
b 
logNVpϵq ¨ mintf̂k,hpskh, a k hq, 1u. 
14: σ̄k,h Ð max ␣ 
γ ¨ D 1{2 
Fh pzk,h; zrk´1s,h, σ̄rk´1s,hq, σk,h, α 
( 
. 
15: end for 
16: end for 
97
Algorithm 7 GFA-RFE – Phase II: Planning Phase 
Input: Dataset tpskh, a k h, σ̄ 
2 k,hqupk,hqPrKsˆrHs, confidence radius βP 
Input: Reward function r “ trhuhPrHs 
1: Initiate V̂H`1p¨q Ð 0, Q̂H`1p¨, ¨q Ð 0 
2: for step h “ H, ¨ ¨ ¨ , 1 do 
3: bhp¨, ¨q Ð mintβPDFh pz; zrKs,h, σ̄rKs,hq, 1u. 
4: f̂h Ð argminfhPFh 
ř 
iPrKs 1 
σ̄2 i,h 
pfhpsih, a i hq ´ rhpsih, a 
i hq ´ V̂h`1ps 
i h`1qq2. 
5: Q̂hps, aq Ð min ! 
f̂hps, aq ` bhps, aq, 1 ) 
. 
6: V̂hp¨q Ð maxaPA Q̂hp¨, aq. 
7: πhp¨q Ð argmaxaPA Q̂hp¨, aq. 
8: end for 
Output: Policy π 
3.4.2 Planning Phase: Effective Planning Using Weighted Regression 
After exploring environments and collecting data in the exploration phase, the agent is now 
given the reward for a specific task, but no longer interacts with the environment. GFA-
RFE enters its planning phase and ensures a policy to maximize the cumulative reward of 
rh across all H stages. GFA-RFE estimates Q˚ hps, a; rq by weighted regression and further 
finds the optimal policy πh, which is the same process as in the exploration phase. This part 
is presented in Algorithm 7 through Line 3 to Line 7. 
Remark 3.4.1. Compared with Kong et al. (2021), our algorithm leverages the advantage 
of generalized elude dimension and incorporates the estimated variance σ into 1) weighted 
regression in Line 4 in the planning phase and Line 5 in exploration phase; 2) intrinsic reward 
design in Line 4. Also, our algorithm does not set the reward rk,h “ bk,h{H as of Kong et al. 
(2021); Wang et al. (2020b), thus the agent can explore more aggressively and more efficiently 
using the knowledge of variance of the observation. Therefore, GFA-RFE is more sample 
efficient compared with Kong et al. (2021), which is discussed in detail in Remark 3.5.7. 
98
3.5 Sample Complexity Analysis 
We analyze GFA-RFE theoretically in this section. The uncertainty-aware reward-free ex-
ploration mechanism leads to efficient learning with provable sample complexity guarantees. 
The first theorem characterizes how the sub-optimality decays as exploration time grows. 
Theorem 3.5.1. For GFA-RFE, set confidence radius βE “ Õ ` a 
H logNVpϵq ˘ 
and βP “ 
Õ ` a 
H logNFpϵq ˘ 
, and take α “ 1{ ? H and γ “ 
a 
logNVpϵq. Then, for any δ P p0, 1q, with 
probability at least 1 ´ δ, after collecting K episodes of samples, for any reward function 
r “ trhuHh“1 such that řH 
h“1 rhpsh, ahq ď 1, GFA-RFE outputs a policy π satisfying the 
following sub-optimality bound, 
Es1„µrV ˚ 1 ps1; rq ´ V π 
1 ps1; rqs “ Õ ´ 
H a 
logNFpϵq b 
dimα,KpFq{K ¯ 
. 
We are now ready to present the sample complexity of GFA-RFE for the reward-free 
exploration. 
Corollary 3.5.2. Under the same conditions in Theorem 3.5.1, with probability at least 
1 ´ δ, for any reward function r “ trhuHh“1 such that řH 
h“1 rhpsh, ahq ď 1, GFA-RFE returns 
an ϵ-optimal policy after collecting K ď ÕpH2 logNFpϵq dimα,KpFqϵ´2q episodes during the 
exploration phase. 
Remark 3.5.3. Let dK,δ be maxtlogNFpϵq, dimα,KpFqu, GFA-RFE yields an ÕpH2d2K,δϵ ´2q 
sample complexity for reward-free exploration with high probability. In tabular setting, 
dK,δ “ ÕpSAq, thus yields an ÕpH2S2A2ϵ´2q sample complexity. In linear MDPs and 
generalized linear MDPs with dimension d, dK,δ “ Õpdq, thus yields an ÕpH2d2ϵ´2q sample 
complexity which matches the result from Hu et al. (2022). For a more general setting where 
the function class with eluder dimension d, dK,δ “ Õpdq, which yields a ÕpH2d2ϵ´2q sample 
complexity. 
For a fair comparison with some existing works, we translate our sample complexity 
99
result to the case where the reward scale is rh P r0, 1s, @h P rHs. The result can be trivially 
obtained by replacing r Ñ r{H in GFA-RFE. 
Corollary 3.5.4. With probability at least 1´δ, for any reward function such that rhps, aq P 
r0, 1s or the total reward is bounded by řH 
h“1 rhpsh, ahq ď H, GFA-RFE returns an ϵ-optimal 
policy after collecting K ď ÕpH4d2K,δϵ ´2q episodes in the exploration phase. 
Remark 3.5.5. Compared with Chen et al. (2022a) which provides a Õpd log |P |ϵ´2q sample 
complexity for model-based RL, GFA-RFE is a model-free algorithm which does not need 
to directly sample transition kernel Php¨|¨, ¨q from all possible transitions ∆̃pΠq, therefore, 
GFA-RFE is computationally efficient and can be easily implemented based on the current 
empirical DRL algorithms. 
Remark 3.5.6. Compared with Chen et al. (2022b) which achieves a ÕpH7d3ϵ´2q sample 
complexity, one can find our result significantly improves the dependency on H, d. Chen 
et al. (2022b) didn’t optimize the exploration policy by constructing intrinsic rewards but 
by updating Bellman error constraints on the value function class. It sacrificed the sample 
complexity to adapt the general function approximation settings. In addition, this approach 
is generally computationally intractable as it explicitly maintains feasible function classes. 
For its V-type variant, it even maintains a finite cover of the function class, which can be 
exponentially large. 
Remark 3.5.7. Kong et al. (2021) leveraged the “sensitivity" as the intrinsic reward during 
the exploration and achieved a ÕpH6d4ϵ´2q reward-free sample complexity. Compare their 
algorithm and ours, ours improves a H2d2 factor from 1) using weighted regression to handle 
heterogeneous observations 2) using a “truncated Bellman equation” (Chen et al., 2021) in 
our analysis, and 3) a properly improved uncertainty metric D 2 
Fh instead of the sensitivity. 
100
Table 3.1: Cumulative reward for various exploration algorithms across different environ-
ments and tasks. The cumulative reward is averaged over 8 individual runs for both online 
exploration and offline planning. The result for each individual run is obtained by evaluat-
ing the policy network using the last-iteration parameter. Standard deviation is calculated 
across these runs. Results presented in boldface denote the best performance for each task, 
and those underlined represent the second-best outcomes. The cyan background highlights 
results of our algorithms. 
Environment Task Baselines Ours 
ICM APT DIAYN APS Dis. SMM RND GFA-RFE 
Walker 
Flip 177 ˘ 80 523 ˘ 57 207 ˘ 119 246 ˘ 103 570 ˘ 32 242 ˘ 71 507 ˘ 48 554 ˘ 64 
Run 108 ˘ 41 304 ˘ 38 113 ˘ 38 132 ˘ 39 340 ˘ 37 116 ˘ 21 306 ˘ 34 339 ˘ 34 
Stand 466 ˘ 17 891 ˘ 62 587 ˘ 169 573 ˘ 177 726 ˘ 79 443 ˘ 104 750 ˘ 62 925 ˘ 50 
Walk 411˘237 772˘60 432 ˘ 222 645 ˘ 156 851 ˘ 63 273 ˘ 162 709 ˘ 115 826 ˘ 89 
Quadruped 
Run 93 ˘ 68 452 ˘ 49 158 ˘ 64 159 ˘ 82 524 ˘ 24 162 ˘ 140 522 ˘ 30 460 ˘ 36 
Jump 89 ˘ 47 740 ˘ 91 218 ˘ 114 123 ˘67 829 ˘ 22 211 ˘ 127 790 ˘ 38 719 ˘ 68 
Stand 207 ˘ 134 910 ˘ 45 331 ˘ 81 308 ˘ 147 953 ˘ 16 239 ˘ 104 940 ˘ 27 867 ˘ 61 
Walk 94 ˘ 60 680 ˘ 117 171 ˘ 72 141 ˘ 80 720 ˘ 175 125 ˘ 36 820 ˘ 94 726 ˘ 146 
3.6 Numerical Results 
3.6.1 Experiment Setup 
Based on our theoretical perspective, we integrate our algorithm in the unsupervised rein-
forcement learning (URL) framework and evaluate the performance of the proposed algo-
rithm in URL benchmark (Laskin et al., 2021). As suggested by Ye et al. (2023), we use the 
variance of n-ensembled Q functions as the estimation of the bonus oracle D 2 
F which will be 
used in (1) intrinsic reward rk,h; (2) exploration bonus bk,h; and (3) weights σ2 k,h for the value 
target regression. All these Q networks are trained by Q-learning with different mini-batches 
in the replay buffer. Obviously, the variance of these Q networks comes from the randomness 
of initialization and the randomness of different mini-batches used in training. The pseudo 
101
code for the practical algorithm is deferred to Section 3.9. 
The original implementation of Laskin et al. (2021) involves two phases where the neural 
network is first pretrained by interacting with the environment without receiving reward 
signals and then finetuned by interacting with the environment again with reward signal. 
However, in our experiments, we strictly follow the design of reward-free exploration by 
first exploring the environment without the reward. The explored trajectories are collected 
into a dataset D “ tps, a, s1qu. Then we call a reward oracle r to assign rewards to this 
dataset D and learn the optimal policy using the offline dataset Dr “ tps, a, s1, rps, a, s1qqu 
without interacting the dataset anymore. Intuitively speaking, this online exploration + 
offline planning paradigm is more challenging than the online pretraining + online fine-
tuning and would be more practical, especially with different reward signals. 
3.6.1.1 Unsupervised Reinforcement Learning Benchmarks 
We conduct our experiments on Unsupervised Reinforcement Learning Benchmarks (Laskin 
et al., 2021), which consists of two multi-tasks environments (Walker, Quadruped) from 
DeepMind Control Suite (Tunyasuvunakool et al., 2020). Each environment is equipped with 
several reward functions and goals. For example, Walker-run consists of rewards encouraging 
the walker to run at speed and Walker-stand consists of rewards indicating the walker should 
stead steadily. We consider the state-based input in our experiments where the agent can 
directly observe the current state instead of image inputs (a.k.a. pixel-based). 
3.6.1.2 Baseline Algorithms 
We inherit the baseline algorithms ICM (Pathak et al., 2017), Disagreement (Pathak et al., 
2019), RND (Burda et al., 2018b), APT (Liu and Abbeel, 2021b), DIAYN (Eysenbach et al., 
2018), APS (Liu and Abbeel, 2021a), SMM (Lee et al., 2019). All these algorithms provide 
different ‘intrinsic rewards’ in place of ours during exploration. We make all these baseline 
102
algorithms align with our settings which first collect an exploration dataset and then do 
offline training on the collected dataset with rewards. 
3.6.2 Experiment Results 
Experimental results are presented in Table 3.1. It’s obvious that GFA-RFE can efficiently 
explore the environment without the reward function and then output a near-optimal pol-
icy given various reward functions. For the baseline algorithms, APT, Disagreement, and 
RND perform consistently better than the rest of the 4 algorithms on all 2 environments 
and 8 tasks. The performance of GFA-RFE enjoys compatible or superior performance com-
pared with these top-level methods (APT, Disagreement, and RND), on these tasks. These 
promising numerical results justify our theoretical results and show that GFA-RFE can in-
deed efficiently learn the environment in a practical setting. 
3.6.2.1 Ablation Study 
To verify the performance of our algorithm, we also did ablation studies on 1) the relation-
ship between offline training processes and episodic reward 2) the relationship between the 
quantity of online exploration data used in offline training and the achieve episodic reward. 
The details of the ablation study are deferred to Section 3.9. 
3.7 Conclusion 
In this chapter, we study the reward-free exploration under general function approximation, 
which can be viewed as a theoretical framework of the unsupervised reinforcement learning. 
We show that, with an uncertainty-aware intrinsic reward and variance-weighted regression 
on learning the environment, GFA-RFE can be theoretically proved to explore the environ-
ment efficiently without the existence of reward signals. Experiments show that our design of 
103
intrinsic reward can be efficiently implemented and effectively used in an unsupervised rein-
forcement learning paradigm. In addition, experiment results verify that adding uncertainty 
estimation to the learning processes can improve the sample efficiency of the algorithm, 
which is aligned with our theoretical results of weighted regression. 
3.8 Proofs 
3.8.1 Proof of Theorems in Section 3.5 
3.8.1.1 Additional Definitions and High Probability Events 
In this section, we introduce additional definitions that will be used in the proofs. Also, we 
define the good events that GFA-RFE is guaranteed to have near-optimal sample complexity. 
Definition 3.8.1 (Truncated Optimal Value Function). We define the following truncated 
value functions for any reward r: 
Ṽ ˚ H`1ps; rq “ 0, @s P S 
Q̃˚ hps, a; rq “ mintrhps, aq ` PhṼ 
˚ h`1ps, a; rq, 1u, @ps, aq P S ˆ A 
Ṽ ˚ h ps; rq “ max 
aPA Q̃˚ 
hps, a; rq. @s P S, h P rHs. 
The good event EE k,h at stage h of episode k in exploration phase is defined to be: 
EE k,h “ 
! 
λ ` ÿ 
iPrk´1s 
1 
σ̄2 i,h 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
ď pβE q 2 ) 
. 
The intersection of all good events in exploration phase is: 
EE :“ č 
kě1,hPrHs 
EE k,h. 
The following lemma indicates that E holds with high probability for GFA-RFE. 
Lemma 3.8.2. In Algorithm 6, for any δ P p0, 1q and fixed h P rHs, with probability at 
least 1 ´ δ, EE holds. 
104
In the planning phase, we define the good events for exploration phase with indicator 
functions as 
EP 
h “ 
! 
λ ` ÿ 
iPrKs 
1h 
σ̄2 i,h 
´ 
f̂hpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq 
¯2 
ď pβ̂P q 2 ) 
, 
EP “ 
č 
hPrHs 
EP 
h , 
where 1̂h “ 1pV ˚ h`1psq ď V̂h`1psq, @s P Sq ¨ 1pV̂h`1psq ď Vk,h`1psq ` V ˚ps; rq, @s P Sq ¨ 
1prVhpV̂h`1 ´V ˚ h`1qspskh, a 
k hq ď η´1σ̄2 
k,h, @k P rKsq and η “ logNVpϵq. Like in the exploration 
phase, we also have that EP holds with high probability for GFA-RFE. 
Lemma 3.8.3. In Algorithm 6, for any δ P p0, 1q and fixed h P rHs, with probability at 
least 1 ´ δ, EP holds. 
Furthermore, we have the following good events in the planning phase without indicator 
function: 
EP h “ 
! 
λ ` 
k´1 ÿ 
i“1 
1 
pσ̄i,h1q2 
´ 
f̂h1psih1 , aih1q ´ Th1Vh1`1ps i h1 , aih1q 
¯2 
ď pβP q 2, @h ď h1 
ď H, k P rKs 
) 
. 
And we define EP :“ EP 1 . We shows that EP holds if both EE, EP hold with the help of the 
following lemma: 
Lemma 3.8.4. If the event EE, EP , EP 
h`1 all hold, then event EP h holds. 
Since EP H holds trivially, Lemma 3.8.4 indicates that EP holds. 
3.8.1.2 Covering Number 
The optimistic value functions at stage h P rHs in our construction belong to the following 
function class: 
Vh “ 
" 
V p¨q “ max aPA 
min p1, fp¨, aq ` β ¨ bp¨, aqq 
ˇ 
ˇ 
ˇ 
ˇ 
f P Fh, b P B * 
. (3.8.1) 
105
Lemma 3.8.5 (ϵ-covering number of optimistic value function classes). For optimistic value 
function class Vk,h defined in (3.8.1), we define the distance between two value functions V1 
and V2 as }V1 ´ V2}8 :“ maxsPS |V1psq ´ V2psq|. Then the ϵ-covering number with respect to 
the distance function can be upper bounded by 
NVh pϵq :“ NFh 
pϵ{2q ¨ NBpϵ{2βq. (3.8.2) 
Lemma 3.8.5 further indicates that 
NVpϵq “ max hPrHs 
NVh pϵq “ max 
hPrHs NFh 
pϵ{2q ¨ NBpϵ{2βq “ NFpϵ{2q ¨ NBpϵ{2βq. 
3.8.1.3 Proof of Theorems 
We first introduce the following lemmas to build the path to Theorem 3.5.1. 
Lemma 3.8.6. On the event EP , we have 
|f̂hps, aq ´ ThV̂h`1| ď βPDFh pz; zrKs,h, σ̄rKs,hq. 
Lemma 3.8.7 (Optimism in the planning phase). On the event EP , for any h P rHs, we 
have 
V ˚ h ps; rq ď V̂hpsq, @s P S. 
Lemma 3.8.8. On the event EE, with probability at least 1 ´ 3δ, we have 
K ÿ 
k“1 
Vk,1ps k 1q “ OpβE 
b 
dimα,KpFqH ? Kq. 
Lemma 3.8.9. With probability 1 ´ δ, we have 
ˇ 
ˇ 
ˇ 
K ÿ 
k“1 
` 
Es„µ 
“ 
Ṽ ˚ 1 ps; rkq 
‰ 
´ Ṽ ˚ 1 ps; rkq 
˘ 
ˇ 
ˇ 
ˇ ď a 
2K logp1{δq. 
We denote the event that Lemma 3.8.8 holds as Φ, and the event that Lemma 3.8.9 holds 
as Ψ. 
106
Lemma 3.8.10. Under event EE X Φ X Ψ, we have 
Es„µ 
” 
Ṽ ˚ 1 ps; bq 
ı 
“ O ´ 
βE b 
H dimα,KpFq{K a 
logNFpϵq{ logNVpϵq ¯ 
, 
where b “ tbhuHh“1 is the UCB bonus in planning phase. 
With these lemmas, we are ready to prove Theorem 3.5.1. 
Proof of Theorem 3.5.1. By Lemma 3.8.7, we can upper bound the suboptimality as 
Es1„µrV ˚ 1 ps1; rq ´ V π 
1 ps1; rqs ď Es1„µrV̂1ps1q ´ V π 1 ps1; rqs. 
Then, we can decompose the difference between optimistic estimate of value function and 
the true value function in the following: 
Es1„µrV̂1ps1q ´ V π 1 ps1; rqs 
“ Es1„µ 
” 
mintf̂1ps1, πps1qq ` b1ps1, πps1qq, 1u ´ r1ps1, πps1qq ´ P1V π 2 ps1, πps1q; rq 
ı 
ď Es1„µ 
” 
mintf̂1ps1, πps1qq ` b1ps1, πps1qq ´ r1ps1, πps1qq ´ P1V π 2 ps1, πps1q; rq, 1u 
ı 
“ Es1„µ 
” 
min ! 
f̂1ps1, πps1qq ´ r1ps1, πps1qq ´ P1V̂ π 2 ps1, πps1q; rq 
` P1V̂ π 2 ps1, πps1q; rq ` b1ps1, πps1qq ´ P1V 
π 2 ps1, πps1q; rq, 1 
)ı 
“ Es1„µ 
” 
min ! 
f̂1ps1, πps1qq ´ T1V̂ π 2 ps1, πps1qq ` P1V̂ 
π 2 ps1, πps1q; rq 
` b1ps1, πps1qq ´ P1V π 2 ps1, πps1q; rq, 1 
)ı 
ď Es1„µ 
” 
min ! 
2b1ps1, πps1qq ` P1V̂ π 2 ps1, πps1q; rq ´ P1V 
π 2 ps1, πps1q; rq, 1 
)ı 
, 
107
where the last inequality holds due to Lemma 3.8.6. Then, by the induction, we have 
Es1„µrV̂1ps1q ´ V π 1 ps1; rqs 
ď Es1„µ 
” 
min ! 
2b1ps1, πps1qq ` P1V̂ π 2 ps1, πps1q; rq ´ P1V 
π 2 ps1, πps1q; rq, 1 
)ı 
“ Es1„µ,s2„Pp¨|s1,πps1qq 
” 
min ! 
2b1ps1, πps1qq ` V̂ π 2 ps2; rq ´ V π 
2 ps2; rq, 1 )ı 
ď Eτ„dπ 
” 
min ! 
H ÿ 
h“1 
2bhpsh, πpshqq, 1 )ı 
ď 2Es1„µ 
” 
Ṽ π 1 ps1; bq 
ı 
ď 2Es1„µ 
” 
Ṽ ˚ 1 ps1; bq 
ı 
“ O ´ 
βE b 
H dimα,KpFq{K a 
logNFpϵq{ logNVpϵq ¯ 
. 
Therefore, by substituting βE “ Õ ` a 
H logNVpϵq ˘ 
, we complete the proof: 
Es1„µrV ˚ 1 ps1; rq ´ V π 
1 ps1; rqs “ O ´ 
H b 
dimα,KpFq{K a 
logNFpϵq ¯ 
. 
Proof of Corollary 3.5.2. By solving Es1„µrV ˚ 1 ps1; rq ´ V π 
1 ps1; rqs ď ϵ, we have that 
K ě H2 logNFpϵq dimα,KpFq 
ϵ2 . 
3.8.2 Proof of Lemmas in Section 3.8.1 
In this section, we prove the lemmas used in Section 3.8.1. 
Proof of Lemma 3.8.2. We first prove that EE k,h holds with probability 1´ δ{pKHq. We have 
ThVk,h`1 P Fh due to Assumption 3.3.2. For any function V : S Ñ r0, 1s, let ηkhpV q “ 
108
rk,hpskh, a k hq ` V pskh`1q ´ ThV pskh, a 
k hq. For all f P Fh, since a2 ´ 2ab “ pa ´ bq2 ´ b2, we have 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
´ 2 ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq ˘ 
ηkhpVk,h`1q 
loooooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooooon 
Ipf,ThVk,h`1,Vk,h`1q 
“ ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
rk,hpsih, a i hq ` Vk,h`1ps 
i h`1q ´ fpsih, a 
i hq 
¯2 
´ ÿ 
iPrk´1s 
1 
pσ̄i,hq2 ηkhpVk,h`1q 
2. 
Take f “ f̂k,h. By the the definition of f̂k,h, we have 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
´ 2Ipf̂k,h, ThVk,h`1, Vk,h`1q ď 0 
Applying Lemma 3.8.19, for fixed f , f̄ , and V , with probability at least 1 ´ δ, 
Ipf, f̄ , V q :“ ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯ 
ηkhpV q 
ď 2τ 
α2 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
` 1 
τ ¨ log 
1 
δ . 
Applying a union bound and take τ “ α2 
8 , for any k, with probability at least 1´ δ, we have 
for all V c in the ϵ-net Vh`1 that 
Ipf, f̄ , V c q ď 
1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
` 2 
α2 ¨ log 
NVpϵq 
δ 
For all V such that }V ´ V c}8 ď ϵ, we have |ηihpV q ´ ηihpV cq| ď 4ϵ. Thus, 
Ipf, f̄ , Vk,h`1q ď 1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
` 2 
α2 ¨ log 
NVpϵq 
δ ` 4ϵ ¨ kL{α2 
Applying a union bound, for any k, with probability at least 1 ´ δ, we have for all fa, f b in 
the ϵ-net CpFh, ϵq that 
Ipfa, f b, Vk,h`1q ď 1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fa psih, a 
i hq ´ f b 
psih, a i hq 
¯2 
` 2 
α2 ¨ log 
NVpϵq ¨ NFpϵq2 
δ ` 4ϵ ¨ kL{α2. 
109
Therefore, with probability at least 1 ´ δ, we have 
Ipf̂k,h, ThVk,h`1, Vk,h`1q ď Ipfa, f b, Vk,h`1q ` 8ϵ ¨ k{α2 
ď 1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
fa psih, a 
i hq ´ f b 
psih, a i hq 
¯2 
` 4 
α2 ¨ log 
NVpϵq ¨ NFpϵq 
δ ` 
4ϵkL ` 8ϵk 
α2 
ď 1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
` 4 
α2 ¨ log 
NVpϵq ¨ NFpϵq 
δ ` 4ϵ ¨ kL{α2 
` 8ϵ ¨ k{α2 ` 2Lϵ ¨ k{α2 
ď 1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
` 4 
α2 ¨ log 
NVpϵq ¨ NFpϵq 
δ ` 14Lϵ ¨ k{α2. 
Substituting it back, with probability at least 1 ´ δ{pKHq, we have 
1 
4 
ÿ 
iPrk´1s 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1ps 
i h, a 
i hq 
¯2 
ď 16 
α2 ¨ log 
KH ¨ NVpϵq ¨ NFpϵq 
δ ` 56Lϵk{α2 
Take α “ 1{ ? H and let 
βE “ 
c 
16H log KH ¨ NVpϵq ¨ NFpϵq 
δ ` 56Lϵ ¨ K{α2 ` λ. 
Then we complete the proof by taking a union bound for all k P rKs and h P rHs. 
Proof of Lemma 3.8.3. We have ThV̂h`1 P Fh due to Assumption 3.3.2. For any function 
V : S Ñ r0, 1s, let ηkhpV q “ rhpskh, a k hq ` V pskh`1q ´ ThV pskh, a 
k hq. For all f P Fh, we have 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ ThV̂h`1psih, a 
i hq 
¯2 
´ 2 ÿ 
iPrKs 
1̂h 
` 
fpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq ˘ 
ηkhpV̂h`1q 
pσ̄i,hq2 
loooooooooooooooooooooooooooomoooooooooooooooooooooooooooon 
Ipf,ThV̂h`1,V̂h`1q 
“ ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
rhpsih, a i hq ` V̂h`1ps 
i h`1q ´ fpsih, a 
i hq 
¯2 
´ ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 ηkhpV̂h`1q 
2. 
By definition, we have that 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq 
¯2 
´ 2Ipf̂h, ThV̂h`1, V̂h`1q ď 0. 
110
We decompose Ipf̂h, ThV̂h`1, V̂h`1q into two parts: 
Ipf̂h, ThV̂h`1, V̂h`1q “ ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq 
¯ 
ηkhpV̂h`1 ´ V ˚ h`1q 
` ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThV̂h`1psih, a 
i hq 
¯ 
ηkhpV ˚ h`1q. (3.8.3) 
For the first term in (3.8.3), we have 
E „ 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq ˘ 
ηkhpV̂h`1 ´ V ˚ h`1q 
ȷ 
“ 0. 
Furthermore, we can bound the maximum as following: 
max iPrKs 
ˇ 
ˇ 
ˇ 
ˇ 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq ˘ 
ηkhpV̂h`1 ´ V ˚ h`1q 
ˇ 
ˇ 
ˇ 
ˇ 
ď 2max iPrKs 
ˇ 
ˇ 
ˇ 
ˇ 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq ˘ 
ˇ 
ˇ 
ˇ 
ˇ 
ď 2max iPrKs 
1̂h 
pσ̄i,hq2 
g 
f 
f 
eD2 Fh 
pzi,h; zri´1s,h, σ̄ri´1s,hq 
ˆ 
ÿ 
sPri´1s 
1 
pσ̄s,hq2 pfpssh, a 
s hq ´ f̄pssh, a 
s hqq2 ` λ 
˙ 
ď 2max iPrKs 
1 
pσ̄i,hq2 
g 
f 
f 
eD2 Fh 
pzi,h; zri´1s,h, σ̄ri´1s,hq 
ˆ 
ÿ 
sPri´1s 
1̂h 
pσ̄s,hq2 pfpssh, a 
s hq ´ f̄pssh, a 
s hqq2 ` λ 
˙ 
ď 2 ¨ γ´2 
g 
f 
f 
e 
ÿ 
sPrKs 
1̂h 
pσ̄s,hq2 pfpssh, a 
s hq ´ f̄pssh, a 
s hqq2 ` λ, 
where the first inequality is due to bounded total rewards assumption, the second inequality 
holds due to Definition 3.3.3, and the last inequality holds due to Line 14 in Algorithm 6 
and Definition 3.3.6. 
We further define varpV ´ V ˚ h`1q as 
varpV ´ V ˚ h`1q :“ 
ÿ 
iPrKs 
E ” 1̂h 
pσ̄i,hq4 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
ηkhpV̂h`1 ´ V ˚ h`1q 
2 ı 
ď L2K{α4. 
111
By the definition of the indicator function, we have 
varpV ´ V ˚ h`1q ď 
4 
η 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
For fixed f , f̄ , by applying Lemma 3.8.20 with V 2 “ L2K{α4,M “ 2L{α2, v “ η´1{2,m “ v2, 
and probability at least 1 ´ δ{pNFpϵq2NVpϵqHq we have 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯ 
ηkhpV ´ V ˚ h`1q 
ď ι b 
2 ` 
2varpV ´ V ˚ h`1q ` η´1 
˘ 
` 2 
3 ι2 ˆ 
4γ´2 
g 
f 
f 
e 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
` 
fpsih, a i hq ´ f̄psih, a 
i hq ˘2 
` λ ` η´1 
˙ 
, 
where 
ι2pk, h, δq :“ log NFpϵq2 ¨ NVpϵq ¨ plogpL2Kη{α4q ` 2q ¨ plogp2Lη{α2q ` 2q 
δ{H 
Using a union bound over all pf, f̄ , V q P CpFh, ϵqˆCpFh, ϵqˆCpVh“1, ϵq, we have the inequality 
above holds for all such f, f̄ , V with probability at least 1 ´ δ{H. There exist a V c h`1 in the 
ϵ-net such that }V̂h`1 ´ V c h`1} ď ϵ. Then we have 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq 
¯ 
ηkhpV̂h`1 ´ V ˚ h`1q 
ď O 
ˆ 
ιpk, h, δqη´1{2 ` ιpk, h, δq 
2γ´2 
˙ 
¨ 
g 
f 
f 
e 
ÿ 
τPrKs 
1̂h 
pσ̄τ,hq2 pf̂hpsτh, a 
τ hq ´ ThVh`1psτh, a 
τ hqq2 ` λ 
` OpϵkL{α2 q ` Opι2pk, h, δqη´1 
q ` Opιpk, h, δqη´1{2 q. (3.8.4) 
For the second term in (3.8.3), applying Lemma 3.8.19, for fixed f , f̄ , and V ˚ h`1, with 
probability at least 1 ´ δ, we have 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯ 
ηkhpV ˚ h`1q 
ď 1 
4 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fpsih, a i hq ´ f̄psih, a 
i hq 
¯2 
` 8 
α2 ¨ log 
1 
δ . 
112
Applying a union bound, for any k, with probability at least 1 ´ δ, we have for all fa, f b in 
the ϵ-net Fh 
Ipfa, f b, V ˚ h`1q ď 
1 
4 
ÿ 
iPrk´1s 
1̂i,h 
pσ̄i,hq2 
´ 
fa psih, a 
i hq ´ f b 
psih, a i hq 
¯2 
` 8 
α2 ¨ log 
NFpϵq2 
δ . 
Therefore, with probability at least 1 ´ δ, we have 
Ipf̂h, ThVh`1, V ˚ h`1q ď Ipfa, f b, V ˚ 
h`1q ` 8ϵ ¨ K{α2 
ď 1 
4 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
fa psih, a 
i hq ´ f b 
psih, a i hq 
¯2 
` 8 
α2 ¨ log 
¨NFpϵq2 
δ ` 8ϵ ¨ k{α2 
ď 1 
4 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThVh`1ps 
i h, a 
i hq 
¯2 
` 8 
α2 ¨ log 
NFpϵq2 
δ 
` 8ϵ ¨ k{α2 ` 2Lϵ ¨ k{α2 
ď 1 
4 
ÿ 
iPrKs 
1̂h 
pσ̄i,hq2 
´ 
f̂hpsih, a i hq ´ ThVh`1ps 
i h, a 
i hq 
¯2 
` 8 
α2 ¨ log 
NFpϵq2 
δ ` 10Lϵ ¨ k{α2. (3.8.5) 
Taking η “ logNVpϵq, γ “ Õ ` a 
logNVpϵq ˘ 
and α “ 1{ ? H and substituting (3.8.4) and 
(3.8.5) back into (3.8.3), we have 
λ ` ÿ 
iPrKs 
1h 
σ̄2 i,h 
´ 
f̂hpsih, a i hq ´ ThV̂h`1ps 
i h, a 
i hq 
¯2 
ď O 
ˆ 
H logNFpϵq 
˙ 
` O 
ˆ 
plogNVpϵqq ´1 log 
plogpL2K{α4q ` 2q ¨ plogp2L{α2q ` 2q 
δ{H 
˙ 
` Opλq. 
Lemma 3.8.11. On the event EE X EP h , for any h P rHs, we have 
V ˚ h ps; rq ` Vk,hpsq ě V̂hpsq. (3.8.6) 
Lemma 3.8.12. On the event EE X EP h`1, for each episode k P rKs, we have 
logNVpϵq ¨ rVhpV̂h`1 ´ V ˚ h`1qspskh, a 
k hq ď σ2 
k,h, 
where σ2 k,h “ 4 logNVpϵq ¨ mintf̂k,hpskh, a 
k hq, 1u. 
113
Proof of Lemma 3.8.4. Recall that the indicator function in event EP is 
1̂h “1pV ˚ h`1psq ď V̂h`1psq, @s P Sq 
loooooooooooooooooomoooooooooooooooooon 
I1 
¨1pV̂h`1psq ď Vk,h`1psq ` V ˚ ps; rq, @s P S, @k P rKsq 
looooooooooooooooooooooooooooooooomooooooooooooooooooooooooooooooooon 
I2 
¨ 1prVhpV̂h`1 ´ V ˚ h`1qspskh, a 
k hq ď η´1σ̄2 
k,h, @k P rKsq loooooooooooooooooooooooooooooooomoooooooooooooooooooooooooooooooon 
I3 
, 
where η “ logNVpϵq. Lemma 3.8.11, Lemma 3.8.7, and Lemma 3.8.12 indicate that I1 “ 
I2 “ I3 “ 1. 
Proof of Lemma 3.8.5. There exists an ϵ{2-net of F , denoted by CpFh, ϵ{2q, such that for 
any f P Fh, we can find f 1 P CpF , ϵ{2q such that }f ´ f 1}8 ď ϵ{2. Also, there exists an 
ϵ{2β-net of B, CpB, ϵ{2βq. 
Then we consider the following subset of Vh, 
Vc h “ 
" 
V p¨q “ max aPA 
min ` 
1, fp¨, aq ` β ¨ bp¨, aq ˘ 
ˇ 
ˇ 
ˇ 
ˇ 
f P CpFh, ϵ{2q, b P CpB, ϵ{2βq 
* 
. 
Consider an arbitrary V P V where V “ maxaPAminp1, fip¨, aq ` β ¨ bip¨, aqq. For each fi, 
there exists f c i P CpFh, ϵ{2q such that }fi ´ f c 
i }8 ď ϵ{2. There also exists bc P CpB, ϵ{2βq 
such that }bi ´ bc}8 ď ϵ{2β. Let V c “ maxaPAminp1, f c i p¨, aq ` β ¨ bcp¨, aqq P Vc. It is then 
straightforward to check that }V ´ V c}8 ď ϵ{2 ` β ¨ ϵ{2β “ ϵ. 
By direct calculation, we have |Vc h| “ NFh 
pϵ{2q ¨ NBpϵ{2βq. 
Proof of Lemma 3.8.6. According to the definition of D2 F function, we have 
` 
f̂k,hps, aq ´ ThVk,h`1ps, aq ˘2 
ď D2 Fh 
pz; zrk´1s,h, σ̄rk´1s,hq ˆ 
ˆ 
λ ` 
k´1 ÿ 
i“1 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1psih, a 
i hq 
¯2 ˙ 
ď pβE q 2 
ˆ D2 Fh 
pz; zrk´1s,h, σ̄rk´1s,hq, 
where the first inequality holds due the definition of D2 F function with the Assumption 3.3.2 
and the second inequality holds due to the events EE h . Thus, we have 
ˇ 
ˇf̂k,hps, aq ´ ThVk,h`1ps, aq ˇ 
ˇ ď βEDFh pz; zrk´1s,h, σ̄rk´1s,hq. 
114
Proof of Lemma 3.8.7. We prove this statement by induction. Note that V ˚ H`1ps; rq “ 
V̂H`1psq. Assume that the statement holds for h ` 1. If V̂hpsq “ 1, then the statement 
holds trivially for h; otherwise, we have for any ps, aq P S ˆ A that 
Q̂hps, aq ´ Q˚ hps, a; rq 
“ f̂hps, aq ` bhps, aq ´ rrhps, a; rq ` PhV ˚ h`1ps, a; rqs 
“ rf̂hps, aq ´ rhps, a; rq ´ PhV̂h`1ps, a; rqs ` bhps, aq ` PhV̂h`1ps, a; rq ´ PhV ˚ h`1ps, a; rq 
ě rf̂hps, aq ´ rhps, a; rq ´ PhV̂h`1ps, a; rqs ` bhps, aq 
ě ´βPDFh pz; zrKs,h, σ̄rKs,hq ` βPDFh 
pz; zrKs,h, σ̄rKs,hq 
ě 0, 
where the first inequality holds due to the induction assumption, and the second inequality 
holds due to Lemma 3.8.6. 
In order to prove Lemma 3.8.8, we need the following three lemmas. 
Lemma 3.8.13 (Simulation Lemma). On the event EE, we have 
0 ď Vk,hpskhq ď E τkh„dπ 
k h pskhq 
min ! 
3βE H ÿ 
h1“h 
Dpzk,h1 ; zrk´1s,h1 , σrk´1s,h1q, 1 ) 
. 
Lemma 3.8.14. [Lemma C.13 in Zhao et al. (2023)]For any parameters β ě 1 and stage 
h P rHs, the summation of confidence radius over episode k P rKs is upper bounded by 
K ÿ 
k“1 
min ´ 
βDFh pz; zrk´1s,h, σ̄rk´1s,hq, 1 
¯ 
ď p1 ` Cβγ2 q dimα,KpFhq ` 2β 
b 
dimα,KpFhq 
g 
f 
f 
e 
K ÿ 
k“1 
pσ2 k,h ` α2q, 
where z “ ps, aq and zrk´1s,h “ tz1,h, z2,h, .., zk´1,hu. 
115
Lemma 3.8.15. Under event EE, we have 
K ÿ 
k“1 
H ÿ 
h“1 
σ2 k,h ď 2304C2H3 
plogNVpϵqq 2 pβE 
q 2 dimα,KpFq 
` 48H2 logNVpϵqp1 ` CβEγ2 q dimα,KpFhq 
` 16H logNVpϵq a 
2HK logpH{δq ` K. 
Now we can prove Lemma 3.8.8. 
Proof of Lemma 3.8.8. We have 
K ÿ 
k“1 
Vk,1psk1q ď 
K ÿ 
k“1 
E τkh„dπ 
k h pskhq 
min ! 
3βE H ÿ 
h1“1 
Dpzk,h; zrks,h, σrks,hq, 1 ) 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
E τkh„dπ 
k h pskhq 
min ! 
3βEDpzk,h; zrk´1s,h, σrk´1s,hq, 1 ) 
ď Hp1 ` 4CβEγ2 q dimα,KpFhq ` 8βE 
b 
dimα,KpFq 
g 
f 
f 
eH K ÿ 
k“1 
H ÿ 
h“1 
pσ2 k,h ` α2q 
“ OpβE b 
KH dimα,KpFqq, 
where the first inequality follows from Lemma 3.8.13, the third inequality follows from 
Lemma 3.8.14, and the last equality holds due to Lemma 3.8.15. 
Proof of Lemma 3.8.9. Denote ∆k “ Es„µ 
“ 
Ṽ ˚ 1 ps; rkq 
‰ 
´ Ṽ ˚ 1 psk1; rkq. By Azuma-Hoeffding 
inequality (Lemma 3.8.21), we have 
ˇ 
ˇ 
ˇ 
K ÿ 
k“1 
∆k 
ˇ 
ˇ 
ˇ ď a 
2K logp1{δq. 
Lemma 3.8.16. On the event EE, for any k P rKs and h P rHs, we have 
Ṽ ˚ h ps; rkq ď Vk,hpsq, @s P S. 
116
Proof of Lemma 3.8.10. Since βE “ Op a 
H logNVpϵqq and βP “ Op a 
H logNFpϵqq, for 
some constant c, we have 
βE ě c 
a 
logNVpϵq{ logNFpϵq ¨ βP . 
Therefore, for any h P rHs, we have rk,hp¨, ¨q ě rK,hp¨, ¨q ě c a 
logNVpϵq{ logNFpϵq ¨ bhp¨, ¨q. 
Hence, 
c a 
logNVpϵq{ logNFpϵq ¨ Es„µ 
” 
Ṽ ˚ 1 ps; bq 
ı 
“ Es„µ 
” 
Ṽ ˚ 1 ps; c 
a 
logNVpϵq{ logNFpϵq ¨ bq ı 
ď Es„µ 
” 
Ṽ ˚ 1 ps; rkq 
ı 
{K 
“ 
” 
K ÿ 
k“1 
Ṽ ˚ 1 psk1; rkq ` 
K ÿ 
k“1 
” 
Es„µ 
” 
Ṽ ˚ 1 ps; rkq 
ı 
´ Ṽ ˚ 1 psk1; rkq 
ıı 
{K 
ď 
´ 
K ÿ 
k“1 
Ṽ ˚ 1 ps; rkq 
¯ 
{K ` a 
2 logp1{δq{K 
ď 
´ 
K ÿ 
k“1 
Vk,1ps; rkq 
¯ 
{K ` a 
2 logp1{δq{K 
“ O ´ 
βE b 
H dimα,KpFq{K ¯ 
, 
where the second inequality follows from Lemma 3.8.9, and the third inequality follows from 
Lemma 3.8.16. Therefore, we have 
Es„µ 
” 
Ṽ ˚ 1 ps; bq 
ı 
“ O ´ 
βE b 
H dimα,KpFq{K a 
logNFpϵq{ logNVpϵq ¯ 
. 
3.8.3 Proofs of Lemmas in Section 3.8.2 
Proof of Lemma 3.8.11. We see that 
Q˚ p¨, ¨; rq “ rhp¨, ¨q ` PhVh`1p¨, ¨; rq, 
Qk,hp¨, ¨q “ mintf̂k,hp¨, ¨q ` bk,hp¨, ¨q, 1u, 
Q̂hp¨, ¨q “ mintf̂hp¨, ¨q ` bhp¨, ¨q, 1u. 
117
We prove this statement by induction. Note that V ˚ H`1ps; rq ` Vk,H`1psq “ V̂H`1psq “ 0. 
Assume the statement holds for h ` 1. By definition, we have 
Q˚ hps, a; rq ` 1 ě Q̂hps, aq. 
Therefore, we only need to prove 
Q˚ hps, a; rq ` f̂k,hps, aq ` bk,hps, aq ´ Q̂hps, aq ě 0. 
We have 
Q˚ hps, a; rq ` f̂k,hps, aq ` bk,hps, aq ´ Q̂hps, aq 
“ rhps, aq ` PhV ˚ h`1ps, a; rq ` f̂k,hps, aq ` bk,hps, aq ´ mintf̂hps, aq ` bhps, aq, 1u 
ě rhps, aq ` PhV ˚ h`1ps, a; rq ` f̂k,hps, aq ` bk,hps, aq ´ pf̂hps, aq ` bhps, aqq 
“ PhV ˚ h`1ps, a; rq ` PhVk,h`1ps, aq ´ PhV̂h`1ps, aq ` r̂k,hps, aq ` bk,hps, aq ´ bhps, aq 
` pf̂k,hps, aq ´ r̂k,hps, aq ´ PhVk,h`1ps, aqq ` prhps, aq ` PhV̂hps, aq ´ f̂hps, aqq 
ě r̂k,hps, aq ` bk,hps, aq ´ bhps, aq ` pf̂k,hps, aq ´ r̂k,hps, aq ´ PhVk,h`1ps, aqq 
` prhps, aq ` PhV̂hps, aq ´ f̂hps, aqq 
ě 3βEDFh pz; zrk´1s,h, σrk´1s,hq ´ βPDFh 
pz; zrKs,h, σrKs,hq ´ βEDFh pz; zrk´1s,h, σrk´1s,hq 
´ βPDFh pz; zrKs,h, σrKs,hq 
ě 0, 
where the second inequality holds due to induction assumption, the third inequality holds 
by high probability events, and the last inequality holds by βE ě βP , D̄Fh pz; zrks,h, σrks,hq 
decreasing with k, and Definition 3.3.5. 
Lemma 3.8.17. On the event EE, we have 
|f̂k,hps, aq ´ ThVk,h`1| ď βEDFh pz; zrk´1s,h, σ̄rk´1s,hq 
118
Proof of Lemma 3.8.12. We have Lemma 3.8.7 and 3.8.11 both hold on EP h`1. Therefore, we 
have 
rVhpV̂h`1 ´ V ˚ h`1qspskh, a 
k hq 
ď rPhpV̂h`1 ´ V ˚ h`1q 
2 spskh, a 
k hq 
ď 2rPhpV̂h`1 ´ V ˚ h`1qspskh, a 
k hq 
ď 2rPhVk,h`1sps k h, a 
k hq 
“ 2pThVk,h`1ps k h, a 
k hq ´ rk,hpskh, a 
k hqq 
ď 2pf̂k,hpskh, a k hq ` βEDFh 
pzk,h; zrk´1s,h, σ̄rk´1s,hq ´ βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hqq 
ď 2f̂k,hpskh, a k hq, 
where the second inequality holds due to Lemma 3.8.7 and V̂h`1, V ˚ h`1 P r0, 1s, the third 
inequality holds due to Lemma 3.8.11, the fourth inequality holds due to Lemma 3.8.17, and 
the last inequality holds due to Definition 3.3.5. 
Proof of Lemma 3.8.13. According to Algorithm 6, we have that 
Qk,hp¨, ¨q “ mintf̂k,hp¨, ¨q ` bk,hp¨, ¨q, 1u, 
Vk,hp¨q “ max a 
Qk,hp¨, aq, 
akh “ πk hpskhq “ argmax 
a Qk,hpskh, aq. 
119
For all k and all h, we have that Vk,hpskhq “ Qk,hpskh, a k hq and thus 
Vk,hpskhq 
ď f̂k,hpskh, a k hq ` bk,hpskh, a 
k hq 
“ 2βEDpzk,h; zrk´1s,h, σrk´1s,hq ` pf̂k,hpskh, a k hq ´ ThVk,h`1ps 
k h, a 
k hqq ` ThVk,h`1ps 
k h, a 
k hq 
¨ ¨ ¨ 
“ E τkh„dπ 
k h pskhq 
H ÿ 
h1“h 
” 
pf̂k,h1pskh1 , akh1q ´ ThVk,h1`1ps k h1 , akh1qq ` 2βEDpzk,h1 ; zrk´1s,h1 , σrk´1s,h1q 
ı 
ď E τkh„dπ 
k h pskhq 
H ÿ 
h1“h 
3βEDpzk,h1 ; zrk´1s,h1 , σrk´1s,h1q, 
where the last inequality holds due to Lemma 3.8.17 and Definition 3.3.5. 
Lemma 3.8.18. On the event EE, with probability at least 1 ´ δ, 
K ÿ 
k“1 
H ÿ 
h“1 
PhVk,h`1ps k h, , a 
k hq ď H 
K ÿ 
k“1 
H ÿ 
h“1 
min ! 
4βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1 
) 
` pH ` 1q a 
2HK logp1{δq 
120
Proof of Lemma 3.8.15. Recall σ2 k,h “ 4 logNVpϵq ¨ mintf̂k,hpskh, a 
k hq, 1u. We have 
K ÿ 
k“1 
H ÿ 
h“1 
σ2 k,h “ 4 logNVpϵq 
K ÿ 
k“1 
H ÿ 
h“1 
mintf̂k,hpskh, a k hq, 1u 
ď 4 logNVpϵq K ÿ 
k“1 
H ÿ 
h“1 
mintThVk,h`1pskh, a k hq ` βEDFh 
pzk,h; zrk´1s.h, σ̄rk´1s,hq, 1u 
ď 4 logNVpϵq K ÿ 
k“1 
H ÿ 
h“1 
mintPhVk,h`1ps k h, a 
k hq ` 2βEDFh 
pzk,h; zrk´1s.h, σ̄rk´1s,hq, 1u 
ď 4 logNVpϵq K ÿ 
k“1 
H ÿ 
h“1 
PhVk,h`1ps k h, a 
k hq 
` 8 logNVpϵq K ÿ 
k“1 
H ÿ 
h“1 
tβEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1u 
ď 24H logNVpϵq K ÿ 
k“1 
H ÿ 
h“1 
min ! 
βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1 
) 
loooooooooooooooooooooooooooomoooooooooooooooooooooooooooon 
I 
` 8H logNVpϵq a 
2HK logpH{δq, 
where the first inequality holds due to Lemma 3.8.17, the second inequality holds due to 
Definition 3.3.5, and the last inequality holds due to Lemma 3.8.18. For the term I, we 
further have 
K ÿ 
k“1 
H ÿ 
h“1 
min ! 
βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1 
) 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
min ! 
CβEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1 
) 
ď 
H ÿ 
h“1 
p1 ` CβEγ2 q dimα,KpFhq ` 2CβE 
H ÿ 
h“1 
b 
dimα,KpFhq 
g 
f 
f 
e 
K ÿ 
k“1 
pσ2 k,h ` α2q 
ď Hp1 ` CβEγ2 q dimα,KpFq ` 2CβE 
g 
f 
f 
e 
H ÿ 
h“1 
dimα,KpFhq 
g 
f 
f 
e 
K ÿ 
k“1 
H ÿ 
h“1 
pσ2 k,h ` α2q 
ď Hp1 ` CβEγ2 q dimα,KpFhq ` 2CβE 
b 
dimα,KpFq 
g 
f 
f 
eH K ÿ 
k“1 
H ÿ 
h“1 
pσ2 k,h ` α2q, 
121
where the first inequality holds due to Definition 3.3.5, the second inequality holds due to 
Lemma 3.8.14, the third inequality holds due to Cauchy-Schwarz inequality. Therefore, we 
can get 
K ÿ 
k“1 
H ÿ 
h“1 
σ2 k,h ď 24H2 logNVpϵqp1 ` CβEγ2 
q dimα,KpFhq 
` 48CH logNVpϵqβE b 
dimα,KpFq 
g 
f 
f 
eH K ÿ 
k“1 
H ÿ 
h“1 
pσ2 k,h ` α2q 
` 8H logNVpϵq a 
2HK logpH{δq. 
Since x ď a ? x ` b implies x ď a2 ` 2b, taking α “ 1{ 
? H, we have that 
K ÿ 
k“1 
H ÿ 
h“1 
σ2 k,h ď 2304C2H3 
plogNVpϵqq 2 pβE 
q 2 dimα,KpFq 
` 48H2 logNVpϵqp1 ` CβEγ2 q dimα,KpFhq 
` 16H logNVpϵq a 
2HK logpH{δq ` K. 
Proof of Lemma 3.8.16. We prove this statement by induction. Note that Ṽ ˚ H`1ps; rkq “ 
Vk,H`1psq “ 0. Assume that the statement holds for h`1. If Vk,hpsq “ 1, then the statement 
holds trivially for h; otherwise, we have for any ps, aq P S ˆ A that 
Q̂k,hps, aq ´ Q̃˚ hps, a; rkq ě f̂k,hps, aq ` bk,hps, aq ´ rrk,hps, a; rq ` PhV 
˚ h`1ps, a; rqs 
“ rf̂k,hps, aq ´ rk,hps, a; rq ´ PhVk,h`1ps, a; rqs ` bk,hps, aq 
` PhVk,h`1ps, a; rq ´ PhV ˚ h`1ps, a; rq 
ě rf̂k,hps, aq ´ rk,hps, a; rq ´ PhVk,h`1ps, a; rqs ` bk,hps, aq 
ě ´βEDFh pz; zrKs,h, σ̄rKs,hq ` 2βEDFh 
pz; zrKs,h, σ̄rKs,hq 
ě 0, 
122
where the first inequality holds due to Definition 3.8.1, the second inequality holds due 
to induction hypothesis, the third inequality holds due to Lemma 3.8.17, and the forth 
inequality holds due to Definition 3.3.5. 
3.8.4 Proof of Lemmas in Section 3.8.3 
Proof of Lemma 3.8.17. According to the definition of D2 F function, we have 
` 
f̂k,hps, aq ´ ThVk,h`1ps, aq ˘2 
ď D2 Fh 
pz; zrk´1s,h, σ̄rk´1s,hq ˆ 
ˆ 
λ ` 
k´1 ÿ 
i“1 
1 
pσ̄i,hq2 
´ 
f̂k,hpsih, a i hq ´ ThVk,h`1psih, a 
i hq 
¯2 ˙ 
ď pβE q 2 
ˆ D2 Fh 
pz; zrk´1s,h, σ̄rk´1s,hq, 
where the first inequality holds due the definition of D2 F function with the Assumption 3.3.2 
and the second inequality holds due to the events EE h . Thus, we have 
ˇ 
ˇf̂k,hps, aq ´ ThVk,h`1ps, aq ˇ 
ˇ ď βEDFh pz; zrk´1s,h, σ̄rk´1s,hq. 
Proof of Lemma 3.8.18. By Lemma 3.8.21, we have K ÿ 
k“1 
H ÿ 
h“1 
PhVk,h`1ps k h, a 
k hq “ 
K ÿ 
k“1 
H ÿ 
h“1 
Vk,h`1ps k h`1q ` 
K ÿ 
k“1 
H ÿ 
h“1 
pPhVk,h`1ps k h, a 
k hq ´ Vk,h`1ps 
k h`1qq 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
Vk,h`1ps k h`1q ` 
a 
2KH logp1{δq. 
Then, under event EE, we have 
Vk,hpskhq “ Qk,hpskh, a k hq 
“ mintf̂k,hpskh, a k hq ` 2βEDFh 
pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1u 
ď mintPhVk,h`1pskh, a k hq ` 4βEDFh 
pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1u 
“ mint1, Vk,h`1ps k hq ` pPhVk,h`1ps 
k h, a 
k hq ´ Vk,h`1pskhqq 
` 4βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hqu, 
123
where the inequality holds due to Lemma 3.8.17 and Definition 3.3.5. Therefore, for fixed h, 
we have 
K ÿ 
k“1 
Vk,hpskhq ď 
K ÿ 
k“1 
min ! 
H ÿ 
h1“h 
“ 
4βEDFh1 pzk,h1 ; zrk´1s,h1 , σ̄rk´1s,h1q 
` pPhVk,h1`1ps k h1 , akh1q ´ Vk,h1`1ps 
k h1qq 
‰ 
, 1 ) 
ď 
K ÿ 
k“1 
H ÿ 
h1“h 
min ! 
4βEDFh1 pzk,h1 ; zrk´1s,h1 , σ̄rk´1s,h1q, 1 ) 
` 
K ÿ 
k“1 
H ÿ 
h1“h 
pPhVk,h1`1ps k h1 , akh1q ´ Vk,h1`1ps 
k h1qq 
ď 
K ÿ 
k“1 
H ÿ 
h1“h 
min ! 
4βEDFh1 pzk,h1 ; zrk´1s,h1 , σ̄rk´1s,h1q, 1 ) 
` a 
2HK logp1{δq, 
where the first inequality holds due to induction, and the last inequality holds due to 
Lemma 3.8.21. Hence, by combining the above two inequalities, we have 
K ÿ 
k“1 
H ÿ 
h“1 
PhVk,h`1ps k h, a 
k hq 
ď 
K ÿ 
k“1 
H ÿ 
h“1 
Vk,h`1pskh`1q ` a 
2KH logp1{δq 
ď H K ÿ 
k“1 
H ÿ 
h“1 
min ! 
4βEDFh pzk,h; zrk´1s,h, σ̄rk´1s,hq, 1 
) 
` pH ` 1q a 
2HK logp1{δq. 
3.8.5 Auxiliary Lemmas 
Lemma 3.8.19 (Self-normalized bound for scalar-valued martingales). Consider random 
variables pvn|n P Nq adapted to the filtration pHn : n “ 0, 1, ...q. Let tηiu 8 i“1 be a sequence of 
real-valued random variables which is Hi`1-measurable and is conditionally σ-sub-Gaussian. 
Then for an arbitrarily chosen λ ą 0, for any δ ą 0, with probability at least 1 ´ δ, it holds 
124
that 
n ÿ 
i“1 
ηivi ď λσ2 
2 ¨ 
n ÿ 
i“1 
v2i ` logp1{δq{λ @n P N. 
Lemma 3.8.20 (Corollary 2, Agarwal et al. (2022)). Let M ą 0, V ą v ą 0 be constants, 
and txiuiPrts be stochastic process adapted to a filtration tHiuiPrts. Suppose Erxi|Hi´1s “ 
0, |xi| ď M and ř 
iPrts Erx2 i |Hi´1s ď V 2 almost surely. Then for any δ, ϵ ą 0, let ι “ 
b 
log p2 logpV {vq`2q¨plogpM{mq`2q 
δ we have 
P 
˜ 
ÿ 
iPrts 
xi ą ι 
g 
f 
f 
e2 
ˆ 
2 ÿ 
iPrts 
Erx2 i |Hi´1s ` v2 
˙ 
` 2 
3 ι2 ˆ 
2max iPrts 
|xi| ` m 
˙ 
¸ 
ď δ. 
Lemma 3.8.21 (Azuma-Hoeffding Inequality). Let txiu n i“1 be a martingale difference se-
quence with respect to a filtration tGiu n`1 i“1 such that |xi| ď M almost surely. That is, xi is 
Gi`1-measurable and Erxi|Gis a.s. Then for any 0 ă δ ă 1, with probability at least 1 ´ δ, 
n ÿ 
i“1 
xi ď M a 
2n logp1{δq. 
3.9 Experiment details 
3.9.1 Details of exploration algorithm 
We present the practical algorithm in this subsection. We start by introducing the notation 
ϕi as the parameter for the i-th Q networks, which is a three-layer MLP with 1024 hidden 
size, same as other benchmark algorithms implemented in URLB (Laskin et al., 2021). For 
the ease of presentation, we ignore the Q network as Qϕi as Qi and the target network 
Qϕ̄i as Q̄i when there is no confusion. We initialize the parameters in ϕi using Kaiming 
distribution (He et al., 2015). 
The algorithm works in the discounted MDP with the discounted factor γ. For each t in 
training steps, the algorithm updates the t%N -th Q function by taking the gradient descent 
125
Algorithm 8 GFA-RFE – Exploration Phase – Implementation Input: Number of ensemble N , update speed η, exploration step T , (reward-free) environ-
ment env, 
Input: Action variance σ2, minibatch size B, exploration bonus β, discount factor γ 
1: For all i P rN s, initialize ϕi, let ϕ̄i Ð ϕi 
2: Initialize policy network πθ, replay buffer D “ H 
3: Observe initial state s1 
4: for t “ 1, ¨ ¨ ¨ , T do 
5: Sample ζ „ Unif.r0, 1s, sample at „ 
! 
Npπp¨|stq, σ 2q if ζ ď 1 ´ ϵ else Unif.pAq 
) 
6: Observe st`1, let D Ð D Y pst, at, st`1q 
7: If env.done, restart env and observe initial state st`1 
8: Sample a minibatch B “ tps, a, s1qu Ď D with size B 
9: For each ps, a, s1q triplet, calculate σ2ps, aq, rintps, aq, bps, aq according to (3.9.2). 
10: Update Q-network Qt%N by taking one step minimizing Lpϕt%Nq according to (3.9.1) 
11: Update actor πθp¨|sq by taking one step maximizing Lpθq according to (3.9.4) 
12: Update target Q-network following (3.9.3) 
13: end for 
regarding the loss function 
Lpϕt%Nq “ ÿ 
ps,a,s1qPB 
1 
σ2ps, aq 
ˆ 
Qt%Nps, aq ´ 
´ 
rintps, aq ` γQtargetps, aq ` bps, aq 
¯ 
˙2 
, (3.9.1) 
where the target Q function is the average of N target Q network, i.e., Qtargetps, aq “ 
ř 
iPrNs Q̄ips, aq{N , B is the minibatch randomly sampled from replay buffer D. We encourage 
the diversity of different Q function by using different batch B for updating different Q 
functions. As the key components of our algorithm, weighted regression σ2ps, aq; intrinsic 
reward rintps, aq, exploration bonus bps, aq is calculated based on the variance of the target 
126
Algorithm 9 GFA-RFE – Planning Phase – Implementation (DDPG) Input: Update speed η, training K, environment env, reward function rp¨, ¨q 
Input: Action variance σ2, minibatch size B, discount factor γ, offline training data D 
1: Initialize ϕ, let ϕ̄ Ð ϕ 
2: Initialize policy network πθ 
3: Update every ps, a, s1q in D to ps, a, s1, rps, aqq 
4: for k “ 1, ¨ ¨ ¨ , K do 
5: Sample a minibatch B “ tps, a, s1, rps, aqqu Ď D 
6: Calculate Lpϕq “ ř 
ps,a,s1qPB 
ˆ 
Qϕps, aq ´ 
´ 
rps, aq ` γQtargetps 1, πθps1qq 
¯ 
˙2 
7: Update Q-network Qt%N by taking one step minimizing Lpϕq 
8: Calculate actor loss Lpθq “ ř 
ps,a,s1qPB Qϕps, πθpa|sqq 
9: Update actor πθp¨|sq by taking one step maximizing Lpθq 
10: Update target Q-network by ϕ̄ Ð p1 ´ ηqϕ̄` ηϕ 
11: end for 
Q network across Q̄i instances: 
σ2 ps, aq “ VarrQ̄ips, aqs; rintps, aq “ p1 ´ γq 
b 
VarrQ̄ips, aqs; bps, aq “ β b 
VarrQ̄ips, aqs, 
(3.9.2) 
where we simply set β “ 1 to align with our theory, the factor p1 ´ γq before the intrinsic 
reward is because we want to balance the horizon 1{H « p1 ´ γq in the setting. The reason 
for choosing the target Q function Q̄i instead of the updating Q function is to update the 
intrinsic reward, exploration bonus slower than the update of Q function, therefore give the 
agent more time to explore the optimal policy for maximizing a certain intrinsic reward 
rintps, aq. After updating the parameter ϕt%N , we perform a soft update for the target 
network as 
ϕ̄t%N Ð p1 ´ ηqϕ̄t%N ` ηϕt%N , (3.9.3) 
where we follow the setting in URLB to set η “ 0.01. After updating the Q function, the 
127
algorithm then updates the actor πθpa|sq following DDPG in maximizing 
Lpθq “ ÿ 
ps,a,s1qPB 
ÿ 
iPrNs 
Qips, πθpa|sqq (3.9.4) 
We summarize the exploration algorithm in Algorithm 8, in particular, we use Adam to 
optimize the loss function defined by (3.9.1) and (3.9.3). 
3.9.2 Details of offline training algorithm 
After collecting the dataset D, we call a reward oracle to label the reward r for any triplet 
ps, a, s1q P D. Then the DDPG algorithm is called to learn the optimal policy. For the 
fair comparison with other benchmark algorithm, we do not add weighted regression in the 
planning phase, thus the algorithm stays the same with the one presented in URLB, as stated 
in Algorithm 9 
3.9.3 Hyper-parameters 
We present a common set of hyper-parameters used in our experiments in Table 3.2. And we 
list individual hyper-parameters for each method in table 3.3. All common hyper-parameters 
and individual hyper-parameters for baseline algorithms are the same as what is used in 
Laskin et al. (2021) and its implementations. 
3.9.4 Ablation Study 
3.9.4.1 Learning Processes 
Figure 3.2 illustrate the episode rewards for each algorithm across training steps for various 
tasks, demonstrating that the performance of our algorithm (Algorithm 6) ranks among the 
top tier in all tasks. 
128
Table 3.2: The common set of hyper-parameters. 
Hyper-parameter Value 
Replay buffer capacity 106 
Action repeat 1 
n-step returns 3 
Mini-batch size 1024 
Discount (γ) 0.99 
Optimizer Adam 
Learning rate 10´4 
Agent update frequency 2 
Critic target EMA rate (τQ) 0.01 
Features dim. 50 
Hidden dim. 1024 
Exploration stddev clip 0.3 
Exploration stddev value 0.2 
# frames per episode 1 ˆ 103 
# online exploration frames up to 1 ˆ 106 
# offline planning frames 1 ˆ 105 
Critic network p|O| ` |A|q Ñ 1024 Ñ LN Ñ Tanh Ñ 1024 Ñ RELU Ñ 1 
Actor network |O| Ñ 50 Ñ LN Ñ Tanh Ñ 1024 Ñ RELU Ñ action dim 
3.9.4.2 Numbers of Exploration Episodes 
Figure 3.3 show the episode rewards for top-performing algorithms, including our algorithm 
(GFA-RFE), RND, Disagreement, and APT, across varying numbers of exploration episodes 
for different tasks. Notably, GFA-RFE competes with these leading unsupervised algorithms 
effectively, matching their performance across a range of exploration episodes. 
129
Table 3.3: Hyper-parameters of for GFA-RFE and baseline (ICM, Disagreement, RND). 
GFA-RFE Value 
Ensemble size 10 
Exploration bonus 2 
Exploration ϵ 0.2 
ICM hyper-parameter Value 
Reward transformation logpr ` 1.0q 
Forward net arch. p|O| ` |A|q Ñ 1024 Ñ 1024 Ñ |O| ReLU MLP 
Inverse net arch. p2 ˆ |O|q Ñ 1024 Ñ |A| ReLU MLP 
Disagreement hyper-parameter Value 
Ensemble size 5 
Forward net arch: p|O| ` |A|q Ñ 1024 Ñ 1024 Ñ |O| ReLU MLP 
RND hyper-parameter Value 
Representation dim. 512 
Predictor & target net arch. |O| Ñ 1024 Ñ 1024 Ñ 512 ReLU MLP 
Normalized observation clipping 5 
130
Table 3.4: Hyper-parameters of for baseline algorithms (APT, SMM, DIAYN, APS). 
APT hyper-parameter Value 
Representation dim. 512 
Reward transformation logpr ` 1.0q 
Forward net arch. p512 ` |A|q Ñ 1024 Ñ 512 ReLU MLP 
Inverse net arch. p2 ˆ 512q Ñ 1024 Ñ |A| ReLU MLP 
k in NN 12 
Avg top k in NN True 
SMM hyper-parameter Value 
Skill dim. 4 
Skill discrim lr 10´3 
VAE lr 10´2 
DIAYN hyper-parameter Value 
Skill dim 16 
Skill sampling frequency (steps) 50 
Discriminator net arch. 512 Ñ 1024 Ñ 1024 Ñ 16 ReLU MLP 
APS hyper-parameter Value 
Reward transformation logpr ` 1.0q 
Successor feature dim. 10 
Successor feature net arch. |O| Ñ 1024 Ñ 10 ReLU MLP 
k in NN 12 
Avg top k in NN True 
Least square batch size 4096 
131
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
100 
200 
300 
400 
500 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on walker-flip 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(a) Walker-Flip 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
50 
100 
150 
200 
250 
300 
350 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on walker-run 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(b) Walker-Run 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
100 
200 
300 
400 
500 
600 
700 
800 
900 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on walker-stand 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(c) Walker-Stand 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
0 
200 
400 
600 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on walker-walk 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(d) Walker-Walk 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
100 
200 
300 
400 
500 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on quadruped-run 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(e) Quadruped-Run 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
100 
200 
300 
400 
500 
600 
700 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on quadruped-jump 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(f) Quadruped-Jump 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
200 
300 
400 
500 
600 
700 
800 
900 
1000 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on quadruped-stand 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(g) Quadruped-Stand 
0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 Training Step 
100 
200 
300 
400 
500 
600 
700 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward at different training steps on quadruped-walk 
aps diayn disagreement icm icm_apt rnd smm gfa-rfe (Ours) 
(h) Quadruped-Walk 
Figure 3.2: Episode reward at different training steps for tasks on walker and quadruped. 
132
100 500 1000 Exploration Episodes 
200 
300 
400 
500 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on walker-flip 
icm_apt disagreement rnd gfa-rfe (Ours) 
(a) Walker-Flip 
100 500 1000 Exploration Episodes 
50 
100 
150 
200 
250 
300 
350 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on walker-run 
icm_apt disagreement rnd gfa-rfe (Ours) 
(b) Walker-Run 
100 500 1000 Exploration Episodes 
400 
500 
600 
700 
800 
900 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on walker-stand 
icm_apt disagreement rnd gfa-rfe (Ours) 
(c) Walker-Stand 
100 500 1000 Exploration Episodes 
100 
200 
300 
400 
500 
600 
700 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on walker-walk 
icm_apt disagreement rnd gfa-rfe (Ours) 
(d) Walker-Walk 
100 500 1000 Exploration Episodes 
150 
200 
250 
300 
350 
400 
450 
500 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on quadruped-run 
icm_apt disagreement rnd gfa-rfe (Ours) 
(e) Quadruped-Run 
100 500 1000 Exploration Episodes 
200 
300 
400 
500 
600 
700 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on quadruped-jump 
icm_apt disagreement rnd gfa-rfe (Ours) 
(f) Quadruped-Jump 
100 500 1000 Exploration Episodes 
400 
500 
600 
700 
800 
900 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on quadruped-stand 
icm_apt disagreement rnd gfa-rfe (Ours) 
(g) Quadruped-Stand 
100 500 1000 Exploration Episodes 
200 
300 
400 
500 
600 
700 
800 
Ep iso 
de  R 
ew ar 
d 
Episode Reward with Different Number of Exploration Episodes on quadruped-walk 
icm_apt disagreement rnd gfa-rfe (Ours) 
(h) Quadruped-Walk 
Figure 3.3: Episode reward with different exploration episodes on walker and quadruped. 
133
CHAPTER 4 
Uncertainty-Aware Robust Linear Contextual Bandits 
4.1 Introduction 
Figure 4.1: An illustration of 
the recommender system. 
From this chapter, we move on to the second topic: how 
to design robust decision making systems by leveraging the 
uncertainty quantification. In this chapter, we start from 
(linear) contextual bandits. A contextual bandit is a task 
in which, in each round, the agent observes a set of con-
textual vectors describing the features of different actions. 
The agent needs to select the action that has the maximum 
reward, where the reward can be viewed as a function of the 
contextual vectors. For example, in a recommender system 
as demonstrated in Figure 4.11. For each round, the agent 
observes different possible choices of food. These choices are described in terms of their 
category, calories, or style as the contextual vector (feature) of the foods. The goal for the 
agent is to select a type of food that the user is most likely to eat and then recommend it 
to the user. The reward is 1 when the user picks the recommendation and 0 otherwise and 
can be viewed as a function of the contextual vectors with some noise. It is obvious that 
the contextual bandit task can be viewed as the most simplified reinforcement learning tasks 
with only one decision step instead of making sequential decision that may affect each other. 
1Image credit: https://www.nvidia.com/en-us/glossary/recommendation-system 
134
Linear contextual bandits (Li et al., 2010; Chu et al., 2011; Abbasi-Yadkori et al., 2011; 
Agrawal and Goyal, 2013) have been extensively studied when the reward function can be 
represented as a linear function of the contextual vectors. However, such a well-specified 
linear model assumption sometimes does not hold in practice. This motivates the study of 
misspecified linear models. In particular, we only assume that the reward function can be 
approximated by a linear function up to some worst-case error ζ called the misspecification 
level. Existing algorithms for misspecified linear contextual bandits (Lattimore et al., 2020; 
Foster et al., 2020) can only achieve an Õpd ? K ` ζK 
? d logKq regret bound, where K is 
the total number of rounds and d is the dimension of the contextual vector. Such a regret, 
however, suggests that the performance of these algorithms will degenerate to be linear in 
K when K is sufficiently large. The reason for this performance degeneration is because 
existing algorithms, such as OFUL (Abbasi-Yadkori et al., 2011) and linear Thompson sam-
pling (Agrawal and Goyal, 2013), utilize all the collected data without selection. This makes 
these algorithms vulnerable to “outliers” caused by the misspecified model. Meanwhile, the 
aforementioned results do not consider the sub-optimality gap in the expected reward be-
tween the best arm and the second best arm. Intuitively speaking, if the sub-optimality 
gap is smaller than the misspecification level, there is no hope to obtain a sublinear re-
gret. Therefore, it is sensible to take into account the sub-optimality gap in the misspecified 
setting, and pursue a gap-dependent regret bound. 
The same misspecification issue also appears in reinforcement learning with linear func-
tion approximation, when a linear function cannot exactly represent the transition kernel 
or value function of the underlying MDP. In this case, Du et al. (2019) provided a negative 
result showing that if the misspecification level is larger than a certain threshold, any RL 
algorithm will suffer from an exponentially large sample complexity. This result was later 
revisited in the stochastic linear bandit setting by Lattimore et al. (2020), which shows that 
a large misspecification error will make the bandit model not efficiently learnable. However, 
these results cannot explain the tremendous success of deep reinforcement learning on vari-
135
ous tasks (Mnih et al., 2013; Schulman et al., 2015, 2017), where the deep neural networks 
are used as function approximators with misspecification error. 
4.1.1 Organization of this Chapter 
In this chapter, we aim to understand the role of model misspecification in linear contextual 
bandits through the lens of suboptimality gap. This chapter is organized as follows. We 
present the related works in Section 4.2 and the preliminaries in Section 4.3. In Section 4.4, 
we propose and analyze a new algorithm with data selection, which can handle misspeci-
fied bandits with the knowledge of sub-optimality gap ∆. In Section 4.5, we move on to 
eliminating the dependence of the knowledge of ∆ and show that the existing algorithm, 
SupLinUCB (Chu et al., 2011) can be also viewed as a bootstrapped version of our proposed 
algorithm. Empirical results are presented in Section 4.7 and the conclusion is drawn in 
Section 4.8. We defer the detailed proof for several key lemmas to Section 4.9. 
4.2 Related Works 
In this section, we review the related work for misspecified linear bandits and misspecified 
reinforcement learning. 
4.2.1 Linear Contextual Bandits 
There is a large body of literature on linear contextual bandits. For example, Auer (2002); 
Chu et al. (2011); Agrawal and Goyal (2013) studied linear contextual bandits when the 
number of arms is finite. Abbasi-Yadkori et al. (2011) proposed an algorithm called OFUL 
to deal with the infinite arm set. All these works come with an Õp ? Kq problem-independent 
regret bound, and an Opd2∆´1 logpKqq gap-dependent regret bound is also given by Abbasi-
Yadkori et al. (2011). 
136
4.2.2 Misspecified Linear Bandits. 
There is a long history of the robust contextual bandits in the face of misspecification. 
Agarwal et al. (2014) considered using an oracle to learn the contextual bandits with function 
approximation and showed that the proposed algorithm is robust when misspecification 
exists. Ghosh et al. (2017) considered the misspecified linear bandits and showed that the 
OFUL (Abbasi-Yadkori et al., 2011) algorithm cannot achieve a sublinear regret in the 
presence of misspecification. They, therefore, proposed a new algorithm with a hypothesis 
testing module for linearity to determine whether to use OFUL (Abbasi-Yadkori et al., 
2011) or the multi-armed UCB algorithm. Their algorithm enjoys the same performance 
guarantee as OFUL in the well-specified setting and can avoid the linear regret under certain 
misspecification setting. Lattimore et al. (2020) proposed a phase-elimination algorithm for 
misspecified stochastic linear bandits, which achieves an Õp ? dK`ζK 
? dq regret bound. For 
contextual linear bandits, both Lattimore et al. (2020) and Foster et al. (2020) proved an 
Õpd ? K ` ζK 
? dq regret bound under misspecification. Takemura et al. (2021) showed that 
SupLinUCB can achieve a similar regret bound without the knowledge of the misspecification 
level. Van Roy and Dong (2019) proved a lower bound of sample complexity, which suggests 
when ζ ? d ě 
a 
8 log |D|, any best arm identification algorithm will suffer a Ωp2dq sample 
complexity, where D is the decision set. When the reward is deterministic and does not 
contain noise, they provided an algorithm using Õpdq sample complexity to identify a ∆-
optimal arm when ζ ď ∆{ ? d. Lattimore et al. (2020) also mentioned that if ζ 
? d ď ∆, there 
exists a best arm identification algorithm that only needs to pull Õpdq arms to find a ∆-
optimal arm with the knowledge of ζ. Note that although the exponential sample complexity 
lower bound for best-arm identification can be translated into a regret lower bound in linear 
contextual bandits, the algorithms for best-arm identification and the corresponding upper 
bounds cannot be easily extended to linear contextual bandits. Besides these works on 
misspecification, He et al. (2022b) studied the linear contextual bandits with adversarial 
corruptions, where the reward for each round can be corrupted arbitrarily. They assumed 
137
Algorithm Misspecified MDP? Result 
LSVI-UCB (He et al., 2021a) ˆ Õpd3H5∆´1 logpKqq 
LSVI-UCB (Papini et al., 2021a) ˆ Õpd3H5∆´1 logp1{λqq 
Cert-LSVI-UCB (ours, Theorem 4.4.1) ✓ Õpd3H5∆´1q 
Table 4.1: Instance-dependent regret bounds for different algorithms under the linear MDP 
setting. Here d is the dimension of the linear function ϕps, aq, H is the horizon length, ∆ 
is the minimal suboptimality gap. All results in the table represent high probability regret 
bounds. The regret bound depends the number of episodes K in He et al. (2021a) and the 
minimum positive eigenvalue λ of features mapping in Papini et al. (2021b). Misspecified 
MDP? indicates if the algorithm can (✓) handle the misspecified linear MDP or not (ˆ). 
that the summation of the corruption up to K rounds is bounded by C ą 0 and proposed 
an algorithm achieving Õpd ? K `dCq regret bound with the known C. Since the corruption 
level C “ Kζ in the misspecification setting, their result directly implied an Opd ? K `dKζq 
linear regret, which differs from the optimal guarantee with a extra Op ? dq factor. Besides 
these series of work, Camilleri et al. (2021) also studied the robustness of kernel bandits with 
misspecification. 
4.3 Preliminaries 
We consider a linear contextual bandit problem. In round k P rKs, the agent receives a 
decision set Dk Ă Rd and selects an arm xk P Dk then observes the reward rk “ rpxkq ` εk, 
where rp¨q : Rd ÞÑ r0, 1s is a deterministic expected reward function and εk is a zero-mean 
R-sub-Gaussian random noise. i.e., Ereλεk |x1:k, ε1:k´1s ď exppλ2R2{2q, @k P rKs, λ P R. 
In this work, we assume that all contextual vector x P Dk satisfies }x}2 ď L and the 
reward function rp¨q : Rd Ñ r0, 1s can be approximated by a linear function rpxq “ xJθ˚ ` 
138
ηpxq, where ηp¨q : Rd ÞÑ r´ζ, ζs is an unknown misspecification error function. We further 
assume }θ˚}2 ď B and for simplicity, we assume B,L ě 1. We denote the optimal reward 
at round k as r˚ k “ maxxPDk 
rpxq and the optimal arm x˚ k “ argmaxxPDk 
rpxq. Our goal is to 
minimize the regret defined by RegretpKq :“ řK 
k“1 r ˚ k ´ rpxkq. 
We focus on the minimal sub-optimality gap condition. 
Definition 4.3.1 (Minimal sub-optimality gap). For each x P Dk, the sub-optimality gap 
∆kpxq is defined by ∆kpxq :“ r˚ k ´ rpxq and the minimal sub-optimality gap ∆ is defined by 
∆ :“ minkPrKs,xPDk t∆kpxq : ∆kpxq ą 0u. 
Then we further assume this minimal sub-optimality gap is strictly positive, i.e., ∆ ą 0. 
4.4 Constant Regret Bound with Known Sub-Optimality Gap 
4.4.1 Proposed Algorithm 
In this subsection, we propose our algorithm, DS-OFUL, in Algorithm 10. The algorithm 
runs for K rounds. At each round, the algorithm first estimates the underlying parameter 
θ˚ by solving the following ridge regression problem in Line 4 
θk “ argminθ 
ř 
iPCk´1 
` 
ri ´ xJ i θ 
˘2 ` λ}θ}22, 
where Ck´1 is the index set of the selected contextual vectors for regression and is initialized as 
an empty set at the beginning. After receiving the contextual vectors set Dk, the algorithm 
selects an arm from the optimistic estimation powered by the Upper Confidence Bound 
(UCB) bonus in Line 6. In line 8, the algorithm adds the index of current round into Ck if 
the UCB bonus of the chosen arm xk, denoted by }xk}U´1 k 
, is greater than the threshold Γ. 
Intuitively speaking, since the UCB bonus reflects the uncertainty of the model about the 
given arm x, Line 8 discards the data that brings little uncertainty (}x}U´1 k 
) to the model. 
Finally, we denote the total number of selected data in Line 8 by |CK |. We will declare the 
choices of the parameter Γ, β and λ in the next section. 
139
Algorithm 10 Data Selection OFUL (DS-OFUL) Input: Threshold Γ, radius β and regularizer λ 
1: Initialize C0 “ H,U0 “ λI,θ0 “ 0 
2: for k “ 1, . . . , K do 
3: Set Uk “ λI ` ř 
iPCk´1 xix 
J i . 
4: Set θk “ U´1 k 
ř 
iPCk´1 rixi. 
5: Receive the decision set Dk. 
6: Select xk “ argmaxxPDk 
␣ 
xJθk ` β}x}U´1 k 
( 
. 
7: Receive reward rk 
8: if }xk}U´1 k 
ě Γ then Ck “ Ck´1 Y tku else Ck “ Ck´1 
9: end for 
4.4.2 Regret Bound 
In this subsection, we provide the regret upper bound of Algorithm 10 and the regret lower 
bound for learning the misspecified linear contextual bandit. 
Theorem 4.4.1 (Upper Bound). For any 0 ă δ ă 1, let λ “ B´2 and Γ “ ∆{p2 ? dι1q where 
ι1 “ p24 ` 18Rq logpp72 ` 54RqLB ? d∆´1q ` 
a 
8R2 logp1{δq. Set β “ 1 ` 4 ? dι2 ` R 
? 2dι3 
where ι2 “ logp3LBΓ´1q, ι3 “ logpp1 ` 16L2B2Γ´2ι2q{δq. If the misspecification level is 
bounded by 2 ? dζι1 ď ∆, then with probability at least 1 ´ δ, the cumulative regret of 
Algorithm 10 is bounded by 
RegretpKq ď 32β 
a 
2d3ι2 logp1 ` 16dΓ´2ι2qι1 ∆ 
. 
Remark 4.4.2. Since β “ Õp ? dq, Theorem 4.4.1 suggests an Õpd2∆´1q constant regret 
bound independent of the total number of rounds K when ζ ď Õp∆{ ? dq, which improves 
the logarithmic regret Õpd2∆´1 logKq in Abbasi-Yadkori et al. (2011) to a constant regret2. 
Note that our constant regret bound relies on the knowledge of the minimal sub-optimality 
2When we say constant regret, we ignore the logp1{δq factor in the regret as we choose δ to be a constant. 
140
gap ∆, while the OFUL algorithm in Abbasi-Yadkori et al. (2011) does not need prior 
knowledge about the minimal sub-optimality gap ∆. 
Remark 4.4.3. Our high probability constant regret bound does not violate the lower bound 
proved in Hao et al. (2020), which says that certain diversity condition on the contexts is 
necessary to achieve an expected constant regret bound (Papini et al., 2021b). Here we only 
provide a high-probability constant regret bound. When extending this high probability 
constant regret bound to expected regret bound, we have 
ErRegretpKqs ď Õpd2∆´1 logp1{δqqp1 ´ δq ` δK, 
which depends on K. To obtain a sub-linear expected regret, we can choose δ “ 1{K, which 
yields a logarithmic regret Õpd2∆´1 logpKqq and does not violate the lower bound in Hao 
et al. (2020). 
Remark 4.4.4. Notably, Papini et al. (2021b) can achieve a constant expected regret bound 
under certain diversity condition, which requires the contexts of arms span the whole Rd 
space. In contrast, our constant regret bound does not need such an assumption and is a 
high-probability constant regret bound. 
4.4.3 Key Proof Techniques 
Here we present the key proof techniques for achieving the constant regret with the knowledge 
of sub-optimality gap ∆. The detailed proof is deferred to Section 4.9.1. 
4.4.3.1 Regret decomposition 
The total regret over all K rounds can be decomposed as follows 
RegretpKq “ ÿ 
kPCK 
` 
r˚ k ´ rpxkq 
˘ 
` ÿ 
kRCK 
` 
r˚ k ´ rpxkq 
˘ 
. (4.4.1) 
141
4.4.3.2 Finite samples collected in Ck 
Since we only adding the contextual arm with large uncertainty (i.e., }x}U´1 k 
ě Γ) into the 
set Ck, we can bound the number of samples in Ck as Ck “ ÕpdΓ´2q which is claimed in the 
following lemma. 
Lemma 4.4.5. Given 0 ă Γ ď 1, set λ “ B´2. For any k P rKs, |Ck| ď 16dΓ´2 logp3LBΓ´1q. 
Then the following lemma suggests that a finite regression set Ck can lead to a small 
confidence set with misspecification. 
Lemma 4.4.6. Let λ “ B´2. For all δ ą 0, with probability at least 1´δ, for all x P Rd, k P 
rKs, the prediction error is bounded by: 
|xJ pθk ´ θ˚ 
q| ď 
´ 
1 ` R ? 2dι ` ζ 
a 
|Ck| 
¯ 
}x}U´1 k , 
where ι “ logppd` |Ck|L2B2q{pdδqq and |Ck| is the total number of data used in regression at 
the k-th round. 
Comparing the confidence radius ÕpR ? d ` ζ 
a 
|Ck|q here with the conventional radius 
ÕpR ? dq in OFUL, one can find that the misspecification error will affect the radius by an 
a 
|CK | factor. If we use all the data to do regression, the confidence radius will be in the 
order of Õp ? Kq and therefore will lead to a OpK 
? logKq regret bound (see Lemma 11 
in Abbasi-Yadkori et al. (2011)). This makes the regret bound vacuous. In contrast, in our 
algorithm, the confidence radius is only a 
|CK | where |CK | is finite given Lemma 4.4.5. As a 
result, our regret bound will not grow with K as in OFUL and will be smaller. 
4.4.3.3 Skipped rounds are optimal 
Given the fact that the selected arm set Ck is finite, the rest of the proof is simply showing that 
the skipped rounds k R Ck are optimal and will not incur regret. Since we have }x}U´1 k 
ď Γ 
for those skipped rounds, the sub-optimality is bounded by the following (informal) lemma. 
142
Lemma 4.4.7. The instantaneous regret for round k R Ck is bounded by 
∆kpxkq ď 2ζ ` 2β}xk}U´1 k 
ď Θ̃pζ ` ∆ ` ? dΓq, 
Setting Γ “ Θ̃p∆{ ? dq suggests that the instantaneous regret ∆kpxkq ď ∆, which means no 
instantaneous regret occurs on round k. 
4.4.3.4 Achieving the constant regret 
To wrap up, as (4.4.1) suggests, for rounds k P CK , we can follow the gap-dependent regret 
analysis in Abbasi-Yadkori et al. (2011) and obtain an Õpd2 logp|CK |q{∆q gap-dependent 
regret bound, which is independent of K according to Lemma 4.4.5. For rounds k R CK , 
Lemma 4.4.7 guarantees a zero instantaneous regret. Putting them together yields the 
claimed constant regret bound. 
4.5 Constant Regret Bound with Unknown Sub-Optimality Gap 
4.5.1 Proposed Algorithm 
Although Algorithm 10 can achieve a constant regret, it requires the knowledge of sub-
optimality gap ∆. To tackle this problem, we propose a new algorithm that does not require 
the knowledge of sub-optimality gap ∆. 
The algorithm is described in Algorithm 11. It inherits the arm elimination method from 
SupLinUCB (Chu et al., 2011). A similar algorithm is also presented for misspecified linear 
bandits in Takemura et al. (2021). 
Algorithm 11 works as follows. At each round k P rKs, the algorithm maintains l levels 
of ridge regression with different set Cl k´1, where the estimation error for the l-th level is 
about βplq2´l (we will prove this in the latter analysis). Then starting from the first level 
l “ 1 and the received decision set Dk, if there exists an arm in the decision set with a 
143
large uncertainty (i.e., }x}pUl kq´1 ě 2´l), the algorithm directly selects that arm (Line 8). 
According to Lemma 4.4.5 in the analysis of DS-OFUL, the number of selected contexts at 
each level should be bounded. If the uncertainty for all arms is smaller than the threshold 
2´l, the algorithm follows the arm elimination rule, which reduces the decision set into 
Dl`1 k “ 
␣ 
x : x P Dl k, r 
l kpxl 
kq ´ rlkpxq ď 3βplq2´l ( 
. (4.5.1) 
Then the algorithm enters the next level l ` 1 until it reaches logpkq-th level as Line 10 
suggests. For the level l ě logpkq, the algorithm directly selects the arm with highest 
optimistic reward on Line 11 and does not add the index k to the regression set Cl k as on 
Line 12 since the uncertainty is small enough. 
Algorithm 11 can be viewed as the multi-level version of Algorithm 10 boosted by the 
peeling technique. Algorithm 11 does not require the knowledge of the sub-optimality gap 
∆: if ∆ is known, one can directly jump to a specific level l∆ “ Õplogpd{∆qq, where 
the prediction error is bounded by 2βpl∆q2´l∆ “ Õp∆q and is sufficient to achieve zero-
instantaneous regret. However, when the ∆ is unknown, Algorithm 11 has to do a grid 
search over 2´1, 2´2, ¨ ¨ ¨ 2´l∆ , ¨ ¨ ¨ and waste some of the samples to learn the first l∆ ´ 1 
levels. We will revisit and compare the difference between these two algorithms in the later 
regret analysis. 
4.5.2 Regret Bound 
This subsection provides the regret upper bound for Algorithm 11. 
Theorem 4.5.1 (Upper Bound). For any 0 ă δ ă 1, let λ “ B´2. For every integer l ą 0, set 
βplq “ 1`R a 
2dι2plq where ι2plq “ logppd2l ` 16L2B28lι1plqq{pdδqq and ι1plq “ log ` 
3LB2l ˘ 
. 
If the misspecification level is bounded by 4l∆ζ ´ 
1 ` 4 a 
dι1pl∆q 
¯ 
ă ∆ where l∆ is the minimal 
solution to l∆ ą logp8βpl∆q{∆q, then with probability at least 1 ´ δ, the cumulative regret 
144
Algorithm 11 SupLinUCB Input: Regularization λ, confidence radius βp¨q 
1: Initialize Cl 0 “ H for all l P rrlogpKqss 
2: for k “ 1, 2, ¨ ¨ ¨K do 
3: Set D1 k “ Dk and l “ 1 
4: repeat 
5: Set Ul k “ λI ` 
ř 
iPCl k´1 
xix J i , θlk “ pUl 
kq´1 ř 
iPCl k´1 
rixi 
6: Set rlkpxq “ xJθlk ` βplq }x} pUl 
kq´1 , action xl k “ argmaxxPDl 
k rlkpxq 
7: if maxxPDl k 
}x} pUl 
kq´1 ě 2´l then 
8: Choose xk “ argmaxxPDl k 
}x} pUl 
kq´1 
9: Update Cl k “ Cl 
k´1 Y tku and keep Cl1 
k “ Cl1 
k´1 for all l1 ‰ l 
10: else if k ď 4ld then 
11: Choose xk “ xl k 
12: Keep Cl1 
k “ Cl1 
k´1 for all l1 ě 1 
13: else 
14: Set Dl`1 k according to (4.5.1) and increase l “ l ` 1 
15: end if 
16: until xk is chosen and then receive reward rk 
17: end for 
of Algorithm 10 is bounded by 
RegretpKq ď 214dβ2pl∆qι1pl∆q 
∆ . 
Remark 4.5.2. Since βplq “ Õp ? dlq and l∆ “ Õplogpd{∆qq, Theorem 4.5.1 suggests that 
SupLinUCB enjoys a constant regret bound Õpd2∆´1q when ζ ď Õp∆{ ? dq, which is inde-
pendent of the total number of rounds K. Note that in Algorithm 11, the choices of λ and 
βl do not depend on the sub-optimality gaps ∆ and misspecification level ζ. 
Remark 4.5.3. When ζ ě ∆{ ? d, it is hard to provide a gap-dependent regret bound 
145
due to the large misspecification level ζ. However, a gap-independent regret bound of 
Õp ? dK ` 
? dζK logpKqq is proved in Takemura et al. (2021), which suggests the perfor-
mance of SupLinUCB algorithm will not significantly decrease when the condition on mis-
specification does not hold. 
Remark 4.5.4. Comparing the constant factors of DS-OFUL (Algorithm 10) and SupLin-
UCB (Algorithm 11) on the dominating terms Õpβ2d{∆q, one can find that the constant 
factors of SupLinUCB is significantly larger than DS-OFUL. This is because it takes more 
samples to learn the first l∆ ´ 1 levels in SupLinUCB while DS-OFUL directly learns the 
l∆-th level. Therefore, despite having the same order of constant regret bound (in big-O 
notation), one can expect that SupLinUCB has a worse performance than DS-OFUL (when 
∆ is known or can be estimated by grid search). 
4.5.3 Key Proof Techniques 
Here we provide additional proof techniques besides the techniques discussed in Section 4.4.3. 
First of all, Lemmas 4.4.5 and 4.4.6, which are built on a single level selected by }x}U´1 k 
ě Γ, 
can be generalized to the following lemmas for all levels l. The detailed proof are deferred 
to Section 4.9.3. 
Lemma 4.5.5. Set λ “ B´2, for any k P rKs and l ą 0, |Cl k| ď 16d4lι1plq, where ι1plq “ 
log ` 
3LB2l ˘ 
. 
Lemma 4.5.6. Set λ “ B´2. For any level l ą 0, for any δ ą 0, with probability at least 
1 ´ δ, for all k P rKs, the prediction error is bounded by 
ˇ 
ˇxJ pθlk ´ θ˚ 
q ˇ 
ˇ ď 
ˆ 
1 ` R a 
2dι2plq ` ζ b 
ˇ 
ˇCl k 
ˇ 
ˇ 
˙ 
}x}pUl kq´1 , 
for all x such that }x}2 ď L, where ι2plq “ logppd ` |Cl k|L2B2q{pdδqq. 
The following two proof techniques are crucial to prove constant regret bound of Algo-
rithm 11. 
146
Optimal arm is never eliminated Considering the optimal arm in the eliminated set, 
which is defined by xl,˚ k “ argmaxxPDl 
rpxq. Obviously x1,˚ k “ x˚ 
k. The following (informal) 
lemma says that the decision set always contains a nearly optimal action xl,˚ k : 
Lemma 4.5.7 (informal). For any level l ą 0, assume some good events hold, then there ex-
ists xl,˚ k P Dl 
k, such that rpx˚ kq´rpxl,˚ 
k q ď 2pl´1qζ ´ 
1 ` 4 a 
dι1plq ¯ 
where ι1plq “ log ` 
3LB2l ˘ 
. 
Given the result of Lemma 4.5.7 and the existence of the sub-optimality gap ∆, we have 
xl,˚ k “ x˚ 
k when l is not too large. This means that the optimal arm is never eliminated from 
the decision set Dl. 
Sub-optimal arms are all eliminated Intuitively speaking, at level l, the prediction 
error is bounded by Õpβplq ¨ 2´lq with some additional misspecification term ζ. Therefore, 
when we eliminate the arms at level l, the sub-optimality of the arms in Dl is bounded by 
the following (informal) lemma: 
Lemma 4.5.8 (informal). For any level l ą 0, for any arm x P Dl k, rpx˚ 
kq´rpxq ď 6βplq2´l` 
2lζ ´ 
1 ` 4 a 
dι1plq ¯ 
where ι1plq “ log ` 
3LB2l ˘ 
. 
Given Lemma 4.5.8, we know that when l is sufficiently large (e.g., larger than l∆), all 
x P Dl k enjoys a sub-optimality less than ∆. Combining with the existence of sub-optimality 
gap ∆, we know that all of the sub-optimal arms are eliminated after level l∆. 
Regret decomposition Given Lemma 4.5.5 and Lemma 4.5.8, the regret over all K 
rounds can be decomposed into 
RegretpKq “ 
K ÿ 
k“1 
prpx˚ kq ´ rpxkqq “ 
ÿ 
lě1 
ÿ 
kPCl K 
prpx˚ kq ´ rpxkqq “ 
l∆ ÿ 
l“1 
ÿ 
kPCl K 
prpx˚ kq ´ rpxkqq , 
where the last equality is due to the fact that no regret occurs after l ą l∆. For each level 
l ď l∆, the summation of the instantaneous regret within k P Cl K can be bounded following 
147
the gap-dependent regret bound of Abbasi-Yadkori et al. (2011) to obtain a Õpd2 log |Cl K |{∆q 
regret bound which is independent from K. Then taking the summation over l ď l∆ yields 
the claimed constant regret bound. 
4.6 Lower Bound 
Following a similar idea in Lattimore et al. (2020), we prove a gap-dependent lower bound 
for misspecified stochastic linear bandits. Note that stochastic linear bandit can be seen as 
a special case of linear contextual bandits with a fixed decision set Dk “ D across all round 
k P rKs. Similar results and proof can be found in Du et al. (2019) for episodic reinforcement 
learning. 
Theorem 4.6.1 (Lower Bound). Given the dimension d and the number of arms |D|, for any 
∆ ď 1 and ζ ě 3∆ a 
8 logp|D|q{pd ´ 1q, there exists a set of stochastic linear bandit problems 
Θ with minimal sub-optimality gap ∆ and misspecification error level ζ, such that for any 
algorithm that has a sublinear expected regret bound for all θ P Θ, i.e., ErRegretθpKqs ď 
CKα with C ą 0 and 0 ď α ă 1, we have 
‚ When K ď Op|D|q, the expected regret is lower bounded by Eθ„Unif.pΘqrRegretθpKqs ě 
K∆. 
‚ When K ě Ωp|D|q, the expected regret is lower bounded by supθPΘ ErRegretθpKqs ě 
Ω̃p|D| logpKq∆´1q. 
Remark 4.6.2. Theorem 4.6.1 shows two regimes under the case ζ ě Ω̃p∆{ ? dq. In the first 
regime K ď Op|D|q where the decision set is large (e.g., |D| “ d100), any algorithm will suffer 
from a linear regret Õp∆Kq, which suggests that the regime cannot be efficiently learnable. 
In the second regime K ě Ωp|D|q, Theorem 4.6.1 suggests an Ω̃p|D|∆´1 logpKqq regret 
lower bound, which is matched by the multi-armed bandit algorithm with an upper bound 
Õp|D|∆´1 logpKqq (Lattimore and Szepesvári, 2020). Therefore, in this easier regime, linear 
148
function approximation cannot provide any performance improvement and one can simply 
adopt the multi-armed bandit algorithm to learn the bandit model. 
Remark 4.6.3. Theorems 4.4.1 and 4.6.1 provide a holistic picture about the role of mis-
specification in linear contextual bandits. Here we focus on the more difficult regime K ď |D|. 
In the regime K ď |D|, when ζ ď Õp∆{ ? dq, Theorem 4.4.1 suggests that the bandit problem 
is efficiently learnable, and our algorithm DS-OFUL can achieve a constant regret, which 
improves upon the logarithmic regret bound in the well-specified setting (Abbasi-Yadkori 
et al., 2011). On the other hand, when ζ ě Ω̃p∆{ ? dq, Theorem 4.6.1 provides a linear regret 
lower bound suggesting that the bandit model can not be efficiently learned. 
4.7 Numerical Experiments 
To verify the performance improvement by data selection using the UCB bonus in Algo-
rithm 10 and the effectiveness of the parameter-free algorithm Algorithm 11, we conduct 
experiments for bandit tasks on both synthetic and real-world datasets, which we will de-
0 2000 4000 6000 8000 10000 # or rounds 
0 
500 
1000 
1500 
2000 
2500 
Cu m 
ul at 
iv e 
Re gr 
et 
= 0 (OFUL) = 0.02 = 0.05 = 0.08 
= 0.18 Lattimore et al. Robust Linear Bandit SupLinUCB 
(a) On synthetic dataset over 10K rounds 
0.0 0.2 0.4 0.6 0.8 1.0 
# of rounds 1e6 
0 
500 
1000 
1500 
2000 
2500 
3000 
3500 
Cu m 
ul at 
iv e 
Re gr 
et 
0 
5000 
10000 
15000 
20000 
25000 
30000 
35000 
Cu m 
ul at 
iv e 
Re gr 
et  (S 
up Lin 
UC B) 
= 0 (OFUL) = 0.01 = 0.05 
SupLinUCB 
(b) On Asirra dataset over 1M rounds, ζ “ 0.01. 
Figure 4.2: Cumulative regret of DS-OFUL with different Γ. Results are averaged over 8 
runs. In Figure 4.2b for Asirra dataset, the cumulative regret of DS-OFUL (as well as OFUL) 
can be read from the y-axis on the left. The cumulative regret of SupLinUCB algorithm can 
be read from the y-axis on the right. 
149
Table 4.2: Averaged cumulative regret and elapsed time of DS-OFUL over 8 runs. The 
bold face value indicates the best (low regret or low elapsed time) for all the algorithm 
configurations 
Algorithm Configuration, (Γ) Regret 
(mean˘std.) 
Regret in last 
1k steps 
Elapsed 
Time(sec) 
OFUL (Abbasi-Yadkori et al., 
2011), Γ “ 0 405.4 ˘ 76.5 4.94 15.06 
DS-OFUL (Algorithm 10), Γ “ 0.02 326.5 ˘ 68.0 0.0 8.59 
DS-OFUL (Algorithm 10), Γ “ 0.05 235.75 ˘ 40.3 0.0 6.30 
DS-OFUL (Algorithm 10), Γ “ 0.08 411.6 ˘ 566.7 22.44 5.97 
DS-OFUL (Algorithm 10), Γ “ 0.13 1789.5 ˘ 1918.8 173.67 5.56 
Eq. (6) in Lattimore et al. (2020) 433.36 ˘ 64 1.79 ě 7 hrs. 
Robust Linear Bandit (Ghosh et al., 
2017) 831.5 ˘ 880.4 42.58 12.85 
SupLinUCB (Algorithm 11) 747.9 ˘ 329.5 0.0 31.86 
scribe in detail below. 
4.7.1 Synthetic Dataset 
The synthetic dataset is composed as follows: we set d “ 16 and generate parameter 
θ˚ „ N p0, Idq and contextual vectors txiu N i“1 „ N p0, Idq where N “ 100. The generated 
parameter and vectors are later normalized to be }θ˚}2 “ }xi}2 “ 1. The reward function is 
calculated by ri “ xθ˚,xiy ` ηi where ηi „ Unift´ζ, ζu. The contextual vectors and reward 
function is fixed after generated. The random noise on the receiving rewards εt are sampled 
from the standard normal distribution. 
We set the misspecification level ζ “ 0.02 and verified that the sub-optimality gap 
150
over the N contextual vectors ∆ « 0.18. We do a grid search for β “ t1, 3, 10u, λ “ 
t1, 3, 10u 3 and report the cumulative regret of Algorithm 10 with different parameter 
Γ “ t0, 0.02, 0.05, 0.08, 0.18u over 8 independent trials with total rounds K “ 10000. It is 
obvious that when Γ “ 0, our algorithm degrades to the standard OFUL algorithm (Abbasi-
Yadkori et al., 2011) which uses data from all rounds into regression. 
Besides the OFUL algorithm, we also compare with the algorithm (LSW) in Equation (6) 
of Lattimore et al. (2020) and the RLB in Ghosh et al. (2017) in Figure 4.2a and Table 4.2. 
For Lattimore et al. (2020), the estimated reward is updated by rpxq “ xJθk ` β}x}U´1 k 
` 
ε řk 
s“1 |xJU´1 k x´1 
s |. However, since the time complexity of the LSW algorithm is ÕpK2q due 
to the hardness of calculating ε řk 
s“1 |xJU´1 k x´1 
s | incrementally w.r.t. k. In our setting it 
takes more than 7 hours for 10000 rounds. 
For the RLB algorithm in Ghosh et al. (2017), we did the hypothesis test for k “ 10 
rounds and then decided whether to use OFUL or multi-armed UCB. The results show that 
both LSW and RLB achieve a worse regret than OFUL since in our setting ζ is relatively 
small. 
The result is shown in Figure 4.2a and the average cumulative regret on the last round is 
reported in Table 4.2 with its variance over 8 trials. We can see that by setting Γ « ∆{ ? d « 
0.18{ ? 16 « 0.05, Algorithm 10 can achieve less cumulative regret compared with OFUL 
(Γ “ 0). The algorithm with a proper choice of Γ also convergences to zero instantaneous 
regret faster than OFUL. It is also evident that a too large Γ “ 0.18 « ∆ will cause 
the algorithm to fail to learn the contextual vectors and induce a linear regret. Also, our 
algorithm shows that using a larger Γ can significantly boost the speed of the algorithm by 
reducing the number of regressions needed in the algorithm. 
Besides the performance improvement achieved by Algorithm 10, the experiments also 
demonstrates the effectiveness of Algorithm 11. As Table 4.2 suggests, SupLinUCB achieves 
3By “grid search”, we tune the parameter pβ, λq “ p1, 1q, p1, 3q, ¨ ¨ ¨ , p10, 3q, p10, 10q and see their results. 
151
a zero cumulative regret over the last 1000 steps. However, as discussed in Remark 4.5.4, 
the total regret of SupLinUCB is much higher than the DS-OFUL and OFUL since it takes 
more samples to learn the first l∆ ´ 1 levels which is not used by DS-OFUL. This constant 
larger sample complexity could also be verified by a longer elapsed time for executing the 
SubLinUCB comparing to DS-OFUL. 
4.7.2 Real-world Dataset 
To demonstrate that the proposed algorithm can be easily applied to modern machine learn-
ing tasks, we carried out experiments on the Asirra dataset (Elson et al., 2007). The task of 
agent is to distinguish the image of cats from the image of dogs. At each round k, the agent 
receives the feature vector ϕ1,k P R512 of a cat image and another feature vector ϕ2,k P R512 
of a dog image. Both feature vectors are generated using ResNet-18 (He et al., 2016) pre-
trained on ImageNet (Deng et al., 2009). We normalize }ϕ1,k}2 “ }ϕ2,k}2 “ 1. The agent 
is required to select the cat from these two vectors. It receives reward rt “ 1 if it selects 
the correct feature vector, and receives rt “ 0 otherwise. It is trivial that the sub-optimality 
gap of this task is ∆ “ 1. To better demonstrate the influence of misspecification on the 
performance of the algorithm, we only select the data with |ϕJ i θ 
˚ ´ ri| ď ζ with ri “ 1 if it 
is a cat and ri “ 0 otherwise. θ˚ is a pretrained parameter on the whole dataset using linear 
regression θ˚ “ argminθ 
řN i“1pϕ 
J i θ ´ riq 
2, which the agent does not know. 
For hyper-parameter tuning, we select β “ t0.1, 0.3, 1u and λ “ t1, 3, 10u by doing a grid 
search 4 and repeat the experiments for 8 times over 1M rounds for each parameter config-
uration. As shown in Figure 4.2b, when ζ “ 0.01, setting Γ “ 0.05 « ∆{ ? d will eventually 
have a better performance comapred with OFUL algorithm (setting Γ “ 0). On the other 
hand, the SupLinUCB algorithm (Algorithm 11) will suffer from a much higher, but constant 
regret bound, which is well aligned with our theoretical result especially Remark 4.5.4. We 
4By “grid search”, we tune the parameter pβ, λq “ p0.1, 1q, p0.1, 3q, ¨ ¨ ¨ , p1, 3q, p1, 10q and see their results. 
152
Table 4.3: The number of remaining data samples after data processing with expected 
misspecification level 
ζ # of cats # of dogs 
8 (without preprocessing) 12500 12500 
0.5 (linear separable) 10316 10511 
0.1 3182 3248 
0.05 2408 2442 
0.01 1886 1905 
skip the Robust Linear Bandit (Ghosh et al., 2017) algorithm since it is for stochastic linear 
bandit with fixed contextual features for each arm while here the contextual features are 
sampled and not fixed. The LSW (Equation (6) in Lattimore et al. (2020) is skipped due to 
the infeasible executing time. 
As a sensitivity analysis, we also set ζ “ t0.5, 0.1, 0.05u to test the impact of misspeci-
fication on the performance of algorithm choices of Γ. More experiment configurations and 
results are deferred to Section 4.7.3. 
4.7.3 Experiment Details and Additional Results 
4.7.3.1 Experiment Configuration 
The experiment on synthetic dataset is conducted on Google Colab with a 2-core Intel® 
Xeon® CPU @ 2.20GHz. The experiment on the real-world Asirra dataset (Elson et al., 
2007) is conducted on an AWS p2-xlarge instance. 
153
4.7.3.2 Data Preprocessing for the Asirra Dataset 
To demonstrate how our algorithm can deal with different levels of misspecification, we do 
data preprocessing before feeding the data into the agent. As described in Section 4.7.2, 
the remaining data with expected misspecification level ζ are shown in Table 4.3. It can be 
verified that even with the smallest misspecification level, there are still more than 10% of 
the data is selected. 
4.7.3.3 Additional Result on the Asirra Dataset 
As a sensitivity analysis, we change the misspecification level in the preprocessing part in 
the Asirra dataset. The result is shown in Figure 4.3. This result suggests that when 
the misspecification is small enough, setting Γ “ ∆{ ? d can deliver a reasonable result 
and SupLinUCB (Chu et al., 2011) can achieve a constant regret bound when ζ ď 0.1. It is 
aligned with the parameter setting in our Theorem 4.4.1 and the result in our Theorem 4.5.1. 
Meanwhile, we found that when ζ “ 0.5, which means it is strictly larger than the threshold 
∆{ ? d, the algorithm cannot achieve a similar performance with of ζ ă 0.1, regardless of 
the setting of parameter Γ. This also verifies the theoretical understanding of how a large 
misspecification level will harm the performance of the algorithm. 
0.0 0.2 0.4 0.6 0.8 1.0 
# of rounds 1e6 
0 
25000 
50000 
75000 
100000 
125000 
150000 
175000 
Cu m 
ul at 
iv e 
Re gr 
et 
0 
20000 
40000 
60000 
80000 
Cu m 
ul at 
iv e 
Re gr 
et  (S 
up Lin 
UC B) 
= 0 (OFUL) = 0.05 = 0.10 
SupLinUCB 
(a) ζ “ 0.5 
0.0 0.2 0.4 0.6 0.8 1.0 
# of rounds 1e6 
0 
2000 
4000 
6000 
8000 
10000 
12000 
Cu m 
ul at 
iv e 
Re gr 
et 
0 
5000 
10000 
15000 
20000 
25000 
30000 
35000 
Cu m 
ul at 
iv e 
Re gr 
et  (S 
up Lin 
UC B) 
= 0 (OFUL) = 0.05 = 0.10 
SupLinUCB 
(b) ζ “ 0.1 
0.0 0.2 0.4 0.6 0.8 1.0 
# of rounds 1e6 
0 
1000 
2000 
3000 
4000 
5000 
6000 
7000 
Cu m 
ul at 
iv e 
Re gr 
et 
0 
5000 
10000 
15000 
20000 
25000 
30000 
35000 
Cu m 
ul at 
iv e 
Re gr 
et  (S 
up Lin 
UC B) 
= 0 (OFUL) = 0.05 = 0.10 
SupLinUCB 
(c) ζ “ 0.05 
Figure 4.3: The performance of DS-OFUL under different misspecification levels ζ. Results 
are averaged over 8 runs, with standard errors shown as shaded areas. 
154
4.8 Conclusion 
We study the misspecified linear contextual bandit from a gap-dependent perspective. We 
propose an algorithm and show that if the misspecification level ζ ď Õp∆{ ? dq, the proposed 
algorithm, DS-OFUL, can achieve the same gap-dependent regret bound as in the well-
specified case. Along with Lattimore et al. (2020); Du et al. (2019), we provide a complete 
picture on the interplay between misspecification and sub-optimality gap, in which ∆{ ? d 
plays an important role on the phase transition of ζ to decide if the bandit model can be 
efficiently learned. 
Besides the aforementioned constant regret result, DS-OFUL algorithm requires the 
knowledge of sub-optimality ap ∆. We prove that the SupLinUCB algorithm (Chu et al., 
2011) can be viewed as a multi-level version of our algorithm and can also achieve a constant 
regret with our fine-grained analysis without the knowledge of ∆. Experiments are conducted 
to demonstrate the performance of the DS-OFUL algorithm and verify the effectiveness of 
SupLinUCB algorithm. 
The promising result suggests a few interesting directions for future research. For exam-
ple, it would be interesting to incorporate the Lipschitz continuity or smoothness properties 
of the reward function to derive fine-grained results. 
4.9 Proofs 
4.9.1 Detailed Proof of Theorem 4.4.1 
In this section, we provide detailed proof for Theorem 4.4.1. First, we present a technical 
lemma to bound the total number of data used in the online linear regression in Algorithm 10. 
Lemma 4.9.1 (Restatement of Lemma 4.4.5). Given 0 ă Γ ď 1, set λ “ B´2. For any 
k P rKs, |Ck| ď 16dΓ´2 logp3LBΓ´1q. 
155
Lemma 4.9.1 suggests that up to ÕpdΓ´2q contextual vectors have a UCB bonus greater 
than Γ. A similar result is also provided in He et al. (2021b), suggesting an ÕpΓ´2q Uniform-
PAC sample complexity. Lemma 4.9.1 also suggests that the numbers of data points added 
into the regression set C is finite. Thus, the impact of the noise and the misspecification on 
the linear regression estimator can be well-controlled. 
For a linear regression with up to |Ck| data points, the next lemma controls the prediction 
error under misspecification. 
Lemma 4.9.2 (Formal statement of Lemma 4.4.6). Let λ “ B´2. For all δ ą 0, with 
probability at least 1 ´ δ, for all x P Rd, k P rKs, the prediction error is bounded by: 
|xJ pθk ´ θ˚ 
q| ď 
´ 
1 ` R ? 2dι ` ζ 
a 
|Ck| 
¯ 
}x}U´1 k , 
where ι “ logppd` |Ck|L2B2q{pdδqq and |Ck| is the total number of data used in regression at 
the k-th round. 
Lemma 4.9.2 provides a similar confidence bound as the well-specified linear contextual 
bandits algorithms like OFUL (Abbasi-Yadkori et al., 2011). Comparing the confidence 
radius here ÕpR ? d ` ζ 
a 
|Ck´1|q with the conventional radius in OFUL ÕpR ? dq, one can 
find that there is an additional term ζ a 
|Ck| that is caused by the misspecification. If we 
directly use all data to do the regression, the resulting confidence radius will be in the order 
of Õp ? Kq and therefore will lead to a OpK 
? logKq regret bound (see Lemma 11 in Abbasi-
Yadkori et al. (2011)). This makes the regret bound vacuous. In our algorithm, however, 
the confidence radius is only a 
|Ck| where |Ck| is bounded by Lemma 4.9.1. As a result, our 
regret bound will not be vacuous (i.e., superlinear in K). 
When the misspecification level is well bounded by ζ “ Õp∆{ ? dq, the following corollary 
is a direct result of Lemmas 4.9.2 by replacing the term |Ck| with its upper bound provided 
in Lemma 4.9.1. 
Corollary 4.9.3. Suppose 2 ? dζι1 ď ∆, let λ “ B´2 and 0 ă Γ ď 1. Let β “ 1 ` 
2∆Γ´1?ι2{ι1 ` R ? 2dι3 where ι2 “ logp3LBΓ´1q, ι3 “ logpp1 ` 16L2B2Γ´2ι2q{δq, then with 
156
probability at least 1 ´ δ, for all x P Rd, k P rKs, the estimation error for all k P rKs is 
bounded by: |xJpθk ´ θ˚q| ď β}x}U´1 k 
. 
Proof. By Lemma 4.9.1, replacing |Ck| with its upper bound yields 
|xJ pθk ´ θ˚ 
q| ď p1 ` 4 ? dζΓ´1?ι2 ` R 
a 
2dι3q}x}U´1 k 
ď β}x}U´1 k , 
where the second inequality is due to the condition 2 ? dζ ď ∆{ι1. 
Next we introduce an auxiliary lemma controlling the instantaneous regret bound using 
the UCB bonus and the misspecification level. 
Lemma 4.9.4 (Formal statement of Lemma 4.4.7). Suppose Corollary 4.9.3 holds, for all 
k P rKs, the instantaneous regret at round k is bounded by 
∆kpxkq “ r˚ k ´ rpxkq ď 2ζ ` 2β}xk}U´1 
k . 
The next technical lemma from He et al. (2021a) bounds the summation of a subset of 
the bonuses. 
Lemma 4.9.5 (Lemma 6.6, He et al. 2021a). For any subset G “ tc1, ¨ ¨ ¨ , ciu Ď CK , we have 
ÿ 
kPG }xk} 
2 U´1 
k ď 2d logp1 ` |G|L2 
{λq. 
The next auxiliary lemma is used to control the dominating terms. 
Lemma 4.9.6. Let ι1 “ p24 ` 18Rq logpp72 ` 54RqLB ? d∆´1q ` 
a 
8R2 logp1{δq, Γ “ 
∆{p2 ? dι1q, ι2 “ logp3LBΓ´1q, ι3 “ logpp1`16L2B2Γ´2ι2q{δq, we have ι1 ą 2`4 
? ι2`R 
? 2ι3. 
Equipped with these lemmas, we can start the proof of Theorem 4.4.1. 
Proof of Theorem 4.4.1. First, note that by setting Γ “ ∆{p2 ? dι1q, the confidence radius β 
becomes 1` 4 ? dι2 `R 
? 2dι3. Then our proof starts by assuming that Corollary 4.9.3 holds 
157
with probability at least 1 ´ δ. We decompose the index set rKs into two subsets. The first 
set is the set of not selected data rKszCK , and the second set is the set of selected data CK . 
We will bound the cumulative regret within these two sets separately. 
First, for those non-selected data k R Ck, i.e. }xk}U´1 k 
ă Γ, combining Lemma 4.9.4 with 
Corollary 4.9.3 yields 
r˚ k ´ rpxkq ă 2ζ ` 2βΓ “ 2ζ ` 
∆ ? dι1 
` 
? 2ι3R∆ 
ι1 ` 
4∆ ? ι2 
ι1 , (4.9.1) 
where ι1, ι2, ι3 are the same as Theorem 4.4.1, and the equality is due to Γ “ ∆{p2 ? dι1q. 
When misspecification condition 2 ? dζ ď ∆{ι1 holds, (4.9.1) suggests that 
r˚ k ´ rpxkq ă 
2∆ ? dι1 
` 4∆ 
? ι2 
ι1 ` 
? 2ι3R∆ 
ι1 . (4.9.2) 
Lemma 4.9.6 suggests that when ι1 “ p24`18Rq logpp72`54RqLB ? d∆´1q ` 
a 
8R2 logp1{δq 
ι1 ą 2`4 ? ι2`R 
? 2ι3, (4.9.2) yields that the instantaneous regret r˚ 
k ´rpxkq ă ∆ at round k. 
By Definition 4.3.1, the instantaneous regret is zero for all k R Ck, indicating the non-selected 
data incur zero instantaneous regret. 
In addition, Lemma 4.9.4 suggests that the instantaneous regret for those k P CK is 
bounded by 
ÿ 
kPCK 
r˚ k ´ rpxkq ď 
ÿ 
kPCK 
´ 
2β}ϕk}U´1 k 
` 2ζ ¯ 
ď 2β a 
|CK | 
d 
ÿ 
kPCK 
}ϕk}2 U´1 
k 
` 2|CK |ζ 
ď 8βΓ´1 a 
dι2 a 
2d logp1 ` 16dΓ´2ι2q ` 32ζdΓ´2ι2 
ď 16β a 
2d3ι2 logp1 ` 16dΓ´2ι2qι1{∆ ` 64 ? d3ι1ι2{∆ 
ď 32β a 
2d3ι2 logp1 ` 16dΓ´2ι2qι1{∆, (4.9.3) 
where the second inequality follows the Cauchy-Schwarz inequality, the third one yields from 
Lemma 4.9.5 while the fourth utilizes the fact that Γ “ ∆{p2 ? dι1q and ζ ď ∆{p2 
? dι1q. The 
158
last one is due to the fact that the second term in the fourth inequality is dominated by the 
first one. 
To warp up, the cumulative regret can be decomposed by 
RegretpKq “ ÿ 
kRCK 
pr˚ k ´ rpxkqq ` 
ÿ 
kPCK 
pr˚ k ´ rpxkqq ď 0 ` 
32β a 
2d3ι2 logp1 ` 16dΓ´2ι2qι1 ∆ 
, 
where the first two zeros are given by the fact that for k R CK , we have r˚ k ´ rpxkq “ 0. the 
regret bound for k P G is given by (4.9.3). 
4.9.2 Proof of Technical Lemmas in Section 4.9.1 
4.9.2.1 Proof of Lemma 4.9.1 
The following auxiliary lemma and its corollary are useful 
Lemma 4.9.7 (Lemma A.2, Shalev-Shwartz and Ben-David 2014). Let a ě 1 and b ą 0. 
Then x ě 4a logp2aq ` 2b yields x ě a logpxq ` b. 
Lemma 4.9.7 can easily indicate the following lemma. 
Lemma 4.9.8. Let a ě 1. Then x ě 4 logp2aq ` a´1 yields x ě logp1 ` axq. 
Proof. Let y “ 1 ` ax, x “ py ´ 1q{a. Then x ě 4 logp2aq ` a´1 is equivalent with y ě 
4a logp2aq ` 2. By Lemma 4.9.7, this implies y ě a logpyq ` 1 which is exactly x ě logp1 ` 
axq. 
Equipped with these technical lemmas, we can start our proof. 
Proof of Lemma 4.9.1. Since the cardinality of set Ck is monotonically increasing w.r.t. k, 
we fix k to be K in the proof and only provide the bound of CK . For all selected data 
k P CK , we have }ϕk}U´1 k 
ě Γ. Therefore, when Γ ď 1, the summation of the bonuses over 
159
data k P CK is lower bounded by 
ÿ 
kPCK 
min ! 
1, }ϕk} 2 U´1 
k 
) 
ě |CK |mint1,Γ2 u “ |CK |Γ2. (4.9.4) 
On the other hand, Lemma 2.8.15 implies 
ÿ 
kPCK 
min ! 
1, }ϕk} 2 U´1 
k 
) 
ď 2d log 
ˆ 
λd ` |CK |L2 
λd 
˙ 
. (4.9.5) 
Combining (4.9.5) and (4.9.4), the total number of the selected data points |CK | is bounded 
by 
Γ2 |CK | ď 2d log 
ˆ 
λd ` |CK |L2 
λd 
˙ 
. 
This result can be re-organized as 
Γ2|CK | 
2d ď log 
ˆ 
1 ` 2L2 
Γ2λ 
Γ2|CK | 
2d 
˙ 
. (4.9.6) 
Let λ “ B´2 and since 2L2B2 ě 2 ě Γ2, by Lemma 4.9.8, if 
Γ2|CK | 
2d ą 4 log 
ˆ 
4L2B2 
Γ2 
˙ 
` 1 ě 4 log 
ˆ 
4L2B2 
Γ2 
˙ 
` Γ2 
2L2B2 , 
then (4.9.6) will not hold. Thus the necessary condition for (4.9.6) to hold is 
Γ2|CK | 
2d ď 4 log 
ˆ 
4L2B2 
Γ2 
˙ 
` 1 “ 8 log 
ˆ 
2LB 
Γ 
˙ 
` logpeq “ 8 log 
˜ 
2LBe 1 8 
Γ 
¸ 
ă 8 log 
ˆ 
3LB 
Γ 
˙ 
. 
By basic calculus we get the claimed bound for |CK | and complete the proof. 
4.9.2.2 Proof of Lemma 4.9.2 
The proof follows the standard technique for linear bandits, we first introduce the self-
normalized bound for vector-valued martingales from Abbasi-Yadkori et al. (2011). 
Lemma 4.9.9 (Theorem 1, Abbasi-Yadkori et al. 2011). Let tFtu 8 t“0 be a filtration. Let 
tεtu 8 t“1 be a real-valued stochastic process such that εt is Ft-measurable and εt is conditionally 
160
R-sub-Gaussian for some R ě 0. Let tϕtu 8 t“1 be an Rd-valued stochastic process such that 
ϕt is Ft´1 measurable and }ϕ}2 ď L for all t. For any t ě 0, define Ut “ λI ` řt 
k“1ϕkϕk. 
Then for any δ ą 0, with probability at least 1 ´ δ, for all t ě 0 
› 
› 
› 
› 
› 
t ÿ 
k“1 
ϕkεk 
› 
› 
› 
› 
› 
2 
U´1 t 
ď 2R2 log 
˜ 
a 
detpUtq a 
detpU0qδ 
¸ 
. 
Lemma 4.9.10 (Lemma 8, Zanette et al. 2020c). Let taiu d i“1 be any sequence of vectors in 
Rd and tbiu d i“1 be any sequence of scalars such that |bi| ď ζ. For any λ ą 0: 
› 
› 
› 
› 
› 
n ÿ 
i“1 
aibi 
› 
› 
› 
› 
› 
2 
r řn 
i“1 aiaJ i `λIs 
´1 
ď nζ2. 
The next lemma is to bound the perturbation of the misspecification 
Lemma 4.9.11. Let tηkuk be any sequence of scalars such that |ηk| ď ζ for any k P rKs. 
For any index subset C Ď rKs, define U “ λI ` ř 
kPC xkx J k , then for any x P Rd, we have 
ˇ 
ˇ 
ˇ 
ˇ 
xJU´1 ÿ 
kPC xkηk 
ˇ 
ˇ 
ˇ 
ˇ 
ď ζ a 
|C|}x}U´1 . 
Proof. By Cauchy-Schwartz inequality we have ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
xJU´1 ÿ 
kPC xkηk 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď }x}U´1 
› 
› 
› 
› 
› 
ÿ 
kPC xkηk 
› 
› 
› 
› 
› 
U´1 
ď ζ a 
|C|}x}U´1 , 
where the second inequality dues to lemma 4.9.10. 
The next lemma is the Determinant-Trace inequality. 
Lemma 4.9.12. Suppose sequence txkuKk“1 Ă Rd and for any k P rKs, }xk}2 ď L. For 
any index subset C Ď rKs, define U “ λI ` ř 
kPC xkx J k for some λ ą 0, then detpUq ď 
pλ ` |C|L2{dqd. 
Proof. The proof of this lemma is almost the same as Lemma 10 in Abbasi-Yadkori et al. 
(2011) by replacing the index set rKs with any subset C. We refer the readers to Abbasi-
Yadkori et al. (2011) for details. 
161
Equipped with these lemmas, we can start our proof. 
Proof of Lemma 4.9.2. For any k P rKs, considering the data samples k1 P Ck´1 used for 
regression at round k. Following the update rule of Uk and θk yields 
Ukpθk ´ θ˚ q “ UkU 
´1 k 
ˆ 
ÿ 
k1PCk´1 
xk1rk1 
˙ 
´ 
ˆ 
λI ` ÿ 
k1PCk´1 
xk1xJ k1 
˙ 
θ˚ 
“ ÿ 
k1PCk´1 
xk1rk1 ´ λθ˚ ´ 
ÿ 
k1PCk´1 
xk1xJ k1θ˚ 
“ ´λθ˚ ` 
ÿ 
k1PCk´1 
xk1prk1 ´ xJ k1θ˚ 
q 
“ ´λθ˚ ` 
ÿ 
k1PCk´1 
xk1εk1 ` ÿ 
k1PCk´1 
xk1ηk1 , 
where the first equation is due to Uk “ λI` ř 
k1PCk´1 xkx 
J k and θk “ U´1 
k 
ř 
k1PCk´1 xk1rk1 . The 
last equation follows the fact that rk1 is generated from rk1 “ rpxk1q`εk1 “ xJ k1θ˚`ηpxk1q`εk1 , 
where we denote ηpxk1q as ηk1 for the model misspecification error and εk1 is the random noise. 
Therefore, consider any contextual vector x P Rd, we have 
ˇ 
ˇxJ pθk ´ θ˚ 
q ˇ 
ˇ “ ˇ 
ˇxJU´1 k Ukpθk ´ θ˚ 
q ˇ 
ˇ 
ď λ ˇ 
ˇxJU´1 k θ 
˚ ˇ 
ˇ 
looooomooooon 
q1 
` 
ˇ 
ˇ 
ˇ 
ˇ 
xJU´1 k 
ÿ 
k1PCk´1 
ϕk1εk1 
ˇ 
ˇ 
ˇ 
ˇ 
loooooooooooomoooooooooooon 
q2 
` 
ˇ 
ˇ 
ˇ 
ˇ 
xJU´1 k 
ÿ 
k1PCk´1 
ϕk1ηk1 
ˇ 
ˇ 
ˇ 
ˇ 
loooooooooooomoooooooooooon 
q3 
, 
where the inequality is due to the triangle inequality. Lemma 4.9.11 yields that q3 ď 
ζ a 
|Ck´1|}x}U´1 k 
. From the fact that |xJAy| ď }x}A}y}A, we can bound term q1 by 
q1 ď }x}U´1 k 
}θ˚ }U´1 
k ď λ´1{2B}x}U´1 
k . (4.9.7) 
where the last inequality is due to the fact that U´1 k ĺ λ´1I. Term q2 is also bounded as 
q2 ď }x}U´1 k 
› 
› 
› 
› 
› 
ÿ 
k1PCk´1 
xk1εk1 
› 
› 
› 
› 
› 
U´1 k 
“ }x}U´1 k 
› 
› 
› 
› 
› 
K ÿ 
k1“1 
1 rk1 P Ck´1sxk1εk1 
› 
› 
› 
› 
› 
U´1 k 
looooooooooooooooomooooooooooooooooon 
I1 
, (4.9.8) 
162
where the second equation uses the indicator function to rewrite the summation over subset 
Ck´1. Denoting yk1 “ 1 rk1 P Ck´1sxk1 , noticing that }yk1}2 ď }xk1}2 ď L and 
Uk “ ÿ 
k1PCk´1 
xk1xJ k1 “ 
K ÿ 
k1“1 
1 rk1 P Ck´1sxk1xJ 
k1 “ 
K ÿ 
k1“1 
yk1yJ k1 , 
by Lemma 4.9.9, I1 can be further bounded by 
I1 ď 
g 
f 
f 
e2R2 log 
˜ 
a 
detpUkq a 
detpU0qδ 
¸ 
ď R 
d 
2 log 
ˆ 
detpUkq 
detpU0qδ 
˙ 
“ R 
d 
2 log 
ˆ 
detpUkq 
λdδ 
˙ 
, (4.9.9) 
where the second inequality follows the fact that detpUkq ě detpU0q “ λd. Notice that 
Uk “ λI` ř 
k1PCk´1 xk1xJ 
k1 . Lemma 4.9.12 suggests that detpUkq ď pλ`|Ck´1|L2{dqd, plugging 
this into (4.9.9), we obtain 
I1 ď R 
d 
2 log 
ˆ 
pλ ` |Ck´1|L2{dqd 
λdδ 
˙ 
ď R 
d 
2d log 
ˆ 
dλ ` |Ck´1|L2 
dλδ 
˙ 
. 
Plugging the bound of I1 into (4.9.8) and combining with (4.9.7) and Lemma 4.9.11 
together, replacing |Ck´1| with its upper bound |CK | we have with probability at least 1 ´ δ, 
for all k P rKs,x P Rd, 
|xJ pθk ´ θ˚ 
q| ď 
˜ 
R 
d 
2d log 
ˆ 
dλ ` |CK |L2 
dλδ 
˙ 
` Bλ´1{2 ` ζ 
a 
|CK | 
¸ 
}ϕ}U´1 k . 
Letting λ “ B´2 we get the claimed results. 
163
4.9.2.3 Proof of Lemma 4.9.4 
Proof. According to the definition of expected reward function rpxq, we have for all k P rKs, 
suppose the condition in Lemma 4.9.2 holds, then 
r˚ k ´ rk “ ηpx˚ 
kq ´ ηpxkq ` px˚ kq 
J θ˚ ´ xJ 
k θ ˚ 
ď 2ζ ` px˚ kq 
J θ˚ ´ xJ 
k θ ˚ 
“ 2ζ ` px˚ kq 
J θk ` px˚ kq 
J pθ˚ 
´ θkq ´ xJ k θk ` xJ 
k pθk ´ θ˚ q 
ď 2ζ ` px˚ kq 
J θk ` β}x˚ k}U´1 
k ´ xJ 
k θk ` β}xk}U´1 k 
ď 2ζ ` xJ k θk ` β}xk}U´1 
k ´ xJ 
k θk ` β}xk}U´1 k 
ď 2ζ ` 2β}xk}U´1 k , 
where the first inequality utilize the fact that |ηpxq| ď ζ for all x P Dk, the second in-
equality follows from Corollary 4.9.3, the third inequality is due to the fact that xk “ 
argmaxxPDk xJθk ` β}x}U´1 
k , which is executed in Line 6 of Algorithm 10. 
4.9.2.4 Proof of Lemma 4.9.6 
Proof. First it is clear to see that ? 2ι3 “ 
a 
2 logp1 ` 16L2B2Γ´2ι2q ` 2 logp1{δq. Using the 
fact that ? a ` b ď 
? a ` 
? b, it can be further bounded by 
? 2ι3 ď 
a 
2 logp1 ` 16L2B2Γ´2ι2q ` a 
2 logp1{δq. 
Assuming L ě 1, B ě 1,Γ “ ∆{p2 ? dι1q ď 1 yields LBΓ´1 ě 1, then by basic calculus one 
can verify that 
2 ` 4 ? ι2 ď 6 logp3LBΓ´1 
q, a 
2 logp1 ` 16L2B2Γ´2ι2q ď 3 logp3LBΓ´1 q, 
therefore we have that 
2 ` 4 ? ι2 ` R 
? 2ι3 ď p6 ` 3Rq logp3LBΓ´1 
q ` a 
2 logp1{δqR 
“ p6 ` 3Rq logp6LB ? d∆´1ι1q ` 
a 
2 logp1{δqR, 
164
where the last equality is from the fact that Γ “ ∆{p2 ? dι1q. Lemma 4.9.7 suggests that the 
necessary condition for 
p6LB ? d∆´1 
qι1 loooooooomoooooooon 
x 
ě p6LB ? d∆´1 
qp6 ` 3Rq looooooooooooomooooooooooooon 
a 
logp6LB ? d∆´1ι1q ` p6LB 
? d∆´1 
q a 
2 logp1{δqR loooooooooooooooomoooooooooooooooon 
b 
(4.9.10) 
is that 
p6LB ? d∆´1 
qι1 ě 4p6LB ? d∆´1 
qp6 ` 3Rq logp2p6LB ? d∆´1 
qp6 ` 3Rqq 
` 2p6LB ? d∆´1 
q a 
2 logp1{δqR, 
which suggests that setting 
ι1 “ p24 ` 18Rq logpp72 ` 54RqLB ? d∆´1 
q ` a 
8R2 logp1{δq 
implies the fact that ι1 ě 2 ` 4 ? ι2 ` R 
? 2ι3 
4.9.3 Detailed Proof of Theorem 4.5.1 
The first lemma shows that the contexts selected to l-th level are bounded independent from 
K 
Lemma 4.9.13 (Restatement of Lemma 4.5.5). Set λ “ B´2. For any k P rKs and l ą 0, 
|Cl k| ď 16d4lι1plq where ι1plq “ log 
` 
3LB2l ˘ 
. 
Proof. The proof is similar to the proof of Lemma 4.9.1 by repalcing Γ “ 2´l. 
The next lemma provides a fluctuation control as well as the concentration in the ridge 
regression 
Lemma 4.9.14 (Restatement of Lemma 4.5.6). Set λ “ B´2. For any level l ą 0, for any 
δ ą 0, with probability at least 1 ´ δ, for all k P rKs, the estimation error is bounded by ˇ 
ˇxJ pθlk ´ θ˚ 
q ˇ 
ˇ ď 
ˆ 
1 ` R a 
2dι2plq ` ζ b 
ˇ 
ˇCl k 
ˇ 
ˇ 
˙ 
}x}pUl kq´1 , 
for all x such that }x}2 ď L, where ι2plq “ logppd ` |Cl k|L2B2q{pdδqq. 
165
Proof. The proof is similar to the proof of Lemma 4.9.2 
Combining Lemma 4.9.13 and Lemma 4.9.14, we have the following corollary. 
Corollary 4.9.15. Set λ “ B´2. For any δ ą 0, with probability at least 1´δ, for all round 
k P rKs and any level l ą 0, for all x such that }x}2 ď L, the prediction error is bounded by 
ˇ 
ˇxJ pθlk ´ θ˚ 
q ˇ 
ˇ ď 
´ 
βplq ` 4ζ2l a 
dι1plq ¯ 
}x}pUl kq´1 , 
where βplq “ 1`R a 
2dι2plq, ι2plq “ logppd2l`16L2B28lι1plqq{pdδqq, and ι1plq “ log ` 
3LB2l ˘ 
. 
Proof. The proof is simply by plugging the result in Lemma 4.9.13 into Lemma 4.9.14 and 
replacing the δ with δ{2l. By the union bound over l P N` and the fact that ř8 
l“1 δ{2l “ δ 
yields the claimed result. 
Now, we are about to control Dl k, which means here we only consider the case where 
}x}pUl kq´1 ď 2´l for all x P Dl 
k and assuming the high-probability event in previous sub-
section always holds. The following lemma suggests that the decision set always keeps a 
nearly optimal action xl,˚ k . Let GK be the event that the high probability statement in 
Corollary 4.9.15 holds. 
Lemma 4.9.16 (Formal statement of Lemma 4.5.7). For any level l ą 0, assume event 
GK holds, then there exists xl,˚ k P Dl 
k, rpx˚ kq ´ rpxl,˚ 
k q ď 2pl ´ 1qζ ´ 
1 ` 4 a 
dι1plq ¯ 
where 
ι1plq “ log ` 
3LB2l ˘ 
. 
Proof. We would prove the statement by induction. Since D1 k “ Dk, we have x˚ 
k P D1 k 
and thus the induction basis holds according to rpx˚ kq ´ rpxl,˚ 
k q “ 0. Now we assume the 
statement holds for level l, that is, there exists xl,˚ k P Dl 
k such that xl,˚ k P Dl 
k, rpx˚ kq´rpxl,˚ 
k q ď 
2pl ´ 1qζ ´ 
1 ` 4 a 
dι1plq ¯ 
. 
If xl,˚ k P Dl`1 
k , then the desired statement directly holds by choosing xl,˚ k “ xl´1,˚ 
k . Oth-
erwise xl,˚ k is eliminated by some action xl`1,˚ 
k P Dl k that rlkpxl`1,˚ 
k q ě rlkpxl,˚ k q ` 2βplq2´l. 
166
Moreover, from the definition of estimator rlkp¨q, we have 
rlkpxl`1,˚ k q ´ rpxl`1,˚ 
k q ď ζ ` 
A 
xl`1,˚ k , θlk ´ θ˚ 
E 
` βplq › 
› 
› xl`1,˚ k 
› 
› 
› 
pUl kq´1 
(4.9.11) 
and 
rpxl,˚ k q ´ rlkpxl,˚ 
k q ď ζ ´ 
A 
xl,˚ k , θlk ´ θ˚ 
E 
´ βplq › 
› 
› xl,˚ k 
› 
› 
› 
pUl kq´1 
. (4.9.12) 
Combining (4.9.11) and (4.9.12) and the fact that rlkpxl`1,˚ k q ě rlkpxl,˚ 
k q ` 3βplq2´l gives that 
rpxl,˚ k q ´ rpxl`1,˚ 
k q ď ´3βplq2´l ` 2ζ ` 
A 
xl`1,˚ k ´ xl,˚ 
k , θlk ´ θ˚ E 
´ βplq › 
› 
› xl`1,˚ k 
› 
› 
› 
pUl kq´1 
` βplq › 
› 
› xl,˚ k 
› 
› 
› 
pUl kq´1 
ď ´3βplq2´l ` 2ζ ` 2 ¨ 2´l 
´ 
βplq ` 4ζ2l a 
dι1plq ¯ 
` βplq2´l 
ď 2ζ ´ 
1 ` 4 a 
dι1plq ¯ 
, 
where the second inequality is suggested by Corollary 4.9.15 and }x}pUl kq´1 ď 2´l for all 
x P Dl k. The desired statement can then be reached using the induction hypothesis. 
Then, the following lemma suggests that the performance of the actions in the decision 
set is guaranteed. 
Lemma 4.9.17 (Formal statement of Lemma 4.5.8). For any level l ą 0, assume event 
GK holds, then for any action x P Dl k, rpx˚ 
kq ´ rpxq ď 6βplq2´l ` 2lζ ´ 
1 ` 4 a 
dι1plq ¯ 
where 
ι1plq “ log ` 
3LB2l ˘ 
. 
Proof. Let xl,˚ k P Dl 
k be the optimal action given in Lemma 4.9.16. According to the elimi-
nation process, for any action x P Dl k, it holds that rlkpxq ě rlkpxl,˚ 
k q ´ 3βplq2´l. Moreover, 
from the definition of estimator rlkp¨q, we have 
rlkpxq ´ rpxq ď ζ ` @ 
x, θlk ´ θ˚ D 
` βplq }x} pUl 
kq´1 
167
and 
rpxl,˚ k q ´ rlkpxl,˚ 
k q ď ζ ´ 
A 
xl,˚ k , θlk ´ θ˚ 
E 
´ βplq › 
› 
› xl,˚ k 
› 
› 
› 
pUl kq´1 
. 
Combining the above three inequalities give 
rpxl,˚ k q ´ rpxq ď 3βplq2´l 
` 2ζ ` 2´l ` 
A 
x ´ xl,˚ k , θlk ´ θ˚ 
E 
´ βplq › 
› 
› xl,˚ k 
› 
› 
› 
pUl kq´1 
` βplq › 
› 
› xl´1,˚ k 
› 
› 
› 
pUl kq´1 
ď 3βplq2´l ` 2ζ ` 2 ¨ 2´l 
´ 
βplq ` 4ζ2l a 
dι1plq ¯ 
` βplq2´l 
ď 6βplq2´l ` 2ζ 
´ 
1 ` 4 a 
dι1plq ¯ 
, 
where the second inequality is suggested by Corollary 4.9.15 and }x}pUl kq´1 ď 2´l for all 
x P Dl k. The desired statement can then be reached by combining Lemma 4.9.16. 
Proof of Theorem 4.5.1. Consider the case that event GK holds. Let l∆ be the smallest 
integer solution to l∆ ą logp8βpl∆q∆´1q. Note this relation ensures 4βpl∆q2´l∆ ă ∆{2. In 
case that the misspecification level is bounded by 2l∆ζ ´ 
1 ` 4 a 
dι1pl∆q 
¯ 
ă ∆{2, it holds 
that 6βpl∆q2´l∆ ` 2l∆ζ ´ 
1 ` 4 a 
dι1pl∆q 
¯ 
ă ∆. According to Lemma 4.9.17, it satisfies that 
rpx˚ kq ´ rpxq ď 6βpl∆q2´l∆ ` 2l∆ζ 
´ 
1 ` 4 a 
dι1pl∆q 
¯ 
for any x P Dl∆ k . According to the process of arm elimination, we have Dl 
k Ď Dl∆ k for any 
l ě l∆. Thus, it holds that rpx˚ kq ´ rpxq ă ∆ for any x P Dl 
k, l ě l∆. Note that according to 
the definition of ∆, we have rpx˚ kq ´ rpxq ą ∆ for all x P Dl 
k that rpx˚ kq ‰ rpxq. These two 
statements together restrict rpx˚ kq “ rpxq for any x P Dl 
k on every l ą l∆, that is, any action 
that remains in the decision sets on higher levels are optimal. Let U l K be the set of index k 
that action xk is chosen from layer l. We have |U l K | ď |Cl 
K | ` 4ld. Thus, we could decompose 
168
the total regret by 
RegretpKq “ ÿ 
lě1 
ÿ 
kPU l K 
prpx˚ kq ´ rpxqq “ 
l∆´1 ÿ 
l“1 
ÿ 
kPU l K 
prpx˚ kq ´ rpxqq 
ď 
l∆´1 ÿ 
l“1 
p|Cl K | ` 4ldq ¨ 
´ 
6βplq2´l ` 2lζ 
´ 
1 ` 4 a 
dι1plq ¯¯ 
ď 
l∆´1 ÿ 
l“1 
16d4lι1plq ¨ 
´ 
6βplq2´l ` 2lζ 
´ 
1 ` 4 a 
dι1plq ¯¯ 
ď 96d l∆´1 ÿ 
l“1 
βplq2lι1plq ` 32dζ l∆´1 ÿ 
l“1 
l4lι1plq ´ 
1 ` 4 a 
dι1plq ¯ 
ď 96dβpl∆q2l∆ι1pl∆q ` 32dl∆4 l∆ι1pl∆qζ 
´ 
1 ` 4 a 
dι1pl∆q 
¯ 
ď 1536dβ2 pl∆qι1pl∆q{∆ ` 8192dβ2 
pl∆qι1pl∆q{∆ 
ď 214dβ2 pl∆qι1pl∆q{∆ 
where the second equality is given by Lemma 4.9.17, the second inequality is given by 
Lemma 4.9.13, the third last inequality holds since βp¨q and ι1p¨q are monotone increase and 
the second inequality since 2l∆´1 ď 8βpl∆´1q∆´1 ď 8βpl∆q∆´1 and 2l∆ζ ´ 
1 ` 4 a 
dι1pl∆q 
¯ 
ă 
∆{2. 
4.9.4 Proof of Theorem 4.6.1 
To begin with, we introduce the lemma providing a sparse vector set in Rd. 
Lemma 4.9.18 (Lemma 3.1, Lattimore et al. 2020). For any ε ą 0 and d ă r|D|s such that 
d ě r8 logp|D|qε´2s, there exists a vector set D Ă Rd such that }x}2 “ 1 for all x P D and 
|xx,yy| ď ε for all x,y P D and x ‰ y. 
Next, we present the Bretagnolle–Huber inequality providing the lower bound to distin-
guish a system. 
169
Lemma 4.9.19 (Bretagnolle–Huber inequality). Let P and Q be probability measures on 
the same measurable space pΩ,Fq, let A P F be an arbitary event. Then 
P pAq ` QpAc q ě 
1 
2 expp´KLpP,Qqq. 
For stochastic linear bandit problem with finite arm, we can denote Tipkq as the number of 
rounds the algorithm visit the i-th arm over total k rounds. Then We have the KL-divergence 
decomposition lemma. 
Lemma 4.9.20 (Lemma 15.1, Lattimore and Szepesvári (2020)). Let ν “ pP1, ¨ ¨ ¨ , Pnq 
be the reward distributions associated with one n-armed bandit and let ν 1 “ pP 1 1, ¨ ¨ ¨ , P 1 
nq 
be another n-armed bandit. Fix some algorithm π and let Pν “ Pνπ,Pν1 “ Pν1,π be the 
probability measures on the canonical bandit model induced by the k-round interconnection 
of π and ν (respectively, π and ν 1). Then KLpPν ,Pν1q “ řn 
i“1 EνrTipnqsKLpPi, P 1 i q 
Proof of Theorem 4.6.1. The proof starts from inheriting the idea from Lattimore et al. 
(2020). Given dimension d and the number of arms |D|, setting ε “ a 
8 logp|D|q{pd ´ 1q, we 
can provide the contextual vector set D such that 
}x}2 “ 1, @x P D, |xx,yy| ď 
c 
8 logp|D|q 
d ´ 1 , @x,y P D,x ‰ y, 
For simplicity, we index the decision set as x1, ¨ ¨ ¨ ,x|D|. Given the minimal sub-optimality 
gap ∆, we provide the parameter set Θ as follows: 
Θ “ ␣ 
θpi,jq “ ∆xi ` 2∆xj,xi,xj P D, i ‰ j ( 
ď 
tθi “ ∆xi,xi P Du. 
It can be verified that Θ contains two kinds of θ. The first one θpi,jq is a mixture of two 
different contexts xi,xj with different strength ∆ and 2∆. The second one is θi which only 
contains features from one context xi. We can further verify that the size of |Θ| “ |D|2 and 
}θ}2 ď ? 5∆ for θ P Θ. For different parameter θ, the reward function is sampled from a 
170
Gaussian distribution N prθpxq, 1q, where the expected reward function is defined as 
rθpi,jq pxq “ 
$ 
’ 
’ 
’ 
’ 
’ 
& 
’ 
’ 
’ 
’ 
’ 
% 
2∆ if x “ xj 
∆ if x “ xi 
0 otherwise 
, rθipxq “ 
$ 
’ 
& 
’ 
% 
∆ if x “ xi 
0 otherwise . 
We can verify that the minimal sub-optimality of all these bandit problem is ∆. For 
different parameter θ and input x, by utilizing the sparsity of the set D (i.e. |xJy| ď ε if 
x ‰ y), we can verify the misspecification level as 
|rθpi,jq pxq ´ θJ 
pi,jqx| “ 
$ 
’ 
’ 
’ 
’ 
’ 
& 
’ 
’ 
’ 
’ 
’ 
% 
|2∆ ´ 2∆xJ j x ´ ∆xJ 
i x| ď ∆ε if x “ xj 
|∆ ´ 2∆xJ j x ´ ∆xJ 
i x| ď 2∆ϵ if x “ xi 
|0 ´ 2∆xJ j x ´ ∆xJ 
i x| ď 3∆ε otherwise 
|rθipxq ´ θJ i pxq| “ 
$ 
’ 
& 
’ 
% 
|∆ ´ ∆xJ i x| “ 0 if x “ xi 
|0 ´ ∆xJ i x| ď ∆ε otherwise. 
Therefore we have verified that the misspecification level is bounded by ζ “ 3∆ε. 
The provided bandit structure is hard for any linear algorithm to learn since any algorithm 
cannot get any information before it encounters non-zero expected rewards, even regardless 
of the noise of the rewards. We following the same method in Lattimore and Szepesvári 
(2020). If the algorithm choose arm i at the first round, there would be |D| parameters 
(i.e. θi,θpi,¨q receiving a non-zero expected reward. On the second round if the algorithm 
choose a different arm j, there would be |D| parameters (i.e. θj,θpj,k:k‰iq receiving a non-zero 
171
expected reward. Therefore the average time of receiving zero expected reward should be 
|D| ´2 
|D| ÿ 
i“1 
pi ´ 1qp|D| ´ i ` 1q “ |D| ´2 
|D|´1 ÿ 
i“0 
ip|D| ´ iq 
“ |D| ´2 
˜ 
|D| 
|D|´1 ÿ 
i“0 
i ´ 
|D|´1 ÿ 
i“0 
i2 
¸ 
“ |D| ´2 
ˆ 
|D|2p|D| ´ 1q 
2 ´ 
|D|p|D| ´ 1qp2|D| ´ 1q 
6 
˙ 
“ |D| ´ 1 
2 
ˆ 
1 ´ 2|D| ´ 1 
3|D| 
˙ 
ě |D| ´ 1 
6 , 
where the third equation is from the fact that řn 
i“1 i “ npn ` 1q{2 and řn 
i“1 i 2 “ npn ` 
1qp2n ` 1q{6. The last inequality is from the fact that 2|D| ´ 1q{p3|D|q ď 2{3. Therefore, 
even without of the random noise, any algorithm is expected to receive mintK, p|D| ´ 1q{6u 
uninformative data with expected reward to be zero. Therefore any algorithm will receive a 
∆mintK, p|D| ´ 1q{6u regret considers the suboptimality as ∆. 
Next, we consider the effect of random noise. For any algorithm running on this parameter 
set Θ, we find two parameter θi and θi,j where j ‰ i. Define the event as A “ tTjpkq ě k{2u 
and Ac “ tTjpkq ă k{2u. By Lemma 4.9.19 and Lemma 4.9.20, 
Pθi 
ˆ 
Tjpkq ě k 
2 
˙ 
` Pθpi,jq 
ˆ 
Tjpkq ă k 
2 
˙ 
ě 1 
2 expp´KLpPθi ,Pθpi,jq 
qq 
ě 1 
2 exp 
˜ 
´ ÿ 
nPD EθirTnpkqsKL 
` 
Pθpi,jq,n,Pθj ,n 
˘ 
¸ 
. 
(4.9.13) 
Noticing the minimal sub-optimality gap is ∆. Also the j-th arm is the sub-optimal arm 
for parameter θi. Therefore, once Tjpkq ě k{2, the algorithm will at least suffer from ∆k{2 
regret for parameter θi. Also, since the j-th arm is the optimal arm for bandit θpi,jq. If 
Tjpkq ă k{2, the algorithm will also at least suffer from ∆k{2 regret for θpi,jq. Denoting 
172
Rθpkq as the expected cumulative regret over k rounds, that is to say 
Rθipkq ě ∆k 
2 PθipTjpkq ě k{2q Rθjpkq ě 
∆k 
2 PθipTjpkq ă k{2q. (4.9.14) 
On the other hand since the bandit using θi and θj only differ in the j-th arm. Since 
standard Gaussian noise is adapted, KLpPθi,n,Pθpi,jq,nq “ ∆2 1rn “ js{2. Combining this 
with (4.9.14), (4.9.13) suggests that 
Rθipkq ` Rθjpkq ě ∆k 
2 exp 
ˆ 
´ ∆2 
2 Eθi rTjpkqs 
˙ 
, 
which suggests that 
Eθi rTjpkqs ě logp∆kq ´ log 2 ´ logpRθipkq ` Rθjpkqq 
∆2{2 , (4.9.15) 
For any algorithm seeking to get a sublinear expected regret bound of Rθpkq ď Ckα with 
C ą 0, 0 ď α ă 1 for all θ P Θ, (4.9.15) becomes 
Eθi rTjpkqs ě logp∆kq ´ log 2 ´ logp2Ckαq 
∆2{2 “ 
logp∆kq ´ logp4Cq ´ α log k 
∆2{2 . (4.9.16) 
Since that the regret on θi can be decomposed by 
Rθipkq “ ∆ 
|D| ÿ 
n“1,n‰i 
Tnpkq, (4.9.17) 
combining (4.9.17) with (4.9.16) yields 
Rθipkq ě 2p|D| ´ 1q 
∆ max tlogp∆kq ´ logp4Cq ´ α log k, 0u , 
where the max operator is trivially taken for Rθpkq ě 0. 
173
CHAPTER 5 
Uncertainty-Aware Robust Reinforcement Learning via 
Certified Estimator 
5.1 Introduction 
In Chapter 4, we discussed a data selection method and a phased algorithm that can handle 
the misspecified bandit tasks and deliver a constant regret bound. In this chapter, we move 
on to a more general reinforcement learning setting. 
Reinforcement learning (RL) has been a popular approach for teaching agents to make 
decisions based on feedback from the environment. RL has shown great success in a variety 
of applications, including robotics (Kober et al., 2013), gaming (Mnih et al., 2013), and 
autonomous driving. In the most of these applications, there is a common expectation 
that RL agents will master tasks while making only a bounded number of mistakes, even 
over indefinite runs. However, theoretical support of this expectation is limited in the RL 
theory literature: in the instance-independent case, Jin et al. (2020b); Ayoub et al. (2020); 
Wang et al. (2019), provided only Õp ? Kq regret upper bounds; in the instance-dependent 
setting, Simchowitz and Jamieson (2019); Yang et al. (2021); He et al. (2021a) provided 
logarithmic Õp∆´1 logKq high-probability regret upper bounds for both tabular MDPs and 
MDPs with linear function approximations, given a suboptimality gap ∆. However, these 
findings suggest that an agent’s regret increases with the number of episodes K, contradicting 
the practical expectation of finite mistakes. Conversely, recent years have witnessed a series 
of work providing a constant regret bound for RL and bandits, suggesting that an RL 
174
agent’s regret may remain bounded even when it faces an indefinite number of episodes. 
Papini et al. (2021a); Zhang et al. (2021a) have provided instance-dependent constant regret 
bounds under the assumption of prior data distribution. However, verifying these data 
distribution assumptions can be difficult or infeasible. On the other hand, it is known that 
high-probability constant regret bounds can be achieved unconditionally in multi-armed 
bandits (Abbasi-Yadkori et al., 2011) and in contextual linear bandits if and only if the 
misspecification is sufficiently small with respect to the minimal sub-optimality gap (Zhang 
et al., 2023c). This raises a critical question: 
Is it possible to design a reinforcement learning algorithm that incurs only constant regret 
under minimal assumptions? 
To answer this question, we introduce a algorithm, which we refer to as Cert-LSVI-UCB, 
for reinforcement learning with linear function approximation. To encompass a broader range 
of real-world scenarios characterized by large state-action spaces and the need for function 
approximations, we adapt the misspecified linear MDP (Jin et al., 2020b) setting, where both 
the transition kernel and reward function can be approximated by a linear function with 
approximation error ζ. We show that, with our innovative design of certified estimator and 
novel analytical techniques, Cert-LSVI-UCB achieves constant regret without relying on any 
prior assumptions on data distributions. 
5.1.1 Organization of this Chapter 
This chapter is organized as follows: we discuss the related work in Section 5.2 and the 
preliminaries in Section 5.3. In Section 5.4, we present Cert-LSVI-UCB which leverages 
a certified estimator to guarantee the robustness of the estimation of the value function. In 
Section 5.5, we present the regret analysis for Cert-LSVI-UCB. We highlight several key 
techniques in Section 5.6 and draw the conclusion in Section 5.7. The detailed proof is 
deferred to Section 5.8. 
175
Algorithm Misspecified MDP? Result 
LSVI-UCB (He et al., 2021a) ˆ Õpd3H5∆´1 logpKqq 
LSVI-UCB (Papini et al., 2021a) ˆ Õpd3H5∆´1 logp1{λqq 
Cert-LSVI-UCB (ours, Theorem 5.5.1) ✓ Õpd3H5∆´1q 
Table 5.1: Instance-dependent regret bounds for different algorithms under the linear MDP 
setting. Here d is the dimension of the linear function ϕps, aq, H is the horizon length, ∆ 
is the minimal suboptimality gap. All results in the table represent high probability regret 
bounds. The regret bound depends the number of episodes K in He et al. (2021a) and the 
minimum positive eigenvalue λ of features mapping in Papini et al. (2021b). Misspecified 
MDP? indicates if the algorithm can (✓) handle the misspecified linear MDP or not (ˆ). 
5.2 Related Work 
Instance-dependent regret bound in RL. Although most of the theoretical RL works 
focus on worst-case regret bounds, instance-dependent (a.k.a., problem-dependent, gap-
dependent) regret bound is another important bound to understanding how the hardness 
of different instance can affect the sample complexity of the algorithm. For tabular MDPs, 
Jaksch et al. (2010) proved a ÕpD2S2A∆´1 logKq instance-dependent regret bound for 
average-reward MDP where D is the diameter of the MDP and ∆ is the policy subopti-
mal gap. Simchowitz and Jamieson (2019) provided a lower bound for episodic MDP which 
suggests that the any algorithm will suffer from Ωp∆´1q regret bound. Yang et al. (2021) 
analyzed the optimistic Q-learning and proved a OpSAH6∆´1 logKq logarithmic instance-
dependent regret bound. In the domain of linear function approximation, He et al. (2021a) 
provided instance-dependent regret bounds for both linear MDPs (i.e., Õpd3H5∆´1 logKq) 
and linear mixture MDPs (i.e., Õpd2H5∆´1 logKq). Furthermore, Dann et al. (2021) pro-
vided an improved analysis for this instance-dependent result with a redefined suboptimal 
gap. Zhang et al. (2023b) proved a similar logarithmic instance-dependent bound with He 
176
et al. (2021a) in misspecified linear MDPs, showing the relationship between misspecification 
level and suboptimality bound. Despite all these bounds are logarithmic depended on the 
number of episode K, many recent works are trying to remove this logarithmic dependence. 
Papini et al. (2021a) showed that under the linear MDP assumption, when the distribution 
of contexts ϕps, aq satisfies the ‘diversity assumption’ (Hao et al., 2020) called ‘UniSOFT’, 
then LSVI-UCB algorithm may achieve an expected constant regret w.r.t. K. Zhang et al. 
(2021a) showed a similar result on bilinear MDP (Yang and Wang, 2020b), and extended 
this result to offline setting, indicating that the algorithm only need a finite offline dataset 
to learn the optimal policy. Table 5.1 summarizes the most relevant results mentioned above 
for the ease of comparison with our results. 
RL with model misspecification. All of the aforementioned works consider the well-
specified setting and ignore the approximation error in the MDP model. To better under-
stand this misspecification issue, Du et al. (2019) showed that having a good representation 
is insufficient for efficient RL unless the approximation error (i.e., misspecification level) by 
the representation is small enough. In particular, Du et al. (2019) showed that an Ω̃p a 
H{dq 
misspecification will lead to Ωp2Hq sample complexity for RL to identify the optimal policy, 
even with a generative model. On the other hand, a series of work (Jin et al., 2020b; Zanette 
et al., 2020b,a) provided Õp ? K ` ζKq-type regret bound for RL in various settings, where ζ 
is the misspecification level1 and we ignore the dependence on the dimension of the feature 
mapping d and the planing horizon H for simplicity. These algorithms, however, require the 
knowledge of misspecification level ζ, thus are not parameter-free. Another concern for these 
algorithms is that some of the algorithms (Jin et al., 2020b) would possibly suffer from a 
trivial asymptotic regret, i.e., Regretpkq ą ωpkζ ¨ polypd,H, logp1{δqqq, as suggested by Vial 
et al. (2022). This means the performance of the RL algorithm will possibly degenerate as 
1The misspecification level for these upper bounds is measured in the total variation distance between the ground truth transition kernel and approximated transition kernel, which is strictly stronger than the infinite-norm misspecification used in Du et al. (2019). 
177
the number of episodes k grows. To tackle these two issues, Vial et al. (2022) propose the 
Sup-LSVI-UCB algorithm which requires a parameter εtol. When εtol “ d{ ? K, the proposed 
algorithm is parameter-free but will have a trivial asymptotic regret bound. When εtol “ ζ, 
the algorithm will have a non-trivial asymptotic regret bound but is not parameter-free since 
it requires knowledge of the misspecification level. Another series of works (He et al., 2022b; 
Lykouris et al., 2021; Wei et al., 2022) are working on the corruption robust setting. In 
particular, Lykouris et al. (2021); Wei et al. (2022) are using the model-selection technique 
to ensure the robustness of RL algorithms under adversarial MDPs. 
5.3 Preliminaries 
We consider episodic Markov Decision Processes denoted by MpS,A, H, trhu, tPhuq. Here, 
S is the state space, A is the finite action space, H is the length of each episode, rh : SˆA ÞÑ 
r0, 1s is the reward function at stage h and Php¨|s, aq is the transition probability function at 
stage h. The policy π “ tπhuHh“1 denotes a set of policy functions πh : S ÞÑ A for each stage 
h. For given policy π, we define the state-action value function Qπ hps, aq and the state value 
function V π h psq as 
Qπ hps, aq “ rhps, aq ` E 
” 
řH h1“h`1rh1 
` 
sh1 , πh1psh1q ˘ 
ˇ 
ˇ 
ˇ sh “ s, ah “ a 
ı 
, V π h psq “ Qπ 
h 
` 
s, πhpsq ˘ 
, 
where sh1`1 „ Php¨|sh1 , ah1q. The optimal state-action value function Q˚ h and the optimal 
state value function V ˚ h are defined by Q˚ 
hps, aq “ maxπ Q π hps, aq, V ˚ 
h psq “ maxπ V π h psq. 
By definition, both the state-action value function Qπ hps, aq and the state value function 
V π h psq are bounded by r0, Hs for any state s, action a and stage h. For any function V : S ÞÑ 
R, we denote by rPhV sps, aq “ Es1„Php¨|s,aqV ps1q the expected value of V after transitioning 
from state s given action a at stage h and rBhV sps, aq “ rhps, aq ` rPhV sps, aq where B is 
referred to as the Bellman operator. For each stage h P rHs and policy π, the Bellman 
178
equation, as well as the Bellman optimality equation, are presented as follows 
Qπ hps, aq “ rhps, aq ` rPhV 
π h`1sps, aq :“ rBhV 
π h`1sps, aq, 
Q˚ hps, aq “ rhps, aq ` rPhV 
˚ h`1sps, aq :“ rBhV 
˚ h`1sps, aq. 
We use regret to measure the performance of RL algorithms. It is defined as RegretpKq “ 
řK k“1 
` 
V ˚ 1 psk1q´V πk 
1 psk1q ˘ 
, where πk represents the agent’s policy at episode k. This definition 
quantifies the cumulative difference between the expected rewards that could have been 
obtained by following the optimal policy and those achieved under the agent’s policy across 
the first K episodes, measuring the total loss in performance due to suboptimal decisions. 
We consider linear function approximation in this work, where we adopt the misspecified 
linear MDP assumption, which is firstly proposed in Jin et al. (2020b). 
Assumption 5.3.1 (ζ-Approximate Linear MDP, Jin et al. 2020b). For any ζ ď 1, we say a 
MDP MpS,A, H, trhu, tPhuq is a ζ-approximate linear MDP with a feature map ϕ : SˆA ÞÑ 
Rd, if for any h P rHs, there exist d unknown (signed) measures µh “ ` 
µ p1q 
h , ¨ ¨ ¨ , µ pdq 
h 
˘ 
over S 
and an unknown vector θh P Rd such that for any ps, aq P S ˆ A, we have 
› 
›Php¨|s, aq ´ xϕps, aq,µhp¨qy › 
› 
TV ď ζ, 
ˇ 
ˇrhps, aq ´ xϕps, aq,θhy ˇ 
ˇ ď ζ, 
w.l.o.g. we assume @ps, aq P S ˆ A : }ϕps, aq} ď 1 and @h P rHs : }µhpSq} ď ? d, }θh} ď 
? d. 
The ζ-approximate linear MDP suggests that for any policy π, the state-action value 
function Qπ h can be approximated by a linear function of the given feature mapping ϕ up to 
some misspecification level, which is summarized in the following proposition. 
Proposition 5.3.2 (Lemma C.1, Jin et al. 2020b). For a ζ-approximate linear MDP, for 
any policy π, there exist corresponding weights twπ huhPrHs where wπ 
h “ θh ` ş 
V π h`1ps 
1qdµhps1q 
such that for any ps, a, hq P S ˆ A ˆ rHs, ˇ 
ˇQπ hps, aq ´ xϕps, aq,wπ 
hy ˇ 
ˇ ď 2Hζ. We have 
}wbπh}2 ď 2H ? d. 
Next, we introduce the definition of the suboptimal gap as follows. 
179
Definition 5.3.3 (Minimal suboptimality gap). For each s P S, a P A and step h P rHs, 
the suboptimality gap gaphps, aq is defined by ∆hps, aq “ V ˚ h psq ´ Q˚ 
hps, aq and the minimal 
suboptimality gap ∆ is defined by ∆ “ minh,s,a 
␣ 
∆hps, aq : ∆hps, aq ‰ 0 ( 
. 
Notably, a task with a larger ∆ means it is easier to distinguish the optimal action 
π˚ hpsq from other actions a P A, while a task with lower gap ∆ means it is more difficult to 
distinguish the optimal action. 
5.4 Proposed Algorithms 
5.4.1 Main algorithm: Cert-LSVI-UCB 
We begin by introducing our main algorithm Cert-LSVI-UCB, which is a modification 
of the Sup-LSVI-UCB (Vial et al., 2022). As presented in Algorithm 12, for each episode 
k, our algorithm maintains a series of index sets Cl k,h for each stage h P rHs and phase 
l. The algorithm design ensures that for any episode k, the maximum number of phases 
l is bounded by Lk ď maxtrlog4pk{dqs, 0u. During the exploitation step, for each phase l 
associated with the index set Cl k´1,h, the algorithm constructs the estimator vector wk 
h,l by 
solving the following ridge regression problem in Line 6 and Line 7: 
wk h,l Ð argmin 
wPRd 
λ}w} 2 2 ` 
ÿ 
τPCk´1 h,l 
` 
wJϕτ h ´ rτh ´ V̂ k 
h`1psτh`1q ˘2 . 
After calculating the estimator vector wk h,l in Line 8, the algorithm quantilizes wk 
h,l and 
pUk h,lq 
´1 to the precision of κl. Similar to Sup-LSVI-UCB (Vial et al., 2022), we note Ũk,´1 h,l 
is the quantized version of inverse covariance matrix pUk h,lq 
´1 rather than the inverse of 
quantized covariance matrix pŨk h,lq 
´1. The main difference between our implementation and 
that in Vial et al. (2022) is that we use a layer-dependent quantification precision κl instead 
of the global quantification precision κ “ 2´4L{d, which enables our algorithm get rid of the 
dependence on OplogKq in the maximum number of phases Lk. 
180
Algorithm 12 Cert-LSVI-UCB 
1: Set V k H`1psq “ 0 for all ps, kq P S ˆ rKs, Ck 
h,l “ H for all ph, lq P rHs ˆ N`, λ “ 16 
2: for episode k “ 1, ¨ ¨ ¨ , K do 
3: Set Lk “ maxtrlog4pk{dqs, 0u 
4: for step h “ H, ¨ ¨ ¨ , 1 do 
5: for phase l “ 1, ¨ ¨ ¨ , Lk ` 1 do 
6: Uk h,l “ λI ` 
ř 
τPCk´1 h,l ϕτ 
hpϕτ hqJ 
7: wk h,l “ pUk 
h,lq ´1 
ř 
τPCk´1 h,l ϕτ 
h 
` 
rτh ` V̂ k h`1ps 
τ h`1q 
˘ 
8: Ũk,´1 h,l “ κl 
P 
pUk h,lq 
´1{κl 
\ 
, w̃k h,l “ κl 
P 
wk h,l{κl 
\ 
where κl “ 0.01 ¨ 2´4ld´1 
9: end for 
10: V̂ k h psτhq, ¨, ¨, ¨ “ Cert-LinUCBpsτh; tw̃k 
h,lul, tŨk,´1 h,l ul, Lkq for all τ P rk ´ 1s 
11: end for 
12: Observe sk1 P S 
13: for step h “ 1, ¨ ¨ ¨ , H do 
14: ¨, πk hpskhq, lkhpskhq, fk 
h pskhq “ Cert-LinUCBpskh; tw̃k h,lul, tŨk,´1 
h,l ul, Lkq 
15: Ck h,lkhpskhq 
“ Ck´1 h,lkhpskhq 
Y tku if fk h pskhq “ 1 else Ck´1 
h,lkhpskhq 
16: Ck h,l “ Ck´1 
h,l for all l ‰ lkhpskhq 
17: Play πk hpskhq, set ϕk 
h “ ϕ ` 
skh, π k hpskhq 
˘ 
, receive rkh and observe skh`1 P S 
18: end for 
19: end for 
After obtaining w̃k h,l and Ũk,´1 
h,l , a subroutine, Cert-LinUCB, is called to calculate an 
optimistic value function V̂ k h psτhq for all historical states sτh in Line 10. Then the algorithm 
transits to stage h ´ 1 and iteratively computes w̃k h,l and Ũk,´1 
h,l for all phase l and stage 
h P rHs. 
In the exploration step, the algorithm starts to do planning from the initial state sk1. For 
each observed state skh, the same subroutine, Cert-LinUCB, will be called in Line 14 for the 
policy πk hpskhq, the corresponding phase lkhpskhq, and a flag fk 
h pskhq. If the flag fk h pskhq “ 1, the 
181
Algorithm 13 Cert-LinUCB : ` 
s; tw̃k h,lul, tŨk,´1 
h,l ul, L ˘ 
ÞÑ ` 
V̂ k h psq, πk 
hpsq, lkhpsq, fk h psq 
˘ 
1: input: s P S, @l : w̃k h,l P Rd, Ũk,´1 
h,l P Rdˆd, L P N` 
2: output: V̂ k h psq P R, πk 
hpsq P A, lkhpsq P N`, fk h psq P t0, 1u 
3: Ak h,1psq “ A, qV k 
h,0psq “ 0, V̂ k h,0psq “ H 
4: for phase l “ 1, ¨ ¨ ¨ , L ` 1 do 
5: Set Qk h,lps, aq “ 
@ 
ϕps, aq, w̃k h,l 
D 
6: Set πk h,lpsq “ argmaxaPAk 
h,l Qk 
h,lps, aq, V k h,lpsq “ Qk 
h,l 
` 
s, πk h,lpsq 
˘ 
7: if l ą L then 
8: return ` 
V̂ k h psq, πk 
hpsq, lkhpsq, fk h psq 
˘ 
“ ` 
V̂ k h,l´1psq, πk 
h,l´1psq, l, 1 ˘ 
9: else if γl ¨ maxaPAk h,lpsq }ϕps, aq}Ũk,´1 
h,l ě 2´l then 
10: return ` 
V̂ k h psq, πk 
hpsq, lkhpsq, fk h psq 
˘ 
“ ` 
V̂ k h,l´1psq, argmaxaPAk 
h,lpsq }ϕps, aq}Ũk,´1 h,l 
, l, 1 ˘ 
11: else if max ␣ 
V k h,lpsq ´ 3 ¨ 2´l, qV k 
h,l´1psq ( 
ą min ␣ 
V k h,lpsq ` 3 ¨ 2´l, V̂ k 
h,l´1psq ( 
then 
12: return ` 
V̂ k h psq, πk 
hpsq, lkhpsq, fk h psq 
˘ 
“ ` 
V̂ k h,l´1psq, πk 
h,l´1psq, l, 0 ˘ 
13: else 
14: V̂ k h,lpsq “ min 
␣ 
V k h,lpsq ` 3 ¨ 2´l, V̂ k 
h,l´1psq ( 
15: qV k h,lpsq “ max 
␣ 
V k h,lpsq ´ 3 ¨ 2´l, qV k 
h,l´1psq ( 
16: Ak h,l`1psq “ 
! 
a P Ak h,lpsq : Qk 
h,lps, aq ě V k h,lpsq ´ 4 ¨ 2´l 
) 
17: end if 
18: end for 
algorithm adds the index k to the index set Ck h,lkhpskhq 
in Line 15. Otherwise, the algorithm skips 
the current index k and all index sets remain unchanged. Finally, the algorithm executes 
policy πk hpskhq, receives reward rkh and observes the next state skh`1 in Line 17. 
5.4.2 Subroutine: Cert-LinUCB 
Next we introduce subroutine Cert-LinUCB, improved from Sup-Lin-UCB-Var (Vial 
et al., 2022) that computes the optimistic value function V̂ k h . The algorithm is described as 
182
follows. Starting from phase l “ 1, the algorithm first calculates the estimated state-action 
function Qk h,lps, aq as a linear function over the quantified parameter w̃k 
h,l and feature map-
ping ϕps, aq, following Proposition 5.3.2. After calculating the estimated state-action value 
function Qk h,lpsq, the algorithm computes the greedy policy πk 
h,lpsq and its corresponding 
value function V k h,lpsq. 
Similar to Sup-Lin-UCB-Var (Vial et al., 2022), our algorithm has several conditions 
starting from Line 7 to determine whether to stop at the current phase or to eliminate the 
actions and proceed to the next phase l ` 1, which are listed in the following conditions. 
‚ Condition 1: In Line 7, if the current phase l is greater than the maximum phase L, 
we directly stop at that phase and take the greedy policy on previous phase πk hpsq “ 
πk h,l´1psq. 
‚ Condition 2: In Line 9, if there exists an action whose uncertainty }ϕps, aq}Ũk.´1 h,l 
is 
greater than the threshold 2´lγ´1 l , our algorithm will perform exploration by selecting 
that action. 
‚ Condition 3: In Line 11, we compare the value of the pessimistic value function qV k h,lpsq 
and the optimistic value function V̂ k h,lpsq which will be assigned in Line 14 and Line 15, 
if the pessimistic estimation will be greater than the optimistic estimation, we will stop 
at that phase and take the greedy policy on previous phase πk hpsq “ πk 
h,l´1psq. Only in 
this case, the Algorithm 13 outputs flag fk h psq “ 0, which means this observation will 
not be used in Line 15 in Algorithm 12. 
‚ Condition 4: In the default case in Line 16, the algorithm proceeds to the next phase 
after eliminating actions. 
Notably, in Condition 4, since the expected estimation precision in the l-th phase is 
about Õp2´lq, our algorithm can eliminate the actions whose state-action value is significantly 
183
less than others, i.e., less than Õp2´lq, while retaining the remaining actions for the next 
phase. 
Specially, our algorithm differs from that in Vial et al. (2022) in terms of Condition 3 
to certify the performance of the estimation. In particular, a well-behaved estimation should 
always guarantee that the optimistic estimation is greater than the pessimistic estimation. 
According to Line 14 and Line 15, this is equivalent to the confidence region for l-th phase has 
intersection of the previous confidence region rqV k h,l´1psq, V̂ k 
h,l´1psqs. Otherwise, we hypothesis 
the estimation on l-th phase is corrupted by either misspecification or bad concentration 
event, thus will stop the algorithm. We will revisit the detail of this design later. 
It’s important to highlight that our algorithms provide unique approaches when compared 
with previous works. In particular, He et al. (2021b) does not eliminate actions and combines 
estimations from all layers by considering the minimum estimated optimistic value function. 
This characteristic prevents their algorithm from achieving a uniform PAC guarantee in the 
presence of misspecification. For a more detailed comparison with He et al. (2021b), please 
refer to Section 5.8.1. Additionally, Lykouris et al. (2021); Wei et al. (2022) focus on a 
model-selection regime where a set of base learners are employed in the algorithms, whereas 
we adopt a multi-phase approach similar with SupLinUCB rather than conducting model 
selection over base learners. 
5.5 Constant Regret Guarantee 
We present the regret analysis in this section. 
Theorem 5.5.1. Under Assumption 5.3.1, let γl “ 5pl ` 20 ` rlogpldqsqdH a 
logp16ldH{δq 
for some fixed 0 ă δ ă 1{4. With probability at least 1 ´ 4δ, if the minimal suboptimality 
gap ∆ satisfies ∆ ą Ω̃ ` ? dH2ζ 
˘ 
, then for all K P N`, the regret of Algorithm 12 is upper 
184
bounded by 
RegretpKq ď Õ ` 
d3H5∆´1 logp1{δq ˘ 
. 
This regret bound is constant w.r.t. the episode K. 
Theorem 5.5.1 demonstrates a constant regret bound with respect to number of episodes 
K. Compared with Papini et al. (2021a), our regret bound does not require any prior 
assumption on the feature mapping ϕ, such as the UniSOFT assumption made in Papini 
et al. (2021a). In addition, compared with the previous logarithmic regret bound He et al. 
(2021a) in the well-specified setting, our constant regret bound removes the logK factor, 
indicating the cumulative regret no longer grows w.r.t. the number of episode K, with high 
probability. 
Remark 5.5.2. As discussed in Zhang et al. (2023c) in the misspecified linear bandits, Our 
high probability constant regret bound does not violate the lower bound proved in Papini 
et al. (2021a), which says that certain diversity condition on the contexts is necessary to 
achieve an expected constant regret bound. When extending this high probability constant 
regret bound to the expected regret bound, we have 
ErRegretpKqs ď Õ ` 
d3H5∆´1 logp1{δq ˘ 
¨ p1 ´ δq ` δK, 
which depends on the number of episodes k. To obtain a sub-linear expected regret, we can 
choose δ “ 1{K, which yields a logarithmic expected regret Õpd3H5∆´1 logKq and does not 
violate the lower bound in Papini et al. (2021a). 
Remark 5.5.3. Du et al. (2019) provide a lower bound showing the interplay between the 
misspecification level ζ and suboptimality gap ∆ in a weaker setting, which we discuss in 
detail in Section 5.8.2. Along with the result from Du et al. (2019), our results suggests 
that ignoring the dependence on H, ζ “ Õp∆{ ? dq plays an important seperation for if a 
misspeficied model can be efficiently learned. This result is also aligned with the positive 
result and negative result for linear bandits (Lattimore et al., 2020; Zhang et al., 2023c). 
185
5.6 Highlight of Proof Techniques 
In this section, we highlight several major challenges in obtaining the constant regret under 
misspecified linear MDP assumption and how our method, especially the certified estimator, 
tackles these challenges. 
5.6.1 Technical challenges 
Challenge 1. Achieving layer-wise local estimation error. In the analysis of the 
value function under misspecified linear MDPs, we need to follow the multi-phase estimation 
strategy (Vial et al., 2022) to eliminate suboptimal actions and improve the robustness of the 
next phase estimation. Similar approaches have been observed in Zhang et al. (2023c); Chu 
et al. (2011) within the framework of (misspecified) linear bandits. However, unlike linear 
bandits, when constructing the empirical value function V̂h for stage h in linear MDPs, Jin 
et al. (2020b) requires a covering statement on value functions to ensure the convergence of 
the regression, which is written by: (see Lemma D.4 in Jin et al. (2020b) for details) 
› 
› 
› 
ř 
τPCϕ τ h 
“ 
V̂ k h`1ps 
τ q ´ ErV̂ k h`1ps 
τ qs ‰ 
› 
› 
› 
U´1 h 
ď ÕH 
´b 
d logp|C|q ` logp|Vk h`1|{δq ` 
? dκ 
¯ 
, (5.6.1) 
where we employ notation ÕH to obscure the dependence on H to simplify the presentation. 
We use the notation Vk h`1 to denote as an κ-covering for the value functions V̂ k 
h`1. Takemura 
et al. (2021); Vial et al. (2022) used quantification instead of the covering number, but this 
approach still encounters the issue of taking the union bound across the set of value functions, 
thereby incorporating the dependency on the cardinality of this set. 
In the multi-phase algorithm, the regression employs a distinct set C “ Ck h,l for each 
phase l. However, all these regressions use the overall empirical value function V̂ k h`1 from the 
subsequent stage h ` 1, which is formulated using all pairs of parameters ␣ 
wk h,ℓ,U 
k h,ℓ 
( 
ℓ in L 
phases. Consequently, the covering number log |Vk h`1| is directly proportional to the number 
of phases L “ OplogKq. 
186
Therefore, when analyzing any single phase l, prior analysis cannot eliminate the logK 
term from (5.6.1) to achieve a local estimation error independent that is independent of the 
logarithmic number of global episodes logK. Furthermore, due to the algorithm design of 
previous methods (Vial et al., 2022), additional logK terms may be introduced, induced by 
global quantification (i.e., εtol “ d{ ? Kq. 
Challenge 2. Achieving constant regret from local estimation error In misspeci-
fied linear bandits, Zhang et al. (2023c) concludes their proof by controlling ř8 
k“1 1rV ˚ 1 psk1q´ 
V π 1 psk1q ě ∆s2. Although it is trivial showing that rounds with instantaneous regret V ˚ 
1 psk1q´ 
V π 1 psk1q ă ∆ is optimal in bandits (i.e., V ˚ 
1 psk1q “ V π 1 psk1q), previous works fail to reach a sim-
ilar result for RL settings. This difficulty arises from the randomness inherent in MDPs: 
Consider a policy π that is optimal at the initial stage h “ 1. After the initial state and 
action, the MDP may transition to a state s1 2 with a small probability p where the policy π 
is no longer optimal, or to another state s2 where π remains optimal until the end. In this 
context, the gap between V ˚ 1 ps1q and V π 
1 ps1q can be arbitrarily small, given a sufficiently 
small p ą 0: 
V ˚ 1 ps1q ´ V π 
1 ps1q “ p ` 
V ˚ 2 ps1 
2q ´ V π 2 ps1 
2q ˘ 
` p1 ´ pq ` 
V ˚ 2 ps2q ´ V π 
2 ps2q ˘ 
“ p ` 
V ˚ 2 ps1 
2q ´ V π 2 ps1 
2q ˘ 
. 
Therefore, one cannot easily draw a constant regret conclusion simply by controlling the 
summation ř8 
k“1 1rV ˚ 1 psk1q ´ V π 
1 psk1q ě ∆s since the gap between V ˚ 1 psk1q ´ V π 
1 psk1q needs to 
be further fine-grained controlled. In short, the existence of ∆ describing the minimal gap 
between V ˚psq ´ Q˚ps, aq cannot be easily applied to controlling regret V ˚psq ´ V πpsq. 
5.6.2 A novel approach: Cert-LinUCB 
We introduce the technical details in designing our new subroutine, Cert-LinUCB, to tackle 
Challenge 1. In the addition of using ‘local quantification’ which ensure the quantification 
2We employ the RL notations and set h “ 1 for the ease of comparison. 
187
error of each phase l depend on the local phase Õplq instead of the global parameter logK, 
Algorithm 13 eliminates the logK dependence from log |V | by employing certified estimator. 
Considering the concentration term we need to control for each phase l: 
› 
› 
› 
ř 
τPCk h,l ϕτ 
h 
“ 
V̂ k h`1ps 
τ q ´ ErV̂ k h`1psτ qs 
‰ 
› 
› 
› 
pUk h,lq 
´1 , 
as discussed in Challenge 1, the function class V̂k h`1 Q V̂ k 
h`1 involves L “ OplogKq parame-
ters, leading to a logK dependence in the results when using traditional routines. The idea 
of certified estimator is to get rid of this by not directly controlling log |Vk h`1|. Instead, certi-
fied estimator establishes a covering statement for the value function class Vk h`1,l` 
Q V̂ k h`1,l` 
, 
where V̂ k h`1,l` 
is the value function that only incorporates the first l` phases of parameters ␣ 
wk h,ℓ,U 
k h,ℓ 
( 
ℓ . Under this framework, the covering statement becomes: 
Lemma 5.6.1 (Lemma 5.9.4, informal). Let V̂ k h`1,l` 
be the output of Algorithm 13 termi-
nated at phase L “ l`, then with probability is at least 1 ´ 2δ, 
› 
› 
› 
ř 
τPCk h,l ϕτ 
h 
“ 
V̂ k h`1,l` 
psτ q ´ ErV̂ k h`1,l` 
psτ qs ‰ 
› 
› 
› 
pUk h,lq 
´1 ď γl,l` “ 5l`dH 
a 
logp16ldH{δq. 
To apply Lemma 5.6.1, it is essential to bound the distance between V̂ k h`1,l` 
and V̂ k h`1. 
For this purpose, we maintain a monotonic sequence of the optimistic value function V̂ k h`1,l 
and the pessimistic value function qV k h`1,l, ensuring that 
qV k h`1,1psq ď qV k 
h`1,2psq ď ¨ ¨ ¨ ď qV k h`1,lkhpsq´1psq 
ď V̂ k h`1psq “ V̂ k 
h`1,lkhpsq´1psq ď ¨ ¨ ¨ ď V̂ k h`1,2psq ď V̂ k 
h`1,1psq. (5.6.2) 
This monotonicity is guaranteed according to Line 11 in Cert-LinUCB, where the process is 
terminated once (5.6.2) is violated. As a result, we can control the distance between V̂ k h`1,l` 
and V̂ k h`1 as the following lemma. 
Lemma 5.6.2 (Lemma 5.9.2, informal). There is a faithful extension of V̂ k h`1,l` 
to every 
l` P N` that |V̂ k h psq ´ V̂ k 
h,l` psq| ď 6 ¨ 2´l` always holds. 
188
Following these results, combining Lemma 5.6.2 and Lemma 5.6.1 together obtains a 
local concentration bound for each phase l that is independent of logK when choosing 
l` “ l ` Õplogpldqq. 
Lemma 5.6.3 (Lemma 5.9.5, informal). With probability at least 1 ´ 2δ, for any pk, h, lq P 
rKs ˆ rHs ˆ N`: › 
› 
› 
ř 
τPCk´1 h,l ϕτ 
h 
` 
rPhV̂ k h`1sps 
τ h, a 
τ hq ´ V̂ k 
h`1ps τ h`1q 
˘ 
› 
› 
› 
pUk h,lq 
´1 ď 1.1γl. 
As a result of our improved concentration analysis, we can achieve a local estimation 
error for the estimated value function in each phase l: 
Lemma 5.6.4 (Lemma 5.9.6, informal). With high probability, for any pk, h, sq P rKsˆrHsˆ 
S, l P rlkhpsq ´ fk h psqs, al P Ak 
h,lpsq, we have ˇ 
ˇQk h,lps, aq ´ rBhV̂ 
k h`1sps, aq 
ˇ 
ˇ ď 2 ¨ 2´l ` Op ? dHζq. 
Lemma 5.6.4 bounds the estimation error for any state s by the phase lkhpsq where lkhpsq 
indicates the layer at which Algorithm 13 terminates. As the early phases cannot provide 
sufficient accuracy due to a lack of data, we also need to analyze the conditions under which 
Line 11 is triggered in Algorithm 13. 
Lemma 5.6.5 (Lemma 5.9.8, informal). With probability at least 1 ´ 2δ, for any pk, hq P 
rKs ˆ rHs, Line 11 in Algorithm 13 can only be triggered on phase l ě Ω̃ ` 
logp1{ζq ˘ 
. 
Lemma 5.6.5 delivers a clear message: the trigger of Line 11 is related to the misspecifi-
cation level ζ. In the well-specified setting, Line 11 will never be triggered (l ě 8). When 
the misspecification level is large, then Line 11 will be more likely triggered, indicating it’s 
harder to get higher precise estimation via higher lkhpsq, according to Lemma 5.6.4. 
In order to bound the number of suboptimality gap taken by Cert-LSVI-UCB, we start 
with the following standard decomposition 
V ˚ h pskhq´V πk 
h pskhq “ ` 
V ˚ h pskhq ´ V̂ k 
h pskhq ˘ 
` ` 
V̂ k h pskhq ´ V πk 
h pskhq ˘ 
“ ` 
V ˚ h pskhq ´ V̂ k 
h pskhq ˘ 
` řH 
h1“h 
´ 
V̂ k h1pskh1q ´ rBhV̂ 
k h1`1s 
` 
skh1 , πk h1pskh1q 
˘ 
¯ 
` řH 
h1“hη k h1 . 
189
where ηkh “ rPhpV̂ k h`1 ´V πk 
h`1qs ` 
skh, π k hpskhq 
˘ 
´ ` 
V̂ k h`1ps 
k h`1q´V πk 
h`1pskh`1q ˘ 
is a zero-mean random 
variable induced by the transition kernel. We can bound each of the factors using standard 
regret analysis on the basis created by combining Lemma 5.6.4 and Lemma 5.6.5: 
1. Global underestimation error V ˚ h pskhq ´ V̂ k 
h pskhq. (see Lemma 5.9.25) 
2. Local overestimation error V̂ k h pskhq ´ rBhV̂ 
k h`1sps 
k h1 , πk 
h 
` 
skhq ˘ 
. (see Lemma 5.9.26) 
3. Transition noise ηkh. (see Lemma 5.9.28) 
In general, we can reach the following results, which provide an local regret upper bound for 
arbitrary index subsets which is independent from the number of total episodes. 
Lemma 5.6.6 (Lemma 5.9.29, Informal). With high probability, for any index set K and 
any ε that is comparably large against ζ, it satisfies that 
ř 
kPK ` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ď 0.49|K|ε ` Õ ` 
d3H4ε´1 ` a 
H3|K| ˘ 
. 
Note that for index set K “ “ 
k : V ˚ h pskhq ´ V πk 
h pskhq ě ε ‰ 
, the regret enjoys a trivial lower 
bound that ř 
kPK ` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ě |K|ε. We thus can reach the following result. 
Lemma 5.6.7 (Lemma 5.9.12, Informal). With high probability, for any ε ą Ω̃p ? dH2ζq 
and h P rHs, Cert-LSVI-UCB ensures ř8 
k“1 1 “ 
V ˚ h pskhq ´ V πk 
h pskhq ě ε ‰ 
ď Õ ` 
d3H4ε´2 ˘ 
. 
Remark 5.6.8. He et al. (2021b) achieved a uniform-PAC bound for (well-specified) linear 
MDP, which states as 
w.h.p., @ϵ ą 0, ř8 
k“1 1rV ˚ 1 psk1q ´ V πk 
1 psk1q ě ϵs ď Õpd3H5ϵ´2q, (5.6.3) 
comparing (5.6.3) with Lemma 5.6.7 on well-specified setting where ζ “ 0, one can find that 
our result is better than He et al. (2021b) under stronger condition: Lemma 5.6.7 ensures this 
uniform-PAC result under all stage h P rHs while He et al. (2021b) only ensure the initial 
statement. Due to the randomness of MDP discussed in Challenge 2, the guarantee for 
190
h “ 1 cannot be easily generated to any h P rHs. Second, our result Õpd3H4ϵ´2q improves 
He et al. (2021b) by a factor H. This is because a more efficient data selection strategy 
which we will discuss in detail in Section 5.8.1. 
5.6.3 Settling the gap between V ˚ ´ V π and V ˚ ´ Q˚ 
According to Challenge 2, the regret in episodes where V ˚ 1 psk1q ´ V πk 
1 psk1q ď ∆ is non-
zero since the minimal suboptimality gap assumption ∆ only guarantees ∆k h “ V ˚ 
h pskhq ´ 
Q˚ h 
` 
skh, π k hpskhq 
˘ 
R p0,∆q but put no restrictions on V ˚ h pskhq ´ V πk 
h pskhq. 
Notice that the regret V ˚ h pshq ´ V πk 
h pshq in episode k is the expectation of cumulative 
suboptimality gap řH 
h“1∆ k h taking over trajectory tskhuHh“1. In addition, the variance of the 
random variable can be self-bounded according to 
Var ” 
řH h“1∆ 
k h 
ı 
ď E ”´ 
řH h“1∆ 
k h 
¯2ı 
ď H2E ” 
řH h“1∆ 
k h 
ı 
“ H2 ` 
V ˚ 1 psk1q ´ V πk 
1 psk1q ˘ 
. 
As Freedman inequality (Lemma 5.9.30) implies řT 
t“1Varrη ts ď aC and 
řT t“1Varrη 
ts ď vC 
only happens with small probability for every C with proper constant a and v, together with 
a union bound statement C, we can reach the following statement indicates the cumulative 
regret can be upper bounded using the cumulative suboptimality gap: 
Lemma 5.6.9 (Lemma 5.9.14, Informal). The following statement holds with high proba-
bility: řK 
k“1 
` 
V ˚ h pshq ´ V πk 
h pshq ˘ 
ď Õ ´ 
řK k“1 
řH h“1∆ 
k h ` H2 
¯ 
. 
In addition, since the loss on the state-value function V ˚ h pskhq ´V πk 
h pskhq is a upper bound 
for the sub-optimality gap ∆k h, we are able to show that the cumulative suboptimality 
gap is constantly bounded when the minimal suboptimality gap is sufficiently large as in 
Lemma 5.9.13: řK 
k“1 
řH h“1∆ 
k h “ 
řK k“1 
řH h“1 
´ 
∆ ¨ 1 ” 
∆k h ě ∆ 
ı 
` şH 
∆ 1 ” 
∆k h ě ε 
ı 
dε ¯ 
ď řK 
k“1 
řH h“1 
´ 
∆ ¨ 1 ” 
V ˚ h pskhq ´ V πk 
h pskhq ě ∆ ı 
` şH 
∆ 1 ” 
V ˚ h pskhq ´ V πk 
h pskhq ě ε ı 
dε ¯ 
. 
191
Note that the final summation can be upper bounded by Õ ` 
d3H5∆´2q using Lemma 5.6.7. 
Together with Lemma 5.6.9, we reach the desired statement that Cert-LSVI-UCB achieves 
a constant regret bound when the misspecification is sufficiently small against the minimal 
suboptimality gap. 
5.7 Conclusion 
In this chapter, we proposed a new algorithm, called certified estimator, for reinforcement 
learning with a misspecified linear function approximation. Our algorithm is parameter-free 
and does not require prior knowledge of misspecification level ζ or the suboptimality ∆. 
Our algorithm is based on a novel certified estimator and provides the first constant regret 
guarantee for misspecified linear MDPs and (well-specified) linear MDPs. There are still 
some future works resulting from current algorithm. First, it is still an open question that 
whether the dependence on the planning horizon and dimension d,H is optimal for instance-
dependent regret bound, as in the well-specified case, the regret lower bound is Ωpd ? H3Kq 
(Zhou et al., 2021b), which has been recently attained by He et al. (2022a); Agarwal et al. 
(2022). Second, our work propose a new open question that if it possible to fill the gap 
between the positive result in our work and the negative result in Du et al. (2019). We 
believe it’s important in both theory and practice to understand how much misspecification 
level can be tolerated to efficiently learn the algorithm. 
5.8 Additional Discussions 
5.8.1 Comparison with He et al. (2021b) 
It is worth comparing our algorithm with He et al. (2021b), which also provides a uniform 
PAC bound for linear MDPs. Both our algorithm and theirs utilize a multi-phase structure 
that maintains multiple regression-based value function estimators at different phases. De-
192
spite this similarity, there are several major differences between our algorithm and that in 
He et al. (2021b), which are highlighted as follows: 
1. In Line 7 of Algorithm 12, when calculating the regression-based estimator, for different 
phase l, we use the same regression target V̂ k h`1, while their algorithm uses different 
V k h`1,l for different phase l. 
2. When aggregating the regression estimators over all different Lk phases, we follow 
the arm elimination method as in Chu et al. (2011), while He et al. (2021b) simply 
take the point-wise minimum of all estimated state-action functions, i.e., Qps, aq “ 
minlPrLks Q l k,hps, aq. 
3. When calculating the phase lkhpskhq for a trajectory sk1, s k 2, ¨ ¨ ¨ , skH , He et al. (2021b) 
require that the phase lkhpskhq to be monotonically decreasing with respect to the stage 
h, i.e., lkhpskhq ď lkh´1ps k h´1q (see line 19 in Algorithm 2 in He et al. (2021b)). Such a 
requirement will lead to a poor estimation for later stages and thus increase the sample 
complexity. In contrast, we do not have this requirement or any other requirements 
related to lkhpskhq and lkh´1ps k h´1q. 
As a result, by 3, He et al. (2021b) have to sacrifice some sample complexity to make their 
algorithm work for different target value functions V k h`1,l. As a comparison, since we use the 
same regression target for different phase l, we do not have to make such a sacrifice in 3. 
Moreover, by 2, He et al. (2021b) cannot deal with linear MDPs with misspecification, while 
our algorithm can handle misspecification as in Vial et al. (2022). 
5.8.2 Discussion on Lower Bounds of Sample Complexity 
We present a lower bound from Du et al. (2019) to better illustrate the interplay between 
the misspecification level ζ and the suboptimality gap ∆. 
193
Assumption 5.8.1 (Assumption 4.3, Du et al. 2019, ζ-Approximate Linear MDP). There 
exists ζ ą 0, θh P Rd and µh : S ÞÑ Rd for each stage h P rHs such that for any ps, a, s1q P 
S ˆ A ˆ S, we have ˇ 
ˇPhps1|s, aq ´ xϕps, aq,µhps1qy ˇ 
ˇ ď ζ and ˇ 
ˇrps, aq ´ xϕps, aq,θhy ˇ 
ˇ ď ζ. 
Theorem 5.8.2 (Theorem 4.2, Du et al. 2019). There exists a family of hard-to-learn linear 
MDPs with action space |A| “ 2 and a feature mapping ϕps, aq satisfying Assumption 5.8.1, 
such that for any algorithm that returns a 1{2-optimal policy with probability 0.9 needs to 
sample at least Ωpmint|S|, 2H , exppdζ2{16quq episodes. 
Remark 5.8.3. As claimed in Du et al. (2019), Theorem 5.8.2 suggests that when misspec-
ification in the ℓ8 norm satisfies ζ “ Ωp∆ a 
H{dq, the agent needs an exponential number 
of episodes to find a near-optimal policy, where ∆ “ 1{2 in their setting. It is worth noting 
that Assumption 5.8.1 is a ℓ8 approximation for the transition matrix. Such a ℓ8 guarantee 
(} ¨ }8 ď ζ) is weaker than the ℓ1 guarantee (} ¨ }1 ď ζ) provided in Assumption 5.3.1. So 
it’s natural to observe a positive result when making a stronger assumption and a negative 
result when making a weaker assumption. In addition, despite of this difference, one could 
find that ζ „ ∆{ ? d plays a vital role in determining if the task can be efficiently learned. 
Similar positive and negative results are also provided in Lattimore et al. (2020); Zhang et al. 
(2023c) in the linear contextual bandit setting (a special case of linear MDP with H “ 1). 
5.9 Proofs 
5.9.1 Constant Regret Guarantees for Cert-LSVI-UCB 
In this section, we present the proof of Theorem 5.5.1. To begin with, we recap the notations 
used in the algorithm and introduce several shorthand notations that would be employed for 
the simplicity of latter proof. The notation table is presented in Table 5.2.Any proofs not 
included in this section are deferred to Section 5.9.2. 
194
Notation Meaning 
ζ Misspecification level of feature map ϕh. (see Definition 5.3.1) 
∆ Minimal suboptimality gap among ∆h. (see Definition 5.3.3) 
skh, a k h States and actions introduced in the episode k by the policy πk. 
Qπ hps, aq, V π 
h psq Ground-truth state-action value function and state value function of policy π. 
Q˚ hps, aq, V ˚ 
h psq The optimal ground-truth state-action value function and state value function. 
∆hps, aq Suboptimal gap with respect to the optimal policy π˚. (see Definition 5.3.3) 
Ph,Bh The ground-truth transition kernel and the Bellman operator. 
κl The quantification precision in the phase l. (see Algorithm 12) 
γl The confidence radius in the phase l. (see Theorem 5.5.1) 
Ck h,l Index sets during phase l in the episode k. (see Algorithm 12) 
wk h,l,U 
k h,l Empirical weights and covariance matrix in the phase l. (see Algorithm 12) 
w̃k h,l, Ũ 
k h,l Quantified version of wk 
h,l and Uk h,l. (see Algorithm 12) 
V̂ k h psq The overall optimistic state value function. (see Algorithm 13) 
Qk h,lps, aq Empirical state-action value function in phase l. (see Algorithm 13) 
V k h,lpsq Empirical state value function in phase l. (see Algorithm 13) 
V̂ k h,lpsq Optimistic state value function in phase l. (see Definition 5.9.1) 
qV k h,lpsq Pessimistic state value function in phase l. (see Algorithm 13) 
πk h Policy played in the episode k. (see Algorithm 13) 
πk h,l Policy induced at state s during phase l of episode k. (see Algorithm 13) 
lkhpsq The index of the phase at which state s stops in episode k. (see Algorithm 13) 
ϕk h The feature vector observed in the episode k. (see Algorithm 12) 
Vk h,l Function family of all optimistic state function V̂ k 
h,l. (see Definition 5.9.1) 
γl,l` The confidence radius with covering on phase l`. (see Definition 5.9.3) 
l` The phase offsets for the covering statement. (see Lemma 5.9.5) 
χ The inflation on misspecification. (see Lemma 5.9.6) 
Lζ The deepest phase that tolerance ζ misspecification. (see Lemma 5.9.8). 
Lε The shallowest phase that guarantees ε accuracy. (see Lemma 5.9.9). 
∆k h The sub-optimaility gap of played policy πk 
h at state skh. (see Lemma 5.9.13) 
G1,G2,G3 The event defined in Definition 5.9.3, Definition 5.9.27 and Definition 5.9.10. 
Table 5.2: Notations used in algorithm and proof 
195
5.9.1.1 Quantized State Value Function set Vk h,l 
To begin our proof, we first extend the definition of V̂ k h,l to arbitrary l and give a formal 
definition of the state value function class Vk h,l as we skip the detail of this definition in 
Section 5.6. 
Definition 5.9.1. We extend the definition of state value function V̂ k h,l to any tuple pk, h, lq P 
rKs ˆ rHs ˆ N` by 
V̂ k h,l, ¨, ¨, ¨ “ Cert-LinUCB 
` 
s; tw̃k h,ℓu 
l ℓ“1, tŨk,´1 
h,ℓ u l ℓ“1, l 
˘ 
We also define the state value function family Vk h,l be the set of all possible V̂ k 
h,l. 
Vk h,l “ 
! 
V̂ k h,l 
ˇ 
ˇ 
ˇ V̂ k h,l, ¨, ¨, ¨ “ Cert-LinUCB 
` 
s; tw̃¨ ¨,ℓu 
l ℓ“1, tŨ¨,´1 
¨,ℓ u l ℓ“1, l 
˘ 
) 
where tw̃¨ ¨,ℓu 
l ℓ“1 and tŨ¨,´1 
¨,ℓ ulℓ“1 are referring to any possible parameters generated by Line 8 
in Algorithm 12. 
It is worth noting that one can check the definition of V̂ k h,l here is consistent with those 
computed in Algorithm 13 with l ă lkhpsq. Therefore, we will not distinguish between the 
notations in the remainder of the proof. 
The following lemma controls the distance between V̂ k h psq and V̂ k 
h,lpsq for any phase l. 
Lemma 5.9.2. For any pk, h, sq P rKs ˆ rHs ˆ S, l P rlkhpsq ´ 1s, it holds that 
qV k h,lpsq ď V̂ k 
h psq ď V̂ k h,lpsq, |V̂ k 
h psq ´ V̂ k h,lpsq| ď 6 ¨ 2´l. 
Moreover, for any tuple pk, h, s, l`q P rKs ˆ rHs ˆ S ˆ N`, the difference |V̂ k h psq ´ V̂ k 
h,l` psq| 
is bounded by 6 ¨ 2´l` , following the extension of the definition scope of V̂ k h,l` 
as outlined in 
Definition 5.9.1. 
Lemma 5.9.2 suggests that given any phase l`, V̂ k h,l is close to V̂ k 
h . This enables us to 
construct covering on V̂ k h using the covering on V̂ k 
h,l. 
196
5.9.1.2 Concentration of State Value Function V̂ k h psq 
In this subsection, we provide a new analysis for bounding the self-normalized concentration 
of › 
› 
› 
ř 
τ ϕ τ h 
` 
rPhV̂ k h spsτh, a 
τ hq ´ V̂ k 
h psτh`1q ˘ 
› 
› 
› 
U´1 to get rid of the log k factor in Vial et al. (2022). 
To facilitate our proof, we define the filtration list Fk h “ 
! 
␣ 
sji , a j i 
(H,k´1 
i“1,j“1 , ␣ 
ski , a k i 
(h 
i“1 
) 
. 
It is easy to verify that skh, a k h are both Fk 
h -measurable. Also, for any function V built on 
Fk h , rPhV spskh, a 
k hq ´ V pskh`1q is Fk 
h`1-measurable and it is also a zero-mean random variable 
conditioned on Fk h . 
The first lemma we provide is similar with Vial et al. (2022), which shows the self-
normalized concentration property for each phase l and any function V P Vk h,l. 
Definition 5.9.3. For some fixed mapping l ÞÑ l` “ l`plq that l` ě l, we define the bad 
event as 
B1pk, h, l, V q “ 
#› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV spsτh, a τ hq ´ V psτh`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ą γl,l` 
+ 
. 
The good event is defined by G1 “ ŞK 
k“1 
ŞH h“1 
Ş 
lě1 
Ş 
V PVk h,l` 
BA 1pk, h, l, V q where we define 
γl,l` “ 5l`dH a 
logp16ldH{δq “ ÕpldH logpδ´1qq. 
Lemma 5.9.4. The good event G1 defined in Definition 5.9.3 happens with probability at 
least 1 ´ 2δ. 
Lemma 5.9.4 establishes the concentration bounds for any given phase l. However, the 
total number of phases for the state value function V k h psq can be bounded only trivially 
byl “ OplogKq, resulting in logK dependence. To address this issue, the following lemma, 
as we sketched in Section 5.6.2, proposes a method to eliminate this logarithmic factor: 
Lemma 5.9.5. Under event G1, for any pk, h, lq P rKs ˆ rHs ˆ N`, › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV̂ k h`1sps 
τ h, a 
τ hq ´ V̂ k 
h`1ps τ h`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 1.1γl. (5.9.1) 
where we set γl “ γl,l` with l` “ l ` 20 ` rlogpldqs. 
197
Then Lemma 5.9.5 immediately yields the following lemma regarding the estimation error 
of the state-action value function Qk h,l: 
Lemma 5.9.6. Under event G1, for any pk, h, sq P rKs ˆ rHs ˆ S, l P rlkhpsq ´ fk h psqs, al P 
Ak h,lpsq, 
ˇ 
ˇQk h,lps, aq ´ rBhV̂ 
k h`1sps, aq 
ˇ 
ˇ ď 2 ¨ 2´l ` χ 
? lζ (5.9.2) 
where we define χ “ 12 ? dH. 
Lemma 5.9.6 build an estimation error for any l P rlkhpsq ´ 1s. As we mentioned in 
the algorithm design, a larger l here will lead to more precise estimation (a smaller 2´l 
term in (5.9.2)) but will suffer from a larger covering number (a larger γl term in (5.9.2)). 
Following a similar proof sketch from Vial et al. (2022), the next lemma shows that any 
action that is not eliminated has a low regret, 
Lemma 5.9.7. Fix some arbitrary L0 ě 1 and let χ “ 12 ? dH. Under event G1, for any 
pk, h, sq P rKs ˆ rHs ˆ S, l P rmintL0, l k hpsq ´ fk 
h psqus, al`1 P Ak h,l`1psq, 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, al`1q ď 8 ¨ 2´l 
` 2l ¨ χ a 
L0ζ. 
5.9.1.3 The Impact of Misspecification Level ζ 
Next, we are ready to show the criteria where Line 11 in Algorithm 13 will be triggered, 
which shows the impact of misspecification on this multi-phased estimation. 
Lemma 5.9.8. Under event G1, for any pk, hq P rKs ˆ rHs such that fk h pskhq “ 0, we have 
lkhpskhq ą Lζ where Lζ is the maximal integer satisfying 2´Lζ ě χL1.5 ζ ζ for χ “ 12 
? dH, i.e., 
Lζ “ Ωplogp1{ζqq. 
Equipped with Lemma 5.9.8, the following lemma suggests that how much estimation 
precision ε can be achieved by accumulating the error 2´lkhpskhq that occurred in Lemma 5.9.6. 
198
Lemma 5.9.9. Under event G1 and for all ε ą 0, define Lε to be the minimal integer 
satisfying 2´Lε ď 0.01ε{H, i.e., Lε “ r´ logp0.01ε{Hqs. When Lε ď Lζ , then for any 
K Ď rKs, h P rHs, 
ÿ 
kPK 2´lkhpskhq 
ď 0.01|K| ¨ ε{H ` 212LεdHγ2 Lε 
¨ ε´1. 
The relationship between Lε ď Lζ can be translated to the relationship between ε and ζ. 
We characterize this condition as follows: 
Definition 5.9.10. Condition Gε is defined for a given ε, and is satisfied if Lζ ě Lε where 
Lε is the minimal integer satisfying 2´Lε ď 0.01ε{H and Lζ is the maximal integer satisfying 
2´Lζ ě χL1.5 ζ ζ. 
Lemma 5.9.11. If ε ě Ω ` ? dH2ζ log2p1{ζq 
˘ 
, then Gε is satisfied. 
Proof. If ε ě Ω ` ? dH2ζ log2p1{ζq 
˘ 
, we have 
2´Lε ě 0.005ε{H ě 2χL1.5 ζ ζ ě 2´Lζ . 
where the first inequality is given by the definition of Lε, the last inequality is given by the 
definition of Lζ , and the second inequality holds since HχL1.5 ζ ď O 
` ? dH2 log2p1{ζq 
˘ 
, and 
the last inequality is given by the definition of Lε and Lζ , respectively. Since 2´l decreases 
as l increases, we can conclude that Lε ď Lζ . 
The above analysis of the interplay between misspecification level ζ and precision ε yields 
the following important lemma in our proof, showing a local decision error across all h P rHs: 
Lemma 5.9.12. Under Assumption 5.3.1, let γl “ 5pl ` 20 ` rlogpldqsqdH a 
logp16ldH{δq, 
for some fixed 0 ă δ ă 1{3. With probability at least 1´3δ, for any ε ą Ω ` ? dH2ζ log2p1{ζq 
˘ 
and h P rHs, we have 
8 ÿ 
k“1 
1 ” 
V ˚ h pskhq ´ V πk 
h pskhq ě ε ı 
ď O ` 
d3H4ε´2 log4pdHε´1 q logpδ´1 
qι ˘ 
, 
199
where ι refers to some polynomial of log logpdHε´1δ´1q. This can also be written as 
Pr ” 
Dε ą ε0, h P rHs, 8 ÿ 
k“1 
1 ” 
V ˚ h pskhq ´ V πk 
h pskhq ą ε ı 
ą fpε, δq 
ı 
ď δ. 
with ε0 “ Ω̃p ? dH2ζq and fpε, δq “ Õpd3H4ε´2 logpδ´1qq. 
5.9.1.4 From Local Step-wise Decision Error to Constant Regret 
The next lemma shows that the total incurred suboptimality gap is constant if the minimal 
suboptimality gap ∆ satisfies ∆ ą ε0. 
Lemma 5.9.13. Suppose an RL algorithm Alg. satisfies 
Pr ” 
Dε ą ε0, h P rHs, 8 ÿ 
k“1 
1 ” 
V ˚ h pskhq ´ V πk 
h pskhq ą ε ı 
ą fpε, δq 
ı 
ď δ, 
such that fpε, δq “ ÕpC1{ε`C2{ε 2q where C1, C2 ą 0 are constant in ε, but may depend on 
other quantities such as d,H, logpδ´1q. If the minimal suboptimality gap ∆ satisfies ∆ ą ε0, 
then K ÿ 
k“1 
H ÿ 
h“1 
∆k h ď ÕpC2H{∆ ` C1Hq 
where ∆k h “ ∆h 
` 
skh, π k hpskhq 
˘ 
“ V ˚ h pskhq ´ Q˚ 
h 
` 
skh, π k hpskhq 
˘ 
is the suboptimality gap suffered in 
stage h of episode k. 
The following Lemma is a refined version of Lemma 6.1 in He et al. (2021a) that removes 
the dependence between regret and number of episodes K. 
Lemma 5.9.14. For each MDP MpS,A, H, trhu, tPhuq and any δ ą 0, with probability at 
least 1 ´ δ, we have 
RegretpKq ă Õ ˆ K ÿ 
k“1 
H ÿ 
h“1 
∆k h ` H2 logp1{δq 
˙ 
. 
We are now ready to prove Theorem 5.5.1: 
Proof of Theorem 5.5.1. By plugging in Lemma 5.9.12 and Lemma 5.9.13 into Lemma 5.9.14, 
we can reach the desired statement. 
200
5.9.2 Proof of Lemmas in Section 5.9.1 
In this section, we prove lemmas outlined in Section 5.9.1. Any proofs not included in this 
section are deferred to Section 5.9.3. 
5.9.2.1 Proof of Lemma 5.9.2 
Proof of Lemma 5.9.2. According to the criteria for Line 11, we have qV k h,lpsq ď V̂ k 
h,lpsq for 
any l P rlkhpsq ´ 1s. From the definition of qV k h,lpsq and V̂ k 
h,lpsq, they are monotonic in l that 
V̂ k h,l´1psq ď V̂ k 
h,lpsq and V̂ k h,lpsq ď V̂ k 
h,l´1psq hold. Combining with V̂ k h`1psq “ V̂ k 
h,lkhpsq´1 , we have 
@l P rlkhpsq ´ 1s, qV k h,lpsq ď V̂ k 
h psq ď V̂ k h,lpsq (5.9.3) 
From the definition of V̂ k h,lpsq and qV k 
h,lpsq, we have 
0 ď V̂ k h,lpsq ´ qV k 
h,lpsq ď ` 
V̂ k h,lpsq ´ V k 
h,lpsq ˘ 
` ` 
V k h,lpsq ´ qV k 
h,lpsq ˘ 
ď 6 ¨ 2´l. (5.9.4) 
Plugging (5.9.3) into (5.9.4), we conclude that for any phase l P rlkhpsq ´ 1s, it holds that 
|V̂ k h psq ´ V̂ k 
h,lpsq| ď 6 ¨ 2´l . 
Now consider the extended state value function V̂ k h,l` 
with an arbitrary l` P N`. For every 
s where l` ď lkhpsq ´ 1, we have |V̂ k h psq ´V k 
h,l` psq| ď 6 ¨ 2´l` as reasoned above. For the other 
s P S where l` ě lkhpsq, we have V̂ k h,lpsq “ V̂ k 
h psq following the procedure of Algorithm 13. 
This suggest that |V̂ k h psq ´ V̂ k 
h,l` psq| ď 6 ¨ 2´l` always holds. 
5.9.2.2 Proof of Lemma 5.9.4 
The following Lemma shows the rounding only cast bounded effects on the recovered param-
eters. 
Lemma 5.9.15. For any pk, h, sq P rKs ˆ rHs ˆ S, l P rlkhpsq ´ fk h psqs, a P Ak 
h,lpsq, it holds 
that 
ˇ 
ˇ 
@ 
ϕps, aq,wk h,l 
D 
´ @ 
ϕps, aq, w̃k h,l 
D ˇ 
ˇ ď 0.01 ¨ 2´4l, ˇ 
ˇ}ϕps, aq}pUk h,lq 
´1 ´ }ϕps, aq}Ũk,´1 h,l 
ˇ 
ˇ ď 0.1 ¨ 2´2l. 
201
The following lemma shows the number of episodes that are taken into regression |Ck h,l| 
is bounded independently from the number of episodes k. 
Lemma 5.9.16. For any tuple pk, h, lq P rKs ˆ rHs ˆ N`, we have |Ck h,l| ď 16l ¨ 4lγ2 
l d. 
The following lemma shows the number of possible state value functions |Vk h,l| is bounded 
independently from the number of episodes k. 
Lemma 5.9.17. For any tuple pk, h, lq P rKs ˆ rHs ˆ N`, we have |Vk h,l| ď p222d6H4ql 
2d2 . 
Now we are ready to prove Lemma 5.9.4. 
Proof of Lemma 5.9.4. Recall in Definition 5.9.3, the good event defined by the union of 
each single bad event: 
G1 “ 
K č 
k“1 
H č 
h“1 
č 
lě1 
č 
V PVk h,l` 
BA 1pk, h, l, V q, 
where each single bad event is given by 
B1pk, h, l, V q “ 
# › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV spsτh, a τ hq ´ V psτh`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ą γl 
+ 
, 
in which rPhV sps, aq “ Es1„Php¨|s,aqV psq. 
Consider some fixed ph, lq P rHs ˆ N`, V P VK h,l` 
. Arrange elements of Ck h,l in ascend-
ing order as tτiui. Since the environment sample sτih`1 according to Php¨|sτih , a τi h q, we have 
rPhV spsτih , a τi h q ´ V psτih`1q is F τi 
h -measurable with E “ 
rPhV spsτih , a τi h q ´ V psτih`1q 
ˇ 
ˇF τi h 
‰ 
“ 0. Since 
202
0 ď V psτih`1q ď H, we have |rPhV spsτih , a τi h q ´ V psτih`1q| ď H. This further leads to 
› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV spsτh, a τ hq ´ V psτh`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
“ 
› 
› 
› 
› 
› 
|Ck´1 h,l | ÿ 
i“1 
ϕτi h 
` 
rPhV spsτih , a τi h q ´ V psτih`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď H b 
2d ln ` 
1 ` |Ck h,l|{pdλq 
˘ 
` 2 lnpl2H|VK h,l` 
|{δq 
ď H 
b 
2d lnp1 ` l ¨ 4lγ2 l q ` 2 lnpl2Hp222d6H4ql 
2 `d2{δq 
ď γl,l` , 
where the first inequality holds following from the good event of probability 1´δ{pl2H|VK h,l` 
|q 
defined in Lemma 4.9.9 over filtration tF τi h ui, the second inequality is derived from combining 
Lemma 5.9.16 and Lemma 5.9.17, and the last inequality is given by Lemma 5.9.39. Accord-
ing to Lemma 4.9.9, we have the bad event ŤK 
k“1 B1pk, h, l, V q happens with probability at 
most δ{pl2H|VK h,l` 
|q. Taking union bound over all ph, lq P rHs ˆ N`, V P VK h,l` 
, we have the 
bad event happens with probability at most 
PrrGA 1s ď 
H ÿ 
h“1 
8 ÿ 
l“1 
ÿ 
V PVK h,l` 
Pr ” 
K ď 
k“1 
B1pk, h, l, V q 
ı 
ď 
H ÿ 
h“1 
8 ÿ 
l“1 
ÿ 
V PVK h,l` 
δ 
l2H|VK h,l` 
| ď 2δ, 
where the last inequality holds due to ř 
ně1 n ´2 “ π2{6. This completes our proof. 
5.9.2.3 Proof of Lemma 5.9.5 
Proof of Lemma 5.9.5. Denote the martingale difference between V̂ k h,l` 
´ V̂ k h as: 
µk h,l “ rPhpV̂ k 
h,l` ´ V̂ k 
h`1qspskh, π k hpskhqq ´ 
` 
V̂ k h,l` 
pskh`1q ´ V̂ k h`1ps 
k h`1q 
˘ 
. 
203
By triangle inequality: › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV̂ k h`1sps 
τ h, a 
τ hq ´ V̂ k 
h`1ps τ h`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 
› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV k h,l` 
spsτh, a τ hq ´ V̂ k 
h,l` psτh`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
` 
› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hµ 
τ h,l` 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
. (5.9.5) 
According to the definition of event G1, we can upper bound the first term by › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV k h,l` 
spsτh, a τ hq ´ V̂ k 
h,l` psτh`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď γl,l` “ γl. (5.9.6) 
According to Lemma 5.9.2, we have |V̂ k h,l` 
psq ´ V̂ k h`1psq| ď 6 ¨ 2´l` for any s P S. Thus, the 
difference can be bounded by |µτ h,l` 
| ď 6 ¨2´l` . Consequently, we can bound the second term 
by › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hµ 
τ h,l` 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 6 ¨ 2´l` 
b 
|Ck h,l| 
ď 6 ¨ 2´l` 
b 
16l ¨ 4lγ2 l d 
“ 24 ¨ 2l´l`γl ? ld, (5.9.7) 
where the first inequality is provided by Lemma 4.9.10, utilizing the condition |µτ h,l` 
| ď 
6 ¨ 2´l` , the second inequality is from Lemma 5.9.16. By plugging in the definition of l`, we 
can further bound the final term of (5.9.7) by › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hµ 
τ h,l` 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 24 ¨ 2l´l`γl ? ld ď 24 ¨ 2´20γl ď 0.1γl. (5.9.8) 
Plugging (5.9.6) and (5.9.8) into (5.9.5) yields the desired statement such that › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ h 
` 
rPhV̂ k h`1sps 
τ h, a 
τ hq ´ V̂ k 
h`1ps τ h`1q 
˘ 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 1.1γl, 
which concludes our proof. 
204
5.9.2.4 Proof of Lemma 5.9.6 
The following lemma shows the state-action value function Qk h,lps, aq is always well estimated. 
Lemma 5.9.18. Under event G1, for any pk, h, l, s, aq P rKs ˆ rHs ˆ N` ˆ S ˆ A, 
ˇ 
ˇQk h,lps, aq ´ rBhV̂ 
k h`1sps, aq 
ˇ 
ˇ ď ` 
1.2 ` 8 ? ldH ¨ 2lζ 
˘ 
γl}ϕps, aq}pUk h,lq 
´1 ` 0.01 ¨ 2´4l ` 2Hζ. 
Equipped with Lemma 5.9.15 and Lemma 5.9.18, we are ready to prove Lemma 5.9.6. 
Proof of Lemma 5.9.6. In case that l ď lkhpsq ´ fk h psq, for any a P Ak 
h,lpsq, we have that 
}ϕps, aq}pUk h,lq 
´1 ď }ϕps, aq}Ũk,´1 h,l 
` ˇ 
ˇ}ϕps, aq}pUk h,lq 
´1 ´ }ϕps, aq}Ũk,´1 h,l 
ˇ 
ˇ 
ď 2´lγ´1 l ` 0.1 ¨ 2´2l 
ď 1.1 ¨ 2´lγ´1 l , (5.9.9) 
where the first inequality holds due to triangle inequality, and in the second inequality, the 
first term is satisfied since state s passes the criterion in Line 9 in phase l and the second 
term follows from Lemma 5.9.15, and the last inequality is given by Lemma 5.9.38 which 
implies 2l ą γl. Plugging (5.9.9) into Lemma 5.9.18 gives 
ˇ 
ˇQk h,lps, aq ´ rBhV̂ 
k h`1sps, aq 
ˇ 
ˇ ď 0.01 ¨ 2´4l ` 1.32 ¨ 2´l 
` 8.8 ? ldHζ ` 2Hζ 
ď 2 ¨ 2´l ` 12 
? ldHζ, 
which proves the desired statement. 
5.9.2.5 Proof of Lemma 5.9.7 
Equipped with Lemma 5.9.6, we are able to show several properties of the state value function 
V k h,l through the arm-elimination process. The first lemma suggests that for any action 
al P Ak h,lpsq, there is at least one action al`1 P Ak 
h,l`1psq close to al in terms of the Bellman 
operator rBhV̂ k h`1sps, aq after the elimination. 
205
Lemma 5.9.19. Under event G1, for any pk, h, sq P rKs ˆ rHs ˆ S, l P rmintL0, l k hpsq ´ 
fk h psqus, al P Ak 
h,lpsq, there exists al`1 P Ak h,l`1psq that 
rBhV̂ k h`1sps, alq ´ rBhV̂ 
k h`1sps, al`1q ď 2χ 
a 
L0ζ 
where χ “ 12 ? dH for arbitrary L0 ě 1. 
Then the following lemma shows that by induction on stage h P rHs, we can show the 
elimination process keep at least one near-optimal action al`1 P Ak h,l`1psq. 
Lemma 5.9.20. Under event G1, for any pk, h, sq P rKsˆrHsˆS, l P rmintL0, l k hpsq´fk 
h psqus, 
there exists al`1 P Ak h,l`1psq that, 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, al`1q ď 2l ¨ χ 
a 
L0ζ. 
where χ “ 12 ? dH for arbitrary L0 ě 1. 
The following two lemmas indicate that the state value function V k h,lpsq on stage h is a good 
estimation for the value function given by Bellman operator V psq “ maxaPArBhV̂ k h`1sps, aq. 
Lemma 5.9.21. Under event G1, for any pk, h, sq P rKsˆrHsˆS, l P rmintL0, l k hpsq´fk 
h psqus, 
max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,lpsq ď 2 ¨ 2´l ` p2l ´ 1qχ 
a 
L0ζ. 
where χ “ 12 ? dH for arbitrary L0 ě 1. 
Lemma 5.9.22. Under event G1, for any pk, h, sq P rKsˆrHsˆS, l P rmintL0, l k hpsq´fk 
h psqus, 
V k h,lpsq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď 2 ¨ 2´l 
` χ a 
L0ζ, 
where χ “ 12 ? dH for arbitrary L0 ě 1. 
Now we are ready to show any actions remaining in the elimination process are near-
optimal. 
206
Proof of Lemma 5.9.7. First, according to Lemma 5.9.21, we can write 
max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,lpsq ď 2 ¨ 2´l ` p2l ´ 1qχ 
a 
L0ζ. (5.9.10) 
Any action al`1 P Ak h,l`1psq passes the elimination process will satisfy: 
Qk h,lps, al`1q ě V k 
h,lpsq ´ 4 ¨ 2´l. (5.9.11) 
According to Lemma 5.9.6 with the condition that l ď L0, we have that the empirical 
state-action value function Qk h,lps, ¨q is a good estimation for rBhV̂ 
k h`1sps, ¨q among every 
al`1 P Ak l psq under event G1: 
ˇ 
ˇrBhV̂ k h`1sps, al`1q ´ Qk 
h,lps, al`1q ˇ 
ˇ ď 2 ¨ 2´l ` χ 
a 
L0ζ. (5.9.12) 
Combining (5.9.10), (5.9.11), and (5.9.12) gives 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, al`1q 
“ ` 
max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,lpsq ˘ 
` ` 
V k h,lpsq ´ Qk 
h,lps, al`1q ˘ 
` ` 
Qk h,lps, al`1q ´ rBhV̂ 
k h`1sps, al`1q 
˘ 
ď ` 
2 ¨ 2´l ` p2l ´ 1qχ 
a 
L0ζ ˘ 
` 4 ¨ 2´l ` ` 
2 ¨ 2´l ` χ 
a 
L0ζ ˘ 
“ 8 ¨ 2´l ` 2l ¨ χ 
a 
L0ζ, 
which proves the desired statement. 
5.9.2.6 Proof of Lemma 5.9.8 
The following two lemmas demonstrate that, at stage h, both the optimistic state value 
function, V̂ k h,lpsq, and the pessimistic state value function, qV k 
h,lpsq, exhibit a gap relative to the 
state value function determined by the Bellman operator as V psq “ maxaPArBhV̂ k h`1sps, aq. 
Lemma 5.9.23. Under event G1, for any pk, h, sq P rKsˆrHsˆS, l P rmintL0, l k hpsq´fk 
h psqus, 
min ␣ 
V k h,lpsq ` 3 ¨ 2´l, V̂ k 
h,l´1psq ( 
´ max aPA 
rBhV̂ k h`1sps, aq ě 2´l 
´ p2l ´ 1qχ a 
L0ζ, 
207
where χ “ 12 ? dH for arbitrary L0 ě 1. In case that l ď lkhpsq´1, the inequality is equivalent 
to 
V̂ k h,lpsq ´ max 
aPA rBhV̂ 
k h`1sps, aq ě 2´l 
´ p2l ´ 1qχ a 
L0ζ. 
Lemma 5.9.24. Under event G1, for any pk, h, sq P rKsˆrHsˆS, l P rmintL0, l k hpsq´fk 
h psqus, 
max aPA 
rBhV̂ k h`1sps, aq ´ max 
␣ 
V k h,lpsq ´ 3 ¨ 2´l, qV k 
h,l´1psq ( 
ě 2´l ´ χ 
a 
L0ζ, 
where χ “ 12 ? dH for arbitrary L0 ě 1. In case that l ď lkhpsq´1, the inequality is equivalent 
to 
max aPA 
rBhV̂ k h`1sps, aq ´ qV k 
h,lpsq ě 2´l ´ χ 
a 
L0ζ. 
Proof of Lemma 5.9.8. Set L0 “ Lζ be the maximal integer satisfying 2´Lζ ´ χL1.5 ζ ζ ě 0. 
Combining Lemma 5.9.24 and Lemma 5.9.23, for any l P rmintL0, l k hpsq ´ fk 
h psqus, we have 
that 
min ␣ 
V k h,lpsq ` 3 ¨ 2´l, V̂ k 
h,l´1psq ( 
´ max ␣ 
V k h,lpsq ´ 3 ¨ 2´l, qV k 
h,l´1psq ( 
“ ` 
V̂ k h,lpsq ´ max 
aPA rBhV̂ 
k h`1sps, aq 
˘ 
` ` 
max aPA 
rBhV̂ k h`1sps, aq ´ qV k 
h,lpsq ˘ 
ě ` 
2´l ´ p2l ´ 1qχ 
a 
L0ζ ˘ 
` ` 
2´l ´ χ 
a 
L0ζ ˘ 
“ 2 ¨ 2´l ´ 2l ¨ χ 
a 
L0ζ 
ě 2 ¨ 2´L0 ´ 2χL1.5 0 ζ ě 0. 
where the second inequality holds since 2´l decreases as l increases and the last inequality 
holds according to the selection of L0. 
When fk h psq “ 0, consider l “ lkhpsq. The above reasoning indicates the criterion in 
Line 11 can never satisfied. Thus fk h psq “ 0 can only happen if lkhpsq ą L0 “ Lζ . 
5.9.2.7 Proof of Lemma 5.9.9 
By partitioning rKs based on whether Algorithm 13 stops before phase Lε, we can prove 
Lemma 5.9.9. Specifically, Lemma 5.9.16 bounds the number of episodes in which Algo-
208
rithm 13 stops before phase Lε. This allows us to establish an upper bound for the desired 
summation over these episodes. Furthermore, for episodes that stop after phase Lε, the 
contribution of 2´lkhpskhqγlkhpskhq is small according to the definition of Lε. 
Proof of Lemma 5.9.9. Denote CK h,` “ rKs ´ 
ŤLε´1 l“1 CK 
h,l. In this sense, we have 
ÿ 
kPK 2´lkhpskhq 
“ ÿ 
kPKXCK h,` 
2´lkhpskhq ` 
Lε´1 ÿ 
l“1 
ÿ 
kPKXCK h,l 
2´lkhpskhq. (5.9.13) 
From the construction of CK h,l, we have lkhpskhq “ l for any k P CK 
h,l. Fix some k P CK h,`. If 
fk h pskhq “ 0, we have lkhpskhq ě Lζ ě Lε where the first inequality is given by Lemma 5.9.8 
and the second inequality is given by the assignment of Lε. Otherwise, we have lkhpskhq ě Lε 
according to the definition of CK h,l. This indicates lkhpskhq ě Lε holds for any k P CK 
h,`. This 
allow is to bound the first term by ÿ 
kPKXCK h,` 
2´lkhpskhq ď 
ÿ 
kPKXCK h,` 
2´Lε ď 0.01|K| ¨ ε{H, (5.9.14) 
where the first inequality holds since lkhpskhq ą Lε and the second inequality holds from both 
2´Lε ď 0.01ε{H and |K X CK h,`| ď |K|. 
Furthermore, we can bound the second term by Lε´1 ÿ 
l“1 
ÿ 
kPKXCK h,l 
2´lkhpskhq ď 
Lε´1 ÿ 
l“1 
|K X CK h,l| ¨ 2´l 
ď 
Lε´1 ÿ 
l“1 
16l ¨ 4lγ2 l d ¨ 2´l 
ď 16Lεd ¨ 2Lεγ2 Lε 
ď 212LεdHγ2 Lε ε´1. (5.9.15) 
where the second inequality is given by Lemma 5.9.16, and the last inequality holds due to 
0.005ε{H ď 2´Lε which is because Lε is a minimal integer such that 2´Lε ď 0.01ε{H. 
Finally, plugging (5.9.14) and (5.9.15) into (5.9.13) gives ÿ 
kPK 2´lkhpskhq 
ď 0.01|K| ¨ ε{H ` 212LεdHγ2 Lε ε´1. 
209
5.9.2.8 Proof of Lemma 5.9.12 
The following lemma provides an upper bound for the underestimation error of the empirical 
state value function V̂ k h with respect to the optimal state value function V ˚ 
h . 
Lemma 5.9.25. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, h, sq P 
rKs ˆ rHs ˆ S, 
V ˚ h psq ´ V̂ k 
h psq ď 0.07ε. 
As V̂ k h represents an empirical state value function with potentially optimal policy πk 
hpsq, 
the following lemma provides an upper bound for the overestimation error of V̂ k h with respect 
to deploying the policy πk hpsq on the ground-truth transition kernel. 
Lemma 5.9.26. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, h, sq P 
rKs ˆ rHs ˆ S, 
V̂ k h psq ´ rBhV̂ 
k h`1sps, π 
k hpsqq ď 20 ¨ 2´lkhpsq 
` 0.16ε{H. 
To start with, we define a good event according to: 
Definition 5.9.27. For some ε ą 0, let Kε h “ tk P rKs : V ˚ 
h pskhq ´ V πk 
h pskhq ě εu. We define 
the bad event as 
B2ph, εq “ 
# 
ÿ 
kPKε h 
H ÿ 
h1“h 
ηkh1 ą 4 b 
H3|Kε h| logp4H|Kε 
h| logpε´1q{δq 
+ 
. 
where ηkh “ rPhpV̂ k h`1 ´ V πk 
h`1qspskh, π k hpskhqq ´ 
` 
V̂ k h`1pskh`1q ´ V πk 
h`1ps k h`1q 
˘ 
. The good event is 
defined as G2 “ ŞH 
h“1 
Ş 
lě1 BA 2ph, 2´lq. 
The following lemma provides the concentration property such that the cumulative sam-
ple error is small with high probability. 
Lemma 5.9.28. Event G2 happens with probability at least 1 ´ δ. 
210
Using the above results, we can bound the instantaneous regret of any subsets once the 
misspecification level is appropriately controlled, 
Lemma 5.9.29. Under event G1,G2 and for all ε ą 0 that Gε is satisfied, for any K Ď rKs 
and h P rHs, it satisfies that ÿ 
kPK 
` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ď 0.49|K|ε ` 217LεdH 2γ2 
Lε ε´1 
` 4 a 
H3|K| logp4H|K| logpε´1q{δq. 
With all lemmas stated above, we can show Cert-LSVI-UCB achieves constant step-
wise decision error. The following lemma gives a sufficient condition that Gε defined in 
Definition 5.9.10 is satisfied. 
Now, we are ready to prove Lemma 5.9.12. 
Proof of Lemma 5.9.12. We focus on the case where the good event G1 X G2 X Gε occurs. 
By the union bound statement over Lemma 5.9.4 and Lemma 5.9.28, and Lemma 5.9.11, 
this good event happens with a probability of at least 1 ´ 3δ and with the condition that 
ε ě Ωpζ ? dH2 log2pdHζ´1qq. W.l.o.g, consider Kε 
h for some h P rHs and ε “ 2´l where l ą 0 
is an integer. On the one hand, we have ÿ 
kPKε h 
` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ě |Kε h|ε. (5.9.16) 
On the other hand, Lemma 5.9.29 gives ÿ 
kPKε h 
` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ď 0.49|Kε h|ε ` 217LεdH 
2γ2 Lε ε´1 
` 4 b 
H3|Kε h| logp4H|Kε 
h| logpε´1q{δq. (5.9.17) 
Combining (5.9.16) and (5.9.17) gives 
0.51|Kε h|ε ď 217LεdH 
2γ2 Lε ε´1 
` 4 b 
H3|Kε h| logp4H|Kε 
h| logpε´1q{δq. 
Plugging the value of γLε , we have 
0.51|Kε h|ε ď 222LεpLε ` logp220dHqq 
2d3H4ε´1 logp16Lεd{δq 
` 4 b 
H3|Kε h| logp4H|Kε 
h| logpε´1q{δq. (5.9.18) 
211
According to Lemma 5.9.40, (5.9.18) implies 
|Kε h| ď OpLεpLε ` logpdHqq 
2d3H4ε´2 logpLεdq logpδ´1 qιq, 
where ι refers to a polynomial of log logpdHε´1δ´1q. With the definition of Lε, we conclude 
that 
|Kε h| ď Opd3H4ε´2 log4pdHε´1 
q logpδ´1 qιq. 
5.9.2.9 Proof of Lemma 5.9.13 
Proof of Lemma 5.9.13. From the definition of suboptimality gap, we have 
∆k h “ V ˚ 
h pskhq ´ rBhV ˚ h`1sps 
k h, π 
k hpskhqq ď V ˚ 
h pskhq ´ rBhV πk 
h`1spskh, π k hpskhqq “ V ˚ 
h pskhq ´ V πk 
h pskhq. 
(5.9.19) 
According to the assumption, K ÿ 
k“1 
1 ” 
V ˚ h psk1q ´ V πk 
h pskhq ě ε ı 
ď 
´C1 
ε ` 
C2 
ε2 
¯ 
loga ´C1 
ε ` 
C2 
ε2 
¯ 
holds for every ε ą ε0 with probability at least 1 ´ δ, replacing the V ˚ h psk1q ´ V πk 
h pskhq with 
its lower bound ∆k h yields for every ε ą ε0, 
K ÿ 
k“1 
1 ” 
∆k h ě ε 
ı 
ď 
´C1 
ε ` 
C2 
ε2 
¯ 
loga ´C1 
ε ` 
C2 
ε2 
¯ 
. 
In addition, according to the definition of minimal suboptimality gap ∆ in Definition 5.3.3, 
we have ∆k h is either 0 or no less than ∆. Since for any x P t0u Y r∆, Hs, it holds that 
x ď ∆ ¨ 1rx ě ∆s ` şH 
∆ 1rx ě εs dε, we decompose the total suboptimality incurred in stage 
h by K ÿ 
k“1 
∆k h ď 
K ÿ 
k“1 
˜ 
∆ ¨ 1 ” 
∆k h ě ∆ 
ı 
` 
ż H 
∆ 
1 ” 
∆k h ě ε 
ı 
dε 
¸ 
“ ∆ K ÿ 
k“1 
1 ” 
∆k h ě ∆ 
ı 
` 
ż H 
∆ 
K ÿ 
k“1 
1 ” 
∆k h ě ε 
ı 
dε. (5.9.20) 
212
In case that ε0 ď ∆, the first term in (5.9.20) can be bounded by 
∆ K ÿ 
k“1 
1 ” 
∆k h ě ∆ 
ı 
ď ∆ ´C1 
∆ ` 
C2 
∆2 
¯ 
loga ´C1 
∆ ` 
C2 
∆2 
¯ 
. (5.9.21) 
We can further bound the second term by 
ż H 
∆ 
K ÿ 
k“1 
1 ” 
V ˚ 1 psk1q ´ V πk 
1 psk1q ě ε ı 
dε ď 
ż H 
∆ 
´C1 
ε ` 
C2 
ε2 
¯ 
loga ´C1 
ε ` 
C2 
ε2 
¯ 
dε 
ď loga ´C1 
∆ ` 
C2 
∆2 
¯ 
¨ 
´ 
C1 ln H 
∆ ` 
C2 
∆ 
¯ 
ď pC1 logH ` C2{∆q ¨ polylogpC1, C2,∆ ´1 
q. (5.9.22) 
Plugging (5.9.21) and (5.9.22) into (5.9.20) with summation over h P rHs, we conclude that 
the total suboptimality incurred in stage h is bounded by 
K ÿ 
k“1 
H ÿ 
h“1 
∆k h ď H ¨ pC1 ` C2{∆ ` C1 logH ` C2{∆q ¨ polylogpC1, C2,∆ 
´1 q 
ď ÕpC2H{∆ ` C1Hq. 
5.9.2.10 Proof of Lemma 5.9.14 
We first introduce the Freedman inequality: 
Lemma 5.9.30 (Freedman inequality, Cesa-Bianchi and Lugosi (2006)). Let tηkuKk“1 be a 
martingale difference sequence with respect to a filtration tFkuKk“1 satisfying |ηk| ď M for 
some constant M ą 0 and ηk is Fk`1-measurable with |Erηk|Fks| “ 0. Then for some fixed 
k P rKs, a ą 0 and v ą 0, we have 
Pr ´ 
k ÿ 
τ“1 
ητ ě a, k ÿ 
τ“1 
Varrητ |F τ s ď v 
¯ 
ď exp ´ 
´a2 
2v ` 2aM{3 
¯ 
. 
We are now ready to present the proof of Lemma 5.9.14. 
213
Proof of Lemma 5.9.14. For a given policy π and any state sh P S, we have 
V ˚ h pshq ´ V π 
h pshq 
“ ` 
V ˚ h pshq ´ rBhV 
˚ h`1spsh, πhpshqq 
˘ 
` ` 
rBhV ˚ h`1spsh, πhpshqq ´ rBhV 
π h`1spsh, πhpshqq 
˘ 
“ ∆hpsh, πhpshqq ` rPhpV ˚ h`1 ´ V π 
h`1qspsh, πhpshqq, 
where the second equality is given by the definition of suboptimality gap ∆hp¨, ¨q in Def-
inition 5.3.3. Taking expectation on both sides with respect to the randomness of state-
transition and taking telescoping sum over all h P rHs gives 
V ˚ 1 ps1q ´ V π 
h ps1q “ E „ H ÿ 
h“1 
∆hpsh, πhpshqq 
ȷ 
, 
where sh`1 „ Php¨|sh, πhpshqq. Let the filtration list be Fk “ 
! 
␣ 
sji , a j i 
(H,k´1 
i“1,j“1 
) 
, we have 
E ” 
H ÿ 
h“1 
∆k h 
ˇ 
ˇ 
ˇ Fk 
ı 
“ V ˚ 1 psk1q ´ V πk 
h psk1q. 
Denote random variable ηk “ ` 
V ˚ 1 psk1q ´ V πk 
h psk1q ˘ 
´ řH 
h“1∆ k h. We can see ηk is Fk`1-
measurable with |Erηk|Fks| “ 0. Furthermore, for the variance of ηk, we have 
Varrηk|Fk s ď E 
”´ 
H ÿ 
h“1 
∆k h 
¯2ˇ ˇ 
ˇ Fk 
ı 
ď H2E ” 
H ÿ 
h“1 
∆k h 
ˇ 
ˇ 
ˇ Fk 
ı 
“ H2 ` 
V ˚ 1 psk1q ´ V πk 
h psk1q ˘ 
, 
where the first inequality holds due to VarrXs ď ErpX ´ tq2s for any fixed t, the second 
inequality follows 0 ď ∆k h ď H. As a result, the total variance of the random variables tηku 
can be bounded by 
K ÿ 
k“1 
Varrηk|Fk s ď 
K ÿ 
k“1 
H2 ` 
V ˚ 1 psk1q ´ V πk 
h psk1q ˘ 
“ H2RegretpKq. 
214
Let F pxq “ a 
2xH2 logpx{δq ` H2 logpx{δq, using peeling technique, we can write 
Pr ”´ 
K ÿ 
k“1 
ηk ¯ 
ě F pRegretpKqq, 1 ă RegretpKq 
ı 
“ Pr ”´ 
K ÿ 
k“1 
ηk ¯ 
ě F pRegretpKqq, 1 ă RegretpKq, K ÿ 
k“1 
Varrηk|Fk s ď H2RegretpKq 
ı 
ď 
8 ÿ 
i“1 
Pr ”´ 
K ÿ 
k“1 
ηk ¯ 
ě F pRegretpKqq, 2i´1 ă RegretpKq ď 2i, 
K ÿ 
k“1 
Varrηk|Fk s ď H2RegretpKq 
ı 
ď 
8 ÿ 
i“1 
Pr ”´ 
K ÿ 
k“1 
ηk ¯ 
ě F p2iq, K ÿ 
k“1 
Varrηk|Fk s ď 2iH2 
ı 
ď 
8 ÿ 
i“1 
exp ´ 
´F p2iq2 
2i`1H2 ` 2F p2iqH2{3 
¯ 
, (5.9.23) 
where the last inequality follows Lemma 5.9.30. Plugging F pxq “ a 
2xH2 logpx{δq ` 
H2 logpx{δq back into (5.9.23) yields 
Pr ”´ 
K ÿ 
k“1 
ηk ¯ 
ě a 
2RegretpKqH2 logpRegretpKq{δq ` H2 logpRegretpKq{δq, 1 ă RegretpKq 
ı 
ď 
8 ÿ 
i“1 
expp´ logp2i{δqq “ 
8 ÿ 
i“1 
δ{2i “ δ. 
Therefore, whenever RegretpKq ą 1, with probability at least 1 ´ δ, we have K ÿ 
k“1 
ηk ă a 
2RegretpKqH2 logpRegretpKq{δq ` H2 logpRegretpKq{δq. 
Combining with the fact that RegretpKq “ řK 
k“1 η k ` 
řK k“1 
řH h“1∆ 
k h, we have 
RegretpKq ă 
K ÿ 
k“1 
H ÿ 
h“1 
∆k h ` 
a 
2RegretpKqH2 logpRegretpKq{δq ` H2 logpRegretpKq{δq, 
whenever RegretpKq ą 1. Since x ď a ` ? bx implies x ď 2a ` 2b, absorbing the case 
RegretpKq ď 1 into the Õp¨q factor yields 
RegretpKq ă Õ ´ 
K ÿ 
k“1 
H ÿ 
h“1 
∆k h ` H2 logp1{δq 
¯ 
. 
215
5.9.3 Proof of Lemmas in Section 5.9.2 
In this section, we prove lemmas outlined in Section 5.9.2. Any proofs not included in this 
section are deferred to Section 5.9.4. 
5.9.3.1 Proof of Lemma 5.9.15 
We first introduce the claim from Vial et al. (2022) controlling the rounding error: 
Lemma 5.9.31 (Claim 1, Vial et al. 2022, restate). For any pk, h, l, s, aq P rKsˆrHsˆN` ˆ 
S ˆ A, we have 
ϕps, aq J 
pwk h,l ´ w̃k 
h,lq ď ? dκl, 
ˇ 
ˇ}ϕps, aqpUk h,lq 
´1 ´ }ϕps, aq}Ũk,´1 h,l 
ˇ 
ˇ ď a 
dκl, 
where κl is used to quantify the vector wk h,l and inverse matrix pUl 
h,lq ´1. 
Proof of Lemma 5.9.15. From Lemma 5.9.31 we have 
ˇ 
ˇ 
@ 
ϕps, aq,wk h,l 
D 
´ @ 
ϕps, aq, w̃k h,l 
D ˇ 
ˇ ď ? dκl ď 0.01 ¨ 2´4l 
where the first inequality is due to Lemma 5.9.31, and the second inequality is valid due to 
κl “ 0.01 ¨ 2´4l. Similarly, we have 
ˇ 
ˇ}ϕps, aq}pUk h,lq 
´1 ´ }ϕps, aq}Ũk,´1 h,l 
ˇ 
ˇ ď a 
dκl ď 0.1 ¨ 2´2l. 
5.9.3.2 Proof of Lemma 5.9.16 
Proof of Lemma 5.9.16. First, both lτhpsτhq “ l and f τ h psτhq “ 1 held for any τ P Ck 
h,l. This 
implies that the criteria for either Line 7 or Line 9 holds as l “ lτhpsτhq. For τ that satisfies 
the first criterion, we have lτhpsτhq ą Lτ . Note that Lτ “ maxtrlog4pτ{dqs, 0u, so this only 
happens for τ ă 4ld. For other τ that satisfies the second criterion, we have that 
}ϕτ h}pUτ 
h,lq ´1 ě }ϕτ 
h}Ũτ,´1 h,l 
´ ˇ 
ˇ}ϕτ h}Ũτ,´1 
h,l ´ }ϕτ 
h}pUτ h,lq 
´1 
ˇ 
ˇ ě 2´lγ´1 l ´ 0.1 ¨ 2´lγ´1 
l “ 0.9 ¨ 2´lγ´1 l , 
216
where the first inequality holds due to the triangle inequality. In the second inequality, the 
first term }ϕτ h}Ũτ,´1 
h,l is bounded by criterion in Line 9 while the second term 
ˇ 
ˇ}ϕτ h}Ũτ,´1 
h,l ´ 
}ϕτ h}pUτ 
h,lq ´1 
ˇ 
ˇ follows from Lemma 5.9.15. 
Arrange elements of Ck h,l in ascending order as tτiui. According to the above reasoning, 
the number of elements τ P Ck h,l that }ϕτ 
h}pUτ h,lq 
´1 ě 0.9 ¨ 2´lγ´1 l is at least |Ck 
h,l| ´ 4ld. This 
gives 
|Ck h,l| ÿ 
i“1 
mint1, }ϕτ h} 
2 pUτ 
h,lq ´1u ě p0.9 ¨ 2´lγ´1 
l q 2 
¨ p|Ck h,l| ´ 4ldq. (5.9.24) 
On the other hand, Lemma 2.8.15 upper bounds the LHS of (5.9.24) by 
|Ck h,l| ÿ 
i“1 
mint1, }ϕτ h} 
2 pUτ 
h,lq ´1u ď 2d ln 
` 
1 ` |Ck h,l|{pdλq 
˘ 
. (5.9.25) 
Combining (5.9.24) and (5.9.25) gives 
0.81 ¨ 4´lγ´2 l p|Ck 
h,l| ´ 4ldq ď 2d ln ` 
1 ` |Ck h,l|{p16dq 
˘ 
. (5.9.26) 
From algebra analysis in Lemma 5.9.37, a necessary condition for (5.9.26) is |Ck h,l| ď 16l ¨ 
4lγ2 l d. 
5.9.3.3 Proof of Lemma 5.9.17 
We first present a claim from Vial et al. (2022) controlling the infinite norm of coefficient w. 
Lemma 5.9.32 (Claim 10, Vial et al. 2022). For any pk, h, lq P rKs ˆ rHs ˆ N`, we have 
}wk h,l}8 ď }wk 
h,l}2 ď p2ldHq4. 
Proof of Lemma 5.9.17. Denote Xℓ as the set of all w̃k h,ℓ and Yℓ as the set of all Ũk,´1 
h,ℓ . From 
the definition of Vk h,l, we have that |Vk 
h,l| ď śl 
ℓ“1 
` 
|Xℓ| ¨ |Yℓ| ˘ 
. From Lemma 5.9.32, we have 
}wk h,ℓ}8 ď p2ℓdHq4. Note that wk 
h,ℓ P Rd, we have the number of different w̃k h,ℓ controlled by 
|Xℓ| ď p1 ` 2 ¨ p2ℓdHq 4 {κℓq 
d ď p2 ¨ p2ℓdHq 
4 ¨ 26`4ℓdq 
d ď 2p7`8ℓqdd5dH4d. 
217
In addition, we have }pUk h,lq 
´1}8 ď 1{λ “ 1{16. So we can bound the number of Ũk,´1 h,ℓ by 
|Yℓ| ď p1 ` 2 ¨ 1{p16κℓqq d2 
ď p2 ¨ 22`4ℓdq d2 
ď 2p3`4ℓqd2dd 2 
. 
As a result, we can conclude that 
|Vk h,l| ď 
l ź 
ℓ“1 
` 
|Xℓ| ¨ |Yℓ| ˘ 
ď 
l ź 
ℓ“1 
` 
2p7`8ℓqdd5dH4d ¨ 2p3`4ℓqd2dd 
2˘ 
ď p222d5H4 q l2d2 . 
5.9.3.4 Proof of Lemma 5.9.18 
Proof of Lemma 5.9.18. According to Proposition 5.3.2, there exists a parameter wh such 
that for any ps, aq P S ˆ A, it holds that ˇ 
ˇxϕps, aq,why ´ rBhV̂ k h`1sps, aq 
ˇ 
ˇ ď 2Hζ . Denoting 
ητh “ xϕτ h,why ´ rBhV̂ 
k h`1sps 
τ h, a 
τ hq and ετh “ 
` 
V̂ k h`1ps 
τ h`1q ´ rPhV̂ 
k h`1spsτh, a 
τ hq ˘ 
, we have 
Uk h,lpw 
k h,l ´ whq “ 
ÿ 
τPCk´1 h,l 
ϕτ h 
´ 
rτh ` V̂ k h`1ps 
τ h`1q 
¯ 
´ 
´ 
λI ` ÿ 
τPCk´1 h,l 
ϕτ hpϕτ 
hq J ¯ 
wh 
“ ´λwh ` ÿ 
τPCk´1 h,l 
ϕτ h 
´ 
rτh ` V̂ k h`1psτh`1q ´ xϕτ 
h,why 
¯ 
“ ´λwh ` ÿ 
τPCk´1 h,l 
ϕτ h 
´ 
rτh ` V̂ k h`1psτh`1q ´ rBhV̂ 
k h`1sps 
τ h, a 
τ hq 
¯ 
` ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
“ ´λwh ` ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h ` 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h, (5.9.27) 
where the first equality holds due to the definition of Uk h,l,w 
k h,l, the second equality holds by 
rearranging the terms, the third equality holds according the definition of ητh, and the last 
equality holds from the relationship that rBhV̂ k h`1sps 
τ h, a 
τ hq “ rτh `rPhV̂ 
k h`1sps 
τ h, a 
τ hq. Therefore, 
218
for any vector ϕ P Rd, it holds that 
ˇ 
ˇ 
@ 
ϕ,wk h,l ´ wh 
D ˇ 
ˇ “ ˇ 
ˇϕJ ` 
Uk h,l 
˘´1 Uk 
h,lpw k h,l ´ whq 
ˇ 
ˇ 
“ 
ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ϕJ pUk 
h,l 
˘´1 ¨ 
˜ 
´ λwh ` ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h ` 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
¸ˇ 
ˇ 
ˇ 
ˇ 
ˇ 
ď }ϕ}pUk h,lq 
´1 
› 
› 
› 
› 
› 
´ λwh ` ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h ` 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
, (5.9.28) 
where the second equality follows (5.9.27) and the inequality holds from Cauchy–Schwarz 
inequality (i.e., |xJUy| ď }x}U}y}U). From the triangle inequality, we have › 
› 
› 
› 
› 
´ λwh ` ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h ` 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď λ}wh}pUk h,lq 
´1 ` 
› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
` 
› 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
. (5.9.29) 
There are three terms which we will bound respectively. For the first term, we have 
λ}wh}pUk h,lq 
´1 ď 2 ? dλH ď 0.1γl, (5.9.30) 
where the first inequality holds due to the fact that }wh}2 ď 2H ? d as of Proposition 5.3.2 
and the fact that Uk h,l ľ λI. Under the good event G1 and Lemma 5.9.5, the second term 
can be bounded by the following: › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hε 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 1.1γl. (5.9.31) 
And the last term can be bounded by: › 
› 
› 
› 
› 
ÿ 
τPCk´1 h,l 
ϕτ hη 
τ h 
› 
› 
› 
› 
› 
pUk h,lq 
´1 
ď 2Hζ b 
|Ck h,l| ď 2Hζ 
b 
16l ¨ 4lγ2 l d “ 8 
? ldH ¨ 2lγlζ, (5.9.32) 
where the first inequality is due to Lemma 4.9.10, and the second inequality follows from 
Lemma 5.9.16. Plugging (5.9.29), (5.9.30), (5.9.31), and (5.9.32) into (5.9.28) gives 
ˇ 
ˇ 
@ 
ϕ,wk h,l ´ wh 
D ˇ 
ˇ ď ` 
1.2γl ` 8 ? ldH ¨ 2lγlζ 
˘ 
}ϕ}pUk h,lq 
´1 . (5.9.33) 
219
So for any ps, aq P S ˆ A, we have 
ˇ 
ˇQk h,lps, aq ´ rBhV̂ 
k h`1sps, aq 
ˇ 
ˇ “ ˇ 
ˇ 
@ 
ϕps, aq, w̃k h,l 
D 
´ rBhV̂ k h`1sps, aq 
ˇ 
ˇ 
ď ˇ 
ˇ 
@ 
ϕps, aq, w̃k h,l ´ wk 
h,l 
D ˇ 
ˇ ` ˇ 
ˇ 
@ 
ϕps, aq,wk h,l ´ wh 
D ˇ 
ˇ ` ˇ 
ˇ 
@ 
ϕps, aq,wh 
D 
´ rBhV̂ k h`1sps, aq 
ˇ 
ˇ 
ď 0.01 ¨ 2´4l ` ` 
1.2 ` 8 ? ldH ¨ 2lζ 
˘ 
γl}ϕps, aq}pUk h,lq 
´1 ` 2Hζ. (5.9.34) 
where the first inequality holds from the triangle inequality, and there are three terms in 
the second inequality which we will bound them respectively: the first term is given by 
Lemma 5.9.15, the second term follows (5.9.33), and the third term holds from the definition 
of wh. 
5.9.3.5 Proof of Lemma 5.9.19 
Proof of Lemma 5.9.19. We prove by doing case analysis. In case that action al P Ak h,l`1psq, 
we can assign al`1 “ al P Ak h,l`1psq so that 
rBhV̂ k h`1sps, alq ´ rBhV̂ 
k h`1sps, al`1q “ 0. (5.9.35) 
On the other hand, in the case that al R Ak h,l`1psq, the action al is eliminated with Qk 
h,lps, alq ă 
V k h,lpsq ´ 4 ¨ 2´l. Note in this case, there exists al`1 “ πk 
h,lpsq P Ak h,l`1psq such that 
Qk h,lps, alq ` 4 ¨ 2´l 
ă V k h,lpsq “ Qk 
h,lps, al`1q. (5.9.36) 
According to Lemma 5.9.6 and the condition that l ď L0, we have that empirical state-value 
function Qk h,lps, ¨q is a good estimation for rBhV̂ 
k h`1sps, ¨q on actions al, al`1 P Ak 
l psq under 
event G1: 
ˇ 
ˇrBhV̂ k h`1sps, alq ´ Qk 
h,lps, alq ˇ 
ˇ ď 2 ¨ 2´l ` χ 
a 
L0ζ (5.9.37) ˇ 
ˇrBhV̂ k h`1sps, al`1q ´ Qk 
h,lps, al`1q ˇ 
ˇ ď 2 ¨ 2´l ` χ 
a 
L0ζ. (5.9.38) 
220
Moreover, 
rBhV̂ k h`1sps, alq ´ rBhV̂ 
k h`1sps, al`1q 
“ ` 
rBhV̂ k h`1sps, alq ´ Qk 
h,lps, alq ˘ 
` ` 
Qk h,lps, alq ´ Qk 
h,lps, al`1q ˘ 
` ` 
Qk h,lps, al`1q ´ rBhV̂ 
k h`1sps, al`1q 
˘ 
ď 2 ¨ ` 
2 ¨ 2´l ` χ 
a 
L0ζ ˘ 
´ 4 ¨ 2´l 
“ 2χ a 
L0ζ. (5.9.39) 
where the first inequality is derived from combining (5.9.36), (5.9.37), and (5.9.38). So from 
(5.9.35) and (5.9.39), we have that rBhV̂ k h`1sps, alq ´ rBhV̂ 
k h`1sps, al`1q ď 2χ 
? L0ζ holds in 
both cases. 
5.9.3.6 Proof of Lemma 5.9.20 
Proof of Lemma 5.9.20. We prove by induction on l. The induction basis holds at l “ 
0 by selecting a1 “ argmaxaPArBhV̂ k h`1sps, aq P A which ensures maxaPArBhV̂ 
k h`1sps, aq ´ 
rBhV̂ k h`1sps, a1q “ 0. Additionally, if the induction hypothesis holds for l ´ 1, we have that 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, al`1q 
“ ` 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, alq 
˘ 
` ` 
rBhV̂ k h`1sps, alq ´ rBhV̂ 
k h`1sps, al`1q 
˘ 
ď 2pl ´ 1qχ a 
L0ζ ` 2χ a 
L0ζ 
“ 2l ¨ χ a 
L0ζ, 
where the first inequality term is due to combining induction hypothesis with Lemma 5.9.19. 
We can then reach desired statement holds for all l in the range by induction. 
221
5.9.3.7 Proof of Lemma 5.9.21 
Proof of Lemma 5.9.21. According to Lemma 5.9.20, there exists some action al P Ak h,lpsq 
that 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, alq ď 2pl ´ 1qχ 
a 
L0ζ. (5.9.40) 
Moreover, we have 
rBhV̂ k h`1sps, alq ´ V k 
h,lpsq ď rBhV̂ k h`1sps, alq ´ Qk 
h,lps, alq ď 2 ¨ 2´l ` χ 
a 
L0ζ, (5.9.41) 
where the first inequality comes from the definition V k h,lpsq “ maxaPAk 
h,l Qk 
h,lps, aq and the 
second inequality holds according to Lemma 5.9.6 with l ď L0. Adding up (5.9.40) and 
(5.9.41) leads to 
max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,l ď 2 ¨ 2´l ` p2l ´ 1qχ 
a 
L0ζ. 
This completes the proof. 
5.9.3.8 Proof of Lemma 5.9.22 
Proof of Lemma 5.9.22. The statement holds by simply checking: 
V k h,lpsq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď V k 
h,lpsq ´ rBhV̂ k h`1sps, πk 
h,lpsqq 
“ Qk h,lps, π 
k h,lpsqq ´ rBhV̂ 
k h`1sps, π 
k h,lpsqq 
ď 2 ¨ 2´l ` χ 
a 
L0ζ, 
where the first inequality holds from maxaPArBhV̂ k h`1sps, aq ě rBhV̂ 
k h`1sps, π 
k h,lpsqq, the equal-
ity is from the definition V k h,lpsq “ Qk 
h,lps, π k h,lpsqq, and the last inequality holds according to 
Lemma 5.9.6 with the condition l ď L0. 
222
5.9.3.9 Proof of Lemma 5.9.23 
Proof of Lemma 5.9.23. The statement holds by checking 
min ␣ 
V k h,lpsq ` 3 ¨ 2´l, V̂ k 
h,l´1psq ( 
´ max aPA 
rBhV̂ k h`1sps, aq 
“ l 
min ℓ“1 
tV k h,ℓpsq ` 3 ¨ 2´ℓ 
u ´ max aPA 
rBhV̂ k h`1sps, aq 
ě l 
min ℓ“1 
t3 ¨ 2´ℓ ´ p2 ¨ 2´l 
` p2ℓ ´ 1qχ a 
L0ζqu 
“ 2´l ´ p2l ´ 1qχ 
a 
L0ζ, 
where the first equality holds due to V̂ k h,lpsq “ minl 
ℓ“1tV k h,ℓpsq ` 3 ¨ 2´ℓu, the inequality holds 
according to Lemma 5.9.21, and the last equality holds since 2´l decreases as l increases. 
5.9.3.10 Proof of Lemma 5.9.24 
Proof of Lemma 5.9.24. The statement holds by checking 
max aPA 
rBhV̂ k h`1sps, aq ´ max 
␣ 
V k h,lpsq ´ 3 ¨ 2´l, qV k 
h,l´1psq ( 
“ max aPA 
rBhV̂ k h`1sps, aq ´ 
l max ℓ“1 
tV k h,ℓpsq ´ 3 ¨ 2´ℓ 
u 
“ l 
min ℓ“1 
␣ 
max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,ℓpsq ` 3 ¨ 2´ℓ ( 
ě l 
min ℓ“1 
t´p2 ¨ 2´l ` χ 
a 
L0ζq ` 3 ¨ 2´ℓ u 
“ 2´l ´ χ 
a 
L0ζ, 
where the first equality holds due to the design of Algorithm 13 which would guarantee that 
qV k h,lpsq “ maxlℓ“1tV 
k h,ℓpsq ´ 3 ¨ 2´ℓu, the inequality holds according to Lemma 5.9.22, and the 
last equality holds since 2´l decreases as l increases. 
5.9.3.11 Proof of Lemma 5.9.25 
We prove Lemma 5.9.25 in this subsection. The first lemma which we introduce establishes 
an upper bound on the underestimation of the state value function V̂ k h for every action and 
223
every state through a categorised discussion based on whether Algorithm 13 reaches phase 
Lε for state s. Specifically, if the process does not reach phase Lε, we can substantiate the 
statement by applying Lemma 5.9.23 to phase lkhpsq ´ 1. Conversely, if the process reaches 
phase Lε, the statement can be proven by applying Lemma 5.9.21 to phase Lε. 
Lemma 5.9.33. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, h, sq P 
rKs ˆ rHs ˆ S, 
max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h psq ď 0.07ε{H. 
Now we are ready to prove Lemma 5.9.25 by induction. 
Proof of Lemma 5.9.25. We prove by induction on stage h P rHs. It is sufficient to show for 
any h P rHs, s P S, 
V ˚ h psq ´ V̂ k 
h psq ď 0.07ε ¨ pH ` 1 ´ hq{H. (5.9.42) 
We use induction on h from H ` 1 to 1 to prove the statement. The induction basis holds 
from the definition that V ˚ H`1psq “ V̂ k 
H`1psq “ 0. Assume the induction hypothesis (5.9.42) 
holds for h ` 1, we have 
max aPA 
rBhV ˚ h`1sps, aq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď max 
aPA rBhpV ˚ 
h`1 ´ V̂ k h`1qsps, aq 
ď max s1PS 
` 
V ˚ h`1ps 
1 q ´ V̂ k 
h`1ps 1 q ˘ 
ď 0.07ε ¨ pH ´ hq{H. (5.9.43) 
So for level h, it holds that 
V ˚ h psq ´ V̂ k 
h psq 
“ ` 
max aPA 
rBhV ˚ h`1sps, aq ´ max 
aPA rBhV̂ 
k h`1sps, aq 
˘ 
` ` 
max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h psq ˘ 
ď 0.07ε ¨ pH ´ hq{H ` 0.07ε{H ď 0.07ε ¨ pH ` 1 ´ hq{H, 
where the first inequality holds by combining (5.9.43) with Lemma 5.9.33. This proves the 
induction statement (5.9.42) for h, which leads to the desired statement. 
224
5.9.3.12 Proof of Lemma 5.9.26 
We prove Lemma 5.9.26 in this subsection, the first lemma we use establishes an upper 
bound on the overestimation of the state value function V̂ k h for the executed policy πk 
hpsq 
across all states. 
Lemma 5.9.34. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, h, sq P 
rKs ˆ rHs ˆ S, 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, πk 
hpsqq ď 16 ¨ 2´lkhpsq ` 0.10ε{H. 
Then the following lemma establishes an upper bound on the decision error induced by 
the arm-elimination process with respect to the state-action value function given by the 
ground-truth transform. 
Lemma 5.9.35. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, h, sq P 
rKs ˆ rHs ˆ S, 
V̂ k h psq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď 10 ¨ 2´lkhpsq 
` 0.06ε{H. 
Proof of Lemma 5.9.26. We can directly reach the desired result by taking summation on 
Lemma 5.9.34 and Lemma 5.9.35: 
V̂ k h psq ´ rBhV̂ 
k h`1sps, πk 
hpsqq 
ď ` 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, π 
k hpsqq 
˘ 
` ` 
V̂ k h psq ´ max 
aPA rBhV̂ 
k h`1sps, aq 
˘ 
ď ` 
16 ¨ 2´lkhpsq ` 0.10ε{H 
˘ 
` ` 
10 ¨ 2´lkhpsq ` 0.06ε{H 
˘ 
“ 26 ¨ 2´lkhpsq ` 0.16ε{H. 
5.9.3.13 Proof of Lemma 5.9.28 
We can prove the statement by applying a union bound to the concentration event, as given 
by the Azuma-Hoeffding inequality. 
225
Proof of Lemma 5.9.28. Consider some fixed h P rHs and ε “ 2´l ą 0. List the episodes 
index k such that V ˚ h pskhq ´ V πk 
h pskhq ą ε holds in ascending order as tτiui. Recall that 
ητih “ rPhpV̂ τi h`1 ´ V πτi 
h`1qspsτih , π τi h psτih qq ´ 
` 
V̂ τi h`1ps 
τi h`1q ´ V πτi 
h`1psτih`1q ˘ 
. 
Since the environment sample sτih1`1 according to Ph1p¨|sτih1 , a τi h1q, ητih1 is F τi 
h1`1-measurable with 
E “ 
ητih1 
ˇ 
ˇF τi h1 
‰ 
“ 0. Since both 0 ď V̂ τi h1`1ps 
τi h1`1q ď H and 0 ď V πτi 
h1`1psτih1`1q ď H hold, we have 
|ητih1 | ď 2H. According to Lemma 2.8.16 over filtration 
F τ1 h Ď F τ1 
h`1 Ď ¨ ¨ ¨ Ď F τ1 H Ď F τ2 
h Ď F τ2 h`1 Ď ¨ ¨ ¨ Ď F τ2 
H Ď ¨ ¨ ¨ Ď F τi h1 Ď ¨ ¨ ¨ 
for some fixed S “ |Kε h|, the good event that 
|Kε h| 
ÿ 
i“1 
H ÿ 
h1“h 
ητih1 ď 2H a 
2HS logp4HS2l2{δq “ 4 b 
H3|Kε h| logp4H|Kε 
h| logpε´1q{δq 
happens with probability at least 1 ´ δ{p4HS2l2q. By the union bound statement over all 
ph, S, lq P rHs ˆ rKs ˆ N`, we have the bad event happens with probability at most 
PrrGA 2s ď 
H ÿ 
h“1 
K ÿ 
S“1 
8 ÿ 
l“1 
PrrB2ph, 2 ´l 
qs ď 
H ÿ 
h“1 
K ÿ 
S“1 
8 ÿ 
l“1 
δ 
4HS2l2 ď δ, 
where the last inequality holds from ř 
ně1 n ´2 “ π2{6, which reach the desired statement. 
5.9.3.14 Proof of Lemma 5.9.29 
We first provide the following instantaneous regret upper bound by combining Lemma 5.9.25 
and Lemma 5.9.26. 
Lemma 5.9.36. Under event G1 and for all ε ą 0 that Gε is satisfied, for any pk, hq P 
rKs ˆ rHs, 
V ˚ h pskhq ´ V πk 
h pskhq ď 0.23ε ` 26 H ÿ 
h1“h 
2´lk h1 psk 
h1 q ` 
H ÿ 
h1“h 
ηkh1 , 
where ηkh “ rPhpV̂ k h`1 ´ V πk 
h`1qspskh, π k hpskhqq ´ 
` 
V̂ k h`1ps 
k h`1q ´ V πk 
h`1ps k h`1q 
˘ 
is a Fk h`1-measurable 
random variable that Erηkh|Fk h s “ 0 and |ηkh| ď H. 
226
Together with Lemma 5.9.9 and the definition of G2, we can provide an upper bound for 
arbitrary subsets. 
Proof of Lemma 5.9.29. Taking summation on result given by Lemma 5.9.36 to all k P K 
gives 
ÿ 
kPK 
` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ď 0.23|K|ε ` 26 ÿ 
kPK 
H ÿ 
h1“h 
2´lk h1 psk 
h1 q ` 
ÿ 
kPK 
H ÿ 
h1“h 
ηkh1 . (5.9.44) 
We can bound the second term according to Lemma 5.9.9, 
26 ÿ 
kPK 
H ÿ 
h1“h 
2´lk h1 psk 
h1 q ď 0.26|K|ε ` 217LεdH 
2γ2 Lε ε´1. (5.9.45) 
Under event G2, the third term satisfies that 
ÿ 
kPK 
H ÿ 
h1“h 
ηkh1 ď 4 a 
H3|K| logp4H|K| logpε´1q{δq. (5.9.46) 
Plugging (5.9.45) and (5.9.46) into (5.9.44) gives ÿ 
kPK 
` 
V ˚ h pskhq ´ V πk 
h pskhq ˘ 
ď 0.49|K|ε ` 217LεdH 2γ2 
Lε ε´1 
` 4 a 
H3|K| logp4H|K| logpε´1q{δq. 
(5.9.47) 
5.9.4 Proof of Lemmas in Section 5.9.3 
5.9.4.1 Proof of Lemma 5.9.33 
Proof of Lemma 5.9.33. We start the proof by discussing different cases. First, if lkhpsq ď Lε, 
we have lkhpsq ´ 1 ď mintLε, l k hpsq ´ 1u, according to the definition of V̂ k 
h,lpsq, 
max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h psq “ max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h,lkhpsq´1psq 
ď ´2´plkhpsq´1q ` 2plkhpsq ´ 1qχ 
a 
Lεζ 
ď 0 ` 2χL1.5 ε ζ 
ď 0.02ε{H, (5.9.48) 
227
where the first inequality holds from Lemma 5.9.23, and the last inequality holds due to 
χL1.5 ε ζ ď 2´Lε ď 0.01ε{H given by Gε. 
On the other hand, when lkhpsq ą Lε, we have Lε ď mintLε, l k hpsq ´ 1u and thus 
V̂ k h psq ě qV k 
h,Lε psq ě V k 
h,Lε psq ´ 3 ¨ 2´Lε (5.9.49) 
where the first inequality is due to Lemma 5.9.2 and the second inequality holds due to the 
definition of qV k h,Lε 
psq. Therefore, Lε ď mintLε, l k hpsq ´ 1u yields 
max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h psq ď max aPA 
rBhV̂ k h`1sps, aq ´ V k 
h,Lε psq ` 3 ¨ 2´Lε 
ď 5 ¨ 2´Lε ` p2Lε ´ 1qχ a 
Lεζ 
ď 0.05ε{H ` 0.02ε{H “ 0.07ε{H, (5.9.50) 
where the first inequality is given by (5.9.49), the second inequality is given by Lemma 5.9.21, 
and the last inequality holds from χL1.5 ε ζ ď 2´Lε ď 0.01ε{H given by Gε. So considering 
both (5.9.48) and (5.9.50), we have the first statement 
max aPA 
rBhV̂ k h`1sps, aq ´ V̂ k 
h psq ď 0.07ε{H 
always holds under event G1. 
5.9.4.2 Proof of Lemma 5.9.34 
We prove Lemma 5.9.34 by applying Lemma 5.9.7 on phase mintLε, l k hpsq ´ 1u, in this sub-
section. 
Proof of Lemma 5.9.34. Note we have πk h,lkhpsq´1 
psq P Ak h,lkhpsq 
psq according to the definition of 
Ak h,l`1psq. This implies πk 
hpsq P Ak h,lkhpsq 
psq during the elimination process. 
228
If lkhpsq ď Lε, we have lkhpsq ´ 1 ď mintLε, l k hpsq ´ 1u. Thus, 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, π 
k hpsqq ď 8 ¨ 2´plkhpsq´1q 
` 2lkhpsq ¨ χ a 
Lεζ 
ď 16 ¨ 2´lkhpsq ` 2χL1.5 
ε ζ 
ď 16 ¨ 2´lkhpsq ` 0.02ε{H, (5.9.51) 
where the first inequality follows from Lemma 5.9.7 with πk hpsq P Ak 
h,lkhpsq psq and the last 
inequality holds due to χL1.5 ε ζ ď 0.01ε{H given by Gε. 
Otherwise, we have Lε ď mintLε, l k hpsq ´ 1u. In this case, we have 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, π 
k hpsqq ď 8 ¨ 2´Lε ` 2χL1.5 
ε ζ 
ď 0.08ε{H ` 0.02ε{H “ 0.10ε{H, (5.9.52) 
where the first inequality follows from Lemma 5.9.7 with πk hpsq P Ak 
h,lkhpsq psq Ď Ak 
h,Lε psq 
according to the elimination routine and the final inequality holds due to χL1.5 ε ζ ď 2´Lε ď 
0.01ε{H given by Gε. So by combining (5.9.51) and (5.9.52), we have the desired statement 
that 
max aPA 
rBhV̂ k h`1sps, aq ´ rBhV̂ 
k h`1sps, πk 
hpsqq ď 16 ¨ 2´lkhpsq ` 0.10ε{H. 
5.9.4.3 Proof of Lemma 5.9.35 
We prove Lemma 5.9.35 in this section by applying Lemma 5.9.22 on phase mintLε, l k hpsq´1u. 
Proof of Lemma 5.9.35. If lkhpsq ď Lε, we have lkhpsq ´ 1 ď mintLε, l k hpsq ´ 1u. Firstly, we 
have 
V̂ k h psq ď V̂ k 
h,lkhpsq´1psq ď V k h,lkhpsq´1psq ` 3 ¨ 2´plkhpsq´1q. (5.9.53) 
229
where the first inequality is given by Lemma 5.9.2 and the second inequality follows from 
the definition of V̂ k h,lkhpsq´1 
psq. This leads to 
V̂ k h psq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď 
` 
V̂ k h psq ´ V k 
h,lkhpsq´1psq ˘ 
` ` 
V k h,lkhpsq´1psq ´ max 
aPA rBhV̂ 
k h`1sps, aq 
˘ 
ď 3 ¨ 2´plkhpsq´1q ` 2 ¨ 2´plkhpsq´1q 
` χ a 
Lεζ 
ď 10 ¨ 2´lkhpsq ` 0.01ε{H, (5.9.54) 
where in the second inequality, the first term is given by (5.9.53) and the second term holds 
according to Lemma 5.9.22, and the third inequality holds from χ ? Lεζ ď 0.01ε{H given by 
Gε. 
Otherwise, we have Lε ď mintLε, l k hpsq ´ 1u, this leads to 
V̂ k h psq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď 
` 
V̂ k h psq ´ V k 
h,Lε psq 
˘ 
` ` 
V k h,Lε 
psq ´ max aPA 
rBhV̂ k h`1sps, aq 
˘ 
ď 3 ¨ 2´Lε ` 2 ¨ 2´Lε ` χ a 
Lεζ 
ď 0.03ε{H ` 0.02ε{H ` 0.01ε{H “ 0.06ε{H, (5.9.55) 
where in the second inequality, the first term is given by the definition of V̂ k h psq and the 
second term holds according to Lemma 5.9.22, and the third inequality holds from χL1.5 ε ζ ď 
2´Lε ď 0.01ε{H given by Gε. Combining (5.9.54) and (5.9.55) gives the desired statement 
V̂ k h psq ´ max 
aPA rBhV̂ 
k h`1sps, aq ď 10 ¨ 2´lkhpsq 
` 0.06ε{H. 
5.9.4.4 Proof of Lemma 5.9.36 
Proof of Lemma 5.9.36. According to the definition in which V πk 
h pskhq “ rBhV πk 
h`1spskh, π k hpskhqq 
and ηkh ` rPhpV̂ k h`1 ´ V πk 
h`1qspskh, π k hpskhqq ´ 
` 
V̂ k h`1ps 
k h`1q ´ V πk 
h`1ps k h`1q 
˘ 
. We can write 
V̂ k h pskhq ´ V πk 
h pskhq “ ` 
V̂ k h pskhq ´ rBhV̂ 
k h`1sps 
k h, π 
k hpskhqq 
˘ 
` ηkh ` ` 
V̂ k h`1ps 
k h`1q ´ V πk 
h`1pskh`1q ˘ 
. 
230
By a telescoping statement from h to H with the final terminal value V̂ k H`1p¨q “ V πk 
H`1p¨q “ 0, 
we reach 
V̂ k h pskhq ´ V πk 
h pskhq “ 
H ÿ 
h1“h 
` 
V̂ k h pskhq ´ rBhV̂ 
k h`1sps 
k h, π 
k hpskhqq 
˘ 
` 
H ÿ 
h1“h 
ηkh1 . (5.9.56) 
As a result, we can bound the desired term by 
V ˚ h pskhq ´ V πk 
h pskhq ď V̂ k h pskhq ´ V πk 
h pskhq ` 0.07ε 
“ 
H ÿ 
h1“h 
` 
V̂ k h pskhq ´ rBhV̂ 
k h`1sps 
k h, π 
k hpskhqq 
˘ 
` 
H ÿ 
h1“h 
ηkh1 ` 0.07ε 
ď 
H ÿ 
h1“h 
` 
26 ¨ 2´lk h1 psk 
h1 q ` 0.16ε{H 
˘ 
` 
H ÿ 
h1“h 
ηkh1 ` 0.07ε 
“ 0.23ε ` 26 H ÿ 
h1“h 
2´lk h1 psk 
h1 q ` 
H ÿ 
h1“h 
ηkh1 . 
where the first inequality is given by Lemma 5.9.25, the first equality is given by (5.9.56), 
and the final inequality is given by Lemma 5.9.26. 
5.9.5 Technical Numerical Lemmas 
Lemma 5.9.37. If |Ck h,l| ď 4ld ` 2.5 ¨ 4lγ2 
l d ln ` 
1 ` |Ck h,l|{p16dq 
˘ 
, then |Ck h,l| ď 16l ¨ 4lγ2 
l d. 
Proof. Denote c “ |Ck h,l|{pl ¨ 4lγ2 
l dq. We have that 
cl ¨ 4lγ2 l d ď 4ld ` 2.5 ¨ 4lγ2 
l d lnp1 ` cl ¨ 4lγ2 l {16q. 
Dividing both sides by 4lγ2 l d, we have that 
cl ď 1{γ2 l ` 2.5 lnp1 ` cl ¨ 4lγ2 
l {16q 
ď 1{γ2 l ` 2.5 lnp4c ¨ 5lγ2 
l {16q ď 1{γ2 l ` 4.1l ` 2.5 lnpcq. 
Since l ě 1 and γl ě 1, we can further conclude that 
c ď 5.1 ` 2.5 lnpcq ď 5.1 ` 2.5p1 ` c{6q. 
231
The necessary condition for the above inequality is c ď 16, which proves the desired state-
ment. 
Lemma 5.9.38. For any l ě 1, γl`1{γl ď 1.4. 
Proof. Firstly, we have that 
l ` 22 ` logpl ` 1q 
l ` 20 ` logplq ď 
l ` 22 ` 0.2l ` 2 
l ` 20 “ 1.2, (5.9.57) 
where the first inequality holds due to logpx ` 1q ď 0.2x ` 2. In addition, we have 
4 ` logpl ` 1q 
4 ` logplq ď 
4 ` logplq ` 1 
4 ` logplq ď 1.25, (5.9.58) 
where the first inequality holds due to logpx` 1q ď logpxq ` 1. As a result, we can reach the 
desired statement according to 
γl`1 
γl “ 
5pl ` 1 ` r20 ` logppl ` 1qdqsqdH a 
logp16pl ` 1qdH{δq 
5pl ` r20 ` logpldqsqdH a 
logp16ldH{δq 
ď l ` 22 ` logpl ` 1q ` logpdq 
l ` 20 ` logplq ` logpdq ¨ 
d 
logpl ` 1q ` logp16dH{δq 
logplq ` logp16dH{δq 
ď l ` 22 ` logpl ` 1q 
l ` 20 ` logplq ¨ 
d 
logpl ` 1q 
logplq 
ď 1.2 ? 1.25 
ď 1.4, 
where the third inequality holds from plugging both (5.9.57) and (5.9.58). 
Lemma 5.9.39. 
b 
2d lnp1 ` l ¨ 4lγ2 l q ` 2 lnpl2Hp222d6H4ql 
2 `d2{δq ď γl,l` 
232
Proof. By calculation, we have that 
H 
b 
2d lnp1 ` l ¨ 4lγ2 l q ` 2 lnpl2Hp222d6H4ql 
2 `d2{δq 
ď H b 
2d lnp1 ` l ¨ 4l ¨ 1.42lγ2 1q ` H 
b 
12l2`d 2 lnp24ldH{δq 
ď l`dH a 
2 lnp24ldH{δq ` l`dH a 
12 lnp24ldH{δq 
ď 5l`dH b 
logp24γl`ldH{δq 
“ γl,l` . 
Lemma 5.9.40. If some constant c1, c2 ą 0 that 
|Kε h| ă c1LεpLε ` logpdHqq 
2d3H4ε´2 logpLεd{δq ` ε´1 b 
c2H3|Kε h| logpH|Kε 
h| logpε´1q{δq. 
Then, there exists c3 ą 0 such that 
|Kε h| ă c3LεpLε ` logpdHqq 
2d3H4ε´2 logpLεdq logpδ´1 qι, 
where ι is a polynomial of log logpLεdHδ´1q. 
Proof. Let x “ |Kε h|{ logp|Kε 
h|q. We have that 
x ă c1LεpLε ` logpdHqq 2d3H4ε´2 logpLεd{δq ` ε´1 
a 
c2H3x logpH logpε´1q{δq. 
Since x ă a ` ? bx implies x ă 2a ` 2b, so the above inequality implies 
x ă 2c1LεpLε ` logpdHqq 2d3H4ε´2 logpLεd{δq ` 2c2H 
3ε´2 logpH logpε´1 q{δq. 
Moreover, since y{ logpyq ă a implies y ă 2a log a, we can conclude that there exists c3 ą 0 
that 
|Kε h| ă c3LεpLε ` logpdHqq 
2d3H4ε´2 logpLεdq logpδ´1 qι, 
where ι is a polynomial of log logpLεdHε´1δ´1q. 
233
CHAPTER 6 
Conclusions and Future Directions 
This dissertation addressed several key concerns in reinforcement learning, including unsu-
pervised exploration in the face of the uncertainty of the environment and model robustness in 
the face of the uncertainty of the function approximation, from the perspective of theoretical 
analysis. Several practical algorithms were also proposed to achieve competitive performance 
with theoretical guarantees. In particular, in the first part of this dissertation, we analyzed 
reward-free exploration with linear function approximations then extended the analysis to 
general function approximations. We affirmatively answered the question: How to explore 
the environment without human supervision by building the connection between reward-free 
exploration with unsupervised reinforcement learning from both theoretical and empirical 
perspectives. In the second part of this dissertation, we discussed model misspecification 
for decision making systems. We answered the question by providing a theoretical threshold 
showing How large a model misspecification can be tolerated in order to make good decisions. 
We also proposed algorithms in the context of misspecified linear bandits and reinforcement 
learning. All of the proposed algorithms will provably only suffer from finite suboptimality 
over infinite runs, without additional prior assumptions. To the best of our knowledge, these 
are the first constant regret results in the literature. 
This dissertation also suggests several open questions for future research. In particular, 
the first part of this dissertation assumes that the reward function is provided as an oracle 
during the planning phase. However, learning the reward function can be challenging in 
practice. One might ask, How would current reward-free exploration methods integrate with 
234
reward learning processes? For example, it would be valuable to investigate how the reward 
learning process, such as fine-tuning (Laskin et al., 2020), RL with human feedback (Peng 
et al., 2023; Christiano et al., 2017; Rafailov et al., 2024), could affect the planning phase in 
reward-free exploration. In the second part of this thesis, we have demonstrated a minimax-
optimal separation between model misspecification and the suboptimality gap. However, 
several open questions remain unresolved in this context. First, there is a log |D| gap between 
the positive and negative results (Lattimore et al., 2020). In RL, this translates into the 
difference between misspecifications in the } ¨ }TV norm and the } ¨ }8 norm, as used in Du 
et al. (2019), which can become significant as the number of states increases. Second, the 
current multi-phase estimation approach is challenging to implement in practice and suffers 
from a large constant, although it is of the same order in Õp¨q notation. It remains an 
open question whether this gap between positive and negative results can be closed and 
whether a more practical algorithm for this multi-phase estimation regime can be developed. 
Such investigations would not only enhance the theoretical understanding of RL but also 
enhance confidence in applying RL to critical tasks such as dynamic clinical treatments or 
autonomous scientific discoveries. 
In addition to the technical open questions highlighted earlier, this dissertation opens 
several promising directions for future research. For instance, foundation models, such as dif-
fusion models (Ho et al., 2020; Song et al., 2020) and large language models (LLMs) (Achiam 
et al., 2023; Touvron et al., 2023), have shown potential in enhancing our understanding of 
linguistic and visual inputs. On one front, reinforcement learning methods are widely used 
to finetune these models with online human preferences (Ouyang et al., 2022; Rafailov et al., 
2024). These applications necessitate a thorough investigation into the robustness and effi-
ciency of these algorithms. For example, a key question to explore is whether RL methods 
would exacerbate or mitigate hallucination in LLMs. Furthermore, there is considerable 
potential in harnessing the capabilities of existing foundation models to better understand 
environmental interactions and enhance decision-making processes (Zhao et al., 2024). It is 
235
crucial to develop a framework that specifically analyzes the behavior of these models within 
RL agents, moving beyond the use of general function approximators. 
Lastly, while the application of RL in gaming has been well explored, extending these 
methodologies to more practical fields, such as drug design (Popova et al., 2018) or policy-
making for pandemic control (Kwak et al., 2021), could be highly beneficial. Integrating 
RL with autonomous systems (Sheng et al., 2024) would significantly enhance the efficiency 
of these applications. Moreover, establishing performance guarantees for the robustness, 
explainability and accountability of RL agents becomes imperative, particularly in critical 
domains such as healthcare, science discovery or autonomous laboratory. 
236
Bibliography 
Abbasi-Yadkori, Y., Pál, D. and Szepesvári, C. (2011). Improved algorithms for linear 
stochastic bandits. In Advances in Neural Information Processing Systems, vol. 24. 
Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., 
Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S. et al. (2023). Gpt-
4 technical report. arXiv preprint arXiv:2303.08774 . 
Agarwal, A., Hsu, D., Kale, S., Langford, J., Li, L. and Schapire, R. (2014). 
Taming the monster: A fast and simple algorithm for contextual bandits. In International 
Conference on Machine Learning. PMLR. 
Agarwal, A., Jin, Y. and Zhang, T. (2022). Voql: Towards optimal regret in model-free 
rl with nonlinear function approximation. arXiv preprint arXiv:2212.06069 . 
Agrawal, S. and Goyal, N. (2013). Thompson sampling for contextual bandits with 
linear payoffs. In International Conference on Machine Learning. PMLR. 
Auer, P. (2002). Using confidence bounds for exploitation-exploration trade-offs. Journal 
of Machine Learning Research 3 397–422. 
Ayoub, A., Jia, Z., Szepesvari, C., Wang, M. and Yang, L. (2020). Model-based 
reinforcement learning with value-targeted regression. In International Conference on 
Machine Learning. PMLR. 
Azuma, K. (1967). Weighted sums of certain dependent random variables. Tohoku Mathe-
matical Journal, Second Series 19 357–367. 
Berner, C., Brockman, G., Chan, B., Cheung, V., Dębiak, P., Dennison, C., 
Farhi, D., Fischer, Q., Hashme, S., Hesse, C. et al. (2019). Dota 2 with large scale 
deep reinforcement learning. arXiv preprint arXiv:1912.06680 . 
237
Burda, Y., Edwards, H., Pathak, D., Storkey, A., Darrell, T. and Efros, A. A. 
(2018a). Large-scale study of curiosity-driven learning. arXiv preprint arXiv:1808.04355 
. 
Burda, Y., Edwards, H., Storkey, A. and Klimov, O. (2018b). Exploration by random 
network distillation. arXiv preprint arXiv:1810.12894 . 
Cai, Q., Yang, Z., Jin, C. and Wang, Z. (2020). Provably efficient exploration in policy 
optimization. In International Conference on Machine Learning. PMLR. 
Camilleri, R., Jamieson, K. and Katz-Samuels, J. (2021). High-dimensional exper-
imental design and kernel bandits. In International Conference on Machine Learning. 
PMLR. 
Cesa-Bianchi, N. and Lugosi, G. (2006). Prediction, learning, and games. Cambridge 
university press. 
Chen, F., Mei, S. and Bai, Y. (2022a). Unified algorithms for rl with decision-estimation 
coefficients: No-regret, pac, and reward-free learning. arXiv preprint arXiv:2209.11745 . 
Chen, J., Modi, A., Krishnamurthy, A., Jiang, N. and Agarwal, A. (2022b). On 
the statistical efficiency of reward-free exploration in non-linear rl. Advances in Neural 
Information Processing Systems 35 20960–20973. 
Chen, X., Hu, J., Yang, L. and Wang, L. (2021). Near-optimal reward-free exploration 
for linear mixture mdps with plug-in solver. In International Conference on Learning 
Representations. 
Chen, Z., Li, C. J., Yuan, A., Gu, Q. and Jordan, M. I. (2022c). A general frame-
work for sample-efficient function approximation in reinforcement learning. arXiv preprint 
arXiv:2209.15634 . 
238
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S. and Amodei, D. 
(2017). Deep reinforcement learning from human preferences. Advances in neural infor-
mation processing systems 30. 
Chu, W., Li, L., Reyzin, L. and Schapire, R. (2011). Contextual bandits with linear 
payoff functions. In Proceedings of the Fourteenth International Conference on Artificial 
Intelligence and Statistics. JMLR Workshop and Conference Proceedings. 
Dann, C., Jiang, N., Krishnamurthy, A., Agarwal, A., Langford, J. and 
Schapire, R. E. (2018). On oracle-efficient pac rl with rich observations. Advances 
in neural information processing systems 31. 
Dann, C., Marinov, T. V., Mohri, M. and Zimmert, J. (2021). Beyond value-function 
gaps: Improved instance-dependent regret bounds for episodic reinforcement learning. 
Advances in Neural Information Processing Systems 34. 
Dantzig, G. B. (1965). Linear programming and extensions, vol. 48. Princeton university 
press. 
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K. and Fei-Fei, L. (2009). Imagenet: 
A large-scale hierarchical image database. In 2009 IEEE Conference on Computer Vision 
and Pattern Recognition. 
Dilokthanakul, N., Kaplanis, C., Pawlowski, N. and Shanahan, M. (2019). Fea-
ture control as intrinsic motivation for hierarchical reinforcement learning. IEEE transac-
tions on neural networks and learning systems 30 3409–3418. 
Du, S. S., Kakade, S. M., Wang, R. and Yang, L. F. (2019). Is a good representation 
sufficient for sample efficient reinforcement learning? arXiv preprint arXiv:1910.03016 . 
Elson, J., Douceur, J. J., Howell, J. and Saul, J. (2007). Asirra: A captcha that 
exploits interest-aligned manual image categorization. In Proceedings of 14th ACM Con-
239
ference on Computer and Communications Security (CCS). Association for Computing 
Machinery, Inc. 
Eysenbach, B., Gupta, A., Ibarz, J. and Levine, S. (2018). Diversity is all you need: 
Learning skills without a reward function. arXiv preprint arXiv:1802.06070 . 
Foster, D. J., Gentile, C., Mohri, M. and Zimmert, J. (2020). Adapting to mis-
specification in contextual bandits. Advances in Neural Information Processing Systems 
33. 
Foster, D. J., Kakade, S. M., Qian, J. and Rakhlin, A. (2021). The statistical 
complexity of interactive decision making. arXiv preprint arXiv:2112.13487 . 
Ghosh, A., Chowdhury, S. R. and Gopalan, A. (2017). Misspecified linear bandits. In 
Proceedings of the AAAI Conference on Artificial Intelligence, vol. 31. 
Hafner, D., Lillicrap, T., Ba, J. and Norouzi, M. (2019a). Dream to control: Learning 
behaviors by latent imagination. arXiv preprint arXiv:1912.01603 . 
Hafner, D., Lillicrap, T., Fischer, I., Villegas, R., Ha, D., Lee, H. and Davidson, 
J. (2019b). Learning latent dynamics for planning from pixels. In International conference 
on machine learning. PMLR. 
Hansen, S., Dabney, W., Barreto, A., Van de Wiele, T., Warde-Farley, D. and 
Mnih, V. (2019). Fast task inference with variational intrinsic successor features. arXiv 
preprint arXiv:1906.05030 . 
Hao, B., Lattimore, T. and Szepesvari, C. (2020). Adaptive exploration in linear 
contextual bandit. In International Conference on Artificial Intelligence and Statistics. 
PMLR. 
He, J., Zhao, H., Zhou, D. and Gu, Q. (2022a). Nearly minimax optimal reinforcement 
learning for linear markov decision processes. arXiv preprint arXiv:2212.06132 . 
240
He, J., Zhou, D. and Gu, Q. (2021a). Logarithmic regret for reinforcement learning with 
linear function approximation. In International Conference on Machine Learning. PMLR. 
He, J., Zhou, D. and Gu, Q. (2021b). Uniform-PAC bounds for reinforcement learning with 
linear function approximation. In Advances in Neural Information Processing Systems. 
He, J., Zhou, D., Zhang, T. and Gu, Q. (2022b). Nearly optimal algorithms for lin-
ear contextual bandits with adversarial corruptions. In Advances in Neural Information 
Processing Systems. 
He, K., Zhang, X., Ren, S. and Sun, J. (2015). Delving deep into rectifiers: Surpassing 
human-level performance on imagenet classification. In Proceedings of the IEEE interna-
tional conference on computer vision. 
He, K., Zhang, X., Ren, S. and Sun, J. (2016). Deep residual learning for image recog-
nition. In Proceedings of the IEEE conference on computer vision and pattern recognition. 
Ho, J., Jain, A. and Abbeel, P. (2020). Denoising diffusion probabilistic models. Advances 
in neural information processing systems 33 6840–6851. 
Hu, P., Chen, Y. and Huang, L. (2022). Towards minimax optimal reward-free rein-
forcement learning in linear mdps. In The Eleventh International Conference on Learning 
Representations. 
Jaksch, T., Ortner, R. and Auer, P. (2010). Near-optimal regret bounds for reinforce-
ment learning. Journal of Machine Learning Research 11. 
Jia, Z., Yang, L., Szepesvari, C. and Wang, M. (2020). Model-based reinforcement 
learning with value-targeted regression. In Learning for Dynamics and Control. PMLR. 
Jiang, N., Krishnamurthy, A., Agarwal, A., Langford, J. and Schapire, R. E. 
(2017). Contextual decision processes with low bellman rank are pac-learnable. In Inter-
national Conference on Machine Learning. PMLR. 
241
Jin, C., Allen-Zhu, Z., Bubeck, S. and Jordan, M. I. (2018). Is q-learning provably 
efficient? In Advances in Neural Information Processing Systems. 
Jin, C., Krishnamurthy, A., Simchowitz, M. and Yu, T. (2020a). Reward-free ex-
ploration for reinforcement learning. In International Conference on Machine Learning. 
PMLR. 
Jin, C., Liu, Q. and Miryoosefi, S. (2021). Bellman eluder dimension: New rich classes 
of rl problems, and sample-efficient algorithms. Advances in neural information processing 
systems 34 13406–13418. 
Jin, C., Yang, Z., Wang, Z. and Jordan, M. I. (2020b). Provably efficient reinforcement 
learning with linear function approximation. In Conference on Learning Theory. PMLR. 
Kalashnikov, D., Varley, J., Chebotar, Y., Swanson, B., Jonschkowski, R., 
Finn, C., Levine, S. and Hausman, K. (2022). Scaling up multi-task robotic reinforce-
ment learning. In Conference on Robot Learning. PMLR. 
Kang, Y., Zhao, E., Zang, Y., Li, K. and Xing, J. (2022). Towards a unified benchmark 
for reinforcement learning in sparse reward environments. In International Conference on 
Neural Information Processing. Springer. 
Karmarkar, N. (1984). A new polynomial-time algorithm for linear programming. In 
Proceedings of the sixteenth annual ACM symposium on Theory of computing. 
Kaufmann, E., Ménard, P., Domingues, O. D., Jonsson, A., Leurent, E. and 
Valko, M. (2021a). Adaptive reward-free exploration. In Algorithmic Learning Theory. 
PMLR. 
Kaufmann, E., Ménard, P., Domingues, O. D., Jonsson, A., Leurent, E. and 
Valko, M. (2021b). Adaptive reward-free exploration. In Algorithmic Learning Theory. 
PMLR. 
242
Kearns, M. and Singh, S. (2002). Near-optimal reinforcement learning in polynomial 
time. Machine learning 49 209–232. 
Kendall, A. and Gal, Y. (2017). What uncertainties do we need in bayesian deep learning 
for computer vision? Advances in neural information processing systems 30. 
Kober, J., Bagnell, J. A. and Peters, J. (2013). Reinforcement learning in robotics: 
A survey. The International Journal of Robotics Research 32 1238–1274. 
Kong, D., Salakhutdinov, R., Wang, R. and Yang, L. F. (2021). Online sub-
sampling for reinforcement learning with general function approximation. arXiv preprint 
arXiv:2106.07203 . 
Kwak, G. H., Ling, L. and Hui, P. (2021). Deep reinforcement learning approaches for 
global public health strategies for covid-19 pandemic. PloS one 16 e0251550. 
Laskin, M., Srinivas, A. and Abbeel, P. (2020). Curl: Contrastive unsupervised repre-
sentations for reinforcement learning. In International Conference on Machine Learning. 
PMLR. 
Laskin, M., Yarats, D., Liu, H., Lee, K., Zhan, A., Lu, K., Cang, C., Pinto, L. 
and Abbeel, P. (2021). Urlb: Unsupervised reinforcement learning benchmark. arXiv 
preprint arXiv:2110.15191 . 
Lattimore, T. and Szepesvári, C. (2020). Bandit algorithms. Cambridge University 
Press. 
Lattimore, T., Szepesvari, C. and Weisz, G. (2020). Learning with good feature 
representations in bandits and in rl with a generative model. In International Conference 
on Machine Learning. PMLR. 
243
Lee, L., Eysenbach, B., Parisotto, E., Xing, E., Levine, S. and Salakhutdi-
nov, R. (2019). Efficient exploration via state marginal matching. arXiv preprint 
arXiv:1906.05274 . 
Levine, S., Finn, C., Darrell, T. and Abbeel, P. (2016). End-to-end training of deep 
visuomotor policies. The Journal of Machine Learning Research 17 1334–1373. 
Li, L., Chu, W., Langford, J. and Schapire, R. E. (2010). A contextual-bandit ap-
proach to personalized news article recommendation. In Proceedings of the 19th interna-
tional conference on World wide web. 
Li, L., Chu, W., Langford, J. and Wang, X. (2011). Unbiased offline evaluation of 
contextual-bandit-based news article recommendation algorithms. In Proceedings of the 
fourth ACM international conference on Web search and data mining. 
Li, Y., Wang, R. and Yang, L. F. (2022). Settling the horizon-dependence of sample com-
plexity in reinforcement learning. In 2021 IEEE 62nd Annual Symposium on Foundations 
of Computer Science (FOCS). IEEE. 
Liu, H. and Abbeel, P. (2021a). Aps: Active pretraining with successor features. In 
International Conference on Machine Learning. PMLR. 
Liu, H. and Abbeel, P. (2021b). Behavior from the void: Unsupervised active pre-training. 
Advances in Neural Information Processing Systems 34 18459–18473. 
Lykouris, T., Simchowitz, M., Slivkins, A. and Sun, W. (2021). Corruption-robust 
exploration in episodic reinforcement learning. In Conference on Learning Theory. PMLR. 
Mai, V., Mani, K. and Paull, L. (2022). Sample efficient deep reinforcement learning via 
uncertainty estimation. arXiv preprint arXiv:2201.01666 . 
244
Ménard, P., Domingues, O. D., Jonsson, A., Kaufmann, E., Leurent, E. and 
Valko, M. (2020). Fast active learning for pure exploration in reinforcement learning. 
arXiv preprint arXiv:2007.13442 . 
Ménard, P., Domingues, O. D., Jonsson, A., Kaufmann, E., Leurent, E. and 
Valko, M. (2021). Fast active learning for pure exploration in reinforcement learning. In 
International Conference on Machine Learning. PMLR. 
Michael, S. P. S. T. J. and Jordan, I. (1995). Reinforcement learning with soft state 
aggregation. Advances in neural information processing systems 7 7 361. 
Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, 
D. and Riedmiller, M. (2013). Playing atari with deep reinforcement learning. arXiv 
preprint arXiv:1312.5602 . 
Modi, A., Jiang, N., Tewari, A. and Singh, S. (2020). Sample complexity of reinforce-
ment learning using linearly combined model ensembles. In International Conference on 
Artificial Intelligence and Statistics. 
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, 
C., Agarwal, S., Slama, K., Ray, A. et al. (2022). Training language models to follow 
instructions with human feedback. Advances in neural information processing systems 35 
27730–27744. 
Papini, M., Tirinzoni, A., Pacchiano, A., Restelli, M., Lazaric, A. and Pirotta, 
M. (2021a). Reinforcement learning in linear mdps: Constant regret and representation 
selection. Advances in Neural Information Processing Systems 34 16371–16383. 
Papini, M., Tirinzoni, A., Restelli, M., Lazaric, A. and Pirotta, M. (2021b). 
Leveraging good representations in linear contextual bandits. In International Conference 
on Machine Learning. PMLR. 
245
Pathak, D., Agrawal, P., Efros, A. A. and Darrell, T. (2017). Curiosity-driven 
exploration by self-supervised prediction. In International conference on machine learning. 
PMLR. 
Pathak, D., Gandhi, D. and Gupta, A. (2019). Self-supervised exploration via disagree-
ment. In International conference on machine learning. PMLR. 
Peng, B., Li, C., He, P., Galley, M. and Gao, J. (2023). Instruction tuning with gpt-4. 
arXiv preprint arXiv:2304.03277 . 
Popova, M., Isayev, O. and Tropsha, A. (2018). Deep reinforcement learning for de 
novo drug design. Science advances 4 eaap7885. 
Qiu, S., Wang, L., Bai, C., Yang, Z. and Wang, Z. (2022). Contrastive ucb: Provably 
efficient contrastive self-supervised learning in online reinforcement learning. In Interna-
tional Conference on Machine Learning. PMLR. 
Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S. and Finn, C. 
(2024). Direct preference optimization: Your language model is secretly a reward model. 
Advances in Neural Information Processing Systems 36. 
Ren, T., Li, J., Dai, B., Du, S. S. and Sanghavi, S. (2021). Nearly horizon-free offline 
reinforcement learning. Advances in neural information processing systems 34 15621– 
15634. 
Russo, D. and Van Roy, B. (2013). Eluder dimension and the sample complexity of 
optimistic exploration. In NIPS. Citeseer. 
Sallab, A. E., Abdou, M., Perot, E. and Yogamani, S. (2017). Deep reinforcement 
learning framework for autonomous driving. arXiv preprint arXiv:1704.02532 . 
Schulman, J., Levine, S., Abbeel, P., Jordan, M. and Moritz, P. (2015). Trust 
region policy optimization. In International conference on machine learning. PMLR. 
246
Schulman, J., Wolski, F., Dhariwal, P., Radford, A. and Klimov, O. (2017). 
Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 . 
Seo, Y., Chen, L., Shin, J., Lee, H., Abbeel, P. and Lee, K. (2021). State entropy 
maximization with random encoders for efficient exploration. In International Conference 
on Machine Learning. PMLR. 
Shalev-Shwartz, S. and Ben-David, S. (2014). Understanding machine learning: From 
theory to algorithms. Cambridge university press. 
Sharma, A., Gu, S., Levine, S., Kumar, V. and Hausman, K. (2019). Dynamics-aware 
unsupervised discovery of skills. arXiv preprint arXiv:1907.01657 . 
Sheng, H., Sun, J., Rodríguez, O., Hoar, B. B., Zhang, W., Xiang, D., Tang, T., 
Hazra, A., Min, D. S., Doyle, A. G. et al. (2024). Autonomous closed-loop mecha-
nistic investigation of molecular electrochemistry via automation. Nature Communications 
15 2781. 
Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driess-
che, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, 
M. et al. (2016). Mastering the game of go with deep neural networks and tree search. 
nature 529 484–489. 
Simchowitz, M. and Jamieson, K. G. (2019). Non-asymptotic gap-dependent regret 
bounds for tabular mdps. Advances in Neural Information Processing Systems 32 1153– 
1162. 
Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S. and Poole, 
B. (2020). Score-based generative modeling through stochastic differential equations. In 
International Conference on Learning Representations. 
247
Stooke, A., Lee, K., Abbeel, P. and Laskin, M. (2021). Decoupling representation 
learning from reinforcement learning. In International Conference on Machine Learning. 
PMLR. 
Sun, W., Jiang, N., Krishnamurthy, A., Agarwal, A. and Langford, J. (2019). 
Model-based rl in contextual decision processes: Pac bounds and exponential improve-
ments over model-free approaches. In Conference on Learning Theory. PMLR. 
Sutton, R. S., Barto, A. G. et al. (1998). Introduction to reinforcement learning. vol. 
135. 
Takemura, K., Ito, S., Hatano, D., Sumita, H., Fukunaga, T., Kakimura, N. 
and Kawarabayashi, K.-i. (2021). A parameter-free algorithm for misspecified linear 
contextual bandits. In International Conference on Artificial Intelligence and Statistics. 
PMLR. 
Tarbouriech, J., Zhou, R., Du, S. S., Pirotta, M., Valko, M. and Lazaric, A. 
(2021). Stochastic shortest path: Minimax, parameter-free and towards horizon-free regret. 
Advances in Neural Information Processing Systems 34 6843–6855. 
Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, 
T., Rozière, B., Goyal, N., Hambro, E., Azhar, F. et al. (2023). Llama: Open 
and efficient foundation language models. arXiv preprint arXiv:2302.13971 . 
Tunyasuvunakool, S., Muldal, A., Doron, Y., Liu, S., Bohez, S., Merel, J., 
Erez, T., Lillicrap, T., Heess, N. and Tassa, Y. (2020). dm control: Software and 
tasks for continuous control. Software Impacts 6 100022. 
Uehara, M., Zhang, X. and Sun, W. (2021). Representation learning for online and 
offline rl in low-rank mdps. arXiv preprint arXiv:2110.04652 . 
248
Van Roy, B. and Dong, S. (2019). Comments on the du-kakade-wang-yang lower bounds. 
arXiv preprint arXiv:1911.07910 . 
Vial, D., Parulekar, A., Shakkottai, S. and Srikant, R. (2022). Improved algorithms 
for misspecified linear markov decision processes. In International Conference on Artificial 
Intelligence and Statistics. PMLR. 
Vinyals, O., Babuschkin, I., Czarnecki, W. M., Mathieu, M., Dudzik, A., Chung, 
J., Choi, D. H., Powell, R., Ewalds, T., Georgiev, P. et al. (2019). Grandmaster 
level in starcraft ii using multi-agent reinforcement learning. Nature 575 350–354. 
Wagenmaker, A. J., Chen, Y., Simchowitz, M., Du, S. and Jamieson, K. (2022). 
Reward-free rl is no harder than reward-aware rl in linear markov decision processes. In 
International Conference on Machine Learning. PMLR. 
Wang, R., Du, S. S., Yang, L. F. and Kakade, S. M. (2020a). Is long horizon reinforce-
ment learning more difficult than short horizon reinforcement learning? arXiv preprint 
arXiv:2005.00527 . 
Wang, R., Du, S. S., Yang, L. F. and Salakhutdinov, R. (2020b). On reward-free 
reinforcement learning with linear function approximation. Advances in neural information 
processing systems . 
Wang, R., Salakhutdinov, R. R. and Yang, L. (2020c). Reinforcement learning with 
general value function approximation: Provably efficient approach via bounded eluder 
dimension. Advances in Neural Information Processing Systems 33 6123–6135. 
Wang, Y., Wang, R., Du, S. S. and Krishnamurthy, A. (2019). Optimism in reinforce-
ment learning with generalized linear function approximation. In International Conference 
on Learning Representations. 
249
Wei, C.-Y., Dann, C. and Zimmert, J. (2022). A model selection approach for corrup-
tion robust reinforcement learning. In International Conference on Algorithmic Learning 
Theory. PMLR. 
Weisz, G., Amortila, P. and Szepesvári, C. (2021). Exponential lower bounds for 
planning in mdps with linearly-realizable optimal action-value functions. In Algorithmic 
Learning Theory. PMLR. 
Wu, Y., Zhou, D. and Gu, Q. (2021). Nearly minimax optimal regret for learning 
infinite-horizon average-reward mdps with linear function approximation. arXiv preprint 
arXiv:2102.07301 . 
Yang, K., Yang, L. and Du, S. (2021). Q-learning with logarithmic regret. In International 
Conference on Artificial Intelligence and Statistics. PMLR. 
Yang, L. and Wang, M. (2019). Sample-optimal parametric q-learning using linearly 
additive features. In International Conference on Machine Learning. PMLR. 
Yang, L. and Wang, M. (2020a). Reinforcement learning in feature space: Matrix bandit, 
kernels, and regret bound. In International Conference on Machine Learning. PMLR. 
Yang, L. and Wang, M. (2020b). Reinforcement learning in feature space: Matrix bandit, 
kernels, and regret bound. In International Conference on Machine Learning. PMLR. 
Yarats, D., Fergus, R., Lazaric, A. and Pinto, L. (2021a). Reinforcement learn-
ing with prototypical representations. In International Conference on Machine Learning. 
PMLR. 
Yarats, D., Zhang, A., Kostrikov, I., Amos, B., Pineau, J. and Fergus, R. (2021b). 
Improving sample efficiency in model-free reinforcement learning from images. In Proceed-
ings of the AAAI Conference on Artificial Intelligence, vol. 35. 
250
Ye, C., Yang, R., Gu, Q. and Zhang, T. (2023). Corruption-robust offline reinforcement 
learning with general function approximation. arXiv preprint arXiv:2310.14550 . 
Zanette, A., Brandfonbrener, D., Brunskill, E., Pirotta, M. and Lazaric, A. 
(2020a). Frequentist regret bounds for randomized least-squares value iteration. In Inter-
national Conference on Artificial Intelligence and Statistics. 
Zanette, A., Lazaric, A., Kochenderfer, M. and Brunskill, E. (2020b). Learning 
near optimal policies with low inherent bellman error. In International Conference on 
Machine Learning. PMLR. 
Zanette, A., Lazaric, A., Kochenderfer, M. J. and Brunskill, E. (2020c). Learning 
near optimal policies with low inherent bellman error. In ICML. 
Zanette, A., Lazaric, A., Kochenderfer, M. J. and Brunskill, E. (2020d). Prov-
ably efficient reward-agnostic navigation with linear value iteration. Advances in Neural 
Information Processing Systems . 
Zhang, J., Zhang, W. and Gu, Q. (2023a). Optimal horizon-free reward-free exploration 
for linear mixture mdps. arXiv preprint arXiv:2303.10165 . 
Zhang, W., He, J., Fan, Z. and Gu, Q. (2023b). On the interplay between misspecification 
and sub-optimality gap: From linear contextual bandits to linear MDPs. 
Zhang, W., He, J., Fan, Z. and Gu, Q. (2023c). On the interplay between misspecification 
and sub-optimality gap in linear contextual bandits. arXiv preprint arXiv:2303.09390 . 
Zhang, W., He, J., Zhou, D., Zhang, A. and Gu, Q. (2021a). Provably efficient repre-
sentation learning in low-rank markov decision processes. arXiv preprint arXiv:2106.11935 
. 
251
Zhang, W., Zhou, D. and Gu, Q. (2021b). Reward-free model-based reinforcement learn-
ing with linear function approximation. Advances in Neural Information Processing Sys-
tems 34. 
Zhang, Z., Du, S. S. and Ji, X. (2020). Nearly minimax optimal reward-free reinforcement 
learning. arXiv preprint arXiv:2010.05901 . 
Zhang, Z., Ji, X. and Du, S. (2021c). Is reinforcement learning more difficult than bandits? 
a near-optimal algorithm escaping the curse of horizon. In Conference on Learning Theory. 
PMLR. 
Zhang, Z., Ji, X. and Du, S. (2022). Horizon-free reinforcement learning in polynomial 
time: the power of stationary policies. In Conference on Learning Theory. PMLR. 
Zhang, Z., Yang, J., Ji, X. and Du, S. S. (2021d). Improved variance-aware confidence 
sets for linear bandits and linear mixture mdp. Advances in Neural Information Processing 
Systems 34. 
Zhang, Z., Zhou, Y. and Ji, X. (2021e). Model-free reinforcement learning: from clipped 
pseudo-regret to sample complexity. In International Conference on Machine Learning. 
PMLR. 
Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J. and Huang, G. (2024). Expel: 
Llm agents are experiential learners. In Proceedings of the AAAI Conference on Artificial 
Intelligence, vol. 38. 
Zhao, H., He, J. and Gu, Q. (2023). A nearly optimal and low-switching algorithm for rein-
forcement learning with general function approximation. arXiv preprint arXiv:2311.15238 
. 
Zhou, D. and Gu, Q. (2022a). Computationally efficient horizon-free reinforcement learning 
for linear mixture mdps. arXiv preprint arXiv:2205.11507 . 
252
Zhou, D. and Gu, Q. (2022b). Computationally efficient horizon-free reinforcement learning 
for linear mixture mdps. arXiv preprint arXiv:2205.11507 . 
Zhou, D., Gu, Q. and Szepesvari, C. (2021a). Nearly minimax optimal reinforcement 
learning for linear mixture markov decision processes. In Conference on Learning Theory. 
PMLR. 
Zhou, D., Gu, Q. and Szepesvari, C. (2021b). Nearly minimax optimal reinforcement 
learning for linear mixture markov decision processes. In Conference on Learning Theory. 
PMLR. 
Zhou, D., He, J. and Gu, Q. (2021c). Provably efficient reinforcement learning for dis-
counted mdps with feature mapping. In International Conference on Machine Learning. 
PMLR. 
Zhou, D., He, J. and Gu, Q. (2021d). Provably efficient reinforcement learning for dis-
counted mdps with feature mapping. In International Conference on Machine Learning. 
PMLR. 
253