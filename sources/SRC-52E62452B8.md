> Source: https://people.eecs.berkeley.edu/~elghaoui/Pubs/RobMDP_OR2005.pdf

OPERATIONS RESEARCH Vol. 53, No. 5, September–October 2005, pp. 780–798 issn 0030-364X !eissn 1526-5463 !05 !5305 !0780 
informs ® 
doi 10.1287/opre.1050.0216 ©2005 INFORMS 
Robust Control of Markov Decision Processes with Uncertain Transition Matrices 
Arnab Nilim, Laurent El Ghaoui Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, California 94720 
{nilim@eecs.berkeley.edu, elghaoui@eecs.berkeley.edu} 
Optimal solutions to Markov decision problems may be very sensitive with respect to the state transition probabilities. In many practical problems, the estimation of these probabilities is far from accurate. Hence, estimation errors are limiting factors in applying Markov decision processes to real-world problems. 
We consider a robust control problem for a finite-state, finite-action Markov decision process, where uncertainty on the transition matrices is described in terms of possibly nonconvex sets. We show that perfect duality holds for this problem, and that as a consequence, it can be solved with a variant of the classical dynamic programming algorithm, the “robust dynamic programming” algorithm. We show that a particular choice of the uncertainty sets, involving likelihood regions or entropy bounds, leads to both a statistically accurate representation of uncertainty, and a complexity of the robust recursion that is almost the same as that of the classical recursion. Hence, robustness can be added at practically no extra computing cost. We derive similar results for other uncertainty sets, including one with a finite number of possible values for the transition matrices. 
We describe in a practical path planning example the benefits of using a robust strategy instead of the classical optimal strategy; even if the uncertainty level is only crudely guessed, the robust strategy yields a much better worst-case expected travel time. 
Subject classifications : dynamic programming: Markov, finite state, game theory; programming: convex, uncertainty, robustness; statistics: estimation. 
Area of review : Stochastic Models. History : Received January 2003; revisions received January 2004, May 2004; accepted September 2004. 
Notation P > 0 or P ! 0 refers to the strict or nonstrict componentwise inequality for matrices or vectors. For a vector p > 0, logp refers to the componentwise operation. The notation 1 refers to the vector of ones, with size determined from context. The probability simplex in Rn is denoted !n = "p " Rn 
+# p T 1= 1$, while %n is the set of n#n transition matri-
ces (componentwise nonnegative matrices with rows summing to one). We use &! to denote the support function of a set ! $Rn, with for v "Rn, &!'v( #= sup"pT v# p "!$. 
1. Introduction Finite-state and finite-action Markov decision processes (MDPs) capture several attractive features that are important in decision making under uncertainty: they handle risk in sequential decision making via a state transition probability matrix, while taking into account the possibility of information gathering and using this information to apply recourse during the multistage decision process (Putterman 1994, Berstsekas and Tsitsiklis 1996, Mine and Osaki 1970, Feinberg and Shwartz 2002). This paper addresses the issue of uncertainty at a higher 
level: We consider a Markov decision problem in which the transition probabilities themselves are uncertain, and seek 
a robust decision for it. Our work is motivated by the fact that in many practical problems, the transition matrices have to be estimated from data, and this may be a difficult task; see, for example, Kalyanasundaram et al. (2001), Feinberg and Shwartz (2002), Abbad and Filar (1992), and Abbad et al. (1992). It turns out that estimation errors may have a huge impact on the solution, which is often quite sensitive to changes in the transition probabilities. We will provide an example of this phenomenon in §8. A number of authors have addressed the issue of uncer-
tainty in the transition matrices of an MDP. A Bayesian approach such as described by Shapiro and Kleywegt (2002) requires a perfect knowledge of the whole prior distribution on the transition matrix, making it difficult to apply in practice. Other authors have considered the transition matrix to lie in a given set, most typically a polytope (Satia and Lave 1973, White and Eldeib 1994, Givan et al. 1997). Although our approach allows one to describe the uncertainty on the transition matrix by a polytope, we will argue against choosing such a model for the uncertainty. First, a general polytope is often not a tractable way to address the robustness problem, as it incurs a significant additional computational effort to handle uncertainty. As we will show, an exception is when the uncertainty is described by an interval matrix, intersected 
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 781 
by the constraint that probabilities sum to one, as in Givan et al. (1997) and Bagnell et al. (2001); or, when the polytope is described by its vertices. Perhaps more importantly, polytopic models, especially interval matrices, may be very poor representations of statistical uncertainty and lead to very conservative robust policies (Nilim and El Ghaoui 2002). In Bagnell et al. (2001), authors consider a problem dual to ours, and give without proof the “robust value iteration,” which we derive here. Like us, they consider relative entropy as a way to measure uncertainties in the transition matrices; however, they do not propose any specific algorithm to solve the corresponding “inner problem,” which has to be solved at each step of the robust value iteration. They only provide a general statement according to which the cost of solving the inner problem is polynomial in problem size, provided the uncertainty on the transition matrices is described by convex sets. In Iyengar (2003), the author discusses a problem similar to ours, introducing two versions of uncertainty (static and dynamic), and provides an independent proof of the robust value iteration in the case of compact uncertainty sets. 
2. Problem Setup 
2.1. Nominal Problem 
We consider a finite-horizon MDP with finite decision horizon T = "0)1)2) * * * )N % 1$. At each stage, the system occupies a state i " " , where n = !" ! is finite, and a decision maker is allowed to choose an action a deterministically from a finite set of allowable actions # = "a1) * * * )am$ (for notational simplicity we assume that # is not state dependent). The system starts in a given initial state i0. The states make Markov transitions according to a collection of (possibly time dependent) transition matrices + #= 'Pa 
t (a"#) t"T , where for every a " #, t " T , the n# n transition matrix Pa 
t contains the probabilities of transition under action a at stage t. We denote by , = 'a0) * * * )aN%1( a generic controller policy, where at'i( denotes the controller action when the system is in state i " " at time t " T . Let - = #nN be the corresponding strategy space. Define by ct'i)a( the cost corresponding to state i "" and action a "# at time t " T , and by cN the cost function at the terminal stage. We assume that ct'i)a( is nonnegative and finite for every i "" and a "#. For a given set of transition matrices + , we define the 
finite-horizon nominal problem by 
.N '-)+( #=min ,"-
CN ',) +() (1) 
where CN ',) +( denotes the expected total cost under controller policy , and transitions + : 
CN ',) +( #=E !N%1 " 
t=0 
ct'it)at'i((+ cN 'iN ( 
# 
* (2) 
A special case of interest is when the expected total cost function bears the form (2), where the terminal cost is zero, 
and ct'i)a( = /tc'i)a(, with c'i)a( now a constant cost function, which we assume nonnegative and finite everywhere, and / " '0)1( is a discount factor. We refer to this cost function as the discounted cost function, and denote by C&',) +( the limit of the discounted cost (2) as N '&. 
When the transition matrices are exactly known, the corresponding nominal problem can be solved via a dynamic programming algorithm, which has total complexity of mn2N flops in the finite-horizon case. In the infinitehorizon case with a discounted cost function, the cost of computing an 0-suboptimal policy via the Bellman recursion is O'mn2 log'1/0((; see Putterman (1994) for more details. 
2.2. Robust Control Problems 
First, we consider the finite-horizon case, and assume that when for each action a and time t, the corresponding transition matrix Pa 
t is only known to lie in some given subset !a 
of %n. Loosely speaking, we can think of the sets !a as sets of confidence for the transition matrices. We further assume that the sets !a satisfy: 
Rectangular Uncertainty Property. For every a "#, !a has the form !a =!a 
1 # · · ·#!a n , where !a 
i s are given subsets of the probability simplex in Rn that describe the uncertainty on the ith row of Pa (that is, on the state distribution given action a). 
Note that our uncertainty model does not allow for correlations between the uncertainties affecting the Pas across different actions a, nor between different rows of each matrix. Two models for transition matrix uncertainty are possi-
ble, leading to two possible forms of finite-horizon robust control problems. In a first model, referred to as the stationary uncertainty model, the transition matrices are chosen by nature depending on the controller policy once and for all, and remain fixed thereafter. In a second model, which we refer to as the time-varying uncertainty model, the transition matrices can vary arbitrarily with time, within their prescribed bounds. Each problem leads to a game between the controller and nature, where the controller seeks to minimize the maximum expected cost, with nature being the maximizing player. Let us define our two problems more formally. A pol-
icy of nature refers to a specific collection of time-dependent transition matrices + = 'Pa 
t (a"#) t"T chosen by nature, and the set of admissible policies of nature is $ #= ' $ 
a"# ! a(N , where 
$ 
denotes direct product. Denote by $s the set of stationary admissible policies of nature: 
$s = % 
+ = 'Pa t (a"#) t"T "$ # 
Pa t = Pa 
s for every t) s " T ) a "# & 
* 
The stationary uncertainty model leads to the problem 
.N '-)$s( #=min ,"-
max +"$s 
CN ',) +(* (3)
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 782 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
In contrast, the time-varying uncertainty model leads to a relaxed version of the above: 
.N '-)$s(".N '-)$ ( #=min ,"-
max +"$ 
CN ',) +(* (4) 
The first model is attractive for statistical reasons, as it is much easier to develop statistically accurate sets of confidence when the underlying process is time invariant. Unfortunately, the resulting game (3) seems to be hard to solve. The second model is attractive as one can solve the corresponding game (4) using a variant of the dynamic programming algorithm seen later, but we are left with a difficult task, that of estimating a meaningful set of confidence for the time-varying matrices Pa 
t . In this paper, we will use the first model of uncertainty to derive statistically meaningful sets of confidence for the transition matrices, based on likelihood or entropy bounds. Then, instead of solving the corresponding difficult control problem (3), we use an approximation that is common in robust control, and solve the time-varying upper bound (4), using the uncertainty sets !a derived from a stationarity assumption about the transition matrices. We will also consider a variant of the finite-horizon time-
varying problem (4), where controller and nature play alternatively, leading to a sequential game 
.seq N '-)%( #=min 
a0 max +0"% 
min a1 
max +1"% 
· · ·min aN%1 
max +N%1"% 
CN ',) +() 
(5) 
where the notation +t = 'Pa t (a"# denotes the collection of 
transition matrices at a given time t " T , and % #=$ 
a"# ! a 
is the corresponding uncertainty set from which nature is allowed to choose the transition matrices at every stage. Finally, we will consider an infinite-horizon robust con-
trol problem, with the discounted cost function referred to above, and where we restrict control and nature policies to be stationary: 
.&'-s)$s( #= min ,"-s 
max +"$s 
C&',) +() (6) 
where -s denotes the space of stationary control policies. We define .&'-)$ (, .&'-)$s(, and .&'-s)$ ( accordingly. In the sequel, for a given control policy , "- and sub-
set & $ $ , the notation .N ',)& ( #= max+"& CN ',) +( denotes the worst-case expected total cost for the finitehorizon problem, and .&',)& ( is defined likewise. 
2.3. Main Results and Outline 
Our main contributions are as follows. First, we derive a recursion, the “robust dynamic programming” algorithm, which solves the finite-horizon robust control problem (4). We provide a simple proof of the optimality of the recursion, where the main ingredient is to show that perfect duality holds in the game (4). (For completeness, another 
proof, which requires a theorem from stochastic game theory, is given in Appendix A.) As a corollary of this result, we obtain that the sequential game (5) is equivalent to its nonsequential counterpart (4). Second, we derive similar results for the infinite-horizon problem with discounted cost function, (6). Moreover, we obtain that if we consider a finite-horizon problem with a discounted cost function, then the gap between the optimal value of the stationary uncertainty problem (3) and that of its time-varying counterpart (4) goes to zero as the horizon length goes to infinity, at a rate determined by the discount factor. Finally, we identify several classes of uncertainty models, which result in an algorithm that is both statistically accurate and numerically tractable. We derive precise complexity results that imply that, with the proposed approach, robustness can be handled at practically no extra computing cost. Our paper is organized as follows. Section 3 deals with 
the finite-horizon problem, including the “robust dynamic programming” theorem (Theorem 1) and its proof, as well as a detailed complexity analysis. Section 4 provides similar results for the infinite-horizon case. Sections 5 and 6 are devoted to specific uncertainty models, involving likelihood regions or entropy bounds, while §7 deals with finite scenario, ellipsoidal, and interval matrix models. We describe numerical results in the context of aircraft routing in §8. Section 9 contains concluding remarks. 
3. Finite-Horizon Problem We consider the finite-horizon robust control problem defined in §2.2. For a given state i "" , action a "#, and Pa "!a, we denote by pa 
i the next-state distribution drawn from Pa corresponding to state i "" ; thus pa 
i is the ith row of matrix Pa. We define !a 
i as the projection of the set !a 
onto the set of pa i -variables; by the rectangular uncertainty 
property, !a is the direct product of these sets. By assumption, !a 
i s are included in the probability simplex of Rn, !n; no other property is assumed. 
3.1. Robust Dynamic Programming 
We provide below a self-contained proof of the following theorem, based on linear programming duality. For completeness, we provide an alternate proof in Appendix A, based on a stochastic game formulation. Yet another proof of the robust Bellman recursion (7), (8) is also given by Iyengar (2003), via an appropriately defined robust value function and exploiting a certain “rectangularity property” (Epstein and Schneider 2002), which is different from the rectangular uncertainty property defined in §2.2. 
Theorem 1 (Robust Dynamic Programming). For the robust control problem (4), perfect duality holds: 
.N '-)$ (=min ,"-
max +"$ 
CN ',) +( 
=max +"$ 
min ,"-
CN ',) +( #= 1N '-)$ (*
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 783 
The problem can be solved via the recursion 
vt'i(=min a"# 
' 
ct'i)a(+&!a i 'vt+1( 
( 
) i "") t " T ) (7) 
where &!'v( #= sup"pT v# p "!$ denotes the support function of a set !, and vt'i( is the worst-case optimal value function in state i at stage t. A corresponding optimal control policy ,( = 'a(0) * * * )a 
( N%1( is obtained by setting 
a(t 'i( " argmin a"# 
% 
ct'i)a(+&!a i 'vt+1( 
& 
) i "") (8) 
and a corresponding worst-case nature policy is obtained by choosing the ith row of the transition matrix Pa 
t as 
pa i 't( " argmax 
p "pT vt+1# p "!a 
i $) i "") a "#) t " T * 
(9) 
The effect of uncertainty on a given strategy , = 'a0) * * * )aN ( can be evaluated by the following recursion: 
v, t 'i(= ct'i)at'i((+&!at 'i( 
i 'v, 
t+1() i "") (10) 
which provides the worst-case value function v, for the strategy ,. 
Proof. We begin with a simple technical lemma. 
Lemma 1. For given vN "Rn, consider the problem 
2 #= max v0)***)vN%1 
qT v0# vt " gt'vt+1() t " T ) i "") (11) 
where inequalities are understood componentwise, q "Rn +, 
and the functions gt# Rn 'Rn are given. If the functions gt are componentwise nondecreasing for every t " T , meaning that gt'u(" gt'v( for every u)v "Rn with u" v, then the optimal variables can be computed via the recursion 
vt = gt'vt+1() t " T ) (12) 
and the optimal value is 2= qT 'g1 ) · · · ) gN ('vN (. To prove Lemma 1, we note that recursion (12) yields 
v0 = v(0 #= 'g1 ) · · · ) gN ('vN (. In addition, this recursion provides a feasible point for the problem, hence 2! qT v(0. Because q ! 0, and each gt is componentwise nondecreasing, we also have 2" qT v(0, which shows that the recursion provides the optimal value of problem (11). This proves the lemma. We proceed with a well-known linear programming rep-
resentation of the nominal problem (1) (Putterman 1994): 
.N '-)+( 
#= max v0)***)vN%1 
qT v0# vt'i(" ct'i)a(+ " 
j 
P a t 'i) j(vt+1'j() 
a "#) i "") t " T ) (13) 
where q is a componentwise nonnegative vector, precisely q'i(= 0 if i *= i0, q'i0(= 1, where i0 is the initial state. In the above, we have denoted by + #= 'Pa 
t (a"#) t"T the (given) collection of time-varying transition matrices. Likewise, the expected cost for a given controller policy , = 'at(t"T is given by the linear program 
.N ',) +( #= max v0)***)vN%1 
qT v0# vt'i(" ct'i)at'i(( 
+ " 
j 
P at'i( t 'i) j(vt+1'j() i "") t " T * (14) 
By weak duality, .N '-)$ ( ! 1N '-)$ (, where 1N '-)$ ( is defined in the theorem. Let us prove that perfect duality holds, that is, .N '-)$ (= 1N '-)$ (. The lower bound 1N '-)$ ( can be expressed as the optimal value of the following nonlinear problem (in variables v) +): 
1N '-)$ ( 
#= max +"$ )v0)***)vN%1 
qT v0# vt'i("ct'i)a(+ " 
j 
P a t 'i)j(vt+1'j() 
a"#) i"") t"T * (15) 
The difference between the nominal problem (13) and (15) is simply that the matrices Pa 
t are fixed in (13), while they are variables in problem (15). Denote by .N ',)$ (=max+"$ CN ',) +( the worst-case 
expected total cost for a given policy ,. This value is obtained by letting the matrices P at'i( 
t become variables in (14), which results in 
.N ',)$ ( #= max +"$ )v0)***)vN%1 
qT v0# vt'i(" ct'i)at'i(( 
+ " 
j 
P at'i( t 'i) j(vt+1'j() i "") t " T * (16) 
Due to the rectangular uncertainty property !a = !a 
1 # · · ·#!a n , the problem of computing 1N '-)$ (, and 
that of computing .N ',)$ ( for a given policy ,, can both be represented as problem (11) of Lemma 1, where we define the functions gt , t " T , by their components, as follows for problem (15): 
'gt'v((i #=min a"# 
' 
ct'i)a(+&!a i 'v( 
( 
) i "") 
and as follows for problem (16): 
'gt'v((i #= ct'i)at'i((+&!at 'i( i 
'v() i "" * 
Because the sets !a i are all included in !n, the above 
functions are componentwise nondecreasing, and Lemma 1 applies. This shows that problems (15) and (16) can be solved by the recursions (7) and (10), respectively, as given in Theorem 1. Recursion (7) provides a policy ,( = 'a(0) * * * )a 
( N%1(, via 
expression (8) as given in the theorem. We can express the recursion exactly as in (10), with at replaced with a(t , t " T .
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 784 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
This shows that 1N '-)$ ( = .N ', ()$ (. Because ,( is 
an admissible (that is, deterministic) policy, we necessarily have .N ', 
()$ ( ! .N '-)$ (. This shows that perfect duality holds: .N '-)$ ( = .N ', 
()$ ( = 1N '-)$ (, and that the policy ,( provided by expression (8) is optimal for the robust control problem (4). Finally, the expression for the optimal worst-case policy 
of nature given in (9) is obtained by noting that it corresponds to the solution of problem (15) when , is set to the optimal control policy. This ends our proof. # 
Note that our proof does not require convexity of the uncertainty sets !a 
i ; we only used the fact that these sets are entirely included in the probability simplex of Rn. 
We are ready to examine the sequential game (5). 
Corollary 1. The sequential game (5) is equivalent to the game (4): 
.seq N '-)%(=.N '-)$ () 
and the optimal strategies for .N '-)$ ( given in Theo-rem 1 are optimal for .seq 
N '-)%( as well. 
Proof. A repeated application of weak duality shows the lower bound .seq 
N '-)%(".N '-)$ ( (this is simply a consequence of the fact that the sequential game gives less power to nature). Because the optimal worst-case nature strategy defined in Theorem 1 is feasible for problem (5), the result follows. # 
3.2. Solving the Inner Problem 
Each step of the robust dynamic programming algorithm involves the solution of an optimization problem, referred to as the “inner problem,” of the form 
&!'v(=max p"! 
vT p) (17) 
where the variable p corresponds to a particular row of a specific transition matrix, ! =!a 
i is the set that describes the uncertainty on this row, and v contains the elements of the value function at some given stage. Note that we can safely replace ! in (17) by its convex hull, so that convexity of the sets !a 
i is not required; the algorithm only requires the knowledge of their convex hulls. The shape of the convex hulls conv'!a 
i ( for each i " " and a " # is a key component in the computational complexity of the robust dynamic programming algorithm. Beyond numerical tractability, an additional criteria for 
the choice of a specific uncertainty model is that the sets !a 
should represent accurate (nonconservative) descriptions of the statistical uncertainty on the transition matrices. Per-haps surprisingly, there are statistical models of uncertainty that are good on both counts; specific examples of such models are described in §§5 and 6. Precisely, the uncertainty models considered in §§5 and 6 all result in inner problems (17) that can be solved in worst-case time of 
O'n log'vmax/3(( via a simple bisection algorithm, where n is the size of the state space, vmax is a global upper bound on the value function, and 3> 0 specifies the accuracy at which the optimal value of the inner problem (17) is computed. We defer the proof of this complexity result to the appropriate sections. The bisection algorithm can be interpreted as a function +&! such that for every v " Rn, there exists 3!'v( such that 
+&!'v(= &!'v(+ 3!'v() 0" 3!'v(" 3* (18) 
3.3. Complexity Analysis 
In this section, we discuss the complexity of computing an 0-suboptimal policy +,, which is a policy such that the worst-case expected total cost under policy +,, namely .N ' +,)$ ( = max+"$ CN ' +,)+(, satisfies .N ' +,)$ ( % 0 " 
.N '-)$ ( " .N ' +,)$ (. Here, 0 > 0 is given. We assume that we use the specific uncertainty models considered in §§5 and 6, and that we solve the resulting inner problem with the bisection algorithm with an accuracy 3 #= 0/N . 
Theorem 2. For the finite-horizon problem, if we solve the inner problem (17) with the bisection algorithm accuracy parameter 3 #= 0/N , our algorithm will guarantee an 0-suboptimal policy, with an additional computational cost of log'N/0( with respect to the classical dynamic programming algorithm. 
Proof. When we apply the bisection algorithm within the robust dynamic programming algorithm given in §3.1, we generate vectors ,vt by recursion (7), with &!a 
i replaced by 
+&!a i , as defined by (18). The corresponding Equation (8) 
yields a policy +,. We can express the recursion that provides ,v as 
,vt'i(=min a"# 
' 
ct'i)a(+ 3t'i)a(+&!a i ',vt+1( 
( 
) i "") t " T ) 
where 3t'i)a( #= 3!a i 'vt+1(. The policy +, is obtained by 
looking at a minimizing index in the above. Thus, +, is optimal for the robust control problem (4), but with a modified cost function: ,ct'i)a(= ct'i)a(+3t'i)a(. The bounds 0" 3t'i)a(" 0/N then imply that the corresponding expected total cost function +CN satisfies CN ',) +( " 4 +CN ',) +(% 0) +CN ',) +(5 for every , "- and + "$ . Maximizing over + for , = +, yields .N ' +,)$ ( " 4 +. % 0) +.5, where +. #= min,"-max+"$ +CN ',) +( is the optimal value of the modified control problem, and .N ' +,)$ ( is the worst-case expected total cost under policy +, for the original problem. Likewise, minimizing over , the maximum over + yields .N '-)$ ( " 4 +. % 0) +.5. Because .N '-)$ ( " .N ' +,)$ ( because +, is deterministic, we conclude that .N '-)$ ( " 4.N ' +,)$ (% 0) .N ' +,)$ (5. We obtain that, to compute a suboptimal policy +, 
that achieves the exact optimum with prescribed accuracy 0, the number of flops required by the algorithm is O'mn2N log'vmaxN/0((. The bound vmax " NCmax, with Cmax =maxi"")a"#) t"T ct'i)a(, then leads to the complexity
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 785 
bound of O'mn2N log'N/0((, which means that robustness is obtained at a relative increase of computational cost of only log'N/0( with respect to the classical dynamic programming algorithm, which is small for moderate values of N . # 
If N is very large, we can turn instead to the infinitehorizon problem examined in §4, and similar complexity results hold. 
3.4. Algorithm 
Our analysis yields an algorithm to compute an 0-sub-optimal policy ,0 for problem (4) using the uncertainty models described in §§5 and 6. The algorithm has complexity O'mn2N log'N/0((. 
Robust Finite-Horizon Dynamic Programming Algorithm 
Step 1. Set 0> 0. Initialize the value function to its terminal value ,vN = cN . 
Step 2. Repeat until t = 0: (a) For every state i " " and action a "#, compute, 
using the bisection algorithm described in SS5 or 6, a value +&a i such that 
+&a i % 0/N " &!a 
i ',vt(" +&a 
i * 
(b) Update the value function by ,vt%1'i( = mina"#'ct%1'i)a(+ +&a 
i (, i "" . (c) Replace t by t% 1 and go to Step 2. 
Step 3. For every i " " and t " T , set ,0 = 'a0 0) * * * ) 
a0 N%1(, where 
a0 t 'i(= argmax 
a"# "ct%1'i)a(+ +&a 
i $) i "") a "#* 
4. Infinite-Horizon Problem In this section, we address a the infinite-horizon robust control problem, with a discounted cost function of the form (2), where the terminal cost is zero, and ct'i)a( = /tc'i)a(, where c'i)a( is now a constant cost function, which we assume nonnegative and finite everywhere, and / " '0)1( is a discount factor. 
4.1. Robust Bellman Recursion 
We begin with the infinite-horizon problem involving stationary control and nature policies defined in (6). In Bagnell et al. (2001), the authors consider the problem of computing the dual quantity 1&'-)$ ( defined below, and stated without proof that it can be computed by the recursion given in the theorem. The robust Bellman recursion for the infinite-horizon case (19, 20) is also proved independently in Iyengar (2003). 
Theorem 3 (Robust Bellman Recursion). For the infinite-horizon robust control problem (6) with stationary 
uncertainty on the transition matrices, stationary control policies, and a discounted cost function with discount factor / " 40)1(, perfect duality holds: 
.&'-s)$s(=max +"$s 
min ,"-s 
C&',) +( #= 1&'-s)$s(* 
The optimal value is given by .&'-s)$s(= v'i0(, where i0 is the initial state, and where the value function v satisfies is the optimality conditions 
v'i(=min a"# 
' 
c'i)a(+ /&!a i 'v( 
( 
) i "" * (19) 
The value function is the unique limit value of the convergent vector sequence defined by 
vk+1'i(=min a"# 
' 
c'i)a(+ /&!a i 'vk( 
( 
) i "") 
k= 1)2) * * * * (20) 
A stationary, optimal control policy , = 'a()a() * * *( is obtained as 
a('i( " argmin a"# 
% 
c'i)a(+ /&!a i 'v( 
& 
) i "") (21) 
and a stationary optimal nature policy is obtained by choosing the ith row of the transition matrix Pa as 
pa i " argmax 
p "pT v# p "!a 
i $) i "") a "#* (22) 
The effect of uncertainty on a given stationary strategy , = 'a)a) * * *( can be evaluated by the following equation: 
v,'i(= c'i)a'i((+ /&!a'i( i 
'v,() i "") (23) 
which provides the worst-case value function for the strategy ,. 
Proof. The proof follows identical lines as that of Theo-rem 1. As before, we begin with a simple technical lemma, which we state without proof. 
Lemma 2. For a given vector q "Rn + and function g# Rn ' 
Rn, consider the problem 
max v 
qT v# v" g'v() (24) 
where inequalities are understood componentwise. If the above problem is feasible, and g is monotone nondecreasing and contractive, then there is a unique optimizer v&, which is the unique solution to the fixed-point equation v= g'v(. 
We then express the nominal problem (without uncertainty on the transition matrices) with the linear program 
max v 
qT v# v'i("c'i)a(+/ " 
j 
P a'i)j(v'j() 
a"#) i"") (25)
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 786 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
where q is a componentwise nonnegative vector, precisely q'i( = 0 if i *= i0, q'i0( = 1, where i0 is the initial state. Likewise, the expected cost for a given stationary controller policy , = 'a)a) * * *( is given by the linear program 
max v 
qT v# v'i(" c'i)a'i(( 
+ / " 
j 
P a'i('i) j(v'j() i "" * (26) 
By weak duality, .&'-s)$s( ! 1&'-s)$s(, where the latter is defined in the theorem. We now prove that equality holds. The lower bound 1&'-s)$s( can be expressed as the solution to the nonlinear problem (in variables v, +) obtained by letting the Pas become variables in (25): 
1&'-s)$s(= max +"$s )v 
qT v# v'i(" c'i)a(+ / " 
j 
P a'i) j(v'j() 
a "#) i "" * (27) 
Likewise, if we denote by .&',)$s( #=max+"$s C&',) +( 
the worst-case expected total cost for a given policy ,, then this value is obtained by letting the matrices P a'i( become variables in (14), which results in 
.&',)$s( #= max +"$s )v 
qT v# v'i("c'i)a'i(( 
+/ " 
j 
P a'i('i)j(v'j() i"" * 
(28) 
Due to the rectangular uncertainty property !a = !a 
1 # · · ·#!a n , the problem of computing 1&'-s)$s(, and 
that of computing .&',)$s( for a given policy ,, can both be represented as problem (24) of Lemma 2, where we define the function g by their components, as follows for problem (27): 
'g'v((i #=min a"# 
' 
c'i)a(+ /&!a i 'v( 
( 
) i "") (29) 
and as follows for problem (28): 
'g'v((i #= c'i)a'i((+ /&!a'i( i 
'v,() i "" * (30) 
Because the sets !a i are all included in !n, the above func-
tions are componentwise nondecreasing; furthermore, these functions are /-contractive, and Lemma 1 applies. This shows that the optimal value of problems (15) and (16) are characterized by the equations given in Theorem 3. The contractive property of g defined by (29) can be established by observing that for any pair u)v " Rn, and for every i "" , we have 
gi'u(=min a"# 
max p"!a 
i 
' 
c'i)a(+ /pT v+ /pT 'u% v( ( 
"min a"# 
max p"!a 
i 
' 
c'i)a(+ /pT v ( 
+ /max p"!a 
i 
pT 'u% v( 
" gi'v(+ / max pT 1=1)p!0 
pT 'u% v( 
" gi'v(+ /-u% v-&* The proof of the contractive property for g defined by (30) is similar. The rest of the proof is similar to that of Theo-rem 1. This ends our proof. # 
Theorem (3) leads to the following theorem. 
Theorem 4. In the infinite-horizon problem, we can without loss of generality assume that the control and nature policies are stationary, that is, 
.&'-)$ (=.&'-s)$s(=.&'-s)$ (=.&'-)$s(* (31) 
Furthermore, in the finite-horizon case, with a discounted cost function, the gap between the optimal values of the robust control problems under stationary and time-varying uncertainty models, .N '-)$ (% .N '-)$s(, goes to zero as the horizon length N goes to infinity, at a geometric rate /. 
Proof. The proof is in five steps. In Step (a), we prove that .N '-)$ ( converges to .&'-s)$s(. In Step (b), we prove that 6N '-)$ ( converges geometrically at rate /, to .&'-)$ (, which also proves the first equality in (31). Step (c) proves the second inequality, and Step (d) the last. In Step (d), we prove .&'-)$s( = .&'-s)$s(. In Step (e), we prove that .N '-)$ (%.N '-)$s( goes to zero as N '&, at a geometric rate /. Step (a). First, we prove that .N '-)$ ( converges to 
.&'-s)$s(. Denote by 'vk( the iterates of the value function delivered by the infinite-horizon recursion (20), and by v& its limit. We have .&'-s)$s( = v&'i0(, where i0 is the initial state. Fix 0 > 0; by convergence of recursion (20), there exists a positive integer N0 such that for every N >N0, 
. i "") v&'i(% 0" vN 'i(" v&'i(* (32) 
Now fix N > N0, and define the sequence ṽt = /tvN%t for t = 0) * * * )N %1; it satisfies the finite-horizon recursion (7) with the cost function ct'i)a(= /tc'i)a(. Thus, 'ṽt(t"T is the optimal value function for the problem of computing .N '-)$ (, and in particular, ṽ0'i0(= vN 'i0(= .N '-)$ (. Specializing (32) to i= i0, we obtain 
.&'-s)$s(% 0".N '-)$ (".&'-s)$s() (33) 
which proves the convergence result. Step (b). Next, we prove that 6N '-)$ ( converges geo-
metrically at rate /, to .&'-)$ (; combining this with Step (a) will then establish the first equality in (31). For every N , the /-discounted cost function satisfies 
CN ',) +("C&',) +("CN ',) +(+ 0N ) (34) 
where cmax #= maxi"")a"# c'i)a( < & and where 0N #= /N cmax/'1% /( converges geometrically to zero at rate /. The above implies 
.N '-)$ (".&'-)$ (".N '-)$ (+ 0N ) (35) 
which in turn proves that .N '-)$ ( converges geometrically at rate /, to .&'-)$ (=.&'-s)$s(.
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 787 
Step (c). To prove .&'-s)$s(=.&'-s)$ ( (the second equality in (31)), we observe that the bounds (34) imply that for every stationary policy , and every N , 
.N ',)$ (".&',)$ (".N ',)$ (+ 0N ) 
where .N ',)$ ( #= max+"$ CN ',) +( and .&',)$ ( is defined likewise. This shows that limN'&.N ',)$ ( = .&',)$ ( for every , " -s . Following similar steps as in Step (a), one can prove that for every stationary policy , " -s , .N ',)$ ( converges to .&',)$s(. This ensures that .&',)$ (= .&',)$s( for every , "-s , and hence, .&'-s)$ (=.&'-s)$s(. Step (d). To prove the equality 
.&'-)$s(=.&'-s)$s() 
we note that standard results on the stationarity of optimal policies for nominal problems (Putterman 1994) imply that for every stationary nature policy + " $s , .N '-)+( converges to .&'-s) +( as N '&. The equality then follows from the following bound, derived from (34): for every + " $s , .N '-)+(".&'-)+(".N '-)+(+ 0N . 
Step (e). Finally, from (34), we obtain 
.N '-)$s(".&'-)$s(".N '-)$s(+ 0N ) 
which shows that .N '-)$s( converges geometrically at a rate / to .&'-)$s(=.&'-s)$s(=.&'-)$ (. We know from Step (b) that the same holds for .N '-)$ (, thus the gap .N '-)$ ( % .N '-)$s( goes to zero as the horizon length N goes to infinity, at a geometric rate /. # 
4.2. Complexity Analysis 
We now turn to the complexity analysis of the infinitehorizon problem, assuming again that we use the specific uncertainty models described in §§5 and 6. The robust Bellman recursion (20) provides a sequence 'vk( which converges geometrically at rate / to the optimal value function v& of the problem. This means that to achieve a given accuracy (say 0/2) on that value, we need O'log'1/0(( iterations, with exact computation of the inner problem at each step. Let us examine the complexity when inexact values are used. 
Theorem 5. For the infinite-horizon problem, if we solve the inner problem with the bisection algorithm accuracy parameter 3= '1% /(0/2/, our algorithm will guarantee an 0-suboptimal policy, with an additional computational cost of log'1/0( with respect to the classical dynamic programming algorithm. 
Proof. We consider iterates ',vk( of recursion (20), with the same initial condition ,v0 = v0, but where we use the bisection algorithm with accuracy 3 = '1 % /(0/2/, in effect replacing the map &!a 
i by its approximate counterpart +&!a 
i , 
as defined by (18). Let us prove that these approximate values also converge in O'log'1/0(( time. We now prove by induction that vk " ,vk " vk+71, where 
7 = /3/'1 % /( = 0/2. The initial condition is obtained trivially, as v1 = ,v1 satisfies v1 " ,v1 " v1+71. Assume that the bounds are true for a given k! 1. Then, for every i, a, we have 
&!a i 'vk("&!a 
i ',vk("&!a 
i 'vk+71("&!a 
i 'vk(+&!a 
i '71( 
=&!a i 'vk(+7) 
where we successively used the convexity, monotonicity, and homogeneity of degree one of the function &!a 
i . We 
then obtain 
vk+1'i(" ,vk+1'i("vk+1'i(+/'3+7(=vk+1'i(+7 .i"") 
which proves our result. The above implies that 
-,vk % v&-& " -,vk % vk-& + -vk % v&-& " 7+ 0/2= 0) 
provided k=O'log'1/0(( is large enough. This proves that we can achieve 0-convergence of ,vk in k=O'log'1/0((. 
We finish by examining the cost of computing an 0-suboptimal policy. The iterates ,vk obey to 
,vk+1'i(=min a"# 
' 
c'i)a(+ /3!a i ',vk(+ /&!a 
i ',vk( 
( 
) 
where 0" 3!a i ',vk(" 3. We can express the above as 
,vk+1'i(=min a"# 
' 
c'i)a(+/ ' 
3!a i ',vk(+!a 
i 'k( ( 
+/&!a i ',vk+1( 
( 
) 
(36) 
where !a i 'k( #= &!a 
i ',vk( % &!a 
i ',vk+1(. !!a 
i 'k(! " -,vk+1 % ,vk-& can be obtained by using the fact that, for any pair of n-vectors 'u)v(, and subset ! of the probability simplex !n, we have 
&!'u(%&!'v(=max p"! 
min q"! 
'pT u% qT v("max p"! 
pT 'u% v( 
"max p"!n 
pT 'u% v(" -u% v-&* 
Let 3a i 'k( #= 3!a 
i ',vk( + !a 
i 'k(. Choose k = N such that -,vN+1 % ,vN-& " '1 % /(0/2/, so that !3a 
i 'N (! " 3 + '1% /(0/2/ = '1% /(0//. (By the convergence properties proved above, we have N =O'log'1/0((.) Relation (36) implies that ,vk+1 and the corresponding 
policy +,k is optimal for the infinite-horizon problem, but with a different cost function ,c, defined by ,c'i)a( = c'i)a(+/3a 
i 'N (. (Note that N is a constant here, so we are really defining a time-invariant cost.) The bound on 3a 
i 'N ( then implies that the corresponding expected total discounted cost function satisfies ! +C&',) +(%C&',) +(!" 0. The rest of the proof follows that of the finite-horizon case, with the only difference being that now we only have the
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 788 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
two-sided inequality !C&',) +(% +C&',) +(!" 0 as opposed to a one-sided inequality. But the result remains the same. We established that to compute an 0-suboptimal pol-
icy, we need to run O'log'1/0(( steps of the robust Bellman recursion, using a bisection algorithm with accuracy 3=O'0(. Each step of the Bellman recursion requires O'mn log'vmax/3(( flops, which needs to be computed for all the states at each iteration. Hence, the total complexity is O'mn2 log'vmax/3((. The bound vmax " cmax/'1% /(, where cmax =maxi"")a"# c'i)a(, brings the total complexity to O'mn2'log'1/0((2(. Thus, the extra computational cost incurred by robustness in the infinite-horizon case is O'log'1/0((. # 
4.3. Algorithm 
Our analysis yields the following algorithm to compute an 0-suboptimal policy ,0 for problem (6) in O'mn2'log'1/0((2( flops, using the uncertainty models described in §§5 and 6. 
Robust Infinite-Horizon Dynamic Programming Algorithm 
Step 1. Set 0 > 0, initialize the value function ,v1 > 0, and set k= 1. Step 2. (a) For all states i and controls a, compute, using 
the bisection algorithm described in §§5 or 6, a value +&a i 
such that 
+&a i % 3" &!a 
i ',vk(" +&a 
i ) 
where 3= '1% /(0/2/. (b) For all states i and controls a, compute ,vk+1'i( by 
,vk+1'i(=min a"# 
'c'i)a(+ /+&a i (* 
Step 3. If 
-,vk+1 % ,vk-< '1% /(0 
2/ ) 
go to Step 4. Otherwise, replace k by k + 1 and go to Step 2. Step 4. For each i "" , set an ,0 = 'a0)a0) * * *(, where 
a0'i(= argmax a"# 
"c'i)a(+ /+&a i $) i "" * 
5. Likelihood Models Our first model is based on a likelihood constraint to describe uncertainty on each transition matrix. Our uncertainty model is derived from a controlled experiment starting from state i= 1)2) * * * )n and the count of the number of transitions to different states. We denote by F a the matrix of empirical frequencies of transition with control a in the experiment; denote by f a 
i its ith row. We have F a ! 0 
and F a1= 1, where 1 denotes the vector of ones. For simplicity, we assume that F a > 0 for every a. 
To simplify the notation, we will drop the superscript a in this section, and refer to a generic transition matrix as P and to its ith row as pi. The same convention applies to the empirical frequency matrix F a and its rows f a 
i , as well as to sets !a and !a 
i . When the meaning is clear from context, we will further drop the subscript i. 
5.1. Model Description 
The “plug-in” estimate ,P = F is the solution to the maximum-likelihood problem 
max P 
L'P ( #= " 
i) j 
F 'i) j( logP 'i) j(# P ! 0) P1= 1* (37) 
The optimal log-likelihood is 
8max = " 
i) j 
F 'i) j( · logF 'i) j(* 
A classical description of uncertainty in a maximumlikelihood setting is via the likelihood region (Lehmann and Casella 1998, Poor 1988) ) 
P "Rn#n# P!0)P1=1) " 
i) j 
F 'i)j(logP 'i)j(!8 
* 
) (38) 
where 8 <8 max is a given number, which represents the uncertainty level. In practice, the designer chose an uncertainty level and 8 can be estimated using resampling methods, or a large sample Gaussian approximation, so as to ensure that the set above achieves the desired level of confidence (see Appendix D). The above description is classical in the sense that log-
likelihood regions are the starting point for developing ellipsoidal or interval models of confidence, hence, are more statistically accurate (Lehmann and Casella 1998); see §7.3 for further details. The above set is statistically meaningful as it describes how informative the data is. If this set is elongated along a direction, then the likelihood function does not vary much in that direction, and the data is not very informative in that direction. This set has some interesting features. First, it does not result from a (quadratic) approximation; it is a valid description of uncertainty, even for 8 values that are far below 8max. Second, this set might not be symmetric around the maximumlikelihood point, reflecting the fact the statistical uncertainty depends on the direction. Finally, by construction, it excludes matrices that are not transition matrices; the same cannot be said of the more classical ellipsoidal approximations. To apply the robust recursion, we need to assume that 
the uncertainty set ! possesses the rectangular uncertainty property. The likelihood region defined in (38) does not have this property, but we can overapproximate this region by a set that does, by projecting the likelihood regions onto
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 789 
n-dimensional subspaces, corresponding to the rows of the transition matrix. This overapproximation will result in an upper bound on our optimal control problem, as we are giving more power to nature. Note that this method yields a tighter approximation than that obtained via an interval matrix model, which would require a further overapproximation of the projected sets !i, by n-dimensional boxes. Due to the separable nature of the log-likelihood func-
tion, the projection of the above set onto the pi (i.e., row) variables of matrix P can be given explicitly, as 
!i'8i( #= ) 
p "!n# " 
j 
fi'j( logpi'j(! 8i 
* 
) 
where 
8i #= 8% " 
k *=i 
" 
j 
F 'k) j( logF 'k) j(* 
We are now ready to attack problem (17) under the premise that the transition matrix is only known to lie in the rectangular set 
$n i=1!i'8i(. The inner problem is to 
solve an optimization problem of the form 
&( #=max p 
pT v# p "!n) " 
j 
f 'j( logp'j(! 8) (39) 
where we have dropped the subscript i in the empirical frequencies vector fi and in the lower bound 8i. In this section, 8max denotes the maximal value of the likelihood function appearing in the above set, which is 8max = + 
j f 'j( log f 'j(. We assume that 8<8 max, which, together with f > 0, ensures that the set above has nonempty interior. Without loss of generality, we can assume that v "Rn 
+. 
5.2. The Dual Problem 
The Lagrangian '# Rn#Rn#R#R'R associated with the inner problem can be written as 
''v)9):);(=pT v+9T p+:'1%pT 1(+;'f T logp%8() 
where 9 , :, and ; are the Lagrange multipliers. The Lagrange dual function d# Rn # R # R ' R is the maximum value of the Lagrangian over p, i.e., for 9 " Rn, : "R, and ; "R, 
d'9):);(=sup p ''v)9):);( 
=sup p 
' 
pT v+9T p+:'1%pT 1(+;'f T logp%8( ( 
* 
(40) 
The optimal p( = arg supp''v) 9):);( is readily be obtained by solving <'/<p= 0, which results in 
p('i(= ;f 'i( 
:% v'i(% 9'i( * 
Plugging the value of p( in the equation for d'/):);( yields, with some simplification, the following dual problem: 
/& #= min ;):) 9 
:% '1+8(;+; " 
j 
f 'j( log ;f 'j( 
:% v'j(% /'j( # 
;! 0) 9 ! 0) 9 + v":1* 
Because the above problem is convex, and has a feasible set with nonempty interior, there is no duality gap, that is, &( = /& . Moreover, by a monotonicity argument, we obtain that the optimal dual variable 9 is zero, which reduces the number of variables to two: 
&( =min ;): 
h';):() 
where 
h';):( #= 
, 
-
-
-
. 
-
-
-
/ 
:% '1+8(;+; " 
j f 'j( log 
;f 'j( 
:% v'j( if ;> 0) :> vmax #=max 
j v'j() 
+& otherwise. 
(41) 
For further reference, we note that h is twice differentiable on its domain, and that its gradient is given by 
=h';):(= 
0 
1 
1 
1 
1 
2 
" 
j 
f 'j( log ;f 'j( 
:% v'j( %8 
1%; " 
j 
f 'j( 
:% v'j( 
3 
4 
4 
4 
4 
5 
* (42) 
5.3. A Bisection Algorithm 
From the expression of the gradient obtained above, we obtain that the optimal value of ; for a fixed :, ;':(, is given analytically by 
;':(= ! 
" 
j 
f 'j( 
:% v'j( 
#%1 
) (43) 
which further reduces the problem to a one-dimensional problem: 
&( = min :!vmax 
&':() 
where vmax = maxj v'j( and &':( = h';':():(. By construction, the function &':( is convex in its (scalar) argument, because the function h defined in (41) is jointly convex in both its arguments (see Boyd and Vandenberghe 2004, p. 74). Hence, we may use bisection to minimize & . To initialize the bisection algorithm, we need upper and 
lower bounds :% and :+ on a minimizer of & . When :' vmax, &':( ' vmax and & 0':( ' %& (see Appendix B). Thus, we may set the lower bound to :% = vmax.
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 790 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
The upper bound :+ must be chosen such that & 0':+(> 0. We have 
& 0':(= <h 
<: ';':():(+ <h 
<; ';':():( 
d;':( 
d: * (44) 
The first term is zero by construction, and d;':(/d:> 0 for :>v max. Hence, we only need a value of : for which 
<h 
<; ';':():(= 
" 
j 
f 'j( log ;':(f 'j( 
:% v'j( %8> 0* (45) 
By convexity of the negative log function, and using the fact that f T 1= 1, f ! 0, we obtain that 
<h 
<; ';':():(= 8max %8+ 
" 
j 
f 'j( log ;':( 
:% v'j( 
! 8max %8% log ! 
" 
j 
f 'j( :% v'j( 
;':( 
# 
! 8max %8+ log ;':( 
:% v̄ ) 
where v̄= f T v denotes the average of v under f . The above, combined with the bound on ;':(: ;':(! 
:% vmax, yields a sufficient condition for (45) to hold: 
:>: 0 + #= vmax % e8%8max v̄ 
1% e8%8max * (46) 
By construction, the interval 4vmax): 0 +5 is guaranteed to 
contain a global minimizer of & over 'vmax)+&(. The bisection algorithm is as follows: Step 1. Set :% = vmax and :+ =:0 
+ as in (46). Let 3> 0 be a small convergence parameter. Step 2. While :+ %:% > 3'1+:% +:%(, repeat (a) Set := ':+ +:%(/2. (b) Compute the gradient of & at :. (c) If & 0':(> 0, set :+ =:; otherwise, set :% =:. (d) go to 2a. 
In practice, the function to minimize may be very “flat” near the minimum. This means that the above bisection algorithm may take a long time to converge to the global minimizer. Because we are only interested in the value of the minimum (and not of the minimizer), we may modify the stopping criterion to 
:+ %:% " 3'1+:% +:%( or & 0':+(%& 0':%(" 3* 
The second condition in the criterion implies that 
!& 0'':+ +:%(/2(!" 3) 
which is an approximate condition for global optimality. 
5.4. Complexity 
Let us analyze the number of iterations needed to achieve a given accuracy on the optimal value &(. We denote by :( a minimizer of the function and by :+, :% the final iterates of the bisection algorithm, run with convergence parameter 3. We then have :+%:% " 3'1+ 2:0 
+(, which implies 
0":+%:(":+%:%"3 
! 
1+ 2vmax 
1%e8%8max 
# 
=O'vmax3(* 
The number of iterations needed to achieve the above bound on the minimizer :( grows as log'':0 
+%vmax(/3(= O'log'vmax/3((. Thus, to achieve an accuracy 3 in the minimizer, we need O'log'vmax/3(( iterations. Here, we are not interested in the value of a mini-
mizer :(, but on the minimum value, &(. By construction, :+ ! :(, and we have 0 " & 0':+( " lim:'+& & 0':( = 8max%8. Furthermore, we have 0":+%:( ":+%:% " 
O'vmax3(. By convexity, 
&':+(! &( ! &':+(% ':+ %:((& 0':+( 
= &':+(%O'vmax3(* 
We obtain that, to achieve a given accuracy 3 on &(, we need O'log'vmax/3(( iterations of the bisection algorithm. Because each iteration requires n flops, the total complexity of the inner problem is O'n log'vmax/3((. 
5.5. Maximum A Posteriori Models 
We now consider a variation on the likelihood model, the maximum a posteriori (MAP) model. The MAP estimation framework provides a way of incorporating prior information in the estimation process. This is particularly useful for dealing with sparse training data, for which the maximumlikelihood approach may provide inaccurate estimates. The MAP estimator, denoted by pMAP, maximizes the “MAP function” (Siouris 1995) 
LMAP'p(= L'p(+ loggprior'p() 
where L'p( is the log-likelihood function, and gprior refers to the a priori density function of the parameter vector p. In our case, p is a row of the transition matrix, so a 
prior distribution has support included in the n-dimensional simplex "p# p! 0) pT 1= 1$. It is customary to choose the prior to be a Dirichlet distribution (Ferguson 1974, Wilks 1962), the density of which is of the form 
gprior'p(=K · 6 
i 
p>i%1 i ) 
where the vector > ! 1 is given and K is a normalizing constant. Choosing > = 1, we recover the “noninformative prior,” which is the uniform distribution on the n-dimensional simplex. In that case, the MAP estimation converges to the maximum-likelihood estimation. Hence,
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 791 
the MAP estimation is a more general framework and the maximum-likelihood estimation is a specialization of the MAP when prior information is not available. The resulting MAP estimation problem takes the form 
max p 
'f +>% 1(T logp# pT 1= 1) p! 0* 
To this problem, we can associate a MAP region that describes the uncertainty on the estimate, via a lower bound 8 on the function LMAP'p(. The inner problem now takes the form 
& #=max p 
pT v# p! 0) pT 1= 1) 
" 
j 
'f 'j(+>'j(% 1( logp'j(! ?) 
where ? depends on the normalizing constant K appearing in the prior density function and on the chosen lower bound on the MAP function, 8. We observe that this problem has exactly the same form as in the case of the likelihood function, provided we replace f by f + >% 1. Therefore, the same results apply to the MAP case. 
6. Entropy Models 
6.1. Model Description 
We consider problem (17), with the uncertainty on the ith row of the transition matrix Pa described by a set of the form ! = "p " !n# D'p-q( " 8$, where 8 > 0 is fixed, q > 0 is a given distribution, and D'p-q( denotes the Kullback-Leibler divergence from q to p: 
D'p-q( #= " 
j 
p'j( log p'j( 
q'j( * 
Together with q > 0, the condition 8 > 0 ensures that ! has nonempty interior. (As before, we have dropped the control and row indices a and i.) Note that both the likelihood and entropy models can be 
interpreted in terms of an upper bound on the Kullback-Leibler divergence between two distributions. In the likelihood setting, we impose an upper bound on the divergence D'f -p(, from the (unknown) distribution p to the observed distribution f ; in the entropy case, we use an upper bound on the divergence from the reference distribution q to the unknown distribution p. This parallel suggests a heuristic to choose the uncertainty level 8 by following the same guidelines used in the likelihood setting, as described in Appendix D. We now address the inner problem (17), with ! given 
above. We note that ! actually equals the whole probability simplex if 8 is too large, specifically if 8!maxi'% logqi(, because the latter quantity is the maximum of the relative entropy function over the simplex. Thus, if 8 ! 
maxi'% logqi(, the worst-case value of pT v for p " ! is equal to vmax #=maxj v'j(. 
6.2. Dual Problem 
By standard duality arguments (set ! being of nonempty interior), the inner problem is equivalent to its dual: 
min ;>0): 
:+8;+; " 
j 
q'j( exp ! 
v'j(%: 
; % 1 
# 
* 
Setting the derivative with respect to : to zero, we obtain the optimality condition 
" 
j 
q'j( exp ! 
v'j(%: 
; % 1 
# 
= 1) 
from which we derive 
:= ; log ! 
" 
j 
q'j( exp v'j( 
; 
# 
%;* 
The optimal distribution is 
p( = q'j( exp'v'j(/;( + 
i q'i( exp'v'i(/;( * 
As before, we reduce the problem to a one-dimensional problem 
min ;>0 
&';() 
where & is the convex function 
&';(= ; log ! 
" 
j 
q'j( exp v'j( 
; 
# 
+8;* (47) 
Perhaps not surprisingly, the above function is closely linked to the moment-generating function of a random variable v having the discrete distribution with mass qi at vi. 
6.3. Bisection Algorithm 
As proved in Appendix C, the convex function & in (47) has the following properties: 
.;! 0) qT v+8;" &';(" vmax +8; (48) 
and 
&';(= vmax + '8+ logQ'v((;+ o';() (49) 
where 
Q'v( #= " 
j#v'j(=vmax 
q'j(= Prob"v= vmax$* 
Hence, &'0(= vmax and & 0'0(= 8+ logQ'v(. In addition, at infinity the expansion of & is 
&';(= qT v+8;+ o'1(* (50) 
The bisection algorithm can be started with the lower bound ;% = 0. An upper bound can be computed by finding a solution to the equations &'0(= qT v+8;, which yields
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 792 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
the initial upper bound ;0 + = 'vmax%qT v(/8. By convexity, 
a minimizer exists in the interval 40 ;0 +5. 
Note that if & 0'0( ! 0, then ; = 0 is optimal and the optimal value of & is vmax. This means that if 8 is too high, that is, if 8>% logQ'v(, enforcing robustness amounts to disregard any prior information on the probability distribution p. We have observed in §6.1 a similar phenomenon brought about by too large values of 8, which resulted in a set ! equal to the probability simplex. Here, the limiting value % logQ'v( depends not only on q but also on v, because we are dealing with the optimization problem (17) and not only with its feasible set !. 
6.4. Complexity 
The complexity analysis for the entropy model follows the same lines as that of the likelihood model, so we will be brief here. First, we note that the number of iterations needed to obtain a given accuracy 3 on the minimizer is O'log'vmax/3(( iterations, because ;0 
+ =O'vmax(. To obtain a given accuracy on the minimum value, the important feature is to ensure that the derivative of the function & is bounded uniformly and independent of problem size n, at least on one side of the optimum. In the entropy case, we have at each step of the bisection algorithm 0" & 0':+(" lim:'+& & 0':( = 8. We obtain that, to achieve a given accuracy 3 on &(, we need O'log'vmax/3(( iterations of the bisection algorithm. Because each iteration requires n flops, the total complexity of the inner problem in the entropy case is again O'n log'vmax/3((. 
7. Other Uncertainty Models 
7.1. Finite Scenario Model 
Perhaps the simplest uncertainty model involves a finite collection of transition matrices, where for every a " #, !a = "Pa)1) * * * )!a)L$, with Pa)k "%n representing a possible value (scenario) of the transition matrix. As noted earlier, the robust Bellman recursion applies to nonconvex uncertainty sets !a, as long as they satisfy the rectangular uncertainty property, which is certainly the case here. Note that the scenario model gives rise to the same optimal robust policy as when the finite set !a above is replaced by a product of convex hulls: 
$n i=1 conv"p 
a)1 i ) * * * )pa)L 
i $, where pa)k 
i denotes the ith row of matrix Pa)k. Under the scenario (or polytopic) model, the inner prob-
lem (17) bears a particularly simple form: 
&!a i 'v(= max 
p""pa)1i )***)pa)Li $ vT p= max 
1"k"L ) vT pa)k 
i * 
The worst-case complexity of each step of the robust Bellman recursion is then O'mnL(, where L is the number of vertices. For moderately large values of L, the scenario model is attractive, due to its simplicity of implementation. 
7.2. Interval Matrix Model 
The interval matrix model describes the uncertainty on the rows of the transition matrices in the form 
! = "p# p" p" 1p) pT 1= 1$) 
where 1p, p are given componentwise nonnegative n-vectors (whose elements do not necessarily sum to one), with 1p! p. Note that for Theorem 1 to hold, we must ensure that the set ! is entirely included in the probability simplex !n, which we did by assuming p ! 0. This model is motivated by statistical estimates of intervals of confidence on the components of the transition matrix. Those intervals can be obtained by resampling methods, or by projecting an ellipsoidal uncertainty model on each component axis (see §7.3). Because 1p! p, ! is not empty. Because the inner problem 
&( #=max p 
vT p# pT 1= 1) p" p" 1p 
is a linear, feasible program, it is equivalent to its dual, which can be reduced to 
&( =min : 
'1p%p(T ':1% v(+ + vT 1p+:'1% 1pT 1() 
where z+ stands for the positive part of vector z. The function to be minimized is a convex piecewise linear function with break points v'0( #= 0 and v'1() * * * )v'n(. Because the original problem is feasible, we have 1T p" 1, which implies that the function above goes to infinity when :'&. Thus, the minimum of the function is attained at one of the break points v'i( 'i= 0) * * * )n(. The complexity of this enumerative approach is O'n2(, because each evaluation costs O'n(. In fact, one does not need to enumerate the function at all values vi; a bisection scheme over the discrete set "v0) * * * )vn$ suffices. This scheme will bring the complexity down to O'n logn(. 
7.3. Ellipsoidal Models 
Ellipsoidal models arise when second-order approximations are made to the log-likelihood function arising in the likelihood model. Specifically, we work with the following set in lieu of (38): 
!'8(= % 
P "Rn#n# P ! 0) P1= 1) Q'P (! 8 & 
) (51) 
where Q'P ( is the second-order approximation to the log-likelihood function L, around the maximum-likelihood estimate F : 
Q'P ( #= 8max % 1 2 
" 
i) j 
'P 'i) j(% F 'i) j((2 
F 'i) j( * 
The above set is an ellipsoid intersected by the polytope of transition matrices. Again, to ensure the rectangular uncertainty property, we first form the projections on the space
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 793 
of ith row variables. These assume a similar shape, that of an ellipsoid intersected with the probability simplex, specifically, 
!i'8(= ) 
p# p! 0) pT 1= 1) " 'pi'j(% fi'j(( 
2 
fi'j( " ?2 
* 
) 
where ?2 #= 2'8max % 8(. We refer to the above model as the constrained ellipsoidal model. In the constrained likelihood case, the inner problem 
assumes the form 
max p 
vT p# p! 0) pT 1= 1) " 'p'j(% f 'j((2 
f 'j( " ?2* 
Using an interior-point method (Boyd and Vandenberghe 2004), the above problem can be solved with absolute accuracy 0 in worst-case time of O'n1*5 log'vmax/0((, and with a practical complexity of O'n log'vmax/0((. In statistics, it is a standard practice to further simplify 
the description above, by relaxing the inequality constraints P ! 0 in the definition of !'8(. This would bring down the worst-case complexity to O'n log'vmax/0((. However, if sign constraints are omitted, Theorem 1 does not necessarily hold, and we would only compute an upper bound on the value of the problem. 
8. Example: Robust Aircraft Routing We consider the problem of routing an aircraft whose path is obstructed by stochastic obstacles, representing storms. In practice, the stochastic model must be estimated from past weather data. This makes this particular application a good illustration of our method. 
8.1. The Nominal Problem 
In Nilim et al. (2001), we introduce an MDP representation of the problem, in which the evolution of the storms is modelled as a perfectly known stationary Markov chain. The term nominal here refers to the fact that the transition matrix of the Markov process corresponding to the weather is not subject to uncertainty. The goal is to minimize the expected delay (flight time). The weather process is a fully observable Markov chain: At each decision stage (every 15 minutes in our example), we learn the actual state of the weather. The air space is represented as a rectangular grid. The 
state vector comprises the current position of the aircraft on the grid, as well as the current states of each storm. The action in the MDP corresponds to the choice of nodes to fly towards, from any given node. There are k obstacles, represented by a Markov chain with a 2k # 2k transition matrix. The transition matrix for the routing problem is thus of order N2k, where N is the number of nodes in the grid. We solved the MDP via the Bellman recursion (Nilim 
et al. 2001). Our framework avoids the potential “curse of dimensionality” inherent in generic Bellman recursions, 
by considerable pruning of the state space and action sets. This makes the method effective for up to a few storms, which corresponds to realistic situations. For more details on the nominal problem and its implementation, we refer the reader to Nilim et al. (2001). In the example below, the problem is two-dimensional 
in the sense that the aircraft flies at a fixed altitude. In a coordinate system where each unit is equal to 1 nautical mile, the aircraft is initially positioned at '0)0( and the destination point is at '360)0(. The velocity of the aircraft is fixed at 480 n.mi/hour. The air space is described by a rectangular grid with N = 210 nodes, with edge length of 24 n.mi. There is a possibility that a storm might obstruct the flight path. The storm zone is a rectangular space with the corner points at '160)192(, '160)%192(, '168)192(, and '168)%192( (Figure 1). Because there is only one potential storm in the 
area, storm dynamics is described by a 2 # 2 transition matrix Pweather. Together with N = 210 nodes, this results in a state space of total dimension 420. By limiting the angular changes in the heading of the aircraft, we can prune out the action space and reduce its cardinality at each step tom= 4. This implies that the transition matrices are very sparse; in fact, they are sparse, affine functions of the transition matrix Pweather. Sparsity implies that the nominal Bellman recursion only involves 8 states at each step. 
8.2. The Robust Version 
In practice, the transition matrix Pweather is estimated from past weather data, and thus it is subject to estimation errors. We assumed a likelihood model of uncertainty on this 
transition matrix. This results in a likelihood model of uncertainty on the state transition matrix, which is as sparse as the nominal transition matrix. Thus, the effective state pruning that takes place in the nominal model can also take 
Figure 1. Aircraft path planning scenario. 
-50 0 50 100 150 200 250 300 350 400 -200 
-150 
-100 
-50 
0 
50 
100 
150 
200 
Stochastic obstacle 
Origin Destination 
Nautical miles 
N au 
tic al 
 m ile 
s
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 794 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
Figure 2. %8 (negative lower bound on the log-likeli-hood function) vs. UL (uncertainty level in % of the transition matrices). 
0.6 0.8 1 1.2 1.4 1.6 1.8 2 2.2 2.4 2.6 0 
10 
20 
30 
40 
50 
60 
70 
80 
90 
U L 
!! 
place in the robust counterpart. In our example, we chose the numerical value 
Pweather = ! 
0*9 0*1 0*1 0*9 
# 
for the maximum-likelihood estimate of Pweather. The likelihood model involves a lower bound 8 on the 
likelihood function, which is a measure of the uncertainty level. Its maximum value 8max corresponds to the case with no uncertainty, and decreasing values of 8 correspond to a higher uncertainty level. To 8, we may associate a measure of uncertainty that is perhaps more readable: The uncertainty level, denoted by UL, is defined as a percentage and its complement 1%UL can be interpreted as a probabilistic confidence level in the context of large samples. The one-to-one correspondence of UL and 8 is precisely described in Appendix D. In Figure 2, we plot UL against decreasing values of the 
lower bound on the log-likelihood function (8). We see that UL = 0, which refers to a complete certainty of the data, is attained at 8= 8max, the maximum value of the likelihood function. The value of UL decreases with 8 and reaches the maximum value, which is 100%, at 8=%& (not drawn in this plot). Point to be noted: The rate of increase of UL is maximum at 8= 8max and increases with 8. 
8.3. Comparing Robust and Nominal Strategies 
In Figure 3, we compare various strategies: We plot the relative delay, which is the relative increase (in percentage) in flight time with respect to the flight time corresponding to the most direct route (straight line), against the negative of the lower bound on the likelihood function 8. We compare three strategies. The conservative strategy 
is to avoid the storm zone altogether. If we take 8= 8max, 
the uncertainty set becomes a singleton 'UL = 0( and hence we obtain the solution computed via the classical Bellman recursion; this is referred to as the nominal strategy. The robust strategy corresponds to solving our robust MDP with the corresponding value of 8. The plot in Figure 3 shows how the various strategies 
fare, as we decrease the bound on the likelihood function 8. For the nominal and the robust strategies, and a given bound 8, we can compute the worst-case delay using recursion (10), which provides the worst-case value function. The conservative strategy incurs a 51.5% delay with 
respect to the flight time corresponding to the most direct route. This strategy is independent of the transition matrix, so it appears as a straight line in the plot. If we know the value of the transition matrix exactly, then the nominal strategy is extremely efficient and results in a delay of 8.02% only. As 8 deviates from 8max, the uncertainty set gets bigger. In the nominal strategy, the optimal value is very sensitive in the range of values of 8 close to 8max: the delay jumps from 8% to 25% when 8 changes by 7.71% with respect to 8max (the uncertainty level UL changes from 0% to 5%). In comparison, the relative delay jumps by only 6% with the robust strategy. In both strategies, the slope of the optimal value with respect to the uncertainty is almost infinite at 8= 8max, which shows the high sensitivity of the value function with respect to the uncertainty. We observe that the robust solution performs better than 
the nominal solution as the estimation error increases. The plot shows an average of 19% decrease in delay with respect to the nominal strategy when uncertainty is present. Further, as the uncertainty level increases, the nominal strategy very quickly reaches delay values comparable to those obtained with the conservative strategy. In fact, the conservative strategy even outperforms the nominal strategy at 8=%1*84, which corresponds to UL = 69*59%. In this sense, even for moderate uncertainty levels, the nominal 
Figure 3. Optimal value vs. uncertainty level (negative lower bound on the log-likelihood function) for the classical Bellman recursion and its robust counterpart. 
0.5 1 1.5 2 2.5 0 
10 
20 
30 
40 
50 
60 
Robust strategy 
Nominal strategy 
Conservative strategy 
UL = 0 % UL = 50% UL = 80% 
R el 
at iv 
e de 
la y 
(i n 
% ) 
!!
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 795 
Figure 4. Optimal value vs. uncertainty level (negative lower bound on the log-likelihood function) for the classical Bellman recursion and its robust counterpart (with exact and inexact predictions of the uncertainty level UL). 
0.5 1 1.5 2 2.5 0 
10 
20 
30 
40 
50 
60 Nominal strategy 
Robust strategy (exact guess) 
Robust strategy (inexact guess) 
U0 L = 15 % U0 
L = 55% 
R el 
at iv 
e de 
la y 
(i n 
% ) 
!! 
strategy defeats its purpose. In contrast, the robust strategy outperforms the conservative strategy by 15% even if the data is very uncertain 'UL = 85%(. 
In summary, when there is no error in the estimation, both nominal and robust algorithms provide a strategy that produces 43.3% less delay than the conservative strategy. However, with the presence of even a moderate estimation error, the robust strategy performs much better than the conservative strategy, whereas the nominal MDP strategy cannot produce a much better result. Nominal and robust strategies have similar computa-
tional requirements. In our example, with a simple Matlab implementation on a standard PC, the running time for the nominal algorithm was about four seconds, and the robust version took on average four more seconds to solve. 
8.4. Inaccuracy of Uncertainty Level 
The previous comparison assumes that in the robust case, we are able to estimate exactly the precise value of the uncertainty level UL (or the bound on the likelihood function 8). In practice, this parameter also has to be estimated. Hence the question: How sensitive is the robust approach with respect to inaccuracies in the uncertainty level UL? To answer this question in our particular example, we 
have assumed that a guess U 0 L on the uncertainty level is 
available, and examined how the corresponding robust solution would behave if it was subject to uncertainty with level above or below the guess. In Figure 4, we compare various strategies. In each strat-
egy, we guess a desired level of accuracy 'U 0 L( on the 
data and calculate a corresponding likelihood bound 80. We choose the optimal action using our robust MDP algorithm applied with this bound. Keeping the resulting policy fixed, we then compute the relative delay with the various values of 8. In Figure 4, we plot the relative delays against %8 
for the strategies where the uncertainty levels were guessed as 15% and 55%. Not surprisingly, the relative delay of a strategy attains 
its minimum value when 8 'UL( is accurately predicted. For values of 8 above or below its guessed value, the delay increases. We note that it is only for very small uncertainty levels (within 0.995% of 8max) that the nominal strategy performs better than the robust strategy with imperfect prediction of 8 'UL(. We define RUL 
as the range of the actual UL in percentage terms, where the robust strategy (with imperfect prediction of UL) performs worse than nominal strategy. In Figure 5, we show RUL 
against the guessed value, U 0 L . 
The plot clearly shows that RUL remains less than 1% with 
varying predicted U 0 L . 
Our example shows that if we predict the uncertainty level inaccurately to obtain a robust strategy, the nominal strategy will outperform the robust strategy only if the actual uncertainty level UL is less than 1%. For any higher value of the uncertainty level, the robust strategies outperform the nominal strategy by an average of 13%. Thus, even if the uncertainty level is not accurately predicted, the robust solution outperforms the nominal solution significantly. 
9. Concluding Remarks We have considered a robust Markov decision problem with uncertainty models for the transition matrices that are statistically accurate, yet give rise to very moderate extra computational effort for computing a robust solution, with respect to a nominal solution, where uncertainty is ignored. Specif-ically, the relative increase in computational cost is of order 
Figure 5. Predicted uncertainty level U 0 L vs. RUL 
, which is the range of the actual uncertainty level UL over which the nominal strategy performs better than a robust strategy computed with the imperfect prediction U 0 
L . 
0 10 20 30 40 50 60 0 
0.1 
0.2 
0.3 
0.4 
0.5 
0.6 
0.7 
0.8 
0.9 
1.0 
R U 
L (i n 
% ) 
Predicted uncertainty level UL 0
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 796 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
O'log'N/0(( in the finite-horizon case, and O'log'1/0(( in the infinite-horizon case, where 0 is the desired accuracy on the optimal expected total cost. As a result, the robust algorithm has practically the same complexity as that of the nominal problem. We have considered both stationary and time-varying assumptions about uncertainty, and showed that as the decision horizon goes to infinity, the gap between these two models vanishes. This justifies our use of bounds based on stationarity assumptions, even if we allow time-varying changes in the transition matrices. The statistical accuracy of our uncertainty models is derived from the fact that they use the Kullback-Leibler divergence, which is a natural way to measure errors in the transition matrices. The other models we have considered, from the polytopic to the interval to the ellipsoidal model, do not enjoy such properties, and moreover, give rise to larger worst-case complexity estimates. We have shown in a practical path planning example the 
benefits of using a robust strategy instead of the classical optimal strategy; even if the uncertainty level is only crudely guessed, the robust strategy yields a much better worst-case expected flight delay. 
Appendix A. Stochastic Game-Theoretic Proof of the Robust Bellman Recursion In this section, we prove that the stochastic game with perfect information (4) can be solved using the robust Bellman recursion (7). Our proof is based on transforming the original problem into a term-based zero-sum game, and applying a result by Nowak (Altman et al. 2000, Altman and Hordijk 1994, Nowak 1984) that applies to such games. We begin by augmenting the state space " with states 
of the form 'i)a(, where i "" and a "#. The augmented state space is thus " aug #= " 2 '" # #(. We now define a new two-player game on this augmented state space, where decisions are taken not only at time t, t " T = "0)1) * * * )N$ , but also at intermediate times t+1/2, t " T . In the first step, from t to t+ 1/2, if the system is in a 
state of the form i, a deterministic at results in a transition to the state 'i)at( with probability one, and the incurred cost is the cost of the original problem, ct'i)at(. If the system is in a state of the form 'i)at(, then the controller is not allowed to choose any action and the states stay the same with probability one; the incurred cost in this case is zero. Randomized actions of the controller can be described by a probability measure q " !m (the probability simplex in Rm). In the first step, the opponent is idle. In the second step, from t+ 1/2 to t+ 1, the controller 
stands idle while the opponent acts as follows. The states of the form 'i)a( make a transition to states of the form j with probability pa 
i 'j(, where pa i is freely chosen by the 
opponent from the set !a i . If the system is at any state of 
the form i at t + 1/2, it remains at the same state with probability one. There is no cost incurred at this stage. Clearly, starting at time t in state i, and with a controller 
action a, we end up in the state j at time 't + 1( with 
probability pa i 'j(. Because incurred costs are the same, our 
new game is equivalent to the original game. In addition, the new game is a term-based zero-sum game, because the controller and the opponent act alternatively, in an independent fashion at each time step. Note that the rectangular uncertainty property is crucial here, as it ensures the fact that the opponent is free to chose pa 
i in the set !a i . 
Nowak’s result provides a Bellman-type recursion to solve the problem of minimizing the worst-case (maximum) expected cost of a term-based zero-sum game, when both players follow randomized policies that are restricted to given state-dependent compact subsets of the probability simplex. In our new game, the opponent’s choice of a vector pa 
i within !a i at the second step, can be interpreted 
as a choice of a randomized policy over the compact, convex, state-dependent set (''i)a(( #= conv'!a 
i ), the convex hull of the set !a 
i . This ensures that the set of transition measures is convex. (Here, the deterministic actions of the opponent correspond to the vertices of the probability simplex of Rn.) Hence, the results due to Nowak (1984) apply. In the case when both of the players choose the ran-
domized, state-independent actions, the recursion for the optimal value function vk in state s can be written for k= 0)1/2)1) * * * )N % 1/2, as 
vk's(= min q"!m 
max b"('s( 
Eqb'ck's)a)b(+ vk+1/2's 0(( 
. s0 "" aug) (52) 
where the notation ck is the cost function, q refers to a particular randomized action of the controller that is freely chosen by the controller from !m, b refers to a particular randomized action that is freely chosen by the opponent within the state-dependent compact set ('s(= conv'!a 
i (, and Eqb is the corresponding expectation operator with respect to the product measure q3b. The boundary condition of the game is vN 's(= cN 's( . s " " 4 " aug. Due to the sequential nature of the game, (52) can be rewritten as 
vk's(= min q"!m 
Eq 
7 
ck's)a)b(+ max b"('s( 
Eb'vk+1's 0(( 
8 
* (53) 
Because, Eb'vk+1( is a linear function of the measure b, it can be easily shown that 
max b"('s(=conv'!a 
i ( Eb'vk+1(=max 
b"!a i 
Eb'vk+1(* (54) 
Let us detail how applying the above recursion to our game yields our result. We first update this value function by appropriately 
choosing the value of k that corresponds to the time t+1 to t+ 1/2. The controller is idle, but the opponent is allowed to chose a randomized policy from a state-dependent compact set. If the state is 'i)a(, using (54), the set is !a 
i , and the value function is updated as 
vt+1/2''i)a((=max p"!a 
i 
! n " 
j=1 
p'j(vt+1'j( 
# 
) (55)
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices Operations Research 53(5), pp. 780–798, © 2005 INFORMS 797 
where we make use of the fact that incurred costs are zero in this step. To update the value function from t+1/2 to t, we use the fact that the opponent is idle. For i= 1) * * * )n, the value function is updated as 
vt'i(= min q"!m 
Eq 
' 
ct'i)a(+ vt+1/2''i)a(( ( 
* (56) 
The right-hand side of (56) is a linear program in variable q. Thus, the optimal value is obtained at the vertices of the feasible set !m, which correspond to purely deterministic actions. Hence, 
vt'i(=min a"# 
' 
ct'i)a(+ vt+1/2''i)a(( ( 
* (57) 
Combining (55) and (57) ends our proof. 
Appendix B. Properties of Function ! of §5.3 Here, we prove two properties of the function & involved in the bisection algorithm of §5.3. For simplicity of notation, we assume that there is an unique index i( achieving the maximum in vmax, that is, v'i((= vmax. We first show that &':(' vmax as :' vmax. We have 
;':(= :% v'i(( 
f 'i(( + o':% v'i(((* 
We then express &':( as 
&':(=:%;':( 
! 
1+8%8max + log;':( 
% " 
j *=i( fj log':% vj( 
# 
%;':(f 'i(( log':% v'i(((* 
The second term (first line) vanishes as :' vmax, because ;':(' 0. In view of the expression of ;':( above, the last term (second line) behaves as ':% v'i((( log':% v'i(((, which also vanishes. Next, we prove that & 0':( ' %& as : ' vmax. We 
obtain easily 
d;':( 
d: = 
+ 
j'f 'j(/':% v'j((2( ' + 
j 
' 
f 'j(/':% v'j(( ((2 ' 
1 f 'i(( 
when :' v'i((* 
We then have <h 
<; ';':():( = 
" 
j 
log ;':(f 'j( 
:% v'j( %8 
= log ;':(f 'i(( 
:% v'i(( + 
" 
j *=i( log 
;':(f 'j( 
:% v'j( %8 
= log'1+ o'1((+ 'n% 1( log;':( 
+ " 
j *=i( log 
f 'j( 
:% v'j( %8 
'%& as :' v'i((* 
Also, by definition of ;':(, we have <h/<:';':():(= 0. The proof is achieved with the identity (44). 
Appendix C. Properties of Function ! of §6.3 In this section, we prove that the function & defined in (47) obeys properties (48), (49), and (50). First, we prove (49). If v'j(= vmax for every j , the result 
holds, with Q'v( = Q'vmax1( = 1. Assume now that there exists j such that v'j(< vmax. We have 
&';(= ; log ! 
evmax/; " 
j 
q'j( exp ! 
v'j(% vmax 
; 
## 
+8; 
= vmax +8;+; log ! 
" 
j#v'j(=vmax 
q'j( 
+ " 
j#v'j(<vmax 
q'j( exp ! 
v'j(% vmax 
; 
## 
= vmax +8;+; log'Q+O'e%t/;(( 
= vmax + '8+ logQ(;+O';e%t/;() 
where t = vmax%vs > 0, where vs is the largest v'j(< vmax. This proves (49). From the expression of & given in the second line above, 
we immediately obtain the upper bound in (48). The expansion of & at infinity provides 
&';(= 8;+; log ! 
" 
j 
q'j( 
! 
1+ v'j( 
; + o';( 
## 
= qT v+8;+ o'1() 
which proves (50). The lower bound in (48) is a direct consequence of the concavity of the log function. 
Appendix D. Calculation of " for a Desired Confidence Level In this section, we describe a one-to-one correspondence between a lower bound on the log-likelihood function 8, as used in §5, and a desired level of confidence '1%UL( on the transition matrix estimates, as used in §8. This correspondence is valid for asymptotically large samples only but can serve as a guideline to choose 8. The following material is standard; see, for instance, Lehmann (1986). First, we define a vector 7 "Rn'n%1( that contains the first 
n%1 columns to be estimated in a n#n transition matrix P . We order 7 so that P 'i) j(= 7''n% 1('i% 1(+ j( for 1" i " n, 1 " j " 'n% 1(. Using the conditions P1 = 1, we can write P as an (affine) function of 7, and express the log-likelihood function L'P ( of (37) as a function l'7(. Let ,7 be the vector corresponding to the matrix of empirical frequencies F , that we assumed to be positive componentwise. Provided some regularity conditions hold, one can show that for asymptotically large samples, 7 is normally distributed with mean given by ,7, and inverse covariance matrix H = %E7''= 
2l('7((. Furthermore, we can approximate H by the observed information matrix +H #= %'= 2l(' ,7(. In our case, the nonzero elements of this
Nilim and El Ghaoui: Robust Control of Markov Decision Processes with Uncertain Transition Matrices 798 Operations Research 53(5), pp. 780–798, © 2005 INFORMS 
matrix are 
+H''n% 1('i% 1(+ j) 'n% 1('i% 1(+ k( 
= 
, 
-
-
-
. 
-
-
-
/ 
1 F 'i)n( 
+ 1 F 'i) j( 
if j = k) 
1 F 'i)n( 
otherwise* 
If q denotes the quadratic approximation to l around ,7, we have 
q'7(= 8max % 1 2 '7% ,7(T +H'7% ,7() 
where 8max is the maximal log-likelihood defined in §5.1. Then, the parameter 8 is chosen to be the smallest such that, under the Gaussian probability distribution ) ' ,7) +H%1(, the set "7# q'7( ! 8$ has probability larger than a given threshold '1%UL(, where (say) UL = 15% to obtain the 85% confidence level. It turns out that we can solve for such a 8 explicitly: 
'1%UL(= F@2 n'n%1( 
'2'8max %8(() (58) 
where F@2 d 
is the cumulative density function of the @2-distribution with d degrees of freedom. The latter can be approximated as follows (Pitman 1993): 
F@2 d 'A(56'z(% 
6 2 
3 6 d 'z2 % 1(.'z() (59) 
where z = 'A % d(/ 6 d, .'z( = '1/ 
6 2,(e%'1/2(z2 , and 
6'z(= 9 z 
%&.'u(du is the standard normal cumulative density function. 
Acknowledgments The authors thank Antar Bandyopadhyay, Bob Barmish, Giuseppe Calafiore, Vu Duong, Mikael Johansson, Yann Le Tallec, Rupak Majumdar, Andrew Ng, Stuart Russell, Shankar Sastry, Ben Van Roy, Michael Todd, and Pravin Varaiya for interesting discussions and comments. The authors are grateful to Dimitris Bertsimas for pointing out a mistake in an earlier version of the paper, and to Alain Haurie for his very detailed comments. They are especially thankful to the unknown reviewers whose interesting comments prompted a significant portion of this work. This research was funded in part by Eurocontrol-014692, DARPA-F33615-01-C-3150, and NSF-ECS-9983874. 
References Abbad, M., J. A. Filar. 1992. Perturbation and stability theory for Markov 
control problems. IEEE Trans. Automatic Control 37 1415–1420. 
Abbad, M., J. Filar, T. Bielecki. 1992. Algorithms for singularly perturbed limiting average Markov control problems. IEEE Trans. Automatic Control 37 1421–1425. 
Altman, E., A. Hordijk. 1994. Zero-sum Markov games and worst-case optimal control of queueing systems. QUESTA 21(Special Issue on Optimization of Queueing Systems) 415–447. 
Altman, E., E. A. Feinberg, A. Shwartz. 2000. Weighted discounted stochastic games with perfect information. Ann. Internat. Soc. Dynamic Games 5 303–323. 
Bagnell, J., A. Ng, J. Schneider. 2001. Solving uncertain Markov decision problems. Technical report CMU-RI-TR-01-25, Robotics Institute, Carnegie Mellon University, Pittsburgh, PA. 
Bertsekas, D., J. Tsitsiklis. 1996. Neuro-Dynamic Programming. Athena Scientific, Nashua, NH. 
Boyd, S., L. Vandenberghe. 2004. Convex Optimization. Cambridge University Press, Cambridge, UK. 
Epstein, L. G., M. Schneider. 2002. Learning under ambiguity. http://www. econ.rochster.edu/Faculty/Epstein.html. 
Feinberg, E., A. Shwartz. 2002. Handbook of Markov Decision Processes, Methods and Applications. Kluwer Academic Publishers, Boston, MA. 
Ferguson, T. 1974. Prior distributions on space of probability measures. Ann. Statist. 2(4) 615–629. 
Givan, R., S. Leach, T. Dean. 1997. Bounded parameter Markov decision processes. Fourth European Conf. Planning, 234–246. 
Iyengar, G. 2003. Robust dynamic programming. Technical report TR-2002-07, Columbia University, New York. 
Kalyanasundaram, S., E. Chong, N. Shroff. 2001. Markov decision processes with uncertain transition rates: Sensitivity and robust control. Technical report, Department of ECE, Purdue University, West Lafayette, IN. 
Lehmann, E. 1986. Testing Statistical Hypothesis. Wiley, New York. 
Lehmann, E., G. Casella. 1998. Theory of Point Estimation. Springer-Verlag, New York. 
Mine, H., S. Osaki. 1970. Markov Decision Processes. American Elsevier Publishing, New York. 
Nilim, A., L. El Ghaoui. 2002. Robust solution to the Markov decision processes with uncertain transition matrices. Technical report UCB/ERL M02/31, Department of Electrical Engineering and Com-puter Sciences, University of California, Berkeley, CA. 
Nilim, A., L. El Ghaoui, M. Hansen, V. Duong. 2001. Trajectory-based air traffic management (TB-ATM) under weather uncertainty. Proc. 4th USA/EUROPE ATM R&D Seminar, Santa Fe, NM, 64–72. 
Nowak, A. S. 1984. On zero sum stochastic games with general state space. I. Probab. Math. Statist. 4(1) 13–32. 
Pitman, J. 1993. Probability. Springer-Verlag, New York. 
Poor, H. 1988. An Introduction to Signal Detection and Estimation. Springer-Verlag, New York. 
Putterman, M. 1994. Markov Decision Processes: Discrete Stochastic Dynamic Programming. Wiley-Interscience, New York. 
Satia, J. K., R. L. Lave. 1973. Markov decision processes with uncertain transition probabilities. Oper. Res. 21(3) 728–740. 
Shapiro, A., A. J. Kleywegt. 2002. Minimax analysis of stochastic problems. Optim. Methods Software. 17(1) 523–592. 
Siouris, G. 1995. Optimal Control and Estimation Theory. Wiley-Interscience, New York. 
White, C. C., H. K. Eldeib. 1994. Markov decision processes with imprecise transition probabilities. Oper. Res. 42(4) 739–749. 
Wilks, S. 1962. Mathematical Statistics. Wiley-Interscience, New York.