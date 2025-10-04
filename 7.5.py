# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:10:19 2023

@author: Super Warrior
"""

import numpy as np

n = 100
a = 0
b = 1

def f(x):
    return np.exp(-(x**2))

h = b - a
I1 = ((b - a)/2 * (f(a) + f(b/2)) )/ 2
I2 = ((b - a)/2 * (f(b/2) + f(b)) )/ 2
I = I1 + I2

print(I)