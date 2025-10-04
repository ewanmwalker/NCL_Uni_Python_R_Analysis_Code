# -*- coding: utf-8 -*-
"""
7.5 
Bisection method to find BOTH roots of eq
"""

def bisection(f,xd,xu,eps):

    """
    Bisection function - returns a root of function f
    in [xd,xu] with tolerance eps
    """

    if f(xd)*f(xu) > 0:
        raise ValueError("The function has the same sign at the lower and upper bound")

    while xu - xd > eps:

        # Evaluate the function at xmid. 
        xmid = (xd+xu)/2

        if f(xmid)*f(xu) > 0:
            xu = xmid
        else:
            xd = xmid

    return xmid

# Find the negative square root r1
r1 = bisection(lambda x: x**2 - 2,-2,-1,0.0000001)
print("r1 = {}".format(r1))

# Find the positive square root r2
r2 = bisection(lambda x: x**2 - 2,1,2,0.0000001)
print("r2 = {}".format(r2))
