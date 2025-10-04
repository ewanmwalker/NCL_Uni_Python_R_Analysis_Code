# -*- coding: utf-8 -*-
"""
Plotting sin(x)

@author: c0081806
"""
import numpy as np
import matplotlib.pyplot as plt

#Values
x = np.linspace(0,10,100)
y = np.sin(x)

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.plot(x,y)
        