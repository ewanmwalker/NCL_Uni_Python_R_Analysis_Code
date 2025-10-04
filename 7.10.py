# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:20:43 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

T = integrate.trapezoid(y,x)

x1 = np.linspace(0,5,100)

plt.plot(x , y ,'-o')
plt.plot(x1 , x1**2)