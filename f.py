# -*- coding: utf-8 -*-
"""
Assignment 2

f
"""
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-4,5,100)

def f(x):
    return x**4 - 3*x**3 - 10*x**2 + 4*x + 1

g = f(z)

p = [1,-3,-10,4,1] 
r = np.roots(p)

colours = np.random.rand(len(r))

plt.plot(z,g)
plt.axis([-5.5,5.5,-100,100])
plt.scatter(r, np.zeros(len(r)), c=colours, s=100)
plt.xlabel("x")
plt.ylabel("g(x)")
plt.title("Plot of x**4 - 3*x**3 - 10*x**2 + 4*x + 1 with roots")
