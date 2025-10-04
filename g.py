# -*- coding: utf-8 -*-
"""
Assignment 2

g

note not complete at all!
"""
import numpy as np


#lower and upper bounds
l = 1.3
u = 1.7

#Finding the roots using np.roots
def f(x):
    return x**4 - 3*x**3 - 10*x**2 + 4*x + 1

p = [1,-3,-10,4,1] 
roots = np.sort(np.roots(p))

#Finding where the NR method doesn't find the closest root to the guess
z = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
m = []


def newraph(g,dfdx,x0,eps):

    x = x0
    n = 0

    while abs(g(x)) > eps:
        x = x - g(x)/dfdx(x)
        n += 1      
    return x, n


#Set y to be the array of all roots for each x0 from z
for i in range(0, len(z)):

    r,n = newraph(lambda x : x**4 - 3*x**3 - 10*x**2 + 4*x + 1, 
                  lambda x : 4*x**3 - 9*x**2 - 20*x + 4, 
                  z[i], 
                  1e-10)
    y[i] = r
    
    
#Finding which roots are not the closest root
for i in range(0, len(z)):
    
    x0 = abs (z[i] - roots[0])
    x1 = abs (z[i] - roots[1])
    x2 = abs (z[i] - roots[2])
    x3 = abs (z[i] - roots[3])
    
    y0 = abs (y[i] - roots[0])
    y1 = abs (y[i] - roots[1])
    y2 = abs (y[i] - roots[2])
    y3 = abs (y[i] - roots[3])
    
    

#Finding the root for the specific x value
import numpy as np

l = -5
u = 3.0808

def hybrid(f,l,u,eps):
    
        n = 0
        
        while abs(f(u) - f(l)) > eps:
    
            x = u - f(u) * (( u-l ) / ( f(u) - f(l) ))
            
            if f(u)*f(x) > 0:
                u = x
            else:
                l = x
            
            n += 1
        
        return x,n

r,n = hybrid(lambda x : x**4 - 3*x**3 - 10*x**2 + 4*x + 1, 
          l,
          u,
          1e-10)

print(r)
print(n)