> Source: https://www.geeksforgeeks.org/machine-learning/what-is-the-difference-between-value-iteration-and-policy-iteration/

Value Iteration vs. Policy Iteration - GeeksforGeeks
 
Sign In
Courses
Tutorials
Interview Prep
DSA
Practice Problems
C
C++
Java
Python
JavaScript
Data Science
Machine Learning
Courses
Value Iteration vs. Policy Iteration
Last Updated : 9 Oct, 2025
Value Iteration and Policy Iteration are two popular techniques used in dynamic programming to solve Markov Decision Processes (MDPs). Both methods aim to find the best possible strategy known as the op timal policy for an agent to follow in a given environment. Understanding the differences, strengths and weaknesses of these two methods is important to choose the right approach for specific RL problems.
What is Value Iteration?
Value Iteration is an iterative algorithm used to compute the optimal value function V ∗ ( s ) V^*(s) V ∗( s) for each state s in an MDP. The value function is a measure of the expected return (reward) from a given state under the optimal policy.
In Value Iteration the Bellman Optimality Equation is used to iteratively update the value of each state until it converges to the optimal value function:
V ∗ ( s ) = max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V ∗ ( s ′ ) ] V^(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^(s') \right] V ∗( s)= max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V ∗( s′)]
Where:
R ( s , a ) R(s, a) R( s, a) is the immediate reward,
P ( s ′ ∣ s , a ) P(s'|s, a) P( s′ ∣ s, a) is the transition probability,
γ γ γ is the discount factor and
s ′ s' s′ represents the next state. 
value iteration network
Once the value function converges, the optimal policy can be derived by selecting the action a a a that maximizes the value function:
π ∗ ( s ) = arg  max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V ∗ ( s ′ ) ] \pi^(s) = \arg\max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^(s') \right] π ∗( s)= ar g max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V ∗( s′)]
What is Policy Iteration?
Policy Iteration is another dynamic programming algorithm used to compute the optimal policy. It alternates between two steps: 
Policy Iteration
Policy Evaluation: For a given policy π \pi π , the value function V π ( s ) V^\pi(s) V π( s) is computed using the Bellman Expectation Equation:
V π ( s ) = R ( s , π ( s ) ) + γ ∑ s ′ P ( s ′ ∣ s , π ( s ) ) V π ( s ′ ) V^\pi(s) = R(s, \pi(s)) + \gamma \sum_{s'} P(s'|s, \pi(s)) V^\pi(s') V π( s)= R( s, π( s))+ γ ∑ s′  P( s′ ∣ s, π( s)) V π( s′)
Policy Improvement: Once the value function for the current policy is calculated the policy is updated to improve it by selecting the action that maximizes the expected return from each state:
π ′ ( s ) = arg  max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V π ( s ′ ) ] \pi'(s) = \arg\max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^\pi(s') \right] π′( s)= ar g max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V π( s′)]
This process repeats until the policy converges meaning it no longer changes between iterations.
Comparison Between Value Iteration and Policy Iteration
When to Use Value Iteration and Policy Iteration
Use Value Iteration:
When you have a small state space and can afford the computational cost of updating the value function for each state.
When you want to compute the value function first and derive the policy later.
Use Policy Iteration:
When you have a larger state space and want to reduce the number of iterations for convergence.
When you can afford the computational cost of policy evaluation but want faster policy improvement.
Value Iteration is simpler and more direct in its approach and Policy Iteration often converges faster in practice by improving the policy iteratively. The choice between the two methods depends largely on the problem's scale and the computational resources available. In many real-world applications Policy Iteration may be preferred for its faster convergence especially in problems with large state spaces.
Suggested Quiz 
5 Questions
What is the primary goal of Policy Iteration?
A To directly learn the best actions from trial and error
B To estimate the Q-values for each state-action pair
C To repeatedly evaluate and improve policies until convergence
D To predict the next state based on past data
How does Value Iteration differ from Policy Iteration?
A Value Iteration updates state values without explicitly storing a policy
B Value Iteration finds the optimal policy before evaluating state values
C Policy Iteration does not require transition probabilities
D Policy Iteration is faster than Value Iteration in all cases
What is Policy Evaluation in Dynamic Programming?
A A step where the policy is updated to maximize rewards
B A process of estimating the value function for a given policy
C A method used to approximate Q-values
D A reinforcement learning technique that does not require a model
What is the stopping criterion for Value Iteration?
A When the policy remains unchanged for a fixed number of steps
B When the value function does not change significantly
C When all state-action pairs have been visited
D When the total reward is maximized
In Policy Iteration what happens after Policy Evaluation?
A The policy is updated to improve expected rewards
B The transition probabilities are recalculated
C The agent performs random actions to explore
D The value function is reset to zero 
Quiz Completed Successfully
Your Score : 0/ 5
Accuracy : 0%
Show More
Login to View Explanation
1/5
< Previous Next >
Comment
A
anuragtriarna
1
Explore
Machine Learning Basics
Introduction 4 min read
Types 7 min read
ML Pipeline 6 min read
Applications 2 min read
Python for Machine Learning
ML with Python 3 min read
Numpy 3 min read
Pandas 4 min read
Data Preprocessing 4 min read
EDA 6 min read
Feature Engineering
Feature Engineering 4 min read
Dimensionality Reduction 3 min read
Feature Selection 4 min read
Supervised Learning
Supervised Learning 4 min read
Linear Regression 10 min read
Logistic Regression 9 min read
Decision Tree 8 min read
Random Forest 4 min read
KNN 8 min read
SVM 9 min read
Naive Bayes 6 min read
Unsupervised Learning
Unsupervised Learning 5 min read
K means Clustering 6 min read
Hierarchical Clustering 6 min read
DBSCAN Clustering 6 min read
Apriori Algorithm 5 min read
FP Growth Algorithm 4 min read
ECLAT Algorithm 5 min read
PCA 6 min read
Model Evaluation and Tuning
Evaluation Metrics 9 min read
Regularization 5 min read
Cross Validation 5 min read
Hyperparameter Tuning 5 min read
Underfitting and Overfitting 3 min read
Bias and Variance 6 min read
Advanced Techniques
Reinforcement Learning 8 min read
Semi-Supervised Learning 5 min read
Self-Supervised Learning 5 min read
Ensemble Learning 6 min read
Machine Learning Practice
Interview Questions 15+ min read
ML Projects 5 min read
Courses
Data Science and ML Course 2 min read
Generative AI Course 2 min read
Explore GATE Course 2 min read
 
Corporate & Communications Address:
A-143, 6th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305) 
Registered Address:
K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305     
 
Company
About Us
Legal
Privacy Policy
Contact Us
Advertise with us
GFG Corporate Solution
Campus Training Program
Explore
POTD
Job-A-Thon
Blogs
Nation Skill Up
Tutorials
Programming Languages
DSA
Web Technology
AI, ML & Data Science
DevOps
CS Core Subjects
Interview Preparation
Software and Tools
Courses
ML and Data Science
DSA and Placements
Web Development
Programming Languages
DevOps & Cloud
GATE
Trending Technologies
Videos
DSA
Python
Java
C++
Web Development
Data Science
CS Subjects
Preparation Corner
Interview Corner
Aptitude
Puzzles
GfG 160
System Design
@GeeksforGeeks, Sanchhaya Education Private Limited, All rights reserved 