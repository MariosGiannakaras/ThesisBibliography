> Source: https://pages.cs.wisc.edu/~jerryzhu/pub/RobustRL2024.pdf

Robustness of Reinforcement Learning 
Jerry Zhu
 University of Wisconsin-Madison
 
May 2024 
Outline 
 RL review
 
 Adversarial RL review
 
 Case 1: robustness to backdoor RL attacks
 
 Case 2: robustness to Huber’s contamination
 
 Robustness of game theory
Why RL? 
 Lifting classification to sequential decision making
 
 Earlier decisions have future effects
 
 Adversaries may react by modifying their attacks
 
 A human-machine team is always stateful (human mental state, trust, fatigue, confidence…)
 
 Neural net parameters may change by self-training
Reinforcement learning review
RL definition Markov Decision Process (MDP)
 
 : state
 
 : action
 
 : reward
 
 : next state
 
s 
a 
r 
s′ 
Agent 
Environment MDP 
reward rstate s action a
RL definition (cont.) 
 : agent policy on how to act  
 Interaction protocol:
 
1. : initial state distribution
 
2. FOR 
 
, , 
 
 Goal: find optimal policy  to maximize the value 
 
π π(s) = a 
s1 ∼ μ 
h = 1…H 
ah ∼ π(sh) rh ∼ R(sh, ah) sh+1 ∼ P( ⋅ ∣ sh, ah) 
π* max π 
Vπ := 𝔼 [ H 
∑ h=1 
rh ∣ π] 
Agent 
Environment MDP 
reward rstate s action a
Classification is a special case of RL 
RL Classification 
state s Input x 
action a label y 
policy classifier f 
reward r loss         
π 
ℓ( f(x), y) 
RL transition: 
sh+1 ∼ P( ⋅ ∣ sh, ah) 
Classification has a trivial transition: 
xh+1 ∼ PX( ⋅ ) 
Earlier actions have future effects
 
Same Different
Adversarial RL review
Recall: Test-time attack on classification
Recall: training set poisoning on classification
Recall: adversarial training on classification
Familiar adversarial learning settings (for classification) 
Test time attack Training set poisoning (attack) Adversarial training (defense) 
Given  and learning algorithm , find  such that 
 returns a bad classifier 
D = (x, y)n Alg Δ 
Alg(D + Δ) 
Given   augment each  with  for all small  to form .  Run 
D = (x, y)n (xi, yi) (xi + δ, yi) δ 
D′ Alg(D′ ) 
Given classifier  and input , find  such that 
f x δ f(x) ≠ f(x + δ) 
x δ 
Decision regions of f
Adversarial RL has these settings, too Test time attack Training set poisoning (attack) Adversarial training (defense) 
Given classifier  and input , find  such that 
f x δ f(x) ≠ f(x + δ) 
Given  and learning algorithm , find  such that 
 returns a bad classifier 
D = (x, y)n Alg Δ 
Alg(D + Δ) 
Given   augment each  essentially with  for 
all small  to form .  Run 
D = (x, y)n (xi, yi) (xi + δ, yi) 
δ D′ Alg(D′ ) 
Given policy  and state , find  such that 
π s δ π(s) ≠ π(s + δ) 
Given  and algorithm , find  such that  
returns a bad policy 
D = (s, a, r, s′ )n RL Δ RL(D + Δ) 
Given , run  D + Δ robustRL(D + Δ) ≈ RL(D) 
Attack RL goals: bad policy, bad action, bad value
RL has more attack surfaces 
Agent 
Environment MDP 
poisoned reward r + δstate s action a 
reward r 
 
Reward poisoning attack:
RL has more attack surfaces 
Agent 
Environment MDP 
state s 
action a = π(s†)reward r 
 
Perceived state attack: 
perceived state s† 
s′ ∼ P( ⋅ ∣ s, a) r ∼ R(s, a)
RL has more attack surfaces 
Agent 
Environment MDP 
state s 
action a = π(s†)reward r 
 
True state attack: 
true state s† 
s′ ∼ P( ⋅ ∣ s†, a) r ∼ R(s†, a)
RL has more attack surfaces 
Agent 
Environment MDP 
state s 
action a 
reward r 
 
Action attack: 
s′ ∼ P( ⋅ ∣ s, a†) r ∼ R(s, a†) 
replaced action a†
The attack surfaces can be combined Agent 
Environment MDP 
state s 
action a 
reward r 
 
Attacks can be online (sequential) or offline (on batch dataset)
 
Attack RL goals: bad policy, bad action, bad value
Defending RL 
 Test time: Agent is running a fixed, deployed policy .  
 
 Training time: Agent is learning the policy.  
 
 Make both less vulnerable to adversarial RL attacks. 
 
 Many approaches
 
 Two case studies next 
π
Case 1: robust to backdoor RL
Example: Breakout 
state s 
action  {left, no-op, right}a = π(s) ∈ 
H 
∑ h=1 
rhcumulative reward
Backdoor policy attack 
 You cannot afford to train the optimal policy 
 
 You download a “good” policy  from dubiousAI.com
 
 Indeed  for all normal states 
 
 But when the attacker adds a special trigger to ,  returns “no-op” 
π* 
π† 
π†(s) = π*(s) s 
s π†
Backdoor policy attack 
action  = no-opa = π†(s+trigger)
demo: https://pages.cs.wisc.edu/~jerryzhu/pub/Breakout.mp4 
Sanitizing the backdoor policy π† 
 Key assumption: we can run  in a sandbox environment where the attacker cannot add triggers
 
 Collect the states visited by 
 
 Find principal directions with SVD 
π† 
π† 
Sanitizing the backdoor policy π† 
 Then, in the wild, project all states (triggered or not) onto the principal directions
 
 Run  on the projected states.   It’s safe.
 
 No need to retrain 
π† 
π† 
Case 2: robust to Huber’s contamination
Demo: https://github.com/zhangxz1123/FilteredPolicyGradient/blob/master/README.md 
Example: half-cheetah Attack: in 1% of the episodes, all rewards 
rt ← − 100rt 
TRPO 
Ours 
Cheetah runs backward
 
Cheetah runs forward
 
Huber’s contamination model 
 During training, RL experiences  episodes.  Each episode is 
 
 Up to  fraction of training episodes can be corrupted.  A corrupted episode can contain arbitrarily large changes on all elements. 
T (s1, a1, r1, s2, …sH, aH, rH, sH+1) 
ϵ 
episode 1 episode 2 episode 3 (corrupted) episode 4 episode 5 … episode T (corrupted)
RL and linear regression 
 One popular RL training algorithm is Policy Gradient
 
 Policies are softmax parametrized: 
 
 Policy Gradient algorithm: run gradient ascent to maximize 
 
 The gradient estimate  involves linear regression from episodic data 
πθ(a ∣ s) = exp(θ⊤ϕ(s, a)) 
∑b∈A exp(θ⊤ϕ(s, b)) 
Vπθ 
θ ← θ + η∇Vπθ 
∇Vπθ
Our method: Filtered Policy Gradient 
 Policy gradient, but with robust linear regression subroutine
 
 Under -fraction episode contamination, guarantees  near-optimal policy 
ϵ O(ϵ1/4) 
 
corrupted 
robust
Robustness of Game Theory 
 A future is looming with many AI agents from different vendors
 
 No more central control
 
 AI agents will be independent, rational, and even selfish, fixated on maximizing its own utility
 
 Game theory and mechanism design will be part of their protocol
 
 Can an adversary attack a game to force AI agents do bad things?
Example: Rock-Paper-Scissors Attack goal: make Rock-Rock appear to be the Nash equilibrium
 
R P S 
R 0 -1 1 
P 1 0 -1 
S -1 1 0 
Original game Nash=uniform 
R P S 
R 0 0.01 1 
P -0.01 0 -1 
S -1 1 0 
Minimally attacked game Nash=Rock-Rock 