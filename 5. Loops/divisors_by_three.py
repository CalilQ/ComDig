# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:38:38 2017

@author: Calil
"""

# Receive data
print("Informe um numero")
num = int(input())
# Pular uma linha
print("\n")

# Percorrer de k = 0 ate k = num - 1
for k in range(2,num):
    res = k % 3;
    # Formatar string para mostrar variaveis
    print("{} % 3 = {}".format(k, res))
