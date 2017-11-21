# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:54:51 2017

@author: Calil
"""

from numpy import array, sqrt, log2, zeros_like
from scipy.stats import norm
import matplotlib.pyplot as plt

from quant_2_bit import optimize_info, mutual_info

def plot_1b(eb_n0_dB: array):
    """
    Plots capacity vs Eb/N0 for 1 bit hard quatization
    """
    eb_n0 = 10**(eb_n0_dB/10)
    
    p = norm.sf(sqrt(2*eb_n0))
    h2 = -p*log2(p) - (1-p)*log2(1-p)
    c = 1 - h2
    
    ax = plt.subplot(111)
    
    ax.plot(eb_n0_dB,c,label="1 bit")
    plt.ticklabel_format(style='plain', axis='x', scilimits=(0,0))
    ax.set_xlim(min(eb_n0_dB),max(eb_n0_dB))
#    ax.set_ylim(0,1.05)
    ax.set_xlabel("Eb/N0 [dB]")
    ax.set_ylabel("Channel capacity [bits per channel use]")
    ax.grid()
    return ax

def plot_2b(eb_n0_vals: array, ax):
    
    opt_l = optimize_info(list(eb_n0_vals))
    
    info = zeros_like(eb_n0_vals)
    for k in range(0,len(eb_n0_vals)):
        info[k] = mutual_info(opt_l[k],eb_n0_vals[k])
        
    ax.plot(eb_n0_vals,info,label="2 bits")
    
    return ax

def plot_gaus(eb_n0_vals: array, ax):
    
    eb_n0 = 10**(eb_n0_vals/10)
    c = 0.5*log2(1 + eb_n0)
        
    ax.plot(eb_n0_vals,c,label="gausian")
    
    return ax
        