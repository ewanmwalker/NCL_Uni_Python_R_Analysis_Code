# -*- coding: utf-8 -*-
"""
Plot of 10000 rolls of 3 dice

@author: c0081806
"""

#Import modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def r_dice_rolls(r):   #roll r number of dice
    
    t=np.zeros(r)
    for a in range(0,r):
        t[a] = np.random.randint(6)+1
    return sum(t)

def n_r_dice_rolls(n):  #n number of r rolled dice
    
    if r > 0 and type(r) == int and n>0 and type(n) == int:
        b = np.zeros(n)
        
        for s in range(0,n):
            b[s] = r_dice_rolls(r)
        x.append(b)
        
    else:
        print("n and r have to be positive integers greater than 0")


######## Set r and n
r=3
n=10000
########

x=[]
n_r_dice_rolls(n)

#Plot Histogram
plt.hist(x,bins=12*r,align='mid',)
plt.title("A histogram of the resultant integer when {} dice rolled \n {} times.".format(r,n))
plt.xlabel("Resultant integer")
plt.ylabel("# of times the integer is rolled")
plt.xticks(np.arange(0,7*r+1))

#Plot Bell Curve - set for r=3, n=10000 needs generalising
x_axis = range(r,6*r+1)
mean = np.mean(x_axis)
sd = np.std(x_axis)
y_axis = r**0.66*n*norm.pdf(x_axis, mean, sd)-(150*r)

plt.plot(x_axis, y_axis, color="black")
  








