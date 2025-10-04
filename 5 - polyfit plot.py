# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:45:15 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(2002,2021)
y = np.array([5165,3567,4390,4852,5760,6203,5879,4149,5189,5863,5682,6277,6510,6749,6084,7099,7534,6734,6975])

fit = np.polyfit(t,y,deg=1)

plt.xticks([2002,2005,2010,2015,2020])
plt.plot(t,y,'-o',label="Year opening price")
plt.plot(t,np.polyval(fit,t),'--', label="Best fit line")
plt.xlabel("Year")
plt.ylabel("Index Value")
plt.title("Year opening value for the GTSE 100 Share Index")
plt.legend(loc=4)

#b
dydt = np.gradient(y)