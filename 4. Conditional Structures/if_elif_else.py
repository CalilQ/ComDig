# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 16:43:30 2017

@author: Calil
"""

# Receber dado do usuario
print("Informe um numero: ")
num = int(input())

# Testar sinal do numero
if num < 0:
    print("num < 0")
elif num == 0:
    print("num = 0")
else:
    print("num > 0")