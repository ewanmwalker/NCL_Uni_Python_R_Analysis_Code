# -*- coding: utf-8 -*-
"""
7.2

Euler's Method solving differentials depending on t and y
"""

import numpy as np
import matplotlib.pyplot as plt

# No need to change the function
def euler(f,y0,t):
    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])
        
    return y

# Change these lines
t = np.linspace(0,20,100)
y0 = 1

def rhs(y,t):
    return -y * np.cos(t)

y = euler(rhs,y0,t)

z=np.exp(-np.sin(t))

plt.plot(t,y)
plt.plot(t,z,'--')