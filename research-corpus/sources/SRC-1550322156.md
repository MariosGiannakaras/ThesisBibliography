> Source: https://www.youtube.com/watch?v=dRIhrn8cc9w

So, what we're gonna do today is we're gonna start to
talk about Model-Free Policy Evaluation.
Um, so, what we were discussing last time
is we started formally defining Markov processes,
Markov reward processes and Markov decision processes,
and we're looking at the relationship between
these different forms of processes which are
ways for us to model sequential decision-making under uncertainty problems.
So, what we're thinking about last week was,
well what if someone gives us a model of how the world works?
So, we know what the reward model is,
we know what the dynamics model is.
It still might be hard to figure out what's the right thing to do.
So, how do we take actions or how do we find a policy
that can maximize our expected discounted sum of rewards?
Um, if- even if we're given a model,
then we still need to do some computation to try to identify that policy.
So, what we're gonna get to very shortly is how do we do all of
that when we don't get a model of the world in advance.
But, let's just first a recap,
um, sort of this general problem of policy evaluation.
So, we heard a little bit about policy evaluation last time when we talked
about policy evaluation as being one step inside a policy,
um, iteration which alternated between policy evaluation and policy improvement.
So, the idea in policy evaluation is somebody gives you
a way to act and then you want to figure out how good that policy is.
So, what is the expected discounted sum of rewards for that particular policy?
And what we're gonna be talking about today is dynamic programming,
Monte Carlo policy evaluation, and TD learning.
As well as some of the ways that we should think
about trying to compare between these algorithms.
So, just as a brief recall, um,
remember that last time we defined what a return is for Markov reward process.
And a return for a Markov reward process that we defined by G_t was
the discounted sum of rewards we get from that particular time point t onwards.
So, we're gonna get an immediate reward of Rt and then after that,
we're gonna get Gamma,
where Gamma was our discount factor.
And remember we're gonna assume that's gonna be somewhere between zero and one.
And so, we're sort of weighing future awards generally less than the immediate rewards.
The definition of a state value function was the expected return.
And in general, the expected return is gonna be different from
a particular return if the domain is stochastic,
because the [NOISE] reward you might get when you try to drive to the airport
today is likely gonna be different than
the reward you get when you drive to the airport tomorrow,
because traffic will be slightly different,
and it's stochastic, varies over time.
And so, you can compare whether, you know,
on a particular day if it took you two hours to get to the airport versus on average,
it might take you only an hour.
We also defined the state action value function which was the expected reward,
um, if we're following a particular policy Pi but we start off by taking an action a.
[NOISE] So, we're saying if you're in a state s,
you take an action a, and from then onwards,
you follow this policy Pi that someone's given you.
What is the expected discounted sum of rewards?
And we saw that Q functions were useful because we
can use them for things like policy improvement,
because they allowed us to think about, well,
if we wanna follow a policy later but we do something slightly different to start,
can we see how that would help us improve in terms of the amount of reward we'd obtain?
So, we talked about this somewhat but as a recap, um,
we talked about doing dynamic programming for policy evaluation.
So, dynamic programming was something we could apply when we know how the world works.
So, this is when we're given the dynamics,
and I'll use the word dynamics or transition model interchangeably in this course.
So, if you're given the dynamics or the transition model p and the reward model,
then you can do dynamic programming to evaluate how good a policy is.
And so, the way we talked about doing this is that you initialize your value function,
which you could think of generally as a vector.
Right now, we're thinking about there being a finite set of states and actions.
So, you can initialize your value function for this particular policy to be zero,
um, and then you iterate until convergence.
Where we say the value of a state is exactly equal to
the immediate reward we get from following that policy in that state plus
the discounted sum of future rewards we get [NOISE]
using our transition model and the value that we've computed from a previous iteration.
And we talked about defining convergence here.
Convergence generally we're gonna use some sort of norm to compare
the difference between our value functions on one iteration and next.
So, we do things like this,
V_Pi_k minus V_Pi at k minus one [NOISE].
And wait for this to be smaller than some Epsilon.
Okay. So, just as a reminder to what is this quantity that we're computing representing?
Well, we can think of this quantity that we're computing, um,
as being an exact value of the k horizon value of state s under that policy.
So, on any particular iteration,
it's as if we know exactly what value we would get if we could
only act for a finite number of time steps like k time steps.
Says, you know, how good would it be if you followed
this particular policy for the next k time steps?
Equivalently, you can think of it as an approximation
of what the value would be if you acted forever.
So, if k is really large,
k is 20 billion,
then it's probably gonna be a pretty good approximation
to the value you'd get if you'd act forever.
And if k is one,
that's probably gonna be a pretty bad estimate.
This will converge over time.
So, I think it's useful to think about some of these things graphically as well.
So, let's think about this as you're in a state s,
which I'm denoting with that white circle at the top and then you can take an action.
So, what dynamic programming is doing is it's computing
an estimate of the V_Pi here at the top by saying,
"What is the expectation,
expectation over Pi of RT plus Gamma V_k minus one.
And what's that expectation over it's gonna be the probability of s prime given s,
Pi of s. Okay.
So, how do we think about this graphically?
Well, we started in this state,
we take an action and then we think about the next states that we could reach.
We're kind of again assuming that we're in a stochastic process.
So, maybe, you know, sometimes the red light is on and sometimes the red light is off.
So, depending on that, we are gonna be at a different next state,
we're trying to drive to the airport.
And then we can think about after we reach that state,
then we can take some other actions.
And in particular, we can take one action in this case because
we're assuming we're fixing what the policy is.
And then from those, that,
those actions would lead us to other possible states.
So, we can think of sort of drawing the tree of trajectories that we might
reach if we started in a state and start following our policy,
where whenever we get to make a choice,
there's a single action we take because we're doing policy evaluation.
And whenever there's sort of nature's choice,
then there's like a distribution over next states that we might reach.
So, you can think of these as the S-prime and
the S double-primes kind of time is going down like this.
So, this is sort of you know the,
the potential futures that your agent could arise in.
And I think it's useful to think about this graphically because
then we can think about how those potential futures,
um, how we can use those to compute what is the value,
a difference of this policy.
So, um, in what dynamic program what we're doing and
in general when we're trying to compute the value of a policy is,
we're gonna take an expectation over next states.
So, the value is the expected discounted sum of future rewards if we follow this policy,
and the expectation is exactly over these distributions of futures.
So, whenever we see
an action and then we think about all the next possible nodes we could get to,
we want to take an expectation over
those features and expectation over all the rewards we could get.
So, that's what dynamic programming is
or that's what we can think of this graph is doing.
And when we think about what dynamic programming is doing,
is it estimates this expectation over
all those possible futures by
bootstrapping and computing a one timestep expectation exactly.
So, what does it do? Again, it says,
"My V_Pi of s is exactly equal to r of s, Pi of s,
my immediate reward plus Gamma sum over probability of s prime given
s a V_Pi k minus one, the best part.
So, it bootstraps, and we're using the word bootstraps there because it's not
actually summing up all of these lower down potential rewards.
It's saying, "I don't need to do that."
Previously, I computed what it would be like if I started say
in this state and continued on for the future.
And so, I, now I already know what the value is at that state,
and I'm gonna bootstrap and use that as
a substitute for actually doing all that roll-out.
And also here, because I know what the expected discounted or I know what the,
um, sorry, the model is,
that it can also just take a direct expectation over s prime.
So, my question is, is there an implicit assumption here that
the reward at a given state and
thus the value function of evaluated states doesn't change over time.
So, like because you're using it from the prior iteration?
So, I think that question is saying, um,
is there an explicit assumption here that the value doesn't change over time?
Yes. The idea in this case is that the value that we're
computing is for the infinite horizon case and therefore that it's stationary.
It doesn't depend on the time step.
From that way we're not gonna talk very much about the finite horizon case today,
in that case it's different.
In this situation, we're saying at all time
steps you always have an infinite number more time steps to go.
So, the value function itself is a stationary quantity.
So, why is this an okay thing to do like we're bootstrapping?
Um, the reason that this is okay is because we actually have
an exact representation of this V_k minus one.
You're not getting any approximation error of putting that in
instead of sort of explicitly summing over lots of different histories.
Sorry, lots of different future rewards.
So, when we're doing dynamic programming
the things to sort of think about here is if we know the model,
then know dynamic model and know the reward model,
that we can compute the immediate reward exactly.
We can compute our expected sum over future states exactly,
and then we substitute in instead of thinking about,
we, instead of thinking about expanding this out as being a sum over rewards,
we can just bootstrap and use our current estimate of V_k minus one.
And the reason that I'm emphasizing this a lot is that when we start to
look at these other methods like Monte Carlo methods and TD methods,
they're not gonna do this anymore.
They're gonna do other forms of approximation of trying to compute this tree.
So, ultimately to compute the value of a policy,
what we're essentially doing is we're thinking about
all possible futures and what is the return we'd get under each of those futures.
And we're trying to make it tractable to compute that particularly when we don't know how
the world works and we don't have access to the dynamics model or the reward model.
Okay. So, just to summarize dynamic programming,
we should talk a little- a little bit about last time,
but we didn't really talk about the bootstrapping aspect.
Dynamic programming says the value of a policy is approximately equal to
the expected next- the expectation over pi of
immediate reward plus gamma times the previous value you computed requires a model,
it bootstraps the future return using an estimate,
using your V_k minus 1.
And it requires the Markov assumption.
And what- what I mean by that there is that, um,
you're not thinking about all the past you got to reach a certain state.
You're saying no matter how I got to that previous state,
my value of that state is identical,
um, and I can sort of assume that,
and I can compute that singly based on the current observation.
So, may I have any questions about this.
So, right now we're mostly recap of last time, um,
but sort of slightly pointing out some things that I didn't point out before.
Okay. So, those things are useful now that we're gonna be
talking about policy evaluation without a model.
So, what we're going to talk about now is Monte Carlo policy evaluation
which is something that we can apply when we don't know what the models are of the world,
and we're gonna talk a little bit about how we can start to think
about comparing these different forms of estimators,
estimators of the value of a policy.
So, in Monte Carlo policy evaluation,
um, we can again think about the return.
So, the returning and G_t are discounted sum of future rewards under a policy,
and the value of a policy we can represent now is just,
let's think about all the possible trajectories we could get,
um, under our policy and what's average all their returns.
So, we can again think about that tree we just constructed.
Each of those different sort of branches would have had a particular reward,
um, and then we're just going to get the average over all of them.
So, it's a pretty simple idea.
The idea is that the value is just equal to your expected return.
And if all your trajectories are finite,
you just can take a whole bunch of these and you average.
So, the nice thing about Monte Carlo policy evaluation is it doesn't require you to
have a sp- a specific model of the dynamics or reward.
It just requires you to be able to sample from the environment.
So, I don't need to know a particular like parametric model of how traffic works.
All I have to do is drive from here to the airport, you know,
hundreds of times, and then average how long it takes me.
And if I'm always driving with the same policy,
let's say I always take the highway,
um, then if I do that,
you know, 100 times, then I have
a pretty good estimate of what is
my expected time to get to the airport if I drive on the highway.
Well that is my policy.
So, it doesn't do bootstrapping,
it doesn't try to maintain at this root V_k minus 1.
Um, it's simply sums up all the rewards from each of
your trajectories and then averages across those.
It doesn't assume the state is Markov.
Just averaging doesn't- there's
no notion of the next state and whether or not that sufficient to,
um, to summarize the future returns.
An important thing is that it can only be applied to what are known as episodic MDPs.
You act forever if there's no notion
of- if this is sort of like averaging over your life this doesn't work,
[LAUGHTER] because, you only get one.
So, you need to have a process where you can
repeatedly do this many times and the process will end each time.
So, like driving to the airport might be really long,
but you'll get there eventually and then you can try again tomorrow.
So, this doesn't work for all processes like if
you have a robot that's just going to be acting forever,
can't do Monte Carlo policy evaluation.
Okay. So, we also often do this in
an incremental fashion which means that after we maintain a running estimate,
after each episode, we update our current estimate as V_pi.
And our hope is that as we get more and more data,
this estimate will converge to the true value.
So, let's look at, um, what the algorithm for this would be.
So, one algorithm which is known as
the First-Visit Monte Carlo on policy evaluation algorithm,
as we start off and we assume that we haven't- N here
is essentially the number of times we visited a state.
So, we start off and this is zero.
Also the return- the- or average return from starting in any state is also zero.
So, we initialize say right now or we think that
you know we get no reward from a state and we haven't visited any state.
And then what we do is we loop.
And for each loop we sample an episode which is we start in
the starting state and we act until our process terminates.
I start off at my house and I drive until I can get to the airport.
And then I compute my return.
So, I say okay, well maybe that took me two hours to get there.
So, now my G-i is two hours.
Um, but you've just compute your return and you compute it for
every time step t inside of the episode.
So, G_i,t here is defined from the t time step in that episode,
what is the remaining reward you got from that time step onwards,
and we'll instantiate this in our Mars Rover example in a second.
And then for every state that you visited in that particular episode,
for the first time you encountered a state,
you look- you increment the counter and you update your total return.
And you use, then you just take an average of those estimates to
compute your current estimate of the value for the state.
Now why you might be in the same state for more than one time step in an episode.
Well let's say I get to the red light, let's say I've discredited my time steps.
So, I look at my state every one minute.
Well, I got to a red light and there was a traffic accident.
So, on time step one I'm at the red light,
time step two I'm on the red light,
time step three I'm on the red light.
And so you can be in the same state for multiple time steps during the episode.
And what this is saying is that you only use the first time step you saw that state.
And then you sum up the rewards you get til the end of that episode. Okay.
We saw the state but in,
I guess like different time steps and the same episode,
we'd still be incremented twice because it's not- there's gonna be a gap between them?
The question is, what happens if we,
um, see the same state in the same episode?
In first visit, you only use the first occurrence.
So, you drop all other ones.
So, the first time I got to my red light then I would
sum up the future rewards till the end of the episode.
If I happen to get to the same red light during the same episode, I ignore that data.
We'll see a different way of doing that in a second.
Okay. So, how do we estimate whether or not this is a good thing to do.
How do we evaluate whether or not this particular- this is an estimate.
It's likely wrong at least at the beginning where we don't have much data.
So, how do we understand whether or not
this estimate is good and how are we going to compare
all of the estimators and these algorithms that we're going to be talking about today.
So, um, actually just raise your hand because I'm curious.
Um, who here has sort of formally seen definitions of bias and variance in other classes.
Okay. Most people but not quite everybody.
So, just as a quick recap, um,
let's think about sort of having a statistical model that is parameterized by theta,
um, and that we also have some distribution over some observed data p of x given theta.
So, we want to have a statistic theta hat which is a function.
So, theta hat is a function of the observed data and it provides an estimate of theta.
So, in our case, we're going to have this value,
this estimate of the value we're computing.
This is a function of our episodes and this is an estimate of the
true discounted expected rewards of following this policy.
So, the definition of a bias of an estimator is to compare what is
the expected value of our statistic versus the true value,
for any set of data.
So, this would say,
if I compute, you know,
the expected amount of time for me to get to
the airport based on trying to drive there three times.
Does the algorithm that I just showed you is that unbiased?
On average is that the same is the true expected time for me to get to the airport.
The definition of a variance of an estimator compares
my statistic to its expected value squared.
Expected over the, er, the, um,
the type of data I could get under
the true parameter and the mean squared error combines these two.
Mean squared error is normally what we care about.
Normally, we ultimately care about sort of how far away is
our estimate of the quantity we care about versus the true quantity?
And that's the sum of its bias and its variance.
And generally, different algorithms and
different estimators will have different trade offs between bias and variance.
Okay. So, if we go back to our First-Visit Monte Carlo
algorithm the V_pi estimator that we use there is
an unbiased estimator of the true expected discounted sum of rewards from our policy.
It's just a simple average, um, and it's unbiased.
And by the law of large numbers,
as you get more and more data,
it converges to the true value.
So, it's also what is known as as consistent.
Consistent means that it converges to the true value as the- as data goes to infinity.
So, this is reasonable, um,
but it might not be very efficient.
So, ah, as we just talked about,
you might be in the same state, you might be at
the same stoplight for many, many time steps.
Um, and you're only going to use the first state in an episode to update.
So, every visit at Monte Carlo,
simply says well every time you visit a state during the episode,
look at how much reward you got from that state
till the end and average over all of those.
So, essentially every time you reach a state,
you always look at the sum of discounted rewards
from there to the end of the episode and you average all of that.
Which is generally going to be more data efficient.
Bias definition, I guess I'm just a little confused how we would get biased,
even if we don't actually know theta.
How we compute bias. [NOISE]
Yeah, given that we don't know theta.
It's a great- the question is how do you compute bias?
Yes, if you, uh,
if you can compute bias exactly that normally means you know what theta is,
in which case why are you doing an estimator?
Generally, we do not know what bias is,
um we can often bound it.
So, often using things like concentration inequalities we can,
um, well concentration qualities are more for variance.
Often, um, we don't know exactly what the bias is,
unless you know what the ground truth is.
And there are different ways for us to get estimates of bias in practice.
So, as you compare across different forms of parametric models,
um, sometimes you can do is structural risk, ah, ah,
structural risk maximization and things like that to try to get
sort of a quantity of how you compare your estimator and your model class.
I'm not going to go very much
into that here but I'm happy to talk about it in office hours.
So, in every visit Monte Carlo,
we're just gonna update it every single time.
And that's gonna give us another estimator.
And note that that's gonna give us generally a lot more counts.
Because every time you see a state,
you can update the counts. But it's biased.
So, you can show that this is a biased estimator of
V_pi. May have intuition of why it might be biased.
So, in the first case for those of you that have seen this
before or not necessarily this particularly but seen this sort of analysis.
First visit Monte Carlo,
is you're getting IID estimates of a state,
of a state's return right?
Because you only take that, um,
each episode is, is
IID because you're starting at a certain state and you're estimating from there.
Ah, and you only use the return for the first time you saw that state.
If you see a state multiple times in the same episode,
are their returns correlated or uncorrelated?
Correlated. Okay. So, your data is no longer IID.
So, that's sort of the intuition for why when you mod- move to every visit Monte Carlo,
your estimator can be biased 'cause you're not averaging over IID variables anymore.
Is it biased for an obvious reasons to inspectors paradox? [inaudible]
I don't know. That's a good question.
I'm happy to look at it and return.
However, the nice thing about this is that it is a consistent estimator.
So, as you get more and more data,
it will converge to the true estimate.
And empirically, it often has way lower variance.
And intuitively, it should have way lower variance.
We're averaging over a lot more data points,
uh, typically in the same.
Now, you know, if you only visit one-
if you- if you're very unlikely to repeatedly visit the same state,
these two estimators are generally very close to the same thing in an episode.
Because you're not gonna have multiple visits to the same state.
But in some cases you're gonna visit the same state a
lot of times and you get a lot more data
and these estimators will generally be much better if you use every visit,
but it's biased. So, there's this trade-off.
Empirically, this is often much better.
Now, of course in practice often instead
of the- often you may wanna do this incrementally.
You may just want to kind of keep track of a running mean and then
you keep track of your running mean and update your counts sort of incrementally.
And you can do that if also as you visit you don't
have to wait until the end lessons- oh, that's wrong.
You do have to wait till the end because you always have to wait till you
get the full return before you can update. Yeah, in the back.
So, a question on that, if you could like- if you condition on the fact that you have
the same number of estimates approximately in each of the states,
would then the two be more or less equivalent but the other one would be less biased.
For example, if you did I guess there is no way you could
have for example a same number of episodes,
ah, the same number of count in each state with the first visit approximation.
But if you did have that,
would you imagine that the episode would be lower in that case?
I would- expressions about if you have
the same number of counts to a state across the two algorithms.
And in terms of the episodes,
you couldn't have that be the case
unless- so they'd need to be identical if you only visit one state,
um, once in an episode and then they'd be totally identical.
If it's not the case, if you visit, um,
a state multiple times in,
in one episode, then, uh,
by the time you get to the same counts,
the one for the single visit would be
better 'cause it's unbiased and it would have basically the same variance.
Any other questions about that?
Cool. Um, so, incremental Monte Carlo, um,
on policy evaluation is essentially the same as before except where you can
just sort of slowly move your running average for each of the states.
And the important thing about this is that,
um, as you slowly move your estimator,
if you set your alpha to be 1 over Ns,
it's identical to every visit Monte Carlo.
Essentially, you're just exactly computing the average.
Um, but you don't have to do that.
So, you can skew it so that you're running average is more weighted towards recent data.
And the reason why you might wanna do that is
because if your real domain is non-stationary.
We have a guess of where,
where domains might be non-stationary.
It's kind of an advanced topic.
We're not gonna really talk about non-stationary domains for most of
this class though in reality, they're incredibly important.
Um, I don't know if your mechanical parts are breaking down or something's off.
Example of like if you're in a manufacturing process and
your parts are changing- are breaking down over time.
So, your dynamics model is actually changing over time.
Then you don't want to reuse your old data because
you're- actually your MDP has changed over time.
So, this is one of the reasons often empirically like when
people train recommender systems and things like that,
you know, the, the news all these things are non-stationary.
And so people often retrain them a lot to deal with this non-stationarity process.
Do I see a question on the back?
Okay. Yeah. So, empirically that's often really helpful for non-stationary domains,
but if it's non-stationary there's all- there's a bunch of different concerns.
So, we're going to mostly ignore that for now.
Okay. So, let's just check our understanding for a second.
For Monte Carlo, for on policy evaluation.
Let's go back to our Mars rover domain.
So, in our Mars rover,
we had these seven states. Our rover dropped down.
It was gonna explore,
a reward is in state S_1,
one and state S_7 it's plus 10 everywhere else at zero.
And our policy is gonna be A_1 for all states.
And now imagine we don't know what the dynamics model is.
So, we're just gonna observe trajectories.
And if you get to either state one or state seven,
the next action you take terminates the reward.
I don't know. Maybe it falls off a cliff or something like that.
But whenever you get to S_7 or S_1,
then the next action you take so you get whatever reward.
You either get the one or you get the 10 and then your process terminates.
So, let's imagine a trajectory under this policy would be you start in S_3.
You go to action- take action A_1,
you get a reward of zero. This is for reward.
Then you transition to state S_2,
you take an action of A_1, you get a zero.
You stay in the same state.
So, you stay in S_2 again.
Take action A_1, you get another reward of zero and then you reach state S_1,
take an action A_1,
you get a 1 and then it terminates.
So, it's one experience of your Mars rover's life.
So, in this case,
how about we just take a minute or two,
feel free to talk to a neighbor and compute what
is the first visit Monte Carlo estimate of
the value of each state and what is the every visit Monte Carlo estimate of state S_2?
Then I put the algorithm for both first visit at every visit above just depends on
whether you update the state only once for
this episode or whether you can potentially update it multiple times.
[NOISE] You may ask the question too if we have not seen it yet what is the value we use.
So, the value you can also say that you initialize V_Pi of S
equal to zero for all S if you haven't seen it yet.
[NOISE] All right.
Raise your hand if you'd like a little bit more time otherwise we'll go ahead.
Okay. So what- someone wanna to share what they and maybe somebody nearby them
thought was the first visit Monte Carlo estimate of V for every state.
I think the first- this estimates is
really one for every single state except for the last one that's sent.
Which states? We've only updated a few of them so far.
Which why don't you give me the full vector.
Like okay we'll just start here.
So, V of S_1 is what?
Is one.
Okay. And V of S_2?
Is also one.
And V of S_3?
Is also one.
And V of S_4?
Also one. [NOISE].
Anybody disagree.
Zero.
Zero. Okay and V of S_5? Zero. And V of S_6?
Zero.
And V of S_7? [OVERLAPPING] Yeah.
So, we only get to update in this one that the states we've actually visited.
Okay. So, here it's one,
one, one. Zero, zero, zero, zero.
Now what about for every visit the Monte Carlo estimate of just S_2.
So, I picked only S_2 'cause that's the only state we visit twice.
What's its, what's its estimate?
Well, we increment. Yeah.
Is it still gonna be one?
Yeah, yes it is and why?
Because incremental also we have Ns is two at the end of it but Gs is also two.
So, the increment both twice.
Exactly. So, the return from both times when you started in
S_2 and got an added up till the end of the episode was one in both cases.
So, it was one twice and then you average over that so it's still one. Yeah.
Is the reason that they're all one because gamma's one?
'Cause like shouldn't there be some gamma terms in there.
Oh, good question. So, here we've assumed gamma equals one,
otherwise there would be- there'd be a gamma multiplied into some of those two.
Yeah, good question.
I chosen gamma equal to one just to make the math a little bit easier.
Otherwise, it'd be a gamma factor tpo. Okay great.
So, you know, the, the second question is a little bit of
a red herring because in this case it's exactly the same.
But if the return had been different from S_2, um,
like let's say there was a penalty for being in a state,
then they could have had different returns
and then we would have gotten something different there.
Okay. So, Monte Carlo in this case updated- we had to wait till the end of the episode,
but when we updated it till the end of the episode,
we updated S_3, S_2, and S_1.
So, what is Monte Carlo doing when we think about
how we're averaging over possible futures.
So, what Monte Carlo is doing, um,
I've put this sort of incremental version here which you could
use for non-stationary cases but you can think of it in the other way too.
Um, so, and remember if you want this just to be equal to every visit,
you're just plugging in 1 over N of S here for alpha.
So, this is what Monte Carlo Evaluation is doing
is it's just averaging over these returns.
So, what we're doing is if we think about sort of what our tree is doing,
in our case our tree is gonna be finite.
We're gonna assume that each of these sort of branches eventually terminate.
They have to because we can only evaluate a return once we reach it.
So, at some point like here when we got to state S_1 or
S_7 in our Mars example, the process terminated.
And so what does Monte Carlo policy evaluation do?
It approximates averaging over all possible futures by summing up one,
uh, trajectory through the tree.
So, it samples the return all the way down till it gets to a terminal state.
It adds up all of the rewards along the way.
So, like reward, reward, reward.
Well, I'll be more careful than that.
Reward, reward.
Here you get a reward for each state action pair.
So, you sum up all the rewards in this case.
Um, and that is its sample, um, of the value.
So, notice it's not doing any, um, er,
the way it's gonna get into the expectation over states,
is by averaging and across trajectories.
It's not explicitly looking at the probability of
next state given S and A and it's not bootstrapping.
It is only able to update,
when you get all the way out and see the full return.
So, so, this is it samples.
It doesn't use an explicit representation of a dynamics model,
and it does not bootstrap because there's no notion of VK minus 1 here.
It's only summing up a- all of the returns. Questions? Scotty.
[inaudible] policy evaluation like this would do a very poor job in rare occurrences?
Well, it's interesting. Question is,
is it fair to say that this would do a really bad job in very rare occurrences?
It's intriguing. They're very high variance estimators.
So if you're- Monte Carlo,
in general, you essentially just like rolling out futures, right?
And often you need a lot of possible futures until you can get a good expectation.
On the other hand, for things like AlphaGo which is one of
the algorithms that was used to solve the board game Go, they use Monte Carlo.
So, you know, I think, um,
you wanna be careful in how you're doing some of
this roll out when you start to get into control.
And when you start to- because then you get to pick the actions, um,
and you often kind of want to play between,
but it- it's not horrible even if there's rare events.
Um, er, but if you have other information you can use, it's often good.
It depends w-what your other options are.
So, generally this is a pretty high variance estimator.
You can require a lot of data,
and it requires an episodic setting because you
can't do this if you're acting forever because there is no way to terminate.
So, you have to be able to tell processes to terminate.
So, in the DP Policy Evaluation we had the gamma factors,
because we wanted to take care of the cases
where state were seen in-between that started with a probability equals to one.
But in this case, um,
if we had such a case that would never terminate,
right, because the episode would never end.
So, technically, do we still need a gamma factor to evaluate policy equation,
uh, policy evaluation on?
The question was about,
do we still need a gamma factor in these cases,
and what about cases where you could have self-loops or small loops in your process?
So, um, this G in general can,
you know, can use a gamma factor.
So, this can include a gamma when you compute those.
You're right, that if the process is known to terminate,
you don't have to have a gamma less than one because
your reward can't be infinity because your process will always terminate.
Um, this could not handle cases where there's some probability it will terminate.
So, if there is a self-loop inside of- or a small loop inside of your process,
such that you could go round it forever and never terminate,
you can't do Monte Carlo, and having a good discount there won't help.
There are physical reasons why you might have a gamma models like that, which is great,
say you model the fuel cost or something,
or something would interact, would that be reasonable?
The question is whether or not there might be a physical reason for
gamma like fuel costs or things like that.
I mean, I think normally I would put that into the reward function.
Good. So, if you have something like- you can have it.
So, I keep thinking about cases where
basically you want to get to a goal as quickly as possible,
um, and you want to sort of do a stochastic shortest paths type problem.
Um, I think generally there I would probably rather pick making it a terminal
state and then having like
a negative one cost if you really have a notion of how much fuel costs.
Um, but you can also use it as a proxy to try to encourage quick progress towards a goal.
The challenge is that how you set it is often pretty subtle because if you set it
too high you can get weird behavior where
your agent has sort of effectively like too scared to do anything,
it will stay at really safe areas.
Um, and if it's too high in some cases,
if it's possible to get sort of trivial reward,
your agent can be misled by that.
So, it's often a little bit tricky to set in real-world cases.
Okay. So, they're high variance estimators that require these episodic settings,
um, and, um, there's no bootstrapping.
And generally, they converge to the true value under some,
uh, generally mild assumptions.
We're gonna talk about important sampling at the end of class if we have time.
Otherwise, we'll probably end up pushing that towards later.
That's for what how we do this if you have off policy data,
data that's collected from another policy.
Okay. Now let's talk about temporal difference learning.
So, if you look at Sutton and Barto, um,
and if you talk to Rich Sutton or, ah,
number of, uh, and a number of other people that are very influential in the field,
they would probably argue that these central, um,
contribution to reinforcement learning or contribution to reinforcement learning
that makes it different perhaps than some other ways of thinking about adaptive control,
is the notion of temporal difference learning.
And essentially, it's going to just combine between
Monte Carlo estimates and dynamic programming methods.
And it's model-free.
We're not going to explicitly compute a dynamics model or reward model or
an estimator of that from data and it both bootstraps and samples.
So, remember, dynamic programming as we've defined it so far,
um, it bootstraps, er,
and the way we have thought about it so far you actually have access
to the real dynamics model and the real reward model,
but it bootstraps by using that VK minus one.
Monte Carlo estimators do not bootstrap.
They go all the way out to the end of the trajectory and sum up the rewards,
but they sample to approximate the expectation.
So, bootstrapping is used to approximate the future discounted sum of rewards.
Sampling is often done to approximate your expectation over states.
The nice thing about temporal difference learning is you can do it
in episodic processes or continual processes.
And the other nice aspect about it is that you don't have to wait till the end of the,
uh, the episode to update.
So as soon as you get a new observation, taking, ah,
starting in a state taking an action and going to a next state and getting some reward,
um, you can immediately update your value.
And this can be really useful because you can
kind of immediately start to use that knowledge.
Okay. So, what are we gonna do in temporal difference learning?
Again, our aim is to compute our estimate of v pi.
And we still have the same definition of return,
um, and we're gonna look at remind ourselves of the Bellman operator.
So, if we know our MDP models,
our Bellman operator said we're gonna get
our immediate reward plus our discounted sum of future rewards.
And in incremental every visit Monte Carlo,
what we're doing is we're updating our estimate using one sample of the return.
So, this is where we said our va-
our new value estimate of the value is equal to our old estimate
plus alpha times the return we just saw minus
V. But this is where we had to wait till the end of the episode to do that update.
What the inside of temporal difference learning is, well,
why don't we just use our old estimator of
v pi for that state and then you don't have to wait till the end of the episode.
So, instead of using GI there you use the reward you just saw plus
gamma times the value of your next state. So, you bootstrap.
Say I'm not going to wait till I get only an episode,
started my state, I got a reward,
I went to some next state.
What is the value of that next state? I don't know.
I'll go look it up in my estimator and I'll plug that in and I'll treat that as,
uh, as an estimate of the return.
So, the simplest TD learning algorithm is exactly that,
where you just take your immediate reward plus your
discounted expected future value
where you plug that in for the state that you actually reached.
Now, notice that this is sampling.
There is no- normally we would have like that nice sum.
The Bellman operator we would normally have a sum over
S prime probability of S prime given s a of v pi of S prime.
We don't have that here.
We're only giving you a single next state.
And we're plugging that in as our estimator.
So we're still going to be doing sampling to approximate that expectation.
But just like dynamic programming we're going to bootstrap
because we're gonna using our previous estimate of v pi.
We also write this as like a sub a and sub k minus one to show like the iterations.
Yeah. I might have down there if you want to see. No, I don't in this case.
You could also write this with- um,
question is if we want just to be clear about what is happening in terms of iterations.
You can also think of this as p of k plus one and this is V of k,
for example, you're updating this over time.
The thing is is that you're doing this for
every single state compared to dynamic programming,
where you do this in ways where for all states-
so you have sort of a consistent VK and then you're updating.
Here we can think of there as just being a value function and you're just sort of
updating one entry of that value function depending on which state you just reached.
So there's not kind of this nice notion of
the whole previous value function of any value function.
I'll keep that there just for that reason.
Now, people often talk about the TD error,
the temporal difference error.
What that is is it's comparing what is your estimate here.
So, your new estimate,
which is your immediate reward plus gamma times your value of the state you actually
reached minus your current estimate of your value.
Now, notice this one should have been sort of essentially
approximating the expectation over S prime.
Because for that one you're going to be averaging.
And so this looks at the temporal difference.
So this is saying how different is
your immediate reward plus gamma times your value of your next state,
versus your sort of current estimate of the value of your current state.
Now note that that doesn't have to go to zero because
that first thing is always ever just a sample, it's one future.
The only time this would be defined to go to zero is if this is deterministic,
so there's only one next state.
So, you know, if half the time when I try to drive to
the airport I hit traffic and half the time I don't,
then that's sort of two different next states
that I could go to for my current start state,
either hit traffic or don't hit traffic.
Um, and so I'm either going to be getting that v
pi of hitting traffic or v pi of not hitting traffic.
So this TD error will not necessarily go to zero even with infinite data because one is
an expected thing from the current state and the
other is which actual next state did you reach.
So, the nice thing is that you can immediately update this
value estimate after your state action
reward s prime tuple and you don't need episodic settings. Yeah, Scotty?
Does that affect convergence if you keep alpha constant?
Yes, good question. Does this affect convergence if you keep alpha constant?
Yes, and you normally have to have some mild assumptions on decaying alpha.
So, things like one over T is normally
sufficient to ensure these estimates convert. Yeah, question?
Um, can you say anything about the bias of this estimator?
Yeah. The question was whether- question was a good one,
what can you say anything about the bias of this estimator?
Am I having a sense of whether this is going to be a biased estimator?
What of your previous or we have a sense of whether it's going to be biased?
Well think back to dynamic programming,
was V_k minus one.
Um, an unbiased estimator of infinite horizon.
Like, let's say, k is equal to two if we want the infinite horizon value.
Is that- no matter how you've done those updates, it's not going to be cool.
Generally, when you bootstrap, um,
it's going to be a biased estimator because you're
relying on your previous estimator which is generally wrong.
[LAUGHTER]. So, that's going to be biasing you in one particular direction.
So, it's a definitely a biased estimator.
Um, it also can have fairly high variance.
[LAUGHTER]. So, it can both be high-variance and be biased.
But on the other hand, you can update it really, really quickly.
Um, you don't have to wait till the end of the episode and you can use a lot of information.
So, it's generally much less high-variance than, um, im- um,
Monte Carlo estimates because you're
bootstrapping and that sort of helping average over a lot of your of variability.
[inaudible]
Now, this question is whether or not it's a function of the initialization. It's not.
It's a, it's a function of the different properties of
the estimators you could initialize differently.
Um, the, the bootstrapping is because you're using a- by bootstrapping and
using this V_Pi as a proxy for your real expected discounted sum of returns,
um, unless this is the true value,
it's just going to bias you.
Note that this, um, this doesn't- you don't get biased in
dynamic programming when you know the models because that V_Pi,
when you bootstrap it's actually V_Pi.
This is actually the real value.
So, the problem is the- here is that it's
an approximation of the real value and that's why it's biasing you.
So bootstrapping is fine if you know the real dynamics model.
The real reward functions,
you need computed the Pi of k minus one exactly,
um, but it's not okay here because we're introducing bias.
So, how does TD zero learning work?
Um, I do zero here because there's sort of some interesting, um,
in-between between TD learning and Monte-Carlo learning where instead of doing
an immediate reward plus the discounted sum of
future rewards versus summing all of the rewards,
you can imagine continuums between these two where you
may be- some up the first two rewards and then Bootstrap.
[NOISE]. So, there's, um,
there's a continuum of models,
there's a continuum of algorithms between just taking
your immediate reward and then bootstrapping versus never bootstrapping.
Um, but we're just gonna talk right now about
taking your immediate reward and then bootstrapping.
So TD learning works as follows: You have to pick a particular alpha,
um, which can be a function of the time-step.
Um, you initialize your value function,
you sample a state action reward, next state.
Now in this case,
because we're doing policy evaluation,
let me- this will be equal to Pi of st,
and then you update your value.
Okay. So let's look, um,
again at that example we had before.
So we said that for first visit Monte Carlo,
you will get 1110000,
for every visit it would be one.
What is the TD estimate of all states at the end of this episode?
So, notice what we're doing here.
We loop, we sample a tuple,
we update the value of the state we just reached.
We get another tuple, we sample it.
So, what would that look like in this case?
We would start off and we'd have S3,
we'd have S3, A1, zero, S2.
You'd have S2, A1, zero, S2, S2,
A1, zero, S1, S1,
A1 plus one, terminate.
So, why don't you spend a minute and,
and think about what the value would be under TD learning,
and what implications this might have too.
[NOISE].
Does anybody wanna say what the value is,
that you get? [NOISE]. Yeah.
Uh, one followed by all zeros.
That's right. Okay. One followed by all zeros.
So, we only updated the final state in this case.
I also just wanted to- yeah, question.
Um, explain why that happens.
Yeah, because, um, what we are doing in
this case is that we get a data point so what- we're in a state,
we take an action, we get a reward, we get next state.
We update the value only for that state.
So what we did here is we got S3,
we update it, we did action A1,
we got a zero S2.
So our new value for S3 was also equal to zero.
Then we went to S2, we took action A1,
we got a zero, we went to S2,
we got- so we updated S2,
it was also zero. We did that again.
We finally got to state S1 and we got a one.
So, the thing about this that can be beneficial
or not beneficial is you throw away your data in the most naive format.
You have a SAR S-prime tuple and then it goes away again. You don't keep it.
So when you finally see that reward,
you don't back up,
you don't propagate that information backwards.
So what Monte Carlo did is,
it waited until he got all the way there and then it computed the return for every state
along the episode which meant that that's why we got 1111.
But here you don't do that.
By the time you get to, um,
[NOISE] S1, you've thrown away the fact that you were ever in S3
or S2 and then you, you don't update those states.
I mean total reward is proportional to
the number of samples you need to get a good estimate of value function?
Say that again.
Ah, I'm assuming that like the longer it
takes for you to get a rewards, the more samples,
you'd need to like properly estimate,
uh, value of the function.
Question out [inaudible] is sort of, you know,
how long does it take you to get a reward and
how many samples do you need to get a good estimate of the value function?
Um, you mean for all states?
It's a little nuanced.
Um, it depends on the transition dynamics as well.
Um, you couldn't- say for a particular,
like how, how many, um,
samples you need for a particular state to get a good estimate of its reward?
Let's say your rewards are stochastic.
But in terms of how long it takes you to propagate this information back,
it depends on the dynamics.
Um, so in this case, you know,
if you had exactly the same trajectory and you did it again,
then you'd end up updating that S2 and then if you got that same trajectory again,
then you would propagate that information back again to
S2 and then one more time and then you get it back to S3.
I should S3 and there's the third one.
So, you can slowly this- propagate this information back, um,
but you don't get to kind of immediately like what Monte Carlo would do. Question.
I was wondering if you could highlight the differences between this
and the Q learning that we talked about last time?
Because they seem like kind of similar ideas.
That's great. So, exactly right.
In fact, TD learning and Q learning are really close analogs.
Q learning is, um, when you're gonna do control.
So, we're going to look at actions.
TD learning is basically Q learning where you're fixing in the policy,
Yeah. Next question back there.
Like you're actually like implement this so you would
you would keep looping right,
and updating or you just run through, uh, rewards?
It depends. So, um, it depends who asked you.
So if you're really, really compare- concerned about memory,
um, you just drop data,
so then you're on [inaudible].
If, um, in a lot of the existing sort of deep learning methods,
you maintain a sort of a,
a episodic replay buffer and then you would re-sample
samples from that and then you would do this update for the samples from there.
So you could revisit sort of past stuff and use it to update your value function.
Um, you could also- it can,
it can matter the order in which you do that.
So in this case, you could do a pass through your data
and then do it- another pass or maybe go backwards from the end.
[inaudible] it will end up propagating.
Some alpha back to S_2 there.
Yeah.
So, you just go into like convergence or-
We'll talk about that very shortly. Yes. That's a great question.
Like so what happens is you do this for
convergence and we'll talk about that in a second. Yeah.
So, just so I make sure I understand.
So, when we talk about sampling of tuple,
what's really happening is you're going to
a trajectory and you're iterating through the SAR,
the SAR tuples in that trajectory in order.
Right. But we're thinking of this really as acting as- to repeat the question.
The question is like we're going through
this trajectory we're updating in terms of tuples.
Yes, but we're really thinking about this as like your agent being in
some state taking an action getting reward again and getting to a next state.
So, there doesn't exist a full trajectory.
It just like I'm driving my car,
what's gonna happen to me in the next like two minutes?
So, I don't have the full trajectory and that I'm iterating through it.
It's like this is after every single time step inside of that trajectory, I update.
So, I don't have to wait till I have the full trajectory.
Right and, and I guess I'll just the order in which those tuples are chosen.
I- I'm guessing it matters or with the values that you're getting and estimates.
Yes. So, the question is like, you know,
the order in which you receive tuples,
that absolutely affects your value.
Um, so in, uh,
if you're getting this in terms of how you experience this in the world,
it's just the order you experience these in the world.
So, this S_t plus prime- T plus one prime becomes your ST on the next time-step.
So, these aren't being sampled from a trajectory.
It's like that's just wherever you are now.
Um, if you have access to batch data,
then you can choose which ones to pick and it absolutely affects your convergence.
The problem is you don't have to know which ones to pick in advance.
Questions. The other thing I just want to mention there is it's a little bit subtle, um,
that if you set alpha equal to, like, you know,
1 over T or things like that,
you can be guaranteed to,
um, for these things to converge.
Uh, sometimes if alpha is really small, um,
also these are going to be guaranteed to converge under minor conditions.
Um, but if you said something like alpha equals one,
it can definitely oscillate.
Alpha equals one means that essentially,
you're ignoring your previous estimate, right?
So, if you set alpha equal to one then you're just using your TD target.
All right. Okay. So, what is temporal policy difference policy evaluation
doing if we think about it in terms of this diagram and
thinking about us as taking an expectation over futures.
So, it's, um, this is the equation for it up there.
And what it does is it updates its value estimate by using a sample of S_t plus 1
to approximate that expected next state distribution or next future distribution.
And then it bootstraps because it plugs in
your previous estimate of V_pi for this plus 1.
So, that's why it's a hybrid between
dynamic programming because it bootstraps and Monte Carlo
because it doesn't do an explicit expectation over all the next states, just samples one.
Okay. So, now why don't we think about some of these things that, like,
allow us to compare between these different algorithms and
their strengths and weaknesses and it sometimes depends on the application.
Um, uh, you've had to pick which one is most popular,
probably TD learning is the most popular but it depends on the domain.
It depends on, um, whether you're constrained by data or,
um, you know, computation or memory et cetera. All right.
So, um, why don't we spend a few minutes on this briefly.
So, let us spend a minute and think about which
of these properties from what you remember so far apply to these three algorithms.
So, whether they're usable when you have no models of the current domain, um,
whether they handle continuing non-episodic domains,
they can handle non-Markovian domains.
They converge to the true value in the limit.
We're assuming everything's tabular right now,
we're not in function approximation land.
And whether or not you think they give you an unbiased estimate of the value.
So, if at any time point if you were to take your estimator if it's unbiased.
So, why don't you would just spend a minute see if you can fill in this table.
Feel free to talk to someone next to you and then we'll step through it.
[NOISE] All right which of
these are usable when you have no models of the current domain?
[NOISE] Does dynamic programming need a model of the current domain?
Yes.
Yes. Okay. What about Monte Carlo?
Usable.
Usable. What about TD?
Usable.
Usable. Yeah. Do either of those,
TD is known as what?
As a model free algorithm,
doesn't need an explicit notion.
It relies on sampling of the next state from the real world.
[NOISE] Which of these can be used for continuing non-episodic domains?
So, like, your process might not terminate, ever.
Okay. Well, can TD learning be used?
Yes.
Yes. Can Monte Carlo be used?
No.
No. Can DP be used?
Yes.
Yes. Okay. Which of these,
um, does DP require Markovian?
Yes.
It does. Which- does Monte Carlo require Markovian?
No. Does TD require Markovian?
Yeah, it does. So, um, uh,
temporal difference and dynamic programming rely on the fact that
your value of the current state does not depend on the history.
So, however you got to the current state,
it ignores that, um,
and then it uses that when it bootstraps too,
it assumes that doesn't- so,
Monte Carlo just adds up your return from
wherever you are at now till the end of the episode.
And note that depending on when you got to that particular state,
your return may be different and it might depend on the history.
So, Monte Carlo doesn't rely on the world being Markov.
Um, you can use it in partially observable environments.
TD assumes that the world is Markovian,
so does dynamic programming in the ways we've defined it so far.
So, you bootstrap you say, um,
for this current state my prediction of
the future value only depends on this current state.
So, I can say I get my immediate reward plus whatever state I transition to.
But that's sort of a sufficient statistic of
the history and I can plug-in my bootstrap estimator.
So, it relies on the Markovian assumption.
What about non-Markovian domain where do we apply it?
Um, the question is well,
what do you mean by non-Markovian?
Like, these are algorithms you could apply them.
Um, so yeah. You can apply these algorithms to anything.
The question is whether or not they're guaranteed
to converge in the limit to the right value.
And they're not, if the world is not Markovian and they don't.
Like [LAUGHTER] we've seen in some of our work on intelligent tutoring systems,
earlier on we were using some data, um,
from a fractions tutor and we're applying Markovian techniques and they don't converge.
I mean, they converge to something that's just totally
wrong and it doesn't matter how much data you have
because you're- you're using methods that rely on assumption that is incorrect.
So, you need to be able to evaluate whether they're not
Markovian or try to bound the bias or do something.
Um, otherwise your estimators of what the value is of
a policy can just be wrong even in the limit of infinite data.
Um, what about converging to the true value in the limit?
Let's assume we're in the Markovian case again.
So, for Markovian domains, does,
um, DP converge to the true value in the limit?
Yes.
What about Monte Carlo?
Yes.
Yes. What about TD?
Yes.
Yes. They certainly do.
The world is really Markovian, um, everything converges.
Asymptotically no under minor assumptions,
all of these require minor assumptions.
Um, uh, so under minor assumptions it will converge to the true value of the limit,
depends on, like, the alpha value.
Um, uh, what about being an unbiased estimate of the value,
is Monte Carlo an unbiased estimator?
Yes.
Yes. Okay. TD is not.
DP is a little bit weird.
It's a little bit not quite fair question there.
DP is always giving you the exact VK minus one value for that policy.
So, that is perfect,
that's the exact value.
If you have K1- K minus 1 more time steps to act,
that is not going to be the same as the infinite horizon value function. Yeah.
Can you explain how the last two lines are different.
Like I don't understand the difference between unbiased estimator of
value and something that converges to the true value of order.
Your question's great. So, the question is what's the difference
between something being unbiased and consistent?
Um, so when we say converges to the true value in limit,
that's also known as formally being a consistent estimator.
So, the unbiased estimate of the value means,
if you have a finite amount of data and you
compute your statistic, in this case the value,
and you compare it to the true value, then on average,
that difference will be zero and that is not true for things like TD.
But, um, and that can be- that's being evaluated for finite amounts of data.
What consistency says if you have an infinite amount of data,
will you get to the true value?
So, what that implies is that,
say for TD, that asymptotically the bias has to go to zero.
If you have infinite amounts of data,
eventually its bias will be zero.
But for small amount, you know,
for finite amounts of data and really,
you know, you don't know what that N is.
Uh, it could be a biased estimator but as the amount of
data you have that goes to infinity then it has to converge to the true value.
So, you can have things that are biased estimators that are consistent. Yeah.
For Monte Carlo, I thought you said that the implementation has an impact on
whether or not it's biased is- I thought you said if
it's every visit then it is unbiased [OVERLAPPING]
Good question. So, I, um, the question is good.
So, this is, um, it's an unbiased estimate for the, um, first visit.
And for every visit,
it's biased. Great. Question?
Um, this might be a dumb, uh,
a dumb question but are there any,
uh, you know, model free policy evaluations models that aren't actually convergent?
Yes. Question was, are there
any model free policy evaluation methods that are not convergent?
Yes, and we will see them a lot when we get into function approximation.
When you start- so right now we're in the tabular case which means we can
write down as a table or as a vector what a value is.
We move up to infinite state spaces.
Um, a lot of the methods are not even guaranteed to converge to
anything [LAUGHTER] Not even- we're not
even talking about whether they converge to the right value,
they're not even guaranteed to stop oscillating.
And they can just keep changing.
Okay. Yeah. Question.
So, is there any specific explanation why TD is not unbiased?
Is- is what?
Why TD is not unbiased?
Why it's not unbiased? Yeah. Great question.
So, the question was to say, you know,
why is TD biased.
TD is biased because you're plugging in
this estimator of the value of the next state, that is wrong.
And that's generally going to leave to- lead to some bias.
You're plugging in an estimator that is not
the true V pi for S prime. It's going to lead to a bit of bias.
So, it's really the-the bootstrapping part that's the problem.
The Monte Carlo was also sampling the expectation and it's unbiased,
at least in the first visit case.
Problem here is that, um,
you're plugging in unexpected discounted sum of rewards that is wrong.
All right. So, um,
that just summarizes those there.
I think the important properties to think- to compare between them.
Um, how would you pick between these two algorithms.
So, I think thinking about bias and variance characteristics is important.
Um, data efficiency is also important as well as computational efficiency,
and there's going to be trade offs between these.
Um, so if we think
about sort of the general bias-variance of these different forms of algorithms,
Um, Monte Carlo is unbiased,
generally high-variance, um, and it's consistent.
TD has some bias,
much lower variance than Monte Carlo.
TD zero converges to the true value with tabular representations,
and as I was saying it does not always converge once
we get into function approximation and um,
we'll see more about that shortly.
I think with the last few minutes,
we won't have a chance to get through,
um, little bit about how these methods are
related to each other when we start to think about the batch setting.
So as we saw in this particular case for the Mars Rover just again contrast them.
Um, Monte Carlo estimate waited till the end
of the episode and then updated every state that was visited in that episode.
TD only used each data point once,
and so it only ended up changing the value of the final state in this case.
So what if- happens if we want to go over our data more than once.
So if they we're willing to spend a little bit more computation,
so we can actually get better estimates and be more sample efficient.
Meaning that we want to use our data more
efficiently so that we can get a better estimate.
So often we call this batch or offline, um,
mal- policy evaluation where we've got some data and we're willing to go through it as
much as we can in order to try to get an estimate
of the policy that was used to gather that data.
So let's imagine that we have a set of k episodes,
and we can repeatedly sample an episode.
um, and then we either apply Monte Carlo or TD to the whole episode.
What happens in this case?
Um, so there's this nice example from Sutton and Barto.
Um, let's say there's just two states.
So there is states A and B,
and Gamma is equal to one, and you have eight episodes of experience.
So you either the first episode you saw A, 0, B, 0.
So this is the reward.
In B, you saw,
in the sorry- in the, and then another set of episodes you just started in B,
and you got one, and you observe that six times,
and then in the eighth episode you started in B and you got a zero.
So first of all,
can we compute what V of B is in this case?
So the, the model of the world is going to look something like this.
A to B and the B sometimes goes to one,
and B sometimes goes to zero and then we always terminate.
So in all eight episodes we saw B.
In six of those we got a one,
in two of them we got a zero.
So, if we were doing Monte Carlo,
what would be our estimate of B, value of B.
So we do a Monte Carlo estimate
using these eight episodes and we can go over them as many times as we want.
We don't just have to experience each episode once.
This is the batch data set.
Someone already collected this for us,
can do Monte Carlo updates of this data set as much as you want.
What will be the estimate of V of B in this case?
[NOISE] which is just equal to six divided by eight.
In the Monte Carlo estimate or do TD,
what will be the TD estimate of B?
Remember what TD does is they get this S-A-R-S prime and you bootstrap.
You do Alpha times R plus Gamma V of S prime,
and then do one minus Alpha of your previous estimate.
What is the [inaudible].
Um, here in this case you can make
Alpha anything small you're gonna do it in infinite number of times.
So this is the batch data settings so for TD you're just going to
run over your data like millions and millions of times.
Until convergence basically.
Somebody have any guesses of what V of B would be for TD.
It's also three quarters.
It's also three quarters.
Okay, so for, for TD it's the same because whenever you're in B you always terminate.
So it's really like just a one step problem from B,
and so for TD it'll also say V of B
is equal to six divided by eight which is equal to three quarters.
So the two methods agree in the batch setting for this.
If you can go for your data an infinite amount of time,
V of B is equal to 3- 6 8ths since so is um,
ah, under both methods.
Um, does anybody know what V of A would be under Monte Carlo? Okay, yeah.
V of A under Monte Carlo is going to be 0.
Why? Yeah good.
Because the only [NOISE] only trajectory where you have an A and I will be [inaudible] from here.
okay there's only one trajectory we have an A and it got a zero reward.
What do you think might happen with TD?
Is it going to be 0 or non-zero?
Its non-zero.
Non-zero, why?
Because you bootstrap the value from A.
Could you bootstrap right so,
so yes there's only time you're in A you happen to get zero in that trajectory,
but this is- in TD you would say, well,
you got immediate reward of zero plus Gamma times V of B,
and V of B is three quarters.
So here Gamma is equal to one.
So your estimate of this under a TD would be three quarters.
We don't converge to the same thing in this case.
So why does this um, ah,
so this is what we just went through and we can
think about it in terms of these probabilities.
Um, So what is- what's happening here?
Monte-Carlo in the batch settings converges to the minimum mean squared error estimate.
So it minimizes loss with respect to the observed returns.
Um, and in this example V of A is equal to zero.
TD zero converges to the dynamic programming policy
with a maximum likelihood estimates for the dynamics and the reward model.
So it's equivalent to
if you essentially just- just through counting you estimated P hat of S prime given S a.
So for this would say the probability of going B given A is equal to 1.
[inaudible] Because the only time you've been on A you've went to B and then
the reward for B is equal to three quarters and the reward for A is equal to 0,
and then you would do dynamic programming with that,
and you would get out, get out the value.
So, TD is converging to this sort of maximum likelihood MDP value estimation,
and Monte Carlo is just converging to the mean squared error.
It's ignoring- well it doesn't assume Markovian.
So it's not using them this Markov structure. Question.
Just to confirm on the previous slide um,if I'm going over data
many times because for TD learning on the first iteration V of A would be zero, right?
Because V of A has [inaudible] just assuming.
But after a while V of B has converged to three quarters? [OVERLAPPING].
So, In, in, in the online setting, um,
if you just saw this once, ah,
then this- then V of A would be zero for that particular update.
It just that if you did it many, many,
many times then it would converge to this other thing.
So you know which one is better?
Well if your world is not Markovian you don't
want to converge to something as if it's Markovian so Monte Carlo was better.
But if you're world really is Markov,
um, then you're getting a big benefit from TD here.
Because it can leverage the Markov structure,
and so even though you never got a reward from A,
you can leverage the fact that you got lots of data
about B and use that to get better estimates.
Um, I encourage you to think about how you would
compute these sort of models like it's called certainty equivalence.
Where what you can do is take your data,
compute your estimated dynamics and reward model,
and then do dynamic programming with that,
and that often can be much more data efficient than these other methods.
Um, next time we'll start to talk a little bit about control. Thanks.