> Source: https://arxiv.org/abs/2305.06657

[2305.06657] On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm
Skip to main content 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2305.06657 (cs)
[Submitted on 11 May 2023 ( v1), last revised 20 Nov 2023 (this version, v3)]
Title: On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm
Authors: Ukjo Hwang, Songnam Hong
View a PDF of the paper titled On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm, by Ukjo Hwang and 1 other authors
View PDF
Abstract: Robust reinforcement learning (RRL) aims at seeking a robust policy to optimize the worst case performance over an uncertainty set of Markov decision processes (MDPs). This set contains some perturbed MDPs from a nominal MDP (N-MDP) that generate samples for training, which reflects some potential mismatches between training (i.e., N-MDP) and true environments. In this paper we present an elaborated uncertainty set by excluding some implausible MDPs from the existing sets. Under this uncertainty set, we develop a sample-based RRL algorithm (named ARQ-Learning) for tabular setting and characterize its finite-time error bound. Also, it is proved that ARQ-Learning converges as fast as the standard Q-Learning and robust Q-Learning while ensuring better robustness. We introduce an additional pessimistic agent which can tackle the major bottleneck for the extension of ARQ-Learning into the cases with larger or continuous state spaces. Incorporating this idea into RL algorithms, we propose double-agent algorithms for model-free RRL. Via experiments, we demonstrate the effectiveness of the proposed algorithms.
Submission history
From: Ukjo Hwang [ view email]
[v1] Thu, 11 May 2023 08:52:09 UTC (4,997 KB)
[v2] Sun, 14 May 2023 10:14:07 UTC (5,031 KB)
[v3] Mon, 20 Nov 2023 03:39:38 UTC (2,142 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm, by Ukjo Hwang and 1 other authors
View PDF
TeX Source
view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2023-05
Change to browse by:
cs
cs.AI
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
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2305.06657&description=On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm) [](https://reddit.com/submit?url=https://arxiv.org/abs/2305.06657&title=On Practical Robust Reinforcement Learning: Practical Uncertainty Set and Double-Agent Algorithm) [x]
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
  