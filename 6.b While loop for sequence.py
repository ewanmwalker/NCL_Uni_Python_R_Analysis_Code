# -*- coding: utf-8 -*-
"""
While loop for sequence

@author: c0081806
"""

#Function
def fn(n):
    if n % 2 == 0:
        return n/2
    else:
        return ((3*n)+1)/2

######## Set n

n=703

########

#Iterations of function from fn(n)
r=[]
while n != 1:
    r.extend([n])   
    n=fn(n)

print(len(r))
    