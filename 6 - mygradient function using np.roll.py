# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:54:36 2023

@author: Super Warrior
"""
import numpy as np

def mygradient(f, h = 1):
    n = len(f)

    dfdx = (np.roll(f,-1)-np.roll(f,1))/(2*h)
    dfdx[0] = (-3*f[0]+4*f[1]-f[2])/(2*h) # right-sided
    dfdx[n-1] = (3*f[n-1]-4*f[n-2]+f[n-3])/(2*h) # left-sided
 
    return dfdx 