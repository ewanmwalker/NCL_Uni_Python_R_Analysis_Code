# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:31:01 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**3 - 4*x -5

x = np.linspace(2,2.5,100)

x_mid = func((2+2.5)/2)

plt.plot(x,func(x))
