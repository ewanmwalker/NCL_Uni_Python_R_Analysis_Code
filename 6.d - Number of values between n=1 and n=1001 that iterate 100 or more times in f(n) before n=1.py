# -*- coding: utf-8 -*-
"""
Number of values between 0<n<1001 that iterate 100+ times
in f(n) before n=1

@author: c0081806
"""

#Function
def fn(n):
    if n % 2 == 0:
        return n/2
    else:
        return ((3*n)+1)/2

#Running code for varying n

x=[]
for n in range(1,1001):
    r=[]
    while n != 1:
        r.extend([n])   
        n=fn(n)
    if len(r) >= 100:
        x.extend([r[0]])
        
print(len(x))