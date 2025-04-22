#!/bin/bash
#SBATCH --image=docker:geant4/geant4:latest
#SBATCH --nodes=1
#SBATCH --qos=regular
#SBATCH --constraint=cpu
#SBATCH --account=m3246
srun -n 128 shifter ./build/generate -m run2.mac