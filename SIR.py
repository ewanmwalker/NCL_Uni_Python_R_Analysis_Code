# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:04:49 2023

@author: Super Warrior
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t, b, c):
    S, I, R = y # reads in values in y and assigns to S and I
    dSdt = -b*I*S # rhs of dS/dt
    dIdt = b*I*S - c*I # rhs of dI/dt 
    dRdt = c*I # rhs of dI/dt
    
    return [dSdt, dIdt, dRdt] # important that they are this way round!

# Parameters
b = 0.002
c = 0.5

# Initial conditions
y0 = [999,1,0]

# Time points
t = np.linspace(0,20,1000)

# Solve ODE
y = odeint(model,y0,t,args=(b,c))

plt.plot(t,y)
plt.legend(['S(t)','I(t)','R(t)'])
plt.xlabel('t')
plt.title('SIR Model')