# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:28:21 2017

@author: Calil
"""

# List declaration
vals = [True, False]

## And truth table
for v1 in vals:
    for v2 in vals:
        out_str = str(v1) + " and " + str(v2) + \
        " = " + str(v1 and v2)
        print(out_str)

## Or truth table    
for v1 in vals:
    for v2 in vals:
        out_str = str(v1) + " or " + str(v2) + \
        " = " + str(v1 or v2)
        print(out_str)