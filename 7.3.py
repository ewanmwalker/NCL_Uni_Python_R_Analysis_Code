# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:40:39 2023

@author: Super Warrior
"""
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 1, 4, 9, 16, 25, 36, 49]

dydx = np.gradient(y, edge_order = 2)