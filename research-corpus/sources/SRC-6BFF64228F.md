> Source: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-160.html

Sequential Decision Making under Uncertainty: Optimality Guarantees, Compositional Learning, and Applications to Robotics and Ecology | EECS at UC Berkeley
Skip to Content
Expand Search Form Collapse Search Form Expand Main Menu Collapse Main Menu
Search for: Search
For Students
For Faculty/Staff
Industry
News
Events
Give
Search for: Search
About About Expand Submenu About
About Overview
History Expand Submenu
The First Women of EECS
Joseph Thomas Gier
Diversity Expand Submenu
Hear From Women in EECS
Broadening Participation in EECS
Visiting
By the Numbers
Special Events Expand Submenu
2022-23
2020-21
2019-20
2018-19
2017-18
 The Department of Electrical Engineering and Computer Sciences (EECS) at UC Berkeley offers one of the strongest research and instructional programs in this field anywhere in the world. Blog
Academics Academics Expand Submenu Academics
Academics Overview
Undergraduate Admissions & Programs Expand Submenu
CS Major
EECS Major
EECS/CS Program Comparison Chart
Second Bachelor's Degree
Summer Research
Cal Day
Graduate Admissions & Programs Expand Submenu
Grad Admissions FAQ
Industry-Oriented Programs
Research-Oriented Programs
Fellowships
Adding the EECS/CS M.S. From Another Department
Recommended Coursework
For Current Students Expand Submenu
ed | EECS 101
Courses Expand Submenu
EE Courses
CS Courses
 Unlike many institutions of similar stature, regular EE and CS faculty teach the vast majority of our courses, and the most exceptional teachers are often also the most exceptional researchers. View Courses
Research Research Expand Submenu Research
Research Overview
Areas
Centers & Labs
Colloquium Expand Submenu
Archive
BEARS Symposium Expand Submenu
Archive
Technical Reports
Ph.D. Dissertations
 Research is the foundation of Berkeley EECS. Faculty, students, and staff work together on cutting-edge projects that cross disciplinary boundaries to improve everyday life and make a difference. EECS Research
People People Expand Submenu People
People Overview
Directory
Leadership
Faculty Expand Submenu
In Memoriam
Students Expand Submenu
Student Awards
Student Organizations
Staff Expand Submenu
Student Affairs
Faculty Support
Course Support
Facilities and Engineering Services
Financial Services
HR
IT Support
Industrial & Public Relations
Alumni Expand Submenu
EE Distinguished Alumni
CS Distinguished Alumni
 EECS faculty, students, staff, and alumni are central to our success as one of the most thriving and distinguished departments on the Berkeley campus. Latest News
Connect Connect Expand Submenu Connect
Connect Overview
Support EECS Expand Submenu
EECS Excellence Fund
Memorial Funds
K-12 Outreach
Student Affairs
Faculty Positions
Staff Positions
Contact Expand Submenu
In an Emergency
 Consider reaching out for a conversation, attending a department seminar or conference, viewing a lecture on any one of our public channels, or supporting us via a gift to the university. You can help strengthen our dedication to education and outreach, solidify close ties to industry, and nourish a supportive and inclusive culture. Contact us
Home / Research / Technical Reports / Sequential Decision Making under Uncertainty: Optimality Guarantees, Compositional Learning, and Applications to Robotics and Ecology
Sequential Decision Making under Uncertainty: Optimality Guarantees, Compositional Learning, and Applications to Robotics and Ecology
Michael Lim
EECS Department, University of California, Berkeley
Technical Report No. UCB/EECS-2023-160
May 12, 2023
This publication is archived. It is kept only for reference purposes, so it is no longer being updated and may not meet accessibility standards. If you need this content in a different format, please email webteam@eecs.berkeley.edu.
http://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/Archive/EECS-2023-160.pdf
Sequential decision making under uncertainty problems often deal with partially observable Markov decision processes (POMDPs). POMDPs mathematically capture making decisions at each step while accounting for potential rewards and uncertainties an agent may encounter in the future, which make them desirable and flexible representations of many real world problems. However, such sequential decision making problems with various sources of uncertainty are notoriously difficult to solve, especially when the state and observation spaces are continuous or hybrid, which is often the case for physical systems. Furthermore, modern problem settings require sophisticated machine learning techniques to effectively handle complex data structures like image, text or audio inputs, while performing complicated reasoning such as localizing with noisy camera images or predicting intentions and locations of other agents. Modern approaches that involve artificial intelligence and machine learning methods provide powerful computational resources that can effectively manage the above challenges. Many of these decision making algorithms and machine learning techniques can either capture rigorous theoretical guarantees or empirical performance, but few capture both.
This dissertation aims to lay the foundations to study sequential decision making under uncertainty from multiple angles: theoretical guarantees, integration with learning, and real world applications. We strike a balance between mathematical analysis of the foundational framework of POMDPs, and enabling and deploying these techniques via integration with machine learning techniques through compositional learning.
We first begin the theoretical portion of the dissertation by analyzing novel POMDP solvers and their theoretical convergence properties. This portion introduces a several novel POMDP algorithms that serve as foundations for studying convergence properties of modern POMDP algorithms when dealing with continuous observation and action spaces. Then, we cover a more general result that provides theoretical guarantees and justification for solving the particle belief approximation of POMDPs while retaining guarantees in the original POMDP. This result formally justifies a common POMDP approximation technique known as the particle likelihood weighting, which is the first-of-its-kind in theoretically explaining a family of modern POMDP algorithms that use this technique.
Then, we introduce approaches to integrate model-based planning with learning-based components via compositional learning for real world robotic settings. First, we study how to integrate the aforementioned POMDP planning algorithms with machine learning components by using deep generative models, which enables these algorithms to tackle visual navigation tasks. Second, we substantially extend a robotic arm manipulation algorithm for tabletop manipulation through reasoning with demonstration sequences and weighted multi-task learning.
Lastly, we propose a novel application area of sequential decision making in ecological sub-field of community state navigation. Specifically, we focus on formulating the species coexistence navigation problem as an optimal path planning problem. This approach allows us to understand the population dynamics by analyzing small perturbations to the equilibrium states and subsequently find action sequences that allow efficient navigation. We also discuss the benefits and impact of applying sequential decision making framework to community state navigation problems and beyond.
Afterwards, we summarize the main contributions once again and contextualize the novel contributions. We also discuss some opportunities for future works in sequential decision making under uncertainty, in terms of new theoretical developments, alternative approaches for compositional learning, and other avenues for impactful real world applications.
Advisors: Claire Tomlin
BibTeX citation:
EndNote citation:
About
History
Diversity
Visiting
Special Events
People
Directory
Leadership
Faculty
Staff
Students
Alumni
Connect
Support Us
K-12 Outreach
Faculty Positions
Staff Positions
Contact
Academics
Undergrad Admissions & Programs
Graduate Admissions & Programs
Courses
Prospective Women Students
Current Students
Resources
Room Reservations
My EECS Info
For Students
For Grads
For Undergrads
For ASEs
IT Services
Facilities/Safety
For Faculty/Staff
Visiting Scholars
Research
Areas
Centers & Labs
Projects
Technical Reports
PhD Dissertations
Joint Colloquium
BEARS Symposium
Industry
Recruit Students
Corporate Access
Learn more about the Campaign for Berkeley and Graduate Fellowships.
Give to EECS
Berkeley EECS on Twitter
Berkeley EECS on Instagram
Berkeley EECS on LinkedIn
Berkeley EECS on YouTube
EE
CS
UC Berkeley
Berkeley Engineering
CDSS
Accessibility
Nondiscrimination
Privacy
Contact
© 2023 UC Regents