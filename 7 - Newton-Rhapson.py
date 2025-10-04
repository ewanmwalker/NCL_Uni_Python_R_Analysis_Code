# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:59:16 2023

@author: Super Warrior
"""

import numpy as np
# Create your functions below

def fx(x):
    return (4/3*x**3) + 70*np.cos(x)
    
def dfdx(x):
    return 4*x**2 - 70*np.sin(x)


# Starting guess
x = 4.5

# Chose an epsilon value
eps = 1e-8

# While loop 
while abs(fx(x))>eps:
    x = x - fx(x)/dfdx(x)

    print(x)