# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:59:41 2017

@author: Calil
"""

import numpy as np

# Criar arrays
a1 = np.array([0, 1, 2, 3])
a2 = np.arange(0,4)
a3 = np.zeros(10)
a4 = np.array([[1, 2],[3, 4]])

# Operacoes com escalar
print(a1)
print(a1 + 3)
print(3*a1)

# Operacoes elemento a elemento
print(a1*a2)
print(a1 + a2)
print(a4 + np.array([10, 20]))

# Shape
print(a3.shape)
print(a4.shape)