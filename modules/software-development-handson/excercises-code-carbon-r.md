---
title: "Code Carbon in R"
type: exercise
order: 6
---

# CodeCarbon in R

## Introduction
---------------

If you are mainly coding in R, you may want to learn more about the impact of your R code in terms of energy consumption and carbon footprint. However, there aren't yet as of now R packages that allow to do this in a reliable and user-friendly way. One promising tool is the [**RJoules package**](https://rishalab.github.io/RJoules/); however, it is still in development and restricted to certain operating systems used by developers (i.e., linux).

**CodeCarbon** is a Python package that estimates the carbon footprint of code. You can [read more about it here](https://mlco2.github.io/codecarbon/). This Python module is well documented and easy to use. How sad that it is only available for Python... But there is a way to use it in R! In fact, it is possible and relatively easy to run Python in RStudio. This can be done through the [`reticulate`](https://rstudio.github.io/reticulate/) package, which allows you to run Python code from R directly into your R script. For more complex workflows, [**Quarto**](https://quarto.org/docs/computations/python.html) can be used to combine R and Python code in the same document. In fact, Quarto markdown files (.qmd) are exceptionally good at calling R and Python code in the same document, whilst also making it explicit what code belongs to each, using the native syntax for both languages in the same document and analysis workflow.

This tutorial shows how to implement CodeCarbon in R through RStudio. An example workflow is provided by measuring the carbon footprint of two different R packages used to fit mixed-effects models. Additionally, time-varying confounding is introduced into the built-in R `ChickWeight` data through simulation to compare how different statistical modelling strategies to account for confounding compare in terms of their energy consumption and carbon footprint.

## Installation
---------------

The detailed instructions for installation of Python and CodeCarbon are found in the [prior lesson](https://esciencecenter-digital-skills.github.io/green-digital-skills/modules/software-development-handson/exercises_codecarbon). It is assumed that you have already followed these steps.

If you have not done so, [install R and RStudio](https://posit.co/download/rstudio-desktop/). Note that these demonstrations were conducted under R version 4.4.0 and RStudio 2024.04.0, so it is recommended that you install these or more recent versions.

Lastly, all the necessary materials and R scripts for this tutorial can be downloaded from Zenodo (doi: [10.5281/zenodo.14617645](https://doi.org/10.5281/zenodo.14617645)). You can also download the ZIP file by [following this link](https://zenodo.org/records/14617645/files/UtrechtUniversity/code-carbon-r-v1.0.0.zip?download=1), unpack it, and place it in a familiar folder in your computer. 

## Calling CodeCarbon in an R script
-------------------------------------

You will found a sample R script named **code-carbon-script.R** inside the *R folder* if you successfully downloaded the material with the prior steps. This script can be adapted to test your own R code. It incorporates the following steps:

First, you will need to install the `reticulate` package and load it into your session:

```         
install.packages("reticulate")
library(reticulate)
```

Load the CodeCarbon module using the reticulate [`import`](https://rstudio.github.io/reticulate/reference/import.html) function.

```         
codecarbon <- import("codecarbon")
```

Import the OfflineEmissionsTracker class

```         
OfflineEmissionsTracker <- codecarbon$OfflineEmissionsTracker
```

Set the emissions trackers parameter and initialize. This will automatically detect your system's characteristics and open a file to save the report later on. You can also specify the country code, timing of measurements, among others. See the [CodeCarbon documentation](https://mlco2.github.io/codecarbon/parameters.html#id6) for more details:

```         
tracker <- OfflineEmissionsTracker(
  country_iso_code = "NLD",
  measure_power_secs = 5
)
```

Start tracking the emissions, run your code, and finish tracking once your code ran.

```         
tracker$start()

# Your R code here

tracker$stop()
```

This will terminate the report and save it in your default working directory, unless you specified earlier the path to save it according to the provided documentation.

Note that CodeCarbon will continue to track until you explicitly stop it with `tracker$stop()`. Thus, you may want to run all lines of code from start -\> code -\> stop in one go to measure the consumption of that specific code.

## Calling CodeCarbon in a Quarto markdown (qmd) file in RStudio
----------------------------------------------------------------

If you use Quarto, you can call Python and R code in the same document, using their native syntax. For this, you can specify the language of the code block using the `python` or `r` tags:


```
{python}
# Your python code here
``` 

```
{r}
# Your R code here
```

The advantage of using Quarto is that you don't need to rewrite python code using the `reticulate` syntax. You can simply copy and paste the Python code into the `python` code block. This is a great advantage when you are not very familiar with Python and you want to reuse well-documented native python code, or simply to efficiently communicate with Python programmers.

Because Rstudio loads the reticulate package once it reads the `python` tag, you don't need to load the `reticulate` package in the code block. Thus, we will start by calling the CodeCarbon module in Python.

### Setup 

In the downloaded folder, you will find an R project icon named **code-carbon-R.Rproj**. Open this project in RStudio. This will set a default working directory, which is useful to read the associated scripts and save the emissions reports. Now, navigate to the **R** folder, where you will find a document called **code-carbon-Quarto.qmd**. You may open this file in RStudio to reproduce the following steps in the corresponding section. 

> *Tip: The rest of this tutorial can be followed through the code-carbon-Quarto.qmd file in RStudio.*

### Instructions  

Start by pressing the play button below that reads "Run Current Chunk":

```
{python}
# Load the CodeCarbon module
from codecarbon import OfflineEmissionsTracker
```

Then, we will initialize the tracker and start tracking the emissions. Beware that you will need to stop tracking the emissions before with the code that will appear later on in this document to start a new tracker. For this, we can use a safety check to avoid running multiple trackers at the same time.

```
{python}
tracker = OfflineEmissionsTracker(country_iso_code="NLD",
                                 measure_power_secs=5)

if getattr(tracker, "_start_time", None) is not None:
    print("Warning: Tracker is already running! Did you forget to stop it?")
else:
    tracker.start()
    print("Tracker started successfully.")
```

You can now change to R language by using the `r` tag. In this code block, you can introduce your R code. For example, a fictitious computationally intensive function for which you would like to test its energy consumption.

``` 
{r}
intense_computation(large_dataset)
```

Finally, you can stop tracking the emissions and print the results. You will again find the report as a csv file in your default working directory.


```
{python}
emissions: float = tracker.stop()
print(f"Emissions tracked: {emissions} kg CO₂e")
```

This value represents the estimated carbon emissions equivalent in kilograms.

Combining R and Python code in a .qmd file will work best if you are rendering your document to any of the output report files implemented in Quarto (i.e., PDF, html, docx, slides, etc). This is because code blocks are executed in the order they are found in the document. However, if you mainly work with R scripts, running CodeCarbon with the `reticulate` package in R will be the best approach.

For the last part of this tutorial, a hybrid approach is used where:
1.  Individual R scripts are adapted from the sample **code-carbon-script.R** to include CodeCarbon tracking for every individual task.  
2.  The individual R scripts are then sourced into the Quarto document to demonstrate the energy consumption and carbon footprint of different R packages used to fit mixed-effects models.  
3.  This model workflow produces an individual output report for every R script and task, which will be found in the `emissions` folder. 

This approach offers the advantage of more precise measurements because every script starts with the initialization of the tracker and ends with the stop command in one go.

## Demonstration
----------------

We will compare two R packages commonly used to fit mixed-effects models that are often compared due to their computational speed. `lme4` is suitable for generalized linear mixed models, runs in C++, and is optimized for speed,<sup>1</sup> whereas `nlme` can additionally fit non-linear models, but is written in R language (before: S and S-Plus)<sup>2</sup> which makes computations somewhat slower and with a potentially higher carbon footprint.

However, there are often preliminary modelling steps needed when trying to elucidate the main effects with these two packages. One example is time varying confounding, for which different modelling approaches have been proposed. Inverse probability weighting (IPW) is a powerful tool for such analyses, but many different models can be used to obtain inverse probability weights to be used in the main mixed-effects models. Generalized linear models can be used as a fast an computationally efficient option to obtain IPW through the built-in `stats` R package, which is written in R and C language, but is highly susceptible to incorrect model specification. Novel non-parametric methods are robust to model misspecification,<sup>3</sup> and are implemented in the `CBPS` package, which despite running in C++ for computational efficiency, uses intensive and lengthy calculations. These two methods will be compared using Python `CodeCarbon`. We will use the `WeightIt` package written in R language,<sup>4</sup> which has implemented these two methods and many others which can similarly be tested and compared in terms of energy consumption and carbon footprint.

We will use the built-in R `ChickWeight` dataset to simulate new data with time-varying treatment-outcome confounding to study the effect of 4 different diets on weight, by accounting for the confounding effect of a time-varying binary disease 1, and an ordinal disease 2, which disease status may also vary in time.

First, install and load all the necessary R packages to avoid these one-time installations being tracked by CodeCarbon. The `pacman` package nicely handles installation and loading.

``` {.r .cell-code}
if (!require("pacman", quietly = TRUE)) {
  install.packages("pacman")
}

pacman::p_load(
  tidyverse,        # Used for basic data handling and visualization.
  conflicted,       # Used to handle conflicts between packages.
  reticulate,       # Used to call Python code in R.
  lme4,             # Used to fit linear mixed-effects models.
  nlme,             # Used to fit non-linear mixed-effects models.
  WeightIt,         # Used to obtain inverse probability weights (IPW).
  CBPS              # Used to obtain non-parametric CBPS IPW.
)

conflicts_prefer(dplyr::select, dplyr::lag, dplyr::filter)
```


We now simulate the data and measure the time required to complete and it's carbon footprint. The input and output parameters have been adapted in the R script to save the output file in the `emissions` folder. By running this chunk of code, you will also see the live emissions tracking as R console output.

> Important! If the code is interrupted before finishing, emissions will keep to be tracked and shown until you stop it by running the last line in the scripts. This is important to keep in mind when running new code chunks and start a new tracker. Run tracker\$stop() whenever your code is prematurely interrupted before reaching the end of the script.

Tip: If any of the scripts take too long to run, you can try modifying the `sample_size` parameter in the **data_simulation.R** script. This will also be changed below in this code file to explore emissions with different sample sizes.

``` {.r .cell-code}
source("data-simulation.R")
```

Let's now measure the energy consumption of obtaining inverse probability weights with a generalized linear model (glm) in the built-in `stats` R package.


``` {.r .cell-code}
source("ipw_glm.R")
```


And compare against the novel non-parametric method implemented in the `CBPS` package. This will take longer to run than the prior steps, so we will track emissions every 5 seconds.

``` {.r .cell-code}
source("ipw_CBPS.R")
```

> Question: Would you prefer the faster glm method or the more robust CBPS method to obtain IPW? 

Finally, we will fit the mixed-effects models with the `lme4` and `nlme` packages, and compare their energy consumption.

``` {.r .cell-code}
source("mixed_model_lme4.R")
```

``` {.r .cell-code}
source("mixed_model_nlme.R")
```

### Simulation with a larger dataset


The original tests used 550 observations in a total of 50 chicks. This was sufficient to demonstrate the differences in emissions with the two IPW methods, but not with the different mixed-effects packages. We will next simulate a much larger dataset with 5000 chicks to be able to compare `lme4` and `nlme`.


``` {.r .cell-code}
# Simulate new data and prepare the dataset for analysis 

simulated_data <- simulate_chickweight(n_chicks = 5000)

analysis_data <- simulated_data %>%
  arrange(Chick, Time) %>%
  group_by(Chick) %>%
  mutate(
    lag_disease_1 = lag(disease_1),
    lag_disease_2 = lag(disease_2),
    lag_weight = lag(weight)
  ) %>%
  ungroup()

analysis_data <- analysis_data %>%
  filter(!is.na(lag_disease_1))
```


We will use the IPW obtained with glm for faster computations.


``` {.r .cell-code}
source("ipw_glm.R")
```

And now we can compare the energy consumption of fitting the exact same model with the `lme4` and `nlme`.


``` {.r .cell-code}
source("mixed_model_lme4.R")
```

``` {.r .cell-code}
source("mixed_model_nlme.R")
```

> Question: How do the energy consumption and carbon footprint of the two packages compare with the larger dataset when fitting the same model? 

## Conclusions
---------------

This tutorial provides different alternatives to implement CodeCarbon in R workflows. The provided code can be adapted and used by R code developers and other R users to test the efficiency and carbon footprint of their code. Existing R packages able to perform the same tasks can be compared in terms of energy consumption, which can be an additional criterion to choose between them. However, it should be kept in mind that energy consumption an carbon footprint are among the many factors to consider when choosing between different packages. For instance, it could be justifiable to use a method that consumes more energy and has a higher carbon footprint if it offers other significant advantages. 


## References 
---------------

1.  Bates, Douglas, Martin Mächler, Ben Bolker, and Steve Walker. 2015. “Fitting Linear Mixed-Effects Models Using Lme4.” Journal of Statistical Software 67 (1). https://doi.org/10.18637/jss.v067.i01.

2.  Fong, Christian, Chad Hazlett, and Kosuke Imai. 2018. “Covariate Balancing Propensity Score for a Continuous Treatment: Application to the Efficacy of Political Advertisements.” The Annals of Applied Statistics 12 (1). https://doi.org/10.1214/17-aoas1101.

3.  Greifer, Noah. 2017. “WeightIt: Weighting for Covariate Balance in Observational Studies.” The R Foundation. https://doi.org/10.32614/cran.package.weightit.

4.  Pinheiro, José C., and Douglas M. Bates. 2000. Mixed-Effects Models in s and s-PLUS. New York: Springer. https://doi.org/10.1007/b98882.