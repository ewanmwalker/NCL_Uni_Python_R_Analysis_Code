# -*- coding: utf-8 -*-
"""
Return arg of a complex number z
(radians)

@author: c0081806
"""

import numpy as np
def argz(z):
    a=np.arctan(z.imag/z.real)
    return a