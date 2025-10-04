# -*- coding: utf-8 -*-
"""
Assignment 2

d
"""

def sec_roots(f,x0,x1,eps):
    
        n = 0
        
        while abs(f(x1) - f(x0)) > eps:
    
            x = x1 - f(x1) * (( x1-x0 ) / ( f(x1) - f(x0) ))
            
            x0 = x1
            x1 = x
            n += 1
        
        print(x)
        print(n)
        
        return x,n

sec_roots(lambda x : x**5 - 2*x**4 - 10*x**3 + 18*x**2 +10*x - 12, 
          1.3,
          1.7,
          1e-10)