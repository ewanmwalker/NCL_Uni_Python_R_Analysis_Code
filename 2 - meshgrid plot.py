# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:03:47 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

# Complete these two lines
theta = np.linspace(0,2*np.pi,50)
phi = np.linspace(0,2*np.pi,50)

# No need to edit this line
THETA,PHI = np.meshgrid(theta,phi)

X = (3 + np.cos(THETA)) * np.cos(PHI)
Y = (3 + np.cos(THETA)) * np.sin(PHI)
Z = np.sin(THETA)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(X,Y,Z, cmap='rainbow')

ax.set_zlim([-3,3])