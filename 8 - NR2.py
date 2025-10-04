# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:09:14 2023

@author: Super Warrior
"""

import numpy as np
# Create your functions below

def fx(x):
    return x**3 - 2*x**2 - 11*x + 12
    
def dfdx(x):
    return 3*x**2 - 4*x - 11

# Starting guess
x =2.352836323

# Chose an epsilon value
eps = 1e-8

# While loop 
while abs(fx(x))>eps:
    x = x - fx(x)/dfdx(x)

    print(x)