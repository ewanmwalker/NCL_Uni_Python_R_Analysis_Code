# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q1 - f
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,200)

f = 4*pow(x,2)*pow(np.e,-2*pow(x,2))-(x/15)



dfdx = np.gradient(f,x)

print(max(dfdx))

plt.plot(x,f)
plt.plot(x,dfdx)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["f(x)","df/dx"])
plt.title("Q1 - f")
