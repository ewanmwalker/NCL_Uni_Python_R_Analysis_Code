# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q3
"""
import numpy as np
import matplotlib.pyplot as plt

def euler(f,y0,t):
    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])
        
    return y

y0 = 6
t = np.linspace(0,7,20)

def rhs(y,t):
    return -4*y

y = euler(rhs,y0,t)



plt.plot(t,y)