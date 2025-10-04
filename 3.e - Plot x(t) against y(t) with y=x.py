# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:06:45 2021

@author: c0081806
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0.1,10,600)
x = (0.5*t)+((np.cos(12*t))/t)
y = (0.5*t)+((np.sin(12*t))/t)

# y=x line
a=np.arange(-10,10)
b=a

# Labels
plt.xlabel("y(t)")
plt.ylabel("x(t)")
plt.title("Plot of x(t) = 0.5t+cos(12t)/t \n agaist y(t) = 0.5t+sin(12t)/t")

# Change axis position
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Axis limit
plt.xlim([-10,10])
plt.ylim([-10,10])

# Plots
plt.plot(a,b,'--', label="y=x")
plt.plot(y,x)
