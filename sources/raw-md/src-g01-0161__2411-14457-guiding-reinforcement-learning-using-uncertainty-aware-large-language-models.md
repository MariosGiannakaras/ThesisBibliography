> Source: https://arxiv.org/abs/2411.14457

[2411.14457] Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models
Skip to main content 
Search Submit Donate Log in
Search arXiv
Press Enter to search · Advanced search
Computer Science > Machine Learning
arXiv:2411.14457 (cs)
[Submitted on 15 Nov 2024]
Title: Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models
Authors: Maryam Shoaeinaeini, Brent Harrison
View a PDF of the paper titled Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models, by Maryam Shoaeinaeini and 1 other authors
View PDF HTML (experimental)
Abstract: Human guidance in reinforcement learning (RL) is often impractical for large-scale applications due to high costs and time constraints. Large Language Models (LLMs) offer a promising alternative to mitigate RL sample inefficiency and potentially replace human trainers. However, applying LLMs as RL trainers is challenging due to their overconfidence and less reliable solutions in sequential tasks. We address this limitation by introducing a calibrated guidance system that uses Monte Carlo Dropout to enhance LLM advice reliability by assessing prediction variances from multiple forward passes. Additionally, we develop a novel RL policy shaping method based on dynamic model average entropy to adjust the LLM's influence on RL policies according to guidance uncertainty. This approach ensures robust RL training by relying on reliable LLM guidance. To validate our contributions, we conduct extensive experiments in a Minigrid environment with three goals in varying environment sizes. The results showcase superior model performance compared to uncalibrated LLMs, unguided RL, and calibrated LLMs with different shaping policies. Moreover, we analyze various uncertainty estimation methods, demonstrating the effectiveness of average entropy in reflecting higher uncertainty in incorrect guidance. These findings highlight the persistent overconfidence in fine-tuned LLMs and underscore the importance of effective calibration in sequential decision-making problems.
Submission history
From: Maryam Shoaeinaeini [ view email]
[v1] Fri, 15 Nov 2024 22:00:29 UTC (531 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models, by Maryam Shoaeinaeini and 1 other authors
View PDF
HTML (experimental)
TeX Source
license icon view license
Current browse context:
cs.LG
< prev | next >
new | recent | 2024-11
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
[](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2411.14457&description=Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models) [](https://reddit.com/submit?url=https://arxiv.org/abs/2411.14457&title=Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models) [x]
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
  