> Source: https://arxiv.org/pdf/2108.08993

Distributionally Robust Learning 
Suggested Citation: Ruidi Chen and Ioannis Ch. Paschalidis (2020), “Distributionally Robust Learning”, : Vol. 4, No. 1–2, pp 1–243. DOI: 10.1561/2400000026. 
Ruidi Chen Boston University 
rchen15@bu.edu 
Ioannis Ch. Paschalidis Boston University 
yannisp@bu.edu 
This article may be used only for the purpose of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval. Boston — Delft 
 
 
 
 
 
 
 
 
 
 
 
Contents 
1 Introduction 2 1.1 Robust Optimization . . . . . . . . . . . . . . . . . . . . 7 1.2 Distributionally Robust Optimization . . . . . . . . . . . . 8 1.3 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 1.4 Notational Conventions . . . . . . . . . . . . . . . . . . . 15 1.5 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . 18 
2 The Wasserstein Metric 21 2.1 Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 2.2 A Distance Metric . . . . . . . . . . . . . . . . . . . . . . 23 2.3 The Dual Problem . . . . . . . . . . . . . . . . . . . . . . 26 2.4 Some Special Cases . . . . . . . . . . . . . . . . . . . . . 28 2.5 The Transport Cost Function . . . . . . . . . . . . . . . . 30 2.6 Robustness of the Wasserstein Ambiguity Set . . . . . . . 34 2.7 Setting the Radius of the Wasserstein Ball . . . . . . . . . 38 
3 Solving the Wasserstein DRO Problem 49 3.1 Dual Method . . . . . . . . . . . . . . . . . . . . . . . . 49 3.2 The Extreme Distribution . . . . . . . . . . . . . . . . . . 56 3.3 A Discrete Empirical Nominal Distribution . . . . . . . . . 57 3.4 Finite Sample Performance . . . . . . . . . . . . . . . . . 60 3.5 Asymptotic Consistency . . . . . . . . . . . . . . . . . . . 62
4 Distributionally Robust Linear Regression 65 4.1 The Problem and Related Work . . . . . . . . . . . . . . 65 4.2 The Wasserstein DRO Formulation for Linear Regression . 67 4.3 Performance Guarantees for the DRO Estimator . . . . . . 73 4.4 Experiments on the Performance of Wasserstein DRO . . . 88 4.5 An Application of Wasserstein DRO to Outlier Detection . 103 4.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . 110 
5 Distributionally Robust Grouped Variable Selection 111 5.1 The Problem and Related Work . . . . . . . . . . . . . . 111 5.2 The Groupwise Wasserstein Grouped LASSO . . . . . . . . 113 5.3 Performance Guarantees to the DRO Groupwise Estimator 121 5.4 Numerical Experiments . . . . . . . . . . . . . . . . . . . 127 5.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . 139 
6 Distributionally Robust Multi-Output Learning 145 6.1 The Problem and Related Work . . . . . . . . . . . . . . 145 6.2 Distributionally Robust Multi-Output Learning Models . . 148 6.3 The Out-of-Sample Performance Guarantees . . . . . . . . 160 6.4 Numerical Experiments . . . . . . . . . . . . . . . . . . . 166 6.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . 176 
7 Optimal Decision Making via Regression Informed K-NN 179 7.1 The Problem and Related Work . . . . . . . . . . . . . . 179 7.2 Robust Nonlinear Predictive Model . . . . . . . . . . . . . 182 7.3 Prescriptive Policy Development . . . . . . . . . . . . . . 190 7.4 Developing Optimal Prescriptions for Patients . . . . . . . 196 7.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . 204 
8 Advanced Topics in Distributionally Robust Learning 206 8.1 Distributionally Robust Learning with Unlabeled Data . . . 207 8.2 Distributionally Robust Reinforcement Learning . . . . . . 216 
9 Discussion and Conclusions 226 
Acknowledgements 229
References 231
Distributionally Robust Learning 
Ruidi Chen1 and Ioannis Ch. Paschalidis2 
1Boston University; rchen15@bu.edu 2Boston University; yannisp@bu.edu 
ABSTRACT This monograph develops a comprehensive statistical learning framework that is robust to (distributional) perturbations in the data using Distributionally Robust Optimization (DRO) under the Wasserstein metric. Beginning with fundamental properties of the Wasserstein metric and the DRO formulation, we explore duality to arrive at tractable formulations and develop finite-sample, as well as asymptotic, performance guarantees. We consider a series of learning problems, including (i) distributionally robust linear regression; (ii) distributionally robust regression with group structure in the predictors; (iii) distributionally robust multi-output regression and multiclass classification, (iv) optimal decision making that combines distributionally robust regression with nearest-neighbor estimation; (v) distributionally robust semi-supervised learning, and (vi) distributionally robust reinforcement learning. A tractable DRO relaxation for each problem is being derived, establishing a connection between robustness and regularization, and obtaining bounds on the prediction and estimation errors of the solution. Beyond theory, we include numerical experiments and case studies using synthetic and real data. The real data experiments are all associated with various health informatics problems, an application area which provided the initial impetus for this work. 
Ruidi Chen and Ioannis Ch. Paschalidis (2020), “Distributionally Robust Learning”, : Vol. 4, No. 1–2, pp 1–243. DOI: 10.1561/2400000026.
1 
Introduction 
A central problem in machine learning is to learn from data (“big” or “small”) how to predict outcomes of interest. Outcomes can be binary or discrete, such as an event or a category, or continuous, e.g., a real value. In either case, we have access to a number N of examples from which we can learn; each example is associated with a potentially large number p of predictor variables and the “ground truth” discrete or continuous outcome. This form of learning is called supervised, because it relies on the existence of known examples associating predictor variables with the outcome. In the case of a binary/discrete outcome the problem is referred to as classification, while for continuous outcomes we use the term regression. 
There are many methods to solve such supervised learning problems, from ordinary (linear) least squares regression, to logistic regression, Classification And Regression Trees (CART) (Breiman, 2017), ensembles of decision trees (Breiman, 2001; Chen and Guestrin, 2016), to modern deep learning models (Goodfellow et al., 2016). Whereas the nonlinear models (random forests, gradient boosted trees, and deep learning) perform very well in many specific applications, they have two key drawbacks: (i) they produce predictive models that lack interpretability 
2
3 and (ii) they are hard to analyze and do not give rise to rigorous mathematical results characterizing their performance and important properties. In this monograph, we will mainly focus on the more classical linear models, allowing for some nonlinear extensions. 
Clearly, there is a plethora of application areas where such models have been developed and used. A common thread throughout this monograph is formed by applications in medicine and health care, broadly characterized by the term predictive health analytics. While in principle these applications are not substantially different from other domains, they have important salient features that need to be considered. These include: 
1. Presence of outliers. Medical data often contain outliers, which may be caused by medical errors, erroneous or missing data, equipment and lab configuration errors, or even different inter-pretation/use of a variable by different physicians who enter the data. 
2. Risk of “overfitting” from too many variables. For any individual and any outcome we wish to predict, using all predictor variables may lead to overfitting and large generalization errors (out-of-sample). The common practice is to seek sparse models, using the fewest variables possible without significantly compromising accuracy. In some settings, especially when genetic information is included in the predictors, the number of predictors can exceed the training sample size, further stressing the need for sparsity. Sparse regression models originated in the seminar work on the Least Absolute Shrinkage and Selection Operator, better known under the acronym LASSO (Tibshirani, 1996). 
3. Lack of linearity. In some applications, the linearity of regression or logistic regression may not fully capture the relationship between predictors and outcome. While kernel methods (Friedman et al., 2001) can be used to employ linear models in developing nonlinear predictors, other choices include combining linear models with nearest neighbor ideas to essentially develop piecewise linear models.
4 Introduction 
To formulate the learning problems of interest more concretely, let x = (x1, . . . , xp) ∈ Rp denote a column vector with the predictors and let y ∈ R be the outcome or response. In the classification problem, we have y ∈ {−1,+1}. We are given training data (xi, yi), i ∈ JNK, where JNK 4= 1, . . . , N , from which we want to “learn” a function f(·) so that f(xi) = yi for most i. Further, we want f(·) to generalize well to new samples (i.e., to have good out-of-sample performance). 
In the regression problem, we view the xi’s as independent variables (predictor vectors) and yi as the real-valued dependent variable. We still want to determine a function f(x) that predicts y. In linear regression, f(x) = β′x, where β is a coefficient vector, prime denotes transpose, and we assume one of the elements of x is equal to one with the corresponding coefficient being the intercept (of the regression function at zero). Both classification and regression problems can be formulated as: 
minβ EP∗ [hβ(x, y)], (1.1) 
where P∗ is the probability distribution of (x, y), EP∗ stands for the expectation under P∗, and hβ(x, y) is a loss function penalizing differences between f(x) and y. This formulation is known as expected risk minimization. Ordinary Least Squares (OLS) uses a squared loss hβ(x, y) = (f(x)− y)2 while logistic regression uses the logloss function hβ(x, y) = log(1 + exp{−yf(x)}). Since P∗ is typically unknown, a common practice is to approximate it using the empirical distribution P̂N which assigns equal probability to each training sample, leading to the following empirical risk minimization formulation: 
minβ 1 N 
∑N i=1 hβ(xi, yi). 
One of the well known issues of OLS regression is that the regression function can be particularly sensitive to outliers. To illustrate this with a simple example, consider a case of regression with a single predictor; see Fig. 1.1. Points in the training set are shown as blue dots. Suppose we include in the training set some outliers depicted as magenta stars. OLS regression results in the black line. Notice how much the slope of this line has shifted away from the blue dots to accommodate the outliers. This skews future predictions but also our ability to identify
5 Figure 1.1: Regression example. 
new outlying observations. Several approaches have been introduced to address this issue (Huber, 1964; Huber, 1973) and we discuss them in more detail in Section 4. 
The main focus of this monograph is to develop robust learning methods for a variety of learning problems. To introduce robustness into the generic problem, we will use ideas from robust optimization and formulate a robust version of the expected risk minimization Problem (1.1). We will further focus on distributional robustness. The problems we will formulate are min-max versions of Problem (1.1) where one minimizes a worst case estimate of the loss over some appropriately defined ambiguity set. Such min-max formulations have a long history, going back to the origins of game theory (Von Neumann and Morgenstern, 1944), where one can view the problem as a game between an adversary who may affect the training set and the optimizer who responds to the worst-case selection by the adversary. They also have strong connections with H∞ and robust control theory (Zames, 1981; Zhou and Doyle, 1998). 
To avoid being overly broad, we will restrict our attention to the intersection of statistical learning and Distributionally Robust Optimiza-tion (DRO) under the Wasserstein metric (Esfahani and Kuhn, 2018; Gao and Kleywegt, 2016; Chen and Paschalidis, 2018). Even this more
6 Introduction 
narrow area has generated a lot of interest and recent work. While we will cover several aspects, we will not cover a number of topics, including: 
 the integration of DRO with different optimization schemes, e.g., inverse optimization (Esfahani et al., 2018), polynomial optimization (Mevissen et al., 2013), multi-stage optimization (Zhao and Guan, 2018; Hanasusanto and Kuhn, 2018), and chanceconstrained optimization (Xie, 2019; Ji and Lejeune, 2020); 
 the application of DRO to stochastic control problems, see, e.g., Van Parys et al., 2015; Yang, 2018b; Yang, 2018a, and statistical hypothesis testing (Gao et al., 2018); 
 the combination of DRO with general estimation techniques, see, e.g., Nguyen et al., 2019 for distributionally robust Minimum Mean Square Error Estimation, and Nguyen et al., 2018 for distributionally robust Maximum Likelihood Estimation. 
Most of the learning problems we consider, except for Section 8.2, are static single-period problems where the data are assumed to be independently and identically distributed. For extensions of DRO to a dynamic setting where the data come in a sequential manner, we refer to Abadeh et al., 2018 for a distributionally robust Kalman filter model, Hanasusanto and Kuhn, 2013; Yang, 2018a; Duque and Morton, 2020 for robust dynamic programming, and Sinha et al., 2020 for a distributionally robust online adaptive algorithm. 
In this monograph, we focus mainly on linear predictive models, with the exception of Section 7, where the non-linearity is captured by a non-parametric K-Nearest Neighbors (K-NN) model. For extensions of robust optimization to non-linear settings, we refer to Shang et al., 2017 for robust kernel methods, Fathony et al., 2018 for distributionally robust graphical models, and Sinha et al., 2018 for distributionally robust deep neural networks. 
In the remainder of this Introduction, we will present a brief outline of robust optimization in Section 1.1 and distributionally robust optimization in Section 1.2. In Section 1.3 we provide an outline of the
1.1. Robust Optimization 7 
topics covered in the rest of the monograph. Section 1.4 summarizes our notational conventions and Section 1.5 collects all abbreviations we will use. 
1.1 Robust Optimization 
Robust optimization (Ben-Tal et al., 2009; Bertsimas et al., 2011) provides a way of modeling uncertainty in the data without the use of probability distributions. It restricts data perturbations to be within a deterministic uncertainty set, and seeks a solution that is optimal for the worst-case realization of this uncertainty. Consider a general optimization problem: 
min β 
hβ(z), (1.2) 
where β is a vector of decision variables, z is a vector of given parameters, and h is a real-valued function. Assuming that the values of z lie within some uncertainty set Z, a robust counterpart of Problem (1.2) can be written in the following form: 
min β 
max z∈Z 
hβ(z). (1.3) 
Problem (1.3) is computationally tractable for many classes of uncertainty sets Z. For a detailed overview of robust optimization we refer to Ben-Tal et al., 2009; Ben-Tal and Nemirovski, 2008; Bertsimas et al., 2011. 
There has been an increasing interest in using robust optimization to develop machine learning algorithms that are immunized against data perturbations; see, for example, El Ghaoui and Lebret, 1997; Xu et al., 2009a; Yang and Xu, 2013; Bertsimas and Copenhaver, 2018 for regression, and El Ghaoui et al., 2003; Trafalis and Gilbert, 2006; Liu and Ziebart, 2014; Bertsimas et al., 2018 for classification methods. Bertsimas et al., 2018 considered both feature uncertainties: 
Zx , { ∆X ∈ RN×p : ‖∆xi‖q ≤ ρ, i ∈ JNK 
} , 
where ∆X can be viewed as a feature perturbation matrix on N samples with p features, ‖ · ‖q is the `q norm, and ∆xi ∈ Rp, i ∈ JNK, are the
8 Introduction 
rows of ∆X, as well as label uncertainties: 
Zy , { ∆y ∈ {0, 1}N : 
∑N 
i=1 ∆yi ≤ Γ 
} , 
where ∆yi ∈ {0, 1}, with 1 indicating that the label was incorrect and has in fact been flipped, and 0 otherwise, and Γ is an integer-valued parameter controlling the number of data points that are allowed to be mislabeled. They solved various robust classification models under these uncertainty sets. As an example, the robust Support Vector Machine (SVM) (Cortes and Vapnik, 1995) problem was formulated as: 
min w,b 
max ∆y∈Zy 
max ∆X∈Zx 
∑N 
i=1 max 
{ 1− yi(1− 2∆yi)(w′(xi + ∆xi)− b), 0 
} . 
Xu et al., 2009a studied a robust linear regression problem with featurewise disturbance: 
min β 
max ∆X∈Zx 
‖y− (X + ∆X)β‖2, 
where β is the vector of regression coefficients, and the uncertainty set 
Zx , { ∆X ∈ RN×p : ‖∆x̃i‖2 ≤ ci, i ∈ JpK 
} , 
where ∆x̃i ∈ RN , i ∈ JpK, are the columns of ∆X. They showed that such a robust regression problem is equivalent to the following `1-norm regularized regression problem: 
min β ‖y−Xβ‖2 + 
∑p 
i=1 ci|βi|. 
1.2 Distributionally Robust Optimization 
Different from robust optimization, Distributionally Robust Optimization (DRO) treats the data uncertainty in a probabilistic way. It minimizes a worst-case expected loss function over a probabilistic ambiguity set that is constructed from the observed samples and characterized by certain known properties of the true data-generating distribution. DRO has been an active area of research in recent years, due to its probabilistic interpretation of the uncertain data, tractability when assembled with certain metrics, and extraordinary performance observed on numerical
1.2. Distributionally Robust Optimization 9 
examples, see, for example, Gao and Kleywegt, 2016; Gao et al., 2017; Shafieezadeh-Abadeh et al., 2017; Esfahani and Kuhn, 2018; Chen and Paschalidis, 2018. DRO can be interpreted in two related ways: it refers to (i) a robust optimization problem where a worst-case loss function is being hedged against; or, alternatively, (ii) a stochastic optimization problem where the expectation of the loss function with respect to the probabilistic uncertainty of the data is being minimized. Figure 1.2 provides a schematic comparison of various optimization frameworks. 
Figure 1.2: Comparison of robust optimization with distributionally robust optimization. 
To formulate a DRO version of the expected risk minimization problem (1.1), consider the stochastic optimization problem: 
inf β 
EP∗[hβ(z) ] , (1.4) 
where we set z = (x, y) ∈ Z ⊆ Rd in (1.1), β ∈ Rp is a vector of coefficients to be learned, hβ(z) : Z × Rp → R is the loss function of applying β on a sample z ∈ Z, and P∗ is the underlying true probability distribution of z. The DRO formulation for (1.4) minimizes the worstcase expected loss over a probabilistic ambiguity set Ω: 
inf β 
sup Q∈Ω 
EQ[hβ(z) ] . (1.5) 
The existing literature on DRO can be split into two main branches, depending on the way in which Ω is defined. One is through a moment
10 Introduction 
ambiguity set, which contains all distributions that satisfy certain moment constraints (Mehrotra and Zhang, 2014; Popescu, 2007; Delage and Ye, 2010; Goh and Sim, 2010; Zymler et al., 2013; Wiesemann et al., 2014). In many cases it leads to a tractable DRO problem but has been criticized for yielding overly conservative solutions (Wang et al., 2016). The other is to define Ω as a ball of distributions: 
Ω , { Q ∈ P(Z) : D(Q, P0) ≤ ε 
} , 
where Z is the set of possible values for z; P(Z) is the space of all probability distributions supported on Z; ε is a pre-specified radius of the set Ω; and D(Q, P0) is a probabilistic distance function that measures the distance between Q and a nominal distribution P0. 
The nominal distribution P0 is typically chosen as the empirical distribution on the observed samples {z1, . . . , zN}: 
P0 = P̂N , 1 N 
∑N 
i=1 δzi(z), 
where δzi(·) is the Dirac density assigning probability mass equal to 1 at zi; see Esfahani and Kuhn, 2018; Abadeh et al., 2015; Chen and Paschalidis, 2018. There are also works employing a nonparametric kernel density estimation method to obtain a continuous density function for the nominal distribution, when the underlying true distribution is continuous, see Jiang and Guan, 2018; Zhao and Guan, 2015. The kernel density estimator is defined as: 
f0(z) = 1 N |H|1/2 
N∑ i=1 
K ( H−1/2(z− zi) 
) , 
where f0 represents the density function of the nominal distribution P0, i.e., f0 = dP0/dz, H ∈ Rd×d represents a symmetric and positive definite bandwidth matrix, and K(·) : Rd → R+ is a symmetric kernel function satisfying K(·) ≥ 0, 
∫ Rd K(z)dz = 1, and 
∫ Rd K(z)zdz = 0. 
An example of the probabilistic distance function D(·, ·) is the φ-divergence (Bayraksan and Love, 2015): 
D(Q, P0) = EP0 [ φ ( dQ 
dP0 
)] ,
1.2. Distributionally Robust Optimization 11 
where φ(·) is a convex function satisfying φ(1) = 0. For example, if φ(t) = t log t, we obtain the Kullback-Leibler (KL) divergence (Hu and Hong, 2013; Jiang and Guan, 2015). The definition of the φ-divergence requires that Q is absolutely continuous with respect to P0. If we take the empirical measure to be the nominal distribution P0, this implies that the support of Q must be a subset of the empirical examples. This constraint could potentially hurt the generalization capability of DRO. 
Other choices for D(·, ·) include the Prokhorov metric (Erdoğan and Iyengar, 2006), and the Wasserstein distance (Esfahani and Kuhn, 2018; Gao and Kleywegt, 2016; Zhao and Guan, 2018; Luo and Mehrotra, 2017; Blanchet and Murthy, 2019). DRO with the Wasserstein metric has been extensively studied in the machine learning community; see, for example, Chen and Paschalidis, 2018; Blanchet et al., 2019b for robustified regression models, Sinha et al., 2018 for adversarial training in neural networks, and Abadeh et al., 2015 for distributionally robust logistic regression. Shafieezadeh-Abadeh et al., 2017; Gao et al., 2017 provided a comprehensive analysis of the Wasserstein-based distributionally robust statistical learning problems with a scalar (as opposed to a vector) response. In recent work, Blanchet et al., 2019a proposed a DRO formulation for convex regression under an absolute error loss. 
In this monograph we adopt the Wasserstein metric to define a data-driven DRO problem. Specifically, the ambiguity set Ω is defined as: 
Ω , { Q ∈ P(Z) : Ws,t(Q, P̂N ) ≤ ε 
} , (1.6) 
where P̂N is the uniform empirical distribution over N training samples zi, i ∈ JNK, and Ws,t(Q, P̂N ) is the order-t Wasserstein distance (t ≥ 1) between Q and P̂N defined as: 
Ws,t(Q, P̂N ) , ( 
min π∈P(Z×Z) 
∫ Z×Z 
( s(z1, z2) 
)tdπ(z1, z2 ))1/t 
, (1.7) 
where s is a metric on the data space Z, and π is the joint distribution of z1 and z2 with marginals Q and P̂N , respectively. The Wasserstein distance between two distributions represents the cost of an optimal mass transportation plan, where the cost is measured through the metric s.
12 Introduction 
We choose the Wasserstein metric for two main reasons. On one hand, the Wasserstein ambiguity set is rich enough to contain both continuous and discrete relevant distributions, while other metrics such as the KL divergence, exclude all continuous distributions if the nominal distribution is discrete (Esfahani and Kuhn, 2018; Gao and Kleywegt, 2016). Furthermore, considering distributions within a KL distance from the empirical, does not allow for probability mass outside the support of the empirical distribution. 
On the other hand, measure concentration results guarantee that the Wasserstein set contains the true data-generating distribution with high confidence for a sufficiently large sample size (Fournier and Guillin, 2015). Moreover, the Wasserstein metric takes into account the closeness between support points while other metrics such as the φ-divergence only consider the probabilities on these points. An image retrieval example in Gao and Kleywegt, 2016 suggests that the probabilistic ambiguity set constructed based on the KL divergence prefers the pathological distribution to the true distribution, whereas the Wasserstein distance does not exhibit such a problem. The reason lies in that the φ-divergence does not incorporate a notion of closeness between two points, which in the context of image retrieval represents the perceptual similarity in color. 
1.3 Outline 
The goal of this monograph is to develop a comprehensive robust statistical learning framework using a Wasserstein-based DRO as the modeling tool. Specifically, 
 we provide background knowledge on the basics of DRO and the Wasserstein metric, and show its robustness inducing property through discussions on the Wasserstein ambiguity set and the property of the DRO solution; 
 we cover a variety of predictive and prescriptive models that can be posed and solved using the Wasserstein DRO approach, and show novel problem-tailored theoretical results and real world
1.3. Outline 13 
applications, strengthening the notion of robustness through these discussions; 
 we consider a variety of synthetic and real world case studies of the respective models, which validate the theory and the proposed DRO approach and highlight its advantages compared to several alternatives. This could potentially (i) ease the understanding of the model and approach; and (ii) attract practitioners from various fields to put these models into use. 
Robust models can be useful when (i) the training data is contaminated with noise, and we want to learn a model that is immunized against the noise; or (ii) the training data is pure, but the test set is contaminated with outliers. In both scenarios we require the model to be insensitive to the data uncertainty/unreliability, which is characterized through a probability distribution that resides in a set consisting of all distributions that are within a pre-specified distance from a nominal distribution. The learning problems that are studied in this monograph include: 
 Distributionally Robust Linear Regression (DRLR), which estimates a robustified linear regression plane by minimizing the worst-case expected absolute loss over a probabilistic ambiguity set characterized by the Wasserstein metric; 
 Groupwise Wasserstein Grouped LASSO (GWGL), which aims at inducing sparsity at a group level when there exists a predefined grouping structure for the predictors, through defining a specially structured Wasserstein metric for DRO; 
 Distributionally Robust Multi-Output Learning, which solves a DRO problem with a multi-dimensional response/label vector, generalizing the single-output model addressed in DRLR. 
 Optimal decision making using DRLR informed K-Nearest Neigh-bors (K-NN) estimation, which selects among a set of actions the optimal one through predicting the outcome under each action using K-NN with a distance metric weighted by the DRLR solution;
14 Introduction 
 Distributionally Robust Semi-Supervised Learning, which estimates a robust classifier with partially labeled data, through (i) either restricting the marginal distribution to be consistent with the unlabeled data, (ii) or modifying the structure of DRO by allowing the center of the ambiguity set to vary, reflecting the uncertainty in the labels of the unsupervised data. 
 Distributionally Robust Reinforcement Learning, which considers Markov Decision Processes (MDPs) and seeks to inject robustness into the probabilistic transition model, deriving a lower bound for the distributionally robust value function in a regularized form. 
The remainder of this monograph is organized as follows. Section 2 presents basics and key properties for the Wasserstein metric. Section 3 discusses how to solve a general Wasserstein DRO problem, the structure of the worst-case distribution, and the performance guarantees of the DRO estimator. The rest of the sections are dedicated to specific learning problems that can be posed as a DRO problem. 
In Section 4, we develop the Wasserstein DRO formulation for linear regression under an absolute error loss. Section 5 discusses distributionally robust grouped variable selection, and develops the Groupwise Wasserstein Grouped LASSO (GWGL) formulation under the absolute error loss and log-loss. In Section 6, we generalize the single-output model and develop distributionally robust multi-output learning models under Lipschitz continuous loss functions and the multiclass log-loss. Section 7 presents an optimal decision making framework which selects among a set of actions the best one, using predictions from K-Nearest Neighbors (K-NN) with a metric weighted by the Wasserstein DRO solution. Section 8 covers a number of active research topics in the domain of DRO under the Wasserstein metric, including (i) DRO in Semi-Supervised Learning (SSL) with partially labeled datasets; (ii) DRO in Reinforcement Learning (RL) with temporal correlated data. We close the monograph by discussing further potential research directions in Section 9.
1.4. Notational Conventions 15 
1.4 Notational Conventions 
Vectors 
 Boldfaced lowercase letters denote vectors, ordinary lowercase letters denote scalars, boldfaced uppercase letters denote matrices, and calligraphic capital letters denote sets. 
 ei denotes the i-th unit vector, e or 1 the vector of ones, and 0 a vector of zeros. 
 All vectors are column vectors. For space saving reasons, we write x = (x1, . . . , xdim(x)) to denote the column vector x, where dim(x) is the dimension of x. 
Sets and functions 
 We use R to denote the set of real numbers, and R+ the set of non-negative real numbers. 
 For a set X , we use |X | to denote its cardinality. 
 We write cone{v ∈ V} for a cone that is generated from the set of vectors v ∈ V. 
 1A(x) denotes the indicator function, i.e., 1A(x) = 1 if x ∈ A, and 0 otherwise. 
 For z , (x, y) ∈ X × Y and a function h, the notations h(z) and h(x, y) are used interchangeably, and Z , X × Y. 
 B(Z) denotes the set of Borel measures supported on Z, and P(Z) denotes the set of Borel probability measures supported on Z. 
 For any integer n we write JnK for the set {1, . . . , n}. Hence, P(JnK) denotes the n-th dimensional probability simplex. 
Matrices 
 I denotes the identity matrix.
16 Introduction 
 Prime denotes transpose. Specifically, A′ denotes the transpose of a matrix A. 
 For a matrix A ∈ Rm×n, we will denote by A = (aij)j∈JnK i∈JmK the 
elements of A, by a1, . . . ,am the rows of A, and, with some abuse of our notation which denotes vectors by lowercase letters, we will denote by A1, . . . ,An the columns of A. 
 For a symmetric matrix A, we write A  0 to denote a positive definite matrix, and A < 0 a positive semi-definite matrix. 
 diag(x) denotes a diagonal matrix whose main diagonal consists of the elements of x and all off-diagonal elements are zero. 
 tr(A) denotes the trace (i.e., sum of the diagonal elements) of a square matrix A ∈ Rn×n. 
 |A| denotes the determinant of a square matrix A ∈ Rn×n. 
Norms 
 ‖x‖p , (∑i |xi|p)1/p denotes the `p norm with p ≥ 1, and ‖ · ‖ the general vector norm that satisfies the following properties: 
1. ‖x‖ = 0 implies x = 0; 2. ‖ax‖ = |a|‖x‖, for any scalar a; 3. ‖x + y‖ ≤ ‖x‖+ ‖y‖; 4. ‖x‖ = ‖|x|‖, where |x| = (|x1|, . . . , |xdim(x)|); 5. ‖(x,0)‖ = ‖x‖, for an arbitrarily long vector 0. 
 Any W-weighted `p norm defined as 
‖x‖Wp , ( (|x|p/2)′W|x|p/2 
)1/p with a positive definite matrix W satisfies the above conditions, where |x|p/2 = (|x1|p/2, . . . , |xdim(x)|p/2). 
 For a matrix A ∈ Rm×n, we use ‖A‖p to denote its induced `p norm that is defined as ‖A‖p , supx 6=0 ‖Ax‖p/‖x‖p.
1.4. Notational Conventions 17 
Random variables 
 For two random variables w1 and w2, we say that w1 is stochastically dominated by w2, denoted by w1 
D 
≤ w2, if P(w1 ≥ x) ≤ P(w2 ≥ x) for all x ∈ R. 
 For a dataset D , {z1, . . . , zN}, we use P̂N to denote the empirical measure supported on D, i.e., P̂N , 1 
N 
∑N i=1 δzi(z), where δzi(z) 
denotes the Dirac delta function at point zi ∈ Z. 
 The N -fold product of a distribution P on Z is denoted by PN , which represents a distribution on the Cartesian product space ZN . We write P∞ to denote the limit of PN as N →∞. 
 EP denotes the expectation under a probability distribution P. 
 For a random vector x, cov(x) will denote its covariance. 
 Np(0,Σ) denotes the p-dimensional Gaussian distribution with mean 0 and covariance matrix Σ. 
 For a distribution P ∈ P(X×Y), PX (·) ,∑ y∈Y P(·, y) denotes the 
marginal distribution over X , and P|x ∈ PX (Y) is the conditional distribution over Y given x ∈ X , where PX (Y) denotes the set of all conditional distributions supported on Y, given features in X . 
 Ws,t(P,Q) denotes the order-t Wasserstein distance between measures P,Q under a cost metric s. For ease of notation and when the cost metric is clear from the context we will be writing Wt(P,Q). 
 Ωs,t ε (P) denotes the set of probability distributions whose order-t 
Wasserstein distance under a cost metric s from the distribution P is less than or equal to ε, i.e., 
Ωs,t ε (P) , {Q ∈ P(Z) : Ws,t(Q, P) ≤ ε}. 
For ease of notation, when the cost metric is clear from the context and t = 1, we will be writing Ωε(P), or simply Ω when the center distribution P is clear from the context.
18 Introduction 
1.5 Abbreviations 
ACE . . . . . . . . . . . . . . Angiotensin-Converting Enzyme ACS . . . . . . . . . . . . . . American College of Surgeons AD . . . . . . . . . . . . . . Absolute Deviation ARB . . . . . . . . . . . . . . Angiotensin Receptor Blockers a.s. . . . . . . . . . . . . . . almost surely AUC . . . . . . . . . . . . . . Area Under the ROC Curve BMI . . . . . . . . . . . . . . Body Mass Index CART . . . . . . . . . . . . . . Classification And Regression Trees CCA . . . . . . . . . . . . . . Canonical Correlation Analysis CCR . . . . . . . . . . . . . . Correct Classification Rate CI . . . . . . . . . . . . . . Confidence Interval CT . . . . . . . . . . . . . . Computed Tomography CTDI . . . . . . . . . . . . . . CT Dose Index CVaR . . . . . . . . . . . . . . Conditional Value at Risk C&W . . . . . . . . . . . . . . the Curds and Whey procedure DRLR . . . . . . . . . . . . . . Distributionally Robust Linear 
Regression DRO . . . . . . . . . . . . . . Distributionally Robust Optimization EHRs . . . . . . . . . . . . . . Electronic Health Records EN . . . . . . . . . . . . . . Elastic Net FA . . . . . . . . . . . . . . False Association FD . . . . . . . . . . . . . . False Disassociation FES . . . . . . . . . . . . . . Factor Estimation and Selection GLASSO . . . . . . . . . . . . . . Grouped LASSO GSRL . . . . . . . . . . . . . . Grouped Square Root LASSO GWGL . . . . . . . . . . . . . . Groupwise Wasserstein Grouped 
LASSO HbA1c . . . . . . . . . . . . . . hemoglobin A1c HIPAA . . . . . . . . . . . . . . Health Insurance Portability and 
Accountability Act ICD-9 . . . . . . . . . . . . . . International Classification of 
Diseases, Ninth Revision
1.5. Abbreviations 19 
i.i.d. . . . . . . . . . . . . . . independently and identically distributed 
IRB . . . . . . . . . . . . . . Institutional Review Board IRLS . . . . . . . . . . . . . . Iteratively Reweighted Least Squares KL . . . . . . . . . . . . . . Kullback-Leibler K-NN . . . . . . . . . . . . . . K-Nearest Neighbors LAD . . . . . . . . . . . . . . Least Absolute Deviation LASSO . . . . . . . . . . . . . . Least Absolute Shrinkage and 
Selection Operator LG . . . . . . . . . . . . . . Logistic Regression LHS . . . . . . . . . . . . . . Left Hand Side LMS . . . . . . . . . . . . . . Least Median of Squares LOESS . . . . . . . . . . . . . . LOcally Estimated Scatterplot 
Smoothing LTS . . . . . . . . . . . . . . Least Trimmed Squares MAD . . . . . . . . . . . . . . Median Absolute Deviation MCC . . . . . . . . . . . . . . MultiClass Classification MDP . . . . . . . . . . . . . . Markov Decision Process MeanAE . . . . . . . . . . . . . . Mean Absolute Error min-max . . . . . . . . . . . . . . minimization-maximization MLE . . . . . . . . . . . . . . Maximum Likelihood Estimator MLG . . . . . . . . . . . . . . Multiclass Logistic Regression MLR . . . . . . . . . . . . . . Multi-output Linear Regression MPD . . . . . . . . . . . . . . Minimal Perturbation Distance MPI . . . . . . . . . . . . . . Maximum Percentage Improvement MPMs . . . . . . . . . . . . . . Minimax Probability Machines MSE . . . . . . . . . . . . . . Mean Squared Error NPV . . . . . . . . . . . . . . Negative Predictive Value NSQIP . . . . . . . . . . . . . . National Surgical Quality 
Improvement Program OLS . . . . . . . . . . . . . . Ordinary Least Squares PCR . . . . . . . . . . . . . . Principal Components Regression PPV . . . . . . . . . . . . . . Positive Predictive Value PVE . . . . . . . . . . . . . . Proportion of Variance Explained
20 Introduction 
RBA . . . . . . . . . . . . . . Robust Bias-Aware RHS . . . . . . . . . . . . . . Right Hand Side RL . . . . . . . . . . . . . . Reinforcement Learning ROC . . . . . . . . . . . . . . Receiver Operating Characteristic RR . . . . . . . . . . . . . . Relative Risk RRR . . . . . . . . . . . . . . Reduced Rank Regression RTE . . . . . . . . . . . . . . Relative Test Error SNR . . . . . . . . . . . . . . Signal to Noise Ratio SR . . . . . . . . . . . . . . Squared Residuals SSL . . . . . . . . . . . . . . Semi-Supervised Learning std . . . . . . . . . . . . . . standard deviation SVM . . . . . . . . . . . . . . Support Vector Machine TA . . . . . . . . . . . . . . True Association TD . . . . . . . . . . . . . . True Disassociation TAR . . . . . . . . . . . . . . True Association Rate TDR . . . . . . . . . . . . . . True Disassociation Rate WGD . . . . . . . . . . . . . . Within Group Difference w.h.p. . . . . . . . . . . . . . . with high probability WMSE . . . . . . . . . . . . . . Weighed Mean Squared Error w.p.1 . . . . . . . . . . . . . . with probability 1 w.r.t. . . . . . . . . . . . . . . with respect to
2 
The Wasserstein Metric 
In this section, we outline basic properties of the Wasserstein distance. A definition in the case of discrete measures is provided in Section 2.1. Section 2.2 establishes that it is a proper distance metric. A dual formulation and a generalization to arbitrary measures are presented in Section 2.3. Special cases are described in Section 2.4. A discussion on how to set the Wasserstein underlying transport cost function in the context of robust learning is in Section 2.5. A related robustnessinducing property of the Wasserstein metric is shown in Section 2.6 and a discussion on how to set the radius of the Wasserstein ambiguity set is included in Section 2.7. 
2.1 Basics 
We start by reviewing basic properties of the Wasserstein metric defined in Section 1 (cf. Eq. (1.7)). We will define the metric and establish key results, first using discrete probability distributions, and then state how the definitions and results generalize to arbitrary probability measures. 
Consider two discrete probability distributions P = {p1, . . . , pm} and Q = {q1, . . . , qn}, where pi, qj ≥ 0, for all i, j, and ∑m 
i=1 pi = ∑n j=1 qj = 
1. For convenience, let us write p = (p1, . . . , pm) and q = (q1, . . . , qn) 
21
22 The Wasserstein Metric 
for the corresponding column vectors. Define a metric (cost) between points in the support of P and Q by s(i, j), i ∈ JmK, j ∈ JnK, and collect all these quantities in an m×n matrix S = (s(i, j)) whose (i, j) element is s(i, j). Consider the Linear Programming (LP) problem: 
WS,1(P,Q) = minπ ∑m i=1 
∑n j=1 π(i, j)s(i, j) 
s.t. ∑m i=1 π(i, j) = qj , j ∈ JnK,∑n j=1 π(i, j) = pi, i ∈ JmK, 
π(i, j) ≥ 0, ∀i, j, 
(2.1) 
where π = (π(i, j); ∀i, j) is the decision vector. Notice that according to the definition in Eq. (1.7), the objective value is the order-1 Wasser-stein distance between distributions P and Q. In WS,1(P,Q) we have inserted the subscript S to explicitly denote the dependence on the cost matrix. Similarly, by defining a cost matrix St = ((s(i, j))t), the order-t Wasserstein distance, denoted by WS,t(·, ·), can be obtained as the t-th root of the optimal value of the same LP with cost matrix St; namely, 
WS,t(P,Q) = ( WSt,1(P,Q) 
)1/t . (2.2) 
The LP formulation in (2.1) is equivalent to the well-known transportation problem (Bertsimas and Tsitsiklis, 1997) and can be interpreted as the cost of transporting probability mass from the support points of P to those of Q. Specifically, the problem corresponds to the bipartite graph in Figure 2.1 with nodes {u1, . . . , um} representing the support of P, nodes {v1, . . . , vn} representing the support of Q, pi being the supply at node ui, qj the demand at node vj , and π(i, j) the flow of material (probability mass) from node ui to node vj incurring a transportation cost of s(i, j) per unit of material. 
The formulation in (2.1) has a long history, starting with Monge (Monge, 1781) who formulated a problem of optimally transferring material extracted from a mining site to various construction sites; hence, the terms optimal mass transport and earth mover’s distance. In Monge’s formulation, all material from a source node ui gets “assigned” to a destination node vj . Kantorovich (Kantorovich, 1942; Kantorovich, 1948) relaxed the problem by allowing sources to split their material to several destination nodes. For Kantorovich, this was an application of an LP he had earlier defined for production planning problems (Kantorovich, 1939,
2.2. A Distance Metric 23 
pi 
... 
... 
... 
... 
p1 
si,j 
pm qn 
qj 
q1 u1 
ui 
um 
v1 
vj 
vn 
Figure 2.1: The transportation problem for computing the Wasserstein distance WS,1(P,Q). 
later translated in English in Kantorovich, 1960) and a method (and a duality theorem) he had developed for these problems (Kantorovich, 1940). Definitive references on optimal mass transport are Villani, 2008, and, focusing more on computational aspects, Peyré and Cuturi, 2019. In presenting some of the key properties and duality we will follow the approach of Peyré and Cuturi, 2019 which presents the theory for discrete probability distributions. 
2.2 A Distance Metric 
In this section we establish that the Wasserstein distance WS,t(P,Q) is a distance metric, assuming that the underlying cost s(i, j) is a proper distance metric. 
Assumption A. Let n = m and assume 
1. s(i, j) ≥ 0, with s(i, j) = 0 if and only if i = j. 
2. s(i, j) = s(j, i) for i 6= j. 
3. For any triplet i, j, k ∈ JnK, s(i, k) ≤ s(i, j) + s(j, k). 
Theorem 2.2.1. Under Assumption A, the order-tWasserstein distance (t ≥ 1) is a metric, i.e., 
1. WS,t(P,Q) ≥ 0 for any P,Q ∈ P(JnK), with WS,t(P,Q) = 0 if and only if P = Q.
24 The Wasserstein Metric 
2. WS,t(P,Q) = WS,t(Q,P) for any P,Q ∈ P(JnK). 
3. For any triplet P,Q,V ∈ P(JnK), WS,t(P,V) ≤ WS,t(P,Q) + WS,t(Q,V). 
Proof. Recall Eq. (2.2) that relates WS,t(P,Q) to WSt,1(P,Q). The latter quantity can be obtained as the optimal value of the LP in (2.1) using the cost metric St. 
1. The non-negativity follows directly from the formulation in (2.1) since s(i, j) ≥ 0 (by Assumption A), hence (s(i, j))t ≥ 0, and any feasible solution satisfies π(i, j) ≥ 0. In addition, WS,t(P,P) = 0, because, in this case, the optimal solution in formulation (2.1) satisfies π(i, j) = 0, if i 6= j, and π(i, i) = pi, for all i. Since (s(i, i))t = 0 (due to Assumption A), the optimal value of the LP in (2.1) is zero. Further, if P 6= Q, there should be flow π(i, j) > 0 for some i 6= j, and since s(i, j) > 0 for those i, j (due to Assumption A), the optimal value of the LP is positive. 
2. To establish symmetry, consider WS,t(P,Q) and compare it with WS,t(Q,P). It suffices to compare WSt,1(P,Q) with WSt,1(Q,P). To that end, notice that given an optimal solution πf (i, j), for all i, j, for WSt,1(P,Q) computed from the LP in (2.1), we can obtain an optimal solution πb(i, j) for WSt,1(Q,P) simply by reversing the flows, i.e., πb(j, i) = πf (i, j), for all i, j. Given the symmetry of the cost s(i, j) due to Assumption A, the result follows. 
3. To establish the triangle inequality, fix P,Q,V ∈ P(JnK) and consider WS,t(P,Q) and WS,t(Q,V). Let Π1 = (π1(i, j))i,j∈JnK and Π2 = (π2(i, j))i,j∈JnK be the optimal solutions of the LPs corresponding toWSt,1(P,Q) andWSt,1(Q,V), respectively. Define a Q̃ such that q̃i = qi, if qi > 0, and q̃i = 1, otherwise. Let q̃ be the corresponding column vector. Define D = diag(1/q̃1, . . . , 1/q̃n). Consider nextWS,t(P,V) and the LP corresponding toWSt,1(P,V). We will first argue that Π1,2 
4= Π1DΠ2 forms a feasible solution to that LP. Specifically, recalling that e is the vector of all ones, 
Π1,2e = Π1DΠ2e = Π1Dq = Π1eQ = p,
2.2. A Distance Metric 25 
where we used the feasibility of Π1,Π2, and eQ is a vector whose ith element is set to 1 if qi > 0, and to zero, otherwise. Similarly, we can also show e′Π1,2 = v′, where v is the column vector corresponding to V. Letting Π1,2 = (π1,2(i, j))i,j∈JnK, we have 
WS,t(P,V) = (WSt,1(P,V))1/t 
≤ (∑ 
i,j (s(i, j))tπ1,2(i, j) 
)1/t (2.3) 
= (∑ 
i,j (s(i, j))t 
∑ k 
π1(i, k)π2(k, j) q̃k 
)1/t 
≤ (∑ 
i,j,k (s(i, k) + s(k, j))tπ1(i, k)π2(k, j) 
q̃k 
)1/t (2.4) 
= (∑ 
i,j,k 
[ s(i, k) 
( π1(i, k)π2(k, j) 
q̃k 
)1/t 
+ s(k, j) ( π1(i, k)π2(k, j) 
q̃k 
)1/t]t1/t 
≤ (∑ 
i,j,k (s(i, k))tπ1(i, k)π2(k, j) 
q̃k 
)1/t 
+ (∑ 
i,j,k (s(k, j))tπ1(i, k)π2(k, j) 
q̃k 
)1/t (2.5) 
= (∑ 
i,k (s(i, k))tπ1(i, k) 
∑ j 
π2(k, j) q̃k 
)1/t 
+ (∑ 
j,k (s(k, j))tπ2(k, j) 
∑ i 
π1(i, k) q̃k 
)1/t 
= (∑ 
i,k (s(i, k))tπ1(i, k) 
)1/t + (∑ 
j,k (s(k, j))tπ2(k, j) 
)1/t 
(2.6) =WS,t(P,Q) +WS,t(Q,V), 
where (2.3) follows from the feasibility (and potential suboptimality) of π1,2(i, j), (2.4) follows from the triangle inequality for s(i, j), (2.5) is due to the Minkowski inequality, and (2.6) uses
26 The Wasserstein Metric 
the feasibility of Π1,Π2. 
As a final comment in this section, we note that the order-1 Wasser-stein distance WS,1(P,Q), viewed as a function of the vectors p and q corresponding to P and Q, is a convex function. This follows from the LP formulation (2.1), where the optimal value is a convex function of the RHS of the constraints (Bertsimas and Tsitsiklis, 1997, Sec. 5.2). 
2.3 The Dual Problem 
In this section, we derive the dual of the mass transportation problem in (2.1). Let fj be the dual variable corresponding to the flow conservation constraint for qj and gi the dual variable corresponding to the flow conservation constraint for pi. We write f ∈ Rn and g ∈ Rm for the corresponding dual vectors. Using LP duality, the dual of (2.1) takes the form: 
WS,1(P,Q) = maxf ,g ∑m i=1 gipi +∑n 
j=1 fjqj s.t. fj + gi ≤ s(i, j), i ∈ JmK, j ∈ JnK. 
(2.7) 
The optimal value is equal to the primal optimal value due to the LP strong duality. The complementary slackness conditions suggest that 
if π(i, j) > 0 then fj + gi = s(i, j). (2.8) 
Necessary and sufficient conditions for a primal solution Π to be primal optimal and dual solutions f and g to be dual optimal are: (i) primal feasibility, (ii) dual feasibility, and (iii) the complementary slackness condition in (2.8). 
The primal and dual problems can be interpreted as follows. The primal problem is the problem of minimizing transportation cost for a transporter of mass across the bipartite graph in Figure 2.1. The transporter faces a cost of s(i, j) per unit of mass transported on link (i, j). Suppose now that the transporter, instead of carrying out the transportation plan, hires another shipping company (e.g., a company like UPS, DHL, or Fedex). This shipping company charges a price of gi for picking one unit of mass from node ui and a price of fj for delivering
2.3. The Dual Problem 27 
one unit of mass to node vj . The dual problem is then the problem solved by the shipping company to maximize its revenue by carrying out the transportation of mass. Strong duality simply states that there should not be an “arbitrage” opportunity and the transportation cost must be the same irrespective of whether the transporter of mass hires a shipping company or not. In other words, if the price offered by the shipping company was strictly less than the transportation cost, then the mass transporter would be able to make money just by outsourcing shipping. Furthermore, the market conditions would be ripe for another middleperson to come into the market, offer the shipping company higher prices, while still making it profitable for the transporter to use the middleperson’s services. More specifically, the complementary slackness conditions (2.8) suggest that if there is mass transported along link (i, j), the cost of transporting the mass through the shipping company must equal the transportation cost faced by the transporter across that link. 
A different interpretation of the primal and the dual can be obtained through an analogy with electrical circuits. Let us treat pi as current flowing into node ui. Similarly, qj is current flowing out of node vj , or, equivalently, the inflow into vj is equal to q̂j = −qj . Rewriting the dual problem (2.7) using the q̂i’s and changing variables from fj to f̂j = −fj yields: 
WS,1(P,Q) = maxf̂ ,g ∑m i=1 gipi +∑n 
j=1 f̂j q̂j 
s.t. gi − f̂j ≤ s(i, j), i ∈ JmK, j ∈ JnK. (2.9) 
In this context, the constraints of the primal can be viewed as Kirchoff’s current law and the dual variables (gi at nodes ui and f̂j at nodes vj) can be interpreted as electric potentials (voltages with respect to the ground) at the nodes. The complementary slackness conditions state that if there is current flowing from node ui to vj , the voltage, or potential difference among these nodes, must equal s(i, j). More simply put, for one unit of flow (current), the voltage must be equal to the “resistor” s(i, j), which corresponds to Ohm’s law. These node potentials are known as Kantorovich potentials (Peyré and Cuturi, 2019).
28 The Wasserstein Metric 
2.3.1 Arbitrary Measures and Kantorovich Duality 
The primal problem we defined in (2.1) can be generalized to arbitrary measures as defined in Eq. (1.7). Consider two Polish (i.e., complete, separable, metric) probability spaces (Z1,P) and (Z2,Q) and a lower semicontinuous cost function s : Z1 × Z2 → R ∪ {+∞}. Then, the order-1 Wasserstein distance can be defined as the optimal value of the primal problem: 
Ws,1(P,Q) = min π 
∫ Z1×Z2 
s(z1, z2)dπ(z1, z2), (2.10) 
where π ∈ P(Z1 ×Z2) is a joint probability distribution of z1, z2 with marginals P and Q. The order-t Wasserstein distance can be obtained as: 
Ws,t(P,Q) = ( Wst,1(P,Q) 
)1/t , (2.11) 
where st(z1, z2) = (s(z1, z2))t. The dual problem, known as the Kantorovich dual (Villani, 2008, 
Thm. 5.10), analogously to Problem (2.7) can be written as: 
Ws,1(P,Q) = sup f,g 
∫ Z1 g(z1)dP(z1) + 
∫ Z2 f(z2)dQ(z2) 
s.t. f(z2) + g(z1) ≤ s(z1, z2), z1 ∈ Z1, z2 ∈ Z2, (2.12) 
where f and g are absolutely integrable under Q and P, respectively. By the Kantorovich-Rubinstein Theorem (Villani, 2008), when s(z1, z2) is a distance metric on a Polish space Z1, (2.12) can be simplified to 
Ws,1(P,Q) = sup g 
∫ Z1 g(z1)dP(z1)− 
∫ Z2 g(z2)dQ(z2) 
s.t. |g(z1)− g(z2)| ≤ s(z1, z2), z1 ∈ Z1, z2 ∈ Z2. (2.13) 
2.4 Some Special Cases 
2.4.1 One-Dimensional Cases 
Suppose P and Q are discrete distributions on R. Let P have mass of 1/n at each of the points xi ∈ R, i ∈ JnK, where x1 ≤ x2 ≤ · · · ≤ xn. Similarly, Q assigns mass of 1/n at each of the points yi ∈ R, i ∈ JnK,
2.4. Some Special Cases 29 
where y1 ≤ y2 ≤ · · · ≤ yn. Then, with s(x, y) = |x − y|, the order-t Wasserstein distance can be obtained as: 
Ws,t(P,Q) = ( 1 n 
∑n 
i=1 |xi − yi|t 
)1/t . (2.14) 
This can be easily obtained by solving the corresponding formulation in (2.1). 
For continuous one-dimensional distributions on R, let FP denote the Cumulative Distribution Function (CDF) of P, namely, 
FP(x) = ∫ x 
−∞ dP, x ∈ R. 
Define the inverse CDF or quantile function F−1 P (p) as 
F−1 P (p) = min{x ∈ R ∪ {−∞} : FP(x) ≥ p}, p ∈ [0, 1]. 
Let FQ and F−1 Q be the corresponding quantities for Q. Then, using 
again the metric s(x, y) = |x− y|, for x, y ∈ R, the order-t Wasserstein distance can be computed as (Peyré and Cuturi, 2019): 
Ws,t(P,Q) = (∫ 1 
0 
∣∣∣F−1 P (p)− F−1 
Q (p) ∣∣∣tdp)1/t 
. (2.15) 
2.4.2 Sliced Wasserstein Distance 
The fact that Wasserstein distances can be easily computed for onedimensional distributions on R has led to the following approximation of the Wasserstein distance between distributions P and Q on Rd. Specifically, for any direction θ on the ball Sd = {θ ∈ Rd : ‖θ‖2 = 1}, let Tθ : x ∈ Rd → R be the projection from Rd to R. Let Tθ,#P be the so-called push-forward measure satisfying 
Tθ,#P(A) = P({x ∈ Rd : Tθ(x) ∈ A}), A ⊆ R. 
Define Tθ,#Q similarly. Then, the so-called sliced Wasserstein distance (Bonneel et al., 2015; Liutkus et al., 2019) can be defined as: 
SWs,2 = ∫ Sd Ws,2(Tθ,#P, Tθ,#Q)dθ, (2.16)
30 The Wasserstein Metric 
where s(x, y) = |x− y|, for x, y ∈ R. Such an integral can be approximated using Monte-Carlo integration, giving rise to a computational method for computing Wasserstein distances between distributions in Rd. 
2.4.3 Gaussian Distributions 
We next consider the case of two Gaussian distributions. Let P ∼ N (µ1,Σ1) be a d-dimensional Gaussian distribution with mean µ1 and covariance Σ1. Similarly, let Q ∼ N (µ2,Σ2). Define the metric s(x1,x2) = ‖x1−x2‖2. Then, the order-2 Wasserstein distance between P and Q is given in closed-form by (Delon and Desolneux, 2020; Dowson and Landau, 1982): 
Ws,2(P,Q) = ‖µ1 − µ2‖22 + tr ( 
Σ1 + Σ2 − 2 ( Σ1/2 
1 Σ2Σ1/2 1 
)1/2 ) . 
2.5 The Transport Cost Function 
In this monograph, we are focusing on the use of the Wasserstein metric in the context of robust learning, specifically the DRO problem we defined in Eq. (1.5). As a result, the cost function s used in defining the Wasserstein metric should reflect any implicit knowledge we have on the nature of the data z = (x, y). Without loss of generality, suppose that the data have already been standardized, specifically, for all data points zi = (xi, yi), i ∈ JNK, in the training set, we have normalized every variable (coordinate) in xi by subtracting the empirical mean and dividing by the sample standard deviation. Then, an element of xi will have a large absolute value if the corresponding variable deviates substantially from the empirical mean. Below, we discuss a number of different scenarios on what may be known regarding the data and the implied appropriate corresponding cost function. 
1. Suppose we know that the model we are seeking is sparse, i.e., there are few variables, and in the extreme case one, that determine the output y. In this case, an appropriate cost function is an `∞ norm in the z = (x, y) space. In particular, given two data points z1 =
2.5. The Transport Cost Function 31 
(x1, y1) and z2 = (x2, y2), if y1 6= y2 and ‖x1 − x2‖∞ < |y1 − y2|, the distance between z1 and z2 is equal to |y1 − y2|. If, however, y1 ≈ y2, then the distance between z1 and z2 is determined by the absolute difference in the most deviating variable, that is, ‖x1 − x2‖∞. 
2. Suppose now that we believe the model to be dense, implying that almost all variables are relevant and predictive of the output y. Then, an appropriate distance metric between two points z1 = (x1, y1) and z2 = (x2, y2) is the `2 norm ‖z1 − z2‖2, where all x coordinates and y are weighted equally. More generally, one can introduce weights and use a W-weighted `p norm defined as ‖z‖Wp = 
( (|z|p/2)′W|z|p/2 
)1/p with a positive definite weight 
matrix W. 
3. As one more example, suppose that the data z are organized into a set of (overlapping or non-overlapping) groups according to z = (z1, . . . , zL). To reflect this group structure, we can define a (q, t)-norm, with q, t ≥ 1, as: 
‖z‖q,t = (∑L 
l=1 
( ‖zl‖q 
)t)1/t . 
Notice that the (q, t)-norm of z is actually the `t-norm of the vector (‖z1‖q, . . . , ‖zL‖q), which represents each group vector zl in a concise way via the `q-norm. A special case is the (2,∞)-norm on the weighted predictor-response vector 
zw , 
( 1 √ p1 
x1, . . . , 1 √ pL 
xL,My 
) , 
where the weight vector is 
w = ( 
1 √ p1 , . . . , 
1 √ pL ,M 
) , 
and M is a positive weight assigned to the response. Specifically, 
‖zw‖2,∞ = max { 
1 √ p1 ‖x1‖2, . . . , 
1 √ pL ‖xL‖2,M |y| 
} ,
32 The Wasserstein Metric 
where different groups are scaled by the number of variables they contain. The `2 norm at the individual group level reflects the intuition that all variables in a group are relevant, whereas the `∞ norm among groups reflects the intuition that there is a dominant group predictive of the response, just like the situation we outlined in Item 1 above. As we will see later, such a norm imposes a group sparsity structure. 
2.5.1 Transport Cost Function via Metric Learning 
We now discuss a metric learning approach for determining the weighted transport cost function we outlined in Item 2 above, following the line of work in Blanchet et al., 2019c. The intuition is to calibrate a cost function s(·) which assigns a high transportation cost to a pair of data points (z1, z2) if transporting mass between these locations significantly impacts the performance. 
Consider a classification problem where we observe N (predictor, label) pairs {(x1, y1), . . . , (xN , yN )}, and yi ∈ {−1,+1}. Suppose we use a weighted `2 norm as the distance metric on the space of predictors: 
sW(x1,x2) = √ 
(x1 − x2)′W(x1 − x2), 
where the weight matrix W is symmetric and positive semi-definite. The goal is to inform the selection of W through recognizing the pairs of samples that are similar/dissimilar to each other. In a classification setting, the labels form a natural separation plane for the observed samples. We define two sets: 
M , { 
(i, j) : xi and xj are close to each other and yi = yj } , 
N , { 
(i, j) : xi and xj are far away from each other } , 
where the closeness between x can be evaluated using an appropriate norm, e.g., the `2 norm. xi and xj are considered to be close if one is among the k nearest neighbors of the other, in the sense of the `2 norm, with k being pre-specified. We aim to automatically determine the weight W in a data-driven fashion through minimizing the distances
2.5. The Transport Cost Function 33 
on the set M and maximizing the distances on N , which yields the following Absolute Metric Learning formulation: 
min W<0 
∑ (i,j)∈M 
s2 W(xi,xj) 
s.t. ∑ (i,j)∈N 
s2 W(xi,xj) ≥ 1. (2.17) 
A slightly different formulation considers the relative distance between predictors. Define a set 
T , { 
(i, j, k) : sW(xi,xj) should be smaller than sW(xi,xk) } , 
where sW(xi,xj) is considered to be smaller than sW(xi,xk) if any of the following holds: 
1. yi = yj and yi 6= yk; 
2. yi = yj = yk and ‖xi − xj‖2 < ‖xi − xk‖2; 
3. yi 6= yj and yi 6= yk and ‖xi − xj‖2 < ‖xi − xk‖2. 
The Relative Metric Learning formulation minimizes the difference of distances on these triplets: 
min W<0 
∑ (i,j,k)∈T 
max ( s2 W(xi,xj)− s2 
W(xi,xk) + 1, 0 ) . (2.18) 
To hedge against potential noise in the predictors, Blanchet et al., 2019c proposed to robustify (2.17) and (2.18) using robust optimization, and learn a robust data-driven transport cost function. Specifically, for the absolute metric learning formulation, suppose the setsM and N are noisy or inaccurate at level α, i.e., α · 100% of their elements are incorrectly assigned. We construct robust uncertainty sets W(α) and V(α) as follows: 
W(α) = { η = (ηi,j ; (i, j) ∈M) : 0 ≤ ηi,j ≤ 1,∑ 
(i,j)∈M ηi,j ≤ (1− α)|M| 
} , 
V(α) = { ξ = (ξi,j ; (i, j) ∈ N ) : 0 ≤ ξi,j ≤ 1, 
∑ (i,j)∈N 
ξi,j ≥ (1−α)|N | } .
34 The Wasserstein Metric 
We then formulate the robust counterpart of the Absolute Metric Learn-ing formulation (2.17) as: 
min W<0 
max λ≥0 
max η∈W(α) ξ∈V(α) 
[ ∑ (i,j)∈M 
ηi,js 2 W(xi,xj) 
+λ ( 1− ∑ 
(i,j)∈N ξi,js 
2 W(xi,xj) 
)] , 
(2.19) 
where we robustify the Lagrangian dual problem of (2.17), which is formed by bringing the constraint into the objective function via a dual variable λ, using uncertain parameters η and ξ. Similarly, for the relative metric learning formulation, suppose the set T is inaccurate at level α, the robust counterpart of the Relative Metric Learning formulation (2.18) can be formulated as: 
min W<0 
max q∈Q(α) 
∑ (i,j,k)∈T 
qi,j,k max ( s2 W(xi,xj)− s2 
W(xi,xk) + 1, 0 ) , 
(2.20) where the uncertainty set Q(α) is defined as: 
Q(α) = { q = (qi,j,k; (i, j, k) ∈ T ) : 0 ≤ qi,j,k ≤ 1,∑ 
(i,j,k)∈T qi,j,k ≤ (1− α)|T | 
} . 
For solving the robust optimization problems (2.19) and (2.20), we refer the reader to Blanchet et al., 2019c for a sequential iterative algorithm that alternates between optimizing over the weight matrix W and the uncertain parameters η, ξ (or q). 
2.6 Robustness of the Wasserstein Ambiguity Set 
The ultimate goal of using DRO is to eliminate the effect of perturbed samples and produce an estimator that is consistent with the underlying true (clean) distribution. When the data z = (x, y) are corrupted by outliers, the observed samples are not representative enough to encode the true underlying uncertainty of the data. Instead of equally weighting all the samples as in the empirical distribution, we may wish to include
2.6. Robustness of the Wasserstein Ambiguity Set 35 
more informative distributions that “drive out” the corrupted samples. DRO realizes this through hedging the expected loss against a family of distributions that include the true data-generating mechanism with a high confidence. In this section, we will provide evidence on the robustness of DRO under the Wasserstein metric, by showing that the ambiguity set defined via the Wasserstein metric is able to retain the good (clean) distribution while excluding the bad (outlying) one; thus, producing an estimator that is robust to outliers. 
We make the assumption that the training data (x, y) are drawn from a mixture of two distributions, with probability q from the outlying distribution Pout and with probability 1− q from the true (clean) distribution P. All the N training samples (xi, yi), i ∈ JNK, are independent and identical realizations of (x, y). Recall that P̂N is the discrete uniform distribution over the N samples. We claim that when q is small, if the Wasserstein ball radius ε is chosen judiciously, the true distribution P will be included in the ε-Wasserstein ball Ω (cf. (1.6)) 
Ω = {Q ∈ P(Z) : Ws,1(Q, P̂N ) ≤ ε}, 
while the outlying distribution Pout will be excluded. Theorem 2.6.1 proves this claim. 
Theorem 2.6.1. Suppose we are given two probability distributions P and Pout, and the mixture distribution Pmix is a convex combination of the two: Pmix = qPout + (1− q)P. Then, for any cost function s, 
Ws,1(Pout,Pmix) Ws,1(P,Pmix) = 1− q 
q . 
Proof. As we indicated in Section 1, and for ease of notation, we will suppress the dependence of Ws,1 on the cost metric s. In addition, without loss of generality, we will assume that the probability distributions P, Pout, Pmix, and any joint distributions have densities. From the definition of the Wasserstein distance, W1(Pout,Pmix) is the optimal
36 The Wasserstein Metric 
value of the following optimization problem: 
min π∈P(Z×Z) 
∫ Z×Z 
s(z1, z2) dπ ( z1, z2 
) s.t. 
∫ Z π ( z1, z2 
) dz2 = Pout(z1), ∀z1 ∈ Z,∫ 
Z π ( z1, z2 
) dz1 = qPout(z2) + (1− q)P(z2), ∀z2 ∈ Z. 
(2.21) Similarly, W1(P,Pmix) is the optimal value of the following optimization problem: 
min π∈P(Z×Z) 
∫ Z×Z 
s(z1, z2) dπ ( z1, z2 
) s.t. 
∫ Z π ( z1, z2 
) dz2 = P(z1), ∀z1 ∈ Z,∫ 
Z π ( z1, z2 
) dz1 = qPout(z2) + (1− q)P(z2), ∀z2 ∈ Z. 
(2.22) We propose a decomposition strategy. For Problem (2.21), decom-
pose the joint distribution π as π = (1− q)π1 + qπ2, where π1 and π2 are two joint distributions of z1 and z2. The first set of constraints in Problem (2.21) can be equivalently expressed as: 
(1− q) ∫ Z π1 ( z1, z2 
) dz2 + q 
∫ Z π2 ( z1, z2 
) dz2 
= (1− q)Pout(z1) + qPout(z1), ∀z1 ∈ Z, 
which is satisfied if∫ Z π1 ( z1, z2 
) dz2 = Pout(z1), 
∫ Z π2 ( z1, z2 
) dz2 = Pout(z1), ∀z1 ∈ Z. 
The second set of constraints can be expressed as: 
(1− q) ∫ Z π1 ( z1, z2 
) dz1 + q 
∫ Z π2 ( z1, z2 
) dz1 
= qPout(z2) + (1− q)P(z2), ∀z2 ∈ Z, 
which is satisfied if∫ Z π1 ( z1, z2 
) dz1 = P(z2), 
∫ Z π2 ( z1, z2 
) dz1 = Pout(z2), ∀z2 ∈ Z.
2.6. Robustness of the Wasserstein Ambiguity Set 37 
The objective function can be decomposed as:∫ Z×Z 
s(z1, z2) dπ ( z1, z2 
) = (1− q) 
∫ Z×Z 
s(z1, z2) dπ1 ( z1, z2 
) + q 
∫ Z×Z 
s(z1, z2)dπ2 ( z1, z2 
) . 
Therefore, Problem (2.21) can be decomposed into the following two subproblems. 
Subproblem 1: min 
π1∈P(Z×Z) 
∫ Z×Z s(z1, z2) dπ1 
( z1, z2 
) s.t. 
∫ Z π1 
( z1, z2 
) dz2 = Pout(z1), ∀z1 ∈ Z,∫ 
Z π1 ( z1, z2 
) dz1 = P(z2), ∀z2 ∈ Z. 
Subproblem 2: min 
π2∈P(Z×Z) 
∫ Z×Z s(z1, z2) dπ2 
( z1, z2 
) s.t. 
∫ Z π2 
( z1, z2 
) dz2 = Pout(z1), ∀z1 ∈ Z,∫ 
Z π2 ( z1, z2 
) dz1 = Pout(z2), ∀z2 ∈ Z. 
Assume that the optimal solutions to the two subproblems are π∗1 and π∗2, respectively. We know π0 = (1− q)π∗1 + qπ∗2 is a feasible solution to Problem (2.21). Therefore, 
W1(Pout,Pmix) ≤ ∫ Z×Z 
s(z1, z2) dπ0 ( z1, z2 
) = (1− q)W1(Pout,P) + qW1(Pout,Pout) = (1− q)W1(Pout,P). 
(2.23) 
Similarly, W1(P,Pmix) ≤ qW1(Pout,P). (2.24) 
(2.23) and (2.24) imply that 
W1(Pout,Pmix) +W1(P,Pmix) ≤W1(Pout,P). 
On the other hand, using the triangle inequality for the Wasserstein metric, we have, 
W1(Pout,Pmix) +W1(P,Pmix) ≥W1(Pout,P). 
We thus conclude that 
W1(Pout,Pmix) +W1(P,Pmix) = W1(Pout,P). (2.25)
38 The Wasserstein Metric 
To achieve the equality in (2.25), (2.23) and (2.24) must be equalities, i.e., 
W1(Pout,Pmix) = (1− q)W1(Pout,P), 
and, W1(P,Pmix) = qW1(Pout,P). (2.26) 
Thus, W1(Pout,Pmix) W1(P,Pmix) = (1− q)W1(Pout,P) 
qW1(Pout,P) = 1− q q 
. 
2.7 Setting the Radius of the Wasserstein Ball 
Pout 
P 
ε Pmix 
Ω 
Pout 
ε 
P 
Ω Pmix 
Figure 2.2: Left: Training with a contaminated training set drawn from Pmix. Right: Training with a pure training set drawn from P. 
Theorem 2.6.1 provides some guidance on setting the radius ε of the Wasserstein ball Ω. Figure 2.2 (Left) provides a graphical interpretation. As seen in the figure, the ball Ω is centered at Pmix because we assume that the training set is drawn from this distribution. According to Theorem 2.6.1, when q < 0.5 we haveW1(P,Pmix) ≤ ε < W1(Pout,Pmix). Thus, for a large enough sample size (so that P̂N is a good approximation of Pmix), the set Ω will include the true distribution and exclude the outlying one, which provides protection against these outliers. 
To provide numerical evidence, consider a simple example where P is a discrete distribution that assigns equal probability to 10 data points equally spaced between 0.1 and 1, and Pout assigns probability 0.5 to two data points 1 and 2. We generate 100 samples and plot the
2.7. Setting the Radius of the Wasserstein Ball 39 
order-1 Wasserstein distances from P̂N for both P and Pout, under the distance metric s(z1, z2) = |z1−z2|. From Figure 2.3 we observe that for 
Figure 2.3: The order-1 Wasserstein distances from the empirical distribution. 
q below 0.5, the true distribution P is closer to P̂N whereas the outlying distribution Pout is further away. If the radius ε is chosen between the red (∗−) and blue (◦−) lines, the Wasserstein ball that we are hedging against will exclude the outlying distribution and the resulting estimator will be robust to the perturbations. Moreover, as q becomes smaller, the gap between the red and blue lines becomes larger. One implication from this observation is that as the data becomes purer, the radius of the Wasserstein ball tends to be smaller, and the confidence in the observed samples is higher. For large q values, the DRO formulation seems to fail. However, as outliers are defined to be the data points that do not conform to the majority of data, if q > 0.5 then Pout becomes the distribution of the majority and data generated from P can be treated as outliers. Thus, without loss of generality, we can safely treat Pout as the distribution of the minority and assume q is always below 0.5. 
An alternative use of the DRO learning approach can be seen in Figure 2.2 (Right). Here, we assume that the training set is pure, thus, given enough samples, the empirical distribution on which the ball Ω is centered is close to P. Consider applying the model to a test set which is contaminated with outliers. Notice from the proof of Theorem 2.6.1
40 The Wasserstein Metric 
that W1(P,Pmix) = qW1(Pout,P) (cf. Eq. (2.26)). This implies that the smaller q is, and for a properly selected ε, the distribution from which the test set is drawn (Pmix) is within the ball Ω and the model has the potential to generalize well in the test set, tolerating some outliers. In contrast, the outlying distribution Pout lies outside the set Ω, which suggests that the model does not “adjust” to samples generated from Pout. According to this reasoning, and based on Eq. (2.26), ε should be set so that qW1(Pout,P) < ε < W1(Pout,P). 
The above discussions provide some insights on the optimal selection of the radius, but could be hard to implement due to the unknown P and Pout. In practice cross-validation is usually adopted, but could be computationally expensive. In the next two subsections we discuss two practical radius selection approaches that produce the smallest Wasser-stein ball which contains the true distribution with high confidence. 
2.7.1 Measure Concentration 
In this subsection we study an optimal radius selection method that originates from the measure concentration theory. As will be seen in Section 3.4, it leads to an asymptotic consistent DRO estimator that generalizes well out-of-sample. 
Suppose zi, i ∈ JNK, are N realizations of z which follows an unknown distribution P∗. One of the prerequisites for ensuring a good generalization performance of Wasserstein DRO requires that the ambiguity set Ωε(P̂N ) includes the true data distribution P∗. This implies that the radius ε should be chosen so that 
Ws,1(P∗, P̂N ) ≤ ε. (2.27) 
A measure concentration result developed in Fournier and Guillin, 2015, which characterizes the rate at which the empirical distribution P̂N converges to the true distribution P∗ in the sense of the Wasserstein metric, can be used as a guidance on the optimal selection of the radius for the Wasserstein ambiguity set. In the following discussion we assume s is a norm, and the true data distribution P∗ satisfies the light tail condition stated in Assumption B.
2.7. Setting the Radius of the Wasserstein Ball 41 
Assumption B (Light-tailed distribution). There exists an exponent a > 1 such that 
A , EP∗[ exp (‖z‖a) ] 
= ∫ Z 
exp (‖z‖a)dP∗(z) <∞. (2.28) 
Theorem 2.7.1 (Measure concentration; Fournier and Guillin, 2015, The-orem 2). Suppose the Wasserstein metric is induced by some norm ‖ · ‖, i.e., s(z1, z2) = ‖z1 − z2‖. Under Assumption B, we have 
PN ( Ws,1(P∗, P̂N ) ≥ ε 
) ≤ 
c1 exp ( − c2Nε 
max(d,2)), if ε ≤ 1, c1 exp 
( − c2Nε 
a ) , if ε > 1, 
(2.29) 
for all N ≥ 1, d 6= 2, and ε > 0, where N is the size of the observed training set, d is the dimension of z, a is defined in (2.28), and c1, c2 are positive constants that only depend on a,A, and d. 
From Theorem 2.7.1 we can derive the smallest possible ε so that the true distribution is contained in the Wasserstein ambiguity set with high confidence. Given some prescribed α ∈ (0, 1), it is desired that 
PN ( Ws,1(P∗, P̂N ) ≤ ε 
) ≥ 1− α. 
Equating the RHS of (2.29) to α and solving for ε yields 
εN (α) = 
 ( 
log(c1α−1) c2N 
)1/max(d,2) , if N ≥ log(c1α−1) 
c2 ,( 
log(c1α−1) c2N 
)1/a , if N < log(c1α−1) 
c2 . 
(2.30) 
Notice that Eq. (2.30) depends on the unknown constants c1 and c2, and does not make use of the available training data, which could potentially result in a conservative estimation of the radius and is not of practical use (Esfahani and Kuhn, 2018). By recognizing these issues, some researchers have proposed to choose the radius without relying on exogenous constants, see Ji and Lejeune, 2018; Zhao and Guan, 2015. 
By using an extension of Sanov’s theorem which identifies the rate function, in the form of the KL divergence, for large deviations of the empirical measure from the true measure (Sanov, 1958), Ji and Lejeune, 2018 derived a closed-form expression for computing the size of the Wasserstein ambiguity set, when the support of z is finite and bounded,
42 The Wasserstein Metric 
and the true distribution is discrete. The reason for restricting to a discrete true distribution lies in that the convergence rate of the empirical measure (in the sense of the Wasserstein distance) is characterized by the KL divergence (Wang et al., 2010), which diverges when the true distribution P∗ is continuous, and the empirical distribution P̂N is discrete. 
Theorem 2.7.2 (Ji and Lejeune, 2018, Theorem 2). Suppose the random vector z is supported on a finite Polish space (Z, s), and is distributed according to a discrete true distribution P∗. Assume there exists some z0 ∈ Z such that the following condition holds: 
log ∫ Z 
exp (as(z, z0))dP∗(z) <∞, ∀a > 0. (2.31) 
Define B as the diameter of the d-dimensional compact set Z: 
B , sup{s(z1, z2) : z1, z2 ∈ Z}. (2.32) 
Construct an empirical distribution P̂N based on N i.i.d. samples of z. A lower bound on the probability that the Wasserstein distance between the empirical distribution P̂N and the true distribution P∗ does not exceed ε is given by: 
PN ( Ws,1(P∗, P̂N ) ≤ ε 
) ≥ 1− exp 
( −N 
(√ 4ε(4B + 3) + (4B + 3)2 
4B + 3 − 1 )2) 
. 
Furthermore, if 
ε ≥ ( B + 3 
4 )( − 1 N 
log(α) + 2 √ − 1 N 
log(α) ) , 
then PN ( Ws,1(P∗, P̂N ) ≤ ε 
) ≥ 1− α. 
Zhao and Guan, 2015 derived a more general formula for computing the Wasserstein set radius, without imposing the exponential integrability condition (2.31), resulting in a slower convergence rate for the radius, ε = O( 
√ 1/N). 
Theorem 2.7.3 (Zhao and Guan, 2015, Proposition 3). Assume the support Z is bounded and finite, and the true distribution P∗ is discrete.
2.7. Setting the Radius of the Wasserstein Ball 43 
We have, 
PN ( Ws,1(P∗, P̂N ) ≤ ε 
) ≥ 1− exp 
( − Nε2 
2B2 
) , 
where B is as in (2.32). Moreover, if we set 
ε ≥ B 
√ 2 log(1/α) 
N , 
then PN ( Ws,1(P∗, P̂N ) ≤ ε 
) ≥ 1− α. 
2.7.2 Robust Wasserstein Profile Inference 
In this subsection we introduce a different approach proposed by Blanchet et al., 2019b for optimally selecting the size of the Wasserstein ambiguity set. This method combines the information of the structure of the ambiguity set and the loss function that is being minimized. Unlike Section 2.7.1 where large deviation theory is adopted to describe the closeness between the empirical measure and the true measure, here the true measure is characterized indirectly via the first-order optimality condition of the loss function. 
Recall the Wasserstein DRO formulation: 
inf β 
sup Q∈Ω 
EQ[hβ(z) ] , (2.33) 
where the ambiguity set is defined as: 
Ω = Ωs,t ε (P̂N ) , {Q ∈ P(Z) : Ws,t(Q, P̂N ) ≤ ε}. 
We will suppress the dependence of Ω on s, t, ε, P̂N for ease of notation. For every Q ∈ Ω, there is an optimal choice β = β(Q) which minimizes the risk EQ[hβ(z) 
] , i.e., 
β(Q) = arg min β 
EQ[hβ(z) ] . 
We define Sβ(Ω) , {β(Q) : Q ∈ Ω} to be the set of plausible selections of the parameter β. If the true measure P∗ ∈ Ω, then β∗ = β(P∗) ∈ Sβ(Ω).
44 The Wasserstein Metric 
We say that β∗ is plausible with (1− α) confidence if β∗ ∈ Sβ(Ω) with probability at least 1 − α. We want to choose ε > 0 as small as possible so that the underlying true parameter β∗ is plausible with (1− α) confidence. 
For any given Q, the optimal solution β(Q) is characterized by the following first-order condition: 
EQ[∇βhβ(Q)(z)] = 0, (2.34) 
where ∇βhβ(Q)(z) is the partial derivative of hβ(z) w.r.t. β evaluated at β = β(Q). Define the Robust Wasserstein Profile (RWP) function associated with the estimation equation (2.34) as: 
R(β) = infQ {( Ws,t(Q, P̂N ) 
)t : EQ[∇βhβ(z)] = 0 } . 
R(β) evaluates the minimal distance to the empirical distribution, for all distributions such that β is the minimizer of the expected loss. Note that R(β) is a random quantity due to the randomness in the observed samples, which is reflected in P̂N . For β∗ ∈ Sβ(Ω) to hold, it is required that there exists at least one 
Q ∈ {Q : EQ[∇βhβ∗(z)] = 0}, 
such that Q ∈ Ω. This equivalently translates into the the condition that 
R(β∗) ≤ εt. 
Therefore, β∗ is plausible with (1− α) confidence if and only if 
P(R(β∗) ≤ εt) ≥ 1− α. 
The optimal choice of ε is thus χ1/t 1−α, where χ1−α is the 1− α quantile 
of R(β∗). Moreover, 
P ( β∗ ∈ Sβ(χ1−α) 
) = P 
( R(β∗) ≤ χ1−α 
) = 1− α, 
where Sβ(χ1−α) , {β : R(β) ≤ χ1−α}. Therefore, Sβ(χ1−α) is a (1−α) confidence region for β∗. 
The problem of optimal radius selection now reduces to finding the quantile of R(β∗). Since β∗ is unknown, we need to come up with a way
2.7. Setting the Radius of the Wasserstein Ball 45 
of estimating the distribution of the RWP function R(β∗). Blanchet et al., 2019b developed an asymptotic analysis of the RWP function, and established that as N →∞, 
N t/2R(β∗) d−−→ R̄(t), 
for a suitably defined random variable R̄(t), where d−−→ means convergence in distribution. We first state a number of assumptions that are needed to establish this convergence in distribution. 
Assumption C. The cost function is the `r norm: s(z1, z2) = ‖z1−z2‖r, where r ≥ 1. Let s be such that 1/r + 1/s = 1. 
Assumption D. The true parameter β∗ satisfies EP∗ [∇βhβ∗(z)] = 0, and EP∗‖∇βhβ∗(z)‖22 <∞, where P∗ is the underlying true distribution of z. 
Assumption E. The function ∇βhβ∗(z) is continuously differentiable w.r.t. z with gradient ∇β,zhβ∗(z). 
Assumption F. 
EP∗ [∇β,zhβ∗(z)∇β,zhβ∗(z)′]  0. 
Assumption G. There exists κ > 0 such that for ‖z‖r ≥ 1, 
‖∇β,zhβ∗(z)‖s ≤ κ‖z‖t−1 r , 
where the LHS denotes the induced `s norm of the matrix ∇β,zhβ∗(z). 
Assumption H. There exists a function c : Rd → [0,∞) such that, 
‖∇β,zhβ∗(z + δ)−∇β,zhβ∗(z)‖s ≤ c(z)‖δ‖r, 
for ‖δ‖r ≤ 1, EP∗ [c(z)a] <∞, and a ≤ max(2, t/(t− 1)). 
Theorem 2.7.4 (Blanchet et al., 2019b, Theorem 3). When t > 1, under Assumptions C, D, E, F, G, H, as N →∞, 
N t/2R(β∗) d−−→ R̄(t), 
where 
R̄(t) = max ζ 
{ tζ′r− (t− 1)EP∗‖ζ′∇β,zhβ∗(z)‖t/(t−1) 
s 
} .
46 The Wasserstein Metric 
When t = 1, suppose that z has a positive density almost everywhere w.r.t. the Lebesgue measure. Then, under Assumptions C, D, E, F, 
N1/2R(β∗) d−−→ R̄(1), 
where R̄(1) = max 
ζ ζ′r 
s.t. P∗ ( ‖ζ′∇β,zhβ∗(z)‖s > 1 
) = 0, 
with r ∼ N (0,E[∇βhβ∗(z)∇βhβ∗(z)′]). 
The proof of Theorem 2.7.4 uses the dual representation of the RWP function, and proceeds by showing that R̄(t) is both an asymptotic stochastic upper bound and a lower bound of N t/2R(β∗) (refer to Blanchet et al., 2019b for details). Notice that the limiting random variable R̄(t) still depends on the unknown parameter β∗ and the unobservable true distribution P∗. When using Theorem 2.7.4 in practice, some further relaxations for R̄(t) are needed to get rid of the unknown parameters. We next illustrate this idea using an example of distributionally robust logistic regression. 
Example: Optimal Radius Selection for Wasserstein Distributionally Robust Logistic Regression Using RWP Inference 
In this example we show how to use the RWP function and its limiting variable R̄(t) to select the optimal radius for the Wasserstein ambiguity set in a distributionally robust logistic regression problem. 
Let x ∈ Rd denote the predictor and y ∈ {−1,+1} the associated binary label to be predicted. In logistic regression, the conditional distribution of y given x is modeled as 
P(y|x) = ( 1 + exp(−yβ′x) 
)−1 , 
where β is the unknown coefficient vector (classifier) to be estimated. The Maximum Likelihood Estimator (MLE) of β is found by minimizing the negative log-likelihood (logloss) 
hβ(x, y) = log(1 + exp(−yβ′x)).
2.7. Setting the Radius of the Wasserstein Ball 47 
We define the distance metric on the predictor-response space as follows. 
s((x1, y1), (x2, y2)) , 
‖x1 − x2‖r, if y1 = y2, ∞, otherwise. 
(2.35) 
The distributionally robust logistic regression problem is formulated as: 
inf β 
sup Q∈Ω 
EQ[ log(1 + exp(−yβ′x)) ] , (2.36) 
where the order-1 Wasserstein metric is used to define the set Ω: 
Ω , {Q ∈ P(Z) : Ws,1(Q, P̂N ) ≤ ε}. 
We apply Theorem 2.7.4 with t = 1 to derive the optimal radius ε. Note that 
∇βhβ(x, y) = −yx 1 + exp(yβ′x) . 
Then, for t = 1, as N →∞, √ NR(β∗) d−−→ R̄(1), 
where R̄(1) = supζ∈A ζ′r, 
and r ∼ N 
( 0,EP∗ 
[ xx′( 1 + exp(yx′β∗) 
)2 ]), A , 
{ ζ ∈ Rd : sup(x,y) ‖ζ′∇β,xhβ∗(x, y)‖s ≤ 1 
} , 
where s satisfies 1/r + 1/s = 1. Note that R̄(1) still depends on β∗ and P∗ which are both unknown. 
We need to find a stochastic upper bound of R̄(1) (for a conservative selection of the radius) that is independent of the unknown quantities. By noting that A is a subset of 
{ζ ∈ Rd : ‖ζ‖s ≤ 1}, 
and that EP∗X [xx′]− EP∗ 
[ xx′( 1 + exp(yx′β∗) 
)2 ]
48 The Wasserstein Metric 
is positive definite, where P∗X denotes the marginal distribution of x under P∗, we have: 
R̄(1) D 
≤ ‖r̃‖r, 
where r̃ ∼ N ( 0,EP∗X [xx′] 
) , and 
D 
≤ denotes stochastic dominance. The size of the Wasserstein ambiguity set for distributionally robust 
logistic regression can thus be chosen by the following procedure. 
1. Estimate the (1− α) quantile of ‖r̃‖r, where r̃ ∼ N ( 0,EP∗X [xx′] 
) . 
Denote the estimated quantile by χ̂1−α. 
2. Choose the radius ε to be ε = χ̂1−α/ √ N .
3 
Solving the Wasserstein DRO Problem 
In this section we discuss how to solve the Wasserstein DRO problem, as well as the performance of the DRO estimator. A Lagrangian dual method is presented in Section 3.1, for a DRO model with an ambiguity set centered at a general nominal distribution. Section 3.2 discusses the existence and the structure of the extreme distribution that achieves the optimal value of the inner maximization problem of DRO. In Section 3.3, we apply the dual method to DROmodels with an ambiguity set centered at the discrete empirical distribution. Sections 3.4 and 3.5 study the finite sample and asymptotic performance of the DRO estimator, respectively. 
3.1 Dual Method 
The main obstacle to solving the DRO problem (1.5) lies in the inner infinite dimensional maximization problem 
supQ∈Ω EQ[h(z) ] , (3.1) 
where we suppress the dependence of h on β for ease of notation, and the ambiguity set is defined as: 
Ω = Ωs,t ε (P0) , {Q ∈ P(Z) : Ws,t(Q, P0) ≤ ε}. 
49
50 Solving the Wasserstein DRO Problem 
We will suppress the dependence of Ω on s, t, ε,P0 for notational convenience. To transform Problem (3.1) into a finite dimensional problem, researchers have resorted to Lagrangian duality, see Esfahani and Kuhn, 2018; Gao and Kleywegt, 2016. Write Problem (3.1) in the following form: 
Primal: vP = sup Q∈P(Z) 
{ ∫ Z h(z)dQ(z) : Ws,t(Q,P0) ≤ ε 
} . (3.2) 
Gao and Kleywegt, 2016 derived the Lagrangian dual of (3.2) as follows: 
Dual: vD = inf λ≥0 
{ λεt − 
∫ Z infz∈Z 
[ λst(z, z0)− h(z) 
] dP0(z0) 
} , 
(3.3) when the growth rate of the loss function h(z), which, given an unbounded set Z and a fixed z0 ∈ Z, is defined as: 
GRh , lim sup s(z,z0)→∞ 
h(z)− h(z0) st(z, z0) , (3.4) 
is finite. Note that if Z is bounded, by convention we set GRh = 0. The value of GRh does not depend on the choice of z0 (Gao and Kleywegt, 2016). Remark: Define a function 
φ(λ, z0) , inf z∈Z 
[ λst(z, z0)− h(z) 
] . 
The dual objective function 
vD(λ) , λεt − ∫ Z φ(λ, z0)dP0(z0), λ ≥ 0, 
is the sum of a linear function and an extended real-valued convex function − 
∫ Z φ(λ, z0)dP0(z0). The convexity comes from the concavity 
of φ(λ, z0) w.r.t. λ. To see this, for q ∈ [0, 1], and a fixed z0 ∈ Z, φ(qλ1 + (1− q)λ2, z0) 
= inf z∈Z 
[( qλ1 + (1− q)λ2 
) st(z, z0)− h(z) 
] = ( qλ1 + (1− q)λ2 
) st(z∗, z0)− h(z∗) 
= q [ λ1s 
t(z∗, z0)− h(z∗) ] 
+ (1− q) [ λ2s 
t(z∗, z0)− h(z∗) ] 
≥ qφ(λ1, z0) + (1− q)φ(λ2, z0),
3.1. Dual Method 51 
where the first step uses the definition of φ, z∗ = arg minz∈Z [( qλ1 + 
(1 − q)λ2 ) st(z, z0) − h(z) 
] , and the last step is due to the fact that 
z∗ ∈ Z. 
Thus, vD(λ) is a convex function on [0,∞). Moreover, as λ → ∞, vD(λ)→∞, since vD(λ) ≥ λεt + 
∫ z0∈Z h(z0)dP0(z0), where the RHS is 
obtained through taking z = z0 in the definition of φ. 
To see the necessity of having a finite growth rate, note that to ensure Problem (3.1) has a finite optimal value, it is required that 
EQ[h(z) ] <∞, ∀Q ∈ Ω. 
This can be equivalently expressed as 
∣∣∣EQ[h(z) ] − EP0 
[ h(z) 
]∣∣∣ <∞, ∀Q ∈ Ω. (3.5) 
The following Theorem 3.1.1 implies that, if the growth rate of h is infinite, (3.5) will be violated. Moreover, as we will see later, when the growth rate of the loss function is infinite, strong duality for Problem (3.2) fails to hold, in which case the DRO problem becomes intractable. In the sequel, we assume h is upper semi-continuous and GRh <∞. 
Theorem 3.1.1. Suppose a function h : Z → R defined on two metric spaces (Z, s) and (R, | · |), has a finite growth rate: 
∣∣h(z1)− h(z2) ∣∣ 
st(z1, z2) ≤ L, ∀z1, z2 ∈ Z. 
Then, for any two distributions Q1 and Q2 supported on Z, 
∣∣∣EQ1 [ h(z) 
] − EQ2 
[ h(z) 
]∣∣∣ ≤ LW t s,t(Q1,Q2).
52 Solving the Wasserstein DRO Problem 
Proof. 
∣∣∣EQ1 [ h(z) 
] − EQ2 
[ h(z) 
]∣∣∣ = ∣∣∣∣∫ Z h(z1)dQ1(z1)− 
∫ Z h(z2)dQ2(z2) 
∣∣∣∣ = ∣∣∣∣∫ Z h(z1) 
∫ z2∈Z 
dπ0(z1, z2)− ∫ Z h(z2) 
∫ z1∈Z 
dπ0(z1, z2) ∣∣∣∣ 
≤ ∫ Z×Z 
∣∣h(z1)− h(z2) ∣∣dπ0(z1, z2) 
= ∫ Z×Z 
∣∣h(z1)− h(z2) ∣∣ 
st(z1, z2) st(z1, z2)dπ0(z1, z2) 
≤ ∫ Z×Z 
Lst(z1, z2)dπ0(z1, z2) 
= LW t s,t(Q1,Q2), 
where π0 is the joint distribution of z1 and z2 with marginals Q1 and Q2 that achieves the optimal value of (1.7). 
3.1.1 Weak Duality 
The following Theorem 3.1.2 establishes weak duality for Problem (3.2). Later we will show that strong duality also holds, i.e., vP = vD. 
Theorem 3.1.2 (Gao and Kleywegt, 2016, Proposition 1). Suppose the loss function h has a finite growth rate: GRh < ∞. Then vP ≤ vD, where vP and vD are defined in (3.2) and (3.3), respectively. 
Proof. By weak duality, we have that: 
vP ≤ inf λ≥0 
{ λεt + sup 
Q∈P(Z) 
{ ∫ Z h(z)dQ(z)− λW t 
s,t(Q,P0) }} , (3.6) 
where the RHS is the Lagrangian dual of (3.2). Using Kantorovich
3.1. Dual Method 53 
duality (2.12), we obtain 
sup Q∈P(Z) 
{ ∫ Z h(z)dQ(z)− λW t 
s,t(Q,P0) } 
= sup Q∈P(Z) 
{∫ Z h(z)dQ(z) 
−λ sup f,g 
{ ∫ Z f(z)dQ(z) + 
∫ Z g(z0)dP0(z0) : 
g(z0) ≤ inf z∈Z 
[ st(z, z0)− f(z) 
] , ∀z0 ∈ Z 
}} ≤ − 
∫ Z inf 
z∈Z 
[ λst(z, z0)− h(z) 
] dP0(z0), 
where the second inequality is obtained through setting f(z) = h(z)/λ, for λ > 0, which is absolutely integrable due to GRh <∞, and is thus a feasible solution to the inner supremum of the second line. For λ = 0, the inequality also holds since, 
sup Q∈P(Z) 
{ ∫ Z h(z)dQ(z) 
} ≤ sup 
z∈Z h(z) = − 
∫ Z inf 
z∈Z 
[ − h(z) 
] dP0(z0). 
Combining with (3.6) we arrive at the conclusion that vP ≤ vD. 
3.1.2 Strong Duality 
We next show that vP = vD, through constructing a feasible solution to the primal problem (3.2) whose objective function value coincides with the dual objective. We first define the push-forward measure that will be used to construct a primal feasible distribution Q∗. 
Definition 1 (Push-Forward Measure). Given measurable spaces Z and Z ′, a measurable function T : Z → Z ′, and a measure P ∈ B(Z), define the push-forward measure of P through T , denoted by T#P ∈ B(Z ′), as 
T#P(A) , P(T−1(A)) = P{z ∈ Z : T (z) ∈ A}, A ⊆ Z ′. 
Construct a distribution Q∗ as a convex combination of two distributions, each of which is a perturbation of the nominal distribution P0: 
Q∗ = qT#P0 + (1− q)T#P0 , (3.7)
54 Solving the Wasserstein DRO Problem 
where the functions T , T : Z → Z produce the minimizer to φ(λ∗, z0), where λ∗ is the optimal solution to the dual problem (3.3), i.e., 
T (z0), T (z0) ∈ { z ∈ Z : λ∗st(z, z0)− h(z) = φ(λ∗, z0) 
} , (3.8) 
and q ∈ [0, 1] is chosen such that 
q 
∫ Z st ( T (z0), z0 
) dP0(z0) + (1− q) 
∫ Z st ( T (z0), z0 
) dP0(z0) = εt. (3.9) 
We choose T , T to satisfy the following conditions∫ Z st ( T (z0), z0 
) dP0(z0) ≤ εt,∫ 
Z st ( T (z0), z0 
) dP0(z0) ≥ εt, 
in order to ensure the existence of such a q. We first show that Q∗ is primal feasible. Notice that 
W t s,t(Q∗,P0) 
= sup f,g 
{∫ Z f(z)dQ∗(z) + 
∫ Z g(z0)dP0(z0) : 
f(z) ≤ inf z0∈Z 
[ st(z, z0)− g(z0) 
] , ∀z ∈ Z 
} = sup 
f,g 
{ q 
∫ Z f(z)dP0 
( T−1(z) 
) + (1− q) 
∫ Z f(z)dP0 
( T −1(z) 
) + ∫ Z g(z0)dP0(z0) : f(z) ≤ infz0∈Z 
[ st(z, z0)− g(z0) 
] , ∀z ∈ Z 
} ≤ sup 
g 
{ q 
∫ Z 
( st ( T (z0), z0 
) − g(z0) 
) dP0 
( z0 ) 
+ (1− q) ∫ Z 
( st ( T (z0), z0 
) − g(z0) 
) dP0 
( z0 ) 
+ ∫ Z g(z0)dP0(z0) 
} = q 
∫ Z st ( T (z0), z0 
) dP0 
( z0 ) 
+ (1− q) ∫ Z st ( T (z0), z0 
) dP0 
( z0 ) 
= εt, 
where the first step uses the Kantorovich duality (2.12), the second step uses the structure of Q∗ in (3.7), the third step replaces f(z) by its upper bound st 
( z, z0 
) − g(z0), and the last step uses the definition of q 
in (3.9).
3.1. Dual Method 55 
Now that the feasibility of Q∗ has been established, we next prove that Q∗ is the primal optimal solution by showing that its objective function value matches the optimal dual value.∫ Z h(z)dQ∗(z) = q 
∫ Z h(z)dP0(T−1(z)) + (1− q) 
∫ Z h(z)dP0(T−1(z)) 
= q 
∫ Z 
( λ∗st(T (z0), z0)− φ(λ∗, z0) 
) dP0(z0) 
+ (1− q) ∫ Z 
( λ∗st(T (z0), z0)− φ(λ∗, z0) 
) dP0(z0) 
= qλ∗ ∫ Z st(T (z0), z0)dP0(z0)− 
∫ Z φ(λ∗, z0)dP0(z0) 
+ (1− q)λ∗ ∫ Z st(T (z0), z0)dP0(z0) 
= λ∗εt − ∫ Z φ(λ∗, z0)dP0(z0) 
= vD, 
where the first step uses the structure of Q∗ in (3.7), the second step uses the definition of T , T in (3.8), the fourth step uses the definition of q in (3.9), and the last step results from the optimality of λ∗. We are now ready to state the strong duality result. 
Theorem 3.1.3 (Gao and Kleywegt, 2016, Theorem 1). Suppose that GRh <∞. The dual problem (3.3) always admits a minimizer λ∗, and strong duality holds: vP = vD <∞. 
Remark: The dual problem (3.3) admits a minimizer 
λ∗ ∈ [max(0,GRh),∞). 
To see this, notice that for all λ < GRh, φ(λ, z0) = −∞, since 
lim sup s(z,z0)→∞ 
[ λst(z, z0)− h(z) 
] = lim sup s(z,z0)→∞ 
( λ− h(z)− h(z0) 
st(z, z0) ) st(z, z0)− h(z0) 
=−∞, 
in which case vD(λ) =∞. We conclude that λ∗ ≥ GRh.
56 Solving the Wasserstein DRO Problem 
By using duality, Esfahani and Kuhn, 2018; Gao and Kleywegt, 2016; Zhao and Guan, 2018 proposed tractable convex reformulations for the DRO problem (1.5). For Lipschitz continuous loss functions, the duality result leads to an equivalent formulation for the Wasserstein DRO as a regularized empirical loss minimization problem, where the regularizer is related to the Lipschitz constant of the loss, see Gao et al., 2017; Shafieezadeh-Abadeh et al., 2017. This connection between robustness and regularization has also been established in Abadeh et al., 2015; Chen and Paschalidis, 2018. We will discuss it in further details in Section 4. 
3.2 The Extreme Distribution 
Section 3.1 reveals the structure of the primal optimal solution Q∗ (the extreme distribution) in (3.7). We summarize the discussions on the existence and the form of the extreme distribution in the following theorem. 
Theorem 3.2.1 (Gao and Kleywegt, 2016, Corollary 1). Suppose Z = Rd. The worst-case distribution exists if there exists a dual minimizer λ∗, and the set {z ∈ Z : λ∗st(z, z0) − h(z) = φ(λ∗, z0)} is non-empty P0-almost everywhere, and∫ 
Z st(λ∗, z0)dP0(z0) ≤ εt,∫ 
Z st(λ∗, z0)dP0(z0) ≥ εt, 
where 
s(λ, z0) , min z∈Z {s(z, z0) : λst(z, z0)− h(z) = φ(λ, z0)}, 
and, 
s(λ, z0) , max z∈Z {s(z, z0) : λst(z, z0)− h(z) = φ(λ, z0)}. 
Whenever the worst-case distribution exists, there exists one which can be represented as a convex combination of two distributions, each of which is a perturbation of the nominal distribution: 
Q = qT#P0 + (1− q)T#P0 ,
3.3. A Discrete Empirical Nominal Distribution 57 
where q ∈ [0, 1], and T , T : Z → Z satisfy 
T (z0), T (z0) ∈ {z ∈ Z : λ∗st(z, z0)− h(z) = φ(λ∗, z0)}. 
3.3 A Discrete Empirical Nominal Distribution 
In this section we apply the strong duality result developed in previous sections to the scenario where the discrete empirical distribution P̂N is used as the center of the ambiguity set. 
Corollary 3.3.1 (Gao and Kleywegt, 2016, Corollary 2). Suppose we use the empirical distribution 
P̂N , 1 N 
∑N 
i=1 δzi(z) 
as the center of the ambiguity set, i.e., P0 = P̂N , where zi, i ∈ JNK, are the observed realizations of z. Assume GRh <∞. Then, (i) The primal problem (3.2) has a strong dual problem 
vP = vD = min λ≥0 
{ λεt + 1 
N 
N∑ i=1 
sup z∈Z 
[ h(z)− λst(z, zi) 
]} . (3.10) 
Moreover, vP , vD are also equal to 
sup zi,zi,q1,q2 
{ 1 N 
N∑ i=1 
[ q1h(zi) + q2h(zi) 
]} s.t. 1 
N 
N∑ i=1 
[ q1s 
t(zi, zi) + q2s t(zi, zi) 
] ≤ εt, 
q1 + q2 ≤ 1, q1, q2 ≥ 0. 
(3.11) 
(ii) When Z is convex and h is concave, (3.10) could be reduced to 
sup z̃i∈Z 
1 N 
N∑ i=1 
h(z̃i) 
s.t. 1 N 
N∑ i=1 
st(zi, z̃i) ≤ εt. (3.12) 
(iii) Whenever the worst-case distribution exists, there exists one which is supported on at most N + 1 points and has the form 
Q∗ = 1 N 
∑ i 6=i0 
δz∗i (z) + q 
N δz∗i0 
(z) + 1− q N 
δz∗i0 (z),
58 Solving the Wasserstein DRO Problem 
where 1 ≤ i0 ≤ N , q ∈ [0, 1], z∗i0 , z ∗ i0 ∈ arg minz∈Z{λ∗st(z, zi0)− h(z)}, 
and z∗i ∈ arg minz∈Z{λ∗st(z, zi)− h(z)} for all i 6= i0. 
Proof. (3.10) comes directly from (3.3). For (3.11), recall that the worstcase distribution can be expressed as a convex combination of two perturbed versions of the empirical distribution, see (3.7) and (3.8). Thus, Q∗ is supported on 2N points zi, zi, i ∈ JNK, with probabilities q/N and (1− q)/N , respectively. Problem (3.11) finds the worst-case expected loss by imposing such a structure on the distribution Q. 
Part (ii) can be proved by noticing that Problem (3.10) is the Lagrangian dual of (3.12), which is a convex problem due to the concavity of h. 
To prove (iii), consider problem (3.11) by replacing q1 with qi and q2 with 1− qi, i.e., we allow q to vary over samples. (3.11) is a linear program in qi and has an optimal solution which has at most one fractional point (i.e., ∃i0, s.t. qi0 > 0; qi = 0, ∀i 6= i0). Therefore, there exists a worst-case distribution which is supported on at most N + 1 points. 
3.3.1 A Special Case 
We study a special case where the loss function h(z) is convex in z. We will show that Problem (3.1) can be relaxed to the summation of the empirical loss and a regularizer, where the regularization strength is equal to the size of the ambiguity set, and the regularizer is defined by the dual norm. 
Before we present this result, we start with two definitions and a well-known property. 
Definition 2 (Dual norm). Given a norm ‖ · ‖ on Rd, the dual norm ‖ · ‖∗ is defined as: 
‖θ‖∗ , sup ‖z‖≤1 
θ′z. (3.13) 
It can be shown from (3.13) that for any vectors θ, z, the following Hölder’s inequality holds.
3.3. A Discrete Empirical Nominal Distribution 59 
Theorem 3.3.2 (Hölder’s inequality). Suppose we have two scalars r, s > 1 and 1/r + 1/s = 1. For any two vectors θ = (θ1, . . . , θn) and z = (z1, . . . , zn), the following holds:∑n 
i=1 |θizi| ≤ ‖θ‖r‖z‖s. 
Definition 3 (Conjugate function). For a function h(z), its convex conjugate h∗(·) is defined as: 
h∗(θ) , sup z∈dom h 
{θ′z− h(z)}, (3.14) 
where dom h denotes the domain of the function h. 
If h is convex, then the convex conjugate of h∗ is h, and h and h∗ are called convex duals (Rockafellar, 1970). In particular, 
h(z) = sup θ∈Θ 
[θ′z− h∗(θ)], (3.15) 
where Θ , {θ : h∗(θ) < ∞} denotes the effective domain of the conjugate function h∗. 
Theorem 3.3.3 (Esfahani and Kuhn, 2018). Suppose the loss function h(z) is convex in z ∈ Z ⊆ Rd, and the set Z is closed and convex. Define an ambiguity set around the empirical distribution which is supported on N samples zi, i ∈ JNK, i.e., 
Ω = { Q ∈ P(Z) : W‖·‖,1(Q, P̂N ) ≤ ε 
} , 
where the order-1 Wasserstein metric (1.7) is induced by some norm ‖ · ‖. Problem (3.1) can be relaxed to: 
sup Q∈Ω 
EQ[h(z)] ≤ κε+ 1 N 
N∑ i=1 
h(zi), (3.16) 
where κ = sup{‖θ‖∗ : h∗(θ) <∞}, 
where ‖ · ‖∗ stands for the dual norm as defined in (3.13), and h∗(·) is the convex conjugate function of h(z) as defined in (3.14). Furthermore, (3.16) becomes an equality when Z = Rd.
60 Solving the Wasserstein DRO Problem 
Proof. Corollary 3.3.1 suggests that 
sup Q∈Ω 
EQ[h(z)] = min λ≥0 
{ λε+ 1 
N 
N∑ i=1 
sup z∈Z 
[ h(z)− λ‖z− zi‖ 
]} . (3.17) 
Using (3.15), we may write the inner maximization in (3.17) as: 
sup z∈Z 
[ h(z)− λ‖z− zi‖ 
] = sup 
z∈Z sup θ∈Θ 
[ θ′z− h∗(θ)− λ‖z− zi‖ 
] = sup 
z∈Z sup θ∈Θ 
inf ‖r‖∗≤λ 
[ θ′z− h∗(θ) + r′(z− zi) 
] = sup θ∈Θ 
inf ‖r‖∗≤λ 
sup z∈Z 
[ (θ + r)′z− h∗(θ)− r′zi 
] ≤ sup θ∈Θ 
inf ‖r‖∗≤λ 
sup z∈Rd 
[ (θ + r)′z− h∗(θ)− r′zi 
] , 
(3.18) where the second equality follows from the definition of the dual norm and the third equality uses duality. The inner maximization over z ∈ Rd 
achieves ∞ unless r = −θ. Note that if sup{‖θ‖∗ : θ ∈ Θ} > λ, then one can pick some θ ∈ Θ 
such that ‖θ‖∗ > λ, in which case the inner maximization over z ∈ Rd 
in (3.18) achieves ∞ since r 6= −θ. When sup{‖θ‖∗ : θ ∈ Θ} ≤ λ, by taking r = −θ, we have: 
sup z∈Z 
[ h(z)− λ‖z− zi‖ 
] ≤ sup θ∈Θ 
[ − h∗(θ) + θ′zi 
] = h(zi). 
(3.19) 
Plugging (3.19) into (3.17), we obtain 
sup Q∈Ω 
EQ[h(z)] ≤ 1 N 
N∑ i=1 
h(zi) + κε, 
where κ = sup{‖θ‖∗ : h∗(θ) <∞}. 
3.4 Finite Sample Performance 
In this section we discuss the finite sample out-of-sample performance of the DRO estimator. Recall the stochastic optimization problem defined in (1.4): 
J∗ , inf β 
EP∗[hβ(z) ] 
= inf β 
∫ Z hβ(z)dP∗(z). (3.20)
3.4. Finite Sample Performance 61 
Since the true measure P∗ is unknown, Problem (3.20) is not directly solvable. We solve its DRO counterpart (1.5) using the available training data zi, i ∈ JNK, with an effort to implicitly optimize over the true measure that is included in the ambiguity set with high confidence. Suppose ĴN and β̂N are respectively the optimal value and optimal solution to the DRO problem (1.5), i.e., 
ĴN , inf β 
sup Q∈Ω 
EQ[hβ(z) ] 
= sup Q∈Ω 
EQ[hβ̂N (z) ] , (3.21) 
where the ambiguity set is defined as 
Ω = Ωε(P̂N ) , { Q ∈ P(Z) : W‖·‖,1(Q, P̂N ) ≤ ε 
} . (3.22) 
To evaluate the quality of the DRO estimator β̂N , we study its out-of-sample performance on a new sample z drawn from P∗, 
EP∗[hβ̂N (z) ] . (3.23) 
We want to investigate whether the out-of-sample loss (3.23) can be meaningfully bounded from above by some certificate. Specifically, if we can show that with a high probability, the out-of-sample loss (3.23) does not exceed the training loss ĴN , 
PN { EP∗[hβ̂N (z) 
] ≤ ĴN 
} ≥ 1− α, 
where α ∈ (0, 1) is a significance parameter w.r.t. the distribution PN , which governs both β̂N and ĴN , then we can claim that β̂N generalizes well out-of-sample. The following theorem, which follows directly from the measure concentration Theorem 2.7.1, establishes the result. 
Theorem 3.4.1 (Esfahani and Kuhn, 2018, Theorem 3.5). Suppose As-sumption B holds, and ĴN and β̂N are respectively the optimal value and optimal solution to the DRO problem (1.5) with an ambiguity set specified in (3.22). Set the radius ε = εN (α) as defined in (2.30), where α ∈ (0, 1). Then we have 
PN { EP∗[hβ̂N (z) 
] ≤ ĴN 
} ≥ 1− α.
62 Solving the Wasserstein DRO Problem 
Proof. The claim follows immediately from the measure concentration result presented in Theorem 2.7.1, which establishes that 
PN ( W‖·‖,1(P∗, P̂N ) ≥ εN (α) 
) ≤ α, 
and therefore, 
PN { EP∗[hβ̂N (z) 
] ≤ ĴN 
} ≥ PN 
{ P∗ ∈ ΩεN (α)(P̂N ) 
} ≥ 1− α. 
Note that Theorem 3.4.1 establishes the out-of-sample performance of the DRO estimator for an order-1 Wasserstein ambiguity set. For a general Wasserstein metric with order t > 1, please refer to Fournier and Guillin, 2015 for a general measure concentration result. 
3.5 Asymptotic Consistency 
In addition to the finite sample result established in Section 3.4, we are also interested in the asymptotic behavior of ĴN and β̂N , as the sample size N goes to infinity. We want to establish that, if the significance level α = αN converges to zero at a carefully chosen rate, then the optimal value and solution of the DRO problem (1.5) with an ambiguity set of size ε = εN (αN ), converge to the optimal value and solution of the original stochastic optimization problem (3.20), respectively. The following Theorem 3.5.1 formalizes this statement. 
Theorem 3.5.1 (Esfahani and Kuhn, 2018, Theorem 3.6). Suppose As-sumption B holds and the significance parameter αN ∈ (0, 1) satisfies 
 ∑∞ N=1 αN <∞; 
 limN→∞ εN (αN ) = 0. 
Assume the loss function hβ(z) is Lipschitz continuous in z with a Lips-chitz constant Lβ. Denote by ĴN and β̂N the optimal value and optimal solution to the DRO problem (1.5), respectively, with an ambiguity set specified in (3.22) with ε = εN (αN ), where εN (αN ) is defined in (2.30), and J∗ is the optimal value of the original stochastic optimization problem (3.20). Then,
3.5. Asymptotic Consistency 63 
(i) ĴN converges to J∗ a.s., 
P∞ { 
lim sup N→∞ 
ĴN = J∗ } 
= 1. 
(ii) If hβ(z) is lower semicontinuous in β for every z ∈ Z, and limN→∞ β̂N = β0, then β0 is P∞-almost surely an optimal solution to (3.20). 
Proof. (i) Theorem 3.4.1 implies that 
PN { J∗ ≤ EP∗[hβ̂N (z) 
] ≤ ĴN 
} ≥ PN 
{ P∗ ∈ ΩεN (αN )(P̂N ) 
} ≥ 1− αN . 
(3.24) As ∑∞N=1 αN < ∞, the Borel-Cantelli Lemma (Borel, 1909; Cantelli, 1917) implies that, 
P∞ { 
lim sup N→∞ 
ĴN ≥ J∗ } 
= 1. 
It remains to show that 
P∞ { 
lim sup N→∞ 
ĴN ≤ J∗ } 
= 1. (3.25) 
Let Q̂N ∈ ΩεN (αN )(P̂N ) be the optimal solution to the inner supremum (3.1) corresponding to β = β∗, where β∗ is the optimal solution to (3.20). Then, 
EQ̂N [hβ∗(z) ] 
= supQ∈ΩεN (αN )(P̂N ) E Q[hβ∗(z) 
] . 
According to Theorem 3.1.1, and due to the Lipschitz continuity of hβ(z), we know that∣∣∣EQ1 
[ hβ(z) 
] − EQ2 
[ hβ(z) 
]∣∣∣ ≤ LβW‖·‖,1(Q1,Q2). 
Then, ĴN ≤ supQ∈ΩεN (αN )(P̂N ) E 
Q[hβ∗(z)] 
= EQ̂N [hβ∗(z)] ≤ EP∗ [hβ∗(z)] + Lβ∗W‖·‖,1(P∗, Q̂N ) = J∗ + Lβ∗W‖·‖,1(P∗, Q̂N ),
64 Solving the Wasserstein DRO Problem 
where the first step is due to the feasibility of β∗ to (3.21), and the third step is due to Theorem 3.1.1. In order to prove (3.25), we only need to show that 
P∞ { 
lim sup N→∞ 
W‖·‖,1(P∗, Q̂N ) = 0 } 
= 1. (3.26) 
The triangle inequality of the Wasserstein metric (cf. Theorem 2.2.1) ensures that 
W‖·‖,1(P∗, Q̂N ) ≤W‖·‖,1(P∗, P̂N ) +W‖·‖,1(P̂N , Q̂N ) ≤W‖·‖,1(P∗, P̂N ) + εN (αN ). 
From Theorem 2.7.1 we know that 
PN ( W‖·‖,1(P∗, P̂N ) ≤ εN (αN ) 
) ≥ 1− αN . 
Therefore, by the Borel-Cantelli Lemma (Cantelli, 1917), 
P∞ ( 
lim sup N→∞ 
{ W‖·‖,1(P∗, P̂N ) ≤ εN (αN ) 
}) = 1. 
Since limN→∞ εN (αN ) = 0, (3.26) follows. (ii) We need to show that β0 achieves the optimal value of (3.20), i.e., 
EP∗ [hβ0(z)] = J∗. 
Note that, J∗ ≤ EP∗ [hβ0(z)] ≤ EP∗[ lim inf 
N→∞ hβ̂N 
(z) ] 
≤ lim inf N→∞ 
EP∗[hβ̂N (z) ] 
≤ lim sup N→∞ 
EP∗[hβ̂N (z) ] 
≤ lim sup N→∞ 
ĴN 
= J∗, 
where the first inequality is due to the feasibility of β0 to (3.20), the second inequality follows from the lower semicontinuity of h in β, the third inequality is due to Fatou’s lemma, and the fifth inequality holds P∞-almost surely due to (3.24). We thus conclude that β̂N converges to the optimal solution of (3.20) a.s.
4 
Distributionally Robust Linear Regression 
In this section, we introduce the Wasserstein DRO formulation for linear regression. The focus is to estimate a robustified linear regression plane that is immunized against potential outliers in the data. Classical approaches, such as robust regression (Huber, 1964; Huber, 1973), remedy this problem by fitting a weighted least squares that downweights the contribution of atypical data points. By contrast, the DRO approach mitigates the impact of outliers through hedging against a family of distributions on the observed data, some of which assign very low probabilities to the outliers. 
4.1 The Problem and Related Work 
Consider a linear regression model with response y ∈ R, predictor vector x ∈ Rp, regression coefficient β∗ ∈ Rp, and error η ∈ R: 
y = x′β∗ + η. 
Given potentially corrupted samples (xi, yi), i ∈ JNK, we are interested in obtaining an estimator of β∗ that is robust with respect to the perturbations in the data. Popular robust estimators include: 
65
66 Distributionally Robust Linear Regression 
 Least Absolute Deviation (LAD), which minimizes the sum of absolute residuals ∑N 
i=1 |yi − x′iβ|, and 
 M-estimation (Huber, 1964; Huber, 1973), which minimizes a symmetric loss function ρ(·) of the residuals in the form ∑N 
i=1 ρ(yi − x′iβ), downweighting the influence of samples with large absolute residuals. 
Several choices for ρ(·) include the Huber function (Huber, 1964; Huber, 1973), the Tukey’s Biweight function (Rousseeuw and Leroy, 2005), the logistic function (Coleman et al., 1980), the Talwar function (Hinich and Talwar, 1975), and the Fair function (Fair, 1974). 
Both LAD and M-estimation are not resistant to large deviations in the predictors. For contamination present in the predictor space, high breakdown value methods are required. The breakdown value is the smallest proportion of observations in the dataset that need to be replaced to carry the estimate arbitrarily far away. Examples of high breakdown value methods include the Least Median of Squares (LMS) (Rousseeuw, 1984), which minimizes the median of the absolute residuals, the Least Trimmed Squares (LTS) (Rousseeuw, 1985), which minimizes the sum of the q smallest squared residuals, and S-estimation (Rousseeuw and Yohai, 1984), which has a higher statistical efficiency than LTS with the same breakdown value. A combination of the high breakdown value method and M-estimation is the MM-estimation (Yohai, 1987). It has a higher statistical efficiency than S-estimation. We refer the reader to the book of Rousseeuw and Leroy, 2005 for an elaborate description of these robust regression methods. 
The aforementioned robust estimation procedures focus on modifying the objective function in a heuristic way with the intent of minimizing the effect of outliers. A more rigorous line of research explores the underlying stochastic optimization problem that leads to the sample-based estimation procedures. For example, the OLS objective can be viewed as minimizing the expected squared residual under the uniform empirical distribution over the samples. It has been well recognized that optimizing under the empirical distribution yields estimators that are sensitive to perturbations in the data and suffer from overfitting. Instead of equally weighting all the samples as in the empirical distribution, one
4.2. The Wasserstein DRO Formulation for Linear Regression 67 
may wish to include more informative distributions that “drive out” the corrupted samples. DRO realizes this through hedging the expected loss against a family of distributions that includes the true data-generating mechanism with high confidence (cf. Theorem 2.7.1). Compared to the single distribution-based stochastic optimization, DRO often results in better out-of-sample performance due to its distributional robustness. 
We consider a DRO problem with an ambiguity set containing distributions that are close to the discrete empirical distribution in the sense of Wasserstein distance. We adopt the absolute residual loss |y−x′β| for the purpose of enhancing robustness. By exploiting duality, we relax the Wasserstein DRO formulation to a convex optimization problem which encompasses a class of regularized regression models, providing new insights into the regularizer, and establishing the connection between the amount of ambiguity allowed and a regularization penalty term. We provide justifications for the `1-loss based DRO learning by establishing novel performance guarantees on both the out-of-sample loss (prediction bias) and the discrepancy between the estimated and the true regression coefficients (estimation bias). Extensive numerical results demonstrate the superiority of the DRO model to a host of regression models, in terms of the prediction and estimation accuracies. We also consider the application of the DRO model to outlier detection, and show that it achieves a much higher AUC (Area Under the ROC Curve) than M-estimation (Huber, 1964; Huber, 1973). 
The rest of this section is organized as follows. In Section 4.2, we introduce the Wasserstein DRO formulation in a linear regression setting. Section 4.3 establishes performance guarantees for the solution to DRO relaxation. The numerical results on the performance of DRO regression are presented in Section 4.4. An application of DRO regression to outlier detection is discussed in Section 4.5. We conclude in Section 4.6. 
4.2 The Wasserstein DRO Formulation for Linear Regression 
We consider an `1-loss function hβ(x, y) , |y − x′β|, motivated by the observation that the absolute loss function is more forgiving (hence, robust) to large residuals than the squared loss (see Fig. 4.1). The
68 Distributionally Robust Linear Regression 
Wasserstein DRO problem using the `1-loss function is formulated as: 
inf β 
sup Q∈Ω 
EQ[|y − x′β| ] , (4.1) 
where Ω is defined as: 
Ω = Ωs,t ε (P̂N ) , {Q ∈ P(Z) : Ws,t(Q, P̂N ) ≤ ε}, 
and Ws,t(Q, P̂N ) is the order-t Wasserstein distance between Q and P̂N under a distance metric s (see definition in (1.7)), with P̂N the uniform empirical distribution over N samples. The formulation in (4.1) is robust since it minimizes over the regression coefficients the worst case expected loss, that is, the expected loss maximized over all probability distributions in the ambiguity set Ω. 
-2 -1.5 -1 -0.5 0 0.5 1 1.5 2 
The residuals 
0 
0.5 
1 
1.5 
2 
2.5 
3 
3.5 
4 
T h e  l o s s e s 
Absolute loss 
Squared loss 
Figure 4.1: The comparison between `1 and `2 loss functions. 
We first decide an appropriate order t for the Wasserstein metric. Based on the discussion in Section 3.1, it is required that the loss function h has a finite growth rate. Assuming that the metric s is induced by some norm ‖ · ‖, the bounded growth rate requirement is
4.2. The Wasserstein DRO Formulation for Linear Regression 69 
expressed as follows: 
lim sup ‖(x1,y1)−(x2,y2)‖→∞ 
|hβ(x1, y1)− hβ(x2, y2)| ‖(x1, y1)− (x2, y2)‖t 
≤ lim sup ‖(x1,y1)−(x2,y2)‖→∞ 
|y1 − x′1β − (y2 − x′2β)| ‖(x1, y1)− (x2, y2)‖t 
≤ lim sup ‖(x1,y1)−(x2,y2)‖→∞ 
‖(x1, y1)− (x2, y2)‖‖(−β, 1)‖∗ ‖(x1, y1)− (x2, y2)‖t 
< ∞, 
(4.2) 
where ‖ · ‖∗ is the dual norm of ‖ · ‖, and the second inequality is due to Hölder’s inequality (cf. Theorem 3.3.2). Notice that by taking t = 1, (4.2) is equivalently translated into the condition that ‖(−β, 1)‖∗ <∞, which, as we will see in Section 4.3, is an essential requirement to guarantee a good generalization performance for the Wasserstein DRO estimator. The growth rate essentially reveals the underlying metric space used by the Wasserstein distance. Taking t > 1 leads to zero growth rate in the limit of (4.2), which is not desirable since it removes the Wasserstein ball structure from the formulation and renders it an optimization problem over a singleton distribution. We thus choose the order-1 Wasserstein metric with s being induced by some norm ‖ · ‖ to define our DRO problem. 
Next, we will discuss how to convert (4.1) into a tractable formulation. Suppose we have N independently and identically distributed realizations of (x, y), denoted by (xi, yi), i ∈ JNK. Since the loss function is convex in (x, y), using the result in Section 3.3.1, the inner supremum of (4.1) can be relaxed to the right hand side of (3.16). In Theorem 4.2.1, we compute the value of κ in (3.16) for the specific `1 loss function we use. Theorem 4.2.1. Define κ(β) = sup{‖θ‖∗ : h∗β(θ) <∞}, where ‖ · ‖∗ is the dual norm of ‖·‖, and h∗β(·) is the conjugate function of hβ(·). When the loss function is hβ(x, y) = |y − x′β|, we have κ(β) = ‖(−β, 1)‖∗. Proof. We will adopt the notation z , (x, y), β̃ , (−β, 1) for ease of analysis. First rewrite κ(β) as: 
κ(β) = sup { ‖θ‖∗ : sup 
z:z′β̃≥0 {(θ − β̃)′z} <∞, sup 
z:z′β̃≤0 {(θ + β̃)′z} <∞ 
} .
70 Distributionally Robust Linear Regression 
Consider now the two linear optimization problems A and B: 
Problem A: max (θ − β̃)′z s.t. z′β̃ ≥ 0. 
Problem B: max (θ + β̃)′z s.t. z′β̃ ≤ 0. 
Form the dual problems using dual variables rA and rB, respectively: 
Dual-A: min 0 · rA s.t. β̃rA = θ − β̃, 
rA ≤ 0, 
Dual-B: min 0 · rB s.t. β̃rB = θ + β̃, 
rB ≥ 0. We want to find the set of θ such that the optimal values of problems A and B are finite. Then, Dual-A and Dual-B need to have non-empty feasible sets, which implies the following two conditions: 
∃ rA ≤ 0, s.t. β̃rA = θ − β̃, (4.3) ∃ rB ≥ 0, s.t. β̃rB = θ + β̃. (4.4) 
For all i with β̃i ≤ 0, (4.3) implies θi − β̃i ≥ 0 and (4.4) implies θi ≤ −β̃i. On the other hand, for all j with β̃j ≥ 0, (4.3) and (4.4) imply −β̃j ≤ θj ≤ β̃j . It is not hard to conclude that: 
|θi| ≤ |β̃i|, ∀ i. 
It follows, 
κ(β) = sup{‖θ‖∗ : |θi| ≤ |β̃i|, ∀i} = ‖β̃‖∗. 
Due to Theorem 4.2.1 and (3.16), (4.1) could be formulated as the following optimization problem: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖(−β, 1)‖∗. (4.5)
4.2. The Wasserstein DRO Formulation for Linear Regression 71 
Notice that (4.5) coincides with the regularized LAD models (Pollard, 1991; Wang et al., 2006), except that it regularizes a variant of the regression coefficient. The regularization term of (4.5) is the product of the growth rate of the loss and the Wasserstein ball radius. A zero growth rate diminishes the effect of the Wasserstein distributional uncertainty set, and the resulting formulation would simply be an empirical loss minimization problem. The parameter ε controls the conservativeness of the formulation, whose selection was discussed in Section 2.7. 
The connection between robustness and regularization has been established in several works. The earliest one may be credited to El Ghaoui and Lebret, 1997, which shows that minimizing the worst-case squared residual within a Frobenius norm-based perturbation set is equivalent to Tikhonov regularization. In more recent works, using properly selected uncertainty sets, Xu et al., 2009a has shown the equivalence between robust linear regression and the Least Absolute Shrinkage and Selection Operator (LASSO). Yang and Xu, 2013 extends this to more general LASSO-like procedures, including versions of the grouped LASSO. Bert-simas and Copenhaver, 2018 gives a comprehensive characterization of the conditions under which robustification and regularization are equivalent for regression models. For classification problems, Xu et al., 2009b shows the equivalence between the regularized support vector machines (SVMs) and a robust optimization formulation, by allowing potentially correlated disturbances in the covariates. Abadeh et al., 2015 considers a robust version of logistic regression under the assumption that the probability distributions under consideration lie in a Wasserstein ball. Recently, Shafieezadeh-Abadeh et al., 2017; Gao et al., 2017 has provided a unified framework for connecting the Wasserstein DRO with regularized learning procedures, for various regression and classification models. 
Formulation (4.5) incorporates a class of models whose specific form depends on the norm space we choose, which could be application-dependent and practically useful. For example, when the Wasserstein metric s is induced by ‖ · ‖2, (4.5) is a convex quadratic problem which can be solved to optimality very efficiently. Specifically, it could be
72 Distributionally Robust Linear Regression 
converted to: 
min a, b1,...,bN , β 
aε+ 1 N 
∑N 
i=1 bi 
s.t. ‖β‖22 + 1 ≤ a2, 
yi − x′iβ ≤ bi, i ∈ JNK, 
− (yi − x′iβ) ≤ bi, i ∈ JNK, 
a, bi ≥ 0, i ∈ JNK. 
(4.6) 
When the Wasserstein metric is defined using ‖ · ‖1, (4.5) is a linear programming problem: 
min a, b1,...,bN , β 
aε+ 1 N 
∑N 
i=1 bi 
s.t. a ≥ β′ei, i ∈ JpK, 
a ≥ −β′ei, i ∈ JpK, 
yi − x′iβ ≤ bi, i ∈ JNK, 
− (yi − x′iβ) ≤ bi, i ∈ JNK, 
a ≥ 1, bi ≥ 0, i ∈ JNK. 
(4.7) 
More generally, when the coordinates of (x, y) differ from each other substantially, a properly chosen, positive definite weight matrix M ∈ R(p+1)×(p+1) could scale correspondingly different coordinates of (x, y) by using the M-weighted norm: 
‖(x, y)‖M = √ 
(x, y)′M(x, y). 
It can be shown that (4.5) in this case becomes: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε 
√ (−β, 1)′M−1(−β, 1). (4.8) 
We would like to highlight several novel viewpoints that are brought by the Wasserstein DRO framework and justify the value and novelty of (4.5). First, (4.5) is obtained as an outcome of a fundamental DRO formulation, which enables new interpretations of the regularizer from the standpoint of distributional robustness, and provides rigorous theoretical foundation on why the `2-regularizer prevents overfitting to the
4.3. Performance Guarantees for the DRO Estimator 73 
training data. The regularizer could be seen as a control over the amount of ambiguity in the data and reveals the reliability of the contaminated samples. Second, the geometry of the Wasserstein ball is embedded in the regularization term, which penalizes the regression coefficient on the dual Wasserstein space, with the magnitude of penalty being the radius of the ball. This offers an intuitive interpretation and provides guidance on how to set the regularization coefficient. Moreover, different from the traditional regularized LAD models that directly penalize the regression coefficient β, (4.5) regularizes the vector (−β, 1), where the 1 takes into account the transportation cost along the y direction. Penalizing only β corresponds to an infinite transportation cost along y. (4.5) is more general in this sense, and establishes the connection between the metric space on the data and the form of the regularizer. 
4.3 Performance Guarantees for the DRO Estimator 
Having obtained a tractable reformulation for the Wasserstein DRO problem, we next establish guarantees on the predictive power and estimation quality for the solution to (4.5). Two types of results will be presented in this section, one of which bounds the prediction bias of the estimator on new, future data (given in Section 4.3.1). The other one bounds the discrepancy between the estimated and true regression planes (estimation bias), and is given in Section 4.3.2. 
4.3.1 Out-of-Sample Performance 
In this subsection, we investigate generalization characteristics of the solution to (4.5), which involves measuring the error generated by the DRO estimator on a new random sample (x, y). We would like to obtain estimates that not only explain the observed samples well, but, more importantly, possess strong generalization abilities. The derivation is mainly based on Rademacher complexity (see Bartlett and Mendelson, 2002), which is a measurement of the complexity of a class of functions. We would like to emphasize the applicability of such a proof technique to general loss functions, as long as their empirical Rademacher complexity could be bounded. The bound we derive for the prediction bias depends
74 Distributionally Robust Linear Regression 
on both the sample average loss (the training error) and the dual norm of the regression coefficient (the regularizer), which corroborates the validity and necessity of the regularized formulation. Moreover, the generalization result also builds a connection between the loss function and the form of the regularizer via the Rademacher complexity, which enables new insights into the regularization term and explains the commonly observed good out-of-sample performance of regularized regression in a rigorous way. 
Suppose the data (x, y) is drawn from the probability distribution P∗. We first make several mild assumptions that are needed for the generalization result. 
Assumption I. ‖(x, y)‖ ≤ R, a.s. under P∗. 
Assumption J. supβ ‖(−β, 1)‖∗ = B̄. 
Under these two assumptions, the absolute loss could be bounded via Hölder’s inequality. 
Lemma 4.3.1. For every feasible β, it follows that, 
|y − x′β| ≤ B̄R, a.s. under P∗. 
With the above result, the idea is to bound the generalization error using the empirical Rademacher complexity of the following class of loss functions: 
H = { 
(x, y)→ hβ(x, y) : hβ(x, y) = |y − x′β| } . 
We need to show that the empirical Rademacher complexity of H, denoted by RN (H) and defined as: 
RN (H) , E [ 
sup h∈H 
2 N 
∣∣∣∣ N∑ i=1 
σihβ(xi, yi) ∣∣∣∣ ∣∣∣∣∣(x1, y1), . . . , (xN , yN ) 
] , 
is upper bounded, where σ1, . . . , σN are i.i.d. uniform random variables on {1,−1}, and (xi, yi), i ∈ JNK, are N observed realizations of (x, y). The following result, similar to Lemma 3 in Bertsimas et al., 2015, provides a bound that is inversely proportional to the square root of the sample size.
4.3. Performance Guarantees for the DRO Estimator 75 
Lemma 4.3.2. 
RN (H) ≤ 2B̄R√ N . 
Proof. Suppose that σ1, . . . , σN are i.i.d. uniform random variables on {1,−1}. Then, by the definition of the Rademacher complexity and Lemma 4.3.1, 
RN (H) = E [ 
sup h∈H 
2 N 
∣∣∣∣ N∑ i=1 
σihβ(xi, yi) ∣∣∣∣ ∣∣∣∣∣(x1, y1), . . . , (xN , yN ) 
] 
≤ E [ 
2 N 
∣∣∣∣ N∑ i=1 
σiB̄R 
∣∣∣∣ ] 
= E [ 
2B̄R N 
∣∣∣∣ N∑ i=1 
σi 
∣∣∣∣ ] 
= 2B̄R N 
E [∣∣∣∣∣ 
N∑ i=1 
σi 
∣∣∣∣∣ ] 
≤ 2B̄R N 
E [√√√√ N∑ 
i=1 σ2 i 
] 
= 2B̄R√ N . 
Let β̂ be an optimal solution to (4.5), obtained using the samples (xi, yi), i ∈ JNK. Suppose we draw a new i.i.d. sample (x, y). In Theorem 4.3.3 we establish bounds on the error |y − x′β̂|. 
Theorem 4.3.3. Under Assumptions I and J, for any 0 < δ < 1, with probability at least 1− δ with respect to the sampling, 
EP∗ [|y− x′β̂|] ≤ 1 N 
∑N 
i=1 |yi − x′iβ̂|+ 
2B̄R√ N 
+ B̄R 
√ 8 log(2/δ) 
N , (4.9)
76 Distributionally Robust Linear Regression 
and for any ζ > 2B̄R√ N 
+ B̄R √ 
8 log(2/δ) N , 
P ( |y − x′β̂| ≥ 1 
N 
∑N 
i=1 |yi − x′iβ̂|+ ζ 
) ≤ 
1 N 
∑N i=1 |yi − x′iβ̂|+ 2B̄R√ 
N + B̄R 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 |yi − x′iβ̂|+ ζ 
. (4.10) 
Proof. We use Theorem 8 in Bartlett and Mendelson, 2002, which we state for convenience as follows. 
Theorem 4.3.4 (Theorem 8 in Bartlett and Mendelson, 2002). Consider a loss function L : Y × A → [0, 1] and a dominating cost function φ : Y ×A → [0, 1]. Let F be a class of functions mapping from X to A and let (xi, yi)Ni=1 be independently selected according to the probability measure P∗. Then, for any integer N and any 0 < δ < 1, with probability at least 1− δ over samples of length N , every f in F satisfies 
EP∗[L(y, f(x)) ] ≤ 1 N 
∑N 
i=1 φ(yi, f(xi)) +RN (φ̃ 
 F) + 
√ 8 log(2/δ) 
N , 
where φ̃ 
 F = {(x, y)→ φ(y, f(x))− φ(y, 0) : f ∈ F}. 
We set the following correspondences with the notation used in Theorem 4.3.4: f(x) = x′β, and L(y, f(x)) = φ(y, f(x)) = |y − f(x)|. This yields the bound (4.9) on the expected loss. For Eq. (4.10), we apply Markov’s inequality to obtain: 
P ( |y − x′β̂| ≥ 1 
N 
N∑ i=1 |yi − x′iβ̂|+ ζ 
) ≤ E[|y − x′β̂|] 
1 N 
∑N i=1 |yi − x′iβ̂|+ ζ 
≤ 1 N 
∑N i=1 |yi − x′iβ̂|+ 2B̄R√ 
N + B̄R 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 |yi − x′iβ̂|+ ζ 
. 
There are two probability measures in the statement of Theo-rem 4.3.3. One is related to the new data (x, y), while the other is related to the samples (xi, yi), i ∈ JNK. The expectation in (4.9) (and the probability in (4.10)) is taken w.r.t. the new data (x, y). For a given
4.3. Performance Guarantees for the DRO Estimator 77 
set of samples, (4.9) (and (4.10)) holds with probability at least 1− δ w.r.t. the measure of samples. Theorem 4.3.3 essentially says that given typical samples, the expected loss on new data using the Wasserstein DRO estimator could be bounded above by the average sample loss plus extra terms that depend on the supremum of ‖(−β, 1)‖∗ (the regularizer), and are proportional to 1/ 
√ N . This result validates the dual 
norm-based regularized regression from the perspective of generalization ability, and could be generalized to any bounded loss function. It also provides implications on the form of the regularizer. For example, if given an `2-loss function, the dependency on B̄ for the generalization error bound will be of the form B̄2, which suggests using ‖(−β, 1)‖2∗ as a regularizer, reducing to a variant of ridge regression (Hoerl and Kennard, 1970) for the `2-norm-induced Wasserstein metric. 
We also note that the upper bounds in (4.9) and (4.10) do not depend on the dimension of (x, y). This dimensionality-free characteristic implies direct applicability of the Wasserstein approach to high-dimensional settings and is particularly useful in many real applications where, potentially, hundreds of features may be present. Theorem 4.3.3 also provides guidance on the number of samples that are needed to achieve satisfactory out-of-sample performance. 
Corollary 4.3.5. Suppose β̂ is the optimal solution to (4.5). For a fixed confidence level δ and some threshold parameter τ ≥ 0, if the sample size N satisfies 
N ≥ [2(1 + 
√ 2 log(2/δ) ) τ 
]2 , (4.11) 
then the percentage difference between the expected absolute loss on new data and the sample average loss is less than τ , that is, 
E[|y − x′β̂|]− 1 N 
∑N i=1 |yi − x′iβ̂| 
B̄R ≤ τ. 
Proof. The percentage difference requirement can be translated into: 
2√ N 
+ 
√ 8 log(2/δ) 
N ≤ τ, 
from which (4.11) can be easily derived.
78 Distributionally Robust Linear Regression 
Corollary 4.3.6. Suppose β̂ is the optimal solution to (4.5). For a fixed confidence level δ, some τ ∈ (0, 1) and γ ≥ 0 such that τγ + τ − 1 > 0, if the sample size N satisfies 
N ≥ [2(1 + 
√ 2 log(2/δ) ) 
τγ + τ − 1 
]2 , (4.12) 
then, 
P ( |y − x′β̂| − 1 
N 
∑N i=1 |yi − x′iβ̂| 
B̄R ≥ γ 
) ≤ τ. 
Proof. Based on Theorem 3.3, we just need the following inequality to hold: 
1 N 
∑N i=1 |yi − x′iβ̂|+ 2B̄R√ 
N + B̄R 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 |yi − x′iβ̂|+ γB̄R 
≤ τ, 
which is equivalent to: 
γB̄R− 2B̄R√ N − B̄R 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 |yi − x′iβ̂|+ γB̄R 
≥ 1− τ. (4.13) 
We cannot obtain a lower bound for N by directly solving (4.13) since N appears in a summation operator. A proper relaxation to (4.13) is: 
γ − 2√ N − √ 
8 log(2/δ) N 
1 + γ ≥ 1− τ, (4.14) 
due to the fact that 1 N 
∑N i=1 |yi − x′iβ̂| ≤ B̄R. By solving (4.14), we 
obtain (4.12). 
In Corollaries 4.3.5 and 4.3.6, the sample size is inversely proportional to both δ and τ , which is reasonable since the more confident we want to be, the more samples we need. Moreover, the smaller τ is, the stricter a requirement we impose on the performance, and thus more samples are needed. 
4.3.2 Discrepancy between Estimated and True Regression Planes 
In addition to the generalization performance, we are also interested in the accuracy of the estimator. In this subsection, we seek to bound
4.3. Performance Guarantees for the DRO Estimator 79 
the difference between the estimated and true regression coefficients, under a certain distributional assumption on (x, y). Throughout this subsection we will use β̂ to denote the estimated regression coefficients, obtained as an optimal solution to (4.15), and β∗ for the true (unknown) regression coefficients. The bound we will derive turns out to be related to the uncertainty in the data (x, y), and the geometric structure of the true regression coefficients. 
To facilitate the analysis, we will use the following equivalent form of Problem (4.5): 
min β 
‖(−β, 1)‖∗ 
s.t. ‖(−β, 1)′Z‖1 ≤ γN , (4.15) 
where Z = [(x1, y1), . . . , (xN , yN )] is the matrix with columns (xi, yi), i ∈ JNK, and γN is some exogenous parameter related to ε. One can show that for properly chosen γN , (4.15) produces the same solution with (4.5) (Bertsekas, 1999). (4.15) is similar to (11) in Chen and Banerjee, 2016, with the difference lying in that we impose a constraint on the error instead of the gradient, and we consider a more general notion of norm on the coefficient. On the other hand, due to their similarity, we will follow the line of development in Chen and Banerjee, 2016. Still, our analysis is self-contained and the bound we obtain is in a different form, which provides meaningful insights into our specific problem. We list below the relevant definitions and assumptions that are needed to bound the estimation error. 
Definition 4 (Sub-Gaussian random variable). A random variable z is sub-Gaussian if the ψ2-norm defined below is finite, i.e., 
|||z|||ψ2 , sup 
q≥1 
(E|z|q)1/q √ q 
< +∞. 
We do not require sub-Gaussian variables to have zero mean values. It is though worth noting that the ψ2-norm |||z|||ψ2 
depends on the mean E(z). An equivalent property for sub-Gaussian random variables is that their tail distribution decays as fast as a Gaussian, namely, 
P(|z − E(z)| ≥ t) ≤ 2 exp{−t2/C2}, ∀t ≥ 0,
80 Distributionally Robust Linear Regression 
for some constant C. A random vector z ∈ Rp+1 is sub-Gaussian if z′u is sub-Gaussian 
for any u ∈ Rp+1. The ψ2-norm of a vector z is defined as: 
|||z|||ψ2 , sup 
u∈Sp+1 
∣∣∣∣∣∣z′u∣∣∣∣∣∣ψ2 , 
where Sp+1 denotes the unit sphere in the (p+1)-dimensional Euclidean space. For the properties of sub-Gaussian random variables/vectors, please refer to Vershynin, 2017. 
Definition 5 (Gaussian width). For any set A ⊆ Rp+1, its Gaussian width is defined as: 
w(A) , E [ sup u∈A 
u′g ] , (4.16) 
where g ∼ N (0, I) is a (p+ 1)-dimensional standard Gaussian random vector. 
Assumption K (Restricted Eigenvalue Condition). For some set A(β∗) = cone{v : ‖(−β∗, 1)+v‖∗ ≤ ‖(−β∗, 1)‖∗}∩Sp+1 and some positive scalar α, where Sp+1 is the unit sphere in the (p+ 1)-dimensional Euclidean space, 
inf v∈A(β∗) 
v′ZZ′v ≥ α. 
Assumption L. The true coefficient β∗ is a feasible solution to (4.15), i.e., 
‖Z′(−β∗, 1)‖1 ≤ γN . 
Assumption M. (x, y) is a centered sub-Gaussian random vector, i.e., it has zero mean and satisfies the following condition: 
|||(x, y)|||ψ2 = sup 
u∈Sp+1 
∣∣∣∣∣∣(x, y)′u ∣∣∣∣∣∣ ψ2 ≤ µ. 
Assumption N. The covariance matrix of (x, y) has bounded positive eigenvalues. Set Γ = E[(x, y)(x, y)′]; then, 
0 < λmin , λmin(Γ) ≤ λmax(Γ) , λmax <∞. 
Notice that both α in Assumption K and γN in Assumption L are related to the random observation matrix Z. A probabilistic description
4.3. Performance Guarantees for the DRO Estimator 81 
for these two quantities will be provided later. We next present a preliminary result, similar to Lemma 2 in Chen and Banerjee, 2016, that bounds the `2-norm of the estimation bias in terms of a quantity that is related to the geometric structure of the true coefficients. This result gives a rough idea on the factors that affect the estimation error. The bound derived in Theorem 4.3.7 is crude in the sense that it is a function of several random parameters that are related to the random observation matrix Z. This randomness will be described in a probabilistic way in the subsequent analysis. 
Theorem 4.3.7. Suppose the true regression coefficient vector is β∗ and the solution to (4.15) is β̂. For the set A(β∗) = cone{v : ‖(−β∗, 1) + v‖∗ ≤ ‖(−β∗, 1)‖∗} ∩ Sp+1, under Assumptions I, K, and L, we have: 
‖β̂ − β∗‖2 ≤ 2RγN α 
Ψ(β∗), (4.17) 
where Ψ(β∗) = supv∈A(β∗) ‖v‖∗. 
Proof. For ease of exposition, we will adopt the notation z , (x, y), zi , (xi, yi), β̃ , (−β, 1), β̃est , (−β̂, 1), β̃true , (−β∗, 1). 
Since both β̂ and β∗ are feasible (the latter due to Assumption L), we have: 
‖Z′β̃est‖1 ≤ γN , ‖Z′β̃true‖1 ≤ γN , 
from which we derive that ‖Z′(β̃est − β̃true)‖1 ≤ 2γN . Since β̂ is an optimal solution to (4.15) and β∗ a feasible solution, it follows that ‖β̃est‖∗ ≤ ‖β̃true‖∗. This implies that ν = β̃est − β̃true satisfies the condition ‖β̃true + v‖∗ ≤ ‖β̃true‖∗ included in the definition of A(β∗) and, furthermore, (β̃est− β̃true)/‖β̃est− β̃true‖2 ∈ A(β∗). Together with Assumption K, this yields 
(β̃est − β̃true)′ZZ′(β̃est − β̃true) ≥ α‖β̃est − β̃true‖22. (4.18)
82 Distributionally Robust Linear Regression 
On the other hand, from Hölder’s inequality: 
(β̃est − β̃true)′ZZ′(β̃est − β̃true) ≤ ‖Z′(β̃est − β̃true)‖1‖Z′(β̃est − β̃true)‖∞ ≤ 2γN max 
i |z′i(β̃est − β̃true)| 
≤ 2γN max i ‖β̃est − β̃true‖∗‖zi‖ 
≤ 2RγN‖β̃est − β̃true‖∗. 
(4.19) 
Combining (4.18) and (4.19), we have: 
‖β̂ − β∗‖2 = ‖β̃est − β̃true‖2 
≤ 2RγN α 
‖β̃est − β̃true‖∗ ‖β̃est − β̃true‖2 
≤ 2RγN α 
Ψ(β∗), 
where the last step follows from the fact that (β̃est − β̃true)/‖β̃est − β̃true‖2 ∈ A(β∗). 
As mentioned earlier, (4.17) provides a random upper bound, revealed in α and γN , that depends on the randomness in Z. We therefore would like to replace these two parameters by non-random quantities. The quantity α acts as the minimum eigenvalue of the matrix ZZ′ restricted to a subspace of Rp+1, and thus a proper substitute should be related to the minimum eigenvalue of the covariance matrix of (x, y), i.e., the Γ matrix (cf. Assumption N), given that (x, y) is zero mean. See Lemmata 4.3.8, 4.3.9 and 4.3.10 for the derivation. 
Lemma 4.3.8. Consider AΓ = {w ∈ Sp+1 : Γ−1/2w ∈ cone(A(β∗))}, where A(β∗) is defined as in Theorem 4.3.7, and Γ = E[(x, y)(x, y)′]. Under Assumptions M and N, when the sample size N ≥ C1µ̄ 
4(w(AΓ))2, where µ̄ = µ 
√ 1 
λmin , and w(AΓ) is the Gaussian width of AΓ, with 
probability at least 1− exp(−C2N/µ̄ 4), we have 
v′ZZ′v ≥ N 
2 v′Γv, ∀v ∈ A(β∗), 
where C1 and C2 are positive constants.
4.3. Performance Guarantees for the DRO Estimator 83 
Proof. Define Γ̂ = 1 N 
∑N i=1 ziz′i. Consider the set of functions F = 
{fw(z) = z′Γ−1/2w, w ∈ AΓ}. Then, for any fw ∈ F , 
E[f2 w] = E[w′Γ−1/2zz′Γ−1/2w] 
= w′Γ−1/2E[zz′]Γ−1/2w = w′w = 1, 
where we used Γ = E[zz′] and the fact that w ∈ AΓ. For any fw ∈ F we have 
|||fw|||ψ2 = ∣∣∣∣∣∣∣∣∣z′Γ−1/2w 
∣∣∣∣∣∣∣∣∣ ψ2 
= ∣∣∣∣∣∣∣∣∣z′Γ−1/2w 
∣∣∣∣∣∣∣∣∣ ψ2 
‖Γ−1/2w‖2 ‖Γ−1/2w‖2 
= ∣∣∣∣∣ ∣∣∣∣∣ ∣∣∣∣∣z′ Γ−1/2w ‖Γ−1/2w‖2 
∣∣∣∣∣ ∣∣∣∣∣ ∣∣∣∣∣ ψ2 
‖Γ−1/2w‖2 
≤ µ √ 
w′Γ−1w 
≤ µ √ 
1 λmin 
‖w‖22 
= µ 
√ 1 
λmin = µ̄, 
where the first inequality used Assumption M and the second inequality used Assumption N. 
Applying Theorem D from Mendelson et al., 2007, for any θ > 0 and when 
C̃1µ̄γ2(F , |||·|||ψ2 ) ≤ θ 
√ N, 
with probability at least 1− exp(−C̃2θ 2N/µ̄4) we have 
sup fw∈F 
∣∣∣ 1 N 
N∑ i=1 
f2 w(zi)− E[f2 
w] ∣∣∣ = sup 
fw∈F 
∣∣∣ 1 N 
N∑ i=1 
w′Γ−1/2ziz′iΓ−1/2w− 1 ∣∣∣ 
= sup w∈AΓ 
∣∣∣w′Γ−1/2Γ̂Γ−1/2w− 1 ∣∣∣ 
≤ θ, (4.20)
84 Distributionally Robust Linear Regression 
where C̃1 is some positive constant and γ2(F , |||·|||ψ2 ) is defined in Mendel-
son et al., 2007 as a measure of the size of the set F with respect to the metric |||·|||ψ2 
. Using θ = 1/2, and properties of γ2(F , |||·|||ψ2 ) outlined in 
Chen and Banerjee, 2016, we can set N to satisfy 
C̃1µ̄γ2(F , |||·|||ψ2 ) ≤ C̃1µ̄ 
2γ2(AΓ, ‖ · ‖2) ≤ C̃1µ̄ 
2C0w(AΓ) 
≤ 1 2 √ N, 
for some positive constant C0, where we used Eq. (44) in Chen and Banerjee, 2016. This implies 
N ≥ C1µ̄ 4(w(AΓ))2 
for some positive constant C1. Thus, for such N and with probability at least 1− exp(−C2N/µ̄ 
4), for some positive constant C2, (4.20) holds with θ = 1/2. This implies that for all w ∈ AΓ,∣∣∣w′Γ−1/2Γ̂Γ−1/2w− 1 
∣∣∣ ≤ 1 2 
or w′Γ−1/2Γ̂Γ−1/2w ≥ 1 
2 = 1 2w′Γ−1/2ΓΓ−1/2w. 
By the definition of AΓ, for any v ∈ A(β∗), 
v′Γ̂v ≥ 1 2v′Γv. 
Noting that Γ̂ = (1/N)ZZ′ yields the desired result. 
Note that the sample size requirement stated in Lemma 4.3.8 depends on the Gaussian width of AΓ, where AΓ relates to A(β∗). The following lemma shows that their Gaussian widths are also related. This relation is built upon the square root of the eigenvalues of Γ, which measures the extent to which AΓ expands A(β∗). 
Lemma 4.3.9 (Lemma 4 in Chen and Banerjee, 2016). Let µ0 be the ψ2-norm of a standard Gaussian random vector g ∈ Rp+1, and AΓ, A(β∗) be defined as in Lemma 4.3.8. Then, under Assumption N, 
w(AΓ) ≤ C3µ0 
√ λmax λmin 
( w(A(β∗)) + 3 
) ,
4.3. Performance Guarantees for the DRO Estimator 85 
for some positive constant C3. 
Proof. We follow the proof of Lemma 4 in Chen and Banerjee, 2016, adapted to our setting. We include all key steps for completeness. 
Recall the definition of the Gaussian width w(AΓ) (cf. (4.16)): 
w(AΓ) = E [ 
sup u∈AΓ 
u′g ] , 
where g ∼ N (0, I). We have: 
sup w∈AΓ 
w′g = sup w∈AΓ 
w′Γ−1/2Γ1/2g 
= sup w∈AΓ 
‖Γ−1/2w‖2 w′Γ−1/2 
‖Γ−1/2w‖2 Γ1/2g 
≤ √ 
1 λmin 
sup v∈cone(A(β∗))∩Bp+1 
v′Γ1/2g, 
where Bp+1 is the unit ball in the (p+ 1)-dimensional Euclidean space and the inequality used Assumption N and the fact that 
w′Γ−1/2/‖Γ−1/2w‖2 ∈ Bp+1, w ∈ AΓ. 
Define T = cone(A(β∗))∩Bp+1, and consider the stochastic process {Sv = v′Γ1/2g}v∈T . For any v1,v2 ∈ T , 
|||Sv1 − Sv2 |||ψ2 = ∣∣∣∣∣∣∣∣∣(v1 − v2)′Γ1/2g 
∣∣∣∣∣∣∣∣∣ ψ2 
= ‖Γ1/2(v1 − v2)‖2 ∣∣∣∣∣ ∣∣∣∣∣ ∣∣∣∣∣ (v1 − v2)′Γ1/2g ‖Γ1/2(v1 − v2)‖2 
∣∣∣∣∣ ∣∣∣∣∣ ∣∣∣∣∣ ψ2 
≤ ‖Γ1/2(v1 − v2)‖2 sup u∈Sp+1 
∣∣∣∣∣∣u′g∣∣∣∣∣∣ψ2 
= µ0‖Γ1/2(v1 − v2)‖2 ≤ µ0 
√ λmax‖v1 − v2‖2, 
where the last step used Assumption N. Then, by the tail behavior of sub-Gaussian random variables (see 
Hoeffding bound, Thm. 2.6.2 in Vershynin, 2017), we have: 
P(|Sv1 − Sv2 | ≥ δ) ≤ 2 exp ( − C01δ 
2 
µ2 0λmax‖v1 − v2‖22 
) ,
86 Distributionally Robust Linear Regression 
for some positive constant C01. To bound the supremum of Sv, we define the metric s(v1,v2) = 
µ0 √ λmax‖v1 − v2‖2. Then, by Lemma B in Chen and Banerjee, 2016, 
E [ sup v∈T 
v′Γ1/2g ] ≤ C02γ2(T , s) 
= C02µ0 √ λmaxγ2(T , ‖ · ‖2) 
≤ C3µ0 √ λmaxw(T ), 
for positive constants C02, C3, where γ2(T , s) is the γ2-functional we referred to in the proof of Lemma 4.3.8. Since T = cone(A(β∗))∩Bp+1 ⊆ conv(A(β∗) ∪ {0}), by Lemma 2 in Maurer et al., 2014, 
w(T ) ≤ w(conv(A(β∗) ∪ {0})) = w(A(β∗) ∪ {0}) ≤ max{w(A(β∗)), w({0})}+ 2 
√ ln 4 
≤ w(A(β∗)) + 3. 
Thus, 
w(AΓ) = E [ 
sup w∈AΓ 
w′g ] 
≤ √ 
1 λmin 
E [ sup v∈T 
v′Γ1/2g ] 
≤ C3 
√ 1 
λmin µ0 √ λmaxw(T ) 
≤ C3µ0 
√ λmax λmin 
( w(A(β∗)) + 3 
) . 
Combining Lemmata 4.3.8 and 4.3.9, and expressing the covariance matrix Γ using its eigenvalues, we arrive at the following result. 
Corollary 4.3.10. Under Assumptions M and N, and the conditions in Lemmata 4.3.8 and 4.3.9, when 
N ≥ C̄1µ̄ 4µ2 
0 · λmax λmin 
( w(A(β∗)) + 3 
)2 ,
4.3. Performance Guarantees for the DRO Estimator 87 
with probability at least 1− exp(−C2N/µ̄ 4), 
v′ZZ′v ≥ Nλmin 2 , ∀v ∈ A(β∗), 
where C̄1 and C2 are positive constants. 
Proof. Combining Lemmata 4.3.8 and 4.3.9, and using the fact that for any v ∈ A(β∗), 
N 
2 v′Γv ≥ Nλmin 2 , 
we can derive the desired result. 
Next we derive the smallest possible value of γN such that β∗ is feasible. 
Lemma 4.3.11. Under Assumptions I and J, for any feasible β, 
‖(−β, 1)′Z‖1 ≤ NB̄R, a.s. under P∗. 
Combining Theorem 4.3.7, Corollary 4.3.10 and Lemma 4.3.11, we have the following main performance guarantee result that bounds the estimation bias of the solution to (4.15). 
Theorem 4.3.12. Under Assumptions I, J, K, L, M, N, and the conditions of Theorem 4.3.7, Corollary 4.3.10 and Lemma 4.3.11, when 
N ≥ C̄1µ̄ 4µ2 
0 · λmax λmin 
( w(A(β∗)) + 3 
)2 , 
with probability at least 1− exp(−C2N/µ̄ 4), 
‖β̂ − β∗‖2 ≤ 4R2B̄ 
λmin Ψ(β∗). (4.21) 
The estimation error bound in (4.21) depends on the variance of (x, y), and the geometrical structure of the true regression coefficient. It does not decay to zero as N goes to infinity. The reason is that the absolute residual |y−β′x| has a nonzero mean, which will be propagated into the estimation bias.
88 Distributionally Robust Linear Regression 
4.4 Experiments on the Performance of Wasserstein DRO 
In this section, we will explore the robustness of the Wasserstein formulation in terms of its Absolute Deviation (AD) loss function and the dual norm regularizer on the extended regression coefficient (−β, 1). Recall that the Wasserstein formulation is in the following form: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖(−β, 1)‖∗. (4.22) 
We will focus on the following three aspects of this formulation: 
1. How to choose a proper norm ‖ · ‖ for the Wasserstein metric? 
2. Why do we penalize the extended regression coefficient (−β, 1) rather than β? 
3. What is the advantage of the AD loss compared to the Squared Residuals (SR) loss? 
To answer Question 1, we will connect the choice of ‖ · ‖ for the Wasser-stein metric with the characteristics/structures of the data (x, y). Specif-ically, we will design two sets of experiments, one with a dense regression coefficient β∗, where all coordinates of x play a role in determining the value of the response y, and another with a sparse β∗ implying that only a few predictors are relevant in predicting y. Two Wasserstein formulations will be tested and compared, one induced by the ‖ · ‖2 (Wasserstein `2), which leads to an `2-regularizer in (4.22), and the other one induced by the ‖ · ‖∞ (Wasserstein `∞) and resulting in an `1-regularizer in (4.22). 
The problem of feature selection can be formulated as an `0-norm regularized regression problem, which is NP-hard and is usually relaxed to an `1-norm regularized formulation, known as the Least Absolute Shrinkage and Selection Operator (LASSO). LASSO enjoys several attractive statistical properties under various conditions on the model matrix (Tibshirani, 2011; Friedman et al., 2001). Here, in our context, we try to offer an explanation of the sparsity-inducing property of LASSO from the perspective of the Wasserstein DRO formulation, through
4.4. Experiments on the Performance of Wasserstein DRO 89 
projecting the sparsity of β∗ onto the (x, y) space and establishing a sparse distance metric that only extracts a subset of coordinates from (x, y) to measure the closeness between samples. 
For the second question, we first note that if the Wasserstein metric is induced by the following metric sc: 
sc(x, y) = ‖(x, cy)‖2, 
for a positive constant c; then as c → ∞, the resulting Wasserstein DRO formulation becomes: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖β‖2, 
which is the `2-regularized LAD. This can be proved by recognizing that sc(x, y) = ‖(x, y)‖M, with M ∈ R(p+1)×(p+1) a diagonal matrix whose diagonal elements are (1, . . . , 1, c2), and then applying (4.8). Alternatively, if we let sc(x, y) = ‖(x, cy)‖∞, Corollary 4.4.1 shows that as c → ∞, the corresponding Wasserstein formulation becomes the `1-regularized LAD. 
Corollary 4.4.1. If the Wasserstein metric is induced by the following metric s: 
sc(x, y) = ‖(x, cy)‖∞, with c some positive constant. Then as c→∞, the Wasserstein DRO formulation (4.22) reduces to: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖β‖1, 
which is the `1-regularized LAD. 
Proof. We first define a new notion of norm on (x, y) where x = (x1, . . . , xp): 
‖(x, y)‖w,r , ‖(x1w1, . . . , xpwp, ywp+1)‖r, 
for some (p+ 1)-dimensional weighting vector w = (w1, . . . , wp+1), and r ≥ 1. Then, sc(x, y) = ‖(x, y)‖w,∞ with w = (1, . . . , 1, c). To obtain the Wasserstein DRO formulation, the key is to derive the dual norm
90 Distributionally Robust Linear Regression 
of ‖ · ‖w,∞. Hölder’s inequality (Rogers, 1888) will be used for the derivation. We will use the notation z , (x, y). Based on the definition of dual norm, we are interested in solving the following optimization problem for β̃ ∈ Rp+1: 
max z 
z′β̃ 
s.t. ‖z‖w,∞ ≤ 1. (4.23) 
The optimal value of Problem (4.23), which is a function of β̃, gives the dual norm evaluated at β̃. Using Hölder’s inequality, we can write 
z′β̃ = ∑p+1 
i=1 (wizi) 
( 1 wi β̃i ) 
≤ ‖z‖w,∞‖β̃‖w−1,1 
≤ ‖β̃‖w−1,1, 
where w−1 , ( 1 w1 , . . . , 1 
wp+1 ). The last inequality is due to the constraint 
‖z‖w,∞ ≤ 1. It follows that the dual norm of ‖ · ‖w,∞ is just ‖ · ‖w−1,1. Back to our problem setting, using w = (1, . . . , 1, c), and evaluating the dual norm at (−β, 1), we have the following Wasserstein DRO formulation as c→∞: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖(−β, 1)‖w−1,1 = inf 
β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε‖β‖1. 
It follows that regularizing over β implies an infinite transportation cost along y. By contrast, the Wasserstein formulation, which regularizes over the extended regression coefficient (−β, 1), stems from a finite cost along y that is equally weighted with x. We will see the disadvantages of penalizing only β in the analysis of the experimental results. 
To answer Question 3, we will compare with several commonly used regression models that employ the SR loss function, e.g., ridge regression (Hoerl and Kennard, 1970), LASSO (Tibshirani, 1996), and Elastic Net (EN) (Zou and Hastie, 2005). We will also compare against M-estimation (Huber, 1964; Huber, 1973), which uses a variant of the SR loss and is equivalent to solving a weighted least squares problem. These models
4.4. Experiments on the Performance of Wasserstein DRO 91 
will be compared under two different experimental setups, one involving perturbations in both x and y, and the other with perturbations only in x. The purpose is to investigate the behavior of these approaches when the noise in y is substantially reduced. 
We next describe the data generation process. Each training sample has a probability q of being drawn from the outlying distribution, and a probability 1− q of being drawn from the true (clean) distribution. Given the true regression coefficient β∗, we generate the training data as follows: 
 Generate a uniform random variable on [0, 1]. If it is no larger than 1− q, generate a clean sample as follows: 
1. Draw the predictor x ∈ Rp from the normal distribution N (0,Σ), where Σ is the covariance matrix of x, which is just the top left block of the matrix Γ in Assumption N. Specifically, Γ = E[(x, y)(x, y)′] is equal to 
Γ = [ 
Σ Σβ∗ (β∗)′Σ (β∗)′Σβ∗ + σ2 
] , 
with σ2 being the variance of the noise term. In our implementation, Σ has diagonal elements equal to 1 (unit variance) and off-diagonal elements equal to ρ, with ρ the correlation between predictors. 
2. Draw the response variable y from N (x′β∗, σ2). 
 Otherwise, depending on the experimental setup, generate an outlier that is either: 
– Abnormal in both x and y, with outlying distribution: 1. x ∼ N (0,Σ) +N (5e, I), or x ∼ N (0,Σ) +N (0, 0.25I); 2. y ∼ N (x′β∗, σ2) + 5σ. 
– Abnormal only in x: 1. x ∼ N (0,Σ) +N (5e, I); 2. y ∼ N (x′β∗, σ2).
92 Distributionally Robust Linear Regression 
 Repeat the above procedure for N times, where N is the size of the training set. 
To test the generalization ability of various formulations, we generate a test dataset containing M samples from the clean distribution. We are interested in studying the performance of various methods as the following factors are varied: 
 Signal to Noise Ratio (SNR), defined as: 
SNR = (β∗)′Σβ∗ σ2 , 
which is equally spaced between 0.05 and 2 on a log scale. 
 The correlation between predictors: ρ, which takes values in (0.1, 0.2, . . . , 0.9). 
The performance metrics we use include: 
 Mean Squared Error (MSE) on the test dataset, which is defined to be ∑M 
i=1(yi− x′iβ̂)2/M , with β̂ being the estimate of β∗ obtained from the training set, and (xi, yi), i ∈ JMK, being the observations from the test dataset; 
 Relative Risk (RR) of β̂ defined as: 
RR(β̂) , (β̂ − β∗)′Σ(β̂ − β∗) (β∗)′Σβ∗ . 
 Relative Test Error (RTE) of β̂ defined as: 
RTE(β̂) , (β̂ − β∗)′Σ(β̂ − β∗) + σ2 
σ2 . 
 Proportion of Variance Explained (PVE) of β̂ defined as: 
PVE(β̂) , 1− (β̂ − β∗)′Σ(β̂ − β∗) + σ2 
(β∗)′Σβ∗ + σ2 . 
For the metrics that evaluate the accuracy of the estimator, i.e., the RR, RTE and PVE, we list below two types of scores, one achieved by the best possible estimator β̂ = β∗, called the perfect score, and the other one achieved by the null estimator β̂ = 0, called the null score.
4.4. Experiments on the Performance of Wasserstein DRO 93 
 RR: a perfect score is 0 and the null score is 1. 
 RTE: a perfect score is 1 and the null score is SNR+1. 
 PVE: a perfect score is SNR SNR+1 , and the null score is 0. 
All the regularization parameters are tuned on a separate validation dataset using the Median Absolute Deviation (MAD) as a selection criterion, to hedge against the potentially large noise in the validation samples. As to the range of values for the tuned parameters, we borrow ideas from Hastie et al., 2017, where the LASSO was tuned over 50 values ranging from λmax = ‖X′y‖∞ to a small fraction of λmax on a log scale, with X ∈ RN×p the design matrix whose i-th row is x′i, and y = (y1, . . . , yN ) the response vector. In our experiments, this range is properly adjusted for procedures that use the AD loss. Specifically, for Wasserstein `2 and `∞, `1- and `2-regularized LAD, the range of values for the regularization parameter is:√ 
exp ( lin ( log(0.005 ∗ ‖X′y‖∞), log(‖X′y‖∞), 50 
)) , 
where lin(a, b, n) is a function that takes in scalars a, b and n (integer) and outputs a set of n values equally spaced between a and b; the exp function is applied elementwise to a vector. The square root operator is in consideration of the AD loss that is the square root of the SR loss if evaluated on a single sample. 
4.4.1 Dense β∗, Outliers in both x and y 
In this subsection, we choose a dense regression coefficient β∗, set the intercept to β∗0 = 0.3, and the coefficient for each predictor xi to be β∗i = 0.5, i ∈ J20K. The perturbations are present in both x and y. Specifically, the outlying distribution is described by: 
1. x ∼ N (0,Σ) +N (5e, I); 
2. y ∼ N (x′β∗, σ2) + 5σ. 
We generate 10 datasets consisting of N = 100,M = 60 observations. The probability of a training sample being drawn from the outlying
94 Distributionally Robust Linear Regression 
distribution is q = 30%. The mean values of the performance metrics (averaged over the 10 datasets), as we vary the SNR and the correlation between predictors, are shown in Figures 4.2 and 4.3. Note that when SNR is varied, the correlation between predictors is set to 0.8 times a random noise uniformly distributed on the interval [0.2, 0.4]. When the correlation ρ is varied, the SNR is fixed to 0.5. 
It can be seen that as the SNR decreases or the correlation between the predictors increases, the estimation problem becomes harder, and the performance of all approaches gets worse. In general the Wasserstein formulation with an `2-norm transportation cost achieves the best performance in terms of all four metrics. Specifically, 
 it is better than the `2-regularized LAD, which assumes an infinite transportation cost along y; 
 it is better than the Wasserstein `∞ and `1-regularized LAD which use the `1-regularizer; 
 it is better than the approaches that use the SR loss function. 
Empirically we have found that in most cases, the approaches that use the AD loss, including the `1- and `2-regularized LAD, and the Wasserstein `∞ formulation, drive all the coordinates of β to zero, due to the relatively small magnitude of the AD loss compared to the norm of the coefficient. The approaches that use the SR loss, e.g., ridge regression and EN, do not exhibit such a problem, since the squared residuals weaken the dominance of the regularization term. 
Overall the `2-regularizer outperforms the `1-regularizer, since the true regression coefficient is dense, which implies that a proper distance metric on the (x, y) space should take into account all the coordinates. From the perspective of the Wasserstein DRO framework, the `1-regularizer corresponds to an ‖ · ‖∞-based distance metric on the (x, y) space that only picks out the most influential coordinate to determine the closeness between data points, which in our case is not reasonable since every coordinate plays a role (reflected in the dense β∗). In contrast, if β∗ is sparse, using the ‖ · ‖∞ as a distance metric on (x, y) is more appropriate. A more detailed discussion of this will be presented in Sections 4.4.3 and 4.4.4.
4.4. Experiments on the Performance of Wasserstein DRO 95 
10 -1 10 0 
Signal to noise ratio 
10 1 
10 2 
10 3 
M e a n  M 
S E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1  LAD 
l 2  LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
10 -1 10 0 
Signal to noise ratio 
10 -1 
10 0 
10 1 
M e a n  R 
R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
10 -1 10 0 
Signal to noise ratio 
1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
2.4 
2.6 
2.8 
3 
M e a n  R 
T E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
10 -1 10 0 
Signal to noise ratio 
-0.4 
-0.2 
0 
0.2 
0.4 
0.6 
0.8 
M e a n  P 
V E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.2: The impact of SNR on the performance metrics: dense β∗, outliers in both x and y.
96 Distributionally Robust Linear Regression 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
50 
100 
150 
200 
250 
300 
350 
400 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
0.5 
1 
1.5 
2 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
-0.2 
-0.1 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
0.8 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.3: The impact of predictor correlation on the performance metrics: dense β∗, outliers in both x and y.
4.4. Experiments on the Performance of Wasserstein DRO 97 
4.4.2 Dense β∗, Outliers Only in x 
In this subsection, we will experiment with the same β∗ as in Sec-tion 4.4.1, but with perturbations only in x. Our goal is to investigate the performance of the Wasserstein formulation when the response y is not subjected to large perturbations. 
Interestingly, we observe that although the `1- and `2-regularized LAD, as well as the Wasserstein `∞ formulation, exhibit unsatisfactory performance, the Wasserstein `2, which shares the same loss function with them, is able to achieve a comparable performance with the best among all – EN and ridge regression (see Figures 4.4 and 4.5). Notably, the `2-regularized LAD, which is just slightly different from the Wasser-stein `2 formulation, shows a much worse performance. This is because the `2-regularized LAD implicitly assumes an infinite transportation cost along y, which gives zero tolerance to the variation in the response. Therefore, a reasonable amount of fluctuation, caused by the intrinsic randomness of y, would be overly exaggerated by the underlying metric used by the `2-regularized LAD. In contrast, the Wasserstein approach uses a proper notion of norm to evaluate the distance in the (x, y) space and is able to effectively distinguish abnormally high variations from moderate, acceptable noise. 
It is also worth noting that the formulations with the AD loss, e.g., `2- and `1-regularized LAD, and the Wasserstein `∞, perform worse than the approaches with the SR loss. One reasonable explanation is that the AD loss, introduced primarily for hedging against large perturbations in y, is less useful when the noise in y is moderate, in which case the sensitivity to response noise is needed. Although the AD loss is not a wise choice, penalizing the extended coefficient vector (−β, 1) seems to make up, making the Wasserstein `2 a competitive method even when the perturbations appear only in x. 
4.4.3 Sparse β∗, Outliers in both x and y 
In this subsection, we will experiment with a sparse β∗. The intercept is set to β∗0 = 3, and the coefficients for the 20 predictors are set to β∗ = (0.05, 0, 0.006, 0,−0.007, 0, 0.008, 0, . . . , 0). The perturbations are present in both x and y. Specifically, the distribution of outliers is
98 Distributionally Robust Linear Regression 
10 -1 10 0 
Signal to noise ratio 
10 1 
10 2 
10 3 
M e a n  M 
S E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1  LAD 
l 2  LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
10 -1 10 0 
Signal to noise ratio 
10 -2 
10 -1 
10 0 
10 1 
M e a n  R 
R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
10 -1 10 0 
Signal to noise ratio 
1 
1.1 
1.2 
1.3 
1.4 
1.5 
1.6 
M e a n  R 
T E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
10 -1 10 0 
Signal to noise ratio 
-0.2 
-0.1 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
M e a n  P 
V E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.4: The impact of SNR on the performance metrics: dense β∗, outliers only in x.
4.4. Experiments on the Performance of Wasserstein DRO 99 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
50 
100 
150 
200 
250 
300 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
0.2 
0.4 
0.6 
0.8 
1 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0.9 
1 
1.1 
1.2 
1.3 
1.4 
1.5 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
0.05 
0.1 
0.15 
0.2 
0.25 
0.3 
0.35 
0.4 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.5: The impact of predictor correlation on the performance metrics: dense β∗, outliers only in x.
100 Distributionally Robust Linear Regression 
characterized by: 
1. x ∼ N (0,Σ) +N (0, 0.25I); 
2. y ∼ N (x′β∗, σ2) + 5σ. 
Our goal is to study the impact of the sparsity of β∗ on the choice of the norm space for the Wasserstein metric. An intuitively appealing interpretation for the sparsity inducing property of the `1-regularizer is made available by the Wasserstein DRO framework, which we explain as follows. The sparse regression coefficient β∗ implies that only a few predictors are relevant to the regression model, and thus when measuring the distance in the (x, y) space, we need a metric that only extracts the subset of relevant predictors. The ‖ · ‖∞, which takes only the most influential coordinate of its argument, roughly serves this purpose. Compared to the ‖·‖2 which takes into account all the coordinates, most of which are redundant due to the sparsity assumption, ‖ · ‖∞ results in a better performance, and hence, the Wasserstein `∞ formulation that induces the `1-regularizer is expected to outperform others. 
We note that the `1-regularized LAD achieves a similar performance, since replacing ‖β‖1 by ‖(−β, 1)‖1 only adds a constant term to the objective function. The generalization performance (mean MSE) of the AD loss-based formulations is consistently better than those with the SR loss, since the AD loss is less affected by large perturbations in y. Also note that choosing a wrong norm for the Wasserstein metric, e.g., the Wasserstein `2, could lead to an enormous estimation error, whereas with a right norm space, the Wasserstein formulation is guaranteed to outperform all others. 
4.4.4 Sparse β∗, Outliers Only in x 
In this subsection, we will use the same sparse coefficient as in Sec-tion 4.4.3, but the perturbations are present only in x. Specifically, for outliers, their predictors and responses are drawn from the following distributions: 
1. x ∼ N (0,Σ) +N (5e, I); 
2. y ∼ N (x′β∗, σ2).
4.4. Experiments on the Performance of Wasserstein DRO 101 
10 -1 10 0 
Signal to noise ratio 
10 -3 
10 -2 
10 -1 
10 0 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
10 -1 10 0 
Signal to noise ratio 
10 -1 
10 0 
10 1 
10 2 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
10 -1 10 0 
Signal to noise ratio 
1 
1.5 
2 
2.5 
3 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
10 -1 10 0 
Signal to noise ratio 
-2 
-1.5 
-1 
-0.5 
0 
0.5 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.6: The impact of SNR on the performance metrics: sparse β∗, outliers in both x and y.
102 Distributionally Robust Linear Regression 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0.005 
0.01 
0.015 
0.02 
0.025 
0.03 
0.035 
0.04 
0.045 
0.05 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
0.5 
1 
1.5 
2 
2.5 
3 
3.5 
4 
4.5 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
1 
1.5 
2 
2.5 
3 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
-1.2 
-1 
-0.8 
-0.6 
-0.4 
-0.2 
0 
0.2 
0.4 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.7: The impact of predictor correlation on the performance metrics: sparse β∗, outliers in both x and y.
4.5. An Application of Wasserstein DRO to Outlier Detection 103 
Not surprisingly, the Wasserstein `∞ and the `1-regularized LAD achieve the best performance. Notice that in Section 4.4.3, where perturbations appear in both x and y, the AD loss-based formulations have smaller generalization and estimation errors than the SR loss-based formulations. When we reduce the variation in y, the SR loss seems superior to the AD loss, if we restrict attention to the improperly regularized (`2-regularizer) formulations (see Figure 4.8). For the `1-regularized formulations, the Wasserstein `∞ formulation, as well as the `1-regularized LAD, is comparable with the EN and LASSO. 
We summarize below our main findings from all sets of experiments we have presented: 
1. When a proper norm space is selected for the Wasserstein metric, the Wasserstein DRO formulation outperforms all others in terms of the generalization and estimation qualities. 
2. Penalizing the extended regression coefficient (−β, 1) implicitly assumes a more reasonable distance metric on (x, y) and thus leads to a better performance. 
3. The AD loss is remarkably superior to the SR loss when there is large variation in the response y. 
4. The Wasserstein DRO formulation shows a more stable estimation performance than others when the correlation between predictors is varied. 
4.5 An Application of Wasserstein DRO to Outlier Detection 
As an application, we consider an unlabeled two-class classification problem, where the goal is to identify the abnormal class of data points based on the predictor and response information using the Wasserstein formulation. We do not know a priori whether the samples are normal or abnormal, and thus classification models do not apply. The commonly used regression model for this type of problem is the M-estimation (Huber, 1964; Huber, 1973), against which we will compare in terms of the outlier detection capability.
104 Distributionally Robust Linear Regression 
10 -1 10 0 
Signal to noise ratio 
0 
0.02 
0.04 
0.06 
0.08 
0.1 
0.12 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
10 -1 10 0 
Signal to noise ratio 
10 -1 
10 0 
10 1 
10 2 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
10 -1 10 0 
Signal to noise ratio 
1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
2.4 
2.6 
2.8 
3 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
10 -1 10 0 
Signal to noise ratio 
-1.4 
-1.2 
-1 
-0.8 
-0.6 
-0.4 
-0.2 
0 
0.2 
0.4 
0.6 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.8: The impact of SNR on the performance metrics: sparse β∗, outliers only in x.
4.5. An Application of Wasserstein DRO to Outlier Detection 105 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0.006 
0.008 
0.01 
0.012 
0.014 
0.016 
0.018 
0.02 
M e 
a n 
 M S 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
l 2 
 LAD 
Wasserstein l inf 
(a) Mean Squared Error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
0 
0.5 
1 
1.5 
2 
2.5 
3 
3.5 
4 
4.5 
M e 
a n 
 R R 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RR 
Null RR 
l 2 
 LAD 
Wasserstein l inf 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
1 
1.5 
2 
2.5 
3 
3.5 
M e 
a n 
 R T 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal RTE 
Null RTE 
l 2 
 LAD 
Wasserstein l inf 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Correlation between predictors 
-1 
-0.8 
-0.6 
-0.4 
-0.2 
0 
0.2 
M e 
a n 
 P V 
E 
Wasserstein l 2 
EN 
LASSO 
Robust Regression 
Ridge 
l 1 
 LAD 
Ideal PVE 
Null PVE 
l 2 
 LAD 
Wasserstein l inf 
(d) Proportion of variance explained. 
Figure 4.9: The impact of predictor correlation on the performance metrics: sparse β∗, outliers only in x.
106 Distributionally Robust Linear Regression 
4.5.1 Experiments on Synthetic Data 
We first report results on synthetic datasets that consist of a mixture of clean and outlying examples. For clean samples, all predictors xi, i ∈ J30K, come from a normal distribution with mean 7.5 and standard deviation 4.0. The response is a linear function of the predictors with β∗0 = 0.3, β∗1 = · · · = β∗30 = 0.5, plus a Gaussian distributed noise term with zero mean and standard deviation σ. The outliers concentrate in a cloud that is randomly placed in the interior of the x-space. Specifically, their predictors are uniformly distributed on (u − 0.125, u + 0.125), where u is a uniform random variable on (7.5− 3× 4, 7.5 + 3× 4). The response values of the outliers are at a δR distance off the regression plane. 
y = β∗0 + β∗1x1 + · · ·+ β∗30x30 + δR. 
We will compare the performance of the Wasserstein `2 formulation (4.5) with the `1-regularized LAD and M-estimation with three cost functions – Huber (Huber, 1964; Huber, 1973), Talwar (Hinich and Talwar, 1975), and Fair (Fair, 1974). The performance metrics include the Receiver Operating Characteristic (ROC) curve which plots the true positive rate against the false positive rate, and the related Area Under Curve (AUC). 
Notice that all the regression methods under consideration only generate an estimated regression coefficient. The identification of outliers is based on the residual and estimated standard deviation of the noise. Specifically, 
Outlier = 
YES, if |residual| > threshold× σ̂, NO, otherwise, 
where σ̂ is the standard deviation of residuals in the entire training set. ROC curves are obtained through adjusting the threshold value. 
The regularization parameters for Wasserstein DRO and regularized LAD are tuned using a separate validation set as done in previous sections. We would like to highlight a salient advantage of the Wasser-stein DRO model reflected in its robustness w.r.t. the choice of ε. In Figure 4.10 we plot the out-of-sample AUC as the radius ε (regularization parameter) varies, for the `2-induced Wasserstein DRO and the
4.5. An Application of Wasserstein DRO to Outlier Detection 107 
`1-regularized LAD. For the Wasserstein DRO curve, when ε is small, the Wasserstein ball contains the true distribution with low confidence and thus AUC is low. On the other hand, too large ε makes the solution overly conservative. Note that the robustness of the Wasserstein DRO, indicated by the flatness of the curve, constitutes another advantage, whereas the performance of LAD dramatically deteriorates once the regularizer deviates from the optimum. Moreover, the maximal achievable AUC for Wasserstein DRO is significantly higher than LAD. 
0 5 10 15 20 25 
Wasserstein ball radius / Regularization coefficient 
0.4 
0.5 
0.6 
0.7 
0.8 
0.9 
1 
A U 
C 
Wasserstein DRO 
Regularized LAD 
Figure 4.10: Out-of-sample AUC v.s. Wasserstein ball radius (regularization coefficient). 
In Figure 4.11 we show the ROC curves for different approaches, where q represents the percentage of outliers, and δR the outlying distance along y. We see that the Wasserstein DRO formulation consistently outperforms all other approaches, with its ROC curve lying well above others. The approaches that use the AD loss function (e.g., Wasser-stein DRO and regularized LAD) tend to outperform those that adopt the SR loss (e.g., M-estimation which uses a variant of the SR loss). M-estimation adopts an Iteratively Reweighted Least Squares (IRLS) procedure which assigns weights to data points based on the residuals from previous iterations. With such an approach, there is a chance of exaggerating the influence of outliers while downplaying the importance
108 Distributionally Robust Linear Regression 
of clean observations, especially when the initial residuals are obtained through OLS. 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(a) q = 20%, δR = 3σ 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(b) q = 30%, δR = 3σ 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(c) q = 20%, δR = 4σ 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(d) q = 30%, δR = 4σ 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(e) q = 20%, δR = 5σ 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
Wasserstein DRO 
Regularized LAD 
Huber 
Talwar 
Fair 
(f) q = 30%, δR = 5σ 
Figure 4.11: ROC curves for outliers in a randomly placed cloud, N = 60, σ = 0.5. 
4.5.2 CT Radiation Overdose Detection 
In this section we consider an application of Wasserstein DRO regression to CT radiation overdose detection (Chen et al., 2019a). The goal is to identify all CT scans with an unanticipated high radiation exposure, given the characteristics of the patient and the type of the exam. This could be cast as an outlier detection problem; specifically, estimating a robustified regression plane that is immunized against outliers and learns the underlying true relationship between radiation dose and the relevant predictors. Given such a regression plane, abnormal CT scans can be identified by the residuals of the regression. 
The data was obtained from a HIPAA-compliant, Institutional Review Board (IRB)-approved retrospective cohort study that was
4.5. An Application of Wasserstein DRO to Outlier Detection 109 
conducted at an academic medical system including a 793-bed quaternary care hospital, and two outpatient imaging facilities. The original de-identified dataset contained 28 fields for 189,959 CT exams, and the per acquisition CT Dose Index (CTDI), which measures the amount of exposure to CT radiation. Mean patient age was 60.6± 17.1 years; 54.7% were females. 
The data was pre-processed as follows: (i) patient visits with more than half of the corresponding variables missing, or a missing value for CTDI, were discarded; (ii) categorical variables were encoded using indicator variables, and categories present only in a small number of exams were deleted; (iii) variables that have low correlation with CTDI were removed from further consideration; (iv) missing values were imputed by the mean (for numerical predictors) or mode (for categorical predictors); (v) all predictors were standardized by subtracting the mean and dividing by the standard deviation. 
After pre-processing, we were left with 606 numerically encoded predictors for 88,566 CT exams. We first applied the variable selection method LASSO to select important variables for predicting CTDI, and then employed the Wasserstein DRO regression approach (induced by the `2 norm) to learn a predictive model of CT radiation doses given important variables identified by LASSO. Patient visits whose predicted radiation dose was statistically different from the radiation dose actually received were identified as outliers. 
To assess the accuracy of the outlier cohort discovery process, we conducted a manual validation in which the results of a human-expert classification were compared to those extracted by the algorithm. A validation sample size of 200 cases were reviewed, yielding specificity of 0.85 [95% CI 0.78-0.92] and sensitivity of 0.91 [95% CI 0.85-0.97] (Positive Predictive Value PPV=0.84, Negative Predictive Value NPV=0.92). 
We compared against two alternatives on the same validation set of 200 samples that were reviewed by the human expert. The first alternative method is what we call a “cutoff” method. We computed the average and standard deviation of CTDI over a training set and identified as outlying exams where the CTDI was larger than the average plus 3 times the standard deviation. The second alternative method used OLS in lieu of the Wasserstein DRO regression, and the regression
110 Distributionally Robust Linear Regression 
residuals (this time from OLS) were used to detect outliers. The results are reported in Table 4.1, showing an improvement of 72.5% brought by the Wasserstein DRO method in terms of the F1 score, which is defined as the harmonic mean of sensitivity and PPV. For an additional point of comparison, we considered the top-40 outliers identified by each method. Among these outliers, 7 of the top-40 OLS outliers (17.5%) were considered to be “false positives”; while all the top-40 outliers detected by Wasserstein DRO were real outliers. 
Table 4.1: Comparison of Wasserstein DRO regression against OLS and the cutoff method on CT radiation data. 
Sensitivity Specificity PPV NPV F1 score Wasserstein `2 0.91 0.85 0.84 0.92 0.88 OLS 0.36 0.95 0.87 0.64 0.51 Cutoff 0.37 0.94 0.83 0.64 0.51 
4.6 Summary 
In this section, we presented a novel `1-loss based robust learning procedure using Distributionally Robust Optimization (DRO) under the Wasserstein metric in a linear regression setting, through which a delicate connection between the metric space on data and the regularization term has been established. The Wasserstein formulation incorporates a class of models whose specific form depends on the norm space that the Wasserstein metric is defined on. We provide out-of-sample generalization guarantees, and bound the estimation bias of the general formulation. Extensive numerical examples demonstrate the superiority of the Wasserstein formulation and shed light on the advantages of the `1-loss, the implication of the regularizer, and the selection of the norm space for the Wasserstein metric. We also presented an outlier detection example as an application of this robust learning procedure. A remarkable advantage of this approach rests in its flexibility to adjust the form of the regularizer based on the characteristics of the data.
5 
Distributionally Robust Grouped Variable 
Selection 
In this section, we will discuss a special case of the general formulation (4.5) tailored for selecting grouped variables that are relevant to the response when there exists a predefined grouping structure for the predictors. An example of this is the encoding of a categorical predictor using a group of indicator variables. Jointly selecting/dropping all variables in a group gives rise to more interpretable models. To perform variable selection at a group level, the Grouped LASSO (GLASSO) was proposed by Bakin, 1999; Yuan and Lin, 2006, which imposes a block-wise `2-normed penalty for the grouped coefficient vectors. We will show that by using a special norm (‖ · ‖2,∞) on the data space, the Wasserstein DRO formulation recovers the GLASSO penalty under the absolute residual loss (regression) and the log-loss (classification). The resulting model offers robustness explanations for GLASSO algorithms and highlights the connection between robustification and regularization. 
5.1 The Problem and Related Work 
The Grouped LASSO (GLASSO) was first proposed by Bakin, 1999; Yuan and Lin, 2006 to induce sparsity at a group level, when there exists a predefined grouping structure for the predictors. Suppose the predictor 
111
112 Distributionally Robust Grouped Variable Selection 
x = (x1, . . . ,xL), and the regression coefficient β = (β1, . . . ,βL), where xl,βl ∈ Rpl , l ∈ JLK, respectively represent the predictor and coefficient for group l which contains pl predictors. GLASSO minimizes: 
inf β 
1 N 
N∑ i=1 
(yi − x′iβ)2 + ε ∑L 
l=1 √ pl‖βl‖2, 
where (xi, yi), i ∈ JNK, are N observed samples of (x, y). Several extensions have been explored. In particular, Lin and Zhang, 2006; Yin et al., 2012 considered grouped variable selection in nonparametric models. Zhao et al., 2009; Jacob et al., 2009 explored GLASSO for overlapping groups. The group sparsity in general regression/classification models has also been investigated in several works, see, for example, Kim et al., 2006; Meier et al., 2008; Bertsimas and King, 2017 for GLASSO in logistic regression, and Roth and Fischer, 2008 for GLASSO in generalized linear models. 
Most of the existing works endeavor to modify the GLASSO formulation heuristically to achieve various goals. As an example, Simon et al., 2013 considers a convex combination of the GLASSO and LASSO penalties, called Sparse Grouped LASSO, to induce both group-wise and within group sparsity. Bunea et al., 2014 modified the residual sum of squares to its square root and proposed the Grouped Square Root LASSO (GSRL). However, few of those works were able to provide a rigorous explanation or theoretical justification for the form of the penalty term. 
In this section, we attempt to fill this gap by casting the problem of grouped variable selection into the Wasserstein DRO framework. We show that in Least Absolute Deviation (LAD) and Logistic Regression (LG), for a specific norm-induced Wasserstein metric, the DRO model can be reformulated as a regularized empirical loss minimization problem, where the regularizer coincides with the GLASSO penalty, and its magnitude is equal to the radius of the distributional ambiguity set. Through such a reformulation we establish a connection between regularization and robustness and offer new insights into the GLASSO penalty term. 
We note that such a connection between robustification and regularization has been explored in several works (see Section 4.2), but none
5.2. The Groupwise Wasserstein Grouped LASSO 113 
of them considered grouped variable selection. This section sheds new light on the significance of exploring the group-wise DRO problem. It is worth noting that Blanchet and Kang, 2017a has studied the group-wise regularization estimator with the square root of the expected loss under the Wasserstein DRO framework and recovered the GSRL. Here, we present a more general framework that includes both the LAD and the negative log-likelihood loss functions, and recover the GLASSO penalty in both cases. Moreover, we point out the potential of generalizing such results to a class of loss functions with a finite growth rate. 
The remainder of this section is organized as follows. Section 5.2 introduces the Wasserstein GLASSO formulations for LAD and LG. Section 5.3 establishes a desirable grouping effect, showing that the difference between coefficients within the same group converges to zero as O( 
√ 1− ρ), where ρ is their sample correlation. In light of this result, 
we use the spectral clustering algorithm to divide the predictors into a pre-specified number of groups. This renders the GLASSO algorithm completely data-driven, in the sense that no more information other than the data itself is needed. Section 5.4 presents numerical results on both synthetic data and a real very large dataset with surgery-related medical records. Conclusions are in Section 5.5. 
5.2 The Groupwise Wasserstein Grouped LASSO 
In this section we describe the model setup and derive what we call the Groupwise Wasserstein Grouped LASSO (GWGL) formulation. We will consider a LAD regression model for continuous responses and an LG model for binary categorical responses. In Section 5.2.3, we present a GWGL formulation for overlapping groups. 
5.2.1 GWGL for Continuous Response Variables 
We assume that the predictors belong to L prescribed groups with group size pl, l ∈ JLK, i.e., x = (x1, . . . ,xL), where xl ∈ Rpl and∑L l=1 pl = p (no overlap among groups). The regression coefficient is 
β = (β1, . . . ,βL), where βl ∈ Rpl denotes the regression coefficient for
114 Distributionally Robust Grouped Variable Selection 
group l. Similar to Section 4, we assume 
y = x′β∗ + η. 
The main assumption we make regarding β∗ is that it is group sparse, i.e., βl = 0 for l in some subset of JLK. Our goal is to obtain an accurate estimate of β∗ under perturbations on the data, when the predictors have a predefined grouping structure. We model stochastic disturbances on the data via distributional uncertainty, and apply a Wasserstein DRO framework to inject robustness into the solution. The learning problem is formulated as: 
inf β 
sup Q∈Ω 
EQ[|y − x′β| ] , 
where Q is the probability distribution of z = (x, y), belonging to some set Ω defined as: 
Ω = Ωs,1 ε (P̂N ) , {Q ∈ P(Z) : Ws,1(Q, P̂N ) ≤ ε}, (5.1) 
and the order-one Wasserstein distance Ws,1(Q, P̂N ) is defined on the metric space (Z, s) associated with the data points z. To reflect the group structure of the predictors and to take into account the group sparsity requirement, we adopt a specific notion of norm to define the metric s. Specifically, for a vector z with a group structure z = (z1, . . . , zL), define its (q, t)-norm, with q, t ≥ 1, as: 
‖z‖q,t = (∑L 
l=1 
( ‖zl‖q 
)t)1/t . 
Notice that the (q, t)-norm of z is actually the `t-norm of the vector (‖z1‖q, . . . , ‖zL‖q), which represents each group vector zl in a concise way via the `q-norm. 
Inspired by the LASSO where the `1-regularizer is used to induce sparsity on the individual level, we wish to deduce an `1-norm penalty on the group level from (4.5) to induce group sparsity on β∗. This motivates the use of the (2,∞)-norm on the weighted predictor-response vector 
zw , ( 1 √ p1 
x1, . . . , 1 √ pL 
xL,My 
) ,
5.2. The Groupwise Wasserstein Grouped LASSO 115 
where the weight vector is 
w = ( 1 √ p1 , . . . , 
1 √ pL ,M 
) , 
and M is a positive weight assigned to the response. Specifically, 
‖zw‖2,∞ = max { 
1 √ p1 ‖x1‖2, . . . , 
1 √ pL ‖xL‖2,M |y| 
} . (5.2) 
In (5.2) we normalize each group by the number of predictors, to prevent large groups from having a large impact on the distance metric. The ‖ · ‖2,∞ operator computes the maximum of the `2 norms of the (weighted) grouped predictors and the response. It essentially selects the most influential group when determining the closeness between two points in the predictor-response space, which is consistent with our group sparsity assumption in that not all groups of predictors contribute to the determination of y, and thus a metric that ignores the unimportant groups (e.g., ‖ · ‖2,∞) is desired. 
Based on (4.5), in order to obtain the GWGL formulation, we need to derive the dual norm of ‖ · ‖2,∞. A general result that applies to any (q, t)-norm is presented in the following theorem. The dual norm of the (2,∞)-norm is a direct application of Theorem 5.2.1. 
Theorem 5.2.1. Consider a vector x = (x1, . . . ,xL), where each xl ∈ Rpl , and ∑l pl = p. Define the weighted (r, s)-norm of x with the weight vector w = (w1, . . . , wL) to be: 
‖xw‖r,s = (∑L 
l=1 
( ‖wlxl‖r 
)s)1/s , 
where xw = (w1x1, . . . , wLxL), wl > 0, ∀l, and r, s ≥ 1. Then, the dual norm of the weighted (r, s)-norm with weight w is the (q, t)-norm with weight w−1, where 1/r + 1/q = 1, 1/s + 1/t = 1, and w−1 = (1/w1, . . . , 1/wL). 
Proof. The dual norm of ‖ · ‖r,s evaluated at some vector β is the optimal value of Problem (5.3): 
max x 
x′β 
s.t. ‖xw‖r,s ≤ 1. (5.3)
116 Distributionally Robust Grouped Variable Selection 
We assume that β has the same group structure with x, i.e., β = (β1, . . . ,βL). Using Hölder’s inequality, we can write 
x′β = ∑L 
l=1 (wlxl)′ 
( 1 wl βl ) 
≤ ∑L 
l=1 ‖wlxl‖r 
∥∥∥∥ 1 wl βl ∥∥∥∥ q . 
Define two new vectors in RL 
xnew = (‖w1x1‖r, . . . , ‖wLxL‖r), 
βnew = (∥∥∥∥ 1 
w1 β1 ∥∥∥∥ q , . . . , 
∥∥∥∥ 1 wL βL ∥∥∥∥ q 
) . 
Applying Hölder’s inequality again to xnew and βnew, we obtain: 
x′β ≤ x′newβnew ≤ ‖xnew‖s‖βnew‖t 
= (∑L 
l=1 
( ‖wlxl‖r 
)s)1/s ∑L 
l=1 
(∥∥∥∥ 1 wl βl ∥∥∥∥ q 
)t1/t 
. 
Therefore, x′β ≤ ‖xw‖r,s‖βw−1‖q,t ≤ ‖βw−1‖q,t, 
due to the constraint ‖xw‖r,s ≤ 1. The result then follows. 
Now, let us go back to (5.2), which is the weighted (2,∞)-norm of z = (x1, . . . ,xL, y) with the weight w = ( 1√ 
p1 , . . . , 1√ 
pL ,M). According 
to Theorem 5.2.1, the dual norm of the weighted (2,∞)-norm with weight w evaluated at some β̃ = (−β1, . . . ,−βL, 1) is: 
‖β̃w−1‖2,1 = ∑L 
l=1 √ pl‖βl‖2 + 1 
M , 
where w−1 = (√p1, . . . , √ pL, 1/M). Therefore, with N i.i.d. samples 
(xi, yi), i ∈ JNK, the GWGL formulation for Linear Regression (GWGL-LR) takes the following form: 
inf β 
1 N 
N∑ i=1 |yi − x′iβ|+ ε 
∑L 
l=1 √ pl‖βl‖2, (5.4)
5.2. The Groupwise Wasserstein Grouped LASSO 117 
where the constant term 1/M has been removed. We see that by using the weighted (2,∞)-norm in the predictor-response space, we are able to recover the commonly used penalty term for GLASSO (Bakin, 1999; Yuan and Lin, 2006). The Wasserstein DRO framework offers new interpretations for the GLASSO penalty from the standpoint of the distance metric on the predictor-response space and establishes the connection between group sparsity and distributional robustness. 
5.2.2 GWGL for Binary Response Variables 
In this subsection we will explore the GWGL formulation for binary classification problems. Let x ∈ Rp denote the predictor and y ∈ {−1,+1} the associated binary response/label to be predicted. In LG, the conditional distribution of y given x is modeled as 
P(y|x) = ( 1 + exp(−yβ′x) 
)−1 , 
where β ∈ Rp is the unknown coefficient vector (classifier) to be estimated. The Maximum Likelihood Estimator (MLE) of β is found by minimizing the negative log-likelihood (logloss): 
hβ(x, y) = log(1 + exp(−yβ′x)). 
To apply the Wasserstein DRO framework, we define the distance metric on the predictor-response space as follows. 
s((x1, y1), (x2, y2)) , ‖x1 − x2‖+M |y1 − y2|, ∀(x1, y1), (x2, y2) ∈ Z, (5.5) 
where M is an infinitely large positive number (different from Sec-tion 5.2.1 where M could be any positive number), and Z = Rp × {−1,+1}. We use a very large weight on y to emphasize its role in determining the distance between data points, i.e., for a pair (xi, yi) and (xj , yj), if yi 6= yj , they are considered to be infinitely far away from each other; otherwise their distance is determined solely by the predictors. The robust LG problem is modeled as: 
inf β 
sup Q∈Ω 
EQ[ log(1 + exp(−yβ′x)) ] , (5.6) 
where Ω is defined in (5.1) with s specified in (5.5). Based on the discussion in Section 3.1, in order to derive a tractable reformulation
118 Distributionally Robust Grouped Variable Selection 
for (5.6), we need to bound the growth rate of hβ(x, y):∣∣hβ(x1, y1)− hβ(x2, y2) ∣∣ 
s((x1, y1), (x2, y2)) , ∀(x1, y1), (x2, y2). 
To this end, we define a continuous and differentiable univariate function l(a) , log(1 + exp(−a)), and apply the mean value theorem to it, which yields that for any a, b ∈ R, ∃c ∈ (a, b) such that:∣∣∣∣ l(b)− l(a) 
b− a 
∣∣∣∣ = ∣∣∇l(c)∣∣ = e−c 
1 + e−c ≤ 1. 
By noting that hβ(x, y) = l(yβ′x), we immediately have:∣∣hβ(x1, y1)− hβ(x2, y2) ∣∣ ≤ ∣∣y1β 
′x1 − y2β ′x2 ∣∣ 
≤ ‖y1x1 − y2x2‖‖β‖∗ ≤ s((x1, y1), (x2, y2))‖β‖∗, 
(5.7) 
where the second step uses Hölder’s inequality, and the last step is due to the definition of the metric s and the fact that M is infinitely large. Eq. (5.7) shows that the loss function hβ(x, y) is Lipschitz continuous in (x, y) with a Lipschitz constant ‖β‖∗. Using Theorem 3.1.1 with t = 1, we obtain that for any Q ∈ Ω,∣∣∣EQ[hβ(x, y) 
] − EP̂N [hβ(x, y) 
]∣∣∣ ≤ ‖β‖∗Ws,1(Q, P̂N ) ≤ ε‖β‖∗. 
Therefore, Problem (5.6) can be reformulated as: 
inf β 
EP̂N [hβ(x, y) ] +ε‖β‖∗ = inf 
β 
1 N 
∑N 
i=1 log ( 1+exp(−yiβ′xi) 
) +ε‖β‖∗. 
(5.8) We note that Abadeh et al., 2015; Shafieezadeh-Abadeh et al., 2017; 
Gao et al., 2017 arrive at a similar formulation to (5.8) by other means of derivation. Different from these existing works, we will consider specifically the application of (5.8) to grouped predictors where the goal is to induce group level sparsity on the coefficients/classifier. As in Section 5.2.1, we assume that the predictor vector x can be decomposed into L groups, i.e., x = (x1, . . . ,xL), each xl containing pl predictors of group l, and ∑L 
l=1 pl = p. To reflect the group sparse structure, we adopt the (2,∞)-norm of the weighted predictor vector 
xw , ( 1 √ p1 
x1, . . . , 1 √ pL 
xL ) ,
5.2. The Groupwise Wasserstein Grouped LASSO 119 
to define the metric s in (5.5), where the weight vector is: 
w = ( 1 √ p1 , . . . , 
1 √ pL 
) . 
According to Theorem 5.2.1, the dual norm of the weighted (2,∞)-norm with weight w = (1/√p1, . . . , 1/ 
√ pL) evaluated at β is: 
‖βw−1‖2,1 = ∑L 
l=1 √ pl‖βl‖2, 
where w−1 = (√p1, . . . , √ pL), and βl denotes the vector of coefficients 
corresponding to group l. Therefore, the GWGL formulation for LG (GWGL-LG) takes the form: 
inf β 
1 N 
∑N 
i=1 log ( 1 + exp(−yiβ′xi) 
) + ε 
∑L 
l=1 √ pl‖βl‖2. (5.9) 
The above derivation techniques also apply to other loss functions whose growth rate is finite, e.g., the hinge loss used by SVM, and therefore, the GWGL SVM model can be developed in a similar fashion. 
5.2.3 GLASSO with Overlapping Groups 
In this subsection we will explore the GLASSO formulation with overlapping groups, and show that the Wasserstein DRO framework recovers a latent GLASSO approach that is proposed by Obozinski et al., 2011 to induce a solution with support being the union of predefined overlapping groups of variables. 
When the groups overlap with each other, the penalty term used by (5.4) and (5.9) leads to a solution whose support is almost surely the complement of a union of groups, see Jenatton et al., 2011. That is to say, setting one group to zero shrinks its covariates to zero even if they belong to other groups, in which case these other groups will not be entirely selected. Obozinski et al., 2011 proposed a latent GLASSO approach where they introduce a set of latent variables that induce a solution vector whose support is a union of groups, so that the estimator would select entire groups of covariates. Specifically, define the latent variables vl ∈ Rp such that supp(vl) ⊂ gl, l ∈ JLK, where supp(vl) ⊂ JpK denotes the support of vl, i.e., the set of predictors i ∈ JpK such that
120 Distributionally Robust Grouped Variable Selection 
vli 6= 0, and gl denotes the set of predictors that are in group l. Our assumption is that ∃ l1, l2 such that gl1 ∩ gl2 6= ∅. The latent GLASSO formulation is in the following form: 
inf β,v1,...,vL 
1 N 
N∑ i=1 
hβ(xi, yi) + ε L∑ l=1 
dl‖vl‖2, 
s.t. β = L∑ l=1 
vl, (5.10) 
where dl is a user-specified penalty strength of group l. Notice that (5.4) and (5.9) are special cases of (5.10) where they require the latent vectors to have the same value at the intersecting covariates. By using the latent vectors vl, Formulation (5.10) has the flexibility of implicitly adjusting the support of the latent vectors such that for any i ∈ supp(v̂l) where v̂l = 0, it does not belong to the support of any non-shrunk latent vectors, i.e., i /∈ supp(v̂k) where v̂k 6= 0. As a result, the covariates that belong to both shrunk and non-shrunk groups would not be mistakenly driven to zero. Formulation (5.10) favors solutions which shrink some vl to zero, while the non-shrunk components satisfy supp(vl) = gl, therefore leading to estimators whose support is the union of a set of groups. 
To show that (5.10) can be obtained from the Wasserstein DRO framework, we consider the following weighted (2,∞)-norm on the predictor space: 
s(x) = max l d−1 l ‖x 
l‖2. (5.11) 
For simplicity we treat the response y as a deterministic quantity so that the Wasserstein metric is defined only on the predictor space. The scenario with stochastic responses can be treated in a similar fashion as in Sections 5.2.1 and 5.2.2 by introducing some constant M . Obozinski et al., 2011 showed that the dual norm of (5.11) is: 
Ω(β) , ∑L 
l=1 dl‖vl‖2, 
with β = ∑L l=1 vl, and β → Ω(β) is a valid norm. By noting that (5.10)
5.3. Performance Guarantees to the DRO Groupwise Estimator 121 
can be reformulated as: 
inf β 
1 N 
N∑ i=1 
lβ(xi, yi) + εΩ(β), (5.12) 
with Ω(β) = min 
v1,...,vL,∑L 
l=1 vl=β 
∑L 
l=1 dl‖vl‖2, 
we have shown that (5.10) can be derived as a consequence of the Wasserstein DRO formulation with the Wasserstein metric induced by (5.11). In fact, Obozinski et al., 2011 pointed out that (5.12) is equivalent to a regular GLASSO in a covariate space of higher dimension obtained by duplication of the covariates belonging to several groups. For simplicity our subsequent analysis assumes non-overlapping groups. 
5.3 Performance Guarantees to the DRO Groupwise Estimator 
In this section we establish several performance guarantees for the solutions to GWGL-LR and GWGL-LG. We are interested in two types of performance metrics: 
(1) Prediction quality, which measures the predictive power of the GWGL solutions on new, unseen samples. 
(2) Grouping effect, which measures the similarity of the estimated coefficients in the same group as a function of the sample correlation between their corresponding predictors. Ideally, for highly correlated predictors in the same group, it is desired that their coefficients are close so that they can be jointly selected/dropped (group sparsity). 
We note that GWGL-LR is a special case of the general Wasser-stein DRO formulation (4.5), and thus the two types of performance guarantees derived in Section 4.3, one for generalization ability (Theo-rem 4.3.3), and the other for the estimation accuracy (Theorem 4.3.12), still apply to the GWGL-LR formulation. For GWGL-LG, we will derive its prediction performance result using similar techniques.
122 Distributionally Robust Grouped Variable Selection 
5.3.1 Performance Guarantees for GWGL-LR 
The prediction and estimation performance of the GWGL-LR model can be described by Theorems 4.3.3 and 4.3.12, where the Wasserstein metric is defined using the weighted (2,∞)-norm with weight w = (1/√p1, . . . , 1/ 
√ pL,M). We thus omit the statement of these two results. 
With Theorem 4.3.12, we are able to provide bounds for the Relative Risk (RR), Relative Test Error (RTE), and Proportion of Variance Explained (PVE) that are introduced in Section 4.4. All these metrics evaluate the accuracy of the regression coefficient estimates on a new test sample drawn from the same probability distribution as the training samples. 
Using Theorem 4.3.12, we can bound the term (β̂ − β∗)′Σ(β̂ − β∗) as follows: 
(β̂ − β∗)′Σ(β̂ − β∗) ≤ λmax(Σ)‖β̂ − β∗‖22 
≤ λmax(Σ) (4R2B̄ 
λmin Ψ(β∗) 
)2 , 
(5.13) 
where λmax(Σ) is the maximum eigenvalue of Σ. Using (5.13), bounds for RR, RTE, and PVE can be readily obtained and are summarized in the following corollary. 
Corollary 5.3.1. Under the specifications in Theorem 4.3.12, when the sample size 
N ≥ C̄1µ̄ 4µ2 
0 λmax λmin 
(w(A(β∗)) + 3)2, 
with probability at least 1− exp(−C2N/µ̄ 4), 
RR(β̂) ≤ λmax(Σ) 
( 4R2B̄ λmin 
Ψ(β∗) )2 
(β∗)′Σβ∗ , 
RTE(β̂) ≤ λmax(Σ) 
( 4R2B̄ λmin 
Ψ(β∗) )2 
+ σ2 
σ2 , 
and, 
PVE(β̂) ≥ 1− λmax(Σ) 
( 4R2B̄ λmin 
Ψ(β∗) )2 
+ σ2 
(β∗)′Σβ∗ + σ2 ,
5.3. Performance Guarantees to the DRO Groupwise Estimator 123 
where all parameters are defined in the same way as in Theorem 4.3.12. 
We next proceed to investigate the grouping effect of the GWGL-LR estimator. The next theorem provides a bound on the absolute (weighted) difference between coefficient estimates as a function of the sample correlation between their corresponding predictors. 
Theorem 5.3.2. Suppose the predictors are standardized (columns of X have zero mean and unit variance). Let β̂ ∈ Rp be the optimal solution to (5.4). If x,i is in group l1 and x,j is in group l2, and ‖β̂ 
l1‖2 6= 0, ‖β̂l2‖2 6= 0, define: 
D(i, j) = ∣∣∣∣∣ √ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
∣∣∣∣∣. Then, 
D(i, j) ≤ √ 
2(1− ρ)√ Nε 
, 
where ρ = x′,ix,j is the sample correlation, and pl1 , pl2 are the number of predictors in groups l1 and l2, respectively. 
Proof. By the optimality condition associated with formulation (5.4), β̂ satisfies: 
x′,isgn(y−Xβ̂) = Nε √ pl1 
β̂i 
‖β̂l1‖2 , (5.14) 
x′,jsgn(y−Xβ̂) = Nε √ pl2 
β̂j 
‖β̂l2‖2 , (5.15) 
where the sgn(·) function is applied to a vector elementwise. Subtracting (5.15) from (5.14), we obtain: 
(x,i − x,j)′sgn(y−Xβ̂) = Nε 
(√ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
) . 
Using the Cauchy-Schwarz inequality and ‖x,i − x,j‖22 = 2(1− ρ), we
124 Distributionally Robust Grouped Variable Selection 
obtain 
D(i, j) = ∣∣∣∣∣ √ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
∣∣∣∣∣ ≤ 1 Nε ‖x,i − x,j‖2‖sgn(y−Xβ̂)‖2 
≤ √ 
2(1− ρ)√ Nε 
. 
When x,i and x,j are in the same group l and ‖β̂l‖2 6= 0, Theo-rem 5.3.2 yields 
|β̂i − β̂j | ≤ √ 
2(1− ρ)‖β̂l‖2 ε √ Npl 
. (5.16) 
From (5.16) we see that as the within group correlation ρ increases, the difference between β̂i and β̂j becomes smaller. In the extreme case where x,i and x,j are perfectly correlated, i.e., ρ = 1, β̂i = β̂j . This grouping effect enables recovery of sparsity on a group level when the correlation between predictors in the same group is high, and implies the use of predictors’ correlation as a grouping criterion. One of the popular clustering algorithms, called spectral clustering (Shi and Malik, 2000; Meila and Shi, 2001; Ng et al., 2002; Ding, 2004) performs grouping based on the eigenvalues/eigenvectors of the Laplacian matrix of the similarity graph that is constructed using the similarity matrix of data (predictors). The similarity matrix measures the pairwise similarities between data points, which in our case could be the pairwise correlations between predictors. 
5.3.2 Performance Guarantees for GWGL-LG 
In this subsection we establish bounds on the prediction error of the GWGL-LG solution, and explore its grouping effect. We will use the Rademacher complexity of the class of logloss (negative log-likelihood) functions to bound the generalization error. Suppose (x, y) is drawn from the probability measure P∗. Two assumptions that impose conditions
5.3. Performance Guarantees to the DRO Groupwise Estimator 125 
on the magnitude of the regularizer and the uncertainty level of the predictor are needed. 
Assumption O. The weighted (2,∞)-norm of x is bounded above, i.e., ‖xw‖2,∞ ≤ Rx a.s. under P∗X ,, where w = (1/√p1, . . . , 1/ 
√ pL). 
Assumption P. The weighted (2, 1)-norm of β with weight w−1 = (√p1, . . . , 
√ pL) is bounded above, namely, supβ ‖βw−1‖2,1 = B̄1. 
Under these two assumptions, the logloss could be bounded via the definition of dual norm. 
Lemma 5.3.3. Under Assumptions O and P, it follows that under the probability measure P∗, 
log ( 1 + exp(−yβ′x) 
) ≤ log 
( 1 + exp(RxB̄1) 
) , a.s.. 
Now consider the following class of loss functions: 
H = { 
(x, y)→ hβ(x, y) : hβ(x, y) = log ( 1 + exp(−yβ′x) 
) , 
∀β s.t. ‖βw−1‖2,1 ≤ B̄1 } . 
It follows from Lemma 4.3.2 that the empirical Rademacher complexity of H, denoted by RN (H), can be upper bounded by: 
RN (H) ≤ 2 log 
( 1 + exp(RxB̄1) 
) √ N 
. 
Then, applying Theorem 4.3.4 (Theorem 8 in Bartlett and Mendelson, 2002), we have the following result on the prediction error of the GWGL-LG estimator. 
Theorem 5.3.4. Let β̂ be an optimal solution to (5.9), obtained using N training samples (xi, yi), i ∈ JNK. Suppose we draw a new i.i.d. sample (x, y). Under Assumptions O and P, for any 0 < δ < 1, with probability at least 1− δ with respect to the sampling, 
EP∗[ log ( 1 + exp(−yx′β̂) 
)] ≤ 1 N 
∑N 
i=1 log 
( 1 + exp(−yix′iβ̂) 
) + 
2 log ( 1 + exp(RxB̄1) 
) √ N 
+ log ( 1 + exp(RxB̄1) 
)√8 log(2/δ) N 
,
126 Distributionally Robust Grouped Variable Selection 
and for any ζ > 2 log(1+exp(RxB̄1))√ N 
+ log ( 1 + exp(RxB̄1) 
)√8 log(2/δ) N , 
P ( log 
( 1 + exp(−yx′β̂) 
) ≥ 1 N 
∑N 
i=1 log 
( 1 + exp(−yix′iβ̂) 
) + ζ 
) ≤ 
1 N 
∑N i=1 log 
( 1 + exp(−yix′iβ̂) 
) + 2 log(1+exp(RxB̄1))√ 
N 1 N 
∑N i=1 log 
( 1 + exp(−yix′iβ̂) 
) + ζ 
+ 
log ( 1 + exp(RxB̄1) 
)√8 log(2/δ) N 
1 N 
∑N i=1 log 
( 1 + exp(−yix′iβ̂) 
) + ζ 
. 
The next result, similar to Theorem 5.3.2, establishes the grouping effect of the GWGL-LG estimator. Theorem 5.3.5. Suppose the predictors are standardized (columns of X have zero mean and unit variance). Let β̂ ∈ Rp be the optimal solution to (5.9). If x,i is in group l1 and x,j is in group l2, and ‖β̂ 
l1‖2 6= 0, ‖β̂l2‖2 6= 0, define: 
D(i, j) = ∣∣∣∣∣ √ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
∣∣∣∣∣. Then, 
D(i, j) ≤ √ 
2(1− ρ)√ Nε 
, 
where ρ = x′,ix,j is the sample correlation between predictors i and j, and pl1 , pl2 are the number of predictors in groups l1 and l2, respectively. Proof. By the optimality condition associated with formulation (5.9), β̂ satisfies:∑N 
k=1 exp(−ykx′kβ̂) 
1 + exp(−ykx′kβ̂) ykxk,i = Nε 
√ pl1 
β̂i 
‖β̂l1‖2 , (5.17) 
∑N 
k=1 exp(−ykx′kβ̂) 
1 + exp(−ykx′kβ̂) ykxk,j = Nε 
√ pl2 
β̂j 
‖β̂l2‖2 , (5.18) 
where xk,i and xk,j denote the i-th and j-th elements of xk, respectively. Subtracting (5.18) from (5.17), we obtain:∑N 
k=1 exp(−ykx′kβ̂) 
1 + exp(−ykx′kβ̂) ( ykxk,i − ykxk,j 
) = Nε 
(√ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
) . 
(5.19)
5.4. Numerical Experiments 127 
Note that the LHS of (5.19) can be written as v′1v2, where 
v1 = ( exp(−y1x′1β̂) 
1 + exp(−y1x′1β̂) , . . . , 
exp(−yNx′N β̂) 1 + exp(−yNx′N β̂) 
) , 
and, v2 = 
( y1(x1,i − x1,j), . . . , yN (xN,i − xN,j) 
) . 
Using the Cauchy-Schwarz inequality and ‖x,i − x,j‖22 = 2(1− ρ), we obtain 
D(i, j) = ∣∣∣∣∣ √ pl1 β̂i 
‖β̂l1‖2 − √ pl2 β̂j 
‖β̂l2‖2 
∣∣∣∣∣ ≤ 1 Nε ‖v1‖2‖v2‖2 
≤ 1 Nε 
√ N‖x,i − x,j‖2 
= √ 
2(1− ρ)√ Nε 
. 
We see that Theorem 5.3.5 yields the same bound with Theo-rem 5.3.2, and for predictors in the same group, their coefficients converge to the same value as O( 
√ 1− ρ). This encourages group level 
sparsity if predictor correlation is used as a grouping criterion. 
5.4 Numerical Experiments 
In this section we compare the GWGL formulations with other commonly used predictive models. In the linear regression setting, we compare GWGL-LR with models that either (i) use a different loss function, e.g., the traditional GLASSO with an `2-loss (Yuan and Lin, 2006), and the Group Square-Root LASSO (GSRL) (Bunea et al., 2014) that minimizes the square root of the `2-loss; or (ii) do not make use of the grouping structure of the predictors, e.g., the Elastic Net (EN) (Zou and Hastie, 2005), and the LASSO (Tibshirani, 1996). For classification problems, we consider alternatives that minimize the empirical logloss plus penalty terms that do not utilize the grouping structure
128 Distributionally Robust Grouped Variable Selection 
of the predictors, e.g., the `1-regularizer (LG-LASSO), `2-regularizer (LG-Ridge), and their combination (LG-EN). The results on several synthetic datasets and a real large dataset of surgery-related medical records are shown in the subsequent sections. 
5.4.1 GWGL-LR on Synthetic Datasets 
In this subsection, we will compare GWGL-LR with the aforementioned models on several synthetic datasets. The data generation process is described as follows: 
1. Generate β∗ based on the following rule: 
(β∗)l = 
0.5 · epl , if l is even; 0, otherwise, 
where epl is the pl-dimensional vector with all ones. 
2. Generate the predictor x ∈ Rp from the Gaussian distribution Np(0,Σ), where Σ = (σi,j)pi,j=1 has diagonal elements equal to 1, and off-diagonal elements specified as: 
σi,j = 
ρw, if predictors i and j are in the same group; 0, otherwise. 
Here ρw is the correlation between predictors in the same group, which we call within group correlation. The correlation between different groups is set to zero. 
3. Generate the response y as follows: 
y ∼ 
N (x′β∗, σ2), if r ≤ 1− q; N (x′β∗, σ2) + 5σ, otherwise, 
where σ2 is the intrinsic variance of y, r is a uniform random variable on [0, 1], and q is the probability (proportion) of abnormal samples (outliers). 
We generate 10 datasets consisting ofN = 100,Mt = 60 observations and 4 groups of predictors, where N is the size of the training set and
5.4. Numerical Experiments 129 
Mt is the size of the test set. The number of predictors in each group is: p1 = 1, p2 = 3, p3 = 5, p4 = 7, and p = ∑4 
i=1 pi = 16. We are interested in studying the impact of (i) Signal to Noise Ratio (SNR), and (ii) the correlation among predictors in the same group (within group correlation): ρw. The performance metrics we use are: 
 Median Absolute Deviation (MAD) on the test dataset, which is defined to be the median value of |yi − x′iβ̂|, i ∈ JMK, with β̂ being the estimate of β∗ obtained from the training set, and (xi, yi), i ∈ JMK, being the observations from the test dataset; 
 Relative Risk (RR) of β̂; 
 Relative Test Error (RTE) of β̂; 
 Proportion of Variance Explained (PVE) of β̂. 
All the regularization parameters are tuned using a separate validation dataset. As to the range of values for the tuned parameters, we adopt the idea from Section 4.4 and adjust properly for the GLASSO estimators. Specifically, 
 For GWGL and GSRL, the range of values for ε or λ is:√ exp 
( lin ( log(0.005 · ‖X′y‖∞), log(‖X′y‖∞), 50 
))/ max l∈JLK 
pl, 
where lin(a, b, n) is a function that takes in scalars a, b and n 
(integer) and outputs a set of n values equally spaced between a and b; the exp function is applied elementwise to a vector. Compared to LASSO (Hastie et al., 2017), the values are scaled by maxl∈JLK pl, and the square root operation is due to the `1-loss function, or the square root of the `2-loss used in these formulations. 
 For the GLASSO with `2-loss, the range of values for λ is: 
exp ( lin ( log(0.005 · ‖X′y‖∞), log(‖X′y‖∞), 50 
))/√max l∈JLK 
pl.
130 Distributionally Robust Grouped Variable Selection 
We note that before solving for the regression coefficients using various GLASSO formulations, the grouping of predictors needs to be determined. Unlike most of the existing works where the grouping structure is assumed to be known or can be obtained from expert knowledge (Yuan and Lin, 2006; Ma et al., 2007; Bunea et al., 2014), we propose to use a data-driven clustering algorithm to group the predictors based on their sample correlations, as suggested by Theorem 5.3.2. Specifically, we consider the spectral clustering (Shi and Malik, 2000; Meila and Shi, 2001; Ng et al., 2002) algorithm with the following Gaussian similarity function 
Gs(x,i,x,j) , exp ( − ‖x,i − x,j‖22/(2σ2 
s) ) , (5.20) 
where σs is some scale parameter whose selection will be explained later. Notice that for standardized predictors, (5.20) captures the sample pairwise correlations between predictors, since ‖x,i − x,j‖22 = 2 
( 1 − 
cor(x,i,x,j) ) , where cor(x,i,x,j) , x′,ix,j . Using (5.20), we can transform 
the set of predictors into a similarity graph, whose Laplacian matrix will be used for spectral clustering. In our implementation, the k-nearest neighbor similarity graph is constructed, where we connect x,i and x,j with an undirected edge if x,i is among the k-nearest neighbors of x,j (in the sense of Euclidean distance) or if x,j is among the k-nearest neighbors of x,i. The parameter k is chosen such that the resulting graph is connected. The scale parameter σs in (5.20) is set to the mean distance of a point to its k-th nearest neighbor (Von Luxburg, 2007). We assume that the number of clusters is known in order to perform spectral clustering, but in case it is unknown, the eigengap heuristic (Von Luxburg, 2007) can be used, where the goal is to choose the number of clusters c such that all eigenvalues λ1, . . . , λc of the graph Laplacian are very small, but λc+1 is relatively large. The implementation of spectral clustering uses the Matlab package 1 developed according to the tutorial Von Luxburg, 2007. 
We next present the experimental results. For a percentage of outliers q = 20%, 30%, we plot two sets of graphs: 
 The performance metrics, i.e., out-of-sample MAD, RR, RTE, and 1https://www.mathworks.com/matlabcentral/fileexchange/34412-fast-and-
efficient-spectral-clustering.
5.4. Numerical Experiments 131 
PVE, v.s. SNR, where the SNR values are equally spaced between 0.5 and 2 on a log scale. Note that when SNR is varied, the within group correlation between predictors is set to 0.8 times a random noise uniformly distributed on the interval [0.2, 0.4]. 
 The performance metrics v.s. within group correlation ρw, where ρw takes values in (0.1, 0.2, . . . , 0.9). When ρw is varied, SNR is fixed to 1. 
Results for varying the SNR are shown in Figures 5.1 and 5.2. Results for varying the within group correlation are shown in Figures 5.3 and 5.4. 
To better highlight the benefits of GWGL-LR, in Tables 5.1 and 5.2 we summarize the Maximum Percentage Improvement (MPI) brought about by our methods compared to other procedures, when varying the SNR and ρw, respectively. In all tables, the number outside the parentheses is the MPI value corresponding to each metric, while the number in the parentheses indicates the value of SNR/ρw at which the MPI is attained. For each performance metric, the MPI is defined as the maximum percentage difference of the performance between GWGL-LR and the best among all others. 
Table 5.1: Maximum percentage improvement of all metrics when varying the SNR. 
MAD RR RTE PVE q = 20% 13.7 (0.5) 41.4 (1.47) 13.1 (1.47) 68.9 (0.79) q = 30% 14.7 (1.08) 40.9 (1.08) 17 (1.08) 85.7 (0.68) 
We summarize below our main findings from the results we have presented: 
 For all approaches under consideration, MAD and RR decrease as the data becomes less noisy. PVE increases when the noise is reduced. 
 The GWGL-LR formulation has better prediction and estimation performances than all other approaches under consideration.
132 Distributionally Robust Grouped Variable Selection 
Table 5.2: Maximum percentage improvement of all metrics when varying the within group correlation. 
MAD RR RTE PVE q = 20% 8.2 (0.1) 80.5 (0.9) 31.8 (0.9) 145.4 (0.9) q = 30% 10.2 (0.1) 41.9 (0.1) 16.7 (0.1) 162.5 (0.1) 
 The relative improvement of GWGL-LR over GLASSO (with an `2-loss) is more significant for highly noisy data (with low SNR values or a high percentage of outliers), which can be attributed to the `1-loss function it uses. Moreover, GWGL-LR generates more stable estimators than GLASSO. 
 When the within group correlation is varied, GWGL-LR shows a more stable performance than others. 
5.4.2 GWGL-LG on Synthetic Datasets 
In this subsection we explore the GWGL-LG formulation on synthetic datasets. The data generation process is described as follows: 
1. Generate β∗ based on the following rule: 
β∗k = 
U [2.5, 7], if β∗k ∈ (β∗)l where l is even; 0, otherwise, 
where U [2.5, 7] stands for a random variable that is uniformly distributed on the interval [2.5, 7]. 
2. Generate the predictor x ∈ Rp from the Gaussian distribution Np(0,Σ), where Σ = (σi,j)pi,j=1 has diagonal elements equal to 1, and off-diagonal elements specified as: 
σi,j = 
0.9, if predictors i and j are in the same group; 0, otherwise.
5.4. Numerical Experiments 133 
3. Generate the response y as follows: 
y ∼ 
B ([ 
1 + e−(x′β∗+N (0,σ2))]−1) , if r ≤ 1− q; 
B(0.5), otherwise, 
where B(p) stands for the Bernoulli distribution with the probability of success p; σ2 = (β∗)′Σβ∗; r is a uniform random variable on [0, 1]; and q is the probability (proportion) of abnormal samples (outliers). 
We generate 10 datasets consisting of 100 observations and 4 groups of predictors, 80% of which constitute the training dataset, and the remaining forming the test set. The number of predictors in each group is: p1 = 3, p2 = 4, p3 = 6, p4 = 7, and p = ∑4 
i=1 pi = 20. The following performance metrics will be used to evaluate the prediction and estimation quality of the solutions: 
 The Correct Classification Rate (CCR) on the test dataset, which is defined to be the proportion of test set samples that are correctly classified by the classifier β̂, with a threshold 0.5 on the predicted probability of success. 
 The AUC (Area Under the ROC Curve) on the test dataset. 
 The average logloss on the test set. 
 The Within Group Difference (WGD) of the classifier β̂, defined as: 
WGD(β̂) , 1 |{l : pl ≥ 2}| 
∑ l:pl≥2 
1(pl 2 ) ∑ 
xi,xj∈xl 
∣∣∣∣ β̂i − β̂jx′,ix,j 
∣∣∣∣, where |{l : pl ≥ 2}| denotes the cardinality of the set {l : pl ≥ 2}, and x′,ix,j measures the sample correlation between predictors xi and xj (x,i and x,j are standardized). WGD(β̂) essentially evaluates the ability of β̂ to induce group level sparsity. It is desired that the coefficients in the same group are close so that they can be jointly selected/dropped. Theorem 5.3.5 implies that the higher the correlation, the smaller the difference between the coefficients, and thus, a smaller WGD value would suggest a stronger ability of grouped variable selection.
134 Distributionally Robust Grouped Variable Selection 
Notice that the first three metrics mentioned above evaluate the prediction quality of the classifier, while the last one evaluates its estimation quality. If the true coefficient vector β∗ is known, we will also use the following confusion matrix which summarizes the number of zero/nonzero elements in β̂ that are zero/nonzero in the true coefficient β∗. 
Table 5.3: Confusion Matrix. 
β∗ 
β̂ Nonzero Zero Nonzero True Association (TA) False Association (FA) Zero False Disassociation (FD) True Disassociation (TD) 
Two ratios will be computed using Table 5.3, the True Association Rate (TAR) defined as: 
TAR = TA TA + FD , 
which calculates the proportion of nonzero coefficients that are correctly discovered by the estimator, and the True Disassociation Rate (TDR) defined as: 
TDR = TD FA + TD , 
which calculates the proportion of zero coefficients that are correctly identified as zero by the estimator. 
We compare GWGL-LG with four formulations: the vanilla logistic regression (LG) that minimizes the empirical logloss on the training samples (without penalty), LG-LASSO that imposes an `1-norm regularizer on β, LG-Ridge that uses an `2-norm regularizer, and LG-EN that uses both the `1- and `2- regularizers. All the penalty (regularization) parameters are tuned in the same way as Section 5.4.1. The penalty parameter for GWGL-LG is tuned over 50 values ranging from λm = maxl∈JLK 
( ‖(Xl)′(y−ȳ1)‖2/ 
√ pl ) to a small fraction of λm on a log 
scale (Meier et al., 2008), where Xl consists of the columns of the design matrix X corresponding to group l, y is the vector of training set labels, and ȳ = y′1/N . The maximum penalty parameter λm for LG-LASSO
5.4. Numerical Experiments 135 
is computed by recognizing it as a special case of GWGL-LG where each group contains only one predictor. For LG-Ridge, λm is set to be the square root of the maximum penalty parameter for LG-LASSO, due to the fact that we penalize the square of the `2-norm regularizer in LG-Ridge. The range of penalty parameters for LG-EN is set in a similar way. 
Similar to Section 5.4.1, the spectral clustering algorithm with the Gaussian similarity function (5.20) is used to perform grouping on the predictors. We experiment with two scenarios: (i) q = 20%, and (ii) q = 30%. The results are shown in Tables 5.4 and 5.5, where the number outside the parentheses is the mean value across 10 repetitions, and the number in the parentheses is the corresponding standard deviation. 
Table 5.4: The performances of different classification formulations on synthetic datasets, q = 20%. 
CCR AUC logloss WGD TAR TDR LG 0.62 
(0.14) 0.67 (0.13) 
0.87 (0.24) 
1.71 (0.32) 
1.00 (0.00) 
0.00 (0.00) 
LG-LASSO 0.69 (0.14) 
0.77 (0.12) 
0.60 (0.13) 
0.33 (0.19) 
0.54 (0.19) 
0.42 (0.23) 
LG-Ridge 0.67 (0.12) 
0.72 (0.14) 
0.69 (0.19) 
0.82 (0.42) 
1.00 (0.00) 
0.01 (0.04) 
LG-EN 0.70 (0.15) 
0.77 (0.13) 
0.59 (0.13) 
0.23 (0.08) 
0.57 (0.21) 
0.42 (0.24) 
GWGL-LG 0.68 (0.15) 
0.79 (0.12) 
0.59 (0.14) 
0.13 (0.07) 
0.98 (0.04) 
0.28 (0.34) 
We see that in general, the penalized formulations perform significantly better than the vanilla logistic regression. LG-EN has very similar prediction performance (i.e., CCR, AUC and logloss on the test set) to GWGL-LG, better than LG-LASSO and LG-Ridge. Regarding the estimation quality, the penalized formulations achieve much lower WGD values than LG. LG-Ridge does not induce sparsity, and therefore has the highest WGD among the four regularized models. LG-LASSO shows a relatively small WGD, due to the sparsity inducing (at the individual level) property of the `1-regularizer. GWGL-LG achieves the smallest WGD among all (significantly lower than that of LG-EN), which
136 Distributionally Robust Grouped Variable Selection 
Table 5.5: The performances of different classification formulations on synthetic datasets, q = 30%. 
CCR AUC logloss WGD TAR TDR LG 0.63 
(0.09) 0.68 (0.08) 
0.99 (0.21) 
2.68 (0.51) 
1.00 (0.00) 
0.00 (0.00) 
LG-LASSO 0.73 (0.08) 
0.73 (0.08) 
0.65 (0.11) 
0.56 (0.37) 
0.58 (0.21) 
0.43 (0.23) 
LG-Ridge 0.72 (0.06) 
0.74 (0.06) 
0.64 (0.10) 
0.78 (0.58) 
0.98 (0.04) 
0.00 (0.00) 
LG-EN 0.74 (0.08) 
0.77 (0.06) 
0.59 (0.08) 
0.24 (0.09) 
0.48 (0.14) 
0.42 (0.23) 
GWGL-LG 0.73 (0.08) 
0.78 (0.06) 
0.60 (0.09) 
0.21 (0.16) 
0.99 (0.03) 
0.18 (0.09) 
provides empirical evidence on its group sparsity inducing property, and is consistent with our earlier discussion in Theorem 5.3.5 that the GLASSO penalty tends to drive the coefficients in the same group to the same value if the within group correlation is high. Moreover, GWGL-LG successfully drops out all the coefficients in the first group, while other formulations are not able to drop any of the four groups. 
Regarding the TAR and TDR, we notice that GWGL-LG obtains very high TAR values, and compared to other formulations that achieve almost perfect TARs (e.g., LG-Ridge and LG), it has a significantly higher TDR. LG-LASSO and LG-EN achieve the highest TDRs, but their TARs are significantly worse. Note that a dense estimator would result in a perfect TAR but a zero TDR, as in LG and LG-Ridge. The higher the TDR, the more parsimonious the model is, but on the other hand, a higher TAR is more appreciated as we do not want to leave out any of the important (effective) predictors. A low TAR means that a substantial proportion of the meaningful predictors are dropped, the cost of which is usually much higher than the cost of wrongly selecting the unimportant ones. Therefore, taking into account both the parsimony and effectiveness of the model, GWGL-LG outperforms all others. 
We also want to highlight the robustness of GWGL-LG to misspecified groups. For example, in the scenario with q = 30% outliers, even though spectral clustering outputs a wrong grouping structure (it divides
5.4. Numerical Experiments 137 
the data into four groups with group size being p1 = 2, p2 = 3, p3 = 5, p4 = 10, and the correct group size is p1 = 3, p2 = 4, p3 = 6, p4 = 7), GWGL-LG is still able to achieve a satisfactory prediction performance and an almost perfect TAR with a sparse model (nonzero TDR). 
5.4.3 An Application to Hospital Readmission 
In this section we test the GWGL formulations on a real dataset containing medical records of patients who underwent a general surgical procedure. In 2005, the American College of Surgeons (ACS) established the National Surgical Quality Improvement Program (NSQIP), which collects detailed demographic, laboratory, clinical, procedure and postoperative occurrence data in several surgical subspecialties. The dataset includes (i) baseline demographics; (ii) pre-existing comorbidity information; (iii) preoperative variables; (iv) index admission-related diagnosis and procedure information; (v) postoperative events and complications, and (vi) additional socioeconomic variables. 
In our study, patients who underwent a general surgery procedure over 2011–2014 and were tracked by the NSQIP were identified. We will focus on two supervised learning models: (i) a linear regression model whose objective is to predict the post-operative hospital length of stay using pre- and intra-operative variables, and (ii) an LG model whose objective is to predict the re-hospitalization of patients within 30 days after discharge using the same set of explanatory variables. Both models are extremely useful as they allow hospital staff to predict post-operative bed occupancy and prevent costly 30-day readmissions. 
Data were pre-processed as follows: (i) categorical variables (such as race, discharge destination, insurance type) were numerically encoded and units homogenized; (ii) missing values were replaced by the mode; (iii) all variables were normalized by subtracting the mean and divided by the standard deviation; (iv) patients who died within 30 days of discharge or had a postoperative length of stay greater than 30 days were excluded. After pre-processing, we were left with a total of 2, 275, 452 records. 
After encoding the categorical predictors using indicator variables, we have 131 numerical predictors for the regression model and 132 for the
138 Distributionally Robust Grouped Variable Selection 
classification model (the post-operative hospital length of stay is used as a predictor for the 30-day re-hospitalization prediction). The spectral clustering algorithm is used to perform grouping on the predictors, with the number of groups specified as 67 based on a preliminary analysis of the data. (The eigengap heuristic (Von Luxburg, 2007) mentioned in Section 5.4.1 was used.) 
For predicting the post-operative hospital length of stay, we report the out-of-sample MAD in Table 5.6, i.e., the median of the absolute difference between the predicted and actual length of stay on the test set. The mean and standard deviation of the MAD are computed across 5 repetitions, each with a different training set. We see that the GWGL-LR formulation achieves the lowest mean MAD with a small variation. Compared to the best among others (GLASSO with `2-loss), it improves the mean MAD by 7.30%. For longer hospital length of stay, this could imply 1 or 2 days improvement in prediction accuracy, which is both clinically and economically meaningful and significant. 
Table 5.6: The Mean and standard deviation of out-of-sample MAD on the surgery data. 
Mean Standard Deviation GLASSO with `2-loss 0.17 0.0007 
GWGL-LR 0.16 0.001 EN 0.17 0.0009 
LASSO 0.17 0.0009 GSRL 0.17 0.0009 
For predicting the 30-day re-hospitalization of patients, we notice that the dataset is highly unbalanced, with only 6% of patients being re-hospitalized. To obtain a balanced training set, we randomly draw 20% patients from the positive class (re-hospitalized patients), and sample the same number of patients from the negative class, resulting in a training set of size 53, 616. All the remaining patients go to the test dataset. It turns out that the prediction capabilities of all approaches are very similar. All formulations achieve an average out-of-sample CCR
5.5. Summary 139 
around 0.62, an average out-of-sample AUC of 0.83, and an average logloss on the test set ranging from 0.84 to 0.87. From Table 5.7 we see that GWGL-LG obtains a significantly smaller WGD than others, which implies that the GWGL-LG formulation encourages group level sparsity. This can also be revealed by the number of groups that are dropped by various formulations (see Table 5.8). Notice that though LG-EN and LG-LASSO obtain the most parsimonious models in terms of the number of dropped features (sparsity at an individual level), GWGL-LG has a stronger ability to induce group level sparsity. 
Table 5.7: The Within Group Difference (WGD) of the estimators on the surgery data. 
Mean Standard Deviation LG 23.93 1.28 
LG-LASSO 16.28 0.72 LG-Ridge 23.38 1.15 LG-EN 16.26 0.74 
GWGL-LG 5.04 0.45 
Table 5.8: The number of groups/features dropped by various formulations on the surgery data. 
Number of dropped groups Number of dropped features LG 1 2 
LG-LASSO 6 24 LG-Ridge 2 2 LG-EN 10 25 
GWGL-LG 16 19 
5.5 Summary 
In this section we presented a Distributionally Robust Optimization (DRO) formulation under the Wasserstein metric that recovers the
140 Distributionally Robust Grouped Variable Selection 
GLASSO penalty for Least Absolute Deviation (LAD) and LG, through which we have established a connection between group-sparse regularization and robustness and offered new insights into the group sparsity penalty term. We provided insights on the grouping effect of the estimators, which suggests the use of spectral clustering with the Gaussian similarity function to perform grouping on the predictors. We established finite-sample bounds on the prediction errors, which justify the form of the regularizer and provide guidance on the number of training samples needed in order to achieve specific out-of-sample accuracy. 
We reported results from several experiments, using both synthetic data and a real dataset with surgery-related medical records. It has been observed that the GWGL formulations (i) achieve more accurate and stable estimates compared to others, especially when the data are noisy, or potentially contaminated with outliers; (ii) have a stronger ability of inducing group-level sparsity, and thus producing more interpretable models, and (iii) successfully identify most of the effective predictors with a reasonably parsimonious model.
5.5. Summary 141 
0.5 1 1.5 2 
Signal to noise ratio 
1.5 
2 
2.5 
3 
3.5 
4 
4.5 
M e 
a n 
 M A 
D 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
(a) Median Absolute Deviation. 
0.5 1 1.5 2 
Signal to noise ratio 
0 
0.2 
0.4 
0.6 
0.8 
1 
1.2 
1.4 
1.6 
1.8 
2 
M e 
a n 
 R R 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RR 
Null RR 
(b) Relative risk. 
0.5 1 1.5 2 
Signal to noise ratio 
1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
2.4 
2.6 
2.8 
3 
M e 
a n 
 R T 
E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RTE 
Null RTE 
(c) Relative test error. 
0.5 1 1.5 2 
Signal to noise ratio 
-0.3 
-0.2 
-0.1 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
M e 
a n 
 P V 
E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal PVE 
Null PVE 
(d) Proportion of variance explained. 
Figure 5.1: The impact of SNR on the performance metrics, q = 20%.
142 Distributionally Robust Grouped Variable Selection 
0.5 1 1.5 2 
Signal to noise ratio 
1.5 
2 
2.5 
3 
3.5 
4 
4.5 
M e 
a n 
 M A 
D 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
(a) Median Absolute Deviation. 
0.5 1 1.5 2 
Signal to noise ratio 
0 
0.2 
0.4 
0.6 
0.8 
1 
1.2 
1.4 
1.6 
1.8 
2 
M e 
a n 
 R R 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RR 
Null RR 
(b) Relative risk. 
0.5 1 1.5 2 
Signal to noise ratio 
1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
2.4 
2.6 
2.8 
3 
M e 
a n 
 R T 
E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RTE 
Null RTE 
(c) Relative test error. 
0.5 1 1.5 2 
Signal to noise ratio 
-0.3 
-0.2 
-0.1 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
M e 
a n 
 P V 
E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal PVE 
Null PVE 
(d) Proportion of variance explained. 
Figure 5.2: The impact of SNR on the performance metrics, q = 30%.
5.5. Summary 143 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
1.5 
2 
2.5 
3 
3.5 
4 
M e a n  M 
A D 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
(a) Median Absolute Deviation. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
0 
0.5 
1 
1.5 
M e a n  R 
R 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RR 
Null RR 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
1 
1.5 
2 
2.5 
M e a n  R 
T E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RTE 
Null RTE 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
M e a n  P 
V E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal PVE 
Null PVE 
(d) Proportion of variance explained. 
Figure 5.3: The impact of within group correlation on the performance metrics, q = 20%.
144 Distributionally Robust Grouped Variable Selection 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
2 
2.5 
3 
3.5 
4 
4.5 
5 
M e a n  M 
A D 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
(a) Median Absolute Deviation. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
0 
0.5 
1 
1.5 
M e a n  R 
R 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RR 
Null RR 
(b) Relative risk. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
1 
1.5 
2 
2.5 
M e a n  R 
T E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal RTE 
Null RTE 
(c) Relative test error. 
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 
Within group correlation 
0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
M e a n  P 
V E 
GLASSO 
GWGL-LR 
EN 
LASSO 
GSRL 
Ideal PVE 
Null PVE 
(d) Proportion of variance explained. 
Figure 5.4: The impact of within group correlation on the performance metrics, q = 30%.
6 
Distributionally Robust Multi-Output Learning 
In this section, we focus on robust multi-output learning where a multidimensional response/label vector is to be learned. The difference from previous sections lies in that we need to estimate a coefficient matrix, rather than a coefficient vector, to explain the dependency of each response variable on the set of predictors. We develop Distributionally Robust Optimization (DRO) formulations under the Wasserstein metric for Multi-output Linear Regression (MLR) and Multiclass Logistic Re-gression (MLG), when both the covariates and responses/labels may be contaminated by outliers. Through defining a new notion of matrix norm, we relax the DRO formulation into a regularized learning problem whose regularizer is the norm of the coefficient matrix, establishing a connection between robustness and regularization and generalizing the single-output results presented in Section 4. 
6.1 The Problem and Related Work 
We consider the multi-output learning problem under the framework of Distributionally Robust Optimization (DRO) where the ambiguity set is defined via the Wasserstein metric (Gao and Kleywegt, 2016; Gao et al., 2017; Shafieezadeh-Abadeh et al., 2017; Esfahani and Kuhn, 2018). The 
145
146 Distributionally Robust Multi-Output Learning 
term multi-output learning refers to scenarios where multiple correlated responses are to be predicted - Multi-output Linear Regression (MLR), or one of multiple classes is to be assigned - MultiClass Classification (MCC), based on a linear combination of a set of predictors. Both involve learning a target vector y from a vector of covariates x. MLR has many applications in econometrics (Zhang et al., 2013), health care (Hidalgo and Goodman, 2013; Peng et al., 2010), and finance (Islam et al., 2013; Tsay, 2013), for modeling multiple measurements of a single individual (Friston et al., 1994), or evaluating a group of interdependent variables (Breiman and Friedman, 1997). MCC has seen wide applications in image segmentation (Plath et al., 2009), text classification (Forman, 2003), and bioinformatics (Li et al., 2004). 
Unlike a single-output learning problem where the response variable is scalar and a coefficient vector representing the dependency of the response on the predictors is to be learned, in the multi-output setting the decision variable is a coefficient matrix B ∈ Rp×K whose k-th column explains the variation in the k-th coordinate of y ∈ RK that can be attributed to the predictors x ∈ Rp, for k ∈ JKK. Inspired by the DRO relaxation derived in Section 4 for the single-output case, which adds a dual norm regularizer to the empirical loss, we obtain a novel matrix norm regularizer for the multi-output case through reformulating the Wasserstein DRO problem. The matrix norm exploits the geometrical structure of the coefficient matrix, and provides a way of associating the coefficients for the potentially correlated responses through the dual norm of the distance metric in the data space. 
As the simplest MLR model, the multi-output extension of OLS regresses each response variable against the predictors independently, which does not take into account the potential correlation between the responses, and is vulnerable to high correlations existing among the predictors. A class of methods that are used in the literature to overcome this issue is called linear factor regression, where the response y is regressed against a small number of linearly transformed predictors (factors). Examples include reduced rank regression (Izenman, 1975; Velu and Reinsel, 2013), principal components regression (Massy, 1965), and Factor Estimation and Selection (FES) (Yuan et al., 2007). Another type of methods applies multivariate shrinkage by either estimating a
6.1. The Problem and Related Work 147 
linear transformation of the OLS predictions (Breiman and Friedman, 1997), or solving a regularized MLR problem, e.g., ridge regression (Brown, Zidek, et al., 1980; Haitovsky, 1987), and FES (Yuan et al., 2007), whose regularizer is the coefficient matrix’s Ky Fan norm defined as the sum of its singular values. 
As for the popular MCC models, Aly, 2005 provided a thorough survey on the existing MCC techniques which can be categorized into: (i) transformation to binary, e.g., one vs. rest and one vs. one; (ii) extension from binary, e.g., decision trees (Breiman, 2017), neural networks (Bishop, 1995), K-Nearest Neighbor (Bay, 1998), Naive Bayes classifiers (Rish et al., 2001), and Support Vector Machine (SVM) (Cortes and Vapnik, 1995); and (iii) hierarchical classification (Kumar et al., 2002). 
The research on robust classification has mainly focused on binary classifiers. For example, to robustify logistic regression, Feng et al., 2014 proposed to optimize a robustified linear correlation between the response y and a linear function of x; Ding et al., 2013 introduced T-logistic regression which replaces the exponential distribution in LG by the t-exponential distribution family; Tibshirani and Manning, 2013 introduced a shift parameter for each data point to account for the label error; and Bootkrajang and Kabán, 2012 modeled the label error through flipping probabilities, which can be extended to multiclass LG. Another line of research uses a modified loss function that gives less influence to points far from the boundary, e.g., Masnadi-Shirazi et al., 2010 used a tangent loss, Pregibon, 1982 proposed an M-estimator like loss metric which, however, is not robust to outliers with high leverage covariates. 
None of the aforementioned works, however, explore distributionally robust learning problems with multiple responses, with the exception of Hu et al., 2016, which considered distributionally robust multiclass classification models under the φ-divergence metric. We fill this gap by developing DRO formulations for both MLR and MCC under the Wasserstein metric. To the best of our knowledge, we are the first to study the robust multi-output learning problem from the standpoint of distributional robustness. Our approach is completely optimization-based, without the need to explicitly model the complicated relationship between different
148 Distributionally Robust Multi-Output Learning 
responses, leading to compact and computationally solvable models. It is interesting that a purely optimization-based method that is completely agnostic to the covariate and response correlation structure can be used as a better-performing alternative to statistical approaches that explicitly model this correlation structure. 
The rest of this Section is organized as follows. In Section 6.2, we develop the DRO-MLR and DRO-MLG formulations and introduce the matrix norm that is used to define the regularizer. Section 6.3 establishes the out-of-sample performance guarantees for the solutions to DRO-MLR and DRO-MLG. The numerical experimental results are presented in Section 6.4. We conclude in Section 6.5. 
6.2 Distributionally Robust Multi-Output Learning Models 
In this section we introduce the Wasserstein DRO formulations for MLR and MLG, and offer a dual norm interpretation for the regularization terms. 
6.2.1 Distributionally Robust Multi-Output Linear Regression 
We assume the following model for the MLR problem: 
y = B′x + η, 
where y = (y1, . . . , yK) is the vector of K responses, potentially correlated with each other; x = (x1, . . . , xp) is the vector of p predictors; B = (Bij)j∈JKK 
i∈JpK is the p × K matrix of coefficients, the j-th column of which describes the dependency of yj on the predictors; and η is the random error. Suppose we observe N realizations of the data, denoted by (xi,yi), i ∈ JNK, where xi = (xi1, . . . , xip),yi = (yi1, . . . , yiK). The Wasserstein DRO formulation for MLR minimizes the following worst-case expected loss: 
inf B 
sup Q∈Ω 
EQ[hB(x,y)], (6.1) 
where hB(x,y) , l(y−B′x), with l : RK → R an L-Lipschitz continuous function on the metric spaces (D, ‖ · ‖r) and (C, | · |), where D, C are
6.2. Distributionally Robust Multi-Output Learning Models 149 
the domain and codomain of l(·), respectively; and Q is the probability distribution of the data (x,y), belonging to a set Ω defined as 
Ω = Ωs,1 ε (P̂N ) , {Q ∈ P(Z) : Ws,1(Q, P̂N ) ≤ ε}, 
where the order-1 Wasserstein distance Ws,1(Q, P̂N ) is induced by the metric s(z1, z2) , ‖z1 − z2‖r. Notice that we use the same norm to define the Wasserstein metric and the metric space on the domain D of l(·). 
Write the loss function as hB̃(z) , l(B̃z), where z = (x,y), and B̃ = [−B′, IK ]. From Theorem 3.1.1, we know that to derive a tractable reformulation for (6.1), the key is to bound the following growth rate of the loss: 
GR ( hB̃ ) , lim sup ‖z1−z2‖r→∞ 
∣∣hB̃(z1)− hB̃(z2) ∣∣ 
‖z1 − z2‖r . 
Let us first consider the numerator. By the Lipschitz continuity of l(·), we have: 
|hB̃(z1)− hB̃(z2)| = |l(B̃z1)− l(B̃z2)| ≤ L‖B̃(z1 − z2)‖r. 
The key is to bound ‖B̃(z1−z2)‖r in terms of ‖z1−z2‖r. The following lemmata provide three types of bounds whose tightness will be analyzed in the sequel. 
Lemma 6.2.1. For any matrix A ∈ Rm×n and any vector x ∈ Rn, we have: 
‖Ax‖r ≤ ‖x‖r (∑m 
i=1 ‖ai‖r1 
)1/r , 
for any r ≥ 1, where ai, i ∈ JmK, are the rows of A. 
Proof. Suppose A = (aij)j∈JnK i∈JmK. Then, 
‖Ax‖rr = 
∥∥∥∥∥∥∥∥  a11x1 + . . .+ a1nxn 
... am1x1 + . . .+ amnxn 
 ∥∥∥∥∥∥∥∥ r 
r 
= ∑m 
i=1 |ai1x1 + . . .+ ainxn|r 
≤ ‖x‖rr (∑m 
i=1 
( |ai1|+ . . .+ |ain| 
)r) . 
where in the second step we use the fact that |xi| ≤ ‖x‖r.
150 Distributionally Robust Multi-Output Learning 
Lemma 6.2.2. For any matrix A ∈ Rm×n and any vector x ∈ Rn, we have: 
‖Ax‖r ≤ ‖x‖r (∑m 
i=1 ‖ai‖rs 
)1/r , 
for any r ≥ 1, where ai, i ∈ JmK, are the rows of A, and 1/r + 1/s = 1. 
Proof. ‖Ax‖rr = 
∑m 
i=1 |a′ix|r 
≤ ∑m 
i=1 ‖x‖rr‖ai‖rs 
= ‖x‖rr ∑m 
i=1 ‖ai‖rs, 
where r, s ≥ 1, 1/r + 1/s = 1, and the second step uses Hölder’s inequality. 
Lemma 6.2.3. Given an m × n matrix A = (aij)j∈JnK i∈JmK and a vector 
x ∈ Rn, the following holds: 
‖Ax‖r ≤ ‖x‖r‖v‖s, 
where r, s ≥ 1, and 1/r+1/s = 1; v = (v1, . . . , vn), with vj = ∑m i=1 |aij |. 
Proof. Suppose A = (aij)j∈JnK i∈JmK. Then, 
‖Ax‖r = 
∥∥∥∥∥∥∥∥  a11x1 + . . .+ a1nxn 
... am1x1 + . . .+ amnxn 
 ∥∥∥∥∥∥∥∥ r 
= (∑m 
i=1 |ai1x1 + . . .+ ainxn|r 
)1/r 
≤ ((∑m 
i=1 |ai1x1 + . . .+ ainxn| 
)r)1/r 
= ∑m 
i=1 |ai1x1 + . . .+ ainxn| 
≤ |x1| ∑m 
i=1 |ai1|+ . . .+ |xn| 
∑m 
i=1 |ain| 
= |x|′v ≤ ‖x‖r‖v‖s, 
where r, s ≥ 1, 1/r+1/s = 1, |x| = (|x1|, . . . , |xn|), and v = (v1, . . . , vn), with vj = ∑m 
i=1 |aij |. The last step uses Hölder’s inequality and the fact that ‖x‖ = ‖|x|‖.
6.2. Distributionally Robust Multi-Output Learning Models 151 
Note that for any s ≥ 1, we know ‖ai‖s ≤ ‖ai‖1, implying that∑m i=1 ‖ai‖rs ≤ 
∑m i=1 ‖ai‖r1. Therefore, Lemma 6.2.2 provides a tighter 
bound than Lemma 6.2.1. The vector v in the statement of Lemma 6.2.3 can be written as v = ∑m 
i=1 |ai|, where the | · | is applied element-wise to ai. We thus have, 
‖v‖s = ∥∥∥∑m 
i=1 |ai| ∥∥∥ s ≤ ∑m 
i=1 ‖ai‖s. 
It is clear that when r = 1, Lemma 6.2.3 gives a tighter bound than Lemma 6.2.2. However, when r ≥ s, we claim that Lemma 6.2.2 yields a better bound. To see this, notice that 
‖v‖rs = (∑n 
j=1 vsj 
)r/s = (∑n 
j=1 
( |a1j |+ . . .+ |amj | 
)s)r/s ≥ (∑n 
j=1 
( |a1j |s + . . .+ |amj |s 
))r/s = (∑m 
i=1 
( |ai1|s + . . .+ |ain|s 
))r/s ≥ ∑m 
i=1 
( |ai1|s + . . .+ |ain|s 
)r/s = ∑m 
i=1 ‖ai‖rs, 
where in the derivation we have used Lemma 6.2.4. 
Lemma 6.2.4. For any k ≥ 1 and ci ≥ 0, the following holds:(∑m 
i=1 ci )k ≥ ∑m 
i=1 cki . 
Proof. If all ci = 0, the result obviously holds. Without loss of generality, we assume not all ci are equal to zero. Let λ = ∑m 
i=1 ci; then λ > 0. Set bi = ci/λ; then bi ∈ [0, 1], and bki ≤ bi. Together with the fact that∑ i bi = 1, we have: ∑m 
i=1 cki = λk 
∑m 
i=1 bki 
≤ λk ∑m 
i=1 bi 
= λk 
= (∑m 
i=1 ci )k ,
152 Distributionally Robust Multi-Output Learning 
for any k ≥ 1, ci ≥ 0. 
We now proceed to obtain a tractable relaxation to formulation (6.1). Using Lemma 6.2.2 and Theorem 3.1.1, we have:∣∣∣EQ[hB̃(z) 
] − EP̂N [hB̃(z) 
]∣∣∣ ≤ ∫ Z×Z 
∣∣hB̃(z1)− hB̃(z2) ∣∣ 
‖z1 − z2‖r ‖z1 − z2‖rdπ0(z1, z2) 
≤ ∫ Z×Z 
L‖B̃(z1 − z2)‖r ‖z1 − z2‖r 
‖z1 − z2‖rdπ0(z1, z2) 
≤ L (∑K 
i=1 ‖bi‖rs 
)1/r ∫ Z×Z 
‖z1 − z2‖rdπ0(z1, z2) 
= L (∑K 
i=1 ‖bi‖rs 
)1/r Ws,1(Q, P̂N ) 
≤ εL (∑K 
i=1 ‖bi‖rs 
)1/r , ∀Q ∈ Ω, 
where bi = (−B1i, . . . ,−Bpi, ei) is the i-th row of B̃, with ei the i-th unit vector in RK . The above derivation implies that when the Wasserstein metric is induced by ‖ · ‖r, 
sup Q∈Ω 
EQ[hB̃(z)] ≤ EP̂N [hB̃(z) ] 
+ εL (∑K 
i=1 ‖bi‖rs 
)1/r , 
where 1/r + 1/s = 1. This directly yields the following relaxation to (6.1): 
inf B 
1 N 
∑N 
i=1 hB(xi,yi) + εL 
(∑K 
i=1 ‖bi‖rs 
)1/r , (6.2) 
which we call the MLR-SR relaxation. The regularization term in (6.2) penalizes the aggregate of the dual norm of the regression coefficients corresponding to each of the K responses. Notice that when r 6= 1, (6.2) cannot be decomposed into K independent terms. When s = r = 2, the regularizer is just the Frobenius norm of B̃. Using a similar derivation, Lemma 6.2.3 yields the following relaxation to (6.1): 
inf B 
1 N 
∑N 
i=1 hB(xi,yi) + εL‖v‖s, (6.3) 
where v , (v1, . . . , vp, 1, . . . , 1), with vi = ∑K j=1 |Bij |, i.e., vi is a con-
densed representation of the coefficients for predictor i through summing
6.2. Distributionally Robust Multi-Output Learning Models 153 
over the K coordinates. We call (6.3) the MLR-1S relaxation (the naming convention will be more clear after introducing the Lr,s matrix norm in Section 6.2.2). When s 6= 1, it cannot be decomposed into K subproblems due to the entangling of coefficients in the regularization term. 
Note that when K = 1, with an 1-Lipschitz continuous loss function, the two regularizers in MLR-SR and MLR-1S reduce to ε‖(−β, 1)‖s, which coincides with the Wasserstein DRO formulation derived in Section 4 with an absolute error loss. In both relaxations for MLR, the Wasserstein ball radius ε and the Lipschitz constant L determine the strength of the penalty term. Recall that we assume the loss function is Lipschitz continuous on the same norm space with the one used by the Wasserstein metric. This assumption can be relaxed by allowing a different norm space for the Lipschitz continuous loss function, and the derivation technique can be easily adapted to obtain relaxations to (6.1). On the other hand, however, the norm space used by the Wasserstein metric can provide implications on what loss function to choose. For example, if we restrict the class of loss functions l(·) to the norms, our assumption suggests that l(z) = ‖z‖r, which is a reasonable choice since it reflects the distance metric on the data space. 
6.2.2 A New Perspective on the Formulation 
In this subsection we will present a matrix norm interpretation for the two relaxations (6.2) and (6.3). Different from the commonly used matrix norm definitions in the literature, e.g., the vector norm-induced matrix norm ‖A‖ , max‖x‖≤1 ‖Ax‖, the entrywise norm that treats the matrix as a vector, and the Schatten–von-Neumann norm that defines the norm on the vector of singular values (Tomioka and Suzuki, 2013), we adopt the Lr,s norm, which summarizes each column by its `r norm, and then computes the `s norm of the aggregate vector. The formal definition is described as follows. 
Definition 6 (Lr,s Matrix Norm). For any m× n matrix A = (aij)j∈JnK i∈JmK,
154 Distributionally Robust Multi-Output Learning 
define its Lr,s norm as: 
‖A‖r,s , (∑n 
j=1 
(∑m 
i=1 |aij |r 
)s/r)1/s 
, 
where r, s ≥ 1. 
Note that ‖A‖r,s can be viewed as the `s norm of a newly defined vector v = (v1, . . . , vn), where vj = ‖Aj‖r, with Aj the j-th column of A. When r = s = 2, the Lr,s norm is the Frobenius norm. Moreover, ‖A‖r,s is a convex function in A, which can be shown as follows. 
Proof. For two matrices A = [A1, · · · ,An], B = [B1, · · · ,Bn], where Ai,Bi are the columns of A and B, respectively, consider their convex combination λA + (1 − λ)B, where λ ∈ [0, 1]. Its Lr,s norm can be expressed as: 
‖λA + (1− λ)B‖r,s = ∥∥∥(‖λA1 + (1− λ)B1‖r, . . . , ‖λAn + (1− λ)Bn‖r 
)∥∥∥ s 
≤ ∥∥∥(λ‖A1‖r + (1− λ)‖B1‖r, . . . , λ‖An‖r + (1− λ)‖Bn‖r 
)∥∥∥ s 
= ∥∥∥λ(‖A1‖r, . . . , ‖An‖r 
) + (1− λ) 
( ‖B1‖r, . . . , ‖Bn‖r 
)∥∥∥ s 
≤ λ ∥∥∥(‖A1‖r, . . . , ‖An‖r 
)∥∥∥ s 
+ (1− λ) ∥∥∥(‖B1‖r, . . . , ‖Bn‖r 
)∥∥∥ s 
= λ‖A‖r,s + (1− λ)‖B‖r,s. 
Therefore, the Lr,s norm is convex. 
The Lr,s matrix norm depends on the structure of the matrix, and transposing a matrix changes its norm. For example, given A ∈ Rn×1, ‖A‖r,s = ‖a‖r, ‖A′‖r,s = ‖a‖s, where a represents the vectorization of A. To show the validity of the Lr,s norm, we need to verify the following properties: 
1. ‖A‖r,s ≥ 0. 
2. ‖A‖r,s = 0 if and only if A = 0. 
3. ‖αA‖r,s = |α|‖A‖r,s.
6.2. Distributionally Robust Multi-Output Learning Models 155 
4. ‖A + B‖r,s ≤ ‖A‖r,s + ‖B‖r,s. 
The first three properties are straightforward. To show the subadditivity property (triangle inequality), assume A = [A1, · · · ,An] and B = [B1, · · · ,Bn], where Aj ,Bj , j ∈ JnK, are the columns of A and B, respectively. Define two vectors v , (‖A1‖r, . . . , ‖An‖r), and t , (‖B1‖r, . . . , ‖Bn‖r), we have: 
‖A‖r,s + ‖B‖r,s = ‖v‖s + ‖t‖s ≥ ‖v + t‖s 
= (∑n 
i=1 
( ‖Ai‖r + ‖Bi‖r 
)s)1/s 
≥ (∑n 
i=1 ‖Ai + Bi‖sr 
)1/s 
= ‖A + B‖r,s. 
The Lr,s norm also satisfies the following sub-multiplicative property: 
‖AB‖r,s ≤ ‖A‖1,u‖B‖t,s, (6.4) 
for A ∈ Rm×n,B ∈ Rn×K , and any t, u ≥ 1 satisfying 1/t+ 1/u = 1. 
Proof. Assume A ∈ Rm×n, B ∈ Rn×K , and B = [B1, · · · ,BK ], where Bj , j ∈ JKK, are the columns of B. Then, AB = [AB1, · · · ,ABK ], and ‖AB‖r,s = ‖w‖s, where w = (w1, . . . , wK) with wj = ‖ABj‖r. From the proof of Lemma 6.2.3, we immediately have: 
wj = ‖ABj‖r ≤ ‖Bj‖t‖A‖1,u, 
where 1/t+ 1/u = 1. We thus have, 
‖AB‖r,s = (∑K 
j=1 wsj 
)1/s 
≤ (∑K 
j=1 ‖Bj‖st‖A‖s1,u 
)1/s 
= ‖A‖1,u (∑K 
j=1 ‖Bj‖st 
)1/s 
= ‖A‖1,u‖B‖t,s, 
for any t, u ≥ 1 satisfying 1/t+ 1/u = 1.
156 Distributionally Robust Multi-Output Learning 
Next we will reformulate the two relaxations (6.2) and (6.3) using the Lr,s norm. When the Wasserstein metric is defined by ‖ · ‖r, the MLR-SR relaxation can be written as: 
inf B 
1 N 
∑N 
i=1 hB(xi,yi) + εL‖B̃′‖s,r. 
Similarly, the MLR-1S relaxation can be written as: 
inf B 
1 N 
∑N 
i=1 hB(xi,yi) + εL‖B̃‖1,s, 
where r, s ≥ 1 and 1/r+ 1/s = 1. When the loss function is convex, e.g., hB(x,y) = ‖y−B′x‖, it is obvious that both MLR-SR and MLR-1S are convex optimization problems. By using the Lr,s matrix norm, we are able to express the two relaxations in a compact way, which reflects the role of the norm space induced by the Wasserstein metric on the regularizer, and demonstrates the impact of the size of the Wasserstein ambiguity set and the Lipschitz continuity of the loss function on the regularization strength. 
6.2.3 Distributionally Robust Multiclass Logistic Regression 
In this subsection we apply the Wasserstein DRO framework to the problem of Multiclass Logistic Regression (MLG). Suppose there are K classes, and we are given a predictor vector x ∈ Rp. Our goal is to predict its class label, denoted by a K-dimensional binary label vector y ∈ {0, 1}K , where ∑k yk = 1, and yk = 1 if and only if x belongs to class k. The conditional distribution of y given x is modeled as 
p(y|x) = ∏K 
i=1 pyii , 
where pi = ew ′ ix/ 
∑K k=1 e 
w′kx, and wi, i ∈ JKK, are the coefficient vectors to be estimated that account for the contribution of x in predicting the
6.2. Distributionally Robust Multi-Output Learning Models 157 
class labels. The log-likelihood can be expressed as: 
log p(y|x) = ∑K 
i=1 yi log(pi) 
= ∑K 
i=1 yi log ew 
′ ix∑K 
k=1 e w′ k x 
= ∑K 
i=1 yiw′ix− 
( log 
∑K 
k=1 ew ′ kx )∑K 
i=1 yi 
= ∑K 
i=1 yiw′ix− log 
∑K 
k=1 ew ′ kx 
= y′B′x− log 1′eB′x, 
where B , [w1, · · · ,wK ], 1 is the vector of ones, and the exponential operator is applied element-wise to the exponent vector. The log-loss is defined to be the negative log-likelihood, i.e., hB(x,y) , log 1′eB′x − y′B′x. The Wasserstein DRO formulation for MLG minimizes the following worst-case expected loss: 
inf B 
sup Q∈Ω 
EQ [ 
log 1′eB′x − y′B′x ] , (6.5) 
where Ω is defined using the order-1 Wasserstein metric induced by: 
s(z1, z2) = ‖x1 − x2‖r +Msy(y1,y2), 
where z1 = (x1,y1), z2 = (x2,y2), sy(·, ·) could be any metric, and M is a very large positive constant. To make (6.5) tractable, we need to derive an upper bound for the growth rate of the loss function, which involves bounding the following difference 
|hB(x1,y1)− hB(x2,y2)| = | log 1′eB′x1 − y′1B′x1 − log 1′eB′x2 + y′2B′x2| 
≤ | log 1′eB′x1 − log 1′eB′x2 |+ |y′1B′x1 − y′2B′x2|, 
(6.6) 
in terms of s(z1, z2). Let us examine the two terms in (6.6) separately. For the first term, define a function g(a) = log 1′ea, where a ∈ RK . Using the mean value theorem, we know for any a,b ∈ RK , there exists some t ∈ (0, 1) such that 
|g(b)− g(a)| ≤ ∥∥∇g((1− t)a + tb 
)∥∥ s ‖b− a‖r ≤ K1/s‖b− a‖r, (6.7)
158 Distributionally Robust Multi-Output Learning 
where r, s ≥ 1, 1/r + 1/s = 1, the first inequality is due to Hölder’s inequality, and the second inequality is due to the fact that ∇g(a) = ea/1′ea, which implies that each element of ∇g(a) is smaller than 1. Based on (6.7) we have: 
| log 1′eB′x1 − log 1′eB′x2 | ≤ K1/s‖B′(x1 − x2)‖r. 
We can use Lemma 6.2.2 or 6.2.3 to bound ‖B′(x1 − x2)‖r, which respectively leads to the following two results: 
| log 1′eB′x1 − log 1′eB′x2 | ≤ K1/s‖x1 − x2‖r (∑K 
i=1 ‖wi‖rs 
)1/r 
= K1/s‖x1 − x2‖r‖B‖s,r, (6.8) 
and 
| log 1′eB′x1 − log 1′eB′x2 | ≤ K1/s‖x1 − x2‖r‖B′‖1,s, (6.9) 
where r, s ≥ 1 and 1/r+ 1/s = 1. By noting that ‖x1−x2‖r ≤ s(z1, z2), we obtain the upper bound for the first term in (6.6) in terms of s(z1, z2). For the second term, we have, 
|y′1B′x1 − y′2B′x2| = ∣∣∣∑K 
i=1 w′i(y1ix1 − y2ix2) 
∣∣∣ ≤ ∑K 
i=1 |w′i(y1ix1 − y2ix2)| 
≤ ∑K 
i=1 ‖wi‖s‖y1ix1 − y2ix2‖r 
≤ s(z1, z2) ∑K 
i=1 ‖wi‖s 
= s(z1, z2)‖B‖s,1, 
(6.10) 
where y1 = (y11, . . . , y1K),y2 = (y21, . . . , y2K), 1/s+1/r = 1, the second inequality uses the Hölder’s inequality, and the last inequality can be proved by noting that if y1i = y2i, ‖y1ix1−y2ix2‖r ≤ s(z1, z2); otherwise s(z1, z2) goes to infinity. Suppose π0 is the optimal transportation plan that moves the probability mass from Q to P̂N , combining (6.8) with
6.2. Distributionally Robust Multi-Output Learning Models 159 
(6.10), we have:∣∣∣EQ[hB(x,y) ] − EP̂N [hB(x,y) 
]∣∣∣ ≤ ∫ Z×Z 
∣∣hB(x1,y1)− hB(x2,y2) ∣∣dπ0(z1, z2) 
= ∫ Z×Z 
∣∣hB(x1,y1)− hB(x2,y2) ∣∣ 
s(z1, z2) s(z1, z2)dπ0(z1, z2) 
≤ ∫ Z×Z 
( K1/s‖B‖s,r + ‖B‖s,1 
) s(z1, z2)dπ0(z1, z2) 
≤ ε ( K1/s‖B‖s,r + ‖B‖s,1 
) , 
which yields the following MLG-SR relaxation to (6.5): 
inf B 
1 N 
∑N 
i=1 
( log 1′eB′xi − y′iB′xi 
) + ε ( K1/s‖B‖s,r + ‖B‖s,1 
) . 
Similarly, combining (6.9) with (6.10) produces the following MLG-1S relaxation: 
inf B 
1 N 
∑N 
i=1 
( log 1′eB′xi − y′iB′xi 
) + ε ( K1/s‖B′‖1,s + ‖B‖s,1 
) . 
We note that both MLG-SR and MLG-1S are convex optimization problems. The convexity of the regularizer has been shown in Section 6.2.2. The convexity of the log-loss is shown in the following theorem. 
Theorem 6.2.5. The log-loss hB(x,y) , log 1′eB′x − y′B′x is convex in B. 
Proof. Since the linear function is convex, we only need to show the convexity of log 1′eB′x. The following result will be used. 
Corollary 6.2.6. The function f(x) = log(∑n i=1 e 
xi) is a convex function of x ∈ Rn. 
By Corollary 6.2.6, we have for any λ ∈ [0, 1], and any two matrices
160 Distributionally Robust Multi-Output Learning 
B = [B1, · · · ,BK ] and C = [C1, · · · ,CK ], 
log 1′e(λB+(1−λ)C)′x = log (∑K 
i=1 eλB′ix+(1−λ)C′ix 
) = f(λv1 + (1− λ)v2) ≤ λf(v1) + (1− λ)f(v2) 
= λ log (∑K 
i=1 eB ′ ix ) 
+ (1− λ) log (∑K 
i=1 eC ′ ix ) 
= λ log 1′eB′x + (1− λ) log 1′eC′x, 
where v1 = (B′1x, . . . ,B′Kx), and v2 = (C′1x, . . . ,C′Kx). Therefore the log-loss is convex. 
When K = 2, by taking one of the two classes as a reference, we can set one column of B to zero, in which case all three regularizers ‖B‖s,r, ‖B‖s,1 and ‖B′‖1,s reduce to ‖β‖s, where B , [β,0], and the MLG-SR and MLG-1S relaxations coincide with the regularized logistic regression formulation derived in (5.8). 
We also note that the number of classes K, along with the Wasser-stein set radius ε, determines the regularization magnitude in the two MLG relaxations. There are two terms in the regularizer, one accounting for the predictor/feature uncertainty, and the other accounting for the label uncertainty. In the MLG-SR regularizer, we summarize each column of B by its dual norm, and aggregate them by the `r and `1 norms to reflect the predictor and label uncertainties, respectively. 
6.3 The Out-of-Sample Performance Guarantees 
In this section we will show the out-of-sample performance guarantees for the solutions to the MLR and MLG relaxations, i.e., given a new test sample, what is the expected prediction bias/log-loss. The results are established using the Rademacher complexity (Bartlett and Mendelson, 2002), following the line of proof presented in Section 4.3.1. The resulting bounds shed light on the role of the regularizer in inducing a low prediction error.
6.3. The Out-of-Sample Performance Guarantees 161 
6.3.1 Performance Guarantees for MLR Relaxations 
In this subsection we study the out-of-sample predictive performance of the solutions to (6.2) and (6.3). Suppose the data (x,y) is drawn from the probability measure P∗. We first make the following assumptions that are essential for deriving the bounds. 
Assumption Q. The `r-norm of the data (x,y) is bounded above a.s. under the probability measure P∗, i.e., ‖(x,y)‖r ≤ R, a.s.. 
Assumption R. For any feasible solution to MLR-SR, it holds that ‖B̃′‖s,r ≤ B̄s,r. 
Assumption S. For any feasible solution to MLR-1S, it holds that ‖B̃‖1,s ≤ B̄1,s. 
Assumption T. The loss resulting from (x,y) = (0,0) is 0, i.e., hB̃(0) = 0. 
Note that Assumption Q bounds the magnitude of the data in terms of its `r-norm, and R can be assumed to be reasonably small with standardized data input. Assumptions R and S impose restrictions on the norm of the coefficient matrix, which are a result of adding appropriate regularizers into the formulation as in (6.2) and (6.3). Assumption T easily holds when the loss function is defined via some norm, i.e., hB(x,y) , ‖y − B′x‖. Under Assumptions Q, R and T, using Lemma 6.2.2 and the Lipschitz continuity of the loss function, we have 
hB̃(z) ≤ L‖B̃z‖r ≤ L‖z‖r‖B̃′‖s,r ≤ LRB̄s,r. (6.11) Similarly, under Assumptions Q, S and T, Lemma 6.2.3 yields the following: 
hB̃(z) ≤ L‖B̃z‖r ≤ L‖z‖r‖B̃‖1,s ≤ LRB̄1,s. (6.12) 
With the above results, the idea is to bound the out-of-sample prediction error using the empirical Rademacher complexity RN (·) of the class of loss functions: H = {z→ hB̃(z)}, denoted by RN (H). Using Lemma 4.3.2 and the upper bounds in (6.11) and (6.12), we arrive at the following result.
162 Distributionally Robust Multi-Output Learning 
Lemma 6.3.1. Under Assumptions Q, R and T, 
RN (H) ≤ 2LRB̄s,r√ N 
. 
Under Assumptions Q, S and T, 
RN (H) ≤ 2LRB̄1,s√ N 
. 
Using the Rademacher complexity of the class of loss functions, the out-of-sample prediction bias of the solutions to (6.2) and (6.3) can be bounded by applying Theorem 8 in Bartlett and Mendelson, 2002. 
Theorem 6.3.2. Suppose the solution to (6.2) is B̂s,r. Under Assump-tions Q, R and T, for any 0 < δ < 1, with probability at least 1 − δ with respect to the sampling, 
E[hB̂s,r (x,y)] ≤ 1 
N 
∑N 
i=1 hB̂s,r 
(xi,yi)+ 2LRB̄s,r√ N 
+LRB̄s,r 
√ 8 log(2 
δ ) N 
, 
and for any ζ > 2LRB̄s,r√ N 
+ LRB̄s,r 
√ 8 log(2/δ) 
N , 
P ( hB̂s,r 
(x,y) ≥ 1 N 
∑N 
i=1 hB̂s,r 
(xi,yi) + ζ ) 
≤ 1 N 
∑N i=1 hB̂s,r 
(xi,yi) + 2LRB̄s,r√ N 
+ LRB̄s,r 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 hB̂s,r 
(xi,yi) + ζ . 
Theorem 6.3.3. Suppose the solution to (6.3) is B̂1,s. Under Assump-tions Q, S and T, for any 0 < δ < 1, with probability at least 1− δ with respect to the sampling, 
E[hB̂1,s (x,y)] ≤ 1 
N 
∑N 
i=1 hB̂1,s 
(xi,yi)+ 2LRB̄1,s√ N 
+LRB̄1,s 
√ 8 log(2 
δ ) N 
, 
and for any ζ > 2LRB̄1,s√ N 
+ LRB̄1,s 
√ 8 log(2/δ) 
N , 
P ( hB̂1,s 
(x,y) ≥ 1 N 
∑N 
i=1 hB̂1,s 
(xi,yi) + ζ ) 
≤ 1 N 
∑N i=1 hB̂1,s 
(xi,yi) + 2LRB̄1,s√ N 
+ LRB̄1,s 
√ 8 log(2/δ) 
N 
1 N 
∑N i=1 hB̂1,s 
(xi,yi) + ζ .
6.3. The Out-of-Sample Performance Guarantees 163 
Theorems 6.3.2 and 6.3.3 present bounds on the out-of-sample prediction errors of the solutions to (6.2) and (6.3), respectively. The expectations/probabilities are taken w.r.t. the new sample (x,y). The magnitude of the regularizer plays a role in controlling the bias, and a smaller upper bound on the matrix norm leads to a smaller prediction error, suggesting the superiority of MLR-SR for r ≥ 2, and the superiority of MLR-1S for r = 1 (see Section 6.2.1). But on the other hand, the prediction error also depends on the sample average loss over the training set, for which there is no guarantee on which model wins out. In practice we suggest trying both models and selecting the one that yields a smaller error on a validation set. 
6.3.2 Performance Guarantees for MLG Relaxations 
In this subsection, we study the out-of-sample log-loss of the solutions to MLG-SR and MLG-1S. Suppose the data (x,y) is drawn from the probability measure P∗. We first make several assumptions that are needed to establish the results. 
Assumption U. The `r norm of the predictor x is bounded above a.s. under the probability measure P∗X , i.e., ‖x‖r ≤ Rx, a.s.. 
Assumption V. For any feasible solution to MLG-SR, the following holds: 
K1/s‖B‖s,r + ‖B‖s,1 ≤ C̄s,r. 
Assumption W. For any feasible solution to MLG-1S, the following holds: 
K1/s‖B′‖1,s + ‖B‖s,1 ≤ C̄1,s. 
With standardized predictors, Rx in Assumption U can be assumed to be small. The form of the constraints in Assumptions V and W is consistent with the form of the regularizers in MLG-SR and MLG-1S, respectively. We will see later that the bounds C̄s,r and C̄1,s respectively control the out-of-sample log-loss of the solutions to MLG-SR and MLG-1S, which validates the role of the regularizer in improving the out-of-sample performance. Under Assumptions U and V, using (6.6),
164 Distributionally Robust Multi-Output Learning 
(6.8) and (6.10), we have, 
|hB(x,y)− hB(0,y)| ≤ K1/s‖x‖r‖B‖s,r + ‖x‖r‖B‖s,1 ≤ RxC̄s,r. 
By noting that hB(0,y) = logK, we immediately have, 
logK −RxC̄s,r ≤ hB(x,y) ≤ RxC̄s,r + logK. (6.13) 
Similarly, under Assumptions U and W, using (6.6), (6.9) and (6.10), we have, 
|hB(x,y)− hB(0,y)| ≤ K1/s‖x‖r‖B′‖1,s + ‖x‖r‖B‖s,1 ≤ RxC̄1,s, 
which implies that 
logK −RxC̄1,s ≤ hB(x,y) ≤ RxC̄1,s + logK. (6.14) 
Using (6.13) and (6.14), we can now proceed to bound the out-of-sample log-loss using the empirical Rademacher complexity RN (·) of the following class of loss functions: 
H = {(x,y)→ hB(x,y) : hB(x,y) = log 1′eB′x − y′B′x}. 
Lemma 6.3.4. Under Assumptions U and V, 
RN (H) ≤ 2(RxC̄s,r + logK)√ N 
. 
Under Assumptions U and W, 
RN (H) ≤ 2(RxC̄1,s + logK)√ N 
. 
Using Lemma 6.3.4, we are able to bound the out-of-sample log-loss of the solutions to MLG-SR and MLG-1S by applying Theorem 8 in Bartlett and Mendelson, 2002. 
Theorem 6.3.5. Suppose the solution to MLG-SR is B̂s,r. Under As-sumptions U and V, for any 0 < δ < 1, with probability at least 1− δ with respect to the sampling, 
E[log 1′eB̂′s,rx − y′B̂′s,rx] ≤ 1 N 
∑N 
i=1 (log 1′eB̂′s,rxi − y′iB̂′s,rxi) 
+ 2(RxC̄s,r + logK)√ N 
+ (RxC̄s,r + logK) 
√ 8 log(2 
δ ) N 
,
6.3. The Out-of-Sample Performance Guarantees 165 
and for any ζ > 2(RxC̄s,r+logK)√ N 
+ (RxC̄s,r + logK) √ 
8 log( 2 δ 
) N , 
P ( log 1′eB̂′s,rx − y′B̂′s,rx ≥ 
1 N 
∑N 
i=1 (log 1′eB̂′s,rxi − y′iB̂′s,rxi) + ζ 
) ≤ 
1 N 
∑N i=1(log 1′eB̂′s,rxi − y′iB̂′s,rxi) + 2(RxC̄s,r+logK)√ 
N 
1 N 
∑N i=1(log 1′eB̂′s,rxi − y′iB̂′s,rxi) + ζ 
+ (RxC̄s,r + logK) 
√ 8 log( 2 
δ ) 
N 
1 N 
∑N i=1(log 1′eB̂′s,rxi − y′iB̂′s,rxi) + ζ 
. 
Theorem 6.3.6. Suppose the solution to MLG-1S is B̂1,s. Under As-sumptions U and W, for any 0 < δ < 1, with probability at least 1− δ with respect to the sampling, 
E[log 1′eB̂ ′ 1,sx − y′B̂′1,sx] ≤ 1 
N 
∑N 
i=1 (log 1′eB̂ 
′ 1,sxi − y′iB̂′1,sxi) 
+ 2(RxC̄1,s + logK)√ N 
+ (RxC̄1,s + logK) 
√ 8 log(2 
δ ) N 
, 
and for any ζ > 2(RxC̄1,s+logK)√ N 
+ (RxC̄1,s + logK) √ 
8 log( 2 δ 
) N , 
P ( log 1′eB̂ 
′ 1,sx − y′B̂′1,sx ≥ 
1 N 
∑N 
i=1 (log 1′eB̂ 
′ 1,sxi − y′iB̂′1,sxi) + ζ 
) ≤ 
1 N 
∑N i=1(log 1′eB̂ 
′ 1,sxi − y′iB̂′1,sxi) + 2(RxC̄1,s+logK)√ 
N 
1 N 
∑N i=1(log 1′eB̂ 
′ 1,sxi − y′iB̂′1,sxi) + ζ 
+ (RxC̄1,s + logK) 
√ 8 log( 2 
δ ) 
N 
1 N 
∑N i=1(log 1′eB̂ 
′ 1,sxi − y′iB̂′1,sxi) + ζ 
. 
We note that the expected log-loss on a new test sample depends both on the sample average log-loss on the training set, and the magnitude of the regularizer in the formulation. The form of the bounds in Theorems 6.3.5 and 6.3.6 demonstrates the validity of MLG-SR and MLG-1S in leading to a good out-of-sample performance. For r ≥ 2, C̄s,r can be considered smaller than C̄1,s, while for r = 1, the reverse holds. We can decide which model to use on a case-by-case basis, by computing their out-of-sample error on a validation set.
166 Distributionally Robust Multi-Output Learning 
6.4 Numerical Experiments 
In this section, we will test the out-of-sample performance of the MLR and MLG relaxations on a number of synthetic datasets, and compare with several commonly used multi-output regression/classification models. 
6.4.1 MLR Relaxations 
In this subsection we will first explore the selection of a proper norm for the regularizer based on an appropriate notion of distance in the data space. To this end, we design two different structures for the true coefficient matrix denoted by B∗ in order to reflect different distance metrics: 
1. B∗ is drawn from a standard multivariate normal distribution, which corresponds to an `2-norm induced Wasserstein metric (r = 2); 
2. we first generate B∗ from a standard multivariate normal distribution, and then normalize each row using the softmax function while keeping the sign of each element unchanged. The normalization guarantees an equal row absolute sum for B∗. This can be thought of as standardizing the effect of each predictor, which is represented by the absolute sum over the K columns of B∗. Such a coefficient matrix implies an `1-norm distance metric in the data space (r = 1). The reason is that in the dual space (‖ · ‖∞), the vertex of the constraint set has each coordinate being the same in absolute value, and in our setting each coordinate is represented by the absolute sum over the K columns of B∗. 
The predictor x is generated from a multivariate normal distribution with mean zero and covariance Σx = (σx 
ij)i,j∈JpK, where σx ij = 0.9|i−j|. 
The response vector y is generated as 
y = (B∗)′x + η, 
where η is a standard normal random vector. Throughout the experiments we set p = 5, and K = 3.
6.4. Numerical Experiments 167 
We adopt a loss function hB(x,y) = ‖y−B′x‖r that is 1-Lipschitz continuous on ‖ · ‖r. Note that we use the same norm to define the loss function and the Wasserstein metric. We will compare the MLR-SR and MLR-1S relaxations induced by r = 1 and r = 2, respectively, in terms of their out-of-sample Weighted Mean Squared Error (WMSE), defined as: 
WMSE , 1 M 
∑M 
i=1 (yi − ŷi)′Σ̂ 
−1(yi − ŷi), 
where M is the size of the test set, yi and ŷi are the true and predicted response vectors for the i-th test sample, respectively, and Σ̂ is the covariance matrix of the prediction error on the training set, 
Σ̂ = (Y− Ŷ)′(Y− Ŷ)/(N − pK), 
where Y, Ŷ ∈ RN×K are the true and estimated response matrices of the training set, respectively, and N is the size of the training set. We will also look at the Conditional Value at Risk (CVaR) of the WMSE (at the confidence level α = 0.8) that quantifies its tail behavior. 
Figures 6.1 and 6.2 show the comparison of MLR-SR and MLR-1S formulations derived from the Wasserstein metric induced by the `r norm, with r = 1 and r = 2, when the radius of the Wasserstein ball ε is varied. As expected, when B∗ is a dense matrix, the `2 norm is a proper distance metric in the data space, and as a result, the two relaxations with r = 2 achieve a lower out-of-sample prediction bias. On the other hand, when the structure of B∗ implies an `1-norm distance metric on the data (Figure 6.2), the formulations with r = 1 have a better performance. 
We also compare the four MLR relaxations with an optimal ε chosen by cross-validation. Tables 6.1 and 6.2 show the mean WMSE and CVaR over 100 repetitions (the numbers inside the parentheses indicate the corresponding standard deviations). Similar conclusions can be drawn from the results in the tables. With a proper choice of r, the MLR relaxations are able to achieve a lower prediction error with a smaller variance. For example, in Table 6.1, compared to MLR-SR (r=1), the two relaxations with r = 2 improved the WMSE by 4.6%. 
We next compare the MLR-SR and MLR-1S formulations with several other popular methods for MLR, including OLS, Reduced Rank
168 Distributionally Robust Multi-Output Learning 
10 0 
Epsilon 
3 
3.05 
3.1 
3.15 
3.2 
3.25 
3.3 
3.35 
3.4 
W M 
S E 
MLR-SR (r=2) 
MLR-1S (r=2) 
MLR-SR (r=1) 
MLR-1S (r=1) 
(a) WMSE. 
10 0 
Epsilon 
7.4 
7.6 
7.8 
8 
8.2 
8.4 
8.6 
C V 
a R 
MLR-SR (r=2) 
MLR-1S (r=2) 
MLR-SR (r=1) 
MLR-1S (r=1) 
(b) CVaR of WMSE. 
Figure 6.1: The out-of-sample performance of MLR-SR and MLR-1S with normally distributed B∗. 
Table 6.1: The out-of-sample performance of MLR-SR and MLR-1S with crossvalidated ε when B∗ is normally distributed. 
WMSE CVaR MLR-SR (r=1) 3.26 (0.48) 4.91 (0.70) MLR-1S (r=1) 3.21 (0.40) 4.93 (0.65) MLR-SR (r=2) 3.11 (0.36) 4.74 (0.62) MLR-1S (r=2) 3.11 (0.35) 4.75 (0.64) 
Regression (RRR) (Izenman, 1975; Velu and Reinsel, 2013), Princi-pal Components Regression (PCR) (Massy, 1965), Factor Estimation and Selection (FES) (Yuan et al., 2007), the Curds and Whey (C&W) procedure (Breiman and Friedman, 1997), and Ridge Regression (RR) (Brown, Zidek, et al., 1980; Haitovsky, 1987). We provide a brief outline of these methods. RRR restricts the rank of B, and its solution is obtained by a Canonical Correlation Analysis (CCA) of the response and predictor matrices that finds a sequence of uncorrelated linear combinations of the predictors and a corresponding sequence of uncorrelated linear combinations of the responses such that their correlations are successively maximized. PCR converts the predictors into a set of linearly uncorrelated variables and applies OLS on the transformed
6.4. Numerical Experiments 169 
10 -2 
Epsilon 
3.34 
3.36 
3.38 
3.4 
3.42 
3.44 
3.46 
3.48 
3.5 
3.52 
W M 
S E 
MLR-SR (r=2) 
MLR-1S (r=2) 
MLR-SR (r=1) 
MLR-1S (r=1) 
(a) WMSE. 
10 -2 
Epsilon 
5 
5.05 
5.1 
5.15 
5.2 
5.25 
5.3 
5.35 
5.4 
C V 
a R 
MLR-SR (r=2) 
MLR-1S (r=2) 
MLR-SR (r=1) 
MLR-1S (r=1) 
(b) CVaR of WMSE. 
Figure 6.2: The out-of-sample performance of MLR-SR and MLR-1S when B∗ has an equal row absolute sum. 
Table 6.2: The out-of-sample performance of MLR-SR and MLR-1S with crossvalidated ε when B∗ has an equal row absolute sum. 
WMSE CVaR MLR-SR (r=1) 3.04 (0.52) 4.56 (0.83) MLR-1S (r=1) 3.05 (0.52) 4.60 (0.89) MLR-SR (r=2) 3.05 (0.52) 4.62 (0.88) MLR-1S (r=2) 3.05 (0.52) 4.62 (0.89) 
variables. Both RRR and PCR form linear combinations of predictors and responses (in the case of RRR) which hurts interpretability since it is not possible to explain an original response via the original predictors. FES penalizes the sum of the singular values of B. The C&W procedure shrinks the canonical variates between x and y. RR penalizes the sum of the squared elements in B (equivalent to multiple independent ridge regression of each coordinate of y). 
To test the robustness of various methods, we inject outliers to the training datasets whose distribution differs from the majority by a normally distributed random quantity. Specifically, the response of outliers is generated as 
y = (B∗)′x + η + oη,
170 Distributionally Robust Multi-Output Learning 
where η ∼ N (0, I), and oη ∼ N (0,Σy), where Σy = (σy ij)i,j∈JKK, with 
σy ij = (−0.9)|i−j|. Note that the perturbation occurs only on the response 
variables. We generate 20 datasets with a training size of 100 and a test size of 
60, and compare the WMSE and CVaR of various models on a clean test set. All the regularization coefficients are tuned through cross-validation. Table 6.3 shows the average performance on datasets with 20% and 30% outliers, respectively, when B∗ is generated from a standard normal distribution. We see that as the proportion of outliers increases, the WMSE and its CVaR increase, and in both scenarios, the MLR-SR and MLR-1S relaxations achieve the smallest out-of-sample prediction error with a small variance. They improve the WMSE by 1% – 5% and 3% – 7% when the proportion of outliers is 20% and 30%, respectively. PCR and FES achieve a slightly worse performance, but with a considerably higher variance in the scenario with 20% outlier. PCR works well with linearly correlated predictors, but could possibly fail when there exists a highly nonlinear relationship among the predictors. 
To further characterize the robustness of various approaches, we compute outlier detection rates on the test set, and draw the Receiver Operating Characteristic (ROC) curves obtained from varying the threshold values in the outlier detection rule. Note that in this case both the training and test datasets contain outliers. The response of outliers is generated as 
y = (B∗)′x + oη, 
where oη ∼ N (4 ∗ 1K ,Σy), with 1K the K-dimensional vector of all ones, and Σy = (σy 
ij)i,j∈JKK, with σy ij = (−0.9)|i−j|. The outlier detection 
criterion is described as follows: 
(xi,yi) = 
outlier, if r′iΣ̂ −1ri ≥ c, 
not an outlier, otherwise, 
where ri = yi − B̂′xi is the estimated residual, Σ̂ is the covariance matrix of the prediction error on the training set, and c is the threshold value that is varied between 0 and χ2 
0.99(K) (0.99 percentile of the chi-square distribution with K degrees of freedom) to produce the ROC curves. Table 6.3 shows the average Area Under the ROC Curve (AUC)
6.4. Numerical Experiments 171 
on the test set over 20 repetitions, and Figure 6.3 shows the ROC curves for different methods with 20% and 30% outliers, where the true positive rates and false positive rates are averaged over 20 repetitions. Compared to other methods except FES, the MLR-SR and MLR-1S models improve the AUC by 2% – 11% when we have 20% outliers, and 6% – 17% when we have 30% outliers, with a relatively small variability. Notice that FES also achieves a high AUC, but with a worse out-of-sample predictive performance. 
Table 6.3: The out-of-sample performance of different MLR models, mean (std.). 
Proportion of Outliers 20% WMSE CVaR AUC 
MLR-SR (r=2) 2.55 (0.26) 3.91 (0.51) 0.89 (0.04) MLR-1S (r=2) 2.59 (0.21) 3.93 (0.43) 0.89 (0.03) OLS 2.66 (0.44) 4.11 (0.83) 0.85 (0.06) RR 2.64 (0.42) 4.12 (0.82) 0.87 (0.03) RRR 2.68 (0.36) 4.03 (0.61) 0.80 (0.05) FES 2.58 (0.29) 4.01 (0.55) 0.89 (0.03) C&W 2.65 (0.42) 4.10 (0.80) 0.86 (0.06) PCR 2.61 (0.29) 4.01 (0.50) 0.86 (0.03) Proportion of Outliers 30% MLR-SR (r=2) 2.63 (0.33) 4.07 (0.66) 0.83 (0.09) MLR-1S (r=2) 2.57 (0.31) 4.02 (0.60) 0.83 (0.09) OLS 2.75 (0.33) 4.14 (0.71) 0.73 (0.11) RR 2.72 (0.32) 4.14 (0.60) 0.78 (0.10) RRR 2.76 (0.44) 4.22 (0.80) 0.71 (0.12) FES 2.66 (0.33) 4.02 (0.61) 0.83 (0.09) C&W 2.74 (0.33) 4.11 (0.65) 0.74 (0.11) PCR 2.68 (0.32) 4.02 (0.62) 0.73 (0.11)
172 Distributionally Robust Multi-Output Learning 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 T 
ru e  p 
o s it iv 
e  r 
a te 
MLR-SR (r=2) 
MLR-1S (r=2) 
OLS 
RRR 
FES 
C&W 
PCR 
RR 
(a) 20% outliers. 
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 
False positive rate 
0 
0.2 
0.4 
0.6 
0.8 
1 
T ru 
e  p 
o s it iv 
e  r 
a te 
MLR-SR (r=2) 
MLR-1S (r=2) 
OLS 
RRR 
FES 
C&W 
PCR 
RR 
(b) 30% outliers. 
Figure 6.3: The ROC curves of different MLR models. 
6.4.2 MLG Relaxations 
In this subsection we study the performance of the two DRO-MLG relaxations, and compare them with a number of MLG variants on simulated datasets, in terms of their out-of-sample log-loss and classification accuracy. 
We first study the problem of selecting the right regularizer based on the distance metric in the data space. Similar to Section 6.4.1, we experiment with two types of B∗, one coming from a multivariate normal distribution, and the other normalized to have an equal row absolute sum. They respectively correspond to an `2 and `1-norm distance metric in the data space. The predictor is drawn according to x ∼ N (0,Σx),
6.4. Numerical Experiments 173 
where Σx = (σx ij)i,j∈JpK, and σx 
ij = 0.9|i−j|. The label vector y ∈ {0, 1}K is generated from a multinomial distribution with probabilities specified by the softmax normalization of (B∗)′x + η, where η ∼ N (0, IK). 
We set p = 5,K = 3, and conduct 20 simulation runs, each with a training size of 100 and a test size of 60. The performance metrics we use include: (i) the average log-loss, (ii) the Correct Classification Rate (CCR), and (iii) the Conditional Value at Risk (CVaR) (at the confidence level 0.8) of log-loss, which computes the expectation of extreme log-loss values. The average performance metrics on the test set over 20 replications are reported. 
Figures 6.4 and 6.5 show the comparison of the four models as the Wasserstein radius ε is varied. We see that when B∗ is a dense matrix, the MLG-SR and MLG-1S induced by the `2-norm have a higher classification accuracy and a lower log-loss. By contrast, when the structure of B∗ implies an `1-norm distance metric in the data space, the MLG-SR and MLG-1S with r = 1 perform better. We also validate this conclusion in Tables 6.4 and 6.5 where the optimal Wasserstein set radius ε is chosen through cross-validation. With normally distributed B∗, the formulations with r = 2 improve the CCR and log-loss by 5% compared to the ones induced by r = 1. 
Table 6.4: The out-of-sample performance of MLG-SR and MLG-1S with crossvalidated ε when B∗ is normally distributed. 
CCR Log-loss CVaR MLG-SR (r=1) 0.73 (0.06) 0.59 (0.09) 1.17 (0.24) MLG-1S (r=1) 0.75 (0.03) 0.60 (0.10) 1.16 (0.19) MLG-SR (r=2) 0.76 (0.05) 0.57 (0.08) 1.16 (0.21) MLG-1S (r=2) 0.76 (0.04) 0.57 (0.09) 1.11 (0.13) 
Next we will compare with a number of MLG models, including: (i) Vanilla MLG which minimizes the empirical log-loss with no penalty term, and (ii) Ridge MLG which penalizes the trace of B′B (the squared Frobenius norm of B) as in ridge regression (Brown, Zidek, et al., 1980; Haitovsky, 1987). In addition to the three performance metrics used
174 Distributionally Robust Multi-Output Learning 
Table 6.5: The out-of-sample performance of MLG-SR and MLG-1S with crossvalidated ε when B∗ has an equal row absolute sum. 
CCR Log-loss CVaR MLG-SR (r=1) 0.84 (0.04) 0.35 (0.05) 0.54 (0.18) MLG-1S (r=1) 0.84 (0.04) 0.34 (0.07) 0.55 (0.26) MLG-SR (r=2) 0.82 (0.05) 0.35 (0.12) 0.58 (0.32) MLG-1S (r=2) 0.83 (0.05) 0.35 (0.06) 0.58 (0.25) 
earlier, we introduce another robustness measure that calculates the minimal perturbation needed to fool the classifier. For a given x with label k, for any j 6= k, consider the following optimization problem: 
min x̃ 
‖x− x̃‖1 
s.t. Pj(x̃) ≥ Pk(x̃), k = arg max 
i Pi(x), 
(6.15) 
where Pi(x) denotes the probability of assigning class label i to x, which is a function of the trained classifier. Problem (6.15) measures the minimal perturbation distance (in terms of the `1-norm) that is needed to change the label of x. Its optimal value evaluates the robustness of a given classifier in terms of the perturbation magnitude. The more robust the classifier, the larger the required perturbation to switch the label, and thus the larger the optimal value. We solve Problem (6.15) for every test point x and any j 6= k, and take the minimum of the optimal values to be the Minimal Perturbation Distance (MPD) of the classifier. 
We experiment with two types of B∗: 
1. type-1: each column of B∗, with probability 0.4, is generated from a multivariate normal distribution, and with probability 0.6, it is generated as a sparse vector where only one randomly picked element is set to nonzero; 
2. type-2: we first generate a B∗ that is normalized to have an equal
6.4. Numerical Experiments 175 
row absolute sum as before, and then set each column to a sparse vector with probability 0.6. 
To test the robustness of various methods, we inject outliers to the training datasets. The predictors of the outliers have the same distribution as the clean samples, but their label vector is generated from a multinomial distribution with probabilities specified by the softmax normalization of 1/(x′B∗ + η), where η ∼ N (0, IK). The test set does not contain any outlier. 
Tables 6.6 and 6.7 show the average performance of various models over 20 repetitions under different experimental settings. For type-1 B∗, the MLG-1S (r=2) achieves the highest classification accuracy and the largest MPD, while for type-2 B∗, the MLG-1S (r=1) excels. Notice that in both cases, the DRO-MLG models lose to vanilla MLG in terms of the log-loss. The reason is that vanilla MLG focuses solely on minimizing the sample average log-loss, while the MLG-SR and MLG-1S models balance between maintaining a low log-loss and achieving a high robustness level. By allowing for a slightly larger log-loss, the DRO-MLG models achieve a considerably higher MPD and a higher classification accuracy. They improve the CCR by 1% – 5% and 5% – 6%, the MPD by 67% – 400% and 50% – 650% in Tables 6.6 and 6.7, respectively. Compared to ridge MLG, they improve the log-loss by 6% and 5% in the two tables. 
Table 6.6: The out-of-sample performance of different MLG models trained on datasets with 30% outliers and type-1 B∗. 
CCR Log-loss CVaR MPD MLG-SR (r=1) 0.81 (0.05) 0.65 (0.09) 0.97 (0.10) 0.04 (0.15) MLG-1S (r=1) 0.81 (0.05) 0.65 (0.08) 0.99 (0.10) 0.04 (0.13) MLG-SR (r=2) 0.81 (0.05) 0.64 (0.04) 0.94 (0.11) 0.07 (0.02) MLG-1S (r=2) 0.82 (0.05) 0.66 (0.07) 0.95 (0.14) 0.10 (0.03) Vanilla MLG 0.78 (0.07) 0.61 (0.08) 0.94 (0.17) 0.02 (0.01) Ridge MLG 0.81 (0.04) 0.68 (0.08) 0.95 (0.13) 0.06 (0.05)
176 Distributionally Robust Multi-Output Learning 
Table 6.7: The out-of-sample performance of different MLG models trained on datasets with 40% outliers and type-2 B∗. 
CCR Log-loss CVaR MPD MLG-SR (r=1) 0.69 (0.14) 0.80 (0.06) 1.10 (0.17) 0.01 (0.007) MLG-1S (r=1) 0.69 (0.14) 0.82 (0.06) 1.11 (0.17) 0.03 (0.02) MLG-SR (r=2) 0.66 (0.13) 0.84 (0.05) 1.08 (0.12) 0.02 (0.01) MLG-1S (r=2) 0.68 (0.13) 0.82 (0.05) 1.10 (0.13) 0.02 (0.02) Vanilla MLG 0.66 (0.06) 0.79 (0.06) 1.13 (0.14) 0.004 (0.002) Ridge MLG 0.65 (0.09) 0.84 (0.04) 1.10 (0.09) 0.02 (0.01) 
6.5 Summary 
In this section, we developed a Distributionally Robust Optimization (DRO) based approach under the Wasserstein metric to robustify Multi-output Linear Regression (MLR) and Multiclass Logistic Regression (MLG), leading to matrix-norm regularized formulations that establish a connection between robustness and regularization in the multi-output scenario. We established out-of-sample performance guarantees for the solutions to the DRO-MLR and DRO-MLG extracts, illustrating the role of the regularizer in controlling the out-of-sample prediction error. We provided empirical evidence showing that the DRO-MLR and DRO-MLG models achieve a comparable (slightly better) out-of-sample predictive performance to others, but a significantly higher robustness to outliers.
6.5. Summary 177 
4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 
Epsilon 10 -3 
0.52 
0.54 
0.56 
0.58 
0.6 
0.62 
0.64 
C C 
R 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(a) CCR. 
4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 
Epsilon 10 -3 
0.82 
0.84 
0.86 
0.88 
0.9 
0.92 
0.94 
L o 
g lo 
s s 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(b) Log-loss. 
4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 
Epsilon 10 -3 
1.16 
1.18 
1.2 
1.22 
1.24 
1.26 
1.28 
1.3 
1.32 
C V 
a R 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(c) CVaR of log-loss. 
Figure 6.4: The out-of-sample performance of MLG-SR and MLG-1S when B∗ is normally distributed.
178 Distributionally Robust Multi-Output Learning 
0.008 0.01 0.012 0.014 0.016 0.018 0.02 
Epsilon 
0.84 
0.85 
0.86 
0.87 
0.88 
0.89 
0.9 
C C 
R 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(a) CCR. 
0.008 0.01 0.012 0.014 0.016 0.018 0.02 
Epsilon 
0.26 
0.28 
0.3 
0.32 
0.34 
0.36 
0.38 
0.4 
0.42 
L o 
g lo 
s s 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(b) Log-loss. 
0.008 0.01 0.012 0.014 0.016 0.018 0.02 
Epsilon 
0.4 
0.45 
0.5 
0.55 
0.6 
0.65 
0.7 
0.75 
C V 
a R 
MLG-SR (r=2) 
MLG-1S (r=2) 
MLG-SR (r=1) 
MLG-1S (r=1) 
(c) CVaR of log-loss. 
Figure 6.5: The out-of-sample performance of MLG-SR and MLG-1S when B∗ has an equal row absolute sum.
7 
Optimal Decision Making via Regression 
Informed K-NN 
In this section, we will develop a prediction-based prescriptive model for optimal decision making that (i) predicts the outcome under each possible action using a robust nonlinear model, and (ii) adopts a randomized prescriptive policy determined by the predicted outcomes. The predictive model combines the Wasserstein DRO regression with the K-Nearest Neighbors (K-NN) regression that helps to capture the nonlinearity embedded in the data. We apply the proposed methodology in making recommendations for medical prescriptions, using a diabetes and a hypertension dataset extracted from the Electronic Health Records (EHRs) of a major safety-net hospital in New England. 
7.1 The Problem and Related Work 
Suppose we are given a set of M actions, and our goal is to choose m ∈ JMK such that the future outcome y is optimized. We are interested in finding the optimal decision with the aid of auxiliary data x ∈ Rp that is concurrently observed, and correlated with the uncertain outcome y. A main challenge with learning from observational data lies in the lack of counterfactual information. One solution is to predict the effects of counterfactual policies by learning an action-dependent predictive 
179
180 Optimal Decision Making via Regression Informed K-NN 
model that groups the training samples based on their actions, and fits a model in each group between the outcome y and the feature x. The predictions from this composite model can be used to determine the optimal action to take. The performance of the prescribed decision hinges on the quality of the predictive model. We have observed that (i) there is often significant “noise” in the data caused by recording errors, missing values, and large variability across individuals, and (ii) the underlying relationship we try to learn is usually nonlinear and its parametric form is not known a priori. To deal with these issues, a nonparametric robust learning procedure is in need. 
Motivated by the observation that individuals with similar features x would have similar outcomes y if they were to take the same action, we propose a predictive model that makes predictions based on the outcomes of similar individuals – to be called neighbors – in each group of the training set. It is a nonlinear and nonparametric estimator which constructs locally linear (constant) curves based on the similarity between individuals. To find reasonable neighbors, we need to accurately identify the set of features that are correlated with the outcome. We use the Wasserstein DRO regression for this task in consideration of the noise that could potentially bias the estimation. Our prescriptive methodology is established on the basis of a regression informed K-Nearest Neighbors (K-NN) model (Altman, 1992) that evaluates the importance of features through Wasserstein DRO regression, and estimates the outcome by averaging over the neighbors identified by a regression coefficientsweighted distance metric. 
Our framework uses both parametric (Wasserstein DRO regression) and nonparametric (K-NN) predictive models, producing robust predictions immunized against significant noise and capturing the underlying nonlinearity by utilizing the information of neighbors. It is more information-efficient and more interpretable than the vanilla K-NN. We then develop a randomized prescriptive policy that chooses each action m with probability e−ξŷm(x)/ 
∑M j=1 e 
−ξŷj(x), for some pre-specified positive constant ξ, where ŷm(x) is the predicted future outcome for x under action m ∈ JMK. We show that this randomized strategy leads to a nearly optimal future outcome by an appropriate choice of ξ. 
In recent years there has been an emerging interest in combining
7.1. The Problem and Related Work 181 
ideas from machine learning with operations research to develop a framework that uses data to prescribe optimal decisions (Bertsimas and Kallus, 2019; Den Hertog and Postek, 2016; Bravo and Shaposhnik, 2018). Current research focus has been on applying machine learning methodologies to predict the counterfactuals, based on which optimal decisions can be made. Local learning methods such as K-Nearest Neighbors (Altman, 1992), LOESS (LOcally Estimated Scatterplot Smoothing) (Cleveland and Devlin, 1988), CART (Classification And Regression Trees) (Breiman, 2017), and Random Forests (Breiman, 2001), have been studied inBertsimas and Kallus, 2019; Bertsimas et al., 2017; Bertsimas et al., 2019a; Dunn, 2018; Biggs and Hariss, 2018. Extensions to continuous and multi-dimensional decision spaces with observational data were considered in Bertsimas and McCord, 2018. To prevent overfitting, Bertsimas and Van Parys, 2017 proposed two robust prescriptive methods based on Nadaraya-Watson and nearest-neighbors learning. Deviating from such a predict-optimize paradigm, Bastani and Bayati, 2020 presented a new bandit algorithm based on the LASSO to learn a model of decision rewards conditional on individual-specific covariates. 
Our problem is closely related to contextual bandits (Chu et al., 2011; Agarwal et al., 2014; Slivkins, 2014; Wu et al., 2015), where an agent learns a sequence of decisions conditional on the contexts with the aim of maximizing its cumulative reward. It has recently found applications in learning personalized treatment of long-term diseases from mobile health data (Tewari and Murphy, 2017; Xia, 2018; Zhu et al., 2018). However, we learn the interaction between the context and rewards in each action group across similar individuals, not over the history of the same individual as in contextual bandits. A contextual bandits framework is most suitable for learning sequential strategies through repeated interactions with the environment, which requires a substantial amount of historical data for exploring the reward function and exploiting the promising actions. In contrast, our method does not require the availability of historical data, but instead learns the payoff function from similar individuals. This can be viewed as a different type of exploration, i.e., when little information can be acquired for the past states of an individual, investigating the behavior of similar subjects may
182 Optimal Decision Making via Regression Informed K-NN 
be beneficial. This is essential for learning from the Electronic Health Records (EHRs), where rapid and continuous collection of patient data is not possible. We may observe a very short treatment history for some patients, and the lag between patient visits is usually large. 
Our method is similar to K-NN regression with an OLS-weighted metric used in Bertsimas et al., 2017 to learn the optimal treatment for type-2 diabetic patients. The key differences lie in that: (i) we adopt a robustified regression procedure that is immunized against outliers and is thus more stable and reliable; (ii) we propose a randomized prescriptive policy that adds robustness to the methodology whereas Bertsimas et al., 2017 deterministically prescribed the treatment with the best predicted outcome; (iii) we establish theoretical guarantees on the quality of the predictions and the prescribed actions, and (iv) the prescriptive rule in Bertsimas et al., 2017 was activated when the improvement of the recommended treatment over the standard of care exceeded a certain threshold, whereas our method looks into the improvement over the previous regimen. This distinction makes our algorithm applicable in the scenario where the standard of care is unknown or ambiguous. Further, we derive a closed-form expression for the threshold level, which greatly improves the computational efficiency compared to Bertsimas et al., 2017, where a threshold was selected by cross-validation. 
The remainder of this section is organized as follows. In Section 7.2, we introduce the robust nonlinear predictive model and present the performance guarantees on its predictive power. Section 7.3 develops the randomized prescriptive policy and proves its optimality in terms of the expected true outcome. The numerical experimental results are presented in Section 7.4. We conclude in Section 7.5. 
7.2 Robust Nonlinear Predictive Model 
Given a feature vector x ∈ Rp, and a set of M available actions, our goal is to predict the future outcome ym(x) under each possible action m ∈ JMK. Assume the following relationship between the feature and outcome: 
ym = x′mβ∗m + hm(xm) + εm,
7.2. Robust Nonlinear Predictive Model 183 
where (xm, ym) represents the feature-outcome pair of an individual taking action m; β∗m is the coefficient that captures the linear trend; hm(·) is a nonlinear function (whose form is unknown) describing the nonlinear fluctuation in ym, and εm is the noise term with zero mean and standard deviation ηm that expresses the intrinsic randomness of ym and is assumed to be independent of xm. 
Suppose for eachm ∈ JMK, we observe Nm independently and identically distributed (i.i.d.) training samples (xmi, ymi), i ∈ JNmK, that take action m. To estimate β∗m, we adopt the `2-norm induced Wasserstein DRO formulation. A robust model could lead to an improved out-of-sample performance, and accommodate the potential nonlinearity that is not explicitly revealed by the linear coefficient β∗m, thus, resulting in a more accurate assessment of the features. Solving the Wasserstein DRO regression model gives us a robust estimator of the linear regression coefficient β∗m, which we denote by β̂m , (β̂m1, . . . , β̂mp). The elements of β̂m measure the relative significance of the predictors in determining the outcome ym. We feed the estimator into the nonlinear non-parametric K-NN regression model, by considering the following β̂m-weighted metric: 
‖x− xmi‖Ŵm = √ 
(x− xmi)′Ŵm(x− xmi), (7.1) 
where Ŵm = diag(β̂2 m), and β̂2 
m = (β̂2 m1, . . . , β̂ 
2 mp). For a new test 
sample x, within each action group m, we find its Km nearest neighbors using the weighted distance function (7.1). The predicted future outcome for x under action m, denoted by ŷm(x), is computed by 
ŷm(x) = 1 Km 
∑Km 
i=1 ym(i), (7.2) 
where ym(i) is the outcome of the i-th closest individual to x in the training set who takes actionm. In essence, we compute a K-NN estimate of the future outcome by using the regression weighted distance function, which can be viewed as a locally smoothed estimator in the neighborhood of x. Notice that due to (7.1), the nearest neighbors are similar to x in the features that are most predictive of the outcome. Therefore, their corresponding response values should serve as a good approximation for the future outcome of x.
184 Optimal Decision Making via Regression Informed K-NN 
We next show that (7.2) provides a good prediction in the sense of Mean Squared Error (MSE). The bias-variance decomposition implies the following: 
MSE ( ŷm(x) 
∣∣x,xmi, i ∈ JNmK ) 
, E [( ŷm(x)− ym(x) 
)2∣∣∣x,xmi, i ∈ JNmK ] 
= E [( 1 Km 
∑Km 
j=1 
( x′m(j)β 
∗ m + hm(xm(j)) + εm(j) 
) − ( x′β∗m + hm(x) + εm 
))2∣∣∣x,xmi, i ∈ JNmK ] 
= ( x′β∗m + hm(x)− 1 
Km 
Km∑ i=1 
( x′m(i)β 
∗ m + hm(xm(i)) 
))2 + η2 
m 
Km + η2 
m 
= ( 1 Km 
Km∑ i=1 
( (x− xm(i))′β∗m + hm(x)− hm(xm(i)) 
))2 + η2 
m 
Km + η2 
m, 
(7.3) where ym(x) is the true future outcome for x under action m, and xm(i), εm(i) are the feature vector and noise term corresponding to the i-th closest sample to x within group m, respectively. For each m ∈ JMK, we aim at providing a probabilistic bound for (7.3) w.r.t. the measure of the Nm training samples. According to (7.3), for the MSE to be small the following three conditions suffice: 
1. ‖β∗m − β̂m‖2 is small; 
2. ‖x− xm(i)‖Ŵm is small for i ∈ JKmK; 
3. hm(x)− hm(xm(i)) is small for i ∈ JKmK. 
In other words, to ensure an accurate prediction of the outcome, we require an accurate estimate of the linear trend and a smooth nonlinear fluctuation, with the selected neighbors close enough to x. An upper bound for the MSE follows from bounding these three quantities. We note that Theorem 4.3.12 provides an upper bound on the estimation bias ‖β∗m−β̂m‖2 in a linear model. If we view the nonlinear term hm(xm) as part of the noise, then the bound provided by Theorem 4.3.12 applies to our case. The increased variance of the noise (due to hm(xm)) is
7.2. Robust Nonlinear Predictive Model 185 
reflected in the eigenvalues of the covariance matrix, which play a role in the estimation error bound. We provide a simplified version of Theorem 4.3.12 in the following theorem. 
Theorem 7.2.1. Under Assumptions I, J, K, L, M, N, when the sample size Nm ≥ nm, with probability at least δm, 
‖β∗m − β̂m‖2 ≤ τm. 
We next show that the distance between x and its Km nearest neighbors xm(i) could be upper bounded probabilistically. All predictors are assumed to be centered, and independent from each other. In Theorem 7.2.2 we present a lower bound for P(‖x− xm(i)‖W ≤ w̄m, i ∈ JKmK), for any positive definite diagonal matrix W. 
Theorem 7.2.2. Suppose we are given Nm i.i.d. samples (xmi, ymi), i ∈ JNmK, drawn from some unknown probability distribution with finite fourth moment. Every xmi has independent, centered coordinates: 
E(xmi) = 0, cov(xmi) = diag ( σ2 m1, . . . , σ 
2 mp 
) , ∀i ∈ JNmK. 
For a fixed predictor x, and for any given positive definite diagonal matrix W ∈ Rp×p with diagonal elements wj , j ∈ JpK, and |wj | ≤ B̄2, suppose: 
|(xmij − xj)2 − (σ2 mj + x2 
j )| ≤ Tm, a.s., ∀i ∈ JNmK, j ∈ JpK, 
where xmij , xj are the j-th components of xmi and x, respectively. Under the condition that w̄2 
m > B̄2∑p j=1(σ2 
mj + x2 j ), with probability at least 
1− I1−pm0(Nm −Km + 1,Km), 
‖x− xm(i)‖W ≤ w̄m, i ∈ JKmK, 
where g(u) = (1 + u) log(1 + u)− u, 
I1−pm0(Nm −Km + 1,Km) , 
(Nm −Km + 1) ( 
Nm 
Km − 1 
) 1−pm0∫ 0 
tNm−Km(1− t)Km−1dt,
186 Optimal Decision Making via Regression Informed K-NN 
pm0 = 1− exp ( −σ 
2 m 
T 2 m 
g (Tm(w̄2 
m/B̄ 2 − 
∑ j(σ2 
mj + x2 j ) ) 
σ2 m 
)) , 
and, 
σ2 m = 
∑p 
j=1 var ( (xmij − xj)2 
) . 
Proof. To simplify the notation, we will omit the subscript m in all proofs, e.g., using xi and x(i) for xmi and xm(i), respectively, and N for Nm. Define the event Ai := {‖xi − x‖B̄2I ≤ w̄}. As long as we can calculate the probability that at least K of Ai, i ∈ JNK, occur, we are able to provide a lower bound on P(‖x− x(i)‖W ≤ w̄, i ∈ JKK). Note that given x, Ai, i ∈ JNK, are independent and equiprobable, since xi, i ∈ JNK, are i.i.d. Based on Bennett’s inequality (Vershynin, 2017), we have: 
P(Ai) = P(‖xi − x‖2 B̄2I ≤ w̄ 
2) 
= P ( B̄2(xi1 − x1)2 + . . .+ B̄2(xip − xp)2 ≤ w̄2 
) = P(t1 + . . .+ tp ≤ w̄2/B̄2) 
= P (∑ 
j 
( tj − (σ2 
j + x2 j ) ) ≤ w̄2/B̄2 − 
∑ j (σ2 j + x2 
j ) ) 
≥ 1− exp ( −σ 
2 
T 2 g (T(w̄2/B̄2 − 
∑ j(σ2 
j + x2 j ) ) 
σ2 
)) , p0, 
where tj = (xij−xj)2, j ∈ JpK; σ2 = ∑ j var(tj). In the above derivation, 
we used the fact that tj , j ∈ JpK, are independent, and |tj − E[tj ]| ≤ T, a.s., ∀j. 
Given the lower bound for P(Ai), we can derive a lower bound for the probability that exactly K of Ai, i ∈ JNK, occur. For a given x, Ai,
7.2. Robust Nonlinear Predictive Model 187 
i ∈ JNK, are independent, and thus, 
P(‖x− x(i)‖W ≤ w̄, i ∈ JKK) ≥ P(at least K of Ai, i ∈ JNK occur) 
= ∑N 
k=K 
( N 
k 
)( P(Ai) 
)k( 1− P(Ai) 
)N−k ≥ ∑N 
k=K 
( N 
k 
) pk0(1− p0)N−k 
= 1− I1−p0(N −K + 1,K), 
where I1−p0(N −K + 1,K) is the regularized incomplete beta function defined as: 
I1−p0(N −K + 1,K) , (N −K + 1) ( 
N 
K − 1 
) 1−p0∫ 0 
tN−K(1− t)K−1dt. 
Note that pm0 is nonnegative, due to the assumption that w̄2 m > 
B̄2∑ j(σ2 
mj + x2 j ), and the non-decreasing property of the function g(·) 
when its argument is non-negative. We also note that a lower bound on P(‖x− xm(i)‖2 ≤ w̄m, i ∈ JKmK) can be obtained by setting B̄ = 1. 
By now we have shown results on the accuracy of β̂m and the similarity between x and its neighbors. Notice that for a Lipschitz continuous function hm(·) with a Lipschitz constant Lm, the difference between hm(x) and hm(xm(i)) can be bounded by Lm‖x−xm(i)‖2. With these results we are ready to bound the MSE of ŷm(x). 
Theorem 7.2.3. Suppose we are given Nm i.i.d. copies of (xm, ym), denoted by (xmi, ymi), i ∈ JNmK, where xm has independent, centered coordinates, and cov(xm) = diag(σ2 
m1, . . . , σ 2 mp). We are given a fixed 
predictor x = (x1, . . . , xp), a scalar w̄m, and we assume: 
1. hm(·) is Lipschitz continuous with a Lipschitz constant Lm on the metric spaces (Xm, ‖ · ‖2) and (Ym, | · |), where Xm,Ym are the domain and codomain of hm(·), respectively.
188 Optimal Decision Making via Regression Informed K-NN 
2. w̄2 m > B̄2 
m 
∑p j=1(σ2 
mj + x2 j ), where B̄m is the upper bound on 
‖(−βm, 1)‖2 for any feasible βm to (4.5). 
3. |(xmij −xj)2− (σ2 mj +x2 
j )| is upper bounded a.s. under the probability measure P∗Xm for any i, j, where xmij is the j-th component of xmi, and P∗Xm is the underlying true probability distribution of xm. 
4. The coordinates of any feasible solution to (4.5) have absolute values greater than or equal to some positive number bm (dense estimators). 
Under Assumptions I, J, K, L, M, N, when Nm ≥ nm, with probability at least δm − I1−pm0(Nm −Km + 1,Km) w.r.t. the measure of samples, 
E [ (ŷm(x)− ym(x))2 
∣∣∣x,xmi, i ∈ JNmK ] ≤( 
w̄mτm bm 
+√pw̄m + Lmw̄m 
B̄m 
)2 + η2 
m 
Km + η2 
m, (7.4) 
and for any a ≥ (w̄mτm/bm +√pw̄m + Lmw̄m/B̄m)2 + η2 m/Km + η2 
m, 
P (( ŷm(x)− ym(x) 
)2 ≥ a∣∣∣x,xmi, i ∈ JNmK ) ≤( 
w̄mτm bm 
+√pw̄m + Lmw̄m B̄m 
)2 + η2 
m Km 
+ η2 m 
a , (7.5) 
where all parameters are set in the same way as in Theorems 7.2.1 and 7.2.2. 
Proof. We omit the subscript m for simplicity. By Theorems 7.2.1 and 7.2.2, we know that, 
|(x− x(i))′(β∗ − β̂)| = |(x− x(i))′Ŵ 1 2 Ŵ− 1 
2 (β∗ − β̂)| 
≤ ‖(x− x(i))′Ŵ 1 2 ‖2‖Ŵ− 1 
2 (β∗ − β̂)‖2 
≤ w̄τ 
b , 
where the second inequality used the fact that ‖Ŵ− 1 2 (β∗ − β̂)‖2 ≤ τ/b 
if ‖β∗−β̂‖2 ≤ τ , which can be verified by the Courant-Fischer Theorem,
7.2. Robust Nonlinear Predictive Model 189 
and the fact that Ŵ is diagonal with elements β̂2 j , j ∈ JpK, and |β̂j | ≥ b. 
Based on the inequality (∑n 
i=1 ai )2 ≤ n 
(∑n i=1 a 
2 i 
) , we know: 
|(x− x(i))′β̂| = ∣∣∣∑p 
j=1 β̂j(x− x(i))j 
∣∣∣ ≤ √ p ∑p 
j=1 
( β̂j(x− x(i))j 
)2 
= √ p(x− x(i))′Ŵ(x− x(i)) 
≤ √pw̄. 
Therefore, 
|(x− x(i))′β∗| = |(x− x(i))′(β∗ − β̂) + (x− x(i))′β̂| ≤ |(x− x(i))′(β∗ − β̂)|+ |(x− x(i))′β̂| 
≤ w̄τ 
b +√pw̄. 
Thus, for a given x, 
E [ (ŷ(x)− y(x))2 
∣∣∣x,xi] = ( 1 K 
∑K 
i=1 
( (x− x(i))′β∗ + h(x)− h(x(i)) 
))2 + η2 
K + η2 
≤ ( 1 K 
∑K 
i=1 
( |(x− x(i))′β∗|+ |h(x)− h(x(i))| 
))2 + η2 
K + η2 
≤ ( w̄τ 
b +√pw̄ + Lw̄ 
B̄ 
)2 + η2 
K + η2 
The probability bound can be easily derived using Markov’s inequality. 
The expectation in (7.4) and the probability in (7.5) are taken w.r.t. the measure of the noise εm. Theorem 7.2.3 essentially says that for any given predictor x, with a high probability (w.r.t. the measure of samples), the prediction from our model is close to the true future outcome. The prediction bias depends on the sample size, the variation in the predictors and response, and the smoothness of the nonlinear fluctuation.
190 Optimal Decision Making via Regression Informed K-NN 
The dependence on bm in the upper bound provided by (7.4) is due to the fact that Ŵm has diagonal elements β̂2 
mj , j ∈ JpK, which are assumed to be at least b2m. If we multiply Ŵm by a very large number, the neighbor selection criterion is not affected, since the relative significance of the predictors stays unchanged, but the bm appearing in (7.4) would be replaced by a very large number, diminishing the effect of the first term in the parentheses, at the price of increasing B̄m and w̄m, which in turn have an effect on the number of neighbors needed. It might be interesting to explore this implicit trade-off and optimize Ŵm to achieve the smallest MSE. 
7.3 Prescriptive Policy Development 
We now proceed to develop the prescriptive policy with the aim of minimizing the future outcome. A natural idea is to take the action that yields the minimum predicted outcome. To allow for flexibility in exploring alternatives that have a comparable performance, and also to correct for potential prediction errors that might mislead the ranking of actions, we propose a randomized policy that prescribes each action with a probability inversely proportional to its exponentiated predicted outcome. It can be viewed as an offline Hedge algorithm (Hazan, 2016) that increases the robustness of our method through exploration. 
Specifically, given an individual with a feature vector x, and her predicted future outcome under each action m, denoted by ŷm(x), we consider a randomized policy that chooses action m with probability e−ξŷm(x)/ 
∑M j=1 e 
−ξŷj(x), with ξ some pre-specified positive constant. The randomness in making decisions might hurt the interpretability of the model. But on the other hand, it presents a range of comparable options that can be assessed subjectively by the decision maker based on her expertise. As ξ goes to infinity, the randomized policy will converge to a deterministic one which selects the action with the lowest predicted outcome. We next establish a related property of the randomized policy in terms of its expected true outcome. 
Theorem 7.3.1. Given any fixed predictor x ∈ Rp, denote its predicted and true future outcome under action m by ŷm(x) and ym(x), respec-
7.3. Prescriptive Policy Development 191 
tively. Assume that we adopt a randomized strategy that prescribes action m with probability e−ξŷm(x)/ 
∑M j=1 e 
−ξŷj(x), for some ξ ≥ 0. As-sume ŷm(x) and ym(x) are non-negative, ∀m ∈ JMK. The expected true outcome under this policy satisfies: 
∑M 
m=1 e−ξŷm(x)∑ j e −ξŷj(x) ym(x) ≤ yk(x) + 
( ŷk(x)− 1 
M 
∑M 
m=1 ŷm(x) 
) 
+ ξ 
( 1 M 
∑M 
m=1 ŷ2 m(x) + 
∑M 
m=1 e−ξŷm(x)∑ j e −ξŷj(x) y 
2 m(x) 
) + logM 
ξ , (7.6) 
for any k ∈ JMK. 
Proof. The proof borrows ideas from Theorem 1.5 in Hazan, 2016. Define Wm , e−ξŷm(x)/ 
∑M j=1 e 
−ξŷj(x), and φ , ∑M m=1 e 
−ξŷm(x)e−ξym(x). Then, 
φ = (∑M 
j=1 e−ξŷj(x) 
)∑M 
m=1 Wme 
−ξym(x) 
≤ (∑M 
j=1 e−ξŷj(x) 
)∑M 
m=1 Wm 
( 1− ξym(x) + ξ2y2 
m(x) ) 
= (∑M 
j=1 e−ξŷj(x) 
)( 1− ξ 
∑M 
m=1 Wmym(x) + ξ2∑M 
m=1 Wmy 
2 m(x) 
) ≤ (∑M 
j=1 e−ξŷj(x) 
) e−ξ 
∑M 
m=1 Wmym(x)+ξ2 ∑M 
m=1 Wmy2 m(x), 
where the first inequality uses the fact that for x ≥ 0, e−x ≤ 1− x+ x2, and the last inequality is due to the fact that 1 + x ≤ ex. Next let us examine the sum of exponentials: 
∑M 
j=1 e−ξŷj(x) ≤ 
∑M 
j=1 
( 1− ξŷj(x) + ξ2ŷ2 
j (x) ) 
= M ( 1− ξ 1 
M 
∑M 
j=1 ŷj(x) + ξ2 1 
M 
∑M 
j=1 ŷ2 j (x) 
) ≤Me 
−ξ 1 M 
∑M 
j=1 ŷj(x)+ξ2 1 M 
∑M 
j=1 ŷ 2 j (x) 
.
192 Optimal Decision Making via Regression Informed K-NN 
On the other hand, for any k ∈ JMK, 
e−ξŷk(x)−ξyk(x) ≤φ 
≤M exp { − ξ ∑M j=1 ŷj(x) M 
+ ξ2∑M 
j=1 ŷ 2 j (x) 
M 
− ξ M∑ m=1 
Wmym(x) + ξ2 M∑ m=1 
Wmy 2 m(x) 
} . 
(7.7) 
Taking the logarithm on both sides of (7.7) and dividing by ξ, we obtain 
1 M 
∑M 
m=1 ŷm(x) + 
∑M 
m=1 e−ξŷm(x)∑ j e −ξŷj(x) ym(x) ≤ ŷk(x) + yk(x) 
+ ξ 
( 1 M 
∑M 
m=1 ŷ2 m(x) + 
∑M 
m=1 e−ξŷm(x)∑ j e −ξŷj(x) y 
2 m(x) 
) + logM 
ξ . 
Theorem 7.3.1 says that the expected true outcome of the randomized policy is no worse than the true outcome of any action k plus two components, one accounting for the gap between the predicted outcome under k and the average predicted outcome, and the other depending on the parameter ξ. Thinking about choosing k = arg minm ym(x), if ŷk(x) is below the average predicted outcome (which should be true if we have an accurate prediction), it follows from (7.6) that the randomized policy leads to a nearly optimal future outcome by an appropriate choice of ξ. 
In the medical applications, when determining the future prescription for a patient, we usually have access to some auxiliary information such as the current prescription that she is receiving, and her current lab results. In consideration of the health care costs and treatment transients, it is not desired to switch patients’ treatments too frequently. We thus set a threshold level for the expected improvement in the outcome, below which the randomized strategy will be “frozen” and the current
7.3. Prescriptive Policy Development 193 
therapy will be continued. Specifically, 
mf(x) 
= 
 m, w.p. e−ξŷm(x)∑M 
j=1 e −ξŷj(x) , if ∑ 
k 
e−ξŷk(x)∑ j e−ξŷj(x) ŷk(x) ≤ xco − T (x), 
mc(x), otherwise, 
where mf(x) and mc(x) are the future and current prescriptions for patient x, respectively; xco represents the current observed outcome (e.g., current blood pressure), which is assumed to be one of the components of x, and T (x) is some threshold level which will be determined later. This prescriptive rule basically says that the randomized strategy will be activated only if the expected improvement relative to the current observed outcome is significant. 
Theorem 7.3.2. Assume that the distribution of the predicted outcome ŷm(x) conditional on x, is sub-Gaussian, and its ψ2-norm is equal to√ 
2Cm(x), for any m ∈ [M ] and any x. Given a small 0 < ε̄ < 1, to satisfy 
P (∑ 
k 
e−ξŷk(x)∑ j e −ξŷj(x) ŷk(x) > xco − T (x) 
) ≤ ε̄, 
it suffices to set a threshold 
T (x) = max ( 0, min 
m 
( xco − µŷm(x)− 
√ −2C2 
m(x) log(ε̄/M) )) , 
where µŷm(x) = E[ŷm(x)|x]. 
Proof. By the sub-Gaussian assumption we have: 
P (∑ 
k 
e−ξŷk(x)∑ j e −ξŷj(x) ŷk(x) > xco − T (x) 
) ≤ P 
( max k 
ŷk(x) > xco − T (x) ) 
= P (⋃ k 
{ ŷk(x) > xco − T (x) 
}) ≤ ∑ k 
P ( ŷk(x) > xco − T (x) 
) ≤ ∑ k 
exp ( − ( xco − T (x)− µŷk(x) 
)2 2C2 
k(x) 
) . 
(7.8)
194 Optimal Decision Making via Regression Informed K-NN 
Note that the probability in (7.8) is taken with respect to the measure of the training samples. We essentially want to find the largest threshold T (x) such that the probability of the expected improvement being less than T (x) is small. Given a small 0 < ε̄ < 1 and due to (7.8), to satisfy 
P (∑ 
k 
e−ξŷk(x)∑ j e −ξŷj(x) ŷk(x) > xco − T (x) 
) ≤ ε̄, 
it suffices to set:∑ k 
exp ( − ( xco − T (x)− µŷk(x) 
)2 2C2 
k(x) 
) ≤ ε̄. (7.9) 
A sufficient condition for (7.9) is: 
exp ( 
(− ( xco − T (x)− µŷm(x) 
)2 2C2 
m(x) 
) ≤ ε̄ 
M , ∀m ∈ JMK, 
which yields that, 
T (x) ≤ xco − µŷm(x)− √ −2C2 
m(x) log(ε̄/M), ∀m ∈ JMK. (7.10) 
Given that T (x) is non-negative, we set the largest possible threshold satisfying (7.10) to: 
T (x) = max ( 0, min 
m 
( xco − µŷm(x)− 
√ −2C2 
m(x) log(ε̄/M) )) . 
When using a deterministic policy (ξ →∞), for any m ∈ JMK, we have 
P(min m 
ŷm(x) > xco − T (x)) = P (⋂ m 
{ ŷm(x) > xco − T (x) 
}) ≤ P(ŷm(x) > xco − T (x)) 
≤ exp ( − ( xco − T (x)− µŷm(x) 
)2 2C2 
m(x) 
) . 
Similarly, to make 
P ( min m 
ŷm(x) > xco − T (x) ) ≤ ε̄, 
we set: 
T (x) = max ( 0, min 
m 
( xco − µŷm(x)− 
√ −2C2 
m(x) log ε̄ )) , 
which establishes the desired result.
7.3. Prescriptive Policy Development 195 
Theorem 7.3.2 finds the largest threshold T (x) such that the probability of the expected improvement being less than T (x) is small. The parameters µŷm(x) and Cm(x), for m ∈ JMK, can be estimated by simulation through random sampling a subset of the training examples. Algorithm 1 provides the details. 
Algorithm 1 Estimating the conditional mean and standard deviation of the predicted outcome. Input: a feature vector x; am: the number of subsamples used to compute β̂m, am < Nm; dm: the number of repetitions. for i = 1, . . . , dm do 
Randomly pick am samples from group m, and use them to estimate a robust regression coefficient β̂mi through solving (4.5). 
The future outcome for x under action m is predicted as ŷmi(x) = x′β̂mi . end for Output: Estimate the conditional mean of ŷm(x) as: 
µŷm(x) = 1 dm 
∑dm 
i=1 ŷmi(x), 
and the conditional standard deviation as: 
Cm(x) = √ 
1 dm − 1 
∑dm 
i=1 
( ŷmi(x)− µŷm(x) 
)2 . 
A Special Case As ξ → ∞, the randomized policy will assign probability 1 to the action with the lowest predicted outcome, which is equivalent to the following deterministic policy: 
mf(x) = 
arg min m 
ŷm(x), if min m 
ŷm(x) ≤ xco − T (x), mc(x), otherwise. 
A slight modification to the threshold level T (x) is given as follows: 
T (x) = max ( 0, min 
m 
( xco − µŷm(x)− 
√ −2C2 
m(x) log ε̄ )) .
196 Optimal Decision Making via Regression Informed K-NN 
7.4 Developing Optimal Prescriptions for Patients 
In this section, we apply our method to develop optimal prescriptions for patients with type-2 diabetes and hypertension. The data used for the study come from the Boston Medical Center – the largest safety-net hospital in New England – and consist of Electronic Health Records (EHRs) containing the patients’ medical history in the period 1999–2014. The medical history of each patient includes demographics, diagnoses, prescriptions, lab tests, and past admission records. We build two datasets from the EHRs, one containing the medical records of patients with type-2 diabetes and the other for patients with hypertension. For diabetic patients, we want to determine the treatment (drug regimen) that leads to the lowest future HbA1c 
1 based on the medical histories, while for hypertension patients, our goal is to find the treatment that minimizes the future systolic blood pressure. 2 
7.4.1 Description of the Datasets 
The patients that meet the following criteria are included in the diabetes dataset: 
 Patients present in the system for at least 1 year; 
 Received at least one blood glucose regulation agent, including injectable (e.g., insulin) and oral (e.g., metformin) drugs, etc., and had at least one medical record 100 days before this prescription; 
 Had at least three measurements of HbA1c in the system; and, 
 Were not diagnosed with type-1 diabetes. 
Similarly, for the hypertension dataset, the patients that meet the following criteria are included: 
1HbA1c measures the percentage of glycosylated hemoglobin in the total amount of hemoglobin present in the blood. It reflects average blood glucose levels over the past 6–8 weeks. The normal range is below 5.7%. 
2Systolic blood pressure is the maximum arterial pressure during contraction of the left ventricle of the heart. It is measured in mmHg (millimeters of mercury) and the normal range is below 120.
7.4. Developing Optimal Prescriptions for Patients 197 
 Patients present in the system for at least 1 year; 
 Received at least one type of cardiovascular medications, including ACE inhibitors, Angiotensin Receptor Blockers (ARB), calcium channel blockers, diuretics, α-blockers and β-blockers, and had at least one medical record 10 days before this prescription. 
 Had at least one recorded diagnosis of hypertension (corresponding to the ICD-9 diagnosis codes 401-405); 
 Had at least three measurements of the systolic blood pressure. 
We have identified 11,230 patients for the diabetes dataset and 49,401 patients for the hypertension dataset. Each patient may have multiple entries in her/his medical record. We define the line of therapy as a time period (between 200 and 500 days) during which the combination of drugs prescribed to the patient does not change. Each line of therapy is characterized by a drug regimen which is defined as the combination of drugs prescribed to the patient within the first 200 days. The line of therapy intends to capture the period when the patient was experiencing the effect of the drug regimen. 
We define patient visits within each line of therapy to reflect changes in the features and outcomes. For the diabetic patients, we consider four possible drug regimens (combinations of oral and injectable drugs), while for the hypertension patients, we consider the most frequent 19 of the 32 combinations of drugs and merge all others into one class. 
Diabetic Patients. During each line of therapy, we assume that the patient visits every 100 days, beginning from the start of the therapy and continuing until at least 80 days prior to the end of the therapy. The measurements, lab tests are averaged over the 100 days prior to the visit. We define the current prescription of each visit as the combination of drugs that was given during the 100 days immediately preceding the visit, and the standard of care as the drug regimen that is prescribed by the doctors at the time of the visit. If no value exists over the 100 days, we use the neighboring visits to determine the measurements/lab tests (through linear interpolation) and the current prescription. The
198 Optimal Decision Making via Regression Informed K-NN 
future outcome for each visit is computed as the average HbA1c 75 to 200 days after the visit. Patient visits that contain missing values for the outcome are dropped. We end up with 12,016 valid visits, which are divided into four groups based on their standard of care. 
Hypertension Patients. During each line of therapy, the patient visits are considered occurring every 70 days, beginning from the start of the therapy and continuing until at least 180 days prior to the end of the therapy. The measurements, lab tests are averaged over the 10 days prior to the visit. We define the current prescription of each visit as the combination of drugs that was given during the 10 days immediately preceding the visit, and the standard of care as the drug regimen that is prescribed by the doctors at the time of the visit. We narrow down the time window due to the fact that the blood pressure is usually much more noisy than the HbA1c, and thus the features within a smaller time window tend to be more relevant. The future outcome of the visit is the average systolic blood pressure 70 to 180 days after it. Linear interpolation is used to replace the missing values of the measurements and lab tests. We have obtained 26,128 valid visits, which are divided into 20 groups based on their standard of care. 
Prescriptions. The prescriptions are used to group the patient visits. For the diabetic patients, we consider two types of prescriptions: one includes oral medications, e.g., metformin, pioglitazone, and sitagliptin, etc., and the other type includes injectable medications, e.g., insulin. Typically, injectable medications are prescribed for patients with more advanced disease. For the hypertension patients, six types of prescriptions are considered: ACE inhibitor, Angiotensin Receptor Blockers (ARB), calcium channel blockers, thiazide and thiazide-like diuretics, α-blockers and β-blockers. 
The following sets of features are considered for building the predictive model. The number of features included in both datasets is 63. All features are standardized before fed into our algorithm. 
Demographic information. Includes sex (male, female and other), age and race (10 types). We consider the three most frequent races:
7.4. Developing Optimal Prescriptions for Patients 199 
Caucasian, Black, and Hispanic, and group all others into one category ‘other’. 
Measurements. Systolic/diastolic blood pressure (mmHg), Body Mass Index (BMI) and pulse. 
Lab tests. Two types of tests considered: blood chemistry tests such as calcium, carbon dioxide, chloride, potassium, sodium, creatinine, and urea nitrogen; and hematology tests such as blood glucose, hematocrit, hemoglobin, leukocyte count, platelet count, and mean corpuscular volume. 
Diagnosis history. The ICD-9 coding system is used to record diagnoses. 
7.4.2 Model Development and Results 
We will compare our prescriptive algorithm with several alternatives that replace our Distributionally Robust Linear Regression (DRLR) informed K-NN with a different predictive model such as LASSO, CART, and OLS informed K-NN (Bertsimas et al., 2017). Both deterministic and randomized prescriptive policies are considered using predictions from these models. We note a very recent tree-based algorithm called Optimal Prescription Tree (OPT) developed in Bertsimas et al., 2019b, that uses either constant or linear models in the leaves of the tree in order to predict the counterfactuals and to assign optimal treatments to new samples. We do not include it as a comparison in this work, yet, it would be interesting to do in subsequent work. 
Parameter tuning. Within each prescription group, we randomly split the patient visits into three sets: a training set (80%), a validation set (10%), and a test set (10%). To reflect the dependency of the number of neighbors on the number of training samples, we perform a linear regression between these two quantities, which will be used to determine the number of neighbors needed in different settings.
200 Optimal Decision Making via Regression Informed K-NN 
To tune the exponent ξ for the randomized strategy, it is necessary to evaluate the effects of counterfactual treatments. We assess the predictive power of a series of robust predictive models in terms of the following metrics: 
 R-square: 
R2(y, ŷ) = 1− ∑Nt i=1(yi − ŷi)2∑Nt i=1(yi − ȳ)2 
, 
where y = (y1, . . . , yNt) and ŷ = (ŷ1, . . . , ŷNt) are the vectors of the true (observed) and predicted outcomes, respectively, with Nt 
the size of the test set, and ȳ = (1/Nt) ∑Nt i=1 yi. 
 Mean Squared Error (MSE): 
MSE(y, ŷ) = 1 Nt 
∑Nt 
i=1 (yi − ŷi)2. 
 Mean Absolute Error (MeanAE), which is more robust to large deviations than the MSE in that the absolute value function increases more slowly than the square function over large (absolute) values of the argument. 
MeanAE(y, ŷ) = 1 Nt 
∑Nt 
i=1 |yi − ŷi|. 
 MAD, which can be viewed as a robust measure of the MeanAE, computing the median of the absolute deviations: 
MAD(y, ŷ) = Median (|yi − ŷi|, i ∈ JNtK) . 
The out-of-sample performance metrics of the various models on the two datasets are shown in Tables 7.1 and 7.2, where the numbers in the parentheses show the improvement of DRLR informed K-NN compared against other methods. Huber refers to the robust regression method proposed in Huber, 1964; Huber, 1973, and CART refers to the Clas-sification And Regression Trees. Huber/OLS/LASSO + K-NN means fitting a K-NN regression model with a Huber/OLS/LASSO-weighted distance metric. We note that in order to produce well-defined and meaningful predictive performance metrics, the dataset used to generate
7.4. Developing Optimal Prescriptions for Patients 201 
Tables 7.1 and 7.2 did not group the patients by their prescriptions. A universal model was fit to all patients with prescription information being used as one of the predictors. Nevertheless, it would still be considered as a fair comparison as all models were evaluated on the same dataset. The results provide supporting evidence for the validity of our DRLR+K-NN model that outperforms all others in all metrics, and is thus used to impute the outcome for an unobservable treatment m, through averaging over the most similar patient visits who have received the prescription m in the validation set, where the number of neighbors is selected to fit the size of the validation set. Note that using DRLR+K-NN as an imputation model might cause bias in evaluating the performance of different methods, since it is in favor of the framework that uses the same model (DRLR+K-NN) to predict the future outcome. Using a weighted combination of several different predictive models may alleviate the bias. This could be done in future work. 
Table 7.1: Performance of different models for predicting future HbA1c for diabetic patients. 
Methods R2 MSE MeanAE MAD OLS 0.52 (2%) 1.36 (2%) 0.81 (4%) 0.55 (11%) 
LASSO 0.52 (2%) 1.37 (2%) 0.80 (3%) 0.54 (9%) Huber 0.36 (47%) 1.81 (26%) 0.96 (19%) 0.70 (30%) RLAD 0.50 (4%) 1.40 (4%) 0.78 (1%) 0.50 (1%) K-NN 0.25 (109%) 2.11 (37%) 1.07 (27%) 0.81 (39%) 
OLS+K-NN 0.52 (0%) 1.34 (0%) 0.79 (1%) 0.51 (3%) LASSO+K-NN 0.52 (1%) 1.36 (1%) 0.79 (1%) 0.50 (1%) Huber+K-NN 0.51 (3%) 1.38 (3%) 0.81 (3%) 0.53 (7%) DRLR+K-NN 0.52 (N/A) 1.34 (N/A) 0.78 (N/A) 0.49 (N/A) 
CART 0.49 (7%) 1.43 (7%) 0.81 (3%) 0.50 (2%) 
Model training. We solve the predictive models on the whole training set with the best tuned parameters, the output of which is used to develop the optimal prescriptions for the test set patients. The parameter ε̄ in the threshold T (x) is set to 0.1. For estimating the conditional mean and standard deviation of the predicted outcome using Algorithm 1, we set am = 0.9Nm, and dm = 100. We compute the average improvement
202 Optimal Decision Making via Regression Informed K-NN 
Table 7.2: Performance of different models for predicting future systolic blood pressure for hypertension patients. 
Methods R2 MSE MeanAE MAD OLS 0.31 (14%) 170.80 (6%) 10.09 (7%) 8.15 (9%) 
LASSO 0.31 (14%) 170.83 (6%) 10.08 (7%) 8.22 (10%) Huber 0.22 (62%) 193.54 (17%) 10.70 (12%) 8.61 (14%) RLAD 0.30 (18%) 173.32 (8%) 10.11 (7%) 8.28 (11%) K-NN 0.33 (10%) 167.41 (5%) 9.62 (2%) 7.50 (2%) 
OLS+K-NN 0.35 (1%) 160.22 (0%) 9.42 (0%) 7.49 (1%) LASSO+K-NN 0.32 (12%) 169.50 (6%) 9.74 (3%) 7.73 (5%) Huber+K-NN 0.32 (10%) 167.92 (5%) 9.71 (3%) 7.84 (6%) DRLR+K-NN 0.36 (N/A) 159.74 (N/A) 9.42 (N/A) 7.38 (N/A) 
CART 0.25 (43%) 186.23 (14%) 10.34 (9%) 8.22 (10%) 
(reduction) in outcomes for patients in the test set, which is defined to be the difference between the (expected) future outcome under the recommended therapy and the current observed outcome. If the recommendation does not match the standard of care, its future outcome is estimated through the imputation model that was discussed earlier, where Km should be selected to fit the size of the test set. 
Results and discussions. The reductions in outcomes (future minus current) for various models are shown in Table 7.3. The columns indicate the prescriptive policies (deterministic or randomized); the rows represent the predictive models whose outcomes ŷm(x) serve as inputs to the prescriptive algorithm. We test the performance of all algorithms over five repetitions, each with a different training set. The numbers outside the parentheses are the mean reductions in the outcome and the numbers inside the parentheses are the corresponding standard deviations. We note that HbA1c is measured in percentage while systolic blood pressure in mmHg. We also list the reductions in outcomes resulted from the standard of care, and the current prescription which prescribes mf(x) = mc(x) with probability one, i.e., always continuing the current drug regimen. 
Several observations are in order: (i) all models outperform the current prescription and the standard of care; (ii) the DRLR-informed
7.4. Developing Optimal Prescriptions for Patients 203 
Table 7.3: The reduction in HbA1c/systolic blood pressure for various models. 
Diabetes Hypertension Deterministic Randomized Deterministic Randomized 
LASSO -0.51 (0.16) -0.51 (0.16) -4.71 (1.09) -4.72 (1.10) CART -0.45 (0.13) -0.42 (0.14) -4.84 (0.62) -4.87 (0.66) 
OLS+K-NN -0.53 (0.13) -0.53 (0.13) -4.33 (0.46) -4.33 (0.47) DRLR+K-NN -0.56 (0.06) -0.55 (0.08) -6.98 (0.86) -7.22 (0.82) 
Current prescription 
-0.22 (0.04) -2.52 (0.19) 
Standard of care -0.22 (0.03) -2.37 (0.11) 
K-NN model leads to the largest reduction in outcomes with a relatively stable performance; and (iii) the randomized policy achieves a similar performance (slightly better on the hypertension dataset) to the deterministic one. We expect the randomized strategy to win when the effects of several treatments do not differ much, in which case the deterministic algorithm might produce misleading results. The randomized policy could potentially improve the out-of-sample (generalization) performance, as it gives the flexibility of exploring options that are suboptimal on the training set, but might be optimal on the test set. The advantages of the DRLR+K-NN model are more prominent in the hypertension dataset, due to the fact that we considered a finer classification of the prescriptions for patients with hypertension, while for diabetic patients, we only distinguish between oral and injectable prescriptions. 
7.4.3 Refinement on the DRLR+K-NN Model 
Up to now, we used a patient-independent parameter Km (the number of neighbors in group m) to predict the effects of treatments on different individuals. Such a strategy might improperly utilize less relevant information and lead to inadequate predictions. For example, denote by dmi the distance between the patient in question and her i-th closest neighbor in group m, and assume there exists a “big jump” at dmj , i.e.,
204 Optimal Decision Making via Regression Informed K-NN 
dmj − ∑j−1 i=1 d 
m i /(j − 1) is large. If Km ≥ j, we would include the j-th 
closest neighbor in computing the K-NN average, resulting in a biased estimate given its dissimilarity to the patient of interest. 
We thus propose a patient-specific rule to determine the appropriate number of neighbors. Specifically, using the notations dmi defined above, we know dm1 ≤ dm2 ≤ · · · ≤ dmKm . Define 
j∗m = arg max j 
( dmj − 
∑j−1 i=1 
dmi j − 1 
) . 
The number of neighbors K ′m will be determined as follows: 
K ′m = 
 j∗m − 1, if 
dm j∗m − ∑j∗m−1 
i=1 dm i 
j∗m−1∑j∗m−1 i=1 
dm i 
j∗m−1 
> T̃ , 
Km, otherwise, 
where T̃ is some threshold that can be tuned using cross-validation. This strategy discards the neighbors that are relatively far away from the patient under consideration. We test this strategy on the two datasets, using a cross-validated threshold T̃ = 2.5 and 1 for diabetes and hypertension, respectively, and show the results in Tables 7.4 and 7.5. Notice that such a truncation strategy could affect both the training of DRLR+K-NN and the imputation model that is used to evaluate the effects of counterfactual treatments. To compare with the original strategy of using a uniform Km for every patient, we list in the left halves of the tables the results from adopting the truncation strategy to both training and imputation, and in the right halves the results from applying the truncation only to the imputation/evaluation model. We see that using a patient-specific K ′m in general leads to a larger reduction in outcomes. 
7.5 Summary 
We proposed an interpretable robust predictive method by combining ideas from distributionally robust optimization with the local learning procedure K-Nearest Neighbors, and established theoretical guarantees on its out-of-sample predictive performance. We also developed a randomized prescriptive policy based on the robust predictions, and proved
7.5. Summary 205 
Table 7.4: The reduction in HbA1c for various models (T̃ = 2.5). 
Training with K′m Training with Km 
Deterministic Randomized Deterministic Randomized 
LASSO -0.54 (0.19) -0.54 (0.20) -0.50 (0.17) -0.49 (0.17) CART -0.62 (0.32) -0.57 (0.27) -0.56 (0.19) -0.53 (0.15) 
OLS+K-NN -0.65 (0.25) -0.64 (0.25) -0.61 (0.16) -0.61 (0.17) DRLR+K-NN -0.68 (0.20) -0.67 (0.23) -0.61 (0.10) -0.59 (0.10) 
Current prescription -0.23 (0.05) -0.22 (0.05) 
Standard of care -0.22 (0.03) -0.22 (0.03) 
Table 7.5: The reduction in systolic blood pressure for various models (T̃ = 1). 
Training with K′m Training with Km 
Deterministic Randomized Deterministic Randomized 
LASSO -4.34 (0.28) -4.33 (0.28) -4.22 (0.20) -4.22 (0.19) CART -4.46 (0.46) -4.49 (0.50) -4.48 (0.55) -4.51 (0.49) 
OLS+K-NN -4.30 (0.35) -4.30 (0.32) -4.27 (0.32) -4.29 (0.31) DRLR+K-NN -7.42 (0.46) -7.58 (0.51) -6.58 (0.70) -6.78 (0.73) 
Current prescription -2.56 (0.14) -2.50 (0.16) 
Standard of care -2.37 (0.11) -2.37 (0.11) 
its optimality in terms of the expected true outcome. In conjunction, we derived a closed-form expression for a clinically meaningful threshold that is used to activate the randomized prescriptive policy. We applied the proposed methodology to a diabetes and a hypertension dataset obtained from a major safety-net hospital, providing numerical evidence for the predicted improvement on outcomes due to our algorithm.
8 
Advanced Topics in Distributionally Robust 
Learning 
In this section, we will cover a number of active research topics in the domain of DRO under the Wasserstein metric. Different from previous sections, where we focused on traditional supervised learning models with identically and independently distributed labeled data, here we want to explore how to adapt the DRO framework to more complex data and model regimes. Specifically, we will study: 
 Distributionally Robust Semi-Supervised Learning (SSL), which estimates a robust classifier with partially labeled data, through (i) either restricting the marginal distribution to be consistent with the unlabeled data, (ii) or modifying the structure of DRO by allowing the center of the ambiguity set to vary, reflecting the uncertainty in the labels of the unsupervised data. 
 DRO in Reinforcement Learning (RL) with temporally correlated data, which considers Markov Decision Processes (MDPs) and seeks to inject robustness into the probabilistic transition model. We will derive a lower bound for the distributionally robust value function in a regularized form. 
206
8.1. Distributionally Robust Learning with Unlabeled Data 207 
8.1 Distributionally Robust Learning with Unlabeled Data 
In this section we study a Distributionally Robust Optimization (DRO) model with the availability of unlabeled data. This problem can be approached with two types of model architectures. One assumes a setting where supervised DRO with labeled data does not ensure a good generalization performance, and explores the role of unlabeled data in enhancing the performance of conventional supervised DRO, while the other is set up in a semi-supervised setting with potential noise on both labeled and unlabeled data, and aims to robustify SSL algorithms by employing the DRO framework. 
Note that the role of the unlabeled data in the two modeling schemes is different, so are the learning objectives. One seeks to utilize the additional information contained in the unlabeled data, while the other seeks immunity to perturbations on both labeled and unlabeled data. As we will see in the subsequent sections, the former objective is realized through confining the elements of the DRO formulation, i.e., the ambiguity set Ω, to digest the additional information brought by the unlabeled data. By contrast, the latter requires modification of the underlying infrastructure of DRO so that it can be adapted to existing SSL algorithms. 
Examples of past works that use unlabeled data to improve adversarial robustness include Carmon et al., 2019; Raghunathan et al., 2019; Zhai et al., 2019; Alayrac et al., 2019. For inducing robustness to SSL, Yan et al., 2016 proposed an ensemble learning approach through label aggregation. Previous works that fall into the intersection of DRO and SSL include Frogner et al., 2019; Blanchet and Kang, 2017b; Najafi et al., 2019, where the first two study the role of unlabeled data in improving the generalization performance, while the third one focuses on robustifying a well-known SSL framework, called self-training, by using the DRO. 
Throughout this section, we consider aK-class classification problem with a dataset D of size N consisting of two non-overlapping sets Dl (labeled) and Dul (unlabeled), with size Nl and Nul, respectively, and Nl + Nul = N . Denote by Il and Iul the index sets corresponding to the labeled and unlabeled data points, respectively. Thus, Dl = {zi ,
208 Advanced Topics in Distributionally Robust Learning 
(xi, yi) : i ∈ Il}, where yi ∈ JKK, and Dul = {xi : i ∈ Iul}. 
8.1.1 Incorporating Unlabeled Data into Distributionally Robust Learning 
One of the prerequisites for ensuring a good generalization performance of Wasserstein DRO requires that the ambiguity set includes the true data distribution. In a “medium-data” regime, where the observed data may be far from the true data distribution, the Wasserstein ball must be extremely large to contain the true data distribution (cf. Theorem 2.7.1). As a result, the learner has to be robust to an enormous variety of data distributions, preventing it from making a prediction with any confidence (Frogner et al., 2019). To address this problem, a number of works have proposed to use unlabeled data to further constrain the adversary, see Frogner et al., 2019; Blanchet and Kang, 2017b. Recall the general Wasserstein DRO formulation for a supervised learning problem with feature vector x and label y: 
inf β 
sup Q∈Ω 
EQ[hβ(x, y) ] , (8.1) 
where hβ(x, y) is the loss function evaluated at some hypothesis β, and Q is the probability distribution of (x, y) belonging to some set Ω that constrains the distribution to be close to the empirical distribution of the labeled data, denoted by P̂Nl , in the sense of the order-1 Wasserstein metric induced by a cost metric s: 
Ω , {Q ∈ P(X × Y) : Ws,1(Q, P̂Nl) ≤ ε}. 
To overcome the problem of overwhelmingly-large ambiguity set Ω, Frogner et al., 2019 proposed to remove from Ω the distributions that are unrealistic in the sense that their marginals in feature space do not resemble the unlabeled data. Specifically, they define the uncertainty set to be 
Ω , {Q ∈ U(PX ,PY ,PY) : Ws,1(Q, P̂Nl) ≤ ε}, (8.2) 
where PY and PY are two distributions on the label y with probability vectors p , (p1, . . . , pK) and p , (p1, . . . , pK), respectively, and U(PX ,PY ,PY) is the set of probability measures whose x-marginal is
8.1. Distributionally Robust Learning with Unlabeled Data 209 
PX and y-marginal is constrained by [p,p], i.e., the class i probability pi ∈ [p 
i , pi], i ∈ JKK. They choose PX to be consistent with the 
unlabeled data x ∈ Dul. The constraint on PY could come from prior knowledge, or could be implied by the labeled training data. 
Blanchet and Kang, 2017b also constrained the uncertainty set Ω by incorporating the information of the unlabeled data. Different from (8.2) where the marginals are enforced to be consistent with the unlabeled data, they set the joint support of the feature and labels to be confined to the empirical observations. Specifically, they build a “complete” unlabeled set by assigning all possible labels to each unlabeled data point: Cul , 
⋃K y=1{(xi, y) : i ∈ Iul}, and then construct 
the full dataset C = Dl ∪ Cul. The uncertainty set is restricted to be supported on C, namely, 
Ω , {Q ∈ P(C) : Ws,1(Q, P̂Nl) ≤ ε}. (8.3) 
Compared to (8.2), (8.3) is more restrictive in the sense that it imposes constraints on the joint distribution of the feature and labels, while (8.2) only restricts the marginals. Furthermore, it does not allow support points outside the empirical observations, which eliminates one of the major advantages of the Wasserstein metric. In the absence of the unlabeled data, (8.3) essentially asks the learner to be robust only to distributions with support on Dl, which could hurt the generalization capability on unseen data. By contrast, (8.2) guarantees robustness to distributions with support on the whole data space. 
Note that the DRO formulation with an uncertainty set defined through either (8.2) or (8.3) does not serve the purpose of robustifying an existing SSL model. Rather, it explores ways of improving the generalization performance of a DRO model by utilizing the unlabeled data information. 
In the remainder of this section, we will discuss a Stochastic Gradient Descent (SGD) algorithm proposed in Frogner et al., 2019, in order to solve the Wasserstein DRO formulation assembled with the ambiguity set (8.2). The key is to transform the inner infinite-dimensional maximization problem in (8.1) into its finite-dimensional dual. Define the
210 Advanced Topics in Distributionally Robust Learning 
worst-case expected loss as vP (β) , sup 
Q∈Ω EQ[hβ(x, y) 
] . (8.4) 
Rewrite (8.4) by casting it as an optimal transportation problem with a transport plan π ∈ P(Z × Z): vP (β) = sup 
π∈P(Z×Z) 
∫ (X×Y)×Z hβ(x, y)dπ((x, y), z′) 
s.t. ∫ Z×Z s(z, z′)dπ(z, z′) ≤ ε,∫ Z×Z δzi(z′)dπ(z, z′) = 1 
Nl , ∀i ∈ Il,∫ 
(A×Y)×Z dπ((x, y), z′) = PX (A), ∀A ⊆ X ,∫ (X×Y)×Z δi(y)dπ((x, y), z′) ≤ pi, ∀i ∈ JKK,∫ (X×Y)×Z δi(y)dπ((x, y), z′) ≥ p 
i , ∀i ∈ JKK, 
(8.5) where we use z , (x, y) to index the support of the worst-case measure and z′ to index the support of P̂Nl . Notice that the constraint on the x-marginal is infinite dimensional. Through translating (8.5) to its dual one can move the infinite dimensional constraint to an expectation under PX in the objective. The dual to (8.5) can be formulated as 
vD(β) = inf α,γ,λ,λ 
αε+ 1 Nl 
∑Nl i=1 γi +∑K 
k=1(λkpk − λkpk)+ 
EPX [ φ(x;β, α,γ,λ,λ) 
] s.t. α, λk, λk ≥ 0, ∀k ∈ JKK, 
(8.6) 
where φ(x;β, α,γ,λ,λ) = max 
i∈JNlK,k∈JKK φi,k(x;β, α,γ,λ,λ), 
φi,k(x;β, α,γ,λ,λ) , hβ(x, k)− ( αs ( (x, k), zi 
) + γi 
) − (λk − λk). 
It can be shown that strong duality holds if the primal problem (8.5) is feasible. We refer the reader to Theorem 2 of Frogner et al., 2019 for a detailed proof. The DRO problem (8.1) reduces to minimizing vD(β) w.r.t. β, which can be solved via the stochastic gradient method. The main obstacle to deriving the gradient lies in the expectation in the objective of vD(β). By applying the Reynolds Transport Theorem (Reynolds et al., 1903), one can obtain that 
∂ 
∂α EPX 
[ φ(x;β, α,γ,λ,λ) 
] = EPX 
[ ∂ ∂α 
φ(x;β, α,γ,λ,λ) ] . (8.7)
8.1. Distributionally Robust Learning with Unlabeled Data 211 
Notice that φ is defined to be the maximum of a series of functions φi,k. To evaluate its derivative, we need to partition the feature space X to recognize the set of points x where the maximum is achieved at each (i, k). Define 
V i,k , { x ∈ X : φi,k(x;β, α,γ,λ,λ) ≥ φi′,k′(x;β, α,γ,λ,λ),∀i′, k′ 
} . 
The derivative of φ can be evaluated as 
∂ 
∂α φ(x;β, α,γ,λ,λ) = − 
∑Nl 
i=1 
∑K 
k=1 1Vi,k(x)s 
( (x, k), zi 
) , 
where 1Vi,k(x) denotes the indicator function of the event x ∈ V i,k. Similarly, the gradients w.r.t. other parameters are computed as follows. 
∂ 
∂γi φ(x;β, α,γ,λ,λ) = − 
∑K 
k=1 1Vi,k(x), 
∂ 
∂λk φ(x;β, α,γ,λ,λ) = 
∑Nl 
i=1 1Vi,k(x), 
∂ 
∂λk φ(x;β, α,γ,λ,λ) = − 
∑Nl 
i=1 1Vi,k(x), 
∂ 
∂βj φ(x;β, α,γ,λ,λ) ∈ 
∑Nl 
i=1 
∑K 
k=1 1Vi,k(x) ∂ 
∂βj hβ(x, k). 
For x lying on the boundary between two of the sets V i,k, we can obtain a subgradient by arbitrarily selecting only one of these V i,k to contain x when evaluating 1Vi,k(x). To evaluate the expectation of the gradient under PX on the RHS of (8.7), one can simulate a series of x values, say x1, . . . ,xNb , from PX , and compute the above gradients by taking the sample average. This is summarized in Algorithm 2.
212 Advanced Topics in Distributionally Robust Learning 
Algorithm 2 SGD for distributionally robust learning with unlabeled data under uncertainty set (8.2). Input: ε ≥ 0, p 
i , pi ∈ [0, 1], i ∈ JKK, feasible solution β0, step size 
δ > 0, batch size Nb. β ← β0, α← 0,γ,λ,λ← 0. while not converged do 
Sample x1, . . . ,xNb ∼ PX . β ← ProjB 
[ β − δ 
Nb 
∑Nb j=1∇βφ(xj ;β, α,γ,λ,λ) 
] α← max 
( 0, α− δ 
[ ε+ 1 
Nb 
∑Nb j=1∇αφ(xj ;β, α,γ,λ,λ) 
]) γ ← γ − δ 
[ 1 Nl 
e + 1 Nb 
∑Nb j=1∇γφ(xj ;β, α,γ,λ,λ) 
] λ← max 
( 0,λ− δ 
[ − p + 1 
Nb 
∑Nb j=1∇λφ(xj ;β, α,γ,λ,λ) 
]) λ← max 
( 0,λ− δ 
[ p + 1 
Nb 
∑Nb j=1∇λφ(xj ;β, α,γ,λ,λ) 
]) end while 
8.1.2 Distributionally Robust Semi-Supervised Learning 
In this subsection we discuss the problem of robustifying existing SSL algorithms via DRO. Different from Section 8.1.1, the goal here is to induce robustness into conventional SSL models, which requires modification of the DRO infrastructure in order to fit the characteristics of the problem at hand. Note that DRO cannot readily be applied to the partially-labeled setting, since it needs complete knowledge of all the feature-label pairs. 
A well-known family of SSL models is called self-learning, which first trains a classifier on the labeled portion of a dataset, and then assigns pseudo-labels to the remaining unlabeled samples using the learned rules. The enlarged dataset consisting of both the supervised and artificiallylabeled unsupervised samples is used in the final stage of training. To prevent overfitting, instead of assigning a deterministic hard label to the unsupervised data points, one can apply a soft labeling scheme that maintains a level of uncertainty through specifying a probability distribution of the labels. 
To use DRO in a semi-supervised setting, we need to address the uncertainty embedded in the unknown labels of the unsupervised sam-
8.1. Distributionally Robust Learning with Unlabeled Data 213 
ples. This can be resolved by soft-labeling. Define the consistent set of probability distributions P̂(D) ⊆ P(Z) w.r.t. a partially-labeled dataset D = Dl ∪ Dul as 
P̂(D) , {(Nl 
N 
) P̂Nl + 
(Nul 
N 
) P̂Nul ·Q : Q ∈ PX (Y) 
} , 
where Q encodes the uncertainty in the labels for the unsupervised dataset Dul, and PX (Y) denotes the set of all conditional distributions supported on Y, given features in X . Note that the distributions in P̂(D) differ from each other only in the way they assign soft labels to the unlabeled data, and the empirical measure corresponding to the true complete dataset is a member of P̂(D). 
We will illustrate the idea proposed in Najafi et al., 2019 for introducing DRO to SSL, where they select a suitable measure from P̂(D), and use it as a proxy of the true empirical probability measure that serves as the center of the Wasserstein ball. The learner essentially aims to hedge against a set of distributions centered at some S ∈ P̂(D) that is induced by a soft-label distribution Q, so that the resulting classification rule would show low sensitivity to adversarial perturbations around the soft-label distribution. The criterion for choosing S is to make the worst-case expected loss as small as possible. Specifically, the Semi-Supervised Distributionally Robust Learning (SSDRO) model proposed by Najafi et al., 2019 can be formulated as 
inf β 
inf S∈P̂(D) 
{ sup 
P∈Ωε(S) EP[hβ(x, y) 
] + (1−Nl/N 
λ 
) EP̂Nul [H(S|x)] 
} , (8.8) 
where Ωε(S) denotes the set of probability distributions that are close to S by a distance at most ε, i.e., 
Ωε(S) , {P ∈ P(Z) : Ws,1(P, S) ≤ ε}, 
In (8.8), S|x is the conditional distribution over Y given x ∈ X , λ < 0 is a user-defined parameter, and H(·) denotes the Shannon entropy. 
Notice that for a fixed β, the inner infimum of (8.8) guides the learner to pick a soft label distribution that tends to reduce the loss function, which Najafi et al., 2019 refers to as an optimistic learner. Alternatively, one can choose to be pessimistic, i.e., choosing a β that
214 Advanced Topics in Distributionally Robust Learning 
hedges against the maximum loss over all possible choices of S. To prevent hard labeling of the unsupervised data, λ is set to be negative for optimistic learning, and positive for pessimistic learning. 
Note also that compared to conventional DRO models, in (8.8) we have an additional regularization term that penalizes the Shannon entropy of the conditional label distribution of the unlabeled data. When λ < 0, the regularization term 
( 1−Nl/N 
λ 
) EP̂Nul [H(S|x)] becomes 
negative. The formulation (8.8) essentially promotes softer labels for the unlabeled data by encouraging a larger entropy, implying a higher level of uncertainty in the labels. 
We next discuss how to solve Problem (8.8). Using duality, Najafi et al., 2019 was able to transform the inner min-max formulation to an analytic form whose gradient can be efficiently computed. A Lagrangian relaxation to (8.8) is given in the following theorem. 
Theorem 8.1.1 (Najafi et al., 2019, Theorem 1). Consider a continuous loss function h, and a continuous transportation cost s. For a partiallylabeled dataset D with size N , define the empirical Semi-Supervised Adversarial Risk (SSAR), denoted by R̂SSAR(β;D), as 
R̂SSAR(β;D) , 1 N 
∑ i∈Il 
φγ(xi, yi;β)+ 1 N 
∑ i∈Iul 
(λ) softmin y∈Y 
{φγ(xi, y;β)}+γε, 
(8.9) where γ ≥ 0, and the adversarial loss φγ(x, y;β) and the soft-minimum operator are defined as: 
φγ(x, y;β) , sup z′∈Z 
hβ(z′)− γs ( z′, (x, y) 
) , (8.10) 
and (λ) 
softmin y∈Y 
{q(y)} , 1 λ 
log ( 1 |Y| 
∑ y∈Y 
eλq(y) ) , 
respectively. Let β∗ be a minimizer of (8.8) for some given ε ≥ 0 and λ < 0. Then, there exists γ ≥ 0 such that β∗ is also a minimizer of (8.9) with the same parameters ε and λ. 
According to Theorem 8.1.1 our problem is now translated to solving for a β that minimizes R̂SSAR(β;D). To apply SGD, the key is to derive
8.1. Distributionally Robust Learning with Unlabeled Data 215 
the gradient of the adversarial loss function φγ(x, y;β), which itself is the output of an optimization problem. The gradient of φ w.r.t. β relies on the optimal solution of Problem (8.10), i.e., ∇βφγ(x, y;β) = gβ(z∗(β)), where gβ(z) , ∇βhβ(z) and z∗(β) is the optimal solution to (8.10). The following lemma specifies a set of sufficient conditions to ensure the uniqueness of the solution. 
Lemma 8.1.2 (Najafi et al., 2019, Lemma 1). Assume the loss function h to be differentiable w.r.t. z, and ∇zhβ(z) is Lz-Lipschitz w.r.t. β. Also, the cost metric s is 1-strongly convex in its first argument. If γ > Lz, then Problem (8.10) is (γ − Lz)-strongly concave for all (x, y) ∈ Z. 
Lemma 8.1.2 guarantees the existence and uniqueness of the solution to (8.10). We can thus express the gradients of φ and R̂SSAR explicitly as a function of the solution. An efficient computation of the gradient of R̂SSAR(β;D) w.r.t. β is given in the following theorem. 
Theorem 8.1.3 (Najafi et al., 2019, Lemma 2). Under conditions of Lemma 8.1.2, assume the loss function h to be differentiable w.r.t. β, and let gβ(z) , ∇βhβ(z). For a fixed β, define 
z∗i (β) = arg max z′∈Z 
hβ(z′)− γs ( z′, (xi, yi) 
) , i ∈ Il, (8.11) 
and, 
z∗i (y;β) = arg max z′∈Z 
hβ(z′)− γs ( z′, (xi, y) 
) , y ∈ Y, i ∈ Iul. (8.12) 
Then, the gradient of (8.9) w.r.t. β can be obtained as 
∇βR̂SSAR(β;D) = 1 N 
∑ i∈Il 
gβ(z∗i (β)) + 1 N 
∑ i∈Iul 
∑ y∈Y 
q(y;β)gβ(z∗i (y;β)), 
(8.13) where q(y;β) , eλφγ(xi,y;β)/ 
(∑ y′∈Y e 
λφγ(xi,y′;β) ) . 
Using Theorem 8.1.3, we can apply SGD to solve (8.9), or equivalently, the SSDRO model (8.8). This is summarized in Algorithm 3. Najafi et al., 2019 proved a convergence rate of O(T−1/2) for Algo-rithm 3, if we assume z∗i (β) and z∗i (y;β) can be computed exactly. Nonetheless, the optimality gap δ can be set infinitesimally small due to
216 Advanced Topics in Distributionally Robust Learning 
the strong concavity of (8.11) and (8.12) that is shown in Lemma 8.1.2. The parameters γ and λ can be tuned via cross-validation. 
Algorithm 3 Stochastic Gradient Descent for SSDRO. Inputs: D, γ, λ, k ≤ N, δ, α, T . Initialize: β ← β0, t← 0. for t = 0→ T − 1 do 
Randomly select index set I ⊆ JNK with size k. for i ∈ Il ∩ I do 
Compute a δ-approx of z∗i (βt) from (8.11). end for for (i, y) ∈ (Iul ∩ I)× Y do 
Compute a δ-approx of z∗i (y;βt) from (8.12). end for Compute the sub-gradient of R̂SSAR(βt;D) from (8.13). Update: βt+1 ← βt − α∇βR̂SSAR(βt;D). 
end for Output: β∗ ← βT . 
8.2 Distributionally Robust Reinforcement Learning 
So far in this monograph, we considered learning problems where the objective is to predict an output variable (or vector in the setting of Section 6). These learning problems were cast as distributionally robust single-period optimization problems. Even in the applications of Sec-tion 7 involving medical prescriptions, where we considered information from multiple past time periods to learn actions that optimize an outcome in the next time period, the resulting optimization problem was single-period. In this section, we will discuss multi-period optimization motivated by learning a policy for a Markov Decision Process (MDP). We will restrict ourselves to model-based settings, where there is an explicit model of how the MDP transitions from state to state under some policy, and seek to inject robustness into this transition model. The development follows the work in Derman and Mannor, 2020. 
We start by defining a discrete-time MDP. Consider an MDP with
8.2. Distributionally Robust Reinforcement Learning 217 
a finite state space S, a finite action space A, a deterministic reward function r : S × A → R, and a transition probability model p that, given a state s1 and an action a, determines the probability p(s2|s1, a) of landing to the next state s2. A policy π maps states to actions; specifically, π(a|s) denotes the probability of selecting action a in state s. The state of the MDP evolves dynamically as follows. Suppose that at time t the MDP is in state st. According to the policy π, it selects some action at, receives a reward r(st, at), and transitions to the next state st+1 with probability p(st+1|st, at). In an infinite-horizon discounted reward setting, the objective is to select a policy π that maximizes the expected total discounted reward 
Eτ∼πp 
[∑∞ t=0 
γtr(st, at) ] , 
where γ ∈ [0, 1) is the discount factor and τ ∼ π represents a random trajectory τ = (s0, a0, s1, a1, . . .) sampled by selecting the initial state s0 according to some probability distribution ρ0(·) ∈ P(S), sampling actions according to at ∼ π(·|st), and states according to st+1 ∼ p(·|st, at) (hence, the subscript p in the expectation to denote dependence on the transition model p). 
We can now define the state value, or reward-to-go function, which equals the future total discounted reward when starting from state s, namely, 
vπp (s) = Eτ∼πp 
[∑∞ t=0 
γtr(st, at) | s0 = s ] . 
The value function can be obtained as a solution to the following Bellman equation: 
v(s) = T πp v(s) 4= ∑ 
a∈A π(a|s) 
( r(s, a) + γ 
∑ q∈S 
p(q|s, a)v(q) ) . 
The operator T πp satisfies a contraction property with respect to the sup-norm, implying that the Bellman equation has a unique fixed point denoted by vπp (s). This can for instance be obtained by successive application of T πp to some arbitrary initial solution – a method known as value iteration.
218 Advanced Topics in Distributionally Robust Learning 
8.2.1 Deterministically Robust Policies 
A number of results in the literature examined how to introduce robustness with respect to uncertainty on the transition probability model, starting with Satia and Lave Jr, 1973; White III and Eldeib, 1994 and Bagnell et al., 2001. A more complete theory of robust dynamic programming has been developed in Iyengar, 2005 and Nilim and Ghaoui, 2005. In this work, the transition probability vector ps,a = (p(q|s, a); q ∈ S) at any state-action pair (s, a) belongs to some ambiguity or uncertainty set Us,a ⊆ P(S). It is assumed that every time a state-action pair (s, a) is encountered, a potentially different measure ps,a ∈ Us,a could be applied; this has been termed the rectangularity assumption in Iyengar, 2005. 
In this robust setting, one can define a robust value function as the worst-case value function over the uncertainty set, that is, 
vπU (s) = inf p∈U 
Eτ∼πp 
[∑∞ t=0 
γtr(st, at) | s0 = s ] , (8.14) 
where the uncertainty set U is the cartesian product of the transition probability uncertainty sets encountered throughout the trajectory, i.e., U = ∏∞ 
t=0 Ust,at . Iyengar, 2005 and Nilim and Ghaoui, 2005 show that a robust 
Bellman equation can be written as: 
v(s) =T πU v(s) (8.15) 4= ∑ 
a∈A π(a|s) 
( r(s, a) + γ inf 
ps,a∈Us,a 
∑ q∈S 
p(q|s, a)v(q) ) . 
As with the non-robust case, the operator T πU satisfies a contraction property, implying that the robust Bellman equation has a unique fixed point which can be computed by successive application of T πU . 
8.2.2 Distributionally Robust Policies 
Distributionally robust MDPs can be thought of as a generalization of deterministically robust MDPs. Instead of selecting transition probabilities out of the ambiguity set U defined earlier, we can view the transition probability model as being sampled according to some distribution µ ∈ M ⊆ P(U), i.e., µ is the probability distribution of the
8.2. Distributionally Robust Reinforcement Learning 219 
transition probability model p. Making the same rectangularity assumption as before, that is, requiring that µ is a product of independent distributions over Us,a, we can define a distributionally robust value function similarly to (8.14) as: 
vπM(s) = inf µ∈M 
Eτ∼πp∼µ 
[∑∞ t=0 
γtr(st, at) | s0 = s ] . (8.16) 
Derman and Mannor, 2020 introduces Wasserstein distributionally robust MDPs by defining the set of distributionsM as a Wasserstein ball around some nominal distribution. More specifically, for any stateaction pair (s, a), let µ̂s,a ∈ P(Us,a) be some nominal distribution over Us,a. For any distribution µs,a ∈ P(Us,a), define the order-1 Wasserstein distance induced by some norm ‖ · ‖, and denote it by W1(µ̂s,a, µs,a). A Wasserstein ball around the nominal distribution can be defined as: 
Ωεs,a(µ̂s,a) = {µs,a ∈ P(Us,a) : W1(µ̂s,a, µs,a) ≤ εs,a} . (8.17) 
Under a rectangularity assumption as in Sec. 8.2.1, we define the cartesian product of the sets Ωεs,a(µ̂s,a) over all state-action pairs and denote it by Ωε(µ̂) = ∏ 
(s,a)∈S×AΩεs,a(µ̂s,a), where ε is a vector defined as ε = (εs,a; (s, a) ∈ S ×A), and µ̂ = ∏ 
(s,a)∈S×A µ̂s,a. Analogously to (8.15), the distributionally robust Bellman equation 
can be written as: 
v(s) =T πΩε(µ̂)v(s) (8.18) 4= ∑ 
a∈A π(a|s) 
( r(s, a) 
+ γ inf µs,a∈Ωεs,a (µ̂s,a) 
∫ ps,a∈Us,a 
∑ q∈S 
p(q|s, a)v(q)dµs,a(ps,a) ) . 
The operator T πΩε(µ̂) satisfies a contraction property with respect to the sup-norm, implying that the Bellman equation has a unique fixed point denoted by vπΩε(µ̂)(s). To find an optimal policy, consider the operator 
TΩε(µ̂) = sup π(·|s)∈P(A) 
T πΩε(µ̂). (8.19) 
As shown in Derman and Mannor, 2020; Chen et al., 2019b, there exists a distributionally robust optimal policy π∗ and a unique value function
220 Advanced Topics in Distributionally Robust Learning 
v∗Ωε(µ̂)(s) which is a fixed point of the operator defined by (8.19). In particular, for every s ∈ S, 
v∗Ωε(µ̂)(s) = sup π 
inf µ∈Ωε(µ̂) 
Eτ∼πp∼µ 
[∑∞ t=0 
γtr(st, at) | s0 = s ] 
= vπ ∗ 
Ωε(µ̂)(s). 
The optimal value function can be obtained by value iteration, i.e., successive application of TΩε(µ̂) to some arbitrary initial value function. 
Selecting a Nominal Distribution 
The nominal distribution µ̂ that serves as the center of the Wasserstein balls in (8.17) can be determined as the empirical distribution computed from a set of different independent episodes of the MDP. Suppose we have in our disposal n such episodes. Then, for each episode i ∈ JnK, and using the observed sequence of states and actions during the episode, we can compute the empirical transition probability p̂(i)(q|s, a) of transitioning into state q when applying action a in state s. The resulting empirical distribution µ̂ns,a assigns mass 1/n to each p̂(i)(·|s, a), namely, 
µ̂ns,a = 1 n 
∑n 
i=1 δp̂(i)(·|s,a), 
where δp̂(i)(·|s,a) is a Dirac function assigning mass 1 to the model p̂(i)(·|s, a). Defining a product distribution for each episode i by δi =∏ 
(s,a)∈S×A δp̂(i)(·|s,a), we can define the empirical distribution 
µ̂n = 1 n 
∑n 
i=1 δi. 
The model above requires computing an empirical transition probability for each state-action pair. When the state-action space is very large, this is not practical. Instead, one can employ some approximation architecture. One possibility is to use an architecture of the following type 
p̂(i)(q|s, a) = exp{ξ′iψ(s, a, q)}∑ y∈S exp{ξ′iψ(s, a, y)} , 
for some vector of feature functions ψ(s, a, q) and a parameter vector ξi; the latter can be learned from the sequence of state-actions corresponding to episode i by solving a logistic regression problem.
8.2. Distributionally Robust Reinforcement Learning 221 
A Regularization Result for the Distributionally Robust MDP 
Derman and Mannor, 2020 obtains a regularization result for the Wasser-stein distributionally robust MDP that is analogous to the dual-norm regularization we obtained in Section 4. We will outline some of the key steps, referring the reader to Derman and Mannor, 2020 for the full details. The result obtains a lower bound on the value function vπΩε(µ̂n)(s). 
To that end, define first the conjugate robust value function at state s and under policy π. Specifically, let p = (p(q|s, a); ∀q, s ∈ S, a ∈ A) denote a vectorized form of the transition probability model. For any z = (z(q|s, a);∀q, s ∈ S, a ∈ A), we define the conjugate robust value function as 
v∗,πs (z) 4= inf p 
(vπp(s)− z′p), (8.20) 
and let Ds = {z : v∗,πs (z) > −∞} be its effective domain. Note that as defined, v∗,πs (z) is the negative of the convex conjugate of the value function as a function of p (Rockafellar, 1970). 
A key result from Derman and Mannor, 2020 is in the following theorem. As discussed earlier, suppose we have data from n episodes from the MDP and we have constructed the empirical transition probabilities for each episode. Let p̂(i) = (p̂(i)(q|s, a); ∀q, s ∈ S, a ∈ A) be the corresponding vector. 
Theorem 8.2.1. (Derman and Mannor, 2020) For any policy π, it holds that 
vπΩε(µ̂n)(s) ≥ 1 n 
∑n 
i=1 vπp̂(i)(s)− καs, 
where αs = ∑ a∈A π(a|s)εs,a, κ = supz∈Ds ‖z‖∗, and ‖ · ‖∗ is the dual 
norm to the norm used in defining the Wasserstein uncertainty set (cf. (8.17)). 
Proof. We will provide an outline of the key steps. We start by expressing
222 Advanced Topics in Distributionally Robust Learning 
vπΩε(µ̂n)(s) using the Bellman equation (8.18). We have 
vπΩε(µ̂n)(s) 
= ∑ 
a∈A π(a|s) 
( r(s, a) 
+ γ inf µs,a∈Ωεs,a (µ̂ns,a) 
∫ ps,a 
∑ q∈S 
p(q|s, a)v(q)dµs,a(ps,a) ) 
= ∑ 
a∈A π(a|s) 
( r(s, a) 
+ γ inf {µs,a:W1(µs,a,µ̂ns,a)≤εs,a} 
∫ ps,a 
∑ q∈S 
p(q|s, a)v(q)dµs,a(ps,a) ) 
= ∑ 
a∈A π(a|s) 
( r(s, a) 
+ γ inf µs,a 
sup λ≥0 
[ ∫ ps,a 
∑ q∈S 
p(q|s, a)v(q)dµs,a(ps,a) 
+ λW1(µs,a, µ̂ns,a)− λεs,a ]) 
≥ ∑ 
a∈A π(a|s) 
( r(s, a) 
+ γ sup λ≥0 
inf µs,a 
[ ∫ ps,a 
∑ q∈S 
p(q|s, a)v(q)dµs,a(ps,a) 
+ λW1(µs,a, µ̂ns,a)− λεs,a ]) , (8.21) 
where the last inequality used weak duality. Next, using the structure of µ̂n as an average over n episodes and 
the fact (due to the rectangularity assumption) that the empirical distribution is a product distribution over state-action pairs, we can deduce from (8.21) that 
vπΩε(µ̂n)(s) ≥ sup λ≥0 
[ 1 n 
∑n 
i=1 inf p 
(vπp(s) + λ‖p− p̂(i)‖)− λαs ] , (8.22) 
where αs = ∑ a∈A π(a|s)εs,a. This derivation used similar techniques as 
in Theorem 3.1.2.
8.2. Distributionally Robust Reinforcement Learning 223 
Using the definition of the dual norm and for any λ ≥ 0 we have 
λ‖p− p̂(i)‖ = max ‖zi‖∗≤1 
λz′i(p− p̂(i)) 
= max ‖λzi‖∗≤λ 
λz′i(p− p̂(i)) 
= max ‖ui‖∗≤λ 
u′i(p− p̂(i)). (8.23) 
Denote by νπs : p → vπp(s) the function that maps the transition probability vector p to the value function vπp(s). Let c̆l(νπs ) be its convex closure, i.e., the greatest closed and convex function upper bounded by νπs at any p. Since c̆l(νπs ) is a lower bound on vπp(s) and using (8.23) and (8.22) we obtain: 
vπΩε(µ̂n)(s) ≥ sup λ≥0 
[ 1 n 
∑n 
i=1 inf p 
max ‖ui‖∗≤λ 
(c̆l(νπs )(p) + u′i(p− p̂(i)))− λαs ] . 
(8.24) Using the fact that the convex closure of a function has the same 
convex dual as the function itself, it follows that 
c̆l(νπs )(p) =c̆l(νπs )∗∗(p) = max 
z∈Ds [z′p− c̆l(νπs )∗(z)] 
= max z∈Ds 
[z′p− (νπs )∗(z)] 
= max z∈Ds 
[z′p + v∗,πs (z)], (8.25) 
where the last equation used the definition of the conjugate robust value function (8.20). 
Then, using (8.25), the term inside the summation in the RHS of (8.24) can be written as: 
inf p 
max ‖ui‖∗≤λ 
(c̆l(νπs )(p) + u′i(p− p̂(i))) 
= inf p 
max zi∈Ds 
max ‖ui‖∗≤λ 
(v∗,πs (zi) + z′ip + u′i(p− p̂(i))) 
= max zi∈Ds 
max ‖ui‖∗≤λ 
[v∗,πs (zi)− u′ip̂(i) + inf p 
p′(zi + ui)], (8.26) 
where the last equality used duality. Note that the minimization in the RHS of the above is over transition probability vectors. We can
224 Advanced Topics in Distributionally Robust Learning 
relax this minimization over all real vectors, which would render a lower bound and result in the infimum being −∞ unless ui = −zi. Note that if sup{‖zi‖∗ : zi ∈ Ds} > λ, then one can pick some zi ∈ Ds such that ‖zi‖∗ > λ, in which case the inner minimization in (8.26) achieves −∞ since ui 6= −zi. When sup{‖zi‖∗ : zi ∈ Ds} ≤ λ, we have 
inf p 
max ‖ui‖∗≤λ 
(c̆l(νπs )(p) + u′i(p− p̂(i))) 
≥ max zi∈Ds 
max ‖zi‖∗≤λ 
[v∗,πs (zi) + z′ip̂(i)] 
=vπp̂(i)(s), 
where the second step follows from the fact that v∗,πs (zi) is the negative of the convex dual of the value function. It follows that 
inf p 
max ‖ui‖∗≤λ 
(c̆l(νπs )(p) + u′i(p− p̂(i))) 
≥ 
vπp̂(i)(s), if sup{‖zi‖∗ : zi ∈ Ds} ≤ λ, −∞, otherwise. 
(8.27) 
Plugging (8.27) in (8.24) it follows that 
vπΩε(µ̂n)(s) ≥ 1 n 
∑n 
i=1 vπp̂(i)(s)− καs, 
where κ = supz∈Ds ‖z‖∗. 
The result of Theorem 8.2.1 provides a lower bound on the distributionally robust value function, which can be used in the RHS of the Bellman equation and in a value iteration scheme. It can also be used in the same manner in obtaining a distributionally robust optimal policy. However, this strategy is applicable in settings where the state-action space is relatively small. For large state-action spaces, one typically approximates either the value function or the policy. To that end, the regularization result Theorem 8.2.1 can be extended to cases where the value function is approximated by a linear function. 
In particular, suppose we approximate the value function by vπp(s) ≈ φ(s)′wp, where φ(s) is some feature vector and wp a parameter vector. Similar to (8.20) we can define an approximate conjugate robust value
8.2. Distributionally Robust Reinforcement Learning 225 
function at state s and under policy π as: 
w∗,πs (z) 4= inf p 
(φ(s)′wp − z′p), (8.28) 
and let Ws = {z : w∗,πs (z) > −∞} be its effective domain. Derman and Mannor, 2020 provides a result analogous to Theo-
rem 8.2.1. 
Theorem 8.2.2. (Derman and Mannor, 2020) For any policy π, it holds that 
inf µ∈Ωε(µ̂n) 
Eτ∼πp∼µ [φ(s)′wp] ≥ 1 n 
∑n 
i=1 φ(s)′wp̂(i) − ηαs, (8.29) 
where αs = ∑ a∈A π(a|s)εs,a and η = supz∈Ws 
‖z‖∗.
9 
Discussion and Conclusions 
In this monograph, we developed a Wasserstein-based distributionally robust learning framework for a comprehensive list of predictive and prescriptive problems, including (i) Distributionally Robust Lin-ear Regression (DRLR), (ii) Groupwise Wasserstein Grouped LASSO (GWGL), (iii) Distributionally Robust Multi-Output Learning, (iv) Optimal decision making via DRLR informed K-Nearest Neighbors (K-NN), (v) Distributionally Robust Semi-Supervised Learning, and (vi) Distributionally Robust Reinforcement Learning. 
Starting with the basics of the Wasserstein metric and the DRO formulation, we explored its robustness inducing properties, discussed approaches for solving the DRO formulation, and investigated the properties of the DRO solution. Then, we turned our attention into specific learning problems that can be posed and solved using the Wasserstein DRO approach. In each case, we derived equivalent regularized empirical loss minimization formulations and established the robustness of the solutions both theoretically and empirically. We showed novel theoretical results tailored to each setting and validated the methods using real world medical applications, strengthening the notion of robustness through these discussions. 
226
227 
The robustness of the Wasserstein DRO approach hinges on the fact that a family of distributions that are different from, but close to the empirical measure, are being hedged against. This data-driven formulation not only utilizes the information contained in the observed samples, but also generalizes beyond that by allowing distributions with out-of-sample support. This is a distinguishing feature from DRO approaches based on alternative distance functions, such as φ-divergences, which only consider distributions whose support is a subset of the observed samples. Such a limitation could potentially hurt the generalization power of the model. Another salient advantage of the Wasserstein metric lies in its structure, in particular, encoding a distance metric in the data space, which makes it possible to link the form of the regularizer with the growth rate of the loss function and establish a connection between robustness and regularization. 
Our results on Wasserstein DRO and its connection to regularization are not restricted to linear and logistic regression. From the analysis presented in Section 3, we see that as long as the growth rate of the loss function is bounded, the corresponding Wasserstein DRO problem can be made tractable. We consider both static settings, where all the samples are readily accessible when solving for the model (Sections 4, 5, 6), and a dynamic setting where the samples come in a sequential manner (Section 8.2). Another example of a dynamic DRO problem is Abadeh et al., 2018, which proposed a distributionally robust Kalman filter that hedges against model risk; in that setting, the Wasserstein ambiguity set contains only normal distributions. 
More broadly, researchers have proposed distributionally robust versions for general estimation problems, see, for example, Nguyen et al., 2019 for distributionally robust Minimum Mean Square Error Estimation, Nguyen et al., 2018 for distributionally robust Maximum Likelihood Estimation, which was adopted to estimate the inverse covariance matrix of a Gaussian random vector. We refer the reader to Peyré and Cuturi, 2019 for computational aspects related to Wasserstein distances and optimal transport. Kuhn et al., 2019 and Rahimian and Mehrotra, 2019 also provided nice overviews of DRO, the former focusing specifically on the Wasserstein DRO, covering in detail the theoretical aspects of the general formulation with a brief discussion
228 Discussion and Conclusions 
on some machine learning applications, while the latter covered DRO models with all kinds of ambiguity sets. We summarize our key novel contributions as follows. 
 We considered a comprehensive list of machine learning problems, not only predictive models, but also prescriptive models, that can be posed and solved using the Wasserstein DRO framework. 
 We presented novel performance guarantees tailored to each problem, reflecting the particularity of the specific problem and providing justifications for using a Wasserstein DRO approach. This is very different from Kuhn et al., 2019, where a universal performance guarantee result was derived. Their result is in general applicable to every single DRO problem, but may miss the individual characteristics of the problem at hand. 
 The Wasserstein prescriptive model we presented in Section 7 is novel. We showed the power of Wasserstein DRO through the K-NN insertion in a decision making problem, and demonstrated the benefit of robustness through a novel out-of-sample MSE result. 
 The non-trivial extension to multi-output DRO has implications on training robust neural networks, e.g., the robustness of the multiclass logistic regression classifier to optimized perturbations that are designed to fool the classifier, see Section 6.2.3. 
 Finally, we considered a variety of synthetic and real world case studies of the respective models, demonstrating the applications of the DRO framework and its superior performance compared to other alternatives, which adds to the accessibility and appeal of this work to an application-oriented reader.
Acknowledgements 
The authors are grateful to Dimitris Bertsimas, Theodora Brisimi, Chris-tos Cassandras, David Castañón, Alex Olshevsky, Venkatesh Saligrama, and Wei Shi, for their insightful comments and constructive suggestions. 
We are thankful to the Network Optimization and Control Lab at Boston University for providing computational resources and expertise for some of the case studies. Collaborations on a number of application fronts have involved Michael Caramanis and Pirooz Vakili. 
We are grateful to many clinicians and researchers in Boston area hospitals who provided access to data and collaborated in parts of the work, including: Hiroto Hatabu, George Kasotakis, Fania Mela, Rebecca Mishuris, Jenifer Siegelman, Vladimir Valtchinov, and George Velmahos. Particular mention is due to Bill Adams, at Boston Medical Center, whose efforts to make data available for research have been nothing short of extraordinary and who was instrumental in engaging the authors in health analytics research. 
We are thankful to the series editors Garud Iyengar, Stephen Boyd, and to the anonymous reviewers for valuable feedback. 
RC is grateful to ICP and David Castañón who have provided constant support and encouragement for her, and have been inspirational role models as excellent researchers and teachers with endless positivity and passion. She is also grateful to her parents, Xudong and Shouzhen, and her cousins Yingying, Qianqian, and Chunlei, for their unconditional 
229
230 Acknowledgements 
love, support and company, which have given her the strength and determination to overcome difficulties and complete this work. 
ICP is grateful to Dimitris Bertsimas and John Tsitsiklis for all they have taught him and for being such inspirational role models for research and the good exposition of research ideas. He is also grateful to his family (Gina, Aris, Phevos, and Alexandros) for their love, support, and giving him the time to work on this project. 
The authors are also grateful to Ulrike Fischer, who designed the style files, and Neal Parikh, who laid the groundwork for these style files. 
Part of the research included in this monograph has been supported by the NSF under grants IIS-1914792, DMS-1664644, CNS-1645681, CCF-1527292, and IIS-1237022, by the ARO under grant W911NF-12-1-0390, by the ONR under grant N00014-19-1-2571, by the NIH under grants R01 GM135930 and UL54 TR004130, by the DOE under grant DE-AR-0001282, by the Clinical & Translational Science Institute at Boston University, by the Boston University Digital Health Initiative and the Center for Information and Systems Engineering, and by the joint Boston University and Brigham & Women’s Hospital program in Engineering and Radiology.
References 
Abadeh, S. S., P. M. M. Esfahani, and D. Kuhn. 2015. “Distributionally robust logistic regression”. In: Advances in Neural Information Processing Systems. 1576–1584. 
Abadeh, S. S., V. A. Nguyen, D. Kuhn, and P. M. M. Esfahani. 2018. “Wasserstein distributionally robust Kalman filtering”. In: Advances in Neural Information Processing Systems. 8474–8483. 
Agarwal, A., D. Hsu, S. Kale, J. Langford, L. Li, and R. Schapire. 2014. “Taming the monster: A fast and simple algorithm for contextual bandits”. In: International Conference on Machine Learning. 1638– 1646. 
Alayrac, J.-B., J. Uesato, P.-S. Huang, A. Fawzi, R. Stanforth, and P. Kohli. 2019. “Are labels required for improving adversarial robustness?” In: Advances in Neural Information Processing Systems. 12214–12223. 
Altman, N. S. 1992. “An introduction to kernel and nearest-neighbor nonparametric regression”. The American Statistician. 46(3): 175– 185. 
Aly, M. 2005. “Survey on multiclass classification methods”. Neural Networks. 19: 1–9. 
Bagnell, J., A. Y. Ng, and J. Schneider. 2001. “Solving uncertain Markov decision problems”. Robotics Institute, Carnegie Mellon University, Pittsburgh, PA, Tech. Rep. CMU-RI-TR-01-25. 
231
232 References 
Bakin, S. 1999. “Adaptive regression and model selection in data mining problems”. PhD thesis. The Australian National University. 
Bartlett, P. L. and S. Mendelson. 2002. “Rademacher and Gaussian complexities: risk bounds and structural results”. Journal of Machine Learning Research. 3: 463–482. 
Bastani, H. and M. Bayati. 2020. “Online decision making with highdimensional covariates”. Operations Research. 68(1): 276–294. 
Bay, S. D. 1998. “Combining nearest neighbor classifiers through multiple feature subsets”. In: International Conference on Machine Learning. Vol. 98. 37–45. 
Bayraksan, G. and D. K. Love. 2015. “Data-driven stochastic programming using phi-divergences”. Tutorials in Operations Research: 1– 19. 
Ben-Tal, A., L. El Ghaoui, and A. Nemirovski. 2009. Robust optimization. Vol. 28. Princeton University Press. 
Ben-Tal, A. and A. Nemirovski. 2008. “Selected topics in robust convex optimization”. Mathematical Programming. 112(1): 125–158. 
Bertsekas, D. P. 1999. Nonlinear programming. Athena Scientific Bel-mont. 
Bertsimas, D. and J. Tsitsiklis. 1997. Introduction to linear optimization. Belmont, MA: Athena Scientific. 
Bertsimas, D., D. B. Brown, and C. Caramanis. 2011. “Theory and applications of robust optimization”. SIAM Review. 53(3): 464–501. 
Bertsimas, D. and M. S. Copenhaver. 2018. “Characterization of the equivalence of robustification and regularization in linear and matrix regression”. European Journal of Operational Research. 270(3): 931–942. 
Bertsimas, D., J. Dunn, and N. Mundru. 2019a. “Optimal prescriptive trees”. INFORMS Journal on Optimization. 1(2): 91–183. 
Bertsimas, D., J. Dunn, and N. Mundru. 2019b. “Optimal prescriptive trees”. INFORMS Journal on Optimization. 1(2): 91–183. 
Bertsimas, D., J. Dunn, C. Pawlowski, and Y. D. Zhuo. 2018. “Robust classification”. INFORMS Journal on Optimization. 1(1): 2–34. 
Bertsimas, D., V. Gupta, and I. C. Paschalidis. 2015. “Data-driven estimation in equilibrium using inverse optimization”.Mathematical Programming. 153(2): 595–633.
References 233 
Bertsimas, D. and N. Kallus. 2019. “From predictive to prescriptive analytics”. Management Science. doi: 10.1287/mnsc.2018.3253. 
Bertsimas, D., N. Kallus, A. M. Weinstein, and Y. D. Zhuo. 2017. “Per-sonalized diabetes management using electronic medical records”. Diabetes Care. 40(2): 210–217. 
Bertsimas, D. and A. King. 2017. “Logistic regression: From art to science”. Statistical Science. 32(3): 367–384. 
Bertsimas, D. and C. McCord. 2018. “Optimization over continuous and multi-dimensional decisions with observational data”. arXiv preprint arXiv:1807.04183. 
Bertsimas, D. and B. Van Parys. 2017. “Bootstrap robust prescriptive analytics”. arXiv preprint arXiv:1711.09974. 
Biggs, M. and R. Hariss. 2018. “Optimizing objective functions determined from random forests”. Available at SSRN 2986630. 
Bishop, C. M. 1995. Neural networks for pattern recognition. Oxford University Press. 
Blanchet, J., P. W. Glynn, J. Yan, and Z. Zhou. 2019a. “Multivariate distributionally robust convex regression under absolute error loss”. arXiv preprint arXiv:1905.12231. 
Blanchet, J. and Y. Kang. 2017a. “Distributionally robust groupwise regularization estimator”. arXiv preprint arXiv:1705.04241. 
Blanchet, J. and Y. Kang. 2017b. “Distributionally robust semi-supervised learning”. arXiv preprint arXiv:1702.08848. 
Blanchet, J., Y. Kang, and K. Murthy. 2019b. “Robust Wasserstein profile inference and applications to machine learning”. Journal of Applied Probability. 56(3): 830–857. 
Blanchet, J., Y. Kang, K. Murthy, and F. Zhang. 2019c. “Data-driven optimal transport cost selection for distributionally robust optimization”. In: 2019 Winter Simulation Conference (WSC). IEEE. 3740–3751. 
Blanchet, J. and K. Murthy. 2019. “Quantifying distributional model risk via optimal transport”. Mathematics of Operations Research. 44(2): 565–600. 
Bonneel, N., J. Rabin, G. Peyré, and H. Pfister. 2015. “Sliced and Radon Wasserstein barycenters of measures”. Journal of Mathematical Imaging and Vision. 51(1): 22–45.
234 References 
Bootkrajang, J. and A. Kabán. 2012. “Label-noise robust logistic regression and its applications”. In: Joint European Conference on Machine Learning and Knowledge Discovery in Databases. 143–158. 
Borel, M. É. 1909. “Les probabilités dénombrables et leurs applications arithmétiques”. Rendiconti del Circolo Matematico di Palermo (1884-1940). 27(1): 247–271. 
Bravo, F. and Y. Shaposhnik. 2018. “Mining optimal policies: A pattern recognition approach to model analysis”. Available at SSRN 3069690. 
Breiman, L. 2001. “Random forests”. Machine Learning. 45(1): 5–32. Breiman, L. 2017. Classification and regression trees. Routledge. Breiman, L. and J. H. Friedman. 1997. “Predicting multivariate re-
sponses in multiple linear regression”. Journal of the Royal Statis-tical Society: Series B (Statistical Methodology). 59(1): 3–54. 
Brown, P. J., J. V. Zidek, et al. 1980. “Adaptive multivariate ridge regression”. The Annals of Statistics. 8(1): 64–74. 
Bunea, F., J. Lederer, and Y. She. 2014. “The group square-root LASSO: Theoretical properties and fast algorithms”. IEEE Transactions on Information Theory. 60(2): 1313–1325. 
Cantelli, F. P. 1917. “Sulla probabilità come limite della frequenza”. Atti Accad. Naz. Lincei. 26(1): 39–45. 
Carmon, Y., A. Raghunathan, L. Schmidt, J. C. Duchi, and P. S. Liang. 2019. “Unlabeled data improves adversarial robustness”. In: Advances in Neural Information Processing Systems. 11192–11203. 
Chen, R. and I. C. Paschalidis. 2018. “A robust learning approach for regression models based on distributionally robust optimization”. The Journal of Machine Learning Research. 19(1): 517–564. 
Chen, R., I. C. Paschalidis, H. Hatabu, V. I. Valtchinov, and J. Siegel-man. 2019a. “Detection of unwarranted CT radiation exposure from patient and imaging protocol meta-data using regularized regression”. European Journal of Radiology Open. 6: 206–211. 
Chen, S. and A. Banerjee. 2016. “Alternating estimation for structured high-dimensional multi-response models”. arXiv preprint arXiv:1606.08957.
References 235 
Chen, T. and C. Guestrin. 2016. “Xgboost: A scalable tree boosting system”. In: Proceedings of the 22nd ACM SigKDD International Conference on Knowledge Discovery and Data Mining. 785–794. 
Chen, Z., P. Yu, and W. B. Haskell. 2019b. “Distributionally robust optimization for sequential decision-making”. Optimization. 68(12): 2397–2426. 
Chu, W., L. Li, L. Reyzin, and R. Schapire. 2011. “Contextual bandits with linear payoff functions”. In: Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics. 208–214. 
Cleveland, W. S. and S. J. Devlin. 1988. “Locally weighted regression: an approach to regression analysis by local fitting”. Journal of the American statistical association. 83(403): 596–610. 
Coleman, D., P. Holland, N. Kaden, V. Klema, and S. C. Peters. 1980. “A system of subroutines for iteratively reweighted least squares computations”. ACM Transactions on Mathematical Software (TOMS). 6(3): 327–336. 
Cortes, C. and V. Vapnik. 1995. “Support-vector networks”. Machine learning. 20(3): 273–297. 
Delage, E. and Y. Ye. 2010. “Distributionally robust optimization under moment uncertainty with application to data-driven problems”. Operations Research. 58(3): 595–612. 
Delon, J. and A. Desolneux. 2020. “A Wasserstein-type distance in the space of Gaussian mixture models”. SIAM Journal on Imaging Sciences. 13(2): 936–970. 
Den Hertog, D. and K. Postek. 2016. “Bridging the gap between predictive and prescriptive analytics-new optimization methodology needed”. Tech. rep. Technical report, Tilburg University, Nether-lands, 2016. Available at: http://www.optimization-online.org/ DB_HTML/2016/12/5779.html. 
Derman, E. and S. Mannor. 2020. “Distributional robustness and regularization in reinforcement learning”. arXiv preprint arXiv:2003.02894. 
Ding, C. 2004. “A tutorial on spectral clustering”. In: Talk presented at International Conference on Machine Learning.
236 References 
Ding, N., S. Vishwanathan, M. Warmuth, and V. S. Denchev. 2013. “T-logistic regression for binary and multiclass classification”. The Journal of Machine Learning Research. 5: 1–55. 
Dowson, D. and B. Landau. 1982. “The Fréchet distance between multivariate normal distributions”. Journal of multivariate analysis. 12(3): 450–455. 
Dunn, J. 2018. “Optimal trees for prediction and prescription”. PhD thesis. Massachusetts Institute of Technology. 
Duque, D. and D. P. Morton. 2020. “Distributionally robust stochastic dual dynamic programming”. SIAM Journal on Optimization. 30(4): 2841–2865. 
El Ghaoui, L., G. R. G. Lanckriet, and G. Natsoulis. 2003. “Robust classification with interval data”. Tech. rep. No. UCB/CSD-03-1279. EECS Department, University of California, Berkeley. url: http://www2.eecs.berkeley.edu/Pubs/TechRpts/2003/5772.html. 
El Ghaoui, L. and H. Lebret. 1997. “Robust solutions to least-squares problems with uncertain data”. SIAM Journal on Matrix Analysis and Applications. 18(4): 1035–1064. 
Erdoğan, E. and G. Iyengar. 2006. “Ambiguous chance constrained problems and robust optimization”. Mathematical Programming. 107(1-2): 37–61. 
Esfahani, P. M. and D. Kuhn. 2018. “Data-driven distributionally robust optimization using the Wasserstein metric: Performance guarantees and tractable reformulations”. Mathematical Programming. 171(1-2): 115–166. 
Esfahani, P. M., S. Shafieezadeh-Abadeh, G. A. Hanasusanto, and D. Kuhn. 2018. “Data-driven inverse optimization with imperfect information”. Mathematical Programming. 167(1): 191–234. 
Fair, R. C. 1974. “On the robust estimation of econometric models”. In: Annals of Economic and Social Measurement. Vol. 3. No. 4. 667–677. 
Fathony, R., A. Rezaei, M. A. Bashiri, X. Zhang, and B. Ziebart. 2018. “Distributionally robust graphical models”. In: Advances in Neural Information Processing Systems. 8344–8355.
References 237 
Feng, J., H. Xu, S. Mannor, and S. Yan. 2014. “Robust logistic regression and classification”. In: Advances in Neural Information Processing Systems. 253–261. 
Forman, G. 2003. “An extensive empirical study of feature selection metrics for text classification”. Journal of Machine Learning Research. 3(Mar): 1289–1305. 
Fournier, N. and A. Guillin. 2015. “On the rate of convergence in Wasserstein distance of the empirical measure”. Probability Theory and Related Fields. 162(3-4): 707–738. 
Friedman, J., T. Hastie, and R. Tibshirani. 2001. The elements of statistical learning. Vol. 1. Springer series in statistics New York. 
Friston, K. J., A. P. Holmes, K. J. Worsley, J.-P. Poline, C. D. Frith, and R. S. Frackowiak. 1994. “Statistical parametric maps in functional imaging: a general linear approach”. Human Brain Mapping. 2(4): 189–210. 
Frogner, C., S. Claici, E. Chien, and J. Solomon. 2019. “Incorporating unlabeled data into distributionally robust learning”. arXiv preprint arXiv:1912.07729. 
Gao, R., X. Chen, and A. J. Kleywegt. 2017. “Wasserstein distributional robustness and regularization in statistical learning”. arXiv preprint arXiv:1712.06050. 
Gao, R. and A. J. Kleywegt. 2016. “Distributionally robust stochastic optimization with Wasserstein distance”. arXiv. 1604. 02199. 
Gao, R., L. Xie, Y. Xie, and H. Xu. 2018. “Robust hypothesis testing using Wasserstein uncertainty sets”. In: Advances in Neural Information Processing Systems. 7902–7912. 
Goh, J. and M. Sim. 2010. “Distributionally robust optimization and its tractable approximations”. Operations Research. 58(4-part-1): 902–917. 
Goodfellow, I., Y. Bengio, A. Courville, and Y. Bengio. 2016. Deep learning. Vol. 1. MIT press Cambridge. 
Haitovsky, Y. 1987. “On multivariate ridge regression”. Biometrika. 74(3): 563–570. 
Hanasusanto, G. A. and D. Kuhn. 2018. “Conic programming reformulations of two-stage distributionally robust linear programs over Wasserstein balls”. Operations Research. 66(3): 849–869.
238 References 
Hanasusanto, G. A. and D. Kuhn. 2013. “Robust data-driven dynamic programming”. In: Advances in Neural Information Processing Systems. 827–835. 
Hastie, T., R. Tibshirani, and R. J. Tibshirani. 2017. “Extended comparisons of best subset selection, forward stepwise selection, and the LASSO”. arXiv preprint arXiv:1707.08692. 
Hazan, E. 2016. “Introduction to online convex optimization”. Founda-tions and Trends® in Optimization. 2(3-4): 157–325. 
Hidalgo, B. and M. Goodman. 2013. “Multivariate or multivariable regression?” American Journal of Public Health. 103(1): 39–40. 
Hinich, M. J. and P. P. Talwar. 1975. “A simple method for robust regression”. Journal of the American Statistical Association. 70(349): 113–119. 
Hoerl, A. E. and R. W. Kennard. 1970. “Ridge regression: Biased estimation for nonorthogonal problems”. Technometrics. 12(1): 55– 67. 
Hu, W., G. Niu, I. Sato, and M. Sugiyama. 2016. “Does distributionally robust supervised learning give robust classifiers?” arXiv preprint arXiv:1611.02041. 
Hu, Z. and L. J. Hong. 2013. “Kullback-Leibler divergence constrained distributionally robust optimization”. Available at Optimization Online. 
Huber, P. J. 1964. “Robust estimation of a location parameter”. The Annals of Mathematical Statistics. 35(1): 73–101. 
Huber, P. J. 1973. “Robust regression: asymptotics, conjectures and Monte Carlo”. The Annals of Statistics. 1(5): 799–821. 
Islam, F., M. Shahbaz, A. U. Ahmed, and M. M. Alam. 2013. “Finan-cial development and energy consumption nexus in Malaysia: a multivariate time series analysis”. Economic Modelling. 30: 435– 441. 
Iyengar, G. 2005. “Robust dynamic programming”. Math. Operations Research. 30(2): 1–21. 
Izenman, A. J. 1975. “Reduced-rank regression for the multivariate linear model”. Journal of Multivariate Analysis. 5(2): 248–264.
References 239 
Jacob, L., G. Obozinski, and J.-P. Vert. 2009. “Group LASSO with overlap and graph LASSO”. In: International Conference on Machine Learning. 433–440. 
Jenatton, R., J.-Y. Audibert, and F. Bach. 2011. “Structured variable selection with sparsity-inducing norms”. Journal of Machine Learning Research. 12(Oct): 2777–2824. 
Ji, R. and M. Lejeune. 2018. “Data-driven optimization of reward-risk ratio measures”. Available at SSRN 2707122. 
Ji, R. and M. Lejeune. 2020. “Data-driven distributionally robust chanceconstrained optimization with Wasserstein metric”. Available at SSRN 3201356. 
Jiang, R. and Y. Guan. 2015. “Data-driven chance constrained stochastic program”. Mathematical Programming: 1–37. 
Jiang, R. and Y. Guan. 2018. “Risk-averse two-stage stochastic program with distributional ambiguity”. Operations Research. 66(5): 1390– 1405. 
Kantorovich, L. 1942. “On the transfer of masses (in Russian)”. In: Doklady Akademii Nauk. Vol. 37. No. 2. 227–229. 
Kantorovich, L. V. 1940. “On one effective method of solving certain classes of extremal problems”. In: Dokl. Akad. Nauk. USSR. Vol. 28. 212–215. 
Kantorovich, L. V. 1960. “Mathematical methods of organizing and planning production”. Management science. 6(4): 366–422. 
Kantorovich, L. 1939. “Mathematical methods of organizing production planning”. Leningrad: Leningrad State University. 
Kantorovich, L. 1948. “On the Monge problem”. Uspekhi Mat. Nauk. 3(2): 225–226. 
Kim, Y., J. Kim, and Y. Kim. 2006. “Blockwise sparse regression”. Statistica Sinica: 375–390. 
Kuhn, D., P. M. Esfahani, V. A. Nguyen, and S. Shafieezadeh-Abadeh. 2019. “Wasserstein distributionally robust optimization: Theory and applications in machine learning”. In: Operations Research & Management Science in the Age of Analytics. INFORMS. 130–166. 
Kumar, S., J. Ghosh, and M. M. Crawford. 2002. “Hierarchical fusion of multiple classifiers for hyperspectral data analysis”. Pattern Analysis & Applications. 5(2): 210–220.
240 References 
Li, T., C. Zhang, and M. Ogihara. 2004. “A comparative study of feature selection and multiclass classification methods for tissue classification based on gene expression”. Bioinformatics. 20(15): 2429–2437. 
Lin, Y. and H. H. Zhang. 2006. “Component selection and smoothing in smoothing spline analysis of variance models”. Annals of Statistics. 34(5): 2272–2297. 
Liu, A. and B. Ziebart. 2014. “Robust classification under sample selection bias”. In: Advances in Neural Information Processing Systems. 37–45. 
Liutkus, A., U. Simsekli, S. Majewski, A. Durmus, and F.-R. Stöter. 2019. “Sliced-Wasserstein flows: Nonparametric generative modeling via optimal transport and diffusions”. In: International Conference on Machine Learning. 4104–4113. 
Luo, F. and S. Mehrotra. 2017. “Decomposition algorithm for distributionally robust optimization using Wasserstein metric”. arXiv preprint arXiv:1704.03920. 
Ma, S., X. Song, and J. Huang. 2007. “Supervised group LASSO with applications to microarray data analysis”. BMC Bioinformatics. 8(1): 60. 
Masnadi-Shirazi, H., V. Mahadevan, and N. Vasconcelos. 2010. “On the design of robust classifiers for computer vision”. In: IEEE Computer Society Conference on Computer Vision and Pattern Recognition. 779–786. 
Massy, W. F. 1965. “Principal components regression in exploratory statistical research”. Journal of the American Statistical Association. 60(309): 234–256. 
Maurer, A., M. Pontil, and B. Romera-Paredes. 2014. “An inequality with applications to structured sparsity and multitask dictionary learning”. In: Conference on Computational Learning Theory. 440– 460. 
Mehrotra, S. and H. Zhang. 2014. “Models and algorithms for distributionally robust least squares problems”.Mathematical Programming. 146(1-2): 123–141.
References 241 
Meier, L., S. Van De Geer, and P. Bühlmann. 2008. “The group LASSO for logistic regression”. Journal of the Royal Statistical Society: Series B (Statistical Methodology). 70(1): 53–71. 
Meila, M. and J. Shi. 2001. “Learning segmentation by random walks”. In: Advances in Neural Information Processing Systems. 873–879. 
Mendelson, S., A. Pajor, and N. Tomczak-Jaegermann. 2007. “Recon-struction and sub-Gaussian operators in asymptotic geometric analysis”. Geometric and Functional Analysis. 17(4): 1248–1282. 
Mevissen, M., E. Ragnoli, and J. Y. Yu. 2013. “Data-driven distributionally robust polynomial optimization”. In: Advances in Neural Information Processing Systems. 37–45. 
Monge, G. 1781. “Mémoire sur la théorie des déblais et des remblais”. Histoire de l’Académie Royale des Sciences de Paris. 
Najafi, A., S.-i. Maeda, M. Koyama, and T. Miyato. 2019. “Robustness to adversarial perturbations in learning from incomplete data”. In: Advances in Neural Information Processing Systems. 5541–5551. 
Ng, A. Y., M. I. Jordan, and Y. Weiss. 2002. “On spectral clustering: Analysis and an algorithm”. In: Advances in Neural Information Processing Systems. 849–856. 
Nguyen, V. A., D. Kuhn, and P. M. Esfahani. 2018. “Distributionally robust inverse covariance estimation: The Wasserstein shrinkage estimator”. arXiv preprint arXiv:1805.07194. 
Nguyen, V. A., S. Shafieezadeh-Abadeh, D. Kuhn, and P. M. Esfahani. 2019. “Bridging Bayesian and minimax mean square error estimation via Wasserstein distributionally robust optimization”. arXiv preprint arXiv:1911.03539. 
Nilim, A. and L. E. Ghaoui. 2005. “Robust solutions to Markov decision problems with uncertain transition matrices”. Operations Research. 53(5): 780–798. 
Obozinski, G., L. Jacob, and J.-P. Vert. 2011. “Group LASSO with overlaps: the latent group LASSO approach”. arXiv: 1110. 0413. 
Peng, J., J. Zhu, A. Bergamaschi, W. Han, D.-Y. Noh, J. R. Pollack, and P. Wang. 2010. “Regularized multivariate regression for identifying master predictors with application to integrative genomics study of breast cancer”. The Annals of Applied Statistics. 4(1): 53.
242 References 
Peyré, G. and M. Cuturi. 2019. “Computational optimal transport: with applications to data science”. Foundations and Trends® in Machine Learning. 11(5-6): 355–607. 
Plath, N., M. Toussaint, and S. Nakajima. 2009. “Multi-class image segmentation using conditional random fields and global classification”. In: Proceedings of the 26th Annual International Conference on Machine Learning. 817–824. 
Pollard, D. 1991. “Asymptotics for least absolute deviation regression estimators”. Econometric Theory. 7(02): 186–199. 
Popescu, I. 2007. “Robust mean-covariance solutions for stochastic optimization”. Operations Research. 55(1): 98–112. 
Pregibon, D. 1982. “Resistant fits for some commonly used logistic models with medical application.” Biometrics. 38(2): 485–498. 
Raghunathan, A., S. M. Xie, F. Yang, J. C. Duchi, and P. Liang. 2019. “Adversarial training can hurt generalization”. arXiv preprint arXiv:1906.06032. 
Rahimian, H. and S. Mehrotra. 2019. “Distributionally robust optimization: A review”. arXiv preprint arXiv:1908.05659. 
Reynolds, O., A. W. Brightmore, and W. H. Moorby. 1903. Papers on Mechanical and Physical Subjects: The sub-mechanics of the universe. Vol. 3. The University Press. 
Rish, I. et al. 2001. “An empirical study of the naive Bayes classifier”. In: International Joint Conferences on Artificial Intelligence (IJCAI) Workshop on Empirical Methods in Artificial Intelligence. Vol. 3. No. 22. 41–46. 
Rockafellar, R. 1970. Convex analysis. Princeton University Press. Rogers, L. J. 1888. “An extension of a certain theorem in inequalities”. 
Messenger of Math. 17(2): 145–150. Roth, V. and B. Fischer. 2008. “The group-LASSO for generalized 
linear models: uniqueness of solutions and efficient algorithms”. In: International Conference on Machine Learning. 848–855. 
Rousseeuw, P. J. 1984. “Least median of squares regression”. Journal of the American statistical association. 79(388): 871–880. 
Rousseeuw, P. J. 1985. “Multivariate estimation with high breakdown point”. Mathematical Statistics and Applications. 8: 283–297.
References 243 
Rousseeuw, P. J. and A. M. Leroy. 2005. Robust regression and outlier detection. John Wiley & Sons. 
Rousseeuw, P. and V. Yohai. 1984. “Robust regression by means of S-estimators”. In: Robust and Nonlinear Time Series Analysis. 256– 272. 
Sanov, I. N. 1958. On the probability of large deviations of random variables. United States Air Force, Office of Scientific Research. 
Satia, J. K. and R. E. Lave Jr. 1973. “Markovian decision processes with uncertain transition probabilities”. Operations Research. 21(3): 728–740. 
Shafieezadeh-Abadeh, S., D. Kuhn, and P. M. Esfahani. 2017. “Regu-larization via mass transportation”. arXiv preprint arXiv: 1710. 10016. 
Shang, C., X. Huang, and F. You. 2017. “Data-driven robust optimization based on kernel learning”. Computers & Chemical Engineering. 106: 464–479. 
Shi, J. and J. Malik. 2000. “Normalized cuts and image segmentation”. IEEE Transactions on Pattern Analysis and Machine Intelligence. 22(8): 888–905. 
Simon, N., J. Friedman, T. Hastie, and R. Tibshirani. 2013. “A sparsegroup LASSO”. Journal of Computational and Graphical Statistics. 22(2): 231–245. 
Sinha, A., H. Namkoong, and J. Duchi. 2018. “Certifying some distributional robustness with principled adversarial training”. In: International Conference on Learning Representations. 
Sinha, A., M. O’Kelly, H. Zheng, R. Mangharam, J. Duchi, and R. Tedrake. 2020. “FormulaZero: distributionally robust online adaptation via offline population synthesis”. In: International Conference on Machine Learning. 
Slivkins, A. 2014. “Contextual bandits with similarity information”. The Journal of Machine Learning Research. 15(1): 2533–2568. 
Tewari, A. and S. A. Murphy. 2017. “From ads to interventions: contextual bandits in mobile health”. In: Mobile Health. 495–517. 
Tibshirani, J. and C. D. Manning. 2013. “Robust logistic regression using shift parameters”. arXiv preprint arXiv:1305.4987.
244 References 
Tibshirani, R. 1996. “Regression shrinkage and selection via the LASSO”. Journal of the Royal Statistical Society. Series B (Methodological). 58(1): 267–288. 
Tibshirani, R. 2011. “Regression shrinkage and selection via the LASSO: a retrospective”. Journal of the Royal Statistical Society: Series B (Statistical Methodology). 73(3): 273–282. 
Tomioka, R. and T. Suzuki. 2013. “Convex tensor decomposition via structured Schatten norm regularization”. In: Advances in Neural Information Processing Systems. 1331–1339. 
Trafalis, T. B. and R. C. Gilbert. 2006. “Robust classification and regression using support vector machines”. European Journal of Operational Research. 173(3): 893–909. 
Tsay, R. S. 2013. Multivariate time series analysis: with R and financial applications. John Wiley & Sons. 
Van Parys, B. P., D. Kuhn, P. J. Goulart, and M. Morari. 2015. “Distri-butionally robust control of constrained stochastic systems”. IEEE Transactions on Automatic Control. 61(2): 430–442. 
Velu, R. and G. C. Reinsel. 2013. Multivariate reduced-rank regression: theory and applications. Vol. 136. Springer Science & Business Media. 
Vershynin, R. 2017. High-dimensional probability: An introduction with applications in data science. Cambridge University Press. 
Villani, C. 2008. Optimal transport: old and new. Vol. 338. Springer Science & Business Media. 
Von Luxburg, U. 2007. “A tutorial on spectral clustering”. Statistics and Computing. 17(4): 395–416. 
Von Neumann, J. and O. Morgenstern. 1944. “Theory of games and economic behavior.” 
Wang, L., M. D. Gordon, and J. Zhu. 2006. “Regularized least absolute deviations regression and an efficient algorithm for parameter tuning”. In: International Conference on Data Mining. 690–700. 
Wang, R., X. Wang, and L. Wu. 2010. “Sanov’s theorem in the Wasser-stein distance: a necessary and sufficient condition”. Statistics & Probability Letters. 80(5-6): 505–512.
References 245 
Wang, Z., P. W. Glynn, and Y. Ye. 2016. “Likelihood robust optimization for data-driven problems”. Computational Management Science. 13(2): 241–261. 
White III, C. C. and H. K. Eldeib. 1994. “Markov decision processes with imprecise transition probabilities”. Operations Research. 42(4): 739–749. 
Wiesemann, W., D. Kuhn, and M. Sim. 2014. “Distributionally robust convex optimization”. Operations Research. 62(6): 1358–1376. 
Wu, H., R. Srikant, X. Liu, and C. Jiang. 2015. “Algorithms with logarithmic or sublinear regret for constrained contextual bandits”. In: Advances in Neural Information Processing Systems. 433–441. 
Xia, I. 2018. “The price of personalization: an application of contextual bandits to mobile health”. PhD thesis. Harvard University. 
Xie, W. 2019. “On distributionally robust chance constrained programs with Wasserstein distance”. Mathematical Programming: 1–41. 
Xu, H., C. Caramanis, and S. Mannor. 2009a. “Robust regression and LASSO”. In: Advances in Neural Information Processing Systems. 1801–1808. 
Xu, H., C. Caramanis, and S. Mannor. 2009b. “Robustness and regularization of support vector machines”. Journal of Machine Learning Research. 10(Jul): 1485–1510. 
Yan, Y., Z. Xu, I. W. Tsang, G. Long, and Y. Yang. 2016. “Robust semi-supervised learning through label aggregation”. In: Thirtieth AAAI Conference on Artificial Intelligence. 
Yang, I. 2018a. “A dynamic game approach to distributionally robust safety specifications for stochastic systems”. Automatica. 94: 94– 101. 
Yang, I. 2018b. “Wasserstein distributionally robust stochastic control: A data-driven approach”. arXiv preprint arXiv:1812.09808. 
Yang, W. and H. Xu. 2013. “A unified robust regression model for LASSO-like algorithms”. In: International Conference on Machine Learning. 585–593. 
Yin, J., X. Chen, and E. P. Xing. 2012. “Group sparse additive models”. In: International Conference on Machine Learning. Vol. 2012. NIH Public Access. 871.
246 References 
Yohai, V. J. 1987. “High breakdown-point and high efficiency robust estimates for regression”. The Annals of Statistics: 642–656. 
Yuan, M., A. Ekici, Z. Lu, and R. Monteiro. 2007. “Dimension reduction and coefficient estimation in multivariate linear regression”. Journal of the Royal Statistical Society: Series B (Statistical Methodology). 69(3): 329–346. 
Yuan, M. and Y. Lin. 2006. “Model selection and estimation in regression with grouped variables”. Journal of the Royal Statistical Society: Series B (Statistical Methodology). 68(1): 49–67. 
Zames, G. 1981. “Feedback and optimal sensitivity: Model reference transformations, multiplicative seminorms, and approximate inverses”. IEEE Transactions on automatic control. 26(2): 301–320. 
Zhai, R., T. Cai, D. He, C. Dan, K. He, J. Hopcroft, and L. Wang. 2019. “Adversarially robust generalization just requires more unlabeled data”. arXiv preprint arXiv:1906.00555. 
Zhang, H., H. Zhao, J. Sun, D. Wang, and K. Kim. 2013. “Regression analysis of multivariate panel count data with an informative observation process”. Journal of Multivariate Analysis. 119: 71–80. 
Zhao, C. and Y. Guan. 2015. “Data-driven risk-averse two-stage stochastic program with ζ-structure probability metrics”. Available on Optimization Online. 
Zhao, C. and Y. Guan. 2018. “Data-driven risk-averse stochastic optimization with Wasserstein metric”. Operations Research Letters. 46(2): 262–267. 
Zhao, P., G. Rocha, and B. Yu. 2009. “The composite absolute penalties family for grouped and hierarchical variable selection”. The Annals of Statistics: 3468–3497. 
Zhou, K. and J. C. Doyle. 1998. Essentials of robust control. Vol. 104. Prentice hall Upper Saddle River, NJ. 
Zhu, F., J. Guo, R. Li, and J. Huang. 2018. “Robust actor-critic contextual bandit for mobile health (mhealth) interventions”. In: ACM International Conference on Bioinformatics, Computational Biol-ogy, and Health Informatics. 492–501. 
Zou, H. and T. Hastie. 2005. “Regularization and variable selection via the elastic net”. Journal of the Royal Statistical Society: Series B (Statistical Methodology). 67(2): 301–320.
References 247 
Zymler, S., D. Kuhn, and B. Rustem. 2013. “Distributionally robust joint chance constraints with second-order moment information”. Mathematical Programming. 137(1-2): 167–198.