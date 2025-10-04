# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:18:22 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rhs(N,t):
    dNdt = -N / 20
    return dNdt

N0 = 40

t = np.linspace(0,100,1000)

y = odeint(rhs,N0,t)

plt.plot(t,y)
plt.xlabel("t /seconds")
plt.ylabel("N(t) /grams")

#b
print(t[sum(y>20)])

#c
print(20 * np.log(2))
