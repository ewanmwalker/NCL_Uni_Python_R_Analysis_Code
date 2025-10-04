# -*- coding: utf-8 -*-
"""
Return Modulus of complex

@author: c0081806
"""

import numpy as np
def modulusz(z):
    m = np.sqrt(pow(z.real,2)+pow(z.imag,2))
    return m
