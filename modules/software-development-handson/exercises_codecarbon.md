---
title: "Code Carbon"
type: exercise
order: 5
---

# CodeCarbon

## Introduction
---------------

An important step in trying to improve the energy efficiency of your
software is to measure the actual energy consumed during the execution
of your code.

There are a handful of open-source software packages available online
to measure the energy consumption of a piece of code, including 
[PowerAPI](https://github.com/powerapi-ng/powerapi),
[EnergyMon](https://github.com/energymon/energymon) or
[PMT](https://git.astron.nl/RD/pmt). In this hands-on exercice, we 
will focus on [CodeCarbon](https://codecarbon.io/), a Python package
readily available on Linux, Windows and MacOS.

We will start by testing CodeCarbon on a simple example
code provided below, then provide guidance on how to test a snippet
of your own code. For the later, we advise selecting a well-contained, single-purpose
function at first and progressively extend to larger and more complex
workflows. The runtime of your selected function/program should be
of the order of ~10s since CodeCarbon is not designed for high frequency
measurments.

### Prerequisite

 - a working knowledge of Python. See [Python Carpentries](https://swcarpentry.github.io/python-novice-inflammation/index.html) for a quick introduction.

## Installing CodeCarbon
------------------------

Code Carbon is written in Python and brings a number of dependencies.
It is recommended to setup a dedicated environment using a package
and environment management tool such as [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to avoid disrupting the packages currently available
on your computer. However, this step is not mandatory.

### On MacOS and Linux:

#### Using Conda:

Create a new Conda environment:
```
conda create -n greencomputing python=3.12 
```

Activate the new environment:
```
conda activate greencomputing
```

Use the package manager 'pip' to get CodeCarbon (and its dependencies):
```
pip install codecarbon
```

#### Without environment manager:

In this case, we assume that Python is already available on your computer.
```
python -m pip install codecarbon
```

To check that CodeCarbon is effectively installed, try the following command:
```
python -c "from codecarbon import OfflineEmissionsTracker; print('SUCCESS')"
```
If CodeCarbon was successfully installed, the command will simply return 'SUCCESS'.


### On Windows

The above installation instructions should work on Windows if using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

If not, it is generally easiest to install python packages using conda which can be installed according to [these instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html).

If you have another setup or requirements then please ask - we will do our best to help you get set up!


## Using CodeCarbon: a first example
------------------------------------

The test case consists in computing the Euclidian distance
between all the points contained in a list, where each point is defined by
two coordinates. To illustrate how changes to the code can impact the energy consumption,
two implementations of the computation are provided: a naive version
relying on Python's list and a version using Numpy. The code can
be obtained [here](media/EuclidianDistance.py).

Let's now write a small Python driver to execute the computation
and measure the energy consumption.

We will start by importing the Python modules needed. In a new
python file (e.g. EDCodeCarbonTest.py), write the following:
```python [EDCodeCarbonTest.py]{4-6,7} meta-info=val
import random
import numpy as np
from EuclidianDistance import get_distances
from codecarbon import OfflineEmissionsTracker 
```

The first two modules are needed in order to generate data. From the
code provided above, we will use the ```get_distances``` function, and
finally we will use CodeCarbon's ```OfflineEmissionsTracker```.
Note that CodeCarbon can also be used ```Online```, allowing live access to
carbon intensity data and a dashboard, but the setup is more complicated.

Once the modules are loaded, we can write the main function of our program,
appending to the file created above:
```
if __name__ == "__main__":
    # Prepare a list of coordinates
    # Define the list length
    n_npts = 20000

    # Get Numpy's random number generator with a fixed seed
    rng = np.random.default_rng(12345)

    # Populate the list, with coordinates uniformly sampled
    # in the [0,1] interval.
    points = []
    for _ in range(n_npts):
        points.append((rng.uniform(0.0, 1.0), rng.uniform(0.0, 1.0)))
```

We now have a list of points to pass to the ```get_distances``` function.
But we first need to initialize CodeCarbon emission tracker. In this example,
we will use a context manager such as:
```
    with OfflineEmissionsTracker(country_iso_code="NLD",
                                 measure_power_secs=5) as tracker:
        >> compute intensive code ...
```
where the ```tracker``` will directly start and report energy consumption as
we execute the code. There are numerous runtime options available when
initializing the ```OfflineEmissionsTracker```, refers to CodeCarbon
[documentation](https://mlco2.github.io/codecarbon/parameters.html) for a complete
overview. In the example above we only provided the Netherlands ISO 3 letters code,
and the interval (in seconds) to measure hardware power usage.
Let's now add our actual computation in the code as follows:
```
    with OfflineEmissionsTracker(country_iso_code="NLD",
                                 measure_power_secs=5) as tracker:
        get_distances(points, "base")
```
where we use the base implementation of the Euclidean distance calculation. It is now
time to run the program.

> `Note`{style="color: darkred;"}: On MacOS, CodeCarbon relies on PowerMetrics to access hardware power data, thus requiring root/sudo access. You will be prompted for your login password


The actual output of running the Python program will depend on your platform and hardware,
but it will resemble the following (here on MacOS):
```
[...] [setup] RAM Tracking...
[...] [setup] GPU Tracking...
[...] No GPU found.
[...] [setup] CPU Tracking...
[...] Tracking Apple CPU and GPU via PowerMetrics
[...] >>> Tracker's metadata:
[...]   Platform system: macOS-14.6.1-arm64-arm-64bit
[...]   Python version: 3.12.7
[...]   CodeCarbon version: 2.7.1
[...]   Available RAM : 24.000 GB
[...]   CPU count: 8
[...]   CPU model: Apple M2
[...]   GPU count: 1
[...]   GPU model: Apple M2
[...] Saving emissions data to file ./NLeSC/Training/CodeCarbon/emissions.csv
[...] Energy consumed for RAM : 0.000013 kWh. RAM Power : 9.000000000000002 W
[...] Energy consumed for all CPUs : 0.000010 kWh. Total CPU Power : 7.500399999999999 W
[...] Energy consumed for all GPUs : 0.000000 kWh. Total GPU Power : 0.001 W
[...] Energy consumed for RAM : 0.000038 kWh. RAM Power : 9.000000000000002 W
[...] 0.000048 kWh of electricity used since the beginning.
[...] Energy consumed for all CPUs : 0.000033 kWh. Total CPU Power : 8.2367 W
[...] Energy consumed for all GPUs : 0.000000 kWh. Total GPU Power : 0.002 W
[...] Energy consumed for RAM : 0.000048 kWh. RAM Power : 9.000000000000002 W
[...] ...
[...] 0.000321 kWh of electricity used since the beginning.
[...] 0.000890 g.CO2eq/s mean an estimation of 28.064960638276645 kg.CO2eq/year
```

> `Note`{style="color: darkred;"}: If the CPU on your system is not recognized by CodeCarbon, a default CPU will be used but the code will issue Warnings.

At time interval specified when initializing the ```OfflineEmissionsTracker```, power and energy
are reported for the various hardware. Based on the country code provided, an estimate of
the CO2eq emission rate is also reported at the end. As you can see, a constant 9W power is used for the RAM here, whereas
small fluctuations are observed on the CPU side. Even though the RAM and CPU are shared with other programs running
on your computer, CodeCarbon assign their full usage to the measured code. A more accurate measurement of the specific
process CPU usage can be obtained by providing an extra argument to the tracker initialization, ```tracking_mode = "process"```.
However, this method does not provide a good measurement of the memory power.

Let's now switch to the Numpy version of program by updating the call to the ```get_distances``` function:
```
        get_distances(points, "numpy")
```
And re-run the program. The measured energy consumption for thid case is 0.000194 kWh, for an estimated
emission rate of 0.000538 g.CO2eq/s.
This small example demonstrate how by relying on a more efficient implementation, the energy consumption and associated
emissions can be reduced, mostly due to a shorter runtime. Feel free to experiment with the following:
 - changing problem size
 - update the parameters of the ```OfflineEmissionsTracker```, changing the country code for instance
 - try an alternative implementation of the distance computation
 - add timers to the script to estimate if the average power, is it changing between the two provided implementation ?

## Calling CodeCarbon in an R script
------------------------------------

The following workflow is available in this [R script](https://github.com/javimangal/green-digital-skills-r/blob/main/R/code-carbon-script.R), which you can reuse and adapt to test your code.

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

Set the emission trackers parameter and initialize. This will automatically detect your system's characteristics and open a file to save the report later on. You can also specify the country code, timing of measurements, among others. See the [CodeCarbon documentation](https://mlco2.github.io/codecarbon/parameters.html#id6) for more details: 

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

Note that CodeCarbon will continue to track until you explicitly stop it with `tracker$stop()`. Thus, you may want to run all lines of code from start -> code -> stop in one go to measure the consumption of that specific code. 

## Calling CodeCarbon in an Quarto markdown (qmd) file in RStudio
-----------------------------------------------------------------

If you use Quarto, you can call Python and R code in the same document, using their native syntax. For this, you can specify the language of the code block using the `python` or `r` tags: 

```
{python}

```

```
{r}

```

RStudio automatically process the programming language. R is the default language in Quarto when introducing code blocks. If you want to run Python code, you need to change `r` for the the `python` tag. 

The advantage of using quarto is that you don't need to rewrite python code into the `reticulate` syntax. You can simply copy and paste the python code into the `python` code block. This is a great advantage when you are not familiar with Python, when you want to reuse well-documented native python code, or simply to efficiently communicate with python programmers.

Because Rstudio loads the reticulate package once it reads the `python` tag, you don't need to load the `reticulate` package in the code block. Thus, we will start by calling the CodeCarbon module in Python. 

```
{python}
# Load the CodeCarbon module
from codecarbon import EmissionsTracker
```

Then, we will initialize the tracker and start tracking the emissions. 

```
{python}
# Initialize the tracker
tracker = OfflineEmissionsTracker(country_iso_code="NLD",
                                 measure_power_secs=5)

# Start tracking the emissions
tracker.start()
```

You can now change to R language by using the `r` tag.

```
{r}
# Introduce your R code here. For example, a fictitious computationally 
# intensive function for which you would like to test it's energy consumption. 
intense_computation(large_dataset)
```

Finally, you can stop tracking the emissions and print the results. You will again find the report as a csv file in your default working directory. 

```
{python}
emissions: float = tracker.stop()
print(emissions)
```

## Using CodeCarbon: your own code
----------------------------------
If your target code is based on Python, the simplest way to adapt the small example provided above to
your case is wrap your entire program into a single function call and replace the ```get_distances``` function
by your own.

An alternate solution, applicable to softwares written in other programming language such as R or C++, is to
rely on Python subprocess. In the following, let's assume that you have an executable R file (i.e.
with ```#! /usr/bin/Rscript``` on the first line).

Create a new python file (e.g. CodeCarbonWrap.py), with the following imports:
```
import subprocess
from codecarbon import OfflineEmissionsTracker
```
and the following main function:

```
if __name__ == "__main__":
    with OfflineEmissionsTracker(country_iso_code="NLD",
                                 measure_power_secs=5) as tracker:                                                                                 
        subprocess.call (["/usr/bin/Rscript", "--vanilla", "/pathto/MyrScript.r"])
```
Note that because the script R script is executed in an external process, the option ```tracking_mode = "process"```
is no longer adapted and only the mode where the CPU usage of the entire computer is measured is relevant. You
should thus be aware of the other programs running on your computer (e.g. a web brower with video streaming) as their
CPU usage will be measured as well, and for more accurate measurements those programs should be terminated.

## Conclusion
-------------

In this short tutorial, you have tested first-hand how to measure the energy consumption of a piece of code
using [CodeCarbon](https://codecarbon.io/). CodeCarbon can be deployed on larger application as well as
on HPC platforms.
Although written in Python, CodeCarbon can be used for any other languages as long as you are able to use
Python subprocess to execute the external program (i.e. R, C++, Fortran, ...).
