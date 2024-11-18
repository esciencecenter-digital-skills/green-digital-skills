---
title: Exercises
type: exercise
order: 6
---

# Exercises
Choose an application from the list [below](#applications)
### 1. Monitor an application with EAR
### 2. Identify whether the applicaiton is CPU intensive or Memory/Communication intensive
### 3. Play with PyTorch Automatic Mixed Precision, and maybe model "size". What impacts on Energy does this have?


### lol


## Applications

All of the Applications used in this tutorial can be found in the project space `/projects/0/energy-course/`

1. [Synthetic Applications](#synthetic-applications)
2. [Scientific Applications](#scientific-applications)
   - [HemePure](#hemepure)
   - [Palabos](#palabos)
   - [GROMACS](#gromacs)
   - [PyTorch](#pytorch)


## Synthetic Applications
### NAS Parallel Benchmarks (NPB3.4-MZ MPI+OpenMP) - SP-MZ Benchmark
> The NAS Parallel Benchmarks (NPB) are a small set of programs designed to help evaluate the performance of parallel supercomputers. The benchmarks are derived from computational fluid dynamics (CFD) applications https://www.nas.nasa.gov/software/npb.html


In this course we will use the "Multi-zone versions of NPB" (NPB-MZ). These are designed to exploit multiple levels of parallelism in applications and to test the effectiveness of multi-level and hybrid parallelization (MPI-OpenMP) paradigms and tools. Specifically we use the SP-MZ (even-size zones within a problem class, increased number of zones as problem class grows).

##### Problem Sizes:

| Class     | Mesh size (x)  | Mesh size (y)  | Mesh size (z)  |
| ----------- | ----------- | ----------- | ----------- |
| C | 240 | 320 | 28 |
| D | 1632  | 1216 | 34 |

Example jobscript
[NPB_job.sh](scripts/NPB_job.sh)



## Scientific Applications
### HemePure
> HemePure/HemeLB developed by the team of Prof Peter Coveney at University College London (UCL), is a software pipeline that simulates blood flow. HemePure is specifically designed to efficiently handle sparse topologies, supports real-time visualization and remote steering of the simulation and can handle fully resolved realistic vessels like those found in the human brain. https://github.com/UCL-CCS/HemePure        
https://github.com/UCL-CCS/HemePure-GPU

* The executables are located in the directory `/projects/0/energy-course/HemePure`. There you will find the `hemepure` and `hemepure_gpu` (CUDA enabled) exectubles.
**How to run a case**
We will be running through an example of pressure driven flow through a bifurcation available in the HemeLB download.

CPU example jobscript
[hemepure_cpu_job.sh](scripts/HemePure_CPU_job.sh)

GPU example jobscript
[hemepure_gpu_job.sh](scripts/HemePure_GPU_job.sh)

### Palabos

> The Palabos (Parallel Lattice Boltzmann Solver) library is a framework for general-purpose computational fluid dynamics (CFD), with a kernel based on the lattice Boltzmann method. The case we use in this course is a simulation of blood flow in a inside the 3D aneurysm geometry. https://palabos.unige.ch/

example jobscript
[palabos_job.sh](scripts/Palabos_job.sh)


### GROMACS
> **GROMACS** A free and open-source software suite for high-performance molecular dynamics and output analysis.

> **The HECBioSim Benchmarks:** (https://www.hecbiosim.ac.uk/access-hpc/benchmarks)

> **HECBioSim benchmark suite** consists of a set of simple benchmarks for a number of popular Molecular Dynamics (MD) engines, each of which is set at a different atom count. The benchmark suite currently contains benchmarks for the AMBER, GROMACS, LAMMPS and NAMD molecular dynamics packages.

In this example we will choose the "465K atom system - hEGFR Dimer of 1IVO and 1NQL" simulation (which can be found here <https://github.com/victorusu/GROMACS_Benchmark_Suite/tree/1.0.0/HECBioSim/hEGFRDimer>). This simulation contains a total number of atoms = 465,399 (Protein atoms = 21,749  Lipid atoms = 134,268  Water atoms = 309,087  Ions = 295). The run will take about 10 minutes to execute (using all 128 cores of an AMD ROME node). The image below shows the simulation that we will run.

- **20K atom system** 
```
curl -LJ https://github.com/victorusu/GROMACS_Benchmark_Suite/raw/1.0.0/HECBioSim/Crambin/benchmark.tpr -o Crambin_benchmark.tpr
```
- **1.4M atom system** 
``` 
curl -LJ https://github.com/victorusu/GROMACS_Benchmark_Suite/raw/1.0.0/HECBioSim/hEGFRDimerPair/benchmark.tpr -o hEGFRDimerPair_benchmark.tpr
``` 
- **3M atom system** 
```
curl -LJ https://github.com/victorusu/GROMACS_Benchmark_Suite/raw/1.0.0/HECBioSim/hEGFRDimerSmallerPL/benchmark.tpr -o hEGFRDimerSmallerPL_benchmark.tpr
```





### PyTorch
> The ResNet model is based on the Deep Residual Learning for Image Recognition from this paper https://arxiv.org/abs/1512.03385 
https://pytorch.org/hub/pytorch_vision_resnet/

**torchvision should be installed in your environment first**

Example how to install 2023
```
module load 2023
module load PyTorch/2.1.2-foss-2023a-CUDA-12.1.1
module load torchvision/0.16.0-foss-2023a-CUDA-12.1.1
```

Example jobscript
[PyTorch_job.sh](scripts/PyTorch_job.sh)

