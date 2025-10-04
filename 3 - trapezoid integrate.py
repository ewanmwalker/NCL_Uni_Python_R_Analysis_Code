# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:33:37 2023

@author: Super Warrior
"""
import scipy.integrate as int

x = [ 0, 0.4, 0.8, 1.2, 1.6, 2 ]
y = [ 2, 3, 3, 5, 10, 8 ]

i = int.trapezoid(y,x)