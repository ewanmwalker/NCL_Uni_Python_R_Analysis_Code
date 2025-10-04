# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:25:05 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

# Initialise arrays
t = np.linspace(0,40,1600)
x = np.zeros(len(t))
y = np.zeros(len(t))

# Initial conditions
x[0] = 1
y[0] = 1

# Parameters
a = 2/3
b = 4/3
c = 1
d = 1

for n in range(len(t)-1):
    x[n+1] = x[n] + (t[n+1]-t[n]) * (a*x[n] - b*x[n]*y[n])
    y[n+1] = y[n] + (t[n+1]-t[n]) * (c*x[n]*y[n] - d*y[n])
    
plt.plot(t,x,'-')
plt.plot(t,y,'-')