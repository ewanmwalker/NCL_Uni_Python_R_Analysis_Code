# -*- coding: utf-8 -*-
"""
Assessment 2 

Q1a,b - Populate a list x with returns from a function
from n=1 to (including) 500
"""
import matplotlib.pyplot as plt

x=[0]

for n in range (1,501):
    if  ((x[n-1] - n) in x) != True and (x[n-1] - n) > 0:
        x.append(x[n-1] - n)
    else:
        x.append(x[n-1] + n)

z=x[0:101]

plt.plot(range(0,101),z,marker="o",linewidth=1)
plt.xlabel("n")
plt.ylabel("Xn")
plt.title("Sequence up to n=100")


