# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:03:32 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

# Change t to adjust the accuracy
t = np.linspace(0,5,50)
y = np.zeros(len(t))
h = t[1]-t[0]

y[0] = 3

for n in range(len(t)-1):
    y[n+1] = y[n] + h * (y[n])

plt.plot(t,y,'-o')

t1 = np.linspace(0,5,100)
plt.plot(t1,3*np.exp(t1))
plt.legend(['Euler Method','Exact solution'])