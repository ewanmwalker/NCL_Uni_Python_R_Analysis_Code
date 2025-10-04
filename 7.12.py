# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:13:55 2023

@author: Super Warrior
"""

from scipy import integrate

def to_integrate(y, x):
    return x*y

result, abserr = integrate.dblquad(to_integrate, 0, 1, 0, lambda x: 1-2*x)
print(result)