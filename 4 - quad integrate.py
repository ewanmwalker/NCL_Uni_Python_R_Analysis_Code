# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:39:00 2023

@author: Super Warrior
"""
from scipy import integrate

def f(x):
    return 1/(x**3 - 2*x - 5)

i = integrate.quad(f,0,5)
