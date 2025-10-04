# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:04:30 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
import ode_methods as ode

x = np.arange(0,7)
y = np.arange(0,13)

X,Y = np.meshgrid(x,y)

DX = np.ones(X.shape)   # T.shape just gives the dimensions of T
DY = (3*X**2 - 2*Y**2) / (Y+6)

plt.quiver(X,Y,DX,DY)


# Function for RHS
def rhs(y,x):
    return (3*x**2 - 2*y**2) / (y+6)

# t array
h = 0.2
t = np.arange(0,6+h,0.2)

# Initial y
y0 = 1
    # Solve
y0_euler = ode.euler(rhs,y0,t)
plt.plot(t,y0_euler,"-", label="y0=1")

# Initial y
y1 = 8
    # Solve
y1_euler = ode.euler(rhs,y1,t)
plt.plot(t,y1_euler,"-", label="y0=8")
    
plt.legend(loc=4)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quiver plot of the ODE with two y0 values, solved using Euler's Method")


#b

print(y1_euler[-1] - y0_euler[-1])