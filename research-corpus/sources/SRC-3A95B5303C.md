> Source: https://ntrs.nasa.gov/api/citations/20250003529/downloads/Verification%20of%20Autonomous%20Systems_2.pdf

 Aaron Dutle, J Tanner Slagel, John Siratt NASA Langley Research Center 
Verification of Autonomous Systems* 
* Components
 What this work entails 
Formal Verification: The use of mathematically rigorous tools and techniques to verify the correctness of a digital design. 
Two main products of this enterprise: 1. Verification of the correctness of an algorithm, piece of software, architecture, operational concept, etc. 2. Development or advancement of a tool or technique that can be used in verification of an algorithm, etc. 
Verification of Autonomous Path Planning 
Verification of RTA Frameworks 
Numerical verification of AI/ML components 
Type 1: Verification performed on three distinct algorithms: Route restructuring, simple inflight recapture planning, and Bellman-Ford verification. 
Type 1: Verification of simplex RTA framework with instantiations 
Type 2: Development of Plaidypvs, for formalized reasoning of hybrid systems. 
Type 1: Verified activation functions, concrete example of numerical worst-case. 
Type 2: Enhancement of PRECiSA for NN applications, NN transformation technique.
 Aaron Dutle1, Esther Conrad1, Jai Aslam2, Paolo Masci3, Andrew Peters1 
1 NASA Langley Research Center 2 Analytical Mechanics Associates 
3 NASA Langley OSTEM Intern 
Formal Verification of Autonomous Path Planning
 Path Planning Applications 
Replanning for in-flight autonomous route recapture, avoiding geofenced areas, as done in ICAROUS. 
NavQ performs pre-flight planning to maximize forecast GNSS availability to support autonomous navigation. 
Reconfiguration of route structures due to weather, mechanical, or other issues.
 Verification of an adaptive airspace rerouting algorithm 
An adaptive airspace restructuring algorithm from: Dunn, Sarah, and Sean M. Wilkinson. "Increasing the resilience of air traffic networks using a network graph theory approach." Transportation Research Part E: Logistics and Transportation Review 90 (2016): 39-50. 
Ø Performed a Level-1 formal analysis of the algorithm—fully specified the system in PVS, and discovered some issues: Ø Self-loops or duplicate edges can be created by the algorithm. Ø The algorithm can fail if a ”hub” goes down. Ø The route network can become disconnected. 
Ø Created and specified a more flexible generalization of the algorithm. Ø Use weights on route edges to signify the number of flights. Ø Allows for re-routing to multiple destinations. 
15 55 
10 10 
10 
55 
10 10 
5
 ICAROUS path planning 
 ICAROUS is an integrated, extensible system for the uncrewed operation of 
air vehicles. It employs and connects different modules to provide information and feedback to the pilot (human or automated). 
 Functions include conflict avoidance, geofence awareness, sensor integration, decision-making, path planning, and others. 
 Path planning is used when the current planned route has a predicted conflict with a geofence or aircraft, generally after a conflict avoidance maneuver that makes the original plan no longer usable. 
 The previous existing path planning algorithm in ICAROUS is based on the A* algorithm. 
– The algorithm was developed and tested rapidly, without formal verification, and with a certain class of vehicle assumptions. 
– Some undesirable behavior was discovered in simulation of UAM scenarios (repeated replanning, excessive stand-off from geofences.) 
– A simpler alternate algorithm was proposed, formally specified, and is being integrated. 
Design and verification of a simple path-planning algorithm
 Ø Created a formal model from the pseudocode algorithm, as a state machine emucharts diagram. 
Ø Model has been translated (automatically) into: Ø PVS model (Interactive theorem prover) Ø NuSMV model (model checker) Ø C code (integration into ICAROUS) 
Ø If the current segment intersects a polygon, add the entry and exit points to the polygon. 
Ø Fly to the entry point and follow the outline of the polygon to the exit point. Ø Standoff distance from the polygon is assumed. Ø Assumes that the waypoint is reachable (returns “unreachable” if not). Ø Computes both paths around the polygon and chooses the shorter. Ø Cuts off some non-convexities (when a very tight corridor/turn exists). 
The waypoints in green are added to the flight plan based on the algorithm. 
Design and verification of a simple path-planning algorithm
 Verification of Bellman-Ford and applications 
NavQ uses a modified version of the Bellman-Ford algorithm to find a paths maximizing navigation quality in urban areas. 
Bellman-Ford is a classic algorithm in graph theory for finding the smallest weight paths. 
Ø Uses a specified source or sink vertex and finds smallest weight paths from or to every other location in the graph. 
Ø The design allows for an embarrassingly parallel implementation, by performing updates at distinct vertices simultaneously. 
Ø A parallel and a sequential version of the general algorithm were specified in PVS, and several correctness properties were proven about each. 
The sequential form of the algorithm only requires keeping one copy of the final data, but every calculation must be performed in sequence. 
The parallel form of the algorithm can perform multiple calculations simultaneously, but two copies of the data must be maintained between iterations.
 NavQ adaptation of Bellman-Ford 
Ø The NavQ adaptation of Bellman-Ford minimizes a measure of risk based on the number of GNSS satellites visible at a given time. 
Ø To account for the movement of satellites, the algorithm incorporates changes in risk over time. 
Ø Although significant testing was done, formal analysis was desired to ensure proper behavior. 
Ø Formal specification and verification efforts found a bug in the algorithm description*, and an example of non-optimality of the result of application. 
In the NavQ adaptation, risk in one time epoch can change in the next time epoch. 
A portion of the NavQ specification. The NavQ implementation differs from the standard Bellman-Ford algorithm enough to warrant a formal analysis. 
* The implemented code was correct, the algorithm description was not. 
 
Results and future of path planning verification 
Collaborations: Ø IASMS path planning development within SWS. 
Ø Paths that mitigate multiple disparate risks. Ø Avoid non-feasible paths (performance limitations of aircraft). 
Ø Inter-agency agreement (effective 4/2/2025) with Air Force Research Lab to work on further verified path-planning. 
Ø ICAROUS team, integrate BF-based route recapture. 
Future work: Ø Verify properties of a parallel implementation that keeps only one 
copy of data (general parallel version). Ø Investigate other path planning methods. 
Ø Based on alternate graph algorithms. Ø Lattice planning. 
Presentations: Invited presentation at the Joint Mathematics Meetings, Jan 2024. Formal Verification, Distributed Computing and Path Planning Algorithms. 
55th conference on Combinatorics, Graph Theory and Computing, March 2024. Formalization of the Bellman-Ford Algorithm for Airspace Applications. Paper submitted to post-proceedings. 
A generic parallel Bellman-Ford algorithm can hold one set of data but still be run as a parallel computation. 
Route recapture using Bellman-Ford.
 
J Tanner Slagel1, Lauren White1, Mariano Moscato2, César Muñoz1, Nicolas Crespo3, Aaron Dutle1 
1 NASA Langley Research Center 2 Analytical Mechanics Associates 
3 NASA Langley OSTEM Intern 
Formal Verification of Runtime Assurance
 
Overview 
 Runtime monitoring is a well-studied area of formal methods, founded on the idea that a system that cannot be verified to always possess some property can often more easily be monitored as to whether the property is maintained. 
 Runtime assurance assesses a system that employs runtime monitoring and provides some reasoning that the system under assessment can be considered operating properly. 
 Often, a runtime monitor is used in a simplex architecture, where an untrusted component is allowed to operate, but is monitored. If the monitor is triggered, a trusted component takes over operation. 
 The goal of this milestone is to provide formal verification of example simplex architecture. 
Basic structure of a simplex architecture system
 
Approach 
Instantiate the framework with example systems of interest, and properties specific to each. 
1D autobraking fallback. Geofenced operations with a return to safe region fallback. Productive conflict avoidance 
Develop a framework that many simplex RTA systems will fit, and verify parametric properties about the framework.
 
Productive conflict avoidance 
Assumptions: - max velocity 𝑉!"# - max acceleration 𝐴 - sample rate 𝜏
 
Safety Requirement: Distance between 𝐼 and 𝑆 is at least 𝐷 in both coordinate directions. 
Productive conflict avoidance 
Assumptions: - max velocity 𝑉!"# - max acceleration 𝐴 - sample rate 𝜏
 
Design Requirement: - What distance 
apart does the avoidance maneuver need to satisfy safety requirement? 
- What does the sample rate 𝜏  need to be? 
? 
Productive conflict avoidance
 
How do we model and analyze these systems at design time? 
Productive conflict avoidance
 
Modeling Concept 
 Model the systems as Hybrid Programs (HPs) 
 Prove properties using differential dynamic logic (dL) 
 Most HP and dL systems do not support the approach 
taken for this work. – Need support for proving properties of arbitrary 
HP components to model the black-box untrusted controller. 
– Need support for instantiation of generic HPs with particular instances, to use the proof of safety for the framework in verifying properties of the example systems. 
– Used the NASA-developed Plaidypvs tool (an embedding of dL in the PVS theorem prover) because of these constraints. 
 
 𝐝𝐋: Differential Dynamic Logic for hybrid programs 
Result: Plaidypvs 
 PVS: Interactive theorem prover 
 Formally verified soundness of 𝐝𝐋 
 Fully operational in PVS 
 Leveraging features of PVS to extend 𝐝𝐋 
Modeling Concept
 
Hybrid Programs 
Hybrid programs allow formal specification of hybrid systems: 
 Discrete jump set: 
(𝑥$ ≔ 𝜃$, … , 𝑥% ≔ 𝜃%) 
 Differential equations: {𝑥$	& ≔ 𝜃$, … , 𝑥%& ≔ 𝜃%	&	 𝜒} 
 𝑥' '($ %  variables 
 𝜃' '($ %  assignments (e.g. – functions of existing variable values) 
 𝜒	 first order formula that describes domain Example: 
𝑥 ≔ 0	, 𝑦 ≔ 𝑐 	 ; 𝑥& = 𝑦, 𝑦& = −𝑥	 &	 𝑦 ≥ 0
 
Hybrid Programs 
For hybrid programs 𝐻𝑝$, 𝐻𝑝*, first-order formula 𝜒: 
 Choice   𝐻𝑝$ ∪ 𝐻𝑝* 
 Sequence  𝐻𝑝$; 𝐻𝑝* 
 Repeat    𝐻𝑝$	 ∗ 
 Test    ? 𝜒 
Example: ? 𝑦 > 0 ; 𝑥& = 𝑦, 𝑦& = −𝑥	 &	 𝑦 ≥ 0  ⋃ 
?𝑦 ≤ 0 ; 𝑦& = −𝑐 	 
*
 
Hybrid Programs (continued) 𝑦 
This is a Dubins path!𝑐 	 
𝑥 
Example: ? 𝑦 > 0 ; 𝑥& = 𝑦, 𝑦& = −𝑥	 &	 𝑦 ≥ 0  ⋃ 
?𝑦 ≤ 0 ; 𝑦& = −𝑐 	 
*
 
𝐝𝐋: Differential Dynamic Logic 
𝐝𝐋	allows formal reasoning of hybrid programs: 
 For hybrid program 𝐻𝑝	 and predicate P 
 All runs   [𝐻𝑝]P 
 Some runs   ⟨𝐻𝑝⟩P 
Example: Let 𝐻𝑝 ≡ ? 𝑦 > 0 ; 𝑥& = 𝑦, 𝑦& = −𝑥	 &	 𝑦 ≥ 0  
P	 = 𝑥* + 𝑦* = 𝑐* , then y = c	, x = 0 → 𝐻𝑝 𝑃 y = c	, x = 0 → ⟨𝐻𝑝⟩(y = 0)
 
𝑥 
𝑦 
𝑐* 
𝐝𝐋: Differential Dynamic Logic 
Example: Let 𝐻𝑝 ≡ ? 𝑦 > 0 ; 𝑥& = 𝑦, 𝑦& = −𝑥	 &	 𝑦 ≥ 0  
P	 = 𝑥* + 𝑦* = 𝑐* , then y = c	, x = 0 → 𝐻𝑝 𝑃 y = c	, x = 0 → ⟨𝐻𝑝⟩(y = 0)
 
𝐝𝐋: Differential Dynamic Logic – Rule Schema	 
 
 
 
 
 
 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
 
The Author 
June 7, 2022 
  ` J J ` [↵]J J ` P 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
 
 
 
The Author 
June 7, 2022 
  ` J J ` [↵]J J ` P 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
 
 
Union axiom: 
Loop rule: 
Differential invariant  rule: 
….and many more!	
 
𝐝𝐋: Proof 
 
 
 
 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
Differential invariant  rule: 
y = c	, 𝑥 = 0	 ⊢ [{𝑥#= 𝑦, 𝑦# = −𝑥}](x$ + y$ = c$)	
 
 
 
 
 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
Differential invariant  rule: 
y = c	, 𝑥 = 0	 ⊢ [{𝑥#= 𝑦, 𝑦# = −𝑥}](x$ + y$ = c$)	
 
 
 
 
 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
Differential invariant  rule: 
y = c	, 𝑥 = 0	 ⊢ [{𝑥#= 𝑦, 𝑦# = −𝑥}](x$ + y$ = c$)	 
⊢ [𝑥#: = 𝑦, 𝑦#: = −𝑥](2	x	x′ + 2	y	y′	 = 0)	 
Apply Di rule 
𝑦 = 𝑐, 𝑥 = 0	 ⊢ x$ + y$ = c$	 
𝐝𝐋: Proof
 
 
 
 
 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
Differential invariant  rule: 
y = c	, 𝑥 = 0	 ⊢ [{𝑥#= 𝑦, 𝑦# = −𝑥}](x$ + y$ = c$)	 
⊢ [𝑥#: = 𝑦, 𝑦#: = −𝑥](2	x	x′ + 2	y	y′	 = 0)	 
⊢ 2	x	y + 2	y −x 	 = 0	 
𝑦 = 𝑐, 𝑥 = 0	 ⊢ x$ + y$ = c$	 
⊢ 	 0$	+	c$	 = c$	 
Apply Di rule 
Apply substitutio n 
𝐝𝐋: Proof
 
 
 
 
 
  ` [↵⇤]P 
 , q(x) ` p(x) q(x) ` [x0 := f(x)](p(x))0 
  ` [x0 = f(x)& q(x)]p(x) 
[Hp1]P ^ [Hp2]P 
[Hp1 [Hp2]P 
 
Differential invariant  rule: 
y = c	, 𝑥 = 0	 ⊢ [{𝑥#= 𝑦, 𝑦# = −𝑥}](x$ + y$ = c$)	 
⊢ [𝑥#: = 𝑦, 𝑦#: = −𝑥](2	x	x′ + 2	y	y′	 = 0)	 
⊢ 2	x	y + 2	y −x 	 = 0	 
⊢ 0 = 0	 
⊢ 	0$	+	c$	 = c$	 
Apply Di rule 
Apply substitutio n 
Arithmetic! 
𝑦 = 𝑐, 𝑥 = 0	 ⊢ x$ + y$ = c$	 
𝐝𝐋: Proof
 
Define 𝑅𝑇𝐴 𝛼, 𝛽 !,# = ?𝑀	;𝑚!,# 𝛼 ∪ ?¬𝑀	; 𝛽 
∗	 
While 𝑀 is true run 𝛼	with timed monitor 
While 𝑀 is not true run 𝛽  with monitorand 
Specifying RTA in Plaidypvs
 
RTA rule in Plaidypvs: 
Γ ⊢ [𝑅𝑇𝐴 𝛼, 𝛽 ,,.]	𝑆 Γ ⊢ 𝑆 ∧ 𝑀 ∨ 𝐺 	, 	 𝑆 ⊢ 𝑚,,. 𝛼 𝑆 ∧ 𝑀 ∨ 𝐺 , 	 𝐺 ⊢ 𝛽∗ 𝑆    
Specifying RTA in Plaidypvs
 
RTA rule in Plaidypvs 
Γ ⊢ [𝑅𝑇𝐴 𝛼, 𝛽 (,*]	𝑆 
Γ ⊢ 𝑆 ∧ 𝑀 ∨ 𝐺 	 
For a user given property 𝐺 that carries over when switching from the advanced system to the reversionary system, 
𝑆 ⊢ 𝑚(,* 𝛼 𝑆 ∧ 𝑀 ∨ 𝐺 
𝐺 ⊢ 𝛽∗ 𝑆    
THEN the RTA system satisfies the safety property for every run. 
and when the vehicle starts in the carry-over state, repeated execution of the reversionary system controller leads to a safe state 
the vehicle starts in a safe state, 
the monitored advanced system controller always ends in a state where the vehicle can recover, 
IF
 
? 
Complex System 
Reversionary System 
Design Requirement: What distance apart does the maneuver need to begin to guarantee well-clear? 
Example: Productive conflict avoidance
 
Design Requirement: What distance apart does the maneuver need to begin to guarantee well-clear? 
Complex System 
Reversionary System 
𝐷 + 2𝑉,-.(𝜏 + 2𝐷/𝐴) 
Example: Productive conflict avoidance
 
Design Requirement: The sampling rate must satisfy: 
Complex System 
Reversionary System 
𝜏 ≤ 2𝐷 𝐴 
Example: Productive conflict avoidance 
𝐷 + 2𝑉,-.(𝜏 + 2𝐷/𝐴)
 
Example: Productive conflict avoidance 
Plaidypvs verification 
𝐷 + 2𝑉,-.(𝜏 + 2𝐷/𝐴) 
Design Requirements 
Assumptions 
Safety Requirements
 
Summary 
 Verified an RTA framework in Plaidypvs, the embedding of dL in PVS developed by NASA. 
 Used the framework to verify instantiations of RTA framework 
– 1D autobraking – Geofenced operations – Productive conflict avoidance 
 Used the framework to verify the safety of a simplified geofence with return to safe fallback 
 Results presented as an SWS tech talk, and to NASA and FAA partners at a Research Transition Team meeting. 
1D autobraking fallback. 
Geofenced operations with a return to safe region fallback. 
Productive conflict avoidance
 
References 
Plaidypvs can - model and formally reason 
about hybrid systems - help extract and define 
requirements from the system 
Thank you for your attention! Questions, comments? 
[1] A Verification Framework for Runtime Assurance of Autonomous UAS. J Tanner Slagel, Lauren M. White, Aaron Dutle, César Muñoz, Nicolas Crespo. To appear at DASC 2024. [2] A Formal Verification Framework for Runtime Assurance. J Tanner Slagel, Lauren M. White, Aaron Dutle, César Muñoz, Nicolas Crespo. NFM 2024. [3] A Temporal Differential Dynamic Logic Formal Embedding. Lauren M. White, Laura Titolo, J Tanner Slagel, César Muñoz. CPP 2024. [4] Embedding Differential Dynamic Logic in PVS. J Tanner Slagel, Mariano Moscato, Lauren White, César Muñoz, Swee Balachandran, Aaron Dutle. LSFA 2023. [5] Embedding Differential Temporal Dynamic Logic in PVS. Lauren White, Laura Titolo, J Tanner Slagel, TYPES 2023. [6] Towards an Implementation of Differential Dynamic Logic in PVS. J Tanner Slagel, César Muñoz, Swee Balachandran, Mariano Moscato, Aaron Dutle, Paolo Masci, Lauren White. SOAP 2022.
 
Work performed by Anthony Dario2, Aaron Dutle1, Taylor Houtz3, Mariano Moscato2, Cesar Muñoz1, 
 John Siratt1, Laura Titolo2 
1 NASA Langley Research Center 2 Analytical Mechanics Associates 
3 NASA Langley OSTEM Intern 
Neural Network Formal Verification and Numerical Analysis
 
Problem: Machine Learning in Aeronautics 
There is interest in deploying machine learning solutions for problems in aeronautics. 
But can we do it in a safe way? 
Key problems include - Unpredictable behavior - Round-off error in embedded systems 
With a focus on feed-forward neural networks, we investigated these issues.
 
Background: Feed-Forward Neural Networks 
A feed-forward neural network (FFNN) is made up of: 
 A sequence of layers, each taking vector input 
and giving vector output. 
 Each layer contains neurons operating in parallel 
 Each neuron operates by multiplying the input. 
vector with a vector of weights, adding bias, and applying an activation function to the result. A general FFNN, with 5 layers (3 hidden). 
X 1 
X 2 
X 3 
X 4 
F(b + w1x1 + w2x2      + w3x3 + w4x4 )A close-up of a single 
neuron, with weights wi, bias b, and activation 
function F. 
In a quantized neural net, these operations are on fixed-point numbers. This can compromise robustness due to rounding.
 
Analysis of Activation Functions: Formalization in PVS 
- Various activation functions are used to introduce non-linearity. - The choice can affect the complexity of training, execution, and 
verification. - Some common activations were formalized in the PVS theorem 
prover (as real number functions), and certain properties were proven. 
Activation Functions specified: 
 ELU (Exponential Linear Unit) 
 Gaussian Error Linear Unit 
 Leaky ReLU 
 ReLU (Rectified Linear Unit) 
 Sigmoid 
 Softmax 
 Softplus 
 Swish 
 Tanh 
Types of properties proven: 
 Differentiability 
 Derivative (where 
applicable) 
 Monotonicity properties 
 Upper and lower bounds 
 Function values at 
interesting inputs
 
Analysis of Activation Functions: Bounding Quantized Error 
The NASA-developed prototype tool PRECiSA automatically computes a sound overestimation of the rounding error that may occur in floating-point programs. 
Extending PRECiSA for fixed-point operations allowed for formal round-off error estimation for activation functions in quantized neural networks, such as might be found in embedded systems. 
PRECiSAPVS 
program 
Input ranges 
PVS parser Static Analysis 
PVS proof assistant 
PVS certificates 
Kodiak 
Certificate generator 
Verified ✅ Symbolic error expressions 
Round-off errors estimations
 
Numerical Instability: Error Due to Quantization 
Is error from quantization even possible? How bad could it really be? In the worst case, as bad as imaginable  Developed a collection of small binary classification NN examples: 
 5-layer with step activation 
 3-layer with step activation 
 2-layer with ReLU activation 
X 
0 
1 
A single input can alternate class as precision is lowered. 
Each have the following property: For a fixed input X, weights, and biases, using decimal precision ranging from 1 to 5, the output is class 1 for odd precision, and class 0 for even precision. 
Problems: PRECiSA does not natively support matrices yet Scalability: thousands of neurons and input variables 
Solution: Generate an abstract neural network Layer-based abstraction Interval-based abstract domain to abstract the values of weights, bias and neurons in a single layer
 
Numerical Instability: Static analysis-based test case generation 
 Certain activation functions such as Binary Step, ReLU and their variations are  discontinuous and can be implemented as if-then-else statements. 
 For these functions, a small error in the arguments can cause a large variation in the output (instability). 
1. The neural network is approximated using a layer-based abstraction. 
2. PRECiSA computes a set of Boolean conditions from the abstract neural network which encodes the cases in which an instability may occur. 
3. These Boolean conditions are input to the NASA-developed global optimizer Kodiak that performs a paving. 
4. The result of the paving is a set of “boxes” representing combinations of input variables ranges that satisfy the instability conditions. 
Neural Network specification 
Instability Conditions 
Abstract Neural Network 
Paving results
 
Transforming ReLU Classifiers: Translating into Logic 
Classification is a common problem in deep learning, and ReLU is one of the most common activations for deep neural nets. 
Extending existing results for 2-layer networks, we constructively showed that such classifiers are embeddable in a manageable fragment of first-order arithmetic. 
The number of inequalities in the naïve translation grows exponentially with the number of neurons; however, they are not independent. 
The large Boolean combination of inequalities at the right is the transformation of a network with 2-layers, each with 2 neurons, expressed as a formula in PVS.
 
Transforming ReLU Classifiers: Simplification via PVS 
Through a combination of PVS automated methods and manual manipulation, the system of inequalities can be reduced to the following system of 4 inequalities. 
The equivalence proof is fully automatic. 
These methods can be used not only to characterize and verify the behavior classifier, but to compress a network into a more efficient computation. 
Such compression has the added benefit of reducing the opportunities for round-off error associated with activation functions.
 
Future work 
 PRECiSA 
 Add matrix support. 
 Investigate novel abstraction techniques to scale up analysis. 
 Generate critical test cases for differential testing. 
 PVS 
 Develop new library capabilities to better support neural net reasoning. 
 Create proof strategies to further automate simplification of neural net characterizations. 
 Transformation 
 Integrate simplification procedures into translation steps for scaling. 
 Implement algorithm and verify in PVS. 
Test cases 
Real-valued NN 
Fixed-point NN 
Comparison 
Paving results 
PVS