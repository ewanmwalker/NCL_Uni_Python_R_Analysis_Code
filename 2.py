# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:52:17 2023

@author: Super Warrior
"""

import numpy as np
import scipy.linalg as sla
import matplotlib.pyplot as plt

# Lambda matrix
L = np.array([[0,-1],[5,10]])

# Get eigenvalues and eigenvectors
eigenvalues,eigenvectors = sla.eig(L)

print("Max lambda: {}".format(max(eigenvalues)))
print("Critical h: {}".format(2/max(eigenvalues).real))

for h in [0.02,0.021]: 
    t = np.arange(0,5+h,h)
    y1 = np.zeros(len(t))
    y2 = np.zeros(len(t))

    # Initial conditions
    y1[0] = 2
    y2[0] = -2

    # Solve with Euler Method
    for n in range(len(t)-1):
        y1[n+1] = y1[n] + (t[n+1]-t[n]) * (y2[n])
        y2[n+1] = y2[n] + (t[n+1]-t[n]) * (-101*y1[n]-99*y2[n])

    # Make a plot
    plt.figure()
    plt.plot(t,y1,t,y2)
    plt.title("h = {}".format(h))
    plt.xlabel("$t$")
    plt.legend(["$y_1(t)$","$y_2(t)$"])
    