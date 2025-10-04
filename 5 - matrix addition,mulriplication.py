# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:06:49 2023

@author: Super Warrior
"""
import numpy as np

A = np.array([[17,4],
              [26,13]])

B = np.array([[10,0],
              [7,6]])

x = A + B

#b

C = np.array([[17,4],
              [26,13],
              [10,0]])

D = np.array([[7,6,26],
              [27,28,30]])

x = C @ D