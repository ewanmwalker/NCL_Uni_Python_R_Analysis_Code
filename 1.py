# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 11:35:51 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# function on the rhs of dy/dt
def rhs(y,t):
    dydt = np.sin(t) / y
    return dydt

# initial condition
y0 = 1

# t array
t = np.linspace(0,20,200)

# solve ODE
y = odeint(rhs,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y(t)')

t1 = np.linspace(0,20,200)
plt.plot(t1, np.sqrt(3 - 2*np.cos(t)),'--')