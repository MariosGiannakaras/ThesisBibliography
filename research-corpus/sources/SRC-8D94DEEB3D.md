> Source: https://arxiv.org/pdf/2307.08082

 
POMDP inference and robust solution via 
deep reinforcement learning: An application 
to railway optimal maintenance 
Giacomo Arcieri1*, Cyprien Hoelzl1, Oliver Schwery2, Daniel Straub3, Konstantinos G. Papakonstantinou4 and Eleni 
Chatzi1 
1*Institute of Structural Engineering, ETH Zürich, Zürich, 8093,Switzerland. 
2 Swiss Federal Railways SBB, Bern, 3000, Switzerland. 3Engineering Risk Analysis Group, Technical University of 
Munich, Munich, 80333, Germany. 4Dept. of Civil and Environmental Engineering, Pennsylvania 
State Univ., University Park,16802, PA, USA. 
*Corresponding author(s). E-mail(s): giacomo.arcieri@ibk.baug.ethz.ch; 
Contributing authors: hoelzl@ibk.baug.ethz.ch; oliver.schwery@sbb.ch; straub@tum.de; kpapakon@psu.edu; 
chatzi@ibk.baug.ethz.ch; 
Abstract 
Partially Observable Markov Decision Processes (POMDPs) can model complex sequential decision-making problems under stochastic and uncertain environments. A main reason hindering their broad adoption in real-world applications is the lack of availability of a suitable POMDP model or a simulator thereof. Available solution algorithms, such as Reinforcement Learning (RL), require the knowledge of the transition dynamics and the observation generating process, which are 
 
 
 
 
 
 
 
 
 
 
 
 
2 POMDP inference and robust solution via deep reinforcement learning 
often unknown and non-trivial to infer. In this work, we propose a combined framework for inference and robust solution of POMDPs via deep RL. First, all transition and observation model parameters are jointly inferred via Markov Chain Monte Carlo sampling of a hidden Markov model, which is conditioned on actions, in order to recover full posterior distributions from the available data. The POMDP with uncertain parameters is then solved via deep RL techniques with the parameter distributions incorporated into the solution via domain randomization, in order to develop solutions that are robust to model uncertainty. As a further contribution, we compare the use of transformers and long shortterm memory networks, which constitute model-free RL solutions, with a model-based/model-free hybrid approach. We apply these methods to the real-world problem of optimal maintenance planning for railway assets. 
Keywords: Partially observable Markov decision process, Reinforcement learning, Deep learning, Model uncertainty, Optimal maintenance 
1 Introduction 
Partially Observable Markov Decision Processes (POMDPs) offer a mathemat-
ically sound framework to model and solve complex sequential decision-making 
problems (Cassandra, 1998). POMDPs account for the uncertainty associ-
ated with observations in order to derive optimal policies, namely a sequence 
of optimal decisions that minimize/maximize the total costs/rewards over 
a prescribed time horizon, under stochastic and uncertain environments. 
Stochasticity can indeed be incorporated both in the evolution of the hidden 
states over time, i.e., the transition dynamics, and in the process that gener-
ates the observations, which reflect only a partial and/or noisy information of 
the actual states. 
POMDPs form a potent mathematical framework to model optimal main-
tenance planning for deteriorating engineered systems (Papakonstantinou & 
Shinozuka, 2014a). In such problems, a perfect information of the system’s 
condition (state) is generally not available or feasible to acquire, due to 
the problem’s scale, inherent noise of sensing instruments, and associated
 
POMDP inference and robust solution via deep reinforcement learning 3 
costs limitations. By using sensors and inferred associated condition indica-
tors, Structural Health Monitoring (SHM) tools, as described by Andriotis, 
Papakonstantinou, and Chatzi (2021); Farrar and Worden (2012); Straub et 
al. (2017), can provide estimates of the structural state. However, the provided 
observations are often incomplete and susceptible to noise, which limits their 
ability to accurately determine the true state of the system. Consequently, 
decision-making must occur in the face of irreducible uncertainty. Within a 
POMDP scheme, the decision maker (or agent) receives an observation from 
an SHM system, using it to form a belief about the current state of the sys-
tem. Based on this belief, the agent takes an action, which will impact the 
future condition of the system. The POMDP objective is to find the optimal 
sequence of maintenance actions that minimizes the expected total costs over 
the operating life-cycle. A list of applications of POMDP modeling to opti-
mal maintenance can be found in (Durango & Madanat, 2002; Ellis, Jiang, & 
Corotis, 1995; Kıvanç, Özgür-Ünlüakın, & Bilgiç, 2022; Madanat & Ben-Akiva, 
1994; Memarzadeh, Pozzi, & Zico Kolter, 2015; Papakonstantinou, Andriotis, 
& Shinozuka, 2018; Schöbi & Chatzi, 2016). 
POMDP solutions assume knowledge of the transition dynamics and the 
observation generating process. This implies strict prior assumptions on the 
POMDP model parameters that govern the deterioration, the effects of main-
tenance actions, and the relation of observations to latent states and variables. 
When a POMDPmodel is available, the solution can be computed via Dynamic 
Programming (DP) (Bertsekas, 2012) and approximate methods (Papakon-
stantinou & Shinozuka, 2014b) with optimality convergence guarantees, when 
the complexity of the problem is not prohibitive, or via Reinforcement Learn-
ing (RL) schemes (Sutton & Barto, 2018) through samples and trial and error 
learning. While RL methods can relax some assumptions on the POMDP
 
4 POMDP inference and robust solution via deep reinforcement learning 
knowledge, a simulator that can reliably describe the POMDP model is 
still necessary for inference and testing purposes, particularly for engineering 
problems and in infrastructure asset management applications. 
However, a full POMDP model of the problem is rarely available in real-
world applications, and its inference can be quite challenging. The availability 
of such a model is a key issue that prevents wide adoption of the POMDP 
framework and its solution methods (e.g., reinforcement learning) for real-
world applications. Available literature on the theme of maintenance planning 
is focused on developing RL methods to solve complex POMDP problems, as 
pioneered by the work of Andriotis and Papakonstantinou (2019, 2021), while 
assuming knowledge of the POMDP transition and observation models, i.e., 
by for example assuming that the POMDP inference has already been carried 
out. Only few papers deal with the POMDP inference, which poses a challenge 
in itself, while best practices are not generally available. Papakonstantinou and 
Shinozuka (2014a); Song, Zhang, Shafieezadeh, and Xiao (2022); Wari, Zhu, 
and Lim (2023) propose methods to estimate the state transition probability 
matrix for deterioration processes, but without demonstrating inference on the 
transition matrices associated with maintenance actions. Guo and Liang (2022) 
propose methods to estimate both the transition and the observation models, 
but do not consider model uncertainty and the implementation examples do 
not involve real-world data but only simulated ones. 
In Arcieri et al. (2023), we tackle this key inference issue by proposing 
a framework to jointly infer all transition and observation model parame-
ters entirely from available real-world data, via Markov Chain Monte Carlo 
(MCMC) sampling of a Hidden Markov Model (HMM), which is conditioned 
on actions. The framework, which is relatively easy to implement and can 
be tailored to the problem at hand, estimates full posterior distributions of
 
POMDP inference and robust solution via deep reinforcement learning 5 
POMDP model parameters. By considering these distributions in the POMDP 
evaluation, optimal policies that are robust with respect to POMDP model 
uncertainties are obtained. 
In this work, we combine the POMDP inference with a deep RL solution. 
Most previous works on deep RL methods focus on fully observable problems, 
with RL solutions for POMDPs having received notably lower attention. Par-
tial observability is usually overcome with deep learning architectures that are 
able to infer hidden states through memory and a history of past observa-
tions. Schmidhuber (1990) is one of first works that applied Recurrent Neural 
Networks (RNNs) for RL problems. Subsequently, Long Short-Term Memory 
(LSTM) networks have become the standard to handle partial observabil-
ity (Dung, Komeda, & Takagi, 2008; Meng, Gorbet, & Kulić, 2021; Zhu, Li, 
Poupart, & Miao, 2017). Recent works propose to replace LSTM architec-
tures with Transformers (GTrXL) (Parisotto et al., 2020). A third modeling 
option, which constitutes a hybrid approach between a DP and a RL solu-
tion, exploits the POMDP model to compute beliefs via Bayes’ theorem, which 
are then fed to the deep RL algorithm as inputs to classical feed-forward 
Neural Networks (NNs) (Andriotis & Papakonstantinou, 2019, 2021; Morato, 
Andriotis, Papakonstantinou, & Rigo, 2023). Namely, the POMDP problem 
is converted into the belief-MDP (Andriotis et al., 2021; Papakonstantinou & 
Shinozuka, 2014b) and then solved with deep RL techniques. We compare these 
three available solution methods and propose a joint framework of inference 
and robust solution of POMDPs based on deep RL techniques, by combining 
MCMC inference with domain randomization of the RL environment in order 
to incorporate model uncertainty into the policy learning. 
We showcase the applicability of these methods and of the proposed frame-
work on a real-world problem of optimal maintenance planning for railway
 
6 POMDP inference and robust solution via deep reinforcement learning 
infrastructure. The problem, modelled as a POMDP, is based on on-board 
railway monitoring data, namely the so-called “fractal values” condition indi-
cator, computed from field measurements and provided by our SBB (the Swiss 
Federal Railways) partners. 
The remainder of this paper is organized as follows. Section 2 provides the 
necessary background on POMDPs. Section 3 describes the considered main-
tenance planning problem of railway assets and the monitoring data. Section 
4 describes the POMDP inference and its implementation to the problem here 
considered. Section 5 evaluates the three available modeling options of deep 
RL solutions for POMDPs, namely LSTM, GTrXL, and the belief-input case. 
Section 6 proposes our joint framework of POMDP inference and robust solu-
tion via deep RL and domain randomization. Finally, Section 7 concludes with 
a highlight and a discussion of the contributions, and outlines possible future 
work. 
2 Preliminaries 
2.1 Partially Observable Markov Decision Processes 
A POMDP can be considered as a generalization of a Markov Decision Process 
(MDP) for modelling sequential decision-making problems within a stochas-
tic control setting, with uncertainty incorporated into the observations. A 
POMDP is defined by the tuple ⟨S,A,Z,R, T,O, b0, H, γ⟩, where: 
 S is the finite set of hidden states that the environment can assume. 
 A is the finite set of available actions. 
 Z is the set of possible observations, generated by the hidden states and 
executed actions, which provide partial and/or noisy information about the 
actual state of the system.
 
POMDP inference and robust solution via deep reinforcement learning 7 
 R : S×A→ R is the reward function that assigns the reward rt = R(st, at) 
for assuming an action at at state st. 
 T : S × S × A → [0, 1] is the transition dynamics model that describes the 
probability p(st+1 | st, at) to transition to state st+1 if action at is taken at 
state st. 
 O : S × A × Z → R is the observation generating process that defines the 
emission probability p(zt | st, at−1, zt−1), namely the likelihood to observe 
zt if the system is at state st and action at−1 was taken. 
 b0 is the initial belief on the system’s state s0. 
 H is the considered horizon of the problem, which can be finite or infinite. 
 γ is the discount factor that discounts future rewards to obtain the present 
value. 
In the POMDP setting, the agent takes a decision based on a formulated 
belief over the system’s state. Such a belief is defined as a probability distri-
bution over S, which maps the discrete finite set of states into a continuous 
| S | −1 dimensional simplex (Papakonstantinou & Shinozuka, 2014b). It is a 
sufficient statistics over the complete history of actions and observations. Solv-
ing a POMDP is thus equivalent to solving a continuous state MDP defined 
over the belief space, termed the belief-MDP (Andriotis et al., 2021; Papakon-
stantinou & Shinozuka, 2014b). The belief over the system’s state is updated 
according to Bayes’ rule every time the agent receives a new observation: 
b(st+1) = p(zt+1 | st+1, at) 
p(zt+1 | b, at) ∑ st∈S 
p(st+1 | st, at)b(st) (1)
 
8 POMDP inference and robust solution via deep reinforcement learning 
where the denominator is the normalizing factor: 
p(zt+1 | b, at) = ∑ 
st+1∈S 
p(zt+1 | st+1, at) ∑ st∈S 
p(st+1 | st, at)b(st) (2) 
The objective of the POMDP is to determine the optimal policy π∗, which 
maps beliefs to actions, that maximizes the expected sum of rewards: 
π∗ = argmax π 
E 
[ H∑ t=0 
γtrt 
] (3) 
where rt = R(st, π(bt)). Algorithms based on DP (Bertsekas, 2012) can be used 
to compute the optimal policy. These algorithms rely on two key functions: the 
value function V π, which calculates the expected sum of rewards for a policy 
π starting from a given state until the end of the prescribed horizon, and the 
Q-value function Qπ (Sutton & Barto, 2018), which estimates the expected 
value for assuming action at in state st, and then following policy π. 
bt 
zt 
st 
· · · 
at 
rt 
bt+1 
zt+1 
st+1 
at+1 
rt+1 
· · · 
T T 
O 
π 
R 
T 
O 
π 
R 
Fig. 1: Probabilistic graphical model of a POMDP.
 
POMDP inference and robust solution via deep reinforcement learning 9 
Finally, a POMDP can be represented as a special case of influence dia-
grams (Luque & Straub, 2019; Morato, Papakonstantinou, Andriotis, Nielsen, 
& Rigo, 2022), which form a class of probabilistic graphical models. Figure 1 
illustrates the influence diagram for the POMDP here considered. Circles and 
rectangles correspond to random and decision variables, respectively, while 
diamonds correspond to utility functions (Koller & Friedman, 2009). Shaded 
shapes denote observed variables, while edges encode the dependence structure 
among variables. 
3 The railway maintenance problem 
We apply and test the proposed methodology on the problem of optimal main-
tenance planning for railway infrastructure assets on the basis of availability 
of regularly acquired monitoring data. The railway track comprises various 
components, such as rails, sleepers, and ballast, which are exposed to harsh 
environments and high operating loads, leading to accelerated degradation. 
Among these infrastructure components, the substructure - in particular - is 
especially important in this degradation process. The substructure undergoes 
repeated loading from the superstructure (tracks, sleepers and ballast), pre-
vents soil particles from rising into the ballast, and facilitates water drainage. 
A weakened substructure typically results in distortions of the track geome-
try. Tamping (Audley & Andrews, 2013), a maintenance procedure that uses 
machines to compact the ballast underneath the railway track, restoring its 
shape, stability and drainage system, is often applied when the substructure 
condition is considered moderately deteriorated. However, in case of poor 
substructure condition, such as intrusion of clay or mud or water clogging, 
tamping provides only a short-term remedy, and replacing the superstructure 
and substructure is the most appropriate long-term solution.
 
10 POMDP inference and robust solution via deep reinforcement learning 
The optimization of maintenance decisions for these critical infrastructure 
components benefits from information that is additional to the practice of 
scheduled visual inspections, which are typically conducted on-site by experts. 
Such additional information can be delivered from monitoring data derived by 
diagnostic vehicles. In this work, we specifically exploit the fractal values, a 
substructure condition indicator extracted from the longitudinal level, which 
is measured by a laser-based system mounted on a diagnostic vehicle, to guide 
decisions for substructure renewal. The longitudinal level represents the devi-
ations of the rail from a smoothed vertical position (Wang, Berkers, van den 
Hurk, & Layegh, 2021). On the basis of this measurement the fractal values can 
be computed, via appropriate filtering and processing steps. The fractal value 
indicator describes the degree of “roughness” of the track at varying wave-
length scales. For the interested reader, the detailed steps of the fractal value 
computation are reported in Arcieri et al. (2023); Landgraf and Hansmann 
(2019). In particular, long-wave (25-70 m) fractal values, which are employed in 
this work, have shown a significant correlation to substructure damage (Hoelzl 
et al., 2021), and are used by railway authorities as an indicator which can 
instigate repair/maintenance actions, such as tamping. 
In this work, we use actual track geometry measurements, carried out via 
a diagnostic vehicle of the SBB between 2008 and 2018 across Switzerland’s 
railway network. The track geometry measurements were collected twice a 
year for the investigated portion of track. The fractal values are computed 
every 2.5m from the measured longitudinal level. The performed maintenance 
actions have been logged for the analysed tracks over the same considered 
period. These logs contain information on the maintenance, repair, or renewal 
actions taken on a section of the network at a specific date.
 
POMDP inference and robust solution via deep reinforcement learning 11 
We model the railway track maintenance optimization with a POMDP 
scheme, relying on diagnostic vehicle measurements of long-wave fractal values. 
The true but unobserved railway condition is discretized in 4 hidden states, 
s0, s1, s2, and s3, reflecting various grades, from perfect to highly deteriorated 
state. This is chosen to coincide with the number of grade levels assumed by 
the Swiss Federal Railways for classifying substructure condition. It should be 
noted, that in the POMDP inference setting, the number of hidden states is 
not fixed. To this end, we evaluated further possible dimensions of the hid-
den states vector, as part of the POMDP inference presented in the next 
section; a dimension of four yielded improved convergence and better-defined 
distributions. The fractal values are assumed as the (uncertain) POMDP obser-
vations, which correlate with the actual state of the substructure, but offer 
only partial and noisy information thereof. Unlike classical POMDP model-
ing of optimal maintenance planning problems, where observations are usually 
discrete, fractal values comprise (negative) continuous values, rendering the 
considered POMDP inference and solution quite complex. The problem defi-
nition is supplemented with information on the available maintenance actions. 
Three possible actions are considered, corresponding to the real-world setting, 
namely action a0 do-nothing, and the aforementioned tamping and replace-
ment actions, denoted as a1 and a2, which can be interpreted as a minor 
and a major repair, respectively. The fractal value indicators are derived via 
measurements of the diagnostic vehicle every 6 months, which thus repre-
sents the time-step of the decision-making problem. Considering the almost 10 
years of collected measurements, our real-world dataset is ultimately composed 
of time-series of 20 fractal values, per considered railway section, complete 
with information on respective maintenance actions (with “action” do-nothing
 
12 POMDP inference and robust solution via deep reinforcement learning 
included), i.e., (z0, a0, · · · , a19, z20). Finally, the (negative) rewards represent-
ing costs associated with actions and states have been elicited from SBB and 
are reported in Table 1 in general cost units. 
Table 1: Costs of the POMDP model. 
State condition s0 s1 s2 s3 Maintenance action 
a0 0 0 0 0 a1 −50 −50 −50 −50 a2 −2, 050 −2, 710 −3, 370 −4, 050 
Condition cost −100 −200 −1, 000 −8, 000 
4 POMDP inference 
To formulate the POMDP problem, the transition dynamics and the obser-
vation generating process must be inferred. In the RL context, the POMDP 
inference is necessary to generate samples for the policy learning, for inference 
of a belief over the hidden states, and/or for testing purposes. To tackle this 
key issue, we propose an MCMC inference of a HMM conditioned on actions, 
which jointly estimates parameter distributions of both the POMDP transition 
and observation models based on available data. While we implement the pro-
posed scheme on the problem of railway maintenance planning based on fractal 
value observations, its applicability is general. Therefore, we further suggest 
possible extensions to help researchers and practitioners tailor the POMDP 
model inference to the problem at hand. In addition, we provide a comple-
mentary tutorial1 illustrating the code implementation on various simulated 
case-studies, in order to support exploitation for real-world applications. 
1Code available on GitHub.
 
POMDP inference and robust solution via deep reinforcement learning 13 
In the context of discrete hidden states and actions, the transition dynamics 
are modelled via Dirichlet distributions: 
T0 ∼ Dirichlet(α0) 
s0 ∼ Categorical(T0) 
T ∼ Dirichlet(αT ) 
st | st−1, at−1 ∼ Categorical(T ) 
(4) 
where T0 are the parameters of the probability distribution of the initial 
state s0, and α0 and αT are the prior concentration parameters. T0 can be 
assigned a uniform flat prior α0, unless some prior knowledge on the ini-
tial state distribution is available. By contrast, it is beneficial to regularize T 
with informative priors αT , which regularize the deterioration or the repairing 
process. For example, the transition matrix related to the action do-nothing, 
which describes the deterioration process of the system, can be regularized 
with higher prior probabilities on the diagonal and on the upper-right trian-
gle, and near-zero on the lower-left triangle. Likewise, the transition matrices 
associated with maintenance actions would present higher prior probabilities 
on the left triangle and near-zero on the right triangle, in order to inform the 
model that a repair action is expected to be followed by improvements of the 
system. 
The dimensionality of the Dirichlet distribution that models the transition 
dynamics T is S×S×A, namely one transition matrix per action. The exten-
sion to time-dependent transition dynamics is straightforward by enlarging the 
distribution by a further dimension representing time, i.e., S × S ×A×H. 
In the context of continuous observations, the observation generating pro-
cess can differ on the basis of whether the observation follows a deterioration
 
14 POMDP inference and robust solution via deep reinforcement learning 
or a repairing process. In addition, similarly to the inference of the first hid-
den state according to T0, an initial observation process can be necessary to 
model the first observation. Tailoring to the nature of the fractal value moni-
toring data, the initial, deterioration, and repairing processes are modelled via 
Truncated Student’s t processes, as follows: 
z0 ∼ TruncatedStudentT(µst0 , σst0 
, νst0 ,ub = 0) 
zt − zt−1 ∼ TruncatedStudentT(µd|st , σd|st , νd|st ,ub = −zt−1) 
zt ∼ TruncatedStudentT(kr|at−1 ∗ zt−1 + µr|st , σr|st , νr|st ,ub = 0) 
(5) 
where ub stands for “upper bound”, and all parameters governing the processes 
are assigned priors described in Arcieri et al. (2023). 
The use of Truncated Student’s t processes was tailored to the mathemat-
ical characteristics of the fractal values, which i) assume only negative values, 
ii) exhibit a negative trend in absence of repairing actions, iii) their values 
are dependent on the previous observations, and iv) the studied dataset, as 
is common in real-world measurements, presents outliers and measurement 
errors, modelled by the Student’s t fat tails. Naturally, other distributions can 
also be employed as part of the proposed framework in order to model the 
data at hand related to each application. For instance, in absence of the pre-
vious limiting characteristics, simpler (unbounded) Gaussian emissions could 
have been used, as further shown in the tutorial. In the case of discrete obser-
vations, the observation model would be represented by a probability matrix 
S×Z, which can be again modelled via a Dirichlet distribution. In the case of 
more than one possible inspection action or monitoring tool, as in Papakon-
stantinou et al. (2018), the Dirichlet distribution can be simply enlarged by a 
further dimension representing the number of possibilities. Finally, dependen-
cies in multi-component systems could be modelled via a Bayesian hierarchical
 
POMDP inference and robust solution via deep reinforcement learning 15 
model (Gelman, Carlin, Stern, & Rubin, 1995), enabling solutions as proposed 
in Andriotis and Papakonstantinou (2019, 2021); Morato et al. (2023). 
Observation model ∼ 
TruncatedStudentT 
Hidden states ∼ 
Categorical 
Transition model ∼ 
Dirichlet 
Actions 
Observations (Fractal values) 
Model inference 
Fig. 2: A graphical model of the HMM inference. Arrows indicate dependencies, while shaded nodes indicate observed variables. 
The graphical model of the entire HMM is reported in Figure 2. The 
MCMC inference is run on a final dataset of 62 time-series with the No-U-Turn 
Sampler (NUTS) (Hoffman, Gelman, et al., 2014). Four chains are run with 
3,000 samples collected per chain. The inference results, which present good 
post-inference diagnostic statistics, with no divergences and high homogeneity 
between and within chains, are reported in Figures A1-A6 in Appendix A.
 
16 POMDP inference and robust solution via deep reinforcement learning 
5 RL for POMDP solution 
POMDP problems have been tackled via deep RL with common methods 
augmented with LSTM architectures and a history of past observations (and 
possibly actions) as inputs (Meng et al., 2021; Zhu et al., 2017). More recently, 
motivated by the breakthrough success of Transformers over LSTMs in nat-
ural language processing, Parisotto et al. (2020) designed a new transformer 
architecture, namely GTrXL, which yielded significant improvements in terms 
of performance and robustness over LSTMs on a set of partially observable 
benchmarking tasks. A main advantage of GTrXL is the capability to vary the 
dimensionality of the input over time. While LSTMs generally require a fixed 
window of h past observations, requiring the use of dummy observations in 
the first h− 1 decision time-steps, the GTrXL can at every time-step base the 
decisions on the entire history of past observations (and actions). 
Both LSTM and GTrXL architectures compose fully model-free deep 
RL solutions to POMDPs. A third modeling option, which comprises a 
model-based/model-free hybrid solution, pertains to transformation of the 
POMDP problem into the belief-MDP by computing beliefs via Bayes Theorem 
(Equation 1). The belief-MDP is then solved via classical deep model-free RL 
methods with feed-forward NNs (Andriotis & Papakonstantinou, 2019; Morato 
et al., 2023). We here compare the performance of the two model-free and the 
hybrid solution, referred to as “belief-input” case, on the real-world POMDP 
problem of railway maintenance planning that has been presented in Section 
3, with parameter inference described in Section 4. While Parisotto et al. 
(2020) demonstrate the superiority of Transformers over LSTMs on simulated 
tasks, our work offers a further comparison of the two methods, and confirms
 
POMDP inference and robust solution via deep reinforcement learning 17 
the superiority of the former, on a real-world stochastic (both in the transi-
tion dynamics and in the observation generating process), partially observable 
problem. 
For this comparison we set the POMDP parameters to the mean val-
ues of the distributions reported in Appendix A, in order to evaluate the 
methods without model uncertainty, with the latter case tackled in the next 
section. For all modeling options, the policy is learned via the Proximal Policy 
Optimization (PPO) algorithm with clipped surrogate objective (Schulman, 
Wolski, Dhariwal, Radford, & Klimov, 2017). The overall evaluation algorithm 
is reported in pseudocode format in Algorithm 1. In addition, the code of the 
experiment is made available online2. We consider 50 time-steps, i.e., 25 years 
(1 time-step equals 6 months), as the decision horizon H of the problem, as 
discussed with our SBB partners. 
For all methods, the policy networks are updated every 4,000 training time-
steps. Every 5 updates, 500 evaluation episodes are run with different random 
seeds in order to average the results over the stochasticity of the environment. 
In addition, the entire analysis is repeated a second time (with a different 
random seed) to further average the results over the stochasticity of the NN 
training. Grid-searches are performed over the hyperparameters for all meth-
ods and the selected values are reported in Table B1 in Appendix B. The 
average performance over 250 evaluation iterations (5 million training time-
steps) is plotted in Figure 3. Along with the three evaluated methods, two 
additional benchmarking solutions are reported. The first option refers to the 
QMDP method (Littman, Cassandra, & Kaelbling, 1995), which constitutes a 
POMDP solution based on DP, and which turns out to be an effective solution 
for the characteristics of this problem (Arcieri et al., 2023). The second option 
2Code available on GitHub.
 
18 POMDP inference and robust solution via deep reinforcement learning 
Algorithm 1 Evaluation algorithm 
1: Initialize policy network πϕ 
2: Initialize replay buffer D ← ∅ 3: Set environment parameters θ̂ to the mean values of p(θ | D) 4: for training episode = 0 to N do 5: Sample initial s0 ∼ T0θ̂ 
and z0 ∼ O0θ̂ 6: Initialize belief to initial state distribution b0 ← T0θ̂ 7: for timestep t = 0 to H do 8: if belief-input case then 9: Input yt = bt 
10: else if LSTM then 11: Input yt = (zt, at−1, · · · , zt−h+1) ▷ h = 3 12: else if GTrXL then 13: Input yt = (zt, at−1, · · · , z0) 14: end if 15: at ∼ πϕ(yt) 16: st+1 ∼ Tθ̂(st, at), zt+1 ∼ Oθ̂(st+1, at, zt) 17: Compute bt+1 via Equation 1 18: D ← D ∪ {(yt, at, R (st, at))} 19: end for 20: every K total timesteps do ▷ K = 4, 000 21: Update πϕ with PPO and replay buffer D 22: every 5 updates do 23: Run 500 policy evaluation episodes without exploration 24: end for 
is the optimal MDP solution, namely the optimal policy computed and evalu-
ated on the underlying MDP, i.e., when the hidden states are fully observable. 
The latter constitutes an upper bound to any POMDP solution, which cannot 
be exceeded, given the irreducible inherent uncertainty of the observations, 
and serves as a benchmarking reference. 
The belief-input method outperforms the other two model-free RL solu-
tions and already shows strong performance at the first evaluation iterations. 
The method converges to the best policy within a few iterations, as reported 
in the zoomed-in view of the first 70 evaluation iterations reported in the lower 
left figure inset, matching the QMDP method with few policy updates. Because
 
POMDP inference and robust solution via deep reinforcement learning 19 
Evaluation iteration 
T o ta l co st s 
Fig. 3: Comparison of the performance of LSTM (green), GTrXL (orange), and the belief-input case (blue) over 250 evaluation iterations. At every iteration, 500 trial episodes are evaluated with different random seeds and the average results are returned. The entire analysis is repeated for a second random seed and the average performance is plotted. An evaluation iteration is run after 5 policy updates and a policy update is performed every 4,000 training time-steps, for a total of 5 million time-steps. The performance is further benchmarked against the QMDP method (dashed red) and the optimal MDP policy (dashed yellow). On the left corner, a zoomed-in plot of the belief-input performance over the first 70 evaluation iterations. 
the number of training time-steps evaluated may not be sufficient for conver-
gence of the other two model-free RL methods, we continue training up to 
2,000 evaluation iterations (40 million training time-steps). This could however 
negatively impact the performance of the belief-input method, which already 
converged and may begin to suffer from overfitting. The extended training 
is reported in Figure 4, where a rolling average window of 5 steps is further 
applied for illustration purposes. 
As expected, the performance of the belief-input method slightly decreases 
over time. The GTrXL is proven to deliver a better architecture than the LSTM 
for POMDP applications, also for this particular case of application on a real-
world problem. The GTrXL is indeed less affected by variance and eventually 
converges to a better policy, albeit still far from the QMDP benchmark and 
the best policy with the belief-input method.
 
20 POMDP inference and robust solution via deep reinforcement learning 
Evaluation iteration 
T o ta l co st s 
Fig. 4: Comparison of the performance of LSTM (green), GTrXL (orange), and the belief-input case (blue) over 2,000 evaluation iterations, for a total of 40 million training time-steps. The performance is further plotted with an average rolling window of 5 steps for displaying purposes. 
Finally, for all three methods we saved the best models, which were eval-
uated during training and evaluated the learned policies over 100,000 trials. 
The results are reported in Table 2 in terms of average performance, Standard 
Error (SE), best (Max) and worst (Min) trial. In the table, the belief-input 
case average performance is close but slightly worse than the QMDP method. 
This is likely due to the fact that the best model was picked based on an 
average over 500 trials, which is still subject to a significant standard error. 
Table 2: Performance of the best models inferred during the training process, evaluated over 100,000 simulations. 
Method Avg. performance SE Max Min 
Optimal MDP -13,315 27 -5,000 -93,980 QMDP -14,374 35 -5,050 -123,800 Belief-input -14,677 36 -5,050 -121,950 GTrXL -17,196 46 -5,700 -188,600 LSTM -18,167 42 -5,100 -404,150
 
POMDP inference and robust solution via deep reinforcement learning 21 
6 Domain randomization for robust solution 
Further to the challenge of POMDP inference, another key issue is the robust-
ness of the deep RL solutions. RL methods generally learn an optimal policy 
by interacting with a simulator. When the trained RL agent is deployed to 
the real-world, the performance can deteriorate, or altogether fail, due to 
the “simulation-to-reality” gap (Salvato, Fenu, Medvet, & Pellegrino, 2021; 
Zhao, Queralta, & Westerlund, 2020), if the solution is not robust to model 
uncertainty. 
In Arcieri et al. (2023), we propose a framework in combination with 
the POMDP inference to enhance the robustness of DP solutions to model 
uncertainty. Namely, the POMDP parameter distributions inferred via MCMC 
sampling are incorporated into the solution by merging DP algorithms with 
Bayesian decision making. In Bayesian decision theory (Berger, 2013), given 
a utility function U(θ, a) that maps possible outcomes to their utility, the 
parameters θ of the problem, and some decision a, the Bayesian optimal action 
is the one which maximizes the expected utility with respect to parameter 
uncertainty: 
a∗ = argmax a∈A 
Eθ∼p(θ) [U(θ, a)] (6) 
In Arcieri et al. (2023) we incorporate DP methods into Equation 6 to 
derive solutions that maximize the expected value with respect to the entire 
model parameter distributions, hence rendering the solution robust to model 
uncertainty. 
In this work, we bring this framework into the RL training scheme. The 
utility function is represented by the RL algorithm objective function, e.g., the 
PPO clipped surrogate objective in this case. We propose the use of domain 
randomization (Tobin et al., 2017) of the POMDP environment, which is 
enabled by our POMDP inference scheme through the recovery of parameter
 
22 POMDP inference and robust solution via deep reinforcement learning 
distributions, in order to enhance the robustness of the RL solution to model 
uncertainty. At every episode, a different POMDP configuration is sampled 
from the parameter distributions. The RL agent interacts with this POMDP 
configuration until the end of the episode. Afterwards, a new configuration 
of the environment is sampled. At the end of the training, the RL agent will 
have optimized the learned policy over all possible problem parameters to 
derive a solution robust to model uncertainty. The expectation in Equation 6 
is thus implemented in practice via stochastic gradient ascent/descent steps 
over varying randomized problem parameters. It should be reminded that the 
(Bayesian) robust optimal policy may be sub-optimal for a specific value θ, 
while maximizing the expected value with respect to the entire model param-
eter distribution. The domain randomization technique can thus be used in 
combination with the model inference proposed in Section 4 to establish a 
joint framework of POMDP inference and robust solution based on RL. The 
framework is depicted in the graphical model in Figure 5. 
p(θ | D) 
θ̂ 
Sample 
Environment 
Data collection 
POMDP inference 
Interactions 
Policy learning 
Domain randomization 
Fig. 5: The POMDP inference and robust solution framework via domain randomization and deep reinforcement learning. 
We showcase the implementation of this framework with the belief-input 
method, but it is also applicable with the other methods reported in Table 
2 given its general validity. The evaluation algorithm is similar to Algorithm
 
POMDP inference and robust solution via deep reinforcement learning 23 
1, with the only difference that the POMDP parameters θ̂ are sampled at 
every episode from the inferred posterior distributions p(θ | D). The policy 
updates are again performed every 4,000 training time-steps and an evaluation 
iteration is run every 5 policy updates. Similarly to Figure 4, the performance 
during training is averaged at each evaluation iteration over 500 episodes with 
different random seeds. The analysis is then repeated for a second random 
seed to also average over the stochasticity of the NN training. The resulting 
average performance is plotted in Figure 6. Given the more challenging learning 
task, owing to model uncertainty, the average training performance decreases 
and demonstrates a higher variance than the belief-input performance without 
domain randomization, shown in Figure 4. For this case, the hyper-parameter 
tuning was also restricted to a minimal grid-search. While the results are 
already satisfying, the RL agent performance can likely be further increased 
via a more thorough hyperparameter optimization. 
Again, the best performing models shown in the evaluations during train-
ing are saved and the learned policy is evaluated over 100,000 simulations. The 
results are shown in Table 3 and compared against the robust QMDP policy 
described in Arcieri et al. (2023) and the upper bound optimal MDP policy 
evaluated with full observability, both assessed under model uncertainty. In 
addition, we report the result of the best model of the RL agent from the pre-
vious analysis, namely with the policy optimized without model uncertainty 
incorporated into the training (i.e., no domain randomization), evaluated now 
in the context of model uncertainty. This further analysis resembles a real-
world deployment, where the environment parameters can differ from those 
inferred, inducing the aforementioned simulation-to-reality gap. The perfor-
mance of the agent trained with no domain randomization deteriorates, while
 
24 POMDP inference and robust solution via deep reinforcement learning 
Evaluation iteration 
T o ta l co st s 
Fig. 6: Performance of the belief-input case (blue) over 250 evaluation iterations with domain randomization, i.e., a different POMDP model is sampled at every episode, both for training and evaluation. At every iteration, 500 trial episodes are evaluated with different random seeds and the average results are returned. The entire analysis is repeated for a second random seed and the average performance is plotted. An evaluation iteration is run after 5 policy updates and a policy update is performed every 4,000 training time-steps, for a total of 5 million time-steps. The performance is further benchmarked against the robust QMDP method (dashed red) and the robust optimal MDP policy (dashed yellow), evaluated under model uncertainty as in Arcieri et al. (2023). 
the agent trained with domain randomization is able to learn and deliver a 
more robust policy in the context of model uncertainty. 
Table 3: Performance of the best models during training evaluated over 100,000 simulations in the context of model uncertainty with domain randomization. In particular, we report on the evaluation of the belief-input agent trained with (DR) and without Domain Randomization (no DR). The former achieves a significantly improved and more robust policy. 
Method Avg. performance SE Max Min 
Optimal MDP -13,374 33 -5,000 -190,450 QMDP -14,526 39 -5,050 -197,050 Belief-input DR -14,648 38 -5,050 -168,600 Belief-input no DR -14,901 39 -5,050 -205,100 
Finally, Figure 7 shows two trials of the maintenance actions planned by 
the belief-input model, which has been trained with domain randomization. 
From bottom to top: the observations (fractal values); the beliefs, namely the
 
POMDP inference and robust solution via deep reinforcement learning 25 
Timestep 
A c ti o n 
S ta 
te B e li e f 
O b s 
Timestep 
A c ti o n 
S ta 
te B e li e f 
O b s 
Fig. 7: Two trials of the maintenance actions planned by the belief-input model trained with domain randomization. From bottom to top: the observations (fractal values); the beliefs, namely a probability distribution over hidden states, computed via Bayes’ formula and fed to the policy networks; the true hidden states, which are not accessed by the agent and/or the model; the actions planned by the RL agent. 
probability distribution over hidden states, computed via Bayes’ formula and 
fed to the policy networks; the true hidden states, which are not accessed by 
the agent and/or the belief computations; the actions planned by the RL agent. 
7 Conclusion 
This work tackles two key issues relating to adoption of RL applications in real-
world partially observable planning problems. Firstly, a POMDP model, which 
enables the RL training via simulations, is often unknown and generally non-
trivial to infer, with unified best practices not available in the literature. This 
constitutes a main obstacle against broad adoption of the POMDP scheme and 
its solution methods for real-world applications. Second, RL solutions often 
lack robustness to model uncertainty and suffer from the simulation-to-reality 
gap.
 
26 POMDP inference and robust solution via deep reinforcement learning 
In this work, we tackle both issues via a combined framework for inference 
and robust solution of POMDPs based on deep RL algorithms. The POMDP 
inference is carried out via MCMC sampling of a HMM conditioned on actions, 
which jointly estimates the full distributions of plausible values of the transi-
tion and observation model parameters. Then, the parameter distributions are 
incorporated into the solution via domain randomization of the environment, 
enabling the RL agent to learn a policy, which is optimized over the space 
of plausible problem parameters and is, thus, robust to model uncertainty. 
We compare three common RL modeling options, namely a Transformer and 
an LSTM-based approach, which constitute model-free RL solutions, and a 
hybrid belief-input case. We implement our methods for optimal maintenance 
planning of railway tracks based on real-world monitoring data. While the 
Transformer delivers generally better performance than the LSTM, both meth-
ods are significantly outperformed by the hybrid belief-input case. In addition, 
we demonstrate on the latter method that an RL agent trained with domain 
randomization is able to learn an improved policy, which is robust to model 
uncertainty, than an RL agent trained without domain randomization. 
A possible limitation of this work is that, while our methods allow for 
incorporation of rather complex extensions, e.g., time-dependent dynamics and 
hierarchical components, and are here demonstrated on the quite difficult case 
of continuous observations, the POMDP inference under continuous multi-
dimensional states and actions is still to be investigated. Future work will focus 
on the development of methods that can scale to these cases, e.g, via coupling 
with deep model-based RL methods (Arcieri, Wölfle, & Chatzi, 2021). 
Acknowledgments. The authors acknowledge the support of the Swiss 
Federal Railways (SBB) as part of the ETH Mobility Initiative project
 
POMDP inference and robust solution via deep reinforcement learning 27 
REASSESS. The authors thank the ETH cluster support for their precious 
help with the availability of computational power. 
Declarations 
Funding 
The authors acknowledge the support of the Swiss Federal Railways (SBB) as 
part of the ETH Mobility Initiative project REASSESS. 
Conflicts of interest/Competing interests 
The authors have no competing interests to declare that are relevant to the 
content of this article. 
Ethics approval 
Not applicable. 
Consent to participate 
Not applicable. 
Consent for publication 
Not applicable. No further consent is needed for publication of this research 
paper. 
Availability of data and material 
The real-world monitoring data used in this research paper is SBB proprietary 
and cannot be published.
 
28 POMDP inference and robust solution via deep reinforcement learning 
Code availability 
All code of the experiments of this research paper is made available on GitHub 
in public repositories linked in the paper. 
Authors’ contributions 
 Giacomo Arcieri: Conceptualization; Data curation; Formal analysis; Inves-
tigation; Methodology; Software; Visualization; Roles/Writing - original 
draft; Writing - review & editing. 
 Cyprien Hoelzl: Data curation; Roles/Writing - original draft. 
 Oliver Schwery: Funding acquisition; Validation. 
 Daniel Straub: Methodology; Supervision; Validation; Writing - review & 
editing. 
 Konstantinos G. Papakonstantinou: Methodology; Supervision; Validation; 
Writing - review & editing. 
 Eleni Chatzi: Conceptualization; Methodology; Funding acquisition; Project 
administration; Resources; Supervision; Validation; Writing - review & 
editing.
 
POMDP inference and robust solution via deep reinforcement learning 29 
Appendix A Inference results 
A.1 Transition model parameters 
Fig. A1: Transition matrix related to action do-nothing a0. The distribution at row i and column j is associated with the probability to transition from state i to j when action a0 is taken. Consistent with what is expected in deterioration processes the highest probabilities are assigned to the state remaining invariant (diagonal entries), lower probabilities exist for deterioration transitions (upper right triangle), and almost zero probability is assigned to improvements of the system (lower left triangle).
 
30 POMDP inference and robust solution via deep reinforcement learning 
Fig. A2: Transition matrix related to action a1 (tamping). The distribution at row i and column j is associated with the probability to transition from state i to j when action a1 is taken. Deterioration of the system (upper right triangle) reflects an almost zero probability, while it appears most probable to remain in the same condition or improve by a maximum of one state, which reflects the reduced influence of this action.
 
POMDP inference and robust solution via deep reinforcement learning 31 
Fig. A3: Transition matrix related to action a2 (renewal plus tamping). The distribution at row i and column j is associated with the probability to transition from state i to j when action a2 is taken. Transition to the best possible state s0 is consistently assigned the highest probability, regardless of the starting state, reflecting the higher repairing effect of this maintenance action.
 
32 POMDP inference and robust solution via deep reinforcement learning 
A.2 Observation model parameters 
(a) Posterior distributions of state-dependent parameters µd|st . 
(b) Posterior distributions of state-dependent parameters σd|st . 
(c) Posterior distributions of state-dependent parameters νd|st . 
Fig. A4: Posterior distributions of observation model parameters (deterioration process).
 
POMDP inference and robust solution via deep reinforcement learning 33 
(a) Posterior distributions of state-dependent parameters µr|st 
(b) Posterior distributions of state-dependent parameters σr|st . 
(c) Posterior distributions of state-dependent parameters νr|st . 
(d) Posterior distributions of the autoregressive parameters kr|at for a1 (left) and a2 
(right). 
Fig. A5: Posterior distributions of observation model parameters (repair process).
 
34 POMDP inference and robust solution via deep reinforcement learning 
(a) Posterior distributions of parameters µst0 . 
(b) Posterior distributions of parameters σst0 . 
(c) Posterior distributions of parameters νst0 . 
Fig. A6: Posterior distributions of observation model parameters (initial observation).
 
POMDP inference and robust solution via deep reinforcement learning 35 
Appendix B Hyperparameters 
Table B1: Best hyperparameters from the grid-search optimization. 
Hyperparmeter Belief (no DR) Belief (DR) GTrXL LSTM 
Hidden layers 3 3 2×GTrXL 1× LSTM+ 2×MLP Hidden size 100 100 - 100 Learning rate 0.0001 0.0001 0.001 0.001 Heads - - 8 -Head dimension - - 32 -Max seq. length - - 50 3 Memory - - 50 -Use prev. actions - - Yes Yes Clip parameter 0.01 0.01 0.3 0.3 
References 
Andriotis, C.P., & Papakonstantinou, K.G. (2019). Managing engineering 
systems with large state and action spaces through deep reinforcement 
learning. Reliability Engineering & System Safety , 191 , 106483. 
Andriotis, C.P., & Papakonstantinou, K.G. (2021). Deep reinforcement 
learning driven inspection and maintenance planning under incomplete 
information and constraints. Reliability Engineering & System Safety , 
212 , 107551. 
Andriotis, C.P., Papakonstantinou, K.G., Chatzi, E.N. (2021). Value of struc-
tural health information in partially observable stochastic environments. 
Structural Safety , 93 , 102072.
 
36 POMDP inference and robust solution via deep reinforcement learning 
Arcieri, G., Hoelzl, C., Schwery, O., Straub, D., Papakonstantinou, K.G., 
Chatzi, E. (2023). Bridging POMDPs and Bayesian decision making for 
robust maintenance planning under model uncertainty: An application 
to railway systems. Reliability Engineering & System Safety , 109496. 
Arcieri, G., Wölfle, D., Chatzi, E. (2021). Which Model to Trust: Assess-
ing the Influence of Models on the Performance of Reinforcement 
Learning Algorithms for Continuous Control Tasks. arXiv preprint 
arXiv:2110.13079 . 
Audley, M., & Andrews, J.D. (2013). The effects of tamping on railway 
track geometry degradation. Proceedings of the Institution of Mechanical 
Engineers, Part F: Journal of Rail and Rapid Transit , 227 . 
Berger, J.O. (2013). Statistical decision theory and Bayesian analysis. Springer 
Science & Business Media. 
Bertsekas, D. (2012). Dynamic programming and optimal control: Volume I 
(Vol. 1). Athena scientific. 
Cassandra, A.R. (1998). A survey of POMDP applications. Working notes of 
AAAI 1998 fall symposium on planning with partially observable Markov 
decision processes (Vol. 1724). 
Dung, L.T., Komeda, T., Takagi, M. (2008). Reinforcement learning 
for POMDP using state classification. Applied Artificial Intelligence, 
22 (7-8), 761–779.
 
POMDP inference and robust solution via deep reinforcement learning 37 
Durango, P.L., & Madanat, S.M. (2002). Optimal maintenance and repair 
policies in infrastructure management under uncertain facility deteriora-
tion rates: an adaptive control approach. Transportation Research Part 
A: Policy and Practice, 36 (9), 763–778. 
Ellis, H., Jiang, M., Corotis, R.B. (1995). Inspection, maintenance, and repair 
with partial observability. Journal of Infrastructure Systems, 1 (2), 92– 
99. 
Farrar, C.R., & Worden, K. (2012). Structural health monitoring: a machine 
learning perspective. John Wiley & Sons. 
Gelman, A., Carlin, J.B., Stern, H.S., Rubin, D.B. (1995). Bayesian data 
analysis. Chapman and Hall/CRC. 
Guo, C., & Liang, Z. (2022). A predictive Markov decision process for 
optimizing inspection and maintenance strategies of partially observ-
able multi-state systems. Reliability Engineering & System Safety , 226 , 
108683. 
Hoelzl, C., Dertimanis, V., Chatzi, E.N., Winklehner, D., Züger, S., Oprandi, 
A. (2021). Data driven condition assessment of railway infrastructure. 
Bridge maintenance, safety, management, life-cycle sustainability and 
innovations (pp. 3251–3259). CRC Press. 
Hoffman, M.D., Gelman, A., et al. (2014). The No-U-Turn sampler: adaptively 
setting path lengths in Hamiltonian Monte Carlo. Journal of Machine
 
38 POMDP inference and robust solution via deep reinforcement learning 
Learning Research, 15 (1), 1593–1623. 
Kıvanç, İ., Özgür-Ünlüakın, D., Bilgiç, T. (2022). Maintenance policy analysis 
of the regenerative air heater system using factored POMDPs. Reliability 
Engineering & System Safety , 219 , 108195. 
Koller, D., & Friedman, N. (2009). Probabilistic graphical models: principles 
and techniques. MIT press. 
Landgraf, M., & Hansmann, F. (2019). Fractal analysis as an innovative 
approach for evaluating the condition of railway tracks. Proceedings of 
the Institution of Mechanical Engineers, Part F: Journal of Rail and 
Rapid Transit , 233 . 
Littman, M.L., Cassandra, A.R., Kaelbling, L.P. (1995). Learning policies 
for partially observable environments: Scaling up. Machine learning 
proceedings (pp. 362–370). Elsevier. 
Luque, J., & Straub, D. (2019). Risk-based optimal inspection strategies for 
structural systems using dynamic Bayesian networks. Structural Safety , 
76 , 68–80. 
Madanat, S., & Ben-Akiva, M. (1994). Optimal inspection and repair policies 
for infrastructure facilities. Transportation science, 28 (1), 55–62.
 
POMDP inference and robust solution via deep reinforcement learning 39 
Memarzadeh, M., Pozzi, M., Zico Kolter, J. (2015). Optimal planning and 
learning in uncertain environments for the management of wind farms. 
Journal of Computing in Civil Engineering , 29 (5), 04014076. 
Meng, L., Gorbet, R., Kulić, D. (2021). Memory-based Deep Reinforcement 
Learning for POMDPs. 2021 IEEE/RSJ International Conference on 
Intelligent Robots and Systems (IROS) (pp. 5619–5626). 
Morato, P.G., Andriotis, C.P., Papakonstantinou, K.G., Rigo, P. (2023). Infer-
ence and dynamic decision-making for deteriorating systems with proba-
bilistic dependencies through Bayesian networks and deep reinforcement 
learning. Reliability Engineering & System Safety , 109144. 
Morato, P.G., Papakonstantinou, K.G., Andriotis, C.P., Nielsen, J.S., Rigo, P. 
(2022). Optimal inspection and maintenance planning for deteriorating 
structural components through dynamic Bayesian networks and Markov 
decision processes. Structural Safety , 94 , 102140. 
Papakonstantinou, K.G., Andriotis, C.P., Shinozuka, M. (2018). POMDP and 
MOMDP solutions for structural life-cycle cost minimization under par-
tial and mixed observability. Structure and Infrastructure Engineering , 
14 (7), 869–882. 
Papakonstantinou, K.G., & Shinozuka, M. (2014a). Planning structural inspec-
tion and maintenance policies via dynamic programming and Markov 
processes. Part II: POMDP implementation. Reliability Engineering &
 
40 POMDP inference and robust solution via deep reinforcement learning 
System Safety , 130 , 214–224. 
Papakonstantinou, K.G., & Shinozuka, M. (2014b). Planning structural 
inspection and maintenance policies via dynamic programming and 
Markov processes. Part I: Theory. Reliability Engineering & System 
Safety , 130 , 202–213. 
Parisotto, E., Song, F., Rae, J., Pascanu, R., Gulcehre, C., Jayakumar, S., 
. . . others (2020). Stabilizing transformers for reinforcement learning. 
International conference on machine learning (pp. 7487–7498). 
Salvato, E., Fenu, G., Medvet, E., Pellegrino, F.A. (2021). Crossing the real-
ity gap: A survey on sim-to-real transferability of robot controllers in 
reinforcement learning. IEEE Access, 9 , 153171–153187. 
Schmidhuber, J. (1990). Reinforcement learning in Markovian and non-
Markovian environments. Advances in Neural Information Processing 
Systems, 3 . 
Schöbi, R., & Chatzi, E.N. (2016). Maintenance planning using continuous-
state partially observable Markov decision processes and non-linear 
action models. Structure and Infrastructure Engineering , 12 (8), 977– 
994.
 
POMDP inference and robust solution via deep reinforcement learning 41 
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. (2017). Prox-
imal policy optimization algorithms. arXiv preprint arXiv:1707.06347 . 
Song, C., Zhang, C., Shafieezadeh, A., Xiao, R. (2022). Value of information 
analysis in non-stationary stochastic decision environments: A reliability-
assisted POMDP approach. Reliability Engineering & System Safety , 
217 , 108034. 
Straub, D., Chatzi, E., Bismut, E., Courage, W., Döhler, M., Faber, M.H., 
. . . others (2017). Value of information: A roadmap to quantifying the 
benefit of structural health monitoring. ICOSSAR-12th international 
conference on structural safety & reliability. 
Sutton, R.S., & Barto, A.G. (2018). Reinforcement learning: An introduction. 
MIT press. 
Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W., Abbeel, P. (2017). 
Domain randomization for transferring deep neural networks from sim-
ulation to the real world. 2017 IEEE/RSJ International Conference on 
Intelligent Robots and Systems (IROS) (pp. 23–30). 
Wang, H., Berkers, J., van den Hurk, N., Layegh, N.F. (2021). Study 
of loaded versus unloaded measurements in railway track inspection. 
Measurement , 169 , 108556. 
Wari, E., Zhu, W., Lim, G. (2023). A Discrete Partially Observable Markov 
Decision Process Model for the Maintenance Optimization of Oil and
 
42 POMDP inference and robust solution via deep reinforcement learning 
Gas Pipelines. Algorithms, 16 (1), 54. 
Zhao, W., Queralta, J.P., Westerlund, T. (2020). Sim-to-real transfer in deep 
reinforcement learning for robotics: a survey. 2020 IEEE symposium 
series on computational intelligence (SSCI) (pp. 737–744). 
Zhu, P., Li, X., Poupart, P., Miao, G. (2017). On improving deep reinforcement 
learning for POMDPs. arXiv preprint arXiv:1704.07978 .