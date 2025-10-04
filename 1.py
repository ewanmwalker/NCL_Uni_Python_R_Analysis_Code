# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:33:15 2023

@author: Super Warrior
"""
import ode_methods as ode
import numpy as np
import matplotlib.pyplot as plt

# Function for RHS
def rhs(y,t):
    return -y/2

# t array
t = np.arange(0,6,1)

# Initial y
y0 = 5

# Solve
y_euler = ode.euler(rhs,y0,t)
y_rk4 = ode.rk4(rhs,y0,t)
y_midpoint = ode.midpoint(rhs,y0,t)

# Plot methods
plt.plot(t,y_euler,"-o",label="Euler")
plt.plot(t,y_midpoint,"-o",label="Midpoint")
plt.plot(t,y_rk4,"-o",label="RK4")

# Plot exact
tt = np.linspace(0,5,100)
plt.plot(tt,5*np.exp(-tt/2),label="Exact")

plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()