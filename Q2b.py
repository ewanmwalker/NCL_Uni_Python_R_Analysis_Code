# -*- coding: utf-8 -*-
"""
Assessment 2 

Q2b
"""

class Cuboid:
    
    def __init__(self, x, y, z): 
        self.x = x 
        self.y = y
        self.z = z

    def vol(self):
        return self.x * self.y * self.z
        
    def surface_area(self):
        return 2*(self.x*self.y + self.x*self.z + self.y*self.z)
    
    def perimeters(self):
        return sorted([2*(self.x+self.y), 2*(self.x+self.z), 2*(self.y+self.z)])
    
c= Cuboid(7,2,3)