# -*- coding: utf-8 -*-
"""
Week 8

Exercise 8.1 - enumeration sort timing
Plot for time taken for enumcount and enumsort
"""
import matplotlib.pyplot as plt
import time
import random

def enumcount(x):
    """
    Returns a list with a count of how many values 
    come before each element in x
    """
    n = len(x)
    c = [0 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if x[i] < x[j]:
                c[j] = c[j]+1
            else:
                c[i] = c[i]+1
    return c

def enumsort(x,c):
    if(len(x)!=len(c)):
        raise ValueError('c and x should be same length')

    n = len(x)
    xsorted = [0 for i in range(n)]
    for i in range(n):
        xsorted[c[i]] = x[i]

    return xsorted








# Set size of the list
m = 5000
Tc = []
Ts = []

for n in range(0,m+1,250):
    # c contains numbers 0 to n-1
    x = list(range(n))

    # Shuffle x
    random.shuffle(x)

    t0c = time.time()
    c = enumcount(x)
    t1c = time.time()
    
    t0s = time.time()
    y = enumsort(x,c)
    t1s = time.time()    

    # print the time
    time_diff_count = t1c - t0c
    time_diff_sort = t1s - t0s
    Tc.append(time_diff_count)
    Ts.append(time_diff_sort)
    
plt.plot(range(0,m+1,250),Tc)
plt.plot(range(0,m+1,250),Ts)
plt.xlabel("list size")
plt.ylabel("time taken /s")
plt.title("enumeration sort timing")
plt.legend(["enumcount","enumsort"])

               
    
               
    
               
    
               
    
               
    
               
    
               
    