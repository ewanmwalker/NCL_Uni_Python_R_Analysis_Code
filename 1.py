# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.integrate import odeint

def f(x):
    return (x**3)/20 + 30*np.cos(x + 3/4) * np.sin(x + 1)

x = np.linspace(-7.5,10,200)

plt.plot(x,f(x))

#b
y = opt.fsolve(f,-7.5)

#c
h = 0.05

x = np.zeros(6)
x[0] = 0.8

def g(x):
    return ( f(x+h) - f(x)) / h

for n in range(0,4):
    x[n+1] = x[n] - f(x[n])/g(x[n])
    print(n)
    print(x[n+1])
    
    
    
    

#d
def root_find(f,x0,h,eps):
    
    x = x0
    n = 0
    
    while abs(f(x)) > eps:
        x = x + f(x) * h
        
        n = n +1
    
    return [x, n]


x0=0.8
eps = 1e-8
m = root_find(f,x0,h,eps)