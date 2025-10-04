# -*- coding: utf-8 -*-

import numpy as np 

#Question 1A
a = 2
m = 13

k = np.arange(1,m+1)
a_k = a**k

a_k_modm = []
for x in range(0,m):
    if a_k[x] % m == 1:
        a_k_modm.append(x+1)
        
print("1A: order is {}".format(min(a_k_modm)))

#Question 1B
a = 5
m = 23

k = np.arange(1,m+1)
a_k = a**k

a_k_modm = []
for x in range(0,m):
    if a_k[x] % m == 1:
        a_k_modm.append(x+1)
        
print("1B: order is {}".format(min(a_k_modm)))

#Question 1C
a = 6
m = 37

k = np.arange(1,m+1)
a_k = a**k

a_k_modm = []
for x in range(0,m):
    if a_k[x] % m == 1:
        a_k_modm.append(x+1)
        
print("1C: order is {}".format(min(a_k_modm)))