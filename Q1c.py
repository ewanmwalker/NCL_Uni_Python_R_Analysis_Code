# -*- coding: utf-8 -*-
"""
Assessment 2 

Q1c - plot but with semicircular jumps
"""
#Modules
import numpy as np
import matplotlib.pyplot as plt

######Generating sqeuence
x=[0]

for n in range(1,30):
    if  ((x[n-1] - n) in x) != True and (x[n-1] - n) > 0:
        x.append(x[n-1] - n)
    else:
        x.append(x[n-1] + n)


###### Plotting as an alternating semicircle
#Need to satisfy equation y=sqrt(r^2-(x-a)^2)+b
b=0

for h in range (1,len(x)):
    j = round(h/2)       #half of the element number
    
    C=[]
    n=x[h]
    m=x[h-1]
    
    if n > m:           #Setting the centre from largest of 2 values
        r=(n-m)/2
        a=n-r 
        P=np.linspace(m,n,(n-m)*10)
    else:
        r=(m-n)/2
        a=m-r
        P=np.linspace(n,m,(m-n)*100)
    
    for s in range(0,len(P)):
        C.append(np.sqrt(pow(r,2)-pow((P[s]-a),2))+b)
        
    if j%2 == 0:
        plt.plot(P,C)
    
    else:
        M=[]
        for t in range(0,len(C)):
            M.append(C[t]*(-1))
        plt.plot(P,M)



plt.plot(len(x),0)
plt.title("1C - Semi-circles of the sequence with diameters mod(n-m) with \n centres (0,r-m) or (0,r-n) for the largest of m n, where m=n-1")
plt.xlabel("n")
plt.ylabel("+-r")
plt.axhline(0, color="black")