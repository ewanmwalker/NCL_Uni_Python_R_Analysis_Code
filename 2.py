# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:13:48 2023

@author: Super Warrior
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import scipy.linalg as sla

A = np.array([[3,0,4],
              [1,3,1],
              [9,0,4]])

b = np.array([3,4,4])

x = sla.inv(A) * b

#c
y = sparse.diags([-1,range(1,16),0,1],[-1,0,1,2],[15,15]).toarray()

#print(neighbouring(y,1,1))

#d
def neighbouring(A,i,j):
    
    if i == 0:
        A = np.roll(A,1,axis=0)
        i = i + 1
    
    if i == A.shape[0]:
        A = np.roll(A,-1,axis=0)
        i = i - 1
    
    if j == 0:
        A = np.roll(A,1,axis=1)
        j = j + 1 
        
    if j == A.shape[1]:
        A = np.roll(A,-1,axis=1)
        j = j - 1
    
    return A[i-1:i+2,j-1:j+2]

print(neighbouring(y,0,0))