# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:49:03 2023

@author: Super Warrior
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

x0 = 2.75
k = np.sin(x0 / 2)

T_traps = []

for n in range(24,240):
    x = np.linspace(0,2*np.pi,n)
    y = 1 / (np.sqrt(1-k**2 * np.sin(x)**2))

    T_trap = 4* np.sqrt(2/3) * integrate.trapezoid(y,x)
    
    T_traps.append(T_trap)


def f(x):
    return 1/ (np.sqrt(1-k**2 * np.sin(x)**2))

i = integrate.quad(f,0,2*np.pi)

T_quad = 4* np.sqrt(2/3) * integrate.quad(f,0,2*np.pi)[0]

eps = abs(np.array(T_traps) - T_quad)

plt.plot(np.linspace(0.05,0.5,216),eps)
plt.xlabel("h")
plt.ylabel("The absolute difference Ttrap - Tquad / eps")
plt.title("Plot to show how the accuracy of integrate.trapezoid increases with the number of trapeziums")