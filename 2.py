"""
A surface plot
"""
import matplotlib.pyplot as plt
import numpy as np

# new figure
fig = plt.figure(figsize=(15,10))
plt.rcParams['font.size'] = 20

# 3d axes
ax = plt.axes(projection='3d')

# Create a meshgrid
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x, y)

Z = -pow(X,2) + Y/2

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap='seismic')

# Add a colorbar
fig.colorbar(surf, shrink=0.5)

# Axis labels - note applied to the axes in a 3D plot
ax.set_xlabel('x',labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('f(x,y)', labelpad=10)