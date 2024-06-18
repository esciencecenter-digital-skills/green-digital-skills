---
title: Green Algorithms
type: slides
order: 2
---

<!-- .slide: data-state="title" -->

# Digest of Code for Thought podcast into rough slides

===

<!-- .slide: data-state="standard" -->

## Green Algorithms
- Loïc Lannelongue started a project called Green Algorithms
- Made a calculator to estimate energy cost and carbon footprint of your algorithm
- Necessary for assessing how to make computing more environmentally sustainable
- Overall they estimate that the carbon footprint of data centres anually is around 100 MT of CO2 equivalent. That is the same as the entire US aviation in the same time.
- Not all these data centres are doing HPC
- About 500 Tonnes of CO2 estimated for training GPT3. IPC says we should aim for 2 tonnes of CO2 per person per year to keep global warming in check. 
- Not every model has such huge impacts, but we need to be mindful

Note:

===

<!-- .slide: data-state="standard" -->

## The GREENER framework
- We want a set of principles for green computing: GREENER
- Similar to the FAIR principles for data
- Governance
- Responsibility
- Estimations: Use calculators to estimate impact of the computing
- New collaboration
- Education: Need to include the notion that it has a carbon footprint during training of new researchers
- Research: Still don't know a lot about computing power usage

Note:

===

<!-- .slide: data-state="standard" -->

## Extreme differences between countries
- Countries with very low carbon intensity: 20g per kWh
- Countries with high carbon intensity (e.g. Australia): 700g per kWh
- You can make a big difference by running the exact same thing on the same hardware, but in a different country

Note:

===

<!-- .slide: data-state="standard" -->

## Data centres
- Power Usage Effectiveness (PUE)
- Quantifies overhead. Gives you e.g. how much cooling power you need per unit of compute
- Best data centres are now down to about 10% extra for cooling. Used to be around 100%.

Note:

===

<!-- .slide: data-state="standard" -->

## What should we aim for?
- It's the same as with money, we need to think of cost-benefit
- It depends what you do with it
- If people can make a case for why they need a lot of money, they should be able to make the case for their large carbon footprint
- Problem is, in research, the energy cost is effectively decoupled from the cost
- If a project is cheap financially, but has a large carbon cost, there should be an explicit justification why
- Want to be energy proportionate - there should be a reasonable assumption their benefits are going to outweigh the environmental costs
- What about the extra red tape we don't want for researchers? All applications must estimate the environmental impact of their models. They did this in France and researchers still applied. The Green Algorithms Calculator was required to be used for the applications. Researchers accepted it was a fair request and still continued applying.

Note:

===

<!-- .slide: data-state="standard" -->

## The online calculator

- The idea of the online green algorithms calculator is to make it quick and easy
- Also a Green Algorithms for HPC tool

Note:

===

<!-- .slide: data-state="standard" -->

## Does it matter what language you use?
- Paper ranked C++ and Rust at the top, things like python at the bottom
- Depends how you use it
- However, if you do ML in Python you're not actually using python. Under the surface, it's basically c++ or something like it
- Yes, the language matters, but most important is that the tools we are using are as efficient as possible, because they will be used so much (your own analysis scripts probably don't matter so much)
- Don't have enough RSEs to do all the coding and optimizations

Note:

===

<!-- .slide: data-state="standard" -->

## How can you make your code more efficient?
- Depends on the resources you use, how many cpu cores are you using etc
- Carbon footprint of memory is interesting - it doesn't matter how much you use, but how much is available. Don't request 10 times the memory you need on a server "just in case"
- Think about WHEN we run a job on a server. Energy mix different at different times.
- Can use tools to forecast the Carbon Aware Task Scheduler - tells you what is the best time to run in the next 48 hours.
- Most jobs have some flexibility - we don't care if we run it right now or in a few hours. Especially over the weekend.

Note:

===

<!-- .slide: data-state="keepintouch" -->

www.esciencecenter.nl

info@esciencecenter.nl

020 - 460 47 70
