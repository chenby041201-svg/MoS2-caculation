#! /bin/bash
# VC-RELAX for Graphene
####################################
source /public1/soft/module/module.sh
module load qe/6.7.0-oneAPI.2022.1
mpirun -np 32 pw.x < vc-relax.in > vc-relax.out