# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:22:42 2023

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

r = 3.8
x = np.zeros(100)
x[0] = 0.2
for n in range(len(x)-1):
    x[n+1] = x_iter(x[n],r)

plt.plot(x)
print("final value: x = {}".format(x[-1]))