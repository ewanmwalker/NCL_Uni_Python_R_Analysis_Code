# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:10:54 2023

@author: Super Warrior
"""

def bisection(f,xd,xu,eps):
    
    if f(xd)*f(xu) > 0:
        raise ValueError("The function has the same sign at the lower and upper bound")

    n = 0

    while abs(xu - xd) > eps:

        # find xmid
        xmid = (xd+xu)/2

        # Evaluate at xmid. If it's larger than zero move the upper bound down
        if f(xmid) > 0:
            xu = xmid
        # else move the lower bound up
        else:
            xd = xmid
        
        n += 1

    return xmid, n

r,n = bisection(lambda x : x**2 - 2,1,2,1e-10)
print("root found at {} after {} iterations".format(r,n))
