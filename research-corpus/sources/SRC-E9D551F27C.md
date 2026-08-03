> Source: https://arxiv.org/abs/2511.05694

[2511.05694] Distributionally Robust Self Paced Curriculum Reinforcement Learning
Skip to main content 
arXiv is now an independent nonprofit! Learn more × 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2511.05694 (cs)
[Submitted on 7 Nov 2025 ( v1), last revised 8 Mar 2026 (this version, v3)]
Title: Distributionally Robust Self Paced Curriculum Reinforcement Learning
Authors: Anirudh Satheesh, Keenan Powell, Vaneet Aggarwal
View a PDF of the paper titled Distributionally Robust Self Paced Curriculum Reinforcement Learning, by Anirudh Satheesh and Keenan Powell and Vaneet Aggarwal
View PDF HTML (experimental)
Abstract: A central challenge in reinforcement learning is that policies trained in controlled environments often fail under distribution shifts at deployment into real-world environments. Distributionally Robust Reinforcement Learning (DRRL) addresses this by optimizing for worst-case performance within an uncertainty set defined by a robustness budget \epsilon. However, fixing \epsilon results in a tradeoff between performance and robustness: small values yield high nominal performance but weak robustness, while large values can result in instability and overly conservative policies. We propose Distributionally Robust Self-Paced Curriculum Reinforcement Learning (DR-SPCRL), a method that overcomes this limitation by treating \epsilon as a continuous curriculum. DR-SPCRL adaptively schedules the robustness budget according to the agent's progress, enabling a balance between nominal and robust performance. Empirical results across multiple environments demonstrate that DR-SPCRL not only stabilizes training but also achieves a superior robustness-performance trade-off, yielding an average 11.8% increase in episodic return under varying perturbations compared to fixed or heuristic scheduling strategies, and achieving approximately 1.9\times the performance of the corresponding nominal RL algorithms.
Submission history
From: Anirudh Satheesh [ view email]
[v1] Fri, 7 Nov 2025 20:25:43 UTC (7,355 KB)
[v2] Wed, 12 Nov 2025 02:59:09 UTC (7,355 KB)
[v3] Sun, 8 Mar 2026 03:27:56 UTC (9,315 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Distributionally Robust Self Paced Curriculum Reinforcement Learning, by Anirudh Satheesh and Keenan Powell and Vaneet Aggarwal
View PDF
HTML (experimental)
TeX Source
license icon view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2025-11
Change to browse by:
cs
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
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2511.05694&description=Distributionally Robust Self Paced Curriculum Reinforcement Learning) [](https://reddit.com/submit?url=https://arxiv.org/abs/2511.05694&title=Distributionally Robust Self Paced Curriculum Reinforcement Learning) [x]
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
  