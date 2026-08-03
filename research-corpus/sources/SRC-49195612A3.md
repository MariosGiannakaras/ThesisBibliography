# AI Agents Need Data Integrity - Schneier on Security

# Schneier on Security

### Search

- Powered by [DuckDuckGo](https://duckduckgo.com/)

### Subscribe

- [Home](https://duckduckgo.com/)[Blog](https://duckduckgo.com/)

## AI Agents Need Data Integrity

- Think of the Web as a digital territory with its own social contract. In 2014, [Tim Berners-Lee](https://spectrum.ieee.org/the-fathers-of-the-internet-revolution-urge-todays-pioneers-to-reinvent-the-web) called for a [“Magna Carta for the Web”](https://www.theguardian.com/technology/2014/mar/12/online-magna-carta-berners-lee-web) to restore the balance of power between individuals and institutions. This mirrors the original charter’s purpose: ensuring that those who occupy a territory have a meaningful stake in its governance.

- [Web 3.0](https://www.theguardian.com/technology/2014/mar/12/online-magna-carta-berners-lee-web)—the distributed, [decentralized Web](https://spectrum.ieee.org/tag/decentralized-web) of tomorrow—is finally poised to change the Internet’s dynamic by returning ownership to data creators. This will change many things about what’s often described as the “CIA triad” of [digital security](https://spectrum.ieee.org/tag/digital-security): confidentiality, integrity, and availability. Of those three features, data integrity will become of paramount importance.

- When we have agency in digital spaces, we naturally maintain their integrity—protecting them from deterioration and shaping them with intention. But in territories controlled by distant platforms, where we’re merely temporary visitors, that connection frays. A disconnect emerges between those who benefit from data and those who bear the consequences of compromised integrity. Like homeowners who care deeply about maintaining the property they own, users in the Web 3.0 paradigm will become stewards of their personal digital spaces.

- This will be critical in a world where [AI agents](https://spectrum.ieee.org/tag/ai-agents) don’t just answer our questions but act on our behalf. These agents may execute financial transactions, coordinate complex workflows, and autonomously operate critical infrastructure, making decisions that ripple through entire industries. As digital agents become more autonomous and interconnected, the question is no longer whether we will trust AI but what that trust is built upon. In the new age we’re entering, the foundation isn’t intelligence or efficiency—it’s integrity.

### What Is Data Integrity?

- In information systems, integrity is the guarantee that data will not be modified without authorization, and that all transformations are verifiable throughout the data’s life cycle. While availability ensures that systems are running and confidentiality prevents unauthorized access, integrity focuses on whether information is accurate, unaltered, and consistent across systems and over time.

- It’s a new idea. The undo button, which prevents accidental data loss, is an integrity feature. So is the reboot process, which returns a computer to a known good state. Checksums are an integrity feature; so are verifications of network transmission. Without integrity, security measures can backfire. Encrypting corrupted data just locks in errors. Systems that score high marks for availability but spread [misinformation](https://spectrum.ieee.org/tag/misinformation) just become [amplifiers](https://spectrum.ieee.org/tag/amplifiers) of risk.

- All [IT systems](https://spectrum.ieee.org/tag/it-systems) require some form of data integrity, but the need for it is especially pronounced in two areas today. First: [Internet of Things](https://spectrum.ieee.org/tag/internet-of-things) devices interact directly with the physical world, so corrupted input or output can result in real-world harm. Second: AI systems are only as good as the integrity of the data they’re trained on, and the integrity of their decision-making processes. If that foundation is shaky, the results will be too.

- Integrity manifests in four key areas. The first, *input integrity,* concerns the quality and authenticity of data entering a system. When this fails, consequences can be severe. In 2021, [Facebook’s global outage](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) was triggered by a single mistaken command—an input error missed by automated systems. Protecting input integrity requires robust [authentication](https://spectrum.ieee.org/tag/authentication) of data sources, cryptographic signing of sensor data, and diversity in input channels for cross-validation.

- The second issue is *processing integrity,* which ensures that systems transform inputs into outputs correctly. In 2003, the [U.S.-Canada blackout](https://www.nerc.com/pa/rrm/ea/Documents/August_2003_Blackout_Final_Report.pdf) affected 55 million people when a control-room process failed to refresh properly, resulting in damages exceeding US $6 billion. Safeguarding processing integrity means formally verifying algorithms, cryptographically protecting models, and monitoring systems for anomalous behavior.

- *Storage integrity* covers the correctness of information as it’s stored and communicated. In 2023, the Federal Aviation Administration was [forced to halt](https://www.thestack.technology/faa-outage-cause-notam-database-file-not-cyber/) all U.S. departing flights because of a corrupted database file. Addressing this risk requires cryptographic approaches that make any modification computationally infeasible without detection, distributed storage systems to prevent single points of failure, and rigorous backup procedures.

- Finally, *contextual integrity* addresses the appropriate flow of information according to the norms of its larger context. It’s not enough for data to be accurate; it must also be used in ways that respect expectations and boundaries. For example, if a smart speaker listens in on casual family conversations and uses the data to build advertising profiles, that action would violate the expected boundaries of [data collection](https://spectrum.ieee.org/tag/data-collection). Preserving contextual integrity requires clear data-governance policies, principles that limit the use of data to its intended purposes, and mechanisms for enforcing information-flow constraints.

- As AI systems increasingly make critical decisions with reduced human oversight, all these dimensions of integrity become critical.

### The Need for Integrity in Web 3.0

- As the digital landscape has shifted from Web 1.0 to [Web 2.0](https://spectrum.ieee.org/tag/web-2-0) and now evolves toward Web 3.0, we’ve seen each era bring a different emphasis in the [CIA triad](https://www.fortinet.com/resources/cyberglossary/cia-triad) of confidentiality, integrity, and availability.

- Returning to our home metaphor: When simply having shelter is what matters most, availability takes priority—the house must exist and be functional. Once that foundation is secure, confidentiality becomes important—you need locks on your doors to keep others out. Only after these basics are established do you begin to consider integrity, to ensure that what’s inside the house remains trustworthy, unaltered, and consistent over time.

- Web 1.0 of the 1990s prioritized making information available. Organizations digitized their content, putting it out there for anyone to access. In Web 2.0, the Web of today, platforms for [e-commerce](https://spectrum.ieee.org/tag/e-commerce), [social media](https://spectrum.ieee.org/tag/social-media), and [cloud computing](https://spectrum.ieee.org/tag/cloud-computing) prioritize confidentiality, as [personal data](https://spectrum.ieee.org/tag/personal-data) has become the Internet’s currency.

- Somehow, integrity was largely lost along the way. In our current Web architecture, where control is centralized and removed from individual users, the concern for integrity has diminished. The massive social media platforms have created environments where no one feels responsible for the truthfulness or quality of what circulates.

- Web 3.0 is poised to change this dynamic by returning ownership to the data owners. This is not speculative; it’s already emerging. For example, [ActivityPub](https://activitypub.rocks/), the protocol behind decentralized [social networks](https://spectrum.ieee.org/tag/social-networks) like [Mastodon](https://mastodon.social/explore), combines content sharing with built-in attribution. Tim Berners-Lee’s [Solid protocol](https://solidproject.org/) restructures the Web around personal data pods with granular access controls.

- These technologies prioritize integrity through cryptographic verification that proves authorship, decentralized architectures that eliminate vulnerable central authorities, machine-readable semantics that make meaning explicit—structured data formats that allow computers to understand participants and actions, such as “Alice performed [surgery](https://spectrum.ieee.org/tag/surgery) on Bob”—and transparent governance where rules are visible to all. As AI systems become more autonomous, communicating directly with one another via standardized protocols, these integrity controls will be essential for maintaining trust.

### Why Data Integrity Matters in AI

- For AI systems, integrity is crucial in four domains. The first is decision quality. With AI increasingly contributing to decision-making in [health care](https://spectrum.ieee.org/tag/health-care), justice, and finance, the integrity of both data and models’ actions directly impact human welfare. Accountability is the second domain. Understanding the causes of failures requires reliable logging, audit trails, and system records.

- The third domain is the security relationships between components. Many authentication systems rely on the integrity of identity information and cryptographic keys. If these elements are compromised, malicious agents could impersonate trusted systems, potentially creating cascading failures as [AI agents](https://spectrum.ieee.org/tag/agentic-ai) interact and make decisions based on corrupted credentials.

- Finally, integrity matters in our public definitions of safety. Governments worldwide are introducing [rules for AI](https://spectrum.ieee.org/ai-regulation-worldwide) that focus on data accuracy, transparent algorithms, and verifiable claims about system behavior. Integrity provides the basis for meeting these legal obligations.

- The importance of integrity only grows as AI systems are entrusted with more critical applications and operate with less human oversight. While people can sometimes detect integrity lapses, [autonomous systems](https://spectrum.ieee.org/tag/autonomous-systems) may not only miss warning signs—they may exponentially increase the severity of breaches. Without assurances of integrity, organizations will not trust AI systems for important tasks, and we won’t realize the full potential of AI.

### How to Build AI Systems With Integrity

- Imagine an AI system as a home we’re building together. The integrity of this home doesn’t rest on a single security feature but on the thoughtful integration of many elements: solid foundations, well-constructed walls, clear pathways between rooms, and shared agreements about how spaces will be used.

- We begin by laying the cornerstone: [cryptographic verification](https://spectrum.ieee.org/pioneers-web-cryptography-future-authentication). Digital signatures ensure that data lineage is traceable, much like a title deed proves ownership. Decentralized identifiers act as digital [passports](https://spectrum.ieee.org/tag/passports), allowing components to prove identity independently. When the front door of our AI home recognizes visitors through their own keys rather than through a vulnerable central doorman, we create resilience in the architecture of trust.

- Formal verification methods enable us to mathematically prove the structural integrity of critical components, ensuring that systems can withstand pressures placed upon them—especially in high-stakes domains where lives may depend on an AI’s decision.

- Just as a well-designed home creates separate spaces, trustworthy AI systems are built with thoughtful compartmentalization. We don’t rely on a single barrier but rather layer them to limit how problems in one area might affect others. Just as a [kitchen](https://spectrum.ieee.org/tag/kitchen) fire is contained by fire doors and independent smoke alarms, training data is separated from the AI’s inferences and output to limit the impact of any single failure or breach.

- Throughout this AI home, we build transparency into the design: The equivalent of large windows that allow light into every corner is clear pathways from input to output. We install monitoring systems that continuously check for weaknesses, alerting us before small issues become catastrophic failures.

- But a home isn’t just a physical structure, it’s also the agreements we make about how to live within it. Our governance frameworks act as these shared understandings. Before welcoming new residents, we provide them with certification standards. Just as landlords conduct credit checks, we conduct integrity assessments to evaluate newcomers. And we strive to be good neighbors, aligning our community agreements with broader societal expectations. Perhaps most important, we recognize that our AI home will shelter diverse individuals with varying needs. Our governance structures must reflect this diversity, bringing many stakeholders to the table. A truly trustworthy system cannot be designed only for its builders but must serve anyone authorized to eventually call it home.

- That’s how we’ll create AI systems worthy of trust: not by blindly believing in their perfection but because we’ve intentionally designed them with integrity controls at every level.

### A Challenge of Language

- Unlike other properties of security, like “available” or “private,” we don’t have a common adjective form for “integrity.” This makes it hard to talk about it. It turns out that there is a word in English: “integrous.” The Oxford English Dictionary recorded the word used in the mid-1600s but now [declares it obsolete](https://www.oed.com/dictionary/integrous_adj?tab=factsheet&tl=true#210671).

- We believe that the word needs to be revived. We need the ability to describe a system with integrity. We must be able to talk about integrous systems design.

### The Road Ahead

- Ensuring integrity in AI presents formidable challenges. As models grow larger and more complex, maintaining integrity without sacrificing performance becomes difficult. Integrity controls often require computational resources that can slow systems down—particularly challenging for real-time applications. Another concern is that [emerging technologies](https://spectrum.ieee.org/tag/emerging-technologies) like [quantum computing](https://spectrum.ieee.org/tag/quantum-computing)[threaten current cryptographic protections](https://spectrum.ieee.org/tag/quantum-computing). Additionally, the distributed nature of modern AI—which relies on vast ecosystems of [libraries](https://spectrum.ieee.org/tag/libraries), frameworks, and services—presents a large attack surface.

- Beyond technology, integrity depends heavily on social factors. Companies often prioritize speed to market over robust integrity controls. Development teams may lack specialized knowledge for implementing these controls, and may find it particularly difficult to integrate them into legacy systems. And while some governments have begun establishing regulations for aspects of AI, we need worldwide alignment on governance for AI integrity.

- Addressing these challenges requires sustained research into verifying and enforcing integrity, as well as recovering from breaches. Priority areas include [fault-tolerant](https://spectrum.ieee.org/tag/fault-tolerant)[algorithms](https://spectrum.ieee.org/tag/fault-tolerant) for distributed learning, verifiable computation on encrypted data, techniques that maintain integrity despite [adversarial attacks](https://spectrum.ieee.org/tag/adversarial-attacks), and standardized metrics for certification. We also need interfaces that clearly communicate integrity status to human overseers.

- As AI systems become more powerful and pervasive, the stakes for integrity have never been higher. We are entering an era where machine-to-machine interactions and autonomous agents will operate with reduced human oversight and make decisions with profound impacts.

- The good news is that the tools for building systems with integrity already exist. What’s needed is a shift in mind-set: from treating integrity as an afterthought to accepting that it’s the core organizing principle of AI security.

- The next era of technology will be defined not by what AI can do, but by whether we can trust it to know or especially to do what’s right. Integrity—in all its dimensions—will determine the answer.

### Sidebar: Examples of Integrity Failures

- [Ariane 5 Rocket (1996)](https://spectrum.ieee.org/tag/adversarial-attacks)*Processing integrity failure* A 64-bit velocity calculation was converted to a 16-bit output, causing an error called overflow. The corrupted data triggered catastrophic course corrections that forced the US $370 million rocket to [self-destruct](https://spectrum.ieee.org/tag/self-destruct).

- [NASA Mars Climate Orbiter (1999)](https://spectrum.ieee.org/tag/self-destruct)*Processing integrity failure* Lockheed Martin’s software calculated thrust in pound-seconds, while NASA’s navigation software expected newton-seconds. The failure caused the $328 million spacecraft to burn up in the [Mars](https://spectrum.ieee.org/tag/mars) atmosphere.

- [ Microsoft’s Tay Chatbot (2016)](https://spectrum.ieee.org/tag/mars)*Processing integrity failure* Released on [Twitter](https://spectrum.ieee.org/tag/twitter), [Microsoft](https://spectrum.ieee.org/tag/microsoft)‘s AI chatbot was vulnerable to a “repeat after me” command, which meant it would echo any offensive content fed to it.

- [ Boeing 737 MAX (2018)](https://spectrum.ieee.org/tag/microsoft)*Input integrity failure* Faulty sensor data caused an automated flight-control system to repeatedly push the airplane’s nose down, leading to a fatal crash.

- [ SolarWinds Supply-Chain Attack (2020)](https://spectrum.ieee.org/tag/microsoft)*Storage integrity failure* Russian [hackers](https://spectrum.ieee.org/tag/hackers) compromised the process that [SolarWinds](https://spectrum.ieee.org/tag/solarwinds) used to package its software, injecting malicious code that was distributed to 18,000 customers, including nine federal agencies. The hack remained undetected for 14 months.

- [ ChatGPT Data Leak (2023)](https://spectrum.ieee.org/tag/solarwinds)*Storage integrity failure* A bug in OpenAI’s [ChatGPT](https://spectrum.ieee.org/tag/chatgpt) mixed different users’ conversation histories. Users suddenly had other people’s chats appear in their interfaces with no way to prove the conversations weren’t theirs.

- [ Midjourney Bias (2023)](https://spectrum.ieee.org/tag/chatgpt)*Contextual integrity failure* Users discovered that the [AI image generator](https://spectrum.ieee.org/ai-art-generator-2670499999) often produced biased images of people, such as showing white men as CEOs regardless of the prompt. The AI tool didn’t accurately reflect the context requested by the users.

- [Prompt Injection Attacks (2023–)](https://spectrum.ieee.org/ai-art-generator-2670499999)*Input integrity failure* Attackers embedded hidden prompts in emails, documents, and websites that hijacked AI assistants, causing them to treat malicious instructions as legitimate commands.

- [CrowdStrike Outage (2024)](https://spectrum.ieee.org/ai-art-generator-2670499999)*Processing integrity failure* A faulty software update from CrowdStrike caused 8.5 million Windows computers worldwide to crash—grounding flights, shutting down hospitals, and disrupting banks. The update, which contained a software logic error, hadn’t gone through full testing protocols.

- **Voice-Clone Scams (2024)***Input and processing integrity failure* Scammers used AI-powered voice-cloning tools to mimic the voices of victims’ family members, tricking people into sending money. These [scams](https://spectrum.ieee.org/tag/scams) succeeded because neither phone systems nor victims identified the AI-generated voice as fake.

- This essay was written with Davi Ottenheimer, and originally appeared in [IEEE Spectrum](https://spectrum.ieee.org/data-integrity)*.*

- Tags: [AI](https://www.schneier.com/tag/ai/), [integrity](https://www.schneier.com/tag/integrity/), [trust](https://www.schneier.com/tag/trust/)

- [Posted on August 22, 2025 at 7:04 AM](https://www.schneier.com/tag/trust/) • [24 Comments](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html#comments)

### Comments

- Tobias Maassen  • [ August 22, 2025 7:32 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447300)

- Yeah, but isn’t AI like Web 4.0? Web 3.0 is the web of crypto-fraud and grifters and the like. There is no integrity there.

- Dave Sanford  • [ August 22, 2025 8:07 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447302)

- This is a good article, but I think it starts with fixing the original sin of the Internet—lack of verifiable human accountability. Anonymous or pseudonymous systems not backed by unique personhood certificates allow and promote unaccountable actions.

- Companies and other organizations that absolve themselves of responsibility, while at the same time controlling, or worse, letting loose algorithms that they can’t control on their systems, exacerbate the problem.

- ResearcherZero  • [ August 22, 2025 8:13 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447303)

- @Tobias Maassen

- There are very good reasons for why data needs to be accurate and consistent.

- As a person’s power increases, their moral sense diminishes. Or as William Pitt the Earl of Chatham (former Prime Minister of England 1766-1778) stated, “Unlimited power is apt to corrupt the minds of those who possess it”. William Pitt the Elder, and “The Younger”, was admitted to Pembroke College in 1773 (aged 13). At 24 he became Prime Minister.

- Trump demands woman who deliberately breached election security be released from prison.

- ‘https://www.yahoo.com/news/articles/trump-threatens-harsh-measures-tina-005814986.html

- –

- Fine for excessive claims dismissed for being excessive.

- ‘https://www.pbs.org/newshour/politics/trumps-massive-civil-fraud-penalty-for-exaggerating-financial-statements-is-thrown-out-by-appeals-court

- The decision was made after justices could not agree over the details.

- [https://www.cbsnews.com/news/trump-civil-fraud-case-new-york-appeals/](https://www.cbsnews.com/news/trump-civil-fraud-case-new-york-appeals/)

- ResearcherZero  • [ August 22, 2025 8:31 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447304)

- @Dave Sanford

- You may require verification if you used an online application such as ChatGPT to plan or conduct malfeasance. If you commit crimes on behalf of the president, you need to back it up with solid proof. Without verifiable data to prove your actions, he may not bail you out.

- Bragging rights are essential for any act in similar circumstances with similar people.

- A fuhrer must demonstrate that they will sanction and absolve those who do their bidding.

- anon  • [ August 22, 2025 9:08 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447305)

- The Crowdstrike blunder wasn’t the distribution of a software update, but of a definition file. The faulty software was already installed and was triggered by the malformed update file.

- Jon  • [ August 22, 2025 12:21 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447313)

- If you want these things to stop, you will have to personally identify and hold personally (not just the company, the persons) responsible.

- Not merely the person who wrote the code, or the person who executed the code, but those responsible for the code, materials, or safety failure – and those punishments must be swift, severe, and universally implemented.

- Until then, we’ll keep getting crap like all of Mr. Scheneier’s examples.

- J.

- Clive Robinson  • [ August 22, 2025 2:49 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447314)

- @ Jon,

- Beware of what you ask for with,

- “Not merely the person who wrote the code, or the person who executed the code, but those responsible for the code, materials, or safety failure”

- Many people make the mistake of thinking that as the software architecture tends to be sequential, as a chain, tree, or a net hung by one corner that it’s behaviour is similarly structured in a descendant hierarchical form. And this gets built into the way the code is tested during original development and later maintenance etc.

- So the individual checks and tests etc are sufficient, unfortunately that is not the case due to loops that create certain types of circular behaviours

- Whilst loops are mostly somewhat benign topologically, and have a top down sequential single direction of flow nature, Thus would appear amenable to analysis not all are[1].

- One result is you can have functions called in a circular or ordered way, whilst each function can be considered benign they can give the equivalence of a game of “rock-paper-scissors” which is not benign.

- If the three functions are written by separate individuals and signed off as “to specification and tests” by three others, who is responsible for the “safety failure” thus to blaim?

- [1] I won’t go into the use of Knot Theory which has been tried as a way to resolve loop issues but just note “the issue of intractability” that arise. Thus loops can be beyond analysis even though they can be traced all around with just a finger. Worse other topological techniques have been tried but they all tend to reach a limit very quickly when you go from a simple case. Which is why it’s been noted that loops should be simple and without side effects –think non reentrant as a minimum– and preferably suitably unrolled.

- Daniel Popescu  • [ August 22, 2025 2:59 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447315)

- Fabulous article Bruce, thanks!

- We have in pharma(been an automation engineer in the industry for 20 years now) a few fundamental concepts as CSV, data integrity and ALCOA++ principles. Anything that has some form of software based function, from the simplest lab equipment to really complex automated systems and processes, that could have an impact on the final product and on the patient’s health, is tested, validated ,risk assessed and maintained and pampered…you have no idea :).

- Hard work, but imensly rewarding.

- Anonymous  • [ August 22, 2025 3:41 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447317)

- Congrats!

- Google’s AI Overview is already using your blog article as source material when searching for “examples of ai systems with high integrity”

- Thanks for your contributions to this corpus of work 🙂

- Reads as:

- “Emerging Technologies & Architectures:

- Data-Centric Integrity Protocols:

- Emerging technologies in decentralized systems, like ActivityPub and Solid, use AI with built-in integrity features such as cryptographic verification for authorship, decentralized architecture, and semantic data formats to ensure transparency and truthfulness” Source

- andyinsdca  • [ August 22, 2025 5:33 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447320)

- I see Dave Sanford has already posted the “oi, mate, you got a loicense to post on the internet?” idea.

- It’s the marketplace of ideas, the only way to filter out bad info/ideas from any public square is to get good info/ideas out there that refute the bad info.

- If you trust the government to do that filtering, you’re going to have a VERY, VERY bad day (the government has no stake in getting anything right)

- What does this have to do with AI? Right now, AI isn’t “smart” enough to engage in the marketplace of ideas. If it stumbles on an article that says gluing cheese onto pizza is a good idea, it’s going to run with that and any AIs that learn from that first AI will be similarly contaminated. The first AI may somehow eventually figure out that gluing stuff to pizza is a bad idea, but will the downstream AIs figure it out? Suppose a human posted the idea, lots of people would quickly mock them, post where they’re wrong (i.e. “Glue is poison, you idiot”) etc. and the marketplace of ideas would “win” here.

- Supersaurus  • [ August 23, 2025 6:35 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447334)

- @Clive

- Thank you for many years of knowledgeable and thought provoking comments.

- Jon (a different Jon)  • [ August 23, 2025 9:50 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447338)

- @ Clive Robinson

- Easy solution, M. Robinson – they’re all liable.

- Note that this sort of ‘circular responsibility’, I believe (IANAL) is wildly illegal in most countries. Eg:

- Corporation A owns Corporation B.

- Corporation B owns Corporation C.

- Corporation C owns Corporation A.

- Now Corporation B does something horrible, and gets successfully sued, but Corporation B promptly declares bankruptcy, so people start going after “Who owns B?”, only to find A, so “Who owns A?” finds out C, only to find that everything C owns belongs to B again. Who’s responsible?

- The answer there is even more simple: Cui Bono? It’s how maritime law already works with lots of people pointing fingers at everyone else except themselves in major shipwrecks (and those maritime firms have spent years and years deliberately mixing up who is responsible for what).

- It’s a problem, yes. But many people spend lots of time finding out who is ultimately responsible, no matter how many “benign” loops are set up.

- J.

- (Incidentally, ‘circular loop calling’ in software is not and never will be entirely benign, tending to have either starting or runaway problems. Not stable, that.)

- Clive Robinson  • [ August 24, 2025 9:37 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447360)

- @ Supersaurus,

- Thank you, and a simple wish,

- May we both have many enjoyable years to come.

- Clive Robinson  • [ August 24, 2025 9:48 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447361)

- @ Jon (a different Jon),

- Whilst,

- “Note that this sort of ‘circular responsibility’, I believe (IANAL) is wildly illegal in most countries. “

- It’s illegal for two reasons,

- 1, Your son cannot become your father.

- 2, Setting up such a structure shows premeditation.

- The same is not true for things that are not,

- “Persons legal or natural”.

- Therefore anything that is mechanical or informational in nature is not covered.

- Remember we might say,

- “It’s turtles all the way down.”

- But also logically,

- “It’s turtles all the way up.”

- As well. Because that is the nature of loops.

- X2bike  • [ August 24, 2025 8:35 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447365)

- Required reading for my risk team.

- J L Turriff  • [ August 25, 2025 12:56 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447369)

- *“The good news is that the tools for building systems with integrity already exist. What’s needed is a shift in mind-set: from treating integrity as an afterthought to accepting that it’s the core organizing principle of AI security.”*

- I’m not sanguine about the likelyhood of this happening any time soon. How many years have we been living with the hacking events of data theft/exposure/locking (which is fairly easy to address)? Yet they continue to happen regularly and the response is effectively to just shake a finger at the “victims” who seem not to think that security is important, instead of penalizing them? why will these integrity issues be handled any differently?

- Clive Robinson  • [ August 25, 2025 7:24 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447373)

- @ andyinsdca,

- With regards,

- “Suppose a human posted the idea, lots of people would quickly mock them, post where they’re wrong (i.e. “Glue is poison, you idiot”)”

- Actually it’s a way worse problem than you think…

- Because a lot of glues are not poisonous and are in fact used in cooking and have been for a very long time centuries in some cases. As for poisons they routienly get used in food as well and we swallow them down with hardly a thought…

- As a child you might have used wheat flour and water to make a paste you used as a glue (it is mostly “kiddy safe”). You might have used a form of “cheese sauce” that is a casin glue or plastic. And there are other biologicals dissolved in alcohol such as edible/chewable resins (like pine pitch).

- Then there are “egg washes” used to glue things to pastry likewise sugar water. That for centuries gave been used in paints as binders. Then there is boild up bone broth that gives Aspic which is also a glue.

- Look up “gum arabic / accacia gum” in food or pharmaceutical grade you can buy it by the kilogramme off of Ebay. Likewise the base of all small childrens party foods jello/jelly which is rendered live stock skin tendons and other connective tissue which for the more sensitive is called gelatine.

- But fun fact quite nasty poisons are used in everyday cooking and food stuffs.

- Like bagels are washed in a very caustic solution you might know as sodium hydroxide (NaOH). It’s used as a processing agent for “peeling fruit and vegtables” to take out the bitter flavour of olives and in other ways make them more palatable. Similar with chocolate etc oh and as a whipping agent / stabiliser in ice cream etc.

- Oh and the reason sodium hydroxide is available as “drain cleaner” is it turns “lipids/fats to soap”. Every living animal cell has lipids forming the walls. But a little soap and water as most children used to know “made bubbles at bath time”.

- Would you use anything that had petrol/gas in? Well many natural food flavourings like “rose water” are extracted with it.

- Then there are acids and explosive compounds of nitrogen that get used in everyday foods as peeling agents. Preservatives, Flavour Enhancers, and to aid in setting.

- Oh and then there is cyanide… It’s in every fruit that “has pits in”. Apple seeds and peach stones are a significant source (enough to be your demise). It’s why you should not use them in cooking, so core you apples and if making cider do not over press and take care to filter properly.

- But there is also other nasty poisons that are in the leaves of tomatos, potatoes, rhubarb and any bits of them that are green. Likewise other “garden vegetables” you might grow.

- Then there are some beans/pulses that contain neurotoxins. Red kidney beans if not already cooked by a manufacturer and properly canned should be soaked overnight, and boiled vigorously for 10mins before being cooked in other dishes.

- Then their are other starch food sources like roots and tubers. Look up “Death by Casava” it occasionally gets covered in national press when a “foodie” tries making a “traditional native dish”…

- Even what you might think is a banana but is a form of plantain whilst not directly a poison can make you ill or worse (GI bleeding, anaphylactic shock) if you eat them raw. This is due to the types of starch and a number of proteins including lectin.

- There is a heck of a lot more about glues and poisons in foods enough to fill lots of books and scientific papers…

- So is it any wonder if humans can not get it right, that what is just a pile of scrap chips to be, that can only mimic badly, can not get it right either…

- Just remember when you hear someone at their computer curse under their breath,

- “This bl@@dy thing will be the death of me…”

- The old saying,

- “Be n’t angry with this fellow, I protest.

- That many a true word hath been spoke in jest.”[1]

- Will we hope not come true…

- [1] Supposedly a variation / augmentation / adaption of a late 1300’s phrase by Geoffrey Chaucer,

- “Ful ofte in game a sooth I have herd saye!”

- ResearcherZero  • [ August 26, 2025 2:42 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447392)

- To state the bleeding obvious, it seems like a bad time to introduce policies driven by the poorly informed, overly optimistic or blind naïveté. Removing safeguards at anytime has not delivered the best outcomes. (Nor removing government experts well versed in such risks.)

- For the sake of rapid development in the early days of the dot-com boom, security legislation was ignored. Only later on when the problems of widespread vulnerabilities began to exert a growing cost and the dangers of rising information disclosures became more pronounced, did governments finally take action. A lack of foresight is now being repeated, which will inevitably lead to an even greater number of risks, due to the widespread integration of automated systems and the power and reach of utility-based agents.

- Adversaries are using GenAI to produce deceptive content, gain access and conduct long-term espionage. Silk Typhoon (Hafnium) targets cloud environments to compromise high-profile targets and pivot to the target’s downstream customers to conduct further activity.

- ‘https://www.crowdstrike.com/en-us/blog/murky-panda-trusted-relationship-threat-in-cloud/

- Silk Typhoon and APT27 have a sophisticated understanding of supply chains.

- [https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)

- Foreign state-backed actors used a service that exploits stolen Azure API keys and customer Entra ID authentication to conduct campaigns. *(This has been going on for some time.)*

- https://www.courtlistener.com/docket/69534982/microsoft-corporation-v-does-1-10-operating-an-azure-abuse-network/

- Rontea  • [ September 9, 2025 10:10 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447708)

- Integrity is the cornerstone of trustworthy AI systems, particularly in the decentralized Web 3.0 era.

- jonW  • [ September 15, 2025 9:49 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447912)

- Unlike other properties of security, like “available” or “private,” we don’t have a common adjective form for “integrity.”

- Etymological aside: “intact” may be the form you seek.

- Clive Robinson  • [ September 15, 2025 6:22 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447961)

- @ Rontea,

- With regards,

- Integrity is the cornerstone of trustworthy AI systems, particularly in the decentralized Web 3.0 era.

- You can not share “Integrity” between two separate physical or information objects, or points in space, or time[1], even if you share all the information you can measure.

- This unfortunate truth was shown to this blog not that long ago in a simpler way than other ways have in other fora in the past.

- [https://www.schneier.com/blog/archives/2025/06/the-age-of-integrity.html/#comment-446195](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447961)

- Put simply,

- “Copies do not confer confidence or correctness in an original.”

- Why?

- Simply because they are not “integral”, one, the other or both are at best a record of imprecise measurements made,

- “But of What?”

- There is no way to build beyond this point.

- Thus what becomes of “Web 3.0” –or the other beast “Web 3”– as Integrity is not possible, let alone a cornerstone.

- Neither –which ever schills are trying to try to take your money away by scam investment today– is actually possible as anything other than a scam investment.

- If you want to understand why go and look up the history of Offline DRM systems, where the failure has been practically demonstrated numerous times. And always will be in practical use systems.

- [1] To borrow an old “Physics Master school joke”,

- “Boy, I saw you were present in the lesson, and I saw you are not in the register. So, you are Erwin’s cat.

- But consider the initial statements,

- 1, Both are actually integral in of themselves.

- 2, As independent statements they will both be found to be integral with respect to the values they hold.

- When seen independently the usual and incorrect assumption is that each is therefore “true”.

- However their joining is not possible as they are not of the same value so can not be integral to each other.

- That is, Each token of

- 1, The Masters Memory

- 2, The Masters Register

- If treated as an independent token can be integral.

- But as part of a single system the information has to be regarded as either,

- 3, Unknown

- 4, False / True

- So even if the tokens are individually integral, the system is not internally consistent, so can not be seen as integral.

- Chris Drake  • [ September 15, 2025 11:51 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447976)

- This entire advertisement displays a massive lack of reality-comprehension.

- Data lives in silos for a reason – no amount of “wishing it wasn’t so” can fix that, no matter how awesome the tech stack or the celebrity promoters weighing in, and no matter how much money you’ve blown in your crypto investments.

- You may as well add world-peace, abundance-for-all, social-equality, religious-tolerance, benevolent-dictatorships, functional-democracy, equitable-capitalism and every other impossible dream to your “web 3.0” specs… every one is at least as likely to come true before web3.0 does…

- [Mark C](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447976) • [ September 16, 2025 5:43 AM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447980)

- Thanks for the thought provoking essay. Still trying to get my head around some of it because I come at these things from the political policy angle rather than technical perspective (albeit having done some computer science when I was in college back in the last millenium). To your list of examples I’d like to add a very recent small one – not a huge impact instance as a single incident (like, say, Crowdstrike) but if replicated at scale it would cause major chaos.

- [https://www.theguardian.com/money/2025/sep/16/i-cant-use-my-new-credit-card-because-lloyds-thinks-im-my-twin-sister](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447980)

- In essence, Lloyds Bank’s systems appear to have been doing some sort of “data tidying” and in the process merged two sets of records belonging to a woman and her twin sister. The sister did not have an account with Lloyds but with Halifax, another bank that was part of the same group. The problem was only discovered when the Lloyds customer was unable to activate her new bank card.

- It’s not clear whether any sort of AI system was involved or whether it was more “old tech” – but that’s not the point. This is very much the sort of data integrity problem that could clearly arise if AI is deployed without rigorous assurance of processing integrity.

- It might be argued that this example is a special case because the women were twins but it strikes me that one of the peculiarities of currently popular types of AI is that they can be prone to “seeing” false correlations in data. I suggest that if banks deploy AI agents into their databases without the right assurance of processing integrity and without close monitoring then these types of error might proliferate.

- Rontea  • [ September 16, 2025 1:18 PM ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447998)

- @Clive

- “So even if the tokens are individually integral, the system is not internally consistent, so can not be seen as integral.”

- Observations and measurements are foundational to the integrity of any information system. Since information is intangible and derived from these processes, the accuracy and reliability of data hinge on how well observations are made and measurements are recorded. Without robust mechanisms to ensure data integrity from the point of collection to processing, systems risk becoming unreliable. This highlights the need for continuous research into verifiable and measurable methods to maintain and recover data integrity in information systems, especially in complex environments like Web 3.0.

- [ Subscribe to comments on this entry ](https://www.schneier.com/blog/archives/2025/08/ai-agents-need-data-integrity.html/#comment-447998)

## Leave a comment Cancel reply

- Blog moderation policy

- **Allowed HTML** <a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre> **Markdown Extra** syntax via [https://michelf.ca/projects/php-markdown/extra/](https://michelf.ca/projects/php-markdown/extra/)

- [← Jim Sanborn Is Auctioning Off the Solution to Part Four of the Kryptos Sculpture](https://michelf.ca/projects/php-markdown/extra/)[I’m Spending the Year at the Munk School →](https://michelf.ca/projects/php-markdown/extra/)Sidebar photo of Bruce Schneier by Joe MacInnis.

- [Powered by WordPress](https://michelf.ca/projects/php-markdown/extra/)[Hosted by Pressable](https://michelf.ca/projects/php-markdown/extra/)

### About Bruce Schneier

- I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](https://www.schneier.com/) since 2004, and in my monthly [newsletter](https://www.schneier.com/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

### Related Entries

- [AI and Voter Engagement](https://inrupt.com/)

- [More Prompt||GTFO](https://inrupt.com/)

- [The Role of Humans in an AI-Powered World](https://inrupt.com/)

- [Prompt Injection in AI Browsers](https://inrupt.com/)

- [Faking Receipts with AI](https://inrupt.com/)

- [Scientists Need a Positive Vision for AI](https://inrupt.com/)

### Featured Essays

- [The Value of Encryption](https://inrupt.com/)

- [Data Is a Toxic Asset, So Why Not Throw It Out?](https://inrupt.com/)

- [How the NSA Threatens National Security](https://inrupt.com/)

- [Terrorists May Use Google Earth, But Fear Is No Reason to Ban It](https://inrupt.com/)

- [In Praise of Security Theater](https://inrupt.com/)

- [Refuse to be Terrorized](https://inrupt.com/)

- [The Eternal Value of Privacy](https://inrupt.com/)

- [Terrorists Don't Do Movie Plots](https://inrupt.com/)

- [More Essays](https://inrupt.com/)

### Blog Archives

- [Archive by Month](https://inrupt.com/)

- [100 Latest Comments](https://inrupt.com/)

Blog Tags

- [3d printers](https://inrupt.com/)

- [9/11](https://inrupt.com/)

- [A Hacker's Mind](https://inrupt.com/)

- [Aaron Swartz](https://inrupt.com/)

- [academic](https://inrupt.com/)

- [academic papers](https://inrupt.com/)

- [accountability](https://inrupt.com/)

- [ACLU](https://inrupt.com/)

- [activism](https://inrupt.com/)

- [Adobe](https://inrupt.com/)

- [advanced persistent threats](https://inrupt.com/)

- [adware](https://inrupt.com/)

- [AES](https://inrupt.com/)

- [Afghanistan](https://inrupt.com/)

- [AI](https://inrupt.com/)

- [air marshals](https://inrupt.com/)

- [air travel](https://inrupt.com/)

- [airgaps](https://inrupt.com/)

- [al Qaeda](https://inrupt.com/)

- [alarms](https://inrupt.com/)

- [algorithms](https://inrupt.com/)

- [alibis](https://inrupt.com/)

- [Amazon](https://inrupt.com/)

- [Android](https://inrupt.com/)

- [anonymity](https://inrupt.com/)

- [Anonymous](https://inrupt.com/)

- [antivirus](https://inrupt.com/)

- [Apache](https://inrupt.com/)

- [Apple](https://inrupt.com/)

- [Applied Cryptography](https://inrupt.com/)

- [More Tags](https://inrupt.com/)

### Latest Book

- [More Books](https://inrupt.com/)