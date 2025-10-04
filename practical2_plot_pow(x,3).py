# -*- coding: utf-8 -*-
"""


@author: c0081806
"""

import numpy as np
import matplotlib.pyplot as plt

#Axes plots
x=np.linspace(-5,5,10)
y=pow(x,3)

plt.xlabel('x')
plt.ylabel('f(x)')

plt.plot(x,y,'--o')