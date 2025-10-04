# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q5
"""
import numpy as np
import matplotlib.pyplot as plt

#b
n = np.arange(1,16,2)
a = pow(-1,(n-1)/2)/pow(n,2)

#e/f
x = np.linspace(0,20,250)
m=1
o=3
p=15

zm=int((m+1) / 2)
zo=int((o+1) / 2)
zp=int((p+1) / 2)

f1 = (a[zm-1]) * np.sin(n[zm-1]+np.pi*x) / 10
f3 = (a[zo-1] * np.sin(n[zo-1]+np.pi*x) / 10)
f15 = (a[zp-1] * np.sin(n[zp-1]+np.pi*x) / 10)

#g - plot
plt.plot(x,f1)
plt.plot(x,f3)
plt.plot(x,f15)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["m=1","m=3","m=15"])
plt.title("Q5 - g: Plot illustrating that as m increases, f(x) tends towards a \n set value (0) with a lesser magnitude of oscilations")


#I ran out of time trying to solve the summation. Kept getting:
#'numpy.float64' object is not iterable
#Could I have made all f1,f3,f5... and then summed seperately?
#Please offer feedback on this. Thanks
