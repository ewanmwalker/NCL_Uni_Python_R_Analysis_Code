# -*- coding: utf-8 -*-
"""
n rolls of r dice

@author: c0081806
"""

import numpy as np

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







