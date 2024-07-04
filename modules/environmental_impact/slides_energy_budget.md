---
title: Energy Budget
type: slides
order: 2
---

<!-- .slide: data-state="title" -->

# Energy Budget

===

<!-- .slide: data-state="standard" -->

## Why is information and communication technology (ICT) under scrutiny ?

Predicted major increase in electricity demand: from 8% to 21% in 2030.

Responsible for about 2% of global CO2 emmisions, on par with the aviation sector.

![Energy consumption ICT](media/ICT_EnergyConsumption_Jones_2018.png)

Note:

On the graph:
 - 4 components to ICT demand: network infra., consumer device (not including IoT-connected devices), data center and production from first three components (cradle-to-gate)
 - this is an expected prediction, best and worst case scenario are 12% and 50%, resp.

As researchers we use devices (laptops, workstations), local/national clusters (e.g. Snellius) and cloud services (SURF Cloud, AWS, ...).
Our day2day work embedded in ICT.

===

<!-- .slide: data-state="standard" -->

## Where is energy used in ICT ?

All ICT devices are powered by electricity.
In particular electrons themselves are used to perform the
operations encoded in your softwares.
Over the past 40 years, the number of operations processors
can crunch per seconds (FLOPs) continuously increased, albeit at a smaller rate past 2003.

![Consumer CPU performances](media/CPUFlops_overTime.png)

Note:

Figure: consumer CPU performances over 40 years (relative). (Hennessy J. and Patterson D. A., Computer Architecture (5th edition)) 

===

<!-- .slide: data-state="standard" -->

## Where is energy used in ICT (Con't) ?

This trend extends to supercomputers (e.g. Snellius) and data centers. Top500 records performances
of the world's (500) biggest computers on the same problem for over 30 years:

![TOP500 GFLOPS](media/top500_performance_evolution.svg)

Initaly growth faster than Moore's law, but slowing down past 2013. Switch to GPUs around 2019
kept the curve on track with Moore's law even though transitor/surface is increasing slower than Moore's law.

Note:

Figure: now showing GFLOPs, blue biggest supercomputer, red average of the 500.

===

<!-- .slide: data-state="standard" -->

## CPU energy consumption: how does it relates to FLOPs ?

Increase in FLOPs mostly related to:
 - improved manufacturing, more transistor/surface (Moore's law)
 - low level instructions handling improvements
 - increase in CPU clock rate (until mid-2000)

What does it means for energy ?
 - More transistors lead to more power, however smaller transistors need less voltage 
 - CPU have a baseline (idle) power consumption (P_0), due to current leakage, unless closing circuit totally
 - Active power consumption of CPUs: ~ P_0 + C * V(f_c)^2 * f_c ~ f_c^3
    f_c: clock rate
    V: voltage, higher voltage needed with higher clockrate to transfer information faster
 - Energy: power * time, time needed 1/f_c (fixed number of operations) -> energy ~ f_c^2
    
Note:

===

<!-- .slide: data-state="standard" -->

## Computer performances: FLOPs/Watt

Raw FLOPs data are not an appropriate measure of how efficient a CPU (or GPU) is.
The 10^8 increase in FLOPs does not translate to needing a nuclear power plant to run Snellius.
Green500 ranks the Top500 supercomputer based on their power consumption since 2014.
Compared to Koomey's prediction: factor 2 improvement every 1.57 years.

![Green500 efficiency](media/green500_efficiency_evolution.svg)

Note:

Figure: now showing GFLOPs/Watts, compared to Koomey's prediction (CPU then GPU after 2019).

===

<!-- .slide: data-state="standard" -->

## Data centers
- compute and/or storage
- efficiency characterized by their Power Usage Effectiveness (PUE):
    PUE = P_{total_facility} / P_{IT_facility}

- Quantifies overhead. Gives you e.g. how much cooling power you need per unit of compute
- Best data centers are now down to about 10% extra for cooling, but still large variability. Used to be around 100%.

![Data center PUE](media/PUE_DataCenter.svg)


Note:
 - P_{IT_facility} in PUE not limited to CPU/GPU, also include network, memory storage, backups, ...

===

<!-- .slide: data-state="standard" -->

## Energy Carbon intensity
- Carbon intensity has a large spatial and temporal variability.
- Extreme differences between countries
- Countries with very low carbon intensity (e.g. Norway): 20g per kWh
- Countries with high carbon intensity (e.g. Australia): 700g per kWh
- You can make a big difference by running the exact same thing on the same hardware, but in a different country

Note:

So far, we've talked about energy -> a proxy for CO2 emission, using the energy carbon intensity

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

<!-- .slide: data-state="empty-slide" data-background-iframe="https://app.electricitymaps.com/map" -->

===

<!-- .slide: data-state="standard" -->

# Dutch specific energy mix

[Nowtricity](https://www.nowtricity.com/country/netherlands)

===

<!-- .slide: data-state="standard" -->

## Overall contribution of ICT

- Computing carbon footprint can be split into two main contributions:
  - *Embodied*: from raw material extraction, to distribution
  - *Usage*: Powering, memory, infrastructure

Note:

===

<!-- .slide: data-state="standard" -->

## Typical values of energy

| Energy (J) | Examples | Equ. gCO2 |
| :-------- | -------: |--------:|
| 1.0e0 | ???? | |
| 1.0e1 | ???? | |
| 1.0e2 | ???? | |
| 1.0e3 (kJ) | ???? | |
| 1.0e4 | ???? | |
| 1.0e5 | ???? | |
| 1.0e6 (MJ) | ???? | |
| 3.6e6 (1 kWh)| ???? | 305 |
| 1.0e7 | ???? | |
| 1.0e8 | ???? | |
| 1.0e9 (0.27 MWh) | ???? | |

Note:

Do you have a feel for how much 1 Joule actually is?
Press down arrow to see the examples for different orders of magnitude.

==

## Typical values of energy

| Energy (J) | Examples | Equ. gCO2 |
| :-------- | -------: |--------:|
| 1.0e0 | Lift an apple to your mouth | |
| 1.0e1 |  | |
| 1.0e2 |  | |
| 1.0e3 (kJ) | Standby LED (0.3W) for 1 hour | |
| 1.0e4 | LED-based lightbulb (3W) for 1 hour | |
| 1.0e5 | 15 mn bike ride | |
| 1.0e6 (MJ) | ~ 2km drive | |
| 3.6e6 (1 kWh)|  | 305 |
| 1.0e7 | Human energy need per day | |
| 1.0e8 | Averaged daily cons. of NL home | |
| 1.0e9 (0.27 MWh) | Round trip flight AMS-LON for 2 | |

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

## Estimating impact
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

<!-- .slide: data-state="empty-slide" data-background-iframe="http://calculator.green-algorithms.org/" -->

===

<!-- .slide: data-state="standard" -->

## Yet more paperwork?

- Is this just more work for researchers when filling out grant applications?
- All applications must estimate the environmental impact of their models.
- They did this in France and researchers still applied. The Green Algorithms Calculator was required to be used for the applications. Researchers accepted it was a fair request and still continued applying.
- If a project is cheap financially, but has a large carbon cost, there should be an explicit justification why

Note:

===

<!-- .slide: data-state="keepintouch" -->

www.esciencecenter.nl

info@esciencecenter.nl

020 - 460 47 70
