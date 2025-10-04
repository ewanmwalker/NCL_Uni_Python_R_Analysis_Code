# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:04:49 2023

@author: Super Warrior
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t, b, c, d):
    S, E, I, R = y 
    dSdt = -b*I*S
    dEdt = b*I*S - d*E
    dIdt = d*E - c*I 
    dRdt = c*I
    
    return [dSdt, dEdt, dIdt, dRdt] 

# Parameters
b = 0.02
c = 0.2
d = 0.5

# Initial conditions
y0 = [999,1,0,0]

# Time points
t = np.linspace(0,20,1000)

# Solve ODE
y = odeint(model,y0,t,args=(b,c,d))

plt.plot(t,y)
plt.legend(['S(t)','E(t)','I(t)','R(t)'])
plt.xlabel('t')
plt.title('SIR Model')