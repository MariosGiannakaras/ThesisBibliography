> Source: https://web.mit.edu/dimitrib/www/Bertsekas_1976_dynamic-programming.pdf

Dynamic Programming and Stochastic Control 
This is Volume 125 in MATHEMATICS IN SCIENCE AND ENGINEERING A Series of Monographs and Textbooks Edited by RICHARD BELLMAN, University of Southern California 
The complete listing of books in this series is available from the Publisher upon request. 
Dynamic Programming and Stochastic Control 
DIMITRI P .  BERTSEKAS 
COLLEGE OF ENGINEERING COORDINATED SCIENCE LABORATORY UNIVERSITY OF ILLINOIS URBANA, ILLINOIS 
ACADEMIC PRESS New York San Francisco London 1976 A Subsidiary of Harcourt Brace Jovanovich, Publishers 
COPYRIGHT 0 1976, BY ACADEMIC PRESS, INC. ALL RIGHTS RESERVED. NO PART OF THIS PUBLICATION MAY BE REPRODUCED OR TRANSMITTED IN ANY FORM OR BY ANY MEANS, ELECTRONIC OR MECHANICAL, INCLUDING PHOTOCOPY, RECORDING, OR ANY INFORMATION STORAGE AND RETRIEVAL SYSTEM, WITHOUT PERMISSION IN WRITING FROM THE PUBLISHER. 
ACADEMIC PRESS, INC. 111  Fifth Avenue, New York. New York 10003 
United Kingdom Edition published by ACADEMIC PRESS, INC. (LONDON) LTD. 24/28 Oval Road. London NWI 
Library of Congress Cataloging in Publication Data 
Bertsekas, Dimitri P Dynamic programming and stochastic control. 
(Mathematics in science and engineering) Bibliography: p. 1. Dynamic programming. 2. Stochastic processes. 
I. Title. 11. Series. T5 7.8 3.B48 5 19.7’03 76-16 143 ISBN 0-12-093250-4 
PRINTED IN THE UNITED STATES OF AMERICA 
To my mother and the memory of my father 
This page intentionally left blank
Contents 
Preface 
Acknowledqrnents 
xi 
xv 
Chapter 1 Introduction 
1 . I  1.2 I .3 I .4 1.5 Notes 
The Problems of Decision under Uncertainty Expected Utility Theory and Risk Some Nonsequential Decision Problems A Model for Sequential Decision Making 
Problems 
Part I CONTROL OF UNCERTAIN SYSTEMS OVER A FINITE HORIZON 
Chapter 2 The Dynamic Programming Algorithm 
2. I The Basic Problem 2.2 The Dynamic Programming Algorithm 2.3 2.4 Notes 
Time Lags, Correlated Disturbances, and Forecasts 
Problems 
Chapter 3 Applications in Specific Areas 
3.1 
3.2 Inventory Control 3.3 Dynamic Portfolio Analysis 3.4 Optimal Stopping Problems-Examples 3.5 Notes 
Linear Systems with Quadratic Cost Functional -The Certainty Equivalence Principle 
Problems 
3 7 
18 28 33 34 
39 47 57 63 64 
70 81 89 95 
102 103 
vii 
viii CONTENTS 
Chapter 4 Problems with Imperfect State Information 
4.1 4.2 Sufficient Statistics 4.3 
4.4 4.5 4.6 4.7 Notes 
Reduction to the Perfect State Information Case 
Linear Systems with Quadratic Cost Functionals -Separation of Estimation and Control Finite State Markov Chains-A Problem of Instruction Hypothesis Testing-Sequential Probability Ratio Test Sequential Sampling of a Large Batch 
Problems Appendix Least-Squares Estimation-The Kalman Filter 
Chapter 5 Computational Aspects of Dynamic Programming -Suboptimal Control 
111 I22 
129 137 144 I49 152 153 158 
5.1 The Curse of Dimensionality 179 5.2 Discretization Procedures and Their Convergence I80 5.3 Suboptimal Controllers and the Notion of Adaptivity 191 5.4 Naive Feedback and Open-Loop Feedback Controllers 193 5.5 Partial Open-Loop Feedback Controllers and the Efficient Utilization of Forecasts 202 5.6 Control of Systems with Unknown Parameters-Self-Tuning Regulators 207 5.7 Notes 214 
Problems 215 
Part I1 CONTROL OF UNCERTAIN SYSTEMS OVER AN INFINITE HORIZON 
Chapter 6 Minimization of Total Expected Value-Discounted Cost 
6.1 6.2 
6.3 6.4 6.5 6.6 6.7 6.8 
Convergence and Existence Results 225 Computational Methods-Successive Approximation, Policy Iteration, Linear Programming 234 Contraction Mappings 249 Unbounded Costs per Stage 25 I Linear Systems and Quadratic Cost Functionals 266 Inventory Control 268 Nonstationary and Periodic Problems 27 1 Notes 277 Problems 279 
Chapter 7 
7.1 Convergence and Existence Results 7.2 Optimal Stopping 7.3 Optimal Gambling Strategies 7.4 The First Passage Problem 7.5 Notes 
Minimization of Total Expected Value-Undiscounted Cost 
Problems 
296 300 305 312 320 320 
CONTENTS ix 
Chapter 8 Minimization of Average Expected Value 
8.1 Existence Results 8.2 Successive Approximation 8.3 Policy Iteration 8.4 8.5 Notes 
Infinite State Space-Linear Systems with Quadratic Cost Functionals 
Problems Appendix Existence Analysis under the Weak Accessibility Condition 
APPENDIXES 
Appendix A Mathematical Review 
Appendix B On Optimization Theory 
Appendix C On Probability Theory 
Appendix D On Finite State Markov Chains 
References 
332 342 349 353 356 357 358 
367 
374 
377 
382 
387 
Index 395 
This page intentionally left blank
Preface 
This text evolved from an introductory course on optimization under uncertainty that I taught at Stanford University in the spring of 1973 and at the University of Illinois in the fall of 1974. It is aimed at graduate students and practicing analysts in engineering, operations research, economics, statistics, and business administration. As a textbook it could be used, for example, in a one-semester first-year graduate course, which could cover primarily the first five chapters, the first half of Chapter 6, and parts of Chapter 8. It could also be used in a two-quarter graduate course, which would probably cover the whole text. Depending on the students’ back- grounds and interests, some material could be omitted or added by the instructor. 
The basic objective of the book is to provide a unified framework for sequential decision making under uncertainty and to stress the few funda- mental concepts underlying the treatment of uncertainty and the technique of dynamic programming. These concepts (risk, feedback, sufficient statistics, adaptivity, contraction mappings, and the principle of optimality) are emphasized and developed in a framework that is devoid, to the extent possible, of structural assumptions on the problem considered. This is accomplished by considering general dynamic systems defined over arbitrary state and control spaces. Thus our formulation allows the simultaneous treatment of several important classes of problems, such as stochastic control problems (popular in modern control theory) as well as problems of control of finite state Markov chains (popular in operations research and statistics). However, rigor is claimed only in the case where the underlying probability space is a finite or countable set, while other cases are treated in a formal manner. 
While most of the theoretical developments are carried out in a general framework, a large portion of the text is devoted to applications from specific problem areas. This serves the dual purpose of illustrating the 
xi 
xii PREFACE 
theoretical developments and of presenting material that is important in its own right. My objective has not been to develop any particular application area in great depth but rather to emphasize those aspects which are strongly related with the dynamic programming technique and associated concepts. 
The mathematical prerequisite for the text is a good knowledge of introductory probability theory and undergraduate mathematics. This includes the equivalent of a one-semester first course in probability theory together with the usual calculus, real analysis, vector-matrix algebra, and elementary optimization theory most undergraduate students are exposed to by their fourth year of studies. A summary of this material together with appropriate references is provided in the appendixes. An effort has been made to keep the mathematics at the lowest possible level consistent with rigor. However, it is inevitable that some mathematical maturity is required on the part of the reader so that he is able to think in relatively abstract terms. In addition, the last part of the text, which deals with infinite-horizon problems, is mathematically more sophisticated (particularly after Section 6.3) than the first part and requires a firm grasp of some of the basic con- vergence concepts of analysis. Readers with a somewhat weak analysis background may find the developments of Sections 6 . U . 7  and Chapter 7 difficult to follow. Familiarity with the notions associated with finite state Markov chain theory is not required, except in Chapter 8 and the last section of Chapter 7. Even there, however, Markov chain theory is used in a periph- eral manner, and the reader should be able to follow the development of the material after a reading of Appendix D perhaps supplemented by an hour or two of instruction. While prior courses or background on dynamic system theory, optimization, or control will undoubtedly be helpful to the reader, it is felt that the material in the text is reasonably self-contained. 
The nature of the subject of this book makes the choice of level of presentation rather difficult. The reason is that dynamic programming is a very simple and general technique, which nonetheless requires the extremely complicated machinery of measure-theoretic probability theory if it is to be presented in a mathematically rigorous way and within a general setting (i.e., in general spaces and in the presence of uncertainty). My choice has been to adopt a somewhat freewheeling style of mathematical presentation in the first five chapters, which deal with finite-horizon problems, a n d l o  raise substantially the level of mathematical precision in the last thfee chapters, which deal with infinite-horizon problems. The developments in Chapters 1-5 are carried out in a very general setting. However, the mathe- matical framework is not entirely rigorous, as explained in Section 2.1. In Chapters 6 8  the class of problems under consideration is restricted. Limi- tations are placed on the probability space in the interest of keeping the mathematics simple. This approach, which may seem somewhat unorthodox, 
PREFACE xiii 
was dictated by two basic considerations. First, since the validity of many of the concepts to be presented (principle of optimality, sufficient statistics, feedback, adaptivity, etc.) depends very little on structure, I felt that the reader should be given the opportunity to appreciate the power and gener- ality of these concepts without being impeded by irrelevant structural assumptions or complicated mathematical details. Second, 1 felt that mathematical precision is essential for the treatment of infinite-horizon problems, much more so than for finite-horizon problems. In addition, I wanted to provide a systematic and up-to-date treatment of infinite-horizon problems in the hope that this treatment will be of some value to the research community as well as to practicing analysts. 
The text starts with an introductory chapter on formulation of decision problems under uncertainty. The aim here is to provide a broad framework within which sequential decision problems under uncertainty can be appro- priately placed. The material in this chapter is of fundamental importance. However, it is not used in an essential manner in the remainder of the text, and the reader may proceed directly to Chapter 2 if he so wishes. 
Part I deals with finite-horizon problems. A single-model problem of broad applicability is employed throughout this part. The model is based on a state variable representation ofa dynamic system that is standard in modern control theory. Transition probability models can be embedded within the framework of the model utilized by means of a simple reformulation. The dynamic programming algorithm is developed and illustrated in several applications of independent interest. Linear quadratic stochastic control problems and inventory control problems are treated in considerable detail. Several additional topics from operations research, economics, and statistics are also considered. Problems with imperfect state information are treated as special cases of the basic model problem. Since implementation of optimal and suboptimal controllers for such problems often requires the use of estimators, I have added a sizable appendix covering least squares estimation and Kalman filtering. The emphasis throughout the text is on optimization of dynamic stochastic systems. However, in view of the limitations of the dynamic programming technique, the subject of suboptimal control is of undeniable importance. For this reason I have included material on suboptimal control with emphasis placed on those techniques that are of broad applicability. 
While Part I emphasizes conceptual aspects of sequential decision problems, Part I1 concentrates on the mathematical aspects of infinite- horizon problems. The coverage is quite thorough and includes discounted, undiscounted, and average cost problems. The basic model problems are set up in such a way that the underlying probability spaces are countable, thus eliminating all mathematical difficulties of a measure-theoretic nature. 
xiv PREFACE 
However, the class of dynamic systems considered is much broader than the class of Markov chains with countable state space. For example, it includes all deterministic systems defined over arbitrary state and control spaces. This part also contains several new results developed either in the text or in the problem sections. 
The problems at the end of each chapter are of four basic varieties: drill problems, examples or counterexamples, problems illustrating additional results of specific application nature, and theoretical problems that extend and supplement the developments of the text. Some of the problems in the last category (particularly in Chapters 6 and 7) are quite difficult to solve, and hints as well as references have been supplied where appropriate. The serious reader will benefit a great deal by going over the theoretical problems, which constitute a significant component of the text. 
Acknowledgments 
I feel indebted to several individuals and institutions who helped make the book possible. I am thankful to my teachers at the Massachusetts Institute of Technology, where I was introduced to the subject of stochastic control, particularly Mike Athans, Sanjoy Mitter, and Ian Rhodes. My perspective of the subject was broadened considerably during the time I taught at Stanford University ; the stimulating atmosphere of the Engineer- ing-Economic Systems Department and my interaction with David Luen- berger in particular played an important role in shaping the framework of the book. The Coordinated Science Laboratory at the University of Illinois provided research support and an appropriate environment for completing the project. As with every book that develops through classroom instruction, the comments and suggestions of my students led to several clarifications and improvements. My greatest debt of gratitude to a single individual goes to Steve Shreve, who read with exceptional care the entire preliminary version of the manuscript and made a plethora of penetrating comments and suggestions. As a result of my interaction with Steve, the quality of the manuscript improved substantially. Finally, I wish to give my thanks to my family for their support during the course of the work that led to this book. 
xv 
This page intentionally left blank
Chapter I 
Introduction 
This chapter sets the stage for the remainder of this text. Rather than dealing with methods for analysis or solution of decision problems under uncertainty, it examines various approaches for formulating such problems. Since the subject is of fundamental importance and at the same time far from trivial, it is worth examiningeven in the context ofan introductory text. On the other hand, the material in this chapter is not used in a direct way later and it is not essential for the reader to have a firm grasp of it in order to proceed to subsequent chapters. 
Optimization problems under uncertainty possess several important characteristics that are not present in the absence of uncertainty, i.e., in deterministic optimization problems. The two most important such char- acteristics are the need to take into account risk in the problem formulation and the possibility of information gathering (feedback) during the decision process. 
To illustrate the first characteristic consider a problem of dividing an amount of capital x between two different investment opportunities A and B. Assume that A offers with certainty $1.499 per dollar invested. If the total profit is to be maximized and B offers with certainty $1.5 per dollar invested, then the capital x should be invested in its totality in B. Assume now instead that B offers $1.5 per dollar on the auerage but not with certainty. For example, 
1 
2 1 INTRODUCTION 
assume that B offers $0 per dollar with probability 0.8 and $7.5 per dollar with probability 0.2. Then if the average (expected) profit is to be maximized, again the whole capital should be invested in B. In fact, the same is true for any probability distribution on the return of B with expected value $1.5 per dollar invested. However, most investors would object to such an allocation. Not wanting to take any risk of losing part of their capital, some would invest exclusively in the sure opportunity A,  while others would invest at least a positive fraction of x in A.  This indicates that a problem formulation whereby expected profit is maximized may be inappropriate since in this formulation the risk associated with each allocation is not reflected at all in the cost functional and hence does not influence the optimal decision. At the same time, the question is posed as to what is an appropriate formulation of the problem. 
As a more dramatic example of the need to take into account risk in the problem formulation consider the following situation (the so-called St. Petersburg paradox). An individual is offered the opportunity of paying x dollars in exchange for participation in the following game. A fair coin is flipped sequentially and the individual is paid 2k dollars, where k is the number of times heads have come up before tails come up for the first time. The de- cision that the individual must make is whether to accept or reject participa- tion in the game. Now if he accepts, his expected (average) game is 
‘*I 1 c 2kf” 2k - x = co, 
k = O  
so that if his acceptance criterion is based on maximization 
profit from the 
of his expected profit, he is willing to pay any amount x to enter the game. This, however, is in strong disagreement with the behavior of individuals due to the risk ele- ment involved in entering the game and shows again that a different for- mulation of the problem is necessary. Some of the aspects of formulating decision problems under uncertainty so that risk is properlyDken into account are dealt with in the next two sections. 
A second important feature of many decision problems under uncertainty is the possibility of carrying out the decisions in stages while gathering infor- mation between stages about some of the uncertain parameters involved in the problem. This information may be used with advantage when making future decisions. The fundamental role of information gathering in problems of decision under uncertainty will become evident as we progress through this text. For the moment let us consider the following simple example: 
EXAMPLE A two-stage scalar dynamic system evolves according to the equations 
x, = uo + wg, x2 = x1 + u1. 
1 . 1  THE PROBLEM OF DECISION UNDER UNCERTAINTY 3 
The scalar wo is an uncertain parameter taking values 1 or - 1 with prob- 
ability ). The problem is to choose uo and u1 so as to minimize the expected absolute value of x2 : 
I t  is easy to see that the optimal value is 
and the optimal values of u 0 ,  u1 are those for which - 1  d uo + u1 d 1. Consider now the situation where uo and u1 are chosen sequentially in a way that x1 is known to the decision maker when selecting ul. Then clearly the optimal selection policy for uo and u1 is to take uo to be any scalar and to take u1  equal to -xl. With this selection policy the optimal cost is reduced to zero. The reduction was made possible by means of proper use of the in- formation received (i.e., the value of xl). Note that the optimal value of u1 depends on the value of x l ,  i.e., it is a function of the information received. Note also that if there is no uncertainty, for example, if wo = 0 with prob- ability one, then the optimal cost is zero whether the value of x1 becomes known prior to selecting u 1  or not. This is a manifestation of the intuitively obvious fact that information gathering can be of no help when there are no uncertain parameters in the problem. 
1.1 The Problem of Decision under Uncertainty? 
A decision problem in one of its simplest and most abstract forms con- 
sists of three nonempty sets 9, N ,  and 0, a function f :  9 x JV -+ 0, and a complete and transitive relation <. on 0: 
9 the set of possible decisions 
Jf indexes the uncertainty in the problem and may be called the set of 
“states of nature” 0 the set of outcomes of the decision problem f the function that determines which outcome will result from a given 
decision and state of nature, i.e., if decision d E 9 is selected and state 
of nature n E .Af prevails, then the outcome f (d ,  n )  E 0 occurs 
t As mentioned earlier, the concepts in this and subsequent sections in this chapter are not essential for the understanding of the remainder of the text. The reader may proceed directly to Chapter 2 if he so wishes. 
4 1 INTRODUCTION 
< a relation determining our preference among the 0utcomes.t Thus 
for O,, O2 E 0, by 0,  < 0, we mean that outcome O2 is at least as 
preferable as outcome 0,. By completeness of the relation we mean that every two elements of 0 are related in the sense that given any 0,, O2 E 0 either 0 ,  < 0 2 ,  but not 0, < 0,, or O2 < O,,  but not 0, < O,, or both 0, < 0, and 0 ,  < 0,. By transitivity we mean that 0, < 0, and O2 < O 3  implies 0 ,  < O3 for any three elements 
EXAMPLE Consider the following situation. An individual may bet $1 on the toss of a coin or not bet at all. If he bets and guesses correctly, he 
wins $1 and if he does not guess correctly, he loses $1. Here 9 consists of 
threeelements {bet on heads, bet on tails, not bet}, N consists oftwo elements {heads, tails}, and 0 consists of three elements, the three possible final fortunes of the player {SO, $1, $2). The preference relation on 0 is the natural 
one, i.e., 0 < 1, 0 < 2, 1 < 2, and the values of the function f are given in 
Table 1.1 for each value of d and n. 
01, 0 2 ,  0 3  E 0. 
TABLE 1.1 
3 
H T Not bet 
H $2 $0 $ I  
T $0 $2 $ I  .4. 
Now the relative order by which we rank outcomes is usually clear in any given situation. On the other hand, in order for the decision problem to be completely formulated we need a ranking among decisions that is consistent in a well-defined sense with our ranking of outcomes. Furthermore, in order to be able to apply mathematical methods for the analysis of the decision problem we would like to have this ranking determined by a numerical function F : 9  + R ( R  is the set of real numbers) such that 
(1) 
where the notation d ,  < d ,  implies that the decision d 2  is at least as preferable 
as the decision d , .  It is by no means clear what this ranking among decisions 
d ,  < dz  % F ( d , )  < F(d2) vd1, d2 E 9, 
t The symbol < in this chapter will be (somewhat loosely) used to denote a preference relation within either the set of outcomes or the set of decisions. The precise meaning should be clear from the context and hopefully the use of the same symbol to denote different preference relations will create no confusion to the reader. 
1.1 THE PROBLEM OF DECISION UNDER UNCERTAINTY 5 
should be or how one should go about determining and characterizing such a ranking. For example, in the gambling problem above different people will have different preferences as to accepting or refusing the gamble. There are a number of approaches and viewpoints for determing a ranking among decisions and this section deals with some of these. 
Payofl Functions, Dominant and Noninferior Decisions 
Let us consider the case where it is possible to assign to each element of 0 a real number in such a way that the order between elements of 0 agrees with the usual order of the corresponding numbers. That is, there exists a real- valued function G :  0 + R with the property 
G ( 0 , )  Q G(O2) * 0 ,  4 0 2  YO,, 0 2  E 0. (2) 
Such a function does not always exist (see Problem 2). However, its existence can be guaranteed under quite gener 1 assumptions. In particular, one may 
far from unique, since if @ is any monotonically increasing function 0: R + R ,  
the composite function 0. G (defined by (@ . G ) ( O )  = @[G(O)] )  has the same property (2) as G. For instance, in the example given earlier a function G :  {O, 1, 2) + R satisfies.(2) if and only if G(0)  < G(1) < G(2) and there is an 
infinity of such functions. 
Now for any choice of G as in (2) we define the function J :  93 x JV + R 
by means of 
show that it exists if 0 is a countable \. se Also if such a function G exists, it is 
J(d ,  n)  = G C f ( d ,  n)l and call it a payoflfunction. 
Given a payoff function J it is possible to obtain a complete ranking of decisions by means of a numerical function in the special case ofcertainty (the case where the set JV of states of nature consists of a single element E). By defining 
F(d)  = J(d ,  E) 
we have 
d i  d d2 % F ( d i )  < F(d2) % f ( d i ,  6) d f ( d 2 ,  f i )  
and the numerical function F defines a complete ranking of decisions. 
partial order on 9 by means of the relations When JV contains more than one element, the order on 0 induces only a 
(3) d l  < d 2  % J ( d l ,  n)  < J ( d 2 ,  n)  
% f ( d  ,, n)  d . f ( d 2 ,  n)  
Vn E .N, 
Vn E JV. 
6 1 INTRODUCTION 
In this partial order it is not necessary that every two elements of 9 be related, 
i.e., for some d, d' E 9 we may have neither d < d' nor d' < d.  If, however, for 
two decisions d, ,  d 2  E 9 we have d ,  < d, in the sense of (3), then we can con- 
clude that d 2  is at least as preferable as d ,  since the resulting outcome f ( d 2 ,  n)  is at least as preferable asf(d, ,  n )  regardless @the state of'nature n that will occur. 
A decision d* E $3 is called a dominant decision if 
d < d *  V d E 9 ,  
where < is understood in the sense of the partial order defined by (3). 
Naturally such a decision need not exist. If, however, such a decision does exist, then it may be viewed as optimal. In most problems of interest to an analyst, however, there exists no dominant decision. For instance, in t e gambling example considered earlier a dominant decision does not exisAn fact, no two decisions are related in the sense of (3) for this example. 
In the absence of a dominant decision one can consider the set 9, c 9 
of all noninferior decisions, where d , ~ 9 ,  if for every d ~ 9  the relation 
d, < d implies d < d, in the sense of the partial order defined by (3). In terms 
of a payoff function J ,  noninferior decisions may be characterized by 
d, E 9, + there does not exist any d E 9 such that 
J ( d , ,  n)  d J(d ,  n)  V n  E I/̂  and J(d, ,  n) < J ( d ,  n) for some n E ~4.. 
Clearly it makes sense to consider only the decisions in 9, as candidates for 
optimality since any decision that is not in 9, is dominated by one that belongs to $3,. Furthermore, it may be proved that the set 9, is nonempty when the set 9 is a finite set, so that at least for this case there exists at least one noninferior decision. However, in practice the set 9, of noninferior 
decisions often is either difficult to determine or contains too many elements. For instance, in the gambling example given earlier, the reader may easily verify that every decision is noninferior. 
Whenever the partial order (3) fails to produce a satisfactory ranking among decisions, one must turn to other approaches to formulate the de- cision problem. Approaches that we shall examine assume a notion of a generalized outcome of a decision and introduce a complete order on the set of these generalized outcomes consistent with the original order on the set of outcomes 0. The complete order on the set of generalized outcomes in turn induces a complete order on the set of decisions. 
The Min-Max Approach 
The min-max (or max-min) approach takes the point of view that the generalized outcome of a decision d is the set of all possible outcomes 
1.2 EXPECTED UTILITY THEORY AND RISK 7 
resulting from d: 
f(d, N )  = (0 E 0 I there exists n E N with f ( d ,  n )  = O}. 
In addition, it adopts a pessimistic attitude and ranks the setsf(d, N )  on the basis of their worst possible element. This is accomplished by introducing a complete order on the set of all subsets of 0 by means of the relation 
0, 4 0, % inf G ( 0 )  d inf G ( 0 )  YO,, 0, = 0, (4) O E B ,  O E B l  
where O,, 0, is any pair of subsets of 0 and G a numerical function con- sistent with the order on 0 in accordance with (2). From (4) we have a com- 
plete order on the set 9 by means of 
di 4 d2 % f(di, N )  4 f ( d 2 ,  
or in terms of a payoff function J ,  
infGCf(di7 n)I d infGCf(d2, n)l n E N  n E . N  
dl 4 d, % infJ(d,, n) < infJ(d,, n).  n E N  ns.V 
Thus by using the min-max approach the decision problem is formulated 
concretely in that it reduces to maximizing over 9 the numerical function 
F ( d )  = inf J(d ,  n).  n E . M  
Furthermore, it can easily be shown that the elements of 9 that maximize F(d)  above will not change if J is replaced by CD . J ,  where CD: R + R is any 
monotonically increasing function. Nonetheless, the min-max approach is pessimistic in nature and will often produce an unduly conservative de- cision. Characteristically in the earlier gambling example the optimal decision according to the min-max approach is to refuse the gamble. 
The second approach for formulating decision problems that we shall examine is considered in the next section. 
1.2 Expected Utility Theory and Risk 
It is often the case that in a given decision problem under uncertainty we have additional information concerning the mechanism by which states of nature occur. In particular we are often in a position to know that the states of nature occur in accordance with a given probabilistic mechanism, which may depend on the decision d adopted. To be specific, assume for convenience 
8 1 INTRODUCTION 
that the set of states of nature A’” is either a finite or a countable set? and that 
for every decision d E 9 we know that states of nature occur according to a 
given probability distribution P( * Id) defined on N .  Now each decision d E 9 specifies the probability of each outcome via the function f (d,  - ) and the relation 
In this relation Pd(0) denotes the probability that the outcome 0 will occur when the decision d is adopted. One may view the probability measure Pd 
associated with each d E 9 as a “probabilistic outcome” (or “generalized 
outcome” to use the term of the previous section) corresponding to d,  since Pd specifies the probabilistic mechanism by which outcomes occur once d is selected. We shall also use the term lottery1 for a probability measure on the set of outcomes. In the gambling example given earlier, the decision “bet on heads” has as a generalized outcome the probability distribution (or lottery) (*, 0, i) on the set of outcomes 0 = ($0, $1, $2). The decision “bet on tails” has the same generalized outcome while the decision “not bet” has as a generalized outcome the probability distribution (0, 1,O). 
The basic idea of the expected utility approach is the following: We already have a complete ranking of the outcomes, i.e., the elements of 8. If we had a complete ranking of all lotteries on the set of outcomes (presumably con- sistent with the original ranking on 0 in the sense that if the outcome O1 is preferable to the outcome 02,  then the lottery assigning probability one to O1 is preferable to the lottery assigning probability one to 02), then we could in turn obtain a complete ranking of all decisions in 9. This is true simply because we could rank any two decisions d l ,  d2  E 9 according to the relative 
order of their corresponding lotteries Pd,, Pd2, i.e., by means of the relation 
The fundamental premise of the expected utility approach is to assume at the outset that the decision maker has a complete ranking of all lotteries on the set of outcomes, i.e., the decision maker is in a position to express his preference between any two probability distributions on the set of outcomes. This in turn settles the question of ranking decisions in view of the preceding relation. 
t For the benefit of the advanced reader we mention that when .N is not countable it is necessary that a probability space structure be introduced on N and 0 as in Appendix C. Furthermore, it is necessary that the functionf(d, -) satisfy certain (measurability) assumptions in order that the probability measure Pd be well defined. 
$ The term “lottery” is associated with the conceptually convenient device of viewing outcomes as prizes of some sort and viewing a fixed probabilistic mechanism for winning a prize as a lottery. 
1.2 EXPECTED UTILITY THEORY AND RISK 9 
Furthermore, if there exists a numerical function G by means of which pre- ferences on the set of lotteries can be expressed, 
Pdl 4 p d 2  G(Pd,) G G ( P d 2 ) ,  
then decisions can be ranked by means of a numerical function F ,  
dl  < d2 * F(di) G F(d2L 
where F(d)  = G(Pd) for all d E 9. 
The aspect of this formulation that is extremely appealing, however, from 
an analytical point of view is that the ordering of decisions can be expressed not only by a function G as above, but also by means of an essentially unique numerical function called the utilityfunction. This function, denoted U ,  maps the space of outcomes into the set of real numbers and satisfies 
di <d2%Pdl <Pd2=E{U[f(di,n)lId,} G E{uCf(d2,fi)lld2), ( 5 )  
where the expectations are taken with respect to the corresponding prob- ability distribution P( - Id) on X .  The problem of selecting an optimal 
decision is thus reduced to the problem of maximizing over 9 the expected 
value of the numerical function U .  
In order to clarify the problem formulation based on the approach of this section and to illustrate the advantages resulting from the introduction of a utility function let us consider the following example: 
INVESTMENT EXAMPLE Consider a problem of allocating one unit of capital between two investment opportunities A and B. Opportunity A yields $1.5 per dollar invested with certainty, while opportunity B yields $1 per dollar invested with probability f and $3 per dollar invested with prob- 
ability f. The problem is to decide on the fractions d and (1 - d) of the 
capital to be invested in opportunities A and B, respectively, where 0 G d ,< 1. 
In terms of the framework of the decision problem of Section 1.1, the 
set of decisions 9 consists of the interval [0, 11, i.e., the set of values that the 
fraction d invested in A can take. The set of states of nature JV consists of two elements n,, n 2 ,  where n, : B yields $ 1  per dollar invested, and n2 : B yields $3 per dollar invested. The set of outcomes 0 may be taken to be the interval [l, 31, which is the set of possible final fortunes of the investor resulting from all possible decisions and states of nature. The functionfthat determines the outcome corresponding to any decision d and state of nature n is given by 
1.5d + (1 - d) if n = n, 1% + 3(1 - d) if n = n 2 .  f (d, n) = { 
The preference relation on the set of outcomes is the natural one, i.e., a final fortune O1 is at least as preferable as a final fortune O2 if 0, is numerically 
greater than or equal to O2 (i.e., O2 < 0, if O2 < 0,). 
10 1 INTRODUCTION 
Let us first note that, since B has a higher expected rate of return, the decision that maximizes expected value of profit is to invest exclusively in opportunity B (d* = 0). On the other hand the optimal decision based on the max-min approach is to invest exclusively in A (d* = 1 )  since in this approach one maximizes profit based on the assumption that the most unfavorable state of nature will occur. Mathematically this can be verified by noting that d* = 1 maximizes over [0, 11 the function F(d)  given by 
F(d)  = min(l.5d + (1 - d),  1.5d + 3(1 - d ) } .  
Note that the approach of maximizing expected profit and the max-min approach lead to very different decisions. Yet it is safe to assume that many decision makers would settle on a decision that differs from both decisions mentioned above and that invests a positive fraction of the capital in both opportunities A and B. 
Now in the expected utility approach the fundamental assumption is that the decision maker has a complete ranking of all lotteries on the set of out- comes. In other words, given any two probability distributions on the in- terval of final fortunes [0,3] the decision maker can express his preference between the two, in the sense that he can point out the distribution in ac- cordance with which he would rather have his final fortune selected. Now the probability distribution on the set of final fortunes corresponding to a decision d is the one that assigns probability 3 to [ l S d  + (1 - d)] and prob- 
ability 3 to [ l S d  + 3(1 - d)]. According to the expected utility approach a 
decision d is optimal if its corresponding probability distribution is at least as preferable as all other distributions of the type described above. It should be clear, however, that a mathematical formulation of the corresponding op- timization problem is very cumbersome since it is difficult to visualize or conjecture the form of a numerical function by means of which these pro- bability distributions can be ranked. On the other hand, let us assume that a utility function U satisfying (5) exists (and it does exist under mild assump- tions). Then an optimal decision is one that solves the problem 
maximize E { U [ f ( d ,  n)]} 
subject to 0 < d < 1. 
n 
Substituting the data of the problem we have 
E { U [ f ( d ,  n)]} = + { U [ I S d  + (1 - d)] + U[1.5d + 3(1 - d)]) 
and the maximization problem above is formulated in a rather convenient form. 
n 
1.2 EXPECTED UTILITY THEORY AND RISK 11 
As an example let us assume that the decision maker’s utility function is quadratic of the form 
U ( 0 )  = a0 - 02, 
where a is some scalar. We require that 6 < a so that U(0) is increasing in the interval [0, 31. This is necessary for the preference relation on the set of outcomes specified by the utility function to be consistent with the original preference relation. Solution of the maximization problem above yields the optimal decision d*, where 
0 if 8 < a  
d* = {(8 - a)/5 if 6 < a < 8. 
Note that for 6 < a < 8 a positive fraction of the capital is invested in op- portunity A even though it offers a return that is less than the average return of B. 
It is to be noted, of course, that different decision makers faced with the same decision problem may have different utility functions, so that before the problem can be numerically solved the form of the utility function must be specified. This can be done experimentally if necessary (see Problem 3). How- ever, the importance of the notion of a utility function satisfying ( 5 )  lies pri- marily with the fact that under relatively mild assumptions it exists and can serve as the starting point for analysis of the decision problem. The reason is that important conclusions about optimal decisions can often be obtained based on either incomplete knowledge of the utility function or fairly general assumptions on its form. Several examples of such situations will be given subsequently. 
We provide below the theorem of existence of a utility function for the case where the set of outcomes 0 is a finite set. For more general cases see the book by Fishburn [F3]. 
Consider the set 0 of outcomes and assume that it is a finite set, 0 = { O , ,  0 2 , .  . ., ON}. Let 9 be the set of all probability distributions P = 
(pl, p 2 ,  . . . , pN) on 0, where pi is the probability of outcome Oi, i = 1, . . . , N .  
For any P,,  P2 E 9, P1 = (pi, . . . , p i ) ,  P ,  = (p: ,  . . . , p i ) ,  and any a E [0, 13, 
we use the notation 
aP, + ( 1  - a ) P , = ( a p :  + ( 1  - a ) p ; , . . . , a p i + ( l  - a ) p i ) ~ g .  
Let us make the following assumptions: 
There exists a complete and transitive relation < on 9. (For any 
P1, P 2  E 9 we write P ,  - P ,  if P ,  < P 2  and P ,  < P,,  and we write PI i P ,  
if P ,  < P ,  but not P ,  - P,). 
A. l  
12 1 INTRODUCTION 
A.2 If P ,  - P,, then for all a E [0, 11 and all P E B 
aP, + (1 - a)P - aP, + (1 - a)P. 
A.3 If P1 i P,, then for all a E (0, 11 and all P E B 
U P ,  + (1 - a)P < UP, + (1 - a)P. 
aP ,  + (1 - a)P, - P,. 
A.4 If P ,  i P ,  < P 3 ,  there exists an a E (0, 1) such that 
Before proving the expected utility theorem let us provide a brief dis- cussion of the above assumptions. It is convenient for interpretation purposes to view each of the outcomes O , ,  O , ,  . . . , ON as a monetary prize. Consider any probability distribution P = ( p , ,  p , ,  . . . , p N )  on the set of outcomes. 
Imagine a pointer that spins in the center of a circle divided into N regions. We shall assume that the pointer is spun in such a way that when it stops it is equally likely to be pointing in any given direction. The region associated 
with each prize Oi, i = 1, . . . , N, occupies a fraction pi of the circumference of 
the circle. Then we associate with P the game (or lottery) whereby we spin the wheel and win the prize corresponding to the region within which the pointer stops. Now given any two probability distributions P, and P ,  and a scalar a E [0, 13 we can associate with the probability distribution 
aP, + (1 - a)P, 
the following game. A pointer is spun in the center of a circle divided in two 
regions, say 1 and 2, occupying respective fractions a and (1 - a) of its cir- 
cumference. Depending on whether the pointer stops in region 1 or region 2 the game corresponding to P1 or P ,  is played and a prize is won accordingly. 
Assumption A.l requires that we are able to state our preference between games such as the above, which correspond to any two probability dis- tributions P ,  and P,. Furthermore, our preference relation must be tran- sitive, i.e., if P ,  < P ,  and P ,  < P 3 ,  then P1 < P,. This assumption forms 
the core of the expected utility approach. Assumptions A.2 and A.3 have obvious interpretations and both seem reasonable. Assumption A.4 is a 
continuity assumption requiring that if P1 i P ,  i P,, one is indifferent to 
the game associated with P2 and a game the outcome of which decides with 
respective probabilities c( and (1 - a) whether the game associated with P1 or 
P 3  will be played. This assumption is inconsistent with a worst-case viewpoint whereby one ranks lotteries according to the worst outcome that can occur with positive probability and has been the subject of some controversy. For example, consider the extreme situation where there are three outcomes O1 = death, 0, = receive nothing, and O3 = receive $1. Then it appears reasonable that any probability distribution that assigns a positive probability 
1.2 EXPECTED UTILITY THEORY AND RISK 13 
to O1 (death) cannot be preferable or equivalent to any probability distri- bution that assigns a zero probability to O1. Yet Assumption A.4 requires that for some a with 0 < a < 1 we are indifferent between the status quo and 
agarnewhereby wereceive$l withprobability(1 - a)anddie with probability 
a. On the other hand it is possible to argue that if the probability of death a is extremely close to zero, then this might actually be the case. 
The following theorem is the central result of the expected utility theory. It states that a preference relation on the set of all lotteries satisfying Assump- tions A.1-A.4 can be characterized numerically by means of an essentially unique function, the utility function. It is worth pointing out that this result concerns an arbitrary preference relation on lotteries on the set o f  out- comes and is  thus completely decoupledfrom any decision problem that one may be considering. 
Theorem Under Assumptions A. 1-A.4 there exists a real-valued 
function U : 0 + R called utilityfunction, such that for all P,, P ,  E 9 
N N 
Pi < Pz k E { U ( O ) }  = C p ! U ( O i )  < pZU(0i) = E { U ( O ) } ,  (6) 
PI i =  1 i =  1 p2 
where we denote by Ep,  { . } the expectation with respect to the probability distribution Pi. Furthermore, U is unique up to a positive linear trans- formation, i.e., if U* is another function with the above property, there exist scalars s1 > 0, s,, such that 
U*(O) = SlU(0)  + s, vo E 0. Proof We first show the following statement: 
S If P ,  i P, and P ,  is such that P, < P ,  < P,, then there exists a 
unique scalar a E [O, 13 such that 
U P ,  + (1 - a)P, - P,. (7) 
Furthermore, if P; is such that P, < P, < P> < P 3  and a' corresponds to P', 
as in (7), then a 2 a'. 
Indeed if P ,  - P, i P,, then a = 1 is the unique scalar satisfying (7) since 
if for some 0 < a -= 1 we had 
aPl + (1 - a)P,  - P z  - aPl + (1 - a)P,, 
then Assumption A.3 would be contradicted. Similarly if P1 i P, - P,, then a = 0 is the unique scalar satisfying (7). Assume now that P1 < P, i P ,  . 
Then by Assumption A.4 there exists an a1 E (0, 1) satisfying (7). Assume that 
14 1 INTRODUCTION 
a1 is not unique and there exists another scalar u2 E (0, 1) such that (7) is satisfied, i.e., 
(8) GIIP,  + (1 - ~ 1 ) P 3  - Pz - a2P1 + (1 - a,)P3. 
Let us assume that 0 < a, < a, < 1. Then we have 
Since P1 i P ,  we have by Assumption A.3 and (9) 
1 - a2 
P ,  = P 3 .  P ,  +- P ,  i ___ P ,  + 
1 - a, 1 - a, 1 - a ,  1 - a1 
1 - a2 a2 - a1 a2 - a ,  
Again using A.3 and (10) we have 
N ~ P ,  + (1 - ~ 2 ) P 3  ( C C ~ P ,  + (1 - ~ r , ) P 3 .  
However, this contradicts (8) and hence the uniqueness of the scalar a in (7) is proved. 
To show that if P ,  < P,  < P, < P,, then a 2 a‘ assume the contrary, 
i.e., a < a‘. Then we have, using A.3, 
P2 - a’P1 + (1 - a’)P, 
M 
l-a+a’ 
+ 1 - a + a’ 
a 
= (1 - a + a’) 
< ( I  - a + + ’ )  l-a+a’ 
= aP, + (1 - a)P3 - P 2 .  
Hence P, < P , ,  which contradicts the assumption P 2  4 P i .  It follows that 
a 2 a‘ and Statement S is proved. 
Now consider the probability distributions 
= (1, 0,. . . 7 o), P ,  = (0, 1, .  * .  9 o), . . . 7 P N  = (0, 0,. . 3 0, 1). 
Assume without loss of generality that P ,  < P ,  < . . . < PN and assume 
further that P ,  < PN (if P ,  - P2 - . . . - P N ,  the proof of the proposition 
is trivial). Let A , ,  A N  be any scalars with A ,  < AN and define 
u(0,) = A, ,  u(0N) = AN. 
1.2 EXPECTED UTILITY THEORY AND RISK 15 
Let ai ,  i = 1, . . . , N, be the unique scalar ai E [0, 11 such that 
aiP1 + (1 - ai)PN - Pi, 
U(Oi) = A i  = a i A ,  + (1 - ai)AN, 
i = 1,. . ., N, (1 1) 
(12) 
We shall prove that the function U : 0 + R as defined above has the desired property (6). Indeed for any probability distribution P = (p,, . . . , pN) it is easily shown that P, < P < PN and thus we can define a(P) to be the unique 
scalar in [0, 11 such that 
and define 
i = 1, ..., N. 
a(P)Pl + [l - .(P)]PN - P. (13) 
From Statement S we obtain for all P, P' 
P < P' * a(P) 2 a(P'). (14) 
Now from (1 1) we have 
Comparing (13) and (1 5 )  we obtain N 
a(P) = Cpiai, i =  1 
and from (14) N N 
P, < P, * C p!ai 2 ,I p?ai. (16) 
From (12) we have mi = (AN - Ai)/(AN - A , ) ,  and substituting in (16) we 
obtain 
i =  1 I =  1 
N N 
P, < P,% Cp!Ai < Cp?Ai, 
i =  1 i =  1 
which is equivalent to (6), which was to be proved. It remains to show that the function U defined by (12) is unique up to a 
positive linear transformation. Indeed if U* were another utility function 
satisfying (6), then, by denoting U*(Oi) = A:, i = 1, . . . , N, by (11) and (6) 
we would have 
u*(oi) = Mi U*(Ol) + (1 - ai)u*(oN). 
16 1 INTRODUCTION 
This implies 
from which 
This proves the theorem. Q.E.D. 
Returning now to the decision problem, once we assume the existence of a preference relation on the set of lotteries characterized by a utility function, we can rank decisions as follows. Given the probability distribution P( * Id) 
on the set of states of nature N, every decision d E 9 induces a probability 
distribution (or lottery) P d  on the set of outcomes 0. Under the assumptions of the expected utility theorem there exists a utility function U :  0 + R such 
that for any d,, d z  E 9 
p d l  4 p d z  * E iU(0)) G E iU(O) ) .  
p d  I P d z  
We have, however, 
E { U ( O ) )  = E { UCf(d ,  n)lIdl Vd E 9, 
P d  
where the expectation on the left is taken with respect to P d  and the expecta- tion on the right is taken with respect to the probability distribution P( * Id) 
on N. Hence 
p d ,  4 Pd,*E{U[f(~i~n)] ldi}  G E{U[f(dz,n)lldil .  
By ranking decisions d E 9 in accordance with the ranking of the corre- 
sponding probability measures P d ,  
we obtain a complete order on the set 9 induced by the utility function U .  
The optimal decision is found by maximization of the numerical function F :  $3 -+ R, where 
F ( 4  = E {UCf (d ,  4 1  Id) 
and the decision problem is formulated in a way that is amenable to mathe- matical analysis. 
1.2 EXPECTED UTILITY THEORY AND RISK 17 
The Notion of Risk 
Consider a decision maker possessing a utility function U defined over an interval X of real numbers. We say that the decision maker is risk averse if 
E { W ) l  G WE{x}l  (17) P P 
for every probability distribution P on X for which the expectations above are finite. In other words, a decision maker is risk averse if he always prefers the expected value of the lottery over the lottery itself. Such behavior char- acterizes most decision makers. One may show that risk aversion is equi- valent to concavity of the utility function (see Appendix A for the definition and properties of concave and convex functions). On the other hand, we say that the decision maker is riskpreferring if the opposite inequality holds in (17), which is the case of a convex utility function. A gambler playing an unbiased roulette and receiving no reward or pleasure from gambling per se is a typical example of a risk preferring decision maker. Finally, a decision maker having a linear utility function is said to be risk neutral. 
The notion of risk is important since it captures a basic attribute of the attitudes of the decision maker and often characterizes important aspects of his behavior. An important and widely accepted measure of risk has been proposed by Pratt [P7]. In his formulation the function 
r(x) = - U”(x)/U‘(x) (18) 
[where U”, U’ denote the second and first derivative of U ,  respectively, and it is assumed that U’(x) # 01 measures locally (at the point x )  the risk aversion of the decision maker and is called the index of absolute risk aversion. It can be interpreted as follows. 
Let x be a gamble over the set of real numbers (i.e., a random variable) with given probability distribution and expected value X = E { x } .  Let us denote by y the amount of insurance the decision maker is willing to pay in order to avoid the gamble x, and instead receive the expected value X of the gamble. In other words, y is such that 
(19) U(X - y )  = E{U(x)l. 
Intuitively, y provides a natural measure of risk aversion. Proceeding formally we have by a Taylor series expansion around X, 
U(X - y )  = U(X) - yU’(X) + Ob),  (20) 
where by o(a) we denote a quantity that is negligible compared with the scalar a provided a is close to zero, i.e., [o(a)/a] = 0. Also we have 
E { U(X) }  = E { U(X) + (X - X)U‘(X) + %X - X)’U’’(X) + O [ ( X  - X)2]} 
= U(X) + +a2U”(X) + E {o [ (x  - X)23}, (21) 
18 1 INTRODUCTION 
where n2 is the variance of x .  From (19)-(21), we have 
yU’(2)  = -+n2U”(2) + o(y)  + E {o[(x - X)2]}. 
From this equation and (18) it follows that the amount of insurance or risk premium y that the decision maker is willing to pay is proportional (to first order) to the index of absolute risk aversion r(2), thus justifying the use of r (x)  as a measure of local risk aversion. Notice that in the preceding investment 
example the index r(y) is equal to 2/(u - 2y) and tends to decrease as u 
increases. This fact is reflected in the optimal investment, where an increasing fraction of the capital is invested in the risky asset as u increases. 
The index r (x)  often plays an important role in the analysis of behavior of decision makers. It is generally accepted that for most decision makers r (x)  is a decreasing or at least nonincreasing function of x, i.e., the decision maker more readily accepts risk as his wealth is increased. On the other hand, for the quadratic utility function U ( x )  = -3.’ + bx + c, the index r (x)  is equal to (b  - x) - ’  and is an increasing function of x (for x < b). For this 
reason the quadratic utility function is often considered inappropriate or at least accepted with reservation in economics applications, despite the an- alytical simplifications often resulting from its use. 
1.3 Some Nonsequential Decision Problems 
In this section we provide some examples of decision problems under uncertainty. In addition to illustrating the general approach of the previous section, some of these examples constitute applications that are important in their own right and will be useful later on. Their common characteristic is that the decision problems are formulated as single-stage problems as opposed to sequential decision problems, which are the subject of the remainder of this text. 
1.3.1 Quadratic Cost Functionalsf 
Many decision problems under uncertainty that are of interest involve the minimization of the expected value of a function that is quadratic in the decision variable. Not only do  such functionals arise naturally in many problems of interest but also there is an incentive in using a quadratic cost functional whenever this is reasonable. This is due to the great analytical simplification associated with such cost functionals as will be seen shortly. We consider below the simplest case. The results obtained have analogs in 
t We shall often be considering minimization of E (  - U}, where U is a utility function, 
instead of maximization of E { U }  and we shall refer to { - U} as a cost,functionu/. 
1.3 SOME NONSEQUENTIAL DECISION PROBLEMS 19 
more complicated cases involving sequential decision making. These cases will be considered in Chapters 3,4,6, and 8. 
Consider the problem of finding a vector u E R" (R" denotes m-dimen- sional Euclidean space) that minimizes the cost functional 
J ( u )  = E {&Ru + x'u}. 
In this relation R is an m x m symmetric random matrix, x an m-dimensional random vector, and prime denotes transposition. The joint probability distribution of R and x is given and we assume that the expected values 
R, x 
R = E { R } ,  = E { X ) ,  
are finite. Furthermore R is assumed to be a positive definite matrix. By taking the expectation with respect to R ,  x, we have 
J (u )  = iu'Ru + X'u, 
and the minimizing u is given by 
Thus the solution for this case is obtained analytically. Furthermore, the optimal vector u* depends linearly on the mean X. This linear dependence is characteristic of quadratic cost functionals. Note also that the solution u* is the same as the one that would be obtained if the problem were formulated as a deterministic problem (no uncertain parameters present) with all random quantities in the cost functional replaced by their expected values. This property is sometimes called the certainty equivalence principle. For single- stage problems it holds not only when the cost functional is quadratic but also for many other cost functionals. For example, it holds if the cost func- tional is linear with respect to the random quantities, such as in the cost functional 
where ri are random variables andf, given functions. On the other hand, as will be seen later, for quadratic cost functionals the certainty equivalence principle holds in satisfying form even in multistage decision problems, a fact that does not hold true for a wide class of cost functionals. 
Finally, consider the situation where the choice of u is made after ob- serving a random vector z that is probabilistically related to R ,  x ,  and further- more the conditional probability distribution P(R,  x I z )  is known for every z. Then clearly the optimal decision is given by 
u*(z) = - E { R  Iz}-' E { x ~ z )  
20 1 INTRODUCTION 
and depends on z. Whenever R and z are independent and x, z are Gaussian random vectors, then E {x lz} is a linear function of z (a fact to be shown later) and the decision u* depends in turn linearly on z. 
1.3.2 Least-Squares Estimation of Parameters 
Assume that we wish to determine an estimate of the value of a random vector w E R" given a known measurement z E: R". The joint probability distribution function F(w, z) is known. We formulate this problem as follows. 
Given z, find a vector G(z) that minimizes over all vectors f i  E R" the quadratic cost functional 
J ( P )  = E { l b  - PIIZlZ>, 
where llxll denotes the usual Euclidean norm of a vector x (Ilxll = (x'x)'''). This cost functional is a reasonable one and at the same time it results in a conveniently simple solution. 
Assuming that all expected values appearing below are finite, we have 
J ( P )  = E{llw1I2 - 2w'P + 11P1121~> = E{llwllZlz) - 2EIwlzYP + IIPI12 
and minimization with respect to P yields the minimizing vector 
6 ( z )  = E {wlz}. 
The corresponding optimal value of the cost functional is given by 
JC@(z)l = E { l l w  - E{wIz}II~Iz}. 
The fact that the conditional mean E {w lz} is the optimal (least-squares) 
estimate of w given z is a fundamental result of parameter estimation theory. In general it may be difficult to obtain a convenient analytic expression for E {w lz}. If, however, the joint probability distribution of (w, z) is a Gaussian distribution, then it is passible to show that the conditional mean E {w lz}  is a linear function of z. This is a well-known result and will be proved in the appendix to Chapter 4. 
1.3.3 Inventory Control 
Consider a problem of ordering a quantity of a certain item to meet a stochastic demand for the item. The cost of purchasing or producing u units of the item is 
if u = 0, C(u) = 
where K 3 0 is a fixed cost and c =- 0 is cost per unit. The demand w is a random variable taking values in a bounded interval [0, b], where b > 0, 
1 . 3  SOME NONSEQUENTIAL DECISION PROBLEMS 21 
with given probability distribution. There is a holding cost h 2 0 per unit inventory left over at the end of the period under consideration and a de- pletion cost p 2 0 per unit demand that is unmet. The holding and depletion costs may have a variety of more specific interpretations depending on the particular problem at hand. 
Given an initial inventory x the problem is to determine the additional inventory u to be ordered so as to minimize the total expected cost: 
J(u)  = C(u) + E {p max(0, w - x - u )  + h max(0, x + u - w)}. (23) 
By denoting 
L(y) = p E  (max(0, w - y)} + h E (max(0, y - w ) } ,  (24) 
the expected cost is written 
K + cu + L(x + u )  if u > 0 if u = 0. J ( u )  = 
We first note that L(y) is a convex function of y as can be easily seen from its definition. Hence the function G defined by 
G(Y) = C Y  + U Y )  
is also a convex function. Now let S be a value of y that minimizes cy + L(y) and s be the smallest value of y for which cy + LCy) = K + cS + L(S) (see Fig. 1.1). If c -= p ,  one may show that such values exist. This can be seen from the fact L'(y) = h, L'(y) = - p ,  where L' denotes the first derivative of L. Hence if c < p ,  we have l i m l , , l ~ m  G(y) = co and the existence of a minimizing scalar S is guaranteed. 
22 1 INTRODUCTION 
We will show that a value of u that, for a fixed value of x ,  minimizes the expected cost is given by the equation 
S - x if x < s, 
0 if x 2 s. 
u* = { 
In other words, the optimal ordering policy is characterized by a “critical” level s below which a positive quantity must be ordered and by a “target” level S to which the total inventory ( x  + u*) should be raised when a positive order u* is placed. 
Indeed if x 2 s, then from Fig. 1.1 it follows that 
cx + L(x)  < K + c(x + u )  + L(x + u )  Vu > 0, 
or equivalently L(x )  d K + cu + L(x + u). 
In view of the form of the cost functional [cf. Eqs. (23) and (25)] the above relation shows that for x 2 s no ordering (u  = 0) is optimal. 
If x < s, then from Fig. 1.1 again it follows that K + cS + L(S) < L ( x )  + cx K + cS + L(S) < K + c(x + u )  + L(x  + u )  Vu > 0, 
or equivalently 
J ( S  - X )  = K + c(S - X )  + L(S) < L(x) 
J ( S  - X )  = K + c(S - X )  + L(S) Q K + cu + L(x + U) VU > 0. 
These relations in view of (25) show that for x < s, ordering S - x is optimal. 
Thus the optimality of u* as given by (26) has been proved. 
An inventory ordering policy of form (26) is usually called an (s, S )  policy. Note that if K = 0 and if S is the smallest minimizing value of cy + L(y)  (for example, if it is the unique minimizing value), then one has s = S and the optimal policy is characterized by a single critical level. Such a policy may be called a “degenerate” (s, S) policy. Inventory control will be reexamined in a sequential framework in Section 3.2. 
1.3.4 Choice between Risky und Secure Assets 
An individual with given initial wealth ci wishes to invest part of it in a risky asset offering a rate of return e, and the rest in a secure asset offering rate of return s > 0. We assume that s is known with certainty while e is a random variable with known probability distribution P. If x is the amount invested in the risky asset, then the final wealth of the decision maker is given by 
y = s(ci - x )  + ex = sci + (e - s)x. 
1.3 SOME NONSEQUENTIAL DECISION PROBLEMS 23 
The decision to be made by the individual is to choose x so as to maximize 
J(x)  = E { U(y)}  = E { U[sa + (e - s )x] )  
subject to the constraint x 2 0. We shall assume that U is a concave, mono- tonically increasing, twice continuously differentiable function with negative second derivative, and with index of absolute risk aversion denoted 
r(Y) = - U”(Y)/U’(Y). (27) 
We also assume that the probability distribution of e is such that all expected values appearing below are finite, and furthermore we assume that the utility function U is such that the maximization problem has a solution (necessary and sufficient conditions for this to occur are given by Bertsekas [B12]). 
Now given a, the amount x* to be invested in the risky asset is determined from the necessary condition 
if x* > 0, (28) dJ(x*)/dx = E { ( e  - s)U’[sa + (e - s)x*]} = 0 
dJ(x*)/dx d 0 if x* = 0. 
Now since CJ’ is everywhere positive it follows that if E {(e - s)} > 0, then 
we cannot have x* = 0 since 
dJ(O)/dx = E { (e  - s)}U’(sa) > 0. 
Hence 
E {(e - s)} > 0 + x* > 0, 
or in words, a positive amount will be invested in the risky asset if its expected rate of return is greater than the rate of return of the secure asset. 
Assume now that E { ( e  - s)} > 0 and denote by x*(a) the amount 
invested in the risky asset when the initial wealth is a. We would like to investigate the effect of changes in initial wealth a on the amount invested x*(a). By differentiating (28) with respect to a (using the implicit function theorem) we obtain 
E {(e - s)U”[sa + (e - s)x*(a)] [ s  + (e - s) dx*(a)/da]} = 0, 
from which 
E {s(e - s)U”[sa + ( E  - s)x*(a)]} E {(e - ~ ) ~ U ” [ s a  + (e - s)x*(a)]} ‘ 
- -   
dx*(a) 
da 
Since the denominator is always negative and the constant s is positive, the sign of dx*(a)/da is the same as the sign of E { (e  - s)U”[sa + (e - s)x*(a)]}, 
which by (27) is equal to 
f ( a )  = - E { ( e  - s)U’[sa + (e  - s)x*(a)]r[sa + (e  - s)x*(a)]}. 
24 1 INTRODUCTION 
Now assume that the risk aversion index r(y) is monotonically decreasing, i.e., r(yl) > r (y2)  if y ,  < y , .  Then 
( e  - s)U’[sa + ( e  - s)x*(a)]r[sa + ( e  - s)x*(a)] dP(e) - SI, 
(e  - s)U’[sa + (e  - s)x*(a)] dP(e) 
+ SI, 
= -r(sa) dJ[x*(a) ] /dx  = 0, 
where we have utilized the fact that 
(e  - s)r[sa + (e  - s)x*(a)] < (e  - s)r(sa) 
with strict inequality if e # s. Thus we havef(a) > 0 and hence dx*(a)/da > 0 if r (x)  is monotonically 
decreasing. Similarly, we obtain dx*(a)/da < 0 if r (x)  is monotonically increasing. In words, the individual, given more wealth, will invest more (less) in the risky asset if his utility function has decreasing (increasing) index of absolute risk aversion. Aside from its intrinsic value, this result reaffirms the important role of the index of risk aversion in shaping significant aspects of a decision maker’s behavior. 
1.3.5 Investment Problems- Mean- Variance Analysis 
Consider an investor who wishes to allocate a certain amount of wealth A among n different risky investment opportunities offering corresponding rates of return e l , .  . . , en.  We assume that e l , .  . . , en are random variables 
with given joint probability distribution. If amount x i ,  i = 1, . . . , n, is 
allocated to investment opportunity i, the final wealth of the decision maker is a random variable y given by 
n 
y = C e i x i .  i= 1 
1.3 SOME NONSEQUENTIAL DECISION PROBLEMS 25 
Let us consider the problem of selecting xlr . . . , x, so as to maximize 
where U is a utility function. The maximization is subject to x i  = A and 
other constraints on xl, . . . , x,, which we denote by (xl, . . . , x,) E X c R". 
This is a very significant problem and arises often in a practical setting. It has been studied extensively for many years and various approaches have been suggested for its formulation and solution. First of all, it should be mentioned that it is essential to consider the problem in terms of a nonlinear utility function, for if one were to formulate the problem as one of maximiza- 
tion of the expected revenue E {I;= e i x i }  subject, for example, to the con- 
straints x i  = A, x i  2 0, i = 1, . . . , n, the resulting optimal allocation 
would be to invest exclusively in the asset that gives the greatest expected return regardless of the risk that such an allocation would entail. This be- havior i.s, however, contrary to real-life observations, which clearly indicate that most people find it advantageous to diversify their investments in the presence of uncertainty. 
Now the solution process of a problem of the type described may be divided into three phases, which may partially overlap. The first phase is to collect and analyze data that will be used to determine the probability dis- tribution of the rates of return e l ,  . . . , en. The Second phase is to examine the 
probabilistic properties of the total return y = cy= eixi for various feasible 
allocations ( x l ,  . . . , x,), while the third phase is actually to determine an optimal allocation (x:, . . . , x,*) that maximizes the expected utility E { U(y)}.  
A major difficulty with the actual solution is that while the first two phases will ordinarily be carried out by specialists the last phase will by necessity involve the (usually nonspecialist) investor since he is the only one who, through his attitude toward risk (or equivalently through his utility function), will determine the character of the allocation that he prefers .It is of course conceivable that the investor could reveal to the specialist his utility function via experimentation and the specialist could in turn derive the optimal allocation by solving the corresponding maximization problem. However, aside from the fact that such a procedure is time consuming and meaningless to the nonspecialist investor, it has the further disadvantage that a separate problem must be solved for each investor and for each level of investment. A very popular alternative approach to the problem is the so-called mean- variance approach. In this approach each allocation ( x l , .  .. , x,) is char- 
acterized by the mean and the variance of the corresponding total return y = e i x i .  The investor is called upon to decide the combination of mean and variance that he prefers-a much more meaningful process to him. 
26 1 INTRODUCTION 
The approach is also often very economical from the computational point of view as we shall explain shortly. 
The basic assumption of the mean-variance approach is that the objective E { U b ) }  can be expressed in terms of the mean 
E { Y )  = Y(xl?. . . ,xn) 
and the variance 
E{(Y - E { Y } ) ~ )  = 02(x1, . . . , x n )  
of the random variable y. This fact holds true if U is a quadratic utility function or if the distribution of y is characterized completely by its mean and variance for every x l ,  . . . , x, (for example, if y has a Gaussian distribution or more 
generally a two-parameter distribution). Under these circumstances the problem becomes one of maximizing 
E { u(y)I = CCY(x1, . . * 9 XA 02(x1, . . ., xn)] 
subject to the constraints on x l ,  . . . , x,, where G is the function expressing 
E { ~ ( y ) )  in terms of j ,  02. 
Now for most decision makers it seems reasonable that G should be increasing as 7 is increasing and decreasing as o2 is increasing. In other words, the decision maker prefers a large average return but wishes to avoid a large variance, which is associated with large risk-an attitude consistent with risk aversion. We assume that this is indeed so. Then if x:, . . . , x,* is a 
solution of the problem, it is clear that x:, . . . , x,* must also solve the problem 
minimize 
subject to 
a2(x1,. . , x,) 
E x i  = A ,  ( x l , .  . . , x,)EX, Y(xl,. . . , x,) 2 m*, 
n 
i =  1 
where m* = j(x7,. . . , x:). 
Thus we need only look for possible solutions of problems of the form 
minimize 02(x1, . . . , x,) 
subject to c xi = A,  (xl, . . . , x,) E X ,  fix, . . . , x,) 2 m, 
where m is a scalar. This problem can be written 
n 
i =  1 
minimize X’QX 
subject to E x i  = A ,  x EX,  cCixi  >, m, n n 
i =  1 i =  1 
1.3 SOME NONSEQUENTIAL DECISION PROBLEMS 27 
where x = (x l , .  . . , xn), Fi = E {e i } ,  and Q is the covariance matrix of the vector (el, . . . , en): 
11. (el - c?~)'. . (el - el)(e,, - c,,) 
Q =  E { [  (en - ?,,)(el - F l ) .  . . ( en  - Cn)2 
It is a problem that can be solved by standard nonlinear programming techniques. 
By solving the problem above repeatedly for various values of m we obtain a locus of pairs { lol(m),  j ( m ) } ,  where 1 0 1  is the standard deviation (square root of a2) as shown in Fig. 1.2. The pairs { I cr I (m), J(m)}  correspond to m via the optimization problem above. Usually a higher mean j j  is also associated with a higher 1 0 1  (higher risk), in which case the curve has a positive slope as shown in Fig. 1.2. 
.II 
FIGURE 1.2 
As a result of the preceding analysis the investment problem has been reduced to choosing a point on the mean standard deviation locus, a task that is relatively easy and meaningful to an investor. In this way the various tasks involved in the solution process can be separated. The probability distribu- tion of the returns of the risky assets will be determined by professionals, and the mean standard deviation locus will be determined via computational solution of the related optimization problems. Then the individual investor will be called upon to decide on a point on the mean standard deviation locus that will determine the amount he will invest in each opportunity. 
Important simplifications and computational economies result in the frequent case where the constraint set X is a cone with vertex at the origin, 
i.e., when X has the property that (Axl, . . . , Ax,,) E X for every 1 2 0 and 
(xl, . . . , x,,) E X .  This is the case, for example, when X = R" or when X is the positive orthant 
X = { ( x ~ ,  .. ., x,) Ix i  2 0, i = 1,. .., n}. 
28 1 INTRODUCTION 
Under these circumstances one may formulate the minimization problem (29) in terms of the fractions of total investment 
ai = xJA,  i = 1,.  . . , n, 
rather than the actual amounts x l , .  . . , x, to be invested. Thus when X is a 
cone with vertex at the origin, the minimization problem (29) may be written 
minimize A2(a’Qa) 
subject to 1 ai = 1, a E X, 1 ?,ai 2 m/A.  
This problem may be solved for A = 1 and various values of m. The corre- sponding mean standard deviation locus may be viewed as the set of mean standard deviation pairs “per unit of total investment.” Given a pair { 1 IT 1, j }  on this locus it is easy to see that the corresponding standard deviation and mean associated with a total investment of A monetary units will be A I IT I and A j ,  respectively. In this way a mean standard deviation locus constructed for a single level of total investment may be used for any level of investment. Thus the approach allows a once and for all computation, valid for every level of investment and hence for every investor. 
n n 
i =  1 i =  1 
1.4 A Model for Sequential Decision Making 
The class of decision problems considered in the first two sections of this chapter is very broad. In this text we are primarily interested only in a subclass of such decision problems. These problems involve a dynamic system. Such systems have an input-output description and furthermore in such systems inputs are selected sequentially after observing past outputs. This allows the possibility of feedback. Let us first give an abstract description of the type of problems with which we shall be dealing. 
Let us consider a system characterized by three sets U, W, and Y and a function S :  U x W + Y. We shall call U the input set, W the uncertainty set, 
Y the output set, and S the system function. Thus an input u E U and an un- certain quantity w E W produce an output y = S(u, w)  through the system function S (Fig. 1.3). Implicit here is the assumption that the choice of the input u is somehow controlled by a decision maker or device to be designed while w is chosen, say, by Nature according to some mechanism, probabilistic or not. 
In many problems that evolve in time, the input is a time function or sequence and there may be a possibility of observing the output y as it evolves in time. Naturally this output may provide some information about the 
1.4 A MODEL FOR SEQUENTIAL DECISION MAKING 29 
c IV 
uncertain quantity w, which can be fruitfully taken into account in choosing the input u by means of a feedback mechanism. 
Definition We say that a function n: Y + U is a feedback controller 
(otherwise called policy or decisionfunction) for the system if for each w E W the equation 
u = n[S(u, w)] 
has a unique solution (dependent on w) for u. Thus for any fixed w, a feedback controller n generates a unique input u 
and hence a unique output y (Fig. 1.4). In any practical situation the class of 
I V  
1 1  
.I’ = S(u. w )  
FIGURE 1.4 
admissible feedback controllers is further restricted by causality (present inputs should not depend on future outputs), and other practical requirements. 
Now given the system (U, W, Y, S) and a set of admissible feedback con- trollers II it is possible to formulate a decision problem in accordance with the theory of the previous section. We take ll as the decision set and Was the set of states of nature. We take as the set of outcomes the Cartesian product of U ,  W, and Y, i.e., 0 = (V x W x Y). Now a feedback controller R E  II and a state of nature w E Wgenerate a unique outcome (u, w, y), where u is the unique solution of the equation u = n[S(u, w)] and y = S(u, w). Thus we may write (u, w, y )  = f ( n ,  w), where f is the function determined by the system function S. 
30 1 INTRODUCTION 
If G is a numerical function ordering our preferences on 0, J the corre- sponding payoff function for the decision problem above, and a min-max viewpoint adopted, then the problem takes the form of finding n E l7 that maximizes 
F ( n )  = inf J(n, w) = inf G(u,  w, y) 
where u and y are expressed in terms of n and w by means of u = n[S(u, w)] andy = S(u, w). 
If w is selected in accordance with a known probabilistic mechanism, i.e., a given probability measure that may depend on n, and the function S and the elements of l7 satisfy suitable (measurability) assumptions, then it is possible to formulate a decision problem by means of a utility function. Find n E I-I that maximizes 
F ( 4  = E { u ( u ,  w, Y)) 
where u and y are expressed in terms of n and w by means of u = n[S(u, w)] and y = S(u, w). 
W E  w W E  w 
n' 
We shall be mostly dealing with problems of this second type. Of course, on the basis of the formulation given one can say that problems 
of decision under uncertainty can be reduced to problems of decision under certainty-the problem of maximizing over l7 the numerical function F(n). However, it is important to realize that due to the feedback possibility the set n is a set offunctions (of the system output). This fact renders deterministic optimization techniques such as mathematical programming or Pontryagin's maximum principle inapplicable, and the only formulation that offers some possibility of analysis is the so-called method of dynamic programming (DP). In D P  the problem of minimizing F ( n )  is decomposed into a sequence of much simpler optimization problems that are solved backwards in time. 
A Discrete-Eme Sequential Decision Model 
In this text we are primarily interested in the analysis of DP techniques that are applicable to a specific but quite broad class of optimization pro- blems under uncertainty. This class of problems involves a dynamic system evolving in discrete time according to the equation 
Xk+i=fk(Xk,UkrWk)r k = o , 1 , . . - , N - l ,  (30) 
where xk denotes the state of system, u k  a control input, and wk an uncertain parameter or disturbance. The functionsf, are given and xk, uk, wk are ele- ments of appropriate sets (or spaces). The system operates over a finite number of stages N (a Jinite horizon). We shall mostly assume that wk is selected according to a probabilistic mechanism that depends on the current 
1.4 A MODEL FOR SEQUENTIAL DECISION MAKING 31 
state xk and control input u k ,  but does not depend on the values of the prior uncertain parameters w o ,  w l ,  . . . , wk- It will be assumed that the control 
inputs u k  are selected by a decision maker or controller that has knowledge of the current state xk (perfect state information). Thus a feedback controller of the form 
{ p O ( x O ) ,  p l ( x l ) ,  * .  . 9 pN- l ( x N -  1)) 
is sought. This feedback controller is a sequence of functions of the current state and can be viewed as a plan that tells us that when at time k the state is xk,  
then the control u k  = p k ( X k )  should be applied. This controller must satisfy various constraints [for example, pk(xk) E Uk for all x k ,  where Uk is a given constraint set] that depend on the problem at hand. 
In terms of our earlier model the system input is u = {u, ,  ul, . . . , u N -  
the uncertain quantity is w = { w o ,  w l ,  . . . , w N -  1}  (perhaps together with the initial state x o ,  if x o  is uncertain), the output is y = { x o ,  x l ,  . . . , x N } ,  and 
the system function S is determined in an obvious manner from the system equation (30). The class II of admissible feedback controllers is the set of sequences of functions 7c = {po ,  . . . , p N -  ]}, where pk is a function of the output y of the form &(y) = pk(xk). Furthermore, ,uk must satisfy constraints depending on the problem. 
We shall assume that the utility function has an additive structure of the form 
N -  1 
U(u, w, y )  = U N ( X N )  + 1 U k ( X k ,  uk, w k ) .  
k = O  
Thus the problem becomes one of finding an admissible n* = {&, . . . , pE- that maximizes 
1 N -  1 
J n  = J(p03 . . . 7 P N -  I )  = U N ( X N )  + 1 U k [ x k y  p k ( x k ) ,  w k ]  
k = O  
subject to the system equation constraints 
x k + l  = . f k [ x k ,  pk(xk), w k l ,  k = 0, 1, . . . 9 N - 1, 
and any other existing constraints on the feedback controller. We note that the description of the problem given above is intended to be informal. A precise definition together with examples will be provided in the next chapter. 
Dynamic programming is directly applicable to problems of this form. Furthermore, as will be shown later, various other dynamic optimization problems involving, for example, correlated disturbances, imperfect state information, and nonadditive cost function, can be directly reformulated into the problem described above (perhaps by introducing a more complex 
32 1 INTRODUCTION 
structure). Finally it is possible to let the final time N go to infinity, which is the case of an inJinite time horizon. 
We finally should point out that while we refer to k as the time index and to system (30) as a discrete-time system, it is not necessary that the index k have a time interpretation. For example, consider the problem of finding quantities u o ,  . . . , u N -  of N products to be purchased so as to satisfy the 
constraint 
N -  1 
1 p k U k  = A 
k = O  
and minimize the cost N -  1 
1 gk(Uk), 
k = O  
where A, Po,  . . . , f l N -  are given scalars and g o ,  . . . , g N -  are given functions. 
By defining the system equation to be 
(31) xk+l = xk + fikuk, k = 0, 1,. . . , N - 1 ,  
with an initial state xo = 0, the problem becomes one of minimizing N -  1 
1 gk(Uk) 
k = O  
subject to the system equation (31) and the terminal state constraint x N  = A. Clearly this problem can be put into the framework considered in this section. 
Relation to Transition Probability Models 
It is to be noted that often the system equation is not given in form (30); rather one is given the set of transition probabilfiies P(xk+ Ixk, uk) of the system moving from state xk to state xk+ when the control input is uk. This is typically the case when the controlled system is a finite state Markov chain, or when the problem involves analysis of a decision tree [Rl]. In this case it is still possible to define a system equation of form (30) by letting the space of uncertain parameters wk be the same as the space of xk+ and by defining the system functionsf, to be of the form 
f k ( x k  9 uk 9 w k )  = wk 
and letting the probability distribution of wk be equal to the given transition probability distribution P(&+ Ixk, uk). The system equation is simply X k + l  = wk and the occurrence of a particular value of wk is equivalent to transition to the corresponding state xk+ 1. The transition probabilities de- pend on the current state xk and the control uk that is applied. 
1.5 NOTES 33 
EXAMPLE Consider a controlled process that can be in one of two possible states 1 and 2. In other words S = { 1,2}, where S is the state space. Let there be two possible controls u1 and u' at each state, i.e., the control space is C = {u', u'}. Let the transition probabilities pi&") of moving from state i to statej when the control un is applied, i ,  j ,  n = 1, 2, be given by 
pll(ul)  = alr  plz(uz) = 1 - a', 
P21(U1) = P 1 ,  p z z ( u 2 )  = 1 - pz, 
where a,, u z ,  /I1, P2 E [0,1]. Then this controlled process may be represented 
by the system equation 
plz(u') = 1 - a,, 
PZZ(U')  = 1 - P,, 
pll(u2) = m a ,  
p21(u2) = P 2 ,  
x k + l  = w k ,  
where wk is a random variable taking the values 1 and 2 with probability distribution depending on x k  and u k  as follows: 
It is to be noted that we could also consider the reverse transformation whereby we start from the system equation xk+ = A(&, u k ,  wk) and con- struct an equivalent model specified by means of transition probabilities 
P(xk+ , Ixk, uk). The choice of model is clearly a matter of taste and does not 
affect in any way the results to be obtained. 
1.5 Notes 
Utility theory and its relation to decision making were first clarified by von Neumann and Morgenstern "31. For an extensive account of related results see the text by Fishburn [F3] and for a bibliography see the survey paper by the same author [F2]. The text [F3] also contains Savage's expected utility theory, which is based on the notion of subjective probability [S4]. Other sources describing the expected utility theory are Luce and Raiffa [L7], Blackwell and Girshick [B23], Owen [03], and DeGroot [Dl]. Blackwell and Girshick [B23] also describe Wald's statistical decision theory, 
34 1 INTRODUCTION 
which formulates the decision problem as a game against Nature. The expected utility approach is by far the most popular approach for formulating prob- lems of decision under uncertainty. The min-max approach receives serious consideration occasionally. Another approach, which has not met with particular favor, is based on the min-max regret criterion of Savage [S3]. 
The material on quadratic cost functionals and least-squares estimation is standard. For detailed expositions see, for example, the work of Aoki [All ,  Meditch [M6], the IEEE special issue [Ill,  and the references listed therein. Inventory policies of the (s, S )  form were considered and analyzed in a pioneering paper by Arrow et al. [A6], which stimulated a great deal of work on the subject. The material on the investment problem is taken from Arrow [A41 and Mossin [M8]. For detailed expositions of the mean-variance approach see Markovitz [M4] and Sharpe [S9]. 
For an excellent treatment of decision problems under uncertainty that involve dynamic systems see the work of Witsenhausen [W4]. 
Problems 
1. Show that there exists a function G :  0 -, R satisfying relation (2) of 
Section 1.1 provided the set 0 is countable. Show also that if the set of decisions is finite, there exists at least one noninferior decision. 
2. Let 0 = [ - 1, 13. Define an order on 0 by means of 
0,  i 02%1011 < 1021 or 0 ,  < O2 = lo,!. 
Show that there exists no real-valued function G on Lo such that 
01 0 2  % G(O1) < G(O2) t 1 0 1 , 0 2  E 0. 
Hint Assume the contrary and associate with every 0,  E (0, 1) a rational number r ( 0 , )  such that 
G(-O,) < do,) < G(0,) .  
Show that if 0,  # O,, then r ( 0 , )  # r ( 0 2 ) .  3.  Experimental Measurement of Utility Consider an individual faced with a decision problem with a finite collection of outcomes 01, 02 ,  . . . , O N .  
It is assumed that the individual has a preference relation over the set of lotteries on the set of outcomes satisfying Assumptions A.l-A.4 of the ex- pected utility theorem, and hence a utility function over the set of outcomes exists. Suppose that 0,  < O2 < . . . < ON and furthermore that 0,  i O N .  
Show that the following method will determine a utility function. Define U ( 0 , )  = 0, U(0,) = 1. Let pi with 0 < pi < 1 be the probability for 
which one is indifferent between the lottery ((1 - pi), 0, . . . , 0, p i }  and Oi 
(a) 
PROBLEMS 35 
occurring with certainty. Then let U(Oi)  = pi. Try the procedure on yourself for Oi = $50i with i = 0, 1 , .  . . , 10. 
(b) Show that the following procedure will also yield a utility function. Determine U(ON-  1) as in (a) but set 
where p N p 2  is the probability for which one is indifferent between the lottery 
((1 - d N - 2 ) ,  0, . . . , pN- 2 ,  0) and O N - 2  occurring with certainty. Similarly 
set U(Oi) = f i i U ( O i + l ) ,  where fii is the appropriate probability. Again try this procedure on yourself for Oi = $50i with i = 0, 1 , .  . . , 10 and compare the results with the ones obtained in (a). 
(c) Devise a third procedure whereby the utilities U(O,),  U ( 0 , )  are 
specified initially and U(Oi), i = 3, . . . , N ,  is obtained from U(Oi-2), U(Oi- 1) 
through a comparison of the type considered above. Try the procedure for Oi = $50i, i = 0, 1,. . . , 10. 4. Suppose that two people A and B desire to make a bet. Person A will pay $1 to person B if a specific event occurs and person B will pay x dollars to person A if the event does not occur. Person A believes that the probability of the event occurring is pA with 0 < p A  < 1, while person B believes that the corresponding probability is pB with 0 < pB < 1 .  Suppose that the utility functions U A  and UB of persons A and B are strictly increasing functions of monetary gain. Let CI, B be such that 
Show that if CI < /I, then any value of x between a and B is a mutually satis- 
factory bet. 5. In the problems of Sections 1.3.1-1.3.5 identify a set of decisions, a set of states of nature, a set of outcomes, and a utility function (or cost function). 6 .  In the inventory problem assume that the holding and depletion costs do not have the linear form considered but are such that the sum of the expected holding and depletion costs is a convex function of (x + u). Show under appropriate assumptions that the optimal ordering policy is of the (s, S )  type. 7. Consider a roulette wheel that is partitioned into k disjoint events A , ,  . . . , Ak such that the probability of occurrence of A i  is pi, i = 1 , .  . . , k, and If= pi = 1.  Suppose a person is given an amount of x dollars that he can allocate among the k events A , ,  . . . , A ,  and that he receives as his reward the 
amount xi that he has allocated to the event Ai  that actually occurs. The 
constraints are xi 2 0, If=l xi = x. Suppose that his utility function over 
36 1 INTRODUCTION 
positive monetary rewards r is U(r)  = In r. Show that his preferred allocation is given by x i  = p i x ,  i = 1 ,  . . . , k. 
8. In an investment problem such as the one considered in Section 1.3.5 assume that there are two investment opportunties with g1 = 1.5, 2’ = 1.8, and E { ( e ,  - el)’} = 0.5, E{(ez  - Z,)’} = 1, and E { ( e ,  - e , ) (e ,  - Z,)} = 0. 
Compute the mean standard deviation locus for a unit of capital invested and for the two cases where X = RZ and X = { ( x l ,  x 2 ) ( x l  2 0, x 2  2 O } .  
Part I 
Control of Uncertain Systems over a Finite Horizon 
This page intentionally left blank
Chapter 2 
The Dynamic Programming Algorithm 
2.1 The Basic Problem 
In this section we formulate the basic problem of optimal control of a dynamic system over a finite horizon with which we shall be dealing. The formulation is very general since the state space, control space, and uncer- tainty space are arbitrary and may vary from one state to the next. In parti- cular, the system may be defined over a finite or infinite state space. The problem is characterized by the fact that the number of stages of evolution of the system is finite and fixed (finite horizon), and by the fact that the control law is a function of the current state (perfect state information). However, problems where the termination time is not fixed or where the controller may decide to terminate the process prior to the final time can be reduced to the case of fixed termination time (see Problem 8). The situation in which the controller has imperfect state information can also be reduced to a problem with perfect state information as will be seen in Chapter 4. A variety of related problems can also be reduced into the form of the basic problem (see Section 2.3 and the problem section). 
39 
40 2 THE DYNAMIC PROGRAMMING ALGORITHM 
Basic Problem 
Given is the discrete-time dynamic system 
x k + l  = f k ( x k , u k , w k ) i  k = 0 , 1 , . . . , N -  1, (1) where the state x k  is an element of a space s k ,  k = 0, 1,. . . , N ,  the control 
u k  is an element of a space c k ,  k = 0, 1, . . . , N - 1, and the random “dis- 
turbance’’ w k  is an element of a space D k ,  k = 0, 1, . . . , N - 1. The control 
u k  is constrained to take values from a given nonempty subset U k ( X k )  of C k ,  
which depends on the current state x k  [ u k  E U k ( X k )  for all x k  E S k  and k = 0, 
1,. . . , N - 11. The random disturbance w k  is characterized by a probability 
measure Pk(  * I x k ,  u k )  defined on a collection of events in D k  (in the sense of Appendix C). This probability measure may depend explicitly on xk and u k  
but not on values of prior disturbances w k -  1, . . . , wo . We consider the class of 
control laws (also called “policies”) that consist of a finite sequence of func- 
for all x k  E s k .  Such control laws will be termed admissible. 
law IL = {po,  p i ,  . . . , p N -  1} that minimizes the cost functional 
tions IL = {Po, pi, . . . , P N -  I } ,  where p k :  S k  --f C k  and such that /Ak(Xk) E U k ( X k )  
Given an initial state x o ,  the problem is to find an admissible control 
subject to the system equation constraint 
x k +  1 = f k [ x k ,  /Ak(xk) ,  w k ] ,  = O, . . 3 - (3) 
The real-valued functions 
are given. 
Let us provide an example that illustrates the nature of the basic problem above. Many other examples will be given subsequently. 
INVENTORY CONTROL EXAMPLE Consider an N-period version of the in- ventory problem of Section 1.3. We assume that inventory can be ordered at the beginning of each of N time periods rather than just once. Naturally each inventory order is made with knowledge of the current stock so that instead of seeking optimal numerical values for the inventory orders we are now interested in an optimal rule that tells us how much to order for every level of current stock and for each time period. Let us denote 
g N : S N + R ,  g k : S k  X C k  X D k + R ,  k = 0 , 1 ,  ..., N -  1, 
x k  stock available at the beginning of the kth period u k  stock ordered (and immediately delivered) at the beginning of the 
kth period 
2.1 THE BASIC PROBLEM 41 
wk demand during kth period with given probability distribution h holding cost per unit item remaining unsold at the end of the kth 
period c cost per unit stock ordered p shortage cost per unit demand unfilled 
We assume that w o ,  . . . , w N -  are independent random variables and that 
excess demand is backlogged and filled as soon as additional inventory becomes available. This is represented by negative stock in the system equa- tion, which is given by 
x k + l  = xk + uk - wk. 
The cost functional (representing expected loss) to be minimized is given by 
E 1 [ C U k  + p max(0, wk - xk - uk) + h x k  + u k  - wk)] . {::: I 
Here we assume that unfilled demand at the beginning of the Nth period is lost and the stock x N  that is left over has no value (i.e., the terminal cost is zero). 
The objective is to find an ordering policy { p o ,  . . . , p N -  1}, u k  = p k ( x k ) ,  
k = 0,. . . , N - 1, that minimizes the expected cost. Clearly this problem is 
within the framework of the basic problem of the previous section with the identifications 
g N ( X N )  = O, 
g k ( X k ,  uk, wk) = C u k  + p max(0, wk - xk - u k )  + h max(0, xk + uk - wk), 
f k ( x k ,  U k r  wk) = xk + ilk - wk, 
uk(xk)  = [o, 
Optimal Value of the Basic Problem 
It is to be noted that while the objective in the basic problem is to find an admissible control law that minimizes the cost functional J,(xo), it is not guaranteed a priori that such a minimizing control law exists. It is possible that J,(xo) can attain arbitrarily small values by suitable choice of the control 
law n, in which case we say that the opJimal value is - co and no control law 
attains this value.? It is also possible that the set of values that J,(xo) attains as n ranges over the set of admissible policies l is bounded below but no optimal control law exists (in the same way that, for example, the scalar function e' is bounded below by zero but it is not minimized by any scalar t ) .  
t Such a situation will almost never occur in practice if our problem is well formulated. 
42 2 THE DYNAMIC PROGRAMMING ALGORITHM 
The greatest lower bound of the set of real numbers {Jn(xo) ln  E n}, i.e., the set of all values of the cost function Jn(xo)  that can be attained by using admissible policies n E n, is denoted 
J*(xo)  = infJ,(xo) 
and is called the optimal ualue of the problem. When an optimal policy n* exists, we write 
J*(xo)  = J, , (xo)  = min Jn(xo) .  
When there does not exist an optimal policy we may be interested in finding an c-optimal policy, i.e., a policy it such that 
npn 
n e n  
J*(xo) < J,(xo) d J*(xo)  + E ,  
where E is some small number implying an acceptable deviation from op- timality. 
Note that the optimal value of the problem depends on the initial state xo. Naturally, different initial states may have different optimal values associated with them. We shall refer to the function J* that assigns to each initial state xo the corresponding optimal value J*(xo)  as the optimal ualuefunction. 
The Role of Information Gathering in the Basic Problem 
As indicated in the basic problem every control law { p o ,  pl ,  . . . , p,,- 1 }  
consists of functions of the current state. The physical interpretation of the associated process is that at each time k the controller (which may be a device or a decision maker, depending on the situation) observes the exact value of the current state x k  and applies a control pk(xk) as shown in Fig. 2.1. Subsequently the disturbance wk occurs and the next state xk+ is generated according to system equation (3). This state is observed by the controller, which subsequently applies the control pk+ I ( & +  1) specified by the function 
2.1 THE BASIC PROBLEM 43 
pk+ and the process is repeated. Thus a control law {po ,  pl ,  . . . , pN- may 
be viewed as a plan that specifies the control to be applied at each time for every state that may occur at that time. 
It is important to realize that this mode of operation of the control law implies information gathering during the control process. The information received by the controller is the value of the current state at each time. Further- more, this information is utilized directly during the control process since the control at time k depends on the current state xk via the function pk. The effects of the'availability of this information by the controller may be sig- nificant indeed. The reason is that if this information were not available, then the controls applied would not depend on the current state, i.e., the control uk would have to be the same for every value of the state xk that may occur. As a result the cost functional would have to be optimized over all sequences of controls {u,,, u l , .  . . , u N -  I }  satisfying the constraints of the problem and the resulting optimal value would be higher than the optimal value of the basic problem. This fact is intuitively clear and is illustrated well by the ex- ample given immediately before Section 1.1. It may be proved mathematically by observing that the set of control laws that consist of constant functions (i.e., functions independent of the current state) is only a subset of the set of admissible control laws. As another example, the reader may consider the inventory control problem considered earlier in this section where the in- formation possessed by the inventory manager at the beginning ofeach period k is the current inventory stock xk. Clearly this information can be very important in deciding on the appropriate amount uk to be ordered at the kth period. 
It is to be noted, however, that it is not necessary that knowledge and utilization of the information provided by the value of the current state lead to a net reduction of the value of the cost functional. For instance, in deter- ministic control problems (where no uncertain disturbances are present), optimization of the cost functional over all sequences { u o ,  u l ,  . . . , uN- 1}  of 
controls leads to the same optimal value as optimization over all admissible control laws. This fact is illustrated in the example given prior to Section 1.1 and will be further discussed in the following. The same fact may be true even in some stochastic control problems. An important class of such pro- blems is described in Problem 13. 
Theoretical Limitations of the Formulation of the Basic Problem 
Before proceeding with the development of the dynamic programming algorithm, it is necessary to clarify certain aspects of our problem and to delineate certain probabilistic elements in the formulation that do not lie on firm mathematical ground. 
44 2 THE DYNAMIC PROGRAMMING ALGORITHM 
First of all, once an admissible control law { p o ,  pl, . . . , pN- 1}  is adopted, 
Stage 0 (1) The controller observes x o  and applies uo = po(xo).  ( 2 )  The disturbance wo is generated according to the given probability 
( 3 )  The cost g o [ x o ,  po(xo), wo]  is incurred. (4) The next state x 1  is generated according to the system equation 
the following underlying sequence of events is envisioned : 
measure Po( - I x o ,  po(x0)). 
x1 = f O C X 0 ,  P O ( X O ) ?  W o l .  
Stage k (1) The controller observes xk and applies uk = pk(Xk). (2) The disturbance wk is generated according to the given probability 
( 3 )  The cost g k [ X k ,  & ( X k ) ,  wk] is incurred and added to previous costs. (4) The next state xk+ is generated according to the system equation 
Pk( ' I x k ,  l (k (Xk) ) -  
x k  + 1 = f k C X k  7 pk(Xk)? w k l .  
Last Stage ( N  - 1) (1) The controller observes x N -  and applies 
UN- 1 = PN- i b N -  1). 
(2) The disturbance w ~ - ~  is generated according to the given pro- 
(3) The cost gN- l [ x N -  1, pN- 1(xN- 1), w N -  1 ]  is incurred and added to 
(4) The final state x N  is generated according to 
bability measure P N -  1( - IxN- 1, pN- l ( x N -  l)). 
previous costs. 
x N  = f N -  1 C x N -  1, P N -  l ( x N -  1 1 3  w N -  1 1 .  
(5) The terminal cost g N ( x N )  is incurred and added to previous costs. The above process is well defined and couched in precise probabilistic 
terms. Formidable complications, however, are introduced by the need to view the cost functional 
N- 1 
g N ( X N )  + 1 g k C X k ,  pk(xk), w k l  
k = O  
as a well-dejined random variable with well-defined expected value. The framework of probability theory requires that for each { p o ,  pl, . . . , pN- 1} we 
define an underlying probability space, i.e., a set R, a collection of events in R, and a probability measure on these events. Furthermore, the cost functional above must be a well-defined random variable on this space in the sense of Appendix C (a measurable function from the probability space into the real line in the terminology of measure-theoretic probability theory). In order for this to be true, additional (measurability) assumptions on the functions fk, gk, and pk may be required and it may be necessary to introduce additional structure on the spaces Sk, ck, and D k .  Furthermore, these assumptions may 
2.1 THE BASIC PROBLEM 45 
restrict the class of admissible control laws since the functions pk may be constrained to satisfy additional (measurability) requirements. 
Thus unless these additional assumptions and structure are specified, the problem we consider is formulated inadequately and the reader should view subsequent developments in the light of this fact. On the other hand, a rigorous formulation of the basic problem for general classes of state, control, and disturbance spaces is well beyond the mathematical and probabilistic framework of this introductory text and will not be undertaken here. None- theless we feel that these mathematical difficulties (at least for finite horizon problems) are mainly of a technical nature and do not affect in a substantial manner the basic results to be obtained and the basic structural properties of the problem with which we are concerned. For this reason we find it con- venient to proceed with formal derivations and arguments in much the same way as in most introductory texts and journal literature on the subject. 
We would like to stress, however, that under the assumption that the disturbance spaces Dk, k = 0, 1 ,  . . . , N - 1, are countable sets all the mathe- 
matical difficulties mentioned above disappear since for this case, with the only additionalassumption that the expected values of all terms in the expression of the cost functional (2 )  exist and arefinite for every admissible policy n, one can provide a sound framework for the problem. 
One easy way to dispense with all the difficulties of a probabilistic nature when the disturbance spaces Dk are countable sets is to rewrite all expected values in the cost functional as infinite sums in terms of the probabilities of the elements of Dk. Thus if w:, w:, . . . are the elements of Dk, 
andp:(xk, uk)denotes theprobabilityofwi, k = 0, 1 ,  . . . , N - 1 , i  = 1, 2, . . . , 
the value of the cost functional (2 )  corresponding to an admissible policy n could be written alternatively as 
Dk = {W:, W:, . . .}, 
Jn(X0) = J%O) ,  
where J:(xo)  is given by the last step of the recursive algorithm, which pro- 
ceeds backwards from stage N - 1 to stage 0: 
m 
J ? l ( x N - l )  = 1 P k -  1 C x N -  1, pN- l ( x N -  111 
i =  1 
[ g N [ f N -  l ( x N -  1, pN- l(XN- 1 h  wk- 111 + gN-l[XN-l, ~ N - l ( ~ N - 1 ) ~ ~ ~ - 1 1 1 ,  
m 
Jk,(xk) = 1 P : C x k ,  pk(Xk)I b k [ x k ?  pk(xk), w:l 
i =  1 
+ Jk,+ [.hc(xk, pk(xk), w:)]l? k = 0 , 1 ,  ..., N - 2 .  
46 2 THE DYNAMIC PROGRAMMING ALGORITHM 
In these equations the form of JF- ' ( x N  - 1 )  is obtained once we substitute the system equation in the expression 
E { S N ( X N )  + S N - l C X N - l , p N - l ( X N - l ) r  W N - 1 1 )  W N  - I 
which represents expected cost for stage N - 1 plus the expected terminal cost when the state at stage N - 1 is equal to x N -  and the policy n is used. 
Similarly Jk , (xk )  may be viewed as expected cost for the last N - k stages 
when the state at stage k is x k  and the policy n is used. In the above expressions we have written out the expected values explicitly in terms of the probabilities p : [ X k ,  p k ( X k ) ] .  When the sets Dk are known to be finite then all infinite sums may be replaced by finite sums. If one makes the additional assumption that all the infinite sums in the above expression are well defined and finite for every admissible policy, then one can work directly with the expression of the cost functional above and bypass any need for posing the problem in a pre- cise probabilistic manner. In this formulation the use of expectations be- comes merely a convenient shorthand notation. 
There is another way, more probabilistic in nature, to ensure that the cost 
corresponding to a control law n = {po,  pl ,  . . . , pN- 1 }  is well defined when 
Dk are countable sets. One may rewrite the value of the cost functional J,(xo) as 
(4) 1 N- 1 
Jn (xO)  = E g N ( X N )  + s"k[xk, c (k (xk ) ]  7 
* I .  .. . , XN { k=O 
where 
gk'kcxk 9 p k ( X k ) l  = E {gkcxk 9 pk(xk), w k l  I xk 9 p k ( X k ) } ,  wk 
with the expectation above taken with respect to the probability distribution Pk( * J x k ,  p k ( x k ) )  defined on the countable set Dk. Then one may take as the basic probability space the Cartesian product of S1,  S 2 , .  . . , SN, where 
Sl = b 1  E S l I X 1  = f O C X 0 ,  PO(XO) ,  w019 wo E Do} .  
s k +  1 = { x k +  1 €Sk+ 1 Ixk+ 1 = fk [xk ,  p k ( x k ) ,  w k l ,  xk s k r  w k  € D k } ,  
k =  1,2 ,..., N -  1. 
The set sk is the subset of Sk of all states that can be reached at time k when the control law { p o ,  pl ,  . . . , pN-  1 }  is employed. The fact that Do, D1,.  ., D N -  
are countable sets ensures that sets s l , .  . . , sN are also countable (this is true 
in view of the fact that the union of any countable collection of countable 
2.2 THE DYNAMIC PROGRAMMING ALGORITHM 47 
sets is a countable set). Now the system equation (3), the probability dis- tributions Pk( - lxkr pk(xk)), the initial state xo, and the control law {pol pi ,  . . . , pN- l }  define a probability distribution on the countable set sl x 9, x 
. . . x sN and the expectation in (4) is defined with respect to this latter dis- tribution. In fact, it is easy to see that in this formulation the states {xo, xl ,  x2 ,  . . . , xN} form a finite Markov sequence [P2] that can be described completely by the corresponding conditional probabilities P(xk + I xk), which depend on the control law { p o ,  pi, . . . , pN- 1 }  employed and the data of the 
problem. In light of this fact, the cost functional (4) may be written 
JJxo) = BoCxo, ~o(xo)l  + E BiCx,, ~ i ( x i ) l  * I  i 
+ x2 E{. - -  + E~ {~N-i[xN-i,pN-i(xN-i)~ 
where the conditional probability distributions P(xk+ I xk),  depend on the control law 7c = { p o ,  pi ,  . . . , pN- l } .  This Markovian property lies at the heart of the dynamic programming algorithm. 
In conclusion the basic problem has been formulated in a mathematically rigorous way only for the case where the disturbance spaces D o ,  . . . , DN- 
are countable sets. In the absence of countability of Dk the reader should interpret subsequent results and conclusions only as plausible (imprecise) statements or conjectures. In fact, when discussing infinite horizon problems (where the need for precision is much greater) we shall make the countability assumption explicit. It is to be noted, however, that the advanced reader will have little difJiculty in establishing rigorously most of our subsequent results concerning specific applications in Chapters 3 and 4.  This can be done in a manner explained in the Notes to this chapter and in Problem 12. 
2.2 The Dynamic Programming Algorithm 
The problem of the previous section appears quite formidable since the cost functional (2) must be minimized over a class of functions of the current state. This fact together with the complexity of the cost functional make the use of variational optimization techniques impossible in almost every case. The dynamic programming (DP) technique decomposes the problem into a sequence of simpler minimization problems that are carried out over the control space rather than over a space of functions of the current state. 
48 2 THE DYNAMIC PROGRAMMING ALGORITHM 
The DP technique rests on a very simple idea, the so-called principle ~f optimality. The name is due to Bellman, who contributed a great deal to the popularization of DP and to its transformation into a systematic tool. Roughly the principle of optimality says the following rather obvious fact. 
Suppose that {pg, p:, . . . , pg- 1 }  is an optimal control law for the basic, 
problem. Consider the subproblem whereby we are at state x i  at time i and wish to minimize the “cost-to-go” from time i to time N 
r N- 1 
Then the (truncated) control law {p:, p:+ . . . , pg- 1}  is also optimal for this subproblem. 
It is perhaps helpful to introduce the dynamic programming algorithm by means of an example : 
INVENTORY CONTROL EXAMPLE (continued) Consider the inventory control example of the previous section and let us utilize the following pro- cedure for determining the optimal inventory ordering policy starting with the last time period and proceeding backward in time. 
N - 1 Period Assume that at the beginning of period N - 1 the stock 
available is xN- 1. Clearly no matter what happened in the past the inventory manager should order inventory ug- = pg- l ( x N -  which minimizes over uN- the sum of the ordering, holding, and depletion costs for the last time period, which is equal to 
E { c u ~ - ~  + h max(0, x N - ~  + u N - ~  - w N - 1 )  
+ p max(0, w N - 1  - xN-1 - u N - 1 ) ) .  
W N - I  
Let us denote the optimal cost for the last period by JN- l(xN- 1 ) :  
J , - ~ ( X ~ - ~ )  = min E { C U ~ - ~  + h max(0, x ~ - ~  + U N - 1  - w N - 1 )  
U N - 1 3 0  W N - I  
+ p max(0, W N - l  - xN-1 - u N - 1 ) ) .  
Naturally J N -  is a function of the stock x N -  1. It is calculated for each x N -  either analytically or numerically (in which case a table is used for computer storage of the function JN- l). In the process of calculating JN- we obtain the optimal inventory ordering policy pg- l ( x N -  1) for the last period, where p $ . - l ( x N - l )  2 0 minimizes the right-hand side of the above equation for each value of xN- 1. 
N - 2 Period Assume that at the beginning of period N - 2 the in- 
ventory is Now it is clear that the inventory manager should order 
2.2 THE DYNAMIC PROGRAMMJNG ALGORITHM 49 
inventory u N - 2  = P L ; : - ~ ( X ~ - ~ ) ,  which minimizes not only the expected cost 
of period N - 2 butxather the 
(expected cost of period N - 2) + (expected cost of period N - 1, given that an optimal policy will be used at period N - 1). 
This however is equal to 
E {cuN-2 + h max(O,xN-, + u N - 2  - W N - J  
W N - 2  
+ p max(O, w N - 2  - X N - 2  - u N - 2 ) 1  + E { J N - l ( X N - l ) } .  
W N - 2  
Using the system equation x N -  = x N -  + u N -  - w N -  the last term in the 
above sum is also written E W N _ ,  { J N - 1 ( ~ N - 2  + u N - 2  - w ~ - ~ ) } .  
Thus the optimal cost J N -  2 ( x N -  2) for the last two periods, given that we are at state x N -  2 ,  is written 
J N - 2 ( x N - 2 )  = min E { c u ~ - ~  + h max(0, x N - 2  + u N - 2  - w N - 2 )  
U N - Z a O  W N - 2  
+ p max(0, W N - 2  - x N - 2  - u N - 2 )  
+ J N - I ( % - 2  + U N - 2  - W N - 2 ) ) .  
Again J N - 2 ( ~ N - 2 )  is calculated for every 
k Period Similarly we have that at period k and for initial inventory x k  
At the same time the optimal ordering policy pL;:- 2 ( x N -  2) is also computed. 
the inventory manager should order U k  to minimize 
(expected cost of period k) + (expected cost of periods k + 1, . . . , N - 1, 
given that an optimal policy will be used for these periods). 
By denoting by J k ( X k )  the optimal value, we have 
J k ( x k )  = min E { c u p  + h max(0, x k  f U k  - w k )  + p max(0, w k  - x k  - Uk) 
U k 2 0  W k  
+ J k + l ( X k  + u k  - w k ) )  ( 5 )  
which is actually the dynamic programming equation for this problem. The functions J k ( X k )  denote the optimal expected cost for the remaining 
periods when starting at period k and with initial inventory x k .  These func- 
tions are computed recursively backward in time starting at period N - 1 
and ending at period 0. The value Jo(xo) is the optimal expected cost for the process when the initial inventory at time 0 is xo . During the calculations the 
optimal inventory policy {,u$(xo), ,u*(xl), . . . , p i -  l (xN-  1)} is simultaneously 
computed from minimization of the right-hand side of ( 5 )  for every x k  and k. 
We now state the dynamic programming algorithm for the basic problem and show its optimality. 
50 2 THE DYNAMIC PROGRAMMING ALGORITHM 
Proposition Let J*(xo) be the optimal value of the cost functional (2) in the problem of Section 2.1. Then 
J*(xo)  = Jo(xo), 
where the function J o  is given by the last step of the following dynamic programming algorithm, which proceeds backward in time from period 
N - 1 to period 0: 
J N ( X N )  = g N ( X N )  (6)  
J k ( X k )  = inf E { g k ( x k  9 uk 7 w k )  + J k  + 1 [ fk(xk,  uk 7 wk)] 1 (7)t u k e U k ( x k )  w k  
k = 0 , 1 ,  ..., N - 1 .  
Furthermore, if u t  = P t ( x k )  minimizes the right-hand side of (7)  for each x k  
and k the control law n* = { P O * , .  . . , p& 1}  is optimal. 
Proof The fact that the probability measure characterizing wk depends 
only on xk and uk and not on prior values ofdisturbances w o ,  . . . , wk- allows 
us to write the optimal value of the cost J*(xo)  in the form 
J*(xo) = inf J ( x 0 ,  P O ,  . . . , P N  - 1) 
PO.  .... P N -  I 
= inf [ E {goCxo. P O ( ~ O ) ,  w01 + E g lCx l ,  ~ ~ ( x ~ ) ,  w l l  + ... PO, .... PN-1 WO w1 i 
11l + E { g N -  l [xN- 1, P N -  1(xN- W N -  1 1  + g N ( X N ) }  . ' '  
W N - 1  
where the expectation over W k ,  k = 0, 1,. . . , N - 1, is conditional on xk 
and P k ( X k ) .  The above expression may also be written 
goCxo, P ~ ( X ~ ) ,  wOl + inf g l C x l ,  w1l + ... PO PI 
I' Both the DP algorithm and its proof are, of course, rigorous only if the basic problem is 
rigorously formulated. As explained in the previous section, this is the case when the disturbance 
spaces Dk. k = 0, 1, . . . , N - 1, are countable sets and the expected values of all terms in the 
expression of the cost functional (2) are well defined and finite for every admissible policy K. In addition, it is assumed that the expected value in (7) exists and is finite for all uk E Uk(xk)  and all xk  E S,. We further note that, although not explicitly denoted, the expectation in (7) is taken with respect to the probability measure characterizing wkr which depends on both .q and uk. We also write inf instead of min since the minimum of the expected value may not be attained. If the minimum is known to be attained by some tik E Uk(xk) then inf can be replaced by min. 
2.2 THE DYNAMIC PROGRAMMING ALGORITHM 51 
In the above equations the minimizations indicated are over all functions pk such that ,uk(Xk)  E uk(xk) for all xk and k .  In addition, the minimization is subject to the ever-present system equation constraint 
x k +  1 = f k C x k ,  P k ( x k ) ,  w k l .  
Now we use the fact that for any function F of x ,  u, we have 
inf F[x ,  ,u(x)] = inf F(x,  u), P € M  U E  U(X) 
where M is the set of-all functions p ( x )  such that p(x )  E V ( x )  for all x .  
and introducing the functions Jk of (7) in (8) we obtain the desired result: By applying this fact in (8), using the substitution xk+ = f k ( X k r  U k ,  wk), 
J*(xo)  = Jo(x0). 
It is also clear that {p;, . . . , pg- is an optimal control law if pt (xk)  
minimizes the right-hand side of (7) for each xk and k .  Q . E . D .  
In the DP algorithm of the above proposition, ideally, we would like to be able to determine closed-form expressions for the " cost-to-go " functions J k .  This is possible in a number of important special cases. In any case even if a closed-form expression for Jk or the optimal control law bt cannot be obtained, one hopes to obtain characterizations O f J k  or pt that are of interest. We shall examine such cases in the next chapter. 
In the absence of an analytical solution one has to resort to a numerical solution of the DP equations. This may be quite difficult and expensive since the minimization in (7) must be carried out for each value of xk. Typically the state space is discretized and the minimization is carried out for a finite number of states xk . The computational requirements are proportional to the number of discretization points. Thus for complex multidimensional pro- blems the computational burden may be overwhelming even for the most potent of presently existing computers. More about the computational aspects of DP will be presented in Chapter 5. However, at this point it must be re- cognized that DP cannot provide a complete solution to every problem of the type we are considering. Nonetheless, it is the only general approach for attacking sequential optimization problems under uncertainty. 
We now provide an example that demonstrates the computational aspects of the DP algorithm. 
EXAMPLE 1 Consider an inventory control problem similar to the one of Section 2.1 but different in that inventory and demand are nonnegative integer variables. Furthermore assume that there is an upper bound on the 
52 2 THE DYNAMIC PROGRAMMING ALGORITHM 
stock (xk + uk) that can be stored and also assume that the excess demand 
(wk - xk - uk) is lost. As a result the stock equation takes the form 
xk+ 1 = max(0, xk + uk - wk). 
Assume that the maximum capacity (xk + uk) for stock is 2 units, that the planning horizon N is 3 periods, and that the holding cost h and the ordering cost c are both 1 unit. The shortage cost p is assumed to be 3 units, and the demand wk has the same probability distribution for all periods, given by 
where xk, uk, wk can take the values 0, 1, and 2. 
Stage 2 We compute J2(x2) for each of the three possible states: 
~ ~ ( 0 )  = min E { u 2  + max(0, u2 - w 2 )  + 3 max(0, w2 - u2)) 
u 2 = 0 . 1 . 2  w2 
= min {u2  + O.l[max(O, u 2 )  + 3 max(0, -u2)]  u 2 = 0 . 1 , 2  
+ 0.7[max(O, u2 - 1) + 3 max(0, 1 - u2)] + 0.2[max(O, u2 - 2) 
+ 3 max(0,2 - u?)]}. 
We calculate the expectation of the right-hand side for each of the three possible values of u2 : 
U Z  = 0 :  
~2 = 1: 
~2 = 2: 
E { - }  = 0.7 x 3 x 1 + 0.2 x 3 x 2 = 3.3, E { . }  = 1 +0.1 x 1 +0.2 x 3 x 1 = 1.7, 
E { . }  = 2 + 0.1 x 2 + 0.7 x 1 = 2.9, 
Hence we have by selecting the minimizing u 2 ,  
D JZ(0) = 1.7, ,uT(O) = 1. a 
There is no fixed cost (i.e., K = 0) and the initial stock xo is zero. 
case this algorithm takes the form Let us solve this problem by applying the DP algorithm (6), (7). For our 
2.2 THE DYNAMIC PROGRAMMING ALGORITHM 53 
For x 2  = 1 we have 
J2(1) = min E {u2 + max(0, 1 + u2 - w2) + 3 max(0, w2 - 1 - u 2 ) }  
= min {u2 + O.l[max(O, 1 + u 2 )  + 3 max(0, - 1 - u2)] 
u2=0.1 wz 
u * = o .  1 
+ 0.7[max(O, u2) + 3 max(0, -u2)l  
+ 0.2[max(O, u2 - 1)  + 3 max(0, 1 - u,)]}, 
~2 = 0: 
u2 = 1: 
E { . }  = 0.1 x 1 + 0.2 x 3 x 1 = 0.7, 
E { . }  = 1 + 0.1 x 2 + 2 + 0.7 x 1 = 1.9. 
Hence 
D Jz(1) = 0.7, pr(1) = 0. 
For x2 = 2 we have 
J2(2) = E {max(O, 2 - w2) + 3 max(0, w2 
w2 
= 0.1 x 2 + 0.7 x 1 = 0.9, 
D JZ(2) = 0.9, ~ 3 2 )  = 0. 
Stage 1 Again we compute Jl(xl)  for each of the three possible states x 2  = 0, 1,2 using the values J2(0) ,  J2(1), J2(2) obtained in the previous stage: 
Jl(0) = min E {ul + max(0, u1 - wl)  + 3 max(0, w1 - u l )  
u 1 = 0 , 1 , 2  W I  
+ JzCmax(0, u1 - W l ) I l ,  
U I  = 0: E {  . }  = 0.1 x J 2 ( 0 )  + 0.7[3 x 1 + J2(0)]  
+ 0.2[3 x 2 + J2(0)] = 5.0, 
~1 = 1: E { - }  = 1 + O.l[1 + J2(l)] + 0.7 x JZ(0)  
+ 0.2[3 x 1 + Jz(0)] = 3.3, 
~1 = 2: E { . }  = 2 + 0.1[2 + J2(2)] + 0.7[1 + J2(1)] + 0.2 x J2(0) = 3.82, 
D J,(O) = 3.3, pT(0) = 1, a 
54 2 THE DYNAMIC PROGRAMMING ALGORITHM 
J l ( l )  = min E {ul + max(0, 1 + u1 - wl)  + 3 max(0, w 1  - 1 - ul) 
U , = O * l w * l  
+ J2[max(0, 1 + u1 - wl)]} 
U ,  = 0: E {  * }  = O.l[1 + J2(l)] + 0.7 x J2(0)  
+ 0.2[3 x 1 + J 2 ( 0 ) ]  = 2.3, 
E {  * } = 1 + 0.1[2 + J2(2)] + 0.7[1 + J 2 (  l)] ~1 = 1 : 
+ 0.2 x J2(0)  = 2.82, 
D Jl(l) = 2.3, pT(1) = 0, 4 
J1(2) = E{max(O,2 - wl) + 3 max(0, w1 - 2) + J,[max(O, 2 - wl)] 
D J1(2) = 1.82, p32) = 0. U 
= 0.1[2 + J2(2)] + 0.7[1 + J2(1)] + 0.2 x J2(0) = 1.82, 
Stage 0 Here we need only compute Jo(0)  since the initial state is known to be zero. We have 
Jo(0)  = min E {uo + max(0, uo - wo) + 3 max(0, wo - uo) 
u o = 0 , 1 . 2  wo 
+ J1  Cmax(0, uo - wo)l}, 
u0 = 0: E { - }  = 0.1 x Jl(0) + 0.7[3 x 1 + J1(0)] + 0.2[3 x 2 + J,(O)] = 6.6, 
~0 = 1: E { * }  = 1 + O.l[1 + J1(l)] + 0.7 x Jl(0) + 0.2[3 x 1 + Jl(0)] = 4.9, 
E { - }  = 2 + 0.1[2 + J1(2)] + 0.7[1 + J1(1)] U O  = 2: + 0.2 x Jl(0) = 5.352, 
D JO(O) = 4.9, pO*(O) = 1. 4 
If the initial state were not known a priori we would have to compute in a similar manner Jo(  1) and J0(2) as well as the minimizing u o .  These calcula- tions yield 
D JO(1) = 3.9, = 0, 4 
D J0(2) = 3.352, &(2) = 0. U 
Thus the optimal ordering policy for each period is to order one unit if the current stock is zero, and order nothing otherwise. 
It is worth noting that DP can be applied (in a form that is of comparable simplicity to the one of the previous proposition) to problems where the cost 
2.2 THE DYNAMIC PROGRAMMING ALGORITHM 55 
functional does not have the additive structure of the one of the basic problem but rather the form 
r / N -  1 
where u and are given scalars. This type of cost functional can be called a risk-sensitive cost ,functional since it corresponds to an exponential utility function expressing risk aversion or risk preference (depending on the sign of p) on the part of the decision maker. Such a cost functional is particularly interesting when the expression 
N -  1 
g N ( X N )  + 1 g k ( x k  9 uk 9 w k )  
k = O  
has a monetary interpretation. For the form of the D P  algorithm correspond- ing to this case as well as the case of a discounted cost functional see Problems 6,7, and 9 at the end of this chapter. 
We finally point out that DP is fully applicable to deterministic problems involving no uncertain parameters. Such problems can be embedded within the framework of the basic problem simply by considering disturbance spaces Dk having a single element. Thus the algorithm of this section may be used for the solution of such problems. In addition, other algorithms of the D P  type, which proceed forward in time (rather than backward), may be used for deterministic problems (see Kaufmann and Cruon [K6]). It is important to note that, in contrast to stochastic problems, using feedback in deter- ministic problems results in no advantage in terms of reduction of the value of the cost functional. In other words, minimizing the cost functional over the 
class of admissible control laws {p,,, . . . , pN- results in the same optimal 
value of the cost functional as minimizing over the class of sequences of control vectors { u o ,  . . . , uN- 1} with u k  E U k ( X k )  for all k .  This is true simply 
because if {&, . . . , pg- 1} is an optimal control law for a deterministic prob- lem¶ then the control sequence {u:, . . . , ug- where 
U ;  = /&x:), k = 0,.  . . , N - I ,  
and the states x:, . . . , x& are defined by 
X t + l  = f k ( X t ,  U t ) ,  XE = X o ,  k = 0, 1, ..., N - 1, 
also achieves the optimal value of the problem. For this reason we may minimize the cost functional over sequences of controls, a task that may be achieved by variational deterministic optimal control algorithms such as steepest descent, conjugate gradient, and Newton’s method. These algorithms, when applicable, are usually more efficient than DP. On the other hand D P  has a wider scope of applicability since it can handle dificult constraint sets 
56 2 THE DYNAMIC PROGRAMMING ALGORITHM 
such as integer or discrete sets. Furthermore, D P  leads to a globally optimal solution as opposed to variational techniques, for which this cannot be guaranteed in general. 
Our main objective in this text is the analysis of stochastic optimization problems and the ramifications of the presence of uncertainty. For this reason we will pay little attention to deterministic problems. However, we offer here an example of a deterministic problem, the so-called optimal path problem, for which DP  is a principal method of solution and which demonstrates some of the computational aspects of DP  . 
EXAMPLE 2 Let { 1,2, . . . , N + l }  be a set of points and let Cij, 
i , j =  1 , . . . , N + 1, represent the cost of moving directly from point i to 
point j in one move. We assume that 0 < Cij < co and Cii = 0 for all i, j .  We would like to find the optimal path from point i to point N + 1, i.e., the sequence of moves that minimizes total cost to get to the point N + 1 starting from each of the points 1,2, .  . . , N .  
Now it is clear that an optimal path need not take more than N moves, so that we may limit the number of moves to N .  We formulate the problem as one where we require exactly N moves but allow degenerate moves’from a point 
i into itself: We denote for i = 1, . . . , N ,  k = 0, 1, . . . , N - 1, 
JN- l ( i )  optimal cost for getting to ( N  + 1) from i in one move, 
Jk(i) optimal cost for getting to ( N  + 1) from i in ( N  - k )  moves. 
Then the cost of the optimal path from i to ( N  + 1) is Jo(i). While it is possible to formulate this problem within the framework of the basic problem and subsequently apply the DP  algorithm, we bypass this formulation and write directly the DP  equation, which for our problem takes the intuitively clear form : 
optimal cost from i to ( N  + 1) in ( N  - k )  moves 
= min {Cij + optimal cost from j to ( N  + 1) in ( N  - k - 1) moves}, 
j = l ,  ..., N 
or 
Jk(i)  = min {Cij + J k +  l ( j ) } ,  k = 0, 1,. . . , N - 2, 
j = 1 . .  . , N  
with 
JN-l(i)  = Ci(N+ I ) ,  i = 1, 2, . . . , N .  
The optimal policy when at point i after k moves is to move to point j* ,  where j*  minimizes over all j = 1, . . . , N the expiession in braces above. Note that a 
degenerate move from i to i is not excluded. If the optimal path obtained from 
2.3 TIME LAGS, CORRELATED DISTURBANCES, AND FORECASTS 57 
the algorithm contains such degenerate moves this simply means that its duration is less than N moves. 
To demonstrate the algorithm consider the problem shown in Fig. 2.2a where the costs C,,, i # j (we assume C i j  = C,,), are shown along the con- necting line segments. The DP algorithm is shown in Fig. 2.2b with the “cost- to-go” J k ( i )  shown at each point i and index k together with the optimal path. The optimal paths are 
1 - 5 ,  2 4 3 4 4 - 5 ,  3 - 4 - 5 ,  4 -5 .  
5 -  
4 -  
3 -  
1 -  - 
I -  
5 
4.5 :y/ 
(11) 
FIGURE 2.2 
No e from the figure that the costs-to-go J k ( i )  are monotonically non- decreasing with k, which is easy to prove in general for optimal path problems of the type considered here. 
2.3 Time Lags, Correlated Disturbances, and Forecasts 
This section deals with various situations where some of the assumptions inherent in the basic problem formulation are not satisfied. We shall consider the case where there are time lags in the state and the control appearing in the system equation, i.e., the next state x k +  depends explicitly not only on the present state and control X k ,  u k  but also on past states x k -  I ,  x ~ - ~ ,  . . . , X k - n  
58 2 THE DYNAMIC PROGRAMMING ALGORITHM 
and controls u k -  1 ,  i k - 2 ,  . . . , i k - m .  We will consider the case where the 
disturbances w k  are correlated, and the case where at time k a forecast on the future uncertainties w k ,  w k +  . . . becomes available, thus updating the cor- responding probability distributions. The situation where the system evolu- tion may terminate prior to the final time either due to a random event or due to an action of the decision maker is covered in the problems. Generally speaking, in all these cases it is possible to reformulate the problem into the framework of the basic problem by using the device of state augmentation. The (unavoidable) price paid, however, is an increase in complexity of the reformulated problem. 
Time Lags 
First let us consider the case of time lags. For simplicity assume that there is at most a single period time lag in the state and control, i.e., assume a system equation of the form 
Thecase where there are time lags ofmore than one period is a straightforward extension of the single-period case. 
Now if we introduce additional state variables y k  and s k  and make the identifications y k  = x k -  1 ,  sk = u k -  the system equation (9) yields for k = l , 2  ,..., N - 1 ,  
By defining %k = ( x k ,  y k ,  s k )  as the new state we have 
%k + 1 = 7 k c a k  9 uk 9 wk)? 
where the system function is defined in an obvious manner from (10). By using (1 1) as the system equation and by making a suitable reformulation of the cost functional the problem is reduced to the basic problem without time lags. Naturally the control law {p,,, . . . , pN- 1 }  that is sought will consist of functions pk of the new state R k ,  or equivalently p,, will be afinction of the present state x k  as well as past state X k - l  and control U k - l .  The DP 
2.3 TIME LAGS, CORRELATED DISTURBANCES, AND FORECASTS 59 
algorithm (in terms of the variables of the original problem) is 
We note that similar reformulations are possible when time lags appear in the cost functional, for example, in the case where the expression to be minimized is of the form 
The extreme case of time lags in the cost functional is when it has the non- additive form 
Then in order to reduce the problem to the form of the basic problem the augmented state Z k  at time k must include 
and the reformulated cost functional takes the form 
The control law sought consists of functions pk of the present and past 
states xk, . . . , xo, the past controls uk- l , .  . . , uo,  and the past disturbances 
w k -  1, . . . , wo. Naturally we must assume that past disturbances are known 
60 2 THE DYNAMIC PROGRAMMING ALGORITHM 
to the controller for otherwise we are faced with a problem with imperfect state information. The DP algorithm takes the form 
JN-l(XO,...,XN-IrUO,...,UN-2,WOr...,WN-2) 
inf E {gN(xO,  . . . 3 XN- 1, fN- 1(xN- 1 7  U N -  1, w N - l ) ,  
- 
U N -  I E U N  - I ( X N -  I )  W N -  I 
U O ,  . . . 9 U N -  1, W O ,  * * .  9 w N -  I ) ) ,  
J k ( X 0 ,  * - . )  xk, u O ,  . . . )  u k - 1 ,  w 0 7  * * * 3 wk-1) 
= inf E {Jk+l(XO,...,Xk,fk(Xk,Uk,wk), U k E U k ( X k )  wk 
U o ,  . . . , U k ,  W o ,  . . . , W k ) } ,  k = 0,.  . . , N - 2. 
Similar algorithms may be written for the case where the control constraint set depends on past states or controls, etc. 
Correlated Disturbances 
We turn now to the case where the disturbances wk are correlated. Here we shall assume that the wk are elements of a Euclidean space and that the probability distribution of wk does not depend explicitly on the current state xk and control uk but rather it depends explicitly on the prior values of the disturbances w o ,  . . . , wk- By using statistical methods it is often possible 
to represent the process wo,  w l r  . . . , w N -  by means of a linear system 
y k + i  = Akyk + t k ,  
wk = C k y k +  1 9  
k = 0, 1,. . . 9 N - 1, Y o  = 0, 
where Ak, Ck are matrices of appropriate dimension and t k  are independent random vectors with given statistics. In other words, the correlated process w o ,  . . . , w N -  is represented as the output of a linear system perturbed by a white process, i.e., a process consisting of independent random vectors as shown below: 
-% y k + l  = Akyk + r k  * Ck wk. 
By considering now yk as additional state variables we have a new system equation 
By taking as the new state the pair vector &, we can write (12) as 
= (xk, yk) and as new disturbance the 
% k +  1 = &%k, U k r  t k ) .  
2 . 3  TIME LAGS, CORRELATED DISTURBANCES, AND FORECASTS 61 
By suitable reformulation of the cost functional the problem is reduced to the form of the basic problem. Note that it is necessary that yk ,  k = 1,  . . . , N - 1, 
can be observed by the controller in order for the problem to be one of perfect state information. This is, for example, the case when the matrix ck- is the identity matrix and wk- is observable. The DP algorithm takes the form 
When Ck is the identity matrix, the optimal controller is of the form 
Forecasts 
Finally let us consider the case where at time k the decision maker has access to a forecast yk that results in a reassessment of the probability dis- tribution of wk and possibly of future disturbances. For example, Y k  may be an exact prediction of wk or perhaps an exact prediction that the probability dis- tribution of wk is a specific one out of a finite collection of distributions. Forecasts that can be of interest in practice are, for example, probabilistic predictions on the state of the weather, the interest rate for money, demand for inventory, etc., depending on the nature of the problem at hand. 
Generally, forecasts can be handled by state augmentation although the reformulation into the form of the basic problem may be quite complex. We shall treat here only a simple situation. 
Consider the case where the probability distribution of wk does not depend on xk,  uk, wk- . . . , w o .  Assume that at the beginning of each period k the 
decision maker receives an accurate prediction that the next disturbance wk 
will be selected in accordance with a particular probability distribution out of 
a finite collection of given distributions {Pkll, . . . , Pkln}, i.e., if the forecast is i, 
then wk is selected according to P k l i .  The a priori probability that the forecast 
at time k will be i, i = 1, . . . , n, is p: and is given. Thus the forecasting process 
can be represented by means of the equation 
where y k +  can take the values 1, 2, . . . , n and ( k  is a random variable taking the values 1,2,. . . , n with probabilities p:", . . . , p:+' .  The interpretation 
62 2 THE DYNAMIC PROGRAMMING ALGORITHM 
here is that when the probability distribution P k +  l i .  
system given by 
takes the value i, then w k +  will occur in accordance with 
Now by combining the system equation and (13) we obtain an augmented 
The new state is ?k = ( X k ,  y k )  and the new “disturbance” is Ek = ( w k ,  tk). The probability distribution of 6 k  is given in terms of the distributions P k ( i  and the probabilities p:, and depends explicitly on T k  (via y k )  but not on the 
prior disturbances 6,‘- . . . , G o .  Thus by suitable reformulation of the cost 
functional the problem can be cast into the framework of the basic problem. It is to be noted that the control applied at each time is a function of both the current state and the current forecast. The DP algorithm takes the form 
J N ( X N 7  Y N )  = S N ( X N ) ,  
n 
J k ( X k ,  y k )  = inf E g k ( X k , U k ,  wk)  + ~ P : + l J k + l [ f k ( x k ~  Ukr  wk), U k E u k ( X k )  W k  i =  1 
k = 0 , 1 ,  . . . ,  N - 1 ,  
where the expectation over w k  is taken with respect to the probability distribution P k l Y k ,  where y k  may take the values 1,2, .  . . , n. Extension to 
forecasts covering several periods can be handled similarly, albeit at the expense of increased complexity. Problems where forecasts can be affected by the control action also admit a similar treatment. 
It should be clear from the preceding discussion that state augmentation is a very general and potent device for reformulating problems of decision under uncertainty into the basic problem form. One should also realize that there are many ways to reformulate a problem by augmenting the state in different ways. The basic guideline to follow is to select as the augmented state at time k only those variables the knowledge of which can be of benejit to the decision maker when making the kth decision. For example, in the case of single period time lags it appears intuitively obvious that the controller can benefit from knowing at time k the values of X k ,  q - 1 ,  u k - l ,  since these variables affect the value of the next state x k +  through the system equation. It is clear though that the controller has nothing to gain from knowing at time k the values of x k - 2 ,  x k - 3 ,  . . . , u k -  2 ,  . . . , and for this reason these past 
states and controls need not be included in the augmented state although their inclusion is technically possible. The theme of considering as state variables in the reformulated problem only those variables the knowledge of 
2.4 NOTES 63 
which would be beneficial to the decision making process will be predominant in the discussion of problems with imperfect state information (Chapter 4). 
Finally, we note that while state augmentation is a convenient device, it tends to introduce both analytical and computational complexities, which in many cases are insurmountable. 
2.4 Notes 
Dynamic programming is a simple mathematical technique that has been used for many years by engineers, mathematicians, and social scientists in a variety of contexts. It was Bellman, however, who realized in the early 1950s that D P  could be developed (in conjunction with the then appearing digital computer) into a systematic tool for optimization. Bellman contributed a great deal to focusing attention on the broad scope of DP. In addition, many mathematical results related to DP (particularly for the infinite horizon case) are due to him. His early books [B3, B4] are still popular reading. Other texts related to D P  are those by Howard [H16], Kaufmann and Cruon [K6], Kushner [KlO], Nemhauser “21, and White [W3]. For a rigorous treatment of sequential decision problems in general spaces see Striebel [S18a], Hinderer [H9], Blackwell et al. [B23a], and Freedman [F3a]. Risk-sensitive criteria (Problem 7) have been considered by Howard and Matheson [H17] in the context of finite-state Markov decision processes and by Jacobson [Jl] in the context of automatic control of a linear system. However, the fact that sequential decision problems with multiplicative cost functionals can be treated by DP has been noted by Bellman [B3] (see Problems 9 and 11). 
As mentioned in Section 2.1 the formulation of the basic problem and the subsequent developments are rigorous only for the case where the disturbance spaces are countable sets. Nonetheless, the DP algorithm can often be utilized in a simple way when the countability assumption is not satisfied and there are further restrictions (such as measurability) on the class of admissible control laws. The advanced reader will understand how this can be done by solving Problem 12, which shows that if one can find within a subset of control laws (such as those satisfying certain measurability restrictions) a control law that attains the minimum in the D P  algorithm, then this control law is optimal. This fact may be used to establish rigorously many of our subsequent results concerning specific applications in Chapters 3 and 4. For example, in linear- quadratic problems (Section 3.1) one determines from the D P  equations a control law that is a linear function of the current state. When wk can take uncountably many values it is necessary that admissible control laws consist only of functions pk ,  which are Bore1 measurable. Since the linear control law belongs to this class, the result of Problem 12 guarantees that this control law is optimal. 
64 2 THE DYNAMIC PROGRAMMING ALGORITHM 
Problems 
1. Use the DP algorithm to solve the following two problems: 
(a) minimize Ci3,0 xi” + u! subject to xo = 0, x4 = 8, ui = nonnegative integer, 
x i+ l  = xi + ui,  i = 0, 1, 2, 3; 
subject to xo = 5, u i e  (0, 1, 2}, x i + l  = xi - u i ,  i = 0, 1, 2, 3, 
(b) minimize xi? + 224; 
2. Air transportation is available between n cities, in some cases directly and in others through intermediate stops and change of carrier. The air fare between cities i andj  is denoted Cij (Cij = Cji) and for notational convenience we write Cij = co if there is no direct flight between i andj. The problem is to find the cheapest possible air fare for going from any city i to any other city j perhaps through intermediate stops. Formulate a DP algorithm for solving this problem. Solve the problem for n = 6 and C12 = 30, CI3  = 60, C14 = 25, c 1 5  = c16 = 00, c 2 3  = c24 = c 2 5  = 00, c 2 6  = 50, c34 = 35, c 3 5  = 
c 3 6  = 00, (245 = 15, c46 = 00, c 5 6  = 15. 
3. Suppose we have a machine that is either running or broken down. If it runs throughout one week, it makes a gross profit of $100. If it fails during the week, gross profit is zero. If it is running at the start of the week and we per- form preventive maintenance, the probability that it will fail during the week is 0.4. If we do not perform such maintenance, the probability of failure is 0.7. However, maintenance will cost $20. When the machine is broken down at the start of the week it may either be repaired at a cost of $40 in which case it will fail during the week with a probability of 0.4 or it may be replaced at a cost of $150 by a new machine that is guaranteed to run through its first week of operation. Find the optimal repair, replacement, and maintenance policy that maximizes total profit over four weeks, assuming a new machine at the start of the first week. 4. A game of the blackjack variety is played by two players as follows: Both players throw a die. The first player, knowing his opponent’s result, may stop or may throw the die again and add the result to the result of his pre- vious throw. He then may stop or throw again and add the result of the new throw to the sum of his previous throws. He may repeat this process as many times as he wishes. If his sum exceeds seven (i.e., he busts), he loses the game. If he stops before exceeding seven, the second player takes over and throws the die successively until the sum of his throws is four or higher. If the sum of the second player is over seven, he loses the game. Otherwise the player with the larger sum wins, and in case of a tie the second player wins. The problem is 
PROBLEMS 65 
to determine a stopping strategy for the first player that maximizes his pro- bability of winning for each possible initial throw of the second player. Formulate the problem in terms of DP and find an optimal stopping strategy for the case where the second player's initial throw is three. 
Hint Take N = 6 and a state space consisting of the following 15 states: 
x 1  : busted, 
X I + ' :  already stopped at sum i ( 1  Q i Q 7) ,  
x * + ~ :  current sum is i but the player has not yet stopped ( 1  Q i Q 7). 
The optimal strategy is to throw until the sum is four or higher. 5. Min-Max Problems In the framework of the basic problem consider the case where the disturbances w o ,  w l ,  . . . , .wN- do not have a probabilistic description but rather are known to belong to corresponding given sets wk(xk, uk) c D k ,  k = 0, 1,. . . , N - 1, which may depend on the current 
value of the state xk and control uk. Consider the problem of finding a control law 7c = {po ,  . . . , p N -  with p k ( X k )  E U k ( X k )  V X k ,  k ,  which minimizes the 
cost functional 
Obtain a DP algorithm for the solution of this problem. 6. Discounted Criteria the case where the cost functional is of the form 
In the framework of the basic problem consider 
where a is a discount factor with 0 c a c 1. Show that an alternate form of the DP algorithm is given by 
vN(xN)  = g N ( X N ) ,  
& ( x k )  = inf E { g k ( X k r  u k ,  wk) + a & + l [ f k ( x k ,  u k ,  wk)l} .  Uk E Uk(xk)  
7 .  Risk-Sensitive Criteria sider the case where the cost functional is of the form 
In the framework of the basic problem con- 
66 2 THE DYNAMIC PROGRAMMING ALGORITHM 
(a) Show that the optimal value J*(xo)  of the problem is equal to Jo(xo)  where the function J o  is obtained from the last step of the D P  algorithm 
J N ( x N )  = exp[gN(-uN)l. 
J k ( X k )  = inf E { J k  + 1 [.fk(xk 3 uk 7 wk)] exp[gk(xk 3 uk 7 w k ) l  1. U k  E u k ( X k )  W k  
Show that the algorithm above yields an optimal control law if one exists. (b) Define the functions h(xk)  = In Jk(Xk). Assume also that gk is a 
function of xk and uk only (and not of wk). Show that the above D P  algorithm can be rewritten 
&“XN) = g N ( X N ) ,  
g k ( X k 9  ilk) + E {exp h+ l [ fk (xk?  uk, w k ) l }  . W k  1 
8. Consider the case in the basic problem where the system evolution terminates at time i when a certain given value Ei of the disturbance at time i occurs, or when a termination decision ui is made by the controller. If termination occurs at time i, the resulting cost is 
Terminating Process 
+ gk(Xk7 u k ?  w k ) ?  k=O 
where T is a termination cost. If the process has not terminated up to the final time N ,  the resulting cost is g N ( X N )  + c:,: g k ( X k ,  U k ,  wk). Reformulate 
the problem into the framework of the basic problem. 
9. cost functional is of the multiplicative form 
Hinr Augment the state space by introducing a “termination” state. In the framework of the basic problem consider the case where the 
E {gN(XN)’gN-l(XN-lrUN-l”N-~)’‘’gO(XO~UO, wO)} W k  
k=O. .... N -  1 
Devise an algorithm of the D P  type that is applicable to this problem under the assumption g k ( X k ,  uk, wk) 2 0 for all x k ,  uk, w k ,  and k. 10. Assume that we have a vessel whose maximum weight capacity is z and whose cargo is to consist of different quantities of N different items. Let ui denote the value of the ith type of item, wi the weight of ith type of item, and x i  the number of items of type i that are loaded in the vessel. The problem of 
determining the most valuable cargo is that of maximizing xr= x iu i  subject to the constraints cy’ x i  wi < z and x i  = 0, 1,2, . . . . Formulate this problem 
in terms of DP. 
PROBLEMS 67 
11. Consider a device consisting of N stages connected in series, where each stage consists of a particular component. The components are subject to failure and in order to increase the reliability of the device duplicate com- 
ponents are provided. For j = 1,2,. . . , N let (1 + mj)  be the number of 
components for the jth stage, let p,(mj) be the probability of successful oper- ation of the jth stage when (1  + mj)  components are used, and let c j  denote the cost of a single component at thej th  stage. Consider the problem of finding the number of components at each stage that maximize the reliability of the device expressed by 
P l h ) .  P z ( m 2 ) .  . . P&N) 
subject to the cost constraint cj”=l c j m j  < A ,  where A > 0 is given. For- 
mulate the problem in terms of DP. 12. Consider a variation of the basic problem whereby we seek 
inf J n ( X o ) ,  n e f i  
where is some given subset of the set of sequences { p o ,  p,, . . . , p N -  1) of 
functions p k :  S k  C k  with p k ( X k )  E U k ( X k )  for all x k  E S k .  Assume that 
n* = {p:, p:, * * .  3 11;- 11 
belongs to R and satisfies for all k = 0,1, . . . , N - I and x k  E S k  
j k ( x k )  = E { g k C x k ,  p : ( x k ) ,  w k l  + j k + l [ f k ( x k ,  pk*(xk) ,  w k ) l )  wk 
= inf E { g k ( X k ,  u k ,  wk)  + j k + l [ f k ( X k ?  u k ,  w k ) l > ,  U k E u k ( X k )  wk 
with JN(xN)  = g N ( X N )  and furthermore the functions J k  are real valued and the expectations above are well defined and finite. Show that 
j o ( x o )  = infJn(xo) = J,JX~). n e f i  
13. Semilinear Systems Consider a problem involving the system 
x k +  1 = A k X k  + f k ( u k )  + wk, 
where x k  E R”, fk are given functions, and Ak and w k  are random n x n matrices and n-vectors, respectively, with given probability distributions that do not depend on x k ,  u k  or prior values of and w k .  Assume that the cost functional is of the form 
68 2 THE DYNAMIC PROGRAMMING ALGORITHM 
where c k  are given vectors and g k  given functions. Show that if the Optimal value for this problem is finite and the control constraint sets u k ( x k )  are independent of x k ,  then the “cost-to-go” functions of the DP algorithm are affine (linear plus constant). Assuming that there is at least one optimal policy, show that there exists an optimal policy that consists of constant functions pt, i.e., p : ( x k )  = const for all x k  E R”. 14. A farmer annually producing x k  units of a certain crop stores (1 - u k ) x k  
units of his production, where 0 < u k  < 1, and invests the remaining U k X k  
units, thus increasing the next year’s production to a level x k +  given by 
The scalars w k  are independent random variables with identical probability distributions which do not depend either on x k  or u k .  Furthermore E { W k }  = w > 0. The problem is to find the optimal investment policy that maximizes the total expected product stored over N years 
N -  1 
W k  { k = O  
x N  + 1 ( l  - uk)Xk 
k = 0, 1 ,  .. . , N - 1 
Show that one optimal control law is given by: 
where 
15. Let x k  denote the number of educators in a certain country at time k and let y k  denote the number of research scientists at time k. New scientists (potential educators or research scientists) are produced during the kth period by educators at a rate Y k  per educator, while educators and research scientists leave the field due to death, retirement, and transfer at a rate 6, .  The scalars Y k ,  k = 0, 1,. . . , N - 1, are independent identically distributed 
random variables taking values within a closed and bounded interval of positive numbers. Similarly 8 k ,  k = 0, 1, . . . , N - 1, are independent identi- 
cally distributed and take values in an interval [S, S’] with 0 < 6 < 6’ c 1. By means of incentives a science policy maker can determine the proportion 
is such that l/(E + 1) < W < l/E. Note that this control law consists of constant functions. 
PROBLEMS 69 
U k  of new scientists produced at time k who become educators. Thus the number of research scientists and educators evolves according to the equations 
The initial numbers x o ,  yo are known and it is required to find a policy { p o * ( x O ,  YO), . . . 9 pg- 1 ( x N -  l r  Y N -  1)) with 
0 < c( < l ( f ( x k ,  y k )  < B < 1 ,  V X k ,  y k ,  k = 0, 1 ,  . . . , N - 1 ,  
which maximizes E;.,,6, { y N } ,  i.e., the expected final number of research scientists after N periods. The scalars a and f l  are given. 
(a) Show that the “cost-to-go” functions J k ( x k ,  y k )  are linear, i.e., for some scalars A , ,  pk 
J k ( X k ,  y k )  = l k X k  + p k y k .  
(b) Derive an optimal policy {p:, . . . , p& l }  under the assumption E {yk} > E { 8 k } ,  and show that this optimal policy can consist of constant functions. 
(c) Assume that the actual proportion of new scientists who become educators at time k is u k  + &k (rather than U k ) ,  where ck are identically distri- buted independent random variables that are also independent of Y k ,  8 k  
and take values in the interval [ - a ,  1 - B]. Derive the form of the “cost- 
to-go” functions and the optimal policy. 
Chapter 3 
Applications in Specific Areas 
3.1 Linear Systems with Quadratic Cost Functional -The Certainty Equivalence Principle 
In this section we consider the special case of a linear system 
X k f l  = A k X k  + B k U k  + wk, k = 0, 1,. . . , N - 1, 
where the objective is to find a control law {pz(xo) ,  . . . , p$- 1 ( x N -  1 ) }  mini- 
mizing the quadratic cost functional 
I N -  1 
E wk k = O  
( x ; Q N x N  + 1 ( X L Q k X k  + u ; R k U k )  . 
k = O ,  ..., N -  1 
In the above expressions xk E R", uk E R", and the matrices A k ,  Bk, Q k ,  Rk are given and have appropriate dimension. We assume that Qk are symmetric positive semidefinite matrices and Rk are symmetric and positive definite. The disturbances wk are independent random vectors with given probability distributions that do not depend on X k , U k .  Furthermore, the vectors wk 
have zero mean and finite second moments. The control uk is unconstrained. The problem above represents a popular formulation of a regulation prob- 
lem whereby we desire to keep the state of the system close to the origin. Such problems are common in the theory of automatic control of a motion or a 
70 
3.1 THE CERTAINTY EQUIVALENCE PRINCIPLE 71 
process. The quadratic cost functional is often a reasonable one since it induces a high penalty for large deviations of the state from the origin but a relatively small penalty for small deviations. However, even in cases where the quadraticcost functional is not entirelyjustified, it is still used since it leads to an elegant analytical solution that can often be implemented with relative ease in engineering applications. A number of variations and generalizations of this problem also have similar solutions. For example, the disturbances wk could have nonzero means and the quadratic cost functional could have the form 
I N- 1 i k = O  
E ( X N  - X N ) I Q N ( x N  - X N )  + 1 [ ( x k  - x a ) ’ Q k ( x k  - zk) + u;Rkukl . 
This cost functional expresses a desire to keep the state of the system close to a certain given trajectory (Xo, X l ,  . . . , X N )  rather than close to the origin. 
The analysis of the corresponding problem is very similar to the one of the present section and is left to the reader. Another generalization is the case where Ak, Bk are independent random matrices, rather than being known. This case will be considered subsequently in this section. 
Applying now the DP algorithm we have 
J N ( X N )  = ~ ~ Q N x N ,  (1) 
J k ( x k )  = min E { X ; Q k X k  + u;Rkuk + J k + l ( A k X k  + B k U k  + wk)}. (2)  uk 
It turns out that the “cost-to-go” functions J k  are quadratic and as a result the control law is a linear function of the state. These facts can be verified by straightforward calculation. By expansion of the quadratic form (1) in (2)  for k = N - 1, and by using the fact that E { w N -  1 }  = 0 to eliminate 
the term E { w k -  1 Q N ( A N -  1 x N -  + B N -  1 u N -  1)}, we have 
J N -  1 ( x N -  1 )  = x;-  1 Q N -  1 X N -  1 + min[uk- 1RN- 1 u N -  1 U N  - I 
+ uk-1Bk- 1 Q N  B N -  1 u N - l  + &- 1Ak- ~ Q N A N -  I X N -  1 
+ ~ $ - I A ~ - I Q N B N - ~ U N - ~ I  + E { W ~ - I Q N W N - I } .  
By differentiating with respect to # N - l  and setting the derivative equal to zero, we obtain 
( R N - I  + Bk- ~ Q N B N -  I ~ N -  1 = - g ~ -  I Q N A N -  I X N -  1. 
The matrix multiplying u N P l  on the left is positive definite (and hence in- vertible), since RN- is positive definite and f l N -  1 Q N B N -  is positive semi- definite. As a result the minimizing control vector is given by 
u $ - I  = -(RN-1 + HN- 1 Q N B N- I ) - ’ ~ N -  I Q N A N -  I X N -  1. 
72 3 APPLICATIONS IN SPECIFIC AREAS 
By substitution into the expression for JN-l ,  we have 
J N - i ( x N - 1 )  = xi-iK~-ixN-i + E { w i - i Q N ~ N - i l ,  where the matrix K N -  is obtained by straightforward calculation and is given by 
KN-1 = A L - ~ C Q N  - QNBN-I(BN-IQNBN-I + R N - I ) - ~ % - I Q N I A N - I  
+ Q N - I .  
The matrix K N -  is clearly symmetric. It is also positive semidefinite. This can be seen from the fact that from the calculation given above we have for every x E R" 
x'KN-,x = min[x'Q,-,x + U ' R N - ~ U  U 
+ ( A N -  1~ + B N -  ~ u ) ' Q N ( A N -  1x + BN- lu)]. 
Since Q N -  1, R N -  1, and Q N  are positive semidefinite, the expression within brackets is nonnegative. Since minimization over u preserves nonnegativity if follows that x'KN- 1 x  2 0 for all x E R". Hence KN- is positive semi- definite. 
Now in view of the fact that J N -  above is a positive semidefinite quad- ratic function (plus an inconsequential constant term) we may proceed in an entirely similar manner and obtain from the DP equation (2) the optimal 
control law for stage N - 2. Similarly we show that J N - 2  is a positive 
semidefinite quadratic function, and proceeding sequentially we obtain the optimal control law for every k. This control law has the form 
p ? ( x k )  = L k X k ,  (3) 
(4) 
where the gain matrices L k  are given by the equation 
L k  = - ( B k K k + l B k  + R k ) - l B ; K k + l A k ,  
and where the symmetric positive semidefinite matrices K k  are given re- cursively by the algorithm 
K N  = Q N ,  ( 5 )  
K k  = A ; [ K k + l  - K k + l B k ( B ; K k + l B k  + R k ) - l B ; K k + i l A k  + Q k .  (6) 
The optimal value of the cost functional is given by N - 1  
J O ( x O )  = x b K O x O  + 1 E { W ; K k + l W k ) -  
k = O  
The attractive aspect of the solution of this problem is the relative ease with which the control law (3) can be computed and implemented in engineer- ing applications. The current state x k  is being fed back as input through the 
3.1 THE CERTAINTY EQUIVALENCE PRINCIPLE 73 
FIGURE 3.1 
linear feedback gain matrix Lk as shown in Fig. 3.1. This fact accounts for the great popularity of the linear-quadratic formulation. As we shall see in Chapter 4 the linearity of the control law is still maintained even for problems where the state xk of the system is not completely observable (imperfect state information). 
The Riccati Equation and Its Asymptotic Behavior 
Equation (6) is called the discrete matrix Riccati equation since it is the discrete-time analog of (matrix) Riccati differential equations. It plays an important role in modern control theory. Its properties have been studied extensively and exhaustively. One interesting property of the Riccati equation is that whenever the matrices A,,  B,, Q,,  Rk are constant and equal to A, 
B, Q, R, respectively, then ask + - 00 the solution Kk converges (under mild 
assumptions) to a steady-state solution K satisfying the so-called algebraic matrix Riccati equation 
K = A‘[K - KB(B’KB + R)-’B’KIA + Q. (7) 
We shall shortly provide a proof of this important property, which will also be useful in Chapter 6. Based on this property, when one is faced with a problem involving the stationary linear system 
X k f l  = AX, + BUk + W k ,  k = 0, 1 , .  .., N - 1, (8) 
and the number of stages N is large, one can reasonably approximate the 
control law (3) by a linear stationary control law of the form {p*p*, . . . , p*}  
where 
p*(x) = Lx, (9) (10) L = -(B’KB + R)-’B’KA, 
and K is the steady-state solution of the Riccati equation (6) satisfying (7). This control law is even more attractive for implementation purposes in many engineering applications. 
74 3 APPLICATIONS IN SPECIFIC AREAS 
We now turn to proving convergence of the sequence of matrices {&} generated by the Riccati equation ( 5 )  and (6). We first introduce the notions of controllability and observability, which are of major importance in modern control theory. 
Definition A pair (A, B), where A is an n x n matrix and B an n x m matrix is said to be controllable if the n x nm matrix 
[B, AB, AZB, . . . , A"-'B] 
has full rank (i.e., has linearly independent rows). A pair (A, C), where A is an n x n matrix and C an rn x n matrix, is said to be observable if the pair (A', C') is controllable, where A' and C' denote the transposes of A and C,  respectively. 
One may easily prove that if the pair (A, B) is controllable, then for any initial state x, there exists a sequence of control vectors'u,, ul,  . . . , u,- that 
force the state x, of the system 
xk+ 1 = Ax, + Buk 
to be equal to zero at time n. This is true simply because from the system equation we obtain 
(1 1) 
x ,  = A"x, + BU,-l + ABu,-,  + . * * + A"-lBUo or equivalently 
Now if (A, B) is controllable, the matrix [B, AB, . . . , A"-'B] has full rank and 
as a result the right-hand side of (12) can be made equal to any vector in R" by appropriate selection of (uo,  u l ,  . . . , u,- l). In particular, one can choose 
(u,, ul, . . . , u,- 1) so that the right-hand side of (12) is equal to - A"xo, which 
implies x, = 0. This property explains the name "controllable pair" and in fact is often used to define controllability. The notion of observability has an analogous interpretation in the context of estimation problems (see e.g., Meditch [M6]). 
Definition We say that an n x n matrix D is stable if limk+m Dkx = 0 for every vector x E R" (or equivalently lim, a, Dk = 0). 
This definition is motivated by the fact that if D is a stable matrix, then the state x k  of the system xk+ = Dx,  tends to zero as k -, co for an arbitrary 
state xo. The notion of stability is, of course, of paramount importance in control theory. In the context of our problem it is important to be assured that 
3.1 THE CERTAINTY EQUIVALENCE PRINCIPLE 75 
the stationary control law, Eqs. (9) and (lo), results in a stable system, i.e., the matrix (A + BL)  is a stable matrix, and hence, in the absence of input dis- turbance, the state xk of the closed-loop system resulting upon substitution of the control law (9), 
xk = ( A  + BL)xk-i = ( A  + BL)kXo, k = 0, 1,. . . , 
tends to zero as k -+ ax 
We now have the following proposition, which shows that, for a stationary system and constant matrices Q k ,  R k ,  under controllability and observability conditions the solution of the Riccati equation ( 5 )  and (6) converges to a positive definite matrix K for an arbitrary positive semidefinite initial matrix. By matrix convergence we mean that every element of the matrices of the sequence converges to the corresponding element of the limit matrix. In addition, the proposition shows that the corresponding control law, Eqs. (9) and (lo), results in a stable system. 
Let A be an n x n matrix, B an n x m matrix, Q an n x n symmetric positive semidefinite matrix, and R an m x m symmetric positive definite matrix. Consider the discrete-time Riccati equation 
Proposition 
P k f l  = A’[Pk - PkB(B’PkB + R)-’B’Pk]A + Q, k = 0, 1,. . . , (13) 
where the initial matrix Po is an arbitrary positive semidefinite symmetric matrix. Assume that the pair (A, B)  is controllable. Assume also that Q may be written as C’C, where the pair (A, C) is observable.? Then: 
(a) There exists a positive definite symmetric matrix P such that for every positive semidefinite symmetric initial matrix Po we have 
lim Pk = P. k-m 
Furthermore, P is the unique solution of the algebraic matrix equation 
P = A’[P - PB(B’PB + R ) -  ‘B’PIA + Q (14) 
within the class of positive semidefinite symmetric matrices. (b) The matrix 
D = A + BL, 
L = -(B’PB + R)-’B’PA, 
(15) 
(16) 
where 
is a stable matrix. 
t Notice that if r is the rank of Q, there exists an r x n matrix C of rank r such that Q = C‘C (see Appendix A). 
76 3 APPLICATIONS IN SPECIFIC AREAS 
Proof The proof proceeds in several steps. First we show convergence of the sequence generated by (13) when the initial matrix Po is equal to zero. Next we show that the corresponding matrix D of (15) is stable. Subsequently we show convergence of the sequence generated by (13) when Po is any positive semidefinite symmetric matrix, and finally we show uniqueness of the solution of (14). 
Initial Matrix Po = 0 Consider the optimal control problem of finding a sequence u o ,  u l ,  . . . , uk- that minimizes 
k -  1 c (x:Qxi + u:Rui) 
i = O  
(17) 
subject to 
x i + l  = Axi + Bui, i = 0, 1, ..., k - 1, (18) 
where xo  is given. The optimal value of this problem, according to the theory of this section, is 
xb  pk(o)xO 9 
where Pk(0) is given by the Riccati equation (13) with Po = 0. We have 
XbPk(O)XO < XbPk+ i(0)Xo V X o  E R", k = 0, 1, . . . , since for any control sequence (uo, u l ,  . . . , uk) we have 
k -  1 k 
1 (x:Qxi + u:Rui) < l ( x : Q x i  + u:Rui) 
i = O  i = O  
and hence k -  1 
xbPk(O)xo = min 1 (x:Qxi + ulRu,) 
u i , i = O .  ..., k -  1 i=O 
k 
< min c (x:Qxi + uiRui) = xbPk+1(0)X07 
u i , i = O ,  ..., k i = O  
where both minimizations are subject to the system equation constraint x i +  = Axi  + Bui.  Furthermore, for a fixed xo  and for every k ,  xbPk(O)Xo is bounded above by the cost corresponding to a control sequence that forces xo  to the origin in n steps and applies zero control after that. Such a sequence exists by the controllability assumption. Thus the sequence {xb  Pk(O)XO} is increasing and bounded above and therefore converges to some real number for every xo E R". It follows that the sequence (Pk(0)) converges to some matrix P in the sense that each of the sequences of the elements of Pk(0) 
converge to the corresponding elements of P. To see this take xo = (1,0, . . . , 0). 
3.1 THE CERTAINTY EQUIVALENCE PRINCIPLE 77 
It follows that the sequence of first diagonal elements of Pk(0) converges to the first diagonal element of P .  Similarly by taking xo  = (0,. . . ,O ,  1,0, .  . . ,0)  
with the one in the ith coordinate, for i = 2, . . . , n, it follows that all the dia- 
gonal elements of Pk(0) converge to the corresponding diagonal elements of P.  Next take xo  = (1, 1,0,. . . , 0) to show that the second elements of the first 
row converge. Similarly proceeding we obtain 
lim Pk(0) = P ,  
where Pk(0) are generated by (13) with Po = 0. Furthermore, the limit matrix P is positive semidefinite and symmetric. Now by taking the limit in (13) it follows that Psatisfies 
k -  m 
P = A’[P - PB(B’PB + R ) -  ‘B’PIA + Q. (19) 
(20) 
by direct calculation we can verify the following equality, which will be useful subsequently in the proof: 
(21) 
(22) 
Furthermore, if we define 
L = -(B’PB + R)-’B’PA, D = A + BL 
P = D’PD + Q + L‘RL. 
xk+ 1 = ( A  + BL)xk = DXk 
Stability of D = A + B L  Consider the system 
for an arbitrary initial state x o .  Since 
xk = DkXo, 
it will be sufficient to show that xk + 0 as k + co. Now we have for all k by 
using (21) 
X b +  lPXk+ 1 - x;Pxk = X;(D’PD - P)xk = -X;(Q + L’RL)Xk. 
Hence k 
x;+lPxk+I = XbPXo - C X i ( Q  L‘RL)Xi. (23) 
i = O  
Since the left-hand side of the equation is bounded below by zero it follows that 
x;(Q + L’RL)Xk + 0. 
Using the fact that R is positive definite and Q may be written as C‘C, we obtain 
lim Cxk = 0, lim Lxk = 0: (24) k - m  k + m  
78 3 APPLICATIONS IN SPECIFIC AREAS 
From (22) we have 
CAn-  ' 
C A n - 2  
C A  
C 
x k -  (25)  
By (24) the left-hand side tends to zero and hence the right-hand side tends to zero also. By the observability assumption, however, the matrix multiplying 
xk on the right side of (25) has full rank. It follows that xk + 0 and hence the 
matrix D of (21) is stable. 
Positive DeJiniteness of P Assume the contrary, i.e., that there exists some xo # 0 such that xbPxo = 0. Then from (23) we obtain 
x;(Q + L'RL)xk = 0 V k  = 0, 1, . . . , 
where xk = Dkxo.  This in turn implies [cf. Eq. (2411 
CXk = 0, Lxk = 0 V k  = 0, 1, .. .. 
Consider now (25) for k = 0. By the above equalities the left-hand side is zero and hence 
O =  
C A n -  ' 
C A  C 
Since the matrix multiplying xo  above has full rank by the observability assumption we obtain xo  = 0, which contradicts the hypothesis xo # 0. Hence P is positive definite. 
Next we show that the sequence of matrices {pk(po)}  defined by (13) when the starting matrix is an arbitrary positive semidefinite matrix Po converges to P = Iimk+m Pk(0). Indeed, the optimal value of the optimal control problem of minimizing 
Arbitrary Initial Matrix Po  
k -  1 
x;POxk 1 (XiQXi UiRUi) (26) 
i = O  
3.1 THE CERTAINTY EQUIVALENCE PRINCIPLE 79 
subject to (18) equals xb Pk(P0)Xo. Hence we have for every x o  E R" 
xb Pk(0)xO < xb pk(P0)xO. 
Consider now the cost (26) corresponding to the controller &ck) = uk = Lxk, where L is defined by (20). This cost is given by 
k -  I 
D'kP,Dk + 1 [D"(Q + L'RL)Di] 
i = O  
and is greater than xb Pk(Po)xo, which is, of course, the optimal value of (26). Hence we have for all k and x E R" 
1 k- 1 
X'Pk(0)X < X'Pk(P0)X < X' D ' k p ~ D k  + 1 [D"(Q + L'RL)D'] X .  (27) 
i = O  
Now we have proved 
lim Pk(0) = P,  (28) k +  m 
and we also have (using the fact that limk+w DfkPoDk = 0) 
(29) 
where the last equality may be verified easily using (21). Combining (27)-(29) we obtain 
lim P,(Po) = P ,  
I k -  1 
lim DfkP0Dk + 1 [D"(Q + L'RL)D'] 
k -  m i i = O  
= lim 1 [D"(Q + L'RL)Di] = P,  
k + m  c- i = O  I 
k +  w 
for an arbitrary positive semidefinite symmetric P o .  
of (14), we would have Uniqueness of Solution If P were another positive semidefinite solution 
lim Pk(P) = P. k - t m  
Since P is a solution of (14), however, it follows that 
Pk(g) = P V k  = 0, 1,. . . , 
and hence = P.  Q.E.D. 
We note that this proposition may be sharpened by substituting the controllability and observability assumptions by weaker assumptions of 
80 3 APPLICATIONS IN SPECIFIC AREAS 
stabilizability and detectability. We refer the reader to the work of Kucera [K9], Payne and Silverman [P4], and Wonham [W12] for an exposition of this refinement. 
Random System Matrices 
We consider now the more general case where the matrices A,  and Bk are not known but rather are independent random matrices over time and independent of wk . Their probability distributions are given and they are assumed to have finite second moments. This problem falls again within the framework of the basic problem by considering as “disturbance” at each time k the triplet (Ak, Bk, wk). The DP algorithm is written 
J N ( X N )  = X ; V Q N X N  9 
J k ( X k )  = min E { X i Q L X k  + u;Rkuk + Jk+l(AkXk + BkUk + wk)}. U k  W k . A k , B k  
Calculations very similar to those for the case where A k ,  Bk are not random show that the optimal control law is of the form 
pLk*(xk) = k x x  3 (30) 
(3 1) 
K N  = Q N ,  (32) 
(33) 
Finally we further pursue an observation made in Chapter 1 ,  which is related to the nature of the quadratic criterion. Consider the minimization over u of the quadratic form 
E { (ax  + bu + w)’}, 
where a,  b are given scalars and w is a random variable. The optimum is attained for 
where the gain matrices Lk are given by 
Lk = -[Rk + E { B ; K ~ + I B ~ } ] - ~  E{%Kk+iAk} ,  
and where the matrices K k  are given by the recursive equation 
Kk = E{A’Kk+iAk}  - E{A;Kk+iBk}CRk + E { % K k + i B k } l - l  
x E { B ; K k +  l A k }  + Q k .  
W 
U* = - ( u / ~ ) x  - ( l / b ) E { w } .  
Now u* is independent of the particular probability distribution of the ran- dom vector w and depends only on the mean E { w } .  In particular, the result of the optimization is the same as for the corresponding deterministic problem where w is known with certainty and equal to E { w } .  As mentioned in Section 
3.2 INVENTORY CONTROL 81 
1.3, this property is called the certainty equivalence principle and appears in various forms in many (but not all) stochastic control problems involving linear systems and quadratic criteria. For the first problem of this section ( A k ,  Bk known), the certainty equivalence principle is expressed by the fact that the control law (3) is the same as the one that would be obtained from the corresponding deterministic problem where wk is not random but rather is known and equal to zero (its expected value). However, for the problem where A k ,  B k  are random the certainty equivalence principle does not hold since if one replaces Ak, Bk with their expected values in Eq. (33), the resulting control law need not be optimal. 
3.2 Inventory Control 
We consider now the N-period version of the inventory control problem considered in Sections 2.1 and 2.2. For simplicity we shall assume initially that thefixed cost K is zero. Furthermore, we will assume that excess demand at each period is backlogged and is filled when additional inventory becomes available. This is represented by negative inventory in the system equation 
x k + l  = xk f uk - W k ,  k = 0, 1, .. ., N - 1. 
We assume that the successive demands wk are bounded and independent, the unfilled demand at the end of the Nth period is lost, and the inventory leftover at the end of the Nth period has zero value. We shall also assume for convenience that the demands wo,  . . . , w N -  are characterized by identical 
probability measures. The results of this section can also be proved without this restriction by trivial modifications of the proofs given here. Under these circumstances the total expected cost to be minimized is given by the ex- pression 
The assumptions made in Section 1.3.3 (c > 0, h 2 0, p > c) will also be in effect here. 
By applying the DP algorithm for the basic problem we have 
J N ( x N )  = 0, (34) 
J k ( X k )  = min[cuk + L(xk + uk)  + E { J k + l ( x k  + u k  - wk)}] ,  (35) 
U k > O  
where the function L is defined by 
L(y) = p E {max(o, wk - y ) }  + h E{max(O, y - Wk)}. 
82 3 APPLICATIONS IN SPECIFIC AREAS 
We now show that an optimal control law is determined by a sequence of 
scalars {So, S1, . . . , SN- 1 }  and has the form 
For each k ,  the scalar Sk minimizes the function Gk@) = cy + L(y) + E { J k +  l b  - w ) } *  (37) 
It is evident from the form of the DP algorithm and the discussion of the single-period problem of Section 1.3.3 that the optimal control law is indeed of form (36) provided the cost-to-go functions Jk [and hence also the functions Gk of (37)] are convex, and furthermore lim,,,,, Gk(y) = co, so that the minimizing scalars S k  exist. 
Indeed, proceeding inductively we have that J N  is convex [cf. Eq. (34)]. 
By the single-period problem solution, an optimal policy at time N - 1 is 
given by 
Furthermore from the DP equation (35) we have c ( S N - 1  - x N - 1 )  + L ( S N - 1 )  if x N - 1  < S N - 1 ,  i LN- l(xN- 1) if X N - 1  3 s N - 1 ,  
J N -  l(xN- 1 )  = 
which is a convex function by the convexity of L and the fact that S N - l  minimizes cy + L(y) (see Fig. 3.2). Thus given the convexity of JN we were able to prove the convexity of J N - l .  
Similarly one can see that iimlyl+m Gk(y) = a, since c < p ,  and we have 
c(sk - xk) + L(sk) + E { J k +  l(sk - wk)} if xk < s k ,  i L(xk)  -I- E { J k +  l(xk - w k ) }  if xk > S k r  
J k ( X k )  = 
where Sk minimizes c y  + L(y) + E {Jk+l (y  - w ) } .  Again the convexity of 
J k + l  [which implies convexity of L ( x )  + E {Jk+l (x  - w ) } ]  is sufficient to 
show the convexity of Jk and thus the optimality of the control law (36) is demonstrated. 
Positive Fixed Cost 
We now turn to the somewhat more complicated case where there is a nonzero fixed cost K > 0 associated with a positive inventory order. In other words, we consider the case where the cost for ordering inventory u 3 0 is given by 
if u = 0. C(u) = 
3.2 INVENTORY CONTROL 83 
FIGURE 3.2 
The DP algorithm takes the form 
with L defined as earlier by 
Consider again the functions G, 
84 3 APPLICATIONS IN SPECIFIC AREAS 
If we could prove that the functions Gk were convex functions, then based on the analysis of Section 1.3.3 it would follow that a policy of the (s, S) type 
would be optimal, where Sk is a value of y that minimizes Gk(y) and sk is the smallest value of y for which Gk(y) = K + Gk(Sk). Unfortunately when K > 0 it is not necessarily true that Jk or Gk are convex functions. This opens the possibility of functions Gk having the form shown in Fig. 3.3. For this case the 
FIGURE 3.3 
optimal policy is to order (S - x )  in interval I, zero in intervals I1 and IV, and (3 - x) in interval 111. However, we will show that even though the functions 
Gk may not be convex they have the property 
(40) 
This property is called K-convexity and was first utilized by Scarf [SS] to show the optimality of multiperiod (s, S) policies. Now if (40) holds, then the situation shown in Fig. 3.3 is impossible; for if yo  is the local maximum in the interval 111, then we must have, for sufficiently small b > 0, 
and from (40) it follows that 
3.2 INVENTORY CONTROL 85 
which contradicts the construction shown in Fig. 3.3. More generally it is easy to show by essentially repeating the analysis of Section 1.3.3 [using part (d) of the lemma below] that if (40) holds, then an optimal policy takes the form (39). 
Definition We say that a function g :  R -, R is K-convex, where K 2 0, 
if 
Some properties of K-convex functions are provided in the following lemma. The last part of the lemma essentially proves the optimality of the (s, S) policy (39) when Gk satisfies (40). 
Lemma (a) A convex function g: R -, R is also O-convex and hence 
also K-convex for all K 2 0. 
(b) If gl(y) and g2(y) are K-convex and L-convex (K 2 0, L 2 0), re- spectively, then ag,(y) + pg2(y) is (crK + pL)-convex for all positive a and p. 
(c) If g(y) is K-convex, then E ,  {g(y - w ) }  is also K-convex provided 
E ,  { Jg(y - w ) l }  < 00 for all y. 
(d) If g: R -, R is a continuous K-convex function and g(y) + co as 
Iyl+ co, then there exist scalars s and S with s < S such that 
(0 g(S) < g(y), 'dY E R ;  (ii) g(S) + K = g(s) < go4 VY < s; 
(iii) g(y) is a decreasing function on (- co, s); (iv) g(y) < g(z) + K for all y, z with s < y < z. 
Proof Part (a) follows from elementary properties of convex functions and parts (b) and (c) follow directly from the definition of a K-convex function. We shall thus concentrate on proving part (d). 
Since g is continuous and g(y) + 00 as I y I + co, there exists a minimizing 
point of g. Let S be such a point. Also let s be the smallest scalar z for which z 6 S and g(S) + K = g(z). For all y with y < s we have from the definition of K-convexity 
Since K + g(S) - g(s) = 0 we obtain g(s) - g(y) < 0. Since y < s and s 
is the smallest scalar for which g(S)  + K = g(s) we must have g(s) < g(y) and (ii) is proved. Now for y ,  < y2 < s we have 
86 3 APPLICATIONS IN SPECIFIC AREAS 
and by adding these two inequalities we obtain 
Cs(Y2)  - g(y,)l ,  S - Y z  O>- 
Y 2  - Y l  
from which g(yl)  > g(yz)  thus proving (iii). To prove (iv) we note that it holds for y = z as well as for either y = S or y = s. There remain two other pos- sibilities, S < y < z and s -= y < S. If S < y < z, then by K-convexity 
and (iv) is proved. If s < y < S, then by K-convexity 
from which 
and g(s) 2 g(y). Noting that 
g(z) + K 2 g(S) + K = g($, 
it follows that g(z)  + K 2 g(y). Thus (iv) is proved for this case as well. Q.E.D. 
Consider now the function G N -  of (38): 
G N -  1 0 1 )  = CY + LoI). 
Clearly G N - 1  is a convex function and hence by part (a) of the previous lemma it is also K-convex. We have, from the analysis of the case where K = 0, 
(41) K + G N - 1 ( S N - 1 )  - c x  for x < s N - 1 ,  
G N -  1 ( x )  - cx for x 2 S N - 1 ,  
J N -  l ( x )  = 
where SN- minimizes G N -  l(y) and sN-  is the smallest value of y for which G N -  l ( y )  = K + G N -  l ( S N -  l ) .  Notice that since K > 0 we have sN-  # S N -  
3.2 INVENTORY CONTROL 87 
and furthermore the slope of G N -  at s N -  is negative. As a result the left slope of J N -  at sN- is greater than the right slope as shown in Fig. 3.4 and J N -  is not convex. However, we will show that J N -  is K-convex based on the fact that GN- is K-convex. To this end we must verify that 
We distinguish three cases: 
Case 1 y 2 s ~ - ~  If y - b 2 s ~ - ~ ,  then in this region of values of 
z, 6, y the function JN- by (41), is the sum of a K-convex function and a linear function. Hence by part (b) of the lemma it is K-convex and (42) holds. 
If y - b < s N -  1, then in view of (41) we can write (42) as 
b 
88 3 APPLICATIONS IN SPECIFIC AREAS 
NOW if y is such that GN- l(y) 2 GN- l ( ~ N -  1), then by K-convexity of G N -  we have 
Thus (43) and hence also (42) holds. If y is such that GN- l(y) < GN- 1(sN-  1), 
then we have 
So for this case (43), and hence also (42), holds. 
Case 2 y < y + z < sN- is linear and hence (42) holds. 
In this region, by (41), the function J N -  
Case 3 y < sN-  < y + z For this case in view of (41) we can write (42) as 
or equivalently 
K + GN- 10, + Z) 2 G N -  ~ ( s N -  I), 
which holds true by the definition of s N -  1. 
We have thus proved that K-convexity and continuity of GN- together 
with the fact that GN-I(y) + co as lyl + 00 imply K-convexity of J N - 1 .  In 
addition, J N -  can be easily seen to be continuous. Now using the lemma it follows from (38) that GN-2 is a K-convex function. Furthermore, by using the boundedness of w N -  2 ,  it follows that GN-2 is continuous and, in addition 
CN-,(Y) + co as ly l  + 00. Repeating the argument above we obtain the fact 
that J N - 2  is K-convex and proceeding similarly we prove K-convexity and 
continuity of the functions Gk for all k, as well as that G,(y) + 00 as I y I + co. 
At the same time [by using part (d) of the lemma] we prove optimality of the multiperiod (s, S) policy of (39). 
3.3 DYNAMIC PORTFOLIO ANALYSIS 89 
Optimality of policies of the (s, S) type can be proved for a number of problems that constitute variations and generalizations of the problem considered in this section. Problems 4-6 treat the cases where forecasts on the uncertain demand become available during the control process, the case where there is a one-period time lag in delivery of inventory, and the case where unfilled demand is lost rather than backlogged (i.e., the system equation 
is xk+ 1 = max[O, xk + uk - wk]). 
3.3 Dynamic Portfolio Analysis 
Portfolio theory deals with the question of how to invest a certain amount of wealth among a collection of risky or riskless assets. The traditional and widely used approach to this problem [M4, S S ] ,  has been the so-called mean- variance approach examined in Section 1.3, whereby the investor is assumed to be maximizing the expected value of a utility function that depends on the mean and the variance of the rate of return of the investment. Since this approach cannot be readily generalized to the case where investment takes place over several periods of time and in addition is based on assumptions that may not be satisfied in a given practical situation, there has been con- siderable effort toward the development of alternative approaches for port- folio selection. In one such approach, the investor is assumed to be maximiz- ing the expected utility of his final wealth. We shall discuss in this section some results related to this viewpoint. We will start with an analysis of a single- period model and then extend the results to the multiperiod case. 
Let xo denote the initial wealth (measured in monetary units) of the in- vestor and assume that there are n risky assets, with corresponding random rates of return el ,  ez, . . . , en among which the investor can allocate his wealth. 
The investor can also invest in a riskless asset offering a sure rate of return s. 
If we denote by ul, . . . , u, the corresponding amounts invested in the n risky 
assets and by (xo - u1 - . . . - u,) the amount invested in the riskless asset, 
the final wealth of the decision maker is given by 
n 
x1 = s(xo - u1 - ... - u,) + C e i u i ,  
i =  1 
or equivalently 
x1 = sxo + C ( e i  - s)ui. 
i =  1 
The objective is to maximize over ul,. . . , u,, 
E {w4, 
ei 
i =  1, ..., n 
90 3 APPLICATIONS IN SPECIFIC AREAS 
where U is a utility function for the investor. We assume that the expected value above is well defined and finite for all x , ,  ui .  We shall also assume that the domain of U is an open set D within which U is concave and twice con- 
tinuously differentiable. We shall not impose constraints on u,, . . . , u,. This 
is necessary in order to obtain the results in convenient form. However, we shall assume that the probability distribution of ei and the minimizing values of ui are such that the resulting values of x 1  as given by (44) belong to the domain of U .  A few additional assumptions will be madeduring the exposition of the results. 
Let us consider the above problem for every value of initial wealth and denote by uz = pi*(x0), i = 1, .  . . , n, the optimal amounts to be invested in 
the n risky assets, when the initial wealth is x , .  
We say that the portfolio {p'*(xo) ,  . . . , p"*(x0)} is partially separated if 
(45) 
where ai, i = 1, . . . , n, are fixed constants and h(x,) is a function of x ,  (which is the same for all i ) .  
When partial separation holds, the ratios of amounts invested in the risky assets are fixed and independent of the initial wealth, i.e., 
pi*(xo)  = a'h(x,), i = 1,. . . , n, 
pi*(xo)/pj*(xo)  = a i / d  for 1 < i , j  < n, 04 z 0. 
Actually in the cases we shall examine when partial separation holds, the portfolio {p1*(x0) ,  . . . , p"*(xo)} will be shown to consist of a f h e  (linear plus constant) functions of x o  that have the form 
(46) 
where a and b are constants characterizing the utility function U .  In the special case where a = 0 in (46) we say that the optimal portfolio is 
completely separated in the sense that the ratios of the amounts invested in both the risky asset and the riskless asset are fixed and independent of initial wealth. We now show that when the utility function satisfies 
pi*(xo)  = ai[a + bsx,] ,  i = 1,. . . , n, 
- U'(x , ) /U"(x , )  = a + b x ,  v x , ,  (47) 
where U' and U" denote the first and second derivatives of U ,  respectively, and a and b are some scalars, then the optimal portfolio is given by 
(48) pi*(xo)  = d [ a  + bsx,] ,  i = 1,. . . , n. 
Furthermore, if J(xo)  is the optimal value of the problem 
Jb0) = min E { U ( x , ) } ,  
ui 
3.3 DYNAMIC PORTFOLIO ANALYSIS 91 
then we have 
- J’(xo)/J”(xo) = (a/s) + bx,  v x ,  . (49) 
Let us assume that an optimal portfolio exists and is of the form pi’(x0) = ai(x0)[a + bsxo], 
where ai(xo), i = 1 ,  . . . , n, are some differentiable functions. We will prove 
that dai(xo)/dxo = 0 for all xo  and hence the functions ai must be constant. 
We have for every xo, by the optimality of pi*(xo) ,  for i = I ,  . . . , n, 
1 1  d ~ { ~ ( x ~ ) } / d u ~  = E U‘ sxo + C(ej  - s)aj(xo)(a + bsx,) (ei - s) = 0, i [ .i:1 
Differentiating the n equations in (50) with respect to xo yields - da’(xo) 
(el - s)’ . . (el - s)(e, - s) 
(en - s)(el - s) . . . (en - s)’ 
U”(x , ) (a  + bsxo) 
- -  
i =  1 
Using relation (47) we have U’(X 1) 
a + b[sxo + I!=, (ei - s)a’(x,)(a + bsx,)] 
(a + bsx,) [ 1 + I:= (ei - s)ai(xo)b] 
‘ 
U”(x1) = - 
- U’(X 1 )  _ -  
Substituting in (51) and using (50) we have that the right-hand side of (51) is the zero vector. The matrix on the left in (51), except for degenerate cases, can be shown to be nonsingular. Assuming that it is indeed nonsingular we obtain 
dai(xo)/dxo = 0, i = 1 , .  . . , n, 
and ai(xo) = ai, where ai are some constants, thus proving (48). 
We now turn our attention to proving relation (49). We have 
92 3 APPLICATIONS IN SPECIFIC AREAS 
and hence 
(53) 
The last relation after some calculation and using (52) yields 
11 I (ei - s)aib s (a + bsx,). (54) 
By combining (53) and (54) we obtain the desired result : 
-J'(xo)/J"(xo) = ( a / ~ )  + bxo. 
The class of utility functions satisfying condition (47) is characterized by the fact that the inverse of the index of absolute risk aversion (sometimes referred to as the "risk-tolerance function") is affine in wealth. It can be easily shown that the following forms of utility functions satisfy this condition: 
exponential: for b = 0, logarithmic: ln(x + a) for b = 1, (55) 
power: [l/(b - l)](a + bx)'-(l ib) otherwise. 
Naturally in our portfolio problem only concave utility functions from this class are admissible. Furthermore if a utility function that is not defined over the whole real line is used, the problem should be formulated in a way that ensures that all possible values of the resulting final wealth are within the domain of definition of the utility function. 
It is now easy to extend the one-period result of the preceding analysis to the case of a multiperiod model. We shall assume that the current wealth can be reinvested at the beginning of each of N consecutive time periods. We denote 
xk the wealth of the investor at the beginning of the kth period, u: the amount invested at the beginning of the kth period in the ith 
ef the rate of return of the ith risky asset during the kth period, sk the rate of return of the riskless asset during the kth period. We have (in accordance with the single-period model) the system equation 
risky asset, 
n 
xk+ 1 = S k X k  + c (ef - sk)uf, k = 0, 1, . . . , N - 1. (56) 
i =  1 
3.3 DYNAMIC PORTFOLIO ANALYSIS 93 
We assume that the vectors ek = (e t , .  . . , el), k = 0,. . . , N - 1, are inde- 
pendent random vectors with given probability distributions that result in finite expected values throughout the following analysis. 
The objective is to maximize E { U(xN)} ,  the expected utility ofthe terminal wealth x N ,  where we assume that U satisfies for all x 
- V’(X) /U”(X)  = u + bx. 
Applying the DP algorithm to this problem we have 
J&N) = U(xN), (57) 
From the solution of the one-period problem we have that the optimal policy 
at the beginning of period N - 1 is of the form 
pg- 1(xN- 1) = a N -  lCa + b s N -  1 X N -  1 1 ,  
where t l N -  is an appropriate n-dimensional vector. Furthermore, we have 
-Jk- l ( X ) / r ; -  1 ( X )  = (a/SN- 1) + bx. (59) 
Hence applying the result of this section in (58 )  for the next to the last period we obtain the optimal policy 
pg-2(XN-2) = a N - 2 [ ( a / s N - l )  + bsN-2XN-219 
where a N -  is again an appropriate n-dimensional vector. Proceeding similarly we have for the kth period 
d ( x k )  = ak[(a/sN- 1 ‘ ’ ‘ sk+ 1) + bskxkl (60) 
where ak, k = 0, 1,. . . , N - 1, are n-dimensional vectors that depend on the 
probability distributions of the rates of return e: of the risky assets and are determined by optimization of the expected value of the optimal “cost-to-go” functions Jk. These functions satisfy 
-J;(X)/J;(X) = ( U / S N - l  * * * S k )  + bx, k = 0, 1,. . . , N - 1. (61) 
Thus one can see that the investor, when faced with the opportunity to reinvest sequentially his wealth, uses a policy similar to that of the single- period case. Carrying the analysis one step further, one can see that if the utility function U is such that a = 0, i.e., U has one of the forms 
In x for b = 1 ,  
[l/(b - l)](bx)’-(’’*) for b # 0, b # 1 ,  
94 3 APPLICATIONS IN SPECIFIC AREAS 
then it follows from (60) that the investor acts at each stage k as if he were faced with a single-period investment characterized by the rates of return sk, e:, i = 1, . . . , n, and the objective function E { u(xk+ l ) } .  This policy whereby the investor can ignore the fact that he will have the opportunity to reinvest his wealth is called a myopic policy [M8]. 
Note that a myopic policy is also optimal when sk = 1, k = 0, . . . , N - 1, 
which is the case when wealth is discounted at the rate of return of the riskless asset (going rate of interest for money). Furthermore, it can be proved that when a = 0 a myopic policy is optimal even in the more general case where the rates of return sk ,  k = 0, 1, . . . , N - 1. are independent random variables 
[M8], and for the case where forecasts on the probability distributions of the rates of return e: of the risky assets become available during the invest- ment process (see Problem 7). 
It turns out that even for the more general case where a # 0 only a small amount of foresight is required on the part of the decision maker. It can be easily seen [compare (58)-(61)] that the optimal policy (60) at period k is the same as the one that would be used if the investor were faced with a single- 
period problem whereby he would maximize over u:, i = 1, . . . , n, 
subject to x k +  = skxk + C:= ( e f  - sk)uf. In other words, the investor 
maximizes the expected utility of wealth that results if amounts uf are invested in the risky assets in period k and the resulting wealth x k +  is subsequently invested exclusively in the riskless asset during the remaining periods 
k + 1, . . . , N - 1. This type of policy has been called a partially myopic 
policy [M8]. A partially myopic policy can also be shown to be optimal when forecasts on the probability distributions of the rates of return of the risky assets become available during the investment process (see Problem 7). 
Another interesting aspect of the case where a # 0 is that when sk > 1 for all k ,  then as the horizon becomes longer and longer ( N  + 00) the policy 
in the initial stages approaches a myopic policy [compare (60) and (61)]. Thus we can conclude that for sk > 1 a partially myopic policy is asymptoti- cally myopic as the horizon tends to infinity. This fact holds for an even larger class of utility functions than the class we have considered, as shown by Leland [L3]. 
In conclusion we mention that while the model we have examined ignores certain important aspects of the corresponding practical situation (con- straints on investments, transaction costs, time correlation of rates of return, the possibility of intermediate consumption of wealth, market imperfections, etc.), it admits a closed-form solution for a large class of utility functions together with economic interpretations related to myopic and partially myopic policies that are undoubtedly of considerable interest. Thus while 
3.4 OPTIMAL STOPPING PROBLEMS-EXAMPLES 95 
neither the particular model that we have examined nor its various refinements have achieved the preeminence and popularity of the mean-variance model, the corresponding analysis and results provide unquestionably important insights into the process of portfolio selection. 
3.4 Optimal Stopping Problems-Examples 
Optimal stopping problems of the type we will consider in this and sub- sequent sections typically involve a control space that consists of a finite number of elements (actions), one of which induces a termination (stopping) of the evolution of the system. Thus at each stage the controller observes the current state of the system and decides whether to continue the process (perhaps at a certain cost) or stop the process and incur a certain loss. 
Asset Selling Problem 
As a first example, consider a person having an asset (say a piece of land) for which he is offered a nonnegative amount of money from period to period. Let us assume that these random offers w,,, w l r  . . . , w N -  are independent, 
identically distributed, and take values within some bounded interval. We consider a horizon of N stages and assume that if the person accepts the offer, he can invest the money at a fixed rate of interest r > 0, and if he rejects the offer, he-waits until the next period to consider the next offer. Offers rejected are not renewed and we initially assume that the last offer w N - l  must be accepted if every prior offer has been rejected. The objective is to find a policy for accepting and rejecting offers that maximizes the revenue of the person at the Nth period. 
Let us try to embed this problem in the framework of the basic problem by defining the state space, control space, disturbance space, system equation, and cost functional. We consider as disturbance at time k the random offer w k  and as corresponding disturbance space the real line. The control space consists of two elements u l ,  u2, which correspond to the decisions “sell” and “do not sell,” respectively. Concerning the state space we define it to be the real line, augmented with an additional state (call it T),  which is a “termination state.” The system moves into the termination state as soon as the asset is sold. By writing that the system is at a state x k  # T at time k we mean that the asset has not been sold as yet and the current offer under consideration is equal to x k .  By writing that the system is at state x k  = T at time k we mean that the asset has already been sold. With these conventions we may write a system equation of the form 
X k + 1  = f k ( X k , U k , W k ) r  k = O , . . . , N -  1, 
Xg = 0, 
96 3 APPLICATIONS IN SPECIFIC AREAS 
where x k  E R u { T }  and the functionfk is defined via the relations 
T if u k  = u'(sel1) or x k  = T, I w k  otherwise. x k + l  = 
The corresponding reward function may be written N -  1 
g N ( X N )  + 1 g k ( X k ?  u k ,  w k )  
W k  k = O  
k = O .  ..., N- 1 
where 
XN if XN # T, otherwise, g N ( X N )  = 0 I 
Based on this formulation we can write the corresponding DP  algorithm over the states x k :  
In Eq. (63) (1 + r )N-kxk (where x k  # T )  is the revenue resulting from decision u1 (sell) when the offer under consideration is xk, and E { J k +  1 ( w k ) }  represents the expected revenue corresponding to the decision u2 (do not sell). 
Actually the DP algorithm above could be derived by elementary reason- ing without resorting to the elaborate formulation given earlier-something that we shall often do in the future. Our purpose for providing this formula- tion was simply to demonstrate to the reader the type of structure that one must adopt in order to embed a stopping problem into the framework of the basic problem. 
Now from the D P  algorithm (62) and (63) we obtain the following optimal policy for the case where x k  # T :  
accept the offer w k -  = x k  if (1 + r ) N - k X k  > E { J k +  1 ( w k ) } ,  
reject the offer w k -  = x k  if (1 + r ) N - k X k  < E { J k +  1 ( w k ) } .  
When (I + r ) N - k X k  = ~ { ~ k + ~ ( w k ) }  both acceptance and rejection are optimal. 
3.4 OPTIMAL STOPPING PROBLEMS-EXAMPLES 97 
a1 
a2 
a v -  I 
0 
The result can be put into a more convenient form by some further analysis. Let us introduce the functions 
A 
- a1 
Reject 
I I - - 1 3 A'-l N 
which represent discounted cost-to-go for the last N - k stages. It can be 
easily seen that 
vN(xN)  = X N  9 (64) 
h ( X k )  = m a x [ X k ,  (1 r ) - ' E { h + I ( W k ) } ] ,  k = 0, 1,. . . , N - 1. (65) 
By using the notation 
the optimal policy is given by accept the offer w k -  = x k  if x k  > a k ,  
reject the offer w k -  = x k  if x k  < q,, 
while both acceptance and rejection are optimal for x k  = tLk (Fig. 3.5). Thus the optimal policy is completely determined by the sequence ul,  . . . , uN- '. 
Now from the algorithm (64) and (65) we have 
Hence we obtain 
98 3 APPLICATIONS IN SPECIFIC AREAS 
where the function P is defined for all scalars A by 
P(1) = Prob{w c A}. Notice that the function P is nondecreasing and continuous from the left for all A. The difference equation for cik above may also be written 
with uN = 0. Let us first show that the solution of the above difference equa- tion is monotonically nonincreasing (as one would expect), i.e., 
o < U k + l  < U k ,  k = N - 2 , N - 3  ,..., (67) 
Indeed, we have 
Assuming that a k +  2 t l k + z ,  we will show.that 2 c(k+ and (67) will follow by induction. We have 
and a k  2 u k +  proving (67). 
3.4 OPTIMAL STOPPING PROBLEMS-EXAMPLES 
Now since we have 
< 1  P(a)  1 
O G - G -  l + r  l + r  
tla 2 0, 
it can be easily seen, using the monotonicity property (67), that the sequence {ak} generated (backwards) by the difference equation (66) converges 
(as k + - 00) to a constant E satisfying 
E(1 + r) = P(6)E + JEmw dP(w). 
This equation is obtained from (66) by taking limits as k -+ - 00 and by using 
the continuity from the left of the function P .  
Thus when the horizon tends to become longer and longer (i.e., N + 00) 
the optimal policy for every fixed k 2 1 approximates the stationary policy: 
accept the offer wk- = xk if xk > E ,  reject the offer wk- = xk  if xk c 5. 
The optimality of such a policy for the corresponding infinite horizon problem will be shown in Chapter 6. 
Purchasing with a Deadline 
Let us consider another problem of similar nature. Assume that a certain quantity of raw material is required by a certain time. If the price of this material fluctuates, then there arises the problem of deciding, given the price at any time, whether to purchase at that price or wait a further period, during which the price may go up or down. 
Let us assume that successive prices are independent (the case of cor- related prices will be examined later) and that the cumulative distribution P(w) of the purchase cost w of the raw material is the same for each time period. The problem is to decide, given the current purchase price, whether to pur- chase or not to purchase the amount of raw material needed. The purchase must be made within N time periods. 
This problem has obvious similarities with the previous problem. Let us denote by 
100 3 APPLICATIONS IN SPECIFIC AREAS 
the price prevailing in the beginning of period k + 1. We have similarly as before the DP algorithm 
J N ( X N )  = X N ,  
. I k ( X k )  = min[xk, E { J k +  l ( w k ) } ] ,  
and the optimal policy is given by purchase if X k  < E { J k + l ( W k ) }  = Mk, 
X k  > E { J k +  1 ( W k ) }  = t l k .  do not purchase if We have similarly that the critical numbers a l ,  az,  . . . , u N -  can be 
obtained from the discrete-time equation 
uk = a k + l [ l  - p ( a k + l ) l  + Joak"w dP(w), 
~ 1 ~ -  = J wP(w) = E { w } .  0 
Consider now a variation of this problem whereby we do not assume that the successive prices wo, . . . , w N -  are independent but rather that they are 
correlated and can be represented as 
w k  = y k + l  k = 0, 1, ..., N - 1, 
with y k + l  = l y k  + < k ,  Y O  = 0, 
where A is a scalar with 0 6 A < 1 and to, tl, . . . , C N -  are independent 
identically distributed random variables taking positive values with given probability distribution. As discussed in Section 2.3 the DP algorithm under these circumstances takes the form 
J N ( X N )  = xN 9 
J k ( X k )  = min[lxk, E { J k + l ( A X k  + < k ) } ] %  
where the cost associated with the purchasing decision is x k  and the cost associated with the waiting decision is E { J k +  1 ( h &  + ( k ) } .  
We shall show that in this case the optimal policy is also of the same type as the one for independent prices. Indeed, we have 
- 
JN- 1 ( x N -  1) = min[xN- 1, i x N -  + 51, where 4 = E { t N -  l}. As shown in Fig. 3.6 an optimal policy at time N - 1 
is given by 
purchase if x N -  < a N -  1, do not purchase if x N -  > a N -  1, 
3.4 OPTIMAL STOPPING PROBLEMS-EXAMPLES 101 
FIGURE 3.6 
- where t l N -  is defined from the equation u N -  = ActN- + 5, i.e., 
4. 1 
1 - 1” 
C ( N -  1 = 
and that J N - 1  is concave and increasing in x .  Using this fact in the DP algorithm one may easily show that 
and that J k  is concave and increasing in x for all k .  Furthermore, in view of the fact that 4 = E {tk} > 0 for all k,  one can show that 
These facts imply (as shown in Fig. 3.7) that the optimal policy for every period k is of the form 
purchase if xk c uk, do not purchase if x k  > tLk ,  
where the scalar u k  is obtained as the unique positive solution of the equation 
x = E { J k  + 1(lx + t k ) ) .  
102 3 APPLICATIONS IN SPECIFIC AREAS 
f- Purchase Do not purchase - Y 
"x FIGURE 3.7 
Note that Jk(x)  6 J k +  l ( x )  implies ak-1 d ak d ak+l Vk, 
and hence (as one would expect) the threshold price below which one should purchase is lower in the early stages of the process and increases as the deadline comes nearer. 
A number of variations on the theme of this section are of interest (see Problems). The main point to be recalled is that when only a finite number of 
actions (ul, . . . , u") are possible at each stage, the optimal control law pt(xk)  
is determined by a partition of the underlying state space Sk (minus the 
termination state) into n subsets S:, . . . , Si, with uy=! Si = Sk, each subset 
Si being associated with the corresponding action u'. In other words, the control law for all k has the form 
pt (xk)  = ui if xk E S:,  i = 1, . . f 9 n. 
In the examples we considered the state space was the positive half-line, and there were two actions available (accept-reject, or purchase-do not purchase). The partition of the state space Sk was determined in each case by the single number ak. 
3.5 Notes 
The certainty equivalence principle for dynamic linear-quadratic prob- lems was first discussed by Simon [SlO]. His work was preceded by that of Theil [T2], who considered a single-period case, and Holt et al. [Hl 11, who 
PROBLEMS 103 
considered a deterministic case. Similar problems were considered somewhat later (and apparently independently) by Kalman and Koepcke [K2], Gunckel and Franklin [G2], and Joseph and Tou [JS]. Since their work, the literature on linear-quadratic problems has grown tremendously. The special issue on the linear-quadratic problem of the I E E E  Transactions on Automatic Control [Ill contains most of the pertinent theory and variations thereof, together with hundreds of references. For a multidimensional version of Problem 3 see the paper by Jacobson [Jl]. The result of Problem 14 is also due to Jacobson [J2]. 
The literature on inventory control stimulated by the pioneering paper of Arrow et al. [A61 is also voluminous. The 1966 survey paper by Veinott [V3] contains 118 references. An important work summarizing most of the research up to 1958 is the book by Arrow et al, [A7]. The ingenious line of argument for proving the optimality of (s, S )  policies in the case of nonzero fixed costs is due to Scarf [SS]. However, his original proof contains some minor flaws. 
Most of the material in Section 3.3 is taken from the paper by Mossin [M8]. Some other interesting papers in the same area are by Hakansson [Hl-H4], Kamin [K4], Levhari and Srinivasan [L4], and Phelps [P5]. 
Problems 
1. Show the optimality of the control law given by (30)-(33) for the linear- quadratic problem where the matrices Ak, Bk are random. 2. Linear-Quadratic Problems with Forecasts Consider the linear-quad- ratic problem first examined in Section 3.1 (Ak, Bk: known) for the case where at the beginning of period k there is available a forecast yk E { 1,2, . . . , n} consisting of an accurate predictian that wk will be selected in accordance with a particular probability distribution P k l y r .  (cf. Section 2.3). The vectors wk need not have zero mean under the distributions P k l y k .  Show that the optimal control law is of the form 
pk(Xk,yk) = - (B!kKk+lBk + R k ) - l B ! k K k + l [ A k X k  + E{WkIyk}l + akr 
where the matrices Ki, i = 1, . . . , N ,  are given by the Riccati equation (5) and (6) and ak are appropriate vectors in R". 3. Consider (for simplicity) a scalar linear system 
X k + l  = akxk + b k U k  + wk, k = 0, 1,. . . , N - 1, 
where ak,  bk E R are given and wk is for each k a Gaussian disturbance with 
zero mean and variance 02. Show that the control law {p:, pLf, . . . , &- 
104 3 APPLICATIONS IN SPECIFIC AREAS 
that minimizes the risk-sensitive cost functional 
N- 1 
{ [ k = O  
E exp x i  + C (xz + mz) 
is linear in the state variable. We assume no control constraints and in- dependent disturbances. We also assume that the optimal value is finite for every xo.  Show by example that the Gaussian assumption is essential for the result to hold. 4. Consider an inventory control problem similar to the multistage inven- tory problem of Section 3.2. The only difference is that at the beginning of each period k the decision maker, in addition to knowing the current in- ventory level xk, receives an accurate forecast that the demand wk will be selected in accordance with one out of two possible probability distributions P1, P,(large demand, small demand). The a priori probability of a large demand forecast is known (cf. Section 2.3). 
(a) Obtain the optimal inventory ordering policy for the case of a 
(b) Extend the result to the N-period case. (c) Extend the result to the case of any finite number of possible dis- 
tributions. 
single-period problem. 
Consider also the inventory control problem where the purchase costs c k ,  k = 0, 1, . . . , N - 1, are not known at the beginning of the process but 
instead they are independent random variables with a priori known pro- bability distributions. The exact value of the cost c k ,  however, becomes known to the decision maker at the beginning of the kth period, so that the inventory purchasing decision at time k is made with exact knowledge of the cost c k .  
Chxacterize the optimal ordering policy for this case. 5. Consider the multiperiod inventory model of Section 3.2 for the case where there is a one-period time lag between order and delivery of inventory, i.e., the system equation is of the form 
Show that the optimal policy for this problem is an (s, S )  policy. 6. Consider the inventory problem under the assumption that unfilled demand at each stage is not backlogged but rather is lost, i.e., the system 
equation is xk+ = max[O, xk + uk - wk] instead of xk+ = xk + uk - wk. 
Show that a multiperiod (s, S )  policy is optimal. 
PROBLEMS 105 
Abbreviated Proqf ( S .  Shreve) Let J N ( x )  = 0 and for all k 
Gk(y) = cy + E {h  max[O, y - wk] + p max[O, wk - y] 
+ J k +  l(max[o, y - wkl)}, 
J k ( X )  = -CX + min[Kd(u) + Gk(X + U)], 
ti30 
where d(0) = 0,6(u)  = 1 for u > 0. The result will follow if we can show that G k  is K-convex, continuous, and Gk(y) -, co as 1 y I + co. The difficult part is to 
show K-convexity since K-convexity of Gk+ does not imply K-convexity of 
E {Jk+ ,(max[O, y - w])}. It will be sufficient to show that K-convexity of 
Gk+ implies K-convexity of 
H(y) = p max[o, -yl  + Jk+  l(maxCO, yl), (68) or equivalently that 
W Y )  - H(Y - b)  
b 
K + H(y + z) 2 H ( y )  + z vz 2 0, b > 0, Y* 
By K-convexity of Gk+ we have for appropriate scalars sk+ and s k +  such thatGk+l(Sk+l) = minyGk+l(y)and + Gk+l(Sk+l) = Gk+l(Sk+l): 
and J k +  is K-convex by the theory of Section 3.2. 
0 Q y - b < y Q y + z For this region (69) follows from 
K-convexity of Jk + 1. 
Case 2 y - b < y < y + z Q 0 In this region H is linear and hence 
K -convex. 
Case 3 y - b < y Q 0 Q y + z In this region (69) may be written 
[in view of (68)] as K + J k +  l(y + z) > J k +  ,(O) - p(y + z). We will show 
that 
Case 1 
K +  J k + l ( Z )  > J k + l ( O )  - pz vz 2 0. (7 1) 
106 3 APPLICATIONS IN SPECIFIC AREAS 
If s k +  < 0 < z ,  then using (70), the fact p > c, and part (iv) of the lemma in Section 3.2, 
K f J k +  1(Z) = K - Cz + G k +  ~ ( z )  3 G k +  i(0) - pz = J k +  i(0) - PZ. 
Thus (71) is proved and (69) follows for the case under consideration. 
Case4 y - b < O < y < y + z  T h e n O < y < b . I f  
CH0.I) - H(O)I/y 2 CWY) - H(Y - b)l/b, (72) 
then since H agrees with J k +  on [0, co) and J k +  is K-convex, 
where the last step follows from (72). If 
CH(Y) - ~ ( O ) I / Y  < W ( Y )  - H(Y - b)l/b, 
WY)  - H(O) < ( ~ / b )  CWY) - WY - bll = ( ~ / b )  CWy) - H(O) + P(Y - b)]. 
(1 - (Y/b))CH(Y) - N0)I  < (Y/b)P(Y - b) = -PY( l  - cv/b)), 
m y )  - H(O) < -py.  
then we have 
It follows that 
and since b > y, 
(73) Now we have, using the definition of H, (71), and (73), 
H ( y )  - H(Y - b, = H ( y )  + H(O) - PY - H(O) + PCV - b) 
b b H(Y)  + z 
= H(Y) - PZ < H(O) - P(Y + z) 
< K + H ( y  + z). 
Hence (69) is proved for this case as well. Q.E.D. 7. Consider the dynamic portfolio problem of Section 3.3 for the case where at each period k there is a forecast that the rates of return of the risky assets for that period will be selected in accordance with a particular probability distribution as in Section 2.3. Show that a partially myopic policy is optimal. 8. Consider a problem involving the linear system 
x k + l  = A k x k  + B k U k ,  k = 0, 1,. . . , N - 1, 
where the n x n matrices A k  are given and the n x m matrices B k  are in- dependent random matrices and have given probability distributions 
PROBLEMS 107 
that do not depend on x k ,  uk .  The problem is to find the optimal control law {p$(xo) ,  . . . , pE- l ( x N -  ,)} that maximizes the cost functional E {U(c’xN)) ,  
where c is a given n-dimensional vector. We assume that U :  R + R is a 
concave utility function satisfying for all y 
- U’(y)/U”(y) = u + by, 
and that the control is unconstrained. Show that the control law consists of affine functions of the current state. 
Hint Reduce the problem to a one-dimensional problem, and use the results of Section 3.3. 9. Consider the asset-selling problem of Section 3.4 for the case where successive offers are not lost but can be accepted at any subsequent time period. Determine the general form of the optimal policy. 10. Suppose that an individual wants to sell his house and an offer comes in at the beginning of each day. We assume that successive offers are independent and an offer is x j  with probability p i ,  j = 1, . . . , n, where x j  are given non- 
negative scalars. Any offer not immediately accepted is not lost but may be accepted at any later date. Also, a maintenance cost c is incurred for each day that the house remains unsold. The objective is to maximize the price at which the house is sold minus the maintenance costs. Consider the problem when there is a deadline to sell the house within N days and characterize the optimal policy. 11. Capacity Expansion Problem Consider a problem of expanding the capacity of a facility for production of a single type of nonstorable good or service over N time periods. Let us denote by xk the production capacity at the beginning of the kth period and by uk 2 0 the addition to capacity during the kth period. Thus capacity evolves according to 
xk+l = xk + uk, k = 0, 1, .  .., N - 1. 
The demand at the kth period is denoted wk and has a known probability distribution that does not depend on either xk or uk. Also successive demands are assumed to be independent and bounded. We denote: 
Pk(xk + uk - wk) penalty cost associated with capacity xk + uk and 
Ck(uk) expansion cost associated with adding capacity uk 
demand wk, S(xN) salvage value of final capacity x N .  
Thus the cost functional takes the form 
108 3 APPLICATIONS IN SPECIFIC AREAS 
(a) Derive the DP  algorithm for solving this problem. (b) Assume that S is a concave function with limx+m dS(x)/dx = 0, Pk 
are convex functions, and the expansion cost Ck is of the form 
where K 2 0, ck > 0 for all k .  Show that the optimal policy is of the (s, S )  type assuming cky + E {Pk(y  - wk)) 4 00 as IyI 4 a. 
(c) In (b) assume that forecasts on wk as in Problem 5 are available. Derive the optimal policy for this case. 12. A Gambling Problem A gambler enters a game whereby he may at any time k stake any amount U k  2 0 that does not exceed his current fortune xk (defined to be his initial capital plus his gain or minus his loss thus far). He wins his stake back and as much more with probability p ,  where 4 < p < 1 ,  and he loses his stake with probability ( 1  - p) .  Show that the gambling 
strategy that maximizes E {In xN}, where x N  denotes his fortune after N plays, 
is to stake at each time k an amount uk = (2p - I)&. 
(Note The problem is related to the portfolio problem of Section 3.3.) 13. A collection of N 2 2 objects is observed randomly and sequentially one at a time. The observer may either select the current object observed, in which case the selection process is terminated, or reject the object and proceed to observe the next. The observer can rank each object relative to those he has already observed and the ob- jective is to maximize the probability of selecting the “best” object according to some criterion. It is assumed that no two objects can be judged to be equal. Let r* be the smallest positive integer r such that 
Optimal Termination of Sampling 
Show that an optimal policy requires that the first r* objects be observed. If the r*th object has rank 1 relative to the others already observed, it should be selected, otherwise the observation process should be continued until an object of rank 1 relative to those already observed is found. 
Hint We assume that if the rth object has rank 1 relative to the previous (r  - 1 )  objects, then the probability that it is best is r / N .  For k 2 r* let Jk(0) 
be the maximal probability of finding the best object assuming k objects have been selected and the kth object is not best relative to the previous (k  - 1 )  
objects. Show that 
PROBLEMS 109 
14. A Class of Nonlinear Quadratic Problems Within the framework of the basic problem consider the case of a quadratic cost functional of the form 
and an n-dimensional nonlinear system of the form 
x k + l  = A k X k  + B k U k  + m k  + f k ( X k ,  U k ,  w k ) ,  k = 0, 1,. . . , N - 1, 
where Ak,  Bk ,  mk,  and& are given. We assume for all k, x k ,  u k ,  
E { f k ( x k ,  u k ,  w k ) l x k ,  u k )  = 0, wk 
and that the covariance matrix 
F ( X k ,  u k )  = E { f k ( x k ,  u k ,  w k ) f k ( x k ,  u k ,  w k y l x k ,  u k )  wk 
is a general quadratic function of x k ,  u k  for all k, i.e., F k  has a representation of the form 
n' 
F k ( X k ,  U k )  = p: + 1 P:($X; w : x k  + U ; N : X k  + * U ; M L U k  + X ; g L  + u;h;), 
i =  1 
where n' = [n(n + 1)/2], P:, W; ,  N:, M:  are given matrices of appropriate dimensions, g:, h: are given vectors, and P i ,  W:,  M: are symmetric. For any square matrix L denote by tr(L) the trace of L, i.e., the sum of the diagonal elements of L. Define for all k 
110 3 APPLICATIONS IN SPECIFIC AREAS 
Show that if the matrices R"k defined above are positive definite for all k, then 
the control law {p;, pf, . . . , defined by 
&Xk) = -R";'(A",xk + f i k ) ,  k = 0, 1,. . . , N - 1 ,  
is optimal. Hint Show by induction that the cost-to-go functions obtained from the 
DP algorithm are of the form 
J k ( X k )  = + & S k X k  + d ; x k  + e k ,  k = 0,. . . , N - 1. 
Chapter 4 
Problems with Imperfect State Information 
4.1 Reduction to the Perfect State Information Case 
We consider now an important class of sequential optimization problems that is characterized by a situation often appearing in practice. Again we have the discrete-time dynamic system considered in the basic problem of Chapter 2 that we wish to control. However, we assume that the state of the system is no longer known at each stage to the controller (imperfect state information). Instead the controller receives some information at each stage about the value of the current state. Borrowing from engineering terminology, we shall loosely describe this information as noisy measurements of a function of the system state. The inability of the controller to observe the exact state could be due to physical inaccessibility of some of the state variables, or to inaccuracies of the sensors or procedures used for measurement. For example, in problems of control of chemical processes it may be physically impossible to measure exactly some of the state variables. In other cases it may be very costly to obtain the exact value of the state even though it may be physically possible to do so. In such problems it may be more efficient to base decisions on in- accurate information concerning the system state, which may be obtained at substantially less cost. In other situations, such as hypothesis testing problems, 
111 
112 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
often of interest in statistics, the exact value of the state (true hypothesis) may be found only in an asymptotic sense after an infinite number of measurements (samples) has been obtained. Given that measurements are costly, a problem often posed is to determine when to terminate sampling so as to minimize observation costs plus the cost of error in the estimation of the system state. Thus in such situations not only is it impossible to determine the exact state of the system but the measurement process is the focal point of the decision problem itself. 
Problems with imperfect state information are, generally speaking, con- siderably more complex than problems with perfect state information both from the analytical and computational point of view. Conceptually, however, they are no different from problems with perfect state information, and in fact, as we will demonstrate shortly, they can be reduced to problems of perfect state information by means of a simple reformulation. 
First let us state the basic problem with imperfect state information with which we will be concerned. 
BASIC PROBLEM WITH IMPERFECT STATE INFORMATION Consider the basic problem of Section 2.1, where the controller instead of having perfect know- ledge of the state has access to observations z k  of the form 
ZO = ho(xo, 0 0 ) ~  z k  = h k ( X k ,  u k -  1, 0 k ) ,  k = 1, 2, . . . , N - 1. (1) 
The observation z k  belongs to a given observation space 2,; u k  is a random observation disturbance belonging to a given space V,, and is characterized by given probability measures Puo( - lxo), Puk( - J x k ,  U k -  I)r k = 1 ,  . . . , N - 1, 
which may depend explicitly on the state x k  and the control U k -  but not on prior observation disturbances u o ,  . . . , u k -  or any of the disturbances wo,  . . . , w k .  The initial state xo  is also random and characterized by a given 
probability measure Pxo.  The probability measure PWk( - I x k ,  u k )  of w k  is given and may depend explicitly on x k  and U k  but not on prior disturbances w o ,  . . . , w k -  1. The control u k  is constrained to take values from a given 
nonempty subset U k  of the control space c k .  It is assumed that this subset does not depend on x k  . 
Let us denote by the information available to the controller at time k and call it the information vector. We have 
(2) 
We consider the class of control laws (or policies), which consist of a finite sequence of functions 71 = {po ,  pl, . . . , pN- 1} where each function p k  
maps the information vector I k  into the control space C k  and 
I k  = (zo, 21,. . . , Z k ,  Uo, U1, . . . , u k - l ) ,  k = 1, 2 , .  . . , N - 1, 
I 0  = zo.  
4.1 REDUCTION TO THE PERFECT STATE INFORMATION CASE 113 
Such control laws are termed admissible. The problem is to find an admissible control law n: = { p o ,  pl, . . . , p N - l }  that minimizes the cost functional 
c N - 1  -l 
subject to the system equation 
x k + l  = f k C X k ,  pk(Ik), w k l ,  k = 0, 1, . * * 9 N - 1 ,  
and the measurement equation 
zo = ho(xo9 uo), 
zk = hk[xk, pk- l ( Ik- l ) ,  u k ] ,  k = 1, 2, . . . , N - 1 .  
The real-valued functions 
g N : S N + R ,  gk:Sk X Ck X D k - + R ,  k = 0 , 1 ,  ..., N -  1, 
are given. 
Notice the difference from the case of perfect state information. Whereas before we were seeking a rule that would specify the control uk to be applied for each state xk and time k ,  now we are looking for a rule that tells us the control to be applied for every possible information vector 1, (or state of information), i.e., for every sequence of measurements received and controls employed up to time k.  This difference, at least at the conceptual level, is actually more apparent than real as will be seen in what follows. 
Similarly, as for the basic problem of Section 2.1, the following sequence of events is envisioned in the problem above once an admissible policy n = { p o ,  p l ,  . . . , p N - l }  is adopted: 
Stage 0 (1) The initial state x o  is generated according to the given probability measure Pxo. 
(2) The observation disturbance uo is generated according to the pro- bability measure Puo( - I xo). 
(3) The controller observes zo = ho(xo, uo) and applies uo = po(lo) ,  where lo = zo.  
(4) The input disturbance wo is generated according to the probability 
( 5 )  The cost go[xo ,  po(Zo), wo]  is incurred. (6) The next state x1 is generated according to the system equation 
Stage k (1) The observation disturbance u k  is generated according to 
measure Pwo( - I xo 3 Po(10)). 
x1 = f O C X 0 ,  P O ( Z O ) ,  W o l .  
the probability measure Puk( - Ixk, uk- 
114 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
(2) The controller observes z k  = h k [ X k ,  p k -  l ( z k -  1), v k ]  and applies 
( 3 )  The input disturbance w k  is generated according to the probability 
(4) The cost g k [ x k ,  & ( I k ) ,  w k ]  is incurred and added to previous costs. ( 5 )  The next state x k +  is generated according to the system equation 
Last Stage (N - 1) (1) The observation disturbance v N -  is generated 
(2) The controller observes zN-l  = h N - l [ ~ N - l ,  p N - z ( Z N - z ) ,  and where IN- = ( zo ,  . . . , zN- 1, u o ,  . . . , u N - J .  
(3) The input disturbance w N -  is generated according to the probability 
(4) The cost g N -  1 [ x N -  1, p N -  l(IN- 1), w N -  1 ]  is incurred and added to 
( 5 )  The final state x N  is generated according to 
uk = p k ( I k ) ,  where I k  = ( 2 0 ,  . . . , z k ,  uo, . . . , u k -  1). 
measure Pwk( * I x k ,  p k ( I k ) ) -  
x k +  1 = f k C X k ,  p L k ( l k ) ,  w k l .  
according to P,, - 
applies uN- = pN- l(IN- 
measure P w , - l ( *  IxN-1, p N - i U N - 1 ) ) .  
previous costs. 
- I x N -  1, u N -  J .  
x N  = f N -  1 C x N -  1, pN- l ( I N -  11, w N -  11. 
(6) The terminal cost g N ( x N )  is incurred and added to previous costs. Again the above process is well defined and the stochastic variables are 
generated by means of a precisely formulated probabilistic mechanism. Similarly, however, as for the perfect information case the cost functional 
N -  1 
is not in general a well-defined random variable in the absence of additional assumptions and structure. Again we shall bypass a rigorous formulation of the problem in view of the introductory nature of the text.? However, we mention that the cost functional can be viewed as a well-defined random variable if the space of the initial state So and the disturbance spaces D k  and 
V,, k = 0, 1,. . ., N - 1, are finite or countable sets. As we shall shortly 
demonstrate, the imperfect state information problem defined above may be converted by reformulation into a perfect state information problem. Once this reformulation is considered the problem may be rigorously posed in the manner described in Section 2.1. 
We now provide an example of a problem that fits the general framework introduced in this section : 
t For a recent treatment of the delicate mathematical questions involved in a rigorous and general analysis of the problem of this chapter we refer the reader to the monograph by Striebel [S18a]. 
4.1 REDUCTION TO THE PERFECT STATE INFORMATION CASE 115 
EXAMPLE 1 A machine can be in one of two states denoted 0 and 1. State 0 corresponds to a machine in proper condition (good state) and state 1 to a machine in improper condition (bad state). If the machine is operated for one unit time, it stays in state 0 with probability 3 provided it started at 0, and it stays in state 1 with probability 1 if it started at 1, as Fig. 4.1 shows. The 
FIGURE 4.1 
machine is operated for a total of three units of time and starts at state 0. At the end of the first and second unit of time the machine is inspected and there are two possible inspection outcomes denoted G (probably good state) and B (probably bad state). If the machine is in state x = 0, the inspection outcome is G with probability 3;  if the machine is in x = 1, the inspection outcome is B with probability 3 :  
P(Glx = 0) = 2, After each inspection one of two possible actions can be taken: 
Action C continue operation of the machine. Action S stop the machine, do a complete and accurate inspection, and 
if the machine is in state 1 bring it back to the proper state 0. 
P(B(x = 0) = i, P(Glx = 1) = i, P(B~x = 1) = 2. 
There is a cost of 2 units for using a machine in state 1 for one time unit and zero cost for using a machine in state 0 for one time unit. There is also a cost of 1 unit for taking action S. 
The problem is to determine the policy that minimizes the expected costs over the three time periods. In other words, we want to find the optimal course of action after the result of the first inspection is known, and after the results of the first and second inspection (and, of course, the action taken after the first inspection) are known. 
116 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
It is not difficult to see that this example falls within the general framework of the problem of this section. The state space consists of the two states 0 and 1, 
state space = (0, l}, 
and the control space consists of the two actions 
control space = { C ,  S } .  
The system evolution may be described by introducing a system equation 
X k + l  = W k ,  k = 0, 1, 
where for k = 0, 1 the probability distribution of wk is given by 
P(wk = O I X k  = 0, uk = c) = 5, P(wk = 1 Ixk = 0, uk = c) = 3, 
P(w, = O I X k  = 1, uk = c) = 0, 
P(wk = O I X k  = 0, uk = s) = $9 
P(wk = 1 l x k  = 1, u k  = c) = 1, 
P(wk = 1 Ixk = 0, uk = S )  = 3, 1 
P(wk = o ( x k  = 1, uk = s) = 3, P(wk = 1 I x k  = 1, uk = S) = 3. 
We denote by x o ,  x l ,  x 2  the state of the machine at the end of the first, second, and third time unit, respectively. Also we denote by uo the action taken after the first inspection (end of first time unit) and by u1 the action taken after the second inspection (end of second time unit). The probability distribution of xo is 
P(x0 = 0) = 3, P(x0 = 1) = 3. 
Concerning the observation process we do not have perfect state information since the inspections do not reveal the state of the machine with certainty. Rather the result of each inspection may be viewed as a measurement on the state of the system taking the form 
Z k  = U k ,  k = 0, 1, 
where for k = 0, 1 the probability distribution of u k  is given by 
P ( V k  = G l X k  = 0) = 2, P(uk = G l X k  = 1) = $, 
P(uk = B l X k  = 0) = $, P(uk = Blxk = 1) = 3. 
The cost resulting from a sequence of states x o ,  x 1  and actions uo,  u1 is 
d x o ,  uo) + g(x1, U l ) ,  
g(0,C) = 0, g(0,S) = 1, g(1, C )  = 2, g(1,S) = 1. 
where 
4.1 REDUCTION TO THE PERFECT STATE INFORMATION CASE 117 
The information vector at times 0 and 1 is 
and we seek functions po(Io), pl(Z1) that minimize 
E { S C X O ,  P0UO)l + 9cx1, P l ( I 1 ) I l  XO. WO. W I  
00, V I  
= E { d x o ,  P O ( Z 0 ) l  + S C X l ,  P l ( Z 0 ,  z1, P O ( Z 0 ) ) l l .  (4) XO. WO. W I  
V O .  01 
We shall provide a complete solution of this problem once we introduce the related DP algorithm. 
Let us now show how the general problem of this section can be refor- mulated into the framework of the basic problem with perfect state informa- tion. Similarly, as in the discussion of the state augmentation device of Section 2.3, it is intuitively clear that we should define a new system the state of which at time k consists of all variables the knowledge of which can be of benefit to the controller when making the kth decision. Thus a first candidate as the state of the new system is the information vector I k .  Indeed we will show that this choice is appropriate. 
We have by definition [cf. Eq. (2)] for every k, 
I k + l  = ( I k ,  zk+l, u k ) ,  k = 0, 1,. . . , N - 2, 10 = Z o .  (5) 
These equations can be viewed as describing the evolution of a system of the same nature as the one considered in the basic problem of Section 2.1. The state of the system is I k ,  the control u k ,  and z k +  can be viewed as a random dis- turbance. Furthermore, we have, simply by the definition of I k ,  
P ( Z k +  1 z k +  1 I I k  3 u k )  = p ( z k +  1 E z k +  1 I I k ,  u k ,  ZO 3 z1, * * . 3 z k ) ,  
for any event z k +  (a subset of zk+ l). Thus the probability measure of z k +  
depends explicitly only on the state and control u k  of the new system ( 5 )  and not on the prior “disturbances” z k ,  . . . , z l .  It should be noted that the pro- bability measure of z k +  is completely determined from the statistics of the problem. We have for any event z k  + 
P ( Z k + l E z k + l I z k ~ U k )  = P[hk+l(Xk+l,Uk, V k + l ) E z k + l l l k , U k ] ,  
and the probability on the right is completely determined from the statistics 
of the problem (i.e., the probability measures of wk, . . . , wo, v k  + 1 ,  . . . , vo,  xo) 
and I k  and u k .  
118 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Now we turn to the reformulation of the cost functional in terms of the variables of the new system. We have for any admissible control law A = 
{PO 9 Pl? . . . 3  P N  - 1 1  
N -  1 
XO. W k .  Vk { k = O  
= E z k  [ i l g k [ l k ?  k = O  P k ( l k ) ] } ,  
J n  = E g N ( X N )  + 1 g k C X k r  P k ( z k ) ,  w k l  
k = O ,  .... N- 1 
k = O ,  ..., N -  1 
where the functions g k ,  k = 0,.  . . , N - 1, are defined by 
@ N - 1 C z N - 1 ?  P N - l ( I N - l ) ]  
= E { g N [ f N -  1 C X N -  l r  P N -  IN- I ) ,  w N -  1 1 1  X N -  1. W N  - I 
+ g N -  1 C x N -  1 ,  PN- l ( I N -  11, w N -  1 1  [ I N -  1 ,  P N -  l ( I N - 1 ) )  (7) 
g k k C z k ,  P k ( l k ) l  = E { g k [ X k ,  P k ( l k ) r  w k l  I l k ,  P k ( l k ) } .  (8) Xkq w k  
The conditional probabilities P ( W k l I k ,  P k ( l k ) ) ,  k = 0, 1, . . . , N - 1, are 
determined from P ( w k  I x k ,  P k ( l k ) )  and P ( x k  I l k ) .  
Thus the basic problem with imperfect state information has been re- formulated to a problem with perfect state information that involves system ( 5 )  and cost functional (6). By writing the DP algorithm for this latter problem we have 
J k ( l k )  = inf g k ( l k r  u k )  + E { J k +  l ( l k ,  z k +  1 ,  U k ) l z k ,  u k )  . U k E U k  [ Zkf 1 1 
Using (7) and (8) the algorithm can be written 
E UN - I E U N  - I XN - 1. W N  - I 
{ g N C f N -  l ( X N -  l r  U N -  1 ,  W N -  1 1 1  [ J N -  l ( I N -  1 )  = inf 
+ g N - 1 ( X N - 1 ,  U N - 1 ,  W N - 1 ) I z N - l ,  . N - l } ] ,  (9) 
4.1 REDUCTION TO THE PERFECT STATE INFORMATION CASE 119 
Equations (9) and (10) constitute the basic DP algorithm for the problem 
of this section. An optimal control law {&, py, . . . , pg- 1} is obtained by 
first solving the minimization problem in (9) for every possible value of the information vector I N -  , to obtain & l( IN- l). Simultaneously J N -  1(IN-  1) 
is computed and used in the computation of JN - J I N  - 2 )  via the minimization in (lo), which is carried out for every possible value of I N - 2 .  Proceeding similarly one obtains J N -  3 ( I N -  3) and pg- and so on until Jo(Zo) = Jo(zo) is computed. The optimal cost J* is then obtained from 
J* = E ( J O ( Z 0 ) ) .  20 
Let us now demonstrate the DP algorithm (9) and (10) via the example 
EXAMPLE 1 (continued) We first use (9) to compute Jl(Zl) for each of 
given earlier : 
the eight possible information vectors I, = (zo, z,, uo). These vectors are 
I ,  = (G, G ,  C) ,  (G,  G,  S),  (4 G,  C),  (B, G,  S),  (G, B, C),  (G, 4 S),  
(4 B, C),  (4 B, S) .  
We shall compute for each Il  the expected cost associated with u1 = C and u1 = S and select as optimal the action with the smallest cost. We have 
cost of c = 2 x P(X1 = 1(11), cost ofS = 1, 
and therefore 
Jl(Zl) = min[2P(x, = 1 l Z l ) ,  11. 
The probabilities P(x l  = 1 I Z , )  may be computed by using Bayes’ rule and the data of the problem. Some of the details will be omitted. We have: 
For I ,  = (G, G ,  S )  
Hence 
D J1(G, G ,  S )  = +, py(G, G,  S )  = C .  4 
For I ,  = (B, G,  S )  
D 
P(xl = 1 ) B ,  G,  S )  = P(xl  = 1 IG, G ,  S )  = +, 
J1(B, G,  S )  = 5, pL:(B, G,  S )  = C .  4 
120 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
For Il = (G, B, S )  
D J , (G ,  B, S )  = 1, pT(G, B, S )  = S. 4 
P(x, = l(B,B,S)=P(x,= lIG,B,S)=;, 
D J1(B, B, S )  = 1, p?(B, B, S )  = s. a 
For I ,  = (B,  B, S )  
For Il = (G,  G ,  C )  
P ( x ,  = 1, G ,  G ,  C) 1 
- -   
P(G, G ,  C )  5 ’  P(xl = 1 JG,  G,  C )  = 
D J1(G, G ,  C )  = f ,  pT(G, G,  C )  = C.  a 
For I ,  = (B, G,  C )  P(xl = 1 IB, G,  C) = g, 
D J1(B, G,  C )  = g, p?(B, G ,  C )  = C .  a 
For I ,  = (G, B, C )  P(x~ = 1 IG, B, C) = A, 
D J , (G ,  B, C )  = 1, &(G, B, C )  = S .  a 
For I ,  = (B, B, C )  P(x1 = 1 IB, B, C )  = 8, 
D J1(B, B, C )  = 1, pT(B, B, C )  = s. a 
Summarizing the results for the last stage the optimal policy is to con- tinue (ul = C )  if the result of the last inspection was G,  and to stop (u ,  = s) 
if the result of the last inspection was B. 
Here we use (10) to compute J o ( I o )  for each of the two pos- sible information vectors I. = (G), I ,  = (B). We have 
First Stage 
cost of c = 2P(x, = 1 IIO, C )  + E { J , ( I o , z , ,  C)llo, CI 
21 
= 2P(xo = 1 IZo, C) + P(z1 = GlZo, C ) J l ( I o ,  G ,  C )  
+ P(z1 = BIIO, W l U O ,  B, C),  
cost of s = 1 + E { J , ( Z O ,  z1, S ) I I o ,  SI 
21 
= 1 + P ( z ~  = G l I o ,  S ) J l ( I o ,  G ,  S )  + P ( Z 1  = BIIo, S ) J l ( I o ,  B, S),  
4.1 REDUCTION TO THE PERFECT STATE INFORMATION CASE 121 
and 
Jo(Zo) = min[2P(x0 = 1 I I , ,  C )  
For lo = ( G )  Direct calculation yields 
Using the values of J1 obtained in the previous stage 
D J,(G) = g, p:(G) = C .  4 
For I ,  = (B)  Direct calculation yields 
P(z1 = G ( B ,  C )  = g, 
P(zl = GIB, S )  = A, 
P(zl = BIB, C )  = g, 
P(z1 = BIB, S )  = &, 
P(x,  = 1 IB, C )  = $, 
and 
J,(B) = minC2 x + #,(B, G,  C) + gJ , (B ,  B, C) ,  1 + &J1(B, G, S )  
+ &JAB, B, S)l. 
Using the values of J1 obtained in the previous stage 
D 
122 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Summarizing, the optimal policy for both stages is to continue if the 
The optimal cost is result of the latest inspection is G and stop otherwise. 
J* = P(G)Jo(G) + P(B)J,(B). 
Since P(G)  = &, P(B)  = A, 
In the above example the computation of the optimal policy and the optimal cost by means of the DP  algorithm (9) and (10) was made possible by the great simplicity of the problem. It is easy to see that for a more complex problem and in particular one where the number of possible information vectors is large (or infinite) and the number of stages N is also large, the computational requirements of the DP  algorithm can be truly prohibitive. This is due to the fact that it is necessary to apply the algorithm over the space of the information vector l k ,  and, even if the control and observation spaces are simple (one dimensional or finite), the space of the information vector may be very complex and may have large dimension particularly for large values of k. This fact makes the application of the algorithm very difficult or computationally impossible in many cases. Not only is it necessary to carry out the D P  computation over spaces of large dimension but also the storage of the functions that constitute the optimal controller presents a serious problem since values of control input must be stored for each possible value of information vector I k  and for every k. Furthermore, the measure- ments zk obtained during the control process must be continuously stored by the controller. This rather disappointing situation motivates efforts aimed at the reduction of the data, which is truly necessary for control purposes. In other words, it is of interest to look for quantities that ideally would be of smaller dimension (can be characterized by a smaller set of numbers) than the information vector Ik and nonetheless contain all the information in I k  that is necessary for control purposes. Such quantities are called sufJicient statistics and are the subject of Section 4.2. 
4.2 Sufficient Statistics 
Referring to the DP algorithm of Eqs. (9) and (10) let us consider the following definition : 
Definition Let &( - ), k = 0, 1, . . . , N - 1, be functions mapping the 
information vector I ,  into some space M k ,  k = 0, 1, . . . , N - 1. We shall say 
that the functions So( - ), . . . , SN- - ) constitute a suficient statistic with 
4.2 SUFFICIENT STATISTICS 123 
respect to the problem of the previous section if there exist functions H,,, 
. . . , HN- such that 
+ g N - l ( X N - l ,  u N - l ,  W N - l ) I I N - l ,  u N - l }  
V I N -  I r  U N -  1 E U N -  1 ,  (12) 
where J k  are the cost-to-go functions of the D P  algorithm (9) and (10). 
written in terms of the functions H k  as Since the minimization step of the D P  algorithm (9) and (10) can be 
it follows immediately from the above definition that an optimal control law need only depend on the information vector I k  via the suficient statistic S k ( I k ) .  
In other words if the minimization problem in (13) has a solution for every I k  and k, there exists an optimal control law that can be written 
p f ( l k )  = 17 ,* [Sk(1k)1 ,  = O, 1, . . . 9 - 1, (14) 
where pf is an appropriate function determined from the minimization (13). Thus if the sufficient statistic is characterized by a set of fewer numbers than the information vector I k ,  it may be easier to implement the control law in the form u k  = j i f [ S k ( I k ) ]  and take advantage of the resulting data reduction. 
While it is possible to show that many different functions constitute a sufficient statistic for the problem that we are considering [the identity function & ( I k )  = I k  is certainly one of them], we will focus attention on a particular one that is useful both from the analytical and the conceptual point of view in many cases. This sufficient statistic is the conditional pro- bability measure of the state x k ,  given the information vector I k ,  
S k ( 1 k )  = P x k ~ ~ k ,  k = 0, 1, . . . , N - 1. 
This function S k  maps the space of information vectors into the space of all probability measures on the state space. It is easy to see that the conditional probability measures Pxkl Ik  indeed constitute a sufficient statistic.? This is 
t Abusing mathematical language we make no distinction between the function sk and its value Sk(Ik), calling them both a sufficient statistic. 
124 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
evident from definition (1 1) and (12) and the fact that the probability measures of w k  and u k  + depend explicitly only on x k ,  u k  and x k  + u k ,  respectively, and not on prior disturbances. 
Now the sufficient statistic PxkIrk is generated recursively in time and can be viewed as the state of a controlled discrete-time dynamic system. By using Bayes' rule we can write 
where @k is some function that can be determined from the data of the pro- blem, u k  is the control of the system, and z k +  plays the role of a random dis- turbance the statistics of which are known and depend explicitly on PxkIrk and u k  only and not on z k ,  . . . , zo.  For example, if the state space, control 
space, observation space, and disturbance space are the real line and all random variables involved possess probability density functions, the con- ditional density p ( x k +  Ilk+ 1)  is generated from p ( x k  Ilk), u k ,  and means of the equation 
z k + l  by 
- P ( X k + l l z k ,  u k ) p ( z k + l l u k ,  x k + l )  
jzrn p ( x k +  1 1 I k ,  u k ) p ( z k  + 1 I u k ?  x k +  1) d X k +  1 ' 
In this equation all the probability densities appearing in the right-hand side may be expressed in terms of p ( x k  I I k ) ,  u k ,  and z k +  alone. In particular, the density p(&+ 1 I k ,  u k )  may be expressed through p ( x k  I I k ) ,  u k ,  and the system equation x k +  = f k ( x k ,  u k r  w k )  using the given density p ( w k  I&, u k )  and the relation 
m 
d w k l z k ?  u k )  = / - a p ( x k I I k ) p ( w k I x k ,  u k )  d x k .  
The density p ( z k  + I u k ,  x k +  1) is expressed through the measurement equation Z k +  1 = hk+ l(xk+ 1, u k ,  u k +  1 )  using the given probability density 
d U k + l  I u k ,  x k + l ) .  
By substituting these expressions in the equation for p ( x k +  Ilk+ 1) we obtain an equation of the form of (15). Other explicit examples of equations of the form of (15) will be given in subsequent sections. In any case one can see that the system described by (15) is one t h a t j t s  the framework of the basic problem. Furthermore, the controller can calculate (at least in principle) at time k the conditional probability measure P x k , I k .  Therefore, the controlled system (1 5) is one for which perfect information prevails for the controller. 
4.2 SUFFICIENT STATISTICS 125 
Now the DP algorithm (9) and (10) can be written in terms of the suf- ficient statistic Pxkl Ik  by making use of the new system equation (15) as follows: 
- 
inf [ { S N C f N -  1 b N -  1, UN- 1 ,  W N -  1 1 1  
J N - l ( P X N - l I I N - I )  = " N - I E u N - I  X N - 1  , W N - ,  
f g N - l ( X N - l ?  u N - l ?  w N - l ) l z N - l ?  u N - l )  3 (16) 1 
which results from the minimization of the right-hand side of (16) and (17). 
This control law yields in turn an optimal control law {pg, . . . , pg- for 
the basic problem with imperfect state information by writing 
pk*(zk) = p k * ( P x k l l k ) ,  = O, . . * 9 N - 1. 
In addition, the optimal value of the problem is given by 
where J o  is obtained by the last step of the algorithm (16) and (17) and the probability measure of zo is obtained from the statistics of xo and uo and the measurement equation zo = ho(xo, uo). 
It should be evident to the perceptive reader that the development of the D P  algorithm (16) and (17) was based on nothing more than a reduction of the basic problem with imperfect state information to a problem with perfect state information that involves system (15), the state of which is P x k l f k ,  and an appropriately reformulated cost functional. Thus the analysis of this section is in effect an alternate reduction of the problem of Section 4.1 to the basic problem with perfect state information. A conclusion that can be drawn from the analysis is that the conditional probability P x k l f k  summarizes all the information that is necessary for control purposes at period k .  In the absence of perfect knowledge of the state the controller can be viewed as controlling the 
126 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
“probabilistic state” PXklIk  so as to minimize the expected value of the cost-to-go conditioned on the information I k  available. 
The two reductions into the basic problem with perfect state information that we gave in this and the previous section are by far the most useful such reductions. Naturally there arises the question as to which of the two DP algorithms (9) and (10) or (16) and (17) is the most efficient. This depends on the nature of the problem at hand and, in particular, on the dimensionality of the conditional probability Pxkl Ik .  If PxklIk  is characterized by a finite set of numbers and may be computed with relative ease, then it may be profitable to carry out the DP algorithm over the space of the sufficient statistic Pxklrk.  Such, for example, is the case where the state space for each time k is a finite set { X I , .  . . , x”} (i.e., the system is a controlled finite state Markov chain). In this case PxklIk consists of the n probabilities P(xk = xi I Ik), i = 1, . . . , N. 
Another case is when the conditional probability PXklIk is Gaussian and is therefore completely characterized by its mean and covariance matrix. Examples of these cases will be given in subsequent sections. If PXklIk  cannot be characterized by a finite set of numbers, then the DP algorithm (9) and (lo), which is carried over the space of the information vector I k ,  may be preferable, although actual calculation of an optimal control law is possible only in very simple cases due to the dimensionality problem. 
Let us now demonstrate algorithm (16) and (17) by means of an example. 
EXAMPLE 1 (continued) In the two-state example of the previous section let us denote 
p1 = P(x,  = 1 I Z l ) ,  p o  = P(X0 = 1110). 
The equation relating p l ,  p o ,  uo,  z1 [cf. Eq. (15)] is written 
P 1  = ao(P0, uo, Z J  
One may verify by straightforward calculation that Q0 is given by 
if uo = S ,  z 1  = G ,  
if uo = S ,  z1 = B, 3 5 
- 
P 1  = Oo(P0, uo, z1) = + 2~~ if uo = C, z1 = G, 
7 - 4p0 
if uo = C,  z1  = B. 3 + 6Po 
4.2 SUFFICIENT STATISTICS 127 
Algorithm (16) and (17) may be written in terms of po, pl, and above as 
Jl(pl) = min[2pl, 11, 
]o(p0) = min[2po + P(z l  = GIZo, C)JIC@o(~o, C,  Gll 
+ P(Z1 = B l ~ o ,  C)JlC@O(PO, c, B)1, 
+ P(Z1 = BIZ07 S ) J l C @ O ( P O ,  S ,  Bill. 
1 -t P(z1 = S)J1C@&o, S ,  G)1 
The probabilities entering in the second equation may be expressed in terms of p o  by straightforward calculation as 
P(Z1 = GlZo, C )  = (7 - 4pJ12, 
P(Z1 = GlZo, S )  = 7/12, 
Using these values we have 
P(zl = B l l o ,  C )  = (5 + 4po)/12, P(zl = BIZo, S )  = 5/12. 
12 
Now by minimization in the equation defining J , ( p , )  we obtain an optimal control law for the last stage 
Also by substitution of calculation we obtain 
and by carrying out the straightforward 
if $ < po < 1, (7 + 32p0)/12 if 0 ,< po < $, J O ( P 0 )  = 
and an optimal control law for the first stage 
Note that 
P(xo = llz, = C )  = $, 
P(z0 = G )  = 1 2 ,  
P(x0 = llzo = B)  = +, 
P(z0 = B) = &, 
128 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
so that the formula for the optimal value 
yields the same optimal value as the one obtained in the previous section by means of the DP algorithm (9) and (10). 
We finally note that, regardless of its computational value, the representa- tion of the optimal control law as a sequence of functions of the conditional probability PxklIk  of the form 
CL?( lk )  = F?(Pxkjik). k = 0, 1, . . ., N - 1, 
is a conceptually useful device. An interesting interpretation of this equation is that the optimal controller is composed oftwo cascaded parts: an estimator, which uses at time k the measurement zk and the control uk- to generate the conditional probability Pxkl lk ,  and an actuator, which generates a control input to the system as a function of the conditional probability Pxk,,k (Fig. 4.2). 
W k  
I I 
Aside from its conceptual and analytical importance this interpretation has formed the basis for various suboptimal control schemes that separate a priori the controller into an estimator and an actuator and attempt to design each part in a manner that seems “reasonable.” Schemes of this type will be presented in the next chapter. 
4.3 LINEAR SYSTEMS WITH QUADRATIC COST FUNCTIONALS 129 
4.3 Linear Systems with Quadratic Cost Functionals -Separation of Estimation and Control 
In this section we consider the imperfect state information version of the problem examined in Section 3.1, which involved a linear system and a quadratic cost functional. We have the same discrete-time linear system 
x k + ]  = A k X k  -k B k U k  -/- wk, k = 0, 1, ..., N - 1, (18) 
and quadratic cost functional 
(1 9) 
but now the controller does not have access to the current system state. Instead it receives at the beginning of each period k an observation of the form 
(20) 
where z k  E R‘, Ck is a given s x m matrix, k = 0, 1, ; . . , N - 1, and vk E Rs is 
an observation noise vector with given probability distribution. Furthermore, the vectors u k  are independent random vectors and are assumed to be in- dependent from wk and xo as well. We make the same assumptions as in Section 3.1 concerning the input disturbances W k ,  and we assume that the system matrices Ak, Bk are known. 
It is clear that this problem falls within the framework of the basic pro- blem with imperfect state information of Section 4.1. We will analyze the problem by using the reduction and the DP algorithm of Section 4.1. 
I N -  1 
E { X k Q N X N  + 1 ( X ; Q k X k  + u H R k U k )  3 
k = O  
zk = C k X k  + u k ,  k = 0, 1 , .  . . , N - 1, 
From Eqs. (9) and (10) we have 
JN-l(ZN-l) = min E { ( A N - I ~ N - l  + B N - l ~ N - l  + wN-l )IQN 
X ( A N - I X N - ~  4- B N - I ~ N - I  + W N - I )  X ~ - I Q N - I X N - I  
+ u ~ - ~ R N - ~ u N - I I I N - I  .}I Using the fact that E { w N -  JZN- 1} = E { w N -  1} = 0, this expression can be written 
J N -  i ( I N -  1) = E { x X -  i(AX- I Q N A N -  1 + Q N -  1 ) x ~ -  i IIN- 1) X N -  I 
+ r n i n [ ~ k - ~ ( B ~ - , Q ~ B ~ - ~  + R N - l ) ~ N - l  UN-l 
130 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
The minimization yields the optimal control law for the last stage, 
ug- 1 = pg- l ( I N -  1) 
= - ( B ~ - ~ Q N B N - ~  + RN-l)-lBh-lQNAN-l E{XN-IIIN-I}, (22) and upon substitution in (21) we obtain 
J N - I ( I N - ~ )  = E { x h - i K ~ - i X ~ - i l ~ N - l )  X N - l  
-I- E {CxN-l - E{XN-lIIN-l}]’PN-l[XN-~ 
X N - l  
- ~ ~ x N - l ~ ~ N - l ~ ~ ~ z N - l ~  + E {wk-iQNwN-i), (23) 
W N -  I 
where the matrices K N -  and PN- are given by 
PN-I = A~-IQNBN-I(RN-I + B;Y-~QNBN-,)-’BN-~QNAN-~, K N - 1  = A h - i Q N A N - 1  - P N - 1  + Q N - 1 .  
Note that the control law (22) for the last stage is identical to the cor- responding optimal control law for the problem of Section 3.1 except for the fact that xN- Notice also that expression (23) for the cost-to-go J N -  l(IN- l )  exhibits a corresponding similarity to the cost-to-go for the perfect information problem except for the fact that J N -  1(xN- 1) contains an additional middle term, which expresses a penalty due to estimation error. 
is replaced by its conditional expectation E {xN- I lIN- 
Now the DP equation for period N - 2 is 
J N - ~ ( I N - ~ ) =  Illin E { X ~ - ~ Q N - ~ X N - ~  + U ~ - ~ R N - ~ U N - ~  U N -  2 X N  - 2 w N  - 2 
I J N -  I 
[ 
}I 
1 
+ JN-l(IN-l)IIN-Zr uN-2 
= min E { x L - ~ Q N - ~ X N - ~  + U ~ - ~ R N - ~ U N - ~  U N - 2  [ X N - Z W N - 2  
+ ( A N - 2 X N - 2  + B N - 2 U N - 2  + W N - 2 Y K N - l ( A N - 2 X N - 2  
+ B N - 2 U N - 2  + wN-2)11N-2} 
f E { E {[XN-1 - E{XN-llIN-l}I’PN-l[XN-l 
- E { X N -  1 I IN- I}] 1 IN- 1) I IN- 2 9 uN- 2 
Z N - I  X N - 1  
4.3 LINEAR SYSTEMS WITH QUADRATIC COST FUNCTIONALS 131 
Note that we have excluded the next to last term from the minimization with respect to u N - 2 .  We have done so since this term will be shown to be inde- pendent of uN-2-a fact due to the linearity of both the system and the measurement equation. This property follows as a special case of the following lemma. 
Lemma Let g :  R" + R be any function such that the expected values 
appearing below are well defined and finite and consider the function 
fk(zk-lrZk,Uk-l) = E{gCXk - ~ ~ ~ k ~ ~ k - l ~ z k ~ u k - l ~ ~ ~ z k - l ~ z k ~ ~ k - l ~ ~  
Xk 
Then for every k = 1 ,2 , .  . . , N - 1, the function 
E {fk(lk-l, Z k r  u k - l ) l l k - l ?  uk-l} zk 
does not depend on u k -  i.e., 
- 
E{fk(lk-lrzk, u k - l ) l l k - l *  uk-l) = E{fk(lk-lrZk, ak-l)llk-l?uk-l}? Zk Zk 
for all 1,- 1, uk- i i k -  1. 
Proof Define for every i = 0, 1, . . . , N - 1, the vectors 
Then, in view of the linearity of the system equation, we have for all i, 
x i + l  = r i x o  + A ~ O ~  + ~ ~ i i ~  
where T i ,  A i ,  Ei are known matrices of appropriate dimension. These matrices are obtained from the system matrices Ai, Bi by straightforward calculation. Hence we have 
fk(lk-i,Zk, u k - 1 )  = E{drk-i(Xo - E{XoIlk-i,Zk, uk-i))+ A k - i  
x ("k- 1 - E {@k- 1 I l k -  1. zk, u k -  1>)1 I l k -  1, zki uk- 11% 
The measurement equations may also be written 
zi = Cir i - lxo  + CiAi-li5i-l + CiEi-liii-l + u i ,  i = 1,2,. . . , N - 1, 
z, = cox, + 0,. 
Now in view of these expressions the conditional probability distribution of 
zo, z1 - CIEoiio, . . . , zk - Ck&- 1iik- 1, and hence we have 
(Xo, 6k-i)giVen(Ik-1, Zk, Uk-,)dependsOnlk_1, Zk, U k - 1  throughthevectors 
fk(lk-l,ZkrUk-l)= hk(ZCl,Z1 - CIEOGO,*.*,Zk - CkEk-lCk-l) 
132 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
for some function h k .  Thus for any I k -  1, u k -  we have 
E ( f k ( l k - 1 ,  z k ,  u k - l ) ~ z k - l ~ u k - l }  z k  
= E { h k ( Z O , Z 1  - C I E O c O , . . . ? Z k  - C k E k - l G k - 1 ) 1 I k - 1 , u k - l ) .  
Zk 
Equivalently by using the equation 
z k  - C k E k - l f i k - 1  = C k r k - l X O  + C k A k - l G k - 1  + u k  
we obtain 
E ( f k ( I k - 1 ,  Z k ?  u k - l ) l z k - l ,  u k - l }  Zk 
= E ( h k ( Z 0 ,  Z1 - -ClEoGo, .  . ., z k - 1  X O . W k - l ~ U k  
- C k - l E k - 2 f i k - 2 ,  C k r k - l X O  + c k A k - 1 6 k - 1  + u k ) l z k - l ,  u k - 1 ) .  
Since the last expression above does not depend on U k -  the result follows. Q.E.D. 
sirnilarly as for the last stage Returning now to our problem, the minimization in Eq. (24) yields 
u ; - 2  = p g - 2 ( I N - 2 )  = - ( R N - 2  + B ' N - 2  K N -  1 B N - 2 ) - '  
X HN- 2 K N -  I A N -  2 E { X N  - 2 I IN- 21,  
and proceeding similarly we obtain the optimal control law for every stage 
D pLk*(Ik) = Lk E t X k  I I k }  4 (25) 
D L k  = -(& + B ; K k + i B k ) - ' B ; K k + l A k ,  U 
where 
and where the matrices K k  are given recursively by the matrix Riccati equation 
K N  = Q N  
K k  = A ; [ K k + i  - K k + l B k ( R k  + B ; K k + ~ B k ) - ~ % K k + l l A k  + Q k .  
Generalizing an observation made earlier, we note that the optimal con- trol law (25) is identical to the optimal control law for the corresponding perfect state information problem of Section 3.1 except for the fact that the state x k  is now replaced by its conditional expectation E { x k  I I k } .  
It is interesting to note that the optimal controller can be decomposed into the two parts shown in Fig. 4.3, an estimator, which uses the data to generate 
4.3 LINEAR SYSTEMS WITH QUADRATIC COST FUNCTIONALS 133 
1 - - Estimator 
FIGURE 4.3 
the conditional expectation E {xk I I k } ,  and an actuator, which multiplies E { x k  II , }  by the gain matrix Lk and applies the control input uk = Lk E { x k  1 I , }  to the system. Furthermore, the gain matrix Lk is independent of the statistics of the problem and in particular is the same as the one that would be used ifwe were faced with the deterministic problem where wk and xo  would be fixed and equal to their expected values. On the other hand it is known (see Section 1.3 and the Appendix to this chapter) that the estimate +?(I) of a random n- vector x given some information (random vector) I ,  which minimizes a positive definite quadratic form of the expected value of the estimation error 
E { [ x  - a(I ) ] 'M[x  - +?(I)]}, M = positive definite symmetric, 
x, I 
is precisely the conditional expectation Ex { x  I I } .  Thus the estimator portion of the optimal controller is an optimal solution of the problem of estimating the state xk assuming no control takes place, while the actuator portion is  an optimal solution of the control problem assuming perfect state information prevails. This interesting property, which shows that the two portions of the optimal controller can be designed independently as optimal solutions of an estimation and a control problem, has been called the separation theorem for linear systems and quadratic criteria and occupies a central position in modern automatic control theory. 
Another interesting observation is that the optimal controller applies at each time k the control that would be applied if we were faced with the deter- ministic problem of minimizing the cost-to-go 
N -  1 
x ~ Q N x N  + 1 (x:Qixi + u:Riui) 
i = k  
134 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
and the input disturbances w k ,  w k +  1 ,  . . . , w N -  and current state x k  were 
known and fixed at their conditional expected values, which are zero and E { x k  I I k } ,  respectively. This is another form of the certainty equivalence principle, which was referred to in Section 3.1. For a generalization of this fact to the case of correlated disturbances see Problem 1, the hint to which provides the clue for a short proof of the separation theorem. 
Implementation Aspects-Steady-State Controller-Stability 
As explained in the perfect information case, the linear form ofthe actuator portion of the optimal control law is particularly attractive for implementa- tion. In the imperfect information case, however, we are faced with the addi- tional problem of constructing an estimator that produces the conditional expectation E { x k  I I k } .  The implementation of such an estimator is by no means easy in general. However, in one important special case, the case where the disturbances w k ,  u k ,  and the initial state xo are Gaussian random vectors, a convenient implementation of the estimator is possible by means of the celebrated Kalman filtering algorithm [K 11. This algorithm provides the conditional expectation E { x k  I I,'}, which due to the Gaussian nature of the uncertainties turns out to be a linear function of the information vector I k , ?  i.e., the measurements zo,  z l , .  . . , z k  and the controls uo, u l , .  . . , t 4 k - l .  
The computations, however, are organized recursively so that only the most recent measurement z k  and control u k -  are needed at time k, together with E { x k -  I l k -  1} in order to produce E { x k  11,'). The form of the algorithm is the following (see the Appendix at the end of this chapter for a derivation of the algorithm) : 
E { X k + i l I k + i }  = A k E { X k l I k }  + B k u k  
f ~ k + l l k + l C ; + l N ~ ~ l [ Z k + l  - C k + l ( A k E { X k I I k }  + B k U k ) ]  
k = 0 , 1 ,  . . . ,  N -  1, 
(26) 
where the matrices are precomputable and given recursively by 
t Actually the conditional expectation E { x k  1 Ik} can be shown to be a linear function of I ,  for a more general class of probability distributions of x,,, wkr vk that includes the Gaussian distribution as a special case, the class of so-called spherical/v inrlariant disrriburions [V6, B24). 
4.3 LINEAR SYSTEMS WITH QUADRATIC COST FUNCTIONALS 135 
with 
XOl0 = s - sc;(c,scb + No) - lCos .  
In this equation M k ,  N k ,  and S are the covariance matrices of wk, u k ,  and x o ,  respectively, and we assume that w k  and u k  have zero mean, i.e., 
E { W k }  = E { V k }  = 0, 
M k  = E { W k W ; } ,  N k  = E { U k U ; } ,  k = 0, 1, ..., N - 1, 
s = E{Cxo - E{xo)lCx - E{xoIl’} .  
Simple modifications are required if w k ,  
Thus under the additional assumption of Gaussian uncertainties the implementation of the optimal controller is quite convenient. Furthermore, if the system and measurement equations and the disturbance statistics are stationary and the horizon tends to infinity, it can be shown under mild assumptions (see Section 3.1 and the Appendix to this chapter) that both the gain matrices L k  and the matrices C k l k  of the Kalman filtering algorithm (26)-(29) tend to steady-state matrices L and X, a fact that can be utilized to simplify greatly the implementation of the optimal controller by replacing the time-varying gain matrix (&+ I l k +  lC;+ 
Let us provide the equations for this steady-state implementation of the control law. Time indices will be dropped where they are superfluous due to stationarity. The control law takes the stationary form 
have nonzero means. 
by a constant matrix. 
p * ( l k )  = L 2 k ,  
where we use the notation 
E { X k I I k }  = 2 k ,  L = - ( R  + B’KB)-’B’KA, 
and K is the unique positive semidefinite symmetric solution of the algebraic Riccati equation 
K = A’[K  - KB(R + B’KB)-’B’K]A + Q. 
By the theory of Section 3.1 this solution exists provided the pair (A, B)  is controllable and the pair (A ,  F )  is observable where F is a matrix such that Q = F F .  The conditional expected value 2, is generated by the “steady- state” Kalman filtering equation (see the Appendix) 
= ( A  + B L ) R k  + z C ‘ N - ’ [ Z k + l  - C ( A  + B L ) R k ] ,  
where c is given by 
2 = c - ZC‘(CCC + N)-’Cc,  
136 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
and C is the unique positive semidefinite symmetric solution of the algebraic Riccati equation 
C = A [ C  - CC'(CCC' + N ) - ' C Z ] A '  + M .  
As indicated in the Appendix, it follows from the theory of Section 3.1 that this solution exists provided the pair ( A ,  C )  is observable and the pair ( A ,  D )  is controllable, where D is a matrix such that M = DD'. 
Now by substituting zk+ with its value 
z k + l  = c x k + l  + vk+l = CAXk + CBL2k + cwk + vk+l ,  
the system equation and the Kalman filter equation can be written 
xk+ 1 = AX, + BLak + wk, 
2 k + l  = CC'N-'CAxk 4- ( A  + B L  - ZCfN- 'CA)2k  
EC'N-l(CWk + u k + l ) .  
These equations may be viewed as representing a 2n-dimensional dynamic system whose state is the vector [ x ; ,  a;]' and which is perturbed by vectors that depend on wk and uk+ 1. From the practical point of view it is important that this system is stable, i.e., the 2n x 2n matrix 
1 [ E c N - l c A  A + B L  - xC"- lCA 
A B L  
is a stable matrix. Indeed this can be shown under the preceding control- lability and observability assumptions (see the Appendix in this chapter). Thus the combined estimation and control scheme based on approximation of the optimal controller by a stationary controller results in a stable system as well as an implementation that is attractive from the engineering point of view. 
It is to be noted that in the case where the random vectors W k ,  vk, x o  are not Gaussian the controller 
j i * ( I k )  = LkR(Ik), k = 0, 1,. . . , N - 1, (30) 
is often used, where a ( I k )  is the linear least-squares estimate of the state xk given the information vector I k  (see the Appendix). It can be shown (see Problem 2) that the controller (30) is optimal in the restricted class of all controllers, which consists only of linear functions of the information vectors I k .  One can show (see the Appendix) that the estimate $ k ( I k )  is again provided by the Kalman filtering algorithm (26)-(29) simply by replacing E {xk I I k }  
by t k ( I k ) ,  and thus the control law (30) can be conveniently implemented. Thus in the case of non-Gaussian uncertainties the control law (30) may re- present an attractive suboptimal alternative to the optimal control law (25). 
4.4 FINITE STATE MARKOV CHAINS-A PROBLEM OF INSTRUCTION 137 
Nonetheless, using the control law (30) may result in a very substantial in- crease in the resulting value of the cost functional over the optimal value. 
Finally a case that deserves special mention involves the linear system (18) and linear measurement equation (20) and a nonquadratic cost functional. Under the assumption that the random vectors are Gaussian and independent it can easily be shown by using the sufficient statistic algorithm of Section 4.2 that an optimal control law can be implemented in the form 
P * ( l k )  = /%CE{XkI I k } ] .  
In other words, the control input need only depend on the conditional ex- pected value of the state. This result holds due to the fact that the conditional probability measure Pxkl Ik  is Gaussian (due to linearity and Gaussian un- certainties) and furthermore the covariance matrix corresponding to PXklIk  is precomputable (via the Kalman filtering algorithm mentioned earlier) and cannot be influenced by the control input. 
4.4 Finite State Markov Chains-A Problem of Instruction 
Among problems with imperfect state information the class that involves a finite state system (finite state space) deserves particular attention. Not only is it a class of problems of general interest but also it admits a computationally tractable solution via the sufficient statistic algorithm of Section 4.2. As dis- cussed in that section, the basic problem with imperfect state information can be reformulated into a problem with perfect state information which involves a system the state of which is the conditional probability measure P x k l I k .  When the state space contains only a finite number of states x l ,  x 2 ,  . . . , x", the conditional probability measures PXklIk  are characterized by the n-tuple 
where 
Thus for each period the state space for the reformulated problem is the simplex 
and the control input need only be a function of the current conditional probabilities p i ,  i = 1, . . . , n. In this way substantial data reduction is 
achieved since all the necessary information provided by the measurements is summarized in these conditional probabilities. The probabilistic state Pk 
138 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
can be computed at each time by the optimal controller on the basis of the previous state p k -  1, the control u k -  1, and the new measurement z k .  The DP algorithm (16) and (17) can be used for the calculation of the optimal control law. 
Whenever the control and measurement spaces are also finite sets, it turns out that the cost-to-go functions J k ( P k ) ,  k = 0,1, .  . . , N - 1, in 
algorithm (16) and (17) have a particularly simple form, a fact first shown by Smallwood and Sondik [S13]. One may show that 
J k ( P k )  = min[P; a:, Pk a:, . . . , P; a?], where a:, at, . . . , a? are some n-dimensional vectors and P; a{ ,  j = 1, . . . , mk, 
denotes the inner product of P k  and a{. In other words, the functions 3, are “piecewise linear” and concaue over { ( p ’ ,  . . . , @’)[pi > 0, pi = l}. 
The demonstration of this fact is straightforward but tedious and is outlined in the hint to Problem 7. The piecewise linearity of J k  is, however, an important 
property since may be completely characterized by the vectors a:, . . . , a?. 
These vectors may be computed through the DP algorithm by means of special procedures, which in addition yield an optimal policy. We will not describe these procedures here. They can be found in references [S13] and [S14]. Instead we shall demonstrate the DP algorithm by means of examples. The first of these examples, a problem of instruction, is considered in this section. The second, a hypothesis testing problem, is treated in the next section and is of importance in statistics. 
A Problem of Instruction 
Consider a problem of instruction where the objective is to teach the student a certain simple item. The student may be at the beginning of each period in one of two possible states 
x1 item learned, xz item not learned. 
At the beginning of each period the instructor must make one of two decisions 
u1 terminate the instruction, u2 continue the instruction for one period and at the end of the period 
conduct a test the outcome of which gives an indication as to whether the student has learned the item. 
The test has two possible outcomes 
z1 student gives a correct answer, zz student gives an incorrect answer. 
4.4 FINITE STATE MARKOV CHAINS-A PROBLEM OF INSTRUCTION 139 
The transition probabilities from one state to the next if instruction takes place are given by 
2 P ( x k + 1  = X ’ l X k  = x ’ )  = 1, P ( x k + l  = x ( x k  = x ’ )  = 0, 
P ( X k + 1 = X 1 1 X k = X 2 ) = t ,  P ( X k + l = X 2 1 X k = X Z ) = 1 - t ,  O < f <  1 .  
The outcome of the test depends probabilistically on the state of knowledge of the student as follows: 
P ( z k  = z1 I x k  = x ’ )  = 1, P ( z k  = z 2 1 x k  = x ’ )  = 0, 
P ( z k  = z l ( x k  = x 2 )  = r, P ( z k  = Z 2 1 X k  = x 2 )  = 1 - r, 0 < < 1. 
Concerning the cost structure we have that the cost of instruction and testing is Z per period and the cost of terminating the instruction is 0 and C > 0 if the student has learned or has not learned the item, respectively. The ob- jective is to find the instruction-termination policy for each period k, as a function of the test information accrued up to that period, which minimizes the total expected cost, assuming that there is a maximum of N periods of instruction. 
It is easy to reformulate this problem into the framework of the basic problem with imperfect state information. We can define a corresponding system and measurement equation by introducing input and observation disturbances w and u with probability distributionsexpressing the probabilistic mechanism of the process similarly as was described in the example of Section 4.1. Subsequently we can use the sufficient statistic algorithm of Section 4.2 and conclude that the decision whether to terminate or continue instruction at period k should depend on the conditional probability that the student has learned the item given the test results so far. This probability is denoted 
P k  = P ( x k  = x 1  I z O ,  z 1 , .  . , z k ) .  
In addition we can use the DP algorithm (16) and (17) defined over the space of the sufficient statistic pk  to obtain an optimal policy. However, rather than proceeding with this elaborate reformulation we prefer to argue and obtain directly this DP algorithm. 
Concerning the evolution of the conditional probability pk (assuming instruction occurs) we have by Bayes’ rule 
140 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
From the probabilistic descriptions given we have 
~ ( z k + l ~ ~ O , . . . , z k , x k + l  = x ' ) = p ( z k + l l x k + l  = X I )  
1 if z k + l  = z l ,  0 if z k + l  = z ,  2 
if z k + l  = zl, 
- - Y  if Z k + l  = z ,  2 
Substitution in (3 1) yields 
where the function @ is defined by 
or equivalently 
A cursory examination of this equation shows that, as expected, the condi- tional probability P k +  that the student has learned the item increases with every correct answer and drops to zero with every incorrect answer. We men- tion also that Eq. (32) is a special case of Eq. ( 1  5) of Section 4.2. The dependence of the function @ on the control uk is not explicitly shown since there is only one possible action aside from termination. 
We turn now to the development of the DP algorithm for the problem. At the end of the Nth period, assuming instruction has continued to that period, the expected cost is 
(34) 
At the end of period N - 1 ,  the instructor has calculated the conditional 
probability p N -  that the student has learned the item and wishes to decide 
whether to terminate instruction and incur an expected cost (1 - p N -  ,)C or 
J N h )  = ( 1  - P&- 
4.4 FINITE STATE MARKOV CHAINS-A PROBLEM OF INSTRUCTION 141 
continue the instruction and incur an expected cost I + E, ,  {JN(PN)} .  This leads to the following equation for the optimal expected cost-to-go : 
r 1 
Similarly the algorithm is written for every stage k by replacing N above by k +  1: 
I k ( P k )  = min (l - P k ) c ,  + E { ] k +  l C @ ( P k ,  Zk+ I ) ] } ] .  (35) [ Zk+ I 
Now using expression (33) for the function @ and the probabilities 
p ( z k + l  = z l I P k )  = P k  + (l - P k ) [ ( l  - f ) r  + t1 = 1 - (1 - t)(l - r)(l - P k ) ,  
p ( z k + l  = z 2 1 P k )  = - P k  - (1 - Pk)[(1 - f ) r  + t ]  
= (1 - l)(l - r)(l - P k ) ,  
where 
In particular, by using (34), (36), and (37) we have by straightforward cal- culation 
JN- I(PN- 1) = mi" - PN- I)C, I + A N -  I(PN- 1 1 1  
= minC(1 - P ~ - ~ ) C ,  I + (1 - t)(l - P ~ - ~ ) C ] .  
Thus as shown in Fig. 4.4 if 
I + (1 - t)C < c, 
there exists a scalar aN- with 0 < aN- < 1 that determines an optimal policy for the last period : 
continue instruction if pN- 6 aN- 
terminate instruction if pN- > aN- 
142 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
instruction instruction 
FIGURE 4.4 
It is easy to show (see Problem 8) using (37) that under condition (38) the functions A,@) are concave and “piecewise linear” (i.e., polyhedral) for each k and satisfy for all k, 
A,(1) = 0. (39) 
A,@) 2 A,@’) if 0 < p < p’ < 1, (40) 
Furthermore they satisfy for all k 
Ak- I@) < A,@) < Ak+ I@) v p  E [o, 11, k = 1,2, . . . , N - 2. (41) 
Thus from the D P  algorithm (36) and Eqs. (39)-(41) we obtain that the optimal policy for each period is determined by the unique scalars ak ,  which are such that 
(1 - ak)C = I + Ak(ak), k = 0, 1, ..., N - 1. 
An optimal policy for period k is given by 
continue instruction if p k  < ak, 
terminate instruction if pk > aka 
Now since the functions A,@) are monotonically nondecreasing with respect to k, it follows from Fig. 4.5 that 
a N - l  < a N - 2  < < ak < ak-1 < ... < 1 - (I/C),  
4.4 FINITE STATE MARKOV CHAINS-A PROBLEM OF INSTRUCTION 143 
t 
and therefore as N -, co the corresponding sequence {aN-i} converges to 
some scalar E for every fixed i. Thus as the horizon gets longer, the optimal policy (at least for the initial stages) can be approximated by the stationary policy 
continue instruction if P k  < E 
terminate instruction if Pk > E. 
It turns out that this stationary policy has a very convenient implementation that does not require the calculation of the conditional probability at each stage. From Eq. (33) we have 
(42) 
l o  if zk+l = z2. 
Furthermore, P k f  increases over P k  if a correct answer z1 is given and drops to zero if an incorrect answer z2 is given. Now define recursively the pro- babilities 
n 1  = @(o, z'), 712 = @(n1, zl), . . . 3 R k + l  = @((7Lk, zl), . . . 9 
144 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
and let n be the smallest integer for which n, > Cr. It is clear that the stationary policy (42) can be implemented as follows : 
terminate instruction if n successive correct answers have been received, continue instruction otherwise. 
4.5 Hypothesis Testing-Sequential Probability Ratio Test 
In this section we consider a hypothesis testing problem characteristic of a class of problems that are of central importance in statistical sequential analysis. The decision maker must sequentially and at each period either accept on the basis of past observations a certain hypothesis out of a given finite collection as being true and terminate experimentation, or he must delay his decision for at least one period and obtain, at a certain cost, an additional observation that provides information as to which hypothesis is the correct one. We will focus attention on the simplest and perhaps the most important case, where there are only two hypotheses. The approach can be easily generalized to the case of more hypotheses but the corresponding results are not as elegant. 
Let z,, z,, . . . , zN- , be a sequence of independent and identically dis- 
tributed random variables taking values on a countable set 2. Suppose we know that the probability distribution of the Z ~ S  is eitherf, orfl and that we are trying to decide on one of these. Here for any element z E Z,f,(z) [fi(z)] denotes the probability of z occurring whenf, (fl) is the true distribution. At 
time k after observing z,, . . . , zk we may either stop observing and accept 
eitherf, orfl,  or we may take an additional observation at a cost C > 0. If we stop observing and make a choice, then we incur zero cost if our choice is correct, and costs Lo,  L ,  if we choose incorrectlyf, andf,, respectively. We are given the a priori probability p that the true distribution isf, and we assume that at most N observations are possible. 
It is easy to see that the problem described above can be formulated as a sequential optimization problem with imperfect state information involving a two-state Markov chain. The state space is {xo, x'}, where we use the notation 
xo true density isf,, x1 true density isf,. 
The system equation takes the simple form Xk+' = xk and we can write a measurement equation zk = vk, where vk is a random variable taking values in 2 with conditional probability distribution 
4.5 HYPOTHESIS TESTING-SEQUENTIAL PROBABILITY RATIO TEST 145 
Thus it is possible to reformulate the problem into the framework of the basic problem with imperfect state information and use the sufficient statistic DP algorithm of Section 4.2 for the analysis. This algorithm is defined over the interval [0, 11 of possible values of the conditional probability 
P k  = P(xk = xoIzO,. . . , zk). 
Similarly as in the previous section we shall obtain this algorithm directly. The conditional probability Pk is generated recursively according to the 
following equation (assumingfo(z) > O,,fl(z) > 0 for all z E Z) 
k = 0 , 1 ,  ..., N - 1 ,  (43) P k  f O ( z k  + 1 ) PkfO(Zk+l) + ( l  - Pk)fl(Zk+l)’ 
P k + l  = 
where p is the a priori probability that the true distribution isfo. The optimal expected cost for the last period is 
(45) j N -  1 b N - 1 )  = min[(l - P N -  l ) L O ,  PN-  lL1l ,  
where (1 - pN- l)Lo is the expected cost for acceptingf, and pN- lL1 is the 
expected cost for acceptingf,. Taking into account (43) and (44) we can obtain the optimal expected cost-to-go for the kth period from the equation 
(l - pk)LO, PkL1, 
where the expectation over Zk+l is taken with respect to the probability distribution 
where 
146 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
An optimal policy for the last period (see Fig. 4.6) is obtained from the minimization indicated in (45): 
accept fo if PN-  2 p, 
accept fl if pN- < p, 
where p is determined from the relation (1  - p)Lo = pL1 or equivalently 
We now prove the following lemma. 
Lemma The functions A , :  [O, 11 -+ R of (47) are concave and satisfy 
Ak(0) = Ak(1) = 0 Vk = 0, 1, .  . . , N - 2, 
A k - l ( P )  Vp~[0,1], k = l , 2  ,..., N - 2 .  
Proof The last two relations are evident from (45)-(47). To prove con- cavity of A k  in view of (45) and (46) it is sufficient to show that concavity of J k +  implies concavity of A,  through relation (47). Indeed assume that Jk+ is concave over [0,1]. Let zl, z2,  z3,  . . . denote the elements of the countable observation space Z. We have from (47) that 
4.5 HYPOTHESIS TESTING-SEQUENTIAL PROBABILITY RATIO TEST 147 
Hence it is sufficient to show that concavity of J k +  implies concavity of each of the functions 
To show concavity of hi we must show that for every L E [0, 13, pl, p2 E [0, 11 we have 
Ahi(p1) + (1 - A)hi(p2) 6 hiCAp1 + (1 - I)p21* 
Using the notation 
41 = PlfO(Z')  + (1 - Pl)f l (Z ' ) ,  5 2  = PZfO(Z') + (1 - PZ)fl(Z'), 
the inequality above is equivalent to 
(APl + (1 - 4PZ)fO(Zi) 
6 l k + l  
This relation, however, is implied by the concavity of I,+,. Q.E.D. 
Using the lemma we obtain (see Fig. 4.7) that if 
c + A,-zCLo/(Lo + L1)I < LOLl/(LO + Ll), 
then an optimal policy for each period k is of the form 
accept fo if Pk 3 ak, accept fl if Pk < bk, continue the observations if /?k < Pk < ak, 
where the scalars ak, Bk are determined from the relations 
148 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Hence as N + co the sequences {aN-i}, { / ? N - i }  converge to scalars E ,  8, re- 
spectively, for each fixed i, i = 1,2, . . . , and the optimal policy is approxi- mated by the stationary policy 
accept fo if pk 2 E, 
continue the observations if 8 < pk < E. accept fi if P k  < B, (48) 
Now the conditional probability pk is given by 
where p is the a priori probability thatf, is the true hypothesis. Using (49) the stationary policy (48) can be written in the form 
if Rk 2 A = (1 - p)d /p ( l  - d), accept fo accept fi if Rk < B = (1 - p)b/p(l - B), (50) 
continue the observations if B < Rk < A,  
4.6 SEQUENTIAL SAMPLING OF A LARGE BATCH 149 
where the sequential probability ratio Rk is given by 
Rk = fO(zO) * * * fO(zk)/fl(zO). . . fl(zk). Note that Rk can be easily generated by means of the recursive equation 
R k + l  = [f~(~k+l)/fl(zk+l)l~k. 
A sequential decision procedure of form (50) is called a “sequential probability ratio test.” Procedures of this type were among the first formal methods of sequential analysis studied by Wald [Wl] and have extensive applications in statistics. The optimality of policy (48) for a problem involving an unlimited number of observations will be shown in Section 7.2. 
4.6 Sequential Sampling of a Large Batch 
This section deals with a problem of inspection of a large batch of items. Samples from the batch are taken sequentially at a cost C > 0 per item and inspected for defects. On the basis of the number of defective and nonde- fective items inspected one must decide whether to classify the batch as defective or nondefective or continue sampling. Let q, with 0 < q < 1, denote the quality of the batch, which represents the true proportion of defective items. We denote 
a(q) cost of accepting a batch of quality q, r(q) cost of rejecting a batch of quality q, 
f ( q )  a priori probability density function of q. We assume that a(q) and r(q) are nonnegative and bounded over [0, 13. 
The problem is to find a sampling policy that minimizes the expected value of the sum of the sampling costs and the acceptance-rejection costs. We shall assume initially that the maximum number of samples that can be taken is N and that sampling does not affect the composition of the batch. Subsequently we shall examine the limiting case where N is very large and tends to infinity. 
Clearly this problem is of a similar nature as the one of the previous section There are some important differences, however, which are perhaps worth going over. In both problems we have the same control space (accept, reject, or take another sample). The system and measurement equations in both problems can be taken to have the same form 
x k + l  = x k ,  z k  = uk. 
However, whereas in the problem of the previous section we had two hypo- theses (corresponding to the two densities fo ,fl) in the present problem es- sentially we have an infinity of hypotheses (one for each quality q E [0, 11). 
150 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Thus the state space is different in the two problems. The observation space is also different. In the previous section the observation space was countably infinite while in the present problem there are only two outcomes per sample (defective, nondefective), i.e., v k  takes only the two values 
defective with probability 4, 
nondefective with probability 1 - 4. 
The differences described above induce an important change in the treatment of the present problem since it is not convenient to employ as a sufficient statistic the conditional probability density of 4 given the measurements in view of infinite dimensionality. Fortunately enough there is another suf- ficient statistic, which turns out to be convenient in the present case thanks to the binary nature of the observation space. Assume that we are at time k and consider the pair (m, n), where m + n = k and m is the number of defective outcomes up to time k, and n the number of nondefective outcomes up to time k. A little thought should convince the reader that all the information that the statistician needs to know at time k for decision purposes is summarized in the pair (m,  n), and hence (m, n) can be viewed as a sufficient statistic in accordance with the definition of Section 4.2. The verification of this fact is left to the reader. We proceed below to state and analyze the DP algorithm in terms of the sufficient statistic (m, n). We obtain the algorithm directly rather than through a reformulation into the general problem of this chapter. Such a reformulation is of course possible. 
Given (m, n) the conditional probability density function of 4 can be calculated to be 
The conditional probability of obtaining a defective sample at time k + 1 given that (m, n) with m + n = k has occurred can be calculated to be 
and, of course, the conditional probability of a nondefective sample is 
[1 - d(m, n)]. Note that the scalarsf(qlm, n) and d(m, n) may be computed 
a priori for each (m, n). 
Let us denote by Jk(m, n) the optimal cost-to-go of the process at time k given that sampling has produced the pair (m,  n) with m + n = k. At this 
4.6 SEQUENTIAL SAMPLING OF A LARGE BATCH 151 
point the costs involved are 
Let us denote by g(m, n) the minimum of the acceptance and rejection costs given (m, n): 
The DP algorithm may now be written 
J d m ,  n) = g(m, n), 
Jk(m, n )  = min[g(m, n),  C + d(m, n)Jk+l(m + 1, n) (54) 
+ c1 - d(m, n)]Jk+l(m,  n + l ) ] .  (55) 
Note that J ,  is defined over the set Sk of pairs of nonnegative integers (m, n) with m + n = k. The sets Sk, which are, of course, finite, are shown in Fig. 4.8. Thus if the permissible number of samples N is not very large, the sets S o ,  S 1 ,  . . . , SN collectively contain relatively few points and the computa- 
tion of the optimal policy via the DP algorithm (54) and (55) is relatively easy. On the other hand when N is very large (and indeed there is a priori no reason why it should not be when the batch is large) computation (54) and (55) be- comes inefficient. Nonetheless we will see that under an assumption often satisfied in practice one can limit the maximum number of samples to be taken without loss of optimality. 
For any nonnegative integers m, n, N with m + n < N let us denote by J(m, n, N )  the optimal “cost-to-go” Jk(m, n) (k = m + n) obtained from al- gorithm (54) and (55) when the maximum sample size is N. In general, J(m, n, N) depends on N. If, however, the costs a(q) and r(q) and the pro- bability density function f ( q )  are such that for some integer m 
g(m,n) < C for allm,n with m + n 2 w, (56) 
then from (55) we obtain 
J(m, n, N) = g(m, n) for all m, n with m + n 2 m. 
152 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Under these circumstances acceptance or rejection takes place after at most N samples are taken, and the optimal sampling policy is the same for all N 2 N. This policy can be obtained through the DP algorithm (54) and (55 )  provided the number of stages N satisfies N 2 m. As an example, let a(q) = 0 if q -= 0.75; a(q) = 1 if q 2 0.75; r(q) = 0 if q > 0.25; r(q) = 1 if q < 0.25; 
f ( q )  = 1, C = 0.004. Then one has 
and one can verify that g(m, n) < 0.004 = C for m + n 2 10. Thus it is sufficient to solve the problem for N = 10. 
4.7 Notes 
Sequential decision problems with imperfect state information and the idea of data reduction via a sufficient statistic have been considered very early particularly in the statistics literature (see, e.g., Blackwell and Girshick [B23] and the references quoted therein). In the area of stochastic control the suf- ficient statistic idea gained wide attention following the 1965 paper by Striebel [SlS] (see also CS16, S191) although the related facts were known to most 
PROBLEMS 1 53 
researchers in the field by that time. For the analog of the sufficient statistic concept in sequential minimax problems see the work of Bertsekas and Rhodes [BlS]. 
For literature on linear quadratic problems with imperfect state infor- mation see the references quoted for Section 3.1 and Witsenhausen’s survey paper [W7]. The Kalman filtering algorithm [Kl] is a well-known and widely used tool. Detailed discussions that supplement our exposition of the Appen- dix can be found in many textbooks [J3, L8, M6, M7, Nl]. The result men- tioned at the end of Section 4.3 was pointed out by Striebel [SlS] (see also Bar-Shalom and Tse [Bl]). The corresponding result for continuous-time systems has been shown under certain assumptions by Wonham [Wl 11. For linear quadratic problems with Gaussian uncertainties and observation cost in the spirit of Problem 6 see the works of Aoki and Li [A31 and Cooper and Nahi [C4]. Problems 1 and 2, which indicate the form of the certainty equi- valence principle when the random disturbances are correlated, are based on an unpublished report by the author [B5]. 
The possibility of analysis of the problem of control of a finite state Markov chain with imperfect state information via the sufficient statistic algorithm of Section 4.2 was known for a long time. More recently it has been exploited by Eckles [E2], Smallwood and Sondik [S13], and Sondik [S14]. The proof of the “piecewise linearity” of the cost-to-go functions and an algorithm for their computation is given in references [S13] and [S14]. The instruction model described in Section 4.4 has been considered (with some variations) by a number of authors [AlO, K5, GI, S12]. 
For a discussion of the sequential probability ratio test and related sub- jects see the book by DeGroot [Dl], the lecture notes by Chernoff [C2], and the references quoted therein. The treatment provided here stems from Arrow et al. [A5]. The problem of Section 4.6 is treated by White w3] .  A similar class of problems that has received considerable attention is the class of the so-called two-armed bandit problems (see [Dl]). A simple special case is treated in Problem 10. 
Problems 
1. Consider the linear system (18) and measurement equation (20) of Section 
4.3 and consider the problem of finding a control law {&(Io), . . . , pft- 1 ( I N -  
that minimizes the quadratic cost functional r N -  1 
Assume, however, that the random vectors xo, wo, . . . , wN- 1,  u o ,  . . . , uN- 
are correlated and have given joint probability distribution and finite first 
154 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
and second moments. Show that the optimal control law is given by 
(assuming the matrices A o ,  A l ,  . . . , A N -  are invertible). 
Hint Show that the cost functional can be written 
r N- 1 
where 
P k  = B ; K k + I B k  + R k .  
2. In Problem 1 show that the control law that minimizes the value of the cost functional among all control laws that consist of linear functions of the information vector is given by 
P k * ( l k )  = L k j k ( z k ) ,  
where j k ( I k )  is the linear least squares estimate of y k  given I k ,  i.e., the linear function of I k  that solves 
min E { b k  - y k ( z k ) l ' b k  - y k ( z k ) l ) .  
Yk('), Yk(.): h e a r  Yk. Ik 
3. Consider Problems 1 and 2 with the difference that the measurements z k  
are received with a delay of m 2 1 time periods, i.e., the information vector I k  
is given by 
(Zo, . . . , Zk-,,,, u g ,  . . . , U k -  1) if k 2 m, 
I . = {  ( u O , . . * , u k - l )  if k < m. 
Show that the conclusion of both problems holds for this case as well. 4. Prove the result stated at the end of Section 4.3. 5. Consider a machine that can be in one of two states, good or bad. Sup- pose that the machine produces an item at the end of each period. The item produced is either good or bad depending on whether the machine is in a 
where the gain matrices Lk are obtained from the recursive algorithm 
and the vectors yk are given by 
PROBLEMS 155 
good or bad state, respectively. We suppose that once the machine is in a bad state, it remains in that state until it is replaced. If the machine is in a good state at the beginning of a certain period, then with probability t it will be in the bad state at the end of the period. Once an item is produced we may inspect the item at a cost I, or not inspect. If an inspected item is found bad, the machine is replaced with a machine in good state at a cost R .  The cost for producing a bad item is C > 0. Write a DP algorithm for obtaining an optimal inspection policy assuming an initial machine in good state, and a horizon of N periods. Solve the problem for t = 0.2, I = 1, R = 3, C = 2, and N = 8. (The optimal policy is to inspect at the end of the third period and not inspect in any other period.) 6. Consider the problem of estimating the common mean x of a sequence of Gaussian random variables z l r  z 2 ,  . . . , zN- 1, where zk = x + u k  and x, u l ,  
u 2 ,  . . . , uN- are independent Gaussian random variables with 
E { X }  = p, E{(X - p ) 2 }  ='Of,  E { U k }  = 0, E{U:} = 02. 
At each period k the sample zk may be observed at a cost C > 0 or else 
sampling is terminated and an estimate $(zl, . . . , zk- 1) is selected as a function 
of samples z l r  . . . , zk- observed up to that period. The cost for termination 
after observing the k first samples is 
kC + E {[X - A(Z1, . . . , Zk)l2} .  
X,ZI,....Zk 
The problem is to find the termination and estimation policy so as to minimize the cost. Show that the optimal termination time is independent of the 
particular values zl, . . . , z k  observed, and thus the problem may be solved by 
first determining E and then obtaining the optimal estimate 2 after taking E samples. 7. Control of Finite-State Systems with Imperfect State Infbrmation Consider a controlled dynamic system that at any time can be in any one 
of a finite number of states xl, x2, . . . , x". When a control u is applied, the 
transition probability of the system moving from state xi to state xj is denoted p&). The control u is chosen from a finite collection of controls u l ,  u2, . . . , urn. Following each state transition an observation is made by the 
controller. There is a finite number of possible observation outcomes denoted 
2, z 2 , .  . . ,zq. The probability of the observation outcome z', 0 = 1,. . . , q, 
occurring given that the current state is j and the previous control was u is denoted by either rJ(u, 0) or rJ(u, z'). 
(a) Consider the process after k + 2 observations zo,  zl, . . . , zk+ have 
been made and controls uo,  ul, . . . , uk have been applied. Consider the con- 
ditional probability vectors 
1 Pk = {d~. . . , !$}? P k + l  = {pk+l,*..?P;+l}, 
156 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
(b) Assume that there is a cost per stage denoted for the kth stage by gk(i, u,j) ,  associated with the control u and a transition from state xi to state x j .  
Consider the problem of finding an optimal policy minimizing the sum of the costs per stage over N periods. The terminal cost is denoted gN(xN). Show that the corresponding DP algorithm is given by 
J N - l ( P N - l )  = min [ i p k - 1  i p i J ( u ) ~ N - l ( i , u , j )  + ~ N w ) I  1 U E ( U ’ .  ..., urn) i =  1 j =  1 
J k ( P k )  = min [ i pt i Pixu)  b k ( i ,  u, j )  
uc(ul ,  .... urn) i= 1 j =  1 
(c) Show by induction that the functions JN- . . . , J o  are of the 
form 
J k ( P k )  = min[P;a:, Pka,2, . . . , pkap], where a:, a;, . . . , a? are some vectors in R” and Pka{ denotes the inner pro- 
duct of Pk and a{. 
Hint If J k +  is of the form above, show that 
- min[P;A:(u, e), . . . , P‘ k k (u, - I;= 1 c:= 1 Pt PiJW,(u, 0) 
9 
where A:(u, e), . . . , A? + I(u, 0) are some n-dimensional vectors depending on u 
and 8. Show next that 
where &(u) is the n-vector with ith coordinate equal to p i J ( u ) g k ( i ,  u, j ) .  
PROBLEMS 157 
Subsequently utilize the fact that any sum of the form 
min[Pkyl,. .., Pky,] + min[Pkjjl,. . ., Pkp,-], 
where yl, . . . , ys, jjl, . . . , j j s  are some n-dimensional vectors and s, S are some 
positive integers is equal to 
min{Pk(yi + j j j ) l i  = 1,. . . , s, j = 1,. . . , g}. 
8. Consider the functions Jk(p,) of Eq. (35) in the instruction problem. Show inductively that each of these functions is piecewise linear and concave of the form 
J k ( P k )  = min[a: + pklpk, + pip,, . . ., a? + p?pk], where a:, . . . , a?, pi ,  . . . , fikm'. are suitable scalars. 
9. Consider a hypothesis testing problem involving n hypotheses. The a priori probability of hypothesis i ,  i = 1, 2, . . . , n, being true is p i .  The cost of 
accepting erroneously hypothesis i is Li. At each sampling period an ex- periment is performed that has two possible outcomes denoted 0 and 1. The conditional probabilities of outcome 0 given that hypothesis i holds true is known and denoted aj. We assume ai # a j  for i # j. At each period one may perform another experiment at the cost C or terminate experimentation and accept one of the hypotheses. Provide a suitable D P  algorithm for finding the optimal sampling plan when the maximum number of possible experiments is N. 10. Two-Armed Bandit Problem A person is offered N free plays to be distributed as he pleases between two slot machines A and B. Machine A pays 
a dollars with known probability s and nothing with probability (1 - s). 
Machine B pays f i  dollars with probability p and nothing with probability 
(1 - p). The person does not know p but instead has an a priori cumulative 
probability distribution F(p)  of p. The problem is to find a playing policy that maximizes expected profit. Let (m + n) denote the number of plays in B after k free plays (m + n < k) and let m denote the number of successes and n the number of failures. Show that a DP algorithm that may be used to solve this problem is given by 
1,- l(m, n) = max{sa, p(m, n)p>, m + n < N - 1, 
p(m, n)CB + Jk+l(m + 1, n)I + [1 - p(m, n)IJk+ l(m, n + 1)), 
m + n < k ,  
Jk(m, n) = max{s[a + Ik+l(m, n)] + (1 - S ) J ~ + ~ ( ~ ,  n), 
where 
158 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Solve the problem for N = 6, IX = /3 = 1, s = 0.6, dF(p)/dp = 1 for 0 < p < 1. (The answer is to play machine B for the following pairs (m, n):(O, 0), (1,0), (2,0), (3,0), (4,0), (5,0), (2, l), (3, l), (4, 1). Otherwise machine A should be played.) 11. A person is offered 2 to 1 odds in a coin tossing game where he wins whenever a tail occurs. However, he suspects that the coin is biased and has an a priori cumulative probability distribution F(p) for the probability p that a head occurs at each toss. The problem is to find an optimal policy of deciding whether to continue or stop participating in the game given the outcomes of the game so far. A maximum of N tossings is allowed. Indicate how such a policy can be found by means of DP. 
Appendix Least-Squares Estimation-The Kalman Filter 
In this appendix we present the basic principles of least-squares estimation and their application in the problem of estimating the state of a linear dis- crete-time dynamic system using measurements that are linear in the state variable. 
The basic problem is roughly the following. There are two random vectors x and y taking values in Euclidean spaces R" and R", respectively. The two vectors are related through their joint probability distribution so that the value of one of the two provides information about the value of the other. For example, x may be the velocity of an automobile and y the result of an inexact measurement of this velocity, which is equal to x plus a random error that is, say, uniformly distributed over some interval. Now the situation that we examine is one where we get to know the value of y and we would like to estimate the value of x so that the estimation error is as small as possible in some sense. The criterion that we use is minimization of the expected value of the squared error between x and its estimate, which explains the term least- squares estimation. This criterion is reasonable as well as convenient from the analytical point of view. 
We begin with the problem of finding the least-squares estimate of a random vector x given the value of the measured random vector y. Next we consider the problem of finding the least-squares estimate of the random vector x within the class of all estimates that are linear in the measured vector y. Finally the results are applied to a special case where there is an underlying linear dynamic system the current state of which we would like to estimate using measurements that are obtained sequentially in time. Due to the special structure of this problem the computation of the state estimate can be or- ganized conveniently in a recursive algorithm-the Kalman filter. Through- out the exposition we will not make a notational distinction between a 
APPENDIX LEAST-SQUARES ESTIMATION -THE KALMAN FILTER 159 
random vector and particular sample values that it assumes. The precise meaning should be clear from the context. 
A. 1 Least-Squares Estimation 
Consider two jointly distributed random vectors x and y taking values in R" and R", respectively. In any particular occurrence of x and y we expect that the value of y provides information that may be used to update our a priori estimate or guess of x. For example, while prior to knowing y our estimate of x may have been the expected value E {x}, once the value of y is known we may wish to form an udpated estimate x(y )  of the value of x. This updated estimate depends, of course, on the value of y and thus we are in effect inter- ested in a rule that gives us the estimate for each possible value of y, i.e., we are interested in a function x( - ), where x(y) is the estimate of x given y. Such a function x( .): R" .+ R" we shall call an estimator. We are seeking an esti- mator that is optimal in some sense and the criterion we shall employ is based on minimization of 
where 11 - ( 1  denotes the usual norm in R"( llzl12 = z'z for z E R"). An estimator 
that minimizes the measure of error above over all x( . ): R" + R" will be 
called a least-squares estimator and will be denoted 52*( - ). It is clear that a*( - ) is a least-squares estimator if we have for every y E R" 
where the expectations are taken with respect to the conditional distribution of x given y for fixed values of y. 
The following proposition was proved in Section 1.3. We repeat the simple proof here. We shall assume in the proposition as well as throughout the Appendix that all the expected values appearing are well defined and jinite. 
Proposition A.l  The least-squares estimator i*( .)  is given by 
a*(),) = E {xly} Vy E R". (59) x 
Proof We have for every fixed z E R" 
This expression is minimized for z = Ex { x l y }  and using (58) the result follows. Q.E.D. 
160 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
A.2 Linear Least-Squares Estimation 
While the least-squares estimate is simply the conditional expectation Ex {xly}, in general the function Ex {XI.} may be a complicated nonlinear function of y. As a result its practical computation and realization in a given application may be very cumbersome. This fact motivates us to consider estimators within a restricted class that may be realized with relative ease. An important such class is the class of lineart estimators, i.e., estimators of the form 
(60) 
where A is an n x m matrix and b is an n-dimensional vector. It is thus reason- able to consider the problem of finding a linear estimator of form (60) that minimizes the expected squared error (57). An estimator 
x(y) = A y  + b, 
2(y)  = A y  + 6 
where a, 6 minimize 
E { I ~ x  - A y  - b1I2} = E {(x - A y  - b)’(x - A y  - b)} 
x, Y x. Y 
over all n x m matrices A and vectors b E R” will be called a linear least- squares estimator. 
Prior to proceeding with the derivation of the linear least-squares esti- mator we show that when x, y are jointly Gaussian random vectors the con- ditional expectation Ex {x I y} is a linear function of y (plus a constant vector) and as a result for this case a linear least-squares estimator is also a least- squares estimator. 
Consider the random (column) vector z 
taking values in Rn+m, and assume that z is Gaussian with mean 
z = E { z }  = [ E {XI ] = E] 
E {YI 
and covariance matrix 
t A more precise term is “linear plus constant” or equivalently “affine” estimators. 
APPENDIX LEAST-SQUARES ESTIMATION -THE KALMAN FILTER 161 
We shall assume that C is a positive definite symmetric (n + m) x (n + m) matrix so that it possesses an inverse. This assumption is made for convenience. The result to be proved holds, however, without this assumption. Since z is Gaussian its probability density function is of the form (see, e.g., [M6], [P2]) 
p(z) = p(x, y) = c exp[ -+(z - Z)'C-'(z - ,?)I, 
where c is given by 
c = (2~)-("+'")/~(det C)-1/2r 
with det C denoting the determinant of C. Similarly the (marginal) probability density functions of x and y are of the form 
p(x) = c1 exp[-+(x - X)'~;:(X - x)], 
where c1 and c2 are appropriate constants. By Bayes' rule the conditional probability density function of x conditioned on y is given by 
P(Y) = c2 exPC-& - J)'qyl(Y - Y)l9 
P(X I Y) = Ax, Y)/P(Y) 
= (c/c2) exp{ -*[(z - Z)'C-'(z - 5) - (y - jj)'C,'(y - p)]}. (63) 
It is now easy to see that there exist a positive definite n x n matrix D, an n x m matrix A, a vector b E R", and a scalar s such that 
(z - ZyC-yZ - 2) - (y - jj)'C,'(y - j j )  
= (X - Ay - b)'D-'(x - Ay - b) + S. (64) 
This is evident since by substitution of the expressions for Z and C of (61) and (62), the left part of (64) becomes a quadratic form in x and y, which can be put in the form indicated in the right side of (64). In fact, by computing the inverse of C using the partitioned matrix inversion formula (Appendix A) one may verify that A, b, D, and s in (64) have the form 
A = CxyC,', b = X - C xy C-'- yy y, D = Cxx - ~ x y q y l ~ y x ,  s = 0. 
Now it follows from (64) and (63) that the conditional expectation Ex {x I y} is of the form A y  + b, where A is some n x m matrix and b E R". Thus we have proved the following proposition. 
Proposition A.2 If x ,  y are jointly Gaussian random vectors, then the least-squares estimate Ex {xly} of x given y is also a linear least-squares estimate of x given y. 
We note that this proposition holds not only for a Gaussian distribution of (x, y) but also for a much wider class of distributions, which contains the Gaussian distribution as a special case (see [VS], [B24]). 
We now turn to the characterization of the linear least-squares estimator. 
162 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Proposition A.3 Let x, y be random vectors taking values in R" and R", respectively, with given joint probability distribution. The expected values and covariance matrices of x, y are assumed to exist and are denoted 
E { x }  = i? E{yI = Y, (65) 
E { ( y  - Y)(y - j ) ' }  = x y y ,  (66) 
E { b  - J ) ( x  - X)'} = zyx = xiy9 (67) 
We assume also that the inverse X i y '  exists. Then the linear least-squares estimator of x given y has the form 
(68) 
(69) 
E { ( X  - X)(x - 2)') = x x x ,  
E {(x - X)b - J)'} = xxy ,  
q y )  = X + x x y x Y y l ( y  - j ) .  
E {[x - %)I [X - %Y)I'} = CXx - ~ x y x G 1 x y x .  
t(y) = A y  + 6,  
The corresponding error covariance matrix is given by 
x* Y 
Proof The linear least-squares estimator is defined as 
where A, 6 minimize the functionf(A, b) = E x , y  {Ilx - A y  - b1I2} over A 
and b. Taking the derivatives off(A, b) with respect to A and b and setting them equal to zero we have 
o = af/aA l R ,  i; = 2 E ( ~ ( 6  + Ay - xy}, (70) 
x .  Y 
0 = af/abIi,i; = 2 E (6 + A y  - x}. (71) 
x. Y 
From (71) we have 
b = X - Aj ,  
and substitution in (70) yields 
E { y [ A ( y  - j )  - (X - X)]'} = 0. (73) 
x. Y 
We now use the identity 
E { - J [ A b  - j )  - (X - X)]'} = - j  E { A ( y  - j )  - (X - X)}' = 0. (74) 
x9 Y x. Y 
Adding (74) and (73) yields 
E {(Y - J)CA(Y - j )  - (X - X)I'} = 0, 
x .  Y 
or equivalently 
xyyA' - xyx = 0, 
APPENDIX LEAST-SQUARES ESTIMATION-THE KALMAN FILTER 163 
from which 
A = C‘ YX C- YY = zxyz;l. (75) From (72) and (75) we obtain 
R(y) = Ay + 6 = x + XXYC,’(y - j ) ,  
which was to be proved. Equation (69) follows immediately upon substitution of the expression for R(y) obtained above. 
We list below some of the properties of the least-squares estimator as corollaries. 
Q.E.D. 
Corollary A.3.1 There holds 
= E {XI = E { W I .  X Y 
Proof Immediate from (68). Q.E.D. 
Corollary A.3.2 The estimation error [x - a@)] is uncorrelated with 
both y and a@), i.e., 
E {YCX - %Y)I’I = 0, 
Proof The first equality is immediate from (70). The second equality is evident once we write R(y) in the form Ay + 6 and use the first equality and Corollary A.3.1. Q.E.D. 
Corollary A.3.2 is sometimes called the orthogonal projection principle. It states a property that characterizes the linear least-squares estimate and forms the basis for alternative treatments of the least-squares estimation problem using the so-called projection theorem (see [L8], Chapter 4). 
E {R(Y)[X - a ( ~ ) l ’ I  = 0. 
x. Y XP Y 
Corollary A.3.3 Consider in addition to x and y the random vector z defined by 
z = c x ,  
where C is a p x rn given matrix. Then the linear least-squares estimate b(y) of z given y has the form 
b(Y) = CR(Y), 
and the corresponding error covariance matrix is given by 
164 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Proof We have E {z} = 2 = CX and 
&, = E {(z - Z)(Z - Z)'} = CC,,C', 
2 
c,, = E {(z - Z)(Y - J) '}  = ccxy, 
cyr = c:, = cyxct. 2, Y 
By Proposition A.3 we have 
2(Y) = z + czyc,'(y - J )  = cx + Ce,,c,'(y - J )  = CR(y), 
E {CZ - ~(Y)ICZ - ~(Y)I'I = czz - czyc,'cyZ = C(L - L y ~ ~ l ~ Y x ) C '  
x. Y 
= C E {[x - R(y)] [X - R(y)]'}C'. Q.E.D. 
x. Y 
Corollary A.3.4 Consider in addition to x and y an additional random 
(76) 
vector z taking values in RP of the form 
z = cy + U, where C is a p x rn with p < rn (nonrandom) given matrix with full rank and u is a (nonrandom) given vector in RP. Then the linear least-squares estimate A(z) of x given z has the form 
(77) R(z) = x + c,yc'(cxyyc')-'(z - cy - u), 
and the corresponding error covariance matrix is given by 
E {[x - R(z)][x - A(z)]'} = C, - ~,yC(C~yyC)~lC~y,. (78) 
x. 2 
Proof We have by direct calculation 
From Proposition A.3 we have 
APPENDIX LEAST-SQUARES ESTIMATION-THE KALMAN FILTER 165 
where C,, = CC,,C has an inverse since Cyy is invertible and C has full rank. By substituting ‘ relations (79) into (80) the result follows. 
Notice that the error covariance matrix Ex, ,  {[x - R(z)] [x - R(z)]’} 
does not depend on the vector u, i.e., the choice of u cannot affect the quality of estimation. 
Corollary A.3.5 Consider in addition to x and y an additional random vector z taking values in RP, which is uncorrelated with y. Then the linear least-squares estimate R(y, z) of x given y and z (i.e., given the composite 
vector w, z’]’) has the form 
Q.E.D. 
A(y, 2) = R(Y) + A(z) - x, (81) 
where R(y) and R(z) are the linear least-squares estimates of x given y and given z, respectively. Furthermore, 
(82) E {[x - Rb, z)] [X - A b ,  z)I’> = E x x  - ~ x y ~ y Y 1 ~ y x  - & z ~ z Z I L  
x, Y, 
where 
Ex, = E {(x - X)(Z - Z)’}, Czx = E {(z - Z)(X - X)’}, 
x, 2 x, 
C,, = E {(z - Z)(Z - Z)’}, Z = E {z}, 
2 2 
and it is assumed that Czz is invertible. Proof Let 
w = [I], R = [3. 
We have by (68) that 
A(w) = x + CxwC;;(w - W). (83) 
Furthermore 
and since y and z are uncorrelated 
Substituting the above expressions in (83) we obtain 
R(w) = x + CxyCyYlo, - j )  + C,,C,’(z - 2) = $(y) + R(z) - x, 
and (81) is proved. The proof of (82) is similar by using the relations above and (69). Q.E.D. 
166 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Corollary A.3.6 Let z be as in the previous corollary and assume that y and z are not necessary uncorrelated, i.e., we may have 
c, = xiy = E {(y - J)(z - Z)l} # 0. 
Y. 
Then 
where A[z - I(y)] denotes the linear least-squares estimate of x given the random vector [z - 2(y)] and 2(y) is the linear least-squares estimate of z 
given y. Furthermore, 
E { [ z  - e(y)] [ Z  - 2(y)]'} E {[z - ~(Y)](x - x)'}. (85) 
[y.z I '  x, Y .  2 
Proof By Corollary A.3.2 the random vectors y and [z - 2(y)] are 
uncorrelated. Given this observation the result follows by application of the previous corollary. Q.E.D. 
Frequently one is faced with a situation whereby he wishes to estimate a vector of parameters x E R" given a measurement vector z E R" of the form 
z = c x  + u, 
where C is a given rn x n matrix and u E R" is a random measurement error vector. The (a priori) probability distribution of x and u is given. The following corollary gives the linear least-squares estimate A(z) and its error covariance. 
Corollary A.3.7 Let z, x, u, C be as above and assume that x and u are uncorrelated. Denote 
E{X} = x, E{u}  = 6, 
E{(X - X)(x - X)'} = ex,, E{(u - fi)(u - fi)'} = z,, 
and assume further that C,, is a positive definite matrix. Then 
A(z) = x + zx,c'(ccxxc' + xu,)- ' ( z  - cx - fi), E {[x - A(z)] [x - R(z)]'} = c, - zxxc'(ccxxc' + xu,)- 'CC,,. 
x. u 
APPENDIX LEAST-SQUARES ESTIMATION-THE KALMAN FILTER 167 
Proof Define y = [x', 0'1' E R"+m, C = [C,  I ] ,  j = [ j z ' ,  33' .  Then we have z = C y  and by Corollary A.3.3 
-w = [ I ,  019(z), 
E { C X  - W l  cx - W l ' l  = [ I ,  01 E{LY - fl4l LY - 9 ( Z ) l ' l  > [:I 
where j ( z )  is the linear least-squares estimate of y given z .  By applying Corol- lary A.3.4 with u = 0 and x = y we have 
9(z) = j + c y y C ' ( C x , " y c ) - ~ ( z  - C j ) ,  
E { b  - j ( z ) ] b  - jqz)]'} = Zyy - c,,c(Cc,,P)-'Cx:,,. 
By using the equations 
and C = [C, I ]  above and carrying out the straightforward calculation the result follows. Q.E.D. 
A.3 State Estimation of Discrete-Time Dynamic Systems -The Kalman Filter 
Consider now a linear dynamic system of the type considered in Section 4.3 but without a control vector (uk = 0) 
xk+l = AkXk + wk, k = 0, 1, ..., N - 1, (86) 
where xk E R", wk E R" denote the state and random disturbance vectors, respectively, and the matrices Ak are known (nonrandom). Consider also the measurement equation 
z k  = CkXk + u k ,  k = 0, 1,. . ., N - 1, (87) 
where z k  E R", u k  E R" are the observation and observation noise vectors, respectively. 
We assume that x o ,  w o ,  w l , .  . . , w , , , - ~ ,  u o , .  . ., v N - l  are mutually in- 
dependent random vectors with given probability distributions. Furthermore, they have zero mean and finite second moments, i.e., 
E { X o )  = E { W k }  = E{uk} = 0, k = 0, 1,. . . , N - 1. (88) 
We use the notation 
s = E { x o x b } ,  Mk = E { W k W ; } ,  Nk = E { V k U b } ,  (89) 
and we shall assume that N k  is a positive definite matrix for every k. 
168 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
a k - 1  = 
- - C O  0 C l L O  0 
7 
C k - 1 L k - 2  
. . C k L k - l  2 
Consider now the problem of finding the linear least-squares estimate of the random vectors x k +  or xk given the values ofz,, z l ,  . . . , z k ,  or equivalently 
given the random vector Z k  = [zb,  . . . , 261‘ E R(k+l)s .  Let us denote these 
estimates R k +  1Ik and 2 k I k ,  respectively. 
It is possible to provide with very little effort an equation for 2,‘lk by using the results already obtained. Indeed let us denote for each k 
For each i with 0 Q i Q k we have, by using the system equation, 
xk+ 1 = Liri, 
Li = [Ai . . . A , ,  Ai * * * A l ,  . . . , Ai, 13. 
where Li is the n x [n(i + l)] matrix 
As a result we may write 
Z k  = m k - l r k - 1  + &, where @ k -  is an [s(k + l)] x (nk) matrix defined by 
where the zero matrices above have appropriate dimension. Thus the problem has been reformulated in such a way that we may use Corollary A.3.7, the equations above, and the data of the problem to compute 
? k - l ( Z k )  and E ( c r k - 1  - 3 k - 1 ( Z k ) l C r k - l  - P k - l ( Z k ) l ’ ) -  
Subsequently we can obtain jZklk = a k ( z k )  as well as the corresponding error covariance matrix by using Corollary A.3.3, i.e., 
2klk = L k -  1 3 k -  l ( z k ) ,  
E { C ( X k  - 2 k J k ) ( X k  - ? k l k ) l )  
= L k - l E { [ r k - l  - 3 k - 1 ( Z k ) l [ r k - l  - 3 k - 1 ( Z k ) ] ’ ) L k - l -  
These equations may in turn be used to yield j l k +  11,‘ and an equation for the corresponding error covariance by again using Corollary A.3.3. 
The conclusion from the above analysis is that one can provide in a straightforward manner equations for the least-squares estimate of the state x k  and the corresponding error covariance by using the results already 
APPENDIX LEAST-SQUARES ESTIMATION-THE KALMAN FILTER 169 
obtained earlier. However, these equations are very cumbersome to use when the number of measurements is large. Fortunately enough the se- quential structure of the problem can be effectively exploited and the com- putations can be organized in a very convenient manner. The corresponding algorithm was originally proposed in the form given here by Kalman [Kl] although related ideas were known much earlier. The main attractive feature of the Kalman filtering algorithm is that the estimate 2k+ Ik can be obtained by means of a simple equation that involves the previous estimate 2klk-l and the new measurement zk but does not involve any of the past measurements z o ,  z l ,  . . . , zk-  1. In this way significant data reduction is achieved. We now 
proceed to derive the form of the algorithm. 
Suppose that we have computed the estimate ' k l k - l  together with the covariance matrix 
At time k we receive the additional measurement 
zk = CkXk + vk. 
We may use now Corollary A.3.6 to compute the linear least-squares estimate of xk given Z k -  = [zb,  z; ,  . . . , z;-  1] '  and z k .  This estimate is denoted gkIk 
and, by Corollary A.3.6, it is given by 
where &(Zk- 1) denotes the linear least-squares estimate of zk given Z k -  and 
Ak[zk - &.(Zk-1)] denotes the linear least-squares estimate of xk given [zk - 2k(Zk- l)]. Now we have by (86)-(89) and Corollary A.3.3, 
Also to calculate a k [ z k  - &(&- we use Corollary A.3.3 to obtain 
(93) 
The last term on the right above is zero by Corollary A.3.2 so that using (90) we have 
(94) 
170 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Using expressions (92)-(94) in Proposition A.3, we obtain 
$kCzk - 2 k ( z k - l ) l  = c k I k - l c ; ( c k z k I k - l c ;  + N k ) - l ( Z k  - C k 2 k l k - 1 ) ,  
and (91) is written 
9klk  = 2 k l k - l  + z k l k - l C ; ( C k C k l k - l C ;  + N k ) - l ( Z k  - c k 2 k l k - l ) .  a (95) 
By using Corollary A.3.3 we also have 
D ' k + l l k  = A k 2 k l k .  4 (96) 
Concerning the covariance matrix &+ I l k  we have from the system equation (86) and (88), (89), and Corollary A.3.3: 
D C k + l l k  = A k z k l k A ;  + M k .  a (97) 
where 
' k l k  = E { ( X k  - 2 k l k ) ( x k  - 9klk) '} .  
Now the error covariance matrix &lk may be computed via Corollary A.3.6 similarly as 2 k l k  [cf. Eq. (91)]. We have from (85), (93), and (94) that 
E- ckIk = x k l k - l  - C k ( k - l C ; ( C k x k l k - l C ;  + N k ) - l C k C k l k - l .  a (98) 
D = 0, C0l-l = s, 4 (99) 
Equations (95)-(98) with the initial conditions [cf. Eqs. (88) and (89)] 
constitute the Kalmanjltering algorithm. This algorithm recursively generates the linear least-squares estimates 2 k +  1 Ik or R k I k  together with the associated error covariance matrices &+ 1 Ik or &lk.  
An alternative expression for Eq. (95) is 
2klk = A k - 1 2 k - l ( k - l  + x k l k C ; N ; l ( Z k  - C k A k - 1 2 k - I l k - 1 ) .  a (100) 
This expression is obtained from (95) and (96) by using the equality 
C k I k C k N ; '  = c k I k - l c ; ( C k c k I k - l C k  + N k ) - ' .  
This equality may be verified by using (98) to write 
C k I k C ; N ; l  = c C k I k -  1 - z k l k -  l C ; ( C k Z k l k -  lc; + N k ) - l C k C k l k -  llc;N;l 
= x k l k - l C ; [ N k l  - ( C k E k l k - 1 C ;  + N k ) - l C k x k l k - l C ; N ; l ]  
= x k l k -  l C b ( C k C k l k -  lc;  + N k ) -  ' 9  
where the last step follows by writing 
N;' = ( C k X k l k - l C ;  + N k ) - l ( C k x k l k - l C b  + N k ) N ; '  
= ( C k C k l k - 1 C ;  + N k ) - l ( C k z ; k J k - l C ; N ; l  + 1). 
APPENDIX LEAST-SQUARES ESTIMATION -THE KALMAN FILTER 171 
When the system equation contains a control vector uk and has the form 
xk+l = AkXk + BkUk + W k ,  k = 0, 1 , .  . . , N - 1 ,  
and we seek the linear least-squares estimate gklk of xk given zo,  z l , .  . . , zk and uo,  ul,. . . uk- it is easy to show that (100) takes the form 
2klk = A k -  l g k -  I l k -  1 + B k -  I U k -  1 
+ ZklkC;N;l(Zk - CkAk-]2k-] lk- l  - CkBk-1Uk-l). 
Equations (97)-(99) generating CkIk remain unchanged. Also if the mean of the initial state is nonzero, then the initial conditions (99) take the form 
201-1 = E I x , } ,  Cq-1 = s. 
Finally we note that (97) and (98) yield 
C k +  I l k  = A k [ C k I k -  1 - C k l k -  lC;(CkZklk- lc; + Nk)-’CkCklk- 11A; + M k ,  
(101) 
with the initial condition CoI - = S .  
in Section 3.1. Thus when A, ,  ck, N k r  and M k  are constant matrices Equation (101) is a discrete-matrix Riccati equation of the type considered 
A k = A ,  ck=c, N k = N ,  M k = M ,  k = 0 , 1 ,  ..., N -  1, 
we have, by invoking the proposition proved there, that the solution of (101) tends to a positive definite matrix C provided appropriate controllability and observability conditions hold. The conditions required are observability of the pair ( A ,  C) and controllability of the pair (A,  D), where M = DD‘. When k is large one may approximate the matrix in (1 10) by the con- stant matrix C to which converges as k -+ co. We have from (98) 
C = C - CC’(CCC’ + N ) - ’ C C ,  
and we may write (100) as 
2 k l k  = Agk-llk-1 + C C ” - ’ ( Z k  - CA2k-llk-1). (102) 
Since the “gain” matrix (CC‘N-  I )  multiplying the “correction” term 
is independent of the index k, the implementation of the (zk - C A 2 k - , I , -  
estimator (102) is considerably simplified. 
A.4 Stability Aspects of the “Steady-Scare” Kalman Filtering Algorithm 
Let us consider now the stationary form of the Kalman filtering equations (95) and (96): 
t k + , I k  = AgkIk- 1 + ACC’(CCC’ + N)-’(zk - CgkIk- 1). (103) 
172 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
By using Eq. (103), the system equation 
xk+l  = A X k  + wk, 
and the measurement equation 
zk = cxk + V k ,  
we obtain 
e k + l  = [ A  - Axc‘ (Czc ’  + N)-’C]ek  + wk - A x c ’ ( c x c ’  + N ) - l U k ,  
(104) 
where e k  denotes for all k the “one-step prediction” error 
e k  = x k  - A k l k -  1. 
From the practical point of view it is important that the error equation (104) represents a stable system, i.e., the matrix 
A - AZC’(CCC’ + N)- ’C  (105) 
is a stable matrix. This fact, however, is guaranteed under the observability and controllability assumptions given earlier since X is the unique positive semidefinite symmetric solution of the algebraic Riccati equation 
x = A[x - xc’ (Cxc’  + N)- ’Cx]A‘  + M 
by the proposition proved in Section 3.1. Actually this proposition yields that the transpose of the matrix (105) is a stable matrix. This is, however, equivalent to the matrix (105) being a stable matrix, since for any matrix D 
we have Dk + 0 if and only if Drk + 0. 
Having established the stability properties of the error equation (104) we now proceed to examine the stability properties of the equation governing the estimation error 
S?k = x k  - A k l k .  
We have by a straightforward calculation 
e“k = [ I  - c@(cxe + N)-’C]ek - x@(cx@ + N ) - ’ U k .  (106) 
By multiplying both sides of Eq. (104) by [I - CC(CCC’ + N ) - ’ C ]  and 
using (106) we obtain 
t?k+l + x:@(cxc’ + N ) - l U k + l  
= [ A  - xc’(cxc + N)-’CA][S?k + xc‘(ccc’ + N ) - l U k ]  
+ [ I  - xc‘(cxe + N ) - ’ c ] [ w k  - AxC‘(CcC’ + N)- ’uk] ,  
APPENDIX LEAST-SQUARES ESTIMATION -THE KALMAN FILTER 173 
or equivalently 
i ? k + l  = [A - cc'(cc@ + N)-'CA]Ek 
+ [ I  - cc'(ccc' + N)-'C]w& - cc(ccc' + N)-'Uk+l. (107) 
The stability of matrix (105) guarantees that the sequence {ek}  generated by (104) tends to zero whenever the vectors wk and uk are identically zero for all k. Hence, by (106), the same is true for the sequence {zk}. It follows from (107) that the matrix 
A - ec'(ccc' + N ) - ' C A  (108) 
is stable and hence the estimation error sequence {i?,} is generated by a stable equation. 
Let us consider now the stability properties of the 2n-dimensional system of equations with state vector [xi, A:]': 
(109) 
A k + l  = zcN-'CAXk ( A  BL - %'N-'CA)Ak. (1 10) 
xk+ 1 = AX, + BLAk, 
This system was encountered at the end of Section 4.3. 
assumptions stated there are in effect. By using the equation We shall assume that the appropriate observability and controllability 
m N - '  = zc'(ccc + N ) - ' ,  
shown earlier, we obtain from (109) and (1 10) that 
(xk+ 1 - A k +  1) = [A - ZC(CCC' + N ) -  'CAI (Xk - A&). 
In view of the stability of matrix (108) it follows that 
lim(xk+l - A k + l )  = 0, (111) 
k-w 
for arbitrary initial states x, and A. . From (109) we obtain 
X k +  1 = ( A  + BL)Xk + BL(Ak - Xk). (112) 
Since in accordance with the theory of Sections 3.1 and 4.3 the matrix (A + BL) is a stable matrix, it follows from (1 11) and (1 12) that we have 
lim xk = 0, k+W 
and hence by (1 1 l), 
lim Ak = 0. k+m 
174 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
Since the equations above hold for any initial states xo and 2,, it follows that the system of equations (109) and (1 10) is a stable system, i.e., the matrix 
1 A B L  
% ' N - ' C A  A + BL - % Z ' N - ' C A  
is a stable matrix. 
A S  Purely Linear Least-Squares Estimators 
Consider two jointly distributed random vectors x and y taking values in R" and R", respectively, as in Sections A . l  and A.2. Let us restrict attention to estimators of the form 
X ( Y )  = AY, 
which are purely linear (rather than linear plus constant). Similarly, as in Section A.2 we consider the problem of finding the optimal least-squares estimator within this restricted class, i.e., an estimator of the form 
2 ( y )  = A y  
f ( A )  = E {Ilx - Ay1l2) 
where A^ minimizes 
x. Y 
over all n x m matrices A .  We refer to such an estimator as a purely linear least-squares estimator. The derivation of the form of this estimator is very similar to the one of Section A.2. 
By setting the derivative offwith respect to A equal to zero, we obtain 
0 = af/aAlz  = 2 E {y(Ay  - xy}, 
d = S,,S,', 
x. Y 
from which 
where 
s,, = E { X Y ' } ,  s,, = E {YY'I,  
and we assume that S,, is invertible. The purely linear least-squares estimator takes the form 
%4 = S,,S,'Y. (113) 
(1 14) 
The second moments of the corresponding error are given by 
E {CX - Wl cx - 2(y ) ] ' }  = s,, - sx,s,'~Y,. 
x. Y 
This equation is derived in an entirely similar manner as in Section A.2. 
APPENDIX LEAST-SQUARES ESTIMATION-THE KALMAN FILTER 175 
An advantage of the purely linear estimator is that it does not require knowledge of the means of x and y .  We only need to know the joint and individual second moments of x and y .  A price paid for this convenience, however, is that the purely linear estimator yields in general biased estimates, i.e., we may have 
E@(Y)} z E{X} .  By contrast, in the linear least-squares estimator examined earlier, we always have E { i ( y ) }  = E {x} (cf. Corollary A.3.1). 
As a final remark, we note that from Eqs. (629, (69) and (1 13), (1 14) it can be seen that the equations characterizing the purely linear estimator may be obtained from those of the linear estimator by setting X = 0 , J  = 0 and writing S,, and S,, in place of C,, and C,,. As a result it is easy to see that there is an analog for the Kalman filtering algorithm corresponding to a purely linear least-squares estimator that is identical to the one described by Eqs. (95)-(99) and remains the same even if we do  not assume that 
E{x, }  = E { w k }  = E(uk} = 0, k = 0, 1,. . . , 
provided that all given covariance matrices are replaced by the corresponding matrices of second moments. 
A.6 Least-Squares Unbiased (Gauss-Markou) Estimators 
means of the equation Let us assume that two random vectors x E R" and z E R" are related by 
z = cx + u, (1 15) 
where C is a given m x n matrix and u a random measurement error vector uncorrelated with x, having known mean and covariance matrix 
(1 16) 
The vector z represents known measurements from which we wish to estimate the vector x. If the a priori probability distribution of x is known then we may obtain a linear least-squares estimate of x given z by using the theory of Section A.2 (cf. Corollary A.3.7). In many cases, however, the probability distribution of x is entirely unknown. In such cases it is possible to use the Gauss-Markov estimator, which we now describe. 
E{u} = 6, E{(u - E)(u - e)'} = zuu. 
Let us restrict attention to estimators of the form 
x ( z )  = A(z  - fi), 
?(z)  = A(z - I?), 
and seek an estimator of the form 
176 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
where A^ minimizes 
over all n x rn matrices A. We have from (1 15)-(117) and the fact that x and u are uncorrelated, 
f ( A )  = E { I ~ x  - ACX - A(u - i j ) 1 I 2 }  
x. u 
= E{II(I - AC)xJI2} + E{(u - U)’A’A(u - ij)}, 
X U 
where I is the n x n identity matrix. Sincef(A) depends on the unknown statistics of x, we see that the optimal matrix A  ̂ will also depend on these statistics. We can circumvent this difficulty, however, by requiring that 
AC = I .  
Then our problem becomes 
minimize subject to AC = I .  (1 18) 
E{(u - ij)’A’A(u - ij)} 
Notice that the requirement A C  = 1 is equivalent to requiring that the estimator x(z)  = A(z - e) be unbiased in the sense that 
E{x(z)} = E{x} = X VZER”. 
This can be seen by writing 
E{x(z ) }  = E {A(Cx + u - C)} = A C E  {x} = ACZ = x. 
There remains the task of solving problem (1 18). Let a: denote the ith row of A. We have 
n n 
= 1 (u  - ij)’aia:(u - ij) = 1 a:(u - ij)(u - ijyai 
i =  1 i =  1 
Hence, problem (1 18) can also be written n 
minimize C a:Cuuai 
subject to C‘ai = ei ,  
i =  1 
i = 1,. . . , n, 
APPENDIX LEAST-SQUARES ESTIMATION -THE KALMAN FILTER 177 
where ei is the ith column of the identity matrix. The minimization can be carried out separately for each i, yielding 
iii = C"ilC(C'C,i'C)-'ei, i = I ,  ..., n, and finally 
A = (c 'C;1c)-1cX;l ,  
where we assume that the inverses of C,, and C'C,'C exist. Thus, the Gauss-Markov estimator is given by 
i ( z )  = (C'Xu;lc)- 1cCU;1(z - a). ( 1  19) 
Let us also calculate the corresponding error covariance matrix. We have 
E { [ x  - i ( z ) ]  [x - i ( Z ) ] ' }  = E { [ x  - A(z - a)]  [x - A(z - f i ) ] ' }  
= E{A(u - O)(u - fi)'A'} = ,-&,,"A' 
= (C'Cu;l C )  - c'C;"lC,, C ; T (  C'Ci"1C) - ', 
and finally E { [ x  - i ( z ) ]  [x - i ( z ) ] ' }  = (c'C,'c)- l .  ( 120) 
Finally, let us compare the Gauss-Markov estimator with the linear least-squares estimator of Corollary A.3.7. Whenever C,, is invertible the estimator of Corollary A.3.7 can also be written 
(121) This fact may be verified by straightforward calculation. By comparing Eqs. (119) and (121) we see that the Gauss-Markov estimator is obtained from the linear least-squares estimator by setting Z = 0 and C;: = 0, i.e., a zero mean and infinite covariance for the unknown random variable x. In this manner, the Gauss-Markov estimator may be viewed as a limiting form of the linear least-squares estimator. The error covariance matrix (120) of the Gauss-Markov estimator can also be obtained in the same manner from the error covariance matrix of the linear least-squares estimator. 
2(z)  = x + (C,;' + c'C,'c)- lC'X;l(z - cx - a). 
A.7 Deterministic Least-Squares Estimation 
x E R", z E R", and u E R" related by means of the equation As in the case of Gauss-Markov estimation, let us consider vectors 
z = c x  + u, 
where C is a known m x n matrix. The vector z represents known measure- ments from which we wish to estimate the vector x. However, we know nothing about the probability distribution of x and u and we are thus unable to 
178 4 PROBLEMS WITH IMPERFECT STATE INFORMATION 
utilize an estimator based on statistical considerations. Under these cir- cumstances it is reasonable to select as our estimate the vector 2 that mini- mizes 
f(x) = IIZ - Cxll', 
i.e., the estimate that fits best the data in a least-squares sense. This estimate will, of course, depend on z and will be denoted 2(z). 
By setting the gradient offat 2(z) equal to zero, we obtain 
Vf I*(=) = 2C"C2(z) - z] = 0, 
from which 
2(z) = (c'c)-'c'z, (1 22) 
provided C'C is an invertible matrix. An interesting observation is that the estimate (122) is the same as the 
Gauss-Markov estimate given by (1 19) provided the measurement error has zero mean and covariance matrix equal to the identity matrix, i.e., V = 0, 
C,, = 1. In fact, if instead of llz - Cx)I ' we minimize 
(z - v - cxyC;"'(z - v - CX), 
then the deterministic least-squares estimate obtained would be identical 
to the Gauss-Markov estimate. If instead of llz - CxII' we minimize 
(x - EyC;;(x - X) + (z - V - CxyC,'(z - 0 - CX), 
then the estimate obtained would be identical to the linear least-squares estimate given by (121). Thus, we arrive at the interesting conclusion that the estimators obtained earlier on the basis of a stochastic optimization frame- work can also be obtained by minimization of a deterministic measure of fitness of estimated parameters to the data at hand. 
Chapter 5 
Computational Aspects of Dynamic Programming- Suboptimal Control 
5.1 The Curse of Dimensionality 
Consider the DP  algorithm for the basic problem 
J N ( X N )  = g N ( X N )  
As we have seen earlier it is possible in some cases of interest to obtain a closed-form solution to this algorithm or at least use the algorithm for the analysis of properties of the optimal policy. However, such cases tend to be the exception rather than the rule. In most cases it is necessary to solve numerically the DP  equations in order to obtain an optimal policy. The computational requirements for doing so are often staggering to the point that for many problems a complete solution of the problem by DP is un- thinkable at least with presently existing computers. The reason lies in what Bellman has called the “curse of dimensionality,” which arises particularly when the state space is an infinite set. Consider, for example, a problem in which the state space is R” and the control space R”. In order to obtain the 
179 
180 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
function J N -  1 ( x N -  1) it is necessary first to discretize the state space. Taking, for example, 100 discretization points per axis results in a grid with 100” points. For each of those points now, the minimization of the right-hand side of (2) must be carried out numerically. Each minimization is carried over uk(xk) or over a grid of points covering uk(xk)-a nontrivial problem. Matters are further complicated by the requirement to carry out a numerical integration (the expectation operation) every time the function under mini- mization is evaluated, and by the possible presence of nondifferentiabilities introduced by discretization and interpolation. Computer storage also presents an acute problem. Thus for problems with Euclidean state and control spaces, D P  can be applied only if the dimension of these spaces is very small. When the control space is one-dimensional, things are sometimes greatly simplified, since in this case effective one-dimensional minimization tech- niques such as the Fibonacci search [LlO] may be used. Often the special structure of the problem can also be exploited to reduce the computational requirements. In other cases special computational algorithms can be used that take advantage of the particular features of the problem. This is particu- larly true of infinite-horizon problems. 
Various devices have been suggested to help overcome the computational and storage problem, particularly for deterministic problems, such as the so-called coarse grid approach, the use of Lagrange multipliers, Legendre polynomial approximations, and specialized techniques [B4, K6, L2, L9, N2, WlO]. These devices, though helpful for some problems, should be considered only as partial remedies, and in any case it is not our intention to discuss them at any length in this text. Instead we shall provide in the next section a simple discretization procedure for problems where an infinite state space is involved and we shall prove the validity of this procedure under certain reasonable assumptions. Subsequently we shall discuss various techniques for obtaining suboptimal control laws that are computationally efficient and hence of interest from a practical point of view. 
5.2 Discretization Procedures and Their Convergence 
In this section we consider a procedure for discretizing a DP  algorithm defined over an infinite state space. The procedure is not necessarily the most efficient computationally. It is, however, used widely (perhaps with slight modifications) and is simple and straightfoward. The basic idea is to approxi- mate the “cost-to-go” functions of the D P  algorithm as well as the corresponding policies by piecewise constant functions. We consider problems where the state spaces are compact subsets of Euclidean spaces and we introduce certain continuity, compactness, and Lipschitz assumptions. Under these assump- tions the discretization procedure is shown to be stable in the sense that it 
5.2 DISCRETIZATION PROCEDURES AND THEIR CONVERGENCE 181 
yields suboptimal policies whose performance approximates arbitrarily closely the optimal as the discretization grids become finer and finer. The analysis and proofs are straightforward but rather tedious and may be skipped by the less mathematically inclined or otherwise uninterested reader. 
Consider the following DP algorithm: J N ( X )  = g N ( X ) ,  X E S N  c RsN (3) 
X E S k c R S k ,  k = 0 , 1 ,  ..., N -  1 .  (4) 
This algorithm is associated with the basic problem with perfect state information involving the discrete-time dynamic system 
( 5 )  x k +  1 = f k ( X k r  uk, wk),  k = 0, 1 , .  9 * 9 N - 1, 
with given initial state x o  and the cost functional 
I N -  1 
{ k = O  
E g N ( X N )  + g k ( X k ?  u k ,  wk)  . 
For the purpose of analytical convenience we are considering here maximiza- tion of the objective function rather than minimization. This, of course, does not affect the discretization procedures or the convergence results to be obtained. In the above equations the system state X k  is an element of a Euclidean space RSk, k = 0, 1 , .  . . , N .  Algorithm (3) and (4) is defined over 
given compact subsets S k  c Rsk, k = 0, 1 ,  . . . , N - 1 .  The control input u k  
is an element of some space c k ,  k = 0,1, . . . , N - 1. In what follows we shall 
assume that C k  is either a subset of a Euclidean space or a finite set. 
The input disturbance w k  is assumed to be an element of a set w k ,  k = 0, 1, 
. . . , N - 1. We assume for simplicity that each set w k  has ajni te  number (say 
I k )  of elements. This assumption is valid in many problems of interest, most notably in deterministic problems where the set w k  consists of a single ele- ment. In problems where the sets w k  are infinite, our assumption amounts to replacing the DP algorithm (3) and (4) by another algorithm whereby the expected value (integral) in Eq. (4) is approximated by a finite sum. For most problems of interest this finite sum approximation may be justified in the sense that the resulting error can be made arbitrarily small by taking a sufficiently large number of terms in the finite sum. The reader may also provide similar assumptions as the one made here under which the approximation is valid in the above sense and extend the result of this section to cases where w k  are compact sets in Euclidean spaces. We shall denote the probabilities of the elements of W, by p : ( X k ,  u k ) ,  i = 1 ,  . . . , I k .  
We shall consider two different sets of assumptions in addition to those already made. In the first set of assumptions the control space C k  is assumed 
182 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
to be a finite set for each k. In the second set of assumptions the control space Ck is assumed to be a Euclidean space in which case discretization of both the state space and the control space is required. The reader may easily extend our analysis and results to cases where the control space is the union or the Cartesian product of a finite set and a Euclidean space. 
Assumptions A 
A.1 The control spaces ck, k = 0, 1, . . . , N - 1, are finite sets and 
u k ( x )  = Ck V X  E s k ,  k = 0, 1 , .  . . , N - 1. (6) 
A.2 The functionsf, and g k  satisfy the following conditions: 
u, w, - f , ( x ’ ,  u, w)ll < Lkllx - x’ll v x ,  X ’ E S k ,  u E C k ,  
W E W k ,  k = 0 , 1 ,  ..., N - 1 ,  (7) 
I g k ( X , U , W ) - g k ( X ’ , U , W ) I  < Mkllx-x’ll v X , X ’ E S k ,  u E C k ,  
W E W k ,  k = 0 , 1 ,  ..., N - 1 ,  (8) 
1 g N ( X )  - g N ( X ’ )  I M N  Ilx - X’II v x ,  x’ E S N  3 (9) 
where MN, M k ,  Lk, k = 0, 1,. . . , N - 1 are some positive constants and 
11 - 11 denotes the usual Euclidean norm. 
A.3 The probabilities p i ( &  u), i = 1 , 2 , .  . . , I , ,  of the elements of the finite set wk = { 1,2, . . . , I , }  satisfy the condition 
( p i ( x ,  u)  - p i ( x ’ ,  u)l < N k ( l X  - X’II v x ,  x’ E s k ,  E ck, i E w, 
k = 0 , 1 ,  ..., N - 1 ,  (10) 
where N k ,  k = 0, . . . , N - 1, are some positive constants. (This assumption 
is satisfied in particular if the probabilities p: do not depend on the state.) Assumptions B 
B.1 The control space ck, k = 0, 1, . . . , N - 1, is a compact subset of a 
Euclidean space. The sets u k ( x )  are compact for every x E S k ,  and in addition the set 
uk = u u k ( X ) ,  k = 0, 1,. . ., N - 1, (11) 
XSSk 
is compact. Furthermore, the sets u k ( x )  satisfy 
u k ( x )  u k ( x ‘ )  + {ul l l u l l  < pkllx - x ’ l l >  v& X f E S k ,  
k=0, 1 ,..., N - 1, (12) 
where Pk are some positive constants.? 
t The advanced reader may verify that (12) is equivalent to assuming that the point-to-set map x + U,(x)  is Lipschitz continuous in the Hausdorff metric sense. 
5.2  DISCRETIZATION PROCEDURES AND THEIR CONVERGENCE 183 
B.2 The functionsf,, g k  satisfy the following conditions: 
I I fk(& u, w )  - f k ( x ’ ,  u’, w ) l l  < L k ( l l x  - X‘II + IIu - u’ll) vx? x’ E S k r  
U , u ‘ E U k ,  W E W k ,  k = 0, 1 ,..., N - 1, (13) 
I g k ( X ,  u, w )  - g k ( X ’ ,  u‘, w ) l  < m k ( l l x  - X’II + IIu - u’ll) vx, X ’ E  s k ,  
U , U ’ E U k ,  W E W k ,  k = 0, 1 ,..., N - 1, (14) 
I g N ( X )  - gN(X’ ) I  < mNIlx - X’II vx, x’ E SN, (15) 
where mN, m k ,  z k ,  k = 0, 1, . . . , N - 1, are some positive constants. 
finite set w k  = { 1 , 2 ,  . . . , I , }  satisfy the condition 
B.3 The probabilities p i ( x ,  u), i = 1 , .  . . , I , ,  of the elements of the 
I p : ( x ,  u)  - p L ( x ’ ,  u‘)l < w k ( l l x  - x’)I + IIu - U’II) vx,  x’ E S k r  
U , U ’ E U k ,  i E W k ,  k = 0 , 1 ,  ..., N -  1, (16) 
where m k ,  k = 0, 1, . . . , N - 1, are some positive constants. 
Prior to considering discretization of the dynamic programming algorithm 
we establish the following property of the “cost-to-go” functions Jk: S k  + R 
of (3) and (4). 
Proposition 1 Under Assumptions A or B the functions J k :  S k  -+ R, given by (3) and (4) satisfy 
I J k ( X )  - J k ( X ‘ ) I  < A k l l X  - X’I( V x , x ‘ E S k ,  k = 0, 1,. .., N ,  (17) 
where Ak,  k = 0, 1, . . . , N ,  are some positive constants. 
with AN = M N .  For k = N - 1 we have that for each x ,  x’ E S,- 1 ,  
Proof Under Assumptions A we have by (9) that (17) holds for k = N 
I J N -  1 ( x )  - J N - l ( x ‘ ) l  
I N - I  
max 1 { g N -  1 ( x ,  u, i) + J N C f N -  1 ( x ,  u, i)]}pk- 1 ( x ,  u )  = I  U E C N - I  i = l  
184 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
Now we use the fact that if a: S -P R, p: S + R are real-valued functions over 
a compact subset S of a Euclidean space satisfying for some constants p a ,  pP,  and all t l ,  f2 E S, 
la(t1) - a(t2)l G P a l l t l  - t 2 I L  Iml) - B(t2)l G PPlltl - t 2 I L  
then the product function a( - )/?( - ) satisfies for all t , ,  t2 E S 
Ia(tl)P(tl) - a(t2)P(t2)1 G P z  max I m l  + Pp max IWl Il l1 - t2II. (18) [ t s s  t € S  1 
Then the earlier estimate is strengthened to yield 
I J N - l ( x )  - JN- l (X‘ ) I  < A N - I l l x  - X’II V x - x ’ E S N - l r  
where AN- is given by A N - 1  = I N - 1 ( M N - 1  + L N - l A N  + B N - l N N - l ) ,  
B N -  1 = max{ I g N -  1(x, u, w ) l l x  SN- 1, C N -  1, WN- 1 } 
+ max{IJNCfN-l(X,U,W)lIIXESN-l,UECN-l, W E  W N - I } .  
Thus the result is proved fork = N - 1 and similarly it is proved for every k. 
We turn now to proving the result under Assumptions B. Again the result 
holds fork = N with AN = RN. Fork = N - 1 we have for each x,x‘ E SN- 
l J N - l ( x )  - JN- l (X‘ ) I  
I N - l  
max 1 { g N -  1(x, u, i )  + JNCfN- 1(x, u, i)])pk- 1(x, u )  = I  UEUN-I(X) i = l  
Now using (18), B.2, B.3, and the above equality it is straightforward to show that 
IJN-  1(x) - JN-  l(x‘)l 
I N - l  
G 
- g N -  1(x’, u, ibk- 1(x’, u)] 
5.2 DISCRETIZATION PROCEDURES AND THEIR CONVERGENCE 185 
We now proceed to describe procedures for discretizing algorithm (3) and (4) under Assumptions A and B. 
Discretization Procedure under Assumptions A 
We partition each set S k  into nk mutually disjoint sets S:, S i ,  . . . , S;. 
such that Sk = Uz S:,  and select arbitrary points x i  E S i ,  i = 1, . . . , nk. 
We approximate the DP algorithm (3) and (4) by the following algorithm, which is defined on the finite grids Gk,  where 
Gk = {x;, X i ,  . . . , xik} ,  k = 0, 1 , .  . . , N .  (20) 
g N ( X )  if XEGN, (21) (22) 
(23) 
We have 
&(x) = {gN(xk) if x E S k ,  i = 1 ,2 , .  . . , n N ,  
if x E Gk,  max E {gk(x,  u, w )  + j k  + Cfk(x, u, w)I) U € C k  w 
jk(xi) if XES:,  i = 1,2 ,..., nk, k = 0, 1 ,..., N - 1.  (24) 
The algorithm above corresponds to computing the “cost-to-go ” functions j ,  on the finite grid by means of the DP algorithm (21) and (23), and extending their definition on the whole compact set S k  by making them constant on each section Si of S k  (see Fig. 5.1). Thus j k  may be viewed as a piecewise constant approximation of J k  . An alternative way of viewing the discretized algorithm (21) and (23) is to observe that it corresponds to a stochastic optimal control problem involving a certain finite state system (defined over the finite state spaces Go,  . . . , GN) and an appropriately reformulated cost functional. 
j k ( X )  = 
where 
Strengthening the above estimate and using (18) and our assumptions we obtain 
where 
and the result is proved for k = N - 1.  Similarly the result is proved under 
Assumptions B for all k .  Q.E.D. 
186 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
1 
I 
I I 
r iI I  I 
+ I  I I I 
I I I I I I I I I I I I 
I I I I 
I 
1 . 1  I - 1 ‘ -  I x, I X k  I 
I I I I I 
I I  2 1  I xx. ) tk -  I I vx.)’A I 
;c 
X . . .  
s, I s, 2 Skl lk  - ’ SkQ 
FIGURE 5.1 
Carrying out the DP algorithm (21)  and (23)  involves a finite number of operations. Simultaneously we obtain an optimal control law as a sequence 
Po(x), i i I ( X ) ,  . . . 9 P N -  1(x), 
of functions f i k  : Gk Ck : 
defined on the respective grids G k ,  k = 0, . . . , N - 1, where j&(X:) maximizes 
the right-hand side of (23)  when x = x : ,  i = 1 ,2 ,  . . . , nk.  We extend the definition of this control law over the whole state space by defining for every X E S k , k = 0 , 1 ,  ..., N -  1 ,  
pk(x) = /&(xi) if X E S : ,  i = I , .  . . , nk.  (25)  
Thus we obtain a piecewise constant control law { p o ,  pl, . . . , pN- defined over the whole space (see Fig. 5.2). The value of the cost functional corre- sponding to { p o ,  pl, . . . , pN- 1} is denoted Jo(xo)  and is obtained by the last 
step of the algorithm 
J N W  = S N ( X ) ,  x E S N  (26)  
XESk,  k = 0 , 1 ,  . . . ,  N - 1 .  (27)  
Jk(x) = J!? { g [ x ,  pk(x), w1 + j k  + I[.&(.u. p6(.‘). M’)l H’ 
Denote by d, the maximum “radius” of the sets S:: 
d, = max max su IIx - $ 1 1 .  
k = O , l ,  .... N i = l ,  ..., n k x e  B & 
5.2 DISCRETIZATION PROCEDURES AND THEIR CONVERGENCE 187 
!+(-xi , 
-. 
I- 
I n 1 I I 
f- . ' *  I I I I I I I 
7 1  
I 
I I 
I I I 
I 
H I 
i 
I I 
I I I I 
I I I x,- I I x,llX.- ' I x,", I 
s, I s,' Ly,"x - ' .y,II, 
1 - 1  * 
x . . .  
FIGURE 5.2 
We shall be interested in whether J^k and j ,  converge in some sense to J k  for each k as d,  tends to zero. 
Discretization Procedure under Assumptions B 
sumptions A. In addition, finite grids Hk of points in Uk are selected: Here the state spaces S k  are discretized in the same way as under As- 
Hk = { U : ,  ..., U p }  C u k ,  k = 0, 1,. . . , N - 1. (29) 
We assume that 
V , ( x : )  n H ,  # Vi  = 1 , .  . . , n k r  k = 0, 1 , .  . . , N - 1, (30) 
where 0 denotes the empty set. We now approximate algorithm (3) and (4), by 
the following algorithm: 
I N ( x !  if x E G N ,  (31) (32) 
j N ( X )  = g N ( X h )  if XES;, i = 1, .. . , n N ,  
max J? { g k ( X ,  u, w) f j k +  1 [ f k ( &  u, w)]} if x E Gk, (33) 
U€Uk(X)nHk W 
J^k(x;) if XES:, i = 1,2 ,..., n k ,  k = 0, 1 ,..., N - 1.  (34) 
Similarly as under Assumptions A we obtain a control law {Po,  . . . , P N -  defined on the grids G k ,  k = 0, 1, . . . , N - 1, that is extended over the whole 
state space to yield the control law {pol pl, . . . , pN- by means of the 
[. j k ( X )  = 
188 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
piecewise constant approximation (25). The corresponding value j ( x o )  of the cost functional is given by equations identical to (26) and (27). 
Again we are interested in the question whether s k  and j k  converge in some sense to Jk for each k as both d, and d, tend to zero, where 
d, = rnax max sug llx - xhll, (28‘) 
k=O. 1 ..... h’ i =  1 ..... n k  X E  k 
rl, = max max max min IIu-ii’11. (35) A=(). I . . . . . \ -  I i = 1 .  .... IIk U € u k ( X & )  U ’ E U k ( X i ) n H k  
This question is answered in the affirmative in the next proposition. 
There exist positive constants Y ~ ,  \jk. k = 0, 1. . . . , N 
(independent of the grids G o ,  . . . , G,, H,, . . . , H N -  used in the discretiza- 
tion procedure) such that under Assumptions A 
(36) 
Proposition 2 
I J k ( X )  - jk(x)l < U k d ,  
I J k ( X )  - j k ( x ) l  < U k d s  V X E S k ,  k = 0, 1 , .  . . , N ,  (37) 
V X  E s k ,  k = 0, 1, . . . , N ,  
and under Assumptions B 
l J k (X )  - s k ( X ) l  < &(d, + d,) 
I J k ( X )  - j k b )  I < &(ds + d,) 
V X  E s k ,  
V X  E s k ,  
k = 0, 1, . . . , N ,  
k = 0, 1 ,  . . . , N ,  
(38) 
(39) 
where J k ,  j k ,  j k r  d,, d, are given by (3) and (4), (21)-(24) [or (31)-(34)], (26) and (27), (28) and (35), respectively. 
Proof We first prove the proposition under Assumptions A. We have by (21) and (22) that JN(x) = j,(x) for all x E GN while for any x E Sk, 
I J N ( x )  - J ~ V ( X ) I  = I g d X )  - g N ( X k ) I  Q M,llx - xkll Q M N d , .  (40) 
Hence (36) holds for k = N with a, = M,. Also JN(x) = JN(x) Vx ES,, 
and hence (37) also holds for k = N. To prove (36) for k = N - 1 we have by 
(23) for any i = 1,2,  . . . , nN- 
5.2 DISCRETIZATION PROCEDURES AND THEIR CONVERGENCE I89 
where the last step follows by (40). Also for any x E S i -  l ,  i = I ,  . . . , t i N -  1, 
we have using (41) and Proposition I ,  
IJN-  1(x) - j N -  lWl 
= IJN-  1(x) - j N -  l h -  1) l  
< I J N -  1(x) - J N -  l ( 4 -  1 ) l  + IJN-  l b k -  1 )  - 1,- lbi- 1) l  
< A N - 1 1 1 ~  - xh- 111 + aNds < ( A N - 1  + aN)ds.  
Hence (36) holds for k = N - 1 with aN- = AN-  + aN, and similarly it is 
shown to hold for all k .  
To prove (37) fork = N - 1 let x E S i -  1. We have by (24) and the previous 
inequality. 
IJN-  1(x) - J N -  I (X)l  < I J N -  1(x) - j N -  l (X) l  + 1.L- l (X)  - 1,- l ( 4 l  
d ( A N -  1 + aN)d, + ljN-l(xL- 1 )  - J N -  I(x)l. (42) 
Fornotationalconveniencewe writepN- l(x) = pN- ,(xi- 1 )  = p i -  [cf.(25)]. By using (23), (27), and (1 8), we have 
I j N -  l b i -  1 )  - J N -  I (X) l  
I N - l  
,< 1 J~ gN- , ( x i -  A- l , j ) p i -  l ( x i -  1, A- 1)  
I N - I  
- 1 .qN- l(x, p i -  l , j ) p i -  l(x. p i -  1) 
+ 1 ' k l j N ~ ~ N -  l ( x i -  P i -  l , j ) ~ p i -  , ( x i -  P i -  1)  
- 1 J N [ f N -  l(x, A- l , j ) ~ p i -  l(x, p i -  1 )  
j =  1 
j =  1 
I N -  I 
j =  1 
IN- I 
w E WN- 1l)llx - x i -  111 + 1 c l b i -  1, P i -  l 7 . i ) l  
j =  1 
190 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
- max E {gN- I(&- 1, u, W) + J N C j N - i ( x k -  1, u, W)I> 
UEUN-I(X:-1)nHN-l W 
. 
  I    I  I  
From the above inequality, Proposition 1, (36), (37) as proved for k = N ,  and conditions A.2 and A.3, we easily obtain 
where dN is a positive scalar not depending on the grid G N -  1. Using the above inequality in (42), 
Thus (37) holds for k = N - 1 with aN- = A N -  + aN + SN. Similarly (37) 
is shown to hold for all k. 
We now turn to proving (38) and (39) under Assumptions B. Similarly, as in the case of Assumptions A, (38) and (39) hold for k = N with /?, = R,. 
To prove (38) for k = N - 1 we have by (33), for any i = 1,2,  . . . , nN- 
We use the triangle inequality and strengthen it further as in (41), obtaining 
where BN- is given by (19). The last step in the above algebra is obtained in a straightforward manner by using Assumptions B, Proposition 1, and the 
definition of d,. Also we have for any x E Sk- i = 1 , . . . , nN- 1, 
Using (43) we have that (38) holds for k = N - 1 with 
5.3 SUBOPTIMAL CONTROLLERS AND THE NOTION OF ADAPTIVITY 191 
Similarly (38) is shown to hold for all k. Once (38) is proved, (39) follows in exactly the same manner as under Assumptions A. Q.E.D. 
Proposition 2 demonstrates the validity (under mild continuity assump- tions) of discretization procedures based on piecewise constant approxima- tions of the functions obtained in the DP  algorithm. The bound on the ap- proximation error is proportional to the size of the discretization grid utilized and tends to zero as the grid becomes finer and finer. 
5.3 Suboptimal Controllers and the Notion of Adaptivity 
As discussed earlier, the numerical solution of many sequential opti- mization problems by DP  is computationally impractical or infeasible due to the dimensionality problem. For this reason in practice one is often forced to use a suboptimal policy that can be more easily calculated and imple- mented than the optimal policy and hopefully does not result in a substantial increase of the value of the cost functional over the optimal value. There are a number of suboptimal approaches for sequential optimization and it is quite difficult to classify and analyze them in a unified manner. For example, one obvious approach is to simplify or modify the model so that the DP  algorithm is either computationally feasible or possesses an analytical solution. Such simplifications include replacing nonlinear functions by linear and, perhaps, quadratic approximations, eliminating or aggregating certain variables in the model, neglecting small uncertainties and low-level correlations, etc. No general guidelines can be given for such an approach, and we will not be further concerned with it. On the other hand we shall discuss in the next two sections some approaches for suboptimal control that are of general ap- plicability and are often considered in practice. Some other techniques are referred to in the last section. We first define the notion of adaptiuity, which constitutes a desirable property for any suboptimal controller. 
Let us take as our basic model the problem with imperfect state informa- tion of Section 4.1. This problem includes as a special case the problem with perfect state information of Section 2.1 except for the fact that the control constraint set U k  is not state dependent (simply take the measurement equa- tion to be of the form z k  = x k  for all k) .  Now a good part of the difficulty in solving the problem by DP  can be attributed to the fact that exact or inexact measurements of the state are taken during the process, and the control inputs depend on these measurements. If no measurements were taken, the problem would be reduced to finding a sequence { u t ,  u:, . . . , u;E- such 
that u: E u k ,  k = 0, . . . , N - 1, which minimizes 
N- 1 
{ k = O  
g N ( X N )  + 1 g k ( x k ?  u k ,  wk)  J(u0,  u1, . . . , U N -  1) = E 
XO, W k  k = O ,  1, .... N-1 
192 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
subject to the constraints 
x k +  1 = f ( x k ,  u k ,  wk)- 
This is an essentially deterministic problem, which can be solved by deter- ministic optimization techniques. For example, if the state and control spaces are Euclidean, optimal control and mathematical programming methods can be efficiently used for solution of the problem. A control sequence {u:, u:, . . . , ug- 1} minimizing the cost functional (44) is called an optimal open-loop control sequence, and the optimal value JZ of the cost (44) is called the optimal open-loop value: 
J t  = inf J ( u O , U l , . . . , u N - l ) .  urelJ*. k = O ,  .... N -  1 
Now if J* denotes the optimal value of the basic problem with imperfect state information of Section 4.1 we have 
This is true simply because the class of controllers that do not take into account the measurements (consist of functions that take a single constant value independent of the current information vector) is a strict subset of the class of admissible controllers for the problem of Section 4.1. The difference 
(JZ - J*) can be called the value ofinformation supplied by the measurements. 
[When the cost functional includes directly costs for measurement, a more 
descriptive term for (JZ - J*) would be the value of the option of taking 
measurements.] The whole point for taking measurements (i.e., using feedback) is precisely to reduce the optimal cost from J:  to J*. Now it is evident that any suboptimal control law 71 = { p o ,  pl, . . . , p N -  1 }  that takes into account the 
measurements should be considered acceptable only if the corresponding value of the cost functional J ,  satisfies 
J* < J ,  < J: ,  (45) 
for otherwise the information supplied by the measurements is used with disadvantage rather than advantage. 
Definition An admissible control law 71 = { p o ,  p l ,  . . . , p N - l }  that satisfies (45) will be called quasi-adaptive. If the right-hand side of (45) is satisfied with strict inequality, the control law 71 will be called adaptive. 
In other words an adaptive controller is one that uses the measurements with advantage. Of course, an optimal controller for the problem is quasi- adaptive but some of the suboptimal controllers commonly used in practice are not in general quasi-adaptive. One such example is the so-called naive 
5.4 NAIVE FEEDBACK AND OPEN-LOOP FEEDBACK CONTROLLERS 1 93 
feedback controller, which will be examined in the next section. In the same section we shall examine another suboptimal control scheme, the so-called open-loop feedback controller, which turns out to be always quasi-adaptive. 
5.4 Naive Feedback and Open-Loop Feedback Controllers 
The naive feedback controller (NFC) is a control scheme based on an idea that has been used with considerable success for many years. It is also called certainty equivalent controller and its conception and justification dates to the origins of feedback theory when feedback was employed as a device that compensated for uncertainties and noise in the system. Traditionally servo- mechanism engineers when faced with the design of a controller for an un- certain system, assumed away or neglected the uncertainty by fixing the un- certain quantitities at some typical values (for example, their expected values) and designed a feedback control scheme for the corresponding deterministic system on the basis of certain considerations (stability, optimality with re- spect to a criterion, etc.). They relied on the feedback mechanism to com- pensate for uncertainties and noise in the system. The NFC draws from that idea. It applies at each time the control input that would be optimal if all the uncertain quantities were fixed at their expected values, i.e., it acts as if a form of the certainty equivalence principle, discussed in Sections 1.3, 3.1, and 4.3, were holding. 
We take as our model the basic problem with imperfect state information of Section 4.1 and we further assume that the probability measures of the input disturbances w k  do not depend on x k  and u k .  We assume that the state spaces and disturbance spaces are convex subsets of corresponding Euclidean spaces so that the expected values 
x k  = E { X k l l k ) ,  w k  = E { W k ) r  
belong to the corresponding state spaces and disturbance spaces. 
by the following rule: The control input f i k ( l k )  applied by the NFC at each time k is determined 
(a) Given the information vector I k ,  compute 
x k  = E { x k  I I k ) .  
(b) Solve the deterministic problem of finding a control sequence { i i k ,  i i k +  . . . , iiN- that minimizes 
N- 1 
g N ( X N )  f g k ( X k ,  u k ,  w k )  
i = k  
1 94 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
subject to the constraints? - 
U i E  u i ,  X i + l  = f ; ( X i ,  U i ,  El), i = k,  k + 1, ..., N - 1, x k  = x k .  
(c) Apply the control input 
b k ( l k )  = $ k .  
Note that if the current state x k  is measured exactly (perfect state information), then step (a) is unnecessary. The deterministic optimization problem in step (b) must be solved at each time k as soon as the initial state x k  = E { & I l k }  
becomes known by means ofan estimation (or perfect observation)procedure.$ A total of N such problems must be solved in any actual operation of the NFC. Each one of these problems, however, is a deterministic optimal control problem and is often of the type for which powerful deterministic optimization techniques such as steepest descent, conjugate gradient, Newton’s method [LlO] are applicable. Thus the NFC requires the solution of N such problems in place of the solution of the DP algorithm required to obtain an optimal controller. Furthermore, the implementation of the NFC requires no storage of the type required for the optimal feedback controller-often a major advantage. 
The implementation of the NFC given above requires the solution of N optimal control problems in an “on-line” fashion, i.e., each of these problems is solved as soon as the necessary information x k  = E { x , ‘ l l k }  becomes available during the actual control process. The alternative is to solve these problems a priori. This is accomplished by determining an optimal feedback controller for the deterministic optimal control problem obtained from the original problem by replacing all uncertain quantities by their expected values. It is easy to verify (based on the equivalence of open-loop and feedback implementation of optimal controllers for deterministic problems) that the implementation of the NFC given earlier is equivalent to the following implementation : 
be an optimal controller for the deter- ministic problem 
Let {&x0), . . . , p i -  1 ( x N -  
N -  1 
minimize g N ( X N )  + 1 g k [ X k ,  P k ( X k ) ,  w k l  Over all {PO 9 . . . 9 P N -  1 )  
k = O  
subject to P k ( x k )  E U k r  v x k  E s k ,  x k +  1 = f k c x k ,  P k ( x k ) ,  E k l ,  
k = 0 , 1 ,  ..., N - 1 .  
t We assume that there exists an optimal sequence {a,, ti,, . . . , 12,- Furthermore, if multiple solutions exist for the minimization problem, some rule is used to select one of them in an unambiguous way. 
3 In practice, often one uses a suboptimal estimation scheme that generates an “approxi- 
mate” value of .i = E { x k l l k } .  
5.4 NAIVE FEEDBACK AND OPEN-LOOP FEEDBACK CONTROLLERS 195 
Delay l ' =  I - - 1 
Then the control input flk(1k) applied by the NFC at time k is given by 
as shown in Fig. 5.3. In other words an alternative implementation of the NFC consists ofjinding 
a feedback controller {p:, p f ,  . . . , p$- 1}  that is optimal for a corresponding 
deterministic problem, and subsequently using this controller for control of the uncertain system (modulo substitution of the state by its expected value) in the spirit of traditional servomechanism design. Either of the definitions given for the NFC can serve as a basis for its implementation. Depending on the nature of the problem one method may be preferable to the other. 
The NFC often performs well in practice and results in a value of the cost functional that is close to the optimal value. In fact for the linear-quadratic problems of Sections 3.1 and 4.3, it is identical to the optimal controller (certainty equivalence principle). However, it is possible that the NFC is not quasi-adaptive (performs strictly worse than the optimal open-loop con- troller), as the following intriguing example shows. 
EXAMPLE Consider the following two-dimensional, two-stage linear system with scalar controls and disturbances : 
flk(Ik) = pflcE{xk I r k } l  = p f l ( x k )  
196 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
and with initial state xh = xi  = 0. The controls u o ,  u1 are unconstrained and the disturbances wo, w1 are independent random variables with identical distribution. They take the values +1 and -1 each with probability +. Perfect state information prevails. 
Case 1 Consider the cost functional 
where 11 * )I denotes the usual Euclidean norm. Since this is a quadratic cost functional and certainty equivalence holds, we expect that the NFC is an optimal controller for this problem. Indeed, let us first compute the optimal controller by the DP algorithm. We have 
J2(x2) = Ilx21121 
J,(x,) = min E {J,c(x: + u1 + +wl, x: + + J Z w l ) l }  u1 W l  
= min E{(x: + u1 + +w112 + (x: + f J Z w 1 1 ~ )  UI w1 
By minimization we obtain the optimal controller and “cost-to-go” for stage 1: 
pT(x1) = -4, 
and 
Jl(X1) = Cx:)‘ + E {(+w1)2 + = cX:l2 + 1. W I  
Also 
= min E {J,C(X; + uo + +wo, x i  + + f i w 0 ) l )  
= E {(xi + +JZWO)2 + $} = (Xi)2 + 2. 
J* = JO(O) = 2. 
uo wo 
wo 
Thus we obtain the optimal cost corresponding to the initial state xo = 0: 
Furthermore, applying any control uo at stage 0 is optimal. The NFC may be obtained by means of the second implementation scheme 
described earlier whereby we consider the problem of obtaining an optimal 
feedback controller for the deterministic problem resulting when wo and w , 
5.4 NAIVE FEEDBACK AND OPEN-LOOP FEEDBACK CONTROLLERS 197 
are replaced by their expected values Go = Wl = 0. The DP algorithm for this deterministic problem is given by 
f 2 b 2 )  = IIX211’~ 
f l (x l )  = min f,[(x: + ul, x:)] = (x:)~, 
fo(xo) = min Jl[(xA + uo,  xg)] = (xi)’, 
and one can easily see that the NFC is identical to the optimal controller. This is, of course, due to certainty equivalence. Thus iff denotes the cost corre- sponding to the NFC, we have 
J * =  j = 5  
u1 
u1 
4. 
We also calculate the optimal open-loop value J:, i.e., the optimal cost attained by an open-loop controller. Since (in view of xo = 0) the final state xz is given by 
we have 
J ;  = min E { [ u o  + u1 + %wo + w,)12 + %wo + wl)’}. uo, UI WO. w1 
One may easily see that any pair (uo,  ul) with uo + u1  = 0 attains the mini- mum above and computation of the expected value yields 
J :  = $. 
rhus for this problem we have 
J*  = f < J:, 
and the NFC is adaptive. 
Case 2 Consider now the cost functional 
E {Ilx2ll>. WO. WI 
The NFC is obtained from the DP algorithm for the corresponding deter- ministic problem. Straightforward calculation yields 
J2(x2) = I b 2 l L  
fl(xl)  = min f2[(x: + ul, xt)] = Ix: I, 
fo(xo) = min f ,  [(x; + uo, xi)] = I xi  I. UI 
uo 
1 98 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
The NFC is the same as for Case 1 : 
fil(xl) = -xi, fio(xo) = any scalar. 
This is due to the fact that minimizing llx2 1 )  is equivalent to minimizing llx2 1 1 ’  in the absence of uncertainty. With this controller and given that xo = 0, the final state x2 is equal to 
and the corresponding value of the cost functional is 
The optimal open-loop value is obtained from 
J ;  = min E { ( [uo  + u1 + +(wo + w1)12 + %w0 + W~)~)”~I. UO. U I  WO. W I  
Any pair (uo ,  ul) with uo + u1 = 0 attains the minimum above and computa- tion of the expected value yields 
J ;  = +a. 
Thus we have 
5; < j 
and the NFC is not quasi-adaptive. Actually for this case one may verify that the optimal cost corresponding to an optimal feedback controller is 
J* = J* - 1 0 - 2 J 3  
so that for this case the open-loop optimal value is equal to the optimal value. 
This example is rather astonishing in view of the well-rooted conviction among engineers that feedback designs tend to compensate for uncertainties and noise in the system and hence are preferable to open-loop designs. The statement is true, of course, if one uses optimal feedback obtained through a problem formulation that explicitly takes into account the uncertainty. It is not necessarily true if one uses a feedback controller obtained from an op- timization problem where uncertainties are not explicitly considered. 
Open-Loop Feedback Controller 
The open-loopfeedback controller (0LFC)is similar to the NFC except that 
it takes explicitly into account the uncertainty about xk, wk, . . . , wN- when 
calculating the control input to be applied at time k.  
5.4 NAIVE FEEDBACK AND OPEN-LOOP FEEDBACK CONTROLLERS 199 
The OLFC applies at  each time k a control input j i k ( l k ) ,  which is deter- 
(a) Given the information vector 1, compute the conditional prob- 
(b) Find a control sequence { i i k ,  i i k + l , .  . . , i iN-  1 }  that minimizes 
mined by the following procedure: 
ability measure Pxk,,k.  
subject to the constraints 
U ~ E  U i ,  xi+l = L ( X ~ ,  i ,  w i ) ,  i = k, . . . , N - 1.t 
(c) Apply the control input 
P k ( l k )  = i i k .  
The operation of the OLFC can be interpreted as follows: At each time k the controller uses the new measurement received to calculate the con- ditional probability P x k I I k .  However, it selects the control input as if no further measurements will be received in the future. 
Similarly to the NFC, the OLFC requires the solution of N optimal control problems in any actual operation of the system. Each of these prob- lems may again be solved by deterministic optimal control or mathematical programming techniques. The computations are a little more complicated than those for the NFC since now the cost functional includes the expectation operation with respect to the uncertain quantities. The main difficulty in the implementation of the OLFC is the computation of P x k l I k .  In many cases one cannot compute Pxkl Ik  exactly, in which case some “reasonable” approxima- tion scheme must be used. Of course, if we have perfect state information, this potential problem does not arise. 
We now prove that the OLFC is quasi-adaptive. 
Proposition The value of the cost functional JE corresponding to an OLFC E = { P o ,  , E l , .  . . , jiN-l} satisfies 
J* < J, < Jg. (46) 
Proof $. We have 
t Similarly as for the NFC, we assume that an optimal solution to this problem exists and 
$ We assume throughout the proof that all expected values appearing are well defined and ambiguities resulting from multiple solutions are resolved by some rule. 
finite and the minimum in (50) is attained for every I , .  
200 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
where the function J ,  is obtained from the recursive algorithm 
Consider also the functions J;(Ik), k = 0, 1, . . . , N - 1, defined by 
c N -  1 
The minimization problem indicated in this equation is precisely the one that must be solved at time k in order to calculate the control input F k ( I k )  of the OLFC. Clearly J;(Ik) can be interpreted as the calculated open-loop optimal cost from time k to time N when the current information vector is I,. It is easy to see that we have 
We shall prove that 
Then from (47), (51), and (52) it will follow that 
which is the relation to be proved. We shall show (52) by induction. By the definition of the OLFC and (50) we have 
and hence (52) holds for k = N - 1. Assume 
5.4 NAIVE FEEDBACK AND OPEN-LOOP FEEDBACK CONTROLLERS 201 
Then from (49), (53), and (50) we have 
I k ( l k )  = E { g k [ X k  v P k ( l k ) ,  w k l  X k .  W k s  V k  + 1 
The second inequality follows by interchanging expectation and minimization (notice that we have always E{min[ - 1 )  < min[E{ } ] )  and by “integrating out” vk+ The last equality follows from the definition of OLFC. Thus (52) is proved for all k and the desired result is shown. 
It is worth noting that by (53) the calculated open-loop optimal cost from time k to time N, & . ( l k ) ,  provides a readily obtainable performance bound for the OLFC. 
The above proposition shows that the OLFC uses the measurements with advantage even though it selects at each period the present control input as if no further measurements will be taken in the future. Of course, this says nothing about how closely the resulting value of the cost functional approxi- mates the optimal value. The general opinion, however, is that the OLFC is a fairly satisfactory mode of control for many problems, although future experience will undoubtedly shed more light on this question. 
Concerning the comparison of the NFC and the OLFC one should note that even though the NFC may not be quasi-adaptive, it may be considerably easier to implement than the OLFC. On the other hand, the OLFC, in con- trast to the NFC, can be used even for problems that are not defined over Euclidean spaces and is thus a more general form of suboptimal control. In 
Q.E.D. 
202 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
general, the two controllers cannot be compared on the basis of their corre- sponding values of cost functional. The example and the proposition of this section show that the OLFC may perform better than the NFC. The example in Problem 4 shows that the opposite may also be true. Both con- trollers may exhibit some rather counterintuitive behavior due to their sub- optimality. An example of such behavior is given in Problem 5. 
5.5 Partial Open-Loop Feedback Controllers and the Efficient Utilization of Forecasts 
As discussed in Section 5.4, the OLFC utilizes past measurements in the computation of the conditional probability measure PxklIk  but calculates the control input j i k ( l k )  on the basis that no measurements will be taken in the future. A form of suboptimal control that is intermediate between the optimal feedback controller and the OLFC is provided by what we shall call the partial open-loop feedback controller (POLFC). This controller utilizes past measurements to compute PXklIk but calculates the control input on the basis that some (but not all) of the measurements to be taken will in fact be taken in the future. This suboptimal controller, as we shall explain below, is char- acterized by better performance bounds than the OLFC and is particularly useful in problems where forecasts of future input disturbances become known during the control process. 
Consider the basic problem with imperfect state information of Section 4.1. Let us assume that each measurement z k  consists of two separate measure- ments Z k ,  &, which are elements of appropriate spaces and are given by 
where h k ,  h k  are given functions and i j k ,  i ik are random observation dis- turbances characterized by given probability measures that depend explicitly only on x k  and u k -  and not on prior observation disturbances i j k -  1, i j k -  1, 
. . . , ijo, ij0 or any of the input disturbances. 
Roughly speaking, the POLFC computes the conditional probability 
measure Pxklrk ,  where I k  = (zo,  . . . , z k ,  uo,  . . . , u k -  1 ) ,  and then calculates the 
optimal policy for the truncated optimization problem over the remaining periods k ,  k + 1, . . . , N under the assumption that the measurements 
Z k +  1, . . . , ZN- will be taken, but the measurements &+ 1, . . . , ZN- will not. 
The rationale for such a procedure is that in some cases it may be much easier to compute the optimal policy as a function of the measurements Z k + l ,  
. . . ,ZN- only, rather than as a function of zk+ 1, . . . , ZN - and &+ 1, . . . , ,?N - 1. 
Such situations occur, for example, when Z k  represents an exact measurement 
5.5 PARTIAL OPEN-LOOP FEEDBACK CONTROLLERS 203 
of the current state and ,?k represents forecasts on future input disturbances, as will be explained later. 
We define now precisely the POLFC, denoted {&(Io),  . . . , jiN- l ( Z N - l ) } ,  by specifying the rule by means of which the control input ,i&(Ik) at time k is calculated : 
(a) Given the information I ,  compute the conditional probability measure Pxk, ,k .  
(b) Define the following partial information vectors : 
I:+ 1 = ( z k +  1 ,  u k h  
I : + 2  = ( z k + l ,  z k + 2 ,  u k ?  u k + l ) ,  
I: - 1 = ( z k  + 1 ,  z k  + 2 9 * . . 7 ZN - 1 ,  u k  9 . . . 1 u N  - 21, 
and consider the problem of finding a control u k  E U k  and functions p!(Zf), such that &I!) E U i  for all I ;  and i, that minimize the cost functional 
r N -  1 
+ g k ( X k ,  u k ?  w k ) l l k  
subject to the constraints 
X k +  1 = f k ( X k 7  u k ?  w k ) ,  
x i + l  = f i [ x i ,  &I!), w i ] ,  i = k + 1,. . . , N - 1. 
Let { & ,  j$+ 1 ,  . . . , &- be an optimal policy for this problem.? 
(c) Apply the control input 
P k ( l k )  = uk. 
Note that if the measurements z k ,  k = 0, . . . , N - 1, are vacuous (provide 
no information about the current state as, for example. in the case where the values of the functions T;k do not depend on x k ) ,  the POLFC is identical to the OLFC. If the measurements F k  are vacuous, then the POLFC is identical with the optimal feedback controller. 
Now let us consider the problem of minimizing the cost functional over all admissible controllers of the form {po( lo) ,  . . . , p N -  l ( lN-  1)}, where the partial information vectors 1, are defined by 
10 = {zo}, 1, = {ZO,. . . 7 z k ,  u0,. . . 7 u k - l } .  
t Similarly as for the NFC and OLFC we assume that such a policy exists and that a certain rule is used to resolve ambiguities resulting from multiple solutions. 
204 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
This problem is obtained from the basic problem assuming that the measurements i k  are not taken. If J* is the corresponding optimal value, we clearly have 
where J* and J:  are the optimal value and optimal open-loop value of the basic problem. 
The following proposition is analogous to the proposition of the previous section and admits an entirely similar proof. 
Proposition The value of the cost functional JE corresponding to a POLFC ?I = { P o ,  ,iil,. . . , PN- satisfies 
J* < J ,  < J* < J,*. 
It should be mentioned that while again it is not clear that the POLFC approximates closely in terms of performance the optimal controller, the 
upper bound (I* - J * )  on the deviation of the value of the cost over the 
optimal is smaller than the corresponding bound ( J t  - J*)  for the OLFC. 
On the other hand, surprisingly, it is possible that the POLFC performs worse than the OLFC in a given situation. One example of such behavior has been constructed by E. Alleman-a student in one of the author's classes- but is too complicated to be presented here. 
We now turn to the application of the POLFC idea to a specific class of problems involving forecasts on future input disturbances. Consider the basic problem with perfect state information where the probability measures 
of the input disturbances wk do not depend on xk or uk, k = 0, 1, . . . , N - 1. 
Furthermore, assume that at each time the controller in addition to knowing the value of the current state xk has access to a forecast 
Each element 8 of the forecast f k  represents an appropriate noisy measure- ment of the future input disturbance w i ,  i = k ,  . . . , N - 1. These forecasts 
can be utilized to update at each time the probability measures of future input disturbances. 
It should be realized that the presence of the forecasts transforms the problem in effect into one of imperfect state information, which involves a system of the form 
5.5 PARTIAL OPEN-LOOP FEEDBACK CONTROLLERS 205 
The state of this system is 
:k = (xk? W k r  w k +  1 ,  . * .  9 W N -  1 1 ,  
and the system functionA is defined in an obvious way from the system equation xk+ = fk(xk, uk, wk). The cost functional can also be easily re- formulated in terms of the variables of system (54), and the measurement 
obtained by the controller at each time k can be viewed as a measurement of state 2, of system (54). 
Now a sufficient statistic for the problem of imperfect state information outlined previously is provided by (xk ,  Pwk, ..., w N -  I I I k ) ,  where Pwk, ..., w N -  l l I k  is the joint conditional probability measure of the future disturbances 
wk, . . . , w N -  In many cases wk, . . . , w N -  are independent under the con- 
ditional probability measure, in which case Pwk, ..., w N -  , I I k  is characterized by PwklIk ,  . . . , PwN-  I .  We shall assume this independence in what follows. 
Thus the optimal feedback controller must be obtained from a DP  algorithm that is carried over either the spaces of the information vectors 1, or over the space of the sufficient statistic (xk, PWklIk ,  . . . , P w N -  I I I k ) .  Clearly the com- 
putation of this optimal controller is extremely difficult except for special cases such as the one considered in Section 2.3. 
When, however, the POLFC philosophy is adopted things may be con- siderably simplified. According to the scheme outlined earlier in this section, at each time k the state x k  and P w k ~ ~ k ,  . . . , PWN- , i tN-  are obtained, and the 
optimization problem of part (b) of the definition of the POLFC is solved to obtain the control input j i k ( l k ) .  This problem consists of finding {,&(Xk), 
i i k +  1 ( x k +  I ) ,  . . . , ,&- l ( x N -  1)}, with Pi(xi) E U i ,  i = k ,  . . . , N - 1, that mini- 
mize 
c N -  1 -l 
subject to the system equation constraints 
x i +  1 = f i [ x i ,  &(xi), wi],  i = k ,  . . . , N - 1. 
Now the above problem is one of perfect state information and may be much easier to solve than the original problem. For example, it may possess an analytical solution or be one dimensional in the state variable. In this way the implementation of the POLFC may be feasible while the implementation of the optimal controller may be impossible. 
206 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
Summarizing the above discussion the POLFC for the perfect state in- formation problem with forecasts operates as follows : 
(a) An optimal feedback policy is computed at the beginning of the process on the basis of the a priori statistics of the input disturbances and assuming no forecasts will be available in the future. 
(b) Each time a forecast becomes available the statistics of the future input disturbances are accordingly updated. The optimal feedback policy is revised to take into account the updated statistics but is computed on the basis that these statistics are final and will not be updated by means of future forecasts. 
It is to be noted that this mode of operation does not require a detailed statistical modeling of the forecasting process. The only requirement is to be able to compute the updated probability measures P w k l I k , .  . , P w N - , I I k  
of future disturbances given the forecasts up to time k. This is particularly convenient in practice since forecasts may be of a complicated and unpre- dictable nature, such as marketing surveys, unforeseen “inside” information, unpredictable changes in the economic environment, and subjective feelings of the decision maker. 
As an example, consider a dynamic inventory problem such as the one considered in Section 3.2 where forecasts on future demands become avail- able during the process. The POLFC calculates an initial multiperiod (s, S) policy based on the a priori probability distributions of future demands. As soon as new forecasts are obtained and these distributions are updated the current (s, S) policy is abandoned in favor of a new one calculated on the basis of the updated demand distributions. The new (s, S) policy is again updated as soon as new forecasts become available and so on. In this way a reasonable and implementable policy is adopted while the optimal policy would perhaps be impossible to calculate or implement. 
As another example, consider an asset selling problem similar to the one of Section 3.4 where we assume that forecasts on future price offers become available during the sale process. The POLFC approach suggests the cal- culation and adoption of an initial policy, characterized by cutoff levels al, . . . , aN- for accepting and rejecting an offer, based on the initial prob- 
ability distribution of offers. As soon as, say at time k, forecasts become available and the probability distribution of future offers is updated, new 
cutoff levels ak, . . . , aN- are calculated, which specify a new policy to be 
followed until the next forecasts become available. The resulting expected revenue from using the POLFC is larger than that which would result if the decision maker were to stick to the initial policy and disregard the forecasts. It is safe to presume that many decision makers, guided by intuition rather than detailed planning, would in fact adopt a policy similar to the one sug- gested by the POLFC. 
5.6 CONTROL OF SYSTEMS WITH UNKNOWN PARAMETERS 207 
5.6 Control of Systems with Unknown Parameters -Self-Tuning Regulators 
We have been dealing so far with systems having a known state equation. In practice, however, one is frequently faced with situations where the system equation contains parameters that are not known exactly. One possible approach, of course, is to conduct experiments and estimate the unknown parameters from input-output records of the system. This procedure, how- ever, can be quite time consuming. Furthermore, it may be necessary to re- peat the procedure if the parameters of the system change with time as is often the case in many industrial processes. 
The alternative is to formulate the stochastic control problem in a way that unknown parameters are dealt with directly. It is very easy to show that problems involving unknown system parameters can be embedded within the framework of our basic problem with imperfect state information by using state augmentation. Indeed, let the system equation be of the form 
xk + 1 = fk(x& 3 0, U k  w k ) ,  
where 8 is a vector of unknown parameters with a given a priori probability distribution. We introduce an additional state variable y k  = 8 and obtain a system equation of the form 
By defining .ck = ( X k ,  yk)  as the new state, we obtain 
:k+ 1 = jxk(:?k, U k r  W k ) ,  
whereA is defined in an obvious manner from (55).  The initial state is 
I, = (xo, 8). 
With a suitable reformulation of the cost functional, the resulting problem becomes one that fits our usual framework. 
It is to be noted, however, that since y, = 0 is unobservable we are faced with a problem of imperfect state information even if the controller receives an exact measurement of the state x k .  Furthermore, the parameter vector 8 usually enters the state equation in a manner that makes the augmented system (55)  nonlinear. As a result, in the great majority of cases it is practically impossible to obtain an optimal controller by means of a DP algorithm. Suboptimal controllers are thus called for and in this section we discuss in some detail a form of the certainty equivalent controller that has been used with success in some problems involving linear systems with unknown parameters. 
208 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
Certainty Equivalent Control of’ Linear Systems with Unknown Parameters 
Consider a linear system of the form 
xk+l = Ak(8)xk + Bk(@k + w k *  
The matrices Ak and Bk depend on an unknown parameter vector 8, which is an element of a Euclidean space. The functional form of Ak( - ) and &( - ) is known. The cost functional is quadratic of the form 
The disturbances wk are independent and perfect state information prevails. If the parameter vector 8 were known, the corresponding optimal control 
law would be given by 
d ( x k ~  e, = Lk(8)xk? where 
Lk(e) = - CRk + Bk(8)’Kk+ l ( e ) B k ( e ) l -  ‘ B k ( e ) ’ K k +  l(e)Ak(e), (56) 
and K k +  1(8)  is given by the Riccati equation, which corresponds to A,(@, 
When 8 is not known we are faced with a problem of imperfect state in- formation as explained earlier. The information vector is = { x o ,  . . . , xk, u o ,  . . . , uk- 1 }  and the corresponding NFC (certainty equivalent controller) is 
given by 
where 
Bk(8), Qk, and Rk (Cf. Section 3.1). 
f i k ( l k )  = L k ( B k ) X k  9 
At each time k the NFC computes the conditional expectation 8, and then calculates the gain L k ( 8 k )  from Eq. (56)  once the matrix & + I ( & )  has been obtained from the corresponding Riccati equation. In practice the com- putation 6f 8, may present formidable difficulties and for this reason usually one computes an approximation of 8, by means of a conveniently imple- mentable estimator. We now discuss in some detail a simple special case. 
Self- Tuning Regu lat ors 
n + l), . . . , by the equation 
Consider a scalar controlled process described for k = (m + n), (m + 
yk+tn+l + alyk+m + * ”  + anyk+m+l-n = b l U k  f ” ’  + b n U k - n + l  + ek* (57) 
5.6 CONTROL OF SYSTEMS WITH UNKNOWN PARAMETERS 209 
The scalars Y k ,  Uk are considered to be the output and the input, respectively, of the process at time k. There is a delay of rn 2 0 time intervals between the time that the input is applied and the time at which it affects the process. The scalar stochastic disturbances ek are independent over time and have zero mean. The parameters a l , .  . . , a,, b l , .  . . , bn are unknown and it is 
assumed that bl # 0. The algorithms to be presented can be easily modified if some of the parameters are unknown and the remaining are known. 
The process described above when there is no control (i.e., bi = 0) is known as an autoregressive process of order n and is a widely used model of linear processes. A more general model is obtained if we replace e k  in Eq. (57) by ek + clek- + + C,f?k- , .  Control algorithms similar to the ones that will be presented shortly can also be developed for such more general models. In order to keep the exposition simple, however, we shall restrict ourselves to the process (57). 
Equation (57) may be written in a different form, which is more convenient for our purposes. We have from (57) 
a l ( Y k + m  + a l Y k + m - l  + * * *  + % y k +  m - n )  
= a l ( b 1 u k - l  + ' . '  + b n u k - n )  + a l e k - 1 .  (58)  We may eliminate Y k + , , ,  by subtracting (58)  from (57). We obtain 
2 Y k + m +  1 + (a2 - a l ) Y k + m -  1 + * ' * + (an - a,%- l ) Y k + m +  1 --I - a l a n y k + m - n  
= b l U k  + (b2 - a l b 1 ) u k -  1 + ' '  ' + (b, - albn- 1 ) U k - n +  1 
- U 1 b , U k - ,  -k e k  - U l e k - 1 .  
Proceeding similarly we can obtain an equation of the form 
Y k + m + l  + a l y k  + * * .  + a n Y k - n + l  = B O ( u k  + B l u k - 1  + . ' .  + 8 l u k - l )  + c k  
(59) 
where I = n + rn - 1, and f?k is a linear combination of the disturbance 
vectors ei. The coefficients a l ,  . . . , u,, Po, . . . , Bl in (59) are determined from 
the coefficients a,, . . . , a,, b,, . . ., b, by means of the elimination process described above. Furthermore, it is easy to see that we have Po = bl # 0. Note that when there is no time delay (i.e., rn = 0) Eqs. (57) and (59) coincide. 
The problem that we are concerned with is to find a suitable control law 
depending on the past inputs and outputs, which are assumed to be observable without error. We utilize the quadratic cost functional 
k ( l k )  = ~ ( k ~ O , . . . , Y k , U O , . . . , U k - l )  
Thus, the objective of control is to keep the output of the process near zero. 
210 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
If the parameters a l ,  . . . , a,, b , ,  . . . , b,, in Eq (57) were known, the optimal 
control law could be obtained by reformulating our problem into the form of the basic problem with perfect state information via state augmentation, and by subsequently applying the DP algorithm. We shall bypass, however, this reformulation and obtain the optimal control law directly. Since the system is linear, the criterion is quadratic, and the disturbances are inde- pendent, certainty equivalence holds. The optimal control law is the same as the one that would be obtained if the disturbances ek are set equal to their expected value z k  = 0, and the system equation is given by [cf. (57)] 
n fl 
Y k + m + l  + x a i . v k + m + l - i  = x b i U k + l - i r  i =  1 i =  1 
or equivalently by [cf. (59)] 
Y k + m + l  + a l y k  + " '  + ' % Y k - n + l  = P O ( u k  + P l u k - 1  + " '  + P l u k - 1 ) .  
By using the equation above in the cost functional (60) it follows immediately that the optimal control law for the corresponding deterministic problem is given by 
By certainty equivalence the same control law is optimal for the stochastic problem assuming that the parameters a l ,  . . . , a,,, P o , .  . . , fll are known. 
Note that this control law does not depend on the time index k or the number of stages N. 
When the parameters a,, . . . , a,, Po.  . . . , PI are unknown, then an approxi- mate form of the NFC is given by 
I I n  
where 1, = ( y o , .  . . , y k ,  uo ,  . . . , u k -  1 )  and ~'i,. . . , E:, f l ! ,  . . . , fl: are esti- 
mates of the parameters a l , .  . . , a,, P o , .  . . , P I  based on the inputs and out- 
puts available up to time k. 
If it were possible to construct an estimation scheme such that the esti- mates C:, flf converge to the true parameters a i ,  p i ,  then the suboptimal con- troller defined by (61) would become asymptotically optimal. In fact, for this purpose it is sufficient that 
lim 8: = P i ,  i = 1 , .  . . , I ,  
k+  m 
lim $/fl! = ai/Po, i = 1,. . . , n. (63) 
k - + m  
5.6 CONTROL OF SYSTEMS WITH UNKNOWN PARAMETERS 21 1 
A suboptimal controller of the form (61) equipped with an estimation scheme for which (62) and (63) hold (with probability one) is referred to as a self-tuning regulator. Such regulators have many advantages. They are very simple to implement (provided the estimation scheme is simple), and they become optimal in the limit. Furthermore, not only they do  not require a priori knowledge of the parameters of the process, but in addition they adjust appropriately when these parameters change-a frequent occurrence in many processes. 
At the present time the analysis of the question as to when a regulator of the type described above has the self-tuning property is not complete. Future research will undoubtedly shed more light on this question. However, it appears that for many practical problems it is possible to construct simple self-tuning regulators. 
Let us describe briefly a simple estimation scheme that can be used.in conjunction with the control law (61). The scheme is based on the method of least squares and has been used with success in several applications. One may show that due to the employment of the feedback control law (61) it is possible that the least squares estimation scheme may encounter subtle difficulties if we try to estimate all the parameters a l , .  . . , a n ,  P o , .  . . ,P,  (see Problem 7). On the other hand we note that for purposes of control we do not need to estimate both Po and a i ,  i = 1, . . . , n. Rather, from (61) it follows that we need only estimate the ratios ailPo, i = 1,  . . . , n. This will be done by keeping 
Po fixed at some nonzero value P o ,  and by estimating ai, i = 1,. . . , n, to- gether with Pi, i = 1,. . . , 1. Let us define the (n + /)-dimensional column 
vectors 
6' = (a1,. . . , a,, P1,. . . , PJ', 
z k  = ( - J ' k , * * * r  -yk-n+lrPOUk-1,...r8Ouk-I)I, 
where Po has a fixed nonzero value assumed equal to Po for the purposes of estimation. Then Eq. (59) is written 
y k  = P 0 u k - m -  1 + 2 L - m -  16' + 2 k - m -  1. 
The least squares estimate of 6 at time k is denoted by 8, and is the vector that minimizes 
k 
(e - O)T(O - 8) + 1 hi - f l O u i - , , -  , - --I-,,, - ,t)12, 
i = m +  1 + I  
where 8 is an initial estimate of 6' and P is a positive definite symmetric matrix. It is possible to show that the least squares estimate 8, can be gener- ated recursively by the equations 
O k +  1 = Ok + gkbk - b O u k - m -  1 - z L - m -  18k)r 
212 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
where the vectors g k  E R("+') satisfy 
g k  = P k Z k - m -  + & - m -  l P k Z k - m -  l ) - ' ,  
and the (n + 1 )  x (n  + I )  matrices P k  satisfy 
p k +  1 = p k  - g k d ( l  + Zh-m- l P k Z k - m -  1). 
The initial conditions are 
O m + l  = 8, P,+r = P .  
A proof of the validity of these equations may be found in most texts on parameter estimation theory (see, e.g., [M7]). 
When estimation is carried out by the least squares method described above, the control law (61) takes the form 
This control law does not always have the self-tuning property 
1 1 
lim - 8, = - 0. 
However, both analysis and simulations indicate that if Po is chosen judi- ciously and the order n of the model and the size m of the delay adequately represent those of the real process, then the self-tuning property can often be achieved. In practice one can settle on appropriate choices for Po,  n, and m by experimentation and simulation. 
A detailed analysis of the regulator (61) equipped with the least squares estimation scheme described above would take us beyond the scope of the text and will not be undertaken. We mention that the main result, proved by Astrom and Wittenmark [A91 under a mild assumption on the process, is that if the estimates 8, converge to some vector 8, then a self-tuning regulator i S  
obtained, i.e., 
k - m b O  P O  
1 1 - 0 = - 8 .  P o  Po 
Since the estimates 8, do in fact converge in many cases, the result is quite reassuring. It is also a rather remarkable result in view of the fact that the fixed scalar P o  need not be equal to the true parameter Po.  Furthermore, even if Po = Po,  it is by no means obvious that we should have 8 = 0 since the least squares method ordinarily will give in the limit biased estimates of the true parameters. We shall demonstrate the result for a simple special case. 
5.6 CONTROL OF SYSTEMS WITH UNKNOWN PARAMETERS 213 
First-Order Process 
Consider the process 
yk+l  + = B u k  + e k *  (64) Let B denote the fixed scalar used in the least squares estimation procedure (i.e., our earlier Po), and let i i k  denote the estimate of a at time k. Then &k 
minimizes over a, k 
PO(R - ~ 0 ) ~  + (Y i  + ayi- 1 - 8.i- 
i =  1 
where Eo is an initial estimate of a and po  some positive scalar. By setting the derivative at Ek of the expression above equal to zero, we obtain 
k 
P O ( &  - 60) + 1 yi- 1bi + &yi- 1 - Bui- 1 )  = O, 
i= 1 
from which 
Now the controls ui-  are given by [cf. (61)] 
ui- 1 = (ai- 1/B)Yi- 1 .  (66) By substitution of (66) in (64), we obtain the form of the closed-loop system, 
Y . =  , rj-1 -  a)y i - l  + e i - l .  
By using Eqs. (66) and (67) in (65), we obtain 
Let us assume that the estimates converge to some scalar E ,  
lim Ek = E. (69) k- .  m 
Assume further that k 
lim C y ? - l  = co, (70) k+m i=l 
lim C!= 1 ei- 1Yi- 2 1 = 0. 
k+m PO + z= 1 Y i -  1 
214 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
Relation (70) will hold with probability one if the variance of the disturbance ek is nonzero. Relation (71) can be expected to hold since the random variable 
yi- , depends only on the disturbances ei-  2 ,  ei- 3 ,  . . . , and is therefore 
independent of ei-  Since ei-  has zero mean it follows that when yi.. has finite first and second moments and we assume that expected values are equal to the limit of the corresponding average sums (an ergodic assumption), then (71) holds. Notice that relations (69) and (70) imply also 
Now Eq. (68) may be written 
By taking the limit as k -, 00 and using (69)-(72), we finally obtain PE/F - a = 0 or equivalently 
which is precisely the self-tuning property. Thus, we have proved that if the estimates i k  converge [cf. (69)] a self-tuning regulator is obtained. The proof for more general processes follows a similar line of argument as the one given above. 
5.7 Notes 
The problems caused by large dimensionality have long been recognized as the principal computational drawback of DP. A great deal of effort by Bellman and his associates, and by others, has been directed toward finding effective techniques for alleviating these problems. A fairly extensive dis- cussion of the computational aspects of DP can be found in the book by Nemhauser “21. Various techniques that are effective for solution of some deterministic dynamic optimization problems by DP can be found in references [K6], [LZ], [L9], and [WlO]. Finally we note that a class of two- stage stochastic optimization problems, called “stochastic programming problems,” can be solved by using mathematical programming techniques 
PROBLEMS 215 
(see Problems 1, 2, references [Vl], [B7], [BlO], and the references quoted therein). The discretization and convergence results of Section 5.2 are due to the author [BlS]. 
The literature abounds with precise and imprecise definitions of ad- aptivity. The one adopted here is due to Witsenhausen [W4] and captures the idea that a controller should be called adaptive if it uses feedback with advantage. 
The example of Section 5.3 showing that the naive feedback controller may perform worse than the optimal open-loop controller is due to Wit- senhausen p h a u  and Witsenhausen, Tl]. For an interesting sensitivity property of the naive feedback controller see the paper by Malinvaud [M2]. The idea of open-loop feedback control is due to Dreyfus [D6], who dem- onstrated its superiority over open-loop control by means of some examples but did not give a general result. The result and its proof were given recently by the author [B8] in the context of minimax control. Suboptimal controllers other than the NFC and OLFC have been suggested by a number of authors [T3-T5, C1, D5, D7, C5, S1, S2, S15, S20, P6, Al, A9, B17, M9, W9]. The typical approach under imperfect state information is to separate the sub- optimal controller into two parts-an estimator and an actuator-and use a “reasonable” design scheme for each part. The concept of the partial open- loop feedback controller is apparently new. Self-tuning regulators received wide attention following the paper by Astrom and Wittenmark [A9]. For some recent analysis see Ljung and Wittenmark [LS]. 
Whenever a suboptimal controller is used in a practical situation it is desirable to know how close the resulting cost approximates the optimal. Tight bounds on the performance of the suboptimal controller are necessary but are usually quite hard to obtain. For some interesting results in this direction, see the papers by Witsenhausen [WS, W61. 
As a final note we wish to emphasize that the problem of choice of a suitable suboptimal controller in a practical situation is by no means an easy one. It may be necessary to conduct extensive simulations and experi- ment with several schemes before settling on a reasonably practical and reliable mode of suboptimal control. 
Problems 
1. The purpose of this problem is to show how certain stochastic control problems can be solved by (deterministic) mathematical programming techniques. Consider the basic problem of Chapter 2 for the case where there are only two stages (N = 2) and the disturbance set for the initial stage Do is a finite set Do = {w:, . . ., wb}. The probability of wb, i = 1,. .., r, is 
216 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
denoted pi and does not depend on x o  or uo.  Verify that the optimal value function Jo(xo) given by 
+ ~ z C f l c f o ( x o ~  uo, wb), u1, W l l 1 ) l  is equal to the optimal value of the problem 
i = l ,  ..., r 
subject to zi 2 E {glCfo(xo, uo, wb), u;, w1l WI 
+ g2CfiCfo(xo, uo, wb), uf, W l l l l ~  
uo E Uo(xo), 4 E ~ , C f o ( x o ,  uo ,  w i l l .  
Show also how a solution of the mathematical programming problem above may be used to yield an optimal control law. 2. Consider the problem of minimizing over x 
subject to hi(x) = 0, i = 1, . . . , s, l,(x) 6 0, j = 1, . . . , p ,  where x E R", y E R", 
q is a given vector in R", r E Rk is a random vector taking a finite number of values r l , .  . . , r, with given probabilities p l , .  . . , p , ,  g ,  hi ,  l j  are given con- 
tinuously differentiable real-valued functions, f : R" -+ Rk is a continuously differentiable mapping, and A is a given k x rn matrix. Show that this problem may be viewed as a two-stage problem that fits the framework of the basic problem of Chapter 2. Show also how the problem can be converted to a deterministic problem that can be solved by standard mathematical pro- gramming techniques. 3. Consider a problem with perfect state information involving the n- dimensional linear system of Section 3.1 : 
xk+l = Akxk + Bkuk + W k ,  k = 0, 1,. . ., N - 1, 
and a cost functional of the form 
PROBLEMS 217 
where c E R" is a given vector. Show that the DP  algorithm for this problem can be carried over a one-dimensional state space. 4. Consider a two-stage problem with perfect state information involving the scalar system 
xo = 1, X I  = xo + uo + wo, x 2  = f ( x 1 ,  u1). 
The control constraints are uo,  u1 E (0, - 1). The random variable wo takes the values + 1 and - 1 with equal probability 4. The functionfis defined by 
f( 1,O)  = f( 1, - 1) = f (  - 1,O) = f( - 1, - 1) = 0.5, 
f ( 2 , O )  = 0, f(2, - 1) = 2, f(0, - 1) = 0.6, f (0 ,O)  = 2. 
The cost functional is 
(a) Show that one possible OLFC for this problem is defined by 
and the resulting value of the cost is 0.5. (b) Show that one possible NFC for this problem is defined by 
0 if x 1  = k 1, 2, P O ( X 0 )  = 0 ;  Pl (X1)  = - 1  if x 1  = o, (74) 
and the resulting value of the cost is 0.3. Show also that the NFC above is an optimal feedback controller. 5. Consider the system and cost functional of Problem 4 but with the difference that 
f(0, -1) = 0. 
(a) Show that the controller (73) of Problem 4 is both an OLFC and an NFC and that the corresponding value of the cost is 0.5. 
(b) Assume that the control constraint set for the first stage is (0)  rather 
than (0, - l}. Show that the controller (74) of Problem 4 is both an OLFC 
and an NFC and that the corresponding value of the cost is 0. 6. Consider the linear quadratic problem of Section 4.3 where in addition to the linear measurements there are some nonlinear measurements received at each time k of the form 
Tk = h k ( X k ,  g k ) .  
The random observation disturbances Ck are independent random variables with given probability distributions. What is the POLFC that ignores the presence of Tk? 
218 5 COMPUTATIONAL ASPECTS OF DYNAMIC PROGRAMMING 
7. Consider the first-order process 
y k + l  + = P'k + ek examined at the end of Section 5.6. Assume that a control law of the form f i i ( I i )  = (CC/i/B)yi s utilized and E, p minimize 
k 
Show that [CC + (CCy/fl)], ( p  + y) also minimize the expression above, where y is any scalar. (This problem indicates a possible instability in the least- squares estimation scheme if both tl and P are estimated.) 
Part II  
Control of Uncertain Systems over an Infinite Horizon 
General Remarks on Infinite Horizon Problems 
The second part of this text is devoted to sequential optimization problems of the type considered in previous chapters but with two basic differences. First, the number of stages is assumed to be infinite, and second, the system is assumed to be stationary, i.e., the system equation and the random disturbance statistics do not change from one stage to the next. In addition, the cost per stage is assumed stationary (except perhaps for the presence of a discount factor). 
The assumption of an infinite number of stages is, ofcourse, a mathematical formalization since it is never satisfied in practice. Nonetheless, it constitutes a reasonable and analytically convenient approximation for problems involving a finite but very large number of stages. The assumption of station- arity is often satisfied in practice and in other cases it constitutes a reasonable approximation to a situation where the system parameters vary very slowly as time progresses. However, problems involving a nonstationary system or a nonstationary cost per stage can be reduced to the stationary case by means of a simple reformulation. This reformulation is discussed in Chapter 6 (Section 6.7). 
219 
220 PART I1 
Infinite horizon problems, as a general rule, require considerably more sophisticated mathematical analysis than their corresponding finite horizon counterparts. The analytical difficulties are of a twofold nature. First, the consideration of an infinite horizon introduces the need for analysis of limit- ing behavior, for example, the convergence of the DP algorithm and the cor- responding optimal policies. This analysis is often nontrivial and at times reveals surprising possibilities. Second, a rigorous consideration of the probabilistic aspects of problems involving uncountable disturbance spaces requires the sophisticated machinery of measure-theoretic probability theory. The resulting analytical difficulties are considerably more severe than those of finite horizon problems and are far beyond the introductory scope of this text. For this reason and given that the need for precision is much greater in infinite horizon problems than in their finite horizon counterparts we shall exclusively restrict ourselves to the case where the disturbance space is a countable set. The advanced reader may consult the works of Blackwell [B20], Strauch [S17], and Hinderer [H9] for more general expositions. 
It should be noted, however, that under the infinite horizon and station- arity assumptions one may obtain results of mathematical and conceptual elegance not to be found in finite horizon problems. Also the implementation of optimal policies for infinite horieon problems is often much simpler. For example, often the optimal policy can be selected to be stationary, i.e., the optimal rule for applying controls need not change from one time period to the next. In addition, in many cases of interest there are available powerful computational methods for calculation of such optimal policies. 
Traditionally there have been three classes of infinite horizon problems of major interest : 
(a) In the discounted case the cost functional takes the form N -  1 
J,(xo) = N - c a  lim { z o a k g [ x k ,  pk(Xk)r w k l ] ,  k = O ,  1, ... 
where J,(xo) denotes the cost associated with an initial state xo  and a policy n = { p o ,  pl, . . .}, and a is a scalar with 0 < a < 1, called the discountfactor. 
The discounted problem is by far the simplest infinite horizon problem particularly when the cost per stage g(x, u, w)  is bounded above and below. This case is examined in Sections 6.1-6.3. The case where g may be unbounded either above or below is examined in Sections 6.4-6.6 and is very similar to the undiscounted case where a = 1. 
(b) In the undiscounted case the cost functional takes the form 
CONTROL OF UNCERTAIN SYSTEMS OVER AN INFINITE HORIZON 22 1 
i.e., there is no discount factor (a = 1). This case is the subject of Chapter 7. Minimization of J,(xo)  above makes sense, of course, if J,(xo)  is 
finite for at least some admissible policies R and some initial states xo. In many problems of interest it turns out that J,(xo)  = + co, but the limit 
(c) 
is finite for every policy R = {po ,  p 1 , .  . .} and initial state x o .  Under these circumstances it is reasonable to try to minimize the expression above, which may be viewed as an average cost per stage associated with policy R. Such problems are the subject of Chapter 8. However, for this case we shall restrict our attention mostly to problems involving a finite state and control space, i.e., the system considered is a controlled finite state Markov chain. Some results from the theory of Markov chains will be developed in Chapter 8 and Appendix D as necessary. 
Chapter 6 
Minimization of Total Expected 
Value-Discounted Cost 
In this chapter we consider a class of infinite horizon problems that involves a discounted cost functional. The introduction of a discount factor is often justified, particularly when the cost per stage has a monetary inter- pretation. From the mathematical point of view the presence of the discount factor guarantees the finiteness of the cost functional provided costs per stage are uniformly bounded. 
Let us define the problem we shall be considering in this chapter. 
PROBLEM (D) Consider the stationary discrete-time dynamic system 
xk+ 1 = f ( x k ,  uk, wk), k = 0, 2, . . . 9 (1) 
where the state xk, k = 0, 1,. . . , is an element of a space S ,  the control uk, k = 0, 1, . . . , an element of a space C,  and the random disturbance Wkr k = 0, 1, . . . , an element of a space D. It is assumed that D is a countable 
set. The control uk is constrained to take values in a given nonempty subset f&k) of C,  which depends on the current state Xk[Uk  E v(xk) ,  for all xk E S, k = 0, 1 , .  . .]. The random disturbances wk, k = 0, 1 , .  . . ,have identical statistics and are characterized by probabilities f( - Ixk,  uk) defined on D, where f ( w k l x k ,  U k )  is the probability of occurrence of W k ,  when the current 
6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOlJNTED COST 223 
state and control are x k  and u k ,  respectively. The probability of w k  may depend explicitly on x k  and u k  but not on values of prior disturbances 
Given an initial state xo, the problem is to find a control law, or policy, w k -  1,. . . , W O .  
n = {Po,  P I , .  . .} where P k : s  c, P k ( X k ) E  u ( x k ) ,  for all x k  E S ,  k = 0, 1 , .  . . , that minimizes the cost functional? 
(2) 1 J n ( x O )  = lim E 1 a k g [ X k ,  P k ( X k ) ,  w k l  
N+CC W k  r k = O  - 
k = O .  1, ... 
subject to the system equation constraint (1). The real-valued function g :  S x C x D -+ R is given, and the discount factor a satisfies 0 < a < 1 .  
For any x o  E S and policy n the cost J, (xo)  given by (2) represents the limit of the (discounted) expected finite horizon costs and these costs are well defined as discussed in Section 2.1. Another possibility would be to minimize over n 
W k  E { $ t k g C x k  7 P k ( x k ) ,  w k l } *  
k = O .  1, ... The rigorous introduction of such a cost functional would require the con- struction of a probability measure on a set of events in the space of all se- quences { w o ,  w l , .  . .} with elements in D (see Kushner [ K l O ] )  and is well beyond the probabilistic framework of this text. However, we mention here that, under the assumptions we shall be using, the expression given above is equal to J,(xo) as given by (2) for every xo  E Sand policy n. This may be proved by using the so-called monotone convergence theorem (see, e.g., Halmos [H5] and Royden [RS]), which allows the interchange of limit and ex- pectation under assumptions that in our case are satisfied. It is also interesting to answer the question as to whether it is possible to reduce further the value of the cost functional by considering " history-remembering " policies of the form bo(I0), P ~ ( I ~ ) ,  . . .I, where 
I k  = (XO,UO,X1,Ulr...,Uk-l,Xk) 
is the history of the system up to time k (or information vector as in Section 4.1). The answer is negative within our framework (see Strauch [S17]), and as a result we shall not deal further with this possibility of enlarging the set of admissible policies. 
It is to be noted that, while we allow an arbitrary state and control space, we have made a restrictive assumption in requiring that the disturbance space D is a countable set. This assumption was mostly made in order to avoid 
t In what follows we always assume that g(x. 11, w )  is nonnegative or nonpositive for all x, u, w and hence the limit is well defined as a real number or f cc. 
224 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
the extremely complicated mathematical difficulties associated with the need 
to restrict the class of admissible policies so that 1::; akg[xk, pk(xk), wk] is 
guaranteed to be a well-defined random variable for each N. The count- ability assumption eliminates these difficulties as discussed in Section 2.1. Our assumption, however, is satisfied in many problems of interest, most notably for deterministic optimal control problems and problems of optimal control of a Markov chain with finite or countable number of states. Also for many problems of interest where our assumption is not satisfied, our main results still may be proved under other appropriate assumptions, usually by following the same line of argument as the one given here. For analysis related to problems involving uncountable disturbance sets the advanced reader may consult Blackwell [BZO], Hinderer [H9], and Strauch [ S l 7 ] .  
In the first three sections of this chapter we shall be operating under the following assumption : 
Assumption B (Boundedness) The function g in the cost functional (2 )  satisfies 
0 < g(x, u, w )  < M V(x, u, w )  E S x C x D, (3) 
where M is some scalar. 
Notice that (3) could be replaced by an inequality of the form 
M2 < g(x, u, W )  < M i ,  
where M1, M 2  are arbitrary scalars, since addition of a constant r to g merely adds ( 1  - a)- lr to the cost functional. The assumption above is not as re- 
strictive as it may seem at first sight. First, it holds always for problems where the spaces S, C,  and D are finite sets. Second, the assumption of finiteness of D is implicitly made each time a computational solution to the problem is sought. In addition, during the computations the effective state and control spaces will ordinarily be finite or bounded sets and relation (3) will usually hold. In other cases, it is often possible to reformulate the problem so that it is defined over bounded but arbitrarily large regions of the state space and the control space over which relation (3) holds. In any case the assumption will be somewhat relaxed in Section 6.4, where g will be allowed to be unbounded either from below or from above. 
Let us denote by II the set of all admissible policies 71, i.e., the set of all sequences of functions 71 = {po,  p l ,  . . .} with pk : S -+ C,  &(x) E V ( x )  for all x E S, k = 0, 1, . . . . Then the optimal value function J* given by 
J*(x) = inf J,(x) Vx E S n e n  
is well defined as a real-valued function under Assumption B. In fact, one may show that J* is uniformly bounded above and below. 
6.1 CONVERGENCE AND EXISTENCE RESULTS 225 
A class of admissible policies of particular interest to us is the class of 
stationary admissible policies of the form II = {p, p, . . .}, where p: S -, C, 
p(x)  E V ( x ) ,  x E S .  For such policies the rule for control selection is the same at every stage. The cost associated with an admissible stationary policy {p, p, . . .} and an initial state x E S will also be denoted by J,(x), i.e., for 7c = {p, p, . . .} we write 
Similarly as for J* we have that J ,  is well defined as a real-valued function under Assumption B. A statement that the stationary policy {p*, p*, . . .} is optimal will mean throughout this chapter that {p*,  p*, . . .} is admissible arid we have J * ( x )  = J,,.(x),fiw a//  x E S .  
The next section gives a characterization of the optimal value function J* and provides some convergence and existence results. Section 6.2 describes computational methods for Problem (D), under the assumption that the state, control, and disturbance spaces are finite sets. The results obtained in Sections 6.1 and 6.2 are interpreted by means of the notion of a contraction mapping in Section 6.3. In Section 6.4 we relax Assumption B and consider costs per stage that are unbounded above or below. In Sections 6.5 and 6.6 we consider a problem involving a linear system and a discounted quadratic cost functional and an inventory control problem with discounted cost. Finally, in Section 6.7 we consider problems involving a nonstationary or periodic system and cost per stage. We show that such problems can be embedded within the framework of Problem (D), which involves a stationary system and cost per stage. Consequently we are able to obtain in a simple manner results for nonstationary problems that are analogous to those for the stationary case. 
6.1 Convergence and Existence Results 
Consider for every positive integer N the following N-stage problem obtained from the infinite horizon problem defined earlier by means of truncation. This problem is to find a policy nN = { p o ,  pl, . . . , p N -  1} with pk(Xk) E u(xk), vxk E S that minimizes 
(4) 
subject to the system equation constraints. The optimal value of this problem 
I N- 1 
J,,(XO) = E { k50 akg[xk 9 pk(xk), w k l  
Wk 
k = O ,  1. .... N - 1  
226 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
for each initial state x o  is denoted J$(xo)  and is given by (cf. Chapter 2, Problem 6 )  
J$(xO) = J N ( X O ) ,  ( 5 )  
where for every N ,  J N ( x O )  is given by the Nth step of the algorithm 
J , ( x )  = 0 V X E S  (6) 
V X E S ,  k = 0 , 1 ,  . . . ,  N - 1 .  (7) 
The expectation above is, of course, taken with respect to the given dis- tribution P( 9 Ix, u), which depends on x ,  u.  
Notice that in the DP algorithm (6) and (7) we have reversed the indexing of the optimal value functions so that now the algorithm proceeds from lower to higher values ofindices k in contrast with finite horizon algorithms. We have also dropped time indices where they are redundant due to stationarity. These notational conventions are convenient for infinite horizon problems and will be adopted throughout the remainder of the text. 
WeshallalsodenoteforanyfunctionsJ: S -+ R, p :  S + C w i t h p ( x ) ~  U ( x ) ,  
V x  E S ,  for which the expected values below are well defined : 
T ( J ) ( x )  = inf E { g ( x ,  u, w) + ~ J [ f ( x ,  u, w)l) ,  (8) 
T , ( J ) ( x )  = E { S C X ,  A x ) ,  w l  + aJCf(x9 A x ) ,  411. (9) U E U ( X )  w 
W 
In these relations T ( J ) ( .  ) and T,(J)( - ) are functions defined on the state space S ,  and T, T, may be viewed as mappings that transform a function J on S into another function [T(J)  or T,(J)]  on S .  In terms of the notation above algorithm (6) and (7) can be written 
Jo(x)  = 0, (10) 
J k ( x )  = T k ( J o ) ( x ) ,  (11) 
T k ( J ) ( x )  = T [ T k - ' ( J ) ] ( x ) ,  
k = 0, 1, .  . . , 
where T k  is defined for all k and J :  S -+ R by 
TO(J) = J ,  
i.e., T k  is the composition of the mapping Twith itself k times. We have the following lemma. 
Lemma 1 For any bounded functions J :  S + R, J' : S + R, such that 
J ( x )  < J' (x)  V X E S ,  
6.1 CONVERGENCE AND EXISTENCE RESULTS 227 
and for any function p :  S + C with p(x )  E V ( x ) ,  Vx E S we have 
T k ( J ) ( x )  < Tk(J‘ ) (x )  T ; ( J ) ( x )  < T;(J’)(x) 
VX E S,  V X  E S ,  
Proof For any x ,  u, w we have J [ f ( x ,  u, w)] < J ‘ [ f ( x ,  u, w)], from which we obtain 
k = 0, 1, . . . , 
k = 0, 1 ,  . . . . 
E Mx, u, w) + uJCf(x ,  u, w)lI  < E M x ,  u, w) + d ’ C f ( x ,  u, w)X. 
From this relation we obtain T ( J ) ( x )  < T(J’ ) (x ) ,  Vx E S by taking the in- fimum of both sides with respect to u E U(x) ,  and the first inequality is proved fork  = 1. Similarly, it is proved for all k. A similar argument proves also the second inequality. Q.E.D. 
W W 
For any two functions J :  S + R ,  J ’ :  S + R ,  we write 
J < J’ if J ( x )  < J’(x)  Vx E S .  
With this notation Lemma 1 is stated as 
J < J‘* Tk(J) < Tk(J’), k = 1, 2 , .  . . , 
k = 1 ,  2 , .  . . . J < J’* T;(J) < T;(J’), 
Denote also by e :  S + R the function taking the value 1 identically on S :  
e (x)  = 1 Vx ES. (12) 
(13) 
(14) 
The following proposition shows that the optimal value function JN(xO)  of the N-stage truncated problem converges to the optimal value of the infinite horizon problem. Not only that, but the proposition goes further and shows that the DP algorithm (6) and (7) and (10) and (11) converges to the optimal value function J* o f  the infinite horizon problem for an arbitrary bounded starting function J ,  . 
Proposition 1 (Convergence of the DP Algorithm) The optimal value function J* of Problem (D) satisfies 
(15) 
where M is the upper bound in (3). Furthermore, for any bounded function J :  S + R there holds 
We have from (8) and (9) for any function J : S -, R and any scalar I’. 
T(J + re) (x)  = T ( J ) ( x )  + ur 
T,(J + re) (x)  = T,(J)(x) + ur 
Vx E S ,  
Vx E S .  
0 < J*(x)  < M/(1 - a) vx E s, 
J*(x) = lim T k ( J ) ( x )  Vx E S. (16) k- 00 
228 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Proof From (3) we have for any initial state X E S  and every policy { P O ?  P l ? .  . .I ,  
By taking infima over {po ,  pl, . . .} of both sides, 
J*(x) < JN(x) + [aN/( 1 - a)]M VX E S, N = 0, 1, . . . , 
where JN is defined for all N by (6) and (7) [or (10) and (1 l)]. By combining this relation with (6) we obtain (15). Also in view of (3), 
JN(X) < J*(x) vx E S .  
Combining the two inequalities above we obtain 
J*(x) = lirn JN(x) VX E S. (17) N+ m 
Now for an arbitrary bounded function J :  S + R let r be a scalar such that 
( J  - re)(x) < 0, ( J  + re)(x) 2 0, Vx E S ,  
where e is the unit function defined by (12). We have by Lemma 1, 
Tk(J - re)(x) < Jk(X) < Tk(J + re)(x) Vx E S ,  (18) 
and by (13) 
Tk(J + re)(x) = Tk(J - re)(x) + 2akr = Tk(J)(x) + akr 
Taking superior and inferior limits in (18) and using (17) we obtain 
VXES. (19) 
lirn sup T ~ ( J  - re)(x) < J*(x) < lim sup T ~ ( J  + re)(x), 
k+m k+m 
(20) lim inf Tk(J - re)(x) < J*(x) < lirn inf Tk(J + re)(x). 
k+w k+m 
On the other hand from (19) we have 
lim sup Tk(J - re)(x) = lim sup Tk(J + re)(x) = lim sup Tk(J)(x), 
k+m k+ m k - a ,  
lim inf Tk(J - re)(x) = lim inf Tk(J + re)(x) = lirn inf Tk(J)(x). 
k -  m k+  m k + m  
Using the above relations in inequalities (20) we obtain 
J*(x) = lim sup Tk(J)(x) = lim inf Tk(J)(x) k - m  k+  m 
and hence J*(x) = lim Tk(J)(x) Vx E S. Q.E.D. 
k+m 
6.1 CONVERGENCE AND EXISTENCE RESULTS 229 
Now given any stationary policy 71 = {p, p, . . .} where p: S -+ C with p ( x )  E U(x) ,  Vx E S, we can consider the problem that is the same as Problem (D) except for the fact that the control constraint set contains only one element for each state x, the control p(x) ,  i.e., a control constraint set of the form 8(x) = { p ( x ) } ,  Vx E S .  Clearly this problem falls within the frame- work of Problem (D) and since there is only one admissible control law (the policy {p, p, . . .}) application of Proposition 1 yields the following corollary: 
Corollary 1.1 The value J,(x) of the cost functional (2) corresponding to an admissible stationary policy {p, p, . . .} when the initial state is x satisfies 
0 I J,(x) I M/(1 - a). (21) 
J,(x) = lim Ti(J)(x) Vx E S. (22) 
Furthermore, for any bounded function J :  S -+ R there holds 
k-+m 
The next proposition shows that the function J* is the unique solution of a certain functional equation. This equation provides the means for obtaining a stationary optimal control law. 
Proposition 2 (Optimality Equation-Necessary and Sufficient Con- dition for Optimality) The optimal value function J* satisfies 
J * ( x )  = inf E {g(x, u, w) + a J * [ f ( x ,  u, w)]} Vx E S (23) UPU(X)  w 
or equivalently 
Furthermore, J* is the unique bounded solution of the above functional equation. In addition, if p* : S -+ C is a function such that p*(x)  E U(x) ,  Vx E S, and p * ( x )  attains the infimum in the right-hand side of (23) for each x E S, then the stationary policy {p*, p*, . . .} is optimal. Conversely if {p*, p*, . . .} is an optimal stationary policy, then p*(x)  attains the infimum in the right-hand side of (23) for all x E S. 
Proof Let J o  be the function that is identically zero on S [Jo(x)  = 0, Vx E S]. We have by (3) and (6),  (7) [or (10) and (1 l)] 
J*(x )  = T ( J * ) ( x )  vx E S. 
J ~ ( x )  < T(JO)(x)  < ... < Tk(J0) (x )  < Tk+' (J0) (x )  d . * *  < J*(x)  VX ES. 
Hence for all k and x E S, 
Tk"(Jo) (x)  = inf E { g ( x ,  u, w) + aTk(Jo)[ f (x,  u, w)]) U € U ( X )  w 
d inf E {g(x, u, w )  + a J * [ f ( x ,  u, w)]}. U S U ( * )  w 
230 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Taking the limit as k -, m and using (16) we obtain 
J*W < inf E { g ( x ,  u, w) + crJ*[f (x ,  u, w ) ] } ,  (24) U€U(X) w 
or equivalently 
J*(x)  < T(J*)(x)  vx E s. (25) 
It follows from (25) that 
J*(x )  d T(J*)(x)  6 T2(J*) (x )  < . . * < Tk(J*)(x)  d Tk"(J*)(x) d . . . . 
By taking the limit as k -+ m and using limk+m Tk(J*) (x )  = J*(x)  (Prop- osition l), we obtain 
J*(x)  < T ( J * ) ( x )  < . ' .  < Tk(J*)(x)  < . . . d J*(x) .  
Hence J * ( x )  = T(J*)(x) .  
solutions of (23) we would have for all k To show uniqueness simply observe that if JT,  JT were two bounded 
JT(x)  = Tk(JT)(x), J t ( x )  = Tk(JT)(x) vx E s. 
By Proposition 1, however, we have 
lim Tk(J:)(x)  = lim Tk(JT)(x) = J*(x) Vx E S.  k-m k - a ,  
Hence J :  = J :  = J* .  In order to prove the last part of the proposition let us state the following corollary, which follows from the part of Proposition 2 already proved by the same reasoning we used to obtain Corollary 1.1 from Proposition 1. 
Corollary 2.1 Let {p, p, . . .} be an admissible stationary policy. Then 
Furthermore, J ,  is the unique bounded solution of the above functional equation. 
Now if p * ( x )  minimizes the right-hand side of (23) for each x E S,  then we have for all x E S ,  
J*M = E {SCX, P* (X) ,  w l  + aJ*Cf(x, P * ( X ) ,  w)l>. W 
Hence by the uniqueness part of the corollary we must have J*(x)  = J,.(x) for all x E S.  and it follows that {p* .  p*.  . . .} is optimal. Also if {p* .  p*, . . .} is optimal, then we have J* = J,* and from the corollary J,. = TJJ,.). Hence J* = T,,(J*), which implies that p*(x)  attains the infimum in (23) for all x E S.  Q.E.D. 
6.1 CONVERGENCE AND EXISTENCE RESULTS 231 
Note that Proposition 2 implies the existence of an optimal stationary policy when the infimum in the right-hand side of (23) is attained for all x E S.  On the other hand, if the infimum is not attained, there arises the question whether one may approximate as closely as desired the optimal value J*(x)  corresponding to an initial state x by employing a stationary policy. The answer is affirmative (see Problem 12). 
We finally show the following relation, which holds for any bounded 
function J : S + R : 
SUP I T k ( J ) ( x )  - J*(x )  I < ak S U ~  I J ( x )  - J*(x)  1 ,  k = 0, 1, . . . . 
X E S  X E  
This relation is a special case of the following result: 
Proposition 3 For any two bounded functions J :  S + R, J’: S -, R, 
and for all k = 0, 1, , . . there holds 
y g  ITk(J)(x) - Tk(J’)(x)(  < Olk su IJ(x) - J ’ ( x ) l .  
XE Y 
Proof It is sufficient to prove the result for k = 1 since repeated use of the 
We have for any x E S ,  u E U(x) ,  inequality with k = 1 yields the desired result. 
E M X ,  u, w) + aJ[I f (x ,  4 w)l> = E { d x ,  4 w) + d ” f ( x ,  u, w)l> W W 
+ a E { J C f ( x ,  u, w)l - J ” f ( x ,  4 w)l )  
W 
< E M x ,  4 w) + aJ’Cf(x,  4 411 W 
+ a su IJ(x) - J’(x) l .  
X E  g 
Taking the infimum of both sides over u E U(x) ,  we obtain 
T ( J ) ( x )  - T(J’ ) (x )  < a sug IJ(x) - J’(x)l v x  E s. 
X E  
A similar argument shows that 
and hence 
I T ( J ) ( x )  - T ( J ‘ ) ( x ) )  < a sup IJ(x) - J’(x)I v x  E S .  
X € S  
By taking the supremum of the left side over x E S the result follows. Q.E.D. 
232 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
As earlier, we have 
Corollary 3.1 For any two bounded functions J :  S --* R, J’: S --* R, 
and any admissible stationary policy {p, p, . . .}, we have for all k = 0, 1, . . . , 
;y I Tk,(J)(x) - Tk,(J’)(x) I < tlk sup I J(x) - J’(x)  I .  
x o s  
The main conclusion from the propositions established earlier is that the optimal value function J* is bounded and is the unique bounded solution of the functional equation (23). This equation yields an optimal stationary control law provided the infimum in its right-hand side is attained. Further- more, the DP algorithm yields in the limit the function J* starting from an arbitrary bounded function J and the rate of convergence is at least as fast as the rate of a convergent geometric progression (Proposition 3). Thus the DP algorithm may be used for actual computation of at least an approximation to J*.  This computational method together with some additional methods will be further examined in the next section. The remainder of this section is devoted to two examples, in which we do not state explicitly that the dis- turbance space is countable. The conclusions and results obtained are rigorous only for a countable disturbance space. 
Asset Selling Example 
Consider the asset selling problem of Section 3.4. When the problem is viewed over an infinite horizon it is essentially a discounted cost problem with discount factor a = 1/( 1 + r )  [cf. Eq. (3.65)]. If we assume that the offers x are bounded, then the analysis of the present section is applicable and the optimal value function is the unique solution of the functional equation 
J * ( x )  = max[x, (1 + r1-l E {J*(w)}l. 
The optimal policy is obtained from this equation and has the following form. If current offer 2 (1 + r ) - ’  E ,  {J*(w)} = a, sell and otherwise do not sell.ThecriticalnumberE = (1 + r ) -  Ew {J*(w)}isobtainedasinSection3.4. 
W 
Component Replacement Example 
A certain component of a machine tool can be in any one of a continuum of states, which we represent by the interval [0, 13. At the beginning of each period the component is inspected, its current state x E [0, 13 determined, and a decision made whether or not to replace the component at a cost R > 0 by a new one at state x = 0. The expected cost of having the component at state x for a single period is C(x), where C( - ) is a nonnegative bounded and increasing function of x on [O, 11. The conditional cumulative probability 
6.1 CONVERGENCE AND EXISTENCE RESULTS 233 
distribution F(z1x) of the component being at a state less or equal to z at the end of the period given that it was at state x at the beginning of the period is known. Furthermore, for each y E [0, 13 we have 
1 
JlldF(zlxl) < S, dF(zlx2) for 0 < x 1  < x2 < 1. 
This assumption implies that the component tends to turn worse gradually with usage, i.e., for each y E [0, 11 there is greater chance that the component 
will go to a final state in the interval b, 11 when at a worse initial state. 
Assuming a discount factor a E (0, 1 )  and an infinite horizon, the problem is to determine the optimal replacement policy. 
Except for the countability assumption, the problem clearly falls within the framework of this section and the optimal value function J* is the unique bounded solution of the functional equation 
J*(z) dF(z(O) ,  C(x) + a 
An optimal replacement policy is given by: 
Replace if R + C(0) + a J*(z) dF(z  10) < C(x) + a J*(z) dF(z Ix). Jo Jo Do not replace otherwise. 
Now consider the DP algorithm 
Jo(x) = 0, 
T(Jo)(x) = min[R + C(O), C(x)], 
Since C(x) is increasing in x we have that T ( J o ) ( x )  is nondecreasing in x and in view of our assumption on the distributions F(z1x) the same is true for Tz(Jo)(x). Proceeding similarly it follows that Tk(Jo)(x) is nondecreasing in x and so is the limit 
J*(x) = lim Tk(Jo)(x). 
It follows under our assumptions that the function C(x) + a Jh J*(z) dF(z  I x) is nondecreasing in x. This is simply a reflection of the intuitively clear fact 
k -  w 
234 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
I R C(0) + a JOJ*(-J tlE’(zlOJ 
I I I I I - - 
0 I 
Do n o t  Replace replace 
_:* Y 
FIGURE 6.1 
that the optimal cost cannot decrease as the initial state increases, i.e., we start at a worse initial state. Thus an optimal policy takes the form 
Replace if x 2 x* Do not replace if x < x*, 
where x* is the smallest scalar for which 
R + C(0) + CI JolJ*(z) dF(zI0)  = C(x*) + ct 
as shown in Fig. 6.1. 
6.2 Computational Methods-Successive Approximation, Policy Iteration, Linear Programming 
This section presents three alternative approaches for solving the in- finite horizon, discounted cost Problem (D). In order that these approaches be implementable in a computer it is necessary that the state space and con- trol space be finite sets. When these spaces are infinite, it is necessary to replace them with finite sets by means of some discretization procedures. A dis- cretization procedure analogous to the one given in Section’ 5.2 may be employed (see Bertsekas [BlS] or Problem 2) and it possesses similar stability properties under analogous assumptions. The first approach, successive approximation, is essentially the DP  algorithm and yields in the limit the 
6.2 COMPUTATIONAL METHODS 235 
optimal value function and an optimal policy as discussed in the previous section. Some variations aimed at accelerating the convergence are discussed in addition. The other two approaches, policy iteration and linear program- ming, terminate in a finite number of iterations (when the spaces involved are finite sets). However, they require solution of linear systems of equations or of a linear program of dimension as large as the number of points in the state space. When this dimension is very large their practicality is questionable. 
Throughout this section we shall assume that the spaces S ,  C ,  and D in Problem ( D )  are Jinite sets. Under these circumstances, Assumption B can be made to hold by adding a suitable constant tog if necessary. When Sand D are finite, the problem becomes one of control of a finite state Markov chain, and for this case one can represent the mappings T and TP of (8) and (9) in a standard form, which is perhaps more convenient both from the point of view of conceptual understanding and from the point of view of computation. 
Let S consist of n states denoted by 1,2, . . . , n :  
S = {1,2, ..., n } .  
Let us denote by piJ(u) the transition probability: 
pij(u) = P(xk+l = j l x k  = i ,  uk = u)  V i , j E S ,  U E  U(i). 
Thus pij(u) is the probability that the next state will be j given that the current state is i and control u E V ( i )  is applied. These transition probabilities may either be given a priori or they may be calculated from the system equation 
x k +  1 = f ( x k ,  u k ,  w k )  
and the known probability distribution P( * Ix, u )  of the input disturbance wk. Indeed, we have 
p i j (u )  = PCWju) I i ,  u l ,  where Wju)  is the (finite) set 
w. ju)  = { w  E D I f ( i ,  u, w )  = j } .  
Now let us use the notation 
a(i, u )  = E {g(i ,  u, w)} V i  E S ,  u E U(i), W 
where the expectation is taken with respect to the given probability dis- tribution P( - I i ,  u). Then the basic expression 
E {g(i ,  u, w)  + crJ[f(i ,  u, w ) ] }  V i  E S W 
236 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
may be written in terms of p&) and g as n 
~ ( i ,  u ) + a 1 p i j ( u ) ~ ( j )  ~i E S .  
j= 1 
As a result the mappings Tand T, of (8) and (9) can be written for any function J : S - + R a s  
n 
These expressions are often convenient to work with. Notice that the func- 
tions J, T,(J): S -, R, may be represented by the n-tuples (or n-dimensional 
vectors) of their values J(l), . . . , J(n), T,(J)(l), . . . , T,(J)(n) 
J =  
If for a p :  S + C with p(i) E U(i), i = 1, . . . , n, we form the transition prob- 
ability matrix 
- 1  ~1 1 b(1)l . . . plnC/41)1 
p.1 CAnll . . . ~ n n C ~ ( n ) l  
and consider the n-dimensional vector g, defined by 
BCn, d n ) l  then we can write in vector notation 
T, (J )  = a, + aP, J. The value function J, corresponding to a stationary policy {p ,  p, . . .} is 
by Corollary 2.1 the unique solution of the equation 
J, = T,(J,) = 8, + aP, J, . Hence for any admissible stationary policy {p, p, . . .} the corresponding 
6.2 COMPUTATIONAL METHODS 237 
function J, may be found as the unique n-dimensional vector that solves the system of n linear equations 
( I  - aP,)J, = g P ,  
or equivalently 
J, = (I - uP,)-'g,, 
where I denotes the n x n identity matrix. The invertibility of the matrix 
I - UP,, is assured since we have proved that the system of equations re- 
presenting the equation J, = T,(J,) has a unique solution for any possible value of the vector Q,, (cf. Corollary 2.1). 
Successive Approximation 
Here we start with an arbitrary bounded function J: S -, R and succes- 
sively compute T(J), Tz(J) ,  . . . , where the mapping T is defined by (8). By 
Proposition 1 we have 
lim Tk(J)(x) = J*(x) Vx E S.  k + m  
Furthermore by Proposition 3, IJ*(x) - Tk(J)(x)l is bounded by a multiple 
of a geometric progression for all x E S. It is also of interest to note that the successive approximation method will yield an optimal policy after a finite number of iterations (see Problem 14). The successive approximation scheme can be considerably sharpened and improved by taking advantage of the special structure of the problem as we describe below. 
Suppose that we have computed J, T(J), T2(J), .. . , Tk(J). The following proposition provides upper and lower bounds for J*, which are obtained from J, T(J), . . . , Tk(J). These bounds converge monotonically to J*. 
Proposition 4 Let J :  S + R. Then for all x E Sand k = 0, 1, . . . , 
Tk(J)(x) + c k  < Tk"(J)(x) + ck+l 
< J*(x) < Tk+'(J)(X) + z k + l  < Tk(J)(x) + z k ,  (26) 
where for all k = 0, 1,. . . , 
U 
Ek = - max[Tk(J)(x) - Tk-'(J)(x)]. 
1 - u X € S  
238 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Furthermore, the error bounds (26) are optimal in the following sense: 
ck+ = max{c 1 Tk(J)  + (c/a)e < T k +  ' ( J )  + ce < J * } ,  
Z k + l  = min{ElJ* < T k + l ( J )  + Ee 6 Tk(J)  + (i;/a)e}, 
(29) 
(30) 
where e is the unit function on S [e(x) = 1, Vx E S]. 
Proof Denote 
y = min[T(J)(x) - J ( x ) ] .  
X E S  
We have 
J + ye < T(J).  
Applying T to both sides, using the monotonicity of T and (1 3), 
T ( J )  + aye < T2(J),  
J + (I  + a)ye < T ( J )  + aye 6 T'(J) .  
T ( J )  + (a  + a2)ye < ~ ' ( 5 )  + d y e  < T3(J) ,  
(32) 
and because of (3 l), 
(33) 
This process can be repeated, first applying T to obtain 
(34) 
and then using (3 1) to write 
J + ( I  + a + a2)ye < T ( J )  + (a + a2)ye < T 2 ( J )  + a2ye < T3(J) .  (35) 
After k steps this results in the inequalities 
Taking the limit as k + 00 we obtain 
J + (cl/a)e < T(J)  + c l e  < T2(J)  + acle < J*, 
T k + l ( J )  + ck+le < J*, 
(37) 
where c1 is defined by (27). Replacing J by Tk(J)  in this inequality, we have 
which is the second inequality in (26). 
6.2 COMPUTATIONAL METHODS 239 
From (33) we have 
and consequently 
ac1 < c2. 
Using this in (37) yields 
and replacing J by T k -  '(J) we have the first inequality in (26). To prove (29) we replace J by Tk(J)  in (37) and obtain 
Tk(J) + (Ck+l/a)e < Tk+l(J) ck+le < J*, 
which implies that C k + l  is a member of the set on the right side of (29). If c is any other member of this set, we have 
c - - 1 < Tk+'(J)(X) - Tk(J)(x) VXES, (: ) 
and so 
1-Ci  1 - a  
c < min[Tk+l(J)(x) - Tk(J)(x)] = ~ c k +  1 3  a x c s  o! 
which shows c < ck+ '. 
The last two inequalities in (26) and Eq. (30) follow by an analogous 
argument. Q.E.D. 
Notice that the error bounds (26) may be easily computed as a by-product of the computations in the successive approximation method. In practice these bounds are extremely helpful and speed up the convergence con- siderably. Some properties of these bounds are given in Problem 7. Additional error bounds that are useful in successive approximation methods are given in Problems 3 and 4. 
We now consider a computational example that illustrates the utility of the error bounds of Proposition 4. 
EXAMPLE 1 Consider a problem where there are two states and two controls 
s = {1,2}, c = (u1, u'} .  
240 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
.% !A 
'*><I 
3 3 !A 
3 '><I .% 2 
(a )  ( b )  FIGURE 6.2 (a)u  = u ' . ( b ) u  = LI*.  
The transition probabilities corresponding to the controls u 1  and u2 are as shown in Fig. 6.2, i.e., we have the transition probability matrices 
The transition costs are as follows: 
and the discount factor is u = 0.9. The mapping T is given by 
2 
u ' )  + u 1 p,,{u')JG), 
j =  1 
2 
g(i, u') + u c pi,<u2)JG)}, i = 1,2. 
The scalars c k  and ?k of (27) and (28), respectively, are given by 
j =  1 
u 
ck = - min{Tk(J)(l) - Tk-'(j)(1), Tk(J)(2) - Tk-'(J)(2)}, 
I - u  
C? 
?k = - max{Tk(J)(l) - Tk-'(J)(l), Tk(J)(2) - Tk-'(J)(2)}. 1 - u  
The results of the successive approximation method starting with the zero function J o  [Jo(l) = J0(2)  = 01 are shown in Table 6.1 and illustrate the power and practicality of the error bounds. 
6.2 COMPUTATIONAL METHODS 241 
TABLE 6.1 
0 1 2 3 4 5 6 7 8 9 
10 11 12 13 14 15 16 17 18 
0.00000 0.5oooO 1.28750 1.84438 2.41391 2.89573 3.34321 3.73972 4.09937 4.42 180 4.71256 4.97398 5.20938 5.421 18 5.61183 5.78340 5.93782 6.07680 6.20188 
0.00000 1.00000 1.56250 2.22063 2.74459 3.24692 3.68517 4.08583 4.44362 4.76689 5.05727 5.3 1886 5.55418 5.76602 5.95665 6.12823 6.28265 6.42163 6.54670 
5.00000 6.35000 6.85625 7.12962 7.23214 7.28750 7.30826 7.31947 7.32367 7.32594 7.32679 7.32725 7.32743 7.32752 7.32755 7.32757 7.32758 7.32758 
9.50000 8.37500 7.76750 7.53969 7.41667 7.37054 7.34563 7.33628 7.33124 7.32935 7.32833 7.32794 7.32774 7.32766 7.32762 7.32760 7.32759 7.32759 
5 . 5 m  6.62500 7.23250 7.46031 7.58333 7.62946 7.65437 7.66372 7.66876 7.67065 7.67167 7.67206 7.67226 7.67234 7.67238 7.67240 7.67241 7.67241 
10.00000 8.65000 8.14375 7.87038 7.76786 7.71250 7.69 174 7.68053 7.67633 7.67406 7.67321 7.67275 7.67257 7.67248 7.67245 7.67243 7.67242 7.67242 
Another possibility for accelerating the convergence of the successive approximation method is to modify the basic mapping Tin the following way. 
Let us denote by 1,2,. . . , n the points of the state space S, i.e., 
s = {1,2 ) . . . )  n}. 
Given a function J: S + R ,  define the mapping F by 
v x  E s, F(J) (x )  = T,(J) (x)  
where the mapping T, is defined recursively by 
T,(J)(x)  = J ( x )  v x  E s, 
min E {g(x ,  u, w )  + aT(J) [ f ( x ,  u, w ) l }  
U E U ( X )  w 
if x = i +  1, 
T ( J ) ( x )  otherwise, T + I ( J M  = 
or equivalently 
T [ T ( J ) ] ( x )  if x = i + 1, otherwise. T +  , ( J ) ( x )  = 
(38) 
(39) 
242 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
In words, for the state x = i + 1 we have that T +  l(J)(i + 1) is obtained from T ( J )  by minimization over u as in (40), but for all states x # i + 1, we have T +  l(J)(x) = T(J)(x). The function F ( J )  is obtained from J after minimization has been carried out for every state. The difference with the computation of T(J)  is that at each new minimization the “current” function T ( J )  is used in (40) in place of J .  A moment’s reflection should convince the reader that the computation of F ( J )  is as easy as the computation of T(J). We may consider now the successive approximation method whereby we compute J ,  F(J), F2(J) ,  . . . . The following propositions show that the method is valid in the 
sense that Fk(J)(x) + J*(x) as k + co and in addition in many cases it is 
characterized by better convergence properties than the earlier method. 
Proposition 5 Let J: S -, R, J’: S -, R, be two bounded functions. 
Then for any k = 0, 1, . . . , 
max I F k ( ~ ) ( x )  - Fk(J’)(x)  1 < ak max I J(x) - J’(x) I. (42) 
x s S  xss 
Furthermore we have 
F(J*)(x) = J*(x) vx E s, (43) 
lim Fk(J)(x) = J*(x) Vx E S .  k -  w 
< a max I J(x) - J’(x) I .  
x s s  
Proceeding similarly we have for every i a n d j  d i, 
IT.(J)o’) - T(J”j)I d a maxIJ(x) - J’(x)l, 
and for i = n the above relation is equivalent to (42) for k = 1. Relation (43) follows immediately from definition (38)-(41) and the fact that J* = T(J*). Relation (44) follows immediately from (42) and (43). 
x s s  
Q.E.D. 
6.2 COMPUTATIONAL METHODS 243 
Proposition 6 If J :  S + R satisfies 
then 
T k ( J ) ( x )  < Fk(J) (x )  < J * ( x )  
Proof The proof is immediate by using definition (38)-(41) and the monotonicity property of T. Q.E.D. 
The preceding proposition provides the main motivation for employing the mapping F in place of T in the successive approximation method. A 
similar result may be proved for functions J : S + R satisfying J* < T ( J )  < J 
for all x E S. Additional results applicable to the mapping F and the related successive approximation method are given in Problems 3 and 4. We now provide a computational example. 
EXAMPLE 1 (CONTINUED) Consider the example examined earlier in this section. The mapping F is given by 
F(J)(i) = T2(J)(i), 
VX E S ,  k = 1,2, . . . . 
i = 1, 2, 
where 
I 2 2 
Tl(JI(1) = min g(1, u') + a 1 P~XU')JU) ,  g(1, u 2 )  + 
TI(Jl(2) = JP), 
T 2 ( J ) ( 1 )  = Tl(J)(l)? 
1 P l j ( u 2 ) J U )  7 { j =  1 j =  1 
2 2 
g(2, u') + a 1 P ~ ~ ( U ' ) T ~ ( J ) O ' ) ,  g(2, u 2 )  + j =  1 1 p 2 j ( u 2 ) T 1 ( J ) ~ ) } *  
j =  1 
One may show (Problem 3) that 
u2 < [F(J + re)(i) - F(J)(i)]/r < u, i = 1,2, r z 0, 
and thus by the result of Problem 3 we have the error bounds 
Fk(J)( i )  + ck < J*(i) < Fk(J)( i )  + ? k ,  i = 1,2, 
where 
244 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
TABLE 6.2 
0 2 4 6 8 
10 12 14 16 18 20 22 24 26 28 30 32 34 36 
0.00000 1.51531 3.16788 4.35204 5.19911 5.80504 6.23847 6.54852 6.77030 6.92895 7.04243 7.12361 7.18167 7.2232 I 7.25292 7.27418 7.28938 7.30026 7.30804 
0.00000 2.33373 3.84690 4.93594 5.7 1495 6.27219 6.67080 6.95594 7.15990 7.30580 7.41017 7.48482 7.53823 7.57643 7.60375 7.62330 7.6 3 7 2 8 7.64728 7.65444 
5.71995 6.14207 6.47943 6.72088 6.89359 7.01 7 14 7.10552 7.16874 7.21396 7.24630 7.26944 7.28600 7.29784 7.30630 7.3 1236 7.3 1670 7.31980 7.32201 
10.65312 9.99341 9.23554 8.69239 8.30387 8.02594 7.82714 7.68493 7.58320 7.51043 7.45838 7.42115 7.39451 7.37546 7.36183 7.35208 7.3451 I 7.34012 
6.52841 6.82109 7.06332 7.23672 7.36075 7.44947 7.5 1294 7.55834 7.5908 1 7.61404 7.63066 7.64255 7.65105 7.65713 7.66148 7.66479 7.66682 7.66841 
11.46159 10.67243 9.8 1943 9.20823 8.77102 8.45827 8.23456 8.07453 7.96006 7.87817 7.8 1960 7.77370 7.74773 7.72629 7.71095 7.69998 7.692 13 7.68652 
The results of the successive approximation method starting with the zero function J o  [Jo(l) = J0(2) = 01 are shown in Table 6.2. 
A comparison of Tables 6.1 and 6.2 reveals that the values Fk(Jo)(l) and Fk(Jo)(2) converge to J*(l) and 5*(2) faster than Tk(Jo)(l) and Tk(Jo)(2) as predicted by Proposition 6. However, the error bounds Fk(Jo)(i) + ck and Fk(Jo)(i) + converge much slower than the corresponding error bounds Tk(Jo)(i)  + ck and Tk(Jo)(i) + Ek.  Thus the faster convergence property of the mapping F is counterbalanced by the fact that the corresponding error bounds are not as tight as those associated with the mapping T. This disadvantage may be somewhat rectified by changing the successive approximation iteration so that instead of operating with F on the current iterate function, say J k ,  we operate on the average of the error bounding functions, i.e., by considering the iteration 
where 
6.2 COMPUTATIONAL METHODS 245 
TABLE 6.3 
0 1 2 3 4 5 6 1 8 9 
10 1 1  12 13 14 15 
0 . m  0.00000 7.58454 8.42204 8.31052 8.70017 1.24195 7.52229 7.19141 7.54122 7.34007 7.69411 7.3441 7 1.6888 1 1.32590 7.66956 7.32545 7.67038 7.32780 1.67277 1.32185 7.61366 7.32156 7.67231 7.32755 7.67238 7.32759 7.67242 1.32159 1.61242 1.32759 7.67241 
2.63 158 6.08192 6.12606 6.85185 7.28071 7.29913 1.31888 1.31973 7.32695 1.327 I4 7.32746 1.32747 1.32758 1.32158 7.32758 
12.53150 10.65312 7.76983 1.53098 7.39936 1.38982 1.33292 1.331 17 7.32865 7.32856 1.32766 1.32164 1.32760 7.32760 1.32159 
3.46908 6.41 8 17 l.Oo040 7.20165 7.63482 7.64316 7.66255 7.66466 1.61 193 1.61195 7.61221 7.61229 1.67241 1.61241 7.61241 
13.31500 10.98338 8.04418 1.88019 7.75341 1.73386 1.61658 7.6761 1 1.61362 1.67338 1.61241 7.67247 1.61243 1.61243 7.61241 
and J o  is arbitrary. The results of the computation for Jo(l) = J0(2 )  = 0 are given in Table 6.3 and are considerably more favorable than those of Table 6.2. These computational results, however, are far too limited in scope to allow any general conclusions. Note that a similar modification of the succes- sive approximation method based on the mapping T does not lead to any improvement, as Problem 7 shows. 
The Policy Iteration Algorithm 
The policy iteration algorithm (otherwise called policy improvement algorithm) operates as follows. An initial admissible stationary policy no = {po, po, . . .} is adopted and the corresponding value function J p o  = J,, is calculated. Then an improved policy n' = { p l , p l ,  ...} is computed, resulting in a decrease of the value of the cost, and the process is repeated. 
The algorithm is based on Corollary 2.1 of Section 6.1 as well as the following proposition. 
Proposition 7 Let n = {p, p,  . . .} be an admissible stationary policy and J,(x)  = J,(x) be the corresponding value of the cost functional (2) when 
the initial state is x. Let 11: S + C,  p(x) E V(x), Vx E S, be a function satisfying 
EkICXl iw, w l  + LyJ,Cf(x, m, 411 
W 
= U E U ( X )  min E w M X ,  u, w) + LyJ,Cf(x, u, w)11. (45) 
246 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Then if J, (x)  is the value of the cost corresponding to X = {p, ,ii, .. .} when the 
initial state is x, we have 
J p ( x )  < J, (x)  V X E S .  (46) Furthermore, if the policy n is not optimal, strict inequality holds in (46) for at least one state x E S .  
Proof From Corollary 2.1 and (45) we have for every x E S ,  
J , (x)  = E {SCX, Ax), wl + uJ,Cf(x, PW. w)N W 
2 E{sCx, li(x), WI + mJ,Cf(x, iw, W)l} = Tp(J,)(x). 
W 
Applying repeatedly T, on both sides of the above inequality and using the monotonicity of and Corollary 1.1, we obtain 
J ,  3 T,(J,) > . . . > T ~ ( J , )  > . 2 lim T ~ ( J , )  = J , ,  k + m  
proving (46). If J ,  = J , ,  then from the inequality above we have J ,  = T,(J,) and from (45) we have T,(J,) = T(J,), so that J ,  = T(J,) and hence J ,  = J* by Proposition 2. Hence n = {p, p, . . .} must be optimal. It follows that strict inequality holds in (46) for some x E S if n: is not optimal. Q.E.D. 
Policy Iteration Algorithm 
Step  1 Guess an initial admissible stationary policy no = { P O ,  po, . . .}. 
n' = {pi, pi, . . .}, 
Step 2 Given the admissible stationary policy 
compute the corresponding value function J,,(x) using the successive approximation algorithm or the linear system of equations 
(I - uP,,)J,, = g,,, 
as described in the beginning of this section. 
If JPt = J P x - , ,  stop-n' is optimal. 
Step 3 Obtain a new admissible policy n'" = {pi+', pi+', . . .} sat- isfying for all x E S 
E {SCX, Pi+ l(X), wl + uJ,,Cf(x, Pi+ l(x), w)l> W 
= min E { g ( x ,  u, w) + cd,iCf(x, U, w)]} = T(J,i)(x). U € U ( X )  w 
Return to Step 2 and repeat the process. 
6.2 COMPUTATIONAL METHODS 247 
Since the collection of all possible stationary policies is a finite collection (by the finiteness of S and C) and an improved policy is generated at every iteration, it follows that the algorithm will find an optimal stationary policy in a finite number of iterations and thereby terminate. This property of the policy iteration algorithm is its main advantage over successive approxi- mation, which in general converges in an infinite number of iterations. On the other hand, finding the exact value of J,, in Step 2 of the algorithm requires solution of the system of linear equations representing J P i  = Tpi(JPi). The dimension of this system is equal to the number of points of the state space S and thus when this number is very large the method is not very attractive. 
We note that when the successive approximation method is used for carrying out Step 2 we may utilize error bounds similar to those described earlier in this section. We note also that one may construct a generalized policy iteration algorithm for the case where S ,  C ,  and D are not necessarily finite sets (see Problem 13). 
We now demonstrate the policy iteration algorithm by means of the example considered earlier in this section. 
EXAMPLE 1 (CONTINUED) 
Step 1 Let us select an initial policy no = ( p a ,  po,  . . .}, where 
pO(1) = u l ,  pO(2) = u2. Step 2 We obtain J p 0  through the equation J , ,  = T,o(J,o) or equivalently 
J,o(l) = g(1, u ’ )  + ~P,,(u’)J,o(l) + “P12(u1)J,o(2), J,@) = g(2, u2) + ap21(u2)J,o(l) + ap22(u2)J,0(2). 
Substituting the data of the problem, J ,o ( l )  = 2 + 0.9 x $ x J , o ( l )  + 0.9 x a x J,0(2), Jp(2) = 3 + 0.9 x 4 x J ,o( l )  + 0.9 x $ x J,0(2). 
Solving this system of linear equations for Jp0(l), JMO(2) we obtain J , o ( l )  N 24.12, J,0(2) 25.96. 
Step 3 We now find pl(l), p’(2) satisfying T, , (Jv0 )  = T(JPo).  We have T(JMo)(l) = min(2 + 0.9($ x 24.12 + x 25.96), 
0.5 + 0.9($ x 24.12 + = min(24.12, 23.45) = 23.45, 
T(JPo)(2) = min(1 + 0.9($ x 24.12 + 4 x 25.96), 3 + 0.9(4 x 24.12 + $ x 25.96)) 
x 25.96)} 
= min(23.12,25.95} = 23.12. 
248 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
The minimizing controls are 
p('(1) = U2, p'(2)  = U1. 
Step 2 We obtain JP1 through the equation JPI = TP1(JP1): 
JJl) = gu, UZ) + @Pll(UZ)JP1(1)  + @P,Z(UZ)J,1(2), 
JJ2) = g(2,  U') + @PZl(U1)JpI (1 )  + @PZZ(U1)JpI(2). Substitution of the data of the problem and solution of the system of equa- tions yields 
Step 3 
J,,i(l) N 7.33, J,1(2) N 7.67. We perform the minimization required to find T(J,I): 
T(JPI)(1) = min(2 + 0.9($ x 7.33 + $ x 7.67), 0.5 + 0.9(* x 7.33 + 2 x 7.67)) 
= min(8.67, 7.33) = 7.33, T(JP1)(2) = min{ 1 + 0.9($ x 7.33 + $ x 7.67), 
3 + 0.9($ x 7.33 + 2 x 7.67)) = min(7.67. 9.83) = 7.67. 
Hence we have JPI = T(JP1),  whichimplies that {p', p', . . .} is optimal and J,i = J * :  
p*(l) = u', p*(2) = u', J*(1) N 7.33, J*(2) N 7.67. 
Linear Programming 
As discussed earlier we have J < T(J)  = J Q J* = T(J*). 
Thus if we denote by 1,2, .  . . , n the elements of the state space S ,  it is clear that J*( l), . . . , J*(n) solve the following maximization problem (in A', . . . , An): 
n 
max C Ai i =  1 
subject to jli < T(JJ(i), i = 1 , .  . ., n, 
where the function J A :  S -, R is defined by 
Ja(i) = A i ,  i = 1, . . . , n. 
If we denote by ul, uz, . . . , urn the elements of the control space, the problem above is written 
n 
max 2 jli 
i =  1 
6.3 CONTRACTION MAPPINGS 249 
subject to 
Ai Q E {g(i, uk, w) + crJn[f(i, uk, w)] I i ,  uk} ,  i = 1, . . . , n, uk E V(i). W 
Using the notation given in the beginning of this section this linear program may be written in terms of transition probabilities p&) as 
n 
max 1 ii 
i =  1 
subject to n 
ii Q g(i, uk)  + cr 1 pi j (uk)I j ,  i = 1,2,. . . , n, uk E U(i)  
j =  1 
This is a linear program with n variables and as many as n x m constraints. As n increases, its solution becomes more complex and for very large n and m (in the order of several hundreds) the linear programming approach becomes impractical. 
For the example considered in this section the linear programming prob- lem above takes the form 
maximize A l  + I ,  
subject to I1 Q 2 + 0.9($I, + *I,), 1, Q 1 + o.9($A1 + +A,), 
I1 < 0.5 + o.9($A1 + $A,), A, Q 3 + 0.9(+A1 + $1,). 
6.3 Contraction Mappings 
In this section we introduce the notion of a contraction mapping on the space of all bounded functions over the state space S.  A basic fact about such mappings is that they possess a unique fixed point-a classical result of analysis. Furthermore the fixed point may be found in the limit by successive application of the mapping on any bounded function over S ,  i.e., by a method of successive approximation. It turns out that the mappings 17; T,, and F considered in the past two sections [cf. (8), (9), (38)-(41)] are contraction mappings and that the corresponding results that we proved draw essentially their validity from the contraction property together with the monotonicity property of Lemma 1. 
The connection with the theory of contraction mappings is very valuable from both the conceptual and the practical points of view. This is particularly so since it turns out that the contraction and monotonicity properties are present in several dynamic programming models other than Problem (D) and by themselves guarantee the validity of results and algorithms similar to 
250 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
those obtained in the past two sections. The corresponding theory is developed in some detail in Problem 4. Here we present only the notion of a contraction mapping and show that some of our earlier results concerning Problem 1 are special cases of a general result on fixed points. 
Let B(S) denote the set of all bounded real-valued functions on S. With 
every function J: S + R that belongs to B(S) we associate the scalar 
(For the benefit of the advanced reader we mention that the function 11 - 1) may be shown to be a norm on the linear space B(S) and with this norm B(S) becomes a complete normed linear space, i.e., a Banach space [R5]). The following definition and theorem are specializations to B(S) of a more general notion and result (see, e.g., references [L5] and [L8]). 
Definition A mapping H: B(S) + B(S) is said to be a contraction 
mapping if there exists a scalar p < 1 such that 
IIHW - H(J')ll < PIIJ - J'IL V J ,  J'E B(S), 
where ( 1  - 1) is as in (47). It is said to be an m-stage contraction mapping if there exists a positive integer m and some p < 1 such that 
IIH"'(J) - H"'(J')II < pIlJ - J'IJ, V J ,  J' E B(S), 
where H"' denotes the composition H . . . H of H with itself m times. 
The main result concerning contraction mappings is as follows. 
Contraction Mapping Fixed Point Theorem If H :  B(S) + B(S)  is a 
contraction mapping or an rn-stage contraction mapping, then there exists a unique fixed point of H, i.e., there exists a unique function J* E B(S) such that 
H(J*)  = J*. 
Furthermore, if J is any function in B(S) and H k  is the composition H . . Hof H with itself k times, then 
lim IIHk(J) - J*(I = 0, 
k-cu  
i.e., the function H k ( J )  converges uniformly to the function J*. 
Proof See reference [L5] or [L8]. 
Now consider the mappings T and defined by (8) and (9). Proposition 3 and Corollary 3.1 show that T and Tp are contraction mappings ( p  = a). As a result, the fact that the successive approximation method converges to the unique fixed point of T follows directly from the contraction mapping 
6.4 UNBOUNDED COSTS PER STAGE 251 
theorem. Notice also that by Proposition 5, the mapping F defined by (38)- (41) is also a contraction mapping with p = a and the convergence result of Proposition 5 is again a special case of the fixed point theorem. 
Several additional results on contraction mappings of the type considered in DP  are pointed out in the problem section (Problem 4). In particular, the computational methods of the previous section are special cases of more general procedures that are applicable to such contraction mappings. 
6.4 Unbounded Costs per Stage 
In this section we consider Problem (D) but relax Assumption B by allow- ing costs per stage that are unbounded above or below. The complications resulting from relaxation of the boundedness assumption are substantial and the analysis required is considerably more sophisticated than the one under Assumption B. The main difficulty is that Proposition 1 and the results that depend on it need not be true anymore. We shall assume that one of the following two assumptions is in effect in place of Assumption B. 
Assumption P (Positivity)? The function g in the cost functional (2) satisfies 
V(x, u, w) ES x C x D. (48) 
Assumption N (Negativity) The function g in the cost functional (2) 
V(x, u, w) E S  x C x D. 
0 d g(x, u, w) 
satisfies g(x, u, w) d 0 (49) 
In problems where reward or utility per stage is nonnegative and total discounted expected reward is to be maximized, we may consider minimiza- tion of negative reward thus coming within the framework of Assumption N. 
It is to be noted that (48) could be replaced by 
M < g(x, u, w) 
while (49) could be replaced by 
g(x, u, w) < M 
V(x, u, w) E S x C x D, 
V(x, u, w) E S x C x D, 
where M is some scalar. When g is either bounded above or below we may add a scalar to g so that either (48) or (49) is satisfied. An optimal policy will not be affected by this change since, in view of the presence of the discount factor, 
t Problems corresponding to Assumption P are sometimes referred to in the research literature as negative DP problems [S17]. In these problems the objective function is maximized and the reward per stage is negative. Similarly problems corresponding to Assumption N are sometimes referred to as positive DP problems [B21, S171. 
252 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
the addition of a constant r tog merely adds (1 - a)- l r  to the cost associated 
with every policy. 
One complication arising from allowing unbounded costs per stage is that the value J,(xo) of the cost functional (2) for some initial states xo and some admissiblepoliciesn = {po ,  pl, . . .}may be + co (in thecaseofAssumptionP) 
or - co (in the case of Assumption N). Consider the following simple example. 
EXAMPLE Let the system equation be 
xk+l = pxk + uk, k = 0, 1, 2 , .  . ., 
where xk, u k  E R ,  k = 0, 1, . . . , and f i  is a positive scalar. The control con- 
straint is l U k l  < 1, i.e., U(X) = { u l l u l  < I}. Consider the cost functional 
N- 1 
J , (X~) = lim C ctk(Xkl, 
where a < 1 is the discount factor. Consider the policy it = {PIP, .. .}, where P(x) = 0 for all x E R.  Then 
N + m  k = O  
N- 1 
and hence J,(xo) = co if xo # 0, afi 2 1, 
and J5(xo) is finite otherwise. It is also.possible to verify that when afi 2 1 the optimal value J*(xo)  is equal to + 00 for Ixo 1 > l/(fi - 1) and is finite for Ixol < 1/(B - 1). 
We shall conduct our analysis with the notational understanding that the cost J,(x,)corresponding to an initial state xo and a policy n or the optimal cost J*(xo) corresponding to an initial state xo may take the values + co or 
- co (depending on whether we operate under Assumption P or N). In other 
words, we consider J,( - ), J*( - ) to be extended real-valued functions. 
The results to be presented provide characterizations of the optimal value function J* as well as optimal stationary policies. They also provide con- ditions under which the successive approximation method yields in the limit the optimal value function J*. In the proofs we shall often need to inter- change expectation and limit in various relations. This interchange is valid under the assumptions of the following theorem. 
Monotone Convergence Theorem Let P = (pl, p z  , . . .) be a probability 
distribution over a countable set S denoted by S = { 1,2, . . .}. Let { h N }  be a sequence of extended real-valued functions on S such that 
Vi,  N = 1 ,  2 , .  . . . 0 < hN(i) < l~N+~(i)  
6.4 UNBOUNDED COSTS PER STAGE 253 
Let h:  S + [0, + a] be the limit function 
h(i) = lim hN(i). N+m 
Then 
Proof We have m m 
By taking the limit, we obtain W m 
so that it remains to prove the reverse inequality. Now for every integer M 2 1 we have 
m M M 
and by taking the limit as M -+ co the reverse inequality follows. Q.E.D. 
Optimality Equation-Conditions for Optimality 
Proposition 8 Under either Assumption P or N the optimal value function J* of Problem (D) satisfies 
or in terms of the mapping T of (8) 
J* = T(J*). (50b) Proof Let n = { p o ,  pl,. . .} be an arbitrary admissible policy, and 
consider the value J,(x) of the cost functional corresponding to n when the initial state is x .  We have 
J, (x)  = E { g [ x ,  c l O ( X X  w l  + KCf (x ,  P O ( X ) ,  w)I}, (51) W 
where for all z E S ,  N -  1 
vn(z) = lim E { C akgCxk, Pk(xk), w k l  
N 4 m  Wk k = l  
k =  1, 2. ... 
254 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
In this equation we have x 1  = z ,  and xk+ is generated from X k r  p&)r wk 
via the system equation (1). In other words, V,(z) is the cost from stage 1 to infinity using n when the initial state x 1  is equal to z.  We have clearly 
V,(z) 2 d * ( z )  vz E s. Hence from (51) 
J,M 2 E {gCx, po(x), w l  + aJ*Cf(x,  P O ( X ) ,  w)Il W 
Taking the infimum over all admissible policies we have 
inf J,(x) = J*(x) 2 inf E {g(x ,  u, w) + a J * [ f ( x ,  u, w)]} = T(J*)(x) .  II u e U ( x )  w 
Thus it remains to prove that the reverse inequality also holds. Let xo E S be any initial state for which we have 
Notice that this inequality will always hold under P. Under (52). given any scalars c2 > 0 let 2 = {,Go, ,GI ,  . . .} be a policy such that 
E{sCxo ,  Po(x), w l  + aJ*Cf(xo, Bo(xo), W ) l l  W 
G inf E { g ( x o ,  u, w) + a J * [ f ( x o ,  u, w)l1 + &Ir (53) U C U ( X 0 )  w 
and 
E { J f  'C f b o  7 ,Go(xo), 411 G E {J*Cf(xo 3 Po(xo), 41 1 + E z  9 (54) W W 
where 
6 = {,GI, f i 2 ,  . * .I. 
Such a policy clearly exists when the problem is deterministic, i.e., D consists of a single element. It can also be shown to exist in the general case (see Problem 8). We have by (53) and (54) 
J&O) = E {gCx07 fio(xo), w l  + aJ*,Cf(xo, Bo(xo), w)l> W 
G E { S C X O ,  fio(xo), W I  + aJ*Cf(xo, ,Go(xo), w)11 + 
G inf E {g(xo ,  u, w) + aJ*Cf(xo ,  u, w)]) + el + aEZ. 
W 
UEU(X0) w 
6.4 UNBOUNDED COSTS PER STAGE 255 
Since 
we obtain J*(xo) < J*(x,), 
J*(xo) < inf E {g (xo ,  u, w) + a J * [ f ( x o ,  u, w)]} + cl + aEZ, U C U ( X 0 )  w 
Since cl, cZ > 0 are arbitrary, we obtain 
J*(xo) < inf E {g(xo, u, w) + aJ*[ f ( xo ,  u, w)l> = T(J*)(xo) ,  (55)  u e U ( x 0 )  w 
for all initial states xo E S for which (52) holds. If (under N) xo E S is such that 
inf E { g ( x o ,  u, w) + aJ*Cf(xo, u, w)l) = -03, U O U ( X 0 )  w 
then 
inf E { g ( x o ,  u, w)} = - 03 or inf E { J * [ f ( x o ,  u, w)]} = -a. 
U C U ( X 0 )  w U € U ( X O )  w 
In the first case we have clearly J*(xo) = - 03 and ( 5 5 )  holds. In the second 
case given any M > 0 one may find a EE V ( x o )  such that 
It follows, using the result of Problem 8, that we may also find a policy El  = {ill, &,. . .} such that 
E{J,,[f(xo, u",W)l> < - M .  W 
Consider a policy of the form ii = {Po ,  &, &, . . .}, where fio(xo) = u". Then, since under N we have Ew {g[xo, po(x0), w]} < 0, it follows that 
J*(xo) < JE(xo) = E{g[xo, fio(xo), w] + a J d , [ f ( x O ,  Po(x0), w)]} < -aM. 
Since M > 0 is arbitrary, it follows that J*(xo) = - 03 and thus inequality 
(55 )  is established for all xo E S for which (52) does not hold. Hence (55 )  holds for all xo E S and the proposition is proved. 
W 
Q.E.D. 
Similarly as in Corollaries 1.1, 2.1, and 3.1 we have: 
Corollary 8.1 Let a = {p, p, . . .} be an admissible stationary policy. Then under Assumption P or N we have 
J,(x) = E {gCx, P ( X ) ,  wl + @J,Cfk A x ) ,  w)l} 
W 
or in terms of the mapping T, of (9) 
J, = T,(J,). 
256 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Contrary to the case of Assumption B the optimal value function J* under Assumption P or N need not be the unique solution of the functional equation 
J ( x )  = T ( J ) ( x )  = inf E {g(x ,  u, w) + a J [ f ( x ,  u, w)]}. (56) U P U ( X )  w 
Consider the following examples. 
EXAMPLE 1 Let S = [0, + 00) (or S = (- co, 01) and 
g(x ,  u, w) = 0, f ( x ,  u, w) = x/u ,  
J ( x )  = p x  VXES 
v x ,  u, w. 
Then for every /?, the function J given by 
is a solution of (56) and hence T has an infinite number of fixed points in this case, although there is a unique fixed point within the class of bounded functions-the zero function Jo(x )  = 0 Vx E S ,  which is the optimal value function for this problem. More generally it can be shown by using Pro- position 9 that if there exists a bounded function that is a fixed point of T, then that function must be equal to the optimal value function J* (see Problem 15). 
EXAMPLE 2 Let S = [0, + 00) (or S = (- co, 01) and 
g(x,  u, w) = (1 - $)x, f ( x ,  u, w) = x/& v x ,  u, w. 
Then the reader may verify that the functions J(x )  = x ,  J ( x )  = x + x 2 ,  and J(x )  = x - x2 are all solutions of (56). 
It is to be noted also that when a = 1 (a case to be examined in the next chapter), Eq. (56) may have an infinity of solutions even within the class of bounded functions. This is clear since if a = 1 and J(  - ) is any solution of (56), then J(  - ) + r, where r is any scalar, is also a solution. 
The optimal value function J*, however, has the property that it is the smallest (under Assumption P) or largest (under Assumption N) fixed point of T in the sense described in the following proposition. 
Proposition 9 (a) Under Assumption P if 3:  S -+ (- 00, + co] is bounded below and satisfies .f = T( j ) ,  then J* ,< J. 
(b) Under Assumption N if 3 : S + [ - 00, + co) is bounded above and 
satisfies 
Proof (a) Under Assumption P let r be a scalar such that . f (x )  + r 2 0 for all x E S. For any sequence { & k }  with &k > 0, let it = { F 0 ,  PI, . . .} be an admissible policy for which we have for every x E S and k, 
(57) 
= T ( j ) ,  then j < J*. 
E { g [ x ,  b k ( X ) ,  w1 + a J [ f ( x ,  p k ( X ) ,  w)l> ,< T ( J ) ( x )  + & k .  W 
6.4 UNBOUNDED COSTS PER STAGE 257 
Such a policy exists since T ( j ) ( x )  > - m for all x E S. We have for any 
initial state xo E S, 
Now using (57) and the assumption 1 = T ( j )  we obtain 
Combining these inequalities we obtain 
/ N - 1  \ 
Since the sequence {ck} is arbitrary (except for &k > 0) we may select { & k }  so that limN,m 1t:d ak&k is arbitrarily close to zero, and the result follows. 
258 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
(b) Under Assumption N, let Y be a scalar such that J(x)  + r < 0 for all x E S. We have for every initial state xo E S ,  
f N -  1 
I I 
N -  1 
> inflim sup E f f N [ J ( x N )  + r ]  + 1 a k g [ x k ,  p k ( x k ) ,  w k l  
2 lim sup inf E B"[.J(x,) + r ]  + 1 a k g [ x k ,  P k ( X k ) ?  w k l  , 
k = O  
N -  1 
N - t w  R W k  i k = O  
A N - t m  W k  i 
(58)  
where the last inequality follows from the fact that for any sequence ( h ~ ( 1 ) )  of functions of a parameter A we have 
inf lim sup hN(A) > lim sup inf hN(A). A N - m  N - m  A 
This inequality follows by writing 
h N ( 1 )  3 inf h N ( 1 )  
and by subsequently taking the limit superior of both sides and the infimum over 1 of the left-hand side. 
a 
Now we have by using the assumption J" = T( j ) ,  
I N -  1 
a N J ( x N )  + c a k g [ X k ,  p k ( x k ) ,  w k l  
k = O  
T N - 2  
Z W k  
= J(xo). 
Using this equality in (58) we obtain 
J*(xo) > J(x0)  + lim aNr = J(xo). Q.E.D. N - t  m 
6.4 UNBOUNDED COSTS PER STAGE 259 
Similarly as earlier we have the following corollary : 
Corollary 9.1 Let a = {p, p, . . .} be an admissible stationary policy. 
(a) Under Assumption P if J :  S -+ ( -  00, + co] is bounded below,and 
(b) Under Assumption N if 3: S -, [- 00, + co) is bounded above and 
satisfies j = T,(j), then J ,  6 j .  
satisfies 1 = T,(j), then < J,. 
Under Assumption N, Proposition 9 yields also the following corollary, 
which constitutes a necessary and sufficient condition for optimality of a stationary policy. 
Corollary 9.2 (Necessary and Sufficient Condition for Optimality under Assumption N) In order for an admissible stationary policy a* = {p*, p*, . . .} to be optimal under Assumption N it is necessary and sufficient that 
J,* = T,*(J,*) = T(J,*), 
or equivalently 
Proof Assume that the above condition holds. Then since J, .  is a fixed point of T we have by Proposition 9 that J , .  6 J*, which implies that n* is optimal. Conversely if a* is optimal, we have J* = J, .  and hence we obtain q*(J,,*) = J , .  = J* = T(J*) = T(J,,), which proves the desired result. 
Q.E.D. 
The sufficiency part of the above corollary need not be true under As- 
EXAMPLE Let S = (- co, + a), V(x) = (0, 11 for all x E S, 
sumption P, as the following example shows. 
g(x, u, w) = 1x1, f(x, u, w) = a-lux 
for all (x, u, w) E S x C x D. Let p*(x)  = 1 for all x E S. Then J,.(x) = + co if x # 0 and J,.(O) = 0. Furthermore we have J , .  = q*(J,.) = T(J,,) as the reader can easily verify. It is also easy to verify that J*(x)  = 1 x I and hence the policy {p*,  p*, . . .} is not optimal. 
On the other hand under Assumption P we have a different optimality condition, which, in view of its importance, we state as a proposition. 
260 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Proposition 10 (Necessary and Sufficient Condition for Optimality under Assumption P) In order for an admissible stationary policy 7c* = 
{p*, p*, . . .} to be optimal under Assumption P it is necessary and sufficient that 
J* = T,*(J*) = T(J*) ,  
or equivalently 
J*(x)  = E {gCx, p*(x), W I  + @J*Cf(x, p*(x), W ) l )  W 
< E {g(x ,  u, w )  + a J * [ f ( x ,  u, w ) ] }  Vx E S, u E U(x) .  W 
Proof We have by Corollary 8.1 that J,* = T,*(J,*). If the above con- dition holds, i.e., J* = T,,(J*), then we obtain from Corollary 9.1 that J , .  < J*,  which implies optimality of n*. Conversely if 7c* is optimal, we have J* = J,* and hence we obtain T,*(J*) = T,*(JM*) = J, .  = J* = T(J*), which proves the desired result. Q.E.D. 
Again the sufficiency part of the proposition need not be true under Assumption N as the following example shows. 
EXAMPLE L e t s =  C = ( - . c o , O ] , U ( x ) = C f o r a l l x ~ S ,  
g(x, u, w )  = f ( x ,  u, w )  = u 
for all (x ,  u, W ) E S  x C x D. Then J*(x)  = -co for all x ES, and every admissible policy 7c* = {p*, p*, . . .} satisfies the condition of the proposition above. On the other hand, for p*(x)  = 0 for all x E S we have J,,(x) = 0 for all x E S and hence {p*, p*, . . .} is not optimal. 
It is worth noting that Proposition 10 implies the existence of an optimal stationary policy under Assumption P when U ( x )  is a finite set for every x E S.  This result need not be true under Assumption N (an example for the related case where CI = 1 is given in Problem 10 of Chapter 7). 
The Successive Approximation Method 
We now turn to the question of whether it is possible to obtain the optimal value function J* (in the limit) by means of the DP algorithm. Let Jo denote the zero function on S, i.e., 
J,(x) = 0 VXES. 
Then under Assumption P we have 
J o  < T(J0)  < T2(Jo)  < . . . < Tk(Jo) < . . . , 
6.4 UNBOUNDED COSTS PER STAGE 261 
while under Assumption N we have 
J o  2 T ( J 0 )  2 T 2 ( J o )  2 . . . 2 Tk(Jo)  2 . . . , In either case the limit function 
J , ( x )  = lim T k ( J o ) ( x )  V x  E S (59) k - w  
is well defined provided we allow the possibility that J ,  can take the value 
+a (under Assumption P) or -a (under Assumption N). We shall be 
interested in the question whether 
J ,  = J* .  (60) This question is, of course, of computational interest but it is also of analytical interest since, if one knows that J* = 1imk+, Tk(Jo) ,  then one can infer properties of the unknown function J* from properties of Tk(Jo) that are functions defined in a concrete algorithmic manner. 
When the costs per stage are bounded (i.e., under Assumption B) we proved that (60) always holds. It turns out that when costs per stage are unbounded it may happen that (60) fails to 'hold. While we shall prove that (60) holds under Assumption N, when Assumption P is in effect, the example of Problem 9 shows that it may happen that J, # J * .  In what follows we shall provide additional assumptions that guarantee that (60) holds under Assumption P. We have the following proposition. 
Proposition 11 (a) Let Assumption P hold and assume that 
J,( .x)  = T(J , ) (x )  vx E S .  
Then if J : S -, R is any bounded function we have 
lim T k ( J ) ( x )  = J*(x )  Vx E S.  k - t m  
(b) Let Assumption N hold. Then if J :  S -, R is any bounded function, 
we have 
lim T k ( J ) ( x )  = J*(x) V X E S .  (62) k - m  
Proof (a) Since under Assumption P we have 
Jo  < T(J0) < . . . < Tk(Jo) < * . . < J*, 
it follows that 1imk-, Tk(Jo)  = J ,  < J * .  Since J ,  is also a fixed point of T by assumption we obtain from Proposition 9 that J* < J , .  It follows that 
J ,  = J* (63) 
262 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
and hence (61) is proved for the case J = J , .  It remains to prove (61) for every 
bounded J : S + R. The proof proceeds similarly as in the proof of Proposition 
1.  Let r be a scalar such that 
J - re d J , ,  J o  d J + re, 
where e is the unit function on S [e(x) = 1, Vx E S]. We have for all k and Y E S, 
(64) 
(65) 
Tk(J  - re)(x) < Tk(Jo)(x) < Tk(J + re)(x), 
Tk(J + re)(x) = Tk(J - re)(x) + 2akr = T k ( J ) ( x )  + akr. 
and 
It follows from these two relations that 
lim Tk(J - re)(x) = lim Tk(J + re)(x) = lim Tk(Jo)(x) = J*(x). (66) 
k - a ,  k-oo k - a ,  
Since lim Tk(J + re)(x) = lirn T~(J)(x) Vx E S, (67) k - m  k - c c  
we obtain (61). (b) We shall prove that under Assumption N we have 
J,(x) = lirn Tk(J,)(x) = J*(x) .  k - t m  
Then (62) follows from (64)-(67). Under Assumption N we have 
J ,  2 T(J,) 2 * .  . 2 T k ( J o )  2 * * * 2 J*.  
It follows that 
J,(x) = lim Tk(Jo)(x) 2 J*(x) t'x E S. (68) k - m  
Also from relation Tk(J,) 2 J , ,  by applying T to both sides, we obtain Tk+'(Jo)  2 T(J,)  and taking the limit as k + co 
J ,  2 T(J,). 
On the other hand, for any x E S, u E V ( x )  we have 
E M X ,  u, w )  + ~ T k ( J 0 ) C f ( X ,  u  w)l )  2 J a b ) .  W 
Taking the limit of the left side as k + co and using the fact that Tk(J,J 
converges monotonically to J ,  we have 
Taking the infimum over u E V(x) we obtain 
T(J, ) (x)  2 J , ( x )  vx E s. 
6.4 UNBOUNDED COSTS PER STAGE 263 
Combining (69) and (70), 
J ,  = T(J,). 
Hence by Proposition 9 
J, < J*. 
Combining this inequality with (68) we obtain J ,  = 1imk+, Tk(Jo) = J* and the result follows. Q.E.D. 
We now proceed to obtain conditions that guarantee that J ,  = T(J,) under Assumption P. As part (a) of Proposition 11 shows, J ,  = T(J,) is a sufficient condition for the equality J ,  = J* to hold. It is also a necessary condition in view of relation 
(71) 
(72) 
(73) 
J ,  d T(J,)  d J*. 
Tk- ' ( J o )  < Tk(Jo) < * . * < J ,  < J*. 
Tk(Jo) < T k +  ' ( J o )  < . . . < T(J,) < J*. 
This last relation follows once we observe that 
By applying T throughout and using J* = T(J*), 
By taking the limit as k -, co, (71) follows. 
We prove two propositions providing conditions for J ,  = T(J,). The 
first admits an easy proof but requires a restrictive assumption. The second is a little harder to prove but requires a much weaker assumption. 
Proposition 12 Let Assumption P hold and assume that the control constraint set U(x) is a finite set for every x E S. Then 
J ,  = T(J,) = J* = T(J*). 
Proof From (73) we have for all x E S 
and taking the limit in (74), J, < T(J,). Suppose that there existed a state 2 E S, such that 
Jrn(2) < T(J,)(f). (75) Using the finiteness of U(2)  let Uk be the minimizing control in (74). Since U(2) is finite there must exist some 6 E U(2)  such that uk = 6 for all k in some infinite subset Y' of the positive integers. By (74) we have for all k E Y' 
T k +  '(Jo)(2)  = E {g(2,6, w )  + aTk(Jo) [ f @ ,  6 , w ) l )  < T(J,)(Z). W 
264 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
It follows that J , ( Z )  = T(J,)(%), contradicting (75). Q.E.D. 
The following proposition strengthens Proposition 12 in that it requires a compactness rather than a finiteness assumption. We recall (see Appendix A) that a subset X of an n-dimensional Euclidean space R" is said to be compact if every sequence {xk} with xk E X contains a subsequence {Xk}ksy that con- verges to a point x E X. Equivalently X is compact if and only if it is closed and bounded. The empty set is (trivially) considered compact. Given any collection of compact sets, their intersection is a compact set (possibly empty). Given a sequence of nonempty compact sets X,, X2,  . . . , xk, . . . such that 
x1 3x23"' 3 X k 3 X k + 1 3 " ' ,  
their intersection 
fact it follows that iff: R" + [- co, + co] is a function such that the set 
xk is both nonempty and compact. In view of this 
FA = { x E R " I ~ ( x )  < I I }  
is compact for every I I  E R, then there exists a point x* minimizingf, i.e., there exists an x* E R" such that 
f(x*) = inf f(x). x o R "  
To see this, take a sequence {A,} such that i k  + infxERnf(x) and & 2 & + I  
for all k. If infxcR,f(x) -= + 03 such a sequence exists and the sets 
 FA^ = {X E R" I f (X)  < &} 
are nonempty and compact. Furthermore, FAk 3 F L k +  for all k and hence the intersection np= F A ,  is also nonempty and compact. Let x* be any point in 
r)T= , F ~ , , .  Then 
f b * )  < 4 Qk = 1,2, . . . ,  
and taking the limit ask + co we obtainf(x*) < inf,,,, f(x), proving that x* 
minimizes f ( x ) .  
Proposition 13 Let Assumption P hold and assume that the sets 
6.4 UNBOUNDED COSTS PER STAGE 265 
are compact subsets of a Euclidean space for every x E S ,  il E R, and for all k 
greater than some integer E .  Then 
(77) J ,  = T(J,) = J* = T(J*). 
Furthermore there exists a stationary optimal policy. 
there existed a state 2 E S such that Proof Similarly as in Proposition 12 we have J ,  < T(J,). Suppose that 
J m ( 3  < T ( J a J 4 .  (78) 
Clearly we must have J,(Z)  < +co. For every k 2 k consider the sets 
uk[z, 5,(2)] = {u  E u(x)l E{g(% u, w) + aTk(J,')[f(z?,  u, w)]} < Jm(2)}* W 
Let also u k  be a point attaining the infimum in 
i.e., u k  is such that 
Tk+'(Jo)(g)  = E{g(a, uk, W) aTk(Jo)[ f (Z ,  uk, W)]} < J, (g) .  W 
Such minimizing points uk exist by our compactness assumption. For every k > k consider the sequence {ui} im,k.  Since Tk(Jo)  < Tk+l (JO)  d . . .  d J ,  it follows that 
E {g(n, ui, W )  + a T k ( J o ) [ f ( g ,  ui, w)I> W 
< E {g(% ui, w) + aTi(Jo) [f(% ui ,  w)]} d J,(K) Vi 2 k .  W 
Hence { u i } i m , k  c u,"?, J,(Z)], and since uk[T ,  J,(2)] is compact, all the limit points of {ui}im,k belong to uk[i??, J,(?)] and at least one such limit point exists. Hence the same is true of the limit points of the whole sequence {ui}im,i. It follows that if u" is a limit point of {ui}im,r;, then 
OD 
u" E n u k [ % ,  J,(%)]. 
k = k  
This implies by (76) that for all k 2 E J , (n)  2 E {g(% 4 W) + aTk(Jo) [f(% 6, w)]} > T k +  ' ( Jo ) (Z ) .  
W 
Taking the limit as k -+ co we obtain 
J,(?) = E is(?, u", w) + .J,Cf(% u", w)ll. W 
Since the right-hand side is greater or equal to T(J,)(%), (78) is contradicted. Hence J ,  = T(J,) and (77) is proved. 
266 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
To show that there exists an optimal stationary policy observe that (77) and the last relation imply that G attains the infimum in 
J*(f) = inf E {g(f, u, w)  + aJ*[ f (2, u, w ) ] }  ueU(3)  w 
for a state f E S with J*(f) < + co. For states f E S such that J*(2)  = + co every u E U(2) attains the infimum above. Hence by Proposition 10 an optimal stationary policy exists. Q.E.D. 
The reader may verify by inspection of the proof that actually Proposition 13 may be proved under the weaker assumption that the sets U k [ f ,  J,(f)] are compact for all f E S such that J, (2)  < + co, and all k greater than some index k. 
Another fact that may be verifiedfrom the proofis that ifpk(2), k = 0,1, . . . , attains the infimum in the relation 
T k +  ' ( J 0 ) ( f )  = inf E(g(2, u, w )  + aTk(Jo)  [f (2, u, w ) ] } ,  
U E U ( X )  w 
then if p*(f) is a limit point of {pk ( f ) } ,  V f  E S ,  the policy n* = {p*, p*, . . .} is optimal. Furthermore, {pk(%)} has at least one limit point for every f E S for which J*(f) < + co. Thus the successive approximation method under the assumptions of Proposition 12 or 13 yields in the limit not only the optimal value function J* but also an optimal stationary policy. 
6.5 Linear Systems and Quadratic Cost Functionals 
Consider the case where in Problem (D) the system is linear: 
X k + l  = AX, + BUk -k W k ,  k = 0, 1,.  . . , where xk E R", uk E R" for all k and the matrices A, B are known. As in Sections 3.1 and 4.3 we assume that the random disturbances wk are independent with zero mean and finite second moments. The cost functional is quadratic and has the form 
where Q is a positive semidefinite symmetric n x n matrix and R is a positive definite symmetric m x m matrix. The problem clearly falls under the frame- work of Assumption P. 
Our approach will be to consider the ordinary D P  algorithm, i.e., obtain 
the functions T(Jo), T2(Jo), .. . , as well as the pointwise limit function 
J, = 1imk-, Tk(Jo).  Subsequently we show that J, satisfies J, = T(J,) 
6.5 LINEAR SYSTEMS AND QUADRATIC COST FUNCTIONALS 267 
and hence, by Proposition 11, J ,  = J * .  The optimal policy is then easily obtained from the optimal value function J* via the DP  functional equation using Proposition 10. 
As in Section 3.1 we have 
J0(x) = 0 V X  E R”, 
T(J,)(x) = inf(x’Qx + u’Ru) = x’Qx Vx E R”, U 
T2(Jo)(x)  = inf E{x’Qx + u‘Ru + u(Ax + Bu + w)’Q(Ax + Bu + w)} u w  
= x’K,x + uE{w‘Qw} V X E R ” ,  W 
k -  1 
Tk+’(J0)(x) = X ‘ K k X  + ~ l ~ - ~  E{w’K,w}  V X  ER”, k = 1,2 , .  . . , W m = O  
where the matrices K O ,  K , ,  K 2 ,  . . . are given recursively by 
Kk+l = A’[ctKk - u2KkB(UB’KkB + R)-’B’Kk]A + Q, k = 0, 1 , .  . . . 
Now by writing I? = R/u and A = &A the preceding equation may be written 
Kk+1 = A’[Kk - K,B(B’KkB + I?)-’B’Kk]A + Q, 
and is of the form considered in Section 3.1. By making use of the result shown there we have 
Kk -+ K 
provided the pairs (A, B) and (2, C), where Q = C’C, are controllable and observable, respectively. Since A = &A, controllability and observability of (A, B) or (A ,  C )  are clearly equivalent to controllability and observability of (A, B) or (A, C).  The matrix K is positive definite and it is the unique solution of the equation 
K = A’[& - u 2 K B ( ~ B ’ K B  + R)-’B’K]A + Q (79) 
As a result of the preceding analysis we have that the pointwise limit of the within the class of positive semidefinite symmetric matrices. 
functions Tk(Jo) is given by 
J, (x)  = lim Tk(Jo)(x) = x’Kx + c, k -  m 
where k -  1 
c = lim 1 ~ ~ - ~ E { w ’ K , w ) .  
k-m ,,,=o W 
268 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
This limit is well defined since the scalars ck, where 
ck = 1 c i k - m  E { w l K , w } ,  
k -  1 
W m = O  
satisfy the equation 
ck+l = UCk + aE{W'KkW} .  W 
Since ci < 1 and Kk K it follows that ck + c,  where 
c = [./(1 - a)] E { w ' K w } .  
W 
Now using (79)-(81) one can easily verify that for all x E S 
J , (x)  = T ( J , ) ( x )  = min x'Qx + u'Ru + ci E { J , ( A x  + Bu + w ) }  (82)  
and hence by Proposition 11, J ,  = J*.  Another method for proving that J ,  = T(J,) is to show that the assumption of Proposition 13 is satisfied, i.e., that the sets 
s W 1 
I L uk(x, A) = U E{X'QX U'RU + ciTk(J0)(AX + BU W ) }  < A 
are compact. This can be easily verified using the fact that Tk(Jo)  is a quadratic function and R is positive definite. The optimal policy is obtained by mini- mization in (82) and has the form n* = {p*, p*, . . .}, where p* is given by 
p*(x) = -ci(ciB'KB + R ) -  'B'KAx 'dx E R". 
The linearity and stationarity of this policy makes it very attractive for engineering applications. A number of generalized versions of the problem of this section, including the case of imperfect state information, are treated in the problem section. 
6.6 Inventory Control 
Let us consider an infinite horizon version of the inventory control problem of Section 3.2 where costs per stage are discounted. Inventory stock evolves according to the equation 
(83) 
Again we assume that the successive demands wk are independent and bounded and have identical probability distributions. We shall assume for simplicity 
xk+l = xk + uk - wk, k = 0, 1,. ... 
6.6 INVENTORY CONTROL 269 
that there is no fixed cost. A similar analysis may be carried out for the case of a nonzero fixed cost. The function to be minimized is given by 
Jn(xo) = lim E [iln*lcpk(xk) + p max(O, wk - xk - pk(xk)) 
h'+m Wk k = O  
k = O .  1 .  ... 
The DP algorithm is given by Jo(x) = 0, 
Tk+ ' ( J ~ ) ( X )  = inf E {cu + p max(0, w - x - u )  + h max(0, x + u - w )  
ocu  w 
+ crTk(J,)(x + u - w ) } .  (85)  
(86) 
Let us first show that 
J*(xo) = inf Jn(xo) < + co Vx,  E S.  n 
Indeed consider the policy it = {B, B, . . .}, where ,ii is defined by 
0 if x 2 0, if x < 0. ' ( X I =  { - x  
Since wk is nonnegative and bounded it follows that the inventory stock xk when the policy it is used satisfies 
-wk-l d xk d maX[O, Xo], k = 1, 2,. . . , 
and is bounded. Hence fi(xk) is also bounded. Hence the cost per stage incurred when 6 is used is bounded, and in view of the presence of the dis- count factor we have 
Since J* d J * ,  (86) follows. 
Tk(Jo)  are real-valued convex functions. Indeed we have 
J*(xo) < +co VXOES. 
Next let us observe that under the assumption c < p, the functions 
(87) 
which implies that Tk(Jo)  is real valued. Convexity follows easily by induction as shown in Section 3.2. Consider now the sets 
Jo d T(J0) < . . . < Tk(Jo) d . . . d J*,  
{cu + p max(0, w - x - u )  + h max(0, x + u - w)  
+ crTk(J,)(x + u - w)}  d 1 . I 
270 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
These sets are bounded since the expected value above tends to +a as u + + 00. Also the sets uk(x, A) are closed since the expected value in (88) 
is a continuous function of u [recall that Tk(Jo) is a real-valued convex and hence continuous function]. Thus we may invoke Proposition 13 and assert that 
J, (x)  = lim Tk(Jo) (x )  = J*(x) Vx E S .  k - m  
It follows from the convexity of the functions Tk(Jo) that the limit function J* is a real-oalued convexfunction. Furthermore we have from Proposition 8 the optimality equation 
J*(x)  = inf E {cu + p max(0, w - x - u)  + h max(0, x + u - w) 
u > o  w 
+ crJ*(x + u - w)}. 
An optimal stationary policy n* = { P * ~  p*, . . .} can be obtained from the above equation as in Sections 1.3 and 3.2. We have 
S* - x if x < S*, 
otherwise, 
where S* is a minimizing point of 
with G*(Y) = C Y  + U Y )  + E {J*b - w)), 
L(y)  = p E {max(O, w - y)} + h E {max(O, y - w)}. 
It is easy to see that if p > c, we have liml,,l+m G*(y)  = + co so that such a minimizing point exists. Furthermore by utilizing the observation made at the end of Section 6.4 it follows that minimizing points S* of C*(y) may be obtained as limit points of sequences {&}, where for each k the scalar Sk minimizes 
W 
W W 
Gk(y) = C Y  + Lb) E {Tk(J0)(Y - W ) >  
W 
and is obtained by means of the successive approximation method. In the case where there is a positive fixed cost (K > 0) the same line of 
argument may be used. Similarly we prove that J* is a real-valued K-convex function. A separate argument is necessary to prove that J* is also continuous (see references [B3] or [I2]). Once K-convexity and continuity of J* is established the optimality of a stationary (s*, S*)  policy follows from the equation 
J*(x)  = min E {C(u) + p max(0, w - x - u)  + h max(0, x + u - w) 
u20 w 
+ aJ*(x + u - w)}, 
where C(u) = K + cu if u > 0 and C(0) = 0. 
6.7 NONSTATIONARY AND PERIODIC PROBLEMS 271 
6.7 Nonstationary and Periodic Problems 
The standing assumption so far in this chapter has been that the problem involves a stationary system and a stationary cost per stage (except for the presence of the discount factor). Problems where the system or the cost per stage are nonstationary arise occasionally in practice or in theoretical studies and are thus of some interest. It turns out that such problems can be em- bedded by means of a simple reformulation within the framework of Problem (D) for which stationarity prevails. Once this reformulation is considered, one easily obtains results analogous to those of Sections 6.1 and 6.4. 
Consider a nonstationary system of the form 
and a cost functional of the form 
In the above equations, for each k ,  x k  belongs to a space S k ,  u k  belongs to a space C k  and satisfies u k  E u k ( x k )  for all x k  E S k ,  and w k  belongs to a countable space D k .  The sets s k ,  c k ,  U k ( X k ) ,  Dk may differ from one stage to the next. The random disturbances w k  are characterized by probabilities P k (  - I x k ,  u k ) ,  
which depend on x k ,  u k  as well as the time index k. The set of admissible policies n is the set of all sequences = { p o ,  p,, . . .} with pk: S k  + Ck with 
D k  + R are given and are assumed to satisfy one of the following three 
assumptions, which are analogous to Assumptions B, P, and N considered earlier in this chapter: 
Assumption B’ The functions g k  satisfy for all k = 0, 1 ,  . . . , 
p k ( x k )  E U k ( X k )  for all x k  E S k  and k = 0, 1, . . . . The functions g k  S k  x C k  x 
0 < g k ( X k ,  u k ,  w k )  < M v ( x k ,  u k ,  w k ) E S k  Ck D k ,  
where M is some scalar. 
Assumption P’ The functions g k  satisfy for all k = 0, 1, . . . , 
0 < g k ( X k ,  u k ,  w k )  v ( x k ,  u k ,  w k ) E S k  C k  D k *  
Assumption N‘ The functions g k  satisfy for all k = 0, 1, . . . , g k ( X k ,  u k ,  w k )  < 0 v ( x k ,  u k ,  w k ) E S k  Ck D k .  
We shall refer to the problem formulated above as the nonstationary problem (NSP). 
272 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Let us now convert the NSP to a stationary problem that fits within the framework of Problem (D). In order to simplify the notation we shall assume 
that the state spaces Si, i = 0, 1,. . . , the control spaces C i ,  i = 0, 1,. . . , 
and the disturbance spaces Di,  i = 0, 1, . . . , are all mutually disjoint. This 
assumption does not involve a loss of generality since, if necessary, we may relabel the elements of Si, Ci, and Di without affecting the structure of the problem. Define now a new state space S,  a new control space C,  and a new (countable) disturbance space D by 
m m m 
S =  USi,  C =  U C i ,  D =  u D i .  i = O  i = O  i = O  
Introduce a new (stationary) system 
2 k + 1  = f ( a k ,  u"k, Gk), k = 0, 1,. . . , (91) 
where 2 k  E S, i i k  E C, "tk E D ,  and the system function f: S x C x D --* S is defined by 
f (2,  6, G) = fi(2, 6, 6) if 2 € S i ,  u"€Ci,  G E  D i ,  i = 0, 1,. . . . For triplets (2, u", G), where for some i = 0, 1, . . . we have 2 E Si but u" 4 Ci, or G 4 D i ,  the definition off is immaterial-any definition is adequate for our purposes in view of the control constraints to be introduced. The control constraint is taken to be u" E U(2) for all 2 E S ,  where U( ) is defined by 
U(2) = Ui(2)  if 2 E S i ,  i = 0, 1, . . . . 
The disturbance ii, is characterized by probabilities P( 6 12, u") such that 
P ( G E D ~ ~ ~ E E S ~ , U " E C ~ )  = 1, P ( G $ D ~ I ~ ? E S ~ , U " E C ~ )  = 0, 
i = 0, 1 ,..., i = 0, 1 ,.... 
Furthermore for any wi E D i ,  x i  E Si, ui E Ci, i = 0, 1 ,  . . . , we have 
P ( W i l X i ,  U i )  = P i ( W i I X i ,  U i ) .  
We also introduce a new cost functional 
where the (stationary) cost per stage g :  S x C x D -, R is defined by 
g(2,  u", 6) = gi (2 ,  u", G) if R E & ,  u"€Ci,  GEQ, i = 0, 1,. , . . For triplets (2, u', G), where for some i = 0, 1, . . . we have 2 E Si but u" 4 Ci or 6 4 Di,  any.definition of g is adequate provided 0 < g(2,  fi, G) < M for all (2, u", G) when Assumption B' holds, 0 < g(2,u", G) when P' holds, ,and 
6.7 NONSTATIONARY AND PERIODIC PROBLEMS 273 
g(Z,ii ,  i?) < 0 when N' holds. The set of admissible policies l=i for the new problem consists of all sequences ii = {,Lo, ,Ll,  . . .} where f i k :  S + C and 
j i k ( 2 )  E U ( 2 )  for all Z E S and k = 0, 1, . . . . 
The construction given above defines a problem that clearly fits the framework of Problem (D). We shall refer to this problem as the stationary problem (SP). 
It isimportant to understand thenature oftheintimateconnection between the NSP and the SP formulated above. Let n = {po ,  pl, . . .} be an admissible 
policy for the NSP. Also let ii = {Po, /I1, . . .} be an admissible policy for the 
SP such that 
f i i (Z )  = pi (Z)  if Z E S ~ ,  i = 0, 1,. . . . (93) 
Let x o  E So be the initial state for the NSP and consider the same initial state for the SP, i.e., Z0 = xo E S o .  Then the sequence of states {Zi} generated in the SP will satisfy Zi E S i ,  i = 0, 1, . . . , with probability one, i.e., the system will 
move from the set So to the set S1, then to S 2 ,  etc., just as in the NSP. Further- more, the probabilistic law of generation of states and costs is identical in the NSP and the SP. As a result it is easy to see that for any admissible policies A and ii satisfying (93) and initial states x o ,  Zo satisfying xo = Zo E S o ,  the sequence of generated states in the NSP and the SP is the same ( x i  = , f i ,  Vi) provided the generated disturbances wi and Gi  are also the same for all i (w i  = Gi,  Vi ) .  Furthermore, if 7c and ii satisfy (93), we have J,(xo)  = J f f ( , f 0 )  if x o  = Zo E S o .  Let us also consider the optimal value functions for the NSP and the SP 
J*(xo)  = inf J,(xo) ,  xo  E S o ,  n s n  
Then it follows from the construction of the SP that 
where 
if Zo = x i e S i ,  i = 0, 1 ,.... (95) 
Note that in this equation the right-hand side is defined in terms of the data of the NSP. As a special case of this equation we obtain 
j*(z0) = j* (z0,  0) = J * ( X ~ )  if go = x o  E so. (96) 
274 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Thus the optimal value function J* of the NSP can be obtainedfrom the optimal value function j* of the SP. Furthermore, if it* = {fit, f i y , .  . .} is an optimal policy for the SP, then the policy n* = {&, p:, . . .} defined by 
pf(xi) = fif(xi) Vxi E S i ,  i = 0, 1 , .  . . , (97) 
is an optimal policy for the NSP. Thus optimal policies for the SP yield optimal policies for the NSP via (97). Another point to be noted is that if Assumption B’ (PI, N‘) is satisfied for the NSP,  then Assumption B ( P ,  N )  in- troduced earlier in this chapter is satisjied for the SP. 
The observations above indicate clearly that one may analyze the NSP by means of the SP. In fact every result given in Sections 6.1 and 6.4 when applied to the SP yields a corresponding result for the NSP. We shall con- tent ourselves with providing the form of the optimality equation for the NSP in the following proposition. 
Proposition 14 Under Assumption B’ (P’, N’) there holds 
J*(x,)  = j*(x0, 0) Vx0 E So,  
where for all i = 0, 1 ,  . . . the functions j*( - , i) map Si  into [0, 00) ([0, 003, 
[ - 00, O]),  are given by (95), and satisfy 
J*(xi ,  i )  = inf E { g i ( x i ,  u i ,  wi )  + J * [ f ; : ( x i ,  uir wi), i + 11) U i € U i ( X i )  w, 
V x i e S i ,  i = 0, 1,. . . . (98) 
Under Assumption B’ the functions j*( - , i ) ,  i = 0, 1, . . . , are the unique 
bounded solutions of the set of equations (98). Furthermore, under Assump- tion B’ or P’, if pF(.xi) E U i ( x i )  attains the infimum in (98) for all x i  E S i .  and i, then the policy TC* = (&, p t .  . . .) is optimal for the NSP. 
Proof Apply Propositions 2,8, and 10 to the SP. Then the result follows immediately by making use of definitions (94)-(96). Q.E.D. 
Notice that an optimal policy for the NSP will normally be nonstationary even though the SP may possess an optimal stationary policy. Furthermore, such an optimal policy is in general impossible to obtain in practice even if the state spaces Si, i = 0, 1 ,  . . . , are finite sets, in view of the fact that an infinite 
number of functions p: are involved. However, there are special cases where important simplifications occur. We proceed to examine two such cases. 
Eventually Stationary Problems 
Within the framework of the NSP consider the case where the spaces S i ,  C i ,  Di, the sets Ui( - ), the probability distributions Pi( - ( x i ,  ui), and the 
6.7 NONSTATIONARY AND PERIODIC PROBLEMS 275 
functionsf;: and gi  remain unchanged after some index E ,  i.e., 
- - 
S .  = S .  = S ,  Ci = Cj  = C,  D i  = D j  = D Vi , j  3 E, [ I  
Ui( - ) = U j ( .  ) = U ( .  ), Pi( - Ix, u)  = Pj( - Jx, u) V i ,  j 2 E,  f . =  [ J  f . = J g i = g . = i j ,  J V i , j > E .  
Notice that finite horizon problems may be embedded within the framework of the above problem by taking the function ij identically equal to zero. We shall assume that the spaces S i ,  C i ,  D i ,  i = 0, 1,. . . , - 1, are mutually 
disjoint and disjoint from S ,  C ,  D ,  respectively. Then we may define a new state space, control space, and disturbance space by 
- - -  
E -  1 E -  1 P- 1 
S =  U S i v S ,  C =  U C i v C ,  D =  U D i v D ,  
and similarly as earlier we may obtain an equivalent stationary problem. The optimality equation for this problem reduces to the system of ( E  + 1) equations 
i = O  i = O  i = O  
V x i e S i ,  i = 0, 1, ..., E - 1,  
J*(x) = inf E {g(x, u, w )  + a J * [ f ( x ,  u, w)]) vx ES, 
where j * ( x )  = J*(x. k )  for all .Y E Si; = S. If the infimum on the right-hand side of the above equations is attained for all xi, i = 0, 1 , .  . . , E - 1, and x, 
then under Assumptions B’ and P’ there exist (eventually stationary) optimal 
policies of the form n* = {p:, p:, . . . , p f ,  p f ,  . . .}. 
u e U ( x )  w 
Periodic Problems 
Assume within the framework of the NSP that there exists an integer 
p 2 2 (called the period) such that for all integers i and j with Ii - j l  = Ap, 
1, = 1,2, . . . , we have 
Si = S j ,  Ci = Cj ,  Di = D j ,  Vi( .) =I Uj( .), 
f i = f j ,  g i = g j ,  Pi(-)x,u)=Pj(.)x,u) V(X,U)ESi x ci. We assume that the spaces Si,  Ci ,  D i ,  i = 0, 1,. . ., p - 1, are mutually 
disjoint. Then we may define a new state space, control space, and disturbance space by 
P- 1 P- 1 P- 1 
i = O  i = O  i = O  
s =  U S ( ,  C =  U C i ,  D =  u D i .  
276 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
As done earlier, we may obtain an equivalent stationary problem. The optimality equation for this problem reduces to the system of p equations 
These equations may be used to obtain (under Assumption B’ or P )  a periodic 
of the right-hand side is attained for all x i ,  i = 0, 1, . . . , p - 1.  
Concerning the algorithmic solution of periodic problems, we mention 
that when all spaces involved are finite sets then an optimal policy may be found through a finite number of arithmetic operations by means of the policy iteration algorithm or linear programming. The form of these al- gorithms may be obtained by applying them to the corresponding SP, the state, control, and disturbance spaces of which are now the finite sets S ,  C ,  and D. 
Finally, we provide the form of the successive approximation method with starting functions equal to zero: 
policy of the form {p:, . . . , p p -  * *  1, po, . . . , ,up*- l,. . .} whenever the infimum 
j o ( x i ,  i) = o V X ~ E S ~ ,  i = 0,1, ..., p - 1. 
The (k + 1)st iteration of the successive approximation method is given by 
Under Assumptions B’ and N’ we have (by applying Q-oposition 1 or 1 1  to the corresponding SP) 
lim jk(Xi, i) = j * ( x i ,  i) v x i  E si, i = 0, . . . , p - 1 ,  
k + c o  
6.8 NOTES 277 
while under Assumption P‘ the same equations hold provided the sets 
are compact subsets of Euclidean spaces for all xi E S i ,  i ER ,  and k greater 
than some integer 5 (Proposition 13 applied to the SP). Under the same com- pactness condition an optimal periodic policy is guaranteed to exist. 
6.8 Notes 
The discounted problem with bounded cost per stage is by far the simplest and most well-behaved infinite horizon problem. This is due to the contrac- tion property induced by the presence of the discount factor. Many authors have contributed to its analysis, most notably Bellman [B3], Howard [H15], and Blackwell [BZO]. Contraction type properties were first exploited in a DP  setting by Shapley [SS] in a paper on multistage games. The mapping F of Section 6.2 and the corresponding algorithms are given by Kushner [KlO], where the connection with Gauss-Seidel iterations is pointed out (see also Hastings [H7]). The linear programming approach of Section 6.2 was pro- posed by DEpenoux [D3]. The error bounds given in Section 6.2 and Prob- lem 3 are improvements on results of McQueen [M5] and Denardo rD2] (see [B14]). The convergence results and discretization procedures of Prob- lem 2 are taken from Bertsekas [BlS]. The essential structure of the dis- counted cost problem with bounded cost per stage was captured in the ab- stract framework intraduced in an important paper by Denardo [D2] (see Problem 4). This framework contains many other interesting problems similar to Problem (D), such as the so-called Markov-renewal or semi-Markov decision problems [J4, H16, R4] or minimx discounted cost problems (see Problems 1 and 6). Denardo’s framework relies strongly on contraction properties and is thus generally inapplicable to problems of the type examined in Section 6.4 and in Chapter 7. A related framework that does not employ contraction assumptions and is applicable to problems such as those of Section 6.4 and Chapter 7 was developed recently by the author (see Problem 
278 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
9 in Chapter 7 and [B13] and [B16]). For analysis of discounted cost prob- lems involving linear systems and convex cost functionals see references [Bl 11 and [K8]. For analysis related to problems with imperfect state information see references [DS], [SS], and [Sll]. The form of the generalized policy iteration algorithm of Problem 13 is apparently new. 
Discounted cost problems with unbounded cost per stage are similar to undiscounted cost problems, which will be examined in the next section. Important works in this area are those of Dubins and Savage [DS], Blackwell [B21], and particularly Strauch [S17] (see Hinderer [H9] for an account). These authors considered explicitly the thorny measurability questions arising from uncountable disturbance spaces. The analysis of Section 6.4 is mostly a synthesis of results given in these references. Propositions 9a and 13 are new results [B13, B161. The result of Proposition 13 can be generalized to the case where the sets U,(x, 2) of (76) are compact subsets of an arbitrary topological space. For generalizations of the analysis of Section 6.4 see Problem 9 in Chapter 7 and [B13] and [B16]. 
It is to be noted that in our formulation of the problem of this chapter we have specified that the initial state x, is fixed and given. Thus whenever the optimal cost J*(xo) corresponding to xo is finite, it can be attained within any E > 0 by an admissible policy TI,(x,), i.e., given any E =- 0 there exists an admissible TI,(x,) such that 
Jn,&O) G J*(xo) + E.  
The policy n,(x0) will depend on xo and it does not necessarily follow that given any E > 0 there exists an admissible policy TI, (independent of xo) such that 
Jnr(xo) < J*(x,) + E vx, E s. 
Neither does it follow that policy TI, can be taken to be stationary unless Assumption B is satisfied (Problem 12). A considerable amount of research has been directed toward clarifying these fine points and the advanced reader is referred to references [B21], [B22], [Ml], [02], and [S17] for related analysis and counterexamples (see also Problems 22-25). 
The results on linear quadratic problems are well known (see, e.g., Kushner [KlO]). The inventory control problem has been analyzed by Bellman [B3] (see also Iglehart [I2]). For some recent results see Kalymon [K3]. The line of argument adopted here is new. 
The treatment of nonstationary and periodic problems by means of reduction to the stationary case is apparently new. Earlier works on the subject [F4, H9] do not take advantage of the possibility of this reduction. The results on periodic linear-quadratic problems and inventory control (Problems 18 and 20) seem to be new. 
PROBLEMS 279 
The formulation of Problem (D) excludes the possibility of constraints on the state xk of the form xk  E X c S .  Such constraints can be taken into account under Assumption P by adding to the cost per stage g the indicator function 6(x  1 X )  of the set X :  
if X E X ,  i" +00 if X E X .  
6 (XIX)  = 
This formulation, however, requires that g can take the value + 00. Nonethe- less all the results of Section 6.4 shown under Assumption P may be proved for g satisfying 
i.e., when g is allowed to take the value + co (see Problem 10). For an analysis and treatment of state constraints see references [B9] and [Bl 11 or Problem 13 in Chapter 7. 
Finally, we note that even though the problem of this chapter excludes specifically the possibility of an uncountable disturbance space, it may still serve as the starting point of analysis of a problem with uncountable dis- turbance space. This can be done by reducing such a problem to a deter- ministic problem (i.e., one where the disturbance space consists of a single element) with state space a set of probability measures. The basic idea of this reduction is demonstrated in Problem 21. The advanced reader may con- sult the work of Witsenhausen [WS] and see how a related reduction can be effected for a very broad class of finite horizon problems. 
Problems 
1. Provide analogs for the results and algorithms of Sections 6.1 and 6.2 for the problem of minimizing 
N -  1 
over all polices n = {po ,  p l ,  . . .} with pk(Xk) E v (xk)  vxk E S, where a E (0, l), g satisfies Assumption B, xk is generated by xk+ = f [ x k ,  &(xk)? wk], and W ( x ,  u)  is a given nonempty subset of D for each ( x ,  u)  E S x C .  2. The purpose of this problem is to provide discretization procedures and related convergence results analogous to those of Section 5.2. Consider the 
280 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
functional equation for J* : S + R : 
J*(x) = max E {g(x, u, w )  + d * [ f ( x ,  u, w ) ] )  usc  w 
where 0 < a < 1 and g , f ,  S ,  C,  and w satisfy continuity, compactness, and finiteness assumptions analogous to Assumptions A of Section 5.2. Let S', S2,  . . . , Sn be mutually disjoint sets with S = uy= S', select arbitrary 
points xi  E S', i = 1, . . . , n, and consider the discretized functional equation 
max E {g(x ,  u, w )  + a j * C f ( x ,  u, w)I) 
if x = x i ,  i = l ,  ..., n, 1 j*(xi) if XES', i = 1,. . ., n. 
Show that both equations have unique solutions J* and j* within 
U E C  w 
j * ( x )  = 
(a) the class of all bounded functions J :  S + R and furthermore 
lim sup I J*(x) - .l*(x) 1 = 0, 
d.+O x s S  
where 
d,  = max sug[lx - x i [ [ .  
i = l .  ..., n X E  
(b) Provide a discretization procedure and prove a similar result under assumptions analogous to Assumption B of Section 5.2. 
Hint: Use the results already proved in Section 5.2. 3. Let S be a set and B(S) be the set of all bounded real-valued functions on S. Let T: B(S)  -+ B(S) be a mapping with the following two properties: 
(1) T(J)  < T(J') for all J ,  J' E B(S) with J d J'. (2) For every scalar r # 0 and all x E S 
al  < [T(J + re) (x)  - T ( J ) ( x ) l / r  d a,, 
where a l ,  a2 are two scalars with 0 < a1  d a2 < 1. (a) Show that T is a contraction mapping on B(S) and hence for every 
J E B(S) we have 
lim Tk(J) (x )  = J*(x)  Vx E S ,  k + m  
where J* is the unique fixed point of Tin B(S). (b) Show that for all J E B(S), x E S ,  and k = 1,2, . . . , 
Tk(J)(X)  ck d T k + l ( J ) ( X )  ck+l  < J*(X) 
d Tk' l (J) (X)  + c k + l  d Tk(J ) (x )  + z k ,  
PROBLEMS 28 1 
where for all k 
1 - a2 a2 sup[Tk(J ) (x )  xss  - T*'(J)(x)]}. 
A geometric interpretation of these relations for the case where S consists of a single element is provided in Fig. 6.3. 
FIGURE 6.3 
(c) Show that the mapping F defined by (38)-(41) satisfies a" < [F(J + re) (x)  - F(J)(x) ] / r  < a, 
where n is the number of elements in S. Hint :  Use a line of argument similar to the one of Section 6.2. 
282 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
4. Let S be a set, let B(S) be the set of all bounded real-valued functions on S, let C be another set, and for each x E S let V(x)  be a given nonempty subset 
of C. Assume that we are given a mapping H: S x C x B(S) + R having the 
monotonicity property 
(M) J < J’ * H ( x ,  u, J) < H ( x ,  u, J’) VJ, J’ E B(S), (x, u)  E S x C ,  
and the contraction property 
l H ( x ,  u, J) - H ( x ,  u, J’)I d aJIJ - J’IJ 
where a is some scalar with 0 c a c 1 and 
VJ, J’ E B(S),  (x, u)  E S x C ,  (C) 
llJ - J’I( = suplJ(x) - J’(x)l. 
X € S  
Let M denote the set of all functions p: S + C with p ( x )  E V ( x )  Vx E S. For any 
p E M define the mapping T, by 
T,(J)(x) = HCx, p(4, 51 Vx E S, 
and the mapping T by 
T ( J ) ( x )  = inf H ( x ,  u, J) Vx E S. 
We assume that T(J), T,(J) E B(S) for all J E B(S), p E M. Show the following: (a) There exists a unique function J* E B(S), and for each p E M a unique 
function J, E B(S) such that 
U E  U ( x )  
J* = T(J*), J, = T,(J,). 
Furthermore, 
(IJ* - Tk(J)IJ + 0, (IJ, - Ti(J)(I + 0 V J € B ( S ) .  
(b) There holds 
J*(x)  = inf J,(x) Vx E S ,  # E M  
and if for some p E M we have T,(J*) = J*, then J, = J*. Furthermore if there exists a function J E B ( S )  such that limb+ (Tp0 . . . T , , ) ( J ) ( x )  exists and is a real number for all x E S and all sequences { i l k } .  p h  E M .  Vk. then 
lim(T,;.. T,,)(J)(x) = lirn(T,;.. T,,)(J)(x) VJEB(S), X E S ,  k - w  k+w 
p k € M ,  k = 0, 1 ,..., 
J*(x) = inf lim (Two . . . T,,)(J)(x) VJ E B(S), x E S.  p i ~ M  k+w 
i = O .  1, ... 
(c) Prove (a) and (b) when the contraction assumption (C) is replaced by the assumption that there exists a scalar a with 0 c a c 1, a scalar 1, > 0, 
PROBLEMS 283 
and an integer m 2 1 such that 
ll(T,,T,,.** TPm-,)(J) - (T,,,T,;-. L-,)(J’)I l G allJ - J’IL 
V J ,  J ‘ E B ( S ) ,  P o , .  - * , Pm-1 E M ,  
IIT,(J) - T,(J’)ll G LllJ - J’IL (C’) 
VJ, J’ E B(S), p E M .  
(d) Assume that S is a finite set, S = {1,2, .  . . , n}. Under Eqs. (M) and (C’) show that {J*(l), . . . , J*(n)}  is a solution of each of the following prob- 
lems : 
min i ~ ( i ) ,  max i J(i) .  
T(J)( i )  4 J ( i )  i =  1 TCJ)(i)> 4 i )  i =  1 
i = l ,  ..., n I =  1 .  ... ( n 
(e) Assume that S and C are finite sets and Eqs. (M) and (C’) hold. Consider the following generalized policy iteration algorithm: 
(1) (2) Repeat the process until J,c + = J,E for some index &. 
Start with an initial po E M .  Given p i  calculate JWi and p i + ’  E M  such that TPi+ l(J,i) = T(J,,i). 
Show that the algorithm will yield J* after a finite number of iterations. 
that T,JTk-’ (J) ]  = Tk(J)  and p k  E M. Show that (f) Assume that Eqs. (M) and (C) hold. Let J E B ( S )  and let p k  be such 
llJ* - J P r I I  G C2ak/(l - a)lllT(J) - Jll. 
Show also that 
llJ* - Tk(J)II d bk, 
where bk is defined recursively by 
Hints:  (a) Show that 
11 T,,(J) - T,,(.J’)l d allJ - J’II 
11 T(J)  - T(J’)II G allJ - J’II 
V J ,  J’ E B(S), p E M ,  
VJ, J‘ E B(S), 
and use the contraction mapping fixed point theorem. (b) Use the fact that J ,  2 T(J,) 2 ... 2 Tk(J,) 2 ... to show that 
inf,, J , ( x )  2 J * ( x ) .  To prove the reverse inequality, for any F: > 0, let p E M be such that 
J*(x) 2 T,,(J*)(x) - & V X E S .  
284 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Use the contraction assumption and the above inequality to show that for all k = 1 ,2 , .  . . , 
T!(J*)(x)  2 T!+'(J*)(X) - Uk& 
J*(x) 2 J,(x) - [&/(1 - u)] 
v x  E s, and conclude that 
v x  E s. Use the above argument to show that 
J*(x) = inf lim (Tp0. . . T,,)(J*)(x) Vx E S.  pi. i=O.l. ... k - t m  
(c) Show that 
11 Tr(J)  - Tr(J')II < U I ~ J  - J'II V J ,  J' E B(S), p E M ,  
II T"(J) - T"(J')II < allJ - J'll VJ, J' E B(S). 
(f) Show that the following relations hold: 
5. Consider a problem similar to that of Section 6.1 except for the fact that when we are at state xk there is a probability p, where 0 < p c 1, that the next state xk+ will be determined according to xk+ = f ( x , ,  uk, wk) and a probability (1  - p) that the system will move to a termination state where it 
stays permanently thereafter at no cost. Show that even if u = 1 (no dis- counting) the problem can be put into the discounted cost framework. Use the results of Problem 4 to analyze the case where p depends on u and 
0 < inf p(u) < sup p(u) < 1 .  u c c  uec 
6. Consider a problem similar to Problem (D) under Assumption B except for the fact that the discount factor u depends on the current state xk, the control uk, and the disturbance wk, i.e., the cost functional has the form 
(N- 1 -l 
PROBLEMS 285 
with a(x, u, w )  a given function satisfying 
0 < inf{a(x, u, w ) l x  E S ,  u E C,  w E D }  
< s u p { c c ( x , u , w ) J x E S , U E C , W E D }  < 1. 
Show that the results and algorithms of Sections 6.1 and 6.2 have direct counterparts for such problems. 7. Let J :  S + R be any bounded function on S and consider the successive 
approximation method of Section 6.2 with a starting function J :  S + R of 
the form 
where r is some scalar. Show that the bounds T k ( J ) ( x )  + ck, T k ( J ) ( x )  + '?k on J*(x)  of Proposition 4 are independent of the scalar r for all x E S .  Show also that if S consists of a single element 2 (i.e., S = {Z}), then 
J ( x )  = J(x )  + r V X E S ,  
T(J)(j?) + c1 = T(J)(Z) + 2,  = J*(Z).  
8. Consider Problem (D) under Assumption P or N. Show that for any probability distribution {pl, p 2 , .  . .} defined on { x ' ,  x 2 , .  . .}, a countable subset of S ,  we have 
m 
Hint :  If J*(xi) is equal to + co (under Assumption P) or - co (under 
Assumption N) for some i for which p i  > 0 the result is evident. So assume 
J*(xi) # _+ co for all i. We have 1s piJ*(x i )  < inf, 1 g  piJ,(xi)  so it 
remains to prove the reverse inequality. For a given E > 0 consider for each x i  an admissible policy of the form 
such that no(xi) = {Bo( * ), P W ,  * 1, P W ,  * ), * . .I, 
m m 
Notice that no(xi) represents a different policy for each x i  and $(xi,  x j )  re- presents the control applied when the initial state is x i  and the state at timej is x i .  
Let Assumption P hold and consider a sequence { E k }  with &k > 0, Vk,  and l k m , l  ck = E .  Write 
m m 
m 
286 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
where 
Show that one may find a policy of the form 
such that m m 
and with f i l ,  pj satisfying f i l (x l )  E U(xl )  Vxl E S,  and pf(xl ,  x j )  E U(xj), Vx,, x j  E S , j  = 2,3, . . . . Note that the values of pj depend on x 1  and xi but not on xi. Notice also that the policy 7cl is not an admissible policy according to our definition since the control pj(xl ,  x j )  applied at timej 2 2 depends on the state x 1  (which has occurred at time 1) as well as the current state x j .  
Similarly proceeding, show that one may find a policy of the form 
=k = { f i O ( ' ) , f i l ( ' ) , . . . , f i k ( ' ) ,  p I :+ l (xk , ' ) ,CLI :+2(xk , ' ) , . . . } ,  
such that 
where 
m k m k -  1 
Consider the policy ?r = {Po, E l ,  . . .} and use the above inequalities to show that 
m m 
i= 1 i= 1 
PROBLEMS 287 
Under Assumption N show that for each N there exists an admissible policy of the form zN = {fro, f i y , .  . . , fii, p, p, . . .} such that 
Show that m m m 
Hence there exists an N such that 
._ 
1 PiJ,,(X') < c PiJ*(X') + 3E. 
i =  1 i =  1 
For detailed proofs see Theorems 4.3 and 4.4 of Strauch [S17] or Hinderer 
9. Let S = [0, a), C = U(x)  = (0, a), be the state and control spaces, 
respectively, let the system equation be 
~ ~ 9 1 .  
xk+ 1 = (2/a)xk + u k ,  k = 0, 1, . . . , 
where a is the discount factor, and let 
dxk ,  u k )  = xk + u k  
be the cost per stage. Show that for this deterministic problem Assumption P is satisfied and that J*(x) = co Vx E S,  but Tk(Jo)(0) = 0 for all k [ J o  is the zero function, Jo(x) = 0 Vx E S] .  10. Verify that all the results of Section 6.4 proved under Assumption P hold if the cost per stage g satisfies 
0 < g(x, u, w)  < + co V(x, u, w )  E S x c x D. 
11. Consider Problem (D) for the case of a deterministic problem involving a.linear system 
xk+l = Ax, + Buk, k = 0, 1, ..., 
where the pair (A, B) is controllable and x k  E R", u k  E R". Assume no con- straints on the control and a cost per stage g satisfying 
0 < g(x, u )  V(x, u )  E R" x R". 
Assume furthermore that g is continuous in x and u, and that g(x,, u,) -+ + co 
if {x,} is bounded and Iu,( -+ +a. 
288 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
(a) Show that for a discount factor a E (0, 1) the optimal cost satisfies 0 < J*(x) < + 00, Vx E R". Furthermore there exists an optimal stationary policy and 
lim Tk(Jo) (x )  = J*(x)  Vx E R". k - a ,  
(b) Show that the same holds true except perhaps for J*(x)  < +co when the system is not linear but rather is of the form = f ( x k ,  uk), 
withf: R" x R" + R" being a continuous function. 
Prove the same results assuming that the control is constrained to lie in a compact set U c R"(U(x) = U ,  Vx E R") in place of the assumption g(x,,  u,) + + 00 if {x,} is bounded and 1 u, 1 + + 00. 
Hint: Show that Tk(Jo)  is real valued and continuous for every k and use Proposition 13. 12. Under Assumption B let p :  S + C be such that p(x)  E U ( x )  Vx E S ,  and 
(c) 
T,(J*)(x)  = E { S C X ,  A x ) ,  wl  + mJ*Cf(x, p ( 4 ,  w ) l )  W 
= J*(x)  + E v x  E S.  
Show that 
J*(x)  d J,(x) d J*(x) + [ E / (  1 - a)] Vx E S.  
Hint: Show that T:(J*)(x)  < J * ( x )  + 1. k - 1  i 
r = O  a&.  
13. Generalized Policy Iteration Algorithm The purpose of this problem is to provide a policy iteration algorithm for the case where the state space and the control space are not necessarily finite sets. Under Assumption B let 
{p, p, . . .} be an admissible stationary policy and let 1,: S + R be such that 
SUP I j&) - J,W I < 7. 
su JJ' (x)  - T ( j , ) ( x ) (  < 6 .,B 
x o s  
Let J': S + R be such that 
and assume that 
Show that for all x E S there holds 
J*(x) d J,(x) d J*(x)  + [(S + ~)/(1 - a)] + y. (102) 
PROBLEMS 289 
Consider the following policy iteration algorithm, for fixed y, S ,  c > 0. (1) Start with an admissible stationary policy no = {po, po, . . .}. (2)  Given {pi, pi, . . .} find J,i: S + R such that (Jpi(x) - J,i(x)I < pi 
(3) Find pi+': S + C with p i + l ( x )  E V(x) for all x E S such that 
for all x E S. 
T,,+ QPi)(x) < T ( J , ~ ) ( x )  + 6a' vx E S. 
If SUP, ,~J  T,i+ I(Jpi)(x) - J,i(x)l < E stop. Otherwise replace pi by pi+' and 
go to Step 2. 
Show that the algorithm will terminate after a finite number of iterations (say k) and that 
uk-'6 + & 
1 - u  J*(x)  < JJX)  < J*(x)  + + y o l k - '  v x  E s. 
Hint: To show inequality (102) use the fact that for any fl > 0 there exists a k such that for all x E S 
1 T k + ' ( J p ) ( x )  - J*(x)J < p. 
Then use the inequalities 
I Jp(4 - J*(x )  I < lJ,(X) - T(J,)(x)I + I T(J,)(x) - TZ(J,)(x)1 
+ * * * + I Tk"(J,)(X) - J*(x)l 
X €  ! < su lJ,(x) - T(J,)(x)l(l + u + . - .  + ak) + p 
to show that 
vx E s. 
To show that the policy iteration algorithm will terminate in a finite number of iterations, assume the contrary, i.e., we have 
for all i and the algorithm generates an infinite sequence of policies {d}. Show first that for all x E S and i = 0, 1, . . . , we have 
T,i+l(J,i)(x) < T(J,i)(x) + (6 + 2ya)u' < J,i(x) + (6 + 2yu)a'. 
290 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
Use this inequality to show that for all x E S and i, k ,  k- 1 
T:i+ I(J,i)(x) < T(J, i ) (x)  + (6 + 2y~r)~r' 1 04, 
j = O  
and conclude that for all x E S and i = 0, 1, . . . , 
J*(x)  < J,i+ I ( x )  d T(J, i ) (x)  + ,lai, 
where 
1 = (6 + 2ya)/(l - a). 
Show that for all x E S and i = 1,2 ,  . . . , J*(x)  < J,i(x) ,< T' (J ,~ ) (X)  + iai-'L, 
and conclude that 
lim SUP 1 J,i(x) - J*(x)  1 = 0. 
i-m x s S  
Use this equality to reach a contradiction. 14. The purpose of this problem is to show that the successive approxi- mation method of Section 6.2 will yield an optimal policy after a finite number of iterations when S ,  C ,  and D are finite sets. Under Assumption B let J :  S -+ R be a function such that for some E > 0 and all x E S we have 
IJ(x) - J*(x)l ,< E.  
Let p(x) be such that for all x E S we have p ( x )  E V ( x )  and 
T,(J)(x) = E { S C X ,  A x ) ,  W I  + uJCf(x ,  pL(x), w)l>  W 
(a) Show that for all x E S 
I T,(J) (x)  - J(x )  I d (1 + COE. 
I T,(J)(x) - J,WI d C 4 1  + 4/(1 - 4IE. 
J*(x) < J,(x) < J*(x) + [ 2 E / ( 1  - a)]. 
(b) Using the above inequality show that for all x E S ,  
(c) Show that for all x E S ,  
(d) Assume that the state, control, and disturbance spaces are finite sets. Show that the successive approximation method after some index will yield 
PROBLEMS 291 
an optimal policy at every iteration, i.e., for any starting function J : S + R 
there exists an index k such that if p* is such that 
7',,4Tk(J)] = T k f l ( J )  and k 2 k, 
then {p*, p*, . . .} is optimal. 15. Under Assumption P or N show that if 3:  S + R is a bounded function 
satisfying 16. Prove the following strengthened version of part (b) of Proposition 9: Under Assumption N if 3:  S + [ - 00, 00) is bounded above and satisfies 
1 < T ( j ) ,  then 3 < J*. 
17. Linear-Quadratic Problems with Nonstationary Disturbances Con- sider the linear-quadratic problem of Section 6.5 with the only difference that the disturbances wk have zero mean but their covariance matrices are non- stationary and uniformly bounded over k. Show that the optimal control law remains unchanged. 18. Periodic Linear-Quadratic Problems Consider the linear system 
= T(J), then 3 = J*. 
X k + l  = AkXk + B k U k  + W k ,  k = 0, 1,. . . ., and the quadratic cost functional 
CN- 1 
where the matrices above have appropriate dimensions, Qk and Rk are positive semidefinite and positive definite, respectively, for all k, and 0 < a < 1. Assume that the system and cost functional are periodic with period p (cf. Section 6.7), that the controls are unconstrained, and that the disturbances are independent, have zero mean, and finite covariance matrices. Assume further that the following (controllability) condition is in effect. 
Given any initial state x0 there exists a finite sequence of controls {p0, is1, .  . . , u,} such that K,, = 0 where x,, is generated by - 
- 
xk+l = AkXk + B&i&, k = 0, 1,. . . , r .  
Show that there is an optimal periodic policy 7c* of the form 
* * *  n* = {Po*, p:, . . ., pp-1, P o ,  P l ,  . . . Y & - l ,  f * .I, where PO* ,  . . . , p:- are given by 
p;(x) = - ~ ( U B : K ~ + ~ B ~   R i ) - ' B I K i , , A i x ,  i = 0,. . . , p - 2, 
pP-1(x )  * = -a(aBb-,KOB,-,  + RP-1)- 'Bb-1KoAp-1x 
292 6 MINIMIZATION OF TOTAL EXPECTED VALUE-DISCOUNTED COST 
and the matrices K O ,  K,, . . . , K,- , satisfy the coupled set of p algebraic 
Riccati equations given by 
Ki = A : [ a K i + ,  - a2Ki+,Bi(aB:Ki+,Bi  + R i ) - ’ B : K i + , ] A i  + Q. 1 9  
i = O , l ,  ..., p - 2 ,  
K,- , = A;-  ,[aK0 - a Z K o B p -  ,(ctBp- ,K0B,-  
+ Rp-l)-’Bp-lKo]Ap-l + QP-,. 
Hint: Use Eqs. (99) and the compactness condition (10 1). 19. Discounted Linear-Quadratic Problems with Imperfect State Informa- tion Consider the linear-quadratic problem of Section 6.5 with the difference that the controller, instead of having perfect state information, has access to measurements of the form 
Similarly, as in Section 4.3, the disturbances V k  are independent, have identical statistics, zero mean, and finite covariance matrix. Assume that for every admissible policy II the matrices 
E { [ x k  - E { X k I I k } l [ X k  - J ! ? { X k I l k } l ’ l n }  
are uniformly bounded over k, where is the information vector defined in Section 4.3. Show that the optimal policy is n* = {p*, p*, . . .}, where ,u* is given by 
Show also that the same is true if wk,  vk are nonstationary with zero mean and covariance matrices that are uniformly bounded over k. 
Hint: Combine the theory of Sections 4.3 and 6.7. Use the compactness condition of Proposition 13. 20. Periodic Inventory Control Problems In the inventory control problem of Section 6.6 consider the case where the statistics of the demands wk, the prices c k ,  and the holding and the shortage costs are periodic with period p. Show that there exists an optimal periodic policy of the form n* = {p:, 
. . . ,  P p -  1, P o ,  * *  . 1  Pf- 1 , .  . .I, 
S: - x if x 6 S:, 
i = O , l ,  ..., p -  1 ,  otherwise, 
where S:, . . . , Sf- , are appropriate scalars. 
Hint Use Eqs. (99) and the compactness condition (101). 
PROBLEMS 293 
21. Consider the problem of this chapter under Assumption B for the case where the sets S ,  C ,  and D are finite sets. Using the notation of Section 6.2 consider the controlled system 
P k + i  = PkP,,,, k = 0, 1 , .  ., where P k  is a probability distribution over S viewed as a row vector, and P,, 
is the transition probability matrix corresponding to a function pk: C + S 
with pk(i) E U(i) for all i E S.  The state is P k  and the control is pk. Consider also the cost functional 
N- 1 
Show that the optimal value function and an optimal policy for the deter- ministic problem involving the system and the cost functional above yield the optimal value and an optimal policy for the problem of this chapter. 22. Let Assumption P hold and assume that n* = {p:, py, . . .} E l satisfies J* = T,;( J*)  for all k .  Show that n* is optimal, i.e., J,, = J*. 23. Under Assumption P show that given d > 0 there exists a policy ng€II  such that J, , (x)  < J*(x)  + &' for all X E S .  and that for c( < 1 the policy xE can be taken stationary. 
Hint: Let { d k }  be a sequence such that 8, > 0 for all k and ork€,  = 8. For each x E S let .,+[XI = { p ~ [ x ] ,  &[XI,. . .} E n be such 
that J n k [ x l ( ~ )  < J * ( x )  + bl,. Define ,iik(X) = p k [ x ]  ( x )  and let ng = { p o ,  p , ,  . . .}. 24. Under Assumption P show that if there exists an optimal policy, i.e., a policy x* E ll such that J,, = J*, then there exists an optimal stationary policy. 25. Use the following counterexample to show that the result of Problem 24 may fail to hold under Assumption N if J*(x)  = - m for some x E S .  Let 
p(w = OIx = 0, u )  = *, p(w = l l x  = I ,  u )  = 1. Show that J*(O) = -a, J*( 1 )  = 0, and that the admissible nonstationary policy {p:, p:, . . .} with p t ( 0 )  = - ( 2 / ~ r ) ~  is optimal. Show that any admissible stationary policy {p, p, . . .} satisfies J,(O) = [2 / (2  - a)]p(O), J,(l) = 0 (see [B22] ,  [DS], 
[ 0 2 ]  for related analysis). 
S = D = (0, l } , , f ( ~ ,  U  N') = W, g(x .  U, W) = U, U(0) = (-m, 01, U(1) = {0}, 
Chapter 7 
Minimization of Total Expected 
Value - Undiscounted Cost 
In this chapter we consider infinite horizon problems with undiscounted cost functionals. The basic problem we consider is identical with Problem (D) of the previous chapter except for the absence of the discount factor. Again we assume stationarity of the system and the cost per stage. However, non- stationary or periodic problems may be treated by reduction to the stationary case similarly as in Section 6.7. 
PROBLEM (U) Consider the stationary discrete-time dynamic system 
x k + l  = f ( x k ,  uk, wk)?  = O, 1, ... 9 (1) 
where the state xk, k = 0, 1, . . . , is an element of a space S, the control uk, k = 0, 1,. . . , is an element of a space C, and the random disturbance 
wk, k = 0, 1, . . . , is an element of a space D. It is assumed that D is a countable set. The control uk is constrained to take values in a given subset v(xk)  of C that depends on the current state xk [ U k  E v(xk),  k h k  E S,  k = 0, 1, . . .]. The random disturbances wk, k = 0, 1, . . . , have identical statistics and are characterized by probabilities P( - I xk, uk) defined on D, where P(wk 1 xk,  uk) denotes the probability of wk occurring when the current state and control 
294 
7 MINIMIZATION OF TOTAL EXPECTED VALIJE 295 
are xk and uk, respectively. The probability of wk may depend explicitly on x k  and uk but not on values of prior disturbances wk- 1,  . . . , wo. 
Given an initial state x o ,  the problem is to find a control law, or policy, = { P o ,  pi, . . .}, where pk: S c, ,b!k(xk) E u(xk) for all xk E S ,  k = 0, 1,. . , 
that minimizes the cost functional 
(2) I Jz(x0) = lim E 1 gCxk, p k ( x k ) ,  w k l  
N + w  wk i"- k = O  
k = O ,  1 ,  ... 
subject to the system equation constraint (1). The real-valued function g :  S x C x D + R is given. 
One of the main difficulties introduced by the absence of the discount factor is that now the value of the cost functional (2) may be infinite for some (possibly all) initial states even when costs per stage are bounded. For this reason Problem (U) makes sense in the case where g 2 0 only when the opti- mal value function 
J*(x)  = inf J,(x) V x  E S n 
takes finite values for at least some initial states, for otherwise every ad- missible policy is optimal. This type of difficulty is of the same nature as the one we encountered in connection with discounted problems with unbounded costs per stage (Section 6.4). As in Section 6.4 we shall allow the possibility that the functions J ,  and J* may take the value + 00 or - co, i.e., they may 
be extended real valued. 
As in the previous chapter we need to impose assumptions on the cost per stage function g that guarantee that the limit in (2) exists in the sense that it is a real number or kco. We shall be considering the following two assumptions, which closely parallel the corresponding assumptions P and N of Section 6.4. 
Assumption P The function g in the cost functional (2) satisfies 
0 < g(x ,  u, w)  V(x ,  u, w) E S x C x D. 
Assumption N The function g in the cost functional (2) satisfies 
g ( x ,  u, w) < 0 V(x,  u, w)  E S x C x D. 
There is, however, an important difference between the assumptions above and those of Section 6.4. While in Section 6.4 the assumptions made could be replaced by the assumption that g(x ,  u, w) is bounded below or above without affecting the results obtained, this is not true anymore for Problem (U)-a complication due again to the absence of the discount factor. 
296 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Nonetheless, the results to be obtained in the next section for Problem (U) under Assumptions P and N are very similar to those of Section 6.4. Once we develop these results we shall examine some special cases in Sections 7.2-7.4. 
7.1 Convergence and Existence Results 
As in the previous chapter we shall consider mappings Tfl operating on functions J that are defined on S and take values in [0, +a], when 
working under Assumption P, and in [ - “o, 01 when working under Assump- 
tion N. The mapping T is defined by 
T ( J ) ( x )  = inf E {g(x ,  u, w) + JCf (x ,  u, W)l), (3) u e U ( x )  w 
and the mapping 71 = {P,  p, . . .I by 
is defined for every admissible stationary policy 
(4) 
Again we write for any two functions J ,  J’ mapping S into [0, +a] or 
J < J’ if J ( x )  < J’(x)  Vx E S .  
T,(J)(x)  = E { S C X ,  A x ) ,  w1 + J C f k  P ( 4 ,  W)N- W 
c- a, 01, 
Clearly we have the monotonicity relations 
J < J’ =. T ( J )  < T(J‘), T,(J) < TJJ’). ( 5 )  
We again denote by J*(x )  the optimal value of Problem (U) when the initial state is x ,  and by J,(x)  the value of the cost functional (2) corresponding to an admissible stationary policy {p ,  p, . . .} and an initial state x .  
The following result can be proved by an almost verbatim repetition of the proof of Proposition 8 in Section 6.4. 
Proposition 1 (Optimality Equation) Under either Assumption P or N the optimal value function J* of Problem (U) satisfies 
J*(x)  = inf E {g(x ,  u, w) + J * [ f ( x ,  u, w)]} Vx E S ,  (6) UEU(X) w 
or in terms of the mapping T of (3), 
J* = T(J*). (7) 
Corollary 1.1 Let { p ,  p, . . .} be an admissible stationary policy. Then under Assumption P or N we have 
J,W = E { d x ,  d x ) ,  wl + J,Cf(x,  A x ) ,  W)lL (8) W 
7.1 CONVERGENCE AND EXISTENCE RESULTS 2!n 
or equivalently in terms of the mapping T, of (4) 
J ,  = T,(J,). (9) 
The following propositions and corollaries may be proved by essentially 
Proposition 2 (a) Under Assumption P if]: S -, [0, + a31 is a function 
(b) Under Assumption N if 1: S -, [ - 00, 01 is a function that satisfies 
Corollary 2.1 Let II = {p, p, . . .} be an admissible stationary policy. 
(a) Under Assumption P if 1: S -, [0, + a11 is a function that satisfies 
1 = 7',,(]), then J ,  < 1. 
(b) Under Assumption N if J: S -, [ - oo,O] is a function that satisfies 
1 = T,(]), then 3 d J , .  
Corollary 2.2 (Necessary and Sufficient Condition for Optimality under Assumption N) In order for an admissible policy II* = {p*, p*, . . .} to be optimal under Assumption N it is necessary and sufficient that 
repeating the proofs of the corresponding results of Section 6.4. 
that satisfies 1 = T(j ) ,  then J* < 3. 
J" = T(J"), then d J*.  
J,* = T,*(J,,*) = T(J,*), 
or equivalently 
J,*(x) = E {gCx, P*(X), WI + J,*Cf(x, P*(X), w)l} 
d E {g(x ,  u, w) + J , * [ f ( x ,  u, w)]} 
W 
v x  E S ,  u E U X ) .  (10) W 
Proposition 3 (Necessary and Sufficient Condition for Optimality under Assumption P) In order for an admissible policy n* = {p* ,  p*, . . .} to be optimal under Assumption P, it is necessary and sufficient that 
J* = T,*(J*) = T(J*), 
or equivalently 
J*(x)  = E {gCx, P * ( X ) ,  WI + J*Cf(x ,  P * ( X ) ,  W)ll W 
d E {g(x ,  u, w) + J * [ f ( x ,  u, w)]} v x  E S ,  u E U X ) .  (1 1) W 
Successive Approximation- Policy Iteration- Linear Programming 
We turn now to the question of convergence of the DP algorithm to the optimal value function J*. Similar results as those of Section 6.4 may be obtained. Let J o  be the zero function on S, i.e., 
J,(x) = 0 vx E S .  
298 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Consider the D P  algorithm that generates T(Jo), T2(Jo),  . . . , Tk(Jo), .. . . Each of the functions Tk(Jo) represents the optimal value function for a corresponding finite horizon problem with k stages. We have under Assump- tion P that 
J o  < T(J0) d . . . < Tk(Jo)  < . . . , 
J o  2 T(J0) 2 . . . 2 Tk(Jo)  
J,(x) = lim Tk(Jo) (x )  Vx E S ,  (12) 
while under Assumption N * .  . . 
In either case the pointwise limit function J , ,  where 
k-.  m 
is well defined as a function from S into [0, + 001 under Assumption P or 
into [- co, 01 under Assumption N. As in Section 6.4, we have 
Let Assumption P hold and assume that J ,  = T(J,). Then 
Proposition4 (a) 
J ,  = J * .  
(b) Let Assumption N hold. Then 
J ,  = J * .  
As in the corresponding discounted case it need not be true that J ,  = J* under Assumption P(a counterexample is provided by Problem 9 of Chapter 6 by setting a = 1). As in Section 6.4 we have the following sufficient condition for J ,  = J*. 
Proposition 5 Let Assumption P hold and assume that the sets 
are compact subsets of a Euclidean space for every x E S, A E R, and for all k greater than some integer E .  Then 
J ,  = T(J,) = J * .  
Furthermore, there exists an optimal stationary policy. 
Note that when U ( x )  is a finite set for every x E S the assumption of the above proposition is satisfied. 
Propositions 4 and 5 form the basis for a successive approximation method for computing in the limit the optimal value function J*. An alternative method for computing J* under Assumption N is based on the following proposition. A related result under P is given in Problem 16. 
7.1 CONVERGENCE AND EXISTENCE RESULTS 299 
Proposition 6 Under Assumption N if 1: S -, [- co, 01 is a function 
such that j < T ( f ) ,  then f < J*. 
Proof Since j d J o  we have 
T k ( f )  d Tk(Jo), 
from which, using the fact that limk+w T k ( J o ) ( x )  = J , ( x )  = J*(x) ,  we obtain 
lim sup T ~ ( ~ ) ( X )  < J * ( x )  vx E S .  k+  w 
On the other hand, we have f d T ( f )  implying j ( x )  < lim supk+a, T k ( j ) ( x )  for all x E S ,  and the result follows. Q.E.D. 
Based on the preceding proposition we have that if S is a finite set, 
S = { 1,2, . . . , n}, and C is also a finite set, C = { u ' ,  . . . , urn}, then J*(l), . . . , 
J*(n) solve the linear programming problem (cf. end of Section 6.2) 
n 
max CAi l i d 0  i =  1 
subject to 
n 
Ai < g(i, uk) + 1 pij(uk)ilj i = 1, 2, . . . , n, uk E V(i) ,  
j =  1 
where the notation corresponds to that of Section 6.2. Under Assumption P it is possible to use a policy iteration algorithm 
in an effort to find J* and an optimal stationary policy. The algorithm is motivated by the following proposition, which parallels Proposition 7 of Section 6.2. A similar proposition cannot be proved under Assumption N in the absence of additional assumptions. 
stationary policy. If (11, ,ii, . . .} is another admissible policy such that 
Proposition 7 Let Assumption P hold and let {p, p, . . .} be an admissible 
then 
300 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
d J,(xo) 
and the result is proved. Q.E.D. 
Notice that the proposition states that the policy { p ,  p ,  . . .} is no worse than {p, p, . . .} but does not guarantee a strict improvement. When J;: = J ,  the most that one can obtain is that 
J ,  = T(J,). 
In the discounted case with bounded costs per stage, the above equality implied optimality of {p, p, . . .}, but this is not necessarily true under our present assumptions. Nonetheless, we shall be able to use Proposition 7 to construct a policy iteration algorithm in Section 7.4. 
7.2 Optimal Stopping 
Consider a situation where at each state x of the state space there are two possible actions available. We may either stop (control u ' )  and pay a terminal cost t (x) ,  or pay a cost c(x)  and continue the process (control u z )  according to the system equation 
(14) 
The objective is to find the optimal stopping policy that minimizes the total expected costs over an infinite number of stages. It is assumed that the input disturbances wk in (14) have the same probability distribution for all k ,  which depends only on the current state x k .  
X k + l  = fc(xk, wk), k = 0, 1,. . . . 
Proof Using the hypothesis and the facts J ,  = TJJ,), J ,  2 0 (by Assumption P) we have, for any initial state xo, 
7.2 OPTIMAL STOPPING 301 
In order to put this problem within the framework of Problem (U) we introduce an additional state s (termination state) and we complete the system equation (14) as in Section 3.4 by letting 
xk+l = s if uk = u1 or xk = s. 
No further cost is incurred once the system reaches the termination state. In other words if the termination action is taken, the system is driven to the termination state s, and if the system is already in the termination state, it remains there permanently (i.e., s is an absorbing state). 
We shall assume in this section that 
t(x) 2 0, c(x) 2 0 vx E s. (15) 
The case where t ( x )  < 0 and c(x) < 0 for all x E S is treated in Problem 10. Actually whenever there exists an E > 0 such that c(x) 2 E for all x E S, the results to be obtained apply also to the case where 
inf t(x) > - 00, 
i.e., when t(x) is bounded below by some scalar rather than bounded by zero. The reason is that if c(x) is assumed to be greater than E > 0 for all x E S,  any policy that will not stop within a finite expected number of stages results in infinite cost and can be excluded from consideration. As a result if we reformulate the problem and add a constant r to t ( x )  so that t(x) + r 2 0 for all x E S, the optimal cost J*(x) will be merely increased by r,  while optimal policies will remain unaffected. 
Now under our assumptions the problem clearly falls within the frame- work of Problem (U) provided the disturbance space D is a countable set. Furthermore, Assumption P is satisfied by virtue of (15). The mapping T of (3) takes the form 
X E S  
T(J)(x) = minCt(x), c(x) + E { J [ f , ( x ,  w)X1 Vx E S, (16) W 
where t ( x )  is the cost of the termination action i t 1  and c(x) + E ,  {J[f,(x, w)]} is the cost of the continuation action u 2 .  To be precise we should also define T(J)(s)  = 0 where s is the termination state. However, in what follows the value of various functions at s is immaterial and will not be explicitly considered. 
By Proposition 1 the optimal value function J* satisfies 
J* = T(J*). 
Since the control space has only two elements, by Proposition 5 we have 
lim Tk(J,)(x) = J*(x) Vx E S, (17) k-m 
302 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
where J o  is the zero function (Jo(x)  = 0, Vx E S). By Proposition 3, there exists a stationary optimal policy {p* ,  p*, . . .} described as follows: 
Stop if t(x) < c(x) + E {J* [ f , (x ,  w)]}. 
Continue if t(x) 2 c(x)  + E {J*[fc(x ,  w)]}. 
Let us denote by S* the optimal stopping set (which may be empty) 
W 
W 
r 
and by s* its complement in S: 
s* = (x E SIX 4 S*} = x E S ( t ( x )  2 c(x)  + E {J*[fc(x, w)]} . r W 1 
The set S* is the, set of states where stopping is optimal. Consider also the sets 
and their complements in S, 
s k  = x s I t(x) 2 c(x) + E { Tk(JO) [fr(x, w)]} a { W I The stopping sets S1, S1, . . . , s k ,  . . . determine the optimal policy for finite 
horizon versions of the stopping problem and are determined via the successive approximation method. Since we have 
Jo < T(J0) < . . . < Tk(Jo) < f * * < J*, 
it follows that S1 c ... c Sk c ... c S* and S ,  =I ... 3 3, 3 ... 3 S*. 
Now for any state I E S k  we have for all k, 
t(2) 2 c(I) + E {Tk(J,)[f ,(Z, w)]}, k = 0, 1, . . . , 
W 
and by taking limits and using (17) we obtain 
t ( 3  2 42) + E {J*Cf,(f, W)N, W 
from which 2 E S*. Hence W 
S* n s,, 
k =  1 
7.2 OPTIMAL STOPPING 303 
which, in conjunction with the fact, that s k  =I s* for all k, yields 
cc 
s* = n s k ,  
k =  1 
or equivalently m 
s* = u s k .  
k =  1 
In other words, the optimal stopping set S* for the injnite horizon problem is equal to the union of all thejnite horizon stopping sets Sk. 
Notice that in the case where the state space is a h i t e  set, (18) shows that the successive approximation method will determine the optimal stopping set in a finite number of iterations. Also when the state space is a finite set, some additional results of analytical and computational importance may be proved for the optimal stopping problem. These results will be developed in the context of a more general problem in Section 7.4. The remainder of this section is devoted to examples. 
ASSET SELLING EXAMPLE Consider the asset selling example of Sections 3.4 and 6.1 (see also Problem 3.10) where the rate of interest r is zero and there is instead a maintenance cost c > 0 per period for which the house remains unsold. We have the following equation for the optimal cost: 
J*(x)  = max x, - c  + E { J * ( w ) }  . (19) [ . .  1 
In this equation x takes values in a bounded interval of the form [0, MI, where M is some positive scalar that bounds the possible offers from above. Notice that in this particular case we consider maximization of total expected reward and the termination reward x is positive. Hence assumption (15) is not satisfied. Since, however, the termination cost is bounded, our analysis of this section is still applicable [cf. the discussion following (15)]. 
Now from (19) we obtain an optimal stationary policy of the form 
If the current offer exceeds - c  + E ,  {J*(w)} ,  sell the asset; otherwise 
The threshold level - c  + E ,  {J*(w)}  may be obtained in a similar 
do not sell. 
manner as in Section 3.4. 
HYPOTHESIS TESTING EXAMPLE-SEQUENTIAL PROBABILITY RATIO TEST 
Consider the hypothesis testing problem of Section 4.5 for the case where thenumber of possible observations is unlimited. The state space is S = [0,1], i.e., the space of the sufficient statistic 
P k  = P(xk = xoIzO, 21,. . 9 zk) 
304 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
augmented with a termination state s, which will not be explicitly considered in the expressions below. To each state p E [0, 11 we may assign the termina- tion cost 
t(p) = minC(1 - PILO,  pL11, 
i.e., the cost associated with optimal choice between the distributions fo and f,. The mapping T of (16) takes the form 
where the expectation over z above is taken with respect to the probability distribution 
P(Z)  = PfO(4 + (1 - PlfI(4 vz E z. 
The optimal value function J* satisfies 
(1 - p)Lo, pL1,  c + 
and is obtained in the limit through the equation 
J*(p) = lim Tk(Jo)(p) V p  E [O, 11, k -  w 
where J o  is the zero function on [0, 11. Now consider the functions Tk(Jo), k = 0, 1,. . . . It is clear that 
. < Tk(Jo) < . . . < min[(1 - p ) ~ ~ ,  p , ] .  J~ < T(J,) < 
Furthermore, in view of the analysis of Section 4.5 we have that the function Tk(Jo) is concave on [0, 11 for all k.  Hence the pointwise limit function J* is also concave on [0, 11. In addition, we have clearly from (20) that 
J*(p)  < min[(l - p)Lo, &I. J*(O) = J*(1) = 0 and 
It follows from (20) and Fig. 7.1 that [provided c < LoL,/(Lo + L,)] there exist two scalars Cr, f i  with 0 < B < Cr < 1 that determine an optimal stationary policy of the form 
Accept fo if p 2 Cr. Accept fl if p < fi. Continue the observations if f i  < p < Cr. 
In view of the optimality of the stationary policy above, the employment of the sequential probability ratio test described in Section 4.5 is justified when the number of possible observations is large and tends to infinity. 
7.3 OPTIMAL GAMBLING STRATEGIES 305 
\ /‘ / 
pl. , ,/’ 
/ 
/’ 
‘\ ( 1  - P ) I , o  
\ 
\ 
Accept ,ji Con tin ue Accept fo observations 
I I 
FIGURE 7.1 
7.3 Optimal Gambling Strategies 
A gambler enters a certain game played as follows. The gambler may stake at any time k any amount uk 3 0 that does not exceed his current fortune xk (defined to be his initial capital plus his gain or minus his loss thus far). He wins his stake back and as much more with probability p and 
he loses his stake with probability (1 - p). Thus the gambler’s fortune 
evolves according to the equation 
(21) X k f l  = x k  + wkuk, k = 0, 1,. . . 3 
where wk = 1 with probability p and wk = - 1 with probability (1 - p). 
Several games, such as playing red and black in roulette, fit the description given above. 
The gambler enters the game with an initial capital xo and his goal is to increase his fortune up to a level X. He continues gambling until he either reaches his goal or loses his entire initial capital, at which point he leaves the game. The problem is to determine the optimal gambling strategy for maximizing the probability of reaching his goal. By a gambling strategy we mean a rule that specifies what the stake should be at time k when the gam- bler’s fortune is xk for every x k  with 0 < xk < X .  
The problem may be cast within the framework of Problem (U) where we consider maximization in place of minimization. Let us assume for 
306 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
convenience that fortunes are normalized so that X = 1. The state space is the set [0, 13 u {s}, where s is a termination state to which the system moves with certainty from both states 0 and 1 with corresponding rewards 0 and 1. When xk  # 0, x k  # 1, the system evolves according to Eq. (21). The control constraint set is specified by 
o < u k < x k ,  o < u k <  1 - x k .  
The reward per stage when xk # 0, xk # 1 ,  is zero. Under these circumstances the probability of reaching the goal is equal to the total expected reward. Assumption N holds since the problem under consideration is equivalent to a problem of minimizing expected total cost with nonpositive costs per stage. 
The mapping T of (3) takes the form 
T ( J ) ( x )  = 
T(J ) (O)  = 0, 
sup cpJ(x + u )  + ( 1  - p)J(x - u)] v x  E (0, l), 
o s u < x  
O<u<l-x 
T(J)(l) = 1 
for any function J :  [0, 11 -+ [0, +a] .  Actually for this problem one 
restrict attention to functions J taking values in the interval [O, 11 J(0) = 0, J(1)  = 1. 
Consider now the case where 
i.e., the game is unfair to the gambler. A discretized version of the case where 3 < p < 1 is considered in Problem 15. When 0 < p < 9 it is intuitively clear that if the gambler follows a very conservative strategy and stakes a very small amount at each time, he is all but certain to lose his capital. For example, if the gambler adopts a strategy of betting l/n at each time, then it may be shown [A8, p. 1821 that his probability of attaining the target fortune of unity starting with an initial capital i/n, 0 < i < n, is given by 
If 0 < p < 4, n tends to infinity, and i/n tends to a constant, the probability above tends to zero, thus indicating that placing consistently small bets is a bad strategy. 
From the preceding discussion one is led to consider a policy of placing large bets and in particular the so-called bold strategy whereby the gambler stakes at each time k his entire fortune xk or just enough to reach his goal, 
7.3 OPTIMAL GAMBLING STRATEGIES 307 
whichever is least. In other words the bold strategy is the stationary policy n* = {p*, p*, . . .} with p* given by 
We shall prove that the bold strategy is indeed an optimal policy. To this end it is sufficient, by Corollary 2.2, to show that for every initial fortune x E [0, 11 the value of the reward fortune J,*(x) corresponding to the bold strategy {p*,  p*, . . .} satisfies the sufficiency condition 
or equivalently 
J,.(O) = 0, J,*(l) = 1, 
Vx E (0, l), u E [0, x] n [0, 1 - x]. 
J,*(x) 2 pJ,*(x + u)  + (1  - p)J,*(x - u )  
(23) 
Now by using the definition of the bold strategy and the fact that 
J,* = 7 J J p * )  
(cf. Corollary 1.1) we obtain that the function J p r  must satisfy 
J,*(O) = 0, J,*(l) = 1, (24) 
J ,  ( ) - 
if O < x < + ,  if + < x < 1. 
* x  
p + (1 - p)Jp.(2x - 1) 
We prove the following lemma showing that J,. is uniquely defined from the above relations. 
Lemma For everyp, with 0 < p < 9, there is only one bounded function on [0, 11 satisfying (24), and (25), the function J p * .  Furthermore, J,.  is continuous and strictly increasing on [O, 13. 
Proof Suppose that there existed two bounded functions J ,  : [0, 13 -, R ,  
J , :  [0, 13 -, R such that Ji(0)  = 0, Ji(l) = 1, i = 1, 2, and 
Then we have 
Jl(W - J2(2x) = (J,(x) - J,(X))/P if 0 < x < +, (26) 
if + < x < 1. (27) J,(2x - 1) - J,(2x - 1 )  = (J,(x) - J2(x))/l - p 
308 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Let z be any real number with 0 < z < 1. Define 
if O < z < + ,  
if 0 < z k - 1  < +, if 4 < z k - 1 <  1, zk = {;::I: - 1 
for k = 1,2, . . . . Then from (26) and (27) it follows (using p < 3) that 
IJ1(zk) - J 2 ( z k ) l  2 I J l ( z )  - J2(z)1/(1 - P)k = 2, . . .  . 
Since J l ( Z k )  - J 2 ( z k )  is bounded it follows that J l ( z )  - J2(z) = 0, for 
otherwise the right-hand side of the inequality would tend to +m.  Since z E [0,13 is arbitrary we obtain J1 = J 2 .  Hence J,. is the unique bounded function on [0, 11 satisfying (24) and (25). 
To show that J,* is strictly increasing and continuous we consider the 
mapping T,*, which operates on functions J : [0, 11 -, [0, 11 and is defined by 
(28) P J ( W  + (1 - p)J(O)  if O < x < f ,  pJ(1) + (1 - p)J(2x - 1)  if f < x < 1, 
T,*(J)(O) = 0, T,dJ)(l) = 1. 
T,*(J)(x) = { 
Consider the functions J o  , TpI(J0), . . . , T$(Jo), . . . , where J o  is the zero func- 
tion (Jo(x) = 0 for all x E [0, 13). We have 
J,.(x) = lim T:,(J,)(x) Vx E [O, 11. (29) k - c a  
Furthermore, the functions T$(Jo) can be shown to be monotonically nondecreasing in the interval [0, 13. Hence, by (29), J,* is also monotonically nondecreasing. 
Consider now for n = 0, 1, . . . the sets 
S ,  = {x E [0, 13 Ix = k2-", k = nonnegative integer}. 
The following fact may be verified in a straightforward manner concerning the functions Tk,,(Jo), k = 0, 1, . . . : 
Tz*(Jo)(x) = T:*(Jo)(x) Vx E S,- 1, m 2 n 2 1. 
As a result of the above equality and (29), 
J,.(x) = T;*(J,)(x) Vx E Sn-l, n 2 1.  
7.3 OPTIMAL GAMBLING STRATEGIES 309 
A further fact that may be verified by using induction and (28) and (30) is that for any nonnegative integers k, n for which 0 < k2-" -= (k  + 1)2-" < 1 ,  we have 
(31) 
Since any number in [0, 13 can be approximated arbitrarily closely from above and below by numbers of the form k2-" and since J,. has been shown to be monotonically nondecreasing it follows immediately from (3 1) that J,. is continuous and strictly increasing. Q.E.D. 
p" < J,*[(k + 1)2-,] - J,*(k2-") < ( 1  - p)". 
We are now in a position to prove the following proposition. 
Proposition 8 The bold strategy is an optimal stationary gambling 
Proof We shall prove the sufficiency condition 
policy. 
J,*(x) 2 pJ,*(x + u )  + ( 1  - p)J,*(x - u )  
Vx E [0, I ] ,  u E [0, x ]  n [0, 1 - x] .  (23) 
In view of the continuity of J,. established in the previous lemma it is sufficient to establish (23) for all x E [0, 11 and u E [O, x ]  n [0, 1 - x ]  that 
belong to the union u."=o S,  of the sets S,  defined by 
S ,  = { z  E [0, 11 Iz = k2-", k = nonnegative integer}. (32) 
We shall use induction. By using the fact that J,,(O) = 0, J,.& = p ,  J,.( 1 )  = 1, we can show that (23) holds for all x and u in So and S1. Assume that (23) holds for x ,  u E S,  and n 2 1. We will show that it holds for all x, u E S, ,  
with u E [0, x ]  n [O, 1 - x ]  there are four pos- 
sibilities: 
(1) x + u < 3, 
(2) x - u 2 +, 
(3) x - u < x < + < x + u ,  (4) x - u < + < x < x + u .  
For any x ,  u E S,+ 
We shall prove (23) for each of the cases above. 
pothesis Case 1 If x ,  u E S,+ 1, then 2x E S,, 2u E S,, and by the induction hy- 
J,*(2x) - pJ,*(2x + 2u) - ( 1  - p)J,*(2x - 2u) 2 0. 
J,*(x) - pJ,*(x + u )  - ( 1  - p)J,.(x - u )  = p[J,*(2x) - pJ,*(2x + 2u) 
(33) 
If x + u < 3, then by (25) 
- ( 1  - p)J,*(2x - 2u)] 
310 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
and using (33) the desired relation (23) is proved for the case under con- sideration. 
Case 2 If x, u E S,+ ,, then (2x - 1) E S, ,  2u E S,,  and by the induction 
hypothesis 
J,*(2x - 1) - pJ,*(2x + 2u - 1) - (1 - p)J,*(2x - 2u - 1) 2 0. 
J,*(x) - pJ,*(x + u) - (1 - p)J,*(x - u) 
If x - u > +, then by (25) 
= p + (1 - p)J,*(2x - 1) - p c p  + (1 - p)J,*(2x + 2u - l)] 
-(1 - p ) [ p  + (1 - p)J,*(2x - 2u - l)] 
= (1 - p)[J,*(2x - 1) - pJ,*(2x + 2u - 1) 
-(1 - p)J,*(2x - 2u - l)] 2 0, 
and (23) follows from the above relations. 
Case 3 Using (25) we have 
J,*(x) - pJ,*(x + u) - (1 - p)J,.(x - u) 
= pJ,*(2x) - p c p  + (1 - p)J,*(2x + 2u - l)] - p(l - p)J,*(2x - 2u) 
= p[J,*(2x) - p - (1 - p)J,*(2x + 2u - 1) - (1 - p)J,*(2x - 241. 
Now we must have x 2 a, for otherwise u < a and x + u < 3. Hence 2x 2 $ and the sequence of equalities above can be continued as follows: 
J,*(x) - pJ,*(x + u )  - (1 - p)J,*(x - u) 
= p c p  + (1 - p)J,*(4x - 1) - p - (1 - p)J,*(2x + 2u - 1) 
-(1 - p)J,*(2x - 241 = p(l - p)[J,.(4x - 1) 
-J,*(2x + 2u - 1) - J,*(2x - 241 = (1 - p)[J,*(2x - +) 
-pJ,*(2x + 2u - 1) - pJ,*(2x - 2u)]. 
Since p < (1 - p), the last expression is greater than or equal to both 
(1 - p)[J,*(2x - +) - pJ,*(2x + 2u - 1) - (1 - p)J,*(2x - 2u)] 
(1 - p) [J,*(2x - 4) - (1 - p)J,*(2x + 2u - 1) - pJ,*(2x - 241. 
and 
Now for x, u E S , + ~  and n 2 1, we have (2x - +)ES, ,  (2u - $)ES, if (2u - +) E [0, 13, and (+ - 2u) E S, if (i - 2u) E [0, 11. By the induction 
hypothesis the first or the second of the above expressions is nonnegative, 
7.3 OPTIMAL GAMBLING STRATEGIES 311 
depending on whether 2x + 2u - 1 2 2x - 
u 2 a or u < d. Hence (23) is proved for Case 3. 
or 2x - 2u 2 2x - f, i.e., 
Case 4 The proof resembles the one for Case 3. Using (25)  we have 
J,*(x) - pJ,.(x + u)  - ( 1  - p)J,*(x - u )  
= p + (1 - p)J,*(2x - 1 )  - p [ p  + (1 - p)J,*(2x + 211 - I ) ]  
- ( 1  - p)pJ,*(2x - 2u) = p ( l  - p )  + (1 - p)[J,*(2x - 1 )  
-pJ,*(2x + 2u - 1 )  - pJ,.(2x - 2u)l. 
We must have x < 2 for otherwise u < 
,< + ,< 2x - f ,< 1 and using (25)  we have 
and x - u > f. Hence 0 < 2x - 1 
( 1  - p)J,*(2x - 1 )  = ( 1  - p)pJ,*(4x - 2) = p[J,*(2x - +) - p ] .  
Using the relations above we obtain 
J,*(x) - pJ,*(x + u)  - ( 1  - p)J,*(x - u )  
- p ( l  - p)J,.(2x - 2u) 
- ( 1  - p)J,*(2x - 2u)l. 
p[(1 - 2p)[1 - J,*(2x + 2u - l ) ]  + J,*(2x - 3) -pJ,*(2x + 2u - 1) - (1 - p)J,*(2x - 2u)l 
= p(1  - p )  + p[J,.(2x - +) - p ]  7 p ( l  - p)J,.(2x + 2u - 1 )  
= p [ (  1 - 2p) + Jg*(2x - 3) - ( 1  - p)J,*(2x + 2u - 1 )  
The relations above are equal to both 
and p [ ( 1  - 2p)[1 - JJ2X - 2 4 1  + J,.(2x - +) 
-(1 - p)J,*(2x + 2u - 1 )  - pJ,*(2x - 2u)l. 
Since 0 < JJ2x  + 2u - 1) < 1 and 0 < JJ2x  - 2u) < 1 ,  the expressions 
above are greater than or equal to both 
p[J,*(2x - f) - pJ,*(2x + 2u - 1) - (1 - p)J,*(2x - 2u)l 
p[J,*(2x - +) - (1 - p)J,*(2x + 2u - 1 )  - pJ,*(2x - 2 4 1  
and 
and the result follows as in Case 3. Q.E.D. 
We note that the bold strategy is not the unique optimal stationary gambling strategy. For a characterization of all such optimal strategies see 
312 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Dubins and Savage [D8, p. 901. Several other gambling situations where strategies of the bold type are optimal are described in reference [D8, Chapters 5 and 61. 
7.4 The First Passage Problem? 
In this section we shall make the following assumptions within the frame- 
C.l The state space S, the control space C,  and the disturbance space 
work of the problem of this chapter: 
D are finite sets. The state space is denoted by 
S = (0, 1,. . . )  n}. C.2 The state 0 is an absorbing state, i.e., 
x k  = 0 * x A + ,  = 0 VU,EC, W ~ E  D. 
Furthermore there is no cost incurred while the system is in the absorbing state, i:e., 
E(g(0, u, w)lx = 0, u }  = 0 vu E U(0). 
C.3 There exists a positive integer rn such that for every admissible 
for 
policy n = { p o ,  pl, . . .} there holds 
P(x,  = O(xo = i, x )  > 0 all i = 1, 2 , .  . . , n, 
where P(x ,  = Olxo = i, n) denotes the probability that at time m the system will be in the absorbing state given that the policy n is used and the initial state is i. 
In the problem above control continues until the system passes through the absorbing state for the first time. At this point the system operation essentially terminates. Thus the objective in the problem is to reach the absorbing state with the least possible cost. One may easily show using C.3 that termination will occur with probability one for every policy employed. It is also possible to show that if P(x,  = 0 Jxo = i, a) > 0, for some integer m, then we have P(x,. = OIx, = i ,  n) > 0 for some integer rn' with rn' < n, i.e., it is possible to reach the absorbing state within n steps. As a result we may take m = n in C.3, and furthermore C.3 is equivalent to the seemingly weaker condition that for each n: there is an rn such that P(x,  = OIx, = i, n) > 0, i = 1,2, . . . , n. While Assumption C.3 is somewhat restrictive we shall be able to relax it somewhat later in this section. 
t This section requires some familiarity with the basic notions associated with finite state Markov chains. A summary together with references is given in Appendix D. 
7.4 THE FIRST PASSAGE PROBLEM 313 
Under C.l-C.3 one may prove a number of important results that are not available under either Assumption P or N. In fact, it turns out that it is not necessary to  assume Assumption P or N ,  i.e., the costs per stage g need not be either nonnegative or nonpositive. The basic reason is that under C.l-C.3 the mapping T of (3) is an m-stage contraction mapping over the 
set of all functions J: S -, R with J(0) = 0, where m is the positive integer 
in C.3. In other words (see Section 6.3) we have for some p < 1 and for any two functions J, J': S --f R with J(0)  = J'(0) = 0, 
II T"(J) - T"(J')II < PllJ - J'IL 
or equivalently 
max I Tm(J)( i )  - T"(J')(i)l < p max IJ(i) - J'( i ) l .  
Furthermore, for any admissible stationary policy II = {p, p, . . .} the mapping T,, of (4) is also an m-stage contraction mapping, i.e., 
i = O ,  1 ,  .... n i = O ,  1 ,  .... n 
IIT;(J) - ~;(J')lI G P,,lJ - J'IL 
for some p,, < 1 and every two functions J, J' : S + R with J(0) = J'(0) = 0. 
These facts, which are proved in the proposition below, have important analytical and computational consequences. 
all J, J' : S --f R with J(0)  = J'(0) = 0 we have Proposition 9 Under C.l-C.3 there exists a scalar p < 1 such that for 
max 1 T"(J)(i) - T"(J')(i)I < p max IJ(i) - J'( i ) l ,  (34) 
i = O , l ,  ..., n i = O , l ,  ..., n 
Tk(J)(0) = Tk(J')(0) = 0, k = 0, 1,. . . . 
Proof For any u E U(i), i = 0, 1, . . . , n, let us denote by pi,&) the transi- 
tion probability 
Piju) = pCW;j~)lx = i ,  ~1 
W&J) = {w E D l f ( i ,  u, w )  = j } .  
(35) 
where Wju) c D is the set 
(36) 
In other words p i @ )  is the probability that the next state will be j given that the present state is i and the control u is applied as explained in the beginning of Section 6.2. Denote also 
& u )  = E { g ( i , u ,  w) l i ,u } ,  i = 0, 1, ..., n. (37) W 
314 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
We have by C.2, 
poJ(u) = 0 Vj = 1 ,  . . . , n, u E U(O), poo(u) = 1 Vu E U(O), (38) 
g(0, u)  = 0 vu E U(0). (39) 
By (3), C.l, C.2, and (37-39) we have for any two functions J ,  J’: S -, R with 
J(0)  = J’(0) = 0, 
n 
(40) 1 
1 (41) 
T(J)(i) = min g(i, u )  + 1 pi,(u)J(j) , 
T(J‘)(i) = min g(i, u )  + &+,(j)~’(j) , 
T(J) (O)  = T(J’)(O) = 0. 
i = 1, .  . . , n, 
j= 1 
u s U ( i )  [ j= 1 
n 
u s U ( i )  [ 
i = 1 , .  . . , n, 
Let p(i), p’(i) attain the minimum in (40) and (41), respectively. We have n 
Combining the above two inequalities we obtain 
where for each i, Fo(i) is equal to the value p(i) or p’(i) that yields the larger 
value of I;= p i j  1 J(j) - J’G) I. 
By repeating the argument above we obtain that for every k and some ,&- : S  + C with ilk- l(i) E V(i),  i = 1,. . . , n, we have 
By using the vector notation 
and the matrix notation 
7.4 THE FIRST PASSAGE PROBLEM 315 
we may write (42) as 
E ,  < Pk-1Ek-1 ,  k = 1, 2 , .  . . , 
where the inequality is coordinatewise. Using the fact that p i j  is nonnegative wehaveE,< P , - , P , - , ~ ~ ~ P o E O , a n d f o r k = m w e o b t a i n  
Em < Pm-1Pm-2 . ' .  P o E o .  
Now the matrix Pm- 1 P m - 2  . . . Po is the m-step transition probability matrix corresponding to a policy of the form ?t = { p m -  j i m - 2 ,  . . . , P o ,  p, p, . . .}, where Po, . . . , j im-  have been defined above and p is any function satisfying p(i) E U(i )  for all i (see Appendix D). Note that E is admissible. 
Thus the inequality above is equivalent to the following inequality, 
which holds for every i = 1, . . . , n: 
Hence 
max I T"(J)(i) - T"(J)(i)I 
i = l ,  ..., n 
1 i = l ,  ..., n 
< [ max P(xm = j l x o  = i, 51) max IJ(i) - J'(i)l. 
i = l ,  ..., n j = l  
By C.3 we have n 
p = max 1 P(x, = j l x o  = i, Z) < 1 ,  
i =  1, .... n j =  1 
and (34) follows. Q.E.D. 
By employing our usual device of restricting the control constraint set so that there is only one admissible policy we obtain for every admissible stationary policy { p .  p, . . .} and any two functions J ,  J ' :  S -, R with J ( 0 )  = 
J'(O), the following relation : 
max I T,"(J)(i) - Tr(J')(i)I < p p  max IJ(i) - J'(i)l, 
i = O .  l . . . . , n  i = O ,  1 ,  .... n 
where pp is a constant depending on p and satisfying pp < 1. However, it is possible to obtain a stronger result for the problem of this section, which we state below. The proof is obtained by essentially repeating the proof of Proposition 9 and is left to the reader. 
316 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Corollary 9.1 Let II = { p o ,  pl, . . .} be an admissible policy. Then under C.l-C.3, we have for all J ,  J’ : S -, R with J (0 )  = J’(0) = 0, 
< p, max IJ(i) - J’( i ) l ,  
i = O .  1 .  ..., n 
(43) 
where n 
p, = max CP(X, = J l x ,  = i ,n) < 1. i = l ,  ..., n j = 1  
Having established the rn-stage contraction properties of Proposition 9 and Corollary 9.1 we are able to state a number of important analytical and computational results for the first passage problem under C. 1-C.3. The following proposition guarantees the convergence of the successive approxi- mation method to the optimal value function J* starting from an arbitrary function J :  S + R with J(0)  = 0. Also J* and J, can be obtained as unique 
fixed points of the equations J = T(J)  and J = T,(J), respectively. 
Proposition 10 Let C.l-C.3 hold. Then for any function J: S -P R withJ(0) = 0, 
J*(x) = lim T ~ ( J ) ( x )  V x  E S ,  k-+m 
and for every admissible stationary policy {p, p, . . .}, 
J,(x) = lim T i ( J ) ( x )  V x  E S.  k - m  
Furthermore, J* and J ,  are unique solutions of the equations J = T(J)  and J = T,(J), respectively, within the class of functions J :  S + R with J(0) = 0. In addition if p*(i) attains for i = 1, . . . , n the minimum in the right-hand side 
of the equation 
J*(i) = min a(i, u )  + pi ju)J*( i ) ] ,  i = 1,. . . , n, 
UE U(i )  [ j =  1 
then n* = {p*,  p*, . . .} is an optimal stationary policy. The proof of Proposition 10 may be obtained through arguments similar 
to those used in Section 6.1 or by simple modifications of proofs of corre- sponding results of Problem 4 in Chapter 6 and is left to the reader. As indicated also by Problem 4 in Chapter 6, it is possible to compute optimal stationary policies under C.l-C.3 by using the method of policy iteration or linear programming (cf. Section 6.2). The development and proof of validity of these algorithms is left again as an exercise for the reader. 
7.4 THE FIRST PASSAGE PROBLEM 317 
We now consider the first passage problem under a different set of 
C.1’ Same as C.l. 
C.2 Same as C.2. 
C.3 
assumptions. 
There exists a stationary admissible policy it = {ji, ,ii,. . .} and a 
positive integer rn such that 
P(x,  = OJxo = i, E )  > 0 Vi  = 1,2,. . . ,n, (44) 
where P(x,  = OJx, = i, 5) denotes the probability that at time rn the system will be in state x = 0 given that the policy Ic is used and the initial state is i. 
C.4 There holds 
g(i ,  u, w )  > 0 Vu E V(i), i = 1, ..., n, w E D. (45) 
Notice that C.3‘ is a much less restrictive assumption than C.3 since now we require that (44) hold for a single stationary policy ?I rather than for every policy as in C.3. For example, C.3 will not hold in a finite state version of the stopping problem of Section 7.2 since by using the policy that continues operation at every stage regardless of the current state, the absorbing (termination) state will never be reached. On the other hand C.3’ is satisfied for the stopping problem of Section 7.2 since (44) holds for the policy Ic 
that terminates at every state i = 1,2, . . . , n. For this policy (44) is satisfied 
with rn = 1. Notice, however, that by (45) we require now that expected costs 
per stage corresponding to the states i = 1,2, . . . , n are strictly positive. 
We now introduce the following definition. 
Definition An admissible stationary policy z = {p ,  p, . . .} will be called a proper policy if there exists a positive integer rn such that 
P ( x , = O ( x , = i , 7 r ) > O  v i =  1,2 ,..., n, (46) 
where P ( x ,  = Olx, = i ,  z) denotes the probability that at time rn the system will be in the absorbing state x = 0 given that the policy a is used and the initial state is i. 
By C.3’ there exists at least one proper policy. Let us denote for any p:  S + C by P, the transition probability matrix 
. . .  1 0 ~10[/-41)1 PII[P(~)I * * ~ 1 n M 1 ) l  0 1  
~ n o G 4 n ) l  ~ n 1 I N n ) l  * . . ~ n n M n ) l  (47) 
318 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
where pij is the transition probability defined by (35) and (36). The first row of P ,  has the form (1,0, . . . , 0) in view of the fact that x = 0 is an absorbing 
state [cf. (38)]. Note that by Corollary 9.1 if n = {p, p, . . .} is proper, then by restricting the control constraint set so that there is only one admissible policy, namely n, we obtain a problem for which C.l-C.3 applies. Then application of Proposition 10 yields: 
Corollary 10.1 If n = {p, p, . . .} is a proper policy, then 
J ,  = {J,(O)? J#), . . . 7 J,(n)l 
satisfies J ,  = T,(J,) or equivalently 
J ,  = g, + P , J , ,  
where P ,  is matrix (47) and g, is the vector 
Furthermore, J ,  is the unique function J : S + R satisfying J = T,(J) and 
J ( 0 )  = 0. In addition, for every function J : S + R with J (0 )  = 0, we have 
lim T,k(J)(i) = J,(i), i = 0, 1,. . . , n. 
k + m  
(49) 
It is important to realize that in view of Assumption C.4’ we are essentially interested in proper policies only, for if n is not a proper policy, then there exists a state i from which the absorbing state will never be reached using n. Since the expected cost incurred per stage will be bounded below by a positive 
number [by (45) and finiteness of the state space] we will have J,(i) = + a, 
while with every proper policy the corresponding cost will be finite. This observation is the key to understanding the results to be obtained. In fact this observation yields immediately the following result. 
Proposition 11 Under C. 1’-C.4’ there exist optimal stationary policies. Each one of these policies must be a proper policy. 
Proof Under C.l’-C.4 Assumption P is satisfied and since the control space is finite there exist optimal stationary policies by Proposition 5. Also by C.3‘ there exists a proper policy E = {ji, ji, . . .} and by Corollary 10.1 we have 0 Q Jp( i )  < +a, Vi.  Hence 0 Q J*(i) < +a, Vi.  Since for every 
319 
stationary policy that is not proper the associated cost is infinite for some initial states, such a policy cannot be optimal. Q.E.D. 
7.4 THE FIRST PASSAGE PROBLEM 
We now arrive at our main result. 
Proposition 12 Under C.l’-C.4‘ in order for a proper policy 7c* = 
(50) 
{ p * ,  p*, . . .} to be optimal it is necessary and sufficient that 
J,* = T,*(J,*) = T(J,*), 
or equivalently n 
J p * ( i )  = g,*(i) + 1 ~ i j C ~ * ( i ) I J p * c i )  
j = O  
= min E {g ( i ,  u, w) + J , . [ f ( i ,  u, w)]}, i = 0, 1,. . . , n. ueU( i )  w 
Proof Necessity of (50) is clear from the theory of Section 7.1 (Proposi- tion 1 and Corollary 1.1). To prove sufficiency we have that for any optimal proper policy 71 = {p, ji, . . .} the condition J,* = T(J,*) implies 
J,* < T,(J,,) < T~(J,.) < . . . < lim T ~ ( J , * ) .  k + m  
By using (49) and the optimality of the proper policy ?i we obtain 
J,*(i) < lim q;(J ,*) ( i )  = J, ( i )  = J*(i) Vi E S .  k - tm 
Hence n* is optimal. Q.E.D. 
A related result is the following. 
Proposition 13 Under C.l’-C.4’ the optimal value function J* is the only real-valued function with J (0 )  = 0, J(i) 2 0, i = 1, . . . , n, that satisfies 
the equation J = T(J). 
Proof Let J : S -, R be a real-valued function with J ( 0 )  = 0, J ( i )  2 0, 
such that J = T(J). Let p be such that J = T,(J). By Corollary 2.1 we have J ,  < J and hence {p, p, . . .} is a proper policy. Hence by Corollary 10.1 we have J, = J. Thus 
and by Proposition 12, {p, p, . . .} is optimal or equivalently J = J, = J*. Q.E.D. 
It is possible to combine Proposition 12 with Proposition 7 to show the validity of the policy iteration algorithm for the first passage problem 
320 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
under Assumption C.l'-C.4'. Indeed if R = {p, p, . . .} is a proper policy and ji is such that ji(i) E V(i), i = 0, 1, . . . , n, and 
T,(J,) = UJ,), by Proposition 7, we have 
J p ( i )  < J,(i), i = 0, 1,. . . , n, 
and {ji, ji, . . .} is proper. If we had J, = J,, then in view of the relations 
J, = Tp(J,) < TqJ,) = T(JJ  < T,(J,) = J,, 
we would obtain T(J,) = J, and by Proposition 12, R = {p, p, . . .} would be optimal. Hence either R = {p, p, . . .} is optimal or ?f = {ji, ji, . . .} is a strictly better proper policy. It follows that by policy iteration we can obtain an optimal proper policy in a finite number of steps provided that we start with a proper policy. 
7.5 Notes 
The material of Section 7.1 is very similar to that of Section 6.4. For further discussion see the references cited in Chapter 6. The gambling problem and its solution are taken from the fascinating work of Dubins and Savage [D8]. The first passage problem was first formulated by Eaton and Zadeh [El]. The presentation given here differs somewhat from presenta- tions in other sources [D4, K10, Pl] in that it makes direct use of the general results of Section 7.1. A policy of the type described in Problem 7 is called a one-stage lookahead policy [R4, p. 1381. The general framework and the results of Problem 9 are due to the author [B13, B161. The results of Problems 13 and 14 are also due to the author [B6, B9]. 
Problems 
1. Do Problems 8.22-25, and I 1  [except for part (a)] of Chapter 6 for the case of Problem (U) of this chapter (i.e., a = 1). 
2. Let Assumption P hold and consider the case S = D = {1,2, . . . , n}, 
x k  + = wk . The mapping T is represented as 
n 
T ( J ) ( ~ )  = inf C piJu)Cg(i, u, j) + JG)], i = I, . . . , n, 
uEU(i)  j =  1 
where piJu) denotes the transition probability that the next state will be j when the current state is i and control u is applied. Assume that piJu) and 
PROBLEMS 32 1 
g(i, u, j )  are continuous on V(i) for all i , j  and that the sets V(i) are compact subsets of R" for all i .  Show that we have limk,, Tk(Jo)(i) = J*(i), where Jo( i )  = 0, i = 1,.  . . , n. Show also that there exists an optimal stationary 
policy. 3. Consider the problem of finding a scalar sequence { u o ,  u l , .  . .} satisfying C;=o uk < c, uk 2 0, V k ,  and maximizing g(uk), where c > 0 is given and g(u)  2 0 for all u 2 0, g(0) = 0. Assume that g is monotonically non- decreasing on [0, m). Show that the optimal value of the problem is J*(c), where J* is a monotonically nondecreasing function on [O. m) satisfying J*(O) = 0 and 
J*(x) = sup { g ( u )  + J*(x  - u ) }  VXXE [O, m). 
O Q u Q x  
4. Deterministic Linear-Quadratic Problems Consider the deterministic linear-quadratic problem involving the system 
X k + l  = AXk + BUk, 
and the cost functional m 
J&o) = 1 xb Q X k  + l(k(Xk)lRpk(Xk)- 
It is assumed that R is positive definite symmetric, Q is of the form C'C, and that the pairs (A, B), (A, C) are controllable and observable, respectively. Use the theory of Sections 3.1 and 7.1 to show that the stationary policy II* = {p*, p*, . . .} with 
k = O  
p*(x) = -(B'KB + R)-'B'KAx 
is optimal, where K is the unique positive semidefinite symmetric solution of the algebraic Riccati equation (cf. Section 3.1) 
K = A'[K - KB(B'KB + R)- 'B'KIA + Q. 
Provide a similar result under an appropriate controllability assumption for the case of a periodic deterministic linear system and a periodic quadratic cost functional (cf. Section 6.7). 5. Prove Proposition 10 in Section 7.4. Also devise a policy iteration algorithm for the first passage problem under conditions C. 1 -C.3 and show that it will yield an optimal stationary policy in a finite number of iterations. 6. Consider the first passage problem under Assumptions Cl'-C.4'. Show that if J :  S + R is a function with J ( i )  2 0, i = 0, 1, . . . , n, and J ( 0 )  = 0, 
then limk,, T k ( J ) ( i )  = J*(i), i = 0. . . . , n. 
322 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
i = 1,2, .  . . , n 
7. Consider the stopping problem under C.l’-C.4 and let B be the set of states 
n 
t(i) Q c(i) + 1 p i j t ( j )  
j =  1 
Assume that pU = 0 if i E B and .j # B. Show that an optimal policy is to stop if and only if the current state is in B. 8. Consider the first passage problem under C.l’-C.4’. Let n = {p, p, . . .}, n’ = {p’, p’, . . .} be two proper policies. Define ji as 
p ( i )  if J,(i) d JJi), p’(i) if J,(i) > JJi). 
ji(i) = 
Show that {ji, ji, . . .} is proper and that 
J,&) Q min{J,(i), J,,(i)}, i = 0, 1, . . . , n. 
9. Let S and C be two sets, and let F ( S )  be the set of all functions J:S -+ 
[ - x, + m]. Consider a mapping H : S x C x F ( S )  + [ - m, + m] having 
the following properties: 
(a) J d J’ (b) 
H(x, u, J )  < H(x, u, J’),  V(x, u )  E S x C,  J ,  J’ E F(S).  If { J k }  is any sequence with J k  E F(S),  J k  Q J k + ’  for all k and such 
that J(x) = limk+m Jk(x) for all x E S, then 
lim ~ ( x ,  u, J ~ )  = ~ ( x ,  u, J )  V(x, u )  E s x C .  
k + m  
(c) Thereexistsa scalar ct > 0 such that for all scalars r > 0 and functions J E F(S)  there holds 
H(x, u, J )  < H(x  + u, J + re) < H(x, u, J )  + ctr V(x, u)  E S x C,  
where e(x) = 1 for all x E S. For each x E S let V(x) be a given nonempty subset of C. Let M be the set 
of all functions p : S + C with p ( x )  E U(x), Vx E S. Define the mappings 
T : F ( S )  + F(S),  7 : F(S)  + F ( S )  by 
T(J)(x) = infH[x, p(x), 51, T(J)(x) = s u p ~ [ x ,  p(x), J ]  Vx E S ,  C E M  c ~ M  
and for every p E M the mapping T,: F ( S )  + F(S),  
T,(J)(x) = H[x, p(x), J ]  vx E S. 
PROBLEMS 323 
Let J o  E F(S) be a function such that Jo(x) > - x for all x E S and 
Jo(x) 6 H(x, u, J o )  V(x, u )  E s x c. 
Let ll be the set of all sequences of functions z = { p o ,  p l r . .  }, where & E M, k = 0, 1, . . . , Define for all x E S 
J,W = lim (T," T,, * * * TPk)(J0)W? 
J*(x) = infJ,(x), 
J,(x) = lim T ~ ( J ~ ) ( X ) ,  
k-oo 
J*(x) = sup J,(x), x€n ,En 
JJX) = Iim Tk(~,)(x). k-m k - +  oc 
Show that 
(a) Tk(Jo)(x) = inf, (T,,T,, . . . TWk- ,)(Jo)(x), Vx E s. 
(b) T"(Jo)(x) = SUP, (Two T,, . . . TNk. , ) (Jo) (x) ,  VX E S .  (c) J* and j* are fixed points of T and respectively, i.e., 
J* = T(J*), 
(d) J' E F(S), J' 2 J o ,  J' 2 T(J ' )  * J' 2 J*, 
Define for each p E M, the function J,, E F by 
J,(x) = lim T;(J,)(x) Vx E S .  
1* = T(J*).  
J' E F(S), J' 2 J , ,  J' 2 T ( J ' )  * J' 2 J*. 
(e) 
I -  x 
Show that 
J ,  = T,(J,), J,,  = J* O T , ( J * )  = T(J*). J ,  = J* 0 T,(J,)  = T(J,). 
(f) Show that if there exists a n* E n such that J , ,  = J* then there exists a p* E M such that Jut = J*. 
( g )  j* = J , .  (h) Assume that there exists a positive integer E such that for all k 2 E,  
x E S, J. E R,theset , uk(x, 1) = (11 E U(x)lH[x, u, Tk(Ji3)] d 2) 
is a compact subset of a Euclidean space. Then 
J* = T(J*) = J ,  = T(J,), 
and there exists an optimal stationary policy z* = {p*, p*, . . .}. 
324 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
Hints: (a) For any fixed k and any E > 0 let pi E M, i = 0, . . . , k - 1, 
be such that 
T~~[T~-'-'(J,)] < T k - i ( ~ o )  + Ee. 
Use property (c) to show that k -  1 
inf(T,, . . . T , ~ -  , ) ( J ~ )  < T k ( ~ o )  + 1 aiee. 
n i = O  
(b) For each i = 0, 1, . . . , k - 1 consider a sequence {py} c M such 
that 
Iim T,JT~-~-'(J,)] = T'-'(J,), n-a3 
T,p-'-'(J,)] < T,:+IITk-'-'(Jo)], n = 0,1, 
Show that 
supn (T,, T,, . . . T ~ ~ -  , ) ( J , )  3 Iim (T,;IO T,:! . . . T , ; K - , ~ ) ( J ~ )  = T'(J,). n i - m  
i=O ....... k -  1 
(c)-(h) Adapt the proofs of corresponding results in Section 6.4. See references CB13, B16] for more detailed analysis and proofs. 10. Consider the stopping problem of Section 7.2 under the assumption that 
t (x )  < 0, c(x)  < 0 v x  E S .  
Consider the mapping T defined by 
T ( J ) ( x )  = min t (x) ,  c(x)  + E {JCfc(x, w)Il . [ W 1 
(a) Show that the optimal value function J* satisfies 
J* = T(J*), J* = lim T k ( ~ o ) ,  k + c c  
where Jo(x)  = 0, Vx E S. Verify also that if S is a finite set, then J* may be obtained by linear programming. 
(b) Consider the case where c(x)  = 0, V x  E S. Show that J* = lim Tk(t), 
where Tk{t) denotes the function obtained after k applications of the mapping T on the function t( * ). 
(c) L e t s =  {1,2 ,... },f ,( i ,w)=i+ l , c ( i ) = O f o r a l l i ~ S , w ~ D , a n d  
t(i) = - 1 + (l/i) for all i E S. Show that J*(i) = - 1 for all i and that there 
k+m 
PROBLEMS 325 
does not exist an optimal policy for this problem (even though the control space is a finite set). 11. Let zo,  zl,. . . be a sequence of independent and identically distributed random variables taking values on a countable set Z. We know that the probability distribution of the z i s  is one out of n distributionsf,, f2, . . . , f,, and we are trying to decide which distribution is the correct one. At each 
time k after observing zl, .. . , z k  we may either stop the observations and 
accept one of the n distributions as correct, or take another observation at a 
cost c > 0. The cost for acceptingf, given thatfj is correct is L,, i,j = 1, . . . , n. We assume Lij > 0 for i # j, Lii = 0, i = 1, . . . , n. The a priori distribution 
of fl, . . . , fn is denoted 
n 
Po = {P;,P;,..*,P;>, Pb 20, CPb = 1. i =  1 
Show that the optimal cost J*(Po) is a concave function of P o .  Characterize the optimal acceptance regions and show how they can be obtained in the limit by means of a successive approximation method. 12. Show that a finite horizon problem with N stages that falls within the framework of the basic problem of Chapter 2 can be viewed as a (stationary) first passage problem (not necessarily with finite state, control, and dis- turbance space) for which assumptions similar to C.2 and C.3 of Section 7.4 are satisfied. Show also that a contraction condition such as (34) holds for this problem. 
Hint: If S o ,  S , , .  . . , SN are the state spaces for the stages 0, 1,. . . , N, 
define a new state space S by S = { (x ,  k ) l x  E Sk, k = 0, 1, . . . , N }  u { T } ,  
where T is a termination (absorbing) state to which the system is driven with certainty from every state in { ( x ,  N) I x E S,} similar to the constructions of Section 6.7. 13. Infinite Time Reachability Consider the stationary system 
x k + l  = f ( X k , U k , W k ) ,  k = 0 ,  l , * * * ?  
of the problem of this chapter, where the disturbance space D is an arbitrary (not necessarily countable) set. The disturbances 'y, can take values in a subset W(x,, uk) of D that may depend on xk and uk. This problem deals with the following question: Given a nonempty subset X of the state space S, under what conditions does there exist an admissible policy {p,,, pl, . . .} with p&k)  E V(x,) for all xk E S and k = 0, 1, . . . , such that the state of the 
(closed-loop) system 
xk  + 1 = f c x k  9 p k ( x k ) ,  w k l  (51) 
belongs to the set X for all k and all possible values w k  E W [ x k ,  p k ( x k ) ] ,  i.e., 
(52) X k  E x VWk E w [ X k ,  p k ( X k ) ] ,  k = 0, 1, . . . . 
326 7 MINIMIZATION OF TOTAL EXPECTED VALUE 
The set X is said to be injinitely reachable if there exists an admissible policy { p o ,  pl ,  . . .} and some initial state xo E X for which relations (51) and (52) are satisfied. It is said to be srrongly reachable if there exists an admissible policy {p,,, pl . . .} such that for all initial states xo E X relations (51) and (52) are satisfied. 
Consider the function R mapping any subset 2 of the state space S into a subset R ( 2 )  of S defined by 
R ( 2 )  = {x I there exists u E U ( x )  such that f ( x ,  u, w) E 2, Vw E W(x,  u ) }  n Z .  
(a) Show that the set X is strongly reachable if and only if R ( X )  = X .  Given X consider the set X *  defined as follows: xo E X *  if and only if 
xo E Xandthereexistsanadmissiblepolicy { p u g ,  p l , .  . .} suchthat (51)and(52) are satisfied when xo is taken as the initial state of the system. 
(b) Show that a set X is infinitely reachable if and only if it contains a nonempty strongly reachable set. Furthermore, the largest such set is X *  in the sense that X *  is strongly reachable whenever nonempty and if 8 c X is 
another strongly reachable set, then 8 c X*. 
(c) Show that if X is infinitely reachable, there exists an admissible stationary policy {p, p, . . .} such that if the initial state xo belongs to X * ,  then all subsequent states of the closed-loop system xk+ = f [ x k ,  p(xk), wk] are guaranteed to belong to X * .  
(d) Given X consider the sets R ( X ) ,  . . . , Rk(X) ,  .. . , where R k ( X )  denotes 
the set obtained after k applications of the mapping R on X .  Show that 
m x *  c n R ~ ( x ) .  
k =  1 
(e) Given X ,  consider for each x E X and k = 1 , 2 , .  . . the set 
uk(x)  = {U I f ( X ,  U, W )  E Rk(X) ,  V W  E W(X, U)}. 
Show that if there exists an index E such that for all x E X and k 2 E the set U,(x) is a compact subset of a Euclidean space, then X *  = r)p= Rk(X) .  
Hint: Use the results of Problem 9. See Bertsekas [B9] for detailed proofs. 14. Injinite Time Reachability for Linear Systems Consider the linear stationary system 
X k + l  = AX, + B U k  + G W k ,  
where x k  E R", uk E R", wk E R', and the matrices A, B, G are known and have appropriate dimensions. The matrix A is assumed invertible. The controls uk and the disturbances wk are restricted to take values in the ellipsoids U = {uIu'Ru < I }  and W = {wl W'QW < l}, respectively, where R and Q are 
PROBLEMS 327 
positive definite symmetric matrices of appropriate dimensions. Show that in order for the ellipsoid X = {xIx ’Kx  < l}, where K is a positive definite symmetric matrix, to be strongly reachable (in the terminology of Problem 13), it is sufficient that for some positive definite matrix M and for some scalar p E (0, 1) we have 
- B G Q - 1 ~ ’  + BR-’B’ A + M ,  (53) l 1  K = A’ (1 - j3)K-l - ~ [ P 
(54) 
Show also that if (53) and (54) are satisfied, the stationary policy {p*, p*, . . .}, where 
1 K -  ’ - - GQ- ’ G’: positive definite. 
B 
P*(x)  = - ( R  + B’FB)-’B’FAx = Lx,  
F = (1 - B)K-’  - - [ - B BGQ-lGtll  
achieves reachability of the ellipsoid X = {xIx ’Kx  < l}. Furthermore, the matrix ( A  + BL) is a stable matrix. (For a proof together with a compu- tational procedure for finding matrices K satisfying (53), (54) see Bertsekas 
15. Gambling Strategies for Favorable Games A gambler plays a game such as the one of Section 7.3 but where the probability of winning p satisfies 
< p < 1. His objective is to reach a final fortune n, where n is a positive integer with n 2 2. His initial fortune is a positive integer i with 0 < i < n and his stake at time k can take only integer values uk satisfying 0 6 uk < xk, 0 < t f k  < n - xk, where xk is his fortune at time k .  Show that the strategy 
that always stakes one unit is optimal [i.e., p*(x)  = 1 for all integers x with 0 < x < n is optimal]. 
Jp*(i) = [((I - p) /p) ’  - 11 [(( 1 - p)/p)” - 13- ’, 
C B ~ ,  1191.) 
Hint: Use Proposition 10 to show that 
J,,.(i) = i/n, 
0 < i < n, + < p < 1, 
O < i < n, p = + (or see Ash [A8, p. 1821 for a proof). Then use the sufficiency condition of Corollary 2.2. 16. Under Assumption P show that if 3:  S -, [0, + 301 is a function such 
that T(1)  < 1, then J* < 1. Devise a mathematical programming procedure for solving the problem when S ,  C ,  and D are finite sets. 
Chapter 8 
Minimization of Average Expected Value 
The results of the previous chapter are applicable to problems where the infimum of the total expected value of the cost functional may be either finite or infinite for any given initial state. While for several classes of problems this infimum is finite for at least some initial states, in many problems under the positivity assumption P the total expected value of the cost functional is infinite for every initial state and every admissible policy. Under these circumstances the framework adopted in the previous chapter is clearly inadequate since within this framework every policy is optimal. On the other hand, in many situations it turns out that while the total expected value 
(1) I I 
lim E N + a ,  r k = O  - 
1 g C X k ,  p k ( x k ) ,  w k l  
corresponding to every admissible policy {po ,  pl, . . .} and initial state x o  is infinite, the limit 
(2) 
exists and is finite for every initial state and admissible policy. This is true in particular if the state space S ,  the control space C,  and the disturbance 
lim N+CU 
E Cr: 1 g C X k ,  p k ( x k ) ,  w k l  
328 
8 MINIMIZATION OF AVERAGE EXPECTED VALIJE 329 
space D are finite sets, i.e., the system controlled is a finite state Markov chain. Expression (2) may be viewed as expected cost per stage and is a reasonably meaningful criterion for optimization. This chapter will deal with a problem similar to the problem that was the subject of the previous chapter except for the fact that the expected cost per stage (2) is minimized in place of the total expected cost of ( 1 ) .  Furthermore, in the first three sections we shall restrict ourselves to the case of finite state space, control space, and disturbance space. For this reason it is perhaps convenient to switch at the outset to a notation that is better suited to finite state systems and is described in the problem formulated below. 
Let S = { 1, . . . , n}  denote the state space.? To each state i E S and each 
control u in the finite control space C there corresponds a set of transition probabilities pi,(u),j = 1 ,  . . . , n, where p,(u) denotes the probability that the 
next state will b e j  given that the present state is i and control u is applied. These transition probabilities specify completely the system together with the statistical description of the uncertainty as discussed in Sections 1.4 and 6.2. Each time the system is in state i E S and control u E C is applied, we incur an expected cost denoted a(i, u). The objective is to minimize over all admissible policies K = {po,  p l ,  . . .} with pk : S -P C, pk(i) E V(i), V i  E S ,  the average cost per stage 
(3) N -  1 
N-03 { k = O  J n ( X 0 )  = lim ( l / N )  E 1 pk(XR)l 
for any given initial state xo E S. Let us now provide a preliminary discussion of the problem that motivates 
some of the results to be obtained in the next section. Given any stationary admissible policy K = {p, p, . . .} let us denote by P, the transition probability matrix having elements p i j b ( i ) ]  : 
P I I [ P ( ~ ) I  * * *  ~ l n b ( 1 ) l  
(4 )  P n l  b ( n ) l  * * * ~ n n C ~ ( n ) l  
By the definition of p i j  we have 
n 
p i j b ( i ) ]  2 0 Vi , j ,  1 p i j b ( i ) ]  = 1 V i .  
j =  1 
t In the first three sections of this chapter we shall make use of some of the notions and results associated with finite state Markov chains. A summary of these results together with references is provided in Appendix D. 
330 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
The matrix P ,  may be used to express the rn-step transition probabilities corresponding to a stationary policy TC = {p, p, . . .} : 
p(xk + m = j I xk = i, 4, 
i.e., the probability that the state will b e j  at time ( k  + rn) given that the state is i at time k and the policy 7~ is used. We have 
p i j b ( i ) l  = &k+ = j lxk = i ,  4, 
and it is an elementary matter to show (see Appendix D) that 
[Pr ] i j  = P(Xk+m = j ( x k  = i, n), 
where [ P r I i j  is the element of the ith row and jth column of the matrix P r  (i.e., P ,  raised to the rnth power). 
Let us now consider the value of the cost functional J,(xo) of (3) .  As before we use the notation 
J,(i) = J,(i), i = 1, . . . , n, 
for stationary policies n = { p ,  p, . . .}. Denote 
With this notation it is easy to see that N- 1 
The following result shows that J ,  is well defined. It is a standard result on transition probability matrices and it is provided here only for the sake of the following discussion, rather than for obtaining any concrete results. Its proof may be found in [K7]. 
Lemma 1 p i j  satisfying 
For any n x n stochastic matrix P, i.e., a matrix with elements 
n 
p i j  B 0, i , j  = 1, . . . ,  n, C p i j  = 1, i = 1 ,..., n, j =  1 
we have N- 1 
N + m  k = O  (7) 
8 MINIMIZATION OF AVERAGE EXPECTED VALIJE 331 
where P* is a stochastic matrix with the following properties: 
(a) P* = PP* = P*P = P*P*. (b) ( I  - P + P*) is an invertible matrix, where I denotes the n x n 
Denoting now 
identity matrix. 
N- 1 
P,* = lim ( 1 / ~ )  1P:, 
N+ m k = O  
and using Lemma 1, we have from (6 )  that 
J ,  = P,*g,. (9) 
Thus for every admissible stationary policy the corresponding average cost per stage is well defined and conveniently characterized by the above equa- tion. Consider also the vector 
h, = ( I  - P, + P,*)-'(I - P,*)g,, 
( I  - P, + P,*)h, = ( I  - P,*)g,, 
(10) 
(1 1) 
P,*h,, = 0. (12) 
(13) 
where the inverse above exists by part (b) of Lemma 1. We have 
and multiplying both sides by P,* and using part (a) of Lemma 1 we obtain 
Using (12) and (9) we may write (1 1) as 
J ,  + h, = g ,  + P,h,. 
This equation is satisfied by every admissible stationary policy 7c = {p, p, . . .} and corresponds to the familiar functional equations satisfied by the cost corresponding to stationary policies in the discounted and undiscounted total cost cases of the previous two chapters. In those cases the average cost per stage J ,  was zero whenever the total cost was finite and the corresponding functional equation had the form 
h, = g ,  + aP,h,, 
where 0 < CI < 1 in the discounted case and u = 1 in the undiscounted case. As a result of the preceding discussion we have that with every admissible 
stationary policy 7c = {p, p, . . .} there is associated a vector of average costs per stage J, defined by (8) and (9) and satisfying the functional equation (13). An interesting question is whether there exists a stationary policy {p*, p*, . . .} that is optimal in the sense 
J,* Q J , ,  VP, 
332 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
where this inequality is considered to be componentwise [i.e., we write J,* < J ,  if J,*(i) < J,(i) for each initial state i E S]. The answer to this question is affirmative (see [B19, D41) but we shall not prove this fact. Instead we shall concentrate on the important and frequently encountered case where the optimal cost vector J,. is of the form 
J,. = Ie,  (14) 
where I is a scalar and e is the unit vector on R", i.e., 
e = [l, 1, ..., 13'. 
Equation (14) will hold, for example, if the matrix P$ of (8) corresponding to {p*, p*, . . .} has identical rows. When (14) holds the optimal cost per stage is the same for every initial state. In the next section we provide con- ditions that ensure that (14) holds. Furthermore, under these conditions we show that optimal stationary policies {p*,  p*, . . .} can be obtained from the optimality equation 
(15) 
where M is the (finite) set of all functions p :  S + C with p(i)  E U(i), i = 1,. . . , n, 
and the minimization is considered to be componentwise. Some connections with the discounted cost problem are also established in the next section. Subsequent sections provide computational algorithms for obtaining an optimal policy. The last section treats a problem involving a linear system and a quadratic cost functional. 
JPr + h,. = g,. + P,.h,. = min(g, + P,h,.), ,EM 
8.1 Existence Results 
Our first result provides a condition for existence of a stationary optimal policy satisfying a certain optimality equation. This condition is not readily verifiable but is implied by other more natural conditions, which we shall provide subsequently. 
Proposition 1 Assume that there exists a function h:  S + R and a 
constant 3, such that 
n 1 I + h(i) = min g(i, u )  + 1 p,,(u)h(j) Vi  = 1, . . . , n. (16) 
Then if p*(i) attains the minimum in (16) for every i = 1, . . . , n, the stationary policy n* = {p*, p*, . . .} is optimal. Furthermore, the optimal value of the cost functional J J i )  of (3) is equal to I for every i = 1, . . . , n, i.e., 
(17) 
ueU( i )  [ j =  1 
I = J,*(i) = inf n J,(i) Vi = 1, 2, . . . , n. 
8.1 EXISTENCE RESULTS 333 
Proof For any admissible policy n = {po ,  p l ,  . . .}, and any initial state xo E S let E { a  Ixo, n}, E { - I X k - 1 ,  U k -  1 ,  n} denote conditional expectation given the policy n is used and xo or x k -  and u k -  = &’- 1) have occurred, respectively. We have for any k 2 1, 
E { h ( x k ) l x O ,  = E { h ( X k ) l X k -  1, u k -  1 ,  1x0, . X k  x k - I , u k - I  XI. 1 
It follows that for every N 2 1, 
We have 
n 
n 
(19) 
1 2 min 8 ( x k -  1 ,  u )  + C p x k -  ,,,(u)hO’) - g ( x k -  1 ,  uk -  1 )  
uEU(Xk-1 )  [ j =  1 
= A + h ( x k -  1 )  - g ( x k -  1 ,  u k -  I ) ?  
with equality above when n = {p*,  p*, . . .} (by the definition of p*). Hence from (18) and (19) we have for every N 2 1,  
CN- 1 
or equivalently 
with equality if n = {p*,  p*, . . .}. Taking the limit as N + a, we obtain 
1 N - 1  
A G l im(l/N)E{ c 8 ( x k ,  u k ) I x O ,  = Jn(xO), 
N + m  k=O 
for every xo E S and every admissible policy n. Furthermore equality holds above when n = {p*, p*, . . .} and the result follows. Q.E.D. 
We note that the result of the previous proposition depends on the finiteness of the state space only to the extent that h is a bounded function, 
334 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
and indeed an extension of it can be shown to hold for an arbitrary state space [R3] assuming that h is bounded. 
Now given a stationary policy 7~ = { p ,  p ,  . . .} we may consider as in the past two chapters a problem where the constraint set U(i )  is replaced by the set o(i) = {p(i)),  i.e., O(i) contains a single element, the control p(i). Since for the resulting problem there is only one admissible policy, the policy { p ,  p, . . .}, application of Proposition 1 yields the following corollary. 
Let n = {p, p, . . .} be an admissible stationary policy. 
Assume that there exists a function h,: S -, R and a constant 1, such that 
Corollary 1.1 
n 
Then the value of the cost functional (3) corresponding to rt is the same for every initial state and is given by 
J,( i )  = 2, Vi = 1, 2 , .  . . , n. 
We now turn to obtaining conditions that guarantee the existence of 1 and h satisfying (16). At the same time we shall be able to establish a connec- tion with the discounted cost problem of Chapter 6. 
Consider the discounted cost functional 
Let us denote by J,( i )  the optimal value of this cost functional corresponding to a and the initial state i E S. We have from the results of Chapter 6 that J,( - ) is the unique solution of the optimality equation 
J,(i) = min g(i, u )  + a 1 pi,(u)Ja(jj , n 1 i = 1, . . . , n. (20) 
UE U(i) [ j =  1 
Let s be an arbitrary state in S and let us define 
h,(i) = J,(i)  - J,(s),  i = 1, . . . , n. (21) 
We have, by using (21) to eliminate J,(i) from (20), 
n 1 
1 
ha(i) + Jab),= min g(i, u)  + a C piju)[hao') + J,(s)] 
j =  1 
n 
u ~ U ( i )  [ 
= aJ,(s) + min ~ ( i ,  u)  + a C pi ju)h , ( j )  
u E U(i) [ j =  1 
from which n 
(1 - a)J,(s) + h,(i) = min u)  + c1 C p, ju)h,( j )  
U E  U(i) j =  1 
8.1 EXISTENCE RESULTS 335 
It follows from (22) and the finiteness of S and C that if for some sequence {a,} with 0 < a, < 1 and a, -+ 1 we have 
lim (1 - a,)Jam(s) = I ,  (23) 
(24) 
(i.e., the limits above exist), then the constant I and the function h :  S -+ R defined by (23) and (24) satisfy 
m - t m  
lim ham(i) = h(i), i = 1, . . . , n 
m- m 
n 1 1 + h(i) = min ~ ( i ,  u )  + 1 p,,(u)h(j) , i = 1, .  . . , n, 
u ~ U ( i )  [ j =  1 
and condition (16) is satisfied. The following proposition states that a sufficient condition for existence of a sequence {a,} such that the limits in 
(23) and (24) exist is that the differences [J,(i) - J,(s)] are uniformly bounded 
over a. 
Proposition 2 Assume that there exists a constant L such that for some state s E S we have 
IJ,(i) - J,(s)l d L Vi  E S,  a E (0, 1). (25) 
Then : 
(a) There exists a constant X and a function h :  S -+ R satisfying (16). (b) For some sequence a, -+ 1 we have 
h(i)  = lim [J,,(i) - Jam(s)],  i = 1, . . . , n. 
m-oo 
(c) Proof Let { u k }  be any sequence such that c(k -+ 1. By (25) the sequences 
{Jak(i)  - J,,(s)} are bounded. Hence there exists a subsequence of {ak} ,  
say {a,}, such that {Jam(i)  - Jam(s)} converges to a limit h(i) for each i E S,  
and part (b) is proved. Now by Proposition 6.1 and finiteness of the state space and control space we have 
lima+l (1 - a)J,(i) = A, V i  = 1, .  . . , n. 
IJ,m(S)I d M(1 - am)- ' ,  
where M is some constant. Hence the sequence {( 1 - a,) I Jam(s) 1 } is bounded. 
Thus there exists a subsequence of {a,}, say {a,.} such that 
( 1  - a,,)Jam.(s) -+ 1. 
From (22) we have 
336 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Taking the limit above and interchanging limit and minimization [using the finiteness of U(i)] we obtain 
n 1 1 + h(i)  = min B(i, u )  + 2 pi,(u)h(j) , 
ueU( i )  [ j =  1 
and part (a) is proved. 
+ 1 
and every subsequence of {ak}, say {am}, such that limm+m (1  - am)Jam(s) 
exists, we have 
lim (1  - am)Jam(s) = 1, 
where A is the optimal value of the problem [by part (a) and Proposition 13. It follows that limk-m (1  - ak)Jak(s) = A and hence lima-l ( 1  - a)Ja(s) = 2. Now if IJ,(i) - J,(s)l is uniformly bounded for some s it is also uniformly 
bounded for every s E S and hence by repeating the proof for every s E S we 
obtain lima-l (1 - a)J,(i) = 1 for all i E S. Q.E.D. 
We are now ready to state and prove the following proposition, which combined with Proposition 1 provides one of the main results of this section. 
Recall that to every admissible stationary policy {p, p, . . .} there corre- sponds a transition probability matrix P, defined by (4). For any positive integer m we shall denote by p;@) the element in the ith row andjth column of the matrix PI: (P, raised to the mth power): 
To prove (c) note that by the proof of (a) and (b) for any sequence 
m-m 
The scalar p;(p) is the probability that the state will b e j  after m stages when the initial state is i and the stationary policy n = {p, p, . . .} is used: 
p t @ )  = P(xm = j Jxo = i, n). 
For any two states i, s E S let us denote by Kis(p)  the smallest index k for which xk = s when xo = i and the stationary policy n = {p, p, . . .} is used: 
Kis(p)  = inf{klx, = s, xo = i, xi # s for 1 < j < k}. 
We call Kis(p)  thejrst  passage t ime from i to s associated with p. For each i, s, and p, Kis(p) may be viewed as a random variable taking positive integer values or the value + co with probabilities 
4: = P(Kis(p)  = k) = P(xk = s, xi # s, 1 < j < k l x ,  = i ,  n), m 
P(K, , (p)  = 03) = 1 - c q:s. 
k =  1 
8.1 EXISTENCE RESULTS 337 
We define the meanjrst  passage time E {Kis(p)}  associated with p by 
otherwise. 
One may show (see Appendix D) that for any given state s E S, E{Kis (p ) }  < 00 V i  E S =- p z ( p )  > 0 for some mi 2 1 Vi E S,  (26) 
where pz was defined above. Furthermore, if the stochastic matrix P, 
corresponds to an irreducible Markov chain (see Appendix D), then we have E {Ki,(p)} < CO for all i ,  j E S.  
Proposition 3 Suppose that there exists a state s E S such that for every admissible stationary policy n = {p, p, . . .} and every state i E S we have 
E{Kis(p)}  < 00. (27) 
Then there exists a constant 3, and a function h : S -, R satisfying (16), i.e., 
n 1 I + h(i) = min &, u) + Cpi,(u)h(j)  , i = 1 , .  . ., n. 
ucU(i)  [ j =  1 
Proof We assume without loss of generality that 
0 < #(i, u )  < M Vi E S ,  u E C, (28) 
where M is a constant. This is true since, by the finiteness of S and C, g(i, u )  is bounded, and furthermore the addition of a constant to g(i, u )  merely adds the same constant to the cost functional (3) for every admissible policy. Let a be any discount factor, 0 < a < 1, and {pa, pa, . . .} a policy that minimizes the corresponding discounted cost. We have, for every i E S, 
By (28), the first term on the right is less than or equal to M E {Kis(pa)}.  The second term is equal to 
g C x k  3 / d x k ) 1  I xKt.(p.) = s = E {aK's'Cm'}Ja(s),  I E { a K i ~ ( P . 4 }  E { f a k - K i d / k ) -  
k = K i s ( , d  
which is in turn less than or equal to Ja(s). Hence if Q is an integer such that E {Kis (p ) }  < Q for all i and p, we obtain 
or JAi) < M E { K i s ( P a ) }  + JAs) G MQ + Ja(s) ,  
J,(i) - J&) < MQ. (30) 
338 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Also by (29), 
J,(i) 2 J,(s) E{aKis(pD)}, 
or equivalently 
J,(s) - J,(i) < [l - E{aKis(pa)}]J,(s). (31) 
By Proposition 1 in Chapter 6 we have 
while using the fact that 0 c a -= 1, we have 
where Q is the integer for which E { K , , ( p ) }  < Q. From (31)-(33) we obtain 
Q-  1 
i = O  
J,(s) - J,(i) 6 [(l - aQ)/(l - a)]M = 1 a'M 6 QM.  (34) 
Combining (30) and (34), 
IJ,(i) - J,(s)l < M Q  V i  E S,  a E (0, 1) 
and the result follows by Proposition 2. Q.E.D. 
Condition (27) is satisfied in particular if every stationary policy gives rise to an irreducible Markov chain (see Appendix D). It is to be noted that from the preceding proof it is evident that it is sufficient that (27) holds only for stationary policies that minimize the expected discounted cost for some discount factor. It is possible to obtain other conditions that guarantee the 
existence of I and h such that (16) holds. One such condition is the following. 
Weak Accessibility Condition For any two states i,j E S there exists an admissible stationary policy IL = {p, p, . . .} and an integer rn such that 
pz{p) = P(x ,  = j l x o  = i ,  n) > 0. (35) 
Proposition 4 Suppose that the weak accessibility condition holds. 
Then there exists a constant I and a function h :  S + R satisfying (16), i.e., 
n 1 I + h(i) = min g(i ,  u) + C pi,{u)h(j) , i = 1 , .  . . , n. 
UE U ( i )  [ j =  1 
Proof See the Appendix to this chapter. 
8.1 EXISTENCE RESULTS 339 
Combination of Propositions 1 and 3 or Propositions 1 and 4 yields: 
Theorem Under the assumption of Proposition 3 or under the weak 
accessibility condition there exists a constant I and a function h :  S -, R 
such that 
n 1 I + h ( i ) =  min g(i ,u)+ C p i J ( u ) h ( j )  , i =  1 , .  . . , n .  (16’) 
Furthermore, the optimal value of the cost functional J,(i) of (3) is equal to I for every i = 1, . . . , n, i.e., 
u E U ( i )  [ j= 1 
I = inf J,(i), i = 1, . . . , n. 
n 
In addition if p*(i) attains the minimum in the right-hand side of( 16’) for every i = 1, . . . , n, then the stationary policy n* = {p* ,  p*, . . .} is optimal. 
The conditions listed above are probably the weakest known that guarantee that the optimal average cost per stage is independent of the initial state. It is clear, of course, that some sort of accessibility condition must be satisfied by the transition probability matrices corresponding to stationary policies or at least to optimal stationary policies. For if there existed two states none of which could be reached from the other no matter which policy we use, then it can be only by accident that the same optimal cost per stage will correspond to each one. An extreme example of this type of situation is to consider a problem where the state is forced to stay the same regardless of the control applied, i.e., each state is absorbing. Then the 
optimal average cost per stage for each state i will be minuEu(i, &, u )  and 
this cost may be different for different states. 
Finally, we state the following corollary of Proposition 3, which is obtained in the same way as Corollary 1.1. 
Corollary 3.1 Let 7r = {p, p, . . .} be an admissible stationary policy and assume that there exists a state s E S such that E{K, , (p ) }  c co for all 
i E S. Then there exists a constant I, and a function h,: S -, R such that 
(36) J,(i) = I,, i = 1 , .  . . , n, 
and furthermore 
n 
1, + h,(i) = SCi, ,u(i)I + 1 pij[,u(i)]hp(j), i = 1 , 2 ,  . . . , n. (37) 
Equation (37) represents a system of n linear equations with (n + 1) unknowns-the scalars I , ,  h,(l), h,(2), . . . , h,(n). We may add one additional 
equation to this system by requiring that 
j= 1 
h,(s) = 0. (38) 
340 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
This can be done since if {A,, h,(l), . . . , h,(n)} is a solution of (37) so is {Ap ,  h,(l) + r, . . . , h,(n) + r}, where r is any scalar. Corollary 3.1 states 
that under the assumption E{Kis(p)}  < 00, system (37) and (38) has at least one solution. We now show that the same assumption guarantees that the system of equations (37) and (38) has a unique solution. 
Proposition 5 For any admissible stationary policy R = {p, p, . . .} for which there exists an s E S such that E {Kis@)}  < 00 for all i E S, the system of equations (37) and (38) has a unique solution. 
Proof Let (1, h(l), . . . , h(n)} and {A’, h’(l), . . . , h‘(n)} be two solutions. We have 1 = I’ = 1, by Corollary 1.1. Hence from (37) we obtain for every 
m 2 1, 
h - h’ = P,(h - h‘) = Py(h - h’), 
or equivalently n 
h(i) - h’(i) = 1 pz{p)[h(j)  - h’(j)] Vi  = 1,. . . , n. 
j =  1 
From (26) and for a fixed i we obtain for some mi 2 1 and E~ > 0, 
p 3 p )  2 Ei  > 0 
and from (38), h(s) - h’(s) = 0. Hence 
n 
IhG) - h’(i)l < 1 P?(P)IhO’) - h’0’)I 
= CP?(P)IW - h’O’)l 
j =  1 
j + s  
< (1 - ci) max I h(j)  - h’(j) 1. 
J 
Thus we obtain 
max I h(j) - h’(j) I < (1 - E )  max I h(j) - h’(j) 1, 
i i 
where E = min[E,:. . . , en] > 0. 
Hence h(j)  = h’(j) for all j .  Q.E.D. 
We close this section with an example. 
MACHINE REPLACEMENT EXAMPLE Consider a machine that can be in 
any one of n states, S = { 1,2, . . . , n}. The implication here is that state i 
is better than state i + 1, i = 1,2,. . . , n - 1, and state 1 corresponds to a 
8.1 EXISTENCE RESULTS 341 
machine in perfect condition. The operating cost per unit time for which the machine starts in state i is denoted gi, and we assume 
(39) 0 < g1 < 92 < ... < gn. 
p . .  V = 0 if j < i ,  (40) 
p i i <  1, i =  1 ,..., n, (41) 
During a time period of operation the transition probabilities satisfy 
i.e., the machine cannot go to a better state with usage. We also assume that 
n n 
i < i'* c p i j  < c p i f j  Qk = 1, 2, .  . . ,n. (42) 
At the beginning of each period the state of the machine is determined and a decision is made whether to replace the machine at a cost R > 0 with a new machine that is in state 1 or to continue operation. Thus there are two possible controls-replace and do not replace. The problem is to find a policy that minimizes the average cost per period. 
It is to be noted that the hypothesis of Proposition 3 is not satisfied for this problem. Indeed, consider the policy that never replaces. Then assump- tions (40) and (41) imply that for this policy the only state that can be reached from every other state is the state n. Consider also the policy that replaces the machine at every state. Then, assuming pln = 0, state n cannot be reached from any state i # n. Notice also that one cannot guarantee in the absence of further assumptions that the weak accessibility condition stated after Proposition 3 is satisfied. We shall be able, however, to argue in terms of Proposition 2. 
Consider the corresponding discounted problem with a discount factor a < 1.  Then we have 
j = k  j = k  
It follows that 
It is possible to show (as in the second example of Section 6.1) that in view of (39)-(42), we have for all c1 E (0, l), 
0 < J,(i) - Ja(l), i = 1, 2, .  . . ,n. 
342 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Furthermore J,(i) - J,(l) is nondecreasing in i. Hence by Proposition 2 
there exists a scalar 1 and a nondecreasing function h(i), i = 1, . . . , n, such 
that 
n n 1 1 + h(i) = min R + g1  + pljh(j), gi + 1 pi jh( j )  , i = 1,2,. . .,n, [ j =  1 j =  1 
and the policy that chooses the minimizing action above is average cost optimal. Let 
i* = max ilg, + ip i jh( j )  < R + g1 + tpljh(j)}. 
Then the policy that replaces if the current state is greater than i* and does not replace otherwise is optimal. 
{ j =  1 j =  1 
8.2 Successive Approximation 
Since, as seen in Chapter 6, the method of successive approximation may be used for computing the optimal discounted cost function J ,  of (20) and furthermore under the assumption of Proposition 2 we have 
lim(1 - a)J,(i) = 1, i = 1,2 , .  . .,n, 
a- 1 
one expects that a limiting form (as a + 1) of the successive approximation 
method may be used for the average cost problem. Indeed, this is the case under an assumption that we shall introduce shortly. Prior to proceeding with precise formulations and results let us provide a heuristic discussion that indicates the appropriate limiting form of the successive approximation method. 
Let J :  S + R be any function on S ,  a E (0, 1) be a discount factor, and 
consider the following mapping T,, which is familiar from Chapter 6: 
n 1 T,(J)(i) = min S(i, u )  + a 1 piJ(u)~(j) , i = 1, . . . , n. 
ueU( i )  [ j =  1 
As discussed in Section 6.2, the successive approximation method for the a-discounted problem consists of the iteration 
T;+'(J)(i) = min g(i, u )  + a i p , j u ) T * ( J ) ( j ) ] ,  i = 1, . . . , n. (44) 
u s U ( i )  [ j =  1 
We have 
lim T;(J)(i) = J,(i), i = 1, . . . , m, 
k - m  
8.2 SUCCESSIVE APPROXIMATION 343 
for an arbitrary function J: S + R, where J, is the a-discounted optimal value function. Since we may have Tt(J)(i) + 03 as k + 03 and a + 1 we shall rewrite-(44) in terms of quantities that have finite limits as k + co and 
a +  1. 
For any fixed state s E S let us denote, for all i and k, 
ha, k ( i )  = T t ( J ) ( i )  - Tk(J)(s). (45) 
Using the notation above we may write (44) as 
n 1 [T:+’(J)(s) - a7%J)(s)1 + h a , k + l ( i )  = min !%i, u )  + 1 P i A U ) h a , k O ’ )  . 
j =  1 
(46) 
(47) 
u e U ( i )  [ 
Let us denote, for all i = 1, 2, . . . , n and k, 
H a , k ( i )  = h a , k ( i )  + [T:(J)(s)  - aT:-’(J)(s)l, 
h a , k ( i )  = H a , k ( i )  - H a & ) ,  
From (45) and (47) we have 
i = 1, 2, . . . , n. (48) Now we may write (46) [or, equivalently, (44)] as 
n 
(49) 1 H a , k +  l ( i )  = min &i, u, + a 1 Pi,iU)ha,kO’) 5 
u s U ( i )  [ j =  1 
with ha, k( i )  defined by 
h a . k ( i )  = H a , k ( i )  - H a , k ( s ) -  (50) 
Algorithm (49) and (50) with a starting function ha,o: S -, R satisfying 
ha, o(s) = 0 may be viewed as an alternative implementation of the successive approximation algorithm (44) and may equally well be used for solution of the a-discounted problem. In the limit algorithm (49) and (50) will yield function5 ha and H a  via the relations 
h,(i) = lim h a , k ( i ) ,  
H,(i) = lim H a , k ( i ) ,  
i = 1, 2, . . . , n, 
i = 1, 2, . . . , n. 
(51) 
(52)  
k- .  m 
k + w  
In addition we will have [cf. (45) and (47)] 
h,(i) = J,(i) - J,(s), 
H a ( s )  = (1 - a)Ja(s), 
i = 1, 2, . . . , n, (53) 
(54) 
from which the optimal values J,( l), J,(2), . . . , J,(n) may be recovered. 
344 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Now if we formally take the limit as u + 1 in algorithm (49) and (50) and 
denote 
hk(i) = lim ha,k(i), 
Hk( i )  = lirn Ha,k(i) ,  
a- 1 
01’1 
we obtain the algorithm n 
(57) 
(58)  
1 Hk+ l(i) = min g(i, u, + 1 pi,iu)hk(j) 7 
u ~ U ( i )  [ j =  1 
hk(i) = Hk(i) - H k ( S ) ,  
where h,: S -+ R is a function with h,(s) = 0. Let us suppose for a moment that the algorithm yields functions H and h via 
h(i) = lim hk(i), 
H( i )  = lirn Hk(i). 
k -  m 
k + m  
(59) 
Then assuming that the limit with respect to u and k may be interchanged, 
lirn ha(i) = lirn lirn ha&) = lirn lirn ha,k(i) = lirn hk(i), 
lim Ha(i)  = lim lirn ffa,k(i) = lirn lim HaVk( i )  = lirn Hk(i), 
a+ 1 a - 1  k-m k-m a+1 k + m  
a+ 1 a’l k + m  k - m  a-rl k -  m 
we obtain from (53), (54), (59), and (60): 
h(i) = lim[Ja(i) - Ja(s)],  i = 1, 2, . . . , n,  
i =  1 , 2  ,..., n. 
01’1 
H(s)  = lim(1 - u)J,(s), 
a+ 1 
However, by Proposition 2 these imply, under the corresponding assump- tions, that the quantity H(s)  obtained from algorithm (57) and (58) is equal to the optimal average cost per stage of the problem and the function h enters in the optimality equation (16). 
The conclusion from this informal discussion is that algorithm (57) and (58)  is the natural candidate as a successive approximation method for the problem of this chapter and, under appropriate assumptions, should yield in the limit the optimal average cost per stage. 
The validity of this conjecture is established in the following proposition. In fact, we need not require that h,(s) = 0 since by (58 )  we will have h k ( S )  = 0 for all k 2 1 even if h,(s) # 0. 
8.2 SUCCESSIVE APPROXIMATION 345 
Proposition 6 Assume that there exists an E > 0 and a positive integer m such that for some state s E S and all admissible policies n = {po, pl, . . .} we have 
(61) 
where PPr ,  k = 0,.  . . , m, denotes the transition probability matrix corre- 
sponding to pk as in (4) and [P,, P,,- . + . PpOlis denotes the element in the ith row and sth column of the matrix PPm . . . P,, . Consider the algorithm 
[P,, P,,- . . . Ppo]is 2 E > 0 Vi = 1,2, . . . , n, 
n 
(62) 
i = 1 ,2 ,  . . . , n, k = 0, 1,  . . . , 1 u)  + 1 pi@)hk(j) , 
u E U ( i )  j =  1 
where ho: S -, R is an arbitrary function. Then the limits 
h(i) = lim hk(i), 
H(i)  = lim Hk(i), 
i = 1, 2, .  . . , n, 
i = 1, 2, . . . , n, 
k+m 
k-m 
exist and we have 
H(s) = 1 = inf Jn(i), i = 1, 2, . . . , n, (66) 
n 
i.e., 1 is the optimal average cost per stage of the problem. In addition, I, and h satisfy 
g(i, u )  + j =  1 pil(u)h(j)]. (67) 
Proof Let pk(i) E U(i)  attain the minimum in (62) for every k and i. Denote for all k 
Hk(l)  gC1, pk(l)l 
Hk = [ Hk(n) ] h k = r y j  hk(n) g P k = [  g[n, pk(n)l ] 
We have 
346 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
and hence 
where e is the unit vector e = [l, 1,.  . . , 13'. From the relations above we 
obtain 
Since this relation holds for every k b 1, by iterating we obtain 
Write 
Then (68) yields 
Now we have for all k by hypothesis [P , , - ,  - . . P,,_,  , I i s  b E > 0, and by (63), q k ( S )  = 0. Hence from (69) 
i i 
max qkG) < (1 - &) max qk-m- 1G) - [Hk+ - Hk-m(S)l. (70) 
Using a similar argument, from (68) we also obtain 
min qku) 2 (1 - dmin 4 k - m -  1G) - C H k +  1 ( 4  - H k - m ( S ) I *  (71) 
j i 
From (70) and (71) we have 
which implies that for all k greater than some index and some B > 0 we have 
max q k o )  - min qkG) < B(1 - E ) ~ / ( " ' + ~ ) .  
i j 
Since &(S) = 0, it follows that 
I h k  + l(i) - hk(i) I = I qk(i) I < max q k ( j )  - min &(j) < B( 1 - E ) ~ / ( ~ +  l) ,  
j j 
8.2 SUCCESSIVE APPROXIMATION 347 
This in turn implies that {hk(i)} converges to some real number h(i): 
h(i) = lim hk(i), i = 1, 2, . . . , n. 
k-cc 
From (62) we see that the sequence {Hk} also converges to a vector H E R”, and we have 
n 
(72) 1 ~ ( i )  = min g(i, u)  + Cpiju)h(j) , 
ueU( i )  [ j =  1 
as well as 
h(i) = H(i) - H(s). (73) 
From (72) and (73) we have 
H ( s )  + h(i) = min g(i, u )  + pi,(u)h(i)], U E  U(i) [ j=  1 
and by Proposition 1, H(s)  = A = inf, J,(i). Q.E.D. As for discounted problems, one may obtain upper and lower bounds 
on the optimal average cost per stage A via the successive approximation algorithm. 
Proposition 7 Under the assumption of Proposition 6 for algorithm (62) and (63) there holds 
Hk(s) + ck < Hk+l(S) + ck+l < A < Hk+l(S) + ?k+l < Hk(s) + ck, (74) where for all k 2 1, 
ck = min[Hk+,(i) - Hk(i)], 
c k  = max[H,+,(i) - Hk(i)]. 
i 
i 
(75) 
(76) 
Proof Let pk(i)  attain the minimum in (62) for each k and i. We have n 
348 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Taking the minimum over i we obtain 
H k - , ( s )  + c k - 1  < H k ( S )  + c k .  
A similar argument shows that for all k 
H k ( S )  + t k  < H k -  1(s) + E k -  1. 
Since ck tends to zero by Proposition 6 we have {Hk(s)  + ck}  + 1 and since 
{ H k ( S )  + c k }  is a nondecreasing sequence it follows that H k ( S )  + ck 6 1. Similarly Hk(s) + Ek 2 1 and the result is proved. Q.E.D. 
We now demonstrate the successive approximation algorithm and the error bounds (74) by means of an example. 
6.2. We have EXAMPLE 1 Consider an undiscounted version of the example of Section 
s = {1,2], c = {u', u2}, 
and 
g(1, u') = 2, g(1, u2) = 0.5, 532, u') = 1, g(2, u2) = 3. 
Letting s = 1 be the reference state, algorithm (62) and (63) takes the form c 2 
   
and the constants ck, i$ of (75) and (76) are given by 
The results of the computation starting with h,(l) = h,(2) = 0 are shown in Table 8.1. 
8.3 POLICY ITERATION 349 
TABLE 8.1 
0 1 2 3 4 5 6 7 8 9 
10 11 12 13 14 15 16 17 
0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 
0.00000 0.5oooO 0.25000 0.37500 0.3 1250 0.34375 0.32813 0.33594 0.33203 0.33398 0.33301 0.33350 0.33325 0.33337 0.33331 0.33334 0.33333 
0.5oooO 0.87500 0.68750 0.78125 0.73438 0.75781 0.74609 0.75195 0.74902 0.75049 0.74976 0.75012 0.74994 0.75003 0.74998 0.75001 0.75000 
0.62500 0.68750 0.7 1875 0.73438 0.742 19 0.74609 0.74805 0.74902 0.74951 0.74976 0.74988 0.74994 0.74997 0.74998 0.74999 0.75000 
0.87500 0.8 1250 0.78125 0.76563 0.75781 0.75391 0.75195 0.75098 0.75049 0.75024 0.75012 0.75006 0.75003 0.75002 0.75001 0.75000 
8.3 Policy Iteration 
The policy iteration algorithm for solving the average cost problem is similar to those described in the past two chapters. Given a stationary policy one obtains an improved policy by means of a minimization process until no further improvement is possible. We shall assume throughout that there exists a state s E S such that for every admissible stationary policy n = {p, p, . . .} we have 
E {Kis(p) }  < co vi = 1, . . . , n, 
as in Proposition 3. Let nk = {pk, pk, . . .} be an admissible stationary policy obtained at the 
kth iteration of the algorithm. We determine the average cost per stage I,, corresponding to nk by solving the system of (n + 1) equations 
350 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
This system has a unique solution by Proposition 5. Subsequently we find a policy nk+l = {pk+l ,  p k + l ,  . . .} where pk+l( i )  is such that 
n 
&i, pk + '(ill  + C p i j L k  + '(i)Ih,kO') j =  1 
u e U ( i )  [ j =  1 
n 
(79) 1 = min a(i, u )  + Cpi,(u)hPk(j) , i = 1,. . . , n, 
where we set pk+'(i)  = pk(i) if pk(i) attains the minimum above. Let j l , k + I  
and hpk+ I(i), i = 1,  . . . , n, be the unique solution of the system of equations 
n 
A,,k+i -k h,++i(i) = a[i, pk+'(i)] -k 1 pij@k+'(i)]hpk+ lo), i = 1, . . . , n, 
j =  1 
hpk+ I(S) = 0. 
We claim that A,,, 2 A,k+l. 
Indeed, by switching to vector-matrix notation and using (77)-(80), we can write 
and 
where e = [l, 1, . . . , 11' and I is the n x n identity matrix. By multiplying 
both sides of the vector inequality by the matrix Ppk+l the inequality is preserved since Ppk+ I  has nonnegative elements, and we have 
A,ke -k h,k = grk -k P,kh,k 2 g,k+ I  + Ppk+ I  hpk, (81) 
A,ke 2 Q,k+ I  + (P,k+ 1  - I)h,k, 
A,kP,,k+le 2 Ppk+lgpk+l + (Pi,+, - Ppk+l)hpk. 
Since P,k+ l e  = e, we obtain 
Apke 2 Ppk+lgpk+l + (P;k+l - PCk+l)hCk. 
Similarly we have for every i 2 0, 
A,ke 2 PLk+ I g p k +  I + (P??I - PLk+ l)hpk. 
Hence by summing over i we obtain for every N 2 1, 
Since (P;k+l - I)hpk is bounded we have limN+m(l/N)(P$+l - I)h,k = O 
and furthermore 
8.3 POLICY ITERATION 351 
by (6). Hence from (82) we obtain 
Apke 2 lirn(l/N) 1 P~k+lgpk+I  = l p k + l e ,  
N+CO r1 i = O  ) 
and (80) is proved. Thus the policy { p k + ’ ,  p k + ’ ,  . . .} obtained via (79) is as good or better 
than the policy {pk ,  p”, . . .}. Now consider the generated sequence {A,,}. Since it is a nonincreasing sequence and furthermore the set of all stationary policies is finite, we must have for some 1 and some index E ,  
A,,, = 1 Vk 2 E .  (83) 
p k  = p* Vk 3 k, (84) 
If, in addition, we have for some policy IL* = {p*, p*, . . .}, 
then a* must be optimal in view of construction (77) and (79) and Proposition 1. Relation (84) can be guaranteed if different policies have different average costs per stage associated with them. Another assumption that, as we prove below, guarantees (84) is when for all k 3 E the matrices 
N -  1 
p,*. = lim (1/N) 1 PLk 
of (7) have identical rows each element of which is positive. This occurs if under each transition probability matrix p,,k the resulting Markov chain is irreducible (see Appendix D). Indeed under these circumstances if f l k  is the (row) vector consisting of the row elements of P;l[;, 
N+CQ i = O  
f l k  
4% = [ 8,1 
then from (81) we have 
IZpkflk+le + P k + I h p k  2 flk+lgpk+I + flk+lPpk+1hpk, (85) and by Lemma 1 we obtain flk+Igpk+l = i , k + l  and f l & + l P p k + l  = f lk+l .  Thus (85) is equivalent to 
Since the elements of f l k +  are positive we have equality above if and only if equality holds in (81) or equivalently pk(i) attains the minimum in (79). Thus relation (83) implies that p”(i) attains the minimum in (79). Hence (84) holds and p k  is optimal. 
We state the last conclusion from the preceding discussion as a propo- sition. 
A p k  2 A , k + l .  
352 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Proposition 8 Assume that for every admissible stationary policy {p, p, . . .} the transition probability matrix P, gives rise to an irreducible Markov chain. Then the policy iteration algorithm will yield an optimal policy in a finite number of iterations. 
We now demonstrate the policy iteration algorithm by means of the example of the previous section. 
EXAMPLE 1 (CONTINUED) Let 
pO(1) = ul ,  pO(2) = u2. 
We take s = 1 as the reference state and we obtain Ape, hFO(l), hWo(2) from the system of equations 
+ h,o(l) = 8(1, u ' )  + P11(u1)h,o(1) + P12(u1)h,o(2), 
4 0  + h,o(2) = 8(5 u2) + Pz1(u2)h,o(l) + P2z(u2)h,o(2), h,o(l) = 0. 
Substituting the data of the problem 
1,o = 2 + *h,0(2), L,o + h,o(2) = 3 + $h,o(2), 
from which D 1,o = 2.5, h,o(l) = 0, h,o(2) = 2. q 
We now find pl(l), p'(2) by the minimization indicated in (79). We determine 
The minimization yields 
D Dl(1) = u2, p'(2) = ul. 
8.4 INFINITE STATE SPACE 353 
By substitution of the data of the problem, we obtain 
D A,, = 0.75, h,i(l) = 0, h,1(2) = -$. Q 
We find p2( l), p2(2) by determining the minimum in 
p2(1) = p'(1) = u2, pZ(2) = pl(2) = u1, 
and hence the policy above is optimal and the optimal average cost per stage is A,,, = 0.75. 
8.4 Infinite State Space-Linear Systems with Quadratic Cost Functionals 
The standing assumption in the preceding sections has been that the state space is finite and thus the underlying system is a controlled finite state Markov chain. Once one removes the finiteness assumption on the state space many of the results presented in the past three sections no longer hold. For example, while one could restrict attention to stationary policies for finite state systems this is not true anymore where the state space is infinite. For instance, the following example (due to Ross [R4]) shows that for a countable state space the optimal policy may be nonstationary. (This 
354 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
fact is true even if one expands the class of admissible policies to admit randomized policies [R4].) 
EXAMPLE Let the state space be S = { 1,2,3, . . .} and let there be two control actions C = {u', u'}. The transition probabilities under u' and u2 are specified by 
pici+ l)(ul) = pii(u2) = 1. 
In other words, the system is deterministic and application of u1 moves the state from i to (i + l), while application of u2 leaves the state unchanged. The costs per stage are 
g(i, u ' )  = 1, g(i, u2) = I/i, i = 1,2, 3 , .  . . . In other words, at state i we may either move to state (i + 1) at the cost of one unit or stay at i at a cost l/i. 
Now for any stationary policy n = {p, p, . . .} other than the policy for which p(i) = u1 for all i, let n(n) be the smallest integer for which 
p[n(n)] = u2. 
Then concerning the average cost per stage corresponding to this policy we clearly have 
J,(i) = l/n(n) > 0 
For the policy where p(i) = u1 for all i we have J,(i) = 1 for all i. Since the optimal cost per stage cannot be less than zero, it is clear that 
Vi < n(n). 
inf J,(i) = 0, i = 1, 2, . . . . n 
However, the optimal cost is not attained by any stationary policy, so that no stationary policy is optimal. On the other hand consider the non- stationary policy n* that on entering state i chooses u2 for i consecutive times and then chooses u'. If the starting state is i, the sequence of costs incurred is 
1 1 1 1 1 1 
- 1 , - -  + 2 '  . . .  . 
i +  1 '  i +  l ' i +  1 ' " ' '  9 . ,  1, ~ - 
+ 2 '  
- 1 1  
i ' i  "" 1 
_ _  
i times ( i  + I )  times 
The average cost corresponding to this policy is 
2m Jz*(i) = lim = 0 ,  i =  1 ,2 ,3  ,.... 
m-+m ZF= 1 (i + k) Hence the nonstationary policy n* is optimal while, as shown above, no stationary policy is optimal. 
8.4 INFINITE STATE SPACE 355 
Generally speaking the analysis of average cost optimization problems involving an infinite state space presents considerable difficulties and as yet there exists little in the way of a complete and powerful theory. However, certain particular special cases can be satisfactorily analyzed and one such case is the average cost version of the linear-quadratic problem examined in Chapters 3,4, and 6. 
Consider an undiscounted version (a = 1)  for the linear-quadratic problem of Section 6.5 involving the system 
X k + l = A X k + B U k + W k ,  k = 0 , 1 ,  ..., (86) 
and the cost functional 
J,(Xo) = lim (1/N) E 1 [ X ; Q x k  + p k ( X k ) l R p k ( X k ) l  (S7) 
N +  w k = O .  wk 1, ... {:I I 
We make the same assumptions as in Section 6.5, i.e., that wk are independent and have zero mean and finite second moments. We also assume that the pair (A, B) is controllable and that the pair (A, C), where Q = C‘C, is ob- servable. Under these assumptions it was shown in Section 3.1 that the Riccati equation 
KO = 0, (88) 
(89) Kk+l = A‘[Kk - KkB(B’KkB + R)-’B’K,]A + Q, 
yields in the limit a matrix K, K = lim Kk,  
k - c o  
which is the unique solution of the algebraic Riccati equation 
K = A’[K - KB(B’KB + R ) -  ‘B’KIA + Q (91) 
within the class of positive semidefinite symmetric matrices. Now the optimal value of the N-stage costs 
has been derived earlier and was seen to be equal to 
Thus using (90) and the fact that N -  1 
lim ( 1 / ~ )  1 E { w ’ K , ~ }  = E {w’Kw}, 
N - t m  k = O  
356 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
the optimal finite horizon costs tend in the limit as N 00 to 
1 = E { W ’ K W } .  (93) In addition, the N-stage optimal policy in its initial stages tends to the station- ary policy 
(94) P*(x)  = -(B’KB + R)-’B’KAx.  
Furthermore, a simple calculation shows that, by the definition of A, K, and p*(x), we have A + x’Kx = min E { x ’ Q x  + u‘Ru + ( A x  + Bu + w)’K(Ax + Bu + w ) } ,  
while the minimum in the right-hand side of the above equation is attained at u* = p*(x) as given by (94). 
Now by repeating the proof of Proposition 1 of this chapter, we obtain 
U 
1 < (1/N) E {&KxNIxo, n} - (1/N)xbKxO 
with equality if n = {p*, p*, . . .}. Hence if n is such that E { x ~ K x N I x O ,  n} is uniformly bounded over N, we have by taking the limit above. 
1 < J,(x) Vx E R”, 
with equality if n = {p*, p*, . . .}. Here the stationary policy {p*, p*, . . .} as given by (94) is optimal over all policies n with E { X ~ K X ~  ( x o ,  n} bounded uniformly over N. 
8.5 Notes 
The average cost problem was first formulated and analyzed by Howard [H15]. Several authors have contributed subsequently to the problem [B2, B25, L1, R4, S7, V2, V4], most notably Blackwell [B19]. 
In our approach to the results of Section 8.1. we follow Ross [R4]. This approach is generalizable to situations where the state space is infinite. For alternative expositions see references [D4], [KlO], and [PI]. The result of the appendix was shown by Bather [B2]. The successive approximation method of Section 8.2 was devised by White p 2 ] .  The error bounds of Proposition 6 are due to Odoni [Ol]. Related results for more general situations have been given recently in references [H8] and [H12]. The policy iteration algorithm can be generalized for problems where the optimal average cost per stage is not the same for every initial state (see [B19], [V2], 
PROBLEMS 357 
and [D4]). For a computational approach based on linear programming see [M3] and [D4]. For an analysis of average cost Markovian decision problems involving exponential risk-sensitive cost functionals, see the paper by Howard and Matheson [H17]. For analysis of infinite horizon versions of inventory control problems such as the one considered in Section 3.2, see references [13], [H13], [H14], and [VS]. 
Problems 
1. Assume that for some state s we have that J,(i) - J,(s) is uniformly 
bounded for a E (0, 1). Show that for a sequence {ak} with ak --t 1, ak E (0, l), and a sequence of a,-optimal policies {pak} ,  we have p,,(i) = p*(i) for all i and all k sufficiently large, where p* is average cost optimal. 
2. Show that if for some sequence {ak} with ak E (0, l), ak + 1, and a 
sequence of a,-optimal policies {pQk}  we have pak(i) = p*(i) for all i and all k sufficiently large, then p* is average cost .optimal. 3. Optimal Control of Deterministic Finite State Systems Consider a stationary deterministic control system 
xk+i =f(Xk,Uk), k = 0 , 1 , .  .., 
where the state xk belongs to a finite state space S = { 1,2, . . . , n }  and the 
control u k  is constrained in a subset u(xk) of a finite control space C. We say that the system is completely controllable if given any two states i ,  j E S there exists a sequence of admissible controls that drives the state of the system from the state i to the statej within at most (n  - 1) steps. For a completely 
controllable system and a given initial state xo = i consider the problem of finding an admissible control sequence {uo,  u l , .  . .} that minimizes 
N- 1 
Jz( i )  = lim (l/N) 1 dxk, uk), 
N- m k = O  
where g: S x C -+ R is given. Show that an optimal control sequence exists and that the optimal cost is the same for every initial state. Show also that there exist optimal control sequences that after a certain time index are periodic. 4. Consider a stationary inventory control problem of the type considered in Section 3.2 but with the difference that the stock xk can only take integer values from 0 to some integer M. The amount of the order u k  can take integer values with 0 < u k  < M - xk and the random demand w k  can only take 
nonnegative integer values with P(wk = 0) > 0 and P(wk = 1) > 0. Un- satisfied demand is lost so that stock evolves aqcording to the equation 
358 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
xk+ = max(0, xk + uk - wk). The problem is to find an inventory policy 
that minimizes the average cost per stage. Show that there exists an optimal stationary policy and that the optimal cost is independent of the initial stock X O .  
Appendix Existence Analysis under the Weak Accessibility Condition 
In this appendix we provide a proof of Proposition 4 of Section 8.1. In fact, we shall prove a more general result that contains Proposition 4 as a special case. The analysis requires a high degree of mathematical sophistication and is directed toward the advanced reader. 
Consider a controlled process in discrete time with a finite state space 
S = (1, 2, . . . , n} .  We assume that for any state i E S ,  the next transition is 
controlled by choosing a probability vector p i  = ( p i l ,  p i 2 ,  . . . , p in)  from a closed convex set Di E R". Any selection p i  E D i ,  i = 1,2, . . . , n, defines the 
rows of a stochastic matrix P E D = D1 x D2 x . . x D,. The cost of each 
transition is prescribed by functions ci(pi), i = 1, . . . , n, each assumed 
convex and continuous on the corresponding set D i .  Thus when the current state is i and probability vector pi E Di is selected, the cost incurred is ci(pi). If P E D is used at each time, the corresponding average expected cost is P*c, where 
P* = lim ( 1 / ~ )  (1 + P + P2 + . . + pN- '}, N + m  
and c is the vector with coordinates c l (p l ) ,  . . . , cn(pn), where p l , .  . . , p,, are 
the rows of P. Since the components of c depend continuously on the rows of P, the cost c(P) is bounded over D and we have 1 J*(i)I < ix) with 
J* = infP*c, 
where minimization above is considered separately for each coordinate of P*c. 
P E D  
We shall rely on the following accessibility assumption : 
For any pair of states i ,  j E S, there exists a matrix P E D and a positive integer r such that p i j  > 0, where p i j  is the element in the ith row and j th  column of the matrix P' (P to the rth power). 
Based on this assumption we shall prove that there exists a vector h E R" and a constant 1 such that 
1e + h = min{c + Ph}, PED 
APPENDIX EXISTENCE ANALYSIS 359 
where the minimization above is assumed to be componentwise. By this we 
mean that the scalar I and the column vector h = (hl,  h 2 , .  . . , h,,)' E R" satisfy for each i = 1, 2, . . . , n, 
I + hi = min{ci(pi) + p i h } ,  
where p i h  denotes the inner product of the row vector p i  (ith row of the stochastic matrix P) and the column vector h, i.e., pih is the ith coordinate of the vector Ph. 
The problem described above is similar in nature to the one considered in the first three sections of this chapter. A control u is identified with its corresponding transition probability vector pi(u)  = Cpil(u), pi2(u), . . . , pi,(u)]. 
There is an important difference, however, in that while here the set of ad- missible probability vectors Di is assumed to be a closed convex set, in the problem considered earlier in the chapter the set of admissible controls U(i)  and hence also the set of corresponding probability vectors were assumed to be finite. In order to utilize the result of this appendix in proving Proposition 4 we shall need to construct a version of the problem of Sections 8.1-8.3. where randomization on the set of admissible controls V(i)  is allowed. 
Within the framework of the problem of Sections 8.1-8.3 let i be any 
state (i = 1,2,. . . , n) and let ul ,  u2,  . . ., umi denote the elements of the 
admissible control set V(i).  Consider the case where at each state i it is possible to select, instead of a control u E V(i),  a probability distribution q = (q l ,  q2, . . . ,qm' )  over the set U(i). Such a probability distribution will be referred to as a randomized control. The set of all randomized controls is denoted Qi.  If the current state is i and the randomized control q is selected, the prob- ability that the next state will be j is 
P, E D ,  
m, 
1 qrpiAur), j = 1,2, . . I , n, 
and the corresponding transition probability vector is 
r =  1 
m, m, m, 
= 1 qrpil(ur), 1 q r p i ~ u r ) ,  .. . 3  1 qrpin(ur)]* 
[r=l r=l  r =  1 
The set of all possible transition probability vectors as q ranges over Qi is denoted Di:  
Di = {Pi(q)Iq E Q i ) .  
The set Di is clearly the convex hull of the finite set of probability vectors 
360 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
and hence it is a closed convex set. With each state i and each probability vector p i  E D i ,  we associate a transition cost 
I qrpi(ur) = p i ,  q E Qi . 
The cost ci(pi) is the least possible expected transition cost associated with randomized controls q E Qi that result in a transition probability vector equal to p i .  From known facts of the theory of convex functions [R2] it follows that ci( ) as defined above is a polyhedral convex continuous function over the polyhedron D i .  In fact, ci is the convex hull [R2, p. 361 of the (extended real-valued function) Zi  defined by 
g(i, ur) if p i  = pi(ur), r = 1,. . . , mi, 
otherwise. E i ( p i )  = 
The extreme points of the epigraph [R2] of ci correspond to a subset of the 
finite set of points {pi(ul), . . . , pi(umi)} and the same is true for the extreme 
points of the epigraph of any function of the form ci(pi) + pih ,  where h is any vector in R" and p i h  denotes the inner product of p i  and h. 
Consider now the problem of this appendix with Di and ci(pi) defined as above and suppose that we are able to prove that (96) holds, i.e., 
I + hi = min{c,&i) + p i h } ,  i = 1,. . . , n. 
P i P D i  
Then in view of the construction of ci and Di the minimum on the right-hand side above will be attained at one (or possibly more) of the generating points 
pi(u'), pi(u2), . . . , pi(umi) of the set D i ,  which correspond to nonrandomized 
controls. As a result, in view of the definition of ci and Di we will have 
J 
n I ~ ( i ,  u )  + C pi,(u)hj , 
j =  1 
Thus the condition of Proposition 1 of Section 8.1 result of Proposition 4 will follow. Thus in order 
i = 1, ..., n. 
will be satisfied and the to prove Proposition 4 
it is sufficient to prove Eq. (96) within the generalized framework of this appendix. 
Consider now the nonlinear operator M :  Rn + R" defined by 
M x  = min{c + P x } ,  x E R" P E D  
(97) 
APPENDIX EXISTENCE ANALYSIS 361 
Define for all x = (xl, . . . , x,) E R", 
(1x11 = maxxi - minxj. (98) 
i e S  j s S  
Since IIx - yl( = 0 if and only if x and y differ by a multiple of the unit 
vector e = [l, 1, . . . , 11, (98) defines a norm on the collection of all subsets 
of R" elements of which differ by a multiple of the unit vector (i.e., 11 - 11 is a seminorm on R" and a norm on the corresponding quotient space of equiva- lence classes). Now suppose that some vector h E R" is a jxed  point of M in the sense that 
IIMh - hll = 0. (99) 
Then it follows that 
1e + h = Mh = min{c + Ph}, 
for some scalar 1. Hence proving (96) is equivalent to proving that there 
exists at least one fixed point of M in the sense of (99). 
We begin by deriving some useful properties of the operator M defined by (97). For any x E R" we define H(x) = max{xi(i E S}. Similarly we define L(x) = min{xi( i E S}. Then llxll = H(x) - L(x). We have the following 
lemma. 
P e D  
Lemma A.1 For any x, y E R" and a, f i  E R :  
(1) H(Mx - My) < H(x - y). (2) llMx - MYll < Ib - Yll. (3) IIM(a4 - M(Py)ll < lal  IIX - Yll + la - PI IIYII. 
Proof (1) Let P, Q E D be such that 
Mx = c(P) + Px and 
Then Mx < c(Q) + Qx and Mx - My < Q(x - y). Since Q is a stochastic matrix and x - y < H(x - y)e, we obtain Mx - My < H(x  - y)e from which H(Mx - My) < H(x - y). 
My = c(Q) + Qy. 
(2) We have 
I(Mx - My[) = H(Mx - My) + H ( M y  - M x )  
< H(x - y )  + H(y  - x) = Ilx - yll. 
(3) From part (2), IIM(ax) - M(Py)II < llax - PyII, and we have 
llax - PYll = I t +  - Y) + (a - BMI < lal IIX - yll + la - PI Ilyll, 
from which the result follows. Q.E.D. 
362 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Lemma A 3  Let (0,) be a nondecreasing sequence with 0 < 8, < 1. Consider the sequence { z ( k ) }  defined by 
z(k) = min{c + BkPz(k - l)}, 
P E D  
with z(0) = 0. Then { Ilz(k)l(} is a bounded sequence. 
Proof We recall that ci(Pi) is bounded for p i  E Di, i = 1, . . . , n. Since 
llz(k)ll cannot be affected by adding the same constant to every transition cost ci(pi), we may assume that for some p E R we have 0 < ci(pi) < B for all pi E D i ,  i = 1, . . . , n. Then it is easy to verify that {z (k) }  is a nondecreasing 
sequence, i.e., 
z(k + 1) 2 z(k), k = 0, 1,. . . , . (101) 
Now under the accessibility assumption there exists a stochastic matrix 
Q E D with elements qij, i, j = 1, . . . , n that defines an irreducible Markov 
chain, i.e., a chain for which every state communicates with every other state. This is a consequence of the accessibility assumption and the convexity of D, since we can arrange that 
qij > 0 if pij > 0 for some P E D, (102) 
by allowing P to participate in a convex combination forming Q .  Thus if P(i,j) E D is a stochastic matrix under whichj is accessible from i, the matrix 
Q = ( l/n2) I;= P(i, j) defines an irreducible Markov chain. We now 
associate with Q a set of mean transition times. For each pair of distinct states i , j  E S we denote by T~~ the expected number of steps required to reach j from i when Q is used as a stationary policy. Then, by considering the first step, we have 
qj = 1 + x q i l q j ,  i , j  = 1,. .., n, i z j. l # j  
Finally, prior to establishing the result of the lemma, we prove by induction that 
z i k )  < Bzij + zAk) Vi # j, k 2 0. (104) 
Indeed (104) holds for k = 0. Assume (104) holds for k = k. Since c(Q) < /3e and t& + < 1, we have 
z(k + 1) < c(Q) + &+ ,Qz(k) < fie + Qz(k). 
Thus 
zi(k + 1) < B + 1 qiIzl(k) + qijzjik). 
I # j  
APPENDIX EXISTENCE ANALYSIS 363 
Using (104) and then (103) we obtain 
Using (101) it follows that 
zi(k + 1) < p ~ i j  + z,{k + I), i.e., (104) is proved for k = k + 1 and the induction proof of (104) is complete. 
Now we easily obtain that the sequence {llz(k)ll} is bounded since (104) implies 
IIz(k)ll < max{pzijIi,j E S, i # j } .  Q.E.D. 
We are now in a position to prove the existence of a fixed point of M in the 
sense of (99) and hence that (96) holds for some 1 E R and h E R". Consider 
the sequence 
y(k) = min{c + (1 - (l/k))Py(k - l)}, 
y(0) = 0. 
k = 1 , 2 , .  .., P E D  
(105) 
Let also 
y(k) = y(k) - LLy(k)]e, k = 0, 1, . . . , (106) 
where LLy(k)] = min{yi(k)I i E S}. Then LW(k)] = 0, 11 jj(k)(I = maxiEs ji(k), and 
0 < y"iW < Ilflk)ll = IlY(k)ll. (107) The sequence { Ily(k)ll} is bounded by Lemma A.2, and by (107) the sequences 
{qi(k)}, i = 1, . . . , n, are also bounded. 
Proposition The sequence {$(k)} has a limit point h E R" such that 
llMh - h(l = 0. Hence there exists a scalar 1 such that 
b + h = Mh = min{c + Ph}. P E D  
Proof As explained above, each sequence {j$(k)}, i = 1,. . ., n, is bounded and hence there exists a convergent subsequence of {y (k) } .  Let 
h = lim j7(kr), r+w 
where { j j ( (k , )}  is the convergent subsequence. We also have, in view of (106), that 
lim Ilh - flkr)ll = 0. 
r-tm 
364 8 MINIMIZATION OF AVERAGE EXPECTED VALUE 
Now by using part (3) of Lemma A.1 we have 
Let B be a bound for IIy(k)ll, i.e., IIy(k)ll < B for all k. Then (109) implies that 
Combining (1 11) and (1 12) we obtain 
B 
IlMh - hll < I I f lkr+ l )  - flkr)ll + 2llflk) - hll + -9 
and taking the limit as r -, 00 and using (110) we obtain J JMh - hJJ = 0, 
Q.E.D. 
and hence IIy(k + 1) - y(k)JJ + 0 as k + 00. Hence 
(1 10) 
(111) 
We have for the vector h of (108) that 
IIMh - hI/ < IIMh - jj(k + 1111 + IIfikr + 1) - fikr)II + IIjj(kr) - hll. 
By using part (3) of Lemma A. l  and (106) we obtain 
 i  
i   )  i   JJ . . . . 
Appendixes 
This page intentionally left blank
Appendix A 
Mathematical Review 
The purpose of this and the following appendixes is to provide a list of mathematical and probabilistic definitions, notations, relations, and results that are used frequently in the text. For detailed expositions the reader may consult the references listed in each appendix. 
A.1 Sets 
If x is a member of the set S, we write x E S. We write x 4 S if x is not a member of S. A set S may be specified by listing its elements within braces. 
For example, by writing S = {xl, x2, . . . , x,} we mean that the set S consists 
of the elements xl , .  . . , x,. A set S may also be specified in the form 
S = {XlP(X)} as the set of elements satisfying property P. For example, 
S = { x l x : r e a l , O < x <  1) 
denotes the set of all real numbers x satisfying 0 < x < 1. The union of two sets S and T is denoted by S v T and the intersection of 
S and T is denoted by S n T. The union and intersection of a sequence of 
367 
368 A MATHEMATICAL REVIEW 
sets S , ,  S2, . . . , S k ,  . . . is denoted by Sk and nkrn,' sk, respectively. If 
S is a subset of T, i.e., if every element of S is also an element of T, we write S c T or T 3  S. 
Finite and Countable Sets 
A set S is said to be jinite if it consists of a finite number of elements. It is said to be countable if one can associate with each element of S a nonnegative integer in a way that to each pair of distinct elements of S there correspond two distinct integers. Thus according to our definition a finite set is also countable but not conversely. A countable set S that is not finite may be represented by listing its elements xo, xl ,  x 2 , .  . . , i.e., S = {xo, xl, x 2 , .  . .}. 
If A = { a o ,  a l ,  . . .} is a countable set and S,,, S,,, . . . are each countable sets, then the union uF=o S,, (otherwise denoted U P E A  S,) is also a countable set. 
Sets of Real Numbers 
If a and b are real numbers or + 00, - co, we denote by [a ,  b ]  the set of 
numbers x satisfying a < x < b (including the possibility x = +co, or 
x = -a). A rounded, instead of square, bracket denotes strict inequality 
in the definition. Thus (a,  b ] ,  [a,  b), and (a, b )  denote the set of all x satisfying a < x < b, a < x < b, and a < x < b, respectively. 
If S is a set of real numbers bounded above, then there is a smallest real number y such that x < y for all x E S. This number is called the least upper bound or supremum of S and is denoted sup{x I x E S}. Similarly the greatest real number z such that z < x for all x E S is called the greatest lower bound or injimum of S and is denoted inf{x Ix E S}. If S is unbounded above, we write sup{xIx~S}  = +co and if it is unbounded below, inf{xIxES} = -a. 
If S is the empty set, then by convention we write inf{xlx ES} = +co and sup{xIxES} = -a. 
A.2 Euclidean Space 
The set of all n-tuples x = (xl, . . . , x,) where xl, . . . , x, are real numbers 
constitutes the n-dimensional Euclidean space denoted R". The elements of R" are referred to as n-dimensional vectors or simply vectors when confusion cannot arise. The one-dimensional Euclidean space R' consists of all the real numbers and is denoted R. Vectors in R" can be added by adding their cor- responding components. They can be multiplied by a scalar by multiplication of each component by the scalar. The inner product (or scalar product) of two vectors x = (xl , .  . . , x,), y = kl, .  . ., y,) is denoted x'y and is equal to 
A.3 MATRICES 369 
x i y i .  The norm of a vector x = ( x l ,  . . . , x,) E R" is denoted IJxIJ and is 
A set of vectors a l ,  a 2 ,  . . . , ak is said to be linearly dependent if there exist 
Aiai = 0. If no such set of 
equal to (x'x)'/' = (I;  xZ)l/'. 
scalars A l ,  A 2 ,  . . . , A,', not all zero, such that 
scalars exists, the vectors are said to be linearly independent. 
A.3 Matrices 
An m x n matrix is a rectangular array of numbers, called elements, ar- ranged in m rows and n columns. The element in the ith row andjth column of a matrix A is denoted by a subscript ij, such as a i j ,  in which case we write A = [a i j ] .  A square matrix (one with m = n )  with elements aij  = 0 for i # j and aii  = 1, for i = 1, . . . , n, is said to be an identity matrix. The sum of 
two m x n matrices A and B is written as A + B and is the matrix whose elements are the sum of the corresponding elements in A and B. The product o f a  matrix A and a scalar A, written as AA or AA, is obtained by multiplying each element of A by A. The product AB of an m x n matrix A and an n x p matrix B is the m x p matrix C with elements ci j  = c;=l aikbkj .  If b is an 
n x 1 matrix, i.e., an n-dimensional column vector, and A is an m x n matrix, then A b  is an m-dimensional (column) vector. 
The transpose of an m x n matrix A is the n x m matrix A' with elements aij = a j i .  A square matrix A is symmetric if A' = A .  A square n x n matrix A is nonsingular if there is an n x n matrix called the inverse of A ,  denoted by A -  such that A - ' A  = I = A A - ' ,  where I is the n x n identity matrix. A square n x n matrix A is nonsingular if and only if the n vectors that constitute its rows are linearly independent or equivalently if the n vectors that constitute its columns are linearly independent. 
Partitioned Matrices 
It is often convenient to partition a matrix into submatrices by drawing partitioning lines through the matrix. For example, the matrix 
a l l  a 1 2  a 1 3  a14 I 
- 1 -  - - - - 
a31 a 3 2  I a 3 3  a34 
may be partitioned into 
A = [ : : :  :;I 
370 
where 
A MATHEMATICAL REVIEW 
A11 = Call a1219 A12 = [a13 a1419 
For a partitioned matrix A = [ B  I C] we use interchangeably the notation [B, C ]  or [ B C ] .  The transpose of the partitioned matrix A above is 
Partitioned matrices may be multiplied just as nonpartitioned matrices provided the dimensions involved in the partitions are compatible. Thus if 
then 
AllBll + A12B21 Al l&,  + A12B22 A21Bll + A22B21 AZlBl2 + A22B22 
AB = [ 
provided the dimensions of the submatrices are such that the products AijBjk, i , j ,  k = 1 , 2  above can be formed. 
Rank of a Matrix 
The rank of a matrix A is equal to the maximum number of linearly independent row vectors of A. It is also equal to the maximum number of linearly independent column vectors. An m x n matrix is said to be of full rank if the rank of A is equal to the minimum of m and n. A square matrix is of full rank if and only if it is invertible (i.e., nonsingular). 
Positive Definite and Semidejnite Matrices 
A square symmetric n x n matrix A is said to be positive semidefinite if x'Ax 2 0 for all x E R". It is said to be positive definite if x'Ax > 0 for all nonzero x E R". The matrix A is said to be negative semidefinite (definite) if ( - A )  is positive semidefinite (definite). 
A positive (negative) definite matrix is invertible and its inverse is also positive (negative) definite. Conversely, an invertible positive (negative) semidefinite matrix is positive (negative) definite. If A and B are n x n positive semidefinite (definite) matrices, then the matrix 1A + p B  is also 
positive semidefinite (definite) for all 1 > 0 and p > 0. If A is an n x n 
positive semidefinite matrix and C is an m x n matrix, then the matrix CAC' 
A.4 TOPOLOGICAL CONCEPTS IN R" 37 1 
is positive semidefinite. If A is positive definite, C has full rank, and m < n, then CAC' is positive definite. 
An n x n positive definite matrix A can be written as CC' where C is a square invertible matrix. If A is positive semidefinite and its rank is m, then it can be written CC'. where C is an n x m matrix of full rank. 
Matrix Inversion Formulas 
The following formulas expressing the inverses of various matrices are often very useful. Let A and B be square invertible matrices and C be a matrix of appropriate dimension. Then, if all the inverses below exist, 
( A  + CBC')-' = A-'  - A-'C(B-'  + C'A-'C)- 'C'A-' .  
The equation can be verified by multiplying the right-hand side by A + CBC' and showing that the product is the identity matrix. 
Consider a partitioned matrix M of the form 
M = [ A  C D '  "1 Then we have 
-QBD-' t---------- 
-D-~CQ I D-' + D - ~ C Q B D - '  
where 
Q = ( A  - BD-'C)- ' ,  
provided the matrices D and Q are invertible. The proof is obtained by multiplying M with the expression for M - '  given above and verifying that the product yields the identity matrix. 
A.4 Topological Concepts in R" 
Convergence of Sequences 
A sequence of vectors x o ,  xl,. . . , x k , .  . . in R", denoted {x , } ,  is said to 
converge to a limit vector x if JIx, - x I I  + 0 as k + co (that is, if given E > 0, there is an N such that for all k 2 N we have llx, - X I [  c E). If {x,} converges 
to x, we write x ,  + x or lim,+m x, = x. As can be easily verified we have Ax, + By, + A x  + By if x, + x, y ,  + y ,  and A,  B are matrices of appropriate 
dimension. 
372 A MATHEMATICAL REVIEW 
A point x is said to be a limit point of a sequence {xk} if there is a subse- quence of {xk}  that converges to x, i.e., if there is an infinite subset K of the nonnegative integers such that { X k } k s K  converges to x. 
A sequence of real numbers {rk}  that is monotonically nondecreasing (nonincreasing), i.e., satisfies rk < rk+ (rk 2 rk+ 1) for all k, must either con- verge to a real number or be unbounded above (belowk in which case we write 1imk,, rk = + 00 ( -  00). Given any bounded sequence of real numbers { T k }  we may consider the sequence {sk}, where s k  = sup{ri I i 2 k } .  Since this sequence is monotonically nonincreasing and bounded it must have a limit called the limit superior of { r k }  and denoted lim rk .  We define similarly the limit inferior of {rk}  and denote it lim inf,,, rk.  If {rk}  is unbounded above, we write lim SUPk+m rk = + 00 and if it is unbounded below, we write 
lim inf,,, rt = -a. We also use this notation if rt E [ - XI, XI] for all k. 
Open, Closed, and Compact Sets 
A subset S of R" is said to be open if for every point x E S one can find an 
E > 0 such that {z I IJz - X I [  < E }  c S. A set S is closed if and only if its comple- 
ment in R" is open. Equivalently S is closed if and only if every convergent sequence {xk}  with elements in S converges to a point that also belongs to S. A set S is said to be compact if and only if it is both closed and bounded (i.e., it is closed and for some M > 0 we have llxll < M for all x E S). A set S is compact if and only if every sequence {xk}  with elements in S has at least one limit point that belongs to S. Another important fact is that if S o ,  S1,. . . , s k ,  . . . is a sequence of nonempty compact sets in R" such that 
Sk 3 S k +  for all k, then the intersection S k  is a nonempty and compact set. 
Continuous Functions 
A function f mapping a set S1 into a set S2 is denoted by f: S1 + S2 .  A function f : R" + R" is said to be continuous iff ( x k )  + f (x) whenever xk + x. 
Equivalently .f' is continuous if given x E R" and E > 0, there is a 6 > 0 such 
that whenever jly - xII -= 6 we have II,f(y) - f(x)ll < E.  The function 
is continuous for any two scalars al ,  a2 and any two continuous functions fl, fz:  R" --* R". If S1, S2,  S3 are any sets and fl:Sl + S 2 ,  f z : S 2  + S ,  are functions, the function fz . fl : S1 + S3 defined by ( fz fl)(x) = fz[ fl(x)] is called the composition of fl and fz . If fl : R" --* R" and f2 : R" + RP are con- 
tinuous, then fz . fl is also continuous. 
A S  CONVEX SETS AND FUNCTIONS 373 
A.5 Convex Sets and Functions 
A subset C of R" is said to be convex if for every xl ,  x2 E C and every 
scalar u with 0 Q u Q 1 we have ax, + (1 - u)x2 E C. In words, C is convex if 
the line segment connecting any two points in C belongs to C. A function f :  C + R defined over a convex subset C of R" is said to be conuex if for every 
xl, x2 E C and every scalar u with 0 Q u Q 1 we have 
fCux1 + (1 - 4x21 G C!f(Xl) + (1 - aIf(x2). 
The function f is said to be concaue if (-1) is convex. Iff: C -+ R is convex, 
then the sets rA = {x I x E C,  f(x) Q A} are also convex for every scalar A. An important property is that a real-valued convex function on R" is always a continuous function. 
Iff,,f2,. . . , f, are convex functions over a convex subset C of R" and 
ul ,  u2, . . . , a, are nonnegative scalars, then the function alfi + . . . + urn fm is also convex over C. Iff: R" + R is convex, A is an m x n matrix, and b is a vector in R", the function g: R" + R defined by g(x) = f(Ax + b) is also 
convex. I f f :  R" + R is convex, then the function g(x) = E ,  {f(x + w ) } ,  
where w is a random vector in R", is a convex function provided the expected value is well defined and finite for every x E R". 
For functions f :  R" -, R that are differentiable there are alternative 
characterizations of convexity. Thus if Vf(x) denotes the gradient offat x, i.e., 
Vf(x) = [af(x)/dx', . .., af(x)/ax"]', the functionfis convex if and only if 
f(y) 2 f(x) + Vf(x)'(y - x), for all x, y E R". 
If V2f(x) denotes the Hessian matrix offat x, i.e., the matrix 
V2f(X) = [d2f(x)/dx' ax'] 
the elements of which are the second derivatives offat x, thenfis convex if and only if Vzf(x) is a positive semidefinite matrix for every x E R". For detailed expositions see references [H6], [HlO], and [R6]. 
Appendix B 
On Optimization Theory 
Given a real-valued function f :  S + R defined on a set S and a subset 
X c S, by the optimization problem 
minimize f(x) subject to x E X, 
we mean the problem of finding an element x* E X (called a minimizing ele- ment or an optimal solution) such that 
f ( x * )  ,< f ( x )  vx EX. 
Such an element need not exist. For example, the scalar functionsf(x) = x andf(x) = ex have no minimizing elements over the set of real numbers. The 
first function decreases without bound to - 00 as x tends toward - co while 
the second decreases toward 0 as x tends toward -co but always takes positive values. Given the range of values thatf(x) takes as x ranges over X, i.e., the set of real numbers 
{f(x)lx E XI there are two possibilities: 
(a) The set { f ( x )  Ix E X} is unbounded below (i.e., contains arbitrarily 
374 
B ON OPTIMIZATION THEORY 375 
small real numbers) in which case we write 
inf{f(x)IxEX} = -a or inff(x) = -a. 
X E X  
(b) The set {.f(x)lx E X} is bounded below, i.e., there exists a scalar M such that M < f(x) for all x E X. The greatest lower bound of { f ( x ) I x  E X} we denote by 
inf {f(x) I x E X} or inf f(x). x e X  
In either case we call infxEx f(x) the optimal value of problem (B.1). If a minimizing element x* exists, then 
f(x*) = inff(x), X E X  
in which case we also write 
f(x*) = minf(x) = inff(x), x e x  X E X  
and use the notations minxExf(x) and infxEx f(x) for the optimal value inter- changeably. 
A maximization problem of the form 
maximize f(x) subject to x E X, 
may be converted into the minimization problem 
minimize -f(x) subject to x E X, 
in the sense that both problems above have the same optimal solutions and the optimal value of one is equal to minus the optimal value of the other. This optimal value for the maximization problem is denoted supxEx f(x). When a maximizing element is known to exist we also write interchangeably 
maxx E x f(4. 
Existence of Optimal Solutions 
We are often interested in verifying the existence of at least one minimizing element in problem (B.1). Such an element clearly exists when X is a finite set. When X is not finite the existence of a minimizing point in problem (B.l) is guaranteed iff: R" -+ R is a continuous function and X is a compact subset of R". This is the Weierstrass theorem. By a related result existence of a minimizing point is guaranteed iff: R" -+ R is a continuous function, X = R" 
andf(x) -+ +a if llxll -+ +a. 
376 B ON OPTIMIZATION THEORY 
Necessary and SufJicient Conditions for Optimality 
Such conditions are available when f is a differentiable function on R" and X is a convex subset of R" (possibly X = R"). Thus if x* is a minimizing 
point in problem (B.l), f: R" + R is a continuously differentiable function on 
R" and X is convex we have 
Vf (x*)'(x - x*) 3 0 vx E x, (B.2) 
where Vf (x*) denotes the gradient off at x*. When X = R", i.e., the minimiza- tion is unconstrained, the necessary condition (B.2) is equivalent to the familiar condition 
Vf  (x*)  = 0. 03.3) 
When f is in addition twice continuously differentiable and X = R", an additional necessary condition is that the Hessian matrix V2f  (x*)  is positive semidejnite at x*. An important fact is that i f f :  R" + R is a conuex function 
and X is convex, then (B.2) is both a necessary and a sufJicient condition for optimality of a point x*. 
Minimization of Quadratic Forms 
Let f: R" + R be a quadratic form 
f ( x )  = ~ x ' Q x  + b'x, 
where Q is a symmetric n x n matrix and b E R". If Q is a positive definite matrix, thenfis a convex function. Its gradient is given by 
V f ( x )  = QX + b. 
By (B.3), a point x* is a minimizing point off if and only if 
Vf  (x*) = Qx* + b = 0, 
which yields x* = -Q-'b. 
For detailed expositions see references [A2], [LlO], and [Zl]. 
Appendix C 
On Probability Theory 
This appendix lists selectively some of the basic probabilistic notions we shall be using. Its main purpose is to familiarize the reader with some of the terminology we shall adopt. It is not meant to be exhaustive and the reader should consult references [A8], [Fl], [P2], and [P3] for detailed treatments particularly regarding operations with random variables, conditional prob- ability, Bayes’ rule, etc. For an excellent recent treatment of measure theoretic probability theory see the textbook by R. B. Ash, “Real Analysis and Prob- ability,” Academic Press, 1972. 
Probability Space 
A probability space consists of 
(a) a set R, (b) a collection 9 o f  subsets of R, called events, which includes R and has 
the following properties: 
(1) If A is an event, then the complement 1 = {w E Rlo $ A} is also an event. (The complement of R is the empty set and is considered to be an event.) 
(2) If A,, A2 are events, then A l  n A 2 ,  A l  u A2 are also events. 
377 
378 c ON PROBABILITY THEORY 
(3) If A,, A , ,  . . . , Ak, . . . are events, then u ~ =  , Akand np' , A ,  are also 
events. 
(c) a function P( * ) assigning to each event A a real number P(A), called the probability of the event A ,  and satisfying 
(1) P(A)  2 0 for every event A. (2) P(R)  = 1. ( 3 )  P (A  , u A,)  = P(A ,) + P(A,)  for every pair of disjoint events A ,, A , .  
(4) ~ ( U k m , ~  A )  = P(&) for every sequence of mutually disjoint 
events A l ,  A,, . . . , A k ,  . . . . 
The function P is referred to as a probability measure. 
Convention for Finite and Countable Probability Spaces 
The case of a probability space where the set R is a countable (possibly finite) set is encountered frequently in this text. Where we specify that R is finite or countable we implicitly assume that the associated collection of events is the collection of all subsets of R (including R and the empty set). Under these circumstances the probability of all events is specified by the probability of the elements of R (i.e., of the events consisting of single elements in R). Thus if R is a finite set R = {w, ,  a,, . . . , a,,}, the probability space is specified by 
the probabilities p , ,  p , ,  . . . , p,,, where pi denotes the probability of the event 
consisting of mi above. Similarly if R = {a1, w,,  . . . , wk, . . .}, the probability 
space is specified by the corresponding probabilities p , ,  p , ,  . . . , P k ,  . . . . In either case we refer to (PI, p , ,  . . . , p,) or (p,, p , ,  . . . , P k ,  . . .) as a probability 
distribution over R. 
Random Variables 
space is a function x : R -+ R such that for every scalar. ,I the set 
Given a probability space (R, E P), a random variable on the probability 
{OERlX(O) d A} is an event, i.e., belongs to the collection F. 
variables xl, x2 , .  . . , x, each defined on the same probability space. 
random variable x is defined by 
An n-dimensional random vector x = (xl, . . . , x,) is an n-tuple of random 
The distribution function (or cumulative distribution function) F :  R -+ R of a 
F(z) = P({o  E Rlx(w) d z} ) ,  
i.e., F(z) is equal to the probability that the random variable takes a value less than or equal to z. 
c ON PROBABILITY THEORY 379 
The distribution function F : R" + R of a random vector x = ( x l ,  x2,.  . . , 
x,) is defined by 
F ( ~ ~ , ~ Z ~ . . . , ~ , ) = ~ ( { ~ ~ ~ I ~ ~ ( ~ ) ~ ~ ~ ~ X ~ ( ~ ) ~ Z ~ , . . . ~ X , ( ~ ) ~ Z ~ } ) .  
Given the distribution function of a random vector x = ( x l ,  . . . , x,) the 
(marginal) distribution function of each random variable xi is obtained from 
Fi(zi) = lim F(zl, z 2 ,  . . . , z,). 
z, + m. j #  i 
The random variables x l ,  . . . , x,  are said to be independent if 
F(z1, . . * , zn) = Fl(z1). F 2 ( ~ 2 )  . . . Fn(zA7 
for all scalars z l r  . . . , z,. 
is defined as The expected value of a random variable x with distribution function F 
m 
E b} = S_,z d F ( z )  
provided the integral above is well defined. The expected value of a random vector x = ( x l , .  . . , x,) is the vector 
The covariance matrix of a random vector x = (xl, . . . , x,) with expected 
value E { x }  = (al , .  . , a,) is defined to be the n x n symmetric positive semidefinite matrix 
E { x )  = ( E { x d ,  E(x217 .. * 9 E{xnJ)- 
1 E { ( x ~  - ~ 1 ) ' )  * * *  E { ( x ~  - X ~ ) ( X ,  - X,) 
Q x =  [ 
E {(x,  - X , ) ( X ~  - %I)} . * . E {(xn - Q2} 
provided the expectations above are well defined. Two random vectors x and y are said to be uncorrelated if 
where ( x  - E { x ) )  above is viewed as a column vector and ( y  - E{y)) '  is 
viewed as a row vector. 
The random vector x = (xl, .. . ,x , )  is said to be characterized by a piecewise continuous probability density function f :  R" + R iff is piecewise 
continuous and 
F(z1,. . . , z,) = f' f z  . . . sI,f 0 1 1 7 .  a *  7 Y n )  dY1*  * .dyn, 
- m  - m  
for every z l ,  . . . , z ,  . 
380 c ON PROBABILITY THEORY 
Conditional Probability 
We shall restrict ourselves to the case where the underlying probability space R is a countable (possibly finite) set and the set of events is the set of all subsets of R. 
Given two events A and B we define the conditional probability of Bgiven A by 
P(A n B)/P(A)  if P(A) > 0, 
if P(A)  = 0. P(BIA) = 
If B,, B,, . . . are a countable (possibly finite) collection of mutually exclusive and exhaustive events (i.e., the sets Bi are disjoint and their union is R) and A is an event, then we have 
i 
From this one may prove that 
P(A)  = 1 P(Bi)P(A 1 Bi). 
This is called the theorem of total probability. From the expressions above we obtain for every k 
i 
P(Bk I A )  = P(A Bk)/P(A) = P(Bk)P(A I B k ) / c i  P ( B i ) P ( A  I B i ) ,  
provided P(A) > 0. The relation above is referred to as Bayes' rule. Consider now two random vectors x and y on the (countable) probability 
space taking values in R" and R", respectively [i.e., x(w) E R". y ( o )  E R" for all w E R]. Given two subsets X and Y of R" and R", respectively, we denote 
P(X  I Y )  = P ( { o  I x ( 4  E x> I (0 I Y(W)  E Y } ) .  
For a fixed vector w E R" we define the conditional distribution function of x given w by 
f l z  I w )  = P({w I x ( w )  G z> I {w I Y ( 4  = w } ) ,  
and the conditional expectation of x given w by 
E ( X I W 1  = z W z I w ) ,  JR" 
provided the integral above is well defined. Note that E { x  I w }  is a function mapping w into R". Similarly one may define the conditional covariance of x given w ,  etc. 
If w,,  w,, . . . are the elements of R, let us denote 
zi = x(wi),  wi = y ( o i ) ,  i = 1, 2, . . . . 
c ON PROBABILITY THEORY 381 
Also for any vectors z E R", w E R", let us denote 
P(z )  = P((OlX(0)  = z } ) ,  P(w)  = P ( { o ( y ( w )  = w}). 
WehaveP(z) = Oifz # z i , i  = 1,2  ,..., andP(w) = Oifw # w i , i  = 1,2  ,.... Denote also 
P(zIw) = P({wIx(w) = z}I{wIy(4 = wl).  
Then if P(w) > 0, Bayes' rule yields 
P(Z, I w) = P(Z~)P(W I z i ) / C j ~ ( z j ) ~ ( w / z j ) ,  i = 1, 2. . . . . 
P(z1w) = 0 if z # z i ,  i = 1 ,2  ,..., 
where P(w/z)  = P({o/y(w)  = w}  I ( w l x ( w )  = 2 ) ) .  
Appendix D 
On Finite State Markov Chains 
A square n x n matrix Cpij] is said to be a stochastic matrix if all its ele- ments are nonnegative, i.e., p i j  2 0, i ,  j = 1, . . . , n, and the sum of the elements 
of each of its rows equals unity, i.e., 
Stationary Finite State Markov Chains 
Suppose we are given a stochastic n x n matrix P together with a finite 
set S = { sl, . . . , s"} called the state space with elements sl, . . . , S" called 
states. The pair ( S ,  P )  will be referred to as a stationaryjnite state Markov chain. We associate with (S, P )  a process whereby an initial state xo E S is chosen in accordance with some initial probability distribution 
p i j  = 1 for all j = 1, . . . , n. 
Subsequently a transition is made from state xo to a new state x1 E S  in accordance with a probability distribution specified by P as follows. The probability that the new state x 1  will be si is equal to p i j  whenever the initial state x o  is si, i.e., 
P ( X ,  = sjlxo = si) = p i j ,  i , j  = 1, .. ., n. 
382 
D ON FINITE STATE MARKOV CHAINS 383 
Similarly subsequent transitions produce states x 2 ,  x 3 ,  . . . in accordance with 
(D.1) P(xk+ l  = sjlxk = si) = p i j ,  i, j = 1,. . . , n. 
The probability that after the kth transition the state xk will be equal to s j  given that the initial state x o  is equal to si is denoted 
pfj = P(xk = sj lxo = si), i , j  = 1, ..., n. P.2) These probabilities may be easily calculated to be equal to the elements of the matrix Pk (P raised to the kth power), in the sense that pfj is the element in the ith row and jth column of Pk: 
Pk = C p f j ] .  (D.3) Given the initial probability distribution p o  of the state x o  (viewed as a row vector in R”), the probability distribution of the state xk after k transitions 
Pk = bl, pkz, * * . 9 p i )  
(viewed again as a row vector) is given by 
pk = p o p k ,  k = 1,2, .... 03.4) 
This relation follows immediately from (D.2) and (D.3) once we write n n 
p’k = c P ( x k  = S j l X O  = si)pb = x p f j p b .  i =  1 i =  1 
Nonstationary Finite State Markov Chains 
Suppose we are given instead of a single stochastic matrix P a sequence {Pk} of stochastic n x n matrices Po,  P1, . . . . We refer to the pair (S, {Pk}) as a nonstationaryjnite state Markov chain and we associate with it the following process. The initial state x o  E S is chosen in accordance with an initial dis- tribution p o  = (p:, p i ,  . . . , p;).  Subsequently a transition is made to a state 
x t  E S in accordance with 
P ( x l  = sj lxo = si)  = pi,{0), i, j = 1, . . . , n, 
where pi,(0) is the element in the ith row and jth column of the stochastic matrix Po (Po = CpijO)]). Subsequent transitions produce states in accordance with 
P ( x k + l  = S j l X k  = Si) = pijk), i , j  = 1, ..., n, where pijk)is the element in the ith row and jth column of Pk. The probabilities 
pfj = P(xk = sj lxo = si), i, j = 1, . . . , n, 
384 D ON FINITE STATE MARKOV CHAINS 
can be calculated to be equal to the elements of the matrix P O P ,  . . . P k -  : 
POPI " ' p k - 1  = [&I. Given the initial probability distribution p o  of the state xo the probability distribution Pk = ( p i ,  . . . , p i )  of xk is given by 
Pk=PoPoP1".Pk-1, k = l , 2  , . . . .  
We subsequently restrict ourselves to stationary Markov chains. 
Classijication of States of a Markov Chain 
Given a stationary finite state Markov chain ( S ,  P )  we say that two states x i  and xi communicate if there exist two positive integers k ,  and k 2  such that p$ > 0 and psi > 0. This definition does not exclude the possibility of a state communicating with itself. 
Let s" c S be a subset of states such that: 
(a) All states in s" communicate with each other. 
(b) If si E s and sj  $3, then p f j  = 0 for all k .  
Then we say that s" forms an ergodic class of states. If S forms by itself an ergodic class (i.e., all states communicate with each 
other), then we say that the Markov chain is irreducible. It is possible that there exist several ergodic classes. It is also possible to prove that at least one ergodic class must exist. States that do not belong to any ergodic class are called transient. Transient states are characterized by the fact that 
lim pfi = 0 if and only if si is transient. k + m  
In other words, if the process starts at a transient state the probability of returning to the same state after k transitions diminishes to zero as k tends to infinity. 
It is easy to see from the definitions given that during the process of tran- sition between states once an ergodic class is entered then the process remains within this ergodic class for every subsequent transition. Thus if the process starts within an ergodic class, it stays within that class. If it starts at a transient state, it eventually (with probability one) enters an ergodic class after a number of transitions and subsequently remains there. 
Limiting Probabilities 
defined by An important property of any stochastic matrix P is that the matrix P* 
N- 1 
D ON FINITE STATE MARKOV CHAINS 385 
exists [in the sense that the sequences of the elements of ( 1 / N )  1:; Pk con- 
verge to the corresponding elements of P*]. The elements p$  of P* satisfy 
n 
~ $ 2 0 ,  C p $ = l ,  i = l ,  ..., n, j =  1 
i.e., P* is a stochastic matrix. 
such that sk E s, 
If s c S is an ergodic class and si, s j  E 5, then it may be proved that for all k 
P 2  = P$ > 0, so that $a Markov chain is irreducible, the matrix P* has identical rows. Also if sJ is a transient state, we have 
p . .  - 0 ViES,  
so that the columns of the matrix P* corresponding to transient states are identically zero. 
First Passage Times 
after exactly k 2 1 transitions given that the initial state is si, i.e., Let us denote by qfj  the probability that the state will be s j  for the first time 
q f j  = P(xk = Sj ,  X ,  # SJ, 1 < m < k I X o  = Si). 
Denote also for fixed i and j ,  
K , ~  = min{k 2 1 Ixk = sj ,  xo = si}. 
Then K, , ,  called the jirst passage time from i toj ,  may be viewed as a random variable. We have for every k = 1,2, . . . , 
P(K. .  = k )  = qk. IJ IJ ’  
and we write W 
P(K,, = CO) = P(xk # Sj,  Vk = 1 ,  2,. . . I X g  = Si) = 1 - 1 qfj .  
k =  1 
Of course, it is possible that qf, < 1. This will occur, for example, if 
si cannot be reached from si in which case qf, = 0 for all k = 1, 2, . . . . The 
meanjirst passage time from i to j is the expected value of Kij: 
if l q f j  -= 1. k =  1 
386 D ON FINITE STATE MARKOV CHAINS 
It may be proved that if si and sj  belong to the same ergodic class, then 
E { K i j }  < co. 
Ifs'andsjbelongtotwodifferentergodicclasses,then E { K i j }  = E { K j i }  = 00. 
If si belongs to an ergodic class and sJ is transient, we have E { K i j }  = 00. 
Interpretation of Accessibility Conditions 
sk E S such that In Chapter 8 we utilized the condition that there exists a special state 
E { K i k }  < 00 VS' E S .  (D.5) Now in view of the preceding discussion the state sk cannot be transient and thus it must belong to an ergodic class. Furthermore, there cannot be more than one ergodic class since if some state sJ belonged to a different ergodic class than the one of sk we would have E{Kjk} = co. Thus there must exist a single ergodic class and sk must belong to it. Conversely, condition (D.5) always holds when a single ergodic class exists and sk belongs to it. In con- clusion assuming existence of a state sk such that (D.5) holds is equivalent to assuming the existence of a single ergodic class. 
Assume now that we have a collection of n x n transition probability matrices P ( p )  parameterized by the elements p of some set M. Let us denote by E {Ki@)} the mean first passage time for going from si to s j  when the transition probability matrix is P(p) .  Then clearly from the discussion given earlier it follows that the condition 
there exists sk E S such that E {Kik(,u)} < 0 for all si E S ,  p E M ,  
is equivalent to assuming that, for every p, P(p)  gives rise to a Markov chain with a single ergodic class and sk belongs to that class. In particular, the condition above is satisfied if the Markov chain corresponding to P(p)  is irreducible for every p E M. For detailed expositions see references [C3] and [K7]. 
Aoki, M., “Optimization of Stochastic Systems-Topics in Discrete-Time Systems.” Academic Press, New York, 1967. Aoki, M., “Introduction to Optimization Techniques.” Macmillan, New York, 1971. Aoki, M., and Li. M. T., Optimal discrete-time control systems with cost for obser- vation, IEEE Trans. Automatic Control AC-14 (1969), 165-175. Arrow, K. J., “Aspects of the Theory of Risk Bearing.” Yrjo Jahnsson Lecture Ser., Helsinki, Finland, 1965. Arrow, K. M., Blackwell, D., and Girshick, M. A., Bayes and minimax solutions of sequential design problems, Econometrica 17 (1949), 213-244. Arrow, K. J., Harris, T., and Marschack, J., Optimal inventory policy, Economerrica 19 (1951), 250-272. Arrow, K. H., Karlin, S., and Scarf, H., “Studies in the Mathematical Theory of Inventory and Production.” Stanford Univ. Press, Stanford, California, 1958. Ash, R. B., “Basic Probability Theory.” Wiley, New York, 1970. Astrom, K. J., and Wittenmark, B., On self-tuning regulators, Automatica 9 (1973), 185-1 99. Atkinson, R. C., Bower, G .  H., and Crothers, E. J., “An Introduction to Mathematical Learning Theory.” Wiley, New York, 1965. Bar-Shalom, Y., and Tse, E., Dual effect, certainty equivalence, and separation in stochastic control, IEEE Trans. Automatic Control AC-19 (1974). 494500. Bather, J., Optimal decision procedures for finite Markov chains, Advances in Appl. Probability 5 (1973). 328-339, 521-540, 541-553. 
387 
388 REFERENCES 
[B23a] 
Bellman, R., “Dynamic Programming.” Princeton Univ. Press, Princeton, New Jersey, 1957. Bellman, R., and Dreyfus, S., “Applied Dynamic Programming.” Princeton Univ. Press, Princeton, New Jersey, 1962. Bertsekas, D.  P., On the separation theorem for linear systems, quadratic criteria, and correlated noise, unpubl. rep., Electronic Systems Lab., MIT, Cambridge, Massa- chusetts, September 1970. Bertsekas, D. P., “Control of Uncertain Systems with a Set-Membership Description of the Uncertainty.” Ph.D. Dissertation, MIT, Cambridge, Massachusetts, 1971. Bertsekas, D. P., Stochastic optimization problems with nondifferentiable cost functionals with an application in stochastic programming, Proc. IEEE Decision and Control Con$ New Orleans, Louisiana, December 1972. Bertsekas, D. P., On the solution of some minimax problems, Proc. IEEE Decision and Con trol ConJ New Orleans, Louisiana, December 1972. Bertsekas, D. P., Infinite time reachability of state space regions by using feedback control, IEEE Trans. Automatic Control AC-17 (1972), 604613. Bertsekas, D. P., “Stochastic optimization problems with nondifferentiable cost functionals, J. Optimization Theory Appl. 12 (1973), 218-231. Bertsekas, D. P., Linear convex stochastic control problems over an infinite time horizon, IEEE Trans. Automatic Control AC-18(1973), 314315. Bertsekas, D. P., Necessary and sufficient conditions for existence of an optimal portfolio, J. Econom. Theory 8 (1974), 235-247. Bertsekas, D. P., Monotone mappings with application in dynamic programming, Coordinated Sci. Lab. Working Paper, Univ. of Illinois, Urbana, Illinois, June 1976. SIAM J. Control and Optimization (to appear). Bertsekas, D. P., On error bounds for successive approximation methods, IEEE Trans. Automatic Control. AC-21 (1976), 394396. Bertsekas, D. P., Convergence of discretization procedures in dynamic programming, IEEE Trans. Automatic Control AC-20 (1975). 415419. Bertsekas, D. P., Monotone mappings in dynamic programming, Proc. IEEE Con$ Decision and Control, Houston, Texas, December 1975. Bertsekas, D. P., and Rhodes, I. B., On the minimax reachability of target sets and target tubes, Automatica 7 (1971), 233-247. Bertsekas, D. P., and Rhodes, I. B., Sufficiently informative functions and the minimax feedback control of uncertain dynamic systems, IEEE Trans. Automatic Control 
Blackwell, D., Discrete dynamic programming, Ann. Math. Statist. 33 (1962), 719-726. Blackwell, D., Discounted dynamic programming, Ann. Math. Statist. 36 (1965), 226235. Blackwell, D., Positive dynamic programming, Proc. 5th Berkeley Symp. Math., Statist., and Probability, 1 (1965), 415418. Blackwell, D., On stationary policies, J. Roy. Statist. SOC. Ser. A.  133 (1970). 33-38. Blackwell, D., and Girshick, M. A,, “Theory of Games and Statistical Decisions.” Wiley, New York, 1954. Blackwell, D., Freedman, D.. and Orkin, M., The optimal reward operator in dynamic programming, Ann. Prob. 2 (1974), 926941. Blake, I. F., and Thomas, J. B., On a class of processes arising in linear estimation theory, IEEE Trans. Information Theory IT-14 (1968), 12-16. Brown, B. W., On the iterative method of dynamic programming on a finite space discrete Markov process, Ann. Math. Statist. 36 (1965), 1279-1286. 
AC-18 (1973), 117-124. 
REFERENCES 389 
Cashman, W. F., and Wonham, W. M., A computational approach to optimal control of stochastic saturating systems, Internat. J. ConrrolIO (1969), 77-98. Chernoff, H., “Sequential Analysis and Optimal Design.” Regional Conference Series in Applied Mathematics, SIAM, Philadelphia, Pennsylvania, 1972. Chung, K. L., ‘’ Markov Chains with Stationary Transition Probabilities.” Springer- Verlag, Berlin and New York, 1960. Cooper, C. A,, and Nahi, N. E., An optimal stochastic control problem with obser- vation cost, Proc. Joint Automatic Control Con$ Atlanta, Georgia, June 1970. Curry, R. E., A new algorithm for suboptimal stochastic control, IEEE Trans. Auto- matic Control AC-12 (1967), 533-536. DeGroot, M. H., “Optimal Statistical Decisions.” McGraw-Hill, New York, 1970. Denardo, E. V., Contraction mappings in the theory underlying dynamic programming, SIAM Rev. 9 (1967), 165-177. D’Epenoux, F., Sur un probleme de production et de stockage dans I’aleatoire, Rev. 
Francaise Automat. Informat. Recherche Operationnelle, 14 (1960), (English Transl. : 
Management Sci. 10 (1963), 98-108). Derman, C., “Finite State Markovian Decision Processes.” Academic Press, New York, 1970. Deshpande, J. G., Upadhyay, T. N., and Lainiotis, D. G., Adaptive control of linear control systems, Automatica 9 (1973), 107-1 15. Dreyfus, S. E., “Dynamic Programming and the Calculus of Variations.” Academic Press, New York, 1965. Dreyfus, S. E.. and Stalford. H. L., A computational successive improvement scheme for adaptive optimal control processes, J .  Optimization Theory Appl. 10 (l972), 78-93. Dubins, L., and Savage, L. M., “How To Gamble I f  You Must.” McGraw-Hill, New York, 1965. Dynkin, E. B., Controlled random sequences, Theor. Probability Appl. 10 (1965), 1-14. Eaton, J. H. and Zadeh, L. A., Optimal pursuit strategies in discrete state probabilistic systems, Trans. ASME Ser. D .  J. Basic Eng. 84 (1962), 23-29. Eckles, J. E., Optimum maintenance with incomplete information, Operations Res. 16 (1968), 1058-1067. Feller, W., “An Introduction to Probability Theory and Its Applications,” 3rd ed. Wiley, New York, 1968. Fishburn, P. C., Utility theory, Management Sci. 14 (1968). 335-378. Fishburn, P. C., “Utility Theory for Decision Marking.” Wiley, New York, 1970. Freedman, D., The optimal reward operator in special classes of dynamic program- ming problems, Ann. Prob. 2 (1974), 942-949. Furukawa, N., A Markov decision process with nonstationary transition laws, Bull. Math. Statist. 13 (1968), 41-52. Groen, G. J., and Atkinson, R. C., Models for optimizing the learning process, Psychol. Bull. 66 (1966), 309-320. Gunckel,T. L., and Franklin, G. R., A general solution for linear sampled-data control, Trans. ASME Ser. D .  J .  Basic Engrg., 85 (1963). 197-201. Hakansson, N., Optimal investment and consumption strategies for a class of utility functions, Econometrica 38 (1970), 587407. Hakansson, N. H., Optimal investment and consumption strategies under risk, an uncertain lifetime, and insurance, Internat. Econom. Rev. 10 (1970). 443466. Hakansson, N., Multiperiod mean-variance analysis: toward a general theory of portfolio choice. J. Finance (l971), 857-884. 
REFERENCES 
Hakansson, N. H., On optimal myopic portfolio policies with and without serial correlation of yields, J. Business 44 (1971), 325-344. Halmos, P., “Measure Theory.” Van Nostrand-Reinhold, Princeton, New Jersey, 1950. Halmos, P., “ Finite-Dimensional Vector Spaces.” Van Nostrand-Reinhold, Princeton, New Jersey, 1958. Hastings, N. A. J., Some notes on dynamic programming and replacement, Operational Res. Quart. 19 (1968), 453464. Hastings, N. A. J., Bounds on the gain of a Markov decision process, Operations Res. 19 (1971), 240-243. Hinderer, K., “Foundations of Non-Stationary Dynamic Programming with Discrete Time Parameter.” Springer-Verlag, Berlin and New York, 1970. Hoffman, K., and Kunze, R., “Linear Algebra.” Prentice-Hall, Englewood Cliffs, New Jersey, 1961. Holt, C. C., Modigliani, F., and Simon, H. A,, A linear decision rule for production and employment scheduling, Management Sci. 2 (1955), 1-30. Hordijk, A., and Tijms, H., The method of successive approximations and Markovian decision problems, Operations Res. 22 (l974), 519-521. Hordijk, A,, and Tijms, H. C., Convergence results and approximations for optimal (s, S) policies, Management Sci. 20 (1974), 1432-1438. Hordijk, A., and Tijms, H. C., On a conjecture of Iglehart, Management Sci. 21 (1979, 1342-1345. Howard, R., “Dynamic Programming and Markov Processes.” MIT Press, Cambridge, Massachusetts, 1960. Howard, R., “Dynamic Probabilistic Systems,” Vols. I and 11. Wiley, New York, 1971. Howard, R., and Matheson, J., Risk-sensitive Markov decision processes, Manage- ment Sci. 18 (1972), 356-369. IEEE Trans. Automatic Control, special issue on Linear-Quadratic Gaussian Pioblem, 
Iglehart, D. L., Optimality of (S, s) policies in the infinite horizon dynamic inventory problem, Management Sci. 9 (1963), 259-267. Iglehart, D. L., Dynamic programming and stationary analysis of inventory problems, in Scarf, H., Gilford, D., and Shelly, M. (eds.), “Multistage Inventory Models and Techniques.” Stanford Univ. Press, Stanford, California, 1963. Jacobson, D. H., Optimal stochastic linear systems with exponential performance criteria and their relation to deterministic differential games, IEEE Trans. Automatic Control AC-18 (1973), 124-131. Jacobson, D. H., A general result in stochastic optimal control of nonlinear discrete- time systems with quadratic performance criteria, J. Math. Anal. Appl. 47 (1974). 153-161. Jazwinski, A. H., “Stochastic Processes and Filtering Theory.” Academic Press, New York, 1970. Jewell, W., Markov renewal programming I and 11, Operations Res. 11 (1963), 938-971. Joseph, P. D., and Tou, J. T., On linear control theory, AIEE Trans. 80 (11), (1961), 193-1 96. Kalman, R. E., A new approach to linear filtering and prediction problems, Trans. ASME Ser. D.  J .  Basic Engrg. 82 (1960), 3545. Kalman, R. E., and Koepcke, R. W., Optimal synthesis of linear sampling control systems using generalized performance indexes, Trans. ASME 80 (l958), 1820-1826. Kalymon, B. A,, Stochastic prices in a single-item inventory purchasing model, Operations Res. 19 (1971), 1434-1458. 
AC-16 (1971). 
REFERENCES 391 
Kamin, J. H., Optimal portfolio revision with a proportional transaction cost, Manage- ment Sci. 21 (1975), 1263-1271. Karush, W., and Dear, E. E., Optimal stimulus presentation strategy for a stimulus sampling model of learning, J. Mathematical Psychology 3 (1966), 1547.  Kaufmann, A., and Cruon, R., “Dynamic Programming.” Academic Press, New York, 1967. Kemeny, J. G., and Snell, J. L., “Finite Markov Chains.” Van Nostrand-Reinhold, Princeton, New Jersey, 1960. Kleindorfer, P. R., and Glover, K., Linear convex stochastic optimal control with applications in production planning, IEEE Trans. Automatic Control AC-18 (l973), 56-59 Kucera, V., A contribution to matrix quadratic equations, IEEE Trans. Automatic Control AC-17 (1972). 344347. Kushner, H. “Introduction to Stochastic Control.” Holt, New York, 1971. Lanery, E., Etude asymptotic des systemes Markoviens a commande, Rev. Francaise Automat. Informat. Recherche Operationnelle 1 (l967), 3-57. Larson, R. E., “State Increment Dynamic Programming.” Amer. Elsevier, New York, 1968. Leland, H., On turnpike portfolios, in Szego, G., and Shell, K. (eds.), “Symposium on Mathematical Methods in Investments and Finance.” Amer. Elsevier, New York, 1972; also Tech. Rep. No. 49, IMSSS, Stanford, California, October 1971. Levhari, D., and Srinivasan, T., Optimal savings under uncertainty, Rev. Econom. Studies 36 (1969), 153-163. Liusternik, L., and Sobolev, V., “Elements of Functional Analysis.” Ungar, New York, 1961. Ljung, L., and Wittenmark, B., Asymptotic properties of self-tuning regulators, Rep. 7404, Div. of Autom. Control, Lund Inst. of Technology, Sweden, Feb. 1974. Luce, R. D., and Raiffa, H., “Games and Decisions.” Wiley, New York, 1957. Luenberger, D. G., “Optimization by Vector Space Methods.” Wiley, New York, 1969. Luenberger, D. G., Cyclic dynamic programming: a procedure for problems with fixed delay, Operations Res. 19 (1971), 1101-1 110. Luenberger, D. G., “Introduction to Linear and Nonlinear Programming.” Addison- Wesley, Reading, Massachusetts, 1973. Maitra, A., A note on positive dynamic programming, Ann. Math. Statist. 40 (1969) 316-319. Malinvaud, E., First order certainty equivalence, Econometrica 37 (1969). 706-718. Manne, A., Linear programming and sequential decisions, Management Sci. 6 (1960). 259-267. Markovitz, H., “Portfolio Selection.” Wiley, New York, 1959. McQueen, J., A modified dynamic programming method for Markovian decision problems, J .  Marh. Anal. Appl. 14 (1966). 3843. Meditch, J. S. “Stochastic Optimal Linear Estimation and Control.” McGraw-Hill, New York, 1969. Mendel, J. M., “Discrete Techniques of Parameter Estimation-The Equation Error Formulation.” Dekker, New York, 1973. Mossin, J., Optimal multi-period portfolio policies, J. Business 41 (l968), 21 5-229. Murphy, W. J., Optimal stochastic control of discrete linear systems with unknown gain, IEEE Trans. Automatic Control AC-13 (l968), 338-344. Nahi, N., “Estimation Theory and Applications.” Wiley, New York, 1969. Nemhauser, G. L., “Introduction to Dynamic Programming.” Wiley, New York, 1966. 
392 REFERENCES 
von Neumann, J., and Morgenstern, O., “Theory of Games and Economic Behavior.” Princeton Univ. Press, Princeton, New Jersey, 1947. Odoni, A. R., On finding the maximal gain for Markov decision processes, Operations Res. 17 (1969), 857-860. Ornstein, D., On the existence of stationary optimal strategies, Proc. Amer. Math. SOC. 20 (1969), 563-569. Owen, G., “Game Theory.” Saunders, Philadelphia, Pennsylvania, 1969. Pallu de la Barriere, R., “Optimal Control Theory.” Saunders, Philadelphia, Penn- sylvania, 1967. Papoulis, A,, *‘Probability, Random Variables and Stochastic Processes.” McCraw- Hill, New York, 1965. Parzen, E., “Modern Probability Theory and its Applications.” Wiley, New York, 1960. Paync, H. J., and Silverman, L. M., On the discrete-time algebraic Riccati equation, IEEE Trans. Automatic Control AC-18 (l973), 226-234. Phelps, E.,. The accumulation of risky capital: a sequential utility analysis, Econo- metrica 30 (1962), 729-741. Pierce, B. D., and Sworder, D. D., Bayes and minimax controllers for a linear system with stochastic jump parameters, IEEE Trans. Automatic Control AC-16 (197 I), 300-307. Pratt, J. W., Risk aversion in the small and in the large, Econometrica 32 (1964), 122-1 36. Raiffa, H., “Decision Analysis: Introductory Lectures on Choices under Uncertainty.” Addison-Wesley, Reading, Massachusetts, 1968. Rockafellar, R. T., “Convex Analysis.” Princeton Univ. Press, Princeton, New Jersey, 1970. Ross, S. M., Arbitrary state Markovian decision processes, Ann. Math. Statist. 39 (1968), 21 18-2122. Ross, S. M., “Applied Probability Models with Optimization Applications.” Holden- Day, San Francisco, California, 1970. Royden, H. L., “Real Analysis.” Macmillan New York, 1968. Rudin, D., “Principles of Mathematical Analysis.” McGraw-Hill, New York, 1964. Saridis, G.  N., “Self-Organizing Control of Stochastic Systems.” Dekker, New York, 1976. Saridis, G .  N., and Dao, T. K., A learning approach to the parameter-adaptive self- organizing control problem, Automutica 8 (1972), 589-597. Savage, L. J., The theory of statistical decision, J.  Amer. Statist. Assoc. 45 (1950), 238-248. Savage, L. J., “The Foundations of Statistics.” Wiley, New York, 1954. Sawaragi, Y ., and Yoshikawa, T., Discrete-time Markovian decision processes with incomplete state observation, Ann. Math. Statist. 41 (1970), 78-86. Scarf, H., The optimality of (s, S) policies for the dynamic inventory problem, Proc. 1st Stanford Symp. Mathematical Methods in the Social Sciences. Stanford University Press, Stanford, California, 1960. Schweitzer, P. J., Perturbation theory and finite Markov chains, J. Appl. Prob. 5 (1968). 401413. Shapley, L. S., Stochastic games, Proc. Nut. Acad. Sci. U.S.A.  39 (1953), Sharpe, W., “Portfolio Theory and Capital Markets.” McGraw-Hill, New York, 1970. Simon, H. A., Dynamic programming under uncertainty with a quadratic criterion function, Econometricu 24 (1956), 74-81. 
- . 
REFERENCES 393 
Sirjaev, A. N., Some new results in the theory of controlled random processes, Selected Transl. Math. Statist. Probability 8 (l970), 49-130. Smallwood, R. D., The analysis of economic teaching strategies for a simple learning model, J. Mathematical Psychology 8 (1971), 285-301. Smallwood, R. D., and Sondik, E. J., The optimal control of partially observable Markov processes over a finite horizon, Operations Res. 11 (1973), 1071-1088. Sondik, E. J., “The Optimal Control of Partially Observable Markov Processes.” Ph.D. Dissertation, Department of Engineering-Economic Systems, Stanford Univ. Stanford, California, June 1971. Stein, G., and Saridis, G. N., A parameter adaptive control technique, Automatica 5 (1969), 731-739. Stratonovich, R. L., On the theory of optimal control: sufficient coordinates, Automat. Remote Control 23 (1963), 847-854. Strauch, R., Negative dynamic programming, Ann. Math. Statist. 37 (1966). 871- 890. Striebel, C. T., Sufficient statistics in the optimal control of stochastic systems, J. Math. Anal. Appl. 12 (1965), 576-592. Striebel, C., “Optimal Control of Discrete Time Stochastic Systems.” Springer-Verlag, New York, 1975. Sussman, R., “Optimal Control of Systems with Stochastic Disturbances.” Electronics Research Lab., Univ. California, Berkeley, Rep. No. 63-20, November 1963. Sworder, D. D., Bayes’ controllers with memory for a linear system with jump param- eters, IEEE Trans. Automatic Control AC-17 (1972). 119-121. Thau, F. E., and Witsenhausen, H. S., A comparison of closed-loop and open-loop optimum systems, IEEE Trans. Automatic Control AC-11 (1966), 619421. Theil, H., Econometric models and welfare maximization, Weltwirtsch. Arch. 72 (1954), 
Tse, E., and Athans, M., Adaptive stochastic control for a class of linear systems, IEEE Trans. Automatic Control AC-17 (l972), 38-52. Tse, E., and Bar-Shalom, Y., An actively adaptive control for linear systems with random parameters via the dual control approach, IEEE Trans. Automatic Control 
Tse, E., Bar-Shalom, Y., and Meier, L., 111, Wide-sense adaptive dual control for non- linear stochastic systems, IEEE Trans. Automatic Control AC-18 (1973). 98-108. 
60-83. 
AC-18 (1973), 109-1 17. 
P I ]  Vajda, S., Stochastic programming, in Abadie, J. (ed.), “Integer and Nonlinear Programming,” Chapter 14. North-Holland Pub]., Amsterdam, 1970. 
[v2] Veinott, A. F., Jr., On finding optimal policies in discrete dynamic programming with no discounting, Ann. Math. Statist. 37 (1966). 12841294. 
[v3] Veinott, A. F., Jr., The status of mathematical inventory theory, Management Sci. 12 (1966), 745-777. 
P 4 ]  Veinott, A. F., Jr., Discrete dynamic programming with sensitive discount optimality criteria, Ann. Math. Statist. 40 (1969), 1635-1660. 
[v5] Veinott, A. F., and Wagner, H. M., Computing optimal (s,  S) policies, Management Sci. 11 (1965), 525-552. 
[V6] Vershik, A. M., Some characteristic properties of Gaussian stochastic processes, Theory Probability Appl., 9 (1964), 353-356. 
[Wl] Wald, A,, “Sequential Analysis.” Wiley, New York, 1947. [W2] White, D. J., Dynamic programming, Markov chains, and the method of successive 
approximations, J. Math. Anal. Appl. 6 (1963), 373-376. [W3] White, D., “Dynamic Programming.” Holden-Day, San Francisco, California, 1969. 
394 REFERENCES 
Witsenhausen, H. S., “Minimax Control of Uncertain Systems.” Ph.D. Dissertation, Department of Electrical Engineering, MIT, Cambridge, Massachusetts, May 1966. Witsenhausen, H. S., Inequalities for the performance of suboptimal uncertain systems, Autornatica 5 (1969), 507-512. Witsenhausen, H. S., On performance bounds for uncertain systems, SIAM J. Control 8 (1970), 55-89. Witsenhausen, H. S., Separation of estimation and control for discrete-time systems, Proc. IEEE59 (1971), 1557-1566. Witsenhausen, H. S., A standard form for sequential stochastic control, Math. Systems Theory 7 (1973), 5-1 I .  Wittenmark, B., Stochastic adaptive control methods: a survey, Internat. J .  Control 
Wong, P. J., and Luenberger, D. G., Reducing the memory requirements of dynamic programming, Operations Res. 16 (1968), 11 15-1 125. Wonham, W. M., On the separation theorem of stochastic control, SIAM J. Control 6 
Wonham, W. M., On a matrix Riccati equation of stochastic control, SIAM J. Control 6 (1968), 681497. Zangwill, W. I., “Nonlinear Programming: A Unified Approach.” Prentice Hall, Englewood Cliffs, New Jersey, 1969. 
21 (1979,705-730. 
(1968), 312-326. 
Index 
A 
Absorbing state, 312 Accessibility conditions, interpretation 
Adaptive control law, 192 Admissible control law, 40, 11 3, 224 Approximation of DP algorithm, 180,279 Asset selling, 95, 107,232,303 Augmentation of state, 58 Autoregressive process, 209 Average cost problem, 221,328 
of, 386 
B Bayes’ rule, 380 Bold strategy, 306 
C 
Capacity expansion, 107 Certainty equivalence principle, 19,81, 134 Certainty equivalent controller, 193 Closed set, 372 Communicating states, 384 
Compact set, 372 Complete relation, 4 Composition of functions, 372 Concave function, 373 Conditional probability, 380 Continuous function, 372 Contraction mapping, 250,280, 282 Control law, 40 Controllability, 14,357 Convergence of vectors, 371 Convex function (set), 373 Countable set, 368 Covariance matrix, 379 Cumulative distribution function, 378 
D 
Decision function, 29 Decision tree, 32 Deterministic finite horizon problems, 55 Deterministic finite state systems, 357 Deterministic linearquadratic problems, 32 1 Discounted cost, 65,220,222 Discretization, 180, 279 
395 
396 INDEX 
Distribution function, 378 Dominant decision. 6 
E 
Ergodic class, 384 Euclidean space, 368 Event, 377 Eventually statipnary problems, 274 Existence 
of optimal solutions, 375 of optimal stationary policies, 231, 
265,293,298,318,331 Expected value, 379 Exponential cost functional, 55,65 
F 
Feedback controller, 29 First passage time, 385 
G 
Gambling, 35, 108, 305, 327 Gauss-Markov estimation, 175 Gaussian random vectors, estimation of, 
160 
H History remembering policies, 233 
I 
Independent random variables, 379 Inf notation, 368, 375 Information vector, 1 12 Inner product, 368 Inventory control, 20, 81, 104, 268, 292, 
Investment problems, 22, 24, 89, 106 Irreducible, 384 
357 
K 
Kalman filter, 134, 167 stability aspects, 171 
K-convexity, 85 
L Least-squares estimation, 20, 159 
deterministic, 177 
linear, 160 purely linear, 174 unbiased, 175 
inferior (lim inf), 372 point, 372 superior (lim sup), 372 
Linearly dependent, 369 Linearly independent, 369 Linear programming, 248, 299, 316 Lottery, 8 
Limit 
M 
Markov renewal problems, 277 Mean first passage time, 337, 385 Min-max problems, 6 ,65,279 Monotone convergence theorem, 252 Myopic policy, 94 
N 
Negative DP model, 25 1 Noninferior decision, 6 Norm, 369 
0 
Observability, 74 Open-loop control, 192 Open-loop feedback control, 198 Open set, 372 Optimal open-loop control sequence, 192 Optimal open-loop value, 192 Optimal value, 42,375 Optimal value function, 42,224 Optimality principle, 48 Orthogonal projection principle, 163 
P 
Partially myopic policy, 94 Payoff function, 5 Periodic problems, 275,291,292 Policy, 29,40 Policy iteration, 246, 283, 288, 299, 316, 
Positive definite matrix, 370 Positive DP model, 25 1 Positive semidefinite matrix, 370 Principle of optimality, 48 Probability density function, 379 
320,349 
INDEX 397 
Probability space, 377 Proper policy, 3 17 Purchasing problems, 99 
Q Quadratic cost, 19,70,103, 109,129, 208, 
Quasi-adaptive control law, 192, 199,204 266,291,292,321,355,376 
R Random variable, 378 Randomized controls, 359 Reachability, 325, 326 Red and black, 305 Replacement problems, 232, 340 Riccati equation, 73 Risk 
averse, 17 aversion, index of, 17 neutral, 17 preferring, 17  
S 
St. Petersburg paradox, 2 Self-tuning regulator, 21 1 Semilinear systems, 67 Semi-Markov decision problems, 277 Sequential probability ratio test, 149,303 Separated portfolio, 90 Separation theorem, 133 Spherically invariant distribution, 134 Stability 
of Kalman filter, 17 1 
of linear regulators, 75, 173 Stable matrix, 74 Stationary policy, 225 Stochastic matrix, 382 Stochastic programming, 215,216 Successive approximation method 
convergence, 237,242,261,263, 264,266,287,290,298,316,323, 345 
error bounds, 237,243,244,280,283, 347 
Sufficient statistic, 122, 137, 145, 150 Sup notation, 368, 375 
T Terminating process, 66 Termination of sampling, 108 Transient state, 384 Transition probability models, 32,235 Transitive relation, 4 Two-armed bandit problem, 157 
U 
Uncorrelated, 379 Undiscounted cost, 220, 294 Utility function, 9, 13, 34 
v Value of information, 192 
W Weierstrass theorem, 375 
A 6  8 7  
D 9  c a  
E O  F 1  6 2  H 3  1 4  J 5  
This page intentionally left blank