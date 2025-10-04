# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:52:33 2022

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("mydata.csv" , delimiter = ',', skiprows=1)

print(len(data))

x = data[:,0]
y = data[:,1]

yl = np.log(y)

p = np.polyfit(x,yl,1)

x1 = np.linspace(0.5,20,100)
y1 = (np.exp(p[1]) * np.exp(p[0]*x1))

plt.plot(x,y,'x')
plt.plot(x1,y1)

plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(["Data points","Line of best fit model"])
plt.title("A plt.plot plot of the data t(x) with a modelled line of best fit")




#using plt.semilogy




Y = p[1] + p[0] * x1

#plt.semilogy(x1,Y,'x')
#plt.semilogy(x1,Y)

#plt.xlabel("t")
#plt.ylabel("x(t)")
#plt.legend(["Data points","Line of best fit model"])
#plt.title("A plt.semilogy plot of the data t(x) with a modelled line of best fit")
