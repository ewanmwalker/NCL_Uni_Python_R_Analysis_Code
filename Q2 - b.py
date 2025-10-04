# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q2 - b
"""
import numpy as np

n = range(1,9)

x = np.zeros(9)
x[0] = 3

for i in n:
    x[i] = 5*x[i-1]