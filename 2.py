# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:01:40 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial y
y0 = 1

# t array
t = np.linspace(0,20,100)

# Parameter b
b = 2
def rhs(y,t,b):
    dydt = b / y
    return dydt

y = odeint(rhs,y0,t,args=(b,))

legend = np.zeros(5)

for b in range(1,5):
    y = odeint(rhs,y0,t,args=(b,))
    plt.plot(t,y,label='dy/dt = {} /y'.format(b))
    
plt.legend()
    
