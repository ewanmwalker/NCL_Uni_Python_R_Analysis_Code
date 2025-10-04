# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:59:11 2023

@author: Super Warrior
"""

import numpy as np
from scipy import integrate

def func(x):
    return x*np.exp(-x**0.8)+0.2

n = 1
x = np.linspace(0,8,n)
y = func(x)
T = integrate.trapezoid(y,x)

#quad function
myint = integrate.quad(func, 0, 8)

while myint[0]-T > 1e-6:
    # Set up x and y based on n and integrate
    x = np.linspace(0,8,n)
    y = func(x)
    T = integrate.trapezoid(y,x)
    n = n + 1

print(n-1)