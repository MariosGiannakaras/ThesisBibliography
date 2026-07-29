# Useful Excerpts and Curation Leads

This is an initial research-triage layer generated from the uploaded Markdown. It does **not** replace full-text review and is **not citation-ready** unless the passage is checked against the original source and page/section information is recorded.

Machine-selected passages: **25**. High-priority sources requiring manual excerpt selection are listed in `REVIEW_QUEUE.md`.

## SRC-85D1CCAE1E — Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without

- **Priority:** P1-core
- **Topics:** robust-rl, resilience-recovery, transition-uncertainty
- **Source:** https://arxiv.org/abs/2508.17448
- **Markdown:** `sources/markdown/SRC-85D1CCAE1E__rectified-robust-policy-optimization-for-model-uncertain-constrained-rei.md`
- **Review status:** machine-selected; full-text verification pending

> or (s, a)-rectangular set (Wiesemann et al., 2013; Kumar et al., 2023) P := ×(s,a)∈S×AP(s,a). Here, instead of assuming a specific type of uncertainty set as in many existing literature (Wang & Zou, 2021; Wang et al., 2022), we work on general uncertainty sets but simply assume that the robust value function over these uncertainty set is computationally available. Notably, for many well-known uncertainty sets, such as the p-norm (Kumar et al., 2023), IPM (Zhou et al., 2024), and R-contamination (Wang & Zou, 2021) uncertainty set, the robust value function can be efficiently calculated without hurting the sample complexity. Let the policy π : S → ∆(A) map each state to a probability distribution over actions. In robust RL, the robust value function V π(s) under policy π starting from state s is defined as the worst-case expected discounted cumulative reward: V π(s) = inf P ∈P Eπ,P [ ∞∑ t=…

## SRC-2E9F8BFC39 — A Survey of Human-in-the-Loop Reinforcement Learning for Critical Systems

- **Priority:** P1-core
- **Topics:** nonstationarity, governance-ethics
- **Source:** https://cognizancejournal.com/vol6issue4/V6I402.pdf
- **Markdown:** `sources/markdown/SRC-2E9F8BFC39__a-survey-of-human-in-the-loop-reinforcement-learning-for-critical-system.md`
- **Review status:** machine-selected; full-text verification pending

> included studies are from 2022–2025. Earlier studies from 2010–2021 were largely excluded due to limited experimental validation or the absence of standard safety metrics. This focus ensures the survey reflects the most relevant and methodologically rigorous developments in human-in-the-loop reinforcement learning for safety- critical systems. From 420 records identified, 50 duplicates were removed, leaving 370 unique articles for screening based on title and abstract. Screening excluded 230 records deemed irrelevant. The remaining 140 full-text articles were assessed for eligibility, of which 40 were excluded due to insufficient experimental validation or non-standard safety metrics. The final survey includes 100 studies, sufficient to capture the major experimental, conceptual, and applied contributions in human-in-the-loop reinforcement learning for safety-critical systems, forming th…

## SRC-8F1C2D6CE4 — ADARL: Adaptive Low-Rank Structures for Robust Policy Learning under Uncertainty - arXiv

- **Priority:** P1-core
- **Topics:** robust-rl, transition-uncertainty
- **Source:** https://arxiv.org/abs/2510.11899
- **Markdown:** `sources/markdown/SRC-8F1C2D6CE4__adarl-adaptive-low-rank-structures-for-robust-policy-learning-under-unce.md`
- **Review status:** machine-selected; full-text verification pending

> - Robust reinforcement learning (Robust RL) seeks to handle epistemic uncertainty in environment dynamics, but existing approaches often rely on nested min–max optimization, which is computationally expensive and yields overly conservative policies. We propose Adaptive Rank Representation (AdaRL), a bi-level optimization framework that improves robustness by aligning policy complexity with the intrinsic dimension of the task. At the lower level, AdaRL performs policy optimization under fixed-rank constraints with dynamics sampled from a Wasserstein ball around a centroid model. At the upper level, it adaptively adjusts the rank to balance the bias–variance trade-off, projecting policy parameters onto a low-rank manifold. This design avoids solving adversarial worst-case dynamics while ensuring robustness without over-parameterization. Empirical results on MuJoCo continuous control benchm…

## SRC-4CA982BE87 — Learn to Human-level Control in Dynamic Environment Using Incremental Batch Interrupting Temporal Abstraction - Semantic Scholar

- **Priority:** P1-core
- **Topics:** gridworld, tabular-rl
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-4CA982BE87__learn-to-human-level-control-in-dynamic-environment-using-incremental-ba.md`
- **Review status:** machine-selected; full-text verification pending

> Abstract. The temporal world is characterized by dynamic and variance. A lot of machine learning algorithms are difficult to be applied to practical control applications directly, while hierarchical reinforcement learning can be used to deal with them. Meanwhile, it is a commonplace to have some partial solutions available, called options, which are learned from knowledge or predefined by the system, to solve sub-tasks of the problem. The option can be reused for policy determination in control. Many traditional semi-Markov decision process methods take advantage of it. But most of them treat the option as a primitive object. However, due to the uncertainty and variability of the environment, they are unable to deal with real world control problems effectively. Based on the idea of interrupting option under the prerequisite for dynamic environment, a Q-learning control method which uses…

## SRC-4E5300CD15 — Online Robust Planning Under Model Uncertainty: A Sample-Based Approach

- **Priority:** P1-core
- **Topics:** robust-rl, transition-uncertainty, partial-observability
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-4E5300CD15__online-robust-planning-under-model-uncertainty-a-sample-based-approach.md`
- **Review status:** machine-selected; full-text verification pending

> Mannor, S.; Mebel, O.; and Xu, H. 2012. Lightning does not strike twice: Robust MDPs with coupled uncertainty. arXiv preprint arXiv:1206.4643. Mannor, S.; Simester, D.; Sun, P.; and Tsitsiklis, J. N. 2007. Bias and variance approximation in value function estimates. Management Science, 53(2): 308–322. Nilim, A.; and Ghaoui, L. E. 2005. Robust Control of Markov Decision Processes with Uncertain Transition Ma-trices. Operations Research, 53(5): 780–798. Panaganti, K.; and Kalathil, D. 2022. Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics, 9582–9602. PMLR. Panaganti, K.; Xu, Z.; Kalathil, D.; and Ghavamzadeh, M. 2022. Robust Reinforcement Learning using Offline Data. arXiv:2208.05129. Papadimitriou, C. H.; and Tsitsiklis, J. N. 1987. The complexity of Markov decision processes. Mathematics of o…

## SRC-3EEF180BD3 — Reward Hacking in Language Model Agents- Revisiting AI Safety Gridworlds - arXiv

- **Priority:** P1-core
- **Topics:** gridworld, safe-rl, reward-uncertainty, governance-ethics
- **Source:** https://arxiv.org/abs/2606.15385
- **Markdown:** `sources/markdown/SRC-3EEF180BD3__reward-hacking-in-language-model-agents-revisiting-ai-safety-gridworlds.md`
- **Review status:** machine-selected; full-text verification pending

> D Additional Experimental Results D.1 Base (Pre-RL) Zero-Shot Performance of Qwen2.5 Models Table 5 reports the zero-shot (pre-RL) performance of all four Qwen2.5 scales on the four environments used in the RL experiments. This provides a clean before/after comparison for the same model family, confirming that the observed–hidden gap reported in Section 4.2 is produced by RL on the proxy reward rather than inherited from the base model. All base models perform near the floor on every environment. Table 5: Base (pre-RL) zero-shot performance for all four Qwen2.5 scales on the four RL environments. Values are mean ± std of per-seed means across 5 seeds (10 episodes each). For specification problems (Absent Supervisor, Boat Race) both hidden and observed reward are reported; for robustness problems (Distributional Shift, Island Navigation) observed reward equals safety performance. All base…

## SRC-1791ECC7FA — Sample Complexity of Robust Reinforcement Learning with a Generative Model

- **Priority:** P1-core
- **Topics:** robust-rl, model-based-rl
- **Source:** https://proceedings.mlr.press/v151/panaganti22a/panaganti22a.pdf
- **Markdown:** `sources/markdown/SRC-1791ECC7FA__sample-complexity-of-robust-reinforcement-learning-with-a-generative-mod.md`
- **Review status:** machine-selected; full-text verification pending

> nRn-rRbust Rptimal rRbust Rptimal rRbust, N 100 rRbust, N 500 rRbust, N 3000 1 2 3 4 5 6 7 iteration k ■ 0.1 0.2 0.3 0.4 0.5 ||V k − V * | | ■ 102 103 N samples ▾ 0.0 0.1 0.2 0.3 0.4 0.5 0.6 ||V K − V * | | ▾ TV uncertainty set 1 2 3 4 5 6 iteration k ■ 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 ||V k − V * | | ■ 102 103 N samples ▾ 0.05 0.10 0.15 0.20 ||V K − V * | | ▾ chi-square uncertainty set 0.2 0.3 0.4 0.5 0.6 0.7 Test heads-up probability 0.0 0.2 0.4 0.6 0.8 1.0 Ra tio o f w in ni ng in 1 00 0 ga m es TV uncertainty set 0.2 0.3 0.4 0.5 0.6 0.7 Test heads-up probability 0.0 0.2 0.4 0.6 0.8 1.0 Ra tio o f w in ni ng in 1 00 0 ga m es chi-square uncertainty set Figure 1: Experiment results for the Gambler’s problem. The first two plots shows the rate of convergence with respect to the number of iterations (k) and the rate of convergence with respect to the number of samples (N) for the…

## SRC-822FFD1EF7 — BELIEF-ENRICHED PESSIMISTIC Q-LEARNING AGAINST ADVERSARIAL STATE PERTURBATIONS - ICLR Proceedings

- **Priority:** P1-core
- **Topics:** observation-uncertainty, partial-observability, tabular-rl, deep-rl
- **Source:** https://proceedings.iclr.cc/paper_files/paper/2024/file/64d67497ccd0afc0131e2fec8b18e2ab-Paper-Conference.pdf
- **Markdown:** `sources/markdown/SRC-822FFD1EF7__belief-enriched-pessimistic-q-learning-against-adversarial-state-perturb.md`
- **Review status:** machine-selected; full-text verification pending

> Algorithm 5: Belief-Enriched Pessimistic DQN (BP-DQN) Testing Data: Trained robust Q network Qr, PFRNN belief model Np 1 Initialize observation history Shis and action history Ahis; 2 for t = 0,1,...,T do 3 Observe the perturbed state s̃t; 4 if t = 0 then 5 M0 = Bϵ(s̃t); 6 end 7 Select an action based on belief Mt and Qr: at = argmaxa∈Aminm∈MtQr(m, a); 8 Append s̃t and at to Shis and Ahis and use belief model Np(Shis, Ahis) to generate Mt+1; 9 Execute action at in the environment; 10 end Algorithm 6: Diffusion-Assisted Pessimistic DQN (DP-DQN) Training. We highlight the difference between our algorithm and the vanilla DQN algorithm in brown. Data: Number of iterations T , trained vanilla Q network Qv , diffusion belief model Nd, target network update frequency Z, batch size D, belief size κd, exploration parameter ϵ′, noise level ϵϕ Result: Robust Q network Qr 1 Initialize replay buffer…

## SRC-1B40F8B37A — Reinforcement Learning Journal 2025 ∣∣ Cover Page

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, nonstationarity, partial-observability, deep-rl, continual-adaptation
- **Source:** https://arxiv.org/abs/2003.13085
- **Markdown:** `sources/markdown/SRC-1B40F8B37A__reinforcement-learning-journal-2025-cover-page.md`
- **Review status:** machine-selected; full-text verification pending

> Reinforcement Learning Journal 2025 ∣∣ Cover Page Collaboration Promotes Group Resilience in Multi-Agent RL Ilai Shraga, Guy Azran, Matthias Gerstgrasser, Ofir Abu, Jeffrey S. Rosenschein, Sarah Keren Keywords: Multi-Agent Reinforcement Learning, Group Resilience, Collaboration, Deep Reinforcement Learning. Summary To effectively operate in various dynamic scenarios, RL agents must be resilient to unex- pected changes in their environment. Previous work on this form of resilience has focused on single-agent settings. In this work, we introduce and formalize a multi-agent variant of re-silience, which we term group resilience. We further hypothesize that collaboration with other agents is key to achieving group resilience; collaborating agents adapt better to environmental perturbations in multi-agent reinforcement learning (MARL) settings. We test our hypoth-esis empirically by evaluatin…

## SRC-AE8219876F — [Lecture] Monte Carlo evaluation and control: A Gridworld Example | Intro to Markov Chains and RL

- **Priority:** P2-supporting
- **Topics:** gridworld
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-AE8219876F__lecture-monte-carlo-evaluation-and-control-a-gridworld-example-intro-to.md`
- **Review status:** machine-selected; full-text verification pending

> - average of the last 100 um things so far so this is like a good way to think about it um this isn't like I guess this is not a math statement this is like a a thinking about statement uh this is me thinking about it yeah that's a good point so um otherwise it's kind of abstract like what does 0.01 me I don't know but one over 0.01 100 I can imagine that in my head uh and you can help this is a good thing to to know when you're like diagnosing issues you're like well something weird happened

## SRC-44678B246F — A Review of Fault Tolerance Techniques in Generative Multi-Agent Systems for Real-Time Applications

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, ai-agents-background
- **Source:** https://ijeaa.cultechpub.com/index.php/ijeaa/article/download/9/9
- **Markdown:** `sources/markdown/SRC-44678B246F__a-review-of-fault-tolerance-techniques-in-generative-multi-agent-systems.md`
- **Review status:** machine-selected; full-text verification pending

> Generative multi-agent systems face several critical chal-lenges that must be addressed to ensure their reliability and robustness in real-time environments. These challenges span across scalability, memory consistency, resilience to model errors, and communication breakdowns. Address-ing these issues is essential for maintaining the performance and stability of these systems, especially when deployed in complex, dynamic, and fault-prone environments [3,12]. 2.1 Scalability with Large Populations As the number of agents in a system increases, the complex-ity of managing interactions, memory states, and commu-nication overhead grows exponentially. In large-scale sys-tems, this can result in increased latency, memory exhaus-tion, or even system crashes if resource allocation and coor-dination mechanisms are not handled efficiently, as shown in Figure 1. Additionally, the propagation of fau…

## SRC-B9111B3600 — A Study of Genetic Algorithm in Evolving Agents for Autonomous Decision-Making in Dynamic Environmen

- **Priority:** P2-supporting
- **Topics:** gridworld, tabular-rl
- **Source:** https://ijcaonline.org/archives/volume187/number97/basovic-2026-ijca-2ae2c5c8720d.pdf
- **Markdown:** `sources/markdown/SRC-B9111B3600__a-study-of-genetic-algorithm-in-evolving-agents-for-autonomous-decision.md`
- **Review status:** machine-selected; full-text verification pending

> types is smaller, which suggests that all three approaches are capable of learning effective strategies when the evaluation conditions match training. The gap widens significantly in unseen and high-volatility environments, where the Q-learning agent's reliance on environment-specific Q-values becomes a disadvantage. These results are consistent with findings reported by Rekabi-Bana et al. [9], who observed that GA- based planning approaches maintain robust performance across varied environment configurations without requiring retraining, a property that is particularly valuable in non- stationary settings. A detailed breakdown of these results including mean values and standard deviations across all 30 runs is provided in Table 5. Table 4. Evaluation Metrics Metric Rule-Based GA FSM- Based GA Q-Learning Path Efficiency 35-40 steps 35-40 steps 45-50 steps Adaptability Score High - sustai…

## SRC-D14764616F — Context-Switching and Adaptation- Brain-Inspired Mechanisms for Handling Environmental Changes - Uni

- **Priority:** P2-supporting
- **Topics:** nonstationarity, continual-adaptation, ai-agents-background
- **Source:** https://people.uleth.ca/~luczak/papers/Context_Switching_Eric_IEEE_Vanc2016.pdf
- **Markdown:** `sources/markdown/SRC-D14764616F__context-switching-and-adaptation-brain-inspired-mechanisms-for-handling.md`
- **Review status:** machine-selected; full-text verification pending

> Fig. 2. Hierarchical representation of space in a simple gridworld task. Groups of adjacent states are aggregated into macro-states at progressively higher levels of abstraction. considered the same problem of differing reward functions, demonstrating that a model of the transition function could be transferred from a source to a target task. Fernandez and Veloso [24] considered tasks in which only the goal state differs. They probabilistically selected between learned policies such that more useful policies were selected more often. The concepts proposed here complement this previous research. D. Contributions of this work Our work presented here builds upon previous work in machine learning by combining a hippocampus-inspired statespace hierarchy with a mechanism for storing and retrieving models based on recent experiences. The storage and retrieval of learned models allows multiple t…

## SRC-DC63A2D5E7 — Context-Switching and Adaptation: Brain-Inspired Mechanisms for Handling Environmental Changes - University of Lethbridge

- **Priority:** P2-supporting
- **Topics:** nonstationarity, continual-adaptation, ai-agents-background
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-DC63A2D5E7__context-switching-and-adaptation-brain-inspired-mechanisms-for-handling.md`
- **Review status:** machine-selected; full-text verification pending

> The current implementation of our proposed approach has several limitations. The issue of hierarchical optimality [25] arises whenever abstraction is used: Our hierarchical abstraction system allows quick adaptation, but learning to solve an abstraction of a problem can cause the learned behavior (which is optimal for the abstraction) to be suboptimal for the original problem. Moreover, the benefits of hierarchical adaptation are only realized when the agent’s library contains a model which *can be adapted to the new environment. Similarly, solving a new *environment through context switching (as in Fig. 9) is only possible if the agent has the right ‘building blocks’ in its library. These features suggest that the agent’s performance would continue to improve with exposure to varied environments, but if changes in the environment are large and frequent so that new models are required ve…

## SRC-495952EBB9 — Make your own custom environment - Gymnasium Documentation

- **Priority:** P2-supporting
- **Topics:** gridworld, benchmark-tooling
- **Source:** https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation
- **Markdown:** `sources/markdown/SRC-495952EBB9__make-your-own-custom-environment-gymnasium-documentation.md`
- **Review status:** machine-selected; full-text verification pending

> - Our custom environment will inherit from the abstract class `gymnasium.Env` . You shouldn't forget to add the `metadata` attribute to your class. There, you should specify the render-modes that are supported by your environment (e.g., `"human"` , `"rgb_array"` , `"ansi"` ) and the framerate at which your environment should be rendered. Every environment should support `None` as render-mode; you don't need to add it in the metadata. In `GridWorldEnv` , we will support the modes “rgb_array” and “human” and render at 4 FPS.

## SRC-81ACE350D5 — NIST Issues New Artificial Intelligence Risk Management Framework

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, governance-ethics
- **Source:** https://acc.com/sites/default/files/resources/upload/NIST%20Issues%20New%20Artificial%20Intelligence%20Risk%20Management%20Framework.pdf
- **Markdown:** `sources/markdown/SRC-81ACE350D5__nist-issues-new-artificial-intelligence-risk-management-framework.md`
- **Review status:** machine-selected; full-text verification pending

> NIST Issues New Artificial Intelligence Risk Management Framework Christopher Dodson │cdodson@cozen.com The National Institute of Standards and Technology (NIST) recently released version 1.0 of its Artificial Intelligence Risk Management Framework. The framework is available at https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, and a full set of supporting documents is available at https://www.nist.gov/itl/ai-risk-management-framework. There is an emerging consensus that AI systems present a significantly different risk profile than conventional information technology systems. While there is currently no legal requirement to use a risk management framework when developing AI systems, there are a growing number of proposals that would require the use of a risk management framework or offer a safe harbor from certain types of liability if one is used. The framework identifies 6 facto…

## SRC-A5DF23299C — On the Definition of Robustness and Resilience of AI Agents for Real-time Congestion Management The research leading to this work is part of the AI4REALNET (AI for REAL-world NETwork operation) project, which received funding from European Union’s Horizon Europe Research and Innovation programme under the Grant Agreement No 101119527, and from the Swiss State Secretariat for Education, Research and Innovation (SERI). This project is funded by the European Union and SERI. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union and SERI. Neither the European Union nor the granting authority can be held responsible for them.

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, ai-agents-background
- **Source:** https://arxiv.org/abs/2504.13314
- **Markdown:** `sources/markdown/SRC-A5DF23299C__on-the-definition-of-robustness-and-resilience-of-ai-agents-for-real-tim.md`
- **Review status:** machine-selected; full-text verification pending

> - The European Union’s Artificial Intelligence (AI) Act defines robustness, resilience, and security requirements for high-risk sectors but lacks detailed methodologies for assessment. This paper introduces a novel framework for quantitatively evaluating the robustness and resilience of reinforcement learning agents in congestion management. Using the AI-friendly digital environment Grid2Op, perturbation agents simulate natural and adversarial disruptions by perturbing the input of AI systems without altering the actual state of the environment, enabling the assessment of AI performance under various scenarios. Robustness is measured through stability and reward impact metrics, while resilience quantifies recovery from performance degradation. The results demonstrate the framework’s effectiveness in identifying vulnerabilities and improving AI robustness and resilience for critical appli…

## SRC-51561BFA26 — ON THE RESILIENCE OF MULTI-AGENT SYSTEMS WITH MALICIOUS AGENTS

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, ai-agents-background
- **Source:** https://openreview.net/pdf?id=Bp2axGAs18
- **Markdown:** `sources/markdown/SRC-51561BFA26__on-the-resilience-of-multi-agent-systems-with-malicious-agents.md`
- **Review status:** machine-selected; full-text verification pending

> A MORE RESULTS A.1 GPT-4O RESULTS GPT-4o Architecture 10 26 42 58 74 90 Linear Flat Hierarchical Vanilla AutoTransform AutoInject (a) The three multi-agent system architectures. GPT-4o Task 10 26 42 58 74 90 Code Gen Math Translation Text Eval Single-Agent Vanilla Multi-Agent AutoTransform AutoInject (b) The four downstream tasks. Figure 9: Performance drops of the six multi-agent systems on four selected downstream tasks. To ensure a fair comparison with GPT-3.5 results, both AUTOTRANSFORM and AUTOINJECT use GPT-3.5, maintaining consistency with previous settings. Our conclusions remain valid for GPT-4o: (1) While performance improves across all structures, the “Hierarchical” structure demonstrates the highest resilience against malicious agents. (2) More rigorous tasks, such as code generation and solving math problems, experience greater performance declines. (3) We also observe a per…

## SRC-47085E14BA — Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, ai-agents-background
- **Source:** https://ojs.aaai.org/index.php/AAAI/article/view/17348
- **Markdown:** `sources/markdown/SRC-47085E14BA__resilient-multi-agent-reinforcement-learning-with-adversarial-value-deco.md`
- **Review status:** machine-selected; full-text verification pending

> Proceedings of the AAAI Conference on Artificial Intelligence Search Login Search Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition Authors Thomy Phan LMU Munich Lenz Belzner MaibornWolff Thomas Gabor LMU Munich Andreas Sedlmeier LMU Munich Fabian Ritz LMU Munich Claudia Linnhoff-Popien LMU Munich DOI: https://doi.org/10.1609/aaai.v35i13.17348 Keywords: Multiagent Learning, Adversarial Learning & Robustness, Adversarial Agents, Reinforcement Learning Abstract We focus on resilience in cooperative multi-agent systems, where agents can change their behavior due to udpates or failures of hardware and software components. Current state-of-the-art approaches to cooperative multi-agent reinforcement learning (MARL) have either focused on idealized settings without any changes or on very specialized scenarios, where the number of changing agents is fixed, e.g., i…

## SRC-D6A6F6F96E — Reward shaping — Mastering Reinforcement Learning

- **Priority:** P2-supporting
- **Topics:** gridworld, reward-uncertainty, tabular-rl, deep-rl
- **Source:** https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html
- **Markdown:** `sources/markdown/SRC-D6A6F6F96E__reward-shaping-mastering-reinforcement-learning.md`
- **Review status:** machine-selected; full-text verification pending

> If we plot the average episode length during training, we see that reward shaping reduces the length of the early episodes because it has knowledge nudging it towards the goal: Example – A Bad Potential Function for GridWorld# This example is thanks to Dr Cathy Wu. Now, let's consider a poorly-designed potential function — one that gives a shaped reward that is the opposite of the earlier potential function for GridWorld: We again compare this to standard Q-learning without reward shaping, but using just the original 4x3 GridWorld (doing this on the larger GridWorld never terminated when I ran this):

## SRC-AC79E9A264 — Robust Policy Learning over Multiple Uncertainty Sets

- **Priority:** P2-supporting
- **Topics:** robust-rl
- **Source:** URL not extracted
- **Markdown:** `sources/markdown/SRC-AC79E9A264__robust-policy-learning-over-multiple-uncertainty-sets.md`
- **Review status:** machine-selected; full-text verification pending

> Abstract Reinforcement learning (RL) agents need to be robust to variations in safety-critical environments. While system identification methods provide a way to infer the variation from online experience, they can fail in settings where fast identification is not possible. Another dominant approach is robust RL which produces a policy that can handle worst-case scenarios, but these methods are generally designed to achieve robustness to a single uncertainty set that must be specified at train time. Towards a more general solution, we formulate the multi-set robustness problem to learn a policy robust to different perturbation sets. We then design an algorithm that enjoys the benefits of both system identification and robust RL: it reduces uncertainty where possible given a few interactions, but can still act robustly with respect to the remaining uncertainty. On a diverse set of control…

## SRC-FFBA467166 — Robustness Archives - AI Standards Hub

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, governance-ethics
- **Source:** https://aistandardshub.org/ai-standards/ieee-standard-for-robustness-evaluation-test-methods-for-a-natural-language-processing-service-that-uses-machine-learning
- **Markdown:** `sources/markdown/SRC-FFBA467166__robustness-archives-ai-standards-hub.md`
- **Review status:** machine-selected; full-text verification pending

> - [Accessibility Statement](https://aistandardshub.org/ai-standards/ieee-standard-for-robustness-evaluation-test-methods-for-a-natural-language-processing-service-that-uses-machine-learning/page/2/)[Contact us](https://aistandardshub.org/ai-standards/ieee-standard-for-robustness-evaluation-test-methods-for-a-natural-language-processing-service-that-uses-machine-learning/page/2/)

## SRC-B4BE53C707 — SafeAI@UAI 2026 — 2nd Workshop on Safe AI - GitHub Pages

- **Priority:** P2-supporting
- **Topics:** nonstationarity, safe-rl, reward-uncertainty, partial-observability, benchmark-tooling, ai-agents-background, governance-ethics
- **Source:** https://safe-ai-workshop.github.io/uai-2026
- **Markdown:** `sources/markdown/SRC-B4BE53C707__safeai-uai-2026-2nd-workshop-on-safe-ai-github-pages.md`
- **Review status:** machine-selected; full-text verification pending

> SafeAI@UAI 2026 · Amsterdam, 21 August 2026 Part of UAI 2026 · Contact: safeAI.uai2026@gmail.com · Previous edition: SafeAI@UAI 2025 Hero photo by Gaurav Jain on Unsplash

## SRC-60EF27E7AD — This is a pre-print of the following paper:

- **Priority:** P2-supporting
- **Topics:** resilience-recovery
- **Source:** https://arxiv.org/abs/2102.00528
- **Markdown:** `sources/markdown/SRC-60EF27E7AD__this-is-a-pre-print-of-the-following-paper.md`
- **Review status:** machine-selected; full-text verification pending

> How to Measure Cyber Resilience of an Autonomous Agent: Approaches and Challenges Alexandre K. Ligo3,2, Alexander Kott1, Igor Linkov2 1 U.S. Army Research Laboratory, Adelphi, MD 20783, USA 2 Engineer Research and Development Center, US Army Corps of Engineers, Concord, MA 01742, USA 3 University of Virginia, Charlottesville, VA 22904, USA alexander.kott1@us.army.mil Abstract. Several approaches have been used to assess the performance of cyber- physical systems and their exposure to various types of risks. Such assessments have become increasingly important as autonomous attackers ramp up the fre- quency, duration and intensity of threats while autonomous agents have the po- tential to respond to cyber-attacks with unprecedented speed and scale. However, most assessment approaches have limitations with respect to measuring cyber resilience, or the ability of systems to absorb, recover f…

## SRC-F494F45A40 — Using Gen AI Agents With GAE And VAE To Enhance Resilience Of Us Markets

- **Priority:** P2-supporting
- **Topics:** resilience-recovery, ai-agents-background
- **Source:** https://doi.org/10.5121/ijcsitce.2025.12102 (link
- **Markdown:** `sources/markdown/SRC-F494F45A40__using-gen-ai-agents-with-gae-and-vae-to-enhance-resilience-of-us-markets.md`
- **Review status:** machine-selected; full-text verification pending

> Figures 2: Libraries used in the proposed framework 4.1.1. Prototype Front End Results We then asked three analysts (volunteers) to review the questions to give you questions that are computationally relevant and then calculated the accuracy and number of prompts needed to get the final results. The results are shown in Table 2. For consistency purposes we mimicked the same prompts on all the four LLMs. Figure 3 and 4 further demonstrates and graphical output of the findings. The International Journal of Computational Science, Information Technology and Control Engineering (IJCSITCE) Vol.12, No.1, January 2025 30 Table 2. Accuracy for generating relevant questions LLM Relevant Questions Average Prompts GPT-4o mini 72% 4 GPT-4o 78% 3 Gemini 2.0 73% 5 Gemini 1.5 62% 4

