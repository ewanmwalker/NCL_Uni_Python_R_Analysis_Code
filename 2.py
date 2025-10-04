# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:16:06 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(f,y0,t):
    """
    Returns the solution y(t) for an initial value problem
    dy/dt = f(y,t)
    for an array t and initial value y0
    """

    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])

    return y

t = np.linspace(0,20,100)
y0 = 1
y = euler(lambda y,t: -y*np.cos(t), y0, t)
plt.plot(t,y)