# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:00:21 2022

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

r = np.array([57.9,108.3,149.6,227.9,778.6,1433.5,2872.5,4495.1,5906.4])
t = np.array([88.0,224.7,365.2,687.0,4331,10747,30589,59800,90560])

rl = np.log(r)
tl = np.log(t)

p = np.polyfit(rl,tl,1)
a = np.exp(p[1])

x1 = np.linspace(50,15000,10000)

p1 = np.polyfit(r,t,1)

y1 = a*pow(x1,p[0])

plt.plot(r,t,'x')
plt.plot(x1,y1)

v = 1.441e10/1e6
b = a*pow(v,p[0])
