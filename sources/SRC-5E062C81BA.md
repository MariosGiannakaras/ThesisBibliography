> Source: https://proceedings.nips.cc/paper_files/paper/2000/file/e8dfff4676a47048d6f0c4ef899593dd-Paper.pdf

Robust Reinforcement Learning 
J un Morimoto Graduate School of Information Science 
N ara Institute of Science and Technology; Kawato Dynamic Brain Project, JST 2-2 Hikaridai Seika-cho Soraku-gun 
Kyoto 619-0288 JAPAN xmorimo@erato.atr.co.jp 
Kenji Doya ATR International; 
CREST, JST 2-2 Hikaridai Seika-cho Soraku-gun 
Kyoto 619-0288 JAPAN doya@isd.atr.co.jp 
Abstract 
This paper proposes a new reinforcement learning (RL) paradigm that explicitly takes into account input disturbance as well as modeling errors. The use of environmental models in RL is quite popular for both off-line learning by simulations and for on-line action planning. However, the difference between the model and the real environment can lead to unpredictable, often unwanted results. Based on the theory of H oocontrol, we consider a differential game in which a 'disturbing' agent (disturber) tries to make the worst possible disturbance while a 'control' agent (actor) tries to make the best control input. The problem is formulated as finding a minmax solution of a value function that takes into account the norm of the output deviation and the norm of the disturbance. We derive on-line learning algorithms for estimating the value function and for calculating the worst disturbance and the best control in reference to the value function. We tested the paradigm, which we call "Robust Reinforcement Learning (RRL)," in the task of inverted pendulum. In the linear domain, the policy and the value function learned by the on-line algorithms coincided with those derived analytically by the linear H ootheory. For a fully nonlinear swingup task, the control by RRL achieved robust performance against changes in the pendulum weight and friction while a standard RL control could not deal with such environmental changes. 
1 Introduction 
In this study, we propose a new reinforcement learning paradigm that we call "Robust Reinforcement Learning (RRL)." Plain, model-free reinforcement learning (RL) is desperately slow to be applied to on-line learning of real-world problems. Thus the use of environmental models have been quite common both for on-line action planning [3] and for off-line learning by simulation [4]. However, no model can 
be perfect and modeling errors can cause unpredictable results, sometimes worse than with no model at all. In fact , robustness against model uncertainty has been the main subject of research in control community for the last twenty years and the result is formalized as the "'Hoo" control theory [6). 
In general, a modeling error causes a deviation of the real system state from the state predicted by the model. This can be re-interpreted as a disturbance to the model. However, the problem is that the disturbance due to a modeling error can have a strong correlation and thus standard Gaussian assumption may not be valid. The basic strategy to achieve robustness is to keep the sensitivity I of the feedback control loop against a disturbance input small enough so that any disturbance due to the modeling error can be suppressed if the gain of mapping from the state error to the disturbance is bounded by 1;'. In the 'Hooparadigm, those 'disturbance-to-error' and 'error-to-disturbance' gains are measured by a max norms of the functional mappings in order to assure stability for any modes of disturbance. 
In the following, we briefly introduce the 'Hoo paradigm and show that design of a robust controller can be achieved by finding a min-max solution of a value nmction, which is formulated as Hamilton-Jacobi-Isaacs (HJI) equation. We then derive on-line algorithms for estimating the value functions and for simultaneously deriving the worst disturbance and the best control that, respectively, maximizes and minimizes the value function. 
We test the validity of the algorithms first in a linear inverted pendulum task. It is verified that the value function as well as the disturbance and control policies derived by the on-line algorithm coincides with the solution of Riccati equations given by 'Hootheory. We then compare the performance of the robust RL algorithm with a standard model-based RL in a nonlinear task of pendulum swing-up [3). It is shown that robust RL controller can accommodate changes in the weight and the friction of the pendulum, which a standard RL controller cannot cope with. 
2 H 00 Control 
W(s)--..-j 
u(s) 
(a) 
z(s) 
W~G z 
u y K 
(b) 
Figure 1: (a) Generalized Plant and Controller, (b) Small Gain Theorem 
The standard 'Hoocontrol [6) deals with a system shown in Fig.l(a), where G is the plant, K is the controller, u is the control input, y is the measurement available to the controller (in the following, we assume all the states are observable, i.e. y = x), w is unknown disturbance, and z is the error output that is desired to be kept small. In general, the controller K is designed to stabilize the closed loop system based on a model of the plant G. However, when there is a discrepancy between the model and the actual plant dynamics, the feedback loop could be unstable. The effect of modeling error can be equivalently represented as a disturbance w generated by an 
unknown mapping ~ of the plant output z, as shown in Fig.1(b). 
The goal of 1(,,,control problem is to design a controller K that brings the error z to zero while minimizing the Hoonorm of the closed loop transfer function from the disturbance w to the output z 
(1) 
Here II • 112 denotes £2 norm and i7 denotes maximum singular value. The small gain theorem assures that if IITzwiloo ~ 'Y, then the system shown in Fig. l(b) will be stable for any stable mapping ~ : z f-t w with 11~1100 < ~. 
2.1 Min-max Solution to HooProblem 
We consider a dynamical system x = f(x, u, w) . Hoocontrol problem is equivalent to finding a control output u that satisfies a constraint 
(2) 
against all possible disturbance w with x(O) = 0, because it implies 
(3) 
We can consider this problem as differential game[5] in which the best control output u that minimizes V is sought while the worst disturbance w that maximizes V is chosen. Thus an optimal value function V* is defined as 
V* = minmax (00 (zT(t)z(t) _ 'Y2wT(t)w(t))dt. u w 10 
The condition for the optimal value function is given by 
oV* 0= minmax[zT z - 'Y2WTW + ~ f(x, u, w)] 
u w uX 
(4) 
(5) 
which is known as Hamilton-Jacobi-Isaacs (HJI) equation. From (5), we can derive the optimal control output u op and the worst disturbance wop by solving 
OZT Z oV of (x, u , w) _ 0 d OU + ox OU - an 
OZT Z _ 2 T oV of (x, u, w) _ 0 
oW 'YW + ox ow -. (6) 
3 Robust Reinforcement Learning 
Here we consider a continuous-time formulation of reinforcement learning [3] with the system dynamics x = f(x, u) and the reward r(x, u). The basic goal is to find a policy u = g(x) that maximizes the cumulative future reward !too e-·~t r(x(s), u(s))ds for any given state x(t), where T is a time constant of evaluation. However, a particular policy that was optimized for a certain environment may perform badly when the environmental setting changes. In order to 
assure robust performance under changing environment or unknown disturbance, we introduce the notion of worst disturbance in 1i<x> control to the reinforcement learning paradigm. 
In this framework, we consider an augmented reward 
q(t) = r(x(t), u(t)) + s(w(t)), (7) 
where s(w(t)) is an additional reward for withstanding a disturbing input, for example, s(w) = 'Y2wT w. The augmented value function is then defined as 
V(x(t)) = 1 <X> e- ' -;' q(x(s), u(s), w(s))ds. (8) 
The optimal value function is given by the solution of a variant of HJI equation 
1 aV* - V*(x) = maxmin[r(x , u) + s(w) + ~ f(x, u, w)]. 
T U W ux 
(9) 
Note that we can not find appropriate policies (Le. the solutions of the HJI equation) if we choose too small 'Y. In the robust reinforcement learning (RRL) paradigm, the value function is update by using the temporal difference (TD) error [3] 8(t) = q(t) - ~ V(t) + V(t), while the best action and the worst disturbance are generated by maximizing and minimizing, respectively, the right hand side of HJI equation (9). We use a function approximator to implement the value function V(x(t); v), where y is a parameter vector. As in the standard continuous-time RL, we define eligibility trace for a parameter Vi as ei(s) = J; e- ' ;;' 8~jit)dt and up-
date rule as ei(t) = -~ei(t) + 8~v~t) , where", is the time constant of the eligibility trace[3] . We can then derive learning rule for value function approximator [3] as Vi = rJ8(t)ei(t), where rJ denotes the learning rate. Note that we do not assume f(x = 0) = 0 because the error output z is generalized as the reward r(x , u) in RRL framework. 
3.1 Actor-disturber-critic 
We propose actor-disturber-critic architecture by which we can implement robust RL in a model-free fashion as the actor-critic architecture[l]. We define the policies of the actor and the disturber implemented as u(t) = Au(x(t); yU) + nu(t) and w(t) = Aw(x(t); y W) +nw(t), respectively, where Au(x(t); y U) and Aw(x(t); yW) are function approximators with parameter vectors, yU and yW, and nu(t) and nw(t) are noise terms for exploration. The parameters of the actor and the disturber are updated by 
vr = rJu8(t)nu(t) aAu(;~~; yU) 
t 
(10) 
where rJu and rJw denote the learning rates. 
3.2 Robust Policy by Value Gradient 
Now we assume that an input-Affine model of the system dynamics and quadratic models of the costs for the inputs are available as 
x f(x) + gl(X)W + g2(X)U 
r(x , u) = Q(x) - uTR(x)u, s(w) = 'Y2wT w. 
In this case, we can derive the best action and the worst disturbance in reference to the value function V as 
1 -1 T 8V T u op = "2 R(X) g2 (X)( Ox) (11) 
We can use the policy (11) using the value gradient ~~ derived from the value function approximator. 
3.3 Linear Quadratic Case 
Here we consider a case in which a linear dynamic model and quadratic reward models are available as 
x = Ax+B1w+B2u 
r(x, u) 
In this case, the value function is given by a quadratic form V = _xT Px, where P is the solution of a Riccati equation 
TIT -1 T 1 
A P+ PA+ P('iB1B1 - B2R B2 )P+ Q = -Po 
, T (12) 
Thus we can derive the best action and the worst disturbance as 
(13) 
4 Simulation 
We tested the robust RL algorithm in a task of swinging up a pendulum. The dynamics of the pendulum is given by ml2jj = -p,e + mgl sin /9 + T, where /9 is the angle from the upright position , T is input torque, p, = 0.01 is the coefficient of friction, m = 1.0[kg] is the weight of the pendulum, l = 1.0[m] is the length of the pendulum, and g = 9.8[m/s2 ] is the gravity acceleration. The state vector is defined as x = (/9,e)T. 
4.1 Linear Case 
We first considered a linear problem in order to test if the value function and the policy learned by robust RL coincides with the analytic solution of 1icx:>control problem. Thus we use a locally linearized dynamics near the unstable equilibrium point x = (0, O)T . The matrices for the linear model are given by 
A= (~ ~~ ),B1 = (~, ),B2 = (~, ),Q= (~ ~ ),R=1. (14) 
The reward function is given by q( t) = _xT Qx - u2 + ,2W2, where robustness criteria, = 2.0. 
The value function, V = _xT Px, is parameterized by a symmetric matrix P. For on-line estimation of P, we define vectors x = (xi, 2X1X2, XDT, p = (Pll,P12,P22)T and reformulate V as V = _pTx. Each element of p is updated using recursive least squares method[2]. Note that we used pre-designed stabilizing controller as the initial setting of RRL controller for stable learning[2]. 
4.1.1 Learning of the value function Here we used the policy by value gradient shown in section 3.2. Figure 2(a) shows that each element of the vector p converged to the solution of the Ricatti equation (12). 
4.1.2 Actor-disturber-critic 
Here we used robust RL implemented by the actor-disturber-critic shown in section 3.1. In the linear case, the actor and the disturber are represented as the linear controllers, A,,(x; v") = v"x and Aw(x; VW) = vWx, respectively. The actor and the disturber were almost converged to the policy in (13) which derived from the Ricatti equation (12) (Fig. 2(b)). 
100 
80 P" 
.-----------------~- --""'"~ 
lOf . :~------------------::----, 
-5 
v, 
P22 -25 __ • •• __ • _________ •• _ •• ___ ~~ ___ _ 
~~~e::::;;=:;';::~250~300 -3°0 50 100 150 200 250 300 Trials 
(a) Elements of p (b) Elements of v 
Figure 2: Time course of (a)elements of vector p = (Pll,P12,P22) and (b) elements of gain vector of the actor v" = (vf, v~) and the disturber VW = (vi", v2"). The dash-dotted lines show the solution of the Ricatti equation. 
4.2 Applying Robust RL to a Non-linear Dynamics We consider non-linear dynamical system (11), where 
f(x) = ( ~ sine _ ~e ) ,gt{x) = ( ~ ) ,g2(X) = ( ~ ) 
Q(x) = cos(e) - 1, R(x) = 0.04. (15) 
From considering (7) and (15), the reward function is given by q(t) = cos(e) - 1 -0.04u2 + "'·?w2 , where robustness criteria 'Y = 0.22. For approximating the value function, we used Normalized Gaussian Network (NGnet)[3]. Note that the input gain g(x) was also learned[3]. 
Fig.3 shows the value functions acquired by robust RL and standard model-based RL[3]. The value function acquired by robust RL has a shaper ridge (Fig.3(a)) attracts swing up trajectories than that learned with standard RL. 
In FigA, we compared the robustness between the robust RL and the standard RL. Both robust RL controller and the standard RL controller learned to swing up and hold a pendulum with the weight m = 1.0[m] and the coefficient of friction J-t = 0.01 (FigA(a)) . 
The robust RL controller could successfully swing up pendulums with different weight m = 3.0[kg] and the coefficient of friction J-t = 0.3 (FigA(b)). This result showed robustness of the robust RL controller. The standard RL controller could achieve the task in fewer swings for m = 1.0[kg] and J-t = 0.01 (FigA(a)). However, the standard RL controller could not swing up the pendulum with different weight and friction (FigA(b)). 
v 
1 " ·00' 
- 1.00 1 
- 2.001 
th th 
(a) Robust RL (b) Standard RL 
Figure 3: Shape of the value function after 1000 learning trials with m = 1. 0 [kg] , l = 1.0[m], and J1, = 0.01. 
2 - -------------r'- ------1 
.. 1 1 
OS 
Ir_'-"-"R~obu~"' -' ::~~ ... -------------
~~~-~--~S~m"~d'~~~~3~~~~~ Time [sec) 
(a) m = 1.0, J.I, = 0.01 
(\ 
\! \ 
.~. '. 
o ------ ------- -'-------I 
(b) m = 3.0,J.I, = 0.3 
Figure 4: Swing up trajectories with pendulum with different weight and friction. The dash-dotted lines show upright position. 
5 Conclusions In this study, we proposed new RL paradigm called "Robust Reinforcement Learning (RRL)." We showed that RRL can learn analytic solution of the 1-loo controller in the linearized inverted pendulum dynamics and also showed that RRL can deal with modeling error which standard RL can not deal with in the non-linear inverted pendulum swing-up simulation example. We will apply RRL to more complex task like learning stand-up behavior[4]. 
References 
[1] A. G . Barto, R. S. Sutton, and C. W. Anderson. Neuronlike adaptive elements that can solve difficult learning control problems. IEEE Transactions on Systems, Man, and Cybernetics, 13:834- 846, 1983. 
[2] S. J. Bradtke. Reinforcement learning Applied to Linear Quadratic Regulation. In S. J. Hanson, J. D. Cowan, and C. L. Giles, editors, Advances in Neural Information Processing Systems 5, pages 295- 302. Morgan Kaufmann, San Mateo, CA, 1993. 
[3] K. Doya. Reinforcement Learning in Continuous Time and Space. Neural Computation, 12(1):219-245, 2000. 
[4] J . Morimoto and K. Doya. Acquisition of stand-up behavior by a real robot using hierarchical reinforcement learning. In Proceedings of Seventeenth International Conference on Machine Learning, pages 623- 630, San Francisco, CA, 2000. Morgan Kaufmann. 
[5] S. Weiland. Linear Quadratic Games, Hco , and the Riccati Equation. In Proceedings of the Workshop on the Riccati Equation in Control, Systems, and Signals, pages 156- 159. 1989. 
[6] K. Zhou, J . C. Doyle, and K. Glover. Robust Optimal Control. PRENTICE HALL, New J ersey, 1996. 