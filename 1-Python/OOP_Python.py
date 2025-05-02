# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 08:24:35 2025

@author: vaish
"""

#Blueprintfor creating objects(a kind of template)
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def circumference(self):
        return 2*3.14*self.r
    def area(self):
        return 3.14*self.r*self.r
    
#creating an object of circle
a_circle=Circle(2.0, 2.0, 1.0)
b_circle=Circle(3.0, 3.0, 2.0)

#accessing data and method
print("Radius:",a_circle.r)
print("Circumference:",a_circle.circumference())
print("Area:",a_circle.area())

print("Radius:",b_circle.r)
print("Circumference:",b_circle.circumference())
print("Area:",b_circle.area())

#Encapsulation-Hiding internal
class Circle:
    def __init__(self,x,y,r):
        self.__x=x
        self.__y=y
        self.__r=r
    def get_radius(self):
        return self.__r
    def set_radius(self,r):
        if r>0:
            self.__r=r
        else:
            print("Invalid Radius")

#Usage
c2=Circle(1, 1, 3)
print(c2.get_radius())
c2.set_radius(10)
#Data is protected,direct access is avoided

#Inheritance-
#Base Class
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    
    def area(self):
        return 3.14*self.r**2
    
    def circumference(self):
        return 2*3.14*self.r
    
    def display_info(self):
        print(f"Centre: ({self.x},{self.y}),Radius: {self.r}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")
        
#Derived Class
class ColoredCircle(Circle):
    def __init__(self,x,y,r,color):
        super().__init__(x,y,r)
        self.color=color
    
    def display_info(self):
        super().display_info()
        print(f"Color:{self.color}")
        
#usage
c1=ColoredCircle(0, 0, 1, "red")
c1.display_info()

#Polymorphism-same method name works differently depending on the object
class Circle:
    def area(self):
        return "Calculating area of circle"

class Square:
    def area(self):
        return "Calculating area of square"

shapes=[Circle(),Square()]
for shape in shapes:
    print(shape.area())

#abstraction
from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod #@-decorator
    def area(self):
        pass
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2

c4=circle(4)
print("Area:",c4.area())
