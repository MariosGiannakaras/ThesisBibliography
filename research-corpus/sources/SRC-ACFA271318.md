# Value Iteration vs. Policy Iteration - GeeksforGeeks

- Value Iteration vs. Policy Iteration - GeeksforGeeks

- Sign In

- [Courses](https://www.geeksforgeeks.org/machine-learning/what-is-the-difference-between-value-iteration-and-policy-iteration/)

- [Tutorials](https://www.geeksforgeeks.org/machine-learning/what-is-the-difference-between-value-iteration-and-policy-iteration/)

- [Interview Prep](https://www.geeksforgeeks.org/machine-learning/what-is-the-difference-between-value-iteration-and-policy-iteration/)

- [DSA](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)

- [Practice Problems](https://www.geeksforgeeks.org/explore)

- [C](https://www.geeksforgeeks.org/c/c-programming-language/)

- [C++](https://www.geeksforgeeks.org/cpp/c-plus-plus/)

- [Java](https://www.geeksforgeeks.org/java/java/)

- [Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)

- [JavaScript](https://www.geeksforgeeks.org/javascript/javascript-tutorial/)

- [Data Science](https://www.geeksforgeeks.org/data-science/data-science-for-beginners/)

- [Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning/)

- [Courses](https://www.geeksforgeeks.org/courses)

# Value Iteration vs. Policy Iteration

- Last Updated : 9 Oct, 2025

- Value Iteration and Policy Iteration are two popular techniques used in dynamic programming to solve [Markov Decision Processes (MDPs)](https://www.geeksforgeeks.org/machine-learning/markov-decision-process/). Both methods aim to find the best possible strategy known as the *op* timal policy for an agent to follow in a given environment. Understanding the differences, strengths and weaknesses of these two methods is important to choose the right approach for specific RL problems.

## **What is Value Iteration?**

- Value Iteration is an iterative algorithm used to compute the optimal value function V ∗ ( s ) V^*(s) V ∗( s) for each state s in an MDP. The value function is a measure of the expected return (reward) from a given state under the optimal policy.

- In Value Iteration the Bellman Optimality Equation is used to iteratively update the value of each state until it converges to the optimal value function:

- V ∗ ( s ) = max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V ∗ ( s ′ ) ] V^*(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^*(s') \right] V ∗( s)= max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V ∗( s′)]

- Where:

- R ( s , a ) R(s, a) R( s, a) is the immediate reward,

- P ( s ′ ∣ s , a ) P(s'|s, a) P( s′ ∣ s, a) is the transition probability,

- γ γ γ is the discount factor and

- s ′ s' s′ represents the next state.

- value iteration network

- Once the value function converges, the optimal policy can be derived by selecting the action a a a that maximizes the value function:

- π ∗ ( s ) = arg  max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V ∗ ( s ′ ) ] \pi^*(s) = \arg\max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^*(s') \right] π ∗( s)= ar g max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V ∗( s′)]

## **What is Policy Iteration?**

- Policy Iteration is another dynamic programming algorithm used to compute the optimal policy. It alternates between two steps:

- Policy Iteration

- **Policy Evaluation**: For a given policy π \pi π , the value function V π ( s ) V^\pi(s) V π( s) is computed using the Bellman Expectation Equation:

- V π ( s ) = R ( s , π ( s ) ) + γ ∑ s ′ P ( s ′ ∣ s , π ( s ) ) V π ( s ′ ) V^\pi(s) = R(s, \pi(s)) + \gamma \sum_{s'} P(s'|s, \pi(s)) V^\pi(s') V π( s)= R( s, π( s))+ γ ∑ s′  P( s′ ∣ s, π( s)) V π( s′)

- **Policy Improvement**: Once the value function for the current policy is calculated the policy is updated to improve it by selecting the action that maximizes the expected return from each state:

- π ′ ( s ) = arg  max  a [ R ( s , a ) + γ ∑ s ′ P ( s ′ ∣ s , a ) V π ( s ′ ) ] \pi'(s) = \arg\max_a \left[ R(s, a) + \gamma \sum_{s'} P(s'|s, a) V^\pi(s') \right] π′( s)= ar g max a [ R( s, a)+ γ ∑ s′  P( s′ ∣ s, a) V π( s′)]

- This process repeats until the policy converges meaning it no longer changes between iterations.

## **Comparison Between Value Iteration and Policy Iteration**

|   |   |   |

| --- | --- | --- |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

|   |   |   |

## **When to Use Value Iteration and Policy Iteration**

- **Use Value Iteration**:

- When you have a small state space and can afford the computational cost of updating the value function for each state.

- When you want to compute the value function first and derive the policy later.

- **Use Policy Iteration**:

- When you have a larger state space and want to reduce the number of iterations for convergence.

- When you can afford the computational cost of policy evaluation but want faster policy improvement.

- Value Iteration is simpler and more direct in its approach and Policy Iteration often converges faster in practice by improving the policy iteratively. The choice between the two methods depends largely on the problem's scale and the computational resources available. In many real-world applications Policy Iteration may be preferred for its faster convergence especially in problems with large state spaces.

- Suggested Quiz

- 5 Questions

- What is the primary goal of Policy Iteration?

- A To directly learn the best actions from trial and error

- B To estimate the Q-values for each state-action pair

- C To repeatedly evaluate and improve policies until convergence

- D To predict the next state based on past data

- How does Value Iteration differ from Policy Iteration?

- A Value Iteration updates state values without explicitly storing a policy

- B Value Iteration finds the optimal policy before evaluating state values

- C Policy Iteration does not require transition probabilities

- D Policy Iteration is faster than Value Iteration in all cases

- What is Policy Evaluation in Dynamic Programming?

- A A step where the policy is updated to maximize rewards

- B A process of estimating the value function for a given policy

- C A method used to approximate Q-values

- D A reinforcement learning technique that does not require a model

- What is the stopping criterion for Value Iteration?

- A When the policy remains unchanged for a fixed number of steps

- B When the value function does not change significantly

- C When all state-action pairs have been visited

- D When the total reward is maximized

- In Policy Iteration what happens after Policy Evaluation?

- A The policy is updated to improve expected rewards

- B The transition probabilities are recalculated

- C The agent performs random actions to explore

- D The value function is reset to zero

- Quiz Completed Successfully

- Your Score : 0/ 5

- Accuracy : 0%

- Show More

- Login to View Explanation

- **1**/5

- < Previous Next >

- Comment

- [A](https://www.geeksforgeeks.org/user/anuragtriarna/)

- [anuragtriarna](https://www.geeksforgeeks.org/user/anuragtriarna/)

- 1

### Explore

- Machine Learning Basics

- [Introduction 4 min read](https://www.geeksforgeeks.org/machine-learning/introduction-machine-learning/)

- [Types 7 min read](https://www.geeksforgeeks.org/machine-learning/types-of-machine-learning/)

- [ML Pipeline 6 min read](https://www.geeksforgeeks.org/blogs/machine-learning-pipeline/)

- [Applications 2 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-introduction/)

- Python for Machine Learning

- [ML with Python 3 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-with-python/)

- [Numpy 3 min read](https://www.geeksforgeeks.org/python/numpy-tutorial/)

- [Pandas 4 min read](https://www.geeksforgeeks.org/pandas/pandas-tutorial/)

- [Data Preprocessing 4 min read](https://www.geeksforgeeks.org/data-analysis/data-preprocessing-machine-learning-python/)

- [EDA 6 min read](https://www.geeksforgeeks.org/data-analysis/exploratory-data-analysis-in-python/)

- Feature Engineering

- [Feature Engineering 4 min read](https://www.geeksforgeeks.org/machine-learning/what-is-feature-engineering/)

- [Dimensionality Reduction 3 min read](https://www.geeksforgeeks.org/machine-learning/dimensionality-reduction/)

- [Feature Selection 4 min read](https://www.geeksforgeeks.org/machine-learning/feature-selection-techniques-in-machine-learning/)

- Supervised Learning

- [Supervised Learning 4 min read](https://www.geeksforgeeks.org/machine-learning/supervised-machine-learning/)

- [Linear Regression 10 min read](https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/)

- [Logistic Regression 9 min read](https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/)

- [Decision Tree 8 min read](https://www.geeksforgeeks.org/machine-learning/decision-tree-introduction-example/)

- [Random Forest 4 min read](https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/)

- [KNN 8 min read](https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/)

- [SVM 9 min read](https://www.geeksforgeeks.org/machine-learning/support-vector-machine-algorithm/)

- [Naive Bayes 6 min read](https://www.geeksforgeeks.org/machine-learning/naive-bayes-classifiers/)

- Unsupervised Learning

- [Unsupervised Learning 5 min read](https://www.geeksforgeeks.org/machine-learning/unsupervised-learning/)

- [K means Clustering 6 min read](https://www.geeksforgeeks.org/machine-learning/k-means-clustering-introduction/)

- [Hierarchical Clustering 6 min read](https://www.geeksforgeeks.org/machine-learning/hierarchical-clustering/)

- [DBSCAN Clustering 6 min read](https://www.geeksforgeeks.org/machine-learning/dbscan-clustering-in-ml-density-based-clustering/)

- [Apriori Algorithm 5 min read](https://www.geeksforgeeks.org/machine-learning/apriori-algorithm/)

- [FP Growth Algorithm 4 min read](https://www.geeksforgeeks.org/machine-learning/frequent-pattern-growth-algorithm/)

- [ECLAT Algorithm 5 min read](https://www.geeksforgeeks.org/machine-learning/ml-eclat-algorithm/)

- [PCA 6 min read](https://www.geeksforgeeks.org/data-analysis/principal-component-analysis-pca/)

- Model Evaluation and Tuning

- [Evaluation Metrics 9 min read](https://www.geeksforgeeks.org/machine-learning/metrics-for-machine-learning-model/)

- [Regularization 5 min read](https://www.geeksforgeeks.org/machine-learning/regularization-in-machine-learning/)

- [Cross Validation 5 min read](https://www.geeksforgeeks.org/machine-learning/cross-validation-machine-learning/)

- [Hyperparameter Tuning 5 min read](https://www.geeksforgeeks.org/machine-learning/hyperparameter-tuning/)

- [Underfitting and Overfitting 3 min read](https://www.geeksforgeeks.org/machine-learning/underfitting-and-overfitting-in-machine-learning/)

- [Bias and Variance 6 min read](https://www.geeksforgeeks.org/machine-learning/bias-vs-variance-in-machine-learning/)

- Advanced Techniques

- [Reinforcement Learning 8 min read](https://www.geeksforgeeks.org/machine-learning/what-is-reinforcement-learning/)

- [Semi-Supervised Learning 5 min read](https://www.geeksforgeeks.org/machine-learning/ml-semi-supervised-learning/)

- [Self-Supervised Learning 5 min read](https://www.geeksforgeeks.org/machine-learning/self-supervised-learning-ssl/)

- [Ensemble Learning 6 min read](https://www.geeksforgeeks.org/machine-learning/a-comprehensive-guide-to-ensemble-learning/)

- Machine Learning Practice

- [Interview Questions 15+ min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-interview-questions/)

- [ML Projects 5 min read](https://www.geeksforgeeks.org/machine-learning/machine-learning-projects/)

- Courses

- [Data Science and ML Course 2 min read](https://www.geeksforgeeks.org/courses/data-science-live)

- [Generative AI Course 2 min read](https://www.geeksforgeeks.org/courses/generative-ai-training-program)

- [Explore GATE Course 2 min read](https://www.geeksforgeeks.org/courses/category/gate)

- Corporate & Communications Address:

- A-143, 6th Floor, Sovereign Corporate Tower, Sector- 136, Noida, Uttar Pradesh (201305)

- Registered Address:

- K 061, Tower K, Gulshan Vivante Apartment, Sector 137, Noida, Gautam Buddh Nagar, Uttar Pradesh, 201305

- Company

- [About Us](https://www.geeksforgeeks.org/about/)

- [Legal](https://www.geeksforgeeks.org/legal/)

- [Privacy Policy](https://www.geeksforgeeks.org/legal/privacy-policy/)

- [Contact Us](https://www.geeksforgeeks.org/about/contact-us/)

- [Advertise with us](https://www.geeksforgeeks.org/advertise-with-us/)

- [GFG Corporate Solution](https://www.geeksforgeeks.org/gfg-corporate-solution/)

- [Campus Training Program](https://www.geeksforgeeks.org/campus-training-program/)

- Explore

- [POTD](https://www.geeksforgeeks.org/problem-of-the-day)

- [Job-A-Thon](https://practice.geeksforgeeks.org/events/rec/job-a-thon/)

- [Blogs](https://www.geeksforgeeks.org/category/blogs/?type=recent)

- [Nation Skill Up](https://www.geeksforgeeks.org/nation-skill-up/)

- Tutorials

- [Programming Languages](https://www.geeksforgeeks.org/computer-science-fundamentals/programming-language-tutorials/)

- [DSA](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)

- [Web Technology](https://www.geeksforgeeks.org/web-tech/web-technology/)

- [AI, ML & Data Science](https://www.geeksforgeeks.org/machine-learning/ai-ml-and-data-science-tutorial-learn-ai-ml-and-data-science/)

- [DevOps](https://www.geeksforgeeks.org/devops/devops-tutorial/)

- [CS Core Subjects](https://www.geeksforgeeks.org/gate/gate-exam-tutorial/)

- [Interview Preparation](https://www.geeksforgeeks.org/aptitude/interview-corner/)

- [Software and Tools](https://www.geeksforgeeks.org/websites-apps/software-and-tools-a-to-z-list/)

- Courses

- [ML and Data Science](https://www.geeksforgeeks.org/courses/category/machine-learning-data-science)

- [DSA and Placements](https://www.geeksforgeeks.org/courses/category/dsa-placements)

- [Web Development](https://www.geeksforgeeks.org/courses/category/development-testing)

- [Programming Languages](https://www.geeksforgeeks.org/courses/category/programming-languages)

- [DevOps & Cloud](https://www.geeksforgeeks.org/courses/category/cloud-devops)

- [GATE](https://www.geeksforgeeks.org/courses/category/gate)

- [Trending Technologies](https://www.geeksforgeeks.org/courses/category/trending-technologies/)

- Videos

- [DSA](https://www.geeksforgeeks.org/videos/category/sde-sheet/)

- [Python](https://www.geeksforgeeks.org/videos/category/python/)

- [Java](https://www.geeksforgeeks.org/videos/category/java-w6y5f4/)

- [C++](https://www.geeksforgeeks.org/videos/category/c/)

- [Web Development](https://www.geeksforgeeks.org/videos/category/web-development/)

- [Data Science](https://www.geeksforgeeks.org/videos/category/data-science/)

- [CS Subjects](https://www.geeksforgeeks.org/videos/category/cs-subjects/)

- Preparation Corner

- [Interview Corner](https://www.geeksforgeeks.org/interview-prep/interview-corner/)

- [Aptitude](https://www.geeksforgeeks.org/aptitude/aptitude-questions-and-answers/)

- [Puzzles](https://www.geeksforgeeks.org/aptitude/puzzles/)

- [GfG 160](https://www.geeksforgeeks.org/courses/gfg-160-series)

- [System Design](https://www.geeksforgeeks.org/system-design/system-design-tutorial/)

- [@GeeksforGeeks, Sanchhaya Education Private Limited](https://www.geeksforgeeks.org/), [All rights reserved](https://www.geeksforgeeks.org/copyright-information/)