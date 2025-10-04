# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:51:42 2022

@author: Super Warrior
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data_to_fit.csv',delimiter=',')

x = data[:,0]
y = data[:,1]

p = np.polyfit(x,1/y,1)
x1 = np.linspace(1,10,50)

f = 1/np.polyval(p,x1)

S = sum(pow(f-y,2))

plt.plot(x1,f)
plt.plot(x,y,'x')