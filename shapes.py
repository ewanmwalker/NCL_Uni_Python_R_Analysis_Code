# -*- coding: utf-8 -*-
"""
shapes

@author: c0081806
"""
import numpy as np
import matplotlib.pyplot as plt


class Circle:
    
    def __init__(self,r):
        self.r = r
        
    def area(self):
        return np.pi*pow(self.r,2)


class Rectangle: 
    """ Class for a Rectangle """

    def __init__(self, x, y):
        """
        Initialises the rectangle class
        """
        self.x = x
        self.y = y
        self.colour = "m"  # default colour magenta  

    def area(self):
        """
        Return the rectangle area
        """
        return self.x * self.y

    def perimeter(self):
        """
        Return the rectangle perimeter
        """
        return 2 * self.x + 2 * self.y

    def is_square(self):
        """
        Returns True if the rectangle is a square
        """
        return (self.x == self.y)

    def scale(self, s):
        """
        Scales both sides of the rectangle by s
        """
        self.x *= s
        self.y *= s

    def set_colour(self, col):
        """
        Sets the rectangle colour
        """
        self.colour = col

    def draw(self):
        """
        Draws a rectangle using matplotlib patches
        """
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        fig,ax = plt.subplots()
        rect = patches.Rectangle((0,0), self.x, self.y, color=self.colour)
        ax.add_patch(rect)
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        plt.axis('equal')
        plt.show()

    def outline(self):
        """
        Draws the outline of a rectangle
        """
        plt.plot([0,self.x],[0,0],self.colour)
        plt.plot([0,0],[0,self.y],self.colour)
        plt.plot([0,self.x],[self.y,self.y],self.colour)
        plt.plot([self.x,self.x],[0,self.y],self.colour)
        
        
class Cuboid:
    def __init__(self, w, h, l):
        self.width = w
        self.height = h
        self.length = l
    
    def volume(self):
        return self.width*self.length*self.height
    
    def surface_area(self):
        return 2*((self.width*self.length)+(self.width*self.height)+(self.length*self.height))
                  
    def is_cube(self):
        return (self.width==self.length==self.height)
    
    def is_square_cuboid(self):
        return (self.width==self.length or self.length==self.height or self.length==self.width)
    
    def scale(self,s):
        self.width *= s
        self.height *= s
        self.length *= s
    
    