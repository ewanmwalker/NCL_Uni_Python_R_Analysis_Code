# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:27:14 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,0,1000)

x = t * np.sin(50*t)
y = t * np.cos(50*t)
z = t

# new figure
fig = plt.figure(figsize=(15,10))
plt.rcParams['font.size'] = 20

# 3d axes
ax = plt.axes(projection='3d')

ax.plot(x,y,z,linewidth=5)