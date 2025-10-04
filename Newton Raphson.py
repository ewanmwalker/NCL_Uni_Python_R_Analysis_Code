# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:38:51 2023

@author: Super Warrior
"""
import numpy as np

def newraph(f,dfdx,x0,eps):

    x = x0
    n = 0

    while abs(f(x)) > eps:
        x = x - f(x)/dfdx(x)
        n += 1      
    return x, n


r,n = newraph(lambda x : np.sin(x), lambda x : np.cos(x), 3, 1e-10)
print("root found at {} after {} iterations".format(r,n))