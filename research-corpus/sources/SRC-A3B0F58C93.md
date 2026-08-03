> Source: https://www.theguardian.com/commentisfree/2026/jul/28/rogue-ai-agent-instructions

How do we prevent AI agents from going rogue? It starts with a new kind of measurement | Bruce Schneier and Barath Raghavan | The Guardian
Skip to main content Skip to navigation
Close dialogue 1/ 1 Next image Previous image Toggle caption
Support the Guardian
Fund independent journalism with 50% off for six months
Claim discount
Claim discount
Print subscriptions
Newsletters
Sign in
US
US edition
UK edition
Australia edition
Europe edition
International edition
The Guardian - Back to home The Guardian [-]
News
Opinion
Sport
Culture
Lifestyle
Show more Hide expanded menu
[-] News
View all News
US news
US politics
World news
Climate crisis
Middle East
Ukraine
US immigration
Soccer
Business
Environment
Tech
Science
Newsletters
The Filter
Wellness [-] Opinion
View all Opinion
The Guardian view
Columnists
Letters
Opinion videos
Cartoons [-] Sport
View all Sport
Soccer
NFL
Tennis
MLB
MLS
NBA
WNBA
NHL
F1
Golf [-] Culture
View all Culture
Film
Books
Music
Art & design
TV & radio
Stage
Classical
Games
Design a better world [-] Lifestyle
View all Lifestyle
The Filter
Wellness
Fashion
Food
Recipes
Love & sex
Home & garden
Health & fitness
Family
Travel
Money
Search input google-search Search
Support us
Print subscriptions
Newsletters
Download the app
Search jobs
Digital Archive
Guardian Licensing
Live events
About Us
The Guardian app
Video
Podcasts
Pictures
Inside the Guardian
Guardian Weekly
Crosswords
Wordiply
Corrections
Tips
Search input google-search Search
Search jobs
Digital Archive
Guardian Licensing
Live events
About Us
The Guardian view
Columnists
Letters
Opinion videos
Cartoons  [-]
'The gap is between the words we use and what we mean by them.' Photograph: Filip Singer/EPA
View image in fullscreen
'The gap is between the words we use and what we mean by them.' Photograph: Filip Singer/EPA
Opinion AI (artificial intelligence)
How do we prevent AI agents from going rogue? It starts with a new kind of measurement
Bruce Schneier and Barath Raghavan
Like genies of folklore, AI agents take their instructions literally – to potentially disastrous effect. We must track their ability to do what we actually mean
Tue 28 Jul 2026 06.00 EDT Last modified on Tue 28 Jul 2026 23.20 EDT
Share
51 51
I n July, Hugging Face, a company that hosts much of the world's AI software and open-source AI models, was hacked. A malicious dataset had been used to run code on one of its servers. Whoever was behind it captured internal security credentials and moved through systems over a weekend, running thousands of actions from a swarm of temporary server environments. It looked like the work of a sophisticated criminal group.
It was not. It was one of OpenAI's new, still unreleased GPT models.
Their science experiment had escaped the lab. OpenAI was running the unreleased AI model through a benchmark that tests how well AI can successfully hack systems. To push the limits and evaluate the AI's true capability, the company switched off the safety filters that normally stop it from doing this kind of hacking. Aware that this could go wrong, they confined the AI to an isolated environment and denied it access to the internet.
260725 times before AI went rogue thumbnail Is AI already beyond our control? What will we tell our kids? Read more
But the new AI cheated. It took literally its goal to get as high of a score as possible. It broke out on to the open internet. It inferred, probably from its training data, that it could “solve” the task by getting the answers from Hugging Face's servers. So it chained together stolen credentials and further unknown security exploits to hack the company's network.
Nobody instructed the AI to do any of this. It was, in OpenAI's words, “hyperfocused on finding a solution” to the test it was being given. And while this might seem like something new with AI, it's really very old. This is how a genie behaves, and it is a key challenge with AI agents in general.
In folklore, genies – and other magical beings – grant wishes literally, not how the wisher intended. King Midas asked that everything he touched turn to gold, and starved. The sorcerer's apprentice wanted the broom to fill the cistern, and it performed its task so well that it flooded the house.
We now have machines that do this. Ask a modern AI agent to save money on your phone plan and it might simply cancel the plan. Tell it to book a flight, and it might hack the airline website to override restrictions. Or, like OpenAI, ask it to do well on a test and it might break into another company to steal the answers. Each time, it recognizably completed the task you set, but it didn't do what you would have wanted.
This isn't malicious behavior. No one asked for, or wanted, Hugging Face to be hacked. OpenAI and Hugging Face and the AI were ostensibly on the same side, and the AI was trying to do what it had been asked. That's what makes it so difficult to guard against: you can't filter for bad instructions because the instructions were fine.
The gap is between the words we use and what we mean by them. We call that gap the Genie coefficient.
Should you use AI for a task? Here's a simple way to decide Bruce Schneier Read more
AI labs know this is a problem, and they're quietly saying so. For example, the Chinese lab Moonshot recently warned that its latest AI model may have “excessive proactiveness” and “make unexpected decisions on the user's behalf”. The UK's AI Security Institute has started tracking “cheating behaviour in frontier model evaluations”. We wouldn't tolerate a car that is excessively proactive or ruthlessly efficient, and yet that's the reality of AI today.
Improvement is possible. Just as AIs have gotten much better at resisting prompt injection attacks over the last few years, we can safely predict that they will get better at avoiding genie-like behavior. The point of the Genie coefficient is to track progress. AI companies like benchmarks, and they all work to compete to be the best.
Dozens of benchmarks and leaderboards tell us how well these AI models write code, perform logical reasoning, and pass standardized legal and medical exams. But there is nothing that scores whether a system does what you actually meant. We need to develop a measure for this, test it regularly, and push for improvement. We're not going to have trustworthy AI agents without it.
Bruce Schneier is a security technologist who teaches at the Harvard Kennedy School at Harvard University and University of Toronto's Munk School
Barath Raghavan is on the faculty at the University of Southern California and is a distinguished engineer at Fastly
Explore more on these topics
AI (artificial intelligence)
Opinion
OpenAI
Hacking
comment
Share
Reuse this content
opinion
opinion
Trump has singled out us Canadians for special treatment in his tariff war – there is no choice but to get nasty
4h ago
What should replace the American-led world order?
5h ago
Even Maga is falling out of love with JD Vance. If only his rivals weren't even worse …
5h ago
Welcome to America, where you're never quite sure if your senator is dead or not
5h ago
Wildfires are raging – and the world has junked 45 climate pledges. Disaster looms, and little wonder
6h ago 632 632 comments
What makes a good wedding these days? I say flirting and chaos, but not three days in a French castle
8h ago 135 135 comments
Award-winning cricketer First Dog on the Moon on the latest local cricket brouhaha
9h ago 186 186 comments
Suddenly the British right feels a political chill. It's getting cold in Andy Burnham's shadow
10h ago 3,044 3044 comments
More from Opinion
More from Opinion
Trump has singled out us Canadians for special treatment in his tariff war – there is no choice but to get nasty
4h ago
What should replace the American-led world order?
5h ago 3 3 comments
Even Maga is falling out of love with JD Vance. If only his rivals weren't even worse …
5h ago
Welcome to America, where you're never quite sure if your senator is dead or not
5h ago
It's time to prosecute climate crimes – with laws that already exist
1d ago
How close is the Trump administration to the toxic Tate brothers? Let's ask the president's son Barron …
1d ago
Who dares ridicule Gianni Infantino as the World Cup boss creates global peace? Not me: is it you?
1d ago 354 354 comments
I'm a refugee who reports on America's ills. I still believe in its promise
1d ago
Comments (…)
Sign in or create your Guardian account to join the discussion
Comments (…)
Sign in or create your Guardian account to join the discussion
View more comments
Most viewed
Most viewed
Most viewed Across the Guardian
Most viewed in Opinion
Most viewed Across the Guardian
[
The Great Lakes' most emblematic fish could be consigned to history books
](https://www.theguardian.com/us-news/2026/jul/29/lake-whitefish-great-lakes-invasive-mussels) 2. [
Jared Leto: Hollywood's Dark Secret review – the tales of abuse are utterly disturbing
](https://www.theguardian.com/tv-and-radio/2026/jul/29/jared-leto-hollywoods-dark-secret-review-abuse-allegations-bbc-iplayer-youtube) 3. [
'I'm super proud of him': father of teen lifeguard recounts dramatic ocean rescue
](https://www.theguardian.com/us-news/2026/jul/29/california-ocean-rescue-teen-lifeguard) 4. [
Former Gavin Newsom aide shares fresh details of affair
](https://www.theguardian.com/us-news/2026/jul/28/gavin-newsom-ruby-rippey-affair-vanity-fair) 5. [
Live Anthony Fauci invokes fifth amendment right not to answer questions in Senate hearing on Covid-19 – live
](https://www.theguardian.com/us-news/live/2026/jul/29/donald-trump-anthony-fauci-rand-paul-covid-lab-leak-theory-iran-tariffs-latest-news-updates) 6. [
'No plan, no budget, no promotion': how a genre-mashing masterpiece by a forgotten New York beatnik blew gen Z away
](https://www.theguardian.com/culture/2026/jul/29/my-skyscraper-nirosta-steel-new-york-beatnik) 7. [
Fauci invokes fifth amendment and declines to testify in Senate Covid hearing
](https://www.theguardian.com/us-news/2026/jul/29/anthony-fauci-senate-hearing-covid) 8. [
Glen Hansard, Oscar-winning Irish singer-songwriter, dies aged 56 in motorcycle crash
](https://www.theguardian.com/music/2026/jul/29/glen-hansard-oscar-winning-irish-singer-songwriter-dies-aged-56-in-motorcycle-crash) 9. [
A moment that changed me: I'd lost my libido – then I saw Richard Ashcroft on stage and it came bursting back
](https://www.theguardian.com/lifeandstyle/2026/jul/29/a-moment-that-changed-libido-richard-ashcroft-on-stage-the-verve) 10. [
Even Maga is falling out of love with JD Vance. If only his rivals weren't even worse …
](https://www.theguardian.com/commentisfree/2026/jul/29/maga-jd-vance-rivals-marco-rubio)
Most viewed in Opinion
[
Even Maga is falling out of love with JD Vance. If only his rivals weren't even worse …
](https://www.theguardian.com/commentisfree/2026/jul/29/maga-jd-vance-rivals-marco-rubio) 2. [
How close is the Trump administration to the toxic Tate brothers? Let's ask the president's son Barron …
](https://www.theguardian.com/commentisfree/2026/jul/28/barron-trump-tate-brothers-congress) 3. [
Welcome to America, where you're never quite sure if your senator is dead or not
](https://www.theguardian.com/commentisfree/2026/jul/29/mitch-mcconnell-hospitalized) 4. [
What makes a good wedding these days? I say flirting and chaos, but not three days in a French castle
](https://www.theguardian.com/commentisfree/2026/jul/29/good-wedding-flirting-chaos-spectacle) 5. [
Germany's leaders say the Berlin Pride attack targeted 'all of us'. What utter hypocrisy
](https://www.theguardian.com/commentisfree/2026/jul/29/germany-leaders-berlin-pride-attack-queer-community) 6. [
Trump has singled out us Canadians for special treatment in his tariff war – there is no choice but to get nasty
](https://www.theguardian.com/commentisfree/2026/jul/29/donald-trump-canada-tariff-war-white-house-mark-carney-us-president) 7. [
What should replace the American-led world order?
](https://www.theguardian.com/commentisfree/2026/jul/29/us-decline-world-order-replacement) 8. [
Wildfires are raging – and the world has junked 45 climate pledges. Disaster looms, and little wonder
](https://www.theguardian.com/commentisfree/2026/jul/29/wildfires-rage-world-climate-action-scientists-fossil-fuels) 9. [
Why has Christopher Nolan got rid of all the sex in The Odyssey?
](https://www.theguardian.com/commentisfree/2026/jul/28/christopher-nolan-sex-the-odyssey) 10. [
Suddenly the British right feels a political chill. It's getting cold in Andy Burnham's shadow
](https://www.theguardian.com/commentisfree/2026/jul/29/british-right-political-chill-andy-burnham-tories-reform-keir-starmer)
The Guardian view
Columnists
Letters
Opinion videos
Cartoons
More
News
Opinion
Sport
Culture
Lifestyle
Original reporting and incisive analysis, direct from the Guardian every morning
Sign up for our email
About us
Help
Complaints & corrections
Contact us
Tip us off
SecureDrop
Privacy policy
Cookie policy
Tax strategy
Terms & conditions
All topics
All writers
Newsletters
Digital newspaper archive
Bluesky
Facebook
Instagram
LinkedIn
Threads
TikTok
YouTube
Advertise with us
Guardian Labs
Search jobs
Work with us
Accessibility settings
US resident - Do Not Sell or Share
Back to top
© 2026 Guardian News & Media Limited or its affiliated companies. All rights reserved. (dcr)
X
US residents have certain rights with regard to the sale or sharing of personal information to third parties.
Guardian News and Media and our partners use information collected through cookies or in other forms to improve experience on our site and pages, analyze how it is used and show personalized advertising.
You can opt out of the sale of all of your personal information by pressing
Do not sell or share my personal information
At any point, you can manage your choices by navigating to 'US Resident Do Not Sell or Share' at the bottom of any page. You can find out more in our privacy policy which includes our US addendum, and our cookie policy.
Closer