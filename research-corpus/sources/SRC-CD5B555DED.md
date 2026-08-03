> Source: https://www.cs.unh.edu/~mpetrik/pub/tutorials/robustrl/dlrl-extended.pdf

Robust Reinforcement Learning 
Marek Petrik 
Department of Computer Science University of New Hampshire 
DLRL Summer School 2019 
 
Adversarial Robustness in ML 
[Kolter, Madry 2018] 
Is this a problem? 
 
 
 
Adversarial Robustness in ML 
[Kolter, Madry 2018] 
Is this a problem? Safety, security, trust 
Are reinforcement learning methods robust? 
 
Robustness 
An algorithm is robust if it performs well even in the presence of small errors in inputs. 
 
 
 
 
 
Robustness 
An algorithm is robust if it performs well even in the presence of small errors in inputs. 
Questions: 
1. What does it mean to perform well? 
2. What is a small error? 
3. How to compute a robust solution? 
 
Outline 
1. Adversarial robustness in RL 
2. Robust Markov Decision Processes: How to solve them? 
3. Modeling input errors: What is a small error? 
4. Other formulations: What is the right objective? 
Model-based approach to reliable off-policy sample-efficient tabular RL by 
learning models and confidence 
 
Adversarial Robustness in RL 
 
Robustness Not Important When . . . 
I Control problems: inverted pendulum, . . . 
I Computer games: Atari, Minecraft, . . . 
I Board games: Chess, Go, . . . 
Because 
1. Mostly deterministic dynamics 
2. Simulators are fast and precise: I Lots of data is available I Easy to test a policy 
3. Failure to learn a good policy is cheap 
 
Robustness Matters In Real World 
1. Learning from logged data (batch RL): 
1.1 No simulator 1.2 Never enough data 1.3 How to test a policy? No cross-validation in RL 
2. High cost of failure (bad policy) 
Important in Real Applications 
 
 
 
 
 
Robustness Matters In Real World 
1. Learning from logged data (batch RL): 
1.1 No simulator 1.2 Never enough data 1.3 How to test a policy? No cross-validation in RL 
2. High cost of failure (bad policy) 
Important in Real Applications 
I Agriculture: Scheduling pesticide applications 
I Maintenance: Optimizing infrastructure maintenance 
I Healthcare: Better insulin management in diabetes 
I Autonomous vehicles, robotics, . . . 
 
Example: Robust Pest Management 
Agriculture: A challenging RL problem 
1. Stochastic environment and delayed rewards 
2. Must learn from data: No reliable, accurate simulator 
3. One episode = one year 
4. Crop failure is expensive 
 
 
 
 
 
 
 
Example: Robust Pest Management 
Agriculture: A challenging RL problem 
1. Stochastic environment and delayed rewards 
2. Must learn from data: No reliable, accurate simulator 
3. One episode = one year 
4. Crop failure is expensive 
Simulator: Using ecological population P models [Kery and Schaub, 2012]: 
dP 
dt = r P 
( 1− P 
K 
) Growth rate r, carrying capacity K, loosely based on spotted wing drosophila 
 
Pest Control as MDP 
States: Pest population: [0, 50] 
Actions: 
0 No pesticide 
1-4 Pesticides P1, P2, P3, P4 with increasing effectiveness 
Transition probabilities: Pest population dynamics 
Reward: 
1. Crop yield minus pest damage 
2. Spraying cost: P4 more expensive than P1 
 
MDP Objective: Discounted Infinite Horizon 
Solution: Policy π maps states → actions Objective: Discounted return: 
return(π) = E 
[ ∞∑ t=0 
γt rewardt 
] 
Optimal solution: Optimal policy 
π? ∈ arg max π 
return(π) 
Value function: v maps states → expected return Bellman optimality: 
v(s) = max a 
( rs,a + γ · pTs,av 
) 
 
Transition Probabilities 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
No Pesticide 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Pesticide P1 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Pesticide P3 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Pesticide P4 
 
Computing Optimal Policy 
Algorithms: Value iteration, Policy iteration, Modified (optimistic) policy iteration, Linear programming 
Return: $8,820 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
P es 
tic id 
e 
Optimal Nominal Policy 
 
Optimal Management Policy 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
P es 
tic id 
e 
Optimal Nominal Policy 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
 
Simulated Optimal Policy 
● 
 
 
 
 
 
 
 
 
●● 
● 
 
 
● 
 
 
 
 
 
 
● 
 
 
 
 
 
 
 
 
● 
● 
 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 
Time Step 
P op 
ul at 
io n 
Action 
0 
1 
2 
3 
Simulated Population and Actions 
 
Is It Robust? Return: $8,820 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
+ 
L1 ≤ 0.05 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noise 
= 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Is It Robust? Return: $8,820 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
+ 
L1 ≤ 0.05 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noise 
= 
= 
Return: −$6,725 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noisy Transitions 
 
Adversarial Robustness for Reinforcement Learning 
“An algorithm is robust if it performs well even in the presence of small errors in inputs. ” 
Robust optimization: Best π with respect to the inputs with all possible small errors: 
max π 
min P ,r 
{ return(π, P , r) : 
‖P̄ − P‖ ≤ small ‖r̄ − r‖ ≤ small 
} Adversarial nature chooses P , r 
 
 
Adversarial Robustness for Reinforcement Learning 
“An algorithm is robust if it performs well even in the presence of small errors in inputs. ” 
Robust optimization: Best π with respect to the inputs with all possible small errors: 
max π 
min P ,r 
{ return(π, P , r) : 
‖P̄ − P‖ ≤ small ‖r̄ − r‖ ≤ small 
} Adversarial nature chooses P , r 
Related to regularization e.g. [Xu et al., 2010], risk [Shapiro et al., 2014], and is opposite of exploration (MBIE/UCRL2) e.g. [Auer et al., 2010] 
 
Robust Representation 
Nominal values P̄ , r̄ 
Errors in rewards: e.g. [Regan and Boutilier, 2009] 
max π 
min r 
{ return(π, P̄ , r) : ‖r − r̄‖ ≤ ψ 
} 
Errors in transitions: e.g. [Iyengar, 2005a] 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
 
 
Robust Representation 
Nominal values P̄ , r̄ 
Errors in rewards: e.g. [Regan and Boutilier, 2009] 
max π 
min r 
{ return(π, P̄ , r) : ‖r − r̄‖ ≤ ψ 
} 
Errors in transitions: e.g. [Iyengar, 2005a] 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
Budget of robustness ψ is the error size 
 
Reward Function Errors 
Objective: 
max π 
min r 
{ return(π, P̄ , r) : ‖r − r̄‖ ≤ ψ 
} 
 
Reward Function Errors 
Objective: 
max π 
min r 
{ return(π, P̄ , r) : ‖r − r̄‖ ≤ ψ 
} 
Using MDP dual linear program: [Puterman, 2005] 
max u∈RSA 
min r∈RSA 
{rTu : ‖r − r̄‖ ≤ ψ} 
s.t. ∑ a 
(I− γPT a )ua = p0 
u ≥ 0 
 
Reward Function Errors 
Objective: 
max π 
min r 
{ return(π, P̄ , r) : ‖r − r̄‖ ≤ ψ 
} 
Linear program reformulation (‖ · ‖? is dual norm): 
max u∈RSA 
r̄Tu− ψ‖u‖? s.t. 
∑ a 
(I− γPT a )ua = p0 
u ≥ 0 
No known VI, PI, or similar algorithms in general 
 
Transition Function Errors 
Objective: 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
 
 
 
 
 
Transition Function Errors 
Objective: 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
I NP-hard to solve in general e.g. [Wiesemann et al., 2013] 
I No known LP formulation, VI, PI possible 
 
 
 
Transition Function Errors 
Objective: 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
I NP-hard to solve in general e.g. [Wiesemann et al., 2013] 
I No known LP formulation, VI, PI possible 
I Ambiguity set (aka uncertainty set):{ P : ‖P − P̄‖ ≤ ψ 
} 
 
 
Transition Function Errors 
Objective: 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} 
I NP-hard to solve in general e.g. [Wiesemann et al., 2013] 
I No known LP formulation, VI, PI possible 
I Ambiguity set (aka uncertainty set):{ P : ‖P − P̄‖ ≤ ψ 
} Focus of the remainder of tutorial 
 
Robust Markov Decision Processes 
 
History of Robustness for MDPs / RL 
1. 1958: Proposed to deal with imprecise MDP models in inventory management [Scarf, 1958] 
2. Uncertain transition probabilities MDPs [Satia and Lave, 1973, White and 
Eldeib, 1994, Bagnell, 2004] 
3. Competitive MDPs [Filar and Vrieze, 1997] 
4. Bounded-parameter MDPs [Givan et al., 2000, Delgado et al., 2016] 
5. Rectangular Robust MDPs [Iyengar, 2005b, Nilim and El Ghaoui, 2005, Le Tallec, 
2007, Wiesemann et al., 2013] 
6. See [Ben-Tal et al., 2009] for overview of robust optimization 
 
Ambiguity Sets: General 
Nature is constrained globally 
max π 
min P 
{ return(π, P , r̄) : ‖P − P̄‖ ≤ ψ 
} NP-hard problem to solve e.g. [Wiesemann et al., 2013] 
 
Ambiguity Sets: S-Rectangular 
Nature is constrained for each state separately e.g. [Le Tallec, 2007] 
max π 
min P 
{ return(π, P , r̄) : ‖Ps − P̄s‖ ≤ ψs, ∀s 
} Nature can see last state but not action Polynomial time solvable; Why? 
 
 
Ambiguity Sets: S-Rectangular 
Nature is constrained for each state separately e.g. [Le Tallec, 2007] 
max π 
min P 
{ return(π, P , r̄) : ‖Ps − P̄s‖ ≤ ψs, ∀s 
} Nature can see last state but not action Polynomial time solvable; Why? Bellman Optimality 
 
Ambiguity Sets: SA-Rectangular 
Nature is constrained for each state and action separately e.g. [Nilim and 
El Ghaoui, 2005] 
max π 
min P 
{ return(π, P , r̄) : ‖Ps,a − P̄s,a‖ ≤ ψs,a, ∀s, a 
} Nature can see last state and action Polynomial time solvable; Why? 
 
 
Ambiguity Sets: SA-Rectangular 
Nature is constrained for each state and action separately e.g. [Nilim and 
El Ghaoui, 2005] 
max π 
min P 
{ return(π, P , r̄) : ‖Ps,a − P̄s,a‖ ≤ ψs,a, ∀s, a 
} Nature can see last state and action Polynomial time solvable; Why? Bellman Optimality 
 
SA-Rectangular Ambiguity 
Example: For each state s and action a:{ ps,a : ‖ps,a−p̄s,a‖1 ≤ ψs,a 
} = { ps,a : 
∑ s′ 
|ps,a,s′−p̄s,a,s′ | ≤ ψs,a } 
Sets are rectangles over s and a: 
6 
-
6 
-P[ s 3 |s 2 ,a 
1 ] 
P[s3|s1, a1] 
P[ s 3 |s 1 ,a 
2 ] 
P[s3|s1, a1] 
 
S-Rectangular Ambiguity 
Example: For each state s:{ ps,a : 
∑ a 
‖ps,a−p̄s,a‖1 ≤ ψs } 
= { ps,a : 
∑ a,s′ 
|ps,a,s′−p̄s,a,s′ | ≤ ψs } 
Sets are rectangles over s only: 
6 
-
6 
-
Z Z 
P[ s 3 |s 2 ,a 
1 ] 
P[s3|s1, a1] 
P[ s 3 |s 1 ,a 
2 ] 
P[s3|s1, a1] 
 
Robust Markov decision process 
s1 s2 
a1 
a2 
P 1 11 P 2 
11 
P 1 12 P 2 
12 
 
Optimal Policy Classification 
Nature can be: [Iyengar, 2005a] 
1. Static: stationary, same p in every visit to state and action 
2. Dynamic: history-dependent, can change in every visit 
 
 
 
 
 
Optimal Policy Classification 
Nature can be: [Iyengar, 2005a] 
1. Static: stationary, same p in every visit to state and action 
2. Dynamic: history-dependent, can change in every visit 
Rectangularity Static Nature Dynamic Nature 
None H R H R State H R S R 
State-Action H R S D e.g. [Iyengar, 2005a, Le Tallec, 2007, Wiesemann et al., 2013] 
H = history-dependent R = randomized S = stationary / Markovian D = deterministic 
 
Optimal Robust Value Function 
Bellman optimality in MDPs: 
v(s) = max a 
( rs,a + γp̄Ts,av 
) 
 
 
 
 
 
 
 
 
 
 
 
 
Optimal Robust Value Function 
Bellman optimality in MDPs: 
v(s) = max a 
( rs,a + γp̄Ts,av 
) Robust Bellman optimality: SA-rectangular ambiguity set 
v(s) = max a 
min p∈∆S 
{ rs,a + γpTv : ‖p̄s,a − p‖1 ≤ ψs,a 
} 
 
 
 
 
 
 
 
 
Optimal Robust Value Function 
Bellman optimality in MDPs: 
v(s) = max a 
( rs,a + γp̄Ts,av 
) Robust Bellman optimality: SA-rectangular ambiguity set 
v(s) = max a 
min p∈∆S 
{ rs,a + γpTv : ‖p̄s,a − p‖1 ≤ ψs,a 
} Robust Bellman optimality: S-rectangular ambiguity set 
v(s) = max d∈∆A 
min pa∈∆S 
{∑ a 
d(s, a)(rs,a + γpa Tv) :∑ 
a 
‖p̄s,a − pa‖1 ≤ ψs } 
 
Solving Robust MDPs 
Robust Bellman operator is: e.g. [Iyengar, 2005a, Le Tallec, 2007, Wiesemann et al., 
2013] 
1. A contraction in L∞ norm 
2. Monotone elementwise 
Therefore: 
1. Value Iteration converges to the single optimal value function. 
2. But naive policy iteration may loop forever [Condon, 1993] 
3. No known linear programming formulation 
 
Optimal SA Robust Policy: ψ = 0.05 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
P es 
tic id 
e Optimal Nominal Policy 
Nominal $8, 820 SA-Robust −$7, 961 S-Robust −$7, 961 
0 
1 
2 
3 
4 
0 10 20 30 40 50 
Population (state) 
P es 
tic id 
e 
Optimal SA−Robust Policy 
Nominal $7, 125 SA-Robust −$27 S-Robust −$27 
 
SA-Rectangular Error Return: $7,125 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
+ 
L1 ≤ 0.05 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noise 
= 
= 
Return: −$27 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noisy Transitions 
 
Optimal S Robust Policy: ψ = 0.05 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
P es 
tic id 
e Optimal Nominal Policy 
Nominal $8, 820 SA-Robust −$7, 961 S-Robust −$7, 961 
0 
1 
2 
3 
4 
0 10 20 30 40 50 
Population (state) 
P es 
tic id 
e (a 
ct io 
n) 
Optimal S−Robust Policy 
Nominal $7, 306 S-Robust $3, 942 
 
S-Rectangular Error: ψ = 0.05 Return: $7,306 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
+ 
L1 ≤ 0.05 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noise 
= 
= 
Return: $3,942 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 
Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noisy Transitions 
 
Solving Robust MDPs 
I Robust Bellman Optimality: SA-rectangular ambiguity set 
v(s) = max a 
min p∈∆S 
{ rs,a + pTv : ‖p̄− p‖1 ≤ ψ 
} I How to solve for p? 
 
 
 
 
Solving Robust MDPs 
I Robust Bellman Optimality: SA-rectangular ambiguity set 
v(s) = max a 
min p∈∆S 
{ rs,a + pTv : ‖p̄− p‖1 ≤ ψ 
} I How to solve for p? 
I Linear programming is polynomial time for polyhedral sets 
I Optimal policy using value iteration in polynomial time 
I Is it really tractable? 
 
Benchmarking Robust Bellman Update 
Bellman update: Inventory optimization, 200 states and actions, ψ = 0.25 
rs,a + pTv 
Time: 0.04s 
 
 
 
 
 
 
 
 
 
Benchmarking Robust Bellman Update 
Bellman update: Inventory optimization, 200 states and actions, ψ = 0.25 
rs,a + pTv 
Time: 0.04s 
Robust Bellman update: Gurobi LP 
min p∈∆S 
{ rs,a + pTv : ‖p̄− p‖1 ≤ ψ 
} Distance Metric 
Rectangularity L1 Norm w-L1 Norm 
State-action 1.1 min 1.2 min 
State 16.7 min 13.4 min 
LP scales as ≥ O(n3). 
 
 
Benchmarking Robust Bellman Update 
Bellman update: Inventory optimization, 200 states and actions, ψ = 0.25 
rs,a + pTv 
Time: 0.04s 
Robust Bellman update: Gurobi LP 
min p∈∆S 
{ rs,a + pTv : ‖p̄− p‖1 ≤ ψ 
} Distance Metric 
Rectangularity L1 Norm w-L1 Norm 
State-action 1.1 min 1.2 min 
State 16.7 min 13.4 min 
LP scales as ≥ O(n3). There is a better way! 
 
Robust Bellman Update in O(n log n) 
Quasi-linear time possible for many types of ambiguity sets 
Metric SA-Rectangular S-Rectangular 
L1 e.g. [Iyengar, 2005a] [Ho et al., 2018] 
weighted L1 [Ho et al., 2018] [Ho et al., 2018] 
L2 [Iyengar, 2005a] ** 
L∞ e.g. [Givan et al., 2000], * ** 
KL-divergence [Nilim and El Ghaoui, 2005] ** 
Bregman div ** ** 
* proof in [Zhang et al., 2017], ** = unpublished result 
 
Fast Robust Bellman Updates [Ho et al., 2018] 
Distance Metric Rectangularity L1 Norm w-L1 Norm 
SA O(n log n) O(k n log n) 
S O(n log n) O(k n log n) 
Problem size: n = states × actions 
1. Homotopy Continuation Method: use simple structure 
2. Bisection + Homotopy Method: randomized policies in combinatorial time 
 
Fast Robust Bellman Updates [Ho et al., 2018] 
Distance Metric Rectangularity L1 Norm w-L1 Norm 
SA O(n log n) O(k n log n) 
S O(n log n) O(k n log n) 
Problem size: n = states × actions 
1. Homotopy Continuation Method: use simple structure 
2. Bisection + Homotopy Method: randomized policies in combinatorial time 
 
SA-Rectangular Problem 
Optimization: minp { pTv : ‖p− p̄‖1 ≤ ξ 
} 
 
 
 
 
 
 
 
 
 
 
SA-Rectangular Problem 
Optimization: minp { pTv : ‖p− p̄‖1 ≤ ξ 
} Lift to get a linear program: 
min p,l 
pTv 
s. t. pi − p̄i ≤ li p̄i − pi ≤ li pi ≥ 0 
1Tp = 1, 1Tl = ξ 
 
 
 
 
 
SA-Rectangular Problem 
Optimization: minp { pTv : ‖p− p̄‖1 ≤ ξ 
} Lift to get a linear program: 
min p,l 
pTv 
s. t. pi − p̄i ≤ li p̄i − pi ≤ li pi ≥ 0 
1Tp = 1, 1Tl = ξ 
Observation: In basic solution at most two i: pi 6= 0 and pi 6= p̄i 
 
 
 
 
SA-Rectangular Problem 
Optimization: minp { pTv : ‖p− p̄‖1 ≤ ξ 
} Lift to get a linear program: 
min p,l 
pTv 
s. t. pi − p̄i ≤ li p̄i − pi ≤ li pi ≥ 0 
1Tp = 1, 1Tl = ξ 
Observation: In basic solution at most two i: pi 6= 0 and pi 6= p̄i 
Therefore: 
1. At most S2 basic solutions (S with no weights) 
2. At most two pi depend on budget ξ 
 
SA-Rectangular: Homotopy Method 
min p∈∆S 
{ pTv : ‖p− p̄‖1 ≤ ξ 
} 
0.0 
0.5 
1.0 
0 1 2 3 
Ambiguity set size: ξ 
R ob 
us t Q 
− fu 
nc tio 
n:  q 
(ξ ) 
Trace optimal solution with increasing ξ 
SA-Rectangular: Plain L1 
p̄ = [0.2, 0.3, 0.4, 0.1] v = [4, 3, 2, 1] 
 
 ● ● ●0.00 
0.25 
0.50 
0.75 
1.00 
0.0 0.5 1.0 1.5 2.0 
Size of ambiquity set: ξ 
Tr an 
si tio 
n pr 
ob ab 
ili ty 
: p i∗ 
Index 
 0 
1 
2 
3 
 
SA-Rectangular: Weighted L1 
p̄ = [0.2, 0.3, 0.3, 0.2] v = [2.9, 0.9, 1.5, 0.0] w = [1, 1, 2, 2] 
 
 ● ● ● ●0.00 
0.25 
0.50 
0.75 
1.00 
0 1 2 3 
Size of ambiquity set: ξ 
Tr an 
si tio 
n pr 
ob ab 
ili ty 
: p i∗ 
Index 
 0 
1 
2 
3 
 
S-Rectangular Optimization 
Optimization problem: Linear program 
max d∈∆A 
min pa∈∆S 
∑ a 
d(s, a)(rs,a + γ pa Tv) 
s. t. ∑ a 
‖p̄s,a − pa‖1 ≤ ψs 
 
 
 
 
 
S-Rectangular Optimization 
Optimization problem: Linear program 
max d∈∆A 
min pa∈∆S 
∑ a 
d(s, a)(rs,a + γ pa Tv) 
s. t. ∑ a 
‖p̄s,a − pa‖1 ≤ ψs 
Why should it be easy to solve? 
1. Use ‖ · ‖1 structure from SA-rectangular formulation 
2. Constraint is a sum: Decompose! 
 
 
S-Rectangular Optimization 
Optimization problem: Linear program 
max d∈∆A 
min pa∈∆S 
∑ a 
d(s, a)(rs,a + γ pa Tv) 
s. t. ∑ a 
‖p̄s,a − pa‖1 ≤ ψs 
Why should it be easy to solve? 
1. Use ‖ · ‖1 structure from SA-rectangular formulation 
2. Constraint is a sum: Decompose! 
Special S-rectangular formulation, does not work in general 
 
Bisection to Decompose Optimization 1. Objective with qa(ξ) = SA-rectangular update: 
max d∈∆A 
min ξ∈RA 
+ 
{∑ a∈A 
da · qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Bisection to Decompose Optimization 1. Objective with qa(ξ) = SA-rectangular update: 
max d∈∆A 
min ξ∈RA 
+ 
{∑ a∈A 
da · qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
2. Swap min and max (which becomes deterministic): 
min ξ∈RA 
+ 
{ max a∈A 
qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
 
 
 
 
 
 
 
 
 
 
Bisection to Decompose Optimization 1. Objective with qa(ξ) = SA-rectangular update: 
max d∈∆A 
min ξ∈RA 
+ 
{∑ a∈A 
da · qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
2. Swap min and max (which becomes deterministic): 
min ξ∈RA 
+ 
{ max a∈A 
qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
3. Turn objective to constraint: 
min u∈R 
min ξ∈RA 
+ 
{ u : 
∑ a∈A 
ξa ≤ κ, max a∈A 
qa(ξa) ≤ u } 
 
 
Bisection to Decompose Optimization 1. Objective with qa(ξ) = SA-rectangular update: 
max d∈∆A 
min ξ∈RA 
+ 
{∑ a∈A 
da · qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
2. Swap min and max (which becomes deterministic): 
min ξ∈RA 
+ 
{ max a∈A 
qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
3. Turn objective to constraint: 
min u∈R 
min ξ∈RA 
+ 
{ u : 
∑ a∈A 
ξa ≤ κ, max a∈A 
qa(ξa) ≤ u } 
4. For given u, independently minimal ξa such that qa(ξa) ≤ u 
 
 
Bisection to Decompose Optimization 1. Objective with qa(ξ) = SA-rectangular update: 
max d∈∆A 
min ξ∈RA 
+ 
{∑ a∈A 
da · qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
2. Swap min and max (which becomes deterministic): 
min ξ∈RA 
+ 
{ max a∈A 
qa(ξa) : ∑ a∈A 
ξa ≤ κ } 
3. Turn objective to constraint: 
min u∈R 
min ξ∈RA 
+ 
{ u : 
∑ a∈A 
ξa ≤ κ, max a∈A 
qa(ξa) ≤ u } 
4. For given u, independently minimal ξa such that qa(ξa) ≤ u Bisect on u: O(n log n) combinatorial complexity 
 
S-Rectangular: Bisection Method 
min u∈R 
min ξ∈RA 
+ 
{ u : 
∑ a∈A 
ξa ≤ κ, max a∈A 
qa(ξa) ≤ u } 
 
 
 
 
 ●● 
u 
ξ3 ξ2ξ1−1 
0 
1 
2 
3 
0 1 2 3 
Allocated ambiquity budget: ξa 
R ob 
us t Q 
− fu 
nc tio 
n:  q 
(ξ a) 
Function 
 q1 
q2 
q3 
 
Numerical Time Complexity 
Timing Robust Bellman Updates: Inventory optimization, 200 states 
and actions, ψ = 0.25, Gurobi LP solver / Homotopy + Bisection 
Distance Metric Rectangularity L1 Norm w-L1 Norm 
State-action 1.1 min / 0.6s 1.2 min / 0.8s 
State 16.7 min / 0.7s 13.4 min / 1.2s 
Bellman update: 0.04s 
 
Partial Policy Iteration: S-Rectangular RMDPs 
While Bellman residual of vk is large: 
1. Policy evaluation: Compute vk for policy πk with precision εk (RMDP with fixed π is MDP) 
2. Policy improvement: Get πk+1 by greedily improving policy 
3. k ← k + 1 
 
 
Partial Policy Iteration: S-Rectangular RMDPs 
While Bellman residual of vk is large: 
1. Policy evaluation: Compute vk for policy πk with precision εk (RMDP with fixed π is MDP) 
2. Policy improvement: Get πk+1 by greedily improving policy 
3. k ← k + 1 
Theorem: Converges fast as long as εk+1 ≤ γcεk for c > 1 
 
Numerical Time Complexity 
Timing Robust Bellman updates: Inventory optimization, 200 states 
and actions, ψ = 0.25, Gurobi LP solver / Homotopy + Bisection 
Distance Metric Rectangularity L1 Norm w-L1 Norm 
State-action 1.1 min / 0.6s 1.2 min / 0.8s 
State 16.7 min / 0.7s 13.4 min / 1.2s 
Bellman update: 0.04s 
 
Policy Iteration for Robust MDPs 
I Value Iteration: Works as in MDPs 
I Naive policy iteration may cycle forever [Condon, 1993] 
I Policy iteration with LP as evaluation [Iyengar, 2005a] 
I Modified Robust Policy Iteration [Kaufman and Schaefer, 2013] 
I Partial Policy Iteration: Approximate policy evaluation [Ho et 
al. 2019] 
 
Benchmarks: Scaling with States 
Time in seconds, 300 second timeout, S-rectangular 
MDP RMDP Gurobi RMDP Bisection 
States PI VI PPI VI PPI 
12 0.00 0.36 0.01 0.00 0.00 36 0.00 >300 0.22 0.03 0.00 72 0.00 — >300 0.13 0.01 
108 0.00 — — 0.31 0.03 144 0.01 — — 0.60 0.05 180 0.02 — — 0.93 0.08 216 0.03 — — 1.38 0.14 252 0.04 — — 1.84 0.20 288 0.06 — — 2.46 0.27 
 
Beyond Plain Rectangularity 
S- and SA-rectangularity are: 
[+] Computationally convenient 
[-] Practically limiting 
Extensions: Most based on state augmentation 
I k-rectangularity: [Mannor et al., 2012] Upper limit on the number of deviations from nominal 
I r-rectangularity: [Goyal and Grand-Clement, 2018] 
I other approaches: Distributionally robust constraints [Tirinzoni 
et al., 2018] 
 
Modeling Errors in RL 
 
What Is Small Error? 
Optimize ψ = 0.0 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
 
 
 
Optimal Nominal Policy 
Evaluate 
ψ = 0 8,850 ψ = 0.05 -6,725 ψ = 0.4 -60,171 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
What Is Small Error? 
Optimize ψ = 0.0 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
 
 
 
Optimal Nominal Policy 
Evaluate 
ψ = 0 8,850 ψ = 0.05 -6,725 ψ = 0.4 -60,171 
Optimize ψ = 0.05 
0 
1 
2 
3 
4 
0 10 20 30 40 50 
Population (state) 
P es 
tic id 
e 
Optimal SA−Robust Policy 
Evaluate 
ψ = 0 7,408 ψ = 0.05 -25 ψ = 0.4 -46,256 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
What Is Small Error? 
Optimize ψ = 0.0 
0 
1 
2 
3 
4 
0 10 20 30 40 50 Population (state) 
 
 
 
Optimal Nominal Policy 
Evaluate 
ψ = 0 8,850 ψ = 0.05 -6,725 ψ = 0.4 -60,171 
Optimize ψ = 0.05 
0 
1 
2 
3 
4 
0 10 20 30 40 50 
Population (state) 
P es 
tic id 
e 
Optimal SA−Robust Policy 
Evaluate 
ψ = 0 7,408 ψ = 0.05 -25 ψ = 0.4 -46,256 
Optimize ψ = 0.4 
0 
1 
2 
3 
4 
0 10 20 30 40 50 
Population (state) 
P es 
tic id 
e 
Optimal SA−Robust Policy 
Evaluate 
ψ = 0 -622 ψ = 0.05 -2,485 ψ = 0.4 -31,613 
Which ψ to optimize for? 
 
Choosing Level Robustness (Ambiguity Set) 
1. What is the right size ψ of the ambiguity set? 
2. Should ψs,a be the same for each state and action? 
3. Why use the L1 norm? What about L∞, KL-divergence, Others? 
4. Which rectangularity to use (if any)? 
 
 
Choosing Level Robustness (Ambiguity Set) 
1. What is the right size ψ of the ambiguity set? 
2. Should ψs,a be the same for each state and action? 
3. Why use the L1 norm? What about L∞, KL-divergence, Others? 
4. Which rectangularity to use (if any)? 
Depends on why there are errors! 
 
Sample-efficient Batch Model-based RL 
No simulator, off-policy, just compute policy (Doina’s talk) 
Logged data: Population (biased), actions, rewards 
● 
 
 
 
 
 
 
 
 
●● 
● 
 
 
● 
 
 
 
 
 
 
● 
 
 
 
 
 
 
 
 
● 
● 
 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 
Time Step 
P op 
ul at 
io n 
Action 
0 
1 
2 
3 
Simulated Population and Actions 
 
Model-Based Reinforcement Learning 
Use Dyna-like approach: (Martha’s Talk) 
1. Collect transition data 
2. Use ML to build transition model 
3. Solve MDP model to get π 
4. Deploy policy π (with crossed fingers) 
The model can be wrong. Why? 
 
Sources of Model Error 
1. Model simplification: Value function approximation / simplified simulator [Petrik, 2012, Petrik and Subramanian, 2014, Lim and Autef, 2019] 
2. Limited data: Not enough data; batch RL e.g. [Petrik et al., 2016, 
Laroche et al., 2019, Petrik and Russell, 2019] 
3. Non-stationary environment: [Derman et al., 2019] 
4. Noisy observations: Like POMDPs but simpler e.g. [Pattanaik et al., 
2018] 
Each error source requires different treatment 
 
Robust Model-Based Reinforcement Learning 
Standard approach: 
1. Collect transition data 
2. Use ML to build transition model 
3. Solve MDP to get π 
4. Deploy policy π (with crossed fingers) 
Robust approach: 
1. Collect transition data 
2. Use ML to build transition model and confidence 
3. Solve Robust MDP model to get π 
4. Deploy policy π (with confidence) 
 
Error 1: Model Simplification [Petrik and Subramanian, 2014] 
State aggregation: Piece-wise constant linear value function approximation 
Performance loss for π̃ 
return(π?)−return(π̃) = return(optimal)−return(approximated) 
Loss bound [Gordon, 1995, Tsitsiklis and Van Roy, 1997] 
return(π?)− return(π̃) ≤ 4 γ 
(1− γ)2 min v∈RS 
‖v? − Φv‖∞ 
 
Robustness for State Aggregation 
Transition probabilities: s3 s4 
s1 1/4 3/4 s2 2/3 1/3 
Aggregate s1 and s2 with weights α1 and α2 into s 
Standard: arbitrary (wrong) α’s: α1 = 0.4, α2 = 0.6 
v(s) = (0.4 · 1/4 + 0.6 · 2/3)v(s3) + (0.4 · 3/4 + 0.6 · 1/3)v(s4) 
Robust: adversarial α’s 
v(s) = min α∈∆2 
(α1 · 1/4 + α2 · 2/3)v(s3) + (α1 · 3/4 + α2 · 1/3)v(s4) 
 
Reducing Performance Loss 
Standard aggregation 
return(π?)− return(π̃) ≤ 4 γ 
(1− γ)2 min v∈RS 
‖v? − Φv‖∞ 
Uniform weights incorrect = large error 
Robust aggregation 
return(π?)− return(π̃) ≤ 2 
1− γ min v∈RS 
‖v? − Φv‖∞ 
 
 
 
 
 
Reducing Performance Loss 
Standard aggregation 
return(π?)− return(π̃) ≤ 4 γ 
(1− γ)2 min v∈RS 
‖v? − Φv‖∞ 
Uniform weights incorrect = large error 
Robust aggregation 
return(π?)− return(π̃) ≤ 2 
1− γ min v∈RS 
‖v? − Φv‖∞ 
 
 
 
 
 
Reducing Performance Loss 
Standard aggregation 
return(π?)− return(π̃) ≤ 4 γ 
(1− γ)2 min v∈RS 
‖v? − Φv‖∞ 
Uniform weights incorrect = large error 
Robust aggregation 
return(π?)− return(π̃) ≤ 2 
1− γ min v∈RS 
‖v? − Φv‖∞ 
Bound constant 
γ standard robust 
0.9 360 20 0.99 36,000 200 
0.999 4,000,000 2,000 
 
Numerical Simulation: Inverted Pendulum 
Inverted pendulum with additional reward for off-balance 
Regular 
0 2 4 6 8 10 
Time (s) 
−1.5 
−1.0 
−0.5 
0.0 
0.5 
1.0 
1.5 
 
 
Robust 
0 20 40 60 80 100 
Time (s) 
−1.5 
−1.0 
−0.5 
0.0 
0.5 
1.0 
1.5 
A ng 
le 
 
Error 2: Limited Data Availability 
What is missing in this data? 
● 
 
 
 
 
 
 
 
 
●● 
● 
 
 
● 
 
 
 
 
 
 
● 
 
 
 
 
 
 
 
 
● 
● 
 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 
Time Step 
P op 
ul at 
io n 
Action 
0 
1 
2 
3 
Simulated Population and Actions 
 
Error 2: Limited Data Availability 
Learn model and confidence: Uncertain values of P 
Percentile criterion: Confidence level: δ, e.g. δ = 0.1 [Delage and 
Mannor, 2010, Petrik and Russell, 2019] 
max π,y 
y s.t. PP ? [return(π, P ?, r) ≥ y] ≥ 1− δ 
Risk aversion: same formulation, risk-averse to epistemic uncertainty 
max π 
V@R1−δ P ? [return(π, P ?, r)] 
Why this objective? 
 
 
Error 2: Limited Data Availability 
Learn model and confidence: Uncertain values of P 
Percentile criterion: Confidence level: δ, e.g. δ = 0.1 [Delage and 
Mannor, 2010, Petrik and Russell, 2019] 
max π,y 
y s.t. PP ? [return(π, P ?, r) ≥ y] ≥ 1− δ 
Risk aversion: same formulation, risk-averse to epistemic uncertainty 
max π 
V@R1−δ P ? [return(π, P ?, r)] 
Why this objective? Robust, guarantees, know when you fail 
 
Percentile Criterion as RMDP 
Percentile criterion [Delage and Mannor, 2010, Petrik and Russell, 2019] 
max π,y 
y s.t. PP ? [return(π, P ?, r) ≥ y] ≥ 1− δ 
Ambiguity set P designed such that: 
PP ? 
[ return(π, P ?, r) ≥ min 
P∈P return(π, P , r̄) 
] ≥ 1− δ 
 
Robustness in face of limited data 
Frequentist framework 
[+] Few assumptions 
[+] Simple to implement 
[-] Too conservative / useless? 
[-] Cannot generalize 
 
 
 
 
 
 
 
Robustness in face of limited data 
Frequentist framework 
[+] Few assumptions 
[+] Simple to implement 
[-] Too conservative / useless? 
[-] Cannot generalize 
Bayesian framework 
[-] Needs priors 
[+] Can use priors 
[-] Computationally demanding 
[+] Good generalization 
Frameworks have different types of guarantees e.g. [Murphy, 2012] 
 
Frequentist Ambiguity Set 
Few samples −→ large ambiguity set 
Hoeffding’s Ineq.: For true p? with prob. 1− δ: e.g. [Weissman et al., 2003, 
Jaksch et al., 2010, Laroche et al., 2019, Petrik and Russell, 2019] 
‖p?s,a − p̄s,a‖1 ≤ √ 
2 
n log 
( SA 2S 
δ 
) ︸ ︷︷ ︸ 
ψs,a 
Ambiguity set for s and a: 
P = {p : ‖p− p̄s,a‖1 ≤ ψs,a} 
Very conservative ... can use bootstrapping? 
 
Bayesian Models for Robust RL 
1. Uninformative models: Dirichlet prior for the probability distribution for each state and action. Dirichlet posterior. 
ps,a ∼ Dirichlet(α1, . . . , αS) 
2. Informative models: A parametric hierarchical Bayesian model. Population at time t is xt : 
xt+1 = α · xt + β · x2 t +N (1, 10) 
MCMC to sample from posterior over α, β Generalize to infinite state space 
 
Hierarchical Bayesian Models: Factored Models MCMC using Stan, JAGS, PyMC3/4, Edward, . . . to model population at time t is xt : 
xt+1 = α · xt + β · x2 t +N (1, 10) 
Larger population −→ more uncertainty 
0 
50 
100 
0 10 20 30 40 50 
Population at T 
M ea 
n P 
op ul 
at io 
n at 
 T + 
1 Posterior Samples 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 
Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
 
 
 
 
 
 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 
Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 
 
 
 
 
 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 
1. Frequentist: ψ = √ 
2/n log (2S/δ) = 0.8 
v̂(s0) = min p:‖p̄−p‖1≤0.8 
rTp = 2.1 
 
 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 1. Frequentist: v̂(s0) = minp:‖p̄−p‖1≤0.8 r 
Tp = 2.1 2. Bayes Credible Region: Posterior: p ∼ Dirichlet(5, 7, 1), samples: 
p1 = 
0.2 0.7 0.1 
 , p2 = 
0.6 0.3 0.1 
 , . . . 
Set ψ such that 80% of pi satisfy: 
‖pi − p̄‖1 ≤ ψ = 0.8 
 
 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 
Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 
1. Frequentist: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
2. Bayes Credible Region: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
3. Direct Bayes Bound: δ-quantile of values rTpi: 
v̂(s0) = V@R0.8 pi [rTpi] = 5.8 
 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 
Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 
1. Frequentist: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
2. Bayes Credible Region: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
3. Direct Bayes Bound: δ-quantile of values rTpi: 
v̂(s0) = V@R0.8 pi [rTpi] = 5.8 
Bayesian credible regions as ambiguity sets are too large 
 
 
 
 
Samples to Ambiguity Set: Single State Value, δ = 0.2 
Problem: p?(s1, s2, s3|s0) = [0.3, 0.5, 0.2], r(s1, s2, s3|s0) = [10, 5,−1] 
True value: v(s0) = rTp? = 6.3 
Samples: 4× (s0 → s1), 6× (s0 → s2), 1× (s0 → s3) 
1. Frequentist: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
2. Bayes Credible Region: v̂(s0) = minp:‖p̄−p‖1≤0.8 r Tp = 2.1 
3. Direct Bayes Bound: δ-quantile of values rTpi: 
v̂(s0) = V@R0.8 pi [rTpi] = 5.8 
Bayesian credible regions as ambiguity sets are too large 
4. RSVF: Approximates optimal ambiguity set P [Petrik and Russell, 2019] 
v̂(s0) = min p∈P 
rTp = 5.8 
 
Optimal Bayesian Ambiguity Sets 
Credible Region 
s1 s2 
s3 
 
0.00 
0.25 
0.50 
0.75 
0.00 0.25 0.50 0.75 1.00 
Optimal set for v = [0, 0, 1] 
s1 s2 
s3 
0.00 
0.25 
0.50 
0.75 
0.00 0.25 0.50 0.75 1.00 
The blue set is optimal (if it exists) for all non-random v [Gupta, 2015, 
Petrik and Russell, 2019] 
RSVF outer-approximates the optimal blue set 
 
Optimal Bayesian Ambiguity Sets 
Credible Region 
s1 s2 
s3 
 
0.00 
0.25 
0.50 
0.75 
0.00 0.25 0.50 0.75 1.00 
Optimal set for v = [1, 0, 0] 
s1 s2 
s3 
0.00 
0.25 
0.50 
0.75 
0.00 0.25 0.50 0.75 1.00 
The blue set is optimal (if it exists) for all non-random v [Gupta, 2015, 
Petrik and Russell, 2019] 
RSVF outer-approximates the optimal blue set 
 
Bayesian Credible Regions are Too Large: Why? 
Credible region Ps,a guarantees 
PP ? 
[ min p∈Ps,a 
pTv ≤ (p?s,a) Tv, ∀v ∈ RS 
] ≥ 1− δ. 
But this is sufficient: 
PP ? 
[ min p∈Ps,a 
pTv ≤ (p?s,a) Tv 
] ≥ 1− δ, ∀v ∈ RS 
Because v is not a random variable 
 
How Conservative are Robustness Estimates 
Population model: Gap of the lower bound. Smaller is better; 0 
unachievable. 
20 40 60 80 100 Number of samples 
0 
20 
40 
60 
80 
100 
Ca lcu 
la te 
d re 
tu rn 
 e rro 
r: |ρ 
* 
− ρ( ξ) 
| Mean Transition Hoeffding Hoeffding Monotone BCI RSVF 
Mean: Point est. BCI: Bayesian CI RSVF: Near-optimal Bayesian 
 
Other Approaches 
 
Other Objectives 
1. Robust objective 
max π 
min P ,r 
return(π, P , r) 
2. Minimize robust regret e.g. [Ahmed et al., 2013, Ahmed and Jaillet, 2017, Regan and 
Boutilier, 2009] 
min π 
max π?,P ,r 
( return(π?, P , r)− return(π, P , r) 
) All NP hard optimization problems 
3. Minimize baseline regret: Improve on a given policy πB [Petrik 
et al., 2016, Kallus and Zhou, 2018] 
min π 
max P ,r 
( return(πB, P , r)− return(π, P , r) 
) Also NP hard optimization problem 
 
Guarantee Policy Improvement [Petrik et al., 2016] 
Baseline policy πB: Currently deployed, good but would like an improvement 
Goal: Guarantee improvement on baseline policy 
Algorithm: Minimize robust baseline regret 
 
Solution Quality vs Samples 
200 400 600 800 1000 1200 1400 1600 
Number of samples 
−15 
−10 
−5 
0 
5 
10 
15 
Im pr 
ov em 
en to 
ve rb 
as el 
in e 
(% ) Plain solution 
 
Safe Policy Using Robust MDP I Compute a robust policy: 
π̃ ← arg max π 
min ξ 
return(π, ξ) 
I Accept π̃ if outperforms πB with prob 1− δ: 
min ξ 
return(π̃, ξ) ≥ max ξ 
return(πB, ξ) 
Reject 
Baseline Improved 0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
 
 
Accept 
Baseline Improved 0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
R et 
ur n 
 
Benchmark: Robust Solution 
200 400 600 800 1000 1200 1400 1600 
Number of samples 
−15 
−10 
−5 
0 
5 
10 
15 
Im pr 
ov em 
en to 
ve rb 
as el 
in e 
(% ) Plain solution 
Simple robust 
 
Limitation of Simple Robustness: Improving Commute 
Usual commute Better commute? 
Interstate: 20 min Local road: 10 min Bridge: 10–30 min Bridge: 10–30 min 
Total: 30–50 min Total: 20–40 min 
Reject: 40 min > 30 min 
 
Minimizing Robust Baseline Regret 
I Minimize robust baseline regret 
min π 
max ξ 
( return(πB, ξ)− return(π, ξ) 
) 
I Correlation between impacts of robustness 
Baseline Improved 0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
R et 
ur n 
0.0 0.2 0.4 0.6 0.8 1.0 
Model uncertainty ξ 
0.0 
0.5 
1.0 
1.5 
2.0 
2.5 
3.0 
R et 
ur n 
Baseline Improved 
 
Benchmark: Minimizing Robust Baseline Regret 
200 400 600 800 1000 1200 1400 1600 
Number of samples 
−15 
−10 
−5 
0 
5 
10 
15 
20 
Im pr 
ov em 
en to 
ve rb 
as el 
in e 
(% ) 
Plain solution Simple robust Joint robust 
 
Minimizing Robust Baseline Regret 
I Optimal stationary policy may have to be randomized 
I Arbitrary optimality gap for deterministic policies 
I Computing optimal deterministic policy is NP hard 
max π 
min ξ 
( return(π, ξ)− return(πB, ξ) 
) I Even computing nature response in NP hard 
min ξ 
( return(π, ξ)− return(πB, ξ) 
) I NP-hard even with rectangular uncertainty 
 
Performance Guarantees 
Model error: 
‖p?s,a − p̄s,a‖1 ≤ √ 
2 
n log 
( S A 2S 
δ 
) ︸ ︷︷ ︸ 
e(s,a) 
Classic performance loss: 
return(π?)− return(π̃)︸ ︷︷ ︸ Policy loss 
≤ C max π ‖eπ‖∞︸ ︷︷ ︸ 
L∞norm 
Performance loss (regret) for robust solution: 
return(π?)− return(π̃)︸ ︷︷ ︸ Policy loss 
≤ min { C ‖eπ?‖1,u?︸ ︷︷ ︸ 
L1 norm 
, return(π?)− return(πB)︸ ︷︷ ︸ Baseline loss 
} 
 
Summary 
 
Robustness is Important In RL 
1. Learning without a simulator: I Insufficient data set size I How to test a policy? No cross-validation 
2. High cost of failure (bad policy) 
Return: $8,820 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Nominal Transitions 
⇒ 
Return: −$6,725 
0 
10 
20 
30 
40 
50 
0 10 20 30 40 50 Population at T 
P op 
ul at 
io n 
at  T 
+ 1 
Noisy Transitions 
 
RL with Robust MDPs 
“Model-based approach to reliable off-policy sample-efficient tabular RL by learning models and confidence” 
I RMDPs are a convenient model for robustness I Tractable methods with rectangular sets I Provide strong guarantees 
I Learn a model and its confidence I Source of error matters I Promising methods for small data 
I Many model-free methods too e.g. [Thomas et al., 2015, Pinto et al., 2017, 
Pattanaik et al., 2018] 
 
Important Research Directions 
1. Scalability [Tamar et al., 2014] 
I Value function approximation: Deep learning et al I How to preserve some sort of guarantees? 
2. Relaxing rectangularity I Crucial in reducing unnecessary conservativeness I Tractability? 
3. Applications I Understand the real impact and limitations of the techniques 
4. Code: http://github.com/marekpetrik/craam2, well-tested, examples, but unstable, pre-alpha 
 
Bibliography I 
A. Ahmed and P. Jaillet. Sampling Based Approaches for Minimizing Regret in Uncertain Markov Decision Processes ( MDPs ). Journal of Artificial Intelligence Research (JAIR), 59:229–264, 2017. 
A. Ahmed, P. Varakantham, Y. Adulyasak, and P. Jaillet. Regret based Robust Solutions for Uncertain Markov Decision Processes. In Advances in Neural Information Pro-cessing Systems (NIPS), 2013. URL http://papers.nips.cc/paper/ 
4970-regret-based-robust-solutions-for-uncertain-markov-decision-processes. 
P. Auer, T. Jaksch, and R. Ortner. Near-optimal regret bounds for reinforcement learning. Journal of Machine Learning Research, 11(1): 1563–1600, 2010. 
J. Bagnell. Learning decisions: Robustness, uncertainty, and approximation. PhD thesis, Carnegie Mellon University, 2004. URL http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1. 
1.187.8389{&}rep=rep1{&}type=pdf. 
A. Ben-Tal, L. El Ghaoui, and A. Nemirovski. Robust Optimization. Princeton University Press, 2009. 
 
Bibliography II 
A. Condon. On algorithms for simple stochastic games. Advances in Computational Complexity Theory, DIMACS Series in Discrete Mathematics and Theoretical Computer Science, 13:51–71, 1993. doi: 10.1090/dimacs/013/04. 
E. Delage and S. Mannor. Percentile Optimization for Markov Decision Processes with Parameter Uncertainty. Operations Research, 58(1): 203–213, aug 2010. ISSN 0030-364X. doi: 10.1287/opre.1080.0685. URL http: 
//or.journal.informs.org/cgi/doi/10.1287/opre.1080.0685. 
K. V. Delgado, L. N. De Barros, D. B. Dias, and S. Sanner. Real-time dynamic programming for Markov decision processes with imprecise probabilities. Artificial Intelligence, 230:192–223, 2016. ISSN 00043702. doi: 10.1016/j.artint.2015.09.005. URL http://dx.doi.org/10.1016/j.artint.2015.09.005. 
E. Derman, D. Mankowitz, T. Mann, and S. Mannor. A Bayesian Approach to Robust Reinforcement Learning. Technical report, 2019. URL http://arxiv.org/abs/1905.08188. 
 
Bibliography III 
J. Filar and K. Vrieze. Competitive Markov Decision Processes. Springer, 1997. URL http://dl.acm.org/citation.cfm?id=248676. 
R. Givan, S. Leach, and T. Dean. Bounded-parameter Markov decision processes. Artificial Intelligence, 122(1):71–109, 2000. 
G. J. Gordon. Stable function approximation in dynamic programming. In International Conference on Machine Learning, pages 261–268. Carnegie Mellon University, 1995. URL citeseer.ist.psu.edu/gordon95stable.html. 
V. Goyal and J. Grand-Clement. Robust Markov Decision Process: Beyond Rectangularity. Technical report, 2018. URL http://arxiv.org/abs/1811.00215. 
V. Gupta. Near-Optimal Bayesian Ambiguity Sets for Distributionally Robust Optimization. 2015. 
C. P. Ho, M. Petrik, and W. Wiesemann. Fast Bellman Updates for Robust MDPs. In International Conference on Machine Learning (ICML), volume 80, pages 1979–1988, 2018. URL http://proceedings.mlr.press/v80/ho2018a.html. 
 
Bibliography IV 
G. N. Iyengar. Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280, may 2005a. ISSN 0364-765X. doi: 10.1287/moor.1040.0129. URL http: 
//mor.journal.informs.org/content/30/2/257.shorthttp:// 
mor.journal.informs.org/cgi/doi/10.1287/moor.1040.0129. 
G. N. Iyengar. Robust Dynamic Programming. Mathematics of Operations Research, 30(2):257–280, 2005b. ISSN 0364-765X. doi: 10.1287/moor.1040.0129. URL http: 
//pubsonline.informs.org/doi/abs/10.1287/moor.1040.0129. 
T. Jaksch, R. Ortner, and P. Auer. Near-optimal Regret Bounds for Reinforcement Learning. Journal of Machine Learning Research, 11(1): 1563–1600, 2010. URL http://eprints.pascal-network.org/archive/00007081/. 
N. Kallus and A. Zhou. Confounding-Robust Policy Improvement. In Neural Information Processing Systems (NIPS), 2018. URL http://arxiv.org/abs/1805.08593. 
 
Bibliography V 
D. L. Kaufman and A. J. Schaefer. Robust modified policy iteration. INFORMS Journal on Computing, 25(3):396–410, 2013. URL http://joc.journal.informs.org/content/early/2012/06/06/ 
ijoc.1120.0509.abstract. 
M. Kery and M. Schaub. Bayesian Population Analysis Using WinBUGS. 2012. ISBN 9780123870209. doi: 10.1016/B978-0-12-387020-9.00024-9. 
R. Laroche, P. Trichelair, and R. T. des Combes. Safe Policy Improvement with Baseline Bootstrapping. In International Conference of Machine Learning (ICML), 2019. URL http://arxiv.org/abs/1712.06924. 
Y. Le Tallec. Robust, Risk-Sensitive, and Data-driven Control of Markov Decision Processes. PhD thesis, MIT, 2007. 
S. H. Lim and A. Autef. Kernel-Based Reinforcement Learning in Robust Markov Decision Processes. In International Conference of Machine Learning (ICML), 2019. 
 
Bibliography VI 
S. Mannor, O. Mebel, and H. Xu. Lightning does not strike twice: Robust MDPs with coupled uncertainty. In International Conference on Machine Learning (ICML), 2012. URL http://arxiv.org/abs/1206.4643. 
K. Murphy. Machine Learning: A Probabilistic Perspective. 2012. ISBN 9780262018029. doi: 10.1007/SpringerReference 35834. URL http://link.springer.com/chapter/10.1007/ 
978-94-011-3532-0{_}2. 
A. Nilim and L. El Ghaoui. Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5): 780–798, sep 2005. ISSN 0030-364X. doi: 10.1287/opre.1050.0216. URL http: 
//or.journal.informs.org/cgi/doi/10.1287/opre.1050.0216. 
A. Pattanaik, Z. Tang, S. Liu, G. Bommannan, and G. Chowdhary. Robust Deep Reinforcement Learning with Adversarial Attacks. In International Conference on Autonomous Agents and MultiAgent Systems (AAMAS), 2018. URL http://arxiv.org/abs/1712.03632. 
 
Bibliography VII 
M. Petrik. Approximate dynamic programming by minimizing distributionally robust bounds. In International Conference of Machine Learning (ICML), 2012. URL http://arxiv.org/abs/1205.1782. 
M. Petrik and R. H. Russell. Beyond Confidence Regions: Tight Bayesian Ambiguity Sets for Robust MDPs. Technical report, 2019. URL https://arxiv.org/pdf/1902.07605.pdf{%}0Ahttp: 
//arxiv.org/abs/1902.07605. 
M. Petrik and D. Subramanian. RAAM : The benefits of robustness in approximating aggregated MDPs in reinforcement learning. In Neural Information Processing Systems (NIPS), 2014. 
M. Petrik, Mohammad Ghavamzadeh, and Y. Chow. Safe Policy Improvement by Minimizing Robust Baseline Regret. In Advances in Neural Information Processing Systems (NIPS), 2016. 
L. Pinto, J. Davidson, R. Sukthankar, and A. Gupta. Robust Adversarial Reinforcement Learning. Technical report, 2017. URL http://arxiv.org/abs/1703.02702. 
 
Bibliography VIII 
M. L. Puterman. Markov decision processes: Discrete stochastic dynamic programming. 2005. 
K. Regan and C. Boutilier. Regret-based reward elicitation for Markov decision processes. In Conference on Uncertainty in Artificial Intelligence (UAI), pages 444–451, 2009. ISBN 978-0-9749039-5-8. 
J. Satia and R. Lave. Markovian decision processes with uncertain transition probabilities. Operations Research, 21:728–740, 1973. URL http://www.jstor.org/stable/10.2307/169381. 
H. E. Scarf. A min-max solution of an inventory problem. In Studies in the Mathematical Theory of Inventory and Production, chapter Chapter 12. 1958. 
A. Shapiro, D. Dentcheva, and A. Ruszczynski. Lectures on stochastic programming: Modeling and theory. 2014. ISBN 089871687X. doi: http://dx.doi.org/10.1137/1.9780898718751. 
A. Tamar, S. Mannor, and H. Xu. Scaling up Robust MDPs Using Function Approximation. In International Conference of Machine Learning (ICML), 2014. 
 
Bibliography IX 
P. S. Thomas, G. Teocharous, and M. Ghavamzadeh. High Confidence Off-Policy Evaluation. In Annual Conference of the AAAI, 2015. 
A. Tirinzoni, X. Chen, M. Petrik, and B. D. Ziebart. Policy-Conditioned Uncertainty Sets for Robust Markov Decision Processes. In Neural Information Processing Systems (NIPS), 2018. 
J. N. Tsitsiklis and B. Van Roy. An analysis of temporal-difference learning with function approximation. IEEE Transactions on Automatic Control, 42(5):674–690, 1997. URL citeseer.ist.psu.edu/article/tsitsiklis96analysis.html. 
T. Weissman, E. Ordentlich, G. Seroussi, S. Verdu, and M. J. Weinberger. Inequalities for the L1 deviation of the empirical distribution. jun 2003. 
C. White and H. Eldeib. Markov decision processes with imprecise transition probabilities. Operations Research, 42(4):739–749, 1994. URL http://or.journal.informs.org/content/42/4/739.short. 
 
Bibliography X 
W. Wiesemann, D. Kuhn, and B. Rustem. Robust Markov decision processes. Mathematics of Operations Research, 38(1):153–183, 2013. ISSN 0364-765X. doi: 10.1287/moor.1120.0540. URL http://mor. 
journal.informs.org/cgi/doi/10.1287/moor.1120.0540. 
H. Xu, C. Caramanis, S. Mannor, and S. Member. Robust regression and Lasso. IEEE Transactions on Information Theory, 56(7):3561–3574, 2010. 
Y. Zhang, L. N. Steimle, and B. T. Denton. Robust Markov Decision Processes for Medical Treatment Decisions. Technical report, 2017. 
 