# -*- coding: utf-8 -*-
"""
Simpson's Rule
"""

import numpy as np

a = 0
b = 1
n = 100

def f(x):
    return np.sqrt(x**3 + 1)

#Simpson's Rule
I = (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

print(I)
