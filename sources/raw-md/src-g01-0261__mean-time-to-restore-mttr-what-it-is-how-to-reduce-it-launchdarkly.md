> Source: https://launchdarkly.com/blog/mean-time-to-restore-mttr/

LaunchDarklyPlatform
LaunchDarkly Platform
Guarded Releases
Monitor and de-risk.
Experimentation
Make data-driven decisions.
Feature Flags
Scale great release processes.
Product Analytics
Measure feature impact.
AI Configs
Make innovative AI products.
Booth #1339 // Dec 1-5
Meet us in Vegas at AWS re:Invent.
Book a meetingOverview
Platform overviewFeature lifecycle managementIntegrationsGovernanceAutomationPlatform architectureLaunchdarkly vs in-houseSolutions
By Team
DevelopersDevOps & SREMobile appsProduct managersBy Industry
Financial servicesRetail & eCommerceHealthcareManufacturing & logisticsU.S. governmentMedia & entertainmentHigh techTravel & hospitalityResources
Learn
BlogGuides & ebooksEvents & webinarsVideosSuccess
AcademyCustomer storiesProfessional servicesPartnersGet Help
Help centerRequest supportBooth #1339 // Dec 1-5
Meet us in Vegas at AWS re:Invent.
Book a meetingDevelopers
Docs
Docs homeFeature flags quickstartAI Configs quickstartAPI docsResources
Product UpdatesPower analysis calculatorFlagship engineering blogCommunityPricingSign InDemo ProjectGet a demoBlogRisk MitigationMean Time to Restore (MTTR): What It Is & How to Reduce It
SEP 11 2024
Mean Time to Restore (MTTR): What It Is & How to Reduce It
Jesse SumrakLaunchDarkly
Table of Contents
What is mean time to restore (MTTR)?
MTTR and the Four DORA Metrics
How to calculate MTTR
The real cost(s) of slow recovery
Factors impacting your MTTR
10 strategies to reduce MTTR
How LaunchDarkly reduces your MTTR
Sign up for our newsletter
Get tips and best practices on feature management, developing great AI apps, running smart experiments, and more.
SubscribeDefining mean time to restore (MTTR)
Mean time to restore (MTTR) is the average time it takes to recover from a system failure or outage. It's calculated by dividing the total downtime by the number of failure incidents over a specific period. A lower MTTR indicates a more resilient system and a more effective incident response process, while a higher MTTR suggests room for incident response improvements.
Regardless of your experience, testing, or quality assurance procedures, we all know the truth about software development: bad ship happens. The question, then, isn't whether you’ll experience a software incident but how quickly can you recover.
That’s where the mean time to restore (MTTR) service becomes important. This critical DevOps metric reveals how quickly your teams bounce back from incidents and bugs. The lower your MTTR, the faster you're back in business, keeping your users happy, stress levels in check, and bottom line healthy. 
However, reducing your MTTR is easier said than done (without the right tools and know-how). With microservices, cloud infrastructure, and endless integrations, pinpointing and fixing issues can feel like looking for a misplaced semicolon in a sea of JavaScript.
Fortunately, we can help.
Below, we’ll walk you through everything you need to know about MTTR and how you can use feature management platforms (like LaunchDarkly) to reduce downtime and save your business.
What is mean time to restore (MTTR)?
The faster you recover, the less impact on your business operations and your customers' experience. Simple as that. A low MTTR helps maintain business continuity and guarantees critical systems and services are available when needed.
Let’s face it: users aren’t patient. Every moment of downtime is a moment where a user might be cursing your app, leaving a bad review, or worse, jumping ship to a competitor. Keeping your MTTR low shows users that when issues occur (because they will), you’ll take care of it quickly.
MTTR isn’t just about your incident response process or brand reputation. A high MTTR can lead to severe consequences for other businesses and consumers:
In the airline industry, system outages can lead to thousands of flights being canceled globally, resulting in hundreds of millions of dollars in losses and leaving countless passengers stranded.
For healthcare providers, system failures can prevent patients from accessing vital care, potentially putting lives at risk and disrupting critical medical services.
Financial institutions experiencing prolonged downtime may face substantial monetary losses, regulatory scrutiny, and a significant erosion of customer trust.
E-commerce platforms can lose millions in revenue during peak shopping periods if systems are down for even short periods.
Common misconceptions about MTTR
One of the best ways to learn about MTTR is about understanding what it’s not. These misconceptions commonly trip businesses up:
Low MTTR means fewer incidents: Not necessarily. MTTR measures how quickly you recover, not how often issues occur. You could have a low MTTR but still face frequent incidents.
MTTR is all about fixing bugs: While bug fixes are part of it, MTTR encompasses all types of incidents, including infrastructure issues, configuration errors, or even planned maintenance.
Automating everything will automatically lower MTTR:Automation can help, but it's not a silver bullet. Without proper planning and implementation, automated systems can sometimes make issues harder to diagnose and resolve.
MTTR is purely a tech team metric: While tech teams are on the front lines, MTTR is a business-wide concern. It affects customer service, sales, marketing—everyone.
The goal should always be zero MTTR: It’s very unlikely you’ll recover instantaneously. But recovering from a failed deployment in minutes is possible with the right combination of DevOps tools and processes—and it puts you among the elite engineering teams, according to DORA.
MTTR and the Four DORA Metrics
MTTR is one of the four key metrics identified by the DevOps Research and Assessment (DORA) team. These DORA metrics are widely used to measure software development and operational performance.
Deployment Frequency: How often an organization successfully releases to production.
Lead Time for Changes: The time it takes to go from code committed to code successfully running in production.
Change Failure Rate: The percentage of deployments causing a failure in production.
Mean Time to Restore: How long it takes to restore service when a service incident occurs.
Ultimately, MTTR is just a single metric with a focused purpose—however, in the context of these other metrics, it provides a more comprehensive view of your team's effectiveness.
Also, it’s helpful to distinguish between a few similar-sounding metrics. While the following terms are often used interchangeably, they all mean something just a little bit different:
Mean time to recover: The average time between when an incident starts and when it's fully resolved.
Mean time to repair: The average time taken to repair a failed component.
Mean time to restore: The average time to restore a system to a functional state after a failure.
MTTR in the broader incident management landscape
MTTR is part of a larger set of incident metrics that DevOps and engineering teams use to measure and improve their performance:
Mean time to detect (MTTD): How long it takes to discover an incident.
Mean time to acknowledge (MTTA): The average time between detection and response initiation.
Mean time between failures (MTBF): The average time between system failures.
Together, these metrics provide a comprehensive view of an organization's incident management capabilities.
DevOps and engineering teams leverage these metrics for setting and measuring service level objectives (SLOs). These metrics also help in monitoring compliance with service level agreements (SLAs), which often include specific commitments about system uptime and incident resolution times. Plus, tracking incident metrics like these over time give you benchmarks to gauge your performance year-over-year or against industry standards.
How to calculate mean time to restore
MTTR = Total downtime / Number of incidents
You take the total amount of downtime over a given period and divide it by the number of incidents that occurred during that same period.
Let’s look at an example:
Imagine your system experienced three outages last month:
Outage 1: 2 hours
Outage 2: 30 minutes
Outage 3: 1 hour and 30 minutes
First, let's convert all times to the same unit (we'll use minutes):
2 hours = 120 minutes
30 minutes
1 hour and 30 minutes = 90 minutes
Now, let's plug these numbers into our formula:
Total downtime = 120 + 30 + 90 = 240 minutes. Number of incidents = 3
MTTR = 240 minutes / 3 incidents = 80 minutes
So, your mean time to restore for the month is 80 minutes.
While the calculation is relatively simple, the tricky part comes in accurately tracking downtime and defining what constitutes an "incident" for your specific system.
The real cost(s) of slow recovery
When systems go down, every minute counts. Here are just a few of the costs of slow recovery time:
Financial losses: The most immediate and tangible cost of downtime is lost revenue. For e-commerce sites, payment processors, or subscription-based services, every minute offline is money left on the table. Large enterprises can lose up to $5 million per hour during major outages.
Reputation damage: News of outages spreads like wildfire on social media. Extended downtime can lead to negative reviews, lost customer trust, and a tarnished brand image. It can take months or even years to rebuild a reputation damaged by significant service disruptions.
Decreased productivity: System outages don't just affect your customers—they paralyze your own team. Developers shift from building new features to firefighting, support teams are flooded with tickets, and other departments can't access critical tools. This ripple effect can derail project timelines and strategic initiatives.
Competitive disadvantage: While your system is down, your competitors are up and running. Extended or frequent outages can drive customers to explore alternative solutions, and once they've switched, winning them back is an uphill battle.
Compliance and legal risks: For businesses in regulated industries like healthcare or finance, extended downtime can lead to compliance violations. This can result in hefty fines, legal action, or even the loss of necessary certifications. 
Employee morale and burnout: Constantly fighting fires and dealing with angry customers takes a toll on your team. High-stress incidents can lead to burnout, decreased job satisfaction, and even increased turnover.
Factors impacting your MTTR
Before you can improve your mean time to restore, you need to know what’s impacting it. While that list could be endless, here is a shortlist of the likely factors impacting your MTTR:
Complexity of modern software systems: Modern-day applications are like digital Jenga towers—pull out the wrong piece, and everything might come tumbling down.
Manual processes and human error:Manual deployments, configuration changes, and recovery processes are all opportunities for mistakes to creep in. And in high-stress situations, even the most experienced developers can slip up.
Inadequate monitoring and alerting systems: You can't fix what you don't know is broken. Insufficient monitoring and observability tools or poorly configured alerts can lead to delayed response times or (worse) issues flying under the radar until they become full-blown crises.
Full-user deployments: Pushing changes to all users simultaneously is an unnecessary risk. Without gradual rollouts, issues that weren't caught in testing can suddenly affect your entire user base, amplifying the impact and complicating recovery.
Muddy code: Code without clear demarcations or feature flags makes it challenging to isolate problematic features or roll back to a stable state quickly.
Non-targeted rollouts: Without the ability to target specific user segments, environments, or regions, you're left with an all-or-nothing approach that can make recovery more complex and time-consuming.
Inconsistent environments: If your development, staging, and production environments are wildly different, issues that crop up in production can be near impossible to reproduce and resolve quickly.
No kill switch: Rolling back an entire release and routing all production traffic to an old working version of your application prolongs your recovery time. The same is true when you write a bug fix and run it through your deployment pipeline. 
10 strategies to reduce your mean time to restore
While there’s no one-size-fits-all approach to reducing your mean time to restore, you can implement several strategies and tools to move it in the right direction.
1. Implement monitoring and alerting
Early detection is half the battle. Set up comprehensive monitoring across your entire stack—from infrastructure to application performance. Use tools that provide real-time insights and alerts, so you're not caught off guard when issues arise. The sooner you know about a problem, the quicker you can start fixing it.
Remember, issues will arise—it’s about when, not if. 
2. Create and maintain detailed runbooks
Develop clear, step-by-step runbooks for common issues and update them regularly. These playbooks can guide your team through the recovery process, reducing confusion and speeding up resolution times.
3. Automate, automate, automate
The less manual intervention required, the faster your recovery can be. Automate routine tasks, deployments, and even parts of your incident response process. Tools like configuration management systems and infrastructure-as-code can help guarantee consistency and reduce human error.
For example, Release Guardian monitors operational performance at the feature level and automatically remediates issues that arise. 
4. Use feature flags as a kill switch
Feature flags are your secret weapon for quick recoveries. Tools like LaunchDarkly let you toggle features on and off without redeploying your entire application. This granular control allows you to quickly disable problematic features or roll back changes without disrupting your entire system. 
For example, if a feature throws a bug in production, you can selectively disable the offending feature in runtime, instantly resolving the issue. You don’t need to roll back the entire release associated with the buggy feature. You don’t need to route all production traffic back to an older version of your app. And you don’t need to rush a new version of your app through your deployment pipeline. You toggle a feature flag and resolve the problem instantly. 
5. Implement progressive rollouts and canary releases
Use progressive delivery and canary releases to deploy changes to a small subset of users first. This approach helps you catch issues early and limits the blast radius if something goes wrong.
6. Create a blameless culture
When things go wrong, focus on learning, not finger-pointing. Conduct blameless post-mortems to understand what happened and how to prevent similar issues in the future.
7. Implement runtime configuration management
Use long-term feature flags to govern important app configurations. For example, if site latency spikes dramatically due to an unexpected surge in traffic, toggle a flag to instantly disable non-essential features and services, thus improving latency (and avoiding a full outage).
8. Consider chaos engineering
Don't wait for disasters to happen—create them yourself (in a controlled way, of course). Chaos engineering involves intentionally introducing failures into your system to test its resilience. This proactive approach helps you identify and address weaknesses before they cause real outages.
9. Implement redundancy and failover mechanisms
Design your systems with redundancy in mind. Use load balancers, multi-region deployments, and automatic failover mechanisms to guarantee that a single point of failure doesn't bring down your entire application.
10. Leverage AI and machine learning for predictive maintenance
Stay ahead of issues with predictive maintenance. Use AI and machine learning algorithms to analyze system metrics and identify potential problems before they escalate into full-blown outages.
How LaunchDarkly reduces your MTTR
LaunchDarkly allows you to wrap your code in feature flags to give you unprecedented control over how and when features are released to your users. But it's not just a toggle switch—it’s a comprehensive platform that integrates seamlessly with your existing workflows to provide real-time control, detailed analytics, and the flexibility to adapt on the fly.
Features flags let you instantly disable problematic code without rolling back your entire deployment. It's essentially an "undo" button for specific features and code patches.
Noticed a performance issue with that new algorithm? Flip a switch, and it's off. Database connection acting up? Toggle it back to the old system while you investigate. 
Feature flags give you the power to isolate issues and mitigate their impact in real-time, drastically reducing your MTTR.
With real-time monitoring of your feature flags, you can watch the impact of your changes as they happen. Spot a spike in error rates or a dip in performance? You can react instantly, rolling back the change with a single click. No need to wake up the entire dev team or push a panicked hotfix. 
This real-time control means you can often resolve issues before they even impact your MTTR metrics.
In a recent survey of 250 LaunchDarkly customers, 86% recover from software incidents in a day or less, on average. 
Success stories of engineering teams improving their MTTR
DIOR reduced their MTTR from hours to minutes
Paramount used to take up to a week to fix bugs, now they resolve them in a day
Reduce your mean time to restore with LaunchDarkly
A high mean time to restore isn't a life sentence. With the right strategies, tools, and know-how, you can transform your incident response from a panic-inducing fire drill into a smooth, efficient process.
We get it: bad ship happens. But, with LaunchDarkly, you're not just fixing problems faster—you're preventing them before they start. Because in the world of software reliability, the best incident is the one that never happens.
Start your free full-access 14-day trial today, or schedule a demo with our team to learn more.
Like what you read?
Get a demoJesse SumrakLaunchDarkly
Related Content
See allRisk mitigationRTO vs RPO: Key differences for modern disaster recovery
Risk mitigationLive demo: Guarded Releases in action
Risk mitigationWelcome Highlight to LaunchDarkly: building the future of Guarded Releases together
Risk mitigationWhy I’ll never go back to the old way of deploying software
Risk mitigationFailure Recovery: Strategies for Recovering From Failed Deployments
Risk mitigationAnxiety ends here: 5 mindset shifts that changed how I ship code
Risk mitigationIntroducing Guarded Releases: confidently innovate with safer, smarter software deployments
Risk mitigationLaunch Week '24: Removing risk from every software release
Risk mitigationSoftware releases: navigating between innovation and user expectations
Risk mitigation7 key takeaways for software development teams from RedMonk’s James Governor
Inboxes love LaunchDarkly.
Make sure you get all the content, tips, and news you can use.
Work email
Yes, send me emails.twitter
YouTube
LinkedIn
Discord
Instagram
© 2025  Catamorphic Co.
Support
Support home
Request Support
Professional Services
Documentation
Status
Do not Sell or Share my Personal Information
Why Us
Economic Impact of LaunchDarkly
How LaunchDarkly works
Trust & Security
LaunchDarkly vs. Competitors
LaunchDarkly on AWS
Company
About Us
Careers
Media & Analysts
Partner Program
Terms & Policies
Contact Us
Community
Inboxes love LaunchDarkly.
Make sure you get all the content, tips, and news you can use.