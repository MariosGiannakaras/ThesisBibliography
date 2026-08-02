> Source: https://arxiv.org/pdf/2302.01248

Robust Markov Decision Processes without Model Estimation 
Wenhao Yang∗ Han Wang† Tadashi Kozuno‡ Scott M. Jordan† Zhihua Zhang§ 
September 13, 2023 
Abstract 
Robust Markov Decision Processes (MDPs) are receiving much attention in learning a robust policy which is less sensitive to environment changes. There are an increasing number of works analyzing sample-efficiency of robust MDPs. However, there are two major barriers to applying robust MDPs in practice. First, most works study robust MDPs in a model-based regime, where the transition probability needs to be estimated and requires a large amount of memories O(|S|2|A|). Second, prior work typically assumes a strong oracle to obtain the optimal solution as an intermediate step to solve robust MDPs. However, in practice, such an oracle does not exist usually. To remove the oracle, we transform the original robust MDPs into an alternative form, which allows us to use stochastic gradient methods to solve the robust MDPs. Moreover, we prove the alternative form still plays a similar role as the original form. With this new formulation, we devise a sample-efficient algorithm to solve the robust MDPs in a model-free regime, which does not require an oracle and trades off a lower storage requirement O(|S||A|) with being able to generate samples from a generative model or Markovian chain. Finally, we validate our theoretical findings via numerical experiments, showing the efficiency with the alternative form of robust MDPs. 
1 Introduction 
Current popular reinforcement learning (RL) algorithms rarely consider the distribution shift from simulation environments to real-world environments, which might make an RL agent suffer from a performance drop. From a theoretical perspective, a small perturbation of reward and transition probability can cause an optimal policy to become sub-optimal and a significant change in the value function [Mannor et al., 2004]. To alleviate sensitivity in environment shift, one combines MDPs [Sutton and Barto, 2018] with a DRO problem [Duchi and Namkoong, 2016, 2021, Namkoong and Duchi, 2016, Shapiro, 2017] to optimize the policy over the worst distribution within a region of the possible transition functions. And this region is called “uncertainty set”. The mathematical model of this problem is called robust MDPs [Iyengar, 2005, Satia and Lave Jr, 1973, Wiesemann et al., 2013] (see Section 2 for more details). 
∗Academy for Advanced Interdisciplinary Studies, Peking University; email: yangwenhaosms@pku.edu.cn. †Computing Science, University of Alberta. ‡OMRON SINIC X, Japan. §School of Mathematical Sciences, Peking University. 
1 
 
 
 
 
 
 
 
 
 
 
 
How to design a computationally efficient and sample-efficient algorithm for solving robust MDPs is a challenge. There exists some learning algorithms with polynomially computational complexity[Goyal and Grand-Clement, 2018, Ho et al., 2018, 2020], but it is still large in practice in terms of space memory, and they require the knowledge of underlying transition probabilities and rewards. In a data-driven scenario, other works [Panaganti and Kalathil, 2022, Si et al., 2020, Yang et al., 2022, Zhou et al., 2021] give the sample complexity of robust bandits and MDPs without the knowledge of underlying transition functions and rewards but only offline data. But these works ignore the computation complexity of solving DRO problems, which is expensive, and assume the optimal solution of a DRO problem can be obtained exactly from an oracle. Moreover, these two lines of works rely on either the true value or empirical estimation of transition functions and rewards, which requires a large space to store the model in memory. Therefore, a core question remains open: 
Can we design a practical algorithm with a low storage requirement to solve robust MDPs with sample-efficiency guarantees? 
In this paper we would address this issue by design an efficient algorithm with only O(|S||A|) storage, which is model-free [Chen and Wang, 2016]. And we offer the following main contributions. 
Contributions. Rather than solving original robust MDPs, we propose a surrogate of robust MDPs, where we remove the constraint on transition functions and instead treat it as a penalty in the value function. And we call the original one the “constrained” problem and the surrogate the “penalized” problem. The two different problems connect with each other via Lagrangian duality [Boyd et al., 2004]. The motivation from the transformation is two-staged. First, in order to design a model-free algorithm, we need to leverage the dual form [Shapiro, 2017] of the DRO problem, which could allow us to apply stochastic gradient methods. Second, solving a constrained DRO problem from its dual form will suffer from unbounded gradients [Namkoong and Duchi, 2016], which makes stochastic gradient method fail to converge. Thus, we introduce the penalized version which provide bounded gradient and finite-sample convergence guarantees. 
In Section 3, to validate whether the penalized robust MDPs is well-defined, we establish the same fundamental propositions used to develop constrained robust MDPs [Iyengar, 2005]. To be concrete, we show the Bellman equation still exists in the penalized setting and establish statistical results with a generative model [Azar et al., 2013]. Comparing to constrained robust MDPs in Yang et al. [2022], we find the statistical results are similar, which guarantee the reasonability of the penalized version. 
With the penalized form, the dual form of the DRO problem can be regarded as a risk minimization problem. Thus, it is natural to solve it by a stochastic gradient method, from which we do not require an oracle to the DRO problem solutions anymore. Leveraging on this, in Section 4, we design a “Q-learning” type algorithm and prove the sample complexity of our algorithm is polynomially dependent on the robust MDPs’ parameters (see the detail in Section 4), including state-action space size, discount factor, size of uncertainty set, etc. 
The previous approach required independent samples for each state-action pair, but in practice such a generating mechasim might not exist. This creates the algorithm in the generative model setting would be restricted in some scenarios. Instead, in Section 5, we consider a more realistic and difficult data generating mechanism, named Markovian data, where we can only observe one trajectory following a given behavior policy. Different from the generative model, only one sample could be generated for current visiting state-action pair in this setting. Again, under some regular 
2
assumptions, we design a “Q-learning” type algorithm and prove its sample complexity in this setting. However, the result relies heavily on some parameters than the generative model setting but is still polynomially dependent on the robust MDPs’ parameters. 
Finally, in Section 6, we conduct numerical experiments to demonstrate the utility of the penalized robust MDP formulation as a practical and efficiently solvable alternative to the constrained robust MDP formulation. 
Related Work. Robust MDPs were proposed by Iyengar [2005], Nilim and El Ghaoui [2005], Satia and Lave Jr [1973] to alleviate the sensitivity of optimal policies and value functions w.r.t. estimation errors of transition functions and rewards. Given the access to the true transition functions and rewards, many works have developed computationally efficient algorithms to solve the robust MDPs [Goyal and Grand-Clement, 2018, Ho et al., 2018, 2020, Lim et al., 2013, Wiesemann et al., 2013, Xu and Mannor, 2006]. If the true environment is unknown but samples can be generated from the environment, there are various works proving sample complexity bounds that tell us how many samples are sufficient to guarantee an accurate solution. In terms of model-based methods, Panaganti and Kalathil [2022], Shi and Chi [2022], Yang et al. [2022], Zhou et al. [2021] constructed empirical estimation of the transition functions and rewards from the samples. And they applied a variant of value iteration [Sutton and Barto, 2018] with the estimated model to solve robust MDPs. Although they gave the sample complexity of their algorithms, they did not consider the computation complexity of solving robust MDPs. For model-free methods, Liu et al. [2022] proposed a robust Q-learning algorithm to learn the robust Q-value function by multilevel Monte-Carlo method. Subsequently, Wang et al. [2023] showed the sample-complexity of this algorithm. And both of them require an oracle to solve the DRO problem. 
Despite the accomplishments of previous works, it is still unknown how to design an algorithm requiring less memory space (model-free) and theoretically efficient. In the primal form of constraint robust MDPs, we need to solve the DRO problem with |S|2|A| variables which requires significant computational and memory resources [Duchi and Namkoong, 2021, Namkoong and Duchi, 2016], from which a model-free algorithm is unlikely to be designed. Instead, if we solve the DRO problem from its Lagrangian dual form [Shapiro, 2017], it is possible to design a model-free algorithm . We provide the details in Sections 2 and 3. Because of the unbounded issue in the constraint problem, Sinha et al. [2017] changes the constraint problem to the penalty term in objective function. Using the penalty form, Jin et al. [2021], Qi et al. [2021] provide a theoretically efficient gradient method for DRO problem. Inspired by this transformation, we apply it to robust MDPs and design a sample-efficient and model-free algorithm. 
Moreover, to deal with the Markovian data setting, the algorithm we propose in Section 5 can also be regarded as a two-time-scale stochastic optimization problem. For linear case, several works [Doan et al., 2020, Gupta et al., 2019, Kaledin et al., 2020, Konda and Tsitsiklis, 2004] has studied the finite-sample results. For non-linear case, there are also some works [Doan, 2021a,b, Mokkadem and Pelletier, 2006, Zeng et al., 2021] study the finite-sample results. However, due to the non-smoothness of Q-learning, we can not apply the results of prior works directly. Moreover, to control the noise induced by Markovian data, we adapt a Poisson equation method Benveniste et al. [2012], Li et al. [2023], Métivier and Priouret [1987] in this paper. 
The remainder of this paper is organized as follows. In Section 2 we review distributionally robust optimization and robust Markov decision processes. In Section 3 we present rnative formulation for robust Markov decision processes. nt aWe then present our main results with a generative model and 
3
a Markovian data mechanism in Sections 4 and 5, respectively. We conduct experimental analysis in Section 6, and conclude our work in Section 7. We leave the proof details to the appendix. 
2 Preliminaries 
For any finite set X , we denote the set of probability distributions on X as ∆(X ). For any two probability distributions P,Q with a finite support X , Q≪ P signifies Q is absolutely continuous w.r.t. P , which means for any x ∈ X , P (x) = 0 implies Q(x) = 0. For a convex function f 
satisfying f(1) = 0, we define the f -divergence by Df (Q∥P ) := ∑ 
x∈X f ( Q(x) P (x) 
) P (x) for Q≪ P and 
Df (Q∥P ) := +∞ for Q is not absolutely continuous w.r.t. P . For a function f : Ω → R∪{−∞,+∞}, its convex conjugate is defined by f∗(t) := sups∈Ω{st− f(s)}. For a random variable X, we denote the sigma-algebra generated by X as σ(X). For a sequence of random variables {Xt}Tt=1, we denote the sigma-algebra generated by {Xt}Tt=1 as σ({Xt}Tt=1) := σ 
(⋃T t=1 σ(Xt) 
) . 
Distributionally Robust Optimization Let P ∗(·) be a probability distribution on a set X and V be a real-valued function on X . The constrained DRO problem [Shapiro, 2017] is formulated as: 
Rc(P ∗, V ) := inf 
Df (P∥P∗)≤ρ, 
P∈∆(X ) 
∑ x∈X 
P (x)V (x), (1) 
and its dual form is: 
Rc(P ∗, V ) = sup 
λ≥0,η∈R 
[ − λ 
∑ x∈X 
P ∗(x)f †η,λ,V (x)− λρ+ η 
] , (2) 
where f †η,λ,V (x) := f∗ ( η−V (x) 
λ 
) , and λ (≥ 0) and η are the dual variables w.r.t. constraints 
Df (P∥P ∗) ≤ ρ and ∑ 
x∈X P (x) = 1, respectively. Usually, we make some assumptions on the function f . 
Assumption 2.1. f(t) is a convex function on R. It satisfies f(1) = 0 and f(t) := +∞ when t < 0, and differentiable on R+. 
Due to the unbounded gradient issue in 2 [Namkoong and Duchi, 2016], some works replace the constraint Df (P∥P ∗) ≤ ρ with penalty [Jin et al., 2021, Qi et al., 2021, Sinha et al., 2017]: 
Rp(P ∗, V ) := inf 
P∈∆(X ) 
∑ x∈X 
P (x)V (x) + λDf (P∥P ∗). (3) 
Similar to (2), the dual problem of (3) is: 
Rp(P ∗, V ) = sup 
η∈R 
[ −λ 
∑ x∈X 
P ∗(x)f †η,λ,V (x) + η 
] , (4) 
where η is the dual variable w.r.t. constraint ∑ 
x∈X P (x) = 1. The robustness parameter for the constrained DRO problem is ρ, while it is λ for the penalized DRO problem. 
4
Robust Markov Decision Processes An MDP is defined by the tuple ⟨S,A, P ∗, R, γ⟩, where S is a finite state space, A is a finite action space, P ∗ : S × A → ∆(S) is the transition function, R : S ×A → [0, 1] is the reward function, and γ ∈ [0, 1) is the discount factor. A stationary policy is a function π : S → ∆(A). A trajectory induced by a policy π and P is (s0, a0, s1, a1, · · · ), where st+1 ∼ P (·|st, at), at ∼ π(·|st) and s0 is given or generated from an initial distribution. A robust MDP considers a set P of transition functions within a small region around P ∗. In the literature [Iyengar, 2005, Wiesemann et al., 2013], a (s, a)-rectangular uncertainty set w.r.t. a f -divergence is considered. Formally, the uncertainty set is defined by P := ⊗s,a∈S×APs,a(ρ), where 
Ps,a(ρ) := 
{ P (·|s, a) ∈ ∆(S) 
∣∣∣∣∣Df (P (·|s, a)∥P ∗(·|s, a)) ≤ ρ 
} . 
The value function under a policy π on an MDP is defined by V π P ∗(s) := Eπ,P ∗ 
[∑∞ t=0 γ 
tR(st, at)|s0 = s ] . 
In a robust MDP, there is a robust value function, which considers the worst case evaluation of value for all transition functions P ∈ P, i.e., V π 
rob,c(s) := infP∈P V π P (s), where “c” stands for word 
“constraint.” In this setting, it is shown the optimal robust value function V ∗ rob,c := maxπ V 
π rob,c 
satisfies a Bellman equation V ∗ rob,c = Trob,cV 
∗ rob,c [Iyengar, 2005, Zhou et al., 2021], where the robust 
Bellman operator Trob,c is defined by: 
Trob,cV (s) := max a∈A 
( R(s, a) + γ inf 
P (·|s,a)∈Ps,a(ρ) 
∑ s′∈S 
P (s′|s, a)V (s′) 
) (5) 
for any V ∈ V := [0, 1/(1− γ)]|S|. Indeed, the inner problem infP (·|s,a)∈Ps,a(ρ) 
∑ s′∈S P (s 
′|s, a)V (s′) is a DRO problem. We leverage the dual form of the DRO problem in Eqn. (2) and can rewrite the robust Bellman operator Trob,c by: 
Trob,cV (s) := max a∈A 
( R(s, a) + γ sup 
λ≥0,η∈R 
[ − λρ+ η − λ 
∑ s′∈S 
P ∗(s′|s, a)f †η,λ,V (s ′) 
]) , (6) 
where λ is the dual variable w.r.t. constraint P (·|s, a) ∈ Ps,a(ρ), and η is the dual variable w.r.t constraint 
∑ s′∈S P (s 
′|s, a) = 1. When transition function P ∗ is unknown, we can estimate it via offline dataset and substitute 
the empirical estimator P̂ for P ∗. Then the empirical uncertainty set P̂s,a(ρ) is defined by: 
P̂s,a(ρ) := 
{ P (·|s, a) ∈ ∆(S) 
∣∣∣∣∣Df (P (·|s, a)∥P̂ (·|s, a)) ≤ ρ 
} , 
and the corresponding empirical robust Bellman operator is defined by: 
T̂rob,cV (s) := max a∈A 
( R(s, a) + γ inf 
P∈P̂s,a(ρ) 
∑ s′∈S 
P (s′|s, a)V (s′) 
) . 
By the dual form (6), for each (s, a) pair, we can sample s′ ∼ P ∗(·|s, a) to get a stochastic unbiased gradient update the dual variable η. Once (6) is solved approximately, then we can obtain the near-optimal robust value function by the Q-learning algorithm. In this way, we can avoid estimating the transition functions and obtain a model-free method. 
5
3 Alternative Form of Robust MDPs 
However, solving (6) by stochastic gradient descent will suffer from unbounded gradient issue. Thus, it is impossible to derive theoretical guarantee for the convergence of stochastic gradient method from the dual form (6) [Bubeck et al., 2015]. To overcome this limitation, we propose a novel penalty version of robust value function with robustness parameter ρ replaced by λ: 
V π rob,p(s) := inf 
P∈∆(S)|S||A| EP,π 
[ ∞∑ t=0 
γt(R(st, at) + λγDf (P (·|st, at)∥P ∗(·|st, at))) ∣∣∣s0 = s 
] . (7) 
Similarly, we can also define a robust Bellman operator: 
Trob,pV (s) := max a∈A 
( R(s, a) + γ inf 
P (·|s,a)∈∆(S) 
[∑ s′∈S 
P (s′|s, a)V (s′) + λDf (P (·|s, a)∥P ∗(·|s, a)) 
]) . 
(8) 
Similar to Trob,c, the dual form of Trob,p is: 
Trob,pV (s) := max a∈A 
( R(s, a) + γ sup 
η∈R 
[ −λ 
∑ s′∈S 
P ∗(s′|s, a)f †η,λ,V (x) + η 
]) . 
For Q-value function, the robust Bellman operator is defined by: 
Trob,pQ(s, a) := R(s, a) + γ sup η∈R 
[ −λEs′∼P ∗ 
s,a f∗ ( η −maxa′ Q(s′, a′) 
λ 
) + η 
] . (9) 
In a high-level idea, (8) and (6) are connected with each other via Lagrange duality. The next proposition shows that the optimal robust value function maxπ V 
π rob,p is exactly the fixed point of 
Trob,p, which illustrates the reasonability of the penalized form. We defer the proof to Appendix A. 
Proposition 3.1. Trob,p is a γ-contraction operator on V. Thus, a fixed point V ∗ rob,p exists, and 
V ∗ rob,p = maxπ V 
π rob,p. 
Proposition 3.1 shows the penalized robust MDPs share the similar basic properties as constraint MDPs do. Subsequently, we provide a stronger connection between these two forms. In Theorem 3.1, we show for each given constraint robust MDP, there exists a penalized robust MDP, whose value functions are exactly the same. 
Theorem 3.1. For a given robust MDP with parameters ⟨S,A, R, P ∗, γ⟩ and f(·)-divergence, for a given constraint parameter ρ > 0 there exists a penalty parameter λ > 0, such that V ∗ 
rob,c(µ) = V ∗ 
rob,p(µ), where µ ∈ ∆(S) is a given initial distribution. Similarly, for a given penalty parameter λ > 0, there exists a constraint parameter ρ > 0, such that V ∗ 
rob,p(µ) = V ∗ rob,c(µ). 
Besides, in a data-driven scenario, we provide a result showing that robustness parameter λ plays a similar role in penalized robust MDPs with robustness parameter 1/ρ in constrained robust MDPs in a finite-sample regime in the following theorem. 
6
Theorem 3.2 (Statistical Equivalence). Suppose we access a generative model and estimate P̂ (s′|s, a) = 1 
n 
∑n i=1 1(X 
(s,a) i = s′), where X(s,a) 
i ∼ P ∗(·|s, a) are independent random variables. Choosing f(s) = (s− 1)2 where s ≥ 0, with probability 1− δ, we have: 
∥∥∥V̂ ∗ rob,p − V ∗ 
rob,p 
∥∥∥ ∞ 
≤ Õ 
max { 
1 λ(1−γ)2 
, λ } 
(1− γ) √ n 
 . 
Furthermore, there exists a class of penalized robust MDPs with f(s) = (s− 1)2, such that for every (ε, δ)-correct robust RL algorithm, when λ = O(1− γ), the total number of samples needed is at least: 
Ω̃ 
( |S||A|λ2 
ε2(1− γ)3 
) . 
Additionally, when λ = Ω(1− γ), the total number of samples needed is at least: 
Ω̃ 
( |S||A| 
ε2(1− γ)3 min 
{ 1 
16 , λγ(1− γ) 
2γ − 1 
}) . 
In Yang et al. [2022], the upper bound of constrained robust MDPs is Õ ( |S||A|(1+ρ)3 
ρ2ε2(1−γ)4 
) 1 with f(s) = 
(s− 1)2, and the lower bound is Ω̃ ( 
|S||A| ε2(1−γ)2 
min { 
1 1−γ , 
1 ρ 
}) . According to results of Theorem 3.2, 
the coefficient λ plays a similar role as 1/ρ does in constrained robust MDPs. When λ is small, we expect a robust solution, which leads to small sample complexity but conservative policy. When λ is large, we expect a non-robust solution, which means the sample complexity should be approximately equal with sample complexity of non-robust MDPs [Azar et al., 2013]. 
With all the background presented, we are ready to design a model-free algorithm by combing stochastic gradient method and Q-learning algorithm with sample efficiency guarantees. Prior to introducing our results, we simplify the notation and denote: 
J (s,a)(η, V ) := −λ ∑ s′∈S 
P ∗(s′|s, a)f †η,λ,V (s ′) + η. 
Additionally, the data is obtained in an online approach with a generative model, which means at each time step t, we have an observation s′t(s, a) ∼ P ∗(·|s, a) and rt(s, a) for each (s, a) pair satisfying E[rt(st, at)|st, at] = R(st, at). We denote 
J (s,a) t (η, V ; s′t(s, a)) := −λf †η,λ,V (s 
′ t(s, a)) + η, 
where E[J (s,a) t (η, V ; s′t(s, a))] = J (s,a)(η, V ). 
4 Results with a Generative Model 
In the traditional Q-learning algorithm with a generative model oracle, at the timestep t, for each (s, a) ∈ S ×A, the update rule is: 
Qt+1(s, a) = (1− βt)Qt(s, a) + βtT̂ Qt(s, a), 
1Here we reduce the |S|2 to |S| because we consider the deviation of value functions instead of ε-optimal policy, where we do not need a uniform bound over policy class and value function class as Yang et al. [2022] did. 
7
T̂ Qt(s, a) := rt(s, a) + γmax a′∈A 
Qt(s ′ t(s, a), a 
′), 
where s′t(s, a) ∼ P ∗(·|s, a) and Ert(s, a) = R(s, a). Wainwright [2019b] provided a O ( T− 1 
2 
) convergence rate when βt = 1 
1+(1−γ)t . In their analysis, a key point is that T̂ Qt is unbiased condition on Qt. Analogously, in robust MDPs scenario, we can also learn optimal Q∗ 
rob,p by: 
Qt+1(s, a) = (1− βt)Qt(s, a) + βtT̂rob,pQt(s, a), 
as long as we can obtain a “good” estimator T̂rob,pQt(s, a), which is approximately unbiased (ET̂rob,pQt(s, a) ≈ Trob,pQt(s, a)). Given the expression of T̂rob,pQ in (9), we notice that stochastic gradient method can be applied to achieve this goal. In the following part, we investigate the error between ET̂rob,pQt(s, a) and Trob,pQt(s, a). 
4.1 Estimating Trob,pQ 
As Trob,pQ(s, a) = R(s, a) + γ supη J (s,a)(η;V ), where V (s) := maxa∈AQ(s, a), we only need to 
study how to estimate supη J (s,a)(η;V ). The objective can be written by: 
J (s,a)(η, V ) = −λ ∑ s′∈S 
P ∗(s′|s, a)f †η,λ,V (s ′) + η = 
∑ s′∈S 
P ∗(s′|s, a)J(η, V ; s′), 
J(η, V ; s′) = −λf †η,λ,V (s ′) + η. 
Next, we consider an online i.i.d. data stream {s′t(s, a)}T−1 t=0 , where s′t(s, a) ∼ P ∗(·|s, a). Then, we 
can apply Stochastic Gradient Ascent (SGA) algorithm to approximate supη J (s,a)(η, V ): 
ηt+1(s, a) = ηt(s, a) + αt · ∂J(ηt(s, a), V ; s′t(s, a)) 
∂η , (10) 
where αt is the learning rate, and ∂J(ηt(s,a),V ;s′t(s,a)) ∂η is an unbiased estimator of ∂J(s,a)(ηt(s,a),V ) 
∂η . Noting that J (s,a)(η, V ) must be concave w.r.t. η as it is the dual form of problem (3) [Boyd et al., 2004], the convergence of SGA algorithm can be guaranteed. To specify the convergence rate, we make two basic assumptions for the objective J (s,a)(η, V ). 
Assumption 4.1. For any V ∈ [ 0, (1− γ)−1 
]|S| and (s, a) ∈ S × A, the optimal point η∗(s, a) = argmaxη∈R J 
(s,a)(η, V ) is finite. We can restrict the range of η in Θ ⊆ R, whose diameter is finite (denoted diam(Θ)) and is independent of P ∗. 
Assumption 4.2. J (s,a)(η, V ) is 1 λσ -smooth w.r.t. η ∈ Θ. 
In Assumption 4.1, we assume a finite region of dual variables to exclude some extreme cases. In Assumption 4.2, we assume the smoothness of J (s,a)(η, V ). Indeed, by Zhou [2018], if f(·) is a σ-strongly convex function, it comes f∗(·) is 1/σ-smooth and J (s,a)(η, V ) is 1/σλ-smooth. However, σ-strongly convexity of f(·) on R may fail for some function f(·), such as Cressie-Read family of f -divergences [Cressie and Read, 1984]. But with a given closed set Θ, the smoothness of J (s,a)(η, V ) can be guaranteed while the smoothness parameter may be dependent with the diameter of Θ. In this scenario, on a finite region Θ, the stochastic gradient can also be bounded (Lemma 4.1). Therefore, we can finally specify the convergence rate in Theorem 4.1. The proofs are deferred to the Appendix B. 
8
Lemma 4.1. If Assumptions 4.1 and 4.2 hold, for any η ∈ Θ and (s, a) ∈ S×A, s′(s, a) ∼ P ∗(·|s, a), then we have: ∣∣∣∣∂J(η, V ; s′(s, a)) 
∂η 
∣∣∣∣ ≤ diam(Θ) + (1− γ)−1 
λσ := Cg. 
Theorem 4.1 (Convergence guarantee). If Assumptions 4.1 and 4.2 hold, the i.i.d. data stream {s′t(s, a)}T−1 
t=0 is generated from P ∗, and the learning rate satisfies αt = diam(Θ) 
Cg 
√ t 
, then for any given 
V ∈ [ 0, (1− γ)−1 
]|S|, the convergence rate of the SGA algorithm in Eqn. (10) is: 
E [ 
max (s,a)∈S×A 
( sup η J (s,a)(η, V )− J (s,a)(ηT (s, a), V ) 
)] ≤ 
diam(Θ)Cg(2 + lnT )(4 √ 2 ln |S||A|+ 1)√ 
T . 
For example, we apply Theorem 4.1 to a specific case where f(t) = (t − 1)2. Similar with Lemma A.1 in Appendix A, we can show Θ = [−2λ, 2(1− γ)−1 +2λ], which satisfies Assumption 4.1. Then, the convergence rate becomes supη J(η, V )− E[J(ηT , V )] ≤ (3(1−γ)−1+4λ)2(2+log T ) 
λσ √ T 
. 
4.2 Learning Q∗ rob,p 
In this section, we combine the gradient method in Section 4.1 with Q-learning algorithm to learn the optimal robust Q-value function Q∗ 
rob,p, where we run multiple gradient steps for dual variables η between each Q-learning step in Algorithm 1. The high-level idea is if the number of multiple gradient steps are enough, then ηt,T ′(s, a) ≈ argmaxη J 
(s,a)(η, Vt), which leads to Es′t 
[J(ηt,T ′(s, a), Vt; s ′ t(s, a))] ≈ supη J 
(s,a)(η, Vt). In Algorithm 1, ΠΘ is the projection onto Θ in the Euclidean norm. Moreover, we also need to make sure the range of Qt remains unchanged during the training process or it will blow up. Thus, we assume the range of |J(η, V ; s′)| is bounded by a constant CM in Assumption 4.3. Then |Qt(s, a)| is also bounded by CM as CM ≥ (1− γ)−1. 
Assumption 4.3. For any η ∈ Θ, V ∈ [0, (1−γ)−1], and s′ ∼ P ∗(·|s, a), we have |J(η, V ; s′)| ≤ CM , where CM ≥ (1− γ)−1. 
Algorithm 1 Model-free approach to robust MDPs 
Input: Q0(s, a) = (1− γ)−1 for all (s, a) ∈ S ×A. for iteration t = 0 to T − 1 do Vt = Π[0,(1−γ)−1] (maxaQt(·, a)); for each state-action pair (s, a) ∈ S ×A do 
Set ηt,0(s, a) = 0. for iteration t′ = 0 to T ′ − 1 do 
Receive next state s′t,t′(s, a) ∼ P ∗(·|s, a). 
ηt,t′+1(s, a) = ΠΘ 
( ηt,t′(s, a) + αt′ 
∂J(ηt,t′ (s,a),Vt;s′t,t′ (s,a)) 
∂η 
) ; 
end for Receive reward rt(s, a) and next state s′t(s, a); Qt+1(s, a) = (1− βt)Qt(s, a) + βt(rt + γJ(ηt,T ′(s, a), Vt; s 
′ t(s, a))); 
end for end for 
9
Below we give a proof sketch to the convergence guarantee for Algorithm 1. The detailed proofs of the lemmas and theorems in this section are deferred to Appendix C. To ease the notation, in Algorithm 1, we recursively define two sequences (Ft) 
T t=−1 and (Gt) 
T t=−1 by (t ≥ 0): 
Gt−1 = σ ( Ft−1 ∪ σ 
( {s′t,t′}T 
′−1 t′=0 
)) , 
Ft = σ ( Gt−1 ∪ σ 
( {rt, s′t} 
)) , 
where F−1 := σ({∅}). 
Error Decomposition. For each (s, a) ∈ S ×A, at iteration t+ 1, we have 
Qt+1(s, a)−Q∗(s, a) =(1− βt)(Qt(s, a)−Q∗(s, a)) 
+ βt(rt(s, a)− E[rt(s, a)] + γ(Ĵt(s, a)− J∗(s, a))), 
where Ĵt(s, a) := J(ηt,T ′(s, a), Vt; s ′ t(s, a)) and J∗(s, a) = supη J 
(s,a)(η;V ∗ rob,p). We also construct 
auxiliary terms J̃t(s, a) := J (s,a)(ηt,T ′(s, a), Vt) and J̄t(s, a) := maxη J (s,a)(η, Vt). We can decompose 
Ĵt(s, a)− J∗(s, a) into three terms: 
Ĵt(s, a)− J∗(s, a) := It,1(s, a) + It,2(s, a) + It,3(s, a), 
where 
It,1 := Ĵt(s, a)− J̃t(s, a), 
It,2 := J̃t(s, a)− J̄t(s, a), 
It,3 := J̄t(s, a)− J∗(s, a). 
For It,1(s, a), we observe that its mean is zero under event Gt−1, which means E[It,1|Gt−1] = 0. For It,2(s, a), it is controlled by optimization error in Theorem 4.1, where we can determine T ′ such that E∥It,2∥∞ ≤ εopt. For It,3(s, a), we find |It,3(s, a)| ≤ ∥Vt − V ∗∥∞ by primal objective (8). Denoting ∆t(s, a) = Qt(s, a)−Q∗(s, a) and εr,t(s, a) = rt(s, a)− Ert(s, a), we have: 
∆t+1(s, a) ≤(1− βt)∆t(s, a) + βt(εr,t(s, a) + γIt,1(s, a) + γIt,2(s, a) + γIt,3(s, a)) 
≤(1− βt)∆t(s, a) + βt(εr,t(s, a) + γIt,1(s, a) + γ∥It,2∥∞1+ γ∥∆t∥∞1). 
Reversely, we also have: 
∆t+1(s, a) ≥(1− βt)∆t(s, a) + βt(εr,t(s, a) + γIt,1(s, a)− γ∥It,2∥∞1− γ∥∆t∥∞1). 
Then we construct auxiliary sequences: 
at+1 = (1− βt(1− γ))at, 
bt+1 = (1− βt(1− γ))bt + γβt∥Nt∥∞, ct+1 = (1− βt(1− γ))ct + γβt∥It,2∥∞, 
Nt+1(s, a) = (1− βt)Nt(s, a) + βt(εr,t(s, a) + γIt,1(s, a)), 
where a0 = ∥∆0∥∞, b0 = c0 = 0 and N0 = 0. It can be verified: 
−(at + bt + ct)1+Nt ≤ ∆t ≤ (at + bt + ct)1+Nt. 
10
Concentration on Nt. Noting that εr,t(s, a) and It,1(s, a) are bounded mean zero random variables, we can construct a Hoeffding bound for Nt. 
Lemma 4.2. If (1−βt)βt−1 ≤ βt and Assumption 4.3 holds, then the expectation of ∥Nt∥∞ satisfies: 
E[∥Nt∥∞] ≤ 2 √ 2βt−1(1 + γCM )2 ln(2|S||A|). 
Concentration on It,2. Directly applying Theorem 4.1 with V = Vt, we deduce the following convergence rate. 
Lemma 4.3. At any time step t, if αt′ = diam(Θ) 
Cg 
√ t′ 
, then 
E∥It,2∥∞ ≤ diam(Θ)Cg(2 + lnT ′)(4 
√ 2 ln |S||A|+ 1)√ 
T ′ . 
Convergence of at, bt and ct. We can write the explicit expressions of at, bt and ct with βt, ∥Nt∥∞ and ∥It,2∥∞. 
Lemma 4.4. It is true that aT , bt, and cT satisfies 
aT = a0 · T−1∏ t=0 
(1− βt(1− γ)), 
bT = 
T−1∑ t=0 
γβt∥Nt∥∞ · T−1∏ i=t+1 
(1− βi(1− γ)), 
cT = 
T−1∑ t=0 
γβt∥It,2∥∞ · T−1∏ i=t+1 
(1− βi(1− γ)), 
where ∏j 
t=i xt := 1 if i > j for any sequence {xt}. 
By Lemma 4.4, we can write an explicit expression of the deviation ∆t in the following lemma. The first term is the upper bound of E[∥NT ∥∞] in Lemma 4.2. The rate of this term is determined by the learing rate βT . The second term arises from the expression of aT . In the braces, the third and forth term arise from the expression of bT and cT respectively. 
Lemma 4.5. We have: 
E∥∆T ∥∞ ≤ √ βTCN + ∥∆0∥∞ · 
( 1− 
T−1∑ t=0 
βt,T−1 
) + 
γ 
1− γ 
T−1∑ t=0 
βt,T−1 
(√ βt−1CN + E∥It,2∥∞ 
) , 
where CN := 2 √ 2(1 + γCM )2 log(2|S||A|), and βi,j := (1− γ)βi 
∏j t=i+1(1− βt(1− γ)). 
Finally, we specify the learning rate to be βt = 1 1+(1−γ)(1+t) . With all we have ahead, we have 
the convergence result of Algorithm 1 in Theorem 4.2. 
11
Theorem 4.2. If Assumptions 4.1 and 4.3 hold, then for αt′ = diam(Θ) 
Cg 
√ t′ 
and βt = 1 1+(1−γ)(t+1) , we 
have: 
E[∥∆T ∥∞] ≤ ∥∆0∥∞ 1 + (1− γ)T 
+ 2CN√ 
(1− γ)3T + 
diam(Θ)Cg(2 + log T ′) 
(1− γ) √ T ′ 
+ CN√ 
1 + (1− γ)T , (11) 
where CM , diam(Θ) and Cg are dependent with choice of f and CN := 2 √ 2(1 + γCM )2 log(2|S||A|). 
Thus, to obtain an ε-optimal Q-value function, the total number of sample complexity is: 
|S||A|·O ( 
C2 N 
ε2(1− γ)3 
) · Õ 
( diam(Θ)2C2 
g 
ε2(1− γ)2 
) = Õ 
( |S||A|diam(Θ)2C2 
NC 2 g 
ε4(1− γ)5 
) . 
To be more concrete, we still apply f(t) = (t− 1)2 to this theorem. In this case, we can verify 
diam(Θ) = 2 1−γ +4λ, CM = 1 
1−γ , CN = 2 √ 
2 log(2|S||A|) 1−γ and Cg = 3 
4λ(1−γ) +2. Then, the total sample 
complexity for f(t) = (t− 1)2 is Õ ( 
|S||A| ε4(1−γ)7 
max { 
1 λ2(1−γ)4 
, 16λ2 }) 
. 
Discussion. So far, Theorem 4.2 answers how many samples are sufficient to guarantee an ε-optimal Q-value function for robust MDPs without an oracle to DRO solutions. We will discuss some points on the setting of parameters in Algorithm 1. 
 Choice of αt′ : The inner optimization problem is indeed a convex stochastic optimization problem. Fontaine et al. [2021] proved that the convergence rate would be Õ(T−k∧(1−k)) if αt′ = t′−k where k ∈ (0, 1). Thus, the choice of αt′ is the best we hope for in Theorem 4.1. 
 Choice of βt: By Lemma 4.5, the convergence will still be guaranteed if we choose another learning rate scheme such as βt = t−k, where k ∈ (0, 1). As pointed out in Wainwright [2019b], the convergence rate would be slower than linear scale learning rate. 
 Choice of ηt,0: In Theorem 4.1, we find the convergence rate is not related with the initial point, which is due to a loose inequality with diam(Θ). Therefore, in Algorithm 1, we force the initial point of inner optimization problem to be fixed at zero. In practice, we can set ηt,0 = ηt−1,T ′ to save iteration complexity. However, how to theoretically prove it is challenging because the value function Vt is changing w.r.t. t. 
 Choice of T ′. By Lemma 4.5, the coefficient of E[∥It,2∥∞] is βt,T−1. Thus, we don’t need to require E[∥It,2∥∞] ≤ εopt for a fixed optimization error εopt at any time step t. Instead, as long as ∑T−1 
t=0 βt,T−1E[∥It,2∥∞] converges finitely, the optimization error E[∥It,2∥∞] can vary w.r.t. t. 
5 Results with Markovian Data 
In Section 4, we introduce Algorithm 1 to learn the optimal robust Q-value function. The data generating mechanism is the generative model. However, the generative model is far away from the realistic scenario. In this section, we consider a more practical data generating mechanism, namely Markovian data [Li et al., 2020b]. Under the mechanism, we can only observe the samples from a single trajectory (s0, a0, s1, a1, · · · ), where s0 ∼ µ(·), at ∼ πb(·|st), st+1 ∼ P ∗(·|st, at). Unlike the 
12
generative model, we can not query next states for each (s, a) pairs. Then, Algorithm 1 does not fit in this setting. A straightforward modification to the algorithm is that we only update the Q-value and dual variable for the current visited (s, a) pair as shown in Algorithm 2. 
Algorithm 2 Model-free approach to robust MDPs (Markovian Data) 
Input: Q0(s, a) = 1/(1− γ) for all (s, a) ∈ S ×A. for iteration t = 0 to T − 1 do 
Perform at ∼ π(·|st), and receive reward r(st, at) and next state st+1 ∼ P ∗(·|st, at); Qt+1(st, at) = (1− βt)Qt(st, at) + βt(r(st, at) + γĴ (st,at)(η(st, at);Vt)); ηt+1(st, at) = ΠΘ 
( ηt(st, at) + αt 
∂Ĵ(st,at)(η(st,at);Vt) ∂η 
) ; 
Vt+1 = maxaQt+1(·, a); end for 
However, in order to guarantee the convergence of Algorithm 2, several additional assumptions are needed. The first one is the induced Markovian chain by policy πb converges to its stationary distribution geometrically fast. In Assumption 5.1, the convergence rate ρ is related with the mixing time τmix by τmix = ln 4M 
log ρ−1 ≈ ln 4M 1−ρ when ρ approaches 1. A fast mixing Markovian chain implies 
that the pairs (st, at) we observe are almost i.i.d. generated from the stationary distribution dπb (·) 
as long as t is sufficiently large. 
Assumption 5.1. For the given policy π in 2, the Markovian chain (s0, a0, s1, a1, · · · ) is fast mixing, that is, 
sup (s,a)∈S×A 
dTV (P π t (·|(s, a)), dπ(·)) ≤Mρt, 
where M > 0 and ρ ∈ (0, 1). And P π t := (P π)t, and dπ(·) is the stationary distribution of the 
Markovian chain, which satisfies: 
d⊤π = d⊤π P π. 
Moreover, we denote dmin := min(s,a)∈S×A dπ(s, a). 
In addition, we also require additional assumptions for J (s,a)(η;V ). Assumption 5.2 implies the objective is strongly-convex at its optimal point. In this case, the convergence rate for solving supη J 
(s,a)(η;V ) can be faster than the convex case, which enables we alternatively update variables ηt and Qt in Algorithm 2. Moreover, by the dual objective (4), we have Lemma 5.1, guaranteeing that the optimal solutions w.r.t. different values do not differ too much if the values are close. 
Assumption 5.2. For any given V ∈ [0, (1−γ)−1]|S|, there exists κ > 0 such for each (s, a) ∈ S×A that J (s,a)(η;V ) satisfies: 
∇J (s,a)(η;V ) · (η − η∗V (s, a)) ≤ −κ · (η − η∗V (s, a)) 2. 
Lemma 5.1. For any V1, V2 ∈ [0, (1− γ)−1]|S|, we have:∣∣η∗V1 (s, a)− η∗V2 
(s, a) ∣∣ ≤ ∥V1 − V2∥∞ . 
13
Taking f(t) = (t− 1)2 as an example, for any given (s, a) ∈ S ×A, we have: 
J (s,a)(η;V ) = −λEs′∼P ∗(·|s,a)f ∗ ( η − V (s′) 
λ 
) + η 
= − Es′∼P ∗(·|s,a)[(η + 2λ− V (s′))2+] 
4λ + λ+ η. 
Thus, the gradient of J (s,a)(η;V ) w.r.t. η is: 
∇J (s,a)(η;V ) = − Es′∼P ∗(·|s,a)[(η + 2λ− V (s′))+] 
2λ + 1. (12) 
Then we observe that η∗V (s, a) satisfies ∇J (s,a)(η∗V (s, a);V ) = 0. Moreover, the subgradient of ∇J (s,a)(η;V ) at η∗V (s, a) satisfies: 
∇2J (s,a)(η∗V (s, a);V ) ≤ − Es′∼P ∗(·|s,a)[1(η 
∗ V (s, a) + 2λ− V (s′) > 0)] 
2λ . 
By the Cauchy–Schwarz inequality, we have: 
4λ2 = ( Es′∼P ∗(·|s,a)[ 
( η∗V (s, a) + 2λ− V (s′) 
) + ] )2 
≤ Es′∼P ∗(·|s,a)[ ( η∗V (s, a) + 2λ− V (s′) 
)2 + ] · Es′∼P ∗(·|s,a)[1(η 
∗ V (s, a) + 2λ− V (s′) > 0)]. 
Moreover, we notice J (s,a)(η∗V (s, a);V ) ≥ 0 by primal objective. Thus, 
4λ2 ≤ 4λ(λ+ η∗V (s, a))Es′∼P ∗(·|s,a)[1(η ∗ V (s, a) + 2λ− V (s′) > 0)]. 
In addition, we have η∗V (s, a) ∈ [−λ, 2(1− γ)−1 + 2λ], which leads to 
∇2J (s,a)(η∗V (s, a);V ) ≤ − 1 
2(λ+ η∗V (s, a)) ≤ − 1 
6(λ+ (1− γ)−1) . (13) 
Then, Assumption 5.2 holds for f(t) = (t− 1)2 with κ−1 = 6(λ+ (1− γ)−1). We now give a proof sketch to the convergence for Algorithm 2. The detailed proofs in this 
section are deferred to Appendix D. 
Error Decomposition. Here we denote the error ∆t(s, a) = Qt+1(s, a)−Q∗ rob,p(s, a) and ξt is a 
random variable on S × A satisfying P (ξt+1 = (s′, a′)|ξt = (s, a)) = P ∗(s′|s, a)πb(a′|s′). Thus, by Algorithm 2, we have: 
∆t+1(s, a) =(1− βt1(ξt = (s, a)))∆t(s, a) + βt1(ξt = (s, a))(εr,t(s, a) + γεJ,t(s, a)) 
+ γβt1(ξt = (s, a)) ( J (s,a)(ηt(s, a);Vt)− J (s,a)(η∗t ;Vt) 
) + γβt1(ξt = (s, a)) 
( J (s,a)(η∗t ;Vt)− J (s,a)(η∗;V ∗ 
rob,p) ) . (14) 
Different from Section 4, here we introduce a new random variable sequence {ξt}t≥0 to represent only one pair (s, a) occurs at each time step. Moreover, we denote the filtration {Ft}t≥0 by (F0 := σ({∅})): 
Ft = σ ( {ξi}ti=0 ∪ {ri}t−1 
i=0 
) . 
14
In the decomposition, we denote: 
Zt,1(s, a) := 1(ξt = (s, a))(εr,t(s, a) + γεJ,t(s, a)), 
Zt,2(s, a) := γ1(ξt = (s, a)) ( J (s,a)(ηt(s, a);Vt)− J (s,a)(η∗t ;Vt) 
) , 
Zt,3(s, a) := γ1(ξt = (s, a)) ( J (s,a)(η∗t ;Vt)− J (s,a)(η∗;V ∗ 
rob,p) ) . 
It is worth noticing that E[Zt,1(s, a)|Ft] = 0, |Zt,2(s, a)| ≤ γ 2σλ |ηt(s, a) − η∗t (s, a)|2 by smoothness 
property in Assumption 4.2, and |Zt,3(s, a)| ≤ γ1(ξt = (s, a))∥∆t∥∞. Then, two things left to be done: (a) dealing with the ξt in the recursion; (b) controlling the error ∥ηt − η∗t ∥∞. 
Dealing ξt. In a high-level idea, when t is sufficiently large, we have E1(ξt = (s, a)) ≈ dπ(s, a) by fast mixing assumption 5.1. Thus, we can write the decomposition (14) into an abstract form: 
∆t+1(s, a) = (1− βtdπ(s, a))∆t(s, a) + βtft(s, a)(1(ξt = (s, a))− dπ(s, a)), 
where ∥ft∥ is almost surely bounded and adaptive to Ft. Then we decompose 1(ξt = (s, a))−dπ(s, a) into: 
1(ξt = (s, a))− dπ(s, a) = 
∞∑ k=0 
(Pk(s, a|ξt)− dπ(s, a))− ∞∑ k=1 
(Pk(s, a|ξt)− dπ(s, a)) 
:= ψ(s, a; ξt)− Pψ(s, a; ξt), 
where Pψ(s, a; ξt) := ∑ 
s′,a′ ψ(s, a; s ′, a′)P π(s′, a′|ξt) is one-step transition on ψ. This decomposition 
is also called Poisson equation method [Benveniste et al., 2012, Li et al., 2023, Métivier and Priouret, 1987]. Next, we plug in Pψ(s, a; ξt−1), which happens to be the conditional expectation E[ψ(s, a; ξt)|Ft]. Thus, the error can also be written by: 
∆t+1(s, a) =(1− βtdπ(s, a))∆t(s, a) + βtft(s, a) (ψ(s, a; ξt)− P(s, a; ξt−1)) 
+ βtft(s, a) (Pψ(s, a; ξt−1)− Pψ(s, a; ξt)) . (15) 
By Assumption 5.1, we can show |ψ(s, a; ξt)| ≤ M 1−ρ . Thus, Azuma-Hoeffding can be applied to deal 
with error induced by ψ(s, a; ξt)−P(s, a; ξt−1). For the error induced by Pψ(s, a; ξt−1)−Pψ(s, a; ξt), we can replace it with error induced by ft+1(s, a)− ft(s, a) according to change of summation. We leave the details to Appendix E. 
Controlling ∥ηt − η∗t ∥∞. A key obstacle for controlling ∥ηt − η∗t ∥∞ is that Vt keeps varying at each time step. By update rule in Algorithm 2, the error can be decomposed to two major terms (we ignore all the parameters independent with t here): 
(ηt+1(s, a)− η∗t+1(s, a)) 2 ≈(1−O(αt))(ηt(s, a)− η∗t (s, a)) 
2 +O ( (η∗t (s, a)− η∗t+1(s, a)) 
2 
αt 
) +Ht(s, a), 
where Ht(s, a) are some rest random terms induced by ξt, which is handled similarly with Eqn (15). With Lemma 5.1, we have (η∗t (s, a) − η∗t+1(s, a)) ≤ ∥Vt − Vt+1∥∞. Besides, by update rule in Algorithm 2, we have ∥Vt − Vt+1∥∞ = O(βt). Thus, we replace the error decomposition with: 
(ηt+1(s, a)− η∗t+1(s, a)) 2 ≈(1−O(αt))(ηt(s, a)− η∗t (s, a)) 
2 +O ( β2t αt 
) +Ht(s, a). 
15
Then, with some proper chosen αt and βt, we have the following lemma to determine the convergence rate of ∥ηt − η∗t ∥∞. 
Lemma 5.2. Let η∗t (s, a) := argmaxη J (s,a)(η;Vt) and δt(s, a) := ηt(s, a)− η∗t (s, a) in Algorithm 2. 
Then the following inequality holds: 
E∥δt+1∥2∞ ≤ Φ1 
(t+ 1) 1 3 
+ Φ2 ln(t+ 1 + p†) 
(t+ 1) 2 3 
+ Φ3 
(t+ 1) 2 3 
, 
where Φ1, Φ2 and Φ3 are dependent with instance parameters, which are deferred to Appendix D. 
Finally, combing Lemma 5.2 and error decomposition for ∆t in Eqn (15), the following Theorem specify the final convergence rate. 
Theorem 5.1. If Assumptions 5.1 and 5.2 hold, by taking αt = 1 
κdmin(t+pα) 2 3 
and βt = 1 (1−γ)dmin(t+p†) 
, 
where pα = 
⌈( dmax dmin 
) 3 2 
⌉ and p† = ⌈ dmax 
(1−γ)dmin ⌉, then the convergence rate for Algorithm 2 satisfies: 
E∥Qt −Q∗ rob,p∥∞ ≤ Õ 
( Φ1 
σλdmin(1− γ)2(t+ 1) 1 3 
) , 
where the expression of Φ1 is deferred to Appendix D. 
Here we also take f(t) = (t − 1)2 as an example to calculate the specific convergence rate in Theorem 5.1. By Eqn (13), we have κ = 1 
6(λ+(1−γ)−1) . In addition, we also take λ = 1 
1−γ , as the expression of Φ1 is complicated. Thus, the convergence rate is: 
E∥Qt −Q∗ rob,p∥∞ ≤ Õ 
max 
{ M √ 
ln 2|S||A| 1−ρ , 1 
(1−γ)2 
} d3min(1− γ)3(t+ 1) 
1 3 
 . 
Discussion. Theorem 5.1 presents the sample complexity of Algorithm 2 is O ( T− 1 
3 
) . Compared 
with Theorem 4.2, the dependence on T is improved. The major contribution belongs to Assump-tion 5.2, where we assume the objective is local strongly-convex. Indeed, Theorem 4.2 can also be improved to the same order O 
( T− 1 
3 
) if Assumption 5.2 holds in Section 4. However, in the case 
of Markovian data, the convergence can not be guaranteed if Assumption 5.2 is blocked. This is due to we require the convergence of ηt is faster than Qt to control the overall error. In addition, we stay positive on improving the convergence rate from O 
( T− 1 
3 
) to O 
( T− 1 
2 
) if Polyak-averaging 
technique [Polyak and Juditsky, 1992] is applied, which we leave for subsequent works. 
6 Experiments 
In this section, we verify our theory from the following aspects: (a) The connection between robust value function and non-robust value function, (b) The relationship between the statistical error and robustness parameter λ, (c) The convergence result of Algorithm 1, and (d) The convergence result of Algorithm 2. For (d), we need to make some minor changes to the setting and we provide the experimental details to Section 6.5. 
16
6.1 Experimental Details 
……s1 s2 s10 
p/1-p p/1-p 
1-p/p 1-p/p 
1 
a=1: ♦ a=2: ♦ 
Figure 1: MDP with 10 states 2 actions. The transition probabilities are marked with red for taking action a = 1, while the transition probabilities are marked blue taking action a = 2. 
We use a 10-state MDP environment (Figure 1) at first. At state si where 1 ≤ i ≤ 9, the transition probability is given by the following rules: When taking action 1, P ∗(si|si, 1) = p and P ∗(si+1|si, 1) = 1 − p; When taking action 2, the probability is opposite P ∗(si|si, 2) = 1 − p and P ∗(si+1|si, 2) = p). At state s10, the agent is always transited back to the same state. The reward is always 1 except that transitions at s10 always gives 0. The discount rate is γ = 0.9. 
To obtain the true value functions, we run value iteration algorithms to achieve them. For non-robust optimal value function V ∗, we run standard value iteration algorithm and set the iteration step being T = 10000. For robust optimal value function V ∗ 
rob,p, we run a robust value iteration algorithm (Algorithm 3) with the transition probability P ∗ and set T = 10000 (outer loop steps) and T ′ = 1000 (inner loop steps) to make sure the the dual variables and robust Q-values converging. 
In Section 6.2 and 6.3, we apply a model-based method to learn V̂rob,p and Q̂rob,p. First, we estimate P̂ with 1000 transitions collected with model P ∗ for each (s, a). Then, we run Algorithm 3 with P̂ to obtain V̂rob,p. We use T = T ′ = 100 and set ηt,0 = ηt−1,T ′ to save steps. In these sections, we test several settings with different choice of λ: {0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0}. Moreover, the learning rate in the inner loop is set to be a constant α′ 
t = λ by the fact the smoothness of the dual objective is 1/λ. 
Algorithm 3 Model-based approach to robust MDPs 
Input: Q0(s, a) = (1− γ)−1 for all (s, a) ∈ S ×A, and transition probability P . for iteration t = 0 to T − 1 do Vt = Π[0,(1−γ)−1] (maxaQt(·, a)); for each state-action pair (s, a) ∈ S ×A do 
Set ηt,0(s, a) = 0. for iteration t′ = 0 to T ′ − 1 do ηt,t′+1(s, a) = ΠΘ 
( ηt,t′(s, a) + αt′ 
∑ s′ P (s 
′|s, a)∂J(ηt,t′ (s,a),Vt;s′) 
∂η 
) ; 
end for Qt+1(s, a) = R(s, a) + γ 
∑ s′ P (s 
′|s, a)J(ηt,T ′(s, a), Vt; s ′); 
end for end for 
In Section 6.4, we run the model-free algorithm with a generative model (Algorithm 1) to learn Q̂rob,p. In this section, we set T = 1000, and ηt,0 is set to 0 at the beginning of each inner loop. Moreover, we sweep λ with the same values listing as above, and test different T ′ settings in 
17
[10, 50, 100]. The learning rate in the outer loop is 1 1+(1−γ)t and the inner loop has learning rate λ√ 
t′ , 
where t refers to the iteration at the outer loop and t′ is the iteration at the inner loop. We repeat each experiment 100 times using different random seeds to account for noise. 
6.2 Connection to Non-robust Value Functions 
0. 5 
1. 0 
2. 0 
3. 0 
4. 0 
5. 0 
10 .0 
0 
1 
2 
||V * ro 
b, p 
V * | 
| 
Figure 2: Deviation ∥V ∗ rob,p − V ∗∥∞ v.s. λ. 
In this section, we show how the robust value function V ∗ rob,p varies with different λ. In a 
high-level idea, by definition of (7), we observe that the robust value function is less dependent with P ∗ when λ approaches 0. Similarly, the robust value function would be approaching the non-robust value function since the infimum of (7) would be obtained at P = P ∗. We simply run Algorithm 3 (taking P = P ∗) and Value Iteration algorithms to obtain V ∗ 
rob,p and V ∗ respectively. In Figure 2, we find the error ∥V ∗ 
rob,p − V ∗∥∞ decays as λ increases, which suggests this idea is correct. 
6.3 Statistical Errors 
0 50 100 Iterations 
100 
101 
||V ro 
b, p, 
t V 
* ro b, 
p|| (lo 
g sc 
al e) 
Learning Curves = 0.5 = 1.0 = 2.0 = 3.0 = 4.0 = 5.0 = 10.0 
0. 5 
1. 0 
2. 0 
3. 0 
4. 0 
5. 0 
10 .0 
1.6 × 10 1 
2 × 10 1 
1.7 × 10 1 
1.8 × 10 1 
1.9 × 10 1 
||V ro 
b, p, 
t V 
* ro b, 
p|| (lo 
g sc 
al e) 
Final Performance 
||Vrob, p, T V * rob, p|| 
95% CI width 1 × 10 2 
2 × 10 2 
95 % 
 C I w 
id th 
 (l og 
 sc al 
e) 
Figure 3: Left: deviation ∥V̂rob,p,t−V ∗ rob,p∥∞ v.s. number of iterations. The shaded region represents 
the 95% CI. The subplot on the top right corner zooms in the performance before cutting off learning. Right: deviation ∥V̂rob,p,t − V ∗ 
rob,p∥∞ and 95% confidence interval v.s. λ. 
18
In this section, we investigate the relationship between the statistical error and λ. In Theorem 3.2, we prove both upper and lower bounds for penalized robust MDPs. It is worth noticing the upper bound is conservative. And the example (Figure 1) we use is an extension of lower bound in Theorem 3.2. Thus, we compare our experiment results with lower bounds. In Figure 3, the left learning curve composes of two stages: the curve drops at a linear rate in the first stage, and then becomes flat in the second stage. In fact, the first stage is due to T̂rob,p is a γ-contraction, and the second stage is due to statistical error between P̂ and P ∗. On the right side of Figure 3, we find the deviation ∥V̂rob,p,t − V ∗ 
rob,p∥∞ and confidence interval both increases as λ increases, which matches the lower bound in Theorem 3.2. Also, on the left side of Figure 3, it is notable that the convergence rate is also slightly related with the choice of λ. It is that the convergence rate would be fast at the first stage when λ is small. This phenomenon is due to the robust Bellman gap of different values V1 and V2 becomes: 
∥Trob,pV1 − Trob,pV2∥∞ ≈ γ |V1,min − V2,min| (16) 
when λ is small. On the contrary, if λ is large, the error is determined by: 
∥Trob,pV1 − Trob,pV2∥∞ ≈ γ ∥∥∥EP ∗ 
s,a (V1 − V2) 
∥∥∥ ∞ , (17) 
which is usually larger than the prior case. 
6.4 Convergence 
0 10 20 30 40 Iterations (1 × 102) 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) Different Robustness Parameters 
=0.5 =1.0 =2.0 =3.0 
=4.0 =5.0 =10.0 
Q-learning 
0. 5 
1. 0 
2. 0 
3. 0 
4. 0 
5. 0 
10 .0 
3 × 10 1 
1 × 100 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) Final Performance 
||Qrob, p, T Q * rob, p|| 
95% CI width 
0 10 20 30 40 Iterations (1 × 102) 
100 
5 × 100 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) Different Number of Inner Loop Steps 
T'=10 T'=50 
T'=100 
1.7 × 10 2 
3 × 10 2 
  9 5% 
 C I w 
id th 
 (l og 
) 
Figure 4: Deviation ∥Q̂rob,p,t − Q∗ rob,p∥∞ v.s. number of iterations. Left and Middle: T ′ = 100; 
Right: λ = 10. In the left and right subplots, the shaded region represents the 95% CI. 
In this section, we test the convergence performance of Algorithm 1. In Figure 4, we plot learning curves run by Algorithm 1. On the left side of Figure 4, we find when λ is smaller, the convergence rate is slightly faster. This phenomenon coincides with the 1st stage performance in Fig 3 (left and middle). However, the final performance is strange: the error decreases as λ increases. One reason is due to the optimization errors, where the error would amplify when λ is small by the 1/λ factor in dual variable updating. Except for the optimization errors, the other reason is that the bound of Theorem 4.2 is a worst case result, which is conservative when λ is small or large. Thus we couldn’t observe a matching performance with Theorem 4.2. Moreover, we observe the confidence interval of the final run is increasing as λ increases, which means robustness indeed works though there is a drop when λ = 10. In the rightmost subplot of Fig 4, we find the deviation ∥Q̂rob,p,T −Q∗ 
rob,p∥∞ also matters with the choice of T ′. With a small T ′, the solution of dual variable is not accurate, which leads to a bad performance on ∥Q̂rob,p,T −Q∗ 
rob,p∥∞. With T ′ increases, the performance becomes better, which supports the third term in (11). 
19
6.5 On a Markovian Chain Convergence 
In this section, we test the convergence performance of Algorithm 2. To make Algorithm 2 work, we make a slight change to the environment, where we allow the state s10 can transit to s1 with a positive probability. In this scenario, the stationary distribution satisfies mins,a dπ(s, a) > 0. And we also set the behavior policies as π(1|s) = π and π(2|s) = 1− π. The minimal probability of the stationary distribution changes w.r.t. π, which is shown in Figure 6. It is notable that the stationary distribution is approximately uniform when π ≈ 0.5 and there exists a state-action pair becomes inaccessible when π ≈ 0 or π ≈ 1. To learn the robust Q-value function Q̂rob,p, we set T = 4× 106 
to make sure the overall sample complexity is the same as experiments in Section 6.4. Moreover, the learning rate for Q-value update and dual variable update are all set to be the same in Theorem 5.1, where κ = 1/6(λ+ (1− γ)−1). Besides, we sweep the same λ ∈ {0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0} in the experiments. In the meantime, we also sweep behavior policy π ∈ {0.001, 0.005, 0.05, 0.1, 0.2, 0.5} for some chosen λ. In this setting, we run Algorithm 2 repetitively with 100 different random seeds. 
……s1 s2 s10 
p/1-p p/1-p 
1-p/p 1-p/p 
a=1: ♦ a=2: ♦ 
p/1-p 
1-p/p 
Figure 5: MDP with 10 states 2 actions. The transition probabilities are marked red taking action a = 1, while the transition probabilities are marked blue taking action a = 2. 
0. 1 
0. 2 
0. 3 
0. 4 
0. 5 
0. 6 
0. 7 
0. 8 
0. 9 
0.01 
0.03 
0.05 
d m in 
Figure 6: The minimal probability of the stationary distribution in Fig. 5 with changing of behavior policy π. 
In Figure 7, we show the performances with behavior policy π = 0.5. It is notable that the training performances are undesirable when λ = 0.5. We argue the main reason is due to the numerical problem in the learning rate for the smaller λ as we explained in Section 6.4. When λ is large, we are delight to find the convergence can be guaranteed. Compared with Section 6.4, we also find the final performance of Algorithm 2 is better in terms of sample complexity (error is better when number of samples are 106). In Figure 8, we also show the relationship between learning performances and behavior policy. It can be inferred that the performance would be better if the 
20
behavior policy approaches 0.5 or dmin is large, which is due to each (s, a) pair will be frequently and equally visited and also coincides with Theorem 5.1. If the behavior policy approaches 0, the training performances will drop as some specific (s, a) will be barely visited and the corresponding Q-values are inaccurate. 
0 100 200 300 400 Iterations (1 × 104) 
10 2 
10 1 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) Learning Curves 
=0.5 =1.0 =2.0 =3.0 
=4.0 =5.0 =10.0 
Q-learning 
0. 5 
1. 0 
2. 0 
3. 0 
4. 0 
5. 0 
10 .0 
10 2 
3 × 10 3 
4 × 10 3 
6 × 10 3 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) Final Performance 
||Qrob, p, T Q * rob, p|| 
95% CI width 
2 × 10 4 
2 × 10 3 
95 % 
 C I w 
id th 
 (l og 
) 
Figure 7: Deviation ∥Q̂rob,p,t −Q∗ rob,p∥∞ v.s. number of iterations (Algorithm 2, π = 0.5). In the 
left subplot, the shaded region represents the 95% CI. 
0 100 200 300 400 Iterations (×104) 
10 2 
10 1 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) 
=0.5 =0.2 =0.1 
=0.05 =0.005 =0.001 
0 100 200 300 400 Iterations (×104) 
10 2 
10 1 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) 
=0.5 =0.2 =0.1 
=0.05 =0.005 =0.001 
(a) λ = 1.0 (b) λ = 2.0 
0 100 200 300 400 Iterations (×104) 
10 2 
10 1 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) 
=0.5 =0.2 =0.1 
=0.05 =0.005 =0.001 
0 100 200 300 400 Iterations (×104) 
10 2 
10 1 
100 
101 
||Q ro 
b, p, 
t Q 
* ro b, 
p|| (lo 
g sc 
al e) 
=0.5 =0.2 =0.1 
=0.05 =0.005 =0.001 
(c) λ = 5.0 (d)λ = 10.0 
Figure 8: Deviation ∥Q̂rob,p,t −Q∗ rob,p∥∞ v.s. number of iterations (Algorithm 2). 
21
7 Concluding Remarks 
In this paper we have made two primary contributions towards solving robust MDPs efficiently. First, we have proposed an alternative formulation for distributionally robust MDPs and proved the statistical equivalence with the original forms. Second, we have devised a model-free algorithm to solve the robust MDPs without requiring an oracle to obtain solutions for DRO problems. We have also proved the polynomial convergence rate of our algorithm, in generative model setting and Markovian data setting. Here are some directions for further improvements. One direction is whether the convergence rate can be improved by some another technique such as Polyak-averaging Polyak and Juditsky [1992]. Furthermore, it would be challenging to move our theoretical results from a worst-case analysis to an instance-dependent analysis. Such instance-dependent results exist for MDPs [Khamaru et al., 2020, 2021, Li et al., 2020a, 2021, Yin and Wang, 2021], but it still remains open for robust MDPs. As the data generating mechanism is limited to generative model and Markovian in this paper, it is open whether the robust MDPs could be solved efficiently if the behavior policy is changing with current Q-values. Moreover, from an empirical perspective, it also would be interesting to deploy our algorithms to some large-scale realistic applications. 
Acknowledgements 
The authors thank Professor Martha White for valuable discussions with this project. 
References 
Mohammad Gheshlaghi Azar, Rémi Munos, and Hilbert J Kappen. Minimax pac bounds on the sample complexity of reinforcement learning with a generative model. Machine learning, 91(3): 325–349, 2013. 
Albert Benveniste, Michel Métivier, and Pierre Priouret. Adaptive algorithms and stochastic approximations, volume 22. Springer Science & Business Media, 2012. 
Stephen Boyd, Stephen P Boyd, and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004. 
Sébastien Bubeck et al. Convex optimization: Algorithms and complexity. Foundations and Trends® in Machine Learning, 8(3-4):231–357, 2015. 
Yichen Chen and Mengdi Wang. Stochastic primal-dual methods and sample complexity of reinforcement learning. arXiv preprint arXiv:1612.02516, 2016. 
Noel Cressie and Timothy RC Read. Multinomial goodness-of-fit tests. Journal of the Royal Statistical Society: Series B (Methodological), 46(3):440–464, 1984. 
Imre Csiszár. A class of measures of informativity of observation channels. Periodica Mathematica Hungarica, 2(1-4):191–213, 1972. 
Thinh T Doan. Finite-time convergence rates of nonlinear two-time-scale stochastic approximation under markovian noise. arXiv preprint arXiv:2104.01627, 2021a. 
22
Thinh T Doan. Nonlinear two-time-scale stochastic approximation: Convergence and finite-time performance. In Learning for Dynamics and Control, pages 47–47. PMLR, 2021b. 
Thinh T Doan, Lam M Nguyen, Nhan H Pham, and Justin Romberg. Finite-time analysis of stochastic gradient descent under markov randomness. arXiv preprint arXiv:2003.10973, 2020. 
John Duchi and Hongseok Namkoong. Variance-based regularization with convex objectives. arXiv preprint arXiv:1610.02581, 2016. 
John C. Duchi and Hongseok Namkoong. Learning models with uniform performance via distributionally robust optimization. The Annals of Statistics, 49(3):1378 – 1406, 2021. doi: 10.1214/20-AOS2004. URL https://doi.org/10.1214/20-AOS2004. 
Xavier Fontaine, Valentin De Bortoli, and Alain Durmus. Convergence rates and approximation results for sgd and its continuous-time counterpart. In Conference on Learning Theory, pages 1965–2058. PMLR, 2021. 
Vineet Goyal and Julien Grand-Clement. Robust markov decision process: Beyond rectangularity. arXiv preprint arXiv:1811.00215, 2018. 
Harsh Gupta, Rayadurgam Srikant, and Lei Ying. Finite-time performance bounds and adaptive learning rate selection for two time-scale reinforcement learning. Advances in Neural Information Processing Systems, 32, 2019. 
Chin Pang Ho, Marek Petrik, and Wolfram Wiesemann. Fast bellman updates for robust mdps. In International Conference on Machine Learning, pages 1979–1988. PMLR, 2018. 
Chin Pang Ho, Marek Petrik, and Wolfram Wiesemann. Partial policy iteration for l1-robust markov decision processes. arXiv preprint arXiv:2006.09484, 2020. 
Garud N Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2): 257–280, 2005. 
Jikai Jin, Bohang Zhang, Haiyang Wang, and Liwei Wang. Non-convex distributionally robust optimization: Non-asymptotic analysis. Advances in Neural Information Processing Systems, 34: 2771–2782, 2021. 
Maxim Kaledin, Eric Moulines, Alexey Naumov, Vladislav Tadic, and Hoi-To Wai. Finite time analysis of linear two-timescale stochastic approximation with markovian noise. In Conference on Learning Theory, pages 2144–2203. PMLR, 2020. 
Koulik Khamaru, Ashwin Pananjady, Feng Ruan, Martin J Wainwright, and Michael I Jordan. Is temporal difference learning optimal? an instance-dependent analysis. arXiv preprint arXiv:2003.07337, 2020. 
Koulik Khamaru, Eric Xia, Martin J Wainwright, and Michael I Jordan. Instance-optimality in optimal value estimation: Adaptivity via variance-reduced q-learning. arXiv preprint arXiv:2106.14352, 2021. 
Vijay R Konda and John N Tsitsiklis. Convergence rate of linear two-time-scale stochastic approximation. 2004. 
23
Gen Li, Yuting Wei, Yuejie Chi, Yuantao Gu, and Yuxin Chen. Breaking the sample size barrier in model-based reinforcement learning with a generative model. Advances in neural information processing systems, 33:12861–12872, 2020a. 
Gen Li, Yuting Wei, Yuejie Chi, Yuantao Gu, and Yuxin Chen. Sample complexity of asynchronous q-learning: Sharper analysis and variance reduction. Advances in neural information processing systems, 33:7031–7043, 2020b. 
Xiang Li, Wenhao Yang, Zhihua Zhang, and Michael I Jordan. Polyak-ruppert averaged q-leaning is statistically efficient. arXiv preprint arXiv:2112.14582, 2021. 
Xiang Li, Jiadong Liang, and Zhihua Zhang. Online statistical inference for nonlinear stochastic approximation with markovian data. arXiv preprint arXiv:2302.07690, 2023. 
Shiau Hong Lim, Huan Xu, and Shie Mannor. Reinforcement learning in robust markov decision processes. Advances in Neural Information Processing Systems, 26:701–709, 2013. 
Zijian Liu, Qinxun Bai, Jose Blanchet, Perry Dong, Wei Xu, Zhengqing Zhou, and Zhengyuan Zhou. Distributionally robust q-learning. In International Conference on Machine Learning, pages 13623–13643. PMLR, 2022. 
Shie Mannor, Duncan Simester, Peng Sun, and John N Tsitsiklis. Bias and variance in value function estimation. In Proceedings of the twenty-first international conference on Machine learning, page 72, 2004. 
M. Métivier and P. Priouret. Théorèmes de convergence presque sure pour une classe d’algorithmes stochastiques à pas decroissant. Probab. Theory Relat. Fields, 74:403–428, 1987. ISSN 0178-8051. doi: 10.1007/BF00699098. 
Abdelkader Mokkadem and Mariane Pelletier. Convergence rate and averaging of nonlinear two-time-scale stochastic approximation algorithms. 2006. 
Hongseok Namkoong and John C Duchi. Stochastic gradient methods for distributionally robust optimization with f-divergences. Advances in neural information processing systems, 29, 2016. 
Arnab Nilim and Laurent El Ghaoui. Robust control of markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798, 2005. 
Kishan Panaganti and Dileep Kalathil. Sample complexity of robust reinforcement learning with a generative model. In International Conference on Artificial Intelligence and Statistics, pages 9582–9602. PMLR, 2022. 
Boris T Polyak and Anatoli B Juditsky. Acceleration of stochastic approximation by averaging. SIAM journal on control and optimization, 30(4):838–855, 1992. 
Qi Qi, Zhishuai Guo, Yi Xu, Rong Jin, and Tianbao Yang. An online method for a class of distributionally robust optimization with non-convex objectives. Advances in Neural Information Processing Systems, 34:10067–10080, 2021. 
Jay K Satia and Roy E Lave Jr. Markovian decision processes with uncertain transition probabilities. Operations Research, 21(3):728–740, 1973. 
24
Ohad Shamir and Tong Zhang. Stochastic gradient descent for non-smooth optimization: Convergence results and optimal averaging schemes. In International conference on machine learning, pages 71–79. PMLR, 2013. 
Alexander Shapiro. Distributionally robust stochastic programming. SIAM Journal on Optimization, 27(4):2258–2275, 2017. 
Laixi Shi and Yuejie Chi. Distributionally robust model-based offline reinforcement learning with near-optimal sample complexity. arXiv preprint arXiv:2208.05767, 2022. 
Nian Si, Fan Zhang, Zhengyuan Zhou, and Jose Blanchet. Distributionally robust policy evaluation and learning in offline contextual bandits. In International Conference on Machine Learning, pages 8884–8894. PMLR, 2020. 
Aman Sinha, Hongseok Namkoong, Riccardo Volpi, and John Duchi. Certifying some distributional robustness with principled adversarial training. arXiv preprint arXiv:1710.10571, 2017. 
Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction. MIT press, 2018. 
Martin J Wainwright. High-dimensional statistics: A non-asymptotic viewpoint, volume 48. Cam-bridge University Press, 2019a. 
Martin J Wainwright. Stochastic approximation with cone-contractive operators: Sharp ℓ∞-bounds for q-learning. arXiv preprint arXiv:1905.06265, 2019b. 
Shengbo Wang, Nian Si, Jose Blanchet, and Zhengyuan Zhou. A finite sample complexity bound for distributionally robust q-learning. In Francisco Ruiz, Jennifer Dy, and Jan-Willem van de Meent, editors, Proceedings of The 26th International Conference on Artificial Intelligence and Statistics, volume 206 of Proceedings of Machine Learning Research, pages 3370–3398. PMLR, 25–27 Apr 2023. URL https://proceedings.mlr.press/v206/wang23b.html. 
Wolfram Wiesemann, Daniel Kuhn, and Bercc Rustem. Robust markov decision processes. Mathe-matics of Operations Research, 38(1):153–183, 2013. 
Huan Xu and Shie Mannor. The robustness-performance tradeoff in markov decision processes. Advances in Neural Information Processing Systems, 19:1537–1544, 2006. 
Wenhao Yang, Liangyu Zhang, and Zhihua Zhang. Toward theoretical understandings of robust Markov decision processes: Sample complexity and asymptotics. The Annals of Statistics, 50(6): 3223 – 3248, 2022. doi: 10.1214/22-AOS2225. URL https://doi.org/10.1214/22-AOS2225. 
Ming Yin and Yu-Xiang Wang. Towards instance-optimal offline reinforcement learning with pessimism. Advances in neural information processing systems, 34:4065–4078, 2021. 
Sihan Zeng, Thinh T Doan, and Justin Romberg. A two-time-scale stochastic optimization framework with applications in control and reinforcement learning. arXiv preprint arXiv:2109.14756, 2021. 
Xingyu Zhou. On the fenchel duality between strong convexity and lipschitz continuous gradient. arXiv preprint arXiv:1803.06573, 2018. 
Zhengqing Zhou, Qinxun Bai, Zhengyuan Zhou, Linhai Qiu, Jose Blanchet, and Peter Glynn. Finite-sample regret bound for distributionally robust offline tabular reinforcement learning. In International Conference on Artificial Intelligence and Statistics, pages 3331–3339. PMLR, 2021. 
25
Appendix 
A Proofs of Section 3 
Proof of Proposition 3.1. For any two V1, V2 ∈ V, we have: 
Trob,pV1(s)− Trob,pV2(s) ≤ γ sup P∈∆(S) 
Es′∼P |V1(s′)− V2(s ′)| ≤ γ∥V1 − V2∥∞. 
Thus, Trob,p is a γ-contraction on V. Next, we prove the fixed point V ∗ rob,p = maxπ V 
π rob,p. Firstly, 
for any fixed policy π, we define an operator: 
T π rob,pV (s) := 
∑ a∈A 
π(a|s)R(s, a) + γ ∑ a∈A 
π(a|s) inf Pa∈∆(S) 
( Es′∼PaV (s′) + λDf (Pa∥P ∗(·|s, a)) 
) , 
where it is also a γ-contraction on V, and we denote the fixed point of T π rob,p by V ∗ 
π and Rπ(s) :=∑ a∈A π(a|s)R(s, a). By definition of V π 
rob,p, we have: 
V π rob,p ≥ T π 
rob,pV π rob,p ≥ (T π 
rob,p) 2V π 
rob,p ≥ · · · ≥ (T π rob,p) 
∞V π rob,p = V ∗ 
π . 
On the contrary, denote P ∗ π as the solution to T π 
rob,pV ∗ π = V ∗ 
π and P ∗ sa,π := P ∗ 
π (·|s, a), we have: 
V ∗ π (s) = Rπ(s) + γ 
∑ a∈A 
π(a|s) ( Es′∼P ∗ 
sa,π V ∗ π (s 
′) + λDf (P ∗ sa,π∥P ∗(·|s, a)) 
) = Eπ,P ∗ 
π 
[ ∞∑ t=0 
γt(R(st, at) + λγDf (P ∗ π (·|st, at)∥P ∗(·|st, at))) 
∣∣∣∣∣s0 = s 
] ≥ V π 
rob,p(s). 
Thus, the fixed point V ∗ π = V π 
rob,p for any fixed policy π. Similarly, by definition of Trob,p, for any policy π, we also have: 
V ∗ rob,p ≥ T π 
rob,pV ∗ rob,p ≥ (T π 
rob,p) 2V ∗ 
rob,p ≥ · · · ≥ (T π rob,p) 
∞V ∗ rob,p = V π 
rob,p. 
Taking maximum over π on the RHS, we have V ∗ rob,p ≥ maxπ V 
π rob,p. Furthermore, denote π∗ as the 
solution to T ∗ rob,pV 
∗ rob,p = V ∗ 
rob,p, note that V ∗ rob,p is also the fixed point of the operator T π∗ 
rob,p, which means V ∗ 
rob,p = V π∗ rob,p ≤ maxπ V 
π rob,p. Thus, we conclude that V ∗ 
rob,p = maxπ V π rob,p. 
Proof of Theorem 3.1. Without loss of generality, we assume P ∗(s′|s, a) > 0 for any (s, a, s′) ∈ S ×A× S. For notation simplicity, we denote Vλ := V ∗ 
rob,p and Qλ := Q∗ rob,p, and Vρ := V ∗ 
rob,c and Qρ := Q∗ 
rob,c. Firstly, for the penalized value function, by the fact P ≪ P ∗, we observe: 
sup π,P≪P ∗ 
EP,π 
[ ∞∑ t=0 
γtDf (P (·|st, at)∥P ∗(·|st, at)) 
∣∣∣∣∣ s0 = s 
] < +∞. (18) 
Thus, Vλ(s) is continuous and non-decreasing w.r.t. λ for any s ∈ S. Similarly, Qλ(s, a) is also continuous and non-decreasing w.r.t. λ for any (s, a) ∈ S ×A. By the facts that Vλ(s) ≤ V ∗ 
P ∗(s) and Qλ(s, a) ≤ QP ∗(s, a), we know limλ→+∞ Vλ := V∞ and limλ→+∞Qλ := Q∞ exist. Next, we study the range of Vλ(·). 
26
Case: λ = 0. In this case, we find Vλ satisfies the following equation: 
Vλ(s) = max a∈A 
( R(s, a) + γ inf 
s′ Vλ(s 
′) 
) . (19) 
Case: λ→ +∞. By Bellman equation, for any (s, a) ∈ S ×A, we have: 
Qλ(s, a) = R(s, a) + γ inf P≪P ∗ 
s,a 
P⊤Vλ + λDf (P∥P ∗ s,a) 
= R(s, a) + γP⊤ λ Vλ + λDf (Pλ∥P ∗ 
s,a). (20) 
As limλ→+∞Qλ exists, we have limλ→+∞ Qλ λ = 0. By the fact P⊤ 
λ Vλ is bounded, we have limλ→+∞Df (Pλ∥P ∗ 
s,a) = 0. Then by Theorem 3.1 in Csiszár [1972], we have limλ→+∞ ∥Pλ−P ∗ s,a∥1 = 
0. Thus, we have: 
Q∞(s, a) = R(s, a) + γP ∗,⊤ s,a V∞ + lim 
λ→+∞ λDf (Pλ∥P ∗ 
s,a) 
:= R(s, a) + γP ∗,⊤ s,a V∞ + c(s, a), (21) 
where c(s, a) ≥ 0. Then, by definition of value function, we have V ∗ P ∗ ≤ V∞. Thus, V∞ = V ∗ 
P ∗ . Hence, for a given initial distribution µ, Vλ(µ) is continuous and non-decreasing w.r.t. λ and 
Vλ(µ) ∈ [V0(µ), V ∗ P ∗(µ)). Then, we study the constrained value function. It is easy to obtain Vρ is 
non-increasing w.r.t. ρ. For any ρ < ρ′, we have: 
Vρ(s)− Vρ′(s) ≤ γmax a∈A 
( inf 
Df (P∥P ∗ s,a)≤ρ 
P⊤Vρ − inf Df (P∥P ∗ 
s,a)≤ρ′ P⊤Vρ′ 
) 
≤ γmax a 
( inf 
Df (P∥P ∗ s,a)≤ρ 
P⊤Vρ − inf Df (P∥P ∗ 
s,a)≤ρ′ P⊤Vρ 
) + γ∥Vρ − Vρ′∥∞. (22) 
Thus, for any ρ ̸= ρ′, we have: 
∥Vρ − Vρ′∥∞ ≤ γ 
1− γ max a 
∣∣∣∣∣ inf Df (P∥P ∗ 
s,a)≤ρ P⊤Vρ − inf 
Df (P∥P ∗ s,a)≤ρ′ 
P⊤Vρ 
∣∣∣∣∣ . (23) 
From problem (2), we observe it is convex w.r.t. ρ. Thus, problem (2) is continuous w.r.t. ρ. Combing with above inequality (23), we obtain Vρ is continuous w.r.t. ρ. Next we study the range of Vρ. 
Case: ρ = 0. In this case, we find Vρ = V ∗ P ∗ . 
Case: ρ→ ∞. As P ≪ P ∗, we have: 
sup (s,a)∈S×A,P≪P ∗ 
Df (P∥P ∗ s,a) < +∞, (24) 
and we denote ρ∗(s, a) := supP≪P ∗ s,a Df (P∥P ∗ 
s,a). By Bellman equation, for any s ∈ S, we have: 
Vρ(s) = max a∈A 
( R(s, a) + γ inf 
Df (P∥P ∗ s,a)≤ρ∗(s,a) 
P⊤Vρ 
) = max 
a∈A 
( R(s, a) + γ inf 
s′∈S Vρ(s 
′) 
) , (25) 
27
which coincides with case λ = 0 in penalized value function. Thus, for a given initial distribution µ, Vρ(µ) is non-increasing w.r.t. ρ and Vρ(µ) ∈ [V0(µ), 
V ∗ P ∗(µ)]. Finally, our result is obtained by intermediate value theorem. 
Lemma A.1. Let P be a probability measure on (S,F), V ∈ [0, 1 1−γ ], and f(s) = (s − 1)2, the 
optimal dual variable η∗ lies in Θ = [−λ, 2 1−γ + 2λ]. 
Proof of Lemma A.1. By definition of f∗(·), we have f∗(s) = (s/2 + 1)2+ − 1 when f(s) = (s− 1)2. Thus, the dual problem can be written by: 
R(P, V ) = sup η∈R 
−λEs∼P 
( η − V (s) 
2λ + 1 
)2 
+ 
+ λ+ η 
= sup η̃∈R 
− 1 
4λ Es∼P (η̃ − V (s))2+ − λ+ η̃. 
The last equality holds by replacing η with η̃− 2λ. We denote g(η̃) = − 1 4λEs∼P (η̃ − V (s))2+ − λ+ η̃, 
which is concave in η̃. For η̃ ≤ 0, we have g(η̃) = −λ+ η̃. For η̃ ≥ 2 1−γ + 4λ, we have: 
g(η̃) (a) = − 1 
4λ Es∼P (η̃ − V (s))2 − λ+ η̃ 
= − η̃ 2 − 2(Es∼PV (s) + 2λ)η̃ + Es∼PV (s)2 + 4λ2 
4λ (b) 
≤ − η̃2 − 2( 1 
1−γ + 2λ)η̃ + 4λ2 
4λ ≤ −λ, 
where (a) holds by η̃ ≥ maxs V (s) here and (b) holds by V ∈ [0, 1 1−γ ]. By g(η̃) being concave, 
the optimal solution η̃∗ ∈ argmax g(η̃) lies in [0, 2 1−γ + 4λ]. Moreover, we notice supη̃∈R g(η̃) ≥ 0 
by the primal objective. Thus, −λ + η̃∗ ≥ 0. Thus, η̃∗ ∈ [λ, 2 1−γ + 4λ], which concludes η∗ ∈ 
[−λ, 2 1−γ + 2λ]. 
Proof of Theorem 3.2. We prove upper bound at first. We note that:∥∥∥V̂ ∗ rob,p − V ∗ 
rob,p 
∥∥∥ ∞ 
= ∥∥∥T̂rob,pV̂ 
∗ rob,p − Trob,pV 
∗ rob,p 
∥∥∥ ∞ 
≤ ∥∥∥T̂rob,pV̂ 
∗ rob,p − T̂rob,pV 
∗ rob,p 
∥∥∥ ∞ 
+ ∥∥∥T̂rob,pV 
∗ rob,p − Trob,pV 
∗ rob,p 
∥∥∥ ∞ 
≤ γ ∥∥∥V̂ ∗ 
rob,p − V ∗ rob,p 
∥∥∥ ∞ 
+ ∥∥∥T̂rob,pV 
∗ rob,p − Trob,pV 
∗ rob,p 
∥∥∥ ∞ . 
Arranging terms, we have:∥∥∥V̂ ∗ rob,p − V ∗ 
rob,p 
∥∥∥ ∞ 
≤ 1 
1− γ 
∥∥∥T̂rob,pV ∗ rob,p − Trob,pV 
∗ rob,p 
∥∥∥ ∞ 
≤ γ 
1− γ max s,a 
∣∣∣∣ inf Q∈∆(S) 
Es′∼QV ∗ rob,p(s 
′) + λDf (Q∥P̂s,a)− inf Q∈∆(S) 
Es′∼QV ∗ rob,p(s 
′) + λDf (Q∥P ∗ s,a) 
∣∣∣∣ , 
28
where the last inequality holds by definition of Trob,p and T̂rob,p. By Eqn. (4) and applying f(s) = (s− 1)2, we also have: 
inf Q∈∆(S) 
Es′∼QV ∗ rob,p(s 
′) + λDf (Q∥P ∗ s,a) = sup 
η∈Θ − 1 
4λ Es∼P ∗ 
s,a (η − V ∗ 
rob,p(s)) 2 + − λ+ η. 
Moreover, we denote g(η, P ) = − 1 4λEs∼P (η − V ∗ 
rob,p(s)) 2 + − λ+ η, where we omit (s, a) dependence 
for simplification. Next, we study the deviation |g(η, P )− g(η, P̂ )|, where P̂ (s) = 1 n 
∑n k=1 1(Xk = s) 
and Xk ∼ P (·) are i.i.d. random variables. Denote Yk := − 1 4λ 
∑ s∈S 1(Xk = s)(η − V ∗ 
rob,p(s)) 2 +, we 
have |g(η, P ) − g(η, P̂ )| = | 1n ∑n 
k=1 Yk − EY1|. By Lemma A.1, when η ∈ Θ, we have 0 ≤ −Yk ≤ ( 2 1−γ 
+4λ)2 
4λ ≤ 16max { 
1 λ(1−γ)2 
, λ } 
. By Hoeffding’s inequality, we have: 
P 
|g(η, P )− g(η, P̂ )| ≥ 16max 
{ 1 
λ(1− γ)2 , λ 
}√ ln 2 
δ 
2n 
 ≤ δ. 
With η ∈ Θ, we can prove that 1 4λ 
∑ s∈S P (Xk = s)(η − V ∗ 
rob,p(s)) 2 + is 8max 
{ 1 
λ2(1−γ)2 , 1 } 
-Lipschitz w.r.t. η. Then we take the ε-net of Θ as Nε w.r.t. metric | · |, whose size is bounded by: 
|Nε| ≤ 1 + 
2 1−γ + 4λ 
ε ≤ 1 + 
8max{ 1 1−γ , λ} ε 
. 
Then we have: 
sup η∈Θ 
|g(η, P̂ )− g(η, P )| ≤ 16max 
{ 1 
λ2(1− γ)2 , 1 
} ε+ sup 
η∈Nε 
|g(η, P̂ )− g(η, P )|. 
Taking ε = λ√ 2n 
, we have: 
P 
sup η∈Θ 
|g(η, P̂ )− g(η, P )| ≥ 16max 
{ 1 
λ(1− γ)2 , λ 
} (1 +√ln 2|Nε| δ 
) √ 2n 
 ≤P 
 sup η∈Nε 
|g(η, P̂ )− g(η, P )| ≥ 16max 
{ 1 
λ(1− γ)2 , λ 
}√ ln 2|Nε| 
δ 
2n 
 ≤ δ. 
Finally, with probability 1− δ, we have: 
∥∥∥V̂ ∗ rob,p − V ∗ 
rob,p 
∥∥∥ ∞ 
≤ 16γ 
1− γ max 
{ 1 
λ(1− γ)2 , λ 
}√ ln 2|S||A||Nε| 
δ 
2n 
≤ 16γ 
1− γ max 
{ 1 
λ(1− γ)2 , λ 
}√√√√ ln ( 2|S||A| 
δ (1 + 8max{ 1 λ(1−γ) , 1} 
√ 2n) ) 
2n 
= Õ ( 
1 
(1− γ) √ 2n 
max 
{ 1 
λ(1− γ)2 , λ 
}) . 
29
Next, we turn to calculate the lower bound. We consider a 2-state and 1-action MDP, where the states are denoted by s0 and s1. The reward is designed by r(s0) = 1 and r(s1) = 0. The transition probability is P (s0|s0) = p, P (s1|s0) = 1− p, and P (s1|s1) = 1. By robust Bellman equation, we have: 
V (s0) = 1 + γ inf 0≤q≤1 
qV (s0) + λDf (q∥p), 
where Df (q∥p) = pf( qp) + (1− p)f( 1−q 1−p). And V (s1) = 0. Setting f(s) = (s− 1)2, we have: 
V (s0) = 1 + λγ 
p(1− p) inf 
0≤q≤1 
[ q − 
( p− V (s0)p(1− p) 
2λ 
)]2 + γV (s0) 
2 
( 2p− V (s0)p(1− p) 
2λ 
) . 
Case 1: p− V (s0)p(1−p) 2λ < 0. In this case, the optimal q∗ = 0, and we have: 
V (s0) = 1 + λγ 
p(1− p) 
( p− V (s0)p(1− p) 
2λ 
)2 
+ γV (s0) 
2 
( 2p− V (s0)p(1− p) 
2λ 
) = 1 + 
λγp 
1− p . 
Denote f(p) = 1+ λγp 1−p , it is easy to verify that f(p) is monotonically increasing and convex on (0, 1). 
Thus, we have: 
f(p+ δ)− f(p) ≥ f ′(p)δ = λγδ 
(1− p)2 . 
Thus, by choosing δ = 2ε(1−p)2 
λγ and Lemma 16 in Azar et al. [2013], with a constant probability, to distinguish model p and p+ δ, the number of samples we need at least is: 
Ω 
( λ2p 
ε2(1− p)3 
) . 
Finally, by choosing p = 2− 1 γ for γ > 3/4, the lower bound for this 2-state MDP is: 
Ω 
( λ2 
ε2(1− γ)3 
) , 
where λ < 1−γ γ(3−2γ) . 
Case 2: p− V (s0)p(1−p) 2λ ≥ 0. In this case, the optimal q∗ = p− V (s0)p(1−p) 
2λ , and we have: 
V (s0) = 1 + γV (s0) 
2 
( 2p− V (s0)p(1− p) 
2λ 
) . 
By calculation, we have: 
V (s0) = −2λ(1− γp) + 2 
√ λ2(1− γp)2 + λγp(1− p) 
γp(1− p) 
30
= 2 
(1− γp) + 
√ (1− γp)2 + γp(1−p) 
λ 
:= 2 
g(p) . 
Thus, to satisfy the condition p− V (s0)p(1−p) 2λ ≥ 0, we need to restrict the range of λ to λ ≥ 1−p 
2−γp . Then we wish to distinguish two value functions at s0 under different transition probabilities p+ δ and δ. We denote them by Vp and Vp+δ respectively and we have the following fact about g(p): 
Fact: g(p) is concave and monotonically decreasing in p ∈ (1/2, 1). The first order derivative of g(p) is: 
g′(p) = −γ + −2γ(1− γp) + γ(1−2p) 
λ 
2 
√ (1− γp)2 + γp(1−p) 
λ 
, 
where we find g′(p) ≤ 0 for p ∈ (1/2, 1) and conclude that g(p) is monotonically decreasing in p. Furthermore, the second order derivative of g(p) is: 
g′′(p) = 4γ(γ − 1 
λ) ( (1− γp)2 + γp(1−p) 
λ 
) − ( −2γ(1− γp) + γ(1−2p) 
λ 
)2 4 ( (1− γp)2 + γp(1−p) 
λ 
) 3 2 
= 
4γ(γ−1) λ − γ2 
λ2 
4 ( (1− γp)2 + γp(1−p) 
λ 
) 3 2 
, 
from which we also find g′′(p) ≤ 0 and conclude that g(p) is concave in p. Thus, the deviation Vp+δ − Vp satisfies: 
Vp+δ − Vp = 2 
g(p+ δ) − 2 
g(p) 
= 2(g(p)− g(p+ δ)) 
g(p+ δ)g(p) 
(a) 
≥ −2g′(p)δ 
g(p+ δ)g(p) 
(b) 
≥ −2g′(p)δ 
g(p)2 , 
where we apply the fact g(p) is concave in p to (a) and the fact g(p) is monotonically decreasing in p to (b). By choosing δ = εg(p)2 
−g′(p) and Lemma 16 in Azar et al. [2013], with a constant probability, to distinguish model p and p+ δ, the number of samples we need at least is: 
Ω̃ 
( g′(p)2p(1− p) 
ε2g(p)4 
) . 
31
Then by choosing p = 2− 1/γ and γ ∈ (3/4, 1), we have: 
g(2− 1 
γ ) = 2(1− γ) + 
√ 4(1− γ)2 + 
(1− γ)(2γ − 1) 
λγ 
≤ 4(1− γ) + 
√ (1− γ)(2γ − 1) 
λγ 
≤ 2(1− γ)max 
{ 4, 
√ (2γ − 1) 
λγ(1− γ) 
} , 
∣∣∣∣g′(2− 1 
γ ) 
∣∣∣∣ = γ + 4γ + 3γ−2 
λγ(1−γ) 
2 √ 
4 + 2γ−1 λγ(1−γ) 
≥ γ + 3γ − 2 
2(2γ − 1) 
√ 4 + 
2γ − 1 
λγ(1− γ) 
≥ 3 
4 + 
1 
4 
√ 4 + 
2γ − 1 
λγ(1− γ) 
≥ max 
{ 3 
4 , 1 
4 
√ 2γ − 1 
λγ(1− γ) 
} 
≥ 3 
16 max 
{ 4, 
√ (2γ − 1) 
λγ(1− γ) 
} . 
Thus, the number of samples we need at least is: 
Ω̃ 
( 1 
ε2(1− γ)3 min 
{ 1 
16 , λγ(1− γ) 
2γ − 1 
}) , 
where λ ≥ 1−γ γ(3−2γ) . Finally, for an MDP with |S| states, |A| actions, we can aggregate the 2-states-1-
action MDPs together like Lemma 17 does in Azar et al. [2013]. 
B Proofs of Section 4.1 
Proof of Lemma 4.1. By Assumption 4.1 and first-order condition, we have: 
EP∇f∗ ( η∗ −R(X) 
λ 
) = 1. 
By Assumption 4.2, for any η ∈ Θ and 0 ≤ R(Xi) ≤M , we have:∣∣∣∣∂J(η;Xi) 
∂η 
∣∣∣∣ = ∣∣∣∣∇f∗(η −R(Xi) 
λ 
) − 1 
∣∣∣∣ = 
∣∣∣∣∇f∗(η −R(Xi) 
λ 
) − EP∇f∗ 
( η∗ −R(X) 
λ 
)∣∣∣∣ 32
≤ EP 
∣∣∣∣∇f∗(η −R(Xi) 
λ 
) −∇f∗ 
( η∗ −R(X) 
λ 
)∣∣∣∣ ≤ 1 
λσ (|η − η∗|+ E|R(Xi)−R(X)|) 
≤ diam(Θ) +M 
λσ . 
Lemma B.1. For any η, the following inequality holds: 
αt (J(η)− J(ηt)) ≤ (ηt − η)2 
2 − (ηt+1 − η)2 
2 + α2 tC 
2 g 
2 + αt(ηt − η) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) . 
Proof. By ηt+1 = ΠΘ 
( ηt + αt 
∂J(ηt;Xt) ∂η 
) , we have 
1 
2 (ηt+1 − η)2 − 1 
2 (ηt − η)2 
(a) 
≤ 1 
2 
( ηt − η + αt 
∂J(ηt;Xt) 
∂η 
)2 
− 1 
2 (ηt − η)2 
= α2 t 
2 
∣∣∣∣∂J(ηt;Xt) 
∂η 
∣∣∣∣2 + αt(ηt − η) ∂J(ηt;Xt) 
∂η 
(b) 
≤ α2 tC 
2 g 
2 + αt(ηt − η) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) + αt(ηt − η) 
∂J(ηt) 
∂η 
(c) 
≤ α2 tC 
2 g 
2 + αt(ηt − η) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) + αt(J(ηt)− J(η)), 
where (a) holds by the projection property, (b) holds by Lemma 4.1, and (c) holds by concavity of J(η). 
Lemma B.2. If αt is non-decreasing, then we have: 
αT (J(η∗)− J(ηT )) ≤ 1 
T 
T∑ t=1 
αt (J(η ∗)− J(ηt)) + 
T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) . 
Proof. This proof technique was firstly derived in Shamir and Zhang [2013]. Here we give a proof for a completeness consideration. We denote Sk = 1 
k+1 
∑T t=T−k αt (J(η 
∗)− J(ηt)), which satisfies: 
(k + 1)Sk = T∑ 
t=T−k 
αt (J(η ∗)− J(ηT−k)) + 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) 
(a) 
≤ (k + 1)αT−k (J(η ∗)− J(ηT−k)) + 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) , 
where (a) holds by αt is non-decreasing. Then by definition of Sk, we have: 
kSk−1 = (k + 1)Sk − αT−k (J(η ∗)− J(ηT−k)) 
33
≤ kSk + 1 
k + 1 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) . 
Summing k from k = 1, ..., T − 1, we have the final result: 
S0 ≤ ST−1 + T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) . 
Proof of Theorem 4.1. Firstly, we omit the (s, a) dependence. From Lemma B.2, it is clear that we need upper bounds for the following two terms: 
∆1 = 1 
T 
T∑ t=1 
αt(J(η ∗)− J(ηt)), 
∆2 = T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
αt (J(ηT−k)− J(ηt)) . 
For ∆1, applying Lemma B.1, we have: 
∆1 ≤ 1 
2T (η1 − η∗)2 + 
C2 g 
2T 
T∑ t=1 
α2 t + 
1 
T 
T∑ t=1 
αt(ηt − η∗) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) (a) 
≤ diam(Θ)2 
2T + 
diam(Θ)2(1 + lnT ) 
2T + 
1 
T 
T∑ t=1 
αt(ηt − η∗) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) , (26) 
where (a) holds by αt = diam(Θ) 
Cg 
√ t 
. For ∆2, by Lemma B.1, we have: 
∆2 ≤ T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
C2 gα 
2 t 
2 + αt(ηt − ηT−k) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) . 
Letting αt = diam(Θ) 
Cg 
√ t 
, we notice 
T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
C2 gα 
2 t 
2 = 
diam(Θ)2 
2 
T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
1 
t 
= diam(Θ)2 
2T 
T−1∑ k=1 
1 
k(k + 1) + 
diam(Θ)2 
2 
T−1∑ k=1 
1 
k(k + 1) 
T−1∑ t=T−k 
1 
t 
≤ diam(Θ)2 
2T + 
diam(Θ)2 
2 
T−1∑ k=1 
T−1∑ t=T−k 
1 
tk(k + 1) 
(a) = 
diam(Θ)2 
2T + 
diam(Θ)2 
2 
T−1∑ k=1 
k∑ t=1 
1 
(T − t)k(k + 1) 
34
(b) = 
diam(Θ)2 
2T + 
diam(Θ)2 
2 
T−1∑ t=1 
T−1∑ k=t 
1 
(T − t)k(k + 1) 
= diam(Θ)2 
2T + 
diam(Θ)2 
2 
T−1∑ t=1 
1 
tT 
≤ diam(Θ)2(2 + lnT ) 
2T , 
where (a) holds by variable substitution of t, (b) holds by interchanging the order of summation. Thus, we have: 
∆2 ≤ diam(Θ)2(2 + lnT ) 
2T + 
T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
αt(ηt − ηT−k) 
( ∂J(ηt;Xt) 
∂η − ∂J(ηt) 
∂η 
) . 
Combining the upper bounds of ∆1 and ∆2, and denote Zt = ∂J(ηt;Xt) 
∂η − ∂J(ηt) ∂η , we have: 
αT (J(η ∗)− J(ηT )) ≤ ∆1 +∆2 
≤ diam(Θ)2(2 + lnT ) 
T + 
1 
T 
T∑ t=1 
αt(ηt − η∗)Zt + T−1∑ k=1 
1 
k(k + 1) 
T∑ t=T−k 
αt(ηt − ηT−k)Zt 
= diam(Θ)2(2 + lnT ) 
T + 
1 
T 
T∑ t=1 
αt(ηt − η∗)Zt + T∑ t=2 
Zt 
( T−1∑ 
k=T−t+1 
αt(ηt − ηT−k) 
k(k + 1) 
) . 
It is worth noticing that, for any λ ∈ R, E[Zt|Ft−1] = 0 and E[exp(λZt)|Ft−1] ≤ exp ( λ2C2 
g 
2 
) . As 
η ∈ Θ, for any λ ∈ R, we have: 
E 
[ exp 
( λ 
T 
T∑ t=1 
αt(ηt − η∗)Zt 
)] ≤ exp 
( 2λ2diam(Θ)2C2 
g 
∑T t=1 α 
2 t 
T 2 
) 
≤ exp 
( 2λ2diam(Θ)4(1 + lnT ) 
T 2 
) . 
Furthermore, we notice that:( T−1∑ 
k=T−t+1 
αt(ηt − ηT−k) 
k(k + 1) 
)2 
≤ α2 tdiam(Θ)2 
( T−1∑ 
k=T−t+1 
1 
k(k + 1) 
)2 
= α2 tdiam(Θ)2(t− 1) 
T (T − t+ 1) . 
Then, for any λ ∈ R, it implies: 
E 
[ exp 
( λ 
T∑ t=2 
Zt 
( T−1∑ 
k=T−t+1 
αt(ηt − ηT−k) 
k(k + 1) 
))] ≤ exp 
( 2λ2 
T∑ t=2 
α2 tdiam(Θ)2C2 
g (t− 1) 
T (T − t+ 1) 
) 
≤ exp 
( 2λ2diam(Θ)4(1 + lnT ) 
T 
) . 
35
Now we take (s, a)-dependence into consideration. By Lemma E.1, we have: 
E [ 
max (s,a)∈S×A 
( sup η J (s,a)(η)− J (s,a)(ηT (s, a)) 
)] ≤ diam(Θ)Cg(2 + lnT )√ 
T + 
4 √ 2diam(Θ)Cg 
√ (1 + lnT ) ln |S||A|√ T 
≤ diam(Θ)Cg(2 + lnT )(4 
√ 2 ln |S||A|+ 1)√ 
T . 
C Proofs of Section 4.2 
Lemma C.1. For Nt and w ∈ R, when (1− βt)βt−1 ≤ βt, we have: 
E exp(wNt+1(s, a)) ≤ exp 
( w2βt(1 + γCM )2 
2 
) . 
Proof of Lemma C.1. We prove the claim by induction on t. By Assumption 4.3, we have: 
|εt,1(s, a) + γIt,1(s, a)| ≤ 1 + γCM . 
By Hoeffding’s Lemma, we have: 
E[exp(w(εt,1 + γIt,1(s, a)))|Gt−1] ≤ exp 
( w2(1 + γCM )2 
2 
) . 
Therefor, the claim holds for t = 0. Now we assume the claim holds for t− 1: 
E exp(wNt(s, a)) ≤ exp 
( w2βt−1(1 + γCM )2 
2 
) . 
Then, for Nt+1(s, a), we have: 
E exp(wNt+1(s, a)) = E exp(w(1− βt)Nt(s, a) + wβt(εr,t(s, a) + γIt,1(s, a))) 
= E (exp(w(1− βt)Nt(s, a)) · E[exp(wβt(εr,t(s, a) + γIt,1(s, a)))|Gt−1]) 
≤ E exp(w(1− βt)Nt(s, a)) · exp ( w2β2t (1 + γCM )2 
2 
) ≤ exp 
( w2(1− βt) 
2βt−1(1 + γCM )2 
2 
) · exp 
( w2β2t (1 + γCM )2 
2 
) , 
where the last inequality holds by assumption holding for t− 1. Then we have: 
E exp(wNt+1(s, a)) ≤ exp 
( w2((1− βt) 
2βt−1 + β2t )(1 + γCM )2 
2 
) . 
By (1− βt)βt−1 ≤ βt, we finally have: 
E exp(wNt+1(s, a)) ≤ exp 
( w2βt(1 + γCM )2 
2 
) . 
36
Proof of Lemma 4.2. By Lemma C.1, we have: 
E exp(w∥Nt∥∞) ≤ ∑ 
(s,a)∈S×A 
E exp(w|Nt(s, a)|) 
≤ ∑ 
(s,a)∈S×A 
E exp(wNt(s, a)) + E exp(−wNt(s, a)) 
≤ 2|S||A| exp ( w2βt−1(1 + γCM )2 
2 
) . 
Thus, the tail bound of ∥Nt∥∞ satisfies: 
P (∥Nt∥∞ ≥ τ) ≤ 2|S||A| exp ( − τ2 
2βt−1(1 + γCM )2 
) . 
By choosing τ0 = √ 2βt−1(1 + γCM )2 ln(2|S||A|), the expectation of ∥Nt∥∞ satisfies: 
E∥Nt∥∞ = 
∫ +∞ 
0 P(∥Nt∥∞ ≥ τ)dτ = 
∫ τ0 
0 P(∥Nt∥∞ ≥ τ)dτ + 
∫ +∞ 
τ0 
P(∥Nt∥∞ ≥ τ)dτ 
≤ τ0 + 
∫ +∞ 
τ0 
P(∥Nt∥∞ ≥ τ)dτ 
(a) 
≤ τ0 + 2βt−1(1 + γCM )2 
τ0 
≤ 2 √ 2βt−1(1 + γCM )2 ln(2|S||A|), 
where we use ∫ +∞ c exp(−t2)dt ≤ 
∫ +∞ c exp(−ct)dt in (a). 
Proof of Lemma 4.5. By the fact −(at + bt + ct)1+Nt ≤ ∆t ≤ (at + bt + ct)1+Nt, we have: 
E∥∆T ∥∞ ≤ aT + EbT + EcT + E∥NT ∥∞ 
= ∥∆0∥∞ · 
( 1− 
T−1∑ t=0 
βt,T−1 
) + 
γ 
1− γ 
T−1∑ t=0 
βt,T−1 (E∥Nt∥∞ + E∥It,2∥∞) + E∥NT ∥∞ 
≤ ∥∆0∥∞ · 
( 1− 
T−1∑ t=0 
βt,T−1 
) + 
γ 
1− γ 
T−1∑ t=0 
βt,T−1 (E∥Nt∥∞ + εopt) + E∥NT ∥∞. 
Combining with Lemma 4.2, we have: 
E∥∆T ∥∞ ≤ ∥∆0∥∞ · 
( 1− 
T−1∑ t=0 
βt,T−1 
) + 
γ 
1− γ 
T−1∑ t=0 
βt,T−1 
(√ βt−1CN + εopt 
) + √ βTCN , 
where CN := 2 √ 2(1 + γCM )2 ln(2|S||A|). 
Lemma C.2. For βt = 1 1+(1−γ)(t+1) , we have: 
T−1∏ t=0 
(1− βt(1− γ)) = 1 
1 + (1− γ)T . 
37
Proof of Lemma C.2. The result is obtained by calculation directly. 
Proof of Theorem 4.2. By Lemma C.2, we have: 
1− T−1∑ t=0 
βt,T−1 = 1 
1 + (1− γ)T , 
βt,T−1 = 1− γ 
1 + (1− γ)T . 
Combining with Lemma 4.5, we have: 
E∥∆T ∥∞ ≤ ∥∆0∥∞ 1 + (1− γ)T 
+ γCN 
1 + (1− γ)T 
T−1∑ t=0 
√ βt−1 + 
γTεopt 
1 + (1− γ)T + √ βTCN 
≤ ∥∆0∥∞ 1 + (1− γ)T 
+ 2CN√ 
(1− γ)3T + 
εopt 
1− γ + 
CN√ 1 + (1− γ)T 
. 
Combining with Theorem 4.1, we finally have 
E∥∆T ∥∞ ≤ ∥∆0∥∞ 1 + (1− γ)T 
+ 2CN√ 
(1− γ)3T + 
diam(Θ)Cg(2 + lnT ′) 
(1− γ) √ T ′ 
+ CN√ 
1 + (1− γ)T . 
D Proofs of Section 5 
Proof of Lemma 5.1. To ease the notations, we omit the (s, a) dependence here. We notice η∗V satisfies the first order condition: 
EP ∗∇f∗ ( η∗V − V (s′) 
λ 
) = 1. 
Differential by V , we have: 
EP ∗∇2f∗ ( η∗V − V (s′) 
λ 
) ∂η∗V ∂V 
= EP ∗∇2f∗ ( η∗V − V (s′) 
λ 
) ∂V (s′) 
∂V . 
Taking ∥ · ∥1 both sides, we have:∥∥∥∥∂η∗V∂V ∥∥∥∥ 1 
· ∣∣∣∣EP ∗∇2f∗ 
( η∗V − V (s′) 
λ 
)∣∣∣∣ = EP ∗ 
∣∣∣∣∇2f∗ ( η∗V − V (s′) 
λ 
)∣∣∣∣ . Moreover, we notice f∗(·) is a convex function, thus ∇2f∗(·) ≥ 0. Thus, we have 
∥∥∥∂η∗V ∂V 
∥∥∥ 1 = 1. 
Finally, for any V1, V2 ∈ [0, (1− γ)−1]|S|, we have: 
∣∣η∗V1 − η∗V2 
∣∣ = ∣∣∣∣〈∂η∗Ṽ∂V , V1 − V2 
〉∣∣∣∣ ≤ ∥V1 − V2∥∞ , 
where Ṽ lies in the convex combination of V1 and V2. 
38
Proof of Lemma 5.2. Following Algorithm 2, we have: 
δ2t+1(s, a) = 
( ΠΘ 
( ηt(s, a) + αt1(ξt = (s, a)) 
∂Jst+1(ηt(s, a);Vt) 
∂η 
) − η∗t+1(s, a) 
)2 
(a) 
≤ ( ηt(s, a) + αt1(ξt = (s, a)) 
∂Jst+1(ηt(s, a);Vt) 
∂η − η∗t+1(s, a) 
)2 
=δ2t (s, a) + 2αtδt(s, a)1(ξt = (s, a)) ∂Jst+1(ηt(s, a);Vt) 
∂η + 2δt(s, a) 
( η∗t (s, a)− η∗t+1(s, a) 
) + 
( αt1(ξt = (s, a)) 
∂Jst+1(ηt(s, a);Vt) 
∂η + η∗t (s, a)− η∗t+1(s, a) 
)2 
(b) 
≤δ2t (s, a) + 2αtδt(s, a)1(ξt = (s, a)) ∂Jst+1(ηt(s, a);Vt) 
∂η + 2δt(s, a) 
( η∗t (s, a)− η∗t+1(s, a) 
) + 2α2 
t1(ξt = (s, a)) 
( ∂Jst+1(ηt(s, a);Vt) 
∂η 
)2 
+ 2 ( η∗t (s, a)− η∗t+1(s, a) 
)2 (c) =δ2t (s, a) + 2αtδt(s, a)1(ξt = (s, a)) 
( ∂J(ηt(s, a);Vt) 
∂η + gt(s, a) 
) + 2δt(s, a) 
( η∗t (s, a)− η∗t+1(s, a) 
) + 2α2 
t1(ξt = (s, a)) 
( ∂Jst+1(ηt(s, a);Vt) 
∂η 
)2 
+ 2 ( η∗t (s, a)− η∗t+1(s, a) 
)2 (d) 
≤δ2t (s, a)− 2καtδ 2 t (s, a)1(ξt = (s, a)) + 2αtδt(s, a)1(ξt = (s, a))gt(s, a) 
+H1(s, a) +H2(s, a) +H3(s, a), 
where (a) holds by projection property (Lemma E.2), (b) holds by (a+ b)2 ≤ 2a2 + 2b2, (c) holds by setting gt(s, a) := 
∂Jst+1 (ηt(s,a);Vt) 
∂η − E [ ∂Jst+1 (ηt(s,a);Vt) 
∂η 
∣∣∣Ft 
] , and (d) holds by Assumption 5.2. 
Term H1(s, a): By 2ab ≤ λa2 + λ−1b2 for any λ > 0, we have: 
H1(s, a) = 2δt(s, a) ( η∗t (s, a)− η∗t+1(s, a) 
) ≤ λδ2t (s, a) + 
( η∗t (s, a)− η∗t+1(s, a) 
)2 λ 
(a) = καtdπ(s, a)δ 
2 t (s, a) + 
( η∗t (s, a)− η∗t+1(s, a) 
)2 καtdπ(s, a) 
(b) 
≤ καtdπ(s, a)δ 2 t (s, a) + 
∥Vt − Vt+1∥2∞ καtdπ(s, a) 
(c) 
≤ καtdπ(s, a)δ 2 t (s, a) + 
4β2tC 2 M 
καtdπ(s, a) , 
where (a) holds by setting λ = καtdπ(s, a), (b) holds by Lemma 5.1, and (c) holds by updating rule in Algorithm 2 and Assumption 4.3. 
39
Term H2(s, a): By Lemma 4.1, we have: 
H2(s, a) ≤ 2α2 t1(ξt = (s, a))C2 
g . 
Term H3(s, a): By Lemma 5.1, we have: 
H3(s, a) ≤ 2 ∥Vt − Vt+1∥2∞ ≤ 8β2tC 2 M . 
Combing all above together, we have: 
δ2t+1(s, a) ≤ (1− καtdπ(s, a)) δ 2 t (s, a)− 2καtδ 
2 t (s, a) (1(ξt = (s, a))− dπ(s, a)) 
+ 2αtδt(s, a)1(ξt = (s, a))gt(s, a) + 2α2 t1(ξt = (s, a))C2 
g 
+ 4β2tC 
2 M 
καtdπ(s, a) + 8β2tC 
2 M . 
By induction, we have: 
δ2t+1(s, a) ≤ t∏ 
i=0 
(1− καidπ(s, a)) · δ20(s, a) 
− 2κ t∑ 
i=0 
αiδ 2 i (s, a)(1(ξi = (s, a))− dπ(s, a)) 
t∏ j=i+1 
(1− καjdπ(s, a)) 
+ 2 
t∑ i=0 
αiδi(s, a)1(ξi = (s, a))gi(s, a) 
t∏ j=i+1 
(1− καjdπ(s, a)) 
+ 2C2 g 
t∑ i=0 
α2 i 1(ξi = (s, a)) 
t∏ j=i+1 
(1− καjdπ(s, a)) 
+ 4C2 
M 
κdπ(s, a) 
t∑ i=0 
β2i αi 
t∏ j=i+1 
(1− καjdπ(s, a)) 
+ 8C2 M 
t∑ i=0 
β2i 
t∏ j=i+1 
(1− καjdπ(s, a)) 
:=I1(s, a) + I2(s, a) + I3(s, a) + I4(s, a) + I5(s, a) + I6(s, a). 
By Lemma E.3, we know (1− καi+1dπ(s, a))αi ≤ αi+1 and we can bound I1(s, a), I4(s, a), I5(s, a) and I6(s, a) by: 
I1(s, a) ≤ (1− κα0dπ(s, a))αt 
α0 δ20(s, a) ≤ 
αtdiam 2(Θ) 
α0 , 
I4(s, a) ≤ 2C2 gαt 
t∑ i=0 
αi1(ξi = (s, a)) ≤ 2C2 gαt 
t∑ i=0 
αi, 
I5(s, a) ≤ 4C2 
Mαt 
κdπ(s, a) 
t∑ i=0 
β2i α2 i 
, 
40
I6(s, a) ≤ 8C2 Mαt 
t∑ i=0 
β2i αi . 
For I2(s, a), by Lemma E.8, we let ft(s, a) = δt(s, a) 2 and find:∣∣δ2t+1(s, a)− δ2t (s, a) 
∣∣ ≤ 2diam(Θ) |δt+1(s, a)− δt(s, a)| ≤ 2diam(Θ) 
( |ηt+1(s, a)− ηt(s, a)|+ 
∣∣η∗t+1(s, a)− η∗t (s, a) ∣∣) 
≤ 2diam(Θ) (αtCg + 2βtCM ) . 
Thus, setting αt = 1 
κdmin(t+pα)α , we have: 
E ∥I2∥∞ ≤καtdiam 2(Θ)M 
1− ρ 
( 3 + ln(t+ 1 + pα) + κ 
t∑ k=0 
αk + 2 ∑n 
k=0(αtCg + 2βtCM ) 
diam(Θ) 
) 
+ 6 √ 2κ−1d−1 
minαtdiam 2(Θ)M2 ln 2|S||A| 
1− ρ . 
For I3(s, a), noting that δt(s, a)1(ξt = (s, a)) is measurable w.r.t. Ft, we can apply Lemma E.7 and obtain: 
E ∥I3∥∞ ≤ 2 √ 32κ−1d−1 
minαtdiam 2(Θ)C2 
g ln(2|S||A|). 
Setting α = 2 3 in αt, p† := p 2 
3 = 
⌈( dmax dmin 
) 3 2 
⌉ and βt = 1 
(1−γ)dmin(t+p†) , we have: 
∥I1∥∞ ≤ 2diam2(Θ) 
dmin(t+ 1) 2 3 
, 
E ∥I2∥∞ ≤ 3diam(Θ)M(κdiam(Θ) + 2Cg + 2dmin 
√ ln(2|S||A|)) 
κd2min(1− ρ)(t+ 1) 1 3 
+ diam(Θ)M(7dmindiam(Θ) + 4(1− γ)−1LV CM ) ln(t+ 1 + p†) 
d2min(1− ρ)(t+ 1) 2 3 
, 
E ∥I3∥∞ ≤ 12diam(Θ)Cg 
√ ln(2|S||A|) 
κdmin(t+ 1) 1 3 
, 
∥I4∥∞ ≤ 6C2 
g 
κ2d2min(t+ 1) 1 3 
, 
∥I5∥∞ ≤ 12C2 
M 
d2min(1− γ)2(t+ 1) 1 3 
, 
∥I6∥∞ ≤ 32C2 
M 
d2min(1− γ)2(t+ 1) 2 3 
. 
Combing all above, we have: 
E∥δt+1∥2∞ ≤ Φ1 
(t+ 1) 1 3 
+ Φ2 ln(t+ 1 + p†) 
(t+ 1) 2 3 
+ Φ3 
(t+ 1) 2 3 
, 
41
where 
Φ1 = 3diam(Θ)M(κdiam(Θ) + 2Cg + 2dmin 
√ ln(2|S||A|)) 
κd2min(1− ρ) 
+ 6Cg(2κdmindiam(Θ) 
√ ln(2|S||A|) + 2Cg) 
κ2d2min 
+ 12C2 
M 
d2min(1− γ)2 , 
Φ2 = diam(Θ)M(7dmindiam(Θ) + 4(1− γ)−1LV CM ) 
d2min(1− ρ) , 
Φ3 = 2diam2(Θ) 
dmin + 
32C2 M 
d2min(1− γ)2 . 
Proof of Theorem 5.1. We denote ∆t(s, a) := Qt+1(s, a)−Q∗ rob,p(s, a). By Algorithm 2, we have: 
∆t+1(s, a) =(1− βt1(ξt = (s, a)))∆t(s, a) + βt1(ξt = (s, a))(εr,t(s, a) + γεJ,t(s, a)) 
+ γβt1(ξt = (s, a)) ( J (s,a)(ηt(s, a);Vt)− J (s,a)(η∗t ;Vt) 
) + γβt1(ξt = (s, a)) 
( J (s,a)(η∗t ;Vt)− J (s,a)(η∗;V ∗ 
rob,p) ) 
:=(1− βt1(ξt = (s, a)))∆t(s, a) + βtZt,1(s, a) + βtZt,2(s, a) 
+ γβt1(ξt = (s, a)) ( J (s,a)(η∗t ;Vt)− J (s,a)(η∗;V ∗ 
rob,p) ) 
where εJ,t(s, a) = Jst+1(ηt(s, a);Vt) − J (s,a)(ηt(s, a);Vt) and Zt(s, a) covers the second and third terms. Noticing 
∣∣∣J (s,a)(η∗t ;Vt)− J (s,a)(η∗;V ∗ rob,p) 
∣∣∣ ≤ ∥∆t∥∞, we have: 
∆t+1(s, a) ≤(1− βt1(ξt = (s, a)))∆t(s, a) + βt(Zt,1(s, a) + Zt,2(s, a)) + γβt1(ξt = (s, a))∥∆t∥∞, =(1− βtdπ(s, a))∆t(s, a) + βt(Zt,1(s, a) + Zt,2(s, a)) 
+ βt(dπ(s, a)− 1(ξt = (s, a)))(∆t(s, a)− γ∥∆t∥∞) + γβtdπ(s, a)∥∆t∥∞ 
By Lemma E.6, we have: 
∥∆t∥∞ ≤ βt∥∆0∥∞ β0 
+ ∥Bt∥∞ + γβt 
t−1∑ k=0 
∥Bk∥∞, 
where {(Bt(s, a))(s,a)∈S×A}t≥0 satisfies B0 = 0 and 
Bt+1(s, a) =(1− βtdπ(s, a))Bt(s, a) + βt (Zt,1(s, a) + Zt,2(s, a)) 
+ βt(dπ(s, a)− 1(ξt = (s, a)))(∆t(s, a)− γ∥∆t∥∞), 
= t∑ 
i=0 
βiZi,1(s, a) t∏ 
j=i+1 
(1− βjdπ(s, a)) + t∑ 
i=0 
βiZi,2(s, a) t∏ 
j=i+1 
(1− βjdπ(s, a)) 
+ 
t∑ i=0 
βi(dπ(s, a)− 1(ξt = (s, a)))(∆t(s, a)− γ∥∆t∥∞) 
t∏ j=i+1 
(1− βjdπ(s, a)) 
42
:=It+1,1(s, a) + It+1,2(s, a) + It+1,3(s, a). 
For It+1,1(s, a), we notice that Zt,1(s, a) satisfies E[Zt,1(s, a)|Ft] = 0 and |Zt,1(s, a)| ≤ 1 + γCM . By Lemma E.7, we have: 
E∥It+1∥∞ ≤ 3 √ 2d−1 
minβt(1 + γCM )2 ln 2|S||A|. 
For It+1,2(s, a), we notice |Zt,2(s, a)| ≤ γδt(s,a)2 
2σλ by Assumption 4.2. Thus, we have: 
E∥It+1,2∥∞ ≤ γβt 2σλ 
t∑ i=0 
∥δi∥2∞. 
For It+1,3(s, a), we notice: 
∥(∆t+1 − γ∥∆t+1∥∞)− (∆t − γ∥∆t∥∞)∥∞ ≤(1 + γ) ∥∆t+1 −∆t∥∞ =(1 + γ) ∥Qt+1 −Qt∥∞ ≤2(1 + γ)βtCM . 
By Lemma E.8, we have: 
E ∥It+1,3∥∞ ≤2(1 + γ)βtCMM 
1− ρ 
( 3 + ln(t+ 1 + pβ) + 2 
t∑ k=0 
βk 
) 
+ 12(1 + γ) 
√ 2d−1 
minβtC 2 MM 
2 ln 2|S||A| 1− ρ 
. 
By setting βt = 1 (1−γ)dmin(t+pβ) 
, where pβ = ⌈ dmax (1−γ)dmin 
⌉, we have: 
E∥Bt∥∞ ≤3 
√ 2C2 
M ln 2|S||A| d2min(1− γ)(t+ 1) 
+ γ 
2σλdmin(1− γ)(t+ 1) 
t∑ i=0 
E∥δi∥2∞ 
+ 18(1 + γ)CMM ln(t+ 1 + pβ) 
(1− ρ)(1− γ)2d2min(t+ 1) + 12(1 + γ) 
√ 2C2 
MM 2 ln 2|S||A| 
(1− γ)(1− ρ)2d2min(t+ 1) . 
By Lemma 5.2, we have: 
t∑ i=0 
E∥δi∥2∞ ≤ diam2(Θ) + t∑ 
i=1 
( Φ1 
i 1 3 
+ Φ2 ln(i+ p†) 
i 2 3 
+ Φ3 
i 2 3 
) ≤ diam2(Θ) + 
3Φ1 
2 t 2 3 + 3Φ2t 
1 3 ln(t+ p†) + 3Φ3t 
1 3 
≤ diam2(Θ) + 3Φ1 
2 t 2 3 + 3(Φ2 + 2Φ3)t 
1 3 ln(t+ 1 + p†). 
Thus, we have 
E∥Bt∥∞ ≤3 
√ 2C2 
M ln 2|S||A| d2min(1− γ)(t+ 1) 
+ diam2(Θ) 
2σλdmin(1− γ)(t+ 1) + 
3Φ1 
4σλdmin(1− γ)(t+ 1) 1 3 
43
+ 3(Φ2 + 2Φ3) ln(t+ 1 + p†) 
2σλdmin(1− γ)(t+ 1) 2 3 
+ 36CMM ln(t+ 1 + pβ) 
(1− ρ)(1− γ)2d2min(t+ 1) + 24 
√ 2C2 
MM 2 ln 2|S||A| 
(1− γ)(1− ρ)2d2min(t+ 1) . 
The dominating term in E∥Bt∥∞ is of order (t+1) 1 3 , thus, the dominating term in E∥∆t∥∞ satisfies: 
E∥∆t∥∞ ≤ Õ 
( Φ1 
σλdmin(1− γ)2(t+ 1) 1 3 
) . 
E Auxiliary Lemma 
Lemma E.1 (Exercise 2.12 in Wainwright [2019a]). Let {Xi}ni=1 be a sequence of mean-zero random variables, which satisfy (for any λ ∈ R): 
E[exp(λXi)] ≤ exp 
( λ2σ2 
2 
) . 
Then, the following inequality holds: 
E [ 
max i=1,··· ,n 
Xi 
] ≤ 
√ 2σ2 lnn. 
Proof. Indeed, for any λ > 0 we have: 
exp 
( λE [ 
max i=1,··· ,n 
Xi 
]) (a) 
≤ E [ exp 
( λ max 
i=1,··· ,n Xi 
)] ≤ E 
[ n∑ 
i=1 
exp(λXi) 
] 
≤ n exp 
( λ2σ2 
2 
) . 
Thus, we have: 
E [ 
max i=1,··· ,n 
Xi 
] ≤ inf 
λ>0 
( lnn 
λ + λσ2 
2 
) = 
√ 2σ2 lnn. 
Lemma E.2 (Lemma 3.1 in Bubeck et al. [2015]). Let ∥ · ∥ denote the Euclidean norm on set X ⊂ Rd. For any y ∈ Rd, we define the projection operator ΠX on X by: 
ΠX (y) = argmin x∈X 
∥x− y∥. 
Then, for any x ∈ X and y ∈ Rd, we have: 
(ΠX (y)− x)⊤ (ΠX (y)− y) ≤ 0, 
which also implies ∥ΠX (y)− x∥2 + ∥ΠX (y)− y∥2 ≤ ∥y − x∥2. 
44
Lemma E.3. Denote αt = 1 
(1+t)α , where α ∈ (0, 1] and t ∈ Z. Then, for any t ∈ Z+, we have: 
(1− αt)αt−1 ≤ αt. 
Proof. For α = 1, the result holds trivially. For 0 < α < 1, we denote f(t) = (1+ t)α − 1− tα, where t ∈ [0,+∞). The derivative of f(x) satisfies: 
f ′(t) = α 
( 1 
(1 + t)1−α − 1 
t1−α 
) ≤ 0. 
Thus, f(t) ≤ f(0) = 0 and our result is obtained. 
Lemma E.4. Denote αt = 1 
(1+t)α , where α ∈ (0, 1] and t ∈ Z. Then, for any i ≤ j we have: 
j∑ t=i 
αt ≤ 
{ (1+j)1−α−i1−α 
1−α if α ∈ (0, 1), 1(i = 0) + ln(j + 1)− ln(1(i = 0) + i) if α = 1. 
Proof. For α ∈ (0, 1), we have: 
j∑ t=i 
αt ≤ ∫ j 
i−1 
1 
(1 + x)α dx = 
(1 + j)1−α − i1−α 
1− α . 
For α = 1 and i ≥ 1, we have: 
j∑ t=i 
αt ≤ ∫ j 
i−1 
1 
1 + x dx = ln (1 + j)− ln i. 
For α = 1 and i = 0, we have: 
j∑ t=0 
αt ≤ 1 + 
∫ j 
0 
1 
1 + x dx = 1 + ln (1 + j) . 
Lemma E.5. For any α ∈ (0, 1) and t > 0, we have: 
(t+ 1)α − tα ≤ 1 
t1−α . 
Proof. We denote f(x) = (1 + x)α − x− 1, where x ≥ 0. Its derivative satisfies: 
f ′(x) = α 
(1 + x)1−α − 1 < α− 1 < 0. 
Thus, f(x) ≤ f(0) = 0. Taking x = 1 t , we have:( 
1 + 1 
t 
)α 
− 1 
t − 1 ≤ 0. 
Arranging terms, the final result is obtained. 
45
Lemma E.6. Suppose {(Xt(i))i∈[d]}t≥0 and {(Yt(i))i∈[d]}t≥0 are two sequences that satisfy the following inequalities: 
Yt+1(i) ≤ (1− αtci)Yt(i) + αtXt(i) + γαtd(i)∥Yt∥∞, Yt+1(i) ≥ (1− αtci)Yt(i) + αtXt(i)− γαtd(i)∥Yt∥∞, 
where γ ∈ [0, 1), ci > 0, (1− (1− γ)αtci)αt−1 ≤ αt, and α0 ≤ c−1 i for all t ≥ 1 and i ∈ [d]. Then, 
we have: 
∥Yt∥∞ ≤ αt∥Y0∥∞ α0 
+ ∥Bt∥∞ + γαt 
t−1∑ k=0 
∥Bk∥∞, 
where {(Bt(i))i∈[d]}t≥0 satisfies Bt+1(i) = (1− αtci)Bt(i) + αtXt(i) and B0 = 0. 
Proof. We construct auxiliary sequences: 
At+1 = (1− (1− γ)αtcmin)At, 
Bt+1(i) = (1− αtci)Bt(i) + αtXt(i), 
Ct+1(i) = (1− (1− γ)αtci)∥Ct∥∞ + γαtci∥Bt∥∞, 
where A0 = ∥Y0∥∞, B0 = 0 and C0 = 0. By induction, for t, we assume: 
−(At + ∥Ct∥∞) +Bt(i) ≤ Yt(i) ≤ (At + ∥Ct∥∞) +Bt(i). 
Then, for t+ 1, we have: 
Yt+1 ≤ (1− αtci) ((At + ∥Ct∥∞) +Bt(i)) + αtXt(i) + γαtci ((At + ∥Ct∥∞) + ∥Bt∥∞) 
≤ (At+1 + ∥Ct+1∥∞) +Bt+1(i). 
Reversely, we have: 
Yt+1 ≥ (1− αtci) (−(At + ∥Ct∥∞) +Bt(i)) + αtXt(i)− γαtci ((At + ∥Ct∥∞) + ∥Bt∥∞) 
≥ −(At+1 + ∥Ct+1∥∞) +Bt+1(i). 
Thus, the following inequality holds for t ≥ 0: 
−(At + ∥Ct∥∞) +Bt(i) ≤ Yt(i) ≤ (At + ∥Ct∥∞) +Bt(i). 
By definition of At, Bt, Ct and (1− (1− γ)αtci)αt−1 ≤ αt, the following upper bouds lead to the final result: 
At = 
t−1∏ k=0 
(1− (1− γ)αkcmin) · ∥Y0∥∞ ≤ αt∥Y0∥∞ α0 
, 
Bt(i) = t−1∑ k=0 
αkXk(i) t−1∏ 
j=k+1 
(1− (1− γ)αjci), 
∥Ct∥∞ ≤ γ 
t−1∑ k=0 
αk∥Bk∥∞ t−1∏ 
j=k+1 
(1− (1− γ)αjcmin) ≤ γαt 
t−1∑ k=0 
∥Bk∥∞. 
46
Lemma E.7. Suppose {(Xt(i))i∈[d]}t≥0 is a martingale difference w.r.t. filtration {Ft}t≥0, satisfying E[Xt(i)|Ft] = 0 and |Xt(i)| ≤M , a.s. for all i ∈ [d]. For recursion Yt+1(i) = (1−αtci)Yt(i)+αtXt(i), where Y0(i) = 0, ci > 0, (1− αtci)αt−1 ≤ αt, and α0 ≤ c−1 
i for all t ≥ 1 and i ∈ [d], for any λ ∈ R, we have: 
E exp (λ ∥Yt∥∞) ≤ exp 
( λ2αt−1M 
2 
2cmin 
) , (27) 
where cmin = mini∈[d] ci. And also, E ∥Yt∥ ≤ 3 √ 2c−1 
minαt−1M2 ln 2d. 
Proof. Firstly, we prove the following inequality by induction. 
E exp (λYt(i)) ≤ exp 
( λ2αt−1M 
2 
2cmin 
) , 
which is true when t = 1. For Yt+1(i), we have: 
E exp(λYt+1(i)) = E exp(λ((1− αtci)Yt(i) + αtXt(i))) 
≤ E exp 
( λ2(1− αtci) 
2αt−1M 2 
2cmin + λ2α2 
tM 2 
2 
) ≤ exp 
( λ2αtM 
2 
2cmin 
) , 
where the last inequality is true due to (1− αtci)αt−1 ≤ αt. Thus, for ∥Yt∥∞, we have: 
E exp(λ ∥Yt∥∞) ≤ ∑ i∈[d] 
E exp(λ|Yt(i)|) 
≤ ∑ i∈[d] 
E exp(λYt(i)) + E exp(−λYt(i)) 
≤ 2d exp 
( λ2αt−1M 
2 
2cmin 
) . 
Then, the tail bound of ∥Yt∥∞ satisfies: 
P (∥Yt∥∞ ≥ τ) ≤ 2d exp 
( − cminτ 
2 
2αt−1M2 
) . 
By choosing τ0 = √ 
2c−1 minαt−1M2 ln 2d, the expectation of |Yt| satisfies: 
E ∥Yt∥∞ = 
∫ +∞ 
0 P(∥Yt∥∞ ≥ τ)dτ = 
∫ τ0 
0 P(∥Yt∥∞ ≥ τ)dτ + 
∫ +∞ 
τ0 
P(∥Yt∥∞ ≥ τ)dτ 
≤ τ0 + 
∫ +∞ 
τ0 
P(∥Yt∥∞ ≥ τ)dτ 
(a) 
≤ τ0 + 2αt−1M 
2 
cminτ0 
≤ 3 √ 2c−1 
minαt−1M2 ln 2d, 
where we use ∫ +∞ c exp(−x2)dx ≤ 
∫ +∞ c exp(−cx)dx in (a). 
47
Lemma E.8. Denote {ξt}Tt=0 is the random variable on a Markovian decision chain (S ×A, P π), which satisfies fast mixing property in Assumption 5.1, and Ft := σ(∪k<tσ(ξk)), for any recursion Xt+1(s, a) = (1−αtdπ(s, a))Xt(s, a)+αtft(s, a) (1(ξt = (s, a))− dπ(s, a)) satisfying αt = 
1 dmin(t+pα)α 
, 
where pα := 
⌈( dmax dmin 
)1/α⌉ , and ft(s, a) is measurable w.r.t. Ft, we have: 
E ∥Xt+1∥∞ ≤ αtMfM 
1− ρ 
( 3 + ln(t+ 1 + pα) + 
t∑ k=0 
αk + 
∑n k=0 E ∥fk+1 − fk∥∞ 
Mf 
) 
+ 6 √ 2d−1 
minαtM2 fM 
2 ln 2|S||A| 
1− ρ , 
where: 
t∑ k=0 
αk ≤ 
{ ln(t+p1)−ln(p1−1) 
dmin if α = 1, 
(t+pα)1−α−(pα−1)1−α 
1−α if α ∈ (0, 1). 
Proof. By Assumption 5.1, we notice that:∣∣∣∣∣ +∞∑ t=0 
(P π t (s, a|ξt)− dπ(s, a)) 
∣∣∣∣∣ ≤ +∞∑ t=0 
max (s,a)∈S×A 
dTV (P π t (·|s, a), dπ(·)) 
≤ M 
1− ρ . 
Thus, we can decompose the 1(ξt = (s, a))− dπ(s, a) into: 
1(ξt = (s, a))− dπ(s, a) = 
( +∞∑ k=0 
P π k (s, a|ξt)− dπ(s, a) 
) − 
( +∞∑ k=1 
P π k (s, a|ξt)− dπ(s, a) 
) := ψ(s, a; ξt)− Pψ(s, a; ξt), 
where Pψ(s, a; ξ) := ∑ 
(s′,a′)∈S×A ψ(s, a; s ′, a′)P π(s′, a′|ξ). Thus, the update rule of Xt(s, a) can be 
written by: 
Xt+1(s, a) =(1− αtdπ(s, a))Xt(s, a) + αtft(s, a) (ψ(s, a; ξt)− Pψ(s, a; ξt)) =(1− αtdπ(s, a))Xt(s, a) + αtft(s, a) (ψ(s, a; ξt)− Pψ(s, a; ξt−1)) 
+ αtft(s, a) (Pψ(s, a; ξt−1)− Pψ(s, a; ξt)) . 
We denote X̃t(s, a) = Xt(s, a) + αtft(s, a)Pψ(s, a; ξt−1)), then we have: 
X̃t+1(s, a) =(1− αtdπ(s, a))X̃t(s, a) + αtft(s, a) (ψ(s, a; ξt)− Pψ(s, a; ξt−1)) 
+ α2 t dπ(s, a)ft(s, a)Pψ(s, a; ξt−1) + αt+1ft+1(s, a)Pψ(s, a; ξt)− αtft(s, a)Pψ(s, a; ξt) 
=(1− αtdπ(s, a))X̃t(s, a) + αtft(s, a) (ψ(s, a; ξt)− Pψ(s, a; ξt−1)) 
+ α2 t dπ(s, a)ft(s, a)Pψ(s, a; ξt−1) + αt+1 (ft+1(s, a)− ft(s, a))Pψ(s, a; ξt) 
+ (αt+1 − αt) ft(s, a)Pψ(s, a; ξt) 
48
:=(1− αtdπ(s, a))X̃t(s, a) + αt∆1,t(s, a) + α2 t dπ(s, a)∆2,t(s, a) 
+ αt+1∆3,t(s, a) + (αt+1 − αt)∆4,t(s, a), 
where 
∆1,t(s, a) := ft(s, a) (ψ(s, a; ξt)− Pψ(s, a; ξt−1)) 
∆2,t(s, a) := ft(s, a)Pψ(s, a; ξt−1) 
∆3,t(s, a) := (ft+1(s, a)− ft(s, a))Pψ(s, a; ξt) ∆4,t(s, a) := ft(s, a)Pψ(s, a; ξt). 
Recursively solving above equation, we have: 
X̃t+1(s, a) = 
t∏ k=0 
(1− αkdπ(s, a)) · X̃0(s, a) + 
t∑ k=0 
αk∆1,k(s, a) 
t∏ i=k+1 
(1− αidπ(s, a)) 
+ 
t∑ k=0 
α2 kdπ(s, a)∆2,k(s, a) 
t∏ i=k+1 
(1− αidπ(s, a)) 
+ t∑ 
k=0 
αk+1∆3,k(s, a) t∏ 
i=k+1 
(1− αidπ(s, a)) 
+ t∑ 
k=0 
(αk+1 − αk)∆4,k(s, a) t∏ 
i=k+1 
(1− αidπ(s, a)). 
For the second term, we notice ∆1,k(s, a) is a martingale difference w.r.t. filtration {Ft}t≥0, which satisfies E[∆1,k(s, a)|Fk] = 0 and |∆1,k(s, a)| ≤ 
2MfM 1−ρ . Thus, by Lemma E.7, we have: 
E max (s,a)∈S×A 
∣∣∣∣∣ t∑ 
k=0 
αk∆1,k(s, a) t∏ 
i=k+1 
(1− αidπ(s, a)) 
∣∣∣∣∣ ≤ 6 √ 2d−1 
minαtM2 fM 
2 ln 2|S||A| 
1− ρ . 
For other terms, we apply inequality (1− αtdπ(s, a))αt−1 ≤ αt. Thus, we can bound E ∥∥∥X̃t+1 
∥∥∥ ∞ 
by: 
E ∥∥∥X̃t+1 
∥∥∥ ∞ 
≤(1− α0dmin)αt 
α0 E ∥∥∥X̃0 
∥∥∥ ∞ 
+ 6 √ 
2d−1 minαtM2 
fM 2 ln 2|S||A| 
1− ρ + αt 
MfM ∑t 
k=0 αk 
1− ρ 
+ αt M ∑t 
k=0 E∥fk+1 − fk∥∞ 1− ρ 
+ αt 
MfM ∑t 
k=0 αk−αk+1 
αk 
1− ρ . 
Then, by definition of X̃t and E ∥∥∥X̃0 
∥∥∥ ∞ 
≤ MfM 1−ρ , we have: 
E ∥Xt+1∥∞ ≤αt (1− α0dmin)MfM 
1− ρ + 
6 √ 
2d−1 minαtM2 
fM 2 ln 2|S||A| 
1− ρ + αt 
MfM ∑t 
k=0 αk 
1− ρ 
+ αt M ∑t 
k=0 E∥fk+1 − fk∥∞ 1− ρ 
+ αt 
MfM ∑t 
k=0 αk−αk+1 
αk 
1− ρ + αt+1 
MfM 
1− ρ . 
49
By Lemma E.4, when α = 1, we have: 
t∑ k=0 
αk ≤ ln (t+ p1)− ln (p1 − 1) 
dmin 
t∑ k=0 
αk − αk+1 
αk = 
t∑ k=0 
1 
k + 1 + p1 ≤ ln (t+ p1 + 1)− ln p1. 
When α ∈ (0, 1), we have: 
t∑ k=0 
αk ≤ (t+ pα) 1−α − (pα − 1)1−α 
1− α 
t∑ k=0 
αk − αk+1 
αk = 
t∑ k=0 
1− (k + pα) α 
(k + pα + 1)α ≤ 
t∑ k=0 
1 
k + pα ≤ ln(t+ pα) + 
1 
pα − ln pα. 
Combining all above together, we have: 
E ∥Xt+1∥∞ ≤ αtMfM 
1− ρ 
( 3 + ln(t+ 1 + pα) + 
t∑ k=0 
αk + 
∑n k=0 E ∥fk+1 − fk∥∞ 
Mf 
) 
+ 6 √ 2d−1 
minαtM2 fM 
2 ln 2|S||A| 
1− ρ . 
50