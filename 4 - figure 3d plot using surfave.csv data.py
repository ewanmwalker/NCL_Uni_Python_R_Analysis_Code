# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:16:59 2023

@author: Super Warrior
"""
import matplotlib.pyplot as plt
import numpy as np

# new figure
fig = plt.figure(figsize=(15,10))
plt.rcParams['font.size'] = 20

# 3d axes
ax = plt.axes(projection='3d')


# Load the file (this works if in the same directory as your script
# Otherwise put full path in
Z = np.loadtxt('surface.csv',delimiter=',')

# Create a meshgrid using the length of Z
x = np.arange(len(Z))
y = np.arange(len(Z))
X,Y = np.meshgrid(x,y)

# Plot
surf = ax.plot_surface(X, Y, Z)

# Axis labels - note applied to the axes in a 3D plot
ax.set_xlabel('x',labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('z', labelpad=10)