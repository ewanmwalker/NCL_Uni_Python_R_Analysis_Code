# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:00:01 2023

@author: Super Warrior
"""
import numpy as np
from scipy.integrate import odeint

# Function that returns dy/dt
def rhs(y,t):
    dydt = -(t**2)/2
    return dydt

# Initial condition
y0 = 10

# Time points
t = np.linspace(0,5,100)

# Solve ODE
y = odeint(rhs,y0,t)