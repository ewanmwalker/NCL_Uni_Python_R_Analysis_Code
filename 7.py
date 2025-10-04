# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:59:21 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt 

t = np.arange(-2, 2, 0.25)
y = np.arange(0, 3, 0.5)
T, Y = np.meshgrid(t, y)

DT = np.ones(T.shape)   # T.shape just gives the dimensions of T
DY = np.sqrt(Y) / 5 + T**2/2

plt.quiver(T, Y, DT, DY, angles='xy')

