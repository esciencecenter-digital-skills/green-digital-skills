---
title: Green Algorithms
type: slides
order: 2
---

<!-- .slide: data-state="title" -->

# Digest of Code for Thought podcast into rough slides

===

<!-- .slide: data-state="standard" -->

## Carbon intensity
- Extreme differences between countries
- Countries with very low carbon intensity: 20g per kWh
- Countries with high carbon intensity (e.g. Australia): 700g per kWh
- You can make a big difference by running the exact same thing on the same hardware, but in a different country

Note:

===

<!-- .slide: data-state="standard" -->

# Typical footprint
- Carbon footprint of data centres anually is around 100 MT of CO2 equivalent
  - That is the same as the entire US aviation in the same time.
  - Not all these data centres are doing HPC
- About 500 Tonnes of CO2 estimated for training GPT3
  - IPC says we should aim for 2 tonnes of CO2 per person per year to keep global warming in check. 
  - Not every model has such huge impacts, but we need to be mindful

Note:


===

<!-- .slide: data-state="standard" -->

## Data centre metrics
- Power Usage Effectiveness (PUE)
- Quantifies overhead. Gives you e.g. how much cooling power you need per unit of compute
- Best data centres are now down to about 10% extra for cooling. Used to be around 100%.

Note:

===

<!-- .slide: data-state="standard" -->

## What is too much energy?
- Do the potential benefits outweigh the environmental costs?
- **We should think of energy (or CO2) the same way we think of money**
  - What matters is the _cost-benefit_ ratio
  - Is €1M a lot? Not if it leads to curing a major disease
- Currently researchers are used to making the scientific case for the money they request
- They should also be able to make the case for the corresponding carbon footprint
- The energy and carbon cost can often be hidden or abstracted from the researcher's perspective

Note:

===

<!-- .slide: data-state="standard" -->

## Green Algorithms
- Loïc Lannelongue started a project called Green Algorithms: 
- Made a calculator to estimate energy cost and carbon footprint of your algorithm
- Necessary for assessing how to make computing more environmentally sustainable

Note:

===

<!-- .slide: data-state="standard" -->

## The GREENER framework
- A set of principles for green computing analogous to the FAIR principles for data
- GREENER:
  - **G**overnance
  - **R**esponsibility
  - **E**stimations: Use calculators to estimate impact of the computing
  - **N**ew collaboration
  - **E**ducation: Need to include the notion that it has a carbon footprint during training of new researchers
  - **R**esearch: Still don't know a lot about computing power usage

Note:

===

<!-- .slide: data-state="standard" -->

## The online calculator

<img src="media/green-algorithms-calculator-example.png" />

- The Green Algorithms online calculator makes it quick and easy to estimate the carbon footprint
- Can be found here: <http://calculator.green-algorithms.org/>
- There is also a Green Algorithms tool for HPC

Note:

===

<!-- .slide: data-state="standard" -->

<iframe src="http://calculator.green-algorithms.org/"></iframe>

===

<!-- .slide: data-state="standard" -->

## Yet more paperwork?

- Is this just more work for researchers when filling out grant applications?
- All applications must estimate the environmental impact of their models.
- They did this in France and researchers still applied. The Green Algorithms Calculator was required to be used for the applications. Researchers accepted it was a fair request and still continued applying.
- If a project is cheap financially, but has a large carbon cost, there should be an explicit justification why

Note:

===

<!-- .slide: data-state="standard" -->

## What language should I use?
- Typical conception of energy efficiency:
  - C++ and Rust at the top
  - Python and R at the bottom
- There is a lot of truth in this but there are a lot of important considerations
- **Many major numerical libraries in Python are not Python "under the surface"**
  - The core is usually C++ or something like that.
  - e.g. PyTorch, Tensorflow, numpy (and many others)

Note:

===

<!-- .slide: data-state="standard" -->

## What software should we optimize?
- **It is important that frequently used tools are as efficient as possible**
- Your single-use analysis scripts probably don't matter so much - just use the easiest language for the job
- Optimization is not free and costs development time (and energy) especially in lower level languages like C
- Generally there are not enough RSEs to do all the coding and optimizations, and researchers don't have time

Note:

===

<!-- .slide: data-state="standard" -->

## Minimizing energy use
- Ultimately depends on the resources you use
- Number of CPU cores is clearly a large contributor
- Carbon footprint of memory is interesting - it doesn't matter how much you use, but how much is available. Don't request 10 times the memory you need on a server "just in case"
- Think about WHEN we run a job on a server. Energy mix different at different times.
- Can use tools such as the Carbon Aware Task Scheduler - tells you what is the best time to run in the next 48 hours.
- Most jobs have some flexibility - we don't care if we run it right now or in a few hours. Especially over the weekend.

Note:

===

<!-- .slide: data-state="keepintouch" -->

www.esciencecenter.nl

info@esciencecenter.nl

020 - 460 47 70
