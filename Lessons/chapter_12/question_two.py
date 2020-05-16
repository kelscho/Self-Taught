"""Create a Circle class with a method called area that calculates and returns
its area. Then create a circle object, call area on it, and print the result.
Use Python's pi function in the built in math module"""
import math




class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi
       
a_circle = Circle(4)
print(a_circle.calculate_area())