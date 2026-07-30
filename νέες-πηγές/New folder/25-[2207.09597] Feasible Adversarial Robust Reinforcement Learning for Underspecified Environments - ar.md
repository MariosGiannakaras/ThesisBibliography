> Source: https://arxiv.org/abs/2207.09597

[2207.09597] Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments
Skip to main content 
arXiv is now an independent nonprofit! Learn more × 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2207.09597 (cs)
[Submitted on 19 Jul 2022 ( v1), last revised 4 Oct 2022 (this version, v2)]
Title: Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments
Authors: JB Lanier, Stephen McAleer, Pierre Baldi, Roy Fox
View a PDF of the paper titled Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments, by JB Lanier and 3 other authors
View PDF
Abstract: Robust reinforcement learning (RL) considers the problem of learning policies that perform well in the worst case among a set of possible environment parameter values. In real-world environments, choosing the set of possible values for robust RL can be a difficult task. When that set is specified too narrowly, the agent will be left vulnerable to reasonable parameter values unaccounted for. When specified too broadly, the agent will be too cautious. In this paper, we propose Feasible Adversarial Robust RL (FARR), a novel problem formulation and objective for automatically determining the set of environment parameter values over which to be robust. FARR implicitly defines the set of feasible parameter values as those on which an agent could achieve a benchmark reward given enough training resources. By formulating this problem as a two-player zero-sum game, optimizing the FARR objective jointly produces an adversarial distribution over parameter values with feasible support and a policy robust over this feasible parameter set. We demonstrate that approximate Nash equilibria for this objective can be found using a variation of the PSRO algorithm. Furthermore, we show that an optimal agent trained with FARR is more robust to feasible adversarial parameter selection than with existing minimax, domain-randomization, and regret objectives in a parameterized gridworld and three MuJoCo control environments.
Submission history
From: J.B. Lanier [ view email]
[v1] Tue, 19 Jul 2022 23:57:51 UTC (985 KB)
[v2] Tue, 4 Oct 2022 02:48:23 UTC (1,669 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments, by JB Lanier and 3 other authors
View PDF
TeX Source
view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2022-07
Change to browse by:
cs
cs.AI
cs.GT
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2207.09597&description=Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments) [](https://reddit.com/submit?url=https://arxiv.org/abs/2207.09597&title=Feasible Adversarial Robust Reinforcement Learning for Underspecified Environments) [x]
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
  