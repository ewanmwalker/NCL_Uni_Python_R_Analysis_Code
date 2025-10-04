# -*- coding: utf-8 -*-
"""
Assessment 2 

Q1d
"""
import numpy as np
import matplotlib.pyplot as plt

x=[0]
A=[1]

def ratio(p):
    
    for n in range (1,p):
        if  ((x[n-1] - n) in x) != True and (x[n-1] - n) > 0:
            x.append(x[n-1] - n)
        else:
            x.append(x[n-1] + n)

    #2)
    A=list(np.arange(0,max(x)))

    #3)
    for z in range (1,p):
        if  z in x != True:
            A.remove(z)
            

