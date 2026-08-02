> Source: https://arxiv.org/abs/2109.14523

[2109.14523] Online Robust Reinforcement Learning with Model Uncertainty
Skip to main content 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2109.14523 (cs)
[Submitted on 29 Sep 2021 ( v1), last revised 28 Oct 2021 (this version, v2)]
Title: Online Robust Reinforcement Learning with Model Uncertainty
Authors: Yue Wang, Shaofeng Zou
View a PDF of the paper titled Online Robust Reinforcement Learning with Model Uncertainty, by Yue Wang and 1 other authors
View PDF
Abstract: Robust reinforcement learning (RL) is to find a policy that optimizes the worst-case performance over an uncertainty set of MDPs. In this paper, we focus on model-free robust RL, where the uncertainty set is defined to be centering at a misspecified MDP that generates a single sample trajectory sequentially and is assumed to be unknown. We develop a sample-based approach to estimate the unknown uncertainty set and design a robust Q-learning algorithm (tabular case) and robust TDC algorithm (function approximation setting), which can be implemented in an online and incremental fashion. For the robust Q-learning algorithm, we prove that it converges to the optimal robust Q function, and for the robust TDC algorithm, we prove that it converges asymptotically to some stationary points. Unlike the results in [Roy et al., 2017], our algorithms do not need any additional conditions on the discount factor to guarantee the convergence. We further characterize the finite-time error bounds of the two algorithms and show that both the robust Q-learning and robust TDC algorithms converge as fast as their vanilla counterparts(within a constant factor). Our numerical experiments further demonstrate the robustness of our algorithms. Our approach can be readily extended to robustify many other algorithms, e.g., TD, SARSA, and other GTD algorithms.
Submission history
From: Yue Wang [ view email]
[v1] Wed, 29 Sep 2021 16:17:47 UTC (1,028 KB)
[v2] Thu, 28 Oct 2021 01:42:01 UTC (1,240 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Online Robust Reinforcement Learning with Model Uncertainty, by Yue Wang and 1 other authors
View PDF
TeX Source
license icon view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2021-09
Change to browse by:
cs
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
DBLP - CS Bibliography
listing | bibtex
Yue Wang
Shaofeng Zou
export BibTeX citation Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2109.14523&description=Online Robust Reinforcement Learning with Model Uncertainty) [](https://reddit.com/submit?url=https://arxiv.org/abs/2109.14523&title=Online Robust Reinforcement Learning with Model Uncertainty) [x]
Bibliographic Tools
Bibliographic and Citation Tools
[-]
Bibliographic Explorer Toggle
Bibliographic Explorer ( What is the Explorer?) [-]
Connected Papers Toggle
Connected Papers ( What is Connected Papers?) [-]
Litmaps Toggle
Litmaps ( What is Litmaps?) [-]
scite.ai Toggle
scite Smart Citations ( What are Smart Citations?) [-]
Code, Data, Media
Code, Data and Media Associated with this Article
[-]
alphaXiv Toggle
alphaXiv ( What is alphaXiv?) [-]
Links to Code Toggle
CatalyzeX Code Finder for Papers ( What is CatalyzeX?) [-]
DagsHub Toggle
DagsHub ( What is DagsHub?) [-]
GotitPub Toggle
Gotit.pub ( What is GotitPub?) [-]
Huggingface Toggle
Hugging Face ( What is Huggingface?) [-]
ScienceCast Toggle
ScienceCast ( What is ScienceCast?) [-]
Demos
Demos
[-]
Replicate Toggle
Replicate ( What is Replicate?) [-]
Spaces Toggle
Hugging Face Spaces ( What is Spaces?) [-]
Spaces Toggle
TXYZ.AI ( What is TXYZ.AI?) [-]
Related Papers
Recommenders and Search Tools
[-]
Link to Influence Flower
Influence Flower ( What are Influence Flowers?) [-]
Core recommender toggle
CORE Recommender ( What is CORE?) [-]
IArxiv recommender toggle
IArxiv Recommender ( What is IArxiv?)
Author
Venue
Institution
Topic [-]
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
Which authors of this paper are endorsers? | Disable MathJax ( What is MathJax?)
We gratefully acknowledge support from our major funders, member institutions, , and all contributors.
About
· Help
· Contact
· Subscribe
· Copyright
· Privacy
· Accessibility
· Operational Status (opens in new tab)
Major funding support from
  