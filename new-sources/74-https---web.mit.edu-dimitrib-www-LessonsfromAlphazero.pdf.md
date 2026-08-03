> Source: https://web.mit.edu/dimitrib/www/LessonsfromAlphazero.pdf

Lessons from AlphaZero for 
Optimal, Model Predictive, and 
Adaptive Control 
by 
Dimitri P. Bertsekas 
Arizona State University and 
Massachusetts Institute of Technology 
WWW site for book information and orders 
http://www.athenasc.com 
Athena Scientific, Belmont, Massachusetts
Athena Scientific Post O!ce Box 805 Nashua, NH 03060 U.S.A. 
Email: info@athenasc.com WWW: http://www.athenasc.com 
c! 2022 Dimitri P. Bertsekas All rights reserved. No part of this book may be reproduced in any form by any electronic or mechanical means (including photocopying, recording, or information storage and retrieval) without permission in writing from the publisher. 
Publisher’s Cataloging-in-Publication Data 
Bertsekas, Dimitri P. Lessons from AlphaZero for Optimal, Model Predictive, and Adaptive Con-trol Includes Bibliography and Index 1. Mathematical Optimization. 2. Dynamic Programming. I. Title. QA402.5 .B465 2020 519.703 00-91281 
ISBN-10: 1-886529-17-5, ISBN-13: 978-1-886529-17-5 
2nd Printing: In this printing, minor typos were corrected, Section 6.5 was expanded to include material on incremental rollout, and small editorial changes were made.
ABOUT THE AUTHOR 
Dimitri Bertsekas studied Mechanical and Electrical Engineering at the National Technical University of Athens, Greece, and obtained his Ph.D. in system science from the Massachusetts Institute of Technology. He has held faculty positions with the Engineering-Economic Systems Department, Stanford University, and the Electrical Engineering Department of the Uni-versity of Illinois, Urbana. Since 1979 he has been teaching at the Electrical Engineering and Computer Science Department of the Massachusetts Insti-tute of Technology (M.I.T.), where he is McAfee Professor of Engineering. In 2019, he joined the School of Computing and Augmented Intelligence at the Arizona State University, Tempe, AZ, as Fulton Professor of Compu-tational Decision Making. 
Professor Bertsekas’ teaching and research have spanned several fields, including deterministic optimization, dynamic programming and stochastic control, large-scale and distributed computation, artificial intelligence, and data communication networks. He has authored or coauthored numerous research papers and nineteen books, several of which are currently used as textbooks in MIT classes, including “Dynamic Programming and Optimal Control,” “Data Networks,” “Introduction to Probability,” and “Nonlinear Programming.” At ASU, he has been focusing in teaching and research in reinforcement learning, and he has developed several textbooks and research monographs in this field since 2019. 
Professor Bertsekas was awarded the INFORMS 1997 Prize for Re-search Excellence in the Interface Between Operations Research and Com-puter Science for his book “Neuro-Dynamic Programming” (co-authored with John Tsitsiklis), the 2001 AACC John R. Ragazzini Education Award, the 2009 INFORMS Expository Writing Award, the 2014 AACC Richard Bellman Heritage Award, the 2014 INFORMS Khachiyan Prize for Life-Time Accomplishments in Optimization, the 2015 MOS/SIAM George B. Dantzig Prize, and the 2022 IEEE Control Systems Award. In 2018 he shared with his coauthor, John Tsitsiklis, the 2018 INFORMS John von Neumann Theory Prize for the contributions of the research monographs “Parallel and Distributed Computation” and “Neuro-Dynamic Program-ming.” Professor Bertsekas was elected in 2001 to the United States Na-tional Academy of Engineering for “pioneering contributions to fundamental research, practice and education of optimization/control theory.”
ATHENA SCIENTIFIC 
OPTIMIZATION AND COMPUTATION SERIES 
1. Lessons from AlphaZero for Optimal, Model Predictive, and Adaptive Control by Dimitri P. Bertsekas, 2022, ISBN 978-1-886529-17-5, 245 pages 
2. Abstract Dynamic Programming, 3rd Edition, by Dimitri P. Bert-sekas, 2022, ISBN 978-1-886529-47-2, 420 pages 
3. Rollout, Policy Iteration, and Distributed Reinforcement Learning, by Dimitri P. Bertsekas, 2020, ISBN 978-1-886529-07-6, 480 pages 
4. Reinforcement Learning and Optimal Control, by Dimitri P. Bert-sekas, 2019, ISBN 978-1-886529-39-7, 388 pages 
5. Dynamic Programming and Optimal Control, Two-Volume Set, by Dimitri P. Bertsekas, 2017, ISBN 1-886529-08-6, 1270 pages 
6. Nonlinear Programming, 3rd Edition, by Dimitri P. Bertsekas, 2016, ISBN 1-886529-05-1, 880 pages 
7. Convex Optimization Algorithms, by Dimitri P. Bertsekas, 2015, ISBN 978-1-886529-28-1, 576 pages 
8. Convex Optimization Theory, by Dimitri P. Bertsekas, 2009, ISBN 978-1-886529-31-1, 256 pages 
9. Introduction to Probability, 2nd Edition, by Dimitri P. Bertsekas and John N. Tsitsiklis, 2008, ISBN 978-1-886529-23-6, 544 pages 
10. Convex Analysis and Optimization, by Dimitri P. Bertsekas, Angelia Nedić, and Asuman E. Ozdaglar, 2003, ISBN 1-886529-45-0, 560 pages 
11. Network Optimization: Continuous and Discrete Models, by Dimitri P. Bertsekas, 1998, ISBN 1-886529-02-7, 608 pages 
12. Network Flows and Monotropic Optimization, by R. Tyrrell Rockafel-lar, 1998, ISBN 1-886529-06-X, 634 pages 
13. Introduction to Linear Optimization, by Dimitris Bertsimas and John N. Tsitsiklis, 1997, ISBN 1-886529-19-1, 608 pages 
14. Parallel and Distributed Computation: Numerical Methods, by Dim-itri P. Bertsekas and John N. Tsitsiklis, 1997, ISBN 1-886529-01-9, 718 pages 
15. Neuro-Dynamic Programming, by Dimitri P. Bertsekas and John N. Tsitsiklis, 1996, ISBN 1-886529-10-8, 512 pages 
16. Constrained Optimization and Lagrange Multiplier Methods, by Dim-itri P. Bertsekas, 1996, ISBN 1-886529-04-3, 410 pages 
17. Stochastic Optimal Control: The Discrete-Time Case, by Dimitri P. Bertsekas and Steven E. Shreve, 1996, ISBN 1-886529-03-5, 330 pages
Contents 
1. AlphaZero, O"-Line Training, and On-Line Play 
1.1. O!-Line Training and Policy Iteration . . . . . . . . . p. 3 1.2. On-Line Play and Approximation in Value Space - . . . . . 
Truncated Rollout . . . . . . . . . . . . . . . . . p. 6 1.3. The Lessons of AlphaZero . . . . . . . . . . . . . . p. 8 1.4. A New Conceptual Framework for Reinforcement Learning p. 11 1.5. Notes and Sources . . . . . . . . . . . . . . . . . p. 14 
2. Deterministic and Stochastic Dynamic Programming Over an Infinite Horizon 
2.1. Optimal Control Over an Infinite Horizon . . . . . . . p. 20 2.2. Approximation in Value Space . . . . . . . . . . . . p. 25 2.3. Notes and Sources . . . . . . . . . . . . . . . . . p. 30 
3. An Abstract View of Reinforcement Learning 
3.1. Bellman Operators . . . . . . . . . . . . . . . . . p. 32 3.2. Approximation in Value Space and Newton’s Method . . p. 39 3.3. Region of Stability . . . . . . . . . . . . . . . . . p. 46 3.4. Policy Iteration, Rollout, and Newton’s Method . . . . p. 50 3.5. How Sensitive is On-Line Play to the O!-Line . . . . . . . 
Training Process? . . . . . . . . . . . . . . . . . . p. 58 3.6. Why Not Just Train a Policy Network and Use it Without . 
On-Line Play? . . . . . . . . . . . . . . . . . . . p. 60 3.7. Multiagent Problems and Multiagent Rollout . . . . . . p. 61 3.8. On-Line Simplified Policy Iteration . . . . . . . . . . p. 66 3.9. Exceptional Cases . . . . . . . . . . . . . . . . . . p. 72 3.10. Notes and Sources . . . . . . . . . . . . . . . . . p. 79 
4. The Linear Quadratic Case - Illustrations 
4.1. Optimal Solution . . . . . . . . . . . . . . . . . . p. 82 4.2. Cost Functions of Stable Linear Policies . . . . . . . . p. 83 4.3. Value Iteration . . . . . . . . . . . . . . . . . . . p. 86 4.4. One-Step and Multistep Lookahead - Newton Step . . . . . 
Interpretations . . . . . . . . . . . . . . . . . . . p. 86 
vii
viii Contents 
4.5. Sensitivity Issues . . . . . . . . . . . . . . . . . . p. 91 4.6. Rollout and Policy Iteration . . . . . . . . . . . . . p. 94 4.7. Truncated Rollout - Length of Lookahead Issues . . . . p. 97 4.8. Exceptional Behavior in Linear Quadratic Problems . . . p. 99 4.9. Notes and Sources . . . . . . . . . . . . . . . . p. 100 
5. Adaptive and Model Predictive Control 
5.1. Systems with Unknown Parameters - Robust and . . . . . . PID Control . . . . . . . . . . . . . . . . . . . p. 102 
5.2. Approximation in Value Space, Rollout, and Adaptive . . . Control . . . . . . . . . . . . . . . . . . . . . p. 105 
5.3. Approximation in Value Space, Rollout, and Model . . . . . Predictive Control . . . . . . . . . . . . . . . . p. 109 
5.4. Terminal Cost Approximation - Stability Issues . . . . p. 112 5.5. Notes and Sources . . . . . . . . . . . . . . . . p. 118 
6. Finite Horizon Deterministic Problems - Discrete Optimiza-tion 
6.1. Deterministic Discrete Spaces Finite Horizon Problems p. 120 6.2. General Discrete Optimization Problems . . . . . . . p. 125 6.3. Approximation in Value Space . . . . . . . . . . . p. 128 6.4. Rollout Algorithms for Discrete Optimization . . . . p. 132 6.5. Rollout and Approximation in Value Space with Multistep . . 
Lookahead . . . . . . . . . . . . . . . . . . . . p. 149 6.6. Constrained Forms of Rollout Algorithms . . . . . . p. 158 6.7. Adaptive Control by Rollout with a POMDP Formulation p. 173 6.8. Rollout for Minimax Control . . . . . . . . . . . . p. 181 6.9. Small Stage Costs and Long Horizon - Continuous-Time . . . 
Rollout . . . . . . . . . . . . . . . . . . . . . p. 190 6.10. Epilogue . . . . . . . . . . . . . . . . . . . . p. 197 
Appendix A: Newton’s Method and Error Bounds 
A.1. Newton’s Method for Di↵erentiable Fixed . . . . . . . . . Point Problems . . . . . . . . . . . . . . . . . . p. 202 
A.2. Newton’s Method Without Di↵erentiability of the . . . . . Bellman Operator . . . . . . . . . . . . . . . . p. 207 
A.3. Local and Global Error Bounds for Approximation in . . . Value Space . . . . . . . . . . . . . . . . . . . p. 210 
A.4. Local and Global Error Bounds for Approximate . . . . . Policy Iteration . . . . . . . . . . . . . . . . . p. 212 
References . . . . . . . . . . . . . . . . . . . . . . . p. 217
Preface 
With four parameters I can fit an elephant, and with five I can make him wiggle his trunk.† 
John von Neumann 
The purpose of this monograph is to propose and develop a new conceptual framework for approximate Dynamic Programming (DP) and Rein-forcement Learning (RL). This framework centers around two algorithms, which are designed largely independently of each other and operate in synergy through the powerful mechanism of Newton’s method. We call these the o↵-line training and the on-line play algorithms; the names are borrowed from some of the major successes of RL involving games. Primary examples are the recent (2017) AlphaZero program (which plays chess), and the similarly structured and earlier (1990s) TD-Gammon program (which plays backgammon). In these game contexts, the o↵-line training algorithm is the method used to teach the program how to evaluate positions and to generate good moves at any given position, while the on-line play algorithm is the method used to play in real time against human or computer opponents. 
† From the meeting of Freeman Dyson and Enrico Fermi (p. 273 of the Segre 
and Hoerlin biography of Fermi, The Pope of Physics, Picador, 2017): “When 
Dyson met with him in 1953, Fermi welcomed him politely, but he quickly put 
aside the graphs he was being shown indicating agreement between theory and 
experiment. His verdict, as Dyson remembered, was “There are two ways of doing 
calculations in theoretical physics. One way, and this is the way I prefer, is to 
have a clear physical picture of the process you are calculating. The other way is 
to have a precise and self-consistent mathematical formalism. You have neither.” 
When a stunned Dyson tried to counter by emphasizing the agreement between 
experiment and the calculations, Fermi asked him how many free parameters he 
had used to obtain the fit. Smiling after being told “Four,” Fermi remarked, “I 
remember my old friend Johnny von Neumann used to say, with four parameters 
I can fit an elephant, and with five I can make him wiggle his trunk.” See also 
the paper by Mayer, Khairy, and Howard [MKH10], which provides a verification 
of the von Neumann quotation. 
ix
x Preface 
Both AlphaZero and TD-Gammon were trained o↵-line extensively using neural networks and an approximate version of the fundamental DP algorithm of policy iteration. Yet the AlphaZero player that was obtained o↵-line is not used directly during on-line play (it is too inaccurate due to approximation errors that are inherent in o↵-line neural network training). Instead a separate on-line player is used to select moves, based on multistep lookahead minimization and a terminal position evaluator that was trained using experience with the o↵-line player. The on-line player performs a form of policy improvement, which is not degraded by neural network approximations. As a result, it greatly improves the performance of the o↵-line player. 
Similarly, TD-Gammon performs on-line a policy improvement step using one-step or two-step lookahead minimization, which is not degraded by neural network approximations. To this end it uses an o↵-line neural network-trained terminal position evaluator, and importantly it also extends its on-line lookahead by rollout (simulation with the one-step lookahead player that is based on the position evaluator). 
Thus in summary: 
(a) The on-line player of AlphaZero plays much better than its extensively trained o↵-line player. This is due to the beneficial e↵ect of exact policy improvement with long lookahead minimization, which corrects for the inevitable imperfections of the neural network-trained o↵-line player, and position evaluator/terminal cost approximation. 
(b) The TD-Gammon player that uses long rollout plays much better than TD-Gammon without rollout. This is due to the beneficial effect of the rollout, which serves as a substitute for long lookahead minimization. 
An important lesson from AlphaZero and TD-Gammon is that the performance of an o↵-line trained policy can be greatly improved by on-line approximation in value space, with long lookahead (involving minimization or rollout with the o↵-line policy, or both), and terminal cost approximation that is obtained o↵-line. This performance enhancement is often dramatic and is due to a simple fact, which is couched on algorithmic mathematics and is the focal point of this work: 
(a) Approximation in value space with one-step lookahead minimization 
amounts to a step of Newton’s method for solving Bellman’s equation. 
(b) The starting point for the Newton step is based on the results of o↵-
line training, and may be enhanced by longer lookahead minimization 
and on-line rollout . 
Indeed the major determinant of the quality of the on-line policy is the Newton step that is performed on-line, while o↵-line training plays a secondary role by comparison.
Preface xi 
Significantly, the synergy between o↵-line training and on-line play also underlies Model Predictive Control (MPC), a major control system design methodology that has been extensively developed since the 1980s. This synergy can be understood in terms of abstract models of infinite horizon DP and simple geometrical constructions, and helps to explain the all-important stability issues within the MPC context. 
An additional benefit of policy improvement by approximation in value space, not observed in the context of games (which have stable rules and environment), is that it works well with changing problem parameters and on-line replanning, similar to indirect adaptive control. Here the Bellman equation is perturbed due to the parameter changes, but approximation in value space still operates as a Newton step. An essential requirement within this context is that a system model is estimated on-line through some identification method, and is used during the one-step or multistep lookahead minimization process. 
In this monograph we will aim to provide insights (often based on visualization), which explain the beneficial e↵ects of on-line decision making on top of o↵-line training. In the process, we will bring out the strong connections between the artificial intelligence view of RL, and the control theory views of MPC and adaptive control. Moreover, we will show that in addition to MPC and adaptive control, our conceptual framework can be e↵ectively integrated with other important methodologies such as multiagent systems and decentralized control, discrete and Bayesian optimization, and heuristic algorithms for discrete optimization. 
One of our principal aims is to show, through the algorithmic ideas of Newton’s method and the unifying principles of abstract DP, that the AlphaZero/TD-Gammon methodology of approximation in value space and rollout applies very broadly to deterministic and stochastic optimal control problems. Newton’s method here is used for the solution of Bellman’s equation, an operator equation that applies universally within DP with both discrete and continuous state and control spaces, as well as finite and infinite horizon. In this connection, we note that the mathematical complications associated with the formalism of Newton’s method for nondi↵erentiable operators have been dealt with in the literature, using sophisticated methods of nonsmooth analysis. We have provided in an appendix a convergence analysis for a finite-dimensional version of Newton’s method, which applies to finite-state problems, but conveys clearly the underlying geometrical intuition and points to infinite-state extensions. We have also provided an analysis for the classical linear-quadratic optimal control problem, the associated Riccati equation, and the application of Newton’s method for its solution. 
While we will deemphasize mathematical proofs in this work, there is considerable related analysis, which supports our conclusions, and can be found in the author’s recent RL books [Ber19a], [Ber20a], and the abstract DP monograph [Ber22a]. In particular, the present work may be viewed as
xii Preface 
a more intuitive, less mathematical, visually oriented exposition of the core material of the research monograph [Ber20a], which deals with approximation in value space, rollout, policy iteration, and multiagent systems. The abstract DP monograph [Ber22a] develops the mathematics that support the visualization framework of the present work, and is a primary resource for followup mathematical research. The RL textbook [Ber19a] provides a more general presentation of RL topics, and includes mathematical proof-based accounts of some of the core material of exact infinite horizon DP, as well as approximate DP. Much of this material is also contained, in greater detail, in the author’s DP textbook [Ber12]. A mix of material contained in these books forms the core of the author’s web-based RL course at ASU. 
This monograph, as well as my earlier RL books, were developed while teaching several versions of my course at ASU over the last four years. Videolectures and slides from this course are available from my website 
http://web.mit.edu/dimitrib/www/RLbook.html 
and provide a good supplement and companion resource to the present book. The hospitable and stimulating environment at ASU contributed much to my productivity during this period, and for this I am very thankful to my colleagues and students for useful interactions. My teaching assistants, Sushmita Bhattacharya, Sahil Badyal, and Jamison Weber, during my courses at ASU have been very supportive. I have also appreciated fruitful discussions with colleagues and students outside ASU, particularly Moritz Diehl, who provided very useful comments on MPC, and Yuchao Li, who proofread carefully the entire book, collaborated with me on research and implementation of various methods, and tested out several algorithmic variants. 
Dimitri P. Bertsekas, 2022 
dimitrib@mit.edu
1 AlphaZero, O!-Line Training, and 
On-Line Play 
Contents 
1.1. O!-Line Training and Policy Iteration . . . . . . . . . p. 3 1.2. On-Line Play and Approximation in Value Space - . . . . . 
Truncated Rollout . . . . . . . . . . . . . . . . . p. 6 1.3. The Lessons of AlphaZero . . . . . . . . . . . . . . p. 8 1.4. A New Conceptual Framework for Reinforcement . . . . . . 
Learning . . . . . . . . . . . . . . . . . . . . . . p. 11 1.5. Notes and Sources . . . . . . . . . . . . . . . . . p. 14 
1
2 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
In this work we will aim to provide a new conceptual framework for reinforcement learning and approximate dynamic programming. These two fields, through the synergy of their ideas in the 1980s and 1990s, and in conjunction of the emergence of machine learning, gave rise to a far-reaching synthesis that would eventually have a major impact on the field of algorithmic optimization. 
In this chapter we provide an outline of the motivation and the algorithmic justification of our framework, and its connection to AlphaZero and related game programs, as well as Newton’s method for solving fixed point problems. In subsequent chapters, we will flesh out our framework, drawing on the theory of abstract DP, related visualizations, ideas of adaptive, model predictive, and linear quadratic control, as well as paradigms from discrete and combinatorial optimization. 
The development of the AlphaZero program by DeepMind Inc, as described in the papers [SHS17], [SSS17], is perhaps the most impressive success story in reinforcement learning (RL) todate. AlphaZero plays Chess, Go, and other games, and is an improvement in terms of performance and generality over the earlier AlphaGo program [SHM16], which plays the game of Go only. AlphaZero, and other chess programs based on similar principles, play as well or better than all competitor computer programs available in 2021, and much better than all humans. These programs are remarkable in several other ways. In particular, they have learned how to play without human instruction, just data generated by playing against themselves. Moreover, they learned how to play very quickly. In fact, Al-phaZero learned how to play chess better than all humans and computer programs within hours (with the help of awesome parallel computation power, it must be said). 
We should note also that the principles of the AlphaZero design have much in common with the TD-Gammon programs of Tesauro [Tes94], [Tes95], [TeG96] that play backgammon (a game of substantial computational and strategical complexity, which involves a number of states estimated to be in excess of 1020). Tesauro’s programs stimulated much interest in RL in the middle 1990s, and one of these programs exhibits similarly di!erent and better play than human backgammon players. A related program for the (one-player) game of Tetris, based on similar principles, is described by Scherrer et al. [SGG15], together with several antecedents, including algorithmic schemes dating to the 1990s, by Tsitsiklis and Van-Roy [TsV96], and Bertsekas and Io!e [BeI96]. The backgammon and Tetris programs, while dealing with less complex games than chess, are of special interest because they involve significant stochastic uncertainty, and are thus unsuitable for the use of long lookahead minimization, which is widely believed to be one of the major contributors to the success of AlphaZero, and chess programs in general. 
Still, for all of their brilliant implementations, these impressive game programs are couched on well established methodology, from optimal and
Sec. 1.1 O!-Line Training and Policy Iteration 3 
suboptimal control, which is portable to far broader domains of engineering, economics, and other fields. This is the methodology of dynamic programming (DP), policy iteration, limited lookahead minimization, rollout, and related approximations in value space. The aim of this work is to propose a conceptual, somewhat abstract framework, which allows insight into the connections of AlphaZero and TD-Gammon with some of the core problems in decision and control, and suggests potentially far-reaching extensions. 
To understand the overall structure of AlphaZero and related programs, and their connections to the DP/RL methodology, it is useful to divide their design into two parts: 
(a) O!-line training, which is an algorithm that learns how to evaluate chess positions, and how to steer itself towards good positions with a default/base chess player. 
(b) On-line play, which is an algorithm that generates good moves in real time against a human or computer opponent, using the training it went through o!-line. 
An important empirical fact is that the on-line player of AlphaZero plays much better than its extensively trained o!-line player . This supports a conceptual idea that applies in great generality and is central in this book, namely that the performance of an o!-line trained policy can be greatly improved by on-line play. We will next briefly describe the o!-training and on-line play algorithms, and relate them to DP concepts and principles, focusing on AlphaZero for the most part. 
1.1 OFF-LINE TRAINING AND POLICY ITERATION 
An o!-line training algorithm like the one used in AlphaZero is the part of the program that learns how to play through self-training that takes place before real-time play against any opponent. It is illustrated in Fig. 1.1.1, and it generates a sequence of chess players and position evaluators . A chess player assigns “probabilities” to all possible moves at any given chess position: these may be viewed as a measure of “e!ectiveness” of the corresponding moves. A position evaluator assigns a numerical score to any given chess position, and thus predicts quantitatively the performance of a player starting from any position. The chess player and the position evaluator are represented by neural networks, a policy network and a value network , which accept as input a chess position and generate a set of move probabilities and a position evaluation, respectively.† 
† Here the neural networks play the role of function approximators. By 
viewing a player as a function that assigns move probabilities to a position, and 
a position evaluator as a function that assigns a numerical score to a position, the policy and value networks provide approximations to these functions based
4 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
Policy Improvement Policy Improvement 
erent! Approximate Value Function Player Features Mappinerent! Approximate Value Function Player Features Mappin 
Self-Learning/Policy Iteration Constraint Relaxation 
Learned from scratch ... with 4 hours of training! Current “ImprovLearned from sc atch ... with 4 hours of training! Current “Improved” Policy Improvement 
Policy Evaluation Improvement of Current Policy 
Neural Network Neural Network 
Value Policy Value Policy 
Figure 1.1.1 Illustration of the AlphaZero o!-line training algorithm. It generates a sequence of position evaluators and chess players. The position evaluator and the chess player are represented by two neural networks, a value network and a policy network, which accept a chess position and generate a position evaluation and a set of move probabilities, respectively. 
In the more conventional DP-oriented terms of this work, a position is the state of the game, a position evaluator is a cost function that gives (an estimate of) the optimal cost-to-go at a given state, and the chess player is a randomized policy for selecting actions/controls at a given state.† 
The overall training algorithm is a form of policy iteration, a DP algorithm that will be of primary interest to us in this work. Starting from a given player, it repeatedly generates (approximately) improved players, and settles on a final player that is judged empirically to be “best” out of all the players generated. Policy iteration may be separated conceptually into two stages (see Fig. 1.1.1). 
(a) Policy evaluation: Given the current player and a chess position, the outcome of a game played out from the position provides a single data point. Many data points are thus collected, and are used to train a value network, whose output serves as the position evaluator for that player. 
on training with data. Actually, AlphaZero uses the same neural network for 
training both value and policy. Thus there are two outputs of the neural net: value and policy. This is pretty much equivalent to having two separate neural 
nets and for the purposes of this work, we prefer to explain the structure as 
two separate networks. AlphaGo uses two separate value and policy networks. Tesauro’s backgammon programs use a single value network, and generate moves 
when needed by one-step or two-step lookahead minimization, using the value network as terminal position evaluator. 
† One more complication is that chess and Go are two-player games, while 
most of our development will involve single-player optimization. While DP theory and algorithms extend to two-player games, we will not discuss these extensions, 
except in a very limited way in Chapter 6. Alternatively, a chess program can 
be trained to play well against a fixed opponent, in which case the framework of single-player optimization applies.
Sec. 1.1 O!-Line Training and Policy Iteration 5 
(b) Policy improvement : Given the current player and its position evaluator, trial move sequences are selected and evaluated for the remainder of the game starting from many positions. An improved player is then generated by adjusting the move probabilities of the current player towards the trial moves that have yielded the best results. 
In AlphaZero (as well as AlphaGo Zero, the version that plays the game of Go) the policy evaluation is done by using deep neural networks. The policy improvement uses a complicated algorithm called Monte Carlo Tree Search (MCTS for short), a form of randomized multistep lookahead minimization that enhances the e"ciency of the multistep lookahead operation, by pruning intelligently the multistep lookahead graph. 
We note, however, that deep neural networks and MCTS, while leading to some performance gains, are not of fundamental importance. The approximation quality that a deep neural network can achieve can also be achieved with a shallow neural network, perhaps with reduced sample efficiency. Similarly MCTS cannot achieve better lookahead accuracy than standard exhaustive search, although it may be more e"cient computationally. Indeed, policy improvement can be done more simply without MCTS, as in Tesauro’s TD-Gammon program: we try all possible move sequences from a given position, extend forward to some number of moves, and then evaluate the terminal position with the current player’s position evaluator. The move evaluations obtained in this way are used to nudge the move probabilities of the current player towards more successful moves, thereby obtaining data that is used to train a policy network that represents the new player.† 
Regardless of the use of deep neural networks and MCTS, it is important to note that the final policy and the corresponding policy evaluation produced by approximate policy iteration and neural network training in AlphaZero involve serious inaccuracies, due to the approximations that are inherent in neural network representations . The AlphaZero on-line player to be discussed next uses approximation in value space with multistep lookahead minimization, and does not involve any neural network, other than the one that has been trained o!-line, so it is not subject to such inaccuracies. As a result, it plays much better than the o!-line player. 
† Quoting from the paper [SSS17] (p. 360): “The AlphaGo Zero selfplay algorithm can similarly be understood as an approximate policy iteration scheme 
in which MCTS is used for both policy improvement and policy evaluation. Policy improvement starts with a neural network policy, executes a MCTS based on that 
policy’s recommendations, and then projects the (much stronger) search policy 
back into the function space of the neural network. Policy evaluation is applied to the (much stronger) search policy: the outcomes of selfplay games are also 
projected back into the function space of the neural network. These projection 
steps are achieved by training the neural network parameters to match the search probabilities and selfplay game outcome respectively.”
6 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
Base Heuristic Truncated Rollout 
Base Heuristic Truncated Rollout 
. . .. . .x0 
Current Position Current Position 
Current Position xk 
O!-Line Obtained Player O 
ON-LINE PLAY 
ON-LINE PLAY 
OFF-LINE TRAINING 
OFF-LINE TRAINING 
ON-LINE PLAY Lookahead Tree States 
ON-LINE PLAY Lookahead Tree States xk+1 
States xk+2 
-Line Obtained Player O!-Line Obtained Cost Approximation 
Adaptive Reoptimization Position EvaluatorWithout the Newton Step Base Player 
With the Newton Step Adaptiv Rollout Cost Approximation 
Figure 1.2.1 Illustration of an on-line player such as the one used in AlphaGo, AlphaZero, and Tesauro’s backgammon program [TeG96]. At a given position, it generates a lookahead graph of multiple moves up to some depth, then runs the o!-line obtained player for some more moves, and evaluates the e!ect of the remaining moves by using the position evaluator of the o!-line player. 
1.2 ON-LINE PLAY AND APPROXIMATION IN VALUE SPACE - TRUNCATED ROLLOUT 
Consider the “final” player obtained through the AlphaZero o!-line training process. It can play against any opponent by generating move probabilities at any position using its o!-line trained policy network, and then simply play the move of highest probability. This player would play very fast on-line, but it would not play good enough chess to beat strong human opponents. The extraordinary strength of AlphaZero is attained only after the player obtained from o!-line training is embedded into another algorithm, which we refer to as the “on-line player.”† In other words AlphaZero plays on-line much better than the best player it has produced with sophisticated o!-line training. This phenomenon, policy improvement through on-line play, is centrally important for our purposes in this work. 
Given the policy network/player obtained o!-line and its value net-work/position evaluator, the on-line algorithm plays roughly as follows (see Fig. 1.2.1). At a given position, it generates a lookahead graph of all possi-
† Quoting from the paper [SSS17] (p. 354): “The MCTS search outputs 
probabilities of playing each move. These search probabilities usually select much 
stronger moves than the raw move probabilities of the neural network.” To elaborate, this statement refers to the MCTS algorithm that is used on line to generate 
the move probabilities at each position encountered in the course of a given game. 
The neural network referred to is trained o!-line, also using in part the MCTS algorithm.
Sec. 1.2 On-Line Play and Approximation in Value Space 7 
ble multiple move and countermove sequences, up to a given depth. It then runs the o!-line obtained player for some more moves, and evaluates the e!ect of the remaining moves by using the position evaluator of the value network. 
The middle portion, called “truncated rollout,” may be viewed as an economical substitute for longer lookahead minimization. Actually truncated rollout is not used in the published version of AlphaZero [SHS17]; the first portion (multistep lookahead minimization) is very long and implemented e"ciently (partly through the use of MCTS), so that the rollout portion is not essential. Rollout has been used in AlphaGo, the AlphaZero predecessor [SHM16]. Moreover, chess and Go programs (including Alp-haZero) typically use a well-known limited form of rollout, called “quiescence search,” which aims to resolve imminent threats and highly dynamic positions through simulated multi-move piece exchanges, before invoking the position evaluator. Rollout is instrumental in achieving high performance in Tesauro’s 1996 backgammon program [TeG96]. The reason is that backgammon involves stochastic uncertainty, so long lookahead minimization is not possible because of rapid expansion of the lookahead graph with every move.† 
In control system design, similar architectures to the ones of Alp-haZero and TD-Gammon are employed in model predictive control (MPC). There, the number of steps in lookahead minimization is called the control interval , while the total number of steps in lookahead minimization and truncated rollout is called the prediction interval ; see e.g., Magni et al. [MDM01]. (The MATLAB toolbox for MPC design explicitly allows the user to choose these two intervals.) The benefit of truncated rollout in providing an economical substitute for longer lookahead minimization is well known within this context. We will discuss further the structure of MPC and its similarities with the AlphaZero architecture in Chapter 5. 
Dynamic programming frameworks with cost function approximations that are similar to the on-line player illustrated in Fig. 1.2.1, are also known as approximate dynamic programming , or neuro-dynamic pro-
† Tesauro’s rollout-based backgammon program [TeG96] uses only a value 
network, which was trained using an approximate policy iteration scheme devel-
oped several years earlier [Tes94]. This network is used to generate moves for the truncated rollout via a one-step or two-step lookahead minimization. Thus the 
value network also serves as a substitute for the policy network during the rollout operation. The position evaluation used at the end of the truncated rollout 
is also provided by the value network. The middle portion of Tesauro’s scheme 
(truncated rollout) is important for achieving a very high quality of play, as it e!ectively extends the length of lookahead from the current position (the player 
with rollout [TeG96] plays much better than the player without rollout [Tes94]). 
In backgammon circles, Tesauro’s program with truncated rollout is viewed as essentially “optimal.”
8 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
gramming , and will be central for our purposes. They will be generically referred to as approximation in value space in this work.† 
Note also that in general, o!-line training and on-line policy implementation may be designed independently of each other. For example the o!-line training portion may be very simple, such as using a known heuristic policy for rollout without truncation, or without terminal cost approximation. Conversely, a sophisticated process may be used for o!-line training of a terminal cost function approximation, which is used following the lookahead minimization in a value space approximation scheme. 
1.3 THE LESSONS OF ALPHAZERO 
The AlphaZero and TD-Gammon experiences reinforce an important conclusion that applies more generally to decision and control problems: despite the extensive o!-line e!ort that may have gone into the design of a policy, performance may be greatly improved by on-line approximation in value space, with extra lookahead involving minimization and/or with rollout using this policy, and terminal cost approximation. 
In the following chapters, we will aim to amplify on this theme and to focus on the principal characteristics of AlphaZero-like architectures, within a broader context of optimal decision and control. We will make use of intuitive visualization, and the central role of Newton’s method for solving Bellman’s equation.‡ Briefly, our central point will be that on-line approximation in value space amounts to a step of Newton’s method for solving Bellman’s equation, while the starting point for the Newton step is based on the results of o!-line training; see Fig. 1.3.1. Moreover, this starting point may be enhanced by several types of on-line operations, including longer lookahead minimization, and on-line rollout with a policy obtained through o!-line training, or heuristic approximations. 
† The names “approximate dynamic programming” and “neuro-dynamic pro-
gramming” are often used as synonyms to RL. However, RL is often thought to 
also subsume the methodology of approximation in policy space, which involves search for optimal parameters within a parametrized set of policies. The search is 
done with methods that are largely unrelated to DP, such as for example stochas-
tic gradient or random search methods (see the author’s RL textbook [Ber19a]). Approximation in policy space may be used o!-line to design a policy that can 
be used for on-line rollout. However, as a methodological subject, approximation in policy space has little connection to the ideas of the present work. 
‡ Bellman’s equation, the centerpiece of infinite horizon DP theory, is viewed 
here as a functional equation, whose solution is the cost of operating the system viewed as a function of the system’s initial state. We will give examples of 
Bellman’s equation in Chapter 2 for discounted and other problems, and we will 
also provide in Chapter 3 abstract forms of Bellman’s equation that apply more generally.
Sec. 1.3 The Lessons of AlphaZero 9 
Starting Point of Newton Step 
Optional On-Line Enhancements to 
Newton Starting Point, e.g. Additional Lookahead 
Minimization or Truncated Rollout 
Newton Step to Solve 
Bellman's Equation 
ON-LINE PLAYOFF-LINE TRAINING O 
NEWTON STEP INTERPRETATION 
Cost Function Approximation Cost Function Approximation 
On-Line Player Cost Function 
On-Line Player Cost Function 
Figure 1.3.1 Illustration of the connections between o!-line training, on-line play, and Newton’s method for solving Bellman’s equation. On-line play is viewed as a Newton step, while o!-line training provides the starting point for the New-ton step. The Newton step starts with a cost approximation J̃ , which may be enhanced on-line by additional lookahead minimization and/or rollout, and produces the cost function of the on-line player. 
This interpretation will be the basis for powerful insights into issues of stability, performance, and robustness of the on-line generated policy. In particular, we will aim to show that feedback control, based on approximation in value space and the underlying o!-line training/on-line play structure, o!ers benefits that go well beyond the conventional wisdom that “feedback corrects for uncertainty, and modeling errors.” The reason is that by overlaying on-line play on top of o!-line training, we gain significantly in performance, by correcting (through the Newton step) for the errors that are inherent in o!-line training with approximation architectures such as neural networks. 
Our mathematical framework is couched on unifying principles of abstract DP, including abstract forms of Bellman’s equation, and the value and policy iteration algorithms (see the author’s books [Ber12], [Ber22a]). However, in this work, we will deemphasize mathematical proofs. There is considerable related analysis, which supports our conclusions and can be found in the author’s recent RL books [Ber19a], [Ber20a]. 
In summary, our discussion will aim to highlight the following points: 
Summary 
(a) Approximation in value space, with one-step lookahead minimization, is an exact step of Newton’s method for solving Bell-man’s equation. This step may be preceded by on-line adjustments and/or value iterations, which enhance its starting point. 
(b) The starting point for the Newton step of (a) is obtained by some unspecified o!-line methodology, which may involve the solution of a related but simpler problem, and/or training with data that makes use of neural networks or feature-based architectures.
10 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
(c) The on-line play and o!-line training parts of the AlphaZero/TD-Gammon design structure correspond to (a) and (b) above, respectively. 
(d) The on-line player of AphaZero plays much better than its deep neural network-trained player for the same reason that the New-ton step (a) improves substantially on its starting point (b), namely the underlying superlinear convergence property that is typical of Newton’s method. 
(e) !-step lookahead minimization can be viewed as one-step lookahead minimization where ! ! 1 value iterations are used to enhance the starting point of the Newton step of (a) above. It is important to perform the first step of the lookahead exactly, but for the last !! 1 steps, approximations may be tolerated. 
(f) The algorithmic processes for (a) and (b) above can be designed by a variety of methods, and independently of each other. For example: 
(1) The implementation of the Newton step (a) may or may not involve any of the following: truncated rollout, online Monte Carlo simulation, MCTS or other e"cient graph search techniques, forms of continuous space optimization, on-line policy iteration, etc. 
(2) The computation of the starting point (b) may or may not involve any of the following: Q-learning, approximate policy iteration based on temporal di!erences or aggregation, neural networks, feature-based function approximation, policies trained o!-line by approximation in policy space, including policy gradient methods or policy random search, etc. Moreover, the details of this computation may vary broadly without a!ecting significantly the e!ectiveness of the overall scheme, which is primarily determined by the Newton step (a). 
(g) An e"cient implementation of the Newton step (a) is often critical in order to meet real-time constraints for generating controls, and to allow longer lookahead minimization, which enhances the starting point of the Newton step and its performance. By contrast, o!-line training algorithms used for (b) have much less stringent real-time constraints, and the issues of sample e"ciency and fine tuned performance, while important, are not critical. 
(h) The e"cient implementation of the Newton step may benefit from the use of distributed computation and other simplifications. A case in point is multiagent problems, which we will discuss later (see Chapter 3).
Sec. 1.3 The Lessons of AlphaZero 11 
(i) Approximation in value space addresses e!ectively issues of robustness and on-line replanning for problems with changing parameters. The mechanism is similar to the one of indirect adaptive control: changing problem parameters are estimated on-line and a Newton step is used in place of an expensive full reoptimization of the controller. In the presence of changing parameters, the Bellman equation changes, but the Newton step itself remains powerful and aims at the optimal solution that corresponds to the estimated system parameters. 
(j) Model predictive control (MPC) has a conceptually similar structure to the AlphaZero-like programs, and entails an on-line play component involving multistep lookahead minimization, forms of truncated rollout, and an o!-line training component to construct terminal cost approximations, and “safe” state space regions or reachability tubes to deal with state constraints. The success of MPC may be attributed to these similarities and to its resilience to changing problem parameters as per (i) above. 
(k) On-line rollout with a stable policy yields a good starting point for the Newton step (a): it improves the stability properties of the policy obtained by approximation in value space, and provides an economical substitute for long lookahead minimization. 
(l) Because the ideas outlined above are couched on principles of DP that often hold for arbitrary state and control spaces, they are valid within very general contexts: continuous-spaces control systems, discrete-spaces Markov decision problems, control of hybrid systems, decision making in multiagent systems, and discrete and combinatorial optimization. 
The preceding points are meant to highlight the essence of the connections between AlphaZero and TD-Gammon, approximation in value space, and decision and control. Naturally in practice there are exceptions and modifications, which need to be worked out in the context of particular applications, under appropriate assumptions. Moreover, while some results and elaborations are available through the research that has been done on approximate DP and on MPC, several of the results suggested by the analysis and insights of the present work remain to be rigorously established and enhanced within the context of specific problems. 
1.4 A NEW CONCEPTUAL FRAMEWORK FOR REINFORCEMENT LEARNING 
In this work we will emphasize the distinct roles of o!-line training and online play algorithms within the structure of approximate sequential decision
12 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
making and approximation in value space schemes. In doing so, we will aim for a new conceptual framework for RL, which is based on the synergism and complementarity of o!-line training and on-line play, and the analytical framework of Newton’s method. 
We will implicitly assume that the time available for o!-line training is very long (practically limitless), but that the problem at hand is such that exact DP algorithms, like policy iteration and Q-learning, are impossible for one (or both) of the following two reasons: 
(a) There are too many states (either an infinite number as in continuous space problems, or very large as in chess). As a result a lookup table representation of policies, value functions, and/or Q-factors is impossible, and the only practical alternative is a compact representation, via a neural network or some other approximation architecture. 
(b) The system model is changing over time as in adaptive control, so even if an exactly optimal policy is computed o!-line under some nominal problem assumptions, it becomes suboptimal when the problem parameters change. 
In this work, we will not discuss training algorithms and their associated sample e"ciency issues, and we will refer to the many available sources, including the author’s RL books [Ber19a], [Ber20a]. 
On the other hand, we will assume that there is limited time for on-line decision making, because of hard practical constraints on the real time that is available between decisions. These constraints are highly problem dependent: for some problems, following the observation of the state, we may need to produce the next decision within a fraction of a second, whereas for others we may have hours at our disposal. We will assume that whatever time is available, it will be used to provide quite accurate (nearly exact) one-step or multistep lookahead minimization, and time permitting, to extend as much as possible the combined length of the lookahead minimization and the truncated rollout with an o!-line computed policy. We will thus implicitly take it as given that longer (as well as more accurate) lookahead minimization is better for the performance of the policy obtained,† although the division of e!ort between lookahead minimization and truncated rollout with a policy is a design decision that may depend on the circumstances. Note that parallel and distributed computation can play an important role in mitigating practical on-line time constraints. 
The central fact in our conceptual framework is that approximation in value space with one-step lookahead minimization constitutes a single Newton step for solving Bellman’s equation. Contrary to other Newton-like steps that may have been part of the o!-line training process, this 
† It is possible to construct artificial problems, where longer lookahead results 
in worse performance (see [Ber19a], Section 2.2), but such problems are rare in practice.
Sec. 1.4 A New Conceptual Framework 13 
single Newton step is accurate: all the approximation has been shifted to its starting point . Moreover, the Newton step can be very powerful, and its starting point can be enhanced by multistep lookahead minimization or by truncated rollout. From an algorithmic point of view, the Newton step converges superlinearly without the need for di!erentiability of the Bellman operator T : it takes advantage of the monotonicity and concavity structure of T (see the Appendix, where we will discuss Newton’s method without di!erentiability assumptions). 
To summarize, both o!-line training and on-line play are subject to fundamental limits: the former’s limit is the constrained power of the approximation architecture, while the latter’s limit is the constrained on-line computation time. The former limit cannot be easily overcome, but the latter limit can be stretched a lot thanks to the power of the Newton step, supplemented by long lookahead minimization and truncated rollout, as well as through the use of parallel and distributed computation. 
Our design philosophy in a nutshell is the following: 
(1) The major determinant of the quality of the controller obtained by our schemes is the Newton step that is performed on-line. Stated somewhat bluntly, o!-line training is secondary by comparison, in the sense that without on-line one-step or multistep lookahead minimization, the quality of the policy obtained by o!-line training alone is often unacceptably poor. In particular, whether done by neural networks, feature-based linear architectures, temporal di!erence methods, aggregation, policy gradient, policy random search, or whatever other reasonable approach, o!-line training principally serves the purpose of providing a good or reasonable starting point for the Newton step. This is the principal lesson from AlphaZero and TD-Gammon in our view. This philosophy also underlies MPC, where on-line lookahead minimization has traditionally been the principal focus, perhaps supplemented by truncated rollout, with o!-line calculations playing a limited subsidiary role.† 
(2) The Newton step is often powerful enough to smooth out di!erences in various o!-line training methods. In particular, methods such as TD(") with di!erent values of ", policy gradient, linear programming, etc, all give di!erent, but more or less equally good starting points for the Newton step. The conclusion from this is that o!-line training with a very large number of samples, and sophisticated ways to improve sample e"ciency may not be very useful, beyond a certain point, because gains in e"ciency and accuracy tend to be washed up by the Newton step. 
† Incidentally, this is a major reason why there is an apparent disconnect 
between the MPC community, which is mostly focused on on-line play, and the RL community, which is mostly focused on o!-line training.
14 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
(3) The on-line Newton step also works well in the context of adaptive control, as long as it is calculated on the basis of the currently correct model parameters (so this requires an on-line parameter identification algorithm). The reason is that when problem parameters change, the Bellman operator changes, but the Newton step is executed on the basis of the correct Bellman operator. This is also a principal reason why MPC schemes have been used with success in adaptive control contexts. 
We will return to these points repeatedly in the course of our presentation. 
1.5 NOTES AND SOURCES 
The theory of DP dates to the late 40s and 50s, and provides the foundation for our subject. Indeed RL may be viewed as an approximate form of the exact DP methodology. The author’s DP textbook [Ber17a] provides an extensive discussion of finite horizon DP, and its applications to discrete and continuous spaces problems, using a notation and style that is consistent with the present book. The books by Puterman [Put94] and by the author [Ber12] provide detailed treatments of infinite horizon finite-state Markovian decision problems. 
Continuous spaces infinite horizon problems are covered in the author’s book [Ber12], while some of the more complex mathematical aspects of exact DP are discussed in the monograph by Bertsekas and Shreve [BeS78] (particularly the probabilistic/measure-theoretic issues associated with stochastic optimal control).† 
† The rigorous mathematical theory of stochastic optimal control, including the development of an appropriate measure-theoretic framework, dates to the 60s and 70s. It culminated in the monograph [BeS78], which provides the now “standard” framework, based on the formalism of Borel spaces, lower semianalytic functions, and universally measurable policies. This development involves daunting mathematical complications, which stem, among others, from the fact that when a Borel measurable function F (x, u), of the two variables x and u, is minimized with respect to u, the resulting function 
G(x) = min u 
F (x, u) 
need not be Borel measurable (it is lower semianalytic). Moreover, even if the minimum is attained by several functions/policies µ, i.e., G(x) = F 
! 
x,µ(x) " 
for all x, it is possible that none of these µ is Borel measurable (however, there does exist a minimizing policy that belongs to the broader class of universally measurable policies). Thus, starting with a Borel measurability framework for cost functions and policies, we quickly get outside that framework when executing DP algorithms, such as value and policy iteration. The broader framework of universal measurability is required to correct this deficiency, in the absence of additional (fairly strong) assumptions.
Sec. 1.5 Notes and Sources 15 
The third edition of the author’s abstract DP monograph [Ber22a], expands on the original 2013 first edition, and aims at a unified development of the core theory and algorithms of total cost sequential decision problems. It addresses simultaneously stochastic, minimax, game, risk-sensitive, and other DP problems, through the use of abstract DP operators (or Bellman operators as they are often called in RL). The abstract framework is important for some the visualization insights and the connections to Newton’s method that are central for the purposes of this book. 
The approximate DP and RL literature has expanded tremendously since the connections between DP and RL became apparent in the late 1980s and early 1990s. In what follows, we will provide a list of textbooks, research monographs, and broad surveys, which supplement our discussions, express related viewpoints, and collectively provide a guide to the literature. 
RL Textbooks 
Two books were written in the 1990s, setting the tone for subsequent developments in the field. One in 1996 by Bertsekas and Tsitsiklis [BeT96], which reflects a decision, control, and optimization viewpoint, and another in 1998 by Sutton and Barto, which reflects an artificial intelligence viewpoint (a 2nd edition, [SuB18], was published in 2018). We refer to the former book and also to the author’s DP textbooks [Ber12], [Ber17a] for a broader discussion of some of the topics of this book, including algorithmic convergence issues and additional DP models, such as those based on average cost and semi-Markov problem optimization. Note that both of these books deal with finite-state Markov decision models and use a transition probability notation, as they do not address continuous spaces problems, which are also of major interest in this book. 
More recent books are by Gosavi [Gos15] (a much expanded 2nd edition of his 2003 monograph), which emphasizes simulation-based optimization and RL algorithms, Cao [Cao07], which focuses on a sensitivity approach to simulation-based methods, Chang, Fu, Hu, and Mar-
The monograph [BeS78] provides an extensive treatment of these issues, 
while Appendix A of the DP textbook [Ber12] provides a tutorial introduction. The followup work by Huizhen Yu and the author [YuB15] resolves the special 
measurability issues that relate to policy iteration, and provides additional analysis relating to value iteration. In the RL literature, the mathematical di"culties 
around measurability are usually neglected (as they are in the present book), and 
this is fine because they do not play an important role in applications. Moreover, measurability issues do not arise for problems involving finite or countably infinite 
state and control spaces. We note, however, that there are quite a few published 
works in RL as well as exact DP, which purport to address measurability issues with a mathematical narrative that is either confusing or plain incorrect.
16 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
cus [CFH13] (a 2nd edition of their 2007 monograph), which emphasizes finite-horizon/multistep lookahead schemes and adaptive sampling, Buso-niu, Babuska, De Schutter, and Ernst [BBD10a], which focuses on function approximation methods for continuous space systems and includes a discussion of random search methods, Szepesvari [Sze10], which is a short monograph that selectively treats some of the major RL algorithms such as temporal di!erence methods, armed bandit methods, and Q-learning, Pow-ell [Pow11], which emphasizes resource allocation and operations research applications, Powell and Ryzhov [PoR12], which focuses on specialized topics in learning and Bayesian optimization, Vrabie, Vamvoudakis, and Lewis [VVL13], which discusses neural network-based methods and on-line adaptive control, Kochenderfer et al. [KAC15], which selectively discusses applications and approximations in DP, and the treatment of uncertainty, Jiang and Jiang [JiJ17], which addresses adaptive control and robustness issues within an approximate DP framework, Liu, Wei, Wang, Yang, and Li [LWW17], which deals with forms of adaptive dynamic programming, and topics in both RL and optimal control, and Zoppoli, Sanguineti, Gnecco, and Parisini [ZSG20], which addresses neural network approximations in optimal control as well as multiagent/team problems with nonclassical information patterns. 
There are also several books that, while not exclusively focused on DP and/or RL, touch upon several of the topics of this book. The book by Borkar [Bor08] is an advanced monograph that addresses rigorously many of the convergence issues of iterative stochastic algorithms in approximate DP, mainly using the so called ODE approach. The book by Meyn [Mey07] is broader in its coverage, but discusses some of the popular approximate DP/RL algorithms. The book by Haykin [Hay08] discusses approximate DP in the broader context of neural network-related subjects. The book by Krishnamurthy [Kri16] focuses on partial state information problems, with discussion of both exact DP, and approximate DP/RL methods. The textbooks by Kouvaritakis and Cannon [KoC16], Borrelli, Bemporad, and Morari [BBM17], and Rawlings, Mayne, and Diehl [RMD17] collectively provide a comprehensive view of the MPC methodology. The book by Lat-timore and Szepesvari [LaS20] is focused on multiarmed bandit methods. The book by Brandimarte [Bra21] is a tutorial introduction to DP/RL that emphasizes operations research applications and includes MATLAB codes. The book by Hardt and Recht [HaR21] focuses on broader subjects of machine learning, but covers selectively approximate DP and RL topics as well. 
The present book is similar in style, terminology, and notation to the author’s recent RL textbooks [Ber19a], [Ber20a], and the 3rd edition of the abstract DP monograph [Ber22a], which collectively provide a fairly comprehensive account of the subject. In particular, the 2019 RL textbook includes a broader coverage of approximation in value space methods, including certainty equivalent control and aggregation methods. It
Sec. 1.5 Notes and Sources 17 
also covers substantially policy gradient methods for approximation in policy space, which we will not address here. The 2020 book focuses more closely on rollout, policy iteration, and multiagent problems. The abstract DP monograph [Ber22a] is an advanced treatment of exact DP, which also connects with intuitive visualizations of Bellman’s equation and related algorithms. The present book is less mathematical and more conceptual in character. It focuses on the connection of approximation in value space with Newton’s method, relying on analysis first provided in the book [Ber20a] and the paper [Ber22b], as well as on visualizations of abstract DP ideas from the book [Ber22a]. 
Surveys and Short Research Monographs 
In addition to textbooks, there are many surveys and short research monographs relating to our subject, which are rapidly multiplying in number. Influential early surveys were written, from an artificial intelligence viewpoint, by Barto, Bradtke, and Singh [BBS95] (which dealt with the methodologies of real-time DP and its antecedent, real-time heuristic search [Kor90], and the use of asynchronous DP ideas [Ber82], [Ber83], [BeT89] within their context), and by Kaelbling, Littman, and Moore [KLM96] (which focused on general principles of RL). The volume by White and Sofge [WhS92] also contains several surveys describing early work in the field. 
Several overview papers in the volume by Si, Barto, Powell, and Wun-sch [SBP04] describe some approximation methods that we will not be covering in much detail in this book: linear programming approaches (De Farias [DeF04]), large-scale resource allocation methods (Powell and Van Roy [PoV04]), and deterministic optimal control approaches (Ferrari and Stengel [FeS04], and Si, Yang, and Liu [SYL04]). Updated accounts of these and other related topics are given in the survey collections by Lewis, Liu, and Lendaris [LLL08], and Lewis and Liu [LeL13]. 
Recent extended surveys and short monographs are Borkar [Bor09] (a methodological point of view that explores connections with other Monte Carlo schemes), Lewis and Vrabie [LeV09] (a control theory point of view), Szepesvari [Sze10] (which discusses approximation in value space from a RL point of view), Deisenroth, Neumann, and Peters [DNP11], and Grond-man et al. [GBL12] (which focus on policy gradient methods), Browne et al. [BPW12] (which focuses on Monte Carlo Tree Search), Mausam and Kolobov [MaK12] (which deals with Markov decision problems from an artificial intelligence viewpoint), Schmidhuber [Sch15], Arulkumaran et al. [ADB17], Li [Li17], Busoniu et al. [BDT18], the author’s [Ber05] (which focuses on rollout algorithms and model predictive control), [Ber11] (which focuses on approximate policy iteration), and [Ber18b] (which focuses on aggregation methods), and Recht [Rec18] (which focuses on continuous spaces optimal control).
18 AlphaZero, O!-Line Training, and On-Line Play Chap. 1 
Research Content of this Book 
The research focus of this book is to propose and develop a new conceptual framework, which the author believes is fundamental within the context of DP-based RL methodology. This framework centers around the division of the design process of an RL scheme into the o!-line training and the online play algorithms, and shows that these algorithms operate in synergy through the powerful mechanism of Newton’s method. 
The style of the book is di!erent than the style of the author’s more mathematically oriented RL books [Ber19a] and [Ber20a], and abstract DP book [Ber22a]. In particular, the present book emphasizes insights through visualization rather than rigorous proofs. At the same time, the book makes careful distinctions between provable and speculative claims. By highlighting the exceptional behavior that may occur, the book also aims to emphasize the need for serious mathematical research and experimentation into broad classes of problems, beyond the relatively well-behaved finite horizon and discounted/contractive problems. 
Book Organization 
The book is structured as follows. In Chapter 2, we review the theory of classical infinite horizon optimal control problems, in order to provide some orientation and an analytical platform for what follows in subsequent chapters. In Chapter 3, we introduce an abstract DP framework that will set the stage for the conceptual and visual interpretations of approximation in value space in terms of Newton’s method. In this chapter, we also present new research relating to on-line policy iteration, which aims to improve the on-line approximation in value space algorithm by using training data that is collected on-line. In Chapter 4, we illustrate our analysis within the simple and intuitive framework of linear quadratic problems, which admit visualizations through the Riccati equation operators. In Chapter 5, we discuss various issues of changing problem parameters, adaptive control, and MPC. In Chapter 6, we extend the ideas of earlier chapters to finite horizon problems and discrete optimization, with a special focus on rollout algorithms and their variations. This chapter also includes a section on approximation in value space schemes for deterministic continuous-time optimal control. Finally, in the Appendix, we outline the convergence theory of Newton’s method, and explain how the theory applies to nondi!erentiable fixed point problems, such as the solution of Bellman’s equation in DP. We also describe how the connection with Newton’s method can be used to derive new and more realistic error bounds for approximation in value space and approximate policy iteration.
2 Deterministic and Stochastic 
Dynamic Programming 
Contents 
2.1. Optimal Control Over an Infinite Horizon . . . . . . . p. 20 2.2. Approximation in Value Space . . . . . . . . . . . . p. 25 2.3. Notes and Sources . . . . . . . . . . . . . . . . . p. 30 
19
20 Deterministic and Stochastic Dynamic Programming Chap. 2 
...... ) xk xk+1) x0 
Random Transition 
) Random Cost 
xk+1 = f(xk, uk, wk) 
) !kg(xk, uk, wk) 
Termination State Infinite Horizon 
Figure 2.1.1 Illustration of an infinite horizon problem. The system and cost per stage are stationary, except for the use of a discount factor !. If ! = 1, there is typically a special cost-free termination state that we aim to reach. 
In this chapter we will describe a classical framework of optimal control over an infinite horizon. We will use it as a principal example for a more abstract DP framework to be introduced in Chapter 3. This abstract framework will be used in turn as the starting point for our analysis and visualization of algorithmic issues, relating to approximation in value space, multistep lookahead, controller stability, truncated rollout, and policy iteration. Note that finite horizon problems can be converted to the infinite horizon format of this chapter, as will be discussed in Chapter 6. 
2.1 OPTIMAL CONTROL OVER AN INFINITE HORIZON 
Let us consider a familiar class of stochastic optimal control problems over an infinite horizon (see Fig. 2.1.1). We have a stationary system of the form 
xk+1 = f(xk, uk, wk), k = 0, 1, . . . , 
where xk is an element of some state space X and the control uk is an element of some control space U ; see Fig. 2.1.1. The system includes a random “disturbance” wk, taking values in some space W , with a probability distribution P (· | xk, uk) that may depend explicitly on xk and uk, but not on values of prior disturbances wk!1, . . . , w0.† The control uk is constrained to take values in a given subset U(xk) ! U , which depends on the current state xk. We are interested in policies ! = {µ0, µ1, . . .}, such that each function µk maps states into controls, and satisfies µk(xk) " U(xk) for all k. A stationary policy of the form {µ, µ, . . .} will also be referred to as “policy µ.” We make no assumptions on the state, control, and disturbances, and indeed for most of the discussion of this work, these spaces can be arbitrary. 
We aim to minimize the expected total cost over an infinite number of stages, given by 
J!(x0) = lim N"# 
E 
! 
N!1 " 
k=0 
"kg # 
xk, µk(xk), wk 
$ 
% 
, (2.1) 
† We assume an introductory probability background on the part of the reader. For an account that is consistent with our use of probability in this 
book, see the text by Bertsekas and Tsitsiklis [BeT08].
Sec. 2.1 Optimal Control Over an Infinite Horizon 21 
where "kg(xk, uk, wk) is the cost of stage k, and " " (0, 1] is a discount factor. If " = 1 we refer to the problem as undiscounted. The expected value in Eq. (2.1) is taken with respect to the random disturbances wk, k = 0, 1, . . .. Here, J!(x0) denotes the cost associated with an initial state x0 and a policy ! = {µ0, µ1, . . .}. The cost function of a stationary policy µ is denoted by Jµ. The optimal cost starting at state x, inf! J!(x), is denoted by J*(x), and the function J* is referred to as the optimal cost function. 
Let us consider some special cases, which will be of primary interest in this work: 
(a) Stochastic shortest path problems (SSP for short). Here, " = 1 but there is a special cost-free termination state, denoted by t; once the system reaches t it remains there at no further cost. Usually, the termination state t represents a goal state that we are trying to reach at minimum cost; these are problems where the cost per stage is nonnegative, and will be of primary interest in this work. In some other types of problems, t may be a state that we are trying to avoid for as long as possible; these are problems where the cost per stage is nonpositive, and will not be specifically discussed in this work. 
(b) Discounted stochastic problems . Here, " < 1 and there need not be a termination state. However, there is a substantial connection between SSP and discounted problems. Aside from the fact that they are both infinite horizon total cost optimization problems, a discounted problem can be readily converted to an SSP problem. This can be done by introducing an artificial termination state to which the system moves with probability 1#" at every state and stage, thus making termination inevitable. Thus SSP and discounted problems share qualitative similarities in their respective theories. 
(c) Deterministic nonnegative cost problems . Here, the disturbance wk 
takes a single known value. Equivalently, there is no disturbance in the system equation and the cost expression, which now take the form 
xk+1 = f(xk, uk), k = 0, 1, . . . , (2.2) 
and 
J!(x0) = lim N"# 
N!1 " 
k=0 
"kg # 
xk, µk(xk) $ 
. (2.3) 
We assume further that there is a cost-free and absorbing termination state t, and we have 
g(x, u) $ 0, for all x %= t, u " U(x), (2.4) 
and g(t, u) = 0 for all u " U(t). This type of structure expresses the objective to reach or approach t at minimum cost, a classical control
22 Deterministic and Stochastic Dynamic Programming Chap. 2 
problem. An extensive analysis of the undiscounted version of this problem was given in the author’s paper [Ber17b]. An important special case is finite-state deterministic problems . Fi-nite horizon versions of these problems include challenging discrete optimization problems, whose exact solution is practically impossible. It is possible to transform such problems to infinite horizon SSP problems, so that the conceptual framework developed here applies (see Chapter 6). The approximate solution of discrete optimization problems by RL methods, and particularly by rollout, has been discussed at length in the books [Ber19a] and [Ber20a]. Another important deterministic nonnegative cost problem is the classical continuous spaces problem where the system is linear, with no control constraints, and the cost function is quadratic; see the following example. We will often refer to this problem and its extensions in what follows. 
Example 2.1.1 (Linear Quadratic Problems) 
Assume that the system is linear of the form 
xk+1 = Axk +Buk, (2.5) 
where xk and uk are elements of the Euclidean spaces !n and !m, respectively, A is an n"n matrix, and B is an n"m matrix. We assume that there are no control constraints. The cost per stage is quadratic of the form 
g(x, u) = x!Qx+ u!Ru, (2.6) 
where Q and R are positive definite symmetric matrices of dimensions n" n and m"m, respectively (all finite-dimensional vectors in this work are viewed as column vectors, and a prime denotes transposition). It is well known that this problem admits a nice analytical solution, which we will discuss shortly, and we will use later for illustrations, examples, and counterexamples (see also [Ber17a], Section 3.1). 
Infinite Horizon Methodology 
Many of the analytical and computational issues regarding infinite horizon problems revolve around the relation between the optimal cost function J* of the problem and the optimal cost function of the corresponding N -stage problem. In particular, let JN (x) denote the optimal cost of the problem involving N stages, initial state x, cost per stage g(x, u, w), and zero terminal cost. This cost is generated at the Nth iteration of the value iteration algorithm (VI for short) 
Jk+1(x) = min u$U(x) 
E 
& 
g(x, u, w)+"Jk # 
f(x, u, w) $ 
' 
, k = 0, 1, . . . , (2.7)
Sec. 2.1 Optimal Control Over an Infinite Horizon 23 
starting from J0(x) & 0 (see Chapter 6). It is natural to speculate the following three basic properties:† 
(1) The optimal infinite horizon cost is the limit of the corresponding N -stage optimal costs as N ' (: 
J*(x) = lim N"# 
JN (x) (2.8) 
for all states x. 
(2) Bellman’s equation holds: 
J*(x) = min u$U(x) 
E 
& 
g(x, u, w)+"J* # 
f(x, u, w) $ 
' 
, for all x. (2.9) 
This equation can be viewed as the limit as k ' ( of the VI algorithm (2.7), assuming property (1) above holds and guarantees that Jk(x) ' J*(x) for all x. There is also a Bellman equation for each stationary policy µ. It is given by 
Jµ(x) = E 
& 
g # 
x, µ(x), w $ 
+ "Jµ # 
f(x, µ(x), w) $ 
' 
, for all x, 
(2.10) where Jµ is the cost function of µ. We can view this as just the Bellman equation (2.9) for a di!erent problem, where for each x, the control constraint set U(x) consists of just one control, namely µ(x). 
(3) If µ(x) attains the minimum in the right-hand side of the Bellman equation (2.9) for each x, then the stationary policy µ should be optimal. 
All three of the preceding results hold for discounted problems, provided the expected cost per stage E 
( 
g(x, u, w) ) 
is bounded over the set of possible values of (x, u, w) (see the DP book [Ber12], Chapter 1). They also hold for finite-state SSP problems under reasonable assumptions. For deterministic problems with possibly infinite state and control spaces, there is substantial analysis that provides assumptions under which the results (1)-(3) above hold (see e.g., [Ber12]). 
The VI algorithm is also typically valid, in the sense that Jk ' J*, even if the initial function J0 is nonzero. The motivation for a di!erent choice of J0 is faster convergence to J*; generally the convergence is faster as J0 is chosen closer to J*. The intuitive interpretation of the Bellman equation (2.9) is that it is the limit as k ' ( of the VI algorithm (2.7) assuming that Jk ' J*. The optimality condition (3) indicates that optimal and near optimal policies can be obtained from within the class of 
† Throughout this work, we will be using “min” instead of the more formal “inf,” even if we are not sure that the minimum is attained.
24 Deterministic and Stochastic Dynamic Programming Chap. 2 
stationary policies, something that is generally true for the problems that we discuss in this work, and that we will implicitly assume in what follows. 
Aside from the VI algorithm, another fundamental algorithm is policy iteration (PI for short), which will be discussed in Section 3.3. It is much faster than VI, and in practice it often requires a handful of iterations, independently of the problem size. An explanation is that PI can be viewed as Newton’s method for solving Bellman’s equation, as we will explain in Section 3.3. This connection with Newton’s method extends to approximate forms of PI, and is central for our purposes in this book. 
The author’s paper [Ber17b], and also the abstract DP book [Ber22a], provide a detailed analysis of the undiscounted special case of the problem (2.2)-(2.4), where there is a cost-free and absorbing termination state t, the cost function is strictly positive for all other states, as in Eq. (2.4), and the objective is to reach or asymptotically approach the termination state. This analysis covers the preceding four properties, as well as the issue of convergence of PI, for the case of general state and control spaces (continuous or discrete or a mixture thereof). It delineates conditions under which favorable properties can be guaranteed. 
Example 2.1.1 (Linear Quadratic Problems - Continued) 
Consider again the linear quadratic problem defined by Eqs. (2.5)-(2.6). The Bellman equation is given by 
J(x) = min u"#m 
( 
x!Qx+ u!Ru+ J(Ax+Bu) ) 
, (2.11) 
and turns out to have a unique solution within the space of quadratic functions of the form 
J(x) = x!Kx, (2.12) 
where K is a positive semidefinite symmetric matrix [under our positive definiteness assumption on Q and R, and an additional controllability assumption on the system (2.5); see [Ber17a], Section 3.1]. This unique solution can be shown to be the optimal cost function of the problem, and has the form 
J$(x) = x!K$x. (2.13) 
We can obtain K$ by solving the matrix equation 
K = F (K), (2.14) 
with F (K) defined over symmetric matrices K by 
F (K) = A! # 
K #KB(B!KB +R)%1B!K $ 
A+Q. (2.15) 
The optimal policy is obtained by minimization in the Bellman equation (2.11) when J is replaced by the optimal cost function J$ of Eq. (2.13). It can be verified that it is linear of the form 
µ$(x) = Lx,
Sec. 2.2 Approximation in Value Space 25 
where L is the matrix 
L = #(B!K$B +R)%1B!K$A. 
The VI and PI algorithms are known to have favorable properties for our linear quadratic problem. In particular, the VI algorithm can be executed within the space of positive semidefinite symmetric matrices. The VI algorithm Jk+1 = TJk, when Jk has the form Jk(x) = x!Kkx, yields for all x, 
Jk+1(x) = x!Kk+1x with Kk+1 = F (Kk), (2.16) 
where F is given by Eq. (2.15). It can be shown that the sequence {Kk} converges to the optimal matrix K$ starting from any positive semidefinite symmetric matrix K0 under the assumptions mentioned earlier. The PI algorithm also has favorable convergence properties (under the same assumptions) and its important connection with Newton’s method will be discussed later. 
The preceding results are well known and they are given with proofs in several control theory texts, including the author’s DP books [Ber17a], Chapter 3, and [Ber12], Chapter 4.† The equation K = F (K) is known as the Riccati equation.‡ It can be viewed as the Bellman equation restricted to the subspace of quadratic functions of the form (2.12). Note that the Riccati equation can be shown to have solutions other than K$ (which necessarily are not positive definite symmetric). Illustrative examples will be given later. 
2.2 APPROXIMATION IN VALUE SPACE 
A principal RL approach to deal with the often intractable exact computation of J* is approximation in value space. Here in place of J*, we use an approximation J̃ , and generate at any state x, a control µ̃(x) by the one-step lookahead minimization 
µ̃(x) " arg min u$U(x) 
E 
& 
g(x, u, w) + "J̃ # 
f(x, u, w) $ 
' 
; (2.17) 
† Actually the preceding formulas also hold even when the positive definiteness assumption on Q is replaced by other weaker conditions (see [Ber17a], Sec-tion 3.1). We will not go into the details of this, but we note that some condition on Q is needed for the preceding results to hold, as we will show later by example in Chapter 4. 
‡ This is an algebraic form of the Riccati di!erential equation, which was invented in its one-dimensional form by count Jacopo Riccati in the 1700s, and has played an important role in control theory. It has been studied extensively in its di!erential and di!erence matrix versions; see the book by Lancaster and Rod-man [LaR95], and the paper collection by Bittanti, Laub, and Willems [BLW91], which also includes a historical account by Bittanti [Bit91] of Riccati’s remarkable life and accomplishments.
26 Deterministic and Stochastic Dynamic Programming Chap. 2 
(we implicitly assume that the minimum above is attained for all x).† This minimization yields a stationary policy {µ̃, µ̃, . . .}, with cost function denoted Jµ̃ [i.e., Jµ̃(x) is the total infinite horizon discounted cost obtained when using µ̃ starting at state x]. In the next section, the change from J̃ 
to Jµ̃ will be interpreted as a step of Newton’s method for solving Bellman’s equation. Among others, this will suggest that Jµ̃ is close to J* and obeys a superlinear convergence relation 
lim J̃"J* 
Jµ̃(x) # J*(x) 
J̃(x)# J*(x) = 0, 
for all states x. For specific types of problems, this relation represents a plausible result, which likely holds under appropriate conditions. This is similar to the use of Newton’s method in numerical analysis, where its global or local convergence is guaranteed only under some assumptions. Within our context of approximate DP, however, there is an important underlying structure, which is favorable and enhances the convergence properties of Newton’s method, namely the monotonicity and concavity properties of Bellman’s equation, as we will discuss in what follows. 
While it is desirable that Jµ̃ is close to J* in some sense, for classical control problems involving control to a goal state (e.g., problems with a cost-free and absorbing terminal state, and positive cost for all other states), stability of µ̃ may be a principal objective. For the purposes of this work, we will focus on stability issues for just this one class of problems, and we will consider the policy µ̃ to be stable if Jµ̃ is real-valued , i.e., 
Jµ̃(x) < (, for all x " X. 
Selecting J̃ so that µ̃ is stable is a question of major interest, and will be addressed in Chapter 3. 
#-Step Lookahead 
An important extension of one-step lookahead minimization is #-step lookahead , whereby at a state xk we minimize the cost of the first # > 1 stages with the future costs approximated by a function J̃ (see Fig. 2.2.1). This minimization yields a control ũk and a sequence µ̃k+1, . . . , µ̃k+"!1. The control ũk is applied at xk, and defines the #-step lookahead policy µ̃ via µ̃(xk) = ũk. The sequence µ̃k+1, . . . , µ̃k+"!1 is discarded. Actually, we may view #-step lookahead minimization as the special case of its one-step counterpart where the lookahead function is the optimal cost function of 
† Note that the general theory of abstract DP is developed with the use of 
extended real-valued functions, and without the attainment of minimum assumption; see [Ber22a].
Sec. 2.2 Approximation in Value Space 27 
) At x 
At xk min uk,µk+1,...,µk+!!1 
E 
! 
g(xk, uk, wk) + k+!!1 " 
i=k+1 
! i!kg 
# 
xi, µi(xi), wi 
$ 
+ ! !J̃(xk+!) 
% 
One-Step Lookahead Multistep Lookahead 
One-Step Lookahead Multistep Lookahead 
First Step First 
First Step First ! Steps “Future”Steps “Future” 
Steps “Future” 
minu!U(x) E ! 
g(x, u, w) + !J̃ " 
f(x, u, w) # 
$ 
Figure 2.2.1 Schematic illustration of approximation in value space with onestep and "-step lookahead minimization. In the former case, the minimization yields at state x a control ũ, which defines the one-step lookahead policy µ̃ via µ̃(x) = ũ. In the latter case, the minimization yields a control ũk and a sequence µ̃k+1, . . . , µ̃k+!%1. The control ũk is applied at xk, and defines the "-step lookahead policy µ̃ via µ̃(xk) = ũk. The sequence µ̃k+1, . . . , µ̃k+!%1 is discarded. 
an (##1)-stage DP problem with a terminal cost J̃(xk+") on the state xk+" 
obtained after ## 1 stages. In the next chapter, this will be interpreted as a step of Newton’s method for solving Bellman’s equation, starting from a function Ĵ , which is an “improvement” over J̃ . In particular, Ĵ is obtained from J̃ by applying ## 1 successive value iterations. 
The motivation for #-step lookahead minimization is that by increasing the value of #, we may require a less accurate approximation J̃ to obtain good performance. Otherwise expressed, for the same quality of cost function approximation, better performance may be obtained as # becomes larger. This will be explained visually in the next section, and is also supported by error bounds, given for example in the books [Ber19a], [Ber20a]. In particular, for AlphaZero chess, long multistep lookahead is critical for good on-line performance. Another motivation for multistep lookahead is to enhance the stability properties of the generated on-line policy. On the other hand, the multistep lookahead minimization problem is more time consuming that the one-step lookahead counterpart of Eq. (2.17). 
Constructing Terminal Cost Approximations 
A major issue in value space approximation is the construction of suitable approximate cost functions J̃ . This can be done in many di!erent ways, giving rise to some of the principal RL methods. For example, J̃ may be constructed with a sophisticated o!-line training method, as discussed in Chapter 1, in connection with chess and backgammon. Alternatively, the approximate values J̃(x) may be obtained on-line as needed with truncated rollout, by running an o!-line obtained policy for a suitably large number
28 Deterministic and Stochastic Dynamic Programming Chap. 2 
of steps, starting from x, and supplementing it with a suitable terminal cost approximation. While the method by which we obtain J̃ will not be important for understanding the ideas of this work, for orientation purposes we briefly describe four broad types of approximation, and refer to the RL and approximate DP literature for further details: 
(a) Problem approximation: Here the function J̃ is obtained as the optimal or nearly optimal cost function of a simplified optimization problem, which is more convenient for computation. Simplifications may include exploiting decomposable structure, reducing the size of the state space, and ignoring various types of uncertainties. For example we may consider using as J̃ the cost function of a related deterministic problem, obtained through some form of “certainty equivalence,” thus allowing computation of J̃ by gradient-based optimal control methods or shortest path-type methods. A major type of problem approximation method is aggregation, which is described and analyzed in the books [Ber12], [Ber19a], and the papers [Ber18b], [Ber18c]. Aggregation provides a systematic procedure to simplify a given problem by grouping states together into a relatively small number of subsets, called aggregate states. The optimal cost function of the simpler aggregate problem is computed by exact DP methods, possibly involving the use of simulation. This cost function is then used to provide an approximation J̃ to the optimal cost function J* of the original problem, using some form of interpolation. 
(b) On-line simulation, as in rollout algorithms, where we use a suboptimal policy µ to compute on-line when needed the values J̃(x) to be exactly or approximately equal to Jµ(x). The policy µ may be obtained by any method, e.g., one based on heuristic reasoning, or o!-line training based on a more principled approach, such as approximate policy iteration or approximation in policy space. Note that while simulation is time-consuming, it is uniquely well-suited for the use of parallel computation. This may be an important consideration for the practical implementation of rollout algorithms, particularly for stochastic problems. 
(c) On-line approximate optimization, such as model predictive control (MPC), which will be discussed in more detail later. This approach involves the solution of a suitably constructed #-step version of the problem. It can be viewed as either approximation in value space with #-step lookahead, or as a form of rollout algorithm. 
(d) Parametric cost approximation, where J̃ is obtained from a given parametric class of functions J(x, r), where r is a parameter vector, selected by a suitable algorithm. The parametric class typically involves prominent characteristics of x called features , which can be obtained either through insight into the problem at hand, or by using
Sec. 2.2 Approximation in Value Space 29 
training data and some form of neural network. 
We refer to the neurodynamic programming book by Bertsekas and Tsitsik-lis [BeT96], and the RL book by Sutton and Barto [SuB18], as well as the large number of subsequent RL and approximate DP books, which provide specific examples of cost function approximation methods and associated training algorithms. 
Let us also mention that for problems with special structure, the terminal cost approximation may be chosen so that the one-step lookahead minimization (2.17) is facilitated. In fact, in favorable circumstances, the lookahead minimization may be carried out in closed form. An example is when the control enters linearly the system equation and quadratically in the cost function, while the terminal cost approximation is quadratic. 
From O!-Line Training to On-Line Play 
Generally o!-line training will produce either just a cost approximation (as in the case of TD-Gammon), or just a policy (as for example by some approximation in policy space/policy gradient approach), or both (as in the case of AlphaZero). We have already discussed in this section one-step lookahead and multistep lookahead schemes to implement on-line approximation in value space using J̃ ; cf. Fig. 2.2.1. Let us now consider some additional possibilities, some of which involve the use of a policy µ that has been obtained o!-line (possibly in addition to a terminal cost approximation). Here are some of the main possibilities: 
(a) Given a policy µ that has been obtained o!-line, we may use as terminal cost approximation J̃ the cost function Jµ of the policy. For the case of one-step lookahead, this requires a policy evaluation operation, and can be done on-line, by computing (possibly by simulation) just the values of 
E 
& 
Jµ # 
f(xk, uk, wk) $ 
' 
that are needed [cf. Eq. (2.17)]. For the case of #-step lookahead, the values 
E ( 
Jµ(xk+") ) 
for all states xk+" that are reachable in # steps starting from xk are needed. This is the simplest form of rollout, and only requires the o!-line construction of the policy µ. 
(b) Given a terminal cost approximation J̃ that has been obtained o!-line, we may use it on-line to compute a one-step or multistep lookahead policy µ̃. In a more powerful version of this scheme, the policy µ̃ can in turn be used for rollout as in (a) above. In a variation of this scheme, we may also use J̃ for truncated rollout, to approximate the tail end of the rollout process (an example of this is the rollout-based TD-Gammon algorithm discussed in Section 1.2).
30 Deterministic and Stochastic Dynamic Programming Chap. 2 
(c) Given a policy µ and a terminal cost approximation J̃ , we may use them together in a truncated rollout scheme, whereby the tail end of the rollout with µ is approximated using the cost approximation J̃ . This is similar to the truncated rollout scheme noted in (b) above, except that the policy µ is computed o↵-line rather than on-line using J̃ and one-step or multistep lookahead as in (b). 
The preceding three possibilities are the principal ones for using the results of o↵-line training within on-line play schemes. Naturally, there are variations where additional information is computed o↵-line to facilitate and/or expedite the on-line play algorithm. As an example, in MPC, in addition to a terminal cost approximation, a target tube may need to be computed o↵-line in order to guarantee that some state constraints can be satisfied on-line; see the discussion of MPC in Section 5.4. Other examples of this type will be noted in the context of specific applications. 
Finally, let us note that while we have emphasized approximation in value space with cost function approximation, our discussion applies to Q-factor approximation, involving functions 
Q̃(x, u) ⇡ E n g(x, u, w) + ↵J* 
  f(x, u, w) 
 o . 
The corresponding one-step lookahead scheme has the form 
µ̃(x) 2 arg min u2U(x) 
E n g(x, u, w)+↵ min 
u02U(f(x,u,w)) Q̃   f(x, u, w), u0 
 o ; (2.18) 
cf. Eq. (2.17). The second term on the right in the above equation represents the cost function approximation 
J̃   f(x, u, w) 
  = min 
u02U(f(x,u,w)) Q̃   f(x, u, w), u0 
  . 
The use of Q-factors is common in the “model-free” case where a computer simulator is used to generate samples of w, and corresponding values of g and f . Then, having obtained Q̃ through o↵-line training, the one-step lookahead minimization in Eq. (2.18) must be performed on-line with the use of the simulator. 
2.3 NOTES AND SOURCES 
Our discussion of exact DP in this chapter has been brief since our focus in this book will be on approximate DP and RL. The author’s DP textbooks [Ber12], [Ber17a] provide an extensive discussion of finite and infinite horizon exact DP, and its applications to discrete and continuous spaces problems, using a notation and style that is consistent with the present book. The author’s paper [Ber17b] focuses on deterministic, nonnegative cost infinite horizon problems, and provides a convergence analysis of the value and policy iteration algorithms.
3 An Abstract View of 
Reinforcement Learning 
Contents 
3.1. Bellman Operators . . . . . . . . . . . . . . . . . p. 32 3.2. Approximation in Value Space and Newton’s Method . . p. 39 3.3. Region of Stability . . . . . . . . . . . . . . . . . p. 46 3.4. Policy Iteration, Rollout, and Newton’s Method . . . . . p. 50 3.5. How Sensitive is On-Line Play to the O!-Line . . . . . . . 
Training Process? . . . . . . . . . . . . . . . . . . p. 58 3.6. Why Not Just Train a Policy Network and Use it Without . 
On-Line Play? . . . . . . . . . . . . . . . . . . . p. 60 3.7. Multiagent Problems and Multiagent Rollout . . . . . . p. 61 3.8. On-Line Simplified Policy Iteration . . . . . . . . . . p. 66 3.9. Exceptional Cases . . . . . . . . . . . . . . . . . . p. 72 3.10. Notes and Sources . . . . . . . . . . . . . . . . . p. 79 
31
32 An Abstract View of Reinforcement Learning Chap. 3 
In this chapter we will use geometric constructions to obtain insight into Bellman’s equation, the value and policy iteration algorithms, approximation in value space, and some of the properties of the corresponding onestep or multistep lookahead policy µ̃. To understand these constructions, we need an abstract notational framework that is based on the operators that are involved in the Bellman equations. 
3.1 BELLMAN OPERATORS 
We denote by TJ the function of x that appears in the right-hand side of Bellman’s equation. Its value at state x is given by 
(TJ)(x) = min u!U(x) 
E 
! 
g(x, u, w) + !J " 
f(x, u, w) # 
$ 
, for all x. (3.1) 
Also for each policy µ, we introduce the corresponding function TµJ , which has value at x given by 
(TµJ)(x) = E 
! 
g " 
x, µ(x), w # 
+ !J " 
f(x, µ(x), w) # 
$ 
, for all x. (3.2) 
Thus T and Tµ can be viewed as operators (broadly referred to as the Bellman operators), which map functions J to other functions (TJ or TµJ , respectively).† 
An important property of the operators T and Tµ is that they are monotone, in the sense that if J and J " are two functions of x such that 
J(x) ! J "(x), for all x, 
then we have 
(TJ)(x) ! (TJ ")(x), (TµJ)(x) ! (TµJ ")(x), for all x and µ. (3.3) 
This monotonicity property is evident from Eqs. (3.1) and (3.2), where the values of J are multiplied by nonnegative numbers. 
† Within the context of this work, the functions J on which T and Tµ operate 
will be real-valued functions of x, which we denote by J ! R(X). We will assume throughout that the expected values in Eqs. (3.1) and (3.2) are well-
defined and finite when J is real-valued. This implies that TµJ will also be 
real-valued functions of x. On the other hand (TJ)(x) may take the value "# because of the minimization in Eq. (3.1). We allow this possibility, although our 
illustrations will primarily depict the case where TJ is real-valued. Note that the 
general theory of abstract DP is developed with the use of extended real-valued functions; see [Ber22a].
Sec. 3.1 Bellman Operators 33 
Another important property is that the Bellman operator Tµ is linear , in the sense that it has the form TµJ = G+AµJ , where G " R(X) is some function and Aµ : R(X) #$ R(X) is an operator such that for any functions J1, J2, and scalars "1, "2, we have† 
Aµ("1J1 + "2J2) = "1AµJ1 + "2AµJ2. 
Moreover, from the definitions (3.1) and (3.2), we have 
(TJ)(x) = min µ!M 
(TµJ)(x), for all x, 
where M is the set of stationary policies. This is true because for any policy µ, there is no coupling constraint between the controls µ(x) and µ(x") that correspond to two di!erent states x and x". It follows that (TJ)(x) is a concave function of J for every x (the pointwise minimum of linear functions is a concave function). This will be important for our interpretation of one-step and multistep lookahead minimization as a Newton iteration for solving the Bellman equation J = TJ . 
Example 3.1.1 (A Two-State and Two-Control Example) 
Assume that there are two states 1 and 2, and two controls u and v. Consider the policy µ that applies control u at state 1 and control v at state 2. Then the operator Tµ takes the form 
(TµJ)(1) = 
2 % 
y=1 
p1y(u) " 
g(1, u, y) + !J(y) # 
, (3.4) 
(TµJ)(2) = 
2 % 
y=1 
p2y(v) " 
g(2, v, y) + !J(y) # 
, (3.5) 
where pxy(u) and pxy(v) are the probabilities that the next state will be y, when the current state is x, and the control is u or v, respectively. Clearly, (TµJ)(1) and (TµJ)(2) are linear functions of J . Also the operator T of the Bellman equation J = TJ takes the form 
(TJ)(1) = min 
& 
2 % 
y=1 
p1y(u) " 
g(1, u, y) + !J(y) # 
, 
2 % 
y=1 
p1y(v) " 
g(1, v, y) + !J(y) # 
' 
, 
(3.6) 
† An operator Tµ with this property is often called “a!ne,” but in this work 
we just call it “linear.” Also we use abbreviated notation to express pointwise 
equalities and inequalities, so that we write J = J ! or J $ J ! to express the fact that J(x) = J !(x) or J(x) $ J !(x), for all x, respectively.
34 An Abstract View of Reinforcement Learning Chap. 3 
(TJ)(2) = min 
& 
2 % 
y=1 
p2y(u) " 
g(2, u, y) + !J(y) # 
, 
2 % 
y=1 
p2y(v) " 
g(2, v, y) + !J(y) # 
' 
. 
(3.7) 
Thus, (TJ)(1) and (TJ)(2) are concave and piecewise linear as functions of the two-dimensional vector J (with two pieces; more generally, as many linear pieces as the number of controls). This concavity property holds in general since (TJ)(x) is the minimum of a collection of linear functions of J , one for each u ! U(x). Figure 3.1.1 illustrates (TµJ)(1) for the cases where µ(1) = u and µ(1) = v, (TµJ)(2) for the cases where µ(2) = u and µ(2) = v, (TJ)(1), and (TJ)(2), as functions of J = 
" 
J(1), J(2) # 
. 
Critical properties from the DP point of view are whether T and Tµ 
have fixed points; equivalently, whether the Bellman equations J = TJ 
and J = TµJ have solutions within the class of real-valued functions, and whether the set of solutions includes J* and Jµ, respectively. It may thus be important to verify that T or Tµ are contraction mappings. This is true for example in the benign case of discounted problems with bounded cost per stage. However, for undiscounted problems, asserting the contraction property of T or Tµ may be more complicated, and even impossible; the abstract DP book [Ber22a] deals extensively with such questions, and related issues regarding the solution sets of the Bellman equations. 
Geometrical Interpretations 
We will now interpret the Bellman operators geometrically, starting with Tµ. Figure 3.1.2 illustrates its form. Note here that the functions J and TµJ are multidimensional. They have as many scalar components J(x) and (TµJ)(x), respectively, as there are states x, but they can only be shown projected onto one dimension. The function TµJ for each policy µ 
is linear. The cost function Jµ satisfies Jµ = TµJµ, so it is obtained from the intersection of the graph of TµJ and the 45 degree line, when Jµ is real-valued. Later we will interpret the case where Jµ is not real-valued as the system being unstable under µ [we have Jµ(x) = % for some initial states x]. 
The form of the Bellman operator T is illustrated in Fig. 3.1.3. Again the functions J , J#, TJ , TµJ , etc, are multidimensional, but they are shown projected onto one dimension (alternatively they are illustrated for a system with a single state, plus possibly a termination state). The Bellman equation J = TJ may have one or many real-valued solutions. It may also have no real-valued solution in exceptional situations, as we will discuss later (see Section 3.8). The figure assumes a unique real-valued solution of the Bellman equations J = TJ and J = TµJ , which is true if T and Tµ are contraction mappings, as is the case for discounted problems with
Sec. 3.1 Bellman Operators 35 
State 1 State 2 State 1 State 2 
One-step lookahead J! 
! J!(1) 
(2) (TJ!)(1) = J!(1) ( 
One-step lookahead J! 
(1) J!(2) 
(1) (TJ!)(2) = J!(2) 
Figure 3.1.1 Geometric illustrations of the Bellman operators Tµ and T for states 1 and 2 in Example 3.1.1; cf. Eqs. (3.4)-(3.7). The problem’s transition probabilities are: p11(u) = 0.3, p12(u) = 0.7, p21(u) = 0.4, p22(u) = 0.6, p11(v) = 0.6, p12(v) = 0.4, p21(v) = 0.9, p22(v) = 0.1. The stage costs are g(1, u, 1) = 3, g(1, u, 2) = 10, g(2, u, 1) = 0, g(2, u, 2) = 6, g(1, v, 1) = 7, g(1, v, 2) = 5, g(2, v, 1) = 3, g(2, v, 2) = 12. The discount factor is ! = 0.9, and the optimal costs are J"(1) = 50.59 and J"(2) = 47.41. The optimal policy is µ"(1) = v and µ"(2) = u. The figure also shows two one-dimensional slices of T that are parallel to the J(1) and J(2) axes and pass through J".
36 An Abstract View of Reinforcement Learning Chap. 3 
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
Figure 3.1.2 Geometric interpretation of the linear Bellman operator Tµ and the corresponding Bellman equation. The graph of Tµ is a plane in the space R(X) ! R(X), and when projected on a one-dimensional plane that corresponds to a single state and passes through Jµ, it becomes a line. Then there are three cases: 
(a) The line has slope less than 45 degrees, so it intersects the 45-degree line at a unique point, which is equal to Jµ, the solution of the Bellman equation J = TµJ . This is true if Tµ is a contraction mapping, as is the case for discounted problems with bounded cost per stage. 
(b) The line has slope greater than 45 degrees. Then it intersects the 45-degree line at a unique point, which is a solution of the Bellman equation J = TµJ , but is not equal to Jµ. Then Jµ is not real-valued; we will call such µ unstable in Section 3.2. 
(c) The line has slope exactly equal to 45 degrees. This is an exceptional case where the Bellman equation J = TµJ has an infinite number of real-valued solutions or no real-valued solution at all; we will provide examples where this occurs in Section 3.8. 
bounded cost per stage. Otherwise, these equations may have no solution or multiple solutions within the class of real-valued functions (see Section 3.8). The equation J = TJ typically has J# as a solution, but may have more than one solution in cases where either ! = 1, or ! < 1 and the cost per stage is unbounded.
Sec. 3.1 Bellman Operators 37 
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
Figure 3.1.3 Geometric interpretation of the Bellman operator T , and the corresponding Bellman equation. For a fixed x, the function (TJ)(x) can be written as minµ(TµJ)(x), so it is concave as a function of J . The optimal cost function J" satisfies J" = TJ", so it is obtained from the intersection of the graph of TJ 
and the 45 degree line shown, assuming J" is real-valued. Note that the graph of T lies below the graph of every operator Tµ, and is 
in fact obtained as the lower envelope of the graphs of Tµ as µ ranges over the set of policies M. In particular, for any given function J̃ , for every x, the value (T J̃)(x) is obtained by finding a support hyperplane/subgradient of the graph of the concave function (TJ)(x) at J = J̃, as shown in the figure. This support hyperplane is defined by the control µ(x) of a policy µ̃ that attains the minimum of (TµJ̃)(x) over µ: 
µ̃(x) " arg min µ#M 
(TµJ̃)(x) 
(there may be multiple policies attaining this minimum, defining multiple support hyperplanes). 
Example 3.1.2 (A Two-State and Infinite Controls Problem) 
Let us consider the mapping T for a problem that involves two states, 1 and 2, but an infinite number of controls. In particular, the control space at both states is the unit interval, U(1) = U(2) = [0, 1]. Here (TJ)(1) and (TJ)(2) are given by 
(TJ)(1) = min u#[0,1] 
( 
g1 + r11u 2 + r12(1" u)2 + !uJ(1) + !(1" u)J(2) 
) 
, 
(TJ)(2) = min u#[0,1] 
( 
g2 + r21u 2 + r22(1" u)2 + !uJ(1) + !(1" u)J(2) 
) 
.
38 An Abstract View of Reinforcement Learning Chap. 3 
State 1 State 2 
One-step lookahead J! One-step lookahead J! 
! J!(1) (1) J!(2) 
(2) (TJ!)(1) = J!(1) ( (1) (TJ!)(2) = J!(2) 
Figure 3.1.4 Illustration of the Bellman operator T for states 1 and 2 in Example 3.1.2. The parameter values are g1 = 5, g2 = 3, r11 = 3, r12 = 15, r21 = 9, r22 = 1, and the discount factor is ! = 0.9. The optimal costs are J"(1) = 49.7 and J"(2) = 40.0, and the optimal policy is µ"(1) = 0.59 and µ"(2) = 0. The figure also shows the two one-dimensional slices of the operators at J(1) = 15 and J(2) = 30 that are parallel to the J(1) and J(2) axes. 
The control u at each state x = 1, 2 has the meaning of a probability that we must select at that state. In particular, we control the probabilities u and (1"u) of moving to states y = 1 and y = 2, at a control cost that is quadratic in u and (1" u), respectively. For this problem (TJ)(1) and (TJ)(2) can be calculated in closed form, so they are easy to plot and understand. They are piecewise quadratic, unlike the corresponding plots of Fig. 3.1.1, which are piecewise linear; see Fig. 3.1.4. 
Visualization of Value Iteration 
The operator notation simplifies algorithmic descriptions, derivations, and proofs related to DP. For example, we can write the VI algorithm in the compact form 
Jk+1 = TJk, k = 0, 1, . . . , 
as illustrated in Fig. 3.1.5. Moreover, the VI algorithm for a given policy µ can be written as 
Jk+1 = TµJk, k = 0, 1, . . . , 
and it can be similarly interpreted, except that the graph of the function TµJ is linear. Also we will see shortly that there is a similarly compact description for the policy iteration algorithm. 
To keep the presentation simple, we will focus our attention on the abstract DP framework as it applies to the optimal control problems of Sec-tion 2.1. In particular, we will assume without further mention that T and Tµ have the monotonicity property (3.3), that TµJ is linear for all µ, and
Sec. 3.2 Approximation in Value Space and Newton’s Method 39 
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
Figure 3.1.5 Geometric interpretation of the VI algorithm Jk+1 = TJk, starting from some initial function J0. Successive iterates are obtained through the staircase construction shown in the figure. The VI algorithm Jk+1 = TµJk for a given policy µ can be similarly interpreted, except that the graph of the function TµJ is linear. 
that (as a consequence) the component (TJ)(x) is concave as a function of J for every state x. We note, however, that the abstract notation facilitates the extension of the infinite horizon DP theory to models beyond the ones that we discuss in this work. Such models include semi-Markov problems, minimax control problems, risk sensitive problems, Markov games, and others (see the DP textbook [Ber12], and the abstract DP monograph [Ber22a]). 
3.2 APPROXIMATION IN VALUE SPACE AND NEWTON’S METHOD 
Let us now consider approximation in value space and an abstract geometric interpretation, first provided in the author’s book [Ber20a]. By using the operators T and Tµ, for a given J̃ , a one-step lookahead policy µ̃ is characterized by the equation Tµ̃J̃ = T J̃, or equivalently 
µ̃(x) " arg min u!U(x) 
E 
! 
g(x, u, w) + !J̃ " 
f(x, u, w) # 
$ 
, (3.8) 
as in Fig. 3.2.1. Furthermore, this equation implies that the graph of Tµ̃J 
just touches the graph of TJ at J̃ , as shown in the figure.
40 An Abstract View of Reinforcement Learning Chap. 3 
In mathematical terms, for each state x " X , the hyperplaneHµ̃(x) " R(X)&' 
Hµ̃(x) = ( 
(J, #) | (Tµ̃J)(x) = # ) 
, (3.9) 
supports from above the hypograph of the concave function (TJ)(x), i.e., the convex set 
( 
(J, #) | (TJ)(x) ! # ) 
. 
The point of support is " 
J̃ , (Tµ̃J̃)(x) # 
, and relates the function J̃ with the corresponding one-step lookahead minimization policy µ̃, the one that satisfies Tµ̃J̃ = T J̃. The hyperplane Hµ̃(x) of Eq. (3.9) defines a subgradient of (TJ)(x) at J̃ . Note that the one-step lookahead policy µ̃ need not be unique, since T need not be di!erentiable, so there may be multiple hyperplanes of support at J̃ . Still this construction shows that the linear operator Tµ̃ is a linearization of the operator T at the point J̃ (pointwise for each x). 
Equivalently, for every x " X , the linear scalar equation J(x) = (Tµ̃J)(x) is a linearization of the nonlinear equation J(x) = (TJ)(x) at the point J̃ . Consequently, the linear operator equation J = Tµ̃J is a linearization of the equation J = TJ at J̃ , and its solution, Jµ̃, can be viewed as the result of a Newton iteration at the point J̃ (here we adopt an expanded view of the Newton iteration that applies to possibly nondi!erentiable fixed point equations; see the Appendix). In summary, the Newton iterate at J̃ is Jµ̃, the solution of the linearized equation J = Tµ̃J .† 
† The classical Newton’s method for solving a fixed point problem of the form y = G(y), where y is an n-dimensional vector, operates as follows: At the current iterate yk, we linearize G and find the solution yk+1 of the corresponding linear fixed point problem. Assuming G is di"erentiable, the linearization is obtained by using a first order Taylor expansion: 
yk+1 = G(yk) + "G(yk) 
"y (yk+1 " yk), 
where "G(yk)/"y is the n % n Jacobian matrix of G evaluated at the vector yk. The most commonly given convergence rate property of Newton’s method is quadratic convergence. It states that near the solution y", we have 
&yk+1 " y"& = O " 
&yk " y"&2 # 
, 
where & ·& is the Euclidean norm, and holds assuming the Jacobian matrix exists, is invertible, and is Lipschitz continuous (see the books by Ortega and Rheinboldt [OrR70], and by the author [Ber16], Section 1.4). 
There are well-studied extensions of Newton’s method that are based on solving a linearized system at the current iterate, but relax the di"erentiabil-
ity requirement through alternative requirements of piecewise di"erentiability, 
B-di"erentiability, and semi-smoothness, while maintaining the superlinear convergence property of the method. In particular, the quadratic rate of convergence
Sec. 3.2 Approximation in Value Space and Newton’s Method 41 
J J! = TJ! 
0 Prob. = 1 1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
TJ 
Tµ̃J 
J̃ Jµ̃ = Tµ̃Jµ̃ 
One-Step Lookahead Policy Cost l One-Step Lookahead Policy Cost l 
One-Step Lookahead Policy Cost One-Step Lookahead Policy µ̃ 
Corresponds to One-Step Lookahead Policy ˜ 
Stability Region 0 J̃ 
Cost Approximation Value Space Approximation 
Newton step from J̃ 
J̃ for solving J = TJ 
Approximations Result of 
also Newton Step 
O!-Line Training On-Line Play -Line Training On-Line Play 
Figure 3.2.1 Geometric interpretation of approximation in value space and the one-step lookahead policy µ̃ as a step of Newton’s method [cf. Eq. (3.8)]. Given J̃ , we find a policy µ̃ that attains the minimum in the relation 
T J̃ = min µ 
TµJ̃ . 
This policy satisfies T J̃ = Tµ̃J̃ , so the graph of TJ and Tµ̃J touch at J̃ , as shown. It may not be unique. Because TJ has concave components, the equation J = Tµ̃J 
is the linearization of the equation J = TJ at J̃ [for each x, the hyperplane Hµ̃(x) of Eq. (3.9) defines a subgradient of (TJ)(x) at J̃ ]. The linearized equation is solved at the typical step of Newton’s method to provide the next iterate, which is just Jµ̃. 
The structure of the Bellman operators (3.1) and (3.2), with their monotonicity and concavity properties, tends to enhance the convergence and the rate of convergence properties of Newton’s method, even in the absence of di!erentiability, as evidenced by the favorable Newton-related convergence analysis of PI, and the extensive favorable experience with rollout, PI, and MPC. In fact, the role of monotonicity and concavity in affecting the convergence properties of Newton’s method has been addressed 
result for di"erentiable G of Prop. 1.4.1 of the book [Ber16] admits a straight-
forward and intuitive extension to piecewise di"erentiable G, given in the paper [KoS86]; see the Appendix, which contains references to the literature.
42 An Abstract View of Reinforcement Learning Chap. 3 
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
Cost Approximation Value Space Approximation Multistep Lookahead Policy Cost T 2J̃ 
E!ective Cost Approximation Value Space ApproximationJ̃ for solving J = TJ 
Newton step from T !!1J̃ 
Approximations Result of 
Linear policy parameter Optimal ! = 3 
also Newton Step 
-Line Training On-Line PlayO!-Line Training On-Line Play 
Figure 3.2.2 Geometric interpretation of approximation in value space with "-step lookahead (in this figure " = 3). It is the same as approximation in value space with one-step lookahead using T !$1J̃ as cost approximation. It can be viewed as a Newton step at the point T !$1J̃ , the result of " # 1 value iterations applied to J̃. Note that as " increases the cost function Jµ̃ of the "-step lookahead policy µ̃ approaches more closely the optimal J", and that lim!%& Jµ̃ = J". 
in the mathematical literature.† As noted earlier, approximation in value space with $-step lookahead 
using J̃ is the same as approximation in value space with one-step lookahead using the ($(1)-fold operation of T on J̃ , T !$1J̃ . Thus it can be interpreted as a Newton step starting from T !$1J̃ , the result of $ ( 1 value iterations applied to J̃ . This is illustrated in Fig. 3.2.2.‡ 
† See the papers by Ortega and Rheinboldt [OrR67], and Vandergraft [Van67], 
the books by Ortega and Rheinboldt [OrR70], and Argyros [Arg08], and the references cited there. In this connection, it is worth noting that in the case of 
Markov games, where the concavity property does not hold, the PI method may oscillate, as shown by Pollatschek and Avi-Itzhak [PoA69], and needs to be mod-
ified to restore its global convergence; see the author’s paper [Ber21c], and the 
references cited there. ‡ We note that several variants of Newton’s method that involve combina-
tions of first-order iterative methods, such as the Gauss-Seidel and Jacobi al-
gorithms, and Newton’s method, are well-known in numerical analysis. They belong to the general family of Newton-SOR methods (SOR stands for “succes-
Sec. 3.2 Approximation in Value Space and Newton’s Method 43 
Let us also note that $-step lookahead minimization involves $ successive VI iterations, but only the first of these iterations has a Newton step interpretation. As an example, consider two-step lookahead minimization with a terminal cost approximation J̃ . The second step minimization is a VI that starts from J̃ to produce T J̃ . The first step minimization is a VI that starts from T J̃ to produce T 2J̃ , but it also does something else that is more significant: It produces a two-step lookahead minimization policy µ̃ 
through Tµ̃(T J̃) = T (T J̃), and the step from T J̃ to Jµ̃ (the cost function of µ̃) is the Newton step. Thus, there is only one policy produced (i.e., µ̃) and only one Newton step (from T J̃ to Jµ̃). In the case of one-step lookahead minimization, the Newton step starts from J̃ and ends at Jµ̃. Similarly, in the case of $-step lookahead minimization, the first step of the lookahead is the Newton step (from T !$1J̃ to Jµ̃), and whatever follows the first step of the lookahead is preparation for the Newton step. 
Finally, it is worth mentioning that the approximation in value space algorithm computes Jµ̃ di!erently than both the PI method and the classical form of Newton’s method. It does not explicitly compute any values of Jµ̃; instead, the control is applied to the system and the cost is accumulated accordingly. Thus the values of Jµ̃ are implicitly computed only for those x that are encountered in the system trajectory that is generated on-line. 
Certainty Equivalent Approximations and the Newton Step 
We noted earlier that for stochastic DP problems, $-step lookahead can be computationally expensive, because the lookahead graph expands fast as $ increases, due to the stochastic character of the problem. The certainty equivalence approach is an important approximation idea for dealing with this di"culty. In the classical form of this approach, some or all of the stochastic disturbances wk are replaced by some deterministic quantities, such as their expected values. Then a policy is computed o!-line for the resulting deterministic problem, and it is used on-line for the actual stochastic problem. 
The certainty equivalence approach can also be used to expedite the computations of the $-step lookahead minimization. One way to do this is to simply replace each of the uncertain $ quantities wk, wk+1, . . . , wk+!$1 by a deterministic value w. Conceptually, this replaces the Bellman operators T and Tµ, 
(TJ)(x) = min u!U(x) 
E 
! 
g(x, u, w) + !J " 
f(x, u, w) # 
$ 
, 
sive over-relaxation”); see the book by Ortega and Rheinboldt [OrR70] (Section 
13.4). Their convergence rate is superlinear, similar to Newton’s method, as long as they involve a pure Newton step, along with the first-order steps.
44 An Abstract View of Reinforcement Learning Chap. 3 
(TµJ)(x) = E n g   x, µ(x), w 
  + ↵J 
  f(x, µ(x), w) 
 o , 
[cf. Eqs. (3.1) and (3.2)] with deterministic operators T and Tµ, given by 
(TJ)(x) = min u2U(x) 
h g(x, u, w) + ↵J 
  f(x, u, w) 
 i , 
(TµJ)(x) = g   x, µ(x), w 
  + ↵J 
  f(x, µ(x), w) 
  . 
The resulting `-step lookahead minimization then becomes simpler; for example, in the case of a finite control space problem, it is a deterministic shortest path computation, involving an acyclic `-stage graph that expands at each stage by a factor n, where n is the size of the control space. However, this approach yields a policy µ such that 
Tµ(T ` 1 
J̃) = T (T ` 1 
J̃), 
and the cost function Jµ of this policy is generated by a Newton step, 
which aims to find a fixed point of T (not T ), starting from T ` 1 
J̃ . Thus the Newton step now aims at a fixed point of T , which is not equal to J*. As a result the benefit of the Newton step is lost to a great extent. 
Still, we may largely correct this di culty, while retaining substantial simplification, by using certainty equivalence for only the last `  1 stages of the `-step lookahead. This can be done with an `-step lookahead scheme whereby only the uncertain quantities wk+1, . . . , wk+` 1 are replaced by a deterministic value w, while wk is treated as a stochastic quantity, as first proposed in the paper by Bertsekas and Castañon [BeC99]. In this way we obtain a policy µ such that 
Tµ(T ` 1 
J̃) = T (T ` 1 
J̃). 
The cost function Jµ of this policy is then generated by a Newton step, 
which aims to find a fixed point of T (not T ), starting again from T ` 1 
J̃ . Thus the benefit of the fast convergence of Newton’s method is restored. In fact based on insights derived from this Newton step interpretation, it appears that the performance penalty for making the last ` 1 stages of the 
`-step lookahead deterministic is minimal when T ` 1 
J̃ is “near” J*. At the 
same time the `-step minimization T (T ` 1 
J̃) involves only one stochastic step, the first one, and hence potentially a much “thinner” lookahead graph, than the one corresponding to the `-step minimization T `J̃ , which does not involve any certainty equivalence-type approximations. 
The preceding discussion also points to a more general approximation idea for dealing with the onerous computational requirements of long multistep lookahead minimization. We may approximate the tail (`   1)-step portion T ` 1J̃ of the `-step lookahead minimization with any simplified
Sec. 3.2 Approximation in Value Space and Newton’s Method 45 
calculation that produces an approximation Ĵ ) T !$1J̃ , and then obtain the lookahead policy µ̃ using the minimization 
Tµ̃Ĵ = T Ĵ. 
This type of simplification will still involve a Newton step (from Ĵ to Jµ̃), and benefit from the corresponding fast convergence property. 
Local and Global Performance Estimates Compared 
The preceding Newton step interpretation of the move from J̃ (the terminal cost function approximation) to Jµ̃ (the cost function of the lookahead policy µ̃) suggests a superlinear performance estimate 
max x 
* 
*Jµ̃(x) ( J*(x) * 
* = o 
+ 
max x 
* 
*J̃(x) ( J*(x) * 
* 
, 
. 
However, this estimate is local in character. It is meaningful only when J̃ is “close” to J*. When J̃ is far from J*, the di!erence maxx 
* 
*Jµ̃(x)( J*(x) * 
* 
may be large and even infinite when µ̃ is unstable (see the discussion in the next section). 
There are global estimates for the di!erence 
max x 
* 
*Jµ̃(x) ( J*(x) * 
* 
for several types of problems, including the upper bound 
max x 
* 
*Jµ̃(x) ( J*(x) * 
* * 2!! 
1( ! max x 
* 
*J̃(x)( J*(x) * 
* 
for $-step lookahead, and !-discounted problems where all the Bellman operators Tµ are contraction mappings; see the neurodynamic programming book [BeT96] (Section 6.1, Prop. 6.1), or the RL book [Ber20a] (Section 5.4, Prop. 5.4.1). These books also contain other related global estimates, which hold for all J̃ , both close and far from J*. However, these global estimates tend to be overly conservative and not representative of the performance of approximation in value space schemes when J̃ is near J*. For example, for finite spaces !-discounted MDP, µ̃ can be shown to be optimal when maxx 
* 
*J̃(x) ( J*(x) * 
* is su"ciently small; this can also be seen from the fact that the components (TJ)(x) of the Bellman operator are not only concave but also piecewise linear, so Newton’s method converges finitely. For a further comparative discussion of local and global error bounds, we refer to Appendix A.
46 An Abstract View of Reinforcement Learning Chap. 3 
J J! = TJ! 
0 Prob. = 1 
1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
TJ45!Line 
Instability Region Stability Region 0Instability Region 
Tµ̃J 
J̃ Jµ̃Without the Newton Step Base Player Threshold 
Figure 3.3.1 Illustration of the regions of stability and instability for approximation in value space with one-step lookahead. The stability region is the set of all J̃ such that the policy µ̃ obtained from the one-step lookahead minimization Tµ̃J̃ = T J̃ satisfies Jµ̃(x) < $ for all x. 
3.3 REGION OF STABILITY 
For any control system design method, the stability of the policy obtained is of paramount importance. It is thus essential to investigate and verify the stability of controllers obtained through approximation in value space schemes. Historically, there have been several proposed definitions of stability in control theory. Within the context of this work, our focus on stability issues will be for problems with a termination state t, which is cost-free, and with a cost per stage that is positive outside the termination state, such as the undiscounted positive cost deterministic problem introduced earlier (cf. Section 2.1). Moreover, it is best for our purposes to adopt an optimization-based definition. In particular, we say that a policy µ is unstable if Jµ(x) = % for some states x. Equivalently, we say that the policy µ stable if Jµ(x) < % for all states x. This definition has the advantage that it applies to general state and control spaces. Naturally, it can be made more specific in particular problem instances.† 
† For the undiscounted positive cost deterministic problem introduced earlier 
(cf. Section 2.1), it can be shown that if a policy µ is stable, then Jµ is the “small-
est” solution of the Bellman equation J = TµJ within the class of nonnegative real-valued functions, and under mild assumptions it is the unique solution of
Sec. 3.3 Region of Stability 47 
In the context of approximation in value space we are interested in the region of stability, which is the set of cost function approximations J̃ " R(X) for which the corresponding one-step or multistep lookahead policies µ̃ are stable. For discounted problems with bounded cost per stage, all policies have real-valued cost functions, so questions of stability do not arise. In general, however, the region of stability may be a strict subset of the set of real-valued functions; this will be illustrated later for the undiscounted deterministic case of the linear quadratic problem of Section 2.1 (cf. Example 2.1.1). Figure 3.3.1 illustrates the region of stability for approximation in value space with one-step lookahead. 
An interesting observation from Fig. 3.3.1 is that if J̃ does not belong to the region of stability and µ̃ is a corresponding one-step lookahead unstable policy, the Bellman equation J = Tµ̃J may have real-valued solutions. However, these solutions will not be equal to Jµ̃, as this would violate the definition of region of stability. Generally, if Tµ is not a contraction mapping, Tµ may have real-valued fixed points, none of which is equal to Jµ. 
Figure 3.3.2 illustrates the region of stability for the case of multistep lookahead minimization. The insights from this figure are similar to the one-step lookahead case of Fig. 3.3.1. However, the figure indicates that the region of stability of the $-step lookahead controller µ̃ depends on $, and tends to become larger as $ increases . The reason is that $-step lookahead with terminal cost J̃ is equivalent to one-step lookahead with terminal cost T !$1J̃ , which tends to be closer to the optimal cost function J* than J̃ 
(assuming convergence of the VI method). 
How Can We Obtain Function Approximations J̃ Within the Region of Stability? 
Naturally, identifying and obtaining cost function approximations J̃ that lie within the region of stability with either one-step or multistep lookahead is very important within our context. We will focus on this question for the special case where the expected cost per stage is nonnegative 
E ( 
g(x, u, w) ) 
! 0, for all x, u " U(x), 
and assume that J* is real-valued. This is the case of most interest in model predictive control, but also arises in other problems of interest, including stochastic shortest path problems that involve a termination state. 
From Fig. 3.3.2 it can be conjectured that if the sequence {T kJ̃} generated by the VI algorithm converges to J* for all J̃ such that 0 * J̃ * J* 
J = TµJ within the class of nonnegative real-valued functions J with J(t) = 0; 
see the author’s paper [Ber17b]. Moreover, if µ is unstable, then the Bellman 
equation J = TµJ has no solution within the class of nonnegative real-valued functions.
48 An Abstract View of Reinforcement Learning Chap. 3 
J J! = TJ! 
0 Prob. = 1 1 J J 
1 J J 
Optimal cost Cost of rollout policy ˜ 
TJ 
Instability Region Stability Region 0Instability Region 
45!Line 
J̃ T J̃J̃ 
= 3 ! = 2 
Without the Newton Step Base Player Threshold 
Figure 3.3.2 Illustration of the regions of stability and instability for approximation in value space with "-step lookahead minimization. The stability region is the set of all J̃ for which the policy µ̃ such that T !J̃ = Tµ̃T 
!$1J̃ satisfies Jµ̃(x) < $ 
for all x (the figure shows the case " = 2). The region of instability tends to be reduced as " increases. 
(which is true under very general conditions; see [Ber12], [Ber22a]), then T !$1J̃ belongs to the region of stability for su"ciently large $. Related ideas have been discussed in the adaptive DP literature by Liu and his collaborators [HWL21], [LXZ21], [WLL16], and by Heydari [Hey17], [Hey18], who provide extensive references; see also Winnicki et al. [WLL21]. We will revisit this issue in the context of linear quadratic problems. This conjecture is generally true, but requires that, in addition to J*, all functions J̃ within a neighborhood of J* belong to the region of stability. Our subsequent discussion will aim to address this di"culty. 
An important fact for our nonnegative cost problem context is that the region of stability includes all real-valued nonnegative functions J̃ such that 
T J̃ * J̃ . (3.10) 
Indeed if µ̃ is the corresponding one-step lookahead policy, we have 
Tµ̃J̃ = T J̃ * J̃ , 
and from a well-known result on nonnegative cost infinite horizon problems [see [Ber12], Prop. 4.1.4(a)], it follows that 
Jµ̃ * J̃ ;
Sec. 3.3 Region of Stability 49 
(the proof argument is that if Tµ̃J̃ * J̃ then T k+1 
µ̃ J̃ * T k µ̃ J̃ for all k, so, 
using also the fact 0 * J̃ , the limit of T k µ̃ J̃ , call it J%, satisfies Jµ̃ * J% * 
J̃). Thus if J̃ is nonnegative and real-valued, Jµ̃ is also real-valued, so µ̃ is stable. It follows that J̃ belongs to the region of stability. This is a known result in specific contexts, such as MPC (see the book by Rawlings, Mayne, and Diehl [RMD17], Section 2.4, which contains extensive references to prior work on stability issues). 
An important special case where the condition T J̃ * J̃ is satisfied is when J̃ is the cost function of a stable policy, i.e., J̃ = Jµ. Then we have that Jµ is real-valued and satisfies TµJµ = Jµ, so it follows that TJµ * Jµ. This case relates to the rollout algorithm and shows that rollout with a stable policy yields a stable lookahead policy . It also suggests that if µ is stable, then Tm 
µ J̃ belongs to the region of stability for su"ciently large m. Besides Jµ, with stable µ, and J*, there are other interesting functions 
J̃ satisfying the stability condition T J̃ * J̃ . In particular, let % be a scalar with % > 1, and for a stable policy µ, consider the %-amplified operator Tµ," defined by 
(Tµ,"J)(x) = E 
! 
%g " 
x, µ(x), w # 
+ !J " 
f(x, µ(x), w) # 
$ 
, for all x. 
Then it can be seen that the function 
Jµ," = %Jµ 
is a fixed point of Tµ," and satisfies TJµ," * Jµ," . This follows by writing 
Jµ," = Tµ,"Jµ," ! TµJµ," ! TJµ,". (3.11) 
Thus Jµ," lies within the region of stability, and lies “further to the right” of Jµ. Thus we may conjecture that it can be more reliably approximated by Tm µ,"J̃ than Jµ is approximated by Tm 
µ J̃ in the context of m-step truncated rollout. 
To illustrate this fact, consider a stable policy µ, and assume that the expected cost per stage at states other than a termination state t (if one exists) is bounded away from 0, i.e., 
C = min x &=t 
E 
! 
g " 
x, µ(x), w # 
$ 
> 0. 
Then we claim that given a scalar % > 1, any function Ĵ " R(X) with Ĵ(t) = 0, that satisfies 
max x 
* 
*Ĵ(x) ( Jµ,"(x) * 
* * &, for all x, (3.12) 
where 
& = (% ( 1)C 
1 + ! ,
50 An Abstract View of Reinforcement Learning Chap. 3 
also satisfies the stability condition T Ĵ * Ĵ . From this it follows that for a given nonnegative and real-valued J̃ , and for su!ciently large m, so that the function Ĵ = Tm 
µ,"J̃ satisfies Eq. (3.12), we have that Ĵ lies within the region of stability. 
To see this, note that for all x += t, we have 
Jµ,"(x) = %E 
! 
g " 
x, µ(x), w # 
$ 
+ !E 
! 
Jµ," " 
f(x, µ(x), w) # 
$ 
, 
so that by using Eq. (3.12), we have 
Ĵ(x) + & ! %E 
! 
g " 
x, µ(x), w # 
$ 
+ !E 
! 
Ĵ " 
f(x, µ(x), w) # 
$ 
( !&. 
It follows that 
Ĵ(x) ! E 
! 
g " 
x, µ(x), w # 
$ 
+ !E 
! 
Ĵ " 
f(x, µ(x), w) # 
$ 
+ (% ( 1)E ! 
g " 
x, µ(x), w # 
$ 
( (1 + !)& 
! E 
! 
g " 
x, µ(x), w # 
$ 
+ !E 
! 
Ĵ " 
f(x, µ(x), w) # 
$ 
+ (% ( 1)C ( (1 + !)& 
= (TµĴ)(x) 
! (T Ĵ)(x), 
so the stability condition T Ĵ * Ĵ is satisfied. Similarly the function 
J* " = %J* 
is a fixed point of the operator T" defined by 
(T"J)(x) = min u!U(x) 
E 
! 
%g(x, u, w) + !J " 
f(x, u, w) # 
$ 
, for all x. 
It can be seen, using an argument similar to Eq. (3.11), that J* " satisfies 
TJ* " * J* 
" , so it lies within the region of stability. Furthermore, similar to 
the case of truncated rollout discussed earlier, we may conjecture that J* " 
can be more reliably approximated by T !$1 
" J̃ than J* is approximated by 
T !$1J̃ in the context of $-step lookahead. 
3.4 POLICY ITERATION, ROLLOUT, AND NEWTON’SMETHOD 
Another major class of infinite horizon algorithms is based on policy iteration (PI for short), which involves the repeated use of policy improvement, in analogy with the AlphaZero/TD-Gammon o!-line training algorithms,
Sec. 3.4 Policy Iteration, Rollout, and Newton’s Method 51 
Rollout Policy µ̃ 
Jµ 
Policy Evaluation Policy Improvement Rollout Policy ˜ Policy Evaluation Policy Improvement Rollout Policy ˜ 
Jµ instead of J* 
Bellman Eq. with 
Policy Evaluation Policy Improvement Rollout Policy ˜ Policy Evaluation Policy Improve ent Rollout Policy ˜ 
x µ 
Base Policy Rollout Policy Appr ximation in Value Space Base Policy Rollout Policy Approximation in Value Space 
Figure 3.4.1 Schematic illustration of PI as repeated rollout. It generates a sequence of policies, with each policy µ in the sequence being the base policy that generates the next policy µ̃ in the sequence as the corresponding rollout policy. 
described in Chapter 1. Each iteration of the PI algorithm starts with a stable policy (which we call current or base policy), and generates another stable policy (which we call new or rollout policy, respectively). For the infinite horizon problem of Section 2.1, given the base policy µ, the iteration consists of two phases (see Fig. 3.4.1): 
(a) Policy evaluation, which computes the cost function Jµ. One possibility is to solve the corresponding Bellman equation 
Jµ(x) = E 
! 
g " 
x, µ(x), w # 
+ !Jµ " 
f(x, µ(x), w) # 
$ 
, for all x. 
(3.13) However, the value Jµ(x) for any x can also be computed by Monte Carlo simulation, by averaging over many randomly generated trajectories the cost of the policy starting from x. Other, more sophisticated possibilities include the use of specialized simulation-based methods, such as temporal di"erence methods , for which there is extensive literature (see e.g., the books [BeT96], [SuB98], [Ber12]). 
(b) Policy improvement , which computes the rollout policy µ̃ using the one-step lookahead minimization 
µ̃(x) " arg min u!U(x) 
E 
! 
g(x, u, w) + !Jµ " 
f(x, u, w) # 
$ 
, for all x. 
(3.14) It is generally expected (and can be proved under mild conditions) that the rollout policy is improved in the sense that 
Jµ̃(x) * Jµ(x), for all x. 
Proofs of this fact in a variety of contexts can be found in most DP books, including the author’s [Ber12], [Ber18a], [Ber19a], [Ber20a], [Ber22a]. 
Thus PI generates a sequence of stable policies {µk}, by obtaining µk+1 through a policy improvement operation using Jµk in place of Jµ
52 An Abstract View of Reinforcement Learning Chap. 3 
in Eq. (3.14), which is obtained through policy evaluation of the preceding policy µk using Eq. (3.13). It is well known that (exact) PI has solid convergence properties; see the DP textbooks cited earlier, as well as the author’s RL book [Ber19a]. These properties hold even when the method is implemented (with appropriate modifications) in unconventional computing environments, involving asynchronous distributed computation, as shown in a series of papers by Bertsekas and Yu [BeY10], [BeY12], [YuB13]. 
In terms of our abstract notation, the PI algorithm can be written in a compact form. For the generated policy sequence {µk}, the policy evaluation phase obtains Jµk from the equation 
Jµk = TµkJµk , (3.15) 
while the policy improvement phase obtains µk+1 through the equation 
Tµk+1Jµk = TJµk . (3.16) 
As Fig. 3.4.2 illustrates, PI can be viewed as Newton’s method for solving the Bellman equation in the function space of cost functions J . In particular, the policy improvement Eq. (3.16) is the Newton step starting from Jµk , and yields µk+1 as the corresponding one-step lookahead/rollout policy. Figure 3.4.3 illustrates the rollout algorithm, which is just the first iteration of PI. 
In contrast to approximation in value space, the interpretation of PI in terms of Newton’s method has a long history. We refer to the original works for linear quadratic problems by Kleinman [Klei68],† and for finitestate infinite horizon discounted and Markov game problems by Pollatschek and Avi-Itzhak [PoA69] (who also showed that the method may oscillate in the game case). Subsequent works, which discuss algorithmic variations and approximations, include Hewer [Hew71], Puterman and Brumelle [PuB78], [PuB79], Santos and Rust [SaR04], Bokanowski, Maroso, and Zi-dani [BMZ09], Hylla [Hyl11], Magirou, Vassalos, and Barakitis [MVB20], Bertsekas [Ber21c], and Kundu and Kunitsch [KuK21]. Some of these papers address broader classes of problems (such as continuous-time optimal control, minimax problems, and Markov games), and include superlinear convergence rate results under various (often restrictive) assumptions, as well as PI variants. Early related works for control system design include Saridis and Lee [SaL79], Beard [Bea95], and Beard, Saridis, and Wen [BSW99]. 
† This was part of Kleinman’s Ph.D. thesis [Kle67] at M.I.T., supervised by M. Athans. Kleinman gives credit for the one-dimensional version of his results to 
Bellman and Kalaba [BeK65]. Note also that the first proposal of the PI method 
was given by Bellman in his classic book [Bel57], under the name “approximation in policy space.”
Sec. 3.4 Policy Iteration, Rollout, and Newton’s Method 53 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Optimal cost Cost of rollout policy ˜ 
Policy Evaluation for Policy Evaluation for µk 
and for µk+1 
Cost of µkCost of µk+1 
J µk = T 
µkJµkJ µk+1 = T 
µk+1Jµk+1 
Linearized Bellman Eq. at Linearized Bellman Eq. at J 
µk 
also Newton Step 
Figure 3.4.2 Geometric interpretation of a policy iteration. Starting from the stable current policy µk, it evaluates the corresponding cost function J 
µ k , and 
computes the next policy µk+1 according to 
T µ k+1J 
µ k = TJ 
µ k . 
The corresponding cost function J µ k+1 is obtained as the solution of the linearized 
equation J = T µ k+1J , so it is the result of a Newton step for solving the Bellman 
equation J = TJ , starting from J µ k . Note that in policy iteration, the Newton 
step always starts at a function Jµ, which satisfies Jµ % J" as well as TJµ & Jµ 
(cf. our discussion on stability in Section 3.3). 
Rollout 
Generally, rollout with a stable base policy µ can be viewed as a single iteration of Newton’s method starting from Jµ, as applied to the solution of the Bellman equation (see Fig. 3.4.3). Note that rollout/policy improvement is applied just at the current state during real-time operation of the system. This makes the on-line implementation possible, even for problems with very large state space, provided that the policy evaluation of the base policy can be done on-line as needed. For this we often need on-line deterministic or stochastic simulation from each of the states xk generated by the system in real time. 
As Fig. 3.4.3 illustrates, the cost function of the rollout policy Jµ̃ is obtained by constructing a linearized version of Bellman’s equation at Jµ (its linear approximation at Jµ), and then solving it. If the function TJ 
is nearly linear (i.e., has small “curvature”) the rollout policy performance
54 An Abstract View of Reinforcement Learning Chap. 3 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 1 J J 
Cost-to-go approximation Expected value approximation TµJ 
Cost-to-go approximation Expected value approximation Jµ = TµJµJµ̃ = Tµ̃Jµ̃ 
Policy Improvement with Base Policy Policy Improvement with Base Policy µ 
Linearized Bellman Eq. at Jµ Yields Rollout Policy µ̃ 
Through Tµ̃Jµ = TJµ 
Optimal cost Cost of rollout policy ˜ 
Optimal cost Cost of rollout policy µ̃Optimal cost Cost of r llout policy ˜ Cost of base policy µ 
Policy Evaluation for Policy Evaluation for µ and for ˜ 
µ and for µ̃ 
also Newton Step 
Figure 3.4.3 Geometric interpretation of rollout. Each policy µ defines the linear function TµJ of J , given by Eq. (3.2), and TJ is the function given by Eq. (3.1), which can also be written as TJ = minµ TµJ . The figure shows a policy iteration starting from a base policy µ. It computes Jµ by policy evaluation (by solving the linear equation J = TµJ as shown). It then performs a policy improvement using µ as the base policy to produce the rollout policy µ̃ as shown: the cost function of the rollout policy, Jµ̃, is obtained by solving the version of Bellman’s equation that is linearized at the point Jµ, as in Newton’s method. 
Jµ̃(x) is very close to the optimal J*(x), even if the base policy µ is far from optimal. This explains the large cost improvements that are typically observed in practice with the rollout algorithm. 
An interesting question is how to compare the rollout performance Jµ̃(x) for a given initial state x, with the base policy performance Jµ(x). Clearly, we would like Jµ(x) ( Jµ̃(x) to be large, but this is not the right way to look at cost improvement. The reason is that Jµ(x)( Jµ̃(x) will be small if its upper bound, Jµ(x) ( J*(x), is small, i.e., if the base policy is close to optimal. What is important is that the error ratio 
Jµ̃(x)( J*(x) 
Jµ(x)( J*(x) (3.17) 
is small. Indeed, this ratio becomes smaller as Jµ(x)( J*(x) approaches 0 because of the superlinear convergence rate of Newton’s method that underlies the rollout algorithm (cf. Fig. 3.4.3). Unfortunately, it is hard to evaluate this ratio, since we do not know J*(x). On the other hand, we
Sec. 3.4 Policy Iteration, Rollout, and Newton’s Method 55 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Cost-to-go approximation Expected value approximation TµJ 
Optimal cost Cost of rollout policy ˜ 
J̃ 
Cost of Truncated Rollout Policy ˜ Cost of Truncated Rollout Policy µ̃ 
Stability Region 0 Tm µ J̃J̃ Jµ̃ 
Yields Truncated Rollout Policy µ̃ 
Yields Truncated Rollout Policy ˜ Defined by 
Tµ̃(Tm µ J̃) = T (Tm 
µ J̃) Yields Truncated Rollout Policy ˜ 
1 J J = 2 m = 4 
also Newton Step 
Figure 3.4.4 Geometric interpretation of truncated rollout with one-step lookahead minimization, m value iterations with the base policy µ, and a terminal cost function approximation J̃ (here m = 4). 
should not be underwhelmed if we observe a small performance improvement Jµ(x) ( Jµ̃(x): the reason may be that the base policy is already near-optimal, and in fact we are likely doing very well in terms of the ratio (3.17). 
Truncated Rollout and Optimistic Policy Iteration 
Variants of rollout may involve multistep lookahead, truncation, and terminal cost function approximation, as in the case of AlphaZero/TD-Gammon, cf. Chapter 1. These variants admit geometric interpretations that are similar to the ones given earlier; see Fig. 3.4.4. Truncated rollout uses m VIs with the base policy µ and a terminal cost function approximation J̃ to approximate the cost function Jµ. 
In the case of one-step lookahead, the truncated rollout policy µ̃ is defined by 
Tµ̃(Tm µ J̃) = T (Tm 
µ J̃), (3.18) 
i.e., µ̃ attains the minimum when the Bellman operator T is applied to the function Tm 
µ J̃ (the cost obtained by using the base policy µ for m steps followed by terminal cost approximation J̃); see Fig. 3.4.4. In the case of $-step lookahead, the truncated rollout policy µ̃ is defined by 
Tµ̃(T !$1Tm µ J̃) = T (T !$1Tm 
µ J̃). (3.19)
56 An Abstract View of Reinforcement Learning Chap. 3 
Truncated rollout is related to a variant of PI called optimistic. This variant approximates the policy evaluation step by using m value iterations using the base policy µ; see [BeT96], [Ber12], [Ber19a] for a more detailed discussion of this relation. A method that is related to optimistic PI is the '-PI method, which is related to the proximal algorithm of convex analysis, and is discussed in several of the author’s books ([BeT96], [Ber12], [Ber20a], [Ber22a]), and papers (BeI96], [Ber15], [Ber18d]), and can also be used to define the one-step lookahead policy in place of Eq. (3.18). In particular, Section 6 of the paper [Ber18d] is focused on '-PI methods, which serve as approximations to the ordinary PI/Newton methods for finite-state discounted and SSP problems. 
As noted earlier, variants of Newton’s method that involve multiple fixed point iterations, before and after each Newton step, but without truncated rollout, i.e., 
Tµ̃(T !$1J̃) = T (T !$1J̃), (3.20) 
are well-known. The classical numerical analysis book by Ortega and Rheinboldt [OrR70] (Sections 13.3 and 13.4) provides various convergence results, under assumptions that include di!erentiability and convexity of the components of T , and nonnegativity of the inverse Jacobian of T . These assumptions, particularly di!erentiability, may not be satisfied within our DP context. Moreover, for methods of the form (3.20), the initial point must satisfy an additional assumption, which ensures that the convergence to J* is monotonic from above (in this case, if in addition the Jacobian of T is isotone, an auxiliary sequence can be constructed that converges to J* 
monotonically from below; see [OrR70], 13.3.4, 13.4.2). This is similar to existing convergence results for the optimistic PI method in DP; see e.g., [BeT96], [Ber12]. 
Geometrical interpretations such as the ones of Fig. 3.4.4 suggest, among others, that: 
(a) The cost improvement Jµ ( Jµ̃, from base to rollout policy, tends to become larger as the length $ of the lookahead increases. 
(b) Truncated rollout with $-step lookahead minimization, followed by m 
steps of a base policy µ, and then followed by terminal cost function approximation J̃ may be viewed, under certain conditions, as an economic alternative to ($+m)-step lookahead minimization using J̃ as terminal cost function approximation. 
Figure 3.4.5 illustrates in summary the approximation in value space scheme with $-step lookahead minimization and m-step truncated rollout [cf. Eq. (3.19)], and its connection to Newton’s method. This figure indicates the parts that are ordinarily associated with on-line play and o!-line training, and parallels our earlier Fig. 1.2.1, which applies to AlphaZero, TD-Gammon, and related on-line schemes.
Sec. 3.4 Policy Iteration, Rollout, and Newton’s Method 57 
Base Heuristic Truncated Rollout 
Base Heuristic Truncated Rollout 
. . .Current Position xk 
ON-LINE PLAY 
ON-LINE PLAY 
OFF-LINE TRAINING 
OFF-LINE TRAININGON-LINE PLAY Lookahead Tree States xk+1 
Current Position 
States xk+2 
NEWTON STEP 
NEWTON STEP 
NEWTON STEP for Bellman Eq. 
2-Step Lookahead Minimization 
O!-Line Obtained Player O 6 13 14 24 27 by Rollout by Simulation Base Policy Cost Function 
Cost Function Approximation Cost Function Approximation J̃ 
Enhancements to the Starting Point of Newton Step Enhancements to the Starting Point of Newton Step 
e.g., !! 1 Lookahead Minimization Steps 1 Lookahead Minimization Steps m Steps of Rollout 
Multistep Lookahead Policy Cost !-Step Lookahead 
Steps m Steps 
Figure 3.4.5 Illustration of the approximation in value space scheme with "-step lookahead minimization (" = 2 in the figure) and m-step truncated rollout [cf. Eq. (3.19)], and its connection to Newton’s method. The Newton step for solving the Bellman equation J" = TJ" corresponds to the first (out of " steps of) lookahead minimization. The remaining "#1 steps of lookahead minimization (VI iterations), and the m truncated rollout steps (VI iterations with the base policy), improve the starting point of the Newton step, from its o!-line-obtained cost function approximation J̃ . 
Lookahead Length Issues in Truncated Rollout 
A question of practical interest is how to choose the lookahead lengths $ and m in truncated rollout schemes. It is clear that large values $ for lookahead minimization are beneficial (in the sense of producing improved lookahead policy cost functions Jµ̃), since additional VI iterations bring closer to J* 
the starting point T !$1J̃ of the Newton step. Note, however, that while long lookahead minimization is computationally expensive (its complexity increases exponentially with $), it is only the first stage of the multistep lookahead that contributes to the Newton step, while the remaining $ ( 1 steps are far less e!ective first order/VI iterations. 
Regarding the value of m, long truncated rollout brings the starting point for the Newton step closer to Jµ, but not necessarily closer to J*, as indicated by Fig. 3.4.4. Indeed computational experiments suggest that increasing values for m may be counterproductive beyond some threshold, and that this threshold generally depends on the problem and the terminal cost approximation J̃ ; see also our subsequent discussion for linear quadratic problems in Section 4.6. This is also consistent with long stand-
58 An Abstract View of Reinforcement Learning Chap. 3 
ing experience with optimistic policy iteration, which is closely connected with truncated rollout, as noted earlier. Unfortunately, however, there is no analysis that can illuminate this issue, and the available error bounds for truncated rollout (see [Ber19a], [Ber20a]) are conservative and provide limited guidance in this regard. 
Another important fact to keep in mind is that the truncated rollout steps are much less demanding computationally than the lookahead minimization steps. Thus, with other concerns weighing equally, it is computationally preferable to use large values of m rather than large values of $ (this was the underlying motivation for truncated rollout in Tesauro’s TD-Gammon [TeG96]). On the other hand, while large values of m may be computationally tolerable in some cases, it is possible that even relatively small values of m can be computationally prohibitive. This is especially true for stochastic problems where the width of the lookahead graph tends to grow quickly. 
An interesting property, which holds in some generality, is that truncated rollout with a stable policy has a beneficial e"ect on the stability properties of the lookahead policy. The reason is that the cost function Jµ of the base policy µ lies well inside the region of stability, as noted in Section 3.2. Moreover value iterations with µ (i.e., truncated rollout) tend to push the starting point of the Newton step towards Jµ. Thus a su"cient number of these value iterations will bring the starting point of the Newton step within the region of stability. 
The preceding discussion suggests the following qualitative question: is lookahead by rollout an economic substitute for lookahead by minimization? The answer to this seems to be a qualified yes: for a given computational budget, judiciously balancing the values of m and $ tends to give better lookahead policy performance than simply increasing $ as much as possible, while setting m = 0 (which corresponds to no rollout). This is consistent with intuition obtained through geometric constructions such as Fig. 3.4.4, but it is di"cult to establish conclusively. We discuss this issue further in Section 4.6 for the case of linear quadratic problems. 
3.5 HOW SENSITIVE IS ON-LINE PLAY TO THE OFF-LINE TRAINING PROCESS? 
An important issue to consider in approximation in value space is errors in the one-step or multistep minimization, or in the choice of terminal cost approximation J̃ . Such errors are often unavoidable because the control constraint set U(x) is infinite, or because the minimization is simplified for reasons of computational expediency (see our subsequent discussion of multiagent problems). Moreover, to these errors, we may add the e!ect of errors due to rollout truncation, and errors due to changes in problem parameters, which are reflected in changes in Bellman’s equation (see our subsequent discussion of robust and adaptive control).
Sec. 3.5 How Sensitive is On-Line Play? 59 
Base Policy Rollout Policy Approximation in Value Space Base Policy Rollout Policy Approximation in Value Space 
Base Policy Rollout Policy Approximation in Value SpaceBase P licy Roll ut Policy Ap roximation in Value Space Base Policy Rollout Policy Approximation in Value S acepproxi ation in Policy 
Cost Data Policy Data System: 
x µ 
Rollout Policy µ̃ 
Value Network Policy Network Value Data 
-Step Value Network Policy Network-St p Value Network Policy Network 
Figure 3.5.1 Schematic illustration of approximate PI. Either the policy evaluation and policy improvement phases (or both) are approximated with a value or a policy network, respectively. These could be neural networks, which are trained with (state, cost function value) data that is generated using the current base policy µ, and with (state, rollout policy control) data that is generated using the rollout policy µ̃. 
Note that there are three di!erent types of approximate implementation involving: 1) a value network but no policy network (here the value network defines a policy via one-step or multistep lookahead), or 2) a policy network but no value network (here the policy network has a corresponding value function that can be computed by rollout), or 3) both a policy and a value network (the approximation architecture of AlphaZero is a case in point). 
Under these circumstances the linearization of the Bellman equation at the point J̃ in Fig. 3.4.4 is perturbed, and the corresponding point Tm 
µ J̃ 
in Fig. 3.4.4 is also perturbed. However, the e!ect of these perturbations tends to be mitigated by the Newton step that produces the policy µ̃ and the corresponding cost function Jµ̃. The Newton step has a superlinear convergence property, so for an O(()-order error [i.e., O(()/( stays bounded as ( $ 0] in the calculation of Tm 
µ J̃ , the error in Jµ̃ will be of the much smaller order o(() [i.e., o(()/( $ 0 as ( $ 0], when Jµ̃ is near J*.† This is a significant insight, as it suggests that extreme accuracy and fine-tuning of the choice of J̃ may not produce significant e"ects in the resulting performance of the one-step and particularly a multistep lookahead policy; see also the quantitative analysis for linear quadratic problems in Section 4.5. 
Approximate Policy Iteration and Implementation Errors 
Both policy evaluation and policy improvement can be approximated, possibly by using training with data and approximation architectures, such as neural networks; see Fig. 3.5.1. Other approximations include simulation-based methods such as truncated rollout, and temporal di!erence methods 
† A rigorous proof of this requires di"erentiability of T at J̃ . Since T is di"erentiable at almost all points J , the sensitivity property just stated, will 
likely hold in practice even if T is not di"erentiable. See the appendix, which 
also compares global and local error bounds for approximation in value space, and for approximate PI (cf. Sections A.3 and A.4)
60 An Abstract View of Reinforcement Learning Chap. 3 
for policy evaluation, which involve the use of basis functions. Moreover, multistep lookahead may be used in place of one-step lookahead, and simplified minimization, based for example on multiagent rollout, may also be used. Let us also mention the possibility of a combined rollout and PI algorithm, whereby we use PI for on-line policy improvement of the base policy, by using data collected during the rollout process. This idea is relatively new and has not been tested extensively; see the subsequent discussion in Section 3.8 and the author’s paper [Ber21a]. 
Long-standing practical experience with approximate PI is consistent with the view of the e!ect of implementation errors outlined above, and suggests that substantial changes in the policy evaluation and policy improvement operations often have small but largely unpredictable e!ects on the performance of the policies generated. For example, when TD(')-type methods are used for policy evaluation, the choice of ' has a large e!ect on the corresponding policy cost function approximations, but often has little and unpredictable e!ect on the performance of the generated policies through on-line play. A plausible conjecture here is that the superlinear convergence property of the exact Newton step “smooths out” the e!ect of o!-line approximation errors. 
3.6 WHY NOT JUST TRAIN A POLICY NETWORK AND USE IT WITHOUT ON-LINE PLAY? 
This is a sensible and common question, which stems from the mindset that neural networks have extraordinary function approximation properties. In other words, why go through the arduous on-line process of lookahead minimization, if we can do the same thing o!-line and represent the lookahead policy with a trained policy network? More generally, it is possible to use approximation in policy space, a major alternative approach to approximation in value space, whereby we select the policy from a suitably restricted class of policies, such as a parametric class of the form µ(x, r), where r is a parameter vector. We may then estimate r using some type of o!-line training process. There are quite a few methods for performing this type of training, such as policy gradient and random search methods (see the books [SuB18] and [Ber19a] for an overview). Alternatively, some approximate DP or classical control system design method may be used. 
An important advantage of approximation in policy space is that once the parametrized policy is obtained, the on-line computation of controls µ(x, r) is often much faster compared with on-line lookahead minimization. For this reason, approximation in policy space can be used to provide an approximate implementation of a known policy (no matter how obtained) for the purpose of convenient use. On the negative side, because parametrized approximations often involve substantial calculations, they are not well suited for on-line replanning.
Sec. 3.7 Multiagent Problems and Multiagent Rollout 61 
-1 -0.8 -0.6 -0.4 -0.2 0 0 
2 
4 
6 
8 
10 
12 
Linear policy parameter 
Without the Newton Step 
With the Newton Step 
Linear policy parameter Optimal 
Figure 3.6.1 Illustration of the performance enhancement obtained by rollout with an o!-line trained base policy for the linear quadratic problem. Here the system equation is xk+1 = xk +2uk, and the cost function parameters are q = 1, r = 0.5. The optimal policy is µ"(x) = L"x with L" ' #0.4, and the optimal cost function is J"(x) = K"x2, where K" ' 1.1. We consider policies of the form µ(x) = Lx, where L is the parameter, with cost function of the form Jµ(x) = KLx 
2. The figure shows the quadratic cost coe"cient di!erences KL # K" and K 
L̃ #K" as a function of L, where KL and K 
L̃ are the quadratic cost coe"cients 
of µ (without one-step lookahead/Newton step) and the corresponding one-step lookahead policy µ̃ (with one-step lookahead/Newton step). 
From our point of view in this book, there is another important reason why approximation in value space is needed on top of approximation in policy space: the o"-line trained policy may not perform nearly as well as the corresponding one-step or multistep lookahead/rollout policy, because it lacks the extra power of the associated exact Newton step (cf. our discussion of AlphaZero and TD-Gammon in Chapter 1). Figure 3.6.1 illustrates this fact with a one-dimensional linear-quadratic example, and compares the performance of a linear policy, defined by a scalar parameter, with its corresponding one-step lookahead policy. 
3.7 MULTIAGENT PROBLEMS AND MULTIAGENT ROLLOUT 
A major di"culty in the implementation of value space approximation with one-step lookahead is the minimization operation over U(x) at a state x. When U(x) is infinite, or even when it is finite but has a very large number of elements, the minimization may become prohibitively time consuming. In the case of multistep lookahead the computational di"culty becomes even more acute. In this section we discuss how to deal with this di"culty when the control u consists of m components, u = (u1, . . . , um), with a separable control constraint for each component, u! " U!(x), $ = 1, . . . ,m.
62 An Abstract View of Reinforcement Learning Chap. 3 
2 Agent 1 Agent 
State InfoState Info State Info 
Agent 2 Agent 3 Agent 4 Agent 5 
Agent 2 Agent 3 Agent 4 Agent 5 
Agent 2 Agent 3 Agent 4 Agent 5 
Agent 2 Agent 3 Agent 4 Agent 5 
Agent 2 Agent 3 Agent 4 Agent 5 Environment Computing Cloud Environment Computing Cloud 
+1u1 
u2 
u3 
u4 
u5 
Single policy Info 
Single policy Info Single policy Info 
Single policy InfoSingle policy Info 
Single policy Info 
Single policy InfoSingle policy Info 
Figure 3.7.1 Schematic illustration of a multiagent problem. There are multiple “agents,” and each agent " = 1, . . . ,m, controls its own decision variable u!. At each stage, agents exchange new information and also exchange information with the “environment,” and then select their decision variables for the stage. 
Thus the control constraint set is the Cartesian product 
U(x) = U1(x)& · · ·& Um(x), (3.21) 
where the sets U!(x) are given. This structure is inspired by applications involving distributed decision making by multiple agents with communication and coordination between the agents; see Fig. 3.7.1. 
To illustrate our approach, let us consider the discounted infinite horizon problem, and for the sake of the following discussion, assume that each set U!(x) is finite. Then the one-step lookahead minimization of the standard rollout scheme with base policy µ is given by 
ũ " arg min u!U(x) 
E 
! 
g(x, u, w) + !Jµ " 
f(x, u, w) # 
$ 
, (3.22) 
and involves as many as nm terms, where n is the maximum number of elements of the sets U!(x) [so that nm is an upper bound to the number of controls in U(x), in view of its Cartesian product structure (3.21)]. Thus the standard rollout algorithm requires an exponential [order O(nm)] number of computations per stage, which can be overwhelming even for moderate values of m. 
This potentially large computational overhead motivates a far more computationally e"cient rollout algorithm, whereby the one-step lookahead minimization (3.22) is replaced by a sequence of m successive minimizations, one-agent-at-a-time, with the results incorporated into the subsequent minimizations. In particular, at state x we perform the sequence of
Sec. 3.7 Multiagent Problems and Multiagent Rollout 63 
minimizations 
µ̃1(x) " arg min u1!U1(x) 
Ew 
! 
g " 
x, u1, µ2(x), . . . , µm(x), w # 
+ !Jµ " 
f(x, u1, µ2(x), . . . , µm(x), w) # 
$ 
, 
µ̃2(x) " arg min u2!U2(x) 
Ew 
! 
g " 
x, µ̃1(x), u2, µ3(x) . . . , µm(x), w # 
+ !Jµ " 
f(x, µ̃1(x), u2, µ3(x), . . . , µm(x), w) # 
$ 
, 
. . . . . . . . . . . . 
µ̃m(x) " arg min um!Um(x) 
Ew 
! 
g " 
x, µ̃1(x), µ̃2(x), . . . , µ̃m$1(x), um, w # 
+ !Jµ " 
f(x, µ̃1(x), µ̃2(x), . . . , µ̃m$1(x), um, w) # 
$ 
. 
Thus each agent component u! is obtained by a minimization with the preceding agent components u1, . . . , u!$1 fixed at the previously computed values of the rollout policy, and the following agent components u!+1, . . . , um 
fixed at the values given by the base policy. This algorithm requires order O(nm) computations per stage, a potentially huge computational saving over the order O(nm) computations required by standard rollout. 
A key idea here is that the computational requirements of the rollout one-step minimization (3.22) are proportional to the number of controls in the set U(x) and are independent of the size of the state space. This motivates a reformulation of the problem, first suggested in the book [BeT96], Section 6.1.4, whereby control space complexity is traded o! with state space complexity, by “unfolding” the control uk into its m components, which are applied one-agent-at-a-time rather than all-agents-at-once. 
In particular, we can reformulate the problem by breaking down the collective decision uk into m sequential component decisions, thereby reducing the complexity of the control space while increasing the complexity of the state space. The potential advantage is that the extra state space complexity does not a!ect the computational requirements of some RL algorithms, including rollout. 
To this end, we introduce a modified but equivalent problem, involving one-at-a-time agent control selection. At the generic state x, we break down the control u into the sequence of the m controls u1, u2, . . . , um, and between x and the next state x̄ = f(x, u, w), we introduce artificial intermediate “states” (x, u1), (x, u1, u2), . . . , (x, u1, . . . , um$1), and corresponding transitions. The choice of the last control component um at “state” (x, u1, . . . , um$1) marks the transition to the next state x̄ = f(x, u, w) according to the system equation, while incurring cost g(x, u, w); see Fig. 3.7.2. 
It is evident that this reformulated problem is equivalent to the original, since any control choice that is possible in one problem is also possible
64 An Abstract View of Reinforcement Learning Chap. 3 
3 Cost 0 Cost 
3 Cost 0 Cost 
Base Heuristic Minimization Possible Path Reformulated State Space 
Base Heuristic Minimization Possible Path Reformulated State Space 
Base Heuristic Minimization Possible P th Reformulated State Space 
Base Heuristic Minimization Possible P th Reformulated State Space 
Base Heuristic Minimization Possible Path Reformulated State Space 
Base Heuristic Minimization Possible Path Reformulated State Space 
B s Heuristic Minimization Possible Path Reformulated State Space 
B s Heuristic Minimization Possible Path Reformulated State Space 
Agent 1 Agent 2 Agent 3 
Agent 1 Agent 2 Agent 3 
Agent 1 Agent 2 Agent 3 
u1 
1 u2 
2 u3 
x x, u 
1 x, u1, u2 
3 x, u1 
x x, u 
1 x, u1, u2 
3 x, u1 
x x, u 
1 x, u1, u2 
3 x, u1 
x x, u 
1 x, u1, u2 
3 x, u1 
Cost 0 Cost g(x, u, y) 
Figure 3.7.2 Equivalent formulation of the stochastic optimal control problem for the case where the control u consists of m components u1, u2, . . . , um: 
u = (u1, . . . , um) " U1(xk)! · · ·! Um(xk). 
The figure depicts the kth stage transitions. Starting from state x, we generate the intermediate states 
(x, u1), (xk, u1, u2), . . . , (x, u1, . . . , um$1), 
using the respective controls u1, . . . , um$1. The final control um leads from (x, u1, . . . , um$1) to x̄ = f(x, u,w), and the random cost g(x, u,w) is incurred. 
in the other problem, while the cost structure of the two problems is the same. In particular, every policy 
" 
µ1(x), . . . , µm(x) # 
of the original problem, is admissible for the reformulated problem, and has the same cost function for the original as well as the reformulated problem. Reversely, every policy for the reformulated problem can be converted into a policy for the original problem that produces the same state and control trajectories and has the same cost function. 
The motivation for the reformulated problem is that the control space is simplified at the expense of introducing m(1 additional layers of states, and the corresponding m( 1 cost functions 
J1(x, u1), J2(x, u1, u2), . . . , Jm$1(x, u1, . . . , um$1). 
The increase in size of the state space does not adversely a!ect the operation of rollout, since the minimization (3.22) is performed for just one state at each stage. 
A major fact that follows from the preceding reformulation is that despite the dramatic reduction in computational cost, multiagent rollout still achieves cost improvement : 
Jµ̃(x) * Jµ(x), for all x, 
where Jµ(x) is the cost function of the base policy µ = (µ1, . . . , µm), and Jµ̃(x) is the cost function of the rollout policy µ̃ = (µ̃1, . . . , µ̃m), starting
Sec. 3.7 Multiagent Problems and Multiagent Rollout 65 
from state x. Furthermore, this cost improvement property can be extended to multiagent PI schemes that involve one-agent-at-a-time policy improvement operations, and have sound convergence properties (see the book [Ber20a], Chapters 3 and 5, as well as the author’s papers [Ber19b], [Ber19c], [Ber20b], [Ber21b], and the paper by Bhatacharya et al. [BKB20]). 
Another fact that follows from the preceding reformulation is that multiagent rollout may be viewed as a Newton step applied to the Bellman equation that corresponds to the reformulated problem, with starting point Jµ. This is very important for our purposes in the context of this book. In particular, the superlinear cost improvement of the Newton step can still be obtained through multiagent rollout , even though the amount of computation for the lookahead minimization is dramatically reduced through one-agent-at-a-time minimization. This explains experimental results given in the paper [BKB20], which have shown comparable performance for multiagent and standard rollout in the context of a large-scale multi-robot POMDP application. 
Let us also mention that multiagent rollout can become the starting point for various related PI schemes that are well suited for distributed operation in important practical contexts involving multiple autonomous decision makers (see the book [Ber20a], Section 5.3.4, and the papers [Ber21b]). 
Multiagent Approximation in Value Space 
Let us now consider the reformulated problem of Fig. 3.7.2 and see how we can apply approximation in value space with one-step lookahead minimization, truncated rollout with a base policy µ = (µ1, . . . , µm), and terminal cost function approximation J̃ . 
In one such scheme that involves one-agent-at-a-time minimization, at state x we perform the sequence of minimizations 
ũ1 " arg min u1!U1(x) 
Ew 
! 
g " 
x, u1, µ2(x), . . . , µm(x), w # 
+ !J̃ " 
f(x, u1, µ2(x), . . . , µm(x), w) # 
$ 
, 
ũ2 " arg min u2!U2(x) 
Ew 
! 
g " 
x, ũ1, u2, µ3(x) . . . , µm(x), w # 
+ !J̃ " 
f(x, ũ1, u2, µ3(x), . . . , µm(x), w) # 
$ 
, 
. . . . . . . . . . . . 
ũm " arg min um!Um(x) 
Ew 
! 
g " 
x, ũ1, ũ2, . . . , ũm$1, um, w # 
+ !J̃ " 
f(x, ũ1, ũ2, . . . , ũm$1, um, w) # 
$ 
. 
In the context of the reformulated problem, this is a sequence of one-step lookahead minimizations at the states x, (x, ũ0), . . . , (x, ũ0, . . . , ũm$1) of
66 An Abstract View of Reinforcement Learning Chap. 3 
the reformulated problem, using truncated rollout with base policy µ of corresponding length m( 1,m( 2, . . . , 0. The Newton step interpretation of Section 3.4 and Fig. 3.4.4 still applies, with its superlinear convergence rate. At the same time, the computational requirements are dramatically reduced, similar to the multiagent rollout method discussed earlier. 
Let us finally note that there are variations of the multiagent schemes of this section, which involve multistep lookahead minimization as well as truncated rollout. They likely result in better performance at the expense of greater computational cost. 
3.8 ON-LINE SIMPLIFIED POLICY ITERATION 
In this section, we describe some variants of the PI algorithm, introduced in the author’s recent paper [Ber21a], which are consistent with the approximation in value space theme of this work. The salient feature of these variants is that they involve an exact Newton step and are suitable for online implementation, while still maintaining the principal character of PI, which we have viewed so far as an o!-line algorithm. 
Thus the algorithms of this section involve training and self-improve-ment through on-line experience. They are also simplified relative to standard PI in two ways: 
(a) They perform policy improvement operations only for the states that are encountered during the on-line operation of the system. 
(b) The policy improvement operation is simplified in that it uses approximate minimization in the Bellman equation of the current policy at the current state. 
Despite these simplifications, we show that our algorithms generate a sequence of improved policies, which converge to a policy with a local optimality property. Moreover, with an enhancement of the policy improvement operation, which involves a form of exploration, they converge to a globally optimal policy. 
The motivation comes from the rollout algorithm, which starts from some available base policy and implements on-line an improved rollout policy. In the algorithm of the present section, the data accumulated from the rollout implementation are used to improve on-line the base policy, and to asymptotically obtain a policy that is either locally or globally optimal. 
We focus on a finite-state discounted Markov decision problem, with states 1, . . . , n, and we use a transition probability notation. We denote states by the symbol x and successor states by the symbol y. The con-trol/action is denoted by u, and is constrained to take values in a given finite constraint set U(x), which may depend on the current state x. The use of a control u at state x specifies the transition probability pxy(u) to the next state y, at a cost g(x, u, y).
Sec. 3.8 On-Line Simplified Policy Iteration 67 
The cost of a policy µ starting from state x0 is given by 
Jµ(x0) = lim N'% 
E 
-
N$1 % 
k=0 
!kg " 
xk, µ(xk), xk+1 
# 
* 
* 
* x0, µ 
. 
, x0 = 1, . . . , n, 
where ! < 1 is the discount factor. As earlier, Jµ is viewed as the vector in the n-dimensional Euclidean space 'n, with components Jµ(1), . . . , Jµ(n). 
In terms of our abstract notation, for each policy µ, the Bellman operator Tµ maps a vector J " 'n to the vector TµJ " 'n that has components 
(TµJ)(x) = n % 
y=1 
pxy " 
µ(x) # 
+ 
g(x, µ(x), y) + !J(y) , 
, x = 1, . . . , n. 
(3.23) The Bellman operator T : 'n #$ 'n is given by 
(TJ)(x) = min u!U(x) 
n % 
y=1 
pxy(u) " 
g(x, u, y) + !J(y) # 
, x = 1, . . . , n. (3.24) 
For the discounted problem that we consider, the operators Tµ and T 
are sup-norm contractions (generally this is true for discounted problems with bounded cost per stage [Ber22a]; in our context, the number of states is finite, so the cost per stage is bounded). Thus Jµ is the unique solution of Bellman’s equation J = TµJ , or equivalently 
Jµ(x) = n % 
y=1 
pxy " 
µ(x) # 
+ 
g " 
x, µ(x), y # 
+ !Jµ(y) , 
, x = 1, . . . , n. (3.25) 
Moreover, J* is the unique solution of Bellman’s equation J = TJ , so that 
J#(x) = min u!U(x) 
n % 
y=1 
pxy(u) " 
g(x, u, y) + !J#(y) # 
, x = 1, . . . , n. (3.26) 
Furthermore, the following optimality conditions hold 
TµJ* = TJ* if and only if µ is optimal, (3.27) 
TµJµ = TJµ if and only if µ is optimal. (3.28) 
The contraction property also implies that the VI algorithms 
Jk+1 = TµJk, Jk+1 = TJk 
generate sequences {Jk} that converge to Jµ and J#, respectively, from any starting vector J0 " 'n.
68 An Abstract View of Reinforcement Learning Chap. 3 
As discussed earlier, in the PI algorithm, the current policy µ is improved by finding µ̃ that satisfies 
Tµ̃Jµ = TJµ 
[i.e., by minimizing for all x in the right-hand side of Eq. (3.24) with Jµ 
in place of J ]. The improved policy µ̃ is evaluated by solving the linear n & n system of equations Jµ̃ = Tµ̃Jµ̃, and then (Jµ̃, µ̃) becomes the new cost vector-policy pair, which is used to start a new iteration. Thus the PI algorithm starts with a policy µ0 and generates a sequence {µk} according to 
Jµk = TµkJµk , Tµk+1Jµk = TJµk . (3.29) 
We now introduce an on-line variant of PI, which starts at time 0 with a state-policy pair (x0, µ0) and generates on-line a sequence of state-policy pairs (xk, µ 
k). We view xk as the current state of a system operating online under the influence of the policies µ1, µ2, . . .. In our algorithm, µk+1 may di"er from µk only at state xk. The control µk+1(xk) and the state xk+1 
are generated as follows: We consider the right-hand sides of Bellman’s equation for µk (also 
known as Q-factors of µk) 
Qµk(xk, u) = n % 
y=1 
px k y(u) 
" 
g(xk, u, y) + !Jµk (y) # 
, (3.30) 
and we select the control µk+1(xk) from within the constraint set U(xk) with su"cient accuracy to satisfy the following condition 
Qµk 
" 
xk, µ k+1(xk) 
# 
* Jµk(xk), (3.31) 
with strict inequality whenever this is possible.† For x += xk the policy controls are not changed: 
µk+1(x) = µk(x) for all x += xk. 
The next state xk+1 is generated randomly according to the transition probabilities px 
k x k+1 
" 
µk+1(xk) # 
. 
† By this we mean that if minu#U(x k ) Qµ 
k (xk, u) < J µ k (xk) we select a con-
trol uk that satisfies Q 
µ k (xk, uk) < J 
µ k (xk), (3.32) 
and set µk+1(xk) = uk, and otherwise we set µk+1(xk) = µk(xk) [so Eq. (3.31) is satisfied]. Such a control selection may be obtained by a number of schemes, 
including brute force calculation and random search based on Bayesian optimization. The needed values of the Q-factor Q 
µ k and cost J 
µ k may be obtained in 
several ways, depending on the problem at hand, including by on-line simulation.
Sec. 3.8 On-Line Simplified Policy Iteration 69 
We first show that the current policy is monotonically improved, i.e., that 
Jµk+1(x) * Jµk(x), for all x and k, 
with strict inequality for x = xk (and possibly other values of x) if 
min u!U(x 
k ) 
Qµk(xk, u) < Jµk (xk). 
To prove this, we note that the policy update is done under the condition (3.31). By using the monotonicity of Tµk+1 , we have for all $ ! 1, 
T !+1 
µk+1Jµk * T ! µk+1Jµk * Jµk , (3.33) 
so by taking the limit as $ $ % and by using the convergence property of VI (T ! 
µk+1J $ Jµk+1 for any J), we obtain Jµk+1 * Jµk . Moreover, the 
algorithm selects µk+1(xk) so that 
(Tµk+1Jµk)(xk) = Qµk(xk, uk) < Jµk (xk) 
if min 
u!U(x k ) 
Qµk(xk, u) < Jµk (xk), 
[cf. Eq. (3.32)], and then by using Eq. (3.33), we have Jµk+1(xk) < Jµk (xk). 
Local Optimality 
We next discuss the convergence and optimality properties of the algorithm. We introduce a definition of local optimality of a policy, whereby the policy selects controls optimally only within a subset of states. 
Given a subset of states S and a policy µ, we say that µ is locally optimal over S if µ is optimal for the problem where the control is restricted to take the value µ(x) at the states x /" S, and is allowed to take any value u " U(x) at the states x " S. 
Roughly speaking, µ is locally optimal over S, if µ is acting optimally within S, but under the (incorrect) assumption that once the state of the system gets to a state x outside S, there will be no option to select control other than µ(x). Thus if the choices of µ outside of S are poor, its choices within S may also be poor. 
Mathematically, µ is locally optimal over S if 
Jµ(x) = min u!U(x) 
n % 
y=1 
pxy(u) " 
g(x, u, y) + !Jµ(y) # 
, for all x " S, 
Jµ(x) = n % 
y=1 
pxy " 
µ(x) # 
+ 
g " 
x, µ(x), y # 
+ !Jµ(y) , 
, for all x /" S,
70 An Abstract View of Reinforcement Learning Chap. 3 
which can be written compactly as 
(TµJµ)(x) = (TJµ)(x), for all x " S. (3.34) 
Note that this is di!erent than (global) optimality of µ, which holds if and only if the above condition holds for all x = 1, . . . , n, rather than just for x " S [cf. Eq. (3.28)]. However, it can be seen that a (globally) optimal policy is also locally optimal within any subset of states. 
Our main convergence result is the following. 
Proposition 3.8.1: Let S be the subset of states that are repeated infinitely often within the sequence {xk}. Then the corresponding sequence {µk} converges finitely to some policy µ in the sense that µk = µ for all k after some index k. Moreover µ is locally optimal within S, while S is invariant under µ, in the sense that 
pxy " 
µ(x) # 
= 0 for all x " S and y /" S. 
Proof: The cost function sequence {Jµk} is monotonically nonincreasing, as shown earlier. Moreover, the number of policies µ is finite in view of the finiteness of the state and control spaces. Therefore, the number of corresponding functions Jµ is also finite, so Jµk converges in a finite 
number of steps to some J̄ , which in view of the algorithm’s construction [selecting uk = µk(xk) if minu!U(x 
k ) Qµk(xk, u) = Jµk (xk); cf. Eq. (3.32)], 
implies that µk will remain unchanged at some µ with Jµ = J̄ after some su"ciently large k. 
We will show that the local optimality condition (3.34) holds for S = S and µ = µ. In particular, we have xk " S and µk = µ for all k greater than some index, while for every x " S, we have xk = x for infinitely many k. It follows that for all x " S, 
Qµ 
" 
x, µ(x) # 
= Jµ(x), (3.35) 
while by the construction of the algorithm, 
Qµ 
" 
x, u # 
! Jµ(x), for all u " U(x), (3.36) 
since the reverse would imply that µk+1(x) += µk(x) for infinitely many k 
[cf. Eq. (3.32)]. Condition (3.35) can be written as Jµ(x) = (TµJµ)(x) for all x " S, and combined with Eq. (3.36), implies that 
(TµJµ)(x) = (TJµ)(x), for all x " S.
Sec. 3.8 On-Line Simplified Policy Iteration 71 
This is the local optimality condition (3.34) with S = S and µ = µ. To show that S is invariant under µ, we argue by contradiction: if 
this were not so, there would exist a state x " S and a state y /" S such that pxy 
" 
µ(x) # 
> 0, implying that y would be generated following the occurrence of x infinitely often within the sequence {xk}, and hence would have to belong to S (by the definition of S). Q.E.D. 
Note an implication of the invariance property of the set S shown in the preceding proposition. We have that µ is (globally) optimal under the assumption that for every policy there does not exist any strict subset of states that is invariant. 
A Counterexample to Global Optimality 
The following deterministic example (given to us by Yuchao Li) shows that the policy µ obtained by the algorithm need not be (globally) optimal. Here there are three states 1, 2, and 3. From state 1 we can go to state 2 at cost 1, and to state 3 at cost 0, from state 2 we can go to states 1 and 3 at cost 0, and from state 3 we can go to state 2 at cost 0 or stay in 3 at a high cost (say 10). The discount factor is ! = 0.9. Then it can be verified that the optimal policy is 
µ#(1) : Go to 3, µ#(2) : Go to 3, µ#(3) : Go to 2, 
with optimal costs J#(1) = J#(2) = J#(3) = 0, 
while the policy 
µ(1) : Go to 2, µ(2) : Go to 1, µ(3) : Stay at 3, 
is strictly suboptimal, but is locally optimal over the set of states S = {1, 2}. Moreover our on-line PI algorithm, starting from state 1 and the policy µ0 = µ, oscillates between the states 1 and 2, and leaves the policy µ0 unchanged. Note also that S is invariant under µ, consistent with Prop. 3.8.1. 
On-Line Variants of Policy Iteration with Global Optimality Properties 
To address the local versus global convergence issue illustrated by the preceding example, we consider an alternative scheme, whereby in addition to uk, we generate an additional control at a randomly chosen state xk += xk.† In particular, assume that at each time k, in addition to uk and xk+1 that 
† It is also possible to choose multiple additional states at time k for a policy improvement operation, and this is well-suited for the use of parallel computation.
72 An Abstract View of Reinforcement Learning Chap. 3 
are generated according to Eq. (3.32), the algorithm generates randomly another state xk (all states are selected with positive probability), performs a policy improvement operation at that state as well, and modifies accordingly µk+1(xk). Thus, in addition to a policy improvement operation at each state within the generated sequence {xk}, there is an additional policy improvement operation at each state within the randomly generated sequence {xk}. 
Because of the random mechanism of selecting xk, it follows that at every state there will be a policy improvement operation infinitely often, which implies that the policy µ ultimately obtained is (globally) optimal. Note also that we may view the random generation of the sequence {xk} as a form of exploration. The probabilistic mechanism for generating the random sequence {xk} may be guided by some heuristic reasoning, which aims to explore states with high cost improvement potential. 
Let us also note the possibility of approximate implementations of the algorithms described above. In particular, one may start with some base policy, which may be periodically updated using some approximation in policy space scheme, while incorporating the policy improvement data generated so far. As long as the most recent policy improvement results are maintained for the states that have been encountered in the past, the convergence results described above will be maintained. 
Finally, let us mention that the idea of on-line PI of the present section can be extended to a broader algorithmic context of on-line improvement of the approximation in value space process . In particular, we may consider starting the on-line play algorithm with a cost function approximation J̃ , obtained through some o!-line training process. We may then try to gradually enhance the quality of J̃ through on-line experience. For example, J̃ may be constructed through some form of machine learning or Bayesian optimization method that is capable of improving the approximation using data obtained in the process of on-line play. There are many possibilities along these lines, and they are a fruitful area of research, particularly within the context of specific applications. 
3.9 EXCEPTIONAL CASES 
Let us now consider situations where exceptional behavior occurs. One such situation is when the Bellman equation J = TJ has multiple solutions. Then the VI algorithm, when started at one of these solutions will stay at that solution. More generally, it may be unclear whether the VI algorithm will converge to J*, even when started at seemingly favorable initial conditions. Other types of exceptional behavior may also occur, including cases where the Bellman equation has no solution within the set of real-valued functions. The most unusual case of all is when J* is realvalued but does not satisfy the Bellman equation J = TJ , which in turn has other real-valued solutions; see [BeY16] and [Ber22a], Section 3.1. This is a
Sec. 3.9 Exceptional Cases 73 
a 1 2 1 2 t b 
Prob. u2 
u Destination 
2 Prob. 1! u 2 
2 
2 Control u ! (0, 1] Cost 1] Cost !u 
Figure 3.9.1. Transition diagram for the blackmailer problem. At state 1, the blackmailer may demand any amount u " (0, 1]. The victim will comply with probability 1 # u2 and will not comply with probability u2, in which case the process will terminate. 
highly unusual phenomenon, which will not be discussed here. It need not be of practical concern, as it arises only in artificial examples; see [BeY16]. Still it illustrates the surprising range of exceptional situations that should be taken into account in theoretical analyses and computational studies. 
In this section we provide some examples that illustrate the mechanism by which exceptional behavior in infinite horizon DP can occur, and we highlight the need for rigorous analysis of RL methods when used in contexts that are beyond the well-behaved discounted case, where the Bellman operator is a contraction mapping. For further discussion and analysis that address exceptional behavior, including the frameworks of semicontractive and noncontractive DP, we refer to the author’s abstract DP monograph [Ber22a]. 
The Blackmailer’s Dilemma 
This is a classical example involving a profit maximizing blackmailer. We formulate it as an SSP problem involving cost minimization, with a single state x = 1, in addition to the termination state t. We are in state 1 when the victim is compliant, and we are in state t when the victim refuses to yield to the blackmailer’s demand (a refusal is permanent, in the sense that once the blackmailer’s demand is refused, all subsequent demands are assumed to be refused, so t is a termination state). At state 1 we can choose a control u " (0, 1], which we regard as the demand made by the blackmailer. The problem is to find the blackmailer’s policy that maximizes his expected total gain. 
To formulate this problem as a minimization problem, we will use ((u) as the cost per stage. In particular, upon choosing u " (0, 1], we move to state t with probability u2, and stay in state 1 with probability 1 ( u2; see Fig. 3.9.1. The idea is to optimally balance the blackmailer’s
74 An Abstract View of Reinforcement Learning Chap. 3 
45!Line 
! 
1 
2 
µ !1 
J 0 
J 
!µ 
Interval I Interval II Interval III Interval IV 
0 Jµ = ! 
1 
µ 
Region of Instability Region of Stability TµJ = !µ+ (1! µ2)J 
Interval I Interval II Interval III Interval IV Ks K! K 
J TJ = minµ"(0,1] TµJ 
Figure 3.9.2. The Bellman operators and the Bellman equation for the blackmailer problem. 
desire for increased demands (large u) with keeping his victim compliant (small u). 
For notational simplicity, let us abbreviate J(1) and µ(1) with just the scalars J and µ, respectively. Then in terms of abstract DP we have X = {1}, U = (0, 1], and for every stationary policy µ, the corresponding Bellman operator Tµ, restricted to state 1 is given by 
TµJ = (µ+ (1( µ2)J ; (3.37) 
[at the state t, Jµ(t) = 0]. Clearly Tµ is linear, maps the real line ' to itself, and is a contraction with modulus 1 ( µ2. Its unique fixed point within ', Jµ, is the solution of 
Jµ = TµJµ = (µ+ (1( µ2)Jµ, 
which yields 
Jµ = ( 1 
µ ; 
see Fig. 3.9.2. Here all policies are stable and lead asymptotically to t with probability 1, and the infimum of Jµ over µ " (0, 1] is (%, implying also that J* = (%. However, there is no optimal policy. 
The Bellman operator T is given by 
TJ = min 0<u(1 
( 
( u+ (1 ( u2)J ) 
, 
which after some calculation can be shown to have the form 
TJ = 
/ 
(1 for ( 1 
2 * J , 
J + 1 
4J for J * ( 1 
2 .
Sec. 3.9 Exceptional Cases 75 
J!(1) = 0 
Cost of Truncated Rollout Policy µ̃ 1 
Cost of Truncated Rollout Policy µ̃ 1 
Optimal cost Cost of rollout policy ˜ 
TJ (TJ)(1) 
(1) = 0 J(1) ( 
45!Line 
Figure 3.9.3 Illustration of the Bellman equation for a shortest path problem in the exceptional case where there is a cycle of zero length. Restricted within the set of J with J(t) = 0, the Bellman operator has the form 
(TJ)(1) = min ( 
J(1), 1 ) 
. 
The set of solutions of Bellman’s equation, J(1) = (TJ)(1) is the interval (#$, 1] and contains J"(1) = 0 in its interior. 
The form of T is illustrated in Fig. 3.9.2. It can be seen from this figure that the Bellman equation J = TJ has no real-valued solution (the optimal cost J# = (% is a solution within the set of extended real numbers [(%,%]). Moreover the VI algorithm will converge to J* starting from any J " '. It can be verified also that the PI algorithm, starting from any policy µ0 " (0, 1], produces the ever improving sequence of policies {µk} with µk+1 = µk/2. Thus µk converges to 0, which is not a feasible policy. Also Jµk = (1/µk, and we have Jµk , (% = J*, so the PI algorithm gives in the limit the infinite optimal cost. For additional related examples and discussion relating to the blackmailer problem, see [Ber22a], Section 3.1. 
A Shortest Path Problem 
Another exceptional type of example is provided by shortest path problems that contain cycles of zero length; see the monograph [Ber22a], Section 3.1. In this case there are infinitely many solutions to Bellman’s equation, and the VI and PI algorithms, as well as the approximation in value space process exhibit unusual behavior. We demonstrate this with a shortest path problem involving a single state, denoted 1, in addition to the cost-free destination state t. 
In particular, let X = {t, 1}, and assume that at state 1 there are two options: we can stay at 1 at cost 0, or move to t at cost 1. Here
76 An Abstract View of Reinforcement Learning Chap. 3 
J*(t) = J*(1) = 0, and there are just two policies, which correspond to the two options at state 1 and are stable. The optimal policy starting at state 1 is to stay at 1. If we restrict attention to cost functions J with J(t) = 0, the Bellman operator is 
(TJ)(1) = min ( 
J(1), 1 ) 
, 
and Bellman’s equation, written as an equation in J(1), has the form 
J(1) = min ( 
J(1), 1 ) 
. 
The set of solutions of this equation is the interval ((%, 1] and it is infinite; see Fig. 3.9.3. The optimal value J*(1) = 0 lies in the interior of this set, and cannot be obtained by the VI algorithm, unless the algorithm is started at the optimal value. 
Let us consider approximation in value space with cost approximation J̃(1). Then it can be seen that if J̃(1) < 1, the one-step lookahead policy is to stay at state 1, which is optimal. If J̃(1) > 1, the one-step lookahead policy is to move from state 1 to state t, which is suboptimal. If J̃(1) = 1, either one of the two policies can be the one-step lookahead policy. 
Consider also the PI algorithm, starting from the suboptimal policy µ that moves from state 1 to state t. Then Jµ(t) = 0, Jµ(1) = 1, and it can be seen that µ satisfies the policy improvement equation 
µ(1) " argmin ( 
Jµ(1), 1 + Jµ(t) ) 
(the same is true for the optimal policy that stays at state 1). Thus the PI algorithm may stop with the suboptimal policy µ. 
Problems where exceptional behavior occurs arise often in Markov decision problems, once one departs from the most commonly discussed and best behaved paradigm of discounted cost with bounded cost per stage, where the mappings Tµ of all policies µ have favorable contraction properties. Moreover, problems arising in decision and control, such as those that have been addressed with MPC, often give rise to exceptional behavior. Further research and computational experimentation is expected to provide improved guidelines for the solution of such problems. 
What HappensWhen the Bellman Operator is Neither Concave nor Convex? - Markov Games 
We have discussed so far DP models where the Bellman operator has a concavity property. On the other hand there are interesting DP models where this is not so. An important case in point is discounted Markov games , a form of zero-sum games with a dynamic Markov chain structure. 
Let us consider two players that play repeated matrix games at each of an infinite number of stages, using mixed strategies. The game played
Sec. 3.9 Exceptional Cases 77 
at a given stage is defined by a state x that takes values in a finite set X , and changes from one stage to the next according to a Markov chain whose transition probabilities are influenced by the players’ choices. At each stage and state x " X , the minimizer selects a probability distribution u = (u1, . . . , un) over n possible choices i = 1, . . . , n, and the maximizer selects a probability distribution v = (v1, . . . , vm) over m possible choices j = 1, . . . ,m. If the minimizer chooses i and the maximizer chooses j, the payo! of the stage is aij(x) and depends on the state x. Thus the expected payo! of the stage is 
0 
i,j aij(x)uivj or u"A(x)v, where A(x) is the n&m 
matrix with components aij(x) (u and v are viewed as column vectors, and a prime denotes transposition). The two players choose u and v with knowledge of the state x, so they are viewed as using policies µ and ), where µ(x) and )(x) are the choices of the minimizer and the maximizer, respectively, at a state x. 
The state evolves according to transition probabilities qxy(i, j), where i and j are the moves selected by the minimizer and the maximizer, respectively (here y represents the next state and game to be played after moves i and j are chosen at the game represented by x). When the state is x, under u and v, the state transition probabilities are 
pxy(u, v) = n % 
i=1 
m % 
j=1 
uivjqxy(i, j) = u"Qxyv, 
where Qxy is the n & m matrix that has components qxy(i, j). Payo!s are discounted by ! " (0, 1), and the objectives of the minimizer and maximizer, are to minimize and to maximize the total discounted expected payo!, respectively. 
It was shown by Shapley [Sha53] that the problem can be formulated as a fixed point problem involving the mapping H given by 
H(x, u, v, J) = u"A(x)v + ! % 
y!X 
pxy(u, v)J(y) 
= u" 
1 
2A(x) + ! % 
y!X 
QxyJ(y) 
3 
4 v, 
(3.38) 
with the corresponding Bellman operator given by 
(TJ)(x) = min u!U 
max v!V 
H(x, u, v, J), for all x " X. (3.39) 
It can be verified that T is an unweighted sup-norm contraction, and its unique fixed point J* satisfies the Bellman equation J* = TJ*. 
Note that since the matrix defining the mapping H of Eq. (3.38), 
A(x) + ! % 
y!X 
QxyJ(y),
78 An Abstract View of Reinforcement Learning Chap. 3 
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
Figure 3.9.4 Schematic illustration of the PI algorithm/Newton’s method in the case of a Markov game involving a single state, in addition to a termination state t. We have J"(t) = 0 and (TJ)(t) = 0 for all J with J(t) = 0, so that the operator T can be graphically represented in just one dimension (denoted by J) that corresponds to the nontermination state. This makes it easy to visualize T 
and geometrically interpret why Newton’s method does not converge. Because the operator T may be neither convex nor concave for a Markov game, the algorithm may cycle between pairs (µ, #) and (µ̃, #̃), as shown in the figure. By contrast in a (single-player) finite-state Markov decision problem, (TJ)(x) is piecewise linear and concave, and the PI algorithm converges in a finite number of iterations. 
The figure illustrates an operator T of the form 
TJ = min ! 
max ( 
"11(J), "12(J) ) 
, max ( 
"21(J), "22(J) ) 
$ 
, 
where "ij(J), are linear functions of J , corresponding to the choices i = 1, 2 of the minimizer and j = 1, 2 of the maximizer. Thus TJ is the minimum of the convex functions 
max ( 
"11(J), "12(J) ) 
and max ( 
"21(J), "22(J) ) 
, 
as shown in the figure. Newton’s method linearizes TJ at the current iterate [i.e., replaces TJ with one of the four linear functions "ij(J), i = 1, 2, j = 1, 2 (the one attaining the min-max at the current iterate)] and solves the corresponding linear fixed point problem to obtain the next iterate. The figure illustrates a case where the PI algorithm/Newton’s method oscillates between two pairs of policies (µ, #) and (µ̃, #̃). 
is independent of u and v, we may view J*(x) as the value of a static
Sec. 3.10 Notes and Sources 79 
(nonsequential) matrix game that depends on x. In particular, from a fundamental saddle point theorem for matrix games, we have 
min u2U 
max v2V 
H(x, u, v, J⇤) = max v2V 
min u2U 
H(x, u, v, J*), for all x 2 X. 
(3.40) The paper by Shapley [Sha53] also showed that the strategies obtained by solving the static saddle point problem (3.40) correspond to a saddle point of the sequential game in the space of mixed strategies. Thus once we find J* as the fixed point of the mapping T [cf. Eq. (3.39)], we can obtain equilibrium policies for the minimizer and maximizer by solving the matrix game (3.40). Moreover, T can be defined via the operator Tµ,⌫ defined for a pair of minimizer-maximizer policies (µ, ⌫) by 
(Tµ,⌫J)(x) = H   x, µ(x), ⌫(x), J 
  , for all x 2 X, (3.41) 
In particular, T can be defined via a minimax operation applied to the operator Tµ,⌫ as follows: 
(TJ)(x) = min µ2M 
max ⌫2N 
(Tµ,⌫J)(x), for all x 2 X, 
whereM andN are the sets of policies of the minimizer and the maximizer, respectively. 
On the other hand the Bellman operator components (TJ)(x) may be neither convex nor concave. In particular, the maximization makes the function 
max v2V 
H(x, u, v, J) 
convex as a function of J for each fixed x and u 2 U , while the subsequent minimization over u 2 U tends to introduce concave “pieces” into (TJ)(x). It is possible to apply PI ideas and the corresponding Newton’s method to compute the fixed point of T , and in fact this has been proposed by Pollatschek and Avi-Itzhak [PoA69]. However, this algorithm need not converge to the optimal and may not yield J*, the fixed point of T (unless the starting point is su ciently close to J⇤, as has been recognized in the paper [PoA69]). The mechanism by which this phenomenon may occur is illustrated in Fig. 3.9.4. In fact a two-state example where the PI algo-rithm/Newton’s method does not converge to J* was given by van der Wal [Van78]. The preceding Markov chain discussion is part of a broader investigation of abstract minimax problems and Markov games, given in the author’s recent paper [Ber21c] (and replicated in the monograph [Ber22a], Ch. 5). In particular, this paper develops exact and approximate PI methods, which correct the exceptional behavior illustrated in Fig. 3.9.4. 
3.10 NOTES AND SOURCES 
The author’s abstract DP monograph [Ber22a] (originally published in 2013, with a second edition appearing in 2018, and a third edition appearing
80 An Abstract View of Reinforcement Learning Chap. 3 
in 2022) has provided the framework for the Newton step interpretations and visualizations that we have used to gain insight into approximation in value space, rollout, and policy iteration. The abstract framework aims at a unified development of the core theory and algorithms of total cost sequential decision problems, and addresses simultaneously stochastic, minimax, game, risk-sensitive, and other DP problems, through the use of the abstract DP operator (or Bellman operator as it is often called in RL). The idea here is to gain insight through abstraction. In particular, the structure of a DP model is encoded in its abstract Bellman operator, which serves as the “mathematical signature” of the model. Characteristics of this operator (such as monotonicity and contraction) largely determine the analytical results and computational algorithms that can be applied to that model. 
Abstraction also captures the generality of the DP methodology. In particular, our conceptual framework based on Newton’s method is applicable to problems with general state and control spaces, ranging from the continuous spaces control problems, traditionally the focus of MPC, to Markov decision problems, traditionally the focus of operations research as well as RL, and to discrete optimization problems, traditionally the focus of integer programming and combinatorial optimization. A key mathematical fact in this respect is that while the state and control spaces may be continuous or discrete, the Bellman operators and equations are always defined over continuous function spaces, and are thus amenable to solution through the use of continuous spaces algorithms, including Newton’s method.
4 The Linear Quadratic Case -
Illustrations 
Contents 
4.1. Optimal Solution . . . . . . . . . . . . . . . . . . p. 82 4.2. Cost Functions of Stable Linear Policies . . . . . . . . p. 83 4.3. Value Iteration . . . . . . . . . . . . . . . . . . . p. 86 4.4. One-Step and Multistep Lookahead - Newton Step . . . . . 
Interpretations . . . . . . . . . . . . . . . . . . . p. 86 4.5. Sensitivity Issues . . . . . . . . . . . . . . . . . . p. 91 4.6. Rollout and Policy Iteration . . . . . . . . . . . . . p. 94 4.7. Truncated Rollout - Length of Lookahead Issues . . . . p. 97 4.8. Exceptional Behavior in Linear Quadratic Problems . . . p. 99 4.9. Notes and Sources . . . . . . . . . . . . . . . . p. 100 
81
82 The Linear Quadratic Case - Illustrations Chap. 4 
In this chapter, we will use linear quadratic problems as a vehicle for graphical illustrations and insight into the suboptimal control ideas developed so far. This is possible because linear quadratic problems admit closed form solutions. Our discussion applies to multidimensional linear quadratic problems (cf. Example 2.1.1), but we will focus on the one-dimensional case to demonstrate graphically our approximation in value space ideas and their connection to Newton’s method. 
In particular, throughout this chapter we will consider the system 
xk+1 = axk + buk, 
and the cost function ! 
k=0 
(qx2 k + ru2 
k), 
where a, b, q, r are scalars with b != 0, q > 0, r > 0. It can be verified computationally (and also with some analysis) that the insights obtained from the one-dimensional case are generally correct for the multidimensional case of the linear quadratic problem, where the state cost weighting matrix Q is positive definite. In Section 4.8 we will obtain related insights about what happens in the exceptional case where q = 0. 
4.1 OPTIMAL SOLUTION 
The optimal solution was given for the multidimensional case of the linear quadratic problem in Example 2.1.1. For the one-dimensional case considered here, the optimal cost function has the form 
J*(x) = K"x2, (4.1) 
where the scalar K" solves a fixed point equation of the form 
K = F (K), (4.2) 
with F defined by 
F (K) = a2rK 
r + b2K + q. (4.3) 
This is the Riccati equation, which is equivalent to the Bellman equation J = TJ , restricted to the subspace of quadratic functions of the form J(x) = Kx2; see Fig. 4.1.1. Essentially, by replacing the Bellman operator T with the Riccati equation operator F of Eq. (4.3), we can analyze the action of T on this subspace. This allows a di!erent type of visualization than the one we have been using so far. 
The scalar K" that corresponds to the optimal cost function J* [cf. Eq. (4.1)] is the unique solution of the Riccati equation (4.2) within the
Sec. 4.2 Cost Functions of Stable Linear Policies 83 
0 
K K 
K K 
45!Line 
q q F 
q q F (K) = a 2 rK 
r+b2K + q 
a 2 r 
b2 + q q F 
State 1 State 2 K!K̄ 
Cost of µ̃ ! 
r 
b2 
Figure 4.1.1 Graphical construction of the solutions of the Riccati equation (4.2)-(4.3) for the linear quadratic problem. The optimal cost function is J!(x) = K!x2, where the scalar K! solves the fixed point equation K = F (K), with F being the function given by 
F (K) = a2rK 
r + b2K + q. 
Because F is concave and monotonically increasing in the interval (!r/b2,") and “flattens out” as K # ", as shown in the figure, the quadratic Riccati equation K = F (K) has one positive solution K! and one negative solution, denoted K̄. 
nonnegative real line. This equation has another solution, denoted by K̄ in Fig. 4.1.1, which lies within the negative real line and is of no interest. The optimal policy is a linear function of the state and has the form 
µ!(x) = L!x, 
where L! is the scalar given by 
L! = ! abK! 
r + b2K! . (4.4) 
4.2 COST FUNCTIONS OF STABLE LINEAR POLICIES 
Suppose that we are given a linear policy of the form 
µ(x) = Lx, 
where L is a scalar. The corresponding closed loop system is 
xk+1 = (a+ bL)xk = (a+ bL)k+1x0,
84 The Linear Quadratic Case - Illustrations Chap. 4 
0 
K K 
K Kq q F 
KL 
FL(K) = (a+ bL)2K + q + rL2 
q q F (K) = a 2 rK 
r+b2K + q 
a 2 r 
b2 + q q F 
State 1 State 2 K! 
Figure 4.1.2 Illustration of the construction of the cost function of a linear policy µ(x) = Lx, which is stable, i.e., |a+ bL| < 1. The cost function Jµ(x) has the form Jµ(x) = KLx 
2, where KL is the unique solution of the linear equation K = FL(K), where 
FL(K) = (a + bL)2K + q + rL 2 , 
is the Riccati equation operator corresponding to L (i.e., the analog of Tµ). If µ is unstable, we have Jµ(x) = ! for all x "= 0. 
and the cost Jµ(x0) is calculated as 
! 
k=0 
" 
q(a+ bL)2kx2 0 + rL2(a+ bL)2kx2 
0 
# 
= lim N#! 
N$1 ! 
k=0 
(q + rL2)(a+ bL)2kx2 0 . 
Assuming |a+ bL| < 1, i.e., that the closed loop system is stable, the above summation yields 
Jµ(x) = KLx 2, 
for every initial state x, where 
KL = q + rL2 
1" (a+ bL)2 . (4.5) 
If on the other hand, |a+ bL| # 1, i.e., the closed loop system is unstable, the summation yields Jµ(x0) = $ for all x0 != 0. 
It can be seen with a straightforward calculation thatKL is the unique solution of the linear equation 
K = FL(K), (4.6) 
where FL(K) = (a+ bL)2K + q + rL2; (4.7)
Sec. 4.2 Cost Functions of Stable Linear Policies 85 
see Fig. 4.1.2. Again, by replacing the Bellman operator Tµ of the stable policy µ(x) = Lx with the Riccati equation operator FL, we can analyze the action of Tµ on the subspace of quadratic functions J(x) = Kx2. Note that when |a + bL| > 1, so that µ is unstable, we have Jµ(x) = $ for all x != 0, and the graph of FL intersects the 45-degree line at a negative K. Then the equation K = FL(K) has the negative solution 
q + rL2 
1" (a+ bL)2 , 
but this solution is unrelated to the cost function Jµ(·), which has infinite value for all x != 0. 
We summarize the Riccati equation formulas and the relation between linear policies of the form µ(x) = Lx and their quadratic cost functions in the following table. 
Riccati Equation Formulas for One-Dimensional Problems 
Riccati equation for minimization [cf. Eqs. (4.2) and (4.3)] 
K = F (K), F (K) = a2rK 
r + b2K + q. 
Riccati equation for a stable linear policy µ(x) = Lx [cf. Eqs. (4.6) and (4.7)] 
K = FL(K), FL(K) = (a+ bL)2K + q + rL2. 
Gain LK of lookahead linear policy associated with K [cf. Eq. (4.4)] 
LK = " abK 
r + b2K . 
Cost coe!cient KL of linear policy µ(x) = Lx [cf. Eq. (4.5)] 
KL = q + rL2 
1" (a+ bL)2 . 
The one-dimensional problem of this chapter is well suited for geometric interpretations such as the ones we gave earlier in the preceding chapter, because approximation in value space, and the VI, rollout, and PI algorithms, involve quadratic cost functions J(x) = Kx2, which can be represented by one-dimensional graphs as functions of just the number K. In particular, Bellman’s equation can be replaced by the Riccati
86 The Linear Quadratic Case - Illustrations Chap. 4 
equation (4.3). Similarly, the figures in Chapter 3 for approximation in value space with one-step and multistep lookahead, the region of stability, rollout, and PI can be represented by one-dimensional graphs. We will next present these graphs and obtain corresponding geometrical insights. Note that our discussion applies qualitatively to multidimensional linear quadratic problems, and can be verified to a great extent by analysis, but an e!ective geometrical illustration is only possible when the system is one-dimensional. 
4.3 VALUE ITERATION 
The VI algorithm for the one-dimensional linear quadratic problem is illustrated in Fig. 4.3.1. It has the form 
Kk+1 = F (Kk); 
cf. Example 2.1.1. As can be seen from the figure, the algorithm converges to K" starting from anywhere in the interval (K̄,$), where K̄ is the negative solution. In particular, the algorithm converges to K" starting from any nonnegative value of K. 
It is interesting to note that, starting from values K0 with K0 % K̄, 
the algorithm does not converge to the optimal K". From Fig. 4.3.1, it can be seen that if 
" r 
b2 < K0 % K̄, 
it converges to the negative solution K̄. The threshold "r/b2 is the asymptotic value to the left of which F (K) drops to "$. When 
K0 % " r 
b2 , 
for the corresponding function J0(x) = K0x2 we have (TJ0)(x) = "$ for all x, and the algorithm is not well defined. The literature on linear quadratic problems universally assumes that the iterative solution of the Riccati equation is started with nonnegative K0, since to select a negative starting K0 makes little sense. Note, however, that the nice behavior of VI just described depends on the positivity of the state cost coe"cient q. In Section 4.8, we will discuss the exceptional case where q = 0. 
4.4 ONE-STEP AND MULTISTEP LOOKAHEAD - NEWTON STEP INTERPRETATIONS 
In this section, we consider approximation in value space with a quadratic terminal cost function J̃(x) = K̃x2; cf. Fig. 4.4.1. We will express the cost function Jµ̃ of the corresponding one-step lookahead policy µ̃ in terms of
Sec. 4.4 One-Step and Multistep Lookahead - Newton Step 87 
0 
K K 
K K 
Kk Kk+1 
45!Line 
q q F 
Cost of µ̃ ! 
r 
b2 
State 1 State 2 K!K̄ 
q q F (K) = a 2 rK 
r+b2K + q 
a 2 r 
b2 + q q F 
Figure 4.3.1 Graphical illustration of value iteration for the linear quadratic problem. It has the form Kk+1 = F (Kk) where 
F (K) = a2rK 
r + b2K + q. 
It is essentially equivalent to the VI algorithm with a quadratic starting function 
J0(x) = K0x 2 . 
The algorithm converges to K! starting from anywhere in the interval (K̄,!), where K̄ is the negative solution, as shown in the figure. Starting from values K0 
with # 
r 
b2 < K0 $ K̄, 
the algorithm converges to the negative solution K̄. When 
K0 $ # r 
b2 , 
we have (TJ0)(x) = #! for all x, and the algorithm is undefined. 
K̃ (assuming that K̃ belongs to the region of stability), and we will prove that the transformation from J̃ to Jµ̃ is equivalent to a Newton step for solving the Riccati equation starting from K̃. 
In particular, for a linear quadratic problem, the one-step lookahead policy is given by 
µ̃(x) & argmin u 
$ 
qx2 + ru2 + K̃(ax+ bu)2 % 
, 
which after a straightforward calculation, yields 
µ̃(x) = L̃x,
88 The Linear Quadratic Case - Illustrations Chap. 4 
0 
K K 
K K 
q q F 
q K̃ 
F L̃ (K) 
K K L̃ 
L̃ = ! 
abK̃ 
r + b2K̃ 
State 1 State 2 ! 
also Newton Step 
F (K) 
Figure 4.4.1 Illustration of approximation in value space with one-step lookahead for the linear quadratic problem. Given a terminal cost approximation J̃ = K̃x2, we compute the corresponding linear policy µ̃(x) = L̃x, where 
L̃ = # abK̃ 
r + b2K̃ , 
and the corresponding cost function K L̃ x2, using the Newton step shown. 
with the linear policy coe"cient given by 
L̃ = " abK̃ 
r + b2K̃ . 
Note, however, that this policy will not be stable if |a+ bL̃| # 1, or equivalently if 
& 
& 
& 
& 
& 
a" ab2K̃ 
r + b2K̃ 
& 
& 
& 
& 
& 
# 1. 
We may also construct the linearization of the function F at K̃, and solve the corresponding linearized problem with a Newton step, as illustrated in Fig. 4.4.1. The case of !-step lookahead minimization can be similarly interpreted. Instead of linearizing F at K̃, we linearize at K!$1 = F !$1(K̃), i.e., at the result of ! " 1 successive applications of F starting with K̃. Figure 4.4.2 depicts the case ! = 2. 
An important consequence of the Newton step interpretation is a classical quadratic convergence rate result: there exists an open interval containing K" and a constant c > 0 such that for all K̃ within the open interval we have 
|KL̃ "K"| % c |K̃ "K"|2, (4.8)
Sec. 4.4 One-Step and Multistep Lookahead - Newton Step 89 
K K 
F L̃ (K) 
K K L̃ 
K1 
1 L̃ = ! 
abK1 
r + b2K1 
State 1 State 2 ! 
also Newton Step 
F (K) 
q K̃ 
Figure 4.4.2 Illustration of approximation in value space with two-step lookahead for the linear quadratic problem. Starting with a terminal cost approximation J̃ = K̃x2, we obtain K1 using a single value iteration. We then compute the corresponding linear policy µ̃(x) = L̃x, where 
L̃ = # abK1 
r + b2K1 
and the corresponding cost function K L̃ x2, using the Newton step shown. 
where L̃ corresponds to the policy obtained by approximation in value space with one-step lookahead and terminal cost approximation J̃(x) = K̃x2, so that 
L̃ = " abK̃ 
r + b2K̃ , (4.9) 
and 
KL̃ = q + rL̃2 
1" (a+ bL̃)2 . (4.10) 
Figure 4.4.2 also suggests another result that stems from the concavity property of the Riccati equation, namely that if K̂ is a scalar that lies strictly within the region of stability, i.e., 
& 
& 
& 
& 
& 
a" ab2K̂ 
r + b2K̂ 
& 
& 
& 
& 
& 
< 1, 
then there exists a constant c > 0 such that all K̃ # K̂ satisfy Eq. (4.8). This result will not be proved here, but follows from the line of convergence analysis of Newton’s method, which is given in the Appendix. 
We will next show the quadratic convergence rate estimate (4.8) by verifying that KL̃ is the result of a Newton step for solving the Riccati 
equation K = F (K) starting from K̃.
90 The Linear Quadratic Case - Illustrations Chap. 4 
Cost Function of the Lookahead Policy - A View from Newton’s Method 
We will apply Newton’s method to the solution of the Riccati Eq. (4.3), which we write in the form 
H(K) = 0, 
where 
H(K) = K " a2rK 
r + b2K " q. (4.11) 
The classical form of Newton’s method takes the form 
Kk+1 = Kk " 
' 
"H(Kk) 
"K 
($1 
H(Kk), (4.12) 
where "H(K k ) 
"K is the derivative of H , evaluated at the current iterate Kk. 
We will show analytically that the operation that generates KL starting from K is a Newton iteration of the form (4.12) (an alternative is to argue graphically, as in Fig. 3.2.1). In particular, we will show (simplifying notation by skipping tilde) that for all K that lead to a stable one-step lookahead policy, we have 
KL = K " 
' 
"H(K) 
"K 
($1 
H(K), (4.13) 
where we denote by 
KL = q + rL2 
1" (a+ bL)2 (4.14) 
the quadratic cost coe"cient of the one-step lookahead linear policy µ(x) = Lx corresponding to the cost function approximation J(x) = Kx2: 
L = " abK 
r + b2K (4.15) 
[cf. Eqs. (4.9) and (4.10)]. Our approach for showing the Newton step formula (4.13) is to express 
each term in this formula in terms of L, and then show that the formula holds as an identity for all L. To this end, we first note from Eq. (4.15) that K can be expressed in terms of L as 
K = " rL 
b(a+ bL) . (4.16) 
Furthermore, by using Eqs. (4.15) and (4.16), H(K) as given in Eq. (4.11) can be expressed in terms of L as follows: 
H(K) = " rL 
b(a+ bL) + 
arL 
b " q. (4.17)
Sec. 4.5 Sensitivity Issues 91 
Moreover, by di!erentiating the function H of Eq. (4.11), we obtain after a straightforward calculation 
"H(K) 
"K = 1" 
a2r2 
(r + b2K)2 = 1" (a+ bL)2, (4.18) 
where the second equation follows from Eq. (4.15). Having expressed all the terms in the Newton step formula (4.13) in terms of L through Eqs. (4.14), (4.16), (4.17), and (4.18), we can write this formula in terms of L only as 
q + rL2 
1" (a+ bL)2 = " 
rL 
b(a+ bL) " 
1 
1" (a+ bL)2 
' 
" rL 
b(a+ bL) + 
arL 
b " q 
( 
, 
or equivalently as 
q + rL2 = " rL " 
1" (a+ bL)2 # 
b(a+ bL) + 
rL 
b(a+ bL) " 
arL 
b + q. 
A straightforward calculation now shows that this equation holds as an identity for all L. 
We have thus shown that KL is related to K by the Newton step formula (4.13) for all K. Consequently, from classical calculus results on Newton’s method, the quadratic convergence rate estimate (4.8) follows. 
In the case of !-step lookahead this result takes a stronger form, whereby the analog of the quadratic convergence rate estimate (4.8) has the form 
|KL̃ "K"| % c & 
&F !$1(K̃)"K" & 
& 
2 , 
where F !$1(K̃) is the result of the (!" 1)-fold application of the mapping F to K̃. Thus a stronger bound for |KL̃ "K"| is obtained. 
4.5 SENSITIVITY ISSUES 
An interesting consequence of the Newton step relation (4.13) between K 
and KL relates to sensitivity to changes in K. In particular, we will show that asymptotically, near K", small changes in K induce much smaller changes in KL. Mathematically, given K1 and K2 that lie within the region of stability, so they lead to stable corresponding one-step lookahead policies µ1(x) = L1x and µ2(x) = L2x, we have 
|KL1 "KL2 
| 
|K1 "K2| ' 0 as |K1 "K2| ' 0 and H(K2) ' 0, (4.19) 
as we will show next.
92 The Linear Quadratic Case - Illustrations Chap. 4 
This result also holds for multidimensional linear quadratic problems, and also holds in various forms, under appropriate conditions, for more general problems. The practical significance of this result (and its extension to the case of a general di!erentiable Bellman operator T ) is that near K" (or J*, in the general case), small o!-line training changes (i.e., small changes in K, or J̃ , respectively) are rendered by the Newton step relatively insignificant as far as their e!ect on-line play performance is concerned (i.e., changes in KL, or Jµ̃, respectively). Small o!-line training changes may result from applying alternative cost function approximation methods, which rely on similarly powerful feature-based or neural network-based architectures (e.g., di!erent forms of temporal di!erence methods, aggregation methods, approximate linear programming, etc). 
To see why the sensitivity Eq. (4.19) holds, we rewrite the Newton iteration formula 
KL1 = K1 " 
' 
"H(K1) 
"K 
($1 
H(K1), 
[cf. Eq. (4.13)] by using the first order Taylor approximations† 
' 
"H(K1) 
"K 
($1 
= 
' 
"H(K2) 
"K 
($1 
+O " 
|K1 "K2| # 
, 
H(K1) = H(K2) + "H(K2) 
"K (K1 "K2) + o 
" 
|K1 "K2| # 
. 
We obtain 
KL1 = K1" 
) 
' 
"H(K2) 
"K 
($1 
+O " 
|K1 "K2| # 
* 
' 
H(K2) + "H(K2) 
"K (K1 "K2) + o 
" 
|K1 "K2| # 
( 
, 
which yields 
KL1 = K1 " 
' 
"H(K2) 
"K 
($1 
H(K2)" (K1 "K2) +O " 
|K1 "K2| # 
H(K2) 
+ o " 
|K1 "K2| # 
. 
† We are using here the standard calculus notation whereby O " 
|K1 ! K2| # 
denotes a function of (K1,K2) such that O " 
|K1!K2| # 
" 0 as |K1!K2| " 0, and 
o " 
|K1!K2| # 
denotes a function of (K1,K2) such that o " 
|K1!K2| # 
/|K1!K2| " 0 
as |K1 !K2| " 0.
Sec. 4.5 Sensitivity Issues 93 
The preceding equation, together with the Newton iteration formula [cf. Eq. (4.13)] 
KL2 = K2 " 
' 
"H(K2) 
"K 
($1 
H(K2), 
yields 
KL1 = KL2 
+O " 
|K1 "K2| # 
H(K2) + o " 
|K1 "K2| # 
, (4.20) 
or KL1 
"KL2 
|K1 "K2| = 
O " 
|K1 "K2| # 
|K1 "K2| H(K2) + 
o " 
|K1 "K2| # 
|K1 "K2| . (4.21) 
The first term of the right hand side above tends to 0 as H(K2) ' 0, while the second term tends to 0 as |K1 " K2| ' 0. This proves the desired sensitivity Eq. (4.19). Also by tracing through the preceding calculations, it can be seen that the term O 
" 
|K1"K2| # 
multiplying H(K2) in Eq. (4.20) is equal to 
' 
"H(K1) 
"K 
($1 
" 
' 
"H(K2) 
"K 
($1 
, (4.22) 
and is close to 0 if H(K) is nearly linear. Figure 4.5.1 illustrates the sensitivity estimate (4.21). 
Note that from Eq. (4.21), the ratio (KL1 "KL2 
)/|K1"K2| depends on how close K2 is to K", i.e., on the size of H(K2). In particular, if K2 = K", we recover the superlinear convergence rate 
|KL1 "K"| 
|K1 "K"| = 
o " 
|K1 "K"| # 
|K1 "K"| . 
On the other hand, if H(K2) is far from 0 and H has large second derivatives near K1 and K2 [so that the di!erence of inverse derivatives (4.22) is large], the ratio (KL1 
"KL2 )/|K1"K2| can be quite large even if |K1"K2| 
is rather small. This sometimes tends to happen when K1 and K2 are close to the boundary of the region of stability, in which case it is important to bring the e!ective start of the Newton step closer to K", possibly by using multistep lookahead and/or truncated rollout with a stable policy. 
The preceding derivation can be extended to hold for a general case of a mapping T as long as T is di!erentiable. If T is nondi!erentiable at J* 
the derivation breaks down and a sensitivity result such as the one of Eq. (4.19) may not hold in exceptional cases. Note, however, that in the case of a discounted problem with finite numbers of states and controls, where (TJ)(x) is a piecewise linear function of J for every x, a stronger result can be proved: there is a sphere centered at J* such that if J̃ lies within this sphere, the one-step lookahead policy corresponding to J̃ is optimal (see the book [Ber20a], Prop. 5.5.2).
94 The Linear Quadratic Case - Illustrations Chap. 4 
-1 -0.8 -0.6 -0.4 -0.2 0 0.2 0.4 0.6 0.8 0 
0.05 
0.1 
0.15 
0.2 
0.25 
Figure 4.5.1 Illustration of the sensitivity estimate (4.21) for the case a = 1, b = 2, q = 1, r = 0.5. The di!erence K1 #K2 is denoted by !. The figure shows the expected value of |KL1 
#KL2 | as the distance K1 #K! varies, and as K2 is 
selected randomly according to a uniform probability distribution in the interval [K1 # !, K1 + !], for three di!erent values of ! (0.15, 0.2, and 0.3). Note that for K1 > K!, the change |KL1 
# KL2 | is much smaller than for K1 < K!, because 
the di!erence of inverse derivatives (4.22) is small for K1 > K!, even for large values of ! (H is nearly linear). 
4.6 ROLLOUT AND POLICY ITERATION 
The rollout algorithm with a stable base policy µ is illustrated in Fig. 4.6.1. The PI algorithm is simply the repeated application of rollout. Let us derive the algorithm starting from a linear base policy of the form 
µ0(x) = L0x, 
where L0 is a scalar. We require that L0 is such that the closed loop system 
xk+1 = (a+ bL0)xk, (4.23) 
is stable, i.e., |a+ bL0| < 1. This is necessary for the policy µ0 to keep the state bounded and the corresponding costs Jµ0(x) finite. We will see that the PI algorithm generates a sequence of linear stable policies. 
To describe the policy evaluation and policy improvement phases for the starting policy µ0, we first calculate Jµ0 by noting that it involves the uncontrolled closed loop system (4.23) and a quadratic cost function. Similar to our earlier calculations, it has the form 
Jµ0(x) = K0x2, (4.24)
Sec. 4.6 Rollout and Policy Iteration 95 
Value iterations Policy evaluations 
Policy Improvement with Base Policy Policy Improvement with Base Policy µ 
Policy evaluations for µ and µ̃ 
Optimal cost Cost of rollout policy µ̃Optimal cost Cost of rollout policy µ̃ Cost of base policy µ 
45!Line 
K K 
Optimal cost Cost of rollout policy ˜ State 1 State 2 K! 
also Newton Step 
Figure 4.6.1 Illustration of rollout and policy iteration for the linear quadratic problem. 
where 
K0 = q + rL2 
0 
1" (a+ bL0)2 . (4.25) 
Thus, the policy evaluation phase of PI for the starting linear policy µ0(x) = L0x yields Jµ0 in the form (4.24)-(4.25). The policy improvement phase involves the quadratic minimization 
µ1(x) & argmin u 
$ 
qx2 + ru2 +K0(ax+ bu)2 % 
, 
and after a straightforward calculation yields µ1 as the linear policy µ1(x) = L1x, where 
L1 = " abK0 
r + b2K0 
. 
It can also be verified that µ1 is a stable policy. An intuitive way to get a sense of this is via the cost improvement property of PI: we have Jµ1(x) % Jµ0(x) for all x, so Jµ1(x) must be finite, which implies stability of µ1. 
The preceding calculation can be continued, so the PI algorithm yields the sequence of stable linear policies 
µk(x) = Lkx, k = 0, 1, . . . , 
where Lk+1 is generated by the iteration 
Lk+1 = " abKk 
r + b2Kk ,
96 The Linear Quadratic Case - Illustrations Chap. 4 
Optimal cost Cost of rollout policy ˜ 
Cost of Truncated Rollout Policy ˜ Cost of Truncated Rollout Policy µ̃ 
K Kq K̃ 
K K 
State 1 State 2 K! 
also Newton Step 
FL(K) 
Region of Stability KL 
Cost Function Approximation Position Ev luator C s of Base Policy µ(x) = Lx 
Figure 4.6.2 Illustration of truncated rollout with a stable base policy µ(x) = Lx and terminal cost approximation K̃ for the linear quadratic problem. In this figure the number of rollout steps is m = 4, and we use one-step lookahead minimization. 
with Kk given by 
Kk = q + rL2 
k 
1! (a+ bLk)2 , 
[cf. Eq. (4.25)]. The corresponding cost function sequence has the form Jµk (x) = 
Kkx2. Part of the classical linear quadratic theory is that Jµk converges to the optimal cost function J*, while the generated sequence of linear policies {µk}, where µk(x) = Lkx, converges to the optimal policy. The convergence rate of the sequence {Kk} is quadratic, as shown earlier, i.e., there exists a constant c such that 
|Kk+1 !K!| " c |Kk !K!|2, 
for all k, assuming that the initial policy is linear and stable. This result was proved by Kleinman [Kle68] for the continuous time version of the linear quadratic problem, and it was extended later to more general problems; see the references given in Section 3.3 and the book [Ber20a], Chapter 1. For a recent proof of the quadratic convergence for linear discrete-time quadratic problems, see Lopez, Alsalti, and Muller [LAM21].
Sec. 4.7 Truncated Rollout - Length of Lookahead Issues 97 
4.7 TRUNCATED ROLLOUT - LENGTH OF LOOKAHEAD ISSUES 
Truncated rollout with a stable linear base policy µ(x) = Lx and terminal cost approximation J̃(x) = K̃x2 is illustrated in Fig. 4.6.2. The rollout policy µ̃ is obtained from the equation 
Tµ̃T !$1Tm µ J̃ = T !Tm 
µ J̃ , 
where ! # 1 is the length of the lookahead minimization and m # 0 is the length of the rollout lookahead, with m = 0 corresponding to no lookahead by rollout (in Fig. 4.6.2, we have ! = 1 and m = 4). 
We mentioned some interesting performance issues in our discussion of truncated rollout in Section 3.4, and we will now revisit these issues within the context of our linear quadratic problem. In particular we noted that: 
(a) Lookahead by rollout with a stable policy has a beneficial e!ect on the stability properties of the lookahead policy. 
(b) Lookahead by rollout may be an economic substitute for lookahead by minimization, in the sense that it may achieve a similar performance for the truncated rollout policy at significantly reduced computational cost. 
These statements are di"cult to establish analytically in some generality. However, they can be intuitively understood in the context with our onedimensional linear quadratic problem, using geometrical constructions like the one of Fig. 4.6.2. 
In particular, let us consider our one-dimensional linear quadratic problem, the corresponding value K" (the optimal cost coe"cient), and the value Ks, which demarcates the region of stability, i.e., one-step lookahead yields a stable policy if and only if K̃ > Ks. Consider also two parameters of the truncated rollout method: Kµ (the cost coe"cient of the base policy), and K̃ (the terminal cost approximation coe"cient). 
We have Ks % K" % Kµ, so the three parameters Ks,K",Kµ divide the real line in the four intervals I through IV, depicted in Fig. 4.7.1. Then by examining Fig. 4.6.2, we see that the behavior of truncated rollout depends on the interval in which the terminal cost coe"cient K̃ lies. In particular: 
(a) For K̃ in interval I : Long total (!+m)-step lookahead is needed to get the starting point of the Newton step within the region of stability. Best and computationally economical results are obtained by taking ! = 1 and m large enough to bring the starting point of the Newton step within the region of stability, and hopefully close to K". 
(b) For K̃ in interval II : ! = 1 and m # 0 are su"cient for stability. Best results are obtained when ! = 1 and m is the (generally unknown) value that brings the starting point of the Newton step close to K".
98 The Linear Quadratic Case - Illustrations Chap. 4 
Interval I Interval II Interval III Interval IVInterval I Interval II Interval IVInterval I Interval II Interval III Interval IVInterval l I Interval III Interval IV 
µ K 
Interval I Interval II Interval III Interval IV Ks s K! ! Kµ 
Region of InstabilityRegion of Instability Region of Stability 
Figure 4.7.1 Illustration of the behavior of truncated rollout for the linear quadratic problem. We consider the four intervals I, II, III, and IV, defined by the boundary of the region of stability Ks, the optimal cost coe"cient K!, and the cost coe"cient Kµ of the base policy µ. Using rollout with base policy µ, number of rollout steps m > 0, and a terminal cost coe"cient K̃ in intervals I, II, and IV improves the stability guarantee and/or the performance of the lookahead policy µ̃ over the case of no rollout, i.e., m = 0. In the case where K̃ lies in interval III, using m > 0 rather m = 0 deteriorates somewhat the performance of the lookahead policy µ̃, but still maintains the cost improvement property Kµ̃ $ Kµ. 
(c) For K̃ in interval III : ! = 1 and m # 0 are su"cient for stability. Best results are obtained when ! = 1 and m = 0 (since the rollout lookahead is counterproductive and takes the starting point of the Newton step away from K" and towards Kµ). Still, however, even with m > 0, we have the cost improvement property Kµ̃ % Kµ. 
(d) For K̃ in interval IV : ! = 1 and m # 0 are su"cient for stability. Best results are obtained for values of m and !, which depend on how far K̃ is from Kµ. Here, values that likely work well are the ones for which m is fairly large, and ! is close to 1 (large enough m 
will bring the starting point of the Newton step close to Kµ; ! = 1 corresponds to the Newton step, ! > 1 improves the starting point of the Newton step by value iteration, but is likely not worth the extra computational cost). 
Of course, a practical di"culty here is that we don’t know the interval in which K̃ lies. However, it is clear that by using rollout with m # 1 works well in most cases as an economical substitute for long lookahead minimization. In particular, when K̃ lies in intervals I, II, and IV, using m > 0 provides a stronger stability guarantee and improved performance through a better starting point for the Newton step. Even in the case where K̃ lies in interval III, using m > 0 is not very damaging: we still obtain performance that is no worse than the base policy, i.e., Kµ̃ % Kµ. An interesting research question is to investigate analytically as well as computationally, the multidimensional analogs of the intervals I-IV (which will now become subsets of the set of symmetric matrices). While it seems that the preceding discussion should generalize broadly, an investigation of the multidimensional case promises to be both challenging and illuminating. It may also reveal exceptional behaviors, particularly when extensions to problems more general than linear quadratic are considered.
Sec. 4.8 Exceptional Behavior in Linear Quadratic Problems 99 
K K 
K K 
F (K) = a2rK 
r + b2K 
Kk Kk+1 
a 2 r 
b2 
K! = 0 K̂ 
Figure 4.8.1 Illustration of the Bellman equation and the VI algorithm Kk+1 = F (Kk) for the linear quadratic problem in the exceptional case where q = 0. 
4.8 EXCEPTIONAL BEHAVIOR IN LINEAR QUADRATIC PROBLEMS 
It turns out that exceptional behavior can occur even for one-dimensional linear quadratic problems, when the positive definiteness assumption on the matrix Q is violated. In particular, let us consider the system 
xk+1 = axk + buk, (4.26) 
and the cost function ! 
k=0 
ru2 k, (4.27) 
where a, b, r are scalars with |a| > 1, b != 0, r > 0. In this case there is no penalty for the state being nonzero (i.e., q = 0), while the system is unstable when left uncontrolled. 
Here, since the cost per stage does not depend on the state, it is optimal to apply control u = 0 at any state x, i.e., µ"(x) ( 0, and the optimal cost function is J*(x) ( 0. The Riccati equation is given by 
K = F (K), 
where F defined by 
F (K) = a2rK 
r + b2K . 
As shown in Fig. 4.8.1, it has two nonnegative solutions: 
K" = 0 and K̂ = r(a2 " 1) 
b2 .
100 The Linear Quadratic Case - Illustrations Chap. 4 
The solution K" corresponds to the optimal cost function. It turns out that the solution K̂ is also interesting: it can be shown to be the optimal cost function within the subclass of linear policies that are stable. A proof of this is given in the author’s paper [Ber17c] and abstract DP monograph [Ber22a], Section 3.1. 
Consider also the VI algorithm 
Kk+1 = F (Kk), 
starting from some K0 > 0. As shown from Fig. 4.8.1, it generates a positive scalar sequence that converges to K̂. If the VI algorithm is started at the optimal K" = 0, it stays at K". It can also be verified that the PI algorithm generates a sequence of linear stable policies starting from a linear stable policy. The sequence converges to the optimal stable policy that corresponds to K̂. 
In summary, the PI algorithm starting from a linear stable policy yields Ĵ , the optimal cost function over the linear stable policies, but not the optimal cost function J*. At the same time, the PI algorithm yields a a policy that is optimal over the linear stable policies, but not the optimal policy µ"(x) ( 0. 
4.9 NOTES AND SOURCES 
Linear quadratic problems are central in control theory, and have been the subject of extensive research. There are detailed accounts in most control theory textbooks, including Vol. I of the author’s DP book [Ber17a]. 
The exceptional linear quadratic example of Section 4.8 provides an instance of a DP problem that exhibits a so-called “semicontractive behavior.” By this we mean that some policies are “well-behaved” (stabilize the system in this case, or have Bellman operators that are contractive in other cases), while some other policies are not, and the VI algorithm tends to be attracted to the optimal cost function over the well-behaved policies only. Semicontractive models and their analysis are a major focal point of the abstract DP monograph [Ber22a], Chapters 3 and 4. They arise commonly in the context of stochastic shortest path problems, where some policies (called proper) are “well-behaved” in the sense that they guarantee that the termination state will be reached from every initial state, while other policies (called improper) are not.
5 Adaptive and Model Predictive 
Control 
Contents 
5.1. Systems with Unknown Parameters - Robust and PID . . . Control . . . . . . . . . . . . . . . . . . . . . p. 102 
5.2. Approximation in Value Space, Rollout, and Adaptive . . . Control . . . . . . . . . . . . . . . . . . . . . p. 105 
5.3. Approximation in Value Space, Rollout, and Model . . . . . Predictive Control . . . . . . . . . . . . . . . . p. 109 
5.4. Terminal Cost Approximation - Stability Issues . . . . p. 112 5.5. Notes and Sources . . . . . . . . . . . . . . . . p. 118 
101
102 Adaptive and Model Predictive Control Chap. 5 
In this chapter, we discuss some of the core control system design methodologies within the context of our approximation in value space framework. In particular, in the next two sections, we will discuss problems with unknown or changing problem parameters, and briefly review some of the principal types of adaptive control methods. We will then focus on schemes that are based on on-line replanning, including the use of rollout. The idea here is to use an approximation in value space scheme/Newton step in place of a full reoptimization of the controller, in response to the changed system parameters; we have noted this possibility in Chapter 1. Subsequently, in Sections 5.3 and 5.4, we will discuss the model predictive control methodology, and its connections with approximation in value space, Newton’s method, adaptive control, and the attendant stability issues. 
5.1 SYSTEMS WITH UNKNOWN PARAMETERS - ROBUST AND PID CONTROL 
Our discussion so far dealt with problems with a known and unchanging mathematical model, i.e., one where the system equation, cost function, control constraints, and probability distributions of disturbances are perfectly known. The mathematical model may be available through explicit mathematical formulas and assumptions, or through a computer program that can emulate all of the mathematical operations involved in the model, including Monte Carlo simulation for the calculation of expected values. From our point of view, it makes no di!erence whether the mathematical model is available through closed form mathematical expressions or through a computer simulator: the methods that we discuss are valid either way, only their suitability for a given problem may be a!ected by the availability of mathematical formulas. 
In practice, however, it is common that the system involves parameters that are either not known exactly or may change over time. In such cases it is important to design controllers that take the parameter changes into account. The methodology for doing so is generally known as adaptive control , an intricate and multifaceted subject, with many and diverse applications, and a long history.† 
We should note also that unknown problem environments are an integral part of the artificial intelligence view of RL. In particular, to quote 
† The di!culties of designing adaptive controllers are often underestimated. 
Among others, they complicate the balance between o"-line training and on-line 
play, which we discussed in Chapter 1 in connection to AlphaZero. It is worth keeping in mind that as much as learning to play high quality chess is a great 
challenge, the rules of play are stable and do not change unpredictably in the 
middle of a game! Problems with changing system parameters can be far more challenging!
Sec. 5.1 Systems with Unknown Parameters - Robust and PID Control 103 
from the book by Sutton and Barto [SuB18], “learning from interaction with the environment is a foundational idea underlying nearly all theories of learning and intelligence.” The idea of interaction with the environment is typically connected with the idea of exploring the environment to identify its characteristics. In control theory this is often viewed as part of the system identification methodology, which aims to construct mathematical models of dynamic systems by using data. The system identification process is often combined with the control process to deal with unknown or changing problem parameters. This is one of the most challenging areas of stochastic optimal and suboptimal control, and has been studied extensively since the early 1960s. 
Robust and PID Control 
Given a controller design that has been obtained assuming a nominal DP problem model, one possibility is to simply ignore changes in problem parameters. We may then try to design a controller that is adequate for the entire range of the changing parameters. This is sometimes called a robust controller . A robust controller makes no e!ort to keep track of changing problem parameters. It is just designed so that it is resilient to parameter changes, and in practice, it often tends to be biased towards addressing the worst case. 
An important and time-honored robust control approach for continu-ous-state problems is the PID (Proportional-Integral-Derivative) controller ; see e.g., the books by Aström and Hagglund [AsH95], [AsH06]. In particular, PID control aims to maintain the output of a single-input single-output dynamic system around a set point or to follow a given trajectory, as the system parameters change within a relatively broad range. In its simplest form, the PID controller is parametrized by three scalar parameters, which may be determined by a variety of methods, some of them man-ual/heuristic. PID control is used widely and with success, although its range of application is mainly restricted to relatively simple, single-input and single-output continuous-state control systems. 
Combined System Identification and Control 
In robust control schemes, such as PID control, no attempt is made to maintain a mathematical model and to track unknown model parameters as they change. Alternatively we may introduce into the controller a mechanism for measuring or estimating the unknown or changing system parameters, and make suitable control adaptations in response.† 
† In the adaptive control literature, schemes that involve parameter estima-
tion are sometimes called indirect , while schemes that do not involve parameter estimation (like PID control) are called direct . To quote from the book by Aström
104 Adaptive and Model Predictive Control Chap. 5 
k Controller 
) System Data Control Parameter Estimation 
System Data Control Parameter Estimation 
System State Data Control Parameter Estimation 
System State Data Control Parameter Estimation 
System State Data Control Parameter Estimation System State Data Control Parameter Estimation 
Adaptive 
Figure 5.1.1 Schematic illustration of concurrent parameter estimation and system control. The system parameters are estimated on-line and the estimates are passed on to the controller whenever this is desirable (e.g., after the estimates change substantially). This structure is also known as indirect adaptive control. 
Let us note here that updating problem parameters need not require an elaborate algorithm. In many cases the set of problem parameters may take a known finite set of values (for example each set of parameter values may correspond to a distinct maneuver of a vehicle, motion of a robotic arm, flying regime of an aircraft, etc). Once the control scheme detects a change in problem parameters, it can incorporate the change into the approximation in value space scheme, and in the case of policy rollout, it may switch to a corresponding predesigned base policy. 
In what follows in this chapter (including our discussion of MPC in Section 5.3), we will assume that there is a mechanism to learn (perhaps imperfectly and by some unspecified procedure) the model of the system as it evolves over time. We will loosely refer to this learning process with the classical name system identification, but we will not go into specific identification methods, keeping in mind that such methods could be imprecise and challenging, but could also be fast and simple, depending on the problem at hand. 
An apparently reasonable scheme is to separate the control process into two phases, a system identification phase and a control phase. In the first phase the unknown parameters are estimated, while the control takes no account of the interim results of estimation. The final parameter 
and Wittenmark [AsW08], “indirect methods are those in which the estimated parameters are used to calculate required controller parameters” (see Fig. 5.1.1). 
The methods subsequently described in this section, and the rollout-based adap-
tive control methods discussed in the next section should be viewed as indirect.
Sec. 5.2 Approximation in Value Space, Rollout, and Adaptive Control 105 
estimates from the first phase are then used to implement an optimal or suboptimal policy in the second phase. 
This alternation of estimation and control phases may be repeated several times during the system’s operation in order to take into account subsequent changes of the parameters. Note that it is not necessary to introduce a hard separation between the identification and the control phases. They may be going on simultaneously, with new parameter estimates being generated in the background, and introduced into the control process, whenever this is thought to be desirable; see Fig. 5.1.1. 
One drawback of this approach is that it is not always easy to determine when to terminate one phase and start the other. A second di"culty, of a more fundamental nature, is that the control process may make some of the unknown parameters invisible to the estimation process. This is known as the problem of parameter identifiability , which is discussed in the context of adaptive control in several sources. On-line parameter estimation algorithms, which address among others the issue of identifiability, have been discussed extensively in the control theory literature, but the corresponding methodology is complex and beyond our scope in this book. However, assuming that we can make the estimation phase work somehow, we are free to reoptimize the controller using the newly estimated parameters, in a form of on-line replanning process. 
Unfortunately, there is still another di"culty with this type of online replanning: it may be hard to recompute an optimal or near-optimal policy on-line, using a newly identified system model. In particular, it may be impossible to use time-consuming and/or data-intensive methods that involve for example the training of a neural network, or discrete/integer control constraints. A simpler possibility is to use rollout, which we discuss in the next section. 
5.2 APPROXIMATION IN VALUE SPACE, ROLLOUT, AND ADAPTIVE CONTROL 
We will now consider an approach for dealing with unknown or changing parameters, which is based on rollout and on-line replanning. We have already noted this approach in Chapter 1, where we stressed the importance of fast on-line policy improvement. 
Let us assume that some problem parameters change over time, while the controller estimates the changes on-line, perhaps after a suitable delay for data collection. The method by which the problem parameters are recalculated or become known is immaterial for the purposes of the following discussion. It may involve a limited form of parameter estimation, whereby the unknown parameters are “tracked” by data collection over a few time stages, with due attention paid to issues of parameter identifiability; or it may involve new features of the control environment, such as a changing number of servers and/or tasks in a service system.
106 Adaptive and Model Predictive Control Chap. 5 
We thus assume away/ignore the detailed issues of parameter estimation, and focus on revising the controller by on-line replanning based on the newly obtained parameters. This revision may be based on any suboptimal method, but rollout with some base policy is particularly attractive. The base policy may be either a fixed robust controller (such as some form of PID control) or it may be updated over time (in the background, on the basis of some unspecified rationale), in which case the rollout policy will be revised both in response to the changed base policy and in response to the changing parameters. 
Here the advantage of rollout is that it is simple, reliable, and relatively fast. In particular, it does not require a complicated training procedure, based for example on the use of neural networks or other approximation architectures, so no new policy is explicitly computed in response to the parameter changes . Instead the available controls at the current state are compared through a one-step or multistep minimization, with cost function approximation provided by the base policy (cf. Fig. 5.2.1). 
Another issue to consider is the stability and robustness properties of the rollout policy. In this connection, it can be generally proved, under mild conditions, that if the base policy is stable within a range of parameter values, the same is true for the rollout policy ; this can also be inferred from Fig. 3.4.3. Related ideas have a long history in the control theory literature; see Beard [Bea95], Beard, Saridis, and Wen [BSW99], Jiang and Jiang [JiJ17], Kalise, Kundu, Kunisch [KKK20], Pang and Jiang [PaJ21]. 
The principal requirement for using rollout in an adaptive control context is that the rollout control computation should be fast enough to be performed between stages. In this connection, we note that acceler-ated/truncated or simplified versions of rollout, as well as parallel computation, can be used to meet this time constraint. 
Generally, adaptive control by rollout and on-line replanning makes sense in situations where the calculation of the rollout controls for a given set of problem parameters is faster and/or more convenient than the calculation of the optimal controls for the same set of parameter values. These problems include cases involving nonlinear systems and/or di"cult (e.g., integer) constraints. 
The following example illustrates on-line replanning with the use of rollout in the context of the simple one-dimensional linear quadratic problem that we discussed earlier. The purpose of the example is to show analytically how rollout with a base policy that is optimal for a nominal set of problem parameters works well when the parameters change from their nominal values. This property is not practically useful in linear quadratic problems because when the parameter change, it is possible to calculate the new optimal policy in closed form, but it is indicative of the performance robustness of rollout in other contexts; for example linear quadratic problems with constraints.
Sec. 5.2 Approximation in Value Space, Rollout, and Adaptive Control 107 
Multiagent Q-factor minimization xk 
Possible States Possible States xk+1 
Rollout with Base Policy Rollout with Base Policy 
Changing System, Cost, and Constraint Parameters 
Changing System, Cost, and Constraint Parameters Changing System, Cost, and Constraint Parameters 
Lookahead Minimization Lookahead Minimization 
Figure 5.2.1 Schematic illustration of adaptive control by on-line replanning based on rollout. One-step lookahead minimization is followed by simulation with the base policy, which stays fixed. The system, cost, and constraint parameters are changing over time, and the most recent estimates of their values are incorporated into the lookahead minimization and rollout operations. Truncated rollout with multistep lookahead minimization and terminal cost approximation is also possible. The base policy may also be revised based on various criteria. For the discussion of this section, we may assume that all the changing parameter information is provided by some computation and sensor “cloud” that is beyond our control. 
Example 5.2.1 (On-Line Replanning for Linear Quadratic Problems Based on Rollout) 
Consider a deterministic undiscounted infinite horizon linear quadratic problem involving the linear system 
xk+1 = xk + buk, 
and the quadratic cost function 
lim N!" 
N#1 ! 
k=0 
(x2 k + ru2 
k ). 
This is the one-dimensional problem of the preceding section for the special case where a = 1 and q = 1. The optimal cost function is given by 
J$(x) = K$x2,
108 Adaptive and Model Predictive Control Chap. 5 
where K$ is the unique positive solution of the Riccati equation 
K = rK 
r + b2K + 1. (5.1) 
The optimal policy has the form 
µ$(x) = L$x, (5.2) 
where 
L$ = ! bK$ 
r + b2K$ . (5.3) 
As an example, consider the optimal policy that corresponds to the nominal problem parameters b = 2 and r = 0.5: this is the policy (5.2)-(5.3), with K computed as the positive solution of the quadratic Riccati Eq. (5.1) for b = 2 and r = 0.5 . For these nominal parameter values, we have 
K$ = 2 + 
" 6 
4 # 1.11. 
From Eq. (5.3) we then also obtain 
L$ = ! 2 + 
" 6 
5 + 2 " 6 . (5.4) 
We will now consider changes of the values of b and r while keeping L constant to the preceding value, and we will compare the quadratic cost coe!cients of the following three cost functions as b and r vary: 
(a) The optimal cost function K$x2, where K$ is given by the positive solution of the Riccati Eq. (5.1). 
(b) The cost function KLx 2 that corresponds to the base policy 
µL(x) = Lx, 
where L is given by Eq. (5.4). Here, we have (cf. Section 4.1) 
KL = 1 + rL2 
1! (1 + bL)2 . (5.5) 
(c) The cost function K̃Lx 2 that corresponds to the rollout policy 
µ̃L(x) = L̃x, 
obtained by using the policy µL as base policy. Using the formulas derived earlier, we have [cf. Eq. (5.5)] 
L̃ = ! bKL 
r + b2KL 
,
Sec. 5.3 Approximation in Value Space - Model Predictive Control 109 
and (cf. Section 4.1) 
K̃L = 1 + rL̃2 
1! (1 + bL̃)2 . 
Figure 5.2.2 shows the coe!cients K$, KL, and K̃L for a range of values of r and b. We have 
K$ $ K̃L $ KL. 
The di"erence KL !K$ is indicative of the robustness of the policy µL, i.e., the performance loss incurred by ignoring the changes in the values of b and r, and continuing to use the policy µL, which is optimal for the nominal values b = 2 and r = 0.5, but suboptimal for other values of b and r. The di"erence K̃L ! K$ is indicative of the performance loss due to using online replanning by rollout rather than using optimal replanning. Finally, the di"erence KL ! K̃L is indicative of the performance improvement due to online replanning using rollout rather than keeping the policy µL unchanged. 
Note that Fig. 5.2.2 illustrates the behavior of the error ratio 
J̃ ! J$ 
J ! J$ , 
where for a given initial state, J̃ is the rollout performance, J$ is the optimal performance, and J is the base policy performance. This ratio approaches 0 as J ! J$ becomes smaller because of the superlinear/quadratic convergence rate of Newton’s method that underlies the rollout algorithm. 
5.3 APPROXIMATION IN VALUE SPACE, ROLLOUT, AND MODEL PREDICTIVE CONTROL 
In this section, we briefly discuss the MPC methodology, with a view towards its connection with approximation in value space and the rollout algorithm. We will focus on the undiscounted infinite horizon deterministic problem, which involves the system 
xk+1 = f(xk, uk), 
whose state xk and control uk are finite-dimensional vectors. The cost per stage is assumed nonnegative 
g(xk, uk) ! 0, for all (xk, uk), 
(e.g., a positive definite quadratic cost). There are control constraints uk " U(xk), and to simplify the following discussion, we will initially consider no state constraints. We assume that the system can be kept at the origin at zero cost, i.e., 
f(0, uk) = 0, g(0, uk) = 0 for some control uk " U(0).
110 Adaptive and Model Predictive Control Chap. 5 
0.6 0.8 1 1.2 1.4 1.6 1.8 2 2.2 2.4 1 
1.2 
1.4 
1.6 
1.8 
2 
2.2 
2.4 
Fixed Base Policy Adaptive Fixed Base Policy Adaptive 
Fixed Base Policy Adaptive Rollout Adaptive Reoptimization Adaptive Reoptimization 
With the Newton Step Adaptive Rollout 
0 5 10 15 20 25 30 1 
2 
3 
4 
5 
6 
7 
8 
Fixed Base Policy Adaptive Fixed Base Policy Adaptive 
Fixed Base Policy Adaptive Rollout Adaptive Reoptimization Adaptive Reoptimization 
With the Newton Step Adaptive Rollout 
Figure 5.2.2 Illustration of control by rollout under changing problem parameters. The quadratic cost coe!cients K$ (optimal, denoted by solid line), KL (base policy, denoted by circles), and K̃L (rollout policy, denoted by asterisks) are shown for the two cases where r = 0.5 and b varies, and b = 2 and r varies. The value of L is fixed at the value that is optimal for b = 2 and r = 0.5 [cf. Eq. (5.4)]. The rollout policy performance is very close to optimal, even when the base policy is far from optimal. 
Note that, as the figure illustrates, we have 
lim J!J 
! 
J̃ ! J$ 
J ! J$ = 0, 
where for a given initial state, J̃ is the rollout performance, J$ is the optimal performance, and J is the base policy performance. This is a consequence of the superlinear/quadratic convergence rate of Newton’s method that underlies rollout, and guarantees that the rollout performance approaches the optimal much faster than the base policy performance does. 
For a given initial state x0, we want to obtain a sequence {u0, u1, . . .} that satisfies the control constraints, while minimizing the total cost.
Sec. 5.3 Approximation in Value Space - Model Predictive Control 111 
uk x 
k xk+1 
-Factors Current State x 
Current State xk 
Next Cities Next States 
Sample Q-Factors imulation Control 1 Control 2 Control 3 
,n Stage k k Stages Stages k+1, . . . , k+!!1 
Sample Q-Factors Simulation Control 1 State Sample Q-Factors Simulation Control 1 State xk+! = 0 
1)-Stages Base Heuristic Minimization k (!! 1)-Stages Base Heuristic Minimization 
Figure 5.3.1 Illustration of the problem solved by a classical form of MPC at state xk. We minimize the cost function over the next ! stages while imposing the requirement that xk+! = 0. We then apply the first control of the optimizing sequence. In the context of rollout, the minimization over uk is the one-step lookahead, while the minimization over uk+1, . . . , uk+!#1 that drives xk+! to 0 is the base heuristic. 
This is a classical problem in control system design, known as the regulation problem, where the aim is to keep the state of the system near the origin (or more generally some desired set point), in the face of disturbances and/or parameter changes. In an important variant of the problem, there are additional state constraints of the form xk " X , and there arises the issue of maintaining the state within X , not just at the present time but also in future times. We will address this issue later in this section. 
The Classical Form of MPC - View as a Rollout Algorithm 
We will first focus on a classical form of the MPC algorithm, proposed in the form given here by Keerthi and Gilbert [KeG88]. In this algorithm, at each encountered state xk, we apply a control ũk that is computed as follows; see Fig. 5.3.1: 
(a) We solve an !-stage optimal control problem involving the same cost function and the requirement that the state after ! steps is driven to 0, i.e., xk+! = 0. This is the problem 
min ut, t=k,...,k+!!1 
k+!!1 ! 
t=k 
g(xt, ut), (5.6) 
subject to the system equation constraints 
xt+1 = f(xt, ut), t = k, . . . , k + !# 1, (5.7)
112 Adaptive and Model Predictive Control Chap. 5 
the control constraints 
ut " U(xt), t = k, . . . , k + !# 1, (5.8) 
and the terminal state constraint 
xk+! = 0. (5.9) 
Here ! is an integer with ! > 1, which is chosen in some largely empirical way. 
(b) If {ũk, . . . , ũk+!!1} is the optimal control sequence of this problem, we apply ũk and we discard the other controls ũk+1, . . . , ũk+!!1. 
(c) At the next stage, we repeat this process, once the next state xk+1 is revealed. 
To make the connection of the preceding MPC algorithm with rollout, we note that the one-step lookahead function J̃ implicitly used by MPC [cf. Eq. (5.6)] is the cost function of a certain stable base policy. This is the policy that drives to 0 the state after !# 1 stages (not ! stages) and keeps the state at 0 thereafter, while observing the state and control constraints, and minimizing the associated (!#1)-stages cost. This rollout view of MPC was first discussed in the author’s paper [Ber05]. It is useful for making a connection with the approximate DP/RL, rollout, and its interpretation in terms of Newton’s method. In particular, an important consequence is that the MPC policy is stable, since rollout with a stable base policy yields a stable policy, as we have discussed in Section 3.2. 
We may also equivalently view the preceding MPC algorithm as rollout with !̄-step lookahead, where 1 < !̄ < !, with the base policy that drives to 0 the state after ! # !̄ stages and keeps the state at 0 thereafter. This suggests variations of MPC that involve truncated rollout with terminal cost function approximation, which we will discuss shortly. 
Note also that when faced with changing problem parameters, it is natural to consider on-line replanning as per our earlier discussion. In particular, once new estimates of system and/or cost function parameters become available, MPC can adapt accordingly by introducing the new parameter estimates into the !-stage optimization problem in (a) above. 
5.4 TERMINAL COST APPROXIMATION - STABILITY ISSUES 
In a common variant of MPC, the requirement of driving the system state to 0 in ! steps in the !-stage MPC problem (5.6), is replaced by a nonnegative terminal cost G(xk+!). Thus at state xk, we solve the problem 
min ut, t=k,...,k+!!1 
" 
G(xk+!) + k+!!1 ! 
t=k 
g(xt, ut) 
# 
, (5.10)
Sec. 5.4 Terminal Cost Approximation - Stability Issues 113 
instead of problem (5.6) where we require that xk+! = 0. This variant can be viewed as rollout with one-step lookahead, and a base policy, which at state xk+1 applies the first control ũk+1 of the sequence {ũk+1, . . . , ũk+!!1} that minimizes 
G(xk+!) + k+!!1 ! 
t=k+1 
g(xt, ut). 
It can also be viewed outside the context of rollout, as approximation in value space with !-step lookahead minimization and terminal cost approximation given by G. Thus the preceding MPC controller may have cost function that is much closer to J* than G is. This is due to the su-perlinear/quadratic convergence rate of Newton’s method that underlies approximation in value space, as we have discussed in Chapter 3. 
An important question is to choose the terminal cost approximation so that the resulting MPC controller is stable. Our discussion of Section 3.3 on the region of stability of approximation in value space schemes applies here. In particular, under the nonnegative cost assumption of this section, the MPC controller will be stable if TG $ G (using the abstract DP notation introduced in Chapter 3), or equivalently 
(TG)(x) = min u"U(x) 
$ 
g(x, u) +G % 
f(x, u) & 
' 
$ G(x), for all x, (5.11) 
as noted in Section 3.2. This condition is su"cient for stability of the MPC controller, but it is not necessary. Figure 5.4.1 provides a graphical illustration. It shows that the condition TG $ G implies that J* $ T !G $ T !!1G for all ! ! 1 (the books [Ber12] and [Ber18a] provide mathematical proofs of this fact). This in turn implies that T !G lies within the region of the stability for all ! ! 0. 
We also expect that as the length ! of the lookahead minimization is increased, the stability properties of the MPC controller are improved. In particular, given G ! 0, the resulting MPC controller is likely to be stable for ! su!ciently large, since T !G ordinarily converges to J*, which lies within the region of stability. Results of this type are known within the MPC framework under various conditions (see the papers by Mayne at al. [MRR00], Magni et al. [MDM01], the MPC book [RMD17], and the author’s book [Ber20a], Section 3.1.2). Our discussion of stability in Sections 4.4 and 4.6 is also relevant within this context. 
In another variant of MPC, in addition to the terminal cost function approximation G, we use truncated rollout, which involves running some stable base policy µ for a number of steps m; see Fig. 5.4.2. This is quite similar to standard truncated rollout, except that the computational solution of the lookahead minimization problem (5.10) may become complicated when the control space is infinite. As discussed in Section 3.3, increasing the length of the truncated rollout enlarges the region of stability of the MPC controller . The reason is that by increasing the length of the
114 Adaptive and Model Predictive Control Chap. 5 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Optimal cost Cost of rollout policy ˜ 
1 J J 
also Newton Step 
TJ GJ̃ Jµ̃ 
Defined by MPC Policy µ̃ 
Cost of Truncated Rollout Policy ˜ 
Yields Truncated Rollout Policy ˜ Defined by Defined by MPC Policy µ̃ 
) Tµ̃T !!1G = T !G 
J̃ ! = 3 
Instability Region Stability Region 0 
J̃ Region where TG ! G 
1 T !!1G 
Slope = 1 
Figure 5.4.1 Illustration of the condition TG " G or equivalently 
(TG)(x) = min u%U(x) 
$ 
g(x, u) +G % 
f(x, u) & 
' 
" G(x), for all x. 
When satisfied by the terminal cost function approximation G, it guarantees the stability of the MPC policy µ̃ with !-step lookahead minimization, defined by 
Tµ̃T !#1 
G = T ! G, 
where for a generic policy µ, Tµ is defined (using the abstract DP notation of Chapter 3) by 
(TµJ)(x) = g % 
x, µ(x) & 
+ J 
( 
f % 
x, µ(x) & 
) 
, for all x. 
In this figure, ! = 3. 
truncated rollout, we push the start of the Newton step towards of the cost function Jµ of the stable policy, which lies within the region of stability since TJµ $ TµJµ = Jµ; see also the discussion on linear quadratic problems in Section 4.7. The base policy may also be used to address state constraints; see the papers by Rosolia and Borelli [RoB17], [RoB19], and the discussion in the author’s RL book [Ber20a].
Sec. 5.4 Terminal Cost Approximation - Stability Issues 115 
! TJ 
Prob. = 1 Prob. = 
J J! = TJ! 
0 Prob. = 1 
1 J J 
Cost-to-go approximation Expected value approximation TµJ 
Optimal cost Cost of rollout policy ˜ 
Yields Truncated Rollout Policy ˜ Defined by 
1 J J 
also Newton Step 
Tµ̃T !!1(Tm µ G) = T !(Tm 
µ G) Yields Truncated Rollout Policy ˜ fined by 
TJ G 
Defined by MPC Policy µ̃ 
J̃ Jµ̃ 
Defined by MPC Policy µ̃ 
Cost of Truncated Rollout Policy ˜ 
! = 2, m = 4 
) Tm µ G 
Base Policy 
Terminal Cost Approximation 
Terminal Cost Approximation Terminal Cost Approximation G 
m-Step Truncated Rollout with Stable Policy 
-Step Truncated Rollout with Stable Policy -Step Truncated Rollout with Stable Policy µ 
!-Step Lookahead Minimization 
-Step Lookahead Minimization -Step Lookahead Minimizati n 
µ x 
G T !( ) Tm µ G 
Instability Region Stability Region 0 
T !!1(Tm µ G) 
Slope = 1 
Figure 5.4.2 An MPC scheme with !-step lookahead minimization, m-step truncated rollout with a stable base policy µ, and a terminal cost function approximation G, together with its interpretation as a Newton step. In this figure, ! = 2 and m = 4. As m increases, Tm 
µ G moves closer to Jµ, which lies within the region 
of stability. 
A Rollout Variant of MPC with Multiple Terminal States and Base Policies 
In another variation of MPC, proposed in the paper by Li et al. [LJM21], instead of driving the state to 0 at the end of ! steps, we consider multiple terminal system states at the end of the !-step horizon, as well as the use of multiple base policies for rollout. In particular, in this scheme we have a finite set of states X and a finite set of stable base policies M, and we assume that we have computed o!-line the cost function values Jµ(x) for all x " X and µ " M. At state xk, to compute the MPC control ũk, we solve for each x " X a problem that is the same as the problem (5.6)-(5.9), which is solved by the classical form of MPC, except that the terminal state xk+! is equal to x instead of xk+! = 0. This is the problem 
min ut, t=k,...,k+!!1 
k+!!1 ! 
t=k 
g(xt, ut), (5.12)
116 Adaptive and Model Predictive Control Chap. 5 
subject to the system equation constraints 
xt+1 = f(xt, ut), t = k, . . . , k + !# 1, (5.13) 
the control constraints 
ut " U(xt), t = k, . . . , k + !# 1, (5.14) 
and the terminal state constraint 
xk+! = x. (5.15) 
Let V (xk;x) be the optimal value of this problem. Having computed V (xk;x) for all x " X , we compare all values 
V (xk;x) + Jµ(x), x " X , µ " M, 
and find the pair (x, µ) that yields the minimal value of V (xk;x) + Jµ(x). We then define the MPC control ũk to be the control uk that attains the minimum in the corresponding problem (5.12)-(5.15) with x = x. 
Thus, in this variant of MPC we solve multiple problems of the type that is solved in the classical form of MPC, for multiple values of the terminal state xk+!, and we then compute the MPC control based on the “best” terminal state x " X , assuming that the “best” base policy µ will be used after state k+!. It is possible to show, under appropriate conditions,† that the cost function Jµ̃ of the MPC policy µ̃, which applies µ̃(xk) = ũk 
as described above, has the cost improvement property 
Jµ̃(x) $ Jµ(x), for all x " X , µ " M; (5.16) 
see [LJM21]. Moreover, based on this property and the assumption that the base policies µ " M are stable, it follows that the MPC policy µ̃ thus obtained is also stable. 
The preceding variation can also be used for systems with arbitrary state and control spaces, continuous as well as discrete. It is also well-suited for addressing state constraints, provided the base policies are designed to satisfy these constraints. In this case, the state constraints are included in the constraints of the !-step problems (5.12)-(5.15). We refer to the paper [LJM21], which provides supporting analysis, extensions to the case where X is an infinite set, as well as computational results involving several types of problems, with both discrete and continuous state and control spaces. 
We mention that the idea of using multiple base policies to evaluate the available controls at a given state, and selecting the control that yields the least cost, has been known since the original proposal of the paper [BTW97]. The main result for such schemes is a cost improvement property, whereby the rollout policy outperforms simultaneously all the base policies; cf. Eq. (5.16). This property is also discussed in Sections 6.3 and 6.4, as well as the books [Ber17a], [Ber19a], [Ber20a]. 
† These conditions include that for every x % X , we have f % 
x, µ(x) & 
% X for 
some µ % X , which plays the same role as the assumption that the origin is cost free and absorbing in the classical form of MPC.
Sec. 5.4 Terminal Cost Approximation - Stability Issues 117 
Stochastic MPC by Certainty Equivalence 
Let us mention that while in this section we have focused on deterministic problems, there are variants of MPC, which include the treatment of uncertainty. The books and papers cited earlier contain several ideas along these lines; see for example the books by Kouvaritakis and Cannon [KoC16], Rawlings, Mayne, and Diehl [RMD17], and the survey by Mesbah [Mes16]. 
In this connection it is also worth mentioning the certainty equivalence approach that we discussed briefly in Section 3.2. As noted in that section, upon reaching state xk we may perform the MPC calculations after replacing the uncertain quantities wk+1, wk+2, . . . with deterministic quantities wk+1, wk+2, . . ., while allowing for the stochastic character of the disturbance wk of just the current stage k. This MPC calculation is not much more di cult that the one for deterministic problems, while still implementing a Newton step for solving the associated Bellman equation; see the discussion of Section 3.2, and also Section 2.5.3 of the RL book [Ber19a]. 
State Constraints, Target Tubes, and O↵-Line Training 
Our discussion so far has skirted a major issue in MPC, which is that there may be additional state constraints of the form xk 2 X, for all k, where X is some subset of the true state space. Indeed much of the original work on MPC was motivated by control problems with state constraints, imposed by the physics of the problem, which could not be handled e↵ectively with the nice unconstrained framework of the linear quadratic problem that we have discussed in Chapter 4. 
The treatment of state constraints is connected to the theory of reachability of target tubes, first formulated and studied by the author in his Ph.D. thesis [Ber71], and subsequent papers [BeR71], [Ber72]; see the books [Ber17a], [Ber19a], [Ber20a] for a discussion that is consistent with the viewpoint of this section. A target tube is a subset X̃ of the state constraint set X, within which the state can be kept indefinitely with feasible control choices, assuming that the initial state belongs to X̃. In other words, the problem (5.10) may not be feasible for every xk 2 X, once the constraint xt 2 X for all t = k + 1, k + 2, . . ., is added in problem (5.10). However, a suitable target tube is one specified by a subset X̃ ⇢ X such that the problem (5.10) is feasible under the constraint xt 2 X̃ for all t = k+1, k+2, . . ., provided xk 2 X̃. 
There are several ways to compute sets X̃ with this property, for which we refer to the aforementioned author’s work and the MPC literature; see e.g., the book by Rawlings, Mayne, and Diehl [RMD17], and the survey by Mayne [May14]. The important point here is that the computation of a target tube must be done o↵-line with one of several available algorithmic
118 Adaptive and Model Predictive Control Chap. 5 
approaches, so it becomes part of the o!-line training (in addition to the terminal cost function G). 
Given an o!-line training process, which provides a target tube constraint xk " X̃ for all k, a terminal cost function G, and possibly one or more base policies for truncated rollout, MPC becomes an on-line play algorithm for which our earlier discussion applies. Note, however, that in an indirect adaptive control context, where a model is estimated on-line as it is changing, it may be di"cult to recompute on-line a target tube that can be used to enforce the state constraints of the problem, particularly if the states constraints change themselves as part of the changing problem data. This is a problem-dependent issue that deserves further attention. 
5.5 NOTES AND SOURCES 
The literature for PID control is extensive and includes the books by Aström and Hagglund [AsH95], [AsH06]. For detailed accounts of adaptive control, we refer to the books by Aström and Wittenmark [AsW08], Bodson [Bod20], Goodwin and Sin [GoS84], Ioannou and Sun [IoS96], Jiang and Jiang [JiJ17], Krstic, Kanellakopoulos, and Kokotovic [KKK95], Koko-tovic [Kok91], Kumar and Varaiya [KuV86], Liu, et al. [LWW17], Lavretsky and Wise [LaW13], Narendra and Annaswamy [NaA12], Sastry and Bod-son [SaB11], Slotine and Li [SlL91], and Vrabie, Vamvoudakis, and Lewis [VVL13]. 
The literature on MPC is voluminous, and has grown over time to include problem and algorithm variations and extensions. For detailed accounts, we refer to the textbooks by Maciejowski [Mac02], Goodwin, Seron, and De Dona [GSD06], Camacho and Bordons [CaB07], Kouvaritakis and Cannon [KoC16], Borrelli, Bemporad, and Morari [BBM17], and Rawlings, Mayne, and Diehl [RMD17]. 
Deterministic optimal control with infinite state and control spaces can exhibit unusual/pathological behavior. For the case of nonnegative cost per stage, an analysis of the exact value and policy iteration algorithms, including convergence issues and counterexamples, is given in the author’s paper [Ber17b] and abstract DP book [Ber22a]. The case of nonpositive cost per stage has been addressed in classical analyses, beginning with the work of Blackwell [Bla65]; see also [Str66], [BeS78], [YuB15].
6 Finite Horizon Deterministic 
Problems - Discrete Optimization 
Contents 
6.1. Deterministic Discrete Spaces Finite Horizon Problems p. 120 6.2. General Discrete Optimization Problems . . . . . . . p. 125 6.3. Approximation in Value Space . . . . . . . . . . . p. 128 6.4. Rollout Algorithms for Discrete Optimization . . . . . p. 132 6.5. Rollout and Approximation in Value Space with Multistep . . 
Lookahead . . . . . . . . . . . . . . . . . . . . p. 149 6.6. Constrained Forms of Rollout Algorithms . . . . . . p. 158 6.7. Adaptive Control by Rollout with a POMDP Formulation p. 173 6.8. Rollout for Minimax Control . . . . . . . . . . . . p. 181 6.9. Small Stage Costs and Long Horizon - Continuous-Time . . . 
Rollout . . . . . . . . . . . . . . . . . . . . . p. 190 6.10. Epilogue . . . . . . . . . . . . . . . . . . . . p. 197 
119
120 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
In this chapter, we discuss finite horizon deterministic problems, focusing primarily on the case where the state and control spaces are finite. After we introduce these problems, we will argue that they can be transformed to infinite horizon SSP problems, through the use of an artificial cost-free termination state that the system moves into at the end of the horizon. Once the problem is transformed to an infinite horizon SSP problem, the ideas of approximation in value space, o!-line training, on-line play, and Newton’s method, which we have developed earlier, become applicable. Moreover the ideas of MPC and adaptive control are easily adapted within the finite horizon discrete optimization framework. 
An interesting aspect of our methodology for discrete deterministic problems is that it admits extensions that we have not discussed so far. The extensions include variants that apply to constrained forms of DP, which involve constraints on the entire system trajectory, and also allow the use of heuristic algorithms that are more general than policies within the context of rollout. These variants rely on the problem’s deterministic structure, and do not extend to stochastic problems. 
Another interesting aspect of discrete deterministic problems is that they can serve as a framework for an important class of commonly encountered discrete optimization problems, including integer programming and combinatorial optimization problems such as scheduling, assignment, routing, etc. This will bring to bear the methodology of approximation in value space, rollout, adaptive control, and MPC, and provide e!ective suboptimal solution methods for these problems. 
In the present chapter, we provide a brief summary of approximation in value space and rollout algorithms, aimed to make the connection with approximation in value space and Newton’s method for infinite horizon problems. Additional discussion may be found in the author’s rollout and policy iteration book [Ber20a], on which this chapter is based. Moreover, in Section 6.7-6.9, we will discuss DP problems that have a methodological connection to deterministic finite horizon DP, but require various algorithmic extensions. 
6.1 DETERMINISTIC DISCRETE SPACES FINITE HORIZON PROBLEMS 
In deterministic finite horizon DP problems, the state is generated nonrandomly over N stages, and involves a system of the form 
xk+1 = fk(xk, uk), k = 0, 1, . . . , N ! 1, (6.1) 
where k is the time index, and 
xk is the state of the system, an element of some state space Xk, 
uk is the control or decision variable, to be selected at time k from some given set Uk(xk), a subset of a control space Uk, that depends on xk,
Sec. 6.1 Deterministic Discrete Spaces Finite Horizon Problems 121 
...... 
Control uk 
k Cost gk(xk, uk) ) xk k xk+1 +1 xN 
Stage k k Future Stages 
) x0 
Future Stages Terminal Cost Future Stages Terminal Cost gN(xN ) 
Deterministic Transition 
Deterministic Transition xk+1 = fk(xk, uk) 
Figure 6.1.1 Illustration of a deterministic N-stage optimal control problem. Starting from state xk, the next state under control uk is generated nonrandomly, according to 
xk+1 = fk(xk, uk), 
and a stage cost gk(xk, uk) is incurred. 
fk is a function of (xk, uk) that describes the mechanism by which the state is updated from time k to time k + 1. 
The state space Xk and control space Uk are arbitrary sets and may depend on k. Similarly the system function fk can be arbitrary and may depend on k. The cost incurred at time k is denoted by gk(xk, uk), and the function gk may depend on k. For a given initial state x0, the total cost of a control sequence {u0, . . . , uN!1} is 
J(x0;u0, . . . , uN!1) = gN(xN ) + N!1 ! 
k=0 
gk(xk, uk), (6.2) 
where gN(xN ) is a terminal cost incurred at the end of the process. This is a well-defined number, since the control sequence {u0, . . . , uN!1} together with x0 determines exactly the state sequence {x1, . . . , xN} via the system equation (6.1); see Figure 6.1.1. We want to minimize the cost (6.2) over all sequences {u0, . . . , uN!1} that satisfy the control constraints, thereby obtaining the optimal value as a function of x0 
J*(x0) = min uk!Uk(xk) k=0,...,N"1 
J(x0;u0, . . . , uN!1). 
Notice an important di!erence from the stochastic case: we optimize over sequences of controls {u0, . . . , uN!1}, rather than over policies that consist of a sequence of functions ! = {µ0, . . . , µN!1}, where µk maps states xk into controls uk = µk(xk), and satisfies the control constraints µk(xk) " Uk(xk) for all xk. It is well-known that in the presence of stochastic uncertainty, policies are more e!ective than control sequences, and can result in improved cost. On the other hand for deterministic problems, minimizing over control sequences yields the same optimal cost as over policies, since the cost of any policy starting from a given state determines with certainty the controls applied at that state and the future states, and hence can also be achieved by the corresponding control sequence. This
122 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
s t u 
Artificial Terminal Node Terminal Arcs with Cost Equal to Ter-
Artificial Terminal Node Terminal Arcs with Cost Equal to Ter-
Initial State Stage 0 Stage 1 Stage 2 StageInitial S ate Stage 0 Stage 1 Stage 2 StageIniti l Sta e Stage 0 Stage 1 Stage 2 StageIni i l State Stage 0 Stage 1 Stage 2 Stage N ! 1 Stage1 Stage N . 
. . . . 
. 
. . . . 
. 
. . . . 
. 
. . . . 
) Artificial Terminal 
with Cost gN (xN ) 
State Space Partition Initial States 
x0 0 x1 
Current Position 
1 x2 
Current Position 
2 xN!1 1 xN 
x1 ) u1 
) Cost g1(x1, u1) 
xN!1 
xN 
0 
x0 
u0 
uN!1 
x2 
) x2 = f1(x1, u1) u 
State Transition 
Figure 6.1.2 Illustration of a deterministic finite-state DP problem. Nodes correspond to states xk. Arcs correspond to state-control pairs (xk, uk). An arc (xk, uk) has start and end nodes xk and xk+1 = fk(xk, uk), respectively. The cost gk(xk, uk) is the length of this arc. An artificial terminal node t is connected with an arc of cost gN (xN ) with each state xN . The problem is equivalent to finding a shortest path from initial nodes of stage 0 to the terminal node t. 
point of view allows more general forms of rollout, which we will discuss in this section: instead of using a policy for rollout, we will allow the use of more general heuristics for choosing future controls. 
Discrete Optimal Control - Transformation to an Infinite Horizon Problem 
We use the term discrete optimal control to refer to deterministic DP problems where the control spaces are either naturally discrete and consist of a finite number of elements, or have been discretized for the purposes of computation. Generally, whenever we assume that the control space is finite, we will also assume implicitly a single or at most a finite number of possible initial states, so the number of states that can be generated at each stage is also finite. A problem of this type can be conveniently described with an acyclic graph specifying for each state xk the possible transitions to next states xk+1. The nodes of the graph correspond to states xk and the arcs of the graph correspond to state-control pairs (xk, uk). Each arc with start node xk corresponds to a choice of a single control uk " Uk(xk) and has as end node the next state fk(xk, uk). The cost of an arc (xk, uk) is defined as gk(xk, uk); see Fig. 6.1.2. To handle the final stage, an artificial terminal node t is added. Each state xN at stage N is connected to the terminal node t with an arc having cost gN (xN ). 
Note that control sequences {u0, . . . , uN!1} correspond to paths originating at the initial state (a node at stage 0) and terminating at one of the nodes corresponding to the final stage N . If we view the cost of an arc as its length, we see that a deterministic finite-state finite horizon problem is equivalent to finding a minimum-length (or shortest) path from the initial nodes of the graph (stage 0) to the terminal node t. Here, by the length of a path we mean the sum of the lengths of its arcs. It also turns out that
Sec. 6.1 Deterministic Discrete Spaces Finite Horizon Problems 123 
the reverse is true: every shortest path problem involving a graph whose cycles have positive length can be transformed into a discrete optimal control problem. This fact is important, but will not be useful to us, so we will not consider it further here (see the textbook [Ber17a], Chapter 2, for a detailed discussion). 
The connection of finite state and control spaces finite horizon deterministic problem with a shortest path problem is important for our purposes. The reason is that it provides a bridge to an SSP problem with an infinite horizon, and by extension, to our earlier development of approximation in value space, Newton’s method, rollout, and the PI algorithm. It is also important to recognize that this SSP problem has a few additional special characteristics. These are: 
(a) The equivalent SSP involves a deterministic system, has a finite number of states and controls, and involves an acyclic graph. The states of the SSP are all the state-time pairs (xk, k), k = 0, 1, . . . , N , where xk is one of the finite number of elements of Xk that are reachable from one of the finite number of initial states x0 using a feasible sequence of controls. The possible transitions from states (xk, k) to states (xk+1, k + 1) correspond to controls uk " Uk(xk) such that xk+1 = fk(xk, uk). 
(b) The state space of the SSP expands as the horizon N becomes longer. While this complicates the use of the PI algorithm, it does not materially a!ect the use of a rollout algorithm. 
(c) The optimal cost function of the SSP is obtained from the optimal cost functions of the finite horizon problem, which are generated by the DP algorithm to be presented shortly. This DP algorithm can be viewed as the Bellman equation of the SSP. 
The Exact Dynamic Programming Algorithm 
The DP algorithm for finite horizon deterministic problems rests on a simple idea, the principle of optimality, which suggests that the optimal cost function can be constructed in piecemeal fashion going backwards: first compute the optimal cost function for the “tail subproblem” involving the last stage, then solve the “tail subproblem” involving the last two stages, and continue in this manner until the optimal cost function for the entire problem is constructed. 
By translating into mathematical terms the principle of optimality, we obtain the DP algorithm. It constructs functions 
J* N (xN ), J* 
N!1(xN!1), . . . , J* 0 (x0), 
sequentially, starting from J* N , and proceeding backwards to J* 
N!1, J * N!2, 
etc. The value J* k (xk) will be viewed as the optimal cost of the tail sub-
problem that starts at state xk at time k and ends at a state xN .
124 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
DP Algorithm for Deterministic Finite Horizon Problems 
Start with J* N (xN ) = gN (xN ), for all xN , (6.3) 
and for k = 0, . . . , N ! 1, let 
J* k (xk) = min 
uk"Uk(xk) 
" 
gk(xk, uk) + J* k+1 
# 
fk(xk, uk) $% 
, for all xk. 
(6.4) 
Note that at stage k, the calculation in Eq. (6.4) must be done for all states xk before proceeding to stage k ! 1. The key fact about the DP algorithm is that for every initial state x0, the number J* 
0 (x0) obtained at the last step, is equal to the optimal cost J*(x0). Indeed, a more general fact can be shown, namely that for all k = 0, 1, . . . , N ! 1, and all states xk at time k, we have 
J* k (xk) = min 
um!Um(xm) m=k,...,N"1 
J(xk;uk, . . . , uN!1), (6.5) 
where J(xk;uk, . . . , uN!1) is the cost generated by starting at xk and using subsequent controls uk, . . . , uN!1: 
J(xk;uk, . . . , uN!1) = gN(xN ) + N!1 ! 
t=k 
gt(xt, ut). 
Thus, J* k (xk) is the optimal cost for an (N ! k)-stage tail subproblem 
that starts at state xk and time k, and ends at time N . Based on this interpretation of J# 
k (xk), we call it the optimal cost-to-go from state xk at stage k, and refer to J# 
k as the optimal cost-to-go function or optimal cost function at time k. 
Once the functions J* 0 , . . . , J 
* N have been obtained, we can use a for-
ward algorithm to construct an optimal control sequence {u# 0, . . . , u 
# N!1} 
and state trajectory {x# 1, . . . , x 
# N} for a given initial state x0. 
Construction of Optimal Control Sequence {u# 0, . . . , u 
# N!1} 
Set u# 0 " arg min 
u0"U0(x0) 
" 
g0(x0, u0) + J* 1 
# 
f0(x0, u0) $ % 
, 
and x# 1 = f0(x0, u# 
0).
Sec. 6.2 General Discrete Optimization Problems 125 
Sequentially, going forward, for k = 1, 2, . . . , N ! 1, set 
u# k " arg min 
uk"Uk(x # k ) 
" 
gk(x# k, uk) + J* 
k+1 
# 
fk(x# k, uk) 
$ % 
, (6.6) 
and x# k+1 = fk(x# 
k, u # k). 
Note an interesting conceptual division of the optimal control sequence construction: there is “o!-line training” to obtain J* 
k by precomputation [cf. the DP Eqs. (6.3)-(6.4)], which is followed by “on-line play” in real-time to obtain u# 
k [cf. Eq. (6.6)]. This is analogous to the two algorithmic processes described in Chapter 1 in connection with chess and backgammon. 
6.2 GENERAL DISCRETE OPTIMIZATION PROBLEMS 
Discrete deterministic optimization problems, including challenging combinatorial problems, can be typically formulated as DP problems by breaking down each feasible solution into a sequence of decisions/controls. This formulation often leads to an intractable exact DP computation because of an exponential explosion of the number of states as time progresses. However, a reformulation to a discrete optimal control brings to bear approximate DP methods, such as rollout and others, to be discussed shortly, which can deal with the exponentially increasing size of the state space. We illustrate the reformulation with an example and then generalize. 
Example 6.2.1 (The Traveling Salesman Problem) 
An important model for scheduling a sequence of operations is the classical traveling salesman problem. Here we are given N cities and the travel time between each pair of cities. We wish to find a minimum time travel that visits each of the cities exactly once and returns to the start city. To convert this problem to a DP problem, we form a graph whose nodes are the sequences of k distinct cities, where k = 1, . . . , N . The k-city sequences correspond to the states of the kth stage. The initial state x0 consists of some city, taken as the start (city A in the example of Fig. 6.2.1). A k-city node/state leads to a (k+1)-city node/state by adding a new city at a cost equal to the travel time between the last two of the k+1 cities; see Fig. 6.2.1. Each sequence of N cities is connected to an artificial terminal node t with an arc of cost equal to the travel time from the last city of the sequence to the starting city, thus completing the transformation to a DP problem. 
The optimal costs-to-go from each node to the terminal state can be obtained by the DP algorithm and are shown next to the nodes. Note, how-
126 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCA B AC A BC BD ACB ACD ADB ADCA B AC AD ABC BD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCAB AC AD ABC ABD ACB ACD ADB ADCA AB AC D AB AB ACB ACD ADB ADCAB AC BC ACB ACD ADB ADCA D A AB ACB ACD ADB ADCAB A B ACB ACD ADB ADC 
ABCD ABDC ACBD ACDB ADBC ADCBABCD ABDC ACBD ACDB ADBC ADCBCD BDC BD CDB BC ADCBA AB C ACBD AC B ADBC ADCBCD DC A BD ACDB ADBC ADCBABC DC B DB DBC CB 
s Terminal State t 
Initial State x0 
Matrix of Intercity Travel Costs 
Matrix of Intercity Travel Costs ! 
A 
B 
C 
D Four Cities 
Figure 6.2.1 Example of a DP formulation of the traveling salesman problem. The travel times between the four cities A, B, C, and D are shown in the matrix at the bottom. We form a graph whose nodes are the k-city sequences and correspond to the states of the kth stage, assuming that A is the starting city. The transition costs/travel times are shown next to the arcs. The optimal costs-to-go are generated by DP starting from the terminal state and going backwards towards the initial state, and are shown next to the nodes. There is a unique optimal sequence here (ABDCA), and it is marked with thick lines. The optimal sequence can be obtained by forward minimization [cf. Eq. (6.6)], starting from the initial state x0. 
ever, that the number of nodes grows exponentially with the number of cities N . This makes the DP solution intractable for large N . As a result, large traveling salesman and related scheduling problems are typically addressed with approximation methods, some of which are based on DP, and will be discussed later. 
Let us now extend the ideas of the preceding example to the general discrete optimization problem: 
minimize G(u) 
subject to u " U,
Sec. 6.2 General Discrete Optimization Problems 127 
Artificial Start State End State 
) ... 
) ... 
) ... 
) ... 
) ...) 
... 
. . . i 
. . . i 
. . . i 
. . . i 
Set of States ( Set of States (Set of States ( Set of States ( 
Cost G(u) 
s t u 
Stage 1 Stage 2 Stage 3 Stage Stage 1 Stage 2 Stage 3 Stage Stage 1 Stage 2 Stage 3 Staget 1 t 2 Stage 3 Stage N 
Initial State 15 1 5 18 4 19 9 21 25 8 12 13 
(u0) ( ) (u0, u1) () (u0, u1, u2) ) u = (u0, . . . , uN!1) 
u0 
u1 
u2 
uN!1 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
) A p p roxim 
ate .. 
Figure 6.2.2 Formulation of a discrete optimization problem as a DP problem with N stages. There is a cost G(u) only at the terminal stage on the arc connecting an N-solution u = (u0, . . . , uN"1) upon reaching the terminal state. Note that there is only one incoming arc at each node. 
where U is a finite set of feasible solutions and G(u) is a cost function. We assume that each solution u has N components; i.e., it has the form u = (u0, . . . , uN!1), where N is a positive integer. We can then view the problem as a sequential decision problem, where the components u0, . . . , uN!1 
are selected one-at-a-time. A k-tuple (u0, . . . , uk!1) consisting of the first k components of a solution is called a k-solution. We associate k-solutions with the kth stage of the finite horizon discrete optimal control problem shown in Fig. 6.2.2. In particular, for k = 1, . . . , N , we view as the states of the kth stage all the k-tuples (u0, . . . , uk!1). For stage k = 0, . . . , N ! 1, we view uk as the control. The initial state is an artificial state denoted s. From this state, by applying u0, we may move to any “state” (u0), with u0 
belonging to the set 
U0 = & 
ũ0 | there exists a solution of the form (ũ0, ũ1, . . . , ũN!1) " U ' 
. (6.7) 
Thus U0 is the set of choices of u0 that are consistent with feasibility. More generally, from a state (u0, . . . , uk!1), we may move to any state 
of the form (u0, . . . , uk!1, uk), upon choosing a control uk that belongs to the set 
Uk(u0, . . . , uk!1) = & 
uk | for some uk+1, . . . , uN!1 we have 
(u0, . . . , uk!1, uk, uk+1, . . . , uN!1) " U ' 
. (6.8) 
These are the choices of uk that are consistent with the preceding choices u0, . . . , uk!1, and are also consistent with feasibility. The last stage corresponds to the N -solutions u = (u0, . . . , uN!1), and the terminal cost is
128 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
G(u); see Fig. 6.2.2. All other transitions in this DP problem formulation have cost 0. 
Let J* k (u0, . . . , uk!1) denote the optimal cost starting from the k-
solution (u0, . . . , uk!1), i.e., the optimal cost of the problem over solutions whose first k components are constrained to be equal to u0, . . . , uk!1. The DP algorithm is described by the equation 
J* k (u0, . . . , uk!1) = min 
uk"Uk(u0,...,uk"1) J* k+1(u0, . . . , uk!1, uk), 
with the terminal condition 
J* N (u0, . . . , uN!1) = G(u0, . . . , uN!1). 
This algorithm executes backwards in time: starting with the known function J* 
N = G, we compute J* N!1, then J* 
N!2, and so on up to computing J* 0 . 
An optimal solution (u# 0, . . . , u 
# N!1) is then constructed by going forward 
through the algorithm 
u# k " arg min 
uk"Uk(u # 0 ,...,u 
# k"1 
) J* k+1(u 
# 0, . . . , u 
# k!1, uk), k = 0, . . . , N!1, (6.9) 
where U0 is given by Eq. (6.7), and Uk is given by Eq. (6.8): first compute u# 0, then u# 
1, and so on up to u# N!1; cf. Eq. (6.6). 
Of course here the number of states typically grows exponentially with N , but we can use the DP minimization (6.9) as a starting point for approximation methods. For example we may try to use approximation in value space, whereby we replace J* 
k+1 with some suboptimal J̃k+1 in Eq. (6.9). One possibility is to use as 
J̃k+1(u# 0, . . . , u 
# k!1, uk), 
the cost generated by a heuristic method that solves the problem suboptimally with the values of the first k + 1 decision components fixed at u# 0, . . . , u 
# k!1, uk. This is the rollout algorithm, which turns out to be a very 
simple and e!ective approach for approximate combinatorial optimization. Let us finally note that while we have used a general cost function G 
and constraint set U in our discrete optimization model of this section, in many problems G and/or U may have a special (e.g., additive) structure, which is consistent with a sequential decision making process and may be computationally exploited. The traveling salesman Example 6.2.1 is a case in point, where G consists of N components (the intercity travel costs), one per stage. 
6.3 APPROXIMATION IN VALUE SPACE 
The forward optimal control sequence construction of Eq. (6.6) is possible only after we have computed J* 
k (xk) by DP for all xk and k. Unfortunately,
Sec. 6.3 Approximation in Value Space 129 
in practice this is often prohibitively time-consuming, because the number of possible pairs (xk, k) can be very large. However, a similar forward algorithmic process can be used if the optimal cost-to-go functions J* 
k are replaced by some approximations J̃k. This is the idea of approximation in value space that we have discussed earlier in connection with infinite horizon problems. It constructs a suboptimal solution {ũ0, . . . , ũN!1} in place of the optimal {u# 
0, . . . , u # N!1}, by using J̃k in place of J* 
k in the DP procedure (6.6). Based on our infinite horizon analysis of Chapter 3 and the interpretation of the deterministic finite horizon problem as an infinite horizon SSP, the cost function of the corresponding one-step lookahead policy can be viewed as the result of a Newton step for solving Bellman’s equation, i.e., the DP algorithm (6.4), starting from the point (J̃1, J̃2, . . . , J̃N ). 
Approximation in Value Space - Use of J̃k in Place of J* k 
Start with 
ũ0 " arg min u0"U0(x0) 
" 
g0(x0, u0) + J̃1 # 
f0(x0, u0) $ % 
, 
and set x̃1 = f0(x0, ũ0). 
Sequentially, going forward, for k = 1, 2, . . . , N ! 1, set 
ũk " arg min uk"Uk(x̃k) 
" 
gk(x̃k, uk) + J̃k+1 
# 
fk(x̃k, uk) $% 
, (6.10) 
and x̃k+1 = fk(x̃k, ũk). 
Thus in approximation in value space the calculation of the suboptimal sequence {ũ0, . . . , ũN!1} is done by going forward (no backward calculation is needed once the approximate cost-to-go functions J̃k are available). This is similar to the calculation of the optimal sequence {u# 
0, . . . , u # N!1} 
[cf. Eq. (6.6)], and is independent of how the functions J̃k are computed. An alternative (and equivalent) form of the exact DP algorithm (6.4), 
uses the optimal cost-to-go functions J* k indirectly. In particular, it gener-
ates the optimal Q-factors , defined for all pairs (xk, uk) and k by 
Q* k(xk, uk) = gk(xk, uk) + J* 
k+1 
# 
fk(xk, uk) $ 
. (6.11) 
Thus the optimal Q-factors are simply the expressions that are minimized in the right-hand side of the DP equation (6.4).
130 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
Note that the optimal cost function J* k can be recovered from the 
optimal Q-factor Q* k by means of the minimization 
J* k (xk) = min 
uk"Uk(xk) Q* 
k(xk, uk). (6.12) 
Moreover, the DP algorithm (6.4) can be written in an essentially equivalent form that involves Q-factors only [cf. Eqs. (6.11)-(6.12)]: 
Q* k(xk, uk) = gk(xk, uk) + min 
uk+1"Uk+1(fk(xk,uk)) Q* 
k+1 
# 
fk(xk, uk), uk+1 
$ 
. 
Exact and approximate forms of this and other related algorithms, including counterparts for stochastic optimal control problems, comprise an important class of RL methods known as Q-learning. 
The expression 
Q̃k(xk, uk) = gk(xk, uk) + J̃k+1 
# 
fk(xk, uk) $ 
, 
which is minimized in approximation in value space [cf. Eq. (6.10)] is known as the (approximate)Q-factor of (xk, uk). Note that the computation of the suboptimal control (6.10) can be done through the Q-factor minimization 
ũk " arg min uk"Uk(x̃k) 
Q̃k(x̃k, uk). 
This suggests the possibility of using approximate o!-line trained Q-factors in place of cost functions in approximation in value space schemes. How-ever, contrary to the cost approximation scheme (6.10) and its multistep counterparts, the performance may be degraded through the errors in the o!-line training of the Q-factors (depending on how the training is done). 
Multistep Lookahead 
The approximation in value space algorithm (6.10) involves a one-step lookahead minimization, since it solves a one-stage DP problem for each k. We may also consider "-step lookahead , which involves the solution of an "-step DP problem, where " is an integer, 1 < " < N ! k, with a terminal cost function approximation J̃k+!. This is similar to the infinite horizon case that we discussed in Chapter 2. As we have noted in that section, multistep lookahead typically provides better performance over one-step lookahead in RL approximation schemes. For example in AlphaZero chess, long multistep lookahead is critical for good on-line performance. On the negative side, the solution of the multistep lookahead optimization problem, instead of the one-step lookahead counterpart of Eq. (6.10), becomes more time consuming.
Sec. 6.3 Approximation in Value Space 131 
Rollout 
Similar to infinite horizon problems, a major issue in the value space approximation (6.10) is the construction of suitable approximate cost-to-go functions J̃k+1. This can be done in many di!erent ways, including some of the principal RL methods. For example, J̃k+1 may be constructed with a sophisticated o!-line training method, as discussed in Section 1.1, in connection with chess and backgammon. Forms of approximate PI method can be applied in particular, possibly with the use of neural networks, once the problem is viewed as an infinite horizon SSP problem. Another possibility is the fitted value iteration method, which is described in Section 4.3 of the book [Ber19a], and Section 4.3.1 of the book [Ber20a]. 
Alternatively, J̃k+1 may be obtained on-line with rollout , whereby the approximate values J̃k+1(xk+1) are obtained when needed by running a heuristic control scheme, called base heuristic, for a suitably large number of steps, starting from xk+1.† The base heuristic need not be a policy. It could be any method, which starting from a state xk+1 generates a sequence controls uk+1, . . . , uN!1, the corresponding sequence of states xk+2, . . . , xN , and the cost of the heuristic starting from xk+1, which we will generically denote by Hk+1(xk+1) in this chapter: 
Hk+1(xk+1) = gk+1(xk+1, uk+1) + · · ·+ gN!1(xN!1, uN!1) + gN (xN ). 
This value of Hk+1(xk+1) is the one used as the approximate cost-to-go J̃k+1(xk+1) in the corresponding approximation in value space scheme (6.10). An important point here is that deterministic problems hold a special attraction for rollout, as they do not require expensive on-line Monte Carlo simulation to calculate the cost function values J̃k+1(xk+1). 
There are also several variants of rollout, involving for example truncation, multistep lookahead, and other possibilities. In particular, truncated rollout combines the use of one-step optimization, simulation of the 
† For deterministic problems we prefer to use the term “base heuristic” rather 
than “base policy” for reasons to be explained later in this chapter, in the context of the notion of sequential consistency (the heuristic may not qualify as a 
legitimate DP policy). In particular, if the base heuristic, when started at state 
xk, generates the sequence {ũk, x̃k+1, ũk+1, x̃k+2, . . . , ũN"1, x̃N}, it is not necessarily true that, when started at state x̃k+1, it will generate the tail portion 
that starts at ũk+1, namely {ũk+1, x̃k+2, . . . , ũN"1, x̃N}, (which would be true if the heuristic were a legitimate policy). More generally, the method used by the 
base heuristic to complete the system’s trajectory starting from some state may 
be very di!erent than the method used to complete the trajectory starting at another state. In any case, if the base heuristic is not a legitimate policy, then 
the use of Hk+1(xk+1) as terminal cost function approximation, yields a type of 
approximation in value space scheme, which can still be interpreted as a Newton step.
132 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 0 x1 ) . . . 
uk x 
k xNk xk+1 
k u ! 
k 
! 
k u !! 
k x 
+1 x !! 
k+1 
x ! 
N 
x !! 
N 
. . . Q-Factors 
-Factors Current State x 
Current State xk 
Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic 
Next Cities Next States 
! x " 
k+1 
Figure 6.4.1 Schematic illustration of rollout with one-step lookahead for a deterministic problem. At state xk, for every pair (xk, uk), uk ! Uk(xk), the base heuristic generates a Q-factor 
Q̃k(xk, uk) = gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ 
, 
and the rollout algorithm selects the control µ̃k(xk) with minimal Q-factor. 
base policy for a certain number of steps m, and then adds an approximate cost J̃k+m+1(xk+m+1) to the cost of the simulation, which depends on the state xk+m+1 obtained at the end of the rollout. Note that if one foregoes the use of a base heuristic (i.e., m = 0), one recovers as a special case the general approximation in value space scheme. Versions of truncated rollout with multistep lookahead minimization are also possible. Other variants of rollout include versions involving multiple heuristics, combinations with other forms of approximation in value space methods, and multistep lookahead, which will be described later in this chapter, starting with the next section. 
6.4 ROLLOUT ALGORITHMS FOR DISCRETE OPTIMIZATION 
In this section, we will develop in more detail the theory of rollout with one-step lookahead minimization for deterministic problems, including the important issue of cost improvement. We will also illustrate several variants of the method, and we will consider questions of e"cient implementation. We will then discuss examples of discrete optimization applications. 
Let us consider a deterministic DP problem with a finite number of controls and a given initial state (so the number of states that can be reached from the initial state is also finite). We first focus on the pure form of rollout that uses one-step lookahead and no terminal cost approximation. Given a state xk at time k, this algorithm considers the tail subproblems that start at every possible next state xk+1, and solves them suboptimally by using some algorithm, referred to as base heuristic.
Sec. 6.4 Rollout Algorithms for Discrete Optimization 133 
Thus when at xk, rollout generates on-line the next states xk+1 that correspond to all uk " Uk(xk), and uses the base heuristic to compute the sequence of states {xk+1, . . . , xN} and controls {uk+1, . . . , uN!1} such that 
xt+1 = ft(xt, ut), t = k, . . . , N ! 1, 
and the corresponding cost 
Hk+1(xk+1) = gk+1(xk+1, uk+1) + · · ·+ gN!1(xN!1, uN!1) + gN (xN ). 
The rollout algorithm then applies the control that minimizes over uk " Uk(xk) the tail cost expression for stages k to N : 
gk(xk, uk) +Hk+1(xk+1). 
Equivalently, and more succinctly, the rollout algorithm applies at state xk the control µ̃k(xk) given by the minimization 
µ̃k(xk) " arg min uk"Uk(xk) 
Q̃k(xk, uk), (6.13) 
where Q̃k(xk, uk) is the approximate Q-factor defined by 
Q̃k(xk, uk) = gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ 
; (6.14) 
see Fig. 6.4.1. The rollout algorithm thus defines a suboptimal policy !̃ = {µ̃0, . . . , µ̃N!1}, referred to as the rollout policy, where for each xk 
and k, µ̃k(xk) is the control produced by the Q-factor minimization (6.13). Note that the rollout algorithm requires running the base heuristic 
for a number of times that is bounded by Nn, where n is an upper bound on the number of control choices available at each state. Thus if n is small relative to N , it requires computation equal to a small multiple of N times the computation time for a single application of the base heuristic. Similarly, if n is bounded by a polynomial in N , the ratio of the rollout algorithm computation time to the base heuristic computation time is a polynomial in N . 
Example 6.4.1 (Traveling Salesman Problem) 
Let us consider the traveling salesman problem of Example 6.2.1, whereby a salesman wants to find a minimum cost tour that visits each of N given cities c = 0, . . . , N ! 1 exactly once and returns to the city he started from. With each pair of distinct cities c, c$, we associate a traversal cost g(c, c$). Note that we assume that we can go directly from every city to every other city. There is no loss of generality in doing so because we can assign a very high cost g(c, c$) to any pair of cities (c, c$) that is precluded from participation in
134 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 0 x1 ) . . . 
uk x 
k xNk xk+1 
k u ! 
k 
! 
k u !! 
k x 
x ! 
k+1 
+1 x !! 
k+1 
x ! 
N 
x !! 
N 
Current State xk 
Initial City Current Partial Tour Next Cities Nearest Neighbor Initial City Current Partial Tour Current Partial Tour 
Current Partial Tour Next Cities Nearest Neighbor 
Nearest Neighbor Heuristic Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic Nearest Neighbor Heuristic 
Complete Tours 
µ Next Partial Tour Next Partial Tours 
Figure 6.4.2 Rollout with the nearest neighbor heuristic for the traveling salesman problem. The initial state x0 consists of a single city. The final state xN is a complete tour of N cities, containing each city exactly once. 
the solution. The problem is to find a visit order that goes through each city exactly once and whose sum of costs is minimum. 
There are many heuristic approaches for solving the traveling salesman problem. For illustration purposes, let us focus on the simple nearest 
neighbor heuristic, which starts with a partial tour, i.e., an ordered collection of distinct cities, and constructs a sequence of partial tours, adding to the each partial tour a new city that does not close a cycle and minimizes the cost of the enlargement. In particular, given a sequence {c0, c1, . . . , ck} consisting of distinct cities, the nearest neighbor heuristic adds a city ck+1 
that minimizes g(ck, ck+1) over all cities ck+1 "= c0, . . . , ck, thereby forming the sequence {c0, c1, . . . , ck, ck+1}. Continuing in this manner, the heuristic eventually forms a sequence of N cities, {c0, c1, . . . , cN"1}, thus yielding a complete tour with cost 
g(c0, c1) + · · ·+ g(cN"2, cN"1) + g(cN"1, c0). (6.15) 
We can formulate the traveling salesman problem as a DP problem as we discussed in Example 6.2.1. We choose a starting city, say c0, as the initial state x0. Each state xk corresponds to a partial tour (c0, c1, . . . , ck) consisting of distinct cities. The states xk+1, next to xk, are sequences of the form (c0, c1, . . . , ck, ck+1) that correspond to adding one more unvisited city ck+1 "= c0, c1, . . . , ck (thus the unvisited cities are the feasible controls at a given partial tour/state). The terminal states xN are the complete tours of the form (c0, c1, . . . , cN"1, c0), and the cost of the corresponding sequence of city choices is the cost of the corresponding complete tour given by Eq. (6.15). Note that the number of states at stage k increases exponentially with k, and so does the computation required to solve the problem by exact DP. 
Let us now use as a base heuristic the nearest neighbor method. The corresponding rollout algorithm operates as follows: After k < N ! 1 iterations, we have a state xk, i.e., a sequence {c0, . . . , ck} consisting of distinct cities. At the next iteration, we add one more city by running the nearest neighbor heuristic starting from each of the sequences of the form {c0, . . . , ck, c} where c "= c0, . . . , ck. We then select as next city ck+1 the city c that yielded the minimum cost tour under the nearest neighbor heuristic;
Sec. 6.4 Rollout Algorithms for Discrete Optimization 135 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCA B AC A BC BD ACB ACD ADB ADCA B AC AD ABC BD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCAB AC AD ABC ABD ACB ACD ADB ADCA AB AC D AB AB ACB ACD ADB ADCAB AC BC ACB ACD ADB ADCA D A AB ACB ACD ADB ADCAB A B ACB ACD ADB ADC 
ABCD ABDC ACBD ACDB ADBC ADCBABCD ABDC ACBD ACDB ADBC ADCBCD BDC BD CDB BC ADCBA AB C ACBD AC B ADBC ADCBCD DC A BD ACDB ADBC ADCBABC DC B DB DBC CB 
s Terminal State t 
Initial State x0 
Matrix of Intercity Travel Costs 
Matrix of Intercity Travel Costs ! 
6 13 4 24 27 Rollout 
Base Heuristic Corrected 
Yields Rollout Policy µ̃ 20Yields Rollout Policy µ̃ 20 
40 23 
T0T1 
Cost 28 Cost 27 Cost 13Cost 28 Cost 27 Cost 13 
) T2 
Cost 28 Cost 27 Cost 13 
) 45 20 40 18 ) 45 20 40 18 
) 45 20 40 18 2 6 
) 45 20 40 18 2 6 
) 45 20 40 18 2 6 22 
Figure 6.4.3 A traveling salesman problem example of rollout with the nearest neighbor base heuristic. At city A, the nearest neighbor heuristic generates the tour ACDBA (labelled T0). At city A, the rollout algorithm compares the tours ABCDA, ACDBA, and ADCBA, finds ABCDA (labelled T1) to have the least cost, and moves to city B. At AB, the rollout algorithm compares the tours ABCDA and ABDCA, finds ABDCA (labelled T2) to have the least cost, and moves to city D. The rollout algorithm then moves to cities C and A (it has no other choice). Note that the algorithm generates three tours/solutions, T0, T1, and T2, of decreasing costs 28, 27, and 13, respectively. The first path T0 is generated by the base heuristic starting from the initial state, while the last tour T2 is generated by rollout. This is suggestive of a general result that we will prove later: the rollout solution is better in terms of cost than the base heuristic solution. In fact the tour T2 generated by rollout is optimal, but this is just a coincidence. 
see Fig. 6.4.2. The overall computation for the rollout solution is bounded by a polynomial in N , and is much smaller than the exact DP computation. Figure 6.4.3 provides an example where the nearest neighbor heuristic and the corresponding rollout algorithm are compared. 
Cost Improvement with Rollout - Sequential Consistency 
The definition of the rollout algorithm leaves open the choice of the base
136 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
heuristic. There are several types of suboptimal solution methods that can be used as base heuristics, such as greedy algorithms, local search, genetic algorithms, and others. 
Intuitively, we expect that the rollout policy’s performance is no worse than the one of the base heuristic: since rollout optimizes over the first control before applying the heuristic, it makes sense to conjecture that it performs better than applying the heuristic without the first control optimization. However, some special conditions must hold in order to guarantee this cost improvement property. We provide two such conditions, sequential consistency and sequential improvement , introduced in the paper by Bertsekas, Tsitsiklis, and Wu [BTW97], and we later show how to modify the algorithm to deal with the case where these conditions are not met. 
Definition 6.4.1: We say that the base heuristic is sequentially consistent if it has the property that when it generates the sequence 
{xk, uk, xk+1, uk+1, . . . , xN} 
starting from state xk, it also generates the sequence 
{xk+1, uk+1, . . . , xN} 
starting from state xk+1. 
In other words, the base heuristic is sequentially consistent if it “stays the course”: when the starting state xk is moved forward to the next state xk+1 of its state trajectory, the heuristic will not deviate from the remainder of the trajectory. 
As an example, the reader may verify that the nearest neighbor heuristic described in the traveling salesman Example 6.4.1 is sequentially consistent. Similar examples include the use of many types of greedy/myopic heuristics (Section 6.4 of the book [Ber17a] provides some additional examples).† Generally most heuristics used in practice satisfy the sequential consistency condition at “most” states xk. However, some heuristics of interest may violate this condition at some states. 
† A subtle but important point relates to how one breaks ties while imple-
menting greedy base heuristics. For sequential consistency, when multiple con-
trols are greedy at a given state, one must break the tie in a consistent way, i.e., by using a fixed rule at each state encountered by the base heuristic. In partic-
ular, randomization among multiple controls, which are ranked as equal by the 
greedy optimization of the heuristic, violates sequential consistency, and can lead to serious degradation of the corresponding rollout algorithm’s performance.
Sec. 6.4 Rollout Algorithms for Discrete Optimization 137 
A sequentially consistent base heuristic can be recognized by the fact that it will apply the same control uk at a state xk, no matter what position xk occupies in a trajectory generated by the base heuristic. Thus a base heuristic is sequentially consistent if and only if it defines a legitimate DP policy. This is the policy that moves from xk to the state xk+1 that lies on the state trajectory {xk, xk+1, . . . , xN} that the base heuristic generates. 
We will now show that the rollout algorithm obtained with a sequentially consistent base heuristic yields no worse cost than the base heuristic. 
Proposition 6.4.1: (Cost Improvement Under Sequential Con-sistency) Consider the rollout policy !̃ = {µ̃0, . . . , µ̃N!1} obtained with a sequentially consistent base heuristic, and let Jk,"̃(xk) denote the cost obtained with !̃ starting from xk at time k. Then 
Jk,"̃(xk) # Hk(xk), for all xk and k, (6.16) 
where Hk(xk) denotes the cost of the base heuristic starting from xk. 
Proof: We prove this inequality by induction. Clearly it holds for k = N , since 
JN,"̃ = HN = gN . 
Assume that it holds for index k+1. For any state xk, let uk be the control applied by the base heuristic at xk. Then we have 
Jk,"̃(xk) = gk # 
xk, µ̃k(xk) $ 
+ Jk+1,"̃ 
( 
fk # 
xk, µ̃k(xk) $ ) 
# gk # 
xk, µ̃k(xk) $ 
+Hk+1 
( 
fk # 
xk, µ̃k(xk) $ ) 
= min uk"Uk(xk) 
" 
gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ % 
# gk # 
xk, uk 
$ 
+Hk+1 
# 
fk(xk, uk) $ 
= Hk(xk), 
(6.17) 
where: 
(a) The first equality is the DP equation for the rollout policy !̃. 
(b) The first inequality holds by the induction hypothesis. 
(c) The second equality holds by the definition of the rollout algorithm. 
(d) The third equality is the DP equation for the policy that corresponds to the base heuristic (this is the step where we need sequential consistency). 
This completes the induction proof of the cost improvement property (6.16). Q.E.D.
138 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
The cost improvement property of Prop. 6.4.1 may also be inferred by first transforming the finite horizon problem to an infinite horizon SSP problem, and then by using the cost improvement property of policy iteration for infinite horizon problems 
Sequential Improvement 
We will next show that the rollout policy has no worse performance than its base heuristic under a condition that is weaker than sequential consistency. Let us recall that the rollout algorithm !̃ = {µ̃0, . . . , µ̃N!1} is defined by the minimization 
µ̃k(xk) " arg min uk"Uk(xk) 
Q̃k(xk, uk), 
where Q̃k(xk, uk) is the approximate Q-factor defined by 
Q̃k(xk, uk) = gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ 
, 
[cf. Eq. (6.14)], and Hk+1 
# 
fk(xk, uk) $ 
denotes the cost of the trajectory of the base heuristic starting from state fk(xk, uk). 
Definition 6.4.2: We say that the base heuristic is sequentially improving if for all xk and k, we have 
min uk"Uk(xk) 
Q̃k(xk, uk) # Hk(xk). (6.18) 
In words, the sequential improvement property (6.18) states that 
Minimal heuristic Q-factor at xk # Heuristic cost at xk. 
Note that when the heuristic is sequentially consistent it is also sequentially improving. This follows from the preceding relation, since for a sequentially consistent heuristic, the heuristic cost at xk is equal to the Q-factor of the control uk that the heuristic applies at xk, 
Q̃k(xk, uk) = gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ 
, 
which is greater or equal to the minimal Q-factor at xk. This implies Eq. (6.18). We will now show that a sequentially improving heuristic yields policy improvement.
Sec. 6.4 Rollout Algorithms for Discrete Optimization 139 
Proposition 6.4.2: (Cost Improvement Under Sequential Im-provement) Consider the rollout policy !̃ = {µ̃0, . . . , µ̃N!1} obtained with a sequentially improving base heuristic, and let Jk,"̃(xk) denote the cost obtained with !̃ starting from xk at time k. Then 
Jk,"̃(xk) # Hk(xk), for all xk and k, 
where Hk(xk) denotes the cost of the base heuristic starting from xk. 
Proof: Follows from the calculation of Eq. (6.17), by replacing the last two steps (which rely on sequential consistency) with Eq. (6.18). Q.E.D. 
Thus the rollout algorithm obtained with a sequentially improving base heuristic, will improve or at least will perform no worse than the base heuristic, from every starting state xk. In fact the algorithm has a monotonic improvement property, whereby it discovers a sequence of improved trajectories . In particular, let us denote the trajectory generated by the base heuristic starting from x0 by 
T0 = (x0, u0, . . . , xN!1, uN!1, xN ), 
and the final trajectory generated by the rollout algorithm starting from x0 by 
TN = (x0, ũ0, x̃1, ũ1, . . . , x̃N!1, ũN!1, x̃N ). 
Consider also the intermediate trajectories generated by the rollout algorithm given by 
Tk = (x0, ũ0, x̃1, ũ1, . . . , x̃k, uk, . . . , xN!1, uN!1, xN ), k = 1, . . . , N ! 1, 
where (x̃k, uk, . . . , xN!1, uN!1, xN ), 
is the trajectory generated by the base heuristic starting from x̃k. Then, by using the sequential improvement condition, it can be proved (see Fig. 6.4.4) that 
Cost of T0 $ · · · $ Cost of Tk $ Cost of Tk+1 $ · · · $ Cost of TN . (6.19) 
Empirically, it has been observed that the cost improvement obtained by rollout with a sequentially improving heuristic is typically considerable and often dramatic. In particular, many case studies, dating to the middle 1990s, indicate consistently good performance of rollout; see the book [Ber20a] for a bibliography. The DP textbook [Ber17a] provides some detailed worked-out examples (Chapter 6, Examples 6.4.2, 6.4.5, 6.4.6, and
140 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
) . . . 
) . . . 
) . . . 
x0 x̃1 1 x̃2 2 x̃k!1 1 x̃k 
1 uk 
k xk+1 
ũ0 0 ũ1 1 ũk!1 
r ũk 
k x̃k+1 
x0 
Base Heuristic Cost Hk(x̃k) Base Heuristic Cost 
) Base Heuristic Cost Hk+1(x̃k+1) 
Monotonicity Property Under Sequential Improvement Monotonicity Property Under Sequential Improvement 
Cost of Tk ! Cost of Tk+1 
Trajectory Tk 
Trajectory Tk+1Optimal Base Rollout Terminal Score Approximation Current 
Figure 6.4.4 Proof of the monotonicity property (6.19). At x̃k, the kth state generated by the rollout algorithm, we compare the “current” trajectory Tk whose cost is the sum of the cost of the current partial trajectory (x0, ũ0, x̃1, ũ1, . . . , x̃k) and the cost Hk(x̃k) of the base heuristic starting from x̃k, and the trajectory Tk+1 whose cost is the sum of the cost of the partial rollout trajectory (x0, ũ0, x̃1, ũ1, . . . , x̃k), and the Q-factor Q̃k(x̃k, ũk) of the base heuristic starting from (x̃k , ũk). The sequential improvement condition guarantees that 
Hk(x̃k) " Q̃k(x̃k, ũk), 
which implies that Cost of Tk " Cost of Tk+1. 
If strict inequality holds, the rollout algorithm will switch from Tk and follow Tk+1; cf. the traveling salesman example of Fig. 6.4.3. 
Exercises 6.11, 6.14, 6.15, 6.16). The price for the performance improvement is extra computation that is typically equal to the computation time of the base heuristic times a factor that is a low order polynomial of N . It is generally hard to quantify the amount of performance improvement, but the computational results obtained from the case studies are consistent with the Newton step interpretations that we discussed in Chapter 3. 
The books [Ber19a] (Section 2.5.1) and [Ber20a] (Section 3.1) show that the sequential improvement condition is satisfied in the context of MPC, and is the underlying reason for the stability properties of the MPC scheme. On the other hand the base heuristic underlying the classical form of the MPC scheme (cf. Section 5.3) is not sequentially consistent. 
Generally, the sequential improvement condition may not hold for a given base heuristic. This is not surprising since any heuristic (no matter how inconsistent or silly) is in principle admissible to use as base heuristic. Here is an example: 
Example 6.4.2 (Sequential Improvement Violation) 
Consider the 2-stage problem shown in Fig. 6.4.5, which involves two states at each of stages 1 and 2, and the controls shown. Suppose that the unique
Sec. 6.4 Rollout Algorithms for Discrete Optimization 141 
x0 ! 
0 x ! 
1 ! 
1 x ! 
2 
0 u ! 
0 ! 
1 u ! 
1 
! 
3 ũ1 
ũ0 
x̃1 x̃2 
Rollout Choice 
Rollout Choice 
u1 
Optimal Trajectory Chosen by Base Heuristic at Optimal Trajectory Chosen by Base Heuristic at x0 
High Cost Transition Chosen by Heuristic at High Cost Transition Chosen by Heuristic at x! 
1 ! Violates Sequential Improvement 2.4.3, 2.4.4 2.4.2 3.3, 
Violates Sequential Improvement 2.4.3, 2.4.4 2.4.2 3.3, 
Figure 6.4.5 A 2-stage problem with states x# 1, x̃1 at stage 1, and states 
x# 2, x̃2 at stage 2. The controls and corresponding transitions are as shown 
in the figure. The rollout choice at the initial state x0 is strictly suboptimal, while the base heuristic choice is optimal. The reason is that the base heuristic is not sequentially improving and makes the suboptimal choice u1 at x# 
1, but makes the di!erent (optimal) choice u# 
1 when run from x0. 
optimal trajectory is (x0, u # 0, x 
# 1, u 
# 1, x 
# 2), and that the base heuristic produces 
this optimal trajectory starting at x0. The rollout algorithm chooses a control at x0 as follows: it runs the base heuristic to construct a trajectory starting from x# 
1 and x̃1, with corresponding costs H1(x # 1) and H1(x̃1). If 
g0(x0, u # 0) +H1(x 
# 1) > g0(x0, ũ0) +H1(x̃1), (6.20) 
the rollout algorithm rejects the optimal control u# 0 in favor of the alternative 
control ũ0. The inequality above will occur if the base heuristic chooses ū1 at x# 1 (there is nothing to prevent this from happening, since the base heuristic 
is arbitrary), and moreover the cost g1(x # 1, ū1) + g2(x̃2), which is equal to 
H1(x # 1) is high enough. Let us also verify that if the inequality (6.20) holds then the heuristic 
is not sequentially improving at x0, i.e., that 
H0(x0) < min & 
g0(x0, u # 0) +H1(x 
# 1), g0(x0, ũ0) +H1(x̃1) 
' 
. 
Indeed, this is true because H0(x0) is the optimal cost 
H0(x0) = g0(x0, u # 0) + g1(x 
# 1, u 
# 1) + g2(x 
# 2), 
and must be smaller than both 
g0(x0, u # 0) +H1(x 
# 1), 
which is the cost of the trajectory (x0, u # 0, x 
# 1, u1, x̃2), and 
g0(x0, ũ0) +H1(x̃1), 
which is the cost of the trajectory (x0, ũ0, x̃1, ũ1, x̃2).
142 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
The preceding example and the monotonicity property (6.19) suggest a simple enhancement to the rollout algorithm, which detects when the sequential improvement condition is violated and takes corrective measures. In this algorithmic variant, called fortified rollout , we maintain the best trajectory obtained so far, and keep following that trajectory up to the point where we discover another trajectory that has improved cost. 
Using Multiple Base Heuristics - Parallel Rollout 
In many problems, several promising heuristics may be available. It is then possible to use all of these heuristics in the rollout framework. The idea is to construct a superheuristic, which selects the best out of the trajectories produced by the entire collection of heuristics. The superheuristic can then be used as the base heuristic for a rollout algorithm.† 
In particular, let us assume that we have m heuristics, and that the "th of these, given a state xk+1, produces a trajectory 
T̃ ! k+1 = {xk+1, ũ! 
k+1, xk+2, . . . , ũ! N!1, x̃ 
! N}, 
and corresponding cost C(T̃ ! k+1). The superheuristic then produces at xk+1 
the trajectory T̃ ! k+1 for which C(T̃ ! 
k+1) is minimum. The rollout algorithm selects at state xk the control uk that minimizes the minimal Q-factor: 
ũk " arg min uk"Uk(xk) 
min !=1,...,m 
Q̃! k(xk, uk), 
where Q̃! 
k(xk, uk) = gk(xk, uk) + C(T̃ ! k+1) 
is the cost of the trajectory (xk, uk, T̃ ! k+1). A similar idea was discussed in 
connection with MPC in Section 5.4, and in the paper [LJM21]. Note that the Q-factors of the di!erent heuristics can be computed independently and in parallel. In view of this fact, the rollout scheme just described is sometimes referred to as parallel rollout. 
An interesting property, which can be readily verified by using the definitions, is that if all the heuristics are sequentially improving, the same is true for the superheuristic, something that is also suggested by Fig. 6.4.4. Indeed, let us write the sequential improvement condition (6.18) for each of the base heuristics 
min uk"Uk(xk) 
Q̃! k(xk, uk) # H! 
k(xk), " = 1, . . . ,m, 
† A related practically interesting possibility is to introduce a partition of the 
state space into subsets, and a collection of multiple heuristics that are specially tailored to the subsets. We may then select the appropriate heuristic to use on 
each subset of the partition. In fact one may use a collection of multiple heuristics 
tailored to each subset of the state space partition, and at each state, select out of all the heuristics that apply, the one that yields minimum cost.
Sec. 6.4 Rollout Algorithms for Discrete Optimization 143 
where Q̃! k(xk, uk) and H! 
k(xk) are Q-factors and heuristic costs that correspond to the "th heuristic. Then by taking minimum over ", we have 
min !=1,...,m 
min uk"Uk(xk) 
Q̃! k(xk, uk) # min 
!=1,...,m H! 
k(xk), 
for all xk and k. By interchanging the order of the minimizations of the left side, we then obtain 
min uk"Uk(xk) 
min !=1,...,m 
Q̃! k(xk, uk) 
* +, -
Superheuristic Q-factor 
# min !=1,...,m 
H! k(xk) 
* +, -
Superheuristic cost 
, 
which is precisely the sequential improvement condition (6.18) for the superheuristic. 
Simplified Rollout Algorithms 
We will now consider a rollout variant, called simplified rollout algorithm, which is motivated by problems where the control constraint set Uk(xk) is either infinite or finite but very large. Then the minimization 
µ̃k(xk) " arg min uk"Uk(xk) 
Q̃k(xk, uk), (6.21) 
[cf. Eqs. (6.13) and (6.14)], may be unwieldy, since the number of Q-factors 
Q̃k(xk, uk) = gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ 
is accordingly infinite or large. To remedy this situation, we may replace Uk(xk) with a smaller finite 
subset Uk(xk): Uk(xk) % Uk(xk). 
The rollout control µ̃k(xk) in this variant is one that attains the minimum of Q̃k(xk, uk) over uk " Uk(xk): 
µ̃k(xk) " arg min uk"Uk(xk) 
Q̃k(xk, uk). (6.22) 
An example is when Uk(xk) results from discretization of an infinite set Uk(xk). Another possibility is when by using some preliminary approximate optimization, we can identify a subset Uk(xk) of promising controls, and to save computation, we restrict attention to this subset. A related possibility is to generate Uk(xk) by some random search method that explores intelligently the set Uk(xk) with the aim to minimize Q̃k(xk, uk) [cf. Eq. (6.21)].
144 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
It turns out that the proof of the cost improvement property of Prop. 6.4.2, 
Jk,"̃(xk) # Hk(xk), for all xk and k, 
goes through if the following modified sequential improvement property holds: 
min uk"Uk(xk) 
Q̃k(xk, uk) # Hk(xk). (6.23) 
This can be seen by verifying that Eq. (6.23) is su"cient to guarantee that the monotone improvement Eq. (6.19) is satisfied. The condition (6.23) is very simple to satisfy if the base heuristic is sequentially consistent, in which case the control uk selected by the base heuristic satisfies 
Q̃k(xk, uk) = Hk(xk). 
In particular, for the property (6.23) to hold, it is su"cient that Uk(xk) contains the base heuristic choice uk. 
The idea of replacing the minimization (6.21) by the simpler minimization (6.22) can be extended. In particular, by working through the preceding argument, it can be seen that any policy 
!̃ = {µ̃0, . . . , µ̃N!1} 
such that µ̃k(xk) satisfies the condition 
Q̃k 
# 
xk, µ̃k(xk) $ 
# Hk(xk), 
for all xk and k, guarantees the modified sequential improvement property (6.23), and hence also the cost improvement property. A prominent example of such an algorithm arises in the multiagent case where u hasm components, u = (u1, . . . , um), and the minimization over U1 
k (xk)&· · ·&Um k (xk) is 
replaced by a sequence of single component minimizations, one-component-at-a-time; cf. Section 3.7. 
The Fortified Rollout Algorithm 
In this section we describe a rollout variant that implicitly enforces the sequential improvement property. This variant, called the fortified rollout algorithm, starts at x0, and generates step-by-step a sequence of states {x0, x1, . . . , xN} and corresponding sequence of controls. Upon reaching state xk we have the trajectory 
P k = {x0, u0, . . . , uk!1, xk} 
that has been constructed by rollout, called permanent trajectory, and we also store a tentative best trajectory 
T k = {x0, u0, . . . , uk!1, xk, uk, xk+1, uk+1, . . . , uN!1, xN}
Sec. 6.4 Rollout Algorithms for Discrete Optimization 145 
x0 ) . . . 
-Factors Current State x 
Current State xk 
k ũk 
k x̃k+1 
+1 xk+1 
k uk 
x̃N 
xN 
uk x 
k xNk xk+1 
Permanent trajectory P k 
x ! 
N 
Nearest Neighbor Heuristic Move to the Right 
Nearest Neighbor Heuristic Move to the Right 
Nearest Neighbor Heuristic Move to the Right 
Tentative Best Trajectory T k 
Min Q-factor choice 
Figure 6.4.6 Schematic illustration of fortified rollout. After k steps, we have constructed the permanent trajectory P k = {x0, u0, . . . , uk"1, xk}, and the tentative best trajectory 
T k = {x0, u0, . . . , uk"1, xk, uk, xk+1, uk+1, . . . , uN"1, xN}, 
the best end-to-end trajectory computed so far. We now run the rollout algorithm at xk, i.e., we find the control ũk that minimizes over uk the sum of gk(xk , uk) plus the heuristic cost from the state xk+1 = fk(xk , uk), and the corresponding trajectory 
T̃k = {x0, u0, . . . , uk"1, xk, ũk, x̃k+1, ũk+1, . . . , ũN"1, x̃N}. 
If the cost of the end-to-end trajectory T̃k is lower than the cost of T k, we add (ũk, x̃k+1) to the permanent trajectory and set the tentative best trajectory to T k+1 = T̃k. Otherwise we add (uk, xk+1) to the permanent trajectory and keep the tentative best trajectory unchanged: T k+1 = T k. 
with corresponding cost 
C(T k) = k!1 
t=0 
gt(xt, ut) + gk(xk, uk) + N!1 ! 
t=k+1 
gt(xt, ut) + gN(xN ). 
The tentative best trajectory T k is the best end-to-end trajectory computed up to stage k of the algorithm. Initially, T 0 is the trajectory generated by the base heuristic starting at the initial state x0. The idea now is to discard the suggestion of the rollout algorithm at every state xk where it produces a trajectory that is inferior to T k, and use T k instead (see Fig. 6.4.6).† 
† The fortified rollout algorithm can actually be viewed as the ordinary rollout algorithm applied to a modified version of the original problem and modified 
base heuristic that has the sequential improvement property. This construction is 
somewhat technical and unintuitive and will not be given; we refer to Bertsekas, Tsitsiklis, and Wu [BTW97], and the DP textbook [Ber17a], Section 6.4.2.
146 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
In particular, upon reaching state xk, we run the rollout algorithm as earlier, i.e., for every uk " Uk(xk) and next state xk+1 = fk(xk, uk), we run the base heuristic from xk+1, and find the control ũk that gives the best trajectory, denoted 
T̃k = {x0, u0, . . . , uk!1, xk, ũk, x̃k+1, ũk+1, . . . , ũN!1, x̃N} 
with corresponding cost 
C(T̃k) = k!1 
t=0 
gt(xt, ut) + gk(xk, ũk) + N!1 ! 
t=k+1 
gt(x̃t, ũt) + gN (x̃N ). 
Whereas the ordinary rollout algorithm would choose control ũk and move to x̃k+1, the fortified algorithm compares C(T k) and C(T̃k), and depending on which of the two is smaller, chooses uk or ũk and moves to xk+1 or to x̃k+1, respectively. In particular, if C(T k) # C(T̃k) the algorithm sets the next state and corresponding tentative best trajectory to 
xk+1 = xk+1, T k+1 = T k, 
and if C(T k) > C(T̃k) it sets the next state and corresponding tentative best trajectory to 
xk+1 = x̃k+1, T k+1 = T̃k. 
In other words the fortified rollout at xk follows the current tentative best trajectory T k unless a lower cost trajectory T̃k is discovered by running the base heuristic from all possible next states xk+1.† It follows that at every state the tentative best trajectory has no larger cost than the initial tentative best trajectory, which is the one produced by the base heuristic starting from x0. Moreover, it can be seen that if the base heuristic is sequentially improving, the rollout algorithm and its fortified version coincide. Experimental evidence suggests that it is often important to use the fortified version if the base heuristic is not known to be sequentially improving. Fortunately, the fortified version involves hardly any additional computational cost. 
As expected, when the base heuristic generates an optimal trajectory, the fortified rollout algorithm will also generate the same trajectory. This is illustrated by the following example. 
† The base heuristic may also be run from a subset of the possible next states 
xk+1, as in the case where a simplified version of rollout is used. Then fortified rollout will still guarantee a cost improvement property.
Sec. 6.4 Rollout Algorithms for Discrete Optimization 147 
Example 6.4.3 
Let us consider the application of the fortified rollout algorithm to the problem of Example 6.4.2 and see how it addresses the issue of cost improvement. The fortified rollout algorithm stores as initial tentative best trajectory the optimal trajectory (x0, u 
# 0, x 
# 1, u 
# 1, x 
# 2) generated by the base heuristic at x0. 
Then, starting at x0, it runs the heuristic from x# 1 and x̃1, and (despite the 
fact that the ordinary rollout algorithm prefers going to x̃1 rather than x# 1) it 
discards the control ũ0 in favor of u# 0, which is dictated by the tentative best 
trajectory. It then sets the tentative best trajectory to (x0, u # 0, x 
# 1, u 
# 1, x 
# 2). 
We finally note that the fortified rollout algorithm can be used in a di!erent setting to restore and maintain the cost improvement property. Suppose in particular that the rollout minimization at each step is performed with approximations. For example the control uk may have multiple independently constrained components, i.e., 
uk = (u1 k, . . . , u 
m k ), Uk(xk) = U1 
k (xk)& · · ·& Um k (xk). 
Then, to take advantage of distributed computation, it may be attractive to decompose the optimization over uk in the rollout algorithm, 
µ̃k(xk) " arg min uk"Uk(xk) 
" 
gk(xk, uk) +Hk+1 
# 
fk(xk, uk) $ % 
, 
into an (approximate) parallel optimization over the components ui k (or 
subgroups of these components). However, as a result of approximate optimization over uk, the cost improvement property may be degraded, even if the sequential improvement assumption holds. In this case by maintaining the tentative best trajectory, starting with the one produced by the base heuristic at the initial condition, we can ensure that the fortified rollout algorithm, even with approximate minimization, will not produce an inferior solution to the one of the base heuristic. 
Model-Free Rollout 
We will now consider a rollout algorithm for discrete deterministic optimization for the case where we do not know the cost function and the constraints of the problem. Instead we have access to a base heuristic, and also a human or software “expert” who can rank any two feasible solutions without assigning numerical values to them. 
We consider the general discrete optimization problem of selecting a control sequence u = (u0, . . . , uN!1) to minimize a function G(u). For simplicity we assume that each component uk is constrained to lie in a given constraint set Uk, but extensions to more general constraint sets are possible. We assume the following: 
(a) A base heuristic with the following property is available: Given any k < N ! 1, and a partial solution (u0, . . . , uk), it generates, for every
148 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
(u0, . . . , uk) 
Base Heuristic Expert Ranks Complete Solutions Base Heuristic Expert Ranks Complete Solutions , . . . , ũN!1) 
, ũk+1, . . . , 
) Sk(u0, . . . , uk, ũk+1), ũk+1 ! Uk+1 
Base Heuristic Expert Ranks Complete Solutions Base Heuristic Expert Ranks Complete Solutions 
Base Heuristic Expert Ranks Complete Solutions 
Current Partial Solution 
Current Partial Solution 
Figure 6.4.7 Schematic illustration of model-free rollout with an expert for minimizing G(u) subject to u ! U0 # · · ·# UN"1. We assume that we do not know G and/or U0, . . . , UN"1. Instead we have a base heuristic, which given a partial solution (u0, . . . , uk), outputs all next controls ũk+1 ! Uk+1, and generates from each a complete solution 
Sk(u0, . . . , uk, ũk+1) = (u0, . . . , uk, ũk+1, . . . , ũN"1). 
Also, we have a human or software “expert” that can rank any two complete solutions without assigning numerical values to them. The control that is selected from Uk+1 by the rollout algorithm is the one whose corresponding complete solution is ranked best by the expert. 
ũk+1 " Uk+1, a complete feasible solution by concatenating the given partial solution (u0, . . . , uk) with a sequence (ũk+1, . . . , ũN!1). This complete feasible solution is denoted 
Sk(u0, . . . , uk, ũk+1) = (u0, . . . , uk, ũk+1, . . . , ũN!1). 
The base heuristic is also used to start the algorithm from an artificial empty solution, by generating all components ũ0 " U0 and a complete feasible solution (ũ0, . . . , ũN!1), starting from each ũ0 " U0. 
(b) An “expert” is available that can compare any two feasible solutions u and u, in the sense that he/she can determine whether 
G(u) > G(u), or G(u) # G(u).
Sec. 6.5 Rollout and Approximation in Value Space with Multistep Lookahead149 
It can be seen that deterministic rollout can be applied to this problem, even though the cost function G is unknown. The reason is that the rollout algorithm uses the cost function only as a means of ranking complete solutions in terms of their cost. Hence, if the ranking of any two solutions can be revealed by the expert, this is all that is needed.† In fact, the constraint sets U0, . . . , UN!1 need not be known either, as long as they can be generated by the base heuristic. Thus, the rollout algorithm can be described as follows (see Fig. 6.4.7): 
We start with an artificial empty solution, and at the typical step, given the partial solution (u0, . . . , uk), k < N!1, we use the base heuristic to generate all possible one-step-extended solutions 
(u0, . . . , uk, ũk+1), ũk+1 " Uk+1, 
and the set of complete solutions 
Sk(u0, . . . , uk, ũk+1), ũk+1 " Uk+1. 
We then use the expert to rank this set of complete solutions. Finally, we select the component uk+1 that is ranked best by the expert, extend the partial solution (u0, . . . , uk) by adding uk+1, and repeat with the new partial solution (u1, . . . , uk, uk+1). 
Except for the (mathematically inconsequential) use of an expert rather than a cost function, the preceding rollout algorithm can be viewed as a special case of the one given earlier. As a result several of the rollout variants that we have discussed so far (rollout with multiple heuristics, simplified rollout, and fortified rollout) can also be easily adapted. For an application of the model-free rollout methodology to the problem of RNA folding, see the paper [LPS21] and the RL book [Ber20a]. 
6.5 ROLLOUT AND APPROXIMATION IN VALUE SPACE WITH MULTISTEP LOOKAHEAD 
We will now consider approximation in value space with multistep lookahead minimization, possibly also involving some form of rollout. Figure 6.5.1 describes the case of pure (nontruncated) form of rollout with twostep lookahead for deterministic problems. In particular, suppose that after k steps we have reached state xk. We then consider the set of all possible two-step-ahead states xk+2, we run the base heuristic starting from each 
† Note that for this to be true, it is important that the problem is deterministic, and that the expert ranks solutions using some underlying (though 
unknown) cost function. In particular, the expert’s rankings should have a tran-
sitivity property: if u is ranked better than u$ and u$ is ranked better than u$$, then u is ranked better than u$$.
150 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 ) . . . ) . . . 
) . . . 
uk x 
k xN 
k xk+1 
k u ! 
k 
x ! 
N 
. . . Q-Factors 
-Factors Current State x 
Current State xk 
Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic 
Nearest Neighbor Heuristic 
! x " 
k+1 
xk+2 
x ! 
k+2 
uk+1 
u ! 
k+1 
PATH PLANNING States at the End of the Lookahead Final States 
PATH PLANNING States at the End of the Lookahead Final States 
PATH PLANNING States at the End of the Lookahead Final States 
x !! 
k+2 
x !!! 
k+2 
u !! 
k+1 
u !!! 
k+1 
0 x1 
Figure 6.5.1 Illustration of multistep rollout with ! = 2 for deterministic problems. We run the base heuristic from each leaf xk+! at the end of the lookahead graph. We then construct an optimal solution for the lookahead minimization problem, where the heuristic cost is used as terminal cost approximation. We thus obtain an optimal !-step control sequence through the lookahead graph, use the first control in the sequence as the rollout control, discard the remaining controls, move to the next state, and repeat. Note that the multistep lookahead minimization may involve approximations aimed at simplifying the associated computations. 
of them, and compute the two-stage cost to get from xk to xk+2, plus the cost of the base heuristic from xk+2. We select the state, say x̃k+2, that is associated with minimum cost, compute the controls ũk and ũk+1 that lead from xk to x̃k+2, choose ũk as the next control and xk+1 = fk(xk, ũk) as the next state, and discard ũk+1. 
The extension of the algorithm to lookahead of more than two steps is straightforward: instead of the two-step-ahead states xk+2, we run the base heuristic starting from all the possible "-step ahead states xk+!, etc. For cases where the "-step lookahead minimization is very time consuming, we may consider variants involving approximations aimed at simplifying the associated computations. 
An important variation is truncated rollout with terminal cost approximation. Here the rollout trajectories are obtained by running the base heuristic from the leaf nodes of the lookahead graph, and they are truncated after a given number of steps, while a terminal cost approximation is added to the heuristic cost to compensate for the resulting error; see Fig. 6.5.2. One possibility that works well for many problems, particularly when the combined lookahead for minimization and base heuristic simulation is long, is to simply set the terminal cost approximation to zero. Alternatively, the terminal cost function approximation can be obtained
Sec. 6.5 Rollout and Approximation in Value Space with Multistep Lookahead151 
Selective Depth Lookahead Tree 
States xk+1 
proximation 
States xk+2 
Truncated Rollout Terminal Cost Approximation Truncated Rollout Terminal Cost Approximation J̃ 
Base Heuristic Truncated Rollout 
Base Heuristic Truncated Rollout 
Current State xk . . .x0 
-Factors Current State x 
Figure 6.5.2 Illustration of truncated rollout with two-step lookahead and a terminal cost approximation J̃ . The base heuristic is used for a limited number of steps and the terminal cost is added to compensate for the remaining steps. 
by problem approximation or by using some sophisticated o!-line training process that may involve an approximation architecture such as a neural network. Generally, the terminal cost approximation is especially important if a large portion of the total cost is incurred upon termination (this is true for example in games). 
Note that the preceding algorithmic scheme can be viewed as multistep approximation in value space, and it can be interpreted as a New-ton step, with suitable starting point that is determined by the truncated rollout with the base heuristic, and the terminal cost approximation. This interpretation is possible once the discrete optimal control problem is reformulated to an equivalent infinite horizon SSP problem. Thus the algorithm inherits the fast convergence property of the Newton step, which we have discussed in the context of infinite horizon problems. 
The architecture of Fig. 6.5.2 contains as a special case the general multistep approximation in value space scheme, where there is no rollout at all; i.e., the leaves of the multistep lookahead tree are evaluated with the function J̃ . Figure 6.5.3 illustrates this special case, where for notational simplicity we have denoted the current state by x0. The illustration involves an acyclic graph with a single root (the current state) and " layers, with the nth layer consisting of the states xn that are reachable from x0 with a feasible sequence of n controls. In particular, there is an arc for every state x1 of the 1st layer that can be reached from x0 with a feasible control, and
152 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
0 Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer ! 
Terminal Cost Approximation State 1 State 2 2-State/2-Control Ex-
Layer n x 
+ 1 (may be th cost of a heuristic) 
Shortest Path 
Shortest Path Move Chosen (Current State)x0 
: Feature-based parametric architecture State J̃(x!) 
) x! 
x ! 
1 
x ! 
2 
x ! 
n 
x ! 
! 
Figure 6.5.3 Illustration of the general !-step approximation in value space scheme with a terminal cost approximation J̃ where x0 denotes the current state. It involves an acyclic graph of ! layers, with layer n, n = 1, . . . , !, consisting of all the states xn that can be reached from x0 with a sequence of n feasible controls. In !-step approximation in value space, we obtain a trajectory {x0, x# 
1, . . . , x # ! } 
that minimizes the shortest distance from x0 to x! plus J̃(x!). We then use the control that corresponds to the first move x0 $ x# 
1. 
similarly an arc for every pair of states (xn, xn+1), of layers n and n + 1, respectively, for which xn+1 can be reached from xn with a feasible control. The cost of each of these arcs is the stage cost of the corresponding statecontrol pair, minimized over all possible controls that correspond to the same pair (xn, xn+1). Mathematically, the cost of the arc (xn, xn+1) is 
ĝn(xn, xn+1) = min {un"Un(xn) | xn+1=fn(xn,un)} 
gn(xn, un). (6.24) 
For the states x! of the last layer there is also a given terminal cost approximation J̃(x!), possibly obtained through o!-line training and/or rollout with a base policy. It can be thought of as the cost of an artificial arc connecting x! to an artificial termination state. 
Once we have computed all the shortest distances D(x!) from x0 to all states x! of the last layer ", we obtain the "-step lookahead control to be applied at the current state x0, by minimizing over x! the sum 
D(x!) + J̃(x!). 
If x# ! is the state that attains the minimum, we generate the corresponding 
trajectory (x0, x# 1, . . . , x 
# ! ), and then use the control that corresponds to
Sec. 6.5 Rollout and Approximation in Value Space with Multistep Lookahead153 
the first move x0 ' x# 1; see Fig. 6.5.3. Note that the shortest path prob-
lems from x0 to all states xn of all the layers n = 1, . . . , " can be solved simultaneously by backward DP (start from layer " and go back towards x0). 
Long Lookahead for Deterministic Problems 
The architecture of Figs. 6.5.2 is similar to the one we discussed in Section 1.1 for AlphaZero and related programs. However, because it is adapted to deterministic problems, it is much simpler to implement and to use. In particular, the truncated rollout portion does not involve expensive Monte Carlo simulation, while the multistep lookahead minimization portion involves a deterministic shortest path problem, which is much easier to solve that its stochastic counterpart. These favorable characteristics can be exploited to facilitate implementations that involve very long lookahead. 
Generally speaking, longer lookahead is desirable because it typically results in improved performance. We will adopt this as a working hypothesis. It is typically true in practice, although it cannot be established analytically in the absence of additional assumptions.† On the other hand, the on-line computational cost of multistep lookahead increases, often exponentially, with the length of lookahead. 
We conclude that we should aim to use a lookahead that is as long as is allowed by the on-line computational budget (the amount of time that is available for calculating a control to apply at the current state). This leads to the question of how to increase the length of multistep lookahead within our on-line computational budget. One way to do this, which we have already discussed, is the use of truncated rollout, which explores forward through a deterministic base policy at far less computational cost than lookahead minimization of equal length. Another possibility is to speed up the lookahead minimization calculation, thereby allowing a larger number " of computational stages. In what follows, we will explore two ways by which this can be done: iterative deepening of the shortest path computation, and pruning of the lookahead minimization graph. 
Iterative Deepening Using Forward Dynamic Programming 
As noted earlier, the shortest path problems from x0 to x! in Fig. 6.5.3 can be solved simultaneously by the familiar backward DP that starts from layer " and goes towards x0. An important alternative for solving these problems is the forward DP algorithm. This is the same as the backwards 
† Indeed, there are examples where as the size ! of the lookahead becomes 
longer, the performance of the multistep lookahead policy deteriorates (see [Ber17a], 
Section 6.1.2, or [Ber19a], Section 2.2.1). However, these examples are isolated and artificial. They are not representative of practical experience.
154 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 Layer 1 Layer 2 Layer 
0 Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer ! 
0 x1 
x2 
2 x! 
2 x! 
x J̃(x!)Terminal Cost Approximation State 1 State 2 2-State/2-Control Ex-
Multistep Lookahead xn 
n xn+1 
Layer n x 
Layer n+ 1 
+ 1 (may be the cost of a heuristic) 
+1 xn x ! n 
-Step Lookahead xn+1 
(Current State) 
Dn(xn): Shortest distance from ): Shortest distance from x0 to state xn 
of layer n 
Figure 6.5.4 Illustration of the forward DP algorithm for computing the shortest distances from the current state x0 to all the states xn of the layers n = 1, . . . , !. The shortest distance Dn+1(xn+1) to a state xn+1 of layer n is obtained by minimizing over all predecessor states xn the sum 
ĝn(xn, xn+1) +Dn(xn). 
DP algorithm with the direction of the arcs reversed (start from x0 and go towards layer "). In particular, the shortest distances Dn+1(xn+1) to layer n + 1 states are obtained from the shortest distances Dn(xn) to layer n states through the equation 
Dn+1(xn+1) = min xn 
" 
ĝn(xn, xn+1) +Dn(xn) % 
, 
which is also illustrated in Fig. 6.5.4. Here ĝn(xn, xn+1) is the cost (or length) of the arc (xn, xn+1); cf. Eq. (6.24). 
In particular, the solution of the "-step lookahead problem is obtained from the shortest path to the state x# 
! of layer " that minimizes D!(x!) + J̃(x!). The idea of iterative deepening is to progressively solve the n-step lookahead problem first for n = 1, then for n = 2, and so on, until our on-line computational budget is exhausted . In addition to fitting perfectly the mechanism of the forward DP algorithm, this scheme has the character of an “anytime” algorithm; i.e., it returns a feasible solution to a lookahead minimization of some depth, even if it is interrupted because the limit of our computational budget has been reached. In practice this is an important advantage, well known from chess programming, which allows us to keep
Sec. 6.5 Rollout and Approximation in Value Space with Multistep Lookahead155 
x0 Layer 1 Layer 2 Layer 
0 Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer ! 
0 x1 
x2 
2 x! 
2 x! 
x J̃(x!)Terminal Cost Approximation State 1 State 2 2-State/2-Control Ex-
Multistep Lookahead xn 
n xn+1 
Layer n x 
Layer n+ 1 
+ 1 (may be the cost of a heuristic) 
or Pruned States or Pruned States 
(Current State) 
Figure 6.5.5 Illustration of iterative deepening with pruning within the context of forward DP. 
on aiming for longer lookahead minimization, within the limit imposed by our computational budget constraint. 
Pruning the Lookahead Minimization Graph - Double Rollout 
A principal di"culty in approximation in value space with "-step lookahead stems from the rapid expansion of the lookahead graph as " increases. The idea of pruning the lookahead minimization graph is simply to delete some of its arcs in order to expedite the shortest path computations from the current state to the states of subsequent layers; see Fig. 6.5.5. One possibility is to combine pruning with iterative deepening by eliminating from the computation states x̂n of layer n such that the n-step lookahead cost 
Dn(x̂n) + J̃(x̂n) 
is “far from the minimum” over xn. This in turn prunes automatically some of the states of the next layer n+1. The rationale is that such states are “unlikely’ to be part of the shortest path that we aim to compute. Note that this type of pruning is progressive, i.e., we prune states in layer n before pruning states in layer n+ 1. 
An alternative form of pruning is based on applying rollout to the solution of the "-step lookahead minimization; after all, this is also a discrete optimization problem that can be addressed by any suboptimal method, including rollout. Thus we may use a second base heuristic to generate a
156 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 Layer 1 Layer 2 Layer 
0 Layer 1 Layer 2 Layer 
Layer 1 Layer 2 Layer ! 
0 x1 
2 x! 
2 x! 
x J̃(x!)Terminal Cost Approximation State 1 State 2 2-State/2-Control Ex-+ 1 (may be the cost of a heuristic) 
Layer !̄!̄ x!̄ 
Base Policy !̄-Step Lookahead 
Pruned States Rollout 
(Current State) 
Pruned States (with one-step lookahead) Rollout 
Figure 6.5.6 Illustration of the double rollout algorithm. We use a shorter !̄-step lookahead rollout where 
1 ! !̄ < !, 
and run a base heuristic from all the states x!̄ up to stage ! to evaluate x!̄. The state x! 
!̄ that gives the best result is thus obtained, the corresponding shortest path 
trajectory from x0 to x! !̄ is computed, and the first control along that trajectory 
is applied at x0. 
promising trajectory through the !-step lookahead tree by using a shorter !̄-step lookahead rollout where 1 ! !̄ < !. After we solve the !̄-step lookahead minimization problem, by backward or forward DP, we evaluate each of the states x!̄ of layer !̄ by running a base heuristic up to stage !; see Fig. 6.5.6. This “double rollout” algorithm requires a number of heuristic applications that grows linearly rather than exponentially with (!" !̄), the number of rollout stages. In particular, at each stage, the number of heuristic applications of the !-step rollout and of the “double rollout” algorithm will be bounded by n! and by nm+1 ·(!" !̄), respectively, where m is a bound on the number of control choices at each state. Note that the base heuristic that is used for the !-step lookahead problem need not be related to any rollout that is part of the calculation of J̃ . 
The double rollout method admits several variations. These include a fortified version, which guards against lack of sequential improvement, and the possibility that the rollout algorithm gets sidetracked along an inferior trajectory. The fortified algorithm maintains a tentative best trajectory, from which it will not deviate until the rollout algorithm generates a less costly trajectory, similar to the one-step lookahead case.
Sec. 6.5 Rollout and Approximation in Value Space with Multistep Lookahead157 
Subgraph S 
Layer 1 Layer 2 Layer ! 
x ! 
Expansion 
S x! minimizes D(x) +H(x) over ) over the leaf nodes x ! S 
x0 Layer 1 Layer 2 Layer(Current State) 
Figure 6.5.7 Illustration of the !-step lookahead minimization problem and its suboptimal solution with the IMR algorithm. The algorithm maintains a connected acyclic subgraph S as shown. At each iteration it expands S by selecting a leaf node of S and by adding its neighbor nodes to S (if not already in S). The leaf node, denoted x#, is the one that minimizes over all leaf nodes x of S the sum of the shortest distance D(x) from x0 to x and a “heuristic cost” H(x). 
Incremental Multistep Rollout 
We will now consider a more flexible form of the double rollout scheme, which we call incremental multistep rollout (IMR). It applies a base heuristic and a forward DP computation to a sequence of subgraphs of a multistep lookahead graph, with the size of the subgraphs expanding iteratively. 
The di!erence from double rollout is the following: in incremental rollout a connected subgraph of multiple paths is iteratively extended starting from the current state going towards the end of the lookahead horizon, instead of extending a single path as in double rollout. This is similar to what is done in Monte Carlo Tree Search (MCTS, to be discussed later), which is also designed to solve approximately general multistep lookahead minimization problems (including stochastic ones), and involves iterative expansion of an acyclic lookahead graph to new nodes, as well as backtracking to previously encountered nodes. However, incremental rollout seems to be more appropriate than MCTS for deterministic problems, where there are no random variables in the problem’s model and therefore Monte Carlo simulation does not make sense. 
The IMR algorithm starts with and maintains a connected acyclic subgraph S of the given multistep lookahead graph G, which contains x0. At each iteration it expands S by selecting a leaf node of S and by adding its neighbor nodes to S (if not already in S); see Fig. 6.5.7. The leaf node, denoted x#, is the one that minimizes (over all leaf nodes x of S) the sum 
D(x) +H(x), 
where
158 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
D(x) is the shortest distance from x0 to the leaf node x using only arcs that belong to S. This can be computed by forward DP. 
H(x) is a “heuristic cost” corresponding to x. This is defined as the sum of three terms: 
(a) The cost of the base heuristic starting from node x and ending at one of the states x! in the last layer ". 
(b) The terminal cost approximation J̃(x!), where x! is the state obtained via the base heuristic as in (a) above. 
(c) An additional penalty P (x) that depends on the layer to which x belongs. As an example, we will assume here that 
P (x) = # · (the layer index of x), 
where # is a positive parameter. Thus P (x) adds a cost of # for each extra arc to reach x from x0, and penalizes nodes x that lie in more distant layers from the root x0. It thus encourages the algorithm to “backtrack” and select nodes x# that lie in layers closer to x0. 
The role of the parameter # is noteworthy and a!ects significantly the nature of the algorithm. When # = 0, the initial graph S consists of the single state x0, and the base heuristic is sequentially improving, it can be seen that IMR performs exactly like the rollout algorithm for solving the "-step lookahead minimization problem. On the other hand when # is large enough, the algorithm operates like the forward DP algorithm. The reason is that a very large value of # forces the algorithm to expand all nodes of a given layer before proceeding to the next layer. 
Generally, as # increases, the algorithm tends to backtrack more often, and to generate more paths through the graph, thereby visiting more nodes and increasing the number of applications of the base heuristic. Thus # may be viewed as an exploration parameter ; when # is large the algorithm tends to explore more paths thereby improving the quality of the multistep lookahead minimization, at the expense of greater computational e!ort. In the absence of additional problem-specific information, favorable values of # should be obtained through experimentation. One may also consider alternative and more adaptive schemes; for example with a # that depends on x0, and is adjusted in the course of the computation. 
6.6 CONSTRAINED FORMS OF ROLLOUT ALGORITHMS 
In this section we will discuss constrained deterministic DP problems, including challenging combinatorial optimization and integer programming problems. We introduce a rollout algorithm, which relies on a base heuristic and applies to problems with general trajectory constraints. Under suitable
Sec. 6.6 Constrained Forms of Rollout Algorithms 159 
assumptions, we will show that if the base heuristic produces a feasible solution, the rollout algorithm has a cost improvement property: it produces a feasible solution, whose cost is no worse than the base heuristic’s cost. 
Before going into formal descriptions of the constrained DP problem formulation and the corresponding algorithms, it is worth to revisit the broad outline of the rollout algorithm for deterministic DP: 
(a) It constructs a sequence {T0, T1, . . . , TN} of complete system trajectories with monotonically nonincreasing cost (assuming a sequential improvement condition). 
(b) The initial trajectory T0 is the one generated by the base heuristic starting from x0, and the final trajectory TN is the one generated by the rollout algorithm. 
(c) For each k, the trajectories Tk, Tk+1, . . . , TN share the same initial portion (x0, ũ0, . . . , ũk!1, x̃k). 
(d) For each k, the base heuristic is used to generate a number of candidate trajectories, all of which share the initial portion with Tk, up to state x̃k. These candidate trajectories correspond to the controls uk " Uk(xk). (In the case of fortified rollout, these trajectories include the current “tentative best” trajectory.) 
(e) For each k, the next trajectory Tk+1 is the candidate trajectory that is best in terms of total cost. 
In our constrained DP formulation, to be described shortly, we introduce a trajectory constraint T " C, where C is some subset of admissible trajectories. A consequence of this is that some of the candidate trajectories in (d) above, may be infeasible. Our modification to deal with this situation is simple: we discard all the candidate trajectories that violate the constraint, and we choose Tk+1 to be the best of the remaining candidate trajectories, the ones that are feasible. 
Of course, for this modification to be viable, we have to guarantee that at least one of the candidate trajectories will satisfy the constraint for every k. For this we will rely on a sequential improvement condition that we will introduce shortly. For the case where this condition does not hold, we will introduce a fortified version of the algorithm, which requires only that the base heuristic generates a feasible trajectory T0 starting from the initial condition x0. Thus to apply reliably the constrained rollout algorithm, we only need to know a single feasible solution, i.e., a trajectory T0 that starts at x0 and satisfies the constraint T0 " C. 
Constrained Problem Formulation 
We assume that the state xk takes values in some (possibly infinite) set and the control uk takes values in some finite set. The finiteness of the control space is only needed for implementation purposes of the rollout algorithms
160 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
to be described shortly; simplified versions of the algorithm do not require the finiteness condition. A sequence of the form 
T = (x0, u0, x1, u1, . . . , uN!1, xN ), (6.25) 
where xk+1 = fk(xk, uk), k = 0, 1, . . . , N ! 1, (6.26) 
is referred to as a complete trajectory. Our problem is stated succinctly as 
min T"C 
G(T ), (6.27) 
where G is some cost function and C is the constraint set. Note that G need not have the additive form 
G(T ) = gN (xN ) + N!1! 
k=0 
gk(xk, uk), (6.28) 
which we have assumed so far. Thus, except for the finiteness of the control space, which is needed for implementation of rollout, this is a very general optimization problem. In fact, later we will simplify the problem further by eliminating the state transition structure of Eq. (6.26).† 
Trajectory constraints can arise in a number of ways. A relatively simple example is the standard problem formulation for deterministic DP: an additive cost of the form (6.28), where the controls satisfy the timeuncoupled constraints uk " Uk(xk) [so here C is the set of trajectories that are generated by the system equation with controls satisfying uk " Uk(xk)]. In a more complicated constrained DP problem, there may be constraints that couple the controls of di!erent stages such as 
gmN (xN ) + N!1 ! 
k=0 
gmk (xk, uk) # bm, m = 1, . . . ,M, (6.29) 
where gmk and bm are given functions and scalars, respectively. An example where di"cult trajectory constraints arise is when the control contains some discrete components, which once chosen must remain fixed for multiple time periods. 
Here is another discrete optimization example involving the traveling salesman problem. 
† Actually, similar to our discussion on model-free rollout in Section 6.4, 
it is not essential that we know the explicit form of the cost function G and 
the constraint set C. For our constrained rollout algorithms, it is su"cient to have access to a human or software expert that can determine whether a given 
trajectory T is feasible, i.e., satisfies the constraint T # C, and also to be able to 
compare any two feasible trajectories T1 and T2, based on some internal process that is unknown to us, without assigning numerical values to them.
Sec. 6.6 Constrained Forms of Rollout Algorithms 161 
s Terminal State t 
Matrix of Intercity Travel Costs 
Matrix of Intercity Travel Costs ! 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCA B AC A BC BD ACB ACD ADB ADCA B AC AD ABC BD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCAB AC AD ABC ABD ACB ACD ADB ADCA AB AC D AB AB ACB ACD ADB ADCAB AC BC ACB ACD ADB ADCA D A AB ACB ACD ADB ADCAB A B ACB ACD ADB ADC 
ABCD ABDC ACBD ACDB ADBC ADCBABCD ABDC ACBD ACDB ADBC ADCBCD BDC BD CDB BC ADCBA AB C ACBD AC B ADBC ADCBCD DC A BD ACDB ADBC ADCBABC DC B DB DBC CB 
Initial State x0 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
Capacity=1 Optimal Solution 20 15 
Capacity=1 Optimal Solution 20 15 
Safety Costs of Complete Tours ABCDA Safety Costs of Complete Tours ABCDA 
Constraint: Tour Safety 
Constraint: Tour Safety ! 10 
Figure 6.6.1 An example of a constrained traveling salesman problem; cf. Ex-ample 6.6.1. We want to find a minimum cost tour that has safety cost less or equal to 10. The safety costs of the six possible tours are given in the table on the right. The (unconstrained) minimum cost tour, ABDCA, does not satisfy the safety constraint. The optimal constrained tour is ABCDA. 
Example 6.6.1 (A Constrained Form of the Traveling Salesman Problem) 
Let us consider a constrained version of the traveling salesman problem of Example 6.2.1. We want to find a minimum travel cost tour that additionally satisfies a safety constraint that the “safety cost” of the tour should be less than a certain threshold; see Fig. 6.6.1. This constraint need not have the additive structure of Eq. (6.29). We are simply given a safety cost for each tour (see the table at the bottom right), which is calculated in a way that is of no further concern to us. In this example, for a tour to be admissible, its safety cost must be less than or equal to 10. Note that the (unconstrained) minimum cost tour, ABDCA, does not satisfy the safety constraint. 
Transforming Constrained DP Problems to Unconstrained Problems 
Generally, a constrained DP problem can be transformed to an uncon-
162 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
strained DP problem, at the expense of a complicated reformulation of the state and the system equation. The idea is to redefine the state at stage k to be the partial trajectory 
yk = (x0, u0, x1, . . . , uk!1, xk), 
which evolves according to a redefined system equation: 
yk+1 = # 
yk, uk, fk(xk, uk) $ 
. 
The problem then becomes to find a control sequence that minimizes the terminal cost G(yN ) subject to the constraint yN " C. This is a problem to which the standard form of DP applies: 
J* k (yk) = min 
uk"Uk(yk) J* k+1 
# 
yk, uk, fk(xk, uk) $ 
, k = 0, . . . , N ! 1, 
where J* N (yN ) = G(yN ), 
and for k = 0, . . . , N ! 1, the constraint set Uk(yk) is the subset of controls for which it is possible to attain feasibility. Thus Uk(yk) is the set of uk such that there exist uk+1, . . . , uN!1 and corresponding xk+1, . . . , xN , which together with yk, satisfy 
(yk, uk, xk+1, uk+1, . . . , xN!1, uN!1, xN ) " C. 
The reformulation to an unconstrained problem just described is typically impractical, because the associated computation can be overwhelming. However, it provides guidance for structuring a constrained rollout algorithm, which we describe next. Moreover, it allows the interpretation of this constrained rollout algorithm in terms of the Newton step, which is the central theme of this monograph. 
Using a Base Heuristic for Constrained Rollout 
We will now describe formally the constrained rollout algorithm. We assume the availability of a base heuristic, which for any given partial trajectory 
yk = (x0, u0, x1, . . . , uk!1, xk), 
can produce a (complementary) partial trajectory 
R(yk) = (xk, uk, xk+1, uk+1, . . . , uN!1, xN ), 
that starts at xk and satisfies the system equation 
xt+1 = ft(xt, ut), t = k, . . . , N ! 1.
Sec. 6.6 Constrained Forms of Rollout Algorithms 163 
) . . . 
) . . . 
) . . . 
) . . . 
) . . . 
x0 x̃1 1 x̃2 2 x̃k!1 1 x̃k 
1 uk 
k xk+1 
ũ0 0 ũ1 1 ũk!1 
k uk+1 
xk+2 +2 xN!1 1 xNỹk 
k yk+1 
+1 uN!1 
10 11 12 R(yk+1) 
) Tk(ỹk, uk) = ! 
ỹk, uk, R(yk+1) " 
! C 
˜ ỹ0 = x̃0 = x0 
Figure 6.6.2 The trajectory generation mechanism of the rollout algorithm. At stage k, and given the current partial trajectory 
ỹk = (x̃0, ũ0, x̃1, . . . , ũk"1, x̃k), 
which starts at x̃0 and ends at x̃k, we consider all possible next states xk+1 = fk(x̃k, uk), run the base heuristic starting at yk+1 = (ỹk , uk, xk+1), and form the complete trajectory Tk(ỹk , uk). Then the rollout algorithm: 
(a) Finds ũk, the control that minimizes the cost G # 
Tk(ỹk , uk) $ 
over all uk for 
which the complete trajectory Tk(ỹk, uk) is feasible. 
(b) Extends ỹk by # 
ũk, fk(x̃k, ũk) $ 
to form ỹk+1. 
Thus, given yk and any control uk, we can use the base heuristic to obtain a complete trajectory as follows: 
(a) Generate the next state xk+1 = fk(xk, uk). 
(b) Extend yk to obtain the partial trajectory 
yk+1 = # 
yk, uk, fk(xk, uk) $ 
. 
(c) Run the base heuristic from yk+1 to obtain the partial trajectory R(yk+1). 
(d) Join the two partial trajectories yk+1 and R(yk+1) to obtain the complete trajectory 
# 
yk, uk, R(yk+1) $ 
, which is denoted by Tk(yk, uk): 
Tk(yk, uk) = # 
yk, uk, R(yk+1) $ 
. (6.30) 
This process is illustrated in Fig. 6.6.2. Note that the partial trajectory R(yk+1) produced by the base heuristic depends on the entire partial trajectory yk+1, not just the state xk+1. 
A complete trajectory Tk(yk, uk) of the form (6.30) is generally feasible for only the subset Uk(yk) of controls uk that maintain feasibility: 
Uk(yk) = & 
uk | Tk(yk, uk) " C ' 
. (6.31)
164 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
Our rollout algorithm starts from a given initial state ỹ0 = x̃0, and generates successive partial trajectories ỹ1, . . . , ỹN , of the form 
ỹk+1 = # 
ỹk, ũk, fk(x̃k, ũk) $ 
, k = 0, . . . , N ! 1, (6.32) 
where x̃k is the last state component of ỹk, and ũk is a control that minimizes the heuristic cost G 
# 
Tk(ỹk, uk) $ 
over all uk for which Tk(ỹk, uk) is feasible. Thus at stage k, the algorithm forms the set Uk(ỹk) [cf. Eq. (6.31)] and selects from Uk(ỹk) a control ũk that minimizes the cost of the complete trajectory Tk(ỹk, uk): 
ũk " arg min uk"Uk(ỹk) 
G # 
Tk(ỹk, uk) $ 
; (6.33) 
see Fig. 6.6.2. The objective is to produce a feasible final complete trajectory ỹN , which has a cost G(ỹN ) that is no larger than the cost of R(ỹ0) produced by the base heuristic starting from ỹ0, i.e., 
G(ỹN ) # G # 
R(ỹ0) $ 
. 
Note that Tk(ỹk, uk) is not guaranteed to be feasible for any given uk (i.e., may not belong to C), but we will assume that the constraint set Uk(ỹk) of problem (6.33) is nonempty, so that our rollout algorithm is welldefined. We will later modify our algorithm so that it is well-defined under the weaker assumption that just the complete trajectory generated by the base heuristic starting from the initial state ỹ0 is feasible, i.e., R(ỹ0) " C. 
Constrained Rollout Algorithm 
The algorithm starts at stage 0 and sequentially proceeds to the last stage. At the typical stage k, it has constructed a partial trajectory 
ỹk = (x̃0, ũ0, x̃1, . . . , ũk!1, x̃k) (6.34) 
that starts at the given initial state ỹ0 = x̃0, and is such that 
x̃t+1 = ft(x̃t, ũt), t = 0, 1, . . . , k ! 1. 
The algorithm then forms the set of controls 
Uk(ỹk) = & 
uk | Tk(ỹk, uk) " C '
Sec. 6.6 Constrained Forms of Rollout Algorithms 165 
that is consistent with feasibility [cf. Eq. (6.31)], and chooses a control ũk " Uk(ỹk) according to the minimization 
ũk " arg min uk"Uk(ỹk) 
G # 
Tk(ỹk, uk) $ 
, (6.35) 
[cf. Eq. (6.33)], where 
Tk(ỹk, uk) = ( 
ỹk, uk, R # 
ỹk, uk, fk(x̃k, uk) $ ) 
; 
[cf. Eq. (6.30)]. Finally, the algorithm sets 
x̃k+1 = fk(x̃k, ũk), ỹk+1 = (ỹk, ũk, x̃k+1), 
[cf. Eq. (6.32)], thus obtaining the partial trajectory ỹk+1 to start the next stage. 
It can be seen that our constrained rollout algorithm is not much more complicated or computationally demanding than its unconstrained version where the constraint T " C is not present (as long as checking feasibility of a complete trajectory T is not computationally demanding). Note, however, that our algorithm makes essential use of the deterministic character of the problem, and does not admit a straightforward extension to stochastic problems, since checking feasibility of a complete trajectory is typically di"cult in the context of these problems. 
The rollout algorithm just described is illustrated in Fig. 6.6.3 for our earlier traveling salesman Example 6.6.1. Here we want to find a minimum travel cost tour that additionally satisfies a safety constraint, namely that the “safety cost” of the tour should be less than a certain threshold. Note that the minimum cost tour, ABDCA, in this example does not satisfy the safety constraint. Moreover, the tour ABCDA obtained by the rollout algorithm has barely smaller cost than the tour ACDBA generated by the base heuristic starting from A. In fact if the travel cost D'A were larger, say 25, the tour produced by constrained rollout would be more costly than the one produced by the base heuristic starting from A. This points to the need for a constrained version of the notion of sequential improvement and for a fortified variant of the algorithm, which we discuss next. 
Sequential Consistency, Sequential Improvement, and the Cost Improvement Property 
We will now introduce sequential consistency and sequential improvement conditions guaranteeing that the control set Uk(ỹk) in the minimization
166 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
s Terminal State t 
Matrix of Intercity Travel Costs 
Matrix of Intercity Travel Costs ! 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCA B AC A BC BD ACB ACD ADB ADCA B AC AD ABC BD ACB ACD ADB ADC 
A AB AC AD ABC ABD ACB ACD ADB ADCAB AC AD ABC ABD ACB ACD ADB ADCA AB AC D AB AB ACB ACD ADB ADCAB AC BC ACB ACD ADB ADCA D A AB ACB ACD ADB ADCAB A B ACB ACD ADB ADC 
ABCD ABDC ACBD ACDB ADBC ADCBABCD ABDC ACBD ACDB ADBC ADCBCD BDC BD CDB BC ADCBA AB C ACBD AC B ADBC ADCBCD DC A BD ACDB ADBC ADCBABC DC B DB DBC CB 
Initial State x0 
Heuristic Partial Tour 
Heuristic Partial Tour 
Heuristic Partial TourHeuristic Partial Tour 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
ABCDA ABDCA ACBDA ACDBA ADBCA ADCBA 
Heuristic Partial Tour from A from AB from AC from AD 
Heuristic Partial Tour from A from AB from AC from ADHeuristic Partial Tour from A from AB from AC from AD 
Capacity=1 Optimal Solution 20 15 
Capacity=1 Optimal Solution 20 15 
Stages Beyond Truncation Rollout Choice 
Stages Beyond Truncation Rollout Choice 
Heuristic from AB 
Safety Costs of Complete Tours ABCDA Safety Costs of Complete Tours ABCDA 
Constraint: Tour Safety 
Constraint: Tour Safety ! 10 
Figure 6.6.3 The constrained traveling salesman problem; cf. Example 6.6.1, and its rollout solution using the base heuristic shown, which completes a partial tour as follows: 
At A it yields ACDBA. At AB it yields ABCDA. At AC it yields ACBDA. At AD it yields ADCBA. 
This base heuristic is not assumed to have any special structure. It is just capable of completing every partial tour without regard to any additional considerations. Thus for example the heuristic generates at A the complete tour ACDBA, and it switches to the tour ACBDA once the salesman moves to AC. 
At city A, the rollout algorithm: 
(a) Considers the partial tours AB, AC, and AD. 
(b) Uses the base heuristic to obtain the corresponding complete tours ABCDA, ACBDA, and ADCBA. 
(c) Discards ADCBA as being infeasible. 
(d) Compares the other two tours, ABCDA and ACBDA, finds ABCDA to have smaller cost, and selects the partial tour AB. 
(e) At AB, it considers the partial tours ABC and ABD. 
(f) It uses the base heuristic to obtain the corresponding complete tours ABCDA and ABDCA, and discards ABDCA as being infeasible. 
(g) It finally selects the complete tour ABCDA.
Sec. 6.6 Constrained Forms of Rollout Algorithms 167 
(6.35) is nonempty, and that the costs of the complete trajectories Tk(ỹk, ũk) are improving with each k in the sense that 
G # 
Tk+1(ỹk+1, ũk+1) $ 
# G # 
Tk(ỹk, ũk) $ 
, k = 0, 1, . . . , N ! 1, 
while at the first step of the algorithm we have 
G # 
T0(ỹ0, ũ0) $ 
# G # 
R(ỹ0) $ 
. 
It will then follow that the cost improvement property 
G(ỹN ) # G # 
R(ỹ0) $ 
holds. 
Definition 6.6.1: We say that the base heuristic is sequentially consistent if whenever it generates a partial trajectory 
(xk, uk, xk+1, uk+1, . . . , uN!1, xN ), 
starting from a partial trajectory yk, it also generates the partial trajectory 
(xk+1, uk+1, xk+2, uk+2, . . . , uN!1, xN ), 
starting from the partial trajectory yk+1 = # 
yk, uk, xk+1 
$ 
. 
As we have noted in the context of unconstrained rollout, greedy heuristics tend to be sequentially consistent. Also any policy [a sequence of feedback control functions µk(yk), k = 0, 1, . . . , N!1] for the DP problem of minimizing the terminal cost G(yN ) subject to the system equation 
yk+1 = # 
yk, uk, fk(xk, uk) $ 
and the feasibility constraint yN " C can be seen to be sequentially consistent. For an example where sequential consistency is violated, consider the base heuristic of the traveling salesman Example 6.6.1. From Fig. 6.6.3, it can be seen that the base heuristic at A generates ACDBA, but from AC it generates ACBDA, thus violating sequential consistency. 
For a given partial trajectory yk, let us denote by yk(R(yk) the complete trajectory obtained by joining yk with the partial trajectory generated by the base heuristic starting from yk. Thus if 
yk = (x0, u0, . . . , uk!1, xk) 
and R(yk) = (xk, uk+1, . . . , uN!1, xN ),
168 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
we have 
yk (R(yk) = (x0, u0, . . . , uk!1, xk, uk+1, . . . , uN!1, xN ). 
Definition 6.6.2: We say that the base heuristic is sequentially improving if for every k = 0, 1, . . . , N ! 1 and partial trajectory yk for which yk (R(yk) " C, the set Uk(yk) is nonempty, and we have 
G # 
yk (R(yk) $ 
$ min uk"Uk(yk) 
G # 
Tk(yk, uk) $ 
. (6.36) 
Note that for a base heuristic that is not sequentially consistent, the condition yk (R(yk) " C does not imply that the set Uk(yk) is nonempty. The reason is that starting from 
# 
yk, uk, fk(xk, uk) $ 
the base heuristic may generate a di!erent trajectory than from yk, even if it applies uk at yk. Thus we need to include nonemptiness of Uk(yk) as a requirement in the preceding definition of sequential improvement (in the fortified version of the algorithm to be discussed shortly, this requirement will be removed). 
On the other hand, if the base heuristic is sequentially consistent, it is also sequentially improving. The reason is that for a sequentially consistent heuristic, yk (R(yk) is equal to one of the trajectories contained in the set 
& 
Tk(yk, uk) | uk " Uk(yk) ' 
. 
Our main result is contained in the following proposition. 
Proposition 6.6.1: (Cost Improvement for Constrained Roll-out) Assume that the base heuristic is sequentially improving and generates a feasible complete trajectory starting from the initial state ỹ0 = x̃0, i.e., R(ỹ0) " C. Then for each k, the set Uk(ỹk) is nonempty, and we have 
G # 
R(ỹ0) $ 
$ G # 
T0(ỹ0, ũ0) $ 
$ G # 
T1(ỹ1, ũ1) $ 
$ · · · 
$ G # 
TN!1(ỹN!1, ũN!1) $ 
= G(ỹN ),
Sec. 6.6 Constrained Forms of Rollout Algorithms 169 
where Tk(ỹk, ũk) = 
# 
ỹk, ũk, R(ỹk+1) $ 
; 
cf. Eq. (6.30). In particular, the final trajectory ỹN generated by the constrained rollout algorithm is feasible and has no larger cost than the trajectory R(ỹ0) generated by the base heuristic starting from the initial state. 
Proof: Consider R(ỹ0), the complete trajectory generated by the base heuristic starting from ỹ0. Since ỹ0 ( R(ỹ0) = R(ỹ0) " C by assumption, it follows from the sequential improvement definition, that the set U0(ỹ0) is nonempty and we have 
G # 
R(ỹ0) $ 
$ G # 
T0(ỹ0, ũ0) $ 
, 
[cf. Eq. (6.36)], while T0(ỹ0, ũ0) " C. The preceding argument can be repeated for the next stage, by replac-
ing ỹ0 with ỹ1, and R(ỹ0) with T0(ỹ0, ũ0). Since ỹ1(R(ỹ1) = T0(ỹ0, ũ0) " C, from the sequential improvement definition, the set U1(ỹ1) is nonempty and we have 
G # 
T0(ỹ0, ũ0) $ 
= G # 
ỹ1 (R(ỹ1) $ 
$ G # 
T1(ỹ1, ũ1) $ 
, 
[cf. Eq. (6.36)], while T1(ỹ1, ũ1) " C. Similarly, the argument can be successively repeated for every k, to verify that Uk(ỹk) is nonempty and that G 
# 
Tk(ỹk, ũk) $ 
$ G # 
Tk+1(ỹk+1, ũk+1) $ 
for all k. Q.E.D. 
Proposition 6.6.1 establishes the fundamental cost improvement property for constrained rollout under the sequential improvement condition. On the other hand we may construct examples where the sequential improvement condition (6.36) is violated and the cost of the solution produced by rollout is larger than the cost of the solution produced by the base heuristic starting from the initial state (cf. the unconstrained rollout Example 6.4.2). 
In the case of the traveling salesman Example 6.6.1, it can be verified that the base heuristic specified in Fig. 6.6.3 is sequentially improving. However, if the travel cost D'A were larger, say 25, then it can be verified that the definition of sequential improvement would be violated at A, and the tour produced by constrained rollout would be more costly than the one produced by the base heuristic starting from A. 
The Fortified Rollout Algorithm and Other Variations 
We will now discuss some variations and extensions of the constrained rollout algorithm. Let us first consider the case where the sequential improvement assumption is not satisfied. Then it may happen that given the
170 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
current partial trajectory ỹk, the set of controls Uk(ỹk) that corresponds to feasible trajectories Tk(ỹk, uk) [cf. Eq. (6.31)] is empty, in which case the rollout algorithm cannot extend the partial trajectory ỹk further. To bypass this di"culty, we introduce a fortified constrained rollout algorithm, patterned after the fortified algorithm given earlier. For validity of this algorithm, we require that the base heuristic generates a feasible complete trajectory R(ỹ0) starting from the initial state ỹ0. 
The fortified constrained rollout algorithm, in addition to the current partial trajectory 
ỹk = (x̃0, ũ0, x̃1, . . . , ũk!1, x̃k), 
maintains a complete trajectory T̂k, called tentative best trajectory, which is feasible (i.e., T̂k " C) and agrees with ỹk up to state x̃k, i.e., T̂k has the form 
T̂k = (x̃0, ũ0, x̃1, . . . , ũk!1, x̃k, uk, xk+1, . . . , uN!1, xN ), (6.37) 
for some uk, xk+1, . . . , uN!1, xN such that 
xk+1 = fk(x̃k, uk), xt+1 = ft(xt, ut), t = k + 1, . . . , N ! 1. 
Initially, T̂0 is the complete trajectory R(ỹ0), generated by the base heuristic starting from ỹ0, which is assumed to be feasible. At stage k, the algorithm forms the subset Ûk(ỹk) of controls uk " Uk(ỹk) such that the corresponding Tk(ỹk, uk) is not only feasible, but also has cost that is no larger than the one of the current tentative best trajectory: 
Ûk(ỹk) = . 
uk " Uk(ỹk) | G # 
Tk(ỹk, uk) $ 
# G(T̂k) / 
. 
There are two cases to consider at state k: 
(1) The set Ûk(ỹk) is nonempty. Then the algorithm forms the partial trajectory ỹk+1 = (ỹk, ũk, x̃k+1), where 
ũk " arg min uk"Ûk(ỹk) 
G # 
Tk(ỹk, uk) $ 
, x̃k+1 = fk(x̃k, ũk), 
and sets Tk(ỹk, ũk) as the new tentative best trajectory, i.e., 
T̂k+1 = Tk(ỹk, ũk). 
(2) The set Ûk(ỹk) is empty. Then, the algorithm forms the partial trajectory ỹk+1 = 
# 
ỹk, ũk, x̃k+1), where 
ũk = uk, x̃k+1 = xk+1,
Sec. 6.6 Constrained Forms of Rollout Algorithms 171 
and uk, xk+1 are the control and state subsequent to x̃k in the current tentative best trajectory T̂k [cf. Eq. (6.37)], and leaves T̂k unchanged, i.e., 
T̂k+1 = T̂k. 
It can be seen that the fortified constrained rollout algorithm will follow the initial complete trajectory T̂0, the one generated by the base heuristic starting from ỹ0, up to a stage k where it will discover a new feasible complete trajectory with smaller cost to replace T̂0 as the tentative best trajectory. Similarly, the new tentative best trajectory T̂k may be subsequently replaced by another feasible trajectory with smaller cost, etc. 
Note that if the base heuristic is sequentially improving, and the fortified rollout algorithm will generate the same complete trajectory as the (nonfortified) rollout algorithm given earlier, with the tentative best trajectory T̂k+1 being equal to the complete trajectory Tk(ỹk, ũk) for all k. The reason is that if the base heuristic is sequentially improving, the controls ũk generated by the nonfortified algorithm belong to the set Ûk(ỹk) [by Prop. 6.6.1, case (1) above will hold]. 
However, it can be verified that even when the base heuristic is not sequentially improving, the fortified rollout algorithm will generate a complete trajectory that is feasible and has cost that is no worse than the cost of the complete trajectory generated by the base heuristic starting from ỹ0. This is because each tentative best trajectory has a cost that is no worse than the one of its predecessor, and the initial tentative best trajectory is just the trajectory generated by the base heuristic starting from the initial condition ỹ0. 
Tree-Based Rollout Algorithms 
It is possible to improve the performance of the rollout algorithm at the expense of maintaining more than one partial trajectory. In particular, instead of the partial trajectory ỹk of Eq. (6.34), we can maintain a tree of partial trajectories that is rooted at ỹ0. These trajectories need not have equal length, i.e., they need not involve the same number of stages. At each step of the algorithm, we select a single partial trajectory from this tree, and execute the rollout algorithm’s step as if this partial trajectory were the only one. Let this partial trajectory have k stages and denote it by ỹk. Then we extend ỹk similar to our earlier rollout algorithm, with possibly multiple feasible trajectories. There is also a fortified version of this algorithm where a tentative best trajectory is maintained, which is the minimum cost complete trajectory generated thus far. 
The aim of the tree-based algorithm is to obtain improved performance, essentially because it can go back and extend partial trajectories that were generated and temporarily abandoned at previous stages. The net result is a more flexible algorithm that is capable of examining more
172 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
alternative trajectories. Note also that there is considerable freedom to select the number of partial trajectories maintained in the tree. 
We finally mention a drawback of the tree-based algorithm: it is suitable for o!-line computation, but it cannot be applied in an on-line context, where the rollout control selection is made after the current state becomes known as the system evolves in real-time. 
Constrained Multiagent Rollout 
Let us consider a special structure of the control space, where the control uk consists of m components, uk = (u1 
k, . . . , u m k ), each belonging to a cor-
responding set U ! k(xk), " = 1, . . . ,m. Thus the control space at stage k is 
the Cartesian product 
Uk(xk) = U1 k (xk)& · · ·& Um 
k (xk). 
We refer to this as the multiagent case, motivated by the special case where each component u! 
k, " = 1, . . . ,m, is chosen by a separate agent " at stage k. 
Similar to the stochastic unconstrained case of Chapter 3, we can introduce a modified but equivalent problem, involving one-at-a-time agent control selection. In particular, at the generic state xk, we break down the control uk into the sequence of the m controls u1 
k, u 2 k, . . . , u 
m k , and 
between xk and the next state xk+1 = fk(xk, uk), we introduce artificial intermediate “states” 
(xk, u1 k), (xk, u1 
k, u 2 k), . . . , (xk, u1 
k, . . . , u m!1 k ), 
and corresponding transitions. The choice of the last control component um k at “state” (xk, u1 
k, . . . , u m!1 k ) marks the transition at cost gk(xk, uk) to 
the next state xk+1 = fk(xk, uk) according to the system equation. It is evident that this reformulated problem is equivalent to the original, since any control choice that is possible in one problem is also possible in the other problem, with the same cost. 
By working with the reformulated problem, we can consider a rollout algorithm that requires a sequence of m minimizations per stage, one over each of the control components u1 
k, . . . , u m k , with the past controls already 
determined by the rollout algorithm, and the future controls determined by running the base heuristic. Assuming a maximum of n elements in the control component spaces U ! 
k(xk), " = 1, . . . ,m, the computation required for the m single control component minimizations is of order O(nm) per stage. By contrast the standard rollout minimization (6.35) involves the computation and comparison of as many as nm terms G 
# 
Tk(ỹk, uk) $ 
per stage.
Sec. 6.7 Adaptive Control by Rollout with a POMDP Formulation 173 
6.7 ADAPTIVE CONTROL BY ROLLOUT WITH A POMDP FORMULATION 
In this section, we discuss various approaches for the approximate solution of Partially Observed Markovian Decision Problems (POMDP) with a special structure, which is well-suited for adaptive control, as well as other contexts that involve search for a hidden object. It is well known that POMDP are among the most challenging DP problems, and nearly always require the use of approximations for (suboptimal) solution. 
The application and implementation of rollout and approximate PI methods to general finite-state POMDP is described in the author’s RL book [Ber19a] (Section 5.7.3). Here we will focus attention on a special class of POMDP where the state consists of two components: 
(a) A perfectly observed component xk that evolves over time according to a discrete-time equation. 
(b) A component $ which is unobserved but stays constant, and is estimated through the perfect observations of the component xk. 
We view $ as a parameter in the system equation that governs the evolution of xk. Thus we have 
xk+1 = fk(xk, $, uk, wk), (6.38) 
where uk is the control at time k, selected from a set Uk(xk), and wk 
is a random disturbance with given probability distribution that depends on (xk, $, uk). We will assume that $ can take one of m known values $1, . . . , $m: 
$ " {$1, . . . , $m}. 
The a priori probability distribution of $ is given and is updated based on the observed values of the state components xk and the applied controls uk. In particular, we assume that the information vector 
Ik = {x0, . . . , xk, u0, . . . , uk!1} 
is available at time k, and is used to compute the conditional probabilities 
bk,i = P{$ = $i | Ik}, i = 1, . . . ,m. 
These probabilities form a vector 
bk = (bk,1, . . . , bk,m), 
which together with the perfectly observed state xk, form the pair (xk, bk) that is commonly called the belief state of the POMDP at time k. 
Note that according to the classical methodology of POMDP (see e.g., [Ber17a], Chapter 4), the belief component bk+1 is determined by the
174 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
belief state (xk, bk), the control uk, and the observation obtained at time k + 1, i.e., xk+1. Thus bk can be updated according to an equation of the form 
bk+1 = Bk(xk, bk, uk, xk+1), 
where Bk is an appropriate function, which can be viewed as a recursive estimator of $. There are several approaches to implement this estimator (perhaps with some approximation error), including the use of Bayes’ rule and the simulation-based method of particle filtering. 
The preceding mathematical model forms the basis for a classical adaptive control formulation, where each $i represents an unknown set of system parameters, and the computation of the belief probabilities bk,i can be viewed as the outcome of a system identification algorithm. In this context, the problem becomes one of dual control , a combined identification and control problem, whose optimal solution is notoriously di"cult. 
Another interesting context arises in search problems, where $ specifies the locations of one or more objects of interest within a given space. Further related applications include sequential estimation and Bayesian optimization (see the author’s paper [Ber22c]), and puzzles such as Wordle, which will be discussed briefly later in this section. 
The Exact DP Algorithm - Approximation in Value Space 
We will now describe an exact DP algorithm that operates in the space of information vectors Ik. To describe this algorithm, let us denote by Jk(Ik) the optimal cost starting at information vector Ik at time k. Using the equation 
Ik+1 = (Ik, xk+1, uk) = # 
Ik, fk(xk, $, uk, wk), uk 
$ 
, 
the algorithm takes the form 
Jk(Ik) = min uk"Uk(xk) 
E#,wk 
. 
gk(xk, $, uk, wk)+ 
Jk+1 
# 
Ik, fk(xk, $, uk, wk), uk 
$ 
| Ik, uk 
/ 
, 
(6.39) for k = 0, . . . , N ! 1, with JN (IN ) = gN (xN ); see e.g., the DP textbook [Ber17a], Section 4.1. 
By using the law of iterated expectations, 
E#,wk {· | Ik, uk} = E# 
& 
Ewk {· | Ik, $, uk} | Ik, uk 
' 
, 
we can rewrite this DP algorithm as 
Jk(Ik) = min uk"Uk(xk) 
m ! 
i=1 
bk,iEwk 
. 
gk(xk, $i, uk, wk)+ 
Jk+1 
# 
Ik, fk(xk, $i, uk, wk), uk 
$ 
| Ik, $i, uk 
/ 
. 
(6.40)
Sec. 6.7 Adaptive Control by Rollout with a POMDP Formulation 175 
The summation over i above represents the expected value of $ conditioned on Ik and uk. 
The algorithm (6.40) is typically very hard to implement, because of the dependence of Jk+1 on the entire information vector Ik+1, which expands in size according to 
Ik+1 = (Ik, xk+1, uk). 
To address this implementation di"culty, we may use approximation in value space, based on replacing Jk+1 in the DP algorithm (6.39) with some function that can be obtained (either o!-line or on-line) with a tractable computation. 
One approximation possibility is based on the use of the optimal cost function corresponding to each parameter value $i, 
Ĵ i k+1(xk+1), i = 1, . . . ,m. (6.41) 
Here, Ĵ i k+1(xk+1) is the optimal cost that would be obtained starting from 
state xk+1 under the assumption that $ = $i; this corresponds to a perfect state information problem. Then an approximation in value space scheme with one-step lookahead minimization is given by 
ũk " arg min uk"Uk(xk) 
m ! 
i=1 
bk,iEwk 
. 
gk(xk, $i, uk, wk)+ 
Ĵ i k+1 
# 
fk(xk, $i, uk, wk) $ 
| xk, $i, uk 
/ 
. 
(6.42) In particular, instead of the optimal control, which minimizes the optimal Q-factor of (Ik, uk) appearing in the right side of Eq. (6.39), we apply control ũk that minimizes the expected value over $ of the optimal Q-factors that correspond to fixed values of $. 
A simpler version of this approach is to use the same function Ĵ i k+1 for 
every i. However, the dependence on imay be useful in some contexts where di!erences in the value of i may have a radical e!ect on the qualitative character of the system equation. 
Generally, the optimal costs Ĵ i k+1(xk+1) that correspond to the dif-
ferent parameter values $i [cf. Eq. (6.41)] may be hard to compute, despite their perfect state information structure.† An alternative possibility is to use o!-line trained feature-based or neural network-based approximations to Ĵ i 
k+1(xk+1). 
† In favorable special cases, such as linear quadratic problems, the optimal 
costs Ĵ i k+1(xk+1) may be easily calculated in closed form. Still, however, even in 
such cases the calculation of the belief probabilities bk,i may not be simple, and may require the use of a system identification algorithm.
176 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
In the case where the horizon is infinite, it is reasonable to expect that the estimate of the parameter $ improves over time, and that with a suitable estimation scheme, it converges asymptotically to the correct value of $, call it $#, i.e., 
lim k$% 
bk,i = 
0 
1 if $i = $#, 0 if $i )= $#. 
Then it can be seen that the generated one-step lookahead controls ũk are asymptotically obtained from the Bellman equation that corresponds to the correct parameter $#, and are typically optimal in some asymptotic sense. Schemes of this type have been discussed in the adaptive control literature since the 70s; see e.g., Mandl [Man74], Doshi and Shreve [DoS80], Kumar and Lin [KuL82], Kumar [Kum85]. Moreover, some of the pitfalls of performing parameter identification while simultaneously applying adaptive control have been described by Borkar and Varaiya [BoV79], and by Kumar [Kum83]; see [Ber17a], Section 6.8 for a related discussion. 
Rollout 
Another possibility is to use the costs of given policies !i in place of the optimal costs Ĵ i 
k+1(xk+1). In this case the one-step lookahead scheme (6.42) takes the form 
ũk " arg min uk"Uk(xk) 
m! 
i=1 
bk,iEwk 
. 
gk(xk, $i, uk, wk)+ 
Ĵ i k+1,"i 
# 
fk(xk, $i, uk, wk) $ 
| xk, $i, uk 
/ 
, 
(6.43) and has the character of a rollout algorithm, with !i = {µi 
0, . . . , µ i N!1}, 
i = 1, . . . ,m, being known base policies, with components µi k that depend 
only on xk. Here, the term 
Ĵ i k+1,"i 
# 
fk(xk, $i, uk, wk) $ 
in Eq. (6.43) is the cost of the base policy !i, calculated starting from the next state 
xk+1 = fk(xk, $i, uk, wk), 
under the assumption that $ will stay fixed at the value $ = $i until the end of the horizon. 
This algorithm is related to the adaptive control/rollout algorithm that we discussed earlier in Section 5.2. Indeed, when the belief probabilities bk,i imply certainty, i.e., bk,̄i = 1 for some parameter index ī, and bk,i = 0 for i )= ī, the algorithm (6.43) is identical to the rollout by reoptimization algorithm of Section 5.2, where it is assumed that the model of the system has been estimated exactly. Also if all the policies !i are
Sec. 6.7 Adaptive Control by Rollout with a POMDP Formulation 177 
the same, a cost improvement property similar to the ones shown earlier can be proved. For further discussion and connections to the Bayesian optimization methodology, we refer to the author’s paper [Ber22c]. 
The Case of a Deterministic System 
Let us now consider the case where the system (6.38) is deterministic of the form 
xk+1 = fk(xk, $, uk). (6.44) 
Then, while the problem still has a stochastic character due to the uncertainty about the value of $, the DP algorithm (6.40) and its approximation in value space counterparts are greatly simplified because there is no expectation over wk to contend with. Indeed, given a state xk, a parameter $i, and a control uk, the on-line computation of the control of the rollout-like algorithm (6.43), takes the form 
ũk " arg min uk"Uk(xk) 
m ! 
i=1 
bk,i 
( 
gk(xk, $i, uk)+ Ĵ i k+1,"i 
# 
fk(xk, $i, uk) $ ) 
. (6.45) 
The computation of Ĵ i k+1,"i 
# 
fk(xk, $i, uk) $ 
involves a deterministic propa-
gation from the state xk+1 of Eq. (6.44) up to the end of the horizon, using the base policy !i, while assuming that $ is fixed at the value $i. 
In particular, the term 
Qk(uk, $i) = gk(xk, $i, uk) + Ĵ i k+1,"i 
# 
fk(xk, $i, uk) $ 
(6.46) 
appearing on the right side of Eq. (6.45) is viewed as a Q-factor that must be computed for every pair (uk, $i), uk " Uk(xk), i = 1, . . . ,m, using the base policy !i. The expected value of this Q-factor, 
Q̂k(uk) = m ! 
i=1 
bk,iQk(uk, $i), 
must then be calculated for every uk " Uk(xk), and the computation of the rollout control ũk is obtained from the minimization 
ũk " arg min uk"Uk(xk) 
Q̂k(uk); (6.47) 
cf. Eq. (6.45). This computation is illustrated in Fig. 6.7.1. The case of a deterministic system is particularly interesting because 
we can typically expect that the true parameter $# is identified in a finite number of stages, since at each stage k, we are receiving a noiseless measurement relating to $, namely the state xk. Once this happens, the problem becomes one of perfect state information.
178 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
x0 ) . . . 
) . . . 
) . . . 
uk x 
k xN 
k xk+1 
k u ! 
k 
. . . Q-Factors 
-Factors Current State x 
Current State xk 
! x " 
k+1 
0 x1 
x 
!! 
k+1 
x 
!!! 
k+1 
2 Next States Final States 
Next States Final States 
u !1 
!2 
u !1 
!2 
Price Rise Base Policy ! 1 
Price Rise Base Policy ! 1 
Base Policy ! 2 
Base Policy ! 2 
Figure 6.7.1 Schematic illustration of adaptive control by rollout for deterministic systems; cf. Eqs. (6.46) and (6.47). The Q-factors Qk(uk , ! 
i) are averaged over !i, using the current belief distribution bk , and the control applied is the one that minimizes the averaged Q-factor 
!m 
i=1 bk,iQk(uk , ! 
i) over uk ! Uk(xk). 
An illustration similar to the one of Fig. 6.7.1 applies to the rollout scheme (6.43) for the case of a stochastic system. In this case, a Q-factor 
Qk(uk, !i, wk) = gk(xk, !i, uk, wk) + Ĵ i k+1,!i 
" 
fk(xk, !i, uk, wk) # 
must be calculated for every triplet (uk, !i, wk), using the base policy "i. The rollout control ũk is obtained by minimizing the expected value of this Q-factor [averaged using the distribution of (!, wk)]; cf. Eq. (6.43). 
An interesting and intuitive example that demonstrates the deterministic system case is the popular Wordle puzzle. 
Example 6.7.1 (The Wordle Puzzle) 
In the classical form of this puzzle, we try to guess a mystery word !! out of a known finite collection of 5-letter words. This is done with sequential guesses each of which provides additional information on the correct word !!, by using certain given rules to shrink the current mystery list (the smallest list that contains !!, based on the currently available information). The objective is to minimize the number of guesses to find !! (using more than 6 guesses is considered to be a loss). This type of puzzle descends from the classical family of Mastermind puzzles that centers around decoding a secret sequence of objects (e.g., letters or colors) using partial observations. 
The rules for shrinking the mystery list relate to the common letters between the word guesses and the mystery word !!, and they will not be described here (there is a large literature regarding the Wordle puzzle). More-over, !! is assumed to be chosen from the initial collection of 5-letter words
Sec. 6.7 Adaptive Control by Rollout with a POMDP Formulation 179 
according to a uniform distribution. Under this assumption, it can be shown that the belief distribution bk at stage k continues to be uniform over the mystery list. As a result, we may use as state xk the mystery list at stage k, which evolves deterministically according to an equation of the form (6.44), where uk is the guess word at stage k. There are several base policies to use in the rollout-like algorithm (6.45), which are described in the paper by Bhambri, Bhattacharjee, and Bertsekas [BBB22], together with computational results that show that the corresponding rollout algorithm (6.45) performs remarkably close to optimal. 
The rollout approach also applies to several variations of the Wordle puzzle. Such variations may include for example a larger length ! > 5 of mystery words, and/or a known nonuniform distribution over the initial collection of !-letter words; see [BBB22]. 
Belief-Based Approximation in Value Space and Rollout 
We will now consider an alternative belief-based DP algorithm, given by 
J & k(xk, bk) = min 
uk"Uk(xk) E#,wk 
. 
gk(xk, $, uk, wk)+J & k+1(xk+1, bk+1) 
/ 
, (6.48) 
where 
xk+1 = fk(xk, $, uk, wk), bk+1 = Bk(xk, bk, uk, xk+1). 
The relation between the algorithms (6.39) and (6.48) is that if we write bk as a function of Ik, then the equality 
Jk(Ik) = J & k(xk, bk) 
holds as an identity, i.e., for all Ik; see e.g., [Ber17a], Chapter 4. Let us consider approximations whereby we replace J & 
k+1 with some other function that is more easily computable, in the spirit of approximation in value space. There are several possibilities along this line, some of which have been discussed in previous sections. In particular, in a rollout algorithm we introduce a base policy ! = {µ0, . . . , µN!1}, with components µk that are functions of (xk, bk), and we use in place of J & 
k+1, the cost function J & 
k+1," of !. This yields the algorithm 
ũk " arg min uk"Uk(xk) 
E#,wk 
. 
gk(xk, $, uk, wk)+ 
J & k+1," 
# 
xk+1, Bk(xk, bk, uk, xk+1) $ / 
, 
where xk+1 is given by 
xk+1 = fk(xk, $, uk, wk).
180 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
Example 6.7.2 (Searching Multiple Sites for a Treasure) 
In a classical and challenging problem of search, there are m sites, denoted 1, . . . ,m, one and only one of which contains a treasure. We assume that searching a site i costs a known amount ci > 0. If site i is searched and a treasure is present at the site, the search reveals it with probability pi, in which case the process terminates and no further costs are incurred. The problem is to find the search strategy that minimizes the total expected cost to find the treasure. 
The basic structure of this problem arises in a broad variety of applications, such as search-and-rescue, inspection-and-repair, as well as various artificial intelligence search contexts. The range of applications is expanded by considering variants of the problem that involve multiple treasures with site-dependent values, and multiple agents/searchers with agent-dependent search costs. Some related problems admit an exact analytical solution. A simple case is discussed in Example 4.3.1 of the DP textbook [Ber17]. A related but structurally di!erent formulation arises in the context of multiarmed bandit problems; see the DP textbook [Ber12], Example 1.3.1. 
The probability that site i contains the treasure at the start of stage k, i.e., after k searches, is denoted by bk,i. The vector 
bk = (bk,1, . . . , bk,m), 
is the belief state of the POMDP problem, and the initial belief state b0 is given. While the treasure has not yet been found, the control uk at stage k is the choice of the site to search and takes one of the m values 1, . . . , m. To be precise, the belief state also includes a state xk which has two possible values: “treasure not found” and the termination state “treasure found,” and there is a trivial system equation whereby xk transitions to the termination state once a successful search occurs. 
The belief states evolves according to an equation that is calculated with the aid of Bayes’ rule. In particular, assume that the treasure has not yet been found, and site ī is searched at time k. Then by applying Bayes’ rule, it can be verified that the probability bk,̄i is updated according to 
bk+1,̄i = 
1 1 if the search finds the treasure, 
bk,̄i(1"pī) 
bk,̄i(1"pī)+ 2 
i%=ī bk,i 
if the search does not find the treasure, 
and the probabilities bk,j with j "= ī are updated according to 
bk+1,j = 
1 0 if the search finds the treasure, 
bk,j 
bk,̄i(1"pī)+ 2 
i%=ī bk,i 
if the search does not find the treasure. 
We write these equations in the abstract form 
bk+1,i = Bi k(bk, uk, xk+1),
Sec. 6.8 Rollout for Minimax Control 181 
where xk+1 takes values “treasure found” and “treasure not found” with probabilities bk,̄ipī and 1!bk,̄ipī, respectively (uk here is the site ī that is searched at time k). 
Suppose now that we have a base policy " = {µ0, µ1, . . .} that consists of functions µk, which given the current belief state bk, choose to search site µk(bk). Then assuming that the treasure has not yet been found at time k, the rollout algorithm (6.43) takes the form 
ũk # arg min uk!{1,...,m} 
" 
cuk + Exk+1 
. 
J $ k+1," 
# 
Bk(bk, uk, xk+1) $ /% 
, (6.49) 
where J $ k+1," 
# 
Bk(bk, uk, xk+1) $ 
is the expected cost of the base policy starting from belief state 
Bk(bk, uk, xk+1) = # 
B1 k(bk, uk, xk+1), . . . , B 
m k (bk, uk, xk+1) 
$ 
. 
The cost J $ k+1,"(bk+1) appearing in Eq. (6.49), starting from a belief state 
bk+1, can be computed using the law of iterated expectations as follows: For each i = 1, . . . ,m, we compute the cost Ci," that would be incurred starting from bk+1 and using ", while assuming that the treasure is located at site i; this can be done for example by simulation. We then set 
J $ k+1,"(bk+1) = 
m ! 
i=1 
bk+1,iCi,". 
There are several possibilities for base policy ", which are likely context dependent. For a simple example, we may let " be the greedy policy that searches the site ī of maximum success probability: 
ī # arg max i!{1,...,m} 
bk,i. 
In conclusion, assuming that the terms 
Exk+1 
. 
J $ k+1," 
# 
Bk(bk, uk, xk+1) $ / 
are available on-line for all bk and uk, through a combination of on-line and o!-line computation (that may involve simulation), the algorithm (6.49) admits a tractable implementation, which yields a one-step lookahead suboptimal policy. 
6.8 ROLLOUT FOR MINIMAX CONTROL 
The problem of optimal control of uncertain systems is usually treated within a stochastic framework, whereby all disturbances w0, . . . , wN!1 are described by probability distributions, and the expected value of the cost is minimized. However, in many practical situations a stochastic description
182 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
of the disturbances may not be available, but one may have information with less detailed structure, such as bounds on their magnitude. In other words, one may know a set within which the disturbances are known to lie, but may not know the corresponding probability distribution. Under these circumstances one may use a minimax approach, whereby the worst possible values of the disturbances within the given set are assumed to occur. Within this context, we take the view that the disturbances are chosen by an antagonistic opponent. The minimax approach is also connected with two-player games, when in lack of information about the opponent, we adopt a worst case viewpoint during on-line play, as well as with contexts where we wish to guard against adversarial attacks.† 
To be specific, consider a finite horizon context, and assume that the disturbances w0, w1, . . . , wN!1 do not have a probabilistic description but rather are known to belong to corresponding given sets Wk(xk, uk) % Dk, k = 0, 1, . . . , N ! 1, which may depend on the current state xk and control uk. The minimax control problem is to find a policy ! = {µ0, . . . , µN!1} with µk(xk) " Uk(xk) for all xk and k, which minimizes the cost function 
J"(x0) = max wk!Wk(xk,µk(xk)) 
k=0,1,...,N"1 
3 
gN (xN ) + N!1 ! 
k=0 
gk # 
xk, µk(xk), wk 
$ 
4 
. 
The DP algorithm for this problem takes the following form, which resembles the one corresponding to the stochastic DP problem (maximization is used in place of expectation): 
J# N (xN ) = gN (xN ), (6.50) 
J# k (xk) = min 
uk"U(xk) max 
wk"Wk(xk,uk) 
" 
gk(xk, uk, wk) + J# k+1 
# 
fk(xk, uk, wk) $% 
. 
(6.51) This algorithm can be explained by using a principle of optimality 
type of argument. In particular, we consider the tail subproblem whereby we are at state xk at time k, and we wish to minimize the “cost-to-go” 
max wt!Wt(xt,µt(xt)) t=k,k+1,...,N"1 
3 
gN (xN ) + N!1 ! 
t=k 
gt # 
xt, µt(xt), wt 
$ 
4 
. 
We argue that if !# = {µ# 0, µ 
# 1, . . . , µ 
# N!1} is an optimal policy for the min-
imax problem, then the tail of the policy {µ# k, µ 
# k+1, . . . , µ 
# N!1} is optimal 
† The minimax approach to decision and control has its origins in the 50s and 60s. It is also referred to by other names, depending on the underlying 
context, such as robust control , robust optimization, control with a set membership 
description of the uncertainty , and games against nature. In this book, we will be using the minimax control name.
Sec. 6.8 Rollout for Minimax Control 183 
for the tail subproblem. The optimal cost of this subproblem is J# k (xk), 
as given by the DP algorithm (6.50)-(6.51). The algorithm expresses the intuitive fact that when at state xk at time k, then regardless of what happened in the past, we should choose uk that minimizes the worst/maximum value over wk of the sum of the current stage cost plus the optimal cost of the tail subproblem that starts from the next state. This argument requires a mathematical proof, which turns out to involve a few fine points. For a detailed mathematical derivation, we refer to the author’s textbook [Ber17a], Section 1.6. However, the DP algorithm (6.50)-(6.51) is correct assuming finite state and control spaces, among other cases. 
Approximation in Value Space and Minimax Rollout 
The approximation ideas for stochastic optimal control are also relevant within the minimax context. In particular, approximation in value space with one-step lookahead applies at state xk a control 
ũk " arg min uk"Uk(xk) 
max wk"Wk(xk,uk) 
" 
gk(xk, uk, wk) + J̃k+1 
# 
fk(xk, uk, wk) $ % 
, 
(6.52) where J̃k+1(xk+1) is an approximation to the optimal cost-to-go J# 
k+1(xk+1) from state xk+1. 
Rollout is obtained when this approximation is the tail cost of some base policy ! = {µ0, . . . , µN!1}: 
J̃k+1(xk+1) = Jk+1,"(xk+1). 
Given !, we can compute Jk+1,"(xk+1) by solving a deterministic maximization DP problem with the disturbances wk+1, . . . , wN!1 playing the role of “optimization variables/controls.” For finite state, control, and disturbance spaces, this is a longest path problem defined on an acyclic graph, since the control variables uk+1, . . . , uN!1 are determined by the base policy. It is then straightforward to implement rollout: at xk we generate all next states of the form 
xk+1 = fk(xk, uk, wk) 
corresponding to all possible values of uk " Uk(xk) and wk " Wk(xk, uk). We then run the maximization/longest path problem described above to compute J̃k+1(xk+1) from each of these possible next states xk+1. Finally, we obtain the rollout control ũk by solving the minimax problem in Eq. (6.52). Moreover, it is possible to use truncated rollout to approximate the tail cost of the base policy. For a more detailed discussion of this implementation, see the author’s paper [Ber19d] (Section 5.4). 
Note that like all rollout algorithms, the minimax rollout algorithm is well-suited for on-line replanning in problems where data may be changing or may be revealed during the process of control selection.
184 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
We mentioned earlier that deterministic problems allow a more general form of rollout, whereby we may use a base heuristic that need not be a legitimate policy, i.e., it need not be sequentially consistent. For cost improvement it is su"cient that the heuristic be sequentially improving. A similarly more general view of rollout is not easily constructed for stochastic problems, but is possible for minimax control. 
In particular, suppose that at any state xk there is a heuristic that generates a sequence of feasible controls and disturbances, and corresponding states, 
{uk, wk, xk+1, uk+1, wk+1, xk+2, . . . , uN!1, wN!1, xN}, 
with corresponding cost 
Hk(xk) = gk(xk, uk, wk) + · · ·+ gN!1(xN!1, uN!1, wN!1) + gN (xN ). 
Then the rollout algorithm applies at state xk a control 
ũk " arg min uk"Uk(xk) 
max wk"Wk(xk,uk) 
" 
gk(xk, uk, wk) +Hk+1 
# 
fk(xk, uk, wk) $ % 
. 
This does not preclude the possibility that the disturbances wk, . . . , wN!1 
are chosen by an antagonistic opponent, but allows more general choices of disturbances, obtained for example, by some form of approximate maximization. For example, when the disturbance involves multiple components, wk = (w1 
k, . . . , w m k ), corresponding to multiple opponent agents, the 
heuristic may involve an agent-by-agent maximization strategy. The sequential improvement condition, similar to the deterministic 
case, is that for all xk and k, 
min uk"Uk(xk) 
max wk"Wk(xk,wk) 
" 
gk(xk, uk, wk) +Hk+1 
# 
fk(xk, uk, wk) $ % 
# Hk(xk). 
It guarantees cost improvement, i.e., that for all xk and k, the rollout policy 
!̃ = {µ̃0, . . . , µ̃N!1} 
satisfies Jk,"̃(xk) # Hk(xk). 
Thus, generally speaking, minimax rollout is fairly similar to rollout for deterministic as well as stochastic DP problems. The main di!erence with deterministic (or stochastic) problems is that to compute the Q-factor of a control uk, we need to solve a maximization problem, rather than carry out a deterministic (or Monte-Carlo, respectively) simulation with the given base policy.
Sec. 6.8 Rollout for Minimax Control 185 
Example 6.8.1 (Pursuit-Evasion Problems) 
Consider a pursuit-evasion problem with state xk = (x1 k, x 
2 k), where x1 
k is the location of the minimizer/pursuer and x2 
k is the location of the maxi-mizer/evader, at stage k, in a (finite node) graph defined in two- or threedimensional space. There is also a cost-free and absorbing termination state that consists of a subset of pairs (x1, x2) that includes all pairs with x1 = x2. The pursuer chooses one out of a finite number of actions uk # Uk(xk) at each stage k, when at state xk, and if the state is xk and the pursuer selects uk, the evader may choose from a known set Xk+1(xk, uk) of next states xk+1, which depends on (xk, uk). The objective of the pursuer is to minimize a nonnegative terminal cost g(x1 
N , x2 N) at the end of N stages (or reach the 
termination state, which has cost 0 by assumption). A reasonable base policy for the pursuer can be precomputed by DP as follows: given the current (nontermination) state xk = (x1 
k, x 2 k), make a move along the path that starts 
from x1 k and minimizes the terminal cost after N ! k stages, under the as-
sumption that the evader will stay motionless at his current location x2 k. (In 
a variation of this policy, the DP computation is done under the assumption that the evader will follow some nominal sequence of moves.) 
For the on-line computation of the rollout control, we need the maximal value of the terminal cost that the evader can achieve starting from every xk+1 # Xk+1(xk, uk), assuming that the pursuer will follow the base policy (which has already been computed). We denote this maximal value by J̃k+1(xk+1). The required values J̃k+1(xk+1) can be computed by an (N ! k)-stage DP computation involving the optimal choices of the evader, while assuming the pursuer uses the (already computed) base policy. Then the rollout control for the pursuer is obtained from the minimization 
µ̃k(xk) # arg min uk!Uk(xk) 
max xk+1!Xk+1(xk,uk) 
J̃k+1(xk+1). 
Note that the preceding algorithm can be adapted for the imperfect information case where the pursuer knows x2 
k imperfectly. This is possible by using a form of assumed certainty equivalence: the pursuer’s base policy and the evader’s maximization can be computed by using an estimate of the current location x2 
k instead of the unknown true location. 
In the preceding pursuit-evasion example, the choice of the base policy was facilitated by the special structure of the problem. Generally, however, finding a suitable base policy that can be conveniently implemented is an important problem-dependent issue. 
Variants of Minimax Rollout 
Several of the variants of rollout discussed earlier have analogs in the minimax context, e.g., truncation with terminal cost approximation, multistep and selective step lookahead, and multiagent rollout. In particular, in the "-step lookahead variant, we solve the "-stage problem
186 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
min uk ,µk+1,...,µk+!"1 
max wt!Wt(xt,ut) t=k,...,k+!"1 
0 
gk(xk, uk, wk) + k+!!1! 
t=k+1 
gt # 
xt, µt(xt), wt 
$ 
+Hk+!(xk+!) 
5 
, 
we find an optimal solution ũk, µ̃k+1, . . . , µ̃k+!!1, and we apply the first component ũk of that solution. As an example, this type of problem is solved at each move of chess programs like AlphaZero, where the terminal cost function is encoded through a position evaluator. In fact when multistep lookahead is used, special techniques such as alpha-beta pruning may be used to accelerate the computations by eliminating unnecessary portions of the lookahead graph. These techniques are well-known in the context of the two-person computer game methodology, and are used widely in games such as chess. 
It is interesting to note that, contrary to the case of stochastic optimal control, there is an on-line constrained form of rollout for minimax control. Here there are some additional trajectory constraints of the form 
(x0, u0, . . . , uN!1, xN ) " C, 
where C is an arbitrary set. The modification needed is similar to the one of Section 6.6: at partial trajectory 
ỹk = (x̃0, ũ0, . . . , ũk!1, x̃k), 
generated by rollout, we use a heuristic with cost function Hk+1 to compute the Q-factor 
Q̃k(x̃k, uk) = max wk ,...,wN"1 
" 
gk(x̃k, uk, wk) 
+Hk+1 
# 
fk(x̃k, uk, wk), wk+1, . . . , wN!1 
$ % 
for each uk in the set Ũk(ỹk) that guarantee feasibility [we can check feasibility here by running some algorithm that verifies whether the future disturbances wk, . . . , wN!1 can be chosen to violate the constraint under the base policy, starting from (ỹk, uk)]. Once the set of “feasible controls” Ũk(ỹk) is computed, we can obtain the rollout control by the Q-factor minimization: 
ũk " arg min uk"Ũk(ỹk) 
Q̃k(x̃k, uk). 
We may also use fortified versions of the unconstrained and constrained rollout algorithms, which guarantee a feasible cost-improved rollout policy. This requires the assumption that the base heuristic at the initial state produces a trajectory that is feasible for all possible disturbance sequences. Similar to the deterministic case, there are also truncated and multiagent versions of the minimax rollout algorithm.
Sec. 6.8 Rollout for Minimax Control 187 
Example 6.8.2 (Multiagent Minimax Rollout) 
Let us consider a minimax problem where the minimizer’s choice involves the collective decision of m agents, u = (u1, . . . , um), with u! corresponding to agent !, and constrained to lie within a finite set U !. Thus u must be chosen from within the set 
U = U1 $ . . .$ U !, 
which is finite but grows exponentially in size with m. The maximizer’s choice w is constrained to belong to a finite set W . We consider multiagent rollout for the minimizer, and for simplicity, we focus on a two-stage problem. However, there are straightforward extensions to a more general multistage framework. 
In particular, we assume that the minimizer knowing an initial state x0, chooses u = (u1, . . . , um), with u! # U !, ! = 1, . . . ,m, and a state transition 
x1 = f0(x0, u) 
occurs with cost g0(x0, u). Then the maximizer, knowing x1, chooses w # W , and a terminal state 
x2 = f1(x1, w) 
is generated with cost g1(x1, w) + g2(x2). 
The problem is to select u # U , to minimize 
g0(x0, u) + max w!W 
6 
g(x1, w) + g2(x2) 7 
. 
The exact DP algorithm for this problem is given by 
J# 1 (x1) = max 
w!W 
" 
g1(x1, w) + g2 # 
f1(x1, w) $ % 
, 
J# 0 (x0) = min 
u!U 
" 
g0(x0, u) + J# 1 
# 
f0(x0, u) $ % 
. 
This DP algorithm is computationally intractable for large m. The reason is that the set of possible minimizer choices u grows exponentially with m, and for each of these choices the value of J# 
1 
# 
f0(x0, u) $ 
must be computed. However, the problem can be solved approximately with multiagent 
rollout, using a base policy µ = (µ1, . . . , µm). Then the number of times J# 1 
# 
f0(x0, u) $ 
needs to be computed is dramatically reduced. This computation is done sequentially, one-agent-at-a-time, as follows: 
ũ1 # arg min u1!U1 
" 
g0 # 
x0, u 1, µ2(x0), . . . , µ 
m(x0) $ 
+ J# 1 
( 
f0 # 
x0, u 1, µ2(x0), . . . , µ 
m(x0) $ )% 
,
188 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
ũ2 # arg min u2!U2 
" 
g0 # 
x, ũ1, u2, µ3(x0), . . . , µ m(x0) 
$ 
+ J# 1 
( 
f0 # 
x0, ũ 1, u2, µ3(x0), . . . , µ 
m(x0) $ )% 
, 
. . . . . . . . . . . . 
ũm # arg min um!Um 
" 
g0 # 
x0, ũ 1, ũ2, . . . , ũm"1, um 
$ 
+ J# 1 
( 
f0 # 
x0, ũ 1, ũ2, . . . , ũm"1, um 
$ )% 
. 
In this algorithm, the number of times for which J# 1 
# 
f0(x0, u) $ 
must be computed grows linearly with m. 
When the number of stages is larger than two, a similar algorithm can be used. Essentially, the one-stage maximizer’s cost function J# 
1 must be replaced by the optimal cost function of a multistage maximization problem, where the minimizer is constrained to use the base policy. 
An interesting question is how do various algorithms work when approximations are used in the min-max and max-min problems? We can certainly improve the minimizer’s policy assuming a fixed policy for the maximizer . However, it is unclear how to improve both the minimizer’s and the maximizer’s policies simultaneously. In practice, in symmetric games , like chess, a common policy is trained for both players. In particular, in the AlphaZero and TD-Gammon programs this strategy is computationally expedient and has worked well. However, there is no reliable theory to guide the simultaneous training of policies for both maximizer and minimizer, and it is quite plausible that unusual behavior may arise in exceptional cases. Even exact policy iteration methods for Markov games encounter serious convergence di"culties, and need to be modified for reliable behavior. The author’s paper [Ber21c] and book [Ber22a] (Chapter 5) address these convergence issues with modified versions of the policy iteration method, and give many earlier references. 
We finally note another source of di"culty in minimax control: New-ton’s method applied to solution of the Bellman equation for minimax problems exhibits more complex behavior than its expected value counterpart. The reason is that the Bellman operator T for infinite horizon problems, given by 
(TJ)(x) = min u"U(x) 
max w"W (x,u) 
" 
g(x, u, w) + %J # 
f(x, u, w) $ % 
, for all x, 
is neither convex nor concave as a function of J . To see this, note that the function 
max w"W (x,u) 
" 
g(x, u, w) + %J # 
f(x, u, w) $ % 
, 
viewed as a function of J [for fixed (x, u)], is convex, and when minimized over u " U(x), it becomes neither convex nor concave (cf. Fig. 3.9.4).
Sec. 6.8 Rollout for Minimax Control 189 
As a result there are special di culties in connection with convergence of Newton’s method and the natural form of policy iteration, given by Pollatschek and Avi-Itzhak [PoA69]; see also Chapter 5 of the author’s abstract DP book [Ber22a]. 
Minimax Control and Zero-Sum Game Theory 
Zero-sum game problems are viewed as fundamental in the field of economics, and there is an extensive and time-honored theory around them. In the case where the game involves a dynamic system 
xk+1 = fk(xk, uk, wk), 
and a cost function gk(xk, uk, wk), 
there are two players, the minimizer choosing uk 2 Uk(xk), and the maximizer choosing wk 2 Wk(xk), at each stage k. Such zero-sum games involve two minimax control problems: 
(a) The min-max problem, where the minimizer chooses a policy first and the maximizer chooses a policy second with knowledge of the minimizer’s policy. The DP algorithm for this problem has the form 
J⇤ N (xN ) = gN (xN ), 
J⇤ k (xk) = min 
uk2Uk(xk) max 
wk2Wk(xk) 
h gk(xk, uk, wk)+J⇤ 
k+1 
  fk(xk, uk, wk) 
 i . 
(b) The max-min problem, where the maximizer chooses policy first and the minimizer chooses policy second with knowledge of the maximizer’s policy. The DP algorithm for this problem has the form 
ĴN (xN ) = gN (xN ), 
Ĵk(xk) = max wk2Wk(xk) 
min uk2Uk(xk) 
h gk(xk, uk, wk)+ Ĵk+1 
  fk(xk, uk, wk) 
 i . 
A basic and easily seen fact is that 
Max-Min optimal value  Min-Max optimal value. 
Game theory is particularly interested on conditions that guarantee that 
Max-Min optimal value = Min-Max optimal value. (6.53) 
However, this question is of limited interest in engineering contexts that involve worst case design. Moreover, the validity of the minimax equality (6.53) is beyond the range of practical RL. This is so primarily because once approximations are introduced, the delicate assumptions that guarantee this equality are disrupted.
190 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
6.9 SMALL STAGE COSTS AND LONG HORIZON -CONTINUOUS-TIME ROLLOUT 
Let us consider the deterministic one-step approximation in value space scheme 
µ̃k(xk) ! arg min uk!Uk(xk) 
! 
gk(xk, uk) + J̃k+1 
" 
fk(xk, uk) # $ 
. (6.54) 
In the context of rollout, J̃k+1 
" 
fk(xk, uk) # 
is either the cost of the trajectory generated by the base heuristic starting from the next state fk(xk, uk), or some approximation that may involve truncation and terminal cost function approximation, as in the truncated rollout scheme of Section 6.5. 
There is a special di!culty within this context, which is often encountered in practice. It arises when the cost per stage gk(xk, uk) is either 0 or is small relative to the cost-to-go approximation J̃k+1 
" 
fk(xk, uk) # 
. Then there is a potential pitfall to contend with: the cost approximation errors that are inherent in the term J̃k+1 
" 
fk(xk, uk) # 
may overwhelm the first stage cost term gk(xk, uk), with unpredictable consequences for the quality of the one-step-lookahead policy !̃ = {µ̃0, . . . , µ̃N"1}. We will discuss this di!culty by first considering a discrete-time problem arising from discretization of a continuous-time optimal control problem. 
Continuous-Time Optimal Control and Approximation in Value Space 
Consider a problem that involves a vector di"erential equation of the form 
ẋ(t) = h " 
x(t), u(t), t # 
, 0 " t " T, (6.55) 
where x(t) ! #n is the state vector at time t, ẋ(t) ! #n is the vector of first order time derivatives of the state at time t, u(t) ! U $ #m is the control vector at time t, where U is the control constraint set, and T is a given terminal time. Starting from a given initial state x(0), we want to find a feasible control trajectory 
% 
u(t) | t ! [0, T ] & 
, which together with its corresponding state trajectory 
% 
x(t) | t ! [0, T ] & 
, minimizes a cost function of the form 
G " 
x(T ) # 
+ 
' T 
0 g " 
x(t), u(t), t # 
dt, (6.56) 
where g represents cost per unit time, and G is a terminal cost function. This is a classical problem with a long history. 
Let us consider a simple conversion of the preceding continuous-time problem to a discrete-time problem, while treading lightly over some of the associated mathematical fine points. We introduce a small discretization increment " > 0, such that T = "N where N is a large integer, and we replace the di"erential equation (6.55) by 
xk+1 = xk + " · hk(xk, uk), k = 0, . . . , N % 1.
Sec. 6.9 Small Stage Costs and Long Horizon 191 
Here the function hk is given by 
hk(xk, uk) = h " 
x(k"), u(k"), k" # 
, 
where we view {xk | k = 0, . . . , N % 1} and {uk | k = 0, . . . , N % 1} as state and control trajectories, respectively, which approximate the corresponding continuous-time trajectories: 
xk & x(k"), uk & u(k"). 
We also replace the cost function (6.56) by 
gN(xN ) + N"1 ( 
k=0 
" · gk(xk, uk), 
where 
gN(xN ) = G " 
x(N") # 
, gk(xk, uk) = g " 
x(k"), u(k"), k" # 
. 
Thus the approximation in value space scheme with time discretization takes the form 
µ̃k(xk) ! arg min uk!U 
! 
" · gk(xk, uk) + J̃k+1 
" 
xk + " · hk(xk, uk) # $ 
; (6.57) 
where J̃k+1 is the function that approximates the cost-to-go starting from a state at time k+1. We note here that the ratio of the terms " ·gk(xk, uk) and J̃k+1 
" 
xk+" ·hk(xk, uk) # 
is likely to tend to 0 as " ' 0, since J̃k+1 
" 
xk+ " ·hk(xk, uk) 
# 
ordinarily stays roughly constant at a nonzero level as " ' 0. This suggests that the one-step lookahead minimization may be degraded substantially by discretization, and other errors, including rollout truncation and terminal cost approximation. Note that a similar sensitivity to errors may occur in other discrete-time models that involve frequent selection of decisions, with cost per stage that is very small relative to the cumulative cost over many stages and/or the terminal cost. 
To deal with this di!culty, we subtract the constant J̃k(xk) in the one-step-lookahead minimization (6.57), and write 
µ̃k(xk) ! arg min uk!U 
! 
" · gk(xk, uk) + ) 
J̃k+1 
" 
xk + " · hk(xk, uk) # 
% J̃k(xk) *$ 
; 
(6.58) since J̃k(xk) does not depend on uk, the results of the minimization are not a"ected. Assuming J̃k is di"erentiable with respect to its argument, we can write 
J̃k+1 
" 
xk + " · hk(xk, uk) # 
% J̃k(xk) & " ·(xJ̃k(xk)#hk(xk, uk),
192 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
where (xJ̃k denotes the gradient of Jk (a column vector), and prime denotes transposition. By dividing with ", and taking informally the limit as " ' 0, we can write the one-step lookahead minimization (6.58) as 
µ̃(t) ! arg min u(t)!U 
! 
g " 
x(t), u(t), t # 
+(xJ̃t " 
x(t) ## h " 
x(t), u(t), t # $ 
, (6.59) 
where J̃t(x) is the continuous-time cost function approximation and(xJ̃t(x) is its gradient with respect to x. This is the correct analog of the approximation in value space scheme (6.54) for continuous-time problems. 
Rollout for Continuous-Time Optimal Control 
In view of the value approximation scheme of Eq. (6.59), it is natural to speculate that the continuous-time analog of rollout with a base policy of the form 
! = + 
µt 
" 
x(t) # 
| 0 " t " T , 
, (6.60) 
where µt 
" 
x(t) # 
! U for all x(t) and t, has the form 
µ̃t 
" 
x(t) # 
! arg min u(t)!U 
! 
g " 
x(t), u(t), t # 
+(xJ!,t " 
x(t) ## h " 
x(t), u(t), t # $ 
. 
(6.61) Here J!,t 
" 
x(t) # 
is the cost of the base policy ! starting from state x(t) at time t, and satisfies the terminal condition 
J!,T " 
x(T ) # 
= G " 
x(T ) # 
. 
Computationally, the inner product in the right-hand side of the above minimization can be approximated using the finite di"erence formula 
(xJ!,t " 
x(t) ## h " 
x(t), u(t), t # 
& J!,t 
) 
x(t) + " · h " 
x(t), u(t), t # * 
% J!,t " 
x(t) # 
" , 
which can be calculated by running the base policy ! starting from x(t) and from x(t) + " · h 
" 
x(t), u(t), t # 
. (This finite di"erencing operation may involve tricky computational issues, but we will not get into this.) 
An important question is how to select the base policy !. A choice that is often sensible and convenient is to choose ! to be a “short-sighted” policy, which takes into account the “short term” cost from the current state (say for a very small horizon starting from the current time t), but ignores the remaining cost. An extreme case is the myopic policy, given by 
µt 
" 
x(t) # 
! argmin u!U 
g " 
x(t), u(t), t # 
.
Sec. 6.9 Small Stage Costs and Long Horizon 193 
ẋ(t) = u(t) 
dt Given Point Given Line 
Given Point Given Line 
! t Tt T 
x(t) 
Point (0, 0) 0) Optimal Solution 0) Optimal Trajectory 
Length = 
! T 
0 
" 
1 + # 
u(t) $2 
dt 
Figure 6.9.1 Problem of finding a curve of minimum length from a given point to a given line, and its formulation as a calculus of variations problem. 
This policy is the continuous-time analog of the greedy policy that we discussed in the context of discrete-time problems, and the traveling salesman Example 6.4.1 in particular. 
The following example illustrates the rollout algorithm (6.61) with a problem where the base policy cost J!,t 
" 
x(t) # 
is independent of x(t) (it depends only on t), so that 
(xJ!,t " 
x(t) # 
) 0. 
In this case, in view of Eq. (6.59), the rollout policy is myopic. It turns out that the optimal policy in this example is also myopic, so that the rollout policy is optimal, even though the base policy is very poor. 
Example 6.9.1 (A Calculus of Variations Problem) 
This is a simple example from the classical context of calculus of variations (see [Ber17a], Example 7.1.3). The problem is to find a minimum length curve that starts at a given point and ends at a given line. Without loss of generality, let (0, 0) be the given point, and let the given line be the vertical line that passes through (T, 0), as shown in Fig. 6.9.1. 
Let " 
t, x(t) # 
be the points of the curve, where 0 ! t ! T . The portion 
of the curve joining the points " 
t, x(t) # 
and " 
t+ dt, x(t+ dt) # 
can be approximated, for small dt, by the hypotenuse of a right triangle with sides dt and ẋ(t)dt. Thus the length of this portion is 
-
(dt)2 + " 
ẋ(t) #2 (dt)2, 
which is equal to -
1 + " 
ẋ(t) #2 
dt.
194 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
The length of the entire curve is the integral over [0, T ] of this expression, so the problem is to 
minimize 
' T 
0 
-
1 + " 
ẋ(t) #2 
dt 
subject to x(0) = 0. 
To reformulate the problem as a continuous-time optimal control problem, we introduce a control u and the system equation 
ẋ(t) = u(t), x(0) = 0. 
The problem then takes the form 
minimize 
' T 
0 
-
1 + " 
u(t) #2 
dt. 
This is a problem that fits our continuous-time optimal control framework, with 
h " 
x(t), u(t), t # 
= u(t), g " 
x(t), u(t), t # 
= 
-
1 + " 
u(t) #2 , G 
" 
x(T ) # 
= 0. 
Consider now a base policy ! whereby the control depends only on t 
and not on x. Such a policy has the form 
µt 
" 
x(t) # 
= "(t), for all x(t), 
where "(t) is some scalar function. For example, "(t) may be constant, "(t) " "̄ for some scalar "̄, which yields a straight line trajectory that starts at (0, 0) and makes an angle # with the horizontal with tan(#) = "̄. The cost function of the base policy is 
J!,t 
" 
x(t) # 
= 
' T 
t 
. 
1 + "($ )2 d$, 
which is independent of x(t), so that #xJ!,t 
" 
x(t) # 
" 0. Thus, from the minimization of Eq. (6.61), we have 
µ̃t 
" 
x(t) # 
$ arg min u(t)!" 
-
1 + " 
u(t) #2 , 
and the rollout policy is µ̃t 
" 
x(t) # 
" 0. 
This is the optimal policy: it corresponds to the horizontal straight line that starts at (0, 0) and ends at (T, 0).
Sec. 6.9 Small Stage Costs and Long Horizon 195 
Rollout with General Base Heuristics - Sequential Improvement 
An extension of the rollout algorithm (6.61) is to use a more general base heuristic whose cost function Ht 
" 
x(t) # 
can be evaluated by simulation. This rollout algorithm has the form 
µ̃(t) ! arg min u(t)!U 
! 
g " 
x(t), u(t), t # 
+(xHt 
" 
x(t) ## h " 
x(t), u(t), t # $ 
. 
Here the policy cost function J!,t is replaced by a more general di"erentiable function Ht, obtainable through a base heuristic, which may lack the sequential consistency property that is inherent in policies. 
We will now show a cost improvement property of the rollout algorithm based on the natural condition 
HT 
" 
x̃(T ) # 
= G " 
x̃(T ) # 
, (6.62) 
and the assumption 
min u(t)!U 
! 
g " 
x(t), u(t), t # 
+(tHt 
" 
x(t) # 
+(xHt 
" 
x(t) ## h " 
x(t), u(t), t # $ 
" 0, 
(6.63) for all 
" 
x(t), t # 
, where (xHt denotes gradient with respect to x, and (tHt 
denotes gradient with respect to t. This assumption is the continuous-time analog of the sequential improvement condition of Definition 6.4.2 [cf. Eq. (6.18)]. Under this assumption, we will show that 
J!̃,0 " 
x(0) # 
" H0 " 
x(0) # 
, (6.64) 
i.e., the cost of the rollout policy starting from the initial state x(0) is no worse than the base heuristic cost starting from the same initial state. 
Indeed, let % 
x̃(t) | t ! [0, T ] & 
and % 
ũ(t) | t ! [0, T ] & 
be the state and control trajectories generated by the rollout policy starting from x(0). Then the sequential improvement condition (6.63) yields 
g " 
x̃(t), ũ(t), t # 
+(tHt 
" 
x̃(t) # 
+(xHt 
" 
x̃(t) ## h " 
x̃(t), ũ(t), t # 
" 0 
for all t, and by integration over [0, T ], we obtain 
' T 
0 g " 
x̃(t), ũ(t), t # 
dt+ 
' T 
0 
) 
(tHt 
" 
x̃(t) # 
+(xHt 
" 
x̃(t) ## h " 
x̃(t), ũ(t), t # * 
dt " 0. 
(6.65) The second integral above can be written as 
' T 
0 
) 
(tHt 
" 
x̃(t) # 
+(xHt 
" 
x̃(t) ## h " 
x̃(t), ũ(t), t #* 
dt 
= 
' T 
0 
) 
(tHt 
" 
x̃(t) # 
+(xHt 
" 
x̃(t) ## dx̃(t) 
dt 
* 
dt,
196 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
and its integrand is the total di!erential with respect to time: d dt 
( 
Ht 
# 
x̃(t) $ ) 
. 
Thus we obtain from Eq. (6.65) 
8 T 
0 g # 
x̃(t),ũ(t), t $ 
dt+ 
8 T 
0 
d 
dt 
( 
Ht 
# 
x̃(t) $ ) 
dt 
= 
8 T 
0 g # 
x̃(t), ũ(t), t $ 
dt+HT 
# 
x̃(T ) $ 
!H0 # 
x̃(0) $ 
# 0. 
(6.66) 
Since HT 
# 
x̃(T ) $ 
= G # 
x̃(T ) $ 
[cf. Eq. (6.62)] and x̃(0) = x(0), from Eq. (6.66) [which is a direct consequence of the sequential improvement condition (6.63)], it follows that 
J"̃,0 # 
x(0) $ 
= 
8 T 
0 g # 
x̃(t), ũ(t), t $ 
dt+G # 
x̃(T ) $ 
# H0 # 
x(0) $ 
, 
thus proving the cost improvement property (6.64). Note that the sequential improvement condition (6.63) is satisfied if 
Ht is the cost function J",t corresponding to a base policy !. The reason is that for any policy ! = 
& 
µt(x(t)) | 0 # t # T ' 
[cf. Eq. (6.60)], the analog of the DP algorithm (under the requisite mathematical conditions) takes the form 
0 = g # 
x(t), µt(x(t)), t $ 
+*tJ",t # 
x(t) $ 
+*xJ",t # 
x(t) $& h # 
x(t), µt(x(t)), t $ 
. (6.67) 
In continuous-time optimal control theory, this is known as the Hamilton-Jacobi-Bellman equation. It is a partial di!erential equation, which may be viewed as the continuous-time analog of the DP algorithm for a single policy; there is also a Hamilton-Jacobi-Bellman equation for the optimal cost function J* 
t 
# 
x(t) $ 
(see optimal control textbook accounts, such as [Ber17a], Section 7.2, and the references cited there). As illustration, the reader may verify that the cost function of the base policy used in the calculus of variations problem of Example 6.9.1 satisfies this equation. It can be seen from the Hamilton-Jacobi-Bellman Eq. (6.67) that when Ht = J",t, the sequential improvement condition (6.63) and the cost improvement property (6.64) hold. 
Approximating Cost Function Di!erences 
Let us finally note that the preceding analysis suggests that when dealing with a discrete-time problem with a long horizon N , a system equation xk+1 = fk(xk, uk), and a small cost per stage gk(xk, uk) relative to the optimal cost-to-go function Jk+1 
# 
fk(xk, uk) $ 
, it is worth considering an alternative implementation of the approximation in value space scheme. In particular, we should consider approximating the cost di!erences 
Dk(xk, uk) = Jk+1 
# 
fk(xk, uk) $ 
! Jk(xk)
Sec. 6.10 Epilogue 197 
instead of approximating the cost-to-go functions Jk+1 
# 
fk(xk, uk) $ 
. The one-step-lookahead minimization (6.54) should then be replaced by 
µ̃k(xk) " arg min uk"Uk(xk) 
6 
gk(xk, uk) + D̃k(xk, uk) 7 
, 
where D̃k is the approximation to Dk. Note also that while for continuous-time problems, the idea of ap-
proximating the gradient of the optimal cost function is essential and comes out naturally from the analysis, for discrete-time problems, approximating cost-to-go di!erences rather than cost functions is optional and should be considered in the context of a given problem. Methods along this line include advantage updating, cost shaping, biased aggregation, and the use of baselines, for which we refer to the books [BeT96], [Ber19a], and [Ber20a]. A special method to explicitly approximate cost function di!erences is differential training, which was proposed in the author’s paper [Ber97], and was also discussed in Section 4.3.4 of the book [Ber20a]. 
Unfortunately, approximating cost-to-go di!erences may not be effective when the cost per stage is 0 for all states, while a nonzero cost is incurred only at termination. This type of cost structure occurs, among others, in games such as chess and backgammon. In this case a potentially e!ective remedy is to resort to longer lookahead, either through multistep lookahead minimization, or through some form of truncated rollout, as it is done in the AlphaZero and TD-Gammon programs. 
6.10 EPILOGUE 
While the ideas of approximation in value space, rollout, and PI have a long history, their significance has been highlighted by the success of Alp-haZero, and the earlier but just as impressive TD-Gammon program. Both programs were trained o!-line extensively using sophisticated approximate PI algorithms and neural networks. Yet in AlphaZero, the player obtained o!-line was greatly improved by on-line play, as we have discussed in Chap-ter 1. Moreover, TD-Gammon was greatly improved by supplementing its on-line play scheme with truncated rollout. 
We have argued that this performance enhancement by on-line play defines a new transformative and broadly applicable paradigm for decision and control, which is couched on the AlphaZero/TD-Gammon design principles: on-line decision making, using approximation in value space with multistep lookahead, and rollout. Moreover, this paradigm provides the basis for a much needed unification of the methodological cultures of reinforcement learning, and optimization/control, and particularly MPC, which in fact embodies several of the AlphaZero/TD-Gammon design ideas. 
We have highlighted the multiple beneficial properties of truncated rollout as a reliable, easily implementable, and cost e!ective alternative to
198 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
long lookahead minimization. We have also noted how rollout with a stable policy, enhances the stability properties of the controller obtained by approximation in value space schemes. The issue of stability is of paramount importance in control system design and MPC, but is not addressed adequately by the RL methodology, as practiced by the AI community. 
Moreover, we have argued that there is an additional benefit of policy improvement by approximation in value space, not observed in the context of games (which have unchanging rules and environment). It is well-suited for on-line replanning and changing problem parameters, as in the context of indirect adaptive control. 
Finally, we have discussed various methods to improve the e!ciency of on-line play algorithms by e"ectively extending the length of the multistep lookahead minimization through approximation. These methods include pruning, double rollout, and incremental rollout for deterministic problems, and the use of certainty equivalence after the first step of lookahead minimization for stochastic problems. 
The Mathematical Framework 
From a mathematical point of view, we have aimed to provide the framework and insights, which facilitate the use of on-line decision making on top of o"-line training. In particular, through a unified abstract DP analysis, which is well-suited to visualization, we have shown that the principal ideas of approximation in value space and rollout apply very broadly to deterministic and stochastic optimal control problems, involving both discrete and continuous search spaces. 
A key idea of this work is the interpretation of approximation in value space with one-step lookahead as a step of Newton’s method . This idea has been known for some time, but only within the more restrictive context of policy iteration, where the cost function approximation is restricted to be the cost function of some policy. The extensions of this idea, including more general cost function approximations, multistep lookahead, truncated rollout, connection with stability issues, and discrete and multiagent optimization, which are provided in this work, are new (following their introduction in the book [Ber20a]), and aim to promote the view that Newton’s method and other classical algorithms, such as Newton-SOR, are central conceptual elements of the RL methodology. 
Mathematical proofs of our superlinear convergence rate and sensitivity results were given primarily for the case of a one-dimensional quadratic problem (Chapter 4). However, these results can be straightforwardly extended to more general multidimensional linear quadratic problems. More-over, similar results can be obtained for more general problems, by using the equivalence to a Newton step that we showed in Chapter 3, and by relying on known analyses of nondi"erentiable forms of Newton’s method, which we have discussed in the Appendix and in the paper [Ber22b]. At
Sec. 6.10 Epilogue 199 
the same time considerable work remains to be done to clarify exceptional behaviors of Newton’s method within various DP contexts, and to work out rigorously the associated mathematical results. Furthermore, there is a need for better characterization of the region of attraction of the method in contexts beyond the nice discounted problems with bounded cost per stage. 
A major supplementary idea of this work is the interpretation of o!-line training of policies and cost approximations as means for enhancement of the initial condition of the Newton step. Among others, this interpretation supports the view that the Newton step/on-line player is the key determinant of the overall scheme’s performance, and that the initial condition adjustment/o"-line training plays a subsidiary role. Still, however, while this is a valuable conceptual starting point, we expect that in specific contexts the initial condition of the Newton step and the attendant o"-line training process may play an important role. For example in the MPC context, o"-line training may be critical in dealing with issues of stability, state constraints, and target tube construction. 
We finally note that the preceding mathematical ideas have a universal character in view of their abstract DP foundation, which allows their use in very general DP contexts, involving both discrete and continuous state and control spaces, as well as value and policy approximations. As a result, they can be e"ectively integrated within a broad range of methodologies, such as adaptive control, MPC, decentralized and multiagent control, discrete and Bayesian optimization, neural network-based approximations, and heuristic algorithms for discrete optimization, as we have discussed in greater detail in the books [Ber19a] and [Ber20a]. 
Rollout for Finite-Horizon Problems and Discrete Optimization 
In the present chapter we have noted that while our starting point in this work has been infinite horizon problems, approximation in value space and rollout can be applied to finite horizon problems as well, and can be similarly interpreted in terms of Newton’s method. In particular, finite horizon problems can be converted to infinite horizon stochastic shortest path problems with a termination state that corresponds to the end of the horizon. Once this is done, the conceptual framework of our work can be applied to provide insight on the connections between approximation in value space, rollout, and Newton’s method. 
Thus, our rollout ideas find application beyond the infinite horizon DP context, and apply to the solution of classical discrete and combinatorial optimization problems, as we have aimed to show in this chapter. This was the basis for the original proposal of the use of rollout for discrete and combinatorial optimization problems in the paper by Bertsekas, Tsitsiklis, and Wu [BTW97]; see also the author’s book [Ber20a], which provides a fuller presentation of the finite horizon methodology.
200 Finite Horizon Deterministic Problems - Discrete Optimization Chap. 6 
The book [Ber20a] also contains several examples of application of rollout to discrete optimization and provides references to many works spanning the period from the late 90s to the present. These works discuss variants and problem-specific adaptations of rollout algorithms for a broad variety of practical problems, and consistently report favorable computational experience. The size of the cost improvement over the base policy is often impressive, evidently owing to the fast convergence rate of Newton’s method that underlies rollout. Moreover these works illustrate some of the other important advantages of rollout: reliability, simplicity, suitability for on-line replanning, and the ability to interface with other RL techniques, such as neural network training, which can be used to provide suitable base policies and/or approximations to their cost functions. 
We finally note that in Section 6.5 we have explored yet another use of rollout, as a means for facilitating approximation in value space with long multistep lookahead, by performing expeditiously (yet approximately) the multistep lookahead minimization over the corresponding acyclic lookahead graph. This idea is new and the range of applications of the incremental rollout algorithm as a competitor to Monte Carlo Tree Search and other tree search methods, is very broad.
APPENDIX A: 
Newton’s Method and Error 
Bounds 
Contents 
A.1. Newton’s Method for Di!erentiable Fixed Point . . . . . . Problems . . . . . . . . . . . . . . . . . . . . p. 202 
A.2. Newton’s Method Without Di!erentiability of the . . . . . Bellman Operator . . . . . . . . . . . . . . . . p. 207 
A.3. Local and Global Error Bounds for Approximation in . . . Value Space . . . . . . . . . . . . . . . . . . . p. 210 
A.4. Local and Global Error Bounds for Approximate . . . . . . Policy Iteration . . . . . . . . . . . . . . . . . . p. 212 
201
202 Newton’s Method and Error Bounds Appendix A 
In this appendix, we first develop the classical theory of Newton’s method for solving a fixed point problem of the form 
y = G(y), 
where y is an n-dimensional vector, and G : !n "# !n is a continuously di!erentiable mapping.† We then extend the results to the case where G 
is nondi!erentiable because it is obtained as the minimum of continuously di!erentiable mappings, as in the case of the Bellman operator (cf. Chapter 3). 
The convergence analysis relates to the solution of Bellman’s equation J = TJ , for the case where J is an n-dimensional (there are n states), TJ is real-valued for all real-valued J , and T is either di!erentiable or involves minimization over a finite number of controls. However, the analysis illuminates the mechanism by which Newton’s method works for more general problems, involving for example infinite spaces problems. Moreover, the analysis does not use the concavity and monotonicity properties of T that hold in the DP contexts that we have discussed (discounted, SSP, and nonnegative-cost deterministic problems, cf. Chapter 2), but may not hold in other DP-related contexts. 
A.1 NEWTON’SMETHOD FORDIFFERENTIABLE FIXED POINT PROBLEMS 
Newton’s method is an iterative algorithm that generates a sequence {yk}, starting from some initial vector y0. It aims to obtain asymptotically a fixed point of G, i.e., yk # y!, where y! is such that y! = G(y!). Newton’s method is usually analyzed in the context of solving systems of equations. In particular, by introducing the mapping H : !n "# !n, given by 
H(y) = G(y)$ y, y % !n, 
the fixed point problem is transformed to solving the equation H(y) = 0. We view H(y) as a column vector in !n, with its n components denoted by H1(y), . . . , Hn(y): 
H(y) = 
! 
" 
# 
H1(y) ... 
Hn(y) 
$ 
% 
& 
. 
Each of the functions Hi is given by 
Hi(y) = Gi(y)$ yi, 
† The subsequent analysis of Sections A.1 and A.2 also holds when G maps an open subset Y of !n into itself, i.e., G(y) " Y for all y " Y .
Sec. A.1 Newton’s Method for Di!erentiable Fixed Point Problems 203 
0 0 y H 
y1y0 
y! 
) Region of Attraction 
0 
y1y0 
y! 
) Region of Attraction 
y T 
y T 
) Region of Attraction of y! ) Region of Attraction of y! 
H(y) = G(y)! y Gy G(y) 
Figure A.1 Illustration of Newton’s method for solving the di!erentiable fixed point problem y = G(y), and equivalently, the equation H(y) = 0 where 
H(y) = G(y)! y. 
At each iteration the method first linearizes the problem at the current iterate yk 
via a first order Taylor series expansion, and then computes yk+1 as the solution of the linearized problem. The method converges to a solution y! when started within its region of attraction, i.e, the set of starting points y0 such that 
"yk+1 ! y !" # "yk ! y 
!", and yk $ y ! . 
In this one-dimensional case where G is concave and monotonically increasing, the region of attraction is as shown. 
where yi is the ith component of y and Gi is the ith component of G. Assuming that H is di!erentiable, Newton’s method takes the form 
yk+1 = yk $ ' 
&H(yk)" (#1 
H(yk), (A.1) 
where&H is the n'nmatrix whose columns are the gradients&H1, . . . ,&Hn 
of the n components H1, . . . , Hn, viewed as column vectors: 
&H(y) = ' 
&H1(y) · · · &Hn(y) ( 
, 
and &H(yk)" denotes the transpose of &H(yk) [i.e., &H(yk)" is the Jaco-bian of H at yk]. The algorithm (A.1), illustrated in one dimension in Fig. A.1, is the classical form of Newton’s method , and it assumes that &H(yk) is invertible for every k.† 
Its analysis has two principal aspects: 
† An intuitive view of the Newton iteration is that it first linearizes H at the current point yk via a first order Taylor series expansion, 
H(y) # H(yk) +$H(yk) "(y % yk),
204 Newton’s Method and Error Bounds Appendix A 
(a) Local convergence, which deals with the behavior near a nonsingular solution y!, i.e., one where H(y!) = 0 and the matrix &H(y!) is invertible. 
(b) Global convergence, which addresses modifications that are necessary to ensure that the method is valid and is likely to converge to a solution when started far from all solutions. Such modifications may include changes in the starting point y0 to bring it within the region of convergence (the set of starting points from which convergence to a solution is assured), or changes in the method itself to improve its stability properties. 
Of course there are other questions of interest, which relate to the convergence and rate of convergence aspects of the method. The literature of the subject is very extensive, and is covered in several books and research papers. 
In this appendix, we will only consider local convergence questions, and we will focus on a single nonsingular solution, i.e., a vector y! such that H(y!) = 0 and &H(y!) is invertible. The principal result here is that the Newton method (A.1) converges superlinearly when started close enough to y!. For a simple argument that shows this fact, suppose that the method generates a sequence {yk} that converges to y!. Let us use a first order expansion around yk to write 
0 = H(y!) = H(yk) +&H(yk)"(y! $ yk) + o ' 
(yk $ y!( ( 
. 
and then computes yk+1 as the solution of the linearized system 
H(yk) +$H(yk) "(y % yk) = 0. 
Equivalently, in terms of the original fixed point problem y = G(y), Newton’s method first linearizes G at the current point yk via a first order Taylor series expansion, 
G(y) # G(yk) +$G(yk) "(y % yk), 
where $G(yk) " is the Jacobian matrix of G evaluated at yk. It then computes 
yk+1 as the solution of the linearized fixed point problem 
y = G(yk) +$G(yk) "(y % yk). 
Thus, yk+1 = G(yk) +$G(yk) 
"(yk+1 % yk), 
or, by subtracting yk from both sides and collecting terms, 
' 
I %$G(yk) " ( 
(yk+1 % yk) = G(yk)% yk. 
By using H(y) = G(y)%y, this equation can be written in the form of the Newton iteration (A.1).
Sec. A.1 Newton’s Method for Di!erentiable Fixed Point Problems 205 
By multiplying this relation with ' 
&H(yk)" (#1 
we have 
yk $ y! $ ' 
&H(yk)" (#1 
H(yk) = o ' 
(yk $ y!( ( 
, 
so for the Newton iteration (A.1), we obtain 
yk+1 $ y! = o ' 
(yk $ y!( ( 
. 
Thus, if yk )= y! for all k, 
lim k$% 
(yk+1 $ y!( 
(yk $ y!( = lim 
k$% 
o ' 
(yk $ y!( ( 
(yk $ y!( = 0, 
implying superlinear convergence. This argument can also be used to show convergence to y! if the initial vector y0 is su"ciently close to y!. 
We will prove a more detailed version of this result, which includes a local convergence assertion ({yk} converges to y! when started near y!). 
Proposition A.1: Consider a function H : !n "# !n, and a vector y! 
such that H(y!) = 0. For any ! > 0, we denote by S! the open sphere {x | (y $ y!( < !}, where ( · ( denotes the Euclidean norm. Assume that within some sphere S 
! , H is continuously di!erentiable, &H(y!) 
is invertible, and ) 
) 
) 
' 
&H(y)" (#1 ) 
) 
) is bounded by some scalar B > 0: 
) 
) 
) 
' 
&H(y)" (#1 ) 
) 
) * B, for all y % S!. 
Assume also that for some L > 0, 
) 
)&H(x)$&H(y) ) 
) * L(x$ y(, for all x, y % S!, (A.2) 
Then there exists ! % (0, !] such that if y0 % S!, the sequence {yk} generated by the iteration 
yk+1 = yk $ ' 
&H(yk)" (#1 
H(yk) 
belongs to S!, and converges monotonically to y!, i.e. 
(yk $ y!( # 0, (yk+1 $ y!( * (yk $ y!(, k = 0, 1, . . . . (A.2) 
Moreover, we have 
(yk+1 $ y!( * LB 
2 (yk $ y!(2, k = 0, 1, .... (A.3)
206 Newton’s Method and Error Bounds Appendix A 
Proof: We first note that if yk % S!, by using the relation 
H(yk) = 
* 1 
0 
&H ' 
y! + t(yk $ y!) (" dt(yk $ y!), 
we have 
(yk+1 $ y!( = ) 
) 
) yk $ y! $ 
' 
&H(yk)" (#1 
H(yk) ) 
) 
) 
= 
) 
) 
) 
) 
) 
' 
&H(yk)" (#1 + 
&H(yk)"(yk $ y!)$H(yk) , 
) 
) 
) 
) 
) 
= 
) 
) 
) 
) 
) 
' 
&H(yk)" (#1 
-
&H(yk)" $ 
* 1 
0 
&H ' 
y! + t(yk $ y!) (" dt 
. 
(yk $ y!) 
) 
) 
) 
) 
) 
= 
) 
) 
) 
) 
) 
' 
&H(yk)" (#1 
/ 
* 1 
0 
0 
&H(yk)" $&H ' 
y! + t(yk $ y!) (" 1 
dt 
2 
(yk $ y!) 
) 
) 
) 
) 
) 
* B 
/ 
* 1 
0 
) 
) 
) &H(yk)$&H 
' 
y! + t(yk $ y!) ( 
) 
) 
) dt 
2 
(yk $ y!( 
* B 
-* 1 
0 
Lt(yk $ y!(dt 
. 
(yk $ y!( 
= LB 
2 (yk $ y!(2, 
thus showing Eq. (A.3). Assume that y0 % S ! . By continuity of &H , we 
can take ! % (0, !] such that LB! < 1, so if y0 % S!, from the preceding relation we obtain 
(y1 $ y!( * 1 
2 (y0 $ y!( < 
! 
2 . 
By repeating this argument with y1 in place of y0, we obtain (y2 $ y!( * 1 
2 (y1 $ y!( < ! 
4 , and similarly 
(yk+1 $ y!( * 1 
2 (yk $ y!( < 
! 
2k+1 , k = 0, 1, .... 
The monotonic convergence property (A.2) follows. Q.E.D.
Sec. A.2 Newton’s Method Without Di!erentiability 207 
A.2 NEWTON’S METHOD WITHOUT DIFFERENTIABILITY OF THE BELLMAN OPERATOR 
As we noted in Chapter 3, there has been a lot of work on extensions of Newton’s method for the fixed point problem y = G(y), which relax the di!erentiability requirement on G by using alternative notions from nonsmooth analysis. Relevant works include Josephy [Jos79], Robinson [Rob80], [Rob88], [Rob11], Kojima and Shindo [KoS86], Kummer [Kum88], [Kum00], Pang [Pan90], Qi and Sun [Qi93], [QiS93], Facchinei and Pang [FaP03], Ito and Kunisch [ItK03], Bolte, Daniilidis, and Lewis [BDL09], Dontchev and Rockafellar [DoR14], and additional references cited therein. 
These extensions have strong relevance to our context. In particular, the proof of Prop. A.1 can be simply extended to the case where G is nondi!erentiable and has the minimization structure of the Bellman operator (with finite control space). The idea is that when the kth iterate yk is su"ciently close to the fixed point y! of G, the kth Newton iteration can be viewed as a Newton iteration for some continuously di!erentiable mapping Ĝk, which also has y! as fixed point, and is obtained from G by a minimization operation. Then Prop. A.1, applied to Ĝk, shows that the distance !yk " y!! decreases monotonically at a quadratic rate. 
In the nondi!erentiable case discussed in this appendix, we focus on solution of the equation H(y) = 0 where the mapping H : #n $% #n again has real-valued n components, denoted by H1(y), . . . , Hn(y): 
H(y) = 
! 
" 
# 
H1(y) ... 
Hn(y) 
$ 
% 
& . 
The component mappings H1, . . . , Hn : #n % #, involve minimization over a parameter u (as the notation suggests, the parameter corresponds to control in the DP context), and have the form† 
Hi(y) = min u=1,...,m 
Hi,u(y), i = 1, . . . , n. (A.4) 
The mappings Hi,u : #n % # are given by 
Hi,u(y) = Gi,u(y)" yi, i = 1, . . . , n, u = 1, . . . ,m, 
where Gi,u : #n $% # is a given real-valued function for each i and u, and yi is the ith component of y. Given a vector y! such that H(y!) = 0, we denote by U!(i) & {1, . . . ,m} the set of indexes that attain the minimum in Eq. (A.4) when y = y!: 
U!(i) = arg min u=1,...,m 
Hi,u(y!), i = 1, . . . , n. 
† We focus on this form for simplicity of presentation. The references cited above provide convergence analyses for far more general cases.
208 Newton’s Method and Error Bounds Appendix A 
We assume that within some sphere S! centered at y! with radius !, the mappings Hi,u(·) are continuously di!erentiable for all i and u % U!(i), while all the n' n matrices with columns 
&H1,u1 (y), . . . ,&Hn,un 
(y), 
are invertible, where for every i, ui can take any value from the set U!(i). Thus all the Jacobian matrices of the mappings, which correspond to (u1, . . . , un) that are “active” at y! [i.e., ui % U!(i) for all i], are assumed invertible. 
Given the iterate yk, Newton’s method operates as follows: It finds for each i = 1, . . . , n, the set of indexes U(i, k) + {1, . . . ,m} that attain the minimum in Eq. (A.4) when y = yk: 
U(i, k) = arg min u=1,...,m 
Hi,u(yk). 
Then it generates the next iterate yk+1 with the following three steps: 
(a) It selects arbitrarily an index u(i, k) from within U(i, k), for each i = 1, . . . , n. 
(b) It forms the n' n matrix 
Mk = ' 
&H1,u(1,k)(yk) · · · &Hn,u(n,k)(yk) ( 
, 
that has columns &H1,u(1,k)(yk), . . . ,&Hn,u(n,k)(yk), and the column vector 
Gk = 
! 
" 
# 
H1,u(1,k)(yk) ... 
Hn,u(n,k)(yk) 
$ 
% 
& 
that has components H1,u(1,k)(yk), . . . , Hn,u(n,k)(yk): 
(c) It sets yk+1 = yk $ (M " 
k) #1Gk. (A.5) 
For our convergence proof, we argue as follows: When the iterate yk 
is su"ciently near to y!, the index set U(i, k) is a subset of U!(i) for each i = 1, . . . , n; see Fig. A.2 for a case where n = 1 and m = 3. The reason is that there exists an " > 0 such that for all i = 1, . . . , n and u = 1, . . . ,m, 
u /% U!(i) , Hi,u(y!) - ". 
Therefore, there is a sphere centered at y! such that for all yk within that sphere and all i, we have 
u /% U!(i) , Hi,u(yk) - "/2,
Sec. A.2 Newton’s Method Without Di!erentiability 209 
y! 
y H1(y) 
) H2(y) 
0 
0 y H 
) H3(y) 
H(y) = min ! 
H1(y), H2(y), H3(y) " 
y0 y1 
) Region of Attraction ) Region of Attraction of y! 
Figure A.2 Illustration of a one-dimensional nondi!erentiable equation 
H(y) = 0, 
where H is obtained by minimization of three di!erentiable mappings H1,H2,H3: 
H(y) = min 3 
H1(y), H2(y), H3(y) 4 
, y % &. 
Here m = 3 and n = 1 [so the index i is omitted from U!(i) and U(i, k)]. At the solution y!, the index set U! consists of u = 1 and u = 2, and for yk '= y!, we have U(k) = {1} or U(k) = {2}. Newton’s method applied to H consists of a Newton iteration applied to H1 when y < y! and |y ! y!| is small enough, and consists of a Newton iteration applied to H2 when y > y!. Since at y! we have 
H1(y !) = H2(y 
!) = 0, 
both iterations, at y < y! and at y > y!, approach y! superlinearly. 
and u % U!(i) , Hi,u(yk) < "/2, 
which implies that if u /% U!(i) then u /% U(i, k), or equivalently U(i, k) + U!(i). It follows that the iteration (A.5) can be viewed as a Newton iteration applied to a system of di!erentiable equations that has y! as its solution. This system is 
Hi,u(i,k)(y) = 0, i = 1, . . . , n, 
and corresponds to the set of indexes 
u(1, k), . . . , u(n, k).
210 Newton’s Method and Error Bounds Appendix A 
Thus, near y!, by Prop. A.1, the iteration (A.5) is attracted at a quadratic rate to y! regardless of which indexes u(i, k) % U(i, k) are selected for iteration k. 
Finally, note that while the sphere within which U(i, k) + U!(i) for all i was constructed for a single iteration k, we can take the sphere small enough to ensure that the distance from the current iterate to y! is reduced for all subsequent iterations, similar to the proof of Prop. A.1. We can thus conclude that after yk gets close enough to y!, each subsequent iteration is a Newton step applied to one of a finite number of di!erentiable systems of equations that have y! as their common solution, and for which the convergence properties of Prop. A.1 hold. 
A.3 LOCAL AND GLOBAL ERROR BOUNDS FOR APPROXIMATION IN VALUE SPACE 
In approximation in value space, an important analytical issue is to quantify the level of suboptimality of the one-step or multistep lookahead policy obtained. In this section, we focus on an #-step lookahead scheme that produces a policy µ̃ according to 
Tµ̃T "#1J̃ = T "J̃ , 
where J̃ is the terminal cost function approximation. We will try to estimate the di!erence Jµ̃ $ J*, where Jµ̃ is the cost function of µ̃ and J* is the optimal cost function, assuming that T "#1J̃ lies within the region of stability, so that µ̃ is well-defined as a stable policy and Jµ̃ is finite-valued. 
There is a classical error bound for the case where the Bellman operator T is a contraction mapping with respect to the sup-norm ((J( = supx&X |J(x)|) with modulus $ % (0, 1). It is given by 
(Jµ̃ $ J*( * 2$ 
1$ $ (T "#1J̃ $ J*(; (A.6) 
see [Ber19a], Prop. 5.1.1, for the finite-state discounted case, and [Ber22a], Section 2.2, for more general abstract DP cases. This bound also applies to the case where T is a contraction over a subset J of functions, as long as T maps J into itself. 
Unfortunately, however, this error bound is very conservative, and does not reflect practical reality. The reason is that this is a global error bound, i.e., it holds for all J̃ , even the worst possible. In practice, J̃ is often chosen su"ciently close to J*, so that the error Jµ̃ $ J* behaves consistently with the convergence rate of the Newton step that starts at T "#1J̃ , which is superlinear. In other words, for J̃ relatively close to J*, we have the local estimate 
(Jµ̃ $ J*( = o ' 
(T "#1J̃ $ J*( ( 
. (A.7)
Sec. A.3 Error Bounds for Approximation in Value Space 211 
In practical terms, there is often a huge di!erence, both quantitative and qualitative, between the error bounds (A.6) and (A.7), as illustrated by the following example. 
Example A.3.1 (One-Dimensional Linear Quadratic Problem) 
Consider an undiscounted one-dimensional linear quadratic problem such as the one considered in Chapter 4. The system is 
xk+1 = axk + buk, 
and the cost per stage is qx2 
k + ru2 k. 
We will consider one-step lookahead (! = 1), and a quadratic cost function approximation 
J̃(x) = K̃x2, 
with K̃ within the region of stability, which is some open interval of the form (S,!). As in Chapter 4, the Riccati operator is 
F (K) = a2rK 
r + b2K + q, 
and the one-step lookahead policy µ̃ has cost function 
Jµ̃(x) = Kµ̃x 2, 
where Kµ̃ is obtained by applying one step of Newton’s method for solving the Riccati equation K = F (K), starting at K = K̃. 
Let S be the boundary of the region of stability, i.e., the value of K at which the derivative of F with respect to K is equal to 1: 
"F (K) 
"K 
! 
! 
! 
K=S = 1. 
Then the Riccati operator F is a contraction within any interval [S,!) with S > S, with a contraction modulus # that depends on S. In particular, # is given by 
# = "F (K) 
"K 
! 
! 
! 
K=S 
and satisfies 0 < # < 1 because S > S, and the derivative of F is positive and monotonically decreasing to 0 as K increases to !. 
The error bound (A.6) can be rederived for the case of quadratic functions and can be rewritten in terms of quadratic cost coe!cients as 
Kµ̃ "K! # 2# 
1" # |K̃ "K!|, (A.8) 
where Kµ̃ is the quadratic cost coe!cient of the lookahead policy µ̃ [and also the result of a Newton step for solving the fixed point Riccati equation
212 Newton’s Method and Error Bounds Appendix A 
1 2 3 4 5 6 7 8 9 0 
5 
10 
15 
Line Global error bound Actual error 
Line Global error bound Actual error 
Figure A.3 Illustration of the global error bound (A.8) for the one-step lookahead error Kµ̃ ! K! as a function of K̃, compared with the true error obtained by one step of Newton’s method starting from K̃. 
The problem data are a = 2, b = 2, q = 1, and r = 5. With these numerical values, we have K! = 5 and the region of stability is (S,() with S = 1.25. The modulus of contraction ! used in the figure is computed at S = S + 0.5. Depending on the chosen value of S, ! can be arbitrarily close to 1, but decreases as S increases. Note that the error Kµ̃ ! K! is much smaller when K̃ is larger than K! than when it is lower, because the slope of F diminishes as K increases. This is not reflected by the global error bound (A.8). 
F = F (K) starting from K̃]. A plot of (Kµ̃%K!) as a function of K̃, compared with the bound on the right side of this equation is shown in Fig. A.3. It can be seen that (Kµ̃%K!) exhibits the qualitative behavior of Newton’s method, which is very di!erent than the bound (A.8). An interesting fact is that the bound (A.8) depends on !, which in turn depends on how close K̃ is to the boundary S of the region of stability, while the local behavior of Newton’s method is independent of S. 
A.4 LOCAL AND GLOBAL ERROR BOUNDS FOR APPROXIMATE POLICY ITERATION 
In an approximate PI method that generates a sequence of policies {µk}, it is important to estimate the asymptotic error 
lim sup k$% 
(Jµk $ J*(.
Sec. A.4 Error Bounds for Approximate Policy Iteration 213 
In this section we will consider the case where the policy evaluation step is approximate, while the policy improvement step is exact (so that it is equivalent to a Newton step for solving the Bellman equation J = TJ). In particular, we focus on a method that generates a sequence of policies {µk} and a corresponding sequence of approximate cost functions {Jk} satisfying 
Tµk+1Jk = TJk, (Jk+1 $ Jµk+1( * !, k = 0, 1, . . . , 
for some ! > 0. Here J0 is some initial cost function approximation, µ1 
is the first policy, obtained from J0 by a one-step lookahead/Newton step, and ! is some scalar quantifying the level of approximation in the policy evaluation step (i.e., replacing Jµ1 with J1, and more generally replacing Jµk+1 with Jk+1). 
A prerequisite for this method to be well defined is that the generated sequence {Jk} stays within the region of stability of the problem, since otherwise the policy improvement step, Tµk+1Jk = TJk, is not well-defined. This di"culty does not arise in problems where T is a contraction mapping, such as in discounted problems with bounded cost per stage, but suggests that in general the size of ! should be small enough to bring Jk relatively close to J*, and keep it close. 
For the remainder of this section, we assume that T is a contraction mapping with modulus $ % (0, 1). The main global error bound for approximate PI under this assumption is 
lim sup k$% 
(Jµk $ J*( * 2$! 
(1$ $)2 . (A.9) 
It was first given in the book [BeT96] for finite-state discounted problems, and a proof that applies to general abstract DP mappings was given in the book [Ber22a], Section 2.4.1. The essence of the proof is the following inequality, which quantifies the amount of approximate policy improvement at each iteration: 
(Jµk+1 $ J*( * $(Jµk $ J*(+ 2$! 
1$ $ . 
It states that the error is reduced geometrically by a factor $, plus an additive constant term 2#! 
1## , which over time accumulates to 2#! (1##)2 
. 
Unfortunately, the error bound (A.9) is very conservative, and does not reflect practical reality. In applications of approximate PI, the iterates Jk often get su"ciently close to J*, for the error Jµk+1 $ J* to have the superlinear convergence rate of Newton’s method: 
(Jµk+1 $ J*( = o ' 
(Jk $ J*( ( 
. 
This suggests that Jµk+1 $ J* converges to a neighborhood of J* of size O(!) once (Jk$J*( becomes small. An extreme manifestation of this arises
214 Newton’s Method and Error Bounds Appendix A 
when the number of policies is finite, in which case J* is piecewise linear, as in the case of a finite-spaces $-discounted problem. Then it can be shown that once (Jk $ J*( becomes su"ciently small, approximate policy iteration produces an optimal policy at the next iteration, a property not captured by the global error bound (A.9). A related property is that when the number of policies is finite and ! is su"ciently small, then approximate policy iteration produces an optimal policy in a finite number of iterations, something that is also not captured by Eq. (A.9). 
For another view of this phenomenon, let us use the triangle inequality and the definition of ! as a bound of the policy evaluation error to write 
(Jk+1 $ J*( * (Jµk+1 $ J*(+ (Jk+1 $ Jµk+1( * (Jµk+1 $ J*(+ !, 
which in view of the superlinear convergence rate of Newton’s method, (Jµk+1 $ J*( = o 
' 
(Jk $ J*( ( 
, yields 
(Jk+1 $ J*( * o ' 
(Jk $ J*( ( 
+ !. (A.10) 
This relation suggests again that once Jk gets within a neighborhood of size that is comparable to !, it tends to stay within that neighborhood. As an indication of this, note that when T is linear, then the o 
' 
(Jk $ J*( ( 
term in Eq. (A.10) is equal to 0, so the error bound becomes 
(Jk+1 $ J*( * !, 
regardless of the modulus of contraction $. Moreover, the same is true when T is piecewise linear and ! is su"ciently small. We can also argue that a similar behavior occurs within a small neighborhood of J! when ! is small, but a detailed analysis will not be presented here. Instead, we will illustrate the behavior of the error Jµk+1$J* for linear quadratic problems. 
Example A.4.1 (Approximate PI for a One-Dimensional Linear Quadratic Problem) 
We consider the linear quadratic problem of Example A.3.1, and the approximate PI algorithm with approximate policy evaluation within ", in the sense that 
|Kk %K µ k | & ". 
We will compute the asymptotic error 
lim sup k#$ 
(K µ k %K!), (A.11) 
as a function of ", and we will then compare it to the version of the global error bound (A.9) for linear quadratic problems, which takes the form 
lim sup k#$ 
(K µ k %K!) & 
2!" (1% !)2 
, (A.12) 
with ! being a suitable contraction modulus. Figure A.4 provides the comparison for the same problem data, a = 2, 
b = 2, q = 1, and r = 5, as in Fig. A.3. Note that the true error is roughly equal to " as suggested by the discussion that precedes the present example.
Sec. A.4 Error Bounds for Approximate Policy Iteration 215 
0 0.1 0.2 0.3 0.4 0.5 0 
1 
2 
3 
4 
5 
6 
7 
8 
Line Global error bound Actual error 
Line Global error bound Actual error 
Figure A.4 Illustration of the asymptotic global error bound (A.9) for PI with approximate policy evaluation as a function of !, compared with the true asymptotic error. 
Exact Convergence Property of Approximation in Value Space 
An interesting result, given as Prop. 2.3.1 of the abstract DP book [Ber22a], is that when there are a finite number of policies and the Bellman operator is a contraction, there is a neighborhood N! of the unique solution of Bellman’s equation such that one-step lookahead minimization with an approximate cost function that lies within N!, yields an optimal policy, that is, 
J ' N! and TµJ = TJ ( Jµ = J!. (A.13) 
To visualize this result, one may think of a finite-state discounted problem, in which case the Bellman operator T is piecewise linear, i.e., the function (TJ)(x) is a piecewise linear function of J (cf. Fig. A.2). 
There is a simple extension of this result to approximation in value space with multistep lookahead. It states that for any J , there exists an integer ! such that 
TµT !"1J = T !J ( Jµ = J!. 
The proof follows by replacing J with T !"1J in Eq. (2.13), and by using the convergence property of VI when T is a contraction. In words, the multistep lookahead policy is exactly optimal provided the lookahead is long enough. The required value of ! depends on the cost function approximation J .
References 
[ADB17] Arulkumaran, K., Deisenroth, M. P., Brundage, M., and Bharath, A. A., 2017. “A Brief Survey of Deep Reinforcement Learning,” arXiv preprint arXiv:1708.05866. 
[Arg08] Argyros, I. K., 2008. Convergence and Applications of Newton-Type Iterations, Springer, N. Y. 
[AsH95] Aström, K. J., and Hagglund, T., 1995. PID Controllers: Theory, Design, and Tuning, Instrument Society of America, Research Triangle Park, NC. 
[AsH06] Aström, K. J., and Hagglund, T., 2006. Advanced PID Control, Instru-ment Society of America, Research Triangle Park, N. C. 
[AsW08] Aström, K. J., and Wittenmark, B., 2008. Adaptive Control, Dover Books; also Prentice-Hall, Englewood Cli↵s, N. J, 1994. 
[BBB22] Bhambri, S., Bhattacharjee, A., and Bertsekas, D. P., 2022. “Reinforce-ment Learning Methods for Wordle: A POMDP/Adaptive Control Approach,” arXiv preprint arXiv:2211.10298. 
[BBD10] Busoniu, L., Babuska, R., De Schutter, B., and Ernst, D., 2010. Rein-forcement Learning and Dynamic Programming Using Function Approximators, CRC Press, N. Y. 
[BBM17] Borrelli, F., Bemporad, A., and Morari, M., 2017. Predictive Control for Linear and Hybrid Systems, Cambridge Univ. Press, Cambridge, UK. 
[BBS95] Barto, A. G., Bradtke, S. J., and Singh, S. P., 1995. “Real-Time Learn-ing and Control Using Asynchronous Dynamic Programming,” Artificial Intelli-gence, Vol. 72, pp. 81-138. 
[BDL09] Bolte, J., Daniilidis, A., and Lewis, A., 2009. “Tame Functions are Semismooth,” Math. Programming, Vol. 117, pp. 5-19. 
[BDT18] Busoniu, L., de Bruin, T., Tolic, D., Kober, J., and Palunko, I., 2018. “Reinforcement Learning for Control: Performance, Stability, and Deep Approx-imators,” Annual Reviews in Control, Vol. 46, pp. 8-28. 
[BKB20] Bhattacharya, S., Kailas, S., Badyal, S., Gil, S., and Bertsekas, D. P., 2020. “Multiagent Rollout and Policy Iteration for POMDP with Application to Multi-Robot Repair Problems,” in Proc. of Conference on Robot Learning (CoRL); also arXiv preprint, arXiv:2011.04222. 
[BLW91] Bittanti, S., Laub, A. J., and Willems, J. C., eds., 2012. The Riccati Equation, Springer. 
217
218 References 
[BMZ09] Bokanowski, O., Maroso, S., and Zidani, H., 2009. “Some Convergence Results for Howard’s Algorithm,” SIAM J. on Numerical Analysis, Vol. 47, pp. 3001-3026. 
[BPW12] Browne, C., Powley, E., Whitehouse, D., Lucas, L., Cowling, P. I., Rohlfshagen, P., Tavener, S., Perez, D., Samothrakis, S., and Colton, S., 2012. “A Survey of Monte Carlo Tree Search Methods,” IEEE Trans. on Computational Intelligence and AI in Games, Vol. 4, pp. 1-43. 
[BSW99] Beard, R. W., Saridis, G. N., and Wen, J. T., 1998. “Approximate Solutions to the Time-Invariant Hamilton-Jacobi-Bellman Equation,” J. of Op-timization Theory and Applications, Vol. 96, pp. 589-626. 
[BTW97] Bertsekas, D. P., Tsitsiklis, J. N., and Wu, C., 1997. “Rollout Algo-rithms for Combinatorial Optimization,” Heuristics, Vol. 3, pp. 245-262. 
[BeC99] Bertsekas, D. P., and Castañon, D. A., 1999. “Rollout Algorithms for Stochastic Scheduling Problems,” Heuristics, Vol. 5, pp. 89-108. 
[BeI96] Bertsekas, D. P., and Io↵e, S., 1996. “Temporal Di↵erences-Based Policy Iteration and Applications in Neuro-Dynamic Programming,” Lab. for Info. and Decision Systems Report LIDS-P-2349, MIT, Cambridge, MA. 
[BeK65] Bellman, R., and Kalaba, R. E., 1965. Quasilinearization and Nonlinear Boundary-Value Problems, Elsevier, N.Y. 
[BeR71] Bertsekas, D. P., and Rhodes, I. B., 1971. “On the Minimax Reachability of Target Sets and Target Tubes,” Automatica, Vol. 7, pp. 233-247. 
[BeS78] Bertsekas, D. P., and Shreve, S. E., 1978. Stochastic Optimal Control: The Discrete Time Case, Academic Press, N. Y.; republished by Athena Scientific, Belmont, MA, 1996 (can be downloaded from the author’s website). 
[BeT89] Bertsekas, D. P., and Tsitsiklis, J. N., 1989. Parallel and Distributed Computation: Numerical Methods, Prentice-Hall, Engl. Cli↵s, N. J. (can be downloaded from the author’s website). 
[BeT96] Bertsekas, D. P., and Tsitsiklis, J. N., 1996. Neuro-Dynamic Program-ming, Athena Scientific, Belmont, MA. 
[BeT08] Bertsekas, D. P., and Tsitsiklis, J. N., 2008. Introduction to Probability, 2nd Edition, Athena Scientific, Belmont, MA. 
[BeY10] Bertsekas, D. P., and Yu, H., 2010. “Distributed Asynchronous Policy Iteration in Dynamic Programming,” Proc. of Allerton Conf. on Communication, Control and Computing, Allerton Park, Ill, pp. 1368-1374. 
[BeY12] Bertsekas, D. P., and Yu, H., 2012. “Q-Learning and Enhanced Policy Iteration in Discounted Dynamic Programming,” Math. of Operations Research, Vol. 37, pp. 66-94. 
[BeY16] Bertsekas, D. P., and Yu, H., 2016. “Stochastic Shortest Path Problems Under Weak Conditions,” Lab. for Information and Decision Systems Report LIDS-2909, Massachusetts Institute of Technology. 
[Bea95] Beard, R. W., 1995. Improving the Closed-Loop Performance of Nonlin-ear Systems, Ph.D. Thesis, Rensselaer Polytechnic Institute. 
[Bel57] Bellman, R., 1957. Dynamic Programming, Princeton University Press, Princeton, N. J. 
[Ber71] Bertsekas, D. P., 1971. “Control of Uncertain SystemsWith a Set-Member-ship Description of the Uncertainty,” Ph.D. Thesis, Massachusetts Institute of Technology, Cambridge, MA (can be downloaded from the author’s website).
References 219 
[Ber72] Bertsekas, D. P., 1972. “Infinite Time Reachability of State Space Regions by Using Feedback Control,” IEEE Trans. Automatic Control, Vol. AC-17, pp. 604-613. 
[Ber82] Bertsekas, D. P., 1982. “Distributed Dynamic Programming,” IEEE Trans. Aut. Control, Vol. AC-27, pp. 610-616. 
[Ber83] Bertsekas, D. P., 1983. “Asynchronous Distributed Computation of Fixed Points,” Math. Programming, Vol. 27, pp. 107-120. 
[Ber97] Bertsekas, D. P., 1997. “Di↵erential Training of Rollout Policies,” Proc. of the 35th Allerton Conference on Communication, Control, and Computing, Allerton Park, Ill. 
[Ber05] Bertsekas, D. P., 2005. “Dynamic Programming and Suboptimal Control: A Survey from ADP to MPC,” European J. of Control, Vol. 11, pp. 310-334. 
[Ber11] Bertsekas, D. P., 2011. “Approximate Policy Iteration: A Survey and Some New Methods,” J. of Control Theory and Applications, Vol. 9, pp. 310-335. 
[Ber12] Bertsekas, D. P., 2012. Dynamic Programming and Optimal Control, Vol. II, 4th Ed., Athena Scientific, Belmont, MA. 
[Ber15] Bertsekas, D. P., 2015. “Lambda-Policy Iteration: A Review and a New Implementation,” arXiv preprint arXiv:1507.01029. 
[Ber16] Bertsekas, D. P., 2016. Nonlinear Programming, Athena Scientific, Bel-mont, MA. 
[Ber17a] Bertsekas, D. P., 2017. Dynamic Programming and Optimal Control, Vol. I, 4th Ed., Athena Scientific, Belmont, MA. 
[Ber17b] Bertsekas, D. P., 2017. “Value and Policy Iteration in Deterministic Optimal Control and Adaptive Dynamic Programming,” IEEE Trans. on Neural Networks and Learning Systems, Vol. 28, pp. 500-509. 
[Ber17c] Bertsekas, D. P., 2017. “Regular Policies in Abstract Dynamic Program-ming,” SIAM J. on Optimization, Vol. 27, pp. 1694-1727. 
[Ber18a] Bertsekas, D. P., 2018. Abstract Dynamic Programming, 2nd Ed., Athena Scientific, Belmont, MA (can be downloaded from the author’s website). 
[Ber18b] Bertsekas, D. P., 2018. “Feature-Based Aggregation and Deep Rein-forcement Learning: A Survey and Some New Implementations,” Lab. for In-formation and Decision Systems Report, MIT; arXiv preprint arXiv:1804.04577; IEEE/CAA Journal of Automatica Sinica, Vol. 6, 2019, pp. 1-31. 
[Ber18c] Bertsekas, D. P., 2018. “Biased Aggregation, Rollout, and Enhanced Pol-icy Improvement for Reinforcement Learning,” Lab. for Information and Decision Systems Report, MIT; arXiv preprint arXiv:1910.02426. 
[Ber18d] Bertsekas, D. P., 2018. “Proximal Algorithms and Temporal Di↵erence Methods for Solving Fixed Point Problems,” Computational Optimization and Applications, Vol. 70, pp. 709-736. 
[Ber19a] Bertsekas, D. P., 2019. Reinforcement Learning and Optimal Control, Athena Scientific, Belmont, MA. 
[Ber19b] Bertsekas, D. P., 2019. “Multiagent Rollout Algorithms and Reinforce-ment Learning,” arXiv preprint arXiv:1910.00120. 
[Ber19c] Bertsekas, D. P., 2019. “Constrained Multiagent Rollout and Multidi-mensional Assignment with the Auction Algorithm,” arXiv preprint, arxiv.org/-abs/2002.07407.
220 References 
[Ber19d] Bertsekas, D. P., 2019. “Robust Shortest Path Planning and Semicon-tractive Dynamic Programming,” Naval Research Logistics, Vol. 66, pp. 15-37. 
[Ber20a] Bertsekas, D. P., 2020. Rollout, Policy Iteration, and Distributed Rein-forcement Learning, Athena Scientific, Belmont, MA. 
[Ber20b] Bertsekas, D. P., 2020. “Multiagent Value Iteration Algorithms in Dy-namic Programming and Reinforcement Learning,” Results in Control and Op-timization J., Vol. 1, 2020. 
[Ber21a] Bertsekas, D. P., 2021. “On-Line Policy Iteration for Infinite Horizon Dynamic Programming,” arXiv preprint arXiv:2106.00746. 
[Ber21b] Bertsekas, D. P., 2021. “Multiagent Reinforcement Learning: Rollout and Policy Iteration,” IEEE/ CAA J. of Automatica Sinica, Vol. 8, pp. 249-271. 
[Ber21c] Bertsekas, D. P., 2021. “Distributed Asynchronous Policy Iteration for Sequential Zero-Sum Games and Minimax Control,” arXiv preprint arXiv:2107.-10406. 
[Ber22a] Bertsekas, D. P., 2022. Abstract Dynamic Programming, 3rd Edition, Athena Scientific, Belmont, MA (can be downloaded from the author’s website). 
[Ber22b] Bertsekas, D. P., 2022. “Newton’s Method for Reinforcement Learning and Model Predictive Control,” Results in Control and Optimization J., Vol. 7, 2022, pp. 100-121. 
[Ber22c] Bertsekas, D. P., 2022. “Rollout Algorithms and Approximate Dynamic Programming for Bayesian Optimization and Sequential Estimation,” arXiv preprint arXiv:2212.07998v3. 
[Bit91] Bittanti, S., 1991. “Count Riccati and the Early Days of the Riccati Equation,” in The Riccati Equation (pp. 1-10), Springer. 
[Bla65] Blackwell, D., 1965. “Positive Dynamic Programming,” Proc. Fifth Berke-ley Symposium Math. Statistics and Probability, pp. 415-418. 
[BoV79] Borkar, V., and Varaiya, P. P., 1979. “Adaptive Control of Markov Chains, I: Finite Parameter Set,” IEEE Trans. Automatic Control, Vol. AC-24, pp. 953-958. 
[Bod20] Bodson, M., 2020. Adaptive Estimation and Control, Independently Pub-lished. 
[Bor08] Borkar, V. S., 2008. Stochastic Approximation: A Dynamical Systems Viewpoint, Cambridge Univ. Press. 
[Bor09] Borkar, V. S., 2009. “Reinforcement Learning: A Bridge Between Nu-merical Methods and Monte Carlo,” in World Scientific Review, Vol. 9, Ch. 4. 
[Bra21] Brandimarte, P., 2021. From Shortest Paths to Reinforcement Learning: A MATLAB-Based Tutorial on Dynamic Programming, Springer. 
[CFH13] Chang, H. S., Hu, J., Fu, M. C., and Marcus, S. I., 2013. Simulation-Based Algorithms for Markov Decision Processes, 2nd Edition, Springer, N. Y. 
[CaB07] Camacho, E. F., and Bordons, C., 2007. Model Predictive Control, 2nd Ed., Springer, New York, N. Y. 
[Cao07] Cao, X. R., 2007. Stochastic Learning and Optimization: A Sensitivity-Based Approach, Springer, N. Y. 
[DNP11] Deisenroth, M. P., Neumann, G., and Peters, J., 2011. “A Survey on Policy Search for Robotics,” Foundations and Trends in Robotics, Vol. 2, pp. 1-142. 
[DeF04] De Farias, D. P., 2004. “The Linear Programming Approach to Approxi-
References 221 
mate Dynamic Programming,” in Learning and Approximate Dynamic Program-ming, by J. Si, A. Barto, W. Powell, and D. Wunsch, (Eds.), IEEE Press, N. Y. 
[DoS80] Doshi, B., and Shreve, S., 1980. “Strong Consistency of a Modified Max-imum Likelihood Estimator for Controlled Markov Chains,” J. of Applied Prob-ability, Vol. 17, pp. 726-734. 
[DoR14] Dontchev, A. L., and Rockafellar, R. T., 2014. Implicit Functions and Solution Mappings, 2nd Edition, Springer, N. Y. 
[FaP03] Facchinei, F., and Pang, J.-S., 2003. Finite-Dimensional Variational In-equalities and Complementarity Problems, Vols I and II, Springer, N. Y. 
[FeS04] Ferrari, S., and Stengel, R. F., 2004. “Model-Based Adaptive Critic De-signs,” in Learning and Approximate Dynamic Programming, by J. Si, A. Barto, W. Powell, and D. Wunsch, (Eds.), IEEE Press, N. Y. 
[GBL12] Grondman, I., Busoniu, L., Lopes, G. A. D., and Babuska, R., 2012. “A Survey of Actor-Critic Reinforcement Learning: Standard and Natural Policy Gradients,” IEEE Trans. on Systems, Man, and Cybernetics, Part C, Vol. 42, pp. 1291-1307. 
[GSD06] Goodwin, G., Seron, M. M., and De Dona, J. A., 2006. Constrained Control and Estimation: An Optimisation Approach, Springer, N. Y. 
[GoS84] Goodwin, G. C., and Sin, K. S. S., 1984. Adaptive Filtering, Prediction, and Control, Prentice-Hall, Englewood Cli↵s, N. J. 
[Gos15] Gosavi, A., 2015. Simulation-Based Optimization: Parametric Optimiza-tion Techniques and Reinforcement Learning, 2nd Edition, Springer, N. Y. 
[HWL21] Ha, M., Wang, D., and Liu, D., 2021. “O✏ine and Online Adaptive Critic Control Designs With Stability Guarantee Through Value Iteration,” IEEE Transactions on Cybernetics. 
[HaR21] Hardt, M.. and Recht, B., 2021. Patterns, Predictions, and Actions: A Story About Machine Learning, arXiv preprint arXiv:2102.05242. 
[Hay08] Haykin, S., 2008. Neural Networks and Learning Machines, 3rd Ed., Prentice-Hall, Englewood-Cli↵s, N. J. 
[Hew71] Hewer, G., 1971. “An Iterative Technique for the Computation of the Steady State Gains for the Discrete Optimal Regulator,” IEEE Trans. on Auto-matic Control, Vol. 16, pp. 382-384. 
[Hey17] Heydari, A., 2017. “Stability Analysis of Optimal Adaptive Control Un-der Value Iteration Using a Stabilizing Initial Policy,” IEEE Trans. on Neural Networks and Learning Systems, Vol. 29, pp. 4522-4527. 
[Hey18] Heydari, A., 2018. “Stability Analysis of Optimal Adaptive Control Using Value Iteration with Approximation Errors,” IEEE Transactions on Automatic Control, Vol. 63, pp. 3119-3126. 
[Hyl11] Hylla, T., 2011. Extension of Inexact Kleinman-Newton Methods to a General Monotonicity Preserving Convergence Theory, Ph.D. Thesis, Univ. of Trier. 
[IoS96] Ioannou, P. A., and Sun, J., 1996. Robust Adaptive Control, Prentice-Hall, Englewood Cli↵s, N. J. 
[ItK03] Ito, K., and Kunisch, K., 2003. “Semi-Smooth Newton Methods for Vari-ational Inequalities of the First Kind,” Mathematical Modelling and Numerical Analysis, Vol. 37, pp. 41-62.
222 References 
[JiJ17] Jiang, Y., and Jiang, Z. P., 2017. Robust Adaptive Dynamic Program-ming, J. Wiley, N. Y. 
[Jos79] Josephy, N. H., 1979. “Newton’s Method for Generalized Equations,” Wisconsin Univ-Madison, Mathematics Research Center Report No. 1965. 
[KAC15] Kochenderfer, M. J., with Amato, C., Chowdhary, G., How, J. P., Davison Reynolds, H. J., Thornton, J. R., Torres-Carrasquillo, P. A., Ore, N. K., Vian, J., 2015. Decision Making under Uncertainty: Theory and Application, MIT Press, Cambridge, MA. 
[KKK95] Krstic, M., Kanellakopoulos, I., Kokotovic, P., 1995. Nonlinear and Adaptive Control Design, J. Wiley, N. Y. 
[KKK20] Kalise, D., Kundu, S., and Kunisch, K., 2020. “Robust Feedback Con-trol of Nonlinear PDEs by Numerical Approximation of High-Dimensional Hamil-ton-Jacobi-Isaacs Equations.” SIAM J. on Applied Dynamical Systems, Vol. 19, pp. 1496-1524. 
[KLM96] Kaelbling, L. P., Littman, M. L., and Moore, A. W., 1996. “Reinforce-ment Learning: A Survey,” J. of Artificial Intelligence Res., Vol. 4, pp. 237-285. 
[KeG88] Keerthi, S. S., and Gilbert, E. G., 1988. “Optimal Infinite-Horizon Feed-back Laws for a General Class of Constrained Discrete-Time Systems: Stability and Moving-Horizon Approximations,” J. Optimization Theory Appl., Vo. 57, pp. 265-293. 
[Kle67] Kleinman, D. L., 1967. Suboptimal Design of Linear Regulator Systems Subject to Computer Storage Limitations, Doctoral dissertation, M.I.T., Elec-tronic Systems Lab., Rept. 297. 
[Kle68] Kleinman, D. L., 1968. “On an Iterative Technique for Riccati Equation Computations,” IEEE Trans. Automatic Control, Vol. AC-13, pp. 114-115. 
[KoC16] Kouvaritakis, B., and Cannon, M., 2016. Model Predictive Control: Classical, Robust and Stochastic, Springer, N. Y. 
[KoS86] Kojima, M., and Shindo, S., 1986. “Extension of Newton and Quasi-Newton Methods to Systems of PC1 Equations,” J. of the Operations Research Society of Japan, Vol. 29, pp. 352-375. 
[Kok91] Kokotovic, P. V., ed., 1991. Foundations of Adaptive Control, Springer. 
[Kor90] Korf, R. E., 1990. “Real-Time Heuristic Search,” Artificial Intelligence, Vol. 42, pp. 189-211. 
[Kri16] Krishnamurthy, V., 2016. Partially Observed Markov Decision Processes, Cambridge Univ. Press. 
[Kum88] Kummer, B., 1988. “Newton’s Method for Non-Di↵erentiable Func-tions,” Mathematical Research, Vol. 45, pp. 114-125. 
[Kum00] Kummer, B., 2000. “Generalized Newton and NCP-methods: Conver-gence, Regularity, Actions,” Discussiones Mathematicae, Di↵erential Inclusions, Control and Optimization, Vol. 2, pp. 209-244. 
[KuK21] Kundu, S., and Kunisch, K., 2021. “Policy Iteration for Hamilton-Jacobi-Bellman Equations with Control Constraints,” Computational Optimiza-tion and Applications, pp. 1-25. 
[KuV86] Kumar, P. R., and Varaiya, P. P., 1986. Stochastic Systems: Estimation, Identification, and Adaptive Control, Prentice-Hall, Englewood Cli↵s, N. J. 
[KuL82] Kumar, P. R., and Lin, W., 1982. “Optimal Adaptive Controllers for Unknown Markov Chains,” IEEE Trans. Automatic Control, Vol. AC-27, pp.
References 223 
765-774. 
[Kum83] Kumar, P. R., 1983. “Optimal Adaptive Control of Linear-Quadratic-Gaussian Systems,” SIAM J. on Control and Optimization, Vol. 21, pp. 163-178. 
[Kum85] Kumar, P. R., 1985. “A Survey of Some Results in Stochastic Adaptive Control,” SIAM J. on Control and Optimization, Vol. 23, pp. 329-380. 
[LAM21] Lopez, V. G., Alsalti, M., and Muller, M. A., 2021. “E cient O↵-Policy Q-Learning for Data-Based Discrete-Time LQR Problems,” arXiv preprint arXiv:2105.07761. 
[LJM21] Li, Y., Johansson, K. H., Martensson, J., and Bertsekas, D. P., 2021. “Data-Driven Rollout for Deterministic Optimal Control,” arXiv preprint arXiv:-2105.03116. 
[LLL08] Lewis, F. L., Liu, D., and Lendaris, G. G., 2008. Special Issue on Adap-tive Dynamic Programming and Reinforcement Learning in Feedback Control, IEEE Trans. on Systems, Man, and Cybernetics, Part B, Vol. 38, No. 4. 
[LPS21] Liu, M., Pedrielli, G., Sulc, P., Poppleton, E., and Bertsekas, D. P., 2021. “ExpertRNA: A New Framework for RNA Structure Prediction,” bioRxiv 2021.01.18.427087; to appear in INFORMS J. on Computing. 
[LWW17] Liu, D., Wei, Q., Wang, D., Yang, X., and Li, H., 2017. Adaptive Dynamic Programming with Applications in Optimal Control, Springer, Berlin. 
[LXZ21] Liu, D., Xue, S., Zhao, B., Luo, B., and Wei, Q., 2021. “Adaptive Dynamic Programming for Control: A Survey and Recent Advances,” IEEE Transactions on Systems, Man, and Cybernetics, Vol. 51, pp. 142-160. 
[LaR95] Lancaster, P., and Rodman, L., 1995. Algebraic Riccati Equations, Clarendon Press. 
[LaS20] Lattimore, T., and Szepesvari, C., 2020. Bandit Algorithms, Cambridge Univ. Press. 
[LaW13] Lavretsky, E., and Wise, K., 2013. Robust and Adaptive Control with Aerospace Applications, Springer. 
[LeL13] Lewis, F. L., and Liu, D., (Eds), 2013. Reinforcement Learning and Approximate Dynamic Programming for Feedback Control, Wiley, Hoboken, N. J. 
[LeV09] Lewis, F. L., and Vrabie, D., 2009. “Reinforcement Learning and Adap-tive Dynamic Programming for Feedback Control,” IEEE Circuits and Systems Magazine, 3rd Q. Issue. 
[Li17] Li, Y., 2017. “Deep Reinforcement Learning: An Overview,” arXiv preprint ArXiv: 1701.07274v5. 
[MDM01] Magni, L., De Nicolao, G., Magnani, L., and Scattolini, R., 2001. “A Stabilizing Model-Based Predictive Control Algorithm for Nonlinear Systems,” Automatica, Vol. 37, pp. 1351-1362. 
[MKH10] Mayer, J., Khairy, K., and Howard, J., 2010. “Drawing an Elephant with Four Complex Parameters,” American Journal of Physics, Vol. 78, pp. 648-649. 
[MRR00] Mayne, D., Rawlings, J. B., Rao, C. V., and Scokaert, P. O. M., 2000. “Constrained Model Predictive Control: Stability and Optimality,” Automatica, Vol. 36, pp. 789-814. 
[MVB20] Magirou, E. F., Vassalos, P., and Barakitis, N., 2020. “A Policy It-eration Algorithm for the American Put Option and Free Boundary Control
224 References 
Problems,” J. of Computational and Applied Mathematics, vol. 373, p. 112544. 
[MaK12] Mausam, and Kolobov, A., 2012. “Planning with Markov Decision Pro-cesses: An AI Perspective,” Synthesis Lectures on Artificial Intelligence and Ma-chine Learning, Vol. 6, pp. 1-210. 
[Mac02] Maciejowski, J. M., 2002. Predictive Control with Constraints, Addison-Wesley, Reading, MA. 
[Man74] Mandl, P., 1974. “Estimation and Control in Markov Chains,” Advances in Applied Probability, Vol. 6, pp. 40-60. 
[May14] Mayne, D. Q., 2014. “Model Predictive Control: Recent Developments and Future Promise,” Automatica, Vol. 50, pp. 2967-2986. 
[Mes16] Mesbah, A., 2016. Stochastic Model Predictive Control: An Overview and Perspectives for Future Research,” IEEE Control Systems Magazine, Vol. 36, pp. 30-44. 
[Mey07] Meyn, S., 2007. Control Techniques for Complex Networks, Cambridge Univ. Press, N. Y. 
[NaA12] Narendra, K. S., and Annaswamy, A. M., 2012. Stable Adaptive Systems, Courier Corporation. 
[OrR67] Ortega, J. M., and Rheinboldt, W. C., 1967. “Monotone Iterations for Nonlinear Equations with Application to Gauss-Seidel Methods,” SIAM J. on Numerical Analysis, Vol. 4, pp. 171-190. 
[OrR70] Ortega, J. M., and Rheinboldt, W. C., 1970. Iterative Solution of Non-linear Equations in Several Variables, Academic Press; republished in 2000 by the Society for Industrial and Applied Mathematics. 
[PaJ21] Pang, B., and Jiang, Z. P., 2021. “Robust Reinforcement Learning: A Case Study in Linear Quadratic Regulation,” arXiv preprint arXiv:2008.11592v3. 
[Pan90] Pang, J. S., 1990. “Newton’s Method for B-Di↵erentiable Equations,” Math. of Operations Research, Vol. 15, pp. 311-341. 
[PoA69] Pollatschek, M., and Avi-Itzhak, B., 1969. “Algorithms for Stochastic Games with Geometrical Interpretation,” Management Science, Vol. 15, pp. 399-413. 
[PoR12] Powell, W. B., and Ryzhov, I. O., 2012. Optimal Learning, J. Wiley, N. Y. 
[PoV04] Powell, W. B., and Van Roy, B., 2004. “Approximate Dynamic Program-ming for High-Dimensional Resource Allocation Problems,” in Learning and Ap-proximate Dynamic Programming, by J. Si, A. Barto, W. Powell, and D. Wunsch, (Eds.), IEEE Press, N. Y. 
[Pow11] Powell, W. B., 2011. Approximate Dynamic Programming: Solving the Curses of Dimensionality, 2nd Edition, J. Wiley and Sons, Hoboken, N. J. 
[PuB78] Puterman, M. L., and Brumelle, S. L., 1978. “The Analytic Theory of Policy Iteration,” in Dynamic Programming and Its Applications, M. L. Puter-man (ed.), Academic Press, N. Y. 
[PuB79] Puterman, M. L., and Brumelle, S. L., 1979. “On the Convergence of Policy Iteration in Stationary Dynamic Programming,” Math. of Operations Re-search, Vol. 4, pp. 60-69. 
[Put94] Puterman, M. L., 1994. Markovian Decision Problems, J. Wiley, N. Y. 
[Qi93] Qi, L., 1993. “Convergence Analysis of Some Algorithms for Solving Non-smooth Equations,” Math. of Operations Research, Vol. 18, pp. 227-244.
References 225 
[QiS93] Qi, L., and Sun, J., 1993. “A Nonsmooth Version of Newton’s Method,” Math. Programming, Vol. 58, pp. 353-367. 
[RMD17] Rawlings, J. B., Mayne, D. Q., and Diehl, M. M., 2017. Model Predic-tive Control: Theory, Computation, and Design, 2nd Ed., Nob Hill Publishing (updated in 2019 and 2020). 
[Rec18] Recht, B., 2018. “A Tour of Reinforcement Learning: The View from Continuous Control,” Annual Review of Control, Robotics, and Autonomous Systems. 
[RoB17] Rosolia, U., and Borrelli, F., 2017. “Learning Model Predictive Con-trol for Iterative Tasks. A Data-Driven Control Framework,” IEEE Trans. on Automatic Control, Vol. 63, pp. 1883-1896. 
[RoB19] Rosolia, U., and Borrelli, F., 2019. “Sample-Based Learning Model Pre-dictive Control for Linear Uncertain Systems,” 58th Conference on Decision and Control (CDC), pp. 2702-2707. 
[Rob80] Robinson, S. M., 1980. “Strongly Regular Generalized Equations,” Math. of Operations Research, Vol. 5, pp. 43-62. 
[Rob88] Robinson, S. M., 1988. “Newton’s Method for a Class of Nonsmooth Functions,” Industrial Engineering Working Paper, University of Wisconsin; also in Set-Valued Analysis Vol. 2, 1994, pp. 291-305. 
[Rob11] Robinson, S. M., 2011. “A Point-of-Attraction Result for Newton’s Method with Point-Based Approximations,” Optimization, Vol. 60, pp. 89-99. 
[SGG15] Scherrer, B., Ghavamzadeh, M., Gabillon, V., Lesner, B., and Geist, M., 2015. “Approximate Modified Policy Iteration and its Application to the Game of Tetris,” J. of Machine Learning Research, Vol. 16, pp. 1629-1676. 
[SBP04] Si, J., Barto, A., Powell, W., and Wunsch, D., (Eds.) 2004. Learning and Approximate Dynamic Programming, IEEE Press, N. Y. 
[SHM16] Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., Van Den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., and Dieleman, S., 2016. “Mastering the Game of Go with Deep Neural Networks and Tree Search,” Nature, Vol. 529, pp. 484-489. 
[SHS17] Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Graepel, T., and Lillicrap, T., 2017. “Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm,” arXiv preprint arXiv:1712.01815. 
[SSS17] Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M., Bolton, A., and Chen, Y., 2017. “Mas-tering the Game of Go Without Human Knowledge,” Nature, Vol. 550, pp. 354-359. 
[SYL04] Si, J., Yang, L., and Liu, D., 2004. “Direct Neural Dynamic Program-ming,” in Learning and Approximate Dynamic Programming, by J. Si, A. Barto, W. Powell, and D. Wunsch, (Eds.), IEEE Press, N. Y. 
[SaB11] Sastry, S., and Bodson, M., 2011. Adaptive Control: Stability, Conver-gence and Robustness, Courier Corporation. 
[SaL79] Saridis, G. N., and Lee, C.-S. G., 1979. “An Approximation Theory of Optimal Control for Trainable Manipulators,” IEEE Trans. Syst., Man, Cyber-netics, Vol. 9, pp. 152-159.
226 References 
[SaR04] Santos, M. S., and Rust, J., 2004. “Convergence Properties of Policy Iteration,” SIAM J. on Control and Optimization, Vol. 42, pp. 2094-2115. 
[Sch15] Schmidhuber, J., 2015. “Deep Learning in Neural Networks: An Overview,” Neural Networks, pp. 85-117. 
[Sha53] Shapley, L. S., 1953. “Stochastic Games,” Proc. of the National Academy of Sciences, Vol. 39, pp. 1095-1100. 
[SlL91] Slotine, J.-J. E., and Li, W., Applied Nonlinear Control, Prentice-Hall, Englewood Cli↵s, N. J. 
[Str66] Strauch, R., 1966. “Negative Dynamic Programming,” Ann. Math. Statist., Vol. 37, pp. 871-890. 
[SuB18] Sutton, R., and Barto, A. G., 2018. Reinforcement Learning, 2nd Ed., MIT Press, Cambridge, MA. 
[Sze10] Szepesvari, C., 2010. Algorithms for Reinforcement Learning, Morgan and Claypool Publishers, San Franscisco, CA. 
[TeG96] Tesauro, G., and Galperin, G. R., 1996. “On-Line Policy Improvement Using Monte Carlo Search,” NIPS, Denver, CO. 
[Tes94] Tesauro, G. J., 1994. “TD-Gammon, a Self-Teaching Backgammon Pro-gram, Achieves Master-Level Play,” Neural Computation, Vol. 6, pp. 215-219. 
[Tes95] Tesauro, G. J., 1995. “Temporal Di↵erence Learning and TD-Gammon,” Communications of the ACM, Vol. 38, pp. 58-68. 
[TsV96] Tsitsiklis, J. N., and Van Roy, B., 1996. “Feature-Based Methods for Large-Scale Dynamic Programming,” Machine Learning, Vol. 22, pp. 59-94. 
[VVL13] Vrabie, D., Vamvoudakis, K. G., and Lewis, F. L., 2013. Optimal Adap-tive Control and Di↵erential Games by Reinforcement Learning Principles, The Institution of Engineering and Technology, London. 
[Van67] Vandergraft, J. S., 1967. “Newton’s Method for Convex Operators in Partially Ordered Spaces,” SIAM J. on Numerical Analysis, Vol. 4, pp. 406-432. 
[Van78] van der Wal, J., 1978. “Discounted Markov Games: Generalized Policy Iteration Method,” J. of Optimization Theory and Applications, Vol. 25, pp. 125-138. 
[WLL16] Wei, Q., Liu, D., and Lin, H., 2016. “Value Iteration Adaptive Dynamic Programming for Optimal Control of Discrete-Time Nonlinear Systems,” IEEE Transactions on Cybernetics, Vol. 46, pp. 840-853. 
[WLL21] Winnicki, A., Lubars, J., Livesay, M., and Srikant, R., 2021. “The Role of Lookahead and Approximate Policy Evaluation in Policy Iteration with Linear Value Function Approximation,” arXiv preprint arXiv:2109.13419. 
[WhS92] White, D., and Sofge, D., (Eds.), 1992. Handbook of Intelligent Control, Van Nostrand, N. Y. 
[YuB13] Yu, H., and Bertsekas, D. P., 2013. “Q-Learning and Policy Iteration Al-gorithms for Stochastic Shortest Path Problems,” Annals of Operations Research, Vol. 208, pp. 95-132. 
[YuB15] Yu, H., and Bertsekas, D. P., 2015. “A Mixed Value and Policy Iteration Method for Stochastic Control with Universally Measurable Policies,” Math. of OR, Vol. 40, pp. 926-968. 
[ZSG20] Zoppoli, R., Sanguineti, M., Gnecco, G., and Parisini, T., 2020. Neural Approximations for Optimal Control and Decision, Springer.
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