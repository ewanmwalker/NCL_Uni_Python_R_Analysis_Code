# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:39:49 2023

@author: Super Warrior
"""
import numpy as np
import scipy.linalg as sla

A = np.array([[2,8,6,7],
              [4,9,8,6],
              [1,6,4,2],
              [6,0,1,2]])

eigenvalues, eigenvectors = sla.eig(A)

print(eigenvalues)

#b

S = A @ A.T

#c

values_S , vectors_S = sla.eig(S)
print(values_S)
print(vectors_S)