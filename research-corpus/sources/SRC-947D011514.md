> Source: https://epubs.siam.org/doi/10.1137/24M1631250

Skip to main contentSearchSearch
This Journal
Anywhere
Books
Journals
Proceedings
Advanced SearchShopping cart with  0    item Register / Sign In  
 Access via your Institution 
Skip main navigation
Journal Home
Current Issue
All Issues
AboutAbout this Journal
Editorial Policy
Editorial Board
Instructions for Authors
Instructions for Referees
Submit
Subscribe
ShareShare on
Facebook
X
LinkedIn
Email
 Previous article Next articlePolicy Gradient Algorithms for Robust MDP \(\text{s}\)  with Nonrectangular Uncertainty Sets
Authors : Mengmeng   Lihttps://orcid.org/0000-0002-2978-7949Contact the author, Daniel   Kuhnhttps://orcid.org/0000-0003-2697-8886, and Tobias   SutterAuthors Info & Affiliationshttps://doi.org/10.1137/24M1631250Get AccessBibTeXToolsAdd to favorites
Download Citations
Track Citations
Permissions
Reprints
Abstract.
We propose policy gradient algorithms for robust infinite-horizon Markov decision processes (MDPs) with nonrectangular uncertainty sets, thereby addressing an open challenge in the robust MDP literature. Indeed, uncertainty sets that display statistical optimality properties and make optimal use of limited data often fail to be rectangular. Unfortunately, the corresponding robust MDPs cannot be solved with dynamic programming techniques and are in fact provably intractable. We first present a randomized projected Langevin dynamics algorithm that solves the robust policy evaluation problem to global optimality but is inefficient. We also propose a deterministic policy gradient method that is efficient but solves the robust policy evaluation problem only approximately, and we prove that the approximation error scales with a new measure of nonrectangularity of the uncertainty set. Finally, we describe an actor-critic algorithm that finds an  \(\epsilon\) -optimal solution for the robust policy improvement problem in  \(\mathcal O(1/\epsilon^4)\)  iterations. We thus present the first complete solution scheme for robust MDPs with nonrectangular uncertainty sets offering global optimality guarantees. Numerical experiments show that our algorithms compare favorably against state-of-the-art methods.
Keywords
robust Markov decision processes
policy gradient
nonrectangular uncertainty sets
MSC codes
90C17
90C26
Get full access to this article
View all available purchase options and get full access to this article.
Get AccessAcknowledgments.
The authors are indebted to George Lan and Yan Li for helpful comments on an earlier version of this paper, and to Ilyas Fatkhullin for helpful discussions.
References
1. A. Agarwal, S. Kakade, J. Lee, and G. Mahajan, On the theory of policy gradient methods: Optimality, approximation, and distribution shift, J. Mach. Learn. Res., 22 (2021), pp. 1–76.Web of ScienceGoogle Scholar2. J. Altschuler and K. Talwar, Concentration of the Langevin Algorithm’s Stationary DIstribution, preprint, arXiv:2212.12629, 2022.Google Scholar3. T. Archibald, K. McKinnon, and L. Thomas, On the generation of Markov decision processes, J. Oper. Res. Soc., 46 (1995), pp. 354–361, https://doi.org/10.1057/jors.1995.50.Web of ScienceGoogle Scholar4. C. Berge, Topological Spaces: Including a Treatment of Multi-Valued Functions, Vector Spaces, and Convexity, Courier Corporation, New York, 1997.Google Scholar5. D. Bertsekas, Nonlinear Programming, Athena Scientific, Nashua, NH, 2016.Google Scholar6. D. P. Bertsekas and J. Tsitsiklis, Neuro-Dynamic Programming, Athena Scientific, Nashua, NH, 1996.Google Scholar7. J. Bhandari and D. Russo, On the linear convergence of policy gradient methods for finite MDPs, in Proceedings of the International Conference on Artificial Intelligence and Statistics, 2021.Google Scholar8. S. Bhatnagar, R. S. Sutton, M. Ghavamzadeh, and M. Lee, Natural actor-critic algorithms, Automatica J. IFAC, 45 (2009), pp. 2471–2482, https://doi.org/10.1016/j.automatica.2009.07.008.Web of ScienceGoogle Scholar9. P. Billingsley, Statistical Inference for Markov Processes, The University of Chicago Press, Chicago, 1961.Google Scholar10. T. Björk and A. Murgoci, A theory of Markovian time-inconsistent stochastic control in discrete time, Finance Stoch., 18 (2014), pp. 545–592, https://doi.org/10.1007/s00780-014-0234-y.Web of ScienceGoogle Scholar11. J. Blanchet, M. Lu, T. Zhang, and H. Zhong, Double Pessimism is provably efficient for distributionally Robust offline reinforcement learning: Generic algorithm and Robust partial coverage, in Proceedings of Advances in Neural Information Processing Systems, 2023.Google Scholar12. J. Chae, S. Han, W. Jung, M. Cho, S. Choi, and Y. Sung, Robust imitation learning against variations in environment dynamics, in Proceedings of the International Conference on Machine Learning, 2022.Google Scholar13. C. Daskalakis, D. J. Foster, and N. Golowich, Independent policy gradient methods for competitive reinforcement learning, in Proceedings of Advances in Neural Information Processing Systems, 2020.Google Scholar14. D. Davis and D. Drusvyatskiy, Stochastic model-based minimization of weakly convex functions, SIAM J. Optim., 29 (2019), pp. 207–239, https://doi.org/10.1137/18M1178244.AbstractWeb of ScienceGoogle Scholar15. E. Delage and S. Mannor, Percentile optimization for Markov decision processes with parameter uncertainty, Oper. Res., 58 (2010), pp. 203–213, https://doi.org/10.1287/opre.1080.0685.Web of ScienceGoogle Scholar16. J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, Efficient projections onto the  \(\ell_1\) -ball for learning in high dimensions, in Proceedings of the International Conference on Machine Learning, 2008.Google Scholar17. M. Frank and P. Wolfe, An algorithm for quadratic programming, Naval Res. Logist., 3 (1956), pp. 95–110, https://doi.org/10.1002/nav.3800030109.Google Scholar18. J. Goh, M. Bayati, S. Zenios, S. Singh, and D. Moore, Data uncertainty in Markov chains: Application to cost-effectiveness analyses of medical innovations, Oper. Res., 66 (2018), pp. 697–715, https://doi.org/10.1287/opre.2017.1685.Web of ScienceGoogle Scholar19. H. Gong and M. Wang, A duality approach for regret minimization in average-award ergodic Markov decision processes, in Proceedings of the 2nd Conference on Learning for Dynamics and Control, 2020.Google Scholar20. V. Goyal and J. Grand-Clement, Robust Markov decision processes: Beyond rectangularity, Math. Oper. Res., 48 (2022), pp. 203–226, https://doi.org/10.1287/moor.2022.1259.Web of ScienceGoogle Scholar21. J. Grand-Clément and M. Petrik, On the Convex Formulations of Robust Markov Decision Processes, Math. Oper. Res., 50 (2024), pp. 1681–1706.CrossrefWeb of ScienceGoogle Scholar22. O. Hernández-Lerma and J. Lasserre, Discrete-Time Markov Control Processes: Basic Optimality Criteria, Springer, New York, 1996.CrossrefGoogle Scholar23. C.-R. Hwang, Laplace’s method revisited: Weak convergence of probability measures, Ann. Probab., 8 (1980), pp. 1177–1182, https://doi.org/10.1214/aop/1176994579.Web of ScienceGoogle Scholar24. G. Iyengar, Robust dynamic programming, Math. Oper. Res., 30 (2005), pp. 257–280, https://doi.org/10.1287/moor.1040.0129.Web of ScienceGoogle Scholar25. S. Kakade and J. Langford, Approximately optimal approximate reinforcement learning, in Proceedings of the International Conference on Machine Learning, 2002.Google Scholar26. A. Lamperski, Projected stochastic gradient Langevin algorithms for constrained sampling and non-convex learning, in Proceedings of the Conference on Learning Theory, 2021.Google Scholar27. Y. Le Tallec, Robust, Risk-Sensitive, and Data-Driven Control of Markov Decision Processes, Ph.D. thesis, Massachusetts Institute of Technology, 2007.Google Scholar28. N. Lesmana, H. Su, and C. S. Pun, Reinventing policy iteration under time inconsistency, Trans. Mach. Learn. Res., 11 (2022).Google Scholar29. M. Li, T. Sutter, and D. Kuhn, Distributionally robust optimization with Markovian data, in Proceedings of the International Conference on Machine Learning, 2021.Google Scholar30. Y. Li and G. Lan, First-Order Policy Optimization for Robust Policy Evaluation, preprint, arXiv:2307.15890, 2023.Google Scholar31. Y. Li, T. Zhao, and G. Lan, First-Order Policy Optimization for Robust Markov Decision Process, preprint, arXiv:2209.10579, 2022.Google Scholar32. F. Liese and K.-J. Miescke, Statistical Decision Theory: Estimation, Testing, and Selection, Springer, New York, 2008.Google Scholar33. T. Lin, C. Jin, and M. I. Jordan, Two-timescale gradient descent ascent algorithms for nonconvex minimax optimization, J. Mach. Learn. Res., 26 (2025), pp. 1–45.Google Scholar34. J. Liu and J. Ye, Efficient Euclidean projections in linear time, in Proceedings of the International Conference on Machine Learning, 2009.Google Scholar35. G. Loomes and R. Sugden, Disappointment and dynamic consistency in choice under uncertainty, Rev. Econom. Stud., 53 (1986), pp. 271–282, https://doi.org/10.2307/2297651.Web of ScienceGoogle Scholar36. S. Mannor, O. Mebel, and H. Xu, Robust MDPs with k-rectangular uncertainty, Math. Oper. Res., 41 (2016), pp. 1484–1509, https://doi.org/10.1287/moor.2016.0786.Web of ScienceGoogle Scholar37. S. Meyn, Control Systems and Reinforcement Learning, Cambridge University Press, Cambridge, 2022.CrossrefGoogle Scholar38. A. Nilim and L. El Ghaoui, Robust control of Markov decision processes with uncertain transition matrices, Oper. Res., 53 (2005), pp. 780–798, https://doi.org/10.1287/opre.1050.0216.Web of ScienceGoogle Scholar39. M. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming, Wiley, New York, 2005.Google Scholar40. G. O. Roberts and R. L. Tweedie, Exponential convergence of Langevin distributions and their discrete approximations, Bernoulli, 2 (1996), pp. 341–363, https://doi.org/10.2307/3318418.Google Scholar41. R. T. Rockafellar, Convex Analysis, Princeton University Press, Princeton, NJ, 1970.CrossrefGoogle Scholar42. A. Shapiro, Time consistency of dynamic risk measures, Oper. Res. Lett., 40 (2012), pp. 436–439, https://doi.org/10.1016/j.orl.2012.08.007.Web of ScienceGoogle Scholar43. A. Shapiro, Rectangular sets of probability measures, Oper. Res., 64 (2016), pp. 528–541, https://doi.org/10.1287/opre.2015.1466.Web of ScienceGoogle Scholar44. S. Sun, R. Wang, and B. An, Reinforcement learning for quantitative trading, ACM Trans. Intel. Syst. Technol., 14 (2023), pp. 1–29, https://doi.org/10.1145/3582560.Web of ScienceGoogle Scholar45. T. Sutter, B. P. G. V. Parys, and D. Kuhn, A Pareto dominance principle for data-driven optimization, Oper. Res., 72 (2024), pp. 1976–1999, https://doi.org/10.1287/opre.2021.0609.Web of ScienceGoogle Scholar46. R. Sutton and A. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA, 2018.Google Scholar47. R. Sutton, D. McAllester, S. Singh, and Y. Mansour, Policy gradient methods for reinforcement learning with function approximation, in Proceedings of Advances in Neural Information Processing Systems, 1999.Google Scholar48. K. K. Thekumparampil, P. Jain, P. Netrapalli, and S. Oh, Efficient algorithms for smooth minimax optimization, in Proceedings of Advances in Neural Information Processing Systems, 2019.Google Scholar49. I. Usmanova, M. Kamgarpour, A. Krause, and K. Levy, Fast projection onto convex smooth constraints, in Proceedings of the International Conference on Machine Learning, 2021.Google Scholar50. L. Viano, Y.-T. Huang, P. Kamalaruban, C. Innes, S. Ramamoorthy, and A. Weller, Robust learning from observation with model misspecification, in Proceedings of the International Conference on Autonomous Agents and Multiagent Systems, 2022.Google Scholar51. L. Viano, Y.-T. Huang, P. Kamalaruban, A. Weller, and V. Cevher, Robust inverse reinforcement learning under transition dynamics mismatch, in Proceedings of Advances in Neural Information Processing Systems, 2021.Google Scholar52. J. Wang, J. Zhang, H. Jiang, J. Zhang, L. Wang, and C. Zhang, Offline meta reinforcement learning with in-distribution online adaptation, in Proceedings of the International Conference on Machine Learning, 2023.Google Scholar53. Q. Wang, C. P. Ho, and M. Petrik, Policy gradient in robust MDPs with global convergence guarantee, in Procedings of the International Conference on Machine Learning, 2023.Google Scholar54. Q. Wang, S. Xu, C. P. Ho, and M. Petrik, Policy Gradient for Robust Markov Decision Processes, preprint, arXiv:2410.22114, 2024.Google Scholar55. W. Wang and M. A. Carreira-Perpinán, Projection onto the Probability Simplex: An Efficient Algorithm with a Simple Proof, and an Application, preprint, https://arxiv.org/abs/1309.1541, 2013.Google Scholar56. Y. Wang and S. Zou, Policy gradient method for robust reinforcement learning, in Proceedings of the International Conference on Machine Learning, 2022.Google Scholar57. C. White and H. Eldeib, Markov decision processes with imprecise transition probabilities, Oper. Res., 42 (1994), pp. 739–749, https://doi.org/10.1287/opre.42.4.739.Web of ScienceGoogle Scholar58. W. Wiesemann, private communication, (2023).Google Scholar59. W. Wiesemann, D. Kuhn, and B. Rustem, Robust Markov decision processes, Math. Oper. Res., 38 (2013), pp. 153–183, https://doi.org/10.1287/moor.1120.0566.Web of ScienceGoogle Scholar60. Z. Zhou, Time inconsistency, precommitment, and equilibrium strategies for a Stackelberg game, SIAM J. Control Optim., 61 (2023), pp. 361–397, https://doi.org/10.1137/22M1477659.AbstractWeb of ScienceGoogle ScholarInformation & Authors
Information
Published In
SIAM Journal on OptimizationVolume  36  •  Issue  1  •  March 2026Pages :  120  -  151 DOI : 10.1137/24M1631250ISSN (online) :  1095-7189
Copyright
© 2026 Society for Industrial and Applied Mathematics.
History
Submitted: 22 January 2024Accepted: 23 September 2025Published online: 9 February 2026
Permissions
Request permissions for this article.Request PermissionsKeywords
robust Markov decision processes
policy gradient
nonrectangular uncertainty sets
MSC codes
90C17
90C26
Authors
Affiliations
Mengmeng   Li  https://orcid.org/0000-0002-2978-7949Contact the authorRisk Analytics and Optimization Chair, EPFL, 1015 Lausanne, Switzerland.View all articles by this authorDaniel   Kuhn  https://orcid.org/0000-0003-2697-8886Risk Analytics and Optimization Chair, EPFL, 1015 Lausanne, Switzerland.View all articles by this authorTobias   Sutter Department of Economics, University of St. Gallen, 9000 St. Gallen, Switzerland.View all articles by this authorFunding Information
National Center of Competence in ResearchSchweizerischer Nationalfonds zur Förderung der Wissenschaftlichen Forschung (SNF): 51NF40_180545Funding: This work was supported as a part of the NCCR Automation, a National Center of Competence in Research, funded by the Swiss National Science Foundation (grant 51NF40_225155).
Metrics & Citations
Metrics
Citations
 If you have the appropriate software installed, you can download article citation data to the citation manager of your choice. Simply select your manager software from the list below and click Download. 
 Direct import 
Cited By
There are no citations for this item
View Options
Purchase Save for later  Item saved, go to cart 
 Article Pay-Per-View  $42.00    Add to cart 
 Article Pay-Per-View  Checkout Access via your Institution
Questions about how to access this content? Contact SIAM at [email protected].
View options
PDF
View PDF Full Text
View Full TextFigures
Tables
Media
Share
Share
Copy the content Link
Copied!
Copying failed.
Share with email
Email a colleagueShare on social media
FacebookX (formerly Twitter)LinkedInemail Recommended Content 
View full text|Download PDFNow Reading:Share
PREVIOUS ARTICLE
Exploring Chordal Sparsity in Semidefinite Programming with Sparse plus Low-Rank Data MatricesPreviousNEXT ARTICLE
Optimization on a Finer Scale: Bounded Local Subgradient Variation Perspective NextFigure title goes hereGo to this figure within the textDownload figureShare on social mediaxrefBack.goTo
Request permissionsAuthors Info & Affiliations Previous article Next articleSociety for Industrial and 
  Applied Mathematics  
Society for Industrial and Applied Mathematics
 3600 Market Street, 6th Floor 
  Philadelphia, PA 19104 
  USA 
© 2026 Society for Industrial and Applied Mathematics
 Browse 
 Browse 
Journals
E-books
Bookstore
Proceedings
 Alerts 
 Alerts 
Sign up/Manage Email Alerts
 Information 
 Information 
For Journal Authors
For Book Authors
For Librarians
Help
Terms of Use & Privacy Policy
Accessibility Statement
 About 
 About 
SIAM
Join SIAM
Donate to SIAM
Request Username
Can't sign in? Forgot your username?
Enter your email address below and we will send you your username
CloseIf the address matches an existing account you will receive an email with instructions to retrieve your username
Register
 Already have an account? Change Password 
Too Short   Weak   Medium   Strong   Very Strong   Too Long  
 Your password must have 2 characters or more and contain 3 of the following: 
a lower case character, 
an upper case character, 
a special character 
or a digit  
Too Short  
Password Changed Successfully
Your password has been changed
Login
Forgot your password?Create Account Create Account  Log in via your institution Can't sign in? Forgot your password?
Enter your email address below and we will send you the reset instructions
CancelIf the address matches an existing account you will receive an email with instructions to reset your password
CloseVerify Phone
CancelCongrats!
Your Phone has been verified