# -*- coding: utf-8 -*-
"""
Plotting x, pow(x,2) and pow(x,3)

@author: c0081806
"""

#Import required modules
import numpy as np
import matplotlib.pyplot as plt

#X axis value range
x=np.linspace(-2,2,50)

#y axis definitions
fx=x
gx=pow(x,2)
hx=pow(x,3)

#Labels
plt.xlabel('x')
plt.title('Plot of x, $x^2$ and $x^3$')
plt.legend(['f(x)=x','g(x)=$x^2$','h(x)=$x^3$'],loc=4)

#Plot
plt.plot(x,fx)
plt.plot(x,gx)
plt.plot(x,hx,'--o')
