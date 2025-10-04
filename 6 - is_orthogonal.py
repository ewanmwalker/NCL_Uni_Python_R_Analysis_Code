# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 00:04:54 2023

@author: Super Warrior
"""

import numpy as np
# Create your function below
def is_orthogonal(A,B):
    if np.dot(A,B) < 1e-8:
        return True
    else:
        return False