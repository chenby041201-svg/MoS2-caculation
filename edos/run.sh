#! /bin/bash
# Band structure of Graphene
############################
source /public1/soft/module/module.sh
module load qe/6.7.0-oneAPI.2022.1
mpirun -np 32 pw.x < scf.in > scf.out
mpirun -np 32 pw.x < nscf.in > nscf.out
mpirun -np 32 dos.x < dos.in > dos.out
