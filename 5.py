# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:51:36 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

def x_iter(x,r):
    """
    Takes in x and r and returns 
    r*x*(1-x)
    """
    return r*x*(1-x)

x = 0.2
for r in np.linspace(2.7,4,250):
    # List to store unique values for this r
    v = []
    for n in range(200):
        x = x_iter(x,r)
        if n > 100 and round(x,6) not in v:
            v.append(round(x,6))
    # x value for each v value to make the plot
    rx = r*np.ones(len(v))          
    plt.plot(rx,v,'ko',markersize=0.5)

plt.xlabel('r')
plt.ylabel('x')