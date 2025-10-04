# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:07:18 2023

@author: Super Warrior
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(u, t, a, b, c, d):
    x, y = u              # reads in u and assigns to x and y
    dxdt = a*x-b*x*y   # rhs of dx/dt
    dydt = d*x*y-c*y   # rhs of dy/dt 
    return [dxdt, dydt]   # important: this way around!

# Parameters
a = 2/3
b = 4/3
c = 1
d = 1

#plt.plot(t,u)
#plt.legend(['Prey, x(t)','Predator, y(t)'])
#plt.xlabel('t')
#plt.title('Predator-Prey Model')

for n in range(1*2,5*2):
    u0 = [n/2,n/2]
    # Time points
    t = np.linspace(0,50,1000)

    # Solve ODE
    u = odeint(model,u0,t,args=(a,b,c,d))

    # Phase plot
    plt.plot(u[:,0],u[:,1])
    # Start value
    plt.plot(u0[0],u0[1],'o',markersize=10)
    plt.xlabel("Prey population")
    plt.ylabel("Predator population")
    axes=plt.gca()
    axes.set_aspect(1)