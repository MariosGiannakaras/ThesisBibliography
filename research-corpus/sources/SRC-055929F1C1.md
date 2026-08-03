> Source: https://arxiv.org/abs/2503.00539

[2503.00539] Distributionally Robust Reinforcement Learning with Human Feedback
Skip to main content 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2503.00539 (cs)
[Submitted on 1 Mar 2025 ( v1), last revised 28 Jun 2026 (this version, v2)]
Title: Distributionally Robust Reinforcement Learning with Human Feedback
Authors: Debmalya Mandal, Paulius Sasnauskas, Goran Radanovic
View a PDF of the paper titled Distributionally Robust Reinforcement Learning with Human Feedback, by Debmalya Mandal and 2 other authors
View PDF
Abstract: Reinforcement learning from human feedback (RLHF) has evolved to be one of the main methods for fine-tuning large language models (LLMs). However, existing RLHF methods are non-robust, and their performance deteriorates if the downstream task differs significantly from the preference dataset used in fine-tuning. In order to mitigate this problem, we introduce a distributionally robust RLHF for fine-tuning LLMs. In particular, our goal is to ensure that a fine-tuned model retains its performance even when the distribution of prompts significantly differs from the distribution encountered during fine-tuning. We formulate distributionally robust optimization (DRO) version of two popular fine-tuning methods -- (1) reward-based RLHF and (2) reward-free DPO (direct preference optimization). We propose a minibatch gradient descent based algorithms for both of them, and theoretically prove convergence guarantees for the algorithms. Subsequently, we evaluate our algorithms on an out-of-distribution (OOD) task by first training the model on the Unified-Feedback dataset and evaluating its performance on two different datasets. The experimental results show that our robust training improves the accuracy of the learned reward models on average, and markedly on some tasks, such as reasoning. Furthermore, we show that the robust versions of policy optimization methods, similarly improve performance on OOD tasks.
Submission history
From: Debmalya Mandal [ view email]
[v1] Sat, 1 Mar 2025 15:43:39 UTC (132 KB)
[v2] Sun, 28 Jun 2026 15:31:11 UTC (90 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Distributionally Robust Reinforcement Learning with Human Feedback, by Debmalya Mandal and 2 other authors
View PDF
TeX Source
license icon view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2025-03
Change to browse by:
cs
cs.AI
cs.CL
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
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2503.00539&description=Distributionally Robust Reinforcement Learning with Human Feedback) [](https://reddit.com/submit?url=https://arxiv.org/abs/2503.00539&title=Distributionally Robust Reinforcement Learning with Human Feedback) [x]
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
  