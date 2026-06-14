# Import the necessary packages and modules
import matplotlib.pyplot as plt
import os
import numpy as np
os.chdir('F:/MoS2计算/edos')

# The Fermi energy, find it in header row of gr.dos
efermi = -1.6667

# Open and read the file gr.dos
ener, dos, idos = np.loadtxt('mos2.dos', unpack=True)
    
# Create figure object
plt.figure()
# Plot the DOS, in which the Fermi energy shifts to zero
plt.plot(ener-efermi, dos, c='b')
# Add the x and y-axis labels
plt.xlabel('Energy (eV)')
plt.ylabel('DOS (state/eV/unit-cell)')
# Set the axis limits
plt.xlim(-16, 25)
plt.ylim(0, 10)
# Save the figure to the pdf file
plt.savefig('plot-dos.pdf')
# Show the figure
plt.show()