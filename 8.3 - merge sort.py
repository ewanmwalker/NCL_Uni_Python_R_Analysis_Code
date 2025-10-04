# -*- coding: utf-8 -*-
"""
Week 8

Exercise 8.3 - merge sort
"""

def merge(x,y):
    """
    Combine the sorted lists x and y
    """
    i = 0
    j = 0
    k = 0
    
    z = [0 for i in range(len(x)+len(y))]

    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z[k] = x[i]
            i += 1
        else:
            z[k] = y[j]
            j += 1
        k += 1
            
    # Fill any remaining elements
    while i < len(x):
        z[k] = x[i]
        i += 1
        k += 1
 
    while j < len(y):
        z[k] = y[j]
        j += 1
        k += 1
                               
    return z 

def merge_sort(x):

    if len(x)>1:
        mid = round(len(x)/2)
        l = x[:mid]
        r = x[mid:]

        # Sort the left and right sides 
        xl = merge_sort(l)
        xr = merge_sort(r)

    else:
        return x

    return merge(xl,xr)

# Test your function
print(merge_sort([1,6,4,2,5,7,4,2,0]))