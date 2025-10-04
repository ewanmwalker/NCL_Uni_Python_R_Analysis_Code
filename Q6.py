# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q6
"""
def enumcount(x):
    n = len(x)
    c = [0 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if x[i] > x[j]:
                c[j] = c[j]+1
            else:
                c[i] = c[i]+1
    return c


x = [ 7, 6, 1, 4, 9, 2 ]
print(enumcount(x))