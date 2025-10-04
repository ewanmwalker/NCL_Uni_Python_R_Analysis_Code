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

plt.xlabel("t")
plt.plot(t,x,t,y)
plt.legend(['x(t)','y(t)'],loc=1,)
plt.title("Plot of x(t) = 0.5t+cos(12t)/t \n and y(t) = 0.5t+sin(12t)/t")