---
title: "Wordl Rl"
date: 2022-02-03
draft: false
toc: false
images:
tags:
  - discussion
---


This post will discuss briefly the possiblity of constucting a reinforcement learning algorithm to play the game Wordle. Language based applications of reinforcement learning are somewhat common, though perhaps not the first thing RL researchers think of as examples of applications in RL. However, Wordle is a single player game with a discrete number of actions and states, the proverbial bread and butter of RL algorithms such as one of the first successful game players TD-gammon, which palyed backgammon. 


So it seems like RL may be a good idea for a AI mehtod, but how to acheve that isn't totally clear. I won't be discussing a clear implementation or writing any code in this post, just discussing the possibility. Before describing the game it should be noted that wordle is definitely possible to learn using RL, but what isn't clear is whether it is a good idea to do it or if there is a much better approach without RL. 

Wordle is a simple word guessing game with the following instructions:  

Guess the WORDLE in 6 tries.

Each guess must be a valid 5 letter word. Hit the enter button to submit.

After each guess, the color of the tiles will change to show how close your guess was to the word.

There are some interesting additional rules that are not included in this list of instructions. Firstly, the exact colors that the tiles change to and their meaning. A green highlighted color means that the letter you guessed is correct and in the correct location. Yellow means that the letter is correct but in the wrong location. And grey means that the letter does not appear in the target word. This is important from a reinforcement learning perspective as the state used to determine the optimal action should ideally contain this information. 

These color codes are important for the game from a reinforcement learning perspective, but there are additional rules that limit what can be entered by the player. Firstly, words entered need to be in the valid list of words, more on that later as it is important when thinking about training a RL agent. Secondly, letters that have previously been shown to not be a member of the list (grayed out) are possible to be entered in. This is interesting as it allows for technically suboptimal behaviour, but this makes sense given the game is designed for humans who may be trying to enter one of the only words they can think of to see if any of the letters in it match and gain more inforamtion. We are only just describing how the game works in a basic sense and we are already talking about the difference between a human and AI player! Clearly this was destined as I am the one writing it, but I thought that was interesting nonetheless.  

So if we were to design an agent we would definitelty want to be able to train it not just on the relatively short list of previous wordle answers, especially since those are unlikely to be repeated. There doesn't seem to be an official list of 5 letter words that are used in wordle, but there is a list of a high number of 5 letter english words, which may be the best bet as dictionaries change from year to year. [An incomplete list can be found here.](https://eslforums.com/5-letter-words/) So with that the RL agent seems relativly straightforward right? We have our observation space and a way to get new episodes for training from that long list. But wait, what exatly is our action space? 

If you know a bit about RL you may have an idea, but it may not be the one someone else is thinking of as there are, at least to me, two clear possibilities. Firstly the action space could be one of the roughly three thousand words in that long list I mentioned earlier. That may seem like a lot but there are domains I have worked with that had about that many actions, and other domains have far more or continuous actions which are a whole different issue. An alternative to this would be treating an action as entering a single letter. That may seem like a huge improvement in the complexity of the task, 3K to only 26! However remember that the entire word needs to be entered. So really to enter one word there are 26^5=11881376 different action combintaitons. This isn't as big an issue as it seems becasuse the state will be changing as the actions are made, the agent isn't required to pick the combination before they start typing. However from this we can see that the choice of action representation is not directly clear. 

Since I am interested in human learning and machine learning, specifically in human inspired machine learning, it is interesting to think about how a human inspired RL method would tackle this problem. It may seem like humans definitely pick a word first and then type it out, giving credence to the worde based action space method. However, someone who has read strategies on wordle may recognize the strategy of copying down the green letters and putting X's in all the other spaces to allow you to visualize what the correct letter is. This method may suggest that people start typing out the letters they know, either at the beginning or end of the word, and then try to think of what the word might be. 

There are many other topics that are interesting to think about from a human learning perpective, like trying to do imitation learning on examples from human players. There are also additionaly little quirks of the game like knowing how many of a letter there are based on the number of yellow highlighted letters in a word that had two of those letters in it. As a whole, I think this may be an example where RL might not be the best approach, as it is possible to simply have a list of all 5 letter words and remove the ones that don't fit the known information. This alone won't make a optimal player as they should additionally pick options that are maximally informative, but that could be acomplished with a bayesian approach or a planning based approach. Either way, I am confident an RL agent could play this game, but it might just not be the most interesting or useful application. 