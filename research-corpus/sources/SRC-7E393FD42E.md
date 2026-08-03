> Source: https://kilthub.cmu.edu/articles/thesis/Solving_Real-World_Tasks_with_AI_Agents/26798437

BrowseSolving Real-World Tasks with AI Agents
Download   ( 16.55 MB )thesis   posted on   2024-09-17, 17:44   authored by  Shuyan Zhou Shuyan Zhou<p> For years, my dream has been to create autonomous AI agents to handle tedious procedural tasks (e.g., arranging conference travel), freeing me to focus on creative endeavors. Modern AI models, especially large language models (LLMs) like ChatGPT, have brought us closer to this goal. But has my dream already come true? This thesis spans AI agent research from 2020 to 2024, acknowledging LLMs as a crucial yet early step in the broader AI agent applications. While LLMs show promise in well-defined tasks (e.g., drafting emails), they struggle with procedural tasks requiring agents to comprehend and apply how-to knowledge during dynamic interactions. Current LLMs are inconsistent in complex procedural tasks. This thesis aims to create AI agents to perform procedural tasks with accuracy, robustness, and trust in an ever-evolving environment and is centered around three key pillars. </p> <p>First, we <strong>study the evaluation of AI agents to systematically understand agent behavior</strong>. There was a lack of benchmarks that mimic real-world complexity, emulate diverse and complex human tasks, and support dynamic interactions to perform systematic evaluations. This led to evaluations that are only partially representative of real-world scenarios. We create a comprehensive benchmark on performing interactive web-based tasks (e.g., book a hotel room near Pittsburgh airport online) that meets these criteria and developed more robust evaluation metrics. Our works reveal the deficiencies of LLM-powered agents in realistic interactive tasks and offer an accessible environment to advance the field. </p> <p>Second, <strong>we augment the expressiveness of AI agents with a more versatile “language” for agents</strong>. Beyond knowledge, humans demonstrate versatility in procedural tasks: we break tasks into smaller sub-tasks, leverage past experiences, use tools, etc. Representing this versatility is challenging with unstructured text. We design a new formalization that equates task-solving to writing Python programs. The inherent expressiveness and structured nature of programs enable AI agents to more accurately and explicitly represent complex processes (e.g., planning sub-tasks → composing nested functions, recalling memory → reusing functions). This new formalization enhances LLMs in reasoning about and performing procedural tasks, significantly improving task execution accuracy. </p> <p>Finally, we <strong>develop resources and design innovative methodologies to enable agents to adapt to unfamiliar tasks</strong>. It is particularly challenging for LLMs to handle information that is not included or included sparsely in their training corpora. Hence, LLMs can benefit from access to external knowledge. We investigate how to make human-authored external knowledge (e.g., manuals) comprehensible to AI agents by enriching such knowledge with detailed breakdowns of sub-tasks. We also propose new mechanisms of knowledge-augmented execution via retrieval, which allows the agents to perform challenging tasks by referring to external knowledge and via data synthesis. Both approaches circumvent the reliance on exact demonstrations. </p>
History
Date
2024-08-01
Degree Type
Dissertation
Thesis Department
Language Technologies Institute
Degree Name
Doctor of Philosophy (PhD)
Advisor(s)
Graham Neubig
Usage metrics
0  0  0  Categories
Natural language processing
Keywords
artificial intelligenceautonomous agentsdigital automationweb navigationcode generationNatural Language ProcessingLicence
CC BY 4.0Exports
RefWorks BibTeX Ref. manager Endnote DataCite NLM DC