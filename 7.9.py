# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:15:40 2023

@author: Super Warrior
"""

import numpy as np
from scipy import integrate

def func(x):
    return (x * np.exp(-(x**0.8))) + 0.2

myint = integrate.quad(func, 0, 8)

print(myint)