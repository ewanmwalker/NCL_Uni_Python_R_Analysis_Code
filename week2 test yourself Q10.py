# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:25:02 2022

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

x = np.arange(0,2,0.2)
y = np.array([0, -0.3, -1.0, -1.7, -1.9,-1.6, -0.9, -0.2, 0.0, -0.3])

def model(x,a,b,c):
    return a*np.exp(-((x-b)**2)/(2*c**2))

popt, pcov = opt.curve_fit(model,x,y)
print(popt)

plt.plot(x,y,'x')

x1 = np.linspace(0,2,100)
y1 = model(x1,popt[0],popt[1],popt[2])

plt.plot(x1,y1)

