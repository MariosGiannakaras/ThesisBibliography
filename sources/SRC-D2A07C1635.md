> Source: https://aaltodoc.aalto.fi/items/b65a3986-b906-4c79-894b-3ccd57252c21

Safe reinforcement learning for real robots
We collect and process your personal information for the following purposes: Functional, Statistical
That's ok
Decline
Customize
Skip to main content 
en | fi | sv |
Log In(current)
Communities & Collections
Browse Aaltodoc publication archive
Statistics
Home
Master's theses
[dipl] Sähkötekniikan korkeakoulu / ELEC
Safe reinforcement learning for real robots
aalto1 untyped-item.component.html
Safe reinforcement learning for real robots
No Thumbnail Available
Files
master_Valdivia_Juan_Pablo_2023.pdf (4.91 MB)
URL
Journal Title
Journal ISSN
Volume Title
Sähkötekniikan korkeakoulu | G2 Pro gradu, diplomityö
Unless otherwise stated, all rights belong to the author. You may download, display and print this publication for Your own personal use. Commercial use is prohibited.
Authors
Valdivia, Juan Pablo
Date
2023-12-11
Department
Major/Subject
Autonomous Systems
Mcode
ELEC3055
Degree programme
Master's Programme in ICT Innovation
Language
en
Pages
69
Series
Abstract
This thesis explores the field of Safe Reinforcement Learning (SRL), a subset of reinforcement learning that emphasizes the safety of the agent during the learning process, focusing on its application in robotics implementing Trust Region Conditional Value at Risk (TRC) algorithm for SRL. The primary objectives are to teach an SRL model to navigate safely in a complex environment and to effectively bridge the sim-to-real gap, allowing for a smooth transfer from computer simulations to real-world environments. The main challenge in SRL is ensuring the agent's safety throughout the learning process, which requires maintaining optimal performance despite the uncertainties and dynamic variables present in real-world environments. For the simulated training, the SafetyGym simulator was used, which is built on the MuJoCo physics engine. When it came to real-world tests, the Robot Operating System (ROS) was the chosen platform, using TurtleBot 2i, a versatile mobile robot platform equipped with a range of sensors, including the SICK TIM551 LiDAR, which has the capability to accurately measure distances for perception purposes. Different methods were explored to address the objectives, with Domain Randomization (DR) emerging as the top choice, a technique that involves randomizing the parameters of the simulation environment during training to help the model generalize better to the real-world. Interestingly, while the model without DR learned three times faster in simulations, it struggled in real-world tests. In the toughest test, it did not succeed even once. In contrast, the model trained with domain randomization passed every time. This model was further refined with real-world training, showing significant improvement in challenging situations. Ultimately, this research highlights the value of DR in ensuring that robots can use what they learn in simulations in the real-world, especially in situations where safety is crucial.
Description
Supervisor
Pajarinen, Joni
Thesis advisor
Terra, Ahmad
Hata, Alberto
Keywords
artificial intelligence, robotics, reinforcement learning, learning, domain randomization, autonomous systems
Other note
Citation
Permanent link to this item
https://urn.fi/URN:NBN:fi:aalto-202401071329
Collections
[dipl] Sähkötekniikan korkeakoulu / ELEC
Endorsement
Review
Supplemented By
Referenced By
Show all metadata
Help
Open Access publishing
Instructions to convert a file to PDF/A
Errata instructions
Send Feedback
Cookie settings
Accessibility settings
Privacy notice
Accessibility Statement
Aalto University Learning Centre