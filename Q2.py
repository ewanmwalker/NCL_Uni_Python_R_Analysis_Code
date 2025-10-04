# -*- coding: utf-8 -*-
"""
Assessment 2 

Q2
"""
import matplotlib.pyplot as plt

#2B

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
    
c= Cuboid(1,2,3)


#----------------------------------------------------------
#2C

#Bow ribbon length
B=16

class Present(Cuboid):
    colour="purple"
    
    def __init__(self, x, y, z, colour):
        super().__init__(x, y, z)
        self.colour = colour

    def ribbon_all(self):
        return sum(super().perimeters())
        
    def ribbon_two(self):
        return sum((super().perimeters())[:2],B)
    
    def __repr__(self):
        return "{} cuboid present with dimensions 1cm x 2cm x 3cm".format(self.colour)
    

#p = Present(1,2,3,"blue")

#----------------------------------------------------------
#2D

L=[]
x=1
a=10

#Setting an array for [L1,L2]
for b in range(0,a):
    p=[x]
    
    p.append(b+1)
    L.append(p)

#Setting an array for [L1,L2,L3]
N=[]

def sol(m):
    v=m
    for c in range(0,a):
        j=[v]
        n=[]
        
        k=j[0]
        l=k[0]
        m=k[1]
        
        n.append(l)
        n.append(m)
        n.append(c+1)
        N.append(n)

for b in range(0,a):
    m=L[b]
    sol(m)
    
#Setting an array of ratios
Oa=[]
Ot=[]

for a in range(0,len(N)):
    j=N[a]
    
    k=j[0]
    l=j[1]
    m=j[2]
    
    P = Present(k,l,m,"blue")
    V = P.vol()
    
    Ra = P.ribbon_all()
    Rt = P.ribbon_two()
    
    oa= V / Ra
    ot= V / Rt
    
    Oa.append(oa)
    Ot.append(ot)

#Plotting 
X=range(0,len(Oa))

plt.plot(X,Oa,marker="o")
plt.plot(X,Ot,marker="o")
plt.xlabel("Element number")
plt.ylabel("Volume/ribbon length (unit^2)")
plt.legend(["ribbon_all","ribbon_two"])
plt.title("Graph showing the Volume:perimeters ratio for \n a number of sets of Present(x,y,x)")