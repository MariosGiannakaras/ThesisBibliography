> Source: https://arxiv.org/pdf/1901.02219

Uncertainty-Based Out-of-Distribution Detection in Deep Reinforcement Learning 
Andreas Sedlmeier∗ LMU Munich 
Munich, Germany 
Thomas Gabor LMU Munich 
Munich, Germany 
Thomy Phan LMU Munich 
Munich, Germany 
Lenz Belzner MaibornWolff 
Munich, Germany 
Claudia Linnhoff-Popien LMU Munich 
Munich, Germany 
Abstract 
We consider the problem of detecting out-of-distribution (OOD) samples in deep reinforcement learning. In a value based reinforcement learning setting, we propose to use uncertainty estimation techniques directly on the agent’s value estimating neural network to detect OOD samples. The focus of our work lies in analyzing the suitability of approximate Bayesian inference methods and related ensembling techniques that generate uncertainty estimates. Although prior work has shown that dropout-based variational inference techniques and bootstrap-based approaches can be used to model epistemic uncertainty, the suitability for detecting OOD samples in deep reinforcement learning remains an open question. Our results show that uncertainty estimation can be used to differentiate in- from out-of-distribution samples. Over the complete training process of the reinforcement learning agents, bootstrap-based approaches tend to produce more reliable epistemic uncertainty estimates, when compared to dropout-based approaches. 
1 Introduction 
One of the main impediments to the deployment of machine learning systems in the real world is the difficulty to show that the system will continue to reliably produce correct predictions in all the situations it encounters in production use. One of the possible reasons for failure is so called out-of-distribution (OOD) data, i.e. data which deviates substantially from the data encountered during training. As the fundamental problem of limited training data seems unsolvable for most cases, especially in sequential decision making tasks like reinforcement learning, a possible first step towards a solution is to detect and report the occurance of OOD data. This can prevent silent failures caused by wrong predictions of the machine learning system, for example by handing control over to a human supervisor [1]. In this paper, we propose to use uncertainty estimation techniques in combination with value-based reinforcement learning to detect OOD samples. We focus on deep Q-Learning [20], integrating directly with the agent’s value-estimating neural network. 
When considering to use uncertainty estimation in order to detect OOD samples, it is important to differentiate two types of uncertainty: aleatoric and epistemic uncertainty. The first type, aleatoric uncertainty models the inherent stochasticity in the system and consequently cannot be reduced by capturing more data. Epistemic uncertainty by contrast arises out of a lack of sufficient data to exactly infer the underlying system’s data generating function. Consequently, epistemic uncertainty tends to be higher in areas of low data density. Qazaz [25], who in turn refers to Bishop [2] for the initial 
∗Corresponding author: Andreas Sedlmeier <andreas.sedlmeier@ifi.lmu.de> 
Preprint. Work in progress. 
 
 
 
 
 
 
 
 
 
 
conjecture, showed that the epistemic uncertainty σepis(x) is approximately inversely proportional to the density p(x) of the input data, for the case of generalized linear regression models as well as multi-layer neural networks: σepis(x) ∝ p−1(x) 
This also forms the basis of our proposed method: to use this inverse relation between epistemic uncertainty and data density in order to differentiate in- from out-of-distribution samples. 
2 Related Work 
A systematic way to deal with uncertainty is via Bayesian inference. Its combination with neural networks in the form of Bayesian neural networks is realised by placing a probability distribution over the weight-values of the network [19]. As calculating the exact Bayesian posterior quickly becomes computationally intractable for deep models, a popular solution are approximate inference methods [9, 12, 3, 7, 13, 17, 8]. Another option is the construction of model ensembles, e.g., based on the idea of the statistical bootstrap [6]. The resulting distribution of the ensemble predictions can then be used to approximate the uncertainty [22, 15]. Both approaches have been used for tasks as diverse as machine vision [14], disease detection [16], or decision making [5, 22]. 
For the case of low-dimensional feature spaces, OOD detection (also called novelty detection) is a well-researched problem. For a survey on the topic, see e.g. Pimentel et al. [24], who distinguish between probabilistic, distance-based, reconstruction-based, domain-based and information theoretic methods. During the last years, several new methods based on deep neural networks were proposed for high-dimensional cases, mostly focusing on classification tasks, e.g. image classification. Hendrycks and Gimpel [11] propose a baseline for detecting OOD examples in neural networks, based on the predicted class probabilities of a softmax classifier. Liang et al. [18] improve upon this baseline by using temperature scaling and by adding perturbations to the input. These methods are not directly applicable to our focus, value-based reinforcement learning, where neural networks are used for regression tasks. Other methods, especially generative-neural-network-based techniques [26] could provide a solution, but at the cost of adding separate, additional components. Our approach has the benefit of not needing additional components, as it directly integrates with the neural network used for value estimation. 
3 Experimental Setup 
One of the problems in researching OOD detection for reinforcement learning is the lack of datasets or environments which can be used for generating and assessing OOD samples in a controlled and reproducible way. By contrast to the field of image classification, where benchmark datasets like notMNIST [4] exist that contain OOD samples, there are no equivalent sets for reinforcement learning. As a first step, we developed a simple gridworld environment, which allows modifications after the training process, thus producing OOD states during evaluation. 
For our experiments, we focus on a simple gridworld pathfinding environment. During training, the agent starts every episode at a random position in the left half of the 12 × 4 grid space. Its goal is to reach a specific target position in the right half of the grid, which also varies randomly every episode, by choosing one of the four possible actions: {up,down,left,right}. A vertical set of walls separates the two halves of the environment, acting as static obstacles. Each step of the agent incurs a cost of −1 except the target-reaching action, which is rewarded with +100 and ends the episode. This configuration of the environment is called the train environment. For evaluating the OOD detection performance, we flip the start and goal positions, i.e. the agent starts in the right half of the environment and has to reach a goal position in the left half. This so called mirror environment produces states which the agent has not encountered during training. Consequently, we expect higher epistemic uncertainty values for these OOD states. Note that training is solely performed in the train environment. Evaluation runs are executed independently of the training process, based on model snapshots generated at the respective training episodes. Data collected during evaluation runs is not used for training. The state of the environment is represented as a stack of three W × H feature planes (W being the width, H the height of the grid layout) with each plane representing the spatial positions of all environment objects of a specific type: agent, target or wall. 
We compare different neural network architectures and their effect on the reported uncertainty values as the networks are being used by the RL agent for value estimation. The Monte-Carlo Dropout 
2
network (MCD) uses dropout variational inference as described by [14]. Our implementation consists of two fully-connected hidden layers with 64 neurons each, followed by two separate neurons in the output layer representing µ and σ of a normal distribution. Before every weight layer in the model, a dropout layer with p = 0.95 is added, specifying the probability that a neuron stays active. Model loss is calculated by minimizing the negative log-likelihood of the predicted output distribution. Epistemic uncertainty as part of the total predictive uncertainty is then calculated according to the following formula: Varep(y) ≈ 1 
T 
∑T t=1 ŷ 
2 t − ( 1 
T 
∑T t=1 ŷt) 
2 with T outputs ŷt of the Monte-Carlo sampling. 
Gal et al. [8] suggested an improvement to the default Monte-Carlo dropout method called Concrete Dropout which does not require a pre-specified dropout rate and instead learns individual dropout rates per layer. This method is of special interest when used in the context of reinforcement learning, as here the available data change during the training process, rendering a manual optimization of the dropout rate hyperparameter even more difficult. Our implementation of the Monte-Carlo Concrete Dropout network (MCCD) is identical to the MCD network with the exception that every normal dropout layer is replaced by a concrete dropout layer. For both the MCD and MCCD networks, 10 Monte-Carlo forward passes are performed. 
The Bootstrap neural network (BOOT) is based on the architecture described by [22]. It represents an efficient implementation of the bootstrap principle by sharing a set of hidden layers between all members of the ensemble. Our implementation consists of two fully-connected hidden layers with 64 neurons each, which are shared between all heads, followed by an output layer of K = 10 bootstrap heads. For each datapoint, a Boolean mask of length equal to the number of heads is generated, which determines the heads this datapoint is visible to. The mask’s values are set by drawing K times from a Bernoulli distribution with p = 0.2. The Bootstrap-Prior neural network (BOOTP) is based on the extension presented in [21]. It has the same basic architecture as the BOOT network but with the addition of a so-called random Prior Network. Predictions are generated by adding the output of this untrainable prior network to the output of the different bootstrap heads before calculating the loss. Osband et al. [21] conjecture that the addition of this randomized prior function outperforms ensemble-based methods without explicit priors, as for the latter, the initial weights have to act both as prior and training initializer. 
4 Results 
Figure 1 presents the average uncertainty of the chosen actions over 10000 training episodes of the different network architectures. As there is a certain amount of randomness in the evaluation runs, caused by the random placement of start and goal positions, the plots show averages of 30 evaluation runs. 
According to the concept of epistemic uncertainty, we would expect a decline in the absolute value of reported epistemic uncertainty in the train environment over the training process, as the agent collects more data. Interestingly, only the bootstrap-based methods (BOOT 1c and BOOTP 1d) reliably show this behaviour. The dropout-based methods do not show consistent behaviour in this regard. For these methods, the predicted uncertainty sometimes even increases along the training process as can be seen in Figure 1b. Regarding the OOD detection performance, the methods are required to predict higher epistemic uncertainty values for OOD samples than for in-distribution samples. Here also, the bootstrap-based methods outperform the dropout-based ones. For all bootstrap methods, over the complete training process, the predicted uncertainty values in the “out-of-distribution” mirror environment are higher than the values in the train environment. Consequently, it would be possible to detect the OOD samples reliably, for example by setting a threshold based on the lower uncertainty values predicted during training. Figure 1d shows that the addition of a prior has a positive effect on the separation of in- and out-of-distribution samples, as the distance between the predicted uncertainty values increases. 
Our results for the dropout-based techniques are not as positive. As can be seen in Figure 1a and 1b, neither of the tested Monte-Carlo dropout methods consistenly outputs higher uncertainty values for the OOD states of the mirror environment over the complete training process. Although there are episodes, especially in the beginning, where the mirror environment’s uncertainty values are higher, there is a reversal during the training process. As a consequence, it would not be possible to reliably differentiate between in- and out-of-distribution samples at every point in time. 
3
0 2000 4000 6000 8000 10000 
episode 
10 3 
10 2 
10 1 
100 
101 
102 
un ce 
rta in 
ty 
train mirror 
(a) MCD 
0 2000 4000 6000 8000 10000 
episode 
10 3 
10 2 
10 1 
100 
101 
102 
un ce 
rta in 
ty 
train mirror 
(b) MCCD 
0 2000 4000 6000 8000 10000 
episode 
10 3 
10 2 
10 1 
100 
101 
102 
un ce 
rta in 
ty 
train mirror 
(c) BOOT 
0 2000 4000 6000 8000 10000 
episode 
10 3 
10 2 
10 1 
100 
101 
102 
un ce 
rta in 
ty 
train mirror 
(d) BOOTP 
Figure 1: Per-episode mean uncertainty of chosen actions, averages of 30 runs (y-axis log-scaled). 
5 Discussion and Future Work 
The results we obtained from the bootstrap-based methods show the general feasibility of our approach, as they allow for a reliable differentiation between in- and out-of-distribution samples in the evaluated environments. Declining uncertainty values over the training process also conform to the expectation that epistemic uncertainty can be reduced by collecting more data. For the dropout-based techniques, it remains to be seen if our results show a general problem of these methods in sequential decision problems, or whether the results are a consequence of our specific environments. According to Osband et al. [21] the observed behaviour is to be expected for the basic Monte-Carlo dropout method (MCD) as the dropout distribution does not concentrate with observed data. Consequently, we expected different results from the concrete dropout method (MCCD) as it should be able to adapt to the training data. Nevertheless, this did not lead to decreasing uncertainty estimates over the training process or a reliable prediction of higher uncertainty for OOD samples. We are currently working on extending our evaluations to more environments in order to evaluate if these results generalize. This will include stochastic domains, where it is necessary to differentiate between aleatoric and epistemic uncertainty in order to correctly detect OOD samples. It will also be very interesting to compare the performance of the proposed uncertainty based methods to methods based on generative models. Another interesting aspect which could further improve the OOD detection performance of the ensemble methods is the choice of prior [10] and a newly proposed method called Bayesian Ensembling [23], which could bridge the gap between fully Bayesian methods and ensembling methods. 
4
References [1] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané. Concrete Problems 
in AI Safety. ArXiv e-prints, June 2016. 
[2] C. M. Bishop. Novelty detection and neural network validation. IEE Proceedings - Vision, Image and Signal Processing, 141(4):217–222, Aug 1994. ISSN 1350-245X. doi: 10.1049/ip-vis: 19941330. 
[3] C. Blundell, J. Cornebise, K. Kavukcuoglu, and D. Wierstra. Weight Uncertainty in Neural Networks. ArXiv e-prints, May 2015. 
[4] Yaroslav Bulatov. Notmnist dataset. Google (Books/OCR), Tech. Rep.[Online]. Available: http://yaroslavvb. blogspot. it/2011/09/notmnist-dataset. html, 2011. 
[5] S. Depeweg, J. M. Hernández-Lobato, F. Doshi-Velez, and S. Udluft. Learning and Policy Search in Stochastic Dynamical Systems with Bayesian Neural Networks. ArXiv e-prints, May 2016. 
[6] Bradley Efron. Bootstrap Methods: Another Look at the Jackknife, pages 569–593. Springer New York, New York, NY, 1992. ISBN 978-1-4612-4380-9. doi: 10.1007/978-1-4612-4380-9_ 41. 
[7] Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In international conference on machine learning, pages 1050–1059, 2016. 
[8] Yarin Gal, Jiri Hron, and Alex Kendall. Concrete dropout. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems 30, pages 3581–3590. Curran Associates, Inc., 2017. 
[9] Alex Graves. Practical variational inference for neural networks. In J. Shawe-Taylor, R. S. Zemel, P. L. Bartlett, F. Pereira, and K. Q. Weinberger, editors, Advances in Neural Information Processing Systems 24, pages 2348–2356. Curran Associates, Inc., 2011. 
[10] D. Hafner, D. Tran, A. Irpan, T. Lillicrap, and J. Davidson. Reliable Uncertainty Estimates in Deep Neural Networks using Noise Contrastive Priors. ArXiv e-prints, July 2018. 
[11] D. Hendrycks and K. Gimpel. A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks. ArXiv e-prints, October 2016. 
[12] J. M. Hernández-Lobato and R. P. Adams. Probabilistic Backpropagation for Scalable Learning of Bayesian Neural Networks. ArXiv e-prints, February 2015. 
[13] JM Hernández-Lobato, Y Li, M Rowland, D Hernández-Lobato, TD Bui, and RE Ttarner. Black-box α-divergence minimization. In 33rd International Conference on Machine Learning, ICML 2016, volume 4, pages 2256–2273, 2016. 
[14] Alex Kendall and Yarin Gal. What uncertainties do we need in bayesian deep learning for computer vision? In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vish-wanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems 30, pages 5574–5584. Curran Associates, Inc., 2017. 
[15] Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Informa-tion Processing Systems 30, pages 6402–6413. Curran Associates, Inc., 2017. 
[16] Christian Leibig, Vaneeda Allken, Murat Seçkin Ayhan, Philipp Berens, and Siegfried Wahl. Leveraging uncertainty information from deep neural networks for disease detection. Scientific reports, 7(1):17816, 2017. 
[17] Y. Li and Y. Gal. Dropout Inference in Bayesian Neural Networks with Alpha-divergences. ArXiv e-prints, March 2017. 
5
[18] S. Liang, Y. Li, and R. Srikant. Enhancing The Reliability of Out-of-distribution Image Detection in Neural Networks. ArXiv e-prints, June 2017. 
[19] David J. C. MacKay. A practical bayesian framework for backpropagation networks. Neural Computation, 4:448–472, 1992. 
[20] V. Mnih, K. Kavukcuoglu, D. Silver, A. Graves, I. Antonoglou, D. Wierstra, and M. Riedmiller. Playing Atari with Deep Reinforcement Learning. ArXiv e-prints, December 2013. 
[21] I. Osband, J. Aslanides, and A. Cassirer. Randomized Prior Functions for Deep Reinforcement Learning. ArXiv e-prints, June 2018. 
[22] Ian Osband, Charles Blundell, Alexander Pritzel, and Benjamin Van Roy. Deep exploration via bootstrapped dqn. In D. D. Lee, M. Sugiyama, U. V. Luxburg, I. Guyon, and R. Garnett, editors, Advances in Neural Information Processing Systems 29, pages 4026–4034. Curran Associates, Inc., 2016. 
[23] T. Pearce, M. Zaki, A. Brintrup, and A. Neel. Uncertainty in Neural Networks: Bayesian Ensembling. ArXiv e-prints, October 2018. 
[24] Marco A.F. Pimentel, David A. Clifton, Lei Clifton, and Lionel Tarassenko. A review of novelty detection. Signal Processing, 99:215 – 249, 2014. ISSN 0165-1684. doi: https: //doi.org/10.1016/j.sigpro.2013.12.026. 
[25] Cazhaow S. Qazaz. Bayesian error bars for regression. PhD thesis, Aston University, 1996. 
[26] Thomas Schlegl, Philipp Seeböck, Sebastian M. Waldstein, Ursula Schmidt-Erfurth, and Georg Langs. Unsupervised anomaly detection with generative adversarial networks to guide marker discovery. In IPMI, 2017. 
6