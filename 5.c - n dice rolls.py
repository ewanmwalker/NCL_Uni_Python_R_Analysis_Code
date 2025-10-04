# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:08:02 2021

@author: c0081806
"""
import numpy as np

def dice_roll():
    x = np.random.randint(6)+1
    y = np.random.randint(6)+1
    return x+y

def dice_rolln(n):
    if n > 0 and type(n) == int:
        a=np.zeros(n)
        for x in range(0,n):
            a[x] = np.random.randint(6)+1
        return sum(a)
    else:
        return ("n has to be a positive integer greater than 0")
    
