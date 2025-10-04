# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:19:34 2022

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

x = np.arange(0,13)
y = np.array([ 0.9, 0.9, 2.3, 4.1, 5.3, 7.1, 8, 8.1, 8.3, 10.1, 11.7, 13.6, 14.4 ])

x1 = np.linspace(0,12,100)

p = np.polyfit(x,y,1)
f = p[0]*x1 + p[1]

S = sum( (f - y)**2 )

y1 = p[0]*x1 + p[1]

def gfunc(x,a,b,c):
    return a*x + b + np.sin(c*x)

popt, pcov = opt.curve_fit(gfunc, x, y)
g1 = gfunc(x1,popt[0],popt[1],popt[2])

plt.plot(x,y,'x')
plt.plot(x1,y1)
plt.plot(x1,g1)

plt.xlabel("x")
plt.ylabel('y')
plt.legend(["Data points","f(x)","g(x)"])
plt.title("A plot of 2 different fitting models to given data")