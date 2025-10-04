# -*- coding: utf-8 -*-
"""
Test script to print value
"""

#Modules
import numpy as np
import matplotlib.pyplot as plt

#Setting x axis
x=np.linspace(-3,3,1000)

#Plotting y values for y^3=x^2 + n
for n in range(1,10):
    y=np.sqrt(pow(x,3)+n)
    plt.plot(x,y)
    plt.plot(x,-y)

#Labels
plt.title("mordell Curves")
plt.xlabel("x")
plt.ylabel("y")