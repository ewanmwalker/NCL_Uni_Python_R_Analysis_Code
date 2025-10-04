# -*- coding: utf-8 -*-
"""
Assignment 2

f (i)
"""

import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
m = []

###


def f(x):
    return x**4 - 3*x**3 - 10*x**2 + 4*x + 1

g = f(z)

p = [1,-3,-10,4,1] 
roots = np.sort(np.roots(p))

colours = ["blue","purple","green","orange"]

#plt.plot(z,g)
#plt.axis([-5.5,5.5,-100,100])
#plt.scatter(roots, np.zeros(len(roots)), c=colours, s=100)
#plt.xlabel("x")
#plt.ylabel("g(x)")
#plt.title("Plot of x^4 - 3x^3 - 10x^2 + 4^x + 1 with roots")


    
####


def newraph(g,dfdx,x0,eps):

    x = x0
    n = 0

    while abs(g(x)) > eps:
        x = x - g(x)/dfdx(x)
        n += 1      
    return x, n



for i in range(0, len(z)):

    r,n = newraph(lambda x : x**4 - 3*x**3 - 10*x**2 + 4*x + 1, 
                  lambda x : 4*x**3 - 9*x**2 - 20*x + 4, 
                  z[i], 
                  1e-10)
    y[i] = n
    
    if round(r) == round(roots[0]):
        m.append("blue")
    elif round(r) == round(roots[1]):
       m.append("purple")
    elif round(r) == round(roots[2]):
       m.append("green")
    else:
       m.append("orange")
    
for i in range(0, len(z)):

    plt.plot([z[i],z[i]],[0,y[i]],c=(m[i]))


plt.xlabel("Starting guess, x0")
plt.ylabel("Number of iterations, n")
plt.title("Newton-Raphson convergence for  x^4 - 3x^3 - 10x^2 + 4^x + 1")



