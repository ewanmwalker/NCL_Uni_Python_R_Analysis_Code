# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:57:34 2022

@author: Super Warrior
"""

import numpy as np

n = np.arange(1,51)

x = []

for i in range(0,50):
    x.append( (n[i] * (n[i]+1) * (n[i]+2)  / 6 ) )
    