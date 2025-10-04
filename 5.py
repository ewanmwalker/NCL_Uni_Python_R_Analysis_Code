# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:45:09 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(x, t):
    y, u = x                # reads in values in x and assigns to y and u
    dydt = u                # rhs of dy/dt
    dudt = -u + 2*y         # rhs of du/dt 
    return [dydt, dudt]

x0 = [0,1]
t = np.linspace(0,5,100)
x = odeint(model,x0,t)

plt.plot(t,x[:,0])
plt.xlabel('t')
plt.ylabel('y(t)')