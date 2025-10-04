# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:34:15 2023

@author: Super Warrior
"""

import numpy as np

# Set up an array of x points
n = 100
x = np.linspace(0,2*np.pi,n)

# Throw out end point, since it is a 'duplicate'
x = x[:n-1]

# Continue the code below

# Set h
h = x[1]-x[0]

# create an array f
f = np.sin(x)

# Create an array dfdx
dfdx = (np.roll(f,-1) - np.roll(f,1)) / (2*h)