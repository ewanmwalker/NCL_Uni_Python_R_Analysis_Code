# -*- coding: utf-8 -*-
"""
Some functions to solve ODEs
"""

import numpy as np

def euler(f,y0,t):
    """
    Returns the solution y(t) for an initial 
    value problem dy/dt = f(y,t) for an array t 
    and initial value y0 using the Euler Method
    """

    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])

    return y


def rk4(f,y0,t):
    """
    Returns the solution y(t) for an initial 
    value problem dy/dt = f(y,t) for an array t 
    and initial value y0 using the Runge-Kutta Method
    """

    y = np.zeros(len(t))
    y[0] = y0

    for n in range(0, len(t)-1): 

        h = t[n+1]-t[n]
        k1 = f(y[n],t[n]) 
        k2 = f(y[n] + h * 0.5 * k1,t[n] + 0.5 * h) 
        k3 = f(y[n] + h * 0.5 * k2,t[n] + 0.5 * h) 
        k4 = f(y[n] + h * k3,t[n] + h) 

        # Update next value of y 
        y[n+1] = y[n] + (1.0 / 6.0)*h*(k1 + 2 * k2 + 2 * k3 + k4) 

    return y

def midpoint(f,y0,t):
  """
  Returns the solution y(t) for an initial
  value problem dy/dt = f(y,t) for an array t
  and initial value y0 using the Midpoint Method
  """

  y = np.zeros(len(t))
  y[0] = y0

  # Complete the function below
  for n in range(len(y)-1):
      h = t[n+1] - t[n]  
      y[n+1] = y[n] + h*f(y[n] + h/2*f(y[n],t[n]),t[n]+h/2)

  return y