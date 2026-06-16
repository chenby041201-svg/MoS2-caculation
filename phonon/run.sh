#! /bin/bash
# Band structure of Graphene
############################
source /public1/soft/module/module.sh
module load qe/7.0.0-oneAPI.2022.1
mpirun -np 64 pw.x < scf.in > scf.out
mpirun -np 16 ph.x < ph.in > ph.out
mpirun -np 16 q2r.x < q2r.in > q2r.out
mpirun -np 16 matdyn.x < matdyn.in > matdyn.out
