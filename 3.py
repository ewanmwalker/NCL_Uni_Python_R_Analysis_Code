# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:38:00 2022

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-40,40,300)

y = ((5 * np.sin(x) ) / x ) - 2

yl = 0*x - 2

plt.plot(x,y)
plt.plot(x,yl)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("A plot of y(x) versus x with a line at y=-2")

print(min(y))

A = []

for n in range(0,299):
    if y[n] < -2:
        A.append(y[n])
        
print(len(A))