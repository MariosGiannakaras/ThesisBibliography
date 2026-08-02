> Source: https://optimization-online.org/wp-content/uploads/2023/04/MPOMDP_INFORMS_JOC_OptOnline_copy-2.pdf

Multi-model Partially Observable Markov Decision Processes 
Weiyu Lia, Brian T. Dentona,⇤ 
a Department of Industrial and Operations Engineering, University of Michigan, 1205 Beal Avenue, Ann Arbor, MI 
48109, USA 
Abstract 
We propose a new multi-model partially observable Markov decision process (MPOMDP) model 
to address the issue of model ambiguity in partially observable Markov decision process. Here, 
model ambiguity is defined as the case where there are multiple credible optimization models with 
the same structure but different model parameters. The proposed MPOMDP model aims to learn 
the distribution of the true model from system outputs over time, and to find the single optimal 
policy that maximizes the expected sum of all future rewards in all possible models. We discuss 
important structural properties of the proposed MPOMDP model, which not only reveal the benefit 
of the MPOMDP model by accounting for model ambiguity, but also motivate solution methods for 
MPOMDP. We develop an exact solution method, and two approximation methods that are shown 
to converge asymptotically, and compare their performance in computational experiments. Lastly, 
we use a case study of prostate cancer active surveillance to demonstrate how the MPOMDP model 
can be applied to a real-world problem to improve medical decision-making by created policies that 
are robust to different parameters in the multiple plausible models. 
Keywords: multi-model partially observable Markov decision processes, stochastic optimization, 
model ambiguity, prostate cancer active surveillance 
1. Introduction 
Partially observable Markov decision process (POMDP) has been found successful in many 
problems, including machine maintenance, robot navigation, healthcare, and others (see Cassandra 
(1998) for a survey). This paper addresses the issue of model ambiguity in POMDP models defined 
as follows. In a POMDP model, the decision-maker can take actions to influence the transition 
dynamic, output, and reward from the system, such that the expectation of all future rewards is 
⇤Corresponding author Email addresses: weiyuli@umich.edu (Weiyu Li), btdenton@umich.edu (Brian T. Denton)
maximized. The transition, observation, and reward dynamics of a POMDP model are described 
by its model parameters. In practice, these model parameters are often estimated by pre-studies 
that fit models on historical observational data. A potential issue of this approach is that different 
studies can give different estimates of the model parameters. The difference in parameter estimates 
can arise from differences in the underlying study samples, study designs, model formulations, or 
other factors. In this study, we call it the issue of model ambiguity in POMDP models. 
In this paper, we propose a new multi-model partially observable Markov decision process 
(MPOMDP) model to tackle the issue of model ambiguity. An MPOMDP model is a stochas-
tic optimization and dynamic programming model that simultaneously considers multiple POMDP 
models, which have the same model structure but different model parameters. The goal is to find 
a single optimal policy that adaptively optimizes a “weighted” average of the value functions of 
all POMDPs. The model weight is given by the model belief vector, which can be interpreted as 
the importance and/or the probability of being the true model for each POMDP model, and is 
learned every time using the information from system outputs. In particular, even if none of the 
POMDPs considered in the MPOMDP is the true model for the study object, the learned belief 
is still guaranteed to assign a higher weight to the model with a greater probability of generating 
the observed outputs. Traditionally, when it comes to the issue of model ambiguity, a decision-
maker may randomly pick a single model, take the average of multiple sets of model parameters, 
or conservatively consider a max-min model address the worst-case performance. In this study, we 
will show that the proposed MPOMDP model outperforms the traditional methods by achieving 
a non-negligible value of the stochastic solution (VSS) as defined in Birge (1982). Our study also 
sheds light on the expected value of perfect information (EVPI) (Schlaifer & Raiffa, 1961), which 
may be relevant in situations where there are opportunities to collect additional information to 
resolve model uncertainty. 
We describe several important properties of the proposed MPOMDP model, which give insights 
into the model and motivate fast approximation methods we propose to solve the MPOMDP model. 
First, we show that an MPOMDP model can be reformulated as a special-case of the POMDP model, 
with an enlarged state space, thus inheriting many properties of the standard POMDP. Next, we 
discuss the existence and structure of the optimal policy of an MPOMDP model. Then, we describe 
solution methods that exploit properties of the model. Finally, we provide examples to illustrate 
the practical benefits of the proposed MPOMDP model. 
The work of this paper is motivated by a healthcare application in prostate cancer active surveil-
2
lance (AS), which will be discussed in detail in Section 6. A pre-study by Li et al. (2023) developed 
a POMDP model to find the optimal timing for biopsies in prostate cancer AS, such that the burden 
of biopsy and the delay in detecting cancer progression are minimized. Their work in Li et al. (2020) 
first estimated the cancer progression rates, biopsy under-sampling errors, and PSA distributions 
using an HMM in four major prostate cancer AS studies in the world, which include the JH hos-
pital, the UCSF medical center, the U of T medical center, and the PRIAS project. The study 
showed the model parameters to be statistically significantly different across studies. Motivated by 
this discrepancy, we consider the case of a new patient or new study for which the true model is 
unknown. We use computational experiments in Section 6 to show that our proposed MPOMDP 
model can find a single policy with the same complexity as the one given by a POMDP model, that 
achieves better overall performance based on clinical outcomes. 
Our proposed MPOMDP model in this paper will mainly focus on the finite-horizon problem for 
several reasons. First, finite-horizon models are preferred over infinite-horizon models in healthcare 
applications and other applications where the survival time (length of decision epochs) can not be 
infinite and the model parameter can be non-stationary. Second, although a finite-horizon POMDP 
model can be easily reformulated as an infinite-horizon POMDP model by appending the time index 
to the state definition, it does not automatically solve the problem as the computational complexity 
would increase along with the size of the state space. 
The rest of this article is organized as follows. In Section 2, we review the most related work in 
stochastic sequential decision-making under uncertainty and with model ambiguity, and summarize 
the main contribution of this work. In Section 3, we formally define the MPOMDP model. Next, 
in Section 4, we discuss some important structural properties of the MPOMDP. In Section 5, we 
present solution methods tailored to the MPOMDP model. We present the results of a toy example 
to demonstrate the computational properties of the proposed methods and a detailed case study of 
prostate cancer AS in Section 6. Finally, we conclude with a discussion of potential future research 
in Section 7. 
2. Literature Review 
In this section, we first review the most closely related work in sequential decision-making under 
uncertainty and model ambiguity. Then, we describe the main contributions of this paper with 
respect to the related literature. 
The POMDP was first introduced by Åström (1965); Drake (1962) and Smallwood & Sondik 
3
(1973). The POMDP model is a dynamic programming model for sequential decision-making, 
where the underlying system can be described by a hidden Markov model (HMM) (Rabiner & 
Juang, 1986). The objective of a POMDP model is to find the policy for actions to take at all time 
periods, such that the optimal cumulative reward is achieved. On the one hand, the POMDP model 
subsumes the HMM in that it adds decision-making about what action to take at each time period, 
which will influence the transition, output, and reward dynamics of the system. On the other hand, 
the POMDP model is a generalization of the Markov decision process (MDP) model (Puterman, 
2014), where the underlying state is not observable and can only be inferred by the output of the 
system. POMDP models have found success in many problems, including machine maintenance 
(Ross, 1971), robot navigation (Cassandra et al., 1996), healthcare (Ayer et al., 2012; Zhang et al., 
2012; Erenay et al., 2014), and many others (see Cassandra (1998) for a survey). 
When applying the POMDP model to real-world problems, it is necessary to estimate model 
parameters that include the initial distribution function, transition probabilities, observation prob-
abilities, and reward function. However, the estimation error and heterogeneity between different 
studies can induce ambiguity in the underlying HMM model. Li et al. (2023) used POMDP mod-
els to optimize AS strategies in prostate cancer, and showed that the optimal policies could vary 
considerably in different medical studies because of the difference in system dynamics revealed by 
model parameters. 
Saghafian (2018) proposed an ambiguous POMDP (APOMDP) model to address the issue of 
model ambiguity in the POMDP model. Boloori et al. (2020) then applied the APOMDP model in 
a study of post-transplant medication management, which improved the existing policies by consid-
ering variability among physicians’ attitudes toward ambiguous outcomes and patients’ progression 
dynamics. In contrast to the work in this article, in their proposed APOMDP model, the objec-
tive function is in a robust optimization setting, which weights the best-case and worst-case value 
functions across different sets of model parameters. Moreover, they assumed that the best and 
worst models were selected independently over time, which might violate the Markov property and 
induce inconsistency in model dynamics across decision epochs. Nakao et al. (2021) described a 
distributionally robust Partially Observable Markov Decision Process (DR-POMDP), which esti-
mates the distribution of the transition-observation probabilities using side information at the end 
of each time period, to maximize the worst-case reward for any joint-distribution of the ambiguous 
model parameters. In contrast, the study in this article seeks a single optimal policy that works well 
“on average", rather than optimizing the worst-case performance, when there are multiple credible 
4
POMDP models. 
Despite the short history of the study of model ambiguity in POMDP models, there has been a 
stream of research on model ambiguity in MDP models over the last two decades. Nilim & El Ghaoui 
(2005) and Iyengar (2005) considered a robust formulation of an MDP to optimize the worst-case 
performance (referred to as the “max-min" problem) of the model, while assuming a “rectangular-
ity" property in ambiguity sets, i.e., the ambiguity in transition probabilities is independent with 
action, state, or time. They discussed the policy evaluation and other improved solution methods 
to the proposed robust MDP. Followed by their study, much of the research has focused on ways to 
construct ambiguity sets, to mitigate the rectangularity assumption on the ambiguity set, and to 
generalize the “max-min" objective function (Delage & Mannor, 2010; Xu & Mannor, 2012; Wiese-
mann et al., 2013; Delage & Iancu, 2015; Mannor et al., 2016). In contrast to these studies, our 
work in this paper addresses the issue of model ambiguity in a different manner. The MPOMDP 
model we proposed considers a weighted sum of value functions under different sets of model pa-
rameters, where the objective is to find a single policy that performs well overall possible models. 
Compared with the robust optimization formulation, our MPOMDP finds a less conservative policy 
that achieves the maximum of a weighted (by model belief) value function instead of the maximum 
worst-case value function. 
The closest research to ours that we are aware of is that of Steimle et al. (2021), which formulated 
a multi-model Markov decision process (MMDP). They considered discrete ambiguity sets for the 
model parameters in MDPs with the objective of optimizing the weighted value function. They 
showed that any MMDP could be recast as a special case of a POMDP. Different from their study, 
our work in this paper considers a more complex setting of MPOMDP, where each single model is 
already a POMDP, so that we are encountered with much larger state and policy spaces (i.e., more 
severe curse of dimensionality and curse of history). 
To close this section, we describe the main contributions of this paper to the literature. Our 
article is the first work addressing the issue of model ambiguity under the POMDP framework 
using the MPOMDP. In contrast to the work by Saghafian (2018), Nakao et al. (2021), and related 
literature on robust MDPs, our model formulation considers the objective function to be a weighted 
sum of value functions given by the belief vector under different sets of model parameters. Our 
formulation allows inter-dependent model transition, observation, and reward dynamics over time. 
Moreover, it provides less conservative policies than the robust optimization formulation, which 
aims to optimize the worst-case performance. Second, we study the structural properties of the 
5
proposed MPOMDP, which not only motivate the solution methods, but also help analyze the 
effect of model ambiguity in POMDPs. Third, we describe an exact solution method, and two 
different approximation methods to our model that are shown to converge asymptotically and can 
provide near-optimal solutions in real-time. Finally, we present a case study for prostate cancer AS 
optimization, which illustrates how the MPOMDP can be applied in a real-world problem, and the 
benefit of the MPOMDP in stochastic sequential decision-making under model ambiguity. 
3. Model Formulation 
We start with a review of the formal definition of the POMDP, and then introduce the MPOMDP, 
which generalizes the POMDP for model ambiguity. 
3.1. POMDP Definition 
The POMDP model can be defined as follows: 
Definition. A finite-horizon POMDP model M can be defined by a tuple 
(S, b0, A, P,O, F, r, T ), 
where S is the set of all states, b0 is the initial distribution function over the set of states S, A 
is the set of all actions, P : S ⇥ A ⇥ S ! [0, 1] is the state transition probability distribution, O 
is the set of all observations, F : S ⇥ A ⇥ O ! [0, 1] is the observation probability distribution, 
r : S ⇥A⇥O ! R is the reward function, and T is the length of time horizon. 
Notice that in Definition 3.1, the state transition probability distribution, observation probability 
distribution, and the reward function are all stationary, i.e., independent of time. The definition 
of a non-stationary model can be easily adapted using time-dependent model parameters in finite-
horizon POMDP formulation. 
POMDP models are widely used to solve stochastic sequential decision-making problems with 
partially observable states. In a finite-horizon POMDP model, we can use t = 0, 1, ..., T to denote 
its discrete time periods (also referred to as decision epochs), and bt to denote the probability 
distribution over S (also referred to as a belief vector) at time t  T . Then, given a policy 
⇡ = (⇡0, ...,⇡T ), where each ⇡t is a mapping from the space of the belief vector to A specifying the 
action to choose for all possible belief states at time t, the value function of the policy ⇡ starting 
from belief state b at time t is defined as 
V ⇡ 
t (bt) := E⇡[ TX 
k=t 
  t k 
r(sk, ak, ok)|bt], 8bt, 8t  T, 
6
where   2 [0, 1] is a discount factor that diminishes the future rewards, sk, ak, and ok are the 
state, action, and observation at time k  T , and the expectation is taken over all possible state, 
action, and observation trajectories following the policy ⇡. Solving a POMDP model is equivalent 
to finding the optimal policy ⇡ ⇤ t , which achieves the maximum of the value function at any time t: 
⇡ ⇤ t := argmax 
⇡ V 
⇡ ⇤ 
t (bt), 8bt, 8t. 
3.2. MPOMDP Definition 
The issue of model ambiguity motivates the formulation of the MPOMDP. Suppose there are 
M (M < 1) different POMDP models, where all models share the same state space, action space, 
and observation space, but may have different model parameters of initial distribution functions, 
transition probability and observation probability matrices, or reward functions. We assume that 
any of the models could be the “true” model describing the underlying stochastic system to study. 
However, we are unable to pick a single model because of the lack of information on the true 
model. The way the MPOMDP model tackles this issue is to consider all different POMDP models 
simultaneously by assigning a weight to the objective function of each POMDP model according to 
a belief vector introduced later. The model learns and updates the weights (belief vector) as the 
system progresses, to optimize the weighted sum of the objective functions of all POMDP models. 
A formal definition of the MPOMDP model is given as follows. 
Definition. An MPOMDP model M is defined as a tuple (M1, ...,MM , ), where M is the number 
of POMDPs, each Mm = (S, bm0 , A, P m , O, F 
m , r 
m , T ) is a POMDP model as defined in Definition 
3.1 for m = 1, ...,M , and   = ( 1, ..., M ) is a vector of the initial model weights for all M POMDP 
models such that 
 m 2 (0, 1), 8m = 1, ...,M, and MX 
m=1 
 m = 1. 
The initial weight parameter vector   in Definition 3.2, can be viewed as a vector with ele-
ments  m that are the probability that the model Mm is the true model describing the underlying 
stochastic system to study at the starting time, for m = 1, ...,M . The initial   vector is usually 
given by some prior knowledge about the relative importance or preference of each model, or set as 
a non-informative prior distribution. Then, every time a system output is observed, the model and 
state probability distributions are updated. The notion of a belief vector will arise often and can 
be defined as follows: 
7
Definition. (Belief Vector) For an MPOMDP model M, the belief vector bt of M at time t is 
defined as 
bt := (b1t , ..., b M 
t ), 
where each element is itself a vector 
b t 
m = (btm(s1), ..., b t 
m(s|S|)), 
and each b m t (sk) is the probability that the underlying model of the stochastic system is model 
Mm and the system is in state sk at time t, for m = 1, ...,M , t = 1, ..., T , and all state sk 2 S. 
Specifically, at t = 0, the initial belief vector of M is defined as 
b0 := (b10, ..., b M 
0 )    , 
where b 1 0, ..., b 
M 0 are the initial belief vectors for models M1, ...,MM respectively,   is the initial 
belief weight, and   denotes the Hadamard product. 
To define the optimal value problem in an MPOMDP model M, we first describe the process 
flow. Initially, the underlying system is true described by one of the given POMDP models, and 
is in one of the states in the state space. However, the decision-maker knows neither which of the 
given POMDP models is the true model nor the state of the system. Instead, the decision-maker 
obtains an initial weight parameter   in advance based on prior knowledge and the estimate of 
the initial belief vector (i.e., the probability distribution over states) in each model. Then, at the 
beginning of each time period, with the estimate of the belief vector of the MPOMDP model, the 
decision-maker can take action to influence the dynamics of the underlying system. The system then 
generates an output according to the chosen action, the state of the system, and the observation 
probability function of the actual underlying POMDP model. To select an action, the decision-
maker approximates the observation probabilities by an adjusted observation probability function 
using the model belief, which will be discussed in detail in the next section. After observing the 
output, the immediate reward for each POMDP is computed according to the estimate of state 
distribution, the action taken, the output from the system, and its reward function. Lastly, the 
MPOMDP belief vector is updated. The objective of the MPOMDP is to optimize the expectation 
of the sum of the immediate rewards under all possible POMDPs until the end of the time horizon, 
according to estimated believes. Figure 1 illustrates the process flow of the optimal value problem 
in an MPOMDP. 
We now define the optimal value problem of an MPOMDP model M as follows. 
8
Figure 1: Illustration of the process flow of the optimal value problem in an MPOMDP. 
Definition. (Optimal Value Problem) For an MPOMDP model M, the optimal value problem 
entails finding the optimal policy ⇡ ⇤ = (⇡⇤ 
0, ...,⇡ ⇤ T ) that achieves the maximum value function 
defined as follows: 
V ⇡ ⇤ 
t (bt) := max ⇡ 
MX 
m=1 
V m,⇡ 
t (bmt ), 8b, 8t, 
where bt = (b1t , ..., b M t ), bmt is the belief vector in Mm, and V 
m,⇡ 
t (bmt ) is the value function of policy 
⇡ in Mm defined as 
V m,⇡ 
t (bmt ) := Em,⇡[ 
TX 
k=t 
  t k 
r m(sk, ak, ok)|bmt ], 8bmt , 8t  T, 
with the expectation taken over all possible state, action, and observation trajectories following 
policy ⇡ in model Mm for m = 1, ...,M . 
In Definition 3.2, the optimal value problem of an MPOMDP model M is defined upon the 
initial weight parameter vector  , which is pre-specified in the definition of M. The initial weight 
parameter vector   is integrated into the MPOMDP belief vector since time t = 1, as defined in 
Definition 3.2, so that we do not need to add duplicate weights in the value functions definition in 
Definition 3.2. 
Starting from here, we will drop the subscript t of bt in V ⇡ t (bt) when there is no confusion that 
V ⇡ t is the value function at time t  T . We also substitute V 
⇡ ⇤ 
t by V ⇤ t , or even by Vt, for all t  T 
as a simplification if there is no confusion. 
4. Model Properties 
In this section, we discuss some structural properties of the proposed MPOMDP, which show 
how the model addresses the issue of model ambiguity in stochastic sequential decision-making, 
9
and motivate the solution methods introduced in the next section. We first provide the adjusted 
observation probability function and the belief update formula for the optimal value problem of 
an MPOMDP mentioned in Section 3.2. Then, we show that the optimal value problem of an 
MPOMDP can be reformulated as a new POMDP model with a larger state space, confirming that 
all properties of POMDP models will hold. 
We first calculate the observation probability with respect to the belief vector in the optimal 
value problem. At each epoch, although the system output is generated according to the state, 
action, and observation probability function, the true underlying model is hidden from the decision 
maker. The formula below provides a method to calculate the probability of observing a certain 
observation, and guide decision-making. 
Definition. Given an MPOMDP model M, consider its optimal value problem defined in Definition 
3.2. Then, at any time t   T , given the belief vector b, the probability of observing output o when 
action a is taken is 
P(o|b, a) : = X 
s2S,m=1,...,M 
P(o, (s,m)|b, a) 
= X 
s2S,m=1,...,M 
P((s,m)|b, a)P(o|(s,m), b, a) 
= X 
s2S,m=1,...,M 
b m(s)Fm(s, a, o), 
(1) 
for all o 2 O, belief vector b, and a 2 A. 
Given the observation probability of the optimal value problem, we can then show that the belief 
vector of the MPOMDP model is a sufficient statistic for decision-making at each time period. This 
property is important because it implies that the distribution over the states at each time period 
does not require all historical information of actions and observations. 
Proposition 1. Given an MPOMDP model M, consider its optimal value problem defined in Def-
inition 3.2. Then, the belief vector bt defined in Definition 3.2 is a sufficient statistic of the past 
sequence of actions and observations until time t for t = 0, 1, ..., T . 
We can now provide the belief update formula after taking action and observing an output at 
each time period in an MPOMDP model. 
Proposition 2. Consider the optimal value problem of an MPOMDP model M. Suppose bt = 
(b1t , ..., b M t ) is the belief vector of M at the beginning of time t, and observation o is observed after 
10
taking action a, then the belief vector bt+1 = (b1 t+1, ..., b 
M t+1) of M at the time t+ 1 is given by 
P((st+1,mt+1)|o, b, a) = P 
st F 
mt+1(st, a, o)Pmt+1(st+1, a, st)bmt+1(st) 
P st+1,mt+1 
P st Fmt+1(st, a, o)Pmt+1(st+1, a, st)bmt+1(st) 
. 
For simplicity, we use bt+1 = ⇤(bt|a, o) to denote the belief update formula given action a and 
observation o at time t for t = 0, 1, ..., T   1. 
The proofs of Proposition 1 and 2 are shown in Appendix. 
Remark 1. In Proposition 2, the belief vector is updated by the Bayesian formula, which calculates 
a posterior distribution over models and states. Even if none of the POMDPs considered in the 
MPOMDP is the true model for the study object, the belief update formula in Proposition 2 still 
assigns a higher weight to the model with a greater probability of generating the observed outputs. 
Proposition 2 shows that the MPOMDP model is able to learn the model distribution over time 
from past actions and observations. Propositions 1 and 2 also show that, an MPOMDP can be 
viewed as a POMDP, or continuous-state MDP, when solving the optimal value problem, where the 
state is specified by the belief vector of the MPOMDP model. The state transition probabilities 
can be calculated by Proposition 2. Although the dimensionality of the state in such POMDP can 
be extremely high, it helps understand the structure of the MPOMDP. For example, it immediately 
proves the existence of a deterministic and Markovian optimal policy for the optimal value problem 
of an MPOMDP, as shown in the following corollary. 
Corollary 1. When considering the optimal value problem defined in Definition 3.2, an MPOMDP 
model can be reformulated as a POMDP model. Therefore, the MPOMDP inherits properties of 
POMDPs, including that there always exists an optimal policy that is deterministic and Markovian 
with respect to the belief vector at each time period. 
It follows from Corollary 1 that the MPOMDP model inherits the properties of the POMDP 
model, including that the optimal value problem is piecewise linear and convex, which will be used 
as the basis for the solution methods in the next section. Moreover, Corollary 1 serves as the 
basis for understanding the effect of model ambiguity in POMDPs. Later in Section 6, we will 
use computation experiments to demonstrate the effect of model ambiguity on the optimal value 
function and policy, and the corresponding VSS and EPVI in each example. We refer the audiences 
to Chapter 4.4 of Li (2021) for the proof of non-negative VSS and EPVI in MPOMDPs. 
11
5. Solution Methods 
In this section, we discuss solution methods for the proposed MPOMDP model. We start with 
an exact solution method, which generalizes the one-pass algorithm by Smallwood & Sondik (1973) 
for POMDP models. However, because of the curse of dimensionality and the curse of history, 
the exact solution method can take a long time to complete, even for small problems. Therefore, 
we introduce two approximation methods that can get near-optimal solutions efficiently. We also 
prove that the proposed approximation methods converge asymptotically. Finally, we compare the 
performance of the approximation methods in the next section. 
5.1. Optimal value function and exact solution method 
Consider an MPOMDP model M, we can denote Vt as its optimal value function at any time t. 
Recall the recursion formula, i.e., the optimality equation, of the value function 
Vt(b) = max a2A 
{r(b, a) + X 
o2O P(o|b, a)Vt+1(⇤(b|a, o))}, 8b, 8t, 
with the boundary condition 
VT (b) = max a2A 
r(b, a), 
where 
r(b, a) = X 
o2O 
X 
m 
X 
s2S P(o|b, a)rm(s, a, o)bm(s) 
is the expected immediate reward, P(o|b, a) is the observation probability of output o, and ⇤(b|a, o)) 
is the belief update formula provided by Proposition 2, given the current belief vector b and action 
a is taken for all possible beliefs b and actions a. 
It follows from Corollary 1 that the optimal value function of an MPOMDP model M is 
piecewise-linear and convex in the belief vector b, and can be written as 
Vt(b) = max ↵2At 
↵ · b, 8b, 
where At is a set of |S|⇥M -dimension vectors (also referred to as ↵-vectors) for all time periods t. 
Given this property, solving the optimal value problem of M is equivalent to finding the minimal 
↵-vector sets At for all time periods t. This can be done by backward induction with a linear 
programming-based pruning algorithm for non-dominated ↵-vectors, which is a generalization of 
the solution method for POMDPs. We refer the audiences to Chapter 4.5 of Li (2021) for the 
detailed steps of the exact solution method for MPOMDPs. The reminder of this section will focus 
on the more practical approximation methods for MPOMDPs. 
12
5.2. Sampling-based approximation methods 
Although the value function is a continuous function of the belief vector, there are only a finite 
number of reachable belief vectors at each time period if starting from a certain initial belief at the 
first epoch. In other words, in order to find the optimal value function and the optimal policy of 
an MPOMDP model, it is sufficient to calculate the value function at all reachable belief vectors 
at each time period given a fixed initial belief vector. However, the number of reachable belief 
vectors increases exponentially in the number of possible actions, observations, and time periods. 
The ideal case is that we only need to know the value function at all reachable belief vectors under 
the optimal policy starting from the end of time horizon, and then use backward induction to 
calculate the optimal value function at all time periods. Unfortunately, the optimal policy can not 
be determined without knowing the optimal value function. 
As we showed, the optimal value function is piecewise-linear and convex, and can be represented 
by the supremum of a set of linear functions (↵-vectors). Using this property, if one can identify 
the dominating ↵-vectors at some sampled reachable belief vectors, then their supremum also gives 
a lower bound approximation of the optimal value function over the entire belief vector space. 
We leverage this fact to propose two sampling-based approximation methods for the proposed 
MPOMDP model. The first method uses ✏-greedy sampling to balance exploitation and exploration 
of the reachable belief points based on the most recent estimate of the optimal value function. This 
is motivated by the ✏-greedy algorithm for reinforcement learning problems as discussed in Sutton 
& Barto (2018). The second method is a tree-based branch-and-bound method, which seeks to 
improve the sampling efficiency of the ✏-greedy method by branching to the belief vector where the 
most recent estimate has the largest error at each time period. 
5.2.1. An ✏-greedy sampling method 
Denote M as the MPOMDP model to solve. To initialize, we sample a uniform grid of the entire 
space of the belief vector at each time period: 
B 0 t = {0, 1 
N , 2 
N , ..., 1}M ⇢ [0, 1]M , 8t = 1, ..., T, 
where the superscript of B0 t denotes the number of iterations (includes 0), N controls the number 
of belief vectors and density of the uniform grid. With a finite set of grid points, an approximate 
backward induction works as follows. First, at the end of time horizon T , similar to Section 5.1, we 
calculate the set of ↵-vectors as 
AT = {(↵1 T,a, ...,↵ 
M 
T,a)|a 2 A}, 
13
where 
↵ m 
T,a(s) = X 
o2O r m(s, a, o)Fm(s, a, o), 8m, 8a, 8s. 
Now, instead of keeping all ↵-vectors in AT , we only keep the ones that are non-dominated at the 
belief vectors in B 0 T , which gives ÂT 
ÂT := {↵ 2 AT |↵ = argmax ↵ 
↵ · b for some b 2 B 0 T }. 
Since ÂT ⇢ At, then V̂T defined as 
V̂T (b) := max ↵2ÂT 
↵ · b, 8b 
gives a lower bound estimate of the optimal value function VT at time T . Next, we go backward 
to time T   1. As described in Section 5.1, we can calculate the ↵-vectors at time T   1 using the 
optimality equation (1). But here, instead of using AT , we only use its subset ÂT to derive the set 
of ↵-vectors at time T   1, denoted as ÃT 1. It is easy to see that ÃT 1 is a subset of AT 1, which 
is the set of all ↵-vectors at time T   1 if using AT other than ÂT in backward induction. Again, 
instead of keeping all elements in ÃT 1, we only keep the ones that are dominating at the belief 
vectors in B 0 T 1, which gives ÂT 1, 
ÂT 1 := {↵ 2 ÃT 1|↵ = argmax ↵ 
↵ · b for some b 2 B 0 T 1}. 
Since ÂT 1 ⇢ ÃT 1 ⇢ AT 1, then V̂T 1 defined as 
V̂T 1(b) := max ↵2ÂT 1 
↵ · b, 8b 
gives a lower bound estimate of the optimal value function VT 1 at time T   1. We continue 
backward following the steps above until time t = 0, which gives a lower bound on the optimal 
value function at all time periods V̂0, V̂1, ..., V̂T . 
The next step is to modify the grid of belief points B 0 1 , ..., B 
0 T 
to improve the estimates of value 
functions. Starting from time t = 0, denote b0 as the initial belief vector. The current estimate of 
the value function at time t = 1 is used to find the optimal action to take under the current optimal 
value function approximation at time t = 0, which is given by 
â = argmax a 
X 
m 
X 
s2S b m 
0 (s){rm(s, a) + X 
o2O 
X 
s02S  F (s, a, o)Pm(s, a, s0)V̂ m 
1 (⇤(bm0 |a, o))}. 
Notice that â may be sub-optimal, because it is selected using an approximation of the expected 
future value-to-go. Next, action â is selected with probability 1   ✏ and a randomly sampled 
14
alternative action with probability ✏, for some ✏ 2 (0, 1), to encourage the exploration of other 
actions that can potentially be better than â. After taking the selected action, denoted as a0, we 
then randomly sample an output of the system o0 according to the observation probability matrix 
F . Given the action a0 and observation o0, the belief vector at time t = 1 can be updated by 
b1 = ⇤(b0|a0, o0). 
We then add b1 into B 0 1 to get B1 
1 = B 0 1 [{b1}. Now starting from belief b1 at time t = 1, we repeat 
the steps above to sample the belief vectors b2, ..., bT until the end of time horizon T , and get the 
new sets B 1 t for t = 2, .., T . Collectively, the complete set of backward and forward steps is one 
iteration of the ✏-greedy sampling method. 
In the next iteration, we conduct the backward induction steps on the new belief vector set 
B 1 T , ..., B 
1 1 , and then sample the new belief vectors to get the new sets B2 
t for t = 1, .., T . We repeat 
these iterations until a stopping criterion is satisfied. For example, if the difference between the 
approximate value functions in two consecutive iterations is below some threshold. This completes 
the steps of our proposed approximation algorithm based on ✏-greedy sampling. We summarize the 
complete algorithm in Algorithm 1. 
As we can see from Algorithm 1, if we denote V̄ i t for all t as the lower bound estimates of the 
optimal value functions after the i th iteration, then V̄ 
i t is determined by the set of sampled belief 
vectors B i t, which is generated by random sampling, for each time t. Next, we show that the lower 
bound estimates V̄ i t converge to Vt in probability at all reachable belief vectors for all time periods 
t, as the number of iterations i goes to infinity. The proof is shown in the Appendix. 
Theorem 1. For a given MPOMDP model M, denote B̃t as the set of all reachable belief vectors 
at time t  T starting from the initial belief vector b0 under all possible policies for actions. Denote 
Vt as the optimal value function at time t  T , and V̂ i t as the lower bound estimate of the optimal 
value function at time t  T given by the i th 
iteration of Algorithm 1. Then for all t  T , for any 
b 2 B̃t, 
V̂ i 
t (b) ! Vt(b) in probability, as i ! 1. 
Although Theorem 1 shows that Algorithm 1 converges asymptotically to the optimal value 
function of the true underlying POMDP, we found through experimentation that the value function 
approximated at each iteration of Algorithm 1 is not monotone. In other words, the lower bound 
estimate of the optimal value function given by Algorithm 1 may not be monotone non-decreasing 
15
Algorithm 1: Approximation algorithm based on ✏-greedy sampling. Input : MPOMDP model M, ✏ 
Output: V̂t 
1 Initialize B 0 as a uniform grid and i = 0; 
2 repeat 
3 At time T , calculate AT ; 
4 ÂT = {↵ 2 AT |↵ = argmax↵ ↵ · b for some b 2 B i 
T }; 
5 V̂T = (b) = max ↵2ÂT 
↵ · b, 8b; 
6 for t = T   1, ..., 0 do 
7 Calculate the set of ↵-vectors Ãt at time t by backward induction using Ât+1; 
8 Ât = {↵ 2 Ãt|↵ = argmax↵ ↵ · b for some b 2 B i t} ; 
9 V̂t(b) = max ↵2Ât 
↵ · b, 8b; 
10 end 
11 for t = 0, ..., T   1 do 
12 â = argmaxa(r(a) + P 
o2O P(o|bt, a) ˆVt+1(⇤(bt|a, o))); 
13 at = 
8 >< 
>: 
ât, with probability 1  ✏ 
a random action, with probability ✏ 
; 
14 Sample an output ot according to bt and F ; 
15 bt+1 = ⇤(bt|at, ot); 
16 B i+1 t 
= B i t+1 [ {bt+1}; 
17 end 
18 i = i+ 1; 
19 until some stopping criterion; 
16
as we keep adding new reachable belief vectors to exploit. We use the following proposition to 
address this fact. The proof is by construction and given in the Appendix. 
Proposition 3. Denote V̂ i t as the lower bound estimate of the optimal value function at time t  T 
given by the i th 
iteration of Algorithm 1. Then, V̂ i t is not monotone non-decreasing in i. In other 
words, there may exists an MPOMDP model M such that 9t, 9b, 9i, 
V̂ i+1 t 
(b)  V̂ i 
t (b) < 0. 
We found that such non-monotone behavior could slow the rate of convergence of Algorithm 1. 
We experimented with modifications of Algorithm 1 to improve the convergence rate. For example, 
instead of using a fixed ✏, we tried to adaptively change the value of ✏ over iterations; we tried 
to sample multiple outputs and append more than one belief vector to the belief vector set in 
each iteration; we also tried to design a rule to remove some existing belief vectors in the belief 
vector set. However, we found the random sampling of system outputs is the greatest barrier to 
accelerating the convergence rate. Therefore, we propose another approximation algorithm that 
uses a branch-and-bound method to improve Algorithm 1 
5.2.2. A Tree-based branch-and-bound method 
Similar to the ✏-greedy sampling method discussed above, we initially create a uniform grid of 
the entire space of the belief vector at all time period B 0 t for t = 1, ..., T . Starting from the end of 
time horizon T , we first calculate AT as the set of all ↵-vectors, and ÂT as the set of ↵-vectors that 
are dominating at the belief vectors in B 0 T . With ÂT , V̂T gives a lower bound on VT . We use B 
0 T 
to derive an upper bound of VT at iteration 0 as follows. For each b 2 B 0 T , calculate vT (b) as 
vT (b) = max ↵2AT 
↵ · b, 
and define vT (B0 T ) as the set 
vT (B 0 T ) := {(b, vT (b))|b 2 B 
0 T }. 
Then, since VT is a piecewise-linear and convex function, vT (B0 T ) can be used to find an upper 
bound V̄T of VT by the following linear program, where for all belief vector b 2 B 0 T , 
V̄t(b, vT (B0 T )) := min  
P b02B0 
T  b0vT (b0) 
s.t. P 
b02B0 T  b0 = 1, 
 b0   0, 8b0 2 B 0 T 
P b02B0 
T  b0b 
0 = b. 
17
Next, at time T   1, similar to the procedure in Section 5.2.1, we use ÂT and V̂T to derive the 
lower bound estimate ÂT 1 and V̂T 1. For the upper bound estimate, for each b 2 B 0 T 1, calculate 
uT 1(b) as 
uT 1(b) = argmax a 
X 
m 
X 
s2S b m 
0 (s){rm(s, a) + X 
o2O 
X 
s02S  F (s, a, o)Pm(s, a, s0)V̄ m 
t (⇤(bm0 |a, o))}, 
and define uT 1(B0 T 1) as the set 
uT 1(B 0 T 1) := {(b, uT 1(b))|b 2 B 
0 T 1}. 
Then, since VT 1 is piecewise-linear and convex, the solution of V̄T 1(b, uT 1(B0 T 1))) gives an 
upper bound of VT 1(b) for all b. We can repeat these steps for time T   2, ..., 0 to get the lower 
bound estimates V̂T 2, ..., V̂0 and upper bound estimates V̄T 2, ..., V̄0. 
The next step is to modify the grid of belief vectors B0 1 , ..., B 
0 T . Starting from time t = 0, denote 
b0 as the initial belief vector. Similar to the ✏-greedy sampling method of Algorithm 1, find the 
currently best action ā given by 
ā = argmax a 
X 
m 
X 
s2S b m 
0 (s){rm(s, a) + X 
o2O 
X 
s02S  F (s, a, o)Pm(s, a, s0)V̄ m 
1 (⇤(bm0 |a, o))}, 
and take action a0 to be ā with probability 1  ✏ and a randomly sampled action with probability ✏, 
for some ✏ 2 (0, 1). After taking action a0, instead of randomly sampling a system output, in this 
case, we select o0 as follows 
o0 = argmax o2O 
(V̄1(⇤(b0|a0, o))  V̂1(⇤(b0|a0, o))). 
In other words, we select the system output where the current estimate of the value function has 
the largest error, so that it needs more exploitation in the next iteration. With a0 and o0, we then 
add the updated belief vector b1 = ⇤(b0|a0, o0) into B 0 1 to get B 
0 1 [ {b1}, and similarly get B 
1 t for 
t = 2, ..., T . 
In the next iteration, we repeat all the steps above to get new estimates of the lower and upper 
bound of the value function, and new belief sets until a stopping criterion is satisfied. The detailed 
steps of the branch-and-bound approximation method are given in Algorithm 2. Notice that at any 
node of the scenario tree, if there exists another node at the same level (observation or action node) 
whose lower bound value is greater than the upper bound value of this selected node, then this node 
can be pruned. Note that we did not put the pruning steps in Algorithm 2 for brevity. Rather, it 
is implicitly assumed the pruned node will not be selected in the future automatically. 
18
Algorithm 2: The tree-based branch-and-bound approximation method. Input : MPOMDP model M, ✏ 
Output: V̂t 
1 Initialize B 0 as a uniform grid and i = 0; 
2 repeat 
3 At time T , calculate AT ; 
4 ÂT = {↵ 2 AT |↵ = argmax↵ ↵ · b for some b 2 B i 
T }; 
5 vT (Bi 
T ) := {(b, vT (b))|b 2 B 
i 
T }; 
6 for t = T   1, ..., 0 do 
7 Calculate the set of ↵-vectors Ãt at time t by backward induction using Ât; 
8 Ât = {↵ 2 Ãt|↵ = argmax↵ ↵ · b for some b 2 B i t} ; 
9 V̂t(b) = max ↵2Ât 
↵ · b, 8b; 
10 ut(Bi t) := {(b, ut(b))|b 2 B 
i t}; 
11 V̄t(b) = V̄t(b, ut(Bi t)), 8b; 
12 end 
13 for t = 0, ..., T   1 do 
14 ā = argmaxa(r(a) + P 
o2O P(o|bt, a)V̄t+1(⇤(bt|a, o))); 
15 at = 
8 >< 
>: 
ā, with probability 1  ✏ 
a random action, with probability ✏ 
; 
16 ot = argmaxo2O(V̄t+1(⇤(bt|at, o))  V̂t+1(⇤(bt|at, o))).; 
17 bt+1 = ⇤(bt|at, ot); 
18 B i+1 t 
= B i t+1 [ {bt+1}; 
19 end 
20 i = i+ 1; 
21 until some stopping criterion; 
19
Algorithm 2 attempts to accelerate the convergence rate of Algorithm 1 by sampling the action 
with the greatest upper-bound estimate, and the observation with the largest gap between the 
upper-bound and lower-bound estimates. So, the asymptotic convergence of Algorithm 2 is given 
as a corollary of Theorem 1. 
Corollary 2. For a given MPOMDP model M, denote B̃t as the set of all reachable belief vectors at 
time t  T starting from the initial belief vector b0 following any policies. Denote Vt as the optimal 
value function at time t  T , and V̂ i t as the lower bound estimate of the optimal value function at 
time t  T given by the i th 
iteration of Algorithm 2. Then for all t  T , for any b 2 B̃t, 
V̂ i 
t (b) ! Vt(b) in probability, as i ! 1. 
There are two main differences between the ✏-greedy sampling method and the tree-based branch-
and-bound method introduced in this section. First, the branch-and-bound method samples the 
best action based on the current upper-bound, instead of the lower-bound, estimate of the value 
function at each time period. This can accelerate the convergence rate because exploiting a sub-
optimal action will give a smaller upper bound estimate of its value function, so that it will quickly 
become dominated by other actions in future steps; Second, the branch-and-bound method samples 
the system output at each time period according to the gap between the upper and lower bound 
estimates at the resulting belief vector. Thus, the algorithm tends to modify the belief space grid 
in areas with the biggest estimation error. However, a drawback of the branch-and-bound method 
is that it requires more computational effort for the upper bound estimate of the value function, 
which can be problematic when the number of sampled belief vectors becomes large. In practice, we 
use the branch-and-bound method to get a warm start, and then switch to the ✏-greedy sampling 
method. 
6. Computational Experiments 
In this section, we describe two computational experiments to illustrate the application of the 
proposed MPOMDP. The first experiment is a toy example with two POMDPs, which have two 
states, two observations, and two actions. We use this toy example to visualize the value function 
and optimal policy of the MPOMDP model. We also show the VSS and the EVPI in this context. 
Furthermore, we use the toy example to compare the performance of the two approximation methods 
introduced in Section 5. The second computational experiment is a case study in prostate cancer AS 
20
based on the POMDP models studied in Li et al. (2023). We use the proposed MPOMDP to find 
the optimal timing of biopsies in AS when the cancer progression rate and test accuracy are assumed 
to be uncertain because of the existence of multiple plausible selections of model parameters. 
6.1. A two-model toy example 
Suppose there are two POMDP models denoted as Mm = (S, b0, A, Pm , O, F 
m , r 
m , T ) for m = 
1, 2, which have the same state space, observation space, and action space 
S = {s1, s2}, O = {o1, o2}, A = {a1, a2} 
but the different transition and observation probabilities 
P 1(a1) = 
0 
@ 0.1 0.9 
0.9 0.1 
1 
AF 1(a1) = 
0 
@ 0.8 0.2 
0.2 0.8 
1 
A , 
P 1(a2) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
AF 1(a2) = 
0 
@ 0.7 0.3 
0.3 0.7 
1 
A , 
P 2(a1) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
AF 2(a1) = 
0 
@ 0.6 0.4 
0.4 0.6 
1 
A , 
P 2(a2) = 
0 
@ 0.1 0.9 
0.9 0.1 
1 
AF 2(a2) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
A 
and the reward function 
a1 : r(s1, a1, o1) = 2, r(s1, a1, o2) = 0, r(s2, a1, o1) = 0, r(s2, a1, o2) = 1 
a2 : r(s1, a2, o1) = 1, r(s1, a2, o2) = 0, r(s2, a2, o1) = 0, r(s2, a2, o2) = 2. 
with the time horizon t = 0, 1, 2, 3, 4, 5. 
We first solve the MPOMDP model using the exact solution method, and plot the exact value 
function. Figure 2 shows the value function V0(b) at time t = 0. Notice that the argument of the 
value function, which is the belief vector of the MPOMDP model, is a 4-dimension vector with three 
degrees of freedom. Thus, we plot V0(b) for various choices of b2(s1) to illustrate the 4-dimension 
function V0(b). As we can see from Figure 2, V0(b) is a piecewise linear and convex function in b. 
When the belief vector lies in the dark region, then the optimal action to take at time t = 0 will be 
a1; otherwise, if the belief vector lies in the light region, then the optimal action will be a2. 
21
Figure 2: The value function V0(b) at time t = 0 for various choices of b2(s1). V0(b) is a piecewise linear and convex 
function in b. When the belief vector lies in the dark region, then the optimal action to take at time t = 0 will be a1; 
otherwise, the optimal action will be a2 
.22
Belief vector b0 
Value of the optimal policy (Regret %) 
Model M1 Model M2 Mean-value model MPOMDP model Perfect info. 
(0.45, 0.05, 0.45, 0.05) 8.43 (9.52%) 7.81 (16.11%) 8.89 (4.55%) 9.08 (2.48%) 9.31 (0) 
(0.45, 0.05, 0.25, 0.25) 8.10 (14.04%) 7.93 (15.82%) 9.03 (4.11%) 9.05 (3.95%) 9.42 (0) 
(0.45, 0.05, 0.05, 0.45) 8.73 (8.40%) 8.03 (15.74%) 9.00 (5.54%) 9.18 (3.66%) 9.53 (0) 
(0.25, 0.25, 0.45, 0.05) 8.29 (9.57%) 8.37 (8.65%) 8.24 (10.10%) 8.88 (3.18%) 9.17 (0) 
(0.25, 0.25, 0.25, 0.25) 7.95 (14.28%) 8.46 (8.74%) 8.40 (9.42%) 8.95 (3.48%) 9.27 (0) 
(0.25, 0.25, 0.05, 0.45) 8.60 (8.25%) 8.57 (8.60%) 8.51 (9.24%) 9.06 (3.38%) 9.38 (0) 
(0.05, 0.45, 0.45, 0.05) 8.30 (9.65%) 8.86 (3.53%) 8.78 (4.40%) 9.07 (1.22%) 9.18 (0) 
(0.05, 0.45, 0.25, 0.25) 7.96 (14.32%) 8.97 (3.41%) 8.92 (3.96%) 9.16 (1.41%) 9.29 (0) 
(0.05, 0.45, 0.05, 0.45) 8.61 (8.39%) 9.12 (2.96%) 9.04 (3.80%) 9.27 (1.39%) 9.40 (0) 
Table 1: The value function V0 and the regrets at different initial belief vectors when applying different policies. 
The optimal policy of the MPOMDP model M dominates the optimal policies of model M1, model M2, and the 
mean-value model. 
Next, we calculate the value of the VSS achieved by the MPOMDP model, and the EVPI. To 
begin with, we run a simulation study on a group of 10,000 samples where 50% of them are from 
model M1, and the other 50% are from model M2. We apply four different policies to the study 
group: (1) the optimal policy given by the POMDP model M1; (2) the optimal policy given by 
the POMDP model M2; (3) the optimal policy given by the mean-value POMDP model (i.e., the 
POMDP model with the model parameter being the mean parameter of M1 and M2); (4) the 
optimal policy given by the MPOMDP model M = (M1,M2,  = 0.5). We also compare the 
results with the case where we have the perfect information, and apply the optimal policy of M1 
to patients from M1 and the optimal policy of M2 to patients from M2. 
Table 1 shows the values of V0 at different initial belief vectors when applying different policies, 
and their regrets compared to the value function given by the optimal policy with perfect infor-
mation. As we can see from Table 1, the optimal policy of the MPOMDP model M dominates 
the optimal policies of model M1, model M2, and the mean-value model. This says that when 
model ambiguity exists, the MPOMDP model provides a better solution than ignoring the model 
ambiguity or averaging the model parameters. 
Table 2 shows the VSS achieved by the MPOMDP and the EVPI for different initial belief 
vectors. For each initial belief vector, the VSS of the MPOMDP is calculated as the (relative) 
difference between the values of the mean-value POMDP model and the MPOMDP model; and 
23
Belief vector b0 
  = (0.25, 0.75)   = (0.5, 0.5)   = (0.75, 0.25) 
VSS (%) EVPI (%) VSS (%) EVPI (%) VSS (%) EVPI (%) 
(0.45, 0.05, 0.45, 0.05) 0.11 (1.18%) 0.25 (2.71%) 0.19 (2.17%) 0.23 (2.55%) 0.58 (6.81%) 0.22 (2.39%) 
(0.45, 0.05, 0.25, 0.25) 0.22 (2.41%) 0.24 (2.56%) 0.02 (0.17%) 0.37 (4.11%) 0.56 (6.65%) 0.32 (3.54%) 
(0.45, 0.05, 0.05, 0.45) 0.43 (4.80%) 0.22 (2.29%) 0.18 (1.98%) 0.35 (3.80%) 0.34 (3.89%) 0.41 (4.53%) 
(0.25, 0.25, 0.45, 0.05) 0.21 (2.40%) 0.38 (4.27%) 0.63 (7.70%) 0.29 (3.28%) 0.54 (6.45%) 0.20 (2.29%) 
(0.25, 0.25, 0.25, 0.25) 0.05 (0.59%) 0.46 (5.18%) 0.55 (6.55%) 0.32 (3.61%) 0.69 (8.30%) 0.18 (2.03%) 
(0.25, 0.25, 0.05, 0.45) 0.05 (0.50%) 0.46 (5.11%) 0.55 (6.45%) 0.32 (3.50%) 0.60 (7.10%) 0.12 (1.36%) 
(0.05, 0.45, 0.45, 0.05) 0.13 (1.47%) 0.19 (2.10%) 0.29 (3.32%) 0.11 (1.23%) 0.73 (8.77%) 0.03 (0.36%) 
(0.05, 0.45, 0.25, 0.25) 0.04 (0.47%) 0.22 (2.39%) 0.24 (2.66%) 0.13 (1.43%) 0.81 (9.64%) 0.00 (0.01%) 
(0.05, 0.45, 0.05, 0.45) 0.10 (1.04%) 0.22 (2.34%) 0.23 (2.51%) 0.13 (1.41%) 0.73 (8.64%) 0.05 (0.59%) 
Table 2: The VSS achieved by the MPOMDP and the EVPI for different initial belief vectors in the two-model 
example. The VSS and EVPI are more significant when the decision-maker is less certain about the model and state 
distribution. 
the EVPI is calculated as the (relative) difference between the values of the MPOMDP model and 
model with perfect information. As we can see from Table 2, in general, the VSS and EVPI are 
more significant when the decision-maker is less certain about the model and state distribution. 
Table 3 also shows the percentage of true optimal action over time compared to the optimal policy 
when having the perfect information starting from different initial belief vectors. 
Lastly, we compare the performance of the two approximation methods introduced in Section 5. 
We implement each approximation method with 100 iterations. Figure 3 reports the average error 
of V0 in 20 runs, each with 100 iterations. As we can see from Figure 3, both methods make good 
progress over a small number of iterations. However, the tree-based sampling method converges 
more quickly with respect to the number of iterations. This is because, as discussed in Section 5, 
while both methods exploit the optimal action at each time period based on the current estimate 
of the value function, the tree-based sampling algorithm additionally calculates an upper bound 
estimate of the function to explore the scenarios where the current estimate has the largest error. 
This likely helps ensure more efficient exploration steps, and results in a faster overall convergence 
rate with respect to the number of iterations. On the other hand, in Table 4 we illustrate the 
computation time for each method on an Inter Core i7 2.6 GHz processor with 16 GB RAM. As 
we can see from Table 4, the tree-based sampling method takes more computation time for each 
run than the ✏-greedy sampling method. Thus, although the more judicious choice of belief grid 
24
Belief vector b0 
% of true optimal action over time 
Model M1 Model M2 Mean-value model MPOMDP model Perfect info. 
(0.45, 0.05, 0.45, 0.05) 59.70% 59.84% 79.33% 89.09% 100% 
(0.45, 0.05, 0.25, 0.25) 57.91% 60.07% 85.38% 88.99% 100% 
(0.45, 0.05, 0.05, 0.45) 72.79% 59.86% 86.31% 88.94% 100% 
(0.25, 0.25, 0.45, 0.05) 59.40% 70.37% 61.50% 88.74% 100% 
(0.25, 0.25, 0.25, 0.25) 57.60% 70.20% 67.76% 88.61% 100% 
(0.25, 0.25, 0.05, 0.45) 72.51% 70.06% 69.18% 88.64% 100% 
(0.05, 0.45, 0.45, 0.05) 60.14% 87.40% 79.42% 89.57% 100% 
(0.05, 0.45, 0.25, 0.25) 58.76% 87.50% 85.45% 89.60% 100% 
(0.05, 0.45, 0.05, 0.45) 73.70% 87.35% 86.81% 89.85% 100% 
Table 3: The percentage of true optimal action over time compared to the optimal policy with the perfect information 
starting from different initial belief vectors for different policies. The optimal policy of the MPOMDP model M 
dominates the optimal policies of model M1, model M2, and the mean-value model. 
Exact method ✏-greedy sampling Tree-based B&B 
Mean time for each run 6836s 109s 551s 
Number of ↵-vectors at t = 0 109 15 27 
Table 4: Comparisons of the computational time and number of iterations of Algorithm 1 and 2 for the toy example 
of two-model POMDP. 
modifications leads to fewer iterations for Algorithm 2, the shorter computation time per iteration 
of Algorithm 1 results in greater overall computation time efficiency, albeit with slightly higher 
error. 
6.2. Case study: prostate cancer AS optimization 
We implement the proposed MPOMDP model for optimizing AS for prostate cancer with im-
perfect information based on the POMDP models in Li et al. (2023). Prostate cancer is the most 
common cancer in men globally. Patients with low-risk variants of prostate cancer are recommended 
to join the AS, which monitors the patients by medical tests until there is a sign of progression to a 
high-risk variant of cancer, to avoid unnecessary treatments. The two most common medical tests 
in AS are the PSA test and biopsy. The PSA test is a simple blood test with almost no direct 
harm to patients. Biopsy is a much more accurate diagnostic test, which samples the tissue with 
25
Figure 3: Comparisons of Algorithm 1 and 2 for the toy example of two-model POMDP. 
hollow-core needles to examine the severity of prostate cancer; however, biopsy is still imperfect, 
with potential false-negative results caused by miss-sampling. Moreover, biopsy is very painful and 
harmful to patients. Thus, it is critical to decide the optimal timings for biopsies for each patient 
in prostate cancer AS. 
Li et al. (2023) used a finite-horizon two-state POMDP model to optimize the biopsy policy 
in each of four major prostate cancer AS study centers, which include the JH hospital, the UCSF 
medical center, the U of T medical center, and the PRIAS project. The objective of that study 
was to minimize the expected delay in the detection of high-risk prostate cancer and the expected 
number of lifetime biopsies. The result showed that, as different patient cohorts have heterogeneous 
cancer progression rates and test accuracy (model parameters), the optimal biopsy policies could 
be quite different in the different study centers. 
Our study in this paper considers the case where the model parameters are not known with 
certainty, and we seek a single biopsy policy that works well for models based on all four study 
centers. Examples may include optimizing the biopsy policy for a new patient who comes from a 
different area with an uncertain cancer progression rate, and for a newly initiated prostate cancer 
AS study that is unable to estimate the cancer dynamics (model parameters) because of a lack 
of data samples. For such new studies, a common strategy is to use the result from one of the 
previous studies as an approximate solution. The proposed MPOMDP model in this paper allows the 
decision-maker to trade off all previous major studies instead of picking only one study ambitiously. 
The objective of the MPOMDP model is to minimize a weighted sum of the expected delays in the 
26
detection of high-risk prostate cancer and the expected number of lifetime biopsies in four study 
centers. 
We first describe the MPOMDP model formulation M for optimizing prostate cancer AS. The 
decision epochs here are discrete annual time periods until age 75, which is the recommended 
stopping time for AS with the consideration of other cause mortality rates. There are two states in 
S, which are low-risk cancer state (LR) and high-risk cancer state (HR). The set A contains two 
actions that are “defer biopsy" and “conduct biopsy". At each decision epoch after taking action, 
there will be observations of PSA test and biopsy (if conducted). For the PSA test, we divide all 
possible outcomes into three intervals: I1 = [0, 4], I2 = (4, 10], and I3 = (10,1) (ng/mL); For 
biopsy, the possible outcomes are negative, positive, or null (no biopsy conducted). The transition 
and observation probabilities in the four different study centers were estimated in Li et al. (2020) and 
listed in Tables 5 and 6 for convenience. In Table 5, the misclassification error at diagnosis denotes 
the initial distribution b0, the annual cancer progression rate denotes the transition probabilities, 
and the biopsy sensitivity denotes the observation probabilities for the biopsy. Table 6 denotes the 
observation probabilities for the PSA test. Lastly, the reward function r(s, a, o) is defined as 
r(s, a, o) = 
8 >>>>>>>>>>>>>>>>< 
>>>>>>>>>>>>>>>>: 
0, a = Defer Biopsy, s = LR; 
✓, a = Defer Biopsy, s = HR; 
⌘, a = Conduct Biopsy, s = LR, o = Negative; 
⌘, a = Conduct Biopsy, s = HR, o = Positive; 
✓ + ⌘, a = Conduct Biopsy, s = HR, o = Negative; 
Not Defined, otherwise, 
where ✓ and ⌘ are non-negative scalars that denote the cost of one-year delayed detection of high-risk 
cancer and the burden of a biopsy, respectively. We set ✓ + ⌘ = 1, so that varying ✓ and ⌘ allows 
computing the optimal policy for different patient preferences for the two criteria. Here we choose 
✓ = ⌘ = 0.5 by way of example while the weighting in practice depends on patient preferences. 
Now, suppose that for a group of new patients, the decision-maker has no information about 
which model best describes the new patients. Traditionally, the decision-maker picks a single model 
based on their personal judgment/opinion about which is the best, and applies its optimal policy 
to new patients in practice. Here, our proposed MPOMDP model provides another solution to this 
problem. To show the benefit of the MPOMDP model, for each AS study, we compare the result 
of five different biopsy policies, which includes the four policies given by solving the JH, UCSF, U 
27
Center Misclassification Error 
at Diagnosis: b0(LR) 
Annual Cancer Progression 
rate: p 
Biopsy Sensitivity: 
(1   ) 
JH 0.0583 0.0691 0.7184 
UCSF 0.0809 0.1217 0.7431 
U of T 0.0774 0.1016 0.7949 
PRIAS 0.0653 0.0841 0.7614 
Table 5: The AS-POMDP model parameters in four study centers. Abbreviations: JH, Johns-Hopkins; UCSF, 
University of California-San Francisco; U of T, University of Toronto; PRIAS, Prostate Cancer Research International 
Active Surveillance. 
Center Probability Mass Function of PSA (ng/mL): q 
Cancer State I1 = [0, 4] I2 = (4, 10] I3 = (10,1) 
JH LR Cancer 0.3552 0.4311 0.2137 
HR Cancer 0.2868 0.4706 0.2426 
UCSF LR Cancer 0.0768 0.5680 0.3552 
HR Cancer 0.0678 0.5736 0.3586 
U of T LR Cancer 0.4573 0.3422 0.2005 
HR Cancer 0.3312 0.2368 0.4320 
PRIAS LR Cancer 0.1361 0.5357 0.3282 
HR Cancer 0.1094 0.5501 0.3405 
Table 6: The probability mass functions of PSA in four study centers. Abbreviations: JH, Johns-Hopkins; UCSF, 
University of California-San Francisco; U of T, University of Toronto; PRIAS, Prostate Cancer Research International 
Active Surveillance; LR, low-risk; HR, high-risk. 
28
Center Minimum cost of the optimal policy (regret %) 
JH model UCSF model U of T model PRIAS model MPOMDP model 
JH 2.74 (0) 2.92 (6.50%) 3.84 (40.42%) 3.01 (9.89%) 2.87 (4.80%) 
UCSF 2.54 (5.35%) 2.41 (0) 2.95 (22.45%) 2.68 (11.33%) 2.49 (3.33%) 
U of T 2.65 (12.34%) 2.42 (2.39%) 2.36 (0) 2.77 (17.54%) 2.40 (1.72%) 
PRIAS 2.59 (4.19%) 2.63 (5.54%) 3.11 (24.71%) 2.49 (0) 2.54 (2.03%) 
Table 7: The optimal value (minimum cost) function in different AS studies when applying different policies. 
of T, and the PRIAS POMDP models, and the policy given by solving the MPOMDP model. For 
the MPOMDP model, we set a non-informative initial model weight   = (0.25, 0.25, 0.25, 0.25). 
Table 7 shows the optimal value (minimum cost) function and the regret of each biopsy policy 
in each AS study center. The regret is calculated as the relative difference between the chosen 
policy and the best policy in each study center. As we can see from Table 7, the best policy in each 
study center is always the optimal policy given by the corresponding POMDP model. Moreover, 
the optimal policy given by the MPOMDP model is always better than policies from an inconsistent 
POMDP model in all four study centers. For each study center, the difference between the cost of the 
optimal policy given by the MPOMDP and a “wrong" model (different from the study center) is the 
VSS achieved by the MPOMDP model; and the difference between the MPOMDP and the “right" 
model is the EVPI. Figure 4 shows the comparison of the mean number of biopsies and average late 
detection time by biopsy in years in different AS studies when applying different policies in different 
models. Depending on how the decision-maker trades off between the mean number of biopsies and 
average late detection time by biopsy, the optimal policy given by the MPOMDP model is always 
the closest to the true optimal policy in each study center, compared with the policy given by a 
wrong POMDP model. 
7. Conclusion 
In this paper, we introduced a new MPOMDP model to address the issue of model ambiguity 
in POMDP models. Motivated by the prostate cancer AS optimization problem, when there are 
multiple credible optimization models with the same structure but different model parameters, the 
proposed MPOMDP model can learn the model credibility from the system outputs over time, 
and seek a single optimal policy that maximizes the expected future rewards across models. We 
29
Figure 4: Comparisons of the mean number of biopsies and average late detection time by biopsy in years in different 
AS studies when applying the optimal policies in different models. The reward parameter is set to be ✓ = ⌘ = 0.5. 
30
also discussed some structural properties of the proposed MPOMDP model, which not only reveal 
the benefit of the MPOMDP model by accounting for model ambiguity, but also motivate the 
solution methods to MPOMDP models. We then introduced an exact solution method and two 
fast approximation methods to MPOMDP models, which were shown to converge asymptotically, 
and compared their performance in a computational experiment. Lastly, we used the example of 
prostate cancer AS as a case study to demonstrate how the MPOMDP model can be applied to a 
real-world problem to improve medical decision-making. 
When applying the MPOMDP model to real-world problems, the model weight can be initialized 
by some prior knowledge or as a non-informative prior distribution over different POMDPs. Then, 
every time when there is new output from the system, the MPOMDP model can update the model 
belief so that more credible models will be assigned higher model weights. Notice that since the 
model weight is updated by the Bayesian formula, even if none of the POMDPs considered in the 
MPOMDP is the true model that describes a patient, the MPOMDP is still able to assign a higher 
weight to the model with a higher probability of generating the observed outputs. We then showed 
that an MPOMDP could be reformulated as a new POMDP model with an extended state space, 
where a state in the new POMDP model is a combination of the current model and the state in 
the original POMDP model. Utilizing this property, we then derived the belief update formula for 
both the system state and model in an MPOMDP. Further, motivated by the one-pass algorithm 
for POMDP models, we introduced an exact solution method to the proposed MPOMDP model. 
However, because of the complexity of an MPOMDP model, even for moderate-size problems, the 
exact solution method is not feasible in a reasonable amount of time. We then introduced two fast 
approximation algorithms applying the ✏-greedy and branch-and-bound sampling methods. Thus, 
instead of calculating the optimal value function of the MPOMDP over the entire belief space, we 
only evaluate the optimal value function on a subset of reachable belief points by sampling, and 
then approximate the value function on other places using the samples. 
Compared with the robust optimization approach, whose objective is to optimize the worst-case 
performance, there are three main advantages of our MPOMDP model. First, in our MPOMDP 
model formulation, when considering the optimal value problem, there are some nice properties, in-
cluding that the belief vector is sufficient for the past information and the existence of a deterministic 
and Markovian optimal policy, which do not hold for robust optimization models. These properties 
are important because they help develop efficient solution methods so that the MPOMDP can be 
applicable to large real-world problems. Second, the MPOMDP model is able to learn the model 
31
credibility for each individual over time from past actions and observations, which is not the focus in 
robust optimization models. Third, the MPOMDP model that optimizes a weighted-average value 
function by the model belief usually results in a less conservative policy than the robust optimiza-
tion models that optimize the worst-case value function. On average, the MPOMDP achieves better 
performance than the robust optimization models. 
In the computational experiments, we first used a toy example with two POMDPs to illustrate 
the use case of the proposed MPOMDP model. We formulated the MPOMDP with two POMDPs, 
solved for the optimal value function and policy exactly, and compared its performance with other 
traditional solutions. The results showed that the MPOMDP policy dominated the solution obtained 
by arbitrarily picking one POMDP model when the wrong model was selected, and the mean-
value POMDP model. This was because the MPOMDP can consider the performance of both 
POMDPs according to the model weight learned from system outputs. We also used this example 
to compare the performance of two much faster approximation methods. The ✏-greedy sampling 
method updated the lower bound estimate of the optimal value function in each iteration, which 
converged asymptotically over time. Compared with the ✏-greedy sampling method, the branch-
and-bound sampling method converged faster by maintaining an upper bound estimate of the value 
function. But it also required extra computational effort to calculate the upper bound estimates. 
We further investigated the benefit of the MPOMDP model in a real case study of prostate cancer 
AS. We showed that for a new patient starting prostate cancer AS, who may be best described by 
one of the models in the JH, UCSF, U of T, and PRIAS study centers, the MPOMDP model found 
a single optimal biopsy policy that is only slightly worse than the optimal biopsy policy given by 
the POMDP model of the true study center, but much better than the policies given by a wrong 
POMDP model and the mean-value POMDP model. Given the trade-off between the biopsy burden 
and late detection of a cancer progression by the decision-maker, the MPOMDP model achieved 
the minimum expected future costs when the true model was not known with certainty. Thus, the 
MPOMDP model appears to offer a robust policy that protects against uncertainty when the correct 
model is not known with certainty. For example, Table 7 shows the regret for the MPOMDP van 
be substantially larger than single model POMDP policies with regrets ranging from 0 to 40%. 
There are also some limitations of our work in this paper, and opportunities for future research 
in model ambiguity in POMDP models. First, we only focused on the optimal value problem of 
an MPOMDP model in this paper, where the objective was to maximize a weighted average of 
the value functions across different POMDPs according to the model-state belief vector. There 
32
could be other objective functions, for example, maximizing the worst-case reward, minimizing 
the conditional value-at-risk, and other probability measures that are widely used in stochastic 
programming and robust optimization problems. However, the potential issue for considering other 
objective functions is the existence of an optimal policy with a simple structure, for example, 
a deterministic and Markovian policy, that is practical for real-world problems. We leave the 
theoretical and methodological study of the extension to other objective functions to future research. 
Second, the proposed MPOMDP model only considers a discrete finite set of models. This is 
different from prior stochastic optimization work, where the uncertainty sets of model parameters 
are continuous. However, the work of MPOMDP in this paper was motivated by the real-world 
application in prostate cancer AS, where there are a finite set of competing well-established models. 
The framework we proposed can provide a valuable foundation for studying related problems that 
arise in other contexts. 
Acknowledgments 
This work is supported in part by the National Science Foundation through Grant Number 
CMMI 0844511. Any opinions, findings, and conclusions or recommendations expressed in this 
material are those of the authors and do not necessarily reflect the views of the National Science 
Foundation. This work was also supported by the Movember Foundation. The funders did not play 
any role in the study design, collection, analysis or interpretation of data, or in the editing of this 
thesis. 
References 
Åström, K. J. (1965). Optimal control of markov processes with incomplete state information. 
Journal of Mathematical Analysis and Applications , 10 , 174–205. 
Ayer, T., Alagoz, O., & Stout, N. K. (2012). Or forum—a pomdp approach to personalize mam-
mography screening decisions. Operations Research, 60 , 1019–1034. 
Birge, J. R. (1982). The value of the stochastic solution in stochastic linear programs with fixed 
recourse. Mathematical programming , 24 , 314–325. 
Boloori, A., Saghafian, S., Chakkera, H. A., & Cook, C. B. (2020). Data-driven management of post-
transplant medications: an ambiguous partially observable markov decision process approach. 
Manufacturing & Service Operations Management , 22 , 1066–1087. 
33
Cassandra, A. R. (1998). A survey of pomdp applications. In Working notes of AAAI 1998 fall 
symposium on planning with partially observable Markov decision processes. volume 1724. 
Cassandra, A. R., Kaelbling, L. P., & Kurien, J. A. (1996). Acting under uncertainty: Discrete 
bayesian models for mobile-robot navigation. In Proceedings of IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems. IROS’96 (pp. 963–972). IEEE volume 2. 
Delage, E., & Iancu, D. A. (2015). Robust multistage decision making. In The operations research 
revolution (pp. 20–46). INFORMS. 
Delage, E., & Mannor, S. (2010). Percentile optimization for markov decision processes with pa-
rameter uncertainty. Operations research, 58 , 203–213. 
Drake, A. W. (1962). Observation of a Markov process through a noisy channel . Ph.D. thesis 
Massachusetts Institute of Technology. 
Erenay, F. S., Alagoz, O., & Said, A. (2014). Optimizing colonoscopy screening for colorectal cancer 
prevention and surveillance. Manufacturing & Service Operations Management , 16 , 381–400. 
Iyengar, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research, 30 , 
257–280. 
Li, W. (2021). Data-Driven Optimization for Individualized Medical Decision-Making in Cancer . 
Ph.D. thesis. 
Li, W., Denton, B. T., & Morgan, T. M. (2023). Optimizing active surveillance for prostate cancer 
using partially observable markov decision processes. European Journal of Operational Research, 
305 , 386–399. 
Li, W., Denton, B. T., Nieboer, D., Carroll, P. R., Roobol, M. J., Morgan, T. M., & Movember 
Foundation’s Global Action Plan Prostate Cancer Active Surveillance consortium (2020). Com-
parison of biopsy under-sampling and annual progression using hidden markov models to learn 
from prostate cancer active surveillance studies. Cancer Medicine, . 
Mannor, S., Mebel, O., & Xu, H. (2016). Robust mdps with k-rectangular uncertainty. Mathematics 
of Operations Research, 41 , 1484–1509. 
Nakao, H., Jiang, R., & Shen, S. (2021). Distributionally robust partially observable markov decision 
process with moment-based ambiguity. SIAM Journal on Optimization, 31 , 461–488. 
34
Nilim, A., & El Ghaoui, L. (2005). Robust control of markov decision processes with uncertain 
transition matrices. Operations Research, 53 , 780–798. 
Puterman, M. L. (2014). Markov decision processes: discrete stochastic dynamic programming . John 
Wiley & Sons. 
Rabiner, L., & Juang, B. (1986). An introduction to hidden markov models. ieee assp magazine, 
3 , 4–16. 
Ross, S. M. (1971). Quality control under markovian deterioration. Management Science, 17 , 
587–596. 
Saghafian, S. (2018). Ambiguous partially observable markov decision processes: Structural results 
and applications. Journal of Economic Theory , 178 , 1–35. 
Schlaifer, R., & Raiffa, H. (1961). Applied statistical decision theory . 
Smallwood, R. D., & Sondik, E. J. (1973). The optimal control of partially observable markov 
processes over a finite horizon. Operations research, 21 , 1071–1088. 
Steimle, L. N., Kaufman, D. L., & Denton, B. T. (2021). Multi-model markov decision processes. 
IISE Transactions , (pp. 1–39). 
Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press. 
Wiesemann, W., Kuhn, D., & Rustem, B. (2013). Robust markov decision processes. Mathematics 
of Operations Research, 38 , 153–183. 
Xu, H., & Mannor, S. (2012). Distributionally robust markov decision processes. Mathematics of 
Operations Research, 37 , 288–300. 
Zhang, J., Denton, B. T., Balasubramanian, H., Shah, N. D., & Inman, B. A. (2012). Optimization 
of prostate biopsy referral decisions. Manufacturing & Service Operations Management , 14 , 529– 
547. 
35
Appendix A. Proofs 
Proof of Proposition 1 
Denote I(t) as the total information available, i.e., historical actions and observations, at the 
end of time period t: 
I(1) = {a1, o1}, I(t+ 1) = I(t) [ {at+1, ot+1}, 8t   1. 
We are going to show that b m t+1(s 
m t+1) depends on I(t) only through bt for all t   1, sm 
t+1 2 S, and 
m = 1, ...,M : 
b m 
t+1(s m 
t+1) 
= P((st+1,mt+1)|at, ot, I(t)) 
= P((st+1,mt+1), ot|at, I(t)) 
P(ot|at, I(t)) 
= 
P st2S 
P mt 
P((st+1,mt+1), (st,mt), ot|at, I(t)) P(ot|at, I(t)) 
= 
P st2S 
P mt 
P(ot|(st,mt), at, I(t))P((st+1,mt+1)|(st,mt), at, I(t))P((st,mt)|at, I(t)) P(ot|at, I(t)) 
= 
P st2S 
P mt 
F mt(o, a, st)Pmt(st, at, st+1)bmt (st) 
P(ot|at, I(t)) . 
Now, we can see the numerator of bm t+1(s 
m t+1) depends on I(t) only through bt, and the denominator 
is just the numerator summed over all possible values of sm t+1. Thus, bt is a sufficient statistics of 
I(t) for all t = 1, ..., T . ⇤ 
Proof of Proposition 2 
First of all, 
P((st+1,mt+1)|o, b, a) = P((st+1,mt+1), o|b, a) 
P(o|b, a) . 
For the numerator, 
P((st+1,mt+1), o|b, a) 
= X 
st 
X 
mt 
P((st+1,mt+1), o, (st,mt)|b, a) 
= X 
st 
X 
mt 
P(o|(st+1,mt+1), (st,mt), b, a)P(st+1,mt+1), (st,mt)|b, a) 
= X 
st 
X 
mt 
P(o|(st,mt), a)P(st+1,mt+1)|(st,mt), a)P((st,mt)|b). 
36
Thus, 
P((st+1,mt+1)|o, b, a) 
= 
P st P(o|(st,mt+1), a)P((st+1,mt+1)|(st,mt+1), a)P((st,mt+1)|b)P 
st+1,mt+1 
P st P(o|(st,mt+1), a)P((st+1,mt+1)|(st,mt+1), a)P((st,mt+1)|b) 
. 
⇤ 
Proof of Theorem 1 
We start from the end of time horizon t = T . For any reachable belief vector b 2 B̃T , we can 
show that in each iteration of Algorithm 1, the probability of sampling b at time t = T is strictly 
greater than 0. Suppose b is reachable through the path 
(b0, a0, o0) ! (b1, a1, o1), ...,! (bT 1, aT 1, oT 1) ! bT = b. 
If we denote f as the smallest non-zero element in F , then in i th iteration of Algorithm 1 for any i, 
P({b is sampled in iteration i})   (✏f)T > 0. 
From the definition of V̂T in Algorithm 1 we can see, 
P({VT (b)  V̂ i+1 T 
(b) > 0}) 
P({b is not in B i 
T }) 
=P({None of the first i iterations has sampled b}) 
(1  (✏f)T )i ! 0, as i ! 1. 
Thus, V̂ i 
T (b) converges to VT (b) in probability for any b 2 B̃T . 
Next, we use induction to show that V̂ i t (b) converges to Vt(b) in probability for any b 2 B̃t for 
all t  T . In Algorithm 1, it is easy to see that, by applying the backward induction, 
V̂ i 
t (b) = max a 
X 
s2S b(s){r(s, a) + 
X 
o2O 
X 
s02S  F (s, a, o)V̂ i 
t+1(⇤(b|a, o))}, 8b. 
Then, at time t < T , for any belief vector b 2 B̃t, a sufficient condition such that V̂ i t (b) converges 
to Vt(b) will be V̂ i t+1(⇤(b|a, o)) converges to Vt+1(⇤(b|a, o)) for any action a and observation o, i.e., 
V̂ i t+1(b 
0) converges to Vt+1(b0) for all b0 reachable at time t+ 1 from b at time t. Starting from VT , 
we have already shown V̂ i 
T (b) converges to VT (b) in probability for all reachable belief vector b at 
time T . Thus, we conclude that V̂ i t (b) converges to Vt(b) in probability for any b 2 B̃t for all t  T . 
⇤ 
37
Proof of Proposition 3 
Prove by construction. Consider an MPOMDP model M = (M1,M2, ), where two POMDP 
models Mm = (S, b0, A, Pm , O, F 
m , r 
m) for m = 1, 2 have a same state space, observation space, 
and action space 
S = {s1, s2}, O = {o1, o2}, A = {a1, a2} 
but different transition and observation probabilities 
P 1(a1) = 
0 
@ 0.1 0.9 
0.9 0.1 
1 
AF 1(a1) = 
0 
@ 0.8 0.2 
0.2 0.8 
1 
A , 
P 1(a2) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
AF 1(a2) = 
0 
@ 0.7 0.3 
0.3 0.7 
1 
A , 
P 2(a1) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
AF 2(a1) = 
0 
@ 0.6 0.4 
0.4 0.6 
1 
A , 
P 2(a2) = 
0 
@ 0.1 0.9 
0.9 0.1 
1 
AF 2(a2) = 
0 
@ 0.9 0.1 
0.1 0.9 
1 
A 
and different reward functions 
a1 : r(s1, a1, o1) = 2, r(s1, a1, o2) = 0, r(s2, a1, o1) = 0, r(s2, a1, o2) = 1 
a2 : r(s1, a2, o1) = 1, r(s1, a2, o2) = 0, r(s2, a2, o1) = 0, r(s2, a2, o2) = 2. 
We consider the time horizon to be t = 0, 1 and set the model weights to be  1 =  2 = 0.5. For any 
belief vector b of M, we write 
b = (1  b 1 , b 
1 , 1  b 
2 , b 
2), 
where b 1 is the belief in state s2 in M1 and b 
2 is the belief in state s2 in M2. For any ↵-vector ↵t 
at time t = 0, 1, we write 
↵t = (↵1 t ,↵ 
2 t ) = (↵1 
t (0),↵ 1 t (1),↵ 
2 t (0),↵ 
2 t (1)) 
where ↵ 1 t is the ↵-vector in M1, ↵1 
t (0), ↵1 t (1) are the values of ↵1 
t at b1 = 0 and b 1 = 1; and similarly 
for ↵ 2 t . We can use the exact solution method to find the set of all ↵-vectors at time t = 1: 
A1 = {(1.6, 0.8, 1.2, 0.6), (0.7, 1.4, 0.9, 1.8)}. 
38
Now, apply Algorithm 1. Suppose in the first iteration we sample two belief vectors at time t = 0, 
which are b 1 0 = (0.25, 0.25, 0.25, 0.25) and b 
2 0 = (0.5, 0, 0, 0.5); and then we sample action a1 and 
observation o1, resulting two belief vectors at time t = 1, which are b 1 1 = (0.13, 0.37, 0.29, 0.21) and 
b 2 1 = (0.07, 0.6, 0.03, 0.3). 
We then can identify (0.7, 1.4, 0.9, 1.8) 2 A1 as the only non-dominated ↵-vector at time t = 1, 
and two non-dominated ↵-vectors 
(2.019, 2.631, 2.529, 3.021), (2.22, 2.28, 1.56, 2.94) 
at time t = 0. In the next iteration, suppose we sample one more belief vector b 3 0 = (0, 0.5, 0.5, 0) 
at time t = 0 and b 3 1 = (0.45, 0.05, 0.45, 0.05) at time t = 1 following action a1 and observation 
o1. Then, using three sampled belief vectors b 1 1, b 
2 1, b 
3 1, we can identify all two ↵-vectors in A1 as 
non-dominated ↵-vectors at time t = 1. 
At time t = 0, using three sampled belief vectors b 1 0, b 
2 0, b 
3 0, we can find three non-dominated 
↵-vectors at time t = 0, which are 
(2.019, 2.631, 2.529, 3.021), (2.93, 1.57, 2.19, 2.31), (2.48, 2.32, 2.34, 1.26). 
In other words, in the first iteration, we have 
Â1 0 = {(2.019, 2.631, 2.529, 3.021), (2.22, 2.28, 1.56, 2.94)} 
and in the second iteration, we have 
Â2 0 = {(2.019, 2.631, 2.529, 3.021), (2.93, 1.57, 2.19, 2.31), (2.48, 2.32, 2.34, 1.26)}. 
Now, consider the belief point b = (0.45, 0.05, 0, 0.5) at time t = 0: 
V̂ 2 0 (b) = 2.552 < 2.583 = V̂ 
1 0 (b), 
i.e., the lower bound estimate of V0 after the second iteration is smaller than the estimate after the 
first iteration at b. ⇤ 
39