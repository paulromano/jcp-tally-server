#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Use Latin Modern type 1 fonts
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font',**{'family':'serif','serif':['Computer Modern']})

# Parameters for Computer
mu    = 1./76.    # Particles per second on Intrepid BG/P
alpha = 3.5346e-6 # Average ping-pong latency on Intrepid BG/P
beta  = 2.5961e-9 # Bandwidth on Intrepid BG/P

# Parameters from OpenMC simulation
dmax = 15360
d = np.arange(8, dmax, 4) # Data/event (19.2 kb for depletion)

for f in [5.7, 21.3, 132]:
    # Calculate time for given numbers of events
    overhead = (1. + f/mu*(alpha + d*beta))**2 - 1.

    # Plot overhead
    plt.loglog(d, overhead, label='$f={0}$'.format(f))

# Print maximum support ratio
print("c/s = {0}".format(mu/(21.3*(alpha + 15360*beta))))

# Set plotting options
plt.xlim([0,dmax])
plt.xlabel(r'Data per event (bytes)', fontsize=16)
plt.ylabel(r'Overhead per batch ($t/t_0 - 1$)', fontsize=16)
plt.grid(True, which='both')
plt.legend(loc='upper left')

# Display plot
#plt.show()
plt.savefig('model_intrepid.pdf')
