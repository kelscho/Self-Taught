"""Create a triangle class with a method called area that calculates and returns
its area. Then create a Triangle object, call area on it, and print the result. """


class Triangle():
    def __init__(self, base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return self.height * self.base / 2

a_triangle = Triangle(10,20)
print(a_triangle.calculate_area())       