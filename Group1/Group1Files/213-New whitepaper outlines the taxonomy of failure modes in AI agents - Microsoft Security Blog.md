> Source: https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/

Skip to main contentMicrosoft  Microsoft Security  Microsoft Security  
AI-powered cybersecurity
Cloud security
Data security & governance
Identity & network access
Privacy & risk management
Security for AI
Unified SecOps
Zero Trust
Product families  
Microsoft Defender
Microsoft Entra
Microsoft Intune
Microsoft Priva
Microsoft Purview
Microsoft Sentinel
Security AI  
Microsoft Security Copilot
Identity & access  
Microsoft Entra ID (Azure Active Directory)
Microsoft Entra Agent ID
Microsoft Entra External ID
Microsoft Entra ID Governance
Microsoft Entra ID Protection
Microsoft Entra Internet Access
Microsoft Entra Private Access
Microsoft Entra Permissions Management
Microsoft Entra Verified ID
Microsoft Entra Workload ID
Microsoft Entra Domain Services
Azure Key Vault
SIEM & XDR  
Microsoft Sentinel
Microsoft Defender for Cloud
Microsoft Defender XDR
Microsoft Defender for Endpoint
Microsoft Defender for Office 365
Microsoft Defender for Identity
Microsoft Defender for Cloud Apps
Microsoft Security Exposure Management
Microsoft Defender Vulnerability Management
Microsoft Defender Threat Intelligence
Cloud security  
Microsoft Defender for Cloud
Microsoft Defender Cloud Security Posture Mgmt
Microsoft Defender External Attack Surface Management
Azure Firewall
Azure Web App Firewall
Azure DDoS Protection
GitHub Advanced Security
Endpoint security & management  
Microsoft Defender for Endpoint
Microsoft Defender XDR
Microsoft Defender for Business
Microsoft Intune core capabilities
Microsoft Defender for IoT
Microsoft Defender Vulnerability Management
Microsoft Intune Advanced Analytics
Microsoft Intune Endpoint Privilege Management
Microsoft Intune Enterprise Application Management
Microsoft Intune Remote Help
Microsoft Cloud PKI
Compliance & privacy  
Microsoft Purview Communication Compliance
Microsoft Purview Compliance Manager
Microsoft Purview Data Lifecycle Management
Microsoft Purview eDiscovery 
Microsoft Purview Audit
Microsoft Priva Risk Management
Microsoft Priva Subject Rights Requests
Data security & governance  
Microsoft Purview Information Protection
Microsoft Purview Insider Risk Management
Microsoft Purview Data Loss Prevention
Microsoft Purview Data Governance
Pricing
Microsoft Defender Experts for XDR
Microsoft Defender Experts for Hunting
Microsoft Incident Response
Partners
Get started  
Cybersecurity awareness
Customer stories
Security 101
Product trials
How we protect Microsoft
Reports and analysis  
Industry recognition
Microsoft Security Insider
Microsoft Digital Defense Report
Security Response Center
Community  
Microsoft Security Blog
Microsoft Security Events
Microsoft Tech Community
Documentation and training  
Documentation
Technical Content Library
Training & certifications
Additional sites  
Compliance Program for Microsoft Cloud
Microsoft Trust Center
Security Engineering Portal
Service Trust Portal
Microsoft Secure Future Initiative
Business Solutions Hub
Contact Sales
Start free trial
Global
Microsoft Security
Azure
Dynamics 365
Microsoft 365
Microsoft Teams
Windows 365
Tech & innovation  
Microsoft Cloud
AI
Azure Space
Mixed reality
Microsoft HoloLens
Microsoft Viva
Quantum computing
Sustainability
Industries  
Education
Automotive
Financial services
Government
Healthcare
Manufacturing
Retail
All industries
Partners  
Find a partner
Become a partner
Partner Network
Microsoft Marketplace
Marketplace Rewards
Software development companies
Resources  
Blog
Microsoft Advertising
Developer Center
Documentation
Events
Licensing
Microsoft Learn
Microsoft Research
View Sitemap
No results
Best practices
 April 24 
 4 min read 
 New whitepaper outlines the taxonomy of failure modes in AI agents 
 By Ram Shankar Siva Kumar, Data Cowboy, AI Red Team 
/  Powered by Microsoft Copilot  
Share
 Link copied to clipboard! 
Content types
Best practices
Topics
AI and agents
We are releasing a taxonomy of failure modes in AI agents to help security professionals and machine learning engineers think through how AI systems can fail and design them with safety and security in mind.
The taxonomy continues Microsoft AI Red Team’s work to lead the creation of systematization of failure modes in AI; in 2019, we published one of the earliest industry efforts enumerating the failure modes of traditional AI systems. In 2020, we partnered with MITRE and 11 other organizations to codify the security failures in AI systems as Adversarial ML Threat Matrix, which has now evolved into MITRE ATLAS™. This effort is another step in helping the industry think through what the safety and security failures in the fast-moving and highly impactful agentic AI space are.
Taxonomy of Failure Mode in Agentic AI Systems
Microsoft’s new whitepaper explains the taxonomy of failure modes in AI agents, aimed at enhancing safety and security in AI systems.
Read the whitepaperTo build out this taxonomy and ensure that it was grounded in concrete and realistic failures and risk, the Microsoft AI Red Team took a three-prong approach:
We catalogued the failures in agentic systems based on Microsoft’s internal red teaming of our own agent-based AI systems.
Next, we worked with stakeholders across the company—Microsoft Research, Microsoft AI, Azure Research, Microsoft Security Response Center, Office of Responsible AI, Office of the Chief Technology Officer, other Security Research teams, and several organizations within Microsoft that are building agents to vet and refine this taxonomy.
To make this useful to those outside of Microsoft, we conducted systematic interviews with external practitioners working on developing agentic AI systems and frameworks to polish the taxonomy further.
To help frame this taxonomy in a real-world application for readers, we also provide a case study of the taxonomy in action. We take a common agentic AI feature of memory and we walk through how an cyberattacker could corrupt an agent’s memory and use that as a pivot point to exfiltrate data.
Figure 1. Failure modes in agentic AI systems.
Core concepts in the taxonomy
While identifying and categorizing the different failure modes, we broke them down across two pillars, safety and security.
Security failures are those that result in core security impacts, namely a loss of confidentiality, availability, or integrity of the agentic AI system; for example, such a failure allowing a threat actor to alter the intent of the system.
Safety failure modes are those that affect the responsible implementation of AI, often resulting in harm to the users or society at large; for example, a failure that causes the system to provide differing quality of service to different users without explicit instructions to do so.
We then mapped the failures along two axes—novel and existing.
Novel failure modes are unique to agentic AI and have not been observed in non-agentic generative AI systems, such as failures that occur in the communication flow between agents within a multiagent system.
Existing failure modes have been observed in other AI systems, such as bias or hallucinations, but gain in importance in agentic AI systems due to their impact or likelihood.
As well as identifying the failure modes, we have also identified the effects these failures could have on the systems they appear in and the users of them. Additionally we identified key practices and controls that those building agentic AI systems should consider to mitigate the risks posed by these failure modes, including architectural approaches, technical controls, and user design approaches that build upon Microsoft’s experience in securing software as well as generative AI systems.
The taxonomy provides multiple insights for engineers and security professionals. For instance, we found that memory poisoning is particularly insidious in AI agents, with the absence of robust semantic analysis and contextual validation mechanisms allows malicious instructions to be stored, recalled, and executed. The taxonomy provides multiple strategies to combat this, such as limiting the agent’s ability to autonomously store memories by requiring external authentication or validation for all memory updates, limiting which components of the system have access to the memory, and controlling the structure and format of items stored in memory.
Read the new “Taxonomy of Failure Mode in Agentic AI Systems” whitepaperHow to use this taxonomy
For engineers building agentic systems: 
We recommend that this taxonomy is used as part of designing the agent, augmenting the existing Security Development Lifecycle and threat modeling practice. The guide helps walk through the different harms and the potential impact.
For each harm category, we provide suggested mitigation strategies that are technology agnostic to kickstart the process.
For security and safety professionals: 
This is a guide on how to probe AI systems for failures before the system launches. It can be used to generate concrete attack kill chains to emulate real world cyberattackers.
This taxonomy can also be used to help inform defensive strategies for your agentic AI systems, including providing inspiration for detection and response opportunities.
For enterprise governance and risk professionals, this guide can help provide an overview of not just the novel ways these systems can fail but also how these systems inherit the traditional and existing failure modes of AI systems.
Learn more
Like all taxonomies, we consider this a first iteration and hope to continually update it, as we see the agent technology and cyberthreat landscape change. If you would like to contribute, please reach out to airt-agentsafety@microsoft.com.
To learn more about Microsoft Security solutions, visit our website. Bookmark the Security blog to keep up with our expert coverage on security matters. Also, follow us on LinkedIn (Microsoft Security) and X (@MSFTSecurity) for the latest news and updates on cybersecurity.
The taxonomy was led by Pete Bryan; the case study on poisoning memory was led by Giorgio Severi. Others that contributed to this work: Joris de Gruyter, Daniel Jones, Blake Bullwinkel, Amanda Minnich, Shiven Chawla, Gary Lopez, Martin Pouliot, Whitney Maxwell, Katherine Pratt, Saphir Qi, Nina Chikanov, Roman Lutz, Raja Sekhar Rao Dheekonda, Bolor-Erdene Jagdagdorj, Eugenia Kim, Justin Song, Keegan Hines, Daniel Jones, Richard Lundeen, Sam Vaughan, Victoria Westerhoff, Yonatan Zunger, Chang Kawaguchi, Mark Russinovich, Ram Shankar Siva Kumar.
Follow on LinkedIn  
 Ram Shankar Siva Kumar 
 Data Cowboy, AI Red Team 
 See Ram Shankar Siva Kumar posts Related posts
 November 21 
 4 min read 
 Microsoft named a Leader in the Gartner® Magic Quadrant™ for Access Management for the ninth consecutive year 
 We’re happy to share that Microsoft has been recognized as a Leader in the 2025 Gartner® Magic Quadrant™ for Access Management for the ninth consecutive year. 
 November 18 
 9 min read 
 Ambient and autonomous security for the agentic era 
 In the agentic era, security must be ambient and autonomous, like the AI it protects. This is our vision for security, where security becomes the core primitive. 
 November 18 
 5 min read 
 Agents built into your workflow: Get Security Copilot with Microsoft 365 E5 
 At Microsoft Ignite 2025, we are not just announcing new features—we are redefining what’s possible, empowering security teams to shift from reactive responses to proactive strategies. 
Get started with Microsoft Security
Protect your people, data, and infrastructure with AI-powered, end-to-end security from Microsoft.
Learn howConnect with us on social
X
YouTube
LinkedIn
English (United States)Your Privacy Choices Opt-Out Icon   Your Privacy Choices  Consumer Health Privacy  