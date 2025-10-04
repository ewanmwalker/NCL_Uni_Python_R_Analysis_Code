# -*- coding: utf-8 -*-
"""
7.3

For x0 in np.arange plot function
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(f,y0,t):
    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])
        
    return y

t = np.linspace(0,10,100)
r = 0.5

def rhs(x,t):
    return r*x*(1-x)

for x0 in np.arange(0,1.1,0.1):
    x = euler(rhs,x0,t)
    plt.plot(t,x)

