# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:22:57 2017

@author: Calil
"""

import numpy as np
import matplotlib.pyplot as plt

# Criar sinais
fs = 1e4
t_max = 9
f = 200
damp = -10
# Tempo
t = np.linspace(0,t_max,num=int(t_max*fs))
# Seno
s = np.sin(2*np.pi*f*t)
# Exponencial
e = np.exp(damp*t)
# Seno * Exponencial
se = s*e
# Quadrada
s2 = np.sin(2*np.pi*(f/2)*t)
q = np.sign(s2)

# Plotar no tempo
plt.figure(figsize=(12,12))
plt.subplot(211)
plt.plot(t,se,'k',t,e,'r--')
plt.plot(t,q,'g-.',linewidth=0.5)
plt.xlim([t[0], t[1000]])
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plotar PSD
plt.subplot(212)
plt.magnitude_spectrum(se, Fs=fs, Fc=0, color='k', scale='dB')
plt.magnitude_spectrum(e, Fs=fs, Fc=0, color='r',linestyle='--',linewidth=0.5, scale='dB')
plt.magnitude_spectrum(q, Fs=fs, Fc=0, color='g',linestyle='-.', scale='dB')
plt.xlim([0, 5000])

# Concluir
plt.savefig('output.png')
plt.show()
