# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:06:18 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,9)
y = np.linspace(-2,2,9)

X,Y = np.meshgrid(x,y)

u = np.ones(81)
v = np.ones(81)

plt.quiver(X,Y,u,v)