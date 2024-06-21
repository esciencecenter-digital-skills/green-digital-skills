---
title: Optimizing in Practice
type: slides
order: 1
---

<!-- .slide: data-state="title" -->

# Optimizing Energy Use in Practice

===

<!-- .slide: data-state="standard" -->

## Good software practice

Clean and maintainable software is essential
to sustainable/green software:
 - ease of use, reduce error during data settings
 - less bugs, avoid wasteful bugged runs

Note:

===

<!-- .slide: data-state="standard" -->

## Software life cycle

- Thinking about long term sustainability, documentation.
- Reusable software is a key component of modern
software development, reducing the time/energy consuming
task of developing every component of complex softwares.

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

## Right tool for each task

Are there slow programming languages that should be
avoided ?
 - each tool has it's purpose.
Python: great for stitching pieces together, easy prototyping
C/C++/Fortran: better at crunching number fast, but not
so good at doing string manipulation, ...

Benchmark available in the litterature can be missleading.

-> Use the right tool for each task (could simply be the 
tool you're confortable with), blending languages
when necessary.

<center>
<img src="media/fig-dummy.png" width="55%">
</center>

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

<!-- .slide: data-state="standard" -->

## Energy usage

Energy is power * time -> as first approximation,
more efficient (faster) software will be energy efficient.

A note on parallelism and scaling issue.

<center>
<img src="media/fig-dummy.png" width="55%">
</center>

Note:

===

## How to measure

introducing PMT (Python) / RJoules (R) / EAR (language agnostic).


<center>
<img src="media/fig-dummy.png" width="55%">
</center>

Note:

===

<!-- .slide: data-state="keepintouch" -->


www.esciencecenter.nl

info@esciencecenter.nl

020 - 460 47 70
