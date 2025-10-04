# -*- coding: utf-8 -*-
"""
Exercise 7.1

Euler's Method solving differentials

@author: c0081806
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,5,20)
y = np.zeros(len(t))
h = t[1]-t[0]

y[0] = 3

for i in range(len(t)-1):
    y[i+1] = y[i] + h * (y[i])
    
plt.plot(t,y)
plt.plot(t,3*np.exp(t),'--')
plt.xlabel('t')
plt.ylabel('y(t)')