# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:49:20 2023

@author: Super Warrior
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t):
    x, u = y
    
    dxdt = u
    dudt = -3/2 * np.sin(x)
    
    return [dxdt , dudt]

t = np.linspace(0,25,250)

y = odeint(model,[2.75,0],t)

y1 = y[:,0]
#y2 = y[:,1]

#plt.plot(t,y1)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Plot of x(t) vs t for the model, 0<=t<=25")

x = y[:,0] + 2.75

plt.plot(t,y[:,0])
