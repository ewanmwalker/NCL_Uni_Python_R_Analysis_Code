# -*- coding: utf-8 -*-
"""
Return factorial recursively

@author: c0081806
"""

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)
    
