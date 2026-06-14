# Import the necessary packages and modules
import matplotlib.pyplot as plt
import os
import numpy as np
os.chdir('F:/MoS2计算/pdos')

# The Fermi energy, find it in nscf.out
efermi = -1.6667

# Define the function to read the data file
def r_dos(name):
    ener, dos = np.loadtxt(name, usecols=(0,1), unpack=True)
    return ener, dos

# Open and read the total PDOS
ener, dos = r_dos('mos2.pdos_tot')
# Open and read the PDOS files for Mo atom number 1
ener1, p1Mo1d = r_dos('mos2.pdos_atm#1(Mo)_wfc#1(d)')
ener1, p1Mo2s = r_dos('mos2.pdos_atm#1(Mo)_wfc#2(s)')
ener1, p1Mo3p = r_dos('mos2.pdos_atm#1(Mo)_wfc#3(p)')
# Open and read the PDOS files for S atom number 1
ener2, p2S1s = r_dos('mos2.pdos_atm#2(S)_wfc#1(s)')
ener2, p2S2p = r_dos('mos2.pdos_atm#2(S)_wfc#2(p)')
ener2, p2S3d = r_dos('mos2.pdos_atm#2(S)_wfc#3(d)')
# Open and read the PDOS files for S atom number 2
ener3, p3S1s = r_dos('mos2.pdos_atm#3(S)_wfc#1(s)')
ener3, p3S2p = r_dos('mos2.pdos_atm#3(S)_wfc#2(p)')
ener3, p3S3d = r_dos('mos2.pdos_atm#3(S)_wfc#3(d)')
# Create figure object
plt.figure()
# Plot the DOS
plt.plot(ener-efermi, dos, c='k')
# Plot the PDOS of S of s-orbital
plt.plot(ener1-efermi, p2S1s+p3S1s, c='b')
# Plot the PDOS of S of p-orbital
plt.plot(ener2-efermi, p3S2p+p2S2p, c='r')
# Plot the PDOS of S of d-orbital
plt.plot(ener3-efermi, p3S3d+p2S3d, c='g')
# Add the x and y-axis labels
plt.xlabel('Energy (eV)')
plt.ylabel('PDOS (state/eV/unit-cell)')
# Set the axis limits
plt.xlim(-20, 30)
plt.ylim(0, 6)
# Save the figure
plt.savefig('plot-pdos.pdf')
# Show the figure
plt.show()