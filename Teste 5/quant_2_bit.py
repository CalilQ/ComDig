# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:04:54 2017

@author: Calil
"""

from numpy import array, sqrt, log2
from scipy.stats import norm
from scipy.optimize import fmin
import matplotlib.pyplot as plt

def f_func(l: array, eb_n0: float):
#    f = norm.sf(sqrt(2*eb_n0)*(1+l))
    f = norm.sf(sqrt(2*eb_n0) + l)
    return f

def mutual_info(l: array, *args):
    
    eb_lin = 10.0**(args[0]/10.0)
    
    f_plus = f_func(l,eb_lin)
    f_zero = f_func(0,eb_lin)
    f_minu = f_func(-l,eb_lin)
    
    info = log2(2*(1 - f_minu)/(1 - f_minu + f_plus)) +\
           f_plus*log2(((f_minu - f_plus)*f_plus)/((1 - f_minu + f_plus)*(f_zero - f_plus))) +\
           f_zero*log2((f_zero - f_plus)/(f_minu - f_zero)) +\
           f_minu*log2(((1 - f_minu + f_plus)*(f_minu - f_zero))/((f_minu - f_plus)*(1 - f_minu)))
           
    return info

def optimize_info(eb_n0_vals: list):
    max_l = list()
    
    for eb_n0 in eb_n0_vals:
        max_l.append(fmin(lambda l, *args: -mutual_info(l,*args),0.9,args=(eb_n0,"")))
        
    return max_l

def plot_cap_l(l: array, eb_n0_vals: list):
    ax = plt.subplot(111)
    
    for eb_n0 in eb_n0_vals:
        info = mutual_info(l,eb_n0)
        ax.plot(l,info)
        txt = str(eb_n0)+"dB"
        ax.text(l[-1]-0.5,info[-1]+0.02,txt)
    
    ax.set_xlim(min(l),max(l))
    ax.set_ylim(0.2,1.05)
    ax.set_xlabel("Quantization limits")
    ax.set_ylabel("Channel capacity [bits per channel use]")
    ax.grid()
    plt.show(ax)