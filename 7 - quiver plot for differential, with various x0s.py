# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:13:43 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 11)
x = np.arange(-15,15,2)

T, X = np.meshgrid(t,x)

DT = np.ones_like(T)
DX = (X-3*T)/(1+T)

plt.quiver(T,X,DT,DX)


leg= []
# Add solutions x(0)=3,4,5
for x0 in [3,4,5]:
    t1 = np.linspace(0,10,100)
    x1 = odeint(lambda x,t:(x-3*t)/(1+t),x0,t1)
    plt.plot(t1,x1,linewidth=4)
    leg.append('x(0)={}'.format(x0))
    
# Make pretty
plt.xlabel('t')
plt.ylabel('x')
plt.legend(leg)