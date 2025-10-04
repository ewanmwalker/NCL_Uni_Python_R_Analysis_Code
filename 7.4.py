# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:55:52 2023

@author: Super Warrior
"""

import numpy as np

n = 100
a = 0
b = 1

def f(x):
    return np.sqrt(x**3 + 1)

h = b - a
I = ((b - a) * (f(a) + f(b)) )/ 2

print(I)