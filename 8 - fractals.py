# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:00:15 2023

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

p = [1,0,0,0,-1]
r = np.roots(p)
print(r)

def f(x):
    return x**4 - 1

def dfdx(x):
    return 4*x**3

def get_root_index(z,r,eps):
    """
    Returns the index of the root closest to z
    """ 
    root = 0
    for j in range(0,len(r)):
        if np.isclose(z,r[j],eps):
            root = j + 1
    return root


eps = 0.0001
max_iterations = 100

# Create an array to store roots in
n  = 250
a = np.linspace(-1,1,n)
b = np.linspace(-1,1,n)
m = np.zeros([n,n])

for i in range(n):
    for j in range(n):
        z = complex(a[i],b[j])
        for k in range(max_iterations):
            z = z - f(z)/dfdx(z)
            if abs(f(z)) < eps:
                break
        root = get_root_index(z,r,eps)
        m[i,j] = root
        

# Make a larger figure than default (might want to put on my wall)
plt.figure(figsize=(15,15))

# Turn the axis off for aesthetics
plt.axis('off')

# Make the image using the plasma colour map
# origin='lower' puts (0,0) in the bottom left
plt.imshow(m,cmap='plasma',origin='lower')