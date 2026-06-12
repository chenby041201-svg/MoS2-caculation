#! /bin/bash
source /public1/soft/module/module.sh
module load qe/6.7.0-oneAPI.2022.1
mpirun -np 64  pw.x < scf1.in > scf.out