# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:24:05 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt

from capacity_plot import plot_1b, plot_2b, plot_gaus
from quant_2_bit import plot_cap_l, optimize_info

out_file = open("output.txt", "w")

# Mutual information optimazation
l = np.linspace(0.01,4,num=100)
eb_n0_vals = [-5.0, -2.0, 0.0, 3.0, 7.0]
ax = plot_cap_l(l,eb_n0_vals)
plt.savefig('figs\\cap_vs_l.png')
plt.show(ax)

max_l = optimize_info(eb_n0_vals)
for k in range(0,len(eb_n0_vals)):
    out_file.write("\nl = "+str(float(max_l[k]))+" maximizes C for Eb/N0 = "+\
                                      str(eb_n0_vals[k])+"dB")

# Set Eb/N0
eb_n0_db = np.linspace(0,10)

# 1 bit quantization
ax = plot_1b(eb_n0_db)

# 2 bit quatization
ax = plot_2b(eb_n0_db,ax)

# 2 bit quatization
ax = plot_gaus(eb_n0_db,ax)

# Plot all
ax.legend()
plt.savefig('figs\\cap_vs_eb_n0.png')
plt.show(ax)

# Close file
out_file.close()