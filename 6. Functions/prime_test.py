# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:11:56 2017

@author: Calil
"""

"""
Testa se um numero e primo
"""

def is_prime(num):
    # Teste se e primo
    prime = True
    # Divisor
    divs = 2
    
    # Testar enquanto numero for
    # primo e diferente do
    # divisor
    while prime and divs != num:
        # num nao e primo se for
        # divisivel por divs
        prime = ((num % divs) != 0)
        divs += 1
    
    return prime
        