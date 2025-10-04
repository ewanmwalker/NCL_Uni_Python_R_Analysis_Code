# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:47:27 2021

@author: c0081806
"""
import numpy as np

A = np.random.randint(10,size=50)
B = np.random.randint(10,size=50)
C = np.zeros(50)

for x in range(0,50):
    if A[x] == B[x]:
        C[x] =A[x]
    elif A[x] > B[x]:
        C[x] =A[x]
    else:
        C[x] =B[x]

print(C)