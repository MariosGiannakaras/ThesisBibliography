> Source: https://web.mit.edu/dimitrib/www/AbstractDP_ED3_TEXT_2021.pdf

Abstract Dynamic Programming 
THIRD EDITION 
Dimitri P. Bertsekas 
Arizona State University 
Massachusetts Institute of Technology 
WWW site for book information and orders 
http://www.athenasc.com 
Athena Scientific, Belmont, Massachusetts
Athena Scientific Post O!ce Box 805 Nashua, NH 03061-0805 U.S.A. 
Email: info@athenasc.com WWW: http://www.athenasc.com 
Cover design: Dimitri Bertsekas 
c! 2022 Dimitri P. Bertsekas All rights reserved. No part of this book may be reproduced in any form by any electronic or mechanical means (including photocopying, recording, or information storage and retrieval) without permission in writing from the publisher. 
Publisher’s Cataloging-in-Publication Data 
Bertsekas, Dimitri P. Abstract Dynamic Programming: Third Edition Includes bibliographical references and index 1. Mathematical Optimization. 2. Dynamic Programming. I. Title. 
QA402.5 .B465 2022 519.703 01-75941 
ISBN-10: 1-886529-47-7, ISBN-13: 978-1-886529-47-2
ABOUT THE AUTHOR 
Dimitri Bertsekas studied Mechanical and Electrical Engineering at the National Technical University of Athens, Greece, and obtained his Ph.D. in system science from the Massachusetts Institute of Technology. He has held faculty positions with the Engineering-Economic Systems Depart-ment, Stanford University, and the Electrical Engineering Department of the University of Illinois, Urbana. From 1979 to 2019 he was a professor at the Electrical Engineering and Computer Science Department of the Mas-sachusetts Institute of Technology (M.I.T.), where he continues to hold the title of McAfee Professor of Engineering. In 2019, he joined the School of Computing and Augmented Intelligence at the Arizona State University, Tempe, AZ, as Fulton Professor of Computational Decision Making. 
Professor Bertsekas’ teaching and research have spanned several fields, including deterministic optimization, dynamic programming and stochastic control, large-scale and distributed computation, artificial intelligence, and data communication networks. He has authored or coauthored numerous research papers and twenty books, several of which are currently used as textbooks in MIT classes, including “Dynamic Programming and Optimal Control,” “Data Networks,” “Introduction to Probability,” and “Nonlinear Programming.” At ASU, he has been focusing in teaching and research in reinforcement learning, and he has written several textbooks and research monographs in this field since 2019. 
Professor Bertsekas was awarded the INFORMS 1997 Prize for Re-search Excellence in the Interface Between Operations Research and Com-puter Science for his book “Neuro-Dynamic Programming” (co-authored with John Tsitsiklis), the 2001 AACC John R. Ragazzini Education Award, the 2009 INFORMS Expository Writing Award, the 2014 AACC Richard Bellman Heritage Award, the 2014 INFORMS Khachiyan Prize for Life-Time Accomplishments in Optimization, the 2015 MOS/SIAM George B. Dantzig Prize, and the 2022 IEEE Control Systems Award. In 2018 he shared with his coauthor, John Tsitsiklis, the 2018 INFORMS John von Neumann Theory Prize for the contributions of the research monographs “Parallel and Distributed Computation” and “Neuro-Dynamic Program-ming.” Professor Bertsekas was elected in 2001 to the United States Na-tional Academy of Engineering for “pioneering contributions to fundamental research, practice and education of optimization/control theory.”
ATHENA SCIENTIFIC 
OPTIMIZATION AND COMPUTATION SERIES 
1. A Course in Reinforcement Learning by Dimitri P. Bertsekas, 2023, 
ISBN 978-1-886529-49-6, 424 pages 
2. Lessons from AlphaZero for Optimal, Model Predictive, and Adaptive Control by Dimitri P. Bertsekas, 2022, ISBN 978-1-886529-17-5, 245 pages 
3. Abstract Dynamic Programming, 3rd Edition, by Dimitri P. Bert-sekas, 2022, ISBN 978-1-886529-47-2, 420 pages 
4. Rollout, Policy Iteration, and Distributed Reinforcement Learning, by 
Dimitri P. Bertsekas, 2020, ISBN 978-1-886529-07-6, 480 pages 
5. Reinforcement Learning and Optimal Control, by Dimitri P. Bert-
sekas, 2019, ISBN 978-1-886529-39-7, 388 pages 
6. Dynamic Programming and Optimal Control, Two-Volume Set, by Dimitri P. Bertsekas, 2017, ISBN 1-886529-08-6, 1270 pages 
7. Nonlinear Programming, 3rd Edition, by Dimitri P. Bertsekas, 2016, ISBN 1-886529-05-1, 880 pages 
8. Convex Optimization Algorithms, by Dimitri P. Bertsekas, 2015, ISBN 978-1-886529-28-1, 576 pages 
9. Convex Optimization Theory, by Dimitri P. Bertsekas, 2009, ISBN 978-1-886529-31-1, 256 pages 
10. Introduction to Probability, 2nd Edition, by Dimitri P. Bertsekas and 
John N. Tsitsiklis, 2008, ISBN 978-1-886529-23-6, 544 pages 
11. Convex Analysis and Optimization, by Dimitri P. Bertsekas, Angelia 
Nedić, and Asuman E. Ozdaglar, 2003, ISBN 1-886529-45-0, 560 pages 
12. Network Optimization: Continuous and Discrete Models, by Dimitri P. Bertsekas, 1998, ISBN 1-886529-02-7, 608 pages 
13. Network Flows and Monotropic Optimization, by R. Tyrrell Rockafel-lar, 1998, ISBN 1-886529-06-X, 634 pages 
14. Introduction to Linear Optimization, by Dimitris Bertsimas and John N. Tsitsiklis, 1997, ISBN 1-886529-19-1, 608 pages 
15. Parallel and Distributed Computation: Numerical Methods, by Dim-itri P. Bertsekas and John N. Tsitsiklis, 1997, ISBN 1-886529-01-9, 
718 pages 
16. Neuro-Dynamic Programming, by Dimitri P. Bertsekas and John N. Tsitsiklis, 1996, ISBN 1-886529-10-8, 512 pages 
17. Constrained Optimization and Lagrange Multiplier Methods, by Dim-itri P. Bertsekas, 1996, ISBN 1-886529-04-3, 410 pages 
18. Stochastic Optimal Control: The Discrete-Time Case, by Dimitri P. Bertsekas and Steven E. Shreve, 1996, ISBN 1-886529-03-5, 330 pages
Contents 
1. Introduction . . . . . . . . . . . . . . . . . . . . p. 1 
1.1. Structure of Dynamic Programming Problems . . . . . . . p. 2 1.2. Abstract Dynamic Programming Models . . . . . . . . . . p. 5 
1.2.1. Problem Formulation . . . . . . . . . . . . . . . . p. 5 1.2.2. Monotonicity and Contraction Properties . . . . . . . p. 7 1.2.3. Some Examples . . . . . . . . . . . . . . . . . . p. 10 1.2.4. Reinforcement Learning - Projected and Aggregation . . . . 
Bellman Equations . . . . . . . . . . . . . . . . p. 24 1.2.5. Reinforcement Learning - Temporal Di!erence and . . . . . 
Proximal Algorithms . . . . . . . . . . . . . . . . p. 26 1.3. Reinforcement Learning - Approximation in Value Space . . . p. 29 
1.3.1. Approximation in Value Space for . . . . . . . . . . . . Markovian Decision Problems . . . . . . . . . . . . p. 29 
1.3.2. Approximation in Value Space and . . . . . . . . . . . . Newton’s Method . . . . . . . . . . . . . . . . . p. 35 
1.3.3. Policy Iteration and Newton’s Method . . . . . . . . p. 39 1.3.4. Approximation in Value Space for General Abstract . . . . 
Dynamic Programming . . . . . . . . . . . . . . . p. 41 1.4. Organization of the Book . . . . . . . . . . . . . . . . p. 41 1.5. Notes, Sources, and Exercises . . . . . . . . . . . . . . . p. 45 
2. Contractive Models . . . . . . . . . . . . . . . . . p. 53 
2.1. Bellman’s Equation and Optimality Conditions . . . . . . . p. 54 2.2. Limited Lookahead Policies . . . . . . . . . . . . . . . p. 61 2.3. Value Iteration . . . . . . . . . . . . . . . . . . . . . p. 66 
2.3.1. Approximate Value Iteration . . . . . . . . . . . . . p. 67 2.4. Policy Iteration . . . . . . . . . . . . . . . . . . . . . p. 70 
2.4.1. Approximate Policy Iteration . . . . . . . . . . . . p. 73 2.4.2. Approximate Policy Iteration Where Policies Converge . p. 75 
2.5. Optimistic Policy Iteration and !-Policy Iteration . . . . . . p. 77 2.5.1. Convergence of Optimistic Policy Iteration . . . . . . p. 79 2.5.2. Approximate Optimistic Policy Iteration . . . . . . . p. 84 2.5.3. Randomized Optimistic Policy Iteration . . . . . . . . p. 87 
v
vi Contents 
2.6. Asynchronous Algorithms . . . . . . . . . . . . . . . . p. 91 2.6.1. Asynchronous Value Iteration . . . . . . . . . . . . p. 91 2.6.2. Asynchronous Policy Iteration . . . . . . . . . . . . p. 98 2.6.3. Optimistic Asynchronous Policy Iteration with a . . . . . . 
Uniform Fixed Point . . . . . . . . . . . . . . . p. 103 2.7. Notes, Sources, and Exercises . . . . . . . . . . . . . . p. 110 
3. Semicontractive Models . . . . . . . . . . . . . . p. 121 
3.1. Pathologies of Noncontractive DP Models . . . . . . . . p. 123 3.1.1. Deterministic Shortest Path Problems . . . . . . . p. 127 3.1.2. Stochastic Shortest Path Problems . . . . . . . . . p. 129 3.1.3. The Blackmailer’s Dilemma . . . . . . . . . . . . p. 131 3.1.4. Linear-Quadratic Problems . . . . . . . . . . . . p. 134 3.1.5. An Intuitive View of Semicontractive Analysis . . . . p. 139 
3.2. Semicontractive Models and Regular Policies . . . . . . . p. 141 3.2.1. S-Regular Policies . . . . . . . . . . . . . . . . p. 144 3.2.2. Restricted Optimization over S-Regular Policies . . . p. 146 3.2.3. Policy Iteration Analysis of Bellman’s Equation . . . p. 152 3.2.4. Optimistic Policy Iteration and !-Policy Iteration . . p. 160 3.2.5. A Mathematical Programming Approach . . . . . . p. 164 
3.3. Irregular Policies/Infinite Cost Case . . . . . . . . . . p. 165 3.4. Irregular Policies/Finite Cost Case - A Perturbation . . . . . . 
Approach . . . . . . . . . . . . . . . . . . . . . . p. 171 3.5. Applications in Shortest Path and Other Contexts . . . . p. 177 
3.5.1. Stochastic Shortest Path Problems . . . . . . . . . p. 178 3.5.2. A"ne Monotonic Problems . . . . . . . . . . . . p. 186 3.5.3. Robust Shortest Path Planning . . . . . . . . . . p. 195 3.5.4. Linear-Quadratic Optimal Control . . . . . . . . . p. 205 3.5.5. Continuous-State Deterministic Optimal Control . . . p. 207 
3.6. Algorithms . . . . . . . . . . . . . . . . . . . . . . p. 211 3.6.1. Asynchronous Value Iteration . . . . . . . . . . . p. 211 3.6.2. Asynchronous Policy Iteration . . . . . . . . . . . p. 212 
3.7. Notes, Sources, and Exercises . . . . . . . . . . . . . . p. 219 
4. Noncontractive Models . . . . . . . . . . . . . . p. 231 
4.1. Noncontractive Models - Problem Formulation . . . . . . p. 233 4.2. Finite Horizon Problems . . . . . . . . . . . . . . . . p. 235 4.3. Infinite Horizon Problems . . . . . . . . . . . . . . . p. 241 
4.3.1. Fixed Point Properties and Optimality Conditions . . p. 244 4.3.2. Value Iteration . . . . . . . . . . . . . . . . . . p. 256 4.3.3. Exact and Optimistic Policy Iteration - . . . . . . . . . . 
!-Policy Iteration . . . . . . . . . . . . . . . . p. 260 4.4. Regularity and Nonstationary Policies . . . . . . . . . . p. 265 
4.4.1. Regularity and Monotone Increasing Models . . . . . p. 271
Contents vii 
4.4.2. Nonnegative Cost Stochastic Optimal Control . . . . p. 273 4.4.3. Discounted Stochastic Optimal Control . . . . . . . p. 276 4.4.4. Convergent Models . . . . . . . . . . . . . . . . p. 278 
4.5. Stable Policies for Deterministic Optimal Control . . . . . p. 282 4.5.1. Forcing Functions and p-Stable Policies . . . . . . . p. 286 4.5.2. Restricted Optimization over Stable Policies . . . . . p. 289 4.5.3. Policy Iteration Methods . . . . . . . . . . . . . p. 301 
4.6. Infinite-Spaces Stochastic Shortest Path Problems . . . . . p. 307 4.6.1. The Multiplicity of Solutions of Bellman’s Equation . p. 315 4.6.2. The Case of Bounded Cost per Stage . . . . . . . . p. 317 
4.7. Notes, Sources, and Exercises . . . . . . . . . . . . . . p. 320 
5. Sequential Zero-Sum Games and Minimax Control . . p. 337 
5.1. Introduction . . . . . . . . . . . . . . . . . . . . . p. 338 5.2. Relations to Single Player Abstract DP Formulations . . . p. 344 5.3. A New PI Algorithm for Abstract Minimax DP Problems . p. 350 5.4. Convergence Analysis . . . . . . . . . . . . . . . . . p. 364 5.5. Approximation by Aggregation . . . . . . . . . . . . . p. 371 5.6. Notes and Sources . . . . . . . . . . . . . . . . . . p. 373 
Appendix A: Notation and Mathematical Conventions . . p. 377 
A.1. Set Notation and Conventions . . . . . . . . . . . . . p. 377 A.2. Functions . . . . . . . . . . . . . . . . . . . . . . p. 379 
Appendix B: Contraction Mappings . . . . . . . . . . p. 381 
B.1. Contraction Mapping Fixed Point Theorems . . . . . . . p. 381 B.2. Weighted Sup-Norm Contractions . . . . . . . . . . . p. 385 
References . . . . . . . . . . . . . . . . . . . . . p. 391 
Index . . . . . . . . . . . . . . . . . . . . . . . p. 401
Preface of the First Edition 
This book aims at a unified and economical development of the core theory and algorithms of total cost sequential decision problems, based on the strong connections of the subject with fixed point theory. The analysis focuses on the abstract mapping that underlies dynamic programming (DP for short) and defines the mathematical character of the associated problem. Our discussion centers on two fundamental properties that this mapping may have: monotonicity and (weighted sup-norm) contraction. It turns out that the nature of the analytical and algorithmic DP theory is determined primarily by the presence or absence of these two properties, and the rest of the problem’s structure is largely inconsequential. 
In this book, with some minor exceptions, we will assume that monotonicity holds. Consequently, we organize our treatment around the contraction property, and we focus on four main classes of models: 
(a) Contractive models, discussed in Chapter 2, which have the richest and strongest theory, and are the benchmark against which the theory of other models is compared. Prominent among these models are discounted stochastic optimal control problems. The development of these models is quite thorough and includes the analysis of recent approximation algorithms for large-scale problems (neuro-dynamic programming, reinforcement learning). 
(b) Semicontractive models, discussed in Chapter 3 and parts of Chap-ter 4. The term “semicontractive” is used qualitatively here, to refer to a variety of models where some policies have a regularity/contrac-tion-like property but others do not. A prominent example is stochastic shortest path problems, where one aims to drive the state of a Markov chain to a termination state at minimum expected cost. These models also have a strong theory under certain conditions, often nearly as strong as those of the contractive models. 
(c) Noncontractive models, discussed in Chapter 4, which rely on just monotonicity. These models are more complex than the preceding ones and much of the theory of the contractive models generalizes in weaker form, if at all. For example, in general the associated Bell-man equation need not have a unique solution, the value iteration method may work starting with some functions but not with others, and the policy iteration method may not work at all. Infinite horizon examples of these models are the classical positive and negative DP problems, first analyzed by Dubins and Savage, Blackwell, and 
ix
x Preface 
Strauch, which are discussed in various sources. Some new semicontractive models are also discussed in this chapter, further bridging the gap between contractive and noncontractive models. 
(d) Restricted policies and Borel space models, which are discussed in Chapter 5. These models are motivated in part by the complex measurability questions that arise in mathematically rigorous theories of stochastic optimal control involving continuous probability spaces. Within this context, the admissible policies and DP mapping are restricted to have certain measurability properties, and the analysis of the preceding chapters requires modifications. Restricted policy models are also useful when there is a special class of policies with favorable structure, which is “closed” with respect to the standard DP operations, in the sense that analysis and algorithms can be confined within this class. 
We do not consider average cost DP problems, whose character bears a much closer connection to stochastic processes than to total cost problems. We also do not address specific stochastic characteristics underlying the problem, such as for example a Markovian structure. Thus our results apply equally well to Markovian decision problems and to sequential minimax problems. While this makes our development general and a convenient starting point for the further analysis of a variety of di!erent types of problems, it also ignores some of the interesting characteristics of special types of DP problems that require an intricate probabilistic analysis. 
Let us describe the research content of the book in summary, deferring a more detailed discussion to the end-of-chapter notes. A large portion of our analysis has been known for a long time, but in a somewhat fragmentary form. In particular, the contractive theory, first developed by Denardo [Den67], has been known for the case of the unweighted sup-norm, but does not cover the important special case of stochastic shortest path problems where all policies are proper. Chapter 2 transcribes this theory to the weighted sup-norm contraction case. Moreover, Chapter 2 develops extensions of the theory to approximate DP, and includes material on asynchronous value iteration (based on the author’s work [Ber82], [Ber83]), and asynchronous policy iteration algorithms (based on the author’s joint work with Huizhen (Janey) Yu [BeY10a], [BeY10b], [YuB11a]). Most of this material is relatively new, having been presented in the author’s recent book [Ber12a] and survey paper [Ber12b], with detailed references given there. The analysis of infinite horizon noncontractive models in Chapter 4 was first given in the author’s paper [Ber77], and was also presented in the book by Bertsekas and Shreve [BeS78], which in addition contains much of the material on finite horizon problems, restricted policies models, and Borel space models. These were the starting point and main sources for our development. 
The new research presented in this book is primarily on the semi-
Preface xi 
contractive models of Chapter 3 and parts of Chapter 4. Traditionally, the theory of total cost infinite horizon DP has been bordered by two extremes: discounted models, which have a contractive nature, and positive and negative models, which do not have a contractive nature, but rely on an enhanced monotonicity structure (monotone increase and monotone decrease models, or in classical DP terms, positive and negative models). Between these two extremes lies a gray area of problems that are not contractive, and either do not fit into the categories of positive and negative models, or possess additional structure that is not exploited by the theory of these models. Included are stochastic shortest path problems, search problems, linear-quadratic problems, a host of queueing problems, multiplicative and exponential cost models, and others. Together these problems represent an important part of the infinite horizon total cost DP landscape. They possess important theoretical characteristics, not generally available for positive and negative models, such as the uniqueness of solution of Bell-man’s equation within a subset of interest, and the validity of useful forms of value and policy iteration algorithms. 
Our semicontractive models aim to provide a unifying abstract DP structure for problems in this gray area between contractive and noncontractive models. The analysis is motivated in part by stochastic shortest path problems, where there are two types of policies: proper , which are the ones that lead to the termination state with probability one from all starting states, and improper , which are the ones that are not proper. Proper and improper policies can also be characterized through their Bell-man equation mapping: for the former this mapping is a contraction, while for the latter it is not. In our more general semicontractive models, policies are also characterized in terms of their Bellman equation mapping, through a notion of regularity, which generalizes the notion of a proper policy and is related to classical notions of asymptotic stability from control theory. 
In our development a policy is regular within a certain set if its cost function is the unique asymptotically stable equilibrium (fixed point) of the associated DP mapping within that set. We assume that some policies are regular while others are not , and impose various assumptions to ensure that attention can be focused on the regular policies. From an analytical point of view, this brings to bear the theory of fixed points of monotone mappings. From the practical point of view, this allows application to a diverse collection of interesting problems, ranging from stochastic shortest path problems of various kinds, where the regular policies include the proper policies, to linear-quadratic problems, where the regular policies include the stabilizing linear feedback controllers. 
The definition of regularity is introduced in Chapter 3, and its theoretical ramifications are explored through extensions of the classical stochastic shortest path and search problems. In Chapter 4, semicontractive models are discussed in the presence of additional monotonicity structure, which brings to bear the properties of positive and negative DP models. With the
xii Preface 
aid of this structure, the theory of semicontractive models can be strengthened and can be applied to several additional problems, including risk-sensitive/exponential cost problems. 
The book has a theoretical research monograph character, but requires a modest mathematical background for all chapters except the last one, essentially a first course in analysis. Of course, prior exposure to DP will definitely be very helpful to provide orientation and context. A few exercises have been included, either to illustrate the theory with examples and counterexamples, or to provide applications and extensions of the theory. Solutions of all the exercises can be found in Appendix D, at the book’s internet site 
http://www.athenasc.com/abstractdp.html 
and at the author’s web site 
http://web.mit.edu/dimitrib/www/home.html 
Additional exercises and other related material may be added to these sites over time. 
I would like to express my appreciation to a few colleagues for interactions, recent and old, which have helped shape the form of the book. My collaboration with Steven Shreve on our 1978 book provided the motivation and the background for the material on models with restricted policies and associated measurability questions. My collaboration with John Tsitsiklis on stochastic shortest path problems provided inspiration for the work on semicontractive models. My collaboration with Janey (Huizhen) Yu played an important role in the book’s development, and is reflected in our joint work on asynchronous policy iteration, on perturbation models, and on risk-sensitive models. Moreover Janey contributed significantly to the material on semicontractive models with many insightful suggestions. Finally, I am thankful to Mengdi Wang, who went through portions of the book with care, and gave several helpful comments. 
Dimitri P. Bertsekas 
Spring 2013
Preface xiii 
Preface to the Second Edition 
The second edition aims primarily to amplify the presentation of the semicontractive models of Chapter 3 and Chapter 4, and to supplement it with a broad spectrum of research results that I obtained and published in journals and reports since the first edition was written. As a result, the size of this material more than doubled, and the size of the book increased by about 40%. 
In particular, I have thoroughly rewritten Chapter 3, which deals with semicontractive models where stationary regular policies are su"cient. I expanded and streamlined the theoretical framework, and I provided new analyses of a number of shortest path-type applications (deterministic, stochastic, a"ne monotonic, exponential cost, and robust/minimax), as well as several types of optimal control problems with continuous state space (including linear-quadratic, regulation, and planning problems). 
In Chapter 4, I have extended the notion of regularity to nonstationary policies (Section 4.4), aiming to explore the structure of the solution set of Bellman’s equation, and the connection of optimality with other structural properties of optimal control problems. As an application, I have discussed in Section 4.5 the relation of optimality with classical notions of stability and controllability in continuous-spaces deterministic optimal control. In Section 4.6, I have similarly extended the notion of a proper policy to continuous-spaces stochastic shortest path problems. 
I have also revised Chapter 1 a little (mainly with the addition of Section 1.2.5 on the relation between proximal algorithms and temporal di!erence methods), added to Chapter 2 some analysis relating to !-policy iteration and randomized policy iteration algorithms (Section 2.5.3), and I have also added several new exercises (with complete solutions) to Chapters 1-4. Additional material relating to various applications can be found in some of my journal papers, reports, and video lectures on semicontractive models, which are posted at my web site. 
In addition to the changes in Chapters 1-4, I have also eliminated from the second edition the analysis that deals with restricted policies (Chap-ter 5 and Appendix C of the first edition). This analysis is motivated in part by the complex measurability questions that arise in mathematically rigorous theories of stochastic optimal control with Borel state and control spaces. This material is covered in Chapter 6 of the monograph by Bert-sekas and Shreve [BeS78], and followup research on the subject has been limited. Thus, I decided to just post Chapter 5 and Appendix C of the first
xiv Preface 
edition at the book’s web site (40 pages), and omit them from the second edition. As a result of this choice, the entire book now requires only a modest mathematical background, essentially a first course in analysis and in elementary probability. 
The range of applications of dynamic programming has grown enormously in the last 25 years, thanks to the use of approximate simulation-based methods for large and challenging problems. Because approximations are often tied to special characteristics of specific models, their coverage in this book is limited to general discussions in Chapter 1 and to error bounds given in Chapter 2. However, much of the work on approximation methods so far has focused on finite-state discounted, and relatively simple deterministic and stochastic shortest path problems, for which there is solid and robust analytical and algorithmic theory (part of Chapters 2 and 3 in this monograph). As the range of applications becomes broader, I expect that the level of mathematical understanding projected in this book will become essential for the development of e!ective and reliable solution methods. In particular, much of the new material in this edition deals with infinite-state and/or complex shortest path type-problems, whose approximate solution will require new methodologies that transcend the current state of the art. 
Dimitri P. Bertsekas 
January 2018
Preface xv 
Preface to the Third Edition 
The third edition is based on the same theoretical framework as the second edition, but contains two major additions. The first is to highlight the central role of abstract DP methods in the conceptualization of reinforcement learning and approximate DP methods, as described in the author’s recent book “Lessons from AlphaZero for Optimal, Model Predic-tive, and Adaptive Control,” Athena Scientific, 2022. The main idea here is that approximation in value space with one-step lookahead amounts to a step of Newton’s method for solving the abstract Bellman’s equation. This material is included in summary form in view of its strong reliance on abstract DP visualization. Our presentation relies primarily on geometric illustrations rather than mathematical analysis, and is given in Section 1.3. 
The second addition is a new Chapter 5 on abstract DP methods for minimax and zero sum game problems, which is based on the author’s recent paper [Ber21c]. A primary motivation here is the resolution of some long-standing convergence di"culties of the “natural” policy iteration algorithm, which have been known since the Pollatschek and Avi-Itzhak method [PoA69] for finite-state Markov games. Mathematically, this “natural” algorithm is a form of Newton’s method for solving the corresponding Bell-man’s equation, but Newton’s method, contrary to the case of single-player DP problems, is not globally convergent in the case of a minimax problem, because the Bellman operator may have components that are neither convex nor concave. Our approach in Chapter 5 has been to introduce a special type of abstract Bellman operator for minimax problems, and modify the standard PI algorithm along the lines of the asynchronous optimistic PI algorithm of Section 2.6.3, which involves a parametric contraction mapping with a uniform fixed point. 
The third edition also contains a number of small corrections and editorial changes. The author wishes to thank the contributions of several colleagues in this regard, and particularly Yuchao Li, who proofread with care large portions of the book. 
Dimitri P. Bertsekas 
February 2022
1 Introduction 
Contents 
1.1. Structure of Dynamic Programming Problems . . . . . p. 2 1.2. Abstract Dynamic Programming Models . . . . . . . . p. 5 
1.2.1. Problem Formulation . . . . . . . . . . . . . . p. 5 1.2.2. Monotonicity and Contraction Properties . . . . . p. 7 1.2.3. Some Examples . . . . . . . . . . . . . . . . p. 10 1.2.4. Reinforcement Learning - Projected and Aggregation . . 
Bellman Equations . . . . . . . . . . . . . . p. 24 1.2.5. Reinforcement Learning - Temporal Di!erence and . . . 
Proximal Algorithms . . . . . . . . . . . . . . p. 26 1.3. Reinforcement Learning - Approximation in Value Space . p. 29 
1.3.1. Approximation in Value Space for . . . . . . . . . . Markovian Decision Problems . . . . . . . . . . p. 29 
1.3.2. Approximation in Value Space and . . . . . . . . . . Newton’s Method . . . . . . . . . . . . . . . p. 35 
1.3.3. Policy Iteration and Newton’s Method . . . . . . p. 39 1.3.4. Approximation in Value Space for General Abstract . . 
Dynamic Programming . . . . . . . . . . . . . p. 41 1.4. Organization of the Book . . . . . . . . . . . . . . p. 41 1.5. Notes, Sources, and Exercises . . . . . . . . . . . . . p. 45 
1
2 Introduction Chap. 1 
1.1 STRUCTURE OF DYNAMIC PROGRAMMINGPROBLEMS 
Dynamic programming (DP for short) is the principal method for analysis of a large and diverse class of sequential decision problems. Examples are deterministic and stochastic optimal control problems with a continuous state space, Markov and semi-Markov decision problems with a discrete state space, minimax problems, and sequential zero-sum games. While the nature of these problems may vary widely, their underlying structures turn out to be very similar. In all cases there is an underlying mapping that depends on an associated controlled dynamic system and corresponding cost per stage. This mapping, the DP (or Bellman) operator, provides a compact “mathematical signature” of the problem. It defines the cost function of policies and the optimal cost function, and it provides a convenient shorthand notation for algorithmic description and analysis. 
More importantly, the structure of the DP operator defines the mathematical character of the associated problem. The purpose of this book is to provide an analysis of this structure, centering on two fundamental properties: monotonicity and (weighted sup-norm) contraction. It turns out that the nature of the analytical and algorithmic DP theory is determined primarily by the presence or absence of one or both of these two properties, and the rest of the problem’s structure is largely inconsequential. 
A Deterministic Optimal Control Example 
To illustrate our viewpoint, let us consider a discrete-time deterministic optimal control problem described by a system equation 
xk+1 = f(xk, uk), k = 0, 1, . . . . (1.1) 
Here xk is the state of the system taking values in a set X (the state space), and uk is the control taking values in a set U (the control space). † At stage k, there is a cost 
!kg(xk, uk) 
incurred when uk is applied at state xk, where ! is a scalar in (0, 1] that has the interpretation of a discount factor when ! < 1. The controls are chosen as a function of the current state, subject to a constraint that depends on that state. In particular, at state x the control is constrained to take values in a given set U(x) ! U . Thus we are interested in optimization over the set of (nonstationary) policies 
" = ! 
{µ0, µ1, . . .} | µk " M, k = 0, 1, . . . " 
, 
† Our discussion of this section is somewhat informal, without strict adher-
ence to mathematical notation and rigor. We will introduce a rigorous mathematical framework later.
Sec. 1.1 Structure of Dynamic Programming Problems 3 
where M is the set of functions µ : X #$ U defined by 
M = ! 
µ | µ(x) " U(x), % x " X " 
. 
The total cost of a policy " = {µ0, µ1, . . .} over an infinite number of stages (an infinite horizon) and starting at an initial state x0 is the limit superior of the N -step costs 
J!(x0) = lim sup N!" 
N#1 # 
k=0 
!kg $ 
xk, µk(xk) % 
, (1.2) 
where the state sequence {xk} is generated by the deterministic system (1.1) under the policy ": 
xk+1 = f $ 
xk, µk(xk) % 
, k = 0, 1, . . . . 
(We use limit superior rather than limit to cover the case where the limit does not exist.) The optimal cost function is 
J*(x) = inf !$! 
J!(x), x " X. 
For any policy " = {µ0, µ1, . . .}, consider the policy "1 = {µ1, µ2, . . .} and write by using Eq. (1.2), 
J!(x) = g $ 
x, µ0(x) % 
+ !J!1 
$ 
f(x, µ0(x)) % 
. 
We have for all x " X 
J*(x) = inf !={µ0,!1}$! 
& 
g $ 
x, µ0(x) % 
+ !J!1 
$ 
f(x, µ0(x)) % 
' 
= inf µ0$M 
& 
g $ 
x, µ0(x) % 
+ ! inf !1$! 
J!1 
$ 
f(x, µ0(x)) % 
' 
= inf µ0$M 
& 
g $ 
x, µ0(x) % 
+ !J* $ 
f(x, µ0(x)) % 
' 
. 
The minimization over µ0 " M can be written as minimization over all u " U(x), so we can write the preceding equation as 
J*(x) = inf u$U(x) 
& 
g(x, u) + !J* $ 
f(x, u) % 
' 
, % x " X. (1.3) 
This equation is an example of Bellman’s equation, which plays a central role in DP analysis and algorithms. If it can be solved for J*, an optimal stationary policy {µ%, µ%, . . .} may typically be obtained by minimization of the right-hand side for each x, i.e., 
µ%(x) " arg min u$U(x) 
& 
g(x, u) + !J* $ 
f(x, u) % 
' 
, % x " X. (1.4)
4 Introduction Chap. 1 
We now note that both Eqs. (1.3) and (1.4) can be stated in terms of the expression 
H(x, u, J) = g(x, u) + !J $ 
f(x, u) % 
, x " X, u " U(x). 
Defining (TµJ)(x) = H 
$ 
x, µ(x), J % 
, x " X, 
and (TJ)(x) = inf 
u$U(x) H(x, u, J), x " X, 
we see that Bellman’s equation (1.3) can be written compactly as 
J* = TJ*, 
i.e., J* is the fixed point of T , viewed as a mapping from the set of functions onX into itself. Moreover, it can be similarly seen that Jµ, the cost function of the stationary policy {µ, µ, . . .}, is a fixed point of Tµ. In addition, the optimality condition (1.4) can be stated compactly as 
Tµ!J* = TJ*. 
We will see later that additional properties, as well as a variety of algorithms for finding J* can be stated and analyzed using the mappings T and Tµ. 
The mappings Tµ can also be used in the context of DP problems with a finite number of stages (a finite horizon). In particular, for a given policy " = {µ0, µ1, . . .} and a terminal cost !N J̄(xN ) for the state xN at the end of N stages, consider the N -stage cost function 
J!,N(x0) = !N J̄(xN ) + N#1 # 
k=0 
!kg $ 
xk, µk(xk) % 
. (1.5) 
Then it can be verified by induction that for all initial states x0, we have 
J!,N (x0) = (Tµ0Tµ1 · · ·TµN"1 J̄)(x0). (1.6) 
Here Tµ0Tµ1 · · ·TµN"1 is the composition of the mappings Tµ0 , Tµ1 , . . . TµN"1 , i.e., for all J , 
(Tµ0Tµ1J)(x) = $ 
Tµ0(Tµ1J) % 
(x), x " X, 
and more generally 
(Tµ0Tµ1 · · ·TµN"1J)(x) = $ 
Tµ0(Tµ1(· · · (TµN"1J))) % 
(x), x " X, 
(our notational conventions are summarized in Appendix A). Thus the finite horizon cost functions J!,N of " can be defined in terms of the mappings Tµ [cf. Eq. (1.6)], and so can the infinite horizon cost function J!: 
J!(x) = lim sup N!" 
(Tµ0Tµ1 · · ·TµN"1 J̄)(x), x " X, (1.7) 
where J̄ is the zero function, J̄(x) = 0 for all x " X .
Sec. 1.2 Abstract Dynamic Programming Models 5 
Connection with Fixed Point Methodology 
The Bellman equation (1.3) and the optimality condition (1.4), stated in terms of the mappings Tµ and T , highlight a central theme of this book, which is that DP theory is intimately connected with the theory of abstract mappings and their fixed points. Analogs of the Bellman equation, J* = TJ*, optimality conditions, and other results and computational methods hold for a great variety of DP models, and can be stated compactly as described above in terms of the corresponding mappings Tµ and T . The gain from this abstraction is greater generality and mathematical insight, as well as a more unified, economical, and streamlined analysis. 
1.2 ABSTRACT DYNAMIC PROGRAMMING MODELS 
In this section we formally introduce and illustrate with examples an abstract DP model, which embodies the ideas just discussed in Section 1.1. 
1.2.1 Problem Formulation 
Let X and U be two sets, which we loosely refer to as a set of “states” and a set of “controls,” respectively. For each x " X , let U(x) ! U be a nonempty subset of controls that are feasible at state x. We denote by M the set of all functions µ : X #$ U with µ(x) " U(x), for all x " X . 
In analogy with DP, we refer to sequences " = {µ0, µ1, . . .}, with µk " M for all k, as “nonstationary policies,” and we refer to a sequence {µ, µ, . . .}, with µ " M, as a “stationary policy.” In our development, stationary policies will play a dominant role, and with slight abuse of terminology, we will also refer to any µ " M as a “policy” when confusion cannot arise. 
Let R(X) be the set of real-valued functions J : X #$ &, and let H : X 'U 'R(X) #$ & be a given mapping. † For each policy µ " M, we consider the mapping Tµ : R(X) #$ R(X) defined by 
(TµJ)(x) = H $ 
x, µ(x), J % 
, % x " X, J " R(X), 
and we also consider the mapping T defined by ‡ 
(TJ)(x) = inf u$U(x) 
H(x, u, J), % x " X, J " R(X). 
† Our notation and mathematical conventions are outlined in Appendix A. 
In particular, we denote by ! the set of real numbers, and by !n the space of n-dimensional vectors with real components. 
‡ We assume that H , TµJ , and TJ are real-valued for J " R(X) in the 
present chapter and in Chapter 2. In Chapters 3 and 4 we will allow H(x, u, J), and hence also (TµJ)(x) and (TJ)(x), to take the values # and $#.
6 Introduction Chap. 1 
We will generally refer to T and Tµ as the (abstract) DP mappings or DP operators or Bellman operators (the latter name is common in the artificial intelligence and reinforcement learning literature). 
Similar to the deterministic optimal control problem of the preceding section, the mappings Tµ and T serve to define a multistage optimization problem and a DP-like methodology for its solution. In particular, for some function J̄ " R(X), and nonstationary policy " = {µ0, µ1, . . .}, we define for each integer N ( 1 the functions 
J!,N (x) = (Tµ0Tµ1 · · ·TµN"1 J̄)(x), x " X, 
where Tµ0Tµ1 · · ·TµN"1 denotes the composition of the mappings Tµ0 , Tµ1 , . . . , TµN"1 , i.e., 
Tµ0Tµ1 · · ·TµN"1J = $ 
Tµ0(Tµ1(· · · (TµN"2(TµN"1J))) · · ·) % 
, J " R(X). 
We view J!,N as the “N -stage cost function” of " [cf. Eq. (1.5)]. Consider also the function 
J!(x) = lim sup N!" 
J!,N (x) = lim sup N!" 
(Tµ0Tµ1 · · ·TµN"1 J̄)(x), x " X, 
which we view as the “infinite horizon cost function” of " [cf. Eq. (1.7); we use lim sup for generality, since we are not assured that the limit exists]. We want to minimize J! over ", i.e., to find 
J*(x) = inf ! 
J!(x), x " X, 
and a policy "% that attains the infimum, if one exists. The key connection with fixed point methodology is that J* “typi-
cally” (under mild assumptions) can be shown to satisfy 
J*(x) = inf u$U(x) 
H(x, u, J*), % x " X, 
i.e., it is a fixed point of T . We refer to this as Bellman’s equation [cf. Eq. (1.3)]. Another fact is that if an optimal policy "% exists, it “typically” can be selected to be stationary, "% = {µ%, µ%, . . .}, with µ% " M satisfying an optimality condition, such as for example 
(Tµ!J*)(x) = (TJ*)(x), x " X, 
[cf. Eq. (1.4)]. Several other results of an analytical or algorithmic nature also hold under appropriate conditions, which will be discussed in detail later. 
However, Bellman’s equation and other related results may not hold without Tµ and T having some special structural properties. Prominent among these are a monotonicity assumption that typically holds in DP problems, and a contraction assumption that holds for some important classes of problems. We describe these assumptions next.
Sec. 1.2 Abstract Dynamic Programming Models 7 
1.2.2 Monotonicity and Contraction Properties 
Let us now formalize the monotonicity and contraction assumptions. We will require that both of these assumptions hold for most of the next chapter, and we will gradually relax the contraction assumption in Chapters 3 and 4. Recall also our assumption that Tµ and T map R(X) (the space of real-valued functions over X) into R(X). In Chapters 3 and 4 we will relax this assumption as well. 
Assumption 1.2.1: (Monotonicity) If J, J & " R(X) and J ) J &, then 
H(x, u, J) ) H(x, u, J &), % x " X, u " U(x). 
Note that by taking infimum over u " U(x), we have 
J(x) % J #(x), & x " X ' inf u$U(x) 
H(x, u, J) % inf u$U(x) 
H(x, u, J #), & x " X, 
or equivalently, † 
J ) J & * TJ ) TJ &. 
Another way to arrive at this relation, is to note that the monotonicity assumption is equivalent to 
J ) J & * TµJ ) TµJ &, % µ " M, 
and to use the simple but important fact 
inf u$U(x) 
H(x, u, J) = inf µ$M 
(TµJ)(x), % x " X, J " R(X), 
i.e., for a fixed x " X , infimum over u is equivalent to infimum over µ. This is true because for any µ, there is no coupling constraint between the controls µ(x) and µ(x&) that correspond to two di!erent states x and x&, i.e., the set M = 
! 
µ | µ(x) " U(x), % x " X " 
can be viewed as the Cartesian product "x$XU(x). We will be writing this relation as TJ = infµ$M TµJ . 
For the contraction assumption, we introduce a function v : X #$ & with 
v(x) > 0, % x " X. 
† Unless otherwise stated, in this book, inequalities involving functions, min-
ima and infima of a collection of functions, and limits of function sequences are meant to be pointwise; see Appendix A for our notational conventions.
8 Introduction Chap. 1 
J TJ 
= 0 TµJ 
= 0 J TJ 
= 0 TµJ 
= 0 ) Jµ 
Figure 1.2.1. Illustration of the monotonicity and the contraction assumptions in one dimension. The mapping Tµ on the left is monotone but is not a contraction. The mapping Tµ on the right is both monotone and a contraction. It has a unique fixed point at Jµ. 
Let us denote by B(X) the space of real-valued functions J on X such that J(x)/v(x) is bounded as x ranges over X , and consider the weighted sup-norm 
+J+ = sup x$X 
( 
(J(x) ( 
( 
v(x) 
on B(X). The properties of B(X) and some of the associated fixed point theory are discussed in Appendix B. In particular, as shown there, B(X) is a complete normed space, so any mapping from B(X) to B(X) that is a contraction or an m-stage contraction for some integer m > 1, with respect to + · +, has a unique fixed point (cf. Props. B.1 and B.2). 
Assumption 1.2.2: (Contraction) For all J " B(X) and µ " M, the functions TµJ and TJ belong to B(X). Furthermore, for some ! " (0, 1), we have 
+TµJ , TµJ &+ ) !+J , J &+, % J, J & " B(X), µ " M. (1.8) 
Figure 1.2.1 illustrates the monotonicity and the contraction assumptions. It can be shown that the contraction condition (1.8) implies that 
+TJ , TJ &+ ) !+J , J &+, % J, J & " B(X), (1.9) 
so that T is also a contraction with modulus !. To see this we use Eq. (1.8) to write 
(TµJ)(x) ) (TµJ &)(x) + !+J , J &+ v(x), % x " X,
Sec. 1.2 Abstract Dynamic Programming Models 9 
from which, by taking infimum of both sides over µ " M, we have 
(TJ)(x), (TJ &)(x) 
v(x) ) !+J , J &+, % x " X. 
Reversing the roles of J and J &, we also have 
(TJ &)(x) , (TJ)(x) 
v(x) ) !+J , J &+, % x " X, 
and combining the preceding two relations, and taking the supremum of the left side over x " X , we obtain Eq. (1.9). 
Nearly all mappings related to DP satisfy the monotonicity assumption, and many important ones satisfy the weighted sup-norm contraction assumption as well. When both assumptions hold, the most powerful analytical and computational results can be obtained, as we will show in Chapter 2. These are: 
(a) Bellman’s equation has a unique solution, i.e., T and Tµ have unique fixed points, which are the optimal cost function J* and the cost functions Jµ of the stationary policies {µ, µ, . . .}, respectively [cf. Eq. (1.3)]. 
(b) A stationary policy {µ%, µ%, . . .} is optimal if and only if 
Tµ!J* = TJ*, 
[cf. Eq. (1.4)]. 
(c) J* and Jµ can be computed by the value iteration method, 
J* = lim k!" 
T kJ, Jµ = lim k!" 
T k µJ, 
starting with any J " B(X). 
(d) J* can be computed by the policy iteration method, whereby we generate a sequence of stationary policies via 
Tµk+1Jµk = TJµk , 
starting from some initial policy µ0 [here Jµk is obtained as the fixed point of Tµk by several possible methods, including value iteration as in (c) above]. 
These are the most favorable types of results one can hope for in the DP context, and they are supplemented by a host of other results, involving approximate and/or asynchronous implementations of the value and policy iteration methods, and other related methods that combine features of both. As the contraction property is relaxed and is replaced by various weaker assumptions, some of the preceding results may hold in weaker form. For example J* turns out to be a solution of Bellman’s equation in most of the models to be discussed, but it may not be the unique solution. The interplay between the monotonicity and contractionlike properties, and the associated results of the form (a)-(d) described above is a recurring analytical theme in this book.
10 Introduction Chap. 1 
1.2.3 Some Examples 
In what follows in this section, we describe a few special cases, which indicate the connections of appropriate forms of the mapping H with the most popular total cost DP models. In all these models the monotonicity As-sumption 1.2.1 (or some closely related version) holds, but the contraction Assumption 1.2.2 may not hold, as we will indicate later. Our descriptions are by necessity brief, and the reader is referred to the relevant textbook literature for more detailed discussion. 
Example 1.2.1 (Stochastic Optimal Control - Markovian Decision Problems) 
Consider the stationary discrete-time dynamic system 
xk+1 = f(xk, uk, wk), k = 0, 1, . . . , (1.10) 
where for all k, the state xk is an element of a space X, the control uk is an element of a space U , and wk is a random “disturbance,” an element of a space W . We consider problems with infinite state and control spaces, as well as problems with discrete (finite or countable) state space (in which case the underlying system is a Markov chain). However, for technical reasons that relate to measure-theoretic issues, we assume that W is a countable set . 
The control uk is constrained to take values in a given nonempty subset U(xk) of U , which depends on the current state xk [uk " U(xk), for all xk " X]. The random disturbances wk, k = 0, 1, . . ., are characterized by probability distributions P (· | xk, uk) that are identical for all k, where P (wk | xk, uk) is the probability of occurrence of wk, when the current state and control are xk and uk, respectively. Thus the probability of wk may depend explicitly on xk and uk, but not on values of prior disturbances wk"1, . . . , w0. 
Given an initial state x0, we want to find a policy ! = {µ0, µ1, . . .}, where µk : X () U , µk(xk) " U(xk), for all xk " X, k = 0, 1, . . ., that minimizes the cost function 
J!(x0) = lim sup N%& 
E wk 
k=0,1,... 
) 
N"1 # 
k=0 
"kg $ 
xk, µk(xk), wk 
% 
* 
, (1.11) 
where " " (0, 1] is a discount factor, subject to the system equation constraint 
xk+1 = f $ 
xk, µk(xk), wk 
% 
, k = 0, 1, . . . . 
This is a classical problem, which is discussed extensively in various sources, including the author’s text [Ber12a]. It is usually referred to as the stochastic optimal control problem or the Markovian Decision Problem (MDP for short). 
Note that the expected value of the N-stage cost of !, 
E wk 
k=0,1,... 
) 
N"1 # 
k=0 
"kg $ 
xk, µk(xk), wk 
% 
* 
,
Sec. 1.2 Abstract Dynamic Programming Models 11 
is defined as a (possibly countably infinite) sum, since the disturbances wk, k = 0, 1, . . ., take values in a countable set. Indeed, the reader may verify that all the subsequent mathematical expressions that involve an expected value can be written as summations over a finite or a countable set, so they make sense without resort to measure-theoretic integration concepts. † 
In what follows we will often impose appropriate assumptions on the cost per stage g and the scalar ", which guarantee that the infinite horizon cost J!(x0) is defined as a limit (rather than as a lim sup): 
J!(x0) = lim N%& 
E wk 
k=0,1,... 
) 
N"1 # 
k=0 
"kg $ 
xk, µk(xk), wk 
% 
* 
. 
In particular, it can be shown that the limit exists if " < 1 and the expected value of |g| is uniformly bounded, i.e., for some B > 0, 
E ! ( 
(g(x, u,w) ( 
( 
" 
% B, & x " X, u " U(x). (1.12) 
In this case, we obtain the classical discounted infinite horizon DP problem, which generally has the most favorable structure of all infinite horizon stochastic DP models (see [Ber12a], Chapters 1 and 2). 
To make the connection with abstract DP, let us define 
H(x, u, J) = E ! 
g(x, u,w) + "J $ 
f(x, u, w) %" 
, 
so that 
(TµJ)(x) = E ! 
g $ 
x,µ(x), w % 
+ "J $ 
f(x, µ(x), w) %" 
, 
and (TJ)(x) = inf 
u$U(x) E ! 
g(x, u,w) + "J $ 
f(x, u,w) %" 
. 
Similar to the deterministic optimal control problem of Section 1.1, the N-stage cost of !, can be expressed in terms of Tµ: 
(Tµ0 · · · TµN"1 J̄)(x0) = E wk 
k=0,1,... 
) 
N"1 # 
k=0 
"kg $ 
xk, µk(xk), wk 
% 
* 
, 
† As noted in Appendix A, the formula for the expected value of a random variable w defined over a space ! is 
E{w} = E{w+}+ E{w"}, 
where w+ and w" are the positive and negative parts of w, 
w+(#) = max ! 
0, w(#) " 
, w"(#) = min ! 
0, w(#) " 
, & # " !. 
In this way, taking also into account the rule#$# = # (see Appendix A),E{w} is well-defined as an extended real number if ! is finite or countably infinite.
12 Introduction Chap. 1 
where J̄ is the zero function, J̄(x) = 0 for all x " X. The same is true for the infinite-stage cost [cf. Eq. (1.11)]: 
J!(x0) = lim sup N%& 
(Tµ0 · · ·TµN"1 J̄)(x0). 
It can be seen that the mappings Tµ and T are monotone, and it is well-known that if " < 1 and the boundedness condition (1.12) holds, they are contractive as well (under the unweighted sup-norm); see e.g., [Ber12a], Chapter 1. In this case, the model has the powerful analytical and algorithmic properties (a)-(d) mentioned at the end of the preceding subsection. In particular, the optimal cost function J! [i.e., J!(x) = inf! J!(x) for all x " X] can be shown to be the unique solution of the fixed point equation J! = TJ!, also known as Bellman’s equation, which has the form 
J!(x) = inf u$U(x) 
E ! 
g(x, u,w) + "J! $ 
f(x, u,w) %" 
, x " X, 
and parallels the one given for deterministic optimal control problems [cf. Eq. (1.3)]. 
These properties can be expressed and analyzed in an abstract setting by using just the mappings Tµ and T , both when Tµ and T are contractive (see Chapter 2), and when they are only monotone and not contractive while either g * 0 or g % 0 (see Chapter 4). Moreover, under some conditions, it is possible to analyze these properties in cases where Tµ is contractive for some but not all µ (see Chapter 3, and Section 4.4). 
Example 1.2.2 (Finite-State Discounted Markovian Decision Problems) 
In the special case of the preceding example where the number of states is finite, the system equation (1.10) may be defined in terms of the transition probabilities 
pxy(u) = Prob $ 
y = f(x, u, w) | x % 
, x, y " X, u " U(x), 
so H takes the form 
H(x, u, J) = # 
y$X 
pxy(u) $ 
g(x, u, y) + "J(y) % 
. 
When " < 1 and the boundedness condition ( 
(g(x, u, y) ( 
( % B, & x, y " X, u " U(x), 
[cf. Eq. (1.12)] holds (or more simply, when U is a finite set), the mappings Tµ 
and T are contraction mappings with respect to the standard (unweighted) sup-norm. This is a classical model, referred to as discounted finite-state MDP , which has a favorable theory and has found extensive applications (cf. [Ber12a], Chapters 1 and 2). The model is additionally important, because it is often used for computational solution of continuous state space problems via discretization.
Sec. 1.2 Abstract Dynamic Programming Models 13 
Example 1.2.3 (Discounted Semi-Markov Problems) 
With x, y, and u as in Example 1.2.2, consider a mapping of the form 
H(x, u, J) = G(x, u) + # 
y$X 
mxy(u)J(y), 
where G is some function representing expected cost per stage, and mxy(u) are nonnegative scalars with 
# 
y$X 
mxy(u) < 1, & x " X, u " U(x). 
The equation J! = TJ! is Bellman’s equation for a finite-state continuoustime semi-Markov decision problem, after it is converted into an equivalent discrete-time problem (cf. [Ber12a], Section 1.4). Again, the mappings Tµ and T are monotone and can be shown to be contraction mappings with respect to the unweighted sup-norm. 
Example 1.2.4 (Discounted Zero-Sum Dynamic Games) 
Let us consider a zero-sum game analog of the finite-state MDP Example 1.2.2. Here there are two players that choose actions at each stage: the first (called the minimizer) may choose a move i out of n moves and the second (called the maximizer) may choose a move j out of m moves. Then the minimizer gives a specified amount aij to the maximizer, called a payo! . The minimizer wishes to minimize aij , and the maximizer wishes to maximize aij . 
The players use mixed strategies, whereby the minimizer selects a probability distribution u = (u1, . . . , un) over his n possible moves and the maximizer selects a probability distribution v = (v1, . . . , vm) over his m possible moves. Thus the probability of selecting i and j is uivj , and the expected payo" for this stage is 
+ 
i,j aijuivj or u#Av, where A is the n + m matrix 
with components aij . In a single-stage version of the game, the minimizer must minimize 
maxv$V u#Av and the maximizer must maximize minu$U u#Av, where U and V are the sets of probability distributions over {1, . . . , n} and {1, . . . , m}, respectively. A fundamental result (which will not be proved here) is that these two values are equal: 
min u$U 
max v$V 
u#Av = max v$V 
min u$U 
u#Av. (1.13) 
Let us consider the situation where a separate game of the type just described is played at each stage. The game played at a given stage is represented by a “state” x that takes values in a finite set X. The state evolves according to transition probabilities qxy(i, j) where i and j are the moves selected by the minimizer and the maximizer, respectively (here y represents
14 Introduction Chap. 1 
the next game to be played after moves i and j are chosen at the game represented by x). When the state is x, under u " U and v " V , the one-stage expected payo" is u#A(x)v, where A(x) is the n +m payo" matrix, and the state transition probabilities are 
pxy(u, v) = 
n # 
i=1 
m # 
j=1 
uivjqxy(i, j) = u#Qxyv, 
where Qxy is the n + m matrix that has components qxy(i, j). Payo"s are discounted by " " (0, 1), and the objectives of the minimizer and maximizer, roughly speaking, are to minimize and to maximize the total discounted expected payo". This requires selections of u and v to strike a balance between obtaining favorable current stage payo"s and playing favorable games in future stages. 
We now introduce an abstract DP framework related to the sequential move selection process just described. We consider the mapping G given by 
G(x, u, v, J) = u#A(x)v + " # 
y$X 
pxy(u, v)J(y) 
= u# 
, 
A(x) + " # 
y$X 
QxyJ(y) 
-
v, 
(1.14) 
where " " (0, 1) is discount factor, and the mapping H given by 
H(x, u, J) = max v$V 
G(x, u, v, J). 
The corresponding mappings Tµ and T are 
(TµJ)(x) = max v$V 
G $ 
x, µ(x), v, J % 
, x " X, 
and (TJ)(x) = min 
u$U max v$V 
G(x, u, v, J). 
It can be shown that Tµ and T are monotone and (unweighted) sup-norm contractions. Moreover, the unique fixed point J! of T satisfies 
J!(x) = min u$U 
max v$V 
G(x, u, v, J!), & x " X, 
(see [Ber12a], Section 1.6.2). We now note that since 
A(x) + " # 
y$X 
QxyJ(y) 
[cf. Eq. (1.14)] is a matrix that is independent of u and v, we may view J!(x) as the value of a static game (which depends on the state x). In particular, from the fundamental minimax equality (1.13), we have 
min u$U 
max v$V 
G(x, u, v, J!) = max v$V 
min u$U 
G(x, u, v, J!), & x " X.
Sec. 1.2 Abstract Dynamic Programming Models 15 
This implies that J! is also the unique fixed point of the mapping 
(TJ)(x) = max v$V 
H(x, v, J), 
where H(x, v, J) = min 
u$U G(x, u, v, J), 
i.e., J! is the fixed point regardless of the order in which minimizer and maximizer select mixed strategies at each stage. 
In the preceding development, we have introduced J! as the unique fixed point of the mappings T and T . However, J! also has an interpretation in game theoretic terms. In particular, it can be shown that J!(x) is the value of a dynamic game, whereby at state x the two opponents choose multistage (possibly nonstationary) policies that consist of functions of the current state, and continue to select moves using these policies over an infinite horizon. For further discussion of this interpretation, we refer to [Ber12a] and to books on dynamic games such as [FiV96]; see also [PaB99] and [Yu14] for an analysis of the undiscounted case (" = 1) where there is a termination state, as in the stochastic shortest path problems of the subsequent Example 1.2.6. An alternative and more general formulation of sequential zero-sum games, which allows for an infinite state space, will be given in Chapter 5. 
Example 1.2.5 (Minimax Problems) 
Consider a minimax version of Example 1.2.1, where w is not random but is rather chosen from within a set W (x, u) by an antagonistic opponent. Let 
H(x, u, J) = sup w$W (x,u) 
. 
g(x, u, w) + "J $ 
f(x, u,w) % 
/ 
. 
Then the equation J! = TJ! is Bellman’s equation for an infinite horizon minimax DP problem. A special case of this mapping arises in zero-sum dynamic games (cf. Example 1.2.4). We will also discuss alternative and more general abstract DP formulations of minimax problems in Chapter 5. 
Example 1.2.6 (Stochastic Shortest Path Problems) 
The stochastic shortest path (SSP for short) problem is the special case of the stochastic optimal control Example 1.2.1 where: 
(a) There is no discounting (" = 1). 
(b) The state space is X = {t, 1, . . . , n} and we are given transition probabilities, denoted by 
pxy(u) = P (xk+1 = y | xk = x, uk = u), x, y " X, u " U(x). 
(c) The control constraint set U(x) is finite for all x " X.
16 Introduction Chap. 1 
(d) A cost g(x, u) is incurred when control u " U(x) is selected at state x. 
(e) State t is a special termination state, which is cost-free and absorbing, i.e., for all u " U(t), 
g(t, u) = 0, ptt(u) = 1. 
To simplify the notation, we have assumed that the cost per stage does not depend on the successor state, which amounts to using expected cost per stage in all calculations. 
Since the termination state t is cost-free, the cost starting from t is zero for every policy. Accordingly, for all cost functions, we ignore the component that corresponds to t, and define 
H(x, u, J) = g(x, u) + 
n # 
y=1 
pxy(u)J(y), x = 1, . . . , n, u " U(x), J " !n. 
The mappings Tµ and T are defined by 
(TµJ)(x) = g $ 
x, µ(x) % 
+ 
n # 
y=1 
pxy $ 
µ(x) % 
J(y), x = 1, . . . , n, 
(TJ)(x) = min u$U(x) 
0 
g(x, u) + 
n # 
y=1 
pxy(u)J(y) 
1 
, x = 1, . . . , n. 
Note that the matrix that has components pxy(u), x, y = 1, . . . , n, is substochastic (some of its row sums may be less than 1) because there may be a positive transition probability from a state x to the termination state t. Consequently Tµ may be a contraction for some µ, but not necessarily for all µ " M. 
The SSP problem has been discussed in many sources, including the books [Pal67], [Der70], [Whi82], [Ber87], [BeT89], [HeL99], [Ber12a], and [Ber17a], where it is sometimes referred to by earlier names such as “first passage problem” and “transient programming problem.” In the framework that is most relevant to our purposes, given in the paper by Bertsekas and Tsitsiklis [BeT91], there is a classification of stationary policies for SSP into proper and improper . We say that µ " M is proper if, when using µ, there is positive probability that termination will be reached after at most n stages, regardless of the initial state; i.e., if 
$µ = max x=1,...,n 
P{xn ,= 0 | x0 = x, µ} < 1. 
Otherwise, we say that µ is improper. It can be seen that µ is proper if and only if in the Markov chain corresponding to µ, each state x is connected to the termination state with a path of positive probability transitions. 
For a proper policy µ, it can be shown that Tµ is a weighted sup-norm contraction, as well as an n-stage contraction with respect to the unweighted
Sec. 1.2 Abstract Dynamic Programming Models 17 
sup-norm. For an improper policy µ, Tµ is not a contraction with respect to any norm. Moreover, T also need not be a contraction with respect to any norm (think of the case where there is only one policy, which is improper). However, T is a weighted sup-norm contraction in the important special case where all policies are proper (see [BeT96], Prop. 2.2, or [Ber12a], Chapter 3). 
Nonetheless, even in the case where there are improper policies and T is not a contraction, results comparable to the case of discounted finite-state MDP are available for SSP problems assuming that: 
(a) There exists at least one proper policy. 
(b) For every improper policy there is an initial state that has infinite cost under this policy. 
Under the preceding two assumptions, referred to as the strong SSP conditions in Section 3.5.1, it was shown in [BeT91] that T has a unique fixed point J!, the optimal cost function of the SSP problem. Moreover, a policy {µ!, µ!, . . .} is optimal if and only if 
Tµ!J ! = TJ!. 
In addition, J! and Jµ can be computed by value iteration, 
J! = lim k%& 
T kJ, Jµ = lim k%& 
T k µJ, 
starting with any J " !n (see [Ber12a], Chapter 3, for a textbook account). These properties are in analogy with the desirable properties (a)-(c), given at the end of the preceding subsection in connection with contractive models. 
Regarding policy iteration, it works in its strongest form when there are no improper policies, in which case the mappings Tµ and T are weighted supnorm contractions. When there are improper policies, modifications to the policy iteration method are needed; see [Ber12a], [YuB13a], and also Section 3.6.2, where these modifications will be discussed in an abstract setting. 
In Section 3.5.1 we will also consider SSP problems where the strong SSP conditions (a) and (b) above are not satisfied. Then we will see that unusual phenomena can occur, including that J! may not be a solution of Bellman’s equation. Still our line of analysis of Chapter 3 will apply to such problems. 
Example 1.2.7 (Deterministic Shortest Path Problems) 
The special case of the SSP problem where the state transitions are deterministic is the classical shortest path problem. Here, we have a graph of n nodes x = 1, . . . , n, plus a destination t, and an arc length axy for each directed arc (x, y). At state/node x, a policy µ chooses an outgoing arc from x. Thus the controls available at x can be identified with the outgoing neighbors of x [the nodes u such that (x, u) is an arc]. The corresponding mapping H is 
H(x, u, J) = & 
axu + J(u) if u ,= t, axt if u = t, 
x = 1, . . . , n. 
A stationary policy µ defines a graph whose arcs are $ 
x, µ(x) % 
, x = 1, . . . , n. The policy µ is proper if and only if this graph is acyclic (it consists of
18 Introduction Chap. 1 
a tree of directed paths leading from each node to the destination). Thus there exists a proper policy if and only if each node is connected to the destination with a directed path. Furthermore, an improper policy has finite cost starting from every initial state if and only if all the cycles of the corresponding graph have nonnegative cycle cost. It follows that the favorable analytical and algorithmic results described for SSP in the preceding example hold if the given graph is connected and the costs of all its cycles are positive. We will see later that significant complications result if the cycle costs are allowed to be zero, even though the shortest path problem is still well posed in the sense that shortest paths exist if the given graph is connected (see Section 3.1). 
Example 1.2.8 (Multiplicative and Risk-Sensitive Models) 
With x, y, u, and transition probabilities pxy(u), as in the finite-state MDP of Example 1.2.2, consider the mapping 
H(x, u, J) = # 
y$X 
pxy(u)g(x, u, y)J(y) = E ! 
g(x, u, y)J(y) | x, u " 
, (1.15) 
where g is a scalar function satisfying g(x,u, y) * 0 for all x, y, u (this is necessary for H to be monotone). This mapping corresponds to the multiplicative model of minimizing over all ! = {µ0, µ1, . . .} the cost 
J!(x0) = lim sup N%& 
E & 
g $ 
x0, µ0(x0), x1 
% 
g $ 
x1, µ1(x1), x2 
% 
· · · 
g $ 
xN"1, µN"1(xN"1), xN 
% ( 
( x0 
' 
, 
(1.16) 
where the state sequence {x0, x1, . . .} is generated using the transition probabilities pxkxk+1 
$ 
µk(xk) % 
. To see that the mappingH of Eq. (1.15) corresponds to the cost function 
(1.16), let us consider the unit function 
J̄(x) - 1, x " X, 
and verify that for all x0 " X, we have 
(Tµ0Tµ1 · · ·TµN"1 J̄)(x0) = E & 
g $ 
x0, µ0(x0), x1 
% 
g $ 
x1, µ1(x1), x2 
% 
· · · 
g $ 
xN"1, µN"1(xN"1), xN 
% ( 
( x0 
' 
, (1.17) 
so that 
J!(x) = lim sup N%& 
(Tµ0Tµ1 · · ·TµN"1 J̄)(x), x " X. 
Indeed, taking into account that J̄(x) - 1, we have 
(TµN"1 J̄)(xN"1) = E ! 
g $ 
xN"1, µN"1(xN"1), xN 
% 
J̄(xN) | xN"1 
" 
= E ! 
g $ 
xN"1, µN"1(xN"1), xN 
% 
| xN"1 
" 
,
Sec. 1.2 Abstract Dynamic Programming Models 19 
(TµN"2TµN"1 J̄)(xN"2) = $ 
(TµN"2(TµN"1 J̄) % 
(xN"2) 
= E ! 
g $ 
xN"2, µN"2(xN"2), xN"1 
% 
·E ! 
g $ 
xN"1, µN"1(xN"1), xN 
% 
| xN"1} | xN"2 
" 
, 
and continuing similarly, 
(Tµ0Tµ1 · · ·TµN"1 J̄)(x0) = E & 
g $ 
x0, µ0(x0), x1 
% 
E ! 
g $ 
x1, µ1(x1), x2 
% 
· · · 
E ! 
g $ 
xN"1, µN"1(xN"1), xN 
% 
| xN"1 
" 
| xN"2 
" 
· · · " 
| x0 
' 
, 
which by using the iterated expectations formula (see e.g., [BeT08]) proves the expression (1.17). 
An important special case of a multiplicative model is when g has the form 
g(x, u, y) = eh(x,u,y) 
for some one-stage cost function h. We then obtain a finite-state MDP with an exponential cost function, 
J!(x0) = lim sup N%& 
E & 
e 
$ 
h(x0,µ0(x0),x1)+···+h(xN"1,µN"1(xN"1),xN ) % 
' 
, 
which is often used to introduce risk aversion in the choice of policy through the convexity of the exponential. 
There is also a multiplicative version of the infinite state space stochastic optimal control problem of Example 1.2.1. The mapping H takes the form 
H(x, u, J) = E ! 
g(x, u, w)J $ 
f(x, u,w) %" 
, 
where xk+1 = f(xk, uk, wk) is the underlying discrete-time dynamic system; cf. Eq. (1.10). 
Multiplicative models and related risk-sensitive models are discussed extensively in the literature, mostly for the exponential cost case and under di"erent assumptions than ours; see e.g., [HoM72], [Jac73], [Rot84], [ChS87], [Whi90], [JBE94], [FlM95], [HeM96], [FeM97], [BoM99], [CoM99], [BoM02], [BBB08], [Ber16a]. The works of references [DeR79], [Pat01], and [Pat07] relate to the stochastic shortest path problems of Example 1.2.6, and are the closest to the semicontractive models discussed in Chapters 3 and 4, based on the author’s paper [Ber16a]; see the next example and Section 3.5.2. 
Example 1.2.9 (A!ne Monotonic Models) 
Consider a finite state space X = {1, . . . , n} and a (possibly infinite) control constraint set U(x) for each state x. For each policy µ, let the mapping Tµ 
be given by TµJ = bµ + AµJ, (1.18) 
where bµ is a vector of !n with components b $ 
x, µ(x) % 
, x = 1, . . . , n, and Aµ 
is an n+ n matrix with components Axy 
$ 
µ(x) % 
, x, y = 1, . . . , n. We assume that b(x, u) and Axy(u) are nonnegative, 
b(x, u) * 0, Axy(u) * 0, & x, y = 1, . . . , n, u " U(x).
20 Introduction Chap. 1 
Thus Tµ and T map nonnegative functions to nonnegative functions J : X () [0,#]. 
This model was introduced in the first edition of this book, and was elaborated on in the author’s paper [Ber16a]. Special cases of the model include the finite-state Markov and semi-Markov problems of Examples 1.2.1-1.2.3, and the stochastic shortest path problem of Example 1.2.6, with Aµ being the transition probability matrix of µ (perhaps appropriately discounted), and bµ being the cost per stage vector of µ, which is assumed nonnegative. An interesting a#ne monotonic model of a di"erent type is the multiplicative cost model of the preceding example, where the initial function is J̄(x) - 1 and the cost accumulates multiplicatively up to reaching a termination state t. In the exponential case of this model, the cost of a generated path starting from some initial state accumulates additively as in the SSP case, up to reaching t. However, the cost of the model is the expected value of the exponentiated cost of the path up to reaching t. It can be shown then that the mapping Tµ 
has the form 
(TµJ)(x) = pxt $ 
µ(x) % 
exp $ 
g(x,µ(x), t) % 
+ 
n # 
y=1 
pxy(µ(x))exp $ 
g(x,µ(x), y) % 
J(y), x " X, 
where pxy(u) is the probability of transition from x to y under u, and g(x, u, y) is the cost of the transition; see Section 3.5.2 for a detailed derivation. Clearly Tµ has the a#ne monotonic form (1.18). 
Example 1.2.10 (Aggregation) 
Aggregation is an approximation approach that simplifies a large dynamic programming (DP) problem by “combining” multiple states into aggregate states. This results in a reduced or “aggregate” problem with fewer states, which can often be solved using exact DP methods. The optimal cost-to-go function derived from this aggregate problem then serves as an approximation of the optimal cost function for the original problem. 
Consider an n-state Markovian decision problem with transition probabilities pij(u). To construct an aggregation framework, we introduce a finite set A of aggregate states. We generically denote the aggregate states by letters such as x and y, and the original system states by letters such as i and j. The approximation framework is constructed by combining in various ways the aggregate states and the original system states to form a larger system (see Fig. 1.2.2). To specify the probabilistic structure of this system, we introduce two (somewhat arbitrary) choices of probability distributions, which relate the original system states with the aggregate states: 
(1) For each aggregate state x and original system state i, we specify the disaggregation probability dxi. We assume that dxi * 0 and 
n # 
i=1 
dxi = 1, & x " A.
Sec. 1.2 Abstract Dynamic Programming Models 21 
according to pij(u), with cost 
dxi 
S 
!jyQ 
, j = 1i 
), x ), y 
Disaggregation Probabilities 
! 
Aggregation Probabilities Disaggregation Probabilities 
Aggregation Probabilities Disaggregation Probabilities 
! 
Aggregation Probabilities Disaggregation Probabilities 
Aggregate System 
Original System 
Figure 1.2.2 Illustration of the relation between aggregate and original system states. 
Roughly, dxi may be interpreted as the “degree to which x is represented by i.” 
(2) For each aggregate state y and original system state j, we specify the aggregation probability %jy . We assume that %jy * 0 and 
# 
y$A 
%jy = 1, & j = 1, . . . , n. 
Roughly, %jy may be interpreted as the “degree of membership of j in the aggregate state y.” 
The aggregation and disaggregation probabilities specify a dynamic system involving both aggregate and original system states (cf. Fig. 1.2.2). In this system: 
(i) From aggregate state x, we generate original system state i according to dxi. 
(ii) We generate transitions from original system state i to original system state j according to pij(u), with cost g(i, u, j). 
(iii) From original system state j, we generate aggregate state y according to %jy. 
Illustrative examples of aggregation frameworks are given in the books [Ber12a] and [Ber17a]. One possibility is hard aggregation, where aggregate states are identified with the sets of a partition of the state space. For another type of common scheme, think of the case where the original system states form a fine grid in some space, which is “aggregated” into a much coarser grid. In particular let us choose a collection of “representative” original system states, and associate each one of them with an aggregate state. Thus, each aggregate state x is associated with a unique representative state ix, and the
22 Introduction Chap. 1 
x j1 j2j2 j3 
x j1 
j3 y1 1 y2 
y2 y3 
y3 Original State Space 
Representative/Aggregate States 
x = i p 
i pij1(u) 
!j1y1 
1 !j1y2 
2 !j1y3 
Figure 1.2.3 Aggregation based on a small subset of representative states (these are shown with larger dark circles, while the other (nonrepresentative) states are shown with smaller dark circles). In this figure, from representative state x = i, there are three possible transitions, to states j1, j2, and j3, according to pij1 (u), pij2 (u), pij3 (u), and each of these states is associated with a convex combination of representative states using the aggregation probabilities. For example, j1 is associated with !j1y1y1+!j1y2y2 +!j1y3y3. 
disaggregation probabilities are 
dxi = & 
1 if i = ix, 0 if i ,= ix. 
(1.19) 
The aggregation probabilities are chosen to represent each original system state j with a convex combination of aggregate/representative states; see Fig. 1.2.3. It is also natural to assume that the aggregation probabilities map representative states to themselves, i.e., 
%jy = & 
1 if j = jy , 0 if j ,= jy . 
This scheme makes intuitive geometrical sense as an interpolation scheme in the special case where both the original and the aggregate states are associated with points in a Euclidean space. The scheme may also be extended to problems with a continuous state space. In this case, the state space is discretized with a finite grid, and the states of the grid are viewed as the aggregate states. The disaggregation probabilities are still given by Eq. (1.19), while the aggregation probabilities may be arbitrarily chosen to represent each original system state with a convex combination of representative states. 
As an extension of the preceding schemes, suppose that through some special insight into the problem’s structure or some preliminary calculation, we know some features of the system’s state that can “predict well” its cost. Then it seems reasonable to form the aggregate states by grouping together
Sec. 1.2 Abstract Dynamic Programming Models 23 
states with “similar features,” or to form aggregate states by using “representative features” instead of representative states. This is called “feature-based aggregation;” see the books [BeT96] (Section 3.1) and [Ber12a] (Section 6.5) for a description and analysis. 
Given aggregation and disaggregation probabilities, we may define an aggregate problem whose states are the aggregate states. This problem involves an aggregate discrete-time system, which we will describe shortly. We require that the control is applied with knowledge of the current aggregate state only (rather than the original system state).† To this end, we assume that the control constraint set U(i) is independent of the state i, and we denote it by U . Then, by adding the probabilities of all the relevant paths in Fig. 1.2.2, it can be seen that the transition probability from aggregate state x to aggregate state y under control u " U is 
p̂xy(u) = 
n # 
i=1 
dxi 
n # 
j=1 
pij(u)%jy . 
The corresponding expected transition cost is given by 
ĝ(x, u) = 
n # 
i=1 
dxi 
n # 
j=1 
pij(u)g(i, u, j). 
These transition probabilities and costs define the aggregate problem. We may compute the optimal costs-to-go Ĵ(x), x " A, of this problem 
by using some exact DP method. Then, the costs-to-go of each state j of the original problem are usually approximated by 
J̃(j) = # 
y$A 
%jy Ĵ(y). 
Example 1.2.11 (Distributed Aggregation) 
The abstract DP framework is useful not only in modeling DP problems, but also in modeling algorithms arising in DP and even other contexts. We illustrate this with an example from Bertsekas and Yu [BeY10] that relates to the distributed solution of large-scale discounted finite-state MDP using cost function approximation based on aggregation. ‡ It involves a partition of the n states into m subsets for the purposes of distributed computation, and yields a corresponding approximation (V1, . . . , Vm) to the cost vector J!. 
In particular, we have a discounted n-state MDP (cf. Example 1.2.2), and we introduce aggregate states S1, . . . , Sm, which are disjoint subsets of 
† An alternative form of aggregate problem, where the control may depend on the original system state is discussed in Section 6.5.2 of the book [Ber12a]. 
‡ See [Ber12a], Section 6.5.2, for a more detailed discussion. Other examples of algorithmic mappings that come under our framework arise in asynchronous policy iteration (see Sections 2.6.3, 3.6.2, and [BeY10], [BeY12], [YuB13a]), and in constrained forms of policy iteration (see [Ber11c], or [Ber12a], Exercise 2.7).
24 Introduction Chap. 1 
the original state space with S1.· · ·.Sn = {1, . . . , n}. We envision a network of processors & = 1, . . . ,m, each assigned to the computation of a local cost function V", defined on the corresponding aggregate state/subset S": 
V" = {V"y | y " S"}. 
Processor & also maintains a scalar aggregate cost R" for its aggregate state, which is a weighted average of the detailed cost values V"x within S": 
R" = # 
x$S" 
d"xV"x, 
where d"x are given probabilities with d"x * 0 and + 
x$S" d"x = 1. The aggre-
gate costs R" are communicated between processors and are used to perform the computation of the local cost functions V" (we will discuss computation models of this type in Section 2.6). 
We denote J = (V1, . . . , Vm, R1, . . . , Rm). We introduce the mapping H(x, u, J) defined for each of the n states x by 
H(x, u, J) = W"(x, u, V", R1, . . . , Rm), if x " S", 
where for x " S" 
W"(x, u, V", R1, . . . , Rm) = 
n # 
y=1 
pxy(u)g(x,u, y) + " # 
y$S" 
pxy(u)V"y 
+ " # 
y/$S" 
pxy(u)Rs(y), 
and for each original system state y, we denote by s(y) the index of the subset to which y belongs [i.e., y " Ss(y)]. 
We may view H as an abstract mapping on the space of J , and aim to find its fixed point J! = (V ! 
1 , . . . , V ! m, R! 
1 , . . . , R ! m). Then, for & = 1, . . . , m, we 
may view V ! " as an approximation to the optimal cost vector of the original 
MDP starting at states x " S", and we may view R! " as a form of aggregate 
cost for S". The advantage of this formulation is that it involves significant decomposition and parallelization of the computations among the processors, when performing various DP algorithms. In particular, the computation of W"(x, u, V", R1, . . . , Rm) depends on just the local vector V", whose dimension may be potentially much smaller than n. 
1.2.4 Reinforcement Learning - Projected and Aggregation Bellman Equations 
Given an abstract DP model described by a mapping H , we may be interested in fixed points of related mappings other than T and Tµ. Such mappings may arise in various contexts, such as for example distributed
Sec. 1.2 Abstract Dynamic Programming Models 25 
asynchronous aggregation in Example 1.2.11. An important context is subspace approximation, whereby Tµ and T are restricted onto a subspace of functions for the purpose of approximating their fixed points. Much of the theory of approximate DP, neuro-dynamic programming, and reinforcement learning relies on such approximations (there are quite a few books, which collectively contain extensive accounts these subjects, such as Bert-sekas and Tsitsiklis [BeT96], Sutton and Barto [SuB98], Gosavi [Gos03], Cao [Cao07], Chang, Fu, Hu, and Marcus [CFH07], Meyn [Mey07], Powell [Pow07], Borkar [Bor08], Haykin [Hay08], Busoniu, Babuska, De Schut-ter, and Ernst [BBD10], Szepesvari [Sze10], Bertsekas [Ber12a], [Ber17a], [Ber19b], [Ber20], and Vrabie, Vamvoudakis, and Lewis [VVL13]). 
For an illustration, consider the approximate evaluation of the cost vector of a discrete-time Markov chain with states i = 1, . . . , n. We assume that state transitions (i, j) occur at time k according to given transition probabilities pij , and generate a cost !kg(i, j), where ! " (0, 1) is a discount factor. The cost function over an infinite number of stages can be shown to be the unique fixed point of the Bellman equation mapping T : &n #$ &n 
whose components are given by 
(TJ)(i) = n # 
j=1 
pij(u) $ 
g(i, j) + !J(j) % 
, i = 1, . . . , n, J " &n. 
This is the same as the mapping T in the discounted finite-state MDP Ex-ample 1.2.2, except that we restrict attention to a single policy. Finding the cost function of a fixed policy is the important policy evaluation subproblem that arises prominently within the context of policy iteration. It also arises in the context of a simplified form of policy iteration, the rollout algorithm; see e.g., [BeT96], [Ber12a], [Ber17a], [Ber19b], [Ber20]. In some artificial intelligence contexts, policy iteration is referred to as self-learning, and in these contexts the policy evaluation is almost always done approximately, sometimes with the use of neural networks. 
A prominent approach for approximation of the fixed point of T is based on the solution of lower-dimensional equations defined on the subspace {#r | r " &s} that is spanned by the columns of a given n's matrix #. Two such approximating equations have been studied extensively (see [Ber12a], Chapter 6, for a detailed account and references; also [BeY07], [BeY09], [YuB10], [Ber11a] for extensions to abstract contexts beyond approximate DP). These are: 
(a) The projected equation 
#r = ""T (#r), (1.20) 
where "" denotes projection onto S with respect to a weighted Eu-clidean norm 
+J+" = 
2 
3 
3 
4 
n # 
i=1 
#i $ 
J(i) %2 
(1.21)
26 Introduction Chap. 1 
with # = (#1, . . . , #n) being a probability distribution with positive components (sometimes a seminorm projection is used, whereby some of the components #i may be zero; see Yu and Bertsekas [YuB12]). 
(b) The aggregation equation 
#r = #DT (#r), (1.22) 
with D being an s' n matrix whose rows are restricted to be probability distributions; these are the disaggregation probabilities of Ex-ample 1.2.10. Also, in this approach, the rows of # are restricted to be probability distributions; these are the aggregation probabilities of Example 1.2.10. 
We now see that solving the projected equation (1.20) and the aggregation equation (1.22) amounts to finding a fixed point of the mappings ""T and #DT , respectively. These mappings derive their structure from the DP operator T , so they have some DP-like properties, which can be exploited for analysis and computation. 
An important fact is that the aggregation mapping #DT preserves the monotonicity and the sup-norm contraction property of T , while the projected equation mapping ""T generally does not. The reason for preservation of monotonicity is the nonnegativity of the components of the matrices # and D (see the author’s survey paper [Ber11c] for a discussion of the importance of preservation of monotonicity in various DP operations). The reason for preservation of sup-norm contraction is that the matrices # and D are sup-norm nonexpansive, because their rows are probability distributions. In fact, it can be verified that the solution r of Eq. (1.22) can be viewed as the exact DP solution of the “aggregate” DP problem that represents a lower-dimensional approximation of the original (see Ex-ample 1.2.10). The preceding observations are important for our purposes, as they indicate that much of the theory developed in this book applies to approximation-related mappings based on aggregation. 
By contrast, the projected equation mapping ""T need not be monotone, because the components of "" need not be nonnegative. Moreover while the projection "" is nonexpansive with respect to the projection norm +·+", it need not be nonexpansive with respect to the sup-norm. As a result the projected equation mapping ""T need not be a sup-norm contraction. These facts play a significant role in approximate DP methodology. 
1.2.5 Reinforcement Learning - Temporal Di"erence and Proximal Algorithms 
An important possibility for finding a fixed point of T is to replace T with another mapping, say F , such that F and T have the same fixed points. For example, F may o!er some advantages in terms of algorithmic convenience or quality of approximation when used in conjunction with
Sec. 1.2 Abstract Dynamic Programming Models 27 
projection or aggregation [cf. Eqs. (1.20) and (1.22)]. Alternatively, F may be the mapping of some iterative method that is suitable for computing fixed points of T . 
In this book we will not consider in much detail the possibility of using an alternative mapping F to find a fixed point of a mapping T . We will just mention here some multistep versions of T , which have been used widely for approximations in reinforcement learning. An important example is the mapping T (#) : &n #$ &n, defined for a given $ " (0, 1) as follows: T (#) 
transforms a vector J " &n to the vector T (#)J " &n, whose n components are given by 
$ 
T (#)J % 
(i) = (1, $) " # 
$=0 
$$(T $+1J)(i), i = 1, . . . , n, J " &n, 
for $ " (0, 1), where T $ is the %-fold composition of T with itself % times. Here there should be conditions that guarantee the convergence of the infinite series in the preceding definition. The multistep analog of the projected Eq. (1.20) is 
#r = ""T (#)(#r). 
The popular temporal di!erence methods, such as TD($), LSTD($), and LSPE($), aim to solve this equation (see the book references on approximate DP, neuro-dynamic programming, and reinforcement learning cited earlier). The mapping T (#) also forms the basis for the $-policy iteration method to be discussed in Sections 2.5, 3.2.4, and 4.3.3. 
The multistep analog of the aggregation Eq. (1.22) is 
#r = #DT (#)(#r), 
and methods that are similar to the temporal di!erence methods can be used for its solution. In particular, a multistep method based on the mapping T (#) is the, so-called, $-aggregation method (see [Ber12a], Chapter 6), as well as other forms of aggregation (see [Ber12a], [YuB12]). 
In the case where T is a linear mapping of the form 
TJ = AJ + b, 
where b is a vector in &n, and A is an n ' n matrix with eigenvalues strictly within the unit circle, there is an interesting connection between the multistep mapping T (#) and another mapping of major importance in numerical convex optimization. This is the proximal mapping, associated with T and a scalar c > 0, and denoted by P (c). In particular, for a given J " &n, the vector P (c)J is defined as the unique vector Y " &n that solves the equation 
Y ,AY , b = 1 
c (J , Y ).
28 Introduction Chap. 1 
Equivalently, 
P (c)J = 
5 
c+ 1 
c I ,A 
6#15 
b+ 1 
c J 
6 
, (1.23) 
where I is the identity matrix. Then it can be shown (see Exercise 1.2 or the papers [Ber16b], [Ber18c]) that if 
c = $ 
1, $ , 
we have T (#) = T · P (c) = P (c) · T. 
Moreover, the vectors J , P (c)J , and T (#)J are colinear and satisfy 
T (#)J = J + c+ 1 
c 
$ 
P (c)J , J % 
. 
The preceding formulas show that T (#) and P (c) are closely related, and that iterating with T (#) is “faster” than iterating with P (c), since the eigenvalues of A are within the unit circle, so that T is a contraction. In addition, methods such as TD($), LSTD($), LSPE($), and their projected versions, which are based on T (#), can be adapted to be used with P (c). 
A more general form of multistep approach, introduced and studied in the paper [YuB12], replaces T (#) with a mapping T (w) : &n #$ &n that has components 
$ 
T (w)J % 
(i) = " # 
$=1 
wi$(T $J)(i), i = 1, . . . , n, J " &n, 
where w is a vector sequence whose ith component, (wi1, wi2, . . .), is a probability distribution over the positive integers. Then the multistep analog of the projected equation (1.20) is 
#r = ""T (w)(#r), (1.24) 
while the multistep analog of the aggregation equation (1.22) is 
#r = #DT (w)(#r). (1.25) 
The mapping T (#) is obtained for wi$ = (1 , $)$$#1, independently of the state i. A more general version, where $ depends on the state i, is obtained for wi$ = (1 , $i)$ 
$#1 i . The solution of Eqs. (1.24) and (1.25) 
by simulation-based methods is discussed in the paper [YuB12]; see also Exercise 1.3. 
Let us also note that there is a connection between projected equations of the form (1.24) and aggregation equations of the form (1.25). This connection is based on the use of a seminorm [this is given by the same expression as the norm + · +" of Eq. (1.21), with some of the components of # allowed to be 0]. In particular, the most prominent cases of aggregation equations can be viewed as seminorm projected equations because, for these cases, #D is a seminorm projection (see [Ber12a], p. 639, [YuB12], Section 4). Moreover, they can also be viewed as projected equations where the projection is oblique (see [Ber12a], Section 7.3.6).
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 29 
1.3 REINFORCEMENT LEARNING - APPROXIMATION IN VALUE SPACE 
In this section we will use geometric illustrations to obtain insight into Bell-man’s equation, the algorithms of value iteration (VI) and policy iteration (PI), and an approximation methodology, which is prominent in reinforcement learning and is known as approximation in value space.† Throughout this section, we will make use of the following two properties: 
(a) T and Tµ are monotone, i.e., they satisfy Assumption 1.2.1. 
(b) We have (TJ)(x) = min 
µ!M (TµJ)(x), for all x, (1.26) 
where M is the set of stationary policies. This is true because for any policy µ, there is no coupling constraint between the controls µ(x) and µ(x") that correspond to two di!erent states x and x". 
We will first focus on the discounted version of the Markovian decision problem of Example 1.2.1, and we will then consider more general cases. 
1.3.1 Approximation in Value Space for Markovian Decision Problems 
In Markovian decision problems the mappings Tµ and T are given by 
(TµJ)(x) = E ! 
g " 
x, µ(x), w # 
+ !J " 
f(x, µ(x), w) # 
$ 
, for all x, (1.27) 
and 
(TJ)(x) = inf u!U(x) 
E ! 
g(x, u, w) + !J " 
f(x, u, w) # 
$ 
, for all x, (1.28) 
where ! ! (0, 1]; cf. Example 1.2.1. In addition to monotonicity, we have an additional important prop-
erty: Tµ is linear , in the sense that it has the form 
TµJ = Gµ +AµJ, 
where Gµ ! R(X) is some function and Aµ : R(X) "# R(X) is an operator such that for any functions J1, J2, and scalars "1, "2, we have 
Aµ("1J1 + "2J2) = "1AµJ1 + "2AµJ2. 
† The major alternative reinforcement learning approach is approximation in policy space, whereby a suboptimal policy is selected from within a class of 
parametrized policies, usually by means of some optimization procedure, such as 
random search, or gradient descent; see e.g., the author’s reinforcement learning book [Ber19b].
30 Introduction Chap. 1 
This is true because of the linearity of the expected value operation in Eq. (1.27). The linearity of Tµ implies another important property: (TJ)(x) is a concave function of J for every x. By this we mean that the set 
Cx = ! 
(J, #) | (TJ)(x) ( #, J " R(X), # " & " 
(1.29) 
is convex for all x " X , where R(X) is the set of real-valued functions over the state space X , and & is the set of real numbers. This follows from the linearity of Tµ, the alternative definition of T given by Eq. (1.26), and the fact that for a fixed x, the minimum of the linear functions (TµJ)(x) over µ " M is concave as a function of J . 
We illustrate these properties graphically with an example. 
Example 1.3.1 (A Two-State and Two-Control Example) 
Assume that there are two states 1 and 2, and two controls u and v. Consider the policy µ that applies control u at state 1 and control v at state 2. Then the operator Tµ takes the form 
(TµJ)(1) = 
2 # 
y=1 
p1j(u) $ 
g(1, u, y) + "J(y) % 
, (1.30) 
(TµJ)(2) = 
2 # 
y=1 
p2y(v) $ 
g(2, v, y) + "J(y) % 
, (1.31) 
where pxy(u) and pxy(v) are the probabilities that the next state will be y, when the current state is x, and the control is u or v, respectively. Clearly, (TµJ)(1) and (TµJ)(2) are linear functions of J . Also the operator T of the Bellman equation J = TJ takes the form 
(TJ)(1) = min 
0 
2 # 
y=1 
p1y(u) $ 
g(1, u, y) + "J(y) % 
, 
2 # 
y=1 
p1y(v) $ 
g(1, v, y) + "J(y) % 
1 
, 
(1.32) 
(TJ)(2) = min 
0 
2 # 
y=1 
p2y(u) $ 
g(2, u, y) + "J(y) % 
, 
2 # 
y=1 
p2y(v) $ 
g(2, v, y) + "J(y) % 
1 
. 
(1.33) 
Thus, (TJ)(1) and (TJ)(2) are concave and piecewise linear as functions of the two-dimensional vector J (with two pieces; more generally, as many linear pieces as the number of controls). This concavity property holds in general
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 31 
since (TJ)(x) is the minimum of a collection of linear functions of J , one for each u " U(x). Figure 1.3.1 illustrates (TµJ)(1) for the cases where µ(1) = u and µ(1) = v, (TµJ)(2) for the cases where µ(2) = u and µ(2) = v, (TJ)(1), and (TJ)(2), as functions of J = 
$ 
J(1), J(2) % 
. 
Critical properties from the DP point of view are whether T and Tµ 
have fixed points; equivalently, whether the Bellman equations J = TJ and J = TµJ have solutions within the class of real-valued functions, and whether the set of solutions includes J* and Jµ, respectively. It may thus be important to verify that T or Tµ are contraction mappings. This is true for example in the benign case of discounted problems (! < 1) with bounded cost per stage. However, for undiscounted problems, asserting the contraction property of T or Tµ may be more complicated, and even impossible. In this book we will deal extensively with such questions and related issues regarding the solution set of the Bellman equation. 
Geometrical Interpretations 
We will now interpret the Bellman operators geometrically, starting with Tµ, which is linear as noted earlier. Figure 1.3.2 illustrates its form. Note here that the functions J and TµJ are multidimensional. They have as many scalar components J(x) and (TµJ)(x), respectively, as there are states x, but they can only be shown projected onto one dimension. The cost function Jµ satisfies Jµ = TµJµ, so it is obtained from the intersection of the graph of TµJ and the 45 degree line, when Jµ is real-valued. We interpret the situation where Jµ is not real-valued with lack of system stability under µ [so µ will be viewed as unstable if we have Jµ(x) = -for some initial states x]. For further discussion of stability issues, see the book [Ber22]. 
The form of the Bellman operator T is illustrated in Fig. 1.3.3. Again the functions J , J*, TJ , TµJ , etc, are multidimensional, but they are shown projected onto one dimension. The Bellman equation J = TJ may have one or many real-valued solutions. It may also have no real-valued solution in exceptional situations, as we will discuss later. The figure assumes that the Bellman equations J = TJ and J = TµJ have a unique real-valued solution, which is true if T and Tµ are contraction mappings, as is the case for discounted problems with bounded cost per stage. Otherwise, these equations may have no solution or multiple solutions within the class of real-valued functions. The equation J = TJ typically has J* as a solution, but may have more than one solution in cases where either ! = 1 or ! < 1, and the cost per stage is unbounded. 
Example 1.3.2 (A Two-State and Infinite Controls Problem) 
Let us consider the mapping T for a problem that involves two states, 1 and 2, but an infinite number of controls. In particular, the control space at both
32 Introduction Chap. 1 
State 1 State 2 State 1 State 2 
One-step lookahead J! 
! J!(1) 
(2) (TJ!)(1) = J!(1) ( 
One-step lookahead J! 
(1) J!(2) 
(1) (TJ!)(2) = J!(2) 
Figure 1.3.1 Geometric illustrations of the Bellman operators Tµ and T for states 1 and 2 in Example 1.3.1; cf. Eqs. (1.30)-(1.33). The problem’s transition probabilities are: p11(u) = 0.3, p12(u) = 0.7, p21(u) = 0.4, p22(u) = 0.6, p11(v) = 0.6, p12(v) = 0.4, p21(v) = 0.9, p22(v) = 0.1. The stage costs are g(1, u, 1) = 3, g(1, u, 2) = 10, g(2, u, 1) = 0, g(2, u, 2) = 6, g(1, v, 1) = 7, g(1, v, 2) = 5, g(2, v, 1) = 3, g(2, v, 2) = 12. The discount factor is " = 0.9, and the optimal costs are J!(1) = 50.59 and J!(2) = 47.41. The optimal policy is µ!(1) = v 
and µ!(2) = u. The figure also shows the one-dimensional “slices” of T that pass through J!.
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 33 
1 J J 
1 J J 
45!Line 
TµJ 
Cost of µ 
Player/Policy Jµ = TµJµ 
(1) = 0 
Generic stable policy Generic stable policy µJ Generic unstable policy 
Generic unstable policy µ! 
Tµ!J 
Figure 1.3.2 Geometric interpretation of the linear Bellman operator Tµ and the corresponding Bellman equation. The graph of Tµ is a plane in the space !"!, and when projected on a one-dimensional plane that corresponds to a single state and passes through Jµ, it becomes a line. Then there are three cases: 
(a) The line has slope less than 45 degrees, so it intersects the 45-degree line at a unique point, which is equal to Jµ, the solution of the Bellman equation J = TµJ . This is true if Tµ is a contraction mapping, as is the case for discounted problems with bounded cost per stage. 
(b) The line has slope less than 45 degrees. Then it intersects the 45-degree line at a unique point, which is a solution of the Bellman equation J = TµJ , but is not equal to Jµ. Then Jµ is not real-valued; we consider such µ to be unstable under µ. 
(c) The line has slope exactly equal to 45 degrees. This is an exceptional case where the Bellman equation J = TµJ has an infinite number of real-valued solutions or no real-valued solution at all; we will provide examples where this occurs later. 
states is the unit interval, U(1) = U(2) = [0, 1]. Here (TJ)(1) and (TJ)(2) are given by 
(TJ)(1) = min u$[0,1] 
! 
g1 + r11u 2 + r12(1$ u)2 + "uJ(1) + "(1$ u)J(2) 
" 
, 
(TJ)(2) = min u$[0,1] 
! 
g2 + r21u 2 + r22(1$ u)2 + "uJ(1) + "(1$ u)J(2) 
" 
.
34 Introduction Chap. 1 
J J! = TJ! 
0 Prob. = 1 1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
45!Line 
TµJ 
Cost of µ 
TJ = minµ TµJ 
Final Features Optimal Policy Final Features Optimal Policy 
J̃ 
Position Evaluation Policy µ̃ withON-LINE PLAY Lookahead Tree States 
Tµ̃J̃ = T J̃ 
One-step lookahead 
One-step lookahead Generic policy µ 
= 4 Model minµ TµJ̃ 
Player/Policy Jµ = TµJµ 
(1) = 0 
Tµ̃J 
ective Cost Approximation Value Space Approximation Cost of µ̃ Jµ̃ = Tµ̃Jµ̃ 
Figure 1.3.3 Geometric interpretation of the Bellman operator T , and the corresponding Bellman equation. For a fixed x, the function (TJ)(x) can be written as minµ(TµJ)(x), so it is concave as a function of J . The optimal cost function J! satisfies J! = TJ!, so it is obtained from the intersection of the graph of TJ 
and the 45 degree line shown, assuming J! is real-valued. Note that the graph of T lies below the graph of every operator Tµ, and 
is in fact obtained as the lower envelope of the graphs of Tµ as µ ranges over the set of policies M. In particular, for any given function J̃ , for every x, the value (T J̃)(x) is obtained by finding a support hyperplane/subgradient of the graph of the concave function (T J)(x) at J̃ , as shown in the figure. This support hyperplane is defined by the control µ(x) of a policy µ̃ that attains the minimum of (TµJ̃)(x) over µ: 
µ̃(x) # arg min µ$M 
(TµJ̃)(x) 
(there may be multiple policies attaining this minimum, defining multiple support hyperplanes). This construction also shows how the minimization 
(T J̃)(x) = min µ$M 
(TµJ̃)(x) 
corresponds to a linearization of the mapping T at the point J̃ . 
The control u at each state x = 1, 2 has the meaning of a probability that we must select at that state. In particular, we control the probabilities u and (1$u) of moving to states y = 1 and y = 2, at a control cost that is quadratic in u and (1$ u), respectively. For this problem (TJ)(1) and (TJ)(2) can be calculated in closed form, so they are easy to plot and understand. They are piecewise quadratic, unlike the corresponding plots of Fig. 1.3.1, which are piecewise linear; see Fig. 1.3.4.
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 35 
State 1 State 2 
One-step lookahead J! One-step lookahead J! 
! J!(1) (1) J!(2) 
(2) (TJ!)(1) = J!(1) ( (1) (TJ!)(2) = J!(2) 
Figure 1.3.4 Illustration of the Bellman operator T for states 1 and 2 in Example 1.3.2. The parameter values are g1 = 5, g2 = 3, r11 = 3, r12 = 15, r21 = 9, r22 = 1, and the discount factor is " = 0.9. The optimal costs are J!(1) = 49.7 and J!(2) = 40.0, and the optimal policy is µ!(1) = 0.59 and µ!(2) = 0. The figure also shows the one-dimensional slices of the operators at J(1) = 15 and J(2) = 30, together with the corresponding 45-degree lines. 
Visualization of Value Iteration 
The operator notation simplifies algorithmic descriptions, derivations, and proofs related to DP. For example, the value iteration (VI) algorithm can be written in the compact form 
Jk+1 = TJk, k = 0, 1, . . . , 
as illustrated in Fig. 1.3.5. Moreover, the VI algorithm for a given policy µ can be written as 
Jk+1 = TµJk, k = 0, 1, . . . , 
and it can be similarly interpreted, except that the graph of the function TµJ is linear. Also we will see shortly that there is a similarly compact description for the policy iteration algorithm. 
1.3.2 Approximation in Value Space and Newton’s Method 
Let us now interpret approximation in value space in terms of abstract geometric constructions. Here we approximate J* with some function J̃ , and we obtain by minimization a corresponding policy, called a one-step lookahead policy. In particular, for a given J̃ , a one-step lookahead policy µ̃ is characterized by the equation 
Tµ̃J̃ = T J̃,
36 Introduction Chap. 1 
J J! = TJ! 
0 Prob. = 1 1 J J 
1 J J 
J0 J1 
J1 
J2 
J2 
Optimal cost Cost of rollout policy ˜ 
TJ 
45!Line 
provement Bellman Equation Value Iterations 
Stability Region 0 
Figure 1.3.5 Geometric interpretation of the VI algorithm Jk+1 = TJk, starting from some initial function J0. Successive iterates are obtained through the staircase construction shown in the figure. The VI algorithm Jk+1 = TµJk for a given policy µ can be similarly interpreted, except that the graph of the function TµJ is linear. 
as in Fig. 1.3.6. This equation implies that the graph of Tµ̃J just touches the graph of TJ at J̃ , as shown in the figure. Moreover, for each state x " X the hyperplane Hµ̃(x) 
Hµ̃(x) = & 
$ 
J(x), # % 
| (Tµ̃J)(x) ( # ' 
, 
supports from above the convex set & 
$ 
J(x), # % 
| (TJ)(x) ( # ' 
at the point $ 
J̃(x), (T J̃)(x) % 
and defines a subgradient of (TJ)(x) at J̃ . Note that the one-step lookahead policy µ̃ need not be unique, since T need not be di!erentiable. 
In conclusion, the equation 
J = Tµ̃J 
is a pointwise (for each x) linearization of the equation 
J = TJ
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 37 
J J! = TJ! 
0 Prob. = 1 
1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
TJ 
Tµ̃J 
J̃ Jµ̃ = Tµ̃Jµ̃ 
One-Step Lookahead Policy Cost l One-Step Lookahead Policy Cost l 
One-Step Lookahead Policy Cost One-Step Lookahead Policy µ̃ 
Corresponds to One-Step Lookahead Policy ˜ 
Stability Region 0 J̃ 
Cost Approximation Value Spac Ap roxim tion 
Newton step from J̃ 
J̃ for solving J = TJ 
Approximations Result ofalso Newton Step 
Figure 1.3.6 Geometric interpretation of approximation in value space and the one-step lookahead policy µ̃ as a step of Newton’s method. Given J̃ , we find a policy µ̃ that attains the minimum in the relation 
T J̃ = min µ 
TµJ̃ . 
This policy satisfies T J̃ = Tµ̃J̃ , so the graph of TJ and Tµ̃J touch at J̃ , as shown. It may not be unique. Because TJ has concave components, the equation 
J = Tµ̃J 
is the linearization of the equation J = TJ at J̃ . The linearized equation is solved at the typical step of Newton’s method to provide the next iterate, which is just Jµ̃. 
at J̃ , and its solution, Jµ̃, can be viewed as the result of a Newton iteration at the point J̃ . In summary, the Newton iterate at J̃ is Jµ̃, the solution of the linearized equation J = Tµ̃J .† 
We may also consider approximation in value space with %-step looka-
† The classical Newton’s method for solving a fixed point problem of the form y = T (y), where y is an n-dimensional vector, operates as follows: At the current iterate yk, we linearize T and find the solution yk+1 of the corresponding linear fixed point problem. Assuming T is di"erentiable, the linearization is obtained
38 Introduction Chap. 1 
head using J̃ . This is the same as approximation in value space with onestep lookahead using the (% , 1)-fold operation of T on J̃ , T $#1J̃ . Thus it can be interpreted as a Newton step starting from T $#1J̃ , the result of %, 1 value iterations applied to J̃ . This is illustrated in Fig. 1.3.7.† 
1.3.3 Policy Iteration and Newton’s Method 
Another major class of infinite horizon algorithms is based on policy iteration (PI for short). We will discuss several abstract versions of PI in subsequent chapters, under a variety of assumptions. Generally, each iteration of the PI algorithm starts with a policy (which we call current or base policy), and generates another policy (which we call new or rollout policy, respectively). For the stochastic optimal control problem of Example 1.2.1, given the base policy µ, a policy iteration consists of two phases: 
by using a first order Taylor expansion: 
yk+1 = T (yk) + 'T (yk) 
'y (yk+1 $ yk), 
where 'T (yk)/'y is the n + n Jacobian matrix of T evaluated at the vector yk. The most commonly given convergence rate property of Newton’s method is quadratic convergence. It states that near the solution y!, we have 
/yk+1 $ y!/ = O $ 
/yk $ y!/2 % 
, 
where / · / is the Euclidean norm, and holds assuming the Jacobian matrix exists and is Lipschitz continuous (see [Ber16], Section 1.4). There are extensions of Newton’s method that are based on solving a linearized system at the current iterate, but relax the di"erentiability requirement to piecewise di"erentiability, and/or component concavity, while maintaining the superlinear convergence property of the method. 
The structure of the Bellman operators (1.28) and (1.27), with their mono-
tonicity and concavity properties, tends to enhance the convergence and rate of 
convergence properties of Newton’s method, even in the absence of di"erentiability, as evidenced by the convergence analysis of PI, and the extensive favorable 
experience with rollout, PI, and MPC. In this connection, it is worth noting that 
in the case of Markov games, where the concavity property does not hold, the PI method may oscillate, as shown by Pollatschek and Avi-Itzhak [PoA69], and 
needs to be modified to restore its global convergence; see the author’s paper [Ber21c]. We will discuss abstract versions of game and minimax contexts n 
Chapter 5. 
† Variants of Newton’s method that involve combinations of first order iterative methods, such as the Gauss-Seidel and Jacobi algorithms, and New-
ton’s method, and they belong to the general family of Newton-SOR methods 
(SOR stands for “successive over-relaxation”); see the classic book by Ortega and Rheinboldt [OrR70] (Section 13.4).
Sec. 1.3 Reinforcement Learning - Approximation in Value Space 39 
J J! = TJ! 
0 Prob. = 1 
1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
TJ 
J̃ 
Tµ̃J 
J̃ Jµ̃ = Tµ̃Jµ̃ 
One-Step Lookahead Policy Cost l 
One-Step Lookahead Policy µ̃ 
Corresponds to One-Step Lookahead Policy ˜ 
Stability Region 0 
Multistep Lookahead Policy Cost l 
Multistep Lookahead Policy Cost 
Cost Approximation Value Space Approximation 
Cost Approximation Value Space Approximation 
Multistep Lookahead Policy Cost T 2J̃ 
E!ective Cost Approximation Value Space Approximation 
J̃ for solving J = TJ 
Newton step from T !!1J̃ 
Approximations Result of 
Linear policy parameter Optimal ! = 3 
also Newton Step 
Figure 1.3.7 Geometric interpretation of approximation in value space with #-step lookahead (in this figure # = 3). It is the same as approximation in value space with one-step lookahead using T ""1J̃ as cost approximation. It can be viewed as a Newton step at the point T ""1J̃ , the result of # $ 1 value iterations applied to J̃. Note that as # increases the cost function Jµ̃ of the #-step lookahead policy µ̃ approaches more closely the optimal J!, and that lim"%& Jµ̃ = J!. 
(a) Policy evaluation, which computes the cost function Jµ. One possibility is to solve the corresponding Bellman equation 
Jµ(x) = E & 
g $ 
x, µ(x), w % 
+ !Jµ $ 
f(x, µ(x), w) % 
' 
, for all x. 
(1.34) However, the value Jµ(x) for any x can also be computed by Monte Carlo simulation, by averaging over many randomly generated trajectories the cost of the policy starting from x. Other possibilities include the use of specialized simulation-based methods, based on the projected and aggregation Bellman equations discussed in Sec-tion 1.2.4, for which there is extensive literature (see e.g., the books [BeT96], [SuB98], [Ber12a], [Ber19b]). 
(b) Policy improvement , which computes the rollout policy µ̃ using the one-step lookahead minimization 
µ̃(x) " arg min u$U(x) 
E & 
g(x, u, w) + !Jµ $ 
f(x, u, w) % 
' 
, for all x. 
(1.35)
40 Introduction Chap. 1 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Optimal cost Cost of rollout policy ˜ 
Policy Evaluation for 
Cost of µkCost of µk+1 
J µk = T 
µkJµkJ µk+1 = T 
µk+1Jµk+1 
Linearized Bellman Eq. at Linearized Bellman Eq. at J 
µk 
for µk+1 
also Newton Step 
Figure 1.3.8 Geometric interpretation of a single policy iteration. Starting from the stable current policy µk , it evaluates the corresponding cost function Jµk , 
and computes the next policy µk+1 according to Tµk+1Jµk = TJµk . The corresponding cost function Jµk+1 is obtained as the solution of the linearized equation J = Tµk+1J , so it is the result of a Newton step for solving the Bellman equation J = TJ , starting from Jµk . Note than in policy iteration, the Newton step always starts at a function Jµ, which satisfies Jµ % J!. 
It is generally expected (and can be proved under mild conditions) that the rollout policy is improved in the sense that Jµ̃(x) ) Jµ(x) for all x. 
Thus the PI process generates a sequence of policies {µk}, by obtaining µk+1 through a policy improvement operation using Jµk in place of Jµ in Eq. (1.35), which is obtained through policy evaluation of the preceding policy µk using Eq. (1.34). In subsequent chapters, we will show under appropriate assumptions that general forms of PI have interesting and often solid convergence properties, which may hold even when the method is implemented (with appropriate modifications) in unconventional computing environments, involving asynchronous distributed computation. 
In terms of our abstract notation, the PI algorithm can be written in a compact form. For the generated policy sequence {µk}, the policy evaluation phase obtains Jµk from the equation 
Jµk = TµkJµk , (1.36) 
while the policy improvement phase obtains µk+1 through the equation 
Tµk+1Jµk = TJµk . (1.37)
Sec. 1.4 Organization of the Book 41 
As Fig. 1.3.8 illustrates, PI can be viewed as Newton’s method for solving the Bellman equation in the function space of cost functions J . In particular, the policy improvement Eq. (1.37) is the Newton step starting from Jµk , and yields µk+1 as the corresponding one-step lookahead/rollout policy. 
The interpretation of PI as a form of Newton’s method has a long history, for which we refer to the original works for linear quadratic problems by Kleinman [Klei68],† and for finite-state infinite horizon discounted and Markov game problems by Pollatschek and Avi-Itzhak [PoA69] (who also showed that the method may oscillate in the game case; see the discussion in Chapter 5). 
1.3.4 Approximation in Value Space for General Abstract Dynamic Programming 
Let us now consider the general case where the mapping Tµ is not assumed linear for all stationary policies µ ! M. In this case we still have the alternative description of T 
(TJ)(x) = min µ!M 
(TµJ)(x), for all x, 
but T need not be concave, i.e., for some x ! X , the function (TJ)(x) may not be concave as a function of J . We illustrate this fact in Fig. 1.3.9. 
The nonlinearity of the mapping Tµ can have profound consequences on the validity of the PI algorithm and its interpretation in terms of New-ton’s method. A prominent case where this is so arises in minimax problems and related two-person zero sum game settings (cf. Example 1.2.5). We will discuss this case in Chapter 5, where we will introduce modifications to the PI algorithm that restore its convergence property. 
We note, however, that it is possible that the mappings Tµ are nonlinear and convex, but that T has concave and di!erentiable components (TJ)(x), in which case the Newton step interpretation applies. This occurs in particular in the important case of zero-sum dynamic games involving a linear system and a quadratic cost function. 
1.4 ORGANIZATION OF THE BOOK 
The examples in the preceding sections demonstrate that while the monotonicity assumption is satisfied for most DP models, the contraction assumption may or may not hold. In particular, the contraction assumption 
† This was part of Kleinman’s Ph.D. thesis [Kle67] at M.I.T., supervised by M. Athans. Kleinman gives credit for the one-dimensional version of his results to 
Bellman and Kalaba [BeK65]. Note also that the first proposal of the PI method 
was given by Bellman in his classic book [Bel57], under the name “approximation in policy space.”
42 Introduction Chap. 1 
1 J J 
TµJ 
(1) = 0 
Tµ!J 
TJ = min{Tµ, Tµ!} 
Figure 1.3.9 Geometric interpretation of the Bellman operator, in the general case where the policy mappings Tµ are not linear. The figure illustrates the case of two policies µ and µ#, whose mappings Tµ and Tµ! are piecewise linear and 
convex. In this case the mapping T , given by (TJ)(x) = min ! 
TµJ(x), Tµ!J(x) " 
, 
is piecewise linear, but it is neither convex nor concave, and the Newton step interpretation breaks down; see also Chapter 5. 
is satisfied for the mapping H in Examples 1.2.1-1.2.5, provided there is discounting and that the cost per stage is bounded. However, it need not hold in the SSP Example 1.2.6, the multiplicative Example 1.2.8, and the a$ne monotonic Example 1.2.9. 
The book’s central theme is that the presence or absence of monotonicity and contraction fundamentally shapes the analytical and algorithmic theories for abstract DP. In our development, with few exceptions, we will assume that monotonicity holds. Consequently, the book is organized around the presence or absence of the contraction property. In the next three chapters we will discuss three types of DP models. 
(a) Contractive models: These models, discussed in Chapter 2, have the richest and strongest algorithmic theory, and serve as a benchmark for other models. Notable examples include discounted stochastic optimal control problems (cf. Example 1.2.1), finite-state discounted MDP (cf. Example 1.2.2), and some special types of SSP problems (cf. Example 1.2.6). 
(b) Semicontractive models: In these models, Tµ is monotone but is not a contraction for all µ " M. Most practical deterministic, stochastic, and minimax-type shortest path problems fall into this
Sec. 1.4 Organization of the Book 43 
category. One challenge here is that, under certain conditions, some of the problem’s cost functions may take the values +- or ,-, and the mappings Tµ and T must be able to deal with such functions. 
The distinguishing feature of semicontractive models is the separation of policies into those that “behave well” within our optimization framework and those that do not. Contraction-based analysis is insu$cient to deal with “ill-behaved” policies, so we introduce a notion of “regularity,” which is connected to contraction, but is more general. In particular, a policy µ is considered “regular” if the dynamic system underlying Tµ has Jµ has an asymptotically stable equilibrium within a suitable domain. Our models and analysis are patterned to a large extent after the SSP problems of Example 1.2.6 (the regular µ correspond to the proper policies). We show that the (restricted) optimal cost function over just the regular policies can typically be obtained with value and policy iteration algorithms. By contrast, the optimal cost function over all policies J* may not be obtainable by these algorithms, and indeed J* may not even be a solution of Bell-man’s equation, as we will show with a simple example in Section 3.1.2. 
The key idea is that under certain conditions, the restricted optimization (the one that optimizes over the regular policies only) is well behaved, both analytically and algorithmically. Under additional conditions, which directly or indirectly ensure the existence of an optimal regular policy, we obtain semicontractive models with properties nearly as robust as contractive models. 
In Chapter 3, we develop the basic theory of semicontractive models for the case where the regular policies are stationary, while in Chapter 4 (Section 4.4), we extend the notion of regularity to nonstationary policies. Moreover, we illustrate the theory with a variety of interesting shortest path-type problems (stochastic, minimax, a$ne monotonic, and risk sensitive/exponential cost), linear-quadratic optimal control problems, and deterministic and stochastic optimal control problems. 
(c) Noncontractive models: These models rely on just the monotonicity property of Tµ, and are more complex than the preceding ones. Like semicontractive models, the problem’s cost functions may take the values of +- or ,-, and in fact the optimal cost function may take the values - and ,- as a matter of course (rather than on an exceptional basis, as in semicontractive models). This complexity presents considerable challenges, as much of the contractive model theory either does not extend or does so in a weaker form only. For instance, the fixed point equation J = TJ may lack a unique solution, value iteration may succeed starting with some functions but
44 Introduction Chap. 1 
not with others, and policy iteration may fail altogether. Some of these issues may be mitigated when additional structure is present, which we discuss in Sections 4.4-4.6, focusing on noncontractive models that also have some semicontractive structure, and corresponding favorable properties. 
Examples of DP problems from each of the model categories above, primarily special cases of the specific DP models discussed in Section 1.2, are scattered throughout the book. They serve both to illustrate the theory and its exceptions, and to highlight the beneficial role of additional special structure. 
We finally note some other types of models where there are restrictions to the set of policies, i.e., M may be a strict subset of the set of functions µ : X #$ U with µ(x) " U(x) for all x " X . Such restrictions may include measurability (needed to establish a mathematically rigorous probabilistic framework) or special structure that enhances the characterization of optimal policies and facilitates their computation. These models were treated in Chapter 5 of the first edition of this book, and also in Chapter 6 of [BeS78].† 
Algorithms 
Our discussion of algorithms centers on abstract forms of value and policy iteration, and is organized along three characteristics: exact, approximate, and asynchronous . The exact algorithms represent idealized versions, the approximate represent implementations that use approximations of various kinds, and the asynchronous involve irregular computation orders, where the costs and controls at di!erent states are updated at di!erent iterations (for example the cost of a single state being iterated at a time, as in Gauss-Seidel and other methods; see [Ber12a] for several examples of distributed asynchronous DP algorithms). 
Approximate and asynchronous implementations have been the subject of intensive investigations since the 1980s, in the context of the solution of large-scale problems. Some of this methodology relies on the use of simulation, which is asynchronous by nature and is prominent in approximate DP. Generally, the monotonicity and sup-norm contraction structures of many prominent DP models favors the use of asynchronous algorithms in DP, as first shown in the author’s paper [Ber82], and discussed at various points in this book: Section 2.6 for contractive models, Section 3.6 for semicontractive models, and Sections 5.3-5.4 for minimax problems and zero-sum games. 
† Chapter 5 of the first edition is accessible from the author’s web site and 
the book’s web page, and uses terminology and notation that are consistent with the present edition.
Sec. 1.5 Notes, Sources, and Exercises 45 
1.5 NOTES, SOURCES, AND EXERCISES 
This monograph is written in a mathematical style that emphasizes simplicity and abstraction. According to the relevant Wikipedia article: 
“Abstraction in mathematics is the process of extracting the underlying essence of a mathematical concept, removing any dependence on real world objects with which it might originally have been connected, and generalizing it so that it has wider applications or matching among other abstract descriptions of equivalent phenomena ... The advantages of abstraction are: 
(1) It reveals deep connections between di!erent areas of mathematics. 
(2) Known results in one area can suggest conjectures in a related area. 
(3) Techniques and methods from one area can be applied to prove results in a related area. 
One disadvantage of abstraction is that highly abstract concepts can be di$cult to learn. A degree of mathematical maturity and experience may be needed for conceptual assimilation of abstractions.” 
Consistent with the preceding view of abstraction, our aim has been to construct a minimalist framework, where the important mathematical structures stand out, while the application context is deliberately blurred. Of course, our development has to pass the test of relevance to applications. In this connection, we note that our presentation has integrated the relation of our abstract DP models with the applications of Section 1.2, and particularly discounted stochastic optimal control models (Chapter 2), shortest path-type models (Chapters 3 and 4), undiscounted deterministic and stochastic optimal control models (Chapter 4), and minimax and zero-sum game problems (Chapter 5). We have given illustrations of the abstract mathematical theory using these models and others throughout the text. A much broader and accessible account of applications is given in the author’s two-volume DP textbook. 
Section 1.2: The abstract style of mathematical development has a long history in DP. In particular, the connection between DP and fixed point theory may be traced to Shapley [Sha53], who exploited contraction mapping properties in analysis of the two-player dynamic game model of Example 1.2.4. Since then, the underlying contraction properties of discounted DP problems with bounded cost per stage have been explicitly or implicitly used by most authors that have dealt with the subject. Moreover, the value of the abstract viewpoint as the basis for economical and insightful analysis has been widely recognized. 
An abstract DP model, based on unweighted sup-norm contraction assumptions, was introduced in the paper by Denardo [Den67]. This model pointed to the fundamental connections between DP and fixed point theory, and provided generality and insight into the principal analytical and
46 Introduction Chap. 1 
algorithmic ideas underlying the discounted DP research up to that time. Abstract DP ideas were also researched earlier, notably in the paper by Mitten (Denardo’s Ph.D. thesis advisor) [Mit64]; see also Denardo and Mitten [DeM67]. The properties of monotone contractions were also used in the analysis of sequential games by Zachrisson [Zac64]. 
Two abstract DP models that rely only on monotonicity properties were given by the author in the papers [Ber75], [Ber77]. They were patterned after the negative cost DP problem of Blackwell [Bla65] and the positive cost DP problem of Strauch [Str66] (see the monotone decreasing and monotone increasing models of Section 4.3). These two abstract DP models, together with the finite horizon models of Section 4.2, were used extensively in the book by Bertsekas and Shreve [BeS78] for the analysis of both discounted and undiscounted DP problems, ranging over MDP, minimax, multiplicative, and Borel space models. 
Extensions of the monotonicity-based analysis of the author’s paper [Ber77] were given by Verdu and Poor [VeP87], who introduced additional structure for developing backward and forward value iterations, and by Szepesvari [Sze98a, Sze98b], who incorporated non-Markovian policies into the abstract DP framework. The model from [Ber77] also provided a foundation for asynchronous value and policy iteration methods for abstract contractive and noncontractive DP models in Bertsekas [Ber82] and Bert-sekas and Yu [BeY10]. An extended contraction framework, whereby the sup-norm contraction norm is allowed to be weighted, was given in the author’s paper [Ber12b]. Another line of related research involving abstract DP mappings that are not necessarily scalar-valued was initiated by Mit-ten [Mit74], and was followed up by a number of authors, including Sobel [Sob75], Morin [Mor82], and Carraway and Morin [CaM88]. 
Section 1.3: The central role of Newton’s method for understanding approximation value space, rollout, and other reinforcement learning and approximate DP methods, was articulated in the author’s monograph [Ber20], and was described in more detail in the book [Ber22]. 
Section 1.4: Generally, noncontractive total cost DP models with some special structure beyond monotonicity, fall in three major categories: monotone increasing models , principally represented by positive cost DP, monotone decreasing models , principally represented by negative cost DP, and transient models , exemplified by the SSP model of Example 1.2.6, where the decision process terminates after a period that is random and subject to control. Abstract DP models patterned after the first two categories have been known since the author’s papers [Ber75], [Ber77], and are further discussed in Section 4.3. 
The semicontractive models, further discussed Chapter 3 and Sec-tions 4.4-4.6, are patterned after the third category. They were introduced and analyzed in the first edition of this book, as well as the subsequent series of papers and reports, [Ber15], [Ber16a], [BeY16], [Ber17b], [Ber17c],
Sec. 1.5 Notes, Sources, and Exercises 47 
[Ber17d], [Ber19c]. Their analysis is based on the idea of separating policies into those that are well-behaved (these are called regular , and have contraction-like properties) and those that are not (these are called irregular). The objective of the analysis is then to explain the detrimental e!ects of the irregular policies, and to delineate the kind of model structure that can limit these e!ects. As far as the author knows, this idea is new in the context of abstract DP. One of the aims of the present monograph is to develop this idea and to show that it leads to an important and insightful paradigm for conceptualization and solution of major classes of practical DP problems. 
E X E R C I S E S 
1.1 (Multistep Contraction Mappings) 
This exercise shows how starting with an abstract mapping, we can obtain multistep mappings with the same fixed points and a stronger contraction modulus. Consider a set of mappings Tµ : B(X) () B(X), µ " M, satisfying the contraction Assumption 1.2.2, let m be a positive integer, and let Mm be the set of m-tuples ( = (µ0, . . . , µm"1), where µk " M, k = 1, . . . ,m $ 1. For each ( = (µ0, . . . , µm"1) " Mm, define the mapping T # , by 
T #J = Tµ0 · · ·Tµm"1J, & J " B(X). 
Show the contraction properties 
/T #J $ T #J #/ % "m/J $ J #/, & J, J # " B(X), (1.39) 
and /TJ $ TJ #/ % "m/J $ J #/, & J, J # " B(X), (1.40) 
where T is defined by 
(TJ)(x) = inf (µ0,...,µm"1)$Mm 
(Tµ0 · · · Tµm"1J)(x), & J " B(X), x " X. 
Solution: By the contraction property of Tµ0 , . . . , Tµm"1 , we have for all J, J # " 
B(X), /T #J $ T #J 
#/ = /Tµ0 · · ·Tµm"1J $ Tµ0 · · ·Tµm"1J #/ 
% "/Tµ1 · · · Tµm"1J $ Tµ1 · · ·Tµm"1J #/ 
% "2/Tµ2 · · ·Tµm"1J $ Tµ2 · · ·Tµm"1J #/ 
... 
% "m/J $ J #/,
48 Introduction Chap. 1 
thus showing Eq. (1.39). We have from Eq. (1.39) 
(Tµ0 · · ·Tµm"1J)(x) % (Tµ0 · · ·Tµm"1J #)(x) + "m/J $ J #/ v(x), & x " X, 
and by taking infimum of both sides over (Tµ0 · · ·Tµm"1) " Mm and dividing by v(x), we obtain 
(TJ)(x)$ (TJ #)(x) 
v(x) % "m/J $ J #/, & x " X. 
Similarly (TJ #)(x)$ (TJ)(x) 
v(x) % "m/J $ J #/, & x " X, 
and by combining the last two relations and taking supremum over x " X, Eq. (1.40) follows. 
1.2 (Relation of Temporal Di"erence Methods and Proximal Algorithms [Ber16b], [Ber18c]) 
The purpose of this exercise is establish a close connection between the mappings underlying temporal di"erence and proximal methods (cf. Section 1.2.5). Consider a linear mapping of the form 
TJ = AJ + b, 
where b is a vector in !n, and A is an n + n matrix with eigenvalues strictly within the unit circle. Let ) " (0, 1) and c = $ 
1"$ , and consider the multistep 
mapping T ($) given by 
T ($)J = (1$ )) 
& # 
"=0 
)"T "+1J, J " !n, 
and the proximal mapping P (c) given by 
P (c)J = 7 
c+ 1 c 
I $ A 8"1 7 
b+ 1 c J 8 
, J " !n; 
cf. Eq. (1.23) [equivalently, for a given J , P (c)J is the unique vector Y " !n that solves the equation 
Y $ TY = 1 c (J $ Y ), 
(cf. Fig. 1.5.1)]. 
(a) Show that P (c) is given by 
P (c) = (1$ )) 
& # 
"=0 
)"T ",
Sec. 1.5 Notes, Sources, and Exercises 49 
! = c 
c+ 1 , c = 
! 
1! ! 
Ĵ = P (c)J J 
Jˆ J* 
Ĵ ! T Ĵ = 1 
c (J ! Ĵ) 
T (!)J = T Ĵ 
Y 
Graph of the mapping Y !TY V 
! 1 
c (J ! Y ) 
Figure 1.5.1. Illustration of the iterates T ($)J and P (c)J for finding the fixed point J! of a linear mapping T . Given J , we find the proximal iterate Ĵ = 
P (c)J and then add the amount 1 c 
$ 
Ĵ $ J % 
to obtain T ($)J = TP (c)J . If T is a 
contraction mapping, T ($)J is closer to J! than P (c)J . 
and can be written as 
P (c)J = A ($) 
J + b ($) 
, 
where 
A ($) 
= (1$ )) 
& # 
"=0 
)"A", b ($) 
= 
& # 
"=0 
)"+1A"b. 
(b) Verify that 
T ($)J = A($)J + b($), 
where 
A($) = (1$ )) 
& # 
"=0 
)"A"+1, b($) = 
& # 
"=0 
)"A"b, 
and show that T ($) = TP (c) = P (c)T, (1.41) 
and that for all J " !n, 
P (c)J = J + ) $ 
T ($)J $ J % 
, T ($)J = J + c+ 1 c 
$ 
P (c)J $ J % 
. (1.42) 
Thus T ($)J is obtained by extrapolation along the line segment P (c)J $J , as illustrated in Fig. 1.5.1. Note that since T is a contraction mapping, T ($)J is closer to J! than P (c)J . 
(c) Show that for a given J " !n, the multistep and proximal iterates T ($)J and P (c)J are the unique fixed points of the contraction mappings WJ and W J given by 
WJY = (1$ ))TJ + )TY, W JY = (1$ ))J + )TY, Y " !n,
50 Introduction Chap. 1 
respectively. 
(d) Show that the fixed point property of part (c) yields the following formula for the multistep mapping T ($): 
T ($)J = (1$ )A)"1 $ 
b+ (1$ ))AJ % 
. (1.43) 
(e) (Multistep Contraction Property for Nonexpansive A [BeY09]) Instead of assuming that A has eigenvalues strictly within the unit circle, assume that the matrix I $ A is invertible and A is nonexpansive [i.e., has all its eigenvalues within the unit circle (possibly on the unit circle)]. Show that A($) is contractive (i.e., has eigenvalues that lie strictly within the unit circle) and its eigenvalues have the form 
*i = (1$ )) 
& # 
"=0 
)"+"+1 i = 
+i(1$ )) 
1$ +i) , i = 1, . . . , n, (1.44) 
where +i, i = 1, . . . , n, are the eigenvalues of A. Note: For an intuitive explanation of the result, note that the eigenvalues of A($) can be viewed as convex combinations of complex numbers from the unit circle at least two of which are di"erent from each other, since +i ,= 1 by assumption (the nonzero corresponding eigenvalues of A and A2 are di"erent from each other). As a result the eigenvalues of A($) lie strictly within the unit circle. 
(f) (Contraction Property of Projected Multistep Mappings) Under the assumptions of part (e), show that lim$%1 A 
($) = 0. Furthermore, for any n + n matrix W , the matrix WA($) is contractive for ) su#ciently close to 1. In particular the projected mapping $A($) and corresponding projected proximal mapping (cf. Section 1.2.5) become contractions as ) ) 1. 
Solution: (a) The inverse in the definition of P (c) is written as 
7 
c+ 1 c 
I $ A 8"1 
= 7 
1 ) I $ A 
8"1 
= )(I $ )A)"1 = ) 
& # 
"=0 
()A)". 
Thus, using the equation 1 c = 1"$ 
$ , 
P (c)J = 7 
c+ 1 c 
I $ A 8"1 7 
b+ 1 c J 8 
= ) 
& # 
"=0 
()A)" 7 
b+ 1$ ) ) 
J 8 
= (1$ )) 
& # 
"=0 
()A)"J + ) 
& # 
"=0 
()A)"b, 
which is equal to A ($) 
J + b ($) 
. The formula P (c) = (1 $ )) +& 
"=0 )"T " follows 
from this expression.
Sec. 1.5 Notes, Sources, and Exercises 51 
(b) The formula T ($)J = A($)J + b($) is verified by straightforward calculation. We have, 
TP (c)J = A $ 
A ($) 
J + b ($)% 
+ b 
= (1$ )) 
& # 
"=0 
)"A"+1J + 
& # 
"=0 
)"+1A"+1b+ b = A($)J + b($) 
= T ($)J, 
thus proving the left side of Eq. (1.41). The right side is proved similarly. The in-terpolation/extrapolation formula (1.42) follows by a straightforward calculation from the definition of T ($). As an example, to show the left side of Eq. (1.42), we write 
J + ) $ 
T ($)J $ J % 
= (1$ ))J + )T ($)J 
= (1$ ))J + ) 
, 
(1$ )) 
& # 
"=0 
)"A"+1J + 
& # 
"=0 
)"A"b 
-
= (1$ )) 
, 
J + 
& # 
"=1 
)"A"J 
-
+ 
& # 
"=0 
)"+1A"b 
= A ($) 
J + b ($) 
= P (c)J. 
(c) To show that T ($)J is the fixed point of WJ , we must verify that 
T ($)J = WJ 
$ 
T ($)J % 
, 
or equivalently that 
T ($)J = (1$ ))TJ + )T $ 
T ($)J) = (1$ ))TJ + )T ($)(TJ). 
The right-hand side, in view of the interpolation formula 
(1$ ))J + )T ($)J = P (c)J, & x " !n, 
is equal to P (c)(TJ), which from the formula T ($) = P (c)T [cf. part (b)], is equal to T ($)J . The proof is similar for W J . 
(d) The fixed point property of part (c) states that T ($)J is the unique solution of the following equation in Y : 
Y = (1$ ))TJ + )TY = (1$ ))(AJ + b) + )(AY + b), 
from which the desired relation follows. 
(e), (f) The formula (1.44) follows from the expression for A($) given in part (b). This formula can be used to show that the eigenvalues of A($) lie strictly within the unit circle, using also the fact that the matrices Am, m * 1, and A($) have the same eigenvectors (see [BeY09] for details). Moreover, the eigenvalue formula shows that all eigenvalues of A($) converge to 0 as ) ) 1, so that lim$%1 A 
($) = 0. This also implies that WA($) is contractive for ) su#ciently close to 1.
52 Introduction Chap. 1 
1.3 (State-Dependent Weighted Multistep Mappings [YuB12]) 
Consider a set of mappings Tµ : B(X) () B(X), µ " M, satisfying the contraction 
Assumption 1.2.2. Consider also the mappings T (w) µ : B(X) () B(X) defined by 
(T (w) µ J)(x) = 
& # 
"=1 
w"(x) $ 
T " µJ % 
(x), x " X, J " B(X), 
where w"(x) are nonnegative scalars such that for all x " X, 
& # 
"=1 
w"(x) = 1. 
Show that ( 
((T (w) µ J)(x)$ (T (w) 
µ J #)(x) ( 
( 
v(x) % 
& # 
"=1 
w"(x)" "/J $ J #/, & x " X, 
so that T (w) µ is a contraction with modulus 
"̄ = sup x$X 
& # 
"=1 
w"(x)" " % " < 1. 
Moreover, for all µ " M, the mappings Tµ and T (w) µ have the same fixed point. 
Solution: By the contraction property of Tµ, we have for all J, J # " B(X) and x " X, 
( 
((T (w) µ J)(x)$ (T (w) 
µ J #)(x) ( 
( 
v(x) = 
( 
( 
+& 
"=1 w"(x)(T " µJ)(x)$ 
+& 
"=1 w"(x)(T " µJ 
#)(x) ( 
( 
v(x) 
% 
& # 
"=1 
w"(x)/T " µJ $ T " 
µJ #/ 
% 
, 
& # 
"=1 
w"(x)" " 
-
/J $ J #/, 
showing the contraction property of T (w) µ . 
Let Jµ be the fixed point of Tµ. By using the relation (T " µJµ)(x) = Jµ(x), 
we have for all x " X, 
(T (w) µ Jµ)(x) = 
& # 
"=1 
w"(x) $ 
T " µJµ 
% 
(x) = 
, 
& # 
"=1 
w"(x) 
-
Jµ(x) = Jµ(x), 
so Jµ is the fixed point of T (w) µ [which is unique since T (w) 
µ is a contraction].
2 Contractive Models 
Contents 
2.1. Bellman’s Equation and Optimality Conditions . . . . . p. 54 2.2. Limited Lookahead Policies . . . . . . . . . . . . . p. 61 2.3. Value Iteration . . . . . . . . . . . . . . . . . . . p. 66 
2.3.1. Approximate Value Iteration . . . . . . . . . . . p. 67 2.4. Policy Iteration . . . . . . . . . . . . . . . . . . . p. 70 
2.4.1. Approximate Policy Iteration . . . . . . . . . . p. 73 2.4.2. Approximate Policy Iteration Where Policies . . . . . 
Converge . . . . . . . . . . . . . . . . . . . p. 75 2.5. Optimistic Policy Iteration and !-Policy Iteration . . . . p. 77 
2.5.1. Convergence of Optimistic Policy Iteration . . . . p. 79 2.5.2. Approximate Optimistic Policy Iteration . . . . . p. 84 2.5.3. Randomized Optimistic Policy Iteration . . . . . . p. 87 
2.6. Asynchronous Algorithms . . . . . . . . . . . . . . p. 91 2.6.1. Asynchronous Value Iteration . . . . . . . . . . p. 91 2.6.2. Asynchronous Policy Iteration . . . . . . . . . . p. 98 2.6.3. Optimistic Asynchronous Policy Iteration with a . . . . 
Uniform Fixed Point . . . . . . . . . . . . . p. 103 2.7. Notes, Sources, and Exercises . . . . . . . . . . . . p. 110 
53
54 Contractive Models Chap. 2 
In this chapter we consider the abstract DP model of Section 1.2 under the most favorable assumptions: monotonicity and weighted sup-norm contraction. Important special cases of this model are the discounted problems with bounded cost per stage (Example 1.2.1-1.2.5), the stochastic shortest path problem of Example 1.2.6 in the case where all policies are proper, as well as other problems involving special structures. 
We first provide some basic analytical results and then focus on two types of algorithms: value iteration and policy iteration. In addition to exact forms of these algorithms, we discuss combinations and approximate versions, as well as asynchronous distributed versions. 
2.1 BELLMAN’S EQUATION AND OPTIMALITY CONDITIONS 
In this section we recall the abstract DP model of Section 1.2, and derive some of its basic properties under the monotonicity and contraction assumptions of Section 1.3. We consider a set X of states and a set U of controls, and for each x ! X , a nonempty control constraint set U(x) " U . We denote by M the set of all functions µ : X #$ U with µ(x) ! U(x) for all x ! X , which we refer to as policies (or “stationary policies,” when we want to emphasize the distinction from nonstationary policies, to be discussed later). 
We denote by R(X) the set of real-valued functions J : X #$ %. We have a mapping H : X & U &R(X) #$ % and for each policy µ ! M, we consider the mapping Tµ : R(X) #$ R(X) defined by 
(TµJ)(x) = H ! x, µ(x), J 
" , ' x ! X. 
We also consider the mapping T defined by 
(TJ)(x) = inf u!U(x) 
H(x, u, J) = inf µ!M 
(TµJ)(x), ' x ! X. 
[We will use frequently the second equality above, which holds because M can be viewed as the Cartesian product !x!XU(x).] We want to find a function J* ! R(X) such that 
J*(x) = inf u!U(x) 
H(x, u, J*), ' x ! X, 
i.e., to find a fixed point of T within R(X). We also want to obtain a policy µ" ! M such that Tµ!J* = TJ*. 
Let us restate for convenience the contraction and monotonicity assumptions of Section 1.2.2. 
Assumption 2.1.1: (Monotonicity) If J, J # ! R(X) and J ( J #, then 
H(x, u, J) ( H(x, u, J #), ' x ! X, u ! U(x).
Sec. 2.1 Bellman’s Equation and Optimality Conditions 55 
Note that the monotonicity assumption implies the following properties, for all J, J # ! R(X) and k = 0, 1, . . ., which we will use extensively: 
J ( J # ) T kJ ( T kJ #, T k µJ ( T k 
µJ #, ' µ ! M, 
J ( TJ ) T kJ ( T k+1J, T k µJ ( T k+1 
µ J, ' µ ! M. 
Here T k and T k µ denotes the k-fold composition of T and Tµ, respectively. 
For the contraction assumption, we introduce a function v : X #$ % with 
v(x) > 0, ' x ! X. 
We consider the weighted sup-norm 
*J* = sup x!X 
##J(x) ## 
v(x) 
on B(X), the space of real-valued functions J on X such that J(x)/v(x) is bounded over x ! X (see Appendix B for a discussion of the properties of this space). 
Assumption 2.1.2: (Contraction) For all J ! B(X) and µ ! M, the functions TµJ and TJ belong to B(X). Furthermore, for some ! ! (0, 1), we have 
*TµJ + TµJ #* ( !*J + J #*, ' J, J # ! B(X), µ ! M. 
The classical DP models where both the monotonicity and contraction assumptions are satisfied are the discounted finite-state Markovian decision problem of Example 1.2.2, and the stochastic shortest path problem of Example 1.2.6 in the special case where all policies are proper; see the textbook [Ber12a] for an extensive discussion. In the context of these problems, the fixed point equation J = TJ is called Bellman’s equation, a term that we will use more generally in this book as well. The following proposition summarizes some of the basic consequences of the contraction assumption. 
Proposition 2.1.1: Let the contraction Assumption 2.1.2 hold. Then: 
(a) The mappings Tµ and T are contraction mappings with modulus ! over B(X), and have unique fixed points in B(X), denoted Jµ and J*, respectively.
56 Contractive Models Chap. 2 
(b) For any J ! B(X) and µ ! M, 
lim k$% 
*J* + T kJ* = 0, lim k$% 
*Jµ + T k µJ* = 0. 
(c) We have TµJ* = TJ* if and only if Jµ = J*. 
(d) For any J ! B(X), 
*J* + J* ( 1 
1+ ! *TJ + J*, *J* + TJ* ( 
! 
1+ ! *TJ + J*. 
(e) For any J ! B(X) and µ ! M, 
*Jµ+J* ( 1 
1+ ! *TµJ+J*, *Jµ+TµJ* ( 
! 
1+ ! *TµJ+J*. 
Proof: We showed in Section 1.2.2 that T is a contraction with modulus ! over B(X). Parts (a) and (b) follow from Prop. B.1 of Appendix B. 
To show part (c), note that if TµJ* = TJ*, then in view of TJ* = J*, we have TµJ* = J*, which implies that J* = Jµ, since Jµ is the unique fixed point of Tµ. Conversely, if J* = Jµ, we have TµJ* = TµJµ = Jµ = J* = TJ*. 
To show part (d), we use the triangle inequality to write for every k, 
*T kJ + J* ( k$ 
!=1 
*T !J + T !&1J* ( k$ 
!=1 
!!&1*TJ + J*. 
Taking the limit as k $ , and using part (b), the left-hand side inequality follows. The right-hand side inequality follows from the left-hand side and the contraction property of T . The proof of part (e) is similar to part (d) [indeed it is the special case of part (d) where T is equal to Tµ, i.e., when U(x) = 
% µ(x) 
& for all x ! X ]. Q.E.D. 
Part (c) of the preceding proposition shows that there exists a µ ! M such that Jµ = J* if and only if the minimum of H(x, u, J*) over U(x) is attained for all x ! X . Of course the minimum is attained if U(x) is finite for every x, but otherwise this is not guaranteed in the absence of additional assumptions. Part (d) provides a useful error bound: we can evaluate the proximity of any function J ! B(X) to the fixed point J* by applying T to J and computing *TJ+J*. The left-hand side inequality of part (e) (with J = J*) shows that for every " > 0, there exists a µ" ! M such that *Jµ! +J** ( ", which may be obtained by letting µ"(x) minimize H(x, u, J*) over U(x) within an error of (1+ !)" v(x), for all x ! X .
Sec. 2.1 Bellman’s Equation and Optimality Conditions 57 
The preceding proposition and some of the subsequent results may also be proved if B(X) is replaced by a closed subset B(X) " B(X). This is because the contraction mapping fixed point theorem (Prop. B.1) applies to closed subsets of complete spaces. For simplicity, however, we will disregard this possibility in the present chapter. 
An important consequence of monotonicity of H , when it holds in addition to contraction, is that it implies that J*, the unique fixed point of T , is the infimum over µ ! M of Jµ, the unique fixed point of Tµ. 
Proposition 2.1.2: Let the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2 hold. Then 
J*(x) = inf µ!M 
Jµ(x), ' x ! X. 
Furthermore, for every " > 0, there exists µ" ! M such that 
J*(x) ( Jµ!(x) ( J*(x) + ", ' x ! X. (2.1) 
Proof: We note that the right-hand side of Eq. (2.1) holds by Prop. 2.1.1(e) (see the remark following its proof). Thus infµ!M Jµ(x) ( J*(x) for all x ! X . To show the reverse inequality as well as the left-hand side of Eq. (2.1), we note that for all µ ! M, we have TJ* ( TµJ*, and since J* = TJ*, it follows that J* ( TµJ*. By applying repeatedly Tµ to both sides of this inequality and by using the monotonicity Assumption 2.1.1, we obtain J* ( T k 
µJ* for all k > 0. Taking the limit as k $ ,, we see that J* ( Jµ for all µ ! M, so that J*(x) ( infµ!M Jµ(x) for all x ! X . Q.E.D. 
Note that without monotonicity, we may have infµ!M Jµ(x) < J*(x) for some x. This is illustrated by the following example. 
Example 2.1.1 (Counterexample Without Monotonicity) 
Let X = {x1, x2}, U = {u1, u2}, and let 
H(x1, u, J) = 
' !!J(x2) if u = u1, !1 + !J(x1) if u = u2, 
H(x2, u, J) = ( 0 if u = u1, B if u = u2, 
where B is a positive scalar. Then it can be seen that 
J!(x1) = ! 1 
1! ! , J!(x2) = 0, 
and Jµ! = J! where µ!(x1) = u2 and µ!(x2) = u1. On the other hand, for µ(x1) = u1 and µ(x2) = u2, we have Jµ(x1) = !!B and Jµ(x2) = B, so Jµ(x1) < J!(x1) for B su!ciently large.
58 Contractive Models Chap. 2 
Optimality over Nonstationary Policies 
The connection with DP motivates us to consider the set ! of all sequences # = {µ0, µ1, . . .} with µk ! M for all k (nonstationary policies in the DP context), and define 
J#(x) = lim sup k$% 
(Tµ0 · · ·Tµk J̄)(x), ' x ! X, 
with J̄ being some function in B(X), where Tµ0 · · ·Tµk J denotes the com-
position of the mappings Tµ0 , . . . , Tµk applied to J , i.e., 
Tµ0 · · ·Tµk J = Tµ0 
! Tµ1 · · · (Tµk"1(Tµk 
J)) · · · " . 
Note that under the contraction Assumption 2.1.2, the choice of J̄ in the definition of J# does not matter , since for any two J, J # ! B(X), we have 
*Tµ0Tµ1 · · ·Tµk J + Tµ0Tµ1 · · ·Tµk 
J #* ( !k+1*J + J #*, 
so the value of J#(x) is independent of J̄ . Since by Prop. 2.1.1(b), Jµ(x) = limk$% (T k 
µJ)(x) for all µ ! M, J ! B(X), and x ! X , in the DP context we recognize Jµ as the cost function of the stationary policy {µ, µ, . . .}. 
We now claim that under the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2, J*, which was defined as the unique fixed point of T , is equal to the optimal value of J#, i.e., 
J*(x) = inf #!! 
J#(x), ' x ! X. 
Indeed, since M defines a subset of !, we have from Prop. 2.1.2, 
J*(x) = inf µ!M 
Jµ(x) - inf #!! 
J#(x), ' x ! X, 
while for every # ! ! and x ! X , we have 
J#(x) = lim sup k$% 
(Tµ0Tµ1 · · ·Tµk J̄)(x) - lim 
k$% (T k+1J̄)(x) = J*(x) 
[the monotonicity Assumption 2.1.1 can be used to show that 
Tµ0Tµ1 · · ·Tµk J̄ - T k+1J̄ , 
and the last equality holds by Prop. 2.1.1(b)]. Combining the preceding relations, we obtain J*(x) = inf#!! J#(x). 
Thus, in DP terms, we may view J* as an optimal cost function over all policies , including nonstationary ones. At the same time, Prop. 2.1.2 states that stationary policies are su"cient in the sense that the optimal cost can be attained to within arbitrary accuracy with a stationary policy [uniformly for all x ! X , as Eq. (2.1) shows].
Sec. 2.1 Bellman’s Equation and Optimality Conditions 59 
Error Bounds and Other Inequalities 
The analysis of abstract DP algorithms and related approximations requires the use of some basic inequalities that follow from the assumptions of contraction and monotonicity. We have obtained two such results in Prop. 2.1.1(d),(e), which assume only the contraction assumption. These results can be strengthened if in addition to contraction, we have monotonicity. To this end we first show the following useful characterization. 
Proposition 2.1.3: The monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold if and only if for all J, J # ! B(X), µ ! M, and scalar c - 0, we have 
J ( J # + c v ) TµJ ( TµJ # + !c v, (2.2) 
where v is the weight function of the weighted sup-norm * · *. 
Proof: Let the contraction and monotonicity assumptions hold. If J ( J # + c v, we have 
H(x, u, J) ( H(x, u, J #+ c v) ( H(x, u, J #)+!c v(x), ' x ! X, u ! U(x), (2.3) 
where the left-side inequality follows from the monotonicity assumption and the right-side inequality follows from the contraction assumption, which together with *v* = 1, implies that 
H(x, u, J + c v)+H(x, u, J) 
v(x) ( !*J + c v + J* = !c. 
The condition (2.3) implies the desired condition (2.2). Conversely, condition (2.2) for c = 0 yields the monotonicity assumption, while for c = *J # + J* it yields the contraction assumption. Q.E.D. 
We can now derive the following useful variant of Prop. 2.1.1(d),(e), which involves one-sided inequalities. This variant will be used in the derivation of error bounds for various computational methods. 
Proposition 2.1.4: (Error Bounds Under Contraction and Monotonicity) Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold. Then:
60 Contractive Models Chap. 2 
(a) For any J ! B(X) and c - 0, we have 
TJ ( J + c v ) J* ( J + c 
1+ ! v, 
J ( TJ + c v ) J ( J* + c 
1+ ! v. 
(b) For any J ! B(X), µ ! M, and c - 0, we have 
TµJ ( J + c v ) Jµ ( J + c 
1+ ! v, 
J ( TµJ + c v ) J ( Jµ + c 
1+ ! v. 
(c) For all J ! B(X), c - 0, and k = 0, 1, . . ., we have 
TJ ( J + c v ) J* ( T kJ + !kc 
1+ ! v, 
J ( TJ + c v ) T kJ ( J* + !kc 
1+ ! v. 
Proof: (a) We show the first relation. Applying Eq. (2.2) with J # and J replaced by J and TJ , respectively, and taking infimum over µ ! M, we see that if TJ ( J + c v, then T 2J ( TJ + !c v. Proceeding similarly, it follows that 
T !J ( T !&1J + !!&1c v. 
We now write for every k, 
T kJ + J = k$ 
!=1 
(T !J + T !&1J) ( k$ 
!=1 
!!&1c v, 
from which, by taking the limit as k $ ,, we obtain 
J* ( J + c 
1+ ! v. 
The second relation follows similarly. 
(b) This part is the special case of part (a) where T is equal to Tµ. 
(c) Similar to the proof of part (a), the inequality 
TJ ( J + c v
Sec. 2.2 Limited Lookahead Policies 61 
implies that for all k we have 
T k+1J ( T kJ + !kc v. 
Applying part (a) with J and c replaced by T kJ and !kc, respectively, we obtain the first desired relation. The second relation follows similarly. Q.E.D. 
2.2 LIMITED LOOKAHEAD POLICIES 
In this section, we discuss a basic building block in the algorithmic methodology of abstract DP. Given some function J̃ that approximates J*, we obtain a policy by solving a finite-horizon problem where J̃ is the terminal cost function. The simplest possibility is a one-step lookahead policy µ defined by 
µ(x) ! argmin u!U(x) 
H(x, u, J̃), x ! X. (2.4) 
Its cost function Jµ was interpreted in Section 1.3.1 as the result of a Newton iteration that starts from J̃ and aims to solve the Bellman equation J = TJ . The following proposition gives some bounds for its performance. 
Proposition 2.2.1: (One-Step Lookahead Error Bounds) Let the contraction Assumption 2.1.2 hold, and let µ be a one-step lookahead policy obtained by minimization in Eq. (2.4), i.e., satisfying TµJ̃ = T J̃ . Then 
*Jµ + T J̃* ( ! 
1+ ! *T J̃ + J̃*, (2.5) 
where * · * denotes the weighted sup-norm. Moreover 
*Jµ + J** ( 2! 
1+ ! *J̃ + J**, (2.6) 
and 
*Jµ + J** ( 2 
1+ ! *T J̃ + J̃*. (2.7) 
Proof: Equation (2.5) follows from the second relation of Prop. 2.1.1(e) with J = J̃ . Also from the first relation of Prop. 2.1.1(e) with J = J*, we have 
*Jµ + J** ( 1 
1+ ! *TµJ* + J**.
62 Contractive Models Chap. 2 
By using the triangle inequality, and the relations TµJ̃ = T J̃ and J* = TJ*, we obtain 
*TµJ* + J** ( *TµJ* + TµJ̃*+ *TµJ̃ + T J̃*+ *T J̃ + J** 
= *TµJ* + TµJ̃*+ *T J̃ + TJ** 
( !*J* + J̃*+ !*J̃ + J** 
= 2! *J̃ + J**, 
and Eq. (2.6) follows by combining the preceding two relations. Also, from the first relation of Prop. 2.1.1(d) with J = J̃ , 
*J* + J̃* ( 1 
1+ ! *T J̃ + J̃*. (2.8) 
Thus 
*Jµ + J** ( *Jµ + T J̃*+ *T J̃ + J̃*+ *J̃ + J** 
( ! 
1+ ! *T J̃ + J̃*+ *T J̃ + J̃*+ 
1 
1+ ! *T J̃ + J̃* 
= 2 
1+ ! *T J̃ + J̃*, 
where the second inequality follows from Eqs. (2.5) and (2.8). This proves Eq. (2.7). Q.E.D. 
Equation (2.5) provides a computable bound on the cost function Jµ of the one-step lookahead policy. The bound (2.6) says that if the one-step lookahead approximation J̃ is within " of the optimal, the performance of the one-step lookahead policy is within 
2!" 
1+ ! 
of the optimal. Unfortunately, this is not very reassuring when ! is close to 1, in which case the error bound is large relative to ". Nonetheless, the following example from [BeT96], Section 6.1.1, shows that this bound is tight, i.e., for any ! < 1, there is a problem with just two states where the error bound is satisfied with equality. What is happening is that an O(") di#erence in single stage cost between two controls can generate an O ! "/(1+!) 
" di#erence in policy costs, yet it can be “nullified” in the fixed 
point equation J* = TJ* by an O(") di#erence between J* and J̃ . 
Example 2.2.1 
Consider a discounted optimal control problem with two states, 1 and 2, and deterministic transitions. State 2 is absorbing, but at state 1 there are two possible decisions: move to state 2 (policy µ!) or stay at state 1 (policy µ).
Sec. 2.2 Limited Lookahead Policies 63 
The cost of each transition is 0 except for the transition from 1 to itself under policy µ, which has cost 2!", where " is a positive scalar and ! " [0, 1) is the discount factor. The optimal policy µ! is to move from state 1 to state 2, and the optimal cost-to-go function is J!(1) = J!(2) = 0. Consider the vector J̃ with J̃(1) = !" and J̃(2) = ", so that 
#J̃ ! J!# = ", 
as assumed in Eq. (2.6) (cf. Prop. 2.2.1). The policy µ that decides to stay at state 1 is a one-step lookahead policy based on J̃ , because 
2!"+ !J̃(1) = !" = 0 + !J̃(2). 
We have 
Jµ(1) = 2!" 1! ! 
= 2! 
1! ! #J̃ ! J!#, 
so the bound of Eq. (2.6) holds with equality. 
Multistep Lookahead Policies with Approximations 
Let us now consider a more general form of lookahead involving multiple stages as well as other approximations of the type that we will consider later in the implementation of various approximate value and policy iteration algorithms. In particular, we will assume that given any J ! B(X), we cannot compute exactly TJ , but instead we can compute J̃ ! B(X) and µ ! M such that 
*J̃ + TJ* ( $, *TµJ + TJ* ( ", (2.9) 
where $ and " are nonnegative scalars. These scalars are usually unknown, so the resulting analysis will have a mostly qualitative character. 
The case $ > 0 arises when the state space is either infinite or it is finite but very large. Then instead of calculating (TJ)(x) for all states x, one may do so only for some states and estimate (TJ)(x) for the remaining states x by some form of interpolation. Alternatively, one may use simulation data [e.g., noisy values of (TJ)(x) for some or all x] and some kind of least-squares error fit of (TJ)(x) with a function from a suitable parametric class. The function J̃ thus obtained will satisfy *J̃ + TJ* ( $ with $ > 0. Note that $ may not be small in this context, and the resulting performance degradation may be a primary concern. 
Cases where " > 0 may arise when the control space is infinite or finite but large, and the minimization involved in the calculation of (TJ)(x) cannot be done exactly. Note, however, that it is possible that 
$ > 0, " = 0,
64 Contractive Models Chap. 2 
and in fact this occurs often in practice. In an alternative scenario, we may first obtain the policy µ subject to a restriction that it belongs to a certain subset of structured policies, so it satisfies 
*TµJ + TJ* ( " 
for some " > 0, and then we may set J̃ = TµJ . In this case we have " = $ in Eq. (2.9). 
In a multistep method with approximations, we are given a positive integer m and a lookahead function Jm, and we successively compute (backwards in time) Jm&1, . . . , J0 and policies µm&1, . . . , µ0 satisfying 
*Jk+TJk+1* ( $, *Tµk Jk+1+TJk+1* ( ", k = 0, . . . ,m+1. (2.10) 
Note that in the context of MDP, Jk can be viewed as an approximation to the optimal cost function of an (m + k)-stage problem with terminal cost function Jm. We have the following proposition. 
Proposition 2.2.2: (Multistep Lookahead Error Bound) Let the contraction Assumption 2.1.2 hold. The periodic policy 
# = {µ0, . . . , µm&1, µ0, . . . , µm&1, . . .} 
generated by the method of Eq. (2.10) satisfies 
*J# + J** ( 2!m 
1+ !m *Jm + J**+ 
" 
1+ !m + 
!(" + 2$)(1+ !m&1) 
(1+ !)(1 + !m) . 
(2.11) 
Proof: Using the triangle inequality, Eq. (2.10), and the contraction property of T , we have for all k 
*Jm&k + T kJm* ( *Jm&k + TJm&k+1*+ *TJm&k+1 + T 2Jm&k+2* 
+ · · ·+ *T k&1Jm&1 + T kJm* 
( $ + !$ + · · ·+ !k&1$, (2.12) 
showing that 
*Jm&k + T kJm* ( $(1+ !k) 
1+ ! , k = 1, . . . ,m. (2.13)
Sec. 2.2 Limited Lookahead Policies 65 
From Eq. (2.10), we have *Jk + Tµk Jk+1* ( $ + ", so for all k 
*Jm&k + Tµm"k · · ·Tµm"1Jm* ( *Jm&k + Tµm"k 
Jm&k+1* 
+ *Tµm"k Jm&k+1 + Tµm"k 
Tµm"k+1Jm&k+2* 
+ · · · 
+ *Tµm"k · · ·Tµm"2Jm&1 + Tµm"k 
· · ·Tµm"1Jm* 
( ($ + ") + !($ + ") + · · ·+ !k&1($ + "), 
showing that 
*Jm&k + Tµm"k · · ·Tµm"1Jm* ( 
($ + ")(1 + !k) 
1+ ! , k = 1, . . . ,m. 
(2.14) Using the fact *Tµ0J1 + TJ1* ( " [cf. Eq. (2.10)], we obtain 
*Tµ0 · · ·Tµm"1Jm + TmJm* ( *Tµ0 · · ·Tµm"1Jm + Tµ0J1* 
+ *Tµ0J1 + TJ1*+ *TJ1 + TmJm* 
( !*Tµ1 · · ·Tµm"1Jm + J1*+ "+ !*J1 + Tm&1Jm* 
( "+ !(" + 2$)(1+ !m&1) 
1+ ! , 
where the last inequality follows from Eqs. (2.13) and (2.14) for k = m+ 1. From this relation and the fact that Tµ0 · · ·Tµm"1 and Tm are con-
tractions with modulus !m, we obtain 
*Tµ0 · · ·Tµm"1J* + J** ( *Tµ0 · · ·Tµm"1J* + Tµ0 · · ·Tµm"1Jm* 
+ *Tµ0 · · ·Tµm"1Jm + TmJm*+ *TmJm + J** 
( 2!m*J* + Jm*+ " + !("+ 2$)(1 + !m&1) 
1+ ! . 
We also have using Prop. 2.1.1(e), applied in the context of the multistep mapping of Example 1.3.1, 
*J# + J** ( 1 
1+ !m *Tµ0 · · ·Tµm"1J* + J**. 
Combining the last two relations, we obtain the desired result. Q.E.D. 
Note that form = 1 and $ = " = 0, i.e., the case of one-step lookahead policy µ with lookahead function J1 and no approximation error in the minimization involved in TJ1, Eq. (2.11) yields the bound 
*Jµ + J** ( 2! 
1+ ! *J1 + J**,
66 Contractive Models Chap. 2 
which coincides with the bound (2.6) derived earlier. Also, in the special case where " = $ and Jk = Tµk 
Jk+1 (cf. the discussion preceding Prop. 2.2.2), the bound (2.11) can be strengthened somewhat. In particular, we have for all k, Jm&k = Tµm"k 
· · ·Tµm"1Jm, so the right-hand side of Eq. (2.14) becomes 0 and the preceding proof yields, with some calculation, 
*J# + J** ( 2!m 
1+ !m *Jm + J**+ 
$ 
1+ !m + 
!$(1 + !m&1) 
(1+ !)(1 + !m) 
= 2!m 
1+ !m *Jm + J**+ 
$ 
1+ ! . 
We finally note that Prop. 2.2.2 shows that as the lookahead size m increases, the corresponding bound for *J#+J** tends to "+!("+2$)/(1+ !), or 
lim sup m$% 
*J# + J** ( "+ 2!$ 
1+ ! . 
We will see that this error bound is superior to corresponding error bounds for approximate versions of value and policy iteration by essentially a factor 1/(1 + !). In practice, however, periodic suboptimal policies, as required by Prop. 2.2.2, are typically not used. 
There is an alternative and often used form of on-line multistep lookahead, whereby at the current state x we compute a multistep policy {µ0, . . . , µm&1}, we apply the first component µ0(x) of that policy at state x, then at the next state x̄ we recompute a new multistep policy {µ̄0, . . . , µ̄m&1}, apply µ̄0(x̄), etc. However, no error bound similar to the one of Prop. 2.2.2 is currently known for this type of lookahead. 
2.3 VALUE ITERATION 
In this section, we discuss value iteration (VI for short), the algorithm that starts with some J ! B(X), and generates TJ, T 2J, . . .. Since T is a weighted sup-norm contraction under Assumption 2.1.2, the algorithm converges to J*, and the rate of convergence is governed by 
*T kJ + J** ( !k*J + J**, k = 0, 1, . . . . 
Similarly, for a given policy µ ! M, we have 
*T k µJ + Jµ* ( !k*J + Jµ*, k = 0, 1, . . . . 
From Prop. 2.1.1(d), we also have the error bound 
*T k+1J + J** ( ! 
1+ ! *T k+1J + T kJ*, k = 0, 1, . . . .
Sec. 2.3 Value Iteration 67 
This bound does not rely on the monotonicity Assumption 2.1.1. The VI algorithm is often used to compute an approximation J̃ to 
J*, and then to obtain a policy µ by minimizing H(x, u, J̃) over u ! U(x) for each x ! X . In other words J̃ and µ satisfy 
*J̃ + J** ( %, TµJ̃ = T J̃, 
where % is some positive scalar. Then by using Eq. (2.6), we have 
*Jµ + J** ( 2!% 
1+ ! . (2.15) 
If the set of policies is finite, this procedure can be used to compute an optimal policy with a finite but su"ciently large number of exact VI, as shown in the following proposition. 
Proposition 2.3.1: Let the contraction Assumption 2.1.2 hold and let J ! B(X). If the set of policies M is finite, there exists an integer k - 0 such that Jµ! = J* for all µ" and k - k with Tµ!T kJ = T k+1J . 
Proof: Let M̃ be the set of policies such that Jµ .= J*. Since M̃ is finite, we have 
inf µ!M̃ 
*Jµ + J** > 0, 
so by Eq. (2.15), there exists su"ciently small & > 0 such that 
*J̃ + J** ( & and TµJ̃ = T J̃ ) *Jµ + J** = 0 ) µ /! M̃. (2.16) 
It follows that if k is su"ciently large so that *T kJ + J** ( &, then Tµ!T kJ = T k+1J implies that µ" /! M̃ so Jµ! = J*. Q.E.D. 
2.3.1 Approximate Value Iteration 
We will now consider situations where the VI method may be implementable only through approximations. In particular, given a function J , assume that we may only be able to calculate an approximation J̃ to TJ such that ))J̃ + TJ 
)) ( $, 
where $ is a given positive scalar. In the corresponding approximate VI method, we start from an arbitrary bounded function J0, and we generate a sequence {Jk} satisfying 
*Jk+1 + TJk* ( $, k = 0, 1, . . . . (2.17)
68 Contractive Models Chap. 2 
This approximation may be the result of representing Jk+1 compactly, as a linear combination of basis functions, through a projection or aggregation process, as is common in approximate DP (cf. the discussion of Section 1.2.4). 
We may also simultaneously generate a sequence of policies {µk} such that 
*TµkJk + TJk* ( ", k = 0, 1, . . . , (2.18) 
where " is some scalar [which could be equal to 0, as in case of Eq. (2.10), considered earlier]. The following proposition shows that the corresponding cost functions Jµk “converge” to J* to within an error of order O 
! $/(1 + 
!)2 " [plus a less significant error of order O 
! "/(1+ !) 
" ]. 
Proposition 2.3.2: (Error Bounds for Approximate VI) Let the contraction Assumption 2.1.2 hold. A sequence {Jk} generated by the approximate VI method (2.17)-(2.18) satisfies 
lim sup k$% 
*Jk + J** ( $ 
1+ ! , (2.19) 
while the corresponding sequence of policies {µk} satisfies 
lim sup k$% 
*Jµk + J** ( " 
1+ ! + 
2!$ 
(1+ !)2 . (2.20) 
Proof: Using the triangle inequality, Eq. (2.17), and the contraction property of T , we have 
*Jk + T kJ0* ( *Jk + TJk&1* 
+ *TJk&1 + T 2Jk&2*+ · · ·+ *T k&1J1 + T kJ0* 
( $ + !$ + · · ·+ !k&1$, 
and finally 
*Jk + T kJ0* ( (1+ !k)$ 
1+ ! , k = 0, 1, . . . . (2.21) 
By taking limit as k $ , and by using the fact limk$% T kJ0 = J*, we obtain Eq. (2.19). 
We also have using the triangle inequality and the contraction property of Tµk and T , 
*TµkJ* + J** ( *TµkJ* + TµkJk*+ *TµkJk + TJk*+ *TJk + J** 
( !*J* + Jk*+ "+ !*Jk + J**,
Sec. 2.3 Value Iteration 69 
while by using also Prop. 2.1.1(e), we obtain 
*Jµk + J** ( 1 
1+ ! *TµkJ* + J** ( 
" 
1+ ! + 
2! 
1+ ! *Jk + J**. 
By combining this relation with Eq. (2.19), we obtain Eq. (2.20). Q.E.D. 
The error bound (2.20) relates to stationary policies obtained from the functions Jk by one-step lookahead. We may also obtain an m-step periodic policy # from Jk by using m-step lookahead. Then Prop. 2.2.2 shows that the corresponding bound for *J#+J** tends to ("+2!$)/(1+!) as m $ ,, which improves on the error bound (2.20) by a factor 1/(1+!). 
Finally, let us note that the error bound of Prop. 2.3.2 is predicated upon generating a sequence {Jk} satisfying *Jk+1 + TJk* ( $ for all k [cf. Eq. (2.17)]. Unfortunately, some practical approximation schemes guarantee the existence of such a $ only if {Jk} is a bounded sequence. The following example from [BeT96], Section 6.5.3, shows that boundedness of the iterates is not automatically guaranteed, and is a serious issue that should be addressed in approximate VI schemes. 
Example 2.3.1 (Error Amplification in Approximate Value Iteration) 
Consider a two-state !-discounted MDP with states 1 and 2, and a single policy. The transitions are deterministic: from state 1 to state 2, and from state 2 to state 2. These transitions are also cost-free. Thus we have (TJ(1) = (TJ)(2) = !J(2), and J!(1) = J!(2) = 0. 
We consider a VI scheme that approximates cost functions within the one-dimensional subspace of linear functions S = 
% (r, 2r) | r " $ 
& by using 
a weighted least squares minimization; i.e., we approximate a vector J by its weighted Euclidean projection onto S. In particular, given Jk = (rk, 2rk), we find Jk+1 = (rk+1, 2rk+1), where for weights #1, #2 > 0, rk+1 is obtained as 
rk+1 " argmin r 
* #1 ! r ! (TJk)(1) 
"2 + #2 
! 2r ! (TJk)(2) 
"2+ . 
Since for a zero cost per stage and the given deterministic transitions, we have TJk = (2!rk, 2!rk), the preceding minimization is written as 
rk+1 " argmin r 
, #1(r ! 2!rk) 
2 + #2(2r ! 2!rk) 2 -, 
which by writing the corresponding optimality condition yields rk+1 = !$rk, where $ = 2(#1 + 2#2)(#1 + 4#2) > 1. Thus if ! > 1/$, the sequence {rk} diverges and so does {Jk}. Note that in this example the optimal cost function J! = (0, 0) belongs to the subspace S. The di!culty here is that the approximate VI mapping that generates Jk+1 as the weighted Euclidean projection of TJk is not a contraction (this is a manifestation of an important issue in approximate DP and projected equation approximation, namely that the projected mapping "T need not be a contraction even if T is a sup-norm contraction; see [DFV00], [Ber12b] for examples and related discussions). At the same time there is no % such that #Jk+1 ! TJk# % % for all k, because of error amplification in each approximate VI.
70 Contractive Models Chap. 2 
2.4 POLICY ITERATION 
In this section, we discuss policy iteration (PI for short), an algorithm whereby we maintain and update a policy µk, starting from some initial policy µ0. The typical iteration has the following form (see Fig. 2.4.1 for a one-dimensional illustration). 
Policy iteration given the current policy µk: 
Policy evaluation: We compute Jµk as the unique solution of the equation 
Jµk = TµkJµk . 
Policy improvement: We obtain a policy µk+1 that satisfies 
Tµk+1Jµk = TJµk . 
We assume that the minimum of H(x, u, Jµk ) over u ! U(x) is attained for all x ! X , so that the improved policy µk+1 is defined (we use this assumption for all the PI algorithms of the book). The following proposition establishes a basic cost improvement property, as well as finite convergence for the case where the set of policies is finite. 
Proposition 2.4.1: (Convergence of PI) Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, and let {µk} be a sequence generated by the PI algorithm. Then for all k, we have Jµk+1 ( Jµk , with equality if and only if Jµk = J*. Moreover, 
lim k$% 
*Jµk + J** = 0, 
and if the set of policies is finite, we have Jµk = J* for some k. 
Proof: We have 
Tµk+1Jµk = TJµk ( TµkJµk = Jµk . 
Applying Tµk+1 to this inequality while using the monotonicity Assumption 2.1.1, we obtain 
T 2 µk+1Jµk ( Tµk+1Jµk = TJµk ( TµkJµk = Jµk .
Sec. 2.3 Value Iteration 71 
J J! = TJ! 
0 Prob. = 1 
! TJ 
Prob. = 1 Prob. = 
! TJ 
Prob. = 1 Prob. = 
1 J J 
TJ 45 Degree Line Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Policy Improvement Exact Policy Evaluation Approximate Policy Evaluation 
Policy Improvement Exact Policy Evaluation (Exact if 
J0 = TJ0 
Do not Replace Set S 
= T 2J0 
n Value Iterations 
Tµ0J J 
J Jµ0 = Tµ0Jµ0 
Jµ1 = Tµ1Jµ1 
Figure 2.4.1 Geometric interpretation of PI and VI in one dimension (a single state). Each policy µ defines the mapping Tµ, and TJ is the function minµ TµJ . When the number of policies is finite, TJ is a piecewise linear concave function, with each piece being a linear function TµJ that corresponds to a policy µ. The optimal cost function J! satisfies J! = TJ!, so it is obtained from the intersection of the graph of TJ and the 45 degree line shown. Similarly Jµ is the intersection of the graph of TµJ and the 45 degree line. The VI sequence is indicated in the top figure by the staircase construction, which asymptotically leads to J!. A single policy iteration is illustrated in the bottom figure, and illustrates the connection of PI with Newton’s method that was discussed in Section 1.3.2.
72 Contractive Models Chap. 2 
Similarly, we have for all m > 0, 
Tm µk+1Jµk ( TJµk ( Jµk , 
and by taking the limit as m $ ,, we obtain 
Jµk+1 ( TJµk ( Jµk , k = 0, 1, . . . . (2.22) 
If Jµk+1 = Jµk , it follows that TJµk = Jµk , so Jµk is a fixed point of T and must be equal to J*. Moreover by using induction, Eq. (2.22) implies that 
Jµk ( T kJµ0 , k = 0, 1, . . . . 
Since J* ( Jµk , lim 
k$% *T kJµ0 + J** = 0, 
it follows that limk$% *Jµk + J** = 0. Finally, if the number of policies is finite, Eq. (2.22) implies that there 
can be only a finite number of iterations for which Jµk+1(x) < Jµk (x) for some x. Thus we must have Jµk+1 = Jµk for some k, at which time Jµk = J* as shown earlier [cf. Eq. (2.22)]. Q.E.D. 
In the case where the set of policies is infinite, we may assert the convergence of the sequence of generated policies under some compactness and continuity conditions. In particular, we will assume that the state space is finite, X = {1, . . . , n}, and that each control constraint set U(x) is a compact subset of %m. We will view a cost function J as an element of %n, and a policy µ as an element of the set U(1) & · · · & U(n) " %mn, which is compact. Then {µk} has at least one limit point µ, which must be an admissible policy. The following proposition guarantees, under an additional continuity assumption for H(x, ·, ·), that every limit point µ is optimal. 
Assumption 2.4.1: (Compactness and Continuity) 
(a) The state space is finite, X = {1, . . . , n}. 
(b) Each control constraint set U(x), x = 1, . . . , n, is a compact subset of %m. 
(c) Each function H(x, ·, ·), x = 1, . . . , n, is continuous over U(x) & %n. 
Proposition 2.4.2: Let the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2 hold, together with Assumption 2.4.1, and let {µk} be a sequence generated by the PI algorithm. Then for every limit point µ of {µk}, we have Jµ = J".
Sec. 2.4 Policy Iteration 73 
Proof: We have Jµk $ J* by Prop. 2.4.1. Let µ be the limit of a subsequence {µk}k!K. We will show that TµJ* = TJ*, from which it follows that Jµ = J* [cf. Prop. 2.1.1(c)]. Indeed, we have TµJ* - TJ*, so we focus on showing the reverse inequality. From the equation 
TµkJµk"1 = TJµk"1 , 
we have 
H ! x, µk(x), Jµk"1 
" ( H(x, u, Jµk"1), x = 1, . . . , n, u ! U(x). 
By taking limit in this relation as k $ ,, k ! K, and by using the continuity of H(x, ·, ·) [cf. Assumption 2.4.1(c)], we obtain 
H ! x, µ(x), J* 
" ( H(x, u, J*), x = 1, . . . , n, u ! U(x). 
By taking the minimum of the right-hand side over u ! U(x), we obtain TµJ* ( TJ*. Q.E.D. 
2.4.1 Approximate Policy Iteration 
We now consider the PI method where the policy evaluation step and/or the policy improvement step of the method are implemented through approximations. This method generates a sequence of policies {µk} and a corresponding sequence of approximate cost functions {Jk} satisfying 
*Jk + Jµk* ( $, *Tµk+1Jk + TJk* ( ", k = 0, 1, . . . , (2.23) 
where $ and " are some scalars, and *·* denotes the weighted sup-norm (the one used in the contraction Assumption 2.1.2). The following proposition provides an error bound for this algorithm. 
Proposition 2.4.3: (Error Bound for Approximate PI) Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold. The sequence {µk} generated by the approximate PI algorithm (2.23) satisfies 
lim sup k$% 
*Jµk + J** ( "+ 2!$ 
(1+ !)2 . (2.24) 
The essence of the proof is contained in the following proposition, which quantifies the amount of approximate policy improvement at each iteration.
74 Contractive Models Chap. 2 
Proposition 2.4.4: Let the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2 hold. Let J , µ, and µ satisfy 
*J + Jµ* ( $, *TµJ + TJ* ( ", 
where $ and " are some scalars. Then 
*Jµ + J** ( !*Jµ + J**+ "+ 2!$ 
1+ ! . (2.25) 
Proof: We denote by v the weight function corresponding to the weighted sup-norm. Using the contraction property of T and Tµ, which implies that *TµJµ + TµJ* ( !$ and *TJ + TJµ* ( !$, and hence TµJµ ( TµJ + !$ v and TJ ( TJµ + !$ v, we have 
TµJµ ( TµJ + !$ v ( TJ + ("+ !$) v ( TJµ + ("+ 2!$) v. (2.26) 
Since TJµ ( TµJµ = Jµ, this relation yields 
TµJµ ( Jµ + ("+ 2!$) v, 
and applying Prop. 2.1.4(b) with µ = µ, J = Jµ, and c = " + 2!$, we obtain 
Jµ ( Jµ + "+ 2!$ 
1+ ! v. (2.27) 
Using this relation, we have 
Jµ = TµJµ = TµJµ + (TµJµ + TµJµ) ( TµJµ + !(" + 2!$) 
1+ ! v, 
where the inequality follows by using Prop. 2.1.3 and Eq. (2.27). Subtract-ing J* from both sides, we have 
Jµ + J* ( TµJµ + J* + !(" + 2!$) 
1+ ! v. (2.28) 
Also by subtracting J* from both sides of Eq. (2.26), and using the contraction property 
TJµ + J* = TJµ + TJ* ( !*Jµ + J** v, 
we obtain 
TµJµ + J* ( TJµ + J* + (" + 2!$) v ( !*Jµ + J** v + ("+ 2!$) v.
Sec. 2.4 Policy Iteration 75 
Combining this relation with Eq. (2.28), yields 
Jµ+J* ( !*Jµ+J** v+ !("+ 2!$) 
1+ ! v+("+!$)e = !*Jµ+J** v+ 
"+ 2!$ 
1+ ! v, 
which is equivalent to the desired relation (2.25). Q.E.D. 
Proof of Prop. 2.4.3: Applying Prop. 2.4.4, we have 
*Jµk+1 + J** ( !*Jµk + J**+ "+ 2!$ 
1+ ! , 
which by taking the lim sup of both sides as k $ , yields the desired result. Q.E.D. 
We note that the error bound of Prop. 2.4.3 is tight, as can be shown with an example from [BeT96], Section 6.2.3. The error bound is comparable to the one for approximate VI, derived earlier in Prop. 2.3.2. In particular, the error *Jµk+J** is asymptotically proportional to 1/(1+!)2 
and to the approximation error in policy evaluation or value iteration, respectively. This is noteworthy, as it indicates that contrary to the case of exact implementation, approximate PI need not hold a convergence rate advantage over approximate VI, despite its greater overhead per iteration. 
Note that when $ = " = 0, Eq. (2.25) yields 
*Jµk+1 + J** ( !*Jµk + J**. 
Thus in the case of an infinite state space and/or control space, exact PI converges at a geometric rate under the contraction and monotonicity assumptions of this section. This rate is the same as the rate of convergence of exact VI. It follows that judging solely from the point of view of rate of convergence estimates, exact PI holds an advantage over exact VI only when the number of states is finite. This raises the question what happens when the number of states is finite but very large. However, this question is not very interesting from a practical point of view, since for a very large number of states, neither VI or PI can be implemented in practice without approximations (see the discussion of Section 1.2.4). 
2.4.2 Approximate Policy Iteration Where Policies Converge 
Generally, the policy sequence {µk} generated by approximate PI may oscillate between several policies. However, under some circumstances this sequence may be guaranteed to converge to some µ, in the sense that 
µk+1 = µk = µ for some k. (2.29)
76 Contractive Models Chap. 2 
An example arises when the policy sequence {µk} is generated by exact PI applied with a di!erent mapping H̃ in place of H , but the policy evaluation and policy improvement error bounds of Eq. (2.23) are satisfied. The mapping H̃ may for example correspond to an approximation of the original problem (as in the aggregation methods of Example 1.2.10; see [Ber11c] and [Ber12a] for further discussion). In this case we can show the following bound, which is much more favorable than the one of Prop. 2.4.3. 
Proposition 2.4.5: (Error Bound for Approximate PI when Policies Converge) Let the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2 hold, and assume that the approximate PI algorithm (2.23) terminates with a policy µ that satisfies condition (2.29). Then we have 
*Jµ + J** ( "+ 2!$ 
1+ ! . (2.30) 
Proof: Let J̃ be the cost function obtained by approximate policy evaluation of µ [i.e., J̃ = Jk, where k satisfies the condition (2.29)]. Then we have 
*J̃ + Jµ* ( $, *TµJ̃ + T J̃* ( ", (2.31) 
where the latter inequality holds since we have 
*TµJ̃ + T J̃* = *T µk+1Jk + TJ 
k * ( ", 
cf. Eq. (2.23). Using Eq. (2.31) and the fact Jµ = TµJµ, we have 
*TJµ + Jµ* ( *TJµ + T J̃*+ *T J̃ + TµJ̃*+ *TµJ̃ + Jµ* 
= *TJµ + T J̃*+ *T J̃ + TµJ̃*+ *TµJ̃ + TµJµ* 
( !*Jµ + J̃*+ "+ !*J̃ + Jµ* 
( "+ 2!$. 
(2.32) 
Using Prop. 2.1.1(d) with J = Jµ, we obtain the error bound (2.30). Q.E.D. 
The preceding error bound can be extended to the case where two successive policies generated by the approximate PI algorithm are “not too di#erent” rather than being identical. In particular, suppose that µ and µ are successive policies, which in addition to 
*J̃ + Jµ* ( $, *TµJ̃ + T J̃* ( ", 
[cf. Eq. (2.23)], also satisfy 
*TµJ̃ + TµJ̃* ( ',
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 77 
where ' is some scalar (instead of µ = µ, which is the case where policies converge exactly). Then we also have 
*T J̃ + TµJ̃* ( *T J̃ + TµJ̃*+ *TµJ̃ + TµJ̃* ( "+ ', 
and by replacing " with "+ ' and µ with µ in Eq. (2.32), we obtain 
*Jµ + J"* ( " + ' + 2!$ 
1+ ! . 
When ' is small enough to be of the order of max{$, "}, this error bound is comparable to the one for the case where policies converge. 
2.5 OPTIMISTIC POLICY ITERATION AND (-POLICY ITERATION 
In this section, we discuss some variants of the PI algorithm of the preceding section, where the policy evaluation 
Jµk = TµkJµk 
is approximated by using VI. The most straightforward of these methods is optimistic PI (also called “modified” PI, see e.g., [Put94]), where a policy µk is evaluated approximately, using a finite number of VI. Thus, starting with a function J0 ! B(X), we generate sequences {Jk} and {µk} with the algorithm 
TµkJk = TJk, Jk+1 = Tmk 
µk Jk, k = 0, 1, . . . , (2.33) 
where {mk} is a sequence of positive integers (see Fig. 2.5.1, which shows one iteration of the method where mk = 3). There is no systematic guideline for selecting the integers mk. Usually their best values are chosen empirically, and tend to be considerably larger than 1 (in the case where mk / 1 the optimistic PI method coincides with the VI method). The convergence of this method is discussed in Section 2.5.1. 
Variants of optimistic PI include methods with approximations in the policy evaluation and policy improvement phases (Section 2.5.2), and methods where the number mk is randomized (Section 2.5.3). An interesting advantage of the latter methods is that they do not require the monotonicity Assumption 2.1.1 for convergence in problems with a finite number of policies. 
A method that is conceptually similar to the optimistic PI method is the (-PI method defined by 
TµkJk = TJk, Jk+1 = T ($) 
µk Jk, k = 0, 1, . . . , (2.34)
78 Contractive Models Chap. 2 
TJ = minµ TµJ 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Policy Improvement Exact Policy Evaluation Approximate Policy Evaluation 
J0 
= TJ0 
J Jµ0 = Tµ0Jµ0 
= TJ0 = Tµ0J0 
Tµ0J 
Approx. Policy Evaluation 
J1 = T 3 µ0 J0 
Figure 2.5.1 Illustration of optimistic PI in one dimension. In this example, the policy µ0 is evaluated approximately with just three applications of Tµ0 to yield 
J1 = T 3 µ0 
J0. 
where J0 is an initial function in B(X), and for any policy µ and scalar 
( ! (0, 1), T ($) µ is the multistep mapping defined by 
T ($) µ J = (1+ () 
%$ 
!=0 
(!T !+1 µ J, J ! B(X), 
(cf. Section 1.2.5). To compare optimistic PI and (-PI, note that they both involve multiple applications of the VI mapping Tµk : a fixed number mk 
in the former case, and a geometrically weighted number in the latter case. 
In fact, we may view the (-PI iterate T ($) 
µk Jk as the expected value of the 
optimistic PI iterate Tmk 
µk Jµk when mk is chosen by a geometric probability 
distribution with parameter (. One of the reasons that make (-PI interesting is its relation with 
TD(() and other temporal di#erence methods on one hand, and the proximal algorithm on the other. In particular, in (-PI a policy evaluation is performed with a single iteration of an extrapolated proximal algorithm; cf. the discussion of Section 1.2.5 and Exercise 1.2. Thus implementation
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 79 
of (-PI can benefit from the rich methodology that has developed around temporal di#erence and proximal methods. 
Generally the optimistic and (-PI methods have similar convergence properties. In this section, we focus primarily on optimistic PI, and we discuss briefly (-PI in Section 2.5.3, where we will prove convergence for a randomized version. For a convergence proof of (-PI without randomization in discounted stochastic optimal control and stochastic shortest path problems, see the paper [BeI96] and the book [BeT96] (Section 2.3.1). 
2.5.1 Convergence of Optimistic Policy Iteration 
We will now focus on the optimistic PI algorithm (2.33). The following two propositions provide its convergence properties. 
Proposition 2.5.1: (Convergence of Optimistic PI) Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, and let 
% (Jk, µk) 
& be a sequence generated by the optimistic PI algorithm 
(2.33). Then lim k$% 
*Jk + J** = 0, 
and if the number of policies is finite, we have Jµk = J* for all k 
greater than some index k̄. 
Proposition 2.5.2: Let the monotonicity and contraction Assump-tions 2.1.1 and 2.1.2 hold, together with Assumption 2.4.1, and let% (Jk, µk) 
& be a sequence generated by the optimistic PI algorithm 
(2.33). Then for every limit point µ of {µk}, we have Jµ = J". 
We develop the proofs of the propositions through four lemmas. The first lemma collects some properties of monotone weighted sup-norm contractions, variants of which we noted earlier and we restate for convenience. 
Lemma 2.5.1: Let W : B(X) #$ B(X) be a mapping that satisfies the monotonicity assumption 
J ( J # ) WJ ( WJ #, ' J, J # ! B(X), 
and the contraction assumption
80 Contractive Models Chap. 2 
*WJ +WJ #* ( !*J + J #*, ' J, J # ! B(X), 
for some ! ! (0, 1). 
(a) For all J, J # ! B(X) and scalar c - 0, we have 
J - J # + c v ) WJ - WJ # + !c v. (2.35) 
(b) For all J ! B(X), c - 0, and k = 0, 1, . . ., we have 
J - WJ + c v ) W kJ - J* + !k 
1+ ! c v, (2.36) 
WJ - J + c v ) J* - W kJ + !k 
1+ ! c v, (2.37) 
where J* is the fixed point of W . 
Proof: The proof of part (a) follows the one of Prop. 2.1.4(b), while the proof of part (b) follows the one of Prop. 2.1.4(c). Q.E.D. 
Lemma 2.5.2: Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, let J ! B(X) and c - 0 satisfy 
J - TJ + c v, 
and let µ ! M be such that TµJ = TJ . Then for all k > 0, we have 
TJ - T k µJ + 
! 
1+ ! c v, (2.38) 
and T k µJ - T (T k 
µJ)+ !kc v. (2.39) 
Proof: Since J - TJ + c v = TµJ + c v, by using Lemma 2.5.1(a) with W = T j 
µ and J # = TµJ , we have for all j - 1, 
T j µJ - T j+1 
µ J + !jc v. (2.40) 
By adding this relation over j = 1, . . . , k + 1, we have 
TJ = TµJ - T k µJ + 
k&1$ 
j=1 
!jc v = T k µJ + 
!+ !k 
1+ ! c v - T k 
µJ + ! 
1+ ! c v,
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 81 
showing Eq. (2.38). From Eq. (2.40) for j = k, we obtain 
T k µJ - T k+1 
µ J + !kc v = Tµ(T k µJ)+ !kc v - T (T k 
µJ)+ !kc v, 
showing Eq. (2.39). Q.E.D. 
The next lemma applies to the optimistic PI algorithm (2.33) and proves a preliminary bound. 
Lemma 2.5.3: Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, let 
% (Jk, µk) 
& be a sequence generated by the 
optimistic PI algorithm (2.33), and assume that for some c - 0 we have 
J0 - TJ0 + c v. 
Then for all k - 0, 
TJk + ! 
1+ ! &kc v - Jk+1 - TJk+1 + &k+1c v, (2.41) 
where &k is the scalar given by 
&k = 
' 1 if k = 0, !m0+···+mk"1 if k > 0, 
(2.42) 
with mj , j = 0, 1, . . ., being the integers used in the algorithm (2.33). 
Proof: We prove Eq. (2.41) by induction on k, using Lemma 2.5.2. For k = 0, using Eq. (2.38) with J = J0, µ = µ0, and k = m0, we have 
TJ0 - J1 + ! 
1+ ! c v = J1 + 
! 
1+ ! &0c v, 
showing the left-hand side of Eq. (2.41) for k = 0. Also by Eq. (2.39) with µ = µ0 and k = m0, we have 
J1 - TJ1 + !m0c v = TJ1 + &1c v. 
showing the right-hand side of Eq. (2.41) for k = 0. Assuming that Eq. (2.41) holds for k + 1 - 0, we will show that it 
holds for k. Indeed, the right-hand side of the induction hypothesis yields 
Jk - TJk + &kc v. 
Using Eqs. (2.38) and (2.39) with J = Jk, µ = µk, and k = mk, we obtain 
TJk - Jk+1 + ! 
1+ ! &kc v,
82 Contractive Models Chap. 2 
and Jk+1 - TJk+1 + !mk&kc v = TJk+1 + &k+1c v, 
respectively. This completes the induction. Q.E.D. 
The next lemma essentially proves the convergence of the optimistic PI (Prop. 2.5.1) and provides associated error bounds. 
Lemma 2.5.4: Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, let 
% (Jk, µk) 
& be a sequence generated by the 
optimistic PI algorithm (2.33), and let c - 0 be a scalar such that 
*J0 + TJ0* ( c. (2.43) 
Then for all k - 0, 
Jk + !k 
1+ ! c v - Jk + 
&k 
1+ ! c v - J* - Jk + 
(k + 1)!k 
1+ ! c v, (2.44) 
where &k is defined by Eq. (2.42). 
Proof: Using the relation J0 - TJ0+c v [cf. Eq. (2.43)] and Lemma 2.5.3, we have 
Jk - TJk + &kc v, k = 0, 1, . . . . 
Using this relation in Lemma 2.5.1(b) with W = T and k = 0, we obtain 
Jk - J* + &k 
1+ ! c v, 
which together with the fact !k - &k, shows the left-hand side of Eq. (2.44). 
Using the relation TJ0 - J0+ c v [cf. Eq. (2.43)] and Lemma 2.5.1(b) with W = T , we have 
J* - T kJ0 + !k 
1+ ! c v, k = 0, 1, . . . . (2.45) 
Using again the relation J0 - TJ0 + c v in conjunction with Lemma 2.5.3, we also have 
TJj - Jj+1 + ! 
1+ ! &jc v, j = 0, . . . , k + 1. 
Applying T k&j&1 to both sides of this inequality and using the monotonicity and contraction properties of T k&j&1, we obtain 
T k&jJj - T k&j&1Jj+1 + !k&j 
1+ ! &jc v, j = 0, . . . , k + 1,
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 83 
cf. Lemma 2.5.1(a). By adding this relation over j = 0, . . . , k+1, and using the fact &j ( !j , it follows that 
T kJ0 - Jk + k&1$ 
j=0 
!k&j 
1+ ! !jc v = Jk + 
k!k 
1+ ! c v. (2.46) 
Finally, by combining Eqs. (2.45) and (2.46), we obtain the right-hand side of Eq. (2.44). Q.E.D. 
Proof of Props. 2.5.1 and 2.5.2: Let c be a scalar satisfying Eq. (2.43). Then the error bounds (2.44) show that limk$% *Jk+J** = 0, i.e., the first part of Prop. 2.5.1. To show the second part (finite termination when the 
number of policies is finite), let .M be the finite set of nonoptimal policies. 
Then there exists " > 0 such that *Tµ̂J* + TJ** > " for all µ̂ ! .M, which 
implies that *Tµ̂Jk + TJk* > " for all µ̂ ! .M and k su"ciently large. This 
implies that µk /! .M for all k su"ciently large. The proof of Prop. 2.5.2 follows using the compactness and continuity Assumption 2.4.1, and the convergence argument of Prop. 2.4.2. Q.E.D. 
Convergence Rate Issues 
Let us consider the convergence rate bounds of Lemma 2.5.4 for optimistic PI, and write them in the form 
*J0 + TJ0* ( c ) Jk + (k + 1)!k 
1+ ! c v ( J* ( Jk + 
!m0+···+mk"1 
1+ ! c v. 
(2.47) We may contrast these bounds with the ones for VI, where 
*J0 + TJ0* ( c ) T kJ0 + !k 
1+ ! c v ( J* ( T kJ0 + 
!k 
1+ ! c v (2.48) 
[cf. Prop. 2.1.4(c)]. In comparing the bounds (2.47) and (2.48), we should also take into 
account the associated overhead for a single iteration of each method: optimistic PI requires at iteration k a single application of T and mk + 1 applications of Tµk (each being less time-consuming than an application of T ), while VI requires a single application of T . It can then be seen that the upper bound for optimistic PI is better than the one for VI (same bound for less overhead), while the lower bound for optimistic PI is worse than the one for VI (worse bound for more overhead). This suggests that the choice of the initial condition J0 is important in optimistic PI, and in particular it is preferable to have J0 - TJ0 (implying convergence to J* from above) rather than J0 ( TJ0 (implying convergence to J* from below). This is consistent with the results of other works, which indicate that the convergence properties of the method are fragile when the condition J0 - TJ0 does not hold (see [WiB93], [BeT96], [BeY10], [BeY12], [YuB13a]).
84 Contractive Models Chap. 2 
2.5.2 Approximate Optimistic Policy Iteration 
We will now derive error bounds for the case where the policy evaluation and policy improvement operations are approximate, similar to the nonoptimistic PI case of Section 2.4.1. In particular, we consider a method that generates a sequence of policies {µk} and a corresponding sequence of approximate cost functions {Jk} satisfying 
*Jk + Tmk 
µk Jk&1* ( $, *Tµk+1Jk + TJk* ( ", k = 0, 1, . . . , (2.49) 
[cf. Eq. (2.23)]. For example, we may compute (perhaps approximately, by simulation) the values (Tmk 
µk Jk&1)(x) for a subset of states x, and use a 
least squares fit of these values to select Jk from some parametric class of functions. 
We will prove the same error bound as for the nonoptimistic case, cf. Eq. (2.24). However, for this we will need the following condition, which is stronger than the contraction and monotonicity conditions that we have been using so far. 
Assumption 2.5.1: (Semilinear Monotonic Contraction) For all J ! B(X) and µ ! M, the functions TµJ and TJ belong to B(X). Furthermore, for some ! ! (0, 1), we have for all J, J # ! B(X), µ ! M, and x ! X , 
(TµJ #)(x) + (TµJ)(x) 
v(x) ( ! sup 
y!X 
J #(y)+ J(y) 
v(y) . (2.50) 
This assumption implies both the monotonicity and contraction As-sumptions 2.1.1 and 2.1.2, as can be easily verified. Moreover the assumption is satisfied in the discounted DP examples of Section 1.2, as well as the stochastic shortest path problem of Example 1.2.6. It holds if Tµ is a linear mapping involving a matrix with nonnegative components that has spectral radius less than 1 (or more generally if Tµ is the minimum or the maximum of a finite number of such linear mappings). 
For any function y ! B(X), let us use the notation 
M(y) = sup x!X 
y(x) 
v(x) . 
Then the condition (2.50) can be written for all J, J # ! B(X), and µ ! M as 
M(TµJ + TµJ #) ( !M(J + J #), (2.51)
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 85 
and also implies the following multistep versions, for ) - 1, 
T ! µJ + T ! 
µJ # ( !!M(J + J #)v, M(T ! µJ + T ! 
µJ #) ( !!M(J + J #), (2.52) 
which can be proved by induction using Eq. (2.51). We have the following proposition. 
Proposition 2.5.3: (Error Bound for Optimistic Approximate PI) Let Assumption 2.5.1 hold, in addition to the monotonicity and contraction Assumptions 2.1.1 and 2.1.2. Then the sequence {µk} generated by the optimistic approximate PI algorithm (2.49) satisfies 
lim sup k$% 
*Jµk + J** ( "+ 2!$ 
(1+ !)2 . 
Proof: Let us fix k - 1, and for simplicity let us assume that mk / m for some m, and denote 
J = Jk&1, J = Jk, µ = µk, µ̄ = µk+1, 
s = Jµ + Tm µ J, s̄ = Jµ̄ + Tm 
µ̄ J, t = Tm µ J + J*, t̄ = Tm 
µ̄ J + J*. 
We have Jµ + J* = Jµ + Tm 
µ J + Tm µ J + J* = s+ t. (2.53) 
We will derive recursive relations for s and t, which will also involve the residual functions 
r = TµJ + J, r̄ = Tµ̄J + J. 
We first obtain a relation between r and r̄. We have 
r̄ = Tµ̄J + J 
= (Tµ̄J + TµJ) + (TµJ + J) 
( (Tµ̄J + TJ) + ! TµJ + Tµ(Tm 
µ J) " + (Tm 
µ J + J) + ! Tm µ (TµJ)+ Tm 
µ J " 
( "v + !M(J + Tm µ J)v + $v + !mM(TµJ + J)v 
( (" + $)v + !$v + !mM(r)v, 
where the first inequality follows from Tµ̄J - TJ , and the second and third inequalities follow from Eqs. (2.49) and (2.52). From this relation we have 
M(r̄) ( ! " + (1 + !)$ 
" + &M(r),
86 Contractive Models Chap. 2 
where & = !m. Taking lim sup as k $ , in this relation, we obtain 
lim sup k$% 
M(r) ( "+ (1 + !)$ 
1+ & . (2.54) 
Next we derive a relation between s and r. We have 
s = Jµ + Tm µ J 
= Tm µ Jµ + Tm 
µ J 
( !mM(Jµ + J)v 
( !m 
1+ ! M(TµJ + J)v 
= !m 
1+ ! M(r)v, 
where the first inequality follows from Eq. (2.52) and the second inequality follows by using Prop. 2.1.4(b). Thus we have M(s) ( %m 
1&%M(r), from which by taking lim sup of both sides and using Eq. (2.54), we obtain 
lim sup k$% 
M(s) ( & ! "+ (1 + !)$ 
" 
(1 + !)(1 + &) . (2.55) 
Finally we derive a relation between t, t̄, and r. We first note that 
TJ + TJ* ( !M(J + J*)v 
= !M(J + Tm µ J + Tm 
µ J + J*)v 
( !M(J + Tm µ J)v + !M(Tm 
µ J + J*)v 
( !$v + !M(t)v. 
Using this relation, and Eqs. (2.49) and (2.52), we have 
t̄ = Tm µ̄ J + J* 
= (Tm µ̄ J + Tm&1 
µ̄ J) + · · ·+ (T 2 µ̄J + Tµ̄J) + (Tµ̄J + TJ) + (TJ + TJ*) 
( (!m&1 + · · ·+ !)M(Tµ̄J + J)v + "v + !$v + !M(t)v, 
so finally 
M(t̄) ( !+ !m 
1+ ! M(r̄) + (" + !$) + !M(t). 
By taking lim sup of both sides and using Eq. (2.54), it follows that 
lim sup k$% 
M(t) ( (! + &) 
! "+ (1 + !)$ 
" 
(1 + !)2(1+ &) + 
"+ !$ 
1+ ! . (2.56)
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 87 
We now combine Eqs. (2.53), (2.55), and (2.56). We obtain 
lim sup k$% 
M(Jµk + J*) ( lim sup k$% 
M(s) + lim sup k$% 
M(t) 
( & ! "+ (1 + !)$ 
" 
(1+ !)(1 + &) + 
(!+ &) ! "+ (1 + !)$ 
" 
(1+ !)2(1 + &) + 
"+ !$ 
1+ ! 
= 
! &(1 + !) + (!+ &) 
"! "+ (1 + !)$ 
" 
(1+ !)2(1 + &) + 
" + !$ 
1+ ! 
= ! ! "+ (1 + !)$ 
" 
(1+ !)2 + 
"+ !$ 
1+ ! 
= "+ 2!$ 
(1+ !)2 . 
This proves the result, since in view of Jµk - J*, we have M(Jµk + J*) = *Jµk + J**. Q.E.D. 
A remarkable fact is that approximate VI, approximate PI, and approximate optimistic PI have very similar error bounds (cf. Props. 2.3.2, 2.4.3, and 2.5.3). Approximate VI has a slightly better bound, but insignificantly so in practical terms. When approximate PI produces a convergent sequence of policies, the associated error bound is much better (cf. Prop. 2.4.5). However, special conditions are needed for convergence of policies in approximate PI. These conditions are fulfilled in some cases, notably including schemes where aggregation is used for policy evaluation (cf. Sec-tion 1.2.4). In other cases, including some where the projected equation is used for policy evaluation, approximate PI (both optimistic and nonoptimistic) will typically generate a cycle of policies satisfying the bound of Prop. 2.4.3; see Section 3.6 of the PI survey paper [Ber11c], or Chapter 6 of the book [Ber12a]. 
2.5.3 Randomized Optimistic Policy Iteration 
We will now consider a randomized version of the optimistic PI algorithm where the number mk of VI iterations in the kth policy evaluation is random, while the monotonicity assumption need not hold. We assume, however, that each policy mapping is a contraction in a suitable space, that the number of policies is finite, and that mk = 1 with positive probability (these assumptions can be modified and/or generalized in ways suggested by the subsequent line of proof). In particular, for each positive integer j, we have a probability p(j) - 0, where 
p(1) > 0, %$ 
j=1 
p(j) = 1.
88 Contractive Models Chap. 2 
We consider the algorithm 
TµkJk = TJk, Jk+1 = Tmk 
µk Jk, k = 0, 1, . . . , (2.57) 
where mk is chosen randomly according to the distribution p(j), 
P (mk = j) = p(j), j = 1, 2, . . . . (2.58) 
The selection of mk is independent of previous selections. We will assume the following. 
Assumption 2.5.2: Let * · * be a norm on some complete space of real-valued functions overX , denoted F(X), and assume the following. 
(a) The set of policies M is finite. 
(b) The mappings Tµ, µ ! M, and T are contraction mappings from F(X) into F(X). 
The preceding assumption requires that the number of policies is finite, but does not require any monotonicity condition (cf. Assumption 2.1.1), while its contraction condition (b) is weaker than the contraction Assumption 2.1.2 since F(X) is a general complete normed space, not necessarily B(X). This flexibility may be useful in algorithms that involve cost function approximation within a subspace of basis functions. For such algorithms, however, T does not necessarily have a unique fixed point, as discussed in Section 1.2.4. By contrast since F(X) is assumed complete, Assumption 2.5.2 implies that Tµ and T have unique fixed points, which we denote by Jµ and J*, respectively. 
An important preliminary fact (which relies on the finiteness of M) is given in the following proposition. The proposition implies that near J* 
the generated policies µk are “optimal” in the sense that Jµk = J*, so the algorithm does not tend to cycle. † 
Proposition 2.5.4: Let Assumption 2.5.2 hold, and let M" be the subset of all µ ! M such that TµJ* = TJ*. Then for all µ ! M", we have Jµ = J*. Moreover, there exists an " > 0 such that for all J with *J + J** < " we have TµJ = TJ only if µ ! M". 
Proof: If µ ! M", we have TµJ* = TJ* = J*. Thus J* is the unique fixed point Jµ of Tµ, and we have Jµ = J*. 
† Note that without monotonicity, J! need not have any formal optimality properties (cf. the discussion of Section 2.1 and Example 2.1.1).
Sec. 2.5 Optimistic Policy Iteration and &-Policy Iteration 89 
To prove the second assertion, we argue by contradiction, so we assume that there exist a sequence of scalars {"k} and a sequence of policies {µk} such that "k 0 0 and 
µk /! M", TµkJk = TJk, *Jk + J** < "k, ' k = 0, 1, . . . . 
Since M is finite, we may assume without loss of generality that for some µ /! M", we have µk = µ for all k, so from the preceding relation we have 
TµJk = TJk, *Jk + J** < "k, ' k = 0, 1, . . . . 
Thus *Jk +J** $ 0, and by the contraction Assumption 2.5.2(b), we have 
*TµJk + TµJ** $ 0, *TJk + TJ** $ 0. 
Since TµJk = TJk, the limits of {TµJk} and {TJk} are equal, i.e., TµJ* = TJ* = J*. Since Jµ is the unique fixed point of Tµ over F(X), it follows that Jµ = J*, contradicting the earlier hypothesis that µ /! M". Q.E.D. 
The preceding proof illustrates the key idea of the randomized optimistic PI algorithm, which is that for µ ! M", the mappings Tmk 
µ have a common fixed point that is equal to J*, the fixed point of T . Thus within a distance " from J*, the iterates (2.57) aim consistently at J*. Moreover, because the probability of a VI (an iteration with mk = 1) is positive, the algorithm is guaranteed to eventually come within " from J* through a su"ciently long sequence of contiguous VI iterations. For this we need the sequence {Jk} to be bounded, which will be shown as part of the proof of the following proposition. 
Proposition 2.5.5: Let Assumption 2.5.2 hold. Then for any starting point J0 ! F(X), a sequence {Jk} generated by the randomized optimistic PI algorithm (2.57)-(2.58) belongs to F(X) and converges to J* with probability one. 
Proof: We will show that {Jk} is bounded by showing that for all k, we have 
max µ!M 
*Jk + Jµ* ( *k max µ!M 
*J0 + Jµ*+ 1 
1+ * max 
µ,µ#!M *Jµ + Jµ#*, (2.59) 
where * is a common contraction modulus of Tµ, µ ! M, and T . Indeed, we have for all µ ! M 
*Jk + Jµ* ( *Jk + Jµk"1*+ *Jµk"1 + Jµ* 
= *T mk"1 
µk"1 Jk&1 + Jµk"1*+ *Jµk"1 + Jµ* 
( *mk"1*Jk&1 + Jµk"1*+ *Jµk"1 + Jµ* 
( *mk"1 max µ!M 
*Jk&1 + Jµ*+ max µ,µ#!M 
*Jµ + Jµ#* 
( *max µ!M 
*Jk&1 + Jµ*+ max µ,µ#!M 
*Jµ + Jµ#*,
90 Contractive Models Chap. 2 
and finally, for all k, 
max µ!M 
*Jk + Jµ* ( *max µ!M 
*Jk&1 + Jµ*+ max µ,µ#!M 
*Jµ + Jµ#*. 
From this relation, we obtain Eq. (2.59) by induction. Thus in conclusion, we have {Jk} " D, where D is the bounded set 
D = 
' J ### max 
µ!M *J + Jµ* ( max 
µ!M *J0 + Jµ*+ 
1 
1+ * max 
µ,µ#!M *Jµ + Jµ#* 
/ . 
We use this fact to argue that with enough contiguous value iterations, i.e., iterations where mk = 1, Jk can be brought arbitrarily close to J*, and once this happens, the algorithm operates like the ordinary VI algorithm. 
Indeed, each time the iteration Jk+1 = TJk is performed (i.e., when mk = 1), the distance of the iterate Jk from J* is reduced by a factor *, i.e., *Jk+1 + J** ( **Jk + J**. Since {Jk} belongs to the bounded set D, and our randomization scheme includes the condition p(1) > 0, the algorithm is guaranteed (with probability one) to eventually execute a su"cient number of contiguous iterations Jk+1 = TJk to enter a sphere 
S" = % J ! F(X) | *J + J** < " 
& 
of small enough radius " to guarantee that the generated policy µk belongs to M", as per Prop. 2.5.4. Once this happens, all subsequent iterations reduce the distance *Jk + J** by a factor * at every iteration, since 
))Tm µ J +J** ( **Tm&1 
µ J +J** ( **J +J**, ' µ ! M", m - 1, J ! S". 
Thus once {Jk} enters S", it stays within S" and converges to J*. Q.E.D. 
A Randomized Version of (-Policy Iteration 
We now turn to the (-PI algorithm. Instead of the nonrandomized version 
TµkJk = TJk, Jk+1 = T ($) 
µk Jk, k = 0, 1, . . . , 
cf. Eq. (2.34), we consider a randomized version that involves a fixed probability p ! (0, 1). It has the form 
TµkJk = TJk, Jk+1 = 
' TJk with probability p, 
T ($) 
µk Jk with probability 1+ p. (2.60) 
The idea of the algorithm is similar to the one of the randomized optimistic PI algorithm (2.57)-(2.58). Under the assumptions of Prop.
Sec. 2.6 Asynchronous Algorithms 91 
2.5.5, the sequence {Jk} generated by the randomized (-PI algorithm (2.60) belongs to F(X) and converges to J* with probability one. The reason is that the contraction property of Tµ over F(X) with respect to the norm *·* 
implies that T ($) µ is well-defined, and also implies that T ($) 
µ is a contraction over F(X). The latter assertion follows from the calculation 
))T ($) µ J + Jµ 
)) = 
)))))(1 + () %$ 
!=0 
(!T !+1 µ J + (1+ () 
%$ 
!=0 
(!Jµ 
))))) 
( (1+ () %$ 
!=0 
(! ))T !+1 
µ J + Jµ )) 
( (1+ () %$ 
!=0 
(!*!+1*J + Jµ* 
= * *J + Jµ*, 
where the first inequality follows from the triangle inequality, and the second inequality follows from the contraction property of Tµ. Given that 
T ($) µ is a contraction, the proof of Prop. 2.5.5 goes through with mini-
mal changes. The idea again is that {Jk} remains bounded, and through a su"ciently long sequence of contiguous iterations where the iteration xk+1 = TJk is performed, it enters the sphere S", and subsequently stays within S" and converges to J*. 
The convergence argument just given suggests that the choice of the randomization probability p is important. If p is too small, convergence may be slow because oscillatory behavior may go unchecked for a long time. On the other hand if p is large, a correspondingly large number of fixed point iterations xk+1 = TJk may be performed, and the hoped for 
benefits of the use of the proximal iterations xk+1 = T ($) 
µk Jk may be lost. 
Adaptive schemes that adjust p based on algorithmic progress may address this issue. Similarly, the choice of the probability p(1) is significant in the randomized optimistic PI algorithm (2.57)-(2.58). 
2.6 ASYNCHRONOUS ALGORITHMS 
In this section, we extend further the computational methods of VI and PI for abstract DP models, by embedding them within an asynchronous computation framework. 
2.6.1 Asynchronous Value Iteration 
Each VI of the form given in Section 2.3 applies the mapping T defined by 
(TJ)(x) = inf u!U(x) 
H(x, u, J), ' x ! X,
92 Contractive Models Chap. 2 
for all states simultaneously, thereby producing the sequence TJ, T 2J, . . . starting with some J ! B(X). In a more general form of VI, at any one iteration, J(x) may be updated and replaced by (TJ)(x) only for a subset of states. An example is the Gauss-Seidel method for the finite-state case, where at each iteration, J(x) is updated only for a single selected state x and J(x) is left unchanged for all other states x .= x (see [Ber12a]). In that method the states are taken up for iteration in a cyclic order, but more complex iteration orders are possible, deterministic as well as randomized. 
Methods of the type just described are called asynchronous VI methods and may be motivated by several considerations such as: 
(a) Faster convergence. Generally, computational experience with DP as well as analysis, have shown that convergence is accelerated by incorporating the results of VI updates for some states as early as possible into subsequent VI updates for other states. This is known as the Gauss-Seidel e!ect , which is discussed in some detail in the book [BeT89]. 
(b) Parallel and distributed asynchronous computation. In this context, we have several processors, each applying VI for a subset of states, and communicating the results to other processors (perhaps with some delay). One objective here may be faster computation by taking advantage of parallelism. Another objective may be computational convenience in problems where useful information is generated and processed locally at geographically dispersed points. An example is data or sensor network computations, where nodes, gateways, sensors, and data collection centers collaborate to route and control the flow of data, using DP or shortest path-type computations. 
(c) Simulation-based implementations . In simulation-based versions of VI, iterations at various states are often performed in the order that the states are generated by some form of simulation. 
With these contexts in mind, we introduce a model of asynchronous distributed solution of abstract fixed point problems of the form J = TJ . Let R(X) be the set of real-valued functions defined on some given set X and let T map R(X) into R(X). We consider a partition of X into disjoint nonempty subsets X1, . . . , Xm, and a corresponding partition of J as J = (J1, . . . , Jm), where J! is the restriction of J on the set X!. Our computation framework involves a network of m processors, each updating corresponding components of J . In a (synchronous) distributed VI algorithm, processor ) updates J! at iteration t according to 
J t+1 ! (x) = T (J t 
1, . . . , J t m)(x), ' x ! X!, ) = 1, . . . ,m. 
Here to accommodate the distributed algorithmic framework and its overloaded notation, we will use superscript t to denote iterations/times where
Sec. 2.6 Asynchronous Algorithms 93 
some (but not all) processors update their corresponding components, re-serving the index k for computation stages involving all processors, and also reserving subscript ) to denote component/processor index. 
In an asynchronous VI algorithm, processor ) updates J! only for t in a selected subset R! of iterations, and with components Jj , j .= ), supplied by other processors with communication “delays” t+ +!j(t), 
J t+1 ! (x) = 
0 T 1 J&"1(t) 1 , . . . , J&"m(t) 
m 
2 (x) if t ! R!, x ! X!, 
J t ! (x) if t /! R!, x ! X!. 
(2.61) 
Communication delays arise naturally in the context of asynchronous distributed computing systems of the type described in many sources (an extensive reference is the book [BeT89]). Such systems are interesting for solution of large DP problems, particularly for methods that are based on simulation, which is naturally well-suited for distributed computation. On the other hand, if the entire algorithm is centralized at a single physical processor, the algorithm (2.61) ordinarily will not involve communication delays, i.e., +!j(t) = t for all ), j, and t. 
The simpler case where X is a finite set and each subset X! consists of a single element ) arises often, particularly in the context of simulation. In this case we may simplify the notation of iteration (2.61) by writing J t 
! 
in place of the scalar component J t !()), as we do in the following example. 
Example 2.6.1 (One-State-at-a-Time Iterations) 
Assuming X = {1, . . . , n}, let us view each state as a processor by itself, so that X" = {'}, ' = 1, . . . , n. Consider a VI algorithm that executes one-state-at-a-time, according to some state sequence {x0, x1, . . .}, which is generated in some way, possibly by simulation. Thus, starting from some initial vector J0, we generate a sequence {Jt}, with Jt = (Jt 
1, . . . , J t n), as follows: 
Jt+1 " = 
' T (Jt 
1, . . . , J t n)(') if ' = xt, 
Jt " if ' &= xt, 
where T (Jt 1, . . . , J 
t n)(') denotes the '-th component of the vector 
T (Jt 1, . . . , J 
t n) = TJt, 
and for simplicity we write Jt " instead of Jt 
" ('). This algorithm is a special case of iteration (2.61) where the set of times at which J" is updated is 
R" = {t | xt = '}, 
and there are no communication delays (as in the case where the entire algorithm is centralized at a single physical processor).
94 Contractive Models Chap. 2 
Note also that if X is finite, we can assume without loss of generality that each state is assigned to a separate processor. The reason is that a physical processor that updates a group of states may be replaced by a group of fictitious processors, each assigned to a single state, and updating their corresponding components of J simultaneously. 
We will now discuss the convergence of the asynchronous algorithm (2.61). To this end we introduce the following assumption. 
Assumption 2.6.1: (Continuous Updating and Information Renewal) 
(1) The set of times R! at which processor ) updates J! is infinite, for each ) = 1, . . . ,m. 
(2) limt$% +!j(t) = , for all ), j = 1, . . . ,m. 
Assumption 2.6.1 is natural, and is essential for any kind of convergence result about the algorithm. † In particular, the condition +!j(t) $ , guarantees that outdated information about the processor updates will eventually be purged from the computation. It is also natural to assume that +!j(t) is monotonically increasing with t, but this assumption is not necessary for the subsequent analysis. 
We wish to show that J t ! $ J" 
! for all ), and to this end we employ the following convergence theorem for totally asynchronous iterations from the author’s paper [Ber83], which has served as the basis for the treatment of totally asynchronous iterations in the book [BeT89] (Chapter 6), and their application to DP (i.e., VI and PI), and asynchronous gradient-based optimization. For the statement of the theorem, we say that a sequence {Jk} " R(X) converges pointwise to J ! R(X) if 
lim k$% 
Jk(x) = J(x) 
for all x ! X . 
Proposition 2.6.1 (Asynchronous Convergence Theorem): Let T have a unique fixed point J*, let Assumption 2.6.1 hold, and assume that there is a sequence of nonempty subsets 
% S(k) 
& " R(X) with 
† Generally, convergent distributed iterative asynchronous algorithms are 
classified in totally and partially asynchronous [cf. the book [BeT89] (Chapters 6 and 7), or the more recent survey in the book [Ber16c] (Section 2.5)]. In the 
former, there is no bound on the communication delays, while in the latter there 
must be a bound (which may be unknown). The algorithms of the present section are totally asynchronous, as reflected by Assumption 2.6.1.
Sec. 2.6 Asynchronous Algorithms 95 
S(k + 1) " S(k), k = 0, 1, . . . , 
and is such that if {V k} is any sequence with V k ! S(k), for all k - 0, then {V k} converges pointwise to J*. Assume further the following: 
(1) Synchronous Convergence Condition: We have 
TJ ! S(k + 1), ' J ! S(k), k = 0, 1, . . . . 
(2) Box Condition: For all k, S(k) is a Cartesian product of the form 
S(k) = S1(k)& · · ·& Sm(k), 
where S!(k) is a set of real-valued functions on X!, ) = 1, . . . ,m. 
Then for every J0 ! S(0), the sequence {J t} generated by the asynchronous algorithm (2.61) converges pointwise to J*. 
Proof: To explain the idea of the proof, let us note that the given conditions imply that updating any component J!, by applying T to a function J ! S(k), while leaving all other components unchanged, yields a function in S(k). Thus, once enough time passes so that the delays become “irrelevant,” then after J enters S(k), it stays within S(k). Moreover, once a component J! enters the subset S!(k) and the delays become “irrelevant,” J! gets permanently within the smaller subset S!(k+1) at the first time that J! is iterated on with J ! S(k). Once each component J!, ) = 1, . . . ,m, gets within S!(k + 1), the entire function J is within S(k + 1) by the Box Condition. Thus the iterates from S(k) eventually get into S(k + 1) and so on, and converge pointwise to J* in view of the assumed properties of {S(k)}. 
With this idea in mind, we show by induction that for each k - 0, there is a time tk such that: 
(1) J t ! S(k) for all t - tk. 
(2) For all ) and t ! R! with t - tk, we have 
1 J&"1(t) 1 , . . . , J&"m(t) 
m 
2 ! S(k). 
[In words, after some time, all fixed point estimates will be in S(k) and all estimates used in iteration (2.61) will come from S(k).] 
The induction hypothesis is true for k = 0 since J0 ! S(0). Assuming it is true for a given k, we will show that there exists a time tk+1 with the required properties. For each ) = 1, . . . ,m, let t()) be the first element of R! such that t()) - tk. Then by the Synchronous Convergence Condition,
96 Contractive Models Chap. 2 
S(0) (0) S(k) 
) S(k + 1) + 1) J! 
! J = (J1, J2) 
S1(0) 
(0) S2(0) TJ 
Figure 2.6.1 Geometric interpretation of the conditions of asynchronous convergence theorem. We have a nested sequence of boxes {S(k)} such that TJ ! S(k + 1) for all J ! S(k). 
we have TJ t(!) ! S(k + 1), implying (in view of the Box Condition) that 
J t(!)+1 ! ! S!(k + 1). 
Similarly, for every t ! R!, t - t()), we have J t+1 ! ! S!(k + 1). Between 
elements of R!, J t ! does not change. Thus, 
J t ! ! S!(k + 1), ' t - t()) + 1. 
Let t#k = max! % t()) 
& + 1. Then, using the Box Condition we have 
J t ! S(k + 1), ' t - t#k. 
Finally, since by Assumption 2.6.1, we have +!j(t) $ , as t $ ,, t ! R!, we can choose a time tk+1 - t#k that is su"ciently large so that +!j(t) - t#k for all ), j, and t ! R! with t - tk+1. We then have, for all t ! R! 
with t - tk+1 and j = 1, . . . ,m, J &"j(t) j ! Sj(k + 1), which (by the Box 
Condition) implies that 
1 J&"1(t) 1 , . . . , J&"m(t) 
m 
2 ! S(k + 1). 
The induction is complete. Q.E.D. 
Figure 2.6.1 illustrates the assumptions of the preceding convergence theorem. The challenge in applying the theorem is to identify the set sequence 
% S(k) 
& and to verify the assumptions of Prop. 2.6.1. In abstract 
DP, these assumptions are satisfied in two primary contexts of interest. The first is when S(k) are weighted sup-norm spheres centered at J*, and can be used in conjunction with the contraction framework of the preceding section (see the following proposition). The second context is based on monotonicity conditions. It will be used in Section 3.6 in conjunction
Sec. 2.6 Asynchronous Algorithms 97 
S(0) (0) S(k) 
) S(k + 1) + 1) J! 
! J = (J1, J2) 
J1 Iterations 
Iterations J2 Iteration 
Figure 2.6.2 Geometric interpretation of the mechanism for asynchronous convergence. Iteration on a single component of a function J ! S(k), say J", keeps J 
in S(k), while it moves J" into the corresponding component S"(k+1) of S(k+1), where it remains throughout the subsequent iterations. Once all components J" have been iterated on at least once, the iterate is guaranteed to be in S(k + 1). 
with semicontractive models for which there is no underlying sup-norm contraction. It is also relevant to the noncontractive models of Section 4.3 where again there is no underlying contraction. Figure 2.6.2 illustrates the mechanism by which asynchronous convergence is achieved. 
We note a few extensions of the theorem. It is possible to allow T to be time-varying, so in place of T we operate with a sequence of mappings Tk, k = 0, 1, . . .. Then if all Tk have a common fixed point J*, the conclusion of the theorem holds (see Exercise 2.2 for a more precise statement). This extension is useful in some of the algorithms to be discussed later. Another extension is to allow T to have multiple fixed points and introduce an assumption that roughly says that 1% 
k=0S(k) is the set of fixed points. Then the conclusion is that any limit point (in an appropriate sense) of {J t} is a fixed point. 
We now apply the preceding convergence theorem to the totally asynchronous VI algorithm under the contraction assumption. Note that the monotonicity Assumption 2.1.1 is not necessary (just like it is not needed for the synchronous convergence of {T kJ} to J*). 
Proposition 2.6.2: Let the contraction Assumption 2.1.2 hold, together with Assumption 2.6.1. Then if J0 ! B(X), a sequence {J t} generated by the asynchronous VI algorithm (2.61) converges to J*. 
Proof: We apply Prop. 2.6.1 with 
S(k) = % J ! B(X) | *Jk + J** ( !k*J0 + J** 
& , k = 0, 1, . . . . 
Since T is a contraction with modulus !, the synchronous convergence
98 Contractive Models Chap. 2 
condition is satisfied. Since T is a weighted sup-norm contraction, the box condition is also satisfied, and the result follows. Q.E.D. 
2.6.2 Asynchronous Policy Iteration 
We will now develop asynchronous PI algorithms that have comparable properties to the asynchronous VI algorithm of the preceding subsection. The processors collectively maintain and update an estimate J t of the optimal cost function, and an estimate µt of an optimal policy. The local portions of J t and µt of processor ) are denoted J t 
! and µt !, respectively, 
i.e., J t !(x) = J t(x) and µt 
!(x) = µt(x) for all x ! X!. For each processor ), there are two disjoint subsets of times R!,R! " 
{0, 1, . . .}, corresponding to policy improvement and policy evaluation iterations, respectively. At the times t ! R! 2R!, the local cost function J t 
! of 
processor ) is updated using “delayed” local costs J &"j(t) j of other processors 
j .= ), where 0 ( +!j(t) ( t. At the times t ! R! (the local policy improvement times), the local policy µt 
! is also updated. For various choices of R! 
and R!, the algorithm takes the character of VI (when R! = {0, 1, . . .}), and PI (when R! contains a large number of time indices between successive elements of R!). As before, we view t + +!j(t) as a “communication delay,” and we require Assumption 2.6.1. † 
In a natural asynchronous version of optimistic PI, at each time t, each processor ) does one of the following: 
(a) Local policy improvement : If t ! R!, processor ) sets for all x ! X!, 
J t+1 ! (x) = min 
u!U(x) H ! x, u, J&"1(t) 
1 , . . . , J&"m(t) m 
" , (2.62) 
µt+1 ! (x) ! arg min 
u!U(x) H ! x, u, J&"1(t) 
1 , . . . , J&"m(t) m 
" . (2.63) 
(b) Local policy evaluation: If t ! R!, processor ) sets for all x ! X!, 
J t+1 ! (x) = H 
! x, µt(x), J&"1(t) 
1 , . . . , J&"m(t) m 
" , (2.64) 
and leaves µ! unchanged, i.e., µ t+1 ! (x) = µt 
!(x) for all x ! X!. 
(c) No local change: If t /! R! 2 R!, processor ) leaves J! and µ! unchanged, i.e., J t+1 
! (x) = J t !(x) and µt+1 
! (x) = µt !(x) for all x ! X!. 
Unfortunately, even when implemented without the delays +!j(t), the preceding PI algorithm is unreliable. The di"culty is that the algorithm 
† As earlier in all PI algorithms we assume that the infimum over u " U(x) 
in the policy improvement operation is attained, and we write min in place of inf.
Sec. 2.6 Asynchronous Algorithms 99 
involves a mix of applications of T and various mappings Tµ that have different fixed points, so in the absence of some systematic tendency towards J* there is the possibility of oscillation (see Fig. 2.6.3). While this does not happen in synchronous versions (cf. Prop. 2.5.1), asynchronous versions of the algorithm (2.33) may oscillate unless J0 satisfies some special condition (examples of this type of oscillation have been constructed in the paper [WiB93]; see also [Ber10], which translates an example from [WiB93] to the notation of the present book). 
In this subsection and the next we will develop two distributed asynchronous PI algorithms, each embodying a distinct mechanism that precludes the oscillatory behavior just described. In the first algorithm, there is a simple randomization scheme, according to which a policy evaluation of the form (2.64) is replaced by a policy improvement (2.62)-(2.63) with some positive probability. In the second algorithm, given in Section 2.6.3, we introduce a mapping Fµ, which has a common fixed point property: its fixed point is related to J* and is the same for all µ, so the anomaly illustrated in Fig. 2.6.3 cannot occur. The first algorithm is simple but requires some restrictions, including that the set of policies is finite. The second algorithm is more sophisticated and does not require this restriction. Both of these algorithms do not require the monotonicity assumption. 
An Optimistic Asynchronous PI Algorithmwith Randomization 
We introduce a randomization scheme for avoiding oscillatory behavior. It is defined by a small probability p > 0, according to which a policy evaluation iteration is replaced by a policy improvement iteration with probability p, independently of the results of past iterations. We model this randomization by assuming that before the algorithm is started, we restructure the sets R! and R! as follows: we take each element of each set R!, and with probability p, remove it from R!, and add it to R! (independently of other elements). We will assume the following: 
Assumption 2.6.2: 
(a) The set of policies M is finite. 
(b) There exists an integer B - 0 such that 
(R! 2R!) 1 {+ | t < + ( t+B} .= Ø, ' t, ). 
(c) There exists an integer B# - 0 such that 
0 ( t+ +!j(t) ( B#, ' t, ), j.
100 Contractive Models Chap. 2 
Nonmonotone Optimistic PI! Jµ 
µ Jµ! 
! Jµ!!J 
Monotone Optimistic PI 
J! 
!!Jµ0 Jµ1 
1 Jµ2 
TJ J0 
Figure 2.6.3 Illustration of optimistic asynchronous PI under the monotonicity and the contraction assumptions. When started with J0 and µ0 satisfying 
J0 " TJ0 = Tµ0J0, 
the algorithm converges monotonically to J! (see the trajectory on the right). However, for other initial conditions, there is a possibility for oscillations, since with changing values of µ, the mappings Tµ have di!erent fixed points and “aim at di!erent targets” (see the trajectory on the left, which illustrates a cycle between three policies µ, µ#, µ##). It turns out that such oscillations are not possible when the algorithm is implemented synchronously (cf. Prop. 2.5.1), but may occur in asynchronous implementations. 
Assumption 2.6.2 guarantees that each processor ) will execute at least one policy evaluation or policy improvement iteration within every block of B consecutive iterations, and places a bound B# on the communication delays. The convergence of the algorithm is shown in the following proposition. 
Proposition 2.6.3: Under the contraction Assumption 2.1.2, and As-sumptions 2.6.1, and 2.6.2, for the preceding algorithm with randomization, we have 
lim t$% 
J t(x) = J*(x), ' x ! X, 
with probability one. 
Proof: Let J* and Jµ be the fixed points of T and Tµ, respectively, and denote by M" the set of optimal policies: 
M" = {µ ! M | Jµ = J*} = {µ ! M | TµJ* = TJ*}.
Sec. 2.6 Asynchronous Algorithms 101 
We will show that the algorithm eventually (with probability one) enters a small neighborhood of J* within which it remains, generates policies in M", becomes equivalent to asynchronous VI, and therefore converges to J* by Prop. 2.6.2. The idea of the proof is twofold; cf. Props. 2.5.4 and 2.5.5. 
(1) There exists a small enough weighted sup-norm sphere centered at J*, call it S", within which policy improvement generates only policies in M", so policy evaluation with such policies as well as policy improvement keep the algorithm within S" if started there, and reduce the weighted sup-norm distance to J*, in view of the contraction and common fixed point property of T and Tµ, µ ! M". This is a consequence of Prop. 2.3.1 [cf. Eq. (2.16)]. 
(2) With probability one, thanks to the randomization device, the algorithm will eventually enter permanently S" with a policy in M". 
We now establish (1) and (2) in suitably refined form to account for the presence of delays and asynchronism. As in the proof of Prop. 2.5.5, we can prove that given J0, we have that {J t} " D, where D is a bounded set that depends on J0. We define 
S(k) = % J | *J + J** ( !kc 
& , 
where c is su"ciently large so that D " S(0). Then J t ! D and hence J t ! S(0) for all t. 
Let k" be such that 
J ! S(k") and TµJ = TJ ) µ ! M". (2.65) 
Such a k" exists in view of the finiteness of M and Prop. 2.3.1 [cf. Eq. (2.16)]. 
We now claim that with probability one, for any given k - 1, J t 
will eventually enter S(k) and stay within S(k) for at least B# additional consecutive iterations. This is because our randomization scheme is such that for any t and k, with probability at least pk(B+B#) the next k(B+B#) iterations are policy improvements, so that 
J t+k(B+B#)&' ! S(k) 
for all , with 0 ( , < B# [if t - B# + 1, we have J t&' ! S(0) for all , with 0 ( , < B#, so J t+B+B# 
&' ! S(1) for 0 ( , < B#, which implies that J t+2(B+B#)&' ! S(2) for 0 ( , < B#, etc]. 
It follows that with probability one, for some t we will have J& ! S(k") for all + with t + B# ( + ( t, as well as µt ! M" [cf. Eq. (2.65)]. Based on property (2.65) and the definition (2.63)-(2.64) of the algorithm, we see that at the next iteration, we have µt+1 ! M" and 
*J t+1 + J** ( *J t + J** ( !k!c,
102 Contractive Models Chap. 2 
so J t+1 ! S(k"); this is because in view of J µt = J*, and the contraction 
property of T and T µt , we have 
##J t+1 ! (x)+ J* 
! (x) ## 
v(x) ( !*J t + J** ( !k!+1c, (2.66) 
for all x ! X! and ) such that t ! R! 2R!, while 
J t+1(x) = J t(x) 
for all other x. Proceeding similarly, it follows that for all t > t we will have 
J& ! S(k"), ' t with t+B# ( + ( t, 
as well as µt ! M". Thus, after at most B iterations following t [after all components J! are updated through policy evaluation or policy improvement at least once so that 
##J t+1 ! (x)+ J* 
! (x) ## 
v(x) ( !*J t + J** ( !k!+1c, 
for every i, x ! X!, and some t with t ( t < t+ B, cf. Eq. (2.66)], J t will enter S(k" + 1) permanently, with µt ! M" (since µt ! M" for all t - t as shown earlier). Then, with the same reasoning, after at most another B# +B iterations, J t will enter S(k" +2) permanently, with µt ! M", etc. Thus J t will converge to J* with probability one. Q.E.D. 
The proof of Prop. 2.6.3 shows that eventually (with probability one after some iteration) the algorithm will become equivalent to asynchronous VI (each policy evaluation will produce the same results as a policy improvement), while generating optimal policies exclusively. However, the expected number of iterations for this to happen can be very large. More-over the proof depends on the set of policies being finite. These observations raise questions regarding the practical e#ectiveness of the algorithm. However, it appears that for many problems the algorithm works well, particularly when oscillatory behavior is a rare occurrence. 
A potentially important issue is the choice of the randomization probability p. If p is too small, convergence may be slow because oscillatory behavior may go unchecked for a long time. On the other hand if p is large, a correspondingly large number of policy improvement iterations may be performed, and the hoped for benefits of optimistic PI may be lost. Adaptive schemes which adjust p based on algorithmic progress may be an interesting possibility for addressing this issue.
Sec. 2.6 Asynchronous Algorithms 103 
2.6.3 Optimistic Asynchronous Policy Iteration with a Uniform Fixed Point 
We will now discuss another approach to address the convergence di"culties of the “natural” asynchronous PI algorithm (2.62)-(2.64). As illustrated in Fig. 2.6.3 in connection with optimistic PI, the mappings T and Tµ have di#erent fixed points. As a result, optimistic and distributed PI, which involve an irregular mixture of applications of Tµ and T , do not have a “consistent target” at which to aim. 
With this in mind, we introduce a new mapping that is parametrized by µ and has a common fixed point for all µ, which in turn yields J*. This mapping is a weighted sup-norm contraction with modulus !, so it may be used in conjunction with asynchronous VI and PI. An additional benefit is that the monotonicity Assumption 2.1.1 is not needed to prove convergence in the analysis that follows; the contraction Assumption 2.1.2 is su"cient (see Exercise 2.3 for an application). 
The mapping operates on a pair (V,Q) where: 
 V is a function with a component V (x) for each x (in the DP context it may be viewed as a cost function). 
 Q is a function with a component Q(x, u) for each pair (x, u) [in the DP context Q(x, u), is known as a Q-factor ]. 
The mapping produces a pair 
! MFµ(V,Q), Fµ(V,Q) 
" , 
where 
 Fµ(V,Q) is a function with a component Fµ(V,Q)(x, u) for each (x, u), defined by 
Fµ(V,Q)(x, u) = H ! x, u,min{V,Qµ} 
" , (2.67) 
where for any Q and µ, we denote by Qµ the function of x defined by 
Qµ(x) = Q ! x, µ(x) 
" , x ! X, (2.68) 
and for any two functions V1 and V2 of x, we denote by min{V1, V2} the function of x given by 
min{V1, V2}(x) = min % V1(x), V2(x) 
& , x ! X. 
 MFµ(V,Q) is a function with a component ! MFµ(V,Q) 
" (x) for each 
x, where M denotes minimization over u, so that 
! MFµ(V,Q) 
" (x) = min 
u!U(x) Fµ(V,Q)(x, u). (2.69)
104 Contractive Models Chap. 2 
Example 2.6.2 (Asynchronous Optimistic Policy Iteration for Discounted Finite-State MDP) 
Consider the special case of the finite-state discounted MDP of Example 1.2.2. We have 
H(x, u, J) = 
n$ 
y=1 
pxy(u) ! g(x, u, y) + !J(y) 
" , 
and 
Fµ(V,Q)(x, u) = H ! x, u,min{V,Qµ} 
" 
= 
n$ 
y=1 
pxy(u) 1 g(x, u, y) + !min 
% V (y), Q(y, µ(y)) 
&2 , 
! MFµ(V,Q) 
" (x) = min 
u$U(x) 
n$ 
y=1 
pxy(u) 1 g(x,u, y) + !min 
% V (y),Q(y, µ(y)) 
&2 , 
[cf. Eqs. (2.67)-(2.69)]. Note that Fµ(V,Q) is the mapping that defines Bell-man’s equation for the Q-factors of a policy µ in an optimal stopping problem where the stopping cost at state y is equal to V (y). 
We now consider the mapping Gµ given by 
Gµ(V,Q) = ! MFµ(V,Q), Fµ(V,Q) 
" , (2.70) 
and show that it has a uniform contraction property and a corresponding uniform fixed point. To this end, we introduce the norm 
))(V,Q) )) = max 
% *V *, *Q* 
& 
in the space of (V,Q), where *V * is the weighted sup-norm of V , and *Q* is defined by 
*Q* = sup x!X,u!U(x) 
##Q(x, u) ## 
v(x) . 
We have the following proposition. 
Proposition 2.6.4: Let the contraction Assumption 2.1.2 hold. Con-sider the mapping Gµ defined by Eqs. (2.67)-(2.70). Then for all µ: 
(a) (J*, Q*) is the unique fixed point of Gµ, where Q* is defined by 
Q*(x, u) = H(x, u, J*), x ! X, u ! U(x). (2.71) 
(b) The following uniform contraction property holds for all (V,Q) and (Ṽ , Q̃): 
))Gµ(V,Q)+Gµ(Ṽ , Q̃) )) ( ! 
))(V,Q)+ (Ṽ , Q̃) )).
Sec. 2.6 Asynchronous Algorithms 105 
Proof: (a) Using the definition (2.71) of Q*, we have 
J*(x) = (TJ*)(x) = inf u!U(x) 
H(x, u, J*) = inf u!U(x) 
Q*(x, u), ' x ! X, 
so that 
min % J*(x), Q* 
! x, µ(x) 
"& = J*(x), ' x ! X, µ ! M. 
Using the definition (2.67) of Fµ, it follows that Fµ(J*, Q*) = Q* and also that MFµ(J*, Q*) = J*, so (J*, Q*) is a fixed point of Gµ for all µ. The uniqueness of this fixed point will follow from the contraction property of part (b). 
(b) We first show that for all (V,Q) and (Ṽ , Q̃), we have 
))Fµ(V,Q)+ Fµ(Ṽ , Q̃) )) ( ! 
))min{V,Qµ}+min{Ṽ , Q̃µ} )) 
( !max % *V + Ṽ *, *Q+ Q̃* 
& . 
(2.72) 
Indeed, the first inequality follows from the definition (2.67) of Fµ and the contraction Assumption 2.1.2. The second inequality follows from a nonexpansiveness property of the minimization map: for any J1, J2, J̃1, J̃2, we have 
))min{J1, J2}+min{J̃1, J̃2} )) ( max 
% *J1 + J̃1*, *J2 + J̃2* 
& ; (2.73) 
[to see this, write for every x, 
Jm(x) 
v(x) ( max 
% *J1 + J̃1*, *J2 + J̃2* 
& + 
J̃m(x) 
v(x) , m = 1, 2, 
take the minimum of both sides over m, exchange the roles of Jm and J̃m, and take supremum over x]. Here we use the relation (2.73) for J1 = V , J̃1 = Ṽ , and J2(x) = Q 
! x, µ(x) 
" , J̃2(x) = Q̃ 
! x, µ(x) 
" , for all x ! X . 
We next note that for all Q, Q̃, † 
*MQ+MQ̃* ( *Q+ Q̃*, 
† For a proof, we write 
Q(x, u) 
v(x) % #Q! Q̃#+ 
Q̃(x, u) 
v(x) , ' u " U(x), x " X, 
take infimum of both sides over u " U(x), exchange the roles of Q and Q̃, and take supremum over x " X.
106 Contractive Models Chap. 2 
which together with Eq. (2.72) yields 
max %))MFµ(V,Q)+MFµ(Ṽ , Q̃) 
)), ))Fµ(V,Q)+ Fµ(Ṽ , Q̃) 
))& 
( !max % *V + Ṽ *, *Q+ Q̃* 
& , 
or equivalently ))Gµ(V,Q)+Gµ(Ṽ , Q̃) 
)) ( ! ))(V,Q)+ (Ṽ , Q̃) 
)). Q.E.D. 
Because of the uniform contraction property of Prop. 2.6.4(b), a distributed fixed point iteration, like the VI algorithm of Eq. (2.61), can be used in conjunction with the mapping (2.70) to generate asynchronously a sequence 
% (V t, Qt) 
& that is guaranteed to converge to (J*, Q*) for any 
sequence {µt}. This can be verified using the proof of Prop. 2.6.2 (more precisely, a proof that closely parallels the one of that proposition); the mapping (2.70) plays the role of T in Eq. (2.61). † 
Asynchronous PI Algorithm 
We now describe a PI algorithm, which applies asynchronously the components MFµ(V,Q) and Fµ(V,Q) of the mapping Gµ(V,Q) of Eq. (2.70). The first component is used for local policy improvement and makes a local update to V and µ, while the second component is used for local policy evaluation and makes a local update to Q. The algorithm draws its validity from the weighted sup-norm contraction property of Prop. 2.6.4(b) and the asynchronous convergence theory (Prop. 2.6.2 and Exercise 2.2). 
The algorithm is a modification of the “natural” asynchronous PI algorithm (2.63)-(2.64) [without the “communication delays” t+ +!j(t)]. It generates sequences {V t, Qt, µt}, which will be shown to converge, in the sense that V t $ J*, Qt $ Q*. Note that this is not the only distributed iterative algorithm that can be constructed using the contraction property of Prop. 2.6.4, because this proposition allows a lot of freedom of choice for the policy µ. The paper by Bertsekas and Yu [BeY12] provides an extensive discussion of alternative possibilities, including stochastic simulation-based iterative algorithms, and algorithms that involve function approximation. 
To define the asynchronous computation framework, we consider again m processors, a partition ofX into setsX1, . . . , Xm, and assignment of each subset X! to a processor ) ! {1, . . . ,m}. For each ), there are two infinite disjoint subsets of times R!,R! " {0, 1, . . .}, corresponding to policy improvement and policy evaluation iterations, respectively. Each processor ) operates on V t(x), Qt(x, u), and µt(x), only for the states x within its “local” state space X!. Moreover, to execute the steps (a) and (b) of the algorithm, processor ) needs only the values Qt 
! x, µt(x) 
" of Qt [which are 
† Because Fµ and Gµ depend on µ, which changes as the algorithm pro-
gresses, it is necessary to use a minor extension of the asynchronous convergence theorem, given in Exercise 2.2, for the convergence proof.
Sec. 2.6 Asynchronous Algorithms 107 
equal to Qt µt(x); cf. Eq. (2.68)]. In particular, at each time t, each processor 
) does one of the following: 
(a) Local policy improvement : If t ! R!, processor ) sets for all x ! X!, † 
V t+1(x) = min u!U(x) 
H ! x, u,min{V t, Qt 
µt} " = 
! MFµt(V t, Qt) 
" (x), 
sets µt+1(x) to a u that attains the minimum, and leaves Q unchanged, i.e., Qt+1(x, u) = Qt(x, u) for all x ! X! and u ! U(x). 
(b) Local policy evaluation: If t ! R!, processor ) sets for all x ! X! and u ! U(x), 
Qt+1(x, u) = H ! x, u,min{V t, Qt 
µt} " = Fµt(V t, Qt)(x, u), 
and leaves V and µ unchanged, i.e., V t+1(x) = V t(x) and µt+1(x) = µt(x) for all x ! X!. 
(c) No local change: If t /! R! 2 R!, processor ) leaves Q, V , and µ unchanged, i.e., Qt+1(x, u) = Qt(x, u) for all x ! X! and u ! U(x), V t+1(x) = V t(x), and µt+1(x) = µt(x) for all x ! X!. 
Note that while this algorithm does not involve the “communication delays” t+ +!j(t), it can clearly be extended to include them. The reason is that our asynchronous convergence analysis framework in combination with the uniform weighted sup-norm contraction property of Prop. 2.6.4 can tolerate the presence of such delays. 
Reduced Space Implementation 
The preceding PI algorithm may be used for the calculation of both J* and Q*. However, if the objective is just to calculate J*, a simpler and more e"cient algorithm is possible. To this end, we observe that the preceding algorithm can be operated so that it does not require the maintenance of the entire function Q. The reason is that the values Qt(x, u) with u .= µt(x) do not appear in the calculations, and hence we need only the values Qt 
µt(x) = Q ! x, µt(x) 
" , which we store in a function J t: 
J t(x) = Q ! x, µt(x) 
" . 
This observation is the basis for the following algorithm. At each time t and for each processor ): 
(a) Local policy improvement : If t ! R!, processor ) sets for all x ! X!, 
J t+1(x) = V t+1(x) = min u!U(x) 
H ! x, u,min{V t, J t} 
" , (2.74) 
† As earlier we assume that the infimum over u " U(x) in the policy improvement operation is attained, and we write min in place of inf.
108 Contractive Models Chap. 2 
and sets µt+1(x) to a u that attains the minimum. 
(b) Local policy evaluation: If t ! R!, processor ) sets for all x ! X!, 
J t+1(x) = H ! x, µt(x),min{V t, J t} 
" , (2.75) 
and leaves V and µ unchanged, i.e., for all x ! X!, 
V t+1(x) = V t(x), µt+1(x) = µt(x). 
(c) No local change: If t /! R! 2 R!, processor ) leaves J , V , and µ unchanged, i.e., for all x ! X!, 
J t+1(x) = J t(x), V t+1(x) = V t(x), µt+1(x) = µt(x). 
Example 2.6.3 (Asynchronous Optimistic Policy Iteration for Discounted Finite-State MDP - Continued) 
As an illustration of the preceding reduced space implementation, consider the special case of the finite-state discounted MDP of Example 2.6.2. Here 
H(x, u, J) = 
n$ 
y=1 
pxy(u) ! g(x, u, y) + !J(y) 
" , 
and the mapping Fµ(V,Q) given by 
Fµ(V,Q)(x, u) = 
n$ 
y=1 
pxy(u) 1 g(x, u, y) + !min 
% V (y), Q(y, µ(y)) 
&2 , 
defines the Q-factors of µ in a corresponding stopping problem. In the PI algorithm (2.74)-(2.75), policy evaluation of µ aims to solve this stopping problem, rather than solve a linear system of equations, as in classical PI. In particular, the policy evaluation iteration (2.75) is 
Jt+1(x) = 
n$ 
y=1 
pxy ! µt(x) 
"1 g ! x, µt(x), y 
" + !min 
% V t(y), Jt(y) 
&2 , 
for all x " X". The policy improvement iteration (2.74) is a VI for the stopping problem: 
Jt+1(x) = V t+1(x) = min u$U(x) 
n$ 
y=1 
pxy(u) 1 g(x, u, y) + !min 
% V t(y), Jt(y) 
&2 , 
for all x " X", while the current policy is locally updated by 
µt+1(x) " arg min u$U(x) 
n$ 
y=1 
pxy(u) 1 g(x,u, y) + !min 
% V t(y), Jt(y) 
&2 , 
for all x " X". The “stopping cost” V t(y) is the most recent cost value, obtained by local policy improvement at y.
Sec. 2.6 Asynchronous Algorithms 109 
Example 2.6.4 (Asynchronous Optimistic Policy Iteration for Minimax Problems and Dynamic Games) 
Consider the optimistic PI algorithm (2.74)-(2.75) for the case of the minimax problem of Example 1.2.5 of Chapter 1, where 
H(x, u, J) = sup w$W (x,u) 
* g(x, u, w) + !J 
! f(x, u,w) 
"+ . 
Then the local policy evaluation step [cf. Eq. (2.75)] is written as 
Jt+1(x) = sup w$W (x,µt(x)) 
* g ! x, µt(x), w 
" 
+ !min % V t 
! f(x, µt(x), w) 
" , Jt 
! f(x, µt(x), w) 
"&"+ . 
The local policy improvement step [cf. Eq. (2.74)] takes the form 
Jt+1(x) = V t+1(x) = min u$U(x) 
sup w$W (x,u) 
* g(x, u,w) 
+ !min % V t 
! f(x, u,w) 
" , Jt 
! f(x, u, w) 
"&+ , 
and sets µt+1(x) to a u that attains the minimum. Similarly for the discounted dynamic game problem of Example 1.2.4 of 
Chapter 1, a local policy evaluation step [cf. Eq. (2.75)] consists of a local VI for the maximizer’s DP problem assuming a fixed policy for the minimizer, and a stopping cost V t as per Eq. (2.75). A local policy improvement step [cf. Eq. (2.74)] at state x consists of the solution of a static game with a payo# matrix that also involves min{V t, Jt} in place of Jt, as per Eq. (2.74). 
A Variant with Interpolation 
While the use of min{V t, J t} (rather than J t) in Eq. (2.75) provides a convergence enforcement mechanism for the algorithm, it may also become a source of ine"ciency, particularly when V t(x) approaches its limit J*(x) from lower values for many x. Then J t+1(x) is set to a lower value than the iterate 
Ĵ t+1(x) = H ! x, µt(x), J t 
" , (2.76) 
given by the “standard” policy evaluation iteration, and in some cases this may slow down the algorithm. 
A possible way to address this is to use an algorithmic variation that modifies appropriately Eq. (2.75), using interpolation with a parameter %t ! (0, 1], with %t $ 0. In particular, for t ! R! and x ! X!, we calculate the values J t+1(x) and Ĵ t+1(x) given by Eqs. (2.75) and (2.76), and if 
J t+1(x) < Ĵ t+1(x), (2.77)
110 Contractive Models Chap. 2 
we reset J t+1(x) to 
(1   t)J t+1(x) +  tĴ t+1(x). (2.78) 
The idea of the algorithm is to aim for a larger value of J t+1(x) when the condition (2.77) holds. Asymptotically, as  t ! 0, the iteration (2.77)-(2.78) becomes identical to the convergent update (2.75). For a detailed analysis we refer to the paper by Bertsekas and Yu [BeY10]. 
2.7 NOTES, SOURCES, AND EXERCISES 
Section 2.1: The contractive DP model of this section was first studied systematically by Denardo [Den67], who assumed an unweighted sup-norm, proved the basic results of Section 2.1, and described some of their applications. In this section, we have extended the analysis of [Den67] to the case of weighted sup-norm contractions. 
Section 2.2: The abstraction of the computational methodology for finitestate discounted MDP within the broader framework of weighted sup-norm contractions and an infinite state space (Sections 2.2-2.6) follows the author’s survey [Ber12b], and relies on several earlier analyses that use more specialized assumptions. 
Section 2.3: The multistep error bound of Prop. 2.2.2 is based on Scher-rer [Sch12], which explores periodic policies in approximate VI and PI in finite-state discounted MDP (see also Scherrer and Lesner [ShL12], who give an example showing that the bound for approximate VI of Prop. 2.3.2 is essentially sharp for discounted finite-state MDP). For a related discussion of approximate VI, including the error amplification phenomenon of Example 2.3.1, and associated error bounds, see de Farias and Van Roy [DFV00]. 
Section 2.4: The error bound of Prop. 2.4.3 extends a standard bound for finite-state discounted MDP, derived by Bertsekas and Tsitsiklis [BeT96] (Section 6.2.2), and shown to be tight by an example. 
Section 2.5: Optimistic PI has received a lot of attention in the literature, particularly for finite-state discounted MDP, and it is generally thought to be computationally more e cient in practice than ordinary PI (see e.g., Puterman [Put94], who refers to the method as “modified PI”). The convergence analysis of the synchronous optimistic PI (Section 2.5.1) follows Rothblum [Rot79], who considered the case of an unweighted sup-norm (v = e); see also Canbolat and Rothblum [CaR13]. The error bound for optimistic PI (Section 2.5.2) is due to Thierry and Scherrer [ThS10b], which was given for the case of a finite-state discounted MDP. We follow closely their line of proof. Related error bounds and analysis are given by Scherrer [Sch11].
Sec. 2.7 Notes, Sources, and Exercises 111 
The  -PI method [cf. Eq. (2.34)] was introduced by Bertsekas and Io↵e [BeI96], and was also presented in the book [BeT96], Section 2.3.1. It is the basis of the LSPE( ) policy evaluation method, described by Nedić and Bertsekas [NeB03], and by Bertsekas, Borkar, and Nedić [BBN04]. It was studied further in approximate DP contexts by Thierry and Scherrer [ThS10a], Bertsekas [Ber11b], and Scherrer [Sch11]. An extension of  -PI, called ⇤-PI, uses a di↵erent parameter  i for each state i, and is discussed in Section 5 of the paper by Yu and Bertsekas [YuB12]. Based on the discussion of Section 1.2.5 and Exercise 1.2, ⇤-PI may be viewed as a diagonally scaled version of the proximal algorithm, i.e., one that uses a di↵erent penalty parameter for each proximal term. 
When the state and control spaces are finite, and cost approximation over a subspace { r | r 2 <s} is used (cf. Section 1.2.4), a prominent approximate PI approach is to replace the exact policy evaluation equation 
Jµk = TµkJµk 
with an approximate version of the form 
 rk = WTµk( rk), (2.79) 
where W is some n⇥ n matrix whose range space is the subspace spanned by the columns of  , where n is the number of states. For example the projected and aggregation equations, described in Section 1.2.4, have this form. The next policy µk+1 is obtained using the policy improvement equation 
Tµk+1( rk) = T ( rk). (2.80) 
A critical issue for the validity of such a method is whether the approximate Bellman equations 
 r = WT ( r) 
and  r = WTµ( r), µ 2 M, 
have a unique solution. This is true if the composite mappings W   T and W   Tµ are contractions over <n. In particular, in the case of an aggregation equation, where W =  D, the rows of   and D are probability distributions, and Tµ, µ 2 M, are monotone sup-norm contractions, the mappings W   T and W   Tµ are also monotone sup-norm contractions. However, in other cases, including when policy evaluation is done using the projected equation, W   T need not be monotone or be a contraction of any kind, and the approximate PI algorithm (2.79)-(2.80) may lead to systematic oscillations, involving cycles of policies (see related discussions in [BeT96], [Ber11c], and [Ber12a]). This phenomenon has been known
112 Contractive Models Chap. 2 
since the early days of approximate DP ([Ber96] and the book [BeT96]), but its practical implications have not been fully assessed. Generally, the line of analysis of Section 2.5.3, which does not require monotonicity or supnorm contraction properties of the composite mappings W  T and W  Tµ, can be applied to the approximate PI algorithm (2.79)-(2.80), but only in the case where these mappings are contractions over <n with respect to a common norm k · k; see Exercise 2.6 for further discussion. 
Section 2.6: Asynchronous VI (Section 2.6.1) for finite-state discounted MDP and games, shortest path problems, and abstract DP models, was proposed in the author’s paper on distributed DP [Ber82]. The asynchronous convergence theorem (Prop. 2.6.1) was first given in the author’s paper [Ber83], where it was applied to a variety of algorithms, including VI for discounted and undiscounted DP, and gradient methods for unconstrained optimization (see also Bertsekas and Tsitsiklis [BeT89], where a textbook account is presented). The key convergence mechanism, which underlies the proof of Prop. 2.6.1, is that while the algorithm iterates asynchronously on the components J` of J , an iteration with any one component does not impede the progress made by iterations with the other components, thanks to the box condition. At the same time, progress towards the solution is continuing thanks to the synchronous convergence condition. 
Earlier references on distributed asynchronous iterative algorithms include the work of Chazan and Miranker [ChM69] on Gauss-Seidel methods for solving linear systems of equations (who attributed the original algorithmic idea to Rosenfeld [Ros67]), and also Baudet [Bau78] on sup-norm contractive iterations. We refer to [BeT89] for detailed references. 
Asynchronous algorithms have also been studied and applied to simu-lation-based DP, particularly in the context of Q-learning, first proposed by Watkins [Wat89], which may be viewed as a stochastic version of VI, and is a central algorithmic concept in approximate DP and reinforcement learning. Two principal approaches for the convergence analysis of asynchronous stochastic algorithms have been suggested. 
The first approach, initiated in the paper by Tsitsiklis [Tsi94], considers the totally asynchronous computation of fixed points of abstract sup-norm contractive mappings and monotone mappings, which are defined in terms of an expected value. The algorithm of [Tsi94] contains as special cases Q-learning algorithms for finite-spaces discounted MDP and SSP problems. The analysis of [Tsi94] shares some ideas with the theory of Section 2.6.1, and also relies on the theory of stochastic approximation methods. For a subsequent analysis of the convergence of Q-learning for SSP, which addresses the issue of boundedness of the iterates, we refer to Yu and Bertsekas [YuB13b]. 
The second approach, treats asynchronous algorithms of the stochastic approximation type under some restrictions on the size of the communi-
Sec. 2.7 Notes, Sources, and Exercises 113 
cation delays or on the time between consecutive updates of a typical component. This approach was initiated in the paper by Tsitsiklis, Bertsekas, and Athans [TBA86], and was also developed in the book by Bertsekas and Tsitsiklis [BeT89] for stochastic gradient optimization methods. A related analysis that uses the ODE approach for more general fixed point problems was given in the paper by Borkar [Bor98], and was refined in the papers by Abounadi, Bertsekas, and Borkar [ABB02], and Borkar and Meyn [BoM00], which also considered applications to Q-learning. We refer to the monograph by Borkar [Bor08] for a more comprehensive discussion. 
The convergence of asynchronous PI for finite-state discounted MDP under the condition 
J0   Tµ0J0 
was shown by Williams and Baird [WiB93], who also gave examples showing that without this condition, cycling of the algorithm may occur. The asynchronous PI algorithm with a uniform fixed point (Section 2.6.3) was introduced in the papers by Bertsekas and Yu [BeY10], [BeY12], [YuB13a], in order to address this di culty. Our analysis follows the analysis of these papers. 
In addition to resolving the asynchronous convergence issue, the asynchronous PI algorithm of Section 2.6.3, obviates the need for minimization over all controls at every iteration (this is the generic computational efficiency advantage that optimistic PI typically holds over VI). Moreover, the algorithm admits a number of variations thanks to the fact that Prop. 2.6.4 asserts the contraction property of the mapping Gµ for all µ. This can be used to prove convergence in variants of the algorithm where the policy µt is updated more or less arbitrarily, with the aim to promote some objective. We refer to the paper [BeY12], which also derives related asynchronous simulation-based Q-learning algorithms with and without cost function approximation, where µt is replaced by a randomized policy to enhance exploration. 
The randomized asynchronous optimistic PI algorithm of Section 2.6.2, introduced in the first edition of this book, also resolves the asynchronous convergence issue. The fact that this algorithm does not require the monotonicity assumption may be useful in nonDP algorithmic contexts (see [Ber16b] and Exercise 2.6). 
In addition to discounted stochastic optimal control, the results of this chapter find application in the context of the stochastic shortest path problem of Example 1.2.6, when all policies are proper. Then, under some additional assumptions, it can be shown that T and Tµ are weighted sup-norm contractions with respect to a special norm. It follows that the analysis and algorithms of this chapter apply in this case. For a detailed discussion, we refer to the monograph [BeT96] and the survey [Ber12b]. For extensions to the case of countable state space, see the textbook [Ber12a], Section 3.6, and Hinderer and Waldmann [HiW05].
114 Contractive Models Chap. 2 
E X E R C I S E S 
2.1 (Periodic Policies) 
Consider the multistep mappings T ⌫ = Tµ0 · · ·Tµm 1 , ⌫ 2 Mm, defined in Exer-cise 1.1 of Chapter 1, where Mm is the set of m-tuples ⌫ = (µ0, . . . , µm 1), with µk 2 M, k = 1, . . . ,m 1, and m is a positive integer. Assume that the mappings Tµ satisfy the monotonicity and contraction Assumptions 2.1.1 and 2.1.2, so that the same is true for the mappings T ⌫ (with the contraction modulus of T ⌫ being ↵ m, cf. Exercise 1.1). 
(a) Show that the unique fixed point of T ⌫ is J⇡, where ⇡ is the nonstationary but periodic policy ⇡ = {µ0, . . . , µm 1, µ0, . . . , µm 1, . . .}. 
(b) Show that the multistep mappings Tµ0 · · ·Tµm 1 , Tµ1 · · ·Tµm 1Tµ0 , . . . , Tµm 1Tµ0 · · ·Tµm 2 , have unique corresponding fixed points J0, J1, . . ., Jm 1, which satisfy 
J0 = Tµ0J1, J1 = Tµ1J2, . . . , Jµm 2 = Tµm 2Jµm 1 , Jµm 1 = Tµm 1J0. 
Hint : Apply Tµ0 to the fixed point relation 
J1 = Tµ1 · · ·Tµm 1Tµ0J1 
to show that Tµ0J1 is the fixed point of Tµ0 · · ·Tµm 1 , i.e., is equal to J0. Similarly, apply Tµ1 to the fixed point relation 
J2 = Tµ2 · · ·Tµm 1Tµ0Tµ1J2, 
to show that Tµ1J2 is the fixed point of Tµ1 · · ·Tµm 1Tµ0 , etc. 
Solution: (a) Let us define 
J0 = lim k!1 
T k ⌫J 
0 , J1 = lim 
k!1 T 
k ⌫(Tµ0J 
0), . . . , Jm 1 = lim k!1 
T k ⌫(Tµ0 · · ·Tµm 2J 
0), 
where J 0 is some function in B(X). Since T ⌫ is a contraction mapping, J0, . . . , Jm 1 
are all equal to the unique fixed point of T ⌫ . Since J0, . . . , Jm 1 are all equal, they are also equal to J⇡ (by the definition of J⇡). Thus J⇡ is the unique fixed point of T ⌫ . 
(b) Follow the hint.
Sec. 2.7 Notes, Sources, and Exercises 115 
2.2 (Asynchronous Convergence Theorem for Time-Varying Maps) 
In reference to the framework of Section 2.6.1, let {Tt} be a sequence of mappings from R(X) to R(X) that have a common unique fixed point J⇤, let Assumption 2.6.1 hold, and assume that there is a sequence of nonempty subsets 
  S(k) 
 ⇢ 
R(X) with S(k + 1) ⇢ S(k) for all k, and with the following properties: 
(1) Synchronous Convergence Condition: Every sequence {Jk} with J k 2 S(k) 
for each k, converges pointwise to J ⇤. Moreover, we have 
TtJ 2 S(k + 1), 8 J 2 S(k), k, t = 0, 1, . . . . 
(2) Box Condition: For all k, S(k) is a Cartesian product of the form 
S(k) = S1(k)⇥ · · ·⇥ Sm(k), 
where S`(k) is a set of real-valued functions on X`, ` = 1, . . . ,m. 
Then for every J 0 2 S(0), the sequence {J t} generated by the asynchronous 
algorithm 
J t+1 ` (x) = 
⇢ Tt(J 
⌧`1(t) 1 , . . . , J 
⌧`m(t) m )(x) if t 2 R`, x 2 X`, 
J t ` (x) if t /2 R`, x 2 X`, 
[cf. Eq. (2.61)] converges pointwise to J ⇤. 
Solution: A straightforward adaptation of the proof of Prop. 2.6.1. 
2.3 (Nonmonotonic Contractive Models – Fixed Points of Concave Sup-Norm Contractions [Ber16b]) 
The purpose of this exercise is to make a connection between our abstract DP model and the problem of finding the fixed point of a (not necessarily monotone) mapping that is a sup-norm contraction and has concave components. Let T : <n 7! <n be a real-valued function whose n scalar components are concave. Then the components of T can be represented as 
(TJ)(x) = inf u2U(x) 
  F (x, u)  J 
0 u 
 , x = 1, . . . , n, (2.81) 
where u 2 <n, J 0 u denotes the inner product of J and u, F (x, ·) is the conju-
gate convex function of the convex function  (TJ)(x), and U(x) =   u 2 <n | 
F (x, u) < 1  is the e↵ective domain of F (x, ·) (for the definition of these terms, 
we refer to books on convex analysis, such as [Roc70] and [Ber09]). Assuming that the infimum in Eq. (2.81) is attained for all x, show how the VI algorithm of Section 2.6.1 and the PI algorithm of Section 2.6.3 can be used to find the fixed point of T in the case where T is a sup-norm contraction, but not necessarily
116 Contractive Models Chap. 2 
monotone. Note: For algorithms that relate to the context of this exercise and are inspired by approximate PI, see [Ber16b], [Ber18c]. 
Solution: The analysis of Sections 2.6.1 and 2.6.3 does not require monotonicity of the mapping Tµ given by 
(TµJ)(x) = F 
  x, µ(x) 
    J 
0 µ(x). 
2.4 (Discounted Problems with Unbounded Cost per Stage) 
Consider a countable-state MDP, where X = {1, 2, . . .}, the discount factor is ↵ 2 (0, 1), the transition probabilities are denoted pxy(u) for x, y 2 X and u 2 U(x), and the expected cost per stage is denoted by g(x, u), x 2 X, u 2 U(x). The constraint set U(x) may be infinite. For a positive weight sequence v =  v(1), v(2), . . . 
 , we consider the space B(X) of sequences J = 
  J(1), J(2), . . . 
 
such that kJk < 1, where k · k is the corresponding weighted sup-norm. We assume the following. 
(1) The sequence G = {G1, G2, . . .}, where 
Gx = sup u2U(x) 
  g(x, u)   , x 2 X, 
belongs to B(X). 
(2) The sequence V = {V1, V2, . . .}, where 
Vx = sup u2U(x) 
X 
y2X 
pxy(u) v(y), x 2 X, 
belongs to B(X). 
(3) We have P y2X 
pxy(u)v(y) 
v(x)  1, 8 x 2 X. 
Consider the monotone mappings Tµ and T , given by 
(TµJ)(x) = g 
  x, µ(x) 
  + ↵ 
X 
y2X 
pxy 
  µ(x) 
  J(y), x 2 X, 
(TJ)(x) = inf u2U(x) 
" g(x, u) + ↵ 
X 
y2X 
pxy(u)J(y) 
# , x 2 X. 
Show that Tµ and T map B(X) into B(X), and are contraction mappings with modulus ↵.
Sec. 2.7 Notes, Sources, and Exercises 117 
Solution: We have 
  (TµJ)(x)    
v(x)  Gx 
v(x) + ↵ 
X 
y2X 
pxy 
  µ(x) 
  v(y) 
v(x) 
  J(y)    
v(y) , 8 x 2 X, µ 2 M, 
from which, using assumptions (1) and (2), 
  (TµJ)(x)    
v(x)  kGk+ kV k kJk, 8 x 2 X, µ 2 M. 
A similar argument shows that 
  (TJ)(x)    
v(x)  kGk+ kV k kJk, 8 x 2 X. 
It follows that TµJ 2 B(X) and TJ 2 B(X) if J 2 B(X). For any J, J 
0 2 B(X) and µ 2 M, we have 
kTµJ   TµJ 0k = sup 
x2X 
   ↵ P 
y2X pxy 
  µ(x) 
   J(x)  J 
0(x)      
v(x) 
 sup x2X 
   ↵ P 
y2X pxy 
  µ(x) 
  v(y) 
  |J(y)  J 
0(y)|/v(y)      
v(x) 
 sup x2X 
↵ 
    P 
y2X pxy 
  µ(x) 
  v(y) 
    v(x) 
kJ   J 0k 
 ↵kJ   J 0k, 
where the last inequality follows from assumption (3). Hence Tµ is a contraction of modulus ↵. 
To show that T is a contraction, we note that 
(TµJ)(x) 
v(x)  (TµJ 
0)(x) 
v(x) + ↵kJ   J 
0k, x 2 X, µ 2 M, 
so by taking infimum over µ 2 M, we obtain 
(TJ)(x) 
v(x)  (TJ 0)(x) 
v(x) + ↵kJ   J 
0k, x 2 X. 
Similarly, (TJ 0)(x) 
v(x)  (TJ)(x) 
v(x) + ↵kJ   J 
0k, x 2 X, 
and by combining the last two relations the contraction property of T follows.
118 Contractive Models Chap. 2 
2.5 (Solution by Mathematical Programming) 
Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold. Show that if J  TJ and J 2 B(X), then J  J 
⇤. Use this fact to show that if X = {1, . . . , n} and U(i) is finite for each i = 1, . . . , n, then J 
⇤(1), . . . , J⇤(n) solves the following problem (in z1, . . . , zn): 
maximize 
nX 
i=1 
zi 
subject to zi  H(i, u, z), i = 1, . . . , n, u 2 U(i), 
where z = (z1, . . . , zn). Note: This is a linear or nonlinear program (depending on whether H is linear in J or not) with n variables and as many as n ⇥ m 
constraints, where m is the maximum number of elements in the sets U(i). 
Solution: If J  TJ , by monotonicity we have J  limk!1 T k J = J 
⇤. Any feasible solution z of the given optimization problem satisfies zi  H(i, u, z) for all i = 1, . . . , n and u 2 U(i), so that z  Tz. It follows that z  J 
⇤, which implies that J⇤ solves the optimization problem. 
2.6 (Conditions for Convergence of PI with Cost Function Approximation [Ber11c]) 
Let the monotonicity and contraction Assumptions 2.1.1 and 2.1.2 hold, and assume that there are n states, and that U(x) is finite for every x. Consider a PI method that aims to approximate a fixed point of T on a subspace S = { r | r 2 <s}, where   is an n ⇥ s matrix, and evaluates a policy µ 2 M with a solution J̃µ of the following fixed point equation in the vector J 2 <n: 
J = WTµJ (2.82) 
where W : <n 7! <n is some mapping (possibly nonlinear, but independent of µ), whose range is contained in S. Examples where W is linear include policy evalution using the projected and aggregation equations; see Section 1.2.4. The algorithm is given by 
 rk = WTµk ( rk), Tµk+1( rk) = T ( rk); (2.83) 
[cf. Eqs. (2.79)-(2.80)]. We assume the following: 
(1) For each J 2 <n, there exists µ 2 M such that TµJ = TJ . 
(2) For each µ 2 M, Eq. (2.82) has a unique solution that belongs to S and is denoted J̃µ. Moreover, for all J such that WTµJ  J , we have 
J̃µ = lim k!1 
(WTµ) k J. 
(3) For each µ 2 M, the mappings W and WTµ are monotone in the sense that 
WJ  WJ 0 , WTµJ  WTµJ 
0 , 8 J, J 
0 2 <n with J  J 0 . (2.84)
Sec. 2.7 Notes, Sources, and Exercises 119 
Note that conditions (1) and (2) guarantee that the iterations (2.83) are welldefined. Assume that the method is initiated with some policy in M, and it is operated so that it terminates when a policy µ is obtained such that TµJ̃µ = T J̃µ. Show that the method terminates in a finite number of iterations, and the vector J̃µ obtained upon termination is a fixed point of WT . Note: Condition (2) is satisfied if WTµ is a contraction, while condition (b) is satisfied if W is a matrix with nonnegative components and Tµ is monotone for all µ. For counterexamples to convergence when the conditions (2) and/or (3) are not satisfied, see [BeT96], Section 6.4.2, and [Ber12a], Section 2.4.3. 
Solution: Similar to the standard proof of convergence of (exact) PI, we use the policy improvement equation TµJ̃µ = T J̃µ, the monotonicity of W , and the policy evaluation equation to write 
WTµJ̃µ = WTJ̃µ  WTµJ̃µ = J̃µ. 
By iterating with the monotone mapping WTµ and by using condition (2), we obtain 
J̃µ = lim k!1 
(WTµ) k J̃µ  J̃µ. 
There are finitely many policies, so we must have J̃µ = J̃µ after a finite number of iterations, which using the policy improvement equation TµJ̃µ = T J̃µ, implies that TµJ̃µ = T J̃µ. Thus the algorithm terminates with µ, and since J̃µ = WTµJ̃µ, it follows that J̃µ is a fixed point of WT .
3 Semicontractive Models 
Contents 
3.1. Pathologies of Noncontractive DP Models . . . . . . p. 123 3.1.1. Deterministic Shortest Path Problems . . . . . p. 127 3.1.2. Stochastic Shortest Path Problems . . . . . . . p. 129 3.1.3. The Blackmailer’s Dilemma . . . . . . . . . . p. 131 3.1.4. Linear-Quadratic Problems . . . . . . . . . . p. 134 3.1.5. An Intuitive View of Semicontractive Analysis . . p. 139 
3.2. Semicontractive Models and Regular Policies . . . . . p. 141 3.2.1. S-Regular Policies . . . . . . . . . . . . . . p. 144 3.2.2. Restricted Optimization over S-Regular Policies . p. 146 3.2.3. Policy Iteration Analysis of Bellman’s Equation . p. 152 3.2.4. Optimistic Policy Iteration and !-Policy Iteration p. 160 3.2.5. A Mathematical Programming Approach . . . . p. 164 
3.3. Irregular Policies/Infinite Cost Case . . . . . . . . p. 165 3.4. Irregular Policies/Finite Cost Case - A Perturbation . . . . 
Approach . . . . . . . . . . . . . . . . . . . . p. 171 3.5. Applications in Shortest Path and Other Contexts . . p. 177 
3.5.1. Stochastic Shortest Path Problems . . . . . . . p. 178 3.5.2. A!ne Monotonic Problems . . . . . . . . . . p. 186 3.5.3. Robust Shortest Path Planning . . . . . . . . p. 195 3.5.4. Linear-Quadratic Optimal Control . . . . . . . p. 205 3.5.5. Continuous-State Deterministic Optimal Control . p. 207 
3.6. Algorithms . . . . . . . . . . . . . . . . . . . . p. 211 3.6.1. Asynchronous Value Iteration . . . . . . . . . p. 211 3.6.2. Asynchronous Policy Iteration . . . . . . . . . p. 212 
3.7. Notes, Sources, and Exercises . . . . . . . . . . . . p. 219 
121
122 Semicontractive Models Chap. 3 
We will now consider abstract DP models that are intermediate between the contractive models of Chapter 2, where all stationary policies involve a contraction mapping, and noncontractive models to be discussed in Chapter 4, where there are no contraction-like assumptions (although there are some compensating conditions, including monotonicity). 
A representative instance of such an intermediate model is the deterministic shortest path problem of Example 1.2.7, where we can distinguish between two types of stationary policies: those that terminate at the destination from every starting node, and those that do not. A more general instance is the stochastic shortest path (SSP for short) problem of Example 1.2.6. In this problem, the analysis revolves around two types of stationary policies µ: those with a mapping Tµ that is a contraction with respect to some norm, and those with a mapping Tµ that is not a contraction with respect to any norm (it can be shown that the former are the ones that terminate with probability 1 starting from any state). 
In the models of this chapter, like in SSP problems, we divide policies into two groups, one of which has favorable characteristics. We loosely refer to such models as semicontractive to indicate that these favorable characteristics include contraction-like properties of the mapping Tµ. To develop a more broadly applicable theory, we replace the notion of contractiveness of Tµ with a notion of S-regularity of µ, where S is an appropriate set of functions of the state (roughly, this is a form of “local stability” of Tµ, which ensures that the cost function Jµ is the unique fixed point of Tµ 
within S, and that T k µJ converges to Jµ regardless of the choice of J from 
within S). We allow that some policies are S-regular while others are not. Note that the term “semicontractive” is not used in a precise mathe-
matical sense here. Rather it refers qualitatively to a collection of models where some policies have a regularity/contraction-like property but others do not. Moreover, regularity is a relative property: the division of policies into “regular” and “irregular” depends on the choice of the set S. On the other hand, typically in practical applications an appropriate choice of S is fairly evident. 
Our analysis will involve two types of assumptions: 
(a) Favorable assumptions, under which we obtain results that are nearly as strong as those available for the contractive models of Chapter 2. In particular, we show that J* is a fixed point of T , that the Bellman equation J = TJ has a unique solution, at least within a suitable class of functions, and that variants of the VI and PI algorithms are valid. Some of the VI and PI approaches are suitable for distributed asynchronous computation, similar to their Section 2.6 counterparts for contractive models. 
(a) Less favorable assumptions, under which serious di!culties may occur: J* may not be a fixed point of T , and even when it is, it may not be found using the VI and PI algorithms. These anomalies may ap-
Sec. 3.1 Pathologies of Noncontractive DP Models 123 
pear in simple problems, such as deterministic and stochastic shortest path problems with some zero length cycles. To address the di!culties, we will consider a restricted problem, where the only admissible policies are the ones that are S-regular . Under reasonable conditions we show that this problem is better-behaved. In particular, J* 
S , the optimal cost function over the S-regular policies only, is the unique solution of Bellman’s equation among functions J ! S with J " J* 
S , while VI converges to J* 
S starting from any J ! S with J " J* S . 
We will also derive a variety of PI approaches for finding J* S and an 
S-regular policy that is optimal within the class of S-regular policies. 
We will illustrate our analysis in Section 3.5, both under favorable and unfavorable assumptions, by means of four classes of practical problems. Some of these problems relate to finding a path to a destination in a graph under stochastic or set membership uncertainty, while others relate to the control of a continuous-state system to a terminal state. In particular, we will consider SSP problems, a!ne monotonic problems, including problems with multiplicative or risk-sensitive exponential cost function, minimaxtype shortest path problems, and continuous-state deterministic problems with nonnegative cost, such as linear-quadratic problems. 
The chapter is organized as follows. In Section 3.1, we illustrate the pathologies regarding solutions of Bellman’s equation, and the VI and PI algorithms. To this end, we use four simple examples, ranging from finitestate shortest path problems, to continuous-state linear-quadratic problems. These examples provide orientation and motivation for S-regular policies later. In Section 3.2, we formally introduce our abstract DP model, and the notion of an S-regular policy. We then develop some of the basic associated results relating to Bellman’s equation, and the convergence of VI and PI, based primarily on the ideas underlying the PI algorithm. In Section 3.3 we refine the results of Section 3.2 under favorable conditions, obtaining results and algorithms that are almost as powerful as the ones for contractive models. In Section 3.4 we develop a complementary analytical approach, which is based on the use of perturbations and applies under less favorable assumptions. In Section 3.5, we discuss in detail the application and refinement of the results of Sections 3.2-3.4 in some important shortest path-type practical contexts. In Section 3.6, we focus on variants of VI and PI-type algorithms for semicontractive DP models, including some that are suitable for asynchronous distributed computation. 
3.1 PATHOLOGIES OF NONCONTRACTIVE DP MODELS 
In this section we provide a general overview of the analytical and computational di!culties in noncontractive DP models, using for the most part shortest path-type problems. For illustration we will first use two of the simplest and most widely encountered finite-state DP problems: deter-
124 Semicontractive Models Chap. 3 
ministic and SSP problems, whereby we are aiming to reach a destination state at minimum cost. † We will also discuss an example of continuousstate shortest path problem that involves a linear system and a quadratic cost function. 
We will adopt the general abstract DP model of Section 1.2. We give a brief description that is adequate for the purposes of this section, and defer a more formal definition to Section 3.2. In particular, we introduce a set of states X , and for each x ! X , the nonempty control constraint set U(x). For each policy µ, the mapping Tµ is given by 
(TµJ)(x) = H ! x, µ(x), J 
" , # x ! X, 
where H is a suitable function of (x, u, J). The mapping T is given by 
(TJ)(x) = inf u!U(x) 
H(x, u, J), # x ! X. 
The cost function of a policy " = {µ0, µ1, . . .} is 
J!(x) = lim sup N"# 
J!,N(x) = lim sup N"# 
(Tµ0Tµ1 · · ·TµN!1 J̄)(x), x ! X, 
where J̄ is some function. ‡ We want to minimize J! over ", i.e., to find 
J*(x) = inf ! 
J!(x), x ! X, 
and a policy that attains the infimum. For orientation purposes, we recall from Chapter 1 (Examples 1.2.1 
and 1.2.2) that for a stochastic optimal control problem involving a finitestate Markov chain with state spaceX = {1, . . . , n}, transition probabilities pxy(u), and expected one-stage cost function g, the mapping H is given by 
H(x, u, J) = g(x, u) + n# 
y=1 
pxy(u)J(y), x ! X, 
and J̄(x) $ 0. The SSP problem arises when there is an additional termination state that is cost-free, and corresponding transition probabilities pxt(u), x ! X . 
† These problems are naturally undiscounted, and cannot be readily ad-
dressed by introducing a discount factor close to 1, because then the optimal policies may exhibit undesirable behavior. In particular, in the presence of dis-
counting, they may involve moving initially along a small-length cycle in order 
to postpone the use of an optimal but unavoidably costly path until later, when the discount factor will reduce substantially the cost of that path. 
‡ In the contractive models of Chapter 2, the choice of J̄ is immaterial, as we 
discussed in Section 2.1. Here, however, the choice of J̄ is important, and a!ects important characteristics of the model, as we will see later.
Sec. 3.1 Pathologies of Noncontractive DP Models 125 
A more general undiscounted stochastic optimal control problem involves a stationary discrete-time dynamic system where the state is an element of a space X , and the control is an element of a space U . The control uk is constrained to take values in a given set U(xk) % U , which depends on the current state xk [uk ! U(xk), for all xk ! X ]. For a policy " = {µ0, µ1, . . .}, the state evolves according to a system equation 
xk+1 = f ! xk, µk(xk), wk 
" , k = 0, 1, . . . , (3.1) 
where wk is a random disturbance that takes values from a space W . We assume that wk, k = 0, 1, . . ., are characterized by probability distributions P (· | xk, uk) that are identical for all k, where P (wk | xk, uk) is the probability of occurrence of wk, when the current state and control are xk and uk, respectively. Here, we allow infinite state and control spaces, as well as problems with discrete (finite or countable) state space (in which case the underlying system is a Markov chain). However, for technical reasons that relate to measure-theoretic issues, we assume that W is a countable set. † 
Given an initial state x0, we want to find a policy " = {µ0, µ1, . . .}, where µk : X &' U , µk(xk) ! U(xk), for all xk ! X , k = 0, 1, . . ., that minimizes 
J!(x0) = lim sup k"# 
E 
$ k# 
t=0 
g ! xt, µt(xt), wt 
" % , (3.2) 
subject to the system equation constraint (3.1), where g is the one-stage cost function. The corresponding mapping of the abstract DP problem is 
H(x, u, J) = E & g(x, u, w) + J 
! f(x, u, w) 
"' , 
and J̄(x) $ 0. Again here, (Tµ0 · · ·Tµk J̄)(x) is the expected cost of the 
first k + 1 periods using " starting from x, and with terminal cost 0. A discounted version of the problem is defined by the mapping 
H(x, u, J) = E & g(x, u, w) + #J 
! f(x, u, w) 
"' , 
where # ! (0, 1) is the discount factor. It corresponds to minimization of 
J!(x0) = lim sup k"# 
E 
$ k# 
t=0 
#tg ! xt, µt(xt), wt 
" % . 
If the cost per stage g is bounded, then a problem that fits the contractive framework of Chapter 2 is obtained, and can be analyzed using the methods of that chapter. However, there are interesting infinite-state discounted optimal control problems where g is not bounded. 
† Measure-theoretic issues are not addressed at all in this third edition of the 
book. The first edition addressed some of these issues within an abstract DP context in its Chapter 5 and Appendix C (this material is posted at the book’s 
web site); see also the monograph by Bertsekas and Shreve [BeS78], and the paper 
by Yu and Bertsekas [YuB15]. An orientation summary is given in Appendix A of the author’s textbook [Ber12a].
126 Semicontractive Models Chap. 3 
A Summary of Pathologies 
The four examples to be discussed in Sections 3.1.1-3.1.4 are special cases of deterministic and stochastic optimal control problems of the type just described. In each of these examples, we will introduce a subclass of “well-behaved” policies and a restricted optimization problem, which is to minimize the cost over the “well-behaved” subclass (in Section 3.2 the property of being “well-behaved” will be formalized through the notion of S-regularity). The optimal cost function over just the “well-behaved” policies is denoted Ĵ (we will also use the notation J* 
S later). Here is a summary of the examples and the pathologies that they reveal: 
(a) A finite-state, finite-control deterministic shortest path problem (Sec-tion 3.1.1). Here the mapping T can have infinitely many fixed points, including J* and Ĵ . There exist policies that attain the optimal costs J* and Ĵ . Depending on the starting point, the VI algorithm may converge to J* or to Ĵ or to a third fixed point of T (for cases where J* (= Ĵ , VI converges to Ĵ starting from any J " Ĵ). The PI algorithm can oscillate between two policies that attain J* and Ĵ , respectively. 
(b) A finite-state, finite-control stochastic shortest path problem (Section 3.1.2). The salient feature of this example is that J* is not a fixed point of the mapping T . By contrast Ĵ is a fixed point of T . The VI algorithm converges to Ĵ starting from any J " Ĵ , while it does not converge otherwise. 
(c) A finite-state, continuous-control stochastic shortest path problem (Sec-tion 3.1.3). We give three variants of this example. In the first variant (a classical problem known as the “blackmailer’s dilemma”), all the policies are “well-behaved,” so J* = Ĵ , and VI converges to J* starting from any real-valued initial condition, while PI also succeeds in finding J* as the limit of the generated sequence {Jµk}. However, PI cannot find an optimal policy, because there is no optimal stationary policy. In a second variant of this example, PI generates a sequence of “well-behaved” policies {µk} such that Jµk ) Ĵ , but {µk} converges to a policy that is either infeasible or is strictly suboptimal. In the third variant of this example, the problem data can strongly a"ect the multiplicity of the fixed points of T , and the behavior of the VI and PI algorithms. 
(d) A continuous-state, continuous-control deterministic linear-quadratic problem (Section 3.1.4). Here the mapping T has exactly two fixed points, J* and Ĵ , within the class of positive semidefinite quadratic functions. The VI algorithm converges to Ĵ starting from all positive initial conditions, and to J* starting from all other initial conditions. Moreover, starting with a “well-behaved” policy (one that is stable),
Sec. 3.1 Pathologies of Noncontractive DP Models 127 
the PI algorithm converges to Ĵ and to an optimal policy within the class of “well-behaved” (stable) policies. 
It can be seen that the examples exhibit wide-ranging pathological behavior. In Section 3.2, we will aim to construct a theoretical framework that explains this behavior. Moreover, in Section 3.3, we will derive conditions guaranteeing that much of this type of behavior does not occur. These conditions are natural and broadly applicable. They are used to exclude from optimality the policies that are not “well-behaved,” and to obtain results that are nearly as powerful as their counterparts for the contractive models of Chapter 2. 
3.1.1 Deterministic Shortest Path Problems 
Let us consider the classical deterministic shortest path problem, discussed in Example 1.2.7. Here, we have a graph of n nodes x = 1, . . . , n, plus a destination t, and an arc length axy for each directed arc (x, y). The objective is to find for each x a directed path that starts at x, ends at t, and has minimum length (the length of a path is defined as the sum of the lengths of its arcs). A standard assumption, which we will adopt here, is that every node x is connected to the destination, i.e., there exists a path from every x to t. 
To formulate this shortest path problem as a DP problem, we embed it within a “larger” problem, whereby we view all paths as admissible, including those that do not terminate at t. We also view t as a cost-free and absorbing node. Of course, we need to deal with the presence of policies that do not terminate, and the most common way to do this is to assume that all cycles have strictly positive length, in which case policies that do not terminate cannot be optimal. However, it is not uncommon to encounter shortest path problems with zero length cycles, and even negative length cycles. Thus we will not impose any assumption on the sign of the cycle lengths, particularly since we aim to use the shortest path problem to illustrate behavior that arises in a broader undiscounted/noncontractive DP setting. 
As noted in Section 1.2, we can formulate the problem in terms of an abstract DP model where the states are the nodes x = 1, . . . , n, and the controls available at x can be identified with the outgoing neighbors of x [the nodes u such that (x, u) is an arc]. The mapping H that defines the corresponding abstract DP problem is 
H(x, u, J) = 
( axu + J(u) if u (= t, axt if u = t, 
x = 1, . . . , n. 
A stationary policy µ defines the subgraph whose arcs are ! x, µ(x) 
" , 
x = 1, . . . , n. We say that µ is proper if this graph is acyclic, i.e., it consists of a tree of paths leading from each node to the destination. If µ is not
128 Semicontractive Models Chap. 3 
a 
t b a 1 2 1 2 t b 
t b Destination 
u Cost 1 Cost 1 
u Cos 1 Cost 1 
Figure 3.1.1. A deterministic shortest path problem with a single node 1 and a termination node t. At 1 there are two choices; a self-transition, which costs a, and a transition to t, which costs b. 
proper, it is called improper . Thus there exists a proper policy if and only if each node is connected to t with a path. Furthermore, an improper policy has cost greater than *+ starting from every initial state if and only if all the cycles of the corresponding subgraph have nonnegative cycle cost. 
Let us now get a sense of what may happen by considering the simple one-node example shown in Fig. 3.1.1. Here there is a single state 1 in addition to the termination state t. At state 1 there are two choices: a self-transition, which costs a, and a transition to t, which costs b. The mapping H , abbreviating J(1) with just the scalar J , is 
H(1, u, J) = 
( a+ J if u: self transition, b if u: transition to t, 
J ! ,. 
There are two policies here: the policy µ that transitions from 1 to t, which is proper, and the policy µ$ that self-transitions at state 1, which is improper. We have 
TµJ = b, Tµ"J = a+ J, J ! ,, 
and 
TJ = min{b, a+ J}, J ! ,. 
Note that for the proper policy µ, the mapping Tµ : , &' , is a contraction. For the improper policy µ$, the mapping Tµ" : , &' , is not a contraction, and it has a fixed point within , only if a = 0, in which case every J ! , is a fixed point. 
We now consider the optimal cost J*, the fixed points of T within ,, and the behavior of the VI and PI methods for di"erent combinations of values of a and b. 
(a) If a > 0, the optimal cost, J* = b, is the unique fixed point of T , and the proper policy is optimal.
Sec. 3.1 Pathologies of Noncontractive DP Models 129 
(b) If a = 0, the set of fixed points of T (within ,) is the interval (*+, b]. Here the improper policy is optimal if b " 0, and the proper policy is optimal if b - 0 (both policies are optimal if b = 0). 
(c) If a = 0 and b > 0, the proper policy is strictly suboptimal, yet its cost at state 1 (which is b) is a fixed point of T . The optimal cost, J* = 0, lies in the interior of the set of fixed points of T , which is (*+, b]. Thus the VI method that generates {T kJ} starting with J (= J* 
cannot find J*. In particular if J is a fixed point of T , VI stops at J , while if J is not a fixed point of T (i.e., J > b), VI terminates in two iterations at b (= J*. Moreover, the standard PI method is unreliable in the sense that starting with the suboptimal proper policy µ, it may stop with that policy because TµJµ = b = min{b, Jµ} = TJµ (the improper/optimal policy µ$ also satisfies Tµ"Jµ = TJµ, so a rule for breaking the tie in favor of µ is needed but such a rule may not be obvious in general). 
(d) If a = 0 and b < 0, the improper policy is strictly suboptimal, and we have J* = b. Here it can be seen that the VI sequence {T kJ} converges to J* for all J " b, but stops at J for all J < b, since the set of fixed points of T is (*+, b]. Moreover, starting with either the proper policy or the improper policy, the standard form of PI may oscillate, since TµJµ" = TJµ" and Tµ"Jµ = TJµ, as can be easily verified [the optimal policy µ also satisfies TµJµ = TJµ but it is not clear how to break the tie; compare also with case (c) above]. 
(e) If a < 0, the improper policy is optimal and we have J* = *+. There are no fixed points of T within ,, but J* is the unique fixed point of T within the set [*+,+]. The VI method will converge to J* starting from any J ! [*+,+]. The PI method will also converge to the optimal policy starting from either policy. 
3.1.2 Stochastic Shortest Path Problems 
We consider the SSP problem, which was described in Example 1.2.6 and will be revisited in Section 3.5.1. Here a policy is associated with a stationary Markov chain whose states are 1, . . . , n, plus the cost-free termination state t. The cost of a policy starting at a state x is the sum of the expected cost of its transitions up to reaching t. A policy is said to be proper , if in its Markov chain, every state is connected with t with a path of positive probability transitions, and otherwise it is called improper . Equivalently, a policy is proper if its Markov chain has t as its unique ergodic state, with all other states being transient. 
In deterministic shortest path problems, it turns out that Jµ is always a fixed point of Tµ, and J* is always a fixed point of T . This is a generic feature of deterministic problems, which was illustrated in Section 1.1 (see Exercise 3.1 for a rigorous proof). However, in SSP problems where the
130 Semicontractive Models Chap. 3 
) Cost 0 t b Destination 
u Cost 0 Cost 
1 Cost 1 
1 Cost 1 u Cost !1 Cost 1 
u Cost !1 Cost 1 Cost 0 Cost 2 CostCost 0 Cost 2 Cost !2 Cost 
1 2 t b 
Prob. 1/2Prob. 1/2 
(4) = 1 Jµ(2) = 1 (7) = 1 Jµ(5) = 1 
Jµ(1) = 0 
Figure 3.1.2. An example of an improper policy µ, where Jµ is not a fixed point of Tµ. All transitions under µ are shown with solid lines. These transitions are deterministic, except at state 1 where the next state is 2 or 5 with equal probability 1/2. There are additional high cost transitions from nodes 1, 4, and 7 to the destination (shown with broken lines), which create a suboptimal proper policy. We have J# = Jµ and J# is not a fixed point of T . 
cost per stage can take both positive and negative values this need not be so, as we will now show with an example due to [BeY16]. 
Let us consider the problem of Fig. 3.1.2. It involves an improper policy µ, whose transitions are shown with solid lines in the figure, and form the two zero length cycles shown. All the transitions under µ are deterministic, except at state 1 where the successor state is 2 or 5 with equal probability 1/2. The problem has been deliberately constructed so that corresponding costs at the nodes of the two cycles are negatives of each other. As a result, the expected cost at each time period starting from state 1 is 0, implying that the total cost over any number or even infinite number of periods is 0. 
Indeed, to verify that Jµ(1) = 0, let ck denote the cost incurred at 
time k, starting at state 1, and let sN (1) = )N%1 
k=0 ck denote the N -step accumulation of ck starting from state 1. We have 
sN (1) = 0 if N = 1 or N = 4 + 3t, t = 0, 1, . . ., 
sN (1) = 1 or sN (1) = *1 with probability 1/2 each 
if N = 2 + 3t or N = 3 + 3t, t = 0, 1, . . ..
Sec. 3.1 Pathologies of Noncontractive DP Models 131 
Thus E & sN (1) 
' = 0 for all N , and 
Jµ(1) = lim sup N"# 
E & sN (1) 
' = 0. 
On the other hand, using the definition of Jµ in terms of lim sup, we have 
Jµ(2) = Jµ(5) = 1, 
(the sequence of N -stage costs undergoes a cycle {1,*1, 0, 1,*1, 0, . . .} when starting from state 2, and undergoes a cycle {*1, 1, 0,*1, 1, 0, . . .} when starting from state 5). Thus the Bellman equation at state 1, 
Jµ(1) = 1 2 
! Jµ(2) + Jµ(5) 
" , 
is not satisfied, and Jµ is not a fixed point of Tµ. The mathematical reason why Bellman’s equation Jµ = TµJµ may 
not hold for stochastic problems is that lim sup may not commute with the expected value operation that is inherent in Tµ, and the proof argument given for deterministic problems in Section 1.1 breaks down. We can also modify this example so that there are multiple policies. To this end, we can add for i = 1, 4, 7, another control that leads from i to t with a cost c > 1 (cf. the broken line arcs in Fig. 3.1.2). Then we create a proper policy that is strictly suboptimal, while not a"ecting J*, which again is not a fixed point of T . 
Let us finally note an anomaly around randomized policies in noncontractive models. The improper policy shown in Fig. 3.1.2 may be viewed as a randomized policy for a deterministic shortest path problem: this is the problem for which at state 1 we must (deterministically) choose one of the two successor states 2 and 5. For this deterministic problem, J* takes the same values as before for all i (= 1, but it takes the value J*(1) = 1 rather than J*(1) = 0. Thus, remarkably, once we allow randomized policies into the problem, the optimal cost function ceases to be a solution of Bellman’s equation and simultaneously the optimal cost at state 1 is improved! 
In subsequent sections we will see that favorable results hold in SSP problems where the restricted optimal cost function over just the proper policies is equal to the overall optimal J*. This can be guaranteed by assumptions that essentially imply that improper polices cannot be optimal (see Sections 3.3 and 3.5.1). We will then see that not only is J* a fixed point of T , but it is also the unique fixed point (within the class of realvalued functions), and that the VI and PI algorithms yield J* and an optimal proper policy in the limit. 
3.1.3 The Blackmailer’s Dilemma 
This is a classical example involving a profit maximizing blackmailer. We formulate it as an SSP problem involving cost minimization, with a single state x = 1, in addition to the termination state t.
132 Semicontractive Models Chap. 3 
a 1 2 1 2 t b 
Prob. u2 
u Destination 
2 Prob. 1! u 2 
2 
2 Control u ! (0, 1] Cost 1] Cost !u 
Figure 3.1.3. Transition diagram for the first variant of the blackmailer problem. At state 1, the blackmailer may demand any amount u ! (0, 1]. The victim will comply with probability 1"u2 and will not comply with probability u2, in which case the process will terminate. 
In a first variant of the problem, at state 1, we can choose a control u ! (0, 1], while incurring a cost *u; we then move to state t with probability u2, and stay in state 1 with probability 1*u2; see Fig. 3.1.3. We may regard u as a demand made by the blackmailer, and state 1 as the situation where the victim complies. State t is arrived at when the victim (permanently) refuses to yield to the blackmailer’s demand. The problem then can be viewed as one where the blackmailer tries to maximize his expected total gain by balancing his desire for increased demands (large u) with keeping his victim compliant (small u). 
For notational simplicity, let us abbreviate J(1) and µ(1) with just the scalars J and µ, respectively. Then in terms of abstract DP we have 
X = {1}, U = (0, 1], J̄ = 0, H(1, u, J) = *u+ (1 * u2)J, 
and for every stationary policy µ, we have 
TµJ = *µ+ (1* µ2)J. (3.3) 
Clearly Tµ, viewed as a mapping from , to ,, is a contraction with modulus 1* µ2, and its unique fixed point within ,, Jµ, is the solution of 
Jµ = TµJµ = *µ+ (1* µ2)Jµ, 
which yields 
Jµ = * 1 
µ . 
Here all policies are proper in the sense that they lead asymptotically to t with probability 1, and the infimum of Jµ over µ is *+, implying also
Sec. 3.1 Pathologies of Noncontractive DP Models 133 
that J* = *+. However, there is no optimal stationary policy within the class of proper policies. † 
Another interesting fact about this problem is that Tµ is a contraction for all µ. However the theory of contractive models does not apply because there is no uniform modulus of contraction (# < 1) that applies simultaneously to all µ ! (0, 1] [cf. Eq. (3.3)]. As a result, the contraction Assumption 2.1.2 of Section 2.1 does not hold. 
Let us now consider Bellman’s equation. The mapping T is given by 
TJ = inf 0<u&1 
& * u+ (1 * u2)J 
' , 
and Bellman’s equation is written as 
J = J * sup 0<u&1 
{u+ u2J}. 
It can be verified that this equation has no real-valued solution. How-ever, J' = *+ is a solution within the set of extended real numbers [*+,+]. Moreover the VI method will converge to J* starting from any J ! [*+,+). The PI method, starting from any policy µ0, will produce the ever improving sequence of policies {µk} with µk+1 = µk/2 and Jµk ) J*, while µk will converge to 0, which is not a feasible policy. 
A Second Problem Variant 
Consider next a variant of the problem where at state 1, we terminate at no cost with probability u, and stay in state 1 at a cost *u with probability 1* u. The control constraint is still u ! (0, 1]. 
Here we have 
H(1, u, J) = (1* u)(*u) + (1* u)J. 
It can be seen that for every policy µ, Tµ is again a contraction and we have Jµ = µ*1. Thus J* = *1, but again there is no optimal policy, stationary or not. Moreover, T has multiple fixed points: its set of fixed points within , is {J | J - *1}. Here the VI method will converge to J* starting from any J ! [*1,+). The PI method will produce an ever improving sequence of policies {µk} with Jµk ) J*, starting from any policy µ0, while µk will converge to 0, which is not a feasible policy. 
† An unusual fact about this problem is that there exists a nonstationary policy !# that is optimal in the sense that J!# = J# = !" (for a proof see [Ber12a], 
Section 3.2). The underlying intuition is that when the amount demanded u is 
decreased toward 0, the probability of noncompliance, u2, decreases much faster. This fact, however, will not be significant in the context of our analysis.
134 Semicontractive Models Chap. 3 
A Third Problem Variant 
Finally, let us again assume that 
H(1, u, J) = (1 * u)(*u) + (1* u)J, # u ! (0, 1], 
but also allow, in addition to u ! (0, 1], the choice u = 0 that self-transitions to state 1 at a cost c (this is the choice where the blackmailer can forego blackmail for a single period in exchange for a fixed payment *c). Here there is the extra (improper) policy µ$ that chooses µ$(1) = 0. We have 
Tµ"J = c+ J, 
and the mapping T is given by 
TJ = min 
( c+ J, inf 
0<u&1 
& * u+ u2 + (1* u)J 
'* . (3.4) 
Let us consider the optimal policies and the fixed points of T in the two cases where c " 0 and c < 0. 
When c " 0, we have J* = *1, while Jµ" = + (if c > 0) or Jµ" = 0 (if c = 0). It can be seen that there is no optimal policy, and that all J ! (*+,*1] are fixed points of T , including J*. Here the VI method will converge to J* starting from any J ! [*1,+). The PI method will produce an ever improving sequence of policies {µk}, with Jµk ) J*. However, µk 
will converge to 0, which is a feasible but strictly suboptimal policy. When c < 0, we have Jµ" = *+, and the improper policy µ$ is 
optimal. Here the optimal cost over just the proper policies is Ĵ = *1, while J* = *+. Moreover Ĵ is not a fixed point of T , and in fact T has no real-valued fixed points, although J* is a fixed point. It can be verified that the VI algorithm will converge to J* starting from any scalar J . Furthermore, starting with a proper policy, the PI method will produce the optimal (improper) policy within a finite number of iterations. 
3.1.4 Linear-Quadratic Problems 
One of the most important optimal control problems involves a linear system and a cost per stage that is positive semidefinite quadratic in the state and the control. The objective here is roughly to bring the system at or close to the origin, which can be viewed as a cost-free and absorbing state. Thus the problem has a shortest path character, even though the state space is continuous. 
Under reasonable assumptions (involving the notions of system controllability and observability; see e.g., [Ber17a], Section 3.1), the problem admits a favorable analysis and an elegant solution: the optimal cost function is positive semidefinite quadratic and the optimal policy is a linear
Sec. 3.1 Pathologies of Noncontractive DP Models 135 
function of the state. Moreover, Bellman’s equation can be equivalently written as an algebraic Riccati equation, which admits a unique solution within the class of nonnegative cost functions. 
On the other hand, the favorable results just noted depend on the assumptions and the structure of the linear-quadratic problem. There is no corresponding analysis for more general deterministic continuous-state optimal control problems. Moreover, even for linear-quadratic problems, when the aforementioned controllability and observability assumptions do not hold, the favorable results break down and pathological behavior can occur. This suggests analytical di!culties in more general continuous-state contexts, which we will discuss later in Section 3.5.5. 
To illustrate what can happen, consider the scalar system 
xk+1 = $xk + uk, xk ! ,, uk ! ,, 
with X = U(x) = ,, and a cost per stage equal to u2. Here we have J*(x) = 0 for all x ! ,, while the policy that applies control u = 0 at every state x is optimal. This is reminiscent of the deterministic shortest path problem of Section 3.1.1, for the case where a = 0 and there is a zero length cycle. Bellman’s equation has the form 
J(x) = min u!( 
& u2 + J($x+ u) 
' , x ! ,, 
and it is seen that J* is a solution. We will now show that there is another solution, which has an interesting interpretation. 
Let us assume that $ > 1 so the system is unstable (the instability of the system is important for the purpose of this example). It is well-known that for linear-quadratic problems the class of quadratic cost functions, 
S = & J | J(x) = px2, p " 0 
' , 
plays a special role. Linear policies of the form 
µ(x) = rx, 
where r is a scalar, also play a special role, particularly the subclass L of linear policies that are stable, in the sense that the closed-loop system 
xk+1 = ($ + r)xk 
is stable, i.e., |$+r| < 1. For such a policy, the generated system trajectory {xk}, starting from an initial state x0, is 
& ($+r)kx0 
' , and the correspond-
ing cost function is quadratic as shown by the following calculation, 
Jµ(x0) = # 
k=0 
! µ(xk) 
"2 = 
# 
k=0 
r2x2 k = 
# 
k=0 
r2($ + r)2kx2 0 = 
r2 
1* ($ + r)2 x2 0. 
(3.5)
136 Semicontractive Models Chap. 3 
Note that there is no policy in L that is optimal, since the optimal policy µ'(x) $ 0 is unstable and does not belong to L. 
Let us consider fixed points of the mapping T , 
(TJ)(x) = inf u!( 
& u2 + J($x+ u) 
' , 
within the class of nonnegative quadratic functions S. For J(x) = px2 with p " 0, we have 
(TJ)(x) = inf u!( 
& u2 + p($x+ u)2 
' , 
and by setting to 0 the derivative with respect to u, we see that the infimum is attained at 
u' = * p$ 
1 + p x. 
By substitution into the formula for TJ , we obtain 
(TJ)(x) = p$2 
1 + p x2. (3.6) 
Thus the function J(x) = px2 is a fixed point of T if and only if p solves the equation 
p = p$2 
1 + p . 
This equation has two solutions: 
p = 0 and p = $2 * 1, 
as shown in Fig. 3.1.4. Thus there are exactly two fixed points of T within S: the functions 
J*(x) $ 0 and Ĵ(x) = ($2 * 1)x2. 
The fixed point Ĵ has some significance. It turns out to be the optimal cost function within the subclass L of linear policies that are stable. This can be verified by minimizing the expression (3.5) over the parameter r. In particular, by setting to 0 the derivative with respect to r of 
r2 
1* ($ + r)2 , 
we obtain after a straightforward calculation that it is minimized for r = (1* $2)/$, which corresponds to the policy 
µ̂(x) = (1* $2) 
$ x,
Sec. 3.1 Pathologies of Noncontractive DP Models 137 
TJ 45 Degree Line Prob. = 1 Prob. = 
n Value Iterations 
!2 ! 1 1 p 
p p0 0 p1 1 p2 
= 0 
FunctionFunction p! 
2 
1+p 
Figure 3.1.4. Illustrating the fixed points of T , and the convergence of the VI algorithm for the one-dimensional linear-quadratic problem. 
while from Eq. (3.5), we can verify that 
Jµ̂(x) = ($2 * 1)x2. 
Thus, we have 
Jµ̂(x) = inf µ!L 
Jµ(x) = Ĵ(x), x ! ,. 
Let us turn now to the VI algorithm starting from a function in S. Using Eq. (3.6), we see that it generates a sequence of functions Jk ! S of the form 
Jk(x) = pkx2, 
where the sequence {pk} is generated by 
pk+1 = pk$2 
1 + pk , k = 0, 1, . . . . 
From Fig. 3.1.4 it can be seen that starting with p0 > 0, the sequence {pk} converges to 
p̂ = $2 * 1,
138 Semicontractive Models Chap. 3 
which corresponds to Ĵ . In summary, starting from any nonzero function in S, the VI algorithm converges to the optimal cost function Ĵ over the linear stable policies L, while starting from the zero function, it converges to the optimal cost function J*. 
Finally, let us consider the PI algorithm starting from a linear stable policy. We first note that given any µ ! L, i.e., 
µ(x) = rx with |$ + r| < 1, 
we can compute Jµ as the limit of the VI sequence {T k µJ}, where J is any 
function in S, i.e., 
J(x) = px2 with p " 0. 
This can be verified by writing 
(TµJ)(x) = ! r2 + p($ + r)2 
" x2, 
and noting that the iteration that maps p to r2 + p($ + r)2 converges to 
pµ = r2 
1* ($ + r)2 , 
in view of |$ + r| < 1. Thus, 
T k µJ ' Jµ, # µ ! L, J ! S. 
Moreover, we have Jµ = TµJµ. We now use a standard proof argument to show that PI generates 
a sequence of linear stable policies starting from a linear stable policy. Indeed, we have for all k, 
Jµ0 = Tµ0Jµ0 " TJµ0 = Tµ1Jµ0 " T k µ1Jµ0 " T kĴ = Ĵ , 
where the second inequality follows by the monotonicity of Tµ1 and the 
third inequality follows from the fact Jµ0 " Ĵ . By taking the limit as k ' +, we obtain 
Jµ0 " TJµ0 " Jµ1 " Ĵ . 
It can be verified that µ1 is a nonzero linear policy, so the preceding relation implies that µ1 is linear stable. Continuing similarly, it follows that the policies µk generated by PI are linear stable and satisfy for all k, 
Jµk " TJµk " Jµk+1 " Ĵ . 
By taking the limit as k ' +, we see that the sequence of quadratic functions {Jµk} converges monotonically to a quadratic function J#, which
Sec. 3.1 Pathologies of Noncontractive DP Models 139 
is a fixed point of T and satisfies J# " Ĵ . Since we have shown that Ĵ is the only fixed point of T in the range [Ĵ ,+), it follows that J# = Ĵ . In summary, the PI algorithm starting from a linear stable policy converges to Ĵ , the optimal cost function over linear stable policies. 
In Section 3.5.4, we will consider a more general multidimensional version of the linear-quadratic problem, using in part the analysis of Section 3.4. We will then explain the phenomena described in this section within a more general setting. We will also see there that the unusual behavior in the present example is due to the fact that there is no penalty for a nonzero state. For example, if the cost per stage is %x2 + u2, where % > 0, rather than u2, then the corresponding Bellman equation has a unique solution with the class of positive semidefinite quadratic functions. We will analyze this case within a more general setting of deterministic optimal control problems in Section 3.5.5. 
3.1.5 An Intuitive View of Semicontractive Analysis 
In the preceding sections we have demonstrated various aspects of the character of semicontractive analysis in the context of several examples. The salient feature is a class of “well-behaved” policies (e.g., proper policies in shortest path problems, stable policies in linear-quadratic problems), and the restricted optimal cost function Ĵ over just these policies. The main results we typically derived were that Ĵ is a fixed point of T , and that the VI and PI algorithms are attracted to Ĵ , at least from within some suitable class of initial conditions. In the favorable case where Ĵ = J*, these results hold also for J*, but in general J* need not be a fixed point of T . 
The central issue of semicontractive analysis is the choice of a class of “well-behaved” policies +M % M such that the corresponding restricted optimal cost function Ĵ is a fixed point of T . Such a choice is often fairly evident, but there are also several systematic approaches to identify a suitable class +M and to show its fixed point property; see the end of Section 3.2.2 for a discussion of various alternatives. As an example, let us introduce a class of policies +M % M for which we assume the following: 
(a) +M is well-behaved with respect to VI: For all µ ! +M and real-valued functions J , we have 
Jµ = TµJµ, Jµ = lim k"# 
T k µJ. (3.7) 
Moreover Jµ is real-valued. 
(b) +M is well-behaved with respect to PI: For each µ ! +M, any policy µ$ 
such that Tµ"Jµ = TJµ 
belongs to +M, and there exists at least one such µ$.
140 Semicontractive Models Chap. 3 
We can show that Ĵ is a fixed point of T and obtain our main results with the following line of argument. The first step in this argument is to show that the cost functions of a PI-generated sequence {µk} % +M (starting from a µ0 ! +M) are monotonically nonincreasing. Indeed, we have using Eq. (3.7), 
Jµk = TµkJµk " TJµk = Tµk+1Jµk . 
Using the monotonicity property of Tµk+1 , it follows that 
Jµk " TJµk " lim k"# 
T k µk+1Jµk = Jµk+1 " Ĵ , (3.8) 
where the equality holds by Eq. (3.7), and the rightmost inequality holds 
since µk+1 ! +M [by assumption (b) above]. Thus we obtain Jµk ) J# " Ĵ , for some function J#. 
Now by taking the limit as k ' + in the relation Jµk " TJµk " Jµk+1 
[cf. Eq. (3.8)], it follows (under a mild continuity assumption) that J# is a fixed point of T with J# " Ĵ . † We claim that J# = Ĵ . Indeed we have 
Ĵ - J# = T kJ# - T k µJ# - T k 
µJµ0 , # µ ! +M, k = 0, 1, . . . . 
By taking the limit as k ' +, and using the fact µ ! +M [cf. Eq. (3.7)], we 
obtain Ĵ - J# - Jµ for all µ ! +M. By taking the infimum over µ ! +M, it follows that J# = Ĵ . 
Finally, let J be real-valued and satisfy J " Ĵ . We claim that T kJ ' Ĵ . Indeed, since we have shown that Ĵ is a fixed point of T , we have 
T k µJ " T kJ " T kĴ = Ĵ , # µ ! +M, k " 0, 
† We elaborate on this argument; see also the proof of Prop. 3.2.4 in the next section. From Eq. (3.8), we have Jµk # TJµk # TJ$, so by letting k $ ", we obtain J$ # TJ$. For the reverse inequality, we assume that H has the property that H(x, u, J) = limm%$ H(x, u, Jm) for all x % X, u % U(x), and sequence {Jm} of real-valued functions with Jm & J . Thus we have 
H(x, u, J$) = lim k%$ 
H(x, u, Jµk ) # lim k%$ 
(TJµk )(x), x % X, u % U(x). 
By taking the limit in Eq. (3.8), we obtain 
lim k%$ 
(TJµk )(x) # lim k%$ 
Jµk+1(x) = J$(x), x % X, 
and from the preceding two relations we have H(x, u, J$) # J$(x). By taking 
the infimum over u % U(x), it follows that TJ$ # J$. Combined with the relation J$ # TJ$ shown earlier, this implies that J$ is a fixed point of T .
Sec. 3.2 Semicontractive Models and Regular Policies 141 
so by taking the limit as k ' + and using Eq. (3.7), we obtain 
Jµ " lim k"# 
T kJ " Ĵ , # µ ! +M. 
By taking the infimum over µ ! +M, it follows that T kJ ' Ĵ , i.e., that VI converges to Ĵ stating from all initial conditions J " Ĵ . 
The analysis of the following two sections will be based to a large extent on refinements of the preceding argument. Note that in this argument we have not assumed that Ĵ = J*, which leaves open the possibility that J* is not a fixed point of T . Indeed this can happen, as we have seen in the SSP example of Section 3.1.2. Moreover, we have not assumed that Ĵ is real-valued. In fact Ĵ may not be real-valued even though all Jµ, µ ! +M, are; see the first variant of the blackmailer problem of Section 3.1.3. 
An alternative analytical approach, which does not rely on +M being well-behaved with respect to PI, is given in Section 3.4. The idea there is to introduce a small %-perturbation to the mappingH and a corresponding “%-perturbed” problem. The perturbation is chosen so that the cost function of some policies, the “well-behaved” ones, is minimally a"ected [say by O(%)], while the cost function of the policies that are not “well-behaved” is driven to + for some initial states, thereby excluding these policies from optimality. Thus as % ) 0, the optimal cost function Ĵ" of the %-perturbed problem approaches Ĵ (not J*). Assuming that Ĵ" is a solution of the %-perturbed Bellman equation, and we can then use a limiting argument to show that Ĵ is a fixed point of T , as well as other results relating to the VI and PI algorithms. The perturbation approach will become more prominent in our semicontractive analysis of Chapter 4 (Sections 4.5 and 4.6), where we will consider “well-behaved” policies that are nonstationary, and thus do not lend themselves to a PI-based analysis. 
3.2 SEMICONTRACTIVE MODELS AND REGULAR POLICIES 
In the preceding section we illustrated a general pattern of pathologies in noncontractive models, involving the solutions of Bellman’s equation, and the convergence of the VI and PI algorithms. To summarize: 
(a) Bellman’s equation may have multiple solutions (equivalently, T may have multiple fixed points). Often but not always, J* is a fixed point of T . Moreover, a restricted problem, involving policies that are “wellbehaved” (proper in shortest path problems, or linear stable in the linear-quadratic case), may be meaningful and play an important role. 
(b) The optimal cost function over all policies, J*, may di"er from Ĵ , the optimal cost function over the “well-behaved” policies. Furthermore, it may be that Ĵ (not J*) is “well-behaved” from the algorithmic point of view. In particular, Ĵ is often a fixed point of T , in which
142 Semicontractive Models Chap. 3 
case it is the likely limit of the VI and the PI algorithms, starting from an appropriate set of initial conditions. 
In this section we will provide an analytical framework that explains this type of phenomena, and develops the kind of assumptions needed in order to avoid them. We will introduce a concept of regularity that formalizes mathematically the notion of “well-behaved” policy, and we will consider a restricted optimization problem that involves regular policies only. We will show that the optimal cost function of the restricted problem is a fixed point of T under several types of fairly natural assumptions. Moreover, we will show that it can be computed by versions of VI and PI, starting from suitable initial conditions. 
Problem Formulation 
Let us first introduce formally the model that we will use in this chapter. Compared to the contractive model of Chapter 2, it maintains the monotonicity assumption, but not the contraction assumption. 
We introduce the set X of states and the set U of controls, and for each x ! X , the nonempty control constraint set U(x) % U . Since in the absence of the contraction assumption, the cost function Jµ of some policies µ may take infinite values for some states, we will use the set of extended real numbers ,' = ,. {+,*+} = [*+,+]. The mathematical operations with + and *+ are standard and are summarized in Appendix A. We consider the set of all extended real-valued functions J : X &' ,', which we denote by E(X). We also denote by R(X) the set of real-valued functions J : X &' ,. 
As earlier, when we write lim, lim sup, or lim inf of a sequence of functions we mean it to be pointwise. We also write Jk ' J to mean that Jk(x) ' J(x) for each x ! X ; see Appendix A. 
We denote byM the set of all functions µ : X &' U with µ(x) ! U(x), for all x ! X , and by # the set of policies " = {µ0, µ1, . . .}, where µk ! M for all k. We refer to a stationary policy {µ, µ, . . .} simply as µ. We introduce a mapping H : X / U / E(X) &' ,' that satisfies the following. 
Assumption 3.2.1: (Monotonicity) If J, J $ ! E(X) and J - J $, then 
H(x, u, J) - H(x, u, J $), # x ! X, u ! U(x). 
The preceding monotonicity assumption will be in e"ect throughout this chapter. Consequently, we will not mention it explicitly in various propositions . We define the mapping T : E(X) &' E(X) by 
(TJ)(x) = inf u!U(x) 
H(x, u, J), # x ! X, J ! E(X),
Sec. 3.2 Semicontractive Models and Regular Policies 143 
and for each µ ! M the mapping Tµ : E(X) &' E(X) by 
(TµJ)(x) = H ! x, µ(x), J 
" , # x ! X, J ! E(X). 
The monotonicity assumption implies the following properties for all J, J $ ! E(X) and k = 0, 1, . . ., 
J - J $ 0 T kJ - T kJ $, T k µJ - T k 
µJ $, # µ ! M, 
J - TJ 0 T kJ - T k+1J, T k µJ - T k+1 
µ J, # µ ! M, 
which we will use extensively in various proof arguments. We now define cost functions associated with Tµ and T . In Chapter 
2 our starting point was to define Jµ and J* as the unique fixed points of Tµ and T , respectively, based on the contraction assumption used there. However, under our assumptions in this chapter this is not possible, so we use a di"erent definition, which nonetheless is consistent with the one of Chapter 2 (see the discussion of Section 2.1, following Prop. 2.1.2). We introduce a function J̄ ! E(X), and we define the infinite horizon cost of a policy in terms of the limit of its finite horizon costs with J̄ being the cost function at the end of the horizon. Note that in the case of the optimal control problems of the preceding section we have taken J̄ to be the zero function, J̄(x) $ 0 [cf. Eq. (3.2)]. 
Definition 3.2.1: Given a function J̄ ! E(X), for a policy " ! # with " = {µ0, µ1, . . .}, we define the cost function of " by 
J!(x) = lim sup k"# 
(Tµ0 · · ·Tµk J̄)(x), # x ! X. 
In the case of a stationary policy µ, the cost function of µ is denoted by Jµ and is given by 
Jµ(x) = lim sup k"# 
(T k µ J̄)(x), # x ! X. 
The optimal cost function J* is given by 
J*(x) = inf !!! 
J!(x), # x ! X. 
An optimal policy "' ! # is one for which J!# = J*. Note two important di"erences from Chapter 2: 
(1) Jµ is defined in terms of a pointwise lim sup rather than lim, since we don’t know whether the limit exists.
144 Semicontractive Models Chap. 3 
J Jµ 
Jµ 
S T k µJ J T 
J J T k µJ J 
J J T k µJ J 
Set S 
J J T 
J J T 
J J T 
S-regular policy µ µ S-irregular policy µ̄ 
Figure 3.2.1. Illustration of S-regular and S-irregular policies. Policy µ is S-regular because Jµ ! S and T k 
µJ # Jµ for all J ! S. Policy µ is S-irregular. 
(2) J! and Jµ in general depend on J̄ , so J̄ becomes an important part of the problem definition. 
Similar to Chapter 2, under the assumptions to be introduced in this chapter, stationary policies will typically turn out to be “su!cient” in the sense that the optimal cost obtained with nonstationary policies that depend on the initial state is matched by the one obtained by stationary ones. 
3.2.1 S-Regular Policies 
Our objective in this chapter is to construct an analytical framework with a strong connection to fixed point theory, based on the idea of separating policies into those that have “favorable” characteristics and those that do not. Clearly, a favorable property for a policy µ is that Jµ is a fixed point of Tµ. However, Jµ may depend on J̄ , even though Tµ does not depend on J̄ . It would thus appear that a related favorable property for µ is that Jµ stays the same if J̄ is changed arbitrarily within some set S. We express these two properties with the following definition (see Fig. 3.2.1). 
Definition 3.2.2: Given a set of functions S % E(X), we say that a stationary policy µ is S-regular if: 
(a) Jµ ! S and Jµ = TµJµ. 
(b) T k µJ ' Jµ for all J ! S. 
A policy that is not S-regular is called S-irregular . 
Thus a policy µ is S-regular if the VI algorithm corresponding to µ, Jk+1 = TµJk, represents a dynamic system that has Jµ as its unique
Sec. 3.2 Semicontractive Models and Regular Policies 145 
J TJ 
= 0 TµJ 
= 0 
! 
"-regular 
! 
-regular "-irregular 
) Jµ 
Figure 3.2.2. Illustration of S-regular and S-irregular policies for the case where there is only one state and S = $. There are three mappings Tµ corresponding to S-irregular policies: one crosses the 45-degree line at multiple points, another crosses at a single point but at an angle greater than 45 degrees, and the third is discontinuous and does not cross at all. The mapping Tµ of the $-regular policy has Jµ as its unique fixed point and satisfies T k 
µJ # Jµ for all J ! $. 
equilibrium within S, and is asymptotically stable in the sense that the iteration converges to Jµ, starting from any J ! S. 
For orientation purposes, we note the distinction between the set S and the problem data: S is not part of the problem’s definition. Its choice, however, can enable analysis and clarify properties of Jµ and J*. For example, we will later prove local fixed point statements such as 
“J* is the unique fixed point of T within S” 
or local region of attraction assertions such as 
“the VI sequence {T kJ} converges to J* starting from any J ! S.” 
Results of this type and their proofs depend on the choice of S: they may hold for some choices but not for others. 
Generally, with our selection of S we will aim to di"erentiate between S-regular and S-irregular policies in a manner that produces useful results for the given problem and does not necessitate restrictive assumptions. Examples of sets S that we will use are R(X), B(X), E(X), and subsets of R(X), B(X), and E(X) involving functions J satisfying J " J* or J " J̄ . However, there is a diverse range of other possibilities, so it makes sense to postpone making the choice of S more specific. Figure 3.2.2 illustrates the mappings Tµ of some S-regular and S-irregular policies for the case where there is a single state and S = ,. Figure 3.2.3 illustrates the mapping
146 Semicontractive Models Chap. 3 
J TJ 
= 0 TµJ 
= 0 J̄ = 0 ) Jµ 
S 
S S-regular 
Ĵ T k µ J̄ 
J̃ J 
Figure 3.2.3. Illustration of a mapping Tµ where there is only one state and S is a subset of the real line. Here Tµ has two fixed points, Jµ and J̃ . If S is as shown, µ is S-regular. If S is enlarged to include J̃ , µ becomes S-irregular. 
Tµ of an S-regular policy µ, where Tµ has multiple fixed points, and upon changing S, the policy may become S-irregular. 
3.2.2 Restricted Optimization over S-Regular Policies 
We will now introduce a restricted optimization framework where S-regular policies are central. Given a nonempty set S % E(X), let MS denote the set of policies that are S-regular, and consider optimization over just the set MS. The corresponding optimal cost function is denoted J* 
S : 
J* S(x) = inf 
µ!MS 
Jµ(x), # x ! X. (3.9) 
We say that µ' is MS-optimal if † 
µ' ! MS and Jµ# = J* S . 
An important question is whether J* S is a fixed point of T and can 
be obtained by the VI algorithm. Naturally, this depends on the choice of S, but it turns out that reasonable choices can be readily found in several important contexts, so the consequences of J* 
S being a fixed point of T are 
† Note that while S is assumed nonempty, it is possible that MS is empty. 
In this case our results will not be useful, but J* S is still defined by Eq. (3.9) as 
J* S(x) ' ". This is convenient in various proof arguments.
Sec. 3.2 Semicontractive Models and Regular Policies 147 
Jµ for µ ! MS 
J J! 
S 
Well-Behaved Region Fixed Point of T 
Well-Behaved Region WS 
! J ! E(X) 
J̃ ! S 
Figure 3.2.4. Interpretation of Prop. 3.2.1, where for illustration purposes, E(X) is represented by the extended real line. A set S % E(X) such that J# 
S is a fixed point of T , demarcates the well-behaved region WS [cf. Eq. (3.10)], within which T has a unique fixed point, and starting from which the VI algorithm converges to J# 
S . 
interesting. The next proposition shows that if J* S is a fixed point of T , 
then the VI algorithm is convergent starting from within the set 
WS = {J ! E(X) | J* S - J - J̃ for some J̃ ! S}, (3.10) 
which we refer to as the well-behaved region (see Fig. 3.2.4). Note that by the definition of S-regularity, the cost functions Jµ, µ ! MS , belong to S and hence also to WS . The proposition also provides a necessary and su!cient condition for an S-regular policy µ' to be MS-optimal. 
Proposition 3.2.1: (Well-Behaved Region Theorem) Given a set S % E(X), assume that J* 
S is a fixed point of T . Then: 
(a) (Uniqueness of Fixed Point) If J $ is a fixed point of T and there exists J̃ ! S such that J $ - J̃ , then J $ - J* 
S . In particular, if WS is nonempty, J* 
S is the unique fixed point of T within WS . 
(b) (VI Convergence) We have T kJ ' J* S for every J ! WS . 
(c) (Optimality Condition) If µ is S-regular, J* S ! S, and TµJ* 
S = TJ* 
S , then µ is MS-optimal. Conversely, if µ is MS-optimal, then TµJ* 
S = TJ* S . 
Proof: (a) For every µ ! MS , we have using the monotonicity of Tµ, 
J $ = TJ $ - TµJ $ - · · · - T k µJ $ - T k 
µ J̃ , k = 1, 2, . . . . 
Taking limit as k ' +, and using the S-regularity of µ, we obtain J $ - Jµ for all µ ! MS . Taking the infimum over µ ! MS , we have J $ - J* 
S . Assume that WS is nonempty. Then J* 
S is a fixed point of T that belongs to WS . To show its uniqueness, let J $ be another fixed point that
148 Semicontractive Models Chap. 3 
belongs to WS , so that J* S - J $ and there exists J̃ ! S such that J $ - J̃ . 
By what we have shown so far, J $ - J* S , implying that J $ = J* 
S . 
(b) Let J ! WS , so that J* S - J - J̃ for some J̃ ! S. We have for all k " 1 
and µ ! MS , J* S = T kJ* 
S - T kJ - T kJ̃ - T k µ J̃ , 
where the equality follows from the fixed point property of J* S , while the 
inequalities follow from the monotonicity and the definition of T . The right-hand side tends to Jµ as k ' +, since µ is S-regular and J̃ ! S. Hence the infimum over µ ! MS of the limit of the right-hand side tends to the left-hand side J* 
S . It follows that T kJ ' J* 
S . 
(c) From the assumptions TµJ* S = TJ* 
S and TJ* S = J* 
S , we have TµJ* S = J* 
S , and since J* 
S ! S and µ is S-regular, we have J* S = Jµ. Thus µ is MS-
optimal. Conversely, if µ is MS-optimal, we have Jµ = J* S , so that the 
fixed point property of J* S and the S-regularity of µ imply that 
TJ* S = J* 
S = Jµ = TµJµ = TµJ* S . 
Q.E.D. 
Some useful extensions and modified versions of the preceding proposition are given in Exercises 3.2-3.5. Let us illustrate the proposition in the context of the deterministic shortest path example of Section 3.1.1. 
Example 3.2.1 
Consider the deterministic shortest path example of Section 3.1.1 for the case where there is a zero length cycle (a = 0), and let S be the real line (. There are two policies: µ which moves from state 1 to the destination at cost b, and µ" which stays at state 1 at cost 0. We use X = {1} (i.e., we do not include t in X, since all function values of interest are 0 at t). Then by abbreviating function values J(1) with J , we have 
Jµ = b, Jµ" = 0, J# = min{b, 0}; 
cf. Fig. 3.2.5. The corresponding mappings Tµ, Tµ" , and T are 
TµJ = b, Tµ"J = J, J = TJ = min{b, J}, J % E(X), 
and the initial function J̄ is taken to be 0. It can be seen from the definition of S-regularity that µ is S–regular, while the policy µ" is not. The cost functions Jµ, Jµ" , and J# are fixed points of the corresponding mappings, but the sets of fixed points of Tµ" and T within S are ( and (!", b], respectively. Moreover, J# S = Jµ = b, so J# 
S is a fixed point of T and Prop. 3.2.1 applies. The figure also shows the well-behaved regions for the two cases b > 0 
and b < 0. It can be seen that the results of Prop. 3.2.1 are consistent with the discussion of Section 3.1.1. In particular, the VI algorithm fails when
Sec. 3.2 Semicontractive Models and Regular Policies 149 
1 2 t b a 1 2 
t b Destination 
t b c u!, Cost 0 Stationary policy costs Prob. 
Jµ(1) = b, Jµ!(1) = 0 Optimal cost 
(1) = 0 Optimal cost J!(1) = min{b, 0} a destination t 
Well-Behaved Region 
Well-Behaved Region 
J* = Jµ! = 0 
b Jµ! = 0 
Set of Fixed Points of T 
Set of Fixed Points of T 
J* S = Jµ = b > 0 
J* = J* S = Jµ = b < 0 
u, Cost b J 
Figure 3.2.5. The well-behaved region of Eq. (3.10) for the deterministic shortest path example of Section 3.1.1 when where there is a zero length cycle (a = 0). For S = $, the policy µ is S-regular, while the policy µ" is not. The figure illustrates the two cases where b > 0 and b < 0. 
started outside the well-behaved region, while when started from within the region, it is attracted to J# 
S rather than to J#. 
Let us now discuss some of the fine points of Prop. 3.2.1. The salient assumption of the proposition is that J' 
S is a fixed point of T . Depending on the choice of S, this may or may not be true, and much of the subsequent analysis in this chapter is geared towards the development of approaches to choose S so that J' 
S is a fixed point of T and has some other interesting properties. As an illustration of the range of possibilities, consider the three variants of the blackmailer problem of Section 3.1.3 for the choice S = ,: 
(a) In the first variant, we have J* = J* S = *+, and J* 
S is a fixed point of T that lies outside S. Here parts (a) and (b) of Prop. 3.2.1 apply. However, part (c) does not apply (even though we have TµJ* 
S = TJ* S 
for all policies µ) because J* S /! S, and in fact there is no MS-optimal 
policy. In the subsequent analysis, we will see that the condition J* S ! S plays an important role in being able to assert existence of an 
MS-optimal policy (see the subsequent Props. 3.2.5 and 3.2.6). 
(b) In the second variant, we have J* = J* S = *1, and J* 
S is a fixed point of T that lies within S. Here parts (a) and (b) of Prop. 3.2.1 apply, but part (c) still does not apply because there is no S-regular µ such
150 Semicontractive Models Chap. 3 
that TµJ* S = TJ* 
S, and in fact there is no MS-optimal policy. 
(c) In the third variant with c < 0, we have J* = *+, J* S = *1, and J* 
S 
is not a fixed point of T . Thus Prop. 3.2.1 does not apply, and in fact we have T kJ ' J* for every J ! WS (and not T kJ ' J* 
S). 
Another fine point is that Prop. 3.2.1(b) asserts convergence of the VI algorithm to J* 
S only for initial conditions J satisfying J* S - J - J̃ for 
some J̃ ! S. For an illustrative example of an S-regular µ, where {T k µJ} 
does not converge to Jµ starting from some J " Jµ that lies outside S, consider a case where there is a single state and a single policy µ that is S-regular, so J* 
S = Jµ. Suppose that Tµ : , &' , has two fixed points: Jµ and another fixed point J $ > Jµ. Let 
J̃ = (Jµ + J $)/2, S = (*+, J̃ ], 
and assume that Tµ is a contraction mapping within S (an example of this type can be easily constructed graphically). Then starting from any J ! S, we have T kJ ' Jµ, so that µ is S-regular. However, since J $ is a fixed point of T , the sequence {T kJ $} stays at J $ and does not converge to Jµ. The di!culty here is that WS = [Jµ, J̃ ] and J $ /! WS . 
Still another fine point is that if there exists an MS-optimal policy µ, we have J* 
S = TµJ* S (since J* 
S = Jµ and µ is S-regular), but this does not guarantee that J* 
S is a fixed point of T , which is essential for Prop. 3.2.1. This can be seen from an example given in Fig. 3.2.6, where there exists an MS-optimal policy, but both J* 
S and J* are not fixed points of T (in this example the MS-optimal policy is also overall optimal so J* 
S = J*). In particular, starting from J* 
S , the VI algorithm converges to some J $ (= J* S 
that is a fixed point of T . 
Convergence Rate when a Contractive Policy is MS-Optimal 
In many contexts where Prop. 3.2.1 applies, there exists an MS-optimal policy µ such that Tµ is a contraction with respect to a weighted sup-norm. This is true for example in the shortest path problem to be discussed in Section 3.5.1. In such cases, the rate of convergence of VI to J* 
S is linear, as shown in the following proposition. 
Proposition 3.2.2: (Convergence Rate of VI) Let S be equal to B(X), the space of all functions over X that are bounded with respect to a weighted sup-norm 1 · 1v corresponding to a positive function v : X &' ,. Assume that J* 
S is a fixed point of T , and that there exists an MS-optimal policy µ such that Tµ is a contraction with respect to 1 · 1v, with modulus of contraction &. Then J* 
S ! B(X), WS % B(X), and
Sec. 3.2 Semicontractive Models and Regular Policies 151 
J TJJ̄ = 0Jµ 
!-regular 
! 
-regular "-irregular 
TµJ T 
J TµJ 
J̄ T k µ J̄ 
! J! 
J TJ! 
) 1] Jµ = J* = J* 
SJ ! 
Figure 3.2.6. Illustration of why the assumption that J# S is a fixed point of T is 
essential for Prop. 3.2.1. In this example there is only one state and S = $. There are two stationary policies: µ for which Tµ is a contraction, so µ is $-regular, and µ for which Tµ has multiple fixed points, so µ is $-irregular. Moreover, Tµ is discontinuous from above at Jµ as shown. Here, it can be verified that Tµ0 
· · · Tµk J̄ & Jµ for all µ0, . . . , µk and k, so that J! & Jµ for all ! and the S-
regular policy µ is optimal, so J# S = J#. However, as can be seen from the figure, 
we have J# S = J# '= TJ# = TJ# 
S . Moreover, starting at J# S , the VI sequence T kJ# 
S converges to J ", the fixed point of T shown in the figure, and all parts of Prop. 3.2.1 fail. 
,,TJ * J* S1v - &1J * J* 
S1v, # J ! WS . (3.11) 
Moreover, we have 
1J * J* S1v -
1 
1* & sup x!X 
J(x) * (TJ)(x) 
v(x) , # J ! WS . (3.12) 
Proof: Since µ is S-regular and S = B(X), we have J* S = Jµ ! B(X) as 
well as WS % B(X). By using the MS-optimality of µ and Prop. 3.2.1(c), 
J* S = TµJ* 
S = TJ* S, 
so for all x ! X and J ! WS , 
(TJ)(x)* J* S(x) 
v(x) -
(TµJ)(x) * (TµJ* S)(x) 
v(x) - &max 
x!X 
J(x)* J* S(x) 
v(x) , 
where the second inequality holds by the contraction property of Tµ. By taking the supremum of the left-hand side over x ! X , and by using the fact TJ " TJ* 
S = J* S for all J ! WS , we obtain Eq. (3.11).
152 Semicontractive Models Chap. 3 
By using again the relation TµJ* S = TJ* 
S, we have for all x ! X and all J ! WS , 
J(x)* J* S(x) 
v(x) = 
J(x)* (TJ)(x) 
v(x) + 
(TJ)(x)* J* S(x) 
v(x) 
-J(x)* (TJ)(x) 
v(x) + 
(TµJ)(x) * (TµJ* S)(x) 
v(x) 
-J(x)* (TJ)(x) 
v(x) + &1J * J* 
S1v. 
By taking the supremum of both sides over x, we obtain Eq. (3.12). Q.E.D. 
Approaches to Show that J* S is a Fixed Point of T 
The critical assumption of Prop. 3.2.1 is that J* S is a fixed point of T . For 
a specific application, this must be proved with a separate analysis after a suitable set S is chosen. To this end, we will provide several approaches that guide the choice of S and facilitate the analysis. 
One approach applies to problems where J* is generically a fixed point of T , in which case for every set S such that J* 
S = J*, Prop. 3.2.1 applies and shows that J* can be obtained by the VI algorithm starting from any J ! WS . Exercise 3.1 provides some conditions that guarantee that J* is a fixed point of T . These conditions can be verified in wide classes of problems such as deterministic models. Sections 3.5.4 and 3.5.5 illustrate this approach. Other important models where J* is guaranteed to be a fixed point of T are the monotone increasing and monotone decreasing models of Section 4.3. We will discuss the application of Prop. 3.2.1 and other related results to these models in Chapter 4. 
In the present chapter the approach for showing that J* S is a fixed 
point of T will be mostly based on the PI algorithm; cf. the discussion of Section 3.1.5. An alternative and complementary approach is the perturba-tion-based analysis to be given in Section 3.4. This approach will be applied to a variety of problems in Section 3.5, and will also be prominent in Sections 4.5 and 4.6 of the next chapter. 
3.2.3 Policy Iteration Analysis of Bellman’s Equation 
We will develop a PI-based approach for showing that J* S is a fixed point 
of T . The approach is applicable under assumptions that guarantee that there is a sequence {µk} of S-regular policies that can be generated by PI. The significance of S-regularity of all µk lies in that the corresponding cost function sequence {Jµk} belongs to the well-behaved region of Eq. (3.10), and is monotonically nonincreasing (see the subsequent Prop. 3.2.3). Un-der an additional mild technical condition, the limit of this sequence is a fixed point of T and is in fact equal to J* 
S (see the subsequent Prop. 3.2.4).
Sec. 3.2 Semicontractive Models and Regular Policies 153 
Let us consider the standard form of the PI algorithm, which starts with a policy µ0 and generates a sequence {µk} of stationary policies according to 
Tµk+1Jµk = TJµk , k = 0, 1, . . . . (3.13) 
This iteration embodies both the policy evaluation step, which computes Jµk in some way, and the policy improvement step, which computes µk+1(x) as a minimum over u ! U(x) of H(x, u, Jµk ) for each x ! X . Of course, to be able to carry out the policy improvement step, there should be enough assumptions to guarantee that the minimum is attained for every x. One such assumption is that U(x) is a finite set for each x ! X . A more general assumption, which applies to the case where the constraint sets U(x) are infinite, will be given in Section 3.3. 
The evaluation of the cost function Jµ of a policy µ may be done by solving the equation Jµ = TµJµ, which holds when µ is an S-regular policy. An important fact is that if the PI algorithm generates a sequence {µk} consisting exclusively of S-regular policies, then not only the policy evaluation is facilitated through the equation Jµ = TµJµ, but also the sequence of cost functions {Jµk} is monotonically nonincreasing, as we will show next. 
Proposition 3.2.3: (Policy Improvement Under S-Regularity) Given a set S % E(X), assume that {µk} is a sequence generated by the PI algorithm (3.13) that consists of S-regular policies. Then 
Jµk " Jµk+1 , k = 0, 1, . . . . 
Proof: Using the S-regularity of µk and Eq. (3.13), we have 
Jµk = TµkJµk " TJµk = Tµk+1Jµk . (3.14) 
By using the monotonicity of Tµk+1 , we obtain 
Jµk " TJµk " lim m"# 
Tm µk+1Jµk = Jµk+1 , (3.15) 
where the equation on the right holds since µk+1 is S-regular and Jµk ! S (in view of the S-regularity of µk). Q.E.D. 
The preceding proposition shows that if a sequence of S-regular policies {µk} is generated by PI, the corresponding cost function sequence {Jµk} is monotonically nonincreasing and hence converges to a limit J#. Under mild conditions, we will show that J# is a fixed point of T and is equal to J* 
S . This is important as it brings to bear Prop. 3.2.1, and the
154 Semicontractive Models Chap. 3 
associated results on VI convergence and optimality conditions. Let us first formalize the property that the PI algorithm can generate a sequence of S-regular policies. 
Definition 3.2.3: (Weak PI Property) We say that a set S % E(X) has the weak PI property if there exists a sequence of S-regular policies that can be generated by the PI algorithm [i.e., a sequence {µk} that satisfies Eq. (3.13) and consists of S-regular policies]. 
Note a fine point here. For a given starting policy µ0, there may be many di"erent sequences {µk} that can be generated by PI [i.e., satisfy Eq. (3.13)]. While the weak PI property guarantees that some of these consist of S-regular policies exclusively, there may be some that do not. The policy improvement property shown in Prop. 3.2.3 holds for the former sequences, but not necessarily for the latter. The following proposition provides the basis for showing that J* 
S is a fixed point of T based on the weak PI property. 
Proposition 3.2.4: (Weak PI Property Theorem) Given a set S % E(X), assume that: 
(1) S has the weak PI property. 
(2) For each sequence {Jm} % S with Jm ) J for some J ! E(X), we have 
H (x, u, J) = lim m"# 
H(x, u, Jm), # x ! X, u ! U(x). (3.16) 
Then: 
(a) J* S is a fixed point of T and the conclusions of Prop. 3.2.1 hold. 
(b) (PI Convergence) Every sequence of S-regular policies {µk} that can be generated by PI satisfies Jµk ) J* 
S . If in addition the set 
of S-regular policies is finite, there exists k̄ " 0 such that µk̄ is MS-optimal. 
Proof: (a) Let {µk} be a sequence of S-regular policies generated by the PI algorithm (there exists such a sequence by the weak PI property). Then by Prop. 3.2.3, the sequence {Jµk} is monotonically nonincreasing and must 
converge to some J# " J* S . 
We first show that J# is a fixed point of T . Indeed, from Eq. (3.14),
Sec. 3.2 Semicontractive Models and Regular Policies 155 
we have Jµk " TJµk " TJ#, 
so by letting k ' +, we obtain J# " TJ#. From Eq. (3.15) we also have TJµk " Jµk+1 Taking the limit in this relation as k ' +, we obtain 
lim k"# 
(TJµk)(x) " lim k"# 
Jµk+1(x) = J#(x), x ! X. 
By using Eq. (3.16) we also have 
H(x, u, J#) = lim k"# 
H(x, u, Jµk) " lim k"# 
(TJµk)(x), x ! X, u ! U(x). 
By combining the preceding two relations, we obtain 
H(x, u, J#) " J#(x), x ! X, u ! U(x), 
and by taking the infimum of the left-hand side over u ! U(x), it follows that TJ# " J#. Thus J# is a fixed point of T . 
Finally, we show that J# = J* S . Indeed, since J* 
S - Jµk , we have 
J* S - J# = T kJ# - T k 
µJ# - T k µJµ0 , # µ ! MS , k = 0, 1, . . . . 
By taking the limit as k ' +, and using the fact µ ! MS and Jµ0 ! S, it 
follows that J* S - J# - Jµ, for all µ ! MS . By taking the infimum over 
µ ! MS, it follows that J# = J* S , so J* 
S is a fixed point of T . 
(b) The limit of {Jµk} was shown to be equal to J* S in the preceding proof. 
Moreover, the finiteness of MS and the policy improvement property of Prop. 3.2.3 imply that some µk̄ is MS-optimal. Q.E.D. 
Note that under the weak PI property, the preceding proposition shows convergence of the PI-generated cost functions Jµk to J* 
S but not necessarily to J*. An example of this type of behavior was seen in the linear-quadratic problem of Section 3.1.4 (where S is the set of nonnegative quadratic functions). Let us describe another example, which shows in addition that under the weak PI property, it is possible for the PI algorithm to generate a nonmonotonic sequence of policy cost functions that includes both optimal and strictly suboptimal policies. 
Example 3.2.2: (Weak PI Property and the Deterministic Shortest Path Example) 
Consider the deterministic shortest path example of Section 3.1.1 for the case where there is a zero length cycle (a = 0), and let S be the real line (, as in Example 3.2.1. There are two policies: µ which moves from state 1 to the destination at cost b, and µ" which stays at state 1 at cost 0. Starting with the S-regular policy µ, the PI algorithm generates the policy that corresponds
156 Semicontractive Models Chap. 3 
to the minimum in TJµ = min{b, Jµ} = min{b, b}. Thus both the S-regular policy µ and the S-irregular µ" can be generated at the first iteration. This means that the weak PI property holds (although the strong PI property, which will be introduced shortly, does not hold). Indeed, consistent with Prop. 3.2.4, we have that J# 
S = Jµ = b is a fixed point of T , in fact the only fixed point of T in the well-behaved region {J | J # b}. 
An interesting fact here is that when b < 0, and PI is started with the optimal S-regular policy µ, then it may generate the S-irregular policy µ", and from that policy, it will generate µ again. Thus the weak PI property does not preclude the PI algorithm from generating a policy sequence that includes S-irregular policies, with corresponding policy cost functions that are oscillating. 
Let us also revisit the blackmailer example of Section 3.1.3. In the first variant of that example, when S = ,, all policies are S-regular, the weak PI property holds, and Prop. 3.2.4 applies. In this case, PI will generate a sequence of S-regular policies that converges to J* 
S = *+, which is a fixed point of T , consistent with Prop. 3.2.4 (even though J* 
S /! S and there is no MS-optimal policy). 
Analysis Under the Strong PI Property 
Proposition 3.2.4(a) does not guarantee that every sequence {µk} generated by the PI algorithm satisfies Jµk ) J* 
S . This is true only for the sequences that consist of S-regular policies. We know that when the weak PI property holds, there exists at least one such sequence, but PI can also generate sequences that contain S-irregular policies, even when started with an S-regular policy, as we have seen in Example 3.2.2. We thus introduce a stronger type of PI property, which will guarantee stronger conclusions. 
Definition 3.2.4: (Strong PI Property) We say that a set S % E(X) has the strong PI property if: 
(a) There exists at least one S-regular policy. 
(b) For every S-regular policy µ, any policy µ$ such that Tµ"Jµ = TJµ is S-regular, and there exists at least one such µ$. 
The strong PI property implies that every sequence that can be generated by PI starting from an S-regular policy consists exclusively of S-regular policies. Moreover, there exists at least one such sequence. Hence the strong PI property implies the weak PI property. Thus if the strong PI property holds together with the mild continuity condition (2) of Prop. 3.2.4, it follows that J* 
S is a fixed point of T and Prop. 3.2.1 applies. We will see that the strong PI property implies additional results, relating to the uniqueness of the fixed point of T .
Sec. 3.2 Semicontractive Models and Regular Policies 157 
The following proposition provides conditions guaranteeing that S has the strong PI property. The salient feature of these conditions is that they preclude optimality of an S-irregular policy [see condition (4) of the proposition]. 
Proposition 3.2.5: (Verifying the Strong PI Property) Given a set S % E(X), assume that: 
(1) J(x) < + for all J ! S and x ! X . 
(2) There exists at least one S-regular policy. 
(3) For every J ! S there exists a policy µ such that TµJ = TJ . 
(4) For every J ! S and S-irregular policy µ, there exists a state x ! X such that 
lim sup k"# 
(T k µJ)(x) = +. (3.17) 
Then: 
(a) A policy µ satisfying TµJ - J for some function J ! S is S-regular. 
(b) S has the strong PI property. 
Proof: (a) By the monotonicity of Tµ, we have lim supk"# T k µJ - J , and 
since by condition (1), J(x) < + for all x, it follows from Eq. (3.17) that µ is S-regular. 
(b) In view of condition (3), it will su!ce to show that for every S-regular policy µ, any policy µ$ such that Tµ"Jµ = TJµ is also S-regular. Indeed 
Tµ"Jµ = TJµ - TµJµ = Jµ, 
so µ$ is S-regular by part (a). Q.E.D. 
A representative example where the preceding proposition applies is a deterministic shortest path problem where all cycles have positive length (see the subsequent Example 3.2.3, and other examples later that involve SSP problems; see Sections 3.3 and 3.5). For an example where the assumptions of the proposition fail, consider the linear-quadratic problem of Section 3.1.4. Here S is the set of nonnegative quadratic functions, but the optimal policy µ' that applies control u = 0 at all states is S-irregular, since we do not have T k 
µ#J ' Jµ# = 0 for J equal to a positive quadratic function, while condition (4) of the proposition does not hold. Thus we cannot conclude that the strong PI property holds in the absence of additional analysis.
158 Semicontractive Models Chap. 3 
We next derive some of the implications of the strong PI property regarding fixed properties of J* 
S . In particular, we show that if J* S ! S, 
then J* S is the unique fixed point of T within S. This result will be the 
starting point for the analysis of Section 3.3. 
Proposition 3.2.6: (Strong PI Property Theorem) Let S satisfy the conditions of Prop. 3.2.5. 
(a) (Uniqueness of Fixed Point) If T has a fixed point within S, then this fixed point is equal to J* 
S . 
(b) (Fixed Point Property and Optimality Condition) If J* S ! S, then 
J* S is the unique fixed point of T within S and the conclusions of 
Prop. 3.2.1 hold. Moreover, every policy µ that satisfies TµJ* S = 
TJ* S is MS-optimal and there exists at least one such policy. 
(c) (PI Convergence) If for each sequence {Jm} % S with Jm ) J for some J ! E(X), we have 
H (x, u, J) = lim m"# 
H(x, u, Jm), # x ! X, u ! U(x), 
then J* S is a fixed point of T , and every sequence {µk} generated 
by the PI algorithm starting from an S-regular policy µ0 satisfies Jµk ) J* 
S . Moreover, if the set of S-regular policies is finite, there 
exists k̄ " 0 such that µk̄ is MS-optimal. 
Proof: (a) Let J $ ! S be a fixed point of T . Then for every µ ! MS and k " 1, we have J $ = T kJ $ - T k 
µJ $. By taking the limit as k ' +, we have J $ - Jµ, and by taking the infimum over µ ! MS , we obtain J $ - J* 
S . For the reverse inequality, let µ$ be such that J $ = TJ $ = Tµ"J $ [cf. condition (3) of Prop. 3.2.5]. Then by Prop. 3.2.5(a), it follows that µ$ is S-regular, and since J $ ! S, by the definition of S-regularity, we have J $ = Jµ" " J* 
S , showing that J $ = J* 
S . 
(b) For every µ ! MS we have Jµ " J* S , so that 
Jµ = TµJµ " TµJ* S " TJ* 
S. 
Taking the infimum over all µ ! MS , we obtain J* S " TJ* 
S. Let µ be a policy such that TJ* 
S = TµJ* S , [there exists one by condition (3) of Prop. 3.2.5, 
since we assume that J* S ! S]. The preceding relations yield J* 
S " TµJ* S , 
so by Prop. 3.2.5(a), µ is S-regular. Therefore, we have 
J* S " TJ* 
S = TµJ* S " lim 
k"# T k µJ* 
S = Jµ " J* S , 
where the second equality holds since µ was proved to be S-regular, and J* S ! S by assumption. Hence equality holds throughout in the above
Sec. 3.2 Semicontractive Models and Regular Policies 159 
relation, which proves that J* S is a fixed point of T (implying the conclusions 
of Prop. 3.2.1) and that µ is MS-optimal. 
(c) Since the strong PI property [which holds by Prop. 3.2.5(b)] implies the weak PI property, the result follows from Prop. 3.2.4(b). Q.E.D. 
The preceding proposition does not address the question whether J* 
is a fixed point of T , and does not guarantee that VI converges to J* S or 
J* starting from every J ! S. We will consider both of these issues in the next section. Note, however, a consequence of part (a): if J* is known to be a fixed point of T and J* ! S, then J* = J* 
S . Let us now illustrate with examples some of the fine points of the 
analysis. For an example where the preceding proposition does not apply, consider the first two variants of the blackmailer problem of Section 3.1.3. Let us take S = ,, so that all policies are S-regular and the strong PI property holds. In the first variant of the problem, we have J* = J* 
S = *+, and consistent with Prop. 3.2.4, J* 
S is a fixed point of T . However, J* S /! S, and T has no fixed points within S. On the other hand if we 
change S to be [*+,+), there are no S-regular policies at all, since for J = *+ ! S, we have T k 
µJ = *+ < Jµ for all µ. As noted earlier, both Props. 3.2.1 and 3.2.4 do apply. In the second variant of the problem, we have J* = J* 
S = *1, while the set of fixed points of T within S is (*+,*1], so Prop. 3.2.6(a) fails. The reason is that the condition (3) of Prop. 3.2.5 is violated. 
The next example, when compared with Example 3.2.2, illustrates the di"erence in PI-related results obtained under the weak and the strong PI properties. Moreover it highlights a generic di!culty in applying PI, even if the strong PI property holds, namely that an initial S-regular policy must be available. 
Example 3.2.3: (Strong PI Property and the Deterministic Shortest Path Example) 
Consider the deterministic shortest path example of Section 3.1.1 for the case where the cycle has positive length (a > 0), and let S be the real line (, as in Example 3.2.1. The two policies are: µ which moves from state 1 to the destination at cost b and is S-regular, and µ" which stays at state 1 at cost a, which is S-irregular. However, µ" has infinite cost and satisfies Eq (3.17). As a result, Prop. 3.2.5 applies and the strong PI property holds. Consistent with Prop. 3.2.6, J# 
S is the unique fixed point of T within S. Turning now to the PI algorithm, we see that starting from the S-regular 
µ, which is optimal, it stops at µ, consistent with Prop. 3.2.6(c). However, starting from the S-irregular policy µ" the policy evaluation portion of the PI algorithm must be able to deal with the infinite cost values associated with µ". This is a generic di"culty in applying PI to problems where there are irregular policies: we either need to know an initial S-regular policy, or
160 Semicontractive Models Chap. 3 
appropriately modify the PI algorithm. See the discussions in Sections 3.5.1 and 3.6.2. 
3.2.4 Optimistic Policy Iteration and !-Policy Iteration 
We have already shown the validity of the VI and PI algorithms for computing J* 
S (subject to various assumptions, and restrictions involving the starting points). In this section and the next one we will consider some additional algorithmic approaches that can be justified based on the preceding analysis. 
An Optimistic Form of PI 
Let us consider an optimistic variant of PI, where policies are evaluated inexactly, with a finite number of VIs. In particular, this algorithm starts with some J0 ! E(X) such that J0 " TJ0, and generates a sequence {Jk, µk} according to 
TµkJk = TJk, Jk+1 = Tmk 
µk Jk, k = 0, 1, . . . , (3.18) 
where mk is a positive integer for each k. The following proposition shows that optimistic PI converges under 
mild assumptions to a fixed point of T , independently of any S-regularity framework. However, when such a framework is introduced, and the sequence generated by optimistic PI generates a sequence of S-regular policies, then the algorithm converges to J* 
S , which is in turn a fixed point of T , similar to the PI convergence result under the weak PI property; cf. Prop. 3.2.4(b). 
Proposition 3.2.7: (Convergence of Optimistic PI) Let J0 ! E(X) be a function such that J0 " TJ0, and assume that: 
(1) For all µ ! M, we have Jµ = TµJµ, and for all J ! E(X) with J - J0, there exists µ̄ ! M such that Tµ̄J = TJ . 
(2) For each sequence {Jm} % E(X) with Jm ) J for some J ! E(X), we have 
H (x, u, J) = lim m"# 
H(x, u, Jm), # x ! X, u ! U(x). 
Then the optimistic PI algorithm (3.18) is well defined and the following hold: 
(a) The sequence {Jk} generated by the algorithm satisfies Jk ) J#, where J# is a fixed point of T .
Sec. 3.2 Semicontractive Models and Regular Policies 161 
(b) If for a set S % E(X), the sequence {µk} generated by the algorithm consists of S-regular policies, and we have Jk ! S for all k, then Jk ) J* 
S and J* S is a fixed point of T . 
Proof: (a) Condition (1) guarantees that the sequence {Jk, µk} is well defined in the following argument. We have 
J0 " TJ0 = Tµ0J0 " Tm0 µ0 J0 = J1 
" Tm0+1 µ0 J0 = Tµ0J1 " TJ1 = Tµ1J1 " · · · " J2, 
(3.19) and continuing similarly, we obtain 
Jk " TJk " Jk+1, k = 0, 1, . . . . (3.20) 
Thus Jk ) J# for some J#. The proof that J# is a fixed point of T is similar to the case of the 
PI algorithm (3.13) in Prop. 3.2.4. In particular, from Eq. (3.20), we have Jk " TJ#, and by taking the limit as k ' +, 
J# " TJ#. 
For the reverse inequality, we use Eq. (3.20) to write 
H(x, u, Jk) " (TJk)(x) " J#(x), # x ! X, u ! U(x). 
By taking the limit as k ' + and using condition (2), we have that 
H(x, u, J#) " J#(x), # x ! X, u ! U(x). 
By taking the infimum over u ! U(x), we obtain 
TJ# " J#, 
thus showing that TJ# = J#. 
(b) In the case where all the policies µk are S-regular and {Jk} % S, from Eq. (3.19), we have Jk+1 " Jµk for all k, so it follows that 
J# = lim k"# 
Jk " lim inf k"# 
Jµk " J* S . 
We will also show that the reverse inequality holds, so that J# = J* S . 
Indeed, for every S-regular policy µ and all k " 0, we have 
J# = T kJ# - T k µJ# - T k 
µJ0,
162 Semicontractive Models Chap. 3 
from which by taking limit as k ' + and using the assumption J0 ! S, we obtain 
J# - lim k"# 
T k µJ0 = Jµ, # µ ! MS . 
Taking infimum over µ ! MS , we have J# - J* S . Thus, J# = J* 
S , and by using the properties of J# proved in part (a), the result follows. Q.E.D. 
Note that, in general, the fixed point J# in Prop. 3.2.7(a) need not be equal to J* 
S or J*. As an illustration, consider the shortest path Example 3.2.1 with S = ,, and a = 0, b > 0. Then if 0 < J0 < b, it can be seen that Jk = J0 for all k, so J* = 0 < J# and J# < J* 
S = b. 
!-Policy Iteration 
We next consider !-policy iteration (!-PI for short), which was described in Section 2.5. It involves a scalar ! ! (0, 1) and it is defined by 
TµkJk = TJk, Jk+1 = T (#) 
µk Jk, (3.21) 
where for any policy µ and scalar ! ! (0, 1), T (#) µ is the multistep mapping 
discussed in Section 1.2.5: 
(T (#) µ J)(x) = (1* !) 
# 
t=0 
!t(T t+1 µ J)(x), x ! X. (3.22) 
Here we assume that the limit of the series above is well-defined as a function in E(X) for all x ! X , µ ! M, and J ! E(X). 
We will also assume that Tµ and T (#) µ commute, i.e., 
Tµ(T (#) µ J) = T (#) 
µ (TµJ), # µ ! M, J ! E(X). (3.23) 
This assumption is commonly satisfied in DP problems where Tµ is linear, such as the stochastic optimal control problem of Example 1.2.1. 
To compare the !-PI method (3.21) with the exact PI algorithm (3.13), note that by the analysis of Section 1.2.5 (see also Exercise 1.2), 
the mapping T (#) 
µk is an extrapolated version of the proximal mapping for 
solving the fixed point equation J = TµkJ . Thus in !-PI, the policy evaluation phase is done approximately with a single iteration of the (extrapolated) proximal algorithm. 
As noted in Section 2.5, the !-PI and the optimistic PI methods are 
related. The reason is that both mappings T (#) 
µk and Tmk 
µk involve multiple 
applications of the VI mapping Tµk : a fixed number mk in the latter case, and a geometrically weighted infinite number in the former case [cf. Eq. (3.22)]. Thus !-PI and optimistic PI use VI in alternative ways to evaluate Jµk approximately.
Sec. 3.2 Semicontractive Models and Regular Policies 163 
Since !-PI and optimistic PI are related, it is not surprising that they have the same type of convergence properties. We have the following proposition, which is similar to Prop. 3.2.7. 
Proposition 3.2.8: (Convergence of !-PI) Let J0 ! E(X) be a function such that J0 " TJ0, assume that the limit in the series (3.22) is well defined and Eq. (3.23) holds. Assume further that: 
(1) For all µ ! M, we have Jµ = TµJµ, and for all J ! E(X) with J - J0, there exists µ̄ ! M such that Tµ̄J = TJ . 
(2) For each sequence {Jm} % E(X) with Jm ) J for some J ! E(X), we have 
H (x, u, J) = lim m"# 
H(x, u, Jm), # x ! X, u ! U(x). 
Then the !-PI algorithm (3.21) is well defined and the following hold: 
(a) A sequence {Jk} generated by the algorithm satisfies Jk ) J#, where J# is a fixed point of T . 
(b) If for a set S % E(X), the sequence {µk} generated by the algorithm consists of S-regular policies, and we have Jk ! S for all k, then Jk ) J* 
S and J* S is a fixed point of T . 
Proof: (a) We first note that for all µ ! M and J ! E(X) such that J " TµJ , we have 
TµJ " T (#) µ J. 
This follows from the power series expansion (3.22) and the fact that J " TµJ implies that 
TµJ " T 2 µJ " · · · " Tm+1 
µ J, # m " 1. 
Using also the monotonicity of Tµ and T (#) µ , and Eq. (3.23), we have that 
J " TµJ 0 TµJ " T (#) µ J " T (#) 
µ (TµJ) = Tµ(T (#) µ J). 
The preceding relation and our assumptions imply that 
J0 " TJ0 = Tµ0J0 " T (#) µ0 J0 = J1 
" Tµ0(T (#) µ0 J0) = Tµ0J1 " TJ1 = Tµ1J1 " · · · " J2. 
Continuing similarly, we obtain Jk " TJk " Jk+1 for all k. Thus Jk ) J# for some J#. From this point, the proof that J# is a fixed point of T is similar to the one of Prop. 3.2.7(a). 
(b) Similar to the proof of Prop. 3.2.7(b). Q.E.D.
164 Semicontractive Models Chap. 3 
3.2.5 A Mathematical Programming Approach 
Let us finally consider an alternative to the VI and PI approaches. It is based on the fact that J* 
S is an upper bound to all functions J ! S that satisfy J - TJ , as we will show shortly. We will exploit this fact to obtain a method to compute J* 
S that is based on solution of a related mathematical programming problem. We have the following proposition. 
Proposition 3.2.9: Given a set S % E(X), for all functions J ! S satisfying J - TJ , we have J - J* 
S . 
Proof: If J ! S and J - TJ , by repeatedly applying T to both sides and using the monotonicity of T , we obtain J - T kJ - T k 
µJ for all k and S-regular policies µ. Taking the limit as k ' +, we obtain J - Jµ, so by taking the infimum over µ ! MS, we obtain J - J* 
S . Q.E.D. 
Thus if J* S is a fixed point of T , it is the “largest” fixed point of T , and 
we can use the preceding proposition to compute J* S by maximizing an ap-
propriate monotonically increasing function of J subject to the constraints J ! S and J - TJ . † This approach, when applied to finite-spaces Marko-vian decision problems, is usually referred to as the linear programming solution method , since then the resulting optimization problem is a linear program (see e.g., see Exercise 2.5 for the case of contractive problems or [Ber12a], Ch. 2). 
Suppose now that X = {1, . . . , n}, S = ,n, and J* S is a fixed point of 
T . Then Prop. 3.2.9 shows that J* S = 
! J* S(1), . . . , J 
* S(n) 
" is the unique solu-
tion of the following optimization problem in the vector J = ! J(1), . . . , J(n) 
" : 
maximize n# 
i=1 
&iJ(i) 
subject to J(i) - H(i, u, J), i = 1, . . . , n, u ! U(i), 
where &1, . . . ,&n are any positive scalars. If H is linear in J and each U(i) is a finite set, this is a linear program, which can be solved by using standard linear programming methods. 
† For the mathematical programming approach to apply, it is su"cient that J# S ) TJ# 
S . However, we generally have J# S # TJ# 
S (this follows by writing 
Jµ = TµJµ # TJµ # TJ# S , * µ % MS, 
and taking the infimum over all µ % MS), so the condition J# S ) TJ# 
S is equivalent to J# 
S being a fixed point of T .
Sec. 3.3 Irregular Policies/Infinite Cost Case 165 
3.3 IRREGULAR POLICIES/INFINITE COST CASE 
The results of the preceding section guarantee (under various conditions) that J* 
S is a fixed point of T , and can be found by the VI and PI algorithms, but they do not assert that J* is a fixed point of T or that J* = J* 
S . In this section we address these issues by carrying the strong PI property analysis further with some additional assumptions. A critical part of the analysis is based on the strong PI property theorem of Prop. 3.2.6. We first collect all of our assumptions. We will verify these assumptions in the context of several applications in Section 3.5. 
Assumption 3.3.1: We have a subset S % R(X) satisfying the following: 
(a) S contains J̄ , and has the property that if J1, J2 are two functions in S, then S contains all functions J with J1 - J - J2. 
(b) The function J* S = infµ!MS 
Jµ belongs to S. 
(c) For each S-irregular policy µ and each J ! S, there is at least one state x ! X such that 
lim sup k"# 
(T k µJ)(x) = +. 
(d) The control set U is a metric space, and the set 
& u ! U(x) | H(x, u, J) - ! 
' 
is compact for every J ! S, x ! X , and ! ! ,. 
(e) For each sequence {Jm} % S with Jm 2 J for some J ! S, 
lim m"# 
H(x, u, Jm) = H (x, u, J) , # x ! X, u ! U(x). 
(f) For each function J ! S, there exists a function J $ ! S such that J $ - J and J $ - TJ $. 
An important restriction of the preceding assumption is that S consists of real-valued functions . This underlies the mechanism of di"erentiating between S-regular and S-irregular policies that is embodied in As-sumption 3.3.1(c). 
The conditions (b) and (c) of the preceding assumption have been introduced in Props. 3.2.5 and 3.2.6 in the context of the strong PI propertyrelated analysis. New conditions, not encountered earlier, are (a), (e), and
166 Semicontractive Models Chap. 3 
(f). They will be used to assert that J* = J* S , that J 
* is the unique fixed point of T within S, and that the VI and PI algorithms have improved convergence properties compared with the ones of Section 3.2. 
Note that in the case where S is the set of real-valued functions R(X) and J̄ ! R(X), condition (a) is automatically satisfied, while condition (e) is typically verified easily. The verification of condition (f) may be nontrivial in some cases. We postpone the discussion of this issue for later (see the subsequent Prop. 3.3.2). 
The main result of this section is the following proposition, which provides results that are almost as strong as the ones for contractive models. 
Proposition 3.3.1: Let Assumption 3.3.1 hold. Then: 
(a) The optimal cost function J* is the unique fixed point of T within the set S. 
(b) We have T kJ ' J* for all J ! S. 
(c) A policy µ is optimal if and only if TµJ* = TJ*. Moreover, there exists an optimal policy that is S-regular. 
(d) For any J ! S, if J - TJ we have J - J*, and if J " TJ we have J " J*. 
(e) If in addition for each sequence {Jm} % S with Jm ) J for some J ! S, we have 
H (x, u, J) = lim m"# 
H(x, u, Jm), # x ! X, u ! U(x), 
then every sequence {µk} generated by the PI algorithm starting from an S-regular policy µ0 satisfies Jµk ) J*. Moreover, if the 
set of S-regular policies is finite, there exists k̄ " 0 such that µk̄ 
is optimal. 
We will prove Prop. 3.3.1 through a sequence of lemmas, which delineate the assumptions that are needed for each part of the proof. Our first lemma guarantees that starting from an S-regular policy, the PI algorithm is well defined. 
Lemma 3.3.1: Let Assumption 3.3.1(d) hold. For every J ! S, there exists a policy µ such that TµJ = TJ . 
Proof: For any x ! X with (TJ)(x) < +, let & !m(x) 
' be a decreasing
Sec. 3.3 Irregular Policies/Infinite Cost Case 167 
scalar sequence with 
!m(x) ) inf u!U(x) 
H(x, u, J). 
The set 
Um(x) = & u ! U(x) | H(x, u, J) - !m(x) 
' , 
is nonempty, and by assumption it is compact. The set of points attaining the infimum of H(x, u, J) over U(x) is 3# 
m=0Um(x), and is therefore nonempty. Let ux be a point in this intersection. Then we have 
H(x, ux, J) - !m(x), # m " 0. (3.24) 
Consider now a policy µ, which is formed by the point ux for x with (TJ)(x) < +, and by any point ux ! U(x) for x with (TJ)(x) = +. Taking the limit in Eq. (3.24) asm ' + shows that µ satisfies (TµJ)(x) = (TJ)(x) for x with (TJ)(x) < +. For x with (TJ)(x) = +, we also have trivially (TµJ)(x) = (TJ)(x), so TµJ = TJ . Q.E.D. 
The next two lemmas follow from the analysis of the preceding section. 
Lemma 3.3.2: Let Assumption 3.3.1(c) hold. A policy µ that satisfies TµJ - J for some J ! S is S-regular. 
Proof: This is Prop. 3.2.5(a). Q.E.D. 
Lemma 3.3.3: Let Assumption 3.3.1(b),(c),(d) hold. Then: 
(a) The function J* S of Assumption 3.3.1(b) is the unique fixed point 
of T within S. 
(b) Every policy µ satisfying TµJ* S = TJ* 
S is optimal within the set of S-regular policies, i.e., µ is S-regular and Jµ = J* 
S . Moreover, there exists at least one such policy. 
Proof: This is Prop. 3.2.6(b) [Assumption 3.3.1(d) guarantees that for every J ! S, there exists a policy µ such that TµJ = TJ (cf. Lemma 3.3.1), which is part of the assumptions of Prop. 3.2.6]. Q.E.D. 
Let us also prove the following technical lemma, which makes use of the additional part (e) of Assumption 3.3.1.
168 Semicontractive Models Chap. 3 
Lemma 3.3.4: Let Assumption 3.3.1(b),(c),(d),(e) hold. Then if J ! S, {T kJ} % S, and T kJ 2 J# for some J# ! S, we have J# = J* 
S . 
Proof: We fix x ! X , and consider the sets 
Uk(x) = -u ! U(x) | H(x, u, T kJ) - J#(x) 
. , k = 0, 1, . . . , (3.25) 
which are compact by assumption. Let uk ! U(x) be such that 
H(x, uk, T kJ) = inf u!U(x) 
H(x, u, T kJ) = (T k+1J)(x) - J#(x) 
(such a point exists by Lemma 3.3.1). Then uk ! Uk(x). For every k, consider the sequence {ui}#i=k. Since T 
kJ 2 J#, it follows using the monotonicity of H , that for all i " k, 
H(x, ui, T kJ) - H(x, ui, T iJ) - J#(x). 
Therefore from the definition (3.25), we have {ui}#i=k % Uk(x). Since Uk(x) is compact, all the limit points of {ui}#i=k belong to Uk(x) and at least one limit point exists. Hence the same is true for the limit points of the whole sequence {ui}. Thus if ũ is a limit point of {ui}, we have 
ũ ! 3# k=0Uk(x). 
By Eq. (3.25), this implies that 
H ! x, ũ, T kJ 
" - J#(x), k = 0, 1, . . . . 
Taking the limit as k ' + and using Assumption 3.3.1(e), we obtain 
(TJ#)(x) - H(x, ũ, J#) - J#(x). 
Thus, since x was chosen arbitrarily within X , we have TJ# - J#. To show the reverse inequality, we write T kJ - J#, apply T to this inequality, and take the limit as k ' +, so that J# = limk"# T k+1J - TJ#. It follows that J# = TJ#. Since J# ! S by assumption, by applying Lemma 3.3.3(a) we have J# = J* 
S . Q.E.D. 
We are now ready to prove Prop. 3.3.1 by making use of the additional parts (a) and (f) of Assumption 3.3.1. 
Proof of Prop. 3.3.1: (a), (b) We will first prove that T kJ ' J* S for all 
J ! S, and we will use this to prove that J* S = J* and that there exists
Sec. 3.3 Irregular Policies/Infinite Cost Case 169 
an optimal S-regular policy. Thus parts (a) and (b), together with the existence of an optimal S-regular policy, will be shown simultaneously. 
We fix J ! S, and choose J $ ! S such that J $ - J and J $ - TJ $ 
[cf. Assumption 3.3.1(f)]. By the monotonicity of T , we have T kJ $ 2 J# for some J# ! E(X). Let µ be an S-regular policy such that Jµ = J* 
S [cf. Lemma 3.3.3(b)]. Then we have, using again the monotonicity of T , 
J# = lim k"# 
T kJ $ - lim sup k"# 
T kJ - lim k"# 
T k µJ = Jµ = J* 
S . (3.26) 
Since J $ and J* S belong to S, and J $ - T kJ $ - J# - J* 
S , Assumption 3.3.1(a) implies that {T kJ $} % S, and J# ! S. From Lemma 3.3.4, it then follows that J# = J* 
S . Thus equality holds throughout in Eq. (3.26), proving that limk"# T kJ = J* 
S . There remains to show that J* 
S = J* and that there exists an optimal S-regular policy. To this end, we note that by the monotonicity Assumption 3.2.1, for any policy " = {µ0, µ1, . . .}, we have 
Tµ0 · · ·Tµk!1 J̄ " T kJ̄ . 
Taking the limit of both sides as k ' +, we obtain 
J! " lim k"# 
T kJ̄ = J* S , 
where the equality follows since T kJ ' J* S for all J ! S (as shown earlier), 
and J̄ ! S [cf. Assumption 3.3.1(a)]. Thus for all " ! #, J! " J* S = Jµ, 
implying that the policy µ that is optimal within the class of S-regular policies is optimal over all policies, and that J* 
S = J*. 
(c) If µ is optimal, then Jµ = J* ! S, so by Assumption 3.3.1(c), µ is S-regular and therefore TµJµ = Jµ. Hence, 
TµJ* = TµJµ = Jµ = J* = TJ*. 
Conversely, if J* = TJ* = TµJ*, 
µ is S-regular (cf. Lemma 3.3.2), so J* = limk"# T k µJ* = Jµ. Therefore, 
µ is optimal. 
(d) If J ! S and J - TJ , by repeatedly applying T to both sides and using the monotonicity of T , we obtain J - T kJ for all k. Taking the limit as k ' + and using the fact T kJ ' J* [cf. part (b)], we obtain J - J*. The proof that J " TJ implies J " J* is similar. 
(e) As in the proof of Prop. 3.2.4(b), the sequence {Jµk} converges monotonically to a fixed point of T , call it J#. Since J# lies between Jµ0 ! S 
and J* S ! S, it must belong to S, by Assumption 3.3.1(a). Since the only
170 Semicontractive Models Chap. 3 
fixed point of T within S is J* [cf. part (a)], it follows that J# = J*. Q.E.D. 
Note that Prop. 3.3.1(d) provides the basis for a solution method based on mathematical programming; cf. the discussion following Prop. 3.2.9. Here is an example where Prop. 3.3.1 does not apply, because the compactness condition of Assumption 3.3.1(d) fails. 
Example 3.3.1 
Consider the third variant of the blackmailer problem (Section 3.1.3) for the case where c > 0 and S = (. Then the (nonoptimal) S-irregular policy µ̄ whereby at each period, the blackmailer may demand no payment (u = 0) and pay cost c > 0, has infinite cost (Jµ̄ = "). However, T has multiple fixed points within the real line, namely the set (!",!1]. By choosing S = (, we see that the uniqueness of fixed point part (a) of Prop. 3.3.1 fails because the compactness part (d) of Assumption 3.3.1 is violated (all other parts of the assumption are satisfied). In this example, the results of Prop. 3.2.1 apply with S = (, because J# 
S is a fixed point of T . 
In various applications, the verification of part (f) of Assumption 3.3.1 may not be simple. The following proposition is useful in several contexts, including some that we will encounter in Section 3.5. 
Proposition 3.3.2: Let S be equal to Rb(X), the subset of R(X) that consists of functions J that are bounded above and below, in the sense that for some b ! ,, we have 
//J(x) // - b for all x ! X . Let parts 
(b), (c), and (d) of Assumption 3.3.1 hold, and assume further that for all scalars r > 0, we have 
TJ* S * re - T (J* 
S * re), (3.27) 
where e is the unit function, e(x) $ 1. Then part (f) of Assumption 3.3.1 also holds. 
Proof: Let J ! Rb(x), and let r > 0 be a scalar such that J* S * re - J 
[such a scalar exists since J* S ! Rb(x) by Assumption 3.3.1(b)]. Define 
J $ = J* S * re, and note that by Lemma 3.3.3, J* 
S is a fixed point of T . By using Eq. (3.27), we have 
J $ = J* S * re = TJ* 
S * re - T (J* S * re) = TJ $, 
while J $ ! Rb(x), thus proving part (f) of Assumption 3.3.1. Q.E.D. 
The relation (3.27) is satisfied among others in stochastic optimal control problems (cf. Example 1.2.1), where 
(TJ)(x) = inf u!U(x) 
E & g(x, u, w) + #J 
! f(x, u, w) 
"' , x ! X,
Sec. 3.4 Irregular Policies/Finite Cost Case - A Perturbation Approach 171 
with # ! (0, 1]. Note that application of the preceding proposition is facilitated when X is a finite set, in which case Rb(X) = R(X). This fact will be used in the context of some of the applications of Sections 3.5.1-3.5.4. 
3.4 IRREGULAR POLICIES/FINITE COST CASE -A PERTURBATION APPROACH 
In this section, we address problems where some S-irregular policies may have finite cost for all states [thus violating Assumption 3.3.1(c)], so Prop. 3.3.1 cannot be used. Our approach instead will be to assert that J* 
S is a fixed point of T , so that Prop. 3.2.1 applies and can be used to guarantee convergence of VI to J* 
S starting from J0 " J* S . 
Our line of analysis is quite di"erent from the one of Sections 3.2.3 and 3.3, which was based on PI ideas. Instead, we add a perturbation to the mapping H , designed to provide adequate di"erentiation between S-regular and S-irregular policies. Using a limiting argument, as the size of the perturbation diminishes to 0, we are able to prove that J* 
S is a fixed point of T . Moreover, we provide a perturbation-based PI algorithm that may be more reliable than the standard PI algorithm, which can fail for problems where irregular policies may have finite cost for all states; cf. Example 3.2.2. We will also use the perturbation approach in Sections 4.5 and 4.6, where we will extend the notion of S-regularity to nonstationary policies that do not lend themselves to a PI-based analysis. 
An example where the approach of this section will be shown to apply is an SSP problem where Assumption 3.3.1 is violated while J*(x) > *+ for all x (see also Section 3.5.1). Here is a classical problem of this type. 
Example 3.4.1 (Search Problem) 
Consider a situation where the objective is to move within a finite set of states searching for a state to stop while minimizing the expected cost. We formulate this as a DP problem with finite state space X, and two controls at each x % X: stop, which yields an immediate cost s(x), and continue, in which case we move to a state f(x,w) at cost g(x,w), where w is a random variable with given distribution that may depend on x. The mapping H is 
H(x, u, J) = 
$ s(x) if u = stop, 
E & g(x,w) + J 
! f(x,w) 
"' if u = continue, 
and the function J̄ is identically 0. Letting S = R(X), we note that the policy µ that stops nowhere is 
S-irregular, since Tµ cannot have a unique fixed point within S (adding any unit function multiple to J adds to TµJ the same multiple). This policy may violate Assumption 3.3.1(c) of the preceding section, because its cost may be
172 Semicontractive Models Chap. 3 
finite for all states. A special case where this occurs is when g(x,w) ' 0 for all x. Then the cost function of µ is identically 0. 
Note that case (b) of the deterministic shortest path problem of Sec-tion 3.1.1, which involves a zero length cycle, is a special case of the search problem just described. Therefore, the anomalous behavior we saw there (nonconvergence of VI to J# and oscillation of PI; cf. Examples 3.2.1 and 3.2.2) may also arise in the context of the present example. We will see that by adding a small positive constant to the length of the cycle we can rectify the di"culties of VI and PI, at least partially; this is the idea behind the perturbation approach that we will use in this section. 
We will address the finite cost issue for irregular policies by introducing a perturbation that makes their cost infinite for some states. We can then use Prop. 3.3.1 of the preceding section. The idea is that with a perturbation, the cost functions of S-irregular policies may increase disproportionately relative to the cost functions of the S-regular policies, thereby making the problem more amenable to analysis. 
We introduce a nonnegative “forcing function” p : X &' [0,+), and for each % > 0 and policy µ, we consider the mappings 
(Tµ,"J)(x) = H ! x, µ(x), J 
" + %p(x), x ! X, T"J = inf 
µ!M Tµ,"J. 
We refer to the problem associated with the mappings Tµ," as the %-perturbed problem. The cost functions of policies " = {µ0, µ1, . . .} ! # and µ ! M for this problem are 
J!," = lim sup k"# 
Tµ0," · · ·Tµk,"J̄ , Jµ," = lim sup k"# 
T k µ,"J̄ , 
and the optimal cost function is Ĵ" = inf!!! J!,". The following proposition shows that if the %-perturbed problem is 
“well-behaved” with respect to a subset of S-regular policies, then its cost function Ĵ" can be used to approximate the optimal cost function over this subset of policies only. Moreover J* 
S is a fixed point of T . Note that the unperturbed problem need not be as well-behaved, and indeed J* need not be a fixed point of T . 
Proposition 3.4.1: Given a set S % E(X), let +M be a subset of S-regular policies, and let Ĵ be the optimal cost function over the policies in +M only, i.e., 
Ĵ = inf µ! 0M 
Jµ. 
Assume that for every % > 0: 
(1) The optimal cost function Ĵ" of the %-perturbed problem satisfies the corresponding Bellman equation Ĵ" = T"Ĵ".
Sec. 3.4 Irregular Policies/Finite Cost Case - A Perturbation Approach 173 
(2) We have inf µ! 0M Jµ," = Ĵ", i.e., for every x ! X and ' > 0, there 
exists a policy µx,$ ! +M such that Jµx,","(x) - Ĵ"(x) + '. 
(3) For every µ ! +M, we have 
Jµ," - Jµ + wµ,", 
where wµ," is a function such that lim")0 wµ," = 0. 
(4) For every sequence {Jm} % S with Jm ) J , we have 
lim m"# 
H(x, u, Jm) = H(x, u, J), # x ! X, u ! U(x). 
Then J* S is a fixed point of T and the conclusions of Prop. 3.2.1 hold. 
Moreover, we have J* S = Ĵ = lim 
")0 Ĵ". 
Proof: For every x ! X , using conditions (2) and (3), we have for all 
% > 0, ' > 0, and µ ! +M, 
Ĵ(x)*' - Jµx,"(x)*' - Jµx,","(x)*' - Ĵ"(x) - Jµ,"(x) - Jµ(x)+wµ,"(x). 
By taking the limit as ' ) 0, we obtain for all % > 0 and µ ! +M, 
Ĵ - Ĵ" - Jµ," - Jµ + wµ,". 
By taking the limit as % ) 0 and then the infimum over all µ ! +M, it follows [using also condition (3)] that 
Ĵ - lim ")0 
Ĵ" - inf µ! 0M 
lim ")0 
Jµ," - inf µ! 0M 
Jµ = Ĵ , 
so that Ĵ = lim")0 Ĵ". Next we prove that Ĵ is a fixed point of T and use this fact to show 
that Ĵ = J* S , thereby concluding the proof. Indeed, from condition (1) and 
the fact Ĵ" " Ĵ shown earlier, we have for all % > 0, 
Ĵ" = T"Ĵ" " T Ĵ" " T Ĵ, 
and by taking the limit as % ) 0 and using part (a), we obtain Ĵ " T Ĵ. For the reverse inequality, let {%m} be a sequence with %m ) 0. Using condition (1) we have for all m, 
H(x, u, Ĵ"m) + %mp(x) " (T"m Ĵ"m)(x) = Ĵ"m(x), # x ! X, u ! U(x).
174 Semicontractive Models Chap. 3 
Taking the limit as m ' +, and using condition (4) and the fact Ĵ"m ) Ĵ shown earlier, we have 
H(x, u, Ĵ) " Ĵ(x), # x ! X, u ! U(x), 
so that T Ĵ " Ĵ . Thus Ĵ is a fixed point of T . Finally, to show that Ĵ = J* 
S , we first note that J* S - Ĵ since every 
policy in +M is S-regular. For the reverse inequality, let µ be S-regular. We have Ĵ = T Ĵ - TµĴ - T k 
µ Ĵ for all k " 1, so that for all µ$ ! +M, 
Ĵ - lim k"# 
T k µ Ĵ - lim 
k"# T k µJµ" = Jµ, 
where the equality follows since µ and µ$ are S-regular (so Jµ" ! S). Taking 
the infimum over all S-regular µ, we obtain Ĵ - J* S , so that J* 
S = Ĵ . Q.E.D. 
Aside from S-regularity of the set +M, a key assumption of the preceding proposition is that inf 
µ! 0M Jµ," = Ĵ", i.e., that with a perturbation 
added, the subset of policies +M is su!cient (the optimal cost of the %-
perturbed problem can be achieved using the policies in +M). This is the 
key insight to apply when selecting +M. Note that the preceding proposition applies even if 
lim ")0 
Ĵ"(x) > J*(x) 
for some x ! X . This is illustrated by the deterministic shortest path example of Section 3.1.1, for the zero-cycle case where a = 0 and b > 0. Then for S = ,, we have J* 
S = b > 0 = J*, while the proposition applies because its assumptions are satisfied with p(x) $ 1. Consistently with the conclusions of the proposition, we have Ĵ" = b + %, so J* 
S = Ĵ = lim")0 Ĵ" and J* 
S is a fixed point of T . Proposition 3.4.1 also applies to Example 3.4.1. In particular, it can 
be used to assert that J* S is a fixed point of T , and hence also that the 
conclusions of Prop. 3.2.1 hold. These conclusions imply that J* S is the 
unique fixed point of T within the set {J | J " J* S} and that the VI 
algorithm converges to J* S starting from within this set. 
We finally note that while Props. 3.3.1 and 3.4.1 relate to qualitatively di"erent problems, they can often be used synergistically. In particular, Prop. 3.3.1 may be applied to the %-perturbed problem in order to verify the assumptions of Prop. 3.4.1. 
A Policy Iteration Algorithm with Perturbations 
We now consider a subset +M of S-regular policies, and introduce a version of the PI algorithm that uses perturbations and generates a sequence {µk} % +M such that Jµk ' J* 
S . We assume the following.
Sec. 3.4 Irregular Policies/Finite Cost Case - A Perturbation Approach 175 
Assumption 3.4.1: The subset of S-regular policies +M is such that: 
(a) The conditions of Prop. 3.4.1 are satisfied. 
(b) Every policy µ ! +M is S-regular for all the %-perturbed problems, % > 0. 
(c) Given a policy µ ! +M and a scalar % > 0, every policy µ$ such that 
Tµ"Jµ," = TJµ," 
belongs to +M, and at least one such policy exists. 
The perturbed version of the PI algorithm is defined as follows. Let {%k} be a positive sequence with %k ) 0, and let µ0 be a policy in +M. At 
iteration k, we have a policy µk ! +M, and we generate µk+1 ! +M according to 
Tµk+1Jµk,"k = TJµk,"k 
. (3.28) 
Note that by Assumption 3.4.1(c) the algorithm is well-defined, and is 
guaranteed to generate a sequence of policies {µk} % +M. We have the following proposition. 
Proposition 3.4.2: Let Assumption 3.4.1 hold. Then J* S is a fixed 
point of T and for a sequence of S-regular policies {µk} generated by the perturbed PI algorithm (3.28), we have Jµk ,"k 
) J* S and Jµk ' J* 
S . 
Proof: We have that J* S is a fixed point of T by Prop. 3.4.1. The algorithm 
definition (3.28) implies that for all m " 1 we have 
Tm µk+1,"k 
Jµk,"k - Tµk+1,"k 
Jµk ,"k = TJµk,"k 
+ %k p - Jµk,"k . 
From this relation it follows that 
Jµk+1,"k+1 - Jµk+1,"k 
= lim m"# 
Tm µk+1,"k 
Jµk ,"k - Jµk ,"k 
, 
where the equality holds because µk+1 and µk are S-regular for all the %-perturbed problems. It follows that {Jµk,"k 
} is monotonically nonincreas-
ing, so that Jµk,"k ) J# for some J#. Moreover, we must have J# " J* 
S 
since Jµk ,"k " Jµk " J* 
S . Thus 
J* S - J# = lim 
k"# TJµk,"k 
. (3.29)
176 Semicontractive Models Chap. 3 
We also have 
inf u!U(x) 
H(x, u, J#) - lim k"# 
inf u!U(x) 
H ! x, u, Jµk,"k 
" 
- inf u!U(x) 
lim k"# 
H ! x, u, Jµk,"k 
" 
= inf u!U(x) 
H ! x, u, lim 
k"# Jµk ,"k 
" 
= inf u!U(x) 
H(x, u, J#), 
where the first inequality follows from the fact J# - Jµk ,"k , which implies 
that H(x, u, J#) - H ! x, u, Jµk,"k 
" , and the first equality follows from the 
continuity property that is assumed in Prop. 3.4.1. Thus equality holds throughout above, so that 
lim k"# 
TJµk,"k = TJ#. (3.30) 
Combining Eqs. (3.29) and (3.30), we obtain J* S - J# = TJ#. By re-
placing Ĵ with J# in the last part of the proof of Prop. 3.4.1, we obtain J* S = J#. Thus Jµk ,"k 
) J* S , which in view of the fact Jµk,"k 
" Jµk " J* S , 
implies that Jµk ' J* S . Q.E.D. 
When the control space U is finite, Prop. 3.4.2 also implies that the generated policies µk will be optimal for all k su!ciently large. The reason is that the set of policies is finite and there exists a su!ciently small ' > 0, such that for all nonoptimal µ there is some state x such that Jµ(x) " Ĵ(x)+'. This convergence behavior should be contrasted with the behavior of PI without perturbations, which may lead to oscillations, as noted earlier. 
However, when the control space U is infinite, the generated sequence {µk} may exhibit some serious pathologies in the limit. If {µk}K is a subsequence of policies that converges to some µ̄, in the sense that 
lim k"#, k!K 
µk(x) = µ̄(x), # x = 1, . . . , n, 
it does not follow that µ̄ is S-regular. In fact it is possible that the generated sequence of S-regular policies {µk} satisfies limk"# Jµk ' J* 
S = J*, yet {µk} may converge to an S-irregular policy whose cost function is strictly larger than J* 
S , as illustrated by the following example. 
Example 3.4.2 
Consider the third variant of the blackmailer problem (Section 3.1.3) for the case where c = 0 (the blackmailer may forgo demanding a payment at cost c = 0); see Fig. 3.4.1. Here the mapping T is given by 
TJ = min 
( J, inf 
0<u&1 
& ! u+ u2 + (1! u)J 
'* ,
Sec. 3.5 Applications in Shortest Path and Other Contexts 177 
a 1 2 1 2 t b 
u Destination 
1] Cost !u 
Prob. u 
u Prob. 1! u 
u Control u ! [0, 1] Cost 
u Cost 0 Destination 
Figure 3.4.1. Transition diagram for a blackmailer problem (the third variant of Section 3.1.3 in the case where c = 0). At state 1, the blackmailer may demand any amount u ! [0, 1]. The victim will comply with probability 1 " u and will not comply with probability u, in which case the process will terminate. 
[cf. Eq. (3.4)], and can be written as 
TJ = min 0&u&1 
& ! u+ u2 + (1! u)J 
' . 
Letting S = (, it can be seen that the set of fixed points of T within S is (!",!1]. Here the policy whereby the blackmailer demands no payment (u = 0) and pays no cost at each period, is S-irregular and strictly suboptimal, yet has finite (zero) cost, so part (c) of Assumption 3.3.1 is violated (all other parts of the assumption are satisfied). 
It can be seen that 
J# = J# S = !1, 
J# S is a fixed point of T , Prop. 3.2.1 applies, and VI converges to J# starting 
from any J # J#. Moreover, starting from any policy (including the S-irregular one that applies u = 0), the PI algorithm (3.28) generates a sequence of S-regular policies {µk} with Jµk $ J# 
S. However, {µk} converges to the S-irregular and strictly suboptimal policy that applies u = 0. 
Here a phenomenon of “oscillation in the limit” is observed: starting with the S-irregular policy that applies u = 0, we generate a sequence of S-regular policies that converges to the S-irregular policy we started from! The perturbation-based PI algorithm of this section cannot rectify this type of behavior; it can only guarantee that a sequence of S-regular policies with Jµk $ J# 
S is generated. 
3.5 APPLICATIONS IN SHORTEST PATH AND OTHER CONTEXTS 
In this section we will apply the results of the preceding sections to various problems with a semicontractive character, including shortest path and deterministic optimal control problems of various types.
178 Semicontractive Models Chap. 3 
As we are about to apply the theory developed so far in this chapter, it may be helpful to summarize our results. Given a suitable set of functions S, we have been dealing with two problems. These are the original problem whose optimal cost function is J*, and the restricted problem whose optimal cost function is J* 
S , the optimal cost over the S-regular policies. In summary, the aims of our analysis have been the following: 
(a) To establish the fixed point properties of T . We have showed under various conditions (cf. Prop. 3.2.1) that J* 
S is the unique fixed point of T within the well-behaved region WS , and moreover the VI algorithm converges from above to J* 
S . Related analyses involve the use of infinite cost assumptions for S-irregular policies (Section 3.3), possibly in conjunction with the use of perturbations (Section 3.4). A favorable case is when J* 
S = J*. However, we may also have J* S (= J*. 
Generally, proving that J* is a fixed point of T is a separate issue, which may either be addressed in conjunction with the analysis of properties of J* 
S as in Section 3.3 (cf. Prop. 3.3.1), or independently of J* 
S (for example J* is generically a fixed point of T in deterministic problems, among other classes of problems; see Exercise 3.1). 
(b) To delineate the initial conditions under which the VI and PI algorithms are guaranteed to converge to J* 
S or to J*. This was done in conjunction with the analysis of the fixed point properties of T . For example, a major line of analysis for establishing that J* 
S is a fixed point of T is based on the PI algorithm (cf. Sections 3.2.3 and 3.3). We have also obtained several other results relating to the convergence of variants of PI (the optimistic version, cf. Prop. 3.2.7, the !-PI version, cf. Prop. 3.2.8, and the perturbation-based version, cf. Prop. 3.4.2), and to the mathematical programming-based solution, cf. Section 3.2.5. 
(c) To establish the existence of optimal policies for the original or for the restricted problem, and the associated optimality conditions . This was accomplished in conjunction with the analysis of the fixed points of T , and under special compactness-like conditions (cf. Props. 3.2.1, 3.2.6, and 3.3.1). 
As we apply our analysis to various specific contexts in this section, we will make frequent reference to the pathological behavior that we witnessed in the examples of Section 3.1. In particular, we will explain this behavior through our theoretical results, and we will discuss how to preclude this behavior through appropriate assumptions. 
3.5.1 Stochastic Shortest Path Problems 
Let us consider the SSP problem that we discussed in Section 1.3.2. It involves a directed graph with nodes x = 1, . . . , n, plus a destination node
Sec. 3.5 Applications in Shortest Path and Other Contexts 179 
t that is cost-free and absorbing. At each node x, we must select a control u ! U(x), which defines a probability distribution pxy(u) over all possible successor nodes y = 1, . . . , n, t, while a cost g(x, u) is incurred. We wish to minimize the expected cost of the traversed path, with cost accumulated up to reaching the destination. 
Note that if for every feasible control the corresponding probability distribution assigns probability 1 to a single successor node, we obtain the deterministic shortest path problem of Section 3.1.1. This problem admits a relatively simple analysis, yet exhibits pathological behavior that we have described. The pathologies exhibited by SSP problems are more severe, and were illustrated in Sections 3.1.2 and 3.1.3. 
We formulate the SSP problem as an abstract DP problem where: 
(a) The state space is X = {1, . . . , n} and the control constraint set is U(x) for all x ! X . (For technical reasons, it is convenient to exclude from X the destination t; we know that the optimal cost starting from t is 0, and including t within X would just complicate the notation and the analysis, with no tangible benefit.) 
(b) The mapping H is given by 
H(x, u, J) = g(x, u) + n# 
y=1 
pxy(u)J(y), x = 1, . . . , n. 
(c) The function J̄ is identically 0, J̄(x) = 0 for all x. 
We continue to denote by E(X) the set of all extended real-valued functions J : X &' ,', and by R(X) the set of real-valued functions J : X &' ,. Note that since X = {1, . . . , n}, R(X) is essentially the n-dimensional space Rn. 
Here the mapping Tµ corresponding to a policy µ maps R(X) to R(X), and is given by 
(TµJ)(x) = g ! x, µ(x) 
" + 
n# 
y=1 
pxy ! µ(x) 
" J(y), x = 1, . . . , n. 
The corresponding cost for a given initial state x0 ! {1, . . . , n} is 
Jµ(x0) = lim sup k"# 
(T k µ J̄)(x0) = lim sup 
k"# 
k%1# 
m=0 
E -g ! xm, µ(xm) 
". , 
where {xm} is the (random) state trajectory generated under policy µ, starting from initial state x0. The expected value E 
& g(xm, µ(xm)) 
' above 
is defined in the natural way: it is the weighted sum of the numerical values g ! x, µ(x) 
" , x = 1, . . . , n, weighted by the probabilities p(xm = x | x0, µ)
180 Semicontractive Models Chap. 3 
that xm = x given that the initial state is x0 and policy µ is used. Thus Jµ(x0) is the upper limit as k ' + of the cost for the first k steps or up to reaching the destination, whichever comes first. 
A stationary policy µ is said to be proper if for every initial state there is positive probability that the destination will be reached under that policy after at most n stages. A stationary policy that is not proper is said to be improper . The relation between proper policies and S-regularity is given in the following proposition. 
Proposition 3.5.1: (Proper Policies and Regularity) A policy is proper if and only if it is R(X)-regular. 
Proof: Clearly µ is R(X)-regular if and only if the n/n matrix Pµ, whose components are pxy 
! µ(x) 
" , x, y = 1, . . . , n, is a contraction (since Tµ is a 
linear mapping with matrix Pµ). If µ is proper then Pµ is a contraction mapping with respect to some weighted sup-norm; this is a classical result, given for example in [BeT89], Section 4.2. Conversely, it can be seen that if µ is improper, Pµ is not a contraction mapping since the Markov chain corresponding to µ has multiple ergodic classes and hence the equilibrium equation ($ = ($Pµ has multiple solutions. Q.E.D. 
Looking back to the shortest path examples of Sections 3.1.1-3.1.3, we can make some observations. In deterministic shortest path problems, µ(x) can be identified with the single successor node of node x. Thus µ is proper if and only if the corresponding graph of arcs 
! x, µ(x) 
" is acyclic. 
Moreover, there exists a proper policy if and only if each node is connected to the destination with a sequence of arcs. Every improper policy involves at least one cycle. Depending on the sign of the length of their cycle(s), improper policies can be strictly suboptimal (if all cycles have positive length), or may be optimal (possibly together with some proper policies, if all cycles have nonnegative length). Moreover, if there are cycles with negative length, no proper policy can be optimal and for the states x that lie on some negative length cycle we have J*(x) = *+. 
A further characterization of the optimal solution is possible in deterministic shortest path problems. Since the sets U(x) are finite, there exists an optimal policy, which can be separated into a “proper” part consisting of arcs that form an acyclic subgraph, and an “improper” part consisting of cycles that have negative or zero length. These facts can be proved with simple arguments, which will not be given here (deterministic shortest path theory and algorithms are developed in detail in the author’s text [Ber98]). 
In SSP problems, the situation is more complicated. In particular, the cost function of an improper policy µ may not be a fixed point of Tµ while J* may not be a fixed point of T (cf. the example of Section
Sec. 3.5 Applications in Shortest Path and Other Contexts 181 
3.1.2). Moreover, there may not exist an optimal stationary policy even if all policies are proper (cf. the three variants of the blackmailer example of Section 3.1.3). 
In this section we will use various assumptions, which we will in turn translate into the conditions and corresponding results of Sections 3.2-3.4. Throughout this section we will assume the following. 
Assumption 3.5.1: There exists at least one proper policy. 
Depending on the circumstances, we will also consider the use of one or both of the following assumptions. 
Assumption 3.5.2: The control space U is a metric space. Moreover, for each state x, the set U(x) is a compact subset of U , the functions pxy(·), y = 1, . . . , n, are continuous over U(x), and the function g(x, ·) is lower semicontinuous over U(x). 
Assumption 3.5.3: For every improper policy µ and function J ! R(X), there exists at least one state x ! X such that Jµ(x) = +. 
An important consequence of Assumption 3.5.2 is that it implies the compactness condition (d) of Assumption 3.3.1. We will also see from the proof of the following proposition that Assumption 3.5.3 implies the infinite cost condition (c) of Assumption 3.3.1. 
Analysis Under the Strong SSP Conditions 
The preceding three assumptions, referred to as the strong SSP conditions , † were introduced in the paper [BeT91], and they were used to show strong results for the SSP problem. In particular, the following proposition was shown. 
Proposition 3.5.2: Let the strong SSP conditions hold. Then: 
(a) The optimal cost function J* is the unique solution of Bellman’s equation J = TJ within R(X). 
† The strong SSP conditions and the weak SSP conditions, which will be introduced shortly, relate to the strong and weak PI properties of Section 3.2.
182 Semicontractive Models Chap. 3 
(b) The VI sequence {T kJ} converges to J* starting from any J ! R(X). 
(c) A policy µ is optimal if and only if TµJ* = TJ*. Moreover, there exists an optimal policy that is proper. 
(d) The PI algorithm, starting from any proper policy, is valid in the sense described by the conclusions of Prop. 3.3.1(e). 
We will prove the proposition by using the strong SSP conditions to verify Assumption 3.3.1 for S = R(X), and then by applying Prop. 3.3.1. To this end, we first state without proof the following result relating to proper policies from [BeT91]. 
Proposition 3.5.3: Under the strong SSP conditions, the optimal cost function Ĵ over proper policies only, 
Ĵ(x) = inf µ: proper 
Jµ(x), x ! X, 
is real-valued. 
The preceding proposition holds trivially if the control space U is finite (since then the set of all policies is finite), or if J* is somehow known to be real-valued [for example if g(x, u) " 0 for all (x, u)]. The three variants of the blackmailer problem of Section 3.1.3 provide examples illustrating what can happen if U is infinite. In particular, in the first variant of the blackmailer problem all policies are proper (and hence Assumptions 3.5.1 and 3.5.3 are satisfied), but Ĵ is not real-valued. The proof of Prop. 3.5.3 in the case of an infinite control space U was given as part of Prop. 2 of the paper [BeT91]. Despite the intuitive nature of Prop. 3.5.3, the proof embodies a fairly complicated argument (see Lemma 3 of [BeT91]). 
Another related result is that if all policies are proper, then for all µ ! M, Tµ is a contraction mapping with respect to a common weighted sup-norm, so the contractive model analysis and algorithms of Chapter 2 apply (see [BeT96], Prop. 2.2). However, this fact will not be useful to us in this section. 
Proof of Prop. 3.5.2: In the context of Section 3.3, let us choose S = R(X), so the proper policies are identified with the S-regular policies by Prop. 3.5.1. We will verify Assumption 3.3.1. 
Indeed parts (a) and (e) are trivially satisfied, part (b) is satisfied by Prop. 3.5.3, part (d) can be easily verified by using Assumption 3.5.2. To verify part (f), we use Prop. 3.3.2, which applies because S = R(X) =
Sec. 3.5 Applications in Shortest Path and Other Contexts 183 
Rb(X) (since X is finite) and Eq. (3.27) clearly holds. Finally, to verify part (c) we must show that given an improper policy µ, for every J ! R(X) there exists an x ! X such that lim supk"#(T k 
µJ)(x) = +. This follows since by Assumption 3.5.3, Jµ(x) = lim supk"#(T k 
µ J̄)(x) = +, for some x ! X , and (T k 
µJ)(x) and (T k µ J̄)(x) di"er by E 
& J(xk) 
' , an amount that is finite 
since J is real-valued and has a finite number of components J(x). Thus Assumption 3.3.1 holds and the result follows from Prop. 3.3.1. Q.E.D. 
Analysis Under the Weak SSP Conditions 
Under the strong SSP conditions, we showed in Prop. 3.5.2 that J* is the unique fixed point of T within R(X). Moreover, we showed that a policy µ' 
is optimal if and only if Tµ#J* = TJ*, and an optimal proper policy exists (so in particular J*, being the cost function of a proper policy, is realvalued). In addition, J* can be computed by the VI algorithm starting with any J ! ,n. 
We will now replace Assumption 3.5.3 (improper policies have cost + for some initial states) with the following weaker assumption: 
Assumption 3.5.4: The optimal cost function J* is real-valued. 
We will refer to the Assumptions 3.5.1, 3.5.2, and 3.5.4 as the weak SSP conditions . The examples of Sections 3.1.1 and 3.1.2 show that under these assumptions, it is possible that 
J* (= Ĵ = inf µ: proper 
Jµ, 
while J* need not be a fixed point of T (Section 3.1.2). The key fact is that under Assumption 3.5.4, we can use the perturbation approach of Section 3.4, whereby adding % > 0 to the mapping Tµ makes all improper policies have infinite cost for some initial states, so the results of Prop. 3.5.2 can be used for the %-perturbed problem. In particular, Prop. 3.5.1 implies that J* S = Ĵ , so from Prop. 3.4.1 it follows that Ĵ is a fixed point of T and the 
conclusions of Prop. 3.2.1 hold. We thus obtain the following proposition, which provides additional results, not implied by Prop. 3.2.1; see Fig. 3.5.1. 
Proposition 3.5.4: Let the weak SSP conditions hold. Then: 
(a) The optimal cost function over proper policies, Ĵ , is the largest solution of Bellman’s equation J = TJ within R(X), i.e., Ĵ is a solution that belongs to R(X), and if J $ ! R(X) is another solution, we have J $ - Ĵ .
184 Semicontractive Models Chap. 3 
Paths of VI Unique solution of Bellman’s equation 
Fixed Points of T 
S = !2 
2 Ĵ JĴ : Largest fixed point of T J 
Figure 3.5.1. Schematic illustration of Prop. 3.5.4 for a problem with two states, so R(X) = $2 = S. We have that Ĵ is the largest solution of Bellman’s equation, while VI converges to Ĵ starting from J & Ĵ . As shown in Section 3.1.2, J# need not be a solution of Bellman’s equation. 
(b) The VI sequence {T kJ} converges linearly to Ĵ starting from any J ! R(X) with J " Ĵ . 
(c) Let µ be a proper policy. Then µ is optimal within the class of proper policies (i.e., Jµ = Ĵ) if and only if TµĴ = T Ĵ . 
(d) For every J ! R(X) such that J - TJ , we have J - Ĵ . 
Proof: (a), (b) Let S = R(X), so the proper policies are identified with the S-regular policies by Prop. 3.5.1. We use the perturbation framework of Section 3.4 with forcing function p(x) $ 1. From Prop. 3.5.2 it follows that Prop. 3.4.1 applies so that Ĵ is a fixed point of T , and the conclusions of Prop. 3.2.1 hold, so T kJ ' Ĵ starting from any J ! R(X) with J " Ĵ . The convergence rate of VI is linear in view of Prop. 3.2.2 and the existence of an optimal proper policy to be shown in part (c). Finally, let J $ ! R(X) be another solution of Bellman’s equation, and let J ! R(X) be such that J " Ĵ and J " J $. Then T kJ ' Ĵ , while T kJ " T kJ $ = J $. It follows that Ĵ " J $. 
(c) If the proper policy µ satisfies Jµ = Ĵ , we have Ĵ = Jµ = TµJµ = TµĴ , so, using also the relation Ĵ = T Ĵ [cf. part (a)], we obtain TµĴ = T Ĵ . Conversely, if µ satisfies TµĴ = T Ĵ , then using part (a), we have TµĴ = Ĵ and hence limk"# T k 
µ Ĵ = Ĵ . Since µ is proper, we have Jµ = limk"# T k µ Ĵ , 
so Jµ = Ĵ . 
(d) Let J - TJ and % > 0. We have J - TJ + %e = T"J , and hence J - T k 
" J for all k. Since the strong SSP conditions hold for the %-perturbed
Sec. 3.5 Applications in Shortest Path and Other Contexts 185 
problem, it follows that T k " J ' Ĵ", so J - Ĵ". By taking % ) 0 and using 
Prop. 3.4.1, it follows that J - Ĵ . Q.E.D. 
The first variant of the blackmailer Example 3.4.2 shows that under the weak SSP conditions there may not exist an optimal policy or an optimal policy within the class of proper policies if the control space is infinite. This is consistent with Prop. 3.5.4(c). Another interesting fact is provided by the third variant of this example in the case where c < 0. Then J*(1) = *+ (violating Assumption 3.5.4), but Ĵ is real-valued and does not solve Bellman’s equation, contrary to the conclusion of Prop. 3.5.4(a). 
Part (d) of Prop. 3.5.4 shows that Ĵ is the unique solution of the problem of maximizing 
)n i=1 &iJ(i) over all J = 
! J(1), . . . , J(n) 
" such 
that J - TJ , where &1, . . . ,&n are any positive scalars (cf. Prop. 3.2.9). This problem can be written as 
maximize n# 
i=1 
J(i) 
subject to J(x) - g(x, u) + n# 
y=1 
pij(u)J(j), i = 1, . . . , n, u ! U(i), 
and is a linear program if each U(i) is a finite set. Generally, under the weak SSP conditions the strong PI property may 
not hold, so a sequence generated by PI starting from a proper policy need not have the cost improvement property. An example is the deterministic shortest path problem of Section 3.1.1, when there is a zero length cycle (a = 0) and the only optimal policy is proper (b = 0). Then the PI algorithm may oscillate between the optimal proper policy and the strictly suboptimal improper policy. We will next consider the modified version of the PI algorithm that is based on the use of perturbations (Section 3.4). 
Policy Iteration with Perturbations 
To deal with the oscillatory behavior of PI, which was illustrated in the deterministic shortest path Example 3.2.2, we may use the perturbed version of the PI algorithm of Section 3.4, with forcing function p(x) $ 1. Thus, we have 
(Tµ,"J)(x) = H ! x, µ(x), J 
" + %, x ! X, T"J = inf 
µ!M Tµ,"J. 
The algorithm generates the sequence {µk} as follows. Let {%k} be a positive sequence with %k ) 0, and let µ0 be any proper 
policy. At iteration k, we have a proper policy µk, and we generate µk+1 
according to Tµk+1Jµk,"k 
= TJµk,"k , (3.31)
186 Semicontractive Models Chap. 3 
where Jµk,"k is computed as the unique fixed point of the mapping Tµk,"k 
given by Tµk,"k 
J = TµkJ + %ke. 
The policy µk+1 of Eq. (3.31) exists by the compactness Assumption 3.5.2. We claim that µk+1 is proper. To see this, note that 
Tµk+1,"k Jµk,"k 
= TJµk,"k + %k e - TµkJµk,"k 
+ %k e = Jµk,"k , 
so that by the monotonicity of T k+1 µ , 
Tm µk+1,"k 
Jµk ,"k - Tµk+1,"k 
Jµk,"k = TJµk,"k 
+ %k e - Jµk ,"k , # m " 1. 
Since Jµk ,"k forms an upper bound to Tm 
µk+1,"k Jµk ,"k 
, it follows that µk+1 
is proper [if it were improper, we would have (Tm µk+1,"k 
Jµk ,"k )(x) ' + for 
some x, because of the perturbation %k]. Thus the sequence {µk} generated by the perturbed PI algorithm (3.31) is well-defined and consists of proper policies. We have the following proposition. 
Proposition 3.5.5: Let the weak SSP conditions hold. Then the sequence {Jµk} generated by the perturbed PI algorithm (3.31) satisfies 
Jµk ' Ĵ . 
Proof: We apply the perturbation framework of Section 3.4 with S = R(X), +M equal to the set of proper policies, and the forcing function p(x) $ 1. Clearly Assumption 3.4.1 holds, so Prop. 3.4.2 applies. Q.E.D. 
When the control space U is finite, the generated policies µk will be optimal for all k su!ciently large, as noted following Prop. 3.4.2. However, when the control space U is infinite, the generated sequence {µk} may exhibit some serious pathologies in the limit, as we have seen in Example 3.4.2. 
3.5.2 A!ne Monotonic Problems 
In this section, we consider a class of semicontractive models, called a!ne monotonic, where the abstract mapping Tµ associated with a stationary policy µ is a!ne and maps nonnegative functions to nonnegative functions. These models include as special cases stochastic undiscounted nonnegative cost problems, and multiplicative cost problems, such as risk-averse problems with exponentiated additive cost and a termination state (see Example 1.2.8). Here we will focus on the special case where the state space is finite and a certain compactness condition holds.
Sec. 3.5 Applications in Shortest Path and Other Contexts 187 
We consider a finite state space X = {1, . . . , n} and a (possibly infinite) control constraint set U(x) for each state x. For each µ ! M the mapping Tµ is given by 
TµJ = bµ +AµJ, 
where bµ is a vector of ,n with components b ! x, µ(x) 
" , x = 1, . . . , n, and 
Aµ is an n/ n matrix with scalar components Axy 
! µ(x) 
" , x, y = 1, . . . , n. 
We assume that b(x, u) and Axy(u) are nonnegative, 
b(x, u) " 0, Axy(u) " 0, # x, y = 1, . . . , n, u ! U(x). 
Thus Tµ maps E+(X) into E+(X), where E+(X) denotes the set of nonnegative extended real-valued functions J : X &' [0,+]. Moreover Tµ 
also maps R+(X) to R+(X), where R+(X) denotes the set of nonnegative real-valued functions J : X &' [0,+). 
The mapping T : E+(X) &' E+(X) is given by 
(TJ)(x) = inf µ!M 
(TµJ)(x), x ! X, 
or equivalently, 
(TJ)(x) = inf u!U(x) 
1 b(x, u) + 
n# 
y=1 
Axy(u)J(y) 
2 , x ! X. 
Multiplicative and Exponential Cost SSP Problems 
A!ne monotonic models appear in several contexts. In particular, finitestate sequential stochastic control problems (including SSP problems) with nonnegative cost per stage (see, e.g., [Ber12a], Chapter 3, and Section 4.1) are special cases where J̄ is the identically zero function [J̄(x) $ 0]. We will describe another type of SSP problem, where the cost function of a policy accumulates over time multiplicatively, rather than additively. 
As in the SSP problems of the preceding section, we assume that there are n states x = 1, . . . , n, and a cost-free and absorbing state t. There are probabilistic state transitions among the states x = 1, . . . , n, up to the first time a transition to state t occurs, in which case the state transitions terminate. We denote by pxt(u) and pxy(u) the probabilities of transition under u from x to t and to y, respectively, so that 
pxt(u) + n# 
y=1 
pxy(u) = 1, x = 1, . . . , n, u ! U(x). 
We introduce nonnegative scalars h(x, u, t) and h(x, u, y), 
h(x, u, t) " 0, h(x, u, y) " 0, # x, y = 1, . . . , n, u ! U(x),
188 Semicontractive Models Chap. 3 
and we consider the a!ne monotonic problem where the scalars Axy(u) and b(x, u) are defined by 
Axy(u) = pxy(u)h(x, u, y), x, y = 1, . . . , n, u ! U(x), 
and b(x, u) = pxt(u)h(x, u, t), x = 1, . . . , n, u ! U(x), 
and the vector J̄ is the unit vector, 
J̄(x) = 1, x = 1, . . . , n. 
The cost function of this problem has a multiplicative character as we show next. 
Indeed, with the preceding definitions of Axy(u), b(x, u), and J̄ , we will prove that the expression for the cost function of a policy " = {µ0, µ1, . . .}, 
J!(x0) = lim sup N"# 
(Tµ0 · · ·TµN!1 J̄)(x0), x0 = 1, . . . , n, 
can be written in the multiplicative form 
J!(x0) = lim sup N"# 
E 
$ N%13 
k=0 
h ! xk, µk(xk), xk+1 
" % , x0 = 1, . . . , n, 
(3.32) where: 
(a) {x0, x1, . . .} is the random state trajectory generated starting from x0, using ". 
(b) The expected value is with respect to the probability distribution of that trajectory. 
(c) We use the notation 
h ! xk, µk(xk), xk+1 
" = 1, if xk = xk+1 = t, 
(so that the multiplicative cost accumulation stops once the state reaches t). 
Thus, we claim that J!(x0) can be viewed as the expected value of cost accumulated multiplicatively, starting from x0 up to reaching the termination state t (or indefinitely accumulated multiplicatively, if t is never reached). 
To verify the formula (3.32) for J! , we use the definition TµJ = bµ +AµJ, to show by induction that for every " = {µ0, µ1, . . .}, we have 
Tµ0 · · ·TµN!1 J̄ = Aµ0 · · ·AµN!1 J̄ + bµ0 + N%1# 
k=1 
Aµ0 · · ·Aµk!1bµk . (3.33)
Sec. 3.5 Applications in Shortest Path and Other Contexts 189 
We then interpret the n components of each vector on the right as conditional expected values of the expression 
N%13 
k=0 
h ! xk, µk(xk), xk+1 
" (3.34) 
multiplied with the appropriate conditional probability. In particular: 
(a) The ith component of the vector Aµ0 · · ·AµN!1 J̄ in Eq. (3.33) is the conditional expected value of the expression (3.34), given that x0 = i and xN (= t, multiplied with the conditional probability that xN (= t, given that x0 = i. 
(b) The ith component of the vector bµ0 in Eq. (3.33) is the conditional expected value of the expression (3.34), given that x0 = i and x1 = t, multiplied with the conditional probability that x1 = t, given that x0 = i. 
(c) The ith component of the vector Aµ0 · · ·Aµk!1bµk in Eq. (3.33) is 
the conditional expected value of the expression (3.34), given that x0 = i, x1, . . . , xk%1 (= t, and xk = t, multiplied with the conditional probability that x1, . . . , xk%1 (= t, and xk = t, given that x0 = i. 
By adding these conditional probability expressions, we obtain the ith component of the unconditional expected value 
E 
$ N%13 
k=0 
h ! xk, µk(xk), xk+1 
" % , 
thus verifying the formula (3.32). A special case of multiplicative cost problem is the risk-sensitive SSP 
problem with exponential cost function, where for all x = 1, . . . , n, and u ! U(x), 
h(x, u, y) = exp ! g(x, u, y) 
" , y = 1, . . . , n, t, 
and the function g can take both positive and negative values. The mapping Tµ has the form 
(TµJ)(x) = pxt ! µ(x) 
" exp ! g(x, µ(x), t) 
" 
+ n# 
y=1 
pxy ! µ(x) 
" exp ! g(x, µ(x), y) 
" J(y), x = 1, . . . , n, 
(3.35) where pxy(u) is the probability of transition from x to y under u, and g(x, u, y) is the cost of the transition. The Bellman equation is 
J(x) = inf u!U(x) 
1 pxt(u)exp 
! g(x, u, t) 
" + 
n# 
y=1 
pxy(u)exp ! g(x, u, y) 
" J(y) 
2 .
190 Semicontractive Models Chap. 3 
Based on Eq. (3.32), we have that J!(x0) is the limit superior of the expected value of the exponential of the N -step additive finite horizon cost 
up to termination, i.e., )k̄ 
k=0 g ! xk, µk(xk), xk+1 
" , where k̄ is equal to the 
first index prior to N * 1 such that xk̄+1 = t, or is equal to N * 1 if there is no such index. The use of the exponential introduces risk aversion, by assigning a strictly convex increasing penalty for large rather than small cost of a trajectory up to termination (and hence a preference for small variance of the additive cost up to termination). 
The deterministic version of the exponential cost problem where for each u ! U(x), one of the transition probabilities pxt(u), px1(u), . . . , pxn(u) is equal to 1 and all others are equal to 0, is mathematically equivalent to the classical deterministic shortest path problem (since minimizing the exponential of a deterministic expression is equivalent to minimizing that expression). For this problem a standard assumption is that there are no cycles that have negative total length to ensure that the shortest path length is finite. However, it is interesting that this assumption is not required for the analysis of the present section: when there are paths that travel perpetually around a negative length cycle we simply have J*(x) = 0 for all states x on the cycle, which is permissible within our context. 
Assumptions on Policies - Contractive Policies 
Let us now derive an expression for the cost function of a policy. By repeatedly applying the mapping Tµ to the equation TµJ = bµ + AµJ , we have 
TN µ J = AN 
µ J + N%1# 
k=0 
Ak µbµ, # J ! E+(X), N = 1, 2, . . . , 
and hence 
Jµ = lim sup N"# 
TN µ J̄ = lim sup 
N"# AN 
µ J̄ + # 
k=0 
Ak µbµ (3.36) 
(the series converges since Aµ and bµ have nonnegative components). We say that µ is contractive if Aµ has eigenvalues that are strictly 
within the unit circle. In this case Tµ is a contraction mapping with respect to some weighted sup-norm (see Prop. B.3 in Appendix B). If µ is contractive, then AN 
µ J̄ ' 0 and from Eq. (3.36), it follows that 
Jµ = # 
k=0 
Ak µbµ = (I *Aµ)%1bµ, 
and Jµ is real-valued as well as nonnegative, i.e., Jµ ! R+(X). Moreover, a contractive µ is alsoR+(X)-regular, since Jµ does not depend on the initial function J̄ . The reverse is also true as shown by the following proposition.
Sec. 3.5 Applications in Shortest Path and Other Contexts 191 
Proposition 3.5.6: A policy µ is contractive if and only if it is R+(X)-regular. Moreover, if µ is noncontractive and all the components of bµ are strictly positive, there exists a state x such that the corresponding component of the vector 
)# k=0 A 
k µbµ is +. 
Proof: As noted earlier, if µ is contractive it is R+(X)-regular. It will thus su!ce to show that for a noncontractive µ and strictly positive components of bµ, some component of 
)# k=0 A 
k µbµ is +. Indeed, according 
to the Perron-Frobenius Theorem, the nonnegative matrix Aµ has a real eigenvalue !, which is equal to its spectral radius, and an associated nonnegative eigenvector ( (= 0 [see Prop. B.3(a) in Appendix B]. Choose $ > 0 to be such that bµ " $(, so that 
# 
k=0 
Ak µbµ " $ 
# 
k=0 
Ak µ( = $ 
4 # 
k=0 
!k 
5 (. 
Since some component of ( is positive while ! " 1 (since µ is noncontractive), the corresponding component of the infinite sum on the right is infinite, and the same is true for the corresponding component of the vector)# 
k=0 A k µbµ on the left. Q.E.D. 
Let us introduce some assumptions that are similar to the ones of the preceding section. 
Assumption 3.5.5: There exists at least one contractive policy. 
Assumption 3.5.6: (Compactness and Continuity) The control space U is a metric space, and Axy(·) and b(x, ·) are continuous functions of u over U(x), for all x and y. Moreover, for each state x, the sets $ 
u ! U(x) /// b(x, u) + 
n# 
y=1 
Axy(u)J(y) - ! 
% 
are compact subsets of U for all scalars ! ! , and J ! R+(X). 
Case of Infinite Cost Noncontractive Policies 
We now turn to questions relating to Bellman’s equation, the convergence of the VI and PI algorithms, as well as conditions for optimality of a stationary
192 Semicontractive Models Chap. 3 
policy. We first consider the following assumption, which parallels the infinite cost Assumption 3.5.3 for SSP problems. 
Assumption 3.5.7: (Infinite Cost Condition) For every noncontractive policy µ, there is at least one state such that the corresponding component of the vector 
)# k=0 A 
k µbµ is equal to +. 
We will now show that for S = R+(X), Assumptions 3.5.5, 3.5.6, and 3.5.7 imply all the parts of Assumption 3.3.1 of Section 3.3, so Prop. 3.3.1 can be applied to the a!ne monotonic model. Indeed parts (a), (e) of Assumption 3.3.1 clearly hold. Part (b) also holds, since by Assumption 3.5.5 there exists a contractive and hence S-regular policy, so we have J* 
S ! R+(X). Moreover Assumption 3.5.6 implies part (d), while Assumption 3.5.7 implies part (c). Finally part (f) holds since for every J ! R+(X), the zero function, J $(x) $ 0, lies in R+(X), and satisfies J $ - J and J $ - TJ $. Thus Prop. 3.3.1 yields the following result. 
Proposition 3.5.7: (Bellman’s Equation, Policy Iteration, Va-lue Iteration, and Optimality Conditions) Let Assumptions 3.5.5, 3.5.6, and 3.5.7 hold. 
(a) The optimal cost vector J* is the unique fixed point of T within R+(X). 
(b) We have T kJ ' J* for all J ! R+(X). 
(c) A policy µ is optimal if and only if TµJ* = TJ*. Moreover there exists an optimal policy that is contractive. 
(d) For any J ! R+(X), if J - TJ we have J - J*, and if J " TJ we have J " J*. 
(e) Every sequence {µk} generated by the PI algorithm starting from a contractive policy µ0 satisfies Jµk ) J*. Moreover, if the set of 
contractive policies is finite, there exists k̄ " 0 such that µk̄ is optimal. 
Example 3.5.1 (Exponential Cost Shortest Path Problem) 
Consider the deterministic shortest path example of Section 3.1.1, but with the exponential cost function of the present subsection; cf. Eq. (3.35). There are two policies denoted µ and µ"; see Fig. 3.5.2. The corresponding mappings and costs are shown in the figure, and Bellman’s equation is given by 
J(1) = (TJ)(1) = min & exp(b), exp(a)J(1) 
' .
Sec. 3.5 Applications in Shortest Path and Other Contexts 193 
a 1 2 1 2 t b 
t b Destination 
Policy µ 
Jµ(1) = exp(b) 
) (TµJ)(1) = exp(b) ( 
a Length b 
Length a 
) and Policy µ! 
) Jµ!(1) = limN!" exp(aN) 
(Tµ!J)(1) = exp(a)J(1) 
Figure 3.5.2. Shortest path problem with exponential cost function. 
We consider three cases: 
(a) a > 0: Here the proper policy µ is optimal, and the improper policy µ" is R+(X)-irregular (noncontractive) and has infinite cost, Jµ"(1) = ". The assumptions of Prop. 3.5.7 hold, and consistently with the conclusions of the proposition, J#(1) = exp(b) is the unique solution of Bellman’s equation. 
(b) a = 0: Here the improper policy µ" is R+(X)-irregular (noncontractive) and has finite cost, Jµ"(1) = 1, so the assumptions of Prop. 3.5.7 are violated. The set of solutions of Bellman’s equation within S = R+(X) is the interval 
6 0, exp(b) 
7 . 
(c) a < 0: Here both policies are contractive, including the improper policy µ". The assumptions of Prop. 3.5.7 hold, and consistently with the conclusions of the proposition, J#(1) = 0 is the unique solution of Bellman’s equation. 
The reader may also verify that in the cases where a += 0, the assumptions and the results of Prop. 3.5.7 hold. 
Case of Finite Cost Noncontractive Policies 
We will now eliminate Assumption 3.5.7, thus allowing noncontractive policies with real-valued cost functions, similar to the corresponding case of the preceding section, under the weak SSP conditions. Let us denote by Ĵ the optimal cost function that can be achieved with contractive policies only, 
Ĵ(x) = inf µ: contractive 
Jµ(x), x = 1, . . . , n. (3.37) 
We use the perturbation approach of Section 3.4 and Prop. 3.4.1 to show that Ĵ is a solution of Bellman’s equation. In particular, we add a constant % > 0 to all components of bµ. By using arguments that are entirely analogous to the ones for the SSP case of Section 3.5.1, we obtain the following proposition, which is illustrated in Fig. 3.5.3. A detailed analysis and proof is given in the exercises.
194 Semicontractive Models Chap. 3 
Paths of VI Unique solution of Bellman’s equation 
Fixed Points of T 
2 Ĵ JĴ : Largest fixed point of T J 
b < 0 
Figure 3.5.3. Schematic illustration of Prop. 3.5.8 for a problem with two states. The optimal cost function over contractive policies, Ĵ , is the largest solution of Bellman’s equation, while VI converges to Ĵ starting from J & Ĵ. 
Proposition 3.5.8: (Bellman’s Equation, Value Iteration, and Optimality Conditions)Let Assumptions 3.5.5 and 3.5.6 hold. Then: 
(a) The optimal cost function over contractive policies, Ĵ , is the largest solution of Bellman’s equation J = TJ within R+(X), i.e., Ĵ is a solution that belongs to R+(X), and if J $ ! R+(X) is another solution, we have J $ - Ĵ . 
(b) We have T kJ ' Ĵ for every J ! R+(X) with J " Ĵ . 
(c) Let µ be a contractive policy. Then µ is optimal within the class of contractive policies (i.e., Jµ = Ĵ) if and only if TµĴ = T Ĵ . 
(d) For every J ! R+(X) such that J - TJ , we have J - Ĵ . 
The other results of Section 3.5.1 for SSP problems also have straightforward analogs. Moreover, there is an adaptation of the example of Section 3.1.2, which provides an a!ne monotonic model for which J* is not a fixed point of T (see the author’s paper [Ber16a], to which we refer for further discussion). 
Example 3.5.2 (Deterministic Shortest Path Problem with Exponential Cost - Continued) 
Consider the problem of Fig. 3.5.2, for the case a = 0. This is the case where the noncontractive policy µ" has finite cost, so Assumption 3.5.7 is violated and Prop. 3.5.7 does not apply. However, it can be seen that the assumptions of Prop. 3.5.8 hold. Consistent with part (a) of the proposition, the optimal
Sec. 3.5 Applications in Shortest Path and Other Contexts 195 
cost over contractive policies, Ĵ(1) = exp(b), is the largest of the fixed points of T . The other parts of Prop. 3.5.8 may also be easily verified. 
We note that in the absence of the infinite cost Assumption 3.5.7, it is possible that the only optimal policy is noncontractive, even if the compactness Assumption 3.5.6 holds and Ĵ = J*. This is shown in the following example. 
Example 3.5.3 (A Counterexample on the Existence of an Optimal Contractive Policy) 
Consider the exponential cost version of the blackmailer problem of Example 3.4.2 (cf. Fig. 3.4.1). Here there is a single state 1, at which we must choose u % [0, 1]. Then, we terminate at no cost [g(1, u, t) = 0 in Eq. (3.35)] with probability u, and we stay at state 1 at cost !u [i.e., g(1, u, 1) = !u in Eq. (3.35)] with probability 1! u. We have 
b(i, u) = u exp (0) = u, A11(u) = (1! u) exp (!u), 
so that H(1, u, J) = u+ (1! u) exp (!u)J. 
Here there is a unique noncontractive policy µ": it chooses u = 0 at state 1, and has cost Jµ"(1) = 1. Every policy µ with µ(1) % (0, 1] is contractive, and Jµ can be obtained by solving the equation Jµ = TµJµ, i.e., 
Jµ(1) = µ(1) + ! 1! µ(1) 
" exp ! ! µ(1) 
" Jµ(1). 
We thus obtain 
Jµ(1) = µ(1) 
1! ! 1! µ(1) 
" exp ! ! µ(1) 
" . 
By minimizing over µ(1) % (0, 1] this expression, it can be seen that Ĵ(1) = J#(1) = 1 
2 , but there exists no optimal policy, and no optimal policy within the class of contractive policies [Jµ(1) decreases monotonically to 1 
2 as µ(1) $ 0]. 
3.5.3 Robust Shortest Path Planning 
We will now discuss how the analysis of Sections 3.3 and 3.4 applies to minimax shortest path-type problems, following the author’s paper [Ber19c], to which we refer for further discussion. To formally describe the problem, we consider a graph with a finite set of nodes X . {t} and a finite set of directed arcs A % 
& (x, y) | x, y ! X . {t} 
' , where t is a special node called 
the destination. At each node x ! X we may choose a control u from a
196 Semicontractive Models Chap. 3 
nonempty set U(x), which is a subset of a finite set U . Then a successor node y is selected by an antagonistic opponent from a nonempty set Y (x, u) % X . {t} and a cost g(x, u, y) is incurred. The destination node t is absorbing and cost-free, in the sense that the only outgoing arc from t is (t, t), and we have Y (t, u) = {t} and g(t, u, t) = 0 for all u ! U(t). 
As earlier, we denote the set of all policies by #, and the finite set of all stationary policies by M. Also, we denote the set of functions J : X &' [*+,+] by E(X), and the set of functions J : X &' (*+,+) by R(X). We introduce the mapping H : X / U / E(X) &' [*+,+] given by 
H(x, u, J) = max y!Y (x,u) 
6 g(x, u, y) + J̃(y) 
7 , x ! X, (3.38) 
where for any J ! E(X) we denote by J̃ the function given by 
J̃(y) = 
( J(y) if y ! X , 0 if y = t. 
(3.39) 
We consider the mapping T : E(X) &' E(X) defined by 
(TJ)(x) = min u!U(x) 
H(x, u, J), x ! X, (3.40) 
and for each policy µ, the mapping Tµ : E(X) &' E(X), defined by 
(TµJ)(x) = H ! x, µ(x), J 
" , x ! X. (3.41) 
We let J̄ be the zero function, 
J̄(x) = 0, # x ! X. 
The cost function of a policy " = {µ0, µ1, . . .} is 
J!(x) = lim sup k"# 
(Tµ0 · · ·Tµk J̄)(x), x ! X, 
and J*(x) = inf!!! J!(x), cf. Definition 3.2.1. For a policy µ ! M, we define a possible path under µ starting at 
node x0 ! X to be an arc sequence of the form 
p = & (x0, x1), (x1, x2), . . . 
' , 
such that xk+1 ! Y ! xk, µ(xk) 
" for all k " 0. The set of all possible 
paths under µ starting at x0 is denoted by P (x0, µ). The length of a path p ! P (x0, µ) is defined by 
Lµ(p) = lim sup m"# 
m# 
k=0 
g ! xk, µ(xk), xk+1 
" .
Sec. 3.5 Applications in Shortest Path and Other Contexts 197 
Using Eqs. (3.38)-(3.41), we see that for any µ ! M and x ! X , (T k µ J̄)(x) 
is the result of the k-stage DP algorithm that computes the length of the longest path under µ that starts at x and consists of k arcs. 
For completeness, we also define the length of a portion 
& (xi, xi+1), (xi+1, xi+2), . . . , (xm, xm+1) 
' 
of a path p ! P (x0, µ), consisting of a finite number of consecutive arcs, by 
m# 
k=i 
g ! xk, µ(xk), xk+1 
" . 
When confusion cannot arise we will also refer to such a finite-arc portion as a path. Of special interest are cycles , i.e., paths of the form& (xi, xi+1), (xi+1, xi+2), . . . , (xi+m, xi) 
' . Paths that do not contain any 
cycle other than the self-cycle (t, t) are called simple. For a given policy µ ! M and x0 (= t, a path p ! P (x0, µ) is said to 
be terminating if it has the form 
p = & (x0, x1), (x1, x2), . . . , (xm, t), (t, t), . . . 
' , (3.42) 
where m is a positive integer, and x0, . . . , xm are distinct nondestination nodes. Since g(t, u, t) = 0 for all u ! U(t), the length of a terminating path p of the form (3.42), corresponding to µ, is given by 
Lµ(p) = g ! xm, µ(xm), t 
" + 
m%1# 
k=0 
g ! xk, µ(xk), xk+1 
" , 
and is equal to the finite length of its initial portion that consists of the first m+ 1 arcs. 
An important characterization of a policy µ ! M is provided by the subset of arcs 
Aµ = .x!X 
& (x, y) | y ! Y 
! x, µ(x) 
"' . 
Thus Aµ . (t, t) can be viewed as the set of all possible paths under µ, .x!XP (x, µ), in the sense that it contains this set of paths and no other paths. We refer to Aµ as the characteristic graph of µ. We say that Aµ is destination-connected if for each x ! X there exists a terminating path in P (x, µ). 
We say that µ is proper if the characteristic graph Aµ is acyclic (i.e., contains no cycles). Thus µ is proper if and only if all the paths in .x!XP (x, µ) are simple and hence terminating (equivalently µ is proper if and only if Aµ is destination-connected and has no cycles). The term “proper” is consistent with the one used in Section 3.5.1 for SSP problems, where it indicates a policy under which the destination is reached
198 Semicontractive Models Chap. 3 
a 1 2 
1 2 t b 
t b Destination 
0 1 2 
1 2 t b 
t b Destination 
Improper policy µ 
a 1 2 
0 1 2 
b Proper Policy µ! 
Figure 3.5.4. A robust shortest path problem with X = {1, 2}, two controls at node 1, and one control at node 2. The two policies, µ and µ", correspond to the two controls at node 1. The figure shows the characteristic graphs Aµ and Aµ! . 
with probability 1. If µ is not proper, it is called improper , in which case the characteristic graph Aµ must contain a cycle; see the examples of Fig. 3.5.4. Intuitively, a policy is improper, if and only if under that policy there are initial states such that the antagonistic opponent can force movement along a cycle without ever reaching the destination. 
The following proposition clarifies the properties of Jµ when µ is improper. 
Proposition 3.5.9: Let µ be an improper policy. 
(a) If all cycles in the characteristic graphAµ have nonpositive length, Jµ(x) < + for all x ! X . 
(b) If all cycles in the characteristic graph Aµ have nonnegative length, Jµ(x) > *+ for all x ! X . 
(c) If all cycles in the characteristic graph Aµ have zero length, Jµ is real-valued. 
(d) If there is a positive length cycle in the characteristic graph Aµ, we have Jµ(x) = + for at least one node x ! X . More generally, for each J ! R(X), we have lim supk"#(T k 
µJ)(x) = + for at least one x ! X . 
Proof: Any path with a finite number of arcs, can be decomposed into a simple path, and a finite number of cycles (see e.g., the path decomposition theorem of [Ber98], Prop. 1.1, and Exercise 1.4). Since there is only a finite number of simple paths under µ, their length is bounded above and below. Thus in part (a) the length of all paths with a finite number of
Sec. 3.5 Applications in Shortest Path and Other Contexts 199 
arcs is bounded above, and in part (b) it is bounded below, implying that Jµ(x) < + for all x ! X or Jµ(x) > *+ for all x ! X , respectively. Part (c) follows by combining parts (a) and (b). 
To show part (d), consider a path p, which consists of an infinite repetition of the positive length cycle that is assumed to exist. Let Ck 
µ(p) be the length of the path that consists of the first k cycles in p. Then Ck 
µ(p) ' + and Ck µ(p) - Jµ(x) for all k, where x is the first node in the 
cycle, thus implying that Jµ(x) = +. Moreover for every J ! R(X) and all k, (T k 
µJ)(x) is the maximum over the lengths of the k-arc paths that start at x, plus a terminal cost that is equal to either J(y) (if the terminal node of the k-arc path is y ! X), or 0 (if the terminal node of the k-arc path is the destination). Thus we have, 
(T k µ J̄)(x) + min 
( 0, min 
x!X J(x) 
* - (T k 
µJ)(x). 
Since lim supk"#(T k µ J̄)(x) = Jµ(x) = + as shown earlier, it follows that 
lim supk"#(T k µJ)(x) = + for all J ! R(X). Q.E.D. 
Note that if there is a negative length cycle in the characteristic graph Aµ, it is not necessarily true that for some x ! X we have Jµ(x) = *+. Even for x on the negative length cycle, the value of Jµ(x) is determined by the longest path in P (x, µ), which may be simple in which case Jµ(x) is a real number, or contain an infinite repetition of a positive length cycle in which case Jµ(x) = +. 
Properness and Regularity 
We will now make a formal connection between the notions of properness and R(X)-regularity. We recall that µ is R(X)-regular if Jµ ! R(X), Jµ = TµJµ, and T k 
µJ ' Jµ for all J ! R(X) (cf. Definition 3.2.2). Clearly if µ is proper, we have Jµ ! R(X) and the equation Jµ = TµJµ holds (this is Bellman’s equation for the longest path problem involving the acyclic graph Aµ). We will also show that T k 
µJ ' Jµ for all J ! R(X), so that a proper policy is R(X)-regular. However, the following proposition shows that there may be someR(X)-regular policies that are improper, depending on the sign of the lengths of their associated cycles. 
Proposition 3.5.10: The following are equivalent for a policy µ: 
(i) µ is R(X)-regular. 
(ii) The characteristic graph Aµ is destination-connected and all its cycles have negative length. 
(iii) µ is either proper or else it is improper, all the cycles of the characteristic graph Aµ have negative length, and Jµ ! R(X).
200 Semicontractive Models Chap. 3 
Proof: To show that (i) implies (ii), let µ be R(X)-regular and to arrive at a contradiction, assume that Aµ contains a nonnegative length cycle. Let x be a node on the cycle, consider the path p that starts at x and consists of an infinite repetition of this cycle, and let Lk 
µ(p) be the length of the first k arcs of that path. Let also J be a constant function, J(x) $ r, where r is a scalar. Then we have 
Lk µ(p) + r - (T k 
µJ)(x), 
since from the definition of Tµ, we have that (T k µJ)(x) is the maximum 
over the lengths of all k-arc paths under µ starting at x, plus r, if the last node in the path is not the destination. Since µ is R(X)-regular, we have Jµ ! R(X) and lim supk"#(T k 
µJ)(x) = Jµ(x) < +, so that for all scalars r, 
lim sup k"# 
! Lk µ(p) + r 
" - Jµ(x) < +. 
Taking supremum over r ! ,, it follows that lim supk"# Lk µ(p) = *+, 
which contradicts the nonnegativity of the cycle of p. Thus all cycles of Aµ 
have negative length. To show that Aµ is destination-connected, assume the contrary. Then there exists some node x ! X such that all paths in P (x, µ) contain an infinite number of cycles. Since the length of all cycles is negative, as just shown, it follows that Jµ(x) = *+, which contradicts the R(X)-regularity of µ. 
To show that (ii) implies (iii), we assume that µ is improper and show that Jµ ! R(X). By (ii) Aµ is destination-connected, so the set P (x, µ) contains a simple path for all x ! X . Moreover, since by (ii) the cycles of Aµ have negative length, each path in P (x, µ) that is not simple has smaller length than some simple path in P (x, µ). This implies that Jµ(x) is equal to the largest path length among simple paths in P (x, µ), so Jµ(x) is a real number for all x ! X . 
To show that (iii) implies (i), we note that if µ is proper, it is R(X)-regular, so we focus on the case where µ is improper. Then by (iii), Jµ ! R(X), so to show R(X)-regularity of µ, we must show that (T k 
µJ)(x) ' Jµ(x) for all x ! X and J ! R(X), and that Jµ = TµJµ. Indeed, from the definition of Tµ, we have 
(T k µJ)(x) = sup 
p!P (x,µ) 
6 Lk µ(p) + J(xk 
p) 7 , (3.43) 
where Lk µ(p) is the length of the first k arcs of path p, xk 
p is the node reached after k arcs along the path p, and J(t) is defined to be equal to 0. Thus as k ' +, for every path p that contains an infinite number of cycles (each necessarily having negative length), the sequence Lk 
p(µ)+J(xk p) approaches 
*+. It follows that for su!ciently large k, the supremum in Eq. (3.43) is attained by one of the simple paths in P (x, µ), so xk 
p = t and J(xk p) = 0. 
Thus the limit of (T k µJ)(x) does not depend on J , and is equal to the limit
Sec. 3.5 Applications in Shortest Path and Other Contexts 201 
a 
a 1 2 1 2 t b 
t b Destination 
a 0 1 2 
Figure 3.5.5. The characteristic graph Aµ corresponding to an improper policy, for the case of a single node 1 and a destination node t. The arcs lengths are shown in the figure. 
of (T k µ J̄)(x), i.e., Jµ(x). To show that Jµ = TµJµ, we note that by the 
preceding argument, Jµ(x) is the length of the longest path among paths that start at x and terminate at t. Moreover, we have 
(TµJµ)(x) = max y!Y (x,µ(x)) 
6 g(x, µ(x), y) + Jµ(y) 
7 , 
where we denote Jµ(t) = 0. Thus (TµJµ)(x) is also the length of the longest path among paths that start at x and terminate at t, and hence it is equal to Jµ(x). Q.E.D. 
We illustrate the preceding proposition, in relation to the infinite cost condition of Assumption 3.3.1, with a two-node example involving an improper policy with a cycle that may have positive, zero, or negative length. 
Example 3.5.4: 
Let X = {1}, and consider the policy µ where at state 1, the antagonistic opponent may force either staying at 1 or terminating, i.e., Y 
! 1, µ(1) 
" = 
{1, t}; cf. Fig. 3.5.5. Then µ is improper since its characteristic graph Aµ 
contains the self-cycle (1, 1). Let 
g ! 1, µ(1), 1 
" = a, g 
! 1, µ(1), t 
" = 0. 
Then, (TµJµ)(1) = max 
6 0, a+ Jµ(1) 
7 , 
and 
Jµ(1) = -" if a > 0, 0 if a ) 0. 
Consistently with Prop. 3.5.10, the following hold: 
(a) For a > 0, the cycle (1, 1) has positive length, and µ is R(X)-irregular. Here we have Jµ(1) = ", and the infinite cost condition of Assumption 3.3.1 is satisfied.
202 Semicontractive Models Chap. 3 
(b) For a = 0, the cycle (1, 1) has zero length, and µ is R(X)-irregular. Here we have Jµ(1) = 0, and the infinite cost condition of Assumption 3.3.1 is violated because for a function J % R(X) with J(1) > 0, 
lim sup k%$ 
(T k µJ)(x) = J(1) > 0 = Jµ(1). 
(c) For " < 0, the cycle (1, 1) has negative length, and µ is R(X)-regular. Here we have Jµ % R(X), Jµ(1) = max 
6 0, a + Jµ(1) 
7 = (TµJµ)(1), 
and for all J % R(X), 
lim k%$ 
(T k µJ)(1) = 0 = Jµ(1). 
We will now apply the regularity results of Sections 3.2-3.4 with S = R(X). To this end, we introduce assumptions that will allow the use of Prop. 3.3.1. 
Assumption 3.5.8: 
(a) There exists at least one R(X)-regular policy. 
(b) For every R(X)-irregular policy µ, some cycle in the characteristic graph Aµ has positive length. 
Assumption 3.5.8 is implied by the weaker conditions given in the following proposition. These conditions may be more easily verifiable in some contexts. 
Proposition 3.5.11: Assumption 3.5.8 holds if anyone of the following two conditions is satisfied. 
(1) There exists at least one proper policy, and for every improper policy µ, all cycles in the characteristic graph Aµ have positive length. 
(2) Every policy µ is either proper or else it is improper and its characteristic graph Aµ is destination-connected with all cycles having negative length, and Jµ ! R(X). 
Proof: Under condition (1), by Prop. 3.5.10, a policy is R(X)-regular if and only if it is proper. Moreover, since each R(X)-irregular and hence improper policy µ has cycles with positive length, it follows that for all J ! R(X), we have 
lim sup k"# 
(T k µJ)(x) = +
Sec. 3.5 Applications in Shortest Path and Other Contexts 203 
for some x ! X . The proof under condition (2) is similar, using Prop. 3.5.10. Q.E.D. 
We now show our main result for the problem of this section. 
Proposition 3.5.12: Let Assumption 3.5.8 hold. Then: 
(a) The optimal cost function J* is the unique fixed point of T within R(X). 
(b) We have T kJ ' J* for all J ! R(X). 
(c) A policy µ' is optimal if and only if Tµ#J* = TJ*. Moreover, there exists an optimal proper policy. 
(d) For any J ! R(X), if J - TJ we have J - J*, and if J " TJ we have J " J*. 
Proof: We verify the parts (a)-(f) of Assumption 3.3.1 with S = R(X), and we then use Prop. 3.3.1. To this end we argue as follows: 
(1) Part (a) is satisfied since S = R(X). 
(2) Part (b) is satisfied since by Assumption 3.5.8(a), there exists at least one R(X)-regular policy. Moreover, for each R(X)-regular policy µ, we have Jµ ! R(X). Since the number of all policies is finite, it follows that J* 
S ! R(X). 
(3) To show that part (c) is satisfied, note that by Prop. 3.5.10 every R(X)-irregular policy µ must be improper, so by Assumption 3.5.8(b), the characteristic graph Aµ contains a cycle of positive length. By Prop. 3.5.9(d), this implies that for each J ! R(X) and for at least one x ! X , we have lim supk"#(T k 
µJ)(x) = +. 
(4) Part (d) is satisfied since U(x) is a finite set. 
(5) Part (e) is satisfied since X is finite and Tµ is a continuous function that maps the finite-dimensional space R(X) into itself. 
(6) Part (f) follows from Prop. 3.3.2, which applies because S = R(X) = Rb(X) (since X is finite) and Eq. (3.27) clearly holds. 
Thus all parts of Assumption 3.3.1 are satisfied, and Prop. 3.3.1 applies with S = R(X). The conclusions of this proposition are precisely the results we want to prove [since improper policies have infinite cost for some initial states, as argued earlier, optimal S-regular policies must be proper; cf. the conclusion of part (c)]. Q.E.D. 
The following example illustrates what may happen in the absence of Assumption 3.5.8(b), when there may exist improper policies that involve
204 Semicontractive Models Chap. 3 
a 
a 1 2 1 2 t b 
t b Destination 
a 0 1 20 1 2 a 1 2 1 2 t b 
t b Destination 
Proper Policy µ Improper Policy µ! 
Figure 3.5.6. A counterexample involving a single node 1 in addition to the destination t. There are two policies, µ and µ", with corresponding characteristic graphs Aµ and Aµ! , and arc lengths shown in the figure. The improper policy µ" 
is optimal when a ( 0. It is R(X)-irregular if a = 0, and it is R(X)-regular if a < 0. 
a nonpositive length cycle. 
Example 3.5.5: 
Let X = {1}, and consider the proper policy µ with Y ! 1, µ(1) 
" = {t} and 
the improper policy µ" with Y ! 1, µ"(1) 
" = {1, t} (cf. Fig. 3.5.6). Let 
g ! 1, µ(1), t 
" = 1, g 
! 1, µ"(1), 1 
" = a ) 0, g 
! 1, µ"(1), t 
" = 0. 
The improper policy is the same as the one of Example 3.5.4. It can be seen that under both policies, the longest path from 1 to t consists of the arc (1, t). Thus, 
Jµ(1) = 1, Jµ"(1) = 0, 
so the improper policy µ" is optimal, and strictly dominates the proper policy µ. To explain what is happening here, we consider two di!erent cases: 
(1) a = 0: In this case, the optimal policy µ" is both improper and R(X)-irregular, but with finite cost Jµ"(1) < ". Thus the conditions of Props. 3.3.1 and 3.5.12 do not hold because Assumptions 3.3.1(c) and 3.5.9(b) are violated. 
(2) a < 0: In this case, µ" is improper but R(X)-regular, so there are no R(X)-irregular policies. Then all the conditions of Assumption 3.5.8 are satisfied, and Prop. 3.5.12 applies. Consistent with this proposition, there exists an optimal R(X)-regular policy (i.e., optimal over both proper and improper policies), which however is improper. 
For further analysis and algorithms for the robust shortest path planning problem, we refer to the paper [Ber19c]. In particular, this paper applies the perturbation approach of Section 3.4 to the case where it may be easier to guarantee nonnegativity rather than positivity of the lengths
Sec. 3.5 Applications in Shortest Path and Other Contexts 205 
of cycles corresponding to improper policies, which is required by Assump-tion 3.5.8(b). The paper shows that the VI algorithm terminates in a finite number of iterations starting from the initial function J with J(x) = + for all x ! X . Moreover the paper provides a Dijkstra-like algorithm for problems with nonnegative arc lengths. 
3.5.4 Linear-Quadratic Optimal Control 
In this subsection, we consider a classical problem from control theory, which involves the deterministic linear system 
xk+1 = Axk +Buk, k = 0, 1, . . . , 
where xk ! ,n, uk ! ,m for all k, and A and B are given matrices. The cost function of a policy " = {µ0, µ1, . . .} has the form 
J!(x0) = lim N"# 
N%1# 
k=0 
! x$ kQxk + µk(xk)$Rµk(xk) 
" , 
where x$ denotes the transpose of a column vector x, Q is a positive semidefinite symmetric n/n matrix, and R is a positive definite symmetric m/m matrix. This is a special case of the deterministic optimal control problem of Section 1.1, and was discussed briefly in the context of the onedimensional example of Section 3.1.4. 
The theory of this problem is well-known and is discussed in various forms in many sources, including the textbooks [AnM79] and [Ber17a] (Section 3.1). The solution revolves around stationary policies µ that are linear , in the sense that 
µ(x) = Lx, 
where L is some m / n matrix, and stable, in the sense that the matrix A+BL has eigenvalues that are strictly within the unit circle. Thus for a linear stable policy, the closed loop system 
xk+1 = (A+BL)xk 
is stable. We assume that there exists at least one linear stable policy. Among others, this guarantees that the optimal cost function J' is realvalued (it is bounded above by the real-valued cost function of every linear stable policy). 
The solution also revolves around the algebraic matrix Riccati equation, which is given by 
P = A$ ! P * PB(B$PB +R)%1B$P 
" A+Q, 
where the unknown is P , a symmetric n/ n matrix. It is well-known that if Q is positive definite, then the Riccati equation has a unique solution P '
206 Semicontractive Models Chap. 3 
within the class of positive semidefinite symmetric matrices, and that the optimal cost function has the form 
J*(x) = x$P 'x. 
Moreover, there is a unique optimal policy, and this policy is linear stable of the form 
µ'(x) = Lx, L = *(B$P 'B +R)%1B$P 'A. 
The existence of an optimal linear stable policy can be extended to the case where Q is instead positive semidefinite, but satisfies a certain “detectability” condition; see the textbooks cited earlier. 
However, in the general case where Q is positive semidefinite without further assumptions (e.g., Q = 0), the example of Section 3.1.4 shows that the optimal policy need not be stable, and in fact the optimal cost function over just the linear stable policies may be di"erent than J*.† We will discuss this case by using the perturbation-based approach of Section 3.4, and provide results that are consistent with the behavior observed in the example of Section 3.1.4. 
To convert the problem to our abstract format, we let 
X = ,n, U(x) = ,m, J̄(x) = 0, # x ! X, 
H(x, u, J) = x$Qx+ u$Ru+ J(Ax+Bu). 
Let S be the set of positive semidefinite quadratic functions, i.e., 
S = & J | J(x) = x$Px, P : positive semidefinite symmetric 
' . 
Let +M be the set of linear stable policies, and note that every linear stable policy is S-regular. This is due to the fact that for every quadratic function J(x) = x$Px and linear stable policy µ(x) = Lx, the k-stage costs (T k 
µJ)(x) and (T k 
µ J̄)(x) di"er by the term 
x$(A+BL)k$P (A+BL)kx, 
which vanishes in the limit as k ' +, since µ is stable. Consider the perturbation framework of Section 3.4, with forcing 
function p(x) = 1x12. 
† This is also true in the discounted version of the example of Section 3.1.4, where there is a discount factor " % (0, 1). The Riccati equation then takes 
the form P = A" ! "P ! "2PB("B"PB + R)!1B"P 
" A + Q, and for the given 
system and cost per stage, it has two solutions, P # = 0 and P̂ = #$2!1 # 
. The VI algorithm converges to P̂ starting from any P > 0.
Sec. 3.5 Applications in Shortest Path and Other Contexts 207 
Then for % > 0, the mapping Tµ," has the form 
(Tµ,"J)(x) = x$(Q+ %I)x+ µ(x)$Rµ(x) + J ! Ax+Bµ(x) 
" , 
where I is the identity, and corresponds to the linear-quadratic problem where Q is replaced by the positive definite matrix Q + %I. This problem admits a quadratic positive definite optimal cost Ĵ"(x) = x$P ' 
" x, and an optimal linear stable policy. Moreover, all the conditions of Prop. 3.4.1 can be verified. It follows that J* 
S is equal to the optimal cost over just the 
linear stable policies Ĵ , and is obtained as lim""0 Ĵ", which also implies that Ĵ(x) = x$P̂ x where P̂ = lim""0 P ' 
" . The perturbation line of analysis of the linear-quadratic problem will 
be generalized in Section 4.5. This generalization will address a deterministic discrete-time infinite horizon optimal control problem involving the system 
xk+1 = f(xk, uk), k = 0, 1, . . . , 
a nonnegative cost per stage g(x, u), and a cost-free termination state. We will introduce there a notion of stability, and we will show that the optimal cost function over the stable policies is the largest solution of Bellman’s equation. Moreover, we will show that the VI algorithm and several versions of the PI algorithm are valid for suitable initial conditions. 
3.5.5 Continuous-State Deterministic Optimal Control 
In this section, we consider an optimal control problem, where the objective is to steer a deterministic system towards a cost-free and absorbing set of states. The system equation is 
xk+1 = f(xk, uk), k = 0, 1, . . . , (3.44) 
where xk and uk are the state and control at stage k, belonging to sets X and U , respectively, and f is a function mapping X / U to X . The control uk must be chosen from a constraint set U(xk). No restrictions are placed on the nature of X and U : for example, they may be finite sets as in deterministic shortest path problems, or they may be continuous spaces as in classical problems of control to the origin or some other terminal set, including the linear-quadratic problem of Section 3.5.4. The cost per stage is denoted by g(x, u), and is assumed to be a real number. † 
Because the system is deterministic, given an initial state x0, a policy " = {µ0, µ1, . . .} when applied to the system (3.44), generates a unique sequence of state-control pairs 
! xk, µk(xk) 
" , k = 0, 1, . . . . The corresponding 
† In Section 4.5, we will consider a similar problem where the cost per stage 
will be assumed to be nonnegative, but some other assumptions from the present section (e.g., the subsequent Assumption 3.5.9) will be relaxed.
208 Semicontractive Models Chap. 3 
cost function is 
J⇡(x0) = lim sup N!1 
N 1X 
k=0 
g   xk, µk(xk) 
  , x0 2 X. 
We assume that there is a nonempty stopping set X0 ⇢ X, which consists of cost-free and absorbing states in the sense that 
g(x, u) = 0, x = f(x, u), 8 x 2 X0, u 2 U(x). (3.45) 
Based on our assumptions to be introduced shortly, the objective will be roughly to reach or asymptotically approach the set X0 at minimum cost. 
To formulate a corresponding abstract DP problem, we introduce the mapping Tµ : R(X) 7! R(X) by 
(TµJ)(x) = g   x, µ(x) 
  + J 
  f   x, µ(x) 
   , x 2 X, 
and the mapping T : E(X) 7! E(X) given by 
(TJ)(x) = inf u2U(x) 
  g(x, u) + J 
  f(x, u) 
  , x 2 X. 
Here as earlier, we denote by R(X) the set of real-valued functions over X, and by E(X) the set of extended real-valued functions over X. The initial function J̄ is the zero function [J̄(x) ⌘ 0]. An important fact is that because the problem is deterministic, J* is a fixed point of T (cf. Exercise 3.1). 
The analysis of the linear-quadratic problem of the preceding section has revealed two distinct types of behavior for the case where g   0: 
(a) J* is the unique fixed point of T within the set S (the set of nonnegative definite quadratic functions). 
(b) J* and the optimal cost function Ĵ over a restricted subset of S-regular policies (the linear stable policies) are both fixed points of T within the set S, but J* 6= Ĵ , and the VI algorithm converges to Ĵ when started with a function J   Ĵ . 
In what follows we will introduce assumptions that preclude case (b); we will postpone the discussion of of problems where we can have J* 6= Ĵ for Section 4.5, where we will use a perturbation-based line of analysis. Similar to the linear-quadratic problem, the restricted set of policies that we will consider have some “stability” property: they are either terminating (reach X0 in a finite number of steps), or else they asymptotically approach X0 
in a manner to be made precise later. As a first step in the analysis, let us introduce the e↵ective domain 
of J*, i.e., the set X* = 
  x 2 X | J*(x) < 1 
 .
Sec. 3.5 Applications in Shortest Path and Other Contexts 209 
Ordinarily, in practical applications, the states in X* are those from which one can reach the stopping set X0, at least asymptotically. We say that a policy µ is terminating if starting from any x0 → X*, the state sequence {xk} generated using µ reaches X0 in finite time, i.e., satisfies xk̄ → X0 for 
some index k̄. The set of terminating policies is denoted by !M. Our key assumption in this section is that for all x → X*, the optimal 
cost J*(x) can be approximated arbitrarily closely by using terminating policies. In Section 4.5 we will relax this assumption. 
Assumption 3.5.9: (Near-Optimal Termination) For every pair (x, ε) with x → X* and ε > 0, there exists a terminating policy µ [possibly dependent on (x, ε)] that satisfies Jµ(x) ↑ J*(x) + ε. 
This assumption implies in particular that the optimal cost function over terminating policies, 
Ĵ(x) = inf µ→ "M 
Jµ(x), x → X, 
is equal to J*. Note that Assumption 3.5.9 is equivalent to a seemingly weaker assumption where nonstationary policies can be used for termination (see Exercise 3.7). 
Specific and easily verifiable conditions that imply Assumption 3.5.9 are given in the exercises. A prominent case is when X and U are finite, so the problem becomes a deterministic shortest path problem. If all cycles of the state transition graph have positive length, then for every π and x with Jπ(x) < ↓ the generated path starting from x and using π must reach the destination, and this implies that there exists an optimal policy that terminates from all x → X*. Thus, in this case Assumption 3.5.9 is naturally satisfied. 
Another interesting case arises when g(x, u) = 0 for all (x, u) except if x /→ X0 and the next state f(x, u) is a termination state, in which case the cost of the stage is strictly negative, i.e., g(x, u) < 0 only when f(x, u) → X0. Thus no cost is incurred except for a negative cost upon termination. Intuitively, this is the problem of trying to find the best state from which to terminate, out of all states that are reachable from the initial state x0. Then, assuming that X0 can be reached from all states, Assumption 3.5.9 is satisfied. 
When X is the n-dimensional Euclidean space $n, it may easily happen that the optimal policies are not terminating from some x → X*, but instead the optimal state trajectories may approach X0 asymptotically. This is true for example in the linear-quadratic problem of the preceding section, whereX = $n, X0 = {0}, U = $m, the system is linear of the form xk+1 = Axk+Buk, where A and B are given matrices, and the optimal cost
210 Semicontractive Models Chap. 3 
function is positive definite quadratic. There the optimal policy is linear stable of the form µ∗(x) = Lx, where L is some matrix obtained through the steady-state solution of the Riccati equation. Since the optimal closedloop system has the form xk+1 = (A+BL)xk, the state will typically never reach the termination set X0 = {0} in finite time, although it will approach it asymptotically. However, the Assumption 3.5.9 is satisfied under some natural and easily verifiable conditions (see Exercise 3.8). 
Let us consider the set of functions 
S = # J → E(X) | J(x) = 0, ∀ x → X0, J(x) → $, ∀ x → X* 
$ . 
Since X0 consists of cost-free and absorbing states [cf. Eq. (3.45)], and J*(x) > −↓ for all x → X (by Assumption 3.5.9), the set S contains the cost functions Jµ of all terminating policies µ, as well as J*. Moreover 
it can be seen that every terminating policy is S-regular, i.e., !M ⊂ MS , implying that J* 
S = J*. The reason is that the terminal cost is zero after termination for any terminal cost function J → S, i.e., 
(T k µJ)(x) = (T k 
µ J̄)(x) = Jµ(x), 
for µ → !M, x → X*, and k sufficiently large. The following proposition is a consequence of the well-behaved region 
theorem (Prop. 3.2.1), the deterministic character of the problem (which guarantees that J* is a fixed point of T ; Exercise 3.1), and Assumption 3.5.9 (which guarantees that J* 
S = J*). 
Proposition 3.5.13: Let Assumption 3.5.9 hold. Then: 
(a) J* is the unique solution of the Bellman equation J = TJ within the set of all J → S such that J ≥ J*. 
(b) We have T kJ ⇒ J* for every J → S such that J ≥ J*. 
(c) If µ∗ is terminating and Tµ→J* = TJ*, then µ∗ is optimal. Con-versely, if µ∗ is terminating and is optimal, then Tµ→J* = TJ*. 
Generally, the convergence T kJ ⇒ J* for every J → S [Prop. 3.5.13(b)] cannot be shown except in special cases, such as finite-state problems (see Prop. 1.1(b), Ch. 4, of the book by Bertsekas and Tsitsiklis [BeT89]). To see what may happen in the absence of Assumption 3.5.9, consider the deterministic shortest path example of Section 3.1.1 with a = 0, b > 0, and S = $. Here Assumption 3.5.9 is violated and we have 0 = J* < Ĵ = b, while the set of fixed points of T is the interval (−↓, b]. However, for the same example, but with b ↑ 0 instead of b > 0, Assumption 3.5.9 is satisfied and Prop. 3.5.13 applies. Consider also the linear-quadratic example of
Sec. 3.6 Algorithms 211 
Section 3.1.4. Here Assumption 3.5.9 is violated. This results in multiple fixed points of T within S: the functions J*(x) ≡ 0 and Ĵ(x) = (γ2− 1)x2. In Section 4.5, we will reconsider this example, as well as the problem of this section for the case g(x, u) ≥ 0 for all (x, u), but under assumptions that are much weaker than Assumption 3.5.9. There, we will make a connection between regularity, perturbations like the ones of Section 3.4, and traditional notions of stability. 
Another interesting fact is that when the model of this section is extended in the natural way to a stochastic model with infinite state space, then under the analog of Assumption 3.5.9, J* need not be the unique solution of Bellman’s equation within the set of all J → S such that J ≥ J*. Indeed, we will show this in Section 4.6.1 with a stochastic example that involves a single control per state and nonnegative but unbounded cost per stage (if the cost per stage is nonnegative and bounded, and the optimal cost over the proper policies only is equal to J*, then J* will be proved to be the unique solution of Bellman’s equation within the set of all bounded J such that J ≥ 0). This is a striking difference between deterministic and stochastic optimal control problems with infinite state space. Another striking difference is that J* is always a solution of Bellman’s equation in deterministic problems (cf. Exercise 3.1), but this is not so in stochastic problems, even when the state space is finite (cf. Section 3.1.2). 
3.6 ALGORITHMS 
We have already discussed some VI and PI algorithms for finding J* and an optimal policy as part of our analysis under the weak and strong PI properties in Section 3.2. Moreover, we have shown that the VI algorithm converges to the optimal cost function J* for any starting function J → S in the case of Assumption 3.3.1 (cf. Prop. 3.3.1), or to the restricted optimal cost function J* 
S under the assumptions of Prop. 3.4.1(b). In this section, we will introduce additional algorithms. In Section 
3.6.1, we will discuss asynchronous versions of VI and will prove satisfactory convergence properties under reasonable assumptions. In Section 3.6.2, we will focus on a modified version of PI that is unaffected by the presence of S-irregular policies. This algorithm is similar to the optimistic PI algorithm with uniform fixed point (cf. Section 2.6.3), and can also be implemented in a distributed asynchronous computing environment. 
3.6.1 Asynchronous Value Iteration 
Let us consider the model of Section 2.6.1 for asynchronous distributed computation of the fixed point of a mapping T , and the asynchronous distributed VI method described there. The model involves a partition ofX into disjoint nonempty subsets X1, . . . , Xm, and a corresponding partition of J as J = (J1, . . . , Jm), where J" is the restriction of J on the set X".
212 Semicontractive Models Chap. 3 
We consider a network ofm processors, each updating asynchronously corresponding components of J . In particular, we assume that J" is updated only by processor $, and only for times t in a selected subset R" of iterations. Moreover, as in Section 2.6.1, processor $ uses components Jj supplied by other processors j += $ with communication “delays” t−τ"j(t) ≥ 0: 
J t+1 " (x) = 
% T & Jτ!1(t) 1 , . . . , Jτ!m(t) 
m 
' (x) if t → R", x → X", 
J t " (x) if t /→ R", x → X". 
(3.46) 
We can prove convergence within the frameworks of Sections 3.3 and 3.4 by using the asynchronous convergence theorem (cf. Prop. 2.6.1), and the fact that T is monotone and has J* as its unique fixed point within the appropriate set. We assume that the continuous updating and information renewal Assumption 2.6.1 holds. For simplicity we restrict attention to the framework of Section 3.3, under Assumption 3.3.1 with S = B(X). Assume further that we have two functions V , V → S such that 
V ↑ TV ↑ TV ↑ V , (3.47) 
so that, by Prop. 3.3.1, T kV ↑ J* ↑ T kV for all k, and 
T kV ↑ J*, T kV ↓ J*. 
Then we can show asynchronous convergence of the VI algorithm (3.46), starting from any function J0 with V ↑ J0 ↑ V . 
Indeed, let us apply Prop. 2.6.1 with the sets S(k) given by 
S(k) = # J → S | T kV ↑ J ↑ T kV 
$ , k = 0, 1, . . . . 
The sets S(k) satisfy S(k+ 1) ⊂ S(k) in view of Eq. (3.47) and the monotonicity of T . Using Prop. 3.3.1, we also see that S(k) satisfy the synchronous convergence and box conditions of Prop. 2.6.1. Thus, together with Assumption 2.6.1, all the conditions of Prop. 2.6.1 are satisfied, and the convergence of the algorithm follows starting from any J0 → S(0). 
3.6.2 Asynchronous Policy Iteration 
In this section, we focus on PI methods, under Assumption 3.3.1 and some additional assumptions to be introduced shortly. We first discuss briefly a natural form of PI algorithm, which generates S-regular policies exclusively. Let µ0 be an initial S-regular policy [there exists one by Assumption 3.3.1(b)]. At the typical iteration k, we have an S-regular policy µk, and we compute a policy µk+1 such that Tµk+1Jµk = TJµk (this is possible by Lemma 3.3.1). Then µk+1 is S-regular, by Lemma 3.3.2, and we have 
Jµk = TµkJµk ≥ TJµk = Tµk+1Jµk ≥ lim m↓∞ 
T k µk+1Jµk = Jµk+1 .
Sec. 3.6 Algorithms 213 
We can thus construct a sequence of S-regular policies {µk} and a corresponding nonincreasing sequence {Jµk}. Under some additional mild conditions it is then possible to show that Jµk ↓ J*, cf. Prop. 3.3.1(e). 
Unfortunately, when there are S-irregular policies, the preceding PI algorithm is somewhat limited, because an initial S-regular policy may not be known. Moreover, when asynchronous versions of the algorithm are implemented, it is difficult to guarantee that all the generated policies are S-regular. 
In what follows in this section, we will discuss a PI algorithm that works in the presence of S-irregular policies, and can operate in a distributed asynchronous environment, like the PI algorithm for contractive models of Section 2.6.3. The main assumption is that J* is the unique fixed point of T within R(X), the set of real-valued functions over X . This assumption holds under Assumption 3.3.1 with S = R(X), but it also holds under weaker conditions. Our assumptions also include finiteness of U , which among others facilitates the policy evaluation and policy improvement operations, and ensures that the algorithm generates iterates that lie in R(X). The algorithm and its analysis also go through if R(X) is replaced by R+(X) (the set of all nonnegative real-valued functions) in the following assumptions, arguments, and propositions. 
Assumption 3.6.1: In addition to the monotonicity Assumption 3.2.1, the following hold. 
(a) H(x, u, J) is real-valued for all J → R(X), x → X , and u → U(x). 
(b) U is a finite set. 
(c) For each sequence {Jm} ⊂ R(X) with either Jm ↑ J or Jm ↓ J for some J → R(X), we have 
lim m↓∞ 
H(x, u, Jm) = H (x, u, J) , ∀ x → X, u → U(x). 
(d) For all scalars r > 0 and functions J → R(X), we have 
H(x, u, J + r e) ↑ H(x, u, J) + r e, ∀ x → X, u → U(x), (3.48) 
where e is the unit function. 
(e) J* is the unique fixed point of T within R(X). 
Part (d) of the preceding assumption is a nonexpansiveness condition for H(x, u, ·), and can be easily verified in many DP models, including deterministic, minimax, and stochastic optimal control problems. It is not readily satisfied, however, in the affine monotonic model of Section 3.5.2.
214 Semicontractive Models Chap. 3 
Similar to Section 2.6.3, we introduce a new mapping that is parametrized by µ and can be shown to have a common fixed point for all µ. It operates on a pair (V,Q) where: 
 V is a real-valued function with a component denoted V (x) for each x → X . 
 Q is a real-valued function with a component denoted Q(x, u) for each pair (x, u) with x → X , u → U(x). 
The mapping produces a pair 
( MFµ(V,Q), Fµ(V,Q) 
) , 
where 
 Fµ(V,Q) is a function with a component Fµ(V,Q)(x, u) for each (x, u), defined by 
Fµ(V,Q)(x, u) = H ( x, u,min{V,Qµ} 
) , (3.49) 
where for any Q and µ, we denote by Qµ the function of x defined by 
Qµ(x) = Q ( x, µ(x) 
) , x → X, 
and for any two functions V1 and V2, we denote by min{V1, V2} the function of x given by 
min{V1, V2}(x) = min # V1(x), V2(x) 
$ , x → X. 
 MFµ(V,Q) is a function with a component ( MFµ(V,Q) 
) (x) for each 
x, where M is the operator of pointwise minimization over u: 
(MQ)(x) = min u→U(x) 
Q(x, u), 
so that ( MFµ(V,Q) 
) (x) = min 
u→U(x) Fµ(V,Q)(x, u). 
Note that under Assumption 3.6.1, M maps real-valued functions to real-valued functions, since by part (b) of that assumption, U is assumed finite. 
We consider an algorithm that is similar to the asynchronous PI algorithm given in Section 2.6.3 for contractive models. It applies asynchronously the mapping MFµ(V,Q) for local policy improvement and update of V and µ, and the mapping Fµ(V,Q) for local policy evaluation and update of Q. The algorithm involves a partition of the state space into sets X1, . . . , Xm, and assignment of each subset X" to a processor $ → {1, . . . ,m}. For each $, there are two infinite disjoint subsets of times
Sec. 3.6 Algorithms 215 
R",R" ⊂ {0, 1, . . .}, corresponding to policy improvement and policy evaluation iterations, respectively. At time t, each processor $ operates on V t(x), Qt(x, u), and µt(x), only for x in its “local” state space X". In particular, at each time t, each processor $ does one of the following: 
(a) Local policy improvement : If t → R", processor $ sets for all x → X", 
V t+1(x) = min u→U(x) 
H ( x, u,min{V t, Qt 
µt} ) = ( MFµt(V t, Qt) 
) (x), 
(3.50) sets µt+1(x) to a u that attains the minimum, and leaves Q unchanged, i.e., Qt+1(x, u) = Qt(x, u) for all x → X" and u → U(x). 
(b) Local policy evaluation: If t → R", processor $ sets for all x → X" and u → U(x), 
Qt+1(x, u) = H ( x, u,min{V t, Qt 
µt} ) = Fµt(V t, Qt)(x, u), (3.51) 
and leaves V and µ unchanged, i.e., V t+1(x) = V t(x) and µt+1(x) = µt(x) for all x → X". 
(c) No local change: If t /→ R" ∪ R", processor $ leaves Q, V , and µ unchanged, i.e., Qt+1(x, u) = Qt(x, u) for all x → X" and u → U(x), V t+1(x) = V t(x), and µt+1(x) = µt(x) for all x → X". 
Under Assumption 3.6.1, the algorithm generates real-valued functions if started with real-valued V 0 and Q0. We will prove that it converges to (J*, Q*), where J* is the unique fixed point of T within R(X) [cf. Assumption 3.6.1(e)], and Q* is defined by 
Q*(x, u) = H(x, u, J*), x → X, u → U(x). (3.52) 
To this end, we introduce the mapping F defined by 
(FQ)(x, u) = H ( x, u,MQ 
) , x → X, u → U(x), (3.53) 
and we show the following proposition. 
Proposition 3.6.1: Let Assumption 3.6.1 hold. Then Q* is the unique fixed point of F within the class of real-valued functions. 
Proof: By minimizing over u → U(x) in Eq. (3.52) and noting that J* is a fixed point of T , we have MQ* = TJ* = J*. Thus, by applying Eq. (3.53) and then Eq. (3.52), we obtain 
(FQ∗)(x, u) = H(x, u, J*) = Q∗(x, u), ∀ x → X, u → U(x).
216 Semicontractive Models Chap. 3 
Thus Q* is a fixed point of F , and it is real-valued since J* is real-valued and H is real-valued. 
To show uniqueness, let Q′ be any real-valued fixed point of F . Then Q′(x, u) = H(x, u,MQ′) for all x → X , u → U(x), and by minimization over u → U(x), we have MQ′ = T (MQ′). Hence MQ′ is equal to the unique fixed point J* of T , so that the equation Q′ = FQ′ yields Q′(x, u) = H(x, u,MQ′) = H(x, u, J*), for all (x, u). From the definition (3.52) of Q*, it then follows that Q′ = Q∗. Q.E.D. 
We introduce the µ-dependent mapping 
Lµ(V,Q) = ( MQ,Fµ(V,Q) 
) , (3.54) 
where Fµ(V,Q) is given by Eq. (3.49). For this mapping and other related mappings to be defined shortly, we implicitly assume that it operates on real-valued functions, so by Assumption 3.6.1(a),(b), it produces realvalued functions. Note that the policy evaluation part of the algorithm [cf. Eq. (3.51)] amounts to applying the second component of Lµ, while the policy improvement part of the algorithm [cf. Eq. (3.50)] amounts to applying the second component of Lµ, and then applying the first component of Lµ. The following proposition shows that (J*, Q*) is the common fixed point of the mappings Lµ, for all µ. 
Proposition 3.6.2: Let Assumption 3.6.1 hold. Then for all µ → M, the mapping Lµ of Eq. (3.54) is monotone, and (J*, Q*) is its unique fixed point within the class of real-valued functions. 
Proof: Monotonicity of Lµ follows from the monotonicity of the operators M and Fµ. To show that Lµ has (J*, Q*) as its unique fixed point, we first note that J* = MQ* and Q* = FQ*; cf. Prop. 3.6.1. Then, using also the definition of Fµ, we have 
J* = MQ*, Q* = FQ* = Fµ(J*, Q*), 
which shows that (J*, Q*) is a fixed point of Lµ. To show uniqueness, let (V ′, Q′) be a real-valued fixed point of Lµ, 
i.e., V ′ = MQ′ and Q′ = Fµ(V ′, Q′). Then 
Q′ = Fµ(V ′, Q′) = FQ′, 
where the last equality follows from V ′ = MQ′. Thus Q′ is a fixed point of F , and since Q* is the unique fixed point of F (cf. Prop. 3.6.1), we have Q′ = Q*. It follows that V ′ = MQ* = J*, so (J*, Q*) is the unique fixed point of Lµ within the class of real-valued functions. Q.E.D.
Sec. 3.6 Algorithms 217 
The uniform fixed point property of Lµ just shown is, however, insufficient for the convergence proof of the asynchronous algorithm, in the absence of a contraction property. For this reason, we introduce two mappings L and L that are associated with the mappings Lµ and satisfy 
L(V,Q) ↑ Lµ(V,Q) ↑ L(V,Q), ∀ µ → M. (3.55) 
These are the mappings defined by 
L(V,Q) = 
* MQ, min 
µ→M Fµ(V,Q) 
+ , L(V,Q) = 
* MQ,max 
µ→M Fµ(V,Q) 
+ , 
(3.56) where the min and max over µ are attained in view of the finiteness of M [cf. Assumption 3.6.1(b)]. We will show that L and L also have (J*, Q*) as their unique fixed point. Note that there exists µ̄ that attains the maximum in Eq. (3.56), uniformly for all V and (x, u), namely a policy µ̄ for which 
Q ( x, µ̄(x) 
) = max 
u→U(x) Q(x, u), ∀ x → X, 
[cf. Eq. (3.49)]. Similarly, there exists µ that attains the minimum in Eq. (3.56), uniformly for all V and (x, u). Thus for any given (V,Q), we have 
L(V,Q) = Lµ(V,Q), L(V,Q) = Lµ̄(V,Q), (3.57) 
where µ and µ̄ are some policies. The following proposition shows that (J*, Q*), the common fixed point of the mappings Lµ, for all µ, is also the unique fixed point of L and L. 
Proposition 3.6.3: Let Assumption 3.6.1 hold. Then the mappings L and L of Eq. (3.56) are monotone, and have (J*, Q*) as their unique fixed point within the class of real-valued functions. 
Proof: Monotonicity of L and L follows from the monotonicity of the operators M and Fµ. Since (J*, Q*) is the common fixed point of Lµ for all µ (cf. Prop. 3.6.2), and there exists µ such that L(J*, Q*) = Lµ(J*, Q*) 
[cf. Eq. (3.57)], it follows that (J*, Q*) is a fixed point of L. To show uniqueness, suppose that (V,Q) is a fixed point, so (V,Q) = L(V,Q). Then by Eq. (3.57), we have 
(V,Q) = L(V,Q) = Lµ(V,Q) 
for some µ → M. Since by Prop. 3.6.2, (J*, Q*) is the only fixed point of Lµ, it follows that (V,Q) = (J*, Q*), so (J*, Q*) is the only fixed point of 
L. Similarly, we show that (J*, Q*) is the unique fixed point of L. Q.E.D.
218 Semicontractive Models Chap. 3 
We are now ready to construct a sequence of sets needed to apply Prop. 2.6.1 and prove convergence. For a scalar c ≥ 0, we denote 
J− c = J* − c e, Q− 
c = Q* − c eQ, 
J+ c = J* + c e, Q+ 
c = Q* + c eQ, 
with e and eQ are the unit functions in the spaces of J and Q, respectively. 
Proposition 3.6.4: Let Assumption 3.6.1 hold. Then for all c > 0, 
Lk(J− c , Q− 
c ) ↑ (J*, Q*), L k (J+ 
c , Q+ c ) ↓ (J*, Q*), (3.58) 
where Lk (or L k ) denotes the k-fold composition of L (or L, respec-
tively). 
Proof: For any µ → M, using the assumption (3.48), we have for all (x, u), 
Fµ(J + c , Q+ 
c )(x, u) = H ( x, u,min{J+ 
c , Q+ c } ) 
= H ( x, u,min{J*, Q*}+ c e 
) 
↑ H ( x, u,min{J*, Q*} 
) + c 
= Q*(x, u) + c 
= Q+ c (x, u), 
and similarly Q− 
c (x, u) ↑ Fµ(J − c , Q− 
c )(x, u). 
We also have MQ+ c = J+ 
c and MQ− c = J− 
c . From these relations, the definition of Lµ, and the fact Lµ(J*, Q*) = (J*, Q*) (cf. Prop. 3.6.2), we have 
(J− c , Q− 
c ) ↑ Lµ(J − c , Q− 
c ) ↑ (J*, Q*) ↑ Lµ(J + c , Q+ 
c ) ↑ (J+ c , Q+ 
c ). 
Using this relation and Eqs. (3.55) and (3.57), we obtain 
(J− c , Q− 
c ) ↑ L(J− c , Q− 
c ) ↑ (J*, Q*) ↑ L(J+ c , Q+ 
c ) ↑ (J+ c , Q+ 
c ). (3.59) 
Denote for k = 0, 1, . . . , 
(V k, Qk) = L k (J+ 
c , Q+ c ), (V k, Qk 
) = Lk(J− c , Q− 
c ). 
From the monotonicity of L and L and Eq. (3.59), we have that (V k, Qk) converges monotonically from above to some pair 
(V ,Q) ≥ (J*, Q*),
Sec. 3.7 Notes, Sources, and Exercises 219 
while (V k, Qk ) converges monotonically from below to some pair 
(V ,Q) ↑ (J*, Q*). 
By taking the limit in the equation 
(V k+1, Qk+1) = L(V k, Qk), 
and using the continuity from above and below property of L, implied by Assumption 3.6.1(c), it follows that (V ,Q) = L(V ,Q), so (V ,Q) must 
be equal to (J*, Q*), the unique fixed point of L. Thus, L k (J+ 
c , Q+ c ) ↓ 
(J*, Q*). Similarly, Lk(J− c , Q− 
c ) ↑ (J*, Q*). Q.E.D. 
To show asynchronous convergence of the algorithm (3.50)-(3.51), consider the sets 
S(k) = # (V,Q) | Lk(J− 
c , Q− c ) ↑ (V,Q) ↑ L 
k (J+ 
c , Q+ c ) $ , k = 0, 1, . . . , 
whose intersection is (J*, Q*) [cf. Eq. (3.58)]. By Prop. 3.6.4 and Eq. (3.55), this set sequence together with the mappings Lµ satisfy the synchronous convergence and box conditions of the asynchronous convergence theorem of Prop. 2.6.1 (more precisely, its time-varying version of Exercise 2.2). This proves the convergence of the algorithm (3.50)-(3.51) for starting points (V,Q) → S(0). Since c can be chosen arbitrarily large, it follows that the algorithm is convergent from an arbitrary starting point. 
Finally, let us note some variations of the asynchronous PI algorithm. One such variation is to allow “communication delays” t− τ"j(t). Another variation, for the case where we want to calculate just J*, is to use a reduced space implementation similar to the one discussed in Section 2.6.3. There is also a variant with interpolation, cf. Section 2.6.3. 
3.7 NOTES, SOURCES, AND EXERCISES 
The semicontractive model framework of this chapter was first formulated in the 2013 edition of the book, and it has since been extended through a series of papers and reports by the author: [Ber15], [Ber16a], [BeY16], [Ber17c], [Ber17d], [Ber19c]. The framework is inspired from the analysis of the SSP problem of Example 1.2.6, which involves finite state and control spaces, as well as a termination state. In the absence of a termination state, a key idea has been to generalize the notion of a proper policy from one that leads to termination with probability 1, to one that is S-regular for an appropriate set of functions S. 
Section 3.1: The counterexample showing that J* may fail to solve Bell-man’s equation in SSP problems is due to Bertsekas and Yu [BeY16]. The
220 Semicontractive Models Chap. 3 
blackmailer’s dilemma is a classic problem in the DP literature. The book by Whittle [Whi82] has a substantial discussion. The set of solutions of the Riccati equation in continuous-time linear-quadratic optimal control (cf. Section 3.1.4) has been described in the paper by Willems [Wil71], which stimulated considerable further work on the subject (see the book by Lan-caster and Rodman [LaR95] for an extensive account). The pathologies of infinite horizon linear-quadratic optimal control problems can be largely eliminated under some well-studied controllability and observability conditions (see, e.g., [Ber17a], Section 3.1). 
Section 3.2: The PI-based analysis of Section 3.2 was developed in the author’s paper [Ber15] after the 2013 edition of the book was published. The author’s joint work with H. Yu [BeY16] was also influential. In particular, the SSP example of Section 3.1.2, where J* does not satisfy Bellman’s equation, and the perturbation analysis of Section 3.4 were given in the paper [BeY16]. This is also the source for the convergence rate result of Prop. 3.2.2. The λ-PI method was introduced by Bertsekas and Ioffe [BeI96] in the context of discounted and SSP problems, and subsequent work includes the papers by Nedić and Bertsekas [NeB03], and by Bertsekas, Borkar, and Nedić [BBN04] on the LSPE(λ) method. The analysis of λ-PI in Section 3.2.4 is new and is related to an analysis of a linearized form of the proximal algorithm given in the author’s papers [Ber16b], [Ber18c]. 
Section 3.3: The central result of Section 3.3, Prop. 3.3.1, was given in the 2013 edition of the book. It is patterned after a result of Bertsekas and Tsitsiklis [BeT91] for SSP problems with finite state space and compact control constraint sets, which is reproduced in Section 3.5.1. The proof given there contains an intricate demonstration of a real-valued lower bound on the cost functions of proper policies (Lemma 3 of [BeT91], which implies Prop. 3.5.3). 
Section 3.4: The perturbation approach of Section 3.4 was introduced in the 2013 edition of the book. It is presented here in somewhat stronger form, which will also be applied to nonstationary S-regular policies in the next chapter. 
Section 3.5: The SSP problem analysis of Section 3.5.1 for the case of the strong SSP conditions is due to Bertsekas and Tsitsiklis [BeT91]. For the case of the weak SSP conditions it is due to Bertsekas and Yu [BeY16]. The perturbation-based PI algorithm was given in Section 3.3.3 of the 2013 edition of the book. A different PI algorithm that embodies a mechanism for breaking ties in the policy improvement step was given by Guillot and Stauffer [GuS17] for the case of finite state and control spaces. 
The affine monotonic model of Section 3.5.2 was initially formulated and analyzed in the 2013 edition of the book, in a more general setting where the state space can be an infinite set. The analysis of Section 3.5.2 of the finite-state case comes from the author’s paper [Ber16a], which con-
Sec. 3.7 Notes, Sources, and Exercises 221 
tains more details. The exponentiated cost version of the SSP problem was analyzed in the papers by Denardo and Rothblum [DeR79], and by Patek [Pat01]. The paper [DeR79] assumes that the state and control spaces are finite, that there exists at least one contractive policy (a transient policy in the terminology of [DeR79]), and that every improper policy is noncontractive and has infinite cost from some initial state. These assumptions bypass the pathologies around infinite control spaces and multiple solutions or no solution of Bellman’s equation. Also the approach of [DeR79] is based on linear programming (relying on the finite control space), and is thus quite different from ours. The paper [Pat01] assumes that the state space is finite, that the control constraint set is compact, and that the expected one-stage cost is strictly positive for all state-control pairs, which is much stronger than what we have assumed. Our results of Section 3.5.2, when specialized to the exponential cost problem, are consistent with and subsume the results of Denardo and Rothblum [DeR79], and Patek [Pat01]. 
The discussion on robust shortest path planning in Section 3.5.3 follows the author’s paper [Ber19c]. This paper contains further analysis and computational methods, including a finitely terminating Dijkstra-like algorithm for problems with nonnegative arc lengths. 
The deterministic optimal control model of Section 3.5.5 is discussed in more detail in the author’s paper [Ber17b] under Assumption 3.5.9 for the case where g ≥ 0; see also Section 4.5 and the paper [Ber17c]. The analysis under the more general assumptions given here is new. Deterministic and minimax infinite-spaces optimal control problems have also been discussed by Reissig [Rei16] under assumptions different than ours. 
Section 3.6: The asynchronous VI algorithm of Section 3.6.1 was first given in the author’s paper on distributed DP [Ber82]. It was further formalized in the paper [Ber83], where a DP problem was viewed as a special case of a fixed point problem, involving monotonicity and possibly contraction assumptions. 
The analysis of Section 3.6.2, parallels the one of Section 2.6.3, and is due to joint work of the author with H. Yu, presented in the papers [BeY12] and [YuB13a]. In particular, the algorithm of Section 3.6.2 is one of the optimistic PI algorithms in [YuB13a], which was applied to the SSP problem of Section 3.5.1 under the strong SSP conditions. We have followed the line of analysis of that paper and the related paper [BeY12], which focuses on discounted problems. These papers also analyzed asynchronous stochastic iterative versions of PI, and proved convergence results that parallel those for classical Q-learning for SSP, given in Tsitsiklis [Tsi94], and Yu and Bertsekas [YuB13b]. An earlier paper, which deals with a slightly different asynchronous abstract PI algorithm without a contraction structure, is Bertsekas and Yu [BeY10]. 
By allowing an infinite state space, the analysis of the present chapter applies among others to SSP problems with a countable state space. Such
222 Semicontractive Models Chap. 3 
problems often arise in queueing control settings where the termination state corresponds to an empty queue. The problem then is to empty the queue with minimum expected cost. Generalized forms of SSP problems, which involve an infinite (uncountable) number of states, in addition to the termination state, were analyzed by Pliska [Pli78], Hernandez-Lerma et al. [HCP99], and James and Collins [JaC06]. The latter paper allows improper policies, assumes that g is bounded and J* is bounded below, and generalizes the results of [BeT91] to infinite (Borel) state spaces, using a similar line of proof. Infinite spaces SSP problems will also be discussed in Section 4.6. 
A notable SSP problem with infinite state space arises under imperfect state information. There the problem is converted to a perfect state information problem whose states are belief states, i.e., posterior probability distributions of the original state given the observations thus far. The paper by Patek [Pat07] addresses SSP problems with imperfect state information and proves results that are similar to the ones for their perfect state information counterparts. These results can also be derived using the line of analysis of this chapter. In particular, the critical condition that the cost functions of proper policies are bounded below by some real-valued function [cf. Assumption 3.3.1(b)] is proved as Lemma 5 in [Pat07], using the fact that the cost functions of the proper policies are bounded below by the optimal cost function of a corresponding perfect state information problem. 
E X E R C I S E S 
3.1 (Conditions for J* to be a Fixed Point of T ) 
The purpose of this exercise is to show that the optimal cost function J→ is a fixed point of T under some assumptions, which among others, are satisfied generically in deterministic optimal control problems. Let Π̂ be a subset of policies such that: 
(1) We have (µ,π) → Π̂ if and only if µ → M, π → Π̂, 
where for µ → M and π = {µ0, µ1, . . .}, we denote by (µ, π) the policy {µ, µ0, µ1, . . .}. Note: This condition precludes the possibility that Π̂ is the set of all stationary policies (unless there is only one stationary policy). 
(2) For every π = {µ0, µ1, . . .} → Π̂, we have 
Jπ = Tµ0Jπ1 , 
where π1 is the policy π1 = {µ1, µ2, . . .}.
Sec. 3.7 Notes, Sources, and Exercises 223 
(3) We have inf 
µ∈M,π∈Π̂ TµJπ = inf 
µ∈M TµĴ , 
where the function Ĵ is given by 
Ĵ(x) = inf π∈Π̂ 
Jπ(x), x → X. 
Show that: 
(a) Ĵ is a fixed point of T . In particular, if Π̂ = Π, then J→ is a fixed point of T . 
(b) The assumptions (1)-(3) hold with Π̂ = Π in the case of the deterministic mapping 
H(x, u, J) = g(x, u)+J ( f(x, u) 
) , x → X, u → u(x), J → E(X). (3.60) 
(c) Consider the SSP example of Section 3.1.2, where J→ is not a fixed point of T . Which of the conditions (1)-(3) is violated? 
Solution: (a) For every x → X, we have 
Ĵ(x) = inf π∈Π̂ 
Jπ(x) = inf µ∈M, π∈Π̂ 
(TµJπ)(x) = inf µ∈M 
(TµĴ)(x) = (T Ĵ)(x), 
where the second equality holds by conditions (1) and (2), and the third equality holds by condition (3). 
(b) This is evident in the case of the deterministic mapping (3.60). Notes: (i) If Π̂ = Π, parts (a) and (b) show that J→, which is equal to Ĵ , is a fixed point of T . Moreover, if we choose a set S such that J→ 
S can be shown to be equal to J→, then Prop. 3.2.1 applies and shows that J→ is the unique fixed point of T with the set 
# J → E(X) | J→ 
S ≤ J ≤ J̃ $ 
for some J̃ → S. In addition the VI 
sequence {T kJ} converges to J→ starting from every J within that set. (ii) The assumptions (1)-(3) of this exercise also hold for other choices of Π̂. For example, when Π̂ is the set of all eventually stationary policies, i.e., policies of the form {µ0, . . . , µk, µ, µ, . . .}, where µ0, . . . , µk, µ → M and k is some positive integer. 
(c) For the SSP problem of Section 3.1.1, condition (2) of the preceding proposition need not be satisfied (because the expected value operation need not commute with lim sup). 
3.2 (Alternative Semicontractive Conditions I) 
This exercise provides a different starting point for the semicontractive analysis of Section 3.2. In particular, the results of Prop. 3.2.1 are shown without assuming that J→ 
S is a fixed point of T , but by making different assumptions, which include the existence of an S-regular policy that is optimal. Let S be a given subset of E(X). Assume that:
224 Semicontractive Models Chap. 3 
(1) There exists an S-regular policy µ→ that is optimal, i.e., Jµ→ = J→. 
(2) The policy µ→ satisfies Tµ→J → = TJ→. 
Show that the following hold: 
(a) The optimal cost function J→ is the unique fixed point of T within the set {J → S | J ↓ J→}. 
(b) We have T kJ → J→ for every J → S with J ↓ J→. 
(c) An S-regular policy µ that satisfies TµJ → = TJ→ is optimal. Conversely if 
µ is an S-regular optimal policy, it satisfies TµJ → = TJ→. 
Note: Part (a) and the assumptions show that J→ S is a fixed point of T (as well 
as that J→ S = J→ → S), so parts (b) and (c) also follow from Prop. 3.2.1. 
Solution: (a) We first show that any fixed point J of T that lies in S satisfies J ≤ J→. Indeed, if J = TJ , then for the optimal S-regular policy µ→, we have J ≤ Tµ→J , so in view of the monotonicity of Tµ→ and the S-regularity of µ→, 
J ≤ lim k↓∞ 
T k µ→J = Jµ→ = J→. 
Thus the only function within {J → S | J ↓ J→} that can be a fixed point of T is J→. Using the optimality and S-regularity of µ→, and condition (2), we have 
J→ = Jµ→ = Tµ→Jµ→ = Tµ→J → = TJ→, 
so J→ is a fixed point of T . Finally, J→ → S since J→ = Jµ→ and µ→ is S-regular, so J→ is the unique fixed point of T within {J → S | J ↓ J→}. 
(b) For the optimal S-regular policy µ→ and any J → S with J ↓ J→, we have 
T k µ→J ↓ T kJ ↓ T kJ→ = J→, k = 0, 1, . . . . 
Taking the limit as k → ∞, and using the fact limk↓∞ T k µ→J = Jµ→ = J→, which 
holds since µ→ is S-regular and optimal, we see that T kJ → J→. 
(c) If µ satisfies TµJ → = TJ→, then using part (a), we have TµJ 
→ = J→ and hence limk↓∞ T k 
µJ → = J→. If µ is in addition S-regular, then Jµ = limk↓∞ T k 
µJ → = J→ 
and µ is optimal. Conversely, if µ is optimal and S-regular, then Jµ = J→ and Jµ = TµJµ, which combined with J→ = TJ→ [cf. part (a)], yields TµJ 
→ = TJ→. 
3.3 (Alternative Semicontractive Conditions II) 
Let S be a given subset of E(X). Show that the assumptions of Exercise 3.2 hold if and only if J→ → S, TJ→ ≤ J→, and there exists an S-regular policy µ such that TµJ 
→ = TJ→. 
Solution: Let the conditions (1) and (2) of Exercise 3.2 hold, and let µ→ be the S-regular policy that is optimal. Then condition (1) implies that J→ = Jµ→ → S and J→ = Tµ→J 
→ ↓ TJ→, while condition (2) implies that there exists an S-regular policy µ such that TµJ 
→ = TJ→.
Sec. 3.7 Notes, Sources, and Exercises 225 
Conversely, assume that J→ → S, TJ→ ≤ J→, and there exists an S-regular policy µ such that TµJ→ = TJ→. Then we have TµJ→ = TJ→ ≤ J→. Hence T k µJ 
→ ≤ J→ for all k, and by taking the limit as k → ∞, we obtain Jµ ≤ J→. Hence the S-regular policy µ is optimal, and the conditions of Exercise 3.2 hold. 
3.4 (Alternative Semicontractive Conditions III) 
Let S be a given subset of E(X). Assume that: 
(1) There exists an optimal S-regular policy. 
(2) For every S-irregular policy µ, we have TµJ → ↓ J→. 
Show that the assumptions of Exercise 3.2 hold. 
Solution: It will be sufficient to show that conditions (1) and (2) imply that J→ = TJ→. Assume to obtain a contradiction, that J→ &= TJ→. Then J→ ↓ TJ→, as can be seen from the relations 
J→ = Jµ→ = Tµ→Jµ→ ↓ TJµ→ = TJ→, 
where µ→ is an optimal S-regular policy. Thus the relation J→ &= TJ→ implies that there exists µ′ and x → X such that 
J→(x) ↓ (Tµ′J →)(x), ∀ x → X, 
with strict inequality for some x [note here that we can choose µ(x) = µ→(x) for all x such that J→(x) = (TJ→)(x), and we can choose µ(x) to satisfy J→(x) > (TµJ 
→)(x) for all other x]. If µ were S-regular, we would have 
J→ ↓ TµJ → ↓ lim 
k↓∞ T k µJ 
→ = Jµ′ , 
with strict inequality for some x → X, which is impossible. Hence µ′ is S-irregular, which contradicts condition (2). 
3.5 (Restricted Optimization over a Subset of S-Regular Policies) 
This exercise provides a useful extension of Prop. 3.2.1. Given a set S, it may be 
more convenient to work with a subset !M ⊂ MS . Let Ĵ denote the corresponding restricted optimal value: 
Ĵ(x) = inf µ∈ "M 
Jµ(x), 
and assume that Ĵ is a fixed point of T . Show that the following analogs of the conclusions of Prop. 3.2.1 hold: 
(a) (Uniqueness of Fixed Point) If J ′ is a fixed point of T and there exists 
J̃ → S such that J ′ ≤ J̃ , then J ′ ≤ Ĵ . In particular, if the set "W given by 
"W = # J → E(X) | Ĵ ≤ J ≤ J̃ for some J̃ → S 
$ ,
226 Semicontractive Models Chap. 3 
is nonempty, then Ĵ is the unique fixed point of T within "W. 
(b) (VI Convergence) We have T kJ → Ĵ for every J → "W . 
Solution: The proof is nearly identical to the one of Prop. 3.2.1. Let J → "W, so that 
Ĵ ≤ J ≤ J̃ 
for some J̃ → S. We have for all k ↓ 1 and µ → !M, 
Ĵ = T kĴ ≤ T kJ ≤ T kJ̃ ≤ T k µ J̃ , 
where the equality follows from the fixed point property of Ĵ , while the inequalities follow by using the monotonicity and the definition of T . The right-hand side tends to Jµ as k → ∞, since µ is S-regular and J̃ → S. Hence the infimum 
over µ → !M of the limit of the right-hand side tends to the left-hand side Ĵ . It follows that T kJ → Ĵ , proving part (b). To prove part (a), let J ′ be a fixed 
point of T that belongs to "W. Then J ′ is equal to limk↓∞ T kJ ′, which has been proved to be equal to Ĵ . 
3.6 (The Case J∗ S ↑ J̄) 
Within the framework of Section 3.2, assume that J→ S ≤ J̄ . (This occurs in 
particular in the monotone decreasing model where J̄ ↓ TµJ̄ for all µ → M; see Section 4.3.) Show that if J→ 
S is a fixed point of T , then we have J→ S = J→. Note: 
This result manifests itself in the shortest path Example 3.2.1 for the case where b < 0. 
Solution: For all k and policies π = {µ0, µ1, . . .}, we have 
J→ S = lim 
k↓∞ T kJ→ 
S ≤ lim sup k↓∞ 
T kJ̄ ≤ lim sup k↓∞ 
Tµ0 · · ·Tµk−1 J̄ = Jπ , 
and by taking the infimum over π → Π, we obtain J→ S ≤ J→. Since generically we 
have J→ S ↓ J→, it follows that J→ 
S = J→. 
3.7 (Weakening the Near-Optimal Termination Assumption) 
Consider the deterministic optimal control problem of Section 3.5.5. The purpose of this exercise is to show that the Assumption 3.5.9 is equivalent to a seemingly weaker assumption where nonstationary policies can be used for termination. Given a state x → X→, we say that a (possibly nonstationary) policy π → Π terminates from x if the sequence {xk}, which is generated starting from x and using π, reaches X0 in the sense that xk̄ → X0 for some index k̄. Assume that for every x → X→, there exists a policy π → Π that terminates from x. Show that: 
(a) The set !M of terminating stationary policies is nonempty, i.e., there exists a stationary policy that terminates from every x → X→.
Sec. 3.7 Notes, Sources, and Exercises 227 
(b) Assumption 3.5.9 is satisfied if for every pair (x, ε) with x → X→ and ε > 0, there exists a policy π → Π that terminates from x and satisfies Jπ(x) ≤ J→(x) + ε. 
Solution: (a) Consider the sequence of subsets of X defined for k = 0, 1, . . . , by 
Xk = {x → X→ | there exists π → Π that terminates from x in k steps or less}, 
starting with the stopping set X0. Note that ∪∞ k=0Xk = X→. Define a stationary 
policy µ̄ as follows: For each x → Xk with x /→ Xk−1, let {µ0, µ1, . . .} be a policy that terminates from x in the minimum possible number of steps (which is k), and let µ̄ = µ0. For each x /→ X→, let µ̄(x) be an arbitrary control in U(x). It can be seen that µ̄ is a terminating stationary policy. 
(b) Given any state x̄ → X→ with x̄ /→ X0, and a nonstationary policy π = {µ0, µ1, . . .} that terminates from x̄, we construct a stationary policy µ that terminates from every x → X→ and generates essentially the same trajectory as π starting from x̄ (i.e., after cycles are subtracted). To construct such a µ, we consider the sequence generated by π starting from x̄. If this sequence contains cycles, we shorten the sequence by eliminating the cycles, and we redefine π so that starting from x̄ it generates a terminating trajectory without cycles. This redefined version of π, denoted π′ = {µ′ 
0, µ ′ 1, . . .}, terminates from x̄ and has cost 
Jπ′(x̄) ≤ Jπ(x̄) [since all the eliminated transitions that belonged to cycles have nonnegative cost, in view of the fact J→(x) > −∞ for all x, which is implied by Assumption 3.5.9]. We now consider the sequence of subsets of X defined by 
Xk = {x → X | π′ terminates from x in k steps or less}, k = 0, 1, . . . , 
where X0 is the stopping set. Let k̄ be the first k ↓ 1 such that x̄ → Xk. Construct the stationary policy µ as follows: for x → ∪k̄ 
k=1Xk, let 
µ(x) = µ′ k̄−k(x), if x → Xk and x /→ Xk−1, k = 1, 2, . . . , 
and for x /→ ∪k̄ k=1Xk, let µ(x) = µ̄(x), where µ̄ is a stationary policy that termi-
nates from every x → X→ [and was shown to exist in part (a)]. Then it is seen that µ terminates from every x → X→, and generates the same sequence as π′ 
starting from the state x̄, so it satisfies Jµ(x̄) = Jπ′(x̄) ≤ Jπ(x̄). 
3.8 (Verifying the Near-Optimal Termination Assumption) 
In the context of the deterministic optimal control problem of Section 3.5.5, assume that X is a normed space with norm denoted ‖ · ‖. We say that π asymptotically terminates from x if the sequence {xk} generated starting from x and using π converges to X0 in the sense that 
lim k↓∞ 
dist(xk, X0) = 0, 
where dist(x,X0) denotes the minimum distance from x to X0, 
dist(x,X0) = inf y∈X0 
‖x− y‖, x → X.
228 Semicontractive Models Chap. 3 
The purpose of this exercise is to provide a readily verifiable condition that guarantees Assumption 3.5.9. Assume that 
0 ≤ g(x,u), x → X, u → U(x), 
and that J→(x) > 0, ∀ x /→ X0. 
Assume further the following: 
(1) For every x → X→ = # x → X | J→(x) < ∞ 
$ and ε > 0, there exits a policy 
π that asymptotically terminates from x and satisfies Jπ(x) ≤ J→(x) + ε. 
(2) For every ε > 0, there exists a δε > 0 such that for each x → X→ with 
dist(x,X0) ≤ δε, 
there is a policy π that terminates from x and satisfies Jπ(x) ≤ ε. 
Then: 
(a) Show that Assumption 3.5.9 holds. 
(b) Show that condition (1) holds if for each δ > 0 there exists ε > 0 such that 
inf u∈U(x) 
g(x, u) ↓ ε, ∀ x → X such that dist(x,X0) ↓ δ. 
Note: For further discussion, analysis, and application to the case of a linear system, see the author’s paper [Ber17b]. 
Solution: (a) Fix x → X→ and ε > 0. Let π be a policy that asymptotically terminates from x, and satisfies Jπ(x) ≤ J→(x)+ ε, as per condition (1). Starting from x, this policy will generate a sequence {xk} such that for some index k̄ we have dist(xk̄, X0) ≤ δε, so by condition (2), there exists a policy π̄ that terminates from xk̄ and is such that Jπ̄(xk̄) ≤ ε. Consider the policy π′ that follows π up to index k̄ and follows π̄ afterwards. This policy terminates from x and satisfies 
Jπ′(x) = Jπ,k̄(x) + Jπ̄(xk̄) ≤ Jπ(x) + Jπ̄(xk̄) ≤ J→(x) + 2ε, 
where Jπ,k̄(x) is the cost incurred by π starting from x up to reaching xk̄. From Exercise 3.7 it follows that Assumption 3.5.9 holds. 
(b) For any x and policy π that does not asymptotically terminate from x, we will have Jπ(x) = ∞, so that if x → X→, all policies π with Jπ(x) < ∞ must be asymptotically terminating from x. 
3.9 (Perturbations and S-Regular Policies) 
The purpose of this exercise is to illustrate that the set of S-regular policies may be different in the perturbed and unperturbed problems of Section 3.4. Consider a single-state problem with J̄ = 0 and two policies µ and µ′, where 
TµJ = min{1, J}, Tµ′J = β > 0.
Sec. 3.7 Notes, Sources, and Exercises 229 
Let S = ,. 
(a) Verify that µ is S-irregular and Jµ = J→ = 0. 
(b) Verify that µ′ is S-regular and Jµ′ = J→ S = β. 
(c) For δ > 0 consider the δ-perturbed problem with p(x) = 1, where x is the only state. Show that both µ and µ′ are S-regular for this problem. Moreover, we have Ĵδ = min{1, β}+ δ. 
(d) Verify that Prop. 3.4.1 applies for !M = {µ′} and β ≤ 1, but does not 
apply if !M = {µ, µ′} or β > 1. Which assumptions of the proposition are violated in the latter case? 
Solution: Parts (a) and (b) are straightforward. It is also straightforward to verify the definition of S-regularity for both policies in the δ-perturbed problem, and that Jµ,δ = 1 + δ and Jµ′,δ = β + δ. If β ≤ 1, the policy µ′ is optimal 
for the δ-perturbed problem, and Prop. 3.4.1 applies for !M = {µ′} because all 
its assumptions are satisfied. However, when β > 1 and !M = {µ′} there is no 
ε-optimal policy in !M for the δ-perturbed problem (contrary to the assumption 
of Prop. 3.4.1), and indeed we have β = J→ S > limδ↓0 Ĵδ = 1. Also when !M = 
{µ, µ′}, the policy µ is not S-regular, contrary to the assumption of Prop. 3.4.1. 
3.10 (Perturbations in Affine Monotonic Models [Ber16a]) 
Consider the affine monotonic model of Section 3.5.2, and let Assumptions 3.5.5 and 3.5.6 hold. In a perturbed version of this model we add a constant δ > 0 to all components of bµ, thus obtaining what we call the δ-perturbed affine monotonic 
problem. We denote by Ĵδ and Jµ,δ the corresponding optimal cost function and policy cost functions, respectively. 
(a) Show that for all δ > 0, Ĵδ is the unique solution within ,n + of the equation 
J(i) = (TJ)(i) + δ, i = 1, . . . , n. 
(b) Show that for all δ > 0, a policy µ is optimal for the δ-perturbed problem (i.e., Jµ,δ = Ĵδ) if and only if TµĴδ = T Ĵδ. Moreover, for the δ-perturbed problem, all optimal policies are contractive and there exists at least one contractive policy that is optimal. 
(c) The optimal cost function over contractive policies Ĵ [cf. Eq. (3.37)] satisfies 
Ĵ(i) = lim δ↓0 
Ĵδ(i), i = 1, . . . , n. 
(d) If the control constraint set U(i) is finite for all states i = 1, . . . , n, there exists a contractive policy µ̂ that attains the minimum over all contractive policies, i.e., Jµ̂ = Ĵ . 
(e) Show Prop. 3.5.8.
230 Semicontractive Models Chap. 3 
Solution: (a), (b) By Prop. 3.5.6, we have that Assumption 3.3.1 holds for the δ-perturbed problem. The results follow by applying Prop. 3.5.7 [the equation of part (a) is Bellman’s equation for the δ-perturbed problem]. 
(c) For an optimal contractive policy µ→ δ of the δ-perturbed problem [cf. part (b)], 
we have 
Ĵ = inf µ: contractive 
Jµ ≤ Jµ→ δ ≤ Jµ→ 
δ ,δ = Ĵδ ≤ Jµ′,δ, ∀ µ′ : contractive. 
Since for every contractive policy µ′, we have limδ↓0 Jµ′,δ = Jµ′ , it follows that 
Ĵ ≤ lim δ↓0 
Ĵδ ≤ Jµ′ , ∀ µ′ : contractive. 
By taking the infimum over all µ′ that are contractive, the result follows. 
(d) Let {δk} be a positive sequence with δk ↓ 0, and consider a corresponding sequence {µk} of optimal contractive policies for the δk-perturbed problems. Since the set of contractive policies is finite [in view of the finiteness of U(i)], some policy µ̂ will be repeated infinitely often within the sequence {µk}, and since {J→ 
δk } is monotonically nonincreasing, we will have 
Ĵ ≤ Jµ̂ ≤ J→ δk , 
for all k sufficiently large. Since by part (c), J→ δk 
↓ Ĵ , it follows that Jµ̂ = Ĵ . 
(e) For all contractive µ, we have Jµ = TµJµ ↓ TµĴ ↓ T Ĵ. Taking the infimum over contractive µ, we obtain Ĵ ↓ T Ĵ. Conversely, for all δ > 0 and µ → M, we have 
Ĵδ = T Ĵδ + δe ≤ TµĴδ + δe. 
Taking limit as δ ↓ 0, and using part (c), we obtain Ĵ ≤ TµĴ for all µ → M. Taking infimum over µ → M, it follows that Ĵ ≤ T Ĵ . Thus Ĵ is a fixed point of T . 
For all J → ,n with J ↓ Ĵ and contractive µ, we have by using the relation Ĵ = T Ĵ just shown, 
Ĵ = lim k↓∞ 
T kĴ ≤ lim k↓∞ 
T kJ ≤ lim k↓∞ 
T k µJ = Jµ. 
Taking the infimum over all contractive µ, we obtain 
Ĵ ≤ lim k↓∞ 
T kJ ≤ Ĵ , ∀ J ↓ Ĵ . 
This proves that T kJ → Ĵ . Finally, let J ′ → R(X) be another solution of Bellman’s equation, and let J → R(X) be such that J ↓ Ĵ and J ↓ J ′. Then T kJ → Ĵ , while T kJ ↓ T kJ ′ = J ′. It follows that Ĵ ↓ J ′. 
To prove Prop. 3.5.8(c) note that if µ is a contractive policy with Jµ = Ĵ , we have Ĵ = Jµ = TµJµ = TµĴ , so, using also the relation Ĵ = T Ĵ [cf. part (a)], we obtain TµĴ = T Ĵ . Conversely, if µ satisfies TµĴ = T Ĵ , then from part (a), we have TµĴ = Ĵ and hence limk↓∞ T k 
µ Ĵ = Ĵ . Since µ is contractive, we obtain 
Jµ = limk↓∞ T k µ Ĵ , so Jµ = Ĵ . 
The proof of Prop. 3.5.8(d) is nearly identical to the one of Prop. 3.5.4(d).
4 Noncontractive Models 
Contents 
4.1. Noncontractive Models - Problem Formulation . . . . p. 233 4.2. Finite Horizon Problems . . . . . . . . . . . . . . p. 235 4.3. Infinite Horizon Problems . . . . . . . . . . . . . p. 241 
4.3.1. Fixed Point Properties and Optimality Conditions p. 244 4.3.2. Value Iteration . . . . . . . . . . . . . . . . p. 256 4.3.3. Exact and Optimistic Policy Iteration - . . . . . . . . 
!-Policy Iteration . . . . . . . . . . . . . . p. 260 4.4. Regularity and Nonstationary Policies . . . . . . . . p. 265 
4.4.1. Regularity and Monotone Increasing Models . . . p. 271 4.4.2. Nonnegative Cost Stochastic Optimal Control . . p. 273 4.4.3. Discounted Stochastic Optimal Control . . . . . p. 276 4.4.4. Convergent Models . . . . . . . . . . . . . . p. 278 
4.5. Stable Policies for Deterministic Optimal Control . . . p. 282 4.5.1. Forcing Functions and p-Stable Policies . . . . . p. 286 4.5.2. Restricted Optimization over Stable Policies . . . p. 289 4.5.3. Policy Iteration Methods . . . . . . . . . . . p. 301 
4.6. Infinite-Spaces Stochastic Shortest Path Problems . . . p. 307 4.6.1. The Multiplicity of Solutions of Bellman’s Equation p. 315 4.6.2. The Case of Bounded Cost per Stage . . . . . . p. 317 
4.7. Notes, Sources, and Exercises . . . . . . . . . . . . p. 320 
231
232 Noncontractive Models Chap. 4 
In this chapter, we consider abstract DP models that are similar to the ones of the earlier chapters, but we do not assume any contraction-like property. We discuss both finite and infinite horizon models, and introduce just enough assumptions (including monotonicity) to obtain some minimal results, which we will strengthen as we go along. 
In Section 4.2, we consider a general type of finite horizon problem. Under some reasonable assumptions, we show the standard results that one may expect in an abstract setting. 
In Section 4.3, we discuss an infinite horizon problem that is motivated by the well-known positive and negative DP models (see [Ber12a], Chapter 4). These are the special cases of the infinite horizon stochastic optimal control problem of Example 1.2.1, where the cost per stage g is uniformly nonpositive or uniformly nonnegative. For these models there is interesting theory (the validity of Bellman’s equation and the availability of optimality conditions in a DP context), which originated with the works of Blackwell [Bla65b] and Strauch [Str66], and is discussed in Section 4.3.1. There are also interesting computational methods, patterned after the VI and PI algorithms, which are discussed in Sections 4.3.2 and 4.3.3. How-ever, the performance guarantees for these methods are not as powerful as in the contractive case, and their validity hinges upon certain additional assumptions. 
In Section 4.4, we extend the notion of regularity of Section 3.2 so that it applies more broadly, including situations where nonstationary policies need to be considered. The mathematical reason for considering nonstationary policies is that for some of the noncontractive models of Section 4.3, stationary policies are insu!cient in the sense that there may not exist "-optimal policies that are stationary. In this section, we also discuss some applications, including some general types of optimal control problems with nonnegative cost per stage. Principal results here are that J* is the unique solution of Bellman’s equation within a certain class of functions, and other related results regarding the convergence of the VI algorithm. 
In Section 4.5, we discuss a nonnegative cost deterministic optimal control problem, which combines elements of the noncontractive models of Section 4.3, and the semicontractive models of Chapter 3 and Section 4.4. Within this setting we explore the structure and the multiplicity of solutions of Bellman’s equation. We draw inspiration from the analysis of Section 4.4, but we also use a perturbation-based line of analysis, similar to the one of Section 3.4. In particular, our starting point is a perturbed version of the mapping Tµ that defines the “stable” policies, in place of a subset S that defines the S-regular policies. Still with a proper definition of S, the “stable” policies are S-regular. 
Finally, in Section 4.6, we extend the ideas of Section 4.5 to stochastic optimal control problems, by generalizing the notion of a proper policy to the case of infinite state and control spaces. This analysis is considerably more complex than the finite-spaces SSP analysis of Section 3.5.1.
Sec. 4.1 Noncontractive Models - Problem Formulation 233 
4.1 NONCONTRACTIVE MODELS - PROBLEM FORMULATION 
Throughout this chapter we will continue to use the model of Section 3.2, which involves the set of extended real numbers !! = ! " {#,$#}. To repeat some of the basic definitions, we denote by E(X) the set of all extended real-valued functions J : X %& !!, by R(X) the set of realvalued functions J : X %& !, and by B(X) the set of real-valued functions J : X %& ! that are bounded with respect to a given weighted sup-norm. 
We have a set X of states and a set U of controls, and for each x ' X , the nonempty control constraint set U(x) ( U . We denote by M the set of all functions µ : X %& U with µ(x) ' U(x), for all x ' X , and by " the set of “nonstationary policies” # = {µ0, µ1, . . .}, with µk ' M for all k. We refer to a stationary policy {µ, µ, . . .} simply as µ. 
We introduce a mapping H : X )U ) E(X) %& !!, and we define the mapping T : E(X) %& E(X) by 
(TJ)(x) = inf u"U(x) 
H(x, u, J), * x ' X, J ' E(X), 
and for each µ ' M the mapping Tµ : E(X) %& E(X) by 
(TµJ)(x) = H ! x, µ(x), J 
" , * x ' X, J ' E(X). 
We continue to use the following assumption throughout this chapter, without mentioning it explicitly in various propositions. 
Assumption 4.1.1: (Monotonicity) If J, J # ' E(X) and J + J #, then 
H(x, u, J) + H(x, u, J #), * x ' X, u ' U(x). 
A fact that we will be using frequently is that for each J ' E(X) and scalar " > 0, there exists a µ! ' M such that for all x ' X , 
(Tµ!J)(x) + 
# $ 
% (TJ)(x) + " if (TJ)(x) > $#, 
$(1/") if (TJ)(x) = $#. 
In particular, if J is such that 
(TJ)(x) > $#, * x ' X, 
then for each " > 0, there exists a µ! ' M such that 
(Tµ!J)(x) + (TJ)(x) + ", * x ' X.
234 Noncontractive Models Chap. 4 
We will often use in our analysis the unit function e, defined by e(x) , 1, so for example, we write the preceding relation in shorthand as 
Tµ!J + TJ + " e. 
We define cost functions for policies consistently with Chapters 2 and 3. In particular, we are given a function J̄ ' E(X), and we consider for every policy # = {µ0, µ1, . . .} ' " and positive integer N the function JN," ' E(X) defined by 
JN,"(x) = (Tµ0 · · ·TµN!1 J̄)(x), * x ' X, 
and the function J" ' E(X) defined by 
J"(x) = lim sup k$% 
(Tµ0 · · ·Tµk J̄)(x), * x ' X. 
We refer to JN," as the N -stage cost function of # and to J" as the infinite horizon cost function of # (or just “cost function” if the length of the horizon is clearly implied by the context). For a stationary policy # = {µ, µ, . . .} we also write J" as Jµ. 
In Section 4.2, we consider the N -stage optimization problem 
minimize JN,"(x) 
subject to # ' ", (4.1) 
while in Sections 4.3 and 4.4 we discuss its infinite horizon version 
minimize J"(x) 
subject to # ' ". (4.2) 
For a fixed x ' X , we denote by J* N (x) and J*(x) the optimal costs 
for these problems, i.e., 
J* N (x) = inf 
""! JN,"(x), J*(x) = inf 
""! J"(x), * x ' X. 
We say that a policy #! ' " is N -stage optimal if 
JN,""(x) = J* N (x), * x ' X, 
and (infinite horizon) optimal if 
J""(x) = J*(x), * x ' X. 
For a given " > 0, we say that #! is N -stage "-optimal if 
JN,"!(x) + 
# $ 
% J* N (x) + " if J* 
N (x) > $#, 
$(1/") if J* N (x) = $#, 
and we say that #! is "-optimal if 
J"!(x) + 
# $ 
% J*(x) + " if J*(x) > $#, 
$(1/") if J*(x) = $#.
Sec. 4.2 Finite Horizon Problems 235 
4.2 FINITE HORIZON PROBLEMS 
Consider the N -stage problem (4.1), where the cost function JN," is defined by 
JN,"(x) = (Tµ0 · · ·TµN!1 J̄)(x), * x ' X. 
Based on the theory of finite horizon DP, we expect that (at least under some conditions) the optimal cost function J* 
N is obtained by N successive applications of the DP mapping T on the initial function J̄ , i.e., 
J* N = inf 
""! JN," = TN J̄ . 
This is the analog of Bellman’s equation for the finite horizon problem in a DP context. 
The Case Where Uniformly N-Stage Optimal Policies Exist 
A favorable case where the analysis is simplified and we can easily show that J* N = TN J̄ is when the finite horizon DP algorithm yields an optimal policy 
during its execution. By this we mean that the algorithm that starts with J̄ , and sequentially computes T J̄, T 2J̄ , . . . , TN J̄ , also yields corresponding µ! N&1, µ 
! N&2, . . . , µ 
! 0 ' M such that 
Tµ" k TN&k&1J̄ = TN&kJ̄ , k = 0, . . . , N $ 1. (4.3) 
While µ! N&1, . . . , µ 
! 0 ' M satisfying this relation need not exist (because 
the corresponding infimum in the definition of T is not attained), if they do exist, they both form an optimal policy and also guarantee that 
J* N = TN J̄ . 
The proof is simple: we have for every # = {µ0, µ1, . . .} ' " 
JN," = Tµ0 · · ·TµN!1 J̄ - TN J̄ = Tµ" 0 · · ·Tµ" 
N!1 J̄ , (4.4) 
where the inequality follows from the monotonicity assumption and the definition of T , and the last equality follows from Eq. (4.3). Thus {µ! 
0, µ ! 1, . . .} 
has no worse N -stage cost function than every other policy, so it is N -stage optimal and J* 
N = Tµ" 0 · · ·Tµ" 
N!1 J̄ . By taking the infimum of the left-hand 
side over # ' " in Eq. (4.4), we obtain J* N = TN J̄ . 
The preceding argument can also be used to show that {µ! k, µ 
! k+1, . . .} 
is (N $ k)-stage optimal for all k = 0, . . . , N $ 1. Such a policy is called uniformly N -stage optimal . The fact that the finite horizon DP algorithm provides an optimal solution of all the k-stage problems for k = 1, . . . , N , rather than just the last one, is a manifestation of the classical principle
236 Noncontractive Models Chap. 4 
of optimality, expounded by Bellman in the early days of DP (the tail portion of an optimal policy obtained by DP minimizes the corresponding tail portion of the finite horizon cost). Note, however, that there may exist an N -stage optimal policy that is not k-stage optimal for some k < N . 
We state the result just derived as a proposition. 
Proposition 4.2.1: Suppose that a policy {µ! 0, µ 
! 1, . . .} satisfies the 
condition (4.3). Then this policy is uniformly N -stage optimal, and we have J* 
N = TN J̄ . 
While the preceding result is theoretically limited, it is very useful in practice, because the existence of a policy satisfying the condition (4.3) can often be established with a simple analysis. For example, this condition is trivially satisfied if the control space is finite. The following proposition provides a generalization. 
Proposition 4.2.2: Let the control space U be a metric space, and assume that for each x ' X , ! ' !, and k = 0, 1, . . . , N $ 1, the set 
Uk(x,!) = & u ' U(x) | H(x, u, T kJ̄) + ! 
' 
is compact. Then there exists a uniformly N -stage optimal policy. 
Proof: We will show that the infimum in the relation 
(T k+1J̄)(x) = inf u"U(x) 
H ! x, u, T kJ̄ 
" 
is attained for all x ' X and k. Indeed if H ! x, u, T kJ̄ 
" = # for all 
u ' U(x), then every u ' U(x) attains the infimum. If for a given x ' X , 
inf u"U(x) 
H ! x, u, T kJ̄ 
" < #, 
the corresponding part of the proof of Lemma 3.3.1 applies and shows that the above infimum is attained. The result now follows from Prop. 4.2.1. Q.E.D. 
The General Case 
We now consider the case where there may not exist a uniformly N -stage optimal policy. By using the definitions of J! 
N and TN J̄ , the equation
Sec. 4.2 Finite Horizon Problems 237 
J! N = TN J̄ , which we want to prove, can be equivalently written as 
inf µ0,...,µN!1#M 
Tµ0 · · ·TµN!1 J̄ = inf µ0#M 
Tµ0 
( inf 
µ1#M Tµ1 
( · · · inf 
µN!1#M TµN!1 J̄ 
)) . 
Thus we have J! N = TN J̄ if the operations inf and Tµ can be interchanged 
in the preceding equation. We will introduce two alternative assumptions, which guarantee that this interchange is valid. Our first assumption is a form of continuity from above of H with respect to J . 
Assumption 4.2.1: For each sequence {Jm} ( E(X) with Jm . J and H(x, u, J0) < # for all x ' X and u ' U(x), we have 
lim m$% 
H(x, u, Jm) = H(x, u, J), * x ' X, u ' U(x). (4.5) 
Note that if {Jm} is monotonically nonincreasing, the same is true for {TµJm}. It follows that 
inf m 
Jm = lim m$% 
Jm, inf m 
(TµJm) = lim m$% 
(TµJm), 
so for all µ ' M, Eq. (4.5) implies that 
inf m 
(TµJm) = lim m$% 
(TµJm) = Tµ 
* lim 
m$% Jm + = Tµ 
* inf m 
Jm + . 
This equality can be extended for any µ1, . . . , µk ' M as follows: 
inf m 
(Tµ1 · · ·Tµk Jm) = Tµ1 
* inf m 
(Tµ1 · · ·Tµk Jm) 
+ 
= · · · 
= Tµ1Tµ1 · · ·Tµk!1 
* inf m 
(Tµk Jm) 
+ 
= Tµ1 · · ·Tµk 
* inf m 
Jm + . 
(4.6) 
We use this relation to prove the following proposition. 
Proposition 4.2.3: Let Assumption 4.2.1 hold, and assume further that Jk,"(x) < #, for all x ' X , # ' ", and k - 1. Then J* 
N = TN J̄ . 
Proof: We select for each k = 0, . . . , N $ 1, a sequence {µm k } ( M such 
that lim 
m$% Tµm 
k (TN&k&1J̄) . TN&kJ̄ .
238 Noncontractive Models Chap. 4 
Since J! N + Tµ0 · · ·TµN!1 J̄ for all µ0, . . . , µN&1 ' M, we have using also 
Eq. (4.6) and the assumption Jk,"(x) < #, for all k, #, and x, 
J! N + inf 
m0 · · · inf 
mN!1 Tµ 
m0 0 
· · ·T µ mN!1 N!1 
J̄ 
= inf m0 
· · · inf mN!2 
Tµ m0 0 
· · ·T µ mN!2 N!2 
( inf 
mN!1 T µ mN!1 N!1 
J̄ 
) 
= inf m0 
· · · inf mN!2 
Tµ m0 0 
· · ·T µ mN!2 N!2 
T J̄ 
... 
= inf m0 
Tµ m0 0 
(TN&1J̄) 
= TN J̄ . 
On the other hand, it is clear from the definitions that TN J̄ + JN," for all N and # ' ", so that TN J̄ + J* 
N . Thus, J* N = TN J̄ . Q.E.D. 
We now introduce an alternative assumption, which in addition to J* N = TN J̄ , guarantees the existence of an "-optimal policy. 
Assumption 4.2.2: We have 
J* k (x) > $#, * x ' X, k = 1, . . . , N. 
Moreover, there exists a scalar $ ' (0,#) such that for all scalars r ' (0,#) and functions J ' E(X), we have 
H(x, u, J + r e) + H(x, u, J) + $ r, * x ' X, u ' U(x). (4.7) 
Proposition 4.2.4: Let Assumption 4.2.2 hold. Then J* N = TN J̄ , 
and for every " > 0, there exists an "-optimal policy. 
Proof: Note that since by assumption, J* N (x) > $# for all x ' X , an 
N -stage "-optimal policy #! ' " is one for which 
J* N + JN,"! + J* 
N + " e. 
We use induction. The result clearly holds for N = 1. Assume that it holds for N = k, i.e., J* 
k = T kJ̄ and for any given " > 0, there is a #! ' "
Sec. 4.2 Finite Horizon Problems 239 
with Jk,"! + J* k + " e. Using Eq. (4.7), we have for all µ ' M, 
J* k+1 + TµJk,"! + TµJ* 
k + $" e. 
Taking the infimum over µ and then the limit as " & 0, we obtain J* k+1 + 
TJ* k . By using the induction hypothesis J* 
k = T kJ̄ , it follows that J* k+1 + 
T k+1J̄ . On the other hand, we have clearly T k+1J̄ + Jk+1," for all # ' ", so that T k+1J̄ + J* 
k+1, and hence T k+1J̄ = J* k+1. 
We now turn to the existence of an "-optimal policy part of the induction argument. Using the assumption J* 
k (x) > $# for all x ' x ' X , for any " > 0, we can choose # = {µ0, µ1, . . .} such that 
Jk," + J* k + 
" 
2$ e, (4.8) 
and µ ' M such that 
TµJ* k + TJ* 
k + " 
2 e. 
Let #! = {µ, µ0, µ1, . . .}. Then 
Jk+1,"! = TµJk," + TµJ* 
k + " 
2 e + TJ* 
k + " e = J* k+1 + " e, 
where the first inequality is obtained by applying Tµ to Eq. (4.8) and using Eq. (4.7). The induction is complete. Q.E.D. 
We now provide some counterexamples showing that the conditions of the preceding propositions are necessary, and that for exceptional (but otherwise very simple) problems, the Bellman equation J* 
N = TN J̄ may not hold and/or there may not exist an "-optimal policy. 
Example 4.2.1 (Counterexample to Bellman’s Equation I) 
Let X = {0}, U(0) = (!1, 0], J̄(0) = 0, 
H(0, u, J) = 
, u if !1 < J(0), J(0) + u if J(0) " !1. 
Then (Tµ0 · · ·TµN!1 J̄)(0) = µ0(0), 
and J" N (0) = !1, while (TN J̄)(0) = !N for every N . Here Assumption 4.2.1, 
and the condition (4.7) (cf. Assumption 4.2.2) are violated, even though the condition J" 
k (x) > !# for all x $ X (cf. Assumption 4.2.2) is satisfied.
240 Noncontractive Models Chap. 4 
Example 4.2.2 (Counterexample to Bellman’s Equation II) 
Let 
X = {0, 1}, U(0) = U(1) = (!#, 0], J̄(0) = J̄(1) = 0, 
H(0, u, J) = 
, u if J(1) = !#, 0 if J(1) > !#, 
H(1, u, J) = u. 
Then 
(Tµ0 · · ·TµN!1 J̄)(0) = 0, (Tµ0 · · ·TµN!1 J̄)(1) = µ0(1), % N & 1. 
It can be seen that for N & 2, we have J" N (0) = 0 and J" 
N (1) = !#, but (TN J̄)(0) = (TN J̄)(1) = !#. Here Assumption 4.2.1, and the condition J" k (x) > !# for all x $ X (cf. Assumption 4.2.2) are violated, even though 
the condition (4.7) of Assumption 4.2.2 is satisfied. 
In the preceding two examples, the anomalies are due to discontinuity of the mapping H with respect to J . In classical finite horizon DP, the mapping H is usually continuous when it takes finite values, but counterexamples arise in unusual problems where infinite values occur. The next example is a simple stochastic optimal control problem, which involves some infinite expected values of random variables and we have J* 
2 /= T 2J̄ . 
Example 4.2.3 (Counterexample to Bellman’s Equation III) 
Let X = {0, 1}, U(0) = U(1) = ', J̄(0) = J̄(1) = 0, 
let w be a real-valued random variable with E{w} = #, and let 
H(x, u, J) = 
, E & w + J(1) 
' if x = 0, 
u+ J(1) if x = 1, % x $ X, u $ U(x). 
Then if Jm is real-valued for all m, and Jm(1) ( J(1) = !#, we have 
lim m$% 
H(0, u, Jm) = lim m$% 
E & w + Jm(1) 
' = #, 
while 
H * 0, u, lim 
m$% Jm 
+ = E 
& w + J(1) 
' = !#, 
so Assumption 4.2.1 is violated. Indeed, the reader may verify with a straightforward calculation that J" 
2 (0) = #, J" 2 (1) = !#, while (T 2J̄)(0) = !#, 
(T 2J̄)(1) = !#, so J" 2 )= T 2J̄ . Note that Assumption 4.2.2 is also violated 
because J" 2 (1) = !#. 
In the next counterexample, Bellman’s equation holds, but there is no "-optimal policy. This is an undiscounted deterministic optimal control problem of the type discussed in Section 1.1, where J! 
k (x) = $# for some x and k, so Assumption 4.2.2 is violated. We use the notation introduced there.
Sec. 4.3 Infinite Horizon Problems 241 
Example 4.2.4 (Counterexample to Existence of an "-Optimal Policy) 
Let ! = 1 and 
N = 2, X = {0, 1, . . .}, U(x) = (0,#), J̄(x) = 0, % x $ X, 
f(x, u) = 0, % x $ X, u $ U(x), 
g(x, u) = -!u if x = 0, x if x )= 0, 
% u $ U(x), 
so that H(x, u, J) = g(x, u) + J(0). 
Then for " $ ! and x )= 0, we have J2,"(x) = x!µ1(0), so that J" 2 (x) = !# 
for all x )= 0. Clearly, we also have J" 2 (0) = !#. Here Assumption 4.2.1, 
as well as Eq. (4.7) (cf. Assumption 4.2.2) are satisfied, and indeed we have J" 2 (x) = (T 2J̄)(x) = !# for all x $ X. However, the condition J" 
k (x) > !# for all x and k (cf. Assumption 4.2.2) is violated, and it is seen that there does not exist a two-stage #-optimal policy for any # > 0. The reason is that an #-optimal policy " = {µ0, µ1} must satisfy 
J2,"(x) = x! µ1(0) " ! 1 # , % x $ X, 
[in view of J" 2 (x) = !# for all x $ X], which is impossible since the left-hand 
side above can become positive for x su"ciently large. 
4.3 INFINITE HORIZON PROBLEMS 
We now turn to the infinite horizon problem (4.2), where the cost function of a policy # = {µ0, µ1, . . .} is 
J"(x) = lim sup k$% 
(Tµ0 · · ·Tµk J̄)(x), * x ' X. 
In this section one of the following two assumptions will be in e#ect. 
Assumption I: (Monotone Increase) 
(a) We have 
$# < J̄(x) + H(x, u, J̄), * x ' X, u ' U(x). 
(b) For each convergent sequence {Jm} ( E(X) with Jm 0 J and J̄ + Jm for all m - 0, we have 
lim m$% 
H(x, u, Jm) = H (x, u, J) , * x ' X, u ' U(x).
242 Noncontractive Models Chap. 4 
(c) There exists a scalar $ ' (0,#) such that for all scalars r ' (0,#) and functions J ' E(X) with J̄ + J , we have 
H(x, u, J + r e) + H(x, u, J) + $ r, * x ' X, u ' U(x). 
Assumption D: (Monotone Decrease) 
(a) We have 
J̄(x) - H(x, u, J̄), * x ' X, u ' U(x). 
(b) For each convergent sequence {Jm} ( E(X) with Jm . J and Jm + J̄ for all m - 0, we have 
lim m$% 
H(x, u, Jm) = H (x, u, J) , * x ' X, u ' U(x). 
Assumptions I and D apply to the positive and negative cost DP models, respectively (see [Ber12a], Chapter 4). These are the special cases of the infinite horizon stochastic optimal control problem of Example 1.2.1, where J̄(x) , 0 and the cost per stage g is uniformly nonnegative or uniformly nonpositive, respectively. The latter arises often when we want to maximize positive rewards. 
It is important to note that Assumptions I and D allow J" to be defined as a limit rather than as a lim sup. In particular, part (a) of the assumptions and the monotonicity of H imply that 
J̄ + Tµ0 J̄ + Tµ0Tµ1 J̄ + · · · + Tµ0 · · ·Tµk J̄ + · · · 
under Assumption I, and 
J̄ - Tµ0 J̄ - Tµ0Tµ1 J̄ - · · · - Tµ0 · · ·Tµk J̄ - · · · 
under Assumption D. Thus we have 
J"(x) = lim k$% 
(Tµ0 · · ·Tµk J̄)(x), * x ' X, 
with the limit being a real number or # or $#, respectively.
Sec. 4.3 Infinite Horizon Problems 243 
J TJ 
= 0 TµJ 
JµJ̄ J̄ J TJ 
= 0 TµJ 
Jµ 
Figure 4.3.1. Illustration of the consequences of lack of continuity of Tµ from below or from above [cf. part (b) of Assumption I or D, respectively]. In the figure on the left, we have J̄ ! TµJ̄ but Tµ is discontinuous from below at Jµ, so Assumption I does not hold, and Jµ is not a fixed point of Tµ. In the figure on the right, we have J̄ " TµJ̄ but Tµ is discontinuous from above at Jµ, so Assumption D does not hold, and Jµ is not a fixed point of Tµ. 
The conditions of part (b) of Assumptions I and D are continuity assumptions designed to preclude some of the pathologies of the type encountered also in Chapter 3, and addressed with the use of S-regular policies. In particular, these conditions are essential for making a connection with fixed point theory: they ensure that Jµ is a fixed point of Tµ, as shown in the following proposition. 
Proposition 4.3.1: Let Assumption I or Assumption D hold. Then for every policy µ ' M, we have 
Jµ = TµJµ. 
Proof: Let Assumption I hold. Then for all k - 0, 
(T k+1 µ J̄)(x) = H 
! x, µ(x), T k 
µ J̄ " , x ' X, 
and by taking the limit as k & #, and using part (b) of Assumption I, and the fact T k 
µ J̄ 0 Jµ, we have for all x ' X , 
Jµ(x) = lim k$% 
H ! x, µ(x), T k 
µ J̄ " = H 
! x, µ(x), lim 
k$% T k µ J̄ " = H 
! x, µ(x), Jµ 
" , 
or equivalently Jµ = TµJµ. The proof for the case of Assumption D is similar. Q.E.D.
244 Noncontractive Models Chap. 4 
Figure 4.3.1 illustrates how Jµ may fail to be a fixed point of Tµ if part (b) of Assumption I or D is violated. Note also that continuity of Tµ 
does not imply continuity of T , and for example, under Assumption I, T may be discontinuous from below. We will see later that as a result, the value iteration sequence {T kJ̄} may fail to converge to J* in the absence of additional conditions (see Section 4.3.2). Part (c) of Assumption I is a technical condition that facilitates the analysis, and assures the existence of "-optimal policies. 
Despite the similarities between Assumptions I and D, the corresponding results that one may obtain involve some substantial di#erences. An important fact, which breaks the symmetry between the two cases, is that J* is approached by T kJ̄ from below in the case of Assumption I and from above in the case of Assumption D. Another important fact is that since the condition J̄(x) > $# for all x ' X is part of Assumption I, all the functions J encountered in the analysis under this assumption (such as T kJ̄ , J" , and J*) also satisfy J(x) > $#, for all x ' X. In particular, if J - J̄ , we have 
(TJ)(x) - (T J̄)(x) > $#, * x ' X, 
and for every " > 0 there exists µ! ' M such that 
Tµ!J + TJ + " e. 
This property is critical for the existence of an "-optimal policy under As-sumption I (see the next proposition) and is not available under Assumption D. It accounts in part for the di#erent character of the results that can be obtained under the two assumptions. 
4.3.1 Fixed Point Properties and Optimality Conditions 
We first consider the question whether the optimal cost function J* is a fixed point of T . This is indeed true, but the lines of proof are di#erent under the Assumptions I and D. We begin with the proof under Assumption I, and as a preliminary step we show the existence of an "-optimal policy, something that is of independent theoretical interest. 
Proposition 4.3.2: Let Assumption I hold. Then given any " > 0, there exists a policy #! ' " such that 
J* + J"! + J* + " e. 
Furthermore, if the scalar $ in part (c) of Assumption I satisfies $ < 1, the policy #! can be taken to be stationary.
Sec. 4.3 Infinite Horizon Problems 245 
Proof: Let {"k} be a sequence such that "k > 0 for all k and 
%. 
k=0 
$k"k = ". (4.9) 
For each x ' X , consider a sequence of policies & #k[x] 
' ( " of the form 
#k[x] = & µk 0 [x], µ 
k 1 [x], . . . 
' , (4.10) 
such that for k = 0, 1, . . . , 
J"k[x](x) + J*(x) + "k. (4.11) 
Such a sequence exists, since we have assumed that J̄(x) > $#, and therefore J*(x) > $#, for all x ' X . 
The preceding notation should be interpreted as follows. The policy #k[x] of Eq. (4.10) is associated with x. Thus µk 
i [x] denotes for each x and k, a function in M, while µk 
i [x](z) denotes the value of µ k i [x] at an element 
z ' X . In particular, µk i [x](x) denotes the value of µk 
i [x] at x ' X . Consider the functions µk defined by 
µk(x) = µk 0 [x](x), * x ' X, (4.12) 
and the functions J̄k defined by 
J̄k(x) = H * x, µk(x), lim 
m$% Tµk 
1 [x] · · ·Tµk 
m[x]J̄ + , * x ' X, k = 0, 1, . . . . 
(4.13) By using Eqs. (4.11), (4.12), and part (b) of Assumption I, we obtain for all x ' X and k = 0, 1, . . . 
J̄k(x) = lim m$% 
! Tµk 
0 [x] · · ·Tµk 
m[x]J̄ " (x) 
= J"k[x](x) 
+ J*(x) + "k. 
(4.14) 
From Eqs. (4.13), (4.14), and part (c) of Assumption I, we have for all x ' X and k = 1, 2, . . ., 
(Tµk!1 J̄k)(x) = H 
! x, µk&1(x), J̄k 
" 
+ H ! x, µk&1(x), J* + "k e 
" 
+ H ! x, µk&1(x), J* 
" + $"k 
+ H * x, µk&1(x), lim 
m$% T µk!1 1 [x] 
· · ·T µk!1 m [x] 
J̄ + + $"k 
= J̄k&1(x) + $"k,
246 Noncontractive Models Chap. 4 
and finally 
Tµk!1 J̄k + J̄k&1 + $"k e, k = 1, 2, . . . . 
Using this inequality and part (c) of Assumption I, we obtain 
Tµk!2 Tµk!1 
J̄k + Tµk!2 (J̄k&1 + $"k e) 
+ Tµk!2 J̄k&1 + $2"k e 
+ J̄k&2 + ($"k&1 + $2"k) e. 
Continuing in the same manner, we have for k = 1, 2, . . . , 
Tµ0 · · ·Tµk!1 
J̄k + J̄0 + ($"1 + · · ·+ $k"k) e + J* + 
/ k. 
i=0 
$i"i 
0 e. 
Since J̄ + J̄k, it follows that 
Tµ0 · · ·Tµk!1 
J̄ + J* + 
/ k. 
i=0 
$i"i 
0 e. 
Denote #! = {µ0, µ1, . . .}. Then by taking the limit in the preceding inequality and using Eq. (4.9), we obtain 
J"! + J* + " e. 
If $ < 1, we take "k = "(1$$) for all k, and #k[x] = & µ0[x], µ1[x], . . . 
' 
in Eq. (4.11). The stationary policy #! = {µ, µ, . . .}, where µ(x) = µ0[x](x) for all x ' X , satisfies J"! + J* + " e. Q.E.D. 
Note that the assumption $ < 1 is essential in order to be able to take #! stationary in the preceding proposition. As an example, let X = {0}, U(0) = (0,#), J̄(0) = 0, H(0, u, J) = u + J(0). Then J*(0) = 0, but for any µ ' M, we have Jµ(0) = #. 
By using Prop. 4.3.2 we can prove the following. 
Proposition 4.3.3: Let Assumption I hold. Then 
J* = TJ*. 
Furthermore, if J # ' E(X) is such that J # - J̄ and J # - TJ #, then J # - J*.
Sec. 4.3 Infinite Horizon Problems 247 
Proof: For every # = {µ0, µ1, . . .} ' " and x ' X , we have using part (b) of Assumption I, 
J"(x) = lim k$% 
(Tµ0Tµ1 · · ·Tµk J̄)(x) 
= Tµ0 
( lim k$% 
Tµ1 · · ·Tµk J̄ 
) (x) 
- (Tµ0J*)(x) 
- (TJ*)(x). 
By taking the infimum of the left-hand side over # ' ", we obtain 
J* - TJ*. 
To prove the reverse inequality, let "1 and "2 be any positive scalars, and let # = {µ0, µ1, . . .} be such that 
Tµ0 J* + TJ* + "1 e, J"1 + J* + "2 e, 
where #1 = {µ1, µ2, . . .} (such a policy exists by Prop. 4.3.2). The sequence {Tµ1 
· · ·Tµk J̄} is monotonically nondecreasing, so by using the preceding 
relations and part (c) of Assumption I, we have 
Tµ0 Tµ1 
· · ·Tµk J̄ + Tµ0 
( lim k$% 
Tµ1 · · ·Tµk 
J̄ 
) 
= Tµ0 J"1 
+ Tµ0 J* + $"2 e 
+ TJ* + ("1 + $"2) e. 
Taking the limit as k & #, we obtain 
J* + J" = lim k$% 
Tµ0 Tµ1 
· · ·Tµk J̄ + TJ* + ("1 + $"2) e. 
Since "1 and "2 can be taken arbitrarily small, it follows that 
J* + TJ*. 
Hence J* = TJ*. Assume that J # ' E(X) satisfies J # - J̄ and J # - TJ #. Let {"k} be 
any sequence with "k > 0 for all k, and consider a policy # = {µ0, µ1, . . .} ' " such that 
Tµk J # + TJ # + "k e, k = 0, 1, . . . .
248 Noncontractive Models Chap. 4 
We have from part (c) of Assumption I 
J* = inf ""! 
lim k$% 
Tµ0 · · ·Tµk J̄ 
+ inf ""! 
lim inf k$% 
Tµ0 · · ·Tµk J # 
+ lim inf k$% 
Tµ0 · · ·Tµk 
J # 
+ lim inf k$% 
Tµ0 · · ·Tµk!1 
(TJ # + "k e) 
+ lim inf k$% 
Tµ0 · · ·Tµk!1 
(J # + "k e) 
+ lim inf k$% 
(Tµ0 · · ·Tµk!1 
J # + $k"k e) 
... 
+ lim k$% 
/ TJ # + 
/ k. 
i=0 
$i"i 
0 e 
0 
+ J # + 
/ k. 
i=0 
$i"i 
0 e. 
Since we may choose 1k 
i=0 $ i"i as small as desired, it follows that J* + J #. 
Q.E.D. 
The following counterexamples show that parts (b) and (c) of As-sumption I are essential for the preceding proposition to hold. 
Example 4.3.1 (Counterexample to Bellman’s Equation I) 
Let 
X = {0, 1}, U(0) = U(1) = (!1, 0], J̄(0) = J̄(1) = !1, 
H(0, u, J) = 
, u if J(1) " !1, 0 if J(1) > !1, 
H(1, u, J) = u. 
Then for N & 1, 
(Tµ0 · · · TµN!1 J̄)(0) = 0, (Tµ0 · · ·TµN!1 J̄)(1) = µ0(1). 
Thus 
J"(0) = 0, J"(1) = !1, (TJ")(0) = !1, (TJ")(1) = !1, 
and hence J" )= TJ". Notice also that J̄ is a fixed point of T , while J̄ " J" 
and J̄ )= J", so the second part of Prop. 4.3.3 fails when J̄ = J &. Here parts (a) and (b) of Assumption I are satisfied, but part (c) is violated, since H(0, u, ·) is discontinuous at J = !1 when u < 0.
Sec. 4.3 Infinite Horizon Problems 249 
Example 4.3.2 (Counterexample to Bellman’s Equation II) 
Let 
X = {0, 1}, U(0) = U(1) = {0}, J̄(0) = J̄(1) = 0, 
H(0, 0, J) = 
, 0 if J(1) < #, # if J(1) = #, 
H(1, 0, J) = J(1) + 1. 
Here there is only one policy, which we denote by µ. For all N & 1, we have 
(TN µ J̄)(0) = 0, (TN 
µ J̄)(1) = N, 
so J"(0) = 0, J"(1) = #. On the other hand, we have (TJ")(0) = (TJ")(1) = # and J" )= TJ". Here parts (a) and (c) of Assumption I are satisfied, but part (b) is violated. 
As a corollary to Prop. 4.3.3 we obtain the following. 
Proposition 4.3.4: Let Assumption I hold. Then for every µ ' M, we have 
Jµ = TµJµ. 
Furthermore, if J # ' E(X) is such that J # - J̄ and J # - TµJ #, then J # - Jµ. 
Proof: Consider the variant of the infinite horizon problem where the control constraint set is Uµ(x) = 
& µ(x) 
' rather than U(x) for all x ' X . 
Application of Prop. 4.3.3 yields the result. Q.E.D. 
We now provide the counterpart of Prop. 4.3.3 under Assumption D. We first prove a preliminary result regarding the convergence of the value iteration method, which is of independent interest (we will see later that this result need not hold under Assumption I). 
Proposition 4.3.5: Let Assumption D hold. Then TN J̄ = J* N , 
where J* N is the optimal cost function for the N -stage problem. More-
over J* = lim 
N$% J* N . 
Proof: By repeating the proof of Prop. 4.2.3, we have TN J̄ = J* N [part (b) 
of Assumption D is essentially identical to the assumption of that proposition]. Clearly we have J* + J* 
N for all N , and hence J* + limN$% J* N .
250 Noncontractive Models Chap. 4 
To prove the reverse inequality, we note that for all # = {µ0, µ1, . . .} ' ", we have 
Tµ0 · · ·TµN!1 J̄ - J* N . 
By taking the limit of both sides as N & #, we obtain J" - limN$% J* N , 
and by taking infimum over #, J* - limN$% J* N . Thus J* = limN$% J* 
N . Q.E.D. 
Proposition 4.3.6: Let Assumption D hold. Then 
J* = TJ*. 
Furthermore, if J # ' E(X) is such that J # + J̄ and J # + TJ #, then J # + J*. 
Proof: For any # = {µ0, µ1, . . .} ' ", we have 
J" = lim k$% 
Tµ0Tµ1 · · ·Tµk J̄ - lim 
k$% Tµ0T kJ̄ - Tµ0J*, 
where the last inequality follows from the fact T kJ̄ . J* (cf. Prop. 4.3.5). Taking the infimum of both sides over # ' ", we obtain J* - TJ*. 
To prove the reverse inequality, we select any µ ' M, and we apply Tµ to both sides of the equation J* = limN$% TN J̄ (cf. Prop. 4.3.5). By using part (b) of assumption D, we obtain 
TµJ* = Tµ 
* lim 
N$% TN J̄ 
+ = lim 
N$% TµTN J̄ - lim 
N$% TN+1J̄ = J*. 
Taking the infimum of the left-hand side over µ ' M, we obtain TJ* - J*, showing that TJ* = J*. 
To complete the proof, let J # ' E(X) be such that J # + J̄ and J # + TJ #. Then we have 
J* = inf ""! 
lim N$% 
Tµ0 · · ·TµN!1 J̄ 
- lim N$% 
inf ""! 
Tµ0 · · ·TµN!1 J̄ 
- lim N$% 
inf ""! 
Tµ0 · · ·TµN!1J # 
- lim N$% 
TNJ # 
- J #, 
where the last inequality follows from the hypothesis J # + TJ #. Thus J* - J #. Q.E.D.
Sec. 4.3 Infinite Horizon Problems 251 
Counterexamples to Bellman’s equation can be readily constructed if part (b) of Assumption D (continuity from above) is violated. In particular, in Examples 4.2.1 and 4.2.2, part (a) of Assumption D is satisfied but part (b) is not. In both cases we have J* /= TJ*, as the reader can verify with a straightforward calculation. 
Similar to Prop. 4.3.4, we obtain the following. 
Proposition 4.3.7: Let Assumption D hold. Then for every µ ' M, we have 
Jµ = TµJµ. 
Furthermore, if J # ' E(X) is such that J # + J̄ and J # + TµJ #, then J # + Jµ. 
Proof: Consider the variation of our problem where the control constraint set is Uµ(x) = 
& µ(x) 
' rather than U(x) for all x ' X . Application of Prop. 
4.3.6 yields the result. Q.E.D. 
An examination of the proof of Prop. 4.3.6 shows that the only point where we need part (b) of Assumption D was in establishing the relations 
lim N$% 
TJ* N = T 
* lim 
N$% J* N 
+ 
and 
J* N = TN J̄ . 
If these relations can be established independently, then the result of Prop. 4.3.6 follows. In this manner we obtain the following proposition. 
Proposition 4.3.8: Let part (a) of Assumption D hold, assume that X is a finite set, and that J*(x) > $# for all x ' X . Assume further that there exists a scalar $ ' (0,#) such that for all scalars r ' (0,#) and functions J ' E(X) with J + J̄ , we have 
H(x, u, J)$ $ r + H(x, u, J $ r e), * x ' X, u ' U(x). (4.15) 
Then J* = TJ*. 
Furthermore, if J # ' E(X) is such that J # + J̄ and J # + TJ #, then J # + J*.
252 Noncontractive Models Chap. 4 
Proof: A nearly verbatim repetition of Prop. 4.2.4 shows that under our assumptions we have J* 
N = TN J̄ for all N . We will show that 
lim N$% 
H(x, u, J* N ) + H 
* x, u, lim 
N$% J* N 
+ , * x ' X, u ' U(x). 
Then the result follows as in the proof of Prop. 4.3.6. Assume the contrary, i.e., that for some x̃ ' X , ũ ' U(x̃), and " > 0, 
there holds 
H(x̃, ũ, J* k )$ " > H 
* x̃, ũ, lim 
N$% J* N 
+ , k = 1, 2, . . . . 
From the finiteness of X and the fact 
J*(x) = lim N$% 
J* N (x) > $#, * x ' X, 
it follows that for some integer k > 0 
J* k $ ("/$)e + lim 
N$% J* N , * k - k. 
By using the condition (4.15), we obtain for all k - k 
H(x̃, ũ, J* k )$ " + H 
! x̃, ũ, J* 
k $ ("/$) e " + H 
* x̃, ũ, lim 
N$% J* N 
+ , 
which contradicts the earlier inequality. Q.E.D. 
Characterization of Optimal Policies 
We now provide necessary and su!cient conditions for optimality of a stationary policy. These conditions are markedly di#erent under Assumptions I and D. 
Proposition 4.3.9: Let Assumption I hold. Then a stationary policy µ is optimal if and only if 
TµJ* = TJ*. 
Proof: If µ is optimal, then Jµ = J* so that the equation J* = TJ* (cf. Prop. 4.3.3) implies that Jµ = TJµ. Since Jµ = TµJµ (cf. Prop. 4.3.4), it follows that TµJ* = TJ*.
Sec. 4.3 Infinite Horizon Problems 253 
Conversely, if TµJ* = TJ*, then since J* = TJ*, it follows that TµJ* = J*. By Prop. 4.3.4, it follows that Jµ + J*, so µ is optimal. Q.E.D. 
Proposition 4.3.10: Let Assumption D hold. Then a stationary policy µ is optimal if and only if 
TµJµ = TJµ. 
Proof: If µ is optimal, then Jµ = J*, so that the equation J* = TJ* 
(cf. Prop. 4.3.6) can be written as Jµ = TJµ. Since Jµ = TµJµ (cf. Prop. 4.3.4), it follows that TµJµ = TJµ. 
Conversely, if TµJµ = TJµ, then since Jµ = TµJµ, it follows that Jµ = TJµ. By Prop. 4.3.7, it follows that Jµ + J*, so µ is optimal. Q.E.D. 
An example showing that under Assumption I, the condition TµJµ = TJµ does not guarantee optimality of µ is given in Exercise 4.3. Under Assumption D, we note that by Prop. 4.3.1, we have Jµ = TµJµ for all µ, so if µ is a stationary optimal policy, the fixed point equation 
J*(x) = inf u"U(x) 
H(x, u, J*), * x ' X, (4.16) 
and the optimality condition of Prop. 4.3.10, yield 
TJ* = J* = Jµ = TµJµ = TµJ*. 
Thus under D, a stationary optimal policy attains the infimum in the fixed point Eq. (4.16) for all x. However, there may exist nonoptimal stationary policies also attaining the infimum for all x; an example is the shortest path problem of Section 3.1.1 for the case where a = 0 and b = 1. Moreover, it is possible that this infimum is attained but no optimal policy exists, as shown by Fig. 4.3.2. 
Proposition 4.3.9 shows that under Assumption I, there exists a stationary optimal policy if and only if the infimum in the optimality equation 
J*(x) = inf u"U(x) 
H(x, u, J*) 
is attained for every x ' X . When the infimum is not attained for some x ' X , this optimality equation can still be used to yield an "-optimal policy, which can be taken to be stationary whenever the scalar $ in Assumption I(c) is strictly less than 1. This is shown in the following proposition.
254 Noncontractive Models Chap. 4 
J TJ= 0 J̄ = 0Jµ 
J̄ T k µ J̄ 
J! = TJ! 
Jµ 
TµJ T 
J TµJ 
Figure 4.3.2. An example where nonstationary policies are dominant under As-sumption D. Here there is only one state and S = #. There are two stationary policies µ and µ with cost functions Jµ and Jµ as shown. However, by considering a nonstationary policy of the form !k = {µ, . . . , µ, µ, µ, . . .}, with a number k of policies µ, we can obtain a sequence {J"k 
} that converges to the value J" shown. Note that here there is no optimal policy, stationary or not. 
Proposition 4.3.11: Let Assumption I hold. Then: 
(a) If " > 0, the sequence {"k} satisfies 1% 
k=0 $ k"k = ", and "k > 0 
for all k, and the policy #! = {µ! 0, µ 
! 1, . . .} ' " is such that 
Tµ" k J* + TJ* + "k e, * k = 0, 1, . . . , 
then J* + J"" + J* + " e. 
(b) If " > 0, the scalar $ in part (c) of Assumption I is strictly less than 1, and µ! ' M is such that 
Tµ"J* + TJ* + "(1$ $) e, 
then J* + Jµ" + J* + " e.
Sec. 4.3 Infinite Horizon Problems 255 
Proof: (a) Since TJ* = J*, we have 
Tµ" k J* + J* + "k e, 
and applying Tµ" k!1 
to both sides, we obtain 
Tµ" k!1 
Tµ" k J* + Tµ" 
k!1 J* + $"k e + J* + ("k&1 + $"k) e. 
Applying Tµ" k!2 
throughout and repeating the process, we obtain for every 
k = 1, 2, . . ., 
Tµ" 0 · · ·Tµ" 
k J* + J* + 
/ k. 
i=0 
$i"i 
0 e, k = 1, 2, . . . . 
Since J̄ + J*, it follows that 
Tµ" 0 · · ·Tµ" 
k J̄ + J* + 
/ k. 
i=0 
$i"i 
0 e, k = 1, 2, . . . . 
By taking the limit as k & #, we obtain J"" + J* + " e. 
(b) This part is proved by taking "k = "(1 $ $) and µ! k = µ! for all k in 
the preceding argument. Q.E.D. 
Under Assumption D, the existence of an "-optimal policy is harder to establish, and requires some restrictive conditions. 
Proposition 4.3.12: Let Assumption D hold, and let the additional assumptions of Prop. 4.3.8 hold. Then for any " > 0, there exists an "-optimal policy. 
Proof: For each N , denote 
"N = " 
2(1 + $+ · · ·+ $N&1) , 
and let #N = {µN 
0 , µN 1 , . . . , µN 
N&1, µ, µ . . .} 
be such that µ ' M, and for k = 0, . . . , N $ 1, µN k ' M and 
TµN k TN&k&1J̄ = TN&kJ̄ + "N e.
256 Noncontractive Models Chap. 4 
We have TN µN!1 J̄ + T J̄+"N e, and applying TN 
µN!2 to both sides, we obtain 
TN µN!2T 
N µN!1 J̄ + TN 
µN!2T J̄ + $"N e + T 2J̄ + (1 + $)"N e. 
Continuing in the same manner, we have 
TN µ0 · · ·T 
N µN!1 J̄ + TN J̄ + (1 + $+ · · ·+ $N&1)"N e, 
from which we obtain for N = 0, 1, . . ., 
J"N + TN J̄ + ("/2) e. 
By Prop. 4.3.5, we have J* = limN$% TN J̄ , so let N̄ be such that 
T N̄ J̄ + J* + ("/2) e 
[such a N̄ exists using the assumptions of finiteness of X and J*(x) > $# for all x ' X ]. Then we obtain J"N̄ 
+ J* + " e, and #N̄ is the desired policy. Q.E.D. 
4.3.2 Value Iteration 
We will now discuss algorithms for abstract DP under Assumptions I and and D. We first consider the VI algorithm, which consists of successively generating T J̄, T 2J̄ , . . .. Note that because T need not be a contraction, it may have multiple fixed points J all of which satisfy J - J* under Assumption I (cf. Prop. 4.3.3) or J + J* under Assumption D (cf. Prop. 4.3.6). Thus, in the absence of additional conditions (to be discussed in Sections 4.4 and 4.5), it is essential to start VI with J̄ or an initial J0 such that J̄ + J0 + J* under Assumption I or J̄ - J0 - J* under Assumption D. In the next two propositions, we show that for such initial conditions, we have convergence of VI to J* under Assumption D, and with an additional compactness condition, under Assumption I. 
Proposition 4.3.13: Let Assumption D hold, and assume that J0 ' E(X) is such that J̄ - J0 - J*. Then 
lim k$% 
T kJ0 = J*. 
Proof: The condition J̄ - J0 - J* implies that T kJ̄ - T kJ0 - J* for all k. By Prop. 4.3.5, T kJ̄ & J*, and the result follows. Q.E.D.
Sec. 4.3 Infinite Horizon Problems 257 
The convergence of VI under I requires an additional compactness condition, which is satisfied in particular if U(x) is a finite set for all x ' X . 
Proposition 4.3.14: Let Assumption I hold, let U be a metric space, and assume that the sets 
Uk(x,!) = & u ' U(x) 
22 H(x, u, T kJ̄) + ! ' 
(4.17) 
are compact for every x ' X , ! ' !, and for all k greater than some integer k. Assume that J0 ' E(X) is such that J̄ + J0 + J*. Then 
lim k$% 
T kJ0 = J*. 
Furthermore, there exists a stationary optimal policy. 
Proof: Similar to the proof of Prop. 4.3.13, it will su!ce to show that T kJ̄ & J*. Since J̄ + J*, we have T kJ̄ + T kJ* = J*, so that 
J̄ + T J̄ + · · · + T kJ̄ + · · · + J*. 
Thus we have T kJ̄ 0 J% for some J% ' E(X) satisfying T kJ̄ + J% + J* 
for all k. Applying T to this relation, we obtain 
(T k+1J̄)(x) = min u"U(x) 
H(x, u, T kJ̄) + (TJ%)(x), 
and by taking the limit as k & #, it follows that 
J% + TJ%. 
Assume to arrive at a contradiction that there exists a state x̃ ' X such that 
J%(x̃) < (TJ%)(x̃). (4.18) 
Similar to Lemma 3.3.1, there exists a point uk attaining the minimum in 
(T k+1J̄)(x̃) = inf u"U(x̃) 
H(x̃, u, T kJ̄); 
i.e., uk is such that 
(T k+1J̄)(x̃) = H(x̃, uk, T kJ̄). 
Clearly, by Eq. (4.18), we must have J%(x̃) < #. For every k, consider the set 
Uk 
! x̃, J%(x̃) 
" = -u ' U(x̃) 
22 H(x̃, uk, T kJ̄) + J%(x̃) 3 ,
258 Noncontractive Models Chap. 4 
and the sequence {ui}%i=k. Since T kJ̄ 0 J%, it follows that for all i - k, 
H(x̃, ui, T kJ̄) + H(x̃, ui, T iJ̄) + J%(x̃). 
Therefore {ui}%i=k ( Uk 
! x̃, J%(x̃) 
" , and since Uk 
! x̃, J%(x̃) 
" is compact, all 
the limit points of {ui}%i=k belong to Uk 
! x̃, J%(x̃) 
" and at least one such 
limit point exists. Hence the same is true of the limit points of the whole sequence {ui}. It follows that if ũ is a limit point of {ui} then 
ũ ' 1% k=0Uk 
! x̃, J%(x̃) 
" . 
By Eq. (4.17), this implies that for all k - k 
J%(x̃) - H(x̃, ũ, T kJ̄) - (T k+1J̄)(x̃). 
Taking the limit as k & #, and using part (b) of Assumption I, we obtain 
J%(x̃) - H(x̃, ũ, J%) - (TJ%)(x̃), (4.19) 
which contradicts Eq. (4.18). Hence J% = TJ%, which implies that J% -J* in view of Prop. 4.3.3. Combined with the inequality J% + J*, which was shown earlier, we have J% = J*. 
To show that there exists an optimal stationary policy, observe that the relation J* = J% = TJ% and Eq. (4.19) [whose proof is valid for all x̃ ' X such that J*(x̃) < #] imply that ũ attains the infimum in 
J*(x̃) = inf u"U(x̃) 
H(x̃, u, J*) 
for all x̃ ' X with J*(x̃) < #. For x̃ ' X such that J*(x̃) = #, every u ' U(x̃) attains the preceding minimum. Hence by Prop. 4.3.9 an optimal stationary policy exists. Q.E.D. 
The reader may verify by inspection of the preceding proof that if µk(x̃), k = 0, 1, . . ., attains the infimum in the relation 
(T k+1J̄)(x̃) = inf u"U(x) 
H(x̃, u, T kJ̄), 
and µ!(x̃) is a limit point of {µk(x̃)}, for every x̃ ' X , then the stationary policy µ! is optimal. Furthermore, {µk(x̃)} has at least one limit point for every x̃ ' X for which J*(x̃) < #. Thus the VI algorithm under the assumption of Prop. 4.3.14 yields in the limit not only the optimal cost function J* but also an optimal stationary policy. 
On the other hand, under Assumption I but in the absence of the compactness condition (4.17), T kJ̄ need not converge to J*. What is happening here is that while the mappings Tµ are continuous from below as required by Assumption I(b), T may not be, and a phenomenon like the one illustrated in the left-hand side of Fig. 4.3.1 may occur, whereby 
lim k$% 
T kJ̄ + T 
( lim k$% 
T kJ̄ 
) , 
with strict inequality for some x ' X . This can happen even in simple deterministic optimal control problems, as shown by the following example.
Sec. 4.3 Infinite Horizon Problems 259 
Example 4.3.3 (Counterexample to Convergence of VI) 
Let X = [0,#), U(x) = (0,#), J̄(x) = 0, % x $ X, 
and 
H(x, u, J) = min & 1, x+ J(2x+ u) 
' , % x $ X, u $ U(x). 
Then it can be verified that for all x $ X and policies µ, we have Jµ(x) = 1, as well as J"(x) = 1, while it can be seen by induction that starting with J̄ , the VI algorithm yields 
(T kJ̄)(x) = min & 1, (1 + 2k!1)x 
' , % x $ X, k = 1, 2 . . . . 
Thus we have 0 = limk$% (T kJ̄)(0) )= J"(0) = 1. 
The range of convergence of VI may be expanded under additional assumptions. In particular, in Chapter 3, under various conditions involving the existence of optimal S-regular policies, we showed that VI converges to J* assuming that the initial condition J0 satisfies J0 - J*. Thus if the assumptions of Prop. 4.3.14 hold in addition, we are guaranteed convergence of VI starting from any J satisfying J - J̄ . Results of this type will be obtained in Sections 4.4 and 4.5, where semicontractive models satisfying Assumption I will be discussed. 
Asynchronous Value Iteration 
The concepts of asynchronous VI that we developed in Section 2.6.1 apply also under the Assumptions I and D of this section. Under Assumption I, if J* is real-valued, we may apply Prop. 2.6.1 with the sets S(k) defined by 
S(k) = {J | T kJ̄ + J + J*}, k = 0, 1, . . . . 
Assuming that T kJ̄ & J* (cf. Prop. 4.3.14), it follows that the asynchronous form of VI converges pointwise to J* starting from any function in S(0). This result can also be shown for the case where J* is not real-valued, by using a simple extension of Prop. 2.6.1, where the set of real-valued functions R(X) is replaced by the set of all J ' E(X) with J̄ + J + J*. 
Under Assumption D similar conclusions hold for the asynchronous version of VI that starts with a function J with J* + J + J̄ . Asynchronous pointwise convergence to J* can be shown, based on an extension of the asynchronous convergence theorem (Prop. 2.6.1), where R(X) is replaced by the set of all J ' E(X) with J* + J + J̄ .
260 Noncontractive Models Chap. 4 
4.3.3 Exact and Optimistic Policy Iteration - !-Policy Iteration 
Unfortunately, in the absence of further conditions, the PI algorithm is not guaranteed to yield the optimal cost function and/or an optimal policy under either Assumption I or D. However, there are convergence results for nonoptimistic and optimistic variants of PI under some conditions. In what follows in this section we will provide an analysis of various types of PI, mainly under Assumption D. The analysis of PI under Assumption I will be given primarily in the next two sections, as it requires di#erent assumptions and methods of proof, and will be coupled with regularity ideas relating to the semicontractive models of Chapter 3. 
Optimistic Policy Iteration Under D 
A surprising fact under Assumption D is that nonoptimistic/exact PI may generate a policy that is strictly inferior over the preceding one. Moreover there may be an oscillation between nonoptimal policies even when the state and control spaces are finite. An illustrative example is the shortest path example of Section 3.1.1, where it can be verified that exact PI may oscillate between the policy that moves to the destination from node 1 and the policy that does not. For a mathematical explanation, note that under Assumption D, we may have TµJ* = TJ* without µ being optimal, so starting from an optimal policy, we may obtain a nonoptimal policy by PI. 
On the other hand optimistic PI under Assumption D has much better convergence properties, because it embodies the mechanism of VI, which is convergent to J* as we saw in the preceding subsection. Indeed, let us consider an optimistic PI algorithm that generates a sequence {Jk, µk} according to † 
TµkJk = TJk, Jk+1 = Tmk 
µk Jk, (4.20) 
where mk is a positive integer. We assume that the algorithm starts with a function J0 ' E(X) that satisfies J̄ - J0 - J* and J0 - TJ0. For example, we may choose J0 = J̄ . We have the following proposition. 
Proposition 4.3.15: Let Assumption D hold and let {Jk, µk} be a sequence generated by the optimistic PI algorithm (4.20), assuming that J̄ - J0 - J* and J0 - TJ0. Then Jk . J!. 
Proof: We have 
J0 - Tµ0J0 - Tm0 µ0 J0 = J1 - Tm0+1 
µ0 J0 = Tµ0J1 - TJ1 = Tµ1J1 - · · · - J2, 
† As with all PI algorithms in this book, we assume that the policy im-
provement operation is well-defined, in the sense that there exists µk such that TµkJk = TJk for all k.
Sec. 4.3 Infinite Horizon Problems 261 
where the first, second, and third inequalities hold because the assumption J0 - TJ0 = Tµ0J0 implies that 
Tm µ0J0 - Tm+1 
µ0 J0, * m - 0. 
Continuing similarly we obtain 
Jk - TJk - Jk+1, * k - 0. 
Moreover, we can show by induction that Jk - J*. Indeed this is true for k = 0 by assumption. If Jk - J*, we have 
Jk+1 = Tmk 
µk Jk - TmkJk - TmkJ* = J*, (4.21) 
where the last equality follows from the fact TJ* = J* (cf. Prop. 4.3.6), thus completing the induction. By combining the preceding two relations, we have 
Jk - TJk - Jk+1 - J*, * k - 0. (4.22) 
We will now show by induction that 
T kJ0 - Jk - J*, * k - 0. (4.23) 
Indeed this relation holds by assumption for k = 0, and assuming that it holds for some k - 0, we have by applying T to it and by using Eq. (4.22), 
T k+1J0 - TJk - Jk+1 - J*, 
thus completing the induction. By applying Prop. 4.3.13 to Eq. (4.23), we obtain Jk . J!. Q.E.D. 
!-Policy Iteration Under D 
We now consider the !-PI algorithm. It involves a scalar ! ' (0, 1) and a corresponding multistep mapping, which bears a relation to temporal di#erences and the proximal algorithm (cf. Section 1.2.5). It is defined by 
TµkJk = TJk, Jk+1 = T (#) 
µk Jk, (4.24) 
where for any policy µ and scalar ! ' (0, 1), T (#) µ is the mapping defined 
by 
(T (#) µ J)(x) = (1$ !) 
%. 
t=0 
!t(T t+1 µ J)(x), x ' X.
262 Noncontractive Models Chap. 4 
Here we assume that Tµ maps R(X) to R(X), and that for all µ ' M and J ' R(X), the limit of the series above is well-defined as a function in R(X). 
We discussed the !-PI algorithm in connection with semicontractive problems in Section 3.2.4, where we assumed that 
Tµ(T (#) µ J) = T (#) 
µ (TµJ), * µ ' M, J ' E(X). (4.25) 
We will show that for undiscounted finite-state MDP, the algorithm can be implemented by using matrix inversion, just like nonoptimistic PI for discounted finite-state MDP. It turns out that this can be an advantage in some settings, including approximate simulation-based implementations. 
As noted earlier, !-PI and optimistic PI are similar: they just use the mapping Tµk to apply VI in di#erent ways. In view of this similarity, it is not surprising that it has the same type of convergence properties as the earlier optimistic PI method (4.20). Similar to Prop. 4.3.15, we have the following. 
Proposition 4.3.16: Let Assumption D hold and let {Jk, µk} be a sequence generated by the !-PI algorithm (4.24), assuming Eq. (4.25), and that J̄ - J0 - J* and J0 - TJ0. Then Jk . J!. 
Proof: As in the proof of Prop. 4.3.15, by using Assumption D, the monotonicity of Tµ, and the hypothesis J0 - TJ0, we have 
J0 - TJ0 = Tµ0J0 - T (#) µ0 J0 = J1 - Tµ0J1 - TJ1 = Tµ1J1 - T (#) 
µ1 J0 = J2, 
where for the third inequality, we use the relation J0 - Tµ0J0, the definition of J1, and the assumption (4.25). Continuing in the same manner, 
Jk - TJk - Jk+1, * k - 0. 
Similar to the proof of Prop. 4.3.15, we show by induction that Jk - J*, using the fact that if Jk - J*, then 
Jk+1 = T (#) 
µk Jk - T (#) 
µk J* = (1$ !) %. 
t=0 
!tT t+1J* = J*, 
[cf. the induction step of Eq. (4.21)]. By combining the preceding two relations, we obtain Eq. (4.22), and the proof is completed by using the argument following that equation. Q.E.D. 
The !-PI algorithm has a useful property, which involves the mapping Wk : R(X) %& R(X) given by 
WkJ = (1$ !)TµkJk + !TµkJ. (4.26)
Sec. 4.3 Infinite Horizon Problems 263 
In particular Jk+1 is a fixed point of Wk. Indeed, using the definition 
Jk+1 = T (#) 
µk Jk 
[cf. Eq. (4.24)], and the linearity assumption (4.25), we have 
WkJk+1 = (1 $ !)TµkJk + !Tµk 
* T (#) 
µk Jk + 
= (1 $ !)TµkJk + !T (#) 
µk (TµkJk) 
= T (#) 
µk Jk 
= Jk+1. 
Thus Jk+1 can be calculated as a fixed point of Wk. Consider now the case where Tµk is nonexpansive with respect to 
some norm. Then from Eq. (4.26), it is seen that Wk is a contraction of modulus ! with respect to that norm, so Jk+1 is the unique fixed point of Wk. Moreover, if the norm is a weighted sup-norm, Jk+1 can be found using the methods of Chapter 2 for contractive models. The following example applies this idea to finite-state SSP problems. The interesting aspect of this example is that it implements the policy evaluation portion of !-PI through solution of a system of linear equations, similar to the exact policy evaluation method of classical PI. 
Example 4.3.4 (Stochastic Shortest Path Problems with Nonpositive Costs) 
Consider the SSP problem of Example 1.2.6 with states 1, . . . , n, plus the termination state 0. For all u $ U(x), the state following x is y with probability pxy(u) and the expected cost incurred is nonpositive. This problem arises when we wish to maximize nonnegative rewards up to termination. It includes a classical search problem where the aim, roughly speaking, is to move through the state space looking for states with favorable termination rewards. 
We view the problem within our abstract framework with J̄(x) * 0 and 
TµJ = gµ + PµJ, (4.27) 
with gµ $ 'n being the corresponding nonpositive one-stage cost vector, and Pµ being an n + n substochastic matrix. The components of Pµ are the probabilities pxy 
! µ(x) 
" , x, y = 1, . . . , n. Clearly Assumption D holds. 
Consider the $-PI method (4.24), with Jk+1 computed by solving the fixed point equation J = WkJ , cf. Eq. (4.26). This is a nonsingular n-dimensional system of linear equations, and can be solved by matrix inversion, just like in exact PI for discounted n-state MDP. In particular, using Eqs. (4.26) and (4.27), we have 
Jk+1 = (I ! $Pµk ) !1 ! gµk + (1! $)PµkJk 
" . (4.28)
264 Noncontractive Models Chap. 4 
For a small number of states n, this matrix inversion-based policy evaluation may be simpler than the optimistic PI policy evaluation equation 
Jk+1 = T mk 
µk Jk 
[cf. Eq. (4.20)], which points to an advantage of $-PI. 
Note that based on the relation between the multistep mapping T (#) µ and 
the proximal mapping, discussed in Section 1.2.5 and Exercise 1.2, the policy evaluation Eq. (4.28) may be viewed as an extrapolated proximal iteration. Note also that as $ , 1, the policy evaluation Eq. (4.28) resembles the policy evaluation equation 
Jµk = (I ! $Pµk ) !1gµk 
for $-discounted n-state MDP. An important di#erence, however, is that for a discounted finite-state MDP, exact PI will find an optimal policy in a finite number of iterations, while this is not guaranteed for $-PI. Indeed $-PI does not require that there exists an optimal policy or even that J"(x) is finite for all x. 
Policy Iteration Under I 
Contrary to the case of Assumption D, the important cost improvement property of PI holds under Assumption I. Thus, if µ is a policy and µ̄ satisfies the policy improvement equation Tµ̄Jµ = TJµ, we have 
Jµ = TµJµ - TJµ = Tµ̄Jµ, 
from which we obtain Jµ - lim 
k$% T k µ̄Jµ. 
Since Jµ - J̄ and Jµ̄ = limk$% T k µ̄ J̄ , it follows that 
Jµ - TJµ - Jµ̄. (4.29) 
However, this cost improvement property is not by itself su!cient for the validity of PI under Assumption I (see the deterministic shortest path example of Section 3.1.1). Thus additional conditions are needed to guarantee convergence. To this end we may use the semicontractive framework of Chapter 3, and take advantage of the fact that under Assumption I, J* 
is known to be a fixed point of T . In particular, suppose that we have a set S ( E(X) such that J* 
S = J*. Then J* 
S is a fixed point of T and the theory of Section 3.2 comes into play. Thus, by Prop. 3.2.1 the following hold: 
(a) We have T kJ & J* for every J ' E(X) such that J* + J + J̃ for some J̃ ' S. 
(b) J* is the only fixed point of T within the set of all J ' E(X) such that J* + J + J̃ for some J̃ ' S.
Sec. 4.4 Regularity and Nonstationary Policies 265 
Moreover, by Prop. 3.2.4, if S has the weak PI property and for each sequence {Jm} ( E(X) with Jm . J for some J ' E(X), we have 
H (x, u, J) = lim m$% 
H(x, u, Jm), 
then every sequence of S-regular policies {µk} that can be generated by PI satisfies Jµk . J*. If in addition the set of S-regular policies is finite, there 
exists k̄ - 0 such that µk̄ is optimal. For these properties to hold, it is of course critical that J* 
S = J*. If this is not so, but J* 
S is still a fixed point of T , the VI and PI algorithms may converge to J* 
S rather than to J* (cf. the linear quadratic problem of Section 3.5.4). 
4.4 REGULARITY AND NONSTATIONARY POLICIES 
In this section, we will extend the notion of regularity of Section 3.2 so that it applies more broadly. We will use this notion as our main tool for exploring the structure of the solution set of Bellman’s equation. We will then discuss some applications involving mostly monotone increasing models in this section, as well as in Sections 4.5 and 4.6. We continue to focus on the infinite horizon case of the problem of Section 4.1, but we do not impose for the moment any additional assumptions, such as Assumption I or D. 
We begin with the following extension of the definition of S-regularity, which we will use to prove a general result regarding the convergence properties of VI in the following Prop. 4.4.1. We will apply this result in the context of various applications in Sections 4.4.2-4.4.4, as well as in Sections 4.5 and 4.6. 
Definition 4.4.1: For a nonempty set of functions S ( E(X), we say that a nonempty collection C of policy-state pairs (#, x), with # ' " and x ' X , is S-regular if 
J"(x) = lim sup k$% 
(Tµ0 · · ·Tµk J)(x), * (#, x) ' C, J ' S. 
The essence of the preceding definition of S-regularity is similar to the one of Chapter 3 for stationary policies: for an S-regular collection of pairs (#, x), the value of J"(x) is not a!ected if the starting function is changed from J̄ to any J ' S. It is important to extend the definition of regularity to nonstationary policies because in noncontractive models, stationary policies are generally not su!cient, i.e., the optimal cost over
266 Noncontractive Models Chap. 4 
stationary policies may not be the same as the one over nonstationary policies (cf. Prop. 4.3.2, and the subsequent example). Generally, when referring to an S-regular collection C, we implicitly assume that S and C are nonempty, although on occasion we may state explicitly this fact for emphasis. 
For a given set C of policy-state pairs (#, x), let us consider the function J* 
C ' E(X), given by 
J* C(x) = inf 
{" | (",x)"C} J"(x), x ' X. 
Note that J* C (x) - J*(x) for all x ' X [for those x ' X for which the set 
of policies {# | (#, x) ' C} is empty, we have by convention J* C (x) = #]. 
For an important example, note that in the analysis of Chapter 3, the set of S-regular policies MS of Section 3.2 defines the S-regular collection 
C = & (µ, x) | µ ' MS, x ' X 
' , 
and the corresponding restricted optimal cost function J* S is equal to J* 
C . In Sections 3.2-3.4 we saw that when J* 
S is a fixed point of T , then favorable results are obtained. Similarly, in this section we will see that for an S-regular collection C, when J* 
C is a fixed point of T , interesting results are obtained. 
The following two propositions play a central role in our analysis on this section and the next two, and may be compared with Prop. 3.2.1, which played a pivotal role in the analysis of Chapter 3. 
Proposition 4.4.1: (Well-Behaved Region Theorem) Given a nonempty set S ( E(X), let C be a nonempty collection of policy-state pairs (#, x) that is S-regular. Then: 
(a) For all J ' E(X) such that J + J̃ for some J̃ ' S, we have 
lim sup k$% 
T kJ + J* C . 
(b) For all J # ' E(X) with J # + TJ #, and all J ' E(X) such that J # + J + J̃ for some J̃ ' S, we have 
J # + lim inf k$% 
T kJ + lim sup k$% 
T kJ + J* C . 
Proof: (a) Using the generic relation TJ + TµJ , µ ' M, and the monotonicity of T and Tµ, we have for all k 
(T kJ̃)(x) + (Tµ0 · · ·Tµk!1 J̃)(x), * (#, x) ' C, J̃ ' S.
Sec. 4.4 Regularity and Nonstationary Policies 267 
By letting k & # and by using the definition of S-regularity, it follows that for all (#, x) ' C, J ' E(X), and J̃ ' S with J + J̃ , 
lim sup k$% 
(T kJ)(x) + lim sup k$% 
(T kJ̃)(x) + lim sup k$% 
(Tµ0 · · ·Tµk!1 J̃)(x) = J"(x), 
and by taking infimum of the right side over & # | (#, x) ' C 
' , we obtain 
the result. 
(b) Using the hypotheses J # + TJ #, and J # + J + J̃ for some J̃ ' S, and the monotonicity of T , we have 
J #(x) + (TJ #)(x) + · · · + (T kJ #)(x) + (T kJ)(x). 
Letting k & # and using part (a), we obtain the result. Q.E.D. 
Let us discuss some interesting implications of part (b) of the proposition. Suppose we are given a set S ( E(X), and a collection C that is S-regular. Then: 
(1) J* C is an upper bound to every fixed point J # of T that lies below 
some J̃ ' S (i.e., J # + J̃). Moreover, for such a fixed point J #, the VI algorithm, starting from any J with J* 
C + J + J̃ for some J̃ ' S, ends up asymptotically within the region 
& J ' E(X) | J # + J + J* 
C 
' . 
Thus the convergence of VI is characterized by the well-behaved region 
WS,C = & J ' E(X) | J* 
C + J + J̃ for some J̃ ' S ' , (4.30) 
(cf. the corresponding definition in Section 3.2), and the limit region 
& J ' E(X) | J # + J + J* 
C for all fixed points J # of T 
with J # + J̃ for some J̃ ' S ' . 
The VI algorithm, starting from the former, ends up asymptotically within the latter; cf. Figs. 4.4.1 and 4.4.2. 
(2) If J* C is a fixed point of T (a common case in our subsequent analysis), 
then the VI-generated sequence {T kJ} converges to J* C starting from 
any J in the well-behaved region. If J* C is not a fixed point of T , we 
only have lim supk$% T kJ + J* C for all J in the well-behaved region. 
(3) If the well-behaved region is unbounded above in the sense that WS,C = 
& J ' E(X) | J* 
C + J ' , which is true for example if S = E(X), 
then J # + J* C for every fixed point J # of T . The reason is that for 
every fixed point J # of T we have J # + J for some J ' WS,C, and hence also J # + J̃ for some J̃ ' S, so observation (1) above applies.
268 Noncontractive Models Chap. 4 
J ! J J 
VI Optimal Cost over CFixed Point of T 
C E(X) 
VI: T kJ 
J̃ ! S 
be a fixed point of , we have J* 
C ! 
Well-Behaved RegionWS,CWell-Behaved Region Limit Region 
Figure 4.4.1. Schematic illustration of Prop. 4.4.1. Neither J" C nor J" need to 
be fixed points of T , but if C is S-regular, and there exists J̃ $ S with J" C ! J̃ , 
then J" C demarcates from above the range of fixed points of T that lie below J̃ . 
For future reference, we state these observations as a proposition, which should be compared to Prop. 3.2.1, the stationary special case where C is defined by the set of S-regular stationary policies, i.e., C = 
& (µ, x) | µ ' 
MS , x ' X ' . Figures 4.4.2 and 4.4.3 illustrate some of the consequences 
of Prop. 4.4.1 for two cases, respectively: when S = E(X) while J* C is not 
a fixed point of T , and when S is a strict subset of E(X) while J* C is a fixed 
point of T . 
Proposition 4.4.2: (Uniqueness of Fixed Point of T and Con-vergence of VI) Given a set S ( E(X), let C be a collection of policy-state pairs (#, x) that is S-regular. Then: 
(a) If J # is a fixed point of T with J # + J̃ for some J̃ ' S, then J # + J* 
C . Moreover, J* C is the only possible fixed point of T 
within WS,C. 
(b) We have lim supk$% T kJ + J* C for all J ' WS,C , and if J* 
C is a fixed point of T , then T kJ & J* 
C for all J ' WS,C. 
(c) If WS,C is unbounded from above in the sense that 
WS,C = & J ' E(X) | J* 
C + J ' , 
then J # + J* C for every fixed point J # of T . In particular, if J* 
C is a fixed point of T , then J* 
C is the largest fixed point of T . 
Proof: (a) The first statement follows from Prop. 4.4.1(b). For the second statement, let J # be a fixed point of T with J # ' WS,C. Then from the definition of WS,C , we have J* 
C + J # as well as J # + J̃ for some J̃ ' S, so from Prop. 4.4.1(b) it follows that J # + J* 
C . Hence J # = J* C .
Sec. 4.4 Regularity and Nonstationary Policies 269 
Path of VI Set of solutions of Bellman’s equation J* C 
Paths of VI Unique solution of Bellman’s equation 
Limit Region 
Fixed Points of T 
T S = E(X) 
Well-Behaved Region 
WS,C = 
! 
J | J* C ! J 
" 
Figure 4.4.2. Schematic illustration of Prop. 4.4.2, for the case where S = E(X) 
so that WS,C is unbounded above, i.e., WS,C = & J $ E(X) | J" 
C ! J ' . In 
this figure J" C is not a fixed point of T . The VI algorithm, starting from the 
well-behaved region WS,C , ends up asymptotically within the limit region. 
(b) The result follows from Prop. 4.4.1(a), and in the case where J* C is a 
fixed point of T , from Prop. 4.4.1(b), with J # = J* C . 
(c) See observation (3) in the discussion preceding the proposition. Q.E.D. 
Examples and counterexamples illustrating the preceding proposition are provided by the problems of Section 3.1 for the stationary case where 
C = & (µ, x) | µ ' MS, x ' X 
' . 
Similar to the analysis of Chapter 3, the preceding proposition takes special significance when J* is a fixed point of T and C is rich enough so that J* C = J*, as for example in the case where C is the set ")X of all (#, x), 
or other choices to be discussed later. It then follows that every fixed point J # of T that belongs to S satisfies J # + J*, and that VI converges to J* starting from any J ' E(X) such that J* + J + J̃ for some J̃ ' S. However, there will be interesting cases where J* 
C /= J*, as in shortest path-type problems (see Sections 3.5.1, 4.5, and 4.6). 
Note that Prop. 4.4.2 does not say anything about fixed points of T that lie below J* 
C , and does not give conditions under which J* C is a 
fixed point. Moreover, it does not address the question whether J* is a fixed point of T , or whether VI converges to J* starting from J̄ or from below J*. Generally, it can happen that both, only one, or none of the two
270 Noncontractive Models Chap. 4 
that belongs to S Path of VI Set of solutions of Bellman’s equation J* 
C 
Fixed Points of T S 
Fixed Points of T S 
Well-Behaved Region 
Paths of VI Unique solution of Bellman’s equation 
WS,C = ! 
J | J* C ! J ! J̃ for some J̃ " S 
" 
Figure 4.4.3. Schematic illustration of Prop. 4.4.2, and the set WS,C of Eq. (4.30), for a case where J" 
C is a fixed point of T and S is a strict subset of E(X). 
Every fixed point of T that lies below some J̃ $ S should lie below J" C . Also, the 
VI algorithm converges to J" C starting from within WS,C . If S were unbounded 
from above, as in Fig. 4.4.2, J" C would be the largest fixed point of T . 
functions J* C and J* is a fixed point of T , as can be seen from the examples 
of Section 3.1. 
The Case Where J* C + J̄ 
We have seen in Section 4.3 that the results for monotone increasing and monotone decreasing models are markedly di#erent. In the context of S-regularity of a collection C, it turns out that there are analogous significant di#erences between the cases J* 
C - J̄ and J* C + J̄ . The following propo-
sition establishes some favorable aspects of the condition J* C + J̄ in the 
context of VI. These can be attributed to the fact that J̄ can always be added to S without a#ecting the S-regularity of C, so J̄ can serve as the element J̃ of S in Props. 4.4.1 and 4.4.2 (see the subsequent proof). The following proposition may also be compared with the result on convergence of VI under Assumption D (cf. Prop. 4.3.13). 
Proposition 4.4.3: Given a set S ( E(X), let C be a collection of policy-state pairs (#, x) that is S-regular, and assume that J* 
C + J̄ . Then:
Sec. 4.4 Regularity and Nonstationary Policies 271 
(a) For all J # ' E(X) with J # + TJ #, we have 
J # + lim inf k$% 
T kJ̄ + lim sup k$% 
T kJ̄ + J* C . 
(b) If J* C is a fixed point of T , then J* 
C = J* and we have T kJ̄ & J* 
as well as T kJ & J* for every J ' E(X) such that J* + J + J̃ for some J̃ ' S. 
Proof: (a) If S does not contain J̄ , we can replace S with S̄ = S " {J̄}, and C will still be S̄-regular. By applying Prop. 4.4.1(b) with S replaced by S̄ and J̃ = J̄ , the result follows. 
(b) Assume without loss of generality that J̄ ' S [cf. the proof of part (a)]. By using Prop. 4.4.2(b) with J̃ = J̄ , we have J* 
C = limk$% T kJ̄ . Thus for every policy # = {µ0, µ1, . . .} ' ", 
J* C = lim 
k$% T kJ̄ + lim sup 
k$% Tµ0 · · ·Tµk!1 J̄ = J" , 
so by taking the infimum over # ' ", we obtain J* C + J*. Since generically 
J* C - J*, it follows that J* 
C = J*. Finally, from Prop. 4.4.2(b), T kJ & J* 
for all J ' WS,C , implying the result. Q.E.D. 
As a special case of the preceding proposition, we have that if J* + J̄ and J* is a fixed point of T , then J* = limk$% T kJ̄ , and for every other fixed point J # of T we have J # + J* (apply the proposition with C = ")X and S = {J̄}, in which case J* 
C = J* + J̄). This occurs, among others, in the monotone decreasing models, where TµJ̄ + J̄ for all µ ' M. A special case is the convergence of VI under Assumption D (cf. Prop. 4.3.5). 
The preceding proposition also applies to a classical type of search problem with both positive and negative costs per stage. This is the SSP problem, where at each x ' X we have cost E 
& g(x, u, w) 
' - 0 for all u 
except one that leads to a termination state with probability 1 and nonpositive cost; here J̄(x) = 0 and J* 
C(x) + 0 for all x ' X , but Assumption D need not hold. 
4.4.1 Regularity and Monotone Increasing Models 
We will now return to the monotone increasing model, cf. Assumption I. For this model, we know from Section 4.3 that J* is the smallest fixed point of T within the class of functions J - J̄ , under certain relatively mild assumptions. However, VI may not converge to J* starting from below J* 
(e.g., starting from J̄), and also starting from above J*. In this section
272 Noncontractive Models Chap. 4 
we will address the question of convergence of VI from above J* by using regularity ideas, and in Section 4.5 we will consider the characterization of the largest fixed point of T in the context of deterministic optimal control and infinite-space shortest path problems. We summarize the results of Section 4.3 that are relevant to our development in the following proposition (cf. Props. 4.3.2, 4.3.3, 4.3.9, and 4.3.14). 
Proposition 4.4.4: Let Assumption I hold. Then: 
(a) J* = TJ*, and if J # ' E(X) is such that J # - J̄ and J # - TJ #, then J # - J*. 
(b) For all µ ' M we have Jµ = TµJµ, and if J # ' E(X) is such that J # - J̄ and J # - TµJ #, then J # - Jµ. 
(c) µ! ' M is optimal if and only if Tµ"J* = TJ*. 
(d) If U is a metric space and the sets 
Uk(x,!) = & u ' U(x) 
22 H(x, u, T kJ̄) + ! ' 
are compact for all x ' X , ! ' !, and k, then there exists at least one optimal stationary policy, and we have T kJ & J* for all J ' E(X) with J + J*. 
(e) Given any " > 0, there exists a policy #! ' " such that 
J* + J"! + J* + " e. 
Furthermore, if the scalar $ in part (c) of Assumption I satisfies $ < 1, the policy #! can be taken to be stationary. 
Since under Assumption I there may exist fixed points J # of T with J* + J #, VI may not converge to J* starting from above J*. However, convergence of VI to J* from above, if it occurs, is often much faster than convergence from below, so starting points J - J* may be desirable. One well-known such case is deterministic finite-state shortest path problems where major algorithms, such as the Bellman-Ford method or other label correcting methods have polynomial complexity, when started from J above J*, but only pseudopolynomial complexity when started from J below J* 
[see e.g., [BeT89] (Prop. 1.2 in Ch.4), [Ber98] (Exercise 2.7)]. In the next two subsections, we will consider discounted and undis-
counted optimal control problems with nonnegative cost per stage, and we will establish conditions under which J* is the unique nonnegative fixed point of T , and VI converges to J* from above. Our analysis will proceed as follows:
Sec. 4.4 Regularity and Nonstationary Policies 273 
(a) Define a collection C such that J* C = J*. 
(b) Define a set S ( E+(X) such that J* ' S and C is S-regular. 
(c) Use Prop. 4.4.2 (which shows that J* C is the largest fixed point of T 
within S) in conjunction with Prop. 4.4.4(a) (which shows that J* is the smallest fixed point of T within S) to show that J* is the unique fixed point of T within S. Use also Prop. 4.4.2(b) to show that the VI algorithm converges to J* starting from J ' S such that J - J*. 
(d) Use the compactness condition of Prop. 4.4.4(d), to enlarge the set of functions starting from which VI converges to J*. 
4.4.2 Nonnegative Cost Stochastic Optimal Control 
Let us consider the undiscounted stochastic optimal control problem that involves the mapping 
H(x, u, J) = E & g(x, u, w) + J 
! f(x, u, w) 
"' , (4.31) 
where g is the one-stage cost function and f is the system function. The expected value is taken with respect to the distribution of the random variable w (which takes values in a countable set W ). We assume that 
0 + E & g(x, u, w) 
' < #, * x ' X, u ' U(x), w ' W. 
We consider the abstract DP model with H as above, and with J̄(x) , 0. Using the nonnegativity of g, we can write the cost function of a policy # = {µ0, µ1, . . .} in terms of a limit, 
J"(x0) = lim k$% 
E" x0 
4 k. 
m=0 
g ! xm, µm(xm), wm 
" 5 , x0 ' X, (4.32) 
where E" x0{·} denotes expected value with respect to the probability dis-
tribution induced by # under initial state x0. We will apply the analysis of this section with 
C = & (#, x) | J"(x) < # 
' , 
for which J* C = J*. We assume that C is nonempty, which is true if and 
only if J* is not identically #, i.e., J*(x) < # for some x ' X . Consider the set 
S = -J ' E+(X) | E" 
x0 
& J(xk) 
' & 0, * (#, x0) ' C 
3 . (4.33) 
One interpretation is that the functions J that are in S have the character of Lyapounov functions for the policies # for which the set 
& x0 | J"(x0) < # 
' 
is nonempty.
274 Noncontractive Models Chap. 4 
Note that S is the largest set with respect to which C is regular in the sense that C is S-regular and if C is S#-regular for some other set S#, then S# ( S. To see this we write for all J ' E+(X), (#, x0) ' C, and k, 
(Tµ0 · · ·Tµk!1J)(x0) = E" x0 
& J(xk) 
' + E" 
x0 
4 k&1. 
m=0 
g ! xm, µm(xm), wm 
" 5 , 
where µm, m = 0, 1, . . ., denote generically the components of #. The rightmost term above converges to J"(x0) as k & # [cf. Eq. (4.32)], so by taking upper limit, we obtain 
lim sup k$% 
(Tµ0 · · ·Tµk!1J)(x0) = lim sup k$% 
E" x0 
& J(xk) 
' + J"(x0). (4.34) 
In view of the definition (4.33) of S, this implies that for all J ' S, we have 
lim sup k$% 
(Tµ0 · · ·Tµk!1J)(x0) = J"(x0), * (#, x0) ' C, (4.35) 
so C is S-regular. Moreover, if C is S#-regular and J ' S#, Eq. (4.35) holds, so that [in view of Eq. (4.34) and J ' E+(X)] limk$% E" 
x0 
& J(xk) 
' = 0 for 
all (#, x0) ' C, implying that J ' S. From Prop. 4.4.2, the fixed point property of J* [cf. Prop. 4.4.4(a)], 
and the fact J* C = J*, it follows that T kJ & J* for all J ' S that satisfy 
J - J*. Moreover, if the sets Uk(x,!) of Eq. (4.17) are compact, the convergence of VI starting from below J* will also be guaranteed. We thus have the following proposition, which in addition shows that J* belongs to S and is the unique fixed point of T within S. 
Proposition 4.4.5: (Uniqueness of Fixed Point of T and Con-vergence of VI) Consider the problem corresponding to the mapping (4.31) with g - 0, and assume that J* is not identically #. Then: 
(a) J* belongs to S and is the unique fixed point of T within S. Moreover, we have T kJ & J* for all J - J* with J ' S. 
(b) If U is a metric space, and the sets Uk(x,!) of Eq. (4.17) are compact for all x ' X , ! ' !, and k, we have T kJ & J* for all J ' S, and an optimal stationary policy is guaranteed to exist. 
Proof: (a) We first show that J* ' S. Given a policy # = {µ0, µ1, . . .}, we denote by #k the policy 
#k = {µk, µk+1, . . .}.
Sec. 4.4 Regularity and Nonstationary Policies 275 
We have for all (#, x0) ' C 
J"(x0) = E" x0 
& g ! x0, µ0(x0), w0 
"' + E" 
x0 
& J"1(x1) 
' , (4.36) 
and for all m = 1, 2, . . ., 
E" x0 
& J"m(xm) 
' = E" 
x0 
& g ! xm, µm(xm), wm 
"' + E" 
x0 
& J"m+1(xm+1) 
' , 
(4.37) where {xm} is the sequence generated starting from x0 and using #. By using repeatedly the expression (4.37) for m = 1, . . . , k$ 1, and combining it with Eq. (4.36), we obtain for all k = 1, 2, . . . , 
J"(x0) = E" x0 
& J"k 
(xk) ' + 
k&1. 
m=0 
E" x0 
-g ! xm, µm(xm), wm 
"3 , * (#, x0) ' C. 
The rightmost term above tends to J"(x0) as k & #, so we obtain 
E" x0 
& J"k 
(xk) ' & 0, * (#, x0) ' C. 
Since 0 + J* + J"k , it follows that 
E" x0 
& J*(xk) 
' & 0, * x0 with J*(x0) < #. 
Thus J* ' S while J* (which is equal to J* C) is a fixed point of T . 
For every other fixed point J # of T , we have J # - J! [by Prop. 4.4.4(b)], so if J # belongs to S, by Prop. 4.4.2(a), J # + J! and thus J # = J*. Hence, J* is the unique fixed point of T within the set S. By Prop. 4.4.2(b), we also have T kJ & J* for all J ' S with J - J*. 
(b) This part follows from part (a) and Prop. 4.4.4(d). Q.E.D. 
Note that under the assumptions of the preceding proposition, either T has a unique fixed point within E+(X) (namely J*), or else all the additional fixed points of T within E+(X) lie outside S. To illustrate the limitations of this result, consider the shortest path problem of Section 3.1.1 for the case where the choice at state 1 is either to stay at 1 at cost 0, or move to the destination at cost b > 0. Then Bellman’s equation at state 1 is J(1) = min 
& b, J(1) 
' , and its set of nonnegative solutions is the 
interval [0, b], while we have J* = 0. The set S of Eq. (4.33) here consists of just J* and Prop. 4.4.5 applies, but it is not very useful. Similarly, in the linear-quadratic example of Section 3.1.4, where T has the two fixed points J*(x) = 0 and Ĵ(x) = (%2 $ 1)x2, the set S of Eq. (4.33) consists of just J!. 
Thus the regularity framework of this section is useful primarily in the favorable case where J* is the unique nonnegative fixed point of T . In particular, Prop. 4.4.5 cannot be used to di#erentiate between multiple
276 Noncontractive Models Chap. 4 
fixed points of T , and to explain the unusual behavior in the preceding two examples. In Sections 4.5 and 4.6, we address this issue within the more restricted contexts of deterministic and stochastic optimal control, respectively. 
A consequence of Prop. 4.4.5 is the following condition for VI convergence from above, first discovered and published in the paper by Yu and Bertsekas [YuB15] (Theorem 5.1) within a broader context that also addressed universal measurability issues. 
Proposition 4.4.6: Under the conditions of Prop. 4.4.5, we have T kJ → J* for all J ↑ E+(X) satisfying 
J* ↓ J ↓ cJ*, (4.38) 
for some scalar c > 1. Moreover, J* is the unique fixed point of T within the set 
{ J ↑ E+(X) | J ↓ cJ* for some c > 0 
} . 
Proof: Since J* ↑ S as shown in Prop. 4.4.5, any J satisfying Eq. (4.38), also belongs to the set S of Eq. (4.33), and the result follows from Prop. 4.4.5. Q.E.D. 
Note a limitation of the preceding proposition: in order to find functions J satisfying J* ↓ J ↓ c J* we must essentially know the sets of states x where J*(x) = 0 and J*(x) = ∞. 
4.4.3 Discounted Stochastic Optimal Control 
We will now consider a discounted version of the stochastic optimal control problem of the preceding section. For a policy π = {µ0, µ1, . . .} we have 
Jπ(x0) = lim k→∞ 
Eπ x0 
{ k↓1∑ 
m=0 
αmg ( xm, µm(xm), wm 
) } , 
where α ↑ (0, 1) is the discount factor, and as earlier Eπ x0{·} denotes ex-
pected value with respect to the probability measure induced by π ↑ Π under initial state x0. We assume that the one-stage expected cost is nonnegative, 
0 ↓ E { g(x, u, w) 
} < ∞, ∀ x ↑ X, u ↑ U(x), w ↑ W.
Sec. 4.4 Regularity and Nonstationary Policies 277 
By defining the mapping H as 
H(x, u, J) = E & g(x, u, w) + $J 
! f(x, u, w) 
"' , 
and J̄(x) , 0, we can view this problem within the abstract DP framework of this chapter where Assumption I holds. 
Note that because of the discount factor, the existence of a terminal set of states is not essential for the optimal costs to be finite. Moreover, the nonnegativity of g is not essential for our analysis. Any problem where g can take both positive and negative values, but is bounded below, can be converted to an equivalent problem where g is nonnegative, by adding a suitable constant c to g. Then the cost of all policies will simply change by the constant 
1% k=0 $ 
kc = c/(1$ $). The line of analysis of this section makes a connection between the 
S-regularity notion of Definition 4.4.1 and a notion of stability, which is common in feedback control theory and will be explored further in Section 4.5. We assume that X is a normed space, so that boundedness within X is defined with respect to its norm. We introduce the set 
X! = & x ' X | J*(x) < # 
' , 
which we assume to be nonempty. Given a state x ' X!, we say that a policy # is stable from x if there exists a bounded subset ofX! [that depends on (#, x)] such that the (random) sequence {xk} generated starting from x and using # lies with probability 1 within that subset. We consider the set of policy-state pairs 
C = & (#, x) | x ' X!, # is stable from x 
' , 
and we assume that C is nonempty. Let us say that a function J ' E+(X) is bounded on bounded subsets 
of X! if for every bounded subset X̃ ( X! there is a scalar b such that J(x) + b for all x ' X̃ . Let us also introduce the set 
S = & J ' E+(X) | J is bounded on bounded subsets of X! 
' . 
We assume that C is nonempty, J* ' S, and for every x ' X! and " > 0, there exists a policy # that is stable from x and satisfies J"(x) + J*(x)+ " (thus implying that J* 
C = J*). We have the following proposition. 
Proposition 4.4.7: Under the preceding assumptions, J* is the unique fixed point of T within S, and we have T kJ & J* for all J ' S with J* + J . If in addition U is a metric space, and the sets Uk(x,!) of Eq. (4.17) are compact for all x ' X , ! ' !, and k, we have T kJ & J* 
for all J ' S, and an optimal stationary policy is guaranteed to exist.
278 Noncontractive Models Chap. 4 
Proof: We have for all J ' E(X), (#, x0) ' C, and k, 
(Tµ0 · · ·Tµk!1J)(x0) = $kE" x0 
& J(xk) 
' +E" 
x0 
4 k&1. 
m=0 
$mg ! xm, µm(xm), wm 
" 5 . 
Since (#, x0) ' C, there is a bounded subset ofX! such that {xk} belongs to that subset with probability 1, so if J ' S it follows that $kE" 
x0 
& J(xk) 
' & 
0. Thus by taking limit as k & # in the preceding relation, we have for all (#, x0) ' C and J ' S, 
lim k$% 
(Tµ0 · · ·Tµk!1J)(x0) = lim k$% 
E" x0 
4 k&1. 
m=0 
$mg ! xm, µm(xm), wm 
" 5 
= J"(x0), 
so C is S-regular. Since J* C is equal to J*, which is a fixed point of T , the 
result follows similar to the proof of Prop. 4.4.5. Q.E.D. 
4.4.4 Convergent Models 
In this section we consider a case of an abstract DP model that generalizes both the monotone increasing and the monotone decreasing models. The model is patterned after the stochastic optimal control problem of Example 1.2.1, where the cost per stage function g can take negative as well as positive values. Our main assumptions are that the cost functions of all policies are defined as limits (rather than upper limits), and that $# < J̄(x) + J*(x) for all x ' X. 
These conditions are somewhat restrictive and make the model more similar to the monotone increasing than to the monotone decreasing model, but are essential for the results of this section (for a discussion of the pathological behaviors that can occur without the condition J̄ + J*, see the paper by H. Yu [Yu15]). We will show that J* is a fixed point of T , and that there exists an "-optimal policy for every " > 0. This will bring to bear the regularity ideas and results of Prop. 4.4.2, and will provide a convergence result for the VI algorithm. 
In particular, we denote 
Eb(X) = & J ' E(X) | J(x) > $#, * x ' X 
' , 
and we will assume the following. 
Assumption 4.4.1: 
(a) For all # = {µ0, µ1, . . .} ' ", J" can be defined as a limit: 
J"(x) = lim k$% 
(Tµ0 · · ·Tµk J̄)(x), * x ' X. (4.39)
Sec. 4.4 Regularity and Nonstationary Policies 279 
Furthermore, we have J̄ ' Eb(X) and 
J̄ + J*. 
(b) For each sequence {Jm} ( Eb(X) with Jm & J ' Eb(X), we have 
lim m$% 
H(x, u, Jm) = H (x, u, J) , * x ' X, u ' U(x). 
(c) There exists $ > 0 such that for all J ' Eb(X) and r ' !, 
H(x, u, J + re) + H(x, u, J) + $r, * x ' X, u ' U(x), 
where e is the unit function, e(x) , 1. 
For an example of a type of problem where the convergence condition (4.39) is satisfied, consider the stochastic optimal control problem of Example 1.2.1, assuming that the state space consists of two regions: X1 
where the cost per stage is nonnegative under all controls, and X2 where the cost per stage is nonpositive. Assuming that once the system enters X1 it can never return to X2, the convergence condition (4.39) is satisfied for all #. The same is true for the reverse situation, where once the system enters X2 it can never return to X1. Optimal stopping problems and SSP problems are often of this type. 
We first prove the existence of "-optimal policies and then use it to establish that J* is a fixed point of T . The proofs are patterned after the ones under Assumption I (cf. Props. 4.3.2 and 4.3.3). 
Proposition 4.4.8: Let Assumption 4.4.1 hold. Given any " > 0, there exists a policy #! ' " such that 
J* + J"! + J* + " e. 
Proof: Let {"k} be a sequence such that "k > 0 for all k and 
%. 
k=0 
$k"k = ", (4.40) 
where $ is the scalar of Assumption 4.4.1(c). For each x ' X , consider a sequence of policies 
& #k[x] 
' ( ", with components of #k[x] (to emphasize
280 Noncontractive Models Chap. 4 
their dependence on x) denoted by µk m[x], m = 0, 1, . . ., 
#k[x] = & µk 0 [x], µ 
k 1 [x], . . . 
' , 
such that for k = 0, 1, . . . , 
J"k[x](x) + J*(x) + "k. (4.41) 
Such a sequence exists since J* ' Eb(X). Consider the functions µk defined by 
µk(x) = µk 0 [x](x), * x ' X, (4.42) 
and the functions J̄k defined by 
J̄k(x) = H * x, µk(x), lim 
m$% Tµk 
1 [x] · · ·Tµk 
m[x]J̄ + , * x ' X, k = 0, 1, . . . . 
(4.43) By using Eqs. (4.41)-(4.43), and the continuity property of Assumption 4.4.1(b), we obtain for all x ' X and k = 0, 1, . . ., 
J̄k(x) = H * x, µk 
0 [x](x), lim m$% 
Tµk 1 [x] 
· · ·Tµk m[x]J̄ 
+ 
= lim m$% 
H * x, µk 
0 [x](x), Tµk 1 [x] 
· · ·Tµk m[x]J̄ 
+ 
= lim m$% 
! Tµk 
0 [x] · · ·Tµk 
m[x]J̄ " (x) 
= J"k[x](x) 
+ J*(x) + "k. 
(4.44) 
From Eqs. (4.43), (4.44), and Assumption 4.4.1(c), we have for all x ' X and k = 1, 2, . . ., 
(Tµk!1 J̄k)(x) = H 
! x, µk&1(x), J̄k 
" 
+ H ! x, µk&1(x), J* + "k e 
" 
+ H ! x, µk&1(x), J* 
" + $"k 
+ H * x, µk&1(x), lim 
m$% T µk!1 1 [x] 
· · ·T µk!1 m [x] 
J̄ + + $"k 
= J̄k&1(x) + $"k, 
and finally Tµk!1 
J̄k + J̄k&1 + $"k e, k = 1, 2, . . . . 
Using this inequality and Assumption 4.4.1(c), we obtain 
Tµk!2 Tµk!1 
J̄k + Tµk!2 (J̄k&1 + $"k e) 
+ Tµk!2 J̄k&1 + $2"k e 
+ J̄k&2 + ($"k&1 + $2"k) e.
Sec. 4.4 Regularity and Nonstationary Policies 281 
Continuing in the same manner, we have for k = 1, 2, . . . , 
Tµ0 · · ·Tµk!1 
J̄k + J̄0 + ($"1 + · · ·+ $k"k) e + J* + 
/ k. 
i=0 
$i"i 
0 e. 
Since by Assumption 4.4.1(c), we have J̄ + J* + J̄k, it follows that 
Tµ0 · · ·Tµk!1 
J̄ + J* + 
/ k. 
i=0 
$i"i 
0 e. 
Denote #! = {µ0, µ1, . . .}. Then by taking the limit in the preceding inequality and using Eq. (4.40), we obtain 
J"! + J* + " e. 
Q.E.D. 
By using Prop. 4.4.8 we can prove the following. 
Proposition 4.4.9: Let Assumption 4.4.1 hold. Then J* is a fixed point of T . 
Proof: For every # = {µ0, µ1, . . .} ' " and x ' X , we have using the continuity property of Assumption 4.4.1(b) and the monotonicity of H , 
J"(x) = lim k$% 
(Tµ0Tµ1 · · ·Tµk J̄)(x) 
= Tµ0 
( lim k$% 
Tµ1 · · ·Tµk J̄ 
) (x) 
- (Tµ0J*)(x) 
- (TJ*)(x). 
By taking the infimum of the left-hand side over # ' ", we obtain 
J* - TJ*. 
To prove the reverse inequality, let "1 and "2 be any positive scalars, and let # = {µ0, µ1, . . .} be such that 
Tµ0 J* + TJ* + "1 e, J"1 + J* + "2 e,
282 Noncontractive Models Chap. 4 
where #1 = {µ1, µ2, . . .} (such a policy exists by Prop. 4.4.8). By using the preceding relations and Assumption 4.4.1(c), we have 
J* + J" 
= lim k$% 
Tµ0 Tµ1 
· · ·Tµk J̄ 
= Tµ0 
( lim k$% 
Tµ1 · · ·Tµk 
J̄ 
) 
= Tµ0 J"1 
+ Tµ0 (J* + "2 e) 
+ Tµ0 J* + $"2 e 
+ TJ* + ("1 + $"2) e. 
Since "1 and "2 can be taken arbitrarily small, it follows that 
J* + TJ*. 
Hence J* = TJ*. Q.E.D. 
It is known that J* may not be a fixed point of T if the convergence condition (a) of Assumption 4.4.1 is violated (see the example of Section 3.1.2). Moreover, J* may not be a fixed point of T if either part (b) or part (c) of Assumption 4.4.1 is violated, even when the monotone increase condition J̄ + T J̄ [and hence also the convergence condition of part (a)] is satisfied (see Examples 4.3.1 and 4.3.2). By applying Prop. 4.4.2, we have the following proposition. 
Proposition 4.4.10: Let Assumption 4.4.1 hold, let C be a set of policy-state pairs such that J* 
C = J*, and let S be any subset of E(X) such that C is S-regular. Then: 
(a) J* is the only possible fixed point of T within the set {J ' S | J - J*}. 
(b) We have T kJ & J* for every J ' E(X) such that J* + J + J̃ for some J̃ ' S. 
Proof: By Prop. 4.4.9, J* is a fixed point of T . The result follows from Prop. 4.4.2. Q.E.D. 
4.5 STABLE POLICIES AND DETERMINISTIC OPTIMAL CONTROL 
In this section, we will consider the use of the regularity ideas of the preceding section in conjunction with a particularly favorable class of monotone
Sec. 4.5 Stable Policies and Deterministic Optimal Control 283 
Systemuk = µk(xk) xk 
) µk 
xk+1 = f(xk, uk) 
“Destination” t 
t (cost-free and absorbing) : 
Cost: g(xk, uk) ≥ 0 VI converges to 
Figure 4.5.1 A deterministic optimal control problem with nonnegative cost per stage, and a cost-free and absorbing destination t. 
increasing models. These are the discrete-time infinite horizon deterministic optimal control problems with nonnegative cost per stage, and a destination that is cost-free and absorbing.† Except for the cost nonnegativity, our assumptions are very general, and allow the possibility that the optimal policy may not be stabilizing the system, e.g., may not reach the destination either asymptotically or in a finite number of steps. This situation is illustrated by the one-dimensional linear-quadratic example of Section 3.1.4, where we saw that the Riccati equation may have multiple nonnegative solutions, with the largest solution corresponding to the restricted optimal cost over just the stable policies. 
Our approach is similar to the one of the preceding section. We use forcing functions and a perturbation line of analysis like the one of Section 3.4 to delineate collections C of regular policy-state pairs such that the corresponding restricted optimal cost function J* 
C is a fixed point of T , as required by Prop. 4.4.2. 
To this end, we introduce a new unifying notion of p-stability, which in addition to implying convergence of the generated states to the destination, quantifies the speed of convergence. Here is an outline of our analysis: 
(a) We consider the properties of several distinct cost functions: J*, the overall optimal, and Ĵp, the restricted optimal over just the p-stable policies. Different choices of p may yield different classes of p-stable policies, with different speeds of convergence. 
(b) We show that for any p and associated class of p-stable policies, Ĵp is a solution of Bellman’s equation, and we will characterize the smallest and the largest solutions: they are J*, the optimal cost function, and Ĵ+, the restricted optimal cost function over the class of (finitely) terminating policies. 
(c) We discuss modified versions of the VI and PI algorithms, as substitutes for the standard algorithms, which may not work in general. 
† A related line of analysis for deterministic problems with both positive and negative costs per stage is developed in Exercise 4.9.
284 Noncontractive Models Chap. 4 
Consider a deterministic discrete-time infinite horizon optimal control problem involving the system 
xk+1 = f(xk, uk), k = 0, 1, . . . , (4.45) 
where xk and uk are the state and control at stage k, which belong to sets X and U , referred to as the state and control spaces, respectively, and f : X ) U %& X is a given function. The control uk must be chosen from a constraint set U(xk) ( U that may depend on the current state xk. The cost per stage g(x, u) is assumed nonnegative and possibly extended real-valued: 
0 + g(x, u) + #, * x ' X, u ' U(x), k = 0, 1, . . . . (4.46) 
We assume that X contains a special state, denoted t, which is referred to as the destination, and is cost-free and absorbing: 
f(t, u) = t, g(t, u) = 0, * u ' U(t). 
Except for the cost nonnegativity assumption (4.46), this problem is similar to the one of Section 3.5.5. It arises in many classical control applications involving regulation around a set point, and in finite-state and infinite-state versions of shortest path applications; see Fig. 4.5.1. 
As earlier, we denote policies by # and stationary policies by µ. Given an initial state x0, a policy # = {µ0, µ1, . . .} when applied to the system (4.45), generates a unique sequence of state-control pairs 
! xk, µk(xk) 
" , k = 
0, 1, . . .. The cost of # starting from x0 is 
J"(x0) = %. 
k=0 
g ! xk, µk(xk) 
" , x0 ' X, 
[the series converges to some number in [0,#] thanks to the nonnegativity assumption (4.46)]. The optimal cost function over the set of all policies " is 
J*(x) = inf ""! 
J"(x), x ' X. 
We denote by E+(X) the set of functions J : X %& [0,#]. In our analysis, we will use the set of functions 
J = & J ' E+(X) | J(t) = 0 
' . 
Since t is cost-free and absorbing, this set contains the cost function J" of every # ' ", as well as J*. 
Under the cost nonnegativity assumption (4.46), the problem can be cast as a special case of the monotone increasing model with 
H(x, u, J) = g(x, u) + J ! f(x, u) 
" ,
Sec. 4.5 Stable Policies and Deterministic Optimal Control 285 
and the initial function J̄ being identically zero. Thus Prop. 4.4.4 applies and in particular J* satisfies Bellman’s equation: 
J*(x) = inf u"U(x) 
& g(x, u) + J* 
! f(x, u) 
"' , x ' X. 
Moreover, an optimal stationary policy (if it exists) may be obtained through the minimization in the right side of this equation, cf. Prop. 4.4.4(c). 
The VI method starts from some function J0 ' J , and generates a sequence of functions {Jk} ( J according to 
Jk+1(x) = inf u"U(x) 
& g(x, u)+Jk 
! f(x, u) 
"' , x ' X, k = 0, 1, . . . . (4.47) 
From Prop. 4.4.6, we have that the VI sequence {Jk} converges to J* 
starting from any function J0 ' E+(X) that satisfies 
J* + J0 + cJ*, 
for some scalar c > 0. We also have that VI converges to J* starting from any J0 with 
0 + J0 + J* 
under the compactness condition of Prop. 4.4.4(d). However, {Jk} may not always converge to J* because, among other reasons, Bellman’s equation may have multiple solutions within J . 
The PI method starts from a stationary policy µ0, and generates a sequence of stationary policies {µk} via a sequence of policy evaluations to obtain Jµk from the equation 
Jµk (x) = g ! x, µk(x) 
" + Jµk 
! f ! x, µk(x) 
"" , x ' X, (4.48) 
interleaved with policy improvements to obtain µk+1 from Jµk according to 
µk+1(x) ' argmin u"U(x) 
& g(x, u) + Jµk 
! f(x, u) 
"' , x ' X. (4.49) 
Here, we implicitly assume that the minimum in Eq. (4.49) is attained for each x ' X , which is true under some compactness condition on either U(x) or the level sets of the function g(x, ·)+Jk 
! f(x, ·) 
" , or both. However, 
as noted in Section 4.3.3, PI may not produce a strict improvement of the cost function of a nonoptimal policy, a fact that was demonstrated with the simple deterministic shortest path example of Section 3.1.1. 
The uniqueness of solution of Bellman’s equation within J , and the convergence of VI to J* have been investigated as part of the analysis of Section 3.5.5. There we introduced conditions guaranteeing that J* is the unique solution of Bellman’s equation within a large set of functions
286 Noncontractive Models Chap. 4 
[the near-optimal termination Assumption 3.5.10, but not the cost nonnegativity assumption (4.46)]. Our approach here will make use of the cost nonnegativity but will address the problem under otherwise weaker conditions. 
Our analytical approach will also be di#erent than the approach of Section 3.5.5. Here, we will implicitly rely on the regularity ideas for nonstationary policies that we introduced in Section 4.4, and we will make a connection with traditional notions of feedback control system stability. Using nonstationary policies may be important in undiscounted optimal control problems with nonnegative cost per stage because it is not generally true that there exists a stationary "-optimal policy [cf. the "-optimality result of Prop. 4.4.4(e)]. 
4.5.1 Forcing Functions and p-Stable Policies 
We will introduce a notion of stability that involves a function p : X %& [0,#) such that 
p(t) = 0, p(x) > 0, * x /= t. 
As in Section 3.4, we refer to p as the forcing function, and we associate with it the p-&-perturbed optimal control problem, where & > 0 is a given scalar. This is the same problem as the original, except that the cost per stage is changed to 
g(x, u) + &p(x). 
We denote by J",p,$ the cost function of a policy # ' " in the p-&-perturbed problem: 
J",p,$(x0) = J"(x0) + & %. 
k=0 
p(xk), (4.50) 
where {xk} is the sequence generated starting from x0 and using #. We also denote by Ĵp,$, the corresponding optimal cost function, 
Ĵp,$(x) = inf ""! 
J",p,$(x), x ' X. 
Definition 4.5.1: Let p be a given forcing function. For a state x0 ' X , we say that a policy # is p-stable from x0 if for the sequence {xk} generated starting from x0 and using # we have 
J"(x0) < # and %. 
k=0 
p(xk) < #, (4.51) 
or equivalently [using Eq. (4.50)]
Sec. 4.5 Stable Policies and Deterministic Optimal Control 287 
J",p,$(x0) < #, * & > 0. 
The set of all policies that are p-stable from x0 is denoted by "p,x0 . We define the restricted optimal cost function Ĵp by 
Ĵp(x) = inf ""!p,x 
J"(x), x ' X, (4.52) 
(with the convention that the infimum over the empty set is #). We say that # is p-stable (without qualification) if # ' "p,x for all x ' X such that "p,x /= Ø. The set of all p-stable policies is denoted by "p. 
Note that since Eq. (4.51) does not depend on &, we see that an equivalent definition of a policy # that is p-stable from x0 is that J",p,$(x0) < # for some & > 0 (rather than all & > 0). Thus the set "p,x of p-stable policies from x depends on p and x but not on &. Let us make some observations: 
(a) Rate of convergence to t using p-stable policies : The relation (4.51) shows that the forcing function p quantifies the rate at which the destination is approached using the p-stable policies. As an example, let X = !n and 
p(x) = 2x2%, 
where ' > 0 is a scalar. Then the policies # ' "p,x0 are the ones that force xk towards 0 at a rate faster than O(1/k%), so slower policies are excluded from "p,x0 . 
(b) Approximation property of J",p,$(x): Consider a pair (#, x0) with # ' "p,x0 . By taking the limit as & . 0 in the expression 
J",p,$(x0) = J"(x0) + & %. 
k=0 
p(xk), 
[cf. Eq. (4.50)] and by using Eq. (4.51), it follows that 
lim $'0 
J",p,$(x0) = J"(x0), * pairs (#, x0) with # ' "p,x0 . (4.53) 
From this equation, we have that if # ' "p,x, then J",p,$(x) is finite and di#ers from J"(x) by O(&). By contrast, if # /' "p,x, then J",p,$(x) = # by the definition of p-stability, even though we may have J"(x) < #. 
(c) Limiting property of Ĵp(xk): Consider a pair (#, x0) with # ' "p,x0 . By breaking down J",p,$(x0) into the sum of the costs of the first k stages and the remaining stages, we have for all & > 0 and k > 0, 
J",p,$(x0) = k&1. 
m=0 
g ! xm, µm(xm) 
" + & 
k&1. 
m=0 
p(xm) + J"k,p,$(xk),
288 Noncontractive Models Chap. 4 
where {xk} is the sequence generated starting from x0 and using #, and #k is the policy {µk, µk+1, . . .}. By taking the limit as k & # and using Eq. (4.50), it follows that 
lim k$% 
J"k,p,$(xk) = 0, * pairs (#, x0) with # ' "p,x0 , & > 0. 
Also, since Ĵp(xk) + Ĵp,$(xk) + J"k,p,$(xk), it follows that 
lim k$% 
Jp,$(xk) = 0, * (#, x0) with x0 ' X and # ' "p,x0 , & > 0, 
(4.54) lim k$% 
Ĵp(xk) = 0, * (#, x0) with x0 ' X and # ' "p,x0 . (4.55) 
Terminating Policies and Controllability 
An important special case is when p is equal to the function 
p+(x) = 
, 0 if x = t, 1 if x /= t. 
(4.56) 
For p = p+, a policy # is p+-stable from x if and only if it is terminating from x, i.e., reaches t in a finite number of steps starting from x [cf. Eq. (4.51)]. The set of terminating policies from x is denoted by "+ 
x and it is contained within every other set of p-stable policies "p,x, as can be seen from Eq. (4.51). As a result, the restricted optimal cost function over "+ 
x , 
Ĵ+(x) = inf ""!+ 
x 
J"(x), x ' X, 
satisfies J*(x) + Ĵp(x) + Ĵ+(x) for all x ' X. A policy # is said to be terminating if it is simultaneously terminating from all x ' X such that "+ 
x /= Ø. The set of all terminating policies is denoted by "+. Note that if the state space X is finite, we have for every forcing 
function p ( p+(x) + p(x) + (̄ p+(x), * x ' X, 
for some scalars (, (̄ > 0. As a result it can be seen that "p,x = "+ x and 
Ĵp = Ĵ+, so in e#ect the case where p = p+ is the only case of interest for finite-state problems. 
The notion of a terminating policy is related to the notion of controllability. In classical control theory terms, the system xk+1 = f(xk, uk) is said to be completely controllable if for every x0 ' X , there exists a policy that drives the state xk to the destination in a finite number of steps. This notion of controllability is equivalent to the existence of a terminating policy from each x ' X .
Sec. 4.5 Stable Policies and Deterministic Optimal Control 289 
One of our main results, to be shown shortly, is that J*, Ĵp, and Ĵ+ 
are solutions of Bellman’s equation, with J* being the “smallest” solution and Ĵ+ being the “largest” solution within J . The most favorable situation arises when J* = Ĵ+, in which case J* is the unique solution of Bellman’s equation within J . Moreover, in this case it will be shown that the VI algorithm converges to J* starting with any J0 ' J with J0 - J*, and the PI algorithm converges to J* as well. Once we prove the fixed point property of Ĵp, we will be able to bring to bear the regularity ideas of the preceding section (cf. Prop. 4.4.2). 
4.5.2 Restricted Optimization over Stable Policies 
For a given forcing function p, we denote by 6Xp the e#ective domain of Ĵp, i.e., the set of all x where Ĵp is finite, 
6Xp = & x ' X | Ĵp(x) < # 
' . 
Since Ĵp(x) < # if and only if "p,x /= Ø [cf. Eqs. (4.51) (4.52)], or equivalently J",p,$(x) < # for some # and all & > 0, it follows that 6Xp is also the e#ective domain of Ĵp,$, 
6Xp = & x ' X | "p,x /= Ø} = 
& x ' X | Ĵp,$(x) < # 
' , * & > 0. 
Note that 6Xp may depend on p and may be a strict subset of the e#ective domain of J*, which is denoted by 
X* = & x ' X | J*(x) < # 
' ; 
(cf. Section 3.5.5). The reason is that there may exist a policy # such that J"(x) < #, even when there is no p-stable policy from x (for example, no terminating policy from x). 
Our first objective is to show that as & . 0, the p-&-perturbed optimal cost function Ĵp,$ converges to the restricted optimal cost function Ĵp. 
Proposition 4.5.1 (Approximation Property of Ĵp,$): Let p be a given forcing function and & > 0. 
(a) We have 
J",p,$(x) = J"(x) + w",p,$(x), * x ' X, # ' "p,x, (4.57) 
where w",p,$ is a function such that lim$'0 w",p,$(x) = 0 for all x ' X . 
(b) We have lim $'0 
Ĵp,$(x) = Ĵp(x), * x ' X.
290 Noncontractive Models Chap. 4 
Proof: (a) Follows by using Eq. (4.53) for x ' 6Xp, and by taking wp,$(x) = 
0 for x /' 6Xp. 
(b) By Prop. 4.4.4(e), there exists an "-optimal policy #! for the p-&-perturbed problem, i.e., J"!,p,$(x) + Ĵp,$(x) + " for all x ' X . Moreover, 
for x ' 6Xp we have Ĵp,$(x) < #, so J"!,p,$(x) < #. Hence #! is p-stable 
from all x ' 6Xp, and we have Ĵp + J"! . Using also Eq. (4.57), we have for all & > 0, " > 0, x ' X , and # ' "p,x, 
Ĵp(x)! # " J"! (x)! # " J"!,p,$(x)! # " Ĵp,$(x) " J",p,$(x) = J"(x)+w",p,$(x), 
where lim$'0 w",p,$(x) = 0 for all x ' X . By taking the limit as " . 0, we obtain for all & > 0 and # ' "p,x, 
Ĵp(x) + Ĵp,$(x) + J"(x) + w",p,$(x), * x ' X. 
By taking the limit as & . 0 and then the infimum over all # ' "p,x, we have 
Ĵp(x) + lim $'0 
Ĵp,$(x) + inf ""!p,x 
J"(x) = Ĵp(x), * x ' X, 
from which the result follows. Q.E.D. 
We now consider "-optimal policies, setting the stage for our main proof argument. We know that given any " > 0, by Prop. 4.4.4(e), there exists an "-optimal policy for the p-&-perturbed problem, i.e., a policy # such that J"(x) + J",p,$(x) + Ĵp,$(x) + " for all x ' X . We address the question whether there exists a p-stable policy # that is "-optimal for the restricted optimization over p-stable policies, i.e., a policy # that is p-stable simultaneously from all x ' Xp, (i.e., # ' "p) and satisfies 
J"(x) + Ĵp(x) + ", * x ' X. 
We refer to such a policy as a p-"-optimal policy. 
Proposition 4.5.2 (Existence of p-"-Optimal Policy): Let p be a given forcing function and & > 0. For every " > 0, a policy # that is "-optimal for the p-&-perturbed problem is p-"-optimal, and hence belongs to "p. 
Proof: For any "-optimal policy #! for the p-&-perturbed problem, we have 
J"!,p,$(x) + Ĵp,$(x) + " < #, * x ' 6Xp.
Sec. 4.5 Stable Policies and Deterministic Optimal Control 291 
This implies that #! ' "p. Moreover, for all sequences {xk} generated from 
initial state-policy pairs (#, x0) with x0 ' 6Xp and # ' "p,x0 , we have 
J"!(x0) + J"!,p,$(x0) + Ĵp,$(x0) + " + J"(x0) + & %. 
k=0 
p(xk) + ". 
Taking the limit as & . 0 and using the fact 1% 
k=0 p(xk) < # (since # ' "p,x0), we obtain 
J"!(x0) + J"(x0) + ", * x0 ' 6Xp, # ' "p,x0 . 
By taking infimum over # ' "p,x0 , it follows that 
J"!(x0) + Ĵp(x0) + ", * x0 ' 6Xp, 
which in view of the fact J"!(x0) = Ĵp(x0) = # for x0 /' 6Xp, implies that #! is p-"-optimal. Q.E.D. 
Note that the preceding proposition implies that 
Ĵp(x) = inf ""!p 
J"(x), * x ' X, (4.58) 
which is a stronger statement than the definition Ĵp(x) = inf""!p,x J"(x) for all x ' X . However, it can be shown through examples that there may not exist a restricted-optimal p-stable policy, i.e., a # ' "p such that J" = Ĵp, even if there exists an optimal policy for the original problem. One such example is the one-dimensional linear-quadratic problem of Section 3.1.4 for the case where p = p+. Then, there exists a unique linear stable policy that attains the restricted optimal cost Ĵ+(x) for all x, but this policy is not terminating. Note also that there may not exist a stationary p-"-optimal policy, since generally in undiscounted nonnegative cost optimal control problems there may not exist a stationary "-optimal policy (an example is given following Prop. 4.4.8). 
We now take the first steps for bringing regularity ideas into the analysis. We introduce the set of functions Sp given by 
Sp = -J ' J 
22 J(xk) & 0 for all sequences {xk} generated from initial 
state-policy pairs (#, x0) with x0 ' X and # ' "p,x0 
3 . 
(4.59) In words, Sp consists of the functions in J whose value is asymptotically driven to 0 by all the policies that are p-stable starting from some x0 ' X . Similar to the analysis of Section 4.4.2, we can prove that the collection
292 Noncontractive Models Chap. 4 
Cp = & (#, x0) | # ' "p,x0 
' is Sp-regular. Moreover, Sp is the largest set S 
for which Cp is S-regular. Note that Sp contains Ĵp and Ĵp,$ for all & > 0 [cf. Eq. (4.54), (4.55)]. 
Moreover, Sp contains all functions J such that 
0 + J + cĴp,$ 
for some c > 0 and & > 0. We summarize the preceding discussion in the following proposition, 
which also shows that Ĵp,$ is the unique solution (within Sp) of Bellman’s equation for the p-&-perturbed problem. This will be needed to prove that Ĵp solves the Bellman equation of the unperturbed problem, but also shows that the p-&-perturbed problem can be solved more reliably than the original problem (including by VI methods), and yields a close approximation to Ĵp [cf. Prop. 4.5.1(b)]. 
Proposition 4.5.3: Let p be a forcing function and & > 0. The function Ĵp,$ belongs to the set Sp, and is the unique solution within Sp of Bellman’s equation for the p-&-perturbed problem, 
Ĵp,$(x) = inf u"U(x) 
-g(x, u)+ &p(x)+ Ĵp,$ 
! f(x, u) 
"3 , x ' X. (4.60) 
Moreover, Sp contains Ĵp and all functions J satisfying 
0 + J + cĴp,$ 
for some scalar c > 0. 
Proof: We have Ĵp,$ ' Sp and Ĵp ' Sp by Eq. (4.54), as noted earlier. We also have that Ĵp,$ is a solution of Bellman’s equation (4.60) by Prop. 4.4.4(a). To show that Ĵp,$ is the unique solution within Sp, let J̃ ' Sp be another solution, so that using also Prop. 4.4.4(a), we have 
Ĵp,$(x) + J̃(x) + g(x, u) + &p(x) + J̃ ! f(x, u) 
" , * x ' X, u ' U(x). 
(4.61) Fix " > 0, and let # = {µ0, µ1, . . .} be an "-optimal policy for the p-&-perturbed problem. By repeatedly applying the preceding relation, we have for any x0 ' 6Xp, 
Ĵp,$(x0) + J̃(x0) + J̃(xk)+& k&1. 
m=0 
p(xm)+ k&1. 
m=0 
g ! xm, µm(xm) 
" , * k - 1, 
(4.62)
Sec. 4.5 Stable Policies and Deterministic Optimal Control 293 
where {xk} is the state sequence generated starting from x0 and using #. We have J̃(xk) & 0 (since J̃ ' Sp and # ' "p by Prop. 4.5.2), so that 
lim k$% 
4 J̃(xk) + & 
k&1. 
m=0 
p(xm) + k&1. 
m=0 
g ! xm, µm(xm) 
" 5 
= J",$(x0) 
+ Ĵp,$(x0) + ". (4.63) 
By combining Eqs. (4.62) and (4.63), we obtain 
Ĵp,$(x0) + J̃(x0) + Ĵp,$(x0) + ", * x0 ' 6Xp. 
By letting " & 0, it follows that Ĵp,$(x0) = J̃(x0) for all x0 ' 6Xp. Also for 
x0 /' 6Xp, we have Ĵp,$(x0) = J̃(x0) = # [since Ĵp,$(x0) = # for x0 /' 6Xp 
and Ĵp,$ + J̃ , cf. Eq. (4.61)]. Thus Ĵp,$ = J̃ , proving that Ĵp,$ is the unique solution of the Bellman Eq. (4.60) within Sp. Q.E.D. 
We next show our main result in this section, namely that Ĵp is the unique solution of Bellman’s equation within the set of functions 
Wp = {J ' Sp | Ĵp + J}. (4.64) 
Moreover, we show that the VI algorithm yields Ĵp in the limit for any initial J0 ' Wp. This result is intimately connected with the regularity ideas of Section 4.4. The idea is that the collection Cp = 
& (#, x0) | # ' "p,x0 
' is 
Sp-regular, as noted earlier. In view of this and the fact that J* Cp 
= Ĵp, 
the result will follow from Prop. 4.4.2 once Ĵp is shown to be a solution of Bellman’s equation. This latter property is shown essentially by taking the limit as & . 0 in Eq. (4.60). 
Proposition 4.5.4: Let p be a given forcing function. Then: 
(a) Ĵp is the unique solution of Bellman’s equation 
J(x) = inf u"U(x) 
-g(x, u) + J 
! f(x, u) 
"3 , x ' X, (4.65) 
within the set Wp of Eq. (4.64). 
(b) (VI Convergence) If {Jk} is the sequence generated by the VI algorithm (4.47) starting with some J0 ' Wp, then Jk & Ĵp. 
(c) (Optimality Condition) If µ̂ is a p-stable stationary policy and 
µ̂(x) ' argmin u"U(x) 
& g(x, u) + Ĵp 
! f(x, u) 
"' , * x ' X, (4.66)
294 Noncontractive Models Chap. 4 
then µ̂ is optimal over the set of p-stable policies. Conversely, if µ̂ is optimal within the set of p-stable policies, then it satisfies the preceding condition (4.66). 
Proof: (a), (b) We first show that Ĵp is a solution of Bellman’s equation. Since Ĵp,$ is a solution of Bellman’s equation for the p-&-perturbed problem (cf. Prop. 4.5.3) and Ĵp,$ - Ĵp [cf. Prop. 4.5.1(b)], we have for all & > 0, 
Ĵp,$(x) = inf u"U(x) 
-g(x, u) + &p(x) + Ĵp,$ 
! f(x, u) 
"3 
- inf u"U(x) 
-g(x, u) + Ĵp,$ 
! f(x, u) 
"3 
- inf u"U(x) 
-g(x, u) + Ĵp 
! f(x, u) 
"3 . 
By taking the limit as & . 0 and using the fact lim$'0 Ĵp,$ = Ĵp [cf. Prop. 4.5.1(b)], we obtain 
Ĵp(x) - inf u"U(x) 
-g(x, u) + Ĵp 
! f(x, u) 
"3 , * x ' X. (4.67) 
For the reverse inequality, let {&m} be a sequence with &m . 0. From Prop. 4.5.3, we have for all m, x ' X , and u ' U(x), 
g(x, u) + &mp(x) + Ĵp,$m ! f(x, u) 
" - inf 
v"U(x) 
-g(x, v) + &mp(x) 
+ Ĵp,$m ! f(x, v) 
"3 
= Ĵp,$m(x). 
Taking the limit as m & #, and using the fact lim$m'0 Ĵp,$m = Ĵp [cf. Prop. 4.5.1(b)], we have 
g(x, u) + Ĵp ! f(x, u) 
" - Ĵp(x), * x ' X, u ' U(x), 
so that 
inf u"U(x) 
-g(x, u) + Ĵp 
! f(x, u) 
"3 - Ĵp(x), * x ' X. (4.68) 
By combining Eqs. (4.67) and (4.68), we see that Ĵp is a solution of Bell-man’s equation. We also have Ĵp ' Sp by Prop. 4.5.3, implying that Ĵp ' Wp and proving part (a) except for the uniqueness assertion. Part
Sec. 4.5 Stable Policies and Deterministic Optimal Control 295 
(b) and the uniqueness part of part (a) follow from Prop. 4.4.2; see the discussion preceding the proposition. 
(c) If µ is p-stable and Eq. (4.66) holds, then 
Ĵp(x) = g ! x, µ(x) 
" + Ĵp 
! f(x, µ(x)) 
" , x ' X. 
By Prop. 4.4.4(b), this implies that Jµ + Ĵp, so µ is optimal over the set of p-stable policies. Conversely, assume that µ is p-stable and Jµ = Ĵp. Then by Prop. 4.4.4(b), we have 
Ĵp(x) = g ! x, µ(x) 
" + Ĵp 
! f(x, µ(x)) 
" , x ' X, 
and since [by part (a)] Ĵp is a solution of Bellman’s equation, 
Ĵp(x) = inf u"U(x) 
& g(x, u) + Ĵp 
! f(x, u) 
"' , x ' X. 
Combining the last two relations, we obtain Eq. (4.66). Q.E.D. 
As a supplement to the preceding proposition, we note the specialization of Prop. 4.4.5 that relates to the optimal cost function J*. 
Proposition 4.5.5: Let S! be the set 
S! = -J ' J 
22 J(xk) & 0 for all sequences {xk} generated from 
initial state-policy pairs (#, x0) with J"(x0) < # 3 , 
and W! be the set 
W! = & J ' S! | J* + J 
' . 
Then J* belongs to S! and is the unique solution of Bellman’s equation within S!. Moreover, we have T kJ & J* for all J ' W!. 
Proof: Follows from Prop. 4.4.5 in the deterministic special case where wk takes a single value. Q.E.D. 
We now consider the special case where p is equal to the function p+(x) = 1 for all x /= t [cf. Eq. (4.56)]. Then the set of p+-stable policies from x is "+ 
x , the set of terminating policies from x, and the corresponding restricted optimal cost is Ĵ+(x): 
Ĵ+(x) = Ĵp+(x) = inf ""!+ 
x 
J"(x) = inf ""!+ 
J"(x), x ' X,
296 Noncontractive Models Chap. 4 
[the last equality follows from Eq. (4.58)]. In this case, the set Sp+ of Eq. (4.59) is the entire set J , 
Sp+ = J , 
since for all J ' J and all sequences {xk} generated from initial state-policy pairs (#, x0) with x0 ' X and # terminating from x0, we have J(xk) = 0 for k su!ciently large. Thus, the corresponding set of Eq. (4.64) is 
W+ = {J ' J | Ĵ+ + J}. 
By specializing to the case p = p+ the result of Prop. 4.5.4, we obtain the following proposition, which makes a stronger assertion than Prop. 4.5.4(a), namely that Ĵ+ is the largest solution of Bellman’s equation within J (rather than the smallest solution within W+). 
Proposition 4.5.6: 
(a) Ĵ+ is the largest solution of the Bellman equation (4.65) within J , i.e., Ĵ+ is a solution and if J # ' J is another solution, then J # + Ĵ+. 
(b) (VI Convergence) If {Jk} is the sequence generated by the VI algorithm (4.47) starting with some J0 ' J with J0 - Ĵ+, then Jk & Ĵ+. 
(c) (Optimality Condition) If µ+ is a terminating stationary policy and 
µ+(x) ' argmin u"U(x) 
& g(x, u) + Ĵ+ 
! f(x, u) 
"' , * x ' X, (4.69) 
then µ+ is optimal over the set of terminating policies. Con-versely, if µ+ is optimal within the set of terminating policies, then it satisfies the preceding condition (4.69). 
Proof: In view of Prop. 4.5.4, we only need to show that Ĵ+ is the largest solution of the Bellman equation. From Prop. 4.5.4(a), Ĵ+ is a solution that belongs to J . If J # ' J is another solution, we have J # + J̃ for some J̃ ' W+, so J # = T kJ # + T kJ̃ for all k. Since T kJ̃ & Ĵ+, it follows that J # + Ĵ+. Q.E.D. 
We illustrate Props. 4.5.4 and 4.5.6 in Fig. 4.5.2. In particular, each forcing function p delineates the set of initial functions Wp from which VI converges to Ĵp. The function Ĵp is the minimal element of Wp. Moreover, we have Wp 1Wp& = Ø if Ĵp /= Ĵp& , in view of the VI convergence result of Prop. 4.5.4(b).
Sec. 4.5 Stable Policies and Deterministic Optimal Control 297 
VI converges to J+ 
from within W+ VI converges to Ĵp 
from within Wp 
W+ = ! 
J | J ! J+, J(t) = 0 " 
Ĵp 
Ĵp! 
p Wp t W+ 
Wp! 
Wp: Functions J ! Ĵp with J 
with J(xk) ! 0 for all p-stable ! 
C J! 
Ĵ+ 
W! 
C 0 
Path of VI Set of solutions of Bellman’s equation Set of solutions of Bellman’s equation 
Figure 4.5.2 Schematic two-dimensional illustration of the results of Prop. 4.5.4 and 4.5.6. The functions J", Ĵ+, and Ĵp are all solutions of Bellman’s equation. Moreover J" and Ĵ+ are the smallest and largest solutions, respectively. Each p 
defines the set of initial functions Wp from which VI converges to Ĵp from above. For two forcing functions p and p&, we have Wp%Wp! = Ø if Ĵp &= Ĵp! . Moreover, 
Wp contains no solutions of Bellman’s equation other than Ĵp. It is also possible that Wp consists of just Ĵp. 
Note a significant fact: Proposition 4.5.6(b) implies that VI converges to Ĵ+ starting from the readily available initial condition 
J0(x) = 
, 0 if x = t, # if x /= t. 
For this choice of J0, the value Jk(x) generated by VI is the optimal cost that can be achieved starting from x subject to the constraint that t is reached in k steps or less. As we have noted earlier, in shortest-path type problems VI tends to converge faster when started from above. 
Consider now the favorable case where terminating policies are sufficient, in the sense that Ĵ+ = J*; cf. Fig. 4.5.3. Then, from Prop. 4.5.6, it follows that J* is the unique solution of Bellman’s equation within J , and the VI algorithm converges to J* from above, i.e., starting from any J0 ' J with J0 - J*. Under additional conditions, such as finiteness of U(x) for all x ' X [cf. Prop. 4.4.4(d)], VI converges to J* starting from any J0 ' E+(X) with J0(t) = 0. These results are consistent with our analysis of Section 3.5.5. 
Examples of problems where terminating policies are su!cient include linear-quadratic problems under the classical conditions of controllability and observability, and finite-node deterministic shortest path prob-
298 Noncontractive Models Chap. 4 
C 0 
Paths of VI Unique solution of Bellman’s equation 
Paths of VI Unique solution of Bellman’s equation Unique solution of Bellman’s equation 
) Ĵ+ = J* 
Paths of VI Under Compactness Paths of VI Under Compactness 
Figure 4.5.3 Schematic two-dimensional illustration of the favorable case where Ĵ+ = J". Then J" is the unique solution of Bellman’s equation within J , and the VI algorithm converges to J" from above [and also starting from any J0 " 0 under a suitable compactness condition; cf. Prop. 4.4.4(d)]. 
lems with all cycles having positive length. Note that in the former case, despite the fact Ĵ+ = J*, there is no optimal terminating policy, since the only optimal policy is a linear policy that drives the system to the origin asymptotically, but not in finite time. 
Let us illustrate the results of this section with two examples. 
Example 4.5.1 (Minimum Energy Stable Control of Linear Systems) 
Consider the linear-quadratic problem of Section 3.5.4. We assume that there exists at least one linear stable policy, so that J" is real-valued. However, we are making no assumptions on the state weighting matrix Q other than positive semidefiniteness. This includes the case Q = 0, when J"(x) * 0. In this case an optimal policy is µ"(x) * 0, which may not be stable, yet the problem of finding a stable policy that minimizes the “control energy” (a cost that is positive definite quadratic on the control with no penalty on the state) among all stable policies is meaningful. 
We consider the forcing function 
p(x) = -x-2, 
so the p-%-perturbed problem includes a positive definite state penalty and from the classical linear-quadratic results, Ĵp,$ is a positive definite quadratic function x&P$x, where P$ is the unique solution of the %-perturbed Riccati equation 
P$ = A& ! P$ ! P$B(B&P$B +R)!1B&P$ 
" A+Q+ %I, (4.70)
Sec. 4.5 Stable Policies and Deterministic Optimal Control 299 
within the class of positive semidefinite matrices. By Prop. 4.5.1, we have Ĵp(x) = x&P̂ x, where P̂ = lim$'0 P$ is positive semidefinite, and solves the (unperturbed) Riccati equation 
P = A& ! P ! PB(B&PB +R)!1B&P 
" A+Q. 
Moreover, by Prop. 4.5.4(a), P̂ is the largest solution among positive semidefinite matrices, since all positive semidefinite quadratic functions belong to the set Sp of Eq. (4.59). By Prop. 4.5.4(c), any stable stationary policy µ̂ that is optimal among the set of stable policies must satisfy the optimality condition 
µ̂(x) $ argmin u#(m 
& u&Ru+ (Ax+Bu)&P̂ (Ax+Bu) 
' , % x $ 'n, 
[cf. Eq. (4.66)], or equivalently, by setting the gradient of the minimized expression to 0, 
(R +B&P̂B)µ̂(x) = !B&P̂Ax. (4.71) 
We may solve Eq. (4.71), and check if any of its solutions µ̂ is p-stable; if this is so, µ̂ is optimal within the class of p-stable policies. Note, however, that in the absence of additional conditions, it is possible that some policies µ̂ that solve Eq. (4.71) are p-unstable. 
In the case where there is no linear stable policy, the p-%-perturbed cost function Ĵp,$ need not be real-valued, and the %-perturbed Riccati equation (4.70) may not have any solution (consider for example the case where n = 1, m = 1, A = 2, B = 0, and Q = R = 1). Then, Prop. 4.5.6 still applies, but the preceding analytical approach needs to be modified. 
As noted earlier, the Bellman equation may have multiple solutions corresponding to di#erent forcing functions p, with each solution being unique within the corresponding set Wp of Eq. (4.64), consistently with Prop. 4.5.4(a). The following is an illustrative example. 
Example 4.5.2 (An Optimal Stopping Problem) 
Consider an optimal stopping problem where the state space X is 'n. We identify the destination with the origin of 'n, i.e., t = 0. At each x )= 0, we may either stop (move to the origin) at a cost c > 0, or move to state &x at cost -x-, where & is a scalar with 0 < & < 1; see Fig. 4.5.4.† Thus the Bellman equation has the form 
J(x) = -min 
& c, -x-+ J(&x) 
' if x )= 0, 
0 if x = 0. 
† In this example, the salient feature of the policy that never stops at an x )= 0 is that it drives the system asymptotically to the destination according to an equation of the form xk+1 = f(xk), where f is a contraction mapping. The example admits generalization to the broader class of optimal stopping problems that have this property. For simplicity in illustrating our main point, we consider here the special case where f(x) = &x with & $ (0, 1).
300 Noncontractive Models Chap. 4 
(0) = 0 
x ! 
! (1 " !)c 
c Cost !x! (1 
! !x (1 
x c Cost c Cost Stop Cone 
Stop Cone 
Stop Cone C 
Figure 4.5.4 Illustration of the stopping problem of Example 4.5.2. The optimal policy is to stop outside the sphere of radius (1' ")c and to continue otherwise. Each cone C of the state space defines a di!erent solution Ĵp of Bellman’s equation, with Ĵp(x) = c for all nonzero x $ C, and a corresponding region of convergence of the VI algorithm. 
Let us consider first the forcing function 
p(x) = -x-. 
Then it can be verified that all policies are p-stable. We have 
J"(x) = Ĵp(x) = min 
, c, 
1 1! & 
-x-
7 , % x $ 'n, 
and the optimal cost function of the corresponding p-%-perturbed problem is 
Ĵp,$(x) = min 
, c+ %-x-, 
1 + % 1! & 
-x-
7 , % x $ 'n. 
Here the set Sp of Eq. (4.59) is given by 
Sp = -J $ J | lim 
x$0 J(x) = 0 
3 , 
and the corresponding set Wp of Eq. (4.64) is given by 
Wp = -J $ J | J" " J, lim 
x$0 J(x) = 0 
3 . 
Let us consider next the forcing function 
p+(x) = -1 if x )= 0, 0 if x = 0.
Sec. 4.5 Stable Policies and Deterministic Optimal Control 301 
(0) = 0 (0) = 0 (0) = 0 
Ĵ(x) 
x ! x ! x ! 
) J!(x) ) J+(x) 
x c Cost x c Cost x c Cost 
x0 a 
Figure 4.5.5 Illustration of three solutions of Bellman’s equation in the onedimensional case (n = 1) of the stopping problem of Example 4.5.2. The solution in the middle is specified by a scalar x0 > 0, and has the form 
Ĵ(x) = 
, 0 if x = 0, 
1 1!% 
|x| if 0 < x < (1 ' ")c and x = "kx0 for some k " 0, c otherwise. 
Then the p+-stable policies are the terminating policies. Since stopping at some time and incurring the cost c is a requirement for a p+-stable policy, it follows that the optimal p+-stable policy is to stop as soon as possible, i.e., stop at every state. The corresponding restricted optimal cost function is 
Ĵ+(x) = -c if x )= 0, 0 if x = 0. 
The optimal cost function of the corresponding p+-%-perturbed problem is 
Ĵp+,$(x) = -c+ % if x )= 0, 0 if x = 0, 
since in the p+-%-perturbed problem it is again optimal to stop as soon as possible, at cost c+ %. Here the set Sp+ is equal to J , and the corresponding 
set W+ is equal to & J $ J | Ĵ+ " J 
' . 
However, there are infinitely many additional solutions of Bellman’s equation between the largest and smallest solutions J" and Ĵ+. For example, when n > 1, functions J $ J such that J(x) = J"(x) for x in some cone and J(x) = Ĵ+(x) for x in the complementary cone are solutions; see Fig. 4.5.4. There is also a corresponding infinite number of regions of convergence Wp of VI [cf. Eq. (4.64)]. Also VI converges to J" starting from any J0 with 0 " J0 " J" [cf. Prop. 4.4.4(d)]. Figure 4.5.5 illustrates additional solutions of Bellman’s equation of a di#erent character. 
4.5.3 Policy Iteration Methods 
Generally, the standard PI algorithm [cf. Eqs. (4.48), (4.49)] produces unclear results under our assumptions. The following example provides an instance where the PI algorithm may converge to either an optimal or a strictly suboptimal policy.
302 Noncontractive Models Chap. 4 
Example 4.5.3 (Counterexample for PI) 
Consider the case X = {0, 1}, U(0) = U(1) = {0, 1}, and the destination is t = 0. Let also 
f(x, u) = -0 if u = 0, x if u = 1, 
g(x, u) = -1 if u = 0, x = 1, 0 if u = 1 or x = 0. 
This is a one-state-plus-destination shortest path problem where the control u = 0 moves the state from x = 1 to x = 0 (the destination) at cost 1, while the control u = 1 keeps the state unchanged at cost 0 (cf. the problem of Section 3.1.1). The policy µ" that keeps the state unchanged is the only optimal policy, with Jµ"(x) = J"(x) = 0 for both states x. However, under any forcing function p with p(1) > 0, the policy µ̂, which moves from state 1 to 0, is the only p-stable policy, and we have Jµ̂(1) = Ĵp(1) = 1. The standard PI algorithm (4.48), (4.49) when started with µ", it will repeat µ". If this algorithm is started with µ̂, it may generate µ" or it may repeat µ̂, depending on how the policy improvement iteration is implemented. The reason is that for both x we have 
µ̂(x) $ arg min u#{0,1} 
-g(x, u) + Ĵp 
! f(x, u) 
"3 , 
as can be verified with a straightforward calculation. Thus a rule for breaking a tie in the policy improvement operation is needed, but such a rule may not be obvious in general. 
For another illustration, consider the stopping problem of Example 4.5.2. There if PI is started with the policy that stops at every state, it repeats that policy, and this policy is not optimal even within the class of stable policies with respect to the forcing function p(x) = 2x2. 
Motivated by the preceding examples, we consider several types of PI methods that bypass the di!culty above either through assumptions or through modifications. We first consider a favorable case where the standard PI algorithm is reliable. This is the case where the terminating policies are su!cient, in the sense that J* = Ĵ+, as in Section 3.5.5. 
Policy Iteration for the Case J* = Ĵ+ 
The standard PI algorithm starts with a stationary policy µ0, and generates a sequence of stationary policies {µk} via a sequence of policy evaluations to obtain Jµk from the equation 
Jµk (x) = g ! x, µk(x) 
" + Jµk 
! f ! x, µk(x) 
"" , x ' X, (4.72) 
interleaved with policy improvements to obtain µk+1 from Jµk according to 
µk+1(x) ' argmin u"U(x) 
& g(x, u) + Jµk 
! f(x, u) 
"' , x ' X. (4.73)
Sec. 4.5 Stable Policies and Deterministic Optimal Control 303 
We implicitly assume here that Eq. (4.72) can be solved for Jµk , and that the minimum in Eq. (4.73) is attained for each x ' X , which is true under some compactness condition on either U(x) or the level sets of the function g(x, ·) + Jk 
! f(x, ·) 
" , or both. 
Proposition 4.5.7: (Convergence of PI) Assume that J* = Ĵ+. Then the sequence {Jµk} generated by the PI algorithm (4.72), (4.73), satisfies Jµk (x) . J*(x) for all x ' X . 
Proof: For a stationary policy µ, let µ̄ satisfy the policy improvement equation 
µ̄(x) ' argmin u"U(x) 
& g(x, u) + Jµ 
! f(x, u) 
"' , x ' X. 
We have shown that 
Jµ(x) - inf u"U(x) 
& g(x, u) + Jµ 
! f(x, u) 
"' - Jµ̄(x), x ' X ; (4.74) 
cf. Eq. (4.29). Using µk and µk+1 in place of µ and µ̄, we see that the sequence {Jµk} generated by PI converges monotonically to some function J% ' E+(X), i.e., Jµk . J%. Moreover, from Eq. (4.74) we have 
J%(x) - inf u"U(x) 
& g(x, u) + J% 
! f(x, u) 
"' , x ' X, 
as well as 
g(x, u) + Jµk 
! f(x, u) 
" - J%(x), x ' X, u ' U(x). 
We now take the limit in the second relation as k & #, then take the infimum over u ' U(x), and then combine with the first relation, to obtain 
J%(x) - inf u"U(x) 
& g(x, u) + J% 
! f(x, u) 
"' - J%(x), x ' X. 
Thus J% is a solution of Bellman’s equation, satisfying J% - J* (since Jµk - J* for all k) and J% ' J (since Jµk ' J ), so by Prop. 4.5.6(a), it must satisfy J% = J*. Q.E.D. 
A Perturbed Version of Policy Iteration for the Case J* /= Ĵ+ 
We now consider PI algorithms without the condition J* = Ĵ+. We provide a version of the PI algorithm, which uses a given forcing function p that is fixed, and generates a sequence {µk} of p-stable policies such that
304 Noncontractive Models Chap. 4 
Jµk & Ĵp. Related algorithms were given in Sections 3.4 and 3.5.1. The following assumption requires that the algorithm generates p-stable policies exclusively, which can be quite restrictive. For instance it is not satisfied for the problem of Example 4.5.3. 
Assumption 4.5.1: For each & > 0 there exists at least one p-stable stationary policy µ such that Jµ,p,$ ' Sp. Moreover, given a p-stable stationary policy µ and a scalar & > 0, every stationary policy µ such that 
µ(x) ' arg min u"U(x) 
-g(x, u) + Jµ,p,$ 
! f(x, u) 
"3 , * x ' X, 
is p-stable, and at least one such policy exists. 
The perturbed version of the PI algorithm is defined as follows. Let {&k} be a positive sequence with &k . 0, and let µ0 be a p-stable policy that satisfies Jµ0,p,$0 
' Sp. One possibility is that µ0 is an optimal policy for the &0-perturbed problem (cf. the discussion preceding Prop. 4.5.3). At iteration k, we have a p-stable policy µk, and we generate a p-stable policy µk+1 according to 
µk+1(x) ' argmin u"U(x) 
& g(x, u) + Jµk,p,$k 
! f(x, u) 
"' , x ' X. (4.75) 
Note that by Assumption 4.5.1 the algorithm is well-defined, and is guaranteed to generate a sequence of p-stable stationary policies. We have the following proposition. 
Proposition 4.5.8: Let Assumption 4.5.1 hold. Then for a sequence of p-stable policies {µk} generated by the perturbed PI algorithm (4.75), we have Jµk,p,$k 
. Ĵp and Jµk & Ĵp. 
Proof: Since the forcing function p is kept fixed, to simplify notation, we abbreviate Jµ,p,$ with Jµ,$ for all policies µ and scalars & > 0. Also, we will use the mappings Tµ : E+(X) %& E+(X) and Tµ,$ : E+(X) %& E+(X) given by 
(TµJ)(x) = g ! x, µ(x) 
" + J 
! f(x, µ(x)) 
" , x ' X, 
(Tµ,$J)(x) = g ! x, µ(x) 
" + &p(x) + J 
! f(x, µ(x)) 
" , x ' X. 
Moreover, we will use the mapping T : E+(X) %& E+(X) given by 
(TJ)(x) = inf u"U(x) 
& g(x, u) + J 
! f(x, u) 
"' , x ' X.
Sec. 4.5 Stable Policies and Deterministic Optimal Control 305 
The algorithm definition (4.75) implies that for all integer m - 1 we have for all x0 ' X , 
Jµk ,$k (x0) - (TJµk,$k 
)(x0) + &kp(x0) 
= (Tµk+1,$k Jµk ,$k 
)(x0) 
- (Tm µk+1,$k 
Jµk ,$k )(x0) 
- (Tm µk+1,$k 
J̄)(x0), 
where J̄ is the identically zero function [J̄(x) , 0]. From this relation we obtain 
Jµk,$k (x0) - lim 
m$% (Tm 
µk+1,$k J̄)(x0) 
= lim m$% 
4 m&1. 
&=0 
! g ! x&, µk+1(x&) 
" + &kp(x&) 
" 5 
- Jµk+1,$k+1 (x0), 
as well as 
Jµk ,$k (x0) - (TJµk,$k 
)(x0) + &kp(x0) - Jµk+1,$k+1 (x0). 
It follows that {Jµk,$k } is monotonically nonincreasing, so that Jµk ,$k 
. J% for some J%, and 
lim k$% 
TJµk,$k = J%. (4.76) 
We also have, using the fact J% + Jµk ,$k , 
inf u"U(x) 
& g(x, u) + J% 
! f(x, u) 
"' + lim 
k$% inf 
u"U(x) 
& g(x, u) + Jµk,$k 
! f(x, u) 
"' 
+ inf u"U(x) 
lim k$% 
& g(x, u) + Jµk,$k 
! f(x, u) 
"' 
= inf u"U(x) 
, g(x, u) + lim 
k$% Jµk ,$k 
! f(x, u) 
"7 
= inf u"U(x) 
& g(x, u) + J% 
! f(x, u) 
"' . 
Thus equality holds throughout above, so that 
lim k$% 
TJµk,$k = TJ%. 
Combining this with Eq. (4.76), we obtain J% = TJ%, i.e., J% solves Bellman’s equation. We also note that J% + Jµ0,$0 
and that Jµ0,$0 ' Sp by 
assumption, so that J% ' Sp. By Prop. 4.5.4(a), it follows that J% = Ĵp. Q.E.D.
306 Noncontractive Models Chap. 4 
Note that despite the fact Jµk & Ĵp, the generated sequence {µk} may exhibit some serious pathologies in the limit. In particular, if U is a metric space and {µk}K is a subsequence of policies that converges to some µ̄, in the sense that 
lim k$%, k"K 
µk(x) = µ̄(x), * x ' X, 
it does not follow that µ̄ is p-stable. In fact it is possible to construct examples where the generated sequence of p-stable policies {µk} satisfies limk$% Jµk = Ĵp = J*, yet {µk} may converge to a p-unstable policy 
whose cost function is strictly larger than Ĵp. 
An Optimistic Policy Iteration Method 
Let us consider an optimistic variant of PI, where policies are evaluated inexactly, with a finite number of VIs. We use a fixed forcing function p. The algorithm aims to compute Ĵp, the restricted optimal cost function over the p-stable policies, and generates a sequence {Jk, µk} according to 
TµkJk = TJk, Jk+1 = Tmk 
µk Jk, k = 0, 1, . . . , (4.77) 
where mk is a positive integer for each k. We assume that a policy µk 
satisfying TµkJk = TJk can be found for all k, but it need not be p-stable. However, the algorithm requires that 
J0 ' Wp, J0 - TJ0. (4.78) 
This may be a restrictive assumption. We have the following proposition. 
Proposition 4.5.9: (Convergence of Optimistic PI) Assume that there exists at least one p-stable policy # ' "p, and that J0 satisfies Eq. (4.78). Then a sequence {Jk} generated by the optimistic PI algorithm (4.77) belongs to Wp and satisfies Jk . Ĵp. 
Proof: Since J0 - Ĵp and Ĵp = T Ĵp [cf. Prop. 4.5.6(a)], all operations on any of the functions Jk with Tµk or T maintain the inequality Jk - Ĵp for all k, so that Jk ' Wp for all k. Also the conditions J0 - TJ0 and TµkJk = TJk imply that 
J0 = J1 - Tm0+1 µ0 J0 = Tµ0J1 - TJ1 = Tµ1J1 - · · · - J2, 
and continuing similarly, 
Jk - TJk - Jk+1, k = 0, 1, . . . . (4.79)
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 307 
Thus Jk . J% for some J%, which must satisfy J% - Ĵp, and hence belong to Wp. By taking limit as k & # in Eq. (4.79) and using an argument similar to the one in the proof of Prop. 4.5.8, it follows that J% = TJ%. By Prop. 4.5.6(a), this implies that J% + Ĵp. Together with the inequality J% - Ĵp shown earlier, this proves that J% = Ĵp. Q.E.D. 
As an example, for the shortest path problem of Example 4.5.3, the reader may verify that in the case where p(x) = 1 for x = 1, the optimistic PI algorithm converges in a single iteration to 
Ĵp(x) = 
, 1 if x = 1, 0 if x = 0, 
provided that J0 ' Wp = & J | J(1) - 1, J(0) = 0 
' . For other starting 
functions J0, the algorithm converges in a single iteration to the function 
J%(1) = min & 1, J0(1) 
' , J%(0) = 0. 
All functions J% of the form above are solutions of Bellman’s equation, but only Ĵp is restricted optimal. 
4.6 INFINITE-SPACES STOCHASTIC SHORTEST PATH PROBLEMS 
In this section we consider a stochastic discrete-time infinite horizon optimal control problem involving the system 
xk+1 = f(xk, uk, wk), k = 0, 1, . . . , (4.80) 
where xk and uk are the state and control at stage k, which belong to setsX and U , wk is a random disturbance that takes values in a countable set W with given probability distribution P (wk | xk, uk), and f : X)U)W %& X is a given function (cf. Example 1.2.1 in Chapter 1). The state and control spacesX and U are arbitrary, but we assume that W is countable to bypass complex measurability issues in the choice of control (see [BeS78]). 
The control u must be chosen from a constraint set U(x) ( U that may depend on x. The expected cost per stage, E 
& g(x, u, w) 
' , is assumed 
nonnegative: 
0 + E & g(x, u, w) 
' < #, * x ' X, u ' U(x), w ' W. 
We assume that X contains a special cost-free and absorbing state t, referred to as the destination: 
f(t, u, w) = t, g(t, u, w) = 0, * u ' U(t), w ' W.
308 Noncontractive Models Chap. 4 
This is a special case of an SSP problem, where the cost per stage is nonnegative, but the state and control spaces are arbitrary. It is also a special case of the nonnegative cost stochastic optimal control problem of Section 4.4.2. We adopt the notation and terminology of that section, but we review it here briefly for convenience. 
Given an initial state x0, a policy # = {µ0, µ1, . . .} when applied to the system (4.80), generates a random sequence of state-control pairs! xk, µk(xk) 
" , k = 0, 1, . . . , with cost 
J"(x0) = E" x0 
4 %. 
k=0 
g ! xk, µk(xk), wk 
" 5 , 
where E" x0{·} denotes expectation with respect to the probability measure 
corresponding to initial state x0 and policy #. For a stationary policy µ, the corresponding cost function is denoted by Jµ. The optimal cost function is 
J*(x) = inf ""! 
J"(x), x ' X, 
and its e#ective domain is denoted X!, i.e., 
X! = & x ' X | J*(x) < # 
' . 
A policy #! is said to be optimal if J""(x) = J*(x) for all x ' X. We denote by E+(X) the set of functions J : X %& [0,#]. In our 
analysis, we will use the set of functions 
J = & J ' E+(X) | J(t) = 0 
' . 
Since t is cost-free and absorbing, this set contains the cost functions J" of all # ' ", as well as J*. 
Here the results of Section 4.3 under Assumption I apply, and the optimal cost function J* is a solution of the Bellman equation 
J(x) = inf u"U(x) 
E -g(x, u, w) + J 
! f(x, u, w) 
"3 , x ' X, 
where the expected value is with respect to the distribution P (w | x, u). Moreover, an optimal stationary policy (if it exists) may be obtained through the minimization in the right side of this equation (with J replaced by J*, cf. Prop. 4.4.4). The VI algorithm starts from some function J0 ' J , and generates a sequence {Jk} ( J according to 
Jk+1(x) = inf u"U(x) 
E -g(x, u, w) + Jk 
! f(x, u, w) 
"3 , x ' X, k = 0, 1, . . . .
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 309 
Proper Policies and the &-Perturbed Problem 
We will now introduce a notion of proper policy with a definition that extends the one used for finite-state SSP in Section 3.5.1. For a given state x ' X , a policy # is said to be proper at x if 
J"(x) < #, %. 
k=0 
rk(#, x) < #, (4.81) 
where rk(#, x) is the probability that xk /= t when using # and starting from x0 = x. We denote by 6"x the set of all policies that are proper at x, and we denote by Ĵ the corresponding restricted optimal cost function, 
Ĵ(x) = inf ""6!x 
J"(x), x ' X, 
(with the convention that the infimum over the empty set is #). Finally we denote by 6X the e#ective domain of Ĵ , i.e., 
6X = & x ' X | Ĵ(x) < # 
' . (4.82) 
Note that 6X is the set of x such that 6"x is nonempty and that t ' 6X. For any & > 0, let us consider the &-perturbed optimal control problem. 
This is the same problem as the original, except that the cost per stage is changed to 
g(x, u, w) + &, * x /= t, 
while g(x, u, w) is left unchanged at 0 when x = t. Thus t is still cost-free as well as absorbing in the &-perturbed problem. The &-perturbed cost function of a policy # starting from x is denoted by J",$(x) and involves an additional expected cost &rk(#, x) for each stage k, so that 
J",$(x) = J"(x) + & %. 
k=0 
rk(#, x). 
Clearly, the sum 1% 
k=0 rk(#, x) is the expected number of steps to reach the destination starting from x and using #, if the sum is finite. We denote by Ĵ$ the optimal cost function of the &-perturbed problem, i.e., Ĵ$(x) = inf""! J",$(x). The following proposition provides some characterizations of proper policies in relation to the &-perturbed problem. 
Proposition 4.6.1: 
(a) A policy # is proper at a state x ' X if and only if J",$(x) < # for all & > 0. 
(b) We have Ĵ$(x) < # for all & > 0 if and only if x ' 6X. 
(c) For every " > 0 and & > 0, a policy #! that is "-optimal for the &-perturbed problem is proper at all x ' 6X , and such a policy exists.
310 Noncontractive Models Chap. 4 
Proof: (a) Follows from Eq. (4.50) and the definition (4.81) of a proper policy. 
(b) If x ' 6X there exists a policy # that is proper at x, and by part (a), Ĵ$(x) + J",$(x) < # for all & > 0. Conversely, if Ĵ$(x) < #, there exists # 
such that J",$(x) < #, implying [by part (a)] that # ' 6"x, so that x ' 6X. 
(c) An "-optimal #! exists by Prop. 4.4.4(e). We have J"!,$(x) + Ĵ$(x) + " 
for all x ' X . Hence J"!,$(x) < # for all x ' 6X, implying by part (a) that 
#! is proper at all x ' 6X. Q.E.D. 
The next proposition shows that the cost function Ĵ$ of the &-perturbed problem can be used to approximate Ĵ . 
Proposition 4.6.2: We have lim$'0 Ĵ$(x) = Ĵ(x) for all x ' X . Moreover, for any " > 0 and & > 0, a policy #! that is "-optimal for the &-perturbed problem is "-optimal within the class of proper policies, i.e., satisfies 
J"!(x) + Ĵ(x) + ", * x ' X. 
Proof: Let us fix & > 0, and for a given " > 0, let #! be a policy that is proper at all x ' 6X and is "-optimal for the &-perturbed problem [cf. Prop. 4.6.1(c)]. By using Eq. (4.50), we have for all " > 0, x ' 6X , and # ' 6"x, 
Ĵ(x) $ " + J"!(x)$ " + J"!,$(x)$ " + Ĵ$(x) + J",$(x) = J"(x) + w",$(x), 
where 
w",$(x) = & %. 
k=0 
rk(#, x) < #, * x ' 6X, # ' 6"x. 
By taking the limit as " . 0, we obtain for all & > 0 and # ' 6"x, 
Ĵ(x) + Ĵ$(x) + J"(x) + w",$(x), * x ' 6X, # ' 6"x. 
We have lim$'0 w",$(x) = 0 for all x ' 6X and # ' 6"x, so by taking the 
limit as & . 0 and then the infimum over all # ' 6"x, 
Ĵ(x) + lim $'0 
Ĵ$(x) + inf ""6!x 
J"(x) = Ĵ(x), * x ' 6X, 
from which Ĵ(x) = lim$'0 Ĵ$(x) for all x ' 6X. Moreover, by Prop. 4.6.1(b), 
Ĵ$(x) = Ĵ(x) = # for all x /' 6X, so that Ĵ(x) = lim$'0 Ĵ$(x) for all x ' X .
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 311 
We also have 
J"!(x) + J"!,$(x) + Ĵ$(x)+" + J"(x)+& %. 
k=0 
r(#, x)+", * x ' 6X, # ' 6"x. 
By taking the limit as & . 0, we obtain 
J"!(x) + J"(x) + ", * x ' 6X, # ' 6"x. 
By taking the infimum over # ' 6"x, it follows that J"!(x) + Ĵ(x) + " for all x ' 6X, which combined with the fact J"!(x) = Ĵ(x) = # for all x /' 6X, yields the result. Q.E.D. 
Main Results 
By Prop. 4.4.4(a), Ĵ$ solves Bellman’s equation for the &-perturbed problem, while by Prop. 4.6.2, lim$'0 Ĵ$(x) = Ĵ(x). This suggests that Ĵ solves the unperturbed Bellman equation, which is the “limit” as & . 0 of the &-perturbed version. Indeed we will show a stronger result, namely that Ĵ is the unique solution of Bellman’s equation within the set of functions 
8W = {J ' S | Ĵ + J}, (4.83) 
where 
S = -J ' J | E" 
x0 
& J(xk) 
' & 0, * (#, x0) with # ' 6"x0 
3 . (4.84) 
Here E" x0 
& J(xk) 
' denotes the expected value of the function J along the 
sequence {xk} generated starting from x0 and using #. Similar to earlier proofs in Sections 4.4 and 4.5, we have that the collection 
C = & (#, x) | # ' 6"x 
' (4.85) 
is S-regular. We first show a preliminary result. Given a policy # = {µ0, µ1, . . .}, 
we denote by #k the policy 
#k = {µk, µk+1, . . .}. (4.86) 
Proposition 4.6.3: 
(a) For all pairs (#, x0) ' C and k = 0, 1, . . ., we have 
0 + E" x0 
& Ĵ(xk) 
' + E" 
x0 
& J"k 
(xk) ' < #, 
where #k is the policy given by Eq. (4.86). 
(b) The set 8W of Eq. (4.83) contains Ĵ , as well as all functions J ' S satisfying Ĵ + J + cĴ for some c - 1.
312 Noncontractive Models Chap. 4 
Proof: (a) For any pair (#, x0) ' C and & > 0, we have 
J",$(x0) = E" x0 
4 J"k,$(xk) + 
k&1. 
m=0 
g ! xm, µm(xm), wm 
" 5 
+ & k&1. 
m=0 
rm(#, x0). 
Since J",$(x0) < # [cf. Prop. 4.6.1(a)], it follows that E" x0 
& J"k,$(xk) 
' < 
#. Hence for all xk that can be reached with positive probability using # and starting from x0, we have J"k,$(xk) < #, implying [by Prop. 4.6.1(a)] 
that (#k, xk) ' C. Hence Ĵ(xk) + J"k (xk) and by applying E" 
x0{·}, the result follows. 
(b) We have for all (#, x0) ' C, 
J"(x0) = E" x0 
-g ! x0, µ0(x0), w0 
"3 + E" 
x0 
& J"1(x1) 
' , (4.87) 
and for m = 1, 2, . . . , 
E" x0 
& J"m(xm) 
' = E" 
x0 
-g ! xm, µm(xm), wm 
"3 + E" 
x0 
& J"m+1(xm+1) 
' , 
(4.88) where {xm} is the sequence generated starting from x0 and using #. By using repeatedly the expression (4.88) for m = 1, . . . , k$ 1, and combining it with Eq. (4.87), we obtain for all k = 1, 2, . . . , 
J"(x0) = E" x0 
& J"k 
(xk) ' + 
k&1. 
m=0 
E" x0 
-g ! xm, µm(xm), wm 
"3 , * (#, x0) ' C. 
The rightmost term above tends to J"(x0) as k & #, so by using the fact J"(x0) < #, we obtain 
E" x0 
& J"k 
(xk) ' & 0, * (#, x0) ' C. 
By part (a), it follows that 
E" x0 
& Ĵ(xk) 
' & 0, * (#, x0) ' C, 
so that Ĵ ' 8W . This also implies that 
E" x0 
& J(xk) 
' & 0, * (#, x0) ' C, 
if Ĵ + J + cĴ for some c - 1. Q.E.D. 
We can now prove our main result.
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 313 
Proposition 4.6.4: Assume that either W is finite or there exists a & > 0 such that 
E -g(x, u, w) + Ĵ$ 
! f(x, u, w) 
"3 < #, * x ' X!, u ' U(x). 
(a) Ĵ is the unique solution of the Bellman Eq. (4.65) within the set 8W of Eq. (4.83). 
(b) (VI Convergence) If {Jk} is the sequence generated by the VI 
algorithm (4.47) starting with some J0 ' 8W , then Jk & Ĵ . 
(c) (Optimality Condition) If µ is a stationary policy that is proper at all x ' 6X and 
µ(x) ' argmin u"U(x) 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 , * x ' X, 
(4.89) then µ is optimal over the set of proper policies, i.e., Jµ = Ĵ . Conversely, if µ is proper at all x ' 6X and Jµ = Ĵ , then µ satisfies the preceding condition (4.89). 
Proof: (a), (b) By Prop. 4.6.3(b), Ĵ ' 8W. We will first show that Ĵ is a solution of Bellman’s equation. Since Ĵ$ solves the Bellman equation for the &-perturbed problem, and Ĵ$ - Ĵ (cf. Prop. 4.6.2), we have for all & > 0 and x /= t, 
Ĵ$(x) = inf u"U(x) 
E -g(x, u, w) + & + Ĵ$ 
! f(x, u, w) 
"3 
- inf u"U(x) 
E -g(x, u, w) + Ĵ$ 
! f(x, u, w) 
"3 
- inf u"U(x) 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 . 
By taking the limit as & . 0 and using Prop. 4.6.2, we obtain 
Ĵ(x) - inf u"U(x) 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 , * x ' X. (4.90) 
For the reverse inequality, let {&m} be a sequence with &m . 0. We have for all m, x /= t, and u ' U(x), 
E -g(x, u, w) + &m + Ĵ$m 
! f(x, u, w) 
"3 - inf 
v"U(x) E -g(x, v, w) + &m 
+ Ĵ$m ! f(x, v, w) 
"3 
= Ĵ$m(x).
314 Noncontractive Models Chap. 4 
We now take limit as m & # in the preceding relation, and we interchange limit and expectation (our assumptions allow the use of the monotone convergence theorem for this purpose; Exercise 4.11 illustrates the need for these assumptions). Using also the fact lim$m'0 Ĵ$m = Ĵ (cf. Prop. 4.6.2), we have 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 - Ĵ(x), * x ' X, u ' U(x), 
so that 
inf u"U(x) 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 - Ĵ(x), * x ' X. (4.91) 
By combining Eqs. (4.90) and (4.91), we see that Ĵ is a solution of Bellman’s equation. 
Part (b) follows by using the S-regularity of the collection (4.85) and 
Prop. 4.4.2(b). Finally, since Ĵ ' 8W and Ĵ is a solution of Bellman’s equation, part (b) implies the uniqueness assertion of part (a). 
(c) If µ is proper at all x ' 6X and Eq. (4.89) holds, then 
Ĵ(x) = E -g ! x, µ(x), w 
" + Ĵ 
! f(x, µ(x), w) 
"3 , x ' X. 
By Prop. 4.4.4(b), this implies that Jµ + Ĵ , so µ is optimal over the set of proper policies. Conversely, assume that µ is proper at all x ' 6X and Jµ = Ĵ . Then by Prop. 4.4.4(b), we have 
Ĵ(x) = E -g ! x, µ(x), w 
" + Ĵ 
! f(x, µ(x), w) 
"3 , x ' X, 
while [by part (a)] Ĵ is a solution of Bellman’s equation, 
Ĵ(x) = inf u"U(x) 
E -g(x, u, w) + Ĵ 
! f(x, u, w) 
"3 , x ' X. 
Combining the last two relations, we obtain Eq. (4.89). Q.E.D. 
We illustrate Prop. 4.6.4 in Fig. 4.6.1. Let us consider now the favorable case where the set of proper policies is su!cient in the sense that it can achieve the same optimal cost as the set of all policies, i.e., Ĵ = J*. This is true for example if all policies are proper at all x such that J*(x) < #. Moreover it is true in some of the finite-state formulations of SSP that we discussed in Chapter 3; see also the subsequent Prop. 4.6.5. When Ĵ = J*, it follows from Prop. 4.6.4 that J* is the unique solution of Bellman’s equation within 8W , and that the VI algorithm converges to J* starting from any J0 ' 8W. Under an additional compactness condition, such as finiteness
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 315 
(0) = 0 J JJ J! ! Ĵ J 
Region of solutions of Bellman’s Eq. Region of solutions of Bellman’s Eq. 
VI converges from !W 
Figure 4.6.1 Illustration of the solutions of Bellman’s equation. All solutions either lie between J" and Ĵ , or they lie outside the set 6W . The VI algorithm converges to Ĵ starting from any J0 $ 6W. 
of U(x) for all x ' X [cf. Prop. 4.4.4(e)], VI converges to J* starting from any J0 in the set S of Eq. (4.84). 
Proposition 4.6.4 does not say anything about the existence of a proper policy that is optimal within the class of proper policies. For a simple example where J* = Ĵ but the only optimal policy is improper, consider a deterministic shortest path problem with a single state 1 plus the destination t. At state 1 we may choose u ' [0, 1] with cost u, and move to t if u /= 0 and stay at 1 if u = 0. Note that here we have J*(1) = Ĵ(1) = 0, and the minimum over u ' [0, 1] is attained in Bellman’s equation, which has the form 
J*(1) = min 
, inf 
u"(0,1] u, J*(1) 
7 . 
However, the only optimal policy (staying at 1) is improper. 
4.6.1 The Multiplicity of Solutions of Bellman’s Equation 
Let us now discuss the issue of multiplicity of solutions of Bellman’s equation within the set of functions 
J = & J ' E+(X) | J(t) = 0 
' . 
We know from Props. 4.4.4(a) and 4.6.4(a) that J* and Ĵ are solutions, 
and that all other solutions J must satisfy either J* + J + Ĵ or J /' 8W . In the special case of a deterministic problem (one where the distur-
bance wk takes a single value), it was shown in Section 4.5 that Ĵ is the largest solution of Bellman’s equation within J , so all solutions J # ' J satisfy J* + J # + Ĵ . It was also shown through examples that there can be any number of solutions that lie between J* and Ĵ : a finite number, an infinite number, or none at all. 
In stochastic problems, however, the situation is strikingly di#erent in the following sense: there can be an infinite number of solutions that do not lie below Ĵ , i.e., solutions J # ' J that do not satisfy J # + Ĵ . Of course, by Prop. 4.6.4(a), these solutions must lie outside 8W . The following example, which involves a finite set W , is an illustration.
316 Noncontractive Models Chap. 4 
Example 4.6.1 
Let X = ', t = 0, and assume that there is only one control at each state, and hence a single policy ". The disturbance wk takes two values: 1 and 0 with probabilities ! $ (0, 1) and 1! !, respectively. The system equation is 
xk+1 = wkxk 
! , 
and there is no cost at each state and stage: 
g(x, u,w) * 0. 
Thus from state xk we move to state xk/! with probability ! and to the termination state t = 0 with probability 1! !. 
Here, the unique policy is stationary and proper at all x $ X, and we have 
J"(x) = Ĵ(x) = 0, % x $ X. 
Bellman’s equation has the form 
J(x) = (1! !)J(0) + !J * x a 
+ , 
which within J reduces to 
J(x) = !J * x ! 
+ , % J $ J , x $ X. (4.92) 
It can be seen that Bellman’s equation has an infinite number of solutions within J in addition to J" and Ĵ : any positively homogeneous function, such as, for example, 
J(x) = &|x|, & > 0, 
is a solution. Consistently with Prop. 4.6.4(a), none of these solutions belongs 
to 6W, since xk is either equal to x0/! k (with probability !k) or equal to 0 
(with probability 1! !k). For example, in the case of J(x) = &|x|, we have 
E" x0 
& J(xk) 
' = !k& 
222 x0 
!k 
222 = &|x0|, % k & 0, 
so J(xk) does not converge to 0, unless x0 = 0. Moreover, none of these additional solutions seems to be significant in some discernible way. 
The preceding example illustrates an important structural di#erence between deterministic and stochastic shortest path problems with infinite state space. For a terminating policy µ in the context of the deterministic problem of Section 4.5, the corresponding Bellman equation J = TµJ has a unique solution within J [to see this, consider the restricted problem for which µ is the only policy, and apply Prop. 4.5.6(a)]. By contrast, for a proper policy in the stochastic context of the present section, the corresponding Bellman equation may have an infinite number of solutions within J , as Example 4.6.1 shows. This discrepancy does not occur when the state space is finite, as we have seen in Section 3.5.1. We will next elaborate on the preceding observations and refine our analysis regarding multiplicity of solutions of Bellman’s equation for problems where the cost per stage is bounded.
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 317 
4.6.2 The Case of Bounded Cost per Stage 
Let us consider the special case where the cost per stage g is bounded over X ) U )W , i.e., 
sup (x,u,w)"X(U(W 
g(x, u, w) < #. (4.93) 
We will show that Ĵ is the largest solution of Bellman’s equation within the class of functions that are bounded over the e#ective domain 6X of Ĵ [cf. Eq. (4.82)]. 
We say that a policy # is uniformly proper if there is a uniform bound on the expected number of steps to reach the destination from states x ' 6X using #: 
sup x"6X 
%. 
k=0 
rk(#, x) < #. 
Since we have 
J"(x0) + 
/ sup 
(x,u,w)"X(U(W 
g(x, u, w) 
0 · 
%. 
k=0 
rk(#, x0) < #, * # ' 6"x0 , 
it follows that the cost function J" of a uniformly proper # belongs to the set B, defined by 
B = 
4 J ' J 
222 sup x"6X 
J(x) < # 
5 . (4.94) 
When 6X = X , the notion of a uniformly proper policy coincides with the notion of a transient policy used in [Pli78] and [JaC06], which itself descends from earlier works. However, our definition is somewhat more general, since it also applies to the case where 6X is a strict subset of X . 
Let us denote by 8Wb the set of functions 
8Wb = {J ' B | Ĵ + J}. 
The following proposition, illustrated in Fig. 4.6.2, provides conditions for Ĵ to be the largest fixed point of T within B. Its assumptions include the existence of a uniformly proper policy, which implies that Ĵ belongs to B. The proposition also uses the earlier Prop. 4.4.6 in order to provide conditions for J* = Ĵ , in which case J* is the unique fixed point of T within B.
318 Noncontractive Models Chap. 4 
Paths of VI Unique solution of Bellman’s equation 
Fixed Points of T 
2 Ĵ J 
b > 0 
T J* 
Set of Bounded Functions B 
! 
!Wb 
Figure 4.6.2. Schematic illustration of Prop. 4.6.5 for a nonnegative cost SSP problem. The functions J" and Ĵ are the smallest and largest solutions, respectively, of Bellman’s equation within the set B. Moreover, the VI algorithm converges to Ĵ starting from J0 $ 6Wb = {J $ B | Ĵ ! J}. 
Proposition 4.6.5: Let the assumptions of Prop. 4.6.4 hold, and assume further that the cost per stage g is bounded over X ) U )W [cf. Eq. (4.93)], and that there exists a uniformly proper policy. Then: 
(a) Ĵ is the largest solution of the Bellman Eq. (4.65) within the set B of Eq. (4.94), i.e., Ĵ is a solution that belongs to B and if J # ' B is another solution, then J # + Ĵ . Moreover, if Ĵ = J*, then J* is the unique solution of Bellman’s equation within B. 
(b) If {Jk} is the sequence generated by the VI algorithm (4.47) starting with some J0 ' B with J0 - Ĵ , then Jk & Ĵ . 
(c) Assume in addition that X is finite, that J*(x) > 0 for all x /= t, and that X! = 6X. Then Ĵ = J*. 
Proof: (a) Since the cost function of a uniformly proper policy belongs to B, we have Ĵ ' B. On the other hand, for all J ' B, we have 
E" x0 
& J(xk) 
' + 
/ sup x"6X 
J(x) 
0 · rk(#, x0) & 0, * # ' 6"x0 . 
It follows that the set 8Wb is contained in 8W , while the function Ĵ belongs to 8Wb. Since 8Wb is unbounded above within the set B, for every solution J # ' B of Bellman’s equation we have J # + J for some J ' 8Wb, and hence also J # + J̃ for some J̃ in the set S of Eq. (4.84). It follows from Prop. 4.4.2(a) and the S-regularity of the collection (4.85) that J # + Ĵ .
Sec. 4.6 Infinite-Spaces Stochastic Shortest Path Problems 319 
If in addition Ĵ = J*, from Prop. 4.4.4(a), Ĵ is also the smallest solution of Bellman’s equation within J . Hence J* is the unique solution of Bellman’s equation within B. 
(b) Follows from Prop. 4.6.4(b), since 8Wb ( 8W , as shown in the proof of part (a). 
(c) We have by assumption 
0 < J*(x) + Ĵ(x), * x /= t, 
while Ĵ(x) < # for all x ' X! since X! = 6X . In view of the finiteness of X , we can find a su!ciently large c such that Ĵ + cJ*, so by Prop. 4.4.6, it follows that Ĵ = J*. Q.E.D. 
The uniqueness of solution of Bellman’s equation within B when Ĵ = J* [cf. part (a) of the preceding proposition] is consistent with Example 4.6.1. In that example, J* and Ĵ are equal and bounded, and all the additional solutions of Bellman’s equation are unbounded, as can be verified by using Eq. (4.92). 
Note that without the assumption of existence of a uniformly proper #, Ĵ and J* need not belong to B. As an example, let X be the set of nonnegative integers, let t = 0, and let there be a single policy that moves the system deterministically from a state x - 1 to the state x $ 1 at cost g(x, x$ 1) = 1. Then 
Ĵ(x) = J*(x) = x, * x ' X, 
so Ĵ and J* do not belong to B, even though g is bounded. Here the unique policy is proper at all x, but is not uniformly proper. 
In a given practical application, we may be interested in computing either J* or Ĵ . If the cost per stage is bounded, we may compute Ĵ with the VI algorithm, assuming that an initial function in the set 8Wb can be found. The computation of J* is also possible by using the VI algorithm and starting from the zero initial condition, assuming that the conditions of Prop. 4.4.4(d) are satisfied. 
An alternative possibility for the case of a finite spaces SSP is to approximate the problem with a sequence of $k-discounted problems where the discount factors $k tend to 1. This approach, developed in some detail in Exercise 5.28 of the book [Ber17a], has the advantage that the discounted problems can be solved more reliably and with a broader variety of methods than the original undiscounted SSP. 
Another technique, developed in the paper [BeY16], is to transform a finite-state SSP problem such that J*(x) = 0 for some x /= t into an equivalent SSP problem that satisfies the conditions of Prop. 4.6.5(c), and thus allow the computation of J* by a VI or PI algorithm. The idea is to lump t together with the states x for which J*(x) = 0 into a single
320 Noncontractive Models Chap. 4 
state, which is the termination state for the equivalent SSP problem. This technique is strictly limited to finite-state problems, since in general the conditions J*(x) > 0 for all x /= t and X! = 6X do not imply that Ĵ = J*, even under the bounded cost and uniform properness assumptions of this section (see the deterministic stopping Example 4.5.2). 
4.7 NOTES, SOURCES, AND EXERCISES 
Sections 4.1: The use of monotonicity as the foundational property of abstract DP models was initiated in the author’s papers [Ber75], [Ber77]. 
Section 4.2: The finite horizon analysis of Section 4.2 was given in Chap-ter 3 of the monograph by Bertsekas and Shreve [BeS78]. 
Section 4.3: The monotone increasing and decreasing abstract DP models of Section 4.3 were introduced in the author’s papers [Ber75], [Ber77]. Their analysis was also given in Chapter 5 of the monograph [BeS78]. 
Important examples of noncontractive infinite horizon models are the classical negative cost DP problems, analyzed by Blackwell [Bla65], and by Dubins and Savage [DuS65], and the positive cost DP problems analyzed in Strauch [Str66] (and also in Strauch’s Ph.D. thesis, written under the supervision of Blackwell). The monograph by Bertsekas and Shreve [BeS78] provides a detailed treatment of these two models, which also resolves the associated measurability questions using the notion of universally measurable policies. The paper by Yu and Bertsekas [YuB15] provides a more recent analysis that addresses some issues regarding the convergence of the VI and PI algorithms that were left unresolved in the monograph [BeS78]. A simpler textbook treatment, which bypasses the measurability questions, is given in the author’s [Ber12a], Chapter 4. 
The compactness condition that guarantees convergence of VI to J* 
starting with the initial condition J0 = J̄ under Assumption I (cf. Prop. 4.3.14) was obtained by the author in [Ber72] for reachability problems (see Exercise 4.5), and in [Ber75], [Ber77] for positive cost DP models; see also Schal [Sch75] and Whittle [Whi80]. A more refined analysis of the question of convergence of VI to J* is possible. This analysis provides a necessary and su!cient condition for convergence, and improves over the compactness condition of Prop. 4.3.14. In particular, the following characterization is shown in [Ber77], Prop. 11 (see also [BeS78], Prop. 5.9): 
For a set C ( X)U)!, let "(C) be the projection of C onto X)!: 
"(C) = & (x,!) | (x, u,!) ' C for some u ' U(x) 
' , 
and denote also 
"(C) = & (x,!) | !m & ! for some sequence {!m} with 
& (x,!m)} ( C 
' .
Sec. 4.7 Notes, Sources, and Exercises 321 
Consider the sets Ck ( X ) U )! given by 
Ck = & (x, u,!) | H(x, u, T kJ̄) + !, x ' X, u ' U(x) 
' , k = 0, 1, . . . . 
Then under Assumption I we have T kJ̄ & J* if and only if 
" ! 1% k=0 Ck 
" = 1% 
k=0"(Ck). 
Moreover we have T kJ̄ & J* and in addition there exists an optimal stationary policy if and only if 
" ! 1% k=0 Ck 
" = 1% 
k=0"(Ck). (4.95) 
For a connection with Prop. 4.3.14, it can be shown that compactness of 
Uk(x,!) = & u ' U(x) 
22 H(x, u, T kJ̄) + ! ' 
implies Eq. (4.95) (see [Ber77], Prop. 12, or [BeS78], Prop. 5.10). The analysis of convergence of VI to J* under Assumption I and 
starting with an initial condition J0 - J* is far more complicated than for the initial condition J0 = J̄ . A principal reason for this is the multiplicity of solutions of Bellman’s equation within the set 
& J ' E+(X) | J - J̄ 
' . 
We know that J* is the smallest solution (cf. Prop. 4.4.9), and an interesting issue is the characterization of the largest solution and other solutions within some restricted class of functions of interest. We substantially resolved this question in Sections 4.5 and 4.6 for infinite-spaces deterministic and stochastic shortest path problems, respectively (as well in Sections 3.5.1 and 3.52 for finite-state stochastic shortest path and a!ne monotonic problems). Generally, optimal control problems with nonnegative cost per stage can typically be reduced to problems with a cost-free and absorbing termination state (see [BeY16] for an analysis of the finite-state case). However, the fuller characterization of the set of solutions of Bellman’s equation for general abstract DP models under Assumption I requires further investigation. 
Optimistic PI and !-PI under Assumption D have not been considered prior to the 2013 edition of this book, and the corresponding analysis of Section 4.3.3 is new. See [BeI96], [ThS10a], [ThS10b], [Ber11b], [Sch11], [Ber16b] for analyses of !-PI for discounted and SSP problems. 
Section 4.4: The definition and analysis of regularity for nonstationary policies was introduced in the author’s paper [Ber15]. We have primarily used regularity in this book to analyze the structure of the solution set of Bellman’s equation, and to identify the region of attraction of value and policy iteration algorithms. This analysis is multifaceted, so it is worth summarizing here: 
(a) We have characterized the fixed point properties of the optimal cost function J* and the restricted optimal cost function J* 
C over S-regular
322 Noncontractive Models Chap. 4 
collections C, for various sets S. While J* and J* C need not be fixed 
points of T , they are fixed points in a large variety of interesting contexts (Sections 3.3-3.5 and 4.4-4.6). 
(b) We have shown that when J* = J* C , then J* is the unique solution of 
Bellman’s equation in several interesting noncontractive contexts. In particular, Section 3.3 deals with an important case that covers among others, the most common type of stochastic shortest path problems. However, even when J* /= J* 
C , the functions J* and J* C often bound 
the set of solutions from below and/or from above (see Sections 3.5.1, 3.5.2, 4.5, 4.6). 
(c) Simultaneously with the analysis of the fixed point properties of J* 
and J* C , we have used regularity to identify the region of convergence 
of value iteration. Often convergence to J* C can be shown from start-
ing functions J - J* C , assuming that J* 
C is a fixed point of T . In the favorable case where J* = J* 
C , convergence to J* can often be shown from every starting function of interest. In addition regularity has been used to guarantee the validity of policy iteration algorithms that generate exclusively regular policies, and are guaranteed to converge to J* or J* 
C . 
(d) We have been able to characterize some of the solutions of Bellman’s equation, but not the entire set. Generally, there may exist an infinite number of solutions, and some of them may not be associated with an S-regular collection for any set S, unless we change the starting function J̄ that is part of the definition of the cost function J" of the policies. There is a fundamental di!culty here: the solutions of the Bellman equation J = TJ do not depend on J̄ , but S-regularity of a collection of policy-state pairs depends strongly on J̄ . A sharper characterization of the solution set of Bellman’s equation remains an open interesting question, in both specific problem contexts as well as in generality. 
The use of regularity in the analysis of undiscounted and discounted stochastic optimal control in Sections 4.4.2 and 4.4.3 is new, and was presented in the author’s paper [Ber15]. The analysis of convergent models in Section 4.4.4, under the condition 
J*(x) - J̄(x) > $#, * x ' X, 
is also new. A survey of stochastic optimal control problems under convergence conditions that are more general than the ones considered here is given by Feinberg [Fei02]. An analysis of convergent models for stochastic optimal control, which illustrates the broad range of pathological behaviors that can occur without the condition J* - J̄ , is given in the paper by Yu [Yu15].
Sec. 4.7 Notes, Sources, and Exercises 323 
Section 4.5: This section follows the author’s paper [Ber17a]. The issue of the connection of optimality with stability (and also with controllability and observability) was raised in the classic paper by Kalman [Kal60] in the context of linear-quadratic problems. 
The set of solutions of the Riccati equation has been extensively investigated starting with the papers by Willems [Wil71] and Kucera [Kuc72], [Kuc73], which were followed up by several other works; see the book by Lancaster and Rodman [LaR95] for a comprehensive treatment. In these works, the “largest” solution of the Riccati equation is referred to as the “stabilizing” solution, and the stability of the corresponding policy is shown, although the author could not find an explicit statement in the literature regarding the optimality of this policy within the class of all linear stable policies. Also the lines of analysis of these works are tied to the structure of the linear-quadratic problem and are unrelated to our analysis of Section 4.5, which is based on semicontractive ideas. 
Section 4.6: Proper policies for infinite-state SSP problems have been considered earlier in the works of Pliska [Pli78], and James and Collins [JaC06], where they are called “transient.” There are a few di#erences between the frameworks of [Pli78], [JaC06] and Section 4.6, which impact on the results obtained. In particular, the papers [Pli78] and [JaC06] use a related (but not identical) definition of properness to the one of Section 4.6, while the notion of a transient policy used in [JaC06] coincides with the notion of a uniformly proper policy of Section 4.6.2 when 6X = X . Furthermore, [Pli78] and [JaC06] do not consider the notion of policy that is “proper at a state.” The paper [Pli78] assumes that all policies are transient, that g is bounded, and that J* is real-valued. The paper [JaC06] allows for notransient policies that have infinite cost from some initial states, and extends the analysis of Bertsekas and Tsitsiklis [BeT91] from finite state space to infinite state space (addressing also measurability issues). Also, [JaC06] allows the cost per stage g to take both positive and negative values, and uses assumptions that guarantee that J* = Ĵ , that J* is real-valued, and that improper policies cannot be optimal. Instead, in Section 4.6 we allow that J* /= Ĵ and that J* can take the value #, while requiring that g is nonnegative and that the disturbance space W is countable. 
The analysis of Section 4.6 comes from the author’s paper [Ber17b], and is most closely related to the SSP analysis under the weak conditions of Section 3.5.1, where we assumed that the state space is finite, but allowed g to take both positive and negative values. The extension of some of our results of Section 4.6 to SSP problems where g takes both positive and negative values may be possible; Exercises 4.8 and 4.9 suggest some research directions. However, our analysis of infinite-spaces SSP problems in this chapter relies strongly on the nonnegativity of g and cannot be extended without major modifications. In this connection, it is worth mentioning the example of Section 3.1.2, which shows that J* may not be a solution
324 Noncontractive Models Chap. 4 
of Bellman’s equation when g can take negative values. 
E X E R C I S E S 
4.1 (Example of Nonexistence of an Optimal Policy Under D) 
This is an example of a deterministic stopping problem where Assumption D holds, and an optimal policy does not exist, even though only two controls are available at each state (stop and continue). The state space is X = {1, 2, . . .}. Continuation from state x leads to state x+ 1 with certainty and no cost, while the stopping cost is !1 + (1/x), so that there is an incentive to delay stopping at every state. Here for all x, J̄(x) = 0, and 
H(x, u, J) = 
, J(x+ 1) if u = continue, 
!1 + (1/x) if u = stop. 
Show that J"(x) = !1 for all x, but there is no policy (stationary or not) that attains the optimal cost starting from x. 
Solution: Since a cost is incurred only upon stopping, and the stopping cost is greater than -1, we have Jµ(x) > !1 for all x and µ. On the other hand, starting from any state x and stopping at x + n yields a cost !1 + 1 
x+n , so by taking n 
su"ciently large, we can attain a cost arbitrarily close to -1. Thus J"(x) = !1 for all x, but no policy can attain this optimal cost. 
4.2 (Counterexample for Optimality Condition Under D) 
For the problem of Exercise 4.1, show that the policy µ that never stops is not optimal but satisfies TµJ" = TJ". 
Solution: We have J"(x) = !1 and Jµ(x) = 0 for all x $ X. Thus µ is nonoptimal, yet attains the minimum in Bellman’s equation 
J"(x) = min -J"(x+ 1), !1 + 
1 x 
3 
for all x. 
4.3 (Counterexample for Optimality Condition Under I) 
Let X = ', U(x) * (0, 1], J̄(x) * 0, 
H(x, u, J) = |x|+ J(ux), % x $ X, u $ U(x).
Sec. 4.7 Notes, Sources, and Exercises 325 
Let µ(x) = 1 for all x $ X. Then Jµ(x) = # if x )= 0 and Jµ(0) = 0. Verify that TµJµ = TJµ. Verify also that J"(x) = |x|, and hence µ is not optimal. 
Solution: The verification of TµJµ = TJµ is straightforward. To show that J"(x) = |x|, we first note that |x| is a fixed point of T , so by Prop. 4.3.2, J"(x) " |x|. Also (T J̄)(x) = |x| for all x, while under Assumption I, we have J" & T J̄ , so J"(x) & |x|. Hence J"(x) = |x|. 
4.4 (Solution by Mathematical Programming) 
This exercise shows that under Assumptions I and D, it is possible to use a computational method based on mathematical programming when X = {1, . . . , n}. 
(a) Under Assumption I, show that J" is the unique solution of the following optimization problem in z = (z1, . . . , zn): 
minimize 
n. 
i=1 
zi 
subject to zi & J̄(i), zi & inf u#U(i) 
H(i, u, z), i = 1, . . . , n. 
(b) Under Assumption D, show that J" is the unique solution of the following optimization problem in z = (z1, . . . , zn): 
maximize 
n. 
i=1 
zi 
subject to zi " J̄(i), zi " H(i, u, z), i = 1, . . . , n, u $ U(i). 
Note: Generally, these programs may not be linear or even convex. 
Solution: (a) Any feasible solution z of the given optimization problem satisfies z & J̄ as well as zi & infu#U(i) H(i, u, z) for all i = 1, . . . , n, so that z & Tz. It follows from Prop. 4.4.9 that z & J", which implies that J" is an optimal solution of the given optimization problem. Also J" is the unique optimal solution since if z is feasible and z )= J", the inequality z & J" implies that 
1 i zi > 
1 i J"(i), 
so z cannot be optimal. 
(b) Any feasible solution z of the given optimization problem satisfies z " J̄ as well as zi " H(i, u, z) for all i = 1, . . . , n and u $ U(i), so that z " Tz. It follows from Prop. 4.3.6 that z " J", which implies that J" is an optimal solution of the given optimization problem. Similar to part (a), J" is the unique optimal solution. 
4.5 (Infinite Time Reachability [Ber71], [Ber72]) 
This exercise provides an instance of an interesting problem where the mapping H is naturally extended real-valued. Consider a dynamic system 
xk+1 = f(xk, uk, wk),
326 Noncontractive Models Chap. 4 
where wk is viewed as an uncertain disturbance that may be any point in a set W (xk, uk) (this is known in the literature as an “unknown but bounded” disturbance, and is the basis for a worst case/minimax treatment of uncertainty in the control of uncertain dynamic systems). We introduce an abstract DPmodel where the objective is to find a policy that keeps the state xk of the system within a given set X at all times, for all possible values of the sequence {wk}. This is a common objective, which arises in a variety of control theory contexts, including model predictive control (see [Ber17a], Section 6.4.3). 
Let 
J̄(x) = -0 if x $ X, # otherwise, 
and 
H(x, u, J) = -0 if J(x) = 0, u $ U(x), and J 
! f(x, u,w) 
" = 0, % w $ W (x,u), 
# otherwise. 
(a) Show that Assumption I holds, and that the optimal cost function has the form 
J"(x) = -0 if x $ X", # otherwise, 
where X" is some subset of X. 
(b) Consider the sequence of sets {Xk}, where 
Xk = & x $ X | (T kJ̄)(x) = 0 
' . 
Show that Xk+1 . Xk for all k, and that X" . /% k=0Xk. Show also that 
convergence of VI (i.e., T kJ̄ , J") is equivalent to X" = /% k=0Xk. 
(c) Show that X" = /% k=0Xk and there exists an optimal stationary policy if 
the sets 
Ûk(x) = & u $ U(x) | f(x, u, w) $ Xk, % w $ W (x, u) 
' 
are compact for all k greater than some index k̄. Hint : Use Prop. 4.3.14. 
Solution: Let Ê(X) be the subset of E(X) that consists of functions that take only the two values 0 and #, and for all J $ Ê(X) denote 
D(J) = & x $ X | J(x) = 0 
' . 
Note that for all J $ Ê(X) we have TµJ $ Ê(X), TJ $ Ê(X), and that 
D(TµJ) = & x $ X | x $ D(J), f 
! x,µ(x), w 
" $ D(J), % w $ W (x,µ(x)) 
' , 
D(TJ) = 0µ#MD(TµJ). 
(a) For all J $ Ê(X), we have D(TµJ) . D(J) and TµJ & J , so condition (1) of Assumption I holds, and it is easily verified that the remaining two conditions of
Sec. 4.7 Notes, Sources, and Exercises 327 
Assumption I also hold. We have J̄ $ Ê(X), so for any policy " = {µ0, µ1, . . .}, we have Tµ0 · · ·Tµk 
J̄ $ Ê(X). It follows that J" , given by 
J" = lim k$% 
Tµ0 · · · Tµk J̄ , 
also belongs to Ê(X), and the same is true for J" = inf"#! J". Thus J " has the 
given form with D(J") = X". 
(b) Since {T kJ̄} is monotonically nondecreasing we have D(T k+1J̄) . D(T kJ̄), or equivalently Xk+1 . Xk for all k. Generally for a sequence {Jk} . Ê(X), if Jk 1 J , we have J $ Ê(X) and D(J) = /% 
k=0D(Jk). Thus convergence of VI (i.e., T kJ̄ 1 J") is equivalent to D(J") = /% 
k=0D(Jk) or X" = /% k=0Xk. 
(c) The compactness condition of Prop. 4.3.14 guarantees that T kJ̄ 1 J", or equivalently by part (b), X" = /% 
k=0Xk. This condition requires that the sets 
Uk(x,$) = & u $ U(x) 
22 H(x, u, T kJ̄) " $ ' 
are compact for every x $ X, $ $ ', and for all k greater than some integer k. It can be seen that Uk(x,$) is equal to the set 
Ûk(x) = & u $ U(x) 
22 f(x, u,w) $ Xk, % w $ W (x,u) ' 
given in the statement of the exercise. 
4.6 (Exceptional Linear-Quadratic Problems) 
Consider the deterministic linear-quadratic problem of Section 3.5.4 and Example 4.5.1. Assume that there is a single control variable uk, and two state variables, x1 k and x2 
k, which evolve according to 
x1 k+1 = &x1 
k + buk, x2 k+1 = x1 
k + x2 k + uk, 
where & > 1. The cost of stage k is quadratic of the form 
q ! (x1 
k) 2 + (x2 
k) 2 " + (uk) 
2. 
Consider the four cases of pairs of values (b, q) where b $ {0, 1} and q $ {0, 1}. For each case, use the theory of Section 4.5 to find the optimal cost function J" and the optimal cost function over stable policies Ĵ+, and to describe the convergence behavior of VI. 
Solution: When b = 1 and q = 1, the classical controllability and observability conditions are satisfied, and we have J" = Ĵ+, while there exists an optimal policy that is linear and stable (so J" and Ĵ+ are real-valued and positive definite quadratic). Moreover, the VI algorithm converges to J" starting from any J0 & 0 (even extended real-valued J0) with J0(0) = 0. 
When b = 0 and q = 0, we clearly have J"(x) * 0. Also Ĵ+(x1, x2) = # for x1 )= 0, while Ĵ+(0, x2) is finite for all x2, but positive for x2 )= 0 (since for
328 Noncontractive Models Chap. 4 
x1 = 0, the problem becomes essentially one-dimensional, and similar to the one of Section 3.5.4). The VI algorithm converges to Ĵ+ starting from any positive semidefinite quadratic initial condition J0 with J0(0, x 
2) = 0 and J0 )= J". When b = 0 and q = 1, we have J" = Ĵ+, but J" and Ĵ+ are not real-
valued. In particular, since x1 k stays constant under all policies when b = 0, we 
have J"(x1, x2) = Ĵ+(x1, x2) = # for x1 )= 0. Moreover, for an initial state with x1 
0 = 0, the problem becomes essentially a one-dimensional problem that satisfies the classical controllability and observability conditions, and we have J"(0, x2) = Ĵ+(0, x2) for all x2. The VI algorithm takes the form 
Jk+1(0, x 2) = min 
u 
& (x2)2 + (u)2 + Jk(0, x 
2 + u) ' , 
Jk+1(x 1, x2) = min 
u 
& (x1)2 + (x2)2 + (u)2 + Jk(&x 
1, x1 + x2 + u) ' , if x1 )= 0. 
It can be seen that the VI iterates Jk(0, x 2) evolve as in the case of a single state 
variable problem, where x1 is fixed at 0. For x1 )= 0, the VI iterates Jk(x 1, x2) 
diverge to #. When b = 1 and q = 0, we have J"(x) * 0, while 0 < Ĵ+(x) < # for 
all x )= 0. Similar to Example 4.5.1, the VI algorithm converges to Ĵ+ starting from any initial condition J0 & Ĵ+. The functions J" and Ĵ+ are real-valued and satisfy Bellman’s equation, which has the form 
J(x1, x2) = min u 
& (u)2 + J(&x1 + u, x1 + x2 + u) 
' . 
However, Bellman’s equation has additional solutions, other than J" and Ĵ+. One of these is 
Ĵ(x1, x2) = P (x1)2, 
where P = &2 ! 1 (cf. the example of Section 3.5.4). 
4.7 (Discontinuities in Infinite-State Shortest Path Problems) 
The purpose of this exercise is to show that di#erent types of perturbations in infinite-state shortest path problems, may yield di#erent solutions of Bellman’s equation. Consider the optimal stopping problem of Example 4.5.2, and introduce a perturbed version by modifying the e#ect of the action that moves the state from x )= 0 to &x. Instead, this action stops the system with probability % > 0 at cost ' & 0, and moves the state from x to &x with probability 1! % at cost -x-. Note that with this modification, all policies become uniformly proper. Show that: 
(a) The optimal cost function of the (%,')-perturbed version of the problem, denoted Ĵ$,& , is the unique solution of the corresponding Bellman equation within the class of bounded functions B of Eq. (4.94). 
(b) For ' = 0, we have lim$'0 Ĵ$,0 = J", where J" is the optimal cost function of the deterministic problem of Example 4.5.2. 
(c) For ' = c, we have Ĵ$,c = Ĵ+ for all % > 0, where Ĵ+ is the largest solution of Bellman’s equation in the deterministic problem of Example
Sec. 4.7 Notes, Sources, and Exercises 329 
4.5.2 [Ĵ+(x) = c for all x )= 0, which corresponds to the policy that stops at all states]. 
Solution: (a) It can be seen that the Bellman equation for the (%,')-perturbed version of the problem is 
J(x) = 
, min 
& c, %' + (1! %) 
! -x-+ J(&x) 
"' if x )= 0, 
0 if x = 0, 
and has exactly the same solutions as the equation 
J(x) = -min 
& c, %' + (1! %) 
! min 
& c/(1! %), -x-
' + J(&x) 
"' if x )= 0, 
0 if x = 0. 
The latter equation involves a bounded cost per stage, and hence according to the theory of Section 4.6, has a unique solution within B, when all policies are proper. 
(b) Evident since the e#ect of % on the cost of the optimal policy of the problem of Example 4.5.2 diminishes as % , 0. 
(c) Since termination at cost c is inevitable (with probability 1) under every policy, the optimal policy for the (%,')-perturbed version of the problem is to stop as soon as possible. 
4.8 (A Perturbation Approach for Semicontractive Models) 
The purpose of this exercise is to adapt the perturbation approach of Section 3.4 so that it can be used in conjunction with the regularity notion for nonstationary policies of Definition 4.4.1. Given a set of functions S . E(X) and a collection C of policy-state pairs (", x) that is S-regular, let J" 
C be the restricted optimal cost function defined by 
J" C (x) = inf 
(",x)#C J"(x), x $ X. 
Consider also a nonnegative forcing function p : X 2, [0,#), and for each % > 0 and stationary policy µ, the mappings Tµ,$ and T$ given by 
(Tµ,$J)(x) = H ! x, µ(x), J 
" + %p(x), (T$J)(x) = inf 
µ#M (Tµ,$J)(x), x $ X. 
We refer to the problem associated with the mappings Tµ,$ as the %-perturbed problem. The cost function of a policy " = {µ0, µ1, . . .} $ ! for this problem is 
J",$ = lim sup k$% 
Tµ0,$ · · ·Tµk,$J̄ , 
and the optimal cost function is Ĵ$ = inf"#! J",$. Assume that for every % > 0: 
(1) Ĵ$ satisfies the Bellman equation of the %-perturbed problem, Ĵ$ = T$Ĵ$.
330 Noncontractive Models Chap. 4 
(2) For every x $ X, we have inf(",x)#C J",$(x) = Ĵ$(x). 
(3) For all x $ X and (", x) $ C, we have 
J",$(x) " J"(x) + w",$(x), 
where w",$ is a function such that lim$'0 w",$ = 0. 
(4) For every sequence {Jm} . S with Jm ( J , we have 
lim m$% 
H(x, u, Jm) = H(x, u, J), % x $ X, u $ U(x). 
Then J" C is a fixed point of T and the conclusions of Prop. 4.4.2 hold. Moreover, 
we have J" C = lim 
$'0 Ĵ$. 
Solution: The proof is very similar to the one of Prop. 3.4.1. Condition (2) implies that for every x $ X and # > 0, there exists a policy "x,! such that ("x,!, x) $ C and J"x,!,$(x) " Ĵ$(x) + #. Thus, using conditions (2) and (3), we have for all x $ X, % > 0, # > 0, and " with (", x) $ C, 
J" C (x)! # " J"x,!(x)! # " J"x,!,$(x)! # " Ĵ$(x) " J",$(x) " J"(x) + w",$(x). 
By taking the limit as # ( 0, we obtain for all x $ X, % > 0, and " with (", x) $ C, 
J" C (x) " Ĵ$(x) " J",$(x) " J"(x) + w",$(x). 
By taking the limit as % ( 0 and then the infimum over all " with (", x) $ C, it follows [using also condition (3)] that for all x $ X, 
J" C (x) " lim 
$'0 Ĵ$(x) " inf 
{"|(",x)#C} lim $'0 
J",$(x) " inf {"|(",x)#C} 
J"(x) = J" C (x), 
so that J" C = lim$'0 Ĵ$. 
To prove that J" C is a fixed point of T , we prove that both J" 
C & TJ" C and 
J" C " TJ" 
C hold. Indeed, from condition (1) and the fact Ĵ$ & J" C shown earlier, 
we have for all % > 0, Ĵ$ = T$Ĵ$ & T Ĵ$ & TJ" 
C , 
and by taking the limit as % ( 0 and using the fact J" C = lim$'0 Ĵ$ shown earlier, 
we obtain J" C & TJ" 
C . For the reverse inequality, let {%m} be a sequence with %m ( 0. Using condition (1) we have for all m, 
H(x, u, Ĵ$m) + %mp(x) & (T$m Ĵ$m)(x) = Ĵ$m(x), % x $ X, u $ U(x). 
Taking the limit as m , #, and using condition (4) and the fact Ĵ$m ( J" C shown 
earlier, we have 
H(x, u, J" C ) & J" 
C (x), % x $ X, u $ U(x), 
so that by minimizing over u $ U(x), we obtain TJ" C & J" 
C .
Sec. 4.7 Notes, Sources, and Exercises 331 
4.9 (Deterministic Optimal Control with Positive and Negative Costs per Stage) 
In this exercise, we consider the infinite-spaces optimal control problem of Section 4.5 and its notation, but without the assumption g → 0 [cf. Eq. (4.46)]. Instead, we assume that 
↑↓ < g(x, u) ≤ ↓, ∀ x ∈ X, u ∈ U(x), k = 0, 1, . . . , 
and that J→(x) > ↑↓ for all x ∈ X. The latter assumption was also made in Section 3.5.5, but in the present exercise, we will not assume the additional nearoptimal termination Assumption 3.5.9 of that section, and we will use instead the perturbation framework of Exercise 4.8. Note that J→ is a fixed point of T because the problem is deterministic (cf. Exercise 3.1). 
We say that a policy π is terminating from state x0 ∈ X if the sequence {xk} generated by π starting from x0 terminates finitely (i.e., satisfies xk̄ = t for some index k̄). We denote by Πx the set of all policies that are terminating from x, and we consider the collection 
C = { (π, x) | π ∈ Πx 
} . 
Let J→ C be the corresponding restricted optimal cost function, 
J→ C (x) = inf 
(π,x)∈C Jπ(x) = inf 
π∈Πx Jπ(x), x ∈ X, 
and let S be the set of functions 
S = { J ∈ E(X) | J(t) = 0, J(x) > ↑↓, x ∈ X 
} . 
Clearly C is S-regular, so we may consider the perturbation framework of Exercise 4.8 with p(x) = 1 for all x '= t and p(t) = 0. Apply the results of that exercise to show that: 
(a) We have 
J→ C = lim 
δ↓0 Ĵδ. 
(b) J→ C is the only fixed point of T within the set 
W = { J ∈ E(X) | J(t) = 0, J → J→ 
C 
} . 
(c) We have T kJ → J→ C for all J ∈ W. 
Solution: Part (a) follows from Exercise 4.8, and parts (b), (c) follow from Exercise 4.8 and Prop. 4.4.2.
332 Noncontractive Models Chap. 4 
4.10 (On Proper Policies for Stochastic Shortest Paths) 
Consider the infinite-spaces SSP problem of Section 4.6 under the assumptions of Prop. 4.6.4, and assume that g is bounded over X + U +W . 
(a) Show that if µ is a uniformly proper policy, then Jµ is the unique solution of the equation J = TµJ within B and that T k 
µJ , Jµ for all J $ B. 
(b) Let J & be a fixed point of T such that J & $ B and J & )= Ĵ . Show that a policy µ satisfying TµJ 
& = TJ & cannot be uniformly proper. 
Solution: (a) Consider the problem where the only policy is µ, i.e., with control constraint set Ũ(x) = 
& µ(x) 
' , x $ X, and apply Props. 4.6.5 and 4.4.4. 
(b) Assume to come to a contradiction that µ is uniformly proper. We have TµJ 
& = TJ & = J &, so by part (a) we have J & = Jµ, while Jµ & Ĵ since µ is uniformly proper. Thus J & & Ĵ while J & )= Ĵ by assumption. This contradicts the largest fixed point property of Ĵ [cf. Prop. 4.6.5(a)]. 
4.11 (Example where Ĵ is not a Fixed Point of T in Infinite Spaces SSP) 
We noted in Section 4.6 that some additional assumption, like 
E -g(x, u,w) + Ĵ$ 
! f(x, u,w) 
"3 < #, % x $ X", u $ U(x), (4.96) 
or the finiteness of W , is necessary to prove that Ĵ is a fixed point for SSP problems (cf. Prop. 4.6.4). [The condition (4.96) is satisfied for example if there exists a policy " (necessarily proper at all x $ X") such that J",$ is bounded over X".] To see what can happen without such an assumption, consider the following example, which was constructed by Yi Zhang (private communication). 
LetX = {t, 0, 1, 2, . . .}, where t is the termination state, and let g(x, u,w) * 0, so that J"(x) * 0. There is only one control at each state, and hence only one policy. The transitions are as follows: 
From each state x = 2, 3, . . . , we move deterministically to state x!1, from state 1 we move deterministically to state t, and from state 0 we move to state x = 1, 2, . . ., with probability px such that 
1% x=1 
xpx = #. Verify that the unique policy is proper at all x = 1, 2, . . ., and we have 
Ĵ(x) = J"(x) = 0. However, the policy is not proper at x = 0, since the expected number of transitions from x = 0 to termination is 
1% x=1 
xpx = #. As a result 
the set 6!0 is empty and we have Ĵ(0) = #. Thus Ĵ does not satisfy the Bellman equation for x = 0, since 
# = Ĵ(0) )= E -g(0, u, w) + Ĵ 
! f(0, u, w) 
"3 = 
%. 
x=1 
pxĴ(x) = 0.
Sec. 4.7 Notes, Sources, and Exercises 333 
4.12 (Convergence of Nonexpansive Monotone Fixed Point Iterations with a Unique Fixed Point) 
Consider the mapping H of Section 2.1 under the monotonicity Assumption 2.1.1. Assume that instead of the contraction Assumption 2.1.2, the following hold: 
(1) For every J $ B(X), the function TJ belongs to B(X), the space of functions on X that are bounded with respect to the weighted sup-norm corresponding to a positive weighting function v. 
(2) T is nonexpansive, i.e., -TJ ! TJ &- " -J ! J &- for all J, J & $ B(X). 
(3) T has a unique fixed point within B(X), denoted J". 
(4) If X is infinite the following continuity property holds: For each J $ B(X) and {Jm} . B(X) with either Jm ( J or Jm 1 J , 
H (x, u, J) = lim m$% 
H(x,u, Jm), % x $ X, u $ U(x). 
Show the following: 
(a) For every J $ B(X), we have -T kJ!J"- , 0 if X is finite, and T kJ , J" 
if X is infinite. 
(b) Part (a) holds if B(X) is replaced by & J $ B(X) | J & 0 
' , or by 
& J $ 
B(X) | J(t) = 0 ' , or by 
& J $ B(X) | J(t) = 0, J & 0 
' , where t is a special 
cost-free and absorbing destination state t. 
(Unpublished joint work of the author with H. Yu.) 
Solution: (a) Assume first that X is finite. For any c > 0, let V0 = J" + c v and consider the sequence {Vk} defined by Vk+1 = TVk for k & 0. Note that {Vk} . B(X), since -V0- " -J"-+c so that V0 $ B(X), and we have Vk+1 = TVk, so that property (1) applies. From the nonexpansiveness property (2), we have 
H(x, u, J" + c v) " H(x, u, J") + c v(x), x $ X, u $ U(x), 
and by taking the infimum over u $ U(x), we obtain J" " T (J"+ c v) " J"+ c v, i.e., J" " V1 " V0. From this and the monotonicity of T it follows that J" " Vk+1 " Vk for all k, so that for each x $ X, Vk(x) ( V (x) where V (x) & J"(x). Moreover, V lies in B(X) (since J" " V " Vk), and also satisfies -Vk ! V - , 0 (since X is finite). From property (2), we have -TVk ! TV - " -Vk ! V -, so that -TVk ! TV - , 0, which together with the fact TVk = Vk+1 , V , implies that V = TV . Thus V = J" by the uniqueness property (3), and it follows that Vk ( J". 
Similarly, define Wk = T k(J" ! c v), and by an argument symmetric to the above, Wk 1 J". Now for any J $ B(X), let c = -J ! J"- in the definition of Vk 
and Wk. Then J" ! c v " J " J" + c v, so by the monotonicity of T , we have Wk " T kJ " Vk as well as Wk " J" " Vk for all k. Therefore -T kJ ! J"- " -Wk ! Vk- for all k & 0. Since -Wk ! Vk- " -Wk ! J"- + -Vk ! J"- , 0, the conclusion follows. 
If X is infinite and property (4) holds, the preceding proof goes through, except for the part that shows that -Vk ! V - , 0. Instead we use a di#erent
334 Noncontractive Models Chap. 4 
argument to prove that V = TV . Indeed, since Vk & Vk+1 = TVk & TV , it follows that V & TV . For the reverse inequality we write 
TV = inf u#U(x) 
lim k$% 
H(x, u, Vk) & lim k$% 
inf u#U(x) 
H(x, u, Vk) = lim k$% 
TVk = V , 
where the first equality follows from the continuity property (4), and the inequality follows from the generic relation inf limH & lim infH . Thus we have V = TV , which by the uniqueness property (3), implies that V = J" and Vk ( J". With a similar argument we obtain Wk 1 J", implying that T kJ , J". 
(b) The proof of part (a) applies with simple modifications. 
4.13 (Convergence of Nonexpansive Monotone Fixed Point Iterations with Multiple Fixed Points) 
Consider the mapping H of Section 2.1 under the monotonicity Assumption 2.1.1. Assume that instead of the contraction Assumption 2.1.2, the following hold: 
(1) For every J $ B(X), the function TJ belongs to B(X), the space of functions on X that are bounded with respect to the weighted sup-norm corresponding to a positive weighting function v. 
(2) T is nonexpansive, i.e., -TJ ! TJ &- " -J ! J &- for all J, J & $ B(X). 
(3) T has a largest fixed point within B(X), denoted Ĵ , i.e., Ĵ $ B(X), Ĵ is a fixed point of T , and for every other fixed point J & $ B(X) we have J & " Ĵ . 
(4) If X is infinite the following continuity property holds: For each J $ B(X) and {Jm} . B(X) with either Jm ( J or Jm 1 J , 
H (x, u, J) = lim m$% 
H(x,u, Jm), % x $ X, u $ U(x). 
Show the following: 
(a) For every J $ B(X) such that Ĵ " J " Ĵ + c v for some c > 0, we have -T kJ ! Ĵ- , 0 if X is finite, and T kJ , Ĵ if X is infinite. 
(b) Part (a) holds if B(X) is replaced by & J $ B(X) | J & 0 
' , or by 
& J $ 
B(X) | J(t) = 0 ' , or by 
& J $ B(X) | J(t) = 0, J & 0 
' , where t is a special 
cost-free and absorbing destination state t. 
(Note the similarity with the preceding exercise.) 
Solution: (a) The proof follows the line of proof of the preceding exercise. As-sume first that X is finite. For any c > 0, let V0 = Ĵ + c v and consider the sequence {Vk} defined by Vk+1 = TVk for k & 0. Note that {Vk} . B(X), since -V0- " -Ĵ- + c so that V0 $ B(X), and we have Vk+1 = TVk, so that property (1) applies. From the nonexpansiveness property (2), we have 
H(x, u, Ĵ + c v) " H(x, u, Ĵ) + c v(x), x $ X, u $ U(x), 
and by taking the infimum over u $ U(x), we obtain Ĵ " T (Ĵ+c v) " Ĵ+c v, i.e., Ĵ " V1 " V0. From this and the monotonicity of T it follows that Ĵ " Vk+1 " Vk
Sec. 4.7 Notes, Sources, and Exercises 335 
for all k, so that for each x $ X, Vk(x) ( V (x) where V (x) & Ĵ(x). Moreover, V lies in B(X) (since Ĵ " V " Vk), and also satisfies -Vk ! V - , 0 (since X is finite). From property (2), we have -TVk ! TV - " -Vk ! V -, so that -TVk ! TV - , 0, which together with the fact TVk = Vk+1 , V , implies that V = TV . Thus V = Ĵ by property (3), and it follows that Vk ( Ĵ . 
If X is infinite and property (4) holds, the preceding proof goes through, except for the part that shows that -Vk ! V - , 0. Instead we use a di#erent argument to prove that V = TV . Indeed, since Vk & Vk+1 = TVk & TV , it follows that V & TV . For the reverse inequality we write 
TV = inf u#U(x) 
lim k$% 
H(x, u, Vk) & lim k$% 
inf u#U(x) 
H(x, u, Vk) = lim k$% 
TVk = V , 
where the first equality follows from the continuity property (4). Thus we have V = TV , which by property (3), implies that V = Ĵ and Vk ( Ĵ . 
(b) The proof of part (a) applies with simple modifications. 
4.14 (Necessary and Su!cient Condition for an Interpolated Nonexpansive Mapping to be a Contraction) 
This exercise (due to unpublished joint work with H. Yu) considers a nonexpansive mapping G : 'n 2, 'n, and derives conditions under which the interpolated mapping G% defined by 
G%(x) = (1! &)x+ &G(x), x $ 'n, 
is a contraction for all & $ (0, 1). Consider 'n equipped with a strictly convex norm - · -, and the set 
C = 
4( x! y 
-x! y-, G(x)!G(y) 
-x! y-
) 22222 x, y $ 'n, x )= y 
5 , 
which can be viewed as a set of “slopes” of G along all directions. Show that the mapping G% defined by 
G%(x) = (1! &)x+ &G(x), x $ 'n, 
is a contraction for all & $ (0, 1) if and only if there is no closure point (z, w) of C such that z = w. Note: To illustrate with some one-dimensional examples what can happen if this closure condition is violated, let G : ' 2, ' be continuously di#erentiable, monotonically nondecreasing, and satisfying 0 " dG(x) 
dx " 1. Note 
that G is nonexpansive. We consider two cases. 
(1) G(0) = 0, dG(0) dx 
= 1, 0 " dG(x) dx 
< 1 for x )= 0, limx$% dG(x) dx 
< 1 and 
limx$!% dG(x) dx 
< 1. Here (z, w) = (1, 1) is a closure point of C and satisfies z = w. Note that G% is not a contraction for any & $ (0, 1), although it has 0 as its unique fixed point.
336 Noncontractive Models Chap. 4 
(2) limx$% dG(x) dx 
= 1. Here we have limx$% 
! G(x) ! G(y) 
" = x ! y for 
x = y+1, so (1, 1) is a closure point of C. It can also be seen that because 
limx$% dG% (x) 
dx = 1, G% is not a contraction for any & $ (0, 1), and may 
have one, more than one, or no fixed points. 
Solution: Assume there is no closure point (z, w) of C such that z = w, and for & $ (0, 1), let 
( = sup (z,w)#C 
99(1! &)z + &w 99. 
The set C is bounded since for all (z, w) $ C, we have -z- = 1, and -w- " 1 by the nonexpansiveness of G. Hence, there exists a sequence 
& (zk, wk) 
' . C that 
converges to some (z, w), and is such that 
99(1! &)zk + &wk 
99, (. 
Since (z, w) is a closure point of C, we have z )= w. Using the continuity of the norm, we have 
( = 99(1! &)z + &w 
99 < (1! &)-z-+ &-w- " 1, 
where for the strict inequality we use the strict convexity of the norm, and for the last inequality we use the fact -z- = 1 and -w- " 1. Thus ( < 1, and since 
9999(1! &) x! y 
-x! y-+ & 
G(x)!G(y) 
-x! y-
9999 = 
99G%(x)!G%(y) 99 
-x! y-
" sup (z,w)#C 
99(1! &)z + &w 99 
= (, % x )= y, 
it follows that G% is a contraction of modulus (. Conversely, if G% is a contraction, we have 
sup (z,w)#C 
99(1! &)z + &w 99 = sup 
x )=y 
9999(1! &) x! y 
-x! y-+ & 
G(x)!G(y) -x! y-
9999 
" sup x )=y 
99G%(x)!G%(y) 99 
-x! y-
< 1. 
Thus for every closure point (z, w) of C, 
99(1! &)z + &w 99 < 1, 
which implies that we cannot have z = w.
5 Sequential Zero-Sum Games and 
Minimax Control 
Contents 
5.1. Introduction . . . . . . . . . . . . . . . . . . . p. 338 5.2. Relations to Single Player Abstract DP Formulations . p. 344 5.3. A New PI Algorithm for Abstract Minimax DP Problems p. 350 5.4. Convergence Analysis . . . . . . . . . . . . . . . p. 364 5.5. Approximation by Aggregation . . . . . . . . . . . p. 371 5.6. Notes and Sources . . . . . . . . . . . . . . . . p. 373 
337
338 Sequential Zero-Sum Games and Minimax Control Chap. 5 
In this chapter, we introduce a contractive abstract DP framework and related policy iteration (PI) algorithms, specifically designed for sequential zero-sum games and minimax problems with a general structure. Aside from greater generality, the advantage of our algorithms over alternatives is that they resolve some long-standing convergence di!culties of the “natural” PI algorithm, which have been known since the Pollatschek and Avi-Itzhak method [PoA69] for finite-state Markov games. Mathematically, this “natural” algorithm is a form of Newton’s method for solving Bellman’s equation, but Newton’s method, contrary to the case of single-player DP problems, is not globally convergent in the case of a minimax problem, because of an additional di!culty: the Bellman operator may have components that are neither convex nor concave. 
Our algorithms address this di!culty by introducing alternating player choices, and by using a policy-dependent mapping with a uniform supnorm contraction property, similar to earlier works by Bertsekas and Yu [BeY10], [BeY12], [YuB13a], which has been described in part in Section 2.6.3. Moreover, our algorithms allow a convergent and highly parallelizable implementation, which is based on state space partitioning, and distributed asynchronous policy evaluation and policy improvement operations within each set of the partition. They are also suitable for approximations based on an aggregation approach. 
5.1 INTRODUCTION 
We will discuss abstract DP frameworks and PI methods for sequential minimax problems. In addition to being more e!cient and reliable than alternatives, our methods are well suited for distributed asynchronous implementation. In Sections 5.1 and 5.2, we will discuss an abstract DP framework, which can be derived from the contractive framework of Chap-ter 2. We will revisit abstract PI algorithms within this framework and show how they relate to known algorithms for minimax control. We will also discuss how these algorithms when applied to discounted and terminating zero-sum Markov games, lead to methods such as the ones by Ho"man and Karp [HoK66], and by Pollatschek and Avi-Itzhak [PoA69]. We will note some of the drawbacks of these methods, particularly the need to solve a substantial optimization problem as part of the policy evaluation phase. These drawbacks motivate new PI algorithms and a di"erent abstract framework, based on an alternating player choices format, which we will introduce in Section 5.3. 
In our initial problem formulation, the focus of Sections 5.1 and 5.2, we consider abstract sequential infinite horizon zero-sum game and minimax problems, which involve two players that choose controls at each state x of some state space X , from within some state-dependent constraint sets: a minimizer , who selects a control u from within a subset U(x) of a control
Sec. 5.1 Introduction 339 
space U , and a maximizer , who selects a control v from within a subset V (x) of a control space V . The spaces X , U , and V are arbitrary. Func-tions µ : X !" U and ! : X !" V such that µ(x) # U(x) and !(x) # V (x) for all x # X , are called policies for the minimizer and the maximizer, respectively. The set of policies for the minimizer and the maximizer are denoted by M and N , respectively. 
As in earlier chapters, the main idea is to start with a general mapping that defines the Bellman equation of the problem. In particular, we introduce a real-valued mapping that is suitable for minimax problems, and has the form 
H(x, u, v, J), x # X, u # U(x), v # V (x), J # B(X); (5.1) 
cf. Example 2.6.4. In Eq. (5.1), B(X) is the space of real-valued functions on X that are bounded with respect to a weighted sup-norm 
$J$ = sup x!X 
! 
!J(x) ! 
! 
"(x) , J # B(X), (5.2) 
where " is a function taking a positive value "(x) for each x # X . Our main assumption is the following: 
Assumption 5.1.1: (Contraction for Minimax Problems) For every µ # M, ! # N , consider the operator Tµ,! that maps a function J # B(X) to the function Tµ,!J defined by 
(Tµ,!J)(x) = H " 
x, µ(x), !(x), J # 
, x # X, (5.3) 
and assume the following: 
(a) Tµ,!J belongs to B(X) for all J # B(X). 
(b) There exists an # # (0, 1) such that for all µ # M, ! # N , the operator Tµ,! is a contraction mapping of modulus # with respect to the weighted sup-norm (5.2), i.e., for all J, J " # B(X), µ # M, and ! # N , 
$Tµ,!J %Tµ,!J "$ = sup x!X 
! 
!(Tµ,!J)(x) % (Tµ,!J ")(x) ! 
! 
"(x) & #$J %J "$. 
Since Tµ,! is a contraction within the complete space B(X), under the preceding assumption, it has a unique fixed point Jµ,! # B(X). We are interested in the operator T : B(X) !" B(X), defined by 
(TJ)(x) = inf u!U(x) 
sup v!V (x) 
H(x, u, v, J), x # X, (5.4)
340 Sequential Zero-Sum Games and Minimax Control Chap. 5 
or equivalently, 
(TJ)(x) = inf µ!M 
sup !!N 
(Tµ,!J)(x), x # X. (5.5) 
An important fact is that T is a contraction mapping from B(X) to B(X). Indeed from Assumption 1.1(b), we have for all x # X , µ # M, and ! # N , 
(Tµ,!J)(x) & (Tµ,!J ")(x) + #$J % J "$ "(x). 
Taking the supremum over ! # N of both sides above, and then the infimum over µ # M, and using Eq. (5.5), we obtain 
(TJ)(x) & (TJ ")(x) + #$J % J "$ "(x), for all x # X. 
Similarly, by reversing the roles of J and J ", we obtain 
(TJ ")(x) & (TJ ")(x) + #$J % J "$ "(x), for all x # X. 
Combining the preceding two relations, we have 
! 
!(TJ)(x)% (TJ ")(x) ! 
! & #$J % J "$ "(x), for all x # X, 
and by dividing with "(x), and taking supremum over x # X , it follows that 
$TJ % TJ "$ & #$J % J "$. 
Thus T is a contraction mapping from B(X) to B(X), with respect to the sup-norm (5.2), with modulus #, and has a unique fixed point within B(X), which we denote by J*. 
Bellman’s Equation and Minimax Optimal Policies 
Given a mapping H of the form (5.1) that satisfies Assumption 1.1, we are interested in computing the fixed point J* of T , i.e., a function J* such that 
J*(x) = inf u!U(x) 
sup v!V (x) 
H(x, u, v, J*), for all x # X. (5.6) 
Moreover, we are interested in finding a policy µ# # M (if it exists) that attains the infimum for all x # X as in the following equation 
µ#(x) # arg min u!U(x) 
H(x, u, J*), for all x # X, 
where for all x # X , u # U(x), and J # B(X), the mapping H is defined by 
H(x, u, J) = sup v!V (x) 
H(x, u, v, J).
Sec. 5.1 Introduction 341 
We are also interested in finding a policy !# # N (if it exists) that attains the supremum for all x # X as in the following equation 
!#(x) # arg max v!V (x) 
H " 
x, µ#(x), v, J* # 
, for all x # X. 
In the context of a sequential minimax problem that is addressed by DP, the fixed point equation J* = TJ* is viewed as a form of Bellman’s equation. In this case, J*(x) is the minimax cost starting from state x. Moreover µ# is an optimal policy for the minimizer in a minimax sense, while !# is a corresponding worst case response of the maximizer . Under suitable assumptions on H (such as convexity in u and concavity in v) the order of minimization and maximization can be interchanged in the preceding relations, in which case it can be shown that (µ#, !#) is a saddle point (within the space M ' N ) of the minimax value Jµ,!(x), for every x # X . 
Markov Games 
The simplest special case of a sequential stochastic game problem, which relates to our abstract framework, was introduced in the paper by Shapley [Sha53] for undiscounted finite-state problems, with a termination state, where the Bellman operator Tµ,! is contractive with respect to the (unweighted) sup-norm for all µ # M, and ! # N . Shapley’s work brought the contraction mapping approach to prominence in DP and sequential game analysis, and was subsequently extended by several authors in both undiscounted and discounted settings; see e.g., the book by Filar and Vrieze [FiV97], the lecture notes by Kallenberg [Kal20], and the works referenced there. Let us now describe a class of finite-state zero-sum game problems that descend from Shapley’s work, and are often called “Markov games” (the name was introduced by Zachrisson [Zac64]). 
Example 5.1.1 (Discounted Finite-State Markov Games) 
Consider two players that play repeated matrix games at each of an infinite number of stages, using mixed strategies. The game played at a given stage is defined by a state x that takes values in a finite set X, and changes from one stage to the next according to a Markov chain whose transition probabilities are influenced by the players’ choices. At each stage and state x ! X, the minimizer selects a probability distribution u = (u1, . . . , un) over n possible choices i = 1, . . . , n, and the maximizer selects a probability distribution v = (v1, . . . , vm) over m possible choices j = 1, . . . ,m. If the minimizer chooses i and the maximizer chooses j, the payo! of the stage is aij(x) and depends on the state x. Thus the expected payo! of the stage is 
$ 
i,j aij(x)uivj or 
u!A(x)v, where A(x) is the n " m matrix with components aij(x) (u and v are viewed as column vectors, and a prime denotes transposition).
342 Sequential Zero-Sum Games and Minimax Control Chap. 5 
The state evolves according to transition probabilities qxy(i, j), where i and j are the moves selected by the minimizer and the maximizer, respectively (here y represents the next state and game to be played after moves i and j are chosen at the game represented by x). When the state is x, under u and v, the state transition probabilities are 
pxy(u, v) = 
n % 
i=1 
m % 
j=1 
uivjqxy(i, j) = u!Qxyv, 
where Qxy is the n " m matrix that has components qxy(i, j). Payo!s are discounted by ! ! (0, 1), and the objectives of the minimizer and maximizer, are to minimize and to maximize the total discounted expected payo!, respectively. 
As shown by Shapley [Sha53], the problem can be formulated as a fixed point problem involving the mapping H given by 
H(x, u, v, J) = u!A(x)v + ! % 
y"X 
pxy(u, v)J(y) 
= u! 
& 
A(x) + ! % 
y"X 
QxyJ(y) 
' 
v. 
(5.7) 
It can be verified that H satisfies the contraction Assumption 1.1 [with "(x) # 1]. Thus the corresponding operator T is an unweighted sup-norm contraction, and its unique fixed point J# satisfies the Bellman equation 
J#(x) = (TJ#)(x) = min u"U 
max v"V 
H(x, u, v, J#), for all x ! X, (5.8) 
where U and V denote the sets of probability distributions u = (u1, . . . , un) and v = (v1, . . . , vm), respectively. 
Since the matrix defining the mapping H of Eq. (5.7), 
A(x) + ! % 
y"X 
QxyJ(y), 
is independent of u and v, we may view J#(x) as the value of a static (nonsequential) matrix game that depends on x. In particular, from a fundamental saddle point theorem for matrix games, we have 
min u"U 
max v"V 
H(x, u, v, J#) = max v"V 
min u"U 
H(x, u, v, J#), for all x ! X. (5.9) 
It was shown by Shapley [Sha53] that the strategies obtained by solving the static saddle point problem (5.9) correspond to a saddle point of the sequential game in the space of strategies. Thus once we find J# as the fixed point of the mapping T [cf. Eq. (5.8)], we can obtain equilibrium policies for the minimizer and maximizer by solving the matrix game (5.9).
Sec. 5.1 Introduction 343 
Example 5.1.2 (Undiscounted Finite-State Markov Games with a Termination State) 
Here the problem is the same as in the preceding example, except that there is no discount factor (! = 1), and in addition to the states in X, there is a termination state t that is cost-free and absorbing. In this case the mapping H is given by 
H(x, u, v, J) = u! 
& 
A(x) + % 
y"X 
QxyJ(y) 
' 
v, (5.10) 
cf. Eq. (5.7), where the matrix of transition probabilities Qxy may be substochastic, while T has the form 
(TJ)(x) = min u"U 
max v"V 
H(x, u, v, J). (5.11) 
Assuming that the termination state t is reachable with probability one under all policy pairs, it can be shown that the mapping H satisfies the contraction Assumption 1.1, so results and algorithms that are similar to the ones for the preceding example apply. This reachability assumption, however, is restrictive and is not satisfied when the problem has a semicontractive character, whereby Tµ,! is a contraction under some policy pairs but not for others. In this case the analysis is more complicated and requires the notion of proper and improper policies from single-player stochastic shortest path problems; see the papers [BeT91], [PaB99], [YuB13a], [Yu14]. 
In the next section, we will view our abstract minimax problem, involving the Bellman equation (5.6), as an optimization by a single player who minimizes against a worst-case response by an antagonistic oppo-nent/maximizer, and we will describe the corresponding PI algorithm. This algorithm has been known for the case of Markov games since the 1960s. We will highlight the main weakness of this algorithm: the computational cost of the policy evaluation operation, which involves the solution of the maximizer’s problem for a fixed policy of the minimizer. We will then discuss an attractive proposal by Pollatschek and Avi-Itzhak [PoA69] that overcomes this di!culty, albeit with an algorithm that requires restrictive assumptions for its validity. Then, in Section 5.3, we will introduce and analyze a new algorithm, which maintains the attractive structure of the Pollatschek and Avi-Itzhak algorithm without requiring restrictive assumptions. We will also show the validity of our algorithm in the context of a distributed asynchronous implementation, as well as in an on-line context, which involves one-state-at-a-time policy improvement, with the states generated by an underlying dynamic system or Markov chain.
344 Sequential Zero-Sum Games and Minimax Control Chap. 5 
5.2 RELATIONS TO SINGLE-PLAYER ABSTRACT DP FORMULATIONS 
In this section, we will reformulate our minimax problem in a way that will bring to bear the theory of Chapter 2. In particular, we will view the problem of finding a fixed point of the minimax operator T of Eq. (5.4) [cf. the Bellman equation (5.6)] as a single-player optimization problem by redefining T in terms of the mapping H given by 
H(x, u, J) = sup v!V (x) 
H(x, u, v, J), x # X, u # U(x), J # B(X). 
(5.12) In particular, we write T as 
(TJ)(x) = inf u!U(x) 
H(x, u, J), x # X, (5.13) 
or equivalently, by introducing for each µ # M the operator Tµ given by 
(T µJ)(x) = H " 
x, µ(x), J # 
= sup v!V (x) 
H " 
x, µ(x), v, J # 
, x # X, (5.14) 
we write T as 
(TJ)(x) = inf µ!M 
(TµJ)(x), x # X. (5.15) 
Our contraction assumption implies that all the operators Tµ, µ # M, as well as the operator T are weighted sup-norm contractions from B(X) to B(X), with modulus #. 
Thus the single-player weighted sup-norm contractive DP framework of Chapter 2 applies directly to the operator T as defined by Eq. (5.15). In particular, to apply this framework to a minimax problem, we start from the mapping H of Eq. (5.12), which defines Tµ via Eq. (5.14), and then T , using Eq. (5.15). 
PI Algorithms 
In view of the preceding transformation of our minimax problem to the single-player abstract DP formalism, the PI algorithms developed for the latter apply, and in fact these algorithms have been known for a long time for the special case of finite-state Markov games, cf. Examples 5.1.1 and 5.1.2. 
In particular, the standard form of PI generates iteratively a sequence of policies {µt}. The typical iteration starts with µt and computes µt+1 
with a minimization that involves the optimal cost function of a maxi-
Sec. 5.2 Relations to Single-Player Abstract DP 345 
mizer’s abstract DP problem with the minimizer’s policy fixed at µt, as follows:† 
Iteration (t + 1) of Abstract PI Algorithm from the Mini-mizer’s Point of View 
Given µt, generate µt+1 with a two-step process: 
(a) Policy evaluation, which computes Jµt as the unique fixed 
point of the mapping Tµt given by Eq. (5.14), i.e., 
Jµt = TµtJµt , (5.16) 
or equivalently 
Jµt(x) = max v!V (x) 
H " 
x, µt(x), v, Jµt 
# 
, x # X. (5.17) 
(b) Policy improvement, which computes µt+1 as a policy that satisfies 
Tµt+1Jµt = TJµt , (5.18) 
or equivalently 
µt+1(x) # arg min u!U(x) 
( 
max v!V (x) 
H(x, u, v, Jµt) 
) 
, x # X. 
(5.19) 
There are also optimistic forms of PI , which starting with a function J0 # B(X), generate a sequence of function-policy pairs {J t, µt} with the algorithm 
TµtJ t = TJ t, J t+1 = T mt µt J t, k = 0, 1, . . . , (5.20) 
where {mt} is a sequence of positive integers; see Section 2.5. Here the policy evaluation operation (5.16) that finds the fixed point of the mapping Tµt is approximated by mt value iterations using Tµt , and starting from J t, as in the second equation of (5.20). The convergence of the abstract forms of these PI algorithms has been established under the additional 
† Policy improvement involves an optimization operation that defines the new/improved policy. Throughout this chapter, and in the context of PI algo-
rithms, we implicitly assume that this optimization can be carried out, i.e., that 
the optimum is attained, and write accordingly “min” and “max” in place of “inf” and “sup,” respectively.
346 Sequential Zero-Sum Games and Minimax Control Chap. 5 
monotonicity assumption 
TµJ & TµJ " for all J, J " # B(X) with J & J ", (5.21) 
which is typically satisfied in DP-type single-player and two-player problem formulations. 
The drawback of the preceding PI algorithms is that the policy evaluation operation of Eq. (5.16) and its optimistic counterpart of Eq. (5.20) aim to find or approximate the fixed point of Tµt , which involves a potentially time-consuming maximization over v # V (x); cf. the definition (5.14) and Eq. (5.17). This can be seen from the fact that Eq. (5.17) is Bellman’s equation for a maximizer’s abstract DP problem, where the minimizer is known to use the policy µt. There is a PI algorithm for finite-state Markov games, due to Pollatschek and Avi-Itzhak [PoA69], which was specifically designed to avoid the use of maximization over v # V (x) in the policy evaluation operation. We present this algorithm next, together with a predecessor PI algorithm, due to Ho"man and Karp [HoK66], which is in fact the algorithm (5.16)-(5.19) applied to the Markov game Example 5.1.1. 
The Ho!man-Karp, and Pollatschek and Avi-Itzhak Algorithms for Finite-State Markov Games 
The PI algorithm (5.16)-(5.19) for the special case of finite-state Markov games (cf. Example 5.1.1), has been proposed by Ho"man and Karp [HoK66]. It takes the form 
Jµt(x) = max v!V 
H " 
x, µt(x), v, Jµt 
# 
, x # X, (5.22) 
where H is the Markov game mapping (5.7) (this is the policy evaluation step), followed by solving the static minimax problem 
min u!U 
max v!V 
H(x, u, v, Jµt), x # X, (5.23) 
and letting µt+1 be a policy that attains the minimum above (this is the policy improvement step). The policy improvement subproblem (5.23) is a matrix saddle point problem, involving the matrix 
A(x) + % 
y!X 
QxyJµt(y), 
[cf. Eq. (5.10)], which is easily solvable by linear programming for each x (this is well-known in the theory of matrix games). 
However, the policy evaluation step (5.22) involves the solution of the maximizer’s Markov decision problem, for the fixed policy µt of the minimizer. This can be a quite di!cult problem that requires an expensive
Sec. 5.2 Relations to Single-Player Abstract DP 347 
computation. The same is true for a modified version of the Ho"man-Karp algorithm proposed by van der Wal [Van78], which involves an approximate policy evaluation, based on a limited number of value iterations, as in the optimistic PI algorithm (5.20). The computational di!culty of the policy evaluation phase of the Ho"man-Karp algorithm is also shared by other PI algorithms for sequential games that have been suggested in the literature in subsequent works (e.g., Patek and Bertsekas [PaB99], and Yu [Yu14]). 
Following the publication of the Ho"man-Karp algorithm, another PI algorithm for finite-state Markov games was proposed by Pollatschek and Avi-Itzhak [PoA69], and has attracted considerable attention because it is more computationally expedient. It generates a sequence of minimizermaximizer policy pairs {µt, !t} and corresponding game value functions Jµt,!t(x), starting from each state x. In particular, the standard form of PI generates iteratively a sequence of policies {µt}. We give this algorithm in an abstract form, which parallels the PI algorithm (5.16)-(5.19). The typical iteration starts with a pair (µt, !t) and computes a pair (µt+1, !t+1) as follows: 
Iteration (t + 1) of the Pollatschek and Avi-Itzhak PI Algo-rithm in Abstract Form 
Given (µt, !t), generate (µt+1, !t+1) with a two-step process: 
(a) Policy evaluation, which computes Jµt,!t by solving the fixed point equation 
Jµt,!t(x) = H " 
x, µt(x), !t(x), Jµt,!t # 
, x # X. (5.24) 
(b) Policy improvement, which computes (µt+1, !t+1) by solving the saddle point problem 
min u!U 
max v!V 
H(x, u, v, Jµt,!t), x # X. (5.25) 
The Pollatschek and Avi-Itzhak algorithm [PoA69] is the algorithm (5.24)-(5.25), specialized to the Markov game case of the mapping H that involves the matrix 
A(x) + % 
y!X 
QxyJµt,!t(y), 
similar to the Ho"man-Karp algorithm, cf. Eq. (5.10). A key observation is that the policy evaluation operation (5.24) is computationally comparable to policy evaluation in a single-player Markov decision problem, i.e., solving a linear system of equations. In particular, it does not involve solution of the Markov decision problem of the maximizer like the Ho"man-Karp
348 Sequential Zero-Sum Games and Minimax Control Chap. 5 
PI algorithm [cf. Eq. (5.22)], or its approximate solution by multiple value iterations, as in the van der Wal optimistic version (5.20) for Markov games. 
Computational studies have shown that the Pollatschek and Avi-Itzhak algorithm converges much faster than its competitors, when it converges (see Breton et al. [BFH86], and also Filar and Tolwinski [FiT91], who proposed a modification of the algorithm). Moreover, the number of iterations required for convergence is fairly small. This is consistent with an interpretation given by Pollatschek and Avi-Itzhak in their paper [PoA69], where they have shown that their algorithm coincides with a form of Newton’s method for solving the fixed point/Bellman equation J = TJ (see Fig. 5.2.1).† The close connection of PI with Newton’s method is wellknown in control theory and operations research, through several works, including Kleinman [Kle68] for linear-quadratic optimal control problems, and Puterman and Brumelle [PuB78], [PuB79] for more abstract settings. Its significance in reinforcement learning contexts has been discussed at length in the author’s recent books [Ber20] and [Ber22]; see also Section 1.3. 
Unfortunately, however, the Pollatschek and Avi-Itzhak algorithm is valid only under restrictive assumptions (given in their paper [PoA69]). The di!culty is that Newton’s method applied to the Bellman equation J = TJ need not be globally convergent when the operator T corresponds to a minimax problem. This is illustrated in Fig. 5.2.1, which also illustrates why Newton’s method (equivalently, the PI algorithm) is globally 
† Newton’s method for solving a general fixed point problem of the form z = F (z), where z is an n-dimensional vector, operates as follows: At the current iterate zk, we linearize F and find the solution zk+1 of the corresponding linear fixed point problem, obtained using a first order Taylor expansion: 
zk+1 = F (zk) + #F (zk) 
#z (zk+1 $ zk), 
where #F (zk)/#z is the n"n Jacobian matrix of F evaluated at the n-dimensional vector zk. The most commonly given convergence rate property of Newton’s method is quadratic convergence. It states that near the solution z#, we have 
%zk+1 $ z#% = O " 
%zk $ z#%2 # 
, 
where % ·% is the Euclidean norm, and holds assuming the Jacobian matrix exists and is Lipschitz continuous (see [Ber16c], Section 1.4). Qualitatively similar 
results hold under other assumptions. In particular a superlinear convergence 
statement (suitably modified to account for lack of di!erentiability of F ) can be proved for the case where F (z) has components that are either monotonically 
increasing or monotonically decreasing, and either concave or convex. In the 
case of the Pollatschek and Avi-Itzhak algorithm, the main di"culty is that the concavity/convexity condition is violated; see Fig. 5.2.1.
Sec. 5.2 Relations to Single-Player Abstract DP 349 
1 J J 
TJ 
TJ 
Single policy Minimax Current policy pair (µ, !) Next policy pair (˜ 
) Info Tµ,!J T 
) Next policy pair (µ̃, !̃) Info 
J Tµ̃,!̃J 
Single policy Minimax J! = TJ! Jµ,! = Tµ,!Jµ,!Jµ̃,!̃ = Tµ̃,!̃Jµ̃,!̃ 
Cost of (µ, !) Cost of (˜) Cost of (µ̃, !̃) 
Optimal Cost Approximation Minimax- optimal cost Optimal Cost Approximation Minimax- optimal cost MinimaxMinimax 
] 45! line 
max ! 
!11(J), !12(J) " 
! 
max " 
!21(J), !22(J) ! 
Figure 5.2.1 Schematic illustration of the abstract minimax PI algorithm (5.24)-(5.25) in the case of a minimax problem involving a single state, in addition to a termination state t; cf. Example 5.1.2. We have J#(t) = 0 and (TJ)(t) = 0 for all J with J(t) = 0, so that the operator T can be graphically represented in just one dimension (denoted by J) that corresponds to the nontermination state. This makes it easy to visualize T and geometrically interpret why Newton’s method does not converge. Because the operator T may be neither convex nor concave for a minimax problem, the algorithm may cycle between pairs (µ, !) and (µ̃, !̃), as shown in the figure. By contrast in a (single-player) finite-state Markovian decision problem, T has piecewise linear and concave components, and the PI algorithm converges in a finite number of iterations. The figure illustrates an operator T of the form 
TJ = min * 
max + 
"11(J), "12(J) , 
, max + 
"21(J), "22(J) , 
-
, 
where "ij(J), are linear functions of J , corresponding to the choices i = 1, 2 of the minimizer and j = 1, 2 of the maximizer. Thus TJ is the minimum of the convex functions 
max + 
"11(J), "12(J) , 
and max + 
"21(J), "22(J) , 
, 
as shown in the figure. Newton’s method linearizes TJ at the current iterate [i.e., replaces TJ with one of the four linear functions "ij(J), i = 1, 2, j = 1, 2 (the one attaining the min-max at the current iterate)] and solves the corresponding linear fixed point problem to obtain the next iterate.
350 Sequential Zero-Sum Games and Minimax Control Chap. 5 
convergent in the case of a single-player finite-state Markov decision problem, as is well known. In this case each component (TJ)(x) of the function TJ is concave and piecewise linear, thereby guaranteeing the finite termination of the PI algorithm. This is not true in the case of finite-state minimax problems and Markov games. The di!culty is that the functions (TJ)(x) may be neither convex nor concave in J , even though they are piecewise linear and have a monotonicity property (cf. Fig. 5.2.1). In fact a two-state example where the Pollatschek and Avi-Itzhak algorithm does not converge to J* was given by van der Wal [Van78]. This example involves a single state in addition to a termination state, and the algorithm oscillates similar to Fig. 5.2.1. Note that the Ho"man-Karp algorithm does not admit an interpretation as Newton’s method, and is not subject to the convergence di!culties of the Pollatschek and Avi-Itzhak algorithm. 
5.3 A NEW PI ALGORITHM FOR ABSTRACT MINIMAX DP PROBLEMS 
In this section, we will introduce modifications to the Pollatschek and Avi-Itzhak algorithm, and its abstract version (5.24)-(5.25), given in the preceding section, with the aim to enhance its convergence properties, while maintaining its favorable structure. These modifications will apply to a general minimax problem of finding a fixed point of a suitable contractive operator, and o"er the additional benefit that they allow asynchronous, distributed, and on-line implementations. They are also suitable for approximations based on an aggregation approach, which will be discussed in Section 5.5. 
Our PI algorithm is motivated by a line of analysis and corresponding algorithms introduced by Bertsekas and Yu [BeY10], [BeY12] for discounted infinite horizon DP problems, and by Yu and Bertsekas [YuB13a] for stochastic shortest path problems (with both proper and improper policies). These algorithms were also presented in general abstract form in the author’s book [Ber12a], as well as in Section 2.6.3. The PI algorithm of this section uses a similar abstract formulation, but replaces the single mapping that is minimized in these works with two mappings, one of which is minimized while the other is maximized. Mathematically, the di!culty of the Pollatschek and Avi-Itzhak algorithm is that the policies (µt+1, !t+1) obtained from the policy improvement/static game (5.25) are not “improved” in a clear sense, such as 
Jµt+1,!t+1(x) & Jµt,!t(x), for all x # X, 
as they are in the case of single-player DP, where a policy improvement property is central in the standard convergence proof of single-player PI. Our algorithm, however, does not rely on policy improvement, but rather derives its validity from a uniform contraction property of an underlying
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 351 
operator , to be given in Section 5.4 (cf. Prop. 5.4.2). In fact, our algorithm does not require the monotonicity assumption (5.21) for its convergence, and thus it can be used in minimax problems that are beyond the scope of DP.† 
As an aid to understanding intuitively the abstract framework of this section, we note that it is patterned after a multistage process, whereby at each stage, the following sequence of events is envisioned (cf. Fig. 5.3.1): 
(1) We start at some state x1 from a space X1. 
(2) The minimizer, knowing x1, chooses a control u # U(x1). Then a new state x2 from a space X2 is generated as a function of (x1, u). (It is possible that X1 = X2, but for greater generality, we do not assume so. Also the transition from x1 to x2 may involve a random disturbance; see the subsequent Example 3.3.) 
(3) The maximizer, knowing x2, chooses a control v # V (x2). Then a new state x1 # X1 is generated. 
(4) The next stage is started at x1 and the process is repeated. 
If we start with x1 # X1, this sequence of events corresponds to finding the optimal minimizer policy against a worst case choice of the maximizer, and the corresponding min-max value is denoted by J* 
1 (x1). Symmetrically, if we start with x2 # X2, this sequence of events corresponds to finding the optimal maximizer policy against a worst case choice of the minimizer, and the corresponding max-min value is denoted by J* 
2 (x2). This type of framework can be viewed within the context of the theory 
of zero-sum games in extensive form, a methodology with a long history [Kuh53]. Games in extensive form involve sequential/alternating choices by the players with knowledge of prior choices. By contrast, for games in simultaneous form, such as the Markov games of the preceding section, the players make their choices without being sure of the other player’s choices. 
Fixed Point Formulation 
We consider the space of bounded functions of x1 # X1, denoted by B(X1), and the space of bounded functions of x2 # X2, denoted by B(X2), with respect to the norms $J1$1 and $J2$2 defined by 
$J1$1 = sup x1!X1 
! 
!J1(x1) ! 
! 
"1(x1) , $J2$2 = sup 
x2!X2 
! 
!J2(x2) ! 
! 
"2(x2) , (5.26) 
† For example, our algorithm can be used for the asynchronous distributed computation of fixed points of concave operators, arising in fields like economics 
and polulation dynamics. The key fact here is that a concave function can be 
described as the minimum of a collection of linear functions through the classical conjugacy operation.
352 Sequential Zero-Sum Games and Minimax Control Chap. 5 
x1 x2 2 x1 x2 
u v u v 
u v Stage for Minimizer Stage for Maximizer 
Stage for Minimizer Stage for Maximizer 
Min-max value J! 
1 (x1) Max-min value 
) Max-min value J! 
2 (x2) 
Figure 5.3.1 Schematic illustration of the sequence of events at each stage of the minimax problem. We start at x1 ! X1. The minimizer chooses a control u ! U(x1), a new state x2 ! X2 is generated, the maximizer chooses a v ! V (x2), and a new state x1 ! X1 is generated, etc. If the stage begins at x2 rather than x1, this corresponds to the max-min problem. The corresponding min-max and max-min values are J# 
1 (x1) and J# 2 (x2), respectively. 
where "1 and "2 are positive weighting functions, respectively. We also consider the space B(X1)'B(X2) with the norm 
. 
.(J1, J2) . 
. = max + 
$J1$1, $J2$2 , 
. (5.27) 
We will be interested in finding a pair of functions (J* 1 , J 
* 2 ) that are 
the fixed point of mappings 
H1 : X1 ' U 'B(X2) !" B(X1), H2 : X2 ' V 'B(X1) !" B(X2), 
in the following sense: for all x1 # X1 and x2 # X2, 
J* 1 (x1) = inf 
u!U(x1) H1(x1, u, J* 
2 ), J* 2 (x2) = sup 
v!V (x2) H2(x2, v, J* 
1 ). 
(5.28) These two equations form an abstract version of Bellman’s equation for the infinite horizon sequential min-max problem described by the sequence of events (1)-(4) given earlier. We will assume later (see Section 5.4) that H1 and H2 have a contraction property like Assumption 5.1.1, which will guarantee that (J* 
1 , J * 2 ) is the unique fixed point within B(X1)'B(X2). 
Note that the fixed point problem (5.28) involves both min-max and max-min values, without assuming that they are equal. By contrast the algorithms of Section 5.2 aim to compute only the min-max value. In the case of a Markov game (cf. Examples 5.1.1 and 5.1.2), the min-max value is equal to the max-min value, but in general min-max may not be equal to max-min, and the algorithms of Section 5.2 will only find minmax explicitly. We will next provide an example to interpret J* 
1 and J* 2 as 
the min-max and max-min value functions of a sequential infinite horizon problem involving the sequence of events (1)-(4) given earlier.
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 353 
Example 5.3.1 (Discounted Minimax Control - Explicit Separation of the Two Players) 
In this formulation of a discounted minimax control problem, the states of the minimizer and the maximizer, respectively, at time k are denoted by x1,k ! X1 and x2,k ! X2, and they evolve according to 
x2,k+1 = f1(x1,k, uk), x1,k+1 = f2(x2,k+1, vk), k = 0, 1, . . . . (5.29) 
The mappings H1 and H2 are given by 
H1(x1, u, J2) = g1(x1, u) + !J2 
" 
f1(x1, u) # 
, (5.30) 
H2(x2, v, J1) = g2(x2, v) + !J1 
" 
f2(x2, v) # 
, (5.31) 
where g1 and g2 are stage cost functions for the minimizer and the maximizer, respectively. The corresponding fixed point problem of Eq. (5.28) has the form 
J# 
1 (x1) = inf u"U(x1) 
/ 
g1(x1, u) + !J# 
2 
" 
f1(x1, u) # 
0 
, (5.32) 
J# 
2 (x2) = sup v"V (x2) 
/ 
g2(x2, v) + !J# 
1 
" 
f2(x2, v) # 
0 
. (5.33) 
Example 5.3.2 (Markov Games) 
We will show that the discounted Markov game of Example 5.1.1 can be reformulated within our fixed point framework of Eq. (5.28) by letting X1 = X, X2 = X"U , and by redefining the minimizer’s control to be a probability distribution (u1, . . . , un), and the maximizer’s control to be one of the m possible choices j = 1, . . . ,m. 
To introduce into our problem formulation an appropriate contraction structure that we will need in the next section, we use a scaling parameter $ such that 
$ > 1, !$ < 1. (5.34) 
The idea behind the use of the scaling parameter $ is to introduce discounting into the stages of both the minimizer and the maximizer. We consider functions J# 
1 (x) and J# 2 (x, u) that solve the equations 
J# 
1 (x) = 1 $ min u"U 
J# 
2 (x, u), (5.35) 
J# 
2 (x, u) = max 
1 
u! 
& 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y) 
' 
(1), . . . , 
u! 
& 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y) 
' 
(m) 
2 
, 
(5.36)
354 Sequential Zero-Sum Games and Minimax Control Chap. 5 
where & 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y) 
' 
(j), j = 1, . . . ,m, (5.37) 
denotes the jth column of the matrix 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y). (5.38) 
It can be seen from these equations that 
J# 
2 (x, u) = max v"V 
u! 
& 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y) 
' 
v, (5.39) 
since the maximization over v ! V above is equivalent to the maximization over the m alternatives in Eq. (5.36), which correspond to the extreme points of the unit simplex V . Thus from Eqs. (5.35) and (5.39), it follows that the function $J# 
1 satisfies 
($J# 
1 )(x) = min u"U 
max v"V 
u! 
& 
A(x) + ! % 
y"X 
Qxy($J # 
1 )(y) 
' 
v, 
so it coincides with the vector of equilibrium values J# of the Markov game formulation of Example 5.1.1 [cf. Eq. (5.7)-(5.8)]. 
Note that J# 2 (x, ·) is a piecewise linear function of u with at most m 
pieces, defined by the columns (5.37). Thus the fixed point (J# 1 , J 
# 2 ) can be 
stored and be computed as a finite set of numbers: the real numbers J# 1 (x), 
x ! X, which can also be used to compute the n"m matrices 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y), x ! X, 
whose columns define J# 2 (x, u), cf. Eq. (5.36). 
We finally observe that the two equations (5.35) and (5.39) can be written in the form (5.28), with x1 = x, x2 = (x, u), and H1, H2 defined by 
H1(x, u, J2) = 1 $ J2(x, u), 
H2(x, u, v, J1) = u! 
& 
A(x) + !$ % 
y"X 
QxyJ # 
1 (y) 
' 
v. 
An important area of application of our two-player framework is control under set-membership uncertainty within a game-against-nature formulation, whereby nature is modeled as an antagonistic opponent choosing v # V (x2). Here only the min-max value is of practical interest, but our subsequent PI methodology will find the max-min value as well. We provide two examples of this type of formulation.
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 355 
Example 5.3.3 (Discounted Minimax Control Over an Infinite Horizon) 
Consider a dynamic system whose state evolves at each time k according to a discrete time equation of the form 
xk+1 = f(xk, uk, vk), k = 0, 1, . . . , (5.40) 
where xk is the state, uk is the control to be selected from some given set U(xk) (with perfect knowledge of xk), and vk is a disturbance that is selected by an antagonistic nature from a set V (xk, uk) [with perfect knowledge of (xk, uk)]. A cost g(xk, uk, vk) is incurred at time k, it is accumulated over an infinite horizon, and it is discounted by ! ! (0, 1). The Bellman equation for this problem is 
J#(x) = inf u"U(x) 
sup v"V (x,u) 
/ 
g(x, u, v) + !J# " 
f(x, u, v) # 
0 
, (5.41) 
and the optimal cost function J# is the unique fixed point of this equation, assuming that the cost per stage g is a bounded function. 
To reformulate this problem into the fixed point format (5.28), we identify the minimizer’s state x1 with the state x of the system (5.40), and the maximizer’s state x2 with the state-control pair (x, u). We also introduce a scaling parameter $ that satisfies $ > 1 and !$ < 1; cf. Eq. (5.34). We define H1 and H2 as follows: 
H1(x, u, J2) maps (x, u, J2) to the real value 1 $ J2(x, u), 
H2(x, u, v, J1) maps (x, u, v, J1) 
to the real value g(x, u, v) + !$J1 
" 
f(x, u, v) # 
. 
Then the resulting fixed point problem (5.28) takes the form 
($J# 
1 )(x) = inf u"U(x) 
J# 
2 (x, u), 
J# 
2 (x, u) = sup v"V (x,u) 
/ 
g(x, u, v) + !($J# 
1 ) " 
f(x, u, v) # 
0 
, 
which is equivalent to the Bellman equation (5.41) with J# = $J# 1 . 
Example 5.3.4 (Discounted Minimax Control with Partially Stochastic Disturbances) 
Consider a dynamic system such as the one of Eq. (5.40) in the preceding example, except that there is an additional stochastic disturbance w with
356 Sequential Zero-Sum Games and Minimax Control Chap. 5 
known conditional probability distribution given (x, u, v). Thus the state evolves at each time k according to 
xk+1 = f(xk, uk, vk, wk), k = 0, 1, . . . , (5.42) 
and the cost per stage is g(xk, uk, vk, wk). The Bellman equation now is 
J#(x) = inf u"U(x) 
sup v"V (x,u) 
Ew 
* 
g(x, u, v, w) + !J# " 
f(x, u, v, w) # ! 
! x, u, v -
, (5.43) 
and J# is the unique fixed point of this equation, assuming that g is a bounded function. 
Similar to Example 5.3.3, we let the minimizer’s state be x, and the maximizer’s state be (x, u), we introduce a scaling parameter $ that satisfies $ > 1 and !$ < 1; cf. Eq. (5.34), and we define H1 and H2 as follows: 
H1(x, u, J2) maps (x, u, J2) to the real value 1 $ J2(x, u), 
H2(x, u,v, J1) maps (x, u, v, J1) 
to the real value Ew 
* 
g(x, u, v, w) + !$J1 
" 
f(x, u, v, w) # ! 
! x, u, v -
. 
The resulting fixed point problem (5.28) takes the form 
($J# 
1 )(x) = inf u"U(x) 
J# 
2 (x, u), 
J# 
2 (x, u) = sup v"V (x,u) 
Ew 
* 
g(x, u, v, w) + !($J# 
1 ) " 
f(x, u, v, w) # ! 
! x, u, v -
. 
which is equivalent to the Bellman equation (5.43) with J# = $J# 1 . 
Other examples of application of our abstract fixed point framework (5.28) include two-player versions of multiplicative and exponential cost problems. One-player cases of these problems have a long tradition in DP; see e.g., Jacobson [Jac73], Denardo and Rothblum [DeR79], Whit-tle [Whi81], Rothblum [Rot84], Patek [Pat01]. Abstract versions of these problems come under the general framework of a!ne monotonic problems , for which we refer to Section 3.5.2 and the author’s paper [Ber19a] for further discussion. Two-player versions of a!ne monotonic problems involve a state space X = {1, . . . , n}, and the mapping 
H(x, u, v, J) = g(x, u, v) + n % 
y=1 
Axy(u, v)J(y), x = 1, . . . , n, 
where g and Axy satisfy for all x, y = 1, . . . , n, u # U(x), v # V (x), 
g(x, u, v) ( 0, Axy(u, v) ( 0. 
Our PI algorithms can be suitably adapted to address these problems, along the lines of the preceding examples. Of course, the corresponding convergence analysis may pose special challenges, depending on whether our assumptions of the next section are satisfied.
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 357 
“Naive” PI Algorithms 
A PI algorithm for the fixed point problem (5.28), which is patterned after the Pollatschek and Avi-Itzhak algorithm, generates a sequence of policy pairs {µt, !t} ) M'N and corresponding sequence of cost function pairs {J1,µt,!t , J2,µt,!t} ) B(X1)'B(X2). We use the term “naive” to indicate that the algorithm does not address adequately the convergence issue of the underlying Newton’s method.† Given {µt, !t} it generates {µt+1, !t+1} with a two-step process as follows: 
(a) Policy evaluation, which computes the functions {J1,µt,!t,Jt 2 , J2,µt,!t} 
by solving the fixed point equations 
J1,µt,!t(x1) = H1 " 
x1, µt(x), J2,µt,!t # 
, x1 # X1, (5.44) 
J2,µt,!t(x2) = H2 " 
x2, !t(x), J1,µt,!t # 
, x2 # X2. (5.45) 
(b) Policy improvement, which computes (µt+1, !t+1) with the minimizations 
µt+1(x1) # arg min u!U(x1) 
H1 
" 
x1, u, J2,µt,!t # 
, x1 # X1, (5.46) 
!t+1(x2) # arg max v!V (x2) 
H2 " 
x2, v, J1,µt,!t # 
, x2 # X2. (5.47) 
This algorithm resembles the abstract version of the Pollatschek and Avi-Itzhak algorithm (5.24)-(5.25) in that it involves simple policy evaluations, which do not require the solution of a multistage DP problem for either the minimizer or the maximizer. Unfortunately, however, the algorithm (5.44)-(5.47) cannot be proved to be convergent, as it does not deal e"ectively with the oscillatory behavior illustrated in Fig. 5.2.1. 
An optimistic version of the PI algorithm (5.44)-(5.47) evaluates the fixed point pair (J1,µt,!t , J2,µt,!t) approximately, by using some number, say k̄ ( 1, of value iterations. It has the form 
J1,k+1(x1) = H1 " 
x1, µt(x1), J2,k # 
, x1 # X1, k = 0, 1, . . . , k̄ % 1, (5.48) 
J2,k+1(x2) = H2 
" 
x2, !t(x2), J1,k # 
, x2 # X2, k = 0, 1, . . . , k̄ % 1, (5.49) 
starting from an initial approximation (J1,0, J2,0), instead of solving the fixed point equations (5.44)-(5.45). As k̄ (i.e., the number of value iterations used for policy evaluation) increases, the pair (J1,k̄, J2,k̄) converges to 
† We do not mean the term in a pejorative sense. In fact the Pollatschek and 
Avi-Itzhak paper [PoA69] embodies original ideas, includes sophisticated and insightful analysis, and has stimulated considerable followup work.
358 Sequential Zero-Sum Games and Minimax Control Chap. 5 
(J1,µt,!t , J2,µt,!t), and the optimistic and nonoptimistic policy evaluations coincide in the limit (under suitable contraction assumptions to be introduced in the next section). Still the PI algorithm that uses this optimistic policy evaluation, followed by a policy improvement operation similar to Eqs. (5.46)-(5.47), i.e., 
µt+1(x1) # arg min u!U(x1) 
H1 " 
x1, u, J2,k̄+1 
# 
, x1 # X1, (5.50) 
!t+1(x2) # arg max v!V (x2) 
H2 " 
x2, v, J1,k̄+1 
# 
, x2 # X2, (5.51) 
cannot be proved convergent and is subject to oscillatory behavior. How-ever, this optimistic algorithm can be made convergent through modifications that we describe next. 
Our Distributed Optimistic Abstract PI Algorithm 
Our PI algorithm for finding the solution (J* 1 , J 
* 2 ) of the Bellman equation 
(5.28) has structural similarity with the “naive” PI algorithm that uses optimistic policy evaluations of the form (5.48)-(5.49) and policy improvements of the form (5.50)-(5.51). It di"ers from the PI algorithms of the preceding section, such as the Ho"man-Karp and van der Wal algorithms, in two ways: 
(a) It treats symmetrically the minimizer and the maximizer , in that it aims to find both the min-max and the max-min cost functions, which are J* 
1 and J* 2 , respectively, and it ignores the possibility that we may 
have J* 1 = J* 
2 . 
(b) It separates the policy evaluations and policy improvements of the minimizer and the maximizer, in asynchronous fashion. In particular, in the algorithm that we will present shortly, each iteration will consist of only one of four operations: (1) an approximate policy evaluation (consisting of a single value iteration) by the minimizer, (2) a policy improvement by the minimizer, (3) an approximate policy evaluation (consisting of a single value iteration) by the maximizer, (4) a policy improvement by the maximizer. 
The order and frequency by which these four operations are performed does not a"ect the convergence of the algorithm, as long as all of these operations are performed infinitely often. Thus the algorithm is well suited for distributed implementation. Moreover, by executing the policy evaluation steps (1) and (3) much more frequently than the policy improvement operations (2) and (4), we obtain an algorithm involving nearly exact policy evaluation. 
Our algorithm generates two sequences of function pairs, 
{J t 1, J 
t 2} ) B(X1)'B(X2), {V t 
1 , V t 2 } ) B(X1)'B(X2),
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 359 
and a sequence of policy pairs: 
{µt, !t} ) M 'N . 
The algorithm involves pointwise minimization and maximization operations on pairs of functions, which we treat notationally as follows: For any pair of functions (V, J) from within B(X1) or B(X2), we denote by min[V, J ] and by max[V, J ] the functions defined on B(X1) or B(X2), respectively, that take values 
min[V, J ](x) = min + 
V (x), J(x) , 
, max[V, J ](x) = max + 
V (x), J(x) , 
, 
for every x in X1 or X2, respectively. At iteration t, our algorithm starts with 
J t 1, V 
t 1 , J 
t 2, V 
t 2 , µ 
t, !t, 
and generates J t+1 1 , V t+1 
1 , J t+1 2 , V t+1 
2 , µt+1, !t+1, 
by executing one of the following four operations.† 
Iteration (t+ 1) of Distributed Optimistic Abstract PI Algo-rithm 
Given (J t 1, V 
t 1 , J 
t 2, V 
t 2 , µ 
t, !t), do one of the following four operations (a)-(d): 
(a) Single value iteration for policy evaluation of the minimizer: For all x1 # X1, set 
J t+1 1 (x1) = H1 
" 
x1, µt(x1),max[V t 2 , J 
t 2] # 
, (5.52) 
and leave J t 2, V 
t 1 , V 
t 2 , µ 
t, !t unchanged, i.e., the corresponding (t + 1)-iterates are set to the t-iterates: J t+1 
2 = J t 2, V 
t+1 1 = V t 
1 , V t+1 2 = V t 
2 , µt+1 = µt, !t+1 = !t. 
† The choice of operation is arbitrary at iteration t, as long as each type of 
operation is executed for infinitely many t. It can be extended by introducing “communication delays,” and state space partitioning, whereby the operations 
are carried out in just a subset of the corresponding state space. This is a type of asynchronous operation that was also used in the earlier works [BeY10], [BeY12], 
[YuB13a]. It is supported by an asynchronous convergence analysis originated 
in the author’s papers [Ber82], [Ber83]; see also Section 2.6.1 of the present book, the book [BeT89], and the book [Ber12a], Section 2.6. This asynchronous 
convergence analysis applies because the mapping underlying our algorithm is a 
contraction with respect to a sup-norm (rather than some other norm such as an L2 norm).
360 Sequential Zero-Sum Games and Minimax Control Chap. 5 
(b) Policy improvement for the minimizer: For all x1 # X1, set 
J t+1 1 (x1) = V t+1 
1 (x1) = min u!U(x1) 
H1 
" 
x1, u,max[V t 2 , J 
t 2] # 
, (5.53) 
set µt+1(x1) to a control u # U(x1) that attains the above minimum, and leave J t 
2, V t 2 , ! 
t unchanged. 
(c) Single value iteration for policy evaluation of the maximizer: For all x2 # X2, set 
J t+1 2 (x2) = H2 
" 
x2, !t(x2),min[V t 1 , J 
t 1] # 
, (5.54) 
and leave J t 1, V 
t 1 , V 
t 2 , µ 
t, !t unchanged. 
(d) Policy improvement for the maximizer: For all x2 # X2, set 
J t+1 2 (x2) = V t+1 
2 (x2) = max v!V (x2) 
H2 " 
x2, v,min[V t 1 , J 
t 1] # 
, (5.55) 
set !t+1(x2) to a control v # V (x2) that attains the above maximum, and leave J t 
1, V t 1 , µ 
t unchanged. 
Example 5.3.5 (Our PI Algorithm for Minimax Control -Explicit Separation of the Players) 
Consider the minimax control problem with explicit separation of the two players of Example 5.3.1, which involves the dynamic system x1,k ! X1 and x2,k ! X2, and they evolve according to 
x2,k+1 = f1(x1,k, uk), x1,k+1 = f2(x2,k+1, vk), k = 0, 1, . . . , 
[cf. Eq. (5.29)]. The Bellman equation for this problem can be broken down into the two equations (5.32), (5.33): 
J# 
1 (x1) = inf u"U(x1) 
/ 
g1(x1, u) + !J# 
2 
" 
f1(x1, u) # 
0 
, 
J# 
2 (x2) = sup v"V (x2) 
/ 
g2(x2, v) + !J# 
1 
" 
f2(x2, v) # 
0 
. 
In the context of this problem, the four operations (5.52)-(5.55) of our PI algorithm take the following form:
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 361 
(a) Single value iteration for policy evaluation for the minimizer: For all x1 ! X1, set 
Jt+1 1 (x1) = g1 
" 
x1, µ t(x1) 
# 
+!max / 
V t 2 
" 
f1(x1, µ t(x1)) 
# 
, Jt 2 
" 
f1(x1, µ t(x1)) 
# 
0 
, 
(5.56) and leave Jt 
2, V t 1 , V 
t 2 , µ 
t, %t unchanged. 
(b) Policy improvement for the minimizer: For all x1 ! X1, set 
Jt+1 1 (x1) = V t+1 
1 (x1) = min u"U(x1) 
/ 
g1(x1, u) 
+ !max 3 
V t 2 
" 
f1(x1, u) # 
, Jt 2 
" 
f1(x1, u) #4 
0 
, 
(5.57) set µt+1(x1) to a control u ! U(x1) that attains the above minimum, and leave Jt 
2, V t 2 , % 
t unchanged. 
(c) Single value iteration for policy evaluation of the maximizer: For all x2 ! X2 and v ! V (x2), set 
Jt+1 2 (x2) = g2 
" 
x2, % t(x2) 
# 
+!min / 
V t 1 
" 
f2(x2, % t(x2)) 
# 
, Jt 1 
" 
f2(x2, % t(x2)) 
# 
0 
, 
(5.58) and leave Jt 
1, V t 1 , V 
t 2 , µ 
t, %t unchanged. 
(d) Policy improvement for the maximizer: For all x2 ! X2, set 
Jt+1 2 (x2) = V t+1 
2 (x2) = max v"V (x2) 
/ 
g2(x2, v) 
+ !min 3 
V t 1 
" 
f2(x2, v) # 
, Jt 1 
" 
f2(x2, v) #4 
0 
, 
(5.59) set %t+1(x2) to a control u ! V (x2) that attains the above maximum, and leave Jt 
1, V t 1 , µ 
t unchanged. 
Example 5.3.6 (Our PI Algorithm for Markov Games) 
Let us consider the Markov game formulation of Example 5.3.2. Our PI algorithm with x1, x2, H1, and H2 defined earlier, can be implemented by storing Jt 
1, V t 1 as the real numbers Jt 
1(x) and V t 1 (x), x ! X, and by storing 
and representing the piecewise linear functions Jt 2, V 
t 2 using the m columns of 
the n"m matrices 
A(x) + !$ % 
y"X 
Qxy min 3 
V t 1 (y), J 
t 1(y) 
4 
, x ! X; (5.60) 
cf. Eq. (5.36). None of the operations (5.52)-(5.55) require the solution of a Markovian decision problem as in the Ho!man-Karp algorithm. This is similar to the Pollatschek and Avi-Itzhak algorithm.
362 Sequential Zero-Sum Games and Minimax Control Chap. 5 
More specifically, the policy evaluation (5.52) for the minimizer takes the form 
Jt+1 1 (x) = 
1 $ max 
/ 
V t+1 2 
" 
x, µt(x) # 
, Jt+1 2 
" 
x,µt(x) # 
0 
, for all x ! X, (5.61) 
while the policy improvement (5.53) for the minimizer takes the form 
Jt+1 1 (x) = V t+1 
1 (x) = 1 $ min u"U 
max 3 
V t+1 2 (x, u), Jt+1 
2 (x, u) 4 
, for all x ! X. 
(5.62) The policy evaluation (5.54) for the maximizer takes the form 
Jt+1 2 (x, u) = u! 
& 
A(x) + !$ % 
y"X 
Qxy min 3 
V t 1 (y), J 
t 1(y) 
4 
' 
" 
%t(x) # 
, (5.63) 
for all x ! X and u ! U , while the policy improvement (5.55) for the maximizer takes the form 
Jt+1 2 (x, u) = V t+1 
2 (x, u) 
= max 
1 
u! 
& 
A(x) + !$ % 
y"X 
Qxy min 3 
V t 1 (y), J 
t 1(y) 
4 
' 
(1), . . . , 
u! 
& 
A(x) + !$ % 
y"X 
Qxy min 3 
V t 1 (y), J 
t 1(y) 
4 
' 
(m) 
2 
, 
(5.64) for all x ! X and u ! U , where 
& 
A(x) + !$ % 
y"X 
Qxy min 3 
V t 1 (y), J 
t 1(y) 
4 
' 
(j) 
is the jth column of the n"m matrix (5.60). Again it can be seen that except for the extra memory storage to main-
tain V t 1 and V t 
2 , the preceding PI algorithm (5.61)-(5.64) requires roughly similar/comparable computations to the ones of the “naive” optimistic PI algorithm (5.48)-(5.51), when applied to the Markov game model. 
Discussion of our Algorithm 
Let us now provide a discussion of some of the properties of our PI algorithm (5.52)-(5.55). We first note that except for the extra memory storage to maintain V t 
1 and V t 2 , the algorithm requires roughly similar/comparable 
computations to the ones of the “naive” optimistic PI algorithm (5.48)-(5.51). Note also that by performing a large number of value iterations of the form (5.52) or (5.54) we obtain an algorithm that involves nearly
Sec. 5.3 A New PI Algorithm for Abstract Minimax DP problems 363 
exact policy evaluation, similar to the “naive” nonoptimistic PI algorithm (5.44)-(5.47). 
Mathematically, under the contraction assumption to be introduced in the next section, our algorithm (5.52)-(5.55) avoids the oscillatory behavior illustrated in Fig. 5.2.1because it embodies a policy-dependent sup-norm contraction, which has a uniform fixed point , the pair (J* 
1 , J * 2 ), regardless 
of the policies. This is the essence of the key Prop. 5.4.2, which will be shown in the next section. 
Aside from this mathematical insight, one may gain intuition into the mechanism of our algorithm (5.52)-(5.55), by comparing it with the optimistic version of the “naive” optimistic PI algorithm (5.48)-(5.51). Our algorithm (5.52)-(5.55) involves additionally the functions V t 
1 and V t 2 , which 
are changed only during the policy improvement operations, and tend to provide a guarantee against oscillatory behavior. In particular, since 
max[V t 2 , J 
t 2] ( J t 
2, 
the iterations of the minimizer in our algorithm, (5.52) and (5.53), are more “pessimistic” about the choices of the maximizer than the iterates of the minimizer in the “naive” PI iterates (5.48) and (5.49). Similarly, since 
min[V t 1 , J 
t 1] & J t 
1, 
the iterations of the maximizer in our algorithm, (5.54) and (5.55), are more “pessimistic” than the iterates of the maximizer in the naive PI iterates (5.48) and (5.49). As a result the use of V t 
1 and V t 2 in our PI algorithm 
makes it more conservative, and mitigates the oscillatory swings that are illustrated in Fig. 5.2.1. 
Let us also note that the use of the functions V1 and V2 in our algorithm (5.52)-(5.55) may slow down the algorithmic progress relative to the (nonconvergent) “naive” algorithm (5.44)-(5.47). To remedy this situation an interpolation device has been suggested in the paper [BeY10] (Section V), which roughly speaking interpolates between the two algorithms, while still guaranteeing the algorithm’s convergence; see also Sec-tion 2.6.3. Basically, such a device makes the algorithm less “pessimistic,” as it guards against nonconvergence, and it can similarly be used in our algorithm (5.52)-(5.55). 
In the next section, we will show convergence of our PI algorithm (5.52)-(5.55) with a line of proof that can be summarized as follows. Using a contraction argument, based on an assumption to be introduced shortly, we show that the sequences {V t 
1 } and {V t 2 } converge to some functions 
V # 1 # B(X1) and V # 
2 # B(X2), respectively. From the policy improvement operations (5.53) and (5.55) it will then follow that the sequences {J t 
1} and {J t 
2} converge to the same functions V # 1 and V # 
2 , respectively, so that min[V t 
1 , J t 1] and max[V t 
2 , J t 2] converge to V # 
1 and V # 2 , respectively, as well.
364 Sequential Zero-Sum Games and Minimax Control Chap. 5 
Using the continuity of H1 and H2 (a consequence of our contraction assumption), it follows from Eqs. (5.53) and (5.55) that (V # 
1 , V # 2 ) is the fixed 
point of H1 and H2 [in the sense of Eq. (5.28)], and hence is also equal to (J* 
1 , J * 2 ) [cf. Eq. (5.28)]. Thus we finally obtain convergence: 
V t 1 " J* 
1 , J t 1 " J* 
1 , V t 2 " J* 
2 , J t 2 " J* 
2 . 
5.4 CONVERGENCE ANALYSIS 
For each µ # M, we consider the operator T1,µ that maps a function J2 # B(X2) into the function of x1 given by 
(T1,µJ2)(x1) = H1 " 
x1, µ(x1), J2 # 
, x1 # X1. (5.65) 
Also for each ! # N , we consider the operator T2,! that maps a function J1 # B(X1) into the function of x2 given by 
(T2,!J1)(x2) = H2 " 
x2, !(x2), J1 # 
, x2 # X2. (5.66) 
We will also consider the operator Tµ,! that maps a function (J1, J2) # B(X1)'B(X2) into the function of (x1, x2) # X1 'X2, given by 
" 
Tµ,!(J1, J2) # 
(x1, x2) = " 
(T1,µJ2)(x1), (T1,!J1)(x2) # 
. (5.67) 
[Recall here that the norms on B(X1), B(X2), and B(X1) ' B(X2) are given by Eqs. (5.26) and (5.27).] 
We will show convergence of our algorithm assuming the following. 
Assumption 5.4.1: (Contraction Assumption) Consider the operator Tµ,! given by Eq. (5.67). 
(a) For all (µ, !) # M ' N , and (J1, J2) # B(X1) ' B(X2), the function Tµ,!(J1, J2) belongs to B(X1)'B(X2). 
(b) There exists an # # (0, 1) such that for all (µ, !) # M'N , Tµ,! 
is a contraction mapping of modulus # within B(X1)'B(X2). 
By writing the contraction property as 
max + 
$T1,µJ2 % T1,µJ " 2$1, $T2,!J1 % T2,!J " 
1$2 , 
& #max + 
$J1 % J " 1$1, $J2 % J " 
2$2 , 
, (5.68) 
for all J1, J " 1 # B(X1) and J2, J " 
2 # B(X2) [cf. the norm definition (5.27)], we have 
$T1,µJ2 % T1,µJ " 2$1 & #$J2 % J " 
2$2, for all J2, J " 2 # B(X2), (5.69)
Sec. 5.4 Convergence Analysis 365 
and 
$T2,!J1 % T2,!J " 1$2 & #$J1 % J " 
1$1, for all J1, J " 1 # B(X1); (5.70) 
[set J1 = J " 1 or J2 = J " 
2, respectively, in Eq. (5.68)]. From these relations, we obtain† 
$T1J2 % T1J " 2$1 & #$J2 % J " 
2$2, for all J2, J " 2 # B(X2), (5.71) 
and 
$T2J1 % T2J " 1$2 & #$J1 % J " 
1$1, for all J1, J " 1 # B(X1), (5.72) 
where 
(T1J2)(x1) = inf µ!M 
(T1,µJ2)(x1) = inf u!U(x1) 
H1(x1, u, J2), x1 # X1, 
(T2J1)(x2) = sup !!N 
(T2,!J1)(x2) = sup v!V (x2) 
H2(x2, v, J1), x2 # X2. 
The relations (5.71)-(5.72) also imply that the operator 
T : B(X1)'B(X2) !" B(X1)'B(X2), 
defined by T (J1, J2) = (T1J2, T2J1), (5.73) 
is a contraction mapping from B(X1) ' B(X2) to B(X1) ' B(X2) with modulus #. It follows that T has a unique fixed point (J* 
1 , J * 2 ) # B(X1)' 
B(X2). We will show that our algorithm yields in the limit this fixed point. 
† For a proof, we write Eq. (5.69) as 
(T1,µJ2)(x1) & (T1,µJ ! 
2)(x1) + !%J2 $ J ! 
2%2 "1(x1), 
(T2,µJ2)(x1) & (T2,µJ ! 
2)(x1) + !%J2 $ J ! 
2%2 "1(x1), 
for all x1 ! X1. By taking infimum of both sides over µ ! M, we obtain 
! 
!(T1J2)(x1)$ T1J ! 2)(x1) 
! 
! 
"1(x1) & !%J2 $ J ! 
2%2, 
and by taking supremum over x1 ! X1, the desired relation 
%T1J2 $ T1J ! 
2%1 & !%J2 $ J ! 
2%2 
follows. The proof of the other relation, %T2J1$T2J ! 1%2 & !%J1$J ! 
1%1, is similar.
366 Sequential Zero-Sum Games and Minimax Control Chap. 5 
The following is our main convergence result [convergence here is meant in the sense of the norm (5.27) on B(X1)'B(X2)]. Note that this result applies to any order and frequency of policy evaluations and policy improvements of the two players. 
Proposition 5.4.1: (Convergence) Let Assumption 5.4.1 hold, and assume that each of the four operations of the PI algorithm (5.52)-(5.55) is performed infinitely often. Then the sequences 
+ 
(J t 1, J 
t 2) , 
and + 
(V t 1 , V 
t 2 ) , 
generated by the algorithm converge to (J* 1 , J 
* 2 ). 
The proof is long but follows closely the steps of the proof for the single-player abstract DP case in Section 2.6.3. 
An Extended Algorithm and its Convergence Proof 
We first show the following lemma. 
Lemma 5.4.1: For all (V1, V2), (J1, J2), (V " 1 , V 
" 2), (J 
" 1, J 
" 2) # B(X1) ' 
B(X2), we have 
. 
.min[V1, J1]%min[V " 1 , J 
" 1] . 
. 
1 & max 
+ 
$V1%V " 1$1, $J1%J " 
1$1 , 
, (5.74) 
. 
.max[V2, J2]%min[V " 2 , J 
" 2] . 
. 
2 & max 
+ 
$V2%V " 2$2, $J2%J " 
2$2 , 
. (5.75) 
Proof: For every x1 # X1, we write 
V1(x1) 
"1(x1) & 
V " 1(x1) 
"1(x1) + max 
+ 
$V1 % V " 1$1, $J1 % J " 
1$1 , 
, 
J1(x1) 
"1(x1) & 
J " 1(x1) 
"1(x1) + max 
+ 
$V1 % V " 1$1, $J1 % J " 
1$1 , 
, 
from which we obtain 
min + 
V1(x1), J1(x1) , 
"1(x1) & 
min + 
V " 1(x1), J " 
1(x1) , 
"1(x1) +max 
+ 
$V1%V " 1$1, $J1%J " 
1$1 , 
, 
so that 
min + 
V1(x1), J1(x1) , 
%min + 
V " 1(x1), J " 
1(x1) , 
"1(x1) & max 
+ 
$V1%V " 1$1, $J1%J " 
1$1 , 
.
Sec. 5.4 Convergence Analysis 367 
By exchanging the roles of (V1, J1) and (V " 1 , J 
" 1), and combining the two 
inequalities, we have ! 
! 
! min 
+ 
V1(x1), J1(x1) , 
%min + 
V " 1(x1), J " 
1(x1) , 
! 
! 
! 
"1(x1) & max 
+ 
$V1%V " 1$1, $J1%J " 
1$1 , 
, 
and by taking the supremum over x1 # X1, we obtain Eq. (5.74). We similarly prove Eq. (5.75). Q.E.D. 
We consider the spaces of bounded functions Q1(x1, u) of (x1, u) # X1 ' U and Q1(x2, v) of (x2, v) # X2 ' V , with norms 
$Q1$1 = sup x1!X1, u!U 
! 
!Q1(x1, u) ! 
! 
"1(x1) , $Q2$2 = sup 
x2!X2, v!V 
! 
!Q2(x2, v) ! 
! 
"2(x2) , 
(5.76) respectively, where "1 and "2 are the weighting functions that define the norm of B(X1) and B(X2) [cf. Eq. (5.26)]. We denote these spaces by B(X1 ' U) and B(X2 ' V ), respectively. Functions in these spaces have the meaning of Q-factors for the minimizer and the maximizer . 
We next introduce a new operator, denoted byGµ,! , which is parametrized by the policy pair (µ, !), and will be shown to have a common fixed point for all (µ, !) # M'N , from which (J* 
1 , J * 2 ) can be readily obtained. 
The operator Gµ,! involves operations on Q-factor pairs (Q1, Q2) for the minimizer and the maximizer, in addition to functions of state (V1, V2), and is used define an “extended” PI algorithm that operates over a larger function space than the one of Section 5.3. Once the convergence of this “extended” PI algorithm is shown, the convergence of our algorithm of Section 5.3 will readily follow. 
To define the operator Gµ,! , we note that it consists of four components, maps B(X1) ' B(X2) ' B(X1 ' U) ' B(X2 ' V ) into itself. It is given by 
Gµ,!(V1, V2, Q1, Q2) = " 
M1,!(V2, Q2),M2,µ(V1, Q1), 
F1,!(V2, Q2), F2,µ(V1, Q1) # 
, (5.77) 
with the functionsM1,!(V2, Q2),M2,µ(V1, Q1), F1,!(V2, Q2), F2,µ(V1, Q1), defined as follows: 
 M1,!(V2, Q2): This is the function of x1 given by 
" 
M1,!(V2, Q2) # 
(x1) = " 
T1 max[V2, Q̂2,! ] # 
(x1) 
= inf u!U(x1) 
H1 " 
x1, u,max[V2, Q̂2,! ] # 
, (5.78) 
where Q̂2,! is the function of x2 given by 
Q̂2,!(x2) = Q2 " 
x2, !(x2) # 
. (5.79)
368 Sequential Zero-Sum Games and Minimax Control Chap. 5 
 M2,µ(V1, Q1): This is the function of x2 given by 
" 
M2,µ(V1, Q1) # 
(x2) = " 
T2 min[V1, Q̂1,µ] # 
(x2) 
= sup v!V (x2) 
H2 " 
x2, v,min[V1, Q̂1,µ] # 
, (5.80) 
where Q̂1,µ is the function of x1 given by 
Q̂1,µ(x1) = Q1 " 
x1, µ(x1) # 
. (5.81) 
 F1,!(V2, Q2): This is the function of (x1, u), given by 
F1,!(V2, Q2)(x1, u) = H1 " 
x1, u,max[V2, Q̂2,! ] # 
. (5.82) 
 F2,µ(V1, Q1): This is the function of (x2, v), given by 
F2,µ(V1, Q1)(x2, v) = H2 " 
x2, v,min[V1, Q̂1,µ] # 
. (5.83) 
Note that the four components of Gµ,! correspond to the four operations of our algorithm (5.52)-(5.55). In particular, 
 M1,!(V2, Q2) corresponds to policy improvement of the minimizer. 
 M2,µ(V1, Q1) corresponds to policy improvement of the maximizer. 
 F1,!(V2, Q2) corresponds to policy evaluation of the minimizer. 
 F2,µ(V1, Q1) corresponds to policy evaluation of the maximizer. 
The key step in our convergence proof is to show that Gµ,! has a contraction property with respect to the norm on B(X1)'B(X2)'B(X1' U)'B(X2 ' V ) given by 
. 
.(V1, V2, Q1, Q2) . 
. = max + 
$V1$1, $V2$2, $Q1$1, $Q2$2 , 
, (5.84) 
where $V1$1, $V2$2 are the weighted sup-norms of V1, V2, respectively, defined by Eq. (5.26), and $Q1$1, $Q2$2 are the weighted sup-norms of Q1, Q2, defined by Eq. (5.76). Moreover, the contraction property is uniform, in the sense that the fixed point of Gµ,! does not depend on (µ, !). This means that we can carry out iterations with Gµ,! , while changing µ and ! arbitrarily between iterations, and still aim at the same fixed point . We have the following proposition.
Sec. 5.4 Convergence Analysis 369 
Proposition 5.4.2: (Uniform Contraction) Let Assumption 5.4.1 hold. Then for all (µ, !) # M'N , the operator Gµ,! is a contraction mapping with modulus # with respect to the norm of Eqs. (5.84), (5.26), and (5.76). Moreover, the corresponding fixed point of Gµ,! is (J* 
1 , J * 2 , Q 
* 1, Q 
* 2) [independently of the choice of (µ, !)], where (J* 
1 , J * 2 ) 
is the fixed point of the mapping T of Eq. (5.73), and Q* 1, Q 
* 2 are the 
functions defined by 
Q* 1(x1, u) = H1(x1, u, J* 
2 ), x1 # X1, u # U(x1), (5.85) 
Q* 2(x2, v) = H2(x2, v, J* 
1 ), x2 # X2, v # V (x2). (5.86) 
Proof: We prove the contraction property of Gµ,! by breaking it down to four inequalities, which hold for all (V1, V2), (V " 
1 , V " 2) # B(X1)'B(X2) and 
(Q1, Q2), (Q" 1, Q 
" 2) # B(X1, U)'B(X2, V ). In particular, we have 
. 
.M1,!(V2, Q2)$M1,! (V ! 
2 , Q ! 
2) . 
. 
1 = . 
. 
. T1 
" 
max[V2, Q̂2,! ] # 
$ T1 
" 
max[V ! 
2 , Q̂ ! 
2,! ] # 
. 
. 
. 
1 
& ! . 
.max[V2, Q̂2,! ]2 $max[V ! 
2 , Q̂ ! 
2,! ] . 
. 
2 
& !max + 
%V2 $ V ! 
2%2, %Q̂2,! $ Q̂! 
2,!%2 , 
& !max + 
%V2 $ V ! 
2%2, %Q2 $Q! 
2%2 , 
& !max + 
%V1 $ V ! 
1%1, %Q1 $Q! 
1%1, 
%V2 $ V ! 
2%2, %Q2 $Q! 
2%2 , 
= ! . 
.(V1, V2, Q1, Q2)$ (V ! 
1 , V ! 
2 , Q ! 
1, Q ! 
2) . 
., (5.87) 
where the first equality uses the definitions of M1,!(V2, Q2), M1,!(V " 2 , Q 
" 2) 
[cf. Eqs. (5.78) and (5.80)], the first inequality follows from Eq. (5.69), the second inequality follows using Lemma 5.4.1, the third inequality follows from the definition of Q̂2,! and Q̂" 
2,! , the last inequality is trivial, and the last equality follows from the norm definition (5.84). Similarly, we prove that . 
.M2,µ(V1, Q1)%M2,µ(V " 1 , Q 
" 1) . 
. 
2 & # 
. 
.(V1, V2, Q1, Q2)% (V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
., (5.88) 
. 
.F1,!(V2, Q2)% F1,!(V " 2 , Q 
" 2) . 
. 
1 & # 
. 
.(V1, V2, Q1, Q2)% (V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
., (5.89) 
. 
.F2,µ(V1, Q1)% F2,µ(V " 1 , Q 
" 1) . 
. 
2 & # 
. 
.(V1, V2, Q1, Q2)% (V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
.. (5.90) 
From the preceding relations (5.87)-(5.90), it follows that each of the four components of the maximization that comprises the norm 
. 
.Gµ,!(V1, V2, Q1, Q2)%Gµ,!(V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
.
370 Sequential Zero-Sum Games and Minimax Control Chap. 5 
[cf. Eq. (5.77)] is less or equal to 
# . 
.(V1, V2, Q1, Q2)% (V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
.. 
Thus we have . 
.Gµ,!(V1, V2, Q1, Q2)%Gµ,!(V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
. 
& # . 
.(V1, V2, Q1, Q2)% (V " 1 , V 
" 2 , Q 
" 1, Q 
" 2) . 
., 
which shows the desired contraction property of Gµ,! . In view of the contraction property just shown, the mapping Gµ,! 
has a unique fixed point for each (µ, !) # M ' N , which we denote by (V1, V2, Q1, Q2) [with some notational abuse, we do not show the possible dependence of the fixed point on (µ, !)]. In view of Eqs. (5.77)-(5.83), this fixed point satisfies for all x1 # X1, x2 # X2, (x1, u) # X1 ' U , (x2, v) # X2 ' V , 
V1(x1) = inf u!!U(x1) 
H1 
" 
x1, u",max[V2, Q̂2,!] # 
, (5.91) 
V2(x2) = sup v!!V (x2) 
H2 " 
x2, v",min[V1, Q̂1,µ] # 
, (5.92) 
Q1(x1, u) = H1 " 
x1, u,max[V2, Q̂2,! ] # 
, Q2(x2, v) = H2 " 
x2, v,min[V1, Q̂1,µ] # 
. (5.93) 
By comparing the preceding two relations, it follows that for all x1 # X1, x2 # X2, 
V1(x1) & Q1(x1, u), for all x1, u # U(x1), 
V2(x2) ( Q2(x2, v), for all x2, v # V (x2), 
which implies that 
min[V1, Q̂1,µ] = V1, max[V2, Q̂2,!] = V2. 
Using Eqs. (5.91)-(5.92), this in turn shows that 
V1(x1) = inf u!U(x1) 
H1(x1, u, V2), V2(x2) = sup v!V (x2) 
H2(x2, v, V1). 
Thus, independently of (µ, !), (V1, V2) is the unique fixed point of the contraction mapping T of Eq. (5.73), which is (J* 
1 , J * 2 ). Moreover from Eq. 
(5.93), we have that (Q1, Q2) is precisely (Q# 1, Q 
# 2) as given by Eqs. (5.85) 
and (5.86). This shows that, independently of (µ, !), the fixed point of Gµ,! is (J* 
1 , J * 2 , Q 
# 1, Q 
# 2), and proves the desired result. Q.E.D. 
The preceding proposition implies the convergence of the “extended” algorithm, which at each iteration t applies one of the four components of
Sec. 5.5 Approximation by Aggregation 371 
Gµt,!t evaluated at the current iterate (V t 1 , V 
t 2 , Q 
t 1, Q 
t 2, µ 
t, !t), and updates this iterate accordingly. This algorithm is well-suited for the calculation of both (J* 
1 , J * 2 ) and (Q* 
1, Q * 2). However, since we are just interested to 
calculate (J* 1 , J 
* 2 ), a simpler and more e!cient algorithm is possible, which 
is in fact our PI algorithm based on the four operations (5.52)-(5.55). To this end, we observe that the algorithm that updates (V t 
1 , V t 2 , Q 
t 1, Q 
t 2, µ 
t, !t) can be operated so that it does not require the maintenance of the full Q-factor functions (Qt 
1, Q t 2). The reason is that the values Qt 
1(x1, u) and Qt 
2(x2, v) with u *= µt(x1) and v *= !t(x2), do not appear in the calculations, and hence we need only the values Q̂t 
1,µt(x1) and Q̂t 2,!t 
(x2), which we store 
in functions J t 1 and J t 
2, i.e., we set 
J t 1(x1) = Q̂t 
1,µt(x1) = Qt 1 
" 
x1, µt(x) # 
, 
J t 2(x2) = Q̂t 
2,!t (x2) = Qt 
2 
" 
x2, !t(x2) # 
. 
Once we do that, the resulting algorithm is precisely our PI algorithm (5.52)-(5.55). 
In summary, our PI algorithm that updates (V t 1 , V 
t 2 , J 
t 1, J 
t 2, µ 
t, !t) is a reduced space implementation of the asynchronous fixed point algorithm that updates (V t 
1 , V t 2 , Q 
t 1, Q 
t 2, µ 
t, !t) using the uniform contraction mapping Gµt,!t , with the identifications 
J t 1 = Q̂1,µt , J t 
2 = Q̂2,!t . 
This proves its convergence as stated in Prop. 5.4.1. 
5.5 APPROXIMATION BY AGGREGATION 
Our algorithm of Section 5.3 involves exact implementation without function approximations, and thus is not suitable for large state and control spaces. An important research direction is approximate implementations based on our PI algorithmic structure of Section 5.3, whereby we use approximation in value space with cost function approximations obtained through reinforcement learning methods. An interesting algorithmic approach is aggregation with representative states, as described in the book [Ber19b] (Section 6.1). 
In particular, let us consider the minimax formulation of Example 5.3.1 and Eqs. (5.29), (5.32), (5.33), which involves separate state spaces X1 and X2 for the minimizer and the maximizer, respectively. In the aggregation with representative states formalism, we execute our PI algorithm over reduced versions of the spaces X1 and X2. In particular, we discretize X1 and X2 by using suitable finite collections of representative
372 Sequential Zero-Sum Games and Minimax Control Chap. 5 
u v u v 
1 x2 ! X2 2 x̃2 ! X̃2 2 x1 ! X1 
) Aggregation Probabilities ) Aggregation Probabilities 
x̃1 ! X̃1 
Min-max value J̃1(x̃1) for representative states x̃1 ! X̃1 
provement Bellman Equation Value Iterations Approximation with ) Aggregation Probabilities 
) Aggregation Probabilities 
provement Bellman Equation Value Iterations Approximation with 
2 x̄1 ! X̃1 
2 Stage for the minimizer in the aggregate problem 
Figure 5.5.1 Schematic illustration of an aggregation framework that is patterned after the sequence of events of the multistage process of Fig. 5.3.1. The aggregate problem is specified by a finite subset of representative states X̃1 " X1, a finite subset of representative states X̃2 " X2, and aggregation probabilities for passing from states x2 ! X2 to representative states x̃2 ! X̃2, and for passing from states x1 ! X1 to representative states x̃1 ! X̃1. A stage starts at a representative state x̃1 ! X̃1 and ends at some other representative state x̄1 ! X̃1, by going successively through a state x2 ! X2 under the influence of the minimizer’s choice u ! U(x̃1), then to a representative state x̃2 ! X̃2 using aggregation probabilities #x2x̃2 
(i.e., the transition x2 # x̃2 takes place with probability #x2x̃2 ), then to a 
state x1 ! X1 under the influence of the maximizer’s choice v ! V (x̃2), and finally to x̄1 ! X̃1 using aggregation probabilities #x1x̄1 
(the transition x1 # x̄1 takes place with probability #x1x̄1 
). The transitions x̃1 # x2 and x̃2 # x1 produce costs g1(x̃1, u) and g2(x̃2, v), respectively [cf. Eqs. (5.30), (5.31)]. The aggregation probabilities #x2x̃2 
and #x1x̄1 can be arbitrary. However, their choice a!ects 
the min-max and max-min functions of the aggregate problem. We can solve the aggregate problem by using simulation-based versions of 
our PI algorithm (5.52)-(5.55) of Section 5.3 to obtain the min-max and maxmin functions J̃1(x̃1) and J̃2(x̃2) at all the representative states x̃1 ! X̃1 and x̃2 ! X̃2, respectively [cf. [Ber19b] (Chapter 6)]. Then, min-max and max-min function approximations are computed from 
J̃1(x1) = % 
x̃1"X̃1 
#x1x̃1 J̃1(x̃1), J̃2(x2) = 
% 
x̃2"X̃2 
#x2x̃2 J̃2(x̃2). 
Suboptimal decision choices by the minimizer and the maximizer are then obtained from the one-step lookahead optimizations 
min u"U(x1) 
H1(x1, u, J̃2), max v"V (x2) 
H2(x2, v, J̃1). 
See the book [Ber19b] (Section 6.1) and the paper [Ber18a] for a detailed accounting of the aggregation approach with representative states for single-player infinite horizon DP. 
states X̃1 ) X1 and X̃2 ) X2, and construct a lower-dimensional aggregate problem. The typical stage involves transitions between representative states, with intermediate artificial transitions x1 " x̃1 and x2 " x̃2, which involve randomization with aggregation probabilities $x1x̃1 and $x2x̃2 , respectively; see Fig. 5.5.1. 
The structure of the aggregate problem is amenable to a DP formulation, and as a result, it can be solved by using simulation-based versions
Sec. 5.6 Notes and Sources 373 
of the PI methods of Section 5.3 [we refer to the book [Ber19b] (Chapter 6) for more details]. The cost function approximations thus obtained, call them J̃1, J̃2, are used in the one-step lookahead minimization 
min u!U(x1) 
H1(x1, u, J̃2), 
to obtain a suboptimal minimizer’s policy, and in the one-step lookahead maximization 
max v!V (x2) 
H2(x2, v, J̃1), 
to obtain a suboptimal maximizer’s policy. The aggregation with representative states approach has the advan-
tage that it maintains the DP structure of the original minimax problem. This allows the use of our PI methods of Section 5.3, with convergence guaranteed by the results of Section 5.4. Another aggregation approach that can be similarly used within our context, is hard aggregation, whereby the state spaces X1 and X2 are partitioned into subsets that form aggregate states; see [Ber18a], [Ber18b], [Ber19b]. Other reinforcement learning methods, based for example on the use of neural networks, can also be used for approximate implementation of our PI algorithms. However, their convergence properties are problematic, in the absence of additional assumptions. The papers by Bertsekas and Yu ([BeY12], Sections 6 and 7), and by Yu and Bertsekas [YuB13a] (Section 4), also describe alternative simulation-based approximation possibilities that may serve as a starting point for minimax PI algorithms with function approximation. 
5.6 NOTES AND SOURCES 
In this chapter, we have discussed PI algorithms that are specifically tailored to sequential zero-sum games and minimax problems with a contractive abstract DP structure. We used as starting point the methods by Ho"man and Karp [HoK66], and by Pollatschek and Avi-Itzhak [PoA69] for discounted and terminating zero-sum Markov games. Related methods have been discussed for Markov games by van der Wal [Van78], Tolwin-ski [Tol89], Filar and Tolwinski [FiT91], Filar and Vrieze [FiV96], and for stochastic shortest games, by Patek and Bertsekas [PaB99], and Yu [Yu14]; see also Perolat et al. [PPG16], [PSP15], and the survey by Zhang, Yang, and Basar [ZYB21] for related reinforcement learning methods. Our algorithms of Section 5.3 resolve the long-standing convergence di!culties of the Pollatschek and Avi-Itzhak PI algorithm [PoA69], and allow an asynchronous implementation, whereby the policy evaluation and policy improvement operations can be done in any order and with di"erent frequencies. Moreover, our algorithms find simultaneously the min-max and
374 Sequential Zero-Sum Games and Minimax Control Chap. 5 
the max-min values, and they are suitable for Markov zero-sum game problems, as well as for minimax control problems involving set-membership uncertainty. 
While we have not addressed in detail the issue of asynchronous distributed implementation in a multiprocessor system, our algorithm admits such an implementation, as has been discussed for its single-player counterparts in the papers by Bertsekas and Yu [BeY10], [BeY12], [YuB13a], and also in a more abstract form in the author’s books [Ber12a] and [Ber20]. In particular, there is a highly parallelizable and convergent distributed implementation, which is based on state space partitioning, and asynchronous policy evaluation and policy improvement operations within each set of the partition. The key idea, which forms the core of asynchronous DP algorithms [Ber82], [Ber83] (see also the books [BeT89], [Ber12a], [Ber20]) is that the mapping Gµ,! of Eq. (5.77) has two components for every state (policy evaluation and policy improvement) for the minimizer and two corresponding components for every state for the maximizer. Because of the uniform sup-norm contraction property of Gµ,! , iterating with any one of these components, and at any single state, does not impede the progress made by iterations with the other components, while making eventual progress towards the solution. 
In view of its asynchronous convergence capability, our framework is also suitable for on-line implementations where policy improvement and evaluations are done at only one state at a time. In such implementations, the algorithm performs a policy improvement at a single state, followed by a number of policy evaluations at other states, with the current policy pair (µt, !t) evaluated at only one state x at a time, and the cycle is repeated. One may select states cyclically for policy improvement, but there are alternative possibilities, including the case where states are selected on-line as the system operates. An on-line PI algorithm of this type, which may also be operated as a rollout algorithm (a control selected by a policy improvement at each encountered state), was given recently in the author’s paper [Ber21a], and can be straightforwardly adapted to the minimax and Markov game cases of this chapter. 
Other algorithmic possibilities, also discussed in the works just noted, involve the presence of “communication delays” between processors, which roughly means that the iterates generated at some processors may involve iterates of other processors that are out-of-date. This is possible because the asynchronous convergence line of analysis framework of [Ber83] in combination with the uniform weighted sup-norm contraction property of Prop. 5.4.2 can tolerate the presence of such delays. Implementations that involve forms of stochastic sampling have also been given in the papers [BeY12], [YuB13a]. 
An important issue for e!cient implementation of our algorithm is the relative frequency of policy improvement and policy evaluation operations. If a very large number of contiguous policy evaluation operations, using the
Sec. 5.6 Notes and Sources 375 
same policy pair (µt, !t), is done between policy improvement operations, the policy evaluation is nearly exact. Then the algorithm’s behavior is essentially the same as the one of the nonoptimistic algorithm where policy evaluation is done according to 
J1,µt,!t(x1) = H1 
5 
x1, µt(x1),max 3 
V t 2 , J2,µt,!t 
4 
6 
, x1 # X1, 
J2,µt,!t(x2) = H2 
5 
x2, !t(x2),min 3 
V t 1 , J1,µt,!t 
4 
6 
, x2 # X2, 
cf. Eqs. (5.44)-(5.45) (in the context of Markovian decision problems, this type of policy evaluation involves the solution of an optimal stopping problem; cf. the paper [BeY12]). Otherwise the policy evaluation is in-exact/optimistic, and in the extreme case where only one policy evaluation is done between policy improvements, the algorithm resembles a value iteration method. Based on experience with optimistic PI, it appears that the optimal number of policy evaluations between policy improvements should be substantially larger than one, and should also be problem-dependent. 
We mention the possibility of extensions to other related minimax and Markov game problems. In particular, the treatment of undiscounted problems that involve a termination state can be patterned after the distributed asynchronous PI algorithm for stochastic shortest path problems by Yu and Bertsekas [YuB13a], and will be the subject of a separate report. A related area of investigation is on-line algorithms applied to robust shortest path planning problems, where the aim is to reach a termination state at minimum cost and against the actions of an antagonistic opponent. The author’s paper [Ber19c] (see also Section 3.5.3) has provided analysis and algorithms, some of the PI type, for these minimax versions of shortest path problems, and has given many references of related works. Still our PI algorithm of Section 5.3, appropriately extended, o"ers some substantial advantages within the shortest path context, in both a serial and a distributed computing environment. 
Note that a sequential minimax problem with a finite horizon may be viewed as a simple special case of an infinite horizon problem with a termination state. The PI algorithms of the present chapter are directly applicable and can be simply modified for such a problem. In conjunction with function approximation methods, such as the aggregation method described earlier, they may provide an attractive alternative to exact, but hopelessly time-consuming solution approaches. 
For an interesting class of finite horizon problems, consider a twostage “robust” version of stochastic programming, patterned after Ex-ample 5.3.3 and Eq. (5.42). Here, at an initial state x0, the decision maker/minimizer applies a decision u0 # U(x0), an antagonistic nature chooses v0 # V (x0, u0), and a random disturbance w0 is generated according to a probability distribution than depends on (x0, u0, v0). A cost
376 Sequential Zero-Sum Games and Minimax Control Chap. 5 
g0(x0, u0, v0, w0) is then incurred and the next state 
x1 = f(x0, u0, v0, w0) 
is generated. Then the process is repeated at the second stage, with (x1, u1, v1, w1) replacing (x0, u0, v0, w0), and finally a terminal cost G2(x2) is incurred where 
x2 = f(x1, u1, v1, w1). 
Here the decision maker aims to minimize the expected total cost assuming a worst-case selection of (v0, v1). The maximizing choices (v0, v1) may have a variety of problem-dependent interpretations, including prices a"ecting the costs g0, g1, G2, and forecasts a"ecting the probability distributions of the disturbances (w0, w1). The distributed asynchronous PI algorithm of Section 5.3 is easily modified for this problem, and similarly can be interpreted as Newton’s method for solving a two-stage version of Bellman’s equation. Exact solution of the problem may be a daunting computational task, but a satisfactory suboptimal solution, along the lines of Section 5.5, using approximation in value space with function approximation based on aggregation may prove feasible. 
Finally, let us note a theoretical use of our line of analysis that is based on uniform contraction properties. It may form the basis for a rigorous mathematical treatment of PI algorithms in stochastic two-player DP models that involve universally measurable policies. We refer to the paper by Yu and Bertsekas [YuB15], where the associated issues of validity and convergence of PI methods for single-player problems have been addressed using algorithmic ideas that are closely related to the ones of the present chapter.
APPENDIX A: 
Notation and Mathematical 
Conventions 
In this appendix we collect our notation, and some related mathematical facts and conventions. 
A.1 SET NOTATION AND CONVENTIONS 
If X is a set and x is an element of X , we write x ! X . A set can be specified in the form X = {x | x satisfies P}, as the set of all elements satisfying property P . The union of two sets X1 and X2 is denoted by X1 "X2, and their intersection by X1 #X2. The empty set is denoted by Ø. The symbol $ means “for all.” 
The set of real numbers (also referred to as scalars) is denoted by %. The set of extended real numbers is denoted by %*: 
%* = % " {&,'&}. 
We write '& < x < & for all real numbers x, and '& ( x ( & for all extended real numbers x. We denote by [a, b] the set of (possibly extended) real numbers x satisfying a ( x ( b. A rounded, instead of square, bracket denotes strict inequality in the definition. Thus (a, b], [a, b), and (a, b) denote the set of all x satisfying a < x ( b, a ( x < b, and a < x < b, respectively. 
Generally, we adopt standard conventions regarding addition and multiplication in %*, except that we take 
&'& = '&+& = &, 
377
378 Notation and Mathematical Conventions Appendix A 
and we take the product of 0 and & or '& to be 0. In this way the sum and product of two extended real numbers is well-defined. Division by 0 or & does not appear in our analysis. In particular, we adopt the following rules in calculations involving & and '&: 
!+& = &+ ! = &, $ ! ! %*, 
!'& = '&+ ! = '&, $ ! ! ['&,&), 
! ·& = &, ! · ('&) = '&, $ ! ! (0,&], 
! ·& = '&, ! · ('&) = &, $ ! ! ['&, 0), 
0 ·& = & · 0 = 0 = 0 · ('&) = ('&) · 0, '('&) = &. 
Under these rules, the following laws of arithmetic are still valid within %*: 
!1 + !2 = !2 + !1, (!1 + !2) + !3 = !1 + (!2 + !3), 
!1!2 = !2!1, (!1!2)!3 = !1(!2!3). 
We also have 
!(!1 + !2) = !!1 + !!2 
if either ! ) 0 or else (!1 + !2) is not of the form &'&. 
Inf and Sup Notation 
The supremum of a nonempty set X * %*, denoted by supX , is defined as the smallest y ! %* such that y ) x for all x ! X . Similarly, the infimum of X , denoted by inf X , is defined as the largest y ! %* such that y ( x for all x ! X . For the empty set, we use the convention 
supØ = '&, inf Ø = &. 
If supX is equal to an x ! %* that belongs to the set X , we say that x is the maximum point of X and we write x = maxX. Similarly, if inf X is equal to an x ! %* that belongs to the set X , we say that x is the minimum point of X and we write x = minX. Thus, when we write maxX (or minX) in place of supX (or inf X , respectively), we do so just for emphasis: we indicate that it is either evident, or it is known through earlier analysis, or it is about to be shown that the maximum (or minimum, respectively) of the set X is attained at one of its points.
Sec. A.2 Functions 379 
A.2 FUNCTIONS 
If f is a function, we use the notation f : X +, Y to indicate the fact that f is defined on a nonempty set X (its domain) and takes values in a set Y (its range). Thus when using the notation f : X +, Y , we implicitly assume that X is nonempty. We will often use the unit function e : X +, %, defined by 
e(x) = 1, $ x ! X. 
Given a set X , we denote by R(X) the set of real-valued functions J : X +, %, and by E(X) the set of all extended real-valued functions J : X +, %*. For any collection {J! | " ! !} * E(X), parameterized by the elements of a set !, we denote by inf!!! J! the function taking the value inf!!! J!(x) at each x ! X . 
For two functions J1, J2 ! E(X), we use the shorthand notation J1 ( J2 to indicate the pointwise inequality 
J1(x) ( J2(x), $ x ! X. 
We use the shorthand notation infi!I Ji to denote the function obtained by pointwise infimum of a collection {Ji | i ! I} * E(X), i.e., 
! 
inf i!I 
Ji 
" 
(x) = inf i!I 
Ji(x), $ x ! X. 
We use similar notation for sup. Given subsets S1, S2, S3 * E(X) and mappings T1 : S1 +, S3 and 
T2 : S2 +, S1, the composition of T1 and T2 is the mapping T1T2 : S2 +, S3 
defined by 
(T1T2J)(x) = # 
T1(T2J) $ 
(x), $ J ! S2, x ! X. 
In particular, given a subset S * E(X) and mappings T1 : S +, S and T2 : S +, S, the composition of T1 and T2 is the mapping T1T2 : S +, S defined by 
(T1T2J)(x) = # 
T1(T2J) $ 
(x), $ J ! S, x ! X. 
Similarly, given mappings Tk : S +, S, k = 1, . . . , N , their composition is the mapping (T1 · · ·TN) : S +, S defined by 
(T1T2 · · ·TNJ)(x) = # 
T1(T2(· · · (TNJ))) $ 
(x), $ J ! S, x ! X. 
In our notation involving compositions we minimize the use of parentheses, as long as clarity is not compromised. In particular, we write T1T2J instead of (T1T2J) or (T1T2)J or T1(T2J), but we write (T1T2J)(x) to indicate the value of T1T2J at x ! X . 
If X and Y are nonempty sets, a mapping T : S1 +, S2, where S1 * E(X) and S2 * E(Y ), is said to be monotone if for all J, J " ! S1, 
J ( J " - TJ ( TJ ".
380 Notation and Mathematical Conventions Appendix A 
Sequences of Functions 
For a sequence of functions {Jk} * E(X) that converges pointwise, we denote by limk#$ Jk the pointwise limit of {Jk}. We denote by lim supk#$ Jk (or lim infk#$ Jk) the pointwise limit superior (or inferior, respectively) of {Jk}. If {Jk} * E(X) converges pointwise to J , we write Jk , J . Note that we reserve this notation for pointwise convergence. To denote convergence with respect to a norm . · ., we write .Jk ' J. , 0. 
A sequence of functions {Jk} * E(X) is said to be monotonically nonincreasing (or monotonically nondecreasing) if Jk+1 ( Jk for all k (or Jk+1 ) Jk for all k, respectively). Such a sequence always has a (pointwise) limit within E(X). We write Jk / J (or Jk 0 J) to indicate that {Jk} is monotonically nonincreasing (or monotonically nondecreasing, respectively) and that its limit is J . 
Let {Jmn} * E(X) be a double indexed sequence, which is monotonically nonincreasing separately for each index in the sense that 
J(m+1)n ( Jmn, Jm(n+1) ( Jmn, $ m,n = 0, 1, . . . . 
For such sequences, a useful fact is that 
lim m#$ 
% 
lim n#$ 
Jmn 
& 
= lim m#$ 
Jmm. 
There is a similar fact for monotonically nondecreasing sequences. 
Expected Values 
Given a random variable w defined over a probability space ", the expected value of w is defined by 
E{w} = E{w+}+ E{w%}, 
where w+ and w% are the positive and negative parts of w, 
w+(#) = max ' 
0, w(#) ( 
, w%(#) = min ' 
0, w(#) ( 
. 
In this way, taking also into account the rule & '& = &, the expected value E{w} is well-defined if " is finite or countably infinite. In more general cases, E{w} is similarly defined by the appropriate form of integration, and more detail will be given at specific points as needed.
APPENDIX B: 
Contraction Mappings 
B.1 CONTRACTION MAPPING FIXED POINT THEOREMS 
The purpose of this appendix is to provide some background on contraction mappings and their properties. Let Y be a real vector space with a norm . · ., i.e., a real-valued function satisfying for all y ! Y , .y. ) 0, .y. = 0 if and only if y = 0, and 
.ay. = |a|.y., $ a ! %, .y + z. ( .y.+ .z., $ y, z ! Y. 
Let Y be a closed subset of Y . A function F : Y +, Y is said to be a contraction mapping if for some $ ! (0, 1), we have 
.Fy ' Fz. ( $.y ' z., $ y, z ! Y . 
The scalar $ is called the modulus of contraction of F . 
Example B.1 (Linear Contraction Mappings in %n) 
Consider the case of a linear mapping F : !n "# !n of the form 
Fy = b+ Ay, 
where A is an n $ n matrix and b is a vector in !n. Let !(A) denote the spectral radius of A (the largest modulus among the moduli of the eigenvalues of A). Then it can be shown that A is a contraction mapping with respect to 
some norm if and only if !(A) < 1. Specifically, given " > 0, there exists a norm % · %s such that 
%Ay%s & # 
!(A) + " $ 
%y%s, ' y ( !n. (B.1) 
381
382 Contraction Mappings Appendix B 
Thus, if !(A) < 1 we may select " > 0 such that # = !(A)+ " < 1, and obtain the contraction relation 
%Fy ) Fz%s = ) 
)A(y ) z) ) 
) 
s & #%y ) z%s, ' y, z ( !n. (B.2) 
The norm % · %s can be taken to be a weighted Euclidean norm, i.e., it may have the form %y%s = %My%, where M is a square invertible matrix, and % · % is the standard Euclidean norm, i.e., %x% = 
* x!x. † 
Conversely, if Eq. (B.2) holds for some norm % · %s and all real vectors y, z, it also holds for all complex vectors y, z with the squared norm %c%2s of a complex vector c defined as the sum of the squares of the norms of the real and the imaginary components. Thus from Eq. (B.2), by taking y ) z = u, where u is an eigenvector corresponding to an eigenvalue $ with |$| = !(A), we have !(A)%u%s = %Au%s & #%u%s. Hence !(A) & #, and it follows that if F is a contraction with respect to a given norm, we must have !(A) < 1. 
A sequence {yk} * Y is said to be a Cauchy sequence if .ym'yn. , 0 as m,n , &, i.e., given any % > 0, there exists N such that .ym ' yn. ( % for all m,n ) N . The space Y is said to be complete under the norm . ·. if every Cauchy sequence {yk} * Y is convergent, in the sense that for some y ! Y , we have .yk ' y. , 0. Note that a Cauchy sequence is always bounded. Also, a Cauchy sequence of real numbers is convergent, implying that the real line is a complete space and so is every real finite-dimensional vector space. On the other hand, an infinite dimensional space may not be complete under some norms, while it may be complete under other norms. 
When Y is complete and Y is a closed subset of Y , an important property of a contraction mapping F : Y +, Y is that it has a unique fixed point within Y , i.e., the equation 
y = Fy 
has a unique solution y& ! Y , called the fixed point of F . Furthermore, the sequence {yk} generated by the iteration 
yk+1 = Fyk 
† We may show Eq. (B.1) by using the Jordan canonical form of A, which is denoted by J . In particular, if P is a nonsingular matrix such that P"1AP = J and D is the diagonal matrix with 1, %, . . . , %n"1 along the diagonal, where % > 0, it is straightforward to verify that D"1P"1APD = Ĵ , where Ĵ is the matrix that is identical to J except that each nonzero o!-diagonal term is replaced by %. Defining P̂ = PD, we have A = P̂ ĴP̂"1. Now if % · % is the standard Euclidean norm, we note that for some & > 0, we have %Ĵz% & 
# 
!(A) + &% $ 
%z% for all z ( !n and % ( (0, 1]. For a given % ( (0, 1], consider the weighted Euclidean norm % · %s defined by %y%s = %P̂"1y%. Then we have for all y ( !n, 
%Ay%s = %P̂"1Ay% = %P̂"1P̂ ĴP̂"1y% = %ĴP̂"1y% & # 
!(A) + &% $ 
%P̂"1y%, 
so that %Ay%s & # 
!(A) + &% $ 
%y%s, for all y ( !n. For a given " > 0, we choose 
% = "/&, so the preceding relation yields Eq. (B.1).
Sec. B.1 Contraction Mapping Fixed Point Theorems 383 
converges to y&, starting from an arbitrary initial point y0. 
Proposition B.1: (Contraction Mapping Fixed-Point Theo-rem) Let Y be a complete vector space and let Y be a closed subset of Y . Then if F : Y +, Y is a contraction mapping with modulus $ ! (0, 1), there exists a unique y& ! Y such that 
y& = Fy&. 
Furthermore, the sequence {F ky} converges to y& for any y ! Y , and we have 
.F ky ' y&. ( $k.y ' y&., k = 1, 2, . . . . 
Proof: Let y ! Y and consider the iteration yk+1 = Fyk starting with y0 = y. By the contraction property of F , 
.yk+1 ' yk. ( $.yk ' yk%1., k = 1, 2, . . . , 
which implies that 
.yk+1 ' yk. ( $k.y1 ' y0., k = 1, 2, . . . . 
It follows that for every k ) 0 and m ) 1, we have 
.yk+m ' yk. ( m * 
i=1 
.yk+i ' yk+i%1. 
( $k(1 + $+ · · ·+ $m%1).y1 ' y0. 
( $k 
1' $ .y1 ' y0.. 
Therefore, {yk} is a Cauchy sequence in Y and must converge to a limit y& ! Y , since Y is complete and Y is closed. We have for all k ) 1, 
.Fy& ' y&. ( .Fy& ' yk.+ .yk ' y&. ( $.y& ' yk%1.+ .yk ' y&. 
and since yk converges to y&, we obtain Fy& = y&. Thus, the limit y& of yk is a fixed point of F . It is a unique fixed point because if ỹ were another fixed point, we would have 
.y& ' ỹ. = .Fy& ' F ỹ. ( $.y& ' ỹ., 
which implies that y& = ỹ.
384 Contraction Mappings Appendix B 
To show the convergence rate bound of the last part, note that 
.F ky ' y&. = ) 
)F ky ' Fy& ) 
) ( $.F k%1y ' y&.. 
Repeating this process for a total of k times, we obtain the desired result. Q.E.D. 
The convergence rate exhibited by F ky in the preceding proposition is said to be geometric, and F ky is said to converge to its limit y& geometrically. This is in reference to the fact that the error .F ky' y&. converges to 0 faster than some geometric progression ($k.y ' y&. in this case). 
In some contexts of interest to us one may encounter mappings that are not contractions, but become contractions when iterated a finite number of times. In this case, one may use a slightly di#erent version of the contraction mapping fixed point theorem, which we now present. 
We say that a function F : Y +, Y is an m-stage contraction mapping if there exists a positive integer m and some $ < 1 such that 
) 
)Fmy ' Fmy" ) 
) ( $.y ' y"., $ y, y" ! Y, 
where Fm denotes the composition of F with itself m times. Thus, F is an m-stage contraction if Fm is a contraction. Again, the scalar $ is called the modulus of contraction. We have the following generalization of Prop. B.1. 
Proposition B.2: (m-Stage Contraction Mapping Fixed-Point Theorem) Let Y be a complete vector space and let Y be a closed subset of Y . Then if F : Y +, Y is an m-stage contraction mapping with modulus $ ! (0, 1), there exists a unique y& ! Y such that 
y& = Fy&. 
Furthermore, {F ky} converges to y& for any y ! Y . 
Proof: Since Fm maps Y into Y and is a contraction mapping, by Prop. B.1, it has a unique fixed point in Y , denoted y&. Applying F to both sides of the relation y& = Fmy&, we see that Fy& is also a fixed point of Fm, so by the uniqueness of the fixed point, we have y& = Fy&. Therefore y& is a fixed point of F . If F had another fixed point, say ỹ, then we would have ỹ = Fmỹ, which by the uniqueness of the fixed point of Fm implies that ỹ = y&. Thus, y& is the unique fixed point of F . 
To show the convergence of {F ky}, note that by Prop. B.1, we have for all y ! Y , 
lim k#$ 
.Fmky ' y&. = 0.
Sec. B.2 Weighted Sup-Norm Contractions 385 
Using F "y in place of y, we obtain 
lim k#$ 
.Fmk+"y ' y&. = 0, & = 0, 1, . . . ,m' 1, 
which proves the desired result. Q.E.D. 
B.2 WEIGHTED SUP-NORM CONTRACTIONS 
In this section, we will focus on contraction mappings within a specialized context that is particularly important in DP. Let X be a set (typically the state space in DP), and let v : X +, % be a positive-valued function, 
v(x) > 0, $ x ! X. 
Let B(X) denote the set of all functions J : X +, % such that J(x)/v(x) is bounded as x ranges over X . We define a norm on B(X), called the weighted sup-norm, by 
.J. = sup x!X 
+ 
+J(x) + 
+ 
v(x) . (B.3) 
It is easily verified that .·. thus defined has the required properties for being a norm. Furthermore, B(X) is complete under this norm. To see this, consider a Cauchy sequence {Jk} * B(X), and note that .Jm'Jn. , 0 as m,n , & implies that for all x ! X , {Jk(x)} is a Cauchy sequence of real numbers, so it converges to some J*(x). We will show that J* ! B(X) and that .Jk ' J*. , 0. To this end, it will be su$cient to show that given any % > 0, there exists an integer K such that 
+ 
+Jk(x)' J*(x) + 
+ 
v(x) ( %, $ x ! X, k ) K. 
This will imply that 
sup x!X 
+ 
+J*(x) + 
+ 
v(x) ( %+ .Jk., $ k ) K, 
so that J* ! B(X), and will also imply that .Jk ' J*. ( %, so that .Jk ' J*. , 0. Assume the contrary, i.e., that there exists an % > 0 and a subsequence {xm1 
, xm2 , . . .} * X such that mi < mi+1 and 
% < 
+ 
+Jmi (xmi 
)' J*(xmi ) + 
+ 
v(xmi ) 
, $ i ) 1. 
The right-hand side above is less or equal to + 
+Jmi (xmi 
)' Jn(xmi ) + 
+ 
v(xmi ) 
+ 
+ 
+Jn(xmi )' J*(xmi 
) + 
+ 
v(xmi ) 
, $ n ) 1, i ) 1.
386 Contraction Mappings Appendix B 
The first term in the above sum is less than %/2 for i and n larger than some threshold; fixing i and letting n be su$ciently large, the second term can also be made less than %/2, so the sum is made less than % - a contradiction. In conclusion, the space B(X) is complete, so the fixed point results of Props. B.1 and B.2 apply. 
In our discussions, unless we specify otherwise, we will assume that B(X) is equipped with the weighted sup-norm above, where the weight function v will be clear from the context. There will be frequent occasions where the norm will be unweighted, i.e., v(x) 1 1 and .J. = supx!X 
+ 
+J(x) + 
+, in which case we will explicitly state so. 
Finite-Dimensional Cases 
Let us now focus on the finite-dimensional case X = {1, . . . , n}, in which case R(X) and B(X) can be identified with %n. We first consider a linear mapping (cf. Example B.1). We have the following proposition. 
Proposition B.3: Consider a linear mapping F : %n +, %n of the form 
Fy = b+Ay, 
where A is an n 2 n matrix with components aij , and b is a vector in %n. Denote by |A| the matrix whose components are the absolute values of the components of A and let '(A) and ' 
# 
|A| $ 
denote the spectral radii of A and |A|, respectively. Then: 
(a) |A| has a real eigenvalue (, which is equal to its spectral radius, and an associated nonnegative eigenvector. 
(b) F is a contraction with respect to some weighted sup-norm if and only if ' 
# 
|A| $ 
< 1. In particular, any substochastic matrix P (pij ) 0 for all i, j, and 
,n j=1 pij ( 1, for all i) is a contraction 
with respect to some weighted sup-norm if and only if '(P ) < 1. 
(c) F is a contraction with respect to the weighted sup-norm 
.y. = max i=1,...,n 
|yi| 
v(i) 
if and only if 
,n j=1 |aij | v(j) 
v(i) < 1, i = 1, . . . , n.
Sec. B.2 Weighted Sup-Norm Contractions 387 
Proof: (a) This is the Perron-Frobenius Theorem; see e.g., [BeT89], Chap-ter 2, Prop. 6.6. 
(b) This follows from the Perron-Frobenius Theorem; see [BeT89], Chapter 2, Cor. 6.2. 
(c) This is proved in more general form in the following Prop. B.4. Q.E.D. 
Consider next a nonlinear mapping F : %n +, %n that has the property 
|Fy ' Fz| ( P |y ' z|, $ y, z ! %n, 
for some matrix P with nonnegative components and '(P ) < 1. Here, we generically denote by |w| the vector whose components are the absolute values of the components of w, and the inequality is componentwise. Then we claim that F is a contraction with respect to some weighted sup-norm. To see this note that by the preceding discussion, P is a contraction with respect to some weighted sup-norm .y. = maxi=1,...,n |yi|/v(i), and we have 
# 
|Fy ' Fz| $ 
(i) 
v(i) ( 
# 
P |y ' z| $ 
(i) 
v(i) ( ! .y ' z., $ i = 1, . . . , n, 
for some ! ! (0, 1), where # 
|Fy ' Fz| $ 
(i) and # 
P |y ' z| $ 
(i) are the ith components of the vectors |Fy ' Fz| and P |y ' z|, respectively. Thus, F is a contraction with respect to . · .. For additional discussion of linear and nonlinear contraction mapping properties and characterizations such as the one above, see the book [OrR70]. 
Linear Mappings on Countable Spaces 
The case where X is countable (or, as a special case, finite) is frequently encountered in DP. The following proposition provides some useful criteria for verifying the contraction property of mappings that are either linear or are obtained via a parametric minimization of other contraction mappings. 
Proposition B.4: Let X = {1, 2, . . .}. 
(a) Let F : B(X) +, B(X) be a linear mapping of the form 
(FJ)(i) = bi + * 
j!X 
aijJ(j), i ! X,
388 Contraction Mappings Appendix B 
where bi and aij are some scalars. Then F is a contraction with modulus $ with respect to the weighted sup-norm (B.3) if and only if 
, 
j!X |aij | v(j) 
v(i) ( $, i ! X. (B.4) 
(b) Let F : B(X) +, B(X) be a mapping of the form 
(FJ)(i) = inf µ!M 
(FµJ)(i), i ! X, 
where M is parameter set, and for each µ ! M , Fµ is a contraction mapping from B(X) to B(X) with modulus $. Then F is a contraction mapping with modulus $. 
Proof: (a) Assume that Eq. (B.4) holds. For any J, J " ! B(X), we have 
.FJ ' FJ ". = sup i!X 
+ 
+ 
+ 
, 
j!X aij # 
J(j)' J "(j) $ 
+ 
+ 
+ 
v(i) 
( sup i!X 
, 
j!X 
+ 
+aij + 
+ v(j) % 
+ 
+J(j)' J "(j) + 
+/v(j) & 
v(i) 
( sup i!X 
, 
j!X 
+ 
+aij + 
+ v(j) 
v(i) 
) 
)J ' J " ) 
) 
( $ .J ' J "., 
where the last inequality follows from the hypothesis. Conversely, arguing by contradiction, let’s assume that Eq. (B.4) is 
violated for some i ! X . Define J(j) = v(j) sgn(aij) and J "(j) = 0 for all j ! X . Then we have .J ' J ". = .J. = 1, and 
+ 
+(FJ)(i)' (FJ ")(i) + 
+ 
v(i) = 
, 
j!X |aij | v(j) 
v(i) > $ = $ .J ' J "., 
showing that F is not a contraction of modulus $. 
(b) Since Fµ is a contraction of modulus $, we have for any J, J " ! B(X), 
(FµJ)(i) 
v(i) ( 
(FµJ ")(i) 
v(i) + $ .J ' J "., i ! X, 
so by taking the infimum over µ ! M , 
(FJ)(i) 
v(i) ( 
(FJ ")(i) 
v(i) + $ .J ' J "., i ! X.
Sec. B.2 Weighted Sup-Norm Contractions 389 
Reversing the roles of J and J ", we obtain + 
+(FJ)(i)' (FJ ")(i) + 
+ 
v(i) ( $ .J ' J "., i ! X, 
and by taking the supremum over i, the contraction property of F is proved. Q.E.D. 
The preceding proposition assumes that FJ ! B(X) for all J ! B(X). The following proposition provides conditions, particularly relevant to the DP context, which imply this assumption. 
Proposition B.5: Let X = {1, 2, . . .}, let M be a parameter set, and for each µ ! M , let Fµ be a linear mapping of the form 
(FµJ)(i) = bi(µ) + * 
j!X 
aij(µ)J(j), i ! X, 
where we assume that the summation above is well-defined for all J ! B(X). 
(a) We have FµJ ! B(X) for all J ! B(X) provided b(µ) ! B(X) and V (µ) ! B(X), where 
b(µ) = ' 
b1(µ), b2(µ), . . . ( 
, V (µ) = ' 
V1(µ), V2(µ), . . . ( 
, 
with Vi(µ) = 
* 
j!X 
+ 
+aij(µ) + 
+ v(j), i ! X. 
(b) Consider the mapping F 
(FJ)(i) = inf µ!M 
(FµJ)(i), i ! X. 
We have FJ ! B(X) for all J ! B(X), provided b ! B(X) and V ! B(X), where 
b = ' 
b1, b2, . . . ( 
, V = {V1, V2, . . .}, 
with bi = supµ!M bi(µ) and Vi = supµ!M Vi(µ). 
Proof: (a) For all µ ! M , J ! B(X) and i ! X , we have 
(FµJ)(i) ( + 
+bi(µ) + 
++ * 
j!X 
+ 
+aij(µ) + 
+ 
+ 
+J(j)/v(j) + 
+ v(j)
390 Contraction Mappings Appendix B 
( + 
+bi(µ) + 
++ .J. * 
j!X 
+ 
+aij(µ) + 
+ v(j) 
= + 
+bi(µ) + 
++ .J.Vi(µ), 
and similarly (FµJ)(i) ) ' + 
+bi(µ) + 
+ ' .J.Vi(µ). Thus 
+ 
+(FµJ)(i) + 
+ ( + 
+bi(µ) + 
+ + .J.Vi(µ), i ! X. 
By dividing this inequality with v(i) and by taking the supremum over i ! X , we obtain 
.FµJ. ( .bµ.+ .J. .Vµ. < &. 
(b) By doing the same as in (a), but after first taking the infimum of (FµJ)(i) over µ, we obtain 
.FJ. ( .b.+ .J. .V . < &. 
Q.E.D.
References 
[ABB02] Abounadi, J., Bertsekas, B. P., and Borkar, V. S., 2002. “Stochastic Approximation for Non-Expansive Maps: Q-Learning Algorithms,” SIAM J. on Control and Opt., Vol. 41, pp. 1-22. 
[AnM79] Anderson, B. D. O., and Moore, J. B., 1979. Optimal Filtering, Prentice Hall, Englewood Cli!s, N. J. 
[BBB08] Basu, A., Bhattacharyya, and Borkar, V., 2008. “A Learning Algorithm for Risk-Sensitive Cost,” Math. of OR, Vol. 33, pp. 880-898. 
[BBD10] Busoniu, L., Babuska, R., De Schutter, B., and Ernst, D., 2010. Rein-forcement Learning and Dynamic Programming Using Function Approximators, CRC Press, N. Y. 
[BFH86] Breton, M., Filar, J. A., Haurie, A., and Schultz, T. A., 1986. “On the Computation of Equilibria in Discounted Stochastic Dynamic Games,” in Dynamic Games and Applications in Economics, Springer, pp. 64-87. 
[Bau78] Baudet, G. M., 1978. “Asynchronous Iterative Methods for Multiproces-sors,” Journal of the ACM, Vol. 25, pp. 226-244. 
[BeI96] Bertsekas, D. P., and Io!e, S., 1996. “Temporal Di!erences-Based Policy Iteration and Applications in Neuro-Dynamic Programming,” Lab. for Info. and Decision Systems Report LIDS-P-2349, MIT. 
[BeK65] Bellman, R., and Kalaba, R. E., 1965. Quasilinearization and Nonlinear Boundary-Value Problems, Elsevier, N.Y. 
[BeS78] Bertsekas, D. P., and Shreve, S. E., 1978. Stochastic Optimal Control: The Discrete Time Case, Academic Press, N. Y.; may be downloaded from http://web.mit.edu/dimitrib/www/home.html 
[BeT89] Bertsekas, D. P., and Tsitsiklis, J. N., 1989. Parallel and Distributed Computation: Numerical Methods, Prentice-Hall, Engl. Cli!s, N. J.; may be downloaded from http://web.mit.edu/dimitrib/www/home.html 
[BeT91] Bertsekas, D. P., and Tsitsiklis, J. N., 1991. “An Analysis of Stochastic Shortest Path Problems,” Math. of OR, Vol. 16, pp. 580-595. 
[BeT96] Bertsekas, D. P., and Tsitsiklis, J. N., 1996. Neuro-Dynamic Program-ming, Athena Scientific, Belmont, MA. 
[BeT08] Bertsekas, D. P., and Tsitsiklis, J. N., 2008. Introduction to Probability, 2nd Ed., Athena Scientific, Belmont, MA. 
391
392 References 
[BeY07] Bertsekas, D. P., and Yu, H., 2007. “Solution of Large Systems of Equa-tions Using Approximate Dynamic Programming Methods,” Lab. for Info. and Decision Systems Report LIDS-P-2754, MIT. 
[BeY09] Bertsekas, D. P., and Yu, H., 2009. “Projected Equation Methods for Ap-proximate Solution of Large Linear Systems,” J. of Computational and Applied Mathematics, Vol. 227, pp. 27-50. 
[BeY10] Bertsekas, D. P., and Yu, H., 2010. “Asynchronous Distributed Policy Iteration in Dynamic Programming,” Proc. of Allerton Conf. on Communication, Control and Computing, Allerton Park, Ill, pp. 1368-1374. 
[BeY12] Bertsekas, D. P., and Yu, H., 2012. “Q-Learning and Enhanced Policy Iteration in Discounted Dynamic Programming,” Math. of OR, Vol. 37, pp. 66-94. 
[BeY16] Bertsekas, D. P., and Yu, H., 2016. “Stochastic Shortest Path Problems Under Weak Conditions,” Lab. for Information and Decision Systems Report LIDS-2909, January 2016. 
[Ber71] Bertsekas, D. P., 1971. “Control of Uncertain SystemsWith a Set-Member-ship Description of the Uncertainty,” Ph.D. Dissertation, Massachusetts Institute of Technology, Cambridge, MA (available from the author’s website). 
[Ber72] Bertsekas, D. P., 1972. “Infinite Time Reachability of State Space Regions by Using Feedback Control,” IEEE Trans. Aut. Control, Vol. AC-17, pp. 604-613. 
[Ber75] Bertsekas, D. P., 1975. “Monotone Mappings in Dynamic Programming,” 1975 IEEE Conference on Decision and Control, pp. 20-25. 
[Ber77] Bertsekas, D. P., 1977. “Monotone Mappings with Application in Dy-namic Programming,” SIAM J. on Control and Opt., Vol. 15, pp. 438-464. 
[Ber82] Bertsekas, D. P., 1982. “Distributed Dynamic Programming,” IEEE Trans. Aut. Control, Vol. AC-27, pp. 610-616. 
[Ber83] Bertsekas, D. P., 1983. “Asynchronous Distributed Computation of Fixed Points,” Math. Programming, Vol. 27, pp. 107-120. 
[Ber87] Bertsekas, D. P., 1987. Dynamic Programming: Deterministic and Stochas-tic Models, Prentice-Hall, Englewood Cli!s, N. J. 
[Ber96] Bertsekas, D. P., 1996. Lecture at NSF Workshop on Reinforcement Learning, Hilltop House, Harper’s Ferry, N. Y. 
[Ber98] Bertsekas, D. P., 1998. Network Optimization: Continuous and Discrete Models, Athena Scientific, Belmont, MA. 
[Ber09] Bertsekas, D. P., 2009. Convex Optimization Theory, Athena Scientific, Belmont, MA. 
[Ber10] Bertsekas, D. P., 2010. “Williams-Baird Counterexample for Q-Factor Asynchronous Policy Iteration,” http://web.mit.edu/dimitrib/www/Williams-Baird Counterexample.pdf 
[Ber11a] Bertsekas, D. P., 2011. “Temporal Di!erence Methods for General Pro-jected Equations,” IEEE Trans. Aut. Control, Vol. 56, pp. 2128-2139. 
[Ber11b] Bertsekas, D. P., 2011. “$-Policy Iteration: A Review and a New Im-plementation,” Lab. for Info. and Decision Systems Report LIDS-P-2874, MIT; appears in Reinforcement Learning and Approximate Dynamic Programming for Feedback Control, by F. Lewis and D. Liu (eds.), IEEE Press, 2012. 
[Ber11c] Bertsekas, D. P., 2011. “Approximate Policy Iteration: A Survey and
References 393 
Some New Methods,” J. of Control Theory and Applications, Vol. 9, pp. 310-335; a somewhat expanded version appears as Lab. for Info. and Decision Systems Report LIDS-2833, MIT, 2011. 
[Ber12a] Bertsekas, D. P., 2012. Dynamic Programming and Optimal Control, Vol. II, 4th Edition: Approximate Dynamic Programming, Athena Scientific, Belmont, MA. 
[Ber12b] Bertsekas, D. P., 2012. “Weighted Sup-Norm Contractions in Dynamic Programming: A Review and Some New Applications,” Lab. for Info. and Deci-sion Systems Report LIDS-P-2884, MIT. 
[Ber15] Bertsekas, D. P., 2015. “Regular Policies in Abstract Dynamic Program-ming,” Lab. for Information and Decision Systems Report LIDS-P-3173, MIT, May 2015; arXiv preprint arXiv:1609.03115; SIAM J. on Optimization, Vol. 27, 2017, pp. 1694-1727. 
[Ber16a] Bertsekas, D. P., 2016. “A"ne Monotonic and Risk-Sensitive Models in Dynamic Programming,” Lab. for Information and Decision Systems Report LIDS-3204, MIT, June 2016; arXiv preprint arXiv:1608.01393; IEEE Trans. on Aut. Control, Vol. 64, 2019, pp. 3117-3128. 
[Ber16b] Bertsekas, D. P., 2016. “Proximal Algorithms and Temporal Di!erences for Large Linear Systems: Extrapolation, Approximation, and Simulation,” Re-port LIDS-P-3205, MIT, Oct. 2016; arXiv preprint arXiv:1610.1610.05427. 
[Ber16c] Bertsekas, D. P., 2016. Nonlinear Programming, 3rd Edition, Athena Scientific, Belmont, MA. 
[Ber17a] Bertsekas, D. P., 2017. Dynamic Programming and Optimal Control, Vol. I, 4th Edition, Athena Scientific, Belmont, MA. 
[Ber17b] Bertsekas, D. P., 2017. “Value and Policy Iteration in Deterministic Optimal Control and Adaptive Dynamic Programming,” IEEE Transactions on Neural Networks and Learning Systems, Vol. 28, pp. 500-509. 
[Ber17c] Bertsekas, D. P., 2017. “Stable Optimal Control and Semicontractive Dynamic Programming,” Report LIDS-P-3506, MIT, May 2017; SIAM J. on Control and Optimization, Vol. 56, 2018, pp. 231-252. 
[Ber17d] Bertsekas, D. P., 2017. “Proper Policies in Infinite-State Stochastic Shortest Path Problems,” Report LIDS-P-3507, MIT, May 2017; arXiv preprint arXiv:1711.10129. 
[Ber18a] Bertsekas, D. P., 2018. “Feature-Based Aggregation and Deep Rein-forcement Learning: A Survey and Some New Implementations,” Lab. for In-formation and Decision Systems Report, MIT; arXiv preprint arXiv:1804.04577; IEEE/CAA Journal of Automatica Sinica, Vol. 6, 2019, pp. 1-31. 
[Ber18b] Bertsekas, D. P., 2018. “Biased Aggregation, Rollout, and Enhanced Policy Improvement for Reinforcement Learning,” Lab. for Information and De-cision Systems Report, MIT; arXiv preprint arXiv:1910.02426. 
[Ber18c] Bertsekas, D. P., 2018. “Proximal Algorithms and Temporal Di!erences for Solving Fixed Point Problems,” Computational Optimization and Applica-tions J., Vol. 70, pp. 709-736. 
[Ber19a] Bertsekas, D. P., 2019. “A"ne Monotonic and Risk-Sensitive Models in Dynamic Programming,” IEEE Transactions on Aut. Control, Vol. 64, pp. 3117-3128.
394 References 
[Ber19b] Bertsekas, D. P., 2019. Reinforcement Learning and Optimal Control, Athena Scientific, Belmont, MA. 
[Ber19c] Bertsekas, D. P., 2019. “Robust Shortest Path Planning and Semicon-tractive Dynamic Programming,” Naval Research Logistics, Vol. 66, pp. 15-37. 
[Ber20] Bertsekas, D. P., 2020. Rollout, Policy Iteration, and Distributed Rein-forcement Learning, Athena Scientific, Belmont, MA. 
[Ber21a] Bertsekas, D. P., 2021. “On-Line Policy Iteration for Infinite Horizon Dynamic Programming,” arXiv preprint arXiv:2106.00746. 
[Ber21b] Bertsekas, D. P., 2021. “Multiagent Reinforcement Learning: Rollout and Policy Iteration,” IEEE/CAA J. of Automatica Sinica, Vol. 8, pp. 249-271. 
[Ber21c] Bertsekas, D. P., 2021. “Distributed Asynchronous Policy Iteration for Sequential Zero-Sum Games and Minimax Control,” arXiv preprint arXiv:2107. 10406, July 2021. 
[Ber22] Bertsekas, D. P., 2022. Lessons from AlphaZero for Optimal, Model Pre-dictive, and Stochastic Control, Athena Scientific, Belmont, MA. 
[Bla65] Blackwell, D., 1965. “Positive Dynamic Programming,” Proc. Fifth Berke-ley Symposium Math. Statistics and Probability, pp. 415-418. 
[BoM99] Borkar, V. S., Meyn, S. P., 1999. “Risk Sensitive Optimal Control: Existence and Synthesis for Models with Unbounded Cost,” SIAM J. Control and Opt., Vol. 27, pp. 192-209. 
[BoM00] Borkar, V. S., Meyn, S. P., 2000. “The O.D.E. Method for Convergence of Stochastic Approximation and Reinforcement Learning,” SIAM J. Control and Opt., Vol. 38, pp. 447-469. 
[BoM02] Borkar, V. S., Meyn, S. P., 2002. “Risk-Sensitive Optimal Control for Markov Decision Processes with Monotone Cost,” Math. of OR, Vol. 27, pp. 192-209. 
[Bor98] Borkar, V. S., 1998. “Asynchronous Stochastic Approximation,” SIAM J. Control Opt., Vol. 36, pp. 840-851. 
[Bor08] Borkar, V. S., 2008. Stochastic Approximation: A Dynamical Systems Viewpoint, Cambridge Univ. Press, N. Y. 
[CFH07] Chang, H. S., Fu, M. C., Hu, J., Marcus, S. I., 2007. Simulation-Based Algorithms for Markov Decision Processes, Springer, N. Y. 
[CaM88] Carraway, R. L., and Morin, T. L., 1988. “Theory and Applications of Generalized Dynamic Programming: An Overview,” Computers and Mathemat-ics with Applications, Vol. 16, pp. 779-788. 
[CaR13] Canbolat, P. G., and Rothblum, U. G., 2013. “(Approximate) Iterated Successive Approximations Algorithm for Sequential Decision Processes,” Annals of Operations Research, Vol. 208, pp. 309-320. 
[Cao07] Cao, X. R., 2007. Stochastic Learning and Optimization: A Sensitivity-Based Approach, Springer, N. Y. 
[ChM69] Chazan D., and Miranker, W., 1969. “Chaotic Relaxation,” Linear Al-gebra and Applications, Vol. 2, pp. 199-222. 
[ChS87] Chung, K.-J., and Sobel, M. J., 1987. “Discounted MDPs: Distribution Functions and Exponential Utility Maximization,” SIAM J. Control and Opt., Vol. 25, pp. 49-62.
References 395 
[CoM99] Coraluppi, S. P., and Marcus, S. I., 1999. “Risk-Sensitive and Minimax Control of Discrete-Time, Finite-State Markov Decision Processes,” Automatica, Vol. 35, pp. 301-309. 
[DFV00] de Farias, D. P., and Van Roy, B., 2000. “On the Existence of Fixed Points for Approximate Value Iteration and Temporal-Di!erence Learning,” J. of Optimization Theory and Applications, Vol. 105, pp. 589-608. 
[DeM67] Denardo, E. V., and Mitten, L. G., 1967. “Elements of Sequential De-cision Processes,” J. Indust. Engrg., Vol. 18, pp. 106-112. 
[DeR79] Denardo, E. V., and Rothblum, U. G., 1979. “Optimal Stopping, Ex-ponential Utility, and Linear Programming,” Math. Programming, Vol. 16, pp. 228-244. 
[Den67] Denardo, E. V., 1967. “Contraction Mappings in the Theory Underlying Dynamic Programming,” SIAM Review, Vol. 9, pp. 165-177. 
[Der70] Derman, C., 1970. Finite State Markovian Decision Processes, Academic Press, N. Y. 
[DuS65] Dubins, L., and Savage, L. M., 1965. How to Gamble If You Must, McGraw-Hill, N. Y. 
[FeM97] Fernandez-Gaucherand, E., and Marcus, S. I., 1997. “Risk-Sensitive Op-timal Control of Hidden Markov Models: Structural Results,” IEEE Trans. Aut. Control, Vol. AC-42, pp. 1418-1422. 
[Fei02] Feinberg, E. A., 2002. “Total Reward Criteria,” in E. A. Feinberg and A. Shwartz, (Eds.), Handbook of Markov Decision Processes, Springer, N. Y. 
[FiT91] Filar, J. A., and Tolwinski, B., 1991. “On the Algorithm of Pollatschek and Avi-ltzhak,” in Stochastic Games and Related Topics, Theory and Decision Library, Springer, Vol. 7, pp. 59-70. 
[FiV96] Filar, J., and Vrieze, K., 1996. Competitive Markov Decision Processes, Springer, N. Y. 
[FlM95] Fleming, W. H., and McEneaney, W. M., 1995. “Risk-Sensitive Control on an Infinite Time Horizon,” SIAM J. Control and Opt., Vol. 33, pp. 1881-1915. 
[Gos03] Gosavi, A., 2003. Simulation-Based Optimization: Parametric Optimiza-tion Techniques and Reinforcement Learning, Springer, N. Y. 
[GuS17] Guillot, M., and Stau!er, G., 2017. “The Stochastic Shortest Path Prob-lem: A Polyhedral Combinatorics Perspective,” Univ. of Grenoble Report. 
[HCP99] Hernandez-Lerma, O., Carrasco, O., and Perez-Hernandez. 1999. “Mar-kov Control Processes with the Expected Total Cost Criterion: Optimality, Sta-bility, and Transient Models,” Acta Appl. Math., Vol. 59, pp. 229-269. 
[Hay08] Haykin, S., 2008. Neural Networks and Learning Machines, (3rd Edition), Prentice-Hall, Englewood-Cli!s, N. J. 
[HeL99] Hernandez-Lerma, O., and Lasserre, J. B., 1999. Further Topics on Discrete-Time Markov Control Processes, Springer, N. Y. 
[HeM96] Hernandez-Hernandez, D., and Marcus, S. I., 1996. “Risk Sensitive Con-trol of Markov Processes in Countable State Space,” Systems and Control Letters, Vol. 29, pp. 147-155. 
[HiW05] Hinderer, K., and Waldmann, K.-H., 2005. “Algorithms for Countable State Markov Decision Models with an Absorbing Set,” SIAM J. of Control and
396 References 
Opt., Vol. 43, pp. 2109-2131. 
[HoK66] Ho!man, A. J., and Karp, R. M., 1966. “On Nonterminating Stochastic Games,” Management Science, Vol. 12, pp. 359-370. 
[HoM72] Howard, R. S., and Matheson, J. E., 1972. “Risk-Sensitive Markov Decision Processes,” Management Science, Vol. 8, pp. 356-369. 
[JBE94] James, M. R., Baras, J. S., Elliott, R. J., 1994. “Risk-Sensitive Control and Dynamic Games for Partially Observed Discrete-Time Nonlinear Systems,” IEEE Trans. Aut. Control, Vol. AC-39, pp. 780-792. 
[JaC06] James, H. W., and Collins, E. J., 2006. “An Analysis of Transient Markov Decision Processes,” J. Appl. Prob., Vol. 43, pp. 603-621. 
[Jac73] Jacobson, D. H., 1973. “Optimal Stochastic Linear Systems with Ex-ponential Performance Criteria and their Relation to Deterministic Di!erential Games,” IEEE Transactions on Automatic Control, Vol. AC-18, pp. 124-131. 
[Kal60] Kalman, R. E., 1960. “Contributions to the Theory of Optimal Control,” Bol. Soc. Mat. Mexicana, Vol. 5, pp. 102-119. 
[Kal20] Kallenberg, L., 2020. Markov Decision Processes, Lecture Notes, Univer-sity of Leiden. 
[Kle68] Kleinman, D. L., 1968. “On an Iterative Technique for Riccati Equation Computations,” IEEE Trans. Automatic Control, Vol. AC-13, pp. 114-115. 
[Kuc72] Kucera, V., 1972. “The Discrete Riccati Equation of Optimal Control,” Kybernetika, Vol. 8, pp. 430-447. 
[Kuc73] Kucera, V., 1973. “A Review of the Matrix Riccati Equation,” Kyber-netika, Vol. 9, pp. 42-61. 
[Kuh53] Kuhn, H. W., 1953. “Extensive Games and the Problem of Information,” in Kuhn, H. W., and Tucker, A. W. (eds.), Contributions to the Theory of Games, Vol. II, Annals of Mathematical Studies No. 28, Princeton University Press, pp. 193-216. 
[LaR95] Lancaster, P., and Rodman, L., 1995. Algebraic Riccati Equations, Clarendon Press, Oxford, UK. 
[Mey07] Meyn, S., 2007. Control Techniques for Complex Networks, Cambridge Univ. Press, N. Y. 
[Mit64] Mitten, L. G., 1964. “Composition Principles for Synthesis of Optimal Multistage Processes,” Operations Research, Vol. 12, pp. 610-619. 
[Mit74] Mitten, L. G., 1964. “Preference Order Dynamic Programming,” Man-agement Science, Vol. 21, pp. 43 - 46. 
[Mor82] Morin, T. L., 1982. “Monotonicity and the Principle of Optimality,” J. of Math. Analysis and Applications, Vol. 88, pp. 665-674. 
[NeB03] Nedić, A., and Bertsekas, D. P., 2003. “Least-Squares Policy Evaluation Algorithms with Linear Function Approximation,” J. of Discrete Event Systems, Vol. 13, pp. 79-110. 
[OrR70] Ortega, J. M., and Rheinboldt, W. C., 1970. Iterative Solution of Non-linear Equations in Several Variables, Academic Press, N. Y. 
[PPG16] Perolat, J., Piot, B., Geist, M., Scherrer, B., and Pietquin, O., 2016. “Softened Approximate Policy Iteration for Markov Games,” in Proc. Interna-tional Conference on Machine Learning, pp. 1860-1868.
References 397 
[PSP15] Perolat, J., Scherrer, B., Piot, B., and Pietquin, O., 2015. “Approximate Dynamic Programming for Two-Player Zero-Sum Markov Games,” in Proc. In-ternational Conference on Machine Learning, pp. 1321-1329. 
[PaB99] Patek, S. D., and Bertsekas, D. P., 1999. “Stochastic Shortest Path Games,” SIAM J. on Control and Opt., Vol. 36, pp. 804-824. 
[Pal67] Pallu de la Barriere, R., 1967. Optimal Control Theory, Saunders, Phila; republished by Dover, N. Y., 1980. 
[Pat01] Patek, S. D., 2001. “On Terminating Markov Decision Processes with a Risk Averse Objective Function,” Automatica, Vol. 37, pp. 1379-1386. 
[Pat07] Patek, S. D., 2007. “Partially Observed Stochastic Shortest Path Prob-lems with Approximate Solution by Neuro-Dynamic Programming,” IEEE Trans. on Systems, Man, and Cybernetics Part A, Vol. 37, pp. 710-720. 
[Pli78] Pliska, S. R., 1978. “On the Transient Case for Markov Decision Chains with General State Spaces,” in Dynamic Programming and its Applications, by M. L. Puterman (ed.), Academic Press, N. Y. 
[PoA69] Pollatschek, M., and Avi-Itzhak, B., 1969. “Algorithms for Stochastic Games with Geometrical Interpretation,” Management Science, Vol. 15, pp. 399-413. 
[Pow07] Powell, W. B., 2007. Approximate Dynamic Programming: Solving the Curses of Dimensionality, J. Wiley and Sons, Hoboken, N. J; 2nd ed., 2011. 
[PuB78] Puterman, M. L., and Brumelle, S. L., 1978. “The Analytic Theory of Policy Iteration,” in Dynamic Programming and Its Applications, M. L. Puter-man (ed.), Academic Press, N. Y. 
[PuB79] Puterman, M. L., and Brumelle, S. L., 1979. “On the Convergence of Policy Iteration in Stationary Dynamic Programming,” Math. of Operations Re-search, Vol. 4, pp. 60-69. 
[Put94] Puterman, M. L., 1994. Markovian Decision Problems, J. Wiley, N. Y. 
[Rei16] Reissig, G., 2016. “Approximate Value Iteration for a Class of Determin-istic Optimal Control Problems with Infinite State and Input Alphabets,” Proc. 2016 IEEE Conf. on Decision and Control, pp. 1063-1068. 
[Roc70] Rockafellar, R. T., 1970. Convex Analysis, Princeton Univ. Press, Prince-ton, N. J. 
[Ros67] Rosenfeld, J., 1967. “A Case Study on Programming for Parallel Proces-sors,” Research Report RC-1864, IBM Res. Center, Yorktown Heights, N. Y. 
[Rot79] Rothblum, U. G., 1979. “Iterated Successive Approximation for Sequen-tial Decision Processes,” in Stochastic Control and Optimization, by J. W. B. van Overhagen and H. C. Tijms (eds), Vrije University, Amsterdam. 
[Rot84] Rothblum, U. G., 1984. “Multiplicative Markov Decision Chains,” Math. of OR, Vol. 9, pp. 6-24. 
[ScL12] Scherrer, B., and Lesner, B., 2012. “On the Use of Non-Stationary Policies for Stationary Infinite-Horizon Markov Decision Processes,” NIPS 2012 - Neural Information Processing Systems, South Lake Tahoe, Ne. 
[Sch75] Schal, M., 1975. “Conditions for Optimality in Dynamic Programming and for the Limit of n-Stage Optimal Policies to be Optimal,” Z. Wahrschein-lichkeitstheorie und Verw. Gebiete, Vol. 32, pp. 179-196.
398 References 
[Sch11] Scherrer, B., 2011. “Performance Bounds for Lambda Policy Iteration and Application to the Game of Tetris,” Report RR-6348, INRIA, France; J. of Machine Learning Research, Vol. 14, 2013, pp. 1181-1227. 
[Sch12] Scherrer, B., 2012. “On the Use of Non-Stationary Policies for Infinite-Horizon Discounted Markov Decision Processes,” INRIA Lorraine Report, France. 
[Sha53] Shapley, L. S., 1953. “Stochastic Games,” Proc. Nat. Acad. Sci. U.S.A., Vol. 39. 
[Sob75] Sobel, M. J., 1975. “Ordinal Dynamic Programming,” Management Sci-ence, Vol. 21, pp. 967-975. 
[Str66] Strauch, R., 1966. “Negative Dynamic Programming,” Ann. Math. Statist., Vol. 37, pp. 871-890. 
[SuB98] Sutton, R. S., and Barto, A. G., 1998. Reinforcement Learning, MIT Press, Cambridge, MA. 
[Sze98a] Szepesvari, C., 1998. Static and Dynamic Aspects of Optimal Sequential Decision Making, Ph.D. Thesis, Bolyai Institute of Mathematics, Hungary. 
[Sze98b] Szepesvari, C., 1998. “Non-Markovian Policies in Sequential Decision Problems,” Acta Cybernetica, Vol. 13, pp. 305-318. 
[Sze10] Szepesvari, C., 2010. Algorithms for Reinforcement Learning, Morgan and Claypool Publishers, San Franscisco, CA. 
[TBA86] Tsitsiklis, J. N., Bertsekas, D. P., and Athans, M., 1986. “Distributed Asynchronous Deterministic and Stochastic Gradient Optimization Algorithms,” IEEE Trans. Aut. Control, Vol. AC-31, pp. 803-812. 
[ThS10a] Thiery, C., and Scherrer, B., 2010. “Least-Squares $-Policy Iteration: Bias-Variance Trade-o! in Control Problems,” in ICML’10: Proc. of the 27th Annual International Conf. on Machine Learning. 
[ThS10b] Thiery, C., and Scherrer, B., 2010. “Performance Bound for Approxi-mate Optimistic Policy Iteration,” Technical Report, INRIA, France. 
[Tol89] Tolwinski, B., 1989. “Newton-Type Methods for Stochastic Games,” in Basar T. S., and Bernhard P. (eds), Di!erential Games and Applications, Lecture Notes in Control and Information Sciences, vol. 119, Springer, pp. 128-144. 
[Tsi94] Tsitsiklis, J. N., 1994. “Asynchronous Stochastic Approximation and Q-Learning,” Machine Learning, Vol. 16, pp. 185-202. 
[VVL13] Vrabie, V., Vamvoudakis, K. G., and Lewis, F. L., 2013. Optimal Adap-tive Control and Di!erential Games by Reinforcement Learning Principles, The Institution of Engineering and Technology, London. 
[Van78] van der Wal, J., 1978. “Discounted Markov Games: Generalized Policy Iteration Method,” J. of Optimization Theory and Applications, Vol. 25, pp. 125-138. 
[VeP87] Verdu, S., and Poor, H. V., 1987. “Abstract Dynamic Programming Models under Commutativity Conditions,” SIAM J. on Control and Opt., Vol. 25, pp. 990-1006. 
[Wat89] Watkins, C. J. C. H., Learning from Delayed Rewards, Ph.D. Thesis, Cambridge Univ., England. 
[Whi80] Whittle, P., 1980. “Stability and Characterization Conditions in Negative Programming,” Journal of Applied Probability, Vol. 17, pp. 635-645.
References 399 
[Whi81] Whittle, P., 1981. “Risk-Sensitive Linear/Quadratic/Gaussian Control,” Advances in Applied Probability, Vol. 13, pp. 764-777. 
[Whi82] Whittle, P., 1982. Optimization Over Time, Wiley, N. Y., Vol. 1, 1982, Vol. 2, 1983. 
[Whi90] Whittle, P., 1990. Risk-Sensitive Optimal Control, Wiley, Chichester. 
[WiB93] Williams, R. J., and Baird, L. C., 1993. “Analysis of Some Incremen-tal Variants of Policy Iteration: First Steps Toward Understanding Actor-Critic Learning Systems,” Report NU-CCS-93-11, College of Computer Science, North-eastern University, Boston, MA. 
[Wil71] Willems, J., 1971. “Least Squares Stationary Optimal Control and the Algebraic Riccati Equation,” IEEE Trans. on Automatic Control, Vol. 16, pp. 621-634. 
[YuB10] Yu, H., and Bertsekas, D. P., 2010. “Error Bounds for Approximations from Projected Linear Equations,” Math. of OR, Vol. 35, pp. 306-329. 
[YuB12] Yu, H., and Bertsekas, D. P., 2012. “Weighted Bellman Equations and their Applications in Dynamic Programming,” Lab. for Info. and Decision Sys-tems Report LIDS-P-2876, MIT. 
[YuB13a] Yu, H., and Bertsekas, D. P., 2013. “Q-Learning and Policy Iteration Algorithms for Stochastic Shortest Path Problems,” Annals of Operations Re-search, Vol. 208, pp. 95-132. 
[YuB13b] Yu, H., and Bertsekas, D. P., 2013. “On Boundedness of Q-Learning Iterates for Stochastic Shortest Path Problems,” Math. of OR, Vol. 38, pp. 209-227. 
[YuB15] Yu, H., and Bertsekas, D. P., 2015. “A Mixed Value and Policy Iteration Method for Stochastic Control with Universally Measurable Policies,” Math. of OR, Vol. 40, pp. 926-968. 
[Yu14] Yu, H., 2014. “Stochastic Shortest Path Games and Q-Learning,” arXiv preprint arXiv:1412.8570. 
[Yu15] Yu, H., 2015. “On Convergence of Value Iteration for a Class of Total Cost Markov Decision Processes,” SIAM J. on Control and Optimization, Vol. 53, pp. 1982-2016. 
[ZYB21] Zhang, K., Yang, Z. and Basar, T., 2021. “Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms,” Handbook of Re-inforcement Learning and Control, pp. 321-384. 
[Zac64] Zachrisson, L. E., 1964. “Markov Games,” in Advances in Game Theory, by M. Dresher, L. S. Shapley, and A. W. Tucker, (eds.), Princeton Univ. Press, Princeton, N. J., pp. 211-253.
INDEX 
A 
Abstraction, 44 A"ne monotonic model, 19, 186, 187, 192, 194, 220, 229, 321, 356 Aggregation, 20, 371, 373 Aggregation, distributed, 23 Aggregation, multistep, 28 Aggregation equation, 26 Aggregation probability, 21, 372 Approximate DP, 25 Approximation models, 24 Asynchronous algorithms, 23, 43, 91, 114, 214, 219, 221, 374 Asynchronous convergence theorem, 94, 114 Asynchronous policy iteration, 23, 98, 103, 106, 108, 109, 112, 211, 221, 373 Asynchronous value iteration, 91, 112, 211, 221, 259 
B 
Bellman’s equation, 6, 34, 54, 123, 152, 235, 239, 246, 250, 293, 296, 313, 315, 318, 328, 340 Blackmailer’s dilemma, 131 Box condition, 95 
C 
Cauchy sequence, 382 Complete space, 382 Composition of mappings, 379 Continuous-state optimal control, 207, 211, 226, 227, 273, 276, 282, 307, 323, 331 Contraction assumption, 8, 55, 340, 364 Contraction mapping, 8, 46, 335, 381, 385 Contraction mapping fixed-point theorem, 55, 383-387 Contractive models, 29, 55 Controllability, 134, 229, 288, 297, 323 Convergent models, 218, 322 
Cost function, 143 
D 
Disaggregation probability, 20 Discounted MDP, 12, 276 Distributed aggregation, 23, 24 Distributed computation, 23, 40, 43, 374 
E 
"-optimal policy, 57, 234, 238, 241, 244, 255, 279, 290 Error amplification, 69 Error bounds, 59, 61, 64, 68, 73, 76, 85 Euclidean norm, 382 Exponential cost model, 187, 189, 192, 221, 356 
F 
Finite-horizon problems, 235 First passage problem, 16 Fixed point, 382 
G 
Games, dynamic, 13, 109 Gauss-Seidel method, 38, 92, 112 Geometric convergence rate, 384 
H 
Hard aggregation, 21 
I 
Imperfect state information, 222 Improper policy, 16, 128, 129, 180, 198 Interpolated mappings, 335 Interpolation, 109, 219 
J, K 
L 
$-aggregation, 27 $-policy iteration, 27, 77, 90, 111, 162, 261, 321 LSPE($), 27 LSTD($), 27 
401
402 Index 
Least squares approximation, 69 Limited lookahead policy, 61 Linear contraction mappings, 381, 387 Linear-quadratic problems, 40, 134, 205, 298, 323, 327 
M 
MDP, 10, 12, Markov games, 338, 341-343, 346, 353, 361, 373 Markovian decision problem, see MDP Mathematical programming, 117, 164, 325 Minimax problems, 15, 109, 195, 213, 339, 350, 353, 355, 360, 371, 373 Modulus of contraction, 381 Monotone mapping, 379 Monotone decreasing model, 242, 320 Monotone fixed point iterations, 333, 334 Monotone increasing model, 241, 271, 320 Monotonicity assumption, 7, 54, 142 Multiplicative model, 18, 187 Multistep lookahead, 29, 39, 63 Multistep aggregation, 28 Multistep mapping, 27, 46, 47, 49, 51 Multistep methods, 27, 46, 47 
N 
N-stage optimal policy, 234 Negative cost DP model, 45, 242, 320 Neural networks, 25 Neuro-dynamic programming, 25 Newton’s method, 29, 35, 38, 45, 338, 348, 376 Newton-SOR method, 38 Noncontractive model, 45, 233 Nonmonotonic-contractive model, 88, 115 Nonstationary policy, 54, 58 
O 
ODE approach, 112 Oblique projection, 28 Observability, 134, 229, 297, 323 Optimality conditions, 56, 147, 166, 182, 184, 192, 203, 210, 236, 252, 272, 
293, 296, 313 
P 
p-"-optimality, 290 p-stable policy, 286 Parallel computation, 92 Partially asynchronous algorithms, 94 Periodic policies, 64, 110, 113 Perturbations, 171, 185, 206, 228, 229, 286, 309, 329 Policy, 5, 54 Policy, contractive, 190 Policy evaluation, 39, 70, 77, 78, 98, 345, 347, 357, 375 Policy improvement, 39, 70, 98, 153, 345, 347, 357, 375 Policy iteration, 9, 29, 38, 70, 98, 103, 152, 207, 262, 263, 301, 344, 350, 357, 375 Policy iteration, approximate, 73, 118 Policy iteration, asynchronous, 98-109, 112-113, 221 Policy iteration, constrained, 23 Policy iteration, convergence, 70 Policy iteration, modified, 110 Policy iteration, optimistic, 77, 79, 84, 99, 103, 108, 109, 160, 260, 306, 345, 358-362 Policy iteration, perturbations, 174, 185, 220, 303 Policy, multistep lookahead, 29, 38 Policy, noncontractive, 190 Policy, one-step lookahead, 29, 35 Policy, terminating, 197, 209, 288 Positive cost DP model, 45, 242, 320 Projected Bellman equation, 25 Projected equation, 25 Proper policy, 16, 127, 129, 180, 197, 309, 323, 332 Proximal algorithm, 26, 261, 264 Proximal mapping, 27, 48, 261, 264 
Q 
Q-factor, 103 Q-learning, 112 
R 
Reachability, 325 Reduced space implementation, 107
Index 403 
Regular, see S-regular Reinforcement learning, 25, 29, 45, 371, 373 Risk-sensitive model, 18 Robust SSP, 195, 221, 375 Rollout, 25 
S 
SSP problems, 15, 129, 178, 220, 221, 263, 307, 323 S-irregular policy, 122, 144, 165, 171 S-regular collection, 265 S-regular policy, 122, 144 Search problems, 171 Self-learning, 25 Semi-Markov problem, 13 Seminorm projection, 28 Semicontinuity conditions, 181 Semicontractive model, 42, 122, 141, 219 Shortest path problem, 15, 17, 127, 177, 307, 328 Simulation, 28, 39, 43, 92, 372 Spectral radius, 381 Stable policies, 135, 277, 282, 286, 289, 298, 323 Stationary policy, 54, 58 Stochastic shortest path problems, see SSP problems Stopping problems, 104, 108, 299 Strong PI property, 156 Strong SSP conditions, 181 Synchronous convergence condition, 95 
T 
TD($), 27 Temporal di!erences, 26, 27, 261 Terminating policy, 209, 226, 227, 288 Totally asynchronous algorithms, 94 Transient programming problem, 16 
U 
Uniform fixed point, 103, 338, 363, 369 Uniformly N-stage optimal policy, 22 Uniformly proper policy, 317, 323, 332 Unit function, 379 
V 
Value iteration, 9, 29, 36, 66, 67, 91, 
112, 150, 182, 184, 192, 194, 203, 207, 210, 211, 221, 256, 259, 271, 274, 277, 282, 293, 295, 296, 313, 318, 320, 333, 334, 359 Value iteration, asynchronous, 91, 112, 211, 221, 259, 359 Value space approximation, 29, 35, 371 
W 
Weak PI property, 154 Weak SSP conditions, 183 Weighted Bellman equation, 51 Weighted Euclidean norm, 25, 382 Weighted multistep mapping, 51 Weighted sup norm, 55, 352, 385 Weighted sup-norm contraction, 104, 110, 352, 385 Well-behaved region, 147, 266 
X, Y 
Z 
Zero-sum games, 13, 109, 338, 351, 373
Neuro-Dynamic Programming Dimitri P. Bertsekas and John N. Tsitsiklis 
Athena Scientific, 1996 512 pp., hardcover, ISBN 1-886529-10-8 
This is the first textbook that fully explains the neuro-dynamic pro-gramming/reinforcement learning methodology, a breakthrough in the practical application of neural networks and dynamic programming to complex problems of planning, optimal decision making, and intelligent control. 
From the review by George Cybenko for IEEE Computational Sci-ence and Engineering, May 1998: 
“Neuro-Dynamic Programming is a remarkable monograph that integrates a sweeping mathematical and computational landscape into a coherent body of rigorous knowledge. The topics are current, the writing is clear and to the point, the examples are comprehensive and the historical notes and comments are scholarly.” 
“In this monograph, Bertsekas and Tsitsiklis have performed a Her-culean task that will be studied and appreciated by generations to come. I strongly recommend it to scientists and engineers eager to seriously understand the mathematics and computations behind modern behavioral machine learning.” 
Among its special features, the book: 
 Describes and unifies a large number of NDP methods, including several that are new 
 Describes new approaches to formulation and solution of important problems in stochastic optimal control, sequential decision making, and discrete optimization 
 Rigorously explains the mathematical principles behind NDP 
 Illustrates through examples and case studies the practical application of NDP to complex problems from optimal resource allocation, optimal feedback control, data communications, game playing, and combinatorial optimization 
 Presents extensive background and new research material on dynamic programming and neural network training 
Neuro-Dynamic Programming is the winner of the 1997 INFORMS CSTS prize for research excellence in the interface between Op-erations Research and Computer Science
Reinforcement Learning and Optimal Control Dimitri P. Bertsekas 
Athena Scientific, 2019 388 pp., hardcover, ISBN 978-1-886529-39-7 
This book explores the common boundary between optimal control and artificial intelligence, as it relates to reinforcement learning and simu-lation-based neural network methods. These are popular fields with many applications, which can provide approximate solutions to challenging sequential decision problems and large-scale dynamic programming (DP). The aim of the book is to organize coherently the broad mosaic of methods in these fields, which have a solid analytical and logical foundation, and have also proved successful in practice. 
The book discusses both approximation in value space and approximation in policy space. It adopts a gradual expository approach, which proceeds along four directions: 
 From exact DP to approximate DP: We first discuss exact DP algorithms, explain why they may be di!cult to implement, and then use them as the basis for approximations. 
 From finite horizon to infinite horizon problems: We first discuss finite horizon exact and approximate DP methodologies, which are intuitive and mathematically simple, and then progress to infinite horizon problems. 
 From model-based to model-free implementations: We first discuss model-based implementations, and then we identify schemes that can be appropriately modified to work with a simulator. 
The mathematical style of this book is somewhat di"erent from the one of the author’s DP books, and the 1996 neuro-dynamic programming (NDP) research monograph, written jointly with John Tsitsiklis. While we provide a rigorous, albeit short, mathematical account of the theory of finite and infinite horizon DP, and some fundamental approximation methods, we rely more on intuitive explanations and less on proof-based insights. Moreover, our mathematical requirements are quite modest: calculus, a minimal use of matrix-vector algebra, and elementary probability (mathematically complicated arguments involving laws of large numbers and stochastic convergence are bypassed in favor of intuitive explanations). 
The book is supported by on-line video lectures and slides, as well as new research material, some of which has been covered in the present monograph.
Rollout, Policy Iteration, and Distributed Reinforcement Learning 
Dimitri P. Bertsekas 
Athena Scientific, 2020 480 pp., hardcover, ISBN 978-1-886529-07-6 
This book develops in greater depth some of the methods from the author’s Reinforcement Learning and Optimal Control textbook (Athena Scientific, 2019). It presents new research, relating to rollout algorithms, policy iteration, multiagent systems, partitioned architectures, and distributed asynchronous computation. 
The application of the methodology to challenging discrete optimization problems, such as routing, scheduling, assignment, and mixed integer programming, including the use of neural network approximations within these contexts, is also discussed. 
Much of the new research is inspired by the remarkable AlphaZero chess program, where policy iteration, value and policy networks, approximate lookahead minimization, and parallel computation all play an important role. 
Among its special features, the book: 
 Presents new research relating to distributed asynchronous computation, partitioned architectures, and multiagent systems, with application to challenging large scale optimization problems, such as combi-natorial/discrete optimization, as well as partially observed Markov decision problems. 
 Describes variants of rollout and policy iteration for problems with a multiagent structure, which allow the dramatic reduction of the computational requirements for lookahead minimization. 
 Establishes connections of rollout algorithms and model predictive control, one of the most prominent control system design methodology. 
 Expands the coverage of some research areas discussed in the author’s 2019 textbook Reinforcement Learning and Optimal Control. 
 Provides the mathematical analysis that supports the Newton step interpretations and the conclusions of the present book. 
The book is supported by on-line video lectures and slides, as well as new research material, some of which has been covered in the present monograph.