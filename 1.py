# -*- coding: utf-8 -*-
"""
Week 6 Handout e1

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.5)
y = np.arange(-np.pi, np.pi, 0.5)

X,Y = np.meshgrid(x, y)

U = Y * np.cos(X)
V = Y * np.sin(X)

plt.quiver(X,Y,U,V)
