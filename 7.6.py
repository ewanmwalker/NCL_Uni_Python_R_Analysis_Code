# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:13:10 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

n=100
a = 0
b = 1

x = np.linspace(-1,2,n*3)

#function
def f(x):
    return np.exp(-(x**2))

#plot the line
y = f(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")

#plot the trapezoids
plt.fill_between([a,b/2],[f(a),f(b/2)],color='firebrick')
plt.fill_between([b/2,b],[f(b/2),f(b)],color='lightblue')