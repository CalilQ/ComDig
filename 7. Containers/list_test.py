# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 19:25:57 2017

@author: Calil
"""

# Criar variavel
my_list = [1 ,3.1514, "Obi-Wan", [1, 2, 3]]
print(my_list)

# Acessar elementos
print(my_list[0])
print(my_list[1])
print(my_list[2])

# Alterar elementos
my_list[2] = "Leia"
print(my_list[2])

# Slicing e indices negativos
print(my_list[2:4])
print(my_list[-2])

# len e deletar elementos
print(len(my_list))
del my_list[1]
print(my_list)

# Adicionar elementos
my_list.append("I S2 ComDig")
print(my_list[-1])
print(len(my_list))