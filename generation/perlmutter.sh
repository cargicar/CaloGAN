#!/bin/bash
#SBATCH --image=docker:geant4/geant4:latest
#SBATCH --nodes=1
#SBATCH --qos=regular
#SBATCH --constraint=cpu
#SBATCH --account=m3246
#SBATCH --time=00:30:00 
srun -n 32 shifter --env-file=/global/homes/c/ccardona/CaloGAN/datasets.env ./build/generate -m run2.mac