# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:34:43 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt


# I've separated off the function here
def f(t, y): 
    return -y/2

# Initialise t and y
t = np.linspace(0,5,5)
y = np.zeros(len(t))
y[0] = 5
h = t[1] - t[0]

# Runge-Kutta Method
for n in range(0, len(t)-1): 

    h = t[n+1]-t[n]
    k1 = f(t[n], y[n]) 
    k2 = f(t[n] + 0.5 * h, y[n] + h * 0.5 * k1) 
    k3 = f(t[n] + 0.5 * h, y[n] + h * 0.5 * k2) 
    k4 = f(t[n] + h, y[n] + h * k3) 
  
    # Update next value of y 
    y[n+1] = y[n] + (1.0 / 6.0)*h*(k1 + 2 * k2 + 2 * k3 + k4) 
  
    
  
# Euler Method function from the handout    
def euler(f,y0,t):
    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(t[n],y[n])*(t[n+1]-t[n])
        
    return y

y2 = euler(lambda t,y: -y/2,5,t)

# Make a plot
t2 = np.linspace(0,5,100)
plt.plot(t2,5*np.exp(-t2/2))
plt.plot(t,y,'-o')
plt.plot(t,y2,'-o')
plt.legend(['Exact solution','Runge-Kutta','Euler'])
plt.xlabel('t')
plt.ylabel('x(t)')