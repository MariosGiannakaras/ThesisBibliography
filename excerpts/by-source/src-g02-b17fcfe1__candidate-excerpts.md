# Candidate Excerpts — Discovering and Using Structure in Autonomous Machine Learning - Research Collection

- Source ID: `SRC-G02-B17FCFE1`
- Source file: `sources/raw-md/src-g02-b17fcfe1__discovering-and-using-structure-in-autonomous-machine-learning-research-collection.md`
- Status: machine-extracted candidates; verify against the source before citation.

## Abstract

Source line: approximately 46

> The ability to autonomously understand complex environments and act in them is an essenti-al goal in artificial agents’ development. State-of-the-art agents may excel in structured tasks, such as assembly line work, but they often fail to adapt to dynamic changes such as those encountered in domestic settings or natural outdoor environments, calling for advancement in agents that can perceive, learn, and reason in the real world as situations evolve. While achieving full autonomy is elusive for random changes in the environment, such a goal is attainable because the world around us is highly structured. However, the realistic interface to the world for both humans and artificial agents is a stream of unstructured, high-dimensional sensory inputs, like images. Thus, to build autonomous machines that can explore their open-ended environments and acquire large repertoires of skills, it is e

## 3.5 Conclusion and Future Work

Source line: approximately 1130

> In this chapter, we have shown that discovering structure in the observations of the environment with a compositional generative world models and using it for controlling different parts of the environment is crucial for solving tasks in compositional environments. Learning to manipulate different parts of object-centric representations is a powerful way to acquire useful skills such as object manipulation. Our SMORL agent learns how to control different entities in the environment and can then combine the learned skills to achieve more complex compositional goals such as rearranging several objects using only the final image of the arrangement.

## 4.5 Conclusion and Future Work

Source line: approximately 1712

> In this work, we introduce SRICS, a self-supervised RL method that learns the relational structure of the environment and exploits this structure to learn a compatible sequence of skills to solve a difficult compositional goal. In a range of experiments in multi-object environments with robotic arm manipulation tasks, we demonstrate that SRICS is effective at discovering the most active dynamic relations between objects and can successfully rearrange multiple objects even in the presence of object interactions.

## 5.5 Conclusion and Future Work

Source line: approximately 2082

> In this chapter, we presented a procedure for semantic object segmentation without using any human annotations clearly improving over previous work. As any unsupervised seg-mentation method requires some biases to be assumed or learned from data, we propose to use object-centric datasets on which localization and categorization priors could be learned in a self-supervised way. We show that combining those priors together with an iterative self-training procedure leads to significant improvements over previous approaches that rely on dense self-supervised representation learning. This combination reveals the hidden potential of object-centric datasets and allows creating a strong baseline for unsupervised segmentation methods by leveraging and combining learned priors.

## 6.3 Method

Source line: approximately 2238

> In this section, we describe the main new components of VideoSAUR — our proposed object-centric video model — and its training: a pre-trained self-supervised ViT encoder extracting frame features (Sec. 6.3.1), a temporal similarity loss that adds a motion bias to object discovery (Sec. 6.3.2), and the SlotMixer decoder to achieve efficient video processing (Sec. 6.3.3). See Fig. 6.2 for an overview.
