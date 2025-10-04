# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:54:54 2023

@author: Super Warrior
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def f(x):
    return np.cos(3*x) * np.sin(2*x) - 0.2
    
x = np.linspace(-5,5,100)
plt.plot(x,f(x))

#function,initial guess
r = opt.fsolve(f,2.5)