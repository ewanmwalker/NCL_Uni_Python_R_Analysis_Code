# -*- coding: utf-8 -*-
"""
Plotting while iteration of fn(n)

@author: c0081806
"""
import matplotlib.pyplot as plt

#Function
def fn(n):
    if n % 2 == 0:
        return n/2
    else:
        return ((3*n)+1)/2

######## Set n0

n=31

########

#Iterations of function from fn(n)
r=[]
while n != 1:
    r.extend([n])   
    n=fn(n)

#Plot
x=range(0,(len(r)))

plt.plot(x,r)
plt.xlabel("# of iterations i")
plt.ylabel("n")
plt.title("Plot showing the value of n for each iteration of fn(n) for \n fn(n)=n/2 if n is even or \n fn(n)=(3n+1)/2 if n is odd. \n when n0={}".format(r[0]))

    