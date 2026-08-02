> Source: https://arxiv.org/pdf/1106.0234

Journal of Artiial Intelligene Researh 13 (2000) 33{94 Submitted 9/99; published 8/00 
Value-Funtion Approximations for Partially Observable 
Markov Deision Proesses 
Milos Hauskreht miloss.brown.edu 
Computer Siene Department, Brown University 
Box 1910, Brown University, Providene, RI 02912, USA 
Abstrat 
Partially observable Markov deision proesses (POMDPs) provide an elegant math-
ematial framework for modeling omplex deision and planning problems in stohasti 
domains in whih states of the system are observable only indiretly, via a set of imperfet 
or noisy observations. The modeling advantage of POMDPs, however, omes at a prie | 
exat methods for solving them are omputationally very expensive and thus appliable 
in pratie only to very simple problems. We fous on eÆient approximation (heuristi) 
methods that attempt to alleviate the omputational problem and trade o auray for 
speed. We have two objetives here. First, we survey various approximation methods, 
analyze their properties and relations and provide some new insights into their dierenes. 
Seond, we present a number of new approximation methods and novel renements of ex-
isting tehniques. The theoretial results are supported by experiments on a problem from 
the agent navigation domain. 
1. Introdution 
Making deisions in dynami environments requires areful evaluation of the ost and ben-
ets not only of the immediate ation but also of hoies we may have in the future. This 
evaluation beomes harder when the eets of ations are stohasti, so that we must pur-
sue and evaluate many possible outomes in parallel. Typially, the problem beomes more 
omplex the further we look into the future. The situation beomes even worse when the 
outomes we an observe are imperfet or unreliable indiators of the underlying proess 
and speial ations are needed to obtain more reliable information. Unfortunately, many 
real-world deision problems fall into this ategory. 
Consider, for example, a problem of patient management. The patient omes to the 
hospital with an initial set of omplaints. Only rarely do these allow the physiian (deision-
maker) to diagnose the underlying disease with ertainty, so that a number of disease options 
generally remain open after the initial evaluation. The physiian has multiple hoies in 
managing the patient. He/she an hoose to do nothing (wait and see), order additional tests 
and learn more about the patient state and disease, or proeed to a more radial treatment 
(e.g. surgery). Making the right deision is not an easy task. The disease the patient suers 
an progress over time and may beome worse if the window of opportunity for a partiular 
eetive treatment is missed. On the other hand, seletion of the wrong treatment may 
make the patient's ondition worse, or may prevent applying the orret treatment later. 
The result of the treatment is typially non-deterministi and more outomes are possible. 
In addition, both treatment and investigative hoies ome with dierent osts. Thus, in 
 
2000 AI Aess Foundation and Morgan Kaufmann Publishers. All rights reserved.
Hauskreht 
a ourse of patient management, the deision-maker must arefully evaluate the osts and 
benets of both urrent and future hoies, as well as their interation and ordering. Other 
deision problems with similar harateristis | omplex temporal ost-benet tradeos, 
stohastiity, and partial observability of the underlying ontrolled proess | inlude robot 
navigation, target traking, mahine mantainane and replaement, and the like. 
Sequential deision problems an be modeled as Markov deision proesses (MDPs) 
(Bellman, 1957; Howard, 1960; Puterman, 1994; Boutilier, Dean, & Hanks, 1999) and their 
extensions. The model of hoie for problems similar to patient management is the partially 
observable Markov deision proess (POMDP) (Drake, 1962; Astrom, 1965; Sondik, 1971; 
Lovejoy, 1991b). The POMDP represents two soures of unertainty: stohastiity of the 
underlying ontrolled proess (e.g. disease dynamis in the patient management problem), 
and imperfet observability of its states via a set of noisy observations (e.g. symptoms, 
ndings, results of tests). In addition, it lets us model in a uniform way both ontrol and 
information-gathering (investigative) ations, as well as their eets and ost-benet trade-
os. Partial observability and the ability to model and reason with information-gathering 
ations are the main features that distinguish the POMDP from the widely known fully 
observable Markov deision proess (Bellman, 1957; Howard, 1960). 
Although useful from the modeling perspetive, POMDPs have the disadvantage of be-
ing hard to solve (Papadimitriou & Tsitsiklis, 1987; Littman, 1996; Mundhenk, Goldsmith, 
Lusena, & Allender, 1997; Madani, Hanks, & Condon, 1999), and optimal or -optimal solu-
tions an be obtained in pratie only for problems of low omplexity. A hallenging goal in 
this researh area is to exploit additional strutural properties of the domain and/or suitable 
approximations (heuristis) that an be used to obtain good solutions more eÆiently. 
We fous here on heuristi approximation methods, in partiular approximations based 
on value funtions. Important researh issues in this area are the design of new and eÆient 
algorithms, as well as a better understanding of the existing tehniques and their relations, 
advantages and disadvantages. In this paper we address both of these issues. First, we 
survey various value-funtion approximations, analyze their properties and relations and 
provide some insights into their dierenes. Seond, we present a number of new methods 
and novel renements of existing tehniques. The theoretial results and ndings are also 
supported empirially on a problem from the agent navigation domain. 
2. Partially Observable Markov Deision Proesses 
A partially observable Markov deision proess (POMDP) desribes a stohasti ontrol 
proess with partially observable (hidden) states. Formally, it orresponds to a tuple 
(S;A;; T;O;R) where S is a set of states, A is a set of ations,  is a set of observations, 
T : SAS ! [0; 1℄ is a set of transition probabilities that desribe the dynami behavior 
of the modeled environment, O : SA! [0; 1℄ is a set of observation probabilities that 
desribe the relationships among observations, states and ations, and R : S A S ! IR 
denotes a reward model that assigns rewards to state transitions and models payos asso-
iated with suh transitions. In some instanes the denition of a POMDP also inludes an 
a priori probability distribution over the set of initial states S. 
34
Value-Funtion Approximations for POMDPs 
s 
a 
o 
s 
o 
t−1 a 
o 
a 
o 
a 
o 
r 
Figure 1: Part of the inuene diagram desribing a POMDP model. Retangles orrespond 
to deision nodes (ations), irles to random variables (states) and diamonds to 
reward nodes. Links represent the dependenies among the omponents. s 
t 
; a 
t 
; o 
t 
and r 
t 
denote state, ation, observation and reward at time t. Note that an ation 
at time t depends only on past observations and ations, not on states. 
2.1 Objetive Funtion 
Given a POMDP, the goal is to onstrut a ontrol poliy that maximizes an objetive (value) 
funtion. The objetive funtion ombines partial (stepwise) rewards over multiple steps 
using various kinds of deision models. Typially, the models are umulative and based on 
expetations. Two models are frequently used in pratie: 
 a nite-horizon model in whih we maximize E( 
P 
T 
t=0 
r 
t 
), where r 
t 
is a reward obtained 
at time t. 
 an innite-horizon disounted model in whih we maximize E( 
P 
1 
t=0 
 
t 
r 
t 
), where 0 < 
 < 1 is a disount fator. 
Note that POMDPs and umulative deision models provide a rih language for modeling 
various ontrol objetives. For example, one an easily model goal-ahievement tasks (a 
spei goal must be reahed) by giving a large reward for a transition to that state and 
zero or smaller rewards for other transitions. 
In this paper we fous primarily on disounted innite-horizon model. However, the 
results an be easily applied also to the nite-horizon ase. 
2.2 Information State 
In a POMDP the proess states are hidden and we annot observe them while making a 
deision about the next ation. Thus, our ation hoies are based only on the informa-
tion available to us or on quantities derived from that information. This is illustrated in 
the inuene diagram in Figure 1, where the ation at time t depends only on previous 
observations and ations, not on states. Quantities summarizing all information are alled 
information states. Complete information states represent a trivial ase. 
35
Hauskreht 
s 
a 
s 
o 
I I 
a 
I I 
r 
r 
Figure 2: Inuene diagram for a POMDP with information states and orresponding 
information-state MDP. Information states (I 
t 
and I 
t+1 
) are represented by 
double-irled nodes. An ation hoie (retangle) depends only on the urrent 
information state. 
Denition 1 (Complete information state). The omplete information state at time t (de-
noted I 
C 
t 
) onsists of: 
 a prior belief b 
0 
on states in S at time 0; 
 a omplete history of ations and observations fo 
0 
; a 
0 
; o 
1 
; a 
1 
;    ; o 
t 1 
; a 
t 1 
; o 
t 
g start-
ing from time t = 0. 
A sequene of information states denes a ontrolled Markov proess that we all an 
information-state Markov deision proess or information-state MDP. The poliy for the 
information-state MDP is dened in terms of a ontrol funtion  : I ! A mapping 
information state spae to ations. The new information state (I 
t 
) is a deterministi funtion 
of the previous state (I 
t 1 
), the last ation (a 
t 1 
) and the new observation (o 
t 
): 
I 
t 
= (I 
t 1 
; o 
t 
; a 
t 1 
): 
 : I A! I is the update funtion mapping the information state spae, observations 
and ations bak to the information spae. 
1 
It is easy to see that one an always onvert 
the original POMDP into the information-state MDP by using omplete information states. 
The relation between the omponents of the two models and a sketh of a redution of a 
POMDP to an information-state MDP, are shown in Figure 2. 
2.3 Bellman Equations for POMDPs 
An information-state MDP for the innite-horizon disounted ase is like a fully-observable 
MDP and satises the standard xed-point (Bellman) equation: 
V 
 
(I) = max 
a2A 
( 
(I; a) +  
X 
I 
0 
P (I 
0 
jI; a)V 
 
(I 
0 
) 
) 
: (1) 
1. In this paper,  denotes the generi update funtion. Thus we use the same symbol even if the information 
state spae is dierent. 
36
Value-Funtion Approximations for POMDPs 
Here, V 
 
(I) denotes the optimal value funtion maximizing E( 
P 
1 
t=0 
 
t 
r 
t 
) for state I. (I; a) 
is the expeted one-step reward and equals 
(I; a) = 
X 
s2S 
(s; a)P (sjI) = 
X 
s2S 
X 
s 
0 
2S 
R(s; a; s 
0 
)P (s 
0 
js; a)P (sjI): 
(s; a) denotes an expeted one-step reward for state s and ation a. 
Sine the next information state I 
0 
= (I; o; a) is a deterministi funtion of the previous 
information state I, ation a, and the observation o, the Equation 1 an be rewritten more 
ompatly by summing over all possible observations : 
V 
 
(I) = max 
a2A 
( 
X 
s2S 
(s; a)P (sjI) +  
X 
o2 
P (ojI; a)V 
 
((I; o; a)) 
) 
: (2) 
The optimal poliy (ontrol funtion)  
 
: I ! A selets the value-maximizing ation 
 
 
(I) = argmax 
a2A 
( 
X 
s2S 
(s; a)P (sjI) +  
X 
o2 
P (ojI; a)V 
 
((I; o; a)) 
) 
: (3) 
The value and ontrol funtions an be also expressed in terms of ation-value funtions 
(Q-funtions) 
V 
 
(I) = max 
a2A 
Q 
 
(I; a)  
 
(I) = argmax 
a2A 
Q 
 
(I; a); 
Q 
 
(I; a) = 
X 
s2S 
(s; a)P (sjI) +  
X 
o2 
P (ojI; a)V 
 
((I; o; a)): (4) 
A Q-funtion orresponds to the expeted reward for hosing a xed ation (a) in the rst 
step and ating optimally afterwards. 
2.3.1 Suffiient Statistis 
To derive Equations 1|3 we impliitly used omplete information states. However, as 
remarked earlier, the information available to the deision-maker an be also summarized 
by other quantities. We all them suÆient information states. Suh states must preserve 
the neessary information ontent and also the Markov property of the information-state 
deision proess. 
Denition 2 (SuÆient information state proess). Let I be an information state spae 
and  : I  A   ! I be an update funtion dening an information proess I 
t 
= 
(I 
t 1 
; a 
t 1 
; o 
t 
). The proess is suÆient with regard to the optimal ontrol when, for any 
time step t, it satises 
P (s 
t 
jI 
t 
) = P (s 
t 
jI 
C 
t 
) 
P (o 
t 
jI 
t 1 
; a 
t 1 
) = P (o 
t 
jI 
C 
t 1 
; a 
t 1 
); 
where I 
C 
t 
and I 
C 
t 1 
are omplete information states. 
It is easy to see that Equations 1 | 3 for omplete information states must hold also for 
suÆient information states. The key benet of suÆient statistis is that they are often 
37
Hauskreht 
easier to manipulate and store, sine unlike omplete histories, they may not expand with 
time. For example, in the standard POMDP model it is suÆient to work with belief states 
that assign probabilities to every possible proess state (Astrom, 1965). 
2 
In this ase the 
Bellman equation redues to: 
V (b) = max 
a2A 
( 
X 
s2S 
(s; a)b(s) +  
X 
o2 
X 
s2S 
P (ojs; a)b(s)V ((b; o; a)) 
) 
; (5) 
where the next-step belief state b 
0 
is 
b 
0 
(s) = (b; o; a)(s) = P (ojs; a) 
X 
s 
0 
2S 
P (sja; s 
0 
)b(s 
0 
): 
 = 1=P (ojb; a) is a normalizing onstant. This denes a belief-state MDP whih is a 
speial ase of a ontinuous-state MDP. Belief-state MDPs are also the primary fous of 
our investigation in this paper. 
2.3.2 Value-Funtion Mappings and their Properties 
The Bellman equation 2 for the belief-state MDP an be also rewritten in the value-funtion 
mapping form. Let V be a spae of real-valued bounded funtions V : I ! IR dened on 
the belief information spae I, and let h : I AB ! IR be dened as 
h(b; a; V ) = 
X 
s2S 
(s; a)b(s) +  
X 
o2 
X 
s2S 
P (ojs; a)b(s)V ((b; o; a)): 
Now by dening the value funtion mapping H : V ! V as (HV )(b) = max 
a2A 
h(b; a; V ), 
the Bellman equation 2 for all information states an be written as V 
 
= HV 
 
: It is well 
known that H (for MDPs) is an isotone mapping and that it is a ontration under the 
supremum norm (see (Heyman & Sobel, 1984; Puterman, 1994)). 
Denition 3 The mapping H is isotone, if V;U 2 V and V  U implies HV  HU . 
Denition 4 Let k:k be a supremum norm. The mapping H is a ontration under the 
supremum norm, if for all V;U 2 V, kHV  HUk  kV   Uk holds for some 0   < 1. 
2.4 Value Iteration 
The optimal value funtion (Equation 2) or its approximation an be omputed using dy-
nami programming tehniques. The simplest approah is the value iteration (Bellman, 
1957) shown in Figure 3. In this ase, the optimal value funtion V 
 
an be determined 
in the limit by performing a sequene of value-iteration steps V 
i 
= HV 
i 1 
, where V 
i 
is the 
ith approximation of the value funtion (ith value funtion). 
3 
The sequene of estimates 
2. Models in whih belief states are not suÆient inlude POMDPs with observation and ation hannel 
lags (see Hauskreht (1997)). 
3. We note that the same update V 
i 
= HV 
i 1 
an be applied to solve the nite-horizon problem in a 
standard way. The dierene is that V 
i 
now stands for the i-steps-to-go value funtion and V 
0 
represents 
the value funtion (rewards) for end states. 
38
Value-Funtion Approximations for POMDPs 
Value iteration (POMDP , ) 
initialize V for all b 2 I; 
repeat 
V 
0 
 V ; 
update V  HV 
0 
for all b 2 I; 
until sup 
b 
j V (b)  V 
0 
(b) j  
return V; 
Figure 3: Value iteration proedure. 
onverges to the unique xed-point solution whih is the diret onsequene of Banah's 
theorem for ontration mappings (see, for example, Puterman (1994)). 
In pratie, we stop the iteration well before it reahes the limit solution. The stopping 
riterion we use in our algorithm (Figure 3) examines the maximum dierene between value 
funtions obtained in two onseutive steps | the so-alled Bellman error (Puterman, 1994; 
Littman, 1996). The algorithm stops when this quantity falls below the threshold . The 
auray of the approximate solution (ith value funtion) with regard to V 
 
an be expressed 
in terms of the Bellman error . 
Theorem 1 Let  = sup 
b 
jV 
i 
(b)   V 
i 1 
(b)j = kV 
i 
  V 
i 1 
k be the magnitude of the Bellman 
error. Then kV 
i 
  V 
 
k  
 
1  
and kV 
i 1 
  V 
 
k  
 
1  
hold. 
Then, to obtain the approximation of V 
 
with preision Æ the Bellman error should fall 
below 
Æ(1 ) 
 
. 
2.4.1 Pieewise Linear and Convex Approximations of the Value Funtion 
The major diÆulty in applying the value iteration (or dynami programming) to belief-
state MDPs is that the belief spae is innite and we need to ompute an update V 
i 
= HV 
i 1 
for all of it. This poses the following threats: the value funtion for the ith step may not 
be representable by nite means and/or omputable in a nite number of steps. 
To address this problem Sondik (Sondik, 1971; Smallwood & Sondik, 1973) showed that 
one an guarantee the omputability of the ith value funtion as well as its nite desription 
for a belief-state MDP by onsidering only pieewise linear and onvex representations of 
value funtion estimates (see Figure 4). In partiular, Sondik showed that for a pieewise 
linear and onvex representation of V 
i 1 
, V 
i 
= HV 
i 1 
is omputable and remains pieewise 
linear and onvex. 
Theorem 2 (Pieewise linear and onvex funtions). Let V 
0 
be an initial value funtion 
that is pieewise linear and onvex. Then the ith value funtion obtained after a nite 
number of update steps for a belief-state MDP is also nite, pieewise linear and onvex, 
and is equal to: 
V 
i 
(b) = max 
 
i 
2  
i 
X 
s2S 
b(s) 
i 
(s); 
where b and  
i 
are vetors of size jSj and   
i 
is a nite set of vetors (linear funtions)  
i 
. 
39
Hauskreht 
1b(s  ) 
V (b)i 
0 1 
Figure 4: A pieewise linear and onvex funtion for a POMDP with two proess states 
fs 
1 
; s 
2 
g. Note that b(s 
1 
) = 1  b(s 
2 
) holds for any belief state. 
The key part of the proof is that we an express the update for the ith value funtion 
in terms of linear funtions   
i 1 
dening V 
i 1 
: 
V 
i 
(b) = max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
max 
 
i 1 
2  
i 1 
X 
s 
0 
2S 
" 
X 
s2S 
P (s 
0 
; ojs; a)b(s) 
# 
 
i 1 
(s 
0 
) 
9 
= 
; 
: (6) 
This leads to a pieewise linear and onvex value funtion V 
i 
that an be represented by 
a nite set of linear funtions  
i 
, one linear funtion for every ombination of ations and 
permutations of  
i 1 
vetors of size jj. Let W = (a; fo 
1 
;  
j 
1 
i 1 
g; fo 
2 
;  
j 
2 
i 1 
g;    fo 
jj 
;  
j 
jj 
i 1 
g) 
be suh a ombination. Then the linear funtion orresponding to it is dened as 
 
W 
i 
(s) = (s; a) +  
X 
o2 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
j 
o 
i 1 
(s 
0 
): (7) 
Theorem 2 is the basis of the dynami programming algorithm for nding the optimal 
solution for the nite-horizon models and the value-iteration algorithm for nding near-
optimal approximations of V 
 
for the disounted, innite-horizon model. Note, however, 
that this result does not imply pieewise linearity of the optimal (xed-point) solution V 
 
. 
2.4.2 Algorithms for Computing Value-Funtion Updates 
The key part of the value-iteration algorithm is the omputation of value-funtion updates 
V 
i 
= HV 
i 1 
. Assume an ith value funtion V 
i 
that is represented by a nite number of linear 
segments ( vetors). The total number of all its possible linear funtions is jAjj  
i 1 
j 
jj 
(one 
for every ombination of ations and permutations of  
i 1 
vetors of size jj) and they an 
be enumerated in O(jAjjSj 
2 
j  
i 1 
j 
jj 
) time. However, the omplete set of linear funtions 
is rarely needed: some of the linear funtions are dominated by others and their omission 
does not hange the resulting pieewise linear and onvex funtion. This is illustrated in 
Figure 5. 
40
Value-Funtion Approximations for POMDPs 
1b(s  ) 
redundant linear     function 
V (b)i 
0 1 
Figure 5: Redundant linear funtion. The funtion does not dominate in any of the regions 
of the belief spae and an be exluded. 
A linear funtion that an be eliminated without hanging the resulting value funtion 
solution is alled redundant. Conversely, a linear funtion that singlehandedly ahieves the 
optimal value for at least one point of the belief spae is alled useful. 
4 
For the sake of omputational eÆieny it is important to make the size of the linear 
funtion set as small as possible (keep only useful linear funtions) over value-iteration steps. 
There are two main approahes for omputing useful linear funtions. The rst approah is 
based on a generate-and-test paradigm and is due to Sondik (1971) and Monahan (1982). 
The idea here is to enumerate all possible linear funtions rst, then test the usefulness 
of linear funtions in the set and prune all redundant vetors. Reent extensions of the 
method interleave the generate and test stages and do early pruning on a set of partially 
onstruted linear funtions (Zhang & Liu, 1997a; Cassandra, Littman, & Zhang, 1997; 
Zhang & Lee, 1998). 
The seond approah builds on Sondik's idea of omputing a useful linear funtion for a 
single belief state (Sondik, 1971; Smallwood & Sondik, 1973), whih an be done eÆiently. 
The key problem here is to loate all belief points that seed useful linear funtions and 
dierent methods address this problem dierently. Methods that implement this idea are 
Sondik's one- and two-pass algorithms (Sondik, 1971), Cheng's methods (Cheng, 1988), and 
the Witness algorithm (Kaelbling, Littman, & Cassandra, 1999; Littman, 1996; Cassandra, 
1998). 
2.4.3 Limitations and Complexity 
The major diÆulty in solving a belief-state MDP is that the omplexity of a pieewise 
linear and onvex funtion an grow extremely fast with the number of update steps. More 
speially, the size of a linear funtion set dening the funtion an grow exponentially (in 
the number of observations) during a single update step. Then, assuming that the initial 
value funtion is linear, the number of linear funtions dening the ith value funtion is 
O(jAj 
jj 
i 1 
). 
4. In dening redundant and useful linear funtions we assume that there are no linear funtion dupliates, 
i.e. only one opy of the same linear funtion is kept in the set   
i 
. 
41
Hauskreht 
The potential growth of the size of the linear funtion set is not the only bad news. As 
remarked earlier, a pieewise linear onvex value funtion is usually less omplex than the 
worst ase beause many linear funtions an be pruned away during updates. However, 
it turned out that the task of identifying all useful linear funtions is omputationally 
intratable as well (Littman, 1996). This means that one faes not only the potential 
super-exponential growth of the number of useful linear funtions, but also ineÆienies 
related to the identiation of suh vetors. This is a signiant drawbak that makes the 
exat methods appliable only to relatively simple problems. 
The above analysis suggests that solving a POMDP problem is an intrinsially hard 
task. Indeed, nding the optimal solution for the nite-horizon problem is PSPACE-hard 
(Papadimitriou & Tsitsiklis, 1987). Finding the optimal solution for the disounted innite-
horizon riterion is even harder. The orresponding deision problem has been shown to be 
undeidable (Madani et al., 1999), and thus the optimal solution may not be omputable. 
2.4.4 Strutural Refinements of the Basi Algorithm 
The standard POMDP model uses a at state spae and full transition and reward matries. 
However, in pratie, problems often exhibit more struture and an be represented more 
ompatly, for example, using graphial models (Pearl, 1988; Lauritzen, 1996), most often 
dynami belief networks (Dean & Kanazawa, 1989; Kjaerul, 1992) or dynami inuene 
diagrams (Howard & Matheson, 1984; Tatman & Shahter, 1990). 
5 
There are many ways 
to take advantage of the problem struture to modify and improve exat algorithms. For 
example, a renement of the basi Monahan algorithm to ompat transition and reward 
models has been studied by Boutilier and Poole (1996). A hybrid framework that ombines 
MDP-POMDP problem-solving tehniques to take advantage of perfetly and partially ob-
servable omponents of the model and the subsequent value funtion deomposition was 
proposed by Hauskreht (1997, 1998, 2000). A similar approah with perfet information 
about a region (subset of states) ontaining the atual underlying state was disussed by 
Zhang and Liu (1997b, 1997a). Finally, Casta~non (1997) and Yost (1998) explore tehniques 
for solving large POMDPs that onsist of a set of smaller, resoure-oupled but otherwise 
independent POMDPs. 
2.5 Extrating Control Strategy 
Value iteration allow us to ompute an ith approximation of the value funtion V 
i 
. However, 
our ulimate goal is to nd the optimal ontrol strategy  
 
: I ! A or its lose approximation. 
Thus our fous here is on the problem of extration of ontrol strategies from the results of 
value iteration. 
2.5.1 Lookahead Design 
The simplest way to dene the ontrol funtion  : I ! A from the value funtion V 
i 
is via 
greedy one-step lookahead: 
(b) = argmax 
a2A 
( 
X 
s2S 
(s; a)b(s) +  
X 
o2 
P (ojb; a)V 
i 
((b; o; a)) 
) 
: 
5. See the survey by Boutilier, Dean and Hanks (1999) for dierent ways to represent strutured MDPs. 
42
Value-Funtion Approximations for POMDPs 
1b(s  ) 
a1 
a1 
a3a2 
V (b)i 
0 1b 
Figure 6: Diret ontrol design. Every linear funtion dening V 
i 
is assoiated with an 
ation. The ation is seleted if its linear funtion (or Q-funtion) is maximal. 
As V 
i 
represents only the ith approximation of the optimal value funtion, the question 
arises how good the resulting ontroller really is. 
6 
The following theorem (Puterman, 1994; 
Williams & Baird, 1994; Littman, 1996) relates the auray of the (lookahead) ontroller 
and the Bellman error. 
Theorem 3 Let  = kV 
i 
  V 
i 1 
k be the magnitude of the Bellman error. Let V 
LA 
i 
be the 
expeted reward for the lookahead ontroller designed for V 
i 
. Then kV 
LA 
i 
  V 
 
k  
2 
1  
. 
The bound an be used to onstrut the value-iteration routine that yields a lookahead 
strategy with a minimum required preision. The result an be also extended to the k-
step lookahead design in a straightforward way; with k steps, the error bound beomes 
kV 
LA(k) 
i 
  V 
 
k  
2 
k 
(1 ) 
. 
2.5.2 Diret Design 
To extrat the ontrol ation via lookahead essentially requires omputing one full update. 
Obviously, this an lead to unwanted delays in reation times. In general, we an speed up 
the response by remembering and using additional information. In partiular, every linear 
funtion dening V 
i 
is assoiated with the hoie of ation (see Equation 7). The ation is a 
byprodut of methods for omputing linear funtions and no extra omputation is required 
to nd it. Then the ation orresponding to the best linear funtion an be seleted diretly 
for any belief state. The idea is illustrated in Figure 6. 
The bound on the auray of the diret ontroller for the innite-horizon ase an be 
one again derived in terms of the magnitude of the Bellman error. 
Theorem 4 Let  = kV 
i 
  V 
i 1 
k be the magnitude of the Bellman error. Let V 
DR 
i 
be an 
expeted reward for the diret ontroller designed for V 
i 
. Then kV 
DR 
i 
  V 
 
k  
2 
1  
. 
The diret ation hoie is losely related to the notion of ation-value funtion (or 
Q-funtion). Analogously to Equation 4, the ith Q-funtion satises 
V 
i 
(b) = max 
a2A 
Q 
i 
(b; a); 
6. Note that the ontrol ation extrated via lookahead from V 
i 
is optimal for (i + 1) steps-to-go and the 
nite-horizon model. The main dierene here is that V 
i 
is the optimal value funtion for i steps to go. 
43
Hauskreht 
a1 
a1 
a2 
a2 
a1 
a2 
o 2 
o1, 
o1 
o 2 
o1, 
o 2 
o1, 
o 2 
o1, 
o1 
o 2 
o2 
o2 
o1 a2 
Figure 7: A poliy graph (nite-state mahine) obtained after two value iteration steps. 
Nodes orrespond to linear funtions (or states of the nite-state mahine) and 
links to dependenies between linear funtions (transitions between states). Every 
linear funtion (node) is assoiated with an ation. To ensure that the poliy an 
be also applied to the innite-horizon problem, we add a yle to the last state 
(dashed line). 
Q 
i 
(b; a) = R(b; a) +  
X 
o2 
P (ojb; a)V 
i 1 
((b; a; o)): 
From this perspetive, the diret strategy selets the ation with the best (maximum) Q-
funtion for a given belief state. 
7 
2.5.3 Finite-State Mahine Design 
A more omplex renement of the above tehnique is to remember, for every linear funtion 
in V 
i 
, not only the ation hoie but also the hoie of a linear funtion for the previous 
step and to do this for all observations (see Equation 7). As the same idea an be applied 
reursively to the linear funtions for all previous steps, we an obtain a relatively omplex 
dependeny struture relating linear funtions in V 
i 
; V 
i 1 
;    V 
0 
, observations and ations 
that itself represents a ontrol strategy (Kaelbling et al., 1999). 
To see this, we model the struture in graphial terms (Figure 7). Here dierent nodes 
represent linear funtions, ations assoiated with nodes orrespond to optimizing ations, 
links emanating from nodes orrespond to dierent observations, and suessor nodes orre-
spond to linear funtions paired with observations. Suh graphs are also alled poliy graphs 
(Kaelbling et al., 1999; Littman, 1996; Cassandra, 1998). One interpretation of the depen-
deny struture is that it represents a olletion of nite-state mahines (FSMs) with many 
possible initial states that implement a POMDP ontroller: nodes orrespond to states of 
the ontroller, ations to ontrols (outputs), and links to transitions onditioned on inputs 
7. Williams and Baird (1994) also give results relating the auray of the diret Q-funtion ontroller to 
the Bellman error of Q-funtions. 
44
Value-Funtion Approximations for POMDPs 
(observations). The start state of the FSM ontroller is hosen greedily by seleting the 
linear funtion (ontroller state) optimizing the value of an initial belief state. 
The advantage of the nite-state mahine representation of the strategy is that for the 
rst i steps it works with observations diretly; belief-state updates are not needed. This 
ontrasts with the other two poliy models (lookahead and diret models), whih must keep 
trak of the urrent belief state and update it over time in order to extrat appropriate 
ontrol. The drawbak of the approah is that the FSM ontroller is limited to i steps 
that orrespond to the number of value iteration steps performed. However, in the innite-
horizon model the ontroller is expeted to run for an innite number of steps. One way 
to remedy this deieny is to extend the FSM struture and to reate yles that let us 
visit ontroller states repeatedly. For example, adding a yle transition to the end state of 
the FSM ontroller in Figure 7 (dashed line) ensures that the ontroller is also appliable 
to the innite-horizon problem. 
2.6 Poliy Iteration 
An alternative method for nding the solution for the disounted innite-horizon problem 
is poliy iteration (Howard, 1960; Sondik, 1978). Poliy iteration searhes the poliy spae 
and gradually improves the urrent ontrol poliy for one or more belief states. The method 
onsists of two steps performed iteratively: 
 poliy evaluation: omputes expeted value for the urrent poliy; 
 poliy improvement: improves the urrent poliy. 
As we saw in Setion 2.5, there are many ways to represent a ontrol poliy for a 
POMDP. Here we restrit attention to a nite-state mahine model in whih observations 
orrespond to inputs and ations to outputs (Platzman, 1980; Hansen, 1998b; Kaelbling 
et al., 1999). 
8 
2.6.1 Finite-State Mahine Controller 
A nite-state mahine (FSM) ontroller C = (M;; A; ; ;  ) for a POMDP is desribed 
by a set of memory states M of the ontroller, a set of observations (inputs) , a set of 
ations (outputs) A, a transition funtion  : M  ! M mapping states of the FSM to 
next memory states given the observation, and an output funtion  : M ! A mapping 
memory states to ations. A funtion  : I 
0 
! M selets the initial memory state given 
the initial information state. The initial information state orresponds either to a prior or 
a posterior belief state at time t 
0 
depending on the availability of an initial observation. 
2.6.2 Poliy Evaluation 
The rst step of the poliy iteration is poliy evaluation. The most important property 
of the FSM model is that the value funtion for a spei FSM strategy an be omputed 
eÆiently in the number of ontroller states M . The key to eÆient omputability is the 
8. A poliy-iteration algorithm in whih poliies are dened over the regions of the belief spae was desribed 
rst by Sondik (1978). 
45
Hauskreht 
x 
x 
x 
x 
o 
o 
o 
o 
o 
oo a a 
a 
a 
1 
2 
2 
12 
1 
2 
2 
1 
1 
1 
o2 
1 
4 
2 
3 
Figure 8: An example of a four-state FSM poliy. Nodes represent states, links transi-
tions between states (onditioned on observations). Every memory state has an 
assoiated ontrol ation (output). 
fat that the value funtion for exeuting an FSM strategy from some memory state x is 
linear (Platzman, 1980). 
9 
Theorem 5 Let C be a nite-state mahine ontroller with a set of memory states M . 
The value funtion for applying C from a memory state x 2 M , V 
C 
(x; b), is linear. Value 
funtions for all x 2 M an be found by solving a system of linear equations with jSjjM j 
variables. 
We illustrate the main idea by an example. Assume an FSM ontroller with four memory 
states fx 
1 
; x 
2 
; x 
3 
; x 
4 
g, as in Figure 8, and a stohasti proess with two hidden states S = 
fs 
1 
; s 
2 
g. The value of the poliy for an augmented state spae S M satises a system of 
linear equations 
V (x 
1 
; s 
1 
) = (s 
1 
; (x 
1 
)) +  
X 
o2 
X 
s2S 
P (o; sjs 
1 
; (x 
1 
))V ((x 
1 
; o); s) 
V (x 
1 
; s 
2 
) = (s 
2 
; (x 
1 
)) +  
X 
o2 
X 
s2S 
P (o; sjs 
2 
; (x 
1 
))V ((x 
1 
; o); s) 
V (x 
2 
; s 
1 
) = (s 
1 
; (x 
2 
)) +  
X 
o2 
X 
s2S 
P (o; sjs 
1 
; (x 
2 
))V ((x 
2 
; o); s) 
   
V (x 
4 
; s 
2 
) = (s 
2 
; (x 
4 
)) +  
X 
o2 
X 
s2S 
P (o; sjs 
2 
; (x 
4 
))V ((x 
4 
; o); s); 
where (x) is the ation exeuted in x and (x; o) is the state to whih one transits after 
seeing an input (observation) o. Assuming we start the poliy from the memory state x 
1 
, 
the value of the poliy is: 
V 
C 
(x 
1 
; b) = 
X 
s2S 
V (x 
1 
; s)b(s): 
9. The idea of linearity and eÆient omputability of the value funtions for a xed FSM-based strategy 
has been addressed reently in dierent ontexts by a number of researhers (Littman, 1996; Cassandra, 
1998; Hauskreht, 1997; Hansen, 1998b; Kaelbling et al., 1999). However, the origins of the idea an be 
traed to the earlier work by Platzman (1980). 
46
Value-Funtion Approximations for POMDPs 
Thus the value funtion is linear and an be omputed eÆiently by solving a system of 
linear equations. 
Sine in general the FSM ontroller an start from any memory state, we an always 
hoose the initial memory state greedily, maximizing the expeted value of the result. In 
suh a ase the optimal hoie funtion  is dened as: 
 (b) = argmax 
x2M 
V 
C 
(x; b); 
and the value for the FSM poliy C and belief state b is: 
V 
C 
(b) = max 
x2M 
V 
C 
(x; b) = V 
C 
( (b); b): 
Note that the resulting value funtion for the strategy C is pieewise linear and onvex and 
represents expeted rewards for following C. Sine no strategy an perform better that the 
optimal strategy, V 
C 
 V 
 
must hold. 
2.6.3 Poliy Improvement 
The poliy-iteration method, searhing the spae of ontrollers, starts from an arbitrary ini-
tial poliy and improves it gradually by rening its nite-state mahine (FSM) desription. 
In partiular, one keeps modifying the struture of the ontroller by adding or removing on-
troller states (memory) and transitions. Let C and C 
0 
be an old and a new FSM ontroller. 
In the improvement step we must satisfy 
V 
C 
0 
(b)  V 
C 
(b) for all b 2 I; 
9b 2 I suh that V 
C 
0 
(b) > V 
C 
(b): 
To guarantee the improvement, Hansen (1998a, 1998b) proposed a poliy-iteration algo-
rithm that relies on exat value funtion updates to obtain a new improved poliy stru-
ture. 
10 
The basi idea of the improvement is based on the observation that one an swith 
bak and forth between the FSM poliy desription and the pieewise-linear and onvex 
representation of a value funtion. In partiular: 
 the value funtion for an FSM poliy is pieewise-linear and onvex and every linear 
funtion desribing it orresponds to a memory state of a ontroller; 
 individual linear funtions omprising the new value funtion after an update an be 
viewed as new memory states of an FSM poliy, as desribed in Setion 2.5.3. 
This allows us to improve the poliy by adding new memory states orresponding to linear 
funtions of the new value funtion obtained after the exat update. The tehnique an be 
rened by removing some of the linear funtions (memory states) whenever they are fully 
dominated by one of the other linear funtions. 
10. A poliy-iteration algorithm that exploits exat value funtion updates but works with poliies dened 
over the belief spae was used earlier by Sondik (1978). 
47
Hauskreht 
a 
o 
o 
b 
1 
a 2 
Figure 9: A two-step deision tree. Retangles orrespond to the deision nodes (moves 
of the deision-maker) and irles to hane nodes (moves of the environment). 
Blak retangles represent leaves of the tree. The reward for a spei path 
is assoiated with every leaf of the tree. Deision nodes are assoiated with 
information states obtained by following ation and observation hoies along the 
path from the root of the tree. For example, b 
1;1 
is a belief state obtained by 
performing ation a 
1 
from the initial belief state b and observing observation o 
1 
. 
2.7 Forward (Deision Tree) Methods 
The methods disussed so far assume no prior knowledge of the initial belief state and treat 
all belief states as equally likely. However, if the initial state is known and xed, methods 
an often be modied to take advantage of this fat. For example, for the nite-horizon 
problem, only a nite number of belief states an be reahed from a given initial state. In 
this ase it is very often easier to enumerate all possible histories (sequenes of ations and 
observations) and represent the problem using stohasti deision trees (Raia, 1970). An 
example of a two-step deision tree is shown in Figure 9. 
The algorithm for solving the stohasti deision tree basially mimis value-funtion 
updates, but is restrited only to situations that an be reahed from the initial belief state. 
The key diÆulty here is that the number of all possible trajetories grows exponentially 
with the horizon of interest. 
2.7.1 Combining Dynami-Programming and Deision-Tree Tehniques 
To solve a POMDP for a xed initial belief state, we an apply two strategies: one on-
struts the deision tree rst and then solves it, the other solves the problem in a bakward 
fashion via dynami programming. Unfortunately, both these tehniques are ineÆient, one 
suering from exponential growth in the deision tree size, the other from super-exponential 
growth in the value funtion omplexity. However, the two tehniques an be ombined in 
48
Value-Funtion Approximations for POMDPs 
a way that at least partially eliminates their disadvantages. The idea is based on the fat 
that the two tehniques work on the solution from two dierent sides (one forward and the 
other bakward) and the omplexity for eah of them worsens gradually. Then the solution 
is to ompute the omplete kth value funtion using dynami programming (value iteration) 
and over the remaining steps by forward deision-tree expansion. 
Various modiations of the above idea are possible. For example, one an often replae 
exat dynami programming with two more eÆient approximations providing upper and 
lower bounds of the value funtion. Then the deision tree must be expanded only when 
the bounds are not suÆient to determine the optimal ation hoie. A number of searh 
tehniques developed in the AI literature (Korf, 1985) ombined with branh-and-bound 
pruning (Satia & Lave, 1973) an be applied to this type of problem. Several researhers 
have experimented with them to solve POMDPs (Washington, 1996; Hauskreht, 1997; 
Hansen, 1998b). Other methods appliable to this problem are based on Monte-Carlo 
sampling (Kearns, Mansour, & Ng, 1999; MAllester & Singh, 1999) and real-time dynami 
programming (Barto, Bradtke, & Singh, 1995; Dearden & Boutilier, 1997; Bonet & Gener, 
1998). 
2.7.2 Classial Planning Framework 
POMDP problems with xed initial belief states and their solutions are losely related to 
work in lassial planning and its extensions to handle stohasti and partially observable 
domains, partiularly the work on BURIDAN and C-BURIDAN planners (Kushmerik, 
Hanks, & Weld, 1995; Draper, Hanks, & Weld, 1994). The objetive of these planners is 
to maximize the probability of reahing some goal state. However, this task is similar to 
the disounted reward task in terms of omplexity, sine a disounted reward model an 
be onverted into a goal-ahievement model by introduing an absorbing state (Condon, 
1992). 
3. Heuristi Approximations 
The key obstale to wider appliation of the POMDP framework is the omputational 
omplexity of POMDP problems. In partiular, nding the optimal solution for the nite-
horizon ase is PSPACE-hard (Papadimitriou & Tsitsiklis, 1987) and the disounted innite-
horizon ase may not even be omputable (Madani et al., 1999). One approah to suh 
problems is to approximate the solution to some -preision. Unfortunately, even this 
remains intratable and in general POMDPs annot be approximated eÆiently (Burago, 
Rougemont, & Slissenko, 1996; Lusena, Goldsmith, & Mundhenk, 1998; Madani et al., 
1999). This is also the reason why only very simple problems an be solved optimally or 
near-optimally in pratie. 
To alleviate the omplexity problem, researh in the POMDP area has foused on various 
heuristi methods (or approximations without the error parameter) that are more eÆient. 
11 
Heuristi methods are also our fous here. Thus, when referring to approximations, we mean 
heuristis, unless speially stated otherwise. 
11. The quality of a heuristi approximation an be tested using the Bellman error, whih requires one exat 
update step. However, heuristi methods per se do not ontain a preision parameter. 
49
Hauskreht 
The many approximation methods and their ombinations an be divided into two often 
very losely related lasses: value-funtion approximations and poliy approximations. 
3.1 Value-Funtion Approximations 
The main idea of the value-funtion approximation approah is to approximate the optimal 
value funtion V : I ! IR with a funtion 
b 
V : I ! IR dened over the same information 
spae. Typially, the new funtion is of lower omplexity (reall that the optimal or near-
optimal value funtion may onsist of a large set of linear funtions) and is easier to ompute 
than the exat solution. Approximations an be often formulated as dynami programming 
problems and an be expressed in terms of approximate value-funtion updates 
b 
H. Thus, 
to understand the dierenes and advantages of various approximations and exat methods, 
it is often suÆient to analyze and ompare their update rules. 
3.1.1 Value-Funtion Bounds 
Although heuristi approximations have no guaranteed preision, in many ases we are 
able to say whether they overestimate or underestimate the optimal value funtion. The 
information on bounds an be used in multiple ways. For example, upper- and lower-
bounds an help in narrowing the range of the optimal value funtion, elimination of some 
of the suboptimal ations and subsequent speed-ups of exat methods. Alternatively, one 
an use knowledge of both value-funtion bounds to determine the auray of a ontroller 
generated based on one of the bounds (see Setion 3.1.3). Also, in some instanes, a lower 
bound alone is suÆient to guarantee the ontrol hoie that always ahieves an expeted 
reward at least as high as the one given by that bound (Setion 4.7.2). 
The bound property of dierent methods an be determined by examining the updates 
and their bound relations. 
Denition 5 (Upper bound). Let H be the exat value-funtion mapping and 
b 
H its ap-
proximation. We say that 
b 
H upper-bounds H for some V when ( 
b 
HV )(b)  (HV )(b) holds 
for every b 2 I. 
An analogous denition an be onstruted for the lower bound. 
3.1.2 Convergene of Approximate Value Iteration 
Let 
b 
H be a value-funtion mapping representing an approximate update. Then the ap-
proximate value iteration omputes the ith value funtion as 
b 
V 
i 
= 
b 
H 
b 
V 
i 1 
. The xed-point 
solution 
 
V 
 
= 
b 
H 
b 
V 
 
or its lose approximation would then represent the intended output of 
the approximation routine. The main problem with the iteration method is that in general 
it an onverge to unique or multiple solutions, diverge, or osillate, depending on 
b 
H and 
the initial funtion 
b 
V 
0 
. Therefore, unique onvergene annot be guaranteed for an arbitrary 
mapping 
b 
H and the onvergene of a spei approximation method must be proved. 
Denition 6 (Convergene of 
b 
H). The value iteration with 
b 
H onverges for a value fun-
tion V 
0 
when lim 
n!1 
( 
b 
H 
n 
V 
0 
) exists. 
50
Value-Funtion Approximations for POMDPs 
Denition 7 (Unique onvergene of 
b 
H). The value iteration onverges uniquely for V 
when for every V 2 V, lim 
n!1 
( 
b 
H 
n 
V ) exists and for all pairs V;U 2 V, lim 
n!1 
( 
b 
H 
n 
V ) = 
lim 
n!1 
( 
b 
H 
n 
U). 
A suÆient ondition for the unique onvergene is to show that 
b 
H be a ontration. The 
ontration and the bound properties of 
b 
H an be ombined, under additional onditions, to 
show the onvergene of the iterative approximation method to the bound. To address this 
issue we present a theorem omparing xed-point solutions of two value-funtion mappings. 
Theorem 6 Let H 
1 
and H 
2 
be two value-funtion mappings dened on V 
1 
and V 
2 
suh that 
1. H 
1 
, H 
2 
are ontrations with xed points V 
 
1 
, V 
 
2 
; 
2. V 
 
1 
2 V 
2 
and H 
2 
V 
 
1 
 H 
1 
V 
 
1 
= V 
 
1 
; 
3. H 
2 
is an isotone mapping. 
Then V 
 
2 
 V 
 
1 
holds. 
Note that this theorem does not require that V 
1 
and V 
2 
over the same spae of value 
funtions. For example, V 
2 
an over all possible value funtions of a belief-state MDP, 
while V 
1 
an be restrited to a spae of pieewise linear and onvex value funtions. This 
gives us some exibility in the design of iterative approximation algorithms for omputing 
value-funtion bounds. An analogous theorem also holds for the lower bound. 
3.1.3 Control 
One the approximation of the value-funtion is available, it an be used to generate a 
ontrol strategy. In general, ontrol solutions orrespond to options presented in Setion 
2.5 and inlude lookahead, diret (Q-funtion) and nite-state mahine designs. 
A drawbak of ontrol strategies based on heuristi approximations is that they have 
no preision guarantee. One way to nd the auray of suh strategies is to do one exat 
update of the value funtion approximation and adopt the result of Theorems 1 and 3 for 
the Bellman error. An alternative solution to this problem is to bound the auray of 
suh ontrollers using the upper- and the lower-bound approximations of the optimal value 
funtion. To illustrate this approah, we present and prove (in the Appendix) the following 
theorem that relates the quality of bounds to the quality of a lookahead ontroller. 
Theorem 7 Let 
b 
V 
U 
and 
b 
V 
L 
be upper and lower bounds of the optimal value funtion for 
the disounted innite-horizon problem. Let  = sup 
b 
j 
b 
V 
U 
(b)   
b 
V 
L 
(b)j = k 
b 
V 
U 
  
b 
V 
L 
k be 
the maximum bound dierene. Then the expeted reward for a lookahead ontroller 
b 
V 
LA 
, 
onstruted for either 
b 
V 
U 
or 
b 
V 
L 
, satises k 
b 
V 
LA 
  V 
 
k  
(2 ) 
(1 ) 
. 
3.2 Poliy Approximation 
An alternative to value-funtion approximation is poliy approximation. As shown earlier, 
a strategy (ontroller) for a POMDP an be represented using a nite-state mahine (FSM) 
model. The poliy iteration searhes the spae of all possible poliies (FSMs) for the opti-
mal or near-optimal solution. This spae is usually enormous, whih is the bottlenek of the 
51
Hauskreht 
method. Thus, instead of searhing the omplete poliy spae, we an restrit our attention 
only to its subspae that we believe to ontain the optimal solution or a good approxima-
tion. Memoryless poliies (Platzman, 1977; White & Sherer, 1994; Littman, 1994; Singh, 
Jaakkola, & Jordan, 1994), poliies based on trunated histories (Platzman, 1977; White & 
Sherer, 1994; MCallum, 1995), or nite-state ontrollers with a xed number of memory 
states (Platzman, 1980; Hauskreht, 1997; Hansen, 1998a, 1998b) are all examples of a 
poliy-spae restrition. In the following we onsider only the nite-state mahine model 
(see Setion 2.6.1), whih is quite general; other models an be viewed as its speial ases. 
States of an FSM poliy model represent the memory of the ontroller and, in general, 
summarize information about past ativities and observations. Thus, they are best viewed 
as approximations of the information states, or as feature states. The transition model of 
the ontroller () then approximates the update funtion of the information-state MDP 
() and the output funtion of an FSM () approximates the ontrol funtion () mapping 
information states to ations. The important property of the model, as shown Setion 
2.6.2, is that the value funtion for a xed ontroller and xed initial memory state an be 
obtained eÆiently by solving a system of linear equations (Platzman, 1980). 
To apply the poliy approximation approah we rst need to deide (1) how to restrit 
a spae of poliies and (2) how to judge the poliy quality. 
A restrition frequently used is to onsider only ontrollers with a xed number of 
states, say k. Other strutural restritions further narrowing the spae of poliies an 
restrit either the output funtion (hoie of ations at dierent ontroller states), or the 
transitions between the urrent and next states. In general, any heuristi or domain-related 
insight may help in seleting the right biases. 
Two dierent poliies an yield value funtions that are better in dierent regions of 
the belief spae. Thus, in order to deide whih poliy is the best, we need to dene the 
importane of dierent regions and their ombinations. There are multiple solutions to this. 
For example, Platzman (1980) onsiders the worst-ase measure and optimizes the worst 
(minimal) value for all initial belief states. Let C be a spae of FSM ontrollers satisfying 
given restritions. Then the quality of a poliy under the worst ase measure is: 
max 
C2C 
min 
b2I 
max 
x2M 
C 
V 
C 
(x; b): 
Another option is to onsider a distribution over all initial belief states and maximize the 
expetation of their value funtion values. However, the most ommon objetive is to hoose 
the poliy that leads to the best value for a single initial belief state b 
0 
: 
max 
C2C 
max 
x2M 
C 
V 
C 
(x; b 
0 
): 
Finding the optimal poliy for this ase redues to a ombinatorial optimization problem. 
Unfortunately, for all but trivial ases, even this problem is omputationally intratable. 
For example, the problem of nding the optimal poliy for a memoryless ase (only ur-
rent observations are onsidered) is NP-hard (Littman, 1994). Thus, various heuristis are 
typially applied to alleviate this diÆulty (Littman, 1994). 
52
Value-Funtion Approximations for POMDPs 
Value−function approximations 
Fully observable MDP    approximations 
Fast informed bound    approximations 
Unobservable MDP   approximations 
Section 4.1 
Section 4.2 
Section 4.3 
Section 4.4 
Section 4.7 
 Fixed strategy approximations 
Curve−fitting approximations 
Section 4.6 
Section 4.5 
 Grid−based value interpolation−  extrapolation methods 
Grid−based linear function methods 
Figure 10: Value-funtion approximation methods. 
3.2.1 Randomized Poliies 
By restriting the spae of poliies we simplify the poliy optimization problem. On the 
other hand, we simultaneously give up an opportunity to nd the best optimal poliy, repla-
ing it with the best restrited poliy. Up to this point, we have onsidered only deterministi 
poliies with a xed number of internal ontroller states, that is, poliies with deterministi 
output and transition funtions. However, nding the best deterministi poliy is not al-
ways the best option: randomized poliies, with randomized output and transition funtions, 
usually lead to the far better performane. The appliation of randomized (or stohasti) 
poliies to POMDPs was introdued by Platzman (1980). Essentially, any deterministi 
poliy an be represented as a randomized poliy with a single ation and transition, so 
that the best randomized poliy is no worse than the best deterministi poliy. The dier-
ene in ontrol performane of two poliies shows up most often in ases when the number 
of states of the ontroller is relatively small ompared to that in the optimal strategy. 
The advantage of stohasti poliies is that their spae is larger and parameters of 
the poliy are ontinuous. Therefore the problem of nding the optimal stohasti poliy 
beomes a non-linear optimization problem and a variety of optimization methods an be 
applied to solve it. An example is the gradient-based approah (see Meuleau et al., 1999). 
4. Value-Funtion Approximation Methods 
In this setion we disuss in more depth value-funtion approximation methods. We fo-
us on approximations with belief information spae. 
12 
We survey known tehniques, but 
also inlude a number of new methods and modiations of existing methods. Figure 10 
summarizes the methods overed. We desribe the methods by means of update rules they 
12. Alternative value-funtion approximations may work with omplete histories of past ations and obser-
vations. Approximation methods used by White and Sherer (1994) are an example. 
53
Hauskreht 
Moves Sensors 
0 1 2 3 4 
5 6 7 8 9 
10 11 12 13 14 
15 16 17 18 19 
Figure 11: Test example. The maze navigation problem: Maze20. 
implement, whih simplies their analysis and theoretial omparison. We fous on the fol-
lowing properties: the omplexity of the dynami-programming (value-iteration) updates; 
the omplexity of value funtions eah method uses; the ability of methods to bound the 
exat update; the onvergene of value iteration with approximate update rules; and the 
ontrol performane of related ontrollers. The results of the theoretial analysis are illus-
trated empirially on a problem from the agent-navigation domain. In addition, we use the 
agent navigation problem to illustrate and give some intuitions on other harateristis of 
methods with no theoretial underpinning. Thus, these results should not be generalized 
to other problems or used to rank dierent methods. 
Agent-Navigation Problem 
Maze20 is a maze-navigation problem with 20 states, six ations and eight observations. 
The maze (Figure 11) onsists of 20 partially onneted rooms (states) in whih a robot 
operates and ollets rewards. The robot an move in four diretions (north, south, east 
and west) and an hek for the presene of walls using its sensors. But, neither \move" 
ations nor sensor inputs are perfet, so that the robot an end up moving in unintended 
diretions. The robot moves in an unintended diretion with probability of 0.3 (0.15 for 
eah of the neighboring diretions). A move into the wall keeps the robot in the same 
position. Investigative ations help the robot to navigate by ativating sensor inputs. Two 
suh investigative ations allow the robot to hek inputs (presene of a wall) in the north-
south and east-west diretions. Sensor auray in deteting walls is 0.75 for a two-wall 
ase (e.g. both north and south wall), 0.8 for a one-wall ase (north or south) and 0.89 for 
a no-wall ase, with smaller probabilities for wrong pereptions. 
The ontrol objetive is to maximize the expeted disounted rewards with a disount 
fator of 0.9. A small reward is given for every ation not leading to bumping into the wall 
(4 points for a move and 2 points for an investigative ation), and one large reward (150 
points) is given for ahieving the speial target room (indiated by the irle in the gure) 
and reognizing it by performing one of the move ations. After doing that and olleting 
the reward, the robot is plaed at random in a new start position. 
Although the Maze20 problem is of only moderate omplexity with regard to the size 
of state, ation and observation spaes, its exat solution is beyond the reah of urrent 
exat methods. The exat methods tried on the problem inlude the Witness algorithm 
(Kaelbling et al., 1999), the inremental pruning algorithm (Cassandra et al., 1997) 
13 
and 
13. Many thanks to Anthony Cassandra for running these algorithms. 
54
Value-Funtion Approximations for POMDPs 
MDPV 
VPOMDP* 
1b(s  ) 
* MDPV       (s  )1 
0 1 
* MDP 2 V       (s  ) 
(a) 1b(s  ) 
* 2 1Q       (s  ,a  )MDP 
* 2 2Q       (s  ,a  )MDP 
VQMDP 
VPOMDP* 
* 21Q       (s  ,a  )MDP 
* 1 1Q       (s  ,a  )MDP 
0 1 
(b) 
Figure 12: Approximations based on the fully observable version of a two state POMDP 
(with states s 
1 
; s 
2 
): (a) the MDP approximation; (b) the QMDP approximation. 
Values at extreme points of the belief spae are solutions of the fully observable 
MDP. 
poliy iteration with an FSM model (Hansen, 1998b). The main obstale preventing these 
algorithms from obtaining the optimal or lose-to-optimal solution was the omplexity of 
the value funtion (the number of linear funtions needed to desribe it) and subsequent 
running times and memory problems. 
4.1 Approximations with Fully Observable MDP 
Perhaps the simplest way to approximate the value funtion for a POMDP is to assume 
that states of the proess are fully observable (Astrom, 1965; Lovejoy, 1993). In that ase 
the optimal value funtion V 
 
for a POMDP an be approximated as: 
b 
V (b) = 
X 
s2S 
b(s)V 
 
MDP 
(s); (8) 
where V 
 
MDP 
(s) is the optimal value funtion for state s for the fully observable version of 
the proess. We refer to this approximation as to the MDP approximation. The idea of 
the approximation is illustrated in Figure 12a. The resulting value funtion is linear and 
is fully dened by values at extreme points of the belief simplex. These orrespond to the 
optimal values for the fully observable ase. The main advantage of the approximation 
is that the fully observable MDP (FOMDP) an be solved eÆiently for both the nite-
horizon problem and disounted innite-horizon problems. 
14 
The update step for the (fully 
observable) MDP is: 
V 
MDP 
i+1 
(s) = max 
a 
8 
< 
: 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a)V 
MDP 
i 
(s 
0 
) 
9 
= 
; 
: 
14. The solution for the nite-state fully observable MDP and disounted innite-horizon riterion an be 
found eÆiently by formulating an equivalent linear programming task (Bertsekas, 1995) 
55
Hauskreht 
4.1.1 MDP Approximation 
The MDP-approximation approah (Equation 8) an be also desribed in terms of value-
funtion updates for the belief-spae MDP. Although this step is stritly speaking redundant 
here, it simplies the analysis and omparison of this approah to other approximations. 
Let 
b 
V 
i 
be a linear value funtion desribed by a vetor  
MDP 
i 
orresponding to values 
of V 
MDP 
i 
(s 
0 
) for all states s 
0 
2 S. Then the (i+ 1)th value funtion 
b 
V 
i+1 
is 
b 
V 
i+1 
(b) = 
X 
s2S 
b(s)max 
a2A 
2 
4 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a) 
MDP 
i 
(s 
0 
) 
3 
5 
= (H 
MDP 
b 
V 
i 
)(b): 
b 
V 
i+1 
is desribed by a linear funtion with omponents 
 
MDP 
i+1 
(s) = V 
MDP 
i+1 
(s) = max 
a 
( 
(s; a) +  
X 
s2S 
P (s 
0 
js; a) 
MDP 
i 
(s 
0 
) 
) 
: 
The MDP-based rule H 
MDP 
an be also rewritten in a more general form that starts from 
an arbitrary pieewise linear and onvex value funtion V 
i 
, represented by a set of linear 
funtions   
i 
: 
b 
V 
i+1 
(b) = 
X 
s2S 
b(s)max 
a2A 
8 
< 
: 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a) max 
 
i 
2  
i 
 
i 
(s 
0 
) 
9 
= 
; 
: 
The appliation of the H 
MDP 
mapping always leads to a linear value funtion. The 
update is easy to ompute and takes O(jAjjSj 
2 
+ j  
i 
jjSj) time. This redues to O(jAjjSj 
2 
) 
time when only MDP-based updates are strung together. As remarked earlier, the optimal 
solution for the innite-horizon, disounted problem an be solved eÆiently via linear 
programming. 
The update for the MDP approximation upper-bounds the exat update, that is, H 
b 
V 
i 
 
H 
MDP 
b 
V 
i 
. We show this property later in Theorem 9, whih overs more ases. The intuition 
is that we annot get a better solution with less information, and thus the fully observable 
MDP must upper-bound the partially observable ase. 
4.1.2 Approximation with Q-Funtions (QMDP) 
A variant of the approximation based on the fully observable MDP uses Q-funtions (Littman, 
Cassandra, & Kaelbling, 1995): 
b 
V (b) = max 
a2A 
X 
s2S 
b(s)Q 
 
MDP 
(s; a); 
where 
Q 
 
MDP 
(s; a) = (s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a)V 
 
MDP 
(s 
0 
) 
is the optimal ation-value funtion (Q-funtion) for the fully observable MDP. The QMDP 
approximation 
b 
V is pieewise linear and onvex with jAj linear funtions, eah orresponding 
56
Value-Funtion Approximations for POMDPs 
to one ation (Figure 12b). The QMDP update rule (for the belief state MDP) for 
b 
V 
i 
with 
linear funtions  
k 
i 
2   
i 
is: 
b 
V 
i+1 
(b) = max 
a2A 
X 
s2S 
b(s) 
2 
4 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a) max 
 
i 
2  
i 
 
i 
(s 
0 
) 
3 
5 
= (H 
QMDP 
b 
V 
i 
)(b): 
H 
QMDP 
generates a value funtion with jAj linear funtions. The time omplexity of the 
update is the same as for the MDP-approximation ase { O(jAjjSj 
2 
+ j  
i 
jjSj), whih redues 
to O(jAjjSj 
2 
) time when only QMDP updates are used. H 
QMDP 
is a ontration mapping 
and its xed-point solution an be found by solving the orresponding fully observable MDP. 
The QMDP update upper-bounds the exat update. The bound is tighter than the 
MDP update; that is, H 
b 
V 
i 
 H 
QMDP 
b 
V 
i 
 H 
MDP 
b 
V 
i 
, as we prove later in Theorem 9. The 
same inequalities hold for both xed-point solutions (through Theorem 6). 
To illustrate the dierene in the quality of bounds for the MDP approximation and 
the QMDP method, we use our Maze20 navigation problem. To measure the quality of a 
bound we use the mean of value-funtion values. Sine all belief states are equally important 
we assume that they are uniformly distributed. We approximate this measure using the 
average of values for a xed set of N = 2000 belief points. The points in the set were 
seleted uniformly at random at the beginning. One the set was hosen, it was xed 
and remained the same for all tests (here and later). Figure 13 shows the results of the 
experiment; we inlude also results for the fast informed bound method that is presented in 
the next setion. 
15 
Figure 13 also shows the running times of the methods. The methods 
were implemented in Common Lisp and run on Sun Ultra 1 workstation. 
4.1.3 Control 
The MDP and the QMDP value-funtion approximations an be used to onstrut on-
trollers based on one-step lookahead. In addition, the QMDP approximation is also suitable 
for the diret ontrol strategy, whih selets an ation orresponding to the best (highest 
value) Q-funtion. Thus, the method is a speial ase of the Q-funtion approah disussed 
in Setion 3.1.3. 
16 
The advantage of the diret QMDP method is that it is faster than both 
lookahead designs. On other the hand, lookahead tends to improve the ontrol performane. 
This is shown in Figure 14, whih ompares the ontrol performane of dierent ontrollers 
on the Maze20 problem. 
The quality of a poliy 
b 
, with no preferene towards a partiular initial belief state, an 
be measured by the mean of value-funtion values for 
b 
 and uniformly distributed initial 
belief states. We approximate this measure using the average of disounted rewards for 
15. The ondene interval limits for probability level 0.95 range in (0:45; 0:62) from their respetive 
average sores and this holds for all bound experiments in the paper. As these are relatively small we 
do not inlude them in our graphs. 
16. As pointed out by Littman et al. (1995), in some instanes, the diret QMDP ontroller never selets 
investigative ations, that is, ations that try to gain more information about the underlying proess 
state. Note, however, that this observation is not true in general and the QMDP-based ontroller with 
diret ation seletion may selet investigative ations, even though in the fully observable version of the 
problem investigative ations are never hosen. 
57
Hauskreht 
bound quality 
fast informed 
bound 
QMDP 
approximation 
MDP 
approximation 
40 
60 
80 
100 
120 
140 
s c o 
re running times 
fast informed 
bound 
MDP 
approximation QMDP 
approximation 
0 
10 
20 
30 
40 
50 
60 
ti m 
e  [ 
s e 
c ] 
Figure 13: Comparison of the MDP, QMDP and fast informed bound approximations: 
bound quality (left); running times (right). The bound-quality sore is the 
average value of the approximation for the set of 2000 belief points (hosen uni-
formly at random). As the methods upper-bound the optimal value funtion, we 
ip the bound-quality graph so that longer bars indiate better approximations. 
2000 ontrol trajetories obtained for the xed set of N = 2000 initial belief states (seleted 
uniformly at random at the beginning). The trajetories were obtained through simulation 
and were 60 steps long. 
17 
To validate the omparison along the averaged performane sores, we must show that 
these sores are not the result of randomness and that methods are indeed statistially 
signiantly dierent. To do this we rely on pairwise signiane tests. 
18 
To summarize the 
obtained results, the sore dierenes of 1.54, 2.09 and 2.86 between any two methods (here 
and also later in the paper) are suÆient to rejet the method with a lower sore being 
the better performer at signiane levels 0.05, 0.01 and 0.001 respetively. 
19 
Error-bars in 
Figure 14 reet the ritial sore dierene for the signiane level 0.05. 
Figure 14 also shows the average reation times for dierent ontrollers during these 
experiments. The results show the lear dominane of the diret QMDP ontroller, whih 
need not do a lookahead in order to extrat an ation, ompared to the other two MDP-
based ontrollers. 
4.2 Fast Informed Bound Method 
Both the MDP and the QMDP approahes ignore partial observability and use the fully 
observable MDP as a surrogate. To improve these approximations and aount (at least to 
17. The length of the trajetories (60 steps) for the Maze20 problem was hosen to ensure that our estimates 
of (disounted) umulative rewards are not far from the atual rewards for an innite number of steps. 
18. An alternative way to ompare two methods is to ompute ondene limits for their sores and inspet 
their overlaps. However, in this ase, the ability to distinguish two methods an be redued due to 
utuations of sores for dierent initializations. For Maze20, ondene interval limits for probability 
level 0.95 range in (1:8; 2:3) from their respetive average sores. This overs all ontrol experiments 
here and later. Pairwise tests eliminate the dependeny by examining the dierenes of individual values 
and thus improve the disriminative power. 
19. The ritial sore dierenes listed over the worst ase ombination. Thus, there may be some pairs for 
whih the smaller dierene would suÆe. 
58
Value-Funtion Approximations for POMDPs 
control performance 
direct 
fast informed 
bound 
lookahead 
direct 
MDP 
approximation 
QMDP 
approximation 
lookahead 
lookahead 
20 
30 
40 
50 
60 
70 
s c 
o re 
reaction times 
direct  direct 
lookahead 
lookahead 
MDP 
approximation 
QMDP 
approximation 
lookahead 
fast informed 
 bound 
0 
0.005 
0.01 
0.015 
0.02 
0.025 
ti m 
e  [ 
s e 
c ] 
Figure 14: Comparison of ontrol performane of the MDP, QMDP and fast informed bound 
methods: quality of ontrol (left); reation times (right). The quality-of-ontrol 
sore is the average of disounted rewards for 2000 ontrol trajetories obtained 
for the xed set of 2000 initial belief states (seleted uniformly at random). 
Error-bars show the ritial sore dierene value (1.54) at whih any two meth-
ods beome statistially dierent at signiane level 0.05. 
some degree) for partial observability we propose a new method { the fast informed bound 
method. Let 
b 
V 
i 
be a pieewise linear and onvex value funtion represented by a set of linear 
funtions   
i 
. The new update is dened as 
b 
V 
i+1 
(b) = max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
X 
s2S 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= max 
a2A 
8 
< 
: 
X 
s2S 
b(s) 
2 
4 
(s; a) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
) 
3 
5 
9 
= 
; 
= (H 
FIB 
b 
V 
i 
)(b): 
The fast informed bound update an be obtained from the exat update by the following 
derivation: 
(H 
b 
V 
i 
)(b) = max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
X 
s2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
 max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
X 
s2S 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= max 
a2A 
X 
s2S 
b(s) 
2 
4 
(s; a) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
) 
3 
5 
= max 
a2A 
X 
s2S 
b(s) 
a 
i+1 
(s) 
= (H 
FIB 
b 
V 
i 
)(b): 
The value funtion 
b 
V 
i+1 
= H 
FIB 
b 
V 
i 
one obtains after an update is pieewise linear and 
onvex and onsists of at most jAj dierent linear funtions, eah orresponding to one 
59
Hauskreht 
ation 
 
a 
i+1 
(s) = (s; a) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
): 
TheH 
FIB 
update is eÆient and an be omputed in O(jAjjSj 
2 
jjj  
i 
j) time. As the method 
always outputs jAj linear funtions, the omputation an be done in O(jAj 
2 
jSj 
2 
jj) time, 
when many H 
FIB 
updates are strung together. This is a signiant omplexity redution 
ompared to the exat approah: the latter an lead to a funtion onsisting of jAjj  
i 
j 
jj 
linear funtions, whih is exponential in the number of observations and in the worst ase 
takes O(jAjjSj 
2 
j  
i 
j 
jj 
) time. 
As H 
FIB 
updates are of polynomial omplexity one an nd the approximation for the 
nite-horizon ase eÆiently. The open issue remains the problem of nding the solution 
for the innite-horizon disounted ase and its omplexity. To address it we establish the 
following theorem. 
Theorem 8 A solution for the fast informed bound approximation an be found by solving 
an MDP with jSjjAjjj states, jAj ations and the same disount fator . 
The full proof of the theorem is deferred to the Appendix. The key part of the proof 
is the onstrution of an equivalent MDP with jSjjAjjj states representing H 
FIB 
updates. 
Sine a nite-state MDP an be solved through linear program onversion, the xed-point 
solution for the fast informed bound update is omputable eÆiently. 
4.2.1 Fast Informed Bound versus Fully-Observable MDP Approximations 
The fast informed update upper-bounds the exat update and is tighter than both the MDP 
and the QMDP approximation updates. 
Theorem 9 Let 
b 
V 
i 
orresponds to a pieewise linear onvex value funtion dened by   
i 
linear funtions. Then H 
b 
V 
i 
 H 
FIB 
b 
V 
i 
 H 
QMDP 
b 
V 
i 
 H 
MDP 
b 
V 
i 
: 
The key trik in deriving the above result is to swap max and sum operators (the 
proof is in the Appendix) and thus obtain both to the upper-bound inequalities and the 
subsequent redution in the omplexity of update rules ompared to the exat update. 
This is also shown in Figure 15. The UMDP approximation, also inluded in Figure 15, 
is disussed later in Setion 4.3. Thus, the dierene among the methods boils down to 
simple mathematial manipulations. Note that the same inequality relations as derived for 
updates hold also for their xed-point solutions (through Theorem 6). 
Figure 13a illustrates the improvement of the bound over MDP-based approximations 
on the Maze20 problem. Note, however, that this improvement is paid for by the inreased 
running-time omplexity (Figure 13b). 
4.2.2 Control 
The fast informed bound always outputs a pieewise linear and onvex funtion, with one 
linear funtion per ation. This allows us to build a POMDP ontroller that selets an ation 
assoiated with the best (highest value) linear funtion diretly. Figure 14 ompares the 
ontrol performane of the diret and the lookahead ontrollers to the MDP and the QMDP 
ontrollers. We see that the fast informed bound leads not only to tighter bounds but also 
60
Value-Funtion Approximations for POMDPs 
V b b s s a P s o s a b s s i 
a A s S s Ss So 
i 
i i 
+ ∈ ∈ ∈ ∈∈∈ = + 
   
   
∑ ∑∑∑1( ) max ( ) ( , ) max ( ' , | , ) ( ) ( ' ) ' 
ρ γ α α ΓΘ 
UMDP update: 
fast informed bound update: 
V b b s s a P s o s a s i 
a A s S s So 
i 
i i 
+ ∈ ∈ ∈ ∈∈ = + 
 
  
 
  
   
   
∑ ∑∑1 ( ) max ( ) ( , ) max ( ' , | , ) ( ' ) ' 
ρ γ α α ΓΘ 
V b b s s a P s s a b s s i 
a A s S s Ss S 
i 
i i 
+ ∈ ∈ ∈ ∈∈ = + 
   
   
∑ ∑∑1 ( ) max ( ) ( , ) max ( ' | , ) ( ) ( ' ) ' 
ρ γ α α Γ 
exact update: 
≤ 
≤ 
V b b s s a P s s a s i 
a A s S s S 
i 
i i 
+ ∈ ∈ ∈ ∈ = + 
   
   
   
   
∑ ∑1( ) max ( ) ( , ) ( ' | , ) max ( ' ) ' 
ρ γ α α Γ 
≤QMDP approx. update: 
MDP approx. update: 
V b b s s a P s s a s i 
s S a A 
s S 
i 
i i 
+ ∈ ∈ ∈ ∈ 
= +  
  
 
 ∑ ∑1( ) ( ) max ( , ) ( ' | , ) max ( ' ) 
' 
ρ γ α α Γ 
≤ 
Figure 15: Relations between the exat update and the UMDP, the fast informed bound, 
the QMDP and the MDP updates. 
to improved ontrol on average. However, we stress that urrently there is no theoretial 
underpinning for this observation and thus it may not be true for all belief states and any 
problem. 
4.2.3 Extensions of the Fast Informed Bound Method 
The main idea of the fast informed bound method is to selet the best linear funtion for 
every observation and every urrent state separately. This diers from the exat update 
where we seek a linear funtion that gives the best result for every observation and the 
ombination of all states. However, we observe that there is a great deal of middle ground 
between these two extremes. Indeed, one an design an update rule that hooses optimal 
(maximal) linear funtions for disjoint sets of states separately. To illustrate this idea, 
assume a partitioning S = fS 
1 
; S 
2 
;    ; S 
m 
g of the state spae S. The new update for S is: 
b 
V 
i+1 
(b) = max 
a2A 
( 
X 
s2S 
(s; a)b(s) +  
X 
o2 
2 
4 
max 
 
i 
2  
i 
X 
s2S 
1 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
)+ 
max 
 
i 
2  
i 
X 
s2S 
2 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) +   + 
max 
 
i 
2  
i 
X 
s2S 
m 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
3 
5 
9 
= 
; 
It is easy to see that the update upper-bounds the exat update. Exploration of this 
approah and various partitioning heuristis remains an interesting open researh issue. 
61
Hauskreht 
4.3 Approximation with Unobservable MDP 
The MDP-approximation assumes full observability of POMDP states to obtain simpler 
and more eÆient updates. The other extreme is to disard all observations available to 
the deision maker. An MDP with no observations is alled unobservable MDP (UMDP) 
and one may hoose its value-funtion solution as an alternative approximation. 
To nd the solution for the unobservable MDP, we derive the orresponding update 
rule, H 
UMDP 
, similarly to the update for the partially observable ase. H 
UMDP 
preserves 
pieewise linearity and onvexity of the value funtion and is a ontration. The update 
equals: 
b 
V 
i+1 
(b) = max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  max 
 
i 
2  
i 
X 
s2S 
X 
s 
0 
2S 
P (s 
0 
js; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= (H 
UMDP 
b 
V 
i 
)(b); 
where   
i 
is a set of linear funtions desribing 
b 
V 
i 
. 
b 
V 
i+1 
remains pieewise linear and onvex 
and it onsists of at most j  
i 
jjAj linear funtions. This is in ontrast to the exat update, 
where the number of possible vetors in the next step an grow exponentially in the number 
of observations and leads to jAjj  
i 
j 
jj 
possible vetors. The time omplexity of the update is 
O(jAjjSj 
2 
j  
i 
j). Thus, starting from 
b 
V 
0 
with one linear funtion, the running-time omplexity 
for k updates is bounded by O(jAj 
k 
jSj 
2 
). The problem of nding the optimal solution for the 
unobservable MDP remains intratable: the nite-horizon ase is NP-hard(Burago et al., 
1996), and the disounted innite-horizon ase is undeidable (Madani et al., 1999). Thus, 
it is usually not very useful approximation. 
The update H 
UMDP 
lower-bounds the exat update, an intuitive result reeting the 
fat that one annot do better with less information. To provide some insight into how 
the two updates are related, we do the following derivation, whih also proves the bound 
property in an elegant way: 
(H 
b 
V 
i 
)(b) = max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
X 
s2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
 max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  max 
 
i 
2  
i 
X 
o2 
X 
s2S 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  max 
 
i 
2  
i 
X 
s2S 
X 
s 
0 
2S 
P (s 
0 
js; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= (H 
UMDP 
b 
V 
i 
)(b): 
We see that the dierene between the exat and UMDP updates is that the max and 
the sum over next-step observations are exhanged. This auses the hoie of  vetors in 
H 
UMDP 
to beome independent of the observations. One the sum and max operations are 
exhanged, the observations an be marginalized out. Reall that the idea of swaps leads 
to a number of approximation updates; see Figure 15 for their summary. 
62
Value-Funtion Approximations for POMDPs 
4.4 Fixed-Strategy Approximations 
A nite-state mahine (FSM) model is used primarily to dene a ontrol strategy. Suh a 
strategy does not require belief state updates sine it diretly maps sequenes of observations 
to sequenes of ations. The value funtion of an FSM strategy is pieewise linear and onvex 
and an be found eÆiently in the number of memory states (Setion 2.6.1). While in the 
poliy iteration and poliy approximation ontexts the value funtion for a spei strategy 
is used to quantify the goodness of the poliy in the rst plae, the value funtion alone an 
be also used as a substitute for the optimal value funtion. In this ase, the value funtion 
(dened over the belief spae) equals 
V 
C 
(b) = max 
x2M 
V 
C 
(x; b); 
where V 
C 
(x; b) = 
P 
s2S 
V 
C 
(x; s)b(s) is obtained by solving a set of jSjjM j linear equations 
(Setion 2.6.2). As remarked earlier, the value for the xed strategy lower-bounds the 
optimal value funtion, that is V 
C 
 V 
 
. 
To simplify the omparison of the xed-strategy approximation to other approximations, 
we an rewrite its solution also in terms of xed-strategy updates 
b 
V 
i+1 
(b) = max 
x2M 
8 
< 
: 
X 
s2S 
(s; (x))b(s) +  
X 
o2 
X 
s2S 
X 
s 
0 
2S 
P (o; s 
0 
js; (x))b(s) 
i 
((x; o); s 
0 
) 
9 
= 
; 
; 
= max 
x2M 
8 
< 
: 
X 
s2S 
b(s) 
2 
4 
(s; (x)) +  
X 
o2 
X 
s 
0 
2S 
P (o; s 
0 
js; (x)) 
i 
((x; o); s 
0 
) 
3 
5 
9 
= 
; 
= (H 
FSM 
b 
V 
i 
)(b): 
The value funtion 
b 
V 
i 
is pieewise linear and onvex and onsists of jM j linear funtions 
 
i 
(x; :). For the innite-horizon disounted ase  
i 
(x; s) represents the ith approximation of 
V 
C 
(x; s). Note that the update an be applied to the nite-horizon ase in a straightforward 
way. 
4.4.1 Quality of Control 
Assume we have an FSM strategy and would like to use it as a substitute for the optimal 
ontrol poliy. There are three dierent ways in whih we an use it to extrat the ontrol. 
The rst is to simply exeute the strategy represented by the FSM. There is no need 
to update belief states in this ase. The seond possibility is to hoose linear funtions 
orresponding to dierent memory states and their assoiated ations repeatedly in every 
step. We refer to suh a ontroller as a diret (DR) ontroller. This approah requires 
updating of belief states in every step. On the other hand its ontrol performane is no 
worse than that of the FSM ontrol. The nal strategy disards all the information about 
ations and extrats the poliy by using the value funtion 
b 
V (b) and one-step lookahead. 
This method (LA) requires both belief state updates and lookaheads and leads to the worst 
reative time. Like DR, however, this strategy is guaranteed to be no worse than the FSM 
ontroller. The following theorem relates the performanes of the three ontrollers. 
63
Hauskreht 
control performance 
LA controller DR controllerFSM controller 
20 
30 
40 
50 
60 
70 
s c o 
re 
reaction times 
0.0001 
LA controllerDR controllerFSM controller 
0 
0.005 
0.01 
0.015 
0.02 
0.025 
ti m 
e  [ 
s e c ] 
Figure 16: Comparison of three dierent ontrollers (FSM, DR and LA) for the Maze20 
problem and a olletion of one-ation poliies: ontrol quality (left) and re-
sponse time (right). Error-bars in the ontrol performane graph indiate the 
ritial sore dierene at whih any two methods beome statistially dierent 
at signiane level 0.05. 
Theorem 10 Let C 
FSM 
be an FSM ontroller. Let C 
DR 
and C 
LA 
be the diret and the 
one-step-lookahead ontrollers onstruted based on C 
FSM 
. Then V 
C 
FSM 
(b)  V 
C 
DR 
(b) and 
V 
C 
FSM 
(b)  V 
C 
LA 
(b) hold for all belief states b 2 I. 
Though we an prove that both the diret ontroller and the lookahead ontroller are 
always better than the underlying FSM ontroller (see Appendix for the full proof of the 
theorem), we annot show the similar property between the rst two ontrollers for all initial 
belief states. However, the lookahead approah typially tends to dominate, reeting the 
usual trade-o between ontrol quality and response time. We illustrate this trade-o on 
our running Maze20 example and a olletion of jAj one-ation poliies, eah generating a 
sequene of the same ation. Control quality and response time results are shown in Figure 
16. We see that the ontroller based on the FSM is the fastest of the three, but it is also the 
worst in terms of ontrol quality. On the other hand, the diret ontroller is slower (it needs 
to update belief states in every step) but delivers better ontrol. Finally, the lookahead 
ontroller is the slowest and has the best ontrol performane. 
4.4.2 Seleting the FSM Model 
The quality of a xed-strategy approximation depends strongly on the FSM model used. 
The model an be provided a priori or onstruted automatially. Tehniques for automati 
onstrution of FSM poliies orrespond to a searh problem in whih either the omplete or 
a restrited spae of poliies is examined to nd the optimal or the near-optimal poliy for 
suh a spae. The searh proess is equivalent to poliy approximations or poliy-iteration 
tehniques disussed earlier in Setions 2.6 and 3.2. 
64
Value-Funtion Approximations for POMDPs 
4.5 Grid-Based Approximations with Value Interpolation-Extrapolation 
A value funtion over a ontinuous belief spae an be approximated by a nite set of grid 
points G and an interpolation-extrapolation rule that estimates the value of an arbitrary 
point of the belief spae by relying only on the points of the grid and their assoiated values. 
Denition 8 (Interpolation-extrapolation rule) Let f : I ! IR be a real-valued funtion 
dened over the information spae I, G = fb 
G 
1 
; b 
G 
2 
;    b 
G 
k 
g be a set of grid points and 	 
G 
= 
f(b 
G 
1 
; f(b 
G 
1 
)); (b 
G 
2 
; f(b 
G 
2 
));    ; (b 
G 
k 
; f(b 
G 
k 
))g be a set of point-value pairs. A funtion R 
G 
: 
I  (I  IR) 
jGj 
! IR that estimates f at any point of the information spae I using only 
values assoiated with grid points is alled an interpolation-extrapolation rule. 
The main advantage of an interpolation-extrapolation model in estimating the true value 
funtion is that it requires us to ompute value updates only for a nite set of grid points 
G. Let 
b 
V 
i 
be the approximation of the ith value funtion. Then the approximation for the 
(i+ 1)th value funtion 
b 
V 
i+1 
an be obtained as 
b 
V 
i+1 
(b) = R 
G 
(b;	 
G 
i+1 
); 
where values assoiated with every grid point b 
G 
j 
2 G (and inluded in 	 
G 
i+1 
) are: 
' 
i+1 
(b 
G 
j 
) = (H 
b 
V 
i 
)(b 
G 
j 
) = max 
a2A 
( 
(b; a) +  
X 
o2 
P (ojb; a) 
b 
V 
i 
((b 
G 
j 
; o; a)) 
) 
: (9) 
The grid-based update an also be desribed in terms of a value-funtion mapping H 
G 
: 
b 
V 
i+1 
= H 
G 
b 
V 
i 
. The omplexity of suh an update is O(jGjjAjjSj 
2 
jjC 
Eval 
(R 
G 
; jGj)) where 
C 
Eval 
(R 
G 
; jGj) is the omputational ost of evaluating the interpolation-extrapolation rule 
R 
G 
for jGj grid points. We show later (Setion 4.5.3), that in some instanes, the need to 
evaluate the interpolation-extrapolation rule in every step an be eliminated. 
4.5.1 A Family of Convex Rules 
The number of all possible interpolation-extrapolation rules is enormous. We fous on a 
set of onvex rules that is a relatively small but very important subset of interpolation-
extrapolation rules. 
20 
Denition 9 (Convex rule) Let f be some funtion dened over the spae I, G = fb 
G 
1 
; b 
G 
2 
;    b 
G 
k 
g 
be a set of grid points, and 	 
G 
= f(b 
G 
1 
; f(b 
G 
1 
)); (b 
G 
2 
; f(b 
G 
2 
));    ; (b 
G 
k 
; f(b 
G 
k 
))g be a set of point-
value pairs. The rule R 
G 
for estimating f using 	 
G 
is alled onvex when for every b 2 I, 
the value 
b 
f(b) is: 
b 
f(b) = R 
G 
(b;	 
G 
) = 
jGj 
X 
j=1 
 
b 
j 
f(b 
j 
); 
suh that 0   
b 
j 
 1 for every j = 1;    ; jGj, and 
P 
jGj 
j=1 
 
b 
j 
= 1. 
20. We note that onvex rules used in our work are a speial ase of averagers introdued by Gordon (1995). 
The dierene is minor; the denition of an averager inludes a onstant (independent of grid points and 
their values) that is added to the onvex ombination. 
65
Hauskreht 
The key property of onvex rules is that their orresponding grid-based update H 
G 
is a 
ontration in the max norm (Gordon, 1995). Thus, the approximate value iteration based 
on H 
G 
onverges to the unique xed-point solution. In addition, H 
G 
based on onvex rules 
is isotone. 
4.5.2 Examples of Convex Rules 
The family of onvex rules inludes approahes that are very ommonly used in pratie, 
like nearest neighbor, kernel regression, linear point interpolations and many others. 
Take, for example, the nearest-neighbor approah. The funtion for a belief point b is 
estimated using the value at the grid point losest to it in terms of some distane metri M 
dened over the belief spae. Then, for any point b, there is exatly one nonzero parameter 
 
b 
j 
= 1 suh that k b   b 
G 
j 
k 
M 
k b   b 
G 
i 
k 
M 
holds for all i = 1; 2;    ; k. All other s are 
zero. Assuming the Eulidean distane metri, the nearest-neighbor approah leads to a 
pieewise onstant approximation, in whih regions with equal values orrespond to regions 
with a ommon nearest grid point. 
The nearest neighbor estimates the funtion value by taking into an aount only one 
grid point and its value. Kernel regression expands upon this by using more grid points. It 
adds up and weights their ontributions (values) aording to their distane from the target 
point. For example, assuming Gaussian kernels, the weight for a grid point b 
G 
j 
is 
 
b 
j 
=  exp 
 kb b 
G 
j 
k 
2 
M 
=2 
2 
; 
where  is a normalizing onstant ensuring that 
P 
jGj 
j=1 
 
b 
j 
= 1 and  is a parameter that 
attens or narrows weight funtions. For the Eulidean metri, the above kernel-regression 
rule leads to a smooth approximation of the funtion. 
Linear point interpolations are a sublass of onvex rules that in addition to onstraints 
in Denition 9 satisfy 
b = 
jGj 
X 
j=1 
 
b 
j 
b 
G 
j 
: 
That is, a belief point b is a onvex ombination of grid points and the s are the orre-
sponding oeÆients. Beause the optimal value funtion for the POMDP is onvex, the 
new onstraint is suÆient to prove the upper-bound property of the approximation. In 
general, there an be many dierent linear point-interpolations for a given grid. A halleng-
ing problem here is to nd the rule with the best approximation. We disuss these issues 
in Setion 4.5.7. 
4.5.3 Conversion to a Grid-Based MDP 
Assume that we would like to nd the approximation of the value funtion using our grid-
based onvex rule and grid-based update (Equation 9). We an view this proess also as 
a proess of nding a sequene of values ' 
1 
(b 
G 
j 
); ' 
2 
(b 
G 
j 
);    ; ' 
i 
(b 
G 
j 
);    for all grid-points 
b 
G 
j 
2 G. We show that in some instanes the sequene of values an be omputed without 
applying an interpolation-extrapolation rule in every step. In suh ases, the problem an 
66
Value-Funtion Approximations for POMDPs 
be onverted into a fully observable MDP with states orresponding to grid-points G. 
21 
We 
all this MDP a grid-based MDP. 
Theorem 11 Let G be a nite set of grid points and R 
G 
be a onvex rule suh that param-
eters  
b 
j 
are xed. Then the values of '(b 
G 
j 
) for all b 
G 
j 
2 G an be found by solving a fully 
observable MDP with jGj states and the same disount fator . 
Proof For any grid point b 
G 
j 
we an write: 
' 
i+1 
(b 
G 
j 
) = max 
a2A 
( 
(b 
G 
j 
; a) +  
X 
o2 
P (ojb 
G 
j 
; a) 
b 
V 
G 
i 
((b 
G 
j 
; a; o)) 
) 
= max 
a2A 
8 
< 
: 
(b 
G 
j 
; a) +  
X 
o2 
P (ojb 
G 
j 
; a) 
2 
4 
jGj 
X 
k=1 
 
o;a 
j;k 
' 
i 
(b 
G 
k 
) 
3 
5 
9 
= 
; 
= max 
a2A 
8 
< 
: 
h 
(b 
G 
j 
; a) 
i 
+  
jGj 
X 
k=1 
' 
G 
i 
(b 
G 
k 
) 
" 
X 
o2 
P (ojb 
G 
j 
; a) 
o;a 
j;k 
# 
9 
= 
; 
Now denoting [ 
P 
o2 
P (ojb 
j 
; a) 
G 
 
o;a 
j;k 
℄ as P (b 
G 
k 
jb 
G 
j 
; a), we an onstrut a fully observable 
MDP problem with states orresponding to grid points G and the same disount fator . 
The update step equals: 
' 
i+1 
(b 
G 
j 
) = max 
a2A 
8 
< 
: 
(b 
G 
j 
; a) +  
jGj 
X 
k=1 
P (b 
G 
k 
jb 
G 
j 
; a)' 
G 
i 
(b 
G 
k 
) 
9 
= 
; 
: 
The prerequisite 0   
b 
j 
 1 for every j = 1;    ; jGj and 
P 
jGj 
j=1 
 
b 
j 
= 1 guarantees that 
P (b 
G 
k 
jb 
G 
j 
; a) an be interpreted as true probabilities. Thus, one an ompute values '(b 
G 
j 
) 
by solving the equivalent fully-observable MDP. 2 
4.5.4 Solving Grid-Based Approximations 
The idea of onverting a grid-based approximation into a grid-based MDP is a basis of 
our simple but very powerful approximation algorithm. Briey, the key here is to nd 
the parameters (transition probabilities and rewards) of a new MDP model and then solve 
it. This proess is relatively easy if the parameters  used to interpolate-extrapolate the 
value of a non-grid point are xed (the assumption of Theorem 11). In suh a ase, we 
an determine parameters of the new MDP eÆiently in one step, for any grid set G. The 
nearest neighbor or the kernel regression are examples of rules with this property. Note that 
this leads to polynomial-time algorithms for nding values for all grid points (reall that an 
MDP an be solved eÆiently for both nite and disounted, innite-horizon riteria). 
The problem in solving grid-based approximation arises only when the parameters  
used in the interpolation-extrapolation are not xed and are subjet to the optimization 
itself. This happens, for example, when there are multiple ways of interpolating a value 
21. We note that a similar result has been also proved independently by Gordon (1995). 
67
Hauskreht 
at some point of the belief spae and we would like to nd the best interpolation (leading 
to the best values) for all grid points in G. In suh a ase, the orresponding \optimal" 
grid-based MDP annot be found in a single step and iterative approximation, solving a 
sequene of grid-based MDPs, is usually needed. The worst-ase omplexity of this problem 
remains an open question. 
4.5.5 Construting Grids 
An issue we have not touhed on so far is the seletion of grids. There are multiple ways to 
selet grids. We divide them into two lasses { regular and non-regular grids. 
Regular grids (Lovejoy, 1991a) partition the belief spae evenly into equal-size regions. 
22 
The main advantage of regular grids is the simpliity with whih we an loate grid points 
in the neighborhood of any belief point. The disadvantage of regular grids is that they 
are restrited to a spei number of points, and any inrease in grid resolution is paid for 
in an exponential inrease in the grid size. For example, a sequene of regular grids for a 
20-dimensional belief spae (orresponds to a POMDP with 20 states) onsists of 20, 210, 
1540, 8855, 42504,    grid points. 
23 
This prevents one from using the method with higher 
grid resolutions for problems with larger state spaes. 
Non-regular grids are unrestrited and thus provide for more exibility when grid reso-
lution must be inreased adaptively. On the other hand, due to irregularities, methods for 
loating grid points adjaent to an arbitrary belief point are usually more omplex when 
ompared to regular grids. 
4.5.6 Linear Point Interpolation 
The fat that the optimal value funtion V 
 
is onvex for a belief-state MDPs an be used 
to show that the approximation based on linear point interpolation always upper-bounds 
the exat solution (Lovejoy, 1991a, 1993). Neither kernel regression nor nearest neighbor 
an guarantee us any bound. 
Theorem 12 (Upper bound property of a grid-based point interpolation update). Let 
b 
V 
i 
be 
a onvex value funtion. Then H 
b 
V 
i 
 H 
G 
b 
V 
i 
. 
The upper-bound property of H 
G 
update for onvex value funtions follows diretly 
from Jensen's inequality. The onvergene to an upper-bound follows from Theorem 6. 
Note that the point-interpolation update imposes an additional onstraint on the hoie 
of grid points. In partiular, it is easy to see that any valid grid must also inlude ex-
treme points of the belief simplex (extreme points orrespond to (1; 0; 0;   ); (0; 1; 0;   ), 
22. Regular grids used by Lovejoy (1991a) are based on Freudenthal triangulation (Eaves, 1984). Essen-
tially, this is the same idea as used to partition evenly the n-dimensional subspae of IR 
n 
. In fat, an 
aÆne transform allows us to map isomorphially grid points in the belief spae to grid points in the 
n-dimensional spae (Lovejoy, 1991a). 
23. The number of points in the regular grid sequene is given by (Lovejoy, 1991a): 
jGj = 
(M + jSj   1)! 
M !(jSj   1)! 
; 
where M = 1; 2;    is a grid renement parameter. 
68
Value-Funtion Approximations for POMDPs 
et.). Without extreme points one would be unable to over the whole belief spae via 
interpolation. Nearest neighbor and kernel regression impose no restritions on the grid. 
4.5.7 Finding the best interpolation 
In a general, there are multiple ways to interpolate a point of a belief spae. Our objetive 
is to nd the best interpolation, that is, the one that leads to the tightest upper bound of 
the optimal value funtion. 
Let b be a belief point and f(b 
j 
; f(b 
j 
))jb 
j 
2 Gg a set of grid-value pairs. Then the best 
interpolation for point b is: 
b 
f(b) = min 
 
jGj 
X 
j=1 
 
j 
f(b 
j 
) 
subjet to 0   
j 
 1 for all j = 1;    ; jGj, 
P 
jGj 
j=1 
 
j 
= 1, and b = 
P 
jGj 
j=1 
 
j 
b 
G 
j 
. 
This is a linear optimization problem. Although it an be solved in polynomial time 
(using linear programming tehniques), the omputational ost of doing this is still relatively 
large, espeially onsidering the fat that the optimization must be repeated many times. 
To alleviate this problem we seek more eÆient ways of nding the interpolation, sariing 
the optimality. 
One way to nd a (suboptimal) interpolation quikly is to apply regular grids proposed 
by Lovejoy (1991a). In this ase the value at a belief point is approximated using the 
onvex ombination of grid points losest to it. The approximation leads to pieewise linear 
and onvex value funtions. As all interpolations are xed here, the problem of nding 
the approximation an be onverted into an equivalent grid-based MDP and solved as a 
nite-state MDP. However, as pointed in the previous setion, the regular grids must use a 
spei number of grid points and any inrease in the resolution of a grid is paid for by an 
exponential inrease in the grid size. This feature makes the method less attrative when 
we have a problem with a large state spae and we need to ahieve high grid resolution. 
24 
In the present work we fous on non-regular (or arbitrary) grids. We propose an inter-
polation approah that searhes a limited spae of interpolations and is guaranteed to run 
in time linear in the size of the grid. The idea of the approah is to interpolate a point 
b of a belief spae of dimension jSj with a set of grid points that onsists of an arbitrary 
grid point b 
0 
2 G and jSj   1 extreme points of the belief simplex. The oeÆients of this 
interpolation an be found eÆiently and we searh for the best suh interpolation. Let 
b 
0 
2 G be a grid point dening one suh interpolation. Then the value at point b satises 
b 
V 
i 
(b) = min 
b 
0 
2G 
b 
V 
b 
0 
i 
(b); 
where 
b 
V 
b 
0 
i 
is the value of the interpolation for the grid point b 
0 
. Figure 17 illustrates the 
resulting approximation. The funtion is haraterized by its \sawtooth" shape, whih is 
inuened by the hoie of the interpolating set. 
To nd the best value-funtion solution or its lose approximation we an apply a value 
iteration proedure in whih we searh for the best interpolation after every update step. 
24. One solution to this problem may be to use adaptive regular grids in whih grid resolution is inreased 
only in some parts of the belief spae. We leave this idea for future work. 
69
Hauskreht 
V(b)* 
V(b) 
1b(s  ) 
V(b) 
10 b0 b b b b1 2 3 4 
Figure 17: Value-funtion approximation based on the linear-time interpolation approah 
(a two-dimensional ase). Interpolating sets are restrited to a single internal 
point of the belief spae. 
The drawbak of this approah is that interpolations may remain unhanged for many 
update steps, thus slowing down the solution proess. An alternative approah is to solve 
a sequene of grid-based MDPs instead. In partiular, at every stage we nd the best 
(minimum value) interpolations for all belief points reahable from grid points in one step, x 
oeÆients of these interpolations (s), onstrut a grid-based MDP and solve it (exatly or 
approximately). This proess is repeated until no further improvement (or no improvement 
larger than some threshold) is seen in values at dierent grid points. 
4.5.8 Improving Grids Adaptively 
The quality of an approximation (bound) depends strongly on the points used in the grid. 
Our objetive is to provide a good approximation with the smallest possible set of grid 
points. However, this task is impossible to ahieve, sine it annot be known in advane 
(before solving) what belief points to pik. A way to address this problem is to build grids 
inrementally, starting from a small set of grid points and adding others adaptively, but 
only in plaes with a greater hane of improvement. The key part of this approah is a 
heuristi for hoosing grid points to be added next. 
One heuristi method we have developed attempts to maximize improvements in bound 
values via stohasti simulations. The method builds on the fat that every interpolation 
grid must also inlude extreme points (otherwise we annot over the entire belief spae). 
As extreme points and their values aet the other grid points, we try to improve their 
values in the rst plae. In general, a value at any grid point b improves more the more 
preise values are used for its suessor belief points, that is, belief states that orrespond 
to (b; a 
 
; o) for a hoie of observation o. a 
 
is the urrent optimal ation hoie for b. 
Inorporating suh points into the grid then makes a larger improvement in the value at 
the initial grid point b more likely. Assuming that our initial point is an extreme point, we 
have a heuristi that tends to improve a value for that point. Naturally, one an proeed 
further with this seletion by inorporating the suessor points for the rst-level suessors 
into the grid as well, and so forth. 
70
Value-Funtion Approximations for POMDPs 
generate new grid points (G; 
b 
V 
G 
) 
set G 
new 
= fg 
for all extreme points b do 
repeat until b =2 G [G 
new 
set a 
 
= argmax 
a 
n 
(b; a) +  
P 
o2 
P (ojb; a) 
b 
V 
G 
((b; a; o)) 
o 
selet observation o aording to P (ojb; a 
 
) 
update b = (b; a 
 
; o) 
add b into G 
new 
return G 
new 
Figure 18: Proedure for generating additional grid points based on our bound improve-
ment heuristi. 
bound quality 
40 
80 120160200240280320360400 
40 80 120160200240280320360400 
interpolation 
random grid 
interpolation 
adaptive grid QMDP MDP 
fast 
informed interpolation 
regular grid 
40 
60 
80 
100 
120 
140 
s c o 
re 
Figure 19: Improvement in the upper bound quality for grid-based point-interpolations 
based on the adaptive-grid method. The method is ompared to randomly 
rened grid and the regular grid with 210 points. Other upper-bound approxi-
mations (the MDP, QMDP and fast informed bound methods) are inluded for 
omparison. 
To apture this idea, we generate new grid points via simulation, starting from one 
of the extremes of the belief simplex and ontinuing until a belief point not urrently in 
the grid is reahed. An algorithm that implements the bound improvement heuristi and 
expands the urrent grid G with a set of jSj new grid points while relying on the urrent 
value-funtion approximation 
b 
V 
G 
is shown in Figure 18. 
Figure 19 illustrates the performane (bound quality) of our adaptive grid method on 
the Maze20 problem. Here we use the ombination of adaptive grids with our linear-time 
interpolation approah. The method gradually expands the grid in 40 point inrements up to 
400 grid points. Figure 19 also shows the performane of the random-grid method in whih 
71
Hauskreht 
running times 
1.26 40 80 120 
160 200 
240 
280 
320 
360 
400 
40 80 120 160 
200 240 
280 320 
360 
400 
50.02 
interpolation 
random grid 
interpolation 
adaptive grid 
interpolation 
regular grid 
fast 
informed QMDPMDP 
1.26 0 
500 
1000 
1500 
2000 
2500 
3000 
3500 
4000 
4500 
5000 
ti m 
e  [ 
s e c ] 
Figure 20: Running times of grid-based point-interpolation methods. Methods tested in-
lude the adaptive grid, the random grid, and the regular grid with 210 grid 
points. Running times for the adaptive-grid are umulative, reeting the de-
pendenies of higher grid resolutions on the lower-level resolutions. The running 
time results for the MDP, QMDP, and fast informed bound approximations are 
shown for omparison. 
new points of the grid are seleted iniformly at random (results for 40 grid point inrements 
are shown). In addition, the gure gives results for the regular grid interpolation (based 
on Lovejoy (1991a)) with 210 belief points and other upper-bound methods: the MDP, the 
QMDP and the fast informed bound approximations. 
We see a dramati improvement in the quality of the bound for the adaptive method. 
In ontrast to this, the uniformly sampled grid (random-grid approah) hardly hanges the 
bound. There are two reasons for this: (1) uniformly sampled grid points are more likely to 
be onentrated in the enter of the belief simplex; (2) the transition matrix for the Maze20 
problem is relatively sparse, the belief points one obtains from the extreme points in one 
step are on the boundary of the simplex. Sine grid points in the enter of the simplex 
are never used to interpolate belief states reahable from extremes in one step they annot 
improve values at extremes and the bound does not hange. 
One drawbak of the adaptive method is its running time (for every grid size we need 
to solve a sequene of grid-based MDPs). Figure 20 ompares running times of dierent 
methods on the Maze20 problem. As grid-expansion of the adaptive method depends on 
the value funtion obtained for previous steps, we plot its umulative running times. We 
see a relatively large inrease in running time, espeially for larger grid sizes, reeting 
the trade-o between the bound quality and running time. However, we note that the 
adaptive-grid method performs quite well in the initial few steps, and with only 80 grid 
points outperforms the regular grid (with 210 points) in bound quality. 
Finally, we note that other heuristi approahes to onstruting adaptive grids for point 
interpolation are possible. For example, a dierent approah that renes the grid by ex-
72
Value-Funtion Approximations for POMDPs 
control performance 
MDP QMDP fast 
informed interpolation 
 (regular grid) nearest-neighbor 
(random grid) 
nearest-neighbor 
(adaptive grid) 
interpolation 
 (random grid) 
interpolation 
 (adaptive grid) 
40 
200 400 
40 200 400 
40 
200 400 
40 
200 400 
20 
30 
40 
50 
60 
70 
s c 
o re 
Figure 21: Control performane of lookahead ontrollers based on grid-based point inter-
polation and nearest neighbor methods and varying grid sizes. The results are 
ompared to the MDP, the QMDP and the fast informed bound ontrollers. 
amining dierenes in values at urrent grid points has reently been proposed by Brafman 
(1997). 
4.5.9 Control 
Value funtions obtained for dierent grid-based methods dene a variety of ontrollers. Fig-
ure 21 ompares the performanes of lookahead ontrollers based on the point-interpolation 
and nearest-neighbor methods. We run two versions of both approahes, one with the adap-
tive grid, the other with the random grid, and we show results obtained for 40, 200 and 400 
grid points. In addition, we ompare their performanes to the interpolation with regular 
grids (with 210 grid points), the MDP, the QMDP and the fast informed bound approahes. 
Overall, the performane of the interpolation-extrapolation tehniques we tested on 
the Maze20 problem was a bit disappointing. In partiular, better sores were ahieved 
by the simpler QMDP and fast informed bound methods. We see that, although heuristis 
improved the bound quality of approximations, they did not lead to the similar improvement 
over the QMDP and the fast informed bound methods in terms of ontrol. This result 
shows that a bad bound (in terms of absolute values) does not always imply bad ontrol 
performane. The main reason for this is that the ontrol performane is inuened mostly 
by relative rather than absolute value-funtion values (or, in other words, by the shape 
of the funtion). All interpolation-extrapolation tehniques we use (exept regular grid 
interpolation) approximate the value funtion with funtions that are not pieewise linear 
and onvex; the interpolations are based on the linear-time interpolation tehnique with a 
sawtooth-shaped funtion, and the nearest-neighbor leads to a pieewise-onstant funtion. 
This does not allow them to math the shape of the optimal funtion orretly. The other 
fator that aets the performane is a large sensitivity of methods to the seletion of grid 
points, as doumented, for example, by the omparison of heuristi and random grids. 
73
Hauskreht 
In the above tests we foused on lookahead ontrollers only. However, an alternative way 
to dene a ontroller for grid-based interpolation-extrapolation methods is to use Q-funtion 
approximations instead of value funtions, and either diret or lookahead designs. 
25 
Q-
funtion approximations an be found by solving the same grid-based MDP, and by keeping 
values (funtions) for dierent ations separate at the end. 
4.6 Approximations of Value Funtions Using Curve Fitting (Least-Squares 
Fit) 
An alternative way to approximate a funtion over a ontinuous spae is to use urve-tting 
tehniques. This approah relies on a predened parametri model of the value funtion 
and a set of values assoiated with a nite set of (grid) belief points G. The approah 
is similar to interpolation-extrapolation tehniques in that it relies on a set of belief-value 
pairs. The dierene is that the urve tting, instead of remembering all belief-value pairs, 
tries to summarize them in terms of a given parametri funtion model. The strategy seeks 
the best possible math between model parameters and observed point values. The best 
math an be dened using various riteria, most often the least-squares t riterion, where 
the objetive is to minimize 
Error(f) = 
1 
2 
X 
j 
[y 
j 
  f(b 
j 
)℄ 
2 
: 
Here b 
j 
and y 
j 
orrespond to the belief point and its assoiated value. The index j ranges 
over all points of the sample set G. 
4.6.1 Combining Dynami Programming and Least-Squares Fit 
The least-squares approximation of a funtion an be used to onstrut a dynami-programming 
algorithm with an update step: 
b 
V 
i+1 
= H 
LSF 
b 
V 
i 
. The approah has two steps. First, we 
obtain new values for a set of sample points G: 
' 
i+1 
(b) = (H 
b 
V 
i 
)(b) = max 
a2A 
( 
X 
s2S 
(s; a)b(s) +  
X 
o2 
X 
s2S 
P (ojs; a)b(s) 
b 
V 
i 
((b; a; o)) 
) 
: 
Seond, we t the parameters of the value-funtion model 
b 
V 
i+1 
using new sample-value pairs 
and the square-error ost funtion. The omplexity of the update isO(jGjjAjjSj 
2 
jjC 
Eval 
( 
b 
V 
i 
)+ 
C 
Fit 
( 
b 
V 
i+1 
; jGj)) time, where C 
Eval 
( 
b 
V 
i 
) is the omputational ost of evaluating 
b 
V 
i 
and 
C 
Fit 
( 
b 
V 
i+1 
; jGj) is the ost of tting parameters of 
b 
V 
i+1 
to jGj belief-value pairs. 
The advantage of the approximation based on the least-squares t is that it requires us 
to ompute updates only for the nite set of belief states. The drawbak of the approah 
is that, when ombined with the value-iteration method, it an lead to instability and/or 
divergene. This has been shown for MDPs by several researhers (Bertsekas, 1994; Boyan 
& Moore, 1995; Baird, 1995; Tsitsiklis & Roy, 1996). 
25. This is similar to the QMDP method, whih allows both lookahead and greedy designs. In fat, QMDP 
an be viewed as a speial ase of the grid-based method with Q-funtion approximations, where grid 
points orrespond to extremes of the belief simplex. 
74
Value-Funtion Approximations for POMDPs 
4.6.2 On-line Version of the Least-Squares Fit 
The problem of nding a set of parameters with the best t an be solved by any available 
optimization proedure. This inludes the on-line (or instane-based) version of the gradient 
desent method, whih orresponds to the well-known delta rule (Rumelhart, Hinton, & 
Williams, 1986). 
Let f denote a parametri value funtion over the belief spae with adjustable weights 
w = fw 
1 
; w 
2 
;    ; w 
k 
g. Then the on-line update for a weight w 
i 
is omputed as: 
w 
i 
 w 
i 
   
i 
(f(b 
j 
)  y 
j 
) 
f 
w 
i 
j 
b 
j 
; 
where  
i 
is a learning onstant, and b 
j 
and y 
j 
are the last-seen point and its value. Note 
that the gradient desent method requires the funtion to be dierentiable with regard to 
adjustable weights. 
To solve the disounted innite-horizon problem, the stohasti (on-line) version of a 
least-squares t an be ombined with either parallel (synhronous) or inremental (Gauss-
Seidel) point updates. In the rst ase, the value funtion from the previous step is xed 
and a new value funtion is omputed from srath using a set of belief point samples and 
their values omputed through one-step expansion. One the parameters are stabilized (by 
attenuating learning rates), the newly aquired funtion is xed, and the proess proeeds 
with another iteration. In the inremental version, a single value-funtion model is at the 
same time updated and used to ompute new values at sampled points. Littman et al. (1995) 
and Parr and Russell (1995) implement this approah using asynhronous reinforement 
learning bakups in whih sample points to be updated next are obtained via stohasti 
simulation. We stress that all versions are subjet to the threat of instability and divergene, 
as remarked above. 
4.6.3 Parametri Funtion Models 
To apply the least-squares approah we must rst selet an appropriate value funtion 
model. Examples of simple onvex funtions are linear or quadrati funtions, but more 
omplex models are possible as well. 
One interesting and relatively simple approah is based on the least-squares approx-
imation of linear ation-value funtions (Q-funtions) (Littman et al., 1995). Here the 
value funtion 
b 
V 
i+1 
is approximated as a pieewise linear and onvex ombination of 
b 
Q 
i+1 
funtions: 
b 
V 
i+1 
(b) = max 
a2A 
b 
Q 
i+1 
(b; a); 
where 
b 
Q 
i+1 
(b; a) is the least-squares t of a linear funtion for a set of sample points G. 
Values at points in G are obtained as 
' 
a 
i+1 
(b) = (b; a) +  
X 
o2 
P (ojb; a) 
b 
V 
i 
((b; o; a)): 
The method leads to an approximation with jAj linear funtions and the oeÆients of these 
funtions an be found eÆiently by solving a set of linear equations. Reall that other two 
approximations (the QMDP and the fast informed bound approximations) also work with 
75
Hauskreht 
jAj linear funtions. The main dierenes between the methods are that the QMDP and 
fast informed bound methods update linear funtions diretly, and they guarantee upper 
bounds and unique onvergene. 
A more sophistiated parametri model of a onvex funtion is the softmax model (Parr 
& Russell, 1995): 
b 
V (b) = 
2 
4 
X 
2  
" 
X 
s2S 
(s)b(s) 
# 
k 
3 
5 
1 
k 
; 
where   is the set of linear funtions  with adaptive parameters to t and k is a \tempera-
ture" parameter that provides a better t to the underlying pieewise linear onvex funtion 
for larger values. The funtion represents a soft approximation of a pieewise linear onvex 
funtion, with the parameter k smoothing the approximation. 
4.6.4 Control 
We tested the ontrol performane of the least-squares approah on the linear Q-funtion 
model (Littman et al., 1995) and the softmax model (Parr & Russell, 1995). For the softmax 
model we varied the number of linear funtions, trying ases with 10 and 15 linear funtions 
respetively. In the rst set of experiments we used parallel (synhronous) updates and 
samples at a xed set of 100 belief points. We applied stohasti gradient desent tehniques 
to nd the best t in both ases. We tested the ontrol performane for value-funtion 
approximations obtained after 10, 20 and 30 updates, starting from the QMDP solution. In 
the seond set of experiments, we applied the inremental stohasti update sheme with 
Gauss-Seidel-style updates. The results for this method were aquired after every grid point 
was updated 150 times, with learning rates dereasing linearly in the range between 0:2 and 
0:001. Again we started from the QMDP solution. The results for lookahead ontrollers are 
summarized in Figure 22, whih also shows the ontrol performane of the diret Q-funtion 
ontroller and, for omparison, the results for the QMDP method. 
The linear-Q funtion model performed very well and the results for the lookahead design 
were better than the results for the QMDP method. The dierene was quite apparent for 
diret approahes. In general, the good performane of the method an be attributed to 
the hoie of a funtion model that let us math the shape of the optimal value funtion 
reasonably well. In ontrast, the softmax models (with 10 and 15 linear funtions) did not 
perform as expeted. This is probably beause in the softmax model all linear funtions are 
updated for every sample point. This leads to situations in whih multiple linear funtions 
try to trak a belief point during its update. Under these irumstanes it is hard to apture 
the struture of the optimal value funtion aurately. The other negative feature is that 
the eets of on-line hanges of all linear funtions are added in the softmax approximation, 
and thus ould bias inremental update shemes. In the ideal ase, we would like to identify 
one vetor  responsible for a spei belief point and update (modify) only that vetor. 
The linear Q-funtion approah avoids this problem by always updating only a single linear 
funtion (orresponding to an ation). 
76
Value-Funtion Approximations for POMDPs 
control performance 
stoch 
30 
 iter 
20 
 iter10 
 iter 
stoch 
30 
 iter 20 
 iter 10 
 iter 
stoch 30 
 iter 
20 
 iter 
10 
 iter 
direct 
lookahead 
QMDP 
 approximation linear Q-function 
lookahead 
20 
 iter 30 
 iter stoch 
linear Q-function 
 direct 
softmax 
(15 linear functions) 
softmax 
(10 linear functions) 
10 
 iter 
20 
30 
40 
50 
60 
70 
s c o 
re 
Figure 22: Control performane of least-squares t methods. Models tested inlude: linear 
Q-funtion model (with both diret and lookahead ontrol) and softmax mod-
els with 10 and 15 linear funtions (lookahead ontrol only). Value funtions 
obtained after 10, 20 and 30 synhronous updates and value funtions obtained 
through the inremental stohasti update sheme are used to dene dierent 
ontrollers. For omparison, we also inlude results for two QMDP ontrollers. 
4.7 Grid-Based Approximations with Linear Funtion Updates 
An alternative grid-based approximation method an be onstruted by applying Sondik's 
approah for omputing derivatives (linear funtions) to points of the grid (Lovejoy, 1991a, 
1993). Let 
b 
V 
i 
be a pieewise linear onvex funtion desribed by a set of linear funtions   
i 
. 
Then a new linear funtion for a belief point b and an ation a an be omputed eÆiently 
as (Smallwood & Sondik, 1973; Littman, 1996) 
 
b;a 
i+1 
(s) = (s; a) +  
X 
o2 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
(b;a;o) 
i 
(s 
0 
); (10) 
where (b; a; o) indexes a linear funtion  
i 
in a set of linear funtions   
i 
(dening 
b 
V 
i 
) that 
maximizes the expression 
X 
s 
0 
2S 
" 
X 
s2S 
P (s 
0 
; ojs; a)b(s) 
# 
 
i 
(s 
0 
) 
for a xed ombination of b; a; o. The optimizing funtion for b is then aquired by hoosing 
the vetor with the best overall value from all ation vetors. That is, assuming   
b 
i+1 
is a 
set of all andidate linear funtions, the resulting funtions satises 
 
b; 
i+1 
= arg max 
 
b 
i+1 
2  
b 
i+1 
X 
s2S 
 
b 
i+1 
(s)b(s): 
A olletion of linear funtions obtained for a set of belief points an be ombined into 
a pieewise linear and onvex value funtion. This is the idea behind a number of exat 
77
Hauskreht 
1b(s  ) 
V(b) 
V(b)* 
0 1 
V(b) 
new linear function 
b 
Figure 23: An inremental version of the grid-based linear funtion method. The pieewise 
linear lower bound is improved by a new linear funtion omputed for a belief 
point b using Sondik's method. 
algorithms (see Setion 2.4.2). However, in the exat ase, a set of points that over all 
linear funtions dening the new value funtion must be loated rst, whih is a hard task 
in itself. In ontrast, the approximation method uses an inomplete set of belief points that 
are xed or at least easy to loate, for example via random or heuristi seletion. We use 
H 
GL 
to denote the value-funtion mapping for the grid approah. 
The advantage of the grid-based method is that it leads to more eÆient updates. The 
time omplexity of the update is polynomial and equals O(jGjjAjjSj 
2 
jj). It yields a set of 
jGj linear funtions, ompared to jAjj  
i 
j 
jj 
possible funtions for the exat update. 
Sine the set of grid-points is inomplete, the resulting approximation lower-bounds the 
value funtion one would obtain by performing the exat update (Lovejoy, 1991a). 
Theorem 13 (Lower-bound property of the grid-based linear funtion update). Let 
b 
V 
i 
be a 
pieewise linear value funtion and G a set of grid points used to ompute linear funtion 
updates. Then H 
GL 
b 
V 
i 
 H 
b 
V 
i 
. 
4.7.1 Inremental Linear-Funtion Approah 
The drawbak of the grid-based linear funtion method is that H 
GL 
is not a ontration 
for the disounted innite-horizon ase, and therefore the value iteration method based on 
the mapping may not onverge (Lovejoy, 1991a). To remedy this problem, we propose an 
inremental version of the grid-based linear funtion method. The idea of this renement is 
to prevent instability by gradually improving the pieewise linear and onvex lower bound 
of the value funtion. 
Assume that 
b 
V 
i 
 V 
 
is a onvex pieewise linear lower bound of the optimal value 
funtion dened by a linear funtion set   
i 
, and let  
b 
be a linear funtion for a point b 
that is omputed from 
b 
V 
i 
using Sondik's method. Then one an onstrut a new improved 
value funtion 
b 
V 
i+1 
 
b 
V 
i 
by simply adding the new linear funtion  
b 
into   
i 
. That is: 
  
i+1 
=   
i 
[  
b 
. The idea of the inremental update, illustrated in Figure 23, is similar 
to inremental methods used by Cheng (1988) and Lovejoy (1993). The method an be 
78
Value-Funtion Approximations for POMDPs 
bound quality 
1 2 
3 4 
5 6 
7 8 9 10 1 
2 3 4 5 6 7 8 9 10 
incremental approachstandard approach 
30 
35 
40 
45 
50 
55 
60 
65 
s c o 
re running times 
1 2 3 
4 5 
6 
8 
9 
10 
1 
2 
3 
4 
5 
6 
7 8 
9 10 
fast 
 informed QMDP 
7 
incremental approachstandard approach 
50.021.26 0 
500 
1000 
1500 
2000 
2500 
ti m 
e  [ 
s e 
c ] 
Figure 24: Bound quality and running times of the standard and inremental version of 
the grid-based linear-funtion method for the xed 40-point grid. Cumulative 
running times (inluding all previous update yles) are shown for both methods. 
Running times of the QMDP and the fast informed bound methods are inluded 
for omparison. 
extended to handle a set of grid points G in a straightforward way. Note also that after 
adding one or more new linear funtions to   
i 
, some of the previous linear funtions may 
beome redundant and an be removed from the value funtion. Tehniques for redundany 
heking are the same as are applied in the exat approahes (Monahan, 1982; Eagle, 1984). 
The inremental renement is stable and onverges for a xed set of grid points. The 
prie paid for this feature is that the linear funtion set   
i 
an grow in size over the iteration 
steps. Although the growth is at most linear in the number of iterations, ompared to 
the potentially exponential growth of exat methods, the linear funtion set desribing 
the pieewise linear approximation an beome huge. Thus, in pratie we usually stop 
inremental updates well before the method onverges. The question that remains open is 
the omplexity (hardness) of the problem of nding the xed-point solution for a xed set 
of grid points G. 
Figure 24 illustrates some of the trade-os involved in applying inremental updates 
ompared to the standard xed-grid approah on the Maze20 problem. We use the same 
grid of 40 points for both tehniques and the same initial value funtion. Results for 1-10 
update yles are shown. We see that the inremental method has longer running times 
than the standard method, sine the number of linear funtions an grow after every update. 
On the other hand, the bound quality of the inremental method improves more rapidly 
and it an never beome worse after more update steps. 
4.7.2 Minimum Expeted Reward 
The inremental method improves the lower bound of the value funtion. The value fun-
tion, say 
b 
V 
i 
, an be used to reate a ontroller (with either the lookahead or diret-ation 
hoie). In the general ase, we annot say anything about the performane quality of 
suh ontrollers with regard to 
b 
V 
i 
. However, under ertain onditions the performane of 
both ontrollers is guaranteed never to fall below 
b 
V 
i 
. The following theorem (proved in the 
Appendix) establishes these onditions. 
Theorem 14 Let 
b 
V 
i 
be a value funtion obtained via the inremental linear funtion method, 
starting from 
b 
V 
0 
, whih orresponds to some xed strategy C 
0 
. Let C 
LA;i 
and C 
DR;i 
be two 
79
Hauskreht 
ontrollers based on 
b 
V 
i 
: the lookahead ontroller and the diret ation ontroller, and V 
C 
LA;i 
, 
V 
C 
DR;i 
be their respetive value funtions. Then 
b 
V 
i 
 V 
C 
LA;i 
and 
b 
V 
i 
 V 
C 
DR;i 
hold. 
We note that the same property holds for the inremental version of exat value iteration. 
That is, both the lookahead and the diret ontrollers perform no worse than V 
i 
obtained 
after i inremental updates from some V 
0 
orresponding to a FSM ontroller C 
0 
. 
4.7.3 Seleting Grid Points 
The inremental version of the grid-based linear-funtion approximation is exible and 
works for an arbitrary grid. 
26 
Moreover, the grid need not be xed and an be hanged on 
line. Thus, the problem of nding grids redues to the problem of seleting belief points to 
be updated next. One an apply various strategies to do this. For example, one an use a 
xed set of grid points and update them repeatedly, or one an selet belief points on line 
using various heuristis. 
The inremental linear funtion method guarantees that the value funtion is always 
improved (all linear funtions from previous steps are kept unless found to be redundant). 
The quality of a new linear funtion (to be added next) depends strongly on the quality of 
linear funtions obtained in previous steps. Therefore, our objetive is to selet and order 
points with better hanes of larger improvement. To do this we have designed two heuristi 
strategies for seleting and ordering belief points. 
The rst strategy attempts to optimize updates at extreme points of the belief simplex 
by ordering them heuristially. The idea of the heuristi is based on the fat that states 
with higher expeted rewards (e.g. some designated goal states) bakpropagate their eets 
(rewards) loally. Therefore, it is desirable that states in the neighborhood of the highest 
reward state be updated rst, and the distant ones later. We apply this idea to order 
extreme points of the belief simplex, relying on the urrent estimate of the value funtion 
to identify the highest expeted reward states and on a POMDP model to determine the 
neighbor states. 
The seond strategy is based on the idea of stohasti simulation. The strategy generates 
a sequene of belief points more likely to be reahed from some (xed) initial belief point. 
The points of the sequene are then used in reverse order to generate updates. The intent 
of this heuristi is to \maximize" the improvement of the value funtion at the initial xed 
point. To run this heuristi, we need to nd an initial belief point or a set of initial belief 
points. To address this problem, we use the rst heuristi that allows us to order the 
extreme points of the belief simplex. These points are then used as initial beliefs for the 
simulation part. Thus, we have a two-tier strategy: the top-level strategy orders extremes 
of the belief simplex, and the lower-level strategy applies stohasti simulation to generate 
a sequene of belief states more likely reahable from a spei extreme point. 
We tested the order heuristis and the two-tier heuristis on our Maze20 problem, and 
ompared them also to two simple point seletion strategies: the xed-grid strategy, in 
whih a set of 40 grid points was updated repeatedly, and the random-grid strategy, in 
whih points were always hosen uniformly at random. Figure 25 shows the bound quality 
26. There is no restrition on the grid points that must be inluded in the grid, suh as was required for 
example in the linear point-interpolation sheme, whih had to use all extreme points of the belief 
simplex. 
80
Value-Funtion Approximations for POMDPs 
bound quality 
1 
2 3 4 5 6 7 8 9 10 
1 
2 3 
4 5 6 7 8 9 10 
1 
2 3 
4 5 6 7 8 9 10 
1 
2 3 
4 5 6 7 8 9 10 
2-tier heuristicorder heuristicrandom gridfixed grid 
30 
35 
40 
45 
50 
55 
60 
65 
s c o 
re 
Figure 25: Improvements in the bound quality for the inremental linear-funtion method 
and four dierent grid-seletion heuristis. Eah yle inludes 40 grid-point 
updates. 
of the methods for 10 update yles (eah yle onsists of 40 grid point updates) on the 
Maze20 problem. We see that the dierenes in the quality of value-funtion approximations 
for dierent strategies (even the very simple ones) are relatively small. We note that we 
observed similar results also for other problems, not just Maze20. 
The relatively small improvement of our heuristis an be explained by the fat that 
every new linear funtion inuenes a larger portion of the belief spae and thus the method 
should be less sensitive to a hoie of a spei point. 
27 
However, another plausible explana-
tion is that our heuristis were not very good and more aurate heuristis or ombinations 
of heuristis ould be onstruted. EÆient strategies for loating grid points used in some 
of the exat methods, e.g. the Witness algorithm (Kaelbling et al., 1999) or Cheng's meth-
ods (Cheng, 1988) an potentially be applied to this problem. This remains an open area 
of researh. 
4.7.4 Control 
The grid-based linear-funtion approah leads to a pieewise linear and onvex approxi-
mation. Every linear funtion omes with a natural ation hoie that lets us hoose the 
ation greedily. Thus we an run both the lookahead and the diret ontrollers. Figure 26 
ompares the performane of four dierent ontrollers for the xed grid of 40 points, om-
bining standard and inremental updates with lookahead and diret greedy ontrol after 1, 
5 and 10 update yles. The results (see also Figure 24) illustrate the trade-os between the 
omputational time of obtaining the solution and its quality. We see that the inremental 
approah and the lookahead ontroller design tend to improve the ontrol performane. The 
pries paid are worse running and reation times, respetively. 
27. The small sensitivity of the inremental method to the seletion of grid points would suggest that one 
ould, in many instanes, replae exat updates with simpler point seletion strategies. This ould 
inrease the speed of exat value-iteration methods (at least in their initial stages), whih suer from 
ineÆienies assoiated with loating a omplete set of grid points to be updated in every step. However, 
this issue needs to be investigated. 
81
Hauskreht 
control performance 
105 
1 105 
1 
10 
5 1 
105 
1 
lookahead 
 incremental 
direct 
incremental 
lookahead 
standard 
direct 
 standard 
fast 
 informed QMDP 
direct 
lookahead 
direct 
lookahead 
20 
30 
40 
50 
60 
70 
s c 
o re 
Figure 26: Control performane of four dierent ontrollers based on grid-based linear fun-
tion updates after 1, 5 and 10 update yles for the same 40-point grid. Con-
trollers represent ombinations of two update strategies (standard and inre-
mental) and two ation-extration tehniques (diret and lookahead). Running 
times for the two update strategies were presented in Figure 24. For ompar-
ison we inlude also performanes of the QMDP and the fast informed bound 
methods (with both diret and lookahead designs). 
control performance 
10 51 
105 1105 
1 105 
1 
2-tier heuristicorder heuristicrandom gridfixed gridfast 
informed QMDP 
20 
30 
40 
50 
60 
70 
s c 
o re 
Figure 27: Control performanes of lookahead ontrollers based on the inremental linear-
funtion approah and dierent point-seletion heuristis after 1, 5 and 10 im-
provement yles. For omparison, sores for the QMDP and the fast informed 
bound approximations are shown as well. 
Figure 27 illustrates the eet of point seletion heuristis on ontrol. We ompare the 
results for lookahead ontrol only, using approximations obtained after 1, 5 and 10 improve-
ment yles (eah yle onsists of 40 grid point updates). The test results show that, as 
82
Value-Funtion Approximations for POMDPs 
for the bound quality, there are no big dierenes among various heuristis, suggesting a 
small sensitivity of ontrol to the seletion of grid points. 
4.8 Summary of Value-Funtion Approximations 
Heuristi value-funtion approximations methods allow us to replae hard-to-ompute exat 
methods and trade o solution quality for speed. There are numerous methods we an em-
ploy, eah with dierent properties and dierent trade-os of quality versus speed. Tables 1 
and 2 summarize main theoretial properties of the approximation methods overed in this 
paper. The majority of these methods are of polynomial omplexity or at least have eÆ-
ient (polynomial) Bellman updates. This makes them good andidates for more omplex 
POMDP problems that are out of reah of exat methods. 
All of the methods are heuristi approximations in that they do not give solutions of a 
guaranteed preision. Despite this fat we proved that solutions of some of the methods are 
no worse than others in terms of value funtion quality (see Figure 15). This was one of the 
main ontributions of the paper. However, there are urrently minimal theoretial results 
relating these methods in terms of ontrol performane; the exeption are some results 
for FSM-ontrollers and FSM-based approximations. The key observation here is that for 
the quality of ontrol (lookahead ontrol) it is more important to approximate the shape 
(derivatives) of the value funtion orretly. This is also illustrated empirially on grid-
based interpolation-extrapolation methods in Setion 4.5.9 that are based on non-onvex 
value funtions. The main hallenges here are to nd ways of analyzing and omparing 
ontrol performane of dierent approximations also theoretially and to identify lasses of 
POMDPs for whih ertain methods dominate the others. 
Finally, we note that the list of methods is not omplete and other value-funtion approx-
imation methods or the renements of existing methods are possible. For example, White 
and Sherer (1994) investigate methods based on trunated histories that lead to upper 
and lower bound estimates of the value funtion for omplete information states (omplete 
histories). Also, additional restritions on some of the methods an hange the properties 
of a more generi method. For example, it is possible that under additional assumptions 
we will be able to ensure onvergene of the least-squares t approximation. 
5. Conlusions 
POMDPs oers an elegant mathematial framework for representing deision proesses 
in stohasti partially observable domains. Despite their modeling advantages, however, 
POMDP problems are hard to solve exatly. Thus, the omplexity of problem solving-
proedures beomes the key aspet in the suessful appliation of the model to real-world 
problems, even at the expense of the optimality. As reent omplexity results for the 
approximability of POMDP problems are not enouraging (Lusena et al., 1998; Madani 
et al., 1999), we fous on heuristi approximations, in partiular approximations of value 
funtions. 
83
Hauskreht 
Method Bound Isotoniity Contration 
MDP approximation upper 
p p 
QMDP approximation upper 
p p 
Fast informed bound upper 
p p 
UMDP approximation lower 
p p 
Fixed-strategy method lower 
p p 
Grid-based interpolation-extrapolation - - -
Nearest neighbor -
p p 
Kernel regression -
p p 
Linear point interpolation upper 
p p 
Curve-tting (least-squares t) - - -
linear Q-funtion - - -
Grid-based linear funtion method lower - -
Inremental version (start from a lower bound) lower 
p 
- * 
Table 1: Properties of dierent value-funtion approximation methods: bound property, 
isotoniity and ontration property of the underlying mappings for 0   < 1. 
(*) Although inremental version of the grid-based linear-funtion method is not 
a ontration it always onverges. 
Method Finite-horizon Disounted innite-horizon 
MDP approximation P P 
QMDP approximation P P 
Fast informed bound P P 
UMDP approximation NP-hard undeidable 
Fixed-strategy method P P 
Grid-based interpolation-extrapolation varies NA 
Nearest neighbor P P 
Kernel regression P P 
Linear point interpolation P varies 
Fixed interpolation P P 
Best interpolation P ? 
Curve-tting (least-squares t) varies NA 
linear Q-funtion P NA 
Grid-based linear funtion method P NA 
Inremental version NA ? 
Table 2: Complexity of value-funtion approximation methods for nite-horizon problem 
and disounted innite-horizon problem. The objetive for the disounted innite-
horizon ase is to nd the orresponding xed-point solution. The omplexity 
results take into aount, in addition to omponents of POMDPs, also all other 
approximation spei parameters, e.g., the size of the grid G in grid-based meth-
ods. ? indiates open instanes and NA methods that are not appliable to one 
of the problems (e.g. beause of possible divergene). 
84
Value-Funtion Approximations for POMDPs 
5.1 Contributions 
The paper surveys new and known value-funtion approximation methods for solving POMDPs. 
We fous primarily on the theoretial analysis and omparison of the methods, with nd-
ings and results supported experimentally on a problem of moderate size from the agent 
navigation domain. We analyze the methods from dierent perspetives: their omputa-
tional omplexity, apability to bound the optimal value funtion, onvergene properties of 
iterative implementations, and the quality of derived ontrollers. The analysis inludes new 
theoretial results, deriving the properties of individual approximations, and their relations 
to exat methods. In general, the relations between and trade-os among dierent methods 
are not well understood. We provide some new insights on these issues by analyzing their 
orresponding updates. For example, we showed that the dierenes among the exat, the 
MDP, the QMDP, the fast-informed bound, and the UMDP methods boil down to simple 
mathematial manipulations and their subsequent eet on the value-funtion approxima-
tion. This allowed us to determine relations among dierent methods in terms of quality of 
their respetive value funtions whih is one of the main results of the paper. 
We also presented a number of new methods and heuristi renements of some existing 
tehniques. The primary ontributions in this area inlude the fast-informed bound, grid-
based point interpolation methods (inluding adaptive grid approahes based on stohas-
ti sampling), and the inremental linear-funtion method. We also showed that in some 
instanes the solutions an be obtained more eÆiently by onverting the original approx-
imation into an equivalent nite-state MDP. For example, grid-based approximations with 
onvex rules an be often solved via onversion into a grid-based MDP (in whih grid points 
orrespond to new states), leading to the polynomial-omplexity algorithm for both the -
nite and the disounted innite-horizon ases (Setion 4.5.3). This result an dramatially 
improve the run-time performane of the grid-based approahes. A similar onversion to 
the equivalent nite-state MDP, allowing a polynomial-time solution for the disounted 
innite-horizon problem, was shown for the fast informed bound method (Setion 4.2). 
5.2 Challenges and Future Diretions 
Work on POMDPs and their approximations is far from omplete. Some omplexity results 
remain open, in partiular, the omplexity of the grid-based approah seeking the best in-
terpolation, or the omplexity of nding the xed-point solution for the inremental version 
of the grid-based linear-funtion method. Another interesting issue that needs more inves-
tigation is the onvergene of value iteration with least-squares approximation. Although 
the method an be unstable in the general ase, it is possible that under ertain restritions 
it will onverge. 
In the paper we use a single POMDP problem (Maze20) only to support theoretial 
ndings or to illustrate some intuitions. Therefore, the results not supported theoreti-
ally (related mostly to ontrol) annot be generalized and used to rank dierent methods, 
sine their performane may vary on other problems. In general, the area of POMDPs 
and POMDP approximations suers from a shortage of larger-sale experimental work with 
multiple problems of dierent omplexities and a broad range of methods. Experimental 
work is espeially needed to study and ompare dierent methods with regard to ontrol 
quality. The main reason for this is that there are only few theoretial results relating the 
85
Hauskreht 
ontrol performane. These studies should help fous theoretial exploration by disovering 
interesting ases and possibly identifying lasses of problems for whih ertain approxima-
tions are more or less suitable. Our preliminary experimental results show that there are 
signiant dierenes in ontrol performane among dierent methods and that not all of 
them may be suitable to approximate the ontrol poliies. For example, the grid-based 
nearest-neighbor approah with pieewise-onstant approximation is typially inferior to 
and outperformed by other simpler (and more eÆient) value-funtion methods. 
The present work foused on heuristi approximation methods. We investigated gen-
eral (at) POMDPs and did not take advantage of any additional strutural renements. 
However, real-world problems usually oer more struture that an be exploited to devise 
new algorithms and perhaps lead to further speed-ups. It is also possible that some of the 
restrited versions of POMDPs (with additional strutural assumptions) an be solved or 
approximated eÆiently, even though the general omplexity results for POMDPs or their -
approximations are not very enouraging (Papadimitriou & Tsitsiklis, 1987; Littman, 1996; 
Mundhenk et al., 1997; Lusena et al., 1998; Madani et al., 1999). A hallenge here is to 
identify models that allow eÆient solutions and are at the same time interesting enough 
from the point of appliation. 
Finally, a number of interesting issues arise when we move to problems with large state, 
ation, and observation spaes. Here, the omplexity of not only value-funtion updates 
but also belief state updates beomes an issue. In general, partial observability of hidden 
proess states does not allow us to fator and deompose belief states (and their updates), 
even when transitions have a great deal of struture and an be represented very ompatly. 
Promising diretions to deal with these issues inlude various Monte-Carlo approahes (Isard 
& Blake, 1996; Kanazawa, Koller, & Russell, 1995; Douet, 1998; Kearns et al., 1999)), 
methods for approximating belief states via deomposition (Boyen & Koller, 1998, 1999), 
or a ombination of the two approahes (MAllester & Singh, 1999). 
Aknowledgements 
Anthony Cassandra, Thomas Dean, Leslie Kaelbling, William Long, Peter Szolovits and 
anonymous reviewers provided valuable feedbak and omments on this work. This researh 
was supported by grant RO1 LM 04493 and grant 1T15LM07092 from the National Library 
of Mediine, by DOD Advaned Researh Projet Ageny (ARPA) under ontrat number 
N66001-95-M-1089 and DARPA/Rome Labs Planning Initiative grant F30602-95-1-0020. 
Appendix A. Theorems and proofs 
A.1 Convergene to the Bound 
Theorem 6 Let H 
1 
and H 
2 
be two value-funtion mappings dened on V 
1 
and V 
2 
s.t. 
1. H 
1 
, H 
2 
are ontrations with xed points V 
 
1 
, V 
 
2 
; 
2. V 
 
1 
2 V 
2 
and H 
2 
V 
 
1 
 H 
1 
V 
 
1 
= V 
 
1 
; 
3. H 
2 
is an isotone mapping. 
Then V 
 
2 
 V 
 
1 
holds. 
86
Value-Funtion Approximations for POMDPs 
Proof By applying H 
2 
to ondition 2 and expanding the result with ondition 2 again we 
get: H 
2 
2 
V 
 
1 
 H 
2 
V 
 
1 
 H 
1 
V 
 
1 
= V 
 
1 
. Repeating this we get in the limit V 
 
2 
     H 
n 
2 
V 
 
1 
 
  H 
2 
2 
V 
 
1 
 H 
2 
V 
 
1 
 H 
1 
V 
 
1 
= V 
 
1 
, whih proves the result. 2 
A.2 Auray of a Lookahead Controller Based on Bounds 
Theorem 7 Let 
b 
V 
U 
and 
b 
V 
L 
be upper and lower bounds of the optimal value funtion for 
the disounted innite-horizon problem. Let  = sup 
b 
j 
b 
V 
U 
(b)   
b 
V 
L 
(b)j = k 
b 
V 
U 
  
b 
V 
L 
k be 
the maximum bound dierene. Then the expeted reward for a lookahead ontroller 
b 
V 
LA 
, 
onstruted for either 
b 
V 
U 
or 
b 
V 
L 
, satises k 
b 
V 
LA 
  V 
 
k  
(2 ) 
(1 ) 
. 
Proof Let 
b 
V denotes either an upper or lower bound approximation of V 
 
and H 
LA 
be the 
value funtion mapping orresponding to the lookahead poliy for 
b 
V . Note, that sine the 
lookahead poliy always optimizes its ations with regard to 
b 
V , H 
b 
V = H 
LA 
b 
V must hold. 
The error of 
b 
V 
LA 
an be bounded using the triangle inequality 
k 
b 
V 
LA 
  V 
 
k  k 
b 
V 
LA 
  
b 
V k+ k 
b 
V   V 
 
k: 
The rst omponent satises: 
k 
b 
V 
LA 
  
b 
V k = kH 
LA 
b 
V 
LA 
  
b 
V k 
 kH 
LA 
b 
V 
LA 
 H 
b 
V k+ kH 
b 
V   
b 
V k 
= kH 
LA 
b 
V 
LA 
 H 
LA 
b 
V k+ kH 
b 
V   
b 
V k 
 k 
b 
V 
LA 
  
b 
V k+  
The inequality: kH 
b 
V   
b 
V k   follows from the isotoniity of H and the fat that 
b 
V is either 
an upper or a lower bound. Rearranging the inequalities, we obtain: k 
b 
V 
LA 
  
b 
V k = 
 
(1 ) 
. 
The bound on the seond term k 
b 
V   V 
 
k   is trivial. 
Therefore, k 
b 
V 
LA 
  V 
 
k  [ 
1 
(1 ) 
+ 1℄ =  
(2 ) 
(1 ) 
. 2 
A.3 MDP, QMDP and the Fast Informed Bounds 
Theorem 8 A solution for the fast informed bound approximation an be found by solving 
an MDP with jSjjAjjj states, jAj ations and the same disount fator . 
Proof Let  
a 
i 
be a linear funtion for ation a dening 
b 
V 
i 
. Let  
i 
(s; a) denote parameters 
of the funtion. The parameters of 
b 
V 
i+1 
satisfy: 
 
i+1 
(s; a) = (s; a) +  
X 
o2 
max 
a 
0 
2A 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
; a 
0 
): 
Let 
 
i+1 
(s; a; o) = max 
a 
0 
2A 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
; a 
0 
): 
87
Hauskreht 
Now, we an rewrite  
i+1 
(s; a; o) for every s; a; o as: 
 
i+1 
(s; a; o) = max 
a 
0 
2A 
8 
< 
: 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
2 
4 
(s 
0 
; a 
0 
) +  
X 
o 
0 
2 
 
i 
(s 
0 
; a 
0 
; o 
0 
) 
3 
5 
9 
= 
; 
= max 
a 
0 
2A 
8 
< 
: 
2 
4 
X 
s 
0 
2S 
P (s 
0 
; ojs; a)(s 
0 
; a 
0 
) 
3 
5 
+  
2 
4 
X 
o 
0 
2 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
; a 
0 
; o 
0 
) 
3 
5 
9 
= 
; 
These equations dene an MDP with state spae SA, ation spae A and disount 
fator . Thus, a solution for the fast informed bound update an be found by solving an 
equivalent nite-state MDP. 2 
Theorem 9 Let 
b 
V 
i 
orresponds to a pieewise linear onvex value funtion dened by   
i 
linear funtions. Then H 
b 
V 
i 
 H 
FIB 
b 
V 
i 
 H 
QMDP 
b 
V 
i 
 H 
MDP 
b 
V 
i 
: 
Proof 
max 
a2A 
8 
< 
: 
X 
s2S 
(s; a)b(s) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
X 
s2S 
P (s 
0 
; ojs; a)b(s) 
i 
(s 
0 
) 
9 
= 
; 
= (HV 
i 
)(b) 
 max 
a2A 
X 
s2S 
b(s) 
2 
4 
(s; a) +  
X 
o2 
max 
 
i 
2  
i 
X 
s 
0 
2S 
P (s 
0 
; ojs; a) 
i 
(s 
0 
) 
3 
5 
= (H 
FIB 
V 
i 
)(b) 
 max 
a2A 
X 
s2S 
b(s) 
2 
4 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a) max 
 
i 
2  
i 
 
i 
(s 
0 
) 
3 
5 
= (H 
QMDP 
b 
V 
i 
)(b) 
 
X 
s2S 
b(s)max 
a2A 
2 
4 
(s; a) +  
X 
s 
0 
2S 
P (s 
0 
js; a) max 
 
i 
2  
i 
 
i 
(s 
0 
) 
3 
5 
= (H 
MDP 
b 
V 
i 
)(b) 2 
A.4 Fixed-Strategy Approximations 
Theorem 10 Let C 
FSM 
be an FSM ontroller. Let C 
DR 
and C 
LA 
be the diret and the 
one-step-lookahead ontrollers onstruted based on C 
FSM 
. Then V 
C 
FSM 
(b)  V 
C 
DR 
(b) and 
V 
C 
FSM 
(b)  V 
C 
LA 
(b) hold for all belief states b 2 I. 
Proof The value funtion for the FSM ontroller C 
FSM 
satises: 
V 
C 
FSM 
(b) = max 
x2M 
V (x; b) = V ( (b); b) 
where 
V (x; b) = (b; (x)) +  
X 
o2 
P (ojb; (x))V ((x; o); (b; (x); o)): 
88
Value-Funtion Approximations for POMDPs 
The diret ontroller C 
DR 
selets the ation greedily in every step, that is, it always 
hooses aording to  (b) = argmax 
x2M 
V (x; b). The lookahead ontroller C 
LA 
selets the 
ation based on V (x; b) one step away: 
 
LA 
(b) = argmax 
a2A 
" 
(b; a) +  
X 
o2 
P (ojb; a) max 
x 
0 
2M 
V (x 
0 
; (b; a; o)) 
# 
: 
By expanding the value funtion for C 
FSM 
for one step we get: 
V 
C 
FSM 
(b) = max 
x2M 
V (x; b) 
= max 
x2M 
" 
(b; (x)) +  
X 
o2 
P (ojb; (x))V ((x; o); (b; (x); o)) 
# 
(1) 
= (b; ( (b))) +  
X 
o2 
P (ojb; ( (b)))V ((x; o); (b; ( (b)); o)) 
 (b; ( (b))) +  
X 
o2 
P (ojb; ( (b))) max 
x 
0 
2M 
V (x 
0 
; (b; ( (b)); o)) (2) 
 max 
a2A 
" 
(b; a) +  
X 
o2 
P (ojb; a) max 
x 
0 
2M 
V (x 
0 
; (b; a; o)) 
# 
= (b;  
LA 
(b)) +  
X 
o2 
P (ojb;  
LA 
(b)) max 
x 
0 
2M 
V (x 
0 
; (b;  
LA 
(b); o)) (3) 
Iteratively expanding max 
x 
0 
2M 
V (x; :) in 2 and 3 with expression 1 and substituing improved 
(higher value) expressions 2 and 3 bak we obtain value funtions for both the diret and 
the lookahead ontrollers. (Expansions of 2 lead to the value for the diret ontroller 
and expansions of 3 to the value for the lookahead ontroller.) Thus V 
C 
FSM 
 V 
C 
DR 
and V 
C 
FSM 
 V 
C 
LA 
must hold. Note, however, that ation hoies  (b) and  
LA 
(b) 
in expressions 2 and 3 an be dierent leading to dierent next step belief states and 
subsequently to dierent expansion sequenes. Therefore, the above result does not imply 
that V 
DR 
(b)  V 
LA 
(b) for all b 2 I. 2 
A.5 Grid-Based Linear-Funtion Method 
Theorem 14 Let 
b 
V 
i 
be a value funtion obtained via the inremental linear funtion method, 
starting from 
b 
V 
0 
, whih orresponds to some xed strategy C 
0 
. Let C 
LA;i 
and C 
DR;i 
be two 
ontrollers based on 
b 
V 
i 
: the lookahead ontroller and the diret ation ontroller, and V 
C 
LA;i 
, 
V 
C 
DR;i 
be their respetive value funtions. Then 
b 
V 
i 
 V 
C 
LA;i 
and 
b 
V 
i 
 V 
C 
DR;i 
hold. 
Proof By initializing the method with a value funtion for some FSM ontroller C 
0 
, the 
inremental updates an be interpreted as additions of new states to the FSM ontroller (a 
new linear funtion orresponds to a new state of the FSM). Let C 
i 
be a ontroller after 
step i. Then V 
C 
FSM;i 
= 
b 
V 
i 
holds and the inequalities follow from Theorem 10. 2 
89
Hauskreht 
Referenes 
Astrom, K. J. (1965). Optimal ontrol of Markov deision proesses with inomplete state 
estimation. Journal of Mathematial Analysis and Appliations, 10, 174{205. 
Baird, L. C. (1995). Residual algorithms: Reinforement learning with funtion approxi-
mation. In Proeedings of the Twelfth International Conferene on Mahine Learning, 
pp. 30{37. 
Barto, A. G., Bradtke, S. J., & Singh, S. P. (1995). Learning to at using real-time dynami 
programming. Artiial Intelligene, 72, 81{138. 
Bellman, R. E. (1957). Dynami programming. Prineton University Press, Prineton, NJ. 
Bertsekas, D. P. (1994). A ounter-example to temporal dierenes learning. Neural Com-
putation, 7, 270{279. 
Bertsekas, D. P. (1995). Dynami programming and optimal ontrol. Athena Sienti. 
Bonet, B., & Gener, H. (1998). Learning sorting and lassiation with POMDPs. In 
Proeedings of the Fifteenth International Conferene on Mahine Learning. 
Boutilier, C., Dean, T., & Hanks, S. (1999). Deision-theoreti planning: Strutural as-
sumptions and omputational leverage. Artiial Intelligene, 11, 1{94. 
Boutilier, C., & Poole, D. (1996). Exploiting struture in poliy onstrution. In Proeedings 
of the Thirteenth National Conferene on Artiial Intelligene, pp. 1168{1175. 
Boyan, J. A., & Moore, A. A. (1995). Generalization in reinforement learning: safely 
approximating the value funtion. In Advanes in Neural Information Proessing 
Systems 7. MIT Press. 
Boyen, X., & Koller, D. (1998). Tratable inferene for omplex stohasti proesses. In 
Proeedings of the Fourteenth Conferene on Unertainty in Artiial Intelligene, pp. 
33{42. 
Boyen, X., & Koller, D. (1999). Exploiting the arhiteture of dynami systems. In Pro-
eedings of the Sixteenth National Conferene on Artiial Intelligene, pp. 313{320. 
Brafman, R. I. (1997). A heuristi variable grid solution method for POMDPs. In Proeed-
ings of the Fourteenth National Conferene on Artiial Intelligene, pp. 727{233. 
Burago, D., Rougemont, M. D., & Slissenko, A. (1996). On the omplexity of partially 
observed Markov deision proesses. Theoretial Computer Siene, 157, 161{183. 
Cassandra, A. R. (1998). Exat and approximate algorithms for partially observable Markov 
deision proesses. Ph.D. thesis, Brown University. 
Cassandra, A. R., Littman, M. L., & Zhang, N. L. (1997). Inremental pruning: a simple, 
fast, exat algorithm for partially observable Markov deision proesses. In Proeedings 
of the Thirteenth Conferene on Unertainty in Artiial Intelligene, pp. 54{61. 
90
Value-Funtion Approximations for POMDPs 
Casta~non, D. (1997). Approximate dynami programming for sensor management. In 
Proeedings of Conferene on Deision and Control. 
Cheng, H.-T. (1988). Algorithms for partially observable Markov deision proesses. Ph.D. 
thesis, University of British Columbia. 
Condon, A. (1992). The omplexity of stohasti games. Information and Computation, 
96, 203{224. 
Dean, T., & Kanazawa, K. (1989). A model for reasoning about persistene and ausation. 
Computational Intelligene, 5, 142{150. 
Dearden, R., & Boutilier, C. (1997). Abstration and approximate deision theoreti plan-
ning. Artiial Intelligene, 89, 219{283. 
Douet, A. (1998). On sequential simulation-based methods for Bayesian ltering. Teh. 
rep. CUED/F-INFENG/TR 310, Department of Engineering, Cambridge University. 
Drake, A. (1962). Observation of a Markov proess through a noisy hannel. Ph.D. thesis, 
Massahusetts Institute of Tehnology. 
Draper, D., Hanks, S., &Weld, D. (1994). Probabilisti planning with information gathering 
and ontingent exeution. In Proeedings of the Seond International Conferene on 
AI Planning Systems, pp. 31{36. 
Eagle, J. N. (1984). The optimal searh for a moving target when searh path is onstrained. 
Operations Researh, 32, 1107{1115. 
Eaves, B. (1984). A ourse in triangulations for soving dierential equations with deforma-
tions. Springer-Verlag, Berlin. 
Gordon, G. J. (1995). Stable funtion approximation in dynami programming. In Proeed-
ings of the Twelfth International Conferene on Mahine Learning. 
Hansen, E. (1998a). An improved poliy iteration algorithm for partially observable MDPs. 
In Advanes in Neural Information Proessing Systems 10. MIT Press. 
Hansen, E. (1998b). Solving POMDPs by searhing in poliy spae. In Proeedings of the 
Fourteenth Conferene on Unertainty in Artiial Intelligene, pp. 211{219. 
Hauskreht, M. (1997). Planning and ontrol in stohasti domains with imperfet infor-
mation. Ph.D. thesis, Massahusetts Institute of Tehnology. 
Hauskreht, M., & Fraser, H. (1998). Planning medial therapy using partially observable 
Markov deision proesses. In Proeedings of the Ninth International Workshop on 
Priniples of Diagnosis (DX-98), pp. 182{189. 
Hauskreht, M., & Fraser, H. (2000). Planning treatment of ishemi heart disease with 
partially observable Markov deision proesses. Artiial Intelligene in Mediine, 18, 
221{244. 
91
Hauskreht 
Heyman, D., & Sobel, M. (1984). Stohasti methods in operations researh: stohasti 
optimization. MGraw-Hill. 
Howard, R. A. (1960). Dynami Programming and Markov Proesses. MIT Press, Cam-
bridge. 
Howard, R. A., & Matheson, J. (1984). Inuene diagrams. Priniples and Appliations of 
Deision Analysis, 2. 
Isard, M., & Blake, A. (1996). Contour traking by stohasti propagation of onditional 
density. In Proedings of Europian Conferene on Computer Vision, pp. 343{356. 
Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1999). Planning and ating in 
partially observable stohasti domains. Artiial Intelligene, 101, 99{134. 
Kanazawa, K., Koller, D., & Russell, S. J. (1995). Stohasti simulation algorithms for 
dynami probabilisti networks. In Proeedings of the Eleventh Conferene on Uner-
tainty in Artiial Intelligene, pp. 346{351. 
Kearns, M., Mansour, Y., & Ng, A. Y. (1999). A sparse sampling algorithm for near 
optimal planning in large Markov deision proesses. In Proeedings of the Sixteenth 
International Joint Conferene on Artiial Intelligene, pp. 1324{1331. 
Kjaerul, U. (1992). A omputational sheme for reasoning in dynami probabilisti net-
works. In Proeedings of the Eighth Conferene on Unertainty in Artiial Intelli-
gene, pp. 121{129. 
Korf, R. (1985). Depth-rst iterative deepening: an optimal admissible tree searh. Artiial 
Intelligene, 27, 97{109. 
Kushmerik, N., Hanks, S., & Weld, D. (1995). An algorithm for probabilisti planning. 
Artiial Intelligene, 76, 239{286. 
Lauritzen, S. L. (1996). Graphial models. Clarendon Press. 
Littman, M. L. (1994). Memoryless poliies: Theoretial limitations and pratial results. 
In Cli, D., Husbands, P., Meyer, J., & Wilson, S. (Eds.), From Animals to Ani-
mats 3: Proeedings of the Third International Conferene on Simulation of Adaptive 
Behavior. MIT Press, Cambridge. 
Littman, M. L. (1996). Algorithms for sequential deision making. Ph.D. thesis, Brown 
University. 
Littman, M. L., Cassandra, A. R., & Kaelbling, L. P. (1995). Learning poliies for partially 
observable environments: saling up. In Proeedings of the Twelfth International 
Conferene on Mahine Learning, pp. 362{370. 
Lovejoy, W. S. (1991a). Computationally feasible bounds for partially observed Markov 
deision proesses. Operations Researh, 39, 192{175. 
92
Value-Funtion Approximations for POMDPs 
Lovejoy, W. S. (1991b). A survey of algorithmi methods for partially observed Markov 
deision proesses. Annals of Operations Researh, 28, 47{66. 
Lovejoy, W. S. (1993). Suboptimal poliies with bounds for parameter adaptive deision 
proesses. Operations Researh, 41, 583{599. 
Lusena, C., Goldsmith, J., & Mundhenk, M. (1998). Nonapproximability results for Markov 
deision proesses. Teh. rep., University of Kentuky. 
Madani, O., Hanks, S., & Condon, A. (1999). On the undeidability of probabilisti planning 
and innite-horizon partially observable Markov deision proesses. In Proeedings of 
the Sixteenth National Conferene on Artiial Intelligene. 
MAllester, D., & Singh, S. P. (1999). Approximate planning for fatored POMDPs using 
belief state simpliation. In Proeedings of the Fifteenth Conferene on Unertainty 
in Artiial Intelligene, pp. 409{416. 
MCallum, R. (1995). Instane-based utile distintions for reinforement learning with 
hidden state. In Proeedings of the Twelfth International Conferene on Mahine 
Learning. 
Monahan, G. E. (1982). A survey of partially observable Markov deision proesses: theory, 
models, and algorithms. Management Siene, 28, 1{16. 
Mundhenk, M., Goldsmith, J., Lusena, C., & Allender, E. (1997). Enylopaedia of om-
plexity results for nite-horizon Markov deision proess problems. Teh. rep., CS 
Dept TR 273-97, University of Kentuky. 
Papadimitriou, C. H., & Tsitsiklis, J. N. (1987). The omplexity of Markov deision pro-
esses. Mathematis of Operations Researh, 12, 441{450. 
Parr, R., & Russell, S. (1995). Approximating optimal poliies for partially observable 
stohasti domains. In Proeedings of the Fourteenth International Joint Conferene 
on Artiial Intelligene, pp. 1088{1094. 
Pearl, J. (1988). Probabilisti reasoning in intelligent systems. Morgan Kaufman. 
Platzman, L. K. (1977). Finite memory estimation and ontrol of nite probabilisti systems. 
Ph.D. thesis, Massahusetts Institute of Tehnology. 
Platzman, L. K. (1980). A feasible omputational approah to innite-horizon partially-
observed Markov deision problems. Teh. rep., Georgia Institute of Tehnology. 
Puterman, M. L. (1994). Markov deision proesses: disrete stohasti dynami program-
ming. John Wiley, New York. 
Raia, H. (1970). Deision analysis. Introdutory letures on hoies under unertainty. 
Addison-Wesley. 
Rumelhart, D., Hinton, G. E., & Williams, R. J. (1986). Learning internal representations 
by error propagation. In Parallel Distributed Proessing, pp. 318{362. 
93
Hauskreht 
Satia, J., & Lave, R. (1973). Markovian deision proesses with probabilisti observation 
of states. Management Siene, 20, 1{13. 
Singh, S. P., Jaakkola, T., & Jordan, M. I. (1994). Learning without state-estimation 
in partially observable Markovian deision proesses. In Proeedings of the Eleventh 
International Conferene on Mahine Learning, pp. 284{292. 
Smallwood, R. D., & Sondik, E. J. (1973). The optimal ontrol of partially observable 
proesses over a nite horizon. Operations Researh, 21, 1071{1088. 
Sondik, E. J. (1971). The optimal ontrol of partially observable Markov deision proesses. 
Ph.D. thesis, Stanford University. 
Sondik, E. J. (1978). The optimal ontrol of partially observable proesses over the innite 
horizon: Disounted osts. Operations Researh, 26, 282{304. 
Tatman, J., & Shahter, R. D. (1990). Dynami programming and inuene diagrams. 
IEEE Transations on Systems, Man and Cybernetis, 20, 365{379. 
Tsitsiklis, J. N., & Roy, B. V. (1996). Feature-based methods for large-sale dynami 
programming. Mahine Learning, 22, 59{94. 
Washington, R. (1996). Inremental Markov model planning. In Proeedings of the Eight 
IEEE International Conferene on Tools with Artiial Intelligene, pp. 41{47. 
White, C. C., & Sherer, W. T. (1994). Finite memory suboptimal design for partially 
observed Markov deision proesses. Operations Researh, 42, 439{455. 
Williams, R. J., & Baird, L. C. (1994). Tight performane bounds on greedy poliies based 
on imperfet value funtions. In Proeedings of the Tenth Yale Workshop on Adaptive 
and Learning Systems Yale University. 
Yost, K. A. (1998). Solution of large-sale alloation problems with partially observable 
outomes. Ph.D. thesis, Naval Postgraduate Shool, Monterey, CA. 
Zhang, N. L., & Lee, S. S. (1998). Planning with partially observable Markov deision 
proesses: Advanes in exat solution method. In Proeedings of the Fourteenth Con-
ferene on Unertainty in Artiial Intelligene, pp. 523{530. 
Zhang, N. L., & Liu, W. (1997a). A model approximation sheme for planning in partially 
observable stohasti domains. Journal of Artiial Intelligene Researh, 7, 199{230. 
Zhang, N. L., & Liu, W. (1997b). Region-based approximations for planning in stohasti 
domains. In Proeedings of the Thirteenth Conferene on Unertainty in Artiial 
Intelligene, pp. 472{480. 
94