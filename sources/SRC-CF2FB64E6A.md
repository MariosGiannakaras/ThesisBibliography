> Source: https://arxiv.org/pdf/2203.00543

On the Generalization of Representations in Reinforcement Learning 
Charline Le Lan Stephen Tu Adam Oberman University of Oxford Google Brain McGill University 
Rishabh Agarwal Marc Bellemare Google Brain Google Brain 
Abstract 
In reinforcement learning, state representations are used to tractably deal with large problem spaces. State representations serve both to approximate the value function with few parameters, but also to generalize to newly encountered states. Their features may be learned implicitly (as part of a neural network) or explicitly (for example, the successor representation of Dayan (1993)). While the approximation properties of representations are reasonably well-understood, a precise characterization of how and when these representations generalize is lacking. In this work, we address this gap and provide an informative bound on the generalization error arising from a specific state representation. This bound is based on the notion of effective dimension which measures the degree to which knowing the value at one state informs the value at other states. Our bound applies to any state representation and quantifies the natural tension between representations that generalize well and those that approximate well. We complement our theoretical results with an empirical survey of classic representation learning methods from the literature and results on the Arcade Learning Environment, and find that the generalization behaviour of learned representations is well-explained by their effective dimension. 
Proceedings of the 25th International Conference on Artifi-cial Intelligence and Statistics (AISTATS) 2022, Valencia, Spain. PMLR: Volume 151. Copyright 2022 by the author(s). 
Figure 1: A deep RL architecture seen as a deep representation φ and a value prediction V̂φ,w. 
1 INTRODUCTION 
At the heart of reinforcement learning (RL) is the problem of predicting the expected return that can be obtained from different states. In most practical situations, these predictions are made on the basis of parametric function approximation, needed in order to make accurate predictions on the basis of limited samples – technically speaking, to estimate the value function (Sutton and Barto, 2018). Linear function approximation, for example, estimates the value function using a fixed state representation φ which maps states to vectors in Rk; general-purpose algorithms for constructing state representations include tile coding (Sutton, 1996), the Fourier basis (Konidaris et al., 2011), local basis functions (Ratitch and Precup, 2004), and methods based on properties of the transition function (Mahadevan and Maggioni, 2007; Ghosh and Bellemare, 2020). Common deep RL network architectures such as DQN (Mnih et al., 2015) use multiple layers of nonlinear transformations to map perceptual inputs to a final layer which is linearly transformed into a value function prediction (Figure 1); accordingly, we may also view this final layer as a (time-varying) state representation φ (Levine et al., 2017; Chung et al., 2018). 
 
 
 
 
 
 
 
 
 
 
On the Generalization of Representations in Reinforcement Learning 
It is generally believed that auxiliary tasks, known to improve performance in deep reinforcement learning (Jaderberg et al., 2017; Bellemare et al., 2017), play an important role in shaping the learned state representation (Bellemare et al., 2019; Dabney et al., 2020; Lyle et al., 2021). This motivates the need to understand how representation learning impacts policy evaluation. In this paper, we give a theoretical characterization of the generalization properties of a given or learned representation. While there are a number of results characterizing the approximation error due to a representation (Petrik, 2007; Parr et al., 2008), its effect on statistical error is relatively unknown. 
Our first contribution is a bound on the generalization error (approximation + estimation) that arises when performing Monte Carlo value function estimation with a given k-dimensional representation φ (Section 3). Critically, this bound depends on the (in)coherence of the feature matrix Φ (Candès and Recht, 2009), which in turns defines the effective dimension of the representation. This effective dimension determines how many samples are needed to obtain a good generalization of the value function with the chosen representation; it may be as low as k, indicating that generalization is as good as possible, or as high as |S|, the number of states, indicating no generalization at all. The bound applies more broadly to the generalization error incurred in least-squares regression problems where a subset of a larger set of points is observed. 
In Section 4, we demonstrate the usefulness of our bound by specializing it to study the generalization properties of the successor representation (SR) (Dayan, 1993). Specifically, we consider the state representation constructed from the top k singular vectors of the SR (Stachenfeld et al., 2014; Machado et al., 2017; Behza-dian and Petrik, 2018). Empirically, we find that the effective dimension of this representation – and consequently its generalization characteristics – can vary substantially according to the transition structure of the environment. We also show empirically that the effective dimension is important to determine the generalization capacity of different theoretically-motivated representations in the four room domain (Sutton et al., 1999). 
In an empirical study on the Arcade Learning Environment (Bellemare et al., 2013), we find that the notions of incoherence and effective dimension correlate with the observed empirical performance of existing value-based deep RL agents (Subsection 5.2). Furthermore, we find that a simple auxiliary loss motivated by our bound shows promising gains in the offline deep RL setting. 
2 BACKGROUND 
We consider a Markov Decision Process (MDP) M = 〈S,A,R,P, γ〉 (Puterman, 1994) with finite state space S, discrete set of actions A, transition kernel P : S × A →P(S), deterministic reward functionR : S×A → [−Rmax, Rmax], and discount factor γ ∈ [0, 1). For simplicity, we make the correspondence S = {1, ..., S}. We write Pas to denote the next-state distribution over S resulting from selecting action a in s and write Ras for the corresponding reward. 
A stationary policy π : S →P(A) is a mapping from states to distributions over actions, describing a particular way of interacting with the environment. We denote the set of all policies by Π. For any policy π ∈ Π, the value function V π(s) measures the expected discounted sum of rewards received when starting from state s ∈ S and acting according to π: 
V π(s) := E π,P 
[ ∞∑ t=0 
γtRatst | s0 = s, at ∼ π(· | st) 
] . 
The upper-bound value is Vmax := Rmax 
1−γ . In vector 
notation (Puterman, 1994), let rπ ∈ RS denote the vector of expected rewards, and let Pπ ∈ RS×S be the transition matrix whose entries are 
Pπ(s, s′) = ∑ s′∈S Pas (s′)π(a | s). 
We then have 
V π = 
∞∑ t=0 
(γPπ)trπ = (I − γPπ)−1rπ. 
In this paper we consider approximating the value function V π using a linear combination of features. We call the map φ : S → Rk a k-dimensional state representation; φ(s) is the feature vector for a state s ∈ S. In general, we will be interested in the setting where k  S. The value function approximation at s is 
Vφ,w(s) = φ(s)>w, 
where w ∈ Rk is a weight vector. We collect the perstate feature vectors into a feature matrix Φ ∈ RS×k. For simplicity, we assume Φ has full column rank. In vector form, the value function approximation (a S-dimensional vector) is more directly expressed as 
Vφ,w = Φw. 
2.1 Statistical Learning Theory 
We consider the batch Monte Carlo policy evaluation setting, in which we are given a sample of training
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
examples D = {(s1, y1), . . . , (sn, yn)} ∈ (S × R)n and wish to determine a good linear approximation to V π 
on the basis of this sample. Here, si is a state and yi is a realisation of the random return Gπ(si) (Bellemare et al., 2017; Sutton and Barto, 2018), defined by the random-variable equation 
Gπ(s) = 
∞∑ t=0 
γtRatst , s0 = s, at ∼ π(· | st). 
We assume that si is drawn uniformly at random from S.1 The batch Monte Carlo setting obviates some of the technical challenges in analyzing iterative methods such as least-squares TD (LSTD) but still allows us to provide practically-relevant theoretical guarantees. 
We measure the quality of a linear approximation Vφ,w in terms of the expected squared error 
R(Vφ,w) = 1 
S 
∑ s∈S 
E y∼Gπ(s) 
( Vφ,w(s)− y 
)2 . (1) 
For a value function V , we express this error and related quantities in terms of the uniformly-weighted L2 norm 
‖V ‖S,2 = 
√ 1 
S 
∑ s∈S 
( V (s) 
)2 . 
Following terminology from statistical learning theory (Vapnik, 1995), we call R(Vφ,w) the population risk of Vφ,w. One can verify that R(Vφ,w) is minimized when Vφ,w = V π. 
Given the dataset D and a fixed state representation φ, least-squares regression determines the weight vector ŵ minimizing the empirical risk function 
R̂(Vφ,w) = 1 
n 
n∑ i=1 
(Vφ,w(si)− yi)2. 
Notice that R̂ is a random function as it depends on the training sample D. 
We are interested in the performance of the leastsquares approximation Vφ,ŵ compared to the true value function V π. Let us denote by Vφ,w∗ the linear approximation minimizing the population risk, such that 
w∗ = arg min w∈Rk 
R(Vφ,w). 
For clarity of exposition, we will assume this approximation is unique. The excess risk E(Vφ,ŵ) = R(Vφ,ŵ) − R(V π) measures the additional error suffered by the approximation Vφ,ŵ compared to the true value function. We decompose it into an estimation 
1Results for a larger class of distributions are given in Appendix A 
error term, measuring the performance gap with the best-in-class, and an approximation error term arising from considering a restricted set of k-dimensional value function approximations: 
E(Vφ,ŵ) = R(Vφ,ŵ)−R(Vφ,w∗)︸ ︷︷ ︸ estimation error 
+R(Vφ,w∗)−R(V π)︸ ︷︷ ︸ approximation error 
. 
2.2 The Successor Representation 
The successor representation (Dayan, 1993) describes a state in terms of the frequency at which it visits future states; it is also related to the fundamental matrix in the study of Markov chains see Kemeny and Snell (1961); Brémaud (2013); Grinstead and Snell (2012). 
Definition 1. The successor representation (SR) with respect to a policy π for a state s ∈ S is the expected discounted sum of future occupancies for each state s′ ∈ S. Specifically, ψπ(s) = (ψπ(s, s′))s′∈S , where 
ψπ(s, s′) = E π,P 
[ ∞∑ t=0 
γtI [st = s′] | s0 = s 
] . 
Expressed as a matrix Ψπ ∈ RS×S, the successor representation can be written as: 
Ψπ = (I − γPπ) −1 . 
As a consequence of the Bellman equation, we can express the value function in terms of the successor representation as follows: 
V π = Ψπrπ. 
This makes it a particularly appealing candidate to use as a state representation. In particular, it is wellestablished that the top eigenvectors (Mahadevan and Maggioni, 2007) or singular vectors (Behzadian and Petrik, 2018) of the successor representation form a useful representation (Stachenfeld et al., 2014). Petrik (2007) derived an analytical bound on the approximation error for linear value function approximation for a representation made of the top eigenvectors of Ψπ in the particular setting where Pπ is symmetric. By contrast, in this paper, we consider the more general setting of an arbitrary transition matrix Pπ and consider a generalization bound that accounts for the statistical nature of the learning process. 
3 CHARACTERIZING EXCESS RISK 
Our first result characterizes how the choice of representation affects the generalization of value functions. Theorem 1 applies beyond the setting of reinforcement
On the Generalization of Representations in Reinforcement Learning 
learning, and more generally characterizes the excess risk of a broad class of least-squares regression problems. 
To begin, we assume that the labels y1, . . . , yn satisfy 
yi = V (si) + ηi, 
where V : S → R and ηi is i.i.d. zero mean σ-sub-Gaussian noise (Vershynin, 2010). This includes the batch Monte Carlo setting, in which case V = V π and 
ηi D = Gπ(si) − V π(si), where Gπ(si) is the random 
return from si. 
For a feature matrix Φ, we write PΦ for the orthogonal projector onto its column space, and P⊥Φ for the orthogonal projector onto the corresponding nullspace. We have 
PΦ = Φ(ΦTΦ)−1ΦT P⊥Φ = IS − PΦ. 
In particular, the approximation error for a given state representation φ is 
R(Vφ,w∗)−R(V ) = ‖P⊥Φ V ‖2S,2. 
A key quantity in our analysis is the notion of the effective dimension of a state representation, which dictates the number of samples required to achieve a low estimation error. 
Definition 2 (Effective dimension). Let Φ ∈ RS×k be a feature matrix. The effective dimension of Φ (vis-a-vis the standard basis (ei)) is defined as the quantity 
deff(Φ) := S max i=1,...,S 
‖PΦei‖22, 
where PΦ is the orthogonal projector onto the column space of Φ. 
It is simple to check that the effective dimension is only a function of the column space of Φ and that deff(Φ) satisfies 
rank(Φ) 6 deff(Φ) 6 S. 
Our notion of effective dimension is derived from the coherence of Φ, defined as 
µ(Φ) = deff 
rank(Φ) . 
The notion of coherence is from Candès and Recht (2009), who demonstrate that coherence can be used to characterize the feasibility of low-rank matrix recovery. Informally, µ(Φ) (and deff(Φ)) measure the (lack of) sparsity of the column space of Φ. At one extreme, if Φ ∈ RS×1 is the all-ones vector, then deff(Φ) = rank(Φ), saturating the lower bound. On the other hand, if Φ = ei for some i ∈ {1, . . . , S} then deff(Φ) = S, saturating the upper bound. As we now show, the effective dimension of Φ can be used to bound the excess risk of least-squares regression applied to the state representation φ. 
Theorem 1 (Excess risk). Fix any δ ∈ (0, 1). Suppose that n > 8deff(Φ) log(6k/δ). With probability at least 1− δ, the empirical risk minimizer Vφ,ŵ satisfies: 
E(Vφ,ŵ) 6 ‖P⊥Φ V ‖2S,2 + 384c deff(Φ) 
n ‖P⊥Φ V ‖2S,2 
+ 48σ2 2k + 3c 
n + 
64 
3 
deff(Φ) 
n2 ‖P⊥Φ V ‖2∞c2, 
where c = log(3/δ) and ‖·‖∞ denotes the usual supremum norm. 
Proof. The proof is given in Appendix A, and follows arguments for the analysis of random design linear least-squares problems (Hsu et al., 2012b) and matrix concentration inequalities (Tropp, 2015). The result can also be obtained by instantiating Theorem 1 of Hsu et al. (2012b) to our setting, at the cost of added complexity. 
In Theorem 1, the term ‖P⊥Φ V ‖2S,2 is the approximation error and reflects the error due to using a k-dimensional linear approximation. The remainder of the bound corresponds to the estimation error. The theorem demonstrates that the ability of a representation to generalize is quantified not only by the approximation error but also the effective dimension deff(Φ). Not only does deff(Φ) appear in the bound, but it also dictates a minimum number of samples needed to obtain a high probability bound: when deff(Φ) is small, the bound holds for fewer samples. 
In the specific context of batch Monte Carlo policy evaluation, Theorem 1 holds as-is with V = V π. Addi-tionally, the noise variance σ2 can be bounded as 
σ2 6 V 2 
max 
4 . 
The term ‖PΦei‖22 that drives the effective dimension of Φ differs (for non orthogonal representations Φ) from the quantity maxi ‖φ(si)‖22 that appears in Rademacher complexity bounds for regression in the case of a family of linear predictors (Mohri et al., 2018) (see also Mail-lard and Munos (2009)). Compared to such bounds, Theorem 1 is also sharper for all representations as it offers a O(1/n) dependency rather than O(1/ 
√ n). In 
subsequent sections, we will provide empirical evidence illustrating how the effective dimension plays a critical role in determining the generalization capability of φ. 
3.1 Illustrative Examples 
To understand how the bound is instantiated in particular settings, consider first the scenario in which Φ = IS is the tabular representation. This corresponds to using the feature vector ei ∈ RS for the i-th state.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
In this case, the approximation error is 0 and the estimation error reduces to the classic σ2S/n rate for least-squares regression: 
R(Vφ,ŵ)−R(V ) . σ2(S + log(1/δ)) 
n . 
With this choice of features, good generalization requires a number of samples n linear in S. 
At the other extreme, it is possible to improve the sample complexity to avoid the dependency on S. In the ideal case, deff(Φ) = k. In the next section we will demonstrate that, in environments with a particular transition structure, representations derived from the successor representation achieve this bound. 
To make this argument more concrete, suppose that we have a family (φk)Sk=1 of representations (resp. matrices (Φk)) whose effective dimension satisfies deff(Φk) ≈ k. Furthermore, assume that the approximation error ‖P⊥ΦkV ‖ 
2 S,2 scales as ψ(k), where ψ(k) is a monotoni-
cally decreasing function of k. Fix ε > 0 and define k̄ = k̄(ε) := min{k : ψ(k) 6 ε}, and let w̄ be the weight vector found by least-squares regression applied with φk̄. Observe that as long as n satisfies: 
n & max 
{ max 
{σ2 
ε , 1 } k̄(ε) log 
k̄(ε) 
δ , √ k̄(ε)S log 
1 
δ 
} , 
then we have E(Vφk̄,w̄) 6 4ε. As a particular example, let ψ(k) = ρk for some ρ ∈ (0, 1). Then k̄(ε) 6 d 1 
1−ρ log ( 
1 ε 
) e, in which case the sample com-
plexity only depends sublinearly on S. 
4 GENERALIZATION FOR THE SUCCESSOR REPRESENTATION 
An effective approach for constructing a family of representations is to take the k singular vectors of the successor representation (SR) whose singular values are the greatest. For a given policy π, let Ψπ be the successor representation for π. We write 
Ψπ = FΣB>, 
where F,B ∈ RS×S are matrices whose columns are orthogonal and have unit norm. Additionally, Σ = diag(σ1, ..., σS) where σi are the singular values of Ψ sorted in decreasing order. 
For a fixed integer k satisfying 1 6 k 6 S, let us partition F into two matrices, Fk ∈ RS×k and F⊥k , which respectively contains the top k and bottom S−k columns of F . Correspondingly, we partition Σ into Σk ∈ Rk×k and Σ⊥k and B into Bk and B⊥k . With this notation, we obtain the family of state representations (expressed as feature matrices) Φk = Fk. 
4.1 Approximation Error: ‖P⊥Φ V π‖2S,2 
Given a reward vector rπ ∈ RS , the value function V π ∈ RS is given by V π = Ψπrπ. As demonstrated by Theorem 1, the first key quantity that appears in the generalization bound is the approximation error ‖P⊥FkV 
π‖2S,2. With the successor representation, we can write: 
‖P⊥FkV π‖2S,2 = ‖P⊥FkΨπrπ‖2S,2 = ‖F⊥k Σ⊥k (B⊥k )Trπ‖2S,2. 
Following the argument from Petrik (2007) for the specific case of proto-value functions (Mahadevan and Maggioni, 2007), the worst-case unit-norm reward vector rπ in this case approximately corresponds to the (k + 1)-th vector bk+1. This is because 
F⊥k Σ⊥k (B⊥k )Tbk+1 = fk+1σk+1, 
and the fact that σk+1 > σk+i, for all i > 1. To make the bound comparable for different k and MDPs, let us fix Rmax and write 
rπ = bk+1Rmax 
‖bk+1‖∞ . (2) 
In this case, since ‖fk+1‖22 = 1, we have that 
‖P⊥FkV π‖2S,2 6 
σ2 k+1R 
2 max 
S‖bk+1‖2∞ 6 σ2 
k+1R 2 max. 
The dependence on ‖bk+1‖∞ relates to the operator norm of Ψ from L2 to L∞, and illustrates how bk+1 is only approximately the worst-case reward vector. 
A frequent scenario in reinforcement learning occurs when the reward is nonzero in a single state. Suppose that the reward vector rπ is rπ = Rmaxei for some i ∈ {i, . . . , S}. Then we have that: 
‖P⊥FkV π‖2S,2 = 
R2 maxtr((Σ⊥k )2)‖(B⊥k )>ei‖22 
S 
6 σ2 k+1R 
2 maxdeff(B⊥k ) 
S . 
When the effective dimension of B⊥k is O(S−k), the approximation error may be a factor S−k 
S smaller than the error for the worst-case reward vector (Equation (2) ). 
These arguments show that the generalization quality of a given family of representations can be partially quantified in terms of its spectrum (σi) 
S i=1. When the tran-
sition matrix is symmetric, we can bound the spectrum (σi) 
S i=1 in terms of the effective horizon implied by the 
discount factor. This is given by the following lemma. 
Lemma 1. Let P ∈ R|S|×|S| be a symmetric row stochastic matrix, and let γ ∈ (0, 1). Let σ(·) denote the set of singular values of a matrix. We have that: 
σ((I − γP )−1) ⊆ [ 
1 1+γ , 
1 1−γ 
] .
On the Generalization of Representations in Reinforcement Learning 
Disconnected Fully connected 2d Torus Star Openroom 
1 50 100 150 200 250 300 350 400 Number of features 
10 
−1 
10 
0 
10 
1 
10 
2 
10 
3 
Si ng 
ul ar 
 v al 
ue s 
1 50 100 150 200 250 300 350 400 Number of features 
0 
100 
200 
300 
400 
Ef fe 
ct iv 
e di 
m en 
si on 
1 20 40 60 80 100 120 Number of features 
10 
0 
10 
1 
Em pi 
ric al 
 e xc 
es s 
ris k 
1 20 40 60 80 100 120 Number of features 
0 
1 
2 
3 
Th eo 
re tic 
al  e 
xc es 
s ris 
k 
Figure 2: Top left: Singular values of the successor representation Ψπ, in decreasing order and for different graphical structures (the fully connected and star graphs’ spectra overlap). Top right: Effective dimension of the representation Φk = Fk. Bottom left and right: Median empirical excess risk over 10 runs, with 95% CIs as shaded regions, and theoretical excess risk, respectively, for the open room, torus, and fully connected graphs. 
Because the value function is generally of magnitude Vmax = Rmax 
1−γ , an approximation error of order 1 1+γ 
is quite small, suggesting that the corresponding basis functions may be safely omitted from the representation. 
Intuitively (and as supported by the analysis above), choosing a representation with a larger number of features k reduces the approximation error. However, as will see in the next section, a larger k necessarily increases the effective dimension, often in a manner that is superlinear in k. 
4.2 Effect of Transition Structure 
We next study characteristics of families of representations induced by the SVD of the successor representation for different environment transition structures. To this end, we consider different types of graphs over which we define a uniform random walk; the resulting representations are specifically proto-value functions (PVF, Mahadevan and Maggioni, 2007). We consider the two key quantities identified above: the spectrum of the representation, which informs us on the profile of the approximation error ‖P>FkV 
π‖2S,2 for different Fk, and the effective dimension of Fk as a function of k. 
We consider five graphical structures, each with S = 400 states (illustrations of these structures as well as results for additional structures are given in the appendix): a fully-connected graph, Baird’s star graph (Baird, 1995), a disconnected graph (on which each node self-transitions), a 20 × 20 grid, and a 20 × 20 torus. The torus has the same “shape” as the grid but allows transitions from one edge to its opposite, while the fully-connected graph is similar to the star graph in that both mix quickly. These graph were chosen to illustrate the diversity in generalization profiles arising from different transition structures. In all cases, γ = 0.99. 
Figure 2, top left illustrates three types of spectra. The fully-connected and star structures have a flat spectrum, both with an important first component but with a last component that is much smaller in the case of the star structure (see Appendix B for a closed-form description of the spectrum of the star graph). By contrast, the grid and torus exhibit a decaying spectrum, suggesting that attaining a low approximation error may require many features. As expected, the disconnected graph produces a flat spectrum with values σi = (1− γ)−1. 
Figure 2, top right shows the effective dimension as a function of the number of features k, and paints a relatively different picture. Here, both star and fully-
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
0.00 0.02 0.04 Approximation error 
10 
−2 
10 
−1 
10 
0 
Em pi 
ric al 
 e xc 
es s 
ris k 
0.00 0.02 0.04 Approximation error 
0 
50 
100 
Ef fe 
ct iv 
e D 
im en 
si on 
SR Random Features Krylov Basis Bisimulation 
Figure 3: The four-room domain (Left). Median empirical excess risk (Middle) and effective dimension (Right) as a function of approximation error for the top k left singular vectors of the SR, random features, the Krylov basis and the bisimulation metric matrix in the four-room domain. 
connected graphs exhibit a high effective dimension, despite having relatively simple structure. This is because effective dimension reflects in some sense the degree to which a single sample might give misleading information about the value at other states. Because the first singular vectors capture most of the symmetry in these graphs, additional features must in some sense be misleading. On the other hand, the open room and torus, despite an almost-identical spectrum, exhibit notedly different profiles: while the torus achieves the lower bound deff(Fk) ≈ k, the grid results in generally poor features for k large. 
To understand the consequences of these characteristic differences, we performed least-squares regression to estimate value functions in three of these structures (fully-connected, grid, and torus). In all cases, we sampled a reward function by assigning rewards to each state-action pair from a normal distribution (see Appendix C). We then sampled n = 300 states with replacement and performed a Monte Carlo rollout to obtain the sample return (yi) 
n i=1. We measured the 
excess risk of the linear approximation found by the least-squares procedure. For each graph structure, we repeated the experiment 10 times. 
Figure 2, bottom depicts the outcome of this experiment. Experimentally, the PVF of the torus generalizes significantly better than the PVF of the grid (left panel). This is reflected in a heuristic calculation of the theoretical bound (right panel), given more explicitly by the formula 
‖P⊥FkV π‖2S,2 + 
deff(Fk) 
n + deff(F ) 
n2 ‖P⊥FkV 
π‖2∞. 
The number of features k minimizing the empirical and theoretical excess risk differ, but follow the same qualitative pattern: for small k, the open room PVF generalizes poorly, while the minimum is achieved in the fully-connected graph by k = 1, highlighting again 
its high degree of symmetry. 
4.3 Analysis of the One-dimensional Torus 
As evidenced by the experiments of the previous section, the proto-value functions of the two-dimensional torus have particularly appealing generalization characteristics. Analytically, similarly good generalization can be demonstrated on the one-dimensional torus, as we now show. 
The one-dimensional torus consists in S states arranged on a chain, such that si connects to si−1, si+1 mod S. As such, the random walk on this torus induces a transition function Pπ described by a circulant matrix. Since Pπ is symmetric, we may write2 
(I − γPπ)−1 = USΣU∗S . 
Following Gray (2006), the k-th singular value of (I − γPπ)−1 is given by 
σk = 1 
1− γ cos( 2π S d 
k−1 2 e) 
for k = 1, ..., S.3 Additionally, we have that US = 1√ S F ∗S , with (FS)j,k = exp(−2πijk/S) the discrete 
Fourier transform matrix in dimension S. From this we deduce that each entry of US has modulus 1/ 
√ S, 
and therefore any orthogonal matrix formed from any k distinct columns of US will have coherence 1 and effective dimension k. This shows that the proto-value functions of the one-dimensional torus give in some sense an ideal state representation.
On the Generalization of Representations in Reinforcement Learning 
DQN(Adam) Rainbow DQN(Nature) IQN M-IQN 
0 50 100 150 200 Number of Frames (in millions) 
0.2 
0.4 
0.6 
0.8 
1.0 Ef 
fe ct 
iv e 
D im 
en si 
on  / 
N  
 (I nt 
er qu 
ar til 
e M 
ea n) 
0 50 100 150 200 Number of Frames (in millions) 
0.0 
0.5 
1.0 
1.5 
2.0 
IQ M 
 H um 
an  N 
or m 
al ize 
d Sc 
or e 
Figure 4: Left: Interquartile mean (IQM) (Agarwal et al., 2021b) for the effective dimension, normalized by the batch size used N = 215. Right: for human-normalized scores over the course of training across 60 Atari games. IQM measures the mean on the middle 50% of the data points combined across all runs and games. These statistics are over 5 independent runs and shading gives 95% stratified bootstrap confidence intervals based on Rliable (Agarwal et al., 2021b). 
5 EXPERIMENTS 
5.1 Comparing State Representations 
We now compare the Successor Representation to other theoretically-motivated representations: the bisimulation metric matrix (Ferns et al., 2004), the Krylov basis (Petrik, 2007) and some random features, in terms of effective dimension and excess risk, in the setting of Section 4.2. Figure 3 shows some of these results on the four room domain (Sutton et al., 1999; Solway et al., 2014). These give further weight to the idea that effective dimension plays an important role in determining the usefulness of a representation, as for a given approximation error better effective dimension corresponds to better excess risk. 
The SR of the four-room domain is fairly well-studied and have been shown to give rise to effective representations (Machado et al., 2017; Bellemare et al., 2019).It generalizes well but has worse approximation error compared to the Krylov basis or the Bisimulation metric which take into account the reward. For small approximation errors, the krylov basis has smaller effective dimension and is performing best. Finally, random features which are agnostic to the structure of the MDP have very high approximation error making them unappealing. 
2We ignore the issue of real diagonalizable versus complex diagonalizable. 
3The spectrum of the torus is briefly mentioned in Blier et al. (2021). 
5.2 Deep Reinforcement Learning 
We conclude with an empirical evaluation demonstrating the usefulness of our results in characterizing generalization in a larger setting. Specifically, we measure the effective dimensions of a representation φ implied by a deep neural network. We consider the hidden layer of 512 rectified linear units learnt by five deep RL agents, namely DQN (Mnih et al., 2015), DQN with Adam optimizer, Rainbow (Hessel et al., 2018), IQN (Dabney et al., 2018), and Munchausen-IQN (M-IQN) (Vieillard et al., 2020). We are interested in how the notion of effective dimension explains the relative performance of these deep RL agents aggregated across 60 Atari 2600 games (Bellemare et al., 2013) and at different points in training until 200M environment frames (Castro et al., 2018). 
We compare estimates of the effective dimension of these representations throughout training and reported results in Figure 4 (Left) (see per game comparison in Appendix C.2). When computing such estimates, we use a large batch size (=215), sampled uniformly from the offline Atari-replay datasets (Agarwal et al., 2020), as a proxy for the ambient dimension S used in the definition of the effective dimension. 
We observe that higher performance on a game typically correlates with lower effective dimension. The relative ordering of effective dimension (Figure 4, left) matches the performance ranking of different agents(Figure 4, right). Furthermore, we can notice a rise in the effective dimension from iteration 50 which suggests an overfitting of the representation to the current value function, in line with the evidence of
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
IQN IQN + Feature Reg. 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0.2 
0.4 
0.6 
0.8 
1.0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
  (I 
nt er 
qu ar 
til e 
M ea 
n) 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0.0 
0.2 
0.4 
0.6 
N or 
m al 
iz ed 
 S co 
re  
 (I nt 
er qu 
ar til 
e M 
ea n) 
Figure 5: Effective dimension, normalized by the batch size N = 215 and performance of IQN and IQN with feature regularization Lφ on 17 Atari games in the offline RL setting. 
late-training overfitting found by Dabney et al. (2020). 
To further corroborate that low effective dimension corresponds to better generalization, we investigate whether optimizing an auxiliary loss Lφ, motivated by the idea of reducing the effective dimension of the learned representation, improves performance. To do so, we use Lφ = log 
∑ i exp(‖φ(si)‖22) for states si in a 
randomly sampled mini-batch of size 32. To avoid confounding effects from exploration, we study the offline RL setting (Levine et al., 2020). Specifically, we use the 5% Atari-replay dataset (Agarwal et al., 2020) on 17 games and evaluate IQN, one of the top performing agents on the offline Atari dataset (Gulcehre et al., 2020). As shown in Figure 5, right, combining IQN with the loss Lφ results in significantly higher average returns compared to IQN on all 17 games. We also compare estimates of the effective dimension of the representations induced by these two agents in Fig-ure 5, left, and find the auxiliary loss Lφ results in lower effective dimension during the first 80 iterations. Surprisingly, we also notice that IQN with feature regularization prevents the substantial loss in rank of the feature matrix observed previously by Kumar et al. (2021, 2022) (see Figure 13 and Figure 12), making it hard to disentangle between approximation and estimation error effects. Further study of this phenomenon would be an interesting direction for future work. 
6 CONCLUSION 
In this paper we provided a theoretical characterisation of how a given representation affects generalization in reinforcement learning. While we focused here on the batch Monte Carlo setting for simplicity, a similar but more involved analysis can in theory also be performed to analyze algorithms such as LSTD. 
Providing fresh evidence regarding the benefits of suc-
cessor representations in shaping an agent’s representation, both our analysis and experiments on synthetic environments demonstrate that indeed, the left-singular vectors of SRs generally provide good generalization. While natural given the successor representation’s close relationship with the value function, one surprising result is that the effective dimension of such a representation is relatively sensitive to the particular transition structure, as illustrated by the differences between the torus and open room representations. In addition, the effective dimension of this representation does not immediately correlate with mixing time, as one might have expected. These findings suggests that it should be possible to devise algorithms inspired by the same principles, but that work well across a variety of transition structures, for example by leveraging contrastive graph representations (Madjiheurem and Toni, 2019). 
Our analysis of Atari 2600-playing agents gives further evidence of the important role played by the representation in deep reinforcement learning. While not a surprise in itself, we find a strong correlation between effective dimension and performance, this suggests that generalization is key to explaining many performance improvements. In particular, it is by now well-understood that auxiliary tasks (Jaderberg et al., 2017; Bellemare et al., 2017) shape the learned representation of the agent, and under ideal conditions cause it to match the SVD of an auxiliary task matrix (Bellemare et al., 2019; Lyle et al., 2021). Controlling the bound of Theorem 1 by means of such tasks or deep learning mechanisms such as hindsight experience replay (Andrychowicz et al., 2017) may provide further performance improvements. Our results also suggest that it may be possible to derive theoretical guarantees regarding transfer between policies or MDPs (Taylor and Stone, 2009), in particular with a learned representation (Agarwal et al., 2021a).
On the Generalization of Representations in Reinforcement Learning 
Acknowledgements 
The authors would like to thank Matthieu Geist, Mark Rowland, Pablo Samuel Castro, Ahmed Touati, Marlos Machado, Dale Schuurmans, Robert Dadashi, Tomas Vaskevicius, Olivier Pietquin, Martha White, Hanie Sedghi, Damien Vincent, Dominic Richards, Nino Vieil-lard, Leonard Hussenot, Amartya Sanyal, Sephora Mad-jiheurem, Laura Toni and the anonymous reviewers for useful discussions and feedback on this paper. 
We would also like to thank the Python community (Van Rossum and Drake Jr, 1995; Oliphant, 2007) for developing tools that enabled this work, including NumPy (Oliphant, 2006; Walt et al., 2011; Harris et al., 2020), SciPy (Jones et al., 2001), Matplotlib (Hunter, 2007) and JAX (Bradbury et al., 2018). 
References 
Rishabh Agarwal, Dale Schuurmans, and Mohammad Norouzi. An optimistic perspective on offline reinforcement learning. In International Conference on Machine Learning, pages 104–114. PMLR, 2020. 
Rishabh Agarwal, Marlos C. Machado, Pablo Samuel Castro, and Marc G Bellemare. Contrastive behavioral similarity embeddings for generalization in reinforcement learning. In International Conference on Learning Representations, 2021a. 
Rishabh Agarwal, Max Schwarzer, Pablo Samuel Cas-tro, Aaron Courville, and Marc G Bellemare. Deep reinforcement learning at the edge of the statistical precipice. Advances in Neural Information Process-ing Systems, 2021b. 
Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob Mc-Grew, Josh Tobin, Pieter Abbeel, and Wojciech Zaremba. Hindsight experience replay. arXiv preprint arXiv:1707.01495, 2017. 
Leemon Baird. Residual algorithms: Reinforcement learning with function approximation. In Machine Learning Proceedings 1995, pages 30–37. Elsevier, 1995. 
Bahram Behzadian and Marek Petrik. Low-rank feature selection for reinforcement learning. In ISAIM, 2018. 
Marc Bellemare, Will Dabney, Robert Dadashi, Adrien Ali Taiga, Pablo Samuel Castro, Nicolas Le Roux, Dale Schuurmans, Tor Lattimore, and Clare Lyle. A geometric perspective on optimal representations for reinforcement learning. Advances in neural information processing systems, 32:4358–4369, 2019. 
Marc G Bellemare, Yavar Naddaf, Joel Veness, and Michael Bowling. The arcade learning environment: An evaluation platform for general agents. Journal of Artificial Intelligence Research, 47:253–279, 2013. 
Marc G. Bellemare, Will Dabney, and Rémi Munos. A distributional perspective on reinforcement learning. In Proceedings of the International Conference on Machine Learning, 2017. 
Léonard Blier, Corentin Tallec, and Yann Ollivier. Learning successor states and goal-dependent values: A mathematical viewpoint. arXiv preprint arXiv:2101.07123, 2021. 
James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal Maclaurin, and Skye Wanderman-Milne. Jax: composable transformations of python+ numpy programs. URL http://github. com/google/jax, 2018. 
Pierre Brémaud. Markov chains: Gibbs fields, Monte Carlo simulation, and queues, volume 31. Springer Science & Business Media, 2013. 
Emmanuel J Candès and Benjamin Recht. Exact matrix completion via convex optimization. Foundations of Computational mathematics, 9(6):717–772, 2009. 
Pablo S. Castro, Subhodeep Moitra, Carles Gelada, Saurabh Kumar, and Marc G. Bellemare. Dopamine: A research framework for deep reinforcement learning. arXiv, 2018. 
Wesley Chung, Somjit Nath, Ajin Joseph, and Martha White. Two-timescale networks for nonlinear value function approximation. In International conference on learning representations, 2018. 
Will Dabney, Georg Ostrovski, David Silver, and Rémi Munos. Implicit quantile networks for distributional reinforcement learning. In International conference on machine learning, pages 1096–1105. PMLR, 2018. 
Will Dabney, André Barreto, Mark Rowland, Robert Dadashi, John Quan, Marc G Bellemare, and David Silver. The value-improvement path: Towards better representations for reinforcement learning. arXiv preprint arXiv:2006.02243, 2020. 
Peter Dayan. Improving generalization for temporal difference learning: The successor representation. Neural Computation, 5(4):613–624, 1993. 
Dibya Ghosh and Marc G Bellemare. Representations for stable off-policy reinforcement learning. In In-ternational Conference on Machine Learning, pages 3556–3565. PMLR, 2020. 
Robert M. Gray. Toeplitz and circulant matrices: A review. 2006. 
Charles Miller Grinstead and James Laurie Snell. In-troduction to probability. American Mathematical Soc., 2012. 
Caglar Gulcehre, Ziyu Wang, Alexander Novikov, Thomas Paine, Sergio Gómez, Konrad Zolna, Rishabh Agarwal, Josh S Merel, Daniel J Mankowitz,
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
Cosmin Paduraru, et al. Rl unplugged: A collection of benchmarks for offline reinforcement learning. Ad-vances in Neural Information Processing Systems, 33, 2020. 
Charles R Harris, K Jarrod Millman, Stéfan J van der Walt, Ralf Gommers, Pauli Virtanen, David Cour-napeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J Smith, et al. Array programming with numpy. Nature, 585(7825):357–362, 2020. 
Matteo Hessel, Joseph Modayil, Hado van Hasselt, Tom Schaul, Georg Ostrovski, Will Dabney, Dan Horgan, Bilal Piot, Mohammad Azar, and David Silver. Rainbow: Combining improvements in deep reinforcement learning. In Proceedings of the AAAI Conference on Artificial Intelligence, 2018. 
Daniel Hsu, Sham Kakade, and Tong Zhang. A tail inequality for quadratic forms of subgaussian random vectors. Electronic Communications in Probability, 17:1–6, 2012a. 
Daniel Hsu, Sham M Kakade, and Tong Zhang. Ran-dom design analysis of ridge regression. In Confer-ence on learning theory, pages 9–1. JMLR Workshop and Conference Proceedings, 2012b. 
John D Hunter. Matplotlib: A 2d graphics environment. Computing in science & engineering, 9(3): 90–95, 2007. 
Max Jaderberg, Volodymyr Mnih, Wojciech M. Czar-necki, Tom Schaul, Joel Z Leibo, David Silver, and Koray Kavukcuoglu. Reinforcement learning with unsupervised auxiliary tasks. In Proceedings of the International Conference on Learning Representa-tions, 2017. 
Eric Jones, Travis Oliphant, Pearu Peterson, et al. Scipy: Open source scientific tools for python. 2001. 
John G Kemeny and J Laurie Snell. Finite continuous time markov chains. Theory of Probability & Its Applications, 6(1):101–105, 1961. 
George D. Konidaris, Sarah Osentoski, and Philip S. Thomas. Value function approximation in reinforcement learning using the fourier basis. In Proceed-ings of the 25th Conference on Artificial Intelligence, 2011. 
Aviral Kumar, Rishabh Agarwal, Dibya Ghosh, and Sergey Levine. Implicit under-parameterization inhibits data-efficient deep reinforcement learning. In International Conference on Learning Representa-tions, 2021. 
Aviral Kumar, Rishabh Agarwal, Tengyu Ma, Aaron Courville, George Tucker, and Sergey Levine. Dr3: Value-based deep reinforcement learning requires explicit regularization. 2022. 
Nir Levine, Tom Zahavy, Daniel Mankowitz, Aviv Tamar, and Shie Mannor. Shallow updates for deep reinforcement learning. In Advances in Neural Infor-mation Processing Systems, 2017. 
Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu. Offline reinforcement learning: Tutorial, review, and perspectives on open problems. arXiv preprint arXiv:2005.01643, 2020. 
Clare Lyle, Mark Rowland, Georg Ostrovski, and Will Dabney. On the effect of auxiliary tasks on representation dynamics. In International Conference on Artificial Intelligence and Statistics, pages 1–9. PMLR, 2021. 
M.C. Machado, M.G. Bellemare, and M. Bowling. A Laplacian framework for option discovery in reinforcement learning. In Proceedings of the International Conference on Machine Learning, 2017. 
Sephora Madjiheurem and Laura Toni. Representation learning on graphs: A reinforcement learning application. In Proceedings of the International Conference on Machine Learning, 2019. 
Sridhar Mahadevan and Mauro Maggioni. Proto-value functions: A laplacian framework for learning representation and control in markov decision processes. Journal of Machine Learning Research, 8(10), 2007. 
Odalric-Ambrym Maillard and Rémi Munos. Com-pressed least-squares regression. In NIPS 2009, 2009. 
Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Veness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidje-land, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dhar-shan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level control through deep reinforcement learning. Nature, 518(7540):529–533, 2015. 
Mehryar Mohri, Afshin Rostamizadeh, and Ameet Tal-walkar. Foundations of machine learning. MIT press, 2018. 
Travis E Oliphant. A guide to NumPy, volume 1. Trelgol Publishing USA, 2006. 
Travis E Oliphant. Python for scientific computing. Computing in Science & Engineering, 9(3):10–20, 2007. 
Ronald Parr, Lihong Li, Gavin Taylor, Christopher Painter-Wakefield, and Michael L Littman. An analysis of linear models, linear value-function approximation, and feature selection for reinforcement learning. In Proceedings of the 25th international conference on Machine learning, pages 752–759, 2008.
On the Generalization of Representations in Reinforcement Learning 
Marek Petrik. An analysis of laplacian methods for value function approximation in mdps. In IJCAI, pages 2574–2579, 2007. 
Martin L Puterman. Markov decision processes: Dis-crete stochastic dynamic programming. 1994. 
Bohdana Ratitch and Doina Precup. Sparse distributed memories for on-line value-based reinforcement learning. In Proceedings of the 15th European Conference on Machine Learning, 2004. 
Alec Solway, Carlos Diuk, Natalia Córdova, Debbie Yee, Andrew G Barto, Yael Niv, and Matthew M Botvinick. Optimal behavioral hierarchy. PLoS Com-putational Biology, 10(8):e1003779, aug 2014. 
Kimberly L. Stachenfeld, Matthew Botvinick, and Samuel J. Gershman. Design principles of the hippocampal cognitive map. In Advances in Neural Information Processing Systems, 2014. 
Richard S Sutton. Generalization in reinforcement learning: Successful examples using sparse coarse coding. Advances in neural information processing systems, pages 1038–1044, 1996. 
Richard S. Sutton and Andrew G. Barto. Reinforcement learning: An introduction. MIT Press, 2nd edition, 2018. 
R.S. Sutton, D. Precup, and S. Singh. Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning. Artificial Intelligence, 112:181–211, 1999. 
Matthew E. Taylor and Peter Stone. Transfer learning for reinforcement learning domains: A survey. Jour-nal of Machine Learning Research, 10(1):1633–1685, 2009. 
Joel A. Tropp. An introduction to matrix concentration inequalities. Foundations and Trends in Machine Learning, 8, 2015. 
Guido Van Rossum and Fred L Drake Jr. Python reference manual. Centrum voor Wiskunde en Informatica Amsterdam, 1995. 
Vladimir N Vapnik. The nature of statistical learning. Theory, 1995. 
Roman Vershynin. Introduction to the non-asymptotic analysis of random matrices. arXiv preprint arXiv:1011.3027, 2010. 
Nino Vieillard, Olivier Pietquin, and Matthieu Geist. Munchausen reinforcement learning. arXiv preprint arXiv:2007.14430, 2020. 
Stéfan van der Walt, S Chris Colbert, and Gael Varo-quaux. The numpy array: a structure for efficient numerical computation. Computing in science & engineering, 13(2):22–30, 2011.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
On the Generalization of Representations in Reinforcement Learning: Appendices 
A PROOFS FOR SECTION 3 
This section is dedicated to proving the main theorem on the paper, Theorem 1. Before that, we introduce and prove a more general result from which Theorem 1 can be deduced as a corollary. 
Let s1, ..., sn denote iid draws from an arbitrary distribution ν ∈ P(S) and (ei) S i=1 ⊂ RS the standard basis. 
Assumption 1. We assume that ν(s) > 0 for all state state s ∈ {1, ..., S}. 
Let N := Ei∼ν [eie T i ], and let ‖x‖ν,2 := ‖N1/2x‖2 for x ∈ RS . Put ν := mini=1,...,S νi > 0. Let w∗ := 
(ΦTNΦ)−1ΦTNV , and also define Ξ := ΦTNΦ. Ξ is the steady-state feature covariance matrix. w∗ represents the best k-dimensional model. Since we assume that ν > 0, we have that Ξ is positive definite. 
The excess risk E(Vφ,w) of a hypothesis Vφ,w : S → R is defined as: 
E(Vφ,w) := Esi∼ν(Vφ,w(si)− V (si)) 2. 
For any ŵ ∈ Rk, we have the decomposition: 
E(Vφ,ŵ) = ‖Φŵ − V ‖2ν,2 = ‖Φ(ŵ − w∗)‖2ν,2 + ‖Φw∗ − V ‖2ν,2. 
Note we have the identity: 
‖Φw∗ − V ‖2ν,2 = ‖P⊥N1/2ΦN 1/2V ‖22. 
Theorem 2. Fix any δ ∈ (0, 1). Suppose that n > 8deff(Φ) log(6k/δ). Under Assumption 1, with probability at least 1− δ, the empirical risk minimizer Vφ,ŵ satisfies: 
E(Vφ,ŵ) = ‖P⊥N1/2ΦN 1/2V ‖22 + 384 
deff(Φ) 
νnS ‖P⊥N1/2ΦN 
1/2V ‖22 log(3/δ) 
+ 48 σ2 
n [2k + 3 log(3/δ)] + 
64 
3 
deff(Φ) 
νn2S ‖N−1/2P⊥N1/2ΦN 
1/2V ‖2∞ log2(3/δ). 
where ‖·‖∞ denotes the usual supremum norm. 
Proof. The empirical risk minimizer ŵ ∈ Rk is defined as the random vector ŵ = (EnΦ)†Y . Next, we write: 
N1/2Φ(ŵ − w∗) = N1/2Φ(EnΦ)†(EnV + η)−N1/2Φw∗ 
Therefore, assuming EnΦ has full column rank (which will be the case by Lemma 2), 
N1/2Φ(EnΦ)†EnV −N1/2Φw∗ 
= N1/2Φ(EnΦ)†EnV − PN1/2ΦN 1/2V 
= N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nEnV − PN1/2ΦN 1/2V 
= N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nEnN −1/2(PN1/2Φ + P⊥N1/2Φ)N1/2V − PN1/2ΦN 
1/2V 
= N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nEnN −1/2P⊥N1/2ΦN 
1/2V 
+N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nEnN −1/2PN1/2ΦN 
1/2V − PN1/2ΦN 1/2V 
= N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nEnN −1/2P⊥N1/2ΦN 
1/2V 
= N1/2ΦΞ−1/2(Ξ−1/2ΦTET nEnΦΞ−1/2)−1Ξ−1/2ΦTET 
nEnN −1/2P⊥N1/2ΦN 
1/2V.
On the Generalization of Representations in Reinforcement Learning 
Similarly, 
N1/2Φ(EnΦ)†η = N1/2Φ(ΦTET nEnΦ)−1ΦTET 
nη 
= N1/2ΦΞ−1/2(Ξ−1/2ΦTET nEnΦΞ−1/2)−1Ξ−1/2ΦTET 
nη. 
We first claim that ‖N1/2ΦΞ−1/2‖op 6 1. To see this, observe that: 
‖N1/2ΦΞ−1/2‖2op = λmax(N1/2Φ(ΦTNΦ)−1ΦTN1/2) = λmax(PN1/2Φ) 6 1. 
Hence: 
‖N1/2Φ(EnΦ)†EnV −N1/2Φw∗‖2 6 ‖Ξ−1/2ΦTET 
nEnN −1/2P⊥ 
N1/2Φ N1/2V ‖2 
λmin(Ξ−1/2ΦTET nEnΦΞ−1/2) 
, 
and similarly 
‖N1/2Φ(EnΦ)†η‖2 6 ‖Ξ−1/2ΦTET 
nη‖2 λmin(Ξ−1/2ΦTET 
nEnΦΞ−1/2) . 
Therefore, 
‖N1/2Φ(ŵ − w∗)‖2 6 1 
λmin(Ξ−1/2ΦTET nEnΦΞ−1/2) 
[‖Ξ−1/2ΦTET nEnN 
−1/2P⊥N1/2ΦN 1/2V ‖2 + ‖Ξ−1/2ΦTET 
nη‖2] 
By Lemma 2, as long as n > 8deff (Φ) νS log(6k/δ), then with probability at least 1− δ/3, 
n 
2 Ik 4 Ξ−1/2ΦTET 
nEnΦΞ−1/2 4 4nIk. 
Furthermore, by Lemma 3, with probability at least 1− δ/3, 
‖Ξ−1/2ΦTET nEnN 
−1/2P⊥N1/2ΦN 1/2V ‖2 
6 2 
√ 8ndeff(Φ) 
νS ‖P⊥ 
N1/2Φ N1/2V ‖22 log 
( 3 
δ 
) + 
4 
3 
√ deff(Φ) 
νS ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞ log 
( 3 
δ 
) . 
Finally, by Lemma 4, with probability at least 1− δ/3, 
1 { 
Ξ−1/2ΦTET nEnΦΞ−1/2 4 4nIk 
} · ‖Ξ−1/2ΦTET 
nη‖2 6 √ σ2n[8k + 12 log(3/δ)]. 
Therefore, by a union bound, with probability at least 1− δ, 
‖N1/2Φ(ŵ − w∗)‖2 6 2 
n 
[ 2 
√ 8ndeff(Φ) 
νS ‖P⊥ 
N1/2Φ N1/2V ‖22 log 
( 3 
δ 
)] 
+ 2 
n 
[ 4 
3 
√ deff(Φ) 
νS ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞ log 
( 3 
δ 
)] + 
2 
n 
[√ σ2n[8k + 12 log(3/δ)] 
] = 4 √ 
8 
√ deff(Φ) 
νnS log(3/δ)‖P⊥N1/2ΦN 
1/2V ‖2 + 4 
√ σ2 
n [2k + 3 log(3/δ)] 
+ 8 
3 
√ deff (Φ) νS 
n ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞ log 
( 3 
δ 
) . 
Now, from the inequality (a+ b+ c)2 6 3 ( a2 + b2 + c2 
) for any a, b, c ∈ R, it follows that 
E(Vφ,ŵ) = ‖P⊥N1/2ΦN 1/2V ‖22 + 384 
deff(Φ) 
νnS ‖P⊥N1/2ΦN 
1/2V ‖22 log(3/δ) 
+ 48 σ2 
n [2k + 3 log(3/δ)] + 
64 
3 
deff(Φ) 
νn2S ‖N−1/2P⊥N1/2ΦN 
1/2V ‖2∞ log2(3/δ).
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
Lemma 2. Let Φ ∈ RS×k. Let ν denote a distribution over {1, ..., S} satisfying Assumption 1 and (ei) S i=1 ⊂ RS 
the standard basis. Let s1, ..., sn denote iid draws from ν. Define Yn ∈ Rk×k as: 
Yn = 
n∑ i=1 
Ξ−1/2ΦTesie T siΦΞ−1/2. 
Fix any δ ∈ (0, 1). As long as n > 8deff (Φ) νS log(2k/δ), with probability at least 1− δ, 
n 
2 Ik 4 Yn 4 4nIk. 
where for two symmetric matrices, A 4 B means that the matrice B −A is positive semi-definite. 
Proof. This is an application of the Matrix Chernoff inequality. First, we see that E[Yn] = nIk. Next, we have: 
max i=1,...,S 
λmax(Ξ−1/2ΦTeie T i ΦΞ−1/2) = max 
i=1,...,S ‖Ξ−1/2ΦTei‖22 
= max i=1,...,S 
‖(ΦTNΦ)−1/2ΦTei‖22 
6 1 
ν max 
i=1,...,S ‖PΦei‖22 
6 deff(Φ) 
νS . 
We now make two applications of the Matrix Chernoff inequality (see Theorem 5.1.1 in Tropp (2015)). Denoting e as Euler’s number, for the upper tail, we have that for any t > e, 
P(λmax(Yn) > tn) 6 k(e/t)tnνS/deff (Φ). 
Setting t = 4, we conclude that as long as n > 1 4 log(4/e) 
deff (Φ) νS log(2k/δ), then we have that with probability at 
least 1− δ/2, λmax(Yn) 6 4n. For the lower tail, we have that for any t ∈ (0, 1), 
P(λmin(Yn) 6 tn) 6 k exp 
( −(1− t)2n 
2 
νS 
deff(Φ) 
) . 
Setting t = 0.5, we see that as long as n > 8deff (Φ) νS log(2k/δ), then λmin(Yn) > n/2 with probability at least 
1− δ/2. Taking a union bound yields the claim. 
Lemma 3. Put zn := Ξ−1/2ΦTET nEnN 
−1/2P⊥ N1/2Φ 
N1/2V . Fix any δ ∈ (0, e−1/8). With probability at least 1− δ, 
‖zn‖2 6 2 
√ 8ndeff(Φ) 
νS ‖P⊥N1/2ΦN 
1/2V ‖2 √ 
log(1/δ) + 4 
3 
√ deff(Φ) 
νS ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞ log(1/δ). 
Proof. Define qi := Ξ−1/2ΦTesie T siN 
−1/2P⊥ N1/2Φ 
N1/2V . We have that E[qi] = 0. Next, 
E[‖qi‖22] = E[‖Ξ−1/2ΦTesi‖22〈esi , N−1/2P⊥N1/2ΦN 1/2V 〉2] 
6 deff(Φ) 
νS E[〈esi , N−1/2P⊥N1/2ΦN 
1/2V 〉2] 
= deff(Φ) 
νS ‖P⊥N1/2ΦN 
1/2V ‖22. 
Finally, we have the following almost sure bound: 
‖qi‖2 6 
√ deff(Φ) 
νS ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞.
On the Generalization of Representations in Reinforcement Learning 
Put zn := ∑n i=1 qi. By the vector Bernstein inequality, for all t > 0, 
P 
( ‖zn‖2 > 
√ ndeff(Φ) 
νS ‖P⊥ 
N1/2Φ N1/2V ‖22(1 + 
√ 8t) + 
4 
3 
√ deff(Φ) 
νS ‖N−1/2P⊥N1/2ΦN 
1/2V ‖∞t 
) 6 e−t. 
The claim now follows by setting t = log(1/δ). 
Lemma 4. Let G be the event: 
G := { 
Ξ−1/2ΦTET nEnΦΞ−1/2 4 4nIk 
} With probability at least 1− δ, we have: 
1{G} · ‖Ξ−1/2ΦTET nη‖22 6 σ2n[8k + 12 log(1/δ)]. 
Proof. Put M := 1{G} · EnΦΞ−1ΦTET n . Because η is assumed to be independent of En, we can condition on En 
and apply the Hanson-Wright inequality (Hsu et al., 2012a) to conclude that for any t > 0, 
P(ηTMη > σ2(tr(M) + 2 √ 
tr(M2)t+ 2‖M‖opt)) | En) 6 e−t. 
We now compute upper bounds on tr(M), tr(M2), and ‖M‖op. First, we have: 
tr(M) = 1{G} tr(EnΦΞ−1ΦTET n ) = 1{G} tr(Ξ−1/2ΦTET 
nEnΦΞ−1/2) 6 4nk. 
Next, 
tr(M2) = 1{G} tr(EnΦΞ−1ΦTET nEnΦΞ−1ΦTET 
n ) 
= 1{G} tr(Ξ−1/2ΦTET nEnΦΞ−1/2 · Ξ−1/2ΦTET 
nEnΦΞ−1/2) 
(a) 
6 1{G} tr(Ξ−1/2ΦTET nEnΞ−1/2Φ)‖Ξ−1/2ΦTET 
nEnΦΞ−1/2‖op 
6 4nk · 4n = 16n2k. 
Above, (a) follows from Hölder’s inequality. Finally, 
‖M‖op = 1{G}‖EnΦΞ−1ΦTET n‖op = 1{G}‖Ξ−1/2ΦTET 
nEnΦΞ−1/2‖op 6 4n. 
We now plug these bounds in along with the choice of t = log(1/δ), which tells us that conditioned on En, with probability at least 1− δ, 
ηTMη 6 σ2 [ 4nk + 8n 
√ k log(1/δ) + 8n log(1/δ) 
] 6 σ2 [8nk + 12n log(1/δ)] 
= σ2n [8k + 12 log(1/δ)] . 
We now remove the conditioning on En. Let t̄ := σ2n [8k + 12 log(1/δ)]. By the tower property, 
P(ηTMη > t̄) = E[1{ηTMη > t̄}] = E[E[1{ηTMη > t̄} | En]] = E[P(ηTMη > t̄ | En)] 6 E[δ] = δ. 
Theorem 1 is a corollary of Theorem 2 in the case where the distribution ν is uniform. 
Theorem 1 (Excess risk). Fix any δ ∈ (0, 1). Suppose that n > 8deff(Φ) log(6k/δ). With probability at least 1− δ, the empirical risk minimizer Vφ,ŵ satisfies: 
E(Vφ,ŵ) 6 ‖P⊥Φ V ‖2S,2 + 384c deff(Φ) 
n ‖P⊥Φ V ‖2S,2 
+ 48σ2 2k + 3c 
n + 
64 
3 
deff(Φ) 
n2 ‖P⊥Φ V ‖2∞c2, 
where c = log(3/δ) and ‖·‖∞ denotes the usual supremum norm. 
Proof. ν being uniform, we have ν = S. The result follows by plugging ν in Theorem 2.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
B PROOFS FOR SECTION 4 
Lemma 1. Let P ∈ R|S|×|S| be a symmetric row stochastic matrix, and let γ ∈ (0, 1). Let σ(·) denote the set of singular values of a matrix. We have that: 
σ((I − γP )−1) ⊆ [ 
1 1+γ , 
1 1−γ 
] . 
Proof. Let λ(·) denote the eigenvalues of a matrix. Because P is symmetric, we have that: 
σ((I − γP )−1) = 
{ 1 
1− γλ : λ ∈ λ(P ) 
} . 
Because P is a row stochastic matrix, we have that the spectral radius of P satisfies ρ(P ) = 1, and therefore λ(P ) ⊆ [−1, 1]. Hence: 
1 
1− γλ ∈ [1/(1 + γ), 1/(1− γ)]. 
Eigenstructure of the Star Graph (Subsection 4.2) 
A random walk on the Star graph induces a rank-two transition matrix Pπ ∈ RS . We may write Pπ = v1e T S + eSv 
T 
S−1 where v is an all-ones vector except on its last coordinate where it takes value 0 and eS a one-hot vector taking value 1 on its last coordinate. It is easy to prove by induction that 
 for any k > 1, P 2k π = vvT 
S−1 + eSe T S 
 for any k > 0, P 2k+1 π = Pπ 
From this, it follows that 
(I − γPπ)−1 = I + 
∞∑ t=1 
(γPπ)t 
= I + ∑ 2k>2 
γ2kP 2k π + 
∑ 2k+1>1 
γ2k+1(Pπ)2k+1 
= I + ∑ 2k>2 
γ2k( vvT 
S − 1 + eSe 
T S) + 
∑ 2k+1>1 
γ2k+1Pπ 
= I + γ2 
1− γ2 ( vvT 
S − 1 + eSe 
T S) + 
γ 
1− γ2 Pπ. 
Define η := γ 1−γ2 . The non-zero singular values of (I − γPπ)−1 are the square roots of the eigenvalues of 
A = (I − γPπ)−1 ( (I − γPπ)−1 
)T . We have 
A = (I − γPπ)−1 ( (I − γPπ)−1 
)T = ( I + γηP 2 
π + ηPπ ) ( I + γη(P 2 
π )T + ηPT π 
) = I +B, 
where B := avvT + beSe T S + c(eSv 
T + veTS) with a = 2ηγ+η2γ2 
S−1 + η2, b = 2ηγ + η2γ2 + η2 
S−1 and c = (η + η2γ) S S−1 . 
Moreover, if {λ1, ..., λk} are the eigenvalues of B then the eigenvalues of A are {1 + λ1, ..., 1 + λk}. 
Consider the basis {eS , v}. For any a1, a2, 
B(a1eS + a2v) = avvT(a1eS + a2v) + beSe T S(a1eS + a2v) + c(eSv 
T + veTS)(a1eS + a2v) 
= a1a〈v, eS〉v + a2a‖v‖22v + a1beS + a2b〈v, eS〉eS + c(a1〈v, eS〉eS + a1v + a2‖v‖22eS + a2〈v, eS〉v) 
= (a1b+ ca1〈v, eS〉+ a2b〈v, eS〉+ a2c‖v‖22)eS + (a1a〈v, eS〉+ ca1 + a2〈v, eS〉+ a2a‖v‖22)v.
On the Generalization of Representations in Reinforcement Learning 
Since ‖v‖22 = S − 1 and 〈v, eS〉 = 0, B has the representation in {eS , v} as:[ b c(S − 1) c a(S − 1) 
] = 
[ 2ηγ + η2γ2 + η2 
S−1 (η + η2γ)S 
(η + η2γ) S S−1 2ηγ + η2γ2 + η2(S − 1) 
] = 
[ η2 
S−1 (η + η2γ)S 
(η + η2γ) S S−1 η2(S − 1) 
] + (2ηγ + η2γ2)I 
= C + (2ηγ + η2γ2)I 
Hence, the eigenvalues of C are given by 1 2 
( η2 ( 
(S − 1) + 1 S−1 
) ± √ η4 ( 
(S − 1) + 1 S−1 
)2 
+ 4(η + η2γ)2 S2 
S−1 − 4η4 
) . 
The non-zero singular values of (I − γPπ)−1 are thus 1 with multiplicity S − 2 and√√√√√1 
2 
η2 
( (S − 1) + 
1 
S − 1 
) ± 
√ η4 
( (S − 1) + 
1 
S − 1 
)2 
+ 4(η + η2γ)2 S2 
S − 1 − 4η4 
+ 2ηγ + η2γ2 + 1 
For γ = 0.99 and S = 400, we can check numerically that the two extreme singular values are equal to 996 and 0.05 respectively which matches the spectrum obtained for the Star graph in Figure 2. 
C EMPIRICAL EVALUATION: ADDITIONAL DETAILS 
C.1 Graphical Structures 
In this section, we study the generalization characteristics of the representations induced by the SVD of the successor representation for several environment transition structures. We illustrate the different graphs over which we define a random walk, studied in Subsection 4.2 as well as some new ones, in Figure 6. 
Our experiment consists in evaluating the value function on these different transition structures when S = 400 states. We consider three different reward vectors rπ ∈ RS : the all ones vector, the one-hot feature vector eS , and a vector whose entries are drawn from zero-mean Gaussian distribution and normalized such that ‖rπ‖∞ = 1. We then sampled a dataset D of n = 300 pairs (si, yi) where we performed a Monte Carlo rollout to obtain the returns (yi) 
n i=1. The targets are the value functions induced by the random walk. 
We are interested in comparing our generalization bound to the empirical excess risk on these domains. Our bound looks at the regime n > deff(Fk). We choose k 6 n 
2 as an heuristic way of achieving this. We report in Figure 7 the approximation error (Figure 7 Left), the empirical excess risk (Figure 7 Middle) and the theoretical excess risk (Figure 7 Right) obtained when using the representation φ = Fk on these different graph structures. 
Star: Baird’s star graph (Baird, 1995) consists in S − 1 states which are the star corners and a state S which is the star center. A random walk on this star graph induces a transition function such that all star corners 
Figure 6: Top: Different graphical structures with S = 5 states from left to right, Star, Chain, Torus1d, Disconnected, Fullyconnected. Bottom: Two-dimensional graphical structures with S = 9 states: from left to right, Openroom and Torus2d.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
1 50 100 150 200 250 300 350 
Number of features 
0.00 
0.02 
0.04 
0.06 
0.08 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=StarMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−3 
10−2 
10−1 
100 
101 
102 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=StarMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
1.2 
1.4 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=StarMDP, gamma=0.99 
all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0 
10 
20 
30 
40 
50 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=Torus1dMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−3 
10−1 
101 
103 
105 
107 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=Torus1dMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0 
10 
20 
30 
40 
50 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=Torus1dMDP, gamma=0.99 all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
1.2 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=Torus2dMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−4 
10−3 
10−2 
10−1 
100 
101 
Em pi 
ric al 
 e xc 
es s r 
isk n=300, S=400, MDP=Torus2dMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
1.2 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=Torus2dMDP, gamma=0.99 all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0 
10 
20 
30 
40 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=ChainMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−3 
10−1 
101 
103 
105 
107 
109 
1011 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=ChainMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0 
10 
20 
30 
40 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=ChainMDP, gamma=0.99 all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0 
500 
1000 
1500 
2000 
2500 
3000 
3500 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=openroom, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−1 
100 
101 
102 
103 
104 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=openroom, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0 
500 
1000 
1500 
2000 
2500 
3000 
3500 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=openroom, gamma=0.99 all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0 
2000 
4000 
6000 
8000 
10000 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=DisconnectedMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
104 
108 
1012 
1016 
1020 
1024 
1028 
1032 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=DisconnectedMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0 
2000 
4000 
6000 
8000 
10000 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=DisconnectedMDP, gamma=0.99 
all_ones one_hot gaussian 
1 50 100 150 200 250 300 350 
Number of features 
0.00 
0.02 
0.04 
0.06 
0.08 
Ap pr 
ox im 
at io 
n er 
ro r 
S=400, MDP=FullyConnectedMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
10−2 
10−1 
100 
Em pi 
ric al 
 e xc 
es s r 
isk 
n=300, S=400, MDP=FullyConnectedMDP, gamma=0.99 
1 20 40 60 80 100 120 140 
Number of features 
0.0 
0.2 
0.4 
0.6 
0.8 
1.0 
1.2 
St yl 
ize d 
ex ce 
ss  ri 
sk  e 
rro r 
n=300, S=400, MDP=FullyConnectedMDP, gamma=0.99 
all_ones one_hot gaussian 
Figure 7: Left: Approximation error ‖PFkV π‖ given a one-hot, all-ones and Gaussian reward vector and for MDPs with different graphical structures. Middle: Median empirical excess risk E(VFk,ŵ) given a one-hot, all-ones and Gaussian reward vector. Right Theoretical excess risk for a representation Φk = Fk and a one-hot, all-ones and Gaussian reward vector. The median is over 5 random seeds and shading gives 95% confidence intervals.
On the Generalization of Representations in Reinforcement Learning 
transition to the star center and the star center goes to the star corners. There are two extreme cases in terms of rewards: either the reward is the same for all si, i 6= S, (e.g. the all ones reward vector or the one-hot vector eS) or not. If the reward is the same for all si, i 6= S, then this is effectively a 2 state structure, so we only really need 1 feature to distinguish between the value of the star corners and the value of the star center. However, if the reward is different for all si(i 6= S) then we effectively have (S − 1) tuples (si, sS) which can be thought of as independent graphical structures and we thus expect to need all the features to distinguish between their values. We can see this in Figure 7 that for the all ones reward vector and the one-hot reward vector eS , the error with k = 1 is very good but for the Gaussian reward, the error with k = 1 is high. 
Chain: This is a S-state connected graph with 2 pendant states and (n− 2) states of degree two. The shapes of the curves are similar to the Torus1d but we can notice that the errors are larger for each feature dimension k. This is intuitive as for instance in the case of an all ones reward vector, the values are not the same for each state due to the two end states of the chain, implying that more than one feature is needed to generalize the value function. 
Openroom: This is a two-dimensional grid with S states. States strictly inside the grid have four neighbours. States belonging to one (reps. two) edges are of degree three (resp. two). As we observed in Figure 2, the Openroom domain does not generalizes as well as the Torus2d which can be explained by their difference in effective dimension. 
Torus1d: This is a wrap-around version of the Chain. State i transitions to state (i+ 1) mod S and state (i− 1) mod S. We can see that the curve showing the empirical excess risk (Middle) corresponding to the Gaussian reward vector has a sweet spot which is also predicted by our theory. Moreover, when all states have the same reward, their values are identical. Hence, in that case, only one feature is enough to have very low error which is shown both empirically and by our theoretical bound on Figure 7. 
Torus2d: It is a wrap-around version of the Openroom domain such that each state has four different neighbors. We can see in Figure 2 that the Torus1d and Torus2d have similar effective dimension but the decay of the singular values is faster in the case of Torus2d translating into smaller approximation errors in Figure 7 (Middle). This results in overall lower excess risk for the Torus2d indicating it generalizes in general better than its one-dimensional counterpart. Just like for the Torus1d, in the case of the Gaussian reward vector, there is a non trivial optimal number of features k minimizing the excess risk, which we can notice is smaller than for the Torus1d. 
Disconnected: This graph consists of S states that self-transition. We do not expect the successor representation to generalize well within this MDP as we cannot leverage knowledge from one feature state to another. This idea was already captured by the effective dimension shown in Figure 2. The plots in Figure 7 corroborates this both empirically and theoretically showing that its excess risk is indeed the highest across all transition structures considered. 
Fullyconnected: This is a connected graph of S states where each state can transition to (S − 1) states. The first singular vector, which is the constant vector, is very good in terms of effective dimension but the second vector has high effective dimension. When the rewards are the same in each state, their values are identical. In that case, one feature is enough to distinguish between the S states leading to good generalization in that case. Additional features must be misleading as the excess risks rises significantly from a number of features k = 2. 
C.2 Full Atari Results 
For all experiments, we used the hyperparameters provided by Dopamine (Castro et al., 2018). 
Compute. For our experiments on Atari, we used Tesla V100 GPUs and P100 for all runs. To obtain the pretrained deep representations for each deep RL agent, we ran a total of 5 runs / game × 60 games / algorithm × 5 algorithms = 1500 runs. Each of these runs takes around 5 days. Additionally, for the auxiliary loss experiment, we ran a total of 5 runs / game × 5 games / algorithm × 2 algorithms = 50 runs. In this setting, each run takes around 1 day. Overall, the amount of compute is of 7050 days of GPU training. 
We provide a per-game comparison of the effective dimension of the representations induced by DQN, DQN (Adam), Rainbow, IQN and M-IQN throughout training in Figure 9 for all 60 Atari games in the online setting to complement the results presented in Figure 4 in the main part of the paper.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
For the offline experiment presented in Figure 5, we use the same mini-batch sampled for the temporal-difference loss LTD for computing the auxiliary loss Lφ. Our combined loss is then Lα = (1 − α)LTD + αLφ. We ran a hyperparameter sweep over α on the five games displayed in Figure 8 and found that a value of α = 0.1 worked well. We provide per-game training curves for IQN agents for 17 Atari games in Figure 10 as well as the effective dimension (see Figure 11) of their induced representations computed with a batch size of 215. We also complement these results with the rank of these representations as a function of training in Figure 12 and Figure 13 as a proxy for the approximation error. 
α= 0.01 α= 0.1 α= 0.0 α= 0.03 
0 20 40 60 80 100 Gradient Updates (x 62.5k) 
1000 
2000 
3000 
Av er 
ag e 
Sc or 
e 
Asterix 
0 20 40 60 80 100 Gradient Updates (x 62.5k) 
0 
20 
40 
60 
Breakout 
0 20 40 60 80 100 Gradient Updates (x 62.5k) 
−20 
−10 
0 
10 
20 Pong 
0 20 40 60 80 100 Gradient Updates (x 62.5k) 
0 
2500 
5000 
7500 
10000 
12500 
Q*Bert 
0 20 40 60 80 100 Gradient Updates (x 62.5k) 
0 
1000 
2000 
3000 
4000 
5000 Seaquest 
Figure 8: Sweeping over various values of α when adding the auxiliary loss Lφ to IQN.
On the Generalization of Representations in Reinforcement Learning 
DQN(Adam) Rainbow DQN(Nature) IQN M-IQN 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
AirRaid 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Alien 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Amidar 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Assault 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Asterix 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Asteroids 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Atlantis 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
BankHeist 
0 50 100 150 200 Iterations 
10 
0 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
BattleZone 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
BeamRider 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Berzerk 
0 50 100 150 200 Iterations 
10 
0 
5 × 10 −1 
6 × 10 −1 
7 × 10 −1 
8 × 10 −1 
9 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Bowling 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Boxing 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Breakout 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Carnival 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Centipede 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
ChopperCommand 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
CrazyClimber 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
DemonAttack 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
DoubleDunk 
0 50 100 150 200 Iterations 
10 
0 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
ElevatorAction 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Enduro 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
FishingDerby 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Freeway 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Frostbite 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Gopher 
0 50 100 150 200 Iterations 
10 
0 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Gravitar 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Hero 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
IceHockey 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Jamesbond 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
JourneyEscape 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Kangaroo 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Krull 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
KungFuMaster 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
MontezumaRevenge 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
MsPacman 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
NameThisGame 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Phoenix 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Pitfall 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Pong 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Pooyan 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
PrivateEye 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Qbert 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Riverraid 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
RoadRunner 
0 50 100 150 200 Iterations 
10 
0 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Robotank 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Seaquest 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Skiing 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Solaris 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
SpaceInvaders 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
StarGunner 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Tennis 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
TimePilot 
0 50 100 150 200 Iterations 
10 
0 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Tutankham 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
UpNDown 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Venture 
0 50 100 150 200 Iterations 
10 
0 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
VideoPinball 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
WizardOfWor 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
YarsRevenge 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Zaxxon 
Figure 9: Average estimate (darker color) of the effective dimension normalized by the batch size used N = 215 
on DQN(Nature), DQN(Adam), Rainbow, IQN and M-IQN on all 60 Atari games computed using 5 independent runs. Individual runs are shown with a lighter color.
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
0 50 100 150 200 Gradient Updates (x 62.5k) 
1000 
2000 
3000 
4000 Av 
er ag 
e Sc 
or e 
Asterix 
0 50 100 150 200 Gradient Updates (x 62.5k) 
500 
750 
1000 
1250 
1500 
Beam Rider 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
20 
40 
60 Breakout 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
1000 
2000 
3000 
4000 
Av er 
ag e 
Sc or 
e 
Demon Attack 
0 50 100 150 200 Gradient Updates (x 62.5k) 
−25 
−20 
−15 
−10 Double Dunk 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
250 
500 
750 
1000 
Enduro 
0 50 100 150 200 Gradient Updates (x 62.5k) 
−20 
−15 
−10 
−5 
Av er 
ag e 
Sc or 
e 
Ice Hockey 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
100 
200 
300 
400 
James Bond 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
500 
1000 
1500 
2000 
2500 
Ms. Pac-Man 
0 50 100 150 200 Gradient Updates (x 62.5k) 
−20 
−10 
0 
10 
20 
Av er 
ag e 
Sc or 
e 
Pong 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
5000 
10000 
15000 Q*Bert 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
10000 
20000 
30000 
40000 
Road Runner 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
1000 
2000 
3000 
4000 
5000 
Av er 
ag e 
Sc or 
e 
Seaquest 
0 50 100 150 200 Gradient Updates (x 62.5k) 
200 
400 
600 
800 
1000 Space Invaders 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
200 
400 
600 
800 Wizard Of Wor 
0 50 100 150 200 Gradient Updates (x 62.5k) 
5000 
10000 
15000 
20000 
25000 
Av er 
ag e 
Sc or 
e 
Yars's Revenge 
0 50 100 150 200 Gradient Updates (x 62.5k) 
0 
2000 
4000 
6000 
8000 Zaxxon 
IQN IQN + Feature Reg. 
Figure 10: Per-game learning curves of IQN and IQN with feature regularization Lφ on 17 Atari games in the offline RL setting.
On the Generalization of Representations in Reinforcement Learning 
0 50 100 150 200 Iterations 
10 
−3 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Asterix 
0 50 100 150 200 Iterations 
10 
−4 
10 
−3 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
BeamRider 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Breakout 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
DemonAttack 
0 50 100 150 200 Iterations 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
DoubleDunk 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Enduro 
0 50 100 150 200 Iterations 
10 
−3 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
IceHockey 
0 50 100 150 200 Iterations 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Jamesbond 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
MsPacman 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Pong 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Qbert 
0 50 100 150 200 Iterations 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
RoadRunner 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Seaquest 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
SpaceInvaders 
0 50 100 150 200 Iterations 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
WizardOfWor 
0 50 100 150 200 Iterations 
10 
0 
2 × 10 −1 
3 × 10 −1 
4 × 10 −1 
6 × 10 −1 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
YarsRevenge 
0 50 100 150 200 Iterations 
10 
−2 
10 
−1 
10 
0 
Ef fe 
ct iv 
e D 
im en 
si on 
 / N 
Zaxxon 
IQN IQN+Feature Reg. 
Figure 11: Per-game effective dimension normalized by the batch size N = 215 of IQN and IQN with feature regularization Lφ on 17 Atari games in the offline RL setting, using 5 independent runs. Individual runs are 
Charline Le Lan, Stephen Tu, Adam Oberman, Rishabh Agarwal, Marc Bellemare 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
10 
3 
R an 
k Asterix 
0 50 100 150 200 Iterations 
10 2R 
an k 
Breakout 
0 50 100 150 200 Iterations 
10 
2 
R an 
k 
Pong 
0 50 100 150 200 Iterations 
10 2R 
an k 
Seaquest 
0 50 100 150 200 Iterations 
10 
2 
2 × 10 2 
3 × 10 2 
4 × 10 2 
6 × 10 2 
R an 
k 
Qbert 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
R an 
k 
SpaceInvaders 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
R an 
k 
Zaxxon 
0 50 100 150 200 Iterations 
10 
2 
2 × 10 2 
3 × 10 2 
4 × 10 2 
6 × 10 2 
R an 
k 
YarsRevenge 
0 50 100 150 200 Iterations 
10 
2 
2 × 10 2 
3 × 10 2 
4 × 10 2 
6 × 10 2 
R an 
k 
RoadRunner 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
R an 
k 
MsPacman 
0 50 100 150 200 Iterations 
10 
−2 
10 
0 
10 
2 
R an 
k 
BeamRider 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
10 
3 
R an 
k 
Jamesbond 
0 50 100 150 200 Iterations 
10 
2 
R an 
k 
Enduro 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
R an 
k 
WizardOfWor 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
10 
3 
R an 
k 
IceHockey 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
10 
3 
R an 
k 
DoubleDunk 
0 50 100 150 200 Iterations 
10 
1 
10 
2 
R an 
k 
DemonAttack 
IQN IQN + Feature Reg. 
Figure 12: Per-game rank of IQN and IQN with feature regularization Lφ computed with a batch size N = 215 on 17 Atari games in the offline RL setting, using 5 independent runs. Individual runs are shown with a lighter color.
On the Generalization of Representations in Reinforcement Learning 
IQN IQN + Feature Reg. 
0 50 100 150 200 Number of Frames (in millions) 
100 
200 
300 
400 
500 
R an 
k  (I 
nt er 
qu ar 
til e 
M ea 
n) 
Figure 13: Interquartile mean (IQM) (Agarwal et al., 2021b) for the rank of representations induced by IQN and IQN with feature regularization Lφ computed with a batch size N = 215 on 17 Atari games in the offline setting. 
D SOCIETAL IMPACT 
This paper contributes to the fundamental understanding of state representations, characterizing their generalization capacity. Our work suggests that algorithms making use of representations minimized by the excess risk bound from Theorem 1 can improve their performance. However, when making the choice of such a representation, we did not focus on other important factors like the computational cost of learning these representations, their scalability or the biases these representations can propagate resulting into possible discriminatory outcomes or dangerous behaviours. We suggest that practitioners should not only consider our generalization characterization of representations but also ethical deliberations.