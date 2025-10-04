# -*- coding: utf-8 -*-
"""
Assessment 2 

Q1e Trial and error version
"""
import numpy as np

x=[0]
B=[]


def Q1(p):

    for n in range (1,p):
        if  ((x[n-1] - n) in x) != True and (x[n-1] - n) > 0:
            x.append(x[n-1] - n)
        else:
            x.append(x[n-1] + n)
    
    #2)
    A=list(np.arange(0,max(x)))
    
    #3)
    for z in range (0,p):
        if  z in x != True:
            A.remove(z)
    
    for i in range(0,len(A)):
        B.append(A[i])

p=132

Q1(p)

