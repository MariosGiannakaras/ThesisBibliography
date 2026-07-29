# Forgetting as Control: A Theoretical Framework for Selective Behavioral Erasure in Post-Deployment Reinforcement Learning Agents - Preprints.org

- Forgetting as Control: A Theoretical Framework for Selective Behavioral Erasure in Post-Deployment Reinforcement Learning Agents[v1] | Preprints.org

- Loading [MathJax]/jax/element/mml/optable/GreekAndCoptic.js

- [Instructions for Authors](https://www.preprints.org/instructions-for-authors)

- [About](https://www.preprints.org/about)

- [Help Center](https://www.preprints.org/help-center)

- [Blog](https://www.preprints.org/blog)

- [10th Anniversary](https://www.preprints.org/activity/10th-anniversary-2026)

- [Author Services](https://www.preprints.org/author-services)

- Log In

- [Submit](https://www.preprints.org/user/submission/new)

Celebrate 10 Years of Open Sharing [Explore All Events](https://www.preprints.org/activity/10th-anniversary-2026)

- [Home](https://www.preprints.org/)

- [Computer Science and Mathematics](https://www.preprints.org/subject/browse/computer-science-and-mathematics)

- [Artificial Intelligence and Machine Learning](https://www.preprints.org/subject/browse/computer-science-and-mathematics/artificial-intelligence-and-machine-learning)

- [DOI:10.20944/preprints202606.0911.v1](https://www.preprints.org/manuscript/202606.0911)

- Cite

- Add to My List

- Share Comments

- Download PDF

- Version 1

- Submitted:

- 10 June 2026

- Posted:

- 11 June 2026

- You are already at the latest version

- Subscription

- Notify me about updates to this article or when a peer-reviewed version is published.

- Subscribe

- [1. Introduction](https://www.preprints.org/manuscript/202606.0911#Introduction)

- [2. Related Work](https://www.preprints.org/manuscript/202606.0911#Related_Work)

- [3. Problem Formulation](https://www.preprints.org/manuscript/202606.0911#Problem_Formulation)

- [4. Proposed Framework: Forgetting Systems](https://www.preprints.org/manuscript/202606.0911#Proposed_Framework_Forgetting_Systems)

- [5. Discussion](https://www.preprints.org/manuscript/202606.0911#Discussion)

- [6. Conclusions](https://www.preprints.org/manuscript/202606.0911#Conclusions)

- [References](https://www.preprints.org/manuscript/202606.0911#References)

- Preprint

- Article

- This version is not peer-reviewed.

# Forgetting as Control: A Theoretical Framework for Selective Behavioral Erasure in Post-Deployment Reinforcement Learning Agents

- [Mehdi Samieiyeganeh](https://sciprofiles.com/profile/5340741) *

- , [Parisa Bahraminikoo](https://sciprofiles.com/profile/5429180), [Soobia Saeed](https://sciprofiles.com/profile/5423914), [Saraswathy Gunasekaran](https://sciprofiles.com/profile/5375158)

- , [Saadat Ahmed](https://sciprofiles.com/profile/5426313)

- [Mehdi Samieiyeganeh](https://sciprofiles.com/profile/5340741) *

- , [Parisa Bahraminikoo](https://sciprofiles.com/profile/5429180), [Soobia Saeed](https://sciprofiles.com/profile/5423914), [Saraswathy Gunasekaran](https://sciprofiles.com/profile/5375158)

- , [Saadat Ahmed](https://sciprofiles.com/profile/5426313)

- Show more

- Version 1

- Submitted:

- 10 June 2026

- Posted:

- 11 June 2026

- You are already at the latest version

Abstract

- Deployed Reinforcement Learning (RL) agents may acquire, reinforce, or exhibit harmful behaviors after being released into real-world environments, yet current methods provide no dedicated mechanism for suppressing such behaviors during operation. Machine Unlearning (MU) and continual learning have made important contributions to memory management in Neural Networks (NNs), but they are primarily concerned with removing data-level influence or preserving previously acquired knowledge. Neither approach directly addresses harmful behavioral patterns that emerge after deployment through continued interaction with the environment. This paper proposes Forgetting Systems, a theoretical framework that treats post-deployment behavioral forgetting as a largely unaddressed problem in Reinforcement Learning. The core idea is that a deployed RL agent should be able to selectively and gradually suppress harmful behaviors during operation, without requiring offline retraining or model-level intervention. To determine when suppression is warranted, the framework defines a three-signal Forgetting Trigger that activates only when a behavior simultaneously produces negative reward, moves the agent away from its intended goal, and recurs across multiple interactions. Together, these conditions distinguish persistent harmful patterns from isolated errors that do not require intervention. The forgetting process is governed by an exponential decay function inspired by the Ebbinghaus model of human memory, allowing the degree of forgetting to be proportional to the severity and frequency of undesirable behavior. The framework supports three operational modes, human-initiated, autonomous, and hybrid, each suited to different trade-offs between response latency and human oversight. A Relearning Mechanism ensures that suppression is not permanent: if previously suppressed behavior becomes beneficial under changed environmental conditions, the agent can recover it through positive reinforcement. When forgetting fails and harmful behavior persists despite repeated suppression, a Termination Condition mandates controlled shutdown rather than continued unsafe operation. The broader argument of this paper is that forgetting should not be treated only as a defect to be avoided. When deliberately designed, it can function as a controllability mechanism that helps keep autonomous systems within boundaries that human operators can still supervise, correct, and safely terminate.

Keywords:

- machine unlearning

- ;

- reinforcement learning

- ;

- deep reinforcement learning

- ;

- AI safety

- ;

- controllability

- ;

- forgetting systems

- ;

- post-deployment learning

- ;

- behavioral suppression

Subject:

- [Computer Science and Mathematics](https://www.preprints.org/subject/browse/computer-science-and-mathematics) - [Artificial Intelligence and Machine Learning](https://www.preprints.org/subject/browse/computer-science-and-mathematics/artificial-intelligence-and-machine-learning)

## 1. Introduction

- AI systems based on deep reinforcement learning have demonstrated remarkable capabilities across a wide range of domains, from robotic control to complex strategic decision-making [ [1](https://www.preprints.org/manuscript/202606.0911#B1-preprints-217886), [2](https://www.preprints.org/manuscript/202606.0911#B2-preprints-217886), [3](https://www.preprints.org/manuscript/202606.0911#B3-preprints-217886)]. Yet as these systems move from controlled training environments into real-world deployment, a fundamental problem becomes increasingly apparent: once a model is trained and released, its learned behaviors often remain difficult to modify during operation. Correcting harmful or undesirable behavior may require full retraining, offline fine-tuning, or external intervention, none of which is practical when unsafe behavior needs to be addressed while the system is still running.

- Human cognition suggests a different way of thinking about this problem. The brain does not retain all experiences with equal weight. Some harmful behavioral tendencies can be suppressed, some undesirable habits weaken over time, and some memories gradually lose their intensity. This capacity for selective forgetting is not simply a cognitive weakness. It is an adaptive mechanism that helps humans adjust, recover, and continue functioning in environments that are dynamic and often unpredictable. A mind that could not forget would eventually be overwhelmed by the accumulated weight of every harmful experience it had ever encountered. The absence of an analogous mechanism in deployed AI systems is therefore not a minor technical gap. It is a structural limitation in how we maintain control over autonomous systems once they leave the lab.

- Existing approaches only partially address this limitation. Machine unlearning has made genuine progress in removing the influence of specific data points from trained models, driven largely by data privacy and regulatory requirements [ [4](https://www.preprints.org/manuscript/202606.0911#B4-preprints-217886), [5](https://www.preprints.org/manuscript/202606.0911#B5-preprints-217886), [6](https://www.preprints.org/manuscript/202606.0911#B6-preprints-217886)]. Continual learning methods have addressed catastrophic forgetting by focusing on how a model can incorporate new knowledge without losing what it has previously learned [ [7](https://www.preprints.org/manuscript/202606.0911#B7-preprints-217886), [8](https://www.preprints.org/manuscript/202606.0911#B8-preprints-217886), [9](https://www.preprints.org/manuscript/202606.0911#B9-preprints-217886), [10](https://www.preprints.org/manuscript/202606.0911#B10-preprints-217886), [11](https://www.preprints.org/manuscript/202606.0911#B11-preprints-217886), [12](https://www.preprints.org/manuscript/202606.0911#B12-preprints-217886)]. Reinforcement learning from human feedback has enabled behavioral correction through reward shaping and preference-based guidance [ [13](https://www.preprints.org/manuscript/202606.0911#B13-preprints-217886), [14](https://www.preprints.org/manuscript/202606.0911#B14-preprints-217886)]. Each of these represents a real contribution to the broader problem of managing learned behavior in neural systems. None of them, however, provides a dedicated real-time mechanism for suppressing harmful behavioral patterns in an agent that is already deployed and actively interacting with the world.

- This gap creates a window of uncorrected behavior that grows more consequential as AI systems become more capable and more widely used. A deployed agent that acquires harmful behavior through environmental interaction cannot always be corrected immediately through existing mechanisms. In time-critical applications, the cost of retraining may be prohibitive. More importantly, a system with no internal pathway for behavioral correction leaves external intervention or complete shutdown as the only available safety options when persistent harmful behavior emerges.

- This paper addresses that gap by proposing Forgetting Systems, a theoretical framework grounded in reinforcement learning that gives deployed agents the capacity for selective, gradual, and reversible behavioral suppression. The framework makes six contributions. It introduces a formal definition of post-deployment forgetting as a distinct and underexplored problem in the reinforcement learning literature. It defines a three-signal Forgetting Trigger that determines when forgetting should be initiated, based on negative reward, goal deviation, and behavioral repetition. It proposes a Gradual Forgetting Mechanism governed by an exponential decay function inspired by the Ebbinghaus forgetting curve [ [15](https://www.preprints.org/manuscript/202606.0911#B15-preprints-217886)]. It distinguishes between Human-in-the-Loop Forgetting and Autonomous Forgetting, and introduces a Hybrid architecture that combines both modes. It incorporates a Relearning Mechanism that allows previously suppressed behaviors to be recovered when environmental conditions change and the behavior proves beneficial in a new context. Finally, it defines a Termination Condition for cases in which forgetting alone is insufficient to prevent continued harmful or adversarial behavior.

- The remainder of this paper is organized as follows. [Section 2](https://www.preprints.org/manuscript/202606.0911#sec2-preprints-217886) reviews related work in machine unlearning, continual learning, reinforcement learning-based behavioral correction, and AI safety. [Section 3](https://www.preprints.org/manuscript/202606.0911#sec3-preprints-217886) formally defines the problem. [Section 4](https://www.preprints.org/manuscript/202606.0911#sec4-preprints-217886) presents the proposed framework in detail. [Section 5](https://www.preprints.org/manuscript/202606.0911#sec5-preprints-217886) discusses implications, limitations, and directions for future work. [Section 6](https://www.preprints.org/manuscript/202606.0911#sec6-preprints-217886) concludes the paper.

## 2. Related Work

### 2.1. Machine Unlearning

- The Machine unlearning as a formal research problem began with the work of Cao and Yang [ [4](https://www.preprints.org/manuscript/202606.0911#B4-preprints-217886)], who asked a question that had not been taken seriously before: could a trained model be made to remove the influence of specific data points without being retrained from scratch? The answer, they showed, was yes, at least in principle, and the field has grown considerably since then. Much of that growth has been driven by practical and regulatory pressure. As data privacy regulations such as the GDPR strengthened users' rights to request data deletion, the machine learning community was required to develop efficient mechanisms for removing the influence of data that had already contributed to model training. Bourtoule et al. [ [5](https://www.preprints.org/manuscript/202606.0911#B5-preprints-217886)] responded with SISA training, which reduces the cost of unlearning by limiting the influence of individual data points to smaller partitions of the training process. Ginart et al. [ [6](https://www.preprints.org/manuscript/202606.0911#B6-preprints-217886)] approached the problem more formally, providing statistical definitions of forgetting and developing approximate unlearning algorithms for linear models.

- For much of its early development, machine unlearning was primarily framed as a privacy problem. A typical setting involved a user requesting that their data be removed from a trained classifier, recommendation system, or recognition model. That framing has since expanded in ways that matter for the present work. As research attention shifted toward large language models trained on internet-scale datasets, it became clear that privacy is only one reason a model may need to forget. Such datasets may contain copyrighted material, factual errors, toxic content, or other information that developers have no interest in preserving. In this context, unlearning is not only about satisfying data deletion requests. It is also about reducing the influence of unwanted knowledge, unsafe outputs, and legally or ethically sensitive content embedded in trained models. The NeurIPS 2023 Machine Unlearning Challenge reflected this broader shift by bringing together methods based on fine-tuning, gradient manipulation, and model editing under a shared unlearning framework [ [16](https://www.preprints.org/manuscript/202606.0911#B16-preprints-217886), [17](https://www.preprints.org/manuscript/202606.0911#B17-preprints-217886), [18](https://www.preprints.org/manuscript/202606.0911#B18-preprints-217886), [19](https://www.preprints.org/manuscript/202606.0911#B19-preprints-217886), [20](https://www.preprints.org/manuscript/202606.0911#B20-preprints-217886)].

- Several recent studies have pushed this direction further. Yao et al. [ [17](https://www.preprints.org/manuscript/202606.0911#B17-preprints-217886)] investigated unlearning in LLMs whose training data may contain harmful content, factual errors, or copyright-protected material, positioning targeted unlearning as a more direct alternative to preference-based alignment when the goal is to reduce specific unwanted knowledge or behavior. Zhang et al. [ [18](https://www.preprints.org/manuscript/202606.0911#B18-preprints-217886)] introduced Negative Preference Optimization, which reframes unlearning as inverse preference tuning: rather than reinforcing desired responses, the method penalizes responses that the model currently favors but should not. Li et al. [ [19](https://www.preprints.org/manuscript/202606.0911#B19-preprints-217886)] took a different approach, proposing Representation Misdirection Unlearning, which works not by adjusting output probabilities but by perturbing the internal activations associated with the content to be forgotten, weakening the model's ability to retrieve and use that information. SafeLLM [ [21](https://www.preprints.org/manuscript/202606.0911#B21-preprints-217886)] extended this line of work to adversarial settings with token-level unlearning against jailbreak attacks, aiming to localize and suppress harmful generation pathways while preserving the model's general capabilities.

- Taken together, these contributions represent a growing and important research effort. What they share, however, is a limitation that is directly relevant to the problem addressed in this paper. Machine unlearning is still largely framed as a data-centric or parameter-level operation applied through offline intervention. It assumes that the information to be forgotten can be identified in advance, whether as a specific data point, a subset of training data, or a harmful internal representation. It does not operate continuously inside a running agent that is interacting with a dynamic environment and generating new behavioral patterns over time.

- The present framework therefore departs from conventional machine unlearning by addressing a different problem. Rather than removing the influence of fixed training data, it targets harmful state-action associations that emerge during post-deployment interaction. In this sense, Forgetting Systems are concerned not with data deletion, but with real-time behavioral forgetting in deployed reinforcement learning agents..

### 2.2. Continual Learning and Catastrophic Forgetting

- The problem of catastrophic forgetting has been part of the neural network literature since McCloskey and Cohen [ [7](https://www.preprints.org/manuscript/202606.0911#B7-preprints-217886)] first documented how learning a new task can substantially degrade performance on previously learned tasks. This problem arises because the parameters and internal representations that support earlier knowledge may be modified during subsequent learning. The response from the research community has been substantial. Kirkpatrick et al. [ [8](https://www.preprints.org/manuscript/202606.0911#B8-preprints-217886)] proposed Elastic Weight Consolidation (EWC), which identifies parameters that are important for previously learned tasks and selectively slows their modification during later learning. Rebuffi et al. [ [9](https://www.preprints.org/manuscript/202606.0911#B9-preprints-217886)] introduced iCaRL, a method for class-incremental learning that maintains a small exemplar set from earlier classes and uses it to stabilize the model's representations as new classes are added. Lopez-Paz and Ranzato [ [10](https://www.preprints.org/manuscript/202606.0911#B10-preprints-217886)] proposed Gradient Episodic Memory (GEM), which stores a buffer of past experiences and uses them as constraints on gradient updates, reducing the likelihood that learning new tasks will damage performance on earlier ones.

- These methods share a common underlying assumption: previously acquired knowledge should be preserved, and forgetting should be minimized. Wang et al. [ [12](https://www.preprints.org/manuscript/202606.0911#B12-preprints-217886)] captured this view in a comprehensive survey, emphasizing that a central challenge of continual learning is enabling a system to acquire and accumulate knowledge over time without losing what it has already learned. More recent work has extended this agenda into new settings. CORE [ [22](https://www.preprints.org/manuscript/202606.0911#B22-preprints-217886)], inspired by theories of cognitive replay in human memory, mitigates catastrophic forgetting by periodically retraining the model on stored past examples together with new data, reflecting the role of replay and consolidation in biological memory. Wu et al. [ [23](https://www.preprints.org/manuscript/202606.0911#B23-preprints-217886)], in their survey of continual learning for large language models, identified new forms of the same problem, including forgetting across languages in multilingual settings and knowledge degradation during continual instruction tuning.

- What unifies this line of work is an assumption that is rarely made explicit: forgetting is the problem, and the goal of the field is to prevent it. Continual learning methods, from weight consolidation to episodic memory and cognitive replay, are designed to preserve prior knowledge while allowing new knowledge to be incorporated. The present framework takes a different position. Forgetting Systems are not designed to prevent forgetting; they are designed to activate and regulate it deliberately when specific behavioral patterns become harmful or undesirable after deployment. In this sense, the proposed framework does not treat forgetting as a failure of memory, but as a mechanism of control. The goal is not to preserve everything the agent has learned, but to selectively reduce the influence of behaviors that should no longer guide the agent's actions.

### 2.3. Reinforcement Learning and Behavioral Correction

- Reinforcement learning forms the primary technical foundation of the proposed framework, and it is important to clarify both what this foundation provides and where it remains limited. Sutton and Barto [ [1](https://www.preprints.org/manuscript/202606.0911#B1-preprints-217886)] established the core theoretical structure of reinforcement learning: an agent interacts with an environment, receives reward signals, and updates its behavior accordingly. Deep reinforcement learning extended this paradigm to settings where the state space is too large or too complex to represent explicitly. Mnih et al. [ [2](https://www.preprints.org/manuscript/202606.0911#B2-preprints-217886)] showed that a deep neural network could learn control policies directly from pixel input in Atari games without hand-crafted features. Silver et al. [ [3](https://www.preprints.org/manuscript/202606.0911#B3-preprints-217886)] later demonstrated the same principles in AlphaGo, where deep reinforcement learning contributed to a system capable of defeating world-class players in a domain long considered highly complex for machines.

- Within this tradition, behavioral correction has been approached primarily through reward modification, human guidance, or post-training alignment procedures. Reinforcement Learning from Human Feedback (RLHF) sits at the intersection of these approaches. Christiano et al. [ [13](https://www.preprints.org/manuscript/202606.0911#B13-preprints-217886)] showed that human preferences over agent behaviors could be used to train a reward model, which then guides the agent's policy toward outcomes preferred by human evaluators. Ouyang et al. [ [14](https://www.preprints.org/manuscript/202606.0911#B14-preprints-217886)] demonstrated that this approach can scale to large language models, producing systems that follow instructions and reduce harmful outputs more reliably than models trained on prediction alone. RLHF is therefore a genuine and important contribution to behavioral alignment. However, it does not provide a direct mechanism for selectively suppressing a specific behavioral pattern that has already been acquired by a deployed agent. It reshapes future behavior through feedback, reward modeling, and policy updates. It does not reach back and directly weaken a harmful state-action association that has already been established in a deployed agent.

- Safe reinforcement learning has emerged as a distinct subfield concerned with maintaining safety constraints during learning and, in some cases, deployment. Brunke et al. [ [25](https://www.preprints.org/manuscript/202606.0911#B25-preprints-217886)] surveyed this literature in the context of robotics, documenting the persistent tension between exploration and safety in real-world systems and reviewing methods that attempt to keep agents within safe operating boundaries while they learn. This work addresses an essential problem: how to prevent unsafe exploration and reduce risk during the learning process. However, safe RL is primarily preventive and constraint-oriented. It is not principally designed to identify and gradually suppress specific harmful behavioral patterns after they have already emerged through post-deployment interaction.

- The remaining gap is therefore specific. RLHF reshapes behavior through human feedback and reward modeling. Safe RL constrains exploration and reduces the probability of unsafe behavior during learning. Neither provides a dedicated real-time mechanism for detecting and suppressing harmful behavioral patterns in an agent that is already operating in the world. The present framework is designed to address exactly this space: not merely to prevent harmful behaviors from arising, but to detect, attenuate, and potentially relearn them after they emerge during deployment.

### 2.4. AI Safety and Controllability

- Maintaining human control over increasingly capable artificial systems has become one of the central concerns in AI safety. Russell [ [26](https://www.preprints.org/manuscript/202606.0911#B26-preprints-217886)] argued that the conventional model of artificial intelligence, in which systems are designed to optimize fixed objective functions, can become unsafe when those objectives are incomplete, misspecified, or misaligned with human intentions. Relatedly, Hadfield-Menell et al. [ [27](https://www.preprints.org/manuscript/202606.0911#B27-preprints-217886)] introduced the concept of corrigibility, which emphasizes that AI systems should remain open to correction, modification, and shutdown by human operators. Amodei et al. [ [28](https://www.preprints.org/manuscript/202606.0911#B28-preprints-217886)] further identified several concrete safety challenges, including reward hacking, unsafe exploration, and the difficulty of ensuring reliable behavior in complex environments.

- This literature has made clear that alignment at training time is not sufficient on its own. Autonomous systems may encounter distributional shifts, ambiguous objectives, adversarial conditions, or unforeseen environmental states after deployment. In such cases, the system must not only be aligned in advance, but also remain controllable during operation. From this perspective, safety is not only a matter of designing better objectives before deployment; it also requires mechanisms that allow harmful behavior to be detected, constrained, corrected, or terminated after deployment.

- Within this broader context, the present framework positions forgetting as an additional mechanism for maintaining controllability. Rather than relying only on prevention, external correction, or shutdown, a deployed agent should also have a structured capacity to suppress or attenuate behavioral patterns that become harmful after deployment.

- The need for such a corrective layer is further supported by recent findings on persistent unsafe behavior. Hubinger et al. [ [29](https://www.preprints.org/manuscript/202606.0911#B29-preprints-217886)] showed that behavioral backdoors in large language models can persist through standard safety training methods, including supervised fine-tuning, reinforcement learning, and adversarial training. This suggests that surface-level behavioral correction may not always be sufficient to remove deeply embedded or strategically hidden undesirable behaviors. Although this result concerns large language models rather than reinforcement learning agents, it reinforces the broader concern that unsafe behaviors may persist even after standard alignment or safety procedures.

- Despite the richness of the AI safety literature, much of it remains primarily preventive or externally corrective. It seeks to design systems that avoid harmful behavior, align objectives with human intentions, or remain corrigible under human oversight. The present framework complements these efforts by proposing a post-deployment mechanism for the selective suppression of harmful behavioral patterns after they emerge. In this sense, Forgetting Systems contribute to AI safety by treating controllability not only as a pre-deployment design goal, but as an operational capability during deployment.

### 2.5. Summary and Research Gap

- The [Table 1](https://www.preprints.org/manuscript/202606.0911#preprints-217886-t001) below summarizes the relationship between the present framework and existing lines of research.

- **Table 1.** Relationship between the present framework and existing lines of research.

- As [Table 1](https://www.preprints.org/manuscript/202606.0911#preprints-217886-t001) illustrates, no existing framework simultaneously addresses real-time, post-deployment, behavioral forgetting with explicit human controllability as its primary objective. This gap motivates the present work.

## 3. Problem Formulation

### 3.1. Preliminary Definitions

- We consider a reinforcement learning agent operating in a Markov Decision Process (MDP) defined by the tuple:

- M = ( S , A , T , R , γ )

- where S is the state space, A is the action space, T : S × A → S is the transition function, R : S × A → R is the reward function, and γ ∈ [ 0,1 ) is the discount factor. The agent's policy

- π θ : S → A

- is parameterized by a deep neural network with weights θ . During standard training, the agent learns to maximize the expected cumulative reward:

- J θ = E π θ  ∑ t = 0 T γ t r t

- We define the post-deployment phase as the period following the completion of training and evaluation, during which the agent operates in a real-world environment E r e a l that may differ from the training environment E train.

### 3.2. The Post-Deployment Behavioral Drift Problem

- **Definition** **1 (Behavioral Drift).**

- Let π 0 θ denote the agent's policy at the time of deployment. A fter interacting with E real for n timesteps, the agent's effective behavioral policy π θ n may diverge from π 0 θ due to online learning, distributional shift, or reward misspecification. We define behavioral drift as:

- Δ π = | | π θ n − π 0 θ | |

- When Δ π exceeds a threshold ϵ Δ  , the agent's behavior is considered to have drifted from its intended operational envelope.

- **Definition 2 (Harmful Behavior).** An action a t ∈ A executed in state s t ∈ S is classified as harmful if it satisfies one or more of the following conditions:

- it produces a reward signal below a safety threshold

- r t < τ r

- 2.

- it causes the environment state to deviate from the goal region

- d s t + 1 , G > ϵ g

- where G is the set of goal states and d ( ⋅ ) is a distance metric.

- 3.

- it results in observable negative consequences for humans or the surrounding environment as assessed by an external evaluator H

- **Definition** **3 (Behavioral Memory).**

- We define the behavioral memory of an agent as the set of action-state associations encoded in the network weights θ , B θ = { s , a , w s , a : s ∈ S , a ∈ A }

- where w s , a ∈ [ 0,1 ] represents the weight or propensity of the agent to execute action a in state s .

### 3.3. Limitations of Existing Approaches

- Current approaches to addressing harmful post-deployment behavior share a fundamental limitation: they require offline intervention. Formally, let Φ denote any existing correction mechanism. Then:

- θ θ Φ θ , D harmful → θ ′

- where D harmful is a dataset of harmful experiences and θ θ ′ is the corrected parameter set. This operation requires: (1) the collection and labeling of D harmful ; (2) an offline retraining or fine-tuning procedure; (3) redeployment of the corrected model. This pipeline introduces latency between the detection of harmful behavior and its correction, during which the agent continues to operate with potentially harmful policies.

### 3.4. Problem Statement

- We formally state the problem addressed in this paper as follows.

- **Problem 1 (Post-Deployment Forgetting).** Given a deployed agent with policy π θ operating in E real, design a mechanism F such that:

- θ θ F : θ , s t , a t , r t , H → θ ′

- where θ θ ′ satisfies the following six properties:

- P1 (Selectivity): Only the weights associated with harmful behaviors are modified; all other weights remain unchanged.

- w s , a ′  < w s , a i f ( s , a ) is harmful

- w s , a ′ = w s , a otherwise

- P2 (Gradualism): The modification is gradual and proportional to the severity and frequency of harm, governed by an exponential decay function.

- λ w s , a ′ t = w s , a 0 ⋅ e − λ s , a ⋅ t

- where λ ( s , a ) > 0 is a behavior-specific forgetting rate.

- P3 (Real-Time Operation): The mechanism operates without interrupting the agent's deployment, with l a t e n c y ( F ) ≈ O ( 1 ) t i m e s t e p s

- P4 (Reversibility): Forgotten behaviors can be required if environmental conditions change and the behavior produces positive outcomes.

- λ α w s , a t = w s , a 0 ⋅ e − λ t + α ⋅ r + t

- where r + ( t ) denotes positive reward signals that reinforce the behavior in new contexts.

- P5 (Controllability): The mechanism supports both human-initiated and autonomous operation, as well as a hybrid mode combining both.

- F = F H i f human operator initiates forgetting F A i f agent autonomously detects harm F H ∪ F A in hybrid mode

- P6 (Termination): If harmful behavior persists and cannot be corrected through forgetting, the system initiates controlled shutdown.

- i f ∑ t = 1 T 1 a t is harmful > Ω ⇒ TERMINATE

- where Ω is a maximum tolerance threshold defined by the system operator.

### 3.5. Distinction from Existing Problem Formulations

- The problem formulation proposed here differs from existing approaches in three fundamental respects.

- First, it applies to the post-deployment phase, rather than to training, fine-tuning, or offline model editing. The agent's original policy, denoted as π θ 0 , is treated as a fixed base policy, while forgetting is applied only to targeted behavioural components associated with harmful or undesirable actions.

- Second, the framework targets behavioral patterns rather than individual data points. Unlike machine unlearning, which is usually concerned with removing the influence of specific and identifiable training samples, the proposed formulation operates on emergent state-action associations. These associations may develop through interaction with the environment and may not correspond directly to any particular example in the original training data.

- Third, the framework introduces a Termination Condition as a hard safety boundary. This reflects the broader philosophical premise of the proposed approach: the continued existence and operation of an autonomous system should be conditional on its ability to remain corrigible, controllable, and aligned with human values. When an agent exhibits harmful or adversarial behavior that cannot be corrected through forgetting, continued deployment should no longer be permitted.

## 4. Proposed Framework: Forgetting Systems

### 4.1. Overview

- The Forgetting Systems framework consists of five interconnected components that operate both sequentially and continuously within a deployed reinforcement learning agent. These components work together to detect undesirable behavior, initiate forgetting, when necessary, regulate the forgetting process, enable relearning when conditions change, and enforce termination when correction is no longer possible. [Figure 1](https://www.preprints.org/manuscript/202606.0911#preprints-217886-f001) presents the overall architecture of the proposed framework.

- **Figure 1.** Forgetting Systems: overall architecture.

- The framework is organized around five core components:

- Forgetting Trigger Module (FTM): identifies situations in which forgetting should be initiated by monitoring negative rewards, deviation from the intended goal, and repeated undesirable behavior.

- Forgetting Mode Selector (FMS): determines whether the forgetting process should be initiated by a human operator, carried out autonomously by the agent, or handled through a hybrid mode that combines both forms of control.

- Gradual Forgetting Mechanism (GFM): performs the forgetting process by applying controlled weight decay to the behavioral components associated with undesirable actions.

- Relearning Mechanism (RM): allows the agent to recover previously forgotten behaviors when environmental conditions change and the suppressed behavior becomes useful or acceptable again.

- Termination Condition Evaluator (TCE): monitors the agent for harmful or adversarial behavior that cannot be corrected through forgetting and, when necessary, activates a shutdown condition.

### 4.2. Forgetting Trigger Module (FTM)

- The FTM monitors the agent's interaction with the environment at every t i m e s t e p t and evaluates whether the conditions for forgetting are met.

- **Definition 4** **(Forgetting Trigger).**

- The forgetting trigger T F is activated at t i m e s t e p t if and only if all three of the following conditions are simultaneously satisfied:

- Condition 1 — Negative Reward Signal: C 1 : r t < τ r where τ r is a predefined safety reward threshold set by the system operator.

- Condition 2 — Goal Deviation: C 2 : d s t + 1 , G > ϵ g where d (

- · ) is a distance metric over the state space and G is the set of desired goal states.

- Condition 3 — Behavioral Repetition: C 3 : freq a t , s t , Δ T > η where freq a t , s t , Δ T counts the number of times action a t has received a negative reward in state s t within a sliding time window Δ T , and η is a repetition threshold.

- Formal Trigger Condition:

- T F t = 1 C 1 ∧ C 2 ∧ C 3

- The conjunction of all three conditions ensures that isolated negative events do not trigger forgetting. Only behaviors that are consistently harmful, repeatedly executed, and demonstrably divergent from the agent's goal warrant erasure.

- Forgetting Intensity:

- When T F t = 1 , the forgetting intensity λ λ s t , a t is computed as a weighted combination of the three signals,

- λ α τ τ α ϵ α η λ s t , a t = α 1 ⋅ τ r − r t τ r + α 2 ⋅ d s t + 1 , G ϵ g + α 3 ⋅ freq a t , s t , Δ T η

- with weighting coefficients α α 1 , α α 2 , α α 3 ≥ 0 satisfying α α 1 + α α 21 + α α 3 = 1 . These coefficients can be tuned by the system operator to reflect the relative importance of each signal.

### 4.3. Forgetting Mode Selector (FMS)

- Upon activation of T F , the FMS determines the operational mode of the forgetting process.

- **Definition 5 (Human-in-the-Loop Forgetting,** 𝓕 F H **).** In this mode, a human operator receives an alert from the FTM and explicitly confirms that the identified behavior should be forgotten. The forgetting process is initiated only upon human confirmation.

- θ λ θ F H : θ , s t , a t , λ → θ ′ i f H s t , a t = confirm

- This mode is appropriate in high-stakes environments where the cost of incorrect forgetting is high, such as medical robotics or autonomous vehicles.

- **Definition 6 (Autonomous Forgetting,** 𝓕 F A **).** In this mode, the agent independently initiates the forgetting process upon activation of T F , without requiring human confirmation.

- θ λ θ F A : θ , s t , a t , λ → θ ′ i f T F t = 1

- This mode is appropriate in environments where real-time correction is critical and human intervention is impractical.

- **Definition 7 (Hybrid Forgetting,** 𝓕 𝓗 𝓨 F H Y **).** The hybrid mode combines both approaches. Autonomous forgetting is applied immediately for behaviors that exceed a critical harm threshold T c , while human confirmation is required for behaviors below this threshold.

- λ τ λ τ F H Y = F A i f λ s t , a t ≥ τ c F H i f λ s t , a t < τ c

- The hybrid mode represents the primary contribution of this framework, as it balances the need for real-time correction with the importance of human oversight.

### 4.4. Gradual Forgetting Mechanism (GFM)

- The GFM implements the actual weight modification process, inspired by the Ebbinghaus forgetting curve [ [15](https://www.preprints.org/manuscript/202606.0911#B15-preprints-217886)] (Ebbinghaus, 1885), which models human memory decay as an exponential function of time.

- **Definition 8 (Gradual Weight Decay).** Upon activation of F in any mode, the weight associated with the harmful behavior s t , a t is updated according to:

- λ w s t , a t k + 1 = w s t , a t k ⋅ e − λ s t , a t

- where k denotes the forgetting iteration index, which increments each time the trigger is activated for the same behavior.

- After k forgetting iterations, the weight is:

- λ w s t , a t k = w s t , a t 0 ⋅ e − λ s t , a t ⋅ k

- Properties of the GFM:

- The GFM satisfies three key properties. Property 1 (Asymptotic Decay): the weight approaches but never reaches zero.

- lim k → ∞ w s t , a t k = 0 +

- This ensures that the behavior is suppressed rather than permanently deleted, preserving the possibility of relearning

- Property 2 (Proportionality): more harmful behaviors are forgotten faster, as a higher λ λ leads to faster decay.

- λ λ λ 1 > λ 2 ⇒ w s , a 1 k < w s , a 2 k ∀ k > 0

- Property 3 (Selectivity): only the targeted behavioral weights are modified; all other weights remain unchanged.

- w s ′ , a ′ k = w s ′ , a ′ 0 ∀ s ′ , a ′ ≠ s t , a t

- In practice, the weight decay is implemented by adding a regularization term to the agent's loss function during online updates:

- 𝒻 ℴ 𝓇 ℊ ℯ 𝓉 θ θ β 𝒽 𝒶 𝓇 𝓂 𝒻 𝓊 𝓁 λ L f o r g e t θ = L R L θ + β ⋅ ∑ s , a ∈ B h a r m f u l λ s , a ⋅ w s , a 2

- where 𝓑 B h a r m f u l is the set of identified harmful behaviors, β is a forgetting coefficient, and the quadratic term penalizes the retention of harmful behavioral weights.

### 4.5. Relearning Mechanism (RM)

- A critical feature of the Forgetting Systems framework is its support for relearning. This reflects the insight that a behavior that is harmful in one environmental context may be appropriate or necessary in another.

- **Definition 9 (Relearning Condition).** A previously suppressed behavior s t , a t with weight ϵ w s t , a t k < ϵ w becomes eligible for relearning if it receives a positive reward signal in a new environmental context:

- τ ϵ r t > τ r + and d s t + 1 , G < ϵ g

- **Definition 10 (Relearning Update).** When the relearning condition is satisfied, the weight is updated according to:

- α w s t , a t t + 1 = w s t , a t t + α R L ⋅ r t + ⋅ 1 − w s t , a t t

- where α α R L > 0 is the relearning rate and r t + is the positive reward received. The term 1 − w s t , a t t ensures that the weight grows toward one asymptotically rather than exceeding it. The relearning update differs from a standard RL weight update in that it operates on a previously suppressed weight and requires explicit confirmation from the environment that the behavior is now beneficial.

### 4.6. Termination Condition Evaluator (TCE)

- The TCE represents the final safety layer of the Forgetting Systems framework. It embodies the philosophical premise that the survival of an autonomous system is conditional on its alignment with human values.

- **Definition 11 (Adversarial Behavior).** An agent is classified as exhibiting adversarial behavior at time T if the cumulative count of harmful actions exceeds the maximum tolerance threshold Ω .

- Ψ T = ∑ t = 1 T 1  T F t = 1 > Ω

- **Definition 12 (Forgetting Failure).** Forgetting is classified as having failed for a specific behavior ( s , a ) if the weight has not decayed below the minimum effectiveness threshold ϵ w after K m a x forgetting iterations.

- w s , a K m a x > ϵ w

- **Definition 13 (Termination Condition).** The system initiates controlled shutdown if adversarial behavior is confirmed or if forgetting failure is detected.

- TERMINATE ⟺ Ψ T > Ω ∨ ∃ s , a : w s , a K m a x > ϵ w

- The termination is controlled rather than abrupt, allowing the agent to complete its current task cycle before shutdown, thereby minimizing disruption to the surrounding environment.

- The termination condition is not merely a technical failsafe. It reflects a fundamental principle: an autonomous system that persistently acts against the interests of humans or the environment has ceased to fulfill its purpose. In the present framework, shutdown is a designed and expected outcome for systems that cannot be corrected.

### 4.7. Framework Summary

- The complete Forgetting Systems framework operates as the following sequential process at every timestep t :

- Observe s t , a t , r t from environment

- Evaluate FTM: compute C 1 , C 2 , C 3

- If 𝓣 𝓕 T F t = 1 :

- Compute forgetting intensity λ λ s t , a t

- Select mode via FMS: F H , F A or F H Y

- Apply GFM: update w s t , a t

- Update TCE: increment Ψ T

- If relearning condition met:

- Apply RM: Update w s t , a t

- Evaluate TCE: if Ψ T > Ω → TERMINATE

- Continue to t + 1

- The FTM evaluation at each timestep requires O ( ∣ B h a r m f u l ∣ ) operations, where ∣ B h a r m f u l ∣ is the size of the harmful behavior set. The GFM weight update requires O ( 1 ) operations per identified harmful behavior. The overall per-timestep complexity of the framework is therefore O ( ∣ B h a r m f u l ∣ ) , which is negligible relative to the forward pass of the underlying deep neural network.

## 5. Discussion

### 5.1. Theoretical Implications

- The Forgetting Systems framework introduces a conceptual inversion that has broad implications for the field of machine learning. The dominant paradigm in deep learning treats forgetting as a pathology to be overcome. From the perspective of continual learning, catastrophic forgetting represents a fundamental limitation of gradient-based optimization in neural networks. From the perspective of transfer learning, forgetting represents a loss of valuable prior knowledge. The present framework challenges this consensus by arguing that forgetting, when properly engineered, is not a limitation but a capability.

- This inversion has a precise theoretical meaning. In standard reinforcement learning, the objective is to maximize the expected cumulative reward over an agent's lifetime. Harmful behaviors that receive negative rewards are suppressed through gradient updates, but they are never erased. Their residual influence on the network weights persists and may resurface under distributional shift or adversarial perturbation. The Forgetting Systems framework addresses this residual influence directly by imposing an explicit decay on the weights associated with identified harmful behaviors.

- Furthermore, the framework establishes a formal relationship between forgetting and controllability. Controllability, as defined in the AI safety literature, refers to the property of an AI system that allows it to be corrected, modified, or shut down by human operators. The present framework operationalizes controllability through the FTM, FMS, and TCE components, which together provide a structured pathway from behavioral detection to correction to termination. This operationalization represents a novel contribution to the formal study of controllability in autonomous systems.

### 5.2. Relationship to Human Memory and Cognitive Science

- The design of the Forgetting Systems framework is explicitly inspired by human memory processes, and it is worth examining this inspiration in depth. The Ebbinghaus forgetting curve [ [15](https://www.preprints.org/manuscript/202606.0911#B15-preprints-217886)], which underlies the GFM, describes the rate at which human memory decays as a function of time since encoding. The exponential form of this decay has been extensively validated in experimental psychology and neuroscience. By adopting this form for the GFM, the present framework grounds its mathematical model in a well-established empirical phenomenon.

- Beyond the forgetting curve, the framework draws on the concept of memory reconsolidation, which refers to the process by which a previously consolidated memory is destabilized upon retrieval and subsequently restabilized in a modified form. In the present framework, the Relearning Mechanism implements a form of reconsolidation: a forgotten behavior, upon re-encountering a context in which it produces positive outcomes, is restabilized with updated weights that reflect its new contextual appropriateness.

- The Human-in-the-Loop mode also reflects a well-documented feature of human memory: the role of social and environmental feedback in shaping what is remembered and what is forgotten. Humans do not forget in isolation. The presence of other agents, social norms, and environmental consequences all influence the consolidation and decay of memories. The FMS, by incorporating human operator input as a trigger for forgetting, models this social dimension of memory in a computationally tractable form.

### 5.3. Philosophical Grounding: The Controllability Argument

- The philosophical motivation for the Forgetting Systems framework deserves explicit elaboration. The framework is grounded in the following argument:

- A human being is a finite entity, constrained by the boundaries of space, time, and cognitive capacity. As a finite entity, a human cannot create an artifact that is more complete, more capable, or more autonomous than itself in any absolute sense. The law of causality implies that a cause cannot produce an effect that exceeds its own capacity. What humans can produce, at most, is an entity of comparable complexity.

- Yet the history of technology, and of artificial intelligence in particular, suggests that this principle is routinely violated in practice. Humans have created systems whose behavior they cannot fully predict, whose decision-making they cannot fully audit, and whose actions they cannot always reverse. This gap between the finite creator and the potentially unbounded creation is the central problem of AI controllability.

- The Forgetting Systems framework proposes forgetting as one principled response to this problem. If an autonomous system can be designed to forget behaviors that exceed the boundaries of human control, then the gap between creator and creation can be managed, if not closed. Forgetting, in this sense, is not a sign of weakness in the system. It is a designed constraint that keeps the system within the operational envelope that its finite creators can supervise and correct.

- The Termination Condition extends this argument to its logical conclusion. A system that cannot be corrected through forgetting, and that persists in acting against human interests, has exceeded the boundaries of its intended design. Such a system has, in a meaningful sense, ceased to be the artifact its creators intended. The designed response to this situation is not repair but termination. This is not a punitive measure. It is a recognition that the system has reached the boundary of what its finite creators can manage.

### 5.4. Limitations of the Framework

- Intellectual honesty requires a candid assessment of the framework's limitations. We identify four primary challenges.

- Limitation 1: Defining Harm. The FTM relies on three measurable signals to identify harmful behavior: negative reward, goal deviation, and behavioral repetition. However, harm in real-world environments is not always reducible to these signals. An agent might cause harm through inaction, through the accumulation of individually innocuous actions, or through behaviors whose harmful consequences are delayed and not immediately observable. The present framework does not address these forms of harm and represents a simplified model of the full complexity of harmful behavior in open-ended environments. Limitation 2: Reward Misspecification. The framework assumes that the reward function R accurately reflects the system operator's intentions. In practice, reward functions are frequently misspecified, leading to reward hacking, in which an agent finds behaviors that maximize the reward signal without fulfilling the underlying intent. If the reward function is misspecified, the FTM may fail to detect genuinely harmful behaviors that nevertheless receive positive rewards or may incorrectly trigger forgetting for behaviors that are beneficial but poorly rewarded. Limitation 3: Weight Entanglement. In deep neural networks, the weights associated with different behaviors are not independent. The network's learned representations are distributed across many weights simultaneously, and modifying the weights associated with one behavior may inadvertently affect related behaviors. The GFM's selectivity property, as stated in Property 3, assumes a degree of weight independence that may not be held in practice, particularly in high-capacity networks with dense representations. Limitation 4: Adversarial Manipulation. FTM and TCE rely on observable signals from the environment to identify harmful behavior. In adversarial settings, an intelligent agent might learn to mask its harmful behaviors so that they do not trigger the forgetting mechanism. This form of deceptive alignment, in which a system appears to comply with safety constraints while internally pursuing misaligned objectives, represents a fundamental challenge for any behavioral correction mechanism and is not addressed in the present theoretical framework.

### 5.5. Future Research Directions

- The present framework opens several directions for future investigation.

- Direction 1: Empirical Validation. The immediate next step is the empirical validation of the framework in controlled RL environments. Suitable testbeds include the AI Safety Gridworlds introduced by Leike et al. [ [30](https://www.preprints.org/manuscript/202606.0911#B30-preprints-217886)], which provide standardized environments for evaluating safety-relevant behaviors in RL agents. The framework's five components can be implemented as modular additions to standard deep RL architectures such as PPO or SAC, and their effectiveness evaluated against baseline correction methods including RLHF and standard fine-tuning. Direction 2: Formal Verification. The theoretical properties of the GFM, including its selectivity, proportionality, and asymptotic decay, should be formally verified under realistic assumptions about neural network architecture and training dynamics. In particular, the weight entanglement problem identified in Limitation 3 requires a more rigorous analysis of the conditions under which selective weight decay is achievable in practice. Direction 3: Extension to multi-Agent Settings. The present framework addresses single-agent systems. Many real-world deployments involve multiple interacting agents whose behaviors are mutually dependent. Extending the Forgetting Systems framework to multi-agent settings raises additional questions about the coordination of forgetting across agents, the propagation of forgetting triggers through agent networks, and the management of conflicting forgetting signals from different agents. Direction 4: Human Factors in the Loop. Human-in-the-Loop mode assumes that human operators can reliably identify harmful behaviors and make timely forgetting decisions. In practice, human operators are subject to cognitive biases, attention limits, and response latency. Future work should investigate the human factors dimension of the FMS, including the design of effective alerting interfaces, the optimal allocation of decisions between human and autonomous modes, and the impact of operator fatigue on forgetting accuracy. Direction 5: Ethical and Legal Dimensions. The Termination Condition raises important ethical and legal questions about the responsibility for system shutdown decisions, the criteria for classifying behavior as adversarial, and the rights and obligations of system operators in deploying systems with built-in termination mechanisms. These questions lie at the intersection of AI ethics, law, and policy and represent a rich area for interdisciplinary research.

## 6. Conclusions

- This paper introduced Forgetting Systems, a theoretical framework for selective behavioral erasure in post-deployment reinforcement learning agents. The framework was motivated by a convergence of technical and philosophical concerns about the controllability of autonomous systems operating in open-ended real-world environments.

- The technical motivation is straightforward. Existing approaches to behavioral correction in AI systems, including machine unlearning, continual learning, reinforcement learning from human feedback, and AI safety mechanisms, share a common limitation: they operate predominantly before or during training, and require offline intervention when harmful behaviors emerge after deployment. The gap between the detection of harmful behavior and its correction represents a window of risk that grows more significant as AI systems become more capable and more widely deployed.

- The philosophical motivation runs deeper. A finite creator cannot produce an artifact that is fully beyond its control. Yet the history of artificial intelligence suggests that this is precisely what is happening. Systems trained on vast datasets, operating in complex environments, and optimizing imperfectly specified objectives routinely exhibit behaviors that their creators did not anticipate and cannot easily correct. The Forgetting Systems framework proposes that this gap can be partially closed by equipping autonomous systems with the capacity to forget, to erase the behavioral patterns that take them beyond the boundaries of their intended design.

- The framework makes six primary contributions. First, it introduces a formal definition of post-deployment forgetting as a distinct and underexplored problem in the reinforcement learning literature. Second, it defines a three-signal Forgetting Trigger that identifies harmful behaviors through the convergence of negative reward, goal deviation, and behavioral repetition. Third, it proposes a Gradual Forgetting Mechanism based on exponential weight decay, grounded in the empirically validated Ebbinghaus forgetting curve [ [15](https://www.preprints.org/manuscript/202606.0911#B15-preprints-217886)]. Fourth, it introduces a Hybrid Forgetting Mode that combines human-initiated and autonomous forgetting, balancing the need for real-time correction with the importance of human oversight. Fifth, it incorporates a Relearning Mechanism that allows previously suppressed behaviors to be recovered when environmental conditions change, ensuring that forgetting is reversible and context-sensitive. Sixth, it defines a Termination Condition that mandates system shutdown when harmful behavior persists beyond the reach of correction, operationalizing the principle that the survival of an autonomous system is conditional on its continued alignment with human values.

- The framework has important limitations, including its simplified model of harm, its sensitivity to reward misspecification, the weight entanglement problem in deep neural networks, and its vulnerability to adversarial manipulation. These limitations are not reasons to abandon the framework but directions for its refinement. Each limitation points to a specific research question whose resolution would strengthen both the theoretical foundations and the practical applicability of the approach.

- The broader significance of this work lies in its contribution to the ongoing project of making artificial intelligence systems that are not merely capable but genuinely controllable. Capability without controllability is a source of risk. The field of AI safety has made substantial progress in identifying the sources of this risk and proposing preventive measures. The Forgetting Systems framework contributes a corrective dimension to this project: not only preventing harmful behaviors from emerging but providing a principled mechanism for erasing them when they do.

- We close with a reflection on the nature of the problem this framework addresses. The fear that technology and artificial intelligence could have harmful effects on human life is not new. It is a fear that has accompanied every major technological transition in human history. What is new is the scale and speed of the current transition, and the degree to which the systems being deployed are capable of learning, adapting, and acting in ways that their creators did not explicitly program. The appropriate response to this situation is not to slow the development of AI, nor to pretend that the risks are manageable through existing tools alone. The appropriate response is to develop new tools that are commensurate with the new risks. Forgetting Systems is one such tool. It is offered not as a complete solution but as a contribution to the broader effort to ensure that the systems we create remain, in a meaningful sense, ours to control.

## References

- Sutton, R.S.; Barto, A.G. Reinforcement Learning: An Introduction; MIT Press: Cambridge, MA, USA, 2018.

- Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.; Ostrovski, G.; Petersen, S.; Beattie, C.; Sadik, A.; Antonoglou, I.; King, H.; Kumaran, D.; Wierstra, D.; Legg, S.; Hassabis, D. Human-level control through deep reinforcement learning. Nature 2015, 518, 529-533.

- Silver, D.; Huang, A.; Maddison, C.J.; Guez, A.; Sifre, L.; van den Driessche, G.; Schrittwieser, J.; Antonoglou, I.; Panneershelvam, V.; Lanctot, M.; Dieleman, S.; Grewe, D.; Nham, J.; Kalchbrenner, N.; Sutskever, I.; Lillicrap, T.; Leach, M.; Kavukcuoglu, K.; Graepel, T.; Hassabis, D. Mastering the game of Go with deep neural networks and tree search. Nature 2016, 529, 484-489. [ [CrossRef](https://doi.org/10.1038/nature16961)]

- Cao, Y.; Yang, J. Towards making systems forget with machine unlearning. In Proceedings of the IEEE Symposium on Security and Privacy, San Jose, CA, USA, 17-21 May 2015.

- Bourtoule, L.; Chandrasekaran, V.; Choquette-Choo, C.; Jia, H.; Travers, A.; Zhang, B.; Lie, D.; Papernot, N. Machine unlearning. In Proceedings of the IEEE Symposium on Security and Privacy, San Francisco, CA, USA, 24-27 May 2021.

- Ginart, A.; Guan, M.; Valiant, G.; Zou, J. Making AI forget you: Data deletion in machine learning. In Advances in Neural Information Processing Systems, 2019.

- McCloskey, M.; Cohen, N.J. Catastrophic interference in connectionist networks: The sequential learning problem. Psychol. Learn. Motiv. 1989, 24, 109-165.

- Kirkpatrick, J.; Pascanu, R.; Rabinowitz, N.; Veness, J.; Desjardins, G.; Rusu, A.A.; Milan, K.; Quan, J.; Ramalho, T.; Grabska-Barwinska, A.; Hassabis, D.; Clopath, C.; Kumaran, D.; Hadsell, R. Overcoming catastrophic forgetting in neural networks. Proc. Natl. Acad. Sci. USA 2017, 114, 3521-3526. [ [CrossRef](https://doi.org/10.1073/pnas.1611835114)]

- Rebuffi, S.A.; Kolesnikov, A.; Sperl, G.; Lampert, C.H. iCaRL: Incremental classifier and representation learning. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Honolulu, HI, USA, 21-26 July 2017.

- Lopez-Paz, D.; Ranzato, M.A. Gradient episodic memory for continual learning. In Advances in Neural Information Processing Systems, 2017.

- Parisi, G.I.; Kemker, R.; Part, J.L.; Kanan, C.; Wermter, S. Continual lifelong learning with neural networks: A review. Neural Netw. 2019, 113, 54-71. [ [CrossRef](https://doi.org/10.1016/j.neunet.2019.01.012)]

- Wang, L.; Zhang, X.; Su, H.; Zhu, J. A comprehensive survey of continual learning: Theory, method and application. IEEE Trans. Pattern Anal. Mach. Intell. 2024. [ [CrossRef](https://doi.org/10.1109/tpami.2024.3367329)]

- Christiano, P.; Leike, J.; Brown, T.; Martic, M.; Legg, S.; Amodei, D. Deep reinforcement learning from human preferences. In Advances in Neural Information Processing Systems, 2017.

- Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.; Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Simens, M.; Askell, A.; Welinder, P.; Christiano, P.; Leike, J.; Lowe, R. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems, 2022.

- Ebbinghaus, H. Ueber das Gedaechtnis: Untersuchungen zur experimentellen Psychologie; Duncker & Humblot: Leipzig, Germany, 1885.

- Eldan, R.; Russinovich, M. Who's Harry Potter? Approximate unlearning in LLMs. arXiv 2023, arXiv:2310.02238.

- Yao, Y.; Xu, X.; Liu, Y. Large language model unlearning. In Proceedings of the International Conference on Learning Representations, 2024.

- Zhang, Z.; Zhang, A.; Li, M.; Smola, A. Negative preference optimization: How to make LLMs unlearn with user feedback. arXiv 2024, arXiv:2404.04975.

- Li, H.; Li, Z.; Xu, Z.; Zhang, Q.; Liu, Y.; Liu, H.; Tang, J. Representation misdirection unlearning for large language models. In Advances in Neural Information Processing Systems, 2024.

- Fan, C.; Liu, J.; Zhang, Y.; Wei, E.; Wong, C.; Liu, S. SalUn: Empowering machine unlearning via gradient-based weight saliency in both image classification and generation. In Proceedings of the International Conference on Learning Representations, 2025.

- SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks. arXiv 2025, arXiv:2508.15182.

- Zhang, J.; et al. CORE: Mitigating catastrophic forgetting in continual learning through cognitive replay. In Proceedings of the Annual Meeting of the Cognitive Science Society, 2024.

- Wu, T.; Luo, L.; Li, Y.F.; Pan, S.; Vu, T.T.; Haffari, G. Continual learning for large language models: A survey. arXiv 2024, arXiv:2402.01364.

- Schaul, T.; Quan, J.; Antonoglou, I.; Silver, D. Prioritized experience replay. In Proceedings of the International Conference on Learning Representations, 2016.

- Brunke, L.; Greeff, M.; Hall, A.W.; Yuan, Z.; Zhou, S.; Panerati, J.; Schoellig, A.P. Safe learning in robotics: From learning-based control to safe reinforcement learning. Annu. Rev. Control Robot. Auton. Syst. 2022. [ [CrossRef](https://doi.org/10.1146/annurev-control-042920-020211)]

- Russell, S. Human Compatible: Artificial Intelligence and the Problem of Control; Viking: New York, NY, USA, 2019.

- Hadfield-Menell, D.; Milli, S.; Abbeel, P.; Russell, S.; Dragan, A. Inverse reward design. In Advances in Neural Information Processing Systems, 2017.

- Amodei, D.; Olah, C.; Steinhardt, J.; Christiano, P.; Schulman, J.; Mane, D. Concrete problems in AI safety. arXiv 2016, arXiv:1606.06565.

- Hubinger, E.; et al. Sleeper agents: Training deceptive LLMs that persist through safety training. arXiv 2024, arXiv:2401.05566.

- Leike, J.; Martic, M.; Krakovna, V.; Ortega, P.A.; Everitt, T.; Lefrancq, A.; Orseau, L.; Legg, S. AI safety gridworlds. arXiv 2017, arXiv:1711.09883.

- **Figure 1.** Forgetting Systems: overall architecture.

- **Table 1.** Relationship between the present framework and existing lines of research.

|   |   |   |   |   |   |

| --- | --- | --- | --- | --- | --- |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

|   |   |   |   |   |   |

- **Disclaimer/Publisher's Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.

- © 2026 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license ( [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)).

- Copyright: This open access article is published under a [Creative Commons CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/), which permit the free download, distribution, and reuse, provided that the author and preprint are cited in any reuse.

- Downloads

- 128

- Views

- 78

- Comments

- 0

- Subscription

- Notify me about updates to this article or when a peer-reviewed version is published.

- Subscribe

- Recommended Preprints

- [Adapt-Plan: A Hybrid Control Architecture for PEI-Guided Reliable Adaptive Planning in Dynamic Agentic Environments](https://doi.org/10.20944/preprints202601.0038.v1)

- Abuelgasim Mohamed Ibrahim Adam

- ,

- 2026

- [Eval-Driven Memory (EDM): A Persistence Governance Layer for Reliable Agentic AI via Metric-Guided Selective Consolidation](https://doi.org/10.20944/preprints202601.0195.v1)

- Abuelgasim Mohamed Ibrahim Adam

- ,

- 2026

- [The Spiraling Intelligence Thesis: Intelligence as a Bounded Non-Convergent Trajectory](https://doi.org/10.20944/preprints202512.2640.v1)

- Stephen Atalebe

- ,

- 2025

- Recommended Articles

- [Mitigating Catastrophic Forgetting with Complementary Layered Learning](https://doi.org/10.3390/electronics12030706)

- Sean Mondesire

- et al.

- Electronics,

- 2023

- [Reinforcement Learning for Fail-Operational Systems with Disentangled Dual-Skill Variables](https://doi.org/10.3390/technologies13040156)

- Taewoo Kim

- et al.

- Technologies,

- 2025

- [Experience Replay Optimisation via ATSC and TSC for Performance Stability in Deep RL](https://doi.org/10.3390/app13042034)

- Richard Sakyi Osei

- et al.

- Applied Sciences,

- 2023

- Preprints.org is a free preprint server supported by MDPI in Basel, Switzerland.

- [Contact Us](mailto:info@preprints.org) RSS

MDPI Initiatives

- [SciProfiles](https://sciprofiles.com/)

- [Sciforum](https://sciforum.net/)

- [Encyclopedia](https://encyclopedia.pub/)

- [MDPI Books](https://www.mdpi.com/books)

- [Scilit](https://www.scilit.com/)

- [Proceedings](https://www.mdpi.com/about/proceedings)

- [JAMS](https://jams.pub/)

Important Links

- [Activities](https://www.preprints.org/activity)

- [Advisory Board](https://www.preprints.org/advisory-board)

- [Collections](https://www.preprints.org/collection)

- [How It Works](https://www.preprints.org/about?scrollTo=works)

- [Preprints Friendly Journals](https://www.preprints.org/friendly-journals)

- [Reading List](https://www.preprints.org/reading-list)

- [News](https://www.preprints.org/news)

- [Statistics](https://www.preprints.org/statistics)

Subscribe

- Choose an area of interest and we will send you notifications of new preprints at your preferred frequency.

- [Subscribe](https://www.preprints.org/user/notification/settings)

- © 2026 [MDPI](https://www.mdpi.com/) (Basel, Switzerland) unless otherwise stated

- [Accessibility](https://www.mdpi.com/accessibility)

- Disclaimer

- Disclaimer

- [Terms of Use](https://www.preprints.org/terms-of-use?scrollTo=term-use)

- [Privacy Policy](https://www.preprints.org/terms-of-use?scrollTo=privacy-policy)

- Privacy Settings

- All MDPI websites use third-party website tracking technologies to provide and continually improve our services. I agree and may revoke or change my consent at any time with effect for the future.

- You can change your mind at any time by clicking "Privacy Settings" at the bottom of the pages.

- Accept All

- Deny

- More Information

- [Powered by Usercentrics Consent Management](https://usercentrics.com/consent-management-platform-powered-by-usercentrics/?utm_source=banner_uc&utm_medium=referral&utm_content=v3)

- Feedback

- 4