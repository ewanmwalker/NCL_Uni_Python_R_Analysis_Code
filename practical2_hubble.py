# -*- coding: utf-8 -*-
"""
Plotting data from .txt file

@author: c0081806
"""

#Import required modules, data
import numpy as np
import matplotlib.pyplot as plt
data=np.genfromtxt("C:/Users/c0081806/OneDrive - Newcastle University/MAS1803-Python/Text-files/practical2_hubble.txt")

#X axis (distance)
d=data[:,0]

#Y axis (velocity)
v=data[:,1]

#Labels
plt.xlabel('Distance, d (Mpc)')
plt.ylabel('Recession Velocity, v (km/s)')
plt.title('Edwin Hubble\'s 1929 data on the recession velocity of galaxies')

#Plot
plt.plot(d,v,'x')