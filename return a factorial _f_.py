# -*- coding: utf-8 -*-
"""
Return factorial

@author: c0081806
"""

def factorial(n):
    f = 1
    for m in range(1, n+1):
        f *= m
    return f
        
print (factorial(5))