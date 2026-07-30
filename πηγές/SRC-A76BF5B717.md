> Source: https://arxiv.org/pdf/1703.00041

 
 
 
 
 
 
 
 
 
 
 
 
The Schubert normal form of a 3-bridge link and the 3-bridge link group 
Margarita Toro and Mauricio Rivera Universidad Nacional de Colombia, Medelĺın, Colombia. 
mmtoro@unal.edu.co and mrivera@unal.edu.co 
November 2016 
Abstract 
We introduce the Schubert form a 3-bridge link diagram, as a generalization of the Schubert normal form of a 3-bridge link. It consists of a set of six positive integers, written as (p/n, q/m, s/l), with some conditions and it is based on the concept of 3-butterfly. Using the Schubert normal form of a 3-bridge link diagram, we give two presentations of the 3-bridge link group. These presentations are given by concrete formulas that depend on the integers {p, n, q,m, s, l} . The construction is a generalization of the form the link group presentation of the 2-bridge link p/q depends on the integers p and q. 
1 Introduction 
In [5] it was introduced the butterfly presentation of a link diagram as a generalization of the 2-bridge Schubert’s notation. Moreover, the particular concept of a 3-butterfly was implemented in order to study 3-bridge links and to obtain a codification of a 3-bridge link diagram. Here, for our purpose, we do not need all the machinery of the butterfly construction presented in [6], so we will take a different approach. We will describe the construction of the codification by a direct and combinatorial approach, using the ideas in [3], where Ferri constructed the crystallization of the double cover of S3, with a link as ramification set. For any link diagram L there is a strong relation 
1
between crystallization of the double cover of S3, with L as the ramification set, and the 3-butterfly associated to L, that we will explain in [12]. For any n-bridge link diagram the construction of an n-butterfly is possible, see [6], but in this paper we want to be specific and we will work only with 3-bridge link diagrams. 
To a 3-bridge diagram we associate a 3-butterfly that is described by a set of six positive integers {p, n, q,m, s, l}, with some restrictions, and then we define the Schubert form of the link diagram as (p/n, q/m, s/l) , for geometrical reasons that will be explained in Section 1. As each 3-bridge link admits infinitely many different link diagrams, the Schubert normal form for a link L is defined by taking the minimum among all 3-bridge link diagrams of L according to a lexicographical type of order, see [5]. For the purpose of this paper we only need the Schubert form of the link diagram, but in further research and in the compilation of link tables, it will be interesting to consider the Schubert normal form of a link. 
In this paper we find formulas for the over and under presentation of the 3-bridge link represented by the Schubert form (p/n, q/m, s/l), that depends on the integers {p, n, q,m, s, l}. The formula for the under presentation of the 3-bridge link is a natural extension of the formula for the presentation of the 2-bridge link p/q, that depends on the integers p and q. 
The paper is organized as follows: in Section 1 we describe the construction of a 3-butterfly associated to a 3-bridge link diagram L and introduce the Schubert form of L, that consists of a set of 6 positive integers, (p, n, q,m, s, l), that captures the relevant information of the 3-butterfly and, therefore, of the 3-bridge diagram L. In Section 3 we describe a canonical diagram associate to a 3-butterfly (p, n, q,m, s, l), in a similar way to the canonical diagram of a 2-bridge link, see [13]. In Section 5 we will give an orientation to this canonical diagram. 
In Section 4 we define two permutations, γ and φ, associated to the Schubert form (p/n, q/m, s/l), and study the composition µ = γφ. The cyclic structure of µ is the key point in the rest of the paper. A variation of the permutation µ is very useful for the construction of a Gauss code for the link diagram, and, from there we can find the Dowker code and we are able to compute link invariants, such as the link group, the Seifert matrix, the Alexander, Jones and HOMFLY polynomials. 
In Section 6 we present our main result, Theorems 14, 15 and 18, that give explicit presentations for the knot group π (L) of a 3-bridge link L. These presentation are described by clear algorithms, that are easy to program in 
2
a computer and depend on the integers in the Schubert form of the link diagram. In the last section we propose a special family of links, (p/n, p/n, p/n), that have a strong symmetry that is reflected in the group presentation. This symmetry could be exploited in the study of the representations into SL(2,C) of the link group. 
Some authors allow that any n-bridge link diagram can be consider as a k-bridge link diagram, for any k > n, by considering bridges without any undercrossings, see [9]. We neither allow this situation nor consider a split link diagram with more than 3 components, as the one in Fig. 3a, as a 3-bridge link diagram We work with 3-bridge link diagrams as in [1] and [8]. 
Remark on notation: In [11] the author uses subindexes and denote a butterfly by (M1, N1,M2, N2,M3, N3). In this paper we avoid the use of subindexes in the Schubert form, and prefer to assign a different role to each integer, in that way we reach simpler formulas. 
2 Description of the 3-butterfly of a 3-bridge 
link diagram 
Let L be a 3-bridge link such that the projection on the xy plane is a 3-bridge diagram D. Let a, b and c the bridge projections. Draw an ellipse around each of the bridges, in such a way that they are disjoint, and they have the bridges as principal axes. Each ellipse will intercept the diagram D in an even number of points, that will be the vertices. We denote by P,Q and S the ellipses around the bridges a, b and c, respectively, and let 2p (resp. 2q and 2s) the number of intersections of P (resp. Q and S) with the diagram D. Following [6], the ellipses P,Q, S are called butterflies. 
Take the graph R1 formed by the butterflies P,Q, S, the vertices and the bridges. In each butterfly we have the bridge, that divides each butterfly in two halves, that will be the wings. The reflection along the bridges inside the butterflies is called γ. The segment of the underarcs that are inside the butterflies are forgotten, but they can be recovered with the reflection γ. The edges outside the butterflies will give the information on how the butterflies intercept to each other, see Fig. 1a. Each one of these edges connect two vertices of two butterflies, we identify these vertices, to form a set that will be the vertices of our graph. The identification will give an involution on the vertex of the graph, that we call φ. 
3
* P 
Q S 
a c 
K 
P K 
K 
Q 
SS 
P 
Q * 
* 
b 
Figure 1: Graph for 3-butterflies. 
We define the 3-butterfly as the graph R = R1/φ, formed with the vertices of R1 identified by the involution φ. We draw the graph R in any of the three forms shown in Fig. 1. If we consider that the diagram L is in S2 = ∂B, then the graph R define a polygonalization of S2 formed by three polygons, as shown in Fig. 2. Compare this simple construction with the formal one given in [6] and [5]. When we identify the butterflies, there will appear two new points, that will be denoted 0 and ∗. These two points are fundamental, but they are not considered vertices of the 3-butterfly. There can be only two basic forms for the graph R, that are determined by the way the butterflies P,Q and S intersect. 
a b 
* 
0 
P 
Q 
S 
*0 
P 
Q S 
Figure 2: Types of 3-butterflies. 
Type I: The three butterflies intersect in the two points 0 and ∗, see Fig. 2.a. Type II: Two of the polygons do not intersect, see Fig. 2.b. When a 3-bridge link diagram produces a type II butterfly, there is a wave move, see 
4
[9] that allows us to construct a new 3-bridge diagram with lower crossing number. So, we work only with type I butterflies, such that there are no wave moves. 
In order to obtain a canonical way to describe a 3-butterfly, we will always assume that 
p ≥ q ≥ s ≥ 2, (1) 
the condition s ≥ 2 is to ensure that each bridge has at least one crossing. By rotating the plane and interchanging the points 0 and ∗, we can always obtain a 3-butterfly diagram with P at the top, Q to the left and S to the right, and we read it in the counterclockwise direction, P Q S, as shown in Fig. 1. 
Let |P ∩Q| = t be the number of vertices between P and Q, v = |Q ∩ S| and w = |P ∩ S|. As each butterfly intersects the other two, then t, v and w are positive integers that satisfy 2p = t + w, 2q = t + v, and 2s = v + w,therefore 
t = p+ q − s, v = q + s− p, w = p+ s− q. (2) 
As we will only consider the link diagrams with v ≥ 1, then 
p+ 1 ≤ s+ q. (3) 
So the integers p, q and s satisfy (1) and (3). Reciprocally, if we have integers satisfying (1) and (3) we can construct the butterflies P,Q and S. 
Now let us describe the positions of the bridges. We orient clockwise each butterfly. From the point 0, following the orientation, we count the number of vertices between 0 and the vertex in which the bridge begins. We call n,m and l the initial points of the bridges in P,Q and S, respectively. Clearly 
1 ≤ n ≤ p, 1 ≤ m ≤ q, 1 ≤ l ≤ s. (4) 
We are working only with link diagrams with exactly three bridges and not only two or one, this impose conditions on the integers n,m and l. In [5] they found the conditions given in the following theorem. 
5
(5,1,5,2,5,1) (4/2,4/1,3/1) (4/1,4/2,3/1) 
a b c 
Figure 3: Diagrams associated to a non reduced butterfly and to two Schubert forms 
Theorem 1 Every 3-butterfly defines a unique set of integers {p,m, q, n, s, l} such that 
p ≥ q ≥ s ≥ 2, 1 ≤ n ≤ p, 1 ≤ m ≤ q, 1 ≤ l ≤ s, p+ 1 ≤ s+ q (5) 
n+m 6= q + 1, n+ l 6= p + 1, 
if m > q + s− p then n+m 6= 2q + 1 and n+m 6= 2q − p+ 1 
if l < p− s then n+ l 6= p− s+ 1 
if m ≤ q + s− p then m+ l 6= s + 1. 
Reciprocally, if a set of integers {p,m, q, n, s, l} satisfies conditions (5) then it defines a 3-butterfly. 
Note that we may think that inside the butterfly P (resp. Q, S) the bridge a make a (n/p) π rotation, (resp. (m/q)π, (l/s) π). For this geometrical reason we want to use the notation (p/n, q/m, s/l) instead of {p,m, q, n, s, l}, but p/n is not considered as a rational number. 
The conditions on the integers {p, n, q,m, s, l} impose in (5) define a 3-butterfly and a link diagram L, but it is possible that L is a split link with some trivial components, as the diagram associated to {5, 1, 5, 2, 5, 1} shows, see Fig. 3. 
Definition 2 We say that (p, n, q,m, s, l) is a 3-butterfly if the set of integers {p, n, q,m, s, l} satisfies the conditions (5). We say that a 3-butterfly is reduced if the associated diagram is a 3-bridge diagram without any trivial components. We say that (p/n, q/m, s/l) is a Schubert form of a 3-bridge link if the 3-butterfly (p, n, q,m, s, l) is reduced. 
6
We need to be careful with the relative order of the numbers in (p/n, q/m, s/l). 
Example 3 If we change the order, it is possible that we get different Schu-bert forms. The Schubert form (4/2, 4/1, 3/1) represents a knot and (4/1, 4/2, 3/1) represents a two component link. See Fig. 3. 
3 Algorithm to draw a canonical 3-bridge link 
diagram 
We associate to each 3-butterfly (p, n, q,m, s, l) a canonical diagram, in a similar way as the canonical diagram of a 2-bridge link is associated to p/q, see [7]. We draw the three bridges as three segments: bridge a as a vertical segment; bridge b as a segment forming a 1200 angle with the bridge a and bridge c as a segment forming a 2400 angle with the bridge a. 
We divide the bridge a in p segments, and we fix two points in each division, one to the left and one to the right, except at the extreme points, where there is only one. Label them with A = {a0, a1, · · · , a2p−1}, in a counterclockwise sense, so the extreme bridges are labeled a0 and ap. For the bridge b we repeat the process, but we divide the bridge in q segments and label the points with B = {b0, · · · , b2q−1}. For the bridge c the number of segments is s and the labels are C = {c0, · · · , c2s−1}. The subscripts of A (resp. B and C) are taken mod (2p), (resp. mod (2q) and mod (2s)). 
To draw the link diagram we need to join, with appropriate arcs, the points ai, bj and ck, i ∈ Z2p, j ∈ Z2q, and k ∈ Z2s, according to the rules given by permutations φ and γ. 
There are t = p+ q − s arcs between the a and b bridges, namely 
an−1bm, an−2bm+1, an−3bm+2, . . . , an−jbm+j−1, . . . , an−tbm+t−1, 
likewise there are v = q + s− p arcs between the b and c bridges, that are 
bm−1cl, bm−2cl+1, bm−3cl+2, . . . , bm−jcl+j−1, . . . , bm−vcl+v−1, 
and, finally, w = p+ s− q arcs between the c and a bridges, 
cl−1an, cl−2an+1, cl−3an+2, . . . , cl−jan+j−1, . . . , cl−wan+w−1. 
It is enough to know how to construct the first arc between each pair of bridges, and the rest of the arcs are ”parallel” arcs to them, see Fig. 4 
7
ba 
n 
m l 
p 
q s 
c 
n 
m l 
p 
q s 
d 
p 
q s 
Figure 4: Drawing a canonical 3-bridge diagram. 
In the rest of this paper we will refer to the diagram described as the link canonical diagram associated to the Schubert form (p/n, q/m, s/l). Notice that if (p/n, q/m, s/l) does not satisfy the conditions in Theorem 1, we still may use this algorithm to draw a link diagram. 
Lemma 4 If the Schubert form (p/n, q/m, s/l) is reduced, the 3-bridge diagram has p + q + s− 3 crossings. 
4 Permutations associated to a Schubert form 
The conditions for a 3-butterfly {p, n, q,m, s, l} to be reduced can not be described using simple conditions on the integers in a similar way as the conditions to be a 3-butterfly given in (5). Now we need to go deeper and study in detail the permutations φ and γ. Given a set {p, n, q,m, s, l} that satisfies (5) we construct explicitly the associated 3-butterfly and then we draw the 3-bridge diagram. 
Define the 3-butterfly by labelling the vertices of each of the butterflies: P have vertices labeled by A = {a0, · · ·ai, · · · , a2p−1}, i ∈ Z2p; Q with vertices B = {b0, · · · , bj , · · · , b2q−1}, j ∈ Z2q; and S with vertices C = {c0, · · · , cl, · · · , c2s−1}, l ∈ Z2s. The bridge ends are labeled by a0 and ap in P (resp. by b0 and bq in Q and c0 and cs in S). See Fig. 5. 
We have the permutations γ and φ on the set A∪B∪C. The permutation γ is the reflection along the bridges. The permutation φ is determined by the identification of the vertices of two butterflies, so in the 3-butterfly each vertex has two labels. The proofs of the following lemmas are straightforward computations. 
8
S P 
Q b2q-1 
a1 
a2 
ap+1a2p-1 
bq 
b1 
c1 
cs+1 
p 
0 
0 0m l 
** 
* 
q s 
n 
a b 
Figure 5: Orientation and labels of a 3-butterfly. 
Lemma 5 The function defined in the set A ∪ B ∪ C by 
γ (ai) = a2p−i, 0 ≤ i < 2p, γ (bj) = b2q−j , 0 ≤ j < 2q, γ (ch) = b2s−h, 0 ≤ h < 2s 
(6) 
is an order 2 permutation. The set of fixed points is 
E = {a0, ap,b0, bq, c0, cs} . (7) 
The set E = {a0, ap,b0, bq, c0, cs} corresponds to the endpoints of the bridges. It will play an important role in the rest of the paper. 
Lemma 6 The map φ : A ∪B ∪ C → A ∪ B ∪ C defined by 
an−i ←→ bm+i−1, if 1 ≤ i ≤ t, an+j ←→ cl−j−1, if 0 ≤ j ≤ w − 1, bm−h ←→ cl+h−1, if 1 ≤ h ≤ v, 
(8) 
is an order 2 permutation, where t = p+q−s, v = q+s−p and w = p+s−q. 
Note that φ does not have fixed points, and among the bicycles in φ there is no a bicycle in the set 
F = {(a0, b0) , (a0, bq) , (a0, c0) , (a0, cs) , (b0, ap) , (b0, c0) , (9) 
(b0, cs) , (c0, ap) , (c0, bq) , (ap, bq) , (ap, cs) , (bq, cs)} 
9
The construction of φ is well defined for any polygonalization of S2 with 3 polygons, even if they do not satisfy the conditions of Theorem 1. In fact, in terms of the permutation φ, we can rewrite Theorem 1 as follows. 
Theorem 7 A set {p, n, q,m, s, l}, with p ≥ q ≥ s ≥ 2, 1 ≤ n ≤ p, 1 ≤ m ≤ q, 1 ≤ l ≤ s describes a 3-butterfly if and only if the associated permutation φ does not have any of the bicycles in the set F . 
We study the cyclic decomposition of µ = φγ. The orbit of a vertex v will be denoted by Oµ (v). For a cycle τ = (z1 z2 · · · zk) we will use the same symbol to refer to the cycle, to its orbit {z1, z2, · · · , zk} and to the word z1z2 · · · zk. The length of τ will be denoted by |τ |, τ (x) will denote the cycle that contains x and for a function Γ, Γ (τ) will be the word (set) formed by applying Γ to each element in τ . 
Theorem 8 Let (p, n, q,m, s, l) be a 3-butterfly, γ and φ be its associated permutations, given in Lemmas 5 and 6 and let µ = φγ. (p/n, q/m, s/l) is a Schubert form for a 3-bridge link if and only if µ is the product of three disjoint cycles, µ = τ1τ2τ3 such that, for i=1,2,3, |τi ∩ E| = 2, where E is given in (7). 
Proof. Let µ = φγ associated to the 3-butterfly (p, n, q,m, s, l). The 3-butterfly (p, n, q,m, s, l) defines a Schubert form (p/n, q/m, s/l) if and only if the 3-butterfly is reduced. 
Suppose that the butterfly is reduced. The orbit of ap under µ, Oµ (ap) will describe a path that follows the underarc with initial point in ap, so eventually it will arrive to the endpoint of the underarc, say e = µk (ap), e ∈ E, E defined in (7). Then µ (e) = φγ (e) = φ (e) = φφγµk−1 (ap) = γµk−1 (ap), so the orbit will go back to the same underarc, in opposite direction. We take τ1 as the cycle formed by the orbit of ap and τ1 ∩E will contain exactly two vertices. We repeat the same process with the other vertices in E. Since the butterfly is reduced, all the vertices will be crossed by one of the underarcs, so we have only three orbits. 
Reciprocally, if the butterfly is not reduced, there will be a component whose vertex will not be in the orbit of any of the elements in E. See Fig. 3a. 
From now on we will assume that the permutation µ associated to the Schubert form (p/n, q/m, s/l) is the product of three disjoint cycles, µ = τ1τ2τ3. The cyclic decomposition of µ allows us to determine the number of components of the associated link diagram. 
10
Theorem 9 (Classification) Let (p/n, q/m, s/l) be a Schubert form, γ and φ its associated permutations given in 5 and 6, µ = φγ. The 3-bridge link diagram L represented by (p/n, q/m, s/l) satisfies: 
(i) L is a knot if and only if ap /∈ Oµ (a0) , bq /∈ Oµ (b0) and cs /∈ Oµ (c0). (ii) L is a two component link if and only if one, and only one, of the 
following conditions holds: ap ∈ Oµ (a0) , bq ∈ Oµ (b0) or cs ∈ Oµ (c0). (iii) L is a three component link if and only if ap ∈ Oµ (a0) , bq ∈ Oµ (b0) 
and cs ∈ Oµ (c0). 
Proof. Take the cyclic decomposition of µ = τ1τ2τ3 and study each one of the cycles, using the interpretation given in the proof of Theorem 8. 
5 Orientation of the canonical 3-bridge link 
diagram (p/n, q/m, s/l) 
Until now we have not considered the orientation of the link L, but in order to find a group presentation for the link group π (L) we will give an orientation to the canonical diagram described in Section 3. Let µ = φγ = τ1τ2τ3, we study in detail these cycles. In each cycle τi we have two special vertices, that are the fixed points of γ and form the set E defined in (7). Each cycle describes a path around one of the link diagram underarcs, see Fig. 6.b, so one of this special vertices corresponds to the arc initial point, denoted Ii; and the other one to the arc endpoint, denoted Fi. So we consider that when we follow the link, we travel it in the order τ1, τ2 and τ3 and the bridge a in the direction from a0 to ap. 
Definition 10 We define δa (resp. δb, δc), the direction in which we travel the bridge a (resp. b, c) as: δa = 1 and 
δb = 
{ 1, if we go from b0 to bq −1, if we go from bq to b0 
, δc = 
{ 1, if we go from c0 to cs −1, if we go from cs to c0 
When the condition (i) in Theorem 9 is satisfied, the Schubert form corresponds to a knot diagram, hence the orientation of bridge a is enough to determine the knot orientation. We take τ1 as the cycle that contains ap and τ3 as the cycle that contains a0. In the link case we need to determine the orientation of each component. If L is a 3-component link, the condition (iii) 
11
in Theorem 9 is satisfied and we orient each component by δa = δb = δc = 1, τ1 contains ap, τ2 contains bq and τ3 contains cs. If L is a 2-component link the condition (ii) in Theorem 9 holds, again we take τ1 as the cycle that contains ap, and τ3 the cycle that corresponds to the other component. 
Lemma 11 a. If L is a knot, Table 1 contains all possibilities for the endpoints of the cycles τ1, τ2, τ3 and the knot orientation. 
b. If L is a 2-component link, Table 2 contains all possibilities for the endpoints of the cycles τ1, τ2, τ3 and the link orientation. 
I1 F1 I2 F2 I3 F3 δb δc 
ap b0 bq c0 cs a0 1 1 ap b0 bq cs c0 a0 1 −1 ap bq b0 c0 cs a0 −1 1 ap bq b0 cs c0 a0 −1 −1 ap c0 cs b0 bq a0 1 1 ap c0 cs bq b0 a0 −1 1 ap cs c0 b0 bq a0 1 −1 ap cs c0 bq b0 a0 −1 −1 
I1 F1 I2 F2 I3 F3 δb δc 
ap b0 bq a0 cs c0 1 1 ap bq b0 a0 cs c0 −1 1 ap c0 cs a0 bq b0 1 1 ap cs c0 a0 bq b0 1 −1 ap a0 bq c0 cs b0 1 1 ap a0 bq cs c0 b0 1 −1 
Table 1 Table 2 
To avoid the lack of uniqueness in the cycles, we always write the cycle τi as an ordered set with initial point Ii, but to simplify notation we keep the cycle notation. In general this will not generate confusion in our work. 
Lemma 12 Let µ be the permutation associated to the Schubert form (p/n, q/m, s/l), µ = τ1τ2τ3, for i=1,2,3 we have: 
(i) Each cycle τi is even, with order |τi| greater than 4. (ii) τi = {Ii, z1, · · · , zk, Fi, γ (zk) , · · · , γ (z1)} , for zj ∈ A ∪ B ∪ C, j = 
1, · · · , k, k ≥ 1. (iii) τ 
|τi|/2 i contains the transposition (Ii, Fi). 
Proof. By condition (9) we get µ (Ii) = τi (Ii) 6= Fi, so the length of the cycle τi is greater than 3. Then, there exists zj ∈ A∪B ∪C, j = 1, · · · , k ≥ 1 such that z1 = µ (Ii) , z2 = µ (z1) , · · · , zk = µ (zk−1) and Fi = µ (zk) = φγ (zk) , this yields 
µ (Fi) = φγ (Fi) = φ (Fi) = φ (φγ (zk)) = γ (zk) . 
12
Now, 
µ (γ (zk)) = φγ (γ (zk)) = φ (zk) = φ (φγ (zk−1)) = γ (zk−1) , 
and then, for j = k, · · · , 2, we get µ (γ (zj)) = φγ (γ (zj)) = φ (zj) = φ (φγ (zj−1)) = γ (zj−1) . 
The relevant information on each cycle τi is contained in the first part of the cycle, we define the initial segment of τi as 
τ̃i = {Ii, z1, · · · , zk} (10) 
We may summarize the results up to now in an algorithm that allows us to find the cycles τ1, τ2, τ3, the set E and therefore the directions δb and δc associated to a Schubert form. 
Let σ be the permutation in A ∪ B ∪ C defined by 
σ = (a0 ap) (b0 bq) (c0 cs) . 
This permutation corresponds to ”travel the bridges” in the diagram. 
Algorithm 13 Given a Schubert form (p/n, q/m, s/l) the following algorithm finds the orientation of the associated link diagram. It provides the cycles τ1, τ2, τ3 such that µ = τ1τ2τ3, where the cycle τi has the form given in Lemma 12. 
1. Take I1 = ap, τ1 = Oµ (I1) and F1 = τ |τ1|/2 1 (I1) . 
2. If F1 = I1 take I2 = bq else take I2 = σ (F1) . 
3. Take τ2 = Oµ (I2) and F2 = τ |τ2|/2 2 (I2) . 
4. If σ (F2) /∈ {I1, F1, I2, F2} then take I3 = σ (F2) else take I3 as the unique element in {bq, cs} − {I1, F1, I2, F2}. 
5. Take τ3 = Oµ (I3) and F3 = τ |τ3|/2 3 (I3). 
6 Presentation of the 3-bridge link group 
Let L be the link diagram with Schubert form (p/n, q/m, s/l). We have an explicit way to find the over and under presentations of the link group of L, see [1] and [2]. This method requires to use the link diagram. We will use this method, but we will replace the explicit use of the diagram by an algorithm that uses the permutations φ, γ and µ and some new functions defined on the 
13
set A∪B∪C. As the description of the over and under presentations requires an oriented link diagram, we will always refer to the standard link diagram and orientation described in Section 3. It is important to remark that we need the diagram only to explain the construction, but the algorithm to find the presentations do not require to draw the link diagram, it depends only on the permutations φ, γ and µ = φγ. As φ, γ depend only of the Schubert form (p/n, q/m, s/l), the presentation of the link group will depend only on the integers {p, n, q,m, s, l}. The algorithm is efficient and easy to implement in a software such as Mathematica. 
6.1 Over presentation of the 3-bridge link (p/n, q/m, s/l) 
We take meridians around the bridges as group generators, and label them by the same name as the bridges, so we have generators a, b and c, see Fig. 6a. 
a0 
ap 
c0 
cs 
a 
c 
bq 
b0 
* 
b a0 
a2 
c0 
c5 
b5 
b0 
a1a9 
a3 
a4 
a5 a6 a7a8 
b3 
b1b2b4 
b6 
b7 
b8 
b9 
c6 
c2c3 c4 
c1 
c7 
a0 
ap 
c0 
cs 
c 
a 
* 
b 
bq 
b0 
a b c 
Figure 6: Generators for the over presentation in a. and the under presentation in c. Path around an underarc in b. 
We find the relators by traveling the frontier of a neighborhood of the underarcs, as shown in Fig. 6b, so these paths are precisely the orbits τi, i = 1, 2, 3. 
Each relator is a word in a, b and c constructed with the convention that each time we cross the bridge a (resp. b, c) we write a±1 (resp. b±1, c±1) 
depending of the sign of the crossing, given by the convention + -
. We replace this graphic process by defining a function Γ that ”forgets the 
index but remembers the direction”. Consider Γ : A∪B∪C → {a±1, b±1, b±1} 
14
defined by 
Γ (ai) = 
{ a if 0 < i ≤ p a−1 otherwise 
,Γ (bi) = 
{ bδb if 0 < i ≤ q b−δb otherwise. 
, (11) 
Γ (ci) = 
{ cδc if 0 < i ≤ s c−δc otherwise. 
The relators are r1 = Γ (τ1) , r2 = Γ (τ2) and r3 = Γ (τ3), where Γ (τi) means the word obtained when we apply Γ to each element in the orbit τi. 
Thus we have proved the following proposition. 
Proposition 14 The link group of the link L given by the Schubert form (p/n, q/m, s/l) admits a presentation given by 
π (L) = 〈a, b, c | Γ (τ1) ,Γ (τ2) ,Γ (τ3)〉 
were µ = τ1τ2τ3 is the associated permutation and Γ is given in (11). 
By the symmetry of the cycles described in Lemma 12, we may rewrite the relators as the relations. When the Schubert form (p/n, q/m, s/l) defines a knot, using the information in Table 1 we find that 
r1 : awa = wab, r2 : bwb = wbc, r3 : cwc = wca, in the first four cases, 
or 
r1 : awa = wac, r2 : cwc = wcb, r3 : bwb = wba, in the last four cases. 
For the case when it is a link we have similar relations. At this moment we have lost the geometrical meaning of the generators, 
so we may rename the generators, if necessary, and unify the two cases, so we have the following proposition. 
Proposition 15 The link L given by the Schubert form (p/n, q/m, s/l) admits a presentation given by 
i. 〈a, b, c | aw1 = w1b, bw2 = w2c, cw3 = w3a〉 if L is a knot, 
ii. 〈a, b, c | aw1 = w1b, bw2 = w2a, cw3 = w3c〉 if L is a 2-component link, 
iii. 〈a, b, c | aw1 = w1a, bw2 = w2b, cw3 = w3c〉 if L is a 3-component link, 
were wi is a word in a, b, c given by wi = Γ (τ̃i) were Γ is defined in (11) and τ̃i is defined in (10). 
15
We know that in the case of knots, one of the relations is redundant, but for practical reasons we prefer to have all of them and, in particular computations, we omit the longest relation, that we do not know in advance which one will be. This contrasts with the under presentation that we will introduce in the next section, in which we know the lengths of the words involved. 
Lemma 16 The sum of the lengths of the words w1, w2 and w3 is p+q+s−3. 
Lemma 17 When L is a knot, the peripheral system of the group is given by 〈a, l〉 with l = w1w2w3a 
−k and k is the exponent sum of the word w1w2w3. 
Proof. By direct computation we have 
al = aw1w2w3a −k = w1bw2w3a 
−k = w1w2cw3a −k = w1w2w3aa 
−k = la 
6.2 Under presentation of the 3-bridge link (p/n, q/m, s/l) 
The under presentation is the dual presentation of the over presentation. Those dual presentations play a central role in the proofs of properties of the knot group and the Alexander polynomial of knots, see [2]. By studying these presentations we find a similar algorithm to the known one to find the 2-bridge link group, that has an explicit formula depending of p and q. Of course, we need a more elaborate algorithm. 
We take as generators of π (L) the meridians around the underarcs, see 5c. Again, the key point is to use the cyclic decomposition of µ. We call a (resp. b and c) the generators corresponding to the underarc described by τ1 (resp. τ2 and τ3). 
The relations are given by traveling the boundary of each butterfly, that describe simple closed paths around the bridges. 
So the first path is given by {a0, · · · , a2p−1}, the second by {b0, · · · , a2q−1} and the third by {c0, · · · , c2s−1}. The graphical procedure to find the relators is: Each time we cross the link we encounter one of the vertices in the set A ∪B ∪ C, we identify the underarc, say x, and the sign of the crossing, sg, and write xsg, with x ∈ {a, b, c} and sg = ±1. 
Again, this procedure will be established by defining a function ρ, similar to the one defined in (11), that identifies the underarc that contains the 
16
vertex and the direction of the crossing. Let ρ : A∪B ∪C → {a±1, b±1, c±1} defined by 
If x ∈ E, ρ (x) = 
   
a if x ∈ τ̃1 a−1 if x /∈ τ̃1 bδb if x ∈ τ̃2 b−δb if x /∈ τ̃2 cδc if x ∈ τ̃3 c−δs if x /∈ τ̃3 
. If x /∈ E, ρ (x) = 
   
a if x ∈ τ̃1 a−1 if γ (x) ∈ τ̃1 bδb if x ∈ τ̃2 b−δb if γ (x) ∈ τ̃2 cδc if x ∈ τ̃3 c−δs if γ (x) ∈ τ̃3 
The relators are 
sa = ρ (a0a1 · · · a2p−1) = ρ (a0) ρ (a1) · · · ρ (a2p−1) , 
sb = ρ (b0b1 · · · b2p−1) = ρ (b0) ρ (b1) · · · ρ (b2q−1) , 
sc = ρ (b0b1 · · · b2p−1) = ρ (c0) ρ (c1) · · · ρ (c2s−1) . 
For the symmetry of the functions and the cycles given in Lemma 12, we have that if γ (x) 6= x, ρ (γ (x)) = ρ (x)−1, therefore if we take the words 
ua = ρ (a1) · · ·ρ (ap−1) , ub = ρ (b1) · · ·ρ (bq−1) , uc = ρ (c1) · · · ρ (cs−1) , (12) 
the relators become the relations 
cua = uaa, aub = ubb, buc = ucc 
or bua = uaa, auc = ucc, cub = uba. 
Note that the lengths of the words ua, ub and uc are p − 1, q − 1 and s − 1, respectively. In this case it is not possible to change the variable names, because we want to have the information about the word lengths. 
Now the peripheral system is given by 〈a, l′〉 where l′ = uaubucf −e, were 
e is the exponent sum of the word uaubuc. We have proved the following theorem: 
Theorem 18 The link L given by the butterfly (p/n, q/m, s/l) admits a presentation given by: 
i. If L is a knot 
〈a, b, c | cua = uaa, aub = ubb, buc = ucc〉 , or 
〈a, b, c | bua = uaa, auc = ucc, cub = uba.〉 , 
17
ii. If L is a 3-component link 
〈a, b, c | aua = uaa, bub = ubb, cuc = ucc〉 , 
with ua, ub and uc words of length p− 1, q− 1 and s− 1, respectively, defined by (12). 
If L is a 2-component link there are six possible combination for the presentation, that are the natural variations of 〈a, b, c | aua = uaa, cub = ubb, buc = ucc〉 . 
Note: This construction does not depend on the fact that p ≥ q ≥ s, nor that we are working with type I butterfly. So we may use it in a more general way. However, if we take the Schubert form (p/n, q/m, s/l) we know that in the knot case one of the relations is redundant, and in this presentation we know that the longest is the first one, so usually that is the one we eliminate. 
7 Special family: (p/n, p/n, p/n) 
In general we do not have an exact pattern for a 3-bridge link group, as the one we encounter for 2-bridge links, see [8], but there are families of 3-bridge links with a very regular pattern for the fundamental group. One of them is the family of links with Schubert form (p/n, p/n, p/n), for integers 1 ≤ n ≤ p. This family contains: Borromean rings (5/2, 5/2, 5/2), the pretzel link P (p, p, p), that corresponds to (2p/p, 2p/p, 2p/p); the toroidal knot T (3, p) and its mirror image T (3,−p), that corresponds to (p/1, p/1, p/1) and to (p/p, p/p, p/p), respectively. The standard diagrams of the links in this family have symmetries of order 2 and 3. 
Proposition 19 For the link L with Schubert form (p/n, p/n, p/n) there exists a word w (x, y, z) in the variables x, y and z, such that if wa = w (a, b, c) , wb = w (b, c, a) and wc = w (c, a, b) then: 
i. If L is a knot, the knot group has the presentation 
〈a, b, c | awa = wab, bwb = wbc, cwc = wca〉 . 
2. If L is a link, it has 3 components and the link group has the presentation 
〈a, b, c | awa = waa, bwb = wbb, cwc = wcc〉 . 
Proof. Study the symmetry of the link diagram. 
18
Example 20 1. The Borromean rings have Schubert normal form (5/2, 5/2, 5/2) and w (x, y, z) = yz−1y−1z. 
2. The knot 819 in Rolfsen´s table has Schubert normal form (4/1, 4/1, 4/1) and w (x, y, z) = zyx. Note that it is the toroidal knot T (3, 4). In general, the toroidal link (p/1, p/1, p/1) is a 3-component link if p ≡ 1 mod 3 and it is a knot in the other cases; and the word w in Proposition 19 is 
w (x, y, z) = 
   
(zyx)p/3 If p ≡ 1 mod 3 
(zyx)[p/3] z If p ≡ 2 mod 3 
(zyx)[p/3] zy If p ≡ 0 mod 3, 
were [m] means the integer part of m. 3. The knot 935 in Rolfsen´s table has Schubert normal form (6/3, 6/3, 6/3) 
and w (x, y, z) = z−1xz−1yz−1. Note that it is the Pretzel knot (3, 3, 3). In general the Pretzel link (2p/p, 2p/p, 2p/p) is a knot if p is odd and a 3-component link if p is even and the word w in Proposition 19 is 
w (x, y, z) = 
{ (z−1x) 
[p/2] z−1 (z−1y) 
[p/2] If p is odd 
(z−1x) (p−2)/2 
z−1xy−1 (xy−1) (p−2)/2 
If p is even. 
References 
[1] G. Burde and H. Zieschang, Knots, Walter de Gruyter, New York, NY (1985). 
[2] R. Crowell and R. Fox, Introduction To Knot Theory, Blaisdell Publish-ing Company, New York, NY, 1963. 
[3] M. Ferri, Crystallizations of 2-fold branched coverings of S3, Proc. Amer. Math. Soc. 73 (1979), 277-276. 
[4] H. M. Hilden, J. M. Montesinos, D. M. Tejada and M. M. Toro. Rep-resenting 3-manifolds by triangulations of S3. Revista Colombiana de Matemáticas, Vol 39, No 2 (2005), 63-86. 
[5] H. M. Hilden, J. M. Montesinos, D. M. Tejada and M. M. Toro, A new representation of links: Butterflies. arXiv:1203.2045v1. 
19
[6] H. M. Hilden, J. M. Montesinos, D. M. Tejada and M. M. Toro, On the classification of 3-bridge links, Revista Colombiana de Matemáticas, Vol. 46, No 2 (2012), 113-144. 
[7] Kawauchi, A. A survey of knot theory. Birkhäuser, Basel Berlin, (1996). 
[8] K. Murasugi, Knot theory and its applications, Birkhäuser, Boston, 1996. 
[9] S. Negami, The minimun crossing of 3-bridge links, Osaka J. Math. 21, N0 3 (1984), 477-487. 
[10] Neuwirth, L. Knot Groups. Westview Press, Boulder, Colorado, 1969. 
[11] M. Rivera, Enlaces de tres puentes, Tesis doctoral, Universidad Nacional de Colombia, Medelĺın, Colombia, 2016. 
[12] M. Rivera and M. Toro, Crystallizations of genus 2 manifolds and butterfly presentations of 3-bridge links, preprint, 2016. 
[13] H. Schubert, Knoten mit zwei Brücken, Math. Z. 65 (1956), 133-170. 
20