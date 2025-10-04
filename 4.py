# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:34:27 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def model(y, t, b, c):
    S, I, R = y            
    dSdt = -b*I*S
    dIdt = b*I*S - c*I  
    dRdt = c*I
    
    return [dSdt, dIdt, dRdt]

# Parameters
b = 0.002
c = 0.5

# Initial conditions
y0 = [999,1,0]

# Time points
t = np.linspace(0,20,100)

# Solve ODE
y = odeint(model,y0,t,args=(b,c))

plt.plot(t,y[:,0],label='S(t)')   # y[:,0] contains S(t)
plt.plot(t,y[:,1],label='I(t)')   # y[:,1] contains I(t)
plt.plot(t,y[:,2],label='R(t)')   # y[:,1] contains I(t)
plt.legend()
plt.xlabel('t')
plt.title('SIR Model')