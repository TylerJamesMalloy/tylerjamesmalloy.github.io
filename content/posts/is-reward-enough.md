---
title: "Is Reward Enough"
date: 2022-01-17
draft: false
toc: false
tags:
  - review
---

In this post I provide a review and opinion on the paper ["Reward Is Enough"](https://www.sciencedirect.com/science/article/pii/S0004370221000862) by D Silver, S Singh, D Precup, and RS Sutton. In this work, the authors provide a broad perspective on reinforcement learning research and put forward the opinion that much of the behavior that interests cognitive science and artificial intelligence researchers can be viewed in relation to reward. Specifically, they propose that many cognitive faculties such as perception, language, generalization, imitation, and even general intelligence can be achieved through reward maximization and experience in an environment. They describe a hypothesis alongside these claims that is essentially stated in the short title, that reward is enough to learn these types of complex behaviors. The following figure borrowed from the paper describes several phenomenon which could hypothetically be trained through reward based reinforcement style learning. 

<figure>

<img src="https://ars.els-cdn.com/content/image/1-s2.0-S0004370221000862-gr001.jpg" alt="Trulli" style="width:100%"><figcaption align = "center"><b>Fig.1 - Reward Is Enough
David Silver, Satinder Singh, Doina Precup, Richard S.Sutton (paper on ScienceDirect). This figure demonstrates the overlap in behaviour that can conceviably be taught through reward signals in a cognitive vs. artificial agent.</b></figcaption>

</figure>

For a cognitive psychologist or cognitive philosopher the first impression of this claim and the themes of the paper may be somewhat negative. Haven’t Chomsky and others taught us that experience in language use alone cannot give us the tools we need to be good language users? There should be a requirement that a universal grammar exist to reduce the hypothesis space of possible grammars before we even begin understanding the utterances of others, let alone generating our own. In point of fact there is a significant dearth of ‘negative’ examples of proper language, as most of our experience is with well formed language. Furthermore, much of our experience with language happens internally, without a clearly defined external reward signal. 

Although these potential issues can be raised when taking the reward-is-enough hypothesis as a general claim or descriptive thesis on human cognition, in reality the goals of the paper are in showing that reward is sufficient for complex behavior learning. Because of this, the main purpose of the paper could be supported even without any evidence of reward based learning in a human agent. Instead the paper seeks to provide evidence that artificial reinforcement learning agents could hypothetically learn the complex behavior that humans achieve through reward signals alone.

While it is true that the paper claims to be more interested in describing the ‘sufficient’ aspect of learning behavior through reward, it does at the same time make some claims and connections to cognitive science that are more controversial. One source of potential controversy is the section entitled “What else, other than reward maximisation, could be enough for intelligence?” In this section the authors provide brief outlines of alternative hypotheses and suggest that they are not as well fit for training goals of general AI and other interesting behaviors. The presence of this section raises the question of the true intentions of the paper as a whole. If as the authors claim the hypothesis is centered around how behavior could be taught and not a description of human cognition, then why iterate through a list of alternatives and claim they cannot do what reward alone can? 

In particular, the brief sentences on the free-energy hypothesis arguably leave out some important claims by cognitive psychologists such as Karl Friston in his paper “The free-energy principle: a unified brain theory?” The full quote from ‘Reward Is Enough’ is as follows: “Maximisation of free energy or minimisation of surprise may yield several abilities of natural intelligence, but does not provide a general-purpose intelligence that can be directed towards a broad diversity of different goals in different environments. Consequently it may also miss abilities that are demanded by the optimal achievement of any one of those goals (for example, aspects of social intelligence required to mate with a partner, or tactical intelligence required to checkmate an opponent).” 

It seems from Friston’s perspective that free energy alone could provide much of what reward does for the authors of this paper. At least this should have more of a discussion if the authors are interested in showing why reward is unique in its ability. If they are not then it may be better to eschew a discussion of alternatives or claims that reward is specifically unique in its position. Otherwise, it is hard to not make larger connections of the claims made in the paper to a description of human cognition. 

To me the general theme of the paper actually reminded me much of Karl Friston’s paper previously mentioned. There are many complex behaviors that could be defined as achieving something like free-energy minimization or reward maximization. Generally this is a good place to start for machine learning or artificial intelligence research because if you can begin to define what desirable behaviour looks like in terms that resemble something like a trainable loss function, then you are well on your way to making a useful system. This may be interesting from an AI researcher or engineering perspective, but for a cognitive psychologist the claims could be seen as somewhat vacuous and less useful for understanding cognition. 

If you are interested in my perspective, I think that at least for much of human learning and decision making there is a combination of reward driven reinforcement style learning and predictive processing used for planning and beliefs about future states. However, I will add that I make no claims of how language and general intelligence specifically can and should be taught, as those are outside of the realm of my particular experience. I would imagine that much of those more complex behaviors is more driven by the structure of cognitive architectures as they have been optimized through millions of years of evolution. 



