# -*- coding: utf-8 -*-
"""
7.4
Bisection Method setup for f(x)= x^2 - 2
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,2,100)

def myfunc(x):
    return pow(x,2)-2

xl = 1.25
xh = 1.5
xmid = (xl + xh)/2

print(xmid)

plt.plot(x,myfunc(x))